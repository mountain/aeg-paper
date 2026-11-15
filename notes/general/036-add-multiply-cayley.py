#!/usr/bin/env python3
"""
036 — Add-multiply decomposition of a on the Cayley model (conjecture).

Verified facts:  a = -x/y  is singular at the origin (0/0);  on the 45-deg
diagonal (y=x) a=-1, on the 135-deg diagonal (y=-x) a=1; the a=0 line is x=0.

Proposed reading (the user's conjecture):
  * BLUE lines (dual {4,inf} perpendicular bisectors) = ZERO lines (the a=0
    orbit) — the "add zero";
  * ORIGIN = singular point of a, COMPLETED by the value 0 — the "multiply zero";
  * GREEN circles inside the fundamental domain (innermost blue square,
    half-side 4) at radii 4·(1/2,1/4,1/8,...) = MULTIPLY scale 1/2,1/4,1/8,...,
    halving toward the origin (rho -> 0);
  * the 45-deg (a=-1) and 135-deg (a=1) diagonals = ADD axes, separated by two
    add steps a=-1 --(+1)--> a=0 --(+1)--> a=1.

So the polar decomposition (rho, theta) = (multiply, add): "add" moves between
the level lines (rays, angle theta); "multiply" moves between the gradient
lines (circles, radius rho).  They are orthogonal and harmonize with the zero
lines and the level lines.

STATUS: the a-values (singularity, -1/+1, scales) are exact (computed); the
add-multiply READING is a STRUCTURAL PROPOSAL.
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

    fig, ax = plt.subplots(figsize=(9.0, 9.0))

    # square border (light)
    for (cx, cy, R) in squares.values():
        pts = np.array([(cx + R, cy), (cx, cy + R), (cx - R, cy), (cx, cy - R)])
        ax.plot(np.append(pts[:, 0], pts[0, 0]), np.append(pts[:, 1], pts[0, 1]),
                color="0.88", lw=0.4)

    # BLUE zero lines (dual {4,inf} = perpendicular bisectors)
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

    # GREEN multiply-scale circles (radii 4,2,1,0.5,0.25,... inside the domain)
    th = np.linspace(0, 2 * pi, 500)
    for R in [4.0, 2.0, 1.0, 0.5, 0.25, 0.125]:
        ax.plot(R * np.cos(th), R * np.sin(th), color="tab:green", lw=1.0,
                alpha=0.9, zorder=4)

    # diagonals: 45 deg (a=-1) orange, 135 deg (a=1) magenta
    t = np.linspace(-34, 34, 2)
    ax.plot(t, t, color="tab:orange", lw=2.2, zorder=5)          # y=x (45 deg)
    ax.plot(t, -t, color="tab:purple", lw=2.2, zorder=5)         # y=-x (135 deg)

    # origin = singularity (completed with a=0)
    ax.scatter([0], [0], marker="*", s=320, color="tab:red", zorder=7)

    # annotations
    ax.text(6.2, 5.6, r"$a=-1$ (45°)", color="tab:orange", fontsize=10, fontweight="bold")
    ax.text(5.4, -7.6, r"$a=1$ (135°)", color="tab:purple", fontsize=10, fontweight="bold")
    ax.text(0.6, -1.4, r"origin: $a=\frac{0}{0}$ singular, completed $a=0$",
            color="tab:red", fontsize=8.5)
    ax.text(2.3, 2.0, r"$\times\frac{1}{2}$", color="tab:green", fontsize=10,
            fontweight="bold")
    ax.text(2.7, 1.2, r"$\times\frac{1}{4}$", color="tab:green", fontsize=9)
    ax.text(3.4, 0.5, r"$\times\frac{1}{8}$", color="tab:green", fontsize=9)

    ax.set_aspect("equal"); ax.set_xticks([]); ax.set_yticks([])
    for sp in ax.spines.values():
        sp.set_visible(False)
    ax.set_xlim(-34, 34); ax.set_ylim(-34, 34)
    ax.set_title(r"Cayley model: blue zero lines, green multiply scale "
                 r"$\frac{1}{2},\frac{1}{4},\frac{1}{8}$, 45°/135° add axes ($a=\mp1$)",
                 fontsize=10)
    fig.subplots_adjust(top=0.94)
    out = "/Users/mingli/AEG/aeg-paper/notes/general/036-add-multiply-cayley.png"
    fig.savefig(out, dpi=130)
    print("saved:", out)


if __name__ == "__main__":
    main()
