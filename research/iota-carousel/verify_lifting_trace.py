#!/usr/bin/env python3
"""
Lifting 098.1(b): does Donaghey's tau leave a trace at the O(P) (dependency
poset / down-set lattice) level?  Accompanying
notes/analysis-and-calculus/46-lifting-trace-planar.md.

Note 29 already showed tau does NOT descend to the dependency poset / O(P)
(no well-defined map on poset isomorphism classes).  Here we test the *coarse*
version: are the natural poset statistics preserved by tau?

  e(P)      = number of linear extensions (legal evaluation orders)
  |O(P)|    = number of down-sets (partial evaluations)
  height(P) = longest chain
  incomp(P) = number of incomparable pairs

Result: NONE of them is tau-invariant (witnesses below).  By contrast the
*planar* corner-type (k, l) = (#LL, #RL) is tau-invariant up to swap along
every tau-orbit (Pushkarev-Byzov Cor 4.5).  So tau's invariants are strictly
planar, not poset-level.
"""

from functools import lru_cache
from itertools import combinations
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
    x = leaf
    for s in subs:
        x = Node(x, s)
    return x


def tau(t):
    if t is LEAF:
        return LEAF
    ds, bottom = right_decomp(t)
    dp = [tau(d) for d in ds]
    return left_comb(bottom, dp)


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


def desc_of(nodes):
    d = {}

    def rec(v):
        s = set()
        l, r = nodes[v]
        for c in (l, r):
            if c is not None:
                s.add(c)
                s |= rec(c)
        d[v] = s
        return s

    for v in nodes:
        rec(v)
    return d


def stats(nodes):
    d = desc_of(nodes)
    ids = list(nodes)
    m = len(ids)

    cnt = [0]

    def rec_ext(order, rem):
        if not rem:
            cnt[0] += 1
            return
        for v in rem:
            if d[v] <= set(order):
                rec_ext(order + [v], rem - {v})

    rec_ext([], set(ids))

    ds = 0
    for r in range(m + 1):
        for S in combinations(ids, r):
            S = set(S)
            if all(d[v] <= S for v in S):
                ds += 1

    roots = [v for v in ids if not any(v in d[u] for u in ids)]

    def depth(v):
        l, r = nodes[v]
        return 1 + max([depth(c) for c in (l, r) if c is not None] + [0])

    height = max((depth(v) for v in roots), default=0)

    inc = sum(1 for a, b in combinations(ids, 2) if not (a in d[b] or b in d[a]))
    return {"e": cnt[0], "O": ds, "height": height, "incomp": inc}


def corner_counts(t):
    k = l = m = n_ = 0

    def walk(node, side):
        nonlocal k, l, m, n_
        if not isinstance(node, Node):
            if side == "L":
                k += 1
            else:
                l += 1
            return
        if side == "L":
            n_ += 1
        else:
            m += 1
        walk(node.l, "L")
        walk(node.r, "R")

    if isinstance(t, Node):
        walk(t.l, "L")
        walk(t.r, "R")
    return (k, l, m, n_)


def main(out_path="/tmp/lifting.json"):
    keys = ["e", "O", "height", "incomp"]
    inv = {k: True for k in keys}
    witnesses = {}
    for n in range(4, 7):
        for T in ppcts(n):
            s1 = stats(internals(T))
            T2 = tau(T)
            s2 = stats(internals(T2))
            for k in keys:
                if s1[k] != s2[k]:
                    inv[k] = False
                    witnesses.setdefault(k, []).append(
                        {"T": repr(T), "T_tau": repr(T2), "before": s1[k], "after": s2[k]})
    # orbit check for (k,l) up to swap
    orbit_ok = True
    orbit_rows = []
    for n in range(4, 6):
        seen = set()
        for T in ppcts(n):
            if repr(T) in seen:
                continue
            ob, cur = [], T
            orbit_seen = set()
            while repr(cur) not in orbit_seen and len(ob) <= 200:
                ob.append(cur)
                orbit_seen.add(repr(cur))
                cur = tau(cur)
            for x in ob:
                seen.add(repr(x))
            types = [corner_counts(x) for x in ob]
            base = (types[0][0], types[0][1])
            sw = (base[1], base[0])
            ok = all((x[0], x[1]) in (base, sw) for x in types)
            orbit_ok &= ok
            orbit_rows.append({"n": n, "orbit_len": len(ob), "types": types,
                               "kl_up_to_swap_invariant": ok})
    ev = {"poset_statistics_tau_invariant": inv,
          "witnesses": {k: v[:2] for k, v in witnesses.items()},
          "corner_type_kl_up_to_swap_invariant_along_orbits": orbit_ok,
          "orbit_rows": orbit_rows,
          "note": "For n <= 6 (checked), no poset statistic (e, |O|, height, "
                  "incomparability) is tau-invariant; the planar corner-type (k,l) up to "
                  "swap is preserved along the checked orbits. General n is open."}
    with open(out_path, "w") as f:
        json.dump(ev, f, indent=2, sort_keys=True)
    print(json.dumps({"poset_statistics_tau_invariant": inv,
                      "corner_type_kl_up_to_swap_invariant_along_orbits": orbit_ok},
                     indent=2))
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main(*sys.argv[1:])
