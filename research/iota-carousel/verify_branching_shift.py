#!/usr/bin/env python3
"""
Branching-layer S: the left-first POSTORDER of internal nodes is a linear
extension of the dependency poset, and equals the chronological order for both
left and right combs.  Accompanying
notes/analysis-and-calculus/36-branching-layer-shift.md.

Dependency poset (def:internal-dependency-poset): u <= v iff u is a descendant of
v.  A linear extension must place descendants before ancestors (children before
parents) -- that is exactly what the left-first postorder does.

Also reports the left-first PREorder (which is NOT a linear extension) to make
the preorder/postorder distinction of note 36 explicit.
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


def is_linear_extension(order, nodes):
    pos = {v: i for i, v in enumerate(order)}
    desc = descendants(nodes)
    return all(pos[u] < pos[v] for v in nodes for u in desc[v])


def main(out_path="/tmp/branching_shift.json"):
    ev = {"postorder_is_linear_extension": {}, "preorder_is_linear_extension": {},
          "comb_checks": {}}
    all_po = True
    all_pre = True
    for n in range(3, 6):
        ok_po, ok_pre = True, True
        for t in ppcts(n):
            nodes = internals(t)
            if not is_linear_extension(postorder(nodes), nodes):
                ok_po = False
            if not is_linear_extension(preorder(nodes), nodes):
                ok_pre = False
        ev["postorder_is_linear_extension"][str(n)] = ok_po
        ev["preorder_is_linear_extension"][str(n)] = ok_pre
        all_po &= ok_po
        all_pre &= ok_pre

    left_comb = Node(Node(Node(LEAF, LEAF), LEAF), LEAF)
    right_comb = Node(LEAF, Node(LEAF, Node(LEAF, LEAF)))
    for name, t in (("left_comb", left_comb), ("right_comb", right_comb)):
        nodes = internals(t)
        ev["comb_checks"][name] = {
            "tree": repr(t),
            "postorder": postorder(nodes),
            "preorder": preorder(nodes),
            "postorder_equals_chronological": postorder(nodes) == sorted(nodes, reverse=True),
        }

    ev["summary"] = {
        "postorder_all_linear_extensions": all_po,
        "preorder_is_linear_extension": all_pre,
        "comment": "left-first postorder is a linear extension (all n<=5); preorder is "
                   "not (root first). For both combs the postorder is the chronological "
                   "order [2,1,0]. S = postorder successor. See note 36.",
    }
    with open(out_path, "w") as f:
        json.dump(ev, f, indent=2, sort_keys=True)
    print(json.dumps({"summary": ev["summary"],
                      "comb_checks": ev["comb_checks"]}, indent=2))
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main(*sys.argv[1:])
