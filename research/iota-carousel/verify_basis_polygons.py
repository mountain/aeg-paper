#!/usr/bin/env python3
"""Groups and polygons attached to one-point bases.

Two computations:

1. Carrier reading.  The iota carrier's complex unit J has order four, so the
   minimal group it defines is Z/4; its quotient block is a cone of angle pi/2.
   Together with the negative-inverse involution the pair generates
   C2 * C4 = the (2,4,infty) triangle group, whose fundamental polygon is the
   ideal hyperbolic triangle with angles (pi/2, pi/4, 0).

2. Word reading.  Reading a closed term's body as the frontier word of its
   application tree, the one-relator group presented by the word is computed by
   a Tietze elimination for the iota term, Fokker's term and Rosser's term.
   All three collapse to the free group of rank two (the pair of pants).

Run: python3 verify_basis_polygons.py [out.json]
"""
import json
import math
import sys


def eliminate(gens, word):
    """Tietze: one generator occurring exactly once with exponent +1 is solved for.

    Solving for it absorbs the relation, so the presentation becomes free on the
    remaining generators; the loop must not continue eliminating them.
    """
    gens = list(gens)
    counts = {}
    for g, e in word:
        counts[g] = counts.get(g, 0) + 1
    for g in gens:
        if counts.get(g, 0) == 1:
            gens.remove(g)
            return {"rank": len(gens), "generators": gens, "eliminated": [g],
                    "remaining_word": []}
    return {"rank": len(gens), "generators": gens, "eliminated": [],
            "remaining_word": [list(w) for w in word]}


def frontier_word(term):
    """Leaves of the application tree, left to right; a leaf is a generator name."""
    if isinstance(term, str):
        return [term]
    left, right = term
    return frontier_word(left) + frontier_word(right)


# bodies as binary application trees, leaves are generator names
BODIES = {
    "iota (lambda x. x S K)": (("x", "S"), "K"),
    "fokker (lambda f. f S (lambda xyz.x))": (("f", "S"), "Q"),
    "rosser (lambda f. f K S K)": ((("f", "K"), "S"), "K"),
}

def main(out_path="/tmp/basis-polygons.json"):
    word_rows = {}
    for name, body in BODIES.items():
        w = frontier_word(body)
        gens = sorted(set(w))
        row = eliminate(gens, [(g, 1) for g in w])
        row["word"] = w
        word_rows[name] = row
    # carrier data
    # Z/4: cone of angle 2*pi/4
    cone_angle = 2 * math.pi / 4
    # C2 * C4 = (2,4,infty): angles pi/2, pi/4, 0
    A, B, C = math.pi / 2, math.pi / 4, 0.0
    # cosh c = (cos A cos B + cos C) / (sin A sin B), c opposite C
    cosh_c = (math.cos(A) * math.cos(B) + math.cos(C)) / (math.sin(A) * math.sin(B))
    side_c = math.acosh(cosh_c)
    area = math.pi - (A + B + C)
    ev = {
        "carrier": {
            "minimal_group": "Z/4",
            "cone_angle": cone_angle,
            "triangle_group": "C2 * C4 = (2,4,infinity)",
            "triangle_angles": [A, B, C],
            "finite_side_arcosh_sqrt2": side_c,
            "area": area,
            "note": "Z/4 is the group of the complex unit J; with the "
                    "negative-inverse involution the pair gives the (2,4,infinity) "
                    "triangle group. The iota -> carrier step is a proposal, the "
                    "triangle group and its polygon are classical.",
        },
        "word_reading": word_rows,
        "note": "Under the frontier-word proposal all three one-point bases give the "
                "free group of rank two, i.e. the pair of pants; the word reading does "
                "not distinguish the bases. See the note's section 10.",
    }
    with open(out_path, "w") as f:
        json.dump(ev, f, indent=2, sort_keys=True)
    print(json.dumps({"groups": {k: v["rank"] for k, v in word_rows.items()},
                      "carrier_area": area, "side": side_c}, indent=2))
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main(*sys.argv[1:])
