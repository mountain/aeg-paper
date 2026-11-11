#!/usr/bin/env python3
"""Exact witnesses and an optional certified audit of pinned PAL gate logits.

python3 research/aes-probability-transport/verify_memory_and_gates.py
python3 research/aes-probability-transport/verify_memory_and_gates.py \
    --gate-logits /path/to/dirac-belt/pal/gating_logits.npy --output report.json

The optional audit checks bytes from one frozen export, not model accuracy.
Only the Python standard library is used, including for reading the NPY file.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import argparse
import ast
import hashlib
import json
import math
import struct

SOURCE_COMMIT = "7eb633bde849e66feeb4b22c765780abee72936a"
SOURCE_BLOB = "71e4d35e28be599d521f4c1d1ea431e3f05561e8"
DYADIC = 2 ** 96


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def mat(rows):
    return tuple(tuple(F(x) for x in row) for row in rows)


def mm(a, b):
    require(len(a[0]) == len(b), "matrix interface mismatch")
    return tuple(tuple(sum((x * b[k][j] for k, x in enumerate(row)), F(0))
                       for j in range(len(b[0]))) for row in a)


def tv(p, q):
    return sum((abs(x - y) for x, y in zip(p, q)), F(0)) / 2


def dobrushin(k):
    return max(tv(a, b) for a, b in product(k, repeat=2))


def w1_1d(atoms_p, atoms_q):
    """Exact CDF integral for finite rational measures on the line."""
    signed = {}
    for x, w in atoms_p:
        signed[x] = signed.get(x, F(0)) + w
    for x, w in atoms_q:
        signed[x] = signed.get(x, F(0)) - w
    points = sorted(signed)
    cdf = F(0)
    distance = F(0)
    for i, x in enumerate(points[:-1]):
        cdf += signed[x]
        distance += abs(cdf) * (points[i + 1] - x)
    require(sum(signed.values()) == 0, "unequal masses")
    return distance


def witnesses():
    # Two microstates in each visible block. Reset uniformly within each block.
    p = mat([[F(9, 10), 0, F(1, 10), 0],
             [F(7, 10), 0, F(3, 10), 0],
             [F(2, 10), 0, F(8, 10), 0],
             [F(4, 10), 0, F(6, 10), 0]])
    c = mat([[1, 0], [1, 0], [0, 1], [0, 1]])
    r = mat([[F(1, 2), F(1, 2), 0, 0],
             [0, 0, F(1, 2), F(1, 2)]])
    k = mm(mm(r, p), c)
    require(k == mat([[F(4, 5), F(1, 5)], [F(3, 10), F(7, 10)]]),
            "unexpected coarse kernel")
    pc = mm(p, c)
    epsilon = max(tv(row, k[i // 2]) for i, row in enumerate(pc))
    diameter = max(tv(pc[i], pc[j]) for i, j in product(range(4), repeat=2)
                   if i // 2 == j // 2)
    tau = dobrushin(k)
    require((epsilon, diameter, tau) == (F(1, 10), F(1, 5), F(1, 2)),
            "wrong defect constants")
    # Independent point priors include the worst initial microstate.
    max_errors = [F(0)] * 12
    for initial in range(4):
        u = (tuple(F(i == initial) for i in range(4)),)
        surrogate = mm(u, c)
        bound = F(0)
        for n in range(12):
            u = mm(u, p)
            surrogate = mm(surrogate, k)
            error = tv(mm(u, c)[0], surrogate[0])
            max_errors[n] = max(max_errors[n], error)
            bound = epsilon + tau * bound
            require(error <= bound, "finite-horizon bound failed")
    require(max_errors[0] == F(1, 10), "one-step sharpness changed")

    # Quantitative inverse/contraction tradeoff: K then itself, binary case.
    near_inverse_checks = 0
    for numerator in range(9):
        e = F(numerator, 16)
        channel = mat([[1-e, e], [e, 1-e]])
        kl = mm(channel, channel)
        eta = max(tv(kl[i], tuple(F(i == j) for j in range(2)))
                  for i in range(2))
        require(dobrushin(channel) >= 1-2*eta, "inverse lower bound failed")
        near_inverse_checks += 1

    # Hard gate: all shrinking intervals retain two laws, even at arbitrarily
    # small rational widths. The exact singleton chooses only the right law.
    left, right = F(1, 4), F(3, 4)  # probability of branch 1
    hard_images = []
    soft_images = []
    for n in (1, 2, 4, 16, 256, 65536):
        hard_images.append((left, right))
        soft_images.append((F(1, 2)-F(1, 4*n), F(1, 2)+F(1, 4*n)))
    require(all(x == (left, right) for x in hard_images), "hard jump lost")
    require(hard_images[-1] != (right, right), "false hard-gate Scott closure")
    require(all(a <= F(1, 2) <= b for a, b in soft_images), "soft enclosure")
    require(all(a <= c_ <= d <= b for (a, b), (c_, d)
                in zip(soft_images, soft_images[1:])), "soft nesting")

    def soft_law(x):
        t = max(F(-1), min(F(1), x))
        return ((x, F(1, 2)-t/4), (x+1, F(1, 2)+t/4))
    grid = [F(i, 8) for i in range(-8, 9)]
    for x, y in product(grid, repeat=2):
        distance = w1_1d(soft_law(x), soft_law(y))
        require(distance == F(5, 4)*abs(x-y), "soft W1 certificate failed")
    # Weak/W1 continuity must not be replaced by TV continuity of moving atoms.
    require(tv((1, 0), (0, 1)) == 1, "distinct Dirac laws have TV one")
    require(w1_1d(((F(0), F(1)),), ((F(1, 1024), F(1)),)) == F(1, 1024),
            "Dirac Wasserstein control failed")

    # Same assignment a=x*t does not fix a gate depending on x.
    representations = [(F(1), F(2)), (F(2), F(1))]
    require(all(x*t == 2 for x, t in representations), "assignment equality")
    source_gates = mat([[F(3, 4), F(1, 4)], [F(1, 4), F(3, 4)]])
    require(tv(*source_gates) == F(1, 2), "lost representation witness")
    return {
        "status": "PASS",
        "arithmetic": "exact rational",
        "approximation": {"epsilon": str(epsilon), "fiber_diameter": str(diameter),
                          "tau": str(tau), "point_prior_steps_checked": 48,
                          "max_errors_first_3": [str(x) for x in max_errors[:3]]},
        "near_inverse_checks": near_inverse_checks,
        "soft_W1_pairs_checked": len(grid)**2,
        "negative_claims_refuted": [
            "same value forces same gate",
            "hard-gate compact images preserve shrinking intersections",
            "moving Dirac masses are TV-continuous",
            "coarse-kernel error is zero without lumpability"],
    }


def down(x):
    return F((x.numerator * DYADIC) // x.denominator, DYADIC)


def up(x):
    return -down(-x)


def exp_negative_bounds(x):
    """Certified enclosure of exp(-x) for rational x>=0.

    Reduce x to t<=1. Use Taylor terms through degree 24 and a geometric upper
    bound on the positive remainder, then square and invert with outward
    dyadic rounding. No floating-point exponentiation enters the certificate.
    """
    require(x >= 0, "negative input to exp enclosure")
    if x == 0:
        return F(1), F(1)
    t, squares = x, 0
    while t > 1:
        t /= 2
        squares += 1
    term = total = F(1)
    for n in range(1, 25):
        term *= t / n
        total += term
    next_term = term * t / 25
    tail = next_term / (1-t/26)
    low, high = down(total), up(total+tail)
    for _ in range(squares):
        low, high = down(low*low), up(high*high)
    return down(1/high), up(1/low)


def read_pinned_logits(path):
    data = Path(path).read_bytes()
    blob = hashlib.sha1(b"blob "+str(len(data)).encode()+b"\0"+data).hexdigest()
    require(blob == SOURCE_BLOB, "input is not the pinned gate export")
    require(data[:8] == b"\x93NUMPY\x01\x00", "expected NPY version 1")
    size = struct.unpack("<H", data[8:10])[0]
    header = ast.literal_eval(data[10:10+size].decode("latin1").strip())
    require(header == {"descr": "<f4", "fortran_order": False, "shape": (32, 32)},
            "unexpected NPY shape or scalar format")
    raw = data[10+size:]
    require(len(raw) == 32*32*4, "wrong data length")
    floats = struct.unpack("<1024f", raw)
    require(all(math.isfinite(x) for x in floats), "nonfinite gate logit")
    # Every finite binary32 value is represented exactly by Python binary64.
    values = [F.from_float(x) for x in floats]
    return [values[i:i+32] for i in range(0, 1024, 32)]


def softmax_bounds(row):
    top = max(row)
    exps = [exp_negative_bounds(top-x) for x in row]
    low_sum = sum(a for a, b in exps)
    high_sum = sum(b for a, b in exps)
    require(low_sum > 0, "zero softmax denominator")
    return [(down(a/high_sum), up(b/low_sum)) for a, b in exps]


def tv_bounds(p, q):
    low = high = F(0)
    for (pl, ph), (ql, qh) in zip(p, q):
        dl, dh = pl-qh, ph-ql
        low += 0 if dl <= 0 <= dh else min(abs(dl), abs(dh))
        high += max(abs(dl), abs(dh))
    return down(low/2), up(high/2)


def decimal_enclosure(bounds, digits=16):
    scale = 10**digits
    def render(n):
        return f"{n//scale}.{n%scale:0{digits}d}"
    low, high = bounds
    l = (low.numerator*scale)//low.denominator
    h = -((-high.numerator*scale)//high.denominator)
    return [render(l), render(h)]


def audit_logits(path):
    rows = read_pinned_logits(path)
    probabilities = [softmax_bounds(row) for row in rows]
    pairs = {"sector": [], "depth": []}
    for s, d in product(range(8), range(4)):
        for kind, t, e in [("sector", (s+1)%8, d)] + (
                [("depth", s, d+1)] if d < 3 else []):
            interval = tv_bounds(probabilities[s*4+d], probabilities[t*4+e])
            pairs[kind].append((interval, (s, d), (t, e)))
    result = {}
    for kind, entries in pairs.items():
        winner = max(entries, key=lambda x: x[0][0])
        others = [entry for entry in entries if entry is not winner]
        unique = all(winner[0][0] > e[0][1] for e in others)
        result[kind] = {
            "pairs": len(entries),
            "positive_lower_bounds": sum(e[0][0] > 0 for e in entries),
            "maximizer_source": winner[1],
            "maximizer_target": winner[2],
            "unique_maximizer_certified": unique,
            "maximum_TV_enclosure": decimal_enclosure((
                max(e[0][0] for e in entries), max(e[0][1] for e in entries))),
        }
    require(result["sector"]["positive_lower_bounds"] == 32, "sector witness")
    require(result["depth"]["positive_lower_bounds"] == 24, "depth witness")
    return {
        "source_repository": "mountain/dirac-belt",
        "source_commit": SOURCE_COMMIT,
        "source_path": "pal/gating_logits.npy",
        "source_git_blob_sha": SOURCE_BLOB,
        "shape": [32, 32], "n_sectors": 8, "n_depths": 4, "channels": 32,
        "scope": "frozen exported channel gates; not endpoint-law or accuracy audit",
        "target": "mathematical softmax of exact binary32 logits; excludes runtime rounding",
        "certificate_method": "binary32 exact rationals; Taylor degree 24; outward dyadic 96-bit bounds",
        "sector_wrap_included": True,
        "adjacent_cell_TV": result,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--gate-logits", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    report = {"finite_witnesses": witnesses()}
    if args.gate_logits:
        report["export_audit"] = audit_logits(args.gate_logits)
    text = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")


if __name__ == "__main__":
    main()
