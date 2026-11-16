#!/usr/bin/env python3
"""
033 — Overlay the DUAL {4,inf} on the Cayley model, next to the PRIMAL {inf,4}.

In the Cayley embedding the primal {inf,4} tree is the F2 diagonals (the square
crosses); its planar dual {4,inf} crosses each primal edge PERPENDICULARLY at
the edge midpoint (eps_2), i.e. it is the perpendicular bisector of each
half-diagonal.  Around each eps_4 vertex the four dual edges close a 4-gon face
(the {4,inf} face dual to the vertex); the dual's vertices (cusps) sit at the
fractal border where infinitely many dual edges accumulate.

Here: primal tree (black) coloured by the assignment a (odd integers, as in 032)
+ the dual {4,inf} (blue perpendicular bisectors) + the square border.

STATUS: primal tree + a-values are 029/032 (PROVED/computationally verified);
the dual = perpendicular bisectors is the planar-dual reading of the embedding.
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from math import sqrt, sin, cos, radians

SQ2 = sqrt(2.0)
NUMSTEPS = 4


def build_cayley(numsteps):
    squares = {}
    edges = []
    order = []

    def branch(cx, cy, angle, step, squares, edges, parent):
        step -= 1
        if step < 0:
            return
        R = 2.0 ** step
        key = (round(cx, 9), round(cy, 9), round(R, 9))
        if key not in squares:
            squares[key] = (cx, cy, R)
            order.append((cx, cy))
        if parent is not None:
            edges.append((parent, (cx, cy)))
        a = radians(angle)
        nx = cx + R * (-sin(a))
        ny = cy + R * (cos(a))
        for da in (-90, 0, 90):
            branch(nx, ny, angle + da, step, squares, edges, (cx, cy))

    for angle in (0, 90, 180, -90):
        branch(0.0, 0.0, angle, numsteps, squares, edges, None)
    return squares, edges, order


# T_4 a-values (as 032)
def matmul(A, B):
    return A @ B


def mpow(M, n):
    R = np.eye(2, dtype=complex)
    for _ in range(n):
        R = R @ M
    return R


def apply(M, z):
    A, B, C, D = M[0, 0], M[0, 1], M[1, 0], M[1, 1]
    return (A * z + B) / (C * z + D)


J = np.array([[0, -1], [1, 0]], dtype=complex)
T = np.array([[1, SQ2], [0, 1]], dtype=complex)
U = J @ T
EPS4 = (-1 + 1j) / SQ2


def bfs_t4_a_values(depth):
    seen = {EPS4}
    vals = [1.0]
    frontier = [np.eye(2, dtype=complex)]
    for _ in range(depth):
        nxt = []
        for g in frontier:
            for r in range(4):
                g2 = g @ mpow(U, r) @ J
                z2 = apply(g2, EPS4)
                k = complex(round(z2.real, 9), round(z2.imag, 9))
                if k not in seen:
                    seen.add(k)
                    vals.append(-z2.real / z2.imag)
                    nxt.append(g2)
        frontier = nxt
    return vals


def main():
    squares, edges, order = build_cayley(NUMSTEPS)
    avals = bfs_t4_a_values(NUMSTEPS - 1)
    n = min(len(order), len(avals))
    node_a = {order[i]: avals[i] for i in range(n)}

    fig, ax = plt.subplots(figsize=(8.6, 8.6))

    # square border (light)
    for (cx, cy, R) in squares.values():
        pts = np.array([(cx + R, cy), (cx, cy + R), (cx - R, cy), (cx, cy - R)])
        ax.plot(np.append(pts[:, 0], pts[0, 0]), np.append(pts[:, 1], pts[0, 1]),
                color="0.85", lw=0.4)

    # DUAL {4,inf}: perpendicular bisectors of each primal edge
    for (p, q) in edges:
        mx, my = (p[0] + q[0]) / 2.0, (p[1] + q[1]) / 2.0
        dx, dy = q[0] - p[0], q[1] - p[1]
        L = np.hypot(dx, dy)
        px, py = -dy / L, dx / L
        ax.plot([mx - px * L / 2, mx + px * L / 2],
                [my - py * L / 2, my + py * L / 2],
                color="tab:blue", lw=0.9, alpha=0.85, zorder=2)

    # PRIMAL {inf,4} tree coloured by a-value
    xs, ys, cs = [], [], []
    for (cx, cy) in order:
        if (cx, cy) in node_a:
            xs.append(cx); ys.append(cy); cs.append(node_a[(cx, cy)])
    xs = np.array(xs); ys = np.array(ys); cs = np.array(cs)
    vmax = 60.0
    ax.scatter(xs, ys, c=np.clip(cs, -vmax, vmax), cmap="coolwarm",
               vmin=-vmax, vmax=vmax, s=20, zorder=4,
               edgecolors="0.2", linewidths=0.3)
    for (p, q) in edges:
        ax.plot([p[0], q[0]], [p[1], q[1]], color="k", lw=0.8, zorder=3)
    ax.scatter([0], [0], marker="*", s=140, color="k", zorder=6)

    ax.set_aspect("equal"); ax.set_xticks([]); ax.set_yticks([])
    for sp in ax.spines.values():
        sp.set_visible(False)
    ax.set_title(r"primal $\{\infty,4\}$ (black, $a$-coloured) + dual "
                 r"$\{4,\infty\}$ (blue bisectors) on the Cayley model",
                 fontsize=10)
    fig.subplots_adjust(top=0.94)
    out = "/Users/mingli/AEG/aeg-paper/notes/general/033-primal-dual-cayley.png"
    fig.savefig(out, dpi=130)
    print("saved:", out)
    print("primal edges:", len(edges), " dual edges:", len(edges))


if __name__ == "__main__":
    main()
