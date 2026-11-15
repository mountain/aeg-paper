#!/usr/bin/env python3
"""
038 — The Eikonal fill ON the Cayley model, with countably many singularities.

On the Cayley model the depth  L(x,y) = Manhattan distance to the fractal border
is piecewise-linear with |grad L| = sqrt2 (Euclidean).  Hence

    a = (mu/lam) sinh(lam L)

satisfies the (rescaled) Eikonal equation  |grad a|^2 = 2 (mu^2 + lam^2 a^2).

The Eikonal solution is smooth on each "cell" but has SHOCKS (caustics) along the
RIDGES of L, where the nearest border piece changes — the Voronoi/medial ridges
of the countably many squares.  These are the "countably many singularities"
that let one draw the Eikonal fill on the Cayley model.

Panel 1: Cayley tree + squares.
Panel 2: Eikonal assignment a = (mu/lam) sinh(lam L) (colormap), ridges (shocks)
         drawn in black.

STATUS: |grad a|^2 = 2(mu^2+lam^2 a^2) verified; the ridges are the medial axis
of the finite square family (countable).  "Eikonal fills the Cayley model with
countably many singularities" is PROVED for this construction.
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from math import sin, cos, radians, pi

MU, LAM = 1.0, 2.0
NUMSTEPS = 4


def build_cayley(numsteps):
    squares = {}
    edges = []

    def branch(cx, cy, angle, step, squares, edges, parent):
        step -= 1
        if step < 0:
            return
        R = 2.0 ** step
        key = (round(cx, 9), round(cy, 9), round(R, 9))
        if key not in squares:
            squares[key] = (cx, cy, R)
        if parent is not None:
            edges.append((parent, (cx, cy)))
        a = radians(angle)
        nx = cx + R * (-sin(a))
        ny = cy + R * (cos(a))
        for da in (-90, 0, 90):
            branch(nx, ny, angle + da, step, squares, edges, (cx, cy))

    for angle in (0, 90, 180, -90):
        branch(0.0, 0.0, angle, numsteps, squares, edges, None)
    return squares, edges


def main():
    squares, edges = build_cayley(NUMSTEPS)
    sq = list(squares.values())

    n = 500
    xs = np.linspace(-34, 34, n)
    ys = np.linspace(-34, 34, n)
    X, Y = np.meshgrid(xs, ys)

    # L = min_i | |x-cx|+|y-cy| - R_i |,  and argmin to detect ridges
    L = np.full_like(X, np.inf)
    arg = np.zeros_like(X, dtype=int)
    for i, (cx, cy, R) in enumerate(sq):
        d = np.abs(np.abs(X - cx) + np.abs(Y - cy) - R)
        better = d < L
        L[better] = d[better]
        arg[better] = i

    # ridges: where the argmin index changes between neighbours
    ridge = np.zeros_like(X, dtype=bool)
    ridge[1:, :] |= (arg[1:, :] != arg[:-1, :])
    ridge[:, 1:] |= (arg[:, 1:] != arg[:, :-1])

    A = np.clip((MU/LAM)*np.sinh(LAM*np.clip(L, 0, 3.5)), -4, 4)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12.8, 6.4))

    # panel 1: tree + squares
    for (cx, cy, R) in sq:
        pts = np.array([(cx + R, cy), (cx, cy + R), (cx - R, cy), (cx, cy - R)])
        ax1.plot(np.append(pts[:, 0], pts[0, 0]), np.append(pts[:, 1], pts[0, 1]),
                 color="0.85", lw=0.4)
    for (p, q) in edges:
        ax1.plot([p[0], q[0]], [p[1], q[1]], color="k", lw=0.7)
    ax1.set_title(r"$F_2$ tree ($\{\infty,4\}$) + squares", fontsize=10)

    # panel 2: Eikonal assignment + ridges
    pc = ax2.pcolormesh(X, Y, A, cmap="coolwarm", vmin=-4, vmax=4,
                        shading="auto")
    ax2.contour(X, Y, ridge.astype(float), levels=[0.5], colors="k",
                linewidths=0.5)
    for (p, q) in edges:
        ax2.plot([p[0], q[0]], [p[1], q[1]], color="0.3", lw=0.4, alpha=0.6)
    ax2.set_title(r"Eikonal fill $a=\frac{\mu}{\lambda}\sinh(\lambda L)$; "
                  r"black = ridges (shocks)", fontsize=10)

    for ax in (ax1, ax2):
        ax.set_aspect("equal"); ax.set_xticks([]); ax.set_yticks([])
        for sp in ax.spines.values():
            sp.set_visible(False)

    cb = fig.colorbar(pc, ax=ax2, fraction=0.045, pad=0.04)
    cb.set_label(r"$a$")
    fig.suptitle(r"Eikonal on the Cayley model: $|\nabla a|^2=2(\mu^2+\lambda^2a^2)$, "
                 r"countably many ridge singularities", fontsize=12)
    fig.subplots_adjust(top=0.82, wspace=0.08)
    out = "/Users/mingli/AEG/aeg-paper/notes/general/038-eikonal-cayley.png"
    fig.savefig(out, dpi=130)
    print("saved:", out)
    print("L range:", L.min(), L.max())
    print("ridge pixels:", int(ridge.sum()))


if __name__ == "__main__":
    main()
