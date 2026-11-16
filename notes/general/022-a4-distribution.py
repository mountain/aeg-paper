#!/usr/bin/env python3
"""
022 — Distribution of the Hecke assignment  a_4 = (mu/lambda) sinh(lambda s).

Computed from first principles via the Schwarz triangle map of the (2,4,inf)
triangle group:
  s(z) = z^{1/2} 2F1(5/8,5/8;3/2;z) / 2F1(1/8,1/8;1/2;z),
  S(z) = ((eps4 - i)/s(1)) s(z) + i      (S(0)=i, S(1)=eps4, S(inf)=inf),
then  F = sqrt(z/(1-z)),  W = (F-i)/(F+i),  s = log|W|,  a_4 = (mu/lambda) sinh(lambda s).

The fundamental triangle (i, eps4, inf) in the disk has vertices (0, |mu| i, 1).
a_4 = 0 on the edge z in [0,1] (the {inf,4} zero net, the vertical segment
0 -> |mu| i in the disk); it grows like sinh radially away from it.

Left : a_4 colormap on the fundamental triangle (disk), with the zero set
       (edge 0 -> |mu| i) and level-set contours.
Right: |a_4| extended to the disk by the group <J,T> (|a_4| is Gamma_4-invariant),
       so the radial pattern fills the disk; a_4 itself is twisted by the sign
       character chi (chi(J)=-1, chi(T)=+1), so adjacent faces flip sign.

STATUS: Schwarz map + S(0)=i, S(1)=eps4 verified exactly; a_4 is the paper-3
thm:q4-hecke-zero-network assignment, computed numerically here.
"""

import mpmath as mp
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from math import sqrt, pi

mp.mp.dps = 18
SQ2 = sqrt(2.0)
EPS4C = (-1.0 + 1j) / SQ2          # eps4 complex
MUF = 1.0 - SQ2
LAMF = 1.0 + SQ2
CLIM = 3.0


def s_map(z):
    z = mp.mpc(z)
    num = mp.sqrt(z) * mp.hyp2f1(mp.mpf(5)/8, mp.mpf(5)/8, mp.mpf(3)/2, z)
    den = mp.hyp2f1(mp.mpf(1)/8, mp.mpf(1)/8, mp.mpf(1)/2, z)
    return num / den


S1 = mp.mpf(1)/2 * (mp.gamma(mp.mpf(3)/8) / mp.gamma(mp.mpf(7)/8))**2
A_COEF = (mp.mpc(EPS4C.real, EPS4C.imag) - 1j) / S1


def S_of_z(z):
    return A_COEF * s_map(z) + 1j


def a4_of_z(z):
    z = mp.mpc(z)
    F = mp.sqrt(z / (1 - z))
    W = (F - 1j) / (F + 1j)
    s_val = mp.log(abs(W))
    return (MUF / LAMF) * mp.sinh(LAMF * s_val)


def h2_to_disk(tau):
    return (tau - 1j) / (tau + 1j)


# group elements (matrices) and their sign chi
J = (0.0, -1.0, 1.0, 0.0)      # chi -1
T = (1.0, SQ2, 0.0, 1.0)       # chi +1
Tm = (1.0, -SQ2, 0.0, 1.0)     # chi +1


def apply_group(M, tau):
    a, b, c, d = M
    return (a * tau + b) / (c * tau + d)


def gen_group_words(maxlen):
    """Return list of (matrix, chi) for words in {J,T,Tm} up to maxlen."""
    words = {("",): (np.eye(2).tolist() if False else (1.0, 0.0, 0.0, 1.0), 1.0)}
    # use tuples of generator indices
    gens = [("J", J, -1.0), ("T", T, 1.0), ("Tm", Tm, 1.0)]
    out = [(J, -1.0), (T, 1.0), (Tm, 1.0)]  # seed? no, build from scratch
    out = []
    frontier = [( (1.0,0.0,0.0,1.0), 1.0 )]  # (matrix, chi)
    seen_mat = set()
    for L in range(maxlen):
        nxt = []
        for (M, ch) in frontier:
            for (gn, GM, gch) in gens:
                a,b,c,d = M
                ga,gb,gc,gd = GM
                # compose g * M  (apply g after M)
                M2 = (ga*a+gb*c, ga*b+gb*d, gc*a+gd*c, gc*b+gd*d)
                ch2 = ch * gch
                key = tuple(round(x,9) for x in M2)
                if key in seen_mat:
                    continue
                seen_mat.add(key)
                nxt.append((M2, ch2))
                out.append((M2, ch2))
        frontier = nxt
    return out


def main():
    # ---- fundamental triangle: z grid ----
    us = np.linspace(-0.4, 1.6, 90)
    vs = np.linspace(0.02, 0.9, 70)
    pts = []   # (disk_x, disk_y, a4)
    for u in us:
        for v in vs:
            z = mp.mpc(u, v)
            try:
                tau = S_of_z(z)
                a4 = a4_of_z(z)
                w = h2_to_disk(tau)
                pts.append((float(w.real), float(w.imag), float(a4)))
            except Exception:
                continue
    P = np.array(pts)
    X, Y, A = P[:, 0], P[:, 1], P[:, 2]
    A = np.clip(A, -CLIM, CLIM)

    # ---- group extension: |a4| invariant ----
    words = gen_group_words(5)
    pts2 = []
    for (M, ch) in words:
        for (x, y, a) in pts:
            tau = 1j * (1 + (x + 1j*y)) / (1 - (x + 1j*y))  # disk -> H
            tau2 = apply_group(M, tau)
            w2 = h2_to_disk(tau2)
            pts2.append((float(w2.real), float(w2.imag), abs(a)))
    P2 = np.array(pts2)
    X2, Y2, A2 = P2[:, 0], P2[:, 1], P2[:, 2]
    A2 = np.clip(A2, 0, CLIM)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12.2, 6.1))
    th = np.linspace(0, 2*pi, 400)
    for ax in (ax1, ax2):
        ax.plot(np.cos(th), np.sin(th), color="0.2", lw=1.1)

    sc1 = ax1.scatter(X, Y, c=A, cmap="RdBu_r", s=8, vmin=-CLIM, vmax=CLIM,
                      linewidths=0)
    # zero set = edge 0 -> |mu| i (vertical segment in disk)
    ax1.plot([0, 0], [0, abs(MUF)], color="lime", lw=2.6, zorder=5)
    ax1.plot([0], [abs(MUF)], marker="o", ms=5, color="k", zorder=6)
    ax1.text(0.02, abs(MUF)*0.55, r"$a_4=0$", color="lime", fontsize=9)
    ax1.set_title(r"fundamental triangle: $a_4=\frac{\mu}{\lambda}\sinh(\lambda s)$",
                  fontsize=10)
    ax1.set_aspect("equal"); ax1.set_xticks([]); ax1.set_yticks([])
    for sp in ax1.spines.values():
        sp.set_visible(False)

    sc2 = ax2.scatter(X2, Y2, c=A2, cmap="viridis", s=6, vmin=0, vmax=CLIM,
                      linewidths=0)
    ax2.plot([0, 0], [0, abs(MUF)], color="lime", lw=2.0, zorder=5)
    ax2.set_title(r"$|a_4|$ on the disk ($\Gamma_4$-invariant; sign twisted by "
                  r"$\chi$)", fontsize=10)
    ax2.set_aspect("equal"); ax2.set_xticks([]); ax2.set_yticks([])
    for sp in ax2.spines.values():
        sp.set_visible(False)

    cb = fig.colorbar(sc2, ax=[ax1, ax2], fraction=0.03, pad=0.02)
    cb.set_label(r"$|a_4|$")
    fig.suptitle(
        r"distribution of $a_4=\frac{\mu}{\lambda}\sinh(\lambda\log|W|)$, "
        r"$\lambda=1+\sqrt{2},\ \mu=1-\sqrt{2}$ — zero on the $\{\infty,4\}$ net, "
        r"radial $\sinh$ growth", fontsize=11.5)
    fig.subplots_adjust(top=0.83, wspace=0.06)
    out = "/Users/mingli/AEG/aeg-paper/notes/general/022-a4-distribution.png"
    fig.savefig(out, dpi=130)
    print("saved:", out, " (pts:", len(pts), "extended:", len(pts2), ")")


if __name__ == "__main__":
    main()
