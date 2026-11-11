#!/usr/bin/env python3
"""Exact scale-relation comparisons and a frozen PAL three-step gate audit.

All branch geometry and scale-squared values are rational. Only softmax weights
use certified rational enclosures. No floating-point geometric decisions.
"""
from collections import Counter
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import argparse
import hashlib
import json
import math

import pal_successor as ps
import verify_boundary_gluing as prior
import verify_memory_and_gates as gates

PRESERVING = ("fixed", "differential", "squared_multiplier", "potential")
RULES = PRESERVING+("reset", "relax")
CENTER = (F(1, 4), -F(1, 4))+(F(0),)*6
RADIUS_FRACTION = F(1023, 1024)
STRESS = (F(3, 5)*RADIUS_FRACTION, -F(4, 5)*RADIUS_FRACTION)+(F(0),)*6
ZERO = ps.ZERO


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def norm2(a):
    return sum(x*x for x in a)


def potential(a):
    return 1+norm2(a)


def exact_sqrt(x):
    a, b = math.isqrt(x.numerator), math.isqrt(x.denominator)
    require(a*a == x.numerator and b*b == x.denominator, "non-rational square root")
    return F(a, b)


def step(rule, op, a, scale2):
    b = prior.apply_relation(op, a)
    multiplier2 = op[0]**2+op[1]**2
    require(multiplier2 > 0 and scale2 > 0, "positive invertible state required")
    if rule == "fixed":
        next2 = scale2
    elif rule == "differential":
        next2 = scale2*multiplier2
    elif rule == "squared_multiplier":
        next2 = scale2*multiplier2**2
    elif rule == "potential":
        next2 = scale2*(potential(b)/potential(a))**2
    elif rule == "reset":
        next2 = potential(b)**2
    elif rule == "relax":
        next2 = ((exact_sqrt(scale2)+potential(b))/2)**2
    else:
        raise ValueError("unknown rule")
    return b, next2


def scale2_of_composite(rule, op, a, root):
    n = op[0]**2+op[1]**2
    return {"fixed": F(1), "differential": n, "squared_multiplier": n*n,
            "potential": (potential(a)/potential(root))**2}[rule]


def angle_sector(a):
    x, y = a[:2]
    if x == 0 and y == 0:
        return 4
    if y < 0:
        return (0 if x-y < 0 else 1) if x < 0 else (2 if x+y < 0 else 3)
    if y == 0:
        return 4 if x > 0 else 7
    if x > 0:
        return 4 if x-y > 0 else 5
    return 6 if x+y > 0 else 7


def gate_row(a, scale2):
    # Radius R=4; a/c has the same angle as a, and ||a/c||^2=||a||^2/c^2.
    return 4*angle_sector(a)+sum(norm2(a) >= d*d*scale2 for d in (1, 2, 3))


def inverse_word(word):
    return [ps.inverse(op) for op in reversed(word)]


def compose_word(word):
    op = ps.IDENTITY
    for g in word:
        op = ps.compose(g, op)
    return op


def evaluate_word(rule, word, a, scale2):
    for op in word:
        a, scale2 = step(rule, op, a, scale2)
    return a, scale2


def closure_audit(relations):
    cases = [("identity", [ps.IDENTITY])]
    cases += [("inverse", [op, ps.inverse(op)]) for op in relations]
    for s in (F(-1), F(1, 2), F(2)):
        for k in (F(1, 2), F(2), F(3)):
            a = (F(1), F(0), (s,)+(F(0),)*7)
            m = (k, F(0), ZERO)
            b = (F(1), F(0), (-k*s,)+(F(0),)*7)
            cases.append(("AM", [a, m, b, ps.inverse(m)]))
    nonzero_commutators = 0
    for j in range(0, 32, 4):
        def commutator(g, h):
            return [g, h, ps.inverse(g), ps.inverse(h)]
        u = commutator(relations[j], relations[j+1])
        v = commutator(relations[j+2], relations[j+3])
        for w in (u, v):
            op = compose_word(w)
            require(op[:2] == (F(1), F(0)) and op[2] != ZERO,
                    "expected a nonzero translation commutator")
            nonzero_commutators += 1
        cases.append(("PAL_metabelian", u+v+inverse_word(u)+inverse_word(v)))
    for _, word in cases:
        require(compose_word(word) == ps.IDENTITY, "base word is not an operator relation")
    points = (ZERO, CENTER, STRESS)
    counts = {rule: {"tested": 0, "scale_returned": 0, "by_kind": {}} for rule in RULES}
    reset_graph = 0
    for kind, word in cases:
        for a in points:
            for rule in RULES:
                b, s = evaluate_word(rule, word, a, F(1))
                require(b == a, "value failed to return")
                row = counts[rule]
                row["tested"] += 1
                row["scale_returned"] += int(s == 1)
                row["by_kind"].setdefault(kind, [0, 0])
                row["by_kind"][kind][0] += 1
                row["by_kind"][kind][1] += int(s == 1)
                if rule in PRESERVING:
                    require(s == 1, "cocycle failed an operator relation")
            b, s = evaluate_word("reset", word, a, potential(a)**2)
            require(b == a and s == potential(a)**2, "reset failed on its invariant graph")
            reset_graph += 1
    # Check the composite lift independently of a closed-word presentation.
    composite_counts = Counter()
    for j, g in enumerate(relations):
        h = relations[(j+7)%32]
        for a in points:
            for rule in RULES:
                left = evaluate_word(rule, [g, h], a, F(1))
                right = step(rule, ps.compose(h, g), a, F(1))
                composite_counts[rule] += int(left == right)
                if rule in PRESERVING:
                    require(left == right, "composite cocycle identity")
    # A simple rational counterexample which starts on c=H(a).
    translation = (F(1), F(0), (F(1),)+(F(0),)*7)
    b, s = evaluate_word("relax", [translation, ps.inverse(translation)], ZERO, F(1))
    require(b == ZERO and exact_sqrt(s) == F(5, 4), "relaxation counterexample")
    # Actual PAL operators at their own fixed poles: value returns but a
    # nontrivial multiplier character changes scale.
    pole_counts = Counter()
    pole_witness = None
    for j, op in enumerate(relations):
        r, i, b = op
        q = ps.linear_apply(*ps.inverse((1-r, -i, ZERO))[:2], b)
        require(prior.apply_relation(op, q) == q, "pole is not fixed")
        for rule in PRESERVING:
            output, s = step(rule, op, q, F(1))
            require(output == q, "pole value changed")
            pole_counts[rule] += int(s == 1)
        if pole_witness is None:
            pole_witness = {"channel": j, "pole": list(map(str, q)),
                            "differential_scale_squared": str(r*r+i*i)}
    require(pole_counts["fixed"] == pole_counts["potential"] == 32,
            "endpoint potential did not close at a pole")
    require(pole_counts["differential"] == pole_counts["squared_multiplier"] == 0,
            "expected all frozen multiplier moduli to differ from one")
    return {"operator_word_cases": len(cases), "points_per_word": len(points),
            "nonzero_translation_commutators": nonzero_commutators,
            "rules": counts, "reset_graph_closed_cases": reset_graph,
            "composite_tests_per_rule": 32*len(points),
            "composite_equalities": dict(composite_counts),
            "relaxation_counterexample": {"word": "translation +1, translation -1",
                "initial_value": "0", "initial_scale": "1", "final_scale": "5/4"},
            "actual_poles_tested": 32, "actual_pole_scale_returns": dict(pole_counts),
            "actual_pole_witness": pole_witness}


def magnitude_bounds(x):
    low, high = x
    return (F(0) if low <= 0 <= high else min(abs(low), abs(high)), max(abs(low), abs(high)))


def total_variation(p, q):
    return ps.scalar(F(1, 2), ps.interval_sum(magnitude_bounds(ps.add(a, ps.neg(b)))
                                           for a, b in zip(p, q)))


def old_window_center(relations, horizon):
    prefixes = [(ps.IDENTITY, CENTER)]
    checks = 0
    for depth in range(horizon):
        for op, a in prefixes:
            rows = [gate_row(a, scale2_of_composite(rule, op, a, CENTER)) for rule in PRESERVING]
            require(len(set(rows)) == 1, "old boundary point distinguishes scale rules")
            if depth:
                require(a[0]+a[1] != 0, "later gate on initial interface")
            checks += 1
        if depth+1 < horizon:
            prefixes = [(ps.compose(g, op), prior.apply_relation(g, a))
                        for op, a in prefixes for g in relations]
    return {"prefix_gate_agreements": checks,
            "claim": "all four rules have identical conditional rows through this horizon at the note-10 center; initial two ports handled separately"}


def stress_tree(relations, probabilities, horizon):
    # One geometry tree, four weight records. The same initial a,c and the same
    # ordered channel word always give exactly the same value coordinates.
    level = [(ps.IDENTITY, STRESS, (), ((F(1), F(1)),)*len(PRESERVING))]
    results = []
    h0 = potential(STRESS)
    require(h0 < 2, "strict potential depth barrier")
    for depth in range(1, horizon+1):
        next_level = []
        counts = [Counter() for _ in PRESERVING]
        disagreements = 0
        signature = hashlib.sha256()
        for op, a, word, weights in level:
            scales = [scale2_of_composite(rule, op, a, STRESS) for rule in PRESERVING]
            rows = [gate_row(a, s) for s in scales]
            require(rows[3]%4 == 0, "potential barrier failed")
            disagreements += int(len(set(rows)) > 1)
            for count, row in zip(counts, rows):
                count[row] += 1
            signature.update((json.dumps({"word":word,"rows":rows,
                              "scale_squared":list(map(str,scales))}, sort_keys=True)+"\n").encode())
            for j, g in enumerate(relations):
                composite = ps.compose(g, op)
                b = prior.apply_relation(g, a)
                for k, rule in enumerate(PRESERVING):
                    direct_b, direct_s = step(rule, g, a, scales[k])
                    require(direct_b == b and direct_s == scale2_of_composite(rule, composite, b, STRESS),
                            "step and shared composite scale differ")
                next_weights = tuple(ps.mul(w, probabilities[row][j]) for w, row in zip(weights, rows))
                next_level.append((composite, b, word+(j,), next_weights))
        level = next_level
        projections = sorted(a[0] for _, a, _, _ in level)
        gap = min(b-a for a, b in zip(projections, projections[1:]))
        require(gap > 0, "stress outputs not separated")
        masses = [ps.interval_sum(s[3][k] for s in level) for k in range(len(PRESERVING))]
        require(all(lo <= 1 <= hi for lo, hi in masses), "probability enclosure lost mass")
        pairs = {}
        for i, j in combinations(range(len(PRESERVING)), 2):
            p, q = [s[3][i] for s in level], [s[3][j] for s in level]
            tv = total_variation(p, q)
            means = [ps.interval_sum(ps.scalar(s[1][axis], ps.add(s[3][i], ps.neg(s[3][j])))
                                     for s in level) for axis in range(8)]
            mean2 = sum(magnitude_bounds(x)[0]**2 for x in means)
            w1lower = prior.sqrt_bounds(mean2)[0]
            pairs[PRESERVING[i]+"__"+PRESERVING[j]] = {
                "terminal_and_word_TV": gates.decimal_enclosure(tv),
                "W1_lower_bound_from_mean": gates.decimal_enclosure((w1lower, w1lower))[0]}
        results.append({"depth": depth, "paths_and_distinct_outputs": len(level),
                        "parent_gate_row_counts": {r:dict(sorted(c.items())) for r,c in zip(PRESERVING,counts)},
                        "prefixes_with_rule_disagreement": disagreements,
                        "first_coordinate_gap_lower": gates.decimal_enclosure((gap,gap),20)[0],
                        "mass_enclosures": {r:gates.decimal_enclosure(m) for r,m in zip(PRESERVING,masses)},
                        "pairwise_comparisons": pairs,
                        "prefix_gate_scale_sha256": signature.hexdigest()})
    return {"root":list(map(str,STRESS)), "initial_scale":"1", "gate_radius":"4",
            "root_norm":str(RADIUS_FRACTION),
            "potential_coordinate_norm_upper_all_times":str(h0/2),
            "levels":results,
            "scope":"designed rational radial stress input; actual frozen branch and gate parameters; not an empirical sample of concept paths"}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--relations", type=Path, required=True)
    parser.add_argument("--gate-logits", type=Path, required=True)
    parser.add_argument("--horizon", type=int, default=3)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    require(1 <= args.horizon <= 3, "finite replay budget is one to three steps")
    relations = prior.read_relations(args.relations)
    probabilities = [gates.softmax_bounds(row) for row in gates.read_pinned_logits(args.gate_logits)]
    report = {"status":"PASS", "source_commit":gates.SOURCE_COMMIT,
              "source_blobs":{"relations.json":prior.RELATIONS_BLOB,"gating_logits.npy":gates.SOURCE_BLOB},
              "arithmetic":"exact rational geometry and scale squared; mathematical softmax with rational enclosures",
              "scale_rules":list(RULES), "horizon":args.horizon,
              "closure":closure_audit(relations),
              "note10_boundary_center":old_window_center(relations,args.horizon),
              "radial_stress":stress_tree(relations,probabilities,args.horizon)}
    result = json.dumps(report,ensure_ascii=False,indent=2)+"\n"
    if args.output:
        args.output.write_text(result,encoding="utf-8")
    print(result,end="")


if __name__ == "__main__":
    main()
