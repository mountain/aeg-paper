#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""OQ-098 candidate: the translation between AEG's capping obstruction and the
seam-weight gap found on the physics side (V4–V6).

Two statements to be translated into each other:

  AEG side (this round, in ~/AEG/aeg-paper/research/capping-scope/):
    Thm 10.12 / A3.  A scalar assignment a with |da|_g^2 = mu^2 + lambda^2 a^2
    has, on {a != 0}, u = log|a|/|lambda| with |du| = 1; hence its level sets are
    *equidistants*.  A constant boundary value therefore has no regular
    continuation: u = k -+ d_g(., dD) has a non-smooth locus inside.

  Physics side (V4–V6):
    V4.  The interface value sigma alone cannot carry the weight: the weight is a
         function on the *fibre*; the fibre product (colimit) forgets it.
    V5.  The weight is CG_e . d^1(theta) . CG_mu: it needs a *representation
         space* on the seam and a *rotation* along it.
    V6.  The interface record therefore gains (V_e, <,>, U_e); capping = contraction
         with the vacuum, which requires the trivial label.

The bridge tested here:

  W1  "a|_dD = constant" IS "the boundary datum lies in the trivial representation".
      (A constant function on the circle is precisely the rotation-invariant mode.)
  W2  AEG's scalar seam is the j = 0 case of the seam datum.  Compare the two
      seams in one formula:
          j = 0 (1 state)            -> which helicity combinations survive, and is
          j = 1, transverse (2)         the weight theta-dependent at all?
          j = 1, all three states
  W3  Consequence: a scalar seam predicts a *flat* cos(theta) distribution, i.e.
      exactly V4's "weightless gluing".  So A3's obstruction and V4's missing
      weight are the same gap seen from two sides.

Author: DeepSeek Harness agent (deepseek-v4-flash-vision-exp), 2026-10-31,
at Mingli Yuan's direction.  Construction and reception by the same author; no
independent review.  Nothing in ~/AEG is modified by this file.

Run:  python3 verify_bridge.py [--check]
"""
import json
import sys

import sympy as sp

c, s = sp.symbols("c s", real=True)
sqrt2 = sp.sqrt(2)

# ======================================================================
# W1: constant boundary value <=> trivial representation
# ======================================================================
def w1_constant_is_trivial():
    """Fourier modes of a smooth function on S^1: only the m=0 mode is rotation-fixed."""
    th = sp.Symbol("theta", real=True)
    eps = sp.Symbol("epsilon", real=True)
    # a constant is fixed by every rotation
    const = sp.Symbol("k")
    fixed = sp.simplify(const.subs(th, th + eps) - const) == 0
    # a nonzero Fourier mode is not fixed
    mode = sp.cos(3 * th)
    moved = sp.simplify(sp.expand_trig(mode.subs(th, th + eps) - mode)) != 0
    # the m=0 mode of any nonconstant function is not the whole function
    return {"claim": "a|_dD = const  <=>  the boundary datum lies in the trivial rep (j = 0)",
            "constant_is_rotation_fixed": bool(fixed),
            "nonzero_mode_is_not_fixed": bool(moved),
            "reading": ("a function on the circle decomposes into Fourier modes; the constant "
                        "functions are exactly the rotation-invariant (m = 0, hence j = 0) part. "
                        "So AEG's hypothesis 'a|_dD = c is constant' is the hypothesis "
                        "'the seam label is trivial'."),
            "status": "standard consequence (Fourier decomposition on the circle)"}


# ======================================================================
# W2/W3: the seam label decides both the selection and the theta dependence
# ======================================================================
# <1 m | 1/2 h1 ; 1/2 h2>,  h = +-1 standing for +-1/2
CG_J1 = {
    (+1, +1): {+1: sp.Integer(1)},
    (+1, -1): {0: 1 / sqrt2},
    (-1, +1): {0: 1 / sqrt2},
    (-1, -1): {-1: sp.Integer(1)},
}
# <0 0 | 1/2 h1 ; 1/2 h2>  =  +-1/sqrt2, only when h1 = -h2
CG_J0 = {
    (+1, -1): 1 / sqrt2,
    (-1, +1): -1 / sqrt2,
}

D1 = sp.Matrix([
    [(1 + c) / 2, -s / sqrt2, (1 - c) / 2],
    [s / sqrt2, c, -s / sqrt2],
    [(1 - c) / 2, s / sqrt2, (1 + c) / 2],
])
M_INDEX = {+1: 0, 0: 1, -1: 2}


def amplitude(h1, h2, h3, h4, seam):
    """A = sum over the seam's states of CG_e * transport * CG_mu."""
    if seam == "j0":
        ce = CG_J0.get((h1, -h2), 0)
        cm = CG_J0.get((h3, -h4), 0)
        return sp.simplify(ce * 1 * cm)                 # d^0 = 1: no theta at all
    if seam == "j1_t":
        modes = (+1, -1)
    elif seam == "j1_all":
        modes = (+1, 0, -1)
    else:
        raise ValueError("seam:unknown")
    e_side, mu_side = CG_J1[(h1, -h2)], CG_J1[(h3, -h4)]
    total = sp.Integer(0)
    for m in modes:
        for mp in modes:
            a, b = e_side.get(m, 0), mu_side.get(mp, 0)
            if a and b:
                total += a * D1[M_INDEX[m], M_INDEX[mp]] * b
    return sp.simplify(total)


def w2_seam_label_table():
    helicities = (+1, -1)
    table = {}
    for seam in ("j0", "j1_t", "j1_all"):
        rows, nonzero = [], 0
        depends_on_theta = False
        weights = []
        for h1 in helicities:
            for h2 in helicities:
                for h3 in helicities:
                    for h4 in helicities:
                        A = amplitude(h1, h2, h3, h4, seam)
                        if sp.simplify(A) != 0:
                            nonzero += 1
                            if sp.simplify(sp.diff(A, c)) != 0:
                                depends_on_theta = True
                            weights.append(sp.simplify(A ** 2))
                        rows.append({"h": "%s%s->%s%s" % tuple(
                            "↑" if h > 0 else "↓" for h in (h1, h2, h3, h4)),
                            "A": str(A)})
        table[seam] = {"nonzero": nonzero,
                       "theta_dependent": bool(depends_on_theta),
                       "rows": rows}
    # V4's decisive numbers: at fixed sigma, the physical weight varies; flat weights do not
    w_physical = [sp.Rational(2), sp.Rational(34, 25), sp.Rational(26, 25),
                  sp.Rational(26, 25), sp.Rational(34, 25), sp.Rational(2)]
    v4_ratio = max(w_physical) / min(w_physical)
    return {"table": table,
            "V4_measured_variation_at_fixed_sigma": str(v4_ratio),
            "reading": ("the seam label j decides *both* which helicity combinations exist and "
                        "whether the weight depends on theta at all: j = 0 gives a theta-independent "
                        "weight (flat distribution), transverse j = 1 gives ±(1±cos)/2. V4 measured "
                        "that the physical weight varies by a factor %s across one fibre, so the "
                        "physical seam cannot be the scalar (j = 0) one." % v4_ratio),
            "status": "computationally verified example"}


def w3_a3_versus_v4():
    """The same gap, two sides: scalar transport has no internal state to carry the angle."""
    u = sp.Function("u")
    # AEG: |du| = 1 on a 2-disk means u is an arrival time; its level sets are equidistants,
    # so along a level set nothing changes: the transport is trivial on the transverse space.
    th = sp.Symbol("theta", real=True)
    scalar_weight = sp.Integer(1)                       # transporting a scalar along the seam: no theta
    rep_weight = sp.simplify(((1 + c) / 2) ** 2)        # transporting a spin-1 state: theta enters
    return {"aeg_side": ("A3: on {a != 0}, u = log|a|/|lambda| has |du| = 1, so the level sets are "
                         "equidistants; a constant boundary value forces u = k -+ d_g(., dD), which is "
                         "not smooth inside. There is no internal (transverse) degree of freedom."),
            "physics_side": ("V4: the weight is a function on the fibre; a colimit gluing collapses the "
                             "fibre to a point. V5: the weight needs a rep space and a rotation."),
            "the_bridge": ("a scalar transported along the seam carries no theta: moving along the "
                           "seam changes nothing transverse, so any weight built from it is constant "
                           "in theta. The weight that physics needs IS theta-dependent, so it cannot "
                           "come from the scalar sector."),
            "scalar_weight_in_theta": str(scalar_weight),
            "rep_weight_in_theta": str(rep_weight),
            "conclusion": ("A3's 'no regular constant-boundary cap' and V4's 'no weight from the "
                           "interface value' are the same deficiency: the interface has only one "
                           "number, so there is nowhere for the angular data to live."),
            "status": "structural proposal"}


def w4_x4_resolution():
    return {"previous_tension": ("V6 §X4: capping a seam contributes dim V_e (a number) while "
                                 "Thm 10.12 says a constant-boundary cap is impossible."),
            "resolution_by_W1": ("W1 identifies 'constant boundary' with 'trivial label j = 0'. "
                                 "So both statements are about the *same* case: at j = 0 the algebraic "
                                 "contraction is the number 1 = dim V_e, while the analytic realisation "
                                 "is obstructed (A3). They are two layers of one label, not two claims "
                                 "about different labels."),
            "status": "structural proposal",
            "what_would_upgrade_it": ("exhibit an AEG interface whose label is j != 0 and show that "
                                      "the capping obstruction does not apply to it (a j != 0 seam "
                                      "cannot be capped by the vacuum at all, only paired)")}


def run():
    return {"schema": "aeg-qed-seam-bridge-v1",
            "W1_constant_boundary_is_trivial_rep": w1_constant_is_trivial(),
            "W2_seam_label_table": w2_seam_label_table(),
            "W3_a3_versus_v4": w3_a3_versus_v4(),
            "W4_x4_tension_resolved_by_W1": w4_x4_resolution(),
            "limitations": [
                "W2's j=1 rows reuse the conventions of ../pants-v5-labels/ without re-deriving them",
                "W3 and W4 are structural proposals, not theorems; W4's upgrade needs a j != 0 AEG interface",
                "nothing here touches the AEG repository; the translation is not yet a statement in the paper",
            ]}


def main():
    report = run()
    if "--check" in sys.argv:
        a = report["W1_constant_boundary_is_trivial_rep"]
        print("[W1] 常值边界 ⟺ 平凡表示 j=0：", a["status"],
              "| 常数旋转不变", a["constant_is_rotation_fixed"],
              "| 非零模非不变", a["nonzero_mode_is_not_fixed"])
        b = report["W2_seam_label_table"]
        print("[W2] 缝的标签决定选择与角度依赖：")
        for seam, v in b["table"].items():
            print("      %-8s 非零 %2d 个 | θ 依赖 %s" % (seam, v["nonzero"], v["theta_dependent"]))
        print("      V4 实测：同一 σ 下权重跨度 =", b["V4_measured_variation_at_fixed_sigma"])
        print("[W3]", report["W3_a3_versus_v4"]["conclusion"])
        print("[W4]", report["W4_x4_tension_resolved_by_W1"]["resolution_by_W1"][:100], "...")
    else:
        print(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True, default=str))


if __name__ == "__main__":
    main()
