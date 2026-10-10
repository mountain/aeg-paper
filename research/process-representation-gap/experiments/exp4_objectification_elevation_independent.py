#!/usr/bin/env python3
"""Experiment 4 -- independent route.

Contract: research/process-representation-gap/contracts/exp4-objectification-elevation.v1.json

This file is a SECOND checker, written after the primary implementation, that
re-derives the primary's declared numbers by different algebra and a different
enumeration strategy, and raises ``EXP4-ROUTE-DISAGREEMENT`` the moment the two
routes disagree.

Why this is independent (and where it is not):

* Affine part -- genuinely different algebra.  The primary represents an affine
  action by the pair ``(b, k)`` and folds pairs with the formula
  ``(b,k)*(c,l) = (b + k*c, k*l)`` over a word enumerated by length.  This file
  represents the same action by its exact 2x2 upper-triangular matrix
  ``[[k, b], [0, 1]]`` over ``Q``, multiplies matrices explicitly, recovers the
  pair from the matrix, and enumerates the object layer by breadth-first search
  with deduplication instead of enumerating words.
* Affine part -- separate literal input.  The hand table frozen in the contract
  is parsed here and compared with this route, so a wrong literal is caught
  without the primary being consulted.
* Braid part -- weaker independence, stated plainly.  The free-group model has
  to be re-implemented (there is no second algebra for Artin's action available
  inside this contract), so the braid check is a separate implementation plus a
  genuinely different counting route: the number of object classes is counted by
  the probe signatures instead of by equality of automorphism triples.
* The two files never import each other.  The primary's evidence JSON is read as
  DATA only.  The only shared module is gapkit's deterministic JSON serialisation,
  which carries no experiment semantics.

Run:

    python3 research/process-representation-gap/experiments/exp4_objectification_elevation_independent.py
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
from gapkit import require  # noqa: E402

CONTRACT = ROOT / "contracts" / "exp4-objectification-elevation.v1.json"
FROZEN = ROOT / "contracts" / "FROZEN.sha256"
EVIDENCE = ROOT / "evidence" / "exp4-objectification-elevation.json"

PRIMARY_SCHEMA = "aeg.process-representation-gap.exp4.v1"
INDEPENDENT_SCHEMA = PRIMARY_SCHEMA + ".independent"

BASE_LENGTH = 5
EXP2_ALL_LENGTH = 5
EXP2_LEGAL_LENGTH = 6
EXP5_LENGTH = 6
STRANDS = 3
DISAGREE = "EXP4-ROUTE-DISAGREEMENT"


# --------------------------------------------------------------------------
# route 1: exact 2x2 upper-triangular matrices over Q
# --------------------------------------------------------------------------

def mat(scale, shift):
    """[[k, b], [0, 1]] representing x -> k*x + b."""
    return ((Fraction(scale), Fraction(shift)), (Fraction(0), Fraction(1)))


def mat_mul(A, B):
    return (
        (A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]),
        (A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]),
    )


def mat_pair(M):
    """Recover (b, k) from the matrix; the lower-left entry must be 0."""
    require(M[1][0] == 0 and M[1][1] == 1, DISAGREE,
            f"the matrix {M} is not of the declared upper-triangular form")
    return (M[0][1], M[0][0])


def mat_apply(M, x):
    return M[0][0] * x + M[0][1]


IDENTITY_MATRIX = mat(1, 0)

GENERATOR_MATRIX = {
    ("T", 0): mat(1, 0), ("T", -2): mat(1, -2), ("T", 1): mat(1, 1), ("T", 3): mat(1, 3),
    ("D", 1): mat(1, 0), ("D", 2): mat(2, 0), ("D", 3): mat(3, 0), ("D", 5): mat(5, 0),
    ("D", 6): mat(6, 0),
}


def generator_matrix(g):
    kind, value = g
    if kind == "T":
        return mat(1, value)
    require(kind == "D" and isinstance(value, int) and value >= 1, DISAGREE,
            f"generator {g} is outside the declared domain")
    return mat(value, 0)


def word_matrix(word):
    """Chronological fold, applied with matrix multiplication on the left."""
    M = IDENTITY_MATRIX
    for g in word:
        require(g[0] in ("T", "D") and isinstance(g[1], int), DISAGREE,
                f"generator {g} is outside the declared generator types")
        M = mat_mul(generator_matrix(g), M)
    return M


def bfs_objects(alphabet, depth):
    """Breadth-first enumeration of the object layer with deduplication."""
    seen = {IDENTITY_MATRIX}
    frontier = [IDENTITY_MATRIX]
    cumulative = {0: 1}
    for level in range(1, depth + 1):
        nxt = []
        for M in frontier:
            for g in alphabet:
                N = mat_mul(generator_matrix(g), M)
                if N not in seen:
                    seen.add(N)
                    nxt.append(N)
        frontier = nxt
        cumulative[level] = len(seen)
    return seen, cumulative


def word_count(alphabet_size, max_length):
    return sum(alphabet_size ** n for n in range(max_length + 1))


# --------------------------------------------------------------------------
# route 2: separate re-implementation of the experiment-5 free-group model
# --------------------------------------------------------------------------

def reduce_free(word):
    stack = []
    for letter in word:
        if stack and stack[-1] == -letter:
            stack.pop()
        else:
            stack.append(letter)
    return tuple(stack)


def invert_free(word):
    return tuple(-letter for letter in reversed(word))


def substitute(automorphism, word):
    table = {}
    for index in range(STRANDS):
        table[index + 1] = automorphism[index]
    out = []
    for letter in word:
        image = table[abs(letter)]
        out.extend(invert_free(image) if letter < 0 else image)
    return reduce_free(out)


def o_compose(first, later):
    return tuple(substitute(first, later[index]) for index in range(STRANDS))


PHI = {
    1: ((1, 2, -1), (1,), (3,)),
    2: ((1,), (2, 3, -2), (2,)),
    -1: ((2,), (-2, 1, 2), (3,)),
    -2: ((1,), (3,), (-3, 2, 3)),
}
PERM_LETTER = {1: (1, 0, 2), 2: (0, 2, 1), -1: (1, 0, 2), -2: (0, 2, 1)}
PERM_ID = (0, 1, 2)
PROBES = (
    ("x1", (1,)),
    ("x2", (2,)),
    ("x3", (3,)),
    ("x1x2", (1, 2)),
    ("x1x2x3", (1, 2, 3)),
    ("x1x2x1^-1", (1, 2, -1)),
    ("commutator", (1, 2, 3, -1, -2, -3)),
    ("(x1x2)^3", (1, 2, 1, 2, 1, 2)),
)
LETTERS = (1, 2, -1, -2)


def object_of(word):
    M = ((1,), (2,), (3,))
    for letter in word:
        M = o_compose(PHI[letter], M)
    return M


def perm_of(word):
    result = PERM_ID
    for letter in word:
        result = tuple(result[PERM_LETTER[letter][i]] for i in range(STRANDS))
    return result


def probe_signature(M):
    return tuple(substitute(M, probe) for _, probe in PROBES)


def words_over(alphabet, max_length):
    return [tuple(w) for w in gapkit.words(alphabet, max_length)]


# --------------------------------------------------------------------------
# contract literals (parsed here, so the table is an independent input)
# --------------------------------------------------------------------------

def parse_pair_literal(text):
    """Parse '(b=6,k=3)' into (Fraction(6), Fraction(3))."""
    body = text.strip()
    require(body.startswith("(") and body.endswith(")"), DISAGREE,
            f"malformed pair literal {text!r}")
    fields = {}
    for part in body[1:-1].split(","):
        name, _, value = part.partition("=")
        fields[name.strip()] = Fraction(value.strip())
    require(set(fields) == {"b", "k"}, DISAGREE, f"malformed pair literal {text!r}")
    return (fields["b"], fields["k"])


def parse_base_hand_name(name):
    """Parse '(D_1,T_-4)' into a tuple of generators."""
    body = name.strip()
    require(body.startswith("(") and body.endswith(")"), DISAGREE,
            f"malformed hand-table name {name!r}")
    inner = body[1:-1]
    if inner == "":
        return ()
    out = []
    for token in inner.split(","):
        kind, _, value = token.partition("_")
        require(kind in ("T", "D"), DISAGREE, f"malformed generator token {token!r}")
        out.append((kind, int(value)))
    return tuple(out)


def parse_exp2_hand_name(name):
    return tuple(name)


# --------------------------------------------------------------------------
# comparison helpers
# --------------------------------------------------------------------------

class Route:
    def __init__(self):
        self.checks = 0
        self.details = []

    def agree(self, label, expected, observed, note=""):
        self.checks += 1
        require(expected == observed, DISAGREE,
                f"{label}: primary {expected!r} vs independent {observed!r}"
                + (f" ({note})" if note else ""))
        self.details.append({"label": label, "value": _plain(observed), "note": note})
        return _plain(observed)

    def as_record(self):
        return {"checks": self.checks, "compared": self.details}


def _plain(value):
    if isinstance(value, Fraction):
        return qtext_independent(value)
    if isinstance(value, (tuple, list)):
        return [_plain(v) for v in value]
    if isinstance(value, dict):
        return {str(k): _plain(v) for k, v in sorted(value.items(), key=lambda kv: str(kv[0]))}
    return value


def qtext_independent(value):
    value = Fraction(value)
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def pair_text_integer(pair):
    b, k = pair
    require(k.denominator == 1 and b.denominator == 1, DISAGREE,
            f"the integer model produced the rational pair {pair}")
    return (int(b), int(k))


# --------------------------------------------------------------------------
# main comparison
# --------------------------------------------------------------------------

def run(evidence_path):
    contract_sha = gapkit.sha256_file(CONTRACT)
    ledger = _read_ledger()
    require(ledger.get(CONTRACT.name) == contract_sha, "EXP-CONTRACT-DRIFT",
            f"{CONTRACT.name}: ledger {ledger.get(CONTRACT.name)!r} != actual {contract_sha}")
    contract = gapkit.json.loads(CONTRACT.read_text(encoding="utf-8"))

    require(Path(evidence_path).exists(), "EXP4-EVIDENCE-MISSING", str(evidence_path))
    primary = gapkit.json.loads(Path(evidence_path).read_text(encoding="utf-8"))
    require(primary.get("schema") == PRIMARY_SCHEMA, DISAGREE,
            f"the evidence schema is {primary.get('schema')!r}, expected {PRIMARY_SCHEMA!r}")
    require(primary["contract"]["sha256"] == contract_sha, DISAGREE,
            "the evidence cites a different contract digest")

    route = Route()

    # 1. declared word counts and sweep size (combinatorial, not enumerated)
    base_counts = primary["domain"]["base_sweep"]
    route.agree("base sweep per length",
                base_counts,
                {str(n): 5 ** n for n in range(BASE_LENGTH + 1)},
                "recomputed as |alphabet|^n")
    route.agree("base sweep total", primary["domain"]["base_sweep_total"],
                word_count(5, BASE_LENGTH), "5^0 + ... + 5^5")

    # 2. descent sweep size
    descent = primary["baseline_control"]["gates"]["gate_iii_exact_descent"]
    states = primary["domain"]["declared_states"]
    route.agree("descent check count", descent["checks"],
                word_count(5, BASE_LENGTH) * len(states), "words x declared states")
    route.agree("descent states", descent["states"], states)
    route.agree("descent mismatches", descent["mismatches"], 0)

    # 3. the frozen hand table, parsed from the contract, checked by matrices
    hand = contract["independent_check"]["hand_literal_tables"]["base_model"]
    for name, literal in sorted(hand.items()):
        word = parse_base_hand_name(name)
        expected = parse_pair_literal(literal)
        route.agree(f"hand table {name}", expected, mat_pair(word_matrix(word)),
                    "matrix route versus the frozen literal")

    # 4. the primary's witnesses, re-derived from their words
    witness = primary["baseline_control"]["gates"]["gate_i_task_sufficiency_pi_out"]["minimal_witness"]
    words = witness["words"]
    route.agree("gate-i witness words", words, ["epsilon", "D_2"])
    route.agree("gate-i witness objects", witness["objects"],
                [list(pair_text_integer(mat_pair(word_matrix(parse_base_hand_name(
                    "(" + ("T_0" if w == "epsilon" else w) + ")"))))) for w in words],
                "matrix route versus the primary's recorded objects")
    route.agree("gate-i witness endpoint values", witness["endpoint_values"],
                [0, 0], "both objects evaluate to 0 at the declared initial state")
    for index, values in enumerate(witness["values_at_declared_states"]):
        word = parse_base_hand_name("(" + ("T_0" if words[index] == "epsilon" else words[index]) + ")")
        M = word_matrix(word)
        route.agree(f"gate-i witness values {words[index]}", values,
                    [int(mat_apply(M, x)) for x in states])

    nonempty = primary["baseline_control"]["gates"]["gate_i_task_sufficiency_pi_out"][
        "minimal_witness_both_nonempty"]
    route.agree("second gate-i witness objects", nonempty["objects"],
                [list(pair_text_integer(mat_pair(word_matrix(parse_base_hand_name("(" + w + ")")))))
                 for w in nonempty["words"]])

    # 5. repetition versus uniform action
    repetition = primary["baseline_control"]["repetition_versus_uniform"]
    pinned = repetition["repeated_execution"]["pinned_example"]
    route.agree("pinned T_6 fibre", pinned["schemas"], [[1, 6], [2, 3], [3, 2], [6, 1]],
                "n*a = 6 with a in [-6,6] and n in [1,6]")
    route.agree("T_2^3 and T_3^2 share their endpoint",
                pinned["output"],
                list(pair_text_integer(mat_pair(word_matrix((("T", 2), ("T", 2), ("T", 2)))))),
                "matrix route")
    route.agree("T_3^2 endpoint",
                pinned["output"],
                list(pair_text_integer(mat_pair(word_matrix((("T", 3), ("T", 3)))))))
    naming = repetition["naming_trap"]
    route.agree("named power is the translation T_6", naming["named_object"],
                list(pair_text_integer(mat_pair(word_matrix((("T", 6),))))))
    route.agree("named power inside the lower layer", naming["in_lower_translation_layer"], True)

    # 6. relation sweep: the cross relation on the declared integer sweep
    cross = primary["baseline_control"]["relations"]["cross_relation"]
    a_min, a_max = cross["sweep"]["a"]
    k_min, k_max = cross["sweep"]["k"]
    sweep_checks = 0
    for a in range(a_min, a_max + 1):
        for k in range(k_min, k_max + 1):
            left = mat_pair(word_matrix((("T", a), ("D", k))))
            right = mat_pair(word_matrix((("D", k), ("T", k * a))))
            require(left == right == (Fraction(k * a), Fraction(k)), DISAGREE,
                    f"the matrix route fails the cross relation at a={a}, k={k}: {left} vs {right}")
            sweep_checks += 1
    route.agree("cross-relation sweep size", cross["sweep"]["checks"], sweep_checks)
    route.agree("cross-relation both sides", cross["both_sides_pair"], "(k*a, k)")

    # 7. BFS reachable-object counts (different enumeration strategy)
    growth = primary["cost"]["reachable_object_growth"]
    alphabets = {
        "base_sweep": (("T", -2), ("T", 1), ("T", 3), ("D", 2), ("D", 3)),
        "essay_alphabet": (("T", -2), ("T", 1), ("D", 2), ("D", 3)),
        "translation_only": (("T", -2), ("T", 1)),
        "pure_dilation": (("D", 2), ("D", 3)),
    }
    for name, alphabet in sorted(alphabets.items()):
        _, cumulative = bfs_objects(alphabet, BASE_LENGTH)
        route.agree(f"reachable objects {name}", growth[name]["reachable_objects"],
                    {str(k): v for k, v in sorted(cumulative.items())},
                    "matrix BFS with deduplication")
        route.agree(f"word count {name}", growth[name]["words_up_to_length"],
                    word_count(len(alphabet), BASE_LENGTH))

    # 8. the experiment-2 attempt
    attempt2 = primary["attempts"]["exp2_accumulator_object"]
    route.agree("exp2 letter objects", attempt2["letter_objects"],
                {"c": ["1", "2"], "l": ["1", "1"], "v": ["0", "1/2"]},
                "the declared generator actions on the accumulator carrier")
    exp2_pairs = {
        "c": mat(2, 1),
        "v": mat(Fraction(1, 2), 0),
        "l": mat(1, 1),
    }
    for sigma, M in sorted(exp2_pairs.items()):
        b, k = mat_pair(M)
        route.agree(f"exp2 letter matrix {sigma}", attempt2["letter_objects"][sigma],
                    [qtext_independent(b), qtext_independent(k)])
    legal_words = exp2_legal_domain()
    route.agree("exp2 legal domain", attempt2["domain"]["legal_words"],
                {str(k): v for k, v in sorted(_per_length(legal_words).items())})
    route.agree("exp2 unrestricted domain", attempt2["domain"]["all_words"],
                {str(n): 3 ** n for n in range(EXP2_ALL_LENGTH + 1)})
    descent_checks = (word_count(3, EXP2_ALL_LENGTH) + len(legal_words)) * 10
    route.agree("exp2 descent check count", attempt2["gates"]["gate_iii_exact_descent"]["checks"],
                descent_checks, "(all words + legal words) x 10 declared states")

    # accumulator recurrence against the matrix route's shift coordinate
    accumulator_mismatches = 0
    for word in words_over(("c", "v", "l"), EXP2_ALL_LENGTH):
        M = IDENTITY_MATRIX
        for sigma in word:
            M = mat_mul(exp2_pairs[sigma], M)
        b, _ = mat_pair(M)
        if b != _recurrence(word):
            accumulator_mismatches += 1
    route.agree("exp2 accumulator equals the object value at 0", accumulator_mismatches, 0,
                f"checked on all {word_count(3, EXP2_ALL_LENGTH)} words")

    # the exp2 witnesses, re-derived by the matrix route
    gate2 = attempt2["gates"]["gate_i_task_sufficiency"]
    minimal2 = gate2["minimal_witness"]
    route.agree("exp2 minimal witness words", minimal2["words"], ["cvc", "ccvcv"])
    for index, word in enumerate(minimal2["words"]):
        M = IDENTITY_MATRIX
        for sigma in word:
            M = mat_mul(exp2_pairs[sigma], M)
        b, k = mat_pair(M)
        route.agree(f"exp2 witness object {word}", minimal2["objects"][index],
                    [qtext_independent(b), qtext_independent(k)])
        route.agree(f"exp2 witness accumulator {word}", minimal2["accumulators"][index],
                    qtext_independent(b))
    legality = gate2["legality_channel_witness"]
    for index, word in enumerate(legality["words"]):
        M = IDENTITY_MATRIX
        for sigma in word:
            M = mat_mul(exp2_pairs[sigma], M)
        b, k = mat_pair(M)
        route.agree(f"exp2 legality witness object {word}", legality["object"],
                    [qtext_independent(b), qtext_independent(k)])
    route.agree("exp2 legality witness signatures", legality["legal_signatures"],
                [["c", "l"], ["c"]])

    # the frozen exp2 hand table, parsed from the contract and checked by matrices
    exp2_hand = contract["independent_check"]["hand_literal_tables"]["experiment_2_attempt"]
    for name, literal in sorted(exp2_hand.items()):
        expected = parse_pair_literal(literal)
        M = IDENTITY_MATRIX
        for sigma in parse_exp2_hand_name(name):
            require(sigma in exp2_pairs, DISAGREE, f"unknown experiment-2 letter {sigma!r}")
            M = mat_mul(exp2_pairs[sigma], M)
        route.agree(f"exp2 hand table {name!r}", expected, mat_pair(M),
                    "matrix route versus the frozen literal")

    # 9. the experiment-5 attempt
    attempt5 = primary["attempts"]["exp5_artin_object"]
    crossing = words_over(LETTERS, EXP5_LENGTH)
    route.agree("exp5 crossing-word counts", attempt5["domain"]["crossing_words"],
                {str(n): 4 ** n for n in range(EXP5_LENGTH + 1)})
    route.agree("exp5 crossing-word total", attempt5["domain"]["total"], len(crossing))

    object_classes = {}
    reduced_classes = {}
    perm_classes = {}
    signature_classes = {}
    for word in crossing:
        object_classes.setdefault(object_of(word), word)
        reduced_classes.setdefault(reduce_free(word), word)
        perm_classes.setdefault(perm_of(word), word)
        signature_classes.setdefault(probe_signature(object_of(word)), word)
    layers = {
        "L4_literal_words": len(crossing),
        "L3_free_reduction_classes": len(reduced_classes),
        "L2_artin_object_classes": len(object_classes),
        "L1_endpoint_permutation_classes": len(perm_classes),
        "literal_to_reduced_merges": len(crossing) - len(reduced_classes),
        "reduced_to_object_merges": len(reduced_classes) - len(object_classes),
        "object_to_permutation_merges": len(object_classes) - len(perm_classes),
    }
    route.agree("exp5 layer counts", attempt5["layers"], layers, "re-implemented free-group model")
    route.agree("exp5 object classes counted by probe signatures", len(object_classes),
                len(signature_classes),
                "a genuinely different counting route: signatures on the frozen probe family")

    # the recorded exp5 witnesses, re-derived
    history = attempt5["gates"]["gate_i_task_sufficiency"]["history_task"]
    witness_object = history["witness"]["object"]
    route.agree("exp5 history witness object", witness_object,
                ["".join(("xyz"[abs(l) - 1] + ("" if l > 0 else "^-1")) for l in image)
                 for image in object_of((1, 2, 1))],
                "s1 s2 s1 re-derived in the independent model")
    route.agree("exp5 history witness counts", history["witness"]["generator_counts"],
                [{"s1": 2, "s2": 1, "S1": 0, "S2": 0}, {"s1": 1, "s2": 2, "S1": 0, "S2": 0}])
    route.agree("exp5 history witness permutations", history["witness"]["permutations"],
                [list(perm_of((1, 2, 1))), list(perm_of((2, 1, 2)))])
    route.agree("exp5 braid relation", object_of((1, 2, 1)), object_of((2, 1, 2)))
    route.agree("exp5 s1^2 versus the empty word", history["second_witness"]["objects_equal"],
                object_of(()) == object_of((1, 1)))

    hand5 = contract["independent_check"]["hand_literal_tables"]["experiment_5_attempt"]
    for name, expected in sorted(hand5.items()):
        letters = _parse_exp5_hand_name(name)
        observed = ["".join(("xyz"[abs(l) - 1] + ("" if l > 0 else "^-1")) for l in image)
                    for image in object_of(letters)]
        route.agree(f"exp5 hand table {name}", expected, observed,
                    "independent model versus the frozen literal")

    # 10. elevation verdicts recorded by the primary
    route.agree("baseline elevation verdict",
                primary["baseline_control"]["elevation"]["verdict"], "ELEVATION")
    route.agree("exp2 elevation verdict", attempt2["elevation"]["verdict"], "ELEVATION")
    route.agree("exp5 elevation verdict", attempt5["elevation"]["verdict"], "NO-ELEVATION")
    route.agree("exp5 elevation E2 merges", attempt5["elevation"]["E2"]["merges"],
                len(crossing) - len(object_classes),
                "literal words merged by the object layer")

    # 11. negative-control coverage: every declared code must appear in the evidence
    declared_codes = sorted(control["expected_diagnostic"] for control in contract["negative_controls"])
    observed_codes = sorted(control["observed"]["code"] for control in primary["negative_controls"])
    route.agree("negative-control codes", declared_codes, observed_codes,
                "each declared control must actually raise its declared diagnostic")

    route.agree("evidence interpreter", primary["environment"]["implementation"], "cpython",
                "the frozen evidence records the interpreter that produced it")

    detector = _detector_self_test()

    return {
        "schema": INDEPENDENT_SCHEMA + ".route",
        "contract": {"path": str(CONTRACT.relative_to(ROOT.parent.parent)), "sha256": contract_sha},
        "independent_route": {
            "affine_algebra": "exact 2x2 upper-triangular matrices over Q, composed by matrix multiplication",
            "enumeration": "breadth-first search over the object layer with deduplication",
            "literals": "the contract's hand tables, parsed by this file and checked against this route",
            "braid": ("a separate re-implementation of the free-group model plus a different counting "
                      "route (probe signatures instead of automorphism-triple equality)"),
        },
        "checks": route.as_record(),
        "detector_self_test": detector,
    }


def _parse_exp5_hand_name(name):
    body = name.strip()
    require(body.startswith("(") and body.endswith(")"), DISAGREE,
            f"malformed experiment-5 hand-table name {name!r}")
    inner = body[1:-1]
    if inner == "":
        return ()
    out = []
    for token in inner.split(","):
        token = token.strip()
        if token.startswith("s"):
            out.append(int(token[1:]))
        elif token.startswith("S"):
            out.append(-int(token[1:]))
        else:
            require(False, DISAGREE, f"malformed crossing token {token!r}")
    return tuple(out)


def _recurrence(word):
    """The experiment-2 accumulator, recomputed here from its declared recurrence."""
    value = Fraction(0)
    for sigma in word:
        if sigma == "c":
            value = 2 * value + 1
        elif sigma == "v":
            value = value / 2
        else:
            require(sigma == "l", DISAGREE, f"unknown experiment-2 mechanism {sigma!r}")
            value = value + 1
    return value


def _per_length(word_list):
    out = {}
    for word in word_list:
        out[len(word)] = out.get(len(word), 0) + 1
    return out


def exp2_legal_domain(max_length=EXP2_LEGAL_LENGTH):
    """Re-implementation of the declared experiment-2 legality, written independently."""
    out = [()]
    frontier = [()]
    while frontier:
        nxt = []
        for word in frontier:
            if len(word) >= max_length:
                continue
            for sigma in _legal_actions(word):
                nxt.append(word + (sigma,))
                out.append(word + (sigma,))
        frontier = nxt
    return out


def _legal_actions(word):
    count_c = sum(1 for s in word if s == "c")
    count_v = sum(1 for s in word if s == "v")
    actions = ["c"]
    if count_c > count_v:
        actions.append("v")
    if count_v >= 1:
        actions.append("l")
    return tuple(actions)


def _detector_self_test():
    """Prove that EXP4-ROUTE-DISAGREEMENT is actually raised on a disagreement.

    A checker that can never fail is not a checker, so two disagreements are
    manufactured here: a mutated scalar on the primary side, and a mutated
    matrix product on the independent side.
    """
    def mutated_primary_value():
        probe = Route()
        probe.agree("self-test scalar", 6, 7, "a deliberately mutated primary value")

    first = gapkit.reject(mutated_primary_value, DISAGREE)

    def mutated_matrix_product():
        honest = mat_pair(mat_mul(mat(3, 0), mat(1, 2)))     # word (T_2, D_3) -> (6, 3)
        mutated = mat_pair(mat_mul(mat(3, 0), mat(1, 3)))    # one matrix entry moved
        probe = Route()
        probe.agree("self-test matrix", honest, mutated, "a deliberately mutated matrix product")

    second = gapkit.reject(mutated_matrix_product, DISAGREE)

    def honest_matrix():
        probe = Route()
        return probe.agree("self-test honest matrix", mat_pair(mat_mul(mat(3, 0), mat(1, 2))),
                           (Fraction(6), Fraction(3)), "the undeformed matrix product")
    honest = honest_matrix()

    return {
        "mutated_primary_value": first,
        "mutated_matrix_product": second,
        "honest_comparison_passes": honest,
        "status": "proved",
    }


def _read_ledger():
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
    parser.add_argument("--evidence", default=str(EVIDENCE))
    parser.add_argument("--out", default=None)
    args = parser.parse_args()
    record = run(args.evidence)
    text = gapkit.canonical(record)
    if args.out:
        Path(args.out).write_text(text, encoding="utf-8")
        sys.stderr.write(f"exp4 independent written to {args.out} "
                         f"sha256={gapkit.sha256_bytes(text.encode('utf-8'))}\n")
    else:
        sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:  # noqa: BLE001 - diagnostics are the contract
        code = getattr(exc, "code", None)
        if code is None:
            raise
        sys.stderr.write(f"{code}: {exc.detail}\n")
        raise SystemExit(1)
