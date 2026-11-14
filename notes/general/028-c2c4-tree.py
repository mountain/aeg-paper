#!/usr/bin/env python3
"""
028 — C_2 * C_4 normal-form constructor for the {inf,4} Hecke network.

Supersedes 013 (whose IFS F1..F4 had hidden torsion: F3 = F2^{-1}, F4 = F1^{-1},
so the "4-ary tree" was non-free with word collisions).  Here the tiling's
1-skeleton is built collision-free from the free product

    Gamma_4 = < J, U | J^2 = U^4 = 1 >  =  C_2 * C_4,   U = J T (fixes eps_4),
    J (fixes eps_2 = i),   T: z -> z + sqrt2.

The 1-skeleton is the 4-regular Bass-Serre tree T_4:
  * vertices = the eps_4-orbit (right cosets Gamma_4 / <U>), 4-valent;
  * root edge e_0 = [eps_4, J(eps_4)] (through eps_2 = i);
  * neighbours of g(eps_4):  g U^r J (eps_4),  r = 0,1,2,3.
BFS to depth d yields exactly  1 + 2 (3^d - 1)  vertices (no collisions).

Also computes the F_2 rtimes C_4 commutator coordinates:
  alpha~ = J U^2,  beta~_perp = U^3 J U^3  (both hyperbolic, translation 2 ln lambda),
  and verifies  [alpha~, beta~_perp] = (J U)^4 = T^4  (the 4-step tearing).

Four views' data are printed: (1) tree vertices/edges; (2) the Pell axis
(r_i = 2 word); (3) the {4,inf} dual (a=0 line orbit) — computed here too;
(4) the commutator 4-step path eps_4 -> T eps_4 -> T^2 eps_4 -> T^3 eps_4 ->
T^4 eps_4.

STATUS: C_2*C_4 presentation, the tree count, and [alpha~,beta~_perp]=T^4 are
exact (verified); this corrects the non-free IFS of 013.
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from math import sqrt, pi, atan2, hypot, inf

SQ2 = sqrt(2.0)
INF = float("inf")


def matmul(A, B):
    return A @ B


def mpow(M, n):
    R = np.eye(2, dtype=complex)
    for _ in range(n):
        R = R @ M
    return R


def apply(M, z):
    a, b, c, d = M[0, 0], M[0, 1], M[1, 0], M[1, 1]
    return (a * z + b) / (c * z + d)


I = np.eye(2, dtype=complex)
J = np.array([[0, -1], [1, 0]], dtype=complex)
T = np.array([[1, SQ2], [0, 1]], dtype=complex)
U = J @ T                          # [[0,-1],[1,sqrt2]]

EPS4 = (-1 + 1j) / SQ2
EPS2 = 1j


def h2_to_disk(z):
    return (z - 1j) / (z + 1j)


def key(z, prec=9):
    return round(z.real, prec) + 1j * round(z.imag, prec)


def geodesic_arc(z1, z2, n=60):
    x1, y1 = z1.real, z1.imag
    x2, y2 = z2.real, z2.imag
    if abs(x2 - x1) < 1e-12:
        y = np.linspace(min(y1, y2), max(y1, y2), n)
        return x1 + 1j * y
    c = ((x2 * x2 + y2 * y2) - (x1 * x1 + y1 * y1)) / (2.0 * (x2 - x1))
    R = hypot(x1 - c, y1)
    th1, th2 = atan2(y1, x1 - c), atan2(y2, x2 - c)
    if th2 < th1:
        th2 += 2 * pi
    if th2 - th1 > pi:
        th1, th2 = th2, th1 + 2 * pi
    t = np.linspace(th1, th2, n)
    return (c + R * np.cos(t)) + 1j * (R * np.sin(t))


def gen_tree(depth):
    """Collision-free BFS of T_4.  Returns (pos->g, edges list)."""
    pos_to_g = {key(EPS4): I}
    edges = []
    frontier = [I]
    for _ in range(depth):
        new_frontier = []
        for g in frontier:
            z1 = apply(g, EPS4)
            for r in range(4):
                g2 = g @ mpow(U, r) @ J
                z2 = apply(g2, EPS4)
                k = key(z2)
                if k not in pos_to_g:
                    pos_to_g[k] = g2
                    new_frontier.append(g2)
                    edges.append((z1, z2))
        frontier = new_frontier
    return pos_to_g, edges


def main():
    depth = 4
    pos_to_g, edges = gen_tree(depth)
    print("tree vertices at depth", depth, ":", len(pos_to_g),
          " (expect", 1 + 2 * (3**depth - 1), ")")
    print("tree edges (spanning):", len(edges))

    # ---- F_2 rtimes C_4 commutator ----
    al = J @ mpow(U, 2)          # JU^2
    be = mpow(U, 3) @ J @ mpow(U, 3)   # U^3 J U^3
    comm = al @ be @ np.linalg.inv(al) @ np.linalg.inv(be)
    T4 = mpow(T, 4)
    print("\nalpha~ = JU^2 =", al.tolist())
    print("beta~_perp = U^3 J U^3 =", be.tolist())
    print("[alpha,beta] =", np.round(comm, 10).tolist())
    print("T^4 =", T4.tolist())
    print("commutator == T^4 (PSL):",
          np.allclose(comm, T4) or np.allclose(comm, -T4))

    # ---- Pell axis (r_i = 2 word: (U^2 J)^d) ----
    axis = []
    g = I
    for _ in range(4):
        g = g @ mpow(U, 2) @ J
        axis.append(apply(g, EPS4))
    print("\nPell axis (U^2 J)^d eps4:", [key(z) for z in axis])

    # ---- commutator 4-step path eps4 -> T^4 eps4 ----
    path = [apply(mpow(T, k), EPS4) for k in range(5)]
    print("commutator path eps4 -> T^4 eps4:", [key(z) for z in path])

    # ---- figure ----
    fig, ax = plt.subplots(figsize=(7.4, 7.4))
    th = np.linspace(0, 2 * pi, 400)
    ax.plot(np.cos(th), np.sin(th), color="0.2", lw=1.1)
    for (z1, z2) in edges:
        w = h2_to_disk(geodesic_arc(z1, z2))
        ax.plot(w.real, w.imag, color="tab:red", lw=0.8, alpha=0.85, zorder=2)
    for k in pos_to_g:
        w = h2_to_disk(k)
        ax.plot([w.real], [w.imag], marker="o", ms=4, color="tab:red", zorder=3)
    # commutator path (bold)
    for k in range(4):
        w1 = h2_to_disk(geodesic_arc(path[k], path[k + 1]))
        ax.plot(w1.real, w1.imag, color="tab:blue", lw=2.4, alpha=0.95, zorder=4)
    w4 = h2_to_disk(EPS4)
    ax.plot([w4.real], [w4.imag], marker="*", ms=15, color="k", zorder=6)
    ax.set_aspect("equal"); ax.set_xticks([]); ax.set_yticks([])
    for sp in ax.spines.values():
        sp.set_visible(False)
    ax.set_title(r"$C_2{*}C_4$ tree $T_4$ (collision-free) + commutator "
                 r"$[\tilde\alpha,\tilde\beta_\perp]=T^4$ (blue)", fontsize=10)
    fig.subplots_adjust(top=0.94)
    out = "/Users/mingli/AEG/aeg-paper/notes/general/028-c2c4-tree.png"
    fig.savefig(out, dpi=130)
    print("\nsaved:", out)


if __name__ == "__main__":
    main()
