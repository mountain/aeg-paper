#!/usr/bin/env python3
"""Experiment 4 -- objectification and elevation.

Contract: research/process-representation-gap/contracts/exp4-objectification-elevation.v1.json

The work plan asks whether equality of ONE evaluation is enough to form a stable
object, and whether a stable object is enough to form a higher-order computation.
Both halves are answered on exact declared models: the pinned addition ->
multiplication rank transition of ``mountain/process-geometry`` at commit
``c47c96fa79123c677172278be59d67ca1cc891b1`` (baseline control), then one
objectification attempt on the experiment-2 loop model and one on the
experiment-5 braid model.

Nothing here is a new repository API.  In particular no generic ``rank``,
``Objectification``, ``ProcessRank`` or ``RankLowering`` abstraction is written:
the pinned note refuses one and work plan section 6 experiment 4 forbids one.
What is implemented is a declared, exact, reproducible calibration.

Conventions, declared before running (contract ``native.composition_convention``):

* a word ``(g_1, ..., g_n)`` is chronological: ``g_1`` acts first, ``g_n`` last
  (this is ``ProcessWord`` order in ``src/process_geometry/process/history.py``);
* the pinned note writes algebraic composites in juxtaposition, where ``XY``
  applies ``Y`` first and ``X`` second, which is why it computes ``D_k T_a`` as
  ``k(x + a)``;
* the pinned essay's own dictionary is used verbatim: the chronological word
  ``(T_a, D_k)`` denotes the algebraic composite ``D_k T_a``, and ``(D_k, T_ka)``
  denotes ``T_ka D_k``;
* the declared pair is ``(b, k)`` meaning ``x -> k*x + b`` with the declared
  product ``(b,k) * (c,l) = (b + k*c, k*l)``, i.e. the right factor acts first.

Consequently ``pair(w ++ (g,)) = pair(g) * pair(w)``: appending in time multiplies
in the reverse algebraic order.  That orientation is an obligation here and its
opposite is a declared negative control.

Run:

    python3 research/process-representation-gap/experiments/exp4_objectification_elevation.py
    python3 -O research/process-representation-gap/experiments/exp4_objectification_elevation.py
"""

from __future__ import annotations

import argparse
import itertools
import sys
import tempfile
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(ROOT / "tools"))
import gapkit  # noqa: E402
from gapkit import qtext, require  # noqa: E402

CONTRACT = ROOT / "contracts" / "exp4-objectification-elevation.v1.json"
FROZEN = ROOT / "contracts" / "FROZEN.sha256"
EVIDENCE = ROOT / "evidence" / "exp4-objectification-elevation.json"

SCHEMA = "aeg.process-representation-gap.exp4.v1"

# --------------------------------------------------------------------------
# declared bounds (contract domain.length_budget)
# --------------------------------------------------------------------------

BASE_ALPHABET = (("T", -2), ("T", 1), ("T", 3), ("D", 2), ("D", 3))
ESSAY_ALPHABET = (("T", -2), ("T", 1), ("D", 2), ("D", 3))
TRANSLATION_ONLY = (("T", -2), ("T", 1))
PURE_DILATION = (("D", 2), ("D", 3))
TRANSLATION_SUBGROUP = tuple((a, 1) for a in range(-40, 41))

DECLARED_STATES = (-3, -1, 0, 2, 5)
INITIAL_STATE = 0
BASE_LENGTH = 5
SPLIT_LENGTH = 4
ASSOCIATIVITY_DEPTH = 2
RELATION_A = tuple(range(-6, 7))
RELATION_K = tuple(range(1, 7))
REPETITION_A = tuple(range(-6, 7))
REPETITION_N = tuple(range(1, 7))

EXP2_ALPHABET = ("c", "v", "l")
EXP2_ALL_LENGTH = 5
EXP2_LEGAL_LENGTH = 6
EXP2_BFS_DEPTH = 2
EXP2_STATES = (
    Fraction(0), Fraction(1), Fraction(-1), Fraction(2), Fraction(3),
    Fraction(1, 2), Fraction(3, 2), Fraction(7, 2), Fraction(5), Fraction(12, 5),
)
# experiment-2 generator action on the accumulator carrier: x -> k*x + b
EXP2_LETTER_PAIR = {
    "c": (Fraction(1), Fraction(2)),
    "v": (Fraction(0), Fraction(1, 2)),
    "l": (Fraction(1), Fraction(1)),
}
# frozen literal tables (contract independent_check.hand_literal_tables)
EXP2_PAIR_HAND = {
    "": ("0", "1"),
    "c": ("1", "2"),
    "cc": ("3", "4"),
    "ccvcv": ("2", "2"),
    "cv": ("1/2", "1"),
    "cvc": ("2", "2"),
    "l": ("1", "1"),
    "v": ("0", "1/2"),
    "vc": ("1", "1"),
    "vv": ("0", "1/4"),
}
# the nine accumulator literals published by the frozen experiment-2 contract
EXP2_FROZEN_ACCUMULATOR = {
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
BASE_PAIR_HAND = (
    ("(D_1,T_-4)", (("D", 1), ("T", -4)), (-4, 1)),
    ("(D_2,D_3)", (("D", 2), ("D", 3)), (0, 6)),
    ("(D_2,T_1)", (("D", 2), ("T", 1)), (1, 2)),
    ("(D_3,T_2,D_2)", (("D", 3), ("T", 2), ("D", 2)), (4, 6)),
    ("(D_3,T_6)", (("D", 3), ("T", 6)), (6, 3)),
    ("(T_-2,T_1)", (("T", -2), ("T", 1)), (-1, 1)),
    ("(T_0,D_5)", (("T", 0), ("D", 5)), (0, 5)),
    ("(T_1,D_2)", (("T", 1), ("D", 2)), (2, 2)),
    ("(T_2,D_3)", (("T", 2), ("D", 3)), (6, 3)),
    ("(T_2,T_2,T_2)", (("T", 2), ("T", 2), ("T", 2)), (6, 1)),
    ("(T_3,D_2)", (("T", 3), ("D", 2)), (6, 2)),
    ("(T_3,T_3)", (("T", 3), ("T", 3)), (6, 1)),
)

EXP5_LETTERS = (1, 2, -1, -2)
EXP5_LENGTH = 6
EXP5_SPLIT_LENGTH = 4
EXP5_BFS_DEPTH = 3
STRANDS = 3
IDENTITY_AUT = ((1,), (2,), (3,))
EXP5_PROBES = {
    "x1": (1,),
    "x2": (2,),
    "x3": (3,),
    "x1x2": (1, 2),
    "x1x2x3": (1, 2, 3),
    "x1x2x1^-1": (1, 2, -1),
    "commutator": (1, 2, 3, -1, -2, -3),
    "(x1x2)^3": (1, 2, 1, 2, 1, 2),
}
EXP5_PROBE_ORDER = tuple(EXP5_PROBES)
EXP5_PAIR_HAND = (
    ("()", (), ["x", "y", "z"]),
    ("(s1)", (1,), ["xyx^-1", "x", "z"]),
    ("(s1,s1)", (1, 1), ["xyxy^-1x^-1", "xyx^-1", "z"]),
    ("(s1,s2)", (1, 2), ["xyzy^-1x^-1", "x", "y"]),
    ("(s1,s2,s1)", (1, 2, 1), ["xyzy^-1x^-1", "xyx^-1", "x"]),
    ("(s2)", (2,), ["x", "yzy^-1", "y"]),
    ("(s2,s1)", (2, 1), ["xyx^-1", "xzx^-1", "x"]),
    ("(s2,s1,s2)", (2, 1, 2), ["xyzy^-1x^-1", "xyx^-1", "x"]),
)

# provenance: recorded sha256 of the pinned files this experiment relies on,
# computed over the pinned checkout mountain/process-geometry at the pinned commit.
SOURCE_BASELINE = {
    "commit": "c47c96fa79123c677172278be59d67ca1cc891b1",
    "repository": "mountain/process-geometry",
    "files": {
        "docs/51-aeg-addition-multiplication-rank-transition.md":
            "f50600f58ff5a9236baf6d62bedc8785d10bc7938db3275898d98597d6a4f8f2",
        "docs/44-objectification-semantic-compression-and-rank-lowering.md":
            "02b8c82793308926de28fe3aef1593d9a861d07be82b8da80f28dfa49e2afaf4",
        "docs/50-aeg-translation-objectification-rank-lowering.md":
            "ab1a46d8da91a55bb8c91acbc7ca6eb383e51589ddb64b4143e5b35282a5ab36",
        "tests/research/test_aeg_addition_multiplication_rank_transition.py":
            "7682104046ca0a237950459b11a0896ac7dee0cbee1dfe79742cdf90305f3843",
        "src/process_geometry/process/history.py":
            "93e9dc4651f4cf70e2a0980c9fee8ea58cc15acbe89bc064861c37359652cc45",
    },
    "quoted_dictionary": ("ProcessWord stores chronological order.  Therefore (T_a, D_k) means "
                          "the algebraic composite D_k T_a, while (D_k, T_ka) means T_ka D_k."),
    "note": ("the hashes were computed over the pinned checkout, which lives outside this worktree; "
             "the reproduction commands of this experiment do not re-read that checkout"),
}

BOUNDED_SWEEP_DISCLAIMER = (
    "A finite word-length test never substitutes for a general consistency proof over all "
    "composite words. Where a general argument exists it is stated with an explicit status and "
    "the sweep is labelled as its calibration; where only a sweep is available the status is "
    "bounded-domain-compatible."
)


# --------------------------------------------------------------------------
# declared exact model: pair algebra (object layer of the baseline control)
# --------------------------------------------------------------------------

def is_int(value) -> bool:
    return isinstance(value, int) and not isinstance(value, bool)


def is_valid_dilation(k) -> bool:
    return is_int(k) and k >= 1


def translation_pair(a):
    require(is_int(a), "EXP4-TRANSLATION-DOMAIN",
            f"translation parameter {a!r} is not an integer")
    return (a, 1)


def dilation_pair(k):
    require(is_valid_dilation(k), "EXP4-DILATION-DOMAIN",
            f"dilation parameter {k!r} is outside N_>0; the pinned construction admits positive "
            "integers only and excludes D_0, D_-1 and D_1/2")
    return (0, k)


def generator_pair(g):
    kind, value = g
    require(kind in ("T", "D"), "EXP4-UNKNOWN-GENERATOR", f"unknown generator {g!r}")
    return translation_pair(value) if kind == "T" else dilation_pair(value)


def star(P, Q):
    """Declared product (b,k)*(c,l) = (b + k*c, k*l): the RIGHT factor acts first."""
    b, k = P
    c, l = Q
    require(is_valid_dilation(k) and is_valid_dilation(l), "EXP4-DILATION-DOMAIN",
            f"pair scales {k!r},{l!r} are not positive integers")
    return (b + k * c, k * l)


IDENTITY_PAIR = (0, 1)


def pair_of(word):
    """Chronological fold: applying P and then g multiplies on the left by pair(g)."""
    P = IDENTITY_PAIR
    for g in word:
        P = star(generator_pair(g), P)
    return P


def lower(P, x):
    """Lowering of the object layer to the bottom layer: the state map x -> k*x+b."""
    b, k = P
    return k * x + b


def execute(word, x):
    """Bottom-layer step-by-step execution with the declared generator domains."""
    for g in word:
        kind, value = g
        if kind == "T":
            require(is_int(value), "EXP4-TRANSLATION-DOMAIN",
                    f"translation parameter {value!r} is not an integer")
            x = x + value
        else:
            require(kind == "D", "EXP4-UNKNOWN-GENERATOR", f"unknown generator {g!r}")
            require(is_valid_dilation(value), "EXP4-DILATION-DOMAIN",
                    f"dilation parameter {value!r} is outside N_>0")
            x = value * x
    return x


def naive_fold(word):
    """The declared WRONG lowering: D_k is lowered to the translation T_k."""
    P = IDENTITY_PAIR
    for _, value in word:
        P = star((value, 1), P)
    return P


def word_text(word) -> str:
    if not word:
        return "epsilon"
    return " ".join(f"{kind}_{value}" for kind, value in word)


def exp2_word_text(word) -> str:
    return "".join(word) if word else "epsilon"


def per_length(word_list) -> dict:
    out: dict = {}
    for w in word_list:
        out[len(w)] = out.get(len(w), 0) + 1
    return out


def enumerated_domain(alphabet, max_length):
    return [tuple(w) for w in gapkit.words(alphabet, max_length)]


def reachable_objects(alphabet, depth):
    """Breadth-first enumeration of the object layer, deduplicated."""
    seen = {IDENTITY_PAIR}
    frontier = [IDENTITY_PAIR]
    cumulative = {0: 1}
    for level in range(1, depth + 1):
        nxt = []
        for P in frontier:
            for g in alphabet:
                Q = star(generator_pair(g), P)
                if Q not in seen:
                    seen.add(Q)
                    nxt.append(Q)
        frontier = nxt
        cumulative[level] = len(seen)
    return seen, cumulative


# --------------------------------------------------------------------------
# baseline control: relations, composition, repetition versus uniform action
# --------------------------------------------------------------------------

def check_injectivity(objects):
    """The pair is determined by its values at 0 and 1 (exact case analysis)."""
    ordered = sorted(objects)
    for P, Q in itertools.combinations(ordered, 2):
        if lower(P, 0) == lower(Q, 0) and lower(P, 1) == lower(Q, 1):
            require(False, "EXP4-INJECTIVITY",
                    f"pairs {P} and {Q} agree at 0 and 1 but are not equal")
    return {
        "statement": ("if b != b' the values at 0 differ; if b = b' and k != k' the values at 1 "
                      "differ; hence equality of pairs is equality of maps on the whole of Z"),
        "status": "proved",
        "objects_checked": len(ordered),
        "states_used": [0, 1],
    }


def check_relations():
    translation_checks = 0
    for a in RELATION_A:
        for b in RELATION_A:
            left = pair_of((("T", a), ("T", b)))
            right = translation_pair(a + b)
            require(left == right, "EXP4-TRANSLATION-LAW",
                    f"T_a T_b = {left}, T_(a+b) = {right}")
            for x in DECLARED_STATES:
                require(lower(left, x) == lower(right, x), "EXP4-TRANSLATION-LAW",
                        f"T_a T_b and T_(a+b) disagree at x = {x}")
            translation_checks += 1

    dilation_checks = 0
    for k in RELATION_K:
        for l in RELATION_K:
            left = pair_of((("D", k), ("D", l)))
            right = dilation_pair(k * l)
            require(left == right, "EXP4-DILATION-LAW",
                    f"D_k D_l = {left}, D_(k*l) = {right}")
            dilation_checks += 1

    cross_checks = 0
    for a in RELATION_A:
        for k in RELATION_K:
            # algebraic composite D_k T_a  ==  chronological word (T_a, D_k)
            left = pair_of((("T", a), ("D", k)))
            # algebraic composite T_(ka) D_k  ==  chronological word (D_k, T_ka)
            right = pair_of((("D", k), ("T", k * a)))
            require(left == right, "EXP4-CROSS-RELATION",
                    f"D_{k} T_{a} = {left} but T_{k * a} D_{k} = {right}")
            require(left == (k * a, k), "EXP4-CROSS-RELATION",
                    f"the cross composite at a={a}, k={k} is {left}, expected {(k * a, k)}")
            for x in DECLARED_STATES:
                require(lower(left, x) == lower(right, x), "EXP4-CROSS-RELATION",
                        f"D_k T_a and T_(ka) D_k disagree at x = {x}")
            cross_checks += 1

    return {
        "translation_law": {
            "identity": "T_a T_b = T_(a+b)",
            "sweep": {"a": [min(RELATION_A), max(RELATION_A)],
                      "b": [min(RELATION_A), max(RELATION_A)], "checks": translation_checks},
            "general_argument": ("star((a,1),(b,1)) = (a+b,1) = pair(T_(a+b)) exactly, for every "
                                 "a,b in Z; the sweep calibrates that line"),
            "status": "proved",
        },
        "dilation_law": {
            "identity": "D_k D_l = D_(k*l)",
            "sweep": {"k": [min(RELATION_K), max(RELATION_K)],
                      "l": [min(RELATION_K), max(RELATION_K)], "checks": dilation_checks},
            "general_argument": "star((0,k),(0,l)) = (0,k*l) = pair(D_(k*l)) exactly, for every k,l in N_>0",
            "status": "proved",
        },
        "cross_relation": {
            "identity": "D_k T_a = T_(k*a) D_k",
            "declared_convention_form": ("chronological word (T_a, D_k) denotes the algebraic composite "
                                         "D_k T_a; chronological word (D_k, T_ka) denotes T_ka D_k"),
            "sweep": {"a": [min(RELATION_A), max(RELATION_A)],
                      "k": [min(RELATION_K), max(RELATION_K)], "checks": cross_checks},
            "both_sides_pair": "(k*a, k)",
            "general_argument": ("star((0,k),(a,1)) = (k*a, k) and star((k*a,1),(0,k)) = (k*a, k) exactly, "
                                 "for every a in Z and every k in N_>0; both sides lower to "
                                 "x -> k*(x+a) = k*x + k*a"),
            "status": "proved",
        },
    }


def check_composition(domain, objects):
    induction_checks = 0
    for w in domain:
        P = pair_of(w)
        for g in BASE_ALPHABET:
            require(pair_of(w + (g,)) == star(generator_pair(g), P), "EXP4-COMPOSITION-LAW",
                    f"the induction step fails at {word_text(w)} and generator {g}")
            induction_checks += 1

    split_checks = 0
    for w in domain:
        if len(w) > SPLIT_LENGTH:
            continue
        for cut in range(len(w) + 1):
            w1, w2 = w[:cut], w[cut:]
            require(pair_of(w1 + w2) == star(pair_of(w2), pair_of(w1)), "EXP4-COMPOSITION-LAW",
                    f"the anti-homomorphism law fails at {word_text(w1)} ++ {word_text(w2)}")
            split_checks += 1

    map_checks = 0
    ordered = sorted(objects)
    for P, Q in itertools.product(ordered, ordered):
        for x in DECLARED_STATES:
            require(lower(star(P, Q), x) == lower(P, lower(Q, x)), "EXP4-COMPOSITION-LAW",
                    f"star is not composition of the lowered maps at {P}, {Q}, x = {x}")
            map_checks += 1

    assoc_checks = 0
    for P, Q, R in itertools.product(ordered, ordered, ordered):
        require(star(star(P, Q), R) == star(P, star(Q, R)), "EXP4-ASSOCIATIVITY",
                f"star is not associative at {P}, {Q}, {R}")
        assoc_checks += 1
    for P in ordered:
        require(star(IDENTITY_PAIR, P) == P and star(P, IDENTITY_PAIR) == P, "EXP4-IDENTITY",
                f"the two-sided identity fails at {P}")

    wrong_w1, wrong_w2 = (("D", 2), ("T", 1)), (("T", 3),)
    wrong_order_value = star(pair_of(wrong_w1), pair_of(wrong_w2))
    right_order_value = pair_of(wrong_w1 + wrong_w2)
    require(wrong_order_value != right_order_value, "EXP4-COMPOSITION-ORDER",
            "the chronological multiplication order unexpectedly agrees on the declared probe")

    return {
        "product": "(b,k) * (c,l) = (b + k*c, k*l)",
        "induction_step": {
            "identity": "pair(w ++ (g,)) = pair(g) * pair(w)",
            "checks": induction_checks,
            "status": "proved",
            "general_argument": ("pair_of is the left fold of star over the reversed generator sequence; "
                                 "star is total on Z x N_>0 by integer closure of (b,k)*(c,l) = (b+k*c, k*l), "
                                 "and the step itself is the definition of the fold"),
        },
        "anti_homomorphism": {
            "identity": "pair(w1 ++ w2) = pair(w2) * pair(w1)",
            "checks": split_checks,
            "splits_up_to_length": SPLIT_LENGTH,
            "status": "proved",
            "general_argument": ("induction on |w2| using the induction step and associativity of star, "
                                 "which is inherited from associativity of function composition through "
                                 "the pair-versus-map lemma"),
        },
        "star_is_map_composition": {
            "identity": "lower(star(P,Q), x) = lower(P, lower(Q, x))",
            "checks": map_checks,
            "status": "proved",
            "general_argument": "lower(star(P,Q), x) = k*(l*x+c)+b = lower(P, lower(Q, x))",
        },
        "associativity": {
            "checks": assoc_checks,
            "objects": len(objects),
            "depth": ASSOCIATIVITY_DEPTH,
            "status": "proved",
            "general_argument": ("star is composition of maps (previous item) and composition of maps "
                                 "is associative"),
        },
        "two_sided_identity": {"object": list(IDENTITY_PAIR), "status": "proved"},
        "orientation_trap": {
            "witness_words": [word_text(wrong_w1), word_text(wrong_w2)],
            "chronological_product": list(wrong_order_value),
            "declared_product": list(right_order_value),
            "status": "proved",
        },
    }


def repetition_vs_uniform():
    fibres = {}
    for a in REPETITION_A:
        for n in REPETITION_N:
            fibres.setdefault((n * a, 1), []).append((a, n))
    schemas = len(REPETITION_A) * len(REPETITION_N)
    largest = sorted(fibres.items(), key=lambda kv: (-len(kv[1]), kv[0]))[0]
    pinned = sorted(fibres[(6, 1)])
    require(len(pinned) >= 2, "EXP4-FIBRE-SCHEMA",
            "the pinned example T_2^3 = T_6 = T_3^2 does not reproduce: the fibre is a singleton")
    require(pinned == [(1, 6), (2, 3), (3, 2), (6, 1)], "EXP4-FIBRE-SCHEMA",
            f"the fibre of the output T_6 is {pinned}")

    def act_family(k, P):
        b, scale = P
        return (k * b, scale)

    endo_checks = 0
    for k in RELATION_K:
        for a in RELATION_A:
            for b in RELATION_A:
                left = act_family(k, star(translation_pair(a), translation_pair(b)))
                right = star(act_family(k, translation_pair(a)), act_family(k, translation_pair(b)))
                require(left == right, "EXP4-UNIFORM-ACTION",
                        f"R_{k} is not an endomorphism of the translation family at a={a}, b={b}")
                endo_checks += 1

    actions = {k: tuple(act_family(k, translation_pair(a)) for a in REPETITION_A) for k in RELATION_K}
    require(len(set(actions.values())) == len(RELATION_K), "EXP4-UNIFORM-ACTION",
            "two distinct dilation factors induce the same action on the declared translation family")
    index_one = REPETITION_A.index(1)
    require(actions[2][index_one] != actions[3][index_one], "EXP4-UNIFORM-ACTION",
            "R_2 and R_3 agree at T_1; the pinned distinction is not reproduced")
    for k in RELATION_K:
        require(generator_pair(("D", k)) == (0, k), "EXP4-UNIFORM-ACTION",
                f"the object of R_{k} is not D_{k}")
        require(act_family(k, translation_pair(1)) == translation_pair(k), "EXP4-UNIFORM-ACTION",
                f"R_{k}(T_1) is not T_{k}")

    triple = pair_of((("T", 2), ("T", 2), ("T", 2)))
    require(triple == pair_of((("T", 3), ("T", 3))), "EXP4-FIBRE-SCHEMA",
            "T_2^3 and T_3^2 do not share their endpoint")
    return {
        "repeated_execution": {
            "definition": "(T_a)^n = T_(n*a): the fold of one fixed translation",
            "schemas_enumerated": schemas,
            "distinct_outputs": len(fibres),
            "counts_status": "bounded-domain-compatible",
            "largest_fibre": {"output": list(largest[0]), "size": len(largest[1]),
                              "schemas": [list(s) for s in largest[1]]},
            "pinned_example": {"output": [6, 1], "schemas": [list(s) for s in pinned],
                               "words": ["T_2 T_2 T_2", "T_3 T_3"]},
            "finding": ("the endpoint does not determine the schema: the fibre of T_6 under repeated "
                        "execution contains the four schemas (1,6), (2,3), (3,2), (6,1)"),
            "status": "proved",
        },
        "uniform_action": {
            "definition": "R_k(T_a) = T_(k*a) for every a in the declared translation family",
            "endomorphism_checks": endo_checks,
            "distinct_actions_over_k": len(set(actions.values())),
            "distinguishing_probe": {"family": "T_1", "R_2": list(translation_pair(2)),
                                    "R_3": list(translation_pair(3))},
            "object_of_R_k": ["(0,k)", "k in N_>0"],
            "finding": ("the uniform action is a well-defined object determined by its action on the "
                        "family, while the single output is not"),
            "status": "proved",
        },
        "naming_trap": {
            "named_object": list(triple),
            "equal_to_lower_object": list(translation_pair(6)),
            "in_lower_translation_layer": triple in TRANSLATION_SUBGROUP,
            "finding": ("the named composite T_2^3 is the lower-layer translation T_6, so it fails "
                        "elevation criterion E1; renaming a power of one T_a is not elevation"),
            "status": "proved",
        },
    }


def _minimal_summary_collision(groups, min_length):
    """Minimal pair of words with the same declared evaluation but different objects."""
    best = None
    for value, ws in sorted(groups.items()):
        eligible = [w for w in ws if len(w) >= min_length]
        if len(eligible) < 2:
            continue
        by_object = {}
        for w in sorted(eligible, key=lambda w: (len(w), w)):
            by_object.setdefault(pair_of(w), w)
        for (P, w1), (Q, w2) in itertools.combinations(sorted(by_object.items()), 2):
            candidate = (len(w1) + len(w2), word_text(w1), word_text(w2))
            if best is None or candidate < best[0]:
                best = (candidate, P, Q, w1, w2)
    return best


def _summary_witness(best):
    _, P, Q, w1, w2 = best
    return {
        "words": [word_text(w1), word_text(w2)],
        "objects": [list(P), list(Q)],
        "endpoint_values": [lower(P, INITIAL_STATE), lower(Q, INITIAL_STATE)],
        "states": list(DECLARED_STATES),
        "values_at_declared_states": [[lower(P, x) for x in DECLARED_STATES],
                                      [lower(Q, x) for x in DECLARED_STATES]],
        "total_length": len(w1) + len(w2),
    }


def gate_i_base(domain):
    groups = {}
    for w in domain:
        groups.setdefault(lower(pair_of(w), INITIAL_STATE), []).append(w)
    colliding = 0
    largest = 0
    for value, ws in sorted(groups.items()):
        if len(ws) < 2:
            continue
        colliding += 1
        largest = max(largest, len(ws))
    overall = _minimal_summary_collision(groups, 0)
    nonempty = _minimal_summary_collision(groups, 1)
    require(overall is not None and nonempty is not None, "EXP4-SUMMARY-INSUFFICIENT",
            "the single declared evaluation unexpectedly separated every pair of objects")
    require(overall[0][0] == 1, "EXP4-SUMMARY-INSUFFICIENT",
            f"the minimal witness has total length {overall[0][0]}, expected 1 "
            "(the empty word against D_2)")
    require(overall[0][1:] == ("epsilon", "D_2"), "EXP4-SUMMARY-INSUFFICIENT",
            f"the minimal witness is {overall[0][1:]}, expected ('epsilon', 'D_2')")
    require(nonempty[0][0] == 2 and nonempty[0][1:] == ("D_2", "D_3"), "EXP4-SUMMARY-INSUFFICIENT",
            f"the minimal non-empty witness is {nonempty[0][1:]}, expected ('D_2', 'D_3')")
    return {
        "summary": "pi_out(w) = the endpoint value at the single declared initial state x_0 = 0",
        "classes_on_domain": len(groups),
        "colliding_fibres": colliding,
        "largest_fibre": largest,
        "counts_status": "bounded-domain-compatible",
        "minimal_witness": _summary_witness(overall),
        "minimal_witness_both_nonempty": _summary_witness(nonempty),
        "verdict": "FAIL",
        "status": "proved",
        "general_argument": ("evaluating an object at 0 gives b and at 1 gives k+b, so no two distinct "
                             "objects agree at both states; the witness below is minimal in the declared "
                             "sweep, and one counterexample proves the failure for the declared task"),
        "bounded_note": ("the colliding-fibre counts are the counts inside the declared sweep; the "
                         "minimal witness itself is a general counterexample"),
    }


def gate_ii_base(domain, objects):
    successors = {}
    check_count = 0
    for w in domain:
        P = pair_of(w)
        for g in BASE_ALPHABET:
            successors.setdefault((P, g), set()).add(pair_of(w + (g,)))
            check_count += 1
    for (P, g), images in sorted(successors.items()):
        require(len(images) == 1, "EXP4-CLOSED-UPDATE",
                f"object {P} has different successors under generator {g}: {sorted(images)}")
    for P in sorted(objects):
        require(is_valid_dilation(P[1]) and is_int(P[0]), "EXP4-GATE-II-INTERFACE",
                f"the carrier is not closed at {P}")
    return {
        "carrier": "Z x N_>0, closed under * by integer closure of b + k*c and k*l",
        "totality": "star is defined on every pair of declared objects and on every declared generator",
        "closed_update": {
            "checks": check_count,
            "statement": ("equal objects have equal successor objects for every declared generator: the "
                          "declared update Uhat_g(P) = pair(g) * P is a function of the object alone"),
        },
        "verdict": "PASS",
        "status": "proved",
    }


def gate_iii_base(domain):
    checks = 0
    failures = []
    for w in domain:
        P = pair_of(w)
        for x in DECLARED_STATES:
            checks += 1
            if lower(P, x) != execute(w, x):
                failures.append({"word": word_text(w), "state": x, "object_layer": lower(P, x),
                                 "bottom_layer": execute(w, x)})
    require(not failures, "EXP4-DESCENT-DISAGREEMENT",
            f"the descent test failed on {len(failures)} of {checks} checks: {failures[:3]}")
    return {
        "test": ("compose at the object layer (chronological fold of star), then lower, against "
                 "step-by-step execution at the bottom layer"),
        "words": len(domain),
        "states": list(DECLARED_STATES),
        "checks": checks,
        "mismatches": 0,
        "verdict": "PASS",
        "status": "proved",
        "general_argument": ("star is composition of the lowered maps and the carrier is closed under "
                             "star, so by induction on word length the fold of any word lowers to the "
                             "composite of the generators' state maps, for every word over the alphabet "
                             "and every integer state; the sweep calibrates that induction"),
        "bounded_scope": (f"the sweep covers all words of length <= {BASE_LENGTH} over "
                          f"{len(BASE_ALPHABET)} generators and all {len(DECLARED_STATES)} declared states"),
    }


def elevation_base():
    dilation_object = generator_pair(("D", 2))
    require(dilation_object not in TRANSLATION_SUBGROUP, "EXP4-ELEVATION-E1",
            "D_2 turned out to lie in the lower translation layer")
    uniform_values = [lower(generator_pair(("D", 2)), a) for a in (0, 1)]
    require(uniform_values[0] != uniform_values[1], "EXP4-ELEVATION-E3",
            "the novel generator's action is constant on the declared parameter probe")
    composite = star(generator_pair(("D", 2)), generator_pair(("D", 3)))
    single_generators = {generator_pair(g) for g in BASE_ALPHABET}
    require(composite not in single_generators, "EXP4-ELEVATION-E4",
            "D_2 * D_3 coincides with a single declared generator")
    named = pair_of((("T", 2), ("T", 2), ("T", 2)))
    require(named in TRANSLATION_SUBGROUP, "EXP4-NAMING-NOT-ELEVATION",
            "the named composite T_2^3 is not a lower-layer translation")
    return {
        "criterion": ["E1 generator novelty", "E2 strict inclusion", "E3 uniformity",
                      "E4 generative novelty", "E5 not by naming/caching/history"],
        "E1": {"witness": "pair(D_2) = (0,2) is not (b,1) for any integer b",
               "argument": ("if (0,2) = (b,1) then the first coordinate gives b = 0 and the second "
                            "gives 2 = 1: contradiction"),
               "verdict": "HOLDS"},
        "E2": {"witness": "D_2", "lower_image": "Z x {1}", "verdict": "HOLDS",
               "note": "the higher image strictly contains the lower image"},
        "E3": {"witness": {"a": [0, 1], "R_2(T_a)": uniform_values},
               "contrast": ("the single output T_6 has four candidate schemas in the "
                            "repeated-execution fibre"),
               "verdict": "HOLDS"},
        "E4": {"witness": "D_2 * D_3 = (0,6), not among the declared generator objects",
               "verdict": "HOLDS"},
        "E5": {"named_object": list(named), "verdict": "HOLDS",
               "note": "the named power fails E1, so naming cannot satisfy the criterion"},
        "verdict": "ELEVATION",
        "status": "proved",
    }


# --------------------------------------------------------------------------
# attempt 1: objectify the experiment-2 accumulator structure
# --------------------------------------------------------------------------

def exp2_counts(word) -> tuple:
    return (word.count("c"), word.count("v"), word.count("l"))


def exp2_legal(word) -> tuple:
    nc, nv, _ = exp2_counts(word)
    out = ["c"]
    if nc > nv:
        out.append("v")
    if nv >= 1:
        out.append("l")
    return tuple(out)


def exp2_step(word, sigma):
    require(sigma in exp2_legal(word), "EXP4-ILLEGAL-ACTION",
            f"mechanism {sigma!r} is not legal at word {exp2_word_text(word)!r}")
    return word + (sigma,)


def exp2_accum(word) -> Fraction:
    value = Fraction(0)
    for sigma in word:
        value = exp2_accum_step(value, sigma)
    return value


def exp2_accum_step(value, sigma):
    if sigma == "c":
        return 2 * value + 1
    if sigma == "v":
        return value / 2
    require(sigma == "l", "EXP4-ILLEGAL-ACTION", f"unknown mechanism {sigma!r}")
    return value + 1


def exp2_readout(word) -> tuple:
    if not word:
        return ("EMPTY", "EMPTY", "EMPTY")
    nc, nv, _ = exp2_counts(word)
    frames = len(word)
    handoffs = frames - 1
    return (qtext(Fraction(nc + nv)), qtext(Fraction(frames - handoffs)),
            qtext(Fraction(3 * handoffs, frames)))


def star_q(P, Q):
    b, k = P
    c, l = Q
    return (b + k * c, k * l)


def exp2_pair_of(word):
    P = (Fraction(0), Fraction(1))
    for sigma in word:
        P = star_q(EXP2_LETTER_PAIR[sigma], P)
    return P


def exp2_legal_domain(max_length=EXP2_LEGAL_LENGTH):
    out = [()]
    frontier = [()]
    while frontier:
        nxt = []
        for word in frontier:
            if len(word) >= max_length:
                continue
            for sigma in exp2_legal(word):
                child = word + (sigma,)
                nxt.append(child)
                out.append(child)
        frontier = nxt
    return out


def exp2_reachable(alphabet=EXP2_ALPHABET, depth=EXP2_BFS_DEPTH):
    identity = (Fraction(0), Fraction(1))
    seen = {identity}
    frontier = [identity]
    for _ in range(depth):
        nxt = []
        for P in frontier:
            for sigma in alphabet:
                Q = star_q(EXP2_LETTER_PAIR[sigma], P)
                if Q not in seen:
                    seen.add(Q)
                    nxt.append(Q)
        frontier = nxt
    return seen


def is_dyadic(value) -> bool:
    denominator = Fraction(value).denominator
    return denominator & (denominator - 1) == 0


def is_power_of_two_scale(value) -> bool:
    """k is in 2^Z, i.e. exactly a (possibly negative) power of two."""
    value = Fraction(value)
    if value <= 0:
        return False
    numerator, denominator = value.numerator, value.denominator
    return (numerator & (numerator - 1)) == 0 and (denominator & (denominator - 1)) == 0


def attempt_exp2(all_words, legal_words):
    counts = per_length(legal_words)
    expected = {0: 1, 1: 1, 2: 2, 3: 4, 4: 10, 5: 26, 6: 71}
    require(counts == expected, "EXP4-EXP2-DOMAIN-MISMATCH",
            f"the experiment-2 legal domain is {counts}, expected {expected}")
    require(per_length(all_words) == {0: 1, 1: 3, 2: 9, 3: 27, 4: 81, 5: 243},
            "EXP4-EXP2-DOMAIN-MISMATCH",
            "the unrestricted word domain does not match the declaration")

    for word, expected_value in sorted(EXP2_FROZEN_ACCUMULATOR.items()):
        observed = qtext(exp2_accum(tuple(word)))
        require(observed == expected_value, "EXP4-HAND-TABLE-MISMATCH",
                f"A({word!r}) = {observed}, the frozen experiment-2 table says {expected_value}")
    for word, pair in sorted(EXP2_PAIR_HAND.items()):
        P = exp2_pair_of(tuple(word))
        observed = (qtext(P[0]), qtext(P[1]))
        require(observed == pair, "EXP4-HAND-TABLE-MISMATCH",
                f"the affine object of {word!r} is {observed}, the frozen table says {pair}")

    accumulator_checks = 0
    for word in list(all_words) + list(legal_words):
        require(exp2_pair_of(word)[0] == exp2_accum(word), "EXP4-EXP2-ACCUMULATOR-ACTION",
                f"A({exp2_word_text(word)}) does not equal the object action at 0")
        accumulator_checks += 1

    legal_groups = {}
    for word in legal_words:
        legal_groups.setdefault(exp2_pair_of(word), []).append(word)
    colliding = 0
    largest = 0
    best = None
    for key, words in sorted(legal_groups.items(), key=lambda kv: (str(kv[0][0]), str(kv[0][1]))):
        if len(words) < 2:
            continue
        colliding += 1
        largest = max(largest, len(words))
        for w1, w2 in itertools.combinations(sorted(words, key=lambda w: (len(w), w)), 2):
            if exp2_readout(w1) == exp2_readout(w2) and exp2_legal(w1) == exp2_legal(w2):
                continue
            candidate = (len(w1) + len(w2), exp2_word_text(w1), exp2_word_text(w2))
            if best is None or candidate < best[0]:
                best = (candidate, w1, w2)
    require(best is not None, "EXP4-EXP2-SUFFICIENCY-CLAIM",
            "no collision inside the declared experiment-2 legal domain separated by the readout")
    _, w1, w2 = best
    require(len(w1) + len(w2) == 8, "EXP4-EXP2-SUFFICIENCY-CLAIM",
            f"the minimal in-domain witness has total length {len(w1) + len(w2)}, expected 8")

    largest_class = None
    for key, words in sorted(legal_groups.items(), key=lambda kv: (-len(kv[1]), str(kv[0]))):
        largest_class = (key, sorted(words, key=lambda w: (len(w), w)))
        break
    fused_left, fused_right = ("c", "v", "c"), ("c", "c", "v", "c", "v")
    require(exp2_pair_of(fused_left) == exp2_pair_of(fused_right) == (Fraction(2), Fraction(2)),
            "EXP4-EXP2-SUFFICIENCY-CLAIM",
            "cvc and ccvcv do not share the accumulator object (2,2)")
    require(exp2_readout(fused_left) != exp2_readout(fused_right), "EXP4-EXP2-SUFFICIENCY-CLAIM",
            "the declared readout does not separate cvc from ccvcv")
    require(exp2_accum(fused_left) == exp2_accum(fused_right) == 2, "EXP4-EXP2-SUFFICIENCY-CLAIM",
            "the accumulator does not agree on cvc and ccvcv")
    require(fused_left in legal_words and fused_right in legal_words, "EXP4-EXP2-SUFFICIENCY-CLAIM",
            "the named witness is not inside the declared experiment-2 legal domain")

    vc, l_word = ("v", "c"), ("l",)
    require(exp2_pair_of(vc) == exp2_pair_of(l_word), "EXP4-EXP2-SUFFICIENCY-CLAIM",
            "vc and l do not share the accumulator object")
    require(exp2_legal(vc) != exp2_legal(l_word), "EXP4-EXP2-SUFFICIENCY-CLAIM",
            "the legal-action signature does not separate vc from l")

    require(all(is_dyadic(exp2_pair_of(w)[0]) and is_power_of_two_scale(exp2_pair_of(w)[1])
                for w in all_words), "EXP4-GATE-II-INTERFACE",
            "the declared carrier is not closed under the experiment-2 letter actions")
    objects = exp2_reachable()
    for P in sorted(objects):
        require(P[1] > 0, "EXP4-GATE-II-INTERFACE", f"nonpositive scale at {P}")
    assoc_checks = 0
    ordered = sorted(objects)
    for P, Q, R in itertools.product(ordered, ordered, ordered):
        require(star_q(star_q(P, Q), R) == star_q(P, star_q(Q, R)), "EXP4-ASSOCIATIVITY",
                f"the experiment-2 object product is not associative at {P}, {Q}, {R}")
        assoc_checks += 1
    successors = {}
    successor_checks = 0
    for word in all_words:
        P = exp2_pair_of(word)
        for sigma in EXP2_ALPHABET:
            successors.setdefault((P, sigma), set()).add(exp2_pair_of(word + (sigma,)))
            successor_checks += 1
    for (P, sigma), images in sorted(successors.items(),
                                     key=lambda kv: (str(kv[0][0][0]), str(kv[0][0][1]), kv[0][1])):
        require(len(images) == 1, "EXP4-CLOSED-UPDATE",
                f"the experiment-2 object {P} has different successors under {sigma}: {sorted(images)}")

    descent_checks = 0
    failures = []
    for word in list(all_words) + list(legal_words):
        P = exp2_pair_of(word)
        for x in EXP2_STATES:
            step = x
            for sigma in word:
                step = exp2_accum_step(step, sigma)
            descent_checks += 1
            if lower(P, x) != step:
                failures.append({"word": exp2_word_text(word), "state": qtext(x),
                                 "object_layer": qtext(lower(P, x)), "bottom_layer": qtext(step)})
        if P[0] != exp2_accum(word):
            failures.append({"word": exp2_word_text(word), "state": "0 (accumulator)",
                             "object_layer": qtext(P[0]), "bottom_layer": qtext(exp2_accum(word))})
    require(not failures, "EXP4-DESCENT-DISAGREEMENT",
            f"the experiment-2 descent test failed: {failures[:3]}")

    c_pair = EXP2_LETTER_PAIR["c"]
    l_pair = EXP2_LETTER_PAIR["l"]
    require(c_pair[1] != 1, "EXP4-ELEVATION-E1", "the letter c is a pure translation")
    require(l_pair[1] == 1, "EXP4-ELEVATION-E1", "the letter l is not a pure translation")
    composite = star_q(EXP2_LETTER_PAIR["c"], EXP2_LETTER_PAIR["c"])
    require(composite not in set(EXP2_LETTER_PAIR.values()), "EXP4-ELEVATION-E4",
            "c * c coincides with a single declared letter object")
    merged = star_q(EXP2_LETTER_PAIR["c"], EXP2_LETTER_PAIR["v"])
    require(merged == EXP2_LETTER_PAIR["l"], "EXP4-ELEVATION-E4",
            "the declared merge c * v = l does not reproduce")
    named_power = star_q(l_pair, l_pair)
    require(named_power[1] == 1, "EXP4-NAMING-NOT-ELEVATION",
            "the named power of the translation letter is not a lower-layer element")

    return {
        "model": ("the declared experiment-2 model: mechanisms c/v/l, the accumulator recurrence, the "
                  "declared legality, and the declared three-scalar readout"),
        "domain": {"all_words": {str(k): v for k, v in sorted(per_length(all_words).items())},
                   "legal_words": {str(k): v for k, v in sorted(counts.items())},
                   "all_words_total": len(all_words), "legal_words_total": len(legal_words),
                   "status": "bounded-domain-compatible"},
        "carrier": "Z[1/2] x 2^Z with the same declared product",
        "letter_objects": {sigma: [qtext(P[0]), qtext(P[1])]
                           for sigma, P in sorted(EXP2_LETTER_PAIR.items())},
        "accumulator_checks": accumulator_checks,
        "gates": {
            "gate_i_task_sufficiency": {
                "verdict": "FAIL",
                "colliding_fibres_legal_domain": colliding,
                "largest_fibre": largest,
                "object_classes_legal_domain": len(legal_groups),
                "minimal_witness": {
                    "words": [exp2_word_text(w1), exp2_word_text(w2)],
                    "objects": [[qtext(exp2_pair_of(w1)[0]), qtext(exp2_pair_of(w1)[1])],
                                [qtext(exp2_pair_of(w2)[0]), qtext(exp2_pair_of(w2)[1])]],
                    "readouts": [list(exp2_readout(w1)), list(exp2_readout(w2))],
                    "legal_signatures": [list(exp2_legal(w1)), list(exp2_legal(w2))],
                    "accumulators": [qtext(exp2_accum(w1)), qtext(exp2_accum(w2))],
                    "total_length": len(w1) + len(w2),
                },
                "largest_fibre_witness": {
                    "object": [qtext(largest_class[0][0]), qtext(largest_class[0][1])],
                    "words": [exp2_word_text(w) for w in largest_class[1]],
                    "readouts": [list(exp2_readout(w)) for w in largest_class[1]],
                    "legal_signatures": [list(exp2_legal(w)) for w in largest_class[1]],
                    "accumulators": [qtext(exp2_accum(w)) for w in largest_class[1]],
                },
                "legality_channel_witness": {
                    "words": [exp2_word_text(vc), exp2_word_text(l_word)],
                    "object": [qtext(exp2_pair_of(vc)[0]), qtext(exp2_pair_of(vc)[1])],
                    "legal_signatures": [list(exp2_legal(vc)), list(exp2_legal(l_word))],
                },
                "localisation": ("the object determines the accumulator exactly (A(w) equals the "
                                 "object's value at 0, checked on every declared word) but retains "
                                 "nothing of the mechanism incidence counts, and the declared "
                                 "experiment-2 observation and legality are functions of those counts"),
                "status": "proved",
            },
            "gate_ii_stable_interface": {
                "verdict": "PASS",
                "associativity_checks": assoc_checks,
                "closed_update_checks": successor_checks,
                "closure": ("b in Z[1/2] and k in 2^Z are closed under the declared product: a dyadic "
                            "times a power of two is dyadic, and products of powers of two are powers "
                            "of two"),
                "status": "proved",
            },
            "gate_iii_exact_descent": {
                "verdict": "PASS",
                "checks": descent_checks,
                "mismatches": 0,
                "test": ("compose at the object layer, then lower, against step-by-step execution of "
                         "the declared accumulator recurrence (at 0) and of the letter maps (at every "
                         "declared state)"),
                "status": "proved",
                "general_argument": ("the letter maps are affine over Q, affine maps are closed under "
                                     "composition, and the fold of the declared product is their "
                                     "composite, so the equality holds for every word over {c,v,l}"),
            },
        },
        "elevation": {
            "verdict": "ELEVATION",
            "E1": {"witness": "the letter object c = (1,2) is not a pure translation", "verdict": "HOLDS"},
            "E2": {"witness": "c lies outside the translation-only lower layer generated by l",
                   "verdict": "HOLDS"},
            "E3": {"witness": {"letter": "c", "values": [qtext(lower(c_pair, 0)), qtext(lower(c_pair, 1))]},
                   "verdict": "HOLDS"},
            "E4": {"witness": ("c * c = (3,4) is not a single declared letter object, so the letter "
                               "grammar generates elements beyond its generators; note separately that "
                               "c * v = (1,1) = l is a genuine merge of the object layer"),
                   "verdict": "HOLDS"},
            "E5": {"witness": "l * l = (2,1) is a lower-layer translation", "verdict": "HOLDS"},
            "status": "proved",
        },
        "finding": ("the accumulator structure does have a genuine, stable, elevated affine object, "
                    "and it still fails objectification gate (i): a stable object is not automatically "
                    "a task-sufficient one"),
    }


# --------------------------------------------------------------------------
# attempt 2: objectify the experiment-5 crossing process onto Aut(F_3)
# --------------------------------------------------------------------------

def free_reduce(word):
    out = []
    for letter in word:
        if out and out[-1] == -letter:
            out.pop()
        else:
            out.append(letter)
    return tuple(out)


def free_inverse(word):
    return tuple(-letter for letter in reversed(word))


def free_is_reduced(word) -> bool:
    return free_reduce(word) == tuple(word)


def aut_evaluate(automorphism, word):
    images = {i + 1: automorphism[i] for i in range(STRANDS)}
    out = []
    for letter in word:
        image = images[abs(letter)]
        out.extend(free_inverse(image) if letter < 0 else image)
    return free_reduce(out)


def aut_compose(first, later):
    """(first o later)(x) = first(later(x))."""
    return tuple(aut_evaluate(first, later[i]) for i in range(STRANDS))


EXP5_PHI = {
    1: ((1, 2, -1), (1,), (3,)),
    2: ((1,), (2, 3, -2), (2,)),
    -1: ((2,), (-2, 1, 2), (3,)),
    -2: ((1,), (3,), (-3, 2, 3)),
}
EXP5_PERM_LETTER = {
    1: (1, 0, 2),
    2: (0, 2, 1),
    -1: (1, 0, 2),
    -2: (0, 2, 1),
}
PERM_IDENTITY = (0, 1, 2)


def artin_object(word):
    """O(w) = phi_{w_n} o ... o phi_{w_1}: earlier letters act first (inner)."""
    result = IDENTITY_AUT
    for letter in word:
        result = aut_compose(EXP5_PHI[letter], result)
    return result


def exp5_incremental(word):
    """The pinned experiment-5 law: Phi(w . sigma) = Phi(w) o phi_sigma."""
    result = IDENTITY_AUT
    for letter in word:
        result = aut_compose(result, EXP5_PHI[letter])
    return result


def exp5_object_from_table(table, word):
    result = IDENTITY_AUT
    for letter in word:
        result = aut_compose(table[letter], result)
    return result


def perm_compose(first, later):
    return tuple(first[later[i]] for i in range(STRANDS))


def perm_of(word):
    result = PERM_IDENTITY
    for letter in word:
        result = perm_compose(result, EXP5_PERM_LETTER[letter])
    return result


def aut_text(automorphism):
    def letter_text(letter):
        name = "xyz"[abs(letter) - 1]
        return name if letter > 0 else name + "^-1"

    return ["".join(letter_text(l) for l in image) if image else "1" for image in automorphism]


def exp5_words(max_length=EXP5_LENGTH):
    return [tuple(w) for w in gapkit.words(EXP5_LETTERS, max_length)]


def exp5_reachable(depth=EXP5_BFS_DEPTH):
    """Breadth-first enumeration of the object layer Aut(F_3), deduplicated."""
    seen = {IDENTITY_AUT}
    frontier = [IDENTITY_AUT]
    cumulative = {0: 1}
    for level in range(1, depth + 1):
        nxt = []
        for A in frontier:
            for letter in EXP5_LETTERS:
                B = aut_compose(EXP5_PHI[letter], A)
                if B not in seen:
                    seen.add(B)
                    nxt.append(B)
        frontier = nxt
        cumulative[level] = len(seen)
    return seen, cumulative


def attempt_exp5(words):
    for letter, inverse in ((1, -1), (2, -2)):
        require(aut_compose(EXP5_PHI[letter], EXP5_PHI[inverse]) == IDENTITY_AUT,
                "EXP4-RELATION-SOUNDNESS",
                f"phi(s{letter}) o phi(s{letter}^-1) is not the identity")
        require(aut_compose(EXP5_PHI[inverse], EXP5_PHI[letter]) == IDENTITY_AUT,
                "EXP4-RELATION-SOUNDNESS",
                f"phi(s{letter}^-1) o phi(s{letter}) is not the identity")
    require(exp5_incremental((1, 2, 1)) == exp5_incremental((2, 1, 2)), "EXP4-RELATION-SOUNDNESS",
            "s1 s2 s1 and s2 s1 s2 disagree under the pinned Artin action")
    require(artin_object((1, 2, 1)) == artin_object((2, 1, 2)), "EXP4-RELATION-SOUNDNESS",
            "s1 s2 s1 and s2 s1 s2 disagree under the chronological object composition")
    for letter, automorphism in EXP5_PHI.items():
        for image in automorphism:
            require(free_is_reduced(image), "EXP4-REDUCTION-NOT-ADJACENT",
                    f"the generator image of s{letter} is not freely reduced: {image}")

    dictionary_checks = 0
    for word in [tuple(w) for w in gapkit.words(EXP5_LETTERS, 4)]:
        require(artin_object(word) == exp5_incremental(tuple(reversed(word))),
                "EXP4-CONVENTION-DICTIONARY",
                f"O({word}) differs from the pinned law applied to the reversed word")
        dictionary_checks += 1

    for name, letters, expected in EXP5_PAIR_HAND:
        observed = aut_text(artin_object(letters))
        require(observed == expected, "EXP4-HAND-TABLE-MISMATCH",
                f"the object of {name} is {observed}, the frozen table says {expected}")

    require(per_length(words) == {0: 1, 1: 4, 2: 16, 3: 64, 4: 256, 5: 1024, 6: 4096},
            "EXP4-ENUMERATION-MISMATCH",
            f"the crossing-word domain is {per_length(words)}, expected the declared 5461 words")
    objects = {}
    reduced_classes = {}
    perm_classes = {}
    for word in words:
        objects.setdefault(artin_object(word), word)
        reduced_classes.setdefault(free_reduce(word), word)
        perm_classes.setdefault(perm_of(word), word)
    layers = {
        "L4_literal_words": len(words),
        "L3_free_reduction_classes": len(reduced_classes),
        "L2_artin_object_classes": len(objects),
        "L1_endpoint_permutation_classes": len(perm_classes),
        "literal_to_reduced_merges": len(words) - len(reduced_classes),
        "reduced_to_object_merges": len(reduced_classes) - len(objects),
        "object_to_permutation_merges": len(objects) - len(perm_classes),
    }
    require(layers["L2_artin_object_classes"] == 577 and layers["L3_free_reduction_classes"] == 1457
            and layers["L1_endpoint_permutation_classes"] == 6, "EXP4-EXP5-LAYER-MISMATCH",
            f"the pinned layer counts are not reproduced: {layers}")

    per_object_perm = {}
    for word in words:
        per_object_perm.setdefault(artin_object(word), set()).add(perm_of(word))
    for A, perms in per_object_perm.items():
        require(len(perms) == 1, "EXP4-EXP5-PERM-FUNCTION",
                f"the object {aut_text(A)} carries two different endpoint permutations")

    class_list = sorted(objects)
    single_probe = {}
    for name in EXP5_PROBE_ORDER:
        signatures = {}
        for A in class_list:
            value = aut_evaluate(A, EXP5_PROBES[name])
            signatures[value] = signatures.get(value, 0) + 1
        collisions = [v for v in signatures.values() if v > 1]
        single_probe[name] = {"distinct_signatures": len(signatures),
                              "collision_groups": len(collisions),
                              "largest_collision": max(collisions) if collisions else 1}
    require(single_probe["x1"]["collision_groups"] == 101
            and single_probe["x1"]["largest_collision"] == 13, "EXP4-PROBE-SEPARATION",
            f"the pinned x1 probe collisions are not reproduced: {single_probe['x1']}")
    minimal = None
    for size in range(1, len(EXP5_PROBE_ORDER) + 1):
        for subset in itertools.combinations(EXP5_PROBE_ORDER, size):
            seen = set()
            ok = True
            for A in class_list:
                key = tuple(aut_evaluate(A, EXP5_PROBES[name]) for name in subset)
                if key in seen:
                    ok = False
                    break
                seen.add(key)
            if ok:
                minimal = list(subset)
                break
        if minimal is not None:
            break
    require(minimal is not None, "EXP4-PROBE-SEPARATION",
            "no subfamily of the frozen probe family separates the declared object classes")

    left_word, right_word = (1, 2, 1), (2, 1, 2)
    require(artin_object(left_word) == artin_object(right_word), "EXP4-EXP5-HISTORY",
            "s1 s2 s1 and s2 s1 s2 do not share the object")
    require((left_word.count(1), left_word.count(2)) != (right_word.count(1), right_word.count(2)),
            "EXP4-EXP5-HISTORY", "the two histories have equal generator counts")
    empty, square = (), (1, 1)
    require(perm_of(empty) == perm_of(square) and artin_object(empty) != artin_object(square),
            "EXP4-EXP5-HISTORY", "the permutation layer no longer collides on s1^2")

    reachable, cumulative = exp5_reachable()
    assoc_checks = 0
    ordered = sorted(reachable)
    for A, B, C in itertools.product(ordered, ordered, ordered):
        require(aut_compose(aut_compose(A, B), C) == aut_compose(A, aut_compose(B, C)),
                "EXP4-ASSOCIATIVITY", "automorphism composition is not associative")
        assoc_checks += 1
    for A in ordered:
        require(aut_compose(IDENTITY_AUT, A) == A and aut_compose(A, IDENTITY_AUT) == A,
                "EXP4-IDENTITY", "the identity automorphism is not two-sided")
    successors = {}
    successor_checks = 0
    for word in words:
        A = artin_object(word)
        for letter in EXP5_LETTERS:
            successors.setdefault((A, letter), set()).add(artin_object(word + (letter,)))
            successor_checks += 1
    for (A, letter), images in successors.items():
        require(len(images) == 1, "EXP4-CLOSED-UPDATE",
                f"the object {aut_text(A)} has two different successors under letter {letter}")

    split_checks = 0
    split_failures = []
    for word in [tuple(w) for w in gapkit.words(EXP5_LETTERS, EXP5_SPLIT_LENGTH)]:
        for cut in range(len(word) + 1):
            w1, w2 = word[:cut], word[cut:]
            split_checks += 1
            if artin_object(w1 + w2) != aut_compose(artin_object(w2), artin_object(w1)):
                split_failures.append([list(w1), list(w2)])
    require(not split_failures, "EXP4-DESCENT-DISAGREEMENT",
            f"the split descent failed on {split_failures[:3]}")
    probe_checks = 0
    probe_failures = []
    for word in [tuple(w) for w in gapkit.words(EXP5_LETTERS, EXP5_SPLIT_LENGTH)]:
        object_value = artin_object(word)
        for name in EXP5_PROBE_ORDER:
            probe = EXP5_PROBES[name]
            stepwise = probe
            for letter in word:      # chronological order: the first letter acts first
                stepwise = aut_evaluate(EXP5_PHI[letter], stepwise)
            probe_checks += 1
            if aut_evaluate(object_value, probe) != stepwise:
                probe_failures.append({"word": list(word), "probe": name})
    require(not probe_failures, "EXP4-DESCENT-DISAGREEMENT",
            f"the probe descent failed on {probe_failures[:3]}")

    new_elements = reachable - set(objects)
    require(not new_elements, "EXP4-ELEVATION-NOT-ESTABLISHED",
            f"the object layer reached {len(new_elements)} elements with no literal preimage")

    return {
        "model": ("the declared experiment-5 model: crossing words over {s1,s2,s1^-1,s2^-1}, the "
                  "Artin action on F_3, and the endpoint permutation"),
        "convention": {
            "word_order": "crossing letters are read left to right in time",
            "object_composition": ("O(w ++ (sigma,)) = phi_sigma o O(w), i.e. "
                                   "O(w) = phi_{w_n} o ... o phi_{w_1}"),
            "dictionary_to_pinned_law": ("the pinned experiment-5 law Phi(w . sigma) = Phi(w) o phi_sigma "
                                         "equals O with the word reversed; verified as an obligation"),
            "dictionary_checks": dictionary_checks,
        },
        "domain": {"crossing_words": {str(k): v for k, v in sorted(per_length(words).items())},
                   "total": len(words)},
        "layers": layers,
        "layers_status": "bounded-domain-compatible",
        "probe_family": {
            "probes": list(EXP5_PROBE_ORDER),
            "object_classes": len(class_list),
            "single_probe": single_probe,
            "minimal_separating_subfamily": minimal,
            "minimal_size": len(minimal) if minimal else None,
            "status": "bounded-domain-compatible",
        },
        "gates": {
            "gate_i_task_sufficiency": {
                "verdict": "PASS-FOR-THE-DECLARED-GROUP-LEVEL-TASK",
                "permutation_is_a_function_of_the_object": len(per_object_perm),
                "argument": ("if two words have the same Artin object then, given the stated hypothesis "
                             "that Artin's representation B_n -> Aut(F_n) is faithful, they are the same "
                             "braid element, and the endpoint permutation factors through the braid "
                             "group, so their permutations agree"),
                "history_task": {
                    "verdict": "FAIL",
                    "witness": {
                        "words": ["s1 s2 s1", "s2 s1 s2"],
                        "object": aut_text(artin_object(left_word)),
                        "generator_counts": [{"s1": left_word.count(1), "s2": left_word.count(2),
                                              "S1": left_word.count(-1), "S2": left_word.count(-2)},
                                             {"s1": right_word.count(1), "s2": right_word.count(2),
                                              "S1": right_word.count(-1), "S2": right_word.count(-2)}],
                        "permutations": [list(perm_of(left_word)), list(perm_of(right_word))],
                    },
                    "second_witness": {
                        "words": ["epsilon", "s1 s1"],
                        "permutations": [list(perm_of(empty)), list(perm_of(square))],
                        "objects_equal": artin_object(empty) == artin_object(square),
                    },
                    "localisation": ("the quotient that objectifies the crossing process merges literal "
                                     "histories with different generator counts; it serves the group-level "
                                     "task and does not serve a task that observes construction history"),
                    "status": "proved",
                },
                "status": "proved-with-stated-hypotheses",
            },
            "gate_ii_stable_interface": {
                "verdict": "PASS",
                "reachable_objects": {str(k): v for k, v in sorted(cumulative.items())},
                "associativity_checks": assoc_checks,
                "closed_update_checks": successor_checks,
                "closure": "the composition of two automorphisms of F_3 is an automorphism of F_3",
                "status": "proved",
            },
            "gate_iii_exact_descent": {
                "verdict": "PASS",
                "split_checks": split_checks,
                "probe_checks": probe_checks,
                "mismatches": 0,
                "test": ("compose at the object layer then evaluate on a probe, against applying the "
                         "letters one at a time at the bottom layer in the declared chronological order "
                         "(first letter first), and against splitting the word"),
                "status": "proved",
                "general_argument": ("O is defined by composing the generator automorphisms and "
                                     "composition of functions is associative, so "
                                     "O(w1 ++ w2) = O(w2) o O(w1) for every pair of words, by induction "
                                     "on |w2|; the sweep calibrates that induction"),
            },
        },
        "elevation": {
            "verdict": "NO-ELEVATION",
            "E1": {"verdict": "FAILS",
                   "witness": "every object generator is the image of a length-one crossing word"},
            "E2": {"verdict": "FAILS",
                   "witness": (f"the object layer reaches exactly the {len(objects)} images of the declared "
                               f"literal words while the literal layer has {len(words)} words, so the map is "
                               "surjective and adds no element"),
                   "merges": layers["literal_to_reduced_merges"] + layers["reduced_to_object_merges"]},
            "E3": {"verdict": "HOLDS",
                   "witness": "the object action on the probe family is total and non-constant"},
            "E4": {"verdict": "FAILS",
                   "witness": ("a composite such as s1 s2 is a new object, but it is already the image of "
                               "the literal word s1 s2, so the higher grammar adds no element that the "
                               "bottom layer does not reach")},
            "E5": {"verdict": "HOLDS", "witness": "the layer counts are exactly the quotient merges"},
            "status": "proved",
        },
        "finding": ("no objectification gate fails at the declared group-level task, and the elevation "
                    "criterion fails: the Aut(F_3) layer is a quotient object (a decision-complete, "
                    "composable stabilisation of literal histories) rather than a new rank"),
    }


# --------------------------------------------------------------------------
# costs
# --------------------------------------------------------------------------

def base_costs(domain):
    return {
        "pi_out": _cost_of_tier(domain, lambda w: lower(pair_of(w), INITIAL_STATE),
                                answer_steps=1, answers_task=False),
        "pi_obj": _cost_of_tier(domain, lambda w: list(pair_of(w)),
                                answer_steps=len(DECLARED_STATES), answers_task=True),
        "pi_hist": _hist_cost(domain),
    }


def _cost_of_tier(domain, key, answer_steps, answers_task):
    cost = gapkit.Cost()
    sizes = []
    for w in domain:
        payload = key(w)
        cost.store(payload)
        cost.step(len(w))
        sizes.append(len(gapkit.canonical(payload).encode("utf-8")))
    cost.observe(len(domain) * answer_steps)
    cost.verify(len(domain))
    return {
        "storage_bytes": cost.storage_bytes,
        "structural_size": cost.structural_size,
        "build_steps": cost.computation_steps,
        "answer_steps": len(domain) * answer_steps,
        "observations": cost.observations,
        "verification_cost": cost.verification_cost,
        "mean_storage_bytes_per_word": qtext(Fraction(sum(sizes), len(sizes))),
        "max_storage_bytes_per_word": max(sizes),
        "answers_declared_task": answers_task,
    }


def _hist_cost(domain):
    cost = gapkit.Cost()
    sizes = []
    for w in domain:
        payload = [word_text(w)]
        cost.store(payload)
        cost.step(len(w))
        sizes.append(len(gapkit.canonical(payload).encode("utf-8")))
    answer_steps = sum(len(w) * len(DECLARED_STATES) for w in domain)
    cost.observe(len(domain) * len(DECLARED_STATES))
    cost.verify(sum(len(w) for w in domain))
    return {
        "storage_bytes": cost.storage_bytes,
        "structural_size": cost.structural_size,
        "build_steps": cost.computation_steps,
        "answer_steps": answer_steps,
        "observations": cost.observations,
        "verification_cost": cost.verification_cost,
        "mean_storage_bytes_per_word": qtext(Fraction(sum(sizes), len(sizes))),
        "max_storage_bytes_per_word": max(sizes),
        "answers_declared_task": True,
    }


def attempt_costs(all_words, legal_words, exp5_word_list):
    out = {}
    exp2_scalar = gapkit.Cost()
    exp2_object = gapkit.Cost()
    exp2_hist = gapkit.Cost()
    for w in all_words:
        exp2_scalar.store(qtext(exp2_accum(w)))
        exp2_scalar.step(1)
        P = exp2_pair_of(w)
        exp2_object.store([qtext(P[0]), qtext(P[1])])
        exp2_object.step(1)
        exp2_hist.store([exp2_word_text(w)])
        exp2_hist.step(len(w))
    out["exp2_scalar"] = exp2_scalar.as_record()
    out["exp2_object"] = exp2_object.as_record()
    out["exp2_hist"] = exp2_hist.as_record()
    out["exp2_counts"] = {"all_words": len(all_words), "legal_words": len(legal_words)}

    exp5_l1 = gapkit.Cost()
    exp5_l2 = gapkit.Cost()
    exp5_l4 = gapkit.Cost()
    for w in exp5_word_list:
        exp5_l1.store(list(perm_of(w)))
        exp5_l1.step(1)
        exp5_l2.store(aut_text(artin_object(w)))
        exp5_l2.step(len(w))
        exp5_l4.store([[int(x) for x in w]])
        exp5_l4.step(len(w))
    out["exp5_permutation"] = exp5_l1.as_record()
    out["exp5_artin_object"] = exp5_l2.as_record()
    out["exp5_literal"] = exp5_l4.as_record()
    out["exp5_words"] = len(exp5_word_list)
    return out


def reachable_growth():
    table = {}
    for name, alphabet in (("base_sweep", BASE_ALPHABET), ("essay_alphabet", ESSAY_ALPHABET),
                           ("translation_only", TRANSLATION_ONLY), ("pure_dilation", PURE_DILATION)):
        _, cumulative = reachable_objects(alphabet, BASE_LENGTH)
        table[name] = {
            "generators": len(alphabet),
            "words_up_to_length": sum(len(alphabet) ** n for n in range(BASE_LENGTH + 1)),
            "reachable_objects": {str(k): v for k, v in sorted(cumulative.items())},
            "status": "bounded-domain-compatible",
        }
    return table


# --------------------------------------------------------------------------
# negative controls
# --------------------------------------------------------------------------

def negative_controls():
    controls = []
    frozen = _read_frozen()

    def contract_drift():
        text = CONTRACT.read_text(encoding="utf-8")
        mutated = text.replace('"version": "1"', '"version": "1-mutated"', 1)
        require(mutated != text, "EXP-CONTRACT-DRIFT", "the contract copy was not actually mutated")
        directory = Path(tempfile.mkdtemp())
        copy = directory / CONTRACT.name
        copy.write_text(mutated, encoding="utf-8")
        observed = gapkit.sha256_file(copy)
        require(frozen.get(CONTRACT.name) == observed, "EXP-CONTRACT-DRIFT",
                f"the mutated copy digest {observed} matches the frozen ledger entry")
    controls.append({"id": "contract-drift", "expected": "EXP-CONTRACT-DRIFT",
                     "observed": gapkit.reject(contract_drift, "EXP-CONTRACT-DRIFT")})

    def endpoint_sufficiency():
        w1, w2 = (("T", 2), ("D", 3)), (("T", 3), ("D", 2))
        require(lower(pair_of(w1), INITIAL_STATE) != lower(pair_of(w2), INITIAL_STATE),
                "EXP4-SUMMARY-INSUFFICIENT",
                "the single declared evaluation separated T_2 D_3 from T_3 D_2")
    controls.append({"id": "endpoint-value-insufficiency", "expected": "EXP4-SUMMARY-INSUFFICIENT",
                     "observed": gapkit.reject(endpoint_sufficiency, "EXP4-SUMMARY-INSUFFICIENT")})

    def naive_lowering():
        word = (("D", 2), ("T", 1))
        require(lower(naive_fold(word), 0) == execute(word, 0), "EXP4-DESCENT-DISAGREEMENT",
                "lowering D_k to T_k agreed with bottom execution on the word D_2 T_1")
    controls.append({"id": "naive-dilation-lowering", "expected": "EXP4-DESCENT-DISAGREEMENT",
                     "observed": gapkit.reject(naive_lowering, "EXP4-DESCENT-DISAGREEMENT")})

    def composition_order():
        w1, w2 = (("D", 2), ("T", 1)), (("T", 3),)
        require(star(pair_of(w1), pair_of(w2)) == pair_of(w1 + w2), "EXP4-COMPOSITION-ORDER",
                "the chronological multiplication order agreed with the declared order")
    controls.append({"id": "composition-order-flip", "expected": "EXP4-COMPOSITION-ORDER",
                     "observed": gapkit.reject(composition_order, "EXP4-COMPOSITION-ORDER")})

    def unscaled_cross():
        a, k = 1, 2
        require(star(generator_pair(("T", a)), generator_pair(("D", k)))
                == star(generator_pair(("D", k)), generator_pair(("T", a))), "EXP4-CROSS-RELATION",
                "the unscaled cross relation D_k T_a = T_a D_k held")
    controls.append({"id": "cross-relation-without-scaling", "expected": "EXP4-CROSS-RELATION",
                     "observed": gapkit.reject(unscaled_cross, "EXP4-CROSS-RELATION")})

    def dilation_domain():
        require(all(is_valid_dilation(k) for k in (0, -1, Fraction(1, 2))), "EXP4-DILATION-DOMAIN",
                "D_0, D_-1 or D_1/2 was admitted as a dilation object")
    controls.append({"id": "dilation-domain-zero", "expected": "EXP4-DILATION-DOMAIN",
                     "observed": gapkit.reject(dilation_domain, "EXP4-DILATION-DOMAIN")})
    refused = {}
    for bad in (0, -1, Fraction(1, 2)):
        record = gapkit.reject(lambda b=bad: dilation_pair(b), "EXP4-DILATION-DOMAIN")
        require(record["code"] == "EXP4-DILATION-DOMAIN", "EXP4-DILATION-DOMAIN",
                f"dilation_pair({bad}) was admitted")
        refused[qtext(bad)] = record["detail"]

    def route_disagreement():
        honest = pair_of((("D", 2), ("T", 3)))
        mutated = (honest[0], honest[1] + 1)
        require(mutated == honest, "EXP4-ROUTE-DISAGREEMENT",
                f"one route returned {mutated} and the other {honest} for the same word")
    controls.append({"id": "matrix-route-disagreement", "expected": "EXP4-ROUTE-DISAGREEMENT",
                     "observed": gapkit.reject(route_disagreement, "EXP4-ROUTE-DISAGREEMENT")})

    def enumeration_mismatch():
        mutated = [tuple(w) for w in gapkit.words(BASE_ALPHABET[:-1], BASE_LENGTH)]
        require(len(mutated) == 3906, "EXP4-ENUMERATION-MISMATCH",
                f"the declared base sweep total is 3906, the mutated alphabet enumerates {len(mutated)}")
    controls.append({"id": "enumerated-count-mismatch", "expected": "EXP4-ENUMERATION-MISMATCH",
                     "observed": gapkit.reject(enumeration_mismatch, "EXP4-ENUMERATION-MISMATCH")})

    def named_power():
        named = pair_of((("T", 2), ("T", 2), ("T", 2)))
        require(named not in TRANSLATION_SUBGROUP, "EXP4-NAMING-NOT-ELEVATION",
                "the named composite T_2^3 was claimed to lie outside the lower translation layer")
    controls.append({"id": "named-power-as-elevation", "expected": "EXP4-NAMING-NOT-ELEVATION",
                     "observed": gapkit.reject(named_power, "EXP4-NAMING-NOT-ELEVATION")})

    def exp2_sufficiency():
        left, right = ("c", "v", "c"), ("c", "c", "v", "c", "v")
        require(exp2_pair_of(left) != exp2_pair_of(right), "EXP4-EXP2-SUFFICIENCY-CLAIM",
                "the accumulator object separated the legal words cvc and ccvcv")
    controls.append({"id": "exp2-object-sufficiency", "expected": "EXP4-EXP2-SUFFICIENCY-CLAIM",
                     "observed": gapkit.reject(exp2_sufficiency, "EXP4-EXP2-SUFFICIENCY-CLAIM")})

    def exp5_elevation():
        reachable, _ = exp5_reachable()
        images = {artin_object(w) for w in exp5_words()}
        require(reachable - images, "EXP4-ELEVATION-NOT-ESTABLISHED",
                "an object with no literal preimage was claimed for the Artin object layer")
    controls.append({"id": "exp5-elevation-claim", "expected": "EXP4-ELEVATION-NOT-ESTABLISHED",
                     "observed": gapkit.reject(exp5_elevation, "EXP4-ELEVATION-NOT-ESTABLISHED")})

    def mutated_hand_table():
        for word, expected in sorted(EXP2_FROZEN_ACCUMULATOR.items()):
            value = Fraction(0)
            for sigma in word:
                if sigma == "c":
                    value = 2 * value + 1
                elif sigma == "v":
                    value = value - 1
                else:
                    value = value + 1
            require(qtext(value) == expected, "EXP4-HAND-TABLE-MISMATCH",
                    f"mutated A({word!r}) = {qtext(value)}, the frozen table says {expected}")
    controls.append({"id": "hand-table-mutated", "expected": "EXP4-HAND-TABLE-MISMATCH",
                     "observed": gapkit.reject(mutated_hand_table, "EXP4-HAND-TABLE-MISMATCH")})

    def mutated_braid_relation():
        broken = dict(EXP5_PHI)
        broken[2] = ((1,), (2, 3, -2), (2, 1))
        require(exp5_object_from_table(broken, (1, 2, 1)) == exp5_object_from_table(broken, (2, 1, 2)),
                "EXP4-RELATION-SOUNDNESS",
                "s1 s2 s1 and s2 s1 s2 disagreed under the mutated Artin action")
    controls.append({"id": "exp5-braid-relation-mutated", "expected": "EXP4-RELATION-SOUNDNESS",
                     "observed": gapkit.reject(mutated_braid_relation, "EXP4-RELATION-SOUNDNESS")})

    def wrong_reduction():
        require(free_reduce((1, 2, -1)) == (2,), "EXP4-REDUCTION-NOT-ADJACENT",
                "a non-adjacent cancellation was performed in F_3")
    controls.append({"id": "free-reduction-wrong", "expected": "EXP4-REDUCTION-NOT-ADJACENT",
                     "observed": gapkit.reject(wrong_reduction, "EXP4-REDUCTION-NOT-ADJACENT")})

    def illegal_action():
        require("v" in exp2_legal(()), "EXP4-ILLEGAL-ACTION",
                "the mechanism v was executed where the declared legality excludes it")
    controls.append({"id": "illegal-exp2-action", "expected": "EXP4-ILLEGAL-ACTION",
                     "observed": gapkit.reject(illegal_action, "EXP4-ILLEGAL-ACTION")})
    record = gapkit.reject(lambda: exp2_step((), "v"), "EXP4-ILLEGAL-ACTION")
    require(record["code"] == "EXP4-ILLEGAL-ACTION", "EXP4-ILLEGAL-ACTION",
            "exp2_step accepted an illegal mechanism")
    return controls, refused


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


# --------------------------------------------------------------------------
# main
# --------------------------------------------------------------------------

def run():
    require(CONTRACT.exists(), "EXP4-CONTRACT-MISSING", str(CONTRACT))
    contract_sha = gapkit.sha256_file(CONTRACT)
    frozen = _read_frozen()
    require(frozen.get(CONTRACT.name, contract_sha) == contract_sha, "EXP-CONTRACT-DRIFT",
            f"{CONTRACT.name}: frozen {frozen.get(CONTRACT.name)!r} != actual {contract_sha}")

    domain = enumerated_domain(BASE_ALPHABET, BASE_LENGTH)
    counts = per_length(domain)
    require(counts == {0: 1, 1: 5, 2: 25, 3: 125, 4: 625, 5: 3125} and len(domain) == 3906,
            "EXP4-ENUMERATION-MISMATCH",
            f"the declared base sweep is {counts} with {len(domain)} words, expected 3906")
    objects, object_growth = reachable_objects(BASE_ALPHABET, ASSOCIATIVITY_DEPTH)

    for name, word, expected in BASE_PAIR_HAND:
        observed = pair_of(word)
        require(observed == expected, "EXP4-HAND-TABLE-MISMATCH",
                f"the object of {name} is {observed}, the frozen table says {expected}")

    relations = check_relations()
    injectivity = check_injectivity(objects)
    composition = check_composition(domain, objects)
    uniform = repetition_vs_uniform()
    gate_i = gate_i_base(domain)
    gate_ii = gate_ii_base(domain, objects)
    gate_iii = gate_iii_base(domain)
    elevation = elevation_base()

    exp2_all = enumerated_domain(EXP2_ALPHABET, EXP2_ALL_LENGTH)
    exp2_legal_words = exp2_legal_domain()
    attempt2 = attempt_exp2(exp2_all, exp2_legal_words)

    exp5_word_list = exp5_words()
    attempt5 = attempt_exp5(exp5_word_list)

    costs = {
        "base_model": base_costs(domain),
        "attempts": attempt_costs(exp2_all, exp2_legal_words, exp5_word_list),
        "reachable_object_growth": reachable_growth(),
    }

    controls, refused_dilations = negative_controls()

    record = {
        "schema": SCHEMA,
        "contract": {"path": str(CONTRACT.relative_to(ROOT.parent.parent)), "sha256": contract_sha},
        "environment": gapkit.environ(),
        "source_baseline": SOURCE_BASELINE,
        "convention": {
            "declared": ("chronological words, with the declared pair (b,k) meaning x -> k*x + b and "
                         "the product (b,k)*(c,l) = (b + k*c, k*l); appending in time multiplies on "
                         "the left"),
            "word_order": "g_1 acts first, g_n acts last (ProcessWord chronology)",
            "algebraic_juxtaposition": "XY applies Y first, then X (the pinned note's convention)",
            "dictionary": SOURCE_BASELINE["quoted_dictionary"],
            "orientation_verified": composition["orientation_trap"],
        },
        "domain": {
            "base_sweep": {str(k): v for k, v in sorted(counts.items())},
            "base_sweep_total": len(domain),
            "declared_states": list(DECLARED_STATES),
            "initial_state": INITIAL_STATE,
            "exhaustive": True,
            "note": ("full word lists are not embedded; the per-length counts and the reachable-object "
                     "counts are, and the reproduction commands regenerate the lists deterministically"),
        },
        "baseline_control": {
            "relations": relations,
            "injectivity_lemma": injectivity,
            "composition": composition,
            "repetition_versus_uniform": uniform,
            "gates": {
                "gate_i_task_sufficiency_pi_out": gate_i,
                "gate_ii_stable_interface": gate_ii,
                "gate_iii_exact_descent": gate_iii,
            },
            "elevation": elevation,
            "verdict": {
                "gate_i_pi_out": gate_i["verdict"],
                "gate_i_pi_obj": ("PASS: object equality is map equality by the injectivity lemma, and "
                                  "every object is a declared pair, so no two task-distinct words share "
                                  "an object"),
                "gate_ii": gate_ii["verdict"],
                "gate_iii": gate_iii["verdict"],
                "elevation": elevation["verdict"],
                "status": "proved",
            },
        },
        "attempts": {"exp2_accumulator_object": attempt2, "exp5_artin_object": attempt5},
        "cost": costs,
        "negative_controls": controls,
        "dilation_domain_refusals": refused_dilations,
        "bounded_sweep_disclaimer": BOUNDED_SWEEP_DISCLAIMER,
        "boundary": {
            "claimed": [
                "the declared laws are proved by exact integer or rational algebra, with the sweeps as calibrations",
                "gate (i) of the baseline object layer passes; gate (i) of the single-evaluation summary fails with a minimal witness",
                "the experiment-2 accumulator object passes gates (ii) and (iii) and the elevation criterion, and fails gate (i)",
                "the experiment-5 Artin object passes all three gates at the group-level task and fails the elevation criterion",
            ],
            "not_claimed": [
                "no generic objectification, rank, or lowering API is proposed or implemented",
                "no unbounded or adaptive continuation is implemented",
                "a bounded descent sweep is never a general consistency proof; the general arguments are stated separately",
                "no claim about dilation parameters outside N_>0",
                "no claim that the Artin object layer is useless: it is a quotient object with a decidable equality",
            ],
            "open": [
                "whether the experiment-2 accumulator object is sufficient for some other declared task",
                "the closed-form growth of the reachable object layer beyond the declared lengths",
                "whether any non-arithmetic model in this programme admits a genuine elevation rather than a quotient",
            ],
        },
    }
    record["baseline_control"]["reachable_object_growth"] = {
        str(k): v for k, v in sorted(object_growth.items())}

    record["history"] = {
        "rule": ("the literal word is the history and is never identified with a value; the object "
                 "layer identifies exactly the words that share an object, and every identification "
                 "is reported as a merge with its cost"),
        "retained_by_tier": {
            "pi_out": "one integer: the whole history is forgotten",
            "pi_obj": "the affine object: the uniform action is retained, the literal history is not",
            "pi_hist": "the literal word: upper-bound control, and not elevation",
        },
        "merges_on_declared_domains": {
            "base_sweep_words_to_objects_depth2": {"words": len(domain),
                                                   "objects": object_growth[ASSOCIATIVITY_DEPTH]},
            "exp2_legal_words_to_objects": {
                "words": len(exp2_legal_words),
                "objects": attempt2["gates"]["gate_i_task_sufficiency"]["object_classes_legal_domain"]},
            "exp5_words_to_objects": {"words": attempt5["layers"]["L4_literal_words"],
                                      "objects": attempt5["layers"]["L2_artin_object_classes"],
                                      "merges": attempt5["layers"]["literal_to_reduced_merges"]
                                      + attempt5["layers"]["reduced_to_object_merges"]},
        },
        "status": "bounded-domain-compatible",
    }

    record["representation"] = {
        "tiers": {
            "existing-summary": {"base_model": "pi_out", "exp2_attempt": "exp2_scalar",
                                 "exp5_attempt": "exp5_perm"},
            "bounded-enhancement": {"base_model": "pi_obj", "exp2_attempt": "exp2_object",
                                    "exp5_attempt": "exp5_artin"},
            "full-history-upper-bound": {"base_model": "pi_hist", "exp2_attempt": "exp2_hist",
                                         "exp5_attempt": "exp5_literal"},
        },
        "cost_channels": ["storage_bytes", "structural_size", "build_steps", "answer_steps",
                          "observations", "verification_cost"],
        "answers_declared_task": {"pi_out": False, "pi_obj": True, "pi_hist": True},
        "status": "computationally-verified-example",
        "note": ("costs are reported per channel and never collapsed into one number; structural_size "
                 "counts retained fields and does not measure word length, so the upper-bound control "
                 "is not cheaper in the channel that grows with the history"),
    }

    record["lowering"] = {
        "base_model": "L((b,k))(x) = k*x + b on the declared integer states",
        "exp2_attempt": "L((b,k))(x) = k*x + b on the accumulator carrier, plus A(w) = the value at 0",
        "exp5_attempt": "L(O)(p) = the free-group word O(p) for each declared probe p",
        "descent_tests": {
            "base_model": {"checks": gate_iii["checks"], "mismatches": gate_iii["mismatches"]},
            "exp2_attempt": {"checks": attempt2["gates"]["gate_iii_exact_descent"]["checks"],
                             "mismatches": attempt2["gates"]["gate_iii_exact_descent"]["mismatches"]},
            "exp5_attempt": {"split_checks": attempt5["gates"]["gate_iii_exact_descent"]["split_checks"],
                             "probe_checks": attempt5["gates"]["gate_iii_exact_descent"]["probe_checks"],
                             "mismatches": attempt5["gates"]["gate_iii_exact_descent"]["mismatches"]},
        },
        "status": "proved",
    }

    codes = sorted(control["observed"]["code"] for control in controls)
    record["conclusion"] = {
        "question_1_single_evaluation": {
            "verdict": "NO",
            "witness": ("epsilon and D_2 agree at the single declared initial state (both 0) and act "
                        "differently; the pinned fibre T_2^3 = T_6 = T_3^2 = (T_1)^6 shows that one "
                        "output has four candidate schemas"),
            "status": "proved",
        },
        "question_2_stable_object": {
            "verdict": "PARTLY",
            "detail": ("a stable, callable, composable object exists for the arithmetic calibration "
                       "(pi_obj passes gates (i) and (ii) and the descent gate (iii), and satisfies the "
                       "elevation criterion), so a stable object IS enough for a higher-order "
                       "computation in this model; the experiment-2 accumulator object is stable and "
                       "elevated and still fails gate (i); the experiment-5 Artin object passes all "
                       "three gates and fails the elevation criterion"),
            "status": "proved",
        },
        "gate_table": {
            "base_model_gate_i": gate_i["verdict"],
            "base_model_gate_ii": gate_ii["verdict"],
            "base_model_gate_iii": gate_iii["verdict"],
            "base_model_elevation": elevation["verdict"],
            "exp2_attempt_gate_i": attempt2["gates"]["gate_i_task_sufficiency"]["verdict"],
            "exp2_attempt_gate_ii": attempt2["gates"]["gate_ii_stable_interface"]["verdict"],
            "exp2_attempt_gate_iii": attempt2["gates"]["gate_iii_exact_descent"]["verdict"],
            "exp2_attempt_elevation": attempt2["elevation"]["verdict"],
            "exp5_attempt_gate_i": attempt5["gates"]["gate_i_task_sufficiency"]["verdict"],
            "exp5_attempt_gate_ii": attempt5["gates"]["gate_ii_stable_interface"]["verdict"],
            "exp5_attempt_gate_iii": attempt5["gates"]["gate_iii_exact_descent"]["verdict"],
            "exp5_attempt_elevation": attempt5["elevation"]["verdict"],
        },
        "labels": {
            "proved": ["relation laws", "composition laws", "injectivity lemma", "descent equalities",
                       "the three gate verdicts", "the three elevation verdicts"],
            "proved-with-stated-hypotheses": ["the experiment-5 gate (i) argument uses Artin faithfulness"],
            "computationally-verified-example": ["the cost tables", "the witness values"],
            "bounded-domain-compatible": ["all per-length counts", "all reachable-object counts",
                                          "all layer and merge counts", "the probe-collision counts"],
            "budget-exhausted": ["none: every declared bound completed"],
            "open": record["boundary"]["open"] if "boundary" in record else [],
        },
        "status": "proved",
    }

    record["outcomes"] = {
        "success": {
            "items": ["the three relation families", "compositional lowering on every declared word",
                      "the three objectification gates for the base model and for the experiment-5 "
                      "attempt at the group-level task", "the elevation criterion applied to the base "
                      "model and to the experiment-2 object"],
            "status": "proved",
        },
        "expected_negative": {
            "items": [
                "pi_out fails gate (i): epsilon versus D_2",
                "the experiment-2 accumulator object fails gate (i): cvc versus ccvcv, and vc versus l",
                "the experiment-5 object fails the elevation criterion: 5461 words collapse to 577 objects",
                "the naive lowering of D_k to T_k fails the descent test on the word D_2 T_1",
            ],
            "status": "proved",
        },
        "implementation_error": {
            "negative_controls": len(controls),
            "declared_codes_raised": codes,
            "status": "proved",
        },
        "budget_exhausted": {
            "exhausted": False,
            "declared_bounds": {"base_sweep_length": BASE_LENGTH, "exp2_all_length": EXP2_ALL_LENGTH,
                                "exp2_legal_length": EXP2_LEGAL_LENGTH, "exp5_length": EXP5_LENGTH,
                                "exp5_split_length": EXP5_SPLIT_LENGTH,
                                "associativity_depth": ASSOCIATIVITY_DEPTH},
            "status": "budget-exhausted",
            "note": "the slot is instantiated and empty: no declared bound was reached without completion",
        },
        "unknown": {"items": record["boundary"]["open"], "status": "open"},
    }

    return record


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", default=None)
    args = parser.parse_args()
    record = run()
    text = gapkit.canonical(record)
    if args.out:
        Path(args.out).write_text(text, encoding="utf-8")
        written = gapkit.sha256_bytes(text.encode("utf-8"))
        sys.stderr.write(f"exp4 written to {args.out} sha256={written}\n")
    else:
        sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
