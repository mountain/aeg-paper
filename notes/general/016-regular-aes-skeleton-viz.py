#!/usr/bin/env python3
"""
016 — Regular AES  E0  with the {inf,4} apeirogonal skeleton overlaid.

The key coincidence: the {inf,4} tiling's root arm  A0 = positive y-axis  is
EXACTLY the zero set  Z(a) = {a = 0} = {x = 0}  of the assignment a = -x/y.

Shared constant k = 3-2sqrt2 = mu^2 = (sqrt2-1)^2:
  * the {inf,4} IFS (F1..F4) uses this k and has parabolic cusps at +-(sqrt2-1)
    = +-|mu| on the boundary;
  * the regular AES has  |grad a|^2 = mu^2 + lambda^2 a^2 = k + (1/k) a^2,
    with lambda = 1+sqrt2 = 1/|mu| and curvature K = -lambda^2 = -1/k.

Left panel  (upper half-plane):  a = -x/y   (level sets = rays through 0).
Right panel (Poincare disk):     a = 2v/(1-rho^2)  (level sets = circles through
                                 w = -1 and w = +1).

Overlaid in both: the {inf,4} skeleton (4 parabolic chains + 4-ary tree), the
zero set A0 = Z(a) (lime), and the boundary cusps +-(sqrt2-1) = +-|mu|.

STATUS: classical exact identities + the A0 = Z(a) coincidence (computationally
verified); the "same k" reading is a STRUCTURAL PROPOSAL, not a theorem.
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from math import sqrt, log, pi

SQ2 = sqrt(2.0)
K = 3.0 - 2.0 * SQ2              # = (sqrt2-1)^2 = mu^2
MU = 1.0 - SQ2                   # = -(sqrt2-1),  |mu| = sqrt2-1
LAM = 1.0 + SQ2                  # = 1/|mu|
INF = float("inf")
CUSP = SQ2 - 1.0                 # = |mu|

CMAP = "RdBu_r"
CLIM = 3.0
LEVS = [-3, -2, -1, -0.5, 0, 0.5, 1, 2, 3]
CHAIN_COLORS = ["tab:orange", "tab:green", "tab:purple", "tab:cyan"]


def mobius(M, x):
    a, b, c, d = M
    if x == INF:
        return a / c if c != 0 else INF
    den = c * x + d
    if abs(den) < 1e-13:
        return INF
    return (a * x + b) / den


F1 = (K, -K, 1.0, 1.0)
F2 = (1.0, -K, 1.0, K)
F3 = (K, K, -1.0, 1.0)
F4 = (1.0, K, -1.0, K)
MAPS = [F1, F2, F3, F4]


def gen_tree(depth):
    geo = {(0.0, INF)}
    front = [(0.0, INF)]
    for _ in range(depth):
        new = []
        for (u, v) in front:
            for M in MAPS:
                uu, vv = mobius(M, u), mobius(M, v)
                a, b = (uu, vv) if uu < vv else (vv, uu)
                if (a, b) not in geo:
                    geo.add((a, b))
                    new.append((a, b))
        front = new
    return geo


def gen_chains(length):
    chains = []
    for M in MAPS:
        c = []
        u, v = 0.0, INF
        for _ in range(length):
            u, v = mobius(M, u), mobius(M, v)
            a, b = (u, v) if u < v else (v, u)
            c.append((a, b))
        chains.append(c)
    return chains


def h2_to_disk(z):
    return (z - 1j) / (z + 1j)


def boundary_point(x):
    if x == INF:
        return 1.0 + 0.0j
    return (x - 1j) / (x + 1j)


def draw_h2_arc(ax, u, v, xmin, xmax, ymax, color, lw, alpha):
    """Draw the H^2 geodesic (semicircle) with ideal endpoints (u,v), clipped."""
    if u == INF or v == INF:
        x0 = v if u == INF else u
        if xmin <= x0 <= xmax:
            ax.plot([x0, x0], [0, ymax], color=color, lw=lw, alpha=alpha,
                    zorder=3)
        return
    a, b = min(u, v), max(u, v)
    if b - a > 1e4:
        return
    c = (a + b) / 2.0
    R = (b - a) / 2.0
    t = np.linspace(1e-3, pi - 1e-3, 160)
    xx = c + R * np.cos(t)
    yy = R * np.sin(t)
    keep = (xx >= xmin) & (xx <= xmax) & (yy <= ymax)
    if keep.any():
        ax.plot(xx[keep], yy[keep], color=color, lw=lw, alpha=alpha, zorder=3)


def disk_geodesic(u, v, n=140):
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


# ---------------- panels ----------------

def panel_h2(ax, tree, chains):
    n = 620
    x = np.linspace(-1.75, 1.75, n)
    y = np.linspace(0.02, 1.75, n)
    X, Y = np.meshgrid(x, y)
    A = np.clip(-X / Y, -CLIM, CLIM)
    ax.pcolormesh(X, Y, A, cmap=CMAP, vmin=-CLIM, vmax=CLIM, shading="auto",
                  zorder=0)

    # skeleton tree (light) + chains (colored)
    for (u, v) in tree:
        if any((u, v) in c for c in chains):
            continue
        draw_h2_arc(ax, u, v, -1.75, 1.75, 1.75, "white", 0.6, 0.75)
    for ci, chain in enumerate(chains):
        for (u, v) in chain:
            draw_h2_arc(ax, u, v, -1.75, 1.75, 1.75, CHAIN_COLORS[ci], 1.1, 0.95)

    ax.axhline(0, color="0.15", lw=1.6, zorder=4)              # boundary R
    ax.plot([0, 0], [0, 1.75], color="lime", lw=2.6, zorder=5)  # A0 = Z(a)
    ax.text(0.03, 1.55, r"$A_0=Z(a)$", color="lime", fontsize=10)
    # cusps at +-|mu| = +-(sqrt2-1)
    for x0 in (-CUSP, CUSP):
        ax.plot([x0], [0], marker="o", ms=6, color="k", zorder=6)
    ax.text(CUSP, -0.14, r"$+|μ|$", ha="center", fontsize=9)
    ax.text(-CUSP, -0.14, r"$-|μ|$", ha="center", fontsize=9)

    ax.set_xlim(-1.75, 1.75)
    ax.set_ylim(0, 1.75)
    ax.set_aspect("equal")
    ax.set_xlabel("$x$")
    ax.set_ylabel("$y$")
    ax.set_title(r"upper half-plane: $a=-x/y$ + $\{\infty,4\}$ skeleton; "
                 r"$A_0=Z(a)$, cusps $\pm(\sqrt{2}-1)=\pm|μ|$", fontsize=9)


def panel_disk(ax, tree, chains):
    n = 620
    u = np.linspace(-1.0, 1.0, n)
    v = np.linspace(-1.0, 1.0, n)
    U, V = np.meshgrid(u, v)
    rho2 = U * U + V * V
    A = np.clip(2 * V / (1 - rho2), -CLIM, CLIM)
    A = np.ma.masked_where(rho2 >= 1.0, A)
    ax.pcolormesh(U, V, A, cmap=CMAP, vmin=-CLIM, vmax=CLIM, shading="auto",
                  zorder=0)

    for (uu, vv) in tree:
        if any((uu, vv) in c for c in chains):
            continue
        w = disk_geodesic(uu, vv)
        ax.plot(w.real, w.imag, color="white", lw=0.55, alpha=0.7, zorder=3)
    for ci, chain in enumerate(chains):
        for (uu, vv) in chain:
            w = disk_geodesic(uu, vv)
            ax.plot(w.real, w.imag, color=CHAIN_COLORS[ci], lw=1.0, alpha=0.95,
                    zorder=3)

    th = np.linspace(0, 2 * pi, 400)
    ax.plot(np.cos(th), np.sin(th), color="0.15", lw=1.6, zorder=4)
    ax.plot([-1, 1], [0, 0], color="lime", lw=2.6, zorder=5)   # A0 = Z(a)
    ax.text(0.0, 0.045, r"$A_0=Z(a)$", color="lime", fontsize=9, ha="center")
    for x0 in (-CUSP, CUSP):
        w = boundary_point(x0)
        ax.plot([w.real], [w.imag], marker="o", ms=6, color="k", zorder=6)

    ax.set_aspect("equal")
    ax.set_xticks([])
    ax.set_yticks([])
    for sp in ax.spines.values():
        sp.set_visible(False)
    ax.set_title(r"Poincaré disk: $a=2v/(1-\rho^2)$ + $\{\infty,4\}$ skeleton",
                 fontsize=9)


def main():
    tree = gen_tree(4)
    chains = gen_chains(16)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13.4, 6.4))
    panel_h2(ax1, tree, chains)
    panel_disk(ax2, tree, chains)

    fig.suptitle(
        r"Regular AES $E_0$ with the $\{\infty,4\}$ apeirogonal skeleton: "
        r"$A_0=Z(a)$, cusps $\pm(\sqrt{2}-1)=\pm|μ|$, shared $k=3-2\sqrt{2}=μ^2$",
        fontsize=12)
    fig.subplots_adjust(top=0.85, wspace=0.18)
    out = "/Users/mingli/AEG/aeg-paper/notes/general/016-regular-aes-skeleton-viz.png"
    fig.savefig(out, dpi=130)
    print("saved:", out)
    print("  tree geodesics:", len(tree), " chain geodesics:", 4 * 16)
    print("  |mu| =", round(abs(MU), 6), " cusp =", round(CUSP, 6),
          " mu^2 = k =", round(MU * MU, 6))


if __name__ == "__main__":
    main()
