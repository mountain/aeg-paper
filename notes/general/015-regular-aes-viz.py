#!/usr/bin/env python3
"""
015 — Visualizing the regular AES  E0  with  lambda = 1+sqrt2, mu = 1-sqrt2.

Assignment function  a  in the two standard models:

  upper half-plane:  a = -x/y      (zero set: x = 0, the imaginary axis)
  Poincare disk:     a = 2v/(1-rho^2),   w = u + iv, rho^2 = u^2+v^2
                     (zero set: v = 0, the real diameter)

Both carry the same eikonal  |grad a|_g^2 = mu^2 + lambda^2 a^2, with
  mu^2 = 3-2sqrt2 = k,  lambda^2 = 3+2sqrt2 = 1/k,  curvature K = -lambda^2.

Level sets: in H^2 the rays  x = -c y  through the boundary point 0 (a pencil);
in the disk the circles through  w = -1 and w = +1  (plus the diameter v = 0).

STATUS: exact classical identities (computationally verified); the "distribution
of the assignment" is the standard E0 model, not a new theorem.
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from math import sqrt

SQ2 = sqrt(2.0)
MU = 1.0 - SQ2
LAM = 1.0 + SQ2
MU2 = MU * MU          # = 3-2sqrt2 = k
LAM2 = LAM * LAM       # = 3+2sqrt2 = 1/k
K = -LAM2

LEVS = [-4, -2, -1, -0.5, 0, 0.5, 1, 2, 4]
CMAP = "RdBu_r"
CLIM = 3.0


def panel_halfplane(ax):
    n = 700
    x = np.linspace(-2.6, 2.6, n)
    y = np.linspace(0.02, 2.6, n)
    X, Y = np.meshgrid(x, y)
    A = -X / Y
    A = np.clip(A, -CLIM, CLIM)

    pc = ax.pcolormesh(X, Y, A, cmap=CMAP, vmin=-CLIM, vmax=CLIM,
                       shading="auto")
    cs = ax.contour(X, Y, A, levels=LEVS, colors="k", linewidths=0.6,
                    alpha=0.55)
    ax.clabel(cs, fmt="%.1f", fontsize=6)

    ax.axhline(0, color="0.2", lw=1.6)                 # ideal boundary R
    ax.plot([0, 0], [0, 2.6], color="lime", lw=2.2, zorder=5)  # zero set a=0
    ax.text(0.08, 2.4, r"$a=0$", color="lime", fontsize=10)

    # metric gradient  grad a = -mu^2 y dx + lambda^2 x dy   (app B)
    gx = np.linspace(-2.6, 2.6, 21)
    gy = np.logspace(-1.6, 0.4, 13)
    GX, GY = np.meshgrid(gx, gy)
    U = -MU2 * GY
    V = LAM2 * GX
    norm = np.hypot(U, V)
    ax.quiver(GX, GY, U / norm, V / norm, scale=22, color="white",
              alpha=0.5, width=0.0035, zorder=3)

    ax.set_xlim(-2.6, 2.6)
    ax.set_ylim(0, 2.6)
    ax.set_aspect("equal")
    ax.set_xlabel("$x$")
    ax.set_ylabel("$y$")
    ax.set_title(r"upper half-plane: $a=-x/y$  ($a>0$ left, $a<0$ right)",
                 fontsize=10)
    return pc


def panel_disk(ax):
    n = 700
    u = np.linspace(-1.0, 1.0, n)
    v = np.linspace(-1.0, 1.0, n)
    U, V = np.meshgrid(u, v)
    rho2 = U * U + V * V
    A = 2 * V / (1 - rho2)
    A = np.ma.masked_where(rho2 >= 1.0, A)
    A = np.clip(A, -CLIM, CLIM)

    pc = ax.pcolormesh(U, V, A, cmap=CMAP, vmin=-CLIM, vmax=CLIM,
                       shading="auto")
    cs = ax.contour(U, V, A, levels=LEVS, colors="k", linewidths=0.6,
                    alpha=0.55)
    ax.clabel(cs, fmt="%.1f", fontsize=6)

    th = np.linspace(0, 2 * np.pi, 400)
    ax.plot(np.cos(th), np.sin(th), color="0.2", lw=1.6)   # ideal boundary
    ax.plot([-1, 1], [0, 0], color="lime", lw=2.2, zorder=5)  # zero set a=0
    ax.text(0.0, 0.04, r"$a=0$", color="lime", fontsize=10, ha="center")
    ax.plot([-1], [0], marker="o", ms=5, color="k", zorder=6)
    ax.plot([1], [0], marker="o", ms=5, color="k", zorder=6)
    ax.text(-1.0, -0.09, r"$w=w(0)$", ha="center", fontsize=8)
    ax.text(1.0, -0.09, r"$w=w(\infty)$", ha="center", fontsize=8)

    ax.set_aspect("equal")
    ax.set_xticks([])
    ax.set_yticks([])
    for sp in ax.spines.values():
        sp.set_visible(False)
    ax.set_title(r"Poincaré disk: $a=2v/(1-\rho^2)$  ($a>0$ upper, $a<0$ lower)",
                 fontsize=10)
    return pc


def main():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12.4, 5.7))
    pc1 = panel_halfplane(ax1)
    pc2 = panel_disk(ax2)
    cbar = fig.colorbar(pc2, ax=[ax1, ax2], fraction=0.022, pad=0.02)
    cbar.set_label(r"assignment $a$")
    fig.suptitle(
        r"Regular AES $E_0$: $\lambda=1+\sqrt{2},\ \mu=1-\sqrt{2}$, "
        r"$|\nabla a|_g^2=\mu^2+\lambda^2 a^2$, "
        r"$\mu^2=3-2\sqrt{2}=k$, $\lambda^2=3+2\sqrt{2}$, $K=-\lambda^2$",
        fontsize=11.5)
    fig.subplots_adjust(top=0.87, wspace=0.28)
    out = "/Users/mingli/AEG/aeg-paper/notes/general/015-regular-aes-viz.png"
    fig.savefig(out, dpi=130)
    print("saved:", out)
    print("  mu^2 =", round(MU2, 6), " lambda^2 =", round(LAM2, 6),
          " K =", round(K, 6))


if __name__ == "__main__":
    main()
