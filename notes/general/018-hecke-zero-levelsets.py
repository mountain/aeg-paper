#!/usr/bin/env python3
"""
018 — Hecke zero vertices sit on the E0 assignment's level sets.

Assignment a = -x/y  (regular AES E0).  On the q=4 Hecke zero network
beta^{-1}([0,1]):
  * order-4 vertices  eps_4 = (-1+i)/sqrt2  have  a = 2m+1  (odd integers);
  * order-2 vertices  eps_2 = i             have  a = n*sqrt2 (n in Z);
  * so a(eps_2)=0 and a(eps_4)=1 — exactly the Hauptmodul branch values.

The level set a = c maps in the disk (w = u+iv) to the circle
  u^2 + (v + 1/c)^2 = 1 + 1/c^2   (through w = -1 and w = +1),
  with a = 0 the real-axis diameter.  The E0 level sets a = n*sqrt2 pass through
  the eps_2 vertices and a = 2m+1 pass through the eps_4 vertices.

Also: w(eps_4) = (sqrt2-1) i = |mu| i  (the order-4 point sits at height |mu| on
the disk imaginary axis).  The parameter mu = 1-sqrt2 = -|mu| itself is NOT a
vertex a-value (it is neither n*sqrt2 nor an odd integer).

Left panel: Hecke zero network (red eps_4 4-valent, blue eps_2 bivalent).
Right panel: same network + the E0 level-set circles a = 0, +-1, +-sqrt2, +-2,
             +-3, showing every vertex lying on one of these level sets.

STATUS: vertex a-values are computed exactly (BFS over Gamma_4); the "n*sqrt2 /
2m+1" pattern is a COMPUTATIONALLY VERIFIED observation, not yet proved in-paper.
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from math import sqrt, pi, atan2, hypot
from collections import Counter

SQ2 = sqrt(2.0)
MU = 1.0 - SQ2          # -|mu| = -(sqrt2-1)
ABSMU = SQ2 - 1.0       # |mu|


def J(z):
    return -1.0 / z


def T(z):
    return z + SQ2


def Tm(z):
    return z - SQ2


GENS = [J, T, Tm]
EPS2 = 1j
EPS4 = (-1.0 + 1j) / SQ2


def key(c):
    return complex(round(c.real, 6), round(c.imag, 6))


def h2_to_disk(z):
    return (z - 1j) / (z + 1j)


def aval(z):
    return -z.real / z.imag


def hecke_network(depth=7):
    edges, v2, v4 = [], set(), set()
    a2, a4 = [], []
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
            v2.add(key(a))
            v4.add(key(b))
            a2.append(aval(a))
            a4.append(aval(b))
            for g in GENS:
                new.append((g(a), g(b)))
        front = new
    return edges, v2, v4, a2, a4


def geodesic_arc_disk(a, b, n=70):
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


def level_circle(c, n=400):
    """The disk circle a = c (u^2 + (v+1/c)^2 = 1 + 1/c^2), through (-1,0),(1,0)."""
    if abs(c) < 1e-12:
        t = np.linspace(-1, 1, n)
        return t, np.zeros_like(t)
    cy = -1.0 / c
    R = hypot(1.0, cy)
    th = np.linspace(0, 2 * pi, n)
    return R * np.cos(th), cy + R * np.sin(th)


def draw_network(ax, edges, v2, v4, show_verts=True):
    th = np.linspace(0, 2 * pi, 400)
    ax.plot(np.cos(th), np.sin(th), color="0.2", lw=1.2)
    for (a, b) in edges:
        w = geodesic_arc_disk(a, b)
        ax.plot(w.real, w.imag, color="tab:red", lw=0.85, alpha=0.8, zorder=3)
    if show_verts:
        for v in v4:
            w = h2_to_disk(v)
            ax.plot([w.real], [w.imag], marker="o", ms=4.5, color="tab:red",
                    zorder=5)
        for v in v2:
            w = h2_to_disk(v)
            ax.plot([w.real], [w.imag], marker="o", ms=3.2, color="tab:blue",
                    zorder=5)
    ax.set_aspect("equal")
    ax.set_xticks([])
    ax.set_yticks([])
    for sp in ax.spines.values():
        sp.set_visible(False)


def main():
    edges, v2, v4, a2_full, a4_full = hecke_network(7)
    # a-values (full precision, dedup to 12 decimals)
    a2 = sorted({round(v, 12) for v in a2_full})
    a4 = sorted({round(v, 12) for v in a4_full})
    print("eps2 a-values (#distinct):", len(a2), " range", a2[0], a2[-1])
    print("eps4 a-values (#distinct):", len(a4), " sample", a4[:6], "...", a4[-6:])
    n2 = [v / SQ2 for v in a2 if abs(v) > 1e-9]
    print("eps2 values / sqrt2 are integers:",
          all(abs(n - round(n)) < 1e-8 for n in n2))
    print("eps4 values all odd integers:",
          all(abs(v - round(v)) < 1e-8 and int(round(v)) % 2 == 1 for v in a4))
    print("w(eps4) =", h2_to_disk(EPS4), " == |mu| i =", ABSMU)
    print("mu = 1-sqrt2 =", MU, " in vertex a-values?", MU in a2 or MU in a4)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12.2, 6.1))
    draw_network(ax1, edges, v2, v4)
    ax1.set_title(r"Hecke zero network (red $\varepsilon_4$, blue $\varepsilon_2$)",
                  fontsize=10)

    draw_network(ax2, edges, v2, v4)
    for c in [0, 1, -1, SQ2, -SQ2, 2, -2, 3, -3]:
        u, v = level_circle(c)
        ax2.plot(u, v, color="0.45", lw=0.55, alpha=0.55, ls="--", zorder=2)
    # mark eps4 image at |mu| i
    w4 = h2_to_disk(EPS4)
    ax2.plot([w4.real], [w4.imag], marker="*", ms=15, color="k", zorder=6)
    ax2.text(w4.real, w4.imag - 0.12, r"$w(\varepsilon_4)=|\mu|\,i$", fontsize=8,
             ha="center", color="k")
    ax2.set_title(r"$+$ $E_0$ level sets $a=0,\pm1,\pm\sqrt{2},\pm2,\pm3$ "
                  r"(vertices lie on them)", fontsize=10)

    fig.suptitle(
        r"$E_0$ assignment $a=-x/y$ on the Hecke network: "
        r"$\varepsilon_2\mapsto n\sqrt{2}$, $\varepsilon_4\mapsto 2m{+}1$ "
        r"($a(\varepsilon_2)=0,\ a(\varepsilon_4)=1$); $w(\varepsilon_4)=|\mu|i$",
        fontsize=11.5)
    fig.subplots_adjust(top=0.82, wspace=0.05)
    out = "/Users/mingli/AEG/aeg-paper/notes/general/018-hecke-zero-levelsets.png"
    fig.savefig(out, dpi=130)
    print("saved:", out)


if __name__ == "__main__":
    main()
