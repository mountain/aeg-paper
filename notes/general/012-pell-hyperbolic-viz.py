#!/usr/bin/env python3
"""
012 — Visualizing the Pell convergents  x_n = P_n/Q_n,  (1+sqrt2)^n = P_n + Q_n sqrt2.

Two geometric readings combined in one 2x2 figure:

  (a) AEG / HTWR (Axiom I) reading.  Each convergent is a rational cusp p/q on
      the boundary of the upper half-plane H^2 carrying a Ford circle of radius
      1/(2 q^2).  The HTWR information height I = ln max(|p|,|q|) is the
      hyperbolic distance from the base point i to that Ford circle.  The
      Pell convergents' Ford circles shrink geometrically and pile up at the
      cusp sqrt2, alternating above/below it.

  (b) The units of Z[sqrt2].  (1+sqrt2)^n = P_n + Q_n sqrt2 are the units of
      the ring; (Q_n, P_n) run along the hyperbolas P^2 - 2 Q^2 = (-1)^n,
      approaching the asymptote P = sqrt2 Q (slope sqrt2 = lim P_n/Q_n).
      This norm identity is the arithmetic source of the cancellation wormhole.

  (c) The {inf,4} order-4 apeirogonal tiling (the Math.SE "enumeration of
      Q[sqrt2]" skeleton): the iterated-function system
          F1: z -> k f(z),  F2: z -> f(z/k),  F3: z -> k f^{-1}(z),
          F4: z -> f^{-1}(z/k),   f(z)=(z-1)/(z+1),  k = 3-2sqrt2
      tiles H^2 with geodesics whose ideal endpoints lie in Q[sqrt2].  The
      Pell convergent cusps P_n/Q_n (rational, hence in Q[sqrt2]) are marked
      on the boundary, accumulating at sqrt2.

  (d) Convergence and depth.  |x_n - sqrt2| ~= 2 sqrt2 k^n decays geometrically
      with rate k = (sqrt2 - 1)^2, while the HTWR depth I(x_n) = ln P_n grows
      linearly with slope ln(1+sqrt2).

The unifying constant is  k = 3 - 2 sqrt2 = (sqrt2 - 1)^2 = |mu/lam| = lam^{-2}:
  * the Pell contraction factor |mu/lam| (closed form),
  * the inverse square of the silver ratio lam = 1 + sqrt2,
  * the fundamental constant of the {inf,4} tiling, and
  * the convergence rate |x_n - sqrt2| = 2 sqrt2 k^n (1 + o(1)).

STATUS (per AGENTS.md): every identity and curve rendered here is an exact
classical fact (computationally verified); the "AEG/HTWR height" reading of
panel (a) is the Axiom I interpretation (STRUCTURAL PROPOSAL), not a theorem.
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from math import sqrt, log, pi

SQ2 = sqrt(2.0)
LAM = 1.0 + SQ2          # silver ratio
K = 3.0 - 2.0 * SQ2      # = (SQ2-1)^2 = LAM^-2 = |mu/lam|
H0 = log(LAM)            # single-step hyperbolic depth increment

# ---------------------------------------------------------------------------
# Pell convergents
# ---------------------------------------------------------------------------

def pell_pair(n):
    P, Q = 1, 0
    for _ in range(n):
        P, Q = P + 2 * Q, P + Q
    return P, Q


def convergent(n):
    P, Q = pell_pair(n)
    return P / Q  # float


# ---------------------------------------------------------------------------
# Panel (a): Ford circles + HTWR height
# ---------------------------------------------------------------------------

def draw_geodesic_through_i(ax, x, color, lw=1.0, ls="--"):
    """Geodesic (semicircle) of H^2 through base point i=(0,1) and cusp (x,0)."""
    if x == 0:
        return
    cx = (x * x - 1.0) / (2.0 * x)
    R = sqrt(cx * cx + 1.0)
    t = np.linspace(0.0, pi, 400)
    ax.plot(cx + R * np.cos(t), R * np.sin(t), color=color, lw=lw, ls=ls,
            zorder=1, alpha=0.55)


def panel_ford(ax, nmax=8):
    ax.axhline(0, color="0.3", lw=1.2)
    ax.plot([SQ2, SQ2], [0, 1.0], color="purple", lw=1.0, ls=":",
            zorder=2)
    ax.plot([SQ2], [0], marker="o", ms=5, color="purple", zorder=5)
    ax.text(SQ2, 1.03, r"$\sqrt{2}$ (cusp)", color="purple", ha="center",
            fontsize=9)
    ax.plot([0], [1], marker="o", ms=6, color="k", zorder=5)
    ax.text(0.02, 1.02, "$i$ (base)", fontsize=9)

    for n in range(1, nmax + 1):
        P, Q = pell_pair(n)
        x = P / Q
        r = 1.0 / (2.0 * Q * Q)
        col = "tab:red" if n % 2 == 0 else "tab:blue"
        draw_geodesic_through_i(ax, x, col, lw=0.7)
        if r > 2.5e-3:
            ax.add_patch(plt.Circle((x, r), r, fill=False, ec=col, lw=1.3,
                                    zorder=3))
        ax.plot([x], [0], marker="o", ms=4 if r > 2.5e-3 else 3, color=col,
                zorder=4)
        off = 0.012
        ax.text(x, 0.10 + off, f"{P}/{Q}", color=col, fontsize=7.5,
                ha="center", rotation=70)
        ax.text(x, r + 0.04, f"I={log(P):.2f}", color=col, fontsize=6.5,
                ha="center")
    ax.set_xlim(-0.08, 2.12)
    ax.set_ylim(0, 1.12)
    ax.set_aspect("equal")
    ax.set_xlabel("real axis (cusp coordinate $p/q$)")
    ax.set_ylabel(r"$\Im z$")
    ax.set_title(r"(a) HTWR Axiom I — Ford circles of $x_n=P_n/Q_n$; "
                 r"height $I=\ln P_n$", fontsize=9)


# ---------------------------------------------------------------------------
# Panel (b): units of Z[sqrt2] on the norm hyperbolas
# ---------------------------------------------------------------------------

def panel_units(ax, nmax=12):
    qq = np.linspace(0, 420, 800)
    ax.plot(qq, np.sqrt(2 * qq * qq + 1), color="0.6", lw=1.0,
            label=r"$P^2-2Q^2=+1$")
    qm = np.linspace(1.0 / SQ2, 420, 800)
    ax.plot(qm, np.sqrt(np.maximum(2 * qm * qm - 1, 0.0)), color="0.75", lw=1.0,
            label=r"$P^2-2Q^2=-1$")
    ax.plot(qq, SQ2 * qq, color="purple", lw=1.0, ls=":",
            label=r"asymptote $P=\sqrt{2}\,Q$")
    Qs, Ps = [], []
    for n in range(1, nmax + 1):
        P, Q = pell_pair(n)
        Qs.append(Q)
        Ps.append(P)
    ax.plot(Qs, Ps, "o-", color="k", ms=4, lw=0.8, zorder=3)
    for n in range(1, nmax + 1):
        P, Q = pell_pair(n)
        ax.annotate(f"({Q},{P})", (Q, P), textcoords="offset points",
                    xytext=(5, 4), fontsize=6.5,
                    color="tab:red" if n % 2 == 0 else "tab:blue")
    ax.set_xlabel("$Q_n$")
    ax.set_ylabel("$P_n$")
    ax.set_title(r"(b) units $(1+\sqrt{2})^n=P_n+Q_n\sqrt{2}$ on $P^2-2Q^2=(\pm1)^n$",
                 fontsize=9)
    ax.legend(fontsize=7, loc="upper left")
    ax.set_xlim(0, 430)
    ax.set_ylim(0, 600)


# ---------------------------------------------------------------------------
# Panel (c): {inf,4} apeirogonal tiling skeleton (Math.SE IFS)
# ---------------------------------------------------------------------------

INF = float("inf")

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


def apply_map_n(M, u, v, n):
    for _ in range(n):
        u = mobius(M, u)
        v = mobius(M, v)
    return u, v


def generate_geodesics(depth, orbit=6):
    """Finite-depth skeleton of the {inf,4} IFS.

    Returns a set of (u, v) ideal endpoints (u < v, possibly +inf).
    """
    geo = {(0.0, INF)}
    frontier = [(0.0, INF)]
    for _ in range(depth):
        new = []
        for (u, v) in frontier:
            for M in MAPS:
                for j in range(1, orbit + 1):
                    uu, vv = apply_map_n(M, u, v, j)
                    a, b = (uu, vv) if uu < vv else (vv, uu)
                    if (a, b) not in geo:
                        geo.add((a, b))
                        new.append((a, b))
        frontier = new
    return geo


def draw_arc(ax, a, b, color, lw=0.7, alpha=0.85):
    """Geodesic (semicircle) with finite ideal endpoints a < b."""
    if b - a > 1e4:
        return
    c = (a + b) / 2.0
    R = (b - a) / 2.0
    t = np.linspace(0.0, pi, 240)
    ax.plot(c + R * np.cos(t), R * np.sin(t), color=color, lw=lw,
            alpha=alpha, zorder=1)


def panel_tiling(ax, chain_len=8):
    xmin, xmax, ymax = -1.35, 2.05, 1.15
    ax.axhline(0, color="0.3", lw=1.2, zorder=2)
    # root geodesic A0 = positive y-axis
    ax.plot([0, 0], [0, ymax], color="0.2", lw=1.8, zorder=3)
    ax.text(-0.06, 0.6, "$A_0$", fontsize=9, ha="right")
    # the 4 parabolic chains  F_i^j(A0),  j = 1..chain_len
    chain_colors = ["tab:orange", "tab:green", "tab:purple", "tab:cyan"]
    for ci, M in enumerate(MAPS):
        u, v = 0.0, INF
        for j in range(1, chain_len + 1):
            u = mobius(M, u)
            v = mobius(M, v)
            a, b = (u, v) if u < v else (v, u)
            draw_arc(ax, a, b, chain_colors[ci])
    # parabolic cusps of the tiling = fixed points of the maps, at +-(sqrt2-1)
    cusp = SQ2 - 1.0
    for x0, lab in [(-cusp, r"$1-\sqrt{2}$"), (cusp, r"$\sqrt{2}-1$")]:
        ax.plot([x0], [0], marker="o", ms=5, color="k", zorder=5)
        ax.text(x0, -0.14, lab, ha="center", fontsize=8)
    # Pell convergent cusps accumulating at sqrt2 = 1 + (sqrt2 - 1)
    for n in range(1, 7):
        P, Q = pell_pair(n)
        x = P / Q
        col = "tab:red" if n % 2 == 0 else "tab:blue"
        ax.plot([x], [0], marker="o", ms=4, color=col, zorder=5)
        ax.text(x, 0.05, f"{P}/{Q}", ha="center", fontsize=6.5, color=col,
                rotation=82)
    ax.plot([SQ2], [0], marker="o", ms=6, color="purple", zorder=6)
    ax.text(SQ2, 0.15, r"$\sqrt{2}$", color="purple", ha="center", fontsize=9)
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(0, ymax)
    ax.set_aspect("equal")
    ax.set_xlabel("boundary  (ideal endpoints in $\\mathbb{Q}[\\sqrt{2}]$)")
    ax.set_title(r"(c) $\{\infty,4\}$ skeleton — 4 parabolic chains $F_i^j A_0$, "
                 r"cusps at $\pm(\sqrt{2}-1)$", fontsize=9)


# ---------------------------------------------------------------------------
# Panel (d): convergence (rate k^n) and depth (linear)
# ---------------------------------------------------------------------------

def panel_convergence(ax):
    ns = np.arange(1, 15)
    errs = np.array([abs(convergent(n) - SQ2) for n in ns])
    depths = np.array([log(pell_pair(n)[0]) for n in ns])
    ax.semilogy(ns, errs, "o-", color="tab:red", label=r"$|x_n-\sqrt{2}|$")
    ax.semilogy(ns, 2 * SQ2 * K ** ns, ":", color="purple",
                label=r"$2\sqrt{2}\,k^n$ (rate $k$)")
    ax.set_xlabel("$n$")
    ax.set_ylabel(r"error $|x_n-\sqrt{2}|$  (log)", color="tab:red")
    ax.tick_params(axis="y", labelcolor="tab:red")
    ax2 = ax.twinx()
    ax2.plot(ns, depths, "s--", color="tab:blue",
             label=r"depth $I(x_n)=\ln P_n$")
    ax2.set_ylabel(r"depth $I(x_n)$", color="tab:blue")
    ax2.tick_params(axis="y", labelcolor="tab:blue")
    ax.set_title(r"(d) error $=2\sqrt{2}\,k^n$ (geometric) vs depth (linear "
                 r"slope $\ln(1+\sqrt{2})$)", fontsize=9)
    ax.grid(True, ls=":", alpha=0.4)
    lines = ax.get_lines() + ax2.get_lines()
    ax.legend(lines, [l.get_label() for l in lines], fontsize=7,
              loc="center right")


# ---------------------------------------------------------------------------
# Build figure
# ---------------------------------------------------------------------------

def main():
    fig, axes = plt.subplots(2, 2, figsize=(12.4, 10.2))
    panel_ford(axes[0, 0])
    panel_units(axes[0, 1])
    panel_tiling(axes[1, 0])
    panel_convergence(axes[1, 1])
    fig.suptitle(
        r"Pell convergents $x_n=P_n/Q_n$ with $(1+\sqrt{2})^n=P_n+Q_n\sqrt{2}$:  "
        r"HTWR Ford-circle reading and the $\{\infty,4\}$ apeirogonal skeleton, "
        r"unified by $k=3-2\sqrt{2}=(\sqrt{2}-1)^2=\lambda^{-2}$",
        fontsize=11)
    fig.tight_layout(rect=[0, 0, 1, 0.97])
    out = "/Users/mingli/AEG/aeg-paper/notes/general/012-pell-hyperbolic-viz.png"
    fig.savefig(out, dpi=130)
    print("saved:", out)

    # numeric self-check
    print("\nself-check:")
    print("  k = 3-2sqrt2 =", K, "  lam^-2 =", LAM ** -2,
          "  (sqrt2-1)^2 =", (SQ2 - 1) ** 2)
    # parabolic fixed points of the four IFS maps = cusps +-(sqrt2-1)
    cusp = SQ2 - 1.0
    fixed = []
    for M in MAPS:
        a, b, c, d = M
        # fixed points of z -> (az+b)/(cz+d): c z^2 + (d-a) z - b = 0
        disc = (d - a) ** 2 + 4 * c * b
        if disc < 1e-12:
            fixed.append(-(d - a) / (2 * c))
        else:
            fixed.append(None)
    print("  IFS fixed points (cusps):", [round(f, 6) for f in fixed],
          " expect +/-", round(cusp, 6))
    for n in [4, 8, 12]:
        print(f"  n={n}: |x-sqrt2|={abs(convergent(n)-SQ2):.3e}  "
              f"2sqrt2 k^n={2*SQ2*K**n:.3e}")


if __name__ == "__main__":
    main()
