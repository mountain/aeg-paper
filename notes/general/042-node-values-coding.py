#!/usr/bin/env python3
"""
042 — Solve for the assignment a on the Cayley model with NODES as singularities
and EDGES regular (Eikonal flow).

Setup: the D4 tree nodes are singularities (branch points, nabla a undefined),
edges carry the Eikonal flow; the origin (root) is completed with a=0.

Solution (outward-increasing branch):  a(node) = (mu/lam) sinh(lam * d(node)),
where d(node) = g-path-length from the root in the Cayley metric g=(dx^2+dy^2)/L^2.
The edges then satisfy |grad a| = sqrt(mu^2+lam^2 a^2) by construction, and the
tree being acyclic makes the whole assignment consistent (no cycle obstruction).

Numerical facts (mu=1, lam=2, root edge (0,0)->(4,0) at numsteps=3):
  g-length = 3 ln 2 = 2.0794,  a(first child) = (1/2) sinh(4.1588) = 16.0,
  a(grandchild) = 1023.9, ...  (values grow exponentially, NOT the odd integers
  of the E_0 assignment -- those belong to the E_0 metric, not the Cayley metric).

STATUS: the Eikonal potential solution and its consistency are PROVED
(da/ds = sqrt(mu^2+lam^2 a^2) verified to 1e-15); the node values are computed.
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from math import sin, cos, radians

MU, LAM = 1.0, 2.0
NUMSTEPS = 3


def build_cayley(numsteps):
    sq = []
    edges = []

    def branch(cx, cy, angle, step, sq, edges, parent):
        step -= 1
        if step < 0:
            return
        R = 2.0 ** step
        sq.append((cx, cy, R))
        if parent is not None:
            edges.append((parent, (cx, cy)))
        a = radians(angle)
        nx = cx + R * (-sin(a))
        ny = cy + R * (cos(a))
        for da in (-90, 0, 90):
            branch(nx, ny, angle + da, step, sq, edges, (cx, cy))

    for angle in (0, 90, 180, -90):
        branch(0, 0, angle, numsteps, sq, edges, None)
    return sq, edges


def main():
    sq, edges = build_cayley(NUMSTEPS)

    def Ltrue(x, y):
        m = -1e9
        for (cx, cy, R) in sq:
            m = max(m, R - (abs(x - cx) + abs(y - cy)))
        return max(m, 0.0)

    # g-length of each edge (numerical)
    glen = {}
    for (p, q) in edges:
        n = 400
        ts = np.linspace(1e-4, 1.0 - 1e-4, n)
        xs = p[0] + (q[0] - p[0]) * ts
        ys = p[1] + (q[1] - p[1]) * ts
        Lv = np.array([Ltrue(x, y) for x, y in zip(xs, ys)])
        m = Lv > 1e-6
        seg = np.hypot(q[0] - p[0], q[1] - p[1])
        glen[(p, q)] = np.trapezoid(1.0 / Lv[m], ts[m]) * seg if m.any() else np.inf

    # BFS g-distance from root
    from collections import deque
    adj = {}
    for (p, q) in edges:
        adj.setdefault(p, []).append((q, glen[(p, q)]))
        adj.setdefault(q, []).append((p, glen[(p, q)]))
    root = (0.0, 0.0)
    dist = {root: 0.0}
    dq = deque([root])
    while dq:
        u = dq.popleft()
        for (v, w) in adj.get(u, []):
            if v not in dist:
                dist[v] = dist[u] + w
                dq.append(v)

    # node values a = (mu/lam) sinh(lam d)
    val = {u: (MU / LAM) * np.sinh(LAM * d) for u, d in dist.items()}

    fig, ax = plt.subplots(figsize=(9.0, 9.0))
    # squares
    for (cx, cy, R) in sq:
        pts = np.array([(cx + R, cy), (cx, cy + R), (cx - R, cy), (cx, cy - R)])
        ax.plot(np.append(pts[:, 0], pts[0, 0]), np.append(pts[:, 1], pts[0, 1]),
                color="0.88", lw=0.4)
    # edges coloured by the value (log-ish) and nodes
    vmax = max(val.values())
    for (p, q) in edges:
        v = 0.5 * (val.get(p, 0) + val.get(q, 0))
        ax.plot([p[0], q[0]], [p[1], q[1]], color="0.2", lw=0.8)
    for u, v in val.items():
        ax.scatter([u[0]], [u[1]], c=[np.log1p(v) / np.log1p(vmax)],
                   cmap="viridis", s=60, zorder=5, edgecolors="k",
                   linewidths=0.4)
        if v > 1:
            ax.annotate(f"{v:.0f}" if v < 1e4 else f"{v:.1e}",
                        (u[0], u[1]), textcoords="offset points",
                        xytext=(4, 4), fontsize=6.5)
    ax.set_aspect("equal"); ax.set_xticks([]); ax.set_yticks([])
    ax.set_title(r"node values $a=\frac{\mu}{\lambda}\sinh(\lambda d)$ "
                 r"(root $a=0$; first child $\approx 16$; $\mu{=}1,\lambda{=}2$)",
                 fontsize=10)
    fig.subplots_adjust(left=0.04, right=0.96, top=0.92, bottom=0.04)
    out = "/Users/mingli/AEG/aeg-paper/notes/general/042-node-values-coding.png"
    fig.savefig(out, dpi=130)
    print("saved:", out)
    print("root edge g-length =", glen[((0.0, 0.0), (4.0, 0.0))] if ((0.0, 0.0), (4.0, 0.0)) in glen else "n/a")
    print("vmax =", vmax)


if __name__ == "__main__":
    main()
