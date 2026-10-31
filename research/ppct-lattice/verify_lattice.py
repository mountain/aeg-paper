#!/usr/bin/env python3
"""
Lattice attribution for plane planted cubic trees (PPCTs), accompanying
notes/analysis-and-calculus/28-ppct-lattice-attribution.md (OQ-098.2).

Two candidate lattices on PPCTs:

  (A) Tamari / rotation lattice: PPCTs (full binary trees) ordered by the
      transitive closure of the rotation  N(N(a,b),c) -> N(a,N(b,c)).
      Claim checked here: it is a lattice, but NOT distributive (witness: it
      fails the distributive law on T_4 = PPCTs with 5 leaves = 14 trees).

  (B) Birkhoff down-set lattice of the infinite binary (cubic) tree.
      By Birkhoff duality the lattice of down-sets is always distributive and
      its join-irreducibles are the principal down-sets, ordered as the poset.
      The number of down-sets with N vertices satisfies R(0)=1,
      R(N)=sum_{i=0}^{N-1} R(i)R(N-1-i), i.e. R(N)=Catalan(N); checked here.

Output: JSON with the Tamari lattice check and the Catalan count.
"""

from functools import lru_cache
import itertools
import json
import math
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
    if n == 1:
        return (LEAF,)
    out = []
    for a in range(1, n):
        b = n - a
        for L in ppcts(a):
            for R in ppcts(b):
                out.append(Node(L, R))
    return tuple(out)


def all_rotations(t):
    """Yield trees obtained from t by one right-rotation N(N(a,b),c)->N(a,N(b,c))."""
    if t is LEAF:
        return
    if isinstance(t.l, Node):
        a, b, c = t.l.l, t.l.r, t.r
        yield Node(a, Node(b, c))
    for x in all_rotations(t.l):
        yield Node(x, t.r)
    for x in all_rotations(t.r):
        yield Node(t.l, x)


def catalan(n):
    return math.comb(2 * n, n) // (n + 1)


def downset_count(max_n):
    """R(N) = number of down-sets of the infinite binary tree with N vertices."""
    r = [1]  # R(0) = 1 (empty)
    for N in range(1, max_n + 1):
        r.append(sum(r[i] * r[N - 1 - i] for i in range(N)))
    return r


def tamari_check(n_leaves):
    trees = list(ppcts(n_leaves))
    idx = {repr(t): i for i, t in enumerate(trees)}
    N = len(trees)
    reach = [[False] * N for _ in range(N)]
    for i in range(N):
        reach[i][i] = True
    for i, t in enumerate(trees):
        for u in all_rotations(t):
            j = idx[repr(u)]
            if j != i:
                reach[i][j] = True
    # transitive closure (Floyd-Warshall)
    for k in range(N):
        for i in range(N):
            if reach[i][k]:
                rk = reach[k]
                for j in range(N):
                    if rk[j]:
                        reach[i][j] = True

    def le(i, j):
        return reach[i][j]

    def meet(i, j):
        cand = [k for k in range(N) if le(k, i) and le(k, j)]
        maximal = [k for k in cand if all(le(k2, k) for k2 in cand)]
        return maximal[0] if len(maximal) == 1 else None

    def join(i, j):
        cand = [k for k in range(N) if le(i, k) and le(j, k)]
        minimal = [k for k in cand if all(le(k, k2) for k2 in cand)]
        return minimal[0] if len(minimal) == 1 else None

    is_lattice = all(meet(a, b) is not None and join(a, b) is not None
                     for a, b in itertools.combinations(range(N), 2))

    witness = None
    if is_lattice:
        for a, b, c in itertools.product(range(N), repeat=3):
            lhs, rhs = meet(a, join(b, c)), join(meet(a, b), meet(a, c))
            if lhs != rhs:
                witness = {
                    "indices": [a, b, c],
                    "trees": [repr(trees[a]), repr(trees[b]), repr(trees[c])],
                    "lhs_meet_a_join_bc": repr(trees[lhs]),
                    "rhs_join_meet_ab_meet_ac": repr(trees[rhs]),
                }
                break

    return {
        "n_leaves": n_leaves,
        "trees": N,
        "is_lattice": is_lattice,
        "distributive": witness is None,
        "witness": witness,
    }


def main(out_path="/tmp/ppct_lattice.json"):
    evidence = {}
    evidence["tamari_non_distributive"] = tamari_check(5)  # T_4: 14 trees
    evidence["downset_catalan"] = downset_count(8)
    evidence["downset_catalan_ok"] = all(
        evidence["downset_catalan"][N] == catalan(N) for N in range(1, 9)
    )
    with open(out_path, "w") as f:
        json.dump(evidence, f, indent=2, sort_keys=True)
    print(json.dumps({
        "tamari_is_lattice": evidence["tamari_non_distributive"]["is_lattice"],
        "tamari_distributive": evidence["tamari_non_distributive"]["distributive"],
        "downset_catalan_ok": evidence["downset_catalan_ok"],
    }, indent=2))
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main(*sys.argv[1:])
