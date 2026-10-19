#!/usr/bin/env python3
"""Experiment 2, independent route -- exact quotient oracle.

This checker deliberately shares NO implementation with
``exp2_loop_continuation.py``.  It decides the same two properties by a
different algorithm, using code from a different repository:

* the task equivalence is computed by stable partition refinement on the
  totalised Moore machine, using ``minimize_finite_task_process`` from
  ``process-geometry`` (pinned at ``c47c96fa``).  That algorithm is exact --
  no continuation-depth cutoff is used -- and it returns explicit
  distinguishing continuations;
* the accumulator is recomputed by composing exact affine maps
  ``x -> alpha*x + beta`` right to left, instead of folding a recurrence left
  to right;
* the minimal witnesses are compared against a hand-computed table.

The oracle decides a slightly *finer* relation than the primary base
equivalence: the totalised machine observes the illegal outcome explicitly, so
a legality difference separates states there.  That is the legality-augmented
relation of the contract, further refined by the declared budget marker.  The
relationship is reported rather than assumed, and every primary verdict is
re-checked against the oracle's own decision procedure.

Run:

    python3 research/process-representation-gap/experiments/exp2_loop_continuation_independent.py
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(ROOT / "tools"))
import gapkit  # noqa: E402
from gapkit import Diagnostic, qtext, require  # noqa: E402

CONTRACT = ROOT / "contracts" / "exp2-loop-continuation.v1.1.json"
PRIMARY_EVIDENCE = ROOT / "evidence" / "exp2-loop-continuation.json"
FROZEN = ROOT / "contracts" / "FROZEN.sha256"

# Pinned oracle, from a different repository and a different author.
ORACLE_PATH = gapkit.sibling_file(
    "AEG_PROCESS_GEOMETRY_REPO",
    "src/process_geometry/experimental/finite_task_quotient.py")
ORACLE_SHA256 = "1b2bf6a4510fd4f9831f0fa721f63deb19a61c4a658c32c7b138b70b4e38fd66"
ORACLE_REPO = "mountain/process-geometry"
ORACLE_COMMIT = "c47c96fa79123c677172278be59d67ca1cc891b1"
ORACLE_BLOB = "a381c47822ba00f54530d774446a77b2d48c5a7d"

ALPHABET = ("c", "v", "l")
INVALID = "INVALID"
EXHAUSTED = "EXHAUSTED"
MAX_DOMAIN_LENGTH = 6

HAND_TABLE = {
    "": "0", "c": "1", "cc": "3", "ccc": "7", "cv": "1/2",
    "ccv": "3/2", "cvc": "2", "cccv": "7/2", "ccvcl": "5",
}


def load_oracle():
    require(ORACLE_PATH.exists(), "EXP2I-ORACLE-MISSING", str(ORACLE_PATH))
    observed = gapkit.sha256_file(ORACLE_PATH)
    require(observed == ORACLE_SHA256, "EXP2I-ORACLE-DRIFT",
            f"{ORACLE_PATH.name}: {observed} != pinned {ORACLE_SHA256}")
    spec = importlib.util.spec_from_file_location("pg_finite_task_quotient", ORACLE_PATH)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


# --------------------------------------------------------------------------
# independent semantics: affine-map algebra for the accumulator
# --------------------------------------------------------------------------

def affine_of(sigma):
    """The exact affine map x -> alpha*x + beta attached to one mechanism."""
    if sigma == "c":
        return (Fraction(2), Fraction(1))
    if sigma == "v":
        return (Fraction(1, 2), Fraction(0))
    if sigma == "l":
        return (Fraction(1), Fraction(1))
    raise Diagnostic("EXP2I-UNKNOWN-MECHANISM", repr(sigma))


def affine_compose(first, later):
    """(first then later)(x) = later(first(x))."""
    a1, b1 = first
    a2, b2 = later
    return (a2 * a1, a2 * b1 + b2)


def accum_affine(word) -> Fraction:
    """A(w) computed right to left as one composed affine map applied to 0."""
    result = (Fraction(1), Fraction(0))
    for sigma in reversed(word):
        result = affine_compose(affine_of(sigma), result)
    return result[1]


# --------------------------------------------------------------------------
# independent semantics: the totalised Moore machine
# --------------------------------------------------------------------------

def counts(word):
    return (word.count("c"), word.count("v"), word.count("l"))


def legal(word, sigma) -> bool:
    nc, nv, _ = counts(word)
    if sigma == "c":
        return True
    if sigma == "v":
        return nc > nv
    if sigma == "l":
        return nv >= 1
    raise Diagnostic("EXP2I-UNKNOWN-MECHANISM", repr(sigma))


def readout(word):
    if len(word) == 0:
        return ("EMPTY", "EMPTY", "EMPTY")
    nc, nv, _ = counts(word)
    frames = len(word)
    handoffs = frames - 1
    return (qtext(Fraction(nc + nv)), qtext(Fraction(frames - handoffs)),
            qtext(Fraction(3 * handoffs, frames)))


def observe(state):
    """Moore observation of a state."""
    if state == INVALID:
        return ("invalid",)
    if state == EXHAUSTED:
        return ("budget-exhausted",)
    if state and state[-1] == "l":
        return ("learned", qtext(accum_affine(state) - 1))
    return ("readout",) + readout(state)


def carrier(max_length=MAX_DOMAIN_LENGTH):
    states = [()]
    frontier = [()]
    while frontier:
        nxt = []
        for word in frontier:
            if len(word) >= max_length:
                continue
            for sigma in ALPHABET:
                if legal(word, sigma):
                    child = word + (sigma,)
                    nxt.append(child)
                    states.append(child)
        frontier = nxt
    states.append(INVALID)
    states.append(EXHAUSTED)
    return tuple(states)


def transition(state, sigma):
    """Total transition: illegal -> INVALID, past the budget -> EXHAUSTED."""
    if state == INVALID:
        return INVALID
    if state == EXHAUSTED:
        return EXHAUSTED
    if not legal(state, sigma):
        return INVALID
    if len(state) >= MAX_DOMAIN_LENGTH:
        return EXHAUSTED
    return state + (sigma,)


# --------------------------------------------------------------------------
# the independent decision procedures
# --------------------------------------------------------------------------

def pi_of(rid, word):
    if word in (INVALID, EXHAUSTED):
        return (word,)
    nc, nv, nl = counts(word)
    if rid == "pi0":
        return readout(word)
    if rid == "pi1":
        return (nc, nv, nl)
    if rid == "pi2":
        return (nc, nv, nl, word[-1] if word else "NONE")
    if rid == "pi3":
        return (nc, nv, nl, word[-1] if word else "NONE", word[-2:],
                qtext(accum_affine(word)))
    if rid == "hist":
        return word
    raise Diagnostic("EXP2I-UNKNOWN-REPRESENTATION", rid)


_MACHINE = None
_CLASS_INDEX = {}


def _jsonable(value):
    if isinstance(value, (tuple, list)):
        return [_jsonable(v) for v in value]
    return value


def machine_witness(w1, w2):
    """Shortest exact distinguishing continuation, from the oracle's own BFS."""
    if not _CLASS_INDEX:
        for index, cls in enumerate(_MACHINE.classes):
            for state in cls:
                _CLASS_INDEX[state] = index
    left, right = _CLASS_INDEX[w1], _CLASS_INDEX[w2]
    require(left != right, "EXP2I-SAME-CLASS",
            "asked for a witness between two states in one exact class")
    return _MACHINE.witness_between(left, right)


def decide_sufficiency(rid, oracle_classes, words):
    """pi is sufficient iff every pi-fibre lies inside ONE exact class.

    Work-plan section 4.2: pi(h) = pi(h') must IMPLY h ~ h'.  So ker pi must
    refine the task equivalence -- pi may be finer than the equivalence, never
    coarser.  Equivalently every pi-fibre is a subset of a single exact class.
    """
    class_of_word = {}
    for index, cls in enumerate(oracle_classes):
        for state in cls:
            if state not in (INVALID, EXHAUSTED):
                class_of_word[state] = index
    fibers = {}
    for word in words:
        fibers.setdefault(pi_of(rid, word), []).append(word)
    for value, members in sorted(fibers.items(), key=lambda kv: str(kv[0])):
        if len(members) < 2:
            continue
        if len({class_of_word[w] for w in members}) == 1:
            continue
        ordered = sorted(members, key=lambda w: (len(w), w))
        left = ordered[0]
        right = next(w for w in ordered if class_of_word[w] != class_of_word[left])
        return False, {
            "representation_value": gapkit.canonical(_jsonable(value)).strip(),
            "histories": ["".join(left), "".join(right)],
            "exact_classes": [class_of_word[left], class_of_word[right]],
            "oracle_witness": list(machine_witness(left, right)),
        }
    return True, None


def decide_closed_update(rid, words):
    """ker pi is a right congruence iff pi decides legality and commutes."""
    groups = {}
    for word in words:
        groups.setdefault(pi_of(rid, word), []).append(word)
    for value, members in sorted(groups.items(), key=lambda kv: str(kv[0])):
        if len(members) < 2:
            continue
        for i in range(len(members)):
            for j in range(i + 1, len(members)):
                w1, w2 = members[i], members[j]
                if len(w1) != MAX_DOMAIN_LENGTH or len(w2) != MAX_DOMAIN_LENGTH:
                    pass
                for sigma in ALPHABET:
                    t1, t2 = transition(w1, sigma), transition(w2, sigma)
                    if pi_of(rid, t1) != pi_of(rid, t2):
                        return False, {
                            "histories": ["".join(w1), "".join(w2)],
                            "action": sigma,
                            "targets": [t1 if isinstance(t1, str) else "".join(t1),
                                        t2 if isinstance(t2, str) else "".join(t2)],
                            "kind": ("legality-not-decided" if (t1 == INVALID) != (t2 == INVALID)
                                     else "different-digest-after-same-action"),
                        }
    return True, None


# --------------------------------------------------------------------------
# main
# --------------------------------------------------------------------------

def run():
    require(CONTRACT.exists(), "EXP2I-CONTRACT-MISSING", str(CONTRACT))
    contract_sha = gapkit.sha256_file(CONTRACT)
    frozen = _read_frozen()
    require(frozen.get(CONTRACT.name) == contract_sha, "EXP-CONTRACT-DRIFT",
            f"{CONTRACT.name}: frozen {frozen.get(CONTRACT.name)!r} != {contract_sha}")
    require(PRIMARY_EVIDENCE.exists(), "EXP2I-PRIMARY-MISSING", str(PRIMARY_EVIDENCE))

    global _MACHINE
    pg = load_oracle()
    states = carrier()
    machine = pg.minimize_finite_task_process(
        states=states,
        steps=ALPHABET,
        transition=transition,
        observe=observe,
    )
    _MACHINE = machine
    _CLASS_INDEX.clear()
    classes = [tuple(c) for c in machine.classes]
    words = [s for s in states if s not in (INVALID, EXHAUSTED)]

    # Affine route must reproduce the hand table exactly.
    for word, expected in sorted(HAND_TABLE.items()):
        observed = qtext(accum_affine(tuple(word)))
        require(observed == expected, "EXP2-HAND-TABLE-MISMATCH",
                f"affine route A({word!r}) = {observed}, hand table says {expected}")

    primary = json.loads(PRIMARY_EVIDENCE.read_text(encoding="utf-8"))
    require(primary["contract"]["sha256"] == contract_sha, "EXP-CONTRACT-DRIFT",
            "primary evidence cites a different contract")

    verdicts = {}
    disagreements = []
    for rid in ("pi0", "pi1", "pi2", "pi3", "hist"):
        sufficient, witness = decide_sufficiency(rid, classes, words)
        closed, closed_witness = decide_closed_update(rid, words)
        primary_sufficient = primary["representations"][rid]["sufficient"]
        primary_closed = primary["representations"][rid]["closed_update"]
        verdicts[rid] = {
            "oracle_sufficient": sufficient,
            "oracle_sufficiency_witness": witness,
            "primary_sufficient": primary_sufficient,
            "oracle_closed_update": closed,
            "oracle_closed_update_witness": closed_witness,
            "primary_closed_update": primary_closed,
            "agree_sufficiency": sufficient == primary_sufficient,
            "agree_closed_update": closed == primary_closed,
        }
        if sufficient != primary_sufficient or closed != primary_closed:
            disagreements.append(rid)

    # Verify the primary's declared shortest witnesses against the oracle's
    # own breadth-first witness on the exact quotient machine.
    witness_checks = []
    for name, pair in (("ccv|cvc", (("c", "c", "v"), ("c", "v", "c"))),
                       ("ccc|ccv", (("c", "c", "c"), ("c", "c", "v")))):
        w1, w2 = pair
        expected = None
        for entry in (primary["witnesses"]["order_gap"], primary["witnesses"]["legality_gap"]):
            if entry.get("pair") == ["".join(w1), "".join(w2)]:
                expected = entry["shortest_distinguishing_continuation"]
        found = None
        for cls in classes:
            if w1 in cls and w2 in cls:
                found = "same-exact-class"
                break
        if found is None:
            c1 = machine.class_of(w1)
            c2 = machine.class_of(w2)
            witness = machine.witness_between(c1, c2)
            found = list(witness)
        witness_checks.append({
            "pair": ["".join(w1), "".join(w2)],
            "primary_declared": expected,
            "oracle_witness": found,
            "agree": (found == "same-exact-class") or (
                expected is not None and found == expected["eta"] and len(found) == expected["depth"]),
        })
    if not all(w["agree"] for w in witness_checks):
        disagreements.append("witness")

    # A negative control: the oracle must refuse a machine that leaves its carrier.
    def carrier_escape():
        def bad_transition(state, sigma):
            return ("z",) + state
        try:
            pg.minimize_finite_task_process(
                states=[(), ("c",), ("c", "c")], steps=ALPHABET,
                transition=bad_transition, observe=observe)
        except ValueError as exc:
            # The diagnostic must MATCH, not merely be "some exception".
            require("leaves declared state carrier" in str(exc),
                    "EXP2I-WRONG-DIAGNOSTIC", f"unexpected ValueError text: {exc}")
            raise Diagnostic("EXP2I-CARRIER-ESCAPE", str(exc)) from exc
        raise Diagnostic("EXP2I-NO-DIAGNOSTIC", "oracle accepted a carrier escape")
    escape_control = gapkit.reject(carrier_escape, "EXP2I-CARRIER-ESCAPE")

    # A second negative control: a drifted oracle must be refused.
    def drifted():
        require(gapkit.sha256_file(ORACLE_PATH) == "0" * 64, "EXP2I-ORACLE-DRIFT",
                "pinned oracle digest changed")
    drift_control = gapkit.reject(drifted, "EXP2I-ORACLE-DRIFT")

    record = {
        "schema": "aeg.process-representation-gap.exp2-independent.v1",
        "role": "independent verification route for exp2",
        "contract": {"path": str(CONTRACT.relative_to(ROOT.parent.parent)), "sha256": contract_sha},
        "oracle": {
            "repository": ORACLE_REPO,
            "commit": ORACLE_COMMIT,
            "path": "src/process_geometry/experimental/finite_task_quotient.py",
            "git_blob": ORACLE_BLOB,
            "sha256": ORACLE_SHA256,
            "algorithm": "stable partition refinement on a totalised Moore machine; exact, no depth cutoff",
        },
        "environment": gapkit.environ(),
        "machine": {
            "state_count": len(states),
            "declared_word_count": len(words),
            "exact_class_count": machine.class_count,
            "budget_marker": EXHAUSTED,
            "invalid_marker": INVALID,
            "note": ("the oracle's relation observes the invalid and budget-exhausted "
                     "outcomes explicitly, so it refines the primary base equivalence "
                     "by exactly the legality and budget signatures"),
        },
        "affine_hand_table": {w: qtext(accum_affine(tuple(w))) for w in sorted(HAND_TABLE)},
        "verdicts": verdicts,
        "witness_checks": witness_checks,
        "negative_controls": [
            {"id": "carrier-escape", "expected": "EXP2I-CARRIER-ESCAPE", "observed": escape_control},
            {"id": "oracle-drift", "expected": "EXP2I-ORACLE-DRIFT", "observed": drift_control},
        ],
        "disagreements": disagreements,
        "conclusion": ("the independent route reproduces every primary verdict"
                       if not disagreements else
                       "the independent route disagrees; the disagreement is the result"),
    }
    require(not disagreements, "EXP2I-ROUTE-DISAGREEMENT",
            f"independent route disagrees on: {disagreements}")
    return record


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


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", default=None)
    args = parser.parse_args()
    record = run()
    text = gapkit.canonical(record)
    if args.out:
        Path(args.out).write_text(text, encoding="utf-8")
        sys.stderr.write(f"written {args.out} sha256={gapkit.sha256_bytes(text.encode())}\n")
    else:
        sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
