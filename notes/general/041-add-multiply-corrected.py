#!/usr/bin/env python3
"""
041 — CORRECTED add/multiply reading (paper-0 prop:canonical-arithmetic-frame).

Using the g-orthogonal J (not the Euclidean 90 deg), the canonical frame is
    X_u = -mu*y d_x   (ADD,  horizontal)
    X_v = -lambda*y d_y (MULTIPLY, vertical)
i.e. add lines are the HORIZONTAL lines y = const and multiply lines the VERTICAL
lines x = const; they are orthogonal (90 deg), independent of a.

The LEVEL lines of a = -x/y are the rays y = kx with k = -1/a, so the level line
makes an angle
    angle(level, add)      = arctan(1/|a|)         (90 deg at a=0, ->0 as |a|->inf)
    angle(level, multiply) = arctan(|a|)
with the add / multiply lines -- the angle DEPENDS ON a (the user's observation).

Zero set: a = -x/y = 0 <=> x = 0 -> exactly ONE zero line (the imaginary axis),
which is itself a multiply line. Its Gamma_4-orbit (the dual {4,inf}) gives the
countably many "blue" zero lines of the Cayley model.

STATUS: the frame (X_u,X_v)=(horizontal,vertical), the angle formulas, and the
zero-line count are exact (sympy-verified against paper-0).  Redo of 040.
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from math import sqrt, pi

SQ2 = sqrt(2.0)
MU, LAM = 1.0, 2.0
EPS4 = (-1 + 1j) / SQ2

J = np.array([[0, -1], [1, 0]], dtype=complex)
T = np.array([[1, SQ2], [0, 1]], dtype=complex)
U = J @ T


def mpow(M, n):
    R = np.eye(2, dtype=complex)
    for _ in range(n):
        R = R @ M
    return R


def apply(M, z):
    a, b, c, d = M[0, 0], M[0, 1], M[1, 0], M[1, 1]
    return (a * z + b) / (c * z + d)


def main():
    # T4 nodes
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

    fig, ax = plt.subplots(figsize=(10.4, 7.0))
    x0, x1, y1 = -7.0, 7.0, 9.0

    # ADD lines = horizontal y = const
    for yv in np.arange(0.5, y1, 0.5):
        ax.plot([x0, x1], [yv, yv], color="tab:blue", lw=0.5, alpha=0.45)
    # MULTIPLY lines = vertical x = const
    for xv in np.arange(-7, 7.5, 0.5):
        ax.plot([xv, xv], [0, y1], color="tab:orange", lw=0.5, alpha=0.4)
    # zero line x=0 (a=0), a multiply line
    ax.plot([0, 0], [0, y1], color="k", lw=2.2, alpha=0.9, zorder=4)
    # level lines a = ±1, ±3, ±7  -> y = -x/a
    for a in (-7, -3, -1, 1, 3, 7):
        xs = np.linspace(x0, x1, 400)
        ys = -xs / a
        m = (ys > 0) & (ys < y1)
        ax.plot(xs[m], ys[m], color="tab:green", lw=1.0, alpha=0.7, zorder=3)

    # nodes
    xs_n, ys_n, cs = [], [], []
    for z in seen:
        a = -z.real / z.imag
        if x0 < z.real < x1 and 0 < z.imag < y1:
            xs_n.append(z.real); ys_n.append(z.imag); cs.append(int(round(a)))
    sc = ax.scatter(xs_n, ys_n, c=np.clip(cs, -20, 20), cmap="coolwarm",
                    vmin=-20, vmax=20, s=28, zorder=6, edgecolors="0.2",
                    linewidths=0.4, label="nodes $a=2m+1$")
    for i, a in enumerate(cs):
        if abs(a) <= 7:
            ax.annotate(str(a), (xs_n[i], ys_n[i]), textcoords="offset points",
                        xytext=(4, 3), fontsize=7)

    # angle annotation at the a=1 level line
    ax.annotate(r"angle(level, add) $=\arctan(1/|a|)$" "\n" r"$a{=}1:45^\circ,\ a{=}3:18.4^\circ,\ a{=}7:8.1^\circ$",
                xy=(3.0, 3.0), xytext=(3.6, 7.2), fontsize=9, color="tab:green",
                arrowprops=dict(arrowstyle="->", color="tab:green"))

    ax.set_xlim(x0, x1); ax.set_ylim(0, y1)
    ax.set_xlabel(r"$x$"); ax.set_ylabel(r"$y$")
    ax.set_aspect("equal")
    ax.set_title(r"paper-0 frame: ADD $=-\mu y\,\partial_x$ (blue horizontal), "
                 r"MULTIPLY $=-\lambda y\,\partial_y$ (orange vertical); level lines "
                 r"(green rays) at angle $\arctan(1/|a|)$", fontsize=9.5)
    ax.legend(loc="upper left", fontsize=8)
    fig.subplots_adjust(top=0.93, left=0.08, right=0.97, bottom=0.08)
    out = "/Users/mingli/AEG/aeg-paper/notes/general/041-add-multiply-corrected.png"
    fig.savefig(out, dpi=130)
    print("saved:", out)


if __name__ == "__main__":
    main()
