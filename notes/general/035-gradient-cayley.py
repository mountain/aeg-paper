#!/usr/bin/env python3
"""
035 — Gradient lines (green) of a on the Cayley model.

The gradient lines of a = -x/y in H^2 are the concentric circles x^2+y^2=const
(orthogonal to the level lines, the rays).  In the Cayley model (the straightened
Euclidean embedding of the F2 = T4 tree) the analog is the family of concentric
circles centred at the tree root; they are orthogonal to the radial level lines
that radiate from the root.

Overlaid: primal {inf,4} tree (black), dual {4,inf} (blue perpendicular
bisectors), and the gradient lines (green circles).  The circles cut the tree
edges and the blue bisectors orthogonally.

STATUS: gradient lines = circles is the exact H^2 fact (034), drawn here in the
Cayley straightening (the root plays the role of the H^2 cusp 0).
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from math import sin, cos, radians, pi

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

    fig, ax = plt.subplots(figsize=(8.8, 8.8))

    # square border (light)
    for (cx, cy, R) in squares.values():
        pts = np.array([(cx + R, cy), (cx, cy + R), (cx - R, cy), (cx, cy - R)])
        ax.plot(np.append(pts[:, 0], pts[0, 0]), np.append(pts[:, 1], pts[0, 1]),
                color="0.88", lw=0.4)

    # dual {4,inf} (blue perpendicular bisectors)
    for (p, q) in edges:
        mx, my = (p[0] + q[0]) / 2.0, (p[1] + q[1]) / 2.0
        dx, dy = q[0] - p[0], q[1] - p[1]
        L = np.hypot(dx, dy)
        px, py = -dy / L, dx / L
        ax.plot([mx - px * L / 2, mx + px * L / 2],
                [my - py * L / 2, my + py * L / 2],
                color="tab:blue", lw=0.7, alpha=0.7, zorder=2)

    # primal tree (black)
    for (p, q) in edges:
        ax.plot([p[0], q[0]], [p[1], q[1]], color="k", lw=0.8, zorder=3)

    # gradient lines (green concentric circles centred at the root)
    th = np.linspace(0, 2 * pi, 500)
    for R in [0.5, 1.0, 2.0, 4.0, 8.0, 16.0, 32.0]:
        ax.plot(R * np.cos(th), R * np.sin(th), color="tab:green", lw=1.0,
                alpha=0.9, zorder=4)

    ax.scatter([0], [0], marker="*", s=150, color="k", zorder=6)
    ax.set_aspect("equal"); ax.set_xticks([]); ax.set_yticks([])
    for sp in ax.spines.values():
        sp.set_visible(False)
    ax.set_xlim(-34, 34); ax.set_ylim(-34, 34)
    ax.set_title(r"gradient lines (green circles) on the Cayley model; "
                 r"primal $\{\infty,4\}$ (black), dual $\{4,\infty\}$ (blue)",
                 fontsize=10)
    fig.subplots_adjust(top=0.94)
    out = "/Users/mingli/AEG/aeg-paper/notes/general/035-gradient-cayley.png"
    fig.savefig(out, dpi=130)
    print("saved:", out)


if __name__ == "__main__":
    main()
