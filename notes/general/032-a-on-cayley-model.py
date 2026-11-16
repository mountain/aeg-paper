#!/usr/bin/env python3
"""
032 — Visualize the assignment a (= odd integers) ON the Cayley model.

The Cayley tree 4-border (= the F2 4-regular tree, embedded with halving
squares and a fractal border) is combinatorially the SAME 4-regular tree T_4
as the {inf,4} tiling.  The assignment a = -x/y takes odd-integer values on the
T_4 vertices (g.eps_4), so those values transfer verbatim to the Cayley tree's
nodes (square centres):  root a=1, four children a = -1, 3, 7, 3 (two of them
collapse to the same a=3), etc.

Left  : the Cayley tree + fractal border (TikZ reproduction).
Right : the same tree, each node coloured by its a-value (odd integer), with the
        collapse (two branches sharing a=3) visible as repeated colours.

STATUS: the a-values are the PROVED odd integers of 029; the Cayley embedding is
the TikZ construction (030).  The branch->a-value convention (which Cayley
branch carries which odd integer) is a fixed F2-generator convention.
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from math import sqrt, sin, cos, radians

SQ2 = sqrt(2.0)
NUMSTEPS = 4


# ---- Cayley tree (TikZ) ----
def build_cayley(numsteps):
    squares = {}
    edges = []          # (parent_center, child_center)
    order = []          # BFS-ordered list of (cx, cy)

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


# ---- T_4 tree (C_2*C_4), BFS a-values ----
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
    """BFS T_4, return list of a-values in BFS order (root first, then 4
    children r=0..3, then grandchildren)."""
    seen = {EPS4}
    vals = [-EPS4.real / EPS4.imag]     # root a = 1
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
    avals = bfs_t4_a_values(NUMSTEPS - 1)   # Cayley has NUMSTEPS-1 levels
    print("Cayley nodes:", len(order), " a-values:", len(avals))
    # align: Cayley node i <-> a-value i (both BFS order).  May pad/truncate.
    n = min(len(order), len(avals))
    node_a = {order[i]: avals[i] for i in range(n)}

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12.6, 6.4))

    # left: tree + border
    for (cx, cy, R) in squares.values():
        pts = np.array([(cx + R, cy), (cx, cy + R), (cx - R, cy), (cx, cy - R)])
        ax1.fill(pts[:, 0], pts[:, 1], color="cyan", alpha=0.22, lw=0)
        ax1.plot(np.append(pts[:, 0], pts[0, 0]), np.append(pts[:, 1], pts[0, 1]),
                 color="0.4", lw=0.4)
    for (p, q) in edges:
        ax1.plot([p[0], q[0]], [p[1], q[1]], color="k", lw=0.8)
    ax1.set_aspect("equal"); ax1.set_xticks([]); ax1.set_yticks([])
    ax1.set_title(r"$F_2$ tree + fractal border", fontsize=10)

    # right: a-value on the Cayley nodes
    for (p, q) in edges:
        ax2.plot([p[0], q[0]], [p[1], q[1]], color="0.75", lw=0.5, zorder=1)
    xs = []; ys = []; cs = []
    for (cx, cy) in order:
        if (cx, cy) in node_a:
            xs.append(cx); ys.append(cy); cs.append(node_a[(cx, cy)])
    xs = np.array(xs); ys = np.array(ys); cs = np.array(cs)
    vmax = 60.0
    sc = ax2.scatter(xs, ys, c=np.clip(cs, -vmax, vmax), cmap="coolwarm",
                     vmin=-vmax, vmax=vmax, s=26, zorder=3,
                     edgecolors="0.3", linewidths=0.4)
    for i in range(min(5, len(xs))):
        ax2.text(xs[i], ys[i] + 1.0, f"{int(round(cs[i]))}", fontsize=7,
                 ha="center", color="k")
    ax2.set_aspect("equal"); ax2.set_xticks([]); ax2.set_yticks([])
    ax2.set_title(r"assignment $a$ on the Cayley model (odd integers; "
                  r"collapse at $a=3$)", fontsize=10)
    cb = fig.colorbar(sc, ax=ax2, fraction=0.045, pad=0.04)
    cb.set_label(r"$a$ (odd integer)")

    fig.suptitle(r"the assignment $a$ visualised ON the Cayley model "
                 r"($F_2$ tree = $T_4$)", fontsize=12)
    fig.subplots_adjust(top=0.84, wspace=0.16)
    out = "/Users/mingli/AEG/aeg-paper/notes/general/032-a-on-cayley-model.png"
    fig.savefig(out, dpi=130)
    print("saved:", out)
    print("root a=1; four children a =", [int(round(avals[i])) for i in range(1, 5)])


if __name__ == "__main__":
    main()
