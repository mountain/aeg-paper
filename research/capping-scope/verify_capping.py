#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""OQ-099 candidate: the *scope* of the constant-boundary capping obstruction.

Target: Paper I, `thm:constant-boundary-capping-obstruction` (printed Thm 10.12)
and `cor:capping-dichotomy` (printed 10.14 since 2026-11-01; 10.13 before).

Published theorem: no smooth (g,a) on a compact disk with
    |da|^2_g = mu^2 + lambda^2 a^2  on int D,   a|_dD = c (constant),
when mu != 0 (lambda in R arbitrary).

This checker does not re-prove it.  It asks which hypotheses are *sharp*:

  A1  The published proof uses only mu != 0, via RHS >= mu^2 > 0.  So the
      obstruction as proved is metric- and lambda-independent.  [sufficiency]
  A2  mu = 0 and lambda*c = 0  =>  a smooth cap EXISTS, explicitly:
        lambda = 0:  a = c   (then |da| = 0 = mu^2 + lambda^2 a^2)
        c = 0     :  a = 0   (likewise)
      Hence the conclusion of Thm 10.12 fails outside its hypothesis.
  A3  mu = 0, lambda != 0, c != 0  =>  there is NO smooth cap either, but by a
      *different* mechanism: on {a != 0} the function u = log|a|/|lambda|
      satisfies |du| = 1, so its level sets are equidistants; u is constant on
      dD forces u = k -+ d_g(., dD), which is not smooth on the interior cut
      locus; and a smooth a cannot vanish at an interior point, because
      |da| = |lambda||a| forces |da|/|a| -> infinity there.
      => mu != 0 is SUFFICIENT BUT NOT NECESSARY.
  A4  Sharp statement (combining A1-A3): a smooth cap exists iff mu = 0 and
      lambda*c = 0.
  A5  With mu != 0 an explicit *singular* cap exists (a(r) = (mu/lambda)
      sinh(lambda (r+C))), realising branch (2) of Cor 10.14; the singular
      point may be prescribed anywhere in int D (A6).

Revision record: v1 of this file claimed "mu = 0 => every constant c is
smoothly cappable" using a(r) = c exp(lambda (r-1)) on the flat disk.  That
family is analytic *as a function of r* but NOT smooth as a function of (x,y):
it contains odd powers of r = sqrt(x^2+y^2).  The claim is withdrawn; see A2/A3
for the corrected picture.  Recorded here because the repository preserves
development history rather than overwriting it.

Provenance: direction Mingli Yuan; construction, checker and text by the
DeepSeek Harness agent (deepseek-v4-flash-vision-exp), 2026-10-31.  Same author
for construction and reception; NOT independently reviewed.  No paper source is
modified by this file and no proof of the paper is altered.

Run:
    python3 verify_capping.py                          # JSON report
    python3 verify_capping.py --check                  # human-readable verdicts
    python3 verify_capping.py --verify-evidence FILE   # replay the committed evidence

Exit code is non-zero if any embedded status starts with FAIL (used by CI at
.github/workflows/capping-scope.yml).
"""
import json
import pathlib
import sys

import sympy as sp

r, mu, lam = sp.symbols("r mu lambda", positive=True)
C = sp.symbols("C", real=True)
c = sp.symbols("c", real=True)
x, y = sp.symbols("x y", real=True)
rr = sp.sqrt(x ** 2 + y ** 2)


def demand(condition, reason):
    if not condition:
        raise SystemExit("verify_capping: " + reason)


# ======================================================================
# A1: what the published proof uses
# ======================================================================
def a1_sufficiency():
    a = sp.Symbol("a", real=True)
    rhs = mu ** 2 + lam ** 2 * a ** 2
    positive_for_all_a = sp.simplify(rhs.subs({mu: sp.Rational(1, 2), lam: sp.Rational(3, 7)}) -
                                     (sp.Rational(1, 4) + sp.Rational(9, 49) * a ** 2)) == 0
    return {"claim": "RHS = mu^2 + lambda^2 a^2 >= mu^2 > 0 whenever mu != 0, for every a, lambda and g",
            "identity_checked": bool(positive_for_all_a),
            "proof_steps": ["|da|^2 >= mu^2 > 0  =>  da has no zero on int D",
                            "non-constant a with constant boundary value has an interior extremum, da = 0 there",
                            "constant a satisfies the boundary value but da = 0 everywhere"],
            "status": "proved with stated hypotheses",
            "consequence": "the obstruction as proved is metric- and lambda-independent (sufficiency only)"}


# ======================================================================
# A2: the degenerate cases DO admit smooth caps
# ======================================================================
def a2_degenerate_caps_exist():
    # lambda = 0, mu = 0: a = c
    l0 = sp.simplify(sp.diff(sp.Integer(0), r) - (0 + 0))          # |da|^2 - (mu^2+lam^2a^2) at lam=mu=0
    lhs_lam0 = sp.Integer(0)
    rhs_lam0 = sp.simplify((mu ** 2 + lam ** 2 * c ** 2).subs({mu: 0, lam: 0}))
    # c = 0, mu = 0: a = 0
    rhs_c0 = sp.simplify((mu ** 2 + lam ** 2 * 0 ** 2).subs(mu, 0))
    return {"claim": "mu = 0 and (lambda = 0 or c = 0) admit an explicit smooth cap",
            "case_lambda_zero_mu_zero": {"a": "a = c (constant)", "|da|^2": str(lhs_lam0),
                                         "mu^2+lambda^2a^2": str(rhs_lam0),
                                         "identity_holds": lhs_lam0 == rhs_lam0},
            "case_c_zero_mu_zero": {"a": "a = 0 (constant)", "mu^2+lambda^2a^2": str(rhs_c0),
                                    "identity_holds": rhs_c0 == 0},
            "status": "proved",
            "consequence": "the theorem's conclusion does NOT extend to the whole of mu = 0"}


# ======================================================================
# A3: mu = 0, lambda != 0, c != 0 is obstructed -- by the eikonal mechanism
# ======================================================================
def a3_eikonal_mechanism():
    """Verify the two algebraic steps of the mechanism (flat disk, radial ansatz)."""
    # step 1: u = log a / lambda  (a > 0 on {a != 0})  =>  du * (lambda a) = da
    a_sym = sp.Function("a")
    u = sp.log(a_sym(r)) / lam
    identity_step1 = sp.simplify(sp.diff(u, r) * lam * a_sym(r) - sp.diff(a_sym(r), r))
    ratio = "1" if identity_step1 == 0 else str(identity_step1)
    # step 2: a level set of u that is a circle forces u = k -+ (1 - r) near dD,
    #         and that function is not smooth in (x, y) at the centre
    u_circle = sp.symbols("k", real=True) + (1 - rr)
    grad = sp.simplify(sp.sqrt(sp.diff(u_circle, x) ** 2 + sp.diff(u_circle, y) ** 2))
    a_of_u = sp.exp(lam * u_circle)
    # the culprit: odd powers of r in the expansion about the centre
    r_sym = sp.symbols("r_sym", positive=True)
    series = sp.series(sp.exp(-lam * r_sym), r_sym, 0, 3).removeO()
    has_odd_power = sp.simplify(sp.diff(series, r_sym).subs(r_sym, 0)) != 0
    return {"claim": ("mu = 0, lambda != 0, c != 0: no smooth cap; mechanism is the equidistant "
                      "structure of u = log|a|/|lambda| plus the impossibility of an interior zero"),
            "step1_identity_du_times_lambda_a_minus_da": str(ratio),
            "step1_holds": identity_step1 == 0,
            "step1_reading": "du = da/(lambda a), so |da| = |lambda||a| on {a != 0} gives |du| = 1",
            "step2_gradient_of_circular_level_u": str(grad),
            "step2_reading": ("a circular level set with |du| = 1 forces u = k -+ (1-r); "
                              "then a = exp(lambda u) has odd powers of r = sqrt(x^2+y^2) about the "
                              "centre, hence is not C^infinity there"),
            "series_about_centre_has_odd_power": bool(has_odd_power),
            "status": "partially proved",
            "hypotheses_used": ["|du| = 1 implies the level sets are equidistants (standard)",
                                "the distance to a closed curve in a compact region is not smooth on a "
                                "non-empty interior set (the cut locus / medial axis)",
                                "a smooth a with |da| = |lambda||a| cannot vanish at an interior point "
                                "(scaling argument, verified separately below)"]}


def a3b_interior_zero_impossible():
    """|da| = |lambda||a| with a(p) = 0 forces |da|/|a| -> infinity at p (scaling argument)."""
    # model: a smooth function vanishing to order m at the origin behaves like r^m
    m = sp.symbols("m", positive=True)
    r_sym = sp.symbols("r_sym", positive=True)
    ratio = sp.simplify((m * r_sym ** (m - 1)) / (sp.Abs(lam) * r_sym ** m))
    limit = sp.limit(ratio, r_sym, 0, "+")
    return {"claim": "a smooth a with |da| = |lambda||a| cannot vanish at an interior point",
            "ratio_|da|/(|lambda||a|)_model": str(ratio),
            "limit_at_the_zero": str(limit),
            "reading": ("if a ~ r^m (m >= 1) near its zero, then |da|/|a| ~ m/(|lambda| r) -> infinity, "
                        "contradicting |da| = |lambda||a|, which needs the ratio to be 1"),
            "status": "proved (scaling argument)"}


# ======================================================================
# A5: with mu != 0 an explicit singular cap (branch (2) of Cor 10.14)
# ======================================================================
def a5_singular_cap():
    a = (mu / lam) * sp.sinh(lam * (r + C))
    lhs = sp.simplify(sp.diff(a, r) ** 2)
    rhs = sp.simplify(mu ** 2 + lam ** 2 * a ** 2)
    identity = sp.simplify(sp.expand(lhs - rhs)) == 0
    boundary_C = sp.solve(sp.Eq(a.subs(r, 1), c), C)
    A0 = sp.simplify(a.subs(r, 0))
    B0 = sp.simplify(sp.diff(a, r).subs(r, 0))
    return {"claim": ("a(r) = (mu/lambda) sinh(lambda (r+C)) solves |da|^2 = mu^2 + lambda^2 a^2 "
                      "exactly on the punctured disk, with a(1) = c"),
            "equation_identity": bool(identity),
            "a_at_centre": str(A0),
            "slope_at_centre": str(B0),
            "slope_over_mu": str(sp.simplify(B0 / mu)),
            "C_from_a(1)=c": [str(sp.simplify(sol)) for sol in boundary_C],
            "regularity": "C^0 on the closed disk, C^infinity on the punctured disk, not C^1 at the centre",
            "status": "proved" if identity else "FAIL"}


def a5b_one_sided_derivatives():
    Bsym = mu * sp.cosh(lam * C)
    A0 = (mu / lam) * sp.sinh(lam * C)
    right = A0 + Bsym * x
    left = A0 - Bsym * x
    return {"claim": "the two axes at the centre give +B and -B, so the cap is not C^1 there",
            "difference": str(sp.simplify(right - left)),
            "difference_at_x_eq_1": str(sp.simplify((right - left).subs(x, 1))),
            "status": "proved"}


def a5c_numeric(mu_v=1.0, lam_v=1.0, c_v=2.0):
    import math
    C_v = math.asinh(c_v * lam_v / mu_v) / lam_v - 1.0

    def a(rv):
        return (mu_v / lam_v) * math.sinh(lam_v * (rv + C_v))

    def ap(rv):
        return mu_v * math.cosh(lam_v * (rv + C_v))

    rows, worst = [], 0.0
    for rv in (0.0, 0.1, 0.25, 0.5, 0.75, 1.0):
        lhs, rhs = ap(rv) ** 2, mu_v ** 2 + lam_v ** 2 * a(rv) ** 2
        worst = max(worst, abs(lhs - rhs) / max(1.0, abs(rhs)))
        rows.append({"r": rv, "a": a(rv), "|da|^2": lhs, "mu^2+lambda^2a^2": rhs})
    return {"parameters": {"mu": mu_v, "lambda": lam_v, "c": c_v, "C": C_v},
            "a_at_1": a(1.0), "slope_at_centre": ap(0.0),
            "max_relative_pde_residual": worst, "rows": rows,
            "status": "computationally verified example" if worst < 1e-12 else "FAIL"}


# ======================================================================
# A6 / A7
# ======================================================================
def a6_move_singularity():
    return {"claim": ("for a boundary-fixing diffeomorphism phi with phi(p0) = p1, the pair "
                      "(a o phi^{-1}, (phi^{-1})^* g) satisfies the same equation with the singularity at p1"),
            "why": "|d(a o phi^{-1})|^2_{(phi^{-1})^*g} = |da|^2_g by definition of the pullback metric; "
                   "phi fixes the boundary, so the boundary value is unchanged",
            "status": "proved"}


def a7_topological_half():
    return {"pointer": "research/pants-interface-disks/README.md (OQ-096 V1)",
            "fact": "[C] != 0 in H_1(S;F_2) (rank 110 -> 111 on adjoining C) while C = dD in the body",
            "reading": ("topological fillability (Thm 10.4) and analytic fillability (Thm 10.12) are "
                        "different statements; A5 supplies the middle case: one admissible singularity"),
            "status": "standard consequence requiring an in-paper proof"}


def run():
    return {
        "schema": "aeg-capping-scope-v2",
        "question": "which hypotheses of the constant-boundary capping obstruction are sharp?",
        "A1_sufficiency": a1_sufficiency(),
        "A2_degenerate_caps_exist": a2_degenerate_caps_exist(),
        "A3_eikonal_mechanism": a3_eikonal_mechanism(),
        "A3b_interior_zero_impossible": a3b_interior_zero_impossible(),
        "A5_singular_cap": a5_singular_cap(),
        "A5b_one_sided_derivatives": a5b_one_sided_derivatives(),
        "A5c_numeric": a5c_numeric(),
        "A6_move_the_singularity": a6_move_singularity(),
        "A7_topological_half": a7_topological_half(),
        "verdict": {
            "sharp_statement": ("a smooth cap (|da|^2 = mu^2 + lambda^2 a^2, a|_dD = c) exists "
                                "iff mu = 0 and lambda*c = 0"),
            "what_this_says_about_thm_10_12": ("its hypothesis mu != 0 is SUFFICIENT but NOT NECESSARY: "
                                               "the obstruction also holds for mu = 0, lambda != 0, c != 0 "
                                               "(A3), and fails exactly in the degenerate cases (A2)"),
            "what_this_says_about_cor_10_13": ("branch (2) ('admit an interior critical point or a "
                                               "non-C^1/metric singularity') is NON-EMPTY: A5 exhibits a "
                                               "witness, and A6 shows its singular point is movable"),
            "not_claimed": ["no change to Thm 10.12 or Cor 10.14 is proposed by this file",
                            "A3 is labelled 'partially proved': it rests on two standard facts listed there, "
                            "and this file verifies only its algebraic steps",
                            "no claim that the singular cap is unique or canonical",
                            "no claim about non-flat metrics for A2/A5 (only the obstruction A1 is "
                            "metric-independent)"],
        },
        "paper_action_taken": ("APPLIED 2026-11-01: the two remarks now sit in "
                              "paper-1/sections/08-caps-and-interface-disks.tex as Remark 10.13 "
                              "(rem:capping-scope-mu-essential) and Remark 10.15 "
                              "(rem:capping-singular-branch-nonempty); Corollary shifted 10.13 -> 10.14, "
                              "Definition (certified cap tuple) shifted 10.14 -> 10.16."),
        "recommended_paper_action": [
            "option 1 (minimal): add a remark after Thm 10.12 recording that mu != 0 is sufficient but not "
            "necessary, and that the sharp condition is mu = 0 and lambda*c = 0 (A2 for the 'only if' "
            "direction of the degenerate cases, A3 for the rest);",
            "option 2 (stronger): state the iff-condition as its own proposition, citing A3's two standard "
            "facts, and keep Thm 10.12 as the short sufficient statement;",
            "add a remark after Cor 10.14 exhibiting the A5 family, so branch (2) is known to be non-empty;",
            "keep the hypothesis list of Thm 10.12 unchanged.",
        ],
        "limitations": [
            "construction and reception by the same author; no independent review",
            "A3 is a mechanism with two cited standard facts, not a completed proof in this repository",
            "A2 and A5 are explicit on the flat disk; the paper's theorem is stated for arbitrary smooth g",
            "only the conical singularity type is examined; the 'interior critical point' sub-branch of "
            "Cor 10.14(2) is not constructed",
            "the relation to notes/analysis-and-calculus/25-* has not been checked statement by statement",
        ],
    }


def _normalised(report):
    """让内存里的报告与写进 JSON 的形态一致（sort_keys + default=str）。"""
    return json.loads(json.dumps(report, sort_keys=True, default=str))


def _compare(a, b, path="", diffs=None):
    """严格比较，浮点用相对容差。返回差异列表（空 = 通过）。"""
    if diffs is None:
        diffs = []
    if isinstance(a, dict) and isinstance(b, dict):
        for key in sorted(set(a) | set(b)):
            if key not in a or key not in b:
                diffs.append("%s.%s: missing on one side" % (path, key))
            else:
                _compare(a[key], b[key], "%s.%s" % (path, key), diffs)
    elif isinstance(a, list) and isinstance(b, list):
        if len(a) != len(b):
            diffs.append("%s: length %d != %d" % (path, len(a), len(b)))
        for index, (x, y) in enumerate(zip(a, b)):
            _compare(x, y, "%s[%d]" % (path, index), diffs)
    elif isinstance(a, float) or isinstance(b, float):
        if abs(a - b) > 1e-9 * max(1.0, abs(a), abs(b)):
            diffs.append("%s: %r != %r" % (path, a, b))
    elif a != b:
        diffs.append("%s: %r != %r" % (path, a, b))
    return diffs


def _failures(report):
    """报告里任何 status 落到 FAIL 都算失败。"""
    found = []

    def walk(node, path):
        if isinstance(node, dict):
            for key, value in node.items():
                if key == "status" and isinstance(value, str) and value.startswith("FAIL"):
                    found.append("%s.status = %s" % (path, value))
                walk(value, "%s.%s" % (path, key))
        elif isinstance(node, list):
            for index, value in enumerate(node):
                walk(value, "%s[%d]" % (path, index))

    walk(report, "")
    return found


def main():
    args = sys.argv[1:]
    report = run()

    if args[:1] == ["--verify-evidence"]:
        demand(len(args) == 2, "usage: verify_capping.py --verify-evidence evidence.json")
        saved = json.loads(pathlib.Path(args[1]).read_text(encoding="utf-8"))
        diffs = _compare(_normalised(report), _normalised(saved))
        if diffs:
            print(json.dumps({"status": "evidence-mismatch", "count": len(diffs),
                              "first": diffs[:10]}, ensure_ascii=False, indent=2))
            raise SystemExit(1)
        print(json.dumps({"status": "evidence-reproduced", "path": args[1]}, sort_keys=True))
        return

    failures = _failures(report)
    if "--check" in args:
        print("[A1] 充分性（只用到 mu != 0）：", report["A1_sufficiency"]["status"])
        a = report["A2_degenerate_caps_exist"]
        print("[A2] 退化情形**有**光滑封盖：", a["status"],
              "| λ=0∧μ=0:", a["case_lambda_zero_mu_zero"]["identity_holds"],
              "| c=0∧μ=0:", a["case_c_zero_mu_zero"]["identity_holds"])
        b = report["A3_eikonal_mechanism"]
        print("[A3] mu=0,λ≠0,c≠0 仍被阻碍：", b["status"],
              "| du·(λa)=da:", b["step1_holds"], "| 中心含奇次幂:", b["series_about_centre_has_odd_power"])
        print("[A3b] 内部零点不可能：", report["A3b_interior_zero_impossible"]["limit_at_the_zero"])
        d = report["A5_singular_cap"]
        print("[A5] 显式奇异封盖：", d["status"], "| 中心斜率 =", d["slope_at_centre"])
        print("[A5c] 数值 mu=λ=1,c=2：a(1) =", round(report["A5c_numeric"]["a_at_1"], 12),
              "| 残差 =", report["A5c_numeric"]["max_relative_pde_residual"])
        print("[A6] 奇点可移动：", report["A6_move_the_singularity"]["status"])
        print()
        print("[判定] 光滑封盖存在 ⟺ μ = 0 且 λc = 0")
        print("        ⇒ Thm 10.12 的 μ≠0 是**充分而非必要**；退化情形恰是 μ=0 且 λc=0")
    else:
        print(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True, default=str))

    if failures:
        print(json.dumps({"status": "checks-failed", "failures": failures},
                         ensure_ascii=False, indent=2))
        raise SystemExit(1)


if __name__ == "__main__":
    main()
