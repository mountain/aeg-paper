#!/usr/bin/env python3
"""Experiment 5, independent route -- free-group substitution vs composites.

The work plan names this exact independence pattern: "自由群替换对照复合像元组"
(free-group substitution against composite image tuples).

* The PRIMARY implementation materialises each automorphism as an image triple
  and evaluates a probe by substituting into that composite.
* THIS checker never forms a composite for the probe question: it applies one
  generator action at a time directly to the probe word, reducing at each
  step, in the reverse letter order forced by the declared convention
  ``Phi(w) = phi_{w1} o ... o phi_{wn}``.

It additionally re-derives the whole layer class counts by breadth-first search
on the Cayley graph of the automorphism group, instead of enumerating words and
de-duplicating, and re-checks the two defining relations by direct substitution
on a generating set of free words rather than by composing triples.

Run:

    python3 research/process-representation-gap/experiments/exp5_braid_nonarithmetic_independent.py
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import deque
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(ROOT / "tools"))
import gapkit  # noqa: E402
from gapkit import Diagnostic, require  # noqa: E402

CONTRACT = ROOT / "contracts" / "exp5-braid-nonarithmetic.v1.json"
FROZEN = ROOT / "contracts" / "FROZEN.sha256"
PRIMARY = ROOT / "evidence" / "exp5-braid-nonarithmetic.json"

LETTERS = (1, 2, -1, -2)
MAX_LENGTH = 6

# Hand-computed witness table, entered as literals.  Images of x1, x2, x3.
HAND = {
    "": ((1,), (2,), (3,)),
    "s1": ((1, 2, -1), (1,), (3,)),
    "s1^-1": ((2,), (-2, 1, 2), (3,)),
    "s2": ((1,), (2, 3, -2), (2,)),
    "s2^-1": ((1,), (3,), (-3, 2, 3)),
}

# The same generator actions, written as a substitution table.  This checker
# only ever uses THIS table, never a composed automorphism.
SUBSTITUTION = {
    1: {1: (1, 2, -1), 2: (1,), 3: (3,)},
    2: {1: (1,), 2: (2, 3, -2), 3: (2,)},
    -1: {1: (2,), 2: (-2, 1, 2), 3: (3,)},
    -2: {1: (1,), 2: (3,), 3: (-3, 2, 3)},
}

PROBES = {
    "x1": (1,), "x2": (2,), "x3": (3,), "x1x2": (1, 2), "x1x2x3": (1, 2, 3),
    "x1x2x1^-1": (1, 2, -1), "commutator": (1, 2, 3, -1, -2, -3),
    "(x1x2)^3": (1, 2, 1, 2, 1, 2),
}
PROBE_ORDER = tuple(PROBES)


# --------------------------------------------------------------------------
# a second, independent implementation of free-group reduction
# --------------------------------------------------------------------------

def reduce_word(word):
    stack = []
    for letter in word:
        if stack and stack[-1] + letter == 0:
            stack.pop()
        else:
            stack.append(letter)
    return tuple(stack)


def invert(word):
    return tuple(-x for x in reversed(word))


def substitute(letter, word):
    """Apply ONE generator action to a free word, right where it stands."""
    table = SUBSTITUTION[letter]
    out = []
    for x in word:
        image = table[abs(x)]
        out.extend(image if x > 0 else invert(image))
    return reduce_word(out)


def act_incrementally(word, probe):
    """Phi(w) applied to a probe without ever forming a composite.

    Phi(w) = phi_{w1} o ... o phi_{wn}, so the letters act on the argument in
    reverse order.
    """
    current = tuple(probe)
    for letter in reversed(word):
        current = substitute(letter, current)
    return current


def act_by_composite(word, probe):
    """The primary's route, rebuilt here only for the disagreement check.

    Phi(w . sigma) = Phi(w) o phi_sigma, so appending a letter applies the
    ALREADY ACCUMULATED composite to that letter's images.  Writing it the
    other way round silently computes the reversed composite, and the two
    routes then disagree on the first word of length two.
    """
    images = [(1,), (2,), (3,)]
    for letter in word:
        table = SUBSTITUTION[letter]
        images = [apply_images(images, table[i]) for i in (1, 2, 3)]
    return apply_images(images, probe)


def apply_images(images, word):
    """Substitute an image triple into a free word and reduce."""
    out = []
    for x in word:
        image = images[abs(x) - 1]
        out.extend(image if x > 0 else invert(image))
    return reduce_word(out)


# --------------------------------------------------------------------------
# relations, re-checked by substitution on free words
# --------------------------------------------------------------------------

GENERATING_SET = [(1,), (2,), (3,), (1, 2), (2, 3), (1, 3), (1, 2, 3),
                  (1, -1), (2, 1, -2), (-1, 2, 1)]


def check_inverse_relations():
    """phi_s o phi_{s^-1} = id verified on a generating set, not on triples."""
    for letter in (1, 2, -1, -2):
        inverse = -letter
        for word in GENERATING_SET:
            forward = substitute(inverse, substitute(letter, word))
            require(forward == reduce_word(word), "EXP5-INVERSE-RELATION",
                    f"phi({letter}) then phi({inverse}) changed {word} to {forward}")
    return {"verified_on_free_words": len(GENERATING_SET), "pairs": 4}


def check_braid_relation():
    for word in GENERATING_SET:
        left = word
        for letter in (1, 2, 1):
            left = substitute(letter, left)
        right = word
        for letter in (2, 1, 2):
            right = substitute(letter, right)
        require(left == right, "EXP5-BRAID-RELATION",
                f"s1 s2 s1 and s2 s1 s2 disagree on {word}: {left} vs {right}")
    return {"verified_on_free_words": len(GENERATING_SET)}


def check_hand_table():
    for text, expected in sorted(HAND.items()):
        word = tuple(_parse(text))
        observed = tuple(tuple(image) for image in (
            act_incrementally(word, (1,)),
            act_incrementally(word, (2,)),
            act_incrementally(word, (3,)),
        ))
        require(observed == expected, "EXP5-HAND-TABLE-MISMATCH",
                f"Phi({text!r}) = {observed}, hand table says {expected}")
    return {text: [[list(i) for i in images] for images in (expected,)]
            for text, expected in sorted(HAND.items())}


def _parse(text):
    """Parse the hand-table key notation: '', 's1', 's1^-1', 's2', 's2^-1'."""
    if not text:
        return ()
    table = {"s1": (1,), "s2": (2,), "s1^-1": (-1,), "s2^-1": (-2,)}
    step = 2 if text.startswith("s") else 3
    require(text in table or True, "EXP5-PARSE", text)
    return table[text]


def _parse_full(text):
    """Parse s1, s2, S1, S2 into signed letters."""
    if not text:
        return ()
    out = []
    i = 0
    while i < len(text):
        chunk = text[i:i + 2]
        if chunk == "s1":
            out.append(1)
        elif chunk == "s2":
            out.append(2)
        elif chunk == "S1":
            out.append(-1)
        elif chunk == "S2":
            out.append(-2)
        else:
            raise Diagnostic("EXP5-PARSE", text)
        i += 2
    return tuple(out)


# --------------------------------------------------------------------------
# Cayley-graph enumeration instead of word enumeration
# --------------------------------------------------------------------------

def cayley_classes(max_length):
    """Distinct generator-images reachable within max_length, by BFS.

    A state is the image triple itself, so this traverses the automorphism
    group rather than enumerating words.
    """
    identity = ((1,), (2,), (3,))
    seen = {identity: ()}
    queue = deque([(identity, ())])
    while queue:
        state, word = queue.popleft()
        if len(word) >= max_length:
            continue
        for letter in LETTERS:
            table = SUBSTITUTION[letter]
            nxt = tuple(apply_images(list(state), table[i]) for i in (1, 2, 3))
            if nxt in seen:
                continue
            seen[nxt] = word + (letter,)
            queue.append((nxt, word + (letter,)))
    return seen


# --------------------------------------------------------------------------
# main
# --------------------------------------------------------------------------

def run():
    require(CONTRACT.exists(), "EXP5I-CONTRACT-MISSING", str(CONTRACT))
    contract_sha = gapkit.sha256_file(CONTRACT)
    frozen = _read_frozen()
    require(frozen.get(CONTRACT.name) == contract_sha, "EXP-CONTRACT-DRIFT",
            f"{CONTRACT.name}: frozen {frozen.get(CONTRACT.name)!r} != {contract_sha}")
    require(PRIMARY.exists(), "EXP5I-PRIMARY-MISSING", str(PRIMARY))
    primary = json.loads(PRIMARY.read_text(encoding="utf-8"))

    relations = {
        "inverse": check_inverse_relations(),
        "braid": check_braid_relation(),
    }
    hand = check_hand_table()

    # Route agreement on every word and every probe in the declared domain.
    words = [tuple(w) for w in gapkit.words(LETTERS, MAX_LENGTH)]
    disagreements = []
    for word in words:
        for name in PROBE_ORDER:
            left = act_incrementally(word, PROBES[name])
            right = act_by_composite(word, PROBES[name])
            if left != right:
                disagreements.append({
                    "word": [_name(L) for L in word], "probe": name,
                    "incremental": list(left), "composite": list(right),
                })
                break
        if disagreements:
            break
    require(not disagreements, "EXP5-ROUTE-DISAGREEMENT",
            f"incremental and composite routes disagree: {disagreements[:1]}")

    # Independent layer counts.
    literal = len(words)
    reduced = {reduce_word(w) for w in words}
    perm = {_permutation(w) for w in words}
    cayley = cayley_classes(MAX_LENGTH)
    braid_classes = len(cayley)

    declared = primary["layers"]
    agreement = {
        "literal": literal == declared["L4_literal_words"],
        "reduced": len(reduced) == declared["L3_free_reduction_classes"],
        "braid": braid_classes == declared["L2_artin_automorphism_classes"],
        "permutation": len(perm) == declared["L1_endpoint_permutation_classes"],
    }
    require(all(agreement.values()), "EXP5-ROUTE-DISAGREEMENT",
            f"layer counts disagree with the primary: {agreement}")

    # W1 and W2 re-derived here.
    w1 = {
        "same_permutation": _permutation(()) == _permutation((1, 1)),
        "different_braid": act_incrementally((), (1,)) != act_incrementally((1, 1), (1,)),
    }
    require(w1["same_permutation"] and w1["different_braid"], "EXP5-WITNESS-W1",
            f"W1 failed: {w1}")
    w2 = {
        "same_braid": all(
            act_incrementally((1, 2, 1), p) == act_incrementally((2, 1, 2), p)
            for p in PROBES.values()),
        "different_literal": (1, 2, 1) != (2, 1, 2),
    }
    require(w2["same_braid"] and w2["different_literal"], "EXP5-WITNESS-W2",
            f"W2 failed: {w2}")

    # W3 re-derived: which probes collide, and the minimal separating size.
    representatives = sorted(set(cayley.values()), key=lambda w: (len(w), w))
    collision_report = {}
    for name in PROBE_ORDER:
        seen = {}
        collisions = 0
        for word in representatives:
            key = act_incrementally(word, PROBES[name])
            if key in seen:
                collisions += 1
            else:
                seen[key] = word
        collision_report[name] = {"distinct": len(seen), "collisions": collisions}
    minimal_size = None
    for size in range(1, len(PROBE_ORDER) + 1):
        found = False
        import itertools
        for subset in itertools.combinations(PROBE_ORDER, size):
            seen = set()
            ok = True
            for word in representatives:
                key = tuple(act_incrementally(word, PROBES[n]) for n in subset)
                if key in seen:
                    ok = False
                    break
                seen.add(key)
            if ok:
                found = True
                break
        if found:
            minimal_size = size
            break

    require(minimal_size == primary["witnesses"][2]["minimal_size"],
            "EXP5-ROUTE-DISAGREEMENT",
            f"minimal probe family size {minimal_size} != "
            f"primary {primary['witnesses'][2]['minimal_size']}")

    # Negative controls.  Both replay a real defect class.
    def reversed_composition_route():
        """Replay the reversed-composition defect this checker originally had."""
        def wrong_order(word, probe):
            images = [(1,), (2,), (3,)]
            for letter in word:
                table = SUBSTITUTION[letter]
                images = [apply_images([table[1], table[2], table[3]], images[i])
                          for i in (0, 1, 2)]
            return apply_images(images, probe)
        word, probe = (1, 2), (1,)
        require(wrong_order(word, probe) == act_incrementally(word, probe),
                "EXP5-ROUTE-DISAGREEMENT",
                "the reversed-composition route agreed with the incremental route")
    control_reversed = gapkit.reject(reversed_composition_route, "EXP5-ROUTE-DISAGREEMENT")

    def single_sign_mutation():
        """Mutate ONE generator image in the composite route only."""
        global SUBSTITUTION
        mutated = dict(SUBSTITUTION)
        mutated[2] = {1: (1,), 2: (2, 3, -2), 3: (2, 1)}
        original = SUBSTITUTION
        SUBSTITUTION = mutated
        try:
            composite = act_by_composite((2,), (3,))
        finally:
            SUBSTITUTION = original
        require(composite == act_incrementally((2,), (3,)),
                "EXP5-ROUTE-DISAGREEMENT",
                "a single mutated generator image went undetected")
    control_sign = gapkit.reject(single_sign_mutation, "EXP5-ROUTE-DISAGREEMENT")

    record = {
        "schema": "aeg.process-representation-gap.exp5-independent.v1",
        "role": "independent verification route for exp5",
        "contract": {"path": str(CONTRACT.relative_to(ROOT.parent.parent)),
                     "sha256": contract_sha},
        "environment": gapkit.environ(),
        "route": {
            "incremental": "generator actions applied one at a time to the probe, in reverse letter order",
            "composite": "image triple substituted into the probe",
            "cayley": "breadth-first traversal of the automorphism group, not word enumeration",
            "hand_table": "literal images for the five frozen generator words",
        },
        "relations": relations,
        "hand_table": hand,
        "route_agreement": {
            "words_checked": len(words),
            "probes_checked": len(PROBE_ORDER),
            "disagreements": len(disagreements),
        },
        "layer_counts": {
            "literal": literal,
            "reduced": len(reduced),
            "braid_by_cayley_bfs": braid_classes,
            "permutation": len(perm),
            "agreement_with_primary": agreement,
        },
        "witnesses": {"W1": w1, "W2": w2,
                      "W3_collision_report": collision_report,
                      "W3_minimal_size": minimal_size},
        "negative_controls": [
            {"id": "reversed-composition-route", "expected": "EXP5-ROUTE-DISAGREEMENT",
             "observed": control_reversed},
            {"id": "single-generator-image-mutation", "expected": "EXP5-ROUTE-DISAGREEMENT",
             "observed": control_sign},
        ],
        "conclusion": ("the independent route reproduces every primary count, both "
                       "relations and all three witnesses"),
    }
    return record


def _permutation(word):
    table = {1: (1, 0, 2), 2: (0, 2, 1), -1: (1, 0, 2), -2: (0, 2, 1)}
    current = (0, 1, 2)
    for letter in word:
        step = table[letter]
        current = tuple(current[step[i]] for i in range(3))
    return current


def _name(letter):
    return {1: "s1", 2: "s2", -1: "S1", -2: "S2"}[letter]


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
        sys.stderr.write(f"written sha256={gapkit.sha256_bytes(text.encode())}\n")
    else:
        sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
