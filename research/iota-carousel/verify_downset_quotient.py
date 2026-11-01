#!/usr/bin/env python3
"""
O(P) vs the down-set lattice of the infinite binary tree T_inf, accompanying
notes/analysis-and-calculus/45-downset-lattice-residual.md (OQ-098.2 residual).

Pushkarev-Byzov §5 (OCR): "not monotone with respect to the standard lattice
ordering of all trees (recall that the PPCTs form a distributive lattice whose
irreducible elements are ordered as the vertices of the infinite cubic tree)".
By Birkhoff this distributive lattice is Down(T_inf), the down-sets of T_inf;
its elements are ordered binary trees with 0/1/2 children (plane forests), not
full binary PPCTs (identified via the rotation bijection).

AEG's O(P) = Down(P) for P the dependency poset of a binary tree, which is a
finite binary-tree poset, hence order-embeds into T_inf as a finite subtree.

For Q a finite subtree of T_inf containing P, the restriction map
    rho : Down(Q) -> Down(P),   S |-> S ∩ P
is a surjective lattice homomorphism (it preserves union and intersection).
Hence O(P) is a lattice *quotient* of the down-set lattice, not a sublattice
(a down-set of P need not be a down-set of Q).
"""

import json
import sys


def leq_up(e, a, parent):
    y = e
    while True:
        if y == a:
            return True
        if y not in parent:
            return False
        y = parent[y]


def down_sets(els, leq):
    from itertools import combinations

    res = []
    for r in range(len(els) + 1):
        for S in combinations(els, r):
            S = set(S)
            ok = True
            for a in S:
                for e in els:
                    if leq(e, a) and e not in S:
                        ok = False
                        break
                if not ok:
                    break
            if ok:
                res.append(frozenset(S))
    return res


def check(P, parP, Q_els, parQ):
    DP = down_sets(P, lambda e, a: leq_up(e, a, parP))
    DQ = down_sets(Q_els, lambda e, a: leq_up(e, a, parQ))
    Pset = set(P)
    rho = {S: frozenset(set(S) & Pset) for S in DQ}
    surj = set(rho.values()) == set(DP)
    okU = okI = True
    for S in DQ:
        for T in DQ:
            if rho[frozenset(set(S) | set(T))] != frozenset(set(rho[S]) | set(rho[T])):
                okU = False
            if rho[frozenset(set(S) & set(T))] != frozenset(set(rho[S]) & set(rho[T])):
                okI = False
    sub = all(frozenset(S) in DQ for S in DP)
    return {"P": P, "num_DownP": len(DP), "num_DownQ": len(DQ),
            "rho_surjective": surj, "preserves_union": okU,
            "preserves_intersection": okI,
            "DownP_literal_sublattice_of_DownQ": sub}


def main(out_path="/tmp/downset_quotient.json"):
    # Q = binary tree of height 2 (nodes 0..6)
    parQ = {1: 0, 2: 0, 3: 1, 4: 1, 5: 2, 6: 2}
    Q_els = [0, 1, 2, 3, 4, 5, 6]
    cases = {
        "V(root+2children)": ([0, 1, 2], {1: 0, 2: 0}),
        "chain 3<1<0": ([0, 1, 3], {1: 0, 3: 1}),
        "L(1->0,2->0,3->1)": ([0, 1, 2, 3], {1: 0, 2: 0, 3: 1}),
        "root+2 + left has child": ([0, 1, 2, 3, 4], {1: 0, 2: 0, 3: 1, 4: 1}),
    }
    ev = {}
    for name, (P, parP) in cases.items():
        ev[name] = check(P, parP, Q_els, parQ)
    ev["summary"] = {
        "all_quotient": all(e["rho_surjective"] and e["preserves_union"] and e["preserves_intersection"]
                            for e in ev.values()),
        "none_literal_sublattice": all(not e["DownP_literal_sublattice_of_DownQ"] for e in ev.values()),
        "comment": "O(P)=Down(P) is a lattice QUOTIENT of Down(Q) (Q a finite subtree of T_inf) "
                   "via S|->S∩P; it is NOT a sublattice. See note 45.",
    }
    with open(out_path, "w") as f:
        json.dump(ev, f, indent=2, sort_keys=True)
    print(json.dumps(ev["summary"], indent=2))
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main(*sys.argv[1:])
