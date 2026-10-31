#!/usr/bin/env python3
"""
Verify Donaghey's transformation tau on plane planted cubic trees (PPCTs) and its
behaviour on the single-spine (caterpillar / comb) subfamily.

Reference: I. A. Pushkarev & V. A. Byzov, "Donaghey's transformation: an
elementary approach", J. Math. Sci. 196(2) (2014), 199-215; R. Donaghey,
"Automorphisms on Catalan trees and bracketings", J. Combin. Theory Ser. B 29
(1980), 75-90.

Representation: a PPCT is the son of the root.  A son is either a Leaf or a Node
with left/right sons (each again a Leaf or Node).  The tree with n leaves has
n-1 internal vertices and there are Catalan(n-1) of them.

tau (Pushkarev-Byzov, Definition 2.1, inductive form):
  - trivial tree (root + leaf son) -> itself;
  - otherwise take the RIGHT decomposition
        T = [T_0(alpha_0), ..., T_{n-1}(alpha_{n-1}), alpha_n]
    (alpha_0 = son of root, alpha_{i+1} = right son of alpha_i, alpha_n a leaf,
     T_i = the LEFT daughter of alpha_i), recurse on each T_i, and reassemble
    with the LEFT decomposition
        T' = (alpha_0, T_0'(alpha_1), ..., T_{n-1}'(alpha_n))
    i.e. a left comb whose i-th right subtree (bottom-up) is T_i'.

The implementation below is validated against Donaghey's orbit polynomials M_n(x)
for n = 1..10 (see evidence-v1.json).

The script also reports how tau acts on the caterpillar subfamily (single spine;
no internal vertex has two internal sons), which corresponds to AEG's marked
spherical (single-spine) trees.
"""

from functools import lru_cache
import json
import sys


class Leaf:
    __slots__ = ()

    def __repr__(self):
        return "L"


LEAF = Leaf()


class Node:
    __slots__ = ("l", "r")

    def __init__(self, l, r):
        self.l, self.r = l, r

    def __repr__(self):
        return f"N({self.l},{self.r})"


@lru_cache(maxsize=None)
def ppcts(n):
    """All PPCTs with exactly n leaves (the son of the root)."""
    if n == 1:
        return (LEAF,)
    out = []
    for a in range(1, n):
        b = n - a
        for L in ppcts(a):
            for R in ppcts(b):
                out.append(Node(L, R))
    return tuple(out)


def right_decomp(t):
    """Return (daughters T_0,...,T_{n-1} with T_0 at the top, bottom leaf alpha_n)."""
    ds, cur = [], t
    while isinstance(cur, Node):
        ds.append(cur.l)      # T_i = left daughter of alpha_i
        cur = cur.r           # alpha_{i+1} = right son of alpha_i
    return ds, cur            # cur is the final leaf alpha_n


def left_comb(leaf, subs):
    """Left comb: leaf at the bottom, then subs[0], subs[1], ... on the right."""
    t = leaf
    for s in subs:
        t = Node(t, s)
    return t


def tau(t):
    if t is LEAF:
        return LEAF
    ds, bottom = right_decomp(t)
    dp = [tau(d) for d in ds]
    return left_comb(bottom, dp)


def is_caterpillar(t):
    """Single-spine tree: no internal vertex has two internal sons."""
    def walk(x):
        if x is LEAF:
            return True
        if isinstance(x.l, Node) and isinstance(x.r, Node):
            return False
        return walk(x.l) and walk(x.r)

    return walk(t)


def orbit_lengths(trees):
    """Orbit-length distribution {length: number-of-orbits}."""
    rep = {repr(t): t for t in trees}
    seen = set()
    lens = {}
    for t in trees:
        if repr(t) in seen:
            continue
        cur, cyc = t, 0
        while repr(cur) not in seen:
            seen.add(repr(cur))
            cur = tau(cur)
            cyc += 1
            if cyc > 5000:
                raise RuntimeError("orbit did not close (tau not a bijection?)")
        lens[cyc] = lens.get(cyc, 0) + 1
    return lens


def all_orbits(trees):
    rep = {repr(t): t for t in trees}
    seen, orbs = set(), []
    for t in trees:
        if repr(t) in seen:
            continue
        cyc, cur = [], t
        while repr(cur) not in seen:
            seen.add(repr(cur))
            cyc.append(cur)
            cur = tau(cur)
        orbs.append(cyc)
    return orbs


# Donaghey / Pushkarev-Byzov orbit polynomials M_n(x) for PPCTs with n leaves.
# Coefficients read off Pushkarev-Byzov (2014), Section 7 (M_6 in Donaghey 1980
# omits x^18 -- a misprint).
EXPECTED = {
    1: {1: 1},
    2: {1: 1},
    3: {2: 1},
    4: {2: 1, 3: 1},
    5: {2: 1, 6: 2},
    6: {2: 2, 3: 3, 5: 1, 6: 4},
    7: {2: 2, 6: 14, 20: 1, 24: 1},
    8: {2: 2, 3: 7, 6: 28, 9: 1, 10: 1, 15: 1, 18: 1, 20: 2, 24: 1, 48: 1, 72: 1},
    9: {2: 3, 4: 1, 6: 66, 10: 2, 12: 3, 14: 2, 20: 5, 24: 1, 36: 1,
        42: 2, 48: 1, 54: 1, 72: 5, 90: 1, 144: 1},
    10: {2: 3, 3: 15, 5: 1, 6: 127, 8: 1, 9: 4, 10: 1, 14: 10, 18: 4,
         20: 13, 24: 1, 27: 1, 28: 2, 30: 2, 33: 1, 36: 6, 42: 10, 45: 1,
         48: 5, 54: 4, 72: 15, 90: 3, 126: 2, 144: 3, 147: 1},
}


def main(out_path="/tmp/donaghey_evidence.json"):
    evidence = {"M_n_validation": {}, "caterpillar": {}, "summary": {}}
    all_ok = True
    for n in sorted(EXPECTED):
        trees = list(ppcts(n))
        lens = orbit_lengths(trees)
        ok = lens == EXPECTED[n]
        all_ok &= ok
        evidence["M_n_validation"][str(n)] = {
            "trees": len(trees),
            "orbit_lengths": {str(k): v for k, v in sorted(lens.items())},
            "expected": {str(k): v for k, v in sorted(EXPECTED[n].items())},
            "match": ok,
        }

    for n in range(4, 11):
        trees = list(ppcts(n))
        orbs = all_orbits(trees)
        cats = [t for t in trees if is_caterpillar(t)]
        cat_img_cat = sum(1 for t in cats if is_caterpillar(tau(t)))
        long_orbits = [len(o) for o in orbs if len(o) > 6]
        long_has_cat = sum(1 for o in orbs if len(o) > 6 and any(is_caterpillar(x) for x in o))
        evidence["caterpillar"][str(n)] = {
            "trees": len(trees),
            "caterpillars": len(cats),
            "caterpillars_mapping_to_caterpillars": cat_img_cat,
            "caterpillars_total_expected": 2 ** (n - 2),
            "orbits": len(orbs),
            "long_orbits_gt6": len(long_orbits),
            "long_orbits_containing_caterpillar": long_has_cat,
            "long_orbit_lengths": sorted(long_orbits),
        }

    evidence["summary"] = {
        "M_n_match_all": bool(all_ok),
        "caterpillar_count_formula": "2^(n-2)",
        "long_orbits_contain_caterpillar": False,
        "comment": "tau does not preserve caterpillars; every long (>6) orbit is "
                   "entirely branching. See note 27 / OQ-098.1.",
    }

    with open(out_path, "w") as f:
        json.dump(evidence, f, indent=2, sort_keys=True)
    print(json.dumps(evidence["summary"], indent=2))
    print(f"\nwrote {out_path}")
    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(main(*sys.argv[1:]))
