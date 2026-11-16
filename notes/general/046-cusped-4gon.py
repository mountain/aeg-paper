#!/usr/bin/env python3
"""
046 — If the 4 corners of each blue square are ALSO singularities.

The 4 corners of a blue square are the dual {4,inf} vertices = the primal {4,inf}
face centres = the CUSPS (parabolic points Q sqrt2 U {inf}).  Making them
singularities changes three things:

(1) GEOMETRY: the square becomes a CUSPED 4-GON (4 ideal/parabolic vertices); in
    the hyperbolic picture the 4 corners go to infinity (cusps), so the boundary
    data "a=0 on the edge" is Dirichlet on the 4 sides but SINGULAR at the 4
    corners (a -> infinity, poles).

(2) POTENTIAL: the potential is now defined on the BIPARTITE graph
    (nodes = square centres, plus cusps = square corners); the cusps carry
    "cusp potentials" (poles / residues), not finite values.

(3) VALUE FUNCTION: the Eikonal fill on the cusped square is a "4-cusp + centre
    source" solution, not the single-puncture E1; the constant 15/16 fill of 045
    is replaced by a cusp-dominated profile.

STATUS: the corner = cusp identification is the established {inf,4}/{4,inf}
duality (Notes 016/017); the resulting change of the value-function form is a
STRUCTURAL PROPOSAL (geometry exact, analytic form not yet solved).
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

MU, LAM = 1.0, 2.0


def main():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13.0, 6.6))

    # ---------- left: the blue square, corners = cusps ----------
    R = 4.0
    ax1.plot([-R, R, R, -R, -R], [-R, -R, R, R, -R], color="tab:blue", lw=2.2)
    for (x, y) in [(-R, -R), (R, -R), (R, R), (-R, R)]:
        ax1.scatter([x], [y], s=220, marker="o", facecolors="none",
                    edgecolors="tab:red", linewidths=2.2, zorder=5)
        ax1.annotate("cusp", (x, y), textcoords="offset points",
                     xytext=(8, 8), fontsize=8, color="tab:red")
    ax1.scatter([0], [0], marker="*", s=340, color="tab:orange", zorder=6)
    ax1.annotate("source $a(0,0)$", (0, 0), textcoords="offset points",
                 xytext=(8, -18), fontsize=8, color="tab:orange")
    ax1.set_xlim(-6, 6); ax1.set_ylim(-6, 6); ax1.set_aspect("equal")
    ax1.set_xticks([]); ax1.set_yticks([])
    ax1.set_title("blue square: edges $a=0$, corners = cusps\n"
                  "(4 parabolic vertices), centre = source", fontsize=10)

    # ---------- right: schematic cusped 4-gon in the hyperbolic disk ----------
    th = np.linspace(0, 2*np.pi, 400)
    ax2.plot(np.cos(th), np.sin(th), color="0.2", lw=1.1)
    # 4 cusps on the boundary (the corners of the dual 4-gon)
    cusp = np.radians([45, 135, 225, 315])
    for t in cusp:
        ax2.scatter([np.cos(t)], [np.sin(t)], s=120, color="tab:red", zorder=6)
    # sides: geodesic arcs between adjacent cusps (schematic: arcs bowing inward)
    for i in range(4):
        t1, t2 = cusp[i], cusp[(i+1) % 4]
        ts = np.linspace(t1, t2, 100)
        # arc bowing inward: radius shrinks to ~0.55 at the middle
        rr = 1.0 - 0.45*np.sin(np.linspace(0, np.pi, 100))
        ax2.plot(rr*np.cos(ts), rr*np.sin(ts), color="tab:blue", lw=2.0)
    ax2.scatter([0], [0], marker="*", s=320, color="tab:orange", zorder=6)
    ax2.set_xlim(-1.1, 1.1); ax2.set_ylim(-1.1, 1.1); ax2.set_aspect("equal")
    ax2.set_xticks([]); ax2.set_yticks([])
    for sp in ax2.spines.values():
        sp.set_visible(False)
    ax2.set_title(r"hyperbolic picture: cusped 4-gon, 4 cusps on $\partial\mathbb{D}$,"
                  r" sides $a=0$", fontsize=10)

    fig.suptitle(r"Making the 4 corners singular: $E_1\to$ cusped 4-gon, "
                 r"value $a$ has 4 poles + 1 source", fontsize=11)
    fig.subplots_adjust(top=0.84, wspace=0.05, left=0.04, right=0.97, bottom=0.04)
    out = "/Users/mingli/AEG/aeg-paper/notes/general/046-cusped-4gon.png"
    fig.savefig(out, dpi=140)
    print("saved:", out)


if __name__ == "__main__":
    main()
