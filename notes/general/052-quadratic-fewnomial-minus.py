#!/usr/bin/env python3
"""
052 — The quadratic fewnomial on the unit circle, general rule, applied to
P_eps(V) = V^2 - eps V - 1.

For f(V) = a V^2 + b V + c on |V| = 1, a self-intersection f(V)=f(W) with V != W
factors as
    f(V) - f(W) = (V - W)(a(V + W) + b),
so the crossing is the chord-SUM condition V + W = -b/a, solvable iff |b/a| <= 2
(born as a cusp at |b/a| = 2).  At the crossing V + conj(V) = -b/a, hence
    f(V) = a V^2 - a(V + conj V)V + c = -a|V|^2 + c = c - a.
So the node sits at the FIXED image value c - a (independent of b), and the roots
f(V)=0 have product c/a.  All three are exact.

Old example (021/024): a=1, b=eps, c=+1  -> node at 0, roots product +1.
New example here:   a=1, b=-eps, c=-1 -> node at -2, roots product -1,
with the algebraic identity  P_eps(V) + 2 = V^2 - eps V + 1 = Q_{-eps}(V).

STATUS: the node-at-(c-a), birth-at-|b/a|=2, and product-c/a formulas are PROVED;
the figure is a COMPUTATIONALLY VERIFIED EXAMPLE.
"""

from math import pi, acos
import cmath
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path

OUT = Path(__file__).resolve().parent


def node_value(a, b, c):
    """Fixed image value of the self-intersection of a V^2 + b V + c on |V|=1."""
    return c - a


def has_node(a, b, c):
    return abs(b / a) <= 2.0


def roots(a, b, c):
    disc = cmath.sqrt(b * b - 4.0 * a * c)
    return (-b + disc) / (2.0 * a), (-b - disc) / (2.0 * a)


def P(eps, t):
    V = np.exp(1j * t)
    return V ** 2 - eps * V - 1


def main():
    print("general quadratic a V^2 + b V + c on |V|=1:")
    for (a, b, c) in ((1, 1, 1), (1, -1, -1), (2, 3, -1), (1, 2, 0)):
        nv = node_value(a, b, c)
        r1, r2 = roots(a, b, c)
        print(f"  a={a},b={b},c={c}: node at {nv}, |b/a|={abs(b/a):.2f} "
              f"({'node' if has_node(a,b,c) else 'none'}), roots {r1:.4f},{r2:.4f} "
              f"(product {r1*r2:.4f} = c/a = {c/a})")

    print("\nP_eps(V) = V^2 - eps V - 1  (a=1,b=-eps,c=-1): node at c-a = -2")
    for eps in (0.0, 0.5, 1.0, 1.9, 2.0, 2.5):
        if abs(eps) <= 2.0 and eps != 0.0:
            t0 = acos(eps / 2.0)
            print(f"  eps={eps}: crossing V=e^{{+-i t}} with 2 cos t = eps, "
                  f"P(V) = {P(eps, t0).real:.6f} (expect -2)")
        else:
            print(f"  eps={eps}: no transverse node" if abs(eps) > 2 else
                  f"  eps=0: retraced circle e^(2it)-1")
    for eps in (0.0, 1.0, 2.0):
        r1, r2 = roots(1.0, -eps, -1.0)
        print(f"  eps={eps}: roots {r1:.4f},{r2:.4f}  product {r1*r2:.4f} (=-1)")

    t = np.linspace(0, 2 * pi, 3000)
    fig, axes = plt.subplots(1, 4, figsize=(14.5, 4.0))
    for ax, eps in zip(axes, (0.0, 1.0, 2.0, 2.5)):
        z = P(eps, t)
        ax.plot(z.real, z.imag, lw=1.1, color="#1f77b4")
        ax.plot([0], [0], "k+", ms=9)
        ax.plot([-2], [0], "o", mfc="none", mec="#d62728", ms=9)
        if 0 < eps < 2:
            ax.plot([-2], [0], "o", color="#d62728", ms=5)
            ax.set_title(f"$\\varepsilon={eps}$: node at $-2$", fontsize=10)
        elif abs(eps) < 1e-9:
            ax.set_title("$\\varepsilon=0$: circle $e^{2it}-1$ (twice)", fontsize=10)
        elif abs(eps - 2) < 1e-9:
            ax.set_title("$\\varepsilon=2$: cusp at $-2$", fontsize=10)
        else:
            ax.set_title(f"$\\varepsilon={eps}$: smooth", fontsize=10)
        ax.set_aspect("equal")
    fig.suptitle(r"$P_\epsilon(V)=V^2-\epsilon V-1$ on $|V|=1$: node fixed at "
                 "$c-a=-2$, born at $|b/a|=|\\epsilon|=2$;  roots $r_+r_-=-1$")
    fig.tight_layout(rect=[0, 0, 1, 0.92])
    fname = OUT / "052-quadratic-fewnomial-minus.png"
    fig.savefig(fname, dpi=125)
    print("wrote", fname.name)


if __name__ == "__main__":
    main()
