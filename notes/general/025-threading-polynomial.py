#!/usr/bin/env python3
"""
025 — Threading polynomial p(u) for paths (group words) + the {inf,4} grid.

Part (2), aligned definition: a path P is a word in the four operations
  + : a -> a + mu,   - : a -> a - mu,   x : a -> a*u,   / : a -> a/u,
with u = e^{lambda}.  Transporting a from 0 along P gives P_lambda(0) = p(u),
a (Laurent) polynomial in u.  For mu = 1 and lambda = ln2, ln3, ln4 we evaluate
p(2), p(3), p(4)  (i.e. u = e^{ln2}=2, e^{ln3}=3, e^{ln4}=4).

Right panel: p(u) for five paths vs u = e^{lambda}, with u = 2,3,4 marked.
Left panel : the {inf,4} apeirogonal grid (disk) with the origin O = eps_2 and
             the zero line Z (the reference edge), i.e. the canvas on which the
             four operations transport a.

STATUS: the transport a -> a+mu / a*u and p(u) are elementary exact; the left
grid is the Hecke {inf,4} tiling (orbit of eps_2--eps_4) as before.
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from math import sqrt, log, pi, atan2, hypot

SQ2 = sqrt(2.0)
INF = float("inf")


# ---- transport / threading polynomial ----
def p_of_path(word):
    """Return p(u) as a numpy-callable via Horner over +,-,x,/ (a symbolic-free
    approach: build a lambda of u)."""
    def f(u):
        a = 0.0
        for c in word:
            if c == '+':
                a = a + 1.0
            elif c == '-':
                a = a - 1.0
            elif c == 'x':
                a = a * u
            elif c == '/':
                a = a / u
        return a
    return f


# ---- {inf,4} grid (primal) ----
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


def arc_disk(a, b, n=60):
    px, py = a.real, a.imag
    qx, qy = b.real, b.imag
    if abs(qx - px) < 1e-12:
        y = np.linspace(min(py, qy), max(py, qy), n)
        return h2_to_disk(px + 1j * y)
    c = ((qx*qx+qy*qy) - (px*px+py*py)) / (2.0*(qx-px))
    R = hypot(px-c, py)
    thp, thq = atan2(py, px-c), atan2(qy, qx-c)
    if thq < thp:
        thq += 2*pi
    if thq-thp > pi:
        thp, thq = thq, thp + 2*pi
    t = np.linspace(thp, thq, n)
    return h2_to_disk((c + R*np.cos(t)) + 1j*(R*np.sin(t)))


def panel_grid(ax, edges):
    th = np.linspace(0, 2*pi, 400)
    ax.plot(np.cos(th), np.sin(th), color="0.2", lw=1.1)
    for (a, b) in edges:
        w = arc_disk(a, b)
        ax.plot(w.real, w.imag, color="tab:red", lw=0.8, alpha=0.85, zorder=3)
    w2 = h2_to_disk(EPS2)
    w4 = h2_to_disk(EPS4)
    ax.plot([w2.real], [w2.imag], marker="o", ms=7, color="k", zorder=6)
    ax.plot([w4.real], [w4.imag], marker="*", ms=14, color="k", zorder=6)
    ax.text(w2.real, w2.imag-0.09, r"$O=\varepsilon_2$", ha="center", fontsize=9)
    ax.text(w4.real, w4.imag+0.09, r"$Z$-vertex", ha="center", fontsize=8)
    ax.set_aspect("equal"); ax.set_xticks([]); ax.set_yticks([])
    for sp in ax.spines.values():
        sp.set_visible(False)
    ax.set_title(r"$\{\infty,4\}$ grid: origin $O$, zero line $Z$ (red) — "
                 r"canvas for the four ops", fontsize=10)


def panel_thread(ax):
    u = np.linspace(1.0, 5.0, 500)
    paths = ['+x', '+x+', '+xx', '++x', '+x+x']
    colors = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple']
    labels = [r'$+x:\,u$', r'$+x+:\,u{+}1$', r'$+xx:\,u^2$',
              r'$++x:\,2u$', r'$+x{+}x:\,u(u{+}1)$']
    for w, c, lab in zip(paths, colors, labels):
        f = p_of_path(w)
        ax.plot(u, [f(x) for x in u], lw=2, color=c, label=lab)
    for k in (2, 3, 4):
        ax.axvline(k, color="0.6", lw=0.7, ls=":")
        ax.text(k, 0.3, rf"$u=e^{{\lambda}}={k}$", rotation=90,
                fontsize=8, ha="right", color="0.4")
    ax.set_xlabel(r"$u=e^{\lambda}$")
    ax.set_ylabel(r"threading polynomial $p(u)=P_\lambda(0)$")
    ax.set_title(r"$\mu=1$: $p(u)$ vs $e^{\lambda}$ ($\lambda=\ln2,\ln3,\ln4$ "
                 r"$\leftrightarrow u=2,3,4$)", fontsize=10)
    ax.legend(fontsize=7.5, loc="upper left")
    ax.grid(True, ls=":", alpha=0.4)
    ax.set_xlim(1, 5)


def main():
    edges = primal(6)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12.4, 5.9))
    panel_grid(ax1, edges)
    panel_thread(ax2)
    fig.suptitle(
        r"four-operation transport on the $\{\infty,4\}$ grid: path word "
        r"$\Rightarrow$ threading polynomial $p(e^{\lambda})$, "
        r"$\lambda=\ln2,\ln3,\ln4$", fontsize=12)
    fig.subplots_adjust(top=0.83, wspace=0.20)
    out = "/Users/mingli/AEG/aeg-paper/notes/general/025-threading-polynomial.png"
    fig.savefig(out, dpi=130)
    print("saved:", out)


if __name__ == "__main__":
    main()
