#!/usr/bin/env python3
"""
Advance of the "shift" question (note 32 §4), accompanying
notes/analysis-and-calculus/33-shift-research.md.

Two checks:

1. SCREW STRUCTURE of the iota frame.  J = [[0,-I],[I,0]], J^2=-I, H=diag(H0,H0),
   A=-JH.  Verify [J,H]=0, A^2=-H^2, and exp(tA)=cos(tH)-J sin(tH) (matrix cos/sin
   via the symmetric eigendecomposition of H).  This says exp(tA) rotates by an
   angle proportional to the eigenvalue of H: a screw (rotation + height).

2. H DOES NOT CARRY THE SHIFT.  For n=4 PPCTs, build the cut graph (Hasse diagram
   of the down-set lattice O(P) of the dependency poset), compute H0=L/(2 d_max),
   and compare the spectrum with k = #left leaves.  Several trees share the same
   spectrum but have different k, so the cut-graph Laplacian cannot determine the
   carousel index: the shift is a *planar* quantity, the cut graph is not.
"""

import numpy as np
import json
import sys
from functools import lru_cache


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


def internal_nodes(t):
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


def descendants(nodes):
    desc = {}

    def dd(v):
        s = {v}
        for c in nodes[v]:
            if c is not None:
                s |= dd(c)
        desc[v] = s
        return s

    for v in nodes:
        dd(v)
    return desc


def downsets(nodes):
    desc = descendants(nodes)
    ids = list(nodes)
    out = set()
    for mask in range(1 << len(ids)):
        S = frozenset(ids[i] for i in range(len(ids)) if (mask >> i) & 1)
        if all(desc[v] <= S for v in S):
            out.add(S)
    return sorted(out, key=lambda s: (len(s), sorted(s)))


def cut_graph(ds):
    idx = {s: i for i, s in enumerate(ds)}
    n = len(ds)
    A = np.zeros((n, n))
    for i, S in enumerate(ds):
        for v in S:
            T = S - {v}
            if T in idx:
                j = idx[T]
                A[i, j] = A[j, i] = 1
    return A


def h0(A):
    L = np.diag(A.sum(1)) - A
    dmax = max(1, int(np.diag(L).max()))
    return L / (2 * dmax)


def left_leaves(t):
    c = 0

    def walk(x, side):
        nonlocal c
        if not isinstance(x, Node):
            if side == "L":
                c += 1
            return
        walk(x.l, "L")
        walk(x.r, "R")

    walk(t, None)
    return c


def sym_cos_sin(H, t):
    w, Q = np.linalg.eigh(H)
    cosH = (Q * np.cos(t * w)) @ Q.T
    sinH = (Q * np.sin(t * w)) @ Q.T
    return cosH, sinH


def screw_checks():
    rng = np.random.default_rng(0)
    n = 3
    L = rng.integers(0, 3, size=(n, n))
    L = (L + L.T)
    np.fill_diagonal(L, 0)
    H0 = np.diag(L.sum(1)) - L
    H0 = H0 / (2 * max(1, int(np.diag(H0).max())))
    H = np.block([[H0, np.zeros((n, n))], [np.zeros((n, n)), H0]])
    J = np.block([[np.zeros((n, n)), -np.eye(n)], [np.eye(n), np.zeros((n, n))]])
    A = -J @ H
    t = 0.3
    cosH, sinH = sym_cos_sin(H, t)
    return {
        "JH_eq_HJ": bool(np.allclose(J @ H, H @ J)),
        "J2_eq_minusI": bool(np.allclose(J @ J, -np.eye(2 * n))),
        "A2_eq_minus_H2": bool(np.allclose(A @ A, -H @ H)),
        "exp_tA_eq_cos_tH_minus_J_sin_tH": bool(
            np.allclose(_expm_series(A, t), cosH - J @ sinH, atol=1e-9)
        ),
    }


def _expm_series(A, t, order=40):
    n = len(A)
    out = np.eye(n)
    term = np.eye(n)
    for k in range(1, order):
        term = term @ (t * A) / k
        out = out + term
    return out


def shift_checks(n=4):
    rows = []
    for t in ppcts(n):
        nodes = internal_nodes(t)
        ds = downsets(nodes)
        A = cut_graph(ds)
        H = h0(A)
        ev = tuple(round(float(x), 4) for x in np.linalg.eigvalsh(H))
        rows.append({"tree": repr(t), "k_left_leaves": left_leaves(t),
                     "cuts": len(ds), "spectrum": ev})
    # group by spectrum
    byspec = {}
    for r in rows:
        byspec.setdefault(r["spectrum"], []).append(r["k_left_leaves"])
    same_spectrum_diff_k = {
        str(spec): sorted(set(ks)) for spec, ks in byspec.items() if len(set(ks)) > 1
    }
    return {"n_leaves": n, "rows": rows,
            "spectra_with_different_k": same_spectrum_diff_k}


def main(out_path="/tmp/shift.json"):
    ev = {"screw": screw_checks(), "shift": shift_checks(4)}
    ev["comment"] = ("exp(tA) is a screw (rotation by angle proportional to H "
                     "eigenvalue); but the cut-graph Laplacian spectrum does not "
                     "determine the carousel index k (#left leaves): same-spectrum "
                     "trees have different k. The shift is planar; the cut graph is not.")
    with open(out_path, "w") as f:
        json.dump(ev, f, indent=2, sort_keys=True)
    print(json.dumps({"screw": ev["screw"],
                      "spectra_with_different_k": list(ev["shift"]["spectra_with_different_k"].items())},
                     indent=2))
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main(*sys.argv[1:])
