#!/usr/bin/env python3
"""Replay the frozen successor contract and certify complete depth-three trees.

Standard-library certificate. Optional --pal-algebra exercises the pinned NumPy
transport as a numerical cross-check; that check is not interval certification.
"""
from collections import Counter
from fractions import Fraction as F
from pathlib import Path
from types import SimpleNamespace
import argparse
import csv
import gzip
import hashlib
import importlib.util
import io
import json
import math

import pal_successor as ps
import verify_boundary_gluing as prior
import verify_memory_and_gates as gate

ALGEBRA_BLOB = "ba01b61e1be836418c157ca14c482b2c4774b84c"
CONTRACT_PATH = Path(__file__).with_name("pal-successor-contract-v1.json")
CENTER = (F(1, 4), -F(1, 4))+(F(0),)*6
DIRECTION = (F(1),)+(F(0),)*7


def require(x, message):
    if not x:
        raise AssertionError(message)


def magnitude_bounds(x):
    lo, hi = x
    return (F(0) if lo <= 0 <= hi else min(abs(lo), abs(hi)), max(abs(lo), abs(hi)))


def tv_intervals(p, q):
    terms = [magnitude_bounds(ps.add(a, ps.neg(b))) for a, b in zip(p, q)]
    return ps.scalar(F(1, 2), ps.interval_sum(terms))


def pick_concept(path):
    raw = prior.pin_bytes(path, prior.CONCEPTS_BLOB)
    best = None
    with gzip.GzipFile(fileobj=io.BytesIO(raw)) as gz:
        rows = csv.DictReader(io.TextIOWrapper(gz, encoding="utf-8"), delimiter="\t")
        count = 0
        for index, row in enumerate(rows):
            # PAL loads these printed six-decimal entries into binary64.
            x = tuple(F.from_float(float(row[f"coord_{j}"])) for j in range(8))
            alpha = F.from_float(float(row["alpha"]))
            norm2 = sum(a*a for a in x)
            if best is None or (norm2, index) < (best[0], best[1]):
                best = norm2, index, x, alpha
            count += 1
    norm2, index, x, alpha = best
    return ps.Seed(x, ps.exp_bounds(alpha), f"export-row-{index}-exp-alpha"), {
        "selection": "minimum exported coordinate squared norm; ties by row index",
        "zero_based_row": index, "exported_rows": count,
        "coordinates": list(map(str, x)), "parsed_alpha": str(alpha),
        "observation_scale_enclosure": gate.decimal_enclosure(ps.exp_bounds(alpha)),
        "coordinate_norm_squared": str(norm2)}


def absmax(x):
    return max(abs(x[0]), abs(x[1]))


def norm2_upper(xs):
    return sum(absmax(x)**2 for x in xs)


def fingerprint(states):
    digest = hashlib.sha256()
    for s in states:
        row = {"word": s.word, "gates": s.gate_rows,
               "linear": [str(s.affine[0]), str(s.affine[1])],
               "translation": list(map(str, s.affine[2]))}
        digest.update((json.dumps(row, sort_keys=True, separators=(",", ":"))+"\n").encode())
    return digest.hexdigest()


def refine_epsilon(current, margin, slope):
    require(margin > 0, "strict window margin required")
    if slope:
        return min(current, margin/(2*slope))
    return current


def inspect_level(model, states, paired=False):
    values = [s.value_bounds() for s in states]
    projections = sorted((v[0][0], v[0][1], n) for n, v in enumerate(values))
    gaps = [b[0]-a[1] for a, b in zip(projections, projections[1:])]
    require(min(gaps) > 0, "terminal outputs not separated by their first coordinate")
    weights = [model.probability_bounds(s) for s in states]
    mass = ps.interval_sum(weights)
    require(mass[0] <= 1 <= mass[1], "dynamic law lost probability mass")
    source_row = states[0].gate_rows[0]
    frozen = [model.probability_bounds(s, frozen_row=source_row) for s in states]
    dynamic_frozen = tv_intervals(weights, frozen)
    result = {
        "paths": len(states), "terminal_outputs_certified_distinct": len(states),
        "first_coordinate_gap_lower": gate.decimal_enclosure((min(gaps), min(gaps)), 20)[0],
        "total_mass_enclosure": gate.decimal_enclosure(mass),
        "dynamic_vs_cached_start_gate_TV": gate.decimal_enclosure(dynamic_frozen),
        "ordered_path_state_sha256": fingerprint(states)}
    if paired:
        left = [model.probability_bounds(s, first_row=8) for s in states]
        difference = [ps.add(a, ps.neg(b)) for a, b in zip(left, weights)]
        mean = [ps.interval_sum(ps.mul(d, v[j]) for d, v in zip(difference, values))
                for j in range(8)]
        mean_lower2 = sum(magnitude_bounds(x)[0]**2 for x in mean)
        w1_lower = prior.sqrt_bounds(mean_lower2)[0]
        require(w1_lower > 0, "terminal mean did not witness a weak-limit jump")
        pair_tv = tv_intervals(left, weights)
        first_tv = gate.tv_bounds(model.probabilities[8], model.probabilities[12])
        require(max(pair_tv[0], first_tv[0]) <= min(pair_tv[1], first_tv[1]),
                "path TV inconsistent with first-step certificate")
        frozen_left = [model.probability_bounds(s, frozen_row=8) for s in states]
        result.update({
            "two_port_terminal_TV_enclosure": gate.decimal_enclosure(pair_tv),
            "two_port_joint_trace_TV_enclosure": gate.decimal_enclosure(first_tv),
            "terminal_W1_lower_bound_from_mean": gate.decimal_enclosure((w1_lower, w1_lower))[0],
            "left_dynamic_vs_cached_start_gate_TV": gate.decimal_enclosure(tv_intervals(left, frozen_left))})
    return result, projections, gaps


def audit_tree(model, seed, horizon, paired=False):
    level = [ps.State(seed)]
    levels = []
    epsilon = F(1, 64)
    injection_epsilon = F(1, 64)
    largest_coordinate_norm2 = F(0)
    smallest_noninitial_gate_margin = None
    face_checks = 0
    source_normal = (F(1), F(1))+(F(0),)*6
    for depth in range(1, horizon+1):
        counts = Counter()
        for state in level:
            normal, constant = state.transported_face(source_normal, F(0))
            r, i, b = state.affine
            require(ps.linear_apply(r, -i, normal) == source_normal,
                    "transported face has the wrong linear pullback")
            require(constant+sum(a*t for a, t in zip(normal, b)) == 0,
                    "transported face has the wrong translation pullback")
            face_checks += 1
            row = model.row(state)
            counts[row] += 1
            coordinates = state.coordinate_bounds()
            largest_coordinate_norm2 = max(largest_coordinate_norm2, norm2_upper(coordinates))
            require(norm2_upper(coordinates) < F(1, 4), "R>2 independence failed")
            if paired and depth > 1:
                # All subsequent gates are strict at the shared boundary point.
                plain_seed = ps.Seed(seed.coordinates, seed.scale, seed.scale_name)
                plain = ps.State(plain_seed, state.affine, state.word, state.gate_rows)
                require(model.row(plain) == row, "later gate depends on an unresolved port")
                a = tuple(t[0] for t in coordinates)
                require(all(lo == hi for lo, hi in coordinates), "unit-scale expected")
                require(a[0] > 0 and a[1] < 0 and a[0]+a[1] != 0,
                        "unexpected quadrant or later boundary")
                r, i, _ = state.affine
                for margin, slope in [(a[0], abs(r)+abs(i)), (-a[1], abs(r)+abs(i)),
                                      (abs(a[0]+a[1]), abs(r+i)+abs(r-i))]:
                    epsilon = refine_epsilon(epsilon, margin, slope)
                margin = abs(a[0]+a[1])
                smallest_noninitial_gate_margin = margin if smallest_noninitial_gate_margin is None else min(smallest_noninitial_gate_margin, margin)
        level = [child for parent in level for child, probability in model.children(parent)]
        result, projection_order, gaps = inspect_level(model, level, paired)
        if paired:
            for left, right, gap in zip(projection_order, projection_order[1:], gaps):
                l, r = level[left[2]], level[right[2]]
                slope = abs(r.affine[0]-l.affine[0])+abs(r.affine[1]-l.affine[1])
                injection_epsilon = refine_epsilon(injection_epsilon, gap, slope)
        result["depth"] = depth
        result["parent_gate_row_counts"] = dict(sorted(counts.items()))
        levels.append(result)
    # Check a finite set of controlled reverse paths, retaining the same scale.
    reverse_states = level[:32]+level[-32:]
    for state in reverse_states:
        for _ in range(horizon):
            state = model.rewind(state)
        require(state == ps.State(seed), "controlled marked reverse failed")
    report = {"levels": levels, "controlled_inverse_roundtrips": len(reverse_states),
              "exact_transported_face_checks": face_checks,
              "all_gate_inputs_have_norm_below_half": True,
              "maximum_gate_coordinate_norm_squared_upper": str(largest_coordinate_norm2)}
    if paired:
        def dyadic_below(bound):
            n, x = 6, F(1, 64)
            while x > bound:
                n, x = n+1, x/2
            return n, x
        n, eps = dyadic_below(epsilon)
        m, inject_eps = dyadic_below(min(epsilon, injection_epsilon))
        # Rebuild only prefixes where a gate is evaluated and certify the full
        # eight-dimensional box, including the depth-bin margin.
        prefixes = [ps.State(seed)]
        for depth in range(horizon):
            for state in prefixes:
                vals = state.coordinate_bounds()
                r, i, _ = state.affine
                width = (abs(r)+abs(i))*eps
                box = [(lo-width, hi+width) for lo, hi in vals]
                require(norm2_upper(box) < F(1, 4), "subwindow depth certificate")
                require(box[0][0] > 0 and box[1][1] < 0, "subwindow quadrant")
                if depth:
                    centre_h = vals[0][0]+vals[1][0]
                    require(abs(centre_h) > (abs(r+i)+abs(r-i))*eps,
                            "subwindow crosses a later gate")
            if depth+1 < horizon:
                prefixes = [child for s in prefixes for child, _ in model.children(s)]
        report["boundary_subwindows"] = {
            "center": list(map(str, seed.coordinates)),
            "later_gates_constant_half_width": str(eps), "gate_window_power": n,
            "also_all_terminal_outputs_distinct_half_width": str(inject_eps),
            "injective_window_power": m,
            "initial_interface": "x[0]+x[1]=0",
            "minimum_later_center_gate_margin": str(smallest_noninitial_gate_margin),
            "scope": "all branch prefixes through the selected horizon; half-windows separated by the initial interface"}
    return report


def negative_controls(model):
    rejected = []
    def rejects(name, f):
        try:
            f()
        except (ValueError, ps.NeedsRefinement):
            rejected.append(name)
        else:
            raise AssertionError("accepted invalid control: "+name)
    rejects("zero observation scale", lambda: ps.Seed(CENTER, (F(0), F(0)), "bad"))
    rejects("invalid radius", lambda: ps.gate_row(ps.State(ps.Seed(CENTER, (F(1), F(1)), "unit")), F(0)))
    root = ps.State(ps.Seed(CENTER, (F(1), F(1)), "unit", DIRECTION))
    child = next(s for s, _ in model.children(root) if model.row(s) != model.row(root))
    rejects("reuse stale starting gate", lambda: model.advance(child, 0, expected_row=model.row(root)))
    rejects("out-of-range channel", lambda: model.advance(root, 32))
    rejects("unresolved scale sign", lambda: ps.sign_of_germ(((F(-1), F(1)), (F(1), F(1)))))
    # Same value, different retained scales: the forward value quotient fails
    # across scale leaves, using actual frozen gate rows.
    a = (F(1, 4), -F(3, 16))+(F(0),)*6
    seeds = [ps.Seed(tuple(x/c for x in a), (c, c), str(c)) for c in (F(1), F(1, 4))]
    states = list(map(ps.State, seeds))
    require(states[0].value_bounds() == states[1].value_bounds(), "scale witness values differ")
    rows = [model.row(s) for s in states]
    require(rows == [12, 13], "scale witness gate rows")
    variation = gate.tv_bounds(*(model.probabilities[r] for r in rows))
    require(variation[0] > 0, "scale was observationally irrelevant")
    outputs = [s.value_bounds()[0] for s, _ in model.children(states[0])]
    require(len(set(outputs)) == 32, "scale witness output collision")
    return {"rejected": rejected, "same_value_different_scale": {
        "scales": ["1", "1/4"], "gate_rows": rows,
        "value_output_TV_enclosure": gate.decimal_enclosure(variation)}}


def check_gate_conventions():
    # Exact, non-dyadic scales must not lose rational equality through rounding.
    require(ps.reciprocal((F(3), F(3))) == (F(1, 3), F(1, 3)),
            "exact rational scale was unnecessarily rounded")
    rays = [((-1, -1), 1), ((0, -1), 2), ((1, -1), 3),
            ((1, 0), 4), ((1, 1), 5), ((0, 1), 6),
            ((-1, 1), 7), ((-1, 0), 7), ((0, 0), 4)]
    count = 0
    for (x, y), sector in rays:
        seed = ps.Seed((F(x, 16), F(y, 16))+(F(0),)*6,
                       (F(3), F(3)), "rational-three")
        require(ps.gate_row(ps.State(seed)) == 4*sector, "angular tie contract")
        count += 1
    for radius, expected_depth in ((F(1), 1), (F(2), 2), (F(3), 3)):
        seed = ps.Seed((radius,)+(F(0),)*7, (F(1), F(1)), "unit")
        state = ps.State(seed)
        require(ps.gate_row(state) == 16+expected_depth, "radial point tie")
        for sign, expected in ((-1, expected_depth-1), (1, expected_depth)):
            directed = ps.Seed(seed.coordinates, seed.scale, seed.scale_name,
                               (F(sign),)+(F(0),)*7)
            require(ps.gate_row(ps.State(directed)) == 16+expected,
                    "radial one-sided tie")
            count += 1
        count += 1
    return {"exact_rational_scale": "3", "angular_and_radial_tie_checks": count}


def crosscheck_numpy(path, relations_path, model, seeds):
    prior.pin_bytes(path, ALGEBRA_BLOB)
    import numpy as np
    spec = importlib.util.spec_from_file_location("pinned_pal_algebra", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    data = json.loads(Path(relations_path).read_text())
    atlas = SimpleNamespace(q=np.array([c["q"] for c in data["channels"]]),
                            m_real=np.array([c["m_real"] for c in data["channels"]]),
                            m_imag=np.array([c["m_imag"] for c in data["channels"]]),
                            complex_pairs=True, value_for=lambda x: x)
    largest = 0.0
    native_steps = gate_checks = 0
    for seed in seeds:
        c = float(sum(seed.scale)/2)
        words = [(j, j, j) for j in range(32)]+[(j, (j+1)%32, (j+7)%32) for j in range(32)]
        for word in words:
            state = ps.State(seed)
            numeric = np.array(list(map(float, seed.coordinates)))*c
            for j in word:
                numeric = module.transport(atlas, numeric, j)
                state = model.advance(state, j)
                reference = np.array([float((lo+hi)/2) for lo, hi in state.value_bounds()])
                largest = max(largest, float(np.max(np.abs(numeric-reference))))
                native_steps += 1
                # Independent numeric formula from _bin_index; no claim that
                # the unavailable training checkpoint or torch runtime ran.
                x = numeric/c
                sec = int(np.clip(np.floor((np.arctan2(x[1], x[0])+np.pi)/(2*np.pi)*8), 0, 7))
                dep = int(np.clip(np.floor(np.linalg.norm(x)/float(model.radius)*4), 0, 3))
                require(4*sec+dep == model.row(state), "numeric gate cross-check")
                gate_checks += 1
    require(largest < 1e-12, "native PAL transport disagreement")
    return {"native_transport_calls": native_steps, "numeric_gate_crosschecks": gate_checks,
            "maximum_absolute_value_error": largest,
            "status": "numerical cross-check only; exact certificate is separate"}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--relations", type=Path, required=True)
    parser.add_argument("--gate-logits", type=Path, required=True)
    parser.add_argument("--concepts", type=Path, required=True)
    parser.add_argument("--pal-algebra", type=Path)
    parser.add_argument("--horizon", type=int, default=3)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    require(1 <= args.horizon <= 3, "this replay budget supports horizons 1 to 3")
    contract_raw = CONTRACT_PATH.read_bytes()
    contract = json.loads(contract_raw)
    require(contract["interface_id"] == ps.INTERFACE_ID, "wrong interface contract")
    require(contract["successor"]["gate_radius"] == "4", "wrong gate radius")
    model = ps.Successor.from_files(args.relations, args.gate_logits)
    concept, concept_meta = pick_concept(args.concepts)
    unit = ps.Seed(CENTER, (F(1), F(1)), "unit", DIRECTION)
    negative_port = ps.State(ps.Seed(CENTER, (F(1), F(1)), "unit", tuple(-x for x in DIRECTION)))
    require(model.row(negative_port) == 8 and model.row(ps.State(unit)) == 12,
            "initial directional-port interpretation")
    report = {"status": "PASS", "interface_id": ps.INTERFACE_ID,
              "contract_sha256": hashlib.sha256(contract_raw).hexdigest(),
              "source_commit": gate.SOURCE_COMMIT, "horizon": args.horizon,
              "boundary_seed": audit_tree(model, unit, args.horizon, paired=True),
              "concept_seed_metadata": concept_meta,
              "concept_seed": audit_tree(model, concept, args.horizon),
              "negative_controls": negative_controls(model),
              "gate_conventions": check_gate_conventions(),
              "scope": "specified successor completion of real frozen parameters; exhaustive finite trees; not trained rollout semantics or predictive accuracy"}
    if args.pal_algebra:
        report["native_crosscheck"] = crosscheck_numpy(args.pal_algebra, args.relations, model, [unit, concept])
    text = json.dumps(report, ensure_ascii=False, indent=2)+"\n"
    if args.output:
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")


if __name__ == "__main__":
    main()
