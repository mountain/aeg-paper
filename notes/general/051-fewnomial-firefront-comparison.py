#!/usr/bin/env python3
"""
051 — fewnomial–fire-front comparison: the cusp birth, chord sum vs chord difference.

Side-by-side illustration of the mechanism shared by
  (a) the finite-layer exponential polynomial  P_eps(V) = V^2 + eps V + 1  on the
      unit circle V = e^{it}  (notes/algebra/01..., §3): its self-intersection is a
      chord-SUM condition  V + W = -eps, born at |eps| = 2 (V = W, coincident);
  (b) the fire-front on the flat torus  C_t(theta) = (t cos theta, t sin theta) mod 1:
      its crossings are a chord-DIFFERENCE condition  t(u - v) = w (w in Z^2), born at
      t = |w|/2 (u = -v, antipodal).

The two conditions are complementary by the parallelogram law
    |u - v|^2 + |u + v|^2 = 4,
i.e. the birth is "a chord of the parametrising circle reaches the diameter", read
once through the difference (fire-front, antipodal) and once through the sum
(fewnomial, coincident).

Top row:  P_eps(e^{it}) = e^{it}(2 cos t + eps)  for eps = 2.5 (smooth), 2.0 (cusp),
          1.2 (node).
Bottom row: the folded distance circle C_t on T^2 for t = 0.4 (embedded), 0.5
          (self-tangency), 0.6 (transverse crossings).
"""

from math import pi, cos, sin
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path

OUT = Path(__file__).resolve().parent


def fewnomial(eps, n=2000):
    t = np.linspace(0.0, 2 * pi, n)
    z = np.exp(1j * t) * (2.0 * np.cos(t) + eps)
    return z


def torus_curve(t, n=3000):
    th = np.linspace(0.0, 2 * pi, n, endpoint=False)
    return np.stack([t * np.cos(th), t * np.sin(th)], axis=1)


def torus_crossings(t):
    """Crossings of C_t on the unit square torus (lattice vectors |v| < 2t)."""
    R2 = (2.0 * t) ** 2
    M = int(2.0 * t) + 1
    pts = []
    for m in range(-M, M + 1):
        for n in range(-M, M + 1):
            if m == 0 and n == 0:
                continue
            if m * m + n * n >= R2:
                continue
            if not (m > 0 or (m == 0 and n > 0)):
                continue
            L = (m * m + n * n) ** 0.5
            d = (t * t - L * L / 4.0) ** 0.5
            perp = (-n / L, m / L)
            for sgn in (+1.0, -1.0):
                mid = (sgn * d * perp[0], sgn * d * perp[1])
                x = (mid[0] - m / 2.0, mid[1] - n / 2.0)
                pts.append((x[0] % 1.0, x[1] % 1.0))
    return pts


def main():
    fig, axes = plt.subplots(2, 3, figsize=(12.0, 7.6))

    # ---- top row: fewnomial (chord sum) ----
    for ax, eps in zip(axes[0], (2.5, 2.0, 1.2)):
        z = fewnomial(eps)
        ax.plot(z.real, z.imag, lw=1.1, color="#1f77b4")
        ax.plot([0], [0], "k+", ms=8)
        if eps < 2.0:
            ax.plot([0], [0], "o", color="#d62728", ms=5)  # the node at origin
            ax.set_title(f"$\\varepsilon={eps}$: node", fontsize=10)
        elif abs(eps - 2.0) < 1e-9:
            ax.plot([0], [0], "o", color="#d62728", ms=5)
            ax.set_title(f"$\\varepsilon={eps}$: cusp (born)", fontsize=10)
        else:
            ax.set_title(f"$\\varepsilon={eps}$: smooth", fontsize=10)
        ax.set_aspect("equal")

    # ---- bottom row: fire-front on the torus (chord difference) ----
    for ax, t in zip(axes[1], (0.4, 0.5, 0.6)):
        pts = torus_curve(t)
        for ox in (-1, 0, 1):
            for oy in (-1, 0, 1):
                ax.plot(pts[:, 0] + ox, pts[:, 1] + oy, color="#1f77b4", lw=0.9)
        ax.axvline(0.5, color="0.6", lw=0.5, ls="--")
        ax.axhline(0.5, color="0.6", lw=0.5, ls="--")
        for (cx, cy) in torus_crossings(t):
            ax.plot([cx], [cy], "o", color="#d62728", ms=4)
        if t < 0.5:
            ax.set_title(f"$t={t}$: embedded", fontsize=10)
        elif abs(t - 0.5) < 1e-9:
            ax.set_title(f"$t={t}$: self-tangency (born)", fontsize=10)
        else:
            ax.set_title(f"$t={t}$: $N(t)={len(torus_crossings(t))}$ crossings", fontsize=10)
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.set_aspect("equal")
        ax.set_xticks([0, 0.5, 1])
        ax.set_yticks([0, 0.5, 1])

    axes[0, 0].set_ylabel("fewnomial\nchord sum\n$V+W=-\\varepsilon$", fontsize=9)
    axes[1, 0].set_ylabel("fire-front\nchord difference\n$t(u-v)=v$", fontsize=9)
    fig.suptitle(
        "the cusp birth: chord reaches the diameter  (fewnomial $|\\varepsilon|=2$, "
        "fire-front $t=|v|/2$)\n$|u-v|^2+|u+v|^2=4$",
        fontsize=11,
    )
    fig.tight_layout(rect=[0, 0, 1, 0.92])
    fname = OUT / "051-fewnomial-firefront-comparison.png"
    fig.savefig(fname, dpi=125)
    print("wrote", fname.name)


if __name__ == "__main__":
    main()
