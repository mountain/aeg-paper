#!/usr/bin/env python3
"""Dependency-free exact checks for finite calibrations in AEG Paper IV."""
from __future__ import annotations

from collections import Counter
from fractions import Fraction
from itertools import product
from math import comb, factorial


def matmul(A, B, mod=None):
    C = (
        A[0] * B[0] + A[1] * B[2],
        A[0] * B[1] + A[1] * B[3],
        A[2] * B[0] + A[3] * B[2],
        A[2] * B[1] + A[3] * B[3],
    )
    return tuple(x % mod for x in C) if mod else C


def det(A, q=None):
    x = A[0] * A[3] - A[1] * A[2]
    return x % q if q else x


def inv2(A, q):
    di = pow(det(A, q), -1, q)
    return canon((A[3] * di, -A[1] * di, -A[2] * di, A[0] * di), q)


def canon(A, q):
    A = tuple(x % q for x in A)
    first = next(x for x in A if x)
    s = pow(first, -1, q)
    return tuple((s * x) % q for x in A)


def pgl2(q):
    return {
        canon(A, q)
        for A in product(range(q), repeat=4)
        if det(A, q) != 0
    }


def mul(A, B, q):
    return canon(matmul(A, B, q), q)


def right_cosets(G, H, q):
    unseen = set(G)
    cosets = []
    while unseen:
        g = next(iter(unseen))
        C = frozenset(mul(g, h, q) for h in H)
        cosets.append(C)
        unseen -= C
    return cosets


def verify_projector():
    for a, b in [(Fraction(2), Fraction(3)), (Fraction(-4), Fraction(2)), (Fraction(1, 2), Fraction(2, 3))]:
        den = 1 + a * b
        P = (a * b / den, -a / den, -b / den, Fraction(1, 1) / den)
        assert matmul(P, P) == P
        assert P[0] + P[3] == 1
        assert det(P) == 0


def verify_finite_projective():
    for q in (3, 5, 7):
        G = pgl2(q)
        assert len(G) == q * (q * q - 1)
        H = {canon((a, 0, 0, 1), q) for a in range(1, q)}
        cosets = right_cosets(G, H, q)
        assert len(H) == q - 1
        assert len(cosets) == q * (q + 1)
        assert all(len(C) == q - 1 for C in cosets)
        index = {g: i for i, C in enumerate(cosets) for g in C}
        normalizer = {
            k
            for k in G
            if {mul(mul(inv2(k, q), h, q), k, q) for h in H} == H
        }
        descended = set()
        for k in G:
            ok = True
            for C in cosets:
                images = {index[mul(g, k, q)] for g in C}
                if len(images) != 1:
                    ok = False
                    break
            if ok:
                descended.add(k)
        assert descended == normalizer
        assert len(normalizer) == 2 * (q - 1)


def horner(word, k, x=0):
    a = x
    for d in word:
        a = k * a + d
    return a


def verify_horner():
    for k, n in [(2, 8), (3, 6)]:
        vals = {w: horner(w, k) for w in product(range(k), repeat=n)}
        assert len(set(vals.values())) == k**n
        histograms = {}
        for w, v in vals.items():
            h = tuple(Counter(w)[r] for r in range(k))
            histograms.setdefault(h, []).append(v)
        for h, vs in histograms.items():
            count = factorial(n)
            for m in h:
                count //= factorial(m)
            assert len(vs) == count == len(set(vs))
    assert sorted(horner(w, 2) for w in product((0, 1), repeat=4) if sum(w) == 2) == [3, 5, 6, 9, 10, 12]
    assert comb(8, 4) == 70


def eq_value(bits, n):
    return int(bits[:n] == bits[n:])


def residual_truth_table(order, prefix, n):
    rem = order[len(prefix):]
    out = []
    for tail in product((0, 1), repeat=len(rem)):
        assignment = {}
        for var, val in zip(order[:len(prefix)], prefix):
            assignment[var] = val
        for var, val in zip(rem, tail):
            assignment[var] = val
        x = tuple(assignment[("x", i)] for i in range(n))
        y = tuple(assignment[("y", i)] for i in range(n))
        out.append(int(x == y))
    return tuple(out)


def max_residual_width(order, n):
    widths = []
    for t in range(len(order) + 1):
        residuals = {
            residual_truth_table(order, prefix, n)
            for prefix in product((0, 1), repeat=t)
        }
        widths.append(len(residuals))
    return widths


def verify_obdd():
    for n in range(1, 6):
        block = [("x", i) for i in range(n)] + [("y", i) for i in range(n)]
        inter = [z for i in range(n) for z in (("x", i), ("y", i))]
        bw = max_residual_width(block, n)
        iw = max_residual_width(inter, n)
        assert bw[n] == 2**n
        assert max(iw) <= 3


def verify_butterfly_and_ntt():
    q = 257
    assert pow(3, 128, q) == q - 1
    assert pow(3, 256, q) == 1
    for N, expected in [(8, 64), (16, 249)]:
        z = pow(3, 256 // N, q)
        assert z == expected
        assert pow(z, N, q) == 1
        assert pow(z, N // 2, q) == q - 1
    for w in (1, 2, 64, 249):
        B1 = (1, 1, 1, -1)
        D = (1, 0, 0, w)
        Bw = (1, w, 1, -w)
        assert tuple(x % q for x in matmul(B1, D, q)) == tuple(x % q for x in Bw)


def verify_resource_calibrations():
    d0, d1, d2, d3 = 100, 10, 1, 2
    WL = d0 * d1 * d2 + d0 * d2 * d3
    WR = d1 * d2 * d3 + d0 * d1 * d3
    assert (WL, d0 * d2) == (1200, 100)
    assert (WR, d1 * d3) == (2020, 20)
    for N, total in [(8, 44), (16, 152)]:
        assert 2 * N + N * (N - 1) // 2 == total


def verify_fiber_inequality():
    for n in range(1, 9):
        fibers = Counter(sum(w) for w in product((0, 1), repeat=n))
        assert max(fibers.values()) >= 2**n / len(fibers)


def main():
    checks = [
        verify_projector,
        verify_finite_projective,
        verify_horner,
        verify_obdd,
        verify_butterfly_and_ntt,
        verify_resource_calibrations,
        verify_fiber_inequality,
    ]
    for check in checks:
        check()
        print(f"PASS {check.__name__}")
    print(f"PASS all {len(checks)} verification groups")


if __name__ == "__main__":
    main()
