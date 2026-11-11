#!/usr/bin/env python3
"""Exact rational witnesses for note 09: boundary transport and composition.

No third-party packages. Optional PAL audit uses the pinned relations reader
from note 08; no training or probabilistic rollout of the PAL model is done.
"""
from collections import defaultdict
from fractions import Fraction as F
from functools import reduce
from itertools import product
from pathlib import Path
import argparse
import json
import math


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def X(p, s):
    x, y = p
    return x-s*y, y


def Y(p, k):
    require(k > 0, "positive multiplier required")
    x, y = p
    return x, y/k


def face_X(h, s):
    u, v, w = h
    return u, v+s*u, w


def face_Y(h, k):
    require(k > 0, "positive multiplier required")
    u, v, w = h
    return u, k*v, w


def evaluate(h, p):
    return h[0]*p[0]+h[1]*p[1]+h[2]


def assignment(p):
    return -p[0]/p[1]


def loop(p, s, k, b1, b2):
    # Temporal order: X_(b1*s), Y_k, X_(-k*b2*s), Y_(1/k).
    return Y(X(Y(X(p, b1*s), k), -k*b2*s), 1/k)


def distribution(values):
    ans = defaultdict(F)
    for value, mass in values:
        ans[value] += mass
    return dict(ans)


def render_law(law):
    return {str(k): str(v) for k, v in sorted(law.items())}


def tv(p, q):
    return sum(abs(a-b) for a, b in zip(p, q))/2


def mat(rows):
    return tuple(tuple(map(F, row)) for row in rows)


def matvec(p, v):
    return tuple(sum(a*b for a, b in zip(row, v)) for row in p)


def rowmat(v, p):
    return tuple(sum(v[i]*p[i][j] for i in range(len(v)))
                 for j in range(len(p[0])))


def dot(a, b):
    return sum(x*y for x, y in zip(a, b))


def rank(vectors):
    if not vectors:
        return 0
    a = [list(v) for v in vectors]
    pivot_row = 0
    for col in range(len(a[0])):
        candidate = next((i for i in range(pivot_row, len(a)) if a[i][col]), None)
        if candidate is None:
            continue
        a[pivot_row], a[candidate] = a[candidate], a[pivot_row]
        scale = a[pivot_row][col]
        a[pivot_row] = [x/scale for x in a[pivot_row]]
        for i in range(pivot_row+1, len(a)):
            scale = a[i][col]
            a[i] = [x-scale*y for x, y in zip(a[i], a[pivot_row])]
        pivot_row += 1
        if pivot_row == len(a):
            break
    return pivot_row


def invariant_tests(seeds, operators):
    """Retain original test vectors and words, not only reduced row vectors."""
    basis = []
    for name, v in seeds:
        if rank([x[1] for x in basis]+[v]) > len(basis):
            basis.append((name, v))
    dimensions = [len(basis)]
    while True:
        before = len(basis)
        for old_name, v in list(basis):
            for op_name, p in operators:
                candidate = matvec(p, v)
                if rank([x[1] for x in basis]+[candidate]) > len(basis):
                    basis.append((op_name+" "+old_name, candidate))
        if len(basis) == before:
            break
        dimensions.append(len(basis))
    require(rank([v for _, v in basis]) == len(basis), "dependent test basis")
    for _, p in operators:
        for _, v in basis:
            require(rank([x[1] for x in basis]+[matvec(p, v)]) == len(basis),
                    "test space is not invariant")
    return basis, dimensions


def annihilates(d, basis):
    return all(dot(d, v) == 0 for _, v in basis)


def rational_witnesses():
    points = [tuple(map(F, p)) for p in [(0, 1), (2, 3), (-1, 2)]]
    faces = [tuple(map(F, h)) for h in [(1, 0, 0), (1, 2, -3), (0, 1, -2)]]
    shifts = list(map(F, [-2, 0, 1]))+[F(1, 3)]
    scales = [F(1, 2), F(1), F(2), F(3, 2)]
    port_cases = 0
    for p, h, s, k in product(points, faces, shifts, scales):
        require(evaluate(face_X(h, s), X(p, s)) == evaluate(h, p), "X face")
        require(evaluate(face_Y(h, k), Y(p, k)) == evaluate(h, p), "Y face")
        require(Y(X(p, s), k) == X(Y(p, k), k*s), "AM point relation")
        require(face_Y(face_X(h, s), k) == face_X(face_Y(h, k), k*s),
                "AM transported-face relation")
        result_h = face_Y(face_X(face_Y(face_X(h, s), k), -k*s), 1/k)
        require(result_h == h and loop(p, s, k, F(1), F(1)) == p,
                "closed word lost point or face")
        port_cases += 1
    for n in [2, 4, 16, 256]:
        p = (-F(1, n), F(1))
        moved = X(p, F(-2))
        require(evaluate((F(1), F(0), F(0)), moved) > 0,
                "fixed-chart reset example")
        require(evaluate((F(1), F(-2), F(0)), moved) < 0,
                "transported negative port was not preserved")

    return _finish_witnesses(points, shifts, scales, port_cases)


def _finish_witnesses(points, shifts, scales, port_cases):
    closure_cases = 0
    for p, s, k, b1, b2 in product(points, shifts, scales, [F(1), F(2)], [F(1), F(2)]):
        output = loop(p, s, k, b1, b2)
        expected = (p[0]+s*(b2-b1)*p[1], p[1])
        require(output == expected, "closed-word correlation residual")
        if b1 == b2:
            require(output == p, "persistent branch did not close")
        closure_cases += 1
    p = (F(0), F(1))
    shared = distribution((assignment(loop(p, F(1), F(2), b, b)), F(1, 2))
                          for b in [F(1), F(2)])
    reset = distribution((assignment(loop(p, F(1), F(2), b, c)), F(1, 4))
                         for b, c in product([F(1), F(2)], repeat=2))
    require(shared == {F(0): F(1)}, "shared closure law")
    require(reset == {F(-1): F(1, 4), F(0): F(1, 2), F(1): F(1, 4)},
            "reset closure law")
    product_shared = distribution(((b*(1/b)), F(1, 2)) for b in [F(1), F(2)])
    product_reset = distribution((b/c, F(1, 4))
                                 for b, c in product([F(1), F(2)], repeat=2))
    require(product_shared == {F(1): F(1)}, "shared product")
    require(product_reset == {F(1, 2): F(1, 4), F(1): F(1, 2), F(2): F(1, 4)},
            "independent product")

    states = list(product([0, 1], repeat=2))  # (visible value, hidden bit)
    P = mat([[int((b ^ h, h) == target) for target in states] for b, h in states])
    Q = mat([[int((b ^ 1, h) == target) for target in states] for b, h in states])
    C = mat([[int(b == o) for o in [0, 1]] for b, h in states])
    D = [mat([[int(i == j and states[i][0] == o) for j in range(4)]
              for i in range(4)]) for o in [0, 1]]
    seeds = [(f"D{o} 1", tuple(row[o] for row in C)) for o in [0, 1]]
    terminal, terminal_dims = invariant_tests(seeds, [("P", P)])
    trace, trace_dims = invariant_tests(seeds, [("P", P), ("D0", D[0]), ("D1", D[1])])
    require((len(terminal), len(trace)) == (3, 4), "terminal/trace dimension")
    eta_minus = tuple(map(F, [F(3, 4), F(1, 4), 0, 0]))
    eta_plus = tuple(map(F, [F(1, 4), F(3, 4), 0, 0]))
    require(rowmat(eta_minus, C) == rowmat(eta_plus, C), "current equality")
    reveal = tv(rowmat(rowmat(eta_minus, P), C), rowmat(rowmat(eta_plus, P), C))
    require(reveal == F(1, 2), "future terminal reveal")

    mu = (F(1, 2), F(0), F(1, 2), F(0))
    nu = (F(0), F(1, 2), F(0), F(1, 2))
    d = tuple(a-b for a, b in zip(mu, nu))
    require(annihilates(d, terminal) and not annihilates(d, trace),
            "terminal equivalence confused with trace equivalence")
    trace_mu, trace_nu = [], []
    for o0, o1 in product([0, 1], repeat=2):
        test = matvec(D[o0], matvec(P, seeds[o1][1]))
        trace_mu.append(dot(mu, test))
        trace_nu.append(dot(nu, test))
    require(tv(trace_mu, trace_nu) == 1, "two-observation trace witness")
    event = matvec(D[0], matvec(P, seeds[0][1]))
    require(dot(mu, event) == F(1, 2) and dot(nu, event) == 0,
            "00 trace-event probability")
    # Independent enumeration of all complete traces through eight steps.
    for n in range(9):
        laws = []
        for initial in [mu, nu]:
            paths = []
            for (b, h), mass in zip(states, initial):
                observations = [b]
                for _ in range(n):
                    b ^= h
                    observations.append(b)
                paths.append((tuple(observations), mass))
            laws.append(distribution(paths))
        require(sum(laws[0].values()) == sum(laws[1].values()) == 1, "trace mass")
        for final in [0, 1]:
            require(sum(w for t, w in laws[0].items() if t[-1] == final) == F(1, 2)
                    and sum(w for t, w in laws[1].items() if t[-1] == final) == F(1, 2),
                    "terminal marginal counterexample")
    safe, safe_dims = invariant_tests(seeds, [("Q", Q), ("D0", D[0]), ("D1", D[1])])
    require(len(safe) == 2 and annihilates((F(1), F(-1), F(0), F(0)), safe),
            "genuinely invisible hidden-bit control")
    # Pulling the gate a=1 back along repeated multiplication by 2.
    horizons = {}
    for L in [1, 2, 4, 8]:
        cuts = [F(1, 2**t) for t in range(L)]
        require(len(set(cuts)) == L and all(0 < a < 2 for a in cuts), "gate cuts")
        for t, a in enumerate(cuts):
            require(2**t*a == 1, "wrong pulled-back boundary")
        horizons[str(L)] = {"faces": L, "interval_cells_in_0_2": L+1}
    return {
        "status": "PASS", "arithmetic": "exact rational",
        "point_and_oriented_face_cases": port_cases,
        "AM_shared_and_reset_cases": closure_cases,
        "closed_word_shared_law": render_law(shared),
        "closed_word_independent_reset_law": render_law(reset),
        "binary_product_shared_law": render_law(product_shared),
        "binary_product_independent_law": render_law(product_reset),
        "future_tests": {
            "states": states, "transition_P": [[str(x) for x in row] for row in P],
            "terminal_dimensions": terminal_dims, "trace_dimensions": trace_dims,
            "terminal_basis": [{"word": w, "vector": list(map(str, v))} for w, v in terminal],
            "trace_basis": [{"word": w, "vector": list(map(str, v))} for w, v in trace],
            "current_invisible_next_terminal_TV": str(reveal),
            "all_terminal_marginals_equal_but_two_observation_trace_TV": "1",
            "trace_00_probability_mu_nu": ["1/2", "0"],
            "safe_control_dimensions": safe_dims,
            "independent_trace_enumeration_steps": 8},
        "finite_horizon_refinement": horizons,
        "refuted_shortcuts": [
            "fixed-chart sign equals transported side",
            "Scott-continuous relation maps preserve arithmetic word relations",
            "independent choices preserve a shared-parameter closed word",
            "current output equality ensures future output equality",
            "all terminal marginals determine the observation trace law",
            "a finite horizon arrangement automatically works at every horizon"]}


def canonical_oriented(coefficients):
    denominator = math.lcm(*(x.denominator for x in coefficients))
    integers = tuple(x.numerator*(denominator//x.denominator) for x in coefficients)
    divisor = reduce(math.gcd, integers)
    require(divisor > 0, "zero face equation")
    return tuple(x//divisor for x in integers)


def pal_faces(path):
    import verify_boundary_gluing as prior
    relations = prior.read_relations(path)
    faces = []
    for j, (mr, mi, b) in enumerate(relations):
        norm = mr*mr+mi*mi
        require(norm > 0, "PAL channel is not invertible")
        u, v = (mr-mi)/norm, (mr+mi)/norm
        w = -u*b[0]-v*b[1]
        # Exact polynomial identity h_j(F_j(a))=a_0+a_1, not point sampling.
        require(u*mr+v*mi == 1 and -u*mi+v*mr == 1
                and u*b[0]+v*b[1]+w == 0, "transported PAL face identity")
        faces.append(canonical_oriented((u, v, w)))
    unoriented = [h if next(x for x in h if x) > 0 else tuple(-x for x in h)
                  for h in faces]
    require(len(set(faces)) == len(set(unoriented)) == 32, "image faces coincide")
    require(all(h not in [(1, 1, 0), (-1, -1, 0)] for h in faces),
            "a channel preserves the original face")
    return {"status": "PASS", "source_repository": "mountain/dirac-belt",
            "source_commit": prior.gate.SOURCE_COMMIT,
            "source_path": "pal/relations.json", "source_blob": prior.RELATIONS_BLOB,
            "source_face": "a[0]+a[1]=0",
            "transport_formula": "h_j=h_source o F_j^{-1}",
            "nonzero_multipliers": 32, "distinct_oriented_faces": len(set(faces)),
            "distinct_unoriented_faces": len(set(unoriented)),
            "images_equal_to_source_face": 0,
            "face_equations": [{"channel": j, "coefficients_a0_a1_constant": list(map(str, h))}
                               for j, h in enumerate(faces)],
            "semantics": "exact rational PAL coefficients as in note 08; no runtime rounding",
            "scope": "algebraic transport of one source face; no claim about an intended multistep model interface"}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--relations", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    report = {"rational_witnesses": rational_witnesses()}
    if args.relations:
        report["frozen_face_transport"] = pal_faces(args.relations)
    text = json.dumps(report, ensure_ascii=False, indent=2)+"\n"
    if args.output:
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")


if __name__ == "__main__":
    main()
