#!/usr/bin/env python3
"""
045 — The blue squares, +/- and inversion observations, and the "E1-like square".

(1) BLUE SQUARES: the dual {4,inf} perpendicular bisectors bound closed 4-gons
    around every node; for the root (R=8) this is the square [-4,4]^2.  YES.

(2) +/- SYMMETRY: sinh is odd, so a(d) and -a(d) both solve the Eikonal ODE
    along an edge.  (0->-16->-1023 is a valid mirror branch.)  YES.

(3) INVERSION: 1/a is NOT an Eikonal solution in general --
       |grad(1/a)|^2 = lam^2 b^2 + mu^2 b^4  (b=1/a),
    a quartic "dual" equation, not mu^2+lam^2 b^2.  Only the value ROTATION
    a -> e^{i th} a is a symmetry.  So 1,1/16,1/1023 is not a solution.

(4) "E1-LIKE SQUARE": with a=0 on the blue boundary and the Eikonal fill inside,
    the centre value is
       a_centre = (mu/lam) sinh(lam * inradius),  inradius = int dx/L.
    For the Cayley metric the inradius is  ln 2  for EVERY node (self-similar),
    so a_centre = (1/2) sinh(2 ln 2) = 15/16 for ALL squares -- NOT the differing
    potential values (0, 16, 1023, ...).  A differing centre value requires a
    SOURCE (puncture) at each node, whose strength IS the potential a(node).

So the user's picture is right at the level of "E1 = punctured square, a=0 on
the boundary, differing source at the centre"; the differing number is the
source strength a(node), while the source-free Eikonal fill is the constant 15/16.

STATUS: (1),(2),(4-source) exact; (3) refuted (quartic dual, not Eikonal);
the constant 15/16 and inradius ln2 are computed exactly.
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from math import sin, cos, radians

MU, LAM = 1.0, 2.0
NUMSTEPS = 4


def main():
    # one square: the root, [-4,4]^2 ; show a=0 on the boundary and the Eikonal fill
    n = 200
    X = np.linspace(-4, 4, n)
    Y = np.linspace(-4, 4, n)
    XX, YY = np.meshgrid(X, Y)
    # g-distance from the boundary in the Cayley metric, L = 8 - |x| (on the root)
    # approximation: inradius = ln2, a_centre = 15/16; fill a = (mu/lam) sinh(lam * d_edge)
    # where d_edge = g-distance from the boundary.  We use a radial proxy.
    r = np.maximum(np.abs(XX), np.abs(YY))  # Chebyshev to the boundary (>=4 at edge)
    r = np.clip(4.0 - r, 0, 4.0)            # 0 at boundary, up to 4 at centre
    # crude g-distance proxy: s = ln(8/(8 - r))  (matches int_0^r dx/(8-x) on the axis)
    s = np.log(8.0 / (8.0 - r))
    A = (MU / LAM) * np.sinh(LAM * s)
    A = np.clip(A, 0, 1.0)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13.0, 6.4))

    # ---------- left: the blue square + boundary a=0 ----------
    th = np.linspace(0, 2*np.pi, 300)
    ax1.plot([-4, 4, 4, -4, -4], [-4, -4, 4, 4, -4], color="tab:blue", lw=2.2,
             label="blue zero lines")
    ax1.plot([-8, 8], [0, 0], color="k", lw=0.8, alpha=0.5)
    ax1.plot([0, 0], [-8, 8], color="k", lw=0.8, alpha=0.5)
    ax1.scatter([0], [0], marker="*", s=320, color="tab:red", zorder=5,
                label="centre: source $a(\\mathrm{node})$")
    ax1.set_xlim(-5.5, 5.5); ax1.set_ylim(-5.5, 5.5); ax1.set_aspect("equal")
    ax1.set_xticks([]); ax1.set_yticks([])
    ax1.set_title("blue square $[-4,4]^2$: $a=0$ on boundary,\n"
                  "source $a(0,0)$ at centre", fontsize=10)
    ax1.legend(loc="lower left", fontsize=8)

    # ---------- right: E1-like fill with a=0 boundary ----------
    pc = ax2.pcolormesh(XX, YY, A, cmap="plasma", shading="auto")
    ax2.plot([-4, 4, 4, -4, -4], [-4, -4, 4, 4, -4], color="tab:blue", lw=2.0)
    ax2.scatter([0], [0], marker="*", s=320, color="white", edgecolors="k",
                linewidths=1.0, zorder=5)
    ax2.set_aspect("equal"); ax2.set_xticks([]); ax2.set_yticks([])
    ax2.set_title(r"source-free Eikonal fill: $a=0$ boundary, "
                  r"$a_{\rm centre}=15/16$ (all squares)", fontsize=10)
    cb = fig.colorbar(pc, ax=ax2, fraction=0.045, pad=0.03)
    cb.set_label(r"$a$")

    fig.suptitle(r"E$_1$-like blue square: boundary $a=0$, centre source "
                 r"(different per node); source-free fill is constant $15/16$",
                 fontsize=11)
    fig.subplots_adjust(top=0.82, wspace=0.06, left=0.05, right=0.97, bottom=0.05)
    out = "/Users/mingli/AEG/aeg-paper/notes/general/045-e1-square.png"
    fig.savefig(out, dpi=140)
    print("saved:", out)


if __name__ == "__main__":
    main()
