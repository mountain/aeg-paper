#!/usr/bin/env python3
"""
024 — Non-trivial AES from Belyi maps  beta(z) = z^n.

Branched-pullback construction (paper-3 thm:branched-pullback-zero-germ):
  Phi = z^n (holomorphic, degree n),  a = Im(Phi),  g = |d Phi|^2/(mu^2+lam^2 a^2).
The zero set is  a = 0  <=>  Im(z^n) = 0  <=>  sin(n theta) = 0, i.e. the n lines
through the origin (2n prongs), with an essential singular point at 0 (local
degree m=n, cone angle 2 pi n).

n=2  =>  2 lines (4 prongs), cone 4 pi  = the LOCAL model of the Hecke {inf,4}
        four-valent vertex (eps_4).
n=3,4,5  => 3,4,5 lines = finite analogues.

mu, lambda are FREE parameters (any integers, mu != 0), so this is a non-trivial
SINGULAR AES with multiple zero lines on integer mu, lambda — the family the
user conjectured, in its simplest (z^n) form.

STATUS: Im(z^n) = r^n sin(n theta) is exact; the zero-set/cone-angle claims are
paper-3 thm:branched-pullback-zero-germ (PROVED), rendered here.
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

CLIM = 1.5


def im_z_n(n, X, Y):
    """Im((x+iy)^n) via de Moivre: r^n sin(n theta)."""
    r = np.hypot(X, Y)
    theta = np.arctan2(Y, X)
    return r**n * np.sin(n * theta)


def main():
    xs = np.linspace(-1.15, 1.15, 500)
    ys = np.linspace(-1.15, 1.15, 500)
    X, Y = np.meshgrid(xs, ys)

    fig, axes = plt.subplots(2, 2, figsize=(11.0, 10.6))
    for ax, n in zip(axes.ravel(), [2, 3, 4, 5]):
        A = np.clip(im_z_n(n, X, Y), -CLIM, CLIM)
        ax.pcolormesh(X, Y, A, cmap="RdBu_r", vmin=-CLIM, vmax=CLIM,
                      shading="auto")
        # zero set: the n lines theta = k*pi/n
        for k in range(n):
            t = np.linspace(-1.2, 1.2, 300)
            ang = k * np.pi / n
            ax.plot(t * np.cos(ang), t * np.sin(ang), color="white", lw=1.3,
                    alpha=0.9)
        ax.plot([0], [0], marker="o", ms=7, color="k", zorder=6)
        ax.set_aspect("equal")
        ax.set_xticks([]); ax.set_yticks([])
        for sp in ax.spines.values():
            sp.set_visible(False)
        label = r"$2n$ prongs, cone $2\pi n$"
        if n == 2:
            label += r"  ($=$ Hecke $\varepsilon_4$ local model)"
        ax.set_title(rf"$\beta=z^{n}$: $a=\mathrm{{Im}}(z^{n})$  —  {label}",
                     fontsize=9.5)

    fig.suptitle(
        r"Non-trivial AES via Belyi maps $\beta=z^n$: zero set = $n$ lines "
        r"($2n$ prongs), integer $\mu,\lambda$ free — the $n{=}2$ case is the "
        r"$\{\infty,4\}$ four-valent vertex germ", fontsize=12)
    fig.subplots_adjust(top=0.92, wspace=0.06, hspace=0.28)
    out = "/Users/mingli/AEG/aeg-paper/notes/general/024-belyi-z-n-zero-sets.png"
    fig.savefig(out, dpi=130)
    print("saved:", out)


if __name__ == "__main__":
    main()
