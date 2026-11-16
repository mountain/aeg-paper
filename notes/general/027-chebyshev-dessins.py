#!/usr/bin/env python3
"""
027 — Chebyshev Belyi maps  T_n  as threading polynomials: dessins and roots.

T_n(z) = cos(n arccos z) is a Belyi map (ramified only over -1, 1, infinity).
As an AES via branched pullback:  a = Im(T_n),  zero set = T_n^{-1}(R), the
"Chebyshev nodal set" = the dessin (a planar graph with 2-valent vertices at the
critical points).  T_n(u) is ALSO a plain polynomial in u, i.e. a candidate
threading polynomial p(u) = T_n(u).

Roots of T_n (where the threading vanishes, i.e. the degenerate u = e^{lambda}):
  u = cos((2k+1) pi/(2n)),  k = 0..n-1   — algebraic numbers (Chebyshev nodes),
  e.g. n=2: +-sqrt(2)/2;  n=3: 0, +-sqrt(3)/2;  n=4: +-cos(pi/8), +-cos(3pi/8).

This is the "polynomial roots <-> geometry" link: each root is a special u (so a
special lambda) where the thread returns to zero; the roots are algebraic over Q.

STATUS: T_n recurrence, Im(T_n)=0 nodal set, and the Chebyshev roots are exact
classical facts; rendered here.
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

CLIM = 1.5


def cheb(n, Z):
    """T_n(Z) for complex array Z."""
    if n == 0:
        return np.ones_like(Z)
    if n == 1:
        return Z
    T0 = np.ones_like(Z)
    T1 = Z
    for _ in range(2, n + 1):
        T0, T1 = T1, 2 * Z * T1 - T0
    return T1


def main():
    xs = np.linspace(-1.15, 1.15, 500)
    ys = np.linspace(-1.15, 1.15, 500)
    X, Y = np.meshgrid(xs, ys)
    Z = X + 1j * Y

    fig, axes = plt.subplots(2, 2, figsize=(11.0, 10.6))
    for ax, n in zip(axes.ravel(), [2, 3, 4, 5]):
        A = np.clip(cheb(n, Z).imag, -CLIM, CLIM)
        ax.pcolormesh(X, Y, A, cmap="RdBu_r", vmin=-CLIM, vmax=CLIM,
                      shading="auto")
        # zero set (dessin) = Im(T_n) = 0  — draw as thin white contours
        ax.contour(X, Y, cheb(n, Z).imag, levels=[0.0], colors="white",
                   linewidths=1.1)
        ax.set_aspect("equal")
        ax.set_xticks([]); ax.set_yticks([])
        for sp in ax.spines.values():
            sp.set_visible(False)
        ax.set_title(rf"$T_{n}(u)$: $a=\mathrm{{Im}}(T_{n})$ dessin",
                     fontsize=10)

    fig.suptitle(
        r"Chebyshev Belyi maps $T_n$ = threading polynomials: zero set "
        r"$T_n^{-1}(R)$ (dessin), roots $u=\cos((2k{+}1)\pi/2n)$ "
        r"algebraic", fontsize=12)
    fig.subplots_adjust(top=0.92, wspace=0.06, hspace=0.26)
    out = "/Users/mingli/AEG/aeg-paper/notes/general/027-chebyshev-dessins.png"
    fig.savefig(out, dpi=130)
    print("saved:", out)

    print("\nChebyshev T_n as threading polynomial p(u), and its roots:")
    for n in [2, 3, 4]:
        roots = [np.cos((2*k + 1) * np.pi / (2*n)) for k in range(n)]
        print(f"  T_{n}(u) roots (algebraic):",
              [round(r, 5) for r in roots])


if __name__ == "__main__":
    main()
