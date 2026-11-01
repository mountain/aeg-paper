#!/usr/bin/env python3
"""
Planar carrier construction: the "screw module", accompanying
notes/analysis-and-calculus/34-planar-carrier.md.

Model:
  V = V_class (x) V_index,  V_class = <LL, RL, RN, LN> (4-dim, planar),
                            V_index = <e_k : k >= 1> (unbounded index).
Operators:
  J (rotation) : (class, k) -> (class+1 mod 4, k)          [= iota complex unit, Z/4]
  S (shift)    : (class, k) -> (class, k+1)               [unbounded index]
  C (carousel) : (class, k) -> (class+1 mod 4, k + [class == LN])  [screw]
Checks:
  * C^4 = S   (carousel is a screw: 4 class turns = one index shift)
  * J^4 = id  (iota rotation is order 4)
  * [J, S] = 0
  * the COUNT shadow M (Cor 4.4) satisfies M^2 = id, i.e. the screw is invisible
    to the counts (S reduces to id there).
"""

import json
import sys

# 0 = LL (left leaf), 1 = RL (right leaf), 2 = RN (right nonleaf), 3 = LN (left nonleaf)


def J(c, k):
    return ((c + 1) % 4, k)


def S(c, k):
    return (c, k + 1)


def C(c, k):
    return ((c + 1) % 4, k + (1 if c == 3 else 0))


def iterate(f, x, n):
    for _ in range(n):
        x = f(*x)
    return x


def M(q):
    k, l, m, n = q
    return (n + 1, k, l - 1, m)


def main(out_path="/tmp/planar.json"):
    ev = {}
    ev["C_4th_power_equals_S"] = all(iterate(C, (c, k), 4) == S(c, k)
                                     for c in range(4) for k in range(5))
    ev["J_4th_power_is_id"] = all(iterate(J, (c, k), 4) == (c, k)
                                  for c in range(4) for k in range(5))
    ev["J_S_commute"] = all(J(*S(c, k)) == S(*J(c, k))
                           for c in range(4) for k in range(5))
    ev["count_shadow_M2_is_id"] = all(
        M(M((m + 1, n + 1, m, n))) == (m + 1, n + 1, m, n)
        for m in range(1, 5) for n in range(1, 5))
    seq = [(0, 1)]
    for _ in range(8):
        seq.append(C(*seq[-1]))
    ev["carousel_orbit"] = seq
    ev["class_labels"] = {0: "LL left leaf", 1: "RL right leaf",
                          2: "RN right nonleaf", 3: "LN left nonleaf"}
    ev["note"] = ("The carousel is a screw: C^4 = S (index shift).  The pure "
                  "rotation J (= iota complex unit) is the mod-S reduction.  The "
                  "count shadow M is an involution (screw invisible).  See note 34.")
    with open(out_path, "w") as f:
        json.dump(ev, f, indent=2, sort_keys=True)
    print(json.dumps({k: v for k, v in ev.items() if k != "class_labels"}, indent=2))
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main(*sys.argv[1:])
