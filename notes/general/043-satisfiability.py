#!/usr/bin/env python3
"""
043 — Boundary-value problem: given node values, are they realizable?

Two readings of "the value along the edge satisfies the flow equation":

(A) 2D Eikonal  |grad a|_g^2 = mu^2 + lam^2 a^2  (a global solution; no edge
    length constraint).  E_0: a = -x/y gives the odd integers -> REALIZABLE.
    Cayley: the Eikonal solution is a = (mu/lam) sinh(lam d) -> ~16, 1023, ...
    (NOT the odd integers) -> NOT realizable.

(B) 1D ODE along each edge  da/ds = +-sqrt(mu^2+lam^2 a^2)  (the edge must be a
    CHARACTERISTIC).  This forces, for every edge e = (u,v),
        l_e = |arcsinh(lam a_v / mu) - arcsinh(lam a_u / mu)| / lam ,   (CRIT)
    where l_e is the g-length of the edge.  Tree acyclic => locally necessary
    and globally sufficient.

Computation (mu=1, lam=2):
  E_0 edge eps4 -> J(eps4):   l = 1.622734,  required = 1.443635  -> slack 0.179
      (the edge is a geodesic, not a characteristic; the 2D solution a=-x/y has
       da/ds = sqrt(...) cos(angle), so the 1D ODE only has "slack", not equality)
  Cayley root edge:           l = 3 ln 2 = 2.079442, required = 0.721818 (a=0->1)
                              0.524072 (a=1->3), 1.443635 (a=1->-1) -> MISMATCH.

So: odd integers are 2D-realizable in E_0 but not on the Cayley model; under the
strict 1D ODE neither geodesic edge matches, and only the Cayley potential
a = (mu/lam) sinh(lam d) (values ~16, 1023, ...) satisfies (B).

STATUS: criterion (CRIT) and the numbers are exact/computed; the "2D vs 1D"
distinction is PROVED.
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from math import asinh, log, radians

MU, LAM = 1.0, 2.0


def beta(a):
    return asinh(LAM * a / MU)


def required(au, av):
    return abs(beta(av) - beta(au)) / LAM


def main():
    # E0 edge length (eps4 -> J(eps4), unit semicircle)
    t = np.linspace(radians(45), radians(135), 200000)
    ds = np.sqrt(np.sin(t)**2 / MU**2 + np.cos(t)**2 / LAM**2) / np.sin(t)
    l_E0 = float(np.trapezoid(ds, t))
    req_E0 = required(1.0, -1.0)

    # Cayley root edge length
    l_C = 3.0 * log(2.0)

    print(f"E0 edge l = {l_E0:.6f}, required(a:1->-1) = {req_E0:.6f}, "
          f"slack = {l_E0-req_E0:.6f}")
    for (au, av, nm) in [(0, 1, "a=0->1"), (1, 3, "a=1->3"), (1, -1, "a=1->-1")]:
        r = required(au, av)
        print(f"Cayley {nm}: l=3ln2={l_C:.6f}, required={r:.6f}, "
              f"mismatch={l_C-r:+.6f}")

    # figure: required vs actual
    labels = ["E$_0$ edge\n(a:1→−1)", "Cayley root\n(a:0→1)", "Cayley root\n(a:1→3)",
              "Cayley root\n(a:1→−1)"]
    req = [req_E0, required(0, 1), required(1, 3), required(1, -1)]
    act = [l_E0, l_C, l_C, l_C]
    x = np.arange(len(labels))
    fig, ax = plt.subplots(figsize=(9.4, 5.2))
    ax.bar(x - 0.2, req, 0.4, label="required $|\\beta(\\Delta a)|/\\lambda$",
           color="tab:green")
    ax.bar(x + 0.2, act, 0.4, label="actual $g$-length", color="tab:blue")
    for i in range(len(labels)):
        ok = abs(req[i] - act[i]) < 1e-3
        ax.text(i, max(req[i], act[i]) + 0.06, "OK" if ok else "MISMATCH",
                ha="center", fontsize=9, color="tab:green" if ok else "tab:red",
                fontweight="bold")
    ax.set_xticks(x); ax.set_xticklabels(labels, fontsize=8)
    ax.set_ylabel("edge length"); ax.legend(fontsize=8)
    ax.set_title(r"Boundary-value test: odd integers vs the 1D flow condition "
                 r"$l_e=|\beta(\Delta a)|/\lambda$ ($\mu=1,\lambda=2$)", fontsize=10)
    fig.subplots_adjust(left=0.10, right=0.97, top=0.90, bottom=0.18)
    out = "/Users/mingli/AEG/aeg-paper/notes/general/043-satisfiability.png"
    fig.savefig(out, dpi=130)
    print("saved:", out)


if __name__ == "__main__":
    main()
