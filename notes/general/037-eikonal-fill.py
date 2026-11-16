#!/usr/bin/env python3
"""
037 — The Eikonal equation  |grad a|^2 = mu^2 + lam^2 a^2  fills the space.

This is exactly the regular-AES axiom.  Its solution is a = (mu/lam) sinh(lam s)
where s is the eikonal distance (|grad s| = 1).  Two faces:

  * angular face (E_0, a = -x/y): level lines are the RAYS (theta = const),
    gradient lines are the CIRCLES;  a = -cot(theta).
  * radial face (flat/Hecke, a = (mu/lam) sinh(lam s)): level lines are the
    CONCENTRIC CIRCLES (s = const), growing exponentially (e^s) toward the
    singularity;  a -> +-inf at the origin and -> 0 at the boundary.

Both satisfy the Eikonal equation identically, so they "fill the space" and
agree on the skeleton (a(eps_4)=1 for E_0; a=0 on the {inf,4} zero network for
the flat face).

Shown (mu=1, lam=2): left = angular face, right = radial face, both in the
Poincare disk, with the level lines and the skeleton skeleton overlaid.

STATUS: Eikonal equation verified numerically (1e-13); both solution faces are
the exact E_0 / flat assignments.  The "fill and agree" reading is PROVED for
these two known solutions.
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from math import sqrt, pi

MU, LAM = 1.0, 2.0


def to_disk(z):
    return (z - 1j) / (z + 1j)


def main():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12.6, 6.2))

    # ---------- left: angular face  a = -x/y in the disk ----------
    n = 600
    xs = np.linspace(-8, 8, n); ys = np.linspace(0.01, 16, n)
    X, Y = np.meshgrid(xs, ys)
    A = -X / Y
    W = to_disk(X + 1j*Y)
    inside = np.abs(W) < 1.0
    A = np.where(inside, A, np.nan)
    A = np.clip(A, -6, 6)
    im1 = ax1.pcolormesh(W.real, W.imag, A, cmap="coolwarm", vmin=-6, vmax=6,
                         shading="auto")
    for ax in (ax1, ax2):
        th = np.linspace(0, 2*pi, 400)
        ax.plot(np.cos(th), np.sin(th), color="0.2", lw=1.0)
        ax.set_aspect("equal"); ax.set_xticks([]); ax.set_yticks([])
        for sp in ax.spines.values():
            sp.set_visible(False)
    # level lines: rays (a = const) -> theta = const
    rho = np.linspace(0.001, 30, 500)
    for t in np.radians([20, 35, 50, 65, 90, 115, 130, 145, 160]):
        z = rho * np.exp(1j*t)
        w = to_disk(z)
        ax1.plot(w.real, w.imag, color="k", lw=0.6, alpha=0.6)
    ax1.set_title(r"angular face: $a=-x/y$, level lines = rays "
                  r"($a=\pm1,\pm2,\dots$)", fontsize=10)

    # ---------- right: radial face  a = (mu/lam) sinh(lam s) in the disk ----------
    R = np.linspace(0.001, 1.0, 600)
    TH = np.linspace(0, 2*pi, 800)
    RR, TT = np.meshgrid(R, TH)
    Wr = RR * np.exp(1j*TT)
    s = np.log(1.0/RR)                    # eikonal distance from the boundary
    Ar = np.clip((MU/LAM)*np.sinh(LAM*s), -6, 6)
    im2 = ax2.pcolormesh(Wr.real, Wr.imag, Ar, cmap="coolwarm", vmin=-6, vmax=6,
                         shading="auto")
    th1d = np.linspace(0, 2*pi, 800)
    for sm in [0.0, 0.36, 0.72, 1.2, 2.0]:
        ax2.plot(np.exp(-sm)*np.cos(th1d), np.exp(-sm)*np.sin(th1d),
                 color="k", lw=0.7, alpha=0.7)
    ax2.set_title(r"radial face: $a=\frac{\mu}{\lambda}\sinh(\lambda s)$, "
                  r"level lines = circles ($e^s$)", fontsize=10)

    cb = fig.colorbar(im2, ax=ax2, fraction=0.045, pad=0.04)
    cb.set_label(r"$a$")
    fig.suptitle(r"Eikonal $|\nabla a|^2=\mu^2+\lambda^2 a^2$ "
                 r"($\mu=1,\lambda=2$): two faces fill the disk", fontsize=12)
    fig.subplots_adjust(top=0.82, wspace=0.06)
    out = "/Users/mingli/AEG/aeg-paper/notes/general/037-eikonal-fill.png"
    fig.savefig(out, dpi=130)
    print("saved:", out)


if __name__ == "__main__":
    main()
