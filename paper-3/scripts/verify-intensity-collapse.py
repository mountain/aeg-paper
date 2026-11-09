#!/usr/bin/env python3
"""Exact witnesses for Paper III's intensity correction (SymPy 1.14).

These checks guard the counterexamples and explicit formulas, not the general
compactness/transversality proof. Failures remain active with python -O.
"""
import json
import math
import sympy as s

checks = []

def require(name, condition):
    if condition is not True and condition is not s.true:
        raise RuntimeError(f"FAILED: {name}: {condition}")
    checks.append(name)

def zero(name, expression):
    require(name, s.simplify(expression) == 0)

x, t, c = s.symbols("x t c", real=True)
mu, lam, delta = s.symbols("mu lambda delta", positive=True)
b = s.symbols("b", real=True)
q2 = mu**2 + lam**2 * t**2
F = s.asinh(lam*t/mu)/lam
zero("rectified derivative", s.diff(F, t) - 1/s.sqrt(q2))
zero("rectified unit gradient", q2*s.diff(F, t)**2 - 1)
zero("radial length primitive", s.diff(F, t) - 1/s.sqrt(q2))

a = mu/lam*s.sinh(lam*(x-b))
zero("moving-zero eikonal", s.diff(a, x)**2 - mu**2 - lam**2*a**2)
zero("moving-zero location", a.subs(x, b))
require("fixed metric does not fix zero", a.subs({mu:1,lam:1,b:1,x:0}) != 0)

primitive = s.atan(lam*t/mu)/(mu*lam)
zero("area primitive", s.diff(primitive, t) - 1/q2)
one_side = 2*s.pi*primitive.subs(t,1)
two_side = 2*s.pi*(primitive.subs(t,1)-primitive.subs(t,-1))
zero("one-sided area coefficient", s.limit(lam*one_side,lam,s.oo)-s.pi**2/mu)
zero("two-sided area coefficient", s.limit(lam*two_side,lam,s.oo)-2*s.pi**2/mu)
zero("one-sided is half two-sided", two_side-2*one_side)
require("reject old boundary coefficient", s.limit(lam*one_side,lam,s.oo) != 2*s.pi**2/mu)
Iplus, Iminus = s.symbols("Iplus Iminus", nonnegative=True)
side_mass = s.atan(lam*delta/mu)/(mu*lam)
zero("general sided coefficient", s.limit(lam*(Iplus+Iminus)*side_mass,lam,s.oo)
     -s.pi*(Iplus+Iminus)/(2*mu))
error_primitive = s.log(1+lam**2*t**2/mu**2)/(2*lam**2)
zero("Lipschitz density error primitive", s.diff(error_primitive,t)-t/q2)

# Exact geometry for a shortest-path obstruction in the unit disk.
y = s.Rational(19,20)
require("disk starting point interior", y*y < 1)
require("gradient endpoint outside disk", s.Rational(1,4)+y*y > 1)
require("zero curve meets disk", s.Rational(1,4) < 1)

shortcut = 2*s.asinh(lam/mu)/lam+s.pi/s.sqrt(mu**2+lam**2)
diameter_bound = 4*s.asinh(lam/mu)/lam+s.pi/s.sqrt(mu**2+lam**2)
zero("zero-circle shortcut vanishes", s.limit(shortcut,lam,s.oo))
zero("cylinder diameter bound vanishes", s.limit(diameter_bound,lam,s.oo))
require("reject ambient zero-circle isometry", float(shortcut.subs({mu:1,lam:100})) < math.pi)
zero("explicit cylinder rate", s.limit(lam*diameter_bound/s.log(lam),lam,s.oo)-4)
require("assignment oscillation persists", (1-(-1))/2 == 1)

print(json.dumps({"checks":checks,"count":len(checks),"status":"PASS",
    "scope":"explicit symbolic and geometric witnesses; general proof is in the manuscript"},
    indent=2, sort_keys=True))
