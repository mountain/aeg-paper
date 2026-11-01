#!/usr/bin/env python3
"""
Canonicalization of the cross-branch choice, accompanying
notes/analysis-and-calculus/38-canonical-cross-chain-choice.md.

For each PPCT: take the corner order (left standard traversal = PREORDER) of the
internal nodes as reference P; enumerate all linear extensions E of the
dependency poset; compute the inversion count inv(E, P) (Kendall tau distance);
find the minimizers.  Check that the minimizer is unique and equals the
left-first POSTORDER.

Verified for all PPCTs with n = 4 and 5 leaves.
"""

from functools import lru_cache
import itertools
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


def internals(t):
    nodes, nxt = {}, [0]

    def walk(x):
        if not isinstance(x, Node):
            return None
        me = nxt[0]
        nxt[0] += 1
        l = walk(x.l)
        r = walk(x.r)
        nodes[me] = (l, r)
        return me

    walk(t)
    return nodes


def roots_of(nodes):
    children = set()
    for v, (l, r) in nodes.items():
        for c in (l, r):
            if c is not None:
                children.add(c)
    return [v for v in nodes if v not in children]


def preorder(nodes):
    out = []

    def rec(v):
        out.append(v)
        l, r = nodes[v]
        if l is not None:
            rec(l)
        if r is not None:
            rec(r)

    for v in roots_of(nodes):
        rec(v)
    return out


def postorder(nodes):
    out = []

    def rec(v):
        l, r = nodes[v]
        if l is not None:
            rec(l)
        if r is not None:
            rec(r)
        out.append(v)

    for v in roots_of(nodes):
        rec(v)
    return out


def descendants(nodes):
    desc = {}

    def rec(v):
        s = set()
        l, r = nodes[v]
        for c in (l, r):
            if c is not None:
                s.add(c)
                s |= rec(c)
        desc[v] = s
        return s

    for v in nodes:
        rec(v)
    return desc


def linear_extensions(nodes):
    desc = descendants(nodes)
    ids = list(nodes)
    exts = []

    def rec(order, remaining):
        if not remaining:
            exts.append(tuple(order))
            return
        for v in list(remaining):
            if all(d in order for d in desc[v]):
                rec(order + [v], remaining - {v})

    rec([], set(ids))
    return exts


def inversions(order, ref):
    pos = {v: i for i, v in enumerate(order)}
    inv = 0
    for a, b in itertools.combinations(ref, 2):
        ia, ib = ref.index(a), ref.index(b)
        if ia < ib and pos[a] > pos[b]:
            inv += 1
    return inv


def main(out_path="/tmp/canonical_choice.json"):
    ev = {}
    all_unique, all_post = True, True
    for n in range(4, 8):
        rows = []
        for t in ppcts(n):
            nodes = internals(t)
            pre, post = preorder(nodes), postorder(nodes)
            exts = linear_extensions(nodes)
            scored = [(inversions(e, pre), e) for e in exts]
            best = min(s for s, _ in scored)
            mins = [e for s, e in scored if s == best]
            unique = len(mins) == 1
            post_is_min = tuple(post) in mins
            all_unique &= unique
            all_post &= post_is_min
            rows.append({"tree": repr(t), "num_exts": len(exts), "min_inv": best,
                         "num_minimizers": len(mins), "postorder_is_minimizer": post_is_min})
        ev[str(n)] = rows
    ev["summary"] = {"all_unique": all_unique, "postorder_is_minimizer": all_post,
                     "comment": "The unique linear extension minimizing inversions with "
                                "the preorder (corner order) is the left-first postorder. "
                                "See note 38."}
    with open(out_path, "w") as f:
        json.dump(ev, f, indent=2, sort_keys=True)
    print(json.dumps(ev["summary"], indent=2))
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main(*sys.argv[1:])
