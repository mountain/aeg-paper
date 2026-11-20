#!/usr/bin/env python3
"""
053 — Fire-front trichotomy illustration: half = birth, full = root.

For gamma = A : z -> z+2 on the thrice-punctured sphere H^2 / Γ(2), basepoint p=i:
  A p = 2+i,  A^{-1} p = -2+i,  ||A|| = d(i, 2+i) = 2 arsinh(1) = arcosh(3) = 1.7627.
The perpendicular bisector of [p, A^{-1}p] is the vertical geodesic x = -1.

  * birth at t = ||A||/2 = arsinh(1) = 0.8814 : the hyperbolic circles Sigma_t(p)
    (centre i*sqrt2, radius 1) and Sigma_t(A^{-1}p) (centre -2 + i*sqrt2, radius 1)
    are tangent at the midpoint -1 + i*sqrt2 (on the bisector x = -1).
  * root  at t = ||A||   = arcosh(3) = 1.7627 : Sigma_t(p) (centre 3i, radius 2*sqrt2)
    passes through A p = 2+i.

This is the concrete A-instance of note 026's half/full pairing.
"""

from math import pi, sqrt, cosh, sinh, asinh
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path

OUT = Path(__file__).resolve().parent


def main():
    LA = 2.0 * asinh(1.0)
    half = LA / 2.0
    print(f"||A|| = {LA:.6f}   half = {half:.6f}")
    print(f"sinh(half)={sinh(half):.4f} (1), cosh(half)={cosh(half):.4f} (sqrt2)")
    print(f"sinh(||A||)={sinh(LA):.4f} (2*sqrt2), cosh(||A||)={cosh(LA):.4f} (3)")

    circ = np.exp(1j * np.linspace(0, 2 * pi, 400))
    fig, axes = plt.subplots(1, 2, figsize=(11.5, 5.2))

    # left: birth
    ax = axes[0]
    c, r = cosh(half), sinh(half)
    ax.plot((0 + c * 1j + r * circ).real, (0 + c * 1j + r * circ).imag, color="#1f77b4", lw=1.1)
    ax.plot((-2 + c * 1j + r * circ).real, (-2 + c * 1j + r * circ).imag, color="#ff7f0e", lw=1.1)
    ax.axvline(-1, color="0.6", ls="--", lw=0.8)
    for (x, y) in ((0, 1), (2, 1), (-2, 1)):
        ax.plot([x], [y], "o", color="#d62728", ms=5)
    ax.plot([-1], [c], "x", color="#2ca02c", ms=9)
    ax.text(-1.05, c + 0.15, "birth", fontsize=8, color="#2ca02c")
    ax.set_xlim(-3.6, 3.6); ax.set_ylim(-0.4, 4.2); ax.set_aspect("equal")
    ax.set_title(f"t = ||A||/2 = {half:.3f}: two spheres tangent on $x=-1$", fontsize=9)

    # right: root
    ax = axes[1]
    c, r = cosh(LA), sinh(LA)
    ax.plot((0 + c * 1j + r * circ).real, (0 + c * 1j + r * circ).imag, color="#1f77b4", lw=1.1)
    ax.axvline(-1, color="0.6", ls="--", lw=0.8)
    ax.plot([0], [1], "o", color="#d62728", ms=5)
    ax.plot([-2], [1], "o", color="#d62728", ms=5)
    ax.plot([2], [1], "o", color="#d62728", ms=6)
    ax.text(2.15, 1.0, "A p (on $C_t$)", fontsize=8, color="#d62728")
    ax.set_xlim(-3.6, 3.6); ax.set_ylim(-0.4, 4.2); ax.set_aspect("equal")
    ax.set_title(f"t = ||A|| = {LA:.3f}: $C_t$ passes through $A p$", fontsize=9)

    fig.suptitle("half = birth of the crossing (on the fixed bisector), full = wavefront reaches the deck image")
    fig.tight_layout(rect=[0, 0, 1, 0.94])
    fname = OUT / "053-half-full-firefront.png"
    fig.savefig(fname, dpi=125)
    print("wrote", fname.name)


if __name__ == "__main__":
    main()
