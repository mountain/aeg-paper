#!/usr/bin/env python3
"""
Order-4 alignment: AEG six-state carrier complex structure J vs the Hecke group
C4 generator R.  Accompanying
notes/analysis-and-calculus/47-order4-alignment.md (OQ-098.3 precise order-4 match).

AEG side (paper-5 §4): E = <T,S,R> with T^2=S^2=R^2=1 and eps_i eps_j + eps_j eps_i = 0
(Clifford Cl(3)); W = Lambda^1 E (+) Lambda^2 E = <T,S,R> (+) <SR,RT,TS>; Omega=TSR,
Omega^2=-1; J = Omega· acts as J(T)=SR, J(SR)=-T etc., J^2=-I, J^4=I, chi=(lambda^2+1)^3,
with three invariant planes W_T,W_S,W_R on each of which J = [[0,-1],[1,0]].

Hecke side: Gamma_4 = <J_h, R | J_h^2 = R^4 = 1> = C2 * C4 (eq:q4-sign-kernel-presentation),
R = J_h T with T: z->z+sqrt2, J_h: z->-1/z.  As matrices R = [[0,-1],[1,sqrt2]].

Result: R^4 = -I, so R^2 = [[-1,-sqrt2],[sqrt2,1]] is a complex structure ((R^2)^2 = -I),
with characteristic polynomial lambda^2+1 and eigenvalues +-i -- exactly the same as the
carousel's J restriction to any plane.  Hence J (carousel) is *conjugate* to R^2 (Hecke),
and the Hecke C4 generator R is a square root of the carousel's complex structure.
Note R itself is NOT conjugate to J: chi_R = lambda^2 - sqrt2 lambda + 1 (eigenvalues
e^{+-i pi/4}), order 8 in SL2 / order 4 in PGL2, whereas J has order 4 in GL / order 2 in
GL/{+-I}.
"""

import json
import sys

import sympy as sp


def mat_str(M):
    return [[str(x) for x in row] for row in M.tolist()]


def main(out_path="/tmp/order4.json"):
    lam = sp.symbols("lambda")
    # AEG six-state J on basis [T,S,R,SR,RT,TS]
    J = sp.Matrix([
        [0, 0, 0, -1, 0, 0],
        [0, 0, 0, 0, -1, 0],
        [0, 0, 0, 0, 0, -1],
        [1, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0]])
    I6 = sp.eye(6)
    ev = {}
    ev["aeg_J_squared_is_minus_I"] = bool(sp.simplify(J * J + I6) == sp.zeros(6, 6))
    ev["aeg_J_fourth_is_I"] = bool(sp.simplify(J**4 - I6) == sp.zeros(6, 6))
    ev["aeg_J_charpoly"] = str(sp.factor(J.charpoly(lam).as_expr()))
    planes = {}
    for name, idx in [("W_T=<T,SR>", [0, 3]), ("W_S=<S,RT>", [1, 4]), ("W_R=<R,TS>", [2, 5])]:
        sub = J.extract(idx, idx)
        planes[name] = {"matrix": mat_str(sub),
                        "charpoly": str(sp.factor(sub.charpoly(lam).as_expr()))}
    ev["aeg_planes"] = planes

    # Hecke R = J_h o T
    s2 = sp.sqrt(2)
    Jh = sp.Matrix([[0, -1], [1, 0]])
    Th = sp.Matrix([[1, s2], [0, 1]])
    R = sp.simplify(Jh * Th)
    R2 = sp.simplify(R * R)
    ev["hecke_R"] = {"matrix": mat_str(R),
                     "charpoly": str(sp.factor(R.charpoly(lam).as_expr())),
                     "eigenvalues": [str(sp.simplify(e)) for e in sp.solve(R.charpoly(lam).as_expr(), lam)],
                     "R4_is_minus_I": bool(sp.simplify(R**4 + sp.eye(2)) == sp.zeros(2, 2))}
    ev["hecke_R2"] = {"matrix": mat_str(R2),
                      "charpoly": str(sp.factor(R2.charpoly(lam).as_expr())),
                      "eigenvalues": [str(sp.simplify(e)) for e in sp.solve(R2.charpoly(lam).as_expr(), lam)],
                      "R2_squared_is_minus_I": bool(sp.simplify(R2 * R2 + sp.eye(2)) == sp.zeros(2, 2))}
    # comparison: J|plane and R^2 both have char poly lambda^2+1 (hence conjugate)
    Jplane = sp.Matrix([[0, -1], [1, 0]])
    ev["alignment"] = {
        "J_plane_charpoly": str(sp.factor(Jplane.charpoly(lam).as_expr())),
        "R2_charpoly": str(sp.factor(R2.charpoly(lam).as_expr())),
        "conjugate": bool(sp.factor(Jplane.charpoly(lam).as_expr()) == sp.factor(R2.charpoly(lam).as_expr())),
        "comment": "carousel J|plane ~ Hecke R^2 (both complex structures, i.e. square roots "
                   "of -I). R itself is a square root of that complex structure (R^4=-I); "
                   "R is NOT conjugate to J (chi_R = lambda^2 - sqrt2 lambda + 1).",
    }
    with open(out_path, "w") as f:
        json.dump(ev, f, indent=2, sort_keys=True)
    print(json.dumps({"aeg_J_charpoly": ev["aeg_J_charpoly"],
                      "hecke_R_charpoly": ev["hecke_R"]["charpoly"],
                      "hecke_R2_charpoly": ev["hecke_R2"]["charpoly"],
                      "alignment": ev["alignment"]}, indent=2))
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main(*sys.argv[1:])
