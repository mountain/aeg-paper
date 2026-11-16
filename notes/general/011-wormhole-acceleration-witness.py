#!/usr/bin/env python3
"""
011 — HTWR catalytic-wormhole acceleration witness (Pell convergents).

Companion computation for notes 001 (HTWR Core) and 002 (Exact spacetime
Pareto boundary).  It makes the "wormhole acceleration" concrete in three
layers, all in exact / closed-form arithmetic (no floats on the rational
identities):

  1. VERIFY the arithmetic engine of the wormhole:
       * the Pell norm            P_k^2 - 2 Q_k^2 = (-1)^k
       * the Mobius big-step      x_{n+k} = (x_n x_k + 2)/(x_n + x_k)
       * the Cassini cancellation P_{n+k} Q_k - P_k Q_{n+k} = (-1)^{k+1} Q_n
       * the four-gate crossing   x_n -> x_{n+k} with the two Q_k cancellations
         shown explicitly (the "cancellation wormhole" / 约分虫洞).

  2. SHOW the zero-fanout miracle: in x_{n+k} = x_k + (2 - x_k^2)/(x_n + x_k)
     the deep main variable x_n occurs ONCE (no Delta fan-out on the main
     wire), which is what lets a fixed transverse catalytic budget
     Sigma_aux <= sigma_max jump k steps at once.

  3. COMPARE the HTWR action (Axiom II cost model: gate cost = sum of input
     information heights, alpha = 1, epsilon_0 = 0) of three preparation
     strategies for x_N as N grows:
       * continued fraction (g = 0)            -> Theta(N^2)
       * catalytic-wormhole BSGS, giant step k -> Theta(N^2 / k)
       * Heron doubling (full condensation)    -> Theta(N)

STATUS (per AGENTS.md):
  * all rational identities (norm, Mobius big-step, Cassini, four-gate
    crossing) are classical standard facts and are COMPUTATIONALLY VERIFIED
    here;
  * the HTWR action numbers and the "acceleration" they exhibit are a
    STRUCTURAL PROPOSAL reading: they are the Axiom I--IV cost model applied
    to the exact states, not a theorem about wall-clock or machine cost, and
    not an independent lower bound.

Dependencies: Python standard library only (fractions, math).
"""

from fractions import Fraction
from math import log, log1p, exp, sqrt

# ---------------------------------------------------------------------------
# Exact Pell convergents
#   (1 + sqrt 2)^n = P_n + Q_n sqrt 2 ,   x_n = P_n / Q_n
# recurrence: P_{n+1} = P_n + 2 Q_n , Q_{n+1} = P_n + Q_n
# ---------------------------------------------------------------------------

def pell_pair(n):
    """Return (P_n, Q_n) as exact ints."""
    P, Q = 1, 0
    for _ in range(n):
        P, Q = P + 2 * Q, P + Q
    return P, Q


def pell(n):
    P, Q = pell_pair(n)
    return Fraction(P, Q)


# Closed forms for the *heights* (logarithmic Weil height), stable for large n:
#   P_n = (lam^n + mu^n)/2 ,  Q_n = (lam^n - mu^n)/(2 sqrt 2)
#   lam = 1+sqrt2 , mu = 1-sqrt2 ,  |mu/lam| = (sqrt2 - 1)^2
LN_LAMBDA = log(1.0 + sqrt(2.0))          # h0 = ln(1+sqrt2)
LN_R      = log((sqrt(2.0) - 1.0) ** 2)   # ln|mu/lam| < 0
LN2       = log(2.0)


def ln_P(n):
    """ln P_n (exact to double precision, any n >= 0)."""
    t = log1p(((-1.0) ** n) * exp(n * LN_R))
    return n * LN_LAMBDA + t - LN2


def ln_Q(n):
    """ln Q_n (exact to double precision, any n >= 1).

    Q_n = (lam^n - mu^n)/(2 sqrt 2) = lam^n (1 - (-1)^n |mu/lam|^n)/(2 sqrt 2).
    """
    t = log1p(-((-1.0) ** n) * exp(n * LN_R))
    return n * LN_LAMBDA + t - (LN2 + 0.5 * LN2)


# ---------------------------------------------------------------------------
# Layer 1: verify the wormhole arithmetic engine (exact rationals)
# ---------------------------------------------------------------------------

def verify_identities(nmax=6, kmax=6):
    ok = True
    # Pell norm
    for n in range(1, nmax + 1):
        P, Q = pell_pair(n)
        ok &= (P * P - 2 * Q * Q == (-1) ** n)
    # Mobius big-step  x_{n+k} = (x_n x_k + 2)/(x_n + x_k)
    for n in range(1, nmax + 1):
        for k in range(1, kmax + 1):
            xnk = pell(n + k)
            lhs = (pell(n) * pell(k) + 2) / (pell(n) + pell(k))
            ok &= (lhs == xnk)
    # Cassini cancellation  P_{n+k} Q_k - P_k Q_{n+k} = (-1)^{k+1} Q_n
    for n in range(1, nmax + 1):
        for k in range(1, kmax + 1):
            _, Qn = pell_pair(n)
            Pk, Qk = pell_pair(k)
            Pnk, Qnk = pell_pair(n + k)
            ok &= (Pnk * Qk - Pk * Qnk == (-1) ** (k + 1) * Qn)
    return ok


def four_gate_crossing(n, k):
    """The just-in-time four-gate wormhole crossing x_n -> x_{n+k}.

    Returns the four exact intermediate states and a human note about the
    two Q_k cancellations.
    """
    xn = pell(n)
    xk = pell(k)
    ck = 2 - xk * xk            # = (-1)^{k+1} / Q_k^2  (catalyst)
    z1 = xn + xk                # dive: denominator becomes Q_n Q_k
    z2 = 1 / z1
    z3 = z2 * ck                # first wormhole: one Q_k cancels
    z4 = z3 + xk                # second wormhole: Cassini kills the other Q_k
    assert z4 == pell(n + k)
    return xk, ck, z1, z2, z3, z4


# ---------------------------------------------------------------------------
# Layer 2 + 3: HTWR action (Axiom II cost model, alpha = 1, eps_0 = 0)
# ---------------------------------------------------------------------------

def action_continued_fraction(N):
    """g=0 pure geodesic flow.  Per step n->n+1: 3 gates at depth I(u_n),
    u_n = x_n + 1 = Q_{n+1}/Q_n, so I(u_n) = ln Q_{n+1}.  => Theta(N^2)."""
    return sum(3.0 * ln_Q(n + 1) for n in range(1, N))


def action_heron(N):
    """Full condensation (N = 2^K).  K Heron rounds x_{2^j} -> x_{2^{j+1}},
    7 gates each at the current depth.  => Theta(N)."""
    assert N > 0 and (N & (N - 1)) == 0, "Heron needs N a power of 2"
    K = N.bit_length() - 1
    return sum(7.0 * ln_P(2 ** j) for j in range(K))


def action_bsgs(N, k):
    """Catalytic-wormhole BSGS with giant step k.

    Resident catalyst (x_k, c_k), c_k = 2 - x_k^2, at depth s = I(x_k) = ln P_k.
    Each big-step round x_{r+jk} -> x_{r+(j+1)k} costs 4*L_j + 12*s
    (note 002, eq. after the four-gate crossing), L_j = I(x_{r+jk}) = ln P_{r+jk}.
    => Theta(N^2 / k).
    """
    s = ln_P(k)
    r = N % k
    M = N // k
    prep = 7.0 * ln_P(k)          # prepare catalyst (x_k, c_k), O(s)
    total = 0.0
    if r == 0:
        for j in range(1, M):     # start from x_k, M-1 rounds
            total += 4.0 * ln_P(j * k) + 12.0 * s
    else:
        prep += 7.0 * ln_P(r)     # prepare shallow initial state x_r
        for j in range(M):
            total += 4.0 * ln_P(r + j * k) + 12.0 * s
    return prep + total


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    print("=" * 78)
    print("HTWR catalytic-wormhole acceleration witness  (Pell convergents)")
    print("=" * 78)

    # --- Layer 1 ---
    print("\n[1] Arithmetic engine (exact rationals)")
    assert verify_identities()
    print("    Pell norm, Mobius big-step, Cassini cancellation: ALL VERIFIED\n")
    for (n, k) in [(3, 2), (4, 3), (7, 5)]:
        xk, ck, z1, z2, z3, z4 = four_gate_crossing(n, k)
        Pk, Qk = pell_pair(k)
        print(f"    n={n} -> n+k={n+k}  (k={k},  x_k={xk},  c_k=2-x_k^2={ck}"
              f" = (-1)^{k+1}/{Qk}^2)")
        print(f"        z1 = x_n + x_k = {z1}      (dive: denom Q_n*Q_k)")
        print(f"        z2 = 1/z1       = {z2}")
        print(f"        z3 = z2 * c_k   = {z3}     (wormhole #1: Q_k cancels)")
        print(f"        z4 = z3 + x_k   = {z4}  == x_{n+k}   "
              f"(wormhole #2: Cassini kills Q_k)")
        print()

    # --- Layer 2: zero-fanout miracle ---
    print("[2] The zero-fanout miracle")
    print("    x_{n+k} = x_k + (2 - x_k^2)/(x_n + x_k):  the deep main variable")
    print("    x_n occurs ONCE -> no Delta fan-out on the main wire, so a fixed")
    print("    transverse catalytic budget Sigma_aux <= sigma_max = 5 s suffices")
    print("    to jump k steps in 4 gates (instead of k sequential CF steps).\n")

    # --- Layer 3: action comparison ---
    print("[3] HTWR action vs N  (Axiom II cost model, alpha=1, eps_0=0)")
    Ns = [16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768]
    ks = [4, 16, 64]
    header = (f"{'N':>6} | {'CF (g=0)':>14} | "
              + " | ".join(f"BSGS k={k}" for k in ks)
              + f" | {'Heron':>12}")
    print(header)
    print("-" * len(header))
    rows = {k: [] for k in ks}
    cf_rows, heron_rows = [], []
    for N in Ns:
        cf = action_continued_fraction(N)
        cf_rows.append(cf)
        heron = action_heron(N)
        heron_rows.append(heron)
        row = f"{N:>6} | {cf:>14.1f} | "
        for k in ks:
            b = action_bsgs(N, k)
            rows[k].append(b)
            row += f"{b:>10.1f} "
            row += "| "
        row += f"{heron:>12.1f}"
        print(row)

    print("\n    acceleration (speedup) at N=32768:")
    cf = cf_rows[-1]
    print(f"        continued-fraction action = {cf:,.0f}  (Theta(N^2))")
    for k in ks:
        b = rows[k][-1]
        print(f"        BSGS k={k:<2}: action {b:>12,.0f}   speedup vs CF "
              f"{cf/b:6.1f}x   (theory ~3k/4 = {3*k/4:.0f}x)")
    h = heron_rows[-1]
    print(f"        Heron       : action {h:>12,.0f}   speedup vs CF "
          f"{cf/h:6.1f}x   (Theta(N), unbounded)")

    print("\n    (status: identities = computationally-verified classical facts;")
    print("     action/acceleration = STRUCTURAL PROPOSAL reading of Axioms I-IV)")

    # --- Layer 4: log-log plot ---
    try:
        import os
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt

        fig, ax = plt.subplots(figsize=(7.0, 5.2))
        ax.plot(Ns, cf_rows, "o-", label="continued fraction  (g=0, $\\Theta(N^2)$)")
        for k, color in zip(ks, ["C1", "C2", "C3"]):
            ax.plot(Ns, rows[k], "s--", color=color,
                    label=f"catalytic wormhole BSGS  (k={k}, $\\Theta(N^2/k)$)")
        ax.plot(Ns, heron_rows, "^-", label="Heron doubling  ($\\Theta(N)$)")
        ax.set_xscale("log", base=2)
        ax.set_yscale("log", base=10)
        ax.set_xlabel("N  (Pell convergent index, $x_N = P_N/Q_N$)")
        ax.set_ylabel("HTWR action $\\mathcal{A}$  (Axiom II cost, $\\alpha{=}1$)")
        ax.set_title("HTWR catalytic-wormhole acceleration")
        ax.grid(True, which="both", ls=":", alpha=0.5)
        ax.legend(fontsize=8, loc="upper left")
        fig.tight_layout()
        out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           "011-wormhole-acceleration.png")
        fig.savefig(out, dpi=130)
        print(f"\n    plot saved: {out}")
    except Exception as exc:  # pragma: no cover - plotting is optional
        print(f"\n    (plot skipped: {exc})")


if __name__ == "__main__":
    main()
