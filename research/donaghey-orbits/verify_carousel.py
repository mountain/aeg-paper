#!/usr/bin/env python3
"""
Carousel count-shadow verification, accompanying
notes/analysis-and-calculus/31-carousel-and-iota.md (carousel <-> iota).

Pushkarev-Byzov (2014), Corollary 4.4: for a PPCT T with n leaves, let
  k = # left leaves,  l = # right leaves,  m = # right non-leaves,
  n_ = # left non-leaves;
then k = m+1, l = n_+1, and under Donaghey's tau
  (k',l',m',n_') = (n_+1, k, l-1, m).

The script:
  1. builds PPCTs, computes (k,l,m,n_) and tau, and checks the formula
     for all trees up to n leaves = 7;
  2. reports the order of the induced map M on the constrained quadruple;
  3. records the class-level cycle (LL -> RL -> RN -> LN) encoded by the
     componentwise formula.

Result recorded in evidence-carousel-v1.json.
"""

from functools import lru_cache
from collections import Counter
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


def counts(t):
    """(k,l,m,n_) = (#left leaves, #right leaves, #right nonleaves, #left nonleaves)."""
    res = Counter()

    def walk(x, side):
        if isinstance(x, Leaf):
            if side == "L":
                res["k"] += 1
            elif side == "R":
                res["l"] += 1
        else:
            if side == "L":
                res["n"] += 1
            elif side == "R":
                res["m"] += 1
            walk(x.l, "L")
            walk(x.r, "R")

    walk(t, None)
    return (res["k"], res["l"], res["m"], res["n"])


def M(q):
    k, l, m, n = q
    return (n + 1, k, l - 1, m)


def main(out_path="/tmp/carousel.json"):
    ev = {"formula": {}, "order_of_M": None, "class_cycle": "LL -> RL -> RN -> LN -> LL (4-cycle), SR base"}
    all_ok = True
    for n in range(2, 8):
        ok = True
        for t in ppcts(n):
            k, l, m, nn = counts(t)
            if not (k == m + 1 and l == nn + 1):
                ok = False
                break
            k2, l2, m2, n2 = counts(tau(t))
            if not (k2 == nn + 1 and l2 == k and m2 == l - 1 and n2 == m):
                ok = False
                break
        ev["formula"][str(n)] = ok
        all_ok &= ok
    q = (2, 3, 1, 2)
    seq = [q]
    for _ in range(6):
        q = M(q)
        seq.append(q)
    ev["order_of_M"] = next(i for i in range(1, 9) if seq[i] == seq[0])
    ev["orbit_M"] = seq
    ev["formula_all_ok"] = all_ok
    ev["note"] = ("Count map M is an involution (order 2); the class-level core is a "
                  "4-cycle. See note 31.")
    with open(out_path, "w") as f:
        json.dump(ev, f, indent=2, sort_keys=True)
    print(json.dumps({"formula_all_ok": all_ok, "order_of_M": ev["order_of_M"],
                      "orbit_M": seq}, indent=2))
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main(*sys.argv[1:])
