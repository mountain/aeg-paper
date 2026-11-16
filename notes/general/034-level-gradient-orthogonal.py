#!/usr/bin/env python3
"""
034 — Level lines and gradient lines of a = -x/y are ORTHOGONAL.

In H^2 (upper half-plane), a = -x/y:
  * level lines (a = const)  :  y = k x   -> rays through the origin;
  * gradient lines (Euclidean grad a = (-1/y, x/y^2)):
        dy/dx = -x/y  ->  x^2 + y^2 = const  -> concentric circles
        (which ARE H^2-geodesics: semicircles centred on the real axis).
  A ray and a circle meet orthogonally (radial perp circumferential).

For the AES metric  g = y^{-2}(dx^2/mu^2 + dy^2/lam^2)  the gradient is
grad_g a = (-mu^2 y, lam^2 x), so the gradient lines are the ELLIPSES
(lam^2/mu^2) x^2 + y^2 = const  (for mu=1, lam=2:  4 x^2 + y^2 = const);
they are g-orthogonal to the same rays (not Euclidean-orthogonal).

Shown in the Poincare disk (Cayley map).  Rays = red, circles = blue;
right panel adds the mu=1,lam=2 ellipses (green) for the g-gradient.
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from math import pi, sin, cos, sqrt


def to_disk(z):
    return (z - 1j) / (z + 1j)


def main():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12.4, 6.4))

    thc = np.linspace(0, 2 * pi, 400)
    for ax in (ax1, ax2):
        ax.plot(np.cos(thc), np.sin(thc), color="0.2", lw=1.1)
        ax.set_aspect("equal"); ax.set_xticks([]); ax.set_yticks([])
        for sp in ax.spines.values():
            sp.set_visible(False)

    # --- level lines: rays  theta = const (a = -x/y = -cot theta) ---
    rho = np.linspace(0.001, 30, 600)
    rays = np.radians([10, 20, 30, 45, 60, 75, 90, 105, 120, 135, 150, 165])
    # --- gradient lines (Euclidean): circles  x^2+y^2 = R^2 ---
    circ_radii = [0.15, 0.3, 0.55, 1.0, 1.8, 3.2, 6.0]
    thetas = np.linspace(0.02, pi - 0.02, 400)

    for ax in (ax1, ax2):
        for t in rays:
            z = rho * (cos(t) + 1j * sin(t))
            w = to_disk(z)
            ax.plot(w.real, w.imag, color="tab:red", lw=0.8, alpha=0.85)
        for R in circ_radii:
            z = R * (np.cos(thetas) + 1j * np.sin(thetas))
            w = to_disk(z)
            ax.plot(w.real, w.imag, color="tab:blue", lw=1.0, alpha=0.85)

    ax1.set_title(r"level lines (rays, red) $\perp$ gradient lines "
                  r"(circles, blue) for $a=-x/y$", fontsize=10)

    # --- right: add mu=1, lam=2 ellipses (g-gradient lines) ---
    mu, lam = 1.0, 2.0
    eR = [0.3, 0.55, 1.0, 1.8, 3.2]
    for R in eR:
        xs = np.linspace(-R / lam, R / lam, 400)
        yy = R * np.sqrt(1.0 - (lam * xs / R) ** 2)   # (lam^2)x^2 + y^2 = R^2
        z_up = xs + 1j * yy
        w = to_disk(z_up)
        ax2.plot(w.real, w.imag, color="tab:green", lw=1.0, alpha=0.8)
    ax2.set_title(r"plus $\mu{=}1,\lambda{=}2$ g-gradient lines (ellipses "
                  r"$4x^2{+}y^2=c$, green)", fontsize=10)

    fig.suptitle(r"$a=-x/y$: level lines (rays) and gradient lines "
                 r"(circles / $g$-ellipses) are orthogonal", fontsize=12)
    fig.subplots_adjust(top=0.82, wspace=0.06)
    out = "/Users/mingli/AEG/aeg-paper/notes/general/034-level-gradient-orthogonal.png"
    fig.savefig(out, dpi=130)
    print("saved:", out)


if __name__ == "__main__":
    main()
