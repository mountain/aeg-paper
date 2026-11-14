#!/usr/bin/env python3
"""
026 — Big picture: countably many geometries (lambda = ln n), threaded by p(u).

For mu = 1 and lambda = ln2, ln3, ln4 (so u = e^{lambda} = 2,3,4):
  * the geometry is the radial distribution  a(s) = (1/lambda) sinh(lambda s)
    (the fundamental-domain data for that lambda);
  * the threading point is the FIXED flat position s = 1 (independent of lambda);
  * the threading polynomial  p(u)  (transport of a from 0 along a fixed word)
    evaluated at u = 2,3,4 gives the thread values for lambda = ln2,ln3,ln4.

Left  : a(s) for lambda = ln2, ln3, ln4, with the fixed threading point s = 1
        and its values a(1) = sinh(lambda)/lambda marked.
Right : threading polynomials p(u) for four paths (+x, +x+, +xx, +x-x) vs
        u = e^{lambda} (log axis); u = 2,3,4 marked; ROOTS (u where p = 0) at
        u = 0 and u = 1 marked — the degenerate geometries lambda = -inf, 0.

Big picture: lambda = ln n  ->  u = n (rational)  ->  countably many geometries,
threaded by p(u); the roots of p(u) are the lambda where the thread vanishes
(path returns a to 0).
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from math import log

MU = 1.0
LAMS = [log(2.0), log(3.0), log(4.0)]   # ln2, ln3, ln4


def a_of_s(s, lam):
    return (MU / lam) * np.sinh(lam * s)


def p_of_path(word):
    def f(u):
        a = 0.0
        for c in word:
            if c == '+':
                a += 1.0
            elif c == '-':
                a -= 1.0
            elif c == 'x':
                a *= u
            elif c == '/':
                a /= u
        return a
    return f


def main():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12.6, 5.6))

    # ---- left: a-distribution + fixed threading point s=1 ----
    s = np.linspace(-2.0, 2.0, 700)
    colors = ["tab:blue", "tab:orange", "tab:green"]
    for lam, c in zip(LAMS, colors):
        ax1.plot(s, a_of_s(s, lam), lw=2, color=c,
                 label=rf"$\lambda=\ln{int(np.exp(lam))}$ "
                       rf"($u={int(np.exp(lam))}$)")
        ax1.plot([1.0], [a_of_s(1.0, lam)], marker="o", ms=7, color=c, zorder=5)
    ax1.axvline(1.0, color="0.5", lw=1.0, ls="--")
    ax1.text(1.02, -0.4, r"threading point $s=1$ (fixed)", fontsize=8,
             color="0.4", rotation=90)
    ax1.axhline(0, color="0.6", lw=0.8)
    ax1.axvline(0, color="0.6", lw=0.8, ls=":")
    ax1.set_xlabel(r"$s$ (radial)")
    ax1.set_ylabel(r"$a=(\mu/\lambda)\sinh(\lambda s)$, $\mu=1$")
    ax1.set_title(r"geometries: $a(s)$ for $\lambda=\ln2,\ln3,\ln4$; "
                  r"thread at $s=1$", fontsize=10)
    ax1.legend(fontsize=9)
    ax1.grid(True, ls=":", alpha=0.4)

    # ---- right: threading polynomials p(u) + roots ----
    u = np.linspace(0.55, 5.0, 600)
    paths = ['+x', '+x+', '+xx', '+x-x']
    cols = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red']
    labs = [r'$+x:\,u$', r'$+x+:\,u{+}1$', r'$+xx:\,u^2$', r'$+x{-}x:\,u(u{-}1)$']
    roots = [0.0, -1.0, 0.0, (0.0, 1.0)]
    for w, c, lab in zip(paths, cols, labs):
        f = p_of_path(w)
        ax2.plot(u, [f(x) for x in u], lw=2, color=c, label=lab)
    for k in (2, 3, 4):
        ax2.axvline(k, color="0.6", lw=0.7, ls=":")
        ax2.text(k, 0.25, rf"$u=e^{{\lambda}}={k}$", rotation=90, fontsize=8,
                 ha="right", color="0.4")
    # roots
    ax2.plot([1.0], [0.0], marker="*", ms=16, color="purple", zorder=6)
    ax2.text(1.0, 0.6, r"root $u=1$ ($\lambda=0$)", color="purple", fontsize=8,
             ha="center")
    ax2.plot([0.0], [0.0], marker="*", ms=13, color="purple", zorder=6)
    ax2.set_xscale("log")
    ax2.set_xlim(0.55, 5.0)
    ax2.set_xlabel(r"$u=e^{\lambda}$  ($\lambda=\ln u$)")
    ax2.set_ylabel(r"threading polynomial $p(u)=P_\lambda(0)$")
    ax2.set_title(r"threading $p(u)$: values at $u=2,3,4$; roots at $u=0,1$ "
                  r"(degenerate $\lambda$)", fontsize=10)
    ax2.legend(fontsize=8, loc="upper left")
    ax2.grid(True, ls=":", alpha=0.4)

    fig.suptitle(
        r"big picture: $\lambda=\ln n\Rightarrow u=n$ (rational) gives countably "
        r"many geometries, threaded by $p(u)$; roots $\leftrightarrow$ degenerate "
        r"geometry", fontsize=12)
    fig.subplots_adjust(top=0.83, wspace=0.26)
    out = "/Users/mingli/AEG/aeg-paper/notes/general/026-big-picture-threading.png"
    fig.savefig(out, dpi=130)
    print("saved:", out)
    print("\nthread values a(s=1) = sinh(lambda)/lambda:")
    for lam in LAMS:
        print(f"  lambda=ln{int(np.exp(lam))}: a(1) =", round(a_of_s(1.0, lam), 4))


if __name__ == "__main__":
    main()
