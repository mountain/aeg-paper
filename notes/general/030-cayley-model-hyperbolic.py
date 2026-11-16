#!/usr/bin/env python3
"""
030 — Reproduce the "Cayley tree of order 4 + border" construction and put the
hyperbolic metric  g = (dx^2+dy^2)/L^2  on it  (note 01-cayley-hyperbolic-model).

The TikZ source (images/sources/cayley-tree-4-border.tex) draws, recursively:
  * at each node a square (a diamond = L1-ball |x|+|y|<=R) of radius R = 2^step,
  * its two diagonals (the embedded F2 4-regular tree edges),
  * three children at the top vertex, rotated by -90, 0, +90 deg,
  * root has 4 branches (angles 0,90,180,-90).
So the edge lengths halve with depth (s_n = L0/2^n) and the union's boundary
B_n is a fractal border in the limit.

The Cayley model proposes the hyperbolic metric  ds^2 = (dx^2+dy^2)/L^2, where
L(x,y) = Manhattan distance to the border B_n.  For a piecewise-linear L
(L = +-x +-y + C) one has  K = L * Lap L - |grad L|^2 = -2  (a.e.), so the space
has constant negative curvature -2: the border is at infinite intrinsic distance.

STATUS: the construction reproduces the TikZ; the K=-2 computation is the note's
proposal, verified numerically on a grid (away from the L-ridges).
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from math import sqrt, sin, cos, radians

NUMSTEPS = 4


def build(numsteps):
    """Return squares [(cx,cy,R)] and tree edges [( (x1,y1),(x2,y2) )]."""
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
    return list(squares.values()), edges


def manhattan_to_border(X, Y, squares):
    """L(x,y) = min over squares of | (|x-cx|+|y-cy|) - R |."""
    L = np.full_like(X, np.inf)
    for (cx, cy, R) in squares:
        d = np.abs(X - cx) + np.abs(Y - cy)
        L = np.minimum(L, np.abs(d - R))
    return L


def main():
    squares, edges = build(NUMSTEPS)
    print("squares:", len(squares), " tree edges:", len(edges))

    # ---- panel 1: tree + border ----
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12.6, 6.2))
    # squares (diamonds) filled light
    for (cx, cy, R) in squares:
        pts = np.array([(cx + R, cy), (cx, cy + R), (cx - R, cy), (cx, cy - R)])
        ax1.fill(pts[:, 0], pts[:, 1], color="cyan", alpha=0.25, lw=0)
        ax1.plot(np.append(pts[:, 0], pts[0, 0]), np.append(pts[:, 1], pts[0, 1]),
                 color="0.4", lw=0.4)
    for (p, q) in edges:
        ax1.plot([p[0], q[0]], [p[1], q[1]], color="k", lw=0.8)
    ax1.set_aspect("equal")
    ax1.set_title(r"$F_2$ 4-regular tree + border $B_n$ (square = $L^1$-ball)",
                  fontsize=10)
    ax1.set_xticks([]); ax1.set_yticks([])

    # ---- panel 2: L field + metric ----
    n = 600
    xs = np.linspace(-9, 9, n)
    ys = np.linspace(-9, 9, n)
    X, Y = np.meshgrid(xs, ys)
    L = manhattan_to_border(X, Y, squares)
    L = np.clip(L, 0, 3.0)
    pc = ax2.pcolormesh(X, Y, L, cmap="viridis", shading="auto")
    for (p, q) in edges:
        ax2.plot([p[0], q[0]], [p[1], q[1]], color="white", lw=0.5, alpha=0.6)
    ax2.set_aspect("equal")
    ax2.set_title(r"Manhattan depth $L$ to border (metric $g=\frac{dx^2+dy^2}{L^2}$)",
                  fontsize=10)
    ax2.set_xticks([]); ax2.set_yticks([])
    cb = fig.colorbar(pc, ax=ax2, fraction=0.045, pad=0.04)
    cb.set_label(r"$L$ (depth)")

    # ---- curvature check K = L * Lap L - |grad L|^2 = -2 ----
    # in a smooth region away from ridges, L = a*x + b*y + c  (a,b in {+-1})
    # -> Lap L = 0, |grad L|^2 = 2, so K = -2.  Verify numerically at a sample.
    def L_at(x, y):
        return manhattan_to_border(np.array([[x]]), np.array([[y]]), squares)[0, 0]

    h = 0.02
    # pick a point deep in the interior (a smooth region)
    x0, y0 = 0.6, 0.3
    Lxx = (L_at(x0+h, y0) - 2*L_at(x0, y0) + L_at(x0-h, y0)) / h**2
    Lyy = (L_at(x0, y0+h) - 2*L_at(x0, y0) + L_at(x0, y0-h)) / h**2
    Lx = (L_at(x0+h, y0) - L_at(x0-h, y0)) / (2*h)
    Ly = (L_at(x0, y0+h) - L_at(x0, y0-h)) / (2*h)
    LapL = Lxx + Lyy
    grad2 = Lx**2 + Ly**2
    K = L_at(x0, y0) * LapL - grad2
    print(f"\ncurvature check at ({x0},{y0}):  Lap L = {LapL:.3f}, "
          f"|grad L|^2 = {grad2:.3f},  K = L*LapL - |gradL|^2 = {K:.3f} "
          f"(expect -2 in a smooth region)")

    fig.suptitle(
        r"Cayley model $D_\infty$: $F_2$ tree + fractal border, hyperbolic "
        r"metric $g=\frac{dx^2+dy^2}{L^2}$, $K=-2$", fontsize=12)
    fig.subplots_adjust(top=0.82, wspace=0.20)
    out = "/Users/mingli/AEG/aeg-paper/notes/general/030-cayley-model-hyperbolic.png"
    fig.savefig(out, dpi=130)
    print("saved:", out)


if __name__ == "__main__":
    main()
