#!/usr/bin/env python3
"""Level-C witness: fanout count vs interval-arithmetic wrapping.

Reproduces, with EXACT rational interval arithmetic (no floats, no rounding),
that two equal rational functions — the naive and the Heron/partial-fraction
forms of the Pell Newton-doubling map — enclose the same center value but with
strictly different interval widths, monotone in the number of times the variable
is reused (fanout count).

This is a COMPUTATIONALLY VERIFIED EXAMPLE. The reading "fanout cost =
wrapping" is a STRUCTURAL PROPOSAL; see 005-fanout-wrapping.md.

Companion of notes 001–004 (the HTWR core). Status labels follow
governance/05-mathematical-status.md.
"""

from fractions import Fraction as F


# ---- exact rational interval arithmetic over [lo, hi] ---------------------
def add(a, b):
    return (a[0] + b[0], a[1] + b[1])


def mul(a, b):
    p = [a[0] * b[0], a[0] * b[1], a[1] * b[0], a[1] * b[1]]
    return (min(p), max(p))


def div(a, b):  # assumes 0 notin b
    return mul(a, (F(1) / b[1], F(1) / b[0]))


def width(iv):
    return iv[1] - iv[0]


# ---- the two equal forms of the Pell Newton-doubling map ------------------
# Pell n=4: x_4 = 17/12, x_8 = 577/408 via x_{2n} = (x_n^2 + 2)/(2 x_n).
def trueval(x):  # exact point value k(x) = (x^2+2)/(2x)
    return (x * x + 2) / (2 * x)


def naive(iv):  # (x^2 + 2)/(2x)   — x occurs 3 times (x·x, 2x): 2 fanouts
    return div(add(mul(iv, iv), (F(2), F(2))), mul((F(2), F(2)), iv))


def heron(iv):  # (x + 2/x)/2     — x occurs 2 times (x, 2/x): 1 fanout
    return div(add(iv, div((F(2), F(2)), iv)), (F(2), F(2)))


C = F(17, 12)
X8 = F(577, 408)
C2 = C * C  # 289/144

print("Pell doubling n=4: x4 = 17/12  ->  x8 = 577/408")
print("identity at center: naive == heron == x8 ?",
      trueval(C) == X8, " (", trueval(C), " )")
print()
print("occurrence / fanout counts (the HTWR transverse-flux reading):")
print("  naive (x^2+2)/(2x): x occurs 3 times -> 2 Delta fanouts -> 3-wire section")
print("  heron (x+2/x)/2  : x occurs 2 times -> 1 Delta fanout -> 2-wire section")
print()

print("Exact widths for monotone regime (delta < sqrt2 - 17/12 ~ 0.002453):")
print(f"{'delta':>10} | {'W_true':>22} | {'W_naive':>22} | {'W_heron':>22} | {'Wn/Wh':>8}")
for k in (3, 4, 5):
    d = F(1, 10 ** k)
    lo, hi = C - d, C + d
    wt = trueval(hi) - trueval(lo)
    wn = width(naive((lo, hi)))
    wh = width(heron((lo, hi)))
    print(f"1e-{k:<4} | {wt!s:>22} | {wn!s:>22} | {wh!s:>22} | {float(wn/wh):8.4f}")

print()
print("Exact leading-order coefficients (delta -> 0), c = 17/12, c^2 = 289/144:")
print("  W_true  / delta  =  1 - 2/c^2      =", 1 - 2 / C2)
print("  W_heron / delta  =  1 + 2/c^2      =", 1 + 2 / C2)
print("  W_naive / delta  =  3 + 2/c^2      =", 3 + 2 / C2)
print("  excess_heron/d   =  4/c^2          =", 4 / C2)
print("  excess_naive/d   =  2 + 4/c^2      =", 2 + 4 / C2)
print("  excess_naive/excess_heron -> (c^2+2)/2 =", (C2 + 2) / 2)
print()
print("Conclusion: W_true < W_heron < W_naive; the interval-arithmetic excess")
print("(width - exact-image width) is monotone in the fanout count, with exact")
print("leading-order ratio 577/288 ~", float((C2 + 2) / 2), "at x = 17/12.")
