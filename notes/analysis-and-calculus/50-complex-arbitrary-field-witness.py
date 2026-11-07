#!/usr/bin/env python3
"""Witness checks for note 50: complex and arbitrary-field extensions of Paper II.

The script has five independent parts.

A. The complexified basic hyperbolic model over C:
   g = (1/y^2)(dx^2/mu^2 + dy^2/lambda^2) as a *complex bilinear* form,
   a = -x/y, and the complex-bilinear eikonal (grad a)^2 = mu^2 + lambda^2 a^2.
   Also the (w, wbar) form of the same model and the localization of the
   degeneracy divisor q^2 = 0.

B. The algebraic (Weyl-algebra) identity behind Paper II, Theorem 3.14:
   4 dbar^T dbar = -Delta, with no conjugation, no measure, and no positivity.
   Verified both abstractly (central structure functions) and on a concrete
   non-coordinate frame with c_v != 0.

C. The finite-field trichotomy for PGL_2(F_q), q = 3, 5, 7, 11, 13:
   discriminant square / zero / nonsquare against the number of rational
   fixed points, and the criterion "q^2 = a^2 + 1 splits iff q = 1 mod 4".

D. Boundary-kernel and complex-length identities:
   P_y(X-t) = (1/(2 pi i)) (1/(t-w) - 1/(t-wbar)), and
   tau/2 = cosh(l/2) with l = log(kappa).

E. Paper V's field-dependent quadratic types and exchange lifts:
   exact rational/complex witnesses, characteristic-two counterexamples, and
   literal equality versus projective equality versus GL/SL conjugacy.

Run:  python3 50-complex-arbitrary-field-witness.py
"""

import sympy as sp

FAIL = []


def check(name, expr):
    ok = sp.simplify(expr) == 0
    print(("  PASS  " if ok else "  FAIL  ") + name)
    if not ok:
        FAIL.append(name)


print("A. Complexified basic model over C")
x, y, mu, lam = sp.symbols("x y mu lambda", nonzero=True)
a = -x / y
g = sp.Matrix([[1 / (mu**2 * y**2), 0], [0, 1 / (lam**2 * y**2)]])
ginv = g.inv()
grad2 = ginv[0, 0] * sp.diff(a, x) ** 2 + ginv[1, 1] * sp.diff(a, y) ** 2
check("A1  (grad a)^2 = mu^2 + lambda^2 a^2  (complex bilinear)",
      grad2 - (mu**2 + lam**2 * a**2))

sqdet = 1 / (mu * lam * y**2)


def lap(f):
    return sp.simplify(
        (sp.diff(sqdet * ginv[0, 0] * sp.diff(f, x), x)
         + sp.diff(sqdet * ginv[1, 1] * sp.diff(f, y), y)) / sqdet
    )


check("A2  Delta_g a = 2 lambda^2 a", lap(a) - 2 * lam**2 * a)

Xu = lambda f: -mu * y * sp.diff(f, x)
Xv = lambda f: -lam * y * sp.diff(f, y)
h = sp.Function("h")
check("A3  [X_u, X_v] = lambda X_u",
      Xu(Xv(h(x, y))) - Xv(Xu(h(x, y))) - lam * Xu(h(x, y)))
check("A4  Delta_g = X_u^2 + X_v^2 + lambda X_v",
      Xu(Xu(h(x, y))) + Xv(Xv(h(x, y))) + lam * Xv(h(x, y)) - lap(h(x, y)))
check("A5  X_u a = mu, X_v a = lambda a",
      sp.simplify(Xu(a)) - mu)
check("A5b X_v a = lambda a", sp.simplify(Xv(a)) - lam * a)

# (w, wbar) form: w = X + i y, wbar = X - i y
w, wb = sp.symbols("w wbar")
Xw = (w + wb) / 2
yw = (w - wb) / (2 * sp.I)
a_w = sp.simplify(-(mu / lam) * Xw / yw)
check("A6  a = -i mu/lambda (w+wbar)/(w-wbar)",
      a_w - (-sp.I * mu / lam * (w + wb) / (w - wb)))
q2 = sp.simplify(mu**2 + lam**2 * a_w**2)
check("A7  mu^2 + lambda^2 a^2 = -4 mu^2 w wbar/(w-wbar)^2",
      q2 - (-4 * mu**2 * w * wb / (w - wb) ** 2))

J = sp.Matrix([[sp.Rational(1, 2), sp.Rational(1, 2)],
               [1 / (2 * sp.I), -1 / (2 * sp.I)]])
G = sp.Matrix([[1 / (lam**2 * yw**2), 0], [0, 1 / (lam**2 * yw**2)]])
Gw = sp.simplify(J.T * G * J)
check("A8  g = -(4/lambda^2) dw dwbar/(w-wbar)^2",
      Gw[0, 1] - (-2 / (lam**2 * (w - wb) ** 2)))
Gwinv = Gw.inv()
grad2w = sp.simplify(
    Gwinv[0, 0] * sp.diff(a_w, w) ** 2
    + Gwinv[0, 1] * sp.diff(a_w, w) * sp.diff(a_w, wb)
    + Gwinv[1, 0] * sp.diff(a_w, wb) * sp.diff(a_w, w)
    + Gwinv[1, 1] * sp.diff(a_w, wb) ** 2
)
check("A9  eikonal in (w,wbar)", grad2w - (mu**2 + lam**2 * a_w**2))

# A10: dbar = -lambda y d_wbar, with X_u, X_v written in (w, wbar)
F = sp.Function("F")
Xu_w = lambda f: -lam * yw * (sp.diff(f, w) + sp.diff(f, wb))
Xv_w = lambda f: -sp.I * lam * yw * (sp.diff(f, w) - sp.diff(f, wb))
check("A10 (X_u + i X_v)/2 = -lambda y d_wbar",
      sp.simplify((Xu_w(F(w, wb)) + sp.I * Xv_w(F(w, wb))) / 2
                  + lam * yw * sp.diff(F(w, wb), wb)))

print("B. Algebraic Paper II identity (Weyl algebra, no conjugation)")

# B1: abstract check with central structure functions
Ssym, Xus, Xvs, cu_s, cv_s = sp.symbols("S Xu Xv c_u c_v")
I = sp.I
lhs = -Ssym - I * (cu_s * Xus + cv_s * Xvs) + (cv_s + I * cu_s) * (Xus + I * Xvs)
rhs = -(Ssym - cv_s * Xus + cu_s * Xvs)  # -Delta
check("B1  4 dbar^T dbar = -Delta (central structure functions)",
      lhs - rhs)

# B2: concrete non-coordinate frame with c_v != 0:
#     X_u = d_x + y^2 d_y,  X_v = d_y,  [X_u,X_v] = -2y X_v
xx, yy = sp.symbols("x y", real=True)
qfun = yy**2
Xu2 = lambda f: sp.diff(f, xx) + qfun * sp.diff(f, yy)
Xv2 = lambda f: sp.diff(f, yy)
cu2, cv2 = sp.Integer(0), -sp.diff(qfun, yy)
gg = sp.Function("g")
d2 = lambda f: (Xu2(f) - sp.I * Xv2(f)) / 2
db2 = lambda f: (Xu2(f) + sp.I * Xv2(f)) / 2
db2T = lambda f: sp.simplify(-d2(f) + (cv2 + sp.I * cu2) / 2 * f)


def delta2(f):
    return sp.simplify(Xu2(Xu2(f)) + Xv2(Xv2(f)) - cv2 * Xu2(f) + cu2 * Xv2(f))


check("B2  concrete frame: 4 dbar^T dbar = -Delta",
      4 * db2T(db2(gg(xx, yy))) + delta2(gg(xx, yy)))
check("B3  concrete frame: bracket = c_u X_u + c_v X_v",
      Xu2(Xv2(gg(xx, yy))) - Xv2(Xu2(gg(xx, yy)))
      - (cu2 * Xu2(gg(xx, yy)) + cv2 * Xv2(gg(xx, yy))))

print("C. Finite-field trichotomy for PGL_2(F_q)")


def inv(a, q):
    return pow(a, -1, q)


def pgl_elements(q):
    reps = set()
    for a in range(q):
        for b in range(q):
            for c in range(q):
                for d in range(q):
                    if (a * d - b * c) % q == 0:
                        continue
                    for v in (a, b, c, d):
                        if v % q:
                            k = inv(v, q)
                            break
                    reps.add(tuple((k * z) % q for z in (a, b, c, d)))
    return reps


def mobius(M, z, q):
    a, b, c, d = M
    if z is None:
        return None if c % q == 0 else (a * inv(c, q)) % q
    den = (c * z + d) % q
    return None if den == 0 else ((a * z + b) % q * inv(den, q)) % q


def fixed_points(M, q):
    return [z for z in list(range(q)) + [None] if mobius(M, z, q) == z]


def sqclass(v, q):
    v %= q
    if v == 0:
        return 0
    return 1 if any((t * t) % q == v for t in range(1, q)) else -1


for q in (3, 5, 7, 11, 13):
    reps = pgl_elements(q)
    counts = {"split": 0, "parabolic": 0, "nonsplit": 0}
    bad = 0
    for M in reps:
        a0, b0, c0, d0 = M
        tr = (a0 + d0) % q
        det = (a0 * d0 - b0 * c0) % q
        disc = (tr * tr - 4 * det) % q
        sc = sqclass(disc, q)
        typ = "parabolic" if sc == 0 else ("split" if sc == 1 else "nonsplit")
        counts[typ] += 1
        n = len(fixed_points(M, q))
        if M != (1, 0, 0, 1) and n != {"split": 2, "parabolic": 1, "nonsplit": 0}[typ]:
            bad += 1
    ok = bad == 0
    print(("  PASS  " if ok else "  FAIL  ")
          + f"C q={q:2d}: |PGL_2|={len(reps):5d}  split={counts['split']:4d}"
            f" parabolic={counts['parabolic']:3d} nonsplit={counts['nonsplit']:4d}"
            f"  fixed-point mismatches={bad}")
    if not ok:
        FAIL.append(f"C q={q}")
    split_eikonal = sqclass(-1, q) == 1
    check(f"C q={q:2d}: -1 is square iff q = 1 mod 4",
          int(split_eikonal) - int(q % 4 == 1))
    print(f"         -1 square in F_q: {sqclass(-1, q):+d} "
          f"(q mod 4 = {q % 4}); eikonal a^2+1 splits: {split_eikonal}")

print("D. Cauchy/Poisson and complex length")
t = sp.symbols("t", real=True)
X = sp.symbols("X", real=True)
P = (1 / sp.pi) * y / ((X - t) ** 2 + y ** 2)
jump = (1 / (2 * sp.pi * sp.I)) * (1 / (t - (X + sp.I * y)) - 1 / (t - (X - sp.I * y)))
check("D1  Poisson kernel = Cauchy jump", sp.simplify(P - jump))

ell = sp.symbols("ell")
check("D2  tau/2 = cosh(ell/2) with eigenvalues exp(+-ell/2)",
      sp.simplify((sp.exp(ell / 2) + sp.exp(-ell / 2)) / 2 - sp.cosh(ell / 2)))
import math
D3 = all(abs(2 * math.acosh((math.exp(l / 2) + math.exp(-l / 2)) / 2) - l) < 1e-12
         for l in (0.3, 1.0, 2.5, 5.0))
print(("  PASS  " if D3 else "  FAIL  ") + "D3  ell = 2 arccosh(tau/2) (numeric)")
if not D3:
    FAIL.append("D3")

print("E. Paper V: quadratic types and distinct exchange lifts")


def check_matrix(name, expr):
    # Check every entry; a trace or sum of entries could conceal cancellation.
    check(name, int(any(sp.simplify(entry) != 0 for entry in expr)))


z = sp.symbols("z")
poly_q = sp.Poly(z**2 + 1, z, domain=sp.QQ)
check("E1  X^2+1 is irreducible over Q (not just over R)",
      int(not poly_q.is_irreducible))
check("E2  X^2+1 splits over C", (z - sp.I) * (z + sp.I) - (z**2 + 1))
poly_f2 = sp.Poly(z**2 + z + 1, z, modulus=2)
check("E3  characteristic two: irreducible quadratic with square discriminant",
      int(not (poly_f2.is_irreducible and int(poly_f2.discriminant()) % 2 == 1)))

Jlift = sp.Matrix([[0, -1], [1, 0]])
eye2 = sp.eye(2)
check_matrix("E4  J^2 = -I over Q, R and C", Jlift**2 + eye2)
check_matrix("E5  J^(-1) = -J", Jlift.inv() + Jlift)
check("E6  J != -J and -I != I, even over C",
      int(not (Jlift != -Jlift and -eye2 != eye2)))
# The two nonzero output vectors differ but have zero wedge product.
t0, s0 = sp.symbols("t0 s0")
point = sp.Matrix([t0, s0])
check("E7  J and -J induce the same projective map",
      sp.Matrix.hstack(Jlift * point, -Jlift * point).det())

H = sp.diag(1, -1)
check_matrix("E8  real GL conjugacy: H J H^(-1) = -J",
             H * Jlift * H.inv() + Jlift)
u, v, r, s = sp.symbols("u v r s", real=True)
Pgeneral = sp.Matrix([[u, v], [r, s]])
solutions = sp.linsolve(list(Pgeneral * Jlift + Jlift * Pgeneral), (u, v, r, s))
check("E9  every conjugator has P = [[u,v],[v,-u]]",
      int(solutions != sp.FiniteSet((-s, r, r, s))))
Panti = sp.Matrix([[u, v], [v, -u]])
check("E10 real conjugator determinant = -(u^2+v^2)",
      Panti.det() + u**2 + v**2)
# Nonpositivity excludes determinant 1; invertibility makes it strictly negative.
check("E11 no real SL conjugator", int(Panti.det().is_nonpositive is not True))
Cconj = sp.I * H
check("E12 complex conjugator iH has determinant one", Cconj.det() - 1)
check_matrix("E13 complex SL conjugacy: (iH) J (iH)^(-1) = -J",
             Cconj * Jlift * Cconj.inv() + Jlift)

for q in (3, 5, 7, 11, 13):
    isotropic = any((a0*a0 + b0*b0) % q == 0
                    for a0 in range(q) for b0 in range(q) if (a0, b0) != (0, 0))
    check(f"E q={q:2d}: anisotropy iff -1 is a nonsquare",
          int(not isotropic) - int(sqclass(-1, q) == -1))
    check(f"E q={q:2d}: the lifts remain literally distinct",
          int(Jlift.applyfunc(lambda x: x % q) == (-Jlift).applyfunc(lambda x: x % q)))
    pairs = [(a0, b0) for a0 in range(q) for b0 in range(q)
             if (-a0*a0 - b0*b0) % q == 1]
    check(f"E q={q:2d}: SL conjugator exists even in the anisotropic cases",
          int(not pairs))
    if pairs:
        a0, b0 = pairs[0]
        Pq = sp.Matrix([[a0, b0], [b0, -a0]])
        check_matrix(f"E q={q:2d}: conjugator identity",
                     (Pq * Jlift + Jlift * Pq).applyfunc(lambda x: x % q))

P7 = sp.Matrix([[3, 2], [2, -3]])
check("E14 printed F_7 conjugator has determinant one", (P7.det() - 1) % 7)
check_matrix("E15 printed F_7 conjugator anticommutes with J", P7 * Jlift + Jlift * P7)
check_matrix("E16 characteristic two: J = -J", (2 * Jlift).applyfunc(lambda x: x % 2))
check_matrix("E17 characteristic two: J^2 = I", (Jlift**2 - eye2).applyfunc(lambda x: x % 2))

# The parabolic conjugate fixes zero, not 1/2; infinity maps to -1.
SAS = sp.cancel(-1 / (-1 / z + 1))
check("E18  S A S(z) = z/(1-z)", SAS - z / (1 - z))
check("E19  fixed-point equation is z^2/(1-z) = 0",
      sp.cancel((SAS - z) * (1 - z)) - z**2)
check("E20  S A S fixes 0 and does not fix 1/2",
      int(not (SAS.subs(z, 0) == 0 and SAS.subs(z, sp.Rational(1, 2)) != sp.Rational(1, 2))))
check("E21  infinity is not fixed", sp.limit(SAS, z, sp.oo) + 1)

print()
if FAIL:
    print("FAILED:", FAIL)
    raise SystemExit(1)
print("All checks passed.")
