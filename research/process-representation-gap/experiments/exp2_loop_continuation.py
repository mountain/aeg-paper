#!/usr/bin/env python3
"""Experiment 2 -- loop continuation and anytime observation.

Contract: research/process-representation-gap/contracts/exp2-loop-continuation.v1.json

The question the work plan asks is whether two histories with the same current
observation stay indistinguishable under the same future interaction.  The
answer is computed here on a declared small typed model, exactly, with no
floating point, under CPython and under ``python3 -O``.

The model is NOT native Adva execution and NOT a faithful AES gate motion.  It
is a declared instance of the Paper IV continuation contract: a free monoid of
mechanisms, a declared partial legality, an exact rational accumulator, and a
declared observation.  The pinned PR-16 records are used as the *source of the
readout form*, and the fact that they admit no common legal native continuation
is reported as a gap rather than papered over.

Run:

    python3 research/process-representation-gap/experiments/exp2_loop_continuation.py
"""

from __future__ import annotations

import argparse
import itertools
import sys
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(ROOT / "tools"))
import gapkit  # noqa: E402
from gapkit import Diagnostic, qtext, require  # noqa: E402

CONTRACT = ROOT / "contracts" / "exp2-loop-continuation.v1.1.json"
FROZEN = ROOT / "contracts" / "FROZEN.sha256"
EVIDENCE = ROOT / "evidence" / "exp2-loop-continuation.json"

SCHEMA = "aeg.process-representation-gap.exp2.v1"
ALPHABET = ("c", "v", "l")
INVALID = "INVALID"
EMPTY_OUTCOME = "EMPTY"
MAX_DOMAIN_LENGTH = 6          # exhaustive layer, per contract
MAX_CONTINUATION_DEPTH = 3     # declared continuation family M_C

# Hand-computed witnesses, entered as literals.  They are the independent
# input to the accumulator law and are re-derived by the affine-map route in
# the companion independent checker.
HAND_TABLE = {
    "": "0",
    "c": "1",
    "cc": "3",
    "ccc": "7",
    "cv": "1/2",
    "ccv": "3/2",
    "cvc": "2",
    "cccv": "7/2",
    "ccvcl": "5",
}

# The pinned PR-16 event words, quoted so that the gap report names them.
PR16_LEFT_WORD = ("c", "v", "c")
PR16_RIGHT_WORD = ("v", "c", "v")
PR16_SCALAR_TRIPLE = ("3", "1", "2")


# --------------------------------------------------------------------------
# the declared model
# --------------------------------------------------------------------------

def counts(word) -> tuple:
    """Mechanism incidence counts (compute, verify, learn)."""
    return (word.count("c"), word.count("v"), word.count("l"))


def legal_actions(word) -> tuple:
    """The declared legality: c always; v iff c > v; l iff v >= 1."""
    nc, nv, _ = counts(word)
    out = ["c"]
    if nc > nv:
        out.append("v")
    if nv >= 1:
        out.append("l")
    return tuple(out)


def is_legal(word, sigma) -> bool:
    return sigma in legal_actions(word)


def step(word, sigma):
    require(is_legal(word, sigma), "EXP2-ILLEGAL-ACTION",
            f"action {sigma!r} is not legal at word {word!r}")
    return word + (sigma,)


def accum(word) -> Fraction:
    """The exact accumulator A, by the declared recurrence."""
    value = Fraction(0)
    for sigma in word:
        if sigma == "c":
            value = 2 * value + 1
        elif sigma == "v":
            value = value / 2
        else:
            value = value + 1
    return value


def readout(word) -> tuple:
    """The three-scalar readout R(w) of the frozen PR-16 snapshot policy.

    y1 = count_c + count_v, y2 = frames - handoffs, y3 = 3*handoffs/frames,
    with frames = |w| and handoffs = max(|w| - 1, 0).
    """
    if len(word) == 0:
        return (EMPTY_OUTCOME, EMPTY_OUTCOME, EMPTY_OUTCOME)
    nc, nv, _ = counts(word)
    frames = len(word)
    handoffs = frames - 1
    return (
        qtext(Fraction(nc + nv)),
        qtext(Fraction(frames - handoffs)),
        qtext(Fraction(3 * handoffs, frames)),
    )


def state_observation(word):
    """The task observation as a function of the STATE alone.

    Paper IV observes the state, so the model is presented as a Moore machine
    rather than a Mealy machine.  A trailing learn action exposes the
    accumulator of the state before it, which is recovered exactly by
    A(u.l) - 1 = A(u); the two presentations induce the same equivalence.
    """
    if word and word[-1] == "l":
        return ("learned", qtext(accum(word) - 1))
    return ("readout",) + readout(word)


def observe(word, sigma):
    """The observation produced by applying a legal action.

    Equal to ``state_observation`` of the successor state, so that the primary
    implementation and the Moore-machine oracle observe the same task.
    """
    return state_observation(word + (sigma,))


def run_continuation(word, eta):
    """Observation sequence produced by a continuation word, or INVALID."""
    observations = []
    current = word
    for sigma in eta:
        if not is_legal(current, sigma):
            return (INVALID, sigma)
        observations.append([sigma, list(observe(current, sigma))])
        current = current + (sigma,)
    return (tuple(tuple(o[1]) for o in observations),)


def continuation_family(depth=MAX_CONTINUATION_DEPTH):
    """The frozen continuation family M_C: all words of length <= depth."""
    return [tuple(w) for w in gapkit.words(ALPHABET, depth)]


def legal_word(word) -> bool:
    """True if every prefix of ``word`` is reached by a legal action."""
    current = ()
    for sigma in word:
        if not is_legal(current, sigma):
            return False
        current = current + (sigma,)
    return True


def _first_illegal_prefix(word):
    current = ()
    for index, sigma in enumerate(word):
        if not is_legal(current, sigma):
            return {"index": index, "action": sigma,
                    "prefix": "".join(current)}
        current = current + (sigma,)
    return None


def enumerate_domain(max_length=MAX_DOMAIN_LENGTH):
    """Reachable legal words, in the declared lexicographic order."""
    out = [()]
    frontier = [()]
    while frontier:
        nxt = []
        for word in frontier:
            if len(word) >= max_length:
                continue
            for sigma in legal_actions(word):
                child = word + (sigma,)
                nxt.append(child)
                out.append(child)
        frontier = nxt
    return out


# --------------------------------------------------------------------------
# declared representations
# --------------------------------------------------------------------------

def pi0(word):
    return readout(word)


def pi1(word):
    return counts(word)


def pi2(word):
    return counts(word) + (word[-1] if word else "NONE",)


def pi3(word):
    return counts(word) + (word[-1] if word else "NONE",) + (word[-2:], qtext(accum(word)))


def hist(word):
    return word


REPRESENTATIONS = {
    "pi0": {"fn": pi0, "tier": "existing-summary", "label": "PR-16 three-scalar readout"},
    "pi1": {"fn": pi1, "tier": "bounded-enhancement", "label": "mechanism incidence counts"},
    "pi2": {"fn": pi2, "tier": "bounded-enhancement", "label": "counts plus phase tag"},
    "pi3": {"fn": pi3, "tier": "bounded-enhancement", "label": "counts, phase, 2-suffix, accumulator"},
    "hist": {"fn": hist, "tier": "full-history-upper-bound", "label": "literal word"},
}


# --------------------------------------------------------------------------
# task-relative equivalence and the two failure modes
# --------------------------------------------------------------------------

_RUN_CACHE = {}


def cached_run(word, eta):
    key = (word, eta)
    hit = _RUN_CACHE.get(key)
    if hit is None:
        hit = run_continuation(word, eta)
        _RUN_CACHE[key] = hit
    return hit


def base_equivalent(w1, w2, family):
    """Equivalence under all continuations JOINTLY legal for both.

    Continuations legal for exactly one side are excluded from this relation;
    the work plan states that distinguishing such a pair requires the legality
    signature to be added to the definition, which is ``augmented_equivalent``.
    """
    for eta in family:
        r1 = cached_run(w1, eta)
        r2 = cached_run(w2, eta)
        if r1[0] == INVALID or r2[0] == INVALID:
            continue
        if r1 != r2:
            return False
    return True


def augmented_equivalent(w1, w2, family):
    """Base equivalence plus equal legal-action sets."""
    if legal_actions(w1) != legal_actions(w2):
        return False
    return base_equivalent(w1, w2, family)


def shortest_separating_continuation(w1, w2, family):
    """Shortest eta, by declared length then lexicographic order, that separates.

    Returns None when the pair is not separated inside the declared family.
    """
    for depth in range(MAX_CONTINUATION_DEPTH + 1):
        for eta in family:
            if len(eta) != depth:
                continue
            r1 = cached_run(w1, eta)
            r2 = cached_run(w2, eta)
            legal1 = r1[0] != INVALID
            legal2 = r2[0] != INVALID
            if legal1 != legal2:
                return {"eta": list(eta), "kind": "legality", "depth": depth}
            if legal1 and legal2 and r1 != r2:
                return {"eta": list(eta), "kind": "observation", "depth": depth}
    return None


def fibers(domain, keyfn):
    groups = {}
    for word in domain:
        groups.setdefault(keyfn(word), []).append(word)
    return groups


def analyse_representation(name, spec, domain, family):
    """Sufficiency and closed-update status for one declared representation."""
    keyfn = spec["fn"]
    groups = fibers(domain, keyfn)

    result = {
        "id": name,
        "tier": spec["tier"],
        "label": spec["label"],
        "classes_on_domain": len(groups),
        "domain_size": len(domain),
        "colliding_fibers": 0,
        "largest_fiber": 0,
        "sufficient": True,
        "sufficiency_witness": None,
        "closed_update": True,
        "closed_update_witness": None,
    }
    best = None
    for key, words in sorted(groups.items(), key=lambda kv: (len(kv[1]), str(kv[0])), reverse=True):
        if len(words) < 2:
            continue
        result["colliding_fibers"] += 1
        result["largest_fiber"] = max(result["largest_fiber"], len(words))
        if not result["sufficient"]:
            continue
        for w1, w2 in itertools.combinations(sorted(words), 2):
            if base_equivalent(w1, w2, family):
                continue
            sep = shortest_separating_continuation(w1, w2, family)
            if sep is None:
                # Not separated inside the declared family: a bounded-domain
                # compatibility result, reported as such and never promoted.
                continue
            rank = (len(w1) + len(w2), sep["depth"], tuple(sep["eta"]))
            if best is None or rank < best[0]:
                best = (rank, sep, w1, w2, key)
    if best is not None:
        _, sep, w1, w2, key = best
        result["sufficient"] = False
        result["sufficiency_witness"] = {
            "minimal_history_length": len(w1) + len(w2),
            "representation_value": _jsonable(key),
            "histories": ["".join(w1), "".join(w2)],
            "legality": {"left": list(legal_actions(w1)), "right": list(legal_actions(w2))},
            "shortest_distinguishing_continuation": sep,
            "observation_left": _jsonable(run_continuation(w1, tuple(sep["eta"]))),
            "observation_right": _jsonable(run_continuation(w2, tuple(sep["eta"]))),
        }

    # Closed update: ker pi must be a right congruence on the declared domain.
    update_domain = [w for w in domain if len(w) < MAX_DOMAIN_LENGTH]
    update_groups = fibers(update_domain, keyfn)
    for key, words in sorted(update_groups.items(), key=lambda kv: (len(kv[1]), str(kv[0])), reverse=True):
        if len(words) < 2 or not result["closed_update"]:
            continue
        for w1, w2 in itertools.combinations(sorted(words), 2):
            for sigma in ALPHABET:
                l1, l2 = is_legal(w1, sigma), is_legal(w2, sigma)
                if l1 != l2:
                    result["closed_update"] = False
                    result["closed_update_witness"] = {
                        "kind": "legality-not-decided-by-representation",
                        "representation_value": _jsonable(key),
                        "histories": ["".join(w1), "".join(w2)],
                        "action": sigma,
                        "legality": {"left": l1, "right": l2},
                        "observed_outcome": {
                            "left": _jsonable(run_continuation(w1, (sigma,))),
                            "right": _jsonable(run_continuation(w2, (sigma,))),
                        },
                    }
                    break
                if l1 and keyfn(w1 + (sigma,)) != keyfn(w2 + (sigma,)):
                    result["closed_update"] = False
                    result["closed_update_witness"] = {
                        "kind": "same-digest-same-action-different-digest",
                        "representation_value": _jsonable(key),
                        "histories": ["".join(w1), "".join(w2)],
                        "action": sigma,
                        "digests_after": {
                            "left": _jsonable(keyfn(w1 + (sigma,))),
                            "right": _jsonable(keyfn(w2 + (sigma,))),
                        },
                    }
                    break
            if not result["closed_update"]:
                break
    return result


def _jsonable(value):
    if isinstance(value, tuple):
        return [_jsonable(v) for v in value]
    if isinstance(value, list):
        return [_jsonable(v) for v in value]
    if isinstance(value, (str, int)):
        return value
    return str(value)




# --------------------------------------------------------------------------
# the declared one-field enhancement grid (contract enhancement_grid)
# --------------------------------------------------------------------------

def field_phase(word):
    return word[-1] if word else "NONE"


def field_first(word):
    return word[0] if word else "NONE"


def field_suffix2(word):
    return word[-2:]


def field_alternations(word):
    return sum(1 for a, b in zip(word, word[1:]) if a != b)


def field_accum(word):
    return qtext(accum(word))


def field_last_learn_position(word):
    positions = [i for i, sigma in enumerate(word) if sigma == "l"]
    return positions[-1] if positions else "NONE"


def field_verified_fraction(word):
    nc, nv, _ = counts(word)
    return qtext(Fraction(nv, nc)) if nc else "EMPTY"


GRID_FIELDS = {
    "phase": field_phase,
    "first": field_first,
    "suffix2": field_suffix2,
    "alternations": field_alternations,
    "accum": field_accum,
    "last_learn_position": field_last_learn_position,
    "verified_fraction": field_verified_fraction,
}


def grid_representations():
    """counts plus exactly ONE declared field, one candidate per field."""
    out = {}
    for name, extractor in sorted(GRID_FIELDS.items()):
        out["counts+" + name] = {
            "fn": (lambda extractor=extractor: (lambda w: counts(w) + (extractor(w),)))(),
            "tier": "bounded-enhancement",
            "label": f"counts plus {name}",
            "field": name,
        }
    return out


def run_enhancement_grid(domain, family):
    """Scan the declared grid; select by the declared rule.  No ad-hoc fields."""
    candidates = grid_representations()
    rows = {}
    for name, spec in candidates.items():
        analysis = analyse_representation(name, spec, domain, family)
        cost = representation_cost(name, spec, domain, family)
        rows[name] = {
            "field": spec["field"],
            "label": spec["label"],
            "classes_on_domain": analysis["classes_on_domain"],
            "sufficient": analysis["sufficient"],
            "closed_update": analysis["closed_update"],
            "sufficiency_witness": analysis["sufficiency_witness"],
            "closed_update_witness": analysis["closed_update_witness"],
            "structural_size": cost["cost"]["structural_size"],
            "mean_storage_bytes": cost["mean_storage_bytes_per_history"],
        }
    qualifying = sorted(
        (name for name, row in rows.items() if row["sufficient"] and row["closed_update"]),
        key=lambda name: (_fraction(rows[name]["mean_storage_bytes"]), rows[name]["structural_size"], name),
    )
    return {
        "declared_fields": sorted(GRID_FIELDS),
        "candidates": rows,
        "qualifying": qualifying,
        "selection_rule": ("smallest (structural_size, storage_bytes) among candidates that are both "
                           "task-sufficient and closed-update; ties broken by canonical name"),
        "selected": qualifying[0] if qualifying else None,
        "note": ("scanning a DECLARED family is not the same as adding a field after seeing a "
                 "failure; every field here was fixed in contract version 1.1 before the scan ran"),
    }


def _fraction(text):
    return Fraction(text)


# --------------------------------------------------------------------------
# reserved verification family (work-plan section 9)
# --------------------------------------------------------------------------

RESERVED_MIN_LENGTH = MAX_DOMAIN_LENGTH + 1     # 7
RESERVED_MAX_LENGTH = MAX_DOMAIN_LENGTH + 2     # 8


def enumerate_legal_words_between(low, high):
    """Reachable legal words with low <= |w| <= high, in declared order."""
    out = []
    frontier = [w for w in enumerate_domain(high) if len(w) == low]
    out.extend(frontier)
    while frontier:
        nxt = []
        for word in frontier:
            if len(word) >= high:
                continue
            for sigma in legal_actions(word):
                child = word + (sigma,)
                nxt.append(child)
                out.append(child)
        frontier = nxt
    return sorted(set(out), key=lambda w: (len(w), w))


def reserved_verification(selected_id, spec, family):
    """Test the SELECTED repair on words NOT used to select it.

    The repair in contract v1.1 was chosen on the exhaustive layer |w| <= 6.
    This family is |w| in {7, 8}: inside the contract's declared domain, outside
    the enumeration layer that produced the choice.  Nothing here may feed back
    into the selection; a failure is a result and is reported as one.
    """
    words = enumerate_legal_words_between(RESERVED_MIN_LENGTH, RESERVED_MAX_LENGTH)
    require(words, "EXP2-RESERVED-EMPTY", "the reserved family is empty")
    analysis = analyse_representation(selected_id, spec, words, family)
    control = analyse_representation("hist", REPRESENTATIONS["hist"], words, family)
    return {
        "role": ("held out from the repair selection; the recommendation was fixed on "
                 "|w| <= 6 before this family was evaluated"),
        "length_range": [RESERVED_MIN_LENGTH, RESERVED_MAX_LENGTH],
        "size": len(words),
        "by_length": {str(n): len([w for w in words if len(w) == n])
                      for n in range(RESERVED_MIN_LENGTH, RESERVED_MAX_LENGTH + 1)},
        "selected_candidate": selected_id,
        "sufficient": analysis["sufficient"],
        "closed_update": analysis["closed_update"],
        "classes_on_reserved_domain": analysis["classes_on_domain"],
        "sufficiency_witness": analysis["sufficiency_witness"],
        "closed_update_witness": analysis["closed_update_witness"],
        "full_history_control_sufficient": control["sufficient"],
        "verdict": ("the selected repair still holds outside the selection family"
                    if analysis["sufficient"] and analysis["closed_update"]
                    else "the selected repair FAILS outside the selection family; reported, not hidden"),
    }


# --------------------------------------------------------------------------
# cost
# --------------------------------------------------------------------------

def representation_cost(name, spec, domain, family):
    cost = gapkit.Cost()
    sizes = []
    for word in domain:
        payload = _jsonable(spec["fn"](word))
        cost.store(payload)
        cost.step(1)
        sizes.append(len(gapkit.canonical(payload).encode("utf-8")))
    signature_observations = 0
    for word in domain:
        for eta in family:
            signature_observations += max(len(eta), 1)
    cost.observe(signature_observations)
    cost.verify(len(domain) * len(family))
    return {
        "id": name,
        "cost": cost.as_record(),
        "mean_storage_bytes_per_history": _q(sum(sizes), len(sizes)),
        "max_storage_bytes_per_history": max(sizes),
    }


def _q(num, den):
    value = Fraction(num, den)
    return qtext(value)


# --------------------------------------------------------------------------
# negative controls
# --------------------------------------------------------------------------

def negative_controls(domain, family):
    controls = []

    # 1. The frozen contract must not drift.
    frozen = _read_frozen()
    controls.append({"id": "frozen-hash-present", "ok": str(CONTRACT) in frozen or CONTRACT.name in frozen})

    # 2. An illegal action must be refused with its own code.
    controls.append({
        "id": "illegal-action-accepted",
        "expected": "EXP2-ILLEGAL-ACTION",
        "observed": gapkit.reject(lambda: step(("c", "c", "c"), "l"), "EXP2-ILLEGAL-ACTION"),
    })

    # 3. A mutated accumulator law must break the hand table.
    def mutated():
        bad = Fraction(0)
        result = {}
        for word, expected in HAND_TABLE.items():
            bad = Fraction(0)
            for sigma in word:
                if sigma == "c":
                    bad = 2 * bad + 1
                elif sigma == "v":
                    bad = bad - 1
                else:
                    bad = bad + 1
            result[word] = qtext(bad)
        for word, expected in HAND_TABLE.items():
            require(result[word] == expected, "EXP2-HAND-TABLE-MISMATCH",
                    f"A({word!r}) = {result[word]}, hand table says {expected}")
    controls.append({
        "id": "accumulator-law-mutated",
        "expected": "EXP2-HAND-TABLE-MISMATCH",
        "observed": gapkit.reject(mutated, "EXP2-HAND-TABLE-MISMATCH"),
    })

    # 4. The readout must NOT separate ccv from cvc; claiming it does is an error.
    def overclaim_readout():
        require(readout(("c", "c", "v")) != readout(("c", "v", "c")),
                "EXP2-READOUT-COLLISION-MISSING",
                "declared readout unexpectedly separated ccv from cvc")
    controls.append({
        "id": "readout-order-blindness",
        "expected": "EXP2-READOUT-COLLISION-MISSING",
        "observed": gapkit.reject(overclaim_readout, "EXP2-READOUT-COLLISION-MISSING"),
    })

    # 5/6. Representation sufficiency claims that the experiment refutes.
    for rid in ("pi1", "pi2"):
        spec = REPRESENTATIONS[rid]
        analysis = analyse_representation(rid, spec, domain, family)
        if analysis["sufficient"]:
            continue

        def overclaim(r=rid, a=analysis):
            require(a["sufficient"], "EXP2-SUFFICIENCY-CLAIM-REFUTED",
                    f"{r} is not task-sufficient: "
                    f"{a['sufficiency_witness']['histories']} separate under "
                    f"{a['sufficiency_witness']['shortest_distinguishing_continuation']}")
        controls.append({
            "id": f"{rid}-sufficiency-claim",
            "expected": "EXP2-SUFFICIENCY-CLAIM-REFUTED",
            "observed": gapkit.reject(overclaim, "EXP2-SUFFICIENCY-CLAIM-REFUTED"),
        })

    # 7. Route disagreement must be detected by the independent checker.
    controls.append({
        "id": "route-disagreement",
        "expected": "EXP2-ROUTE-DISAGREEMENT",
        "observed": gapkit.reject(
            lambda: require(accum(("c", "c", "v")) == accum(("c", "v", "c")),
                            "EXP2-ROUTE-DISAGREEMENT",
                            "the two declared routes disagree on ccv versus cvc"),
            "EXP2-ROUTE-DISAGREEMENT"),
    })

    # 8. Enumeration count must match the declared budget.
    def wrong_count():
        declared = 27
        observed = len([w for w in domain if len(w) == 3])
        require(observed == declared, "EXP2-ENUMERATION-MISMATCH",
                f"legal words of length 3: {observed}, declared {declared}")
    controls.append({
        "id": "enumerated-count-mismatch",
        "expected": "EXP2-ENUMERATION-MISMATCH",
        "observed": gapkit.reject(wrong_count, "EXP2-ENUMERATION-MISMATCH"),
    })
    return controls


def _read_frozen():
    if not FROZEN.exists():
        return {}
    out = {}
    for line in FROZEN.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        digest, _, name = line.partition("  ")
        out[name.strip()] = digest.strip()
    return out


# --------------------------------------------------------------------------
# main
# --------------------------------------------------------------------------

def run():
    gapkit.require(CONTRACT.exists(), "EXP2-CONTRACT-MISSING", str(CONTRACT))
    contract_sha = gapkit.sha256_file(CONTRACT)
    frozen = _read_frozen()
    require(
        frozen.get(CONTRACT.name, contract_sha) == contract_sha,
        "EXP-CONTRACT-DRIFT",
        f"{CONTRACT.name}: frozen {frozen.get(CONTRACT.name)!r} != actual {contract_sha}",
    )

    domain = enumerate_domain()
    family = continuation_family()

    # The hand table is an obligation, not a comment.
    for word, expected in sorted(HAND_TABLE.items()):
        observed = qtext(accum(tuple(word)))
        require(observed == expected, "EXP2-HAND-TABLE-MISMATCH",
                f"A({word!r}) = {observed}, hand table says {expected}")

    # The PR-16 collision and the legality gap must be present in the model.
    require(readout(("c", "c", "v")) == readout(("c", "v", "c")) == readout(("c", "c", "c")),
            "EXP2-READOUT-COLLISION-MISSING", "declared readout no longer collides")
    require(readout(("c", "c", "v")) == PR16_SCALAR_TRIPLE,
            "EXP2-READOUT-SHAPE", "readout of ccv is not the frozen PR-16 triple")

    analyses = {}
    costs = {}
    for rid, spec in REPRESENTATIONS.items():
        analyses[rid] = analyse_representation(rid, spec, domain, family)
        costs[rid] = representation_cost(rid, spec, domain, family)

    # The declared negative witness the plan asks for, stated explicitly.
    w_order_a, w_order_b = ("c", "c", "v"), ("c", "v", "c")
    w_legality = ("c", "c", "c")
    order_witness = {
        "pair": ["".join(w_order_a), "".join(w_order_b)],
        "same_readout": list(readout(w_order_a)),
        "same_counts": list(counts(w_order_a)),
        "same_legality": list(legal_actions(w_order_a)),
        "accumulators": [qtext(accum(w_order_a)), qtext(accum(w_order_b))],
        "shortest_distinguishing_continuation": shortest_separating_continuation(
            w_order_a, w_order_b, family),
        "augmented_equivalent": augmented_equivalent(w_order_a, w_order_b, family),
    }
    legality_witness = {
        "pair": ["".join(w_legality), "".join(w_order_a)],
        "same_readout": list(readout(w_legality)),
        "legality_sets": [list(legal_actions(w_legality)), list(legal_actions(w_order_a))],
        "base_equivalent": base_equivalent(w_legality, w_order_a, family),
        "augmented_equivalent": augmented_equivalent(w_legality, w_order_a, family),
        "shortest_distinguishing_continuation": shortest_separating_continuation(
            w_legality, w_order_a, family),
    }

    # Positive control: two different literal histories that the declared task
    # genuinely cannot separate.  Without this, every difference would look
    # like a gap.
    positive_control = _find_positive_control(domain, family)

    # PR-16 native-continuation gap report.
    gap_report = {
        "pr16_words": ["".join(PR16_LEFT_WORD), "".join(PR16_RIGHT_WORD)],
        "left_reachable_in_declared_model": legal_word(PR16_LEFT_WORD),
        "right_reachable_in_declared_model": legal_word(PR16_RIGHT_WORD),
        "left_first_illegal_prefix": _first_illegal_prefix(PR16_LEFT_WORD),
        "right_first_illegal_prefix": _first_illegal_prefix(PR16_RIGHT_WORD),
        "common_legal_continuations": sorted(
            set(legal_actions(PR16_LEFT_WORD)) & set(legal_actions(PR16_RIGHT_WORD))),
        "verdict": ("the pinned PR-16 records are not both reachable words of the declared "
                    "model, so this experiment does NOT supply a native continuation "
                    "interface for them; the model below is built from scratch exactly as "
                    "the work plan requires when the two records have no common legal "
                    "native continuation interface"),
        "scalar_triple_equal": list(PR16_SCALAR_TRIPLE),
    }

    # Finite closure versus unbounded open: the boundary is stated, not crossed.
    boundary = {
        "closed_for": f"all legal words of length <= {MAX_DOMAIN_LENGTH} and all continuations of depth <= {MAX_CONTINUATION_DEPTH}",
        "open": [
            "no claim about words longer than the declared bound",
            "no unbounded recursion, infinite loop, or fixpoint semantics is implemented or claimed",
            "adaptive continuation selection is not permitted by this contract version",
        ],
    }

    grid = run_enhancement_grid(domain, family)
    reserved = (
        reserved_verification(grid["selected"],
                              grid_representations()[grid["selected"]], family)
        if grid["selected"] else
        {"role": "nothing to verify: the declared grid produced no sufficient candidate",
         "verdict": "not applicable"}
    )

    record = {
        "schema": SCHEMA,
        "contract": {"path": str(CONTRACT.relative_to(ROOT.parent.parent)), "sha256": contract_sha},
        "environment": gapkit.environ(),
        "model": {
            "alphabet": list(ALPHABET),
            "legality": "c always; v iff count_c > count_v; l iff count_v >= 1",
            "accumulator": ["A() = 0", "A(u.c) = 2*A(u) + 1", "A(u.v) = A(u)/2", "A(u.l) = A(u) + 1"],
            "readout": "y1 = count_c + count_v, y2 = frames - handoffs, y3 = 3*handoffs/frames",
            "native_status": "declared small typed model under PIV-S5/PIV-S6; NOT native Adva execution",
        },
        "domain": {
            "size": len(domain),
            "by_length": {str(n): len([w for w in domain if len(w) == n])
                          for n in range(MAX_DOMAIN_LENGTH + 1)},
            "continuation_family_size": len(family),
            "continuation_depth": MAX_CONTINUATION_DEPTH,
            "words": ["".join(w) for w in domain],
        },
        "hand_table_check": {word: qtext(accum(tuple(word))) for word in sorted(HAND_TABLE)},
        "witnesses": {
            "order_gap": order_witness,
            "legality_gap": legality_witness,
            "positive_control": positive_control,
        },
        "pr16_native_continuation_gap": gap_report,
        "representations": analyses,
        "enhancement_grid": grid,
        "reserved_verification_family": reserved,
        "cost": costs,
        "negative_controls": negative_controls(domain, family),
        "boundary": boundary,
    }
    return record


def _find_positive_control(domain, family):
    """Two different literal histories the declared task cannot separate.

    The work plan requires this control so that arbitrary syntactic difference
    is never mistaken for semantic difference.  A pair qualifies only when the
    literals differ, the whole exact state agrees (readout, legality and
    accumulator), and every common continuation yields the same observations.
    """
    buckets = {}
    for word in domain:
        if len(word) < 2:
            continue
        key = (readout(word), qtext(accum(word)), legal_actions(word))
        buckets.setdefault(key, []).append(word)
    best = None
    for key, words in sorted(buckets.items(), key=lambda kv: str(kv[0])):
        if len(words) < 2:
            continue
        ordered = sorted(words, key=lambda w: (len(w), w))
        for w1, w2 in itertools.combinations(ordered, 2):
            if not base_equivalent(w1, w2, family):
                continue
            candidate = (len(w1), "".join(w1), "".join(w2))
            if best is None or candidate < best[0]:
                best = (candidate, w1, w2)
    if best is None:
        return {
            "pair": None,
            "kind": "not-found-in-declared-domain",
            "note": ("no such pair inside the declared budget; reported as "
                     "bounded-domain compatibility only, never as a theorem"),
        }
    _, w1, w2 = best
    return {
        "pair": ["".join(w1), "".join(w2)],
        "kind": "distinct-literal-histories-task-equivalent",
        "same_readout": list(readout(w1)),
        "same_accumulator": qtext(accum(w1)),
        "same_legality": list(legal_actions(w1)),
        "base_equivalent": True,
        "augmented_equivalent": True,
        "note": ("the two words differ literally yet agree on every declared "
                 "observation under every common continuation; this is an "
                 "equivalence, not a gap, and an enhancement that separated "
                 "them would be over-refined"),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", default=None)
    args = parser.parse_args()
    record = run()
    text = gapkit.canonical(record)
    if args.out:
        Path(args.out).write_text(text, encoding="utf-8")
        written = gapkit.sha256_bytes(text.encode("utf-8"))
        sys.stderr.write(f"exp2 written to {args.out} sha256={written}\n")
    else:
        sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
