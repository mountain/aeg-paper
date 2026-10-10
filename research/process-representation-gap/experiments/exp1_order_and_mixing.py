#!/usr/bin/env python3
"""Experiment 1 -- order and mixing.

Contract: research/process-representation-gap/contracts/exp1-order-and-mixing.v1.json

Question (work plan section 6, 实验一): do the same endpoint, the same action
count, or the same single-action spectral summary preserve order and mixing?

Two declared instances, kept strictly apart:

* Instance N -- NATIVE.  A two-vessel exact-rational mixing plant whose literal
  ordered history is carried by ``process_geometry.process.history.ProcessWord``
  from the pinned checkout (pinned by sha256; a drift raises EXP1-PG-DRIFT).
  The plant is neither linear nor invertible: the capacity bound makes the
  transfer law piecewise linear in ``min`` over the rationals, and explicit
  colliding states show that the actions are not injective.  Nothing here is
  obtained by linearising a process.
* Instance D -- DOWNSTREAM OBSERVATION ONLY.  Two invertible non-commuting
  2x2 matrices over Q with the same characteristic polynomial, and a frozen
  rational vector on which the two orders AB and BA act differently.

Everything is exact: Python ints, ``fractions.Fraction``, strings and tuples.
No floating point appears in any witness, comparison or cost.

Run:

    python3 research/process-representation-gap/experiments/exp1_order_and_mixing.py
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import itertools
import sys
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(ROOT / "tools"))
import gapkit  # noqa: E402
from gapkit import Diagnostic, qtext, require  # noqa: E402

CONTRACT = ROOT / "contracts" / "exp1-order-and-mixing.v1.json"
FROZEN = ROOT / "contracts" / "FROZEN.sha256"
EVIDENCE = ROOT / "evidence" / "exp1-order-and-mixing.json"

SCHEMA = "aeg.process-representation-gap.exp1.v1"

# --------------------------------------------------------------------------
# pinned carrier
# --------------------------------------------------------------------------

PG_HISTORY_PATH = gapkit.sibling_file(
    "AEG_PROCESS_GEOMETRY_REPO", "src/process_geometry/process/history.py"
)
PG_HISTORY_SHA256 = "93e9dc4651f4cf70e2a0980c9fee8ea58cc15acbe89bc064861c37359652cc45"
PG_REPO = "mountain/process-geometry"
PG_COMMIT = "c47c96fa79123c677172278be59d67ca1cc891b1"

_PINNED = {"module": None, "sha256": None, "git_blob": None}

# --------------------------------------------------------------------------
# declared budgets
# --------------------------------------------------------------------------

ALPHABET_N = ("P", "R")
ALPHABET_D = ("A", "B")
INITIAL = (Fraction(1), Fraction(1))
MAX_NATIVE_LENGTH = 6
MAX_CONTINUATION_DEPTH = 3
MAX_DOWNSTREAM_LENGTH = 4
EXPLORATORY_DOWNSTREAM_LENGTH = 6
FROZEN_VECTOR = (Fraction(2), Fraction(1))

BUDGET = "BUDGET-EXHAUSTED"
UNDETERMINED = "NOT-DETERMINED-BY-SUMMARY"

# the declared probe families of the finite mixing-response candidate
PROBE_FAMILIES = {
    "M_C_1_nonempty": ("P", "R"),
    "M_C_2": tuple("".join(w) for w in gapkit.words(ALPHABET_N, 2)),
    "M_C_3": tuple("".join(w) for w in gapkit.words(ALPHABET_N, 3)),
}

# --------------------------------------------------------------------------
# hand-computed literal tables (entered as literals, re-derived below)
# --------------------------------------------------------------------------

# Plant state after each word of length <= 3 from s0 = (1, 1), derived by hand
# from the pour law, plus the two words of the witnesses and the positive
# control.  Example, PRR: P(1,1) = (1/2, 1); R(1/2,1) transfers
# min(1/2, 1-1/2) = 1/2 and gives (1, 1/2); R(1,1/2) transfers
# min(1/4, 1-1) = 0, spills the whole 1/4, and gives (1, 1/4).
HAND_PLANT = {
    "": ("1", "1"),
    "P": ("1/2", "1"),
    "R": ("1", "1/2"),
    "PP": ("1/4", "1"),
    "PR": ("1", "1/2"),
    "RP": ("1/2", "1"),
    "RR": ("1", "1/4"),
    "PPP": ("1/8", "1"),
    "PPR": ("3/4", "1/2"),
    "PRP": ("1/2", "1"),
    "PRR": ("1", "1/4"),
    "RPP": ("1/4", "1"),
    "RPR": ("1", "1/2"),
    "RRP": ("1/2", "3/4"),
    "RRR": ("1", "1/8"),
    "PPRR": ("1", "1/4"),
    "RPRR": ("1", "1/4"),
}

# Downstream instance, hand-computed.  Matrices are written as lists of
# rational strings; the composite of the word w is the matrix product in word
# order because matrices act on row vectors on the right.
HAND_MATRIX = {
    "A": {
        "matrix": [["1", "1"], ["0", "2"]],
        "trace": "3",
        "det": "2",
        "charpoly": ["1", "-3", "2"],
    },
    "B": {
        "matrix": [["0", "2"], ["-1", "3"]],
        "trace": "3",
        "det": "2",
        "charpoly": ["1", "-3", "2"],
    },
    "AB": {
        "matrix": [["-1", "5"], ["-2", "6"]],
        "trace": "5",
        "det": "4",
        "charpoly": ["1", "-5", "4"],
    },
    "BA": {
        "matrix": [["0", "4"], ["-1", "5"]],
        "trace": "5",
        "det": "4",
        "charpoly": ["1", "-5", "4"],
    },
}

# action of each hand-computed composite on the frozen vector v = (2, 1)
HAND_VECTOR_ACTION = {
    "A": ("2", "4"),
    "B": ("-1", "7"),
    "AB": ("-4", "16"),
    "BA": ("-1", "13"),
}

# the declared witnesses
GAP_LEFT = ("P", "R", "R")
GAP_RIGHT = ("R", "P", "R")
CONTROL_LEFT = ("P", "P", "R", "R")
CONTROL_RIGHT = ("R", "P", "R", "R")
SECONDARY_CONTROL_LEFT = ("P", "R")
SECONDARY_CONTROL_RIGHT = ("R", "P", "R")
CENTRAL_WORD = ("P", "R", "R")
DECLARED_SPECTRAL_WORDS = (("A", "B"), ("B", "A"))


# --------------------------------------------------------------------------
# pinned carrier loading
# --------------------------------------------------------------------------

def require_pin(observed, pinned, label):
    """The pinned-source obligation.  A drift is a blocker, not a warning."""
    require(
        observed == pinned,
        "EXP1-PG-DRIFT",
        f"{label}: observed {observed} != pinned {pinned}",
    )


def git_blob_sha1(raw: bytes) -> str:
    header = b"blob " + str(len(raw)).encode("ascii") + b"\0"
    return hashlib.sha1(header + raw).hexdigest()


def load_pinned_history():
    require(PG_HISTORY_PATH.exists(), "EXP1-PG-MISSING", str(PG_HISTORY_PATH))
    raw = PG_HISTORY_PATH.read_bytes()
    observed = gapkit.sha256_bytes(raw)
    require_pin(observed, PG_HISTORY_SHA256, PG_HISTORY_PATH.name)
    spec = importlib.util.spec_from_file_location(
        "exp1_pinned_process_history", PG_HISTORY_PATH
    )
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    _PINNED["module"] = module
    _PINNED["sha256"] = observed
    _PINNED["git_blob"] = git_blob_sha1(raw)
    return module


# --------------------------------------------------------------------------
# Instance N: the native mixing plant
# --------------------------------------------------------------------------

def transfer_and_spill(state, sigma):
    """Exact transferred volume and spilled volume of one declared pour.

    P pours half of U's content towards V; whatever does not fit into V is
    spilled.  R is the mirror image.  ``min`` is taken over exact rationals, so
    the capacity bound is a genuine non-linearity and it binds on the declared
    witnesses.  This is the computation path of the primary route: the state
    transition below is closed form, not a flux ledger.
    """
    u, v = state
    if sigma == "P":
        t = min(u / 2, 1 - v)
        return t, u / 2 - t
    if sigma == "R":
        t = min(v / 2, 1 - u)
        return t, v / 2 - t
    raise Diagnostic("EXP1-UNKNOWN-ACTION", repr(sigma))


def transition(state, sigma):
    u, v = state
    t, _spill = transfer_and_spill(state, sigma)
    if sigma == "P":
        return (u - u / 2, v + t)
    return (u + t, v - v / 2)


_STATE_CACHE = {}


def state_of(word):
    """Reached mixture state, interpreted through the pinned carrier type."""
    key = tuple(word)
    hit = _STATE_CACHE.get(key)
    if hit is None:
        module = _PINNED["module"]
        require(module is not None, "EXP1-PG-MISSING", "pinned history module")
        hit = module.interpret_history(module.ProcessWord(key), INITIAL, transition)
        _STATE_CACHE[key] = hit
    return hit


def advance(state, eta):
    for sigma in eta:
        state = transition(state, sigma)
    return state


def native_domain(max_length=MAX_NATIVE_LENGTH):
    return [tuple(w) for w in gapkit.words(ALPHABET_N, max_length)]


def continuation_family(depth=MAX_CONTINUATION_DEPTH):
    return [tuple(w) for w in gapkit.words(ALPHABET_N, depth)]


def action_counts(word):
    return (
        sum(1 for s in word if s == "P"),
        sum(1 for s in word if s == "R"),
    )


def state_key(state):
    return (qtext(state[0]), qtext(state[1]))


def step_relation(word):
    """(position, action, transferred, spilled) for each step of the history."""
    state = INITIAL
    out = []
    for index, sigma in enumerate(word):
        transferred, spilled = transfer_and_spill(state, sigma)
        out.append((index, sigma, qtext(transferred), qtext(spilled)))
        state = transition(state, sigma)
    return tuple(out)


def occurrence_word(word):
    return tuple((index, sigma) for index, sigma in enumerate(word))


# --------------------------------------------------------------------------
# declared representations (declared before any analysis was run)
# --------------------------------------------------------------------------

def key_pi0(word):
    np_, nr = action_counts(word)
    return (np_, nr, qtext(state_of(word)[0]))


def key_pi0_counts(word):
    np_, nr = action_counts(word)
    return (np_, nr)


def key_pi0_endpoint(word):
    return (qtext(state_of(word)[0]),)


def key_pi1_word(word):
    return tuple(word)


def make_response_key(family):
    def key(word):
        return tuple(state_key(state_of(word + tuple(probe))) for probe in family)

    return key


def key_pi3_prov(word):
    return step_relation(word)


def key_hist(word):
    return occurrence_word(word)


def update_pi0(value, sigma):
    # The action counts update; the endpoint readout is not a function of the
    # retained summary, so the declared abstract update is not determined.
    return UNDETERMINED


def update_pi0_counts(value, sigma):
    np_, nr = value
    if sigma == "P":
        return (np_ + 1, nr)
    return (np_, nr + 1)


def update_pi0_endpoint(value, sigma):
    return UNDETERMINED


def update_pi1_word(value, sigma):
    if len(value) >= MAX_NATIVE_LENGTH:
        return BUDGET
    return value + (sigma,)


def make_response_update(family):
    def update(value, sigma):
        probes = tuple(family)
        require("P" in probes and "R" in probes, "EXP1-RESPONSE-RECOVERY-FAILED",
                "the declared probe family must contain P and R to recover the state")
        u = 2 * Fraction(value[probes.index("P")][0])
        v = 2 * Fraction(value[probes.index("R")][1])
        successor = transition((u, v), sigma)
        return tuple(
            state_key(advance(successor, tuple(probe))) for probe in probes
        )

    return update


def update_pi3_prov(value, sigma):
    u, v = INITIAL
    for _index, action, transferred, spilled in value:
        t, s = Fraction(transferred), Fraction(spilled)
        if action == "P":
            u, v = u - t - s, v + t
        else:
            u, v = u + t, v - t - s
    transferred, spilled = transfer_and_spill((u, v), sigma)
    return value + ((len(value), sigma, qtext(transferred), qtext(spilled)),)


def update_hist(value, sigma):
    if len(value) >= MAX_NATIVE_LENGTH:
        return BUDGET
    return value + ((len(value), sigma),)


REPRESENTATIONS = [
    {
        "id": "pi0",
        "tier": "existing-summary",
        "label": "endpoint readout plus action counts",
        "key": key_pi0,
        "update": update_pi0,
        "update_doc": "counts increment by the unit vector; the endpoint readout is not retained, so no abstract update is determined",
        "declared_steps": lambda w: 1,
        "build_observations": lambda w: 1,
        "domain": "native",
    },
    {
        "id": "pi0_counts",
        "tier": "existing-summary",
        "label": "action counts only",
        "key": key_pi0_counts,
        "update": update_pi0_counts,
        "update_doc": "add the unit vector of the action",
        "declared_steps": lambda w: 1,
        "build_observations": lambda w: 0,
        "domain": "native",
    },
    {
        "id": "pi0_endpoint",
        "tier": "existing-summary",
        "label": "endpoint readout only",
        "key": key_pi0_endpoint,
        "update": update_pi0_endpoint,
        "update_doc": "the pour law cannot be applied to a state the summary does not retain",
        "declared_steps": lambda w: 1,
        "build_observations": lambda w: 1,
        "domain": "native",
    },
    {
        "id": "pi1_word",
        "tier": "bounded-enhancement",
        "label": "ordered word (bounded)",
        "key": key_pi1_word,
        "update": update_pi1_word,
        "update_doc": "append one symbol; total inside the declared budget",
        "declared_steps": lambda w: len(w) + 1,
        "build_observations": lambda w: len(w),
        "domain": "native",
    },
    {
        "id": "pi2_resp",
        "tier": "bounded-enhancement",
        "label": "finite mixing-response table, family M_C_1_nonempty",
        "key": make_response_key(PROBE_FAMILIES["M_C_1_nonempty"]),
        "update": make_response_update(PROBE_FAMILIES["M_C_1_nonempty"]),
        "update_doc": "recover (u, v) by the declared exact recovery law, apply the pour law, re-probe",
        "declared_steps": lambda w: len(PROBE_FAMILIES["M_C_1_nonempty"]),
        "build_observations": lambda w: len(PROBE_FAMILIES["M_C_1_nonempty"]),
        "domain": "native",
    },
    {
        "id": "pi2_resp_d2",
        "tier": "bounded-enhancement",
        "label": "finite mixing-response table, family M_C_2",
        "key": make_response_key(PROBE_FAMILIES["M_C_2"]),
        "update": make_response_update(PROBE_FAMILIES["M_C_2"]),
        "update_doc": "recover (u, v) by the declared exact recovery law, apply the pour law, re-probe",
        "declared_steps": lambda w: len(PROBE_FAMILIES["M_C_2"]),
        "build_observations": lambda w: len(PROBE_FAMILIES["M_C_2"]),
        "domain": "native",
    },
    {
        "id": "pi2_resp_d3",
        "tier": "bounded-enhancement",
        "label": "finite mixing-response table, family M_C_3",
        "key": make_response_key(PROBE_FAMILIES["M_C_3"]),
        "update": make_response_update(PROBE_FAMILIES["M_C_3"]),
        "update_doc": "recover (u, v) by the declared exact recovery law, apply the pour law, re-probe",
        "declared_steps": lambda w: len(PROBE_FAMILIES["M_C_3"]),
        "build_observations": lambda w: len(PROBE_FAMILIES["M_C_3"]),
        "domain": "native",
    },
    {
        "id": "pi3_prov",
        "tier": "bounded-enhancement",
        "label": "provenance and incidence relation",
        "key": key_pi3_prov,
        "update": update_pi3_prov,
        "update_doc": "replay the relation to recover the state, apply the pour law, append one record",
        "declared_steps": lambda w: 2 * len(w) + 1,
        "build_observations": lambda w: 2 * len(w),
        "domain": "native",
    },
    {
        "id": "hist",
        "tier": "full-history-upper-bound",
        "label": "full literal history with occurrence identity",
        "key": key_hist,
        "update": update_hist,
        "update_doc": "append one occurrence; upper-bound control only",
        "declared_steps": lambda w: 2 * len(w),
        "build_observations": lambda w: 2 * len(w),
        "domain": "native",
    },
]


# --------------------------------------------------------------------------
# Instance D: the downstream linear observation
# --------------------------------------------------------------------------

def mat_mul(left, right):
    return [
        [
            sum(left[i][k] * right[k][j] for k in range(2))
            for j in range(2)
        ]
        for i in range(2)
    ]


def mat_of_word(word):
    result = [[Fraction(1), Fraction(0)], [Fraction(0), Fraction(1)]]
    for sigma in word:
        result = mat_mul(result, HAND_MATRIX[sigma]["_matrix"])
    return result


def mat_trace(matrix):
    return matrix[0][0] + matrix[1][1]


def mat_det(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def mat_vec_row(vector, matrix):
    return tuple(
        sum(vector[i] * matrix[i][j] for i in range(2)) for j in range(2)
    )


def charpoly(matrix):
    return ["1", qtext(-mat_trace(matrix)), qtext(mat_det(matrix))]


def spectral_key(word):
    matrix = mat_of_word(word)
    return (qtext(mat_trace(matrix)), qtext(mat_det(matrix)))


def downstream_domain(max_length=MAX_DOWNSTREAM_LENGTH):
    return [tuple(w) for w in gapkit.words(ALPHABET_D, max_length)]


# --------------------------------------------------------------------------
# task-relative equivalence
# --------------------------------------------------------------------------

def task_separates(word_left, word_right, family):
    """First continuation, in declared order, whose observation differs.

    Returns None when the frozen family does not separate the two histories.
    """
    for depth in range(MAX_CONTINUATION_DEPTH + 1):
        for eta in family:
            if len(eta) != depth:
                continue
            left = advance(state_of(word_left), eta)
            right = advance(state_of(word_right), eta)
            if left != right:
                return {
                    "eta": "".join(eta),
                    "depth": depth,
                    "kind": "observation",
                    "left_readout": state_key(left),
                    "right_readout": state_key(right),
                }
    return None


def task_equivalent(word_left, word_right, family):
    return task_separates(word_left, word_right, family) is None


# --------------------------------------------------------------------------
# representation analysis
# --------------------------------------------------------------------------

def fibers(domain, keyfn):
    groups = {}
    for word in domain:
        groups.setdefault(keyfn(word), []).append(word)
    return groups


def analyse(rep, domain, family):
    keyfn = rep["key"]
    groups = fibers(domain, keyfn)
    task_classes = len(fibers(domain, lambda w: state_of(w)))
    # A summary refines the task equivalence exactly when every summary class
    # lies inside one task class.  Class counts alone do not decide this: pi0
    # has more classes than the task (95 > 49) and still merges two
    # task-inequivalent histories.
    refines = all(len({state_of(w) for w in words}) == 1 for words in groups.values())
    result = {
        "id": rep["id"],
        "tier": rep["tier"],
        "label": rep["label"],
        "domain": rep["domain"],
        "domain_size": len(domain),
        "classes_on_domain": len(groups),
        "task_classes_on_domain": task_classes,
        "refinement": (
            "equal-to-task" if refines and len(groups) == task_classes
            else "strictly-finer-than-task" if refines
            else "does-not-refine-task"
        ),
        "colliding_fibers": 0,
        "largest_fiber": 0,
        "sufficient": True,
        "sufficiency_witness": None,
        "declared_update": rep["update_doc"],
        "closed_update": True,
        "closed_update_witness": None,
    }

    best = None
    for value, words in sorted(
        groups.items(), key=lambda kv: (len(kv[1]), str(kv[0])), reverse=True
    ):
        if len(words) < 2:
            continue
        result["colliding_fibers"] += 1
        result["largest_fiber"] = max(result["largest_fiber"], len(words))
        if not result["sufficient"]:
            continue
        for left, right in itertools.combinations(
            sorted(words, key=lambda w: (len(w), w)), 2
        ):
            separation = task_separates(left, right, family)
            if separation is None:
                continue
            rank = (len(left) + len(right), max(len(left), len(right)), left, right)
            if best is None or rank < best[0]:
                best = (rank, separation, left, right, value)
    if best is not None:
        _rank, separation, left, right, value = best
        result["sufficient"] = False
        result["sufficiency_witness"] = {
            "summary_value": _show(value),
            "histories": ["".join(left), "".join(right)],
            "states": [state_key(state_of(left)), state_key(state_of(right))],
            "shortest_separating_continuation": separation,
        }

    # Closed abstract update in the sense of work-plan section 4.3: the
    # declared update must reproduce the summary of the successor from the
    # summary of the state alone.
    for word in domain:
        if len(word) >= MAX_NATIVE_LENGTH:
            continue
        for sigma in ALPHABET_N:
            successor = rep["update"](keyfn(word), sigma)
            if successor == UNDETERMINED:
                result["closed_update"] = False
                result["closed_update_witness"] = {
                    "kind": "update-not-determined-by-summary",
                    "history": "".join(word),
                    "summary_value": _show(keyfn(word)),
                    "action": sigma,
                    "successor_summary": _show(keyfn(word + (sigma,))),
                }
                break
            if successor == BUDGET:
                continue
            if successor != keyfn(word + (sigma,)):
                result["closed_update"] = False
                result["closed_update_witness"] = {
                    "kind": "same-summary-same-action-different-summary",
                    "history": "".join(word),
                    "summary_value": _show(keyfn(word)),
                    "action": sigma,
                    "declared_update_result": _show(successor),
                    "successor_summary": _show(keyfn(word + (sigma,))),
                }
                break
        if not result["closed_update"]:
            break
    return result


def _show(value):
    """JSON-able view of a summary value (tuples become lists)."""
    if isinstance(value, tuple):
        return [_show(v) for v in value]
    if isinstance(value, list):
        return [_show(v) for v in value]
    return value


def provenance_task_analysis(representations, domain):
    """Which candidates actually answer the declared secondary provenance task.

    Q_prov asks for the transferred and spilled volume of every single step.
    A candidate answers it only if two histories with the same summary can never
    have different provenance records.
    """
    results = {}
    for rep in representations:
        groups = fibers(domain, rep["key"])
        witness = None
        for value, words in sorted(
            groups.items(), key=lambda kv: (len(kv[1]), str(kv[0])), reverse=True
        ):
            if len(words) < 2:
                continue
            ordered = sorted(words, key=lambda w: (len(w), w))
            pair = None
            for left, right in itertools.combinations(ordered, 2):
                if step_relation(left) != step_relation(right):
                    pair = (left, right)
                    break
            if pair is not None:
                witness = pair
                break
        results[rep["id"]] = {
            "answers_provenance_task": witness is None,
            "witness": None if witness is None else {
                "histories": ["".join(witness[0]), "".join(witness[1])],
                "summary_value": _show(rep["key"](witness[0])),
                "provenance_left": _show(step_relation(witness[0])),
                "provenance_right": _show(step_relation(witness[1])),
            },
        }
    return results


def representation_cost(rep, domain, family):
    cost = gapkit.Cost()
    sizes = []
    build_observations = 0
    for word in domain:
        payload = rep["key"](word)
        cost.store(payload)
        cost.step(rep["declared_steps"](word))
        build_observations += rep["build_observations"](word)
        sizes.append(len(gapkit.canonical(payload).encode("utf-8")))
    task_observations = sum(len(eta) + 1 for _word in domain for eta in family)
    cost.observe(build_observations + task_observations)
    cost.verify(len(domain) * max(len(family), 1))
    return {
        "id": rep["id"],
        "cost": cost.as_record(),
        "representation_build_observations": build_observations,
        "task_observations": task_observations,
        "mean_storage_bytes_per_history": _q(sum(sizes), len(sizes)),
        "max_storage_bytes_per_history": max(sizes),
    }


def _q(numerator, denominator):
    return qtext(Fraction(numerator, denominator))


# --------------------------------------------------------------------------
# auxiliary declared checks
# --------------------------------------------------------------------------

def reachable_states(domain):
    """Distinct reachable states, in deterministic first-reached order."""
    seen = []
    for word in domain:
        state = state_of(word)
        if state not in seen:
            seen.append(state)
    return seen


def action_non_injectivity_witnesses(domain):
    """Distinct reachable states with the same image under one declared action.

    This is the declared reason why the plant is not a group action and cannot
    be a linearisation by invertible matrices.  It compares STATES, so a pair of
    words reaching the same state is not mistaken for a collision.
    """
    states = reachable_states(domain)
    witnesses = {}
    for sigma in ALPHABET_N:
        images = {}
        for state in states:
            images.setdefault(transition(state, sigma), []).append(state)
        collisions = sorted(
            (
                (image, members)
                for image, members in images.items()
                if len(members) > 1
            ),
            key=lambda kv: (kv[0][0] + kv[0][1], str(kv[0])),
        )
        if collisions:
            image, members = collisions[0]
            ordered = sorted(members, key=lambda st: (st[0] + st[1], str(st)))
            witnesses[sigma] = {
                "image": state_key(image),
                "distinct_states": [state_key(ordered[0]), state_key(ordered[1])],
            }
    return witnesses


def vessel_swap_conjugacy(domain):
    """S(u, v) = (v, u) must satisfy S(P(s)) = R(S(s)) exactly."""
    failures = []
    checked = 0
    for state in reachable_states(domain):
        swapped = (state[1], state[0])
        if (transition(swapped, "R")[1], transition(swapped, "R")[0]) \
                != transition(state, "P"):
            failures.append(state_key(state))
        checked += 1
    require(
        not failures,
        "EXP1-SWAP-CONJUGACY-FAILED",
        f"the vessel swap does not conjugate P and R on {failures[:3]}",
    )
    return {"checked_states": checked, "failures": failures}


def uncapped_variant_check(domain):
    """The declared SEPARATE variant without the capacity bound.

    P(u, v) = (u/2, v + u/2) and R(u, v) = (u + v/2, v/2).  Total volume is
    invariant, so the endpoint readout determines the state and no collision of
    the declared summary can exist.  Verified by enumeration on the domain and
    proved by the two-line conservation identity recorded in the evidence.
    """

    def uncapped(state, sigma):
        u, v = state
        if sigma == "P":
            return (u / 2, v + u / 2)
        return (u + v / 2, v / 2)

    states = {}
    totals_vary = False
    for word in domain:
        state = INITIAL
        for sigma in word:
            before = state[0] + state[1]
            state = uncapped(state, sigma)
            if state[0] + state[1] != before:
                totals_vary = True
        states[word] = state
    collisions = []
    for left, right in itertools.combinations(domain, 2):
        if key_pi0_uncapped(left, states) == key_pi0_uncapped(right, states) \
                and states[left] != states[right]:
            collisions.append(("".join(left), "".join(right)))
    return {
        "conservation_total_violations": 1 if totals_vary else 0,
        "total_is_invariant_on_domain": not totals_vary,
        "summary_collisions_with_distinct_states": len(collisions),
        "first_collision": list(collisions[0]) if collisions else None,
        "declared_states_checked": len(domain),
        "endpoint_determines_state": "v = 2 - u on the declared domain",
    }


def key_pi0_uncapped(word, states):
    np_, nr = action_counts(word)
    return (np_, nr, qtext(states[word][0]))


def response_recovery_law(domain, factor=2):
    """u = factor * first component of the P-probe response, and likewise for R."""
    failures = []
    for word in domain:
        state = state_of(word)
        u = factor * transition(state, "P")[0]
        v = factor * transition(state, "R")[1]
        if (u, v) != state:
            failures.append({"history": "".join(word), "recovered": [qtext(u), qtext(v)],
                             "state": state_key(state)})
    return failures


def check_hand_tables(plant_table, matrix_table, vector_table):
    """Obligations, not comments: the hand tables must be re-derivable."""
    for word, expected in sorted(plant_table.items()):
        observed = state_key(state_of(tuple(word)))
        require(
            observed == tuple(expected),
            "EXP1-HAND-TABLE-MISMATCH",
            f"plant state of {word!r} = {observed}, hand table says {tuple(expected)}",
        )
    for name, expected in sorted(matrix_table.items()):
        matrix = HAND_MATRIX[name]["_matrix"]
        require(
            [qtext(x) for row in matrix for x in row]
            == [x for row in expected["matrix"] for x in row],
            "EXP1-HAND-TABLE-MISMATCH",
            f"matrix {name} = {[[qtext(x) for x in row] for row in matrix]}",
        )
        require(
            qtext(mat_trace(matrix)) == expected["trace"],
            "EXP1-HAND-TABLE-MISMATCH",
            f"trace {name} = {qtext(mat_trace(matrix))}, hand table says {expected['trace']}",
        )
        require(
            qtext(mat_det(matrix)) == expected["det"],
            "EXP1-HAND-TABLE-MISMATCH",
            f"det {name} = {qtext(mat_det(matrix))}, hand table says {expected['det']}",
        )
        require(
            charpoly(matrix) == expected["charpoly"],
            "EXP1-HAND-TABLE-MISMATCH",
            f"charpoly {name} = {charpoly(matrix)}, hand table says {expected['charpoly']}",
        )
        require(
            tuple(qtext(x) for x in mat_vec_row(FROZEN_VECTOR, matrix))
            == tuple(vector_table[name]),
            "EXP1-HAND-TABLE-MISMATCH",
            f"action of {name} on {tuple(qtext(x) for x in FROZEN_VECTOR)}",
        )


def install_matrices():
    HAND_MATRIX["A"]["_matrix"] = [
        [Fraction("1"), Fraction("1")], [Fraction("0"), Fraction("2")]
    ]
    HAND_MATRIX["B"]["_matrix"] = [
        [Fraction("0"), Fraction("2")], [Fraction("-1"), Fraction("3")]
    ]
    HAND_MATRIX["AB"]["_matrix"] = mat_mul(
        HAND_MATRIX["A"]["_matrix"], HAND_MATRIX["B"]["_matrix"]
    )
    HAND_MATRIX["BA"]["_matrix"] = mat_mul(
        HAND_MATRIX["B"]["_matrix"], HAND_MATRIX["A"]["_matrix"]
    )


# --------------------------------------------------------------------------
# negative controls
# --------------------------------------------------------------------------

def _read_frozen():
    out = {}
    if FROZEN.exists():
        for line in FROZEN.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            digest, _, name = line.partition("  ")
            out[name.strip()] = digest.strip()
    return out


def require_contract_digest(name, digest, frozen):
    require(
        frozen.get(name, digest) == digest,
        "EXP-CONTRACT-DRIFT",
        f"{name}: frozen {frozen.get(name)!r} != actual {digest}",
    )


def negative_controls(domain, family, analyses, downstream, product_cache):
    controls = []
    frozen = _read_frozen()

    # 1. Contract drift.
    raw = CONTRACT.read_bytes()
    mutated = raw.replace(b'"version": "1"', b'"version": "2"')
    require(mutated != raw, "EXP1-CONTROL-BROKEN", "contract mutation did not apply")
    controls.append({
        "id": "contract-drift",
        "expected": "EXP-CONTRACT-DRIFT",
        "observed": gapkit.reject(
            lambda: require_contract_digest(
                CONTRACT.name, gapkit.sha256_bytes(mutated), frozen
            ),
            "EXP-CONTRACT-DRIFT",
        ),
    })

    # 2. Pinned carrier drift.
    controls.append({
        "id": "pinned-processword-drift",
        "expected": "EXP1-PG-DRIFT",
        "observed": gapkit.reject(
            lambda: require_pin("0" * 64, PG_HISTORY_SHA256, PG_HISTORY_PATH.name),
            "EXP1-PG-DRIFT",
        ),
    })

    # 3. A mutated hand table must break.
    def mutated_hand_table():
        table = dict(HAND_PLANT)
        np_, nr = action_counts(GAP_LEFT)
        require(
            (np_, nr) == (1, 2), "EXP1-CONTROL-BROKEN", "witness counts changed"
        )
        table["PRR"] = ("1", "1/8")
        check_hand_tables(table, HAND_MATRIX, HAND_VECTOR_ACTION)

    controls.append({
        "id": "hand-table-mutated",
        "expected": "EXP1-HAND-TABLE-MISMATCH",
        "observed": gapkit.reject(mutated_hand_table, "EXP1-HAND-TABLE-MISMATCH"),
    })

    # 4. Claiming that the declared summary separates the witness pair.
    def summary_separates():
        require(
            key_pi0(GAP_LEFT) != key_pi0(GAP_RIGHT),
            "EXP1-SUMMARY-COLLISION-MISSING",
            "the declared summary unexpectedly separates the witness pair",
        )

    controls.append({
        "id": "summary-collision-claim",
        "expected": "EXP1-SUMMARY-COLLISION-MISSING",
        "observed": gapkit.reject(summary_separates, "EXP1-SUMMARY-COLLISION-MISSING"),
    })

    # 5. Claiming that pi0 is task-sufficient.
    def pi0_sufficient():
        require(
            analyses["pi0"]["sufficient"],
            "EXP1-SUMMARY-SUFFICIENCY-REFUTED",
            "pi0 is not task-sufficient: "
            f"{analyses['pi0']['sufficiency_witness']['histories']} separate",
        )

    controls.append({
        "id": "pi0-sufficiency-claim",
        "expected": "EXP1-SUMMARY-SUFFICIENCY-REFUTED",
        "observed": gapkit.reject(pi0_sufficient, "EXP1-SUMMARY-SUFFICIENCY-REFUTED"),
    })

    # 6. Claiming that the declared spectral summary separates AB from BA.
    def spectral_separates():
        require(
            spectral_key(("A", "B")) != spectral_key(("B", "A")),
            "EXP1-SPECTRAL-SEPARATION-MISSING",
            "the declared spectral summary does not separate AB from BA",
        )

    controls.append({
        "id": "spectral-separation-claim",
        "expected": "EXP1-SPECTRAL-SEPARATION-MISSING",
        "observed": gapkit.reject(spectral_separates, "EXP1-SPECTRAL-SEPARATION-MISSING"),
    })

    # 7. Claiming that equal composite spectra imply equal actions.
    def spectral_sufficient():
        left, right = DECLARED_SPECTRAL_WORDS
        require(
            spectral_key(left) == spectral_key(right)
            and mat_vec_row(FROZEN_VECTOR, product_cache[left])
            == mat_vec_row(FROZEN_VECTOR, product_cache[right]),
            "EXP1-SPECTRAL-SUFFICIENCY-REFUTED",
            "equal composite spectra do not imply the same action on the frozen vector",
        )

    controls.append({
        "id": "spectral-sufficiency-claim",
        "expected": "EXP1-SPECTRAL-SUFFICIENCY-REFUTED",
        "observed": gapkit.reject(spectral_sufficient, "EXP1-SPECTRAL-SUFFICIENCY-REFUTED"),
    })

    # 8. Claiming that the uncapped linear variant has a collision.
    def uncapped_collides():
        require(
            downstream["uncapped_variant"]["summary_collisions_with_distinct_states"] > 0,
            "EXP1-CONSERVATION-CLAIM-REFUTED",
            "the uncapped variant conserves total volume, so the endpoint "
            "readout determines the state and no collision exists",
        )

    controls.append({
        "id": "uncapped-collision-claim",
        "expected": "EXP1-CONSERVATION-CLAIM-REFUTED",
        "observed": gapkit.reject(uncapped_collides, "EXP1-CONSERVATION-CLAIM-REFUTED"),
    })

    # 9. Claiming that the positive control pair is separated.
    def control_separated():
        require(
            not task_equivalent(CONTROL_LEFT, CONTROL_RIGHT, family),
            "EXP1-POSITIVE-CONTROL-REFUTED",
            "the declared positive control is task-equivalent, so the mixing "
            "task does not separate it",
        )

    controls.append({
        "id": "positive-control-claim",
        "expected": "EXP1-POSITIVE-CONTROL-REFUTED",
        "observed": gapkit.reject(control_separated, "EXP1-POSITIVE-CONTROL-REFUTED"),
    })

    # 10. Claiming a shorter gap pair exists.
    def shorter_gap():
        short = [w for w in domain if len(w) <= 2]
        found = None
        for left, right in itertools.combinations(short, 2):
            if key_pi0(left) == key_pi0(right) and state_of(left) != state_of(right):
                found = ("".join(left), "".join(right))
                break
        require(
            found is not None,
            "EXP1-MINIMALITY-REFUTED",
            "no pi0-colliding, task-separated pair exists with both words of "
            "length <= 2",
        )

    controls.append({
        "id": "minimality-claim",
        "expected": "EXP1-MINIMALITY-REFUTED",
        "observed": gapkit.reject(shorter_gap, "EXP1-MINIMALITY-REFUTED"),
    })

    # 11. Claiming that P is injective on the reachable state set.
    def plant_injective():
        # The claim tested is injectivity on STATES, so the check must compare
        # distinct states; two words reaching one state are not a collision.
        images = {}
        for state in reachable_states(domain):
            images.setdefault(transition(state, "P"), []).append(state)
        require(
            all(len(members) == 1 for members in images.values()),
            "EXP1-PLANT-INJECTIVITY-CLAIM-REFUTED",
            "P is not injective on the reachable state set",
        )

    controls.append({
        "id": "plant-injectivity-claim",
        "expected": "EXP1-PLANT-INJECTIVITY-CLAIM-REFUTED",
        "observed": gapkit.reject(plant_injective, "EXP1-PLANT-INJECTIVITY-CLAIM-REFUTED"),
    })

    # 12. A mutated recovery factor must break the recovery law.
    controls.append({
        "id": "response-recovery-mutation",
        "expected": "EXP1-RESPONSE-RECOVERY-FAILED",
        "observed": gapkit.reject(
            lambda: require(
                not response_recovery_law(domain, factor=3),
                "EXP1-RESPONSE-RECOVERY-FAILED",
                "the declared recovery factor must be 2, not 3",
            ),
            "EXP1-RESPONSE-RECOVERY-FAILED",
        ),
    })

    # 13. Route disagreement: one mutated plant value must be detected.
    def route_check():
        mutated_state = ("1", "1/8")
        require(
            state_key(state_of(GAP_LEFT)) == mutated_state,
            "EXP1-ROUTE-DISAGREEMENT",
            f"primary route says {state_key(state_of(GAP_LEFT))}, "
            f"mutated table says {mutated_state}",
        )

    controls.append({
        "id": "primary-independent-disagreement",
        "expected": "EXP1-ROUTE-DISAGREEMENT",
        "observed": gapkit.reject(route_check, "EXP1-ROUTE-DISAGREEMENT"),
    })

    # 14. Enumeration count.
    def wrong_count():
        observed = len([w for w in domain if len(w) == 3])
        require(
            observed == 7,
            "EXP1-ENUMERATION-MISMATCH",
            f"native words of length 3: {observed}, declared 7",
        )

    controls.append({
        "id": "enumerated-count-mismatch",
        "expected": "EXP1-ENUMERATION-MISMATCH",
        "observed": gapkit.reject(wrong_count, "EXP1-ENUMERATION-MISMATCH"),
    })
    return controls


# --------------------------------------------------------------------------
# main
# --------------------------------------------------------------------------

def run():
    require(CONTRACT.exists(), "EXP1-CONTRACT-MISSING", str(CONTRACT))
    contract_sha = gapkit.sha256_file(CONTRACT)
    frozen = _read_frozen()
    require_contract_digest(CONTRACT.name, contract_sha, frozen)

    install_matrices()
    require(PG_HISTORY_PATH.exists(), "EXP1-PG-MISSING", str(PG_HISTORY_PATH))
    module = load_pinned_history()
    pinned_sha = _PINNED["sha256"]

    domain = native_domain()
    family = continuation_family()
    down_domain = downstream_domain()

    # The hand tables are obligations, not comments.
    check_hand_tables(HAND_PLANT, HAND_MATRIX, HAND_VECTOR_ACTION)

    for length in range(MAX_NATIVE_LENGTH + 1):
        observed = len([w for w in domain if len(w) == length])
        require(
            observed == 2 ** length,
            "EXP1-ENUMERATION-MISMATCH",
            f"native words of length {length}: {observed}, declared {2 ** length}",
        )
    require(
        len(family) == 15,
        "EXP1-ENUMERATION-MISMATCH",
        f"continuation family size {len(family)}, declared 15",
    )

    # The declared witness pair and the positive control.
    require(
        key_pi0(GAP_LEFT) == key_pi0(GAP_RIGHT),
        "EXP1-SUMMARY-COLLISION-MISSING",
        "the declared witness pair no longer shares the declared summary",
    )
    require(
        state_of(GAP_LEFT) != state_of(GAP_RIGHT),
        "EXP1-SUMMARY-COLLISION-MISSING",
        "the declared witness pair no longer reaches different states",
    )
    gap_separation = task_separates(GAP_LEFT, GAP_RIGHT, family)
    require(
        gap_separation is not None,
        "EXP1-SEPARATION-MISSING",
        "the frozen mixing task does not separate the declared witness pair",
    )
    require(
        CONTROL_LEFT != CONTROL_RIGHT
        and state_of(CONTROL_LEFT) == state_of(CONTROL_RIGHT)
        and task_equivalent(CONTROL_LEFT, CONTROL_RIGHT, family),
        "EXP1-POSITIVE-CONTROL-REFUTED",
        "the declared positive control is not a distinct pair of task-equivalent histories",
    )
    require(
        state_of(SECONDARY_CONTROL_LEFT) == state_of(SECONDARY_CONTROL_RIGHT),
        "EXP1-POSITIVE-CONTROL-REFUTED",
        "the secondary control pair does not share a state",
    )

    # Response recovery law: obligation on the whole declared domain.
    recovery_failures = response_recovery_law(domain)
    require(
        not recovery_failures,
        "EXP1-RESPONSE-RECOVERY-FAILED",
        f"the declared recovery law fails on {len(recovery_failures)} histories",
    )

    # Minimality: exhaustive enumeration of all pairs of the declared domain.
    gap_pairs = []
    for left, right in itertools.combinations(domain, 2):
        if key_pi0(left) != key_pi0(right):
            continue
        if state_of(left) == state_of(right):
            continue
        gap_pairs.append((max(len(left), len(right)), len(left) + len(right),
                          "".join(left), "".join(right)))
    gap_pairs.sort()
    require(
        gap_pairs and gap_pairs[0][2] == "".join(GAP_LEFT)
        and gap_pairs[0][3] == "".join(GAP_RIGHT),
        "EXP1-MINIMALITY-REFUTED",
        f"the minimal pi0 gap pair is not the declared witness: {gap_pairs[:1]}",
    )
    shorter = [row for row in gap_pairs if row[0] <= 2]
    require(
        not shorter,
        "EXP1-MINIMALITY-REFUTED",
        f"a shorter pi0 gap pair exists: {shorter}",
    )
    all_gap_count = len(gap_pairs)

    analyses = {}
    costs = {}
    for rep in REPRESENTATIONS:
        analyses[rep["id"]] = analyse(rep, domain, family)
        costs[rep["id"]] = representation_cost(rep, domain, family)

    # Downstream instance: the spectral summary against the frozen vector.
    product_cache = {w: mat_of_word(w) for w in down_domain}
    spectral_rep = {
        "id": "pi_spectral",
        "tier": "existing-summary",
        "label": "single-action and composite spectral summary",
        "key": spectral_key,
        "update": None,
        "update_doc": "the declared update is the length law (trace, det) -> (2*trace - 1, 2*det), verified on the declared domain",
        "declared_steps": lambda w: len(w),
        "build_observations": lambda w: 0,
        "domain": "downstream",
    }
    spectral_analysis = analyse_spectral(spectral_rep, down_domain, product_cache)
    spectral_cost = representation_cost(spectral_rep, down_domain, [])

    left_word, right_word = DECLARED_SPECTRAL_WORDS
    require(
        spectral_key(left_word) == spectral_key(right_word),
        "EXP1-SPECTRAL-SEPARATION-MISSING",
        "the declared spectral summary separates the two orders",
    )
    action_left = mat_vec_row(FROZEN_VECTOR, product_cache[left_word])
    action_right = mat_vec_row(FROZEN_VECTOR, product_cache[right_word])
    require(
        action_left != action_right,
        "EXP1-SPECTRAL-SUFFICIENCY-REFUTED",
        "the two orders act identically on the frozen vector",
    )

    # Conjugacy: BA = A^(-1) (AB) A, checked exactly.
    inverse_a = inverse(HAND_MATRIX["A"]["_matrix"])
    conjugacy_left = mat_mul(mat_mul(inverse_a, product_cache[("A", "B")]),
                             HAND_MATRIX["A"]["_matrix"])
    require(
        conjugacy_left == product_cache[("B", "A")],
        "EXP1-CONJUGACY-MISMATCH",
        "A^(-1) (AB) A is not BA",
    )
    commutator = mat_mul(
        mat_mul(inverse_a, inverse(HAND_MATRIX["B"]["_matrix"])),
        product_cache[("A", "B")],
    )
    require(
        commutator != [[Fraction(1), Fraction(0)], [Fraction(0), Fraction(1)]],
        "EXP1-COMMUTATIVITY-CLAIM-REFUTED",
        "the declared actions commute",
    )

    # The declared spectral summary is a re-encoding of the word length here.
    trace_law = {}
    for length in range(MAX_DOWNSTREAM_LENGTH + 1):
        words = [w for w in down_domain if len(w) == length]
        keys = sorted({spectral_key(w) for w in words})
        require(
            keys == [(qtext(2 ** length + 1), qtext(2 ** length))],
            "EXP1-SPECTRAL-LAW-MISMATCH",
            f"length {length} spectral summary is {keys}",
        )
        trace_law[str(length)] = _show(keys[0])
    exploratory = {}
    for length in range(MAX_DOWNSTREAM_LENGTH + 1, EXPLORATORY_DOWNSTREAM_LENGTH + 1):
        words = [tuple(w) for w in gapkit.words(ALPHABET_D, length) if len(w) == length]
        keys = sorted({spectral_key(w) for w in words})
        exploratory[str(length)] = {
            "words": len(words),
            "spectral_summaries": _show(keys),
        }

    # Reserved verification family: downstream lengths 3 and 4, reported apart.
    reserved = {}
    for length in (3, 4):
        words = [w for w in down_domain if len(w) == length]
        buckets = {}
        for word in words:
            buckets.setdefault(spectral_key(word), []).append(word)
        separated = 0
        for _value, group in sorted(buckets.items()):
            for left, right in itertools.combinations(group, 2):
                if mat_vec_row(FROZEN_VECTOR, product_cache[left]) != \
                        mat_vec_row(FROZEN_VECTOR, product_cache[right]):
                    separated += 1
        reserved[str(length)] = {
            "words": len(words),
            "summary_classes": len(buckets),
            "largest_class": max(len(g) for g in buckets.values()),
            "same_summary_different_action_pairs": separated,
        }

    swap_conjugacy = vessel_swap_conjugacy(domain)
    uncapped = uncapped_variant_check(domain)

    # The declared endpoint-and-counts gap, stated with concrete values.
    gap_witness = {
        "pair": ["".join(GAP_LEFT), "".join(GAP_RIGHT)],
        "action_counts": _show(action_counts(GAP_LEFT)),
        "same_action_counts": action_counts(GAP_LEFT) == action_counts(GAP_RIGHT),
        "summary_value": _show(key_pi0(GAP_LEFT)),
        "same_declared_summary": key_pi0(GAP_LEFT) == key_pi0(GAP_RIGHT),
        "states": [state_key(state_of(GAP_LEFT)), state_key(state_of(GAP_RIGHT))],
        "totals": [
            qtext(state_of(GAP_LEFT)[0] + state_of(GAP_LEFT)[1]),
            qtext(state_of(GAP_RIGHT)[0] + state_of(GAP_RIGHT)[1]),
        ],
        "initial_total": qtext(INITIAL[0] + INITIAL[1]),
        "spill_paths": {
            "".join(GAP_LEFT): _show(step_relation(GAP_LEFT)),
            "".join(GAP_RIGHT): _show(step_relation(GAP_RIGHT)),
        },
        "shortest_distinguishing_continuation": gap_separation,
        "shorter_continuation_depth1_probe": {
            "P": [state_key(advance(state_of(GAP_LEFT), ("P",))),
                  state_key(advance(state_of(GAP_RIGHT), ("P",)))],
            "R": [state_key(advance(state_of(GAP_LEFT), ("R",))),
                  state_key(advance(state_of(GAP_RIGHT), ("R",)))],
        },
    }
    positive_control = {
        "pair": ["".join(CONTROL_LEFT), "".join(CONTROL_RIGHT)],
        "distinct_literal_histories": CONTROL_LEFT != CONTROL_RIGHT,
        "same_length": len(CONTROL_LEFT) == len(CONTROL_RIGHT),
        "action_counts": _show(action_counts(CONTROL_LEFT)),
        "same_action_counts": action_counts(CONTROL_LEFT) == action_counts(CONTROL_RIGHT),
        "summary_value": _show(key_pi0(CONTROL_LEFT)),
        "same_declared_summary": key_pi0(CONTROL_LEFT) == key_pi0(CONTROL_RIGHT),
        "state": state_key(state_of(CONTROL_LEFT)),
        "same_state": state_of(CONTROL_LEFT) == state_of(CONTROL_RIGHT),
        "task_equivalent": task_equivalent(CONTROL_LEFT, CONTROL_RIGHT, family),
        "note": ("distinct literal histories with the same declared summary that the "
                 "declared task genuinely cannot separate: an enhancement that "
                 "separated them would be over-refined for this task"),
    }
    secondary_control = {
        "pair": ["".join(SECONDARY_CONTROL_LEFT), "".join(SECONDARY_CONTROL_RIGHT)],
        "different_lengths": len(SECONDARY_CONTROL_LEFT) != len(SECONDARY_CONTROL_RIGHT),
        "summary_values": [_show(key_pi0(SECONDARY_CONTROL_LEFT)),
                           _show(key_pi0(SECONDARY_CONTROL_RIGHT))],
        "same_declared_summary": key_pi0(SECONDARY_CONTROL_LEFT)
        == key_pi0(SECONDARY_CONTROL_RIGHT),
        "state": state_key(state_of(SECONDARY_CONTROL_LEFT)),
        "task_equivalent": task_equivalent(SECONDARY_CONTROL_LEFT, SECONDARY_CONTROL_RIGHT, family),
        "note": ("a pair whose declared summaries DIFFER yet which the task cannot "
                 "separate, showing that summary inequality is not a semantic difference"),
    }

    spectral_witness = {
        "words": ["".join(left_word), "".join(right_word)],
        "matrices": {
            name: {"matrix": [[qtext(x) for x in row] for row in HAND_MATRIX[name]["_matrix"]],
                   "trace": HAND_MATRIX[name]["trace"],
                   "det": HAND_MATRIX[name]["det"],
                   "charpoly": HAND_MATRIX[name]["charpoly"]}
            for name in sorted(HAND_MATRIX)
        },
        "single_action_summaries": {name: _show(spectral_key((name,))) for name in sorted(ALPHABET_D)},
        "single_actions_share_spectral_summary": spectral_key(("A",)) == spectral_key(("B",)),
        "single_actions_differ_on_vector": mat_vec_row(FROZEN_VECTOR, product_cache[("A",)])
        != mat_vec_row(FROZEN_VECTOR, product_cache[("B",)]),
        "composite_summaries": [_show(spectral_key(left_word)), _show(spectral_key(right_word))],
        "same_composite_summary": spectral_key(left_word) == spectral_key(right_word),
        "frozen_vector": [qtext(x) for x in FROZEN_VECTOR],
        "computation_path": {
            "".join(left_word): [_show(tuple(qtext(x) for x in FROZEN_VECTOR)),
                                 _show(tuple(qtext(x) for x in mat_vec_row(FROZEN_VECTOR, HAND_MATRIX[left_word[0]]["_matrix"]))),
                                 _show(tuple(qtext(x) for x in action_left))],
            "".join(right_word): [_show(tuple(qtext(x) for x in FROZEN_VECTOR)),
                                  _show(tuple(qtext(x) for x in mat_vec_row(FROZEN_VECTOR, HAND_MATRIX[right_word[0]]["_matrix"]))),
                                  _show(tuple(qtext(x) for x in action_right))],
        },
        "action_on_frozen_vector": {
            "".join(left_word): _show(tuple(qtext(x) for x in action_left)),
            "".join(right_word): _show(tuple(qtext(x) for x in action_right)),
        },
        "conjugacy": {
            "identity": "B*A = A^(-1)*(A*B)*A",
            "A_inverse": [[qtext(x) for x in row] for row in inverse_a],
            "verified": conjugacy_left == product_cache[("B", "A")],
        },
        "commutator": [[qtext(x) for x in row] for row in commutator],
        "conclusion": ("the declared spectral summary is a conjugation invariant, so it "
                       "cannot separate AB from BA, while the declared frozen-vector task "
                       "does separate them"),
        "claim_scope": ("this refutes the CHOSEN spectral summary on the declared domain. "
                        "It does not refute richer spectral systems, and it makes no claim "
                        "about spectra outside 2x2 rational matrices with this observation."),
    }

    boundary = {
        "closed_for": (
            f"native words of length <= {MAX_NATIVE_LENGTH} with continuations of depth "
            f"<= {MAX_CONTINUATION_DEPTH}; downstream words of length <= {MAX_DOWNSTREAM_LENGTH}"
        ),
        "open": [
            "no claim about native words longer than the declared bound",
            "no claim that no bounded representation, no richer spectral system and no summary at all can serve the mixing task",
            "no claim that the plant action semigroup admits no linear representation; only that the declared actions are non-injective and that the instance is not derived from a linearisation",
            "the general trace law trace(composite of n actions) = 2^n + 1 is verified on the declared domain and in the labelled exploratory range, not proved",
            "adaptive selection of the next observation is not permitted by this contract version",
        ],
    }

    record = {
        "schema": SCHEMA,
        "contract": {
            "path": str(CONTRACT.relative_to(ROOT.parent.parent)),
            "sha256": contract_sha,
        },
        "environment": gapkit.environ(),
        "pinned_carrier": {
            "repository": PG_REPO,
            "commit": PG_COMMIT,
            "path": str(PG_HISTORY_PATH),
            "sha256": pinned_sha,
            "git_blob": _PINNED["git_blob"],
            "type": "process_geometry.process.history.ProcessWord",
            "loader": "importlib.util.spec_from_file_location on the pinned file path",
            "fields": list(module.ProcessWord.__dataclass_fields__),
            "interpretation": "interpret_history(ProcessWord, INITIAL, transition) with the caller-supplied pour law",
            "pin_check": "match",
        },
        "native_instance": {
            "alphabet": list(ALPHABET_N),
            "initial_state": state_key(INITIAL),
            "pour_law": [
                "P(u, v): t = min(u/2, 1 - v); transferred = t; spilled = u/2 - t; successor = (u/2, v + t)",
                "R(u, v): t = min(v/2, 1 - u); transferred = t; spilled = v/2 - t; successor = (u + t, v/2)",
            ],
            "legality": "total; no partial action and no INVALID outcome",
            "native_status": ("declared exact-rational mixing plant with caller-supplied semantics, "
                              "carried by the pinned ProcessWord; NOT native Adva execution"),
            "reachable_state_count": len(reachable_states(domain)),
            "cluster_classes_on_domain": len(fibers(domain, lambda w: state_of(w))),
            "non_injectivity_witnesses": action_non_injectivity_witnesses(domain),
            "vessel_swap_conjugacy": swap_conjugacy,
            "vessel_swap_isomorphism": ("the swap S(u, v) = (v, u) conjugates P and R exactly, so "
                                        "every single-action invariant preserved by the swap agrees "
                                        "on the two actions and cannot report which one occurred"),
        },
        "uncapped_variant": uncapped,
        "downstream_instance": {
            "convention": "matrices act on row vectors on the right; the composite is the product in word order",
            "frozen_vector": [qtext(x) for x in FROZEN_VECTOR],
            "status": "downstream observation only",
            "spectral_summary": "sigma(M) = (trace(M), det(M))",
            "spectral_summary_is_a_length_encoding": trace_law,
        },
        "domain": {
            "native_size": len(domain),
            "native_by_length": {
                str(n): len([w for w in domain if len(w) == n])
                for n in range(MAX_NATIVE_LENGTH + 1)
            },
            "native_words": ["".join(w) for w in domain],
            "continuation_family": ["".join(eta) for eta in family],
            "continuation_depth": MAX_CONTINUATION_DEPTH,
            "downstream_size": len(down_domain),
            "downstream_words": ["".join(w) for w in down_domain],
        },
        "hand_table_check": {
            "plant": {word: _show(state_key(state_of(tuple(word)))) for word in sorted(HAND_PLANT)},
            "matrix": {name: HAND_MATRIX[name]["charpoly"] for name in sorted(HAND_MATRIX)},
            "vector_action": {name: _show(HAND_VECTOR_ACTION[name]) for name in sorted(HAND_VECTOR_ACTION)},
        },
        "witnesses": {
            "gap": gap_witness,
            "positive_control": positive_control,
            "secondary_control": secondary_control,
            "spectral": spectral_witness,
            "response_recovery_law": {
                "law": "u = 2 * first component of the response to P; v = 2 * second component of the response to R",
                "verified_on_histories": len(domain),
                "failures": recovery_failures,
            },
        },
        "minimality": {
            "method": "exhaustive enumeration of all pairs of the declared domain, ordered by (max length, total length, word, word)",
            "minimal_pair": [gap_pairs[0][2], gap_pairs[0][3]] if gap_pairs else None,
            "minimal_max_length": gap_pairs[0][0] if gap_pairs else None,
            "minimal_total_length": gap_pairs[0][1] if gap_pairs else None,
            "pairs_with_max_length_at_most_2": len(shorter),
            "gap_pairs_total": all_gap_count,
            "first_six_gap_pairs": _show(gap_pairs[:6]),
            "note": ("the enumeration is finite and exact; it does not upgrade into a general "
                     "minimality theorem for words beyond the declared bound"),
        },
        "representations": analyses,
        "downstream_spectral_analysis": spectral_analysis,
        "cost": costs,
        "cost_downstream": spectral_cost,
        "cost_accounting": {
            "storage_bytes": "canonical JSON size of the declared summary payload",
            "structural_size": "retained scalar fields counted by gapkit.Cost.store",
            "computation_steps": "declared per-history steps of the declared construction",
            "observations": "declared plant observations used to build the summary, plus the task observations over the whole domain and the frozen continuation family",
            "verification_cost": "domain size times continuation family size for every representation",
            "task_observations_per_domain_and_family": sum(
                len(eta) + 1 for _w in domain for eta in family
            ),
        },
        "secondary_task_analysis": {
            "Q_prov": "report the transferred and spilled volume of every step",
            "verdicts": provenance_task_analysis(REPRESENTATIONS, domain),
            "declared_query_cost": {
                "pi0": "cannot answer",
                "pi0_counts": "cannot answer",
                "pi0_endpoint": "cannot answer",
                "pi1_word": "replay the word under the declared pour law: |w| steps",
                "pi2_resp": "cannot answer: the mixture state does not determine the past",
                "pi2_resp_d2": "cannot answer: the mixture state does not determine the past",
                "pi2_resp_d3": "cannot answer: the mixture state does not determine the past",
                "pi3_prov": "one record lookup, no replay",
                "hist": "replay the history under the declared pour law: |w| steps",
            },
        },
        "reserved_verification_family": reserved,
        "exploratory_structural_check": {
            "label": "exploratory-beyond-declared-budget",
            "reason": ("the declared downstream enumeration budget is length <= 4; lengths 5 and 6 "
                       "are checked only to report the shape of the spectral length law and are "
                       "excluded from every declared verdict"),
            "lengths": exploratory,
        },
        "rewrites_used": {
            "appending-one-declared-action": "the only state transition used anywhere in this experiment",
            "processword-notation": "the literal words are carried as ProcessWord tuples; the notation change carries no semantics",
            "vessel-swap-relabelling": "used only to state and check the isomorphism that conjugates P and R; it changes no observation",
            "not-a-rewrite": [
                "the uncapped linear variant is a SEPARATELY declared model, not a rewrite of the declared plant: its results are reported under uncapped_variant and are never substituted into Instance N",
                "no forbidden rewrite listed in the contract is used: P and R are never commuted, occurrences are never identified, and no linearisation is substituted for the plant",
            ],
        },
        "claims": [
            {
                "id": "C1-summary-gap",
                "statement": "pi0(w) = (count_P, count_R, u) is not task-sufficient for the declared mixing task",
                "status": "bounded-domain-compatible",
                "scope": "all 127 native words of length <= 6, continuations of depth <= 3",
                "support": "cap 46 pi0-colliding pairs with distinct states; the pair (PRR, RPR) shares (1, 2, 1) and reaches (1, 1/4) versus (1, 1/2)",
            },
            {
                "id": "C2-witness-pair",
                "statement": "PRR and RPR have the same action counts, the same declared endpoint readout, and different states",
                "status": "proved",
                "scope": "the two declared words, exact arithmetic only",
                "support": "exact ledger of transfers and spills recorded in witnesses.gap.spill_paths",
            },
            {
                "id": "C3-counts-alone",
                "statement": "the action counts alone do not determine the mixture state",
                "status": "computationally-verified-example",
                "scope": "declared domain",
                "support": "PR and RP both have counts (1, 1) and reach (1, 1/2) versus (1/2, 1)",
            },
            {
                "id": "C4-endpoint-alone",
                "statement": "the endpoint readout alone does not determine the mixture state",
                "status": "computationally-verified-example",
                "scope": "declared domain",
                "support": "the empty word and R both have u = 1 and reach (1, 1) versus (1, 1/2)",
            },
            {
                "id": "C5-spectral-blindness",
                "statement": "the declared spectral summary cannot separate AB from BA, while the frozen-vector observation does",
                "status": "proved",
                "scope": "2x2 matrices over Q with the declared row-vector convention; A invertible with det 2",
                "support": "BA = A^(-1)(AB)A, so every conjugation invariant agrees; v*AB = (-4, 16) and v*BA = (-1, 13)",
            },
            {
                "id": "C6-single-action-spectra",
                "statement": "the two declared single actions have the same spectral summary (3, 2) and act differently on the frozen vector",
                "status": "proved",
                "scope": "the declared matrices A and B",
                "support": "v*A = (2, 4), v*B = (-1, 7)",
            },
            {
                "id": "C7-spectral-length-law",
                "statement": "on the declared downstream domain the spectral summary is a re-encoding of the word length: sigma(w) = (2^|w| + 1, 2^|w|)",
                "status": "bounded-domain-compatible",
                "scope": "downstream words of length <= 4; the labelled exploratory range extends to 6 and is excluded from every verdict",
                "support": "the determinant part is proved by multiplicativity of det and det A = det B = 2; the trace part is verified on the declared domain and in the exploratory range",
            },
            {
                "id": "C8-minimality",
                "statement": "the minimal pi0-colliding, task-separated pair is (PRR, RPR) with maximum length 3 and total length 6; no such pair exists with both words of length <= 2",
                "status": "bounded-domain-compatible",
                "scope": "exhaustive enumeration of all 8001 pairs of the declared 127-word domain",
                "support": "minimality block; 46 gap pairs in total",
            },
            {
                "id": "C9-nonlinearity-is-load-bearing",
                "statement": "in the separately declared uncapped variant total volume is invariant, so the endpoint readout determines the state and no gap of the declared form exists there",
                "status": "proved-with-stated-hypotheses",
                "scope": "the declared uncapped variant, all words of length <= 6",
                "support": "P: u/2 + (v + u/2) = u + v and R: (u + v/2) + v/2 = u + v; the declared witnesses spill (PRR ends at total 5/4 against the initial 2)",
            },
            {
                "id": "C10-minimal-repair",
                "statement": "the two-probe mixing-response pair is task-sufficient and realizes exactly the task equivalence (49 classes = 49 reachable states) with a closed declared update",
                "status": "bounded-domain-compatible",
                "scope": "declared domain and continuation family",
                "support": "representations.pi2_resp and the recovery law u = 2*(response to P).u, v = 2*(response to R).v, verified on all 127 histories",
            },
            {
                "id": "C11-over-refinement",
                "statement": "the ordered word and the provenance relation are sufficient but strictly finer than the task (127 classes against 49), so they separate histories the declared task declares equivalent",
                "status": "bounded-domain-compatible",
                "scope": "declared domain",
                "support": "the positive control PPRR versus RPRR is task-equivalent yet separated by both candidates",
            },
            {
                "id": "C12-non-injectivity",
                "statement": "the declared actions are not injective on the reachable state set",
                "status": "computationally-verified-example",
                "scope": "the 49 reachable states of the declared domain",
                "support": "explicit distinct states with equal images under P and under R",
            },
            {
                "id": "C13-no-general-claim",
                "statement": "nothing here is a general theorem about all words, all summaries, all spectra or all plants",
                "status": "open",
                "scope": "the declared domain only",
                "support": "boundary.open",
            },
        ],
        "negative_controls": negative_controls(
            domain, family, analyses, {"uncapped_variant": uncapped}, product_cache
        ),
        "boundary": boundary,
    }
    return record


def inverse(matrix):
    determinant = mat_det(matrix)
    require(
        determinant != 0,
        "EXP1-SINGULAR-MATRIX",
        f"matrix {[[qtext(x) for x in row] for row in matrix]} is singular",
    )
    return [
        [matrix[1][1] / determinant, -matrix[0][1] / determinant],
        [-matrix[1][0] / determinant, matrix[0][0] / determinant],
    ]


def analyse_spectral(rep, domain, product_cache):
    """Sufficiency of the declared spectral summary for the downstream task."""
    groups = {}
    for word in domain:
        groups.setdefault(spectral_key(word), []).append(word)
    task_classes = len(fibers(domain, lambda w: mat_vec_row(FROZEN_VECTOR, product_cache[w])))
    refines = all(
        len({mat_vec_row(FROZEN_VECTOR, product_cache[w]) for w in words}) == 1
        for words in groups.values()
    )
    result = {
        "id": rep["id"],
        "tier": rep["tier"],
        "label": rep["label"],
        "domain": "downstream",
        "domain_size": len(domain),
        "classes_on_domain": len(groups),
        "task_classes_on_domain": task_classes,
        "refinement": (
            "equal-to-task" if refines and len(groups) == task_classes
            else "strictly-finer-than-task" if refines
            else "does-not-refine-task"
        ),
        "colliding_fibers": 0,
        "largest_fiber": 0,
        "sufficient": True,
        "sufficiency_witness": None,
        "declared_update": rep["update_doc"],
        "closed_update": True,
        "closed_update_witness": None,
    }
    best = None
    for value, words in sorted(
        groups.items(), key=lambda kv: (len(kv[1]), str(kv[0])), reverse=True
    ):
        if len(words) < 2:
            continue
        result["colliding_fibers"] += 1
        result["largest_fiber"] = max(result["largest_fiber"], len(words))
        for left, right in itertools.combinations(
            sorted(words, key=lambda w: (len(w), w)), 2
        ):
            if mat_vec_row(FROZEN_VECTOR, product_cache[left]) == \
                    mat_vec_row(FROZEN_VECTOR, product_cache[right]):
                continue
            rank = (len(left) + len(right), max(len(left), len(right)), left, right)
            if best is None or rank < best[0]:
                best = (rank, left, right, value)
    if best is not None:
        _rank, left, right, value = best
        result["sufficient"] = False
        result["sufficiency_witness"] = {
            "summary_value": _show(value),
            "histories": ["".join(left), "".join(right)],
            "observations": [
                _show(tuple(qtext(x) for x in mat_vec_row(FROZEN_VECTOR, product_cache[left]))),
                _show(tuple(qtext(x) for x in mat_vec_row(FROZEN_VECTOR, product_cache[right]))),
            ],
        }
    # Declared abstract update: the length law of the spectral summary.
    for word in domain:
        if len(word) >= MAX_DOWNSTREAM_LENGTH:
            continue
        for sigma in ALPHABET_D:
            trace_now, det_now = (Fraction(x) for x in spectral_key(word))
            declared = (qtext(2 * trace_now - 1), qtext(2 * det_now))
            if declared != spectral_key(word + (sigma,)):
                result["closed_update"] = False
                result["closed_update_witness"] = {
                    "kind": "same-summary-same-action-different-summary",
                    "history": "".join(word),
                    "action": sigma,
                    "declared_update_result": _show(declared),
                    "successor_summary": _show(spectral_key(word + (sigma,))),
                }
                break
        if not result["closed_update"]:
            break
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", default=None)
    args = parser.parse_args()
    record = run()
    text = gapkit.canonical(record)
    if args.out:
        Path(args.out).write_text(text, encoding="utf-8")
        written = gapkit.sha256_bytes(text.encode("utf-8"))
        sys.stderr.write(f"exp1 written to {args.out} sha256={written}\n")
    else:
        sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
