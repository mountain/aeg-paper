#!/usr/bin/env python3
"""
019 — The "0-line is not one": branching of the E0 zero line under add/multiply.

The regular AES E0 has assignment a = -x/y and the trivial zero line A0 =
positive y-axis (a=0).  The two arithmetic motions — add (T: z -> z+sqrt2) and
multiply/invert (J: z -> -1/z) — generate the q=4 Hecke group.  Their orbit of
the "0" line is NOT a single line: it branches (1 -> 2 -> 4 -> 8 -> 20 -> 40, ...)
into the {inf,4} apeirogonal tiling, whose geodesic endpoints lie in Q[sqrt2].

Left:  the branching generations, colored by generation (thick green = the "0"
       line A0, then red = gen1, blue = gen2, orange = gen3, grey = gen4), in
       the Poincare disk.
Right: the same, but every geodesic of the {inf,4} tiling (the full orbit), to
       show that the add/multiply propagation exhausts the apeirogonal skeleton.

KEY:  lambda = 1+sqrt2 = 1 + (add amount sqrt2);  mu = 1-sqrt2 = 1 - sqrt2.
The AES parameters (lambda, mu) = 1 +- sqrt2 ARE the "add +- sqrt2" amounts,
i.e. the fundamental unit and its conjugate of Z[sqrt2].

STATUS: the orbit branching is exact (BFS over <J,T>); the "add/multiply =
Hecke generators" identification is a STRUCTURAL observation, not a theorem.
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from math import sqrt, log, pi

SQ2 = sqrt(2.0)
INF = float("inf")


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


def orbit_levels(depth):
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
    return levels, seen


def h2_to_disk(z):
    return (z - 1j) / (z + 1j)


def disk_geodesic(u, v, n=120):
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


def draw_branching(ax, levels, colors, lws):
    th = np.linspace(0, 2 * pi, 400)
    ax.plot(np.cos(th), np.sin(th), color="0.2", lw=1.2)
    for L, col, lw in zip(levels, colors, lws):
        for (u, v) in L:
            w = disk_geodesic(u, v)
            ax.plot(w.real, w.imag, color=col, lw=lw, alpha=0.9, zorder=3)
    ax.set_aspect("equal")
    ax.set_xticks([])
    ax.set_yticks([])
    for sp in ax.spines.values():
        sp.set_visible(False)


def main():
    levels, seen = orbit_levels(4)
    print("generation counts:", [len(L) for L in levels],
          " total:", len(seen))

    colors = ["lime", "tab:red", "tab:blue", "tab:orange", "0.55"]
    lws = [2.6, 1.3, 1.0, 0.8, 0.5]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12.2, 6.1))
    draw_branching(ax1, levels, colors, lws)
    ax1.set_title(r"branching of the $0$-line $A_0$ under add($\sqrt{2}$)/invert: "
                  r"gen $0$=green, 1=red, 2=blue, 3=orange, 4=grey", fontsize=9.5)

    draw_branching(ax2, [seen], ["0.3"], [0.6])
    ax2.set_title(r"full orbit = the $\{\infty,4\}$ apeirogonal tiling "
                  r"(endpoints in $\mathbb{Q}[\sqrt{2}]$)", fontsize=10)

    fig.suptitle(
        r"the $0$-line is not one: $E_0$ zero line + add/multiply "
        r"$\Rightarrow$ $\{\infty,4\}$ network,  $\lambda,\mu=1\pm\sqrt{2}$ "
        r"$=$ the $\pm\sqrt{2}$ add-amounts", fontsize=12)
    fig.subplots_adjust(top=0.82, wspace=0.05)
    out = "/Users/mingli/AEG/aeg-paper/notes/general/019-zero-line-branching.png"
    fig.savefig(out, dpi=130)
    print("saved:", out)


if __name__ == "__main__":
    main()
