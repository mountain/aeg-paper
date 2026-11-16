#!/usr/bin/env python3
"""
017 — Hecke Hauptmodul zero network  Z(a_4) = beta^{-1}([0,1])  vs  the
Math.SE {inf,4} IFS skeleton, both in the Poincare disk.

The q=4 Hecke triangle group  Gamma_4 = <J, T>,  J: z->-1/z (order 2),
T: z->z+sqrt2 (parabolic), J^2=(JT)^4=1.  Its elliptic orbits:
  eps_2 = i            (order 2, bivalent zero point)
  eps_4 = (-1+i)/sqrt2 (order 4, four-valent zero point, cone angle 4pi)
The zero network is the Gamma_4-orbit of the geodesic arc from eps_2 to eps_4;
by paper-3 thm:q4-hecke-zero-network this equals beta^{-1}([0,1]), the {inf,4}
Hecke graph (4-valent vertices, infinitely many sides per face, parabolic cusps).

Left panel:  the Hecke zero network (eps_4 red 4-valent, eps_2 blue bivalent).
Right panel: the Math.SE {inf,4} IFS geodesic skeleton (full ideal geodesics),
             for the side-by-side comparison.

STATUS: eps_2/eps_4, J,T and the orbit are exact (verified); the identification
beta^{-1}([0,1]) = {inf,4} graph is paper-3's PROVED theorem, rendered here.
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from math import sqrt, pi, atan2, hypot

SQ2 = sqrt(2.0)
K = 3.0 - 2.0 * SQ2
INF = float("inf")


# ---- Hecke group ----
def J(z):
    return -1.0 / z


def T(z):
    return z + SQ2


def Tm(z):
    return z - SQ2


GENS = [J, T, Tm]
EPS2 = 1j                      # i
EPS4 = (-1.0 + 1j) / SQ2       # (-1+i)/sqrt2


def key(c):
    return complex(round(c.real, 6), round(c.imag, 6))


def h2_to_disk(z):
    return (z - 1j) / (z + 1j)


def hecke_network(depth=7):
    """Return edges [(a,b)], vertices eps2-set, eps4-set."""
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
            for g in GENS:
                new.append((g(a), g(b)))
        front = new
    v2 = set(key(a) for (a, _) in edges)
    v4 = set(key(b) for (_, b) in edges)
    return edges, v2, v4


def geodesic_arc_disk(a, b, n=80):
    px, py = a.real, a.imag
    qx, qy = b.real, b.imag
    if abs(qx - px) < 1e-12:
        x0 = px
        y = np.linspace(min(py, qy), max(py, qy), n)
        return h2_to_disk(x0 + 1j * y)
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


# ---- Math.SE IFS ----
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


def disk_geodesic(u, v, n=130):
    if u == INF or v == INF:
        x0 = v if u == INF else u
        y = np.logspace(-3, sqrt(40.0), n)
        return h2_to_disk(x0 + 1j * y)
    a, b = min(u, v), max(u, v)
    if b - a > 1e4:
        c = (a + b) / 2.0
        y = np.logspace(-3, sqrt(40.0), n)
        return h2_to_disk(c + 1j * y)
    c = (a + b) / 2.0
    R = (b - a) / 2.0
    t = np.linspace(1e-3, pi - 1e-3, n)
    return h2_to_disk((c + R * np.cos(t)) + 1j * (R * np.sin(t)))


# ---- panels ----
def panel_hecke(ax, edges, v2, v4):
    th = np.linspace(0, 2 * pi, 400)
    ax.plot(np.cos(th), np.sin(th), color="0.2", lw=1.2)
    for (a, b) in edges:
        w = geodesic_arc_disk(a, b)
        ax.plot(w.real, w.imag, color="tab:red", lw=0.9, alpha=0.85, zorder=3)
    for v in v4:
        w = h2_to_disk(v)
        ax.plot([w.real], [w.imag], marker="o", ms=5, color="tab:red", zorder=5)
    for v in v2:
        w = h2_to_disk(v)
        ax.plot([w.real], [w.imag], marker="o", ms=3.5, color="tab:blue", zorder=5)
    w0 = h2_to_disk(EPS2)
    ax.plot([w0.real], [w0.imag], marker="o", ms=6, color="k", zorder=6)
    ax.set_aspect("equal")
    ax.set_xticks([])
    ax.set_yticks([])
    for sp in ax.spines.values():
        sp.set_visible(False)
    ax.set_title(r"Hecke zero network $Z(a_4)=\beta^{-1}([0,1])$: "
                 r"red $=\varepsilon_4$ (4-valent), blue $=\varepsilon_2$",
                 fontsize=9)


def panel_ifs(ax, tree, chains):
    th = np.linspace(0, 2 * pi, 400)
    ax.plot(np.cos(th), np.sin(th), color="0.2", lw=1.2)
    colors = ["tab:orange", "tab:green", "tab:purple", "tab:cyan"]
    for ci, chain in enumerate(chains):
        for (u, v) in chain:
            w = disk_geodesic(u, v)
            ax.plot(w.real, w.imag, color=colors[ci], lw=0.9, alpha=0.85, zorder=3)
    for (u, v) in tree:
        if any((u, v) in c for c in chains):
            continue
        w = disk_geodesic(u, v)
        ax.plot(w.real, w.imag, color="0.7", lw=0.5, alpha=0.6, zorder=3)
    ax.set_aspect("equal")
    ax.set_xticks([])
    ax.set_yticks([])
    for sp in ax.spines.values():
        sp.set_visible(False)
    ax.set_title(r"Math.SE $\{\infty,4\}$ IFS skeleton (full ideal geodesics)",
                 fontsize=9)


def main():
    edges, v2, v4 = hecke_network(7)
    # valence check: eps4 vertices should be 4-valent, eps2 2-valent
    from collections import Counter
    deg4 = Counter()
    deg2 = Counter()
    for (a, b) in edges:
        deg4[key(b)] += 1
        deg2[key(a)] += 1
    v4_degrees = sorted(set(deg4.values()))
    v2_degrees = sorted(set(deg2.values()))
    print("edges:", len(edges), " eps4 vertices:", len(v4),
          " eps2 vertices:", len(v2))
    print("eps4 valences:", v4_degrees, " (expect {4})")
    print("eps2 valences:", v2_degrees, " (expect {2})")

    tree = gen_tree(4)
    chains = gen_chains(16)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12.4, 6.2))
    panel_hecke(ax1, edges, v2, v4)
    panel_ifs(ax2, tree, chains)
    fig.suptitle(
        r"$q{=}4$ Hecke Hauptmodul zero network vs the $\{\infty,4\}$ IFS "
        r"skeleton — same $\{\infty,4\}$ graph, two realizations",
        fontsize=12)
    fig.subplots_adjust(top=0.84, wspace=0.05)
    out = "/Users/mingli/AEG/aeg-paper/notes/general/017-hecke-zero-network-vs-ifs.png"
    fig.savefig(out, dpi=130)
    print("saved:", out)


if __name__ == "__main__":
    main()
