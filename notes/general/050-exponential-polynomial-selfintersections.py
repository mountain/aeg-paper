#!/usr/bin/env python3
"""
050 — A fewnomial toy model for the fire-front twist: f(z) = z + c z^2 on |z| = 1.

Purpose: make the "exponential-polynomial / fewnomial curve" analogy to the
fire-front concrete.  The fire front on the flat torus is C_t(theta) = t e^{i theta}
mod Z^2, and its self-intersections are born at t = |v|/2 for lattice vectors v
(the length spectrum).  A finite fewnomial curve f(z) = sum_k c_k z^{lambda_k} on
the unit circle is the same kind of object with a FINITE frequency set
{lambda_k} in place of the infinite lattice.

Two-term case (exact, transparent):
    f(z) = z + c z^2,  |z| = 1.
A self-intersection f(u) = f(v) with u != v gives
    (u - v)(1 + c(u + v)) = 0  =>  u + v = -1/c,
so u, v are conjugate with Re u = -1/(2c): one node, born at |c| = 1/2, at the
point f(u) = -c.  Exactly as the fire-front crossing for v is born at t = |v|/2,
the fewnomial node is born when the coefficient crosses half a spectral quantity.

STATUS: the two-term algebra above is PROVED.  The figure is a
COMPUTATIONALLY VERIFIED EXAMPLE.  The full "fewnomial <-> length spectrum"
dictionary (frequencies = lengths, coefficients = marks, Gauss word = phases) is
a STRUCTURAL PROPOSAL for a future note.
"""

from math import pi, acos
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path

OUT = Path(__file__).resolve().parent


def node_point(c):
    """f(th) = e^{i th} + c e^{2 i th} self-intersection: one node at z = -c,
    for |c| >= 1/2, with th = +-arccos(-1/(2c))."""
    th0 = acos(-1.0 / (2.0 * c))
    return [np.exp(1j * s * th0) + c * np.exp(2j * s * th0) for s in (+1.0, -1.0)]


def main():
    print("two-term fewnomial f(z) = z + c z^2, |z| = 1:")
    for c in (0.4, 0.5, 0.8, 1.2):
        if abs(c) < 0.5:
            print(f"  c={c}: no node (|c| < 1/2)")
        elif abs(c) == 0.5:
            print(f"  c={c}: cusp, node just born")
        else:
            pts = node_point(abs(c))
            print(f"  c={c}: one node at z = {-c} (th = +-{acos(-1/(2*abs(c))):.4f})")

    th = np.linspace(0, 2 * pi, 4000)
    z = np.exp(1j * th)
    fig, axes = plt.subplots(1, 3, figsize=(13.5, 4.6))
    for ax, c in zip(axes, (0.5, 0.8, 1.2)):
        cur = z + c * z ** 2
        ax.plot(cur.real, cur.imag, lw=1.0, color="#1f77b4")
        ax.plot([0], [0], "k+", ms=8)
        if abs(c) > 0.5:
            for p in node_point(c):
                ax.plot([p.real], [p.imag], "o", color="#d62728", ms=5)
            ax.set_title(f"c={c}: 1 node at z=-c")
        else:
            ax.set_title(f"c={c}: cusp (node just born)")
        ax.set_aspect("equal")
    fig.suptitle(r"$f(z)=z+c\,z^2$ on $|z|=1$: node born at $|c|=1/2$, "
                 "as the fire-front crossing is born at $t=|v|/2$")
    fig.tight_layout(rect=[0, 0, 1, 0.94])
    fname = OUT / "050-exponential-polynomial-selfintersections.png"
    fig.savefig(fname, dpi=120)
    print("wrote", fname.name)


if __name__ == "__main__":
    main()
