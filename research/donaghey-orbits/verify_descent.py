#!/usr/bin/env python3
"""
Check whether Donaghey's tau descends to the dependency-poset layer (AEG's
"branching layer"), accompanying
notes/analysis-and-calculus/29-branching-layer-descent.md (OQ-098.1(b)).

AEG's dependency poset (def:internal-dependency-poset): for internal vertices
u, v of a binary expression tree, u <= v iff u is a descendant of v (equivalently
v lies on the path from u to the root).  For a full binary tree this poset is the
"internal skeleton": the rooted tree on internal vertices, children below parents.
Two trees have isomorphic dependency posets iff their internal skeletons are
isomorphic as unordered rooted trees.

Question: does tau respect this equivalence, i.e. does it factor through the
dependency poset (hence through O(P))?

The script computes, for each n, whether every skeleton class has a unique
tau-image.  If some class has two different tau-images, tau does NOT descend.
"""

from functools import lru_cache
from collections import defaultdict
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
    ds, cur = [], t
    while isinstance(cur, Node):
        ds.append(cur.l)
        cur = cur.r
    return ds, cur


def left_comb(leaf, subs):
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


def skeleton(t):
    """Canonical form of the dependency poset = unordered rooted internal skeleton."""
    if t is LEAF:
        return None
    kids = [skeleton(t.l), skeleton(t.r)]
    return tuple(sorted(k for k in kids if k is not None))


def descent_check(n):
    trees = list(ppcts(n))
    groups = defaultdict(list)
    for t in trees:
        groups[skeleton(t)].append(t)
    bad = {}
    for sk, grp in groups.items():
        imgs = {skeleton(tau(t)) for t in grp}
        if len(imgs) > 1:
            bad[sk] = {
                "images": [repr(i) for i in sorted(imgs)],
                "witness": repr(grp[0]),
            }
    return {
        "n_leaves": n,
        "trees": len(trees),
        "skeleton_classes": len(groups),
        "classes_not_single_image": len(bad),
        "descends": len(bad) == 0,
        "bad": {repr(k): v for k, v in bad.items()},
    }


def main(out_path="/tmp/descent.json"):
    evidence = {}
    for n in range(3, 9):
        evidence[str(n)] = descent_check(n)
    evidence["summary"] = {
        "descends": all(v["descends"] for k, v in evidence.items() if k.isdigit()),
        "comment": "tau does not factor through the dependency poset / O(P) "
                   "for n >= 4; see note 29 / OQ-098.1(b).",
    }
    with open(out_path, "w") as f:
        json.dump(evidence, f, indent=2, sort_keys=True)
    print(json.dumps({
        "descends": evidence["summary"]["descends"],
        "per_n": {k: evidence[k]["classes_not_single_image"]
                  for k in evidence if k.isdigit()},
    }, indent=2))
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main(*sys.argv[1:])
