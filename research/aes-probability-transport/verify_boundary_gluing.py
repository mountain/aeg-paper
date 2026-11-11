#!/usr/bin/env python3
"""Compare channel-marked and value-only one-sided boundary limits.

Requires the adjacent note-07 verifier, and no third-party packages.
Without data arguments, runs exact rational counterexamples.
With all three pinned exports, produces the window certificate of note 08.
"""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import argparse
import csv
import gzip
import hashlib
import io
import json
import math

import verify_memory_and_gates as gate

RELATIONS_BLOB = "8eecca0e74e4ff32466a912776047a54f5207f60"
CONCEPTS_BLOB = "207fc57a3007469f4e086242b00b4cd0f99fd857"
LOW = (F(15, 64), -F(17, 64)) + (-F(1, 64),) * 6
HIGH = (F(17, 64), -F(15, 64)) + (F(1, 64),) * 6
CENTER = (F(1, 4), -F(1, 4)) + (F(0),) * 6


def exact(x):
    """Same binary64 JSON parse as PAL, then exact rational arithmetic."""
    return F.from_float(x) if isinstance(x, float) else F(x)


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def interval(x):
    return x, x


def add(a, b):
    return a[0]+b[0], a[1]+b[1]


def neg(a):
    return -a[1], -a[0]


def mul(a, b):
    corners = [x*y for x in a for y in b]
    return min(corners), max(corners)


def isum(items):
    result = (F(0), F(0))
    for item in items:
        result = add(result, item)
    return result


def away_from_zero(a):
    return F(0) if a[0] <= 0 <= a[1] else min(abs(a[0]), abs(a[1]))


def sqrt_bounds(x, bits=96):
    require(x >= 0, "negative square")
    scale = 2**bits
    n = math.isqrt((x.numerator * scale**2)//x.denominator)
    low = F(n, scale)
    return low, low if low*low == x else F(n+1, scale)


def pin_bytes(path, expected):
    data = Path(path).read_bytes()
    actual = hashlib.sha1(b"blob "+str(len(data)).encode()+b"\0"+data).hexdigest()
    require(actual == expected, f"unrecognized source bytes: {Path(path).name}")
    return data


def read_relations(path):
    obj = json.loads(pin_bytes(path, RELATIONS_BLOB))
    require((obj["K"], obj["dim"], obj["complex_pairs"]) == (32, 8, True),
            "wrong relation atlas")
    require([c["k"] for c in obj["channels"]] == list(range(32)), "channel IDs")
    result = []
    for ch in obj["channels"]:
        q = tuple(exact(x) for x in ch["q"])
        require(len(q) == 8, "wrong pole dimension")
        mr, mi = exact(ch["m_real"]), exact(ch["m_imag"])
        # Recompute b=(1-m)q exactly from the transport primitive.
        # The separately exported, rounded b field is intentionally not used.
        b = []
        for x, y in zip(q[::2], q[1::2]):
            b.extend(((1-mr)*x+mi*y, (1-mr)*y-mi*x))
        result.append((mr, mi, tuple(b)))
    return result


def apply_relation(r, point):
    mr, mi, b = r
    out = []
    for i in range(0, 8, 2):
        x, y = point[i:i+2]
        out.extend((mr*x-mi*y+b[i], mi*x+mr*y+b[i+1]))
    return tuple(out)


def separation_on_box(r, s):
    """Exact squared minimum and maximum over the full eight-dimensional box."""
    dr, di = r[0]-s[0], r[1]-s[1]
    db = tuple(x-y for x, y in zip(r[2], s[2]))
    norm = dr*dr+di*di
    if norm == 0:
        d2 = sum(x*x for x in db)
        return d2, d2
    # (M_r-M_s) is a scaled orthogonal matrix with factor sqrt(norm).
    root = []
    for x, y in zip(db[::2], db[1::2]):
        root.extend((-(dr*x+di*y)/norm, -(dr*y-di*x)/norm))
    nearest2 = sum(max(lo-x, F(0), x-hi)**2
                   for x, lo, hi in zip(root, LOW, HIGH))
    farthest2 = sum(max(abs(lo-x), abs(hi-x))**2
                   for x, lo, hi in zip(root, LOW, HIGH))
    return norm*nearest2, norm*farthest2


def collision_root(r, s):
    dr, di = r[0]-s[0], r[1]-s[1]
    db = tuple(x-y for x, y in zip(r[2], s[2]))
    den = dr*dr+di*di
    require(den > 0, "global finite-collision argument requires distinct multipliers")
    root = []
    for x, y in zip(db[::2], db[1::2]):
        root.extend((-(dr*x+di*y)/den, -(dr*y-di*x)/den))
    return tuple(root)


def mean_difference_box(relations, weight_differences, low, high):
    ar = isum(mul(d, interval(r[0])) for r, d in zip(relations, weight_differences))
    ai = isum(mul(d, interval(r[1])) for r, d in zip(relations, weight_differences))
    bias = [isum(mul(d, interval(r[2][i]))
                 for r, d in zip(relations, weight_differences)) for i in range(8)]
    out = []
    for i in range(0, 8, 2):
        x, y = (low[i], high[i]), (low[i+1], high[i+1])
        out.extend((add(add(mul(ar, x), neg(mul(ai, y))), bias[i]),
                    add(add(mul(ai, x), mul(ar, y)), bias[i+1])))
    return out


def tv_after_observation(p, q, outputs):
    """Exact collision grouping for a finite rational toy."""
    signed = {}
    for a, b, value in zip(p, q, outputs):
        signed[value] = signed.get(value, F(0))+a-b
    return sum(abs(x) for x in signed.values())/2


def toy_checks():
    p, q = (F(3, 4), F(1, 4)), (F(1, 4), F(3, 4))
    require(gate.tv(p, q) == F(1, 2), "marked toy distance")
    require(tv_after_observation(p, q, (0, 0)) == 0, "collision cancellation")
    require(tv_after_observation(p, q, (0, 1)) == F(1, 2), "injective observation")
    pp = (F(3, 4), F(1, 8), F(1, 8))
    qq = (F(1, 4), F(3, 8), F(3, 8))
    require(gate.tv(pp, qq) == F(1, 2), "partial toy marked distance")
    require(tv_after_observation(pp, qq, (0, 0, 1)) == F(1, 4),
            "partial cancellation")
    # Reflection folds the two branches together all along y=0.
    for x in (F(-1), F(0), F(1, 3), F(1)):
        boundary_outputs = ((x, F(0)), (x, F(0)))
        require(tv_after_observation(p, q, boundary_outputs) == 0,
                "reflection boundary must glue after observation")
    # Central coincidence alone does not glue a whole interface.
    require(tv_after_observation(p, q, ((F(0), F(0)), (F(0), F(0)))) == 0,
            "central coincidence")
    require(tv_after_observation(p, q, ((F(1, 2), F(0)), (-F(1, 2), F(0))))
            == F(1, 2), "false global gluing from a single coincidence")
    # Distinct moving atoms have TV one, although their weak limits coincide.
    for n in (2, 4, 16, 256):
        require(gate.w1_1d(((F(-1, n), F(1)),), ((F(1, n), F(1)),))
                == F(2, n), "one-sided limit check")
    return {"status": "PASS", "marked_full_partial_surviving_TV":
            ["1/2", "0", "1/4", "1/2"],
            "refuted_shortcuts": [
                "forgetting channel identity always removes a gate jump",
                "one collision point glues the entire interface",
                "TV between approaching states is the TV between their weak limits"]}


def certify(relations_path, logits_path, concepts_path):
    relations = read_relations(relations_path)
    rows = gate.read_pinned_logits(logits_path)
    all_probabilities = [gate.softmax_bounds(row) for row in rows]
    p = all_probabilities[2*4]
    q = all_probabilities[3*4]
    jump = gate.tv_bounds(p, q)
    diffs = [add(a, neg(b)) for a, b in zip(p, q)]
    require(jump[0] > 0, "no channel jump")

    # Global exact cancellation obstruction. Distinct pair-collision roots
    # imply that at any value at most one pair of channels can coincide.
    roots = []
    for i, j in combinations(range(32), 2):
        root = collision_root(relations[i], relations[j])
        require(apply_relation(relations[i], root) == apply_relation(relations[j], root),
                "collision-root equation failed")
        roots.append(root)
    require(len(set(roots)) == 496, "multiple collisions share a value")
    nonzero_counts = []
    for s in range(8):
        for d in range(4):
            neighbors = [((s+1)%8, d)] + ([(s, d+1)] if d < 3 else [])
            for t, e in neighbors:
                differences = [add(a, neg(b)) for a, b in
                               zip(all_probabilities[s*4+d], all_probabilities[t*4+e])]
                nonzero_counts.append(sum(away_from_zero(x) > 0 for x in differences))
    require(len(nonzero_counts) == 56 and min(nonzero_counts) == 32,
            "global no-cancellation certificate failed")

    data = pin_bytes(concepts_path, CONCEPTS_BLOB)
    max_coord = F(0)
    with gzip.GzipFile(fileobj=io.BytesIO(data)) as stream:
        reader = csv.DictReader(io.TextIOWrapper(stream, encoding="utf-8"), delimiter="\t")
        count = 0
        for row in reader:
            max_coord = max(max_coord, *(abs(F(row[f"coord_{i}"])) for i in range(8)))
            count += 1
    require(max_coord > 3, "normalizer lower bound failed")
    radius2 = sum(max(abs(a), abs(b))**2 for a, b in zip(LOW, HIGH))
    require(radius2 < F(1, 4), "window is not inside radius 1/2")
    require(LOW[0] > 0 and HIGH[1] < 0, "wrong sector chart")
    # With any frozen R>2, all these inputs are strictly in depth bin zero.
    # Their first-pair angular boundary is the rational hyperplane a0+a1=0.

    distances = [(separation_on_box(relations[i], relations[j]), (i, j))
                 for i, j in combinations(range(32), 2)]
    collision_pairs = [pair for (lo, hi), pair in distances if lo == 0]
    require(not collision_pairs, "a branch collision meets the window")
    min_entry = min(distances, key=lambda x: x[0][0])
    min_distance = sqrt_bounds(min_entry[0][0])
    diameter = sqrt_bounds(max(bounds[1] for bounds, pair in distances))

    mean_box = mean_difference_box(relations, diffs, LOW, HIGH)
    mean_box_lower = sqrt_bounds(sum(away_from_zero(x)**2 for x in mean_box))[0]
    uniform_lower = max(mean_box_lower, min_distance[0]*jump[0])
    uniform_upper = diameter[1]*jump[1]
    require(uniform_lower > 0, "no uniform weak-distance obstruction")

    outputs = [apply_relation(r, CENTER) for r in relations]
    center_mean = mean_difference_box(relations, diffs, CENTER, CENTER)
    center_lower = sqrt_bounds(sum(away_from_zero(x)**2 for x in center_mean))[0]
    # Explicit coupling: retain min(p_j,q_j) on the diagonal, then couple
    # the surplus and deficit by their normalized product.
    plus = [(max(F(0), d[0]), max(F(0), d[1])) for d in diffs]
    minus = [(max(F(0), -d[1]), max(F(0), -d[0])) for d in diffs]
    pair_max = {pair: sqrt_bounds(bounds[1])[1] for bounds, pair in distances}
    cost_upper = F(0)
    box_cost_upper = F(0)
    for i, x in enumerate(outputs):
        for j, y in enumerate(outputs):
            if i != j:
                distance = sqrt_bounds(sum((a-b)**2 for a, b in zip(x, y)))[1]
                cost_upper += plus[i][1]*minus[j][1]*distance
                box_cost_upper += plus[i][1]*minus[j][1]*pair_max[tuple(sorted((i,j)))]
    center_upper = cost_upper/jump[0]
    uniform_upper = min(uniform_upper, box_cost_upper/jump[0])
    # This gate has exactly one surplus channel. Then the direct plan from
    # that channel to every deficit is optimal: distance to its output is a
    # matching 1-Lipschitz dual witness.
    positive = [i for i, d in enumerate(diffs) if d[0] > 0]
    negative = [i for i, d in enumerate(diffs) if d[1] < 0]
    require(len(positive) == 1 and len(negative) == 31, "single-surplus witness")
    pivot = positive[0]
    direct_center = (F(0), F(0))
    direct_window = (F(0), F(0))
    distance_dict = dict((pair, bounds) for bounds, pair in distances)
    for j in negative:
        weight = neg(diffs[j])
        squared = sum((x-y)**2 for x, y in zip(outputs[j], outputs[pivot]))
        direct_center = add(direct_center, mul(weight, sqrt_bounds(squared)))
        lo2, hi2 = distance_dict[tuple(sorted((j, pivot)))]
        direct_window = add(direct_window, mul(
            weight, (sqrt_bounds(lo2)[0], sqrt_bounds(hi2)[1])))
    center_lower = max(center_lower, direct_center[0])
    center_upper = min(center_upper, direct_center[1])
    uniform_lower = max(uniform_lower, direct_window[0])
    uniform_upper = min(uniform_upper, direct_window[1])
    require(center_lower <= center_upper <= uniform_upper, "center transport bounds")

    # Independent finite checks of the affine box-separation formula.
    for (lo, hi), (i, j) in distances:
        squared = sum((a-b)**2 for a, b in zip(outputs[i], outputs[j]))
        require(lo <= squared <= hi, "center violates uniform pair bounds")

    return {
        "source_repository": "mountain/dirac-belt",
        "source_commit": gate.SOURCE_COMMIT,
        "source_blobs": {"relations.json": RELATIONS_BLOB,
                         "gating_logits.npy": gate.SOURCE_BLOB,
                         "concepts.tsv.gz": CONCEPTS_BLOB},
        "semantics": "mathematical PAL pole transport on parsed binary64 coefficients; exact binary32-logit softmax; excludes runtime rounding",
        "transport_formula": "q_j + m_j*(a-q_j); stored rounded b is not used",
        "input_section": "alpha=0, hence a=x; continuous-input extension",
        "window": {"low": list(map(str, LOW)), "high": list(map(str, HIGH)),
                   "radius_squared_upper": str(radius2),
                   "boundary": "a[0]+a[1]=0", "center": list(map(str, CENTER))},
        "gate_cells": {"negative_side": [2, 0], "positive_side": [3, 0],
                       "valid_for_frozen_depth_normalizer": "R>2",
                       "export_max_absolute_coordinate": str(max_coord),
                       "exported_concepts": count},
        "branch_pairs_checked": len(distances),
        "global_collision_certificate": {
            "distinct_pair_collision_points": len(set(roots)),
            "adjacent_gate_pairs_checked": len(nonzero_counts),
            "minimum_certified_nonzero_weight_differences": min(nonzero_counts),
            "consequence": "none of the 56 adjacent gate jumps can cancel completely at any assignment value",
            "limitation": "exact frozen coefficients; no uniform distance lower bound claimed outside the selected window"},
        "collision_pairs_in_window": collision_pairs,
        "minimum_pair_distance_over_box_enclosure": gate.decimal_enclosure(min_distance),
        "minimum_pair": min_entry[1],
        "marked_and_value_limit_TV_enclosure": gate.decimal_enclosure(jump),
        "uniform_value_limit_W1_bounds": gate.decimal_enclosure((uniform_lower, uniform_upper)),
        "center_value_limit_W1_enclosure": gate.decimal_enclosure((center_lower, center_upper)),
        "optimal_transport_witness": {"single_surplus_channel": pivot,
                                     "deficit_channels": len(negative),
                                     "dual_function": "distance to the output of the surplus channel",
                                     "status": "matching primal and dual costs, with rational enclosures"},
        "W1_units": "Euclidean distance of the exported eight-dimensional assignment coordinates",
        "conclusion": "no gate jump is cancelled on this entire interface window; both marked and value-only gluing fail",
        "scope": "qualitative cancellation test for 56 adjacent gate pairs of one pinned atlas; quantitative W1 bounds only on the selected section/window; not training performance"}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--relations", type=Path)
    parser.add_argument("--gate-logits", type=Path)
    parser.add_argument("--concepts", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    report = {"rational_witnesses": toy_checks()}
    paths = (args.relations, args.gate_logits, args.concepts)
    if any(paths):
        if not all(paths):
            parser.error("all three pinned input paths are required")
        report["window_certificate"] = certify(*paths)
    text = json.dumps(report, ensure_ascii=False, indent=2)+"\n"
    if args.output:
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")


if __name__ == "__main__":
    main()
