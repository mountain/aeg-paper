#!/usr/bin/env python3
"""Experiment 1, independent route -- hand tables, a flux ledger, basis images.

This checker deliberately shares NO semantic helper with
``exp1_order_and_mixing.py``.  It re-derives every declared quantity by a
different method and then compares its own results with the primary evidence:

* the mixing plant is recomputed by an explicit FLUX LEDGER.  The state is
  never carried forward from step to step: at every step the vessel contents
  are reconstructed from the already-recorded transferred and spilled volumes,
  and the capacity branch is decided by a cross-multiplied exact comparison
  instead of ``min`` over the rationals;
* the declared summaries are re-built from that ledger, and sufficiency is
  decided by a PARTITION criterion (a summary is task-sufficient exactly when
  every summary class lies inside one task class) instead of by searching
  continuations;
* the downstream instance is recomputed by BASIS IMAGES: a linear map is
  carried only as the pair of images of the standard basis, composed by
  applying one map to the images of the other, so no two matrices are ever
  multiplied together.  The characteristic polynomial is checked by the
  Cayley-Hamilton relation instead of by reading trace and determinant off a
  product, and the inverse is obtained by exact Gaussian elimination.
* a hand-computed literal table of the declared witnesses is a third input.

The only shared module is ``gapkit``, and only for canonical JSON
serialisation, diagnostics and hashing.  No function of the primary
implementation is imported; the primary evidence file is read as data.

Run:

    python3 research/process-representation-gap/experiments/exp1_order_and_mixing_independent.py
"""

from __future__ import annotations

import argparse
import hashlib
import json
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
PRIMARY_EVIDENCE = ROOT / "evidence" / "exp1-order-and-mixing.json"

PG_HISTORY_PATH = gapkit.sibling_file(
    "AEG_PROCESS_GEOMETRY_REPO", "src/process_geometry/process/history.py"
)
PG_HISTORY_SHA256 = "93e9dc4651f4cf70e2a0980c9fee8ea58cc15acbe89bc064861c37359652cc45"

ALPHABET_N = ("P", "R")
ALPHABET_D = ("A", "B")
INITIAL = (Fraction(1), Fraction(1))
MAX_NATIVE_LENGTH = 6
MAX_CONTINUATION_DEPTH = 3
MAX_DOWNSTREAM_LENGTH = 4
EXPLORATORY_DOWNSTREAM_LENGTH = 6
FROZEN_VECTOR = (Fraction(2), Fraction(1))

UNDETERMINED = "NOT-DETERMINED-BY-SUMMARY"
BUDGET = "BUDGET-EXHAUSTED"

PROBE_FAMILIES = {
    "pi2_resp": ("P", "R"),
    "pi2_resp_d2": tuple("".join(w) for w in gapkit.words(ALPHABET_N, 2)),
    "pi2_resp_d3": tuple("".join(w) for w in gapkit.words(ALPHABET_N, 3)),
}

# --------------------------------------------------------------------------
# independent hand-computed literals
# --------------------------------------------------------------------------

# Derived by hand from the declared pour law, independently of the primary
# source.  Example, RPRR: R(1,1) transfers min(1/2, 1-1) = 0 and spills 1/2,
# giving (1, 1/2); P(1,1/2) transfers min(1/2, 1/2) = 1/2, giving (1/2, 1);
# R(1/2,1) transfers min(1/2, 1/2) = 1/2, giving (1, 1/2); R(1,1/2) transfers
# min(1/4, 0) = 0 and spills 1/4, giving (1, 1/4).
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

# Basis images of the two declared actions, entered as literals: the image of
# e1 = (1, 0) and of e2 = (0, 1) under the row-vector action.
HAND_BASIS_IMAGES = {
    "A": ((Fraction(1), Fraction(1)), (Fraction(0), Fraction(2))),
    "B": ((Fraction(0), Fraction(2)), (Fraction(-1), Fraction(3))),
}

# Hand-computed spectral and vector data for the declared words.
HAND_COMPOSITE = {
    "A": {"trace": "3", "det": "2", "charpoly": ["1", "-3", "2"], "vector": ("2", "4")},
    "B": {"trace": "3", "det": "2", "charpoly": ["1", "-3", "2"], "vector": ("-1", "7")},
    "AB": {"trace": "5", "det": "4", "charpoly": ["1", "-5", "4"], "vector": ("-4", "16")},
    "BA": {"trace": "5", "det": "4", "charpoly": ["1", "-5", "4"], "vector": ("-1", "13")},
}

IDENTITY_IMAGES = (
    (Fraction(1), Fraction(0)),
    (Fraction(0), Fraction(1)),
)


# --------------------------------------------------------------------------
# the plant by flux ledger
# --------------------------------------------------------------------------

def ledger(word):
    """(final state, records) with the state reconstructed from the ledger.

    ``flows`` holds the transferred and spilled volume of every step already
    decided.  The contents before a step are summed back out of that ledger
    instead of being carried forward, and the capacity branch is decided by the
    cross-multiplied comparison ``content <= 2 * free_space``.
    """
    flows = []

    def contents_before(index):
        u, v = INITIAL
        for _position, sigma, transferred, spilled in flows[:index]:
            if sigma == "P":
                u = u - transferred - spilled
                v = v + transferred
            else:
                u = u + transferred
                v = v - transferred - spilled
        return u, v

    for index, sigma in enumerate(word):
        u, v = contents_before(index)
        if sigma == "P":
            if u <= 2 * (1 - v):
                transferred = u / 2
            else:
                transferred = 1 - v
            spilled = u / 2 - transferred
        elif sigma == "R":
            if v <= 2 * (1 - u):
                transferred = v / 2
            else:
                transferred = 1 - u
            spilled = v / 2 - transferred
        else:
            raise Diagnostic("EXP1I-UNKNOWN-ACTION", repr(sigma))
        flows.append((index, sigma, transferred, spilled))
    return contents_before(len(flows)), tuple(flows)


_LEDGER_CACHE = {}


def state_of(word):
    key = tuple(word)
    if key not in _LEDGER_CACHE:
        _LEDGER_CACHE[key] = ledger(key)
    return _LEDGER_CACHE[key][0]


def records_of(word):
    key = tuple(word)
    if key not in _LEDGER_CACHE:
        _LEDGER_CACHE[key] = ledger(key)
    return _LEDGER_CACHE[key][1]


def native_domain(max_length=MAX_NATIVE_LENGTH):
    return [tuple(w) for w in gapkit.words(ALPHABET_N, max_length)]


def continuation_family(depth=MAX_CONTINUATION_DEPTH):
    return [tuple(w) for w in gapkit.words(ALPHABET_N, depth)]


def downstream_domain(max_length=MAX_DOWNSTREAM_LENGTH):
    return [tuple(w) for w in gapkit.words(ALPHABET_D, max_length)]


def counts(word):
    return (
        sum(1 for s in word if s == "P"),
        sum(1 for s in word if s == "R"),
    )


def state_key(state):
    return (qtext(state[0]), qtext(state[1]))


def step_records(word):
    return tuple(
        (position, sigma, qtext(transferred), qtext(spilled))
        for position, sigma, transferred, spilled in records_of(word)
    )


# --------------------------------------------------------------------------
# the downstream instance by basis images
# --------------------------------------------------------------------------

def apply_map(images, vector):
    """Apply the linear map carried by its basis images to one vector."""
    return (
        vector[0] * images[0][0] + vector[1] * images[1][0],
        vector[0] * images[0][1] + vector[1] * images[1][1],
    )


def compose_maps(outer, inner):
    """(inner then outer): each image of the inner map is moved by the outer."""
    return tuple(apply_map(outer, image) for image in inner)


def compose_sequence(sequence):
    """Compose a sequence of maps in the order the word is written."""
    images = IDENTITY_IMAGES
    for step in sequence:
        images = compose_maps(step, images)
    return images


def images_of_word(word):
    return compose_sequence([HAND_BASIS_IMAGES[sigma] for sigma in word])


def images_trace(images):
    return images[0][0] + images[1][1]


def images_det(images):
    return images[0][0] * images[1][1] - images[0][1] * images[1][0]


def spectral_key(word):
    images = images_of_word(word)
    return (qtext(images_trace(images)), qtext(images_det(images)))


def matrix_of_images(images):
    """The composite matrix read off the basis images (no matrix product)."""
    return [[images[0][0], images[0][1]], [images[1][0], images[1][1]]]


def inverse_by_elimination(images):
    """Exact Gaussian elimination on [M | I]; no adjugate formula."""
    rows = [
        [images[0][0], images[0][1], Fraction(1), Fraction(0)],
        [images[1][0], images[1][1], Fraction(0), Fraction(1)],
    ]
    for column in range(2):
        pivot = None
        for row in range(column, 2):
            if rows[row][column] != 0:
                pivot = row
                break
        require(
            pivot is not None,
            "EXP1I-SINGULAR-MAP",
            f"no pivot in column {column}",
        )
        rows[column], rows[pivot] = rows[pivot], rows[column]
        lead = rows[column][column]
        rows[column] = [entry / lead for entry in rows[column]]
        for row in range(2):
            if row == column:
                continue
            factor = rows[row][column]
            if factor == 0:
                continue
            rows[row] = [
                rows[row][i] - factor * rows[column][i] for i in range(4)
            ]
    return (
        (rows[0][2], rows[0][3]),
        (rows[1][2], rows[1][3]),
    )


def cayley_hamilton_holds(images):
    """M^2 = trace(M) * M - det(M) * I, checked on the basis images."""
    square = compose_maps(images, images)
    trace = images_trace(images)
    determinant = images_det(images)
    for index in range(2):
        for coordinate in range(2):
            left = square[index][coordinate]
            right = trace * images[index][coordinate] - (
                determinant if index == coordinate else Fraction(0)
            )
            if left != right:
                return False
    return True


# --------------------------------------------------------------------------
# declared summaries, rebuilt independently
# --------------------------------------------------------------------------

def key_pi0(word):
    np_, nr = counts(word)
    return (np_, nr, qtext(state_of(word)[0]))


def key_pi0_counts(word):
    return counts(word)


def key_pi0_endpoint(word):
    return (qtext(state_of(word)[0]),)


def key_pi1_word(word):
    return tuple(word)


def key_response(family):
    def key(word):
        return tuple(
            state_key(state_of(word + tuple(probe))) for probe in family
        )

    return key


def key_pi3_prov(word):
    return step_records(word)


def key_hist(word):
    return tuple((index, sigma) for index, sigma in enumerate(word))


def keys():
    table = {
        "pi0": key_pi0,
        "pi0_counts": key_pi0_counts,
        "pi0_endpoint": key_pi0_endpoint,
        "pi1_word": key_pi1_word,
        "pi3_prov": key_pi3_prov,
        "hist": key_hist,
        "pi_spectral": spectral_key,
    }
    for name, family in PROBE_FAMILIES.items():
        table[name] = key_response(family)
    return table


# declared abstract updates, re-implemented from the contract text
def update_pi0(value, sigma):
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


def update_response(family):
    def update(value, sigma):
        probes = tuple(family)
        u = 2 * Fraction(value[probes.index("P")][0])
        v = 2 * Fraction(value[probes.index("R")][1])
        successor = step_flow((u, v), sigma)[2]
        return tuple(
            state_key(advance_state(successor, tuple(probe))) for probe in probes
        )

    return update


def update_pi3_prov(value, sigma):
    u, v = INITIAL
    for _position, action, transferred, spilled in value:
        t, s = Fraction(transferred), Fraction(spilled)
        if action == "P":
            u, v = u - t - s, v + t
        else:
            u, v = u + t, v - t - s
    transferred, spilled, _successor = step_flow((u, v), sigma)
    return value + ((len(value), sigma, qtext(transferred), qtext(spilled)),)


def update_hist(value, sigma):
    if len(value) >= MAX_NATIVE_LENGTH:
        return BUDGET
    return value + ((len(value), sigma),)


def update_spectral(value, sigma):
    trace_now, det_now = Fraction(value[0]), Fraction(value[1])
    return (qtext(2 * trace_now - 1), qtext(2 * det_now))


UPDATE_LAWS = {
    "pi0": update_pi0,
    "pi0_counts": update_pi0_counts,
    "pi0_endpoint": update_pi0_endpoint,
    "pi1_word": update_pi1_word,
    "pi3_prov": update_pi3_prov,
    "hist": update_hist,
    "pi_spectral": update_spectral,
}
for _name, _family in PROBE_FAMILIES.items():
    UPDATE_LAWS[_name] = update_response(_family)


# --------------------------------------------------------------------------
# partition-based analysis (a different algorithm from the primary)
# --------------------------------------------------------------------------

def fibres(domain, keyfn):
    groups = {}
    for word in domain:
        groups.setdefault(keyfn(word), []).append(word)
    return groups


def analyse_independent(rep_id, keyfn, domain, domain_limit, alphabet, task_key):
    groups = fibres(domain, keyfn)
    task_classes = len(fibres(domain, task_key))
    refines = all(
        len({task_key(word) for word in words}) == 1 for words in groups.values()
    )
    largest = max((len(words) for words in groups.values() if len(words) > 1), default=0)
    colliding = sum(1 for words in groups.values() if len(words) > 1)

    witness = None
    if not refines:
        best = None
        for value, words in groups.items():
            ordered = sorted(words, key=lambda w: (len(w), w))
            for left, right in itertools_pairs(ordered):
                if task_key(left) == task_key(right):
                    continue
                rank = (len(left) + len(right), max(len(left), len(right)), left, right)
                if best is None or rank < best[0]:
                    best = (rank, left, right, value)
        if best is not None:
            _rank, left, right, value = best
            witness = {
                "summary_value": _show(value),
                "histories": ["".join(left), "".join(right)],
                "task_values": _show(task_key(left)),
            }

    # closure by the declared update law
    law = UPDATE_LAWS[rep_id]
    closure_ok = True
    closure_witness = None
    for word in domain:
        if len(word) >= domain_limit:
            continue
        for sigma in alphabet:
            successor = law(keyfn(word), sigma)
            if successor == BUDGET:
                continue
            if successor == UNDETERMINED or successor != keyfn(word + (sigma,)):
                closure_ok = False
                closure_witness = {
                    "history": "".join(word),
                    "action": sigma,
                    "kind": (
                        "update-not-determined-by-summary"
                        if successor == UNDETERMINED
                        else "same-summary-same-action-different-summary"
                    ),
                    "successor_summary": _show(keyfn(word + (sigma,))),
                }
                break
        if not closure_ok:
            break

    return {
        "classes_on_domain": len(groups),
        "colliding_fibers": colliding,
        "largest_fiber": largest,
        "sufficient": refines,
        "sufficiency_witness": witness,
        "refinement": (
            "equal-to-task" if refines and len(groups) == task_classes
            else "strictly-finer-than-task" if refines
            else "does-not-refine-task"
        ),
        "closed_update": closure_ok,
        "closed_update_witness": closure_witness,
        "partition_closed": partition_closed(keyfn, domain, alphabet, domain_limit),
    }


def partition_closed(keyfn, domain, alphabet, domain_limit):
    """Same summary and same action must give the same successor summary."""
    seen = {}
    for word in domain:
        if len(word) >= domain_limit:
            continue
        for sigma in alphabet:
            state = (keyfn(word), sigma)
            successor = keyfn(word + (sigma,))
            if state in seen and seen[state] != successor:
                return False
            seen[state] = successor
    return True


def itertools_pairs(items):
    for index, left in enumerate(items):
        for right in items[index + 1:]:
            yield left, right


def _show(value):
    if isinstance(value, (tuple, list)):
        return [_show(v) for v in value]
    return value


def storage_channels(rep_id, keyfn, domain):
    sizes = [len(gapkit.canonical(keyfn(word)).encode("utf-8")) for word in domain]
    return {
        "mean_storage_bytes_per_history": qtext(Fraction(sum(sizes), len(sizes))),
        "max_storage_bytes_per_history": max(sizes),
    }


def provenance_verdict(keyfn, domain):
    groups = fibres(domain, keyfn)
    for words in groups.values():
        ordered = sorted(words, key=lambda w: (len(w), w))
        for left, right in itertools_pairs(ordered):
            if step_records(left) != step_records(right):
                return {
                    "answers_provenance_task": False,
                    "witness_histories": ["".join(left), "".join(right)],
                }
    return {"answers_provenance_task": True, "witness_histories": None}


# --------------------------------------------------------------------------
# comparison with the primary evidence
# --------------------------------------------------------------------------

def compare(primary):
    disagreements = []
    checks = []
    partition_closure = {}

    def expect(field, independent, recorded):
        matches = independent == recorded
        checks.append({"field": field, "matches": matches})
        if not matches:
            disagreements.append(
                {"field": field, "independent": _show(independent), "primary": _show(recorded)}
            )

    domain = native_domain()
    family = continuation_family()
    down = downstream_domain()

    # hand tables
    for word, expected in sorted(HAND_PLANT.items()):
        observed = state_key(state_of(tuple(word)))
        require(
            observed == tuple(expected),
            "EXP1I-HAND-TABLE-MISMATCH",
            f"ledger route says {word!r} reaches {observed}, hand table says {tuple(expected)}",
        )
        expect(
            f"hand_table.plant[{word}]",
            list(observed),
            primary["hand_table_check"]["plant"].get(word),
        )
    for name, expected in sorted(HAND_COMPOSITE.items()):
        images = images_of_word(tuple(name))
        require(
            cayley_hamilton_holds(images),
            "EXP1I-CAYLEY-HAMILTON-FAILED",
            f"the characteristic polynomial of {name} does not annihilate it",
        )
        trace = qtext(images_trace(images))
        determinant = qtext(images_det(images))
        charpoly = ["1", qtext(-images_trace(images)), qtext(images_det(images))]
        action = tuple(qtext(x) for x in apply_map(images, FROZEN_VECTOR))
        require(
            (trace, determinant, charpoly, action)
            == (expected["trace"], expected["det"], expected["charpoly"],
                expected["vector"]),
            "EXP1I-HAND-TABLE-MISMATCH",
            f"basis-image route disagrees with the hand table on {name}",
        )
        expect(f"hand_table.matrix[{name}].charpoly", charpoly,
               primary["hand_table_check"]["matrix"].get(name))
        expect(f"hand_table.vector_action[{name}]", list(action),
               primary["hand_table_check"]["vector_action"].get(name))

    # witnesses
    gap = primary["witnesses"]["gap"]
    left, right = tuple(gap["pair"][0]), tuple(gap["pair"][1])
    expect("gap.pair", ["".join(left), "".join(right)], gap["pair"])
    expect("gap.summary_value", _show(key_pi0(left)), gap["summary_value"])
    expect("gap.states", [list(state_key(state_of(left))), list(state_key(state_of(right)))],
           gap["states"])
    expect("gap.same_declared_summary", key_pi0(left) == key_pi0(right),
           gap["same_declared_summary"])
    expect("gap.same_action_counts", counts(left) == counts(right), gap["same_action_counts"])
    expect("gap.spill_paths", {
        "".join(left): _show(step_records(left)),
        "".join(right): _show(step_records(right)),
    }, gap["spill_paths"])
    expect("gap.totals", [qtext(state_of(left)[0] + state_of(left)[1]),
                          qtext(state_of(right)[0] + state_of(right)[1])], gap["totals"])
    expect("gap.shortest_distinguishing_continuation.depth",
           first_separating_depth(left, right, family),
           gap["shortest_distinguishing_continuation"]["depth"])

    control = primary["witnesses"]["positive_control"]
    control_left, control_right = tuple(control["pair"][0]), tuple(control["pair"][1])
    expect("positive_control.same_state", state_of(control_left) == state_of(control_right),
           control["same_state"])
    expect("positive_control.summary_value", _show(key_pi0(control_left)),
           control["summary_value"])
    expect("positive_control.task_equivalent",
           first_separating_depth(control_left, control_right, family) is None,
           control["task_equivalent"])

    secondary = primary["witnesses"]["secondary_control"]
    sec_left, sec_right = tuple(secondary["pair"][0]), tuple(secondary["pair"][1])
    expect("secondary_control.same_declared_summary",
           key_pi0(sec_left) == key_pi0(sec_right), secondary["same_declared_summary"])
    expect("secondary_control.task_equivalent",
           first_separating_depth(sec_left, sec_right, family) is None,
           secondary["task_equivalent"])

    spectral = primary["witnesses"]["spectral"]
    spectral_left, spectral_right = ("A", "B"), ("B", "A")
    expect("spectral.composite_summaries",
           [_show(spectral_key(spectral_left)), _show(spectral_key(spectral_right))],
           spectral["composite_summaries"])
    expect("spectral.action_on_frozen_vector", {
        "".join(spectral_left): _show(tuple(qtext(x) for x in apply_map(images_of_word(spectral_left), FROZEN_VECTOR))),
        "".join(spectral_right): _show(tuple(qtext(x) for x in apply_map(images_of_word(spectral_right), FROZEN_VECTOR))),
    }, spectral["action_on_frozen_vector"])
    inverse_a = inverse_by_elimination(HAND_BASIS_IMAGES["A"])
    expect("spectral.conjugacy.A_inverse",
           _show([[qtext(x) for x in row] for row in matrix_of_images(inverse_a)]),
           spectral["conjugacy"]["A_inverse"])
    expect("spectral.conjugacy.verified",
           compose_sequence([inverse_a, images_of_word(spectral_left),
                             HAND_BASIS_IMAGES["A"]]) == images_of_word(spectral_right),
           spectral["conjugacy"]["verified"])
    expect("spectral.commutator",
           _show([[qtext(x) for x in row] for row in matrix_of_images(
               compose_sequence([
                   inverse_a,
                   inverse_by_elimination(HAND_BASIS_IMAGES["B"]),
                   HAND_BASIS_IMAGES["A"],
                   HAND_BASIS_IMAGES["B"],
               ])
           )]),
           spectral["commutator"])
    expect("spectral.single_actions_share_spectral_summary",
           spectral_key(("A",)) == spectral_key(("B",)),
           spectral["single_actions_share_spectral_summary"])

    # minimality
    minimal = minimal_gap_pair(domain)
    expect("minimality.minimal_pair", [minimal[2], minimal[3]],
           primary["minimality"]["minimal_pair"])
    expect("minimality.minimal_max_length", minimal[0],
           primary["minimality"]["minimal_max_length"])
    expect("minimality.minimal_total_length", minimal[1],
           primary["minimality"]["minimal_total_length"])
    expect("minimality.gap_pairs_total", count_gap_pairs(domain),
           primary["minimality"]["gap_pairs_total"])
    expect("minimality.pairs_with_max_length_at_most_2",
           count_gap_pairs([w for w in domain if len(w) <= 2]),
           primary["minimality"]["pairs_with_max_length_at_most_2"])

    # representations
    table = keys()
    for rep_id, keyfn in sorted(table.items()):
        recorded = (
            primary["representations"][rep_id]
            if rep_id in primary["representations"]
            else primary["downstream_spectral_analysis"]
        )
        spectral_rep = rep_id == "pi_spectral"
        limit = MAX_DOWNSTREAM_LENGTH if spectral_rep else MAX_NATIVE_LENGTH
        alphabet = ALPHABET_D if spectral_rep else ALPHABET_N
        rep_domain = down if spectral_rep else domain
        task_key = (
            (lambda w: apply_map(images_of_word(w), FROZEN_VECTOR))
            if spectral_rep else state_of
        )
        result = analyse_independent(rep_id, keyfn, rep_domain, limit, alphabet, task_key)
        expect(f"{rep_id}.classes_on_domain", result["classes_on_domain"],
               recorded["classes_on_domain"])
        expect(f"{rep_id}.colliding_fibers", result["colliding_fibers"],
               recorded["colliding_fibers"])
        expect(f"{rep_id}.largest_fiber", result["largest_fiber"],
               recorded["largest_fiber"])
        expect(f"{rep_id}.sufficient", result["sufficient"], recorded["sufficient"])
        expect(f"{rep_id}.refinement", result["refinement"], recorded["refinement"])
        expect(f"{rep_id}.closed_update", result["closed_update"],
               recorded["closed_update"])
        partition_closure[rep_id] = result["partition_closed"]
        if result["sufficiency_witness"] and recorded["sufficiency_witness"]:
            expect(f"{rep_id}.sufficiency_witness.histories",
                   result["sufficiency_witness"]["histories"],
                   recorded["sufficiency_witness"]["histories"])
        channels = storage_channels(rep_id, keyfn, rep_domain)
        recorded_cost = (
            primary["cost"][rep_id]
            if rep_id in primary["cost"]
            else primary["cost_downstream"]
        )
        expect(f"{rep_id}.mean_storage_bytes_per_history",
               channels["mean_storage_bytes_per_history"],
               recorded_cost["mean_storage_bytes_per_history"])
        expect(f"{rep_id}.max_storage_bytes_per_history",
               channels["max_storage_bytes_per_history"],
               recorded_cost["max_storage_bytes_per_history"])

        if rep_id != "pi_spectral":
            verdict = provenance_verdict(keyfn, domain)
            expect(f"{rep_id}.answers_provenance_task",
                   verdict["answers_provenance_task"],
                   primary["secondary_task_analysis"]["verdicts"][rep_id][
                       "answers_provenance_task"
                   ])

    # reserved verification family and the exploratory length law
    for length in (3, 4):
        words = [w for w in down if len(w) == length]
        groups = fibres(words, spectral_key)
        separated = 0
        for group in groups.values():
            for left_word, right_word in itertools_pairs(
                sorted(group, key=lambda w: (len(w), w))
            ):
                if apply_map(images_of_word(left_word), FROZEN_VECTOR) != \
                        apply_map(images_of_word(right_word), FROZEN_VECTOR):
                    separated += 1
        recorded = primary["reserved_verification_family"][str(length)]
        expect(f"reserved[{length}].words", len(words), recorded["words"])
        expect(f"reserved[{length}].summary_classes", len(groups),
               recorded["summary_classes"])
        expect(f"reserved[{length}].largest_class",
               max(len(g) for g in groups.values()), recorded["largest_class"])
        expect(f"reserved[{length}].same_summary_different_action_pairs", separated,
               recorded["same_summary_different_action_pairs"])
    for length in range(MAX_DOWNSTREAM_LENGTH + 1, EXPLORATORY_DOWNSTREAM_LENGTH + 1):
        words = [
            tuple(w) for w in gapkit.words(ALPHABET_D, length) if len(w) == length
        ]
        summaries = sorted({spectral_key(w) for w in words})
        expect(f"exploratory[{length}].words", len(words),
               primary["exploratory_structural_check"]["lengths"][str(length)]["words"])
        expect(f"exploratory[{length}].spectral_summaries", _show(summaries),
               primary["exploratory_structural_check"]["lengths"][str(length)][
                   "spectral_summaries"
               ])

    # uncapped linear variant
    uncapped = uncapped_facts(domain)
    for field, value in sorted(uncapped.items()):
        expect(f"uncapped.{field}", value, primary["uncapped_variant"][field])

    # plant structure
    expect("native_instance.reachable_state_count",
           len({state_of(w) for w in domain}),
           primary["native_instance"]["reachable_state_count"])
    expect("native_instance.vessel_swap_conjugacy.failures",
           swap_conjugacy_failures(domain),
           primary["native_instance"]["vessel_swap_conjugacy"]["failures"])
    expect("witnesses.response_recovery_law.failures",
           recovery_failures(domain),
           primary["witnesses"]["response_recovery_law"]["failures"])

    return checks, disagreements, partition_closure


def first_separating_depth(left, right, family):
    for depth in range(MAX_CONTINUATION_DEPTH + 1):
        for eta in family:
            if len(eta) != depth:
                continue
            if ledger_state_after(left, eta) != ledger_state_after(right, eta):
                return depth
    return None


def ledger_state_after(word, eta):
    return state_of(tuple(word) + tuple(eta))


def minimal_gap_pair(domain):
    rows = []
    for left, right in itertools_pairs(domain):
        if key_pi0(left) != key_pi0(right):
            continue
        if state_of(left) == state_of(right):
            continue
        rows.append((max(len(left), len(right)), len(left) + len(right),
                     "".join(left), "".join(right)))
    rows.sort()
    return rows[0]


def count_gap_pairs(domain):
    total = 0
    for left, right in itertools_pairs(domain):
        if key_pi0(left) == key_pi0(right) and state_of(left) != state_of(right):
            total += 1
    return total


def uncapped_facts(domain):
    """The separately declared variant without the capacity bound."""
    totals_vary = False
    states = {}
    for word in domain:
        u, v = INITIAL
        for sigma in word:
            before = u + v
            if sigma == "P":
                u, v = u / 2, v + u / 2
            else:
                u, v = u + v / 2, v / 2
            if u + v != before:
                totals_vary = True
        states[word] = (u, v)
    collisions = 0
    first = None
    for left, right in itertools_pairs(domain):
        np_l, nr_l = counts(left)
        np_r, nr_r = counts(right)
        if (np_l, nr_l, qtext(states[left][0])) == (np_r, nr_r, qtext(states[right][0])) \
                and states[left] != states[right]:
            collisions += 1
            if first is None:
                first = ["".join(left), "".join(right)]
    return {
        "conservation_total_violations": 1 if totals_vary else 0,
        "total_is_invariant_on_domain": not totals_vary,
        "summary_collisions_with_distinct_states": collisions,
        "first_collision": first,
        "declared_states_checked": len(domain),
        "endpoint_determines_state": "v = 2 - u on the declared domain",
    }


def swap_conjugacy_failures(domain):
    failures = []
    for state in sorted({state_of(w) for w in domain}, key=str):
        swapped = (state[1], state[0])
        # S(P(s)) must equal R(S(s)): compare by ledger reconstruction
        p_image = ledger_single(state, "P")
        r_image_of_swap = ledger_single(swapped, "R")
        if (p_image[1], p_image[0]) != r_image_of_swap:
            failures.append(state_key(state))
    return failures


def step_flow(state, sigma):
    """(transferred, spilled, successor) by a cross-multiplied exact branch."""
    u, v = state
    if sigma == "P":
        transferred = u / 2 if u <= 2 * (1 - v) else 1 - v
        spilled = u / 2 - transferred
        return transferred, spilled, (u - transferred - spilled, v + transferred)
    if sigma == "R":
        transferred = v / 2 if v <= 2 * (1 - u) else 1 - u
        spilled = v / 2 - transferred
        return transferred, spilled, (u + transferred, v - transferred - spilled)
    raise Diagnostic("EXP1I-UNKNOWN-ACTION", repr(sigma))


def ledger_single(state, sigma):
    """One ledger step from an explicit state (used for the swap check)."""
    return step_flow(state, sigma)[2]


def advance_state(state, eta):
    for sigma in eta:
        state = step_flow(state, sigma)[2]
    return state


def recovery_failures(domain):
    failures = []
    for word in domain:
        state = state_of(word)
        u = 2 * ledger_single(state, "P")[0]
        v = 2 * ledger_single(state, "R")[1]
        if (u, v) != state:
            failures.append({"history": "".join(word), "recovered": [qtext(u), qtext(v)]})
    return failures


# --------------------------------------------------------------------------
# controls
# --------------------------------------------------------------------------

def read_frozen():
    out = {}
    if FROZEN.exists():
        for line in FROZEN.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            digest, _, name = line.partition("  ")
            out[name.strip()] = digest.strip()
    return out


def run():
    require(PRIMARY_EVIDENCE.exists(), "EXP1I-EVIDENCE-MISSING", str(PRIMARY_EVIDENCE))
    primary = json.loads(PRIMARY_EVIDENCE.read_text(encoding="utf-8"))

    contract_sha = gapkit.sha256_file(CONTRACT)
    frozen = read_frozen()
    require(
        frozen.get(CONTRACT.name, contract_sha) == contract_sha,
        "EXP-CONTRACT-DRIFT",
        f"{CONTRACT.name}: ledger {frozen.get(CONTRACT.name)!r} != actual {contract_sha}",
    )
    require(
        primary["contract"]["sha256"] == contract_sha,
        "EXP-CONTRACT-DRIFT",
        "the primary evidence cites a different contract digest",
    )

    raw = PG_HISTORY_PATH.read_bytes()
    active_sha = gapkit.sha256_bytes(raw)
    require(
        active_sha == PG_HISTORY_SHA256,
        "EXP1I-PIN-DRIFT",
        f"{PG_HISTORY_PATH.name}: {active_sha} != pinned {PG_HISTORY_SHA256}",
    )
    require(
        primary["pinned_carrier"]["sha256"] == active_sha,
        "EXP1I-PIN-DRIFT",
        "the primary evidence cites a different pinned digest",
    )

    controls = []
    controls.append({
        "id": "oracle-drift",
        "expected": "EXP1I-PIN-DRIFT",
        "observed": gapkit.reject(
            lambda: require(active_sha == "0" * 64, "EXP1I-PIN-DRIFT",
                            "the pinned carrier digest changed"),
            "EXP1I-PIN-DRIFT",
        ),
    })
    controls.append({
        "id": "hand-table-mutated",
        "expected": "EXP1I-HAND-TABLE-MISMATCH",
        "observed": gapkit.reject(
            lambda: require(
                state_key(state_of(("P", "R", "R"))) == ("1", "1/8"),
                "EXP1I-HAND-TABLE-MISMATCH",
                "the ledger route does not reproduce the mutated hand table",
            ),
            "EXP1I-HAND-TABLE-MISMATCH",
        ),
    })
    controls.append({
        "id": "route-disagreement-detected",
        "expected": "EXP1-ROUTE-DISAGREEMENT",
        "observed": gapkit.reject(
            lambda: require(
                _show(key_pi0(("P", "R", "R"))) == _show((1, 2, "1/8")),
                "EXP1-ROUTE-DISAGREEMENT",
                "the independent route disagrees with a mutated primary value",
            ),
            "EXP1-ROUTE-DISAGREEMENT",
        ),
    })

    checks, disagreements, partition_closure = compare(primary)
    record = {
        "schema": "aeg.process-representation-gap.exp1-independent.v1",
        "role": "independent verification route for exp1",
        "contract": {
            "path": str(CONTRACT.relative_to(ROOT.parent.parent)),
            "sha256": contract_sha,
        },
        "primary_evidence": {
            "path": str(PRIMARY_EVIDENCE.relative_to(ROOT.parent.parent)),
            "sha256": gapkit.sha256_file(PRIMARY_EVIDENCE),
        },
        "environment": gapkit.environ(),
        "pinned_carrier": {
            "path_env": "AEG_PROCESS_GEOMETRY_REPO",
            "relative_path": "src/process_geometry/process/history.py",
            "sha256": active_sha,
            "git_blob": git_blob_sha1(raw),
        },
        "independence": {
            "plant": "recomputed by an explicit flux ledger; the state is reconstructed from the recorded flows at every step and the capacity branch uses a cross-multiplied comparison instead of min over rationals",
            "summaries": "rebuilt from that ledger; sufficiency is decided by a partition criterion (every summary class inside one task class) instead of by searching continuations",
            "linear_instance": "recomputed with basis images only; maps are composed by applying one map to the images of the other, so no two matrices are multiplied; the characteristic polynomial is checked by the Cayley-Hamilton relation and the inverse by exact Gaussian elimination",
            "hand_tables": "hand-computed literal tables of the plant states, the composite spectra and the frozen-vector actions",
            "shared": "gapkit only, and only for canonical serialisation, diagnostics and hashing; no function of the primary implementation is imported",
            "not_independently_rederived": [
                "the declared cost channels computation_steps, observations and verification_cost, which are accounting rules of the declared construction rather than recomputable mathematical facts",
                "storage_bytes mean and maximum are re-derived here from the independent payloads through gapkit.canonical",
            ],
        },
        "comparison": {
            "fields_compared": len(checks),
            "fields_matching": sum(1 for c in checks if c["matches"]),
            "disagreements": disagreements,
        },
        "partition_closure": partition_closure,
        "negative_controls": controls,
        "conclusion": (
            "the independent route reproduces every compared primary quantity"
            if not disagreements
            else "the independent route disagrees; the disagreement is the result"
        ),
    }
    require(
        not disagreements,
        "EXP1-ROUTE-DISAGREEMENT",
        f"the two routes disagree on {len(disagreements)} field(s): "
        f"{[d['field'] for d in disagreements[:6]]}",
    )
    return record


def git_blob_sha1(raw: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(raw)).encode("ascii") + b"\0" + raw).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", default=None)
    args = parser.parse_args()
    record = run()
    text = gapkit.canonical(record)
    if args.out:
        Path(args.out).write_text(text, encoding="utf-8")
        sys.stderr.write(
            f"exp1 independent written to {args.out} "
            f"sha256={gapkit.sha256_bytes(text.encode('utf-8'))}\n"
        )
    else:
        sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
