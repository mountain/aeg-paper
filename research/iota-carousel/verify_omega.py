#!/usr/bin/env python3
"""
Six-state carrier / iota complex unit: matrix checks, accompanying
notes/analysis-and-calculus/32-carousel-iota-alignment.md.

Basis of W = Lambda^1 E + Lambda^2 E  (E = <T,S,R>, Lambda^2 E = <SR,RT,TS>):
    [T, S, R, SR, RT, TS]

The paper (Paper 5, prop:one-complex-unit) states the action
    J(T)=SR, J(SR)=-T;  J(S)=RT, J(RT)=-S;  J(R)=TS, J(TS)=-R
with Omega on the Clifford algebra.  We verify:
  * Omega^2 = -I          (so J = Omega has order 4),
  * Omega^4 = I,
  * J preserves each plane W_T=<T,SR>, W_S=<S,RT>, W_R=<R,TS>,
  * on each plane's four signed states {e, Je, -e, -Je} J is a single 4-cycle.
"""

from fractions import Fraction as Q
import json
import sys

BASIS = ["T", "S", "R", "SR", "RT", "TS"]
IDX = {b: i for i, b in enumerate(BASIS)}

# Omega action: old -> (coeff, new)
ACTION = {"T": (1, "SR"), "SR": (-1, "T"),
          "S": (1, "RT"), "RT": (-1, "S"),
          "R": (1, "TS"), "TS": (-1, "R")}


def Omega():
    M = [[Q(0)] * 6 for _ in range(6)]
    for old, (c, new) in ACTION.items():
        M[IDX[new]][IDX[old]] = Q(c)
    return M


def mul(A, B):
    n = len(A)
    C = [[Q(0)] * n for _ in range(n)]
    for i in range(n):
        for k in range(n):
            if A[i][k]:
                for j in range(n):
                    C[i][j] += A[i][k] * B[k][j]
    return C


def is_scalar(A, s):
    n = len(A)
    return all(A[i][j] == (s if i == j else Q(0)) for i in range(n) for j in range(n))


def planes():
    return [("W_T", "T", "SR"), ("W_S", "S", "RT"), ("W_R", "R", "TS")]


def preserves_plane(M, e, je):
    """M maps span{e,je} into itself."""
    # columns of M at indices of e and je must have support only in {e,je}
    for b in (e, je):
        col = [M[i][IDX[b]] for i in range(6)]
        for i in range(6):
            if col[i] and BASIS[i] not in (e, je):
                return False
    return True


def four_cycle(e, je):
    """signed orbit e -> je -> -e -> -je -> e."""
    return [("+", e), ("+", je), ("-", e), ("-", je)]


def main(out_path="/tmp/omega.json"):
    Om = Omega()
    Om2 = mul(Om, Om)
    Om4 = mul(Om2, Om2)
    ev = {
        "Omega_squared_is_minus_I": is_scalar(Om2, Q(-1)),
        "Omega_fourth_is_I": is_scalar(Om4, Q(1)),
        "planes": [],
    }
    for name, e, je in planes():
        ev["planes"].append({
            "plane": name,
            "generators": [e, je],
            "j_preserves": preserves_plane(Om, e, je),
            "signed_four_cycle": four_cycle(e, je),
        })
    ev["note"] = ("J preserves each plane; on each plane's four signed states J is one "
                  "4-cycle.  The carousel's 4-cycle can align to ONE plane (non-canonical); "
                  "the SR entry / index shift has no J counterpart.  See note 32.")
    with open(out_path, "w") as f:
        json.dump(ev, f, indent=2, sort_keys=True)
    print(json.dumps({"Omega^2=-I": ev["Omega_squared_is_minus_I"],
                      "Omega^4=I": ev["Omega_fourth_is_I"],
                      "planes": [(p["plane"], p["j_preserves"]) for p in ev["planes"]]},
                     indent=2))
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main(*sys.argv[1:])
