#!/usr/bin/env python3
"""
040 — Arithmetic reading of the Eikonal fill: ADD lines (level lines of a) and
MULTIPLY lines (gradient lines / circles), perpendicular, with the discrete
node values (odd integers) matching the interior Eikonal solution
a = (mu/lam) sinh(lam s).

The reading (mu=1, lam=2):
  * ADD lines  = level lines of a = -x/y, i.e. the rays y = kx; every tree node
    (eps_4, a an odd integer 2m+1) lies on the add line a = 2m+1;
  * MULTIPLY lines = gradient lines of a, i.e. the circles rho = const; along
    them the Eikonal distance s grows and a = (mu/lam) sinh(lam s) (multiply).
  * the two families are ORTHOGONAL (gradient perp level set).
  * discrete <-> continuum: at a node with value a, put s = (1/lam) arcsinh((lam/mu) a);
    then (mu/lam) sinh(lam s) = a exactly.  The add step between adjacent nodes
    is +2 (= 2 mu); the multiply ratio along a circle by ds is sinh(lam(s+ds))/sinh(lam s).

STATUS: add/multiply orthogonality, node values = odd integers, and the
discrete<->continuum identity are exact (computed).  The interpretation of the
two families as "add"/"multiply" is a STRUCTURAL PROPOSAL built on these facts.
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from math import sqrt, pi, sin, cos

SQ2 = sqrt(2.0)
MU, LAM = 1.0, 2.0
EPS4 = (-1 + 1j) / SQ2


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


J = np.array([[0, -1], [1, 0]], dtype=complex)
T = np.array([[1, SQ2], [0, 1]], dtype=complex)
U = J @ T


def to_disk(z):
    return (z - 1j) / (z + 1j)


def main():
    # BFS T4 nodes
    seen = {EPS4: np.eye(2, dtype=complex)}
    front = [np.eye(2, dtype=complex)]
    for _ in range(3):
        nxt = []
        for g in front:
            for r in range(4):
                g2 = g @ mpow(U, r) @ J
                z2 = apply(g2, EPS4)
                k = complex(round(z2.real, 9), round(z2.imag, 9))
                if k not in seen:
                    seen[k] = g2
                    nxt.append(g2)
        front = nxt

    a_vals = {}
    for z in seen:
        a = -z.real / z.imag
        a_vals[z] = int(round(a))

    fig, ax = plt.subplots(figsize=(8.8, 8.8))
    th = np.linspace(0, 2*pi, 400)
    ax.plot(np.cos(th), np.sin(th), color="0.2", lw=1.1)

    # ADD lines = rays at the discrete node a-values (odd integers)
    # a = -x/y, so y = -x/a ; draw through origin at slope -1/a
    for a in sorted(set(a_vals.values())):
        if abs(a) < 1e-9:
            continue
        # ray y = -x/a, mapped to disk via z = rho*exp(i*theta)
        theta = np.arctan2(-1.0, a)   # direction (x,y) ∝ (a, -1) normalized
        # parametrize by angle from origin in H2
        rho = np.linspace(0.001, 40, 500)
        z = rho * np.exp(1j * (theta if theta >= 0 else theta + pi))
        w = to_disk(z)
        # keep only |w|<1
        m = np.abs(w) < 1.0
        ax.plot(w.real[m], w.imag[m], color="tab:blue", lw=0.7, alpha=0.5)

    # MULTIPLY lines = circles (gradient lines), perpendicular
    for R in [0.25, 0.5, 1.0, 2.0, 4.0, 8.0]:
        z = R * np.exp(1j * th)
        w = to_disk(z)
        m = np.abs(w) < 1.0
        ax.plot(w.real[m], w.imag[m], color="tab:orange", lw=0.8, alpha=0.6)

    # nodes coloured by a
    xs, ys, cs = [], [], []
    for z, a in a_vals.items():
        w = to_disk(z)
        if abs(w) < 1.0:
            xs.append(w.real); ys.append(w.imag); cs.append(a)
    xs = np.array(xs); ys = np.array(ys); cs = np.array(cs)
    sc = ax.scatter(xs, ys, c=np.clip(cs, -20, 20), cmap="coolwarm",
                    vmin=-20, vmax=20, s=26, zorder=5, edgecolors="0.2",
                    linewidths=0.3)
    # annotate a few
    for i in np.argsort(-np.abs(cs))[:6]:
        ax.text(xs[i], ys[i] + 0.03, f"{int(cs[i])}", fontsize=7, ha="center",
                color="k")

    ax.set_aspect("equal"); ax.set_xticks([]); ax.set_yticks([])
    for sp in ax.spines.values():
        sp.set_visible(False)
    ax.set_title(r"ADD lines (blue rays, $a=2m{+}1$) $\perp$ MULTIPLY lines "
                 r"(orange circles); nodes = odd integers, $a=\frac{\mu}{\lambda}"
                 r"\sinh(\lambda s)$", fontsize=10)
    cb = fig.colorbar(sc, ax=ax, fraction=0.045, pad=0.04)
    cb.set_label(r"$a$ (add-line value)")
    fig.subplots_adjust(top=0.93)
    out = "/Users/mingli/AEG/aeg-paper/notes/general/040-add-multiply-lines.png"
    fig.savefig(out, dpi=130)
    print("saved:", out)
    print("nodes:", len(a_vals), " distinct a:", sorted(set(a_vals.values())))


if __name__ == "__main__":
    main()
