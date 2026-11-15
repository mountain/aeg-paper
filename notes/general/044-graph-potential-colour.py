#!/usr/bin/env python3
"""
044 — Colour the Cayley tree by the graph potential.

The potential problem on the D4 tree:  a(node) = (mu/lam) sinh(lam d(node)),
d(node) = g-path-length from the root (origin, a=0).  The edges carry the flow
rate  |grad a| = sqrt(mu^2+lam^2 a^2) = mu cosh(lam d).

Left panel : nodes coloured by a (log scale), edges coloured by the flow rate.
Right panel: the potential d itself (g-distance) as a colour field on the tree.
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from math import sin, cos, radians
from collections import deque

MU, LAM = 1.0, 2.0
NUMSTEPS = 4


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
        nx = cx + R * (-sin(a)); ny = cy + R * (cos(a))
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

    # g-lengths
    glen = {}
    for (p, q) in edges:
        n = 300
        ts = np.linspace(1e-4, 1 - 1e-4, n)
        xs = p[0] + (q[0] - p[0]) * ts
        ys = p[1] + (q[1] - p[1]) * ts
        Lv = np.array([Ltrue(x, y) for x, y in zip(xs, ys)])
        m = Lv > 1e-6
        seg = np.hypot(q[0] - p[0], q[1] - p[1])
        glen[(p, q)] = np.trapezoid(1.0 / Lv[m], ts[m]) * seg if m.any() else 0.0

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

    a_val = {u: (MU / LAM) * np.sinh(LAM * d) for u, d in dist.items()}
    flow = {u: MU * np.cosh(LAM * d) for u, d in dist.items()}

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13.6, 7.0))

    # ---------- left: a colouring ----------
    for (cx, cy, R) in sq:
        pts = np.array([(cx + R, cy), (cx, cy + R), (cx - R, cy), (cx, cy - R)])
        ax1.plot(np.append(pts[:, 0], pts[0, 0]), np.append(pts[:, 1], pts[0, 1]),
                 color="0.90", lw=0.3)
    vmax = max(a_val.values())
    for (p, q) in edges:
        vm = 0.5 * (a_val.get(p, 0) + a_val.get(q, 0))
        ax1.plot([p[0], q[0]], [p[1], q[1]],
                 color=plt.cm.plasma(np.log1p(vm) / np.log1p(vmax)),
                 lw=1.4, alpha=0.9)
    xs = [u[0] for u in a_val]; ys = [u[1] for u in a_val]
    cs = [np.log1p(a_val[u]) / np.log1p(vmax) for u in a_val]
    sc = ax1.scatter(xs, ys, c=cs, cmap="plasma", s=42, zorder=5,
                     edgecolors="k", linewidths=0.3)
    ax1.scatter([0], [0], marker="*", s=300, color="white", edgecolors="k",
                linewidths=1.0, zorder=7)
    ax1.set_aspect("equal"); ax1.set_xticks([]); ax1.set_yticks([])
    ax1.set_title(r"potential $a=\frac{\mu}{\lambda}\sinh(\lambda d)$ "
                  r"(log colour); edges = flow rate", fontsize=10)
    cb = fig.colorbar(sc, ax=ax1, fraction=0.045, pad=0.03)
    cb.set_label(r"$\log(1+a)$ (normalized)")

    # ---------- right: d colouring ----------
    for (cx, cy, R) in sq:
        pts = np.array([(cx + R, cy), (cx, cy + R), (cx - R, cy), (cx, cy - R)])
        ax2.plot(np.append(pts[:, 0], pts[0, 0]), np.append(pts[:, 1], pts[0, 1]),
                 color="0.90", lw=0.3)
    dmax = max(dist.values())
    for (p, q) in edges:
        dm = 0.5 * (dist.get(p, 0) + dist.get(q, 0))
        ax2.plot([p[0], q[0]], [p[1], q[1]],
                 color=plt.cm.viridis(dm / dmax), lw=1.4, alpha=0.9)
    ds = [dist[u] for u in dist]
    sc2 = ax2.scatter([u[0] for u in dist], [u[1] for u in dist],
                      c=ds, cmap="viridis", s=42, zorder=5,
                      edgecolors="k", linewidths=0.3)
    ax2.scatter([0], [0], marker="*", s=300, color="white", edgecolors="k",
                linewidths=1.0, zorder=7)
    ax2.set_aspect("equal"); ax2.set_xticks([]); ax2.set_yticks([])
    ax2.set_title(r"potential $d$ = $g$-path-length from the origin "
                  r"($a(0)=0$)", fontsize=10)
    cb2 = fig.colorbar(sc2, ax=ax2, fraction=0.045, pad=0.03)
    cb2.set_label(r"$d$ ($g$-distance)")

    fig.suptitle(r"graph potential colouring on the Cayley tree "
                 r"($\mu=1,\lambda=2$; nodes = singularities, edges = flow)",
                 fontsize=11)
    fig.subplots_adjust(top=0.90, wspace=0.06, left=0.03, right=0.97,
                        bottom=0.03)
    out = "/Users/mingli/AEG/aeg-paper/notes/general/044-graph-potential-colour.png"
    fig.savefig(out, dpi=140)
    print("saved:", out)
    print(f"nodes={len(a_val)}, a_max={vmax:.3e}, d_max={dmax:.3f}")


if __name__ == "__main__":
    main()
