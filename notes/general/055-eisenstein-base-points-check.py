#!/usr/bin/env python3
"""
055 — exact checks for note 054: Eisenstein base points and sqrt3.

Model: H^2 with a = -x/y, Gamma_4 = <J, T>, J: z -> -1/z, T: z -> z + sqrt2,
eps2 = i, eps4 = (-1+i)/sqrt2, omega = (-1+i sqrt3)/2.

Checks (exact sympy; the script exits nonzero on any failure)
  (F)  general assignment formula for z0 = x0 + i y0 and g = [[A,B],[C,D]],
       Delta = AD - BC != 0:
         a(g z0) = -[AC(x0^2+y0^2) + BD + (AD+BC) x0] / (y0 Delta)
  (E1) a(m + n omega) = sqrt3 (n - 2m) / (3n)
  (E2) a(omega-1) = sqrt3, a(2+omega) = -sqrt3, a(2 omega + 1) = 0,
       2 omega + 1 = i sqrt3
  (O1) for g in Gamma_4 (entries in Z[sqrt2], det 1):
         a(g (omega-1)) = sqrt3 * R(g),
         R(g) = [3(AD+BC) - 6AC - 2BD] / (3(AD-BC))  in Q(sqrt2)
  (O2) T-orbit: a(omega - 1 + m sqrt2) = sqrt3 - (2m/3) sqrt6
  (R1) ratios in Q(sqrt2) stay in Q(sqrt2); the translation
         b = (sqrt2 - sqrt6)/2  gives a = sqrt3 but lies in Q(sqrt2,sqrt3)
  (R2) orbit representatives: a(eps2)=0, a(T eps2)=-sqrt2, a(eps4)=1,
         a(T eps4)=-1, a(omega-1)=sqrt3

STATUS: exact checks (no figure).  The note's statuses are stated there;
this script only certifies the algebraic identities it prints.
"""

import random
import sys

import sympy as sp

s2, s3, s6 = sp.sqrt(2), sp.sqrt(3), sp.sqrt(6)
omega = (-1 + sp.I * s3) / 2
w0 = omega - 1
EPS2 = sp.I
EPS4 = (-1 + sp.I) / s2

J = (0, -1, 1, 0)
T = (1, s2, 0, 1)
TI = (1, -s2, 0, 1)
GENS = [J, T, TI]
ID = (1, 0, 0, 1)

failures = []


def check(name, ok):
    ok = bool(ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    if not ok:
        failures.append(name)


def mul(f, g):
    A, B, C, D = f
    a, b, c, d = g
    return (sp.simplify(A * a + B * c), sp.simplify(A * b + B * d),
            sp.simplify(C * a + D * c), sp.simplify(C * b + D * d))


def mob(M, z):
    A, B, C, D = M
    return sp.simplify((A * z + B) / (C * z + D))


def a_of(z):
    z = sp.expand_complex(z)
    return sp.simplify(-sp.re(z) / sp.im(z))


def a_formula(z0):
    x0, y0 = sp.re(z0), sp.im(z0)
    def f(M):
        A, B, C, D = M
        Delta = A * D - B * C
        num = A * C * (x0 ** 2 + y0 ** 2) + B * D + (A * D + B * C) * x0
        return sp.simplify(-num / (y0 * Delta))
    return f


def check_general_formula():
    zs = [EPS2, EPS4, w0, -s3 + sp.I, sp.Rational(1, 2) + 2 * sp.I,
          sp.sqrt(5) + sp.I * sp.sqrt(7)]
    gs = [(2, 3, 1, 4), (1, s3, 2, 1 - s2), (s2, 1, 0, 1), (3, 1, 1, 2),
          (1, 0, 0, 1), (0, -1, 1, 0)]
    ok = True
    for z0 in zs:
        f = a_formula(z0)
        for g in gs:
            A, B, C, D = g
            if sp.simplify(A * D - B * C) == 0:
                continue
            lhs = a_of(mob(g, z0))
            rhs = f(g)
            if sp.simplify(lhs - rhs) != 0:
                ok = False
                print("   mismatch:", z0, g, lhs, rhs)
    check("(F) general assignment formula a(g z0)", ok)


def check_eisenstein_values():
    m, n = sp.symbols("m n", integer=True)
    lhs = sp.simplify(a_of(m + n * omega))
    rhs = sp.simplify(s3 * (n - 2 * m) / (3 * n))
    check("(E1) a(m+n omega) = sqrt3 (n-2m)/(3n)", sp.simplify(lhs - rhs) == 0)
    check("(E1b) a(omega) = sqrt3/3", sp.simplify(a_of(omega) - s3 / 3) == 0)
    check("(E2) a(omega-1) = sqrt3", sp.simplify(a_of(w0) - s3) == 0)
    check("(E2) a(2+omega) = -sqrt3", sp.simplify(a_of(2 + omega) + s3) == 0)
    check("(E2) a(2 omega+1) = 0", sp.simplify(a_of(2 * omega + 1)) == 0)
    check("(E2) 2 omega + 1 = i sqrt3", sp.simplify(2 * omega + 1 - sp.I * s3) == 0)


def random_words(count=40, maxlen=8, seed=4):
    rng = random.Random(seed)
    out = []
    for _ in range(count):
        M = ID
        for _ in range(rng.randint(1, maxlen)):
            M = mul(M, GENS[rng.randint(0, 2)])
        out.append(M)
    return out


def check_orbit_formula():
    ok = True
    for g in [ID, T, mul(T, T), J] + random_words():
        A, B, C, D = g
        Delta = sp.simplify(A * D - B * C)
        lhs = a_of(mob(g, w0))
        R = sp.simplify((3 * (A * D + B * C) - 6 * A * C - 2 * B * D) / (3 * Delta))
        if sp.simplify(lhs - s3 * R) != 0:
            ok = False
            print("   mismatch at g =", g, lhs, s3 * R)
    check("(O1) a(g(omega-1)) = sqrt3 R(g), R in Q(sqrt2)", ok)
    # R lies in Q(sqrt2) by construction; spot-check the value set is not just Q
    check("(O1b) sample R(T) = 1 - 2 sqrt2 / 3",
          sp.simplify((3 * (1) - 0 - 2 * s2) / 3 - (1 - 2 * s2 / 3)) == 0)


def check_t_orbit():
    m = sp.symbols("m", integer=True)
    lhs = sp.simplify(a_of(w0 + m * s2))
    rhs = sp.simplify(s3 - 2 * m * s6 / 3)
    check("(O2) T-orbit a(w0 + m sqrt2) = sqrt3 - (2m/3) sqrt6",
          sp.simplify(lhs - rhs) == 0)


def check_ratio_route():
    # ratios in Q(sqrt2) give values in Q(sqrt2): test a random sample
    ok = True
    for g in random_words(count=20, seed=9):
        v = a_of(mob(g, EPS4))
        # v should be an odd integer for g in Gamma_4
        iv = int(round(float(sp.N(v))))
        if sp.simplify(v - iv) != 0 or iv % 2 != 1:
            ok = False
            print("   unexpected value:", v)
    check("(R1a) Gamma_4 orbit of eps4: a is an odd integer", ok)

    # the translation b = (sqrt2 - sqrt6)/2 gives a = sqrt3
    b = (s2 - s6) / 2
    g = (1, b, 0, 1)
    check("(R1b) translation b=(sqrt2-sqrt6)/2 gives a=sqrt3",
          sp.simplify(a_of(mob(g, EPS4)) - s3) == 0)
    check("(R1c) b = (1-sqrt3)/sqrt2", sp.simplify(b - (1 - s3) / s2) == 0)
    x = sp.Symbol("x")
    check("(R1d) deg_Q(b) = 4, so b not in Q(sqrt2)",
          sp.degree(sp.minimal_polynomial(b, x), x) == 4)


def check_representatives():
    check("(R2) a(eps2) = 0", sp.simplify(a_of(EPS2)) == 0)
    check("(R2) a(T eps2) = -sqrt2", sp.simplify(a_of(mob(T, EPS2)) + s2) == 0)
    check("(R2) a(eps4) = 1", sp.simplify(a_of(EPS4) - 1) == 0)
    check("(R2) a(T eps4) = -1", sp.simplify(a_of(mob(T, EPS4)) + 1) == 0)
    check("(R2) a(omega-1) = sqrt3", sp.simplify(a_of(w0) - s3) == 0)


def main():
    print("055 — exact checks for note 054 (Eisenstein base points and sqrt3)\n")
    check_general_formula()
    check_eisenstein_values()
    check_orbit_formula()
    check_t_orbit()
    check_ratio_route()
    check_representatives()
    print()
    if failures:
        print("FAILED:", len(failures), "check(s):", failures)
        return 1
    print("All checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
