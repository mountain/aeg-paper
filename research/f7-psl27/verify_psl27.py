#!/usr/bin/env python3
"""Finite calibration: PGL(2,7), PSL(2,7), the F_7 projective line and Paper IV.

Builds PGL(2,7) and PSL(2,7) as permutations of P^1(F_7) (8 points), computes
their element orders, conjugacy classes and Sylow counts, and checks the
orbit-stabilizer correspondences used in the note:

  * 8 projective points             <-> 8 Sylow 7-subgroups of PSL
  * 56 ordered pairs of points      <-> 56 order-3 elements (PGL and PSL)
  * 21 Fano flags                   <-> 21 involutions / 21 Sylow 2-subgroups
  * 42 ordered pairs of Fano points <-> 42 order-4 elements (size only; the
    stabilizer is V4 while the centralizer is C4, so no PSL-set isomorphism)
  * 24 heptagon cosets              <-> 24 cosets of a Sylow 7-subgroup

Every expected value is asserted, so the script exits non-zero when a check
fails. `--verify-evidence` regenerates the JSON and compares it byte for byte
with the committed evidence file.

Run: python3 verify_psl27.py [out.json] [--verify-evidence]
"""
import itertools
import json
import os
import sys

P = 7
INF = 7


def fail(message):
    raise SystemExit("check failed: " + message)


def check(name, condition, detail=None):
    if not condition:
        fail(name + ("" if detail is None else " (%r)" % (detail,)))


def inv(x):
    return pow(x, P - 2, P)


def act(M, x):
    a, b, c, d = M
    if x == INF:
        return INF if c % P == 0 else (a * inv(c)) % P
    den = (c * x + d) % P
    if den == 0:
        return INF
    return ((a * x + b) * inv(den)) % P


def perm(M):
    return tuple(act(M, x) for x in range(8))


def compose(p, q):
    return tuple(p[q[x]] for x in range(8))


def inverse(p):
    out = [0] * 8
    for i, v in enumerate(p):
        out[v] = i
    return tuple(out)


def order(p):
    e = tuple(range(8))
    q = e
    for k in range(1, 200):
        q = compose(p, q)
        if q == e:
            return k
    return None


def cyclic(p):
    e = tuple(range(8))
    out = {e}
    q = p
    while q != e:
        out.add(q)
        q = compose(p, q)
    return frozenset(out)


def closure(gens):
    elems = {tuple(range(8))}
    frontier = [tuple(range(8))]
    gens = list(gens)
    while frontier:
        x = frontier.pop()
        for g in gens:
            y = compose(g, x)
            if y not in elems:
                elems.add(y)
                frontier.append(y)
    return frozenset(elems)


def conjugates(H, g):
    gi = inverse(g)
    return frozenset(compose(compose(g, h), gi) for h in H)


def conjugacy_classes(G):
    classes = []
    seen = set()
    for g in G:
        if g in seen:
            continue
        cl = {compose(compose(h, g), inverse(h)) for h in G}
        seen |= cl
        classes.append({"order": order(g), "size": len(cl)})
    classes.sort(key=lambda c: (c["order"], c["size"]))
    return classes


def build_group(matrix_predicate, quotient):
    perms = set()
    for a, b, c, d in itertools.product(range(P), repeat=4):
        if not matrix_predicate(a, b, c, d):
            continue
        M = (a, b, c, d)
        perms.add(perm(M))
    if quotient:
        # quotient by +-I: already done by taking permutations; ensure count
        pass
    return sorted(perms)


def main(argv):
    out_path = "/tmp/psl27.json"
    verify = False
    for arg in argv:
        if arg == "--verify-evidence":
            verify = True
        else:
            out_path = arg

    # SL(2,7) modulo +-I = PSL(2,7)
    sl = []
    for a, b, c, d in itertools.product(range(P), repeat=4):
        if (a * d - b * c) % P != 1:
            continue
        M = (a, b, c, d)
        N = tuple((-v) % P for v in M)
        if M <= N:
            sl.append(perm(M))
    G = sorted(set(sl))
    check("|PSL(2,7)| = 168", len(G) == 168, len(G))

    by_order = {}
    for g in G:
        by_order.setdefault(order(g), []).append(g)
    check("PSL order counts", {k: len(v) for k, v in by_order.items()} ==
          {1: 1, 2: 21, 3: 56, 4: 42, 7: 48}, {k: len(v) for k, v in by_order.items()})
    classes = conjugacy_classes(G)
    check("PSL class multiset", sorted((c["order"], c["size"]) for c in classes) ==
          [(1, 1), (2, 21), (3, 56), (4, 42), (7, 24), (7, 24)], classes)

    pairs = {(g[0], g[1]) for g in G}
    check("PSL 2-transitive on 8 points", len(pairs) == 56, len(pairs))
    stab_pair = frozenset(g for g in G if g[0] == 0 and g[1] == 1)
    check("ordered-pair stabilizer order 3", len(stab_pair) == 3, len(stab_pair))
    s3 = next(cyclic(g) for g in G if order(g) == 3)
    check("stabilizer conjugate to a Sylow 3",
          any(conjugates(stab_pair, g) == s3 for g in G))

    def sylow(p):
        return {cyclic(g) for g in G if order(g) == p}

    s3s = sylow(3)
    s7 = sylow(7)
    s2s = set()
    for g in G:
        if order(g) in (2, 4):
            for h in G:
                if order(h) in (2, 4):
                    H = closure([g, h])
                    if len(H) == 8:
                        s2s.add(H)
    check("PSL Sylow counts", (len(s2s), len(s3s), len(s7)) == (21, 28, 8),
          (len(s2s), len(s3s), len(s7)))

    point_stab = frozenset(g for g in G if g[0] == 0)
    s7_one = sorted(s7, key=lambda H: tuple(sorted(H)))[0]
    norm7 = frozenset(g for g in G if conjugates(s7_one, g) == s7_one)
    check("point stabilizer order 21", len(point_stab) == 21, len(point_stab))
    check("Sylow-7 normalizer order 21", len(norm7) == 21, len(norm7))
    check("point stabilizer conjugate to Sylow-7 normalizer",
          any(conjugates(point_stab, g) == norm7 for g in G))
    check("24 cosets of a Sylow 7", len({frozenset(compose(g, h) for h in s7_one)
                                         for g in G}) == 24)

    # centralizer of an order-4 element
    g4 = next(g for g in G if order(g) == 4)
    cent4 = frozenset(h for h in G if compose(h, g4) == compose(g4, h))
    check("order-4 centralizer is C4",
          len(cent4) == 4 and sorted(order(h) for h in cent4) == [1, 2, 4, 4],
          (len(cent4), sorted(order(h) for h in cent4)))

    # GL(3,2) on the Fano plane: flags and their stabilizer
    vecs = [v for v in itertools.product((0, 1), repeat=3) if any(v)]
    mats = []
    for rows in itertools.product(vecs, repeat=3):
        a, b, c = rows
        det = (a[0] * (b[1] * c[2] ^ b[2] * c[1])
               ^ a[1] * (b[0] * c[2] ^ b[2] * c[0])
               ^ a[2] * (b[0] * c[1] ^ b[1] * c[0]))
        if det:
            mats.append(rows)

    def apply(M, v):
        return tuple(sum(M[i][j] * v[j] for j in range(3)) % 2 for i in range(3))

    F = sorted({tuple(vecs.index(apply(M, v)) for v in vecs) for M in mats})
    check("|GL(3,2)| = 168", len(F) == 168, len(F))

    def order7(p):
        e = tuple(range(7))
        q = e
        for k in range(1, 50):
            q = tuple(p[x] for x in q)
            if q == e:
                return k
        return None

    planes = []
    for combo in itertools.combinations(vecs, 3):
        a, b, c = combo
        if (a[0] ^ b[0] ^ c[0], a[1] ^ b[1] ^ c[1], a[2] ^ b[2] ^ c[2]) == (0, 0, 0):
            planes.append(frozenset(vecs.index(v) for v in combo))
    flags = [(vecs.index(v), P) for P in planes for v in vecs
             if vecs.index(v) in P]
    check("7 Fano points, 7 lines, 21 flags",
          (len(vecs), len(planes), len(flags)) == (7, 7, 21))
    v0, P0 = flags[0]
    flag_stab = [g for g in F if g[v0] == v0 and frozenset(g[x] for x in P0) == P0]
    check("flag stabilizer order 8", len(flag_stab) == 8, len(flag_stab))
    check("flag stabilizer is a Sylow 2",
          sorted(order7(g) for g in flag_stab) == [1, 2, 2, 2, 2, 2, 4, 4])

    # canonical Sylow 2 <-> involution bijection via centers
    e8 = tuple(range(8))
    involutions = {g for g in G if order(g) == 2}
    centers = set()
    for S in s2s:
        central = [h for h in S if h != e8 and all(compose(h, s) == compose(s, h) for s in S)]
        check("Sylow 2 center has one nonidentity element", len(central) == 1, len(central))
        centers.add(central[0])
    check("21 Sylow 2 subgroups biject with 21 involutions",
          centers == involutions, len(centers))

    # Fano ordered-pair stabilizer (computed, not hard-coded)
    i0, i1 = vecs.index((1, 0, 0)), vecs.index((0, 1, 0))
    fano_pair_stab = [g for g in F if g[i0] == i0 and g[i1] == i1]
    pair_orders = sorted(order7(g) for g in fano_pair_stab)
    pair_type = ("V4" if len(fano_pair_stab) == 4 and pair_orders == [1, 2, 2, 2]
                 else "other")
    check("Fano ordered-pair stabilizer is V4",
          pair_type == "V4", (len(fano_pair_stab), pair_orders))

    # PGL(2,7)
    pgl = sorted({perm((a, b, c, d))
                  for a, b, c, d in itertools.product(range(P), repeat=4)
                  if (a * d - b * c) % P != 0})
    check("|PGL(2,7)| = 336", len(pgl) == 336, len(pgl))
    pgl_classes = conjugacy_classes(pgl)
    check("PGL class multiset",
          sorted((c["order"], c["size"]) for c in pgl_classes) ==
          [(1, 1), (2, 21), (2, 28), (3, 56), (4, 42), (6, 56), (7, 48),
           (8, 42), (8, 42)],
          pgl_classes)
    pgl_pairs = {(g[0], g[1]) for g in pgl}
    check("PGL transitive on 56 ordered pairs", len(pgl_pairs) == 56, len(pgl_pairs))
    pgl_stab = frozenset(g for g in pgl if g[0] == 0 and g[1] == 1)
    check("PGL ordered-pair stabilizer order 6", len(pgl_stab) == 6, len(pgl_stab))
    pgl3 = next(cyclic(g) for g in pgl if order(g) == 3)
    cent3 = frozenset(h for h in pgl if compose(h, next(g for g in pgl3 if order(g) == 3))
                      == compose(next(g for g in pgl3 if order(g) == 3), h))
    check("PGL order-3 centralizer order 6", len(cent3) == 6, len(cent3))
    check("PGL stabilizer conjugate to order-3 centralizer",
          any(conjugates(pgl_stab, g) == cent3 for g in pgl))

    ev = {
        "pgl": {
            "order": len(pgl),
            "class_multiset": sorted((c["order"], c["size"]) for c in pgl_classes),
            "ordered_pair_stabilizer_order": len(pgl_stab),
            "order3_centralizer_order": len(cent3),
            "ordered_pair_and_order3_centralizer_conjugate": True,
        },
        "psl": {
            "order": len(G),
            "element_order_counts": {str(k): len(v) for k, v in sorted(by_order.items())},
            "class_multiset": sorted((c["order"], c["size"]) for c in classes),
            "two_transitive_on_8_points": True,
            "ordered_pair_stabilizer_order": len(stab_pair),
            "ordered_pair_stabilizer_is_c3": True,
            "sylow_counts": {"2": len(s2s), "3": len(s3s), "7": len(s7)},
            "point_stabilizer_order": len(point_stab),
            "sylow7_normalizer_order": len(norm7),
            "cosets_of_sylow7": 24,
            "order4_centralizer_order": len(cent4),
            "order4_centralizer_element_orders": sorted(order(h) for h in cent4),
            "sylow2_centers_biject_involutions": True,
        },
        "fano": {
            "points": len(vecs), "lines": len(planes), "flags": len(flags),
            "flag_stabilizer_order": len(flag_stab),
            "flag_stabilizer_element_orders": sorted(order7(g) for g in flag_stab),
            "ordered_pair_stabilizer_order": len(fano_pair_stab),
            "ordered_pair_stabilizer_element_orders": pair_orders,
            "ordered_pair_stabilizer_type": pair_type,
        },
        "status": {
            "8_points_and_sylow7": "standard consequence of orbit-stabilizer plus the computed conjugacy",
            "56_pairs_and_order3": "standard consequence of orbit-stabilizer plus the computed conjugacy",
            "21_flags_and_involutions": "classical GL(3,2) flag action; the canonical Sylow-2 center map gives the involution bijection (computed here)",
            "42_pairs_and_order4": "not isomorphic: V4 ordered-pair stabilizer against C4 order-4 centralizer (both computed)",
            "42_six_leaf_trees": "open; no action constructed",
        },
    }
    text = json.dumps(ev, indent=2, sort_keys=True) + "\n"
    if verify:
        with open(out_path, "r", encoding="utf-8") as f:
            committed = f.read()
        check("evidence matches the committed file", text == committed)
        print("evidence verified:", out_path)
        return
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text)
    print(json.dumps({"pgl_order": len(pgl), "psl_order": len(G),
                      "flags": len(flags), "flag_stabilizer": len(flag_stab)}, indent=2))
    print("wrote", out_path)


if __name__ == "__main__":
    main(sys.argv[1:])
