#!/usr/bin/env python3
"""
020 — Assignment distribution and the dual grids {inf,4} vs {4,inf}.

The E0 assignment a = -x/y (disk: a = 2v/(1-rho^2)) has zero line a=0 = the
imaginary axis = the real-axis diameter of the disk.  At eps_2 = i this line is
PERPENDICULAR to the {inf,4} reference edge (the unit-circle arc i -> eps_4).
Hence a=0 is an edge of the DUAL tiling {4,inf}, not of {inf,4}.

  * {inf,4} (primal)  = orbit of the eps_2--eps_4 arc under <J,T> = the Hecke
    zero network  beta^{-1}([0,1])  (red arcs, 4-valent at eps_4).
  * {4,inf} (dual)    = orbit of the "0 line" A0 = (0,inf) under <J,T> = full
    geodesics through the cusps (blue), crossing the red arcs perpendicularly
    at the eps_2 points.

Left  : assignment a colormap (a = 2v/(1-rho^2)) + the primal network (red)
        + the dual full geodesics (blue).
Right : the two dual grids alone (red primal / blue dual), with eps_2 (origin)
        and eps_4 = |mu| i marked.

STATUS: eps_2/eps_4, the two orbits and the perpendicular crossing at eps_2 are
exact (verified); "{4,inf} = orbit of a=0" is a structural observation.
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from math import sqrt, log, pi, atan2, hypot

SQ2 = sqrt(2.0)
INF = float("inf")
MU = 1.0 - SQ2
ABSMU = SQ2 - 1.0


def mob(M, x):
    a, b, c, d = M
    if x == INF:
        return a / c if c != 0 else INF
    den = c * x + d
    if abs(den) < 1e-12:
        return INF
    return (a * x + b) / den


J = (0.0, -1.0, 1.0, 0.0)
T = (1.0, SQ2, 0.0, 1.0)
Tm = (1.0, -SQ2, 0.0, 1.0)
GENS = [J, T, Tm]
EPS2 = 1j
EPS4 = (-1.0 + 1j) / SQ2


def key(c):
    return complex(round(c.real, 6), round(c.imag, 6))


def h2_to_disk(z):
    return (z - 1j) / (z + 1j)


# ---- primal {inf,4}: orbit of eps2--eps4 arc ----
def primal(depth):
    edges = []
    seen = set()
    front = [(EPS2, EPS4)]
    for _ in range(depth + 1):
        new = []
        for (a, b) in front:
            k = frozenset([key(a), key(b)])
            if k in seen:
                continue
            seen.add(k)
            edges.append((a, b))
            for M in GENS:
                new.append((mob(M, a), mob(M, b)))
        front = new
    return edges


def arc_disk(a, b, n=70):
    px, py = a.real, a.imag
    qx, qy = b.real, b.imag
    if abs(qx - px) < 1e-12:
        y = np.linspace(min(py, qy), max(py, qy), n)
        return h2_to_disk(px + 1j * y)
    c = ((qx * qx + qy * qy) - (px * px + py * py)) / (2.0 * (qx - px))
    R = hypot(px - c, py)
    thp = atan2(py, px - c)
    thq = atan2(qy, qx - c)
    if thq < thp:
        thq += 2 * pi
    if thq - thp > pi:
        thp, thq = thq, thp + 2 * pi
    t = np.linspace(thp, thq, n)
    return h2_to_disk((c + R * np.cos(t)) + 1j * (R * np.sin(t)))


# ---- dual {4,inf}: orbit of the "0 line" A0 = (0,inf) ----
def dual(depth):
    seen = {(0.0, INF)}
    levels = [{(0.0, INF)}]
    for _ in range(depth):
        nxt = set()
        for (u, v) in levels[-1]:
            for M in GENS:
                uu, vv = mob(M, u), mob(M, v)
                a, b = (uu, vv) if uu < vv else (vv, uu)
                if (a, b) not in seen:
                    seen.add((a, b))
                    nxt.add((a, b))
        levels.append(nxt)
    return seen


def full_geodesic_disk(u, v, n=140):
    if u == INF or v == INF:
        x0 = v if u == INF else u
        y = np.logspace(-3, log(40.0), n)
        return h2_to_disk(x0 + 1j * y)
    a, b = min(u, v), max(u, v)
    if b - a > 1e4:
        c = (a + b) / 2.0
        y = np.logspace(-3, log(40.0), n)
        return h2_to_disk(c + 1j * y)
    c = (a + b) / 2.0
    R = (b - a) / 2.0
    t = np.linspace(1e-3, pi - 1e-3, n)
    return h2_to_disk((c + R * np.cos(t)) + 1j * (R * np.sin(t)))


def draw_boundary(ax):
    th = np.linspace(0, 2 * pi, 400)
    ax.plot(np.cos(th), np.sin(th), color="0.2", lw=1.2)


def draw_primal(ax, edges, lw=0.9, alpha=0.85):
    for (a, b) in edges:
        w = arc_disk(a, b)
        ax.plot(w.real, w.imag, color="tab:red", lw=lw, alpha=alpha, zorder=3)


def draw_dual(ax, geos, lw=0.7, alpha=0.8):
    for (u, v) in geos:
        w = full_geodesic_disk(u, v)
        ax.plot(w.real, w.imag, color="tab:blue", lw=lw, alpha=alpha, zorder=3)


def assignment_colormap(ax):
    n = 620
    u = np.linspace(-1.0, 1.0, n)
    v = np.linspace(-1.0, 1.0, n)
    U, V = np.meshgrid(u, v)
    rho2 = U * U + V * V
    A = np.clip(2 * V / (1 - rho2), -3.0, 3.0)
    A = np.ma.masked_where(rho2 >= 1.0, A)
    ax.pcolormesh(U, V, A, cmap="RdBu_r", vmin=-3, vmax=3, shading="auto",
                  zorder=0)


def main():
    edges = primal(6)
    geos = dual(4)
    print("primal {inf,4} edges:", len(edges), " dual {4,inf} geodesics:", len(geos))

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12.4, 6.2))

    assignment_colormap(ax1)
    draw_boundary(ax1)
    draw_dual(ax1, geos)
    draw_primal(ax1, edges)
    ax1.set_aspect("equal"); ax1.set_xticks([]); ax1.set_yticks([])
    for sp in ax1.spines.values():
        sp.set_visible(False)
    ax1.set_title(r"assignment $a=2v/(1-\rho^2)$ + primal $\{\infty,4\}$ (red) "
                  r"+ dual $\{4,\infty\}$ (blue)", fontsize=9.5)

    draw_boundary(ax2)
    draw_dual(ax2, geos)
    draw_primal(ax2, edges)
    w2 = h2_to_disk(EPS2)
    w4 = h2_to_disk(EPS4)
    ax2.plot([w2.real], [w2.imag], marker="o", ms=6, color="k", zorder=6)
    ax2.plot([w4.real], [w4.imag], marker="*", ms=15, color="k", zorder=6)
    ax2.text(w2.real, w2.imag - 0.08, r"$\varepsilon_2$", ha="center", fontsize=9)
    ax2.text(w4.real, w4.imag + 0.10, r"$\varepsilon_4=|\mu|i$", ha="center",
             fontsize=8)
    ax2.set_aspect("equal"); ax2.set_xticks([]); ax2.set_yticks([])
    for sp in ax2.spines.values():
        sp.set_visible(False)
    ax2.set_title(r"dual grids: primal $\{\infty,4\}$ (red) $\perp$ "
                  r"dual $\{4,\infty\}$ (blue) at $\varepsilon_2$", fontsize=10)

    fig.suptitle(
        r"the grid you imagined ($\{4,\infty\}$, from $a=0$ line) is the DUAL of "
        r"the Hecke zero network ($\{\infty,4\}$)", fontsize=12)
    fig.subplots_adjust(top=0.83, wspace=0.05)
    out = "/Users/mingli/AEG/aeg-paper/notes/general/020-dual-grids-assignment.png"
    fig.savefig(out, dpi=130)
    print("saved:", out)


if __name__ == "__main__":
    main()
