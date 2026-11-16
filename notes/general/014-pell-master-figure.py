#!/usr/bin/env python3
"""
014 — Integrated master figure for the Pell convergents  x_n = P_n/Q_n,
      (1+sqrt2)^n = P_n + Q_n sqrt2.

A 2x3 panel that consolidates the HTWR Ford-circle reading, the {inf,4}
Poincare-disk tiling, the unit/norm structure, the convergence law, the
catalytic wormhole (with a large step k=8), and the Sylvester "no-wormhole"
control:

  (0,0)  Ford circles + HTWR height          (Axiom I reading)
  (0,1)  {inf,4} apeirogonal tiling (disk)   (Math.SE skeleton, k = 3-2sqrt2)
  (0,2)  units of Z[sqrt2] on P^2-2Q^2=+-1  (norm = wormhole source)
  (1,0)  |x_n - sqrt2| = 2 sqrt2 k^n vs linear depth
  (1,1)  catalytic wormhole depth profile, k=2 and k=8, with naive CF contrast
  (1,2)  Sylvester control: depth doubles, no norm -> no wormhole

Unifying constant  k = 3 - 2 sqrt2 = (sqrt2 - 1)^2 = lambda^{-2} = |mu/lambda|.

STATUS: identities/depths are exact classical arithmetic (verified); the
"wormhole" and "height" readings are HTWR Axiom I-II interpretations
(STRUCTURAL PROPOSAL), not theorems.
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from fractions import Fraction
from math import sqrt, log, pi

SQ2 = sqrt(2.0)
LAM = 1.0 + SQ2
K = 3.0 - 2.0 * SQ2
H0 = log(LAM)
INF = float("inf")


def pell_pair(n):
    P, Q = 1, 0
    for _ in range(n):
        P, Q = P + 2 * Q, P + Q
    return P, Q


def height(f):
    return log(max(abs(f.numerator), abs(f.denominator)))


# ---------------- {inf,4} IFS ----------------

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


def geodesic_disk_points(u, v, ymax=40.0, n=120):
    if u == INF or v == INF:
        x0 = v if u == INF else u
        y = np.logspace(-3.0, log(ymax), n)
        return h2_to_disk(x0 + 1j * y)
    a, b = min(u, v), max(u, v)
    if b - a > 1e4:
        c = (a + b) / 2.0
        y = np.logspace(-3.0, log(ymax), n)
        return h2_to_disk(c + 1j * y)
    c = (a + b) / 2.0
    R = (b - a) / 2.0
    t = np.linspace(1e-3, pi - 1e-3, n)
    return h2_to_disk((c + R * np.cos(t)) + 1j * (R * np.sin(t)))


# ---------------- panels ----------------

def panel_ford(ax, nmax=8):
    ax.axhline(0, color="0.3", lw=1.0)
    ax.plot([SQ2, SQ2], [0, 1.0], color="purple", lw=0.9, ls=":")
    ax.plot([SQ2], [0], marker="o", ms=5, color="purple", zorder=5)
    ax.text(SQ2, 1.03, r"$\sqrt{2}$", color="purple", ha="center", fontsize=8)
    ax.plot([0], [1], marker="o", ms=5, color="k", zorder=5)
    ax.text(0.03, 1.02, "$i$", fontsize=8)
    for n in range(1, nmax + 1):
        P, Q = pell_pair(n)
        x = P / Q
        r = 1.0 / (2.0 * Q * Q)
        col = "tab:red" if n % 2 == 0 else "tab:blue"
        cx = (x * x - 1.0) / (2.0 * x) if x else 0.0
        R = sqrt(cx * cx + 1.0)
        t = np.linspace(0, pi, 200)
        ax.plot(cx + R * np.cos(t), R * np.sin(t), color=col, lw=0.5,
                ls="--", alpha=0.5, zorder=1)
        if r > 2.5e-3:
            ax.add_patch(plt.Circle((x, r), r, fill=False, ec=col, lw=1.1,
                                    zorder=3))
        ax.plot([x], [0], marker="o", ms=4 if r > 2.5e-3 else 3, color=col,
                zorder=4)
    ax.set_xlim(-0.08, 2.12)
    ax.set_ylim(0, 1.12)
    ax.set_aspect("equal")
    ax.set_title(r"(a) HTWR Axiom I — Ford circles, height $I=\ln P_n$",
                 fontsize=9)
    ax.set_xlabel("cusp $p/q$")
    ax.set_ylabel(r"$\Im z$")


def panel_poincare(ax):
    th = np.linspace(0, 2 * pi, 400)
    ax.plot(np.cos(th), np.sin(th), color="0.25", lw=1.0)
    chains = gen_chains(20)
    chain_colors = ["tab:orange", "tab:green", "tab:purple", "tab:cyan"]
    for ci, chain in enumerate(chains):
        for (u, v) in chain:
            w = geodesic_disk_points(u, v)
            ax.plot(w.real, w.imag, color=chain_colors[ci], lw=0.6, alpha=0.75)
    tree = gen_tree(4)
    for (u, v) in tree:
        if any((u, v) in c for c in chains):
            continue
        w = geodesic_disk_points(u, v)
        ax.plot(w.real, w.imag, color="0.72", lw=0.4, alpha=0.5)
    cusp = SQ2 - 1.0
    for x0 in (-cusp, cusp):
        w = boundary_point(x0)
        ax.plot([w.real], [w.imag], marker="o", ms=6, color="k", zorder=6)
    for n in range(1, 9):
        P, Q = pell_pair(n)
        w = boundary_point(P / Q)
        col = "tab:red" if n % 2 == 0 else "tab:blue"
        ax.plot([w.real], [w.imag], marker="o", ms=4, color=col, zorder=6)
    wS = boundary_point(SQ2)
    ax.plot([wS.real], [wS.imag], marker="*", ms=13, color="purple", zorder=7)
    ax.text(wS.real * 1.06, wS.imag * 1.06, r"$w(\sqrt{2})$", color="purple",
            fontsize=8, ha="center")
    ax.plot([0], [0], marker="o", ms=4, color="k", zorder=6)
    ax.set_aspect("equal")
    ax.set_xlim(-1.15, 1.15)
    ax.set_ylim(-1.15, 1.15)
    ax.set_xticks([])
    ax.set_yticks([])
    for sp in ax.spines.values():
        sp.set_visible(False)
    ax.set_title(r"(b) $\{\infty,4\}$ tiling (disk), cusps $w(\pm(\sqrt{2}-1))$",
                 fontsize=9)


def panel_units(ax, nmax=10):
    qq = np.linspace(0, 200, 600)
    ax.plot(qq, np.sqrt(2 * qq * qq + 1), color="0.6", lw=1.0,
            label=r"$P^2-2Q^2=+1$")
    qm = np.linspace(1.0 / SQ2, 200, 600)
    ax.plot(qm, np.sqrt(np.maximum(2 * qm * qm - 1, 0)), color="0.75", lw=1.0,
            label=r"$P^2-2Q^2=-1$")
    ax.plot(qq, SQ2 * qq, color="purple", lw=0.9, ls=":",
            label=r"$P=\sqrt{2}\,Q$")
    Qs, Ps = [], []
    for n in range(1, nmax + 1):
        P, Q = pell_pair(n)
        Qs.append(Q)
        Ps.append(P)
    ax.plot(Qs, Ps, "o-", color="k", ms=3, lw=0.7, zorder=3)
    ax.set_xlabel("$Q_n$")
    ax.set_ylabel("$P_n$")
    ax.set_title(r"(c) units $(1+\sqrt{2})^n=P_n+Q_n\sqrt{2}$ — the norm wormhole "
                 r"source", fontsize=9)
    ax.legend(fontsize=7, loc="upper left")
    ax.set_xlim(0, 205)
    ax.set_ylim(0, 285)


def panel_convergence(ax):
    ns = np.arange(1, 15)
    errs = np.array([abs(pell_pair(n)[0] / pell_pair(n)[1] - SQ2) for n in ns])
    depths = np.array([log(pell_pair(n)[0]) for n in ns])
    ax.semilogy(ns, errs, "o-", color="tab:red", lw=1.2, ms=4,
                label=r"$|x_n-\sqrt{2}|$")
    ax.semilogy(ns, 2 * SQ2 * K ** ns, ":", color="purple", lw=1.4,
                label=r"$2\sqrt{2}\,k^n$")
    ax.set_xlabel("$n$")
    ax.set_ylabel(r"error (log)", color="tab:red")
    ax.tick_params(axis="y", labelcolor="tab:red")
    ax2 = ax.twinx()
    ax2.plot(ns, depths, "s--", color="tab:blue", lw=1.0, ms=3,
             label=r"$I(x_n)=\ln P_n$")
    ax2.set_ylabel(r"depth $I(x_n)$", color="tab:blue")
    ax2.tick_params(axis="y", labelcolor="tab:blue")
    ax.set_title(r"(d) error $=2\sqrt{2}\,k^n$ (rate $k$) vs linear depth",
                 fontsize=9)
    ax.grid(True, ls=":", alpha=0.4)


def wormhole_depths(n, k):
    xn = Fraction(pell_pair(n)[0], pell_pair(n)[1])
    xk = Fraction(pell_pair(k)[0], pell_pair(k)[1])
    ck = 2 - xk * xk
    z1 = xn + xk
    z2 = 1 / z1
    z3 = z2 * ck
    z4 = z3 + xk
    assert z4 == Fraction(pell_pair(n + k)[0], pell_pair(n + k)[1])
    return [height(s) for s in (xn, z1, z2, z3, z4)]


def panel_wormhole(ax):
    # k = 8 : x_4 -> x_12
    d8 = wormhole_depths(4, 8)
    g8 = np.arange(5)
    naive8 = [log(pell_pair(n)[0]) for n in range(4, 13)]
    ng8 = np.arange(0, 25, 3)  # 9 points, 3 gates per CF step
    # k = 2 : x_3 -> x_5
    d2 = wormhole_depths(3, 2)
    g2 = np.arange(5)
    naive2 = [log(pell_pair(n)[0]) for n in (3, 4, 5)]
    ng2 = np.arange(0, 7, 3)

    ax.plot(ng8, naive8, "s--", color="0.6", lw=1.2, ms=4,
            label="CF $x_4\\to x_{12}$ (24 gates)")
    ax.plot(g8, d8, "o-", color="tab:red", lw=2, ms=6, zorder=5,
            label="wormhole $k=8$ (4 gates)")
    ax.plot(ng2, naive2, "^:", color="0.75", lw=1.0, ms=4,
            label="CF $x_3\\to x_5$ (6 gates)")
    ax.plot(g2, d2, "o-", color="tab:blue", lw=1.4, ms=5, zorder=5,
            label="wormhole $k=2$ (4 gates)")

    # ghost (uncanceled) depths for k=8: two Q_k cancellations each save ln Q_8
    lnQ8 = log(pell_pair(8)[1])
    for gi, di, lab in [(3, d8[3], "#1 $\\div Q_8$"), (4, d8[4], "#2 Cassini")]:
        ax.plot([gi], [di + lnQ8], marker="o", mfc="none", mec="tab:red",
                ms=7, ls="none", zorder=4)
        ax.annotate("", xy=(gi, di), xytext=(gi, di + lnQ8),
                    arrowprops=dict(arrowstyle="->", color="tab:red", lw=0.9))
        ax.text(gi + 0.12, di + lnQ8 / 2, f"{lab}\nsaves $\\ln 408$",
                fontsize=6.5, color="tab:red", va="center")

    ax.axvline(4, color="tab:red", lw=0.8, ls=":", alpha=0.6)
    ax.text(4.15, 1.2, "wormhole done at gate 4", color="tab:red", fontsize=7)
    ax.set_xlim(-0.5, 24.5)
    ax.set_ylim(0, 20)
    ax.set_xlabel("gate index")
    ax.set_ylabel(r"information height $I=\ln\max(|p|,|q|)$")
    ax.set_title(r"(e) catalytic wormhole: dive into the abyss, collapse back; "
                 r"$k=8$ saves $2\ln408$", fontsize=9)
    ax.legend(fontsize=7, loc="upper left")
    ax.grid(True, ls=":", alpha=0.4)


def panel_sylvester(ax):
    ns = np.arange(0, 7)
    s = 2
    syl = []
    for _ in ns:
        syl.append(log(s))
        s = s * s - s + 1
    pn = np.arange(1, 8)
    pell_d = np.array([log(pell_pair(n)[0]) for n in pn])
    ax.plot(ns, syl, "o-", color="tab:green", lw=1.6, ms=6,
            label="Sylvester $\\ln s_n$ (doubles)")
    ax.plot(pn - 1, pell_d, "s-", color="tab:blue", lw=1.2, ms=4,
            label="Pell $\\ln P_n$ (linear)")
    # annotate doubling
    ax.annotate(r"$s_{n+1}=s_n^2-s_n+1$: no norm,", xy=(4.5, 20), fontsize=8,
                color="tab:green")
    ax.annotate(r"no cancellation wormhole", xy=(4.5, 16.5), fontsize=8,
                color="tab:green")
    ax.annotate(r"$\Rightarrow$ naive = optimal (note 004)", xy=(4.5, 13),
                fontsize=8, color="tab:green")
    ax.set_xlabel("$n$")
    ax.set_ylabel(r"depth $\ln$ (term)")
    ax.set_title(r"(f) Sylvester control — depth doubles, no wormhole",
                 fontsize=9)
    ax.legend(fontsize=8, loc="upper left")
    ax.set_ylim(0, 31)
    ax.grid(True, ls=":", alpha=0.4)


# ---------------- build ----------------

def main():
    fig, axes = plt.subplots(2, 3, figsize=(17.5, 10.6))
    panel_ford(axes[0, 0])
    panel_poincare(axes[0, 1])
    panel_units(axes[0, 2])
    panel_convergence(axes[1, 0])
    panel_wormhole(axes[1, 1])
    panel_sylvester(axes[1, 2])
    fig.suptitle(
        r"Pell convergents $x_n=P_n/Q_n$, $(1+\sqrt{2})^n=P_n+Q_n\sqrt{2}$:  "
        r"HTWR Ford-circle reading, $\{\infty,4\}$ disk tiling, and the "
        r"catalytic wormhole, unified by $k=3-2\sqrt{2}=(\sqrt{2}-1)^2=\lambda^{-2}$",
        fontsize=12)
    fig.tight_layout(rect=[0, 0, 1, 0.96])
    out = "/Users/mingli/AEG/aeg-paper/notes/general/014-pell-master-figure.png"
    fig.savefig(out, dpi=130)
    print("saved:", out)

    print("\nself-check:")
    print("  k=8 wormhole depths:", [round(d, 3) for d in wormhole_depths(4, 8)])
    print("  k=2 wormhole depths:", [round(d, 3) for d in wormhole_depths(3, 2)])
    print("  ln Q_8 =", round(log(pell_pair(8)[1]), 3), "(saved per wormhole)")
    s = 2
    syl = [log(s)]
    for _ in range(6):
        s = s * s - s + 1
        syl.append(log(s))
    print("  Sylvester ln s_n:", [round(d, 2) for d in syl])


if __name__ == "__main__":
    main()
