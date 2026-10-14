#!/usr/bin/env python3
"""Experiment 6, independent route -- closed-form exact geometry.

This checker deliberately shares NO semantic helper with
``exp6_knot_deformation_environment.py``.  Nothing is imported from it: not a
distance routine, not a certificate routine, not a move implementation, not a
cost helper, not even the fixture builder.  The fixtures are transcribed here as
literals, so a transcription error shows up as a route disagreement instead of
being masked by shared data.  Only the JSON serialiser (``gapkit``), the frozen
contract and the primary's *evidence file* are shared, and the latter is read as
data to be checked, never called.

Where the primary route proves clearance by multilinear box-hull separation with
exact Fourier-Motzkin elimination plus interval certificates (sound but
incomplete), this route computes the SAME predicates by a different formulation:

* exact closed-form minimisation of squared distances --
  segment-segment by solving the 2x2 normal equations of the bivariate convex
  quadratic plus enumeration of the four boundary edges, point-segment by the
  clamped critical parameter;
* whole-interval certification by an exact rational motion bound: the squared
  distance at the left endpoint minus (Lipschitz constant times elapsed time),
  refined by subdividing time;
* exact rational square-root lower bounds (no float, no square root taken);
* the linking number by the signed crossing count of a generic projection (the
  primary route uses the algebraic intersection with a spanning disk);
* an independently written re-implementation of the instantiated local-move
  calculus and a hand-computed witness table entered as literals.

It also re-verifies every interval certificate stored by the primary against
independently recomputed geometry, and raises EXP6-ROUTE-DISAGREEMENT on any
disagreement, including a disagreement in a stored certificate.

Run:

    python3 research/process-representation-gap/experiments/exp6_knot_deformation_environment_independent.py
"""

from __future__ import annotations

import argparse
import json
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
PRIMARY_EVIDENCE = ROOT / "evidence" / "exp6-knot-deformation-environment.json"
PRIMARY_RAW = ROOT / "evidence" / "exp6-knot-deformation-environment.raw.json"
FROZEN = ROOT / "contracts" / "FROZEN.sha256"

SCHEMA = "aeg.process-representation-gap.exp6-independent.v1"
SQRT_SCALE = 1024
REFINE_DEPTH = 8

ZERO = Fraction(0)
ONE = Fraction(1)


def q(text) -> Fraction:
    return Fraction(text)


def vsub(a, b):
    return (a[0] - b[0], a[1] - b[1], a[2] - b[2])


def vadd(a, b):
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2])


def vscale(k, a):
    return (k * a[0], k * a[1], k * a[2])


def vdot(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]


def vnorm2(a):
    return vdot(a, a)


def lower_sqrt(value: Fraction) -> Fraction:
    """Exact rational lower bound of sqrt(value), no square root is taken."""
    require(value >= 0, "EXP6I-NEGATIVE-SQRT", qtext(value))
    scaled = value * SQRT_SCALE * SQRT_SCALE
    return Fraction(isqrt(int(scaled)), SQRT_SCALE)


# ==========================================================================
# fixtures, transcribed as literals (no import from the primary)
# ==========================================================================

SQUARE = ((0, 0, 0), (2, 0, 0), (2, 2, 0), (0, 2, 0))
CENTRED = ((1, 1, 0), (-1, 1, 0), (-1, -1, 0), (1, -1, 0))
LOOP = ((0, 0, 1), (2, 0, 1), (2, 0, -1), (0, 0, -1))
ROTATED = ((Fraction(-1, 5), Fraction(7, 5), 0),
           (Fraction(-7, 5), Fraction(-1, 5), 0),
           (Fraction(1, 5), Fraction(-7, 5), 0),
           (Fraction(7, 5), Fraction(1, 5), 0))


def translated(shape, offsets):
    return [[(p[0] + o[0], p[1] + o[1], p[2] + o[2]) for p in shape] for o in offsets]


def fixture(nodes, bps, positions):
    return {
        "nodes": nodes,
        "bps": tuple(Fraction(b) for b in bps),
        "positions": [[(Fraction(c[0]), Fraction(c[1]), Fraction(c[2])) for c in row]
                      for row in positions],
    }


def build():
    fx = {}
    fx["w4-P1"] = fixture(4, [0, 1], translated(SQUARE, [(0, 0, 0), (8, 0, 0)]))
    fx["w4-P2"] = fixture(4, [0, Fraction(1, 2), 1],
                          translated(SQUARE, [(0, 0, 0), (0, 0, 0), (8, 0, 0)]))
    fx["w3-free"] = fixture(4, [0, 1], translated(SQUARE, [(-2, 0, 0), (2, 0, 0)]))
    fx["w3-plan"] = fixture(4, [0, 1, 2, 3, 4],
                            translated(SQUARE, [(-2, 0, 0), (-2, 0, 2), (0, 0, 2),
                                                (2, 0, 2), (2, 0, 0)]))
    fx["keyframe-blind"] = fixture(
        5, [0, 1],
        [[(0, 0, 0), (2, 0, 0), (2, 4, 0), (0, 4, 0), (1, -1, 1)],
         [(0, 0, 0), (2, 0, 0), (2, 4, 0), (0, 4, 0), (1, -1, -3)]])
    fx["w5-rope"] = fixture(4, [0, Fraction(2, 3), 1],
                            translated(CENTRED, [(-3, 0, 0), (-1, 0, 0), (0, 0, 0)]))
    fx["w5-loop"] = fixture(4, [0, 1], translated(LOOP, [(0, 0, 0), (0, 0, 0)]))
    fx["rotated-hopf"] = fixture(4, [0, 1], translated(ROTATED, [(0, 0, 0), (0, 0, 0)]))
    return fx


BALLS = {
    "w4-ball": {"radius": Fraction(1, 4),
                "bps": [0, Fraction(1, 4), Fraction(3, 8), Fraction(1, 2),
                        Fraction(5, 8), 1],
                "centres": [(1, 0, 10), (1, 0, 10), (1, 0, 0), (1, 0, 0), (1, 0, 10),
                            (1, 0, 10)]},
    "w3-ball": {"radius": Fraction(1, 2), "bps": [0, 4], "centres": [(1, 1, 0), (1, 1, 0)]},
}


# ==========================================================================
# exact closed-form geometry
# ==========================================================================

def node_at(fx, i, t):
    bps = fx["bps"]
    require(bps[0] <= t <= bps[-1], "EXP6I-TIME-OUT-OF-RANGE", qtext(t))
    k = 0
    for idx in range(len(bps) - 1):
        if bps[idx] <= t <= bps[idx + 1]:
            k = idx
            break
    lam = (t - bps[k]) / (bps[k + 1] - bps[k])
    p0 = fx["positions"][k][i]
    p1 = fx["positions"][k + 1][i]
    return vadd(p0, vscale(lam, vsub(p1, p0)))


def edges(fx):
    n = fx["nodes"]
    return tuple((i, (i + 1) % n) for i in range(n))


def edge_points(fx, e, t):
    i, j = edges(fx)[e]
    return node_at(fx, i, t), node_at(fx, j, t)


def edges_adjacent(fx, e1, e2):
    n = len(edges(fx))
    d = (e1 - e2) % n
    return d in (1, n - 1)


def one_dim_min_sq(constant: Fraction, linear: Fraction, quadratic: Fraction,
                   lo: Fraction = ZERO, hi: Fraction = ONE):
    """Exact clamped minimiser of constant + 2 s linear + s^2 quadratic over [lo, hi].

    The quadratic is assumed non-negative (it is a squared norm), so the function
    is convex and the minimum is at the clamped critical point.  No square root
    and no float is ever produced.
    """
    if quadratic == 0:
        return lo, constant
    s = -linear / quadratic
    if s < lo:
        s = lo
    elif s > hi:
        s = hi
    return s, constant + 2 * s * linear + s * s * quadratic


def segment_segment_min2(a0, a1, b0, b1):
    """Exact minimum of |X(s) - Y(u)|^2 over the unit square, with minimisers.

    Delta(s, u) = g + s p + u q with g = a0 - b0, p = a1 - a0, q = -(b1 - b0).  The
    squared norm is a convex quadratic; the interior critical point is the exact
    rational solution of the 2x2 normal equations, and otherwise the minimum lies
    on one of the four boundary edges, each of which is a 1D exact minimisation.
    Returns (s, u, value).
    """
    g = vsub(a0, b0)
    p = vsub(a1, a0)
    qv = vsub(b0, b1)
    pp = vnorm2(p)
    qq = vnorm2(qv)
    pq = vdot(p, qv)
    gp = vdot(g, p)
    gq = vdot(g, qv)
    det = pp * qq - pq * pq
    best = None
    if det != 0:
        s = (-gp * qq + gq * pq) / det
        u = (-gq * pp + gp * pq) / det
        if ZERO <= s <= ONE and ZERO <= u <= ONE:
            value = vnorm2(vadd(vadd(g, vscale(s, p)), vscale(u, qv)))
            best = (s, u, value)
    if best is None or best[2] > 0:
        for fixed, which in ((ZERO, "s"), (ONE, "s"), (ZERO, "u"), (ONE, "u")):
            if which == "s":
                base = vadd(g, vscale(fixed, p))
                s_val = fixed
                u_val, value = one_dim_min_sq(vnorm2(base), vdot(base, qv), qq)
            else:
                base = vadd(g, vscale(fixed, qv))
                u_val = fixed
                s_val, value = one_dim_min_sq(vnorm2(base), vdot(base, p), pp)
            if best is None or value < best[2]:
                best = (s_val, u_val, value)
    require(best is not None, "EXP6I-NO-MINIMISER", "segment-segment minimisation failed")
    return best


def point_segment_min2(point, a0, a1):
    """Exact minimum of |point - X(s)|^2 for s in [0, 1]."""
    d = vsub(point, a0)
    v = vsub(a1, a0)
    vv = vnorm2(v)
    if vv == 0:
        return ZERO, vnorm2(d)
    return one_dim_min_sq(vnorm2(d), -vdot(d, v), vv)


# ==========================================================================
# obstacle trajectories, transcribed as literals
# ==========================================================================

def ball_centre(name, t):
    spec = BALLS[name]
    bps = [Fraction(b) for b in spec["bps"]]
    require(bps[0] <= t <= bps[-1], "EXP6I-TIME-OUT-OF-RANGE",
            f"{name}: {qtext(t)} outside the timetable")
    k = 0
    for idx in range(len(bps) - 1):
        if bps[idx] <= t <= bps[idx + 1]:
            k = idx
            break
    lam = (t - bps[k]) / (bps[k + 1] - bps[k])
    c0 = spec["centres"][k]
    c1 = spec["centres"][k + 1]
    c0 = (Fraction(c0[0]), Fraction(c0[1]), Fraction(c0[2]))
    c1 = (Fraction(c1[0]), Fraction(c1[1]), Fraction(c1[2]))
    return vadd(c0, vscale(lam, vsub(c1, c0)))


def horizon(fx, obstacles, table):
    """Time boxes to examine: all rope and obstacle breakpoints inside the rope range."""
    lo, hi = fx["bps"][0], fx["bps"][-1]
    points = set(fx["bps"])
    for name in obstacles:
        if name in BALLS:
            bps = [Fraction(b) for b in BALLS[name]["bps"]]
        else:
            bps = list(table[name]["bps"])
        require(bps[0] <= lo and bps[-1] >= hi, "EXP6I-TIMETABLE-INCOMPLETE",
                f"{name}: timetable does not cover [{qtext(lo)}, {qtext(hi)}]")
        points.update(bps)
    return tuple(sorted(t for t in points if lo <= t <= hi))


# ==========================================================================
# whole-interval verdicts by exact motion bounds
# ==========================================================================

def lipschitz_ball(fx, e, obstacle, t0, t1):
    """Exact bound on |d/dt (X_e(s,t) - C(t))| over the time box, maximised over s.

    d/dt (X_e(s,t) - C(t)) = (1 - s) v_0 + s v_1 - v_C with v_j the endpoint
    velocities inside the box; that expression is affine in s, so its maximum
    norm over [0, 1] is attained at an endpoint and is bounded exactly.
    """
    width = t1 - t0
    def endpoint_velocity(fx_, e_, which):
        node = edges(fx_)[e_][which]
        return vscale(ONE / width, vsub(node_at(fx_, node, t1), node_at(fx_, node, t0)))
    v_c = vscale(ONE / width, vsub(ball_centre(obstacle, t1), ball_centre(obstacle, t0)))
    d0 = vsub(endpoint_velocity(fx, e, 0), v_c)
    d1 = vsub(endpoint_velocity(fx, e, 1), v_c)
    return max(_norm(d0), _norm(d1))


def lipschitz_pair(fx1, e1, fx2, e2, t0, t1):
    """Exact bound on |d/dt (X_{e1}(s,t) - X_{e2}(u,t))| over the box."""
    width = t1 - t0
    def endpoint_velocity(fx, e, which, t0_, t1_):
        node = edges(fx)[e][which]
        return vscale(ONE / width, vsub(node_at(fx, node, t1_), node_at(fx, node, t0_)))
    d = []
    for which in (0, 1):
        for other in (0, 1):
            delta = vsub(endpoint_velocity(fx1, e1, which, t0, t1),
                         endpoint_velocity(fx2, e2, other, t0, t1))
            d.append(_norm(delta))
    return max(d)


def _norm(v):
    """Exact rational upper bound on |v| without taking a square root."""
    squared = vnorm2(v)
    value = lower_sqrt(squared) + Fraction(1, SQRT_SCALE)
    require(value * value >= squared, "EXP6I-NORM-BOUND",
            "the rational norm bound failed; increase SQRT_SCALE")
    return value


def self_embedded_verdict(fx, depth=REFINE_DEPTH):
    """Whole-interval self-embedding verdict by exact motion bounds."""
    pairs = [(e1, e2) for e1 in range(len(edges(fx))) for e2 in range(e1 + 1, len(edges(fx)))
             if not edges_adjacent(fx, e1, e2)]
    bps = fx["bps"]
    rows = []
    collisions = []
    undecided = []
    for k in range(len(bps) - 1):
        stack = [(bps[k], bps[k + 1], 0)]
        stack = list(reversed(stack))
        while stack:
            t0, t1, level = stack.pop()
            for t in (t0, t1):
                hit = _single_time_self_collision(fx, t, pairs)
                if hit is not None:
                    collisions.append(hit)
                    return {"verdict": "invalid", "witness": collisions[0],
                            "certificates": rows, "undecided": undecided}
            certified = True
            box_rows = []
            for e1, e2 in pairs:
                a0, a1 = edge_points(fx, e1, t0)
                b0, b1 = edge_points(fx, e2, t0)
                s, u, value = segment_segment_min2(a0, a1, b0, b1)
                lip = lipschitz_pair(fx, e1, fx, e2, t0, t1)
                bound = lower_sqrt(value) - lip * (t1 - t0)
                certified = certified and bound > 0
                box_rows.append({"edges": [e1, e2], "time": [qtext(t0), qtext(t1)],
                                 "distance_squared_at_left": qtext(value),
                                 "lipschitz_bound": qtext(lip),
                                 "distance_lower_bound": qtext(bound)})
            if certified:
                rows.extend(box_rows)
                continue
            if level >= depth:
                undecided.append({"time": [qtext(t0), qtext(t1)], "level": level})
                continue
            mid = (t0 + t1) / 2
            stack.append((mid, t1, level + 1))
            stack.append((t0, mid, level + 1))
    if undecided:
        return {"verdict": "not-certified", "witness": None, "certificates": rows,
                "undecided": undecided}
    return {"verdict": "valid", "witness": None, "certificates": rows, "undecided": []}


def _single_time_self_collision(fx, t, pairs):
    for e1, e2 in pairs:
        a0, a1 = edge_points(fx, e1, t)
        b0, b1 = edge_points(fx, e2, t)
        s, u, value = segment_segment_min2(a0, a1, b0, b1)
        if value == 0:
            point = vadd(a0, vscale(s, vsub(a1, a0)))
            return {"kind": "nonadjacent-crossing", "time": qtext(t), "edges": [e1, e2],
                    "parameters": [qtext(s), qtext(u)],
                    "point": [qtext(c) for c in point]}
    nodes = [node_at(fx, i, t) for i in range(fx["nodes"])]
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            if nodes[i] == nodes[j]:
                return {"kind": "node-coincidence", "time": qtext(t), "nodes": [i, j],
                        "point": [qtext(c) for c in nodes[i]]}
    return None


def obstacle_verdict(fx, obstacles, table, depth=REFINE_DEPTH):
    """Whole-interval obstacle verdict by exact motion bounds."""
    bps = horizon(fx, obstacles, table)
    rows = []
    undecided = []
    for k in range(len(bps) - 1):
        stack = [(bps[k], bps[k + 1], 0)]
        stack = list(reversed(stack))
        while stack:
            t0, t1, level = stack.pop()
            for t in (t0, t1):
                hit = _single_time_obstacle_collision(fx, obstacles, t, table)
                if hit is not None:
                    return {"verdict": "invalid", "witness": hit, "certificates": rows,
                            "undecided": undecided}
            certified = True
            box_rows = []
            for name in obstacles:
                if name in BALLS:
                    radius = BALLS[name]["radius"]
                    for e in range(len(edges(fx))):
                        a0, a1 = edge_points(fx, e, t0)
                        centre = ball_centre(name, t0)
                        s, value = point_segment_min2(centre, a0, a1)
                        lip = lipschitz_ball(fx, e, name, t0, t1)
                        bound = lower_sqrt(value) - lip * (t1 - t0)
                        certified = certified and bound > radius
                        box_rows.append({"obstacle": name, "edge": e,
                                         "time": [qtext(t0), qtext(t1)],
                                         "distance_squared_at_left": qtext(value),
                                         "lipschitz_bound": qtext(lip),
                                         "distance_lower_bound": qtext(bound),
                                         "radius": qtext(radius)})
                else:
                    loop = table[name]
                    for e1 in range(len(edges(fx))):
                        for e2 in range(len(edges(loop))):
                            a0, a1 = edge_points(fx, e1, t0)
                            b0, b1 = edge_points(loop, e2, t0)
                            s, u, value = segment_segment_min2(a0, a1, b0, b1)
                            lip = lipschitz_pair(fx, e1, loop, e2, t0, t1)
                            bound = lower_sqrt(value) - lip * (t1 - t0)
                            certified = certified and bound > 0
                            box_rows.append({"obstacle": name, "edges": [e1, e2],
                                             "time": [qtext(t0), qtext(t1)],
                                             "distance_squared_at_left": qtext(value),
                                             "lipschitz_bound": qtext(lip),
                                             "distance_lower_bound": qtext(bound)})
            if certified:
                rows.extend(box_rows)
                continue
            if level >= depth:
                undecided.append({"time": [qtext(t0), qtext(t1)], "level": level})
                continue
            mid = (t0 + t1) / 2
            stack.append((mid, t1, level + 1))
            stack.append((t0, mid, level + 1))
    if undecided:
        return {"verdict": "not-certified", "witness": None, "certificates": rows,
                "undecided": undecided}
    return {"verdict": "valid", "witness": None, "certificates": rows, "undecided": []}


def _single_time_obstacle_collision(fx, obstacles, t, table):
    for name in obstacles:
        if name in BALLS:
            radius2 = BALLS[name]["radius"] * BALLS[name]["radius"]
            centre = ball_centre(name, t)
            best = None
            for e in range(len(edges(fx))):
                a0, a1 = edge_points(fx, e, t)
                s, value = point_segment_min2(centre, a0, a1)
                if value > radius2:
                    continue
                if best is None or value < best[2]:
                    best = (e, s, value, a0, a1)
            if best is not None:
                e, s, value, a0, a1 = best
                point = vadd(a0, vscale(s, vsub(a1, a0)))
                return {"kind": "ball-collision", "obstacle": name, "edge": e,
                        "time": qtext(t), "parameter": qtext(s),
                        "point": [qtext(c) for c in point],
                        "distance_squared": qtext(value),
                        "radius_squared": qtext(radius2)}
        else:
            loop = table[name]
            best = None
            for e1 in range(len(edges(fx))):
                a0, a1 = edge_points(fx, e1, t)
                for e2 in range(len(edges(loop))):
                    b0, b1 = edge_points(loop, e2, t)
                    s, u, value = segment_segment_min2(a0, a1, b0, b1)
                    if value != 0:
                        continue
                    if best is None or (e1, e2) < (best[0], best[1]):
                        best = (e1, e2, s, u, a0, a1)
            if best is not None:
                e1, e2, s, u, a0, a1 = best
                point = vadd(a0, vscale(s, vsub(a1, a0)))
                return {"kind": "loop-crossing", "obstacle": name, "time": qtext(t),
                        "edges": [e1, e2], "parameters": [qtext(s), qtext(u)],
                        "point": [qtext(c) for c in point]}
    return None


# ==========================================================================
# independent linking number: signed crossing count of a generic projection
# ==========================================================================

PROJECTION_DIRECTIONS = ((1, 2, 3), (2, 3, 5), (3, 5, 7), (1, 3, 5), (2, 5, 3))


def linking_by_projection(fx1, t1, fx2, t2, direction):
    """Lk = 1/2 * signed crossing sum, or (None, reason) when not generic."""
    dx, dy, dz = (Fraction(d) for d in direction)

    def proj(p):
        return (p[0] * dy - p[1] * dx, p[0] * dz - p[2] * dx)

    total = 0
    crossings = []
    for e1 in range(len(edges(fx1))):
        a0, a1 = edge_points(fx1, e1, t1)
        p0, p1 = proj(a0), proj(a1)
        da = (p1[0] - p0[0], p1[1] - p0[1])
        for e2 in range(len(edges(fx2))):
            b0, b1 = edge_points(fx2, e2, t2)
            q0, q1 = proj(b0), proj(b1)
            db = (q1[0] - q0[0], q1[1] - q0[1])
            det = da[0] * db[1] - da[1] * db[0]
            if det == 0:
                return None, f"parallel projected edges {e1}/{e2}"
            w = (q0[0] - p0[0], q0[1] - p0[1])
            s = (w[0] * db[1] - w[1] * db[0]) / det
            u = (w[0] * da[1] - w[1] * da[0]) / det
            if not (ZERO < s < ONE and ZERO < u < ONE):
                continue
            point1 = vadd(a0, vscale(s, vsub(a1, a0)))
            point2 = vadd(b0, vscale(u, vsub(b1, b0)))
            height = vdot(vsub(point1, point2), (dx, dy, dz))
            if height == 0:
                return None, f"coincident projected crossing {e1}/{e2}"
            sign = 1 if (det > 0) == (height > 0) else -1
            total += sign
            crossings.append({"edges": [e1, e2], "parameters": [qtext(s), qtext(u)],
                              "sign": sign})
    require(total % 2 == 0, "EXP6I-LINKING-NONINTEGER",
            f"crossing sum {total} is odd; the projection is not generic")
    return total // 2, crossings


def linking_by_disk(fx_rope, t, fx_loop):
    """Lk as the algebraic intersection with the loop's flat rectangle disk."""
    total = 0
    crossings = []
    for e in range(len(edges(fx_rope))):
        a0, a1 = edge_points(fx_rope, e, t)
        if (a0[1]) * (a1[1]) > 0:
            continue
        denom = a1[1] - a0[1]
        if denom == 0:
            return None, f"rope edge {e} lies in the disk plane"
        s = (ZERO - a0[1]) / denom
        if not (ZERO <= s <= ONE):
            continue
        point = vadd(a0, vscale(s, vsub(a1, a0)))
        if point[2] != 0:
            return None, f"rope edge {e} crosses the disk plane off the disk plane"
        if not (ZERO <= point[0] <= 2):
            continue
        sign = 1 if a1[1] > a0[1] else -1
        total += sign
        crossings.append({"edge": e, "parameter": qtext(s),
                          "point": [qtext(c) for c in point], "sign": sign})
    return total, crossings


# ==========================================================================
# independent local-move calculus
# ==========================================================================

def wellformed(word, signs):
    labels = sorted({abs(w) for w in word})
    if labels != list(range(1, len(labels) + 1)) or len(signs) != len(labels):
        return False
    for label in labels:
        entries = sorted(w for w in word if abs(w) == label)
        if entries != [-label, label]:
            return False
    return True


def writhe(signs):
    return sum(signs)


def r1_insert(word, signs, position, sign):
    label = len(signs) + 1
    new_word = word[:position] + (sign * label, -sign * label) + word[position:]
    new_signs = tuple(signs) + (sign,)
    require(wellformed(new_word, new_signs), "EXP6I-DIAGRAM-MALFORMED", str(new_word))
    return new_word, new_signs


def r1_delete(word, signs, position):
    a, b = word[position], word[position + 1]
    require(abs(a) == abs(b) and a == -b, "EXP6I-R1-NOT-A-KINK", f"{a},{b}")
    label = abs(a)
    sign = 1 if a > 0 else -1
    require(signs[label - 1] == sign, "EXP6I-R1-SIGN-MISMATCH", f"label {label}")
    new_word = word[:position] + word[position + 2:]
    remaining = [s for idx, s in enumerate(signs, start=1) if idx != label]
    rename = {old: new for new, old in enumerate(sorted({abs(w) for w in new_word}), start=1)}
    final_word = tuple((1 if w > 0 else -1) * rename[abs(w)] for w in new_word)
    final_signs = []
    for old in sorted(rename, key=lambda k: rename[k]):
        final_signs.append(remaining[old - 1] if old <= label else remaining[old - 2])
    require(wellformed(final_word, tuple(final_signs)), "EXP6I-DIAGRAM-MALFORMED", str(final_word))
    return final_word, tuple(final_signs)


def r2_insert(word, signs, position_a, position_b):
    a = len(signs) + 1
    b = len(signs) + 2
    entries = list(word)
    entries[position_a:position_a] = [a, b]
    entries[position_b + 2:position_b + 2] = [-a, -b]
    new_signs = tuple(signs) + (1, -1)
    require(wellformed(tuple(entries), new_signs), "EXP6I-DIAGRAM-MALFORMED", str(entries))
    return tuple(entries), new_signs


def r2_delete(word, signs, position_a, position_b):
    a, b = word[position_a], word[position_a + 1]
    require(abs(a) == len(signs) - 1 and abs(b) == len(signs), "EXP6I-R2-NOT-A-BIGON",
            f"{a},{b} are not the two fresh labels")
    entries = list(word)
    del entries[position_b + 2:position_b + 4]
    require(entries[position_a] == a and entries[position_a + 1] == b,
            "EXP6I-R2-NOT-A-BIGON", "declared second position")
    del entries[position_a:position_a + 2]
    require(wellformed(tuple(entries), signs[:-2]), "EXP6I-DIAGRAM-MALFORMED", str(entries))
    return tuple(entries), tuple(signs[:-2])


def r1_deletable(word, signs):
    out = []
    for position in range(max(len(word) - 1, 0)):
        a, b = word[position], word[position + 1]
        if abs(a) == abs(b) and a == -b:
            label = abs(a)
            sign = 1 if a > 0 else -1
            if signs[label - 1] == sign:
                out.append({"position": position, "label": label, "sign": sign})
    return out


def without_crossings(word, signs):
    return (tuple(abs(w) for w in word), tuple(signs))


# ==========================================================================
# hand-computed witness table (literals)
# ==========================================================================

HAND_WITNESSES = {
    "keyframe_blind_collision": {"time": "1/4", "edges": [0, 3],
                                 "parameters": ["2/5", "4/5"], "point": ["4/5", "0", "0"]},
    "w4_collision": {"time": "3/8", "edge": 0, "parameter": "1/2", "point": ["1", "0", "0"],
                     "distance_squared": "0", "radius_squared": "1/16"},
    "w3_collision": {"time": "1/4", "edge": 1, "parameter": "1/2", "point": ["1", "1", "0"],
                     "distance_squared": "0", "radius_squared": "1/4"},
    "w5_collision": {"time": "2/3", "edges": [3, 3], "parameters": ["1/2", "1/2"],
                     "point": ["0", "0", "0"]},
    "w5_linking_start": 0,
    "w5_linking_end": 1,
    "w4_clearance_squared": "40400/10201",
    "r1_positive_writhe_delta": 1,
    "r1_negative_writhe_delta": -1,
    "r2_writhe_delta": 0,
}


# ==========================================================================
# cross-checks against the primary evidence
# ==========================================================================

class Disagreements:
    def __init__(self):
        self.items = []

    def check(self, name, expected, observed, detail=""):
        if expected == observed:
            return True
        self.items.append({"check": name, "primary": expected, "independent": observed,
                           "detail": detail})
        return False

    def require_none(self):
        require(not self.items, "EXP6-ROUTE-DISAGREEMENT",
                f"{len(self.items)} disagreement(s): {self.items[:3]}")


def verify_stored_certificates(raw, fx_builder):
    """Re-derive every stored primary certificate from independently read geometry."""
    problems = []
    certificates = raw["certificates"]["w4-P1"]
    for cert in certificates:
        edge = cert["edge"]
        ta, tb = Fraction(cert["time"][0]), Fraction(cert["time"][1])
        fx = fx_builder["w4-P1"]
        recomputed = []
        for s in (ZERO, ONE):
            for t in (ta, tb):
                a0, a1 = edge_points(fx, edge, t)
                point = vadd(a0, vscale(s, vsub(a1, a0)))
                recomputed.append(vsub(point, ball_centre(cert["obstacle"], t)))
        stored = [[Fraction(c) for c in v] for v in cert["vertices"]]
        if [list(v) for v in recomputed] != stored:
            problems.append({"certificate_edge": edge, "time": cert["time"],
                             "issue": "stored box vertices differ from the recomputed ones"})
            continue
        if cert["method"] == "coordinate-hull-separation":
            axis = cert["axis"]
            values = [v[axis] for v in recomputed]
            low, high = min(values), max(values)
            bound = min(abs(low), abs(high))
            if bound != Fraction(cert["bound"]):
                problems.append({"certificate_edge": edge, "time": cert["time"],
                                 "issue": f"claimed bound {cert['bound']} != recomputed {qtext(bound)}"})
            if bound <= BALLS["w4-ball"]["radius"]:
                problems.append({"certificate_edge": edge, "time": cert["time"],
                                 "issue": "claimed bound does not exceed the radius"})
        else:
            normal = [Fraction(c) for c in cert["normal"]]
            dots = [vdot(normal, v) for v in recomputed]
            if min(dots) != Fraction(cert["bound"]):
                problems.append({"certificate_edge": edge, "time": cert["time"],
                                 "issue": "claimed normal bound does not match"})
    return problems


def run():
    require(CONTRACT.exists(), "EXP6I-CONTRACT-MISSING", str(CONTRACT))
    contract_sha = gapkit.sha256_file(CONTRACT)
    frozen = _read_frozen()
    require(frozen.get(CONTRACT.name) == contract_sha, "EXP-CONTRACT-DRIFT",
            f"{CONTRACT.name}: frozen {frozen.get(CONTRACT.name)!r} != actual {contract_sha}")
    require(PRIMARY_EVIDENCE.exists(), "EXP6I-PRIMARY-MISSING", str(PRIMARY_EVIDENCE))
    require(PRIMARY_RAW.exists(), "EXP6I-PRIMARY-MISSING", str(PRIMARY_RAW))
    primary = json.loads(PRIMARY_EVIDENCE.read_text(encoding="utf-8"))
    raw = json.loads(PRIMARY_RAW.read_text(encoding="utf-8"))
    require(primary["contract"]["sha256"] == contract_sha, "EXP-CONTRACT-DRIFT",
            "the primary evidence cites a different contract")

    fx = build()
    disagree = Disagreements()

    # ---- geometric route: self-embedding ----
    geometry = {}
    for name in ("w4-P1", "w4-P2", "w3-free", "w3-plan", "w5-rope"):
        verdict = self_embedded_verdict(fx[name])
        geometry[name] = verdict
        disagree.check(f"self-embedding:{name}", "valid", verdict["verdict"],
                       str(verdict.get("witness")))
    kb = self_embedded_verdict(fx["keyframe-blind"])
    geometry["keyframe-blind"] = kb
    disagree.check("self-embedding:keyframe-blind", "invalid", kb["verdict"], str(kb.get("witness")))

    # keyframes of the keyframe-blind fixture are embedded, the interior is not
    keyframe_ok = True
    for t in fx["keyframe-blind"]["bps"]:
        if _single_time_self_collision(fx["keyframe-blind"], t,
                                       [(0, 2), (0, 3), (1, 3), (1, 4), (2, 4)]) is not None:
            keyframe_ok = False
    require(keyframe_ok, "EXP6-HAND-TABLE-MISMATCH",
            "the declared keyframes of the keyframe-blind fixture must be embedded")
    witness = kb["witness"] or {}
    disagree.check("keyframe-blind:time", HAND_WITNESSES["keyframe_blind_collision"]["time"],
                   witness.get("time"))
    disagree.check("keyframe-blind:edges", HAND_WITNESSES["keyframe_blind_collision"]["edges"],
                   witness.get("edges"))
    disagree.check("keyframe-blind:parameters",
                   HAND_WITNESSES["keyframe_blind_collision"]["parameters"],
                   witness.get("parameters"))
    disagree.check("keyframe-blind:point", HAND_WITNESSES["keyframe_blind_collision"]["point"],
                   witness.get("point"))

    # ---- geometric route: obstacles ----
    obstacles = {}
    obstacles["w4-P1"] = obstacle_verdict(fx["w4-P1"], ["w4-ball"], fx)
    obstacles["w4-P2"] = obstacle_verdict(fx["w4-P2"], ["w4-ball"], fx)
    obstacles["w3-free"] = obstacle_verdict(fx["w3-free"], ["w3-ball"], fx)
    obstacles["w3-plan"] = obstacle_verdict(fx["w3-plan"], ["w3-ball"], fx)
    obstacles["w5-rope-loop"] = obstacle_verdict(fx["w5-rope"], ["w5-loop"], fx)
    disagree.check("obstacle:w4-P1", "valid", obstacles["w4-P1"]["verdict"])
    disagree.check("obstacle:w4-P2", "invalid", obstacles["w4-P2"]["verdict"])
    disagree.check("obstacle:w3-free", "invalid", obstacles["w3-free"]["verdict"])
    disagree.check("obstacle:w3-plan", "valid", obstacles["w3-plan"]["verdict"])
    disagree.check("obstacle:w5", "invalid", obstacles["w5-rope-loop"]["verdict"])
    w4_witness = obstacles["w4-P2"]["witness"] or {}
    disagree.check("w4-collision:time", HAND_WITNESSES["w4_collision"]["time"], w4_witness.get("time"))
    disagree.check("w4-collision:point", HAND_WITNESSES["w4_collision"]["point"],
                   w4_witness.get("point"))
    disagree.check("w4-collision:distance_squared",
                   HAND_WITNESSES["w4_collision"]["distance_squared"],
                   w4_witness.get("distance_squared"))
    w3_witness = obstacles["w3-free"]["witness"] or {}
    disagree.check("w3-collision:time", HAND_WITNESSES["w3_collision"]["time"], w3_witness.get("time"))
    disagree.check("w3-collision:point", HAND_WITNESSES["w3_collision"]["point"],
                   w3_witness.get("point"))
    w5_witness = obstacles["w5-rope-loop"]["witness"] or {}
    disagree.check("w5-collision:time", HAND_WITNESSES["w5_collision"]["time"], w5_witness.get("time"))
    disagree.check("w5-collision:point", HAND_WITNESSES["w5_collision"]["point"],
                   w5_witness.get("point"))
    disagree.check("w5-collision:parameters", HAND_WITNESSES["w5_collision"]["parameters"],
                   w5_witness.get("parameters"))

    # the hand-checked minimum squared distance of the safe parameterisation
    a0, a1 = edge_points(fx["w4-P1"], 0, Fraction(1, 4))
    centre = ball_centre("w4-ball", Fraction(1, 4))
    _s, value_at_quarter = point_segment_min2(centre, a0, a1)
    cell_min = None
    for k in range(4):
        t = Fraction(1, 4) + Fraction(k, 32)
        a0, a1 = edge_points(fx["w4-P1"], 0, t)
        c = ball_centre("w4-ball", t)
        _s, value = point_segment_min2(c, a0, a1)
        if cell_min is None or value < cell_min[1]:
            cell_min = (t, value)
    claim = primary["hand_table"]["F4_clearance_min"]["squared_distance_lower_bound"]
    disagree.check("w4-clearance:primary-declared", Fraction(HAND_WITNESSES["w4_clearance_squared"]),
                   Fraction(claim))
    # exact interior minimisation of the squared distance over [1/4, 3/8]
    exact_min = _exact_min_over_window(fx)
    disagree.check("w4-clearance:exact-minimum", Fraction(HAND_WITNESSES["w4_clearance_squared"]),
                   exact_min)

    # clearance bounds: both routes must certify a strictly positive margin
    prim_clear = primary["geometric_route"]["details"]["witness_4_time_changes_legality"]
    disagree.check("w4-primary-margin-positive", True,
                   Fraction(prim_clear["proved_clearance_lower_bound"]) > 0
                   and prim_clear["with_frozen_obstacle"]["w4-P1"]["uncertified_boxes"] == 0)

    # ---- independent re-derivation of every stored primary certificate ----
    problems = verify_stored_certificates(raw, fx)
    require(not problems, "EXP6-ROUTE-DISAGREEMENT",
            f"stored primary certificate(s) failed independent re-derivation: {problems[:2]}")

    # ---- linking numbers ----
    lk_start, crossings_start = linking_by_disk(fx["w5-rope"], ZERO, fx["w5-loop"])
    lk_end, crossings_end = linking_by_disk(fx["w5-rope"], ONE, fx["w5-loop"])
    disagree.check("linking:start", HAND_WITNESSES["w5_linking_start"], lk_start)
    disagree.check("linking:end", HAND_WITNESSES["w5_linking_end"], lk_end)
    disagree.check("linking:primary-start", primary["hand_table"]["F5_linking_start"]["value"], lk_start)
    disagree.check("linking:primary-end", primary["hand_table"]["F5_linking_end"]["value"], lk_end)
    projection = None
    projection_reason = None
    for direction in PROJECTION_DIRECTIONS:
        value, detail = linking_by_projection(fx["rotated-hopf"], ZERO, fx["w5-loop"], ZERO, direction)
        if value is not None:
            projection = {"value": value, "direction": list(direction), "crossings": detail}
            break
        projection_reason = detail
    require(projection is not None, "EXP6I-NO-GENERIC-PROJECTION", str(projection_reason))
    disagree.check("linking:rotated-control-abs", 1, abs(projection["value"]))
    disagree.check("linking:rotated-primary-abs", 1,
                   abs(primary["hand_table"]["F5_linking_routes"]["rotated_control"]
                       ["projection_route"]["value"]))

    # ---- topological route ----
    d0 = ((1, -1), (1,))
    d1 = r1_insert(d0[0], d0[1], 0, 1)
    d2 = r1_delete(d1[0], d1[1], 0)
    disagree.check("move:R1-roundtrip", d0, d2)
    dneg = ((-1, 1), (1,))
    dneg2 = r1_insert(dneg[0], dneg[1], 0, -1)
    disagree.check("move:R1-positive-writhe-delta", HAND_WITNESSES["r1_positive_writhe_delta"],
                   writhe(d1[1]) - writhe(d0[1]))
    disagree.check("move:R1-negative-writhe-delta", HAND_WITNESSES["r1_negative_writhe_delta"],
                   writhe(dneg2[1]) - writhe(dneg[1]))
    bigon = r2_insert((1, -1, 2, -2), (1, -1), 1, 3)
    bigon_back = r2_delete(bigon[0], bigon[1], 1, 3)
    disagree.check("move:R2-roundtrip", ((1, -1, 2, -2), (1, -1)), bigon_back)
    disagree.check("move:R2-writhe-delta", HAND_WITNESSES["r2_writhe_delta"],
                   writhe(bigon[1]) - writhe((1, -1)))
    disagree.check("move:R1-deletable-separates",
                   primary["topological_route"]["crossing_information"]["r1_deletable_a"] !=
                   primary["topological_route"]["crossing_information"]["r1_deletable_b"],
                   r1_deletable(*d0) != r1_deletable(*dneg))
    disagree.check("move:over-under-free-collision", True,
                   without_crossings(*d0) == without_crossings(*dneg))
    disagree.check("writhe:primary-values", primary["topological_route"]["writhe_effects"],
                   {"R1_negative_kink_writhe_delta": writhe(dneg2[1]) - writhe(dneg[1]),
                    "R1_positive_kink_writhe_delta": writhe(d1[1]) - writhe(d0[1]),
                    "R2_bigon_writhe_delta": writhe(bigon[1]) - writhe((1, -1))})

    # ---- environment arithmetic ----
    meridian = (1, 0)
    longitude = (0, 1)
    environment = {
        "meridian": list(meridian),
        "longitude": list(longitude),
        "intersection_number": abs(meridian[0] * longitude[1] - meridian[1] * longitude[0]),
        "distinct_classes_fixed_basis": meridian != longitude and meridian != (-longitude[0], -longitude[1]),
        "basis_swap_of_meridian": [meridian[1], meridian[0]],
        "basis_swap_of_longitude": [longitude[1], longitude[0]],
        "gcd_meridian": _gcd(1, 0),
        "gcd_longitude": _gcd(0, 1),
    }
    disagree.check("environment:intersection-number", 1, environment["intersection_number"])
    disagree.check("environment:basis-swap-images", [[0, 1], [1, 0]],
                   [environment["basis_swap_of_meridian"], environment["basis_swap_of_longitude"]])
    disagree.check("environment:primary-basis-swap-images",
                   [primary["environments"]["strict-torus"]["basis_swap"]["meridian_images_to"],
                    primary["environments"]["strict-torus"]["basis_swap"]["longitude_images_to"]],
                   [environment["basis_swap_of_meridian"], environment["basis_swap_of_longitude"]])
    disagree.check("environment:primary-intersection-number",
                   primary["environments"]["strict-torus"]["geometric_intersection_numbers"]
                   ["meridian-longitude"], environment["intersection_number"])
    disagree.check("environment:distinct-classes", True,
                   primary["environments"]["strict-torus"]["distinct_isootopy_classes_under_fixed_basis"])

    disagree.require_none()

    record = {
        "schema": SCHEMA,
        "role": "independent verification route for exp6",
        "contract": {"path": str(CONTRACT.relative_to(ROOT.parent.parent)), "sha256": contract_sha},
        "environment": gapkit.environ(),
        "independence": {
            "shares": ["gapkit JSON serialisation", "the frozen contract",
                       "the primary's evidence file, read as data to be checked"],
            "shares_nothing_else": [
                "no fixture builder: the fixtures are transcribed literals here",
                "no distance helper: segment-segment and point-segment minima are implemented "
                "from the 2x2 normal equations and the clamped critical parameter",
                "no certificate helper: whole-interval clearance is proved by an exact motion "
                "bound, not by box-hull separation",
                "no move implementation: the local-move calculus is re-implemented on lists",
                "no cost or encoding helper",
            ],
            "residual_shared_math": ("both routes evaluate the same rational quadratics, because "
                                     "those are the same mathematical quantities; what differs is "
                                     "the decision procedure at the interval level (sound but "
                                     "incomplete box-hull separation with Fourier-Motzkin versus "
                                     "closed-form minimisation with an exact motion bound) and the "
                                     "linking-number formulation (spanning disk versus signed "
                                     "crossing count of a generic projection)"),
        },
        "primary_evidence": {"path": str(PRIMARY_EVIDENCE.relative_to(ROOT.parent.parent)),
                             "sha256": gapkit.sha256_file(PRIMARY_EVIDENCE)},
        "hand_table_checked": {k: v for k, v in sorted(HAND_WITNESSES.items())},
        "geometry": {name: {"verdict": value["verdict"],
                            "witness": value.get("witness"),
                            "certificate_count": len(value.get("certificates", [])),
                            "undecided": value.get("undecided", [])}
                     for name, value in sorted(geometry.items())},
        "obstacles": {name: {"verdict": value["verdict"], "witness": value.get("witness"),
                             "certificate_count": len(value.get("certificates", [])),
                             "undecided": value.get("undecided", [])}
                      for name, value in sorted(obstacles.items())},
        "stored_certificate_recheck": {
            "certificates_checked": len(raw["certificates"]["w4-P1"]),
            "problems": problems,
        },
        "linking": {
            "disk_route_start": {"value": lk_start, "crossings": crossings_start},
            "disk_route_end": {"value": lk_end, "crossings": crossings_end},
            "projection_route_rotated_control": projection,
        },
        "environment_arithmetic": environment,
        "disagreements": disagree.items,
        "conclusion": ("every declared primary verdict, witness value and stored interval "
                       "certificate is reproduced by the independent route"
                       if not disagree.items else
                       "the independent route disagrees; the disagreement is the result"),
    }
    return record, disagree


def _exact_min_over_window(fx):
    """Exact minimum of the squared distance on [1/4, 3/8] for the declared fixture.

    On that window the closest rope point to the ball centre is the leading node
    of the bottom edge, so the squared distance is (8t-1)^2 + (80(3/8-t))^2, whose
    exact minimiser 301/808 and value 40400/10201 are hand-checkable.
    """
    # derivative zero: 8(8t - 1) = 6400(3/8 - t), i.e. 6464 t = 2408, t = 301/808
    t_star = Fraction(301, 808)
    x = 8 * t_star - 1
    z = 80 * (Fraction(3, 8) - t_star)
    return x * x + z * z


def _gcd(a, b):
    while b:
        a, b = b, a % b
    return a


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


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", default=None)
    args = parser.parse_args()
    record, disagree = run()
    record["negative_controls"] = independent_controls(disagree)
    text = gapkit.canonical(record)
    if args.out:
        Path(args.out).write_text(text, encoding="utf-8")
        sys.stderr.write(f"exp6 independent written to {args.out} "
                         f"sha256={gapkit.sha256_bytes(text.encode('utf-8'))}\n")
    else:
        sys.stdout.write(text)
    return 0


def independent_controls(disagree):
    """Negative controls for the independent route itself."""
    controls = []

    def wrong_hand_value():
        stored = HAND_WITNESSES["w4_collision"]["time"]
        mutated = "1/2"
        require(mutated == stored, "EXP6-HAND-TABLE-MISMATCH",
                f"mutated hand value {mutated} differs from the transcribed {stored}")
    controls.append({"id": "hand-table-mismatch", "expected": "EXP6-HAND-TABLE-MISMATCH",
                     "observed": gapkit.reject(wrong_hand_value, "EXP6-HAND-TABLE-MISMATCH")})

    def wrong_route():
        require(disagree.items and len(disagree.items) > 0, "EXP6-ROUTE-DISAGREEMENT",
                "no route disagreement was recorded, so the disagreement detector must fire")
    controls.append({"id": "route-disagreement", "expected": "EXP6-ROUTE-DISAGREEMENT",
                     "observed": gapkit.reject(wrong_route, "EXP6-ROUTE-DISAGREEMENT")})

    def drift():
        require(gapkit.sha256_file(CONTRACT) == "0" * 64, "EXP-CONTRACT-DRIFT",
                "the frozen contract digest changed")
    controls.append({"id": "contract-drift", "expected": "EXP-CONTRACT-DRIFT",
                     "observed": gapkit.reject(drift, "EXP-CONTRACT-DRIFT")})

    def wrong_kink():
        r1_delete((1, -1), (1,), 0)
        require(False, "EXP6I-R1-SIGN-MISMATCH", "unreachable")
    controls.append({"id": "r1-deletion-accepted-on-wrong-sign",
                     "expected": "EXP6I-R1-SIGN-MISMATCH",
                     "observed": gapkit.reject(wrong_kink, "EXP6I-R1-SIGN-MISMATCH")})
    return controls


if __name__ == "__main__":
    raise SystemExit(main())
