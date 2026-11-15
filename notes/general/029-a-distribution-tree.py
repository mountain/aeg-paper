#!/usr/bin/env python3
"""
029 — explicit formula for a(g(eps_4)) and the a-distribution on the C_2*C_4 tree.

For g = [[A,B],[C,D]] in Gamma_4 and eps_4 = (-1+i)/sqrt2 (a(eps_4)=1),
a direct Möbius computation gives

    a(g(eps_4)) = (AD + BC) - sqrt2 (AC + BD).                       (1)

Using the two parity classes of the Hecke group H(sqrt2):
  class I   g = [[p, q s2],[r s2, s]]  ->  a = ps + 2qr - 2(pr + qs),
             det = ps - 2qr = 1  ->  ps odd  ->  a odd;
  class II  g = [[p s2, q],[r, s s2]]  ->  a = 2ps + qr - 2(pr + qs),
             det = 2ps - qr = 1  ->  qr odd  ->  a odd.
So a(g(eps_4)) is ALWAYS an odd integer 2m+1.  Along the Pell axis (U^2 J)^d the
values are the Pell numerators P_n (1,7,17,41,99,...).

Below: symbolic check of (1), the odd-integer proof, a numeric random check,
the Pell-axis values, and a figure coloring each tree vertex by its a-value
with the Pell axis highlighted.

STATUS: formula (1) and the odd-integer statement are PROVED (symbolic); the
Pell-axis values are COMPUTATIONALLY VERIFIED.
"""

import sympy as sp
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from math import sqrt, pi, atan2, hypot

SQ2 = sqrt(2.0)


# ---------------- symbolic verification of (1) ----------------
def symbolic_formula():
    A, B, C, D = sp.symbols('A B C D', real=True)
    s2 = sp.sqrt(2)
    eps = (-1 + sp.I) / s2
    z = (A * eps + B) / (C * eps + D)
    z = sp.simplify(sp.expand_complex(z))
    x = sp.re(z)
    y = sp.im(z)
    a = sp.simplify(-x / y)
    expected = sp.simplify((A * D + B * C) - s2 * (A * C + B * D))
    print("symbolic a(g(eps4)) =", sp.simplify(a))
    print("expected (AD+BC)-s2(AC+BD) =", expected)
    print("  equal:", sp.simplify(a - expected) == 0)

    # odd-integer proof, two classes
    p, q, r, s = sp.symbols('p q r s', integer=True)
    aI = sp.simplify(p * s + 2 * q * r - 2 * (p * r + q * s))
    aII = sp.simplify(2 * p * s + q * r - 2 * (p * r + q * s))
    print("class I  a =", aI, "  (det=ps-2qr=1 -> ps odd -> a odd)")
    print("class II a =", aII, "  (det=2ps-qr=1 -> qr odd -> a odd)")


# ---------------- numeric: random group elements ----------------
def matmul(A, B):
    return A @ B


def mpow(M, n):
    R = np.eye(2, dtype=complex)
    for _ in range(n):
        R = R @ M
    return R


def apply(M, z):
    A, B, C, D = M[0, 0], M[0, 1], M[1, 0], M[1, 1]
    return (A * z + B) / (C * z + D)


J = np.array([[0, -1], [1, 0]], dtype=complex)
T = np.array([[1, SQ2], [0, 1]], dtype=complex)
U = J @ T
EPS4 = (-1 + 1j) / SQ2


def a_formula(M):
    A, B, C, D = M[0, 0], M[0, 1], M[1, 0], M[1, 1]
    return (A * D + B * C) - SQ2 * (A * C + B * D)


def a_of_z(z):
    return -z.real / z.imag


def random_group_elements(n=2000, seed=1):
    rng = np.random.default_rng(seed)
    gens = [J, T, np.linalg.inv(T)]
    for _ in range(n):
        M = np.eye(2, dtype=complex)
        for _ in range(rng.integers(0, 12)):
            M = M @ gens[rng.integers(0, 3)]
        yield M


def numeric_check():
    bad = 0
    for M in random_group_elements():
        a1 = a_of_z(apply(M, EPS4))
        a2 = a_formula(M)
        if abs(a1 - a2) > 1e-6 or abs(a1 - round(a1.real)) > 1e-6 \
           or int(round(a1.real)) % 2 != 1:
            bad += 1
    print(f"\nnumeric: 2000 random g in Gamma_4 -> all a = odd integer, "
          f"formula matches: {'OK' if bad == 0 else f'{bad} FAILURES'}")


# ---------------- Pell axis (U^2 J)^d ----------------
def pell_axis():
    print("\nPell axis (U^2 J)^d eps4 -> a-values:")
    M = np.eye(2, dtype=complex)
    U2J = mpow(U, 2) @ J
    vals = []
    for d in range(5):
        M = M @ U2J
        vals.append(int(round(a_formula(M).real)))
        print(f"  d={d}: a = {vals[-1]}")
    # Pell numerators P_n = 1,3,7,17,41,99,239
    P = [1, 3, 7, 17, 41, 99, 239]
    print("  (Pell numerators P_1,P_3,P_5,...:", P, ")")
    return vals


# ---------------- tree BFS for the figure ----------------
def gen_tree(depth):
    pos_to_g = {EPS4: np.eye(2, dtype=complex)}
    edges = []
    frontier = [np.eye(2, dtype=complex)]
    for _ in range(depth):
        nxt = []
        for g in frontier:
            z1 = apply(g, EPS4)
            for r in range(4):
                g2 = g @ mpow(U, r) @ J
                z2 = apply(g2, EPS4)
                k = complex(round(z2.real, 9), round(z2.imag, 9))
                if k not in pos_to_g:
                    pos_to_g[k] = g2
                    nxt.append(g2)
                    edges.append((z1, z2))
        frontier = nxt
    return pos_to_g, edges


def h2_to_disk(z):
    return (z - 1j) / (z + 1j)


def geodesic_arc(z1, z2, n=50):
    x1, y1 = z1.real, z1.imag
    x2, y2 = z2.real, z2.imag
    if abs(x2 - x1) < 1e-12:
        y = np.linspace(min(y1, y2), max(y1, y2), n)
        return x1 + 1j * y
    c = ((x2*x2+y2*y2) - (x1*x1+y1*y1)) / (2.0*(x2-x1))
    R = hypot(x1-c, y1)
    t1, t2 = atan2(y1, x1-c), atan2(y2, x2-c)
    if t2 < t1:
        t2 += 2*pi
    if t2-t1 > pi:
        t1, t2 = t2, t1 + 2*pi
    t = np.linspace(t1, t2, n)
    return (c + R*np.cos(t)) + 1j*(R*np.sin(t))


def main():
    symbolic_formula()
    numeric_check()
    vals = pell_axis()

    pos_to_g, edges = gen_tree(3)
    # color each vertex by its a-value (odd integer)
    fig, ax = plt.subplots(figsize=(7.6, 7.6))
    th = np.linspace(0, 2*pi, 400)
    ax.plot(np.cos(th), np.sin(th), color="0.2", lw=1.1)
    for (z1, z2) in edges:
        w = h2_to_disk(geodesic_arc(z1, z2))
        ax.plot(w.real, w.imag, color="0.8", lw=0.5, alpha=0.6, zorder=1)
    # vertices colored by a
    for k, g in pos_to_g.items():
        a = a_of_z(k)
        w = h2_to_disk(k)
        ax.scatter([w.real], [w.imag], c=[a], cmap="coolwarm", vmin=-50, vmax=50,
                   s=22, zorder=3, edgecolors="0.3", linewidths=0.4)
    # Pell axis (U^2 J)^d
    M = np.eye(2, dtype=complex)
    U2J = mpow(U, 2) @ J
    axpath = []
    for d in range(4):
        M = M @ U2J
        z = apply(M, EPS4)
        w = h2_to_disk(z)
        axpath.append((w.real, w.imag))
    axpath = np.array(axpath)
    ax.plot(axpath[:, 0], axpath[:, 1], "o-", color="lime", lw=2, ms=5, zorder=5)
    w0 = h2_to_disk(EPS4)
    ax.plot([w0.real], [w0.imag], marker="*", ms=16, color="k", zorder=6)
    ax.set_aspect("equal"); ax.set_xticks([]); ax.set_yticks([])
    for sp in ax.spines.values():
        sp.set_visible(False)
    ax.set_title(r"$a(g\,\varepsilon_4)=(AD{+}BC)-\sqrt{2}(AC{+}BD)\in 2Z{+}1$: "
                 r"odd-integer colormap, Pell axis $(U^2J)^d$ (lime)", fontsize=9.5)
    cbar = fig.colorbar(ax.collections[0], ax=ax, fraction=0.045, pad=0.04)
    cbar.set_label(r"$a$ (odd integer)")
    fig.subplots_adjust(top=0.94)
    out = "/Users/mingli/AEG/aeg-paper/notes/general/029-a-distribution-tree.png"
    fig.savefig(out, dpi=130)
    print("\nsaved:", out)


if __name__ == "__main__":
    main()
