#!/usr/bin/env python3
"""
021 — The simple arithmetic interpretation: the Hecke metric is FLAT.

thm:q4-hecke-zero-network proves  g_4 = |dW/W|^2 = |d zeta|^2  with zeta = log W,
i.e. the Hecke Hauptmodul construction equips the zero network with the FLAT
(Euclidean) metric in the zeta-coordinate.  Writing zeta = s + i theta:

  s  = log|W|  (radial coordinate),   theta = arg W  (angular coordinate),
  a_4 = (mu/lambda) sinh(lambda s)  depends on s ALONE.

So the two dual grids are exactly the two coordinate families of a Euclidean
grid:
  * {inf,4} zero network  a_4 = 0  <=>  s = 0  = a vertical line (radial level);
  * {4,inf} dual grid                <=>  theta = const  = horizontal lines
    (angular levels), PERPENDICULAR to the radial level sets.

Left : the two dual grids in the disk (red {inf,4}, blue {4,inf}).
Right: the FLAT zeta-plane schematic — vertical red = radial level sets
       {s = const} (zero set at s = 0), horizontal blue = angular {theta=const}
       (the dual), with the assignment  a_4 = (mu/lambda) sinh(lambda s)  drawn
       as the radial profile.

STATUS: g_4 = |d zeta|^2 flat is PROVED (paper-3 thm:q4-hecke-zero-network);
a_4 depends on s alone is PROVED; the right panel is a schematic of that proved
flat structure (zeta not computed explicitly here — that needs the Hauptmodul).
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from math import sqrt, log, pi, atan2, hypot

SQ2 = sqrt(2.0)
INF = float("inf")
MU = 1.0 - SQ2
LAM = 1.0 + SQ2


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


def primal(depth):
    edges, seen, front = [], set(), [(EPS2, EPS4)]
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


def dual(depth):
    seen, levels = {(0.0, INF)}, [{(0.0, INF)}]
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


def arc_disk(a, b, n=60):
    px, py = a.real, a.imag
    qx, qy = b.real, b.imag
    if abs(qx - px) < 1e-12:
        y = np.linspace(min(py, qy), max(py, qy), n)
        return h2_to_disk(px + 1j * y)
    c = ((qx * qx + qy * qy) - (px * px + py * py)) / (2.0 * (qx - px))
    R = hypot(px - c, py)
    thp, thq = atan2(py, px - c), atan2(qy, qx - c)
    if thq < thp:
        thq += 2 * pi
    if thq - thp > pi:
        thp, thq = thq, thp + 2 * pi
    t = np.linspace(thp, thq, n)
    return h2_to_disk((c + R * np.cos(t)) + 1j * (R * np.sin(t)))


def full_geodesic_disk(u, v, n=120):
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


def panel_disk(ax, edges, geos):
    th = np.linspace(0, 2 * pi, 400)
    ax.plot(np.cos(th), np.sin(th), color="0.2", lw=1.1)
    for (u, v) in geos:
        w = full_geodesic_disk(u, v)
        ax.plot(w.real, w.imag, color="tab:blue", lw=0.6, alpha=0.8, zorder=2)
    for (a, b) in edges:
        w = arc_disk(a, b)
        ax.plot(w.real, w.imag, color="tab:red", lw=0.85, alpha=0.9, zorder=3)
    ax.set_aspect("equal"); ax.set_xticks([]); ax.set_yticks([])
    for sp in ax.spines.values():
        sp.set_visible(False)
    ax.set_title(r"disk: $\{\infty,4\}$ zero net (red) $\perp$ $\{4,\infty\}$ dual "
                 r"(blue)", fontsize=10)


def panel_flat(ax):
    # vertical radial level sets {s = const}:  s in {-2,-1,0,1,2}
    for s in [-2, -1, 0, 1, 2]:
        lw = 2.4 if abs(s) < 1e-9 else 0.8
        col = "tab:red"
        ax.plot([s, s], [-2, 2], color=col, lw=lw, alpha=0.9)
    # horizontal angular level sets {theta = const}
    for t in [-1.5, -0.75, 0, 0.75, 1.5]:
        lw = 2.0 if abs(t) < 1e-9 else 0.7
        ax.plot([-2, 2], [t, t], color="tab:blue", lw=lw, alpha=0.85)
    ax.text(0.06, 1.75, r"zero set $a_4=0$ ($s=0$)", color="tab:red", fontsize=9)
    ax.text(1.35, 0.08, r"dual ($\theta=\mathrm{const}$)", color="tab:blue",
            fontsize=9)
    # assignment profile a_4(s) = (mu/lambda) sinh(lambda s) on a secondary axis
    ss = np.linspace(-1.6, 1.6, 400)
    a4 = (MU / LAM) * np.sinh(LAM * ss)
    ax2 = ax.twinx()
    ax2.plot(ss, a4, color="k", lw=1.6, zorder=5)
    ax2.set_ylabel(r"$a_4=\frac{\mu}{\lambda}\sinh(\lambda s)$", color="k")
    ax2.set_ylim(-6, 6)
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.set_xlabel(r"$s=\log|W|$ (radial)")
    ax.set_ylabel(r"$\theta=\arg W$ (angular)", color="tab:blue")
    ax.set_aspect("equal")
    ax.set_title(r"FLAT $\zeta=s+i\theta$ plane: $g_4=|d\zeta|^2$ — the two dual "
                 r"grids are the coordinate lines", fontsize=9.5)


def main():
    edges = primal(6)
    geos = dual(4)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12.4, 6.0))
    panel_disk(ax1, edges, geos)
    panel_flat(ax2)
    fig.suptitle(
        r"the Hecke metric $g_4=|dW/W|^2=|d\zeta|^2$ is FLAT: zero net "
        r"$=$ radial level $s=0$, dual $=$ angular level $\theta=\mathrm{const}$, "
        r"$a_4=\frac{\mu}{\lambda}\sinh(\lambda s)$", fontsize=11.5)
    fig.subplots_adjust(top=0.82, wspace=0.22)
    out = "/Users/mingli/AEG/aeg-paper/notes/general/021-flat-hecke-grid.png"
    fig.savefig(out, dpi=130)
    print("saved:", out)
    print("g_4 = |d zeta|^2 is flat (paper-3, proved);  a_4 depends on s alone")


if __name__ == "__main__":
    main()
