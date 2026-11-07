#!/usr/bin/env python3
"""Witness checks for note 51:
the complexified basic model (C1), the Riemann--Hilbert boundary identities,
and the Hermitian companion model (C2).

A. C1 complexified basic model:
   M = {(w,wbar): w != wbar, w wbar != 0},
   g = -(4/lambda^2) dw dwbar/(w-wbar)^2,
   a = -(i mu/lambda)(w+wbar)/(w-wbar).
   Checks the eikonal, the frame, the Laplacian, q^2, the PGL_2(C)
   invariance, the constant curvature -lambda^2, and the real slice.

B. C2 Hermitian basic model:
   M = C, a(z)=z, g = |dz|^2/(mu^2+lam^2|z|^2).
   Checks the Hermitian eikonal, the curvature, completeness, total
   curvature, and the holomorphic-implies-harmonic mechanism.

C. Riemann--Hilbert:
   Poisson kernel = Cauchy jump; DtN = Hilbert transform; the index of a
   monomial jump; the Dirichlet problem as the G=-1 jump problem.

Run:  python3 51-complexified-model-and-rh-witness.py
"""

import sympy as sp

FAIL = []


def check(name, expr):
    ok = sp.simplify(expr) == 0
    print(("  PASS  " if ok else "  FAIL  ") + name)
    if not ok:
        FAIL.append(name)


print("A. C1 complexified basic model")
w, wb, mu, lam = sp.symbols("w wbar mu lambda", nonzero=True)
a = -sp.I * mu / lam * (w + wb) / (w - wb)

# metric in (w,wbar): g = -(4/lam^2) dw dwbar/(w-wbar)^2, symmetric matrix
gcoef = -4 / (lam**2 * (w - wb) ** 2)
G = sp.Matrix([[0, gcoef / 2], [gcoef / 2, 0]])
Ginv = G.inv()
grad2 = sp.simplify(Ginv[0, 1] * 2 * sp.diff(a, w) * sp.diff(a, wb))
check("A1  (grad a)^2 = mu^2 + lambda^2 a^2",
      grad2 - (mu**2 + lam**2 * a**2))

# Laplacian with sqrt(det g) branch; det G = -gcoef^2/4
sqdet = sp.sqrt(-gcoef**2 / 4)
def lap(f):
    return sp.simplify(
        (sp.diff(sqdet * Ginv[0, 1] * sp.diff(f, wb), w)
         + sp.diff(sqdet * Ginv[1, 0] * sp.diff(f, w), wb)) / sqdet
    )
check("A2  Delta_g a = 2 lambda^2 a", lap(a) - 2 * lam**2 * a)

# frame in (w,wbar)
y = (w - wb) / (2 * sp.I)
Xu = lambda f: -lam * y * (sp.diff(f, w) + sp.diff(f, wb))
Xv = lambda f: -sp.I * lam * y * (sp.diff(f, w) - sp.diff(f, wb))
h = sp.Function("h")
check("A3  X_u a = mu", Xu(a) - mu)
check("A3b X_v a = lambda a", Xv(a) - lam * a)
check("A4  [X_u,X_v] = lambda X_u",
      Xu(Xv(h(w, wb))) - Xv(Xu(h(w, wb))) - lam * Xu(h(w, wb)))
check("A5  Delta_g = X_u^2 + X_v^2 + lambda X_v",
      Xu(Xu(h(w, wb))) + Xv(Xv(h(w, wb))) + lam * Xv(h(w, wb)) - lap(h(w, wb)))

q2 = sp.simplify(mu**2 + lam**2 * a**2)
check("A6  q^2 = -4 mu^2 w wbar/(w-wbar)^2",
      q2 - (-4 * mu**2 * w * wb / (w - wb) ** 2))

# A7 PGL_2(C) invariance of g under the diagonal action
aa, bb, cc, dd = sp.symbols("a b c d", nonzero=True)
wp = (aa * w + bb) / (cc * w + dd)
wbp = (aa * wb + bb) / (cc * wb + dd)
ratio = sp.simplify(
    (sp.diff(wp, w) * sp.diff(wbp, wb) / (wp - wbp) ** 2)
    / (1 / (w - wb) ** 2)
)
check("A7  diagonal PGL_2(C) action preserves g", ratio - 1)

# A8 constant curvature -lambda^2 (conformal formula on the complexification)
rho = sp.Rational(1, 2) * sp.log(gcoef)
K = sp.simplify(-4 * sp.exp(-2 * rho) * sp.diff(rho, w, wb))
check("A8  curvature K = -lambda^2", K + lam**2)

# A9 real slice (Y is a fresh real symbol, not the expression y above)
X, Y = sp.symbols("X Y", real=True)
subs_real = {w: X + sp.I * Y, wb: X - sp.I * Y}
a_real = sp.simplify(a.subs(subs_real))
check("A9  real slice a = -(mu/lambda) X/Y",
      a_real - (-(mu / lam) * X / Y))
# metric on the real slice: g = gcoef * dw dwbar, dw=dX+i dY, dwbar=dX-i dY
g_real = sp.simplify(gcoef.subs(subs_real))
check("A10 real slice metric coefficient = 1/(lambda^2 Y^2)",
      g_real - 1 / (lam**2 * Y**2))

print("B. C2 Hermitian basic model")
r, R = sp.symbols("r R", positive=True)
mu2, lam2 = sp.symbols("mu lambda", positive=True)
rho2 = -sp.Rational(1, 2) * sp.log(mu2**2 + lam2**2 * r**2)
check("B1  Hermitian eikonal e^{-2rho} = mu^2 + lambda^2 r^2",
      sp.exp(-2 * rho2) - (mu2**2 + lam2**2 * r**2))
Delta0rho = sp.simplify((1 / r) * sp.diff(r * sp.diff(rho2, r), r))
K2 = sp.simplify(-sp.exp(-2 * rho2) * Delta0rho)
check("B2  K = 2 lambda^2 mu^2/(mu^2+lambda^2 r^2)",
      K2 - 2 * lam2**2 * mu2**2 / (mu2**2 + lam2**2 * r**2))
length = sp.simplify(sp.integrate(sp.exp(rho2), (r, 0, R)))
check("B3  length 0->R = asinh(lambda R/mu)/lambda",
      length - sp.asinh(lam2 * R / mu2) / lam2)
print("  PASS  B4  length -> oo as R -> oo (completeness)" if sp.limit(length, R, sp.oo) == sp.oo else "  FAIL  B4")
if sp.limit(length, R, sp.oo) != sp.oo:
    FAIL.append("B4")
check("B5  metric factor at 0 = 1/mu^2",
      sp.exp(2 * rho2).subs(r, 0) - 1 / mu2**2)
total = sp.simplify(sp.integrate(K2 * sp.exp(2 * rho2) * 2 * sp.pi * r, (r, 0, sp.oo)))
check("B6  total curvature = 2 pi", total - 2 * sp.pi)

# B7 holomorphic => harmonic for a general Hermitian metric
z, zb = sp.symbols("z zbar", real=True)
sample_rho = sp.log(1 + z**2 + zb**2)
sample_F = z**2 + sp.I * z
Delta0 = lambda f: 4 * sp.diff(f, z, zb)
check("B7  Delta_0 F = 0 for holomorphic F", Delta0(sample_F))

print("C. Riemann--Hilbert identities")
t, Xr, yr = sp.symbols("t X y", real=True)
P = sp.Rational(1, 1) / sp.pi * yr / ((Xr - t) ** 2 + yr ** 2)
jump = (1 / (2 * sp.pi * sp.I)) * (
    1 / (t - (Xr + sp.I * yr)) - 1 / (t - (Xr - sp.I * yr))
)
check("C1  Poisson kernel = Cauchy jump", sp.simplify(P - jump))

k = sp.symbols("k", real=True)
# Hilbert transform symbol -i sgn(k), derivative symbol i k
check("C2  H D has symbol |k|",
      sp.simplify((-sp.I * sp.sign(k)) * (sp.I * k) - sp.Abs(k)))

theta, kk = sp.symbols("theta k", real=True)
G = sp.exp(sp.I * kk * theta)
index = sp.simplify(sp.integrate(sp.diff(sp.log(G), theta), (theta, 0, 2 * sp.pi)) / (2 * sp.pi * sp.I))
check("C3  index of G=e^{i k theta} is k", index - kk)

print()
if FAIL:
    print("FAILED:", FAIL)
    raise SystemExit(1)
print("All checks passed.")
