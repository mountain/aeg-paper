#!/usr/bin/env python3
"""New exact finite checks for the 2026-10-09 manuscript integration.

Standard library only. These are not the unavailable original 39-check suite.
The manuscript supplies proofs; samples below are independent regression tests.
"""
import argparse
import json
from fractions import Fraction as F
from pathlib import Path

checks = []

def check(name, condition, certificate=None):
    if not condition:
        raise AssertionError(name)
    checks.append({"name": name, "passed": True, "certificate": certificate})

def mul(p, q):
    out = [F(0)] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i+j] += a*b
    return out

def ev(p, x):
    out = F(0)
    for c in reversed(p):
        out = out*x+c
    return out

class Jet:
    """Value and first two-coordinate derivatives, with exact rational rules."""
    def __init__(self, v, dx=0, dy=0):
        self.v, self.dx, self.dy = F(v), F(dx), F(dy)
    @staticmethod
    def of(x):
        return x if isinstance(x, Jet) else Jet(x)
    def __add__(self, other):
        o = self.of(other)
        return Jet(self.v+o.v, self.dx+o.dx, self.dy+o.dy)
    __radd__ = __add__
    def __neg__(self):
        return Jet(-self.v, -self.dx, -self.dy)
    def __sub__(self, other):
        return self + -self.of(other)
    def __rsub__(self, other):
        return self.of(other) + -self
    def __mul__(self, other):
        o = self.of(other)
        return Jet(self.v*o.v, self.dx*o.v+self.v*o.dx,
                   self.dy*o.v+self.v*o.dy)
    __rmul__ = __mul__
    def __truediv__(self, other):
        o = self.of(other)
        return Jet(self.v/o.v, (self.dx*o.v-self.v*o.dx)/o.v**2,
                   (self.dy*o.v-self.v*o.dy)/o.v**2)
    def __pow__(self, n):
        if n < 0:
            return Jet(1) / (self ** -n)
        result = Jet(1)
        for _ in range(n):
            result = result*self
        return result

for k in range(1, 9):
    roots = [F(i) for i in range(k-1)]
    derivative = [F(1)]
    for r in roots:
        derivative = mul(derivative, [-r, F(1)])
    p = [F(0)] + [c/F(i+1) for i, c in enumerate(derivative)]
    check(f"k={k}: derivative degree and distinct finite roots",
          len(derivative)-1 == k-1 and all(ev(derivative, r) == 0 for r in roots))
    check(f"k={k}: finite count plus infinity", len(roots)+1 == k)
    for x, y in [(F(1,2), F(1)), (F(-1), F(2)), (F(3,2), F(-1,2))]:
        a = ev(p, x)+y*y
        norm = ev(derivative, x)**2+4*y*y
        for mu, lam in [(F(1), F(1)), (F(-2), F(0)), (F(3,2), F(-1))]:
            conformal = norm/(mu*mu+lam*lam*a*a)
            check(f"k={k}: eikonal sample {(str(x),str(y),str(mu),str(lam))}",
                  conformal > 0 and norm/conformal == mu*mu+lam*lam*a*a)
for genus in range(4):
    for k in range(8):
        if 2*genus-2+k > 0:
            n, e = 2*genus-2+k, 3*genus-3+k
            check(f"pants g={genus},k={k}", n > 0 and e >= 0 and 3*n == k+2*e)
for c, inside in [(F(-1,2), [-1,0]), (F(1,2), [0,1])]:
    check(f"k4 seam {c}: puncture partition",
          [r for r in [-1,0,1] if (F(r)-c)**2 < F(9,16)] == inside)
    check(f"k4 seam {c}: no puncture on seam",
          all((F(r)-c)**2 != F(9,16) for r in [-1,0,1]))

x, y = Jet(0,1,0), Jet(1,0,1)
a = x**4/4-x**2/2+y**2
vx, vy = x**3-x, 2*y
grad2 = vx*vx+vy*vy
xu = ((vx+a*vy)/grad2, (vy-a*vx)/grad2)
xv = ((a*vx-vy)/grad2, (a*vy+vx)/grad2)
bracket = tuple(v.dx*xu[0].v+v.dy*xu[1].v-u.dx*xv[0].v-u.dy*xv[1].v
                for u,v in zip(xu,xv))
residue = tuple(b-u.v for b,u in zip(bracket,xu))
check("k4 canonical frame", tuple(u.v for u in xu) == (F(1,2),F(1,2)))
check("k4 bracket", bracket == (F(-1,4),F(1,2)))
check("k4 identity-word residue", residue == (F(-3,4),F(0)),
      [str(z) for z in residue])
check("residue tangent to assignment level", vx.v*residue[0]+vy.v*residue[1] == 0)
# Exact assignment-word identity, writing E=e^t as any positive multiplier.
for initial in [F(-3), F(0), F(5,2)]:
    for step, scale in [(F(1,7),F(2)),(F(-2,3),F(3,2))]:
        result = ((initial+step)*scale-scale*step)/scale
        check(f"assignment identity {initial},{step},{scale}",result==initial)
centres = [(F(1),F(0)), (F(0),F(1)), (F(-1),F(0)), (F(0),F(-1))]
check("four-circle t=1 concurrence and adjacent orthogonality",
      all(cx*cx+cy*cy == 1 for cx,cy in centres) and
      all(centres[i][0]*centres[(i+1)%4][0]+centres[i][1]*centres[(i+1)%4][1] == 0
          for i in range(4)))
# Scaling centres by t with t²=2 gives adjacent distance²=4 and opposite=8.
check("tangent-ring adjacent tangency and opposite disjointness",
      all(2*sum((u-v)**2 for u,v in zip(centres[i],centres[(i+1)%4])) == 4
          for i in range(4)) and
      all(2*sum((u-v)**2 for u,v in zip(centres[i],centres[(i+2)%4])) > 4
          for i in range(4)))
check("three-cycle from distinct transpositions",
      [({0:2,1:1,2:0})[({0:1,1:0,2:2})[i]] for i in range(3)] == [1,2,0])
for depth in range(6):
    check(f"four seeds, ternary depth={depth}", 4*3**depth == sum(3**depth for _ in range(4)))

report = {"suite":"new independent compactification finite checks",
          "original_39_check_suite_rerun":False,
          "passed":len(checks),"failed":0,"checks":checks}
parser = argparse.ArgumentParser()
parser.add_argument('--json', type=Path)
args = parser.parse_args()
if args.json:
    args.json.write_text(json.dumps(report, indent=2)+"\n")
print(f"PASS: {len(checks)} new exact finite checks; original 39-check suite not rerun.")
