#!/usr/bin/env python3
"""
023 — a-distribution for mu=1, lambda=2,3,4,5, and the threading polynomial.

Assignment  a = (mu/lambda) sinh(lambda s)  (s = radial flat coordinate).
For mu = 1:  a(s) = (1/lambda) sinh(lambda s).

Left  : the radial distribution a(s) for lambda = 2,3,4,5 (mu = 1).

Right : the "threading polynomial" through the integer points s = n.
  Write U = e^{lambda};  at s = n the assignment is
        a_n = (1/lambda) sinh(lambda n) = (1/(2 lambda))(U^n - U^{-n}),
  a Laurent polynomial in U = e^lambda.  Equivalently the threading quadratic
  in u = e^{lambda s} is
        P_n(u) = u^2 - (U^n - U^{-n}) u - 1 = 0,    root u = e^{lambda n}.
  Plotted: a_n(U) = (U^n - U^{-n})/(2 ln U)  for n = 1,2,3  vs  U = e^lambda.

STATUS: all elementary identities (sinh, the Laurent rewriting) exact.
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

MU = 1.0
LAMS = [2.0, 3.0, 4.0, 5.0]


def a_of_s(s, lam):
    return (MU / lam) * np.sinh(lam * s)


def main():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12.6, 5.4))

    # ---- left: radial distribution ----
    s = np.linspace(-1.4, 1.4, 600)
    colors = ["tab:blue", "tab:orange", "tab:green", "tab:red"]
    for lam, c in zip(LAMS, colors):
        ax1.plot(s, a_of_s(s, lam), lw=2, color=c, label=rf"$\lambda={lam}$")
    ax1.axhline(0, color="0.6", lw=0.8)
    ax1.axvline(0, color="0.6", lw=0.8, ls=":")
    ax1.set_xlabel(r"$s=\log|W|$ (radial)")
    ax1.set_ylabel(r"$a=(\mu/\lambda)\sinh(\lambda s)$")
    ax1.set_title(r"radial distribution $a(s)$, $\mu=1$", fontsize=11)
    ax1.legend(fontsize=9)
    ax1.grid(True, ls=":", alpha=0.4)

    # ---- right: threading polynomial vs e^lambda ----
    U = np.linspace(np.e**1.0, np.e**5.0, 600)
    for n, c in zip([1, 2, 3], ["tab:blue", "tab:orange", "tab:green"]):
        lam = np.log(U)
        a_n = (1.0 / (2.0 * lam)) * (U**n - U**(-n))
        ax2.plot(U, a_n, lw=2, color=c, label=rf"$n={n}$: $a_n=(U^n-U^{{-n}})/2\lambda$")
    for lam in LAMS:
        Ulam = np.e**lam
        ax2.axvline(Ulam, color="0.6", lw=0.6, ls=":")
        ax2.text(Ulam, ax2.get_ylim()[1] * 0.92, rf"$\lambda={lam}$",
                 rotation=90, fontsize=8, ha="right")
    ax2.set_xscale("log")
    ax2.set_xlabel(r"$U=e^{\lambda}$")
    ax2.set_ylabel(r"thread value $a_n=(U^n-U^{-n})/(2\lambda)$")
    ax2.set_title(r"threading polynomial through integer points $s=n$ "
                  r"vs $e^{\lambda}$", fontsize=11)
    ax2.legend(fontsize=8)
    ax2.grid(True, ls=":", alpha=0.4)

    fig.suptitle(
        r"$a=(\mu/\lambda)\sinh(\lambda s)$: distribution for $\lambda=2,3,4,5$, "
        r"and the thread $a_n=(e^{\lambda n}-e^{-\lambda n})/2\lambda$ "
        r"($P_n(u)=u^2-(U^n-U^{-n})u-1$)", fontsize=12)
    fig.subplots_adjust(top=0.82, wspace=0.26)
    out = "/Users/mingli/AEG/aeg-paper/notes/general/023-a-lambda-family.png"
    fig.savefig(out, dpi=130)
    print("saved:", out)


if __name__ == "__main__":
    main()
