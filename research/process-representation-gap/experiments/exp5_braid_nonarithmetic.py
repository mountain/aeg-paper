#!/usr/bin/env python3
"""Experiment 5 -- braids as non-arithmetic processes.

Contract: research/process-representation-gap/contracts/exp5-braid-nonarithmetic.v1.json

Native object: a crossing word on three strands.  The experiment never encodes
the process as arithmetic and never uses a matrix.  The observation layers are

    L4 literal crossing word
    L3 freely reduced word
    L2 Artin automorphism of F_3   (image triple)
    L1 endpoint permutation in S_3

Artin's representation B_n -> Aut(F_n) is faithful, so L2 determines the braid
group element exactly; that theorem is USED, not reproved, and faithfulness is
claimed only at the braid-element layer.

Conventions, declared before running:
  * the letters of a crossing word are read left to right in time;
  * automorphisms compose by (f o g)(x) = f(g(x)), and
    Phi(empty) = id, Phi(w . sigma) = Phi(w) o phi_sigma;
  * sigma_i sends x_i to x_i x_{i+1} x_i^{-1} and x_{i+1} to x_i;
  * sigma_i^{-1} sends x_i to x_{i+1} and x_{i+1} to x_{i+1}^{-1} x_i x_{i+1}.

Both relations are re-verified here rather than assumed.

Run:

    python3 research/process-representation-gap/experiments/exp5_braid_nonarithmetic.py
"""

from __future__ import annotations

import argparse
import itertools
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(ROOT / "tools"))
import gapkit  # noqa: E402
from gapkit import Diagnostic, require  # noqa: E402

CONTRACT = ROOT / "contracts" / "exp5-braid-nonarithmetic.v1.json"
FROZEN = ROOT / "contracts" / "FROZEN.sha256"
EVIDENCE = ROOT / "evidence" / "exp5-braid-nonarithmetic.json"
RAW_TABLE = ROOT / "evidence" / "exp5-braid-words.raw.json"

SCHEMA = "aeg.process-representation-gap.exp5.v1"
STRANDS = 3
MAX_LENGTH = 6
LETTERS = (1, 2, -1, -2)          # s1, s2, S1, S2  (declared lexicographic order)
LETTER_NAMES = {1: "s1", 2: "s2", -1: "S1", -2: "S2"}

# Free-group generators are signed integers: +i means x_i, -i means x_i^{-1}.
IDENTITY = ((1,), (2,), (3,))

# Pre-registered probe family, frozen before the experiment runs.
PROBES = {
    "x1": (1,),
    "x2": (2,),
    "x3": (3,),
    "x1x2": (1, 2),
    "x1x2x3": (1, 2, 3),
    "x1x2x1^-1": (1, 2, -1),
    "commutator": (1, 2, 3, -1, -2, -3),
    "(x1x2)^3": (1, 2, 1, 2, 1, 2),
}
PROBE_ORDER = tuple(PROBES)


# --------------------------------------------------------------------------
# free group F_3
# --------------------------------------------------------------------------

def free_reduce(word):
    """Cancel adjacent inverse pairs, left to right, to a reduced word."""
    out = []
    for letter in word:
        if out and out[-1] == -letter:
            out.pop()
        else:
            out.append(letter)
    return tuple(out)


def free_inverse(word):
    return tuple(-letter for letter in reversed(word))


def check_reduced(word, code="EXP5-REDUCTION-NOT-ADJACENT"):
    require(free_reduce(word) == tuple(word), code, f"word is not freely reduced: {word}")
    return word


# --------------------------------------------------------------------------
# Aut(F_3): an automorphism is the triple of images of x1, x2, x3
# --------------------------------------------------------------------------

def evaluate(automorphism, word):
    """Apply an automorphism to a free word by substituting the generator images."""
    images = {i + 1: automorphism[i] for i in range(STRANDS)}
    out = []
    for letter in word:
        image = images[abs(letter)]
        if letter < 0:
            out.extend(free_inverse(image))
        else:
            out.extend(image)
    return free_reduce(out)


def compose(first, later):
    """(first o later)(x) = first(later(x))."""
    return tuple(evaluate(first, later[i]) for i in range(STRANDS))


PHI = {
    1: ((1, 2, -1), (1,), (3,)),      # sigma_1
    2: ((1,), (2, 3, -2), (2,)),      # sigma_2
    -1: ((2,), (-2, 1, 2), (3,)),     # sigma_1^{-1}
    -2: ((1,), (3,), (-3, 2, 3)),     # sigma_2^{-1}
}

PERM_TRANSPOSITION = {
    1: (1, 0, 2),      # zero-based images: 0->1, 1->0, 2->2   (1 2)
    2: (0, 2, 1),      # 1<->2                                    (2 3)
    -1: (1, 0, 2),
    -2: (0, 2, 1),
}
PERM_IDENTITY = (0, 1, 2)


def perm_compose(first, later):
    """(first o later)(i) = first(later(i))."""
    return tuple(first[later[i]] for i in range(STRANDS))


def phi_of(word):
    """Phi(w) by the declared homomorphism, computed by composition."""
    result = IDENTITY
    for letter in word:
        result = compose(result, PHI[letter])
    return result


def perm_of(word):
    result = PERM_IDENTITY
    for letter in word:
        result = perm_compose(result, PERM_TRANSPOSITION[letter])
    return result


def artin_apply(word, probe):
    """Evaluate a probe under Phi(w)."""
    return evaluate(phi_of(word), probe)


# --------------------------------------------------------------------------
# layers
# --------------------------------------------------------------------------

def exponent_summary(word):
    s1 = sum(1 for L in word if L == 1)
    s2 = sum(1 for L in word if L == 2)
    S1 = sum(1 for L in word if L == -1)
    S2 = sum(1 for L in word if L == -2)
    return (s1 - S1, s2 - S2, s1, s2, S1, S2)


def enumerate_words(max_length=MAX_LENGTH):
    return [tuple(w) for w in gapkit.words(LETTERS, max_length)]


def word_text(word):
    return "".join(LETTER_NAMES[L] for L in word) if word else "1"


# --------------------------------------------------------------------------
# mandatory witnesses
# --------------------------------------------------------------------------

def witness_w1():
    empty, square = (), (1, 1)
    return {
        "id": "W1-square-versus-trivial",
        "pair": [word_text(empty), word_text(square)],
        "endpoint_per_permutation": [list(perm_of(empty)), list(perm_of(square))],
        "same_endpoint_permutation": perm_of(empty) == perm_of(square),
        "artin_images": [_images(phi_of(empty)), _images(phi_of(square))],
        "same_braid_element": phi_of(empty) == phi_of(square),
        "separated_by_artin": phi_of(empty) != phi_of(square),
        "conclusion": ("the coarsest layer L1 cannot see the torsion that L2 sees; "
                       "sigma_1^2 is not trivial in B_3"),
    }


def witness_w2():
    left, right = (1, 2, 1), (2, 1, 2)
    return {
        "id": "W2-artin-relation",
        "pair": [word_text(left), word_text(right)],
        "same_literal_word": left == right,
        "generator_counts": {
            word_text(left): list(exponent_summary(left)),
            word_text(right): list(exponent_summary(right)),
        },
        "same_generator_counts": exponent_summary(left) == exponent_summary(right),
        "same_braid_element": phi_of(left) == phi_of(right),
        "artin_images": [_images(phi_of(left)), _images(phi_of(right))],
        "same_endpoint_permutation": perm_of(left) == perm_of(right),
        "conclusion": ("the braid quotient merges two distinct literal histories with "
                       "different generator counts; this is NOT a group-semantic "
                       "counterexample when Artin rewriting is allowed, but it shows "
                       "exactly what the quotient forgets"),
    }


def witness_w3(representative_of):
    """Probe collisions: can one or a few free-group words determine the action?"""
    classes = sorted(set(representative_of.values()))
    representatives = {cls: cls for cls in classes}
    single_probe = {}
    for name in PROBE_ORDER:
        signatures = {}
        for cls in classes:
            word = representatives[cls]
            signatures.setdefault(artin_apply(word, PROBES[name]), []).append(cls)
        collisions = [v for v in signatures.values() if len(v) > 1]
        single_probe[name] = {
            "distinct_signatures": len(signatures),
            "collision_groups": len(collisions),
            "largest_collision": max((len(c) for c in collisions), default=1),
            "example_collision": ([word_text(representatives[c]) for c in collisions[0]]
                                  if collisions else None),
            "collision_words": ([word_text(representatives[c]) for c in collisions[0]]
                                if collisions else None),
        }
    full_signature = {}
    for cls in classes:
        word = representatives[cls]
        key = tuple(artin_apply(word, PROBES[name]) for name in PROBE_ORDER)
        full_signature.setdefault(key, []).append(cls)
    full_collisions = [v for v in full_signature.values() if len(v) > 1]

    # Minimal separating subfamily, by exhaustive search over subsets of the
    # frozen probe family, ordered by size then by declared probe order.
    minimal = None
    for size in range(1, len(PROBE_ORDER) + 1):
        for subset in itertools.combinations(PROBE_ORDER, size):
            seen = {}
            ok = True
            for cls in classes:
                word = representatives[cls]
                key = tuple(artin_apply(word, PROBES[name]) for name in subset)
                if key in seen:
                    ok = False
                    break
                seen[key] = cls
            if ok:
                minimal = list(subset)
                break
        if minimal is not None:
            break
    return {
        "id": "W3-probe-collision",
        "probe_family": list(PROBE_ORDER),
        "braid_classes_in_domain": len(classes),
        "single_probe": single_probe,
        "any_single_probe_separates": all(v["collision_groups"] == 0
                                          for v in single_probe.values()),
        "full_family_collision_groups": len(full_collisions),
        "full_family_example_collision": (
            [word_text(representatives[c]) for c in full_collisions[0]]
            if full_collisions else None),
        "minimal_separating_subfamily": minimal,
        "minimal_size": len(minimal) if minimal else None,
        "conclusion": ("a finite probe family is an observation, not the action; the "
                       "experiment reports exactly which collisions survive and what "
                       "a separating subfamily costs"),
    }


def _images(automorphism):
    return ["".join(_letter_text(L) for L in image) if image else "1"
            for image in automorphism]


def _letter_text(letter):
    name = "xyz"[abs(letter) - 1]
    return name if letter > 0 else name + "^-1"


# --------------------------------------------------------------------------
# negative controls
# --------------------------------------------------------------------------

def negative_controls(domain, automorphisms):
    controls = []

    def braid_relation_broken():
        broken = dict(PHI)
        broken[2] = ((1,), (2, 3, -2), (2, 1))   # wrong x3 image
        left = IDENTITY
        right = IDENTITY
        for letter in (1, 2, 1):
            left = compose(left, broken[letter])
        for letter in (2, 1, 2):
            right = compose(right, broken[letter])
        require(left == right, "EXP5-BRAID-RELATION",
                "s1 s2 s1 and s2 s1 s2 disagree under the mutated Artin action")
    controls.append({"id": "braid-relation-fails", "expected": "EXP5-BRAID-RELATION",
                     "observed": gapkit.reject(braid_relation_broken, "EXP5-BRAID-RELATION")})

    def inverse_relation_broken():
        broken = dict(PHI)
        broken[-1] = ((2,), (2, 1, 2), (3,))     # sign error in x1^{-1} image
        product = compose(broken[1], broken[-1])
        require(product == IDENTITY, "EXP5-INVERSE-RELATION",
                "phi(s1) o phi(s1^{-1}) is not the identity under the mutated action")
    controls.append({"id": "inverse-relation-fails", "expected": "EXP5-INVERSE-RELATION",
                     "observed": gapkit.reject(inverse_relation_broken, "EXP5-INVERSE-RELATION")})

    def witness_sign_flip():
        # Candidate checker claiming a flipped crossing is invisible at L2.
        require(phi_of((1, 2, 1)) == phi_of((1, -2, 1)), "EXP5-WITNESS-SIGN",
                "flipping one crossing sign did not change the braid element")
    controls.append({"id": "sign-flip", "expected": "EXP5-WITNESS-SIGN",
                     "observed": gapkit.reject(witness_sign_flip, "EXP5-WITNESS-SIGN")})

    def wrong_reduction():
        word = (1, 2, -1)
        require(free_reduce(word) == (2,), "EXP5-REDUCTION-NOT-ADJACENT",
                "non-adjacent cancellation was performed")
    controls.append({"id": "free-reduction-wrong", "expected": "EXP5-REDUCTION-NOT-ADJACENT",
                     "observed": gapkit.reject(wrong_reduction, "EXP5-REDUCTION-NOT-ADJACENT")})

    def route_disagreement():
        """Candidate checker whose composite route was mutated by one image."""
        word, probe = (1, 2), (2,)
        # Phi(w) = phi_{w1} o ... o phi_{wn}, so an incremental route must apply
        # the letters in REVERSE order to a probe.
        incremental = probe
        for letter in reversed(word):
            incremental = evaluate(PHI[letter], incremental)
        true_composite = phi_of(word)
        require(evaluate(true_composite, probe) == incremental,
                "EXP5-ROUTE-ORDER", "the honest composite disagrees with the route")
        mutated = (true_composite[0], (1,), true_composite[2])
        require(evaluate(mutated, probe) == incremental, "EXP5-ROUTE-DISAGREEMENT",
                "composite and incremental routes disagree on the mutated composite")
    controls.append({"id": "route-disagreement", "expected": "EXP5-ROUTE-DISAGREEMENT",
                     "observed": gapkit.reject(route_disagreement, "EXP5-ROUTE-DISAGREEMENT")})

    def layer_conflation():
        # Candidate checker claiming equal permutation implies equal braid.
        require(phi_of(()) == phi_of((1, 1)), "EXP5-LAYER-CONFLATION",
                "equal endpoint permutation was treated as equal braid element")
    controls.append({"id": "layer-conflation", "expected": "EXP5-LAYER-CONFLATION",
                     "observed": gapkit.reject(layer_conflation, "EXP5-LAYER-CONFLATION")})

    def enumeration_count():
        # Candidate checker run on a MUTATED alphabet with S2 dropped; the
        # declared enumeration budget must then fail loudly.
        mutated = [tuple(w) for w in gapkit.words(LETTERS[:-1], MAX_LENGTH)]
        require(len(mutated) == 5461, "EXP5-ENUMERATION-MISMATCH",
                f"declared word total is 5461, enumerated {len(mutated)}")
    controls.append({"id": "enumeration-count", "expected": "EXP5-ENUMERATION-MISMATCH",
                     "observed": gapkit.reject(enumeration_count, "EXP5-ENUMERATION-MISMATCH")})

    def mutation_detected():
        # Candidate checker claiming a single mutated letter is invisible.
        require(automorphisms[(1, 2)] == automorphisms[(1, -2)], "EXP5-WITNESS-SIGN",
                "a single crossing mutation was not detected")
    controls.append({"id": "single-crossing-mutation", "expected": "EXP5-WITNESS-SIGN",
                     "observed": gapkit.reject(mutation_detected, "EXP5-WITNESS-SIGN")})
    return controls


# --------------------------------------------------------------------------
# main
# --------------------------------------------------------------------------

def run():
    contract_sha = gapkit.sha256_file(CONTRACT)
    frozen = _read_frozen()
    require(frozen.get(CONTRACT.name) == contract_sha, "EXP-CONTRACT-DRIFT",
            f"{CONTRACT.name}: frozen {frozen.get(CONTRACT.name)!r} != {contract_sha}")

    # The declared relations are obligations, verified before any counting.
    for letter, inverse in ((1, -1), (2, -2)):
        require(compose(PHI[letter], PHI[inverse]) == IDENTITY, "EXP5-INVERSE-RELATION",
                f"phi({LETTER_NAMES[letter]}) o phi({LETTER_NAMES[inverse]}) is not the identity")
        require(compose(PHI[inverse], PHI[letter]) == IDENTITY, "EXP5-INVERSE-RELATION",
                f"phi({LETTER_NAMES[inverse]}) o phi({LETTER_NAMES[letter]}) is not the identity")
    require(phi_of((1, 2, 1)) == phi_of((2, 1, 2)), "EXP5-BRAID-RELATION",
            "s1 s2 s1 and s2 s1 s2 disagree under the declared Artin action")
    for name, automorphism in PHI.items():
        for image in automorphism:
            check_reduced(image)

    domain = enumerate_words()
    require(len(domain) == 5461, "EXP5-ENUMERATION-MISMATCH",
            f"declared word total is 5461, enumerated {len(domain)}")

    cost = gapkit.Cost()
    automorphisms = {}
    reduced = {}
    permutations = {}
    summaries = {}
    for word in domain:
        automorphisms[word] = phi_of(word)
        reduced[word] = free_reduce(word)
        permutations[word] = perm_of(word)
        summaries[word] = exponent_summary(word)
        cost.step(1)

    aut_classes = {}
    reduced_classes = {}
    perm_classes = {}
    summary_classes = {}
    for word in domain:
        aut_classes.setdefault(automorphisms[word], word)
        reduced_classes.setdefault(reduced[word], word)
        perm_classes.setdefault(permutations[word], word)
        summary_classes.setdefault(summaries[word], word)

    representative_of = {}
    for word in domain:
        representative_of[word] = aut_classes[automorphisms[word]]

    layer_table = {
        "L4_literal_words": len(domain),
        "L3_free_reduction_classes": len(reduced_classes),
        "L2_artin_automorphism_classes": len(aut_classes),
        "L1_endpoint_permutation_classes": len(perm_classes),
        "writhe_and_counts_classes": len(summary_classes),
        "literal_to_reduced_merges": len(domain) - len(reduced_classes),
        "reduced_to_braid_merges": len(reduced_classes) - len(aut_classes),
        "braid_to_permutation_merges": len(aut_classes) - len(perm_classes),
    }

    # Cost per layer, measured on the declared domain.
    layer_cost = {}
    for name, extractor in (("L4_literal", lambda w: [_letter_names(w)]),
                            ("L3_reduced", lambda w: [_letter_names(reduced[w])]),
                            ("L2_artin", lambda w: _images(automorphisms[w])),
                            ("L1_permutation", lambda w: list(permutations[w]))):
        layer = gapkit.Cost()
        for word in domain:
            layer.store(extractor(word))
            layer.step(1)
        layer_cost[name] = layer.as_record()

    witnesses = [witness_w1(), witness_w2(), witness_w3(representative_of)]

    raw_rows = []
    for word in domain:
        raw_rows.append({
            "word": _letter_names(word),
            "text": word_text(word),
            "length": len(word),
            "reduced": _letter_names(reduced[word]),
            "artin": _images(automorphisms[word]),
            "permutation": list(permutations[word]),
            "summary": list(summaries[word]),
            "braid_representative": word_text(representative_of[word]),
        })

    record = {
        "schema": SCHEMA,
        "contract": {"path": str(CONTRACT.relative_to(ROOT.parent.parent)), "sha256": contract_sha},
        "environment": gapkit.environ(),
        "native": {
            "strands": STRANDS,
            "letters": [_letter_names((L,)) for L in LETTERS],
            "time_order": "letters read left to right in time",
            "composition_order": "Phi(w . sigma) = Phi(w) o phi_sigma, (f o g)(x) = f(g(x))",
            "generator_images": {LETTER_NAMES[k]: _images(v) for k, v in sorted(PHI.items())},
            "faithfulness": ("Artin's representation B_n -> Aut(F_n) is faithful; used here, "
                             "not reproved. Faithfulness is claimed only at the braid-element "
                             "layer, never at the literal-history layer."),
        },
        "domain": {
            "size": len(domain),
            "max_length": MAX_LENGTH,
            "per_length": {str(n): len([w for w in domain if len(w) == n])
                           for n in range(MAX_LENGTH + 1)},
        },
        "layers": layer_table,
        "cost": {"enumerated_words": cost.as_record(), "per_layer": layer_cost},
        "witnesses": witnesses,
        "negative_controls": negative_controls(domain, automorphisms),
        "scope_boundary": [
            "lengths beyond 6 are not enumerated",
            "no linear, Burau, Alexander or Jones representation is used; the plan requires "
            "those under a separate contract",
            "no topological-quantum-computation claim: no anyon model, encoding space, "
            "measurement model, accuracy, or error model is supplied",
            "braid closure and Markov equivalence are not used, and braid element equality is "
            "never identified with knot equality",
        ],
    }
    return record, {"schema": SCHEMA + ".raw", "rows": raw_rows}


def _letter_names(word):
    return [LETTER_NAMES[L] for L in word]


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
    parser.add_argument("--raw", default=None)
    args = parser.parse_args()
    record, raw = run()
    text = gapkit.canonical(record)
    raw_text = gapkit.canonical(raw)
    if args.out:
        Path(args.out).write_text(text, encoding="utf-8")
        if args.raw:
            Path(args.raw).write_text(raw_text, encoding="utf-8")
        sys.stderr.write(
            f"exp5 sha256={gapkit.sha256_bytes(text.encode())} "
            f"raw_sha256={gapkit.sha256_bytes(raw_text.encode())}\n")
    else:
        sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
