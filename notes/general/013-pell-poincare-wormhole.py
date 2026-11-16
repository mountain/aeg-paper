#!/usr/bin/env python3
"""
013 — Poincare-disk {inf,4} tiling and the Ford-circle four-gate wormhole.

Two figures:

  FIG 1 (013-pell-poincare-tiling.png): the order-4 apeirogonal tiling rendered
  in the Poincare disk model.  The Math.SE IFS (F1..F4, k = 3-2sqrt2) generates
  geodesics of H^2; they are Cayley-transformed  w = (z-i)/(z+i)  into the unit
  disk, where the parabolic chains accumulate cleanly at the boundary cusps
  w(+-(sqrt2-1)).  The Pell convergent cusps P_n/Q_n and sqrt2 are marked on
  the boundary.

  FIG 2 (013-pell-wormhole-ford.png): the catalytic-wormhole four-gate crossing
  x_n -> x_{n+k}  (n=3, k=2 -> x_3=7/5 -> x_5=41/29):
    top  — depth profile  I = ln max(|p|,|q|)  vs gate index, showing the dive
            into the abyss (z_3 at depth 4.06) and the collapse back to the
            shallow target x_5 (3.71); the two Q_k cancellations each save
            ln Q_k = ln 2 in depth;
    bottom — the same states as Ford circles (tangent point p/q, radius
            1/(2 q^2)) on a log-radius axis, so the geometric shrinking of the
            dive is visible; arrows trace the four gates.

The four-gate identity is x_{n+k} = x_k + (2 - x_k^2)/(x_n + x_k), with the deep
main variable x_n occurring ONCE (zero fanout); the two "cancellation wormholes"
are  z_3 = z_2 c_k  (c_k = (-1)^{k+1}/Q_k^2 cancels one Q_k) and
z_4 = z_3 + x_k  (the Cassini identity P_{n+k}Q_k - P_k Q_{n+k} = (-1)^{k+1} Q_n
cancels the other Q_k).

STATUS: all identities/depths are exact classical arithmetic (verified); the
"wormhole" reading of the depth profile is the HTWR Axiom I-II interpretation
(STRUCTURAL PROPOSAL), not a theorem.
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from fractions import Fraction
from math import sqrt, log, pi

SQ2 = sqrt(2.0)
K = 3.0 - 2.0 * SQ2          # (sqrt2 - 1)^2 = lambda^-2
INF = float("inf")

# ---------------------------------------------------------------------------
# Pell convergents
# ---------------------------------------------------------------------------

def pell_pair(n):
    P, Q = 1, 0
    for _ in range(n):
        P, Q = P + 2 * Q, P + Q
    return P, Q


def height(frac):
    return log(max(abs(frac.numerator), abs(frac.denominator)))


# ---------------------------------------------------------------------------
# {inf,4} IFS (Math.SE) — Mobius maps acting on ideal endpoints
# ---------------------------------------------------------------------------

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
    """4-ary Cayley tree of geodesics (apply each F_i once per node)."""
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
    """The 4 parabolic chains F_i^j(A0), j=1..length."""
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


# Cayley transform H^2 -> Poincare disk
def h2_to_disk(z):
    return (z - 1j) / (z + 1j)


def boundary_point(x):
    """Image of the boundary cusp x (real or inf) on the unit circle."""
    if x == INF:
        return 1.0 + 0.0j
    return (x - 1j) / (x + 1j)


def geodesic_disk_points(u, v, ymax=40.0, n=150):
    """Sample the H^2 geodesic with ideal endpoints (u,v), mapped to the disk."""
    if u == INF or v == INF:
        x0 = v if u == INF else u
        y = np.logspace(-3.0, log(ymax), n)
        z = x0 + 1j * y
        return h2_to_disk(z)
    a, b = min(u, v), max(u, v)
    if b - a > 1e4:
        c = (a + b) / 2.0
        y = np.logspace(-3.0, log(ymax), n)
        z = c + 1j * y
        return h2_to_disk(z)
    c = (a + b) / 2.0
    R = (b - a) / 2.0
    t = np.linspace(1e-3, pi - 1e-3, n)
    z = (c + R * np.cos(t)) + 1j * (R * np.sin(t))
    return h2_to_disk(z)


# ---------------------------------------------------------------------------
# FIG 1: Poincare-disk {inf,4} tiling
# ---------------------------------------------------------------------------

def fig_poincare():
    fig, ax = plt.subplots(figsize=(8.0, 8.0))
    th = np.linspace(0, 2 * pi, 600)
    ax.plot(np.cos(th), np.sin(th), color="0.25", lw=1.4)

    geos = gen_tree(5) | set().union(*[set(c) for c in gen_chains(24)])
    chain_colors = ["tab:orange", "tab:green", "tab:purple", "tab:cyan"]
    # draw the 4 chains in color, the tree in light gray
    for ci, chain in enumerate(gen_chains(24)):
        for (u, v) in chain:
            w = geodesic_disk_points(u, v)
            ax.plot(w.real, w.imag, color=chain_colors[ci], lw=0.7, alpha=0.8)
    tree = gen_tree(5)
    for (u, v) in tree:
        if any((u, v) in c for c in gen_chains(24)):
            continue
        w = geodesic_disk_points(u, v)
        ax.plot(w.real, w.imag, color="0.72", lw=0.5, alpha=0.55)

    # parabolic cusps +-(sqrt2-1)
    cusp = SQ2 - 1.0
    for x0, lab in [(-cusp, r"$w(1{-}\sqrt{2})$"), (cusp, r"$w(\sqrt{2}{-}1)$")]:
        w = boundary_point(x0)
        ax.plot([w.real], [w.imag], marker="o", ms=7, color="k", zorder=6)
        ax.text(w.real * 1.10, w.imag * 1.10, lab, fontsize=9, ha="center")

    # Pell convergent cusps (accumulate at sqrt2)
    for n in range(1, 9):
        P, Q = pell_pair(n)
        w = boundary_point(P / Q)
        col = "tab:red" if n % 2 == 0 else "tab:blue"
        ax.plot([w.real], [w.imag], marker="o", ms=4, color=col, zorder=6)
    wS = boundary_point(SQ2)
    ax.plot([wS.real], [wS.imag], marker="*", ms=16, color="purple", zorder=7)
    ax.text(wS.real * 1.05, wS.imag * 1.05, r"$w(\sqrt{2})$", color="purple",
            fontsize=10, ha="center")

    ax.plot([0], [0], marker="o", ms=6, color="k", zorder=6)  # base i -> 0
    ax.set_aspect("equal")
    ax.set_xlim(-1.12, 1.12)
    ax.set_ylim(-1.12, 1.12)
    ax.set_xticks([])
    ax.set_yticks([])
    for sp in ax.spines.values():
        sp.set_visible(False)
    ax.set_title(r"$\{\infty,4\}$ apeirogonal tiling (Poincaré disk) — IFS "
                 r"$k=3-2\sqrt{2}$;  parabolic cusps $w(\pm(\sqrt{2}-1))$",
                 fontsize=11)
    fig.tight_layout()
    out = "/Users/mingli/AEG/aeg-paper/notes/general/013-pell-poincare-tiling.png"
    fig.savefig(out, dpi=130)
    print("saved:", out)
    # self-check
    inside = True
    for (u, v) in list(geos)[:400]:
        w = geodesic_disk_points(u, v)
        inside &= bool(np.all(np.abs(w) <= 1.0 + 1e-6))
    print("  all sampled geodesic points inside disk:", inside)
    wc = boundary_point(cusp)
    print("  cusp w(sqrt2-1) =", complex(round(wc.real, 4), round(wc.imag, 4)),
          " angle(deg) =", round(np.angle(wc, deg=True), 2))


# ---------------------------------------------------------------------------
# FIG 2: Ford-circle four-gate wormhole
# ---------------------------------------------------------------------------

def wormhole_states(n=3, k=2):
    """Return the exact rational states of the four-gate crossing."""
    xn = Fraction(pell_pair(n)[0], pell_pair(n)[1])
    xk = Fraction(pell_pair(k)[0], pell_pair(k)[1])
    ck = 2 - xk * xk
    z1 = xn + xk
    z2 = 1 / z1
    z3 = z2 * ck
    z4 = z3 + xk
    return xn, xk, ck, z1, z2, z3, z4


def fig_wormhole():
    xn, xk, ck, z1, z2, z3, z4 = wormhole_states(3, 2)
    states = [xn, z1, z2, z3, z4]
    names = [r"$x_n=\frac{7}{5}$", r"$z_1=x_n+x_k$", r"$z_2=1/z_1$",
             r"$z_3=z_2c_k$", r"$x_{n+k}=\frac{41}{29}$"]
    gates = ["start", r"$+x_k$", r"$1/z$", r"$\times c_k$", r"$+x_k$"]
    depths = [height(s) for s in states]
    radii = [1.0 / (2.0 * s.denominator ** 2) for s in states]
    xs = [float(s) for s in states]

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(9.6, 8.6),
                                   gridspec_kw={"height_ratios": [1, 1.15]})

    # --- top: depth profile ---
    g = np.arange(5)
    ax1.plot(g, depths, "o-", color="tab:blue", lw=2, ms=7, zorder=4,
             label="catalytic wormhole (4 gates)")
    # dive shading
    ax1.fill_between([1, 4], [min(depths)] * 2, [4.06] * 2, alpha=0.12,
                     color="tab:blue")
    ax1.annotate("dive into the abyss", xy=(2.5, 4.05), ha="center",
                 fontsize=9, color="tab:blue")
    # two Q_k cancellations
    ax1.annotate(r"wormhole #1: $\div Q_k$  (saves $\ln2$)",
                 xy=(3, depths[3]), xytext=(3.15, 4.35),
                 arrowprops=dict(arrowstyle="->", color="tab:red"),
                 fontsize=8.5, color="tab:red")
    ax1.annotate(r"wormhole #2: Cassini $\div Q_k$  (saves $\ln2$)",
                 xy=(4, depths[4]), xytext=(2.15, 4.55),
                 arrowprops=dict(arrowstyle="->", color="tab:red"),
                 fontsize=8.5, color="tab:red")
    # naive continued fraction x3 -> x4 -> x5 (3 gates/step)
    naive_depths = [height(Fraction(7, 5)), height(Fraction(17, 12)),
                    height(Fraction(41, 29))]
    ax1.plot([0, 3, 6], naive_depths, "s--", color="0.55", lw=1.4, ms=5,
             label="continued fraction (6 gates, no dive)")
    ax1.plot([0, 3, 6], naive_depths, "s", color="0.55", ms=5)
    for i in range(5):
        ax1.text(g[i], depths[i] + 0.08, f"{depths[i]:.2f}", ha="center",
                 fontsize=8, color="tab:blue")
    ax1.set_xticks(list(g) + [6])
    ax1.set_xticklabels(gates + ["$x_5$"], fontsize=8)
    ax1.set_ylabel(r"information height $I=\ln\max(|p|,|q|)$")
    ax1.set_title(r"four-gate catalytic wormhole $x_3=\frac{7}{5} \to "
                  r"x_5=\frac{41}{29}$  ($k=2$, catalyst $x_2=\frac{3}{2},\ "
                  r"c_2=-\frac{1}{4}$)", fontsize=10)
    ax1.grid(True, ls=":", alpha=0.4)
    ax1.legend(fontsize=8, loc="upper left")
    ax1.set_ylim(1.4, 4.9)

    # --- bottom: Ford circles on log-radius axis ---
    colors = ["tab:blue", "tab:blue", "tab:blue", "tab:red", "tab:green"]
    for i, s in enumerate(states):
        ax2.plot([xs[i]], [log(radii[i])], marker="o", ms=14, color=colors[i],
                 zorder=4)
        ax2.annotate(f"{names[i]}\n$I$={depths[i]:.2f}, "
                     f"$r$={radii[i]:.2e}",
                     (xs[i], log(radii[i])), textcoords="offset points",
                     xytext=(8 if i != 3 else -86, 8 if i != 3 else -6),
                     fontsize=7.5, color=colors[i])
    # gate arrows
    for i in range(4):
        ax2.annotate("", xy=(xs[i + 1], log(radii[i + 1])),
                     xytext=(xs[i], log(radii[i])),
                     arrowprops=dict(arrowstyle="->", color="0.4", lw=1.2,
                                     connectionstyle="arc3,rad=0.25"))
    ax2.axhline(log(radii[0]), color="tab:blue", ls=":", lw=0.8)
    ax2.axhline(log(radii[4]), color="tab:green", ls=":", lw=0.8)
    ax2.set_xlabel("cusp coordinate $p/q$  (Ford circle tangent point)")
    ax2.set_ylabel(r"$\ln($Ford radius $)=\ln(1/2q^2)$")
    ax2.set_title("same states as Ford circles — the dive shrinks the radius "
                  r"$1/2q^2$ toward the boundary", fontsize=10)
    ax2.grid(True, ls=":", alpha=0.4)
    ax2.set_xlim(-0.7, 3.2)

    fig.tight_layout()
    out = "/Users/mingli/AEG/aeg-paper/notes/general/013-pell-wormhole-ford.png"
    fig.savefig(out, dpi=130)
    print("saved:", out)
    print("  depths:", [round(d, 4) for d in depths])
    print("  saved per wormhole = ln Q_k =", round(log(2), 4))


if __name__ == "__main__":
    fig_poincare()
    fig_wormhole()
