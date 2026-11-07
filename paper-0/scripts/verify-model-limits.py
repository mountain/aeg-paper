#!/usr/bin/env python3
"""Symbolic regression checks for the flat limit and complex rank repair.

Requires SymPy. These are identities and finitely many derivative/rank checks,
not a proof of C-infinity convergence, a conic classification, or a Lean audit.
The corresponding general proofs are in Paper 0, Sections 3 and 12.6.
Run normally and with python -O; checks deliberately do not use assert.
"""
import sympy as sp

checks = []


def check(name, condition):
    if not bool(condition):
        raise AssertionError(name)
    checks.append(name)


def zero(name, expression):
    if isinstance(expression, sp.MatrixBase):
        check(name, all(sp.simplify(x) == 0 for x in expression))
    else:
        check(name, sp.simplify(expression) == 0)


u, v = sp.symbols("u v", real=True)
mu, lam = sp.symbols("mu lambda", positive=True)
x, y = sp.symbols("x y", real=True)
phi = sp.Matrix([u, sp.exp(lam * v)])
jac = phi.jacobian([u, v])
g_upper = sp.diag(1 / (mu**2 * y**2), 1 / (lam**2 * y**2))
g = sp.simplify(jac.T * g_upper.subs(y, phi[1]) * jac)
a = (-x / y).subs({x: phi[0], y: phi[1]}, simultaneous=True)
g_expected = sp.diag(sp.exp(-2 * lam * v) / mu**2, 1)
zero("metric pullback by Phi_lambda", g - g_expected)
zero("assignment pullback", a + u * sp.exp(-lam * v))
fields = sp.simplify(jac.inv() * sp.diag(-mu * phi[1], -lam * phi[1]))
zero("frame pullback", fields - sp.diag(-mu * sp.exp(lam * v), -1))
zero("frame is orthonormal", fields.T * g * fields - sp.eye(2))
da = sp.Matrix([sp.diff(a, z) for z in (u, v)])
zero("pulled-back eikonal", (da.T * g.inv() * da)[0] - mu**2 - lam**2 * a**2)
zero("frame acts on assignment", fields.T * da - sp.Matrix([mu, lam * a]))

# Independent curvature calculation from the metric and Christoffel symbols.
coords = (u, v)
ginv = g.inv()
Gamma = [[[sp.simplify(sum(ginv[k, l] * (
    sp.diff(g[l, j], coords[i]) + sp.diff(g[l, i], coords[j])
    - sp.diff(g[i, j], coords[l])) / 2 for l in range(2)))
    for j in range(2)] for i in range(2)] for k in range(2)]
# R^k_{l i j} = d_i Gamma^k_{j l} - d_j Gamma^k_{i l} + products.
def R(k, l, i, j):
    return sp.simplify(sp.diff(Gamma[k][j][l], coords[i])
        - sp.diff(Gamma[k][i][l], coords[j])
        + sum(Gamma[k][i][m] * Gamma[m][j][l]
              - Gamma[k][j][m] * Gamma[m][i][l] for m in range(2)))
K = sp.simplify(sum(g[0, k] * R(k, 1, 0, 1) for k in range(2)) / g.det())
zero("curvature from Christoffel symbols", K + lam**2)
g0 = sp.diag(1 / mu**2, 1)
zero("flat metric limit", g.applyfunc(lambda t: sp.limit(t, lam, 0, dir="+")) - g0)
zero("flat assignment limit", sp.limit(a, lam, 0, dir="+") + u)
zero("flat frame limit", fields.applyfunc(lambda t: sp.limit(t, lam, 0, dir="+"))
     - sp.diag(-mu, -1))
zero("flat eikonal", (sp.Matrix([-1, 0]).T * g0.inv() * sp.Matrix([-1, 0]))[0] - mu**2)
# Finite derivative witnesses only; the manuscript gives the uniform-on-compact proof.
for order in range(1, 5):
    zero(f"exponential derivative formula order {order}",
         sp.diff(sp.exp(-2 * lam * v), v, order)
         - (-2 * lam)**order * sp.exp(-2 * lam * v))
    zero(f"derivative limit order {order}",
         sp.limit(sp.diff(sp.exp(-2 * lam * v), v, order), lam, 0, dir="+"))
check("negative control: fixed-chart vertical coefficient diverges",
      sp.limit(g_upper[1, 1].subs(y, 1), lam, 0, dir="+") == sp.oo)
check("negative control: positive-lambda metric is not flat", K != 0)

# Complex congruence identifies the two nondegenerate signatures, not rank.
Q_real = sp.diag(1, 1, -1)
Q_imaginary = sp.eye(3)
P = sp.diag(1, 1, sp.I)
zero("complex congruence of real and imaginary nonsingular conics",
     P.T * Q_real * P - Q_imaginary)
for rank in (1, 2, 3):
    Q = sp.diag(*([1] * rank + [0] * (3 - rank)))
    check(f"rank-{rank} normal form remains rank {rank} over C", Q.rank() == rank)
    C = sp.Matrix([[1, sp.I, 1], [0, 1, sp.I], [0, 0, 1]])
    check(f"complex congruence preserves rank {rank}", (C.T * Q * C).rank() == rank)
check("negative control: rank-one absolute cannot be nonsingular",
      sp.diag(0, 0, 1).rank() != Q_real.rank())
check("negative control: rank-two absolute cannot be nonsingular",
      sp.diag(1, 1, 0).rank() != Q_real.rank())
J = sp.Matrix([[0, -1], [1, 0]])
check("complexification does not identify exchange lifts", J != -J)
zero("exchange square remains -I", J * J + sp.eye(2))

print(f"PASS: {len(checks)} symbolic/finite model-limit and rank checks.")
for name in checks:
    print("  PASS " + name)
print("Coverage: displayed identities, derivatives through order 4, rank representatives,")
print("and negative controls. General convergence and classification use manuscript proofs.")
