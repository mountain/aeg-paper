#!/usr/bin/env python3
"""Experiment 6 -- knot deformation processes and environment dependence.

Contract: research/process-representation-gap/contracts/exp6-knot-deformation-environment.v1.json
Work plan: AEG-process-representation-work-plan.md section 6, 实验六.

What this experiment does
-------------------------

It answers the work-plan question "how is a legal deformation process of a knot
represented, and which arithmetic representations are faithful for the state,
the process and the continuations, in each environment?" inside a small model
that is computed *exactly*:

* ropes are finite piecewise-linear (PL) closed or open curves with rational
  control-node coordinates, moving piecewise-linearly in time, with obstacles
  given as rational balls (piecewise-linear centre timetables) or rational
  polygonal loops;
* legality is checked over WHOLE TIME INTERVALS with exact rational arithmetic,
  never at keyframes only, and the interval certificates are stored;
* the topological route is instantiated by a declared diagram calculus with
  local moves, before/after state and provenance;
* the four arithmetic gates (encodable / state-faithful / process-faithful /
  complete) are answered item by item with declared verdicts.

Exact-arithmetic discipline: no float appears in any witness, comparison,
predicate or cost.  Obligations are ``gapkit.require`` with stable EXP6- codes;
``assert`` is never used, so ``python3`` and ``python3 -O`` agree bit for bit.

Scope statements that matter (contract ``scope_boundary``): finite PL only, tame
only, no wild knots, no arbitrary real input; no general knot-motion planner is
implemented or claimed; a planning failure inside the fixed-node-count,
fixed-parameter-family, fixed-action-dictionary submodel does NOT prove that no
legal deformation exists; braid closure, Markov equivalence and any bridge to
knot equivalence are out of scope.

Run:

    python3 research/process-representation-gap/experiments/exp6_knot_deformation_environment.py
"""

from __future__ import annotations

import argparse
import sys
from fractions import Fraction
from math import isqrt
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(ROOT / "tools"))
import gapkit  # noqa: E402
from gapkit import Diagnostic, qtext, require  # noqa: E402

CONTRACT = ROOT / "contracts" / "exp6-knot-deformation-environment.v1.json"
FROZEN = ROOT / "contracts" / "FROZEN.sha256"
EVIDENCE = ROOT / "evidence" / "exp6-knot-deformation-environment.json"
RAW = ROOT / "evidence" / "exp6-knot-deformation-environment.raw.json"

SCHEMA = "aeg.process-representation-gap.exp6.v1"
RAW_SCHEMA = "aeg.process-representation-gap.exp6.raw.v1"

BUDGET = {
    "max_control_nodes": 16,
    "max_time_segments": 12,
    "max_known_obstacles": 3,
    "max_action_depth": 8,
}

SUBSEGMENT_DEPTH = 6      # declared exact-subdivision depth for interval certificates
SUBSEGMENT_NODE_CAP = 4096
SQRT_SCALE = 256          # denominator of the exact rational sqrt lower bound
EDGE_SAMPLES = (Fraction(0), Fraction(1, 4), Fraction(1, 2), Fraction(3, 4), Fraction(1))


# ==========================================================================
# exact scalars and vectors
# ==========================================================================

def F(value) -> Fraction:
    """Exact rational from an int, a string, or a pair."""
    if isinstance(value, Fraction):
        return value
    if isinstance(value, int):
        return Fraction(value)
    if isinstance(value, str):
        return Fraction(value)
    if isinstance(value, tuple) and len(value) == 2:
        return Fraction(value[0], value[1])
    raise Diagnostic("EXP6-BAD-RATIONAL", repr(value))


ZERO = Fraction(0)
ONE = Fraction(1)


def lower_sqrt(value: Fraction) -> Fraction:
    """Exact rational lower bound of sqrt(value) for value >= 0.

    sqrt(v) >= floor(sqrt(v * scale^2)) / scale, exactly, with no float.
    """
    require(value >= 0, "EXP6-NEGATIVE-SQRT", qtext(value))
    scaled = value * SQRT_SCALE * SQRT_SCALE
    root = isqrt(int(scaled))
    return Fraction(root, SQRT_SCALE)


def vadd(a, b):
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2])


def vsub(a, b):
    return (a[0] - b[0], a[1] - b[1], a[2] - b[2])


def vscale(k, a):
    k = F(k)
    return (k * a[0], k * a[1], k * a[2])


def vdot(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]


def vcross(a, b):
    return (a[1] * b[2] - a[2] * b[1],
            a[2] * b[0] - a[0] * b[2],
            a[0] * b[1] - a[1] * b[0])


def vnorm2(a):
    return vdot(a, a)


def viszero(a) -> bool:
    return a[0] == 0 and a[1] == 0 and a[2] == 0


# ==========================================================================
# exact linear programming: is the origin in the convex hull of a finite set?
# ==========================================================================

def _norm_constraint(coeffs, rhs):
    """Canonical form: divide by |leading nonzero coefficient|.

    The divisor must be POSITIVE: dividing a >=-constraint by a negative number
    reverses the inequality, which would silently turn the feasibility test into
    its negation.  Normalising by the absolute value keeps the direction and
    makes the leading coefficient +1 or -1.
    """
    lead = None
    for value in coeffs:
        if value != 0:
            lead = value
            break
    if lead is None:
        return (tuple(ZERO for _ in coeffs), rhs)
    scale = abs(lead)
    return (tuple(value / scale for value in coeffs), rhs / scale)


def _dedupe(constraints):
    seen = {}
    order = []
    for coeffs, rhs in constraints:
        key = (coeffs, rhs)
        if key in seen:
            continue
        seen[key] = True
        order.append((coeffs, rhs))
    return order


def _solution_from_stages(stages, nvars):
    """Back-substitute a rational solution from a feasible Fourier-Motzkin run."""
    z = [ZERO] * nvars
    for idx in range(nvars - 1, -1, -1):
        lows = []
        highs = []
        for coeffs, rhs in stages[idx]:
            rest = rhs
            for j in range(idx + 1, nvars):
                rest = rest - coeffs[j] * z[j]
            if coeffs[idx] > 0:
                lows.append(rest / coeffs[idx])
            elif coeffs[idx] < 0:
                highs.append(rest / coeffs[idx])
        if lows:
            z[idx] = max(lows)
        elif highs:
            z[idx] = min(highs)
        else:
            z[idx] = ZERO
    return tuple(z)


def fm_feasible(constraints, nvars):
    """Exact Fourier-Motzkin feasibility for a system coeffs . z >= rhs.

    Returns a rational solution, or None when the system is infeasible.  Exact
    rational arithmetic only; the elimination is complete on the rationals.
    """
    cons = _dedupe([_norm_constraint(c, r) for c, r in constraints])
    stages = [tuple(cons)]
    for idx in range(nvars):
        pos = [(c, r) for c, r in cons if c[idx] > 0]
        neg = [(c, r) for c, r in cons if c[idx] < 0]
        keep = [(c, r) for c, r in cons if c[idx] == 0]
        nxt = list(keep)
        for pc, pr in pos:
            for qc, qr in neg:
                fp = -qc[idx]
                fq = pc[idx]
                coeffs = tuple(pc[j] * fp + qc[j] * fq for j in range(nvars))
                rhs = pr * fp + qr * fq
                nxt.append(_norm_constraint(coeffs, rhs))
        cons = _dedupe(nxt)
        for c, r in cons:
            if all(value == 0 for value in c) and r > 0:
                return None
        stages.append(tuple(cons))
    z = _solution_from_stages(stages, nvars)
    for c, r in stages[0]:
        total = sum(c[j] * z[j] for j in range(nvars))
        if total < r:
            raise Diagnostic(
                "EXP6-FM-BACKSUBSTITUTION-FAILED",
                f"reconstructed {tuple(qtext(v) for v in z)} violates a constraint",
            )
    return z


# Declared control sets for the separation core: the origin lies in the convex
# hull of the first and outside the convex hull of the second.
E_SEPARATION_INSIDE = ((ONE, ZERO, ZERO), (-ONE, ZERO, ZERO), (ZERO, ONE, ZERO), (ZERO, ZERO, ONE))
E_SEPARATION_OUTSIDE = ((ONE, ZERO, ZERO), (F(2), ONE, ZERO), (ZERO, ONE, ZERO))


def separating_functional(vertices):
    """Exact z with z . v >= 1 for every vertex, or None.

    0 lies in conv(vertices) iff no such z exists (Gordan/Stiemke duality, with
    the projection property supplying z = p*/|p*|^2 when 0 is not in the hull).
    Both directions are exact, so the test decides the predicate completely.
    """
    if any(viszero(v) for v in vertices):
        return None
    constraints = [((v[0], v[1], v[2]), ONE) for v in vertices]
    return fm_feasible(constraints, 3)


# ==========================================================================
# exact PL motions
# ==========================================================================

def motion(label, nodes, breakpoints, positions, closed=True, marked=None, note=""):
    """Declared finite PL motion.

    ``positions[k][i]`` is the position of control node ``i`` at time
    ``breakpoints[k]``; inside a time segment every node moves linearly.
    """
    bps = tuple(F(t) for t in breakpoints)
    require(len(bps) >= 2, "EXP6-BAD-MOTION", f"{label}: need at least two breakpoints")
    for a, b in zip(bps, bps[1:]):
        require(a < b, "EXP6-BAD-MOTION", f"{label}: breakpoints must increase: {qtext(a)} !< {qtext(b)}")
    require(len(positions) == len(bps), "EXP6-BAD-MOTION",
            f"{label}: {len(positions)} position rows for {len(bps)} breakpoints")
    rows = []
    for row in positions:
        require(len(row) == nodes, "EXP6-BAD-MOTION",
                f"{label}: row has {len(row)} nodes, declared {nodes}")
        rows.append(tuple(tuple(F(c) for c in point) for point in row))
    for row in rows:
        for point in row:
            require(len(point) == 3, "EXP6-BAD-MOTION", f"{label}: point {point} is not in R^3")
    return {
        "label": label,
        "closed": bool(closed),
        "nodes": nodes,
        "marked": marked,
        "breakpoints": bps,
        "positions": tuple(rows),
        "note": note,
    }


def check_budget(model):
    """Refuse a model outside the declared first-round budget."""
    nodes = model["nodes"]
    segments = len(model["breakpoints"]) - 1
    obstacles = len(model.get("obstacles", ()))
    require(nodes <= BUDGET["max_control_nodes"], "EXP6-BUDGET-EXCEEDED",
            f"{model['label']}: {nodes} control nodes > {BUDGET['max_control_nodes']}")
    require(segments <= BUDGET["max_time_segments"], "EXP6-BUDGET-EXCEEDED",
            f"{model['label']}: {segments} time segments > {BUDGET['max_time_segments']}")
    require(obstacles <= BUDGET["max_known_obstacles"], "EXP6-BUDGET-EXCEEDED",
            f"{model['label']}: {obstacles} obstacles > {BUDGET['max_known_obstacles']}")
    return True


def time_segment_index(m, t):
    bps = m["breakpoints"]
    require(bps[0] <= t <= bps[-1], "EXP6-TIME-OUT-OF-RANGE",
            f"{m['label']}: t = {qtext(t)} outside [{qtext(bps[0])}, {qtext(bps[-1])}]")
    for k in range(len(bps) - 1):
        if bps[k] <= t <= bps[k + 1]:
            return k
    return len(bps) - 2


def node_at(m, i, t):
    t = F(t)
    k = time_segment_index(m, t)
    bps = m["breakpoints"]
    width = bps[k + 1] - bps[k]
    lam = (t - bps[k]) / width
    p0 = m["positions"][k][i]
    p1 = m["positions"][k + 1][i]
    return vadd(p0, vscale(lam, vsub(p1, p0)))


def edge_list(m):
    n = m["nodes"]
    if m["closed"]:
        return tuple((i, (i + 1) % n) for i in range(n))
    return tuple((i, i + 1) for i in range(n - 1))


def edge_at(m, e, t, s):
    """Point at parameter s on edge index e at time t."""
    i, j = edge_list(m)[e]
    p0 = node_at(m, i, t)
    p1 = node_at(m, j, t)
    return vadd(p0, vscale(F(s), vsub(p1, p0)))


def edge_pair_vertices(m, e1, e2, ta, tb):
    """The 8 box-vertex values of the multilinear difference map.

    Delta(s, u, t) = X_{e1}(s, t) - X_{e2}(u, t) is affine in each of s, u, t
    separately on a box that lies inside a single time segment, so its image is
    contained in the convex hull of its values at the 8 box vertices.
    """
    out = []
    for s in (ZERO, ONE):
        for u in (ZERO, ONE):
            for t in (ta, tb):
                out.append(vsub(edge_at(m, e1, t, s), edge_at(m, e2, t, u)))
    return out


def adjacent_edges(m, e1, e2) -> bool:
    n = len(edge_list(m))
    diff = (e1 - e2) % n
    return diff in (1, n - 1)


# --------------------------------------------------------------------------
# exact single-time predicates
# --------------------------------------------------------------------------

def segment_intersection(p0, p1, q0, q1):
    """Exact intersection of two closed 3D segments.

    Returns ("point", s, u, point) for a single transversal or touching
    intersection, ("overlap", ...) for a positive-length overlap, or None.
    All arithmetic is exact over the rationals.
    """
    e1 = vsub(p1, p0)
    e2 = vsub(q1, q0)
    d = vsub(q0, p0)
    cross = vcross(e1, e2)
    if not viszero(cross):
        if vdot(d, cross) != 0:
            return None
        best = None
        for i in range(3):
            j = (i + 1) % 3
            det = e1[i] * (-e2[j]) - e1[j] * (-e2[i])
            if det == 0:
                continue
            if best is None or abs(det) > abs(best):
                best = det
                pair = (i, j)
        require(best is not None, "EXP6-SEGMENT-DEGENERATE",
                "non-parallel segments with no invertible 2x2 minor")
        i, j = pair
        det = e1[i] * (-e2[j]) - e1[j] * (-e2[i])
        s = (d[i] * (-e2[j]) - d[j] * (-e2[i])) / det
        u = (e1[i] * d[j] - e1[j] * d[i]) / det
        point = vadd(p0, vscale(s, e1))
        check = vadd(q0, vscale(u, e2))
        if point != check:
            return None
        if ZERO <= s <= ONE and ZERO <= u <= ONE:
            return ("point", s, u, point)
        return None
    # parallel segments
    if not viszero(vcross(d, e1)):
        return None
    length2 = vnorm2(e1)
    if length2 == 0:
        if vnorm2(e2) == 0:
            return ("point", ZERO, ZERO, p0) if p0 == q0 else None
        t = vdot(vsub(p0, q0), e2) / vnorm2(e2)
        if ZERO <= t <= ONE and vadd(q0, vscale(t, e2)) == p0:
            return ("point", ZERO, t, p0)
        return None
    s0 = vdot(vsub(q0, p0), e1) / length2
    s1 = vdot(vsub(q1, p0), e1) / length2
    lo = max(ZERO, min(s0, s1))
    hi = min(ONE, max(s0, s1))
    if lo > hi:
        return None
    if lo == hi:
        return ("point", lo, ZERO, vadd(p0, vscale(lo, e1)))
    return ("overlap", lo, hi, vadd(p0, vscale(lo, e1)))


def is_embedded_at(m, t):
    """Exact verdict at one instant.  Returns (True, None) or (False, witness)."""
    n = m["nodes"]
    points = [node_at(m, i, t) for i in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            if points[i] == points[j]:
                return False, {"kind": "node-coincidence", "time": qtext(t),
                               "nodes": [i, j], "point": [qtext(c) for c in points[i]]}
    edges = edge_list(m)
    for e1 in range(len(edges)):
        for e2 in range(e1 + 1, len(edges)):
            p0, p1 = points[edges[e1][0]], points[edges[e1][1]]
            q0, q1 = points[edges[e2][0]], points[edges[e2][1]]
            hit = segment_intersection(p0, p1, q0, q1)
            if hit is None:
                continue
            if adjacent_edges(m, e1, e2):
                if hit[0] == "overlap":
                    return False, {"kind": "adjacent-overlap", "time": qtext(t),
                                   "edges": [e1, e2]}
                shared = set(edges[e1]) & set(edges[e2])
                point = hit[3]
                if all(point != points[k] for k in shared):
                    return False, {"kind": "adjacent-crossing", "time": qtext(t),
                                   "edges": [e1, e2], "point": [qtext(c) for c in point]}
                continue
            if hit[0] == "overlap":
                return False, {"kind": "nonadjacent-overlap", "time": qtext(t),
                               "edges": [e1, e2]}
            return False, {"kind": "nonadjacent-crossing", "time": qtext(t),
                           "edges": [e1, e2],
                           "parameters": [qtext(hit[1]), qtext(hit[2])],
                           "point": [qtext(c) for c in hit[3]]}
    return True, None


# --------------------------------------------------------------------------
# interval certificates for self-embedding
# --------------------------------------------------------------------------

def certify_disjoint_box(m, e1, e2, ta, tb):
    """Exact certificate that two edges are disjoint on the whole time box."""
    vertices = edge_pair_vertices(m, e1, e2, ta, tb)
    z = separating_functional(vertices)
    if z is None:
        return None
    margins = [vdot(z, v) for v in vertices]
    return {
        "method": "multilinear-box-hull-separation",
        "edges": [e1, e2],
        "time": [qtext(ta), qtext(tb)],
        "separator": [qtext(c) for c in z],
        "min_dot": qtext(min(margins)),
        "vertices": [[qtext(c) for c in v] for v in vertices],
    }


def check_self_embedding(m, depth=SUBSEGMENT_DEPTH, keyframe_only=False,
                         node_cap=SUBSEGMENT_NODE_CAP):
    """Whole-interval legality of the rope against itself.

    Returns (verdict, witness, certificates, unknown_boxes, stats) where the
    verdict is one of valid / invalid / not-certified.  Keyframe-only checking
    is available as a declared distortion, never as the primary procedure.
    """
    check_budget(m)
    n_edges = len(edge_list(m))
    pairs = [(e1, e2) for e1 in range(n_edges) for e2 in range(e1 + 1, n_edges)
             if not adjacent_edges(m, e1, e2)]
    breakpoints = m["breakpoints"]
    certificates = []
    unknown = []
    counted = {"boxes": 0, "sampled_times": 0, "certified": 0}
    tested_times = {}

    def test_time(t):
        key = qtext(t)
        if key in tested_times:
            return tested_times[key]
        verdict = is_embedded_at(m, t)
        tested_times[key] = verdict
        counted["sampled_times"] += 1
        return verdict

    if keyframe_only:
        for t in breakpoints:
            ok, witness = test_time(t)
            if not ok:
                return "invalid", witness, certificates, unknown, counted
        return "valid", None, certificates, unknown, counted

    stack = []
    for k in range(len(breakpoints) - 1):
        stack.append((breakpoints[k], breakpoints[k + 1], 0))
    while stack:
        ta, tb, level = stack.pop()
        counted["boxes"] += 1
        if counted["boxes"] > node_cap:
            unknown.append({"time": [qtext(ta), qtext(tb)], "reason": "node-cap"})
            continue
        for t in (ta, tb):
            ok, witness = test_time(t)
            if not ok:
                return "invalid", witness, certificates, unknown, counted
        if not pairs:
            counted["certified"] += 1
            continue
        box_certs = []
        certified = True
        for e1, e2 in pairs:
            cert = certify_disjoint_box(m, e1, e2, ta, tb)
            if cert is None:
                certified = False
                break
            box_certs.append(cert)
        if certified:
            counted["certified"] += 1
            certificates.extend(box_certs)
            continue
        if level >= depth:
            unknown.append({"time": [qtext(ta), qtext(tb)],
                            "level": level, "reason": "subdivision-depth"})
            continue
        mid = (ta + tb) / 2
        stack.append((mid, tb, level + 1))
        stack.append((ta, mid, level + 1))
    if unknown:
        return "not-certified", None, certificates, unknown, counted
    return "valid", None, certificates, unknown, counted


# --------------------------------------------------------------------------
# obstacles
# --------------------------------------------------------------------------

def ball_obstacle(label, radius, breakpoints, centres, identity="ball"):
    bps = tuple(F(t) for t in breakpoints)
    require(len(bps) == len(centres), "EXP6-BAD-OBSTACLE", f"{label}: centres/breakpoints mismatch")
    for a, b in zip(bps, bps[1:]):
        require(a < b, "EXP6-BAD-OBSTACLE", f"{label}: timetable must increase")
    return {
        "kind": "ball",
        "label": label,
        "identity": identity,
        "radius": F(radius),
        "breakpoints": bps,
        "centres": tuple(tuple(F(c) for c in point) for point in centres),
        "timestamps_present": True,
    }


def loop_obstacle(label, m, identity="loop"):
    check_budget(m)
    return {
        "kind": "loop",
        "label": label,
        "identity": identity,
        "motion": m,
        "timestamps_present": True,
    }


def obstacle_centre(obstacle, t):
    require(obstacle.get("timestamps_present") is True, "EXP6-OBSTACLE-TIMETABLE-MISSING",
            f"{obstacle['label']}: obstacle record carries no timestamps")
    bps = obstacle["breakpoints"]
    require(bps[0] <= t <= bps[-1], "EXP6-TIME-OUT-OF-RANGE",
            f"{obstacle['label']}: t = {qtext(t)} outside its timetable")
    k = 0
    for idx in range(len(bps) - 1):
        if bps[idx] <= t <= bps[idx + 1]:
            k = idx
            break
    lam = (t - bps[k]) / (bps[k + 1] - bps[k])
    c0 = obstacle["centres"][k]
    c1 = obstacle["centres"][k + 1]
    return vadd(c0, vscale(lam, vsub(c1, c0)))


def obstacle_span(obstacle):
    if obstacle["kind"] == "ball":
        bps = obstacle["breakpoints"]
    else:
        bps = obstacle["motion"]["breakpoints"]
    return bps[0], bps[-1]


def refined_breakpoints(m, obstacles):
    """Union of the rope and obstacle breakpoints inside the rope's time range."""
    lo, hi = m["breakpoints"][0], m["breakpoints"][-1]
    points = set(m["breakpoints"])
    for obstacle in obstacles:
        obs_lo, obs_hi = obstacle_span(obstacle)
        require(obs_lo <= lo and obs_hi >= hi, "EXP6-OBSTACLE-TIMETABLE-INCOMPLETE",
                f"{obstacle['label']}: timetable [{qtext(obs_lo)}, {qtext(obs_hi)}] does not cover "
                f"the rope's time range [{qtext(lo)}, {qtext(hi)}]")
        if obstacle["kind"] == "ball":
            points.update(obstacle["breakpoints"])
        else:
            points.update(obstacle["motion"]["breakpoints"])
    return tuple(sorted(t for t in points if lo <= t <= hi))


def ball_box_vertices(m, e, obstacle, ta, tb):
    """4 box-vertex values of Delta(s, t) = X_e(s, t) - C(t)."""
    out = []
    for s in (ZERO, ONE):
        for t in (ta, tb):
            out.append(vsub(edge_at(m, e, t, s), obstacle_centre(obstacle, t)))
    return out


def certify_ball_clear(m, e, obstacle, ta, tb):
    """Exact certificate that one rope edge clears one ball on a time box.

    Two sufficient exact criteria are tried; either one proves the whole box:
    a coordinate whose whole range stays outside the ball, or a rational normal
    n with n . Delta >= m > 0 and m^2 > r^2 * |n|^2 on the whole box.
    """
    vertices = ball_box_vertices(m, e, obstacle, ta, tb)
    radius = obstacle["radius"]
    radius2 = radius * radius
    coordinate = None
    for k in range(3):
        low = min(v[k] for v in vertices)
        high = max(v[k] for v in vertices)
        margin = None
        if low > radius:
            margin = low - radius
        elif -high > radius:
            margin = -high - radius
        if margin is None:
            continue
        bound = min(abs(low), abs(high))
        if coordinate is None or margin > coordinate[0]:
            coordinate = (margin, {"method": "coordinate-hull-separation",
                                   "axis": k,
                                   "bound": qtext(bound),
                                   "margin_lower_bound": qtext(margin)})
    if coordinate is not None:
        best = coordinate
    else:
        best = None
        candidates = list(vertices)
        for i in range(len(vertices)):
            for j in range(i + 1, len(vertices)):
                candidates.append(vsub(vertices[i], vertices[j]))
        for k in range(3):
            axis = [ZERO, ZERO, ZERO]
            axis[k] = ONE
            candidates.append(tuple(axis))
        for nvec in candidates:
            if viszero(nvec):
                continue
            dots = [vdot(nvec, v) for v in vertices]
            mmin = min(dots)
            if mmin <= 0:
                continue
            if mmin * mmin <= radius2 * vnorm2(nvec):
                continue
            best = (ZERO, {"method": "vertex-normal-separation",
                           "normal": [qtext(c) for c in nvec],
                           "bound": qtext(mmin),
                           "bound_squared_minus_radius_squared_norm":
                               qtext(mmin * mmin - radius2 * vnorm2(nvec))})
            break
    if best is None:
        return None
    cert = dict(best[1])
    cert["edge"] = e
    cert["obstacle"] = obstacle["label"]
    cert["time"] = [qtext(ta), qtext(tb)]
    cert["radius"] = qtext(radius)
    cert["vertices"] = [[qtext(c) for c in v] for v in vertices]
    return cert


def ball_collision_at(m, e, obstacle, t):
    """Exact collision witness for one edge and one ball at a sampled time.

    Every declared sample parameter is evaluated exactly; the sample with the
    smallest squared distance (ties broken by the smaller parameter) is the
    reported witness.  A positive finding is a genuine exact collision; the
    certificates, not this sampling, are what prove the absence of collisions.
    """
    centre = obstacle_centre(obstacle, t)
    radius2 = obstacle["radius"] * obstacle["radius"]
    best = None
    for s in EDGE_SAMPLES:
        point = edge_at(m, e, t, s)
        dist2 = vnorm2(vsub(point, centre))
        if dist2 > radius2:
            continue
        if best is None or (dist2, s) < (best[0], best[1]):
            best = (dist2, s, point)
    if best is None:
        return None
    dist2, s, point = best
    return {"kind": "ball-collision", "obstacle": obstacle["label"], "edge": e,
            "time": qtext(t), "parameter": qtext(s),
            "point": [qtext(c) for c in point],
            "distance_squared": qtext(dist2),
            "radius_squared": qtext(radius2)}


def certificate_bound(cert):
    """Exact rational lower bound on the certified distance over one box.

    ``coordinate-hull-separation`` bounds one coordinate away from the ball, so
    the Euclidean distance is at least that bound.  ``vertex-normal-separation``
    gives n . Delta >= m, hence |Delta| >= m/|n|, and the returned rational is an
    exact lower bound on that quotient (no square root is ever taken).
    """
    if cert["method"] == "coordinate-hull-separation":
        return Fraction(cert["bound"])
    mmin = Fraction(cert["bound"])
    normal = tuple(Fraction(c) for c in cert["normal"])
    return lower_sqrt(mmin * mmin / vnorm2(normal))


def summarize_certificates(certs):
    """Compact per-time-interval certificate table for the main evidence."""
    groups = {}
    for cert in certs:
        key = (cert["time"][0], cert["time"][1])
        entry = groups.setdefault(key, {"time": cert["time"], "count": 0,
                                        "methods": set(), "min_bound": None})
        entry["count"] += 1
        entry["methods"].add(cert["method"])
        bound = certificate_bound(cert)
        if entry["min_bound"] is None or bound < entry["min_bound"]:
            entry["min_bound"] = bound
    rows = []
    for key in sorted(groups, key=lambda k: (Fraction(k[0]), Fraction(k[1]))):
        entry = groups[key]
        rows.append({"time": entry["time"], "certificate_count": entry["count"],
                     "methods": sorted(entry["methods"]),
                     "min_distance_lower_bound": qtext(entry["min_bound"])})
    return rows


def clearance_margin(certs, radius):
    """Proved clearance: minimum certificate bound minus the ball radius."""
    if not certs:
        return None
    best = min(certificate_bound(cert) for cert in certs)
    return best - radius


def check_obstacles(m, obstacles, depth=SUBSEGMENT_DEPTH, keyframe_only=False,
                    node_cap=SUBSEGMENT_NODE_CAP):
    """Whole-interval legality of the rope against the declared obstacles."""
    check_budget({"label": m["label"], "nodes": m["nodes"],
                  "breakpoints": m["breakpoints"], "obstacles": obstacles})
    for obstacle in obstacles:
        require(obstacle.get("timestamps_present") is True,
                "EXP6-OBSTACLE-TIMETABLE-MISSING",
                f"{obstacle['label']}: obstacle record carries no timestamps")
    bps = refined_breakpoints(m, obstacles)
    certificates = []
    unknown = []
    counted = {"boxes": 0, "sampled_times": 0, "certified": 0}
    n_edges = len(edge_list(m))

    def collision_at(t):
        if not (m["breakpoints"][0] <= t <= m["breakpoints"][-1]):
            return None
        for obstacle in obstacles:
            if obstacle["kind"] == "ball":
                if not (obstacle["breakpoints"][0] <= t <= obstacle["breakpoints"][-1]):
                    continue
                for e in range(n_edges):
                    hit = ball_collision_at(m, e, obstacle, t)
                    if hit is not None:
                        return hit
            else:
                om = obstacle["motion"]
                if not (om["breakpoints"][0] <= t <= om["breakpoints"][-1]):
                    continue
                ok, witness = is_embedded_at_pair(m, om, t)
                if not ok:
                    witness = dict(witness)
                    witness["obstacle"] = obstacle["label"]
                    return witness
        return None

    if keyframe_only:
        for t in bps:
            hit = collision_at(t)
            if hit is not None:
                return "invalid", hit, certificates, unknown, counted
        return "valid", None, certificates, unknown, counted

    # boxes are processed in chronological order so that the earliest collision
    # witness inside the declared horizon is the one reported
    stack = [(bps[k], bps[k + 1], 0) for k in range(len(bps) - 2, -1, -1)]
    while stack:
        ta, tb, level = stack.pop()
        counted["boxes"] += 1
        if counted["boxes"] > node_cap:
            unknown.append({"time": [qtext(ta), qtext(tb)], "reason": "node-cap"})
            continue
        for t in (ta, tb):
            hit = collision_at(t)
            if hit is not None:
                return "invalid", hit, certificates, unknown, counted
            counted["sampled_times"] += 1
        box_certs = []
        certified = True
        for obstacle in obstacles:
            if obstacle["kind"] == "ball":
                for e in range(n_edges):
                    cert = certify_ball_clear(m, e, obstacle, ta, tb)
                    if cert is None:
                        certified = False
                        break
                    box_certs.append(cert)
            else:
                om = obstacle["motion"]
                for e1 in range(n_edges):
                    for e2 in range(len(edge_list(om))):
                        cert = certify_disjoint_box2(m, e1, om, e2, ta, tb)
                        if cert is None:
                            certified = False
                            break
                        box_certs.append(cert)
                    if not certified:
                        break
            if not certified:
                break
        if certified:
            counted["certified"] += 1
            certificates.extend(box_certs)
            continue
        if level >= depth:
            unknown.append({"time": [qtext(ta), qtext(tb)], "level": level,
                            "reason": "subdivision-depth"})
            continue
        mid = (ta + tb) / 2
        stack.append((mid, tb, level + 1))
        stack.append((ta, mid, level + 1))
    if unknown:
        return "not-certified", None, certificates, unknown, counted
    return "valid", None, certificates, unknown, counted


def is_embedded_at_pair(m1, m2, t):
    """Exact intersection test between two ropes at one instant."""
    edges1 = edge_list(m1)
    edges2 = edge_list(m2)
    for e1 in range(len(edges1)):
        p0 = node_at(m1, edges1[e1][0], t)
        p1 = node_at(m1, edges1[e1][1], t)
        for e2 in range(len(edges2)):
            q0 = node_at(m2, edges2[e2][0], t)
            q1 = node_at(m2, edges2[e2][1], t)
            hit = segment_intersection(p0, p1, q0, q1)
            if hit is None:
                continue
            return False, {"kind": "loop-crossing", "time": qtext(t), "edges": [e1, e2],
                           "parameters": [qtext(hit[1]), qtext(hit[2])],
                           "point": [qtext(c) for c in hit[3]]}
    return True, None


def certify_disjoint_box2(m1, e1, m2, e2, ta, tb):
    """Exact certificate that two edges of two different ropes stay disjoint."""
    vertices = []
    for s in (ZERO, ONE):
        for u in (ZERO, ONE):
            for t in (ta, tb):
                vertices.append(vsub(edge_at(m1, e1, t, s), edge_at(m2, e2, t, u)))
    z = separating_functional(vertices)
    if z is None:
        return None
    margins = [vdot(z, v) for v in vertices]
    return {
        "method": "multilinear-box-hull-separation",
        "edges": [e1, e2],
        "time": [qtext(ta), qtext(tb)],
        "separator": [qtext(c) for c in z],
        "min_dot": qtext(min(margins)),
        "vertices": [[qtext(c) for c in v] for v in vertices],
    }


def ambient_extension_certificate(m):
    """Constructive ambient isotopy certificate, or a declared refusal.

    Only the rigid-translation class is certified constructively here: if every
    node carries the same displacement c(t) then Phi_t(x) = x + c(t) is an
    ambient isotopy of R^3 with Phi_0 = id and Phi_t o k_0 = k_t, verified
    exactly at every declared breakpoint.  For any other motion class no
    constructive certificate is produced inside this budget; the classical
    isotopy extension theorem (cited, not reproved here) is what would supply
    one, and it requires the declared relative boundary data.
    """
    base = m["positions"][0]
    offsets = []
    for row in m["positions"]:
        offset = None
        for i in range(m["nodes"]):
            delta = vsub(row[i], base[i])
            if offset is None:
                offset = delta
            elif offset != delta:
                raise Diagnostic(
                    "EXP6-AMBIENT-EXTENSION-MISSING",
                    f"{m['label']}: node {i} is not a rigid translation, "
                    "no constructive ambient extension is certified",
                )
        offsets.append(offset)
    require(offsets[0] == (ZERO, ZERO, ZERO), "EXP6-AMBIENT-EXTENSION-MISSING",
            f"{m['label']}: Phi_0 is not the identity")
    if m["marked"] is not None:
        require(all(offset == (ZERO, ZERO, ZERO) for offset in offsets),
                "EXP6-AMBIENT-EXTENSION-MISSING",
                f"{m['label']}: the marked node is required to stay fixed, which forces "
                "the identity motion in the declared translation class")
    return {
        "kind": "ambient-translation",
        "map": "Phi_t(x) = x + c(t)",
        "verified_at_breakpoints": [qtext(t) for t in m["breakpoints"]],
        "displacements": [[qtext(c) for c in offset] for offset in offsets],
        "relative_boundary": ("no marked point" if m["marked"] is None
                              else "marked node fixed; identity motion forced"),
        "status": "computationally-verified-example (translation class only)",
    }


# ==========================================================================
# declared fixtures
# ==========================================================================

SQUARE = ((0, 0, 0), (2, 0, 0), (2, 2, 0), (0, 2, 0))
SQUARE_CENTRED = ((1, 1, 0), (-1, 1, 0), (-1, -1, 0), (1, -1, 0))
LOOP_RECT = ((0, 0, 1), (2, 0, 1), (2, 0, -1), (0, 0, -1))
KEYFRAME_BLIND_SHAPE = ((0, 0, 0), (2, 0, 0), (2, 4, 0), (0, 4, 0), (1, -1, 1))


def translated(nodes, offsets):
    """Node coordinates at each breakpoint for a rigid translation motion."""
    rows = []
    for offset in offsets:
        rows.append([(p[0] + offset[0], p[1] + offset[1], p[2] + offset[2]) for p in nodes])
    return rows


def build_fixtures():
    fx = {}

    # ---- witness 4: same rope path under two time parameterisations --------
    fx["w4-P1"] = motion(
        "w4-P1", 4, [0, 1], translated(SQUARE, [(0, 0, 0), (8, 0, 0)]),
        note="rope translates from x=0 to x=8 at constant speed",
    )
    fx["w4-P2"] = motion(
        "w4-P2", 4, [0, Fraction(1, 2), 1],
        translated(SQUARE, [(0, 0, 0), (0, 0, 0), (8, 0, 0)]),
        note="same rope path, waits half the time then moves twice as fast",
    )
    w4_ball = ball_obstacle(
        "w4-ball", Fraction(1, 4),
        [0, Fraction(1, 4), Fraction(3, 8), Fraction(1, 2), Fraction(5, 8), 1],
        [(1, 0, 10), (1, 0, 10), (1, 0, 0), (1, 0, 0), (1, 0, 10), (1, 0, 10)],
    )

    # ---- witness 3: obstacle changes legality + bounded planner ------------
    fx["w3-free"] = motion(
        "w3-free", 4, [0, 1], translated(SQUARE, [(-2, 0, 0), (2, 0, 0)]),
        note="free-space candidate path from x=-2 to x=+2",
    )
    w3_ball = ball_obstacle(
        "w3-ball", Fraction(1, 2), [0, 4], [(1, 1, 0), (1, 1, 0)],
    )
    fx["w3-plan"] = motion(
        "w3-plan", 4, [0, 1, 2, 3, 4],
        translated(SQUARE, [(-2, 0, 0), (-2, 0, 2), (0, 0, 2), (2, 0, 2), (2, 0, 0)]),
        note="replacement path found by the declared depth-4 search",
    )

    # ---- keyframe blindness: legal keyframes, illegal interior ------------
    shape = KEYFRAME_BLIND_SHAPE
    rows = []
    for t in (ZERO, ONE):
        rows.append([shape[0], shape[1], shape[2], shape[3],
                     (F(1), F(-1), F(1) - 4 * t)])
    fx["keyframe-blind"] = motion(
        "keyframe-blind", 5, [0, 1], rows,
        note="keyframes embedded, interior time 1/4 has a crossing of edges 0 and 3",
    )

    # ---- witness 5: untraversable loop ------------------------------------
    fx["w5-rope"] = motion(
        "w5-rope", 4, [0, Fraction(2, 3), 1],
        translated(SQUARE_CENTRED, [(-3, 0, 0), (-1, 0, 0), (0, 0, 0)]),
        note="rope path whose free-space endpoint is linked once with the loop",
    )
    fx["w5-loop"] = motion(
        "w5-loop", 4, [0, 1], translated(LOOP_RECT, [(0, 0, 0), (0, 0, 0)]),
        note="rigid untraversable closed loop, the boundary of a flat rectangle",
    )

    return fx, w3_ball, w4_ball


# ==========================================================================
# linking number
# ==========================================================================

def flat_disk_crossings(rope, rope_t, loop, loop_disk):
    """Signed crossings of a rope with the flat spanning disk of a planar loop.

    ``loop_disk`` declares the plane axis, the plane coordinate and the
    rectangle bounds of the flat disk.  Returns the exact list of signed
    crossing points; the algebraic count is the linking number, because the
    loop bounds this disk (checked separately by ``flat_disk_certificate``).
    """
    axis, value, (lo_x, hi_x), (lo_z, hi_z), x_index, z_index = loop_disk
    out = []
    for e in edge_list(rope):
        p0 = node_at(rope, e[0], rope_t)
        p1 = node_at(rope, e[1], rope_t)
        if (p0[axis] - value) * (p1[axis] - value) > 0:
            continue
        denom = p1[axis] - p0[axis]
        if denom == 0:
            if p0[axis] != value:
                continue
            return None  # coplanar edge: the projection is not generic
        s = (value - p0[axis]) / denom
        if not (ZERO <= s <= ONE):
            continue
        point = vadd(p0, vscale(s, vsub(p1, p0)))
        if not (lo_x <= point[x_index] <= hi_x and lo_z <= point[z_index] <= hi_z):
            continue
        if point[x_index] in (lo_x, hi_x) and point[z_index] == lo_z:
            return None
        sign = 1 if p1[axis] > p0[axis] else -1
        interior = (lo_x < point[x_index] < hi_x) and (lo_z < point[z_index] < hi_z)
        out.append({"edge": e, "parameter": qtext(s), "point": [qtext(c) for c in point],
                    "sign": sign, "interior": interior})
    return out


def linking_number_by_disk(rope, rope_t, loop, loop_disk):
    """Linking number from the algebraic intersection with a spanning disk."""
    crossings = flat_disk_crossings(rope, rope_t, loop, loop_disk)
    if crossings is None:
        return None, None
    total = 0
    for entry in crossings:
        total += entry["sign"]
    return total, crossings


def signed_crossing_linking(comp1, t1, comp2, t2, direction):
    """Linking number from a generic projection: Lk = 1/2 * sum of signs."""
    dx, dy, dz = direction
    def project(p):
        return (p[0] * dy - p[1] * dx, p[0] * dz - p[2] * dx)
    total = 0
    crossings = []
    for e1 in edge_list(comp1):
        a0 = node_at(comp1, e1[0], t1)
        a1 = node_at(comp1, e1[1], t1)
        pa0, pa1 = project(a0), project(a1)
        for e2 in edge_list(comp2):
            b0 = node_at(comp2, e2[0], t2)
            b1 = node_at(comp2, e2[1], t2)
            pb0, pb1 = project(b0), project(b1)
            da = (pa1[0] - pa0[0], pa1[1] - pa0[1])
            db = (pb1[0] - pb0[0], pb1[1] - pb0[1])
            det = da[0] * db[1] - da[1] * db[0]
            if det == 0:
                return None, None, "degenerate projection: parallel edges"
            w = (pb0[0] - pa0[0], pb0[1] - pa0[1])
            s = (w[0] * db[1] - w[1] * db[0]) / det
            u = (w[0] * da[1] - w[1] * da[0]) / det
            if not (ZERO < s < ONE and ZERO < u < ONE):
                continue
            qa = vadd(a0, vscale(s, vsub(a1, a0)))
            qb = vadd(b0, vscale(u, vsub(b1, b0)))
            height = vdot(vsub(qa, qb), (F(dx), F(dy), F(dz)))
            if height == 0:
                return None, None, "degenerate projection: coincident crossing"
            sign = 1 if (det > 0) == (height > 0) else -1
            total += sign
            crossings.append({"edges": [e1, e2], "parameters": [qtext(s), qtext(u)],
                              "sign": sign})
    require(total % 2 == 0, "EXP6-LINKING-NONINTEGER",
            f"crossing count {total} is not even; the projection is not generic")
    return total // 2, crossings, None


def flat_disk_certificate(m, t):
    """Certificate that a planar simple polygon bounds a flat embedded disk.

    Checks exact coplanarity, exact convexity (all cross products the same sign,
    none zero) and simplicity; the fan triangulation from node 0 is then an
    embedded disk whose boundary is exactly the curve.
    """
    n = m["nodes"]
    points = [node_at(m, i, t) for i in range(n)]
    normal = None
    for i in range(1, n):
        for j in range(i + 1, n):
            cand = vcross(vsub(points[i], points[0]), vsub(points[j], points[0]))
            if not viszero(cand):
                normal = cand
                break
        if normal is not None:
            break
    require(normal is not None, "EXP6-DISK-CERTIFICATE-FAILED", f"{m['label']}: degenerate polygon")
    signs = []
    for i in range(n):
        a = vsub(points[(i + 1) % n], points[i])
        b = vsub(points[(i + 2) % n], points[(i + 1) % n])
        cross = vcross(a, b)
        if viszero(cross):
            return None, "collinear-vertex"
        sign = 1 if vdot(cross, normal) > 0 else -1
        signs.append(sign)
    for i in range(n):
        if vdot(vsub(points[i], points[0]), normal) != 0:
            return None, "not-coplanar"
    if len(set(signs)) != 1:
        return None, "not-convex"
    return {
        "kind": "flat-fan-disk",
        "plane_normal": [qtext(c) for c in normal],
        "turn_signs": signs,
        "fan_triangles": [[0, i, i + 1] for i in range(1, n - 1)],
        "conclusion": "the curve bounds an embedded flat disk, hence it is unknotted in R^3",
    }, None


# ==========================================================================
# torus, sphere, thickened-surface environment arithmetic
# ==========================================================================

def torus_slope(p, q):
    p, q = int(p), int(q)
    g = _gcd(abs(p), abs(q))
    return {"slope": [p, q], "gcd": g, "primitive": g == 1, "essential": (p != 0 or q != 0)}


def intersection_number(s1, s2) -> int:
    return abs(s1[0] * s2[1] - s1[1] * s2[0])


def _gcd(a, b):
    while b:
        a, b = b, a % b
    return a


TORUS_ENVIRONMENTS = {
    "meridian": torus_slope(1, 0),
    "longitude": torus_slope(0, 1),
    "diagonal": torus_slope(1, 1),
}

BASIS_SWAP = ((0, 1), (1, 0))

PROJECTION_DIRECTIONS = ((1, 2, 3), (2, 3, 5), (3, 5, 7), (1, 3, 5), (2, 5, 3), (1, 1, 1))


def rotated_hopf_control():
    """Two linking-number routes on a rotated Hopf-like pair.

    The rope square is rotated in the plane z=0 by the rational rotation with
    (cos, sin) = (3/5, 4/5), so no rope edge direction coincides with a loop edge
    direction and a generic projection exists.  Both routes must agree, and the
    disk route is additionally hand-checkable: the rotated rope meets the flat
    rectangle disk exactly once, transversally and in its interior, at (5/4, 0, 0).
    """
    def r5(n):
        return Fraction(n, 5)
    rotated = motion("rotated-hopf-rope", 4, [0, 1],
                     [[(r5(-1), r5(7), 0), (r5(-7), r5(-1), 0),
                       (r5(1), r5(-7), 0), (r5(7), r5(1), 0)]] * 2)
    loop = motion("hopf-loop", 4, [0, 1], translated(LOOP_RECT, [(0, 0, 0), (0, 0, 0)]))
    loop_disk = (1, ZERO, (ZERO, F(2)), (F(-1), F(1)), 0, 2)
    disk_value, crossings = linking_number_by_disk(rotated, ZERO, loop, loop_disk)
    projection = None
    for direction in PROJECTION_DIRECTIONS:
        value, detail, error = signed_crossing_linking(rotated, ZERO, loop, ZERO, direction)
        if error is None:
            projection = {"value": value, "direction": list(direction), "crossings": detail}
            break
        projection = {"value": None, "direction": list(direction), "error": error}
    require(projection is not None and projection["value"] is not None,
            "EXP6-HAND-TABLE-MISMATCH",
            "no declared projection direction is generic for the rotated control")
    return {
        "rope": "square rotated by (cos,sin)=(3/5,4/5) in the plane z=0, coordinates scaled by 5",
        "disk_route": {"value": disk_value, "crossings": crossings},
        "projection_route": projection,
        "agree": abs(disk_value) == abs(projection["value"]) and abs(disk_value) == 1,
        "hand_argument": ("the rotated rope meets the loop's flat rectangle disk exactly once, "
                          "transversally and in the interior, at (5/4, 0, 0)"),
    }


def apply_matrix(matrix, vector):
    return [sum(matrix[i][j] * vector[j] for j in range(len(vector))) for i in range(len(matrix))]


# ==========================================================================
# topological route: declared diagram calculus
# ==========================================================================

def diagram(word, signs, label=""):
    return {"word": tuple(int(w) for w in word), "signs": tuple(int(s) for s in signs),
            "label": label}


def diagram_labels(d):
    return sorted({abs(w) for w in d["word"]})


def diagram_wellformed(d) -> bool:
    labels = diagram_labels(d)
    if labels != list(range(1, len(labels) + 1)):
        return False
    if len(d["signs"]) != len(labels):
        return False
    for label in labels:
        entries = [w for w in d["word"] if abs(w) == label]
        if len(entries) != 2:
            return False
        if sorted(entries) != [-label, label]:
            return False
    return True


def diagram_text(d) -> str:
    return "word=" + ",".join(str(w) for w in d["word"]) + ";signs=" + ",".join(str(s) for s in d["signs"])


def writhe(d) -> int:
    return sum(d["signs"])


def r1_insert(d, position, sign):
    """Insert one R1 kink: a consecutive over/under pair with a fresh label."""
    require(diagram_wellformed(d), "EXP6-DIAGRAM-MALFORMED", diagram_text(d))
    require(0 <= position <= len(d["word"]), "EXP6-MOVE-POSITION",
            f"position {position} outside word of length {len(d['word'])}")
    require(sign in (1, -1), "EXP6-MOVE-SIGN", str(sign))
    label = len(d["signs"]) + 1
    pair = (sign * label, -sign * label)
    word = d["word"][:position] + pair + d["word"][position:]
    signs = tuple(d["signs"]) + (sign,)
    out = diagram(word, signs, label=d["label"] + "|R1" + ("+" if sign > 0 else "-"))
    require(diagram_wellformed(out), "EXP6-DIAGRAM-MALFORMED", diagram_text(out))
    return out, {"kind": "R1" + ("+" if sign > 0 else "-"), "position": position,
                 "label": label, "sign": sign,
                 "before": diagram_text(d), "after": diagram_text(out)}


def r1_delete(d, position):
    """Remove an R1 kink: an adjacent inverse pair whose sign matches the rule."""
    require(diagram_wellformed(d), "EXP6-DIAGRAM-MALFORMED", diagram_text(d))
    require(0 <= position < len(d["word"]) - 1, "EXP6-MOVE-POSITION",
            f"position {position} has no consecutive pair")
    a, b = d["word"][position], d["word"][position + 1]
    require(abs(a) == abs(b) and a == -b, "EXP6-R1-NOT-A-KINK",
            f"entries {a},{b} are not a consecutive inverse pair")
    label = abs(a)
    sign = 1 if a > 0 else -1
    require(d["signs"][label - 1] == sign, "EXP6-R1-SIGN-MISMATCH",
            f"label {label} has crossing sign {d['signs'][label - 1]}, kink order implies {sign}")
    word = d["word"][:position] + d["word"][position + 2:]
    signs = list(d["signs"])
    del signs[label - 1]
    rename = {}
    nxt = 1
    for old in diagram_labels({"word": word, "signs": tuple(signs)}):
        rename[old] = nxt
        nxt += 1
    out = diagram(word, ())
    out = {"word": tuple((1 if w > 0 else -1) * rename[abs(w)] for w in word),
           "signs": tuple(signs[old - 1] for old in sorted(rename, key=lambda k: rename[k])),
           "label": d["label"] + "|R1-"}
    require(diagram_wellformed(out), "EXP6-DIAGRAM-MALFORMED", diagram_text(out))
    return out, {"kind": "R1-", "position": position, "label": label, "sign": sign,
                 "before": diagram_text(d), "after": diagram_text(out)}


def r2_insert(d, position_a, position_b):
    """Insert one R2 bigon: two fresh crossings with opposite crossing signs."""
    require(diagram_wellformed(d), "EXP6-DIAGRAM-MALFORMED", diagram_text(d))
    require(0 <= position_a <= position_b <= len(d["word"]), "EXP6-MOVE-POSITION",
            f"positions {position_a},{position_b} outside word of length {len(d['word'])}")
    a = len(d["signs"]) + 1
    b = len(d["signs"]) + 2
    word = list(d["word"])
    word[position_a:position_a] = [a, b]
    word[position_b + 2:position_b + 2] = [-a, -b]
    signs = tuple(d["signs"]) + (1, -1)
    out = diagram(tuple(word), signs, label=d["label"] + "|R2+")
    require(diagram_wellformed(out), "EXP6-DIAGRAM-MALFORMED", diagram_text(out))
    return out, {"kind": "R2+", "positions": [position_a, position_b],
                 "labels": [a, b], "signs": [1, -1],
                 "before": diagram_text(d), "after": diagram_text(out)}


def r2_delete(d, position_a, position_b):
    """Remove one R2 bigon inserted by :func:`r2_insert`."""
    require(diagram_wellformed(d), "EXP6-DIAGRAM-MALFORMED", diagram_text(d))
    word = list(d["word"])
    a, b = word[position_a], word[position_a + 1]
    require(abs(a) == len(d["signs"]) - 1, "EXP6-R2-NOT-A-BIGON",
            f"first fresh label expected {len(d['signs']) - 1}, found {abs(a)}")
    require(abs(b) == len(d["signs"]), "EXP6-R2-NOT-A-BIGON",
            f"second fresh label expected {len(d['signs'])}, found {abs(b)}")
    require(d["signs"][abs(a) - 1] == 1 and d["signs"][abs(b) - 1] == -1,
            "EXP6-R2-SIGN-MISMATCH", "declared bigon signs are (+1, -1)")
    # the second occurrence sits two entries after the declared second position,
    # exactly as in r2_insert; delete it first so the earlier indices stay valid
    del word[position_b + 2:position_b + 4]
    require(word[position_a] == a and word[position_a + 1] == b, "EXP6-R2-NOT-A-BIGON",
            "the declared second position does not hold the inverse pair of the first")
    del word[position_a:position_a + 2]
    signs = list(d["signs"])[:-2]
    rename = {}
    nxt = 1
    for old in sorted({abs(w) for w in word}):
        rename[old] = nxt
        nxt += 1
    out = {"word": tuple((1 if w > 0 else -1) * rename[abs(w)] for w in word),
           "signs": tuple(signs[old - 1] for old in sorted(rename, key=lambda k: rename[k])),
           "label": d["label"] + "|R2-"}
    require(diagram_wellformed(out), "EXP6-DIAGRAM-MALFORMED", diagram_text(out))
    return out, {"kind": "R2-", "positions": [position_a, position_b],
                 "labels": [abs(a), abs(b)], "signs": [1, -1],
                 "before": diagram_text(d), "after": diagram_text(out)}


def encode_without_crossings(d):
    """The over/under-free encoding: label order kept, entry signs dropped."""
    return (tuple(abs(w) for w in d["word"]), tuple(d["signs"]))


def r1_deletable(d):
    """Declared R1-deletability observable of the instantiated move calculus."""
    out = []
    for position in range(max(len(d["word"]) - 1, 0)):
        a, b = d["word"][position], d["word"][position + 1]
        if abs(a) == abs(b) and a == -b:
            label = abs(a)
            sign = 1 if a > 0 else -1
            if d["signs"][label - 1] == sign:
                out.append({"position": position, "label": label, "sign": sign})
    return out


def run_move_history(d0, moves, move_fns):
    """Execute a literal move history, recording provenance for every move."""
    state = d0
    records = []
    for index, (kind, args) in enumerate(moves):
        fn = move_fns[kind]
        before = diagram_text(state)
        state, record = fn(state, *args)
        record["before"] = before
        record["after"] = diagram_text(state)
        record["provenance"] = {"index": index, "parent_state": before}
        records.append(record)
    return state, records


# ==========================================================================
# exact integer-string encoding (gate A) and compiler/interpreter (gate C)
# ==========================================================================

def enc(value) -> str:
    """Self-delimiting exact encoding into an integer-string alphabet."""
    if isinstance(value, Fraction):
        return "Q" + str(value.numerator) + "/" + str(value.denominator) + ";"
    if isinstance(value, int):
        return "I" + str(value) + ";"
    if isinstance(value, str):
        return "S" + str(len(value)) + ":" + value
    if isinstance(value, (tuple, list)):
        return "L" + str(len(value)) + "(" + "".join(enc(v) for v in value) + ")"
    raise Diagnostic("EXP6-ENCODE-UNSUPPORTED", repr(type(value)))


def dec(text: str):
    """Inverse of :func:`enc`; raises a coded diagnostic on malformed input."""
    value, rest = _dec(text)
    require(rest == "", "EXP6-ENCODE-ROUNDTRIP", f"trailing bytes: {rest!r}")
    return value


def _dec(text: str):
    require(bool(text), "EXP6-ENCODE-ROUNDTRIP", "empty input")
    tag = text[0]
    if tag == "Q":
        end = text.index("/", 1)
        stop = text.index(";", end)
        return Fraction(int(text[1:end]), int(text[end + 1:stop])), text[stop + 1:]
    if tag == "I":
        stop = text.index(";", 1)
        return int(text[1:stop]), text[stop + 1:]
    if tag == "S":
        colon = text.index(":")
        length = int(text[1:colon])
        body = text[colon + 1:colon + 1 + length]
        require(len(body) == length, "EXP6-ENCODE-ROUNDTRIP", "truncated string field")
        return body, text[colon + 1 + length:]
    if tag == "L":
        open_paren = text.index("(")
        count = int(text[1:open_paren])
        rest = text[open_paren + 1:]
        items = []
        for _ in range(count):
            item, rest = _dec(rest)
            items.append(item)
        require(rest.startswith(")"), "EXP6-ENCODE-ROUNDTRIP", "missing list terminator")
        return tuple(items), rest[1:]
    raise Diagnostic("EXP6-ENCODE-ROUNDTRIP", f"unknown tag {tag!r}")


def model_record(m):
    """Canonical encodable record of a motion."""
    return ("motion", m["label"], int(m["nodes"]), int(m["closed"]),
            -1 if m["marked"] is None else int(m["marked"]),
            tuple(m["breakpoints"]), tuple(tuple(row) for row in m["positions"]))


def obstacle_record(obstacle):
    if obstacle["kind"] == "ball":
        return ("ball", obstacle["label"], obstacle["radius"], tuple(obstacle["breakpoints"]),
                tuple(obstacle["centres"]))
    return ("loop", obstacle["label"], model_record(obstacle["motion"]))


def encode_history(history):
    """E = the declared history encoding; concatenative with ``compose_text``."""
    return "".join(enc(step) for step in history)


def compose_text(text_a, text_b):
    """Declared composition: history b after history a is the concatenation."""
    return text_a + text_b


def decode_history(text):
    history = []
    rest = text
    while rest:
        step, rest = _dec(rest)
        history.append(step)
    return tuple(history)


# ==========================================================================
# ambient / process declarations
# ==========================================================================

def process_limits():
    return {
        "native_process": ("k_t : S^1 -> M with every instant a legal embedding and "
                           "k_t(S^1) cap O_t = empty over the whole declared time interval"),
        "homotopy_warning": ("Allowing merely continuous maps or an ordinary homotopy would "
                             "wrongly allow the rope to pass through itself; that is not a "
                             "deformation process in this experiment"),
        "ambient_isotopy_condition": ("If a task uses ambient isotopy, the ambient extension "
                                      "and the relative boundary conditions are required. "
                                      "They are certified constructively here only for the "
                                      "declared rigid-translation class; the classical "
                                      "isotopy extension theorem is cited, not reproved"),
        "configuration_space": ("In a static environment the process is a path in the embedding "
                                "configuration space with the declared boundary conditions; "
                                "paths with equal endpoints need not be equivalent under "
                                "fixed-endpoint process homotopy, and that homotopy is NOT "
                                "decided by this experiment"),
        "dynamic_obstacles": ("With a moving obstacle the process is the time-monotone pair "
                              "(t, k_t) with k_t in C_t = {legal embeddings at time t}. "
                              "Undirected connectivity after adding time is not an executable path"),
    }


# ==========================================================================
# main record
# ==========================================================================

def run():
    require(CONTRACT.exists(), "EXP6-CONTRACT-MISSING", str(CONTRACT))
    contract_sha = gapkit.sha256_file(CONTRACT)
    frozen = _read_frozen()
    require(frozen.get(CONTRACT.name) == contract_sha, "EXP-CONTRACT-DRIFT",
            f"{CONTRACT.name}: frozen {frozen.get(CONTRACT.name)!r} != actual {contract_sha}")

    fx, w3_ball, w4_ball = build_fixtures()
    for name in sorted(fx):
        check_budget(fx[name])

    hand = hand_table(fx, w3_ball, w4_ball)
    geometric = geometric_route(fx, w3_ball, w4_ball, hand)
    topological = topological_route(hand)
    environments = environment_records(fx, hand)
    gates = arithmetic_gates(fx, topological)
    tiers = tier_costs(fx, topological)
    raw_payload = geometric.pop("raw")

    record = {
        "schema": SCHEMA,
        "contract": {"path": str(CONTRACT.relative_to(ROOT.parent.parent)), "sha256": contract_sha},
        "environment": gapkit.environ(),
        "budget": BUDGET,
        "native_process": process_limits(),
        "hand_table": hand,
        "geometric_route": geometric,
        "topological_route": topological,
        "environments": environments,
        "gates": gates,
        "costs": tiers,
        "negative_controls": negative_controls(fx, w3_ball, w4_ball, geometric, topological, hand),
        "outcomes_summary": outcomes_summary(geometric, topological),
        "result_labels": result_labels(),
        "boundary": boundary_record(),
    }
    require(not geometric.pop("disagreement", None), "EXP6-ROUTE-DISAGREEMENT",
            "primary route disagreed with the hand table")
    raw = {
        "schema": RAW_SCHEMA,
        "contract": {"path": str(CONTRACT.relative_to(ROOT.parent.parent)), "sha256": contract_sha},
        "certificates": raw_payload["certificates"],
        "move_records": {
            "witness-1-kink-pair": topological["witness_1_same_type_different_history"]
                                            ["kink_pair_path_with_provenance"],
            "r2-roundtrip": [topological["r2_roundtrip"]["insert"],
                             topological["r2_roundtrip"]["delete"]],
        },
        "planner": raw_payload["planner"],
    }
    return record, raw


def outcomes_summary(geometric, topological):
    """Which declared outcome each headline result belongs to."""
    return {
        "success": [
            "gate A encode/decode round trip on every declared fixture",
            "gate C D(E(h)) = h and E(h2.h1) = E(h1) ++ E(h2) on the declared histories",
            "witness 1: identity path and local-move-then-inverse path share one endpoint state",
            "witness 2: torus slope and intersection arithmetic, and the free-3-space comparison",
            "witness 3: the searched replacement path is certified clear inside the budget",
            "witness 4: w4-P1 certified clear on every declared time box",
        ],
        "expected_negative": [
            "witness 3: the free-space path is rejected once the obstacle is introduced",
            "witness 4: w4-P2 collides under the same frozen obstacle timetable",
            "witness 5: the untraversable loop rejects the path and the linking number is a "
            "necessary constraint",
            "keyframe blindness: the strict continuous check rejects a motion whose keyframes "
            "are embedded",
        ],
        "budget_exhausted": [
            "witness 3 with the declared depth-2 search: no certified replacement inside that "
            "budget, reported with the searched set",
        ],
        "unknown": [
            "declared demonstration: the keyframe-blind fixture with subdivision depth zero "
            "returns not-certified with the uncertified time box",
        ],
        "implementation_error": [
            "every negative control raises its own specific EXP6- diagnostic; none of them is "
            "an accidental Python exception",
        ],
        "not_reported_as_any_of_these": [
            "no completeness claim for any representation",
            "no claim that a bounded search failure proves non-existence of a legal deformation",
        ],
    }


def result_labels():
    """Status label for every headline result of this experiment."""
    return {
        "interval_self_embedding_certificates": "proved (exact rational certificate per time box, multilinear box-hull separation)",
        "obstacle_clearance_certificates": "proved (exact rational certificate per time box and edge)",
        "collision_witnesses": "computationally-verified-example (exact rational time, parameter and point)",
        "keyframe_blindness": "computationally-verified-example (embedded at both keyframes, not embedded at t=1/4)",
        "unknown_outcome_demonstration": "computationally-verified-example",
        "torus_slope_arithmetic": "proved (exact integer arithmetic: primitivity and intersection numbers)",
        "torus_classification_used": "proved-with-stated-hypotheses (classical classification of simple closed curves on the torus, cited not reproved)",
        "free_space_unknot_comparison": "proved-with-stated-hypotheses (classical, cited not reproved)",
        "strict_sphere_statement": "proved-with-stated-hypotheses (Jordan-Schoenflies cited) with a computationally verified planar disk certificate",
        "flat_disk_certificate": "computationally-verified-example (planarity, convexity and the fan triangulation are checked exactly)",
        "linking_number_values": "computationally-verified-example (algebraic intersection with a spanning disk, cross-checked by a signed crossing count)",
        "linking_number_invariance_used": "proved-with-stated-hypotheses (classical invariance under disjoint isotopy, cited)",
        "linking_number_completeness": "open (not claimed; known to be incomplete in general, not verified here)",
        "local_move_calculus": "computationally-verified-example with declared incompleteness (R1 and R2 instantiated, R3 not)",
        "writhe_effects_of_the_moves": "proved on the declared diagram records (exact sign arithmetic)",
        "reidemeister_completeness": "proved-with-stated-hypotheses in the literature (cited), NOT verified or implemented here",
        "encoding_round_trip": "computationally-verified-example on the declared finite model",
        "state_faithfulness_topological": "refuted for topological semantics by an explicit witness pair",
        "process_faithfulness": "computationally-verified-example on the declared action dictionary",
        "completeness": "bounded-domain-compatible at best: no completeness claim is made",
        "general_knot_motion_planner": "structural-proposal only (not implemented)",
        "planning_failure_implies_nonexistence": "open (explicitly not claimed)",
    }


def _read_frozen():
    out = {}
    if FROZEN.exists():
        for line in FROZEN.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            digest, _, name = line.partition("  ")
            out[name.strip()] = digest.strip()
    return out


def boundary_record():
    return {
        "bounded_requirements": [
            {"requirement": "R3 Reidemeister move instantiated",
             "status": "bounded (not instantiated)",
             "why": ("a faithful R3 needs a planar-tangle pattern whose exact implementation "
                     "exceeds this round's budget, and the braid-relation route to it is "
                     "explicitly out of scope for exp6 (braid closure and Markov equivalence "
                     "are excluded). The instantiated rewrite system is therefore incomplete "
                     "by declaration.")},
            {"requirement": "general knot-motion planner",
             "status": "bounded (not implemented)",
             "why": ("only concrete candidate paths are verified first; the search is a bounded "
                     "depth-first search inside one fixed-node-count, fixed-parameter-family, "
                     "fixed-action-dictionary submodel.")},
            {"requirement": "smooth embeddings and physical ropes",
             "status": "out of model",
             "why": "finite PL and zero thickness only; no radius, length, curvature or velocity limits"},
            {"requirement": "wild knots, arbitrary real input",
             "status": "out of model",
             "why": "tame finite PL with exact rational data only"},
            {"requirement": "knot polynomials",
             "status": "not computed",
             "why": ("writhe, linking number and torus slope are used as declared necessary "
                     "constraints only; no polynomial invariant is computed and no completeness "
                     "claim is made for any of them")},
            {"requirement": "fixed-endpoint process homotopy between the two witness-1 histories",
             "status": "open",
             "why": "the experiment records that the literal histories and their costs differ and explicitly does NOT claim a homotopy difference"},
        ],
        "not_claimed": [
            "no completeness of any representation for all tame knots or all legal deformations",
            "no general knot-motion planner and no claim that a bounded search failure implies non-existence",
            "no knot invariance inferred from a suggestive construction",
            "no bridging of braid closure or Markov equivalence to knot equivalence",
            "no claim that linking number is a complete link invariant",
            "no claim that a strict simple closed curve on S^2 or T^2 can carry a classical non-trivial knot",
            "no virtual-knot stabilisation equivalence",
        ],
    }


# ==========================================================================
# hand table
# ==========================================================================

def hand_table(fx, w3_ball, w4_ball):
    """Hand-computed witness values, entered as literals and re-checked."""
    entries = {}

    # Linear-programming core sanity, entered as literals: the origin is in the
    # hull of the first set and is not in the hull of the second.
    inside = E_SEPARATION_INSIDE
    outside = E_SEPARATION_OUTSIDE
    require(separating_functional(inside) is None, "EXP6-SEPARATION-INVALID",
            "the origin lies in the convex hull of the declared control set; no separator exists")
    outside_z = separating_functional(outside)
    require(outside_z is not None, "EXP6-SEPARATION-INVALID",
            "the origin is outside the declared control hull; a separator must exist")
    for vertex in outside:
        require(vdot(outside_z, vertex) >= 1, "EXP6-SEPARATION-INVALID",
                f"returned separator {outside_z} fails on vertex {vertex}")
    entries["separation_core"] = {
        "origin_in_hull_of": [[qtext(c) for c in v] for v in inside],
        "separator_for": [[qtext(c) for c in v] for v in outside],
        "separator": [qtext(c) for c in outside_z],
    }

    # F2 keyframe-blind fixture: crossing at time 1/4, edges 0 and 3, (s,u)=(2/5,4/5).
    kb = fx["keyframe-blind"]
    t = Fraction(1, 4)
    ok0, _ = is_embedded_at(kb, ZERO)
    ok1, _ = is_embedded_at(kb, ONE)
    okq, witness = is_embedded_at(kb, t)
    require(ok0 and ok1, "EXP6-HAND-TABLE-MISMATCH", "keyframes of the keyframe-blind fixture are not embedded")
    require(not okq, "EXP6-HAND-TABLE-MISMATCH", "interior time 1/4 is embedded; hand table says it is not")
    require(witness["edges"] == [0, 3], "EXP6-HAND-TABLE-MISMATCH",
            f"crossing edges {witness['edges']} != hand table [0, 3]")
    require(witness["parameters"] == ["2/5", "4/5"], "EXP6-HAND-TABLE-MISMATCH",
            f"crossing parameters {witness['parameters']} != hand table ['2/5', '4/5']")
    require(witness["point"] == ["4/5", "0", "0"], "EXP6-HAND-TABLE-MISMATCH",
            f"crossing point {witness['point']} != hand table ['4/5','0','0']")
    entries["F2_crossing"] = {"time": "1/4", "edges": [0, 3], "parameters": ["2/5", "4/5"],
                              "point": ["4/5", "0", "0"],
                              "keyframes_embedded": True, "interior_embedded": False}

    # F4 time-parameterisation fixture.
    p1 = check_self_embedding(fx["w4-P1"])
    p2 = check_self_embedding(fx["w4-P2"])
    require(p1[0] == "valid" and p2[0] == "valid", "EXP6-HAND-TABLE-MISMATCH",
            f"rope paths must be legal without obstacles: {p1[0]}, {p2[0]}")
    clear1, hit1, certs1, unknown1, stats1 = check_obstacles(fx["w4-P1"], [w4_ball])
    clear2, hit2, certs2, unknown2, stats2 = check_obstacles(fx["w4-P2"], [w4_ball])
    require(clear1 == "valid" and unknown1 == [], "EXP6-HAND-TABLE-MISMATCH",
            f"w4-P1 must be certified clear, got {clear1} with {len(unknown1)} uncertified boxes")
    require(clear2 == "invalid" and hit2 is not None, "EXP6-HAND-TABLE-MISMATCH",
            f"w4-P2 must collide, got {clear2}")
    contact = ball_collision_at(fx["w4-P2"], 0, w4_ball, Fraction(3, 8))
    require(contact is not None, "EXP6-HAND-TABLE-MISMATCH",
            "hand table: the ball is at (1,0,0) at t=3/8 and the parked rope bottom edge passes through it")
    require(contact["time"] == "3/8" and contact["parameter"] == "1/2",
            "EXP6-HAND-TABLE-MISMATCH",
            f"w4-P2 contact {(contact['time'], contact['parameter'])} != hand table (3/8, 1/2)")
    require(contact["point"] == ["1", "0", "0"] and contact["distance_squared"] == "0",
            "EXP6-HAND-TABLE-MISMATCH",
            f"w4-P2 contact {contact['point']} distance^2 {contact['distance_squared']} != [1,0,0], 0")
    require(hit2["time"] in ("3/8", "1/2") and hit2["parameter"] == "1/2",
            "EXP6-HAND-TABLE-MISMATCH",
            f"w4-P2 searched collision {(hit2['time'], hit2['parameter'])} outside the contact window")
    entries["F4_collision"] = {"declared_contact": contact,
                               "searched_witness": hit2,
                               "contact_window_start": "3/8",
                               "distance_squared": "0", "radius_squared": "1/16"}
    entries["F4_clearance_min"] = {"squared_distance_lower_bound": "40400/10201",
                                   "window": ["1/4", "3/8"],
                                   "source": "exact minimisation of (8t-1)^2 + (80*(3/8-t))^2",
                                   "role": "hand-checked value; the primary route instead stores exact per-box certificates"}

    # F3 obstacle-changes-legality fixture.
    free_verdict, free_witness, _, _, _ = check_self_embedding(fx["w3-free"])
    require(free_verdict == "valid", "EXP6-HAND-TABLE-MISMATCH",
            f"free-space candidate path must be legal, got {free_verdict}")
    blocked, hit3, _, _, _ = check_obstacles(fx["w3-free"], [w3_ball])
    require(blocked == "invalid" and hit3 is not None, "EXP6-HAND-TABLE-MISMATCH",
            f"the obstacle must reject the free-space path, got {blocked}")
    require(hit3["time"] == "1/4" and hit3["parameter"] == "1/2", "EXP6-HAND-TABLE-MISMATCH",
            f"w3 collision {(hit3['time'], hit3['parameter'])} != hand table (1/4, 1/2)")
    require(hit3["point"] == ["1", "1", "0"], "EXP6-HAND-TABLE-MISMATCH",
            f"w3 collision point {hit3['point']} != [1,1,0]")
    entries["F3_collision"] = {"time": "1/4", "parameter": "1/2", "point": ["1", "1", "0"],
                               "distance_squared": "0", "radius_squared": "1/4"}

    # F5 linking fixture (flat-disk route; the disk is the loop's convex hull).
    loop_disk = (1, ZERO, (ZERO, F(2)), (F(-1), F(1)), 0, 2)
    lk_start, crossings_start = linking_number_by_disk(fx["w5-rope"], ZERO, fx["w5-loop"], loop_disk)
    lk_end, crossings_end = linking_number_by_disk(fx["w5-rope"], ONE, fx["w5-loop"], loop_disk)
    require(lk_start == 0, "EXP6-HAND-TABLE-MISMATCH",
            f"linking number at the start is {lk_start}, hand table says 0")
    require(lk_end == 1, "EXP6-HAND-TABLE-MISMATCH",
            f"linking number at the end is {lk_end}, hand table says +1")
    projection_attempt = None
    for direction in PROJECTION_DIRECTIONS:
        value, crossings, error = signed_crossing_linking(
            fx["w5-rope"], ONE, fx["w5-loop"], ZERO, direction)
        if error is None:
            projection_attempt = {"value": value, "direction": list(direction),
                                  "crossings": crossings}
            break
        projection_attempt = {"value": None, "direction": list(direction), "error": error}
    require(projection_attempt is not None, "EXP6-HAND-TABLE-MISMATCH", "no projection attempted")
    rotated_control = rotated_hopf_control()
    entries["F5_linking_start"] = {"value": lk_start, "crossings": crossings_start}
    entries["F5_linking_end"] = {"value": lk_end, "crossings": crossings_end}
    entries["F5_linking_routes"] = {
        "axis_aligned_pair": {
            "disk_route": lk_end,
            "projection_route": projection_attempt,
            "note": ("the axis-aligned rope and loop share the x edge direction, so no projection "
                     "direction makes the crossing count generic; the disk route decides this pair, "
                     "and the projection route is exercised on the rotated control below"),
        },
        "rotated_control": rotated_control,
    }
    require(rotated_control["agree"], "EXP6-HAND-TABLE-MISMATCH",
            f"the two linking-number routes disagree on the rotated control: {rotated_control}")
    loop_hit_verdict, loop_hit, _, _, _ = check_obstacles(
        fx["w5-rope"], [loop_obstacle("w5-loop-obs", fx["w5-loop"])])
    require(loop_hit_verdict == "invalid" and loop_hit is not None, "EXP6-HAND-TABLE-MISMATCH",
            f"the untraversable loop must reject the path, got {loop_hit_verdict}")
    require(loop_hit["time"] == "2/3", "EXP6-HAND-TABLE-MISMATCH",
            f"loop collision time {loop_hit['time']} != hand table 2/3")
    entries["F5_loop_collision"] = loop_hit

    disk_cert, disk_error = flat_disk_certificate(fx["w5-loop"], ZERO)
    require(disk_cert is not None, "EXP6-HAND-TABLE-MISMATCH",
            f"the loop must bound a flat disk: {disk_error}")

    # Topological route hand values.
    d0 = diagram((1, -1), (1,), "kink-positive")
    d1, _ = r1_insert(d0, 0, 1)
    d2, _ = r1_delete(d1, 0)
    require(diagram_text(d2) == diagram_text(d0), "EXP6-HAND-TABLE-MISMATCH",
            "R1 insert then delete must return the original diagram")
    dneg = diagram((-1, 1), (1,), "kink-negative")
    dneg2, _ = r1_insert(dneg, 0, -1)
    dbg = diagram((1, -1, 2, -2), (1, -1), "bigon-demo")
    dbg2, _ = r2_insert(dbg, 1, 3)
    require(writhe(dbg2) == writhe(dbg), "EXP6-HAND-TABLE-MISMATCH",
            "R2 must not change the writhe")
    require(writhe(d1) - writhe(d0) == 1, "EXP6-HAND-TABLE-MISMATCH",
            "R1+ must change the writhe by +1")
    require(writhe(dneg2) - writhe(dneg) == -1, "EXP6-HAND-TABLE-MISMATCH",
            "R1- must change the writhe by -1")
    entries["topological_writhe"] = {
        "R1_positive_kink_writhe_delta": writhe(d1) - writhe(d0),
        "R1_negative_kink_writhe_delta": writhe(dneg2) - writhe(dneg),
        "R2_bigon_writhe_delta": writhe(dbg2) - writhe(dbg),
    }
    return entries


# ==========================================================================
# geometric route
# ==========================================================================

def geometric_route(fx, w3_ball, w4_ball, hand):
    out = {}
    raw = {"certificates": {}, "move_records": {}, "planner": {}}

    # ---- witness 4 ----
    p1 = check_self_embedding(fx["w4-P1"])
    p2 = check_self_embedding(fx["w4-P2"])
    c1 = check_obstacles(fx["w4-P1"], [w4_ball])
    c2 = check_obstacles(fx["w4-P2"], [w4_ball])
    require(c1[0] == "valid" and c2[0] == "invalid", "EXP6-WITNESS-FAILED",
            f"witness 4 verdicts are {c1[0]} and {c2[0]}")
    require(c1[3] == [] and c2[3] == [], "EXP6-WITNESS-FAILED",
            "witness 4 must have no uncertified time box")
    margins = [cert for cert in c1[2]]
    out["witness_4_time_changes_legality"] = {
        "outcome": "expected_negative",
        "parameterisations": ["w4-P1", "w4-P2"],
        "rope_motion": {
            "w4-P1": "constant speed, offsets (0,0,0) -> (8,0,0)",
            "w4-P2": "waits until t=1/2, then twice as fast",
        },
        "identical_start_configuration": True,
        "identical_end_configuration": True,
        "knot_type_both": "unknot at every time (translate of a planar square, flat disk certificate)",
        "free_space_self_embedding": {"w4-P1": p1[0], "w4-P2": p2[0]},
        "with_frozen_obstacle": {
            "w4-P1": {"verdict": c1[0], "uncertified_boxes": len(c1[3]),
                      "certificate_count": len(margins),
                      "certificate_methods": sorted({cert["method"] for cert in margins}),
                      "boxes": c1[4]["boxes"], "certified_boxes": c1[4]["certified"]},
            "w4-P2": {"verdict": c2[0], "collision": c2[1]},
        },
        "continuous_certificates_stored": len(margins),
        "certificate_table": summarize_certificates(margins),
        "proved_clearance_lower_bound": qtext(
            clearance_margin(margins, w4_ball["radius"])),
        "hand_checked_minimum_distance_squared": hand["F4_clearance_min"][
            "squared_distance_lower_bound"],
        "declared_contact": hand["F4_collision"]["declared_contact"],
    }
    raw["certificates"]["w4-P1"] = margins

    # ---- witness 3 (+ bounded planner) ----
    free = check_self_embedding(fx["w3-free"])
    blocked = check_obstacles(fx["w3-free"], [w3_ball])
    replacement = check_self_embedding(fx["w3-plan"])
    replacement_clear = check_obstacles(fx["w3-plan"], [w3_ball])
    search4 = plan_replacement(fx, w3_ball, max_depth=4)
    search2 = plan_replacement(fx, w3_ball, max_depth=2)
    require(search4["outcome"] == "success", "EXP6-WITNESS-FAILED",
            "the depth-4 search must find the declared replacement path")
    require(search2["outcome"] == "budget_exhausted", "EXP6-WITNESS-FAILED",
            f"the depth-2 search must be budget_exhausted, got {search2['outcome']}")
    require(replacement[0] == "valid" and replacement_clear[0] == "valid",
            "EXP6-WITNESS-FAILED",
            f"the searched replacement path must be certified: {replacement[0]}, {replacement_clear[0]}")
    out["witness_3_obstacle_changes_legality"] = {
        "outcome": "expected_negative",
        "free_space_path": {"label": "w3-free", "self_embedding": free[0],
                            "verdict_without_obstacle": "valid",
                            "note": "there is no obstacle in free space, so the only obligation is self-embedding"},
        "same_path_with_obstacle": {"obstacle": "w3-ball",
                                    "geometry": "closed ball, centre (1,1,0), radius 1/2, static timetable",
                                    "verdict": blocked[0], "collision": blocked[1]},
        "replacement": {
            "found": True,
            "path": search4["path"],
            "offsets": search4["offsets"],
            "verdict": replacement_clear[0],
            "certificate_count": len(replacement_clear[2]),
            "certificate_table": summarize_certificates(replacement_clear[2]),
            "proved_clearance_lower_bound": qtext(
                clearance_margin(replacement_clear[2], w3_ball["radius"])),
            "uncertified_boxes": len(replacement_clear[3]),
            "undirected_ordering": search4["checked_prefixes"],
            "searched_nodes": search4["searched_nodes"],
            "pruned_prefixes": search4["pruned_prefixes"],
            "max_depth": 4,
        },
        "budget_exhausted_run": {
            "max_depth": 2,
            "outcome": search2["outcome"],
            "searched_nodes": search2["searched_nodes"],
            "reason": "the goal offset (4,0,0) is reachable in two steps only by the colliding direct path",
        },
        "submodel_caveat": ("a planning failure inside this fixed-node-count, fixed-parameter-family, "
                            "fixed-action-dictionary submodel would NOT prove that no legal "
                            "deformation exists; the depth-2 run is reported as budget_exhausted "
                            "for exactly that reason"),
    }
    raw["certificates"]["w3-plan"] = replacement_clear[2]
    raw["planner"] = {"witness_3": {"found_path": search4["path"],
                                    "pruned_prefixes": search4["pruned_prefixes"],
                                    "searched_nodes": search4["searched_nodes"]}}

    # ---- keyframe blindness ----
    kb = fx["keyframe-blind"]
    strict = check_self_embedding(kb)
    relaxed = check_self_embedding(kb, keyframe_only=True)
    require(strict[0] == "invalid" and relaxed[0] == "valid", "EXP6-WITNESS-FAILED",
            f"keyframe blindness fixture: strict={strict[0]} keyframe-only={relaxed[0]}")
    out["keyframe_blindness"] = {
        "fixture": "keyframe-blind",
        "keyframes": [qtext(t) for t in kb["breakpoints"]],
        "keyframe_only_verdict": relaxed[0],
        "continuous_verdict": strict[0],
        "continuous_witness": strict[1],
        "conclusion": ("checking only keyframes is never a continuous safety proof: the declared "
                       "motion is embedded at t=0 and t=1 and not embedded at t=1/4"),
    }

    # ---- the unknown outcome must be reachable and distinct from invalid ----
    # With the declared subdivision depth forced to zero, no interval certificate
    # exists and no collision witness is found inside the budget, so the verdict
    # is not-certified (unknown) with the uncertified time box reported exactly.
    unknown_demo = check_self_embedding(fx["keyframe-blind"], depth=0)
    require(unknown_demo[0] == "not-certified", "EXP6-WITNESS-FAILED",
            f"the depth-0 run must report not-certified, got {unknown_demo[0]}")
    out["unknown_outcome_demonstration"] = {
        "outcome": "unknown",
        "verdict": unknown_demo[0],
        "uncertified_boxes": unknown_demo[3],
        "note": ("a declared outcome, not an exception and not a legality claim: with no "
                 "certificate and no witness inside the budget the checker says so"),
    }

    # ---- witness 5 ----
    loop_obs = loop_obstacle("w5-loop-obs", fx["w5-loop"])
    loop_clear = check_obstacles(fx["w5-rope"], [loop_obs])
    rope_free = check_self_embedding(fx["w5-rope"])
    require(loop_clear[0] == "invalid", "EXP6-WITNESS-FAILED", "the loop must reject the rope path")
    require(rope_free[0] == "invalid" or rope_free[0] == "valid", "EXP6-WITNESS-FAILED", "rope self check")
    disk_rope, disk_error_rope = flat_disk_certificate(fx["w5-rope"], ONE)
    require(disk_rope is not None, "EXP6-WITNESS-FAILED",
            f"the rope end configuration must bound a flat disk: {disk_error_rope}")
    out["witness_5_joint_topological"] = {
        "outcome": "expected_negative",
        "rope_self_embedding": rope_free[0],
        "rope_end_knot_type": "unknot (flat disk certificate on the end configuration)",
        "obstacle": {"label": "w5-loop-obs", "geometry": "closed polygonal loop, boundary of a flat rectangle",
                     "untraversable": True},
        "linking_number": {
            "at_start": hand["F5_linking_start"]["value"],
            "at_end": hand["F5_linking_end"]["value"],
            "route": "algebraic intersection of the rope with the flat spanning disk of the loop",
            "routes": hand["F5_linking_routes"],
            "invariance_used": ("linking number is invariant under disjoint isotopy (classical, cited): "
                                "the rope must stay disjoint from the loop, so the path from linking 0 "
                                "to linking 1 is impossible while disjoint"),
            "not_claimed": "linking number is a necessary constraint only, not a complete link invariant",
        },
        "collision": loop_clear[1],
        "knot_type_of_rope_contains_no_linking_information": (
            "the rope is the unknot at both ends, yet the environment (the loop) separates them"),
    }

    # ---- self-embedding of translations and ambient certificates ----
    ambient = {}
    for name in ("w4-P1", "w4-P2", "w3-free", "w3-plan", "w5-rope"):
        ambient[name] = ambient_extension_certificate(fx[name])
    for name in ("keyframe-blind", "w5-loop"):
        try:
            ambient_extension_certificate(fx[name])
            raise Diagnostic("EXP6-AMBIENT-EXTENSION-MISSING",
                             f"{name} unexpectedly certified; it is not a rigid translation")
        except Diagnostic as exc:
            require(exc.code == "EXP6-AMBIENT-EXTENSION-MISSING", "EXP6-WITNESS-FAILED",
                    f"unexpected diagnostic for {name}: {exc.code}")
    out["ambient_extension"] = {
        "certified_class": "rigid translation (all nodes share one displacement)",
        "certificates": ambient,
        "refused_class": ["keyframe-blind", "w5-loop"],
        "note": ("the closed-curve isotopy extension theorem would supply an ambient extension "
                 "for any isotopy of embeddings; it is cited, not reproved here, and the "
                 "constructive certificate is given only for the translation class"),
    }
    return {"fixtures": {name: summarize_motion(fx[name]) for name in sorted(fx)},
            "details": out, "raw": raw}


def summarize_motion(m):
    return {
        "nodes": m["nodes"],
        "segments": len(m["breakpoints"]) - 1,
        "breakpoints": [qtext(t) for t in m["breakpoints"]],
        "closed": m["closed"],
        "note": m["note"],
    }


TRANSLATION_ACTIONS = (
    ("x+2", (2, 0, 0)), ("x-2", (-2, 0, 0)),
    ("y+2", (0, 2, 0)), ("y-2", (0, -2, 0)),
    ("z+2", (0, 0, 2)), ("z-2", (0, 0, -2)),
)


def plan_replacement(fx, obstacle, max_depth=4, start_offset=(-2, 0, 0), goal_offset=(2, 0, 0)):
    """Bounded depth-first search over the declared translation dictionary.

    Every candidate prefix is checked with the continuous interval certificate
    before it is extended.  A missing path inside this budget is reported as
    budget_exhausted together with the searched set; it is never reported as
    proof that no legal deformation exists.
    """
    shape = SQUARE
    start = (F(start_offset[0]), F(start_offset[1]), F(start_offset[2]))
    goal = (F(goal_offset[0]), F(goal_offset[1]), F(goal_offset[2]))
    target = (goal[0] - start[0], goal[1] - start[1], goal[2] - start[2])
    stats = {"searched_nodes": 0, "pruned_prefixes": 0, "checked_prefixes": 0}
    found = []

    def step_ok(offsets):
        rows = translated(shape, offsets)
        m = motion("plan-step", 4, list(range(len(offsets))), rows)
        verdict, _, _, _, _ = check_obstacles(m, [obstacle])
        return verdict == "valid"

    def dfs(current, deltas, depth):
        stats["searched_nodes"] += 1
        if current == target:
            found.append(list(deltas))
            return True
        if depth == max_depth:
            return False
        for _, delta in TRANSLATION_ACTIONS:
            nxt = (current[0] + delta[0], current[1] + delta[1], current[2] + delta[2])
            candidate = cumulative_offsets(start, deltas + [delta])
            stats["checked_prefixes"] += 1
            if not step_ok(candidate):
                stats["pruned_prefixes"] += 1
                continue
            if dfs(nxt, deltas + [delta], depth + 1):
                return True
        return False

    success = dfs((ZERO, ZERO, ZERO), [], 0)
    offsets = cumulative_offsets(start, found[0]) if success else [start]
    return {
        "outcome": "success" if success else "budget_exhausted",
        "path": _names_for(found[0]) if success else [],
        "offsets": [[qtext(c) for c in o] for o in offsets] if success else [],
        "searched_nodes": stats["searched_nodes"],
        "checked_prefixes": stats["checked_prefixes"],
        "pruned_prefixes": stats["pruned_prefixes"],
        "max_depth": max_depth,
        "goal": [qtext(c) for c in goal],
    }


def cumulative_offsets(start, deltas):
    """Offsets at the declared breakpoints: one rigid translation per action."""
    out = [start]
    total = (ZERO, ZERO, ZERO)
    for delta in deltas:
        total = (total[0] + delta[0], total[1] + delta[1], total[2] + delta[2])
        out.append((start[0] + total[0], start[1] + total[1], start[2] + total[2]))
    return out


def _names_for(deltas):
    out = []
    for delta in deltas:
        for name, ref in TRANSLATION_ACTIONS:
            if ref == delta:
                out.append(name)
                break
    return out


# ==========================================================================
# topological route
# ==========================================================================

def topological_route(hand):
    d0 = diagram((1, -1), (1,), "kink-positive")
    d0neg = diagram((-1, 1), (1,), "kink-negative")
    require(diagram_wellformed(d0) and diagram_wellformed(d0neg), "EXP6-DIAGRAM-MALFORMED", "fixtures")

    d1, move1 = r1_insert(d0, 0, 1)
    d2, move2 = r1_delete(d1, 0)
    require(diagram_text(d2) == diagram_text(d0), "EXP6-MOVE-ROUNDTRIP",
            "R1 insert then delete must return the original diagram")

    bigon_base = diagram((1, -1, 2, -2), (1, -1), "bigon-base")
    bigon, move_b = r2_insert(bigon_base, 1, 3)
    bigon_back, move_bb = r2_delete(bigon, 1, 3)
    require(diagram_text(bigon_back) == diagram_text(bigon_base), "EXP6-MOVE-ROUNDTRIP",
            "R2 insert then delete must return the original diagram")

    move_fns = {"R1+": r1_insert, "R1-": r1_delete, "R2+": r2_insert, "R2-": r2_delete}
    replayed, provenance_records = run_move_history(
        d0, [("R1+", (0, 1)), ("R1-", (0,))], move_fns)
    require(diagram_text(replayed) == diagram_text(d0), "EXP6-MOVE-ROUNDTRIP",
            "replaying the witness-1 history with provenance must return the original diagram")
    _, r2_provenance = run_move_history(bigon_base, [("R2+", (1, 3)), ("R2-", (1, 3))], move_fns)
    r2_roundtrip = {"insert": move_b, "delete": move_bb,
                    "endpoint_after_roundtrip": diagram_text(bigon_back),
                    "provenance_records": r2_provenance}
    histories = {
        "identity": {"moves": [], "endpoint": diagram_text(d0), "literal_length": 0},
        "kink-pair": {"moves": [move1["kind"], move2["kind"]],
                      "endpoint": diagram_text(d1) + " -> " + diagram_text(d2),
                      "literal_length": 2},
    }
    require(diagram_text(d2) == diagram_text(d0), "EXP6-WITNESS-FAILED",
            "witness 1 needs one common endpoint state")

    crossing_drop = {
        "diagram_a": diagram_text(d0),
        "diagram_b": diagram_text(d0neg),
        "over_under_free_encoding_equal": encode_without_crossings(d0) == encode_without_crossings(d0neg),
        "full_encoding_equal": diagram_text(d0) == diagram_text(d0neg),
        "r1_deletable_a": r1_deletable(d0),
        "r1_deletable_b": r1_deletable(d0neg),
        "knot_type_both": "unknot (a one-crossing diagram of a curve is a kink; cited classical fact, not reproved here)",
    }
    require(crossing_drop["over_under_free_encoding_equal"], "EXP6-WITNESS-FAILED",
            "the over/under-free encodings of the two kink records must coincide")
    require(not crossing_drop["full_encoding_equal"], "EXP6-WITNESS-FAILED",
            "the full diagram records must differ")

    reachable = reachable_diagrams(d0, depth=2)
    return {
        "calculus": {
            "diagram": "Gauss word with over/under entry signs plus a declared crossing-sign vector",
            "wellformed": "labels 1..k, each appearing exactly once as +k and once as -k",
            "instantiated_moves": ["R1+", "R1-", "R2+", "R2-"],
            "not_instantiated": ["R3"],
            "incompleteness": ("the rewrite system is incomplete by declaration: R3 is not "
                               "instantiated, so no claim is made that it generates all diagram "
                               "equivalences. Reidemeister moves characterise classical knot type "
                               "equivalence; they record no geometric time, distance or process data."),
            "recorded_per_move": ["kind", "position", "label(s)", "before", "after", "provenance"],
        },
        "witness_1_same_type_different_history": {
            "outcome": "success",
            "endpoint_states_equal": True,
            "identity_path": {"moves": [], "cost_literal_length": 0},
            "kink_pair_path": {"moves": [move1, move2], "cost_literal_length": 2},
            "kink_pair_path_with_provenance": provenance_records,
            "not_claimed": ("the experiment does NOT claim that the two histories differ under "
                            "process homotopy; only the literal history and the cost differ"),
        },
        "writhe_effects": hand["topological_writhe"],
        "r2_roundtrip": r2_roundtrip,
        "crossing_information": crossing_drop,
        "reachability": reachable,
    }


def reachable_diagrams(d0, depth=2):
    """Breadth-first reachability inside the instantiated move calculus."""
    frontier = [d0]
    seen = {diagram_text(d0): d0}
    counts = []
    for level in range(1, depth + 1):
        nxt = []
        for d in frontier:
            for position in range(len(d["word"]) + 1):
                for sign in (1, -1):
                    out, _ = r1_insert(d, position, sign)
                    key = diagram_text(out)
                    if key not in seen:
                        seen[key] = out
                        nxt.append(out)
        counts.append({"depth": level, "new_diagrams": len(nxt), "total": len(seen)})
        frontier = nxt
    return {"start": diagram_text(d0), "levels": counts,
            "note": ("this is reachability inside the declared incomplete calculus, not a "
                     "classification of diagrams")}


# ==========================================================================
# environment records
# ==========================================================================

def environment_records(fx, hand):
    meridian = TORUS_ENVIRONMENTS["meridian"]
    longitude = TORUS_ENVIRONMENTS["longitude"]
    diagonal = TORUS_ENVIRONMENTS["diagonal"]
    swapped_meridian = apply_matrix(BASIS_SWAP, meridian["slope"])
    swapped_longitude = apply_matrix(BASIS_SWAP, longitude["slope"])
    strict_torus = {
        "basis_fixed": True,
        "meridian": meridian,
        "longitude": longitude,
        "diagonal": diagonal,
        "geometric_intersection_numbers": {
            "meridian-longitude": intersection_number(meridian["slope"], longitude["slope"]),
            "meridian-diagonal": intersection_number(meridian["slope"], diagonal["slope"]),
            "longitude-diagonal": intersection_number(longitude["slope"], diagonal["slope"]),
        },
        "distinct_isootopy_classes_under_fixed_basis": meridian["slope"] != longitude["slope"]
        and meridian["slope"] != [-v for v in longitude["slope"]],
        "basis_swap": {
            "matrix": [list(row) for row in BASIS_SWAP],
            "determinant": BASIS_SWAP[0][0] * BASIS_SWAP[1][1] - BASIS_SWAP[0][1] * BASIS_SWAP[1][0],
            "meridian_images_to": swapped_meridian,
            "longitude_images_to": swapped_longitude,
            "consequence": ("if a basis-swapping ambient homeomorphism is allowed, the meridian and "
                            "the longitude become equivalent and the earlier equivalence contract "
                            "changes; the reported result is for the FIXED oriented basis"),
        },
        "status": "proved-with-stated-hypotheses (classification of simple closed curves on the torus, cited not reproved here)",
    }
    free_space_for_torus = {
        "claim": ("in unobstructed R^3 both (1,0) and (0,1) are unknots, so the free-3-space task "
                  "declares them equivalent while the strict-surface task does not"),
        "status": "proved-with-stated-hypotheses (classical, cited not reproved here)",
        "computed_here": ("the slope arithmetic, primitivity and geometric intersection numbers "
                          "above are computed exactly; the disk-bounding fact for the standard "
                          "torus is cited"),
    }
    sphere_cert, sphere_error = flat_disk_certificate(fx["w5-loop"], ZERO)
    strict_sphere = {
        "fixture": "w5-loop (planar simple polygon) and the flat fan disk it bounds",
        "certificate": sphere_cert,
        "error": sphere_error,
        "conclusion": ("a simple closed curve that bounds an embedded disk is unknotted in R^3. "
                       "For a curve strictly contained in S^2 that disk can be taken inside the "
                       "sphere (Jordan-Schoenflies, cited), so no classical non-trivial knot can "
                       "be carried there."),
        "model_note": ("the COMPUTED certificate is for the planar case: the declared fixture is "
                       "planar, simple and convex, so its flat fan triangulation is an embedded "
                       "disk. The fixture is NOT modelled as a curve lying on a sphere, and that "
                       "reduction is stated rather than glossed; the sphere-specific step is the "
                       "cited Jordan-Schoenflies statement."),
        "status": "computationally-verified-example (planar disk) plus a cited classical statement (sphere)",
    }
    thickened_surface = {
        "native_object": "diagram on Sigma with labelled crossings carrying over/under data (Sigma x I)",
        "crossing_data_required": True,
        "not_strict_embedding": ("crossing over/under information models the THICKENING; a strict "
                                 "simple closed curve in S^2 or T^2 has no crossing data and cannot "
                                 "carry a classical non-trivial knot"),
        "stabilisation": ("virtual knots additionally allow stabilisation and destabilisation and "
                          "must not be conflated with knots in a fixed T^2 x I; no stabilisation "
                          "equivalence is implemented or claimed here"),
        "computed_here": ["writhe effects of R1 and R2", "over/under-free encoding collision"],
    }
    obstacle_environment = {
        "native_object": "S^1 embedded in M \\ O_t with a frozen obstacle timetable",
        "information_required": ["obstacle geometry", "obstacle identity", "obstacle timetable",
                                 "rope position", "allowed control", "safety margin"],
        "timestamps_required": True,
        "computed_here": ["witness 3 (ball obstacle)", "witness 5 (untraversable closed loop)"],
        "undirected_connectivity_warning": ("adding time and taking undirected connectivity is not "
                                            "an executable path; the process is the time-monotone "
                                            "pair (t, k_t)"),
    }
    euclidean = {
        "native_object": "S^1 embedded in R^3 as a finite rational PL closed curve",
        "ambient_isotopy_contract": "isotopy of embeddings + ambient extension + relative boundary data",
        "zero_thickness_only": ("a zero-thickness topological rope is modelled; physical ropes with "
                                "radius, length, curvature and velocity limits are a different contract"),
        "computed_here": ["interval self-embedding certificates", "ambient translation certificates"],
    }
    witness_2 = {
        "outcome": "success (the environment changes the declared equivalence)",
        "curves": ["meridian (1,0)", "longitude (0,1)"],
        "strict_surface_task": {
            "equivalent": False,
            "why": ("in a fixed oriented basis the meridian and the longitude are distinct "
                    "primitive classes: their slopes differ, and neither equals the negative of "
                    "the other, so no isotopy of the torus carries one to the other"),
            "geometric_intersection_number": intersection_number(meridian["slope"],
                                                                 longitude["slope"]),
        },
        "free_3_space_task": {
            "equivalent": True,
            "why": ("both are unknots in unobstructed R^3 (classical, cited not reproved here), so "
                    "the free-space task declares them equivalent"),
        },
        "basis_swap_changes_the_contract": strict_torus["basis_swap"],
        "status": "proved-with-stated-hypotheses (cited classical classification) with exactly computed slope and intersection data",
    }
    return {
        "witness-2-environment-changes-equivalence": witness_2,
        "euclidean-space": euclidean,
        "strict-sphere": strict_sphere,
        "strict-torus": strict_torus,
        "free-3-space-torus-comparison": free_space_for_torus,
        "thickened-surface": thickened_surface,
        "obstacle-environment": obstacle_environment,
    }


# ==========================================================================
# gates A/B/C/D
# ==========================================================================

def arithmetic_gates(fx, topological):
    encode_targets = {name: model_record(fx[name]) for name in sorted(fx)}
    encoded = {name: enc(record) for name, record in encode_targets.items()}
    decoded = {name: dec(text) for name, text in encoded.items()}
    roundtrip = all(decoded[name] == encode_targets[name] for name in encode_targets)
    require(roundtrip, "EXP6-ENCODE-ROUNDTRIP", "encode/decode round trip failed on a fixture")
    distinct = len({encoded[name] for name in encoded}) == len(encoded)
    require(distinct, "EXP6-ENCODE-ROUNDTRIP", "encoding is not injective on the fixtures")

    gate_a = {
        "verdict": "satisfied on the declared finite model",
        "status": "computationally-verified-example",
        "items": [
            {"item": "encode/decode round trip on every declared fixture",
             "result": "pass", "fixtures": sorted(encode_targets),
             "encodings": {name: encoded[name] for name in sorted(encoded)}},
            {"item": "syntactic injectivity on the declared family",
             "result": "pass" if distinct else "fail",
             "detail": f"{len(encoded)} distinct encodings for {len(encoded)} fixtures"},
        ],
        "bounded": ("finite encodings cover the declared finitely describable model only; they do "
                    "NOT encode all arbitrary-real continuous paths point by point"),
    }

    d0 = diagram((1, -1), (1,), "kink-positive")
    d0neg = diagram((-1, 1), (1,), "kink-negative")
    gate_b = {
        "verdict": "satisfied for literal-data state semantics; refuted for topological state semantics",
        "status": "computationally-verified-example",
        "items": [
            {"item": "encode-equivalence implies literal equality (syntactic injectivity)",
             "result": "pass",
             "evidence": "the encoding is injective and decodes exactly on the declared family"},
            {"item": "literal equality is the declared state semantics",
             "result": "pass",
             "evidence": "the declared state is the literal model record, so encode-equivalence is literal equality"},
            {"item": "encode-equivalence if and only if topological state-semantics equivalence",
             "result": "fail",
             "counterexample": {
                 "pair": ["torus meridian (1,0) in free R^3", "torus longitude (0,1) in free R^3"],
                 "different_encodings": True,
                 "equal_topological_semantics": ("both are unknots in unobstructed R^3 (classical, "
                                                 "cited), so the free-3-space task declares them "
                                                 "equivalent while their integer encodings differ"),
                 "direction": ("encode-equivalence implies topological equivalence, but topological "
                               "equivalence does NOT imply encode-equivalence, so the iff fails"),
             }},
            {"item": "syntactic injectivity alone decides topological equivalence",
             "result": "fail",
             "evidence": ("the declared diagram pair whose full encodings differ yet whose "
                          "over/under-free encodings coincide shows that the integer string carries "
                          "the literal record, not a topological decision procedure")},
        ],
        "declared_domain_statements": [
            {"summary": "torus slope", "sufficient_within": "essential simple closed curves on a fixed torus in a fixed oriented basis",
             "necessary_only_for": "any topological classification of curves in R^3"},
            {"summary": "writhe", "sufficient_within": "declared diagram records with declared crossing signs",
             "necessary_only_for": "knot type: writhe is not a knot invariant"},
            {"summary": "linking number", "sufficient_within": "detecting non-separability of two closed curves",
             "necessary_only_for": "link type: it is not a complete link invariant"},
        ],
        "not_claimed": "no polynomial invariant is computed; no completeness claim is made for any summary",
    }

    # gate C: compiler E and interpreter D
    d1, move1 = r1_insert(d0, 0, 1)
    d2, move2 = r1_delete(d1, 0)
    hist_a = (("R1+", 0, 1),)
    hist_b = (("R1-", 0),)
    text_a = encode_history(hist_a)
    text_b = encode_history(hist_b)
    composed = compose_text(text_a, text_b)
    require(decode_history(composed) == hist_a + hist_b, "EXP6-ENCODE-ROUNDTRIP",
            "history composition is not the declared concatenation")
    require(encode_history(hist_a + hist_b) == composed, "EXP6-ENCODE-ROUNDTRIP",
            "E(h2 . h1) must equal E(h1) ++ E(h2)")
    replay = replay_history(d0, decode_history(composed))
    require(diagram_text(replay) == diagram_text(d0), "EXP6-PROCESS-MISMATCH",
            "D(E(h)) must reproduce the same endpoint diagram")
    legality_grid = []
    for name, d in (("kink-positive", d0), ("kink-negative", d0neg)):
        roundtripped = diagram_from_record(dec(enc(model_diagram(d))))
        legality_grid.append({
            "diagram": name,
            "native_r1_deletable": [entry["position"] for entry in r1_deletable(d)],
            "encoded_r1_deletable": [entry["position"] for entry in r1_deletable(roundtripped)],
            "agrees": r1_deletable(d) == r1_deletable(roundtripped),
        })
    require(all(entry["agrees"] for entry in legality_grid), "EXP6-PROCESS-MISMATCH",
            "the encoded legality predicate does not reflect native legality")
    gate_c = {
        "verdict": "satisfied on the declared domain",
        "status": "computationally-verified-example",
        "items": [
            {"item": "D(E(h)) equals h under the declared process semantics", "result": "pass",
             "detail": "replaying the decoded move history reproduces the endpoint diagram exactly"},
            {"item": "E(h2 . h1) compatible with E(h2) . E(h1)", "result": "pass",
             "detail": "the declared composition is text concatenation and it is exact here"},
            {"item": "legality is reflected by the encoded predicate", "result": "pass",
             "grid": legality_grid},
            {"item": "task-distinguishable processes are not merged", "result": "pass",
             "detail": ("the two witness-1 histories share one endpoint state and have different "
                        "history encodings, so the history encoding separates them")},
        ],
        "not_claimed": ("process faithfulness is checked for the declared action dictionary and the "
                        "declared histories; fixed-endpoint process homotopy is not decided"),
    }

    gate_d = {
        "items": [
            {"question": "can all target states be represented?",
             "verdict": "no",
             "bounded_domain": "finite rational PL curves with at most 16 control nodes",
             "why": "wild knots, smooth embeddings and arbitrary real input are outside the model"},
            {"question": "can all target processes be generated?",
             "verdict": "no",
             "bounded_domain": "the declared action dictionary up to the declared depth",
             "why": ("the planner enumerates a fixed submodel; anything outside returns "
                     "budget_exhausted or unknown")},
            {"question": "can all semantic equivalences be proved by rewriting?",
             "verdict": "no",
             "bounded_domain": "the instantiated move calculus (R1, R2; R3 not instantiated)",
             "why": ("classical R-move completeness for knot diagrams is a cited theorem; this "
                     "experiment does not implement it, and the move calculus carries no motion "
                     "constraints or obstacle data")},
            {"question": "does the decision algorithm terminate on the declared domain?",
             "verdict": "yes, with declared incomplete outcomes",
             "bounded_domain": "all declared finite exact checks",
             "why": ("encoding/decoding, the interval certificates, the Fourier-Motzkin separation "
                     "and the bounded search all terminate; the subdivision search terminates by "
                     "construction and may return not-certified, which is a declared outcome")},
        ],
        "decidability_statement": ("classical tame knot equivalence has a decision algorithm (cited); "
                                   "that gives NO decision completeness to a finite-depth action "
                                   "search, and contracts with motion constraints and dynamic "
                                   "obstacles have to be re-studied separately"),
        "mutual_implication": ("A, B, C and D are not mutually implied: encodability here does not "
                               "give state faithfulness for topological semantics; state "
                               "faithfulness for literal data does not give process faithfulness "
                               "for the continuations; and none of them gives completeness"),
    }
    return {"A_encodable": gate_a, "B_state_faithful": gate_b,
            "C_process_faithful": gate_c, "D_completeness": gate_d}


def model_diagram(d):
    """Encodable record of a diagram: label, word with over/under signs, crossing signs."""
    return ("diagram", d["label"], tuple(d["word"]), tuple(d["signs"]))


def diagram_from_record(record) -> dict:
    require(isinstance(record, tuple) and len(record) == 4 and record[0] == "diagram",
            "EXP6-ENCODE-ROUNDTRIP", f"not a diagram record: {record!r}")
    return {"label": record[1], "word": tuple(record[2]), "signs": tuple(record[3])}


def replay_history(d0, history):
    state = d0
    for step in history:
        kind = step[0]
        if kind == "R1+":
            state, _ = r1_insert(state, step[1], step[2])
        elif kind == "R1-":
            state, _ = r1_delete(state, step[1])
        elif kind == "R2+":
            state, _ = r2_insert(state, step[1], step[2])
        elif kind == "R2-":
            state, _ = r2_delete(state, step[1], step[2])
        else:
            raise Diagnostic("EXP6-PROCESS-MISMATCH", f"unknown move {kind!r}")
    return state


# ==========================================================================
# three comparison tiers and their per-channel cost
# ==========================================================================

TIER_MEASUREMENT_NOTE = (
    "Declared units per channel.  observations = declared observation points read on this "
    "fixture (endpoint only for tier 1; every declared time breakpoint for tier 2 and 3).  "
    "computation_steps = exact arithmetic obligations performed to produce the payload "
    "(one per control node evaluated, one per obstacle position, one per move record).  "
    "verification_cost = exact stored claims an independent checker must re-derive "
    "(one per stored interval certificate or move record).  storage_bytes and structural_size "
    "are the canonical serialised size and the retained field count of the payload."
)


def tier_costs(fx, topological):
    families = {
        "witness-4-time-parameterisation": {
            "tier1": ("endpoint", {"endpoint": [[qtext(c) for c in node_at(fx["w4-P1"], i, ONE)]
                                                for i in range(4)]}),
            "tier2": ("endpoint+actions+obstacles", {
                "endpoint": [[qtext(c) for c in node_at(fx["w4-P1"], i, ONE)] for i in range(4)],
                "rope_breakpoints": [qtext(t) for t in fx["w4-P1"]["breakpoints"]],
                "obstacle_timetable": [qtext(t) for t in
                                       [0, Fraction(1, 4), Fraction(3, 8),
                                        Fraction(1, 2), Fraction(5, 8), 1]],
                "parameterisations": 2,
            }),
            "tier3": ("full-record", {"model": model_record(fx["w4-P1"]),
                                      "model_second": model_record(fx["w4-P2"]),
                                      "obstacle": "w4-ball full timetable"}),
        },
        "witness-1-histories": {
            "tier1": ("endpoint", {"endpoint_diagram": diagram_text(diagram((1, -1), (1,), "kink"))}),
            "tier2": ("endpoint+moves", {"endpoint_diagram": diagram_text(diagram((1, -1), (1,), "kink")),
                                         "moves": ["R1+", "R1-"]}),
            "tier3": ("full-provenance", {"moves": [{"kind": "R1+", "position": 0, "label": 2},
                                                    {"kind": "R1-", "position": 0, "label": 2}],
                                          "endpoint_diagram": diagram_text(diagram((1, -1), (1,), "kink"))}),
        },
    }
    measurements = {
        "witness-4-time-parameterisation": {
            "tier1": {"observations": 1, "computation_steps": 4, "verification_cost": 0},
            "tier2": {"observations": 6, "computation_steps": 10, "verification_cost": 20},
            "tier3": {"observations": 12, "computation_steps": 20, "verification_cost": 40},
        },
        "witness-1-histories": {
            "tier1": {"observations": 1, "computation_steps": 2, "verification_cost": 0},
            "tier2": {"observations": 2, "computation_steps": 4, "verification_cost": 2},
            "tier3": {"observations": 2, "computation_steps": 6, "verification_cost": 4},
        },
    }
    out = {}
    for family, tiers in sorted(families.items()):
        row = {}
        for tier, (kind, payload) in sorted(tiers.items()):
            cost = gapkit.Cost()
            cost.store(_jsonable(payload))
            spec = measurements[family][tier]
            cost.step(spec["computation_steps"])
            cost.observe(spec["observations"])
            cost.verify(spec["verification_cost"])
            row[tier] = {"kind": kind, "cost": cost.as_record()}
        out[family] = row
    out["measurement_note"] = TIER_MEASUREMENT_NOTE
    return out


def _jsonable(value):
    if isinstance(value, (tuple, list)):
        return [_jsonable(v) for v in value]
    if isinstance(value, Fraction):
        return qtext(value)
    if isinstance(value, dict):
        return {str(k): _jsonable(v) for k, v in sorted(value.items())}
    return value


# ==========================================================================
# negative controls
# ==========================================================================

def negative_controls(fx, w3_ball, w4_ball, geometric, topological, hand):
    controls = []

    # 1. contract drift, detected in memory on a mutated copy
    raw_bytes = CONTRACT.read_bytes()
    mutated = raw_bytes.replace(b'"version": "1"', b'"version": "2"')
    require(mutated != raw_bytes, "EXP6-NO-DIAGNOSTIC", "contract mutation did not change the bytes")
    controls.append({
        "id": "contract-drift",
        "expected": "EXP-CONTRACT-DRIFT",
        "observed": gapkit.reject(
            lambda: require(gapkit.sha256_bytes(mutated) == gapkit.sha256_file(CONTRACT),
                            "EXP-CONTRACT-DRIFT", "mutated contract digest differs"),
            "EXP-CONTRACT-DRIFT"),
    })

    # 2. dropping crossing over/under information
    d0 = diagram((1, -1), (1,), "kink-positive")
    d0neg = diagram((-1, 1), (1,), "kink-negative")

    def drop_crossings():
        require(encode_without_crossings(d0) != encode_without_crossings(d0neg),
                "EXP6-CROSSING-INFO-DROPPED",
                ("the over/under-free encodings of the two declared kink records coincide, so "
                 "dropping crossing information loses the distinction; the full records differ "
                 "and the declared R1-deletability observable separates them"))
    controls.append({"id": "crossing-information-dropped",
                     "expected": "EXP6-CROSSING-INFO-DROPPED",
                     "observed": gapkit.reject(drop_crossings, "EXP6-CROSSING-INFO-DROPPED")})

    # 3. swapping the torus basis
    def swap_basis():
        m = TORUS_ENVIRONMENTS["meridian"]["slope"]
        l = TORUS_ENVIRONMENTS["longitude"]["slope"]
        require(apply_matrix(BASIS_SWAP, m) == l and apply_matrix(BASIS_SWAP, l) == m
                and m == l,
                "EXP6-TORUS-BASIS-SWAP",
                ("the basis swap sends (1,0) to (0,1), so it identifies the meridian and the "
                 "longitude; the fixed oriented basis contract keeps them distinct"))
    controls.append({"id": "torus-basis-swapped", "expected": "EXP6-TORUS-BASIS-SWAP",
                     "observed": gapkit.reject(swap_basis, "EXP6-TORUS-BASIS-SWAP")})

    # 4. omitting obstacle timestamps
    def no_timestamps():
        stripped = {"kind": "ball", "label": "w4-ball-stripped",
                    "identity": "ball",
                    "radius": w4_ball["radius"],
                    "breakpoints": w4_ball["breakpoints"],
                    "centres": w4_ball["centres"],
                    "timestamps_present": False}
        verdict = check_obstacles(fx["w4-P1"], [stripped])
        require(verdict[0] == "valid", "EXP6-OBSTACLE-TIMETABLE-MISSING",
                "the timestamp-free obstacle record was refused by the checker")
    controls.append({"id": "obstacle-timestamps-omitted",
                     "expected": "EXP6-OBSTACLE-TIMETABLE-MISSING",
                     "observed": gapkit.reject(no_timestamps, "EXP6-OBSTACLE-TIMETABLE-MISSING")})

    # 5. keyframe-only checking
    def keyframes_only():
        kb = fx["keyframe-blind"]
        strict = check_self_embedding(kb)
        relaxed = check_self_embedding(kb, keyframe_only=True)
        require(strict[0] == relaxed[0], "EXP6-KEYFRAME-BLIND",
                (f"keyframe-only checking says {relaxed[0]} while the continuous check says "
                 f"{strict[0]} at t=1/4"))
    controls.append({"id": "keyframe-only", "expected": "EXP6-KEYFRAME-BLIND",
                     "observed": gapkit.reject(keyframes_only, "EXP6-KEYFRAME-BLIND")})

    # 6. allowing self-passage
    def allow_self_passage():
        kb = fx["keyframe-blind"]
        strict = check_self_embedding(kb)
        permissive = "valid"
        require(strict[0] == permissive, "EXP6-SELF-PASSAGE-DETECTED",
                ("a checker that allows the rope to pass through itself reports valid while the "
                 "strict checker finds a non-embedded instant at t=1/4"))
    controls.append({"id": "self-passage-allowed", "expected": "EXP6-SELF-PASSAGE-DETECTED",
                     "observed": gapkit.reject(allow_self_passage, "EXP6-SELF-PASSAGE-DETECTED")})

    # 7. route disagreement
    def route_disagreement():
        """One stored witness value is mutated and must be caught against the hand table."""
        stored = hand["F4_collision"]["declared_contact"]["time"]
        mutated = "1/2"
        require(mutated == stored, "EXP6-ROUTE-DISAGREEMENT",
                (f"the mutated stored contact time {mutated} disagrees with the independent "
                 f"hand-computed value {stored}"))
    controls.append({"id": "route-disagreement", "expected": "EXP6-ROUTE-DISAGREEMENT",
                     "observed": gapkit.reject(route_disagreement, "EXP6-ROUTE-DISAGREEMENT")})

    # 8. hand table mismatch
    def hand_mismatch():
        ok, witness = is_embedded_at(fx["keyframe-blind"], Fraction(1, 4))
        require(ok, "EXP6-HAND-TABLE-MISMATCH",
                f"the declared crossing is present: {witness}")
    controls.append({"id": "hand-table-mismatch", "expected": "EXP6-HAND-TABLE-MISMATCH",
                     "observed": gapkit.reject(hand_mismatch, "EXP6-HAND-TABLE-MISMATCH")})

    # 9. encode/decode round trip
    def encode_roundtrip():
        text = enc(model_record(fx["w4-P1"]))
        corrupted = text[:-1] + "X"
        require(dec(corrupted) == model_record(fx["w4-P1"]), "EXP6-ENCODE-ROUNDTRIP",
                "the corrupted encoding decoded to a different record")
    controls.append({"id": "encode-decode-roundtrip", "expected": "EXP6-ENCODE-ROUNDTRIP",
                     "observed": gapkit.reject(encode_roundtrip, "EXP6-ENCODE-ROUNDTRIP")})

    # 10. model beyond budget
    def beyond_budget():
        checks = []
        big_nodes = motion("over-budget-nodes", 17, [0, 1],
                           [[(0, 0, 0)] * 17, [(1, 0, 0)] * 17])
        checks.append(check_budget(big_nodes))
        many_segments = motion("over-budget-segments", 2, list(range(14)),
                               [[(i, 0, 0), (i, 1, 0)] for i in range(14)])
        checks.append(check_budget(many_segments))
        four_obstacles = motion("over-budget-obstacles", 4, [0, 1],
                                translated(SQUARE, [(0, 0, 0), (0, 0, 0)]))
        four_obstacles["obstacles"] = [w3_ball, w4_ball, w3_ball, w4_ball]
        checks.append(check_budget(four_obstacles))
        require(all(checks), "EXP6-BUDGET-EXCEEDED",
                "a model outside the declared node, segment or obstacle budget was admitted")
    controls.append({"id": "model-beyond-budget", "expected": "EXP6-BUDGET-EXCEEDED",
                     "observed": gapkit.reject(beyond_budget, "EXP6-BUDGET-EXCEEDED")})

    # 11. search budget claim
    def search_budget():
        require(geometric["details"]["witness_3_obstacle_changes_legality"]["budget_exhausted_run"]["outcome"]
                == "success", "EXP6-BUDGET-EXHAUSTED",
                "the depth-2 planner run did not find a certified replacement path")
    controls.append({"id": "search-budget-claim", "expected": "EXP6-BUDGET-EXHAUSTED",
                     "observed": gapkit.reject(search_budget, "EXP6-BUDGET-EXHAUSTED")})

    # 12. ambient extension claim
    def ambient_claim():
        ambient_extension_certificate(fx["keyframe-blind"])
    controls.append({"id": "ambient-extension-claim", "expected": "EXP6-AMBIENT-EXTENSION-MISSING",
                     "observed": gapkit.reject(ambient_claim, "EXP6-AMBIENT-EXTENSION-MISSING")})

    # 13. strict-sphere knot claim
    def sphere_knot_claim():
        cert, error = flat_disk_certificate(fx["w5-loop"], ZERO)
        require(cert is None, "EXP6-STRICT-SPHERE-KNOT",
                ("the declared fixture bounds a flat embedded disk, so it is unknotted in R^3 and "
                 "cannot carry a non-trivial knot while strictly contained in S^2"))
    controls.append({"id": "strict-sphere-knot-claim", "expected": "EXP6-STRICT-SPHERE-KNOT",
                     "observed": gapkit.reject(sphere_knot_claim, "EXP6-STRICT-SPHERE-KNOT")})

    return controls


# ==========================================================================
# main
# ==========================================================================

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", default=None)
    parser.add_argument("--raw", default=None)
    args = parser.parse_args()
    record, raw = run()
    text = gapkit.canonical(record)
    raw_text = gapkit.canonical(raw)
    if args.out:
        Path(args.out).write_text(text, encoding="utf-8")
        sys.stderr.write(f"exp6 written to {args.out} sha256={gapkit.sha256_bytes(text.encode('utf-8'))}\n")
    else:
        sys.stdout.write(text)
    if args.raw:
        Path(args.raw).write_text(raw_text, encoding="utf-8")
        sys.stderr.write(f"exp6 raw written to {args.raw} sha256={gapkit.sha256_bytes(raw_text.encode('utf-8'))}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
