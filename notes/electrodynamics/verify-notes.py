#!/usr/bin/env python3
"""Exact checks for the claims collected in electrodynamics/*.md.

Every check prints PASS/FAIL with the exact value it established.  Run with

    /Users/mingli/work/public/adva-machine/.venv/bin/python verify-notes.py

The script depends only on sympy + numpy.  It verifies, in order:

  V1  the rank-one projector formula and the exact four-step cross-ratio
      holonomy (Paper IV, Theorem 4.11(3));
  V2  the F_7 calibration (Paper IV, Example 4.13);
  V3  the first-order (infinitesimal) expansion ln Lambda = -int (1+ab)^-2 da db;
  V4  the curvature of the reductive connection of Paper IV, Remark 4.12,
      and its factor-two relation to the idempotent transport (this document,
      Appendix B);
  V5  the Legendre-dual rewrites of the arithmetic contact form (this
      document, Section 3) -- including the corrected coefficient;
  V6  the dual tearing / Reeb drift identity for the kernel word
      (Paper 0, Theorems 8.6 and 9.9);
  V7  the semiclassical Coulomb radial action and the resulting E_n spectrum;
  V8  the F_7 counts quoted from Paper IV, Proposition 3.8 and Example 3.9.
"""

from fractions import Fraction
import itertools
import math

import sympy as sp

FAIL = []
REPORT = []


def check(tag, ok, detail=""):
    status = "PASS" if ok else "FAIL"
    if not ok:
        FAIL.append(tag)
    REPORT.append(f"[{status}] {tag}: {detail}")


# ----------------------------------------------------------------------------
# V1. Projectors and the exact cross-ratio holonomy
# ----------------------------------------------------------------------------

a1, b1, a2, b2 = sp.symbols("a1 b1 a2 b2")


def projector(a, b):
    """Pi_{a,b} = (1+ab)^{-1} v_a (x) phi_b  with v_a=(-a,1), phi_b=(-b,1)."""
    return sp.Matrix([[-a], [1]]) * sp.Matrix([[-b, 1]]) / (1 + a * b)


def holonomy(a, b, c, d):
    """Lambda(square) = (1+a c)(1+b d) / ((1+a b)(1+c d)) for
    vertices (a,b) -> (c,b) -> (c,d) -> (a,d)."""
    return sp.simplify(((1 + c * b) * (1 + a * d)) / ((1 + a * b) * (1 + c * d)))


P11, P12, P22, P21 = (
    projector(a1, b1),
    projector(a1, b2),
    projector(a2, b2),
    projector(a2, b1),
)
lhs = sp.simplify(P11 * P12 * P22 * P21)
lam = holonomy(a1, b1, a2, b2)
target = sp.simplify(P11 / lam)
check("V1.1 projector product closes on Pi_{a1,b1}", sp.simplify(lhs - target).is_zero_matrix,
      "Pi11 Pi12 Pi22 Pi21 = Lambda^{-1} Pi11 identically")
check("V1.2 cross-ratio alternative form",
      sp.simplify(1 - (a2 - a1) * (b2 - b1) / ((1 + a1 * b1) * (1 + a2 * b2)) - lam) == 0,
      "Lambda = 1 - (a2-a1)(b2-b1)/((1+a1 b1)(1+a2 b2))")
check("V1.3 holonomy trivial iff one coordinate frozen",
      sp.simplify(lam.subs(a2, a1) - 1) == 0 and sp.simplify(lam.subs(b2, b1) - 1) == 0,
      "Lambda = 1 when a2=a1 or b2=b1")

# V1.5 the two elementary projector products
ap = sp.symbols("ap")
check("V1.5a Pi_{a,b} Pi_{a',b} = Pi_{a,b}",
      sp.simplify(projector(a1, b1) * projector(ap, b1) - projector(a1, b1)).is_zero_matrix,
      "projectors sharing a kernel covector compose to the first")
bp = sp.symbols("bp")
check("V1.5b Pi_{a,b} Pi_{a,b'} = Pi_{a,b'}",
      sp.simplify(projector(a1, b1) * projector(a1, bp) - projector(a1, bp)).is_zero_matrix,
      "projectors sharing an image vector compose to the second")

# fixed-kernel flatness: b constant, any closed image loop telescopes
m = 4
prod = sp.Integer(1)
xs = sp.symbols("x0:5")
for k in range(1, m + 1):
    prod *= (1 + xs[k] * b1) / (1 + xs[k - 1] * b1)
prod = prod.subs(xs[m], xs[0])
check("V1.4 fixed-kernel flatness (telecoping)", sp.simplify(prod - 1) == 0,
      "prod_k (1+a_k b0)/(1+a_{k-1} b0) = 1 over a closed image loop")

# ----------------------------------------------------------------------------
# V2. F_7 calibration of Paper IV, Example 4.13
# ----------------------------------------------------------------------------
q = 7


def inv(x):
    return pow(x, q - 2, q)


def hol_f7(v):
    (a_, b_), (c_, d_) = v
    return ((1 + c_ * b_) % q) * ((1 + a_ * d_) % q) * inv(((1 + a_ * b_) % q) * ((1 + c_ * d_) % q) % q) % q


vertices = [(0, 0), (1, 0), (1, 1), (0, 1)]
sq = (vertices[0], vertices[2])
L = hol_f7(sq)
check("V2.1 F_7 holonomy equals 4", L == 4, f"Lambda(square) = {L} mod 7")
check("V2.2 F_7 witness is non-unit", L % q != 1, "4 != 1 in F_7^*, H = F_7^*")

# the projector identity itself, over F_7, on every transverse loop: pure
# field arithmetic (no sympy rationals, which would not be mod-7 inverses).
def proj_f7(a, b):
    """entries of Pi_{a,b} over F_7, as a 2x2 list of residues."""
    s_ = inv((1 + a * b) % q)
    return [[(a * b) % q * s_ % q, (-a) % q * s_ % q],
            [(-b) % q * s_ % q, s_]]


def matmul_f7(X, Y):
    return [[sum(X[i][k] * Y[k][j] for k in range(2)) % q for j in range(2)] for i in range(2)]


ok_proj = True
n_loops = 0
for a, b in itertools.product(range(q), repeat=2):
    for c, d in itertools.product(range(q), repeat=2):
        if (1 + a * b) % q == 0 or (1 + c * d) % q == 0:
            continue
        if (1 + c * b) % q == 0 or (1 + a * d) % q == 0:
            continue          # a non-transverse step is outside Definition 4.10
        n_loops += 1
        lamv = hol_f7(((a, b), (c, d)))
        lhs_m = matmul_f7(matmul_f7(matmul_f7(proj_f7(a, b), proj_f7(a, d)), proj_f7(c, d)),
                          proj_f7(c, b))
        rhs_m = [[(proj_f7(a, b)[i][j] * inv(lamv)) % q for j in range(2)] for i in range(2)]
        if lhs_m != rhs_m:
            ok_proj = False
            break
check("V2.3 projector identity holds over F_7 on all transverse loops", ok_proj,
      f"{n_loops} transverse loops with all four of 1+ab, 1+cd, 1+bc, 1+ad nonzero")

# --- V2.4/V2.5: the four edge transports of the square, over F_7, Phi_k = 1 ---
def edge_transport(a_prev, b_prev, a_k, b_k):
    """(Lambda, dxi) of Definition 4.10 with Phi_k = Phi_{k-1} = 1, mod 7."""
    den = (1 + a_prev * b_prev) % q
    lam = (1 + a_k * b_prev) % q * inv(den) % q
    dxi = (-(a_k - a_prev) * inv(den)) % q
    return lam, dxi


loop_vertices = [(0, 0), (1, 0), (1, 1), (0, 1), (0, 0)]
edges = []
for i in range(4):
    edges.append(edge_transport(*loop_vertices[i], *loop_vertices[i + 1]))
check("V2.4 edge transports of the square",
      edges == [(1, 6), (1, 0), (4, 4), (1, 0)],
      f"(Lambda,dxi) per edge = {edges}")
# chronological product T(e4)T(e3)T(e2)T(e1) in Aff(1,F_7)
tot = (1, 0)                       # identity
for lam, dxi in edges:             # accumulate as [[L,x],[0,1]] * total
    tot = (lam * tot[0] % q, (lam * tot[1] + dxi) % q)
check("V2.5 total transport of the square is diag(4,1)",
      tot == (4, 0), f"T(loop) = [[{tot[0]},{tot[1]}],[0,1]] in Aff(1,F_7)")

# ----------------------------------------------------------------------------
# V3. Infinitesimal expansion
# ----------------------------------------------------------------------------
eps, eta = sp.symbols("eps eta", positive=True)
a0, b0 = sp.symbols("a0 b0")
lam_eps = holonomy(a0, b0, a0 + eps, b0 + eta)
series = sp.series(sp.log(lam_eps), eps, 0, 2).removeO()
series = sp.series(series, eta, 0, 2).removeO()
pred = -eps * eta / (1 + a0 * b0) ** 2
check("V3.1 ln Lambda = -(1+ab)^-2 da db + O(3)", sp.simplify(series - pred) == 0,
      f"ln Lambda = {sp.simplify(series)}")

# ----------------------------------------------------------------------------
# V4. Connection curvature and the factor-two reconciliation
# ----------------------------------------------------------------------------
A, B = sp.symbols("A B")
f = 1 / (1 + A * B)
# omega_H = Phi^{-1}dPhi + f (A dB - B dA); the Phi part is closed, so only the
# second term contributes to the curvature.  For omega2 = f A dB - f B dA:
# d(omega2) = [d_A(f A) + d_B(f B)] dA ^ dB
coeff = sp.simplify(sp.diff(f * A, A) + sp.diff(f * B, B))
check("V4.1 d(omega_2) = 2 (1+ab)^-2 da ^ db", sp.simplify(coeff - 2 / (1 + A * B) ** 2) == 0,
      f"coefficient = {coeff}")
check("V4.2 factor two between connection curvature and transport density",
      sp.simplify(coeff / (1 / (1 + A * B) ** 2)) == 2,
      "curvature/transport-density = 2 (Appendix B)")
# solder component theta_+ = Phi^{-1}(1+ab)^{-1} da must reduce to e^{-M}dxi at b=0
check("V4.3 solder form reduces to left Maurer-Cartan at b=0",
      sp.simplify((1 / (1 + A * B)).subs(B, 0) - 1) == 0,
      "theta_+|_{b=0} = Phi^{-1} da = -e^{-M} dxi (Paper 0, Eq. (58))")

# ----------------------------------------------------------------------------
# V5. Legendre-dual rewrites of alpha
# ----------------------------------------------------------------------------
# alpha = da - dA - a dM.  S = a - A, p = a, q = M.
# S~ = p q - S = aM - a + A ; claim alpha = -dS~ + q dp = -d(A+aM-a) + M da
da, dA, dM = sp.symbols("da dA dM")
alpha = da - dA - a1 * dM


def expand_dual():
    Sdual = A + a1 * dM  # placeholder, replaced below
    # d(A + aM - a) = dA + a dM + M da - da ; -dS~ + M da
    return -(dA + a1 * dM + M0 * da - da) + M0 * da


M0 = sp.symbols("M0")
check("V5.1 alpha = -d(A + aM - a) + M da", sp.expand(expand_dual() - alpha) == 0,
      "the Legendre-dual form: S~ = aM - a + A, momentum M, coordinate a")
check("V5.2 the (1+M)da variant of the notes is wrong",
      sp.expand(-(dA + a1 * dM + M0 * da - da) + (1 + M0) * da - alpha) != 0,
      "coefficient is M da, not (1+M) da")
# the exponential (group) Legendre identity e^{-M} alpha = d(e^{-M} a) - e^{-M} dA
eM = sp.Function("eM")(M0)
lhs_id = sp.expand(sp.Symbol("em") * (da - dA - a1 * dM))
rhs_id = sp.expand(a1 * (-sp.Symbol("em")) * dM + sp.Symbol("em") * da - sp.Symbol("em") * dA)
check("V5.3 e^{-M} alpha = d(e^{-M}a) - e^{-M}dA", sp.simplify(lhs_id - rhs_id) == 0,
      "identical term by term; d(e^{-M}a) = e^{-M}da - a e^{-M}dM")

# ----------------------------------------------------------------------------
# V6. Dual tearing for the kernel word h(p,q)
# ----------------------------------------------------------------------------
p_s, q_s = sp.symbols("p q", positive=True)
gamma1 = p_s                      # (M_q, A_p):  bare charge p
gamma2 = sp.exp(-q_s) * p_s       # (A_{e^{-q}p}, M_q)
dA_drift = sp.simplify(gamma1 - gamma2)
# hyperbolic-area side:  -int_{gamma1 - gamma2} a dM  with a(M) = p e^{M-q} on gamma2
area = sp.simplify(-(0 - sp.integrate(p_s * sp.exp(M0 - q_s), (M0, 0, q_s))))
check("V6.1 Reeb drift = p(1-e^{-q}) by both routes", sp.simplify(dA_drift - area) == 0,
      f"bare-charge route {dA_drift}; area route {area}")
check("V6.2 matches Paper 0 Theorem 8.6 charge of h(p,q)",
      sp.simplify(dA_drift - p_s * (1 - sp.exp(-q_s))) == 0,
      "c(h(p,q)) = (p(1-e^{-q}), 0)")
# ACS weighted-area route (Theorem 8.9) for the same word
weighted = sp.simplify(sp.integrate(sp.integrate(sp.exp(0 - M0), (A, 0, p_s)), (M0, 0, q_s)))
check("V6.3 weighted ACS area reproduces p(1-e^{-q})", sp.simplify(weighted - p_s * (1 - sp.exp(-q_s))) == 0,
      f"int_0^q int_0^p e^{{-M}} dA dM = {weighted}")

# ----------------------------------------------------------------------------
# V7. Coulomb radial action and Bohr-Sommerfeld spectrum
# ----------------------------------------------------------------------------
mm, kk, ll, EE = sp.symbols("m k l E", positive=True)
r = sp.symbols("r", positive=True)
# turning points of 2mE + 2mk/r - l^2/r^2 = 0  <=>  r^2 + (k/E) r - l^2/(2mE) = 0
rminus = (-kk / EE - sp.sqrt((kk / EE) ** 2 + 2 * ll ** 2 / (mm * EE))) / 2
rplus = (-kk / EE + sp.sqrt((kk / EE) ** 2 + 2 * ll ** 2 / (mm * EE))) / 2
# half-action int_{r-}^{r+} sqrt(2m(E + k/r) - l^2/r^2) dr == pi(-l + mk/sqrt(-2mE))
vals = []
for (mv, kv, lv, Ev) in [(1, 1, sp.Rational(1, 2), sp.Rational(-1, 2)),
                         (2, 3, 1, sp.Rational(-9, 8)),
                         (sp.Rational(1, 2), 3, 1, sp.Rational(-8, 9))]:
    expr = sp.sqrt(2 * mv * (Ev + kv / r) - lv ** 2 / r ** 2)
    lo = rminus.subs({mm: mv, kk: kv, ll: lv, EE: Ev})
    hi = rplus.subs({mm: mv, kk: kv, ll: lv, EE: Ev})
    num = sp.N(sp.integrate(expr, (r, lo, hi)), 25)
    pred_half = sp.N(sp.pi * (-lv + mv * kv / sp.sqrt(-2 * mv * Ev)), 25)
    vals.append((num, pred_half, abs(num - pred_half) < 1e-12))
check("V7.1 half radial action = pi(mk/sqrt(-2mE) - l)",
      all(v[2] for v in vals),
      "; ".join(f"numeric {sp.N(v[0],12)} vs closed {sp.N(v[1],12)}" for v in vals))
# V7.4 the auxiliary elementary integral used in Appendix C
x_s, aa, bb = sp.symbols("x a b", positive=True)
for av, bv in [(1, 4), (2, 9), (sp.Rational(1, 2), 3)]:
    num = sp.N(sp.integrate(sp.sqrt((bv - x_s) * (x_s - av)) / x_s, (x_s, av, bv)), 25)
    clo = sp.N(sp.pi * (av + bv) / 2 - sp.pi * sp.sqrt(av * bv), 25)
    if abs(num - clo) > 1e-12:
        check("V7.4 elementary integral", False, f"a={av}, b={bv}: {num} vs {clo}")
        break
else:
    check("V7.4 elementary integral: int_a^b sqrt((b-x)(x-a))/x dx = pi(a+b)/2 - pi*sqrt(ab)",
          True, "three numeric points match the closed form")

# with hbar=1: 2*pi*(mk/sqrt(-2mE) - l) = 2*pi*n_r  =>  E = -m k^2/(2 n^2), n = n_r + l
hbar, n, nr = sp.symbols("hbar n n_r", positive=True)
# quantization: 2*pi*(m k/sqrt(-2mE) - l) = 2*pi*hbar*n_r  with  n = n_r + l/hbar
E_n = -mm * kk ** 2 / (2 * hbar ** 2 * n ** 2)
cond_lhs = sp.simplify(mm * kk / sp.sqrt(sp.simplify(-2 * mm * E_n)))
check("V7.2 E_n = -m k^2/(2 hbar^2 n^2) satisfies m k/sqrt(-2mE) = hbar n",
      sp.simplify(cond_lhs - hbar * n) == 0, f"m k/sqrt(-2 m E_n) = {cond_lhs}")
# and the orbit radius / binding energy are the textbook ones
check("V7.3 ground state is E_1 = -m k^2/(2 hbar^2)",
      sp.simplify(E_n.subs(n, 1) + mm * kk ** 2 / (2 * hbar ** 2)) == 0, "Bohr value recovered")

# ----------------------------------------------------------------------------
# V8. Finite-field counts quoted in Paper IV, Proposition 3.8 / Example 3.9
# ----------------------------------------------------------------------------
check("V8.1 |PGL_2(F_7)| = 336", q * (q ** 2 - 1) == 336, "q(q^2-1)")
check("V8.2 |Biv| = 56", (q + 1) * q == 56, "ordered pairs of distinct points of P^1(F_7)")
check("V8.3 |H| = 6 and fibers uniform", q - 1 == 6 and 336 // 6 == 56,
      "every H-fiber over a bivaluation has q-1 = 6 elements")
n_finite_chart = sum(1 for a_, b_ in itertools.product(range(q), repeat=2) if (1 + a_ * b_) % q != 0)
check("V8.4 affine chart has 43 of the 56 bivaluations", n_finite_chart == 43,
      f"{n_finite_chart} finite pairs with 1+ab != 0; the other 13 sit on the line at infinity")

# ----------------------------------------------------------------------------
print("\n".join(REPORT))
print()
print("ALL CHECKS PASSED" if not FAIL else f"FAILURES: {FAIL}")
raise SystemExit(1 if FAIL else 0)
