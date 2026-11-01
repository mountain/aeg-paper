#!/usr/bin/env python3
"""
Verify Pushkarev-Byzov Theorem 6.1 (fringing): Delta(Q(T)) = 3 Delta(T) if Delta
is odd, (3/2) Delta(T) if even.  Accompanying
notes/analysis-and-calculus/42-fringing-hecke.md (OQ-098.3).

The fringing Q replaces each leaf by a "cherry" Node(Leaf, Leaf), so the number
of leaves doubles (L -> 2L), while the orbit length Delta is multiplied by 3 (or
3/2).  This is a *substitution* growth Delta ~ L^{log_2 3}, distinct from the
*counting* growth of Hecke periodic orbits.
"""

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


def orbit_len(t, cap=10000):
    seen = {}
    cur = t
    i = 0
    while repr(cur) not in seen:
        seen[repr(cur)] = i
        cur = tau(cur)
        i += 1
        if i > cap:
            return -1
    return i - seen[repr(cur)]


def fringing(t):
    if t is LEAF:
        return Node(LEAF, LEAF)
    return Node(fringing(t.l), fringing(t.r))


def leaves(t):
    return 1 if t is LEAF else leaves(t.l) + leaves(t.r)


def main(out_path="/tmp/fringing.json"):
    tests = {
        "N(L,L)": Node(LEAF, LEAF),
        "N(L,N(L,L))": Node(LEAF, Node(LEAF, LEAF)),
        "N(N(L,L),L)": Node(Node(LEAF, LEAF), LEAF),
        "N(N(L,L),N(L,L))": Node(Node(LEAF, LEAF), Node(LEAF, LEAF)),
    }
    rows = []
    ok = True
    for name, t in tests.items():
        d = orbit_len(t)
        q = fringing(t)
        dq = orbit_len(q)
        pred = 3 * d if d % 2 == 1 else (3 * d) // 2
        match = dq == pred
        ok &= match
        rows.append({"tree": name, "leaves": leaves(t), "Delta": d,
                     "Q_leaves": leaves(q), "Delta_Q": dq, "Thm6.1_pred": pred,
                     "match": match})
    ev = {"rows": rows, "all_match": ok,
          "note": "fringing doubles leaves (L->2L) and multiplies orbit length by 3 "
                  "(or 3/2); substitution growth Delta ~ L^{log_2 3}. See note 42."}
    with open(out_path, "w") as f:
        json.dump(ev, f, indent=2, sort_keys=True)
    print(json.dumps({"all_match": ok, "rows": rows}, indent=2))
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main(*sys.argv[1:])
