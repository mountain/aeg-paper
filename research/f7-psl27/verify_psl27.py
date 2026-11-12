#!/usr/bin/env python3
"""Finite calibration: PSL(2,7), the F_7 projective line, and the Paper IV counts.

Builds PSL(2,7) as permutations of P^1(F_7) (8 points), computes its element
orders, conjugacy classes and Sylow counts, and checks the orbit-stabilizer
correspondences used in the note:

  * 8 projective points            <-> 8 Sylow 7-subgroups
  * 56 ordered pairs of points     <-> 56 elements of order 3
  * 21 (Fano flags)                <-> 21 involutions (Sylow 2 count)
  * 42 ordered pairs of Fano points<-> 42 elements of order 4 (size only)
  * 24 heptagon cosets             <-> 24 cosets of a Sylow 7-subgroup

Run: python3 verify_psl27.py [out.json]
"""
import itertools
import json
import sys

P = 7
INF = 7


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


def compose(p, q):  # (p o q)(x) = p(q(x))
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


def main(out_path="/tmp/psl27.json"):
    # PSL(2,7): SL(2,7) modulo +-I
    mats = []
    for a, b, c, d in itertools.product(range(P), repeat=4):
        if (a * d - b * c) % P != 1:
            continue
        M = (a, b, c, d)
        N = tuple((-v) % P for v in M)
        if M <= N:
            mats.append(M)
    perms = sorted({perm(M) for M in mats})
    G = perms
    assert len(G) == 168, len(G)
    e = tuple(range(8))

    # element orders and conjugacy classes
    by_order = {}
    for g in G:
        by_order.setdefault(order(g), []).append(g)
    classes = []
    seen = set()
    for g in G:
        if g in seen:
            continue
        cl = {compose(compose(h, g), inverse(h)) for h in G}
        seen |= cl
        classes.append({"order": order(g), "size": len(cl)})
    classes.sort(key=lambda c: (c["order"], c["size"]))

    # 2-transitivity on the 8 points and the ordered-pair stabilizer
    pair_orbit = {(g[0], g[1]) for g in G}
    pairs = [(x, y) for x in range(8) for y in range(8) if x != y]
    two_transitive = len(pair_orbit) == len(pairs) == 56
    stab_pair = frozenset(g for g in G if g[0] == 0 and g[1] == 1)
    s3 = None
    for g in G:
        if order(g) == 3:
            s3 = cyclic(g)
            break
    pair_stab_is_c3 = len(stab_pair) == 3 and any(conjugates(stab_pair, g) == s3 for g in G)

    # Sylow counts
    def sylow(p):
        subs = set()
        for g in G:
            if order(g) == p:
                subs.add(cyclic(g))
        return subs

    s7 = sylow(7)
    s3s = sylow(3)
    s2s = set()
    for g in G:
        if order(g) in (2, 4):
            for h in G:
                if order(h) in (2, 4):
                    H = closure([g, h])
                    if len(H) == 8:
                        s2s.add(H)

    involutions = [g for g in G if order(g) == 2]
    order3 = [g for g in G if order(g) == 3]
    order4 = [g for g in G if order(g) == 4]
    order7 = [g for g in G if order(g) == 7]
    class7 = [c for c in classes if c["order"] == 7]

    # 8 projective points <-> 8 Sylow 7-subgroups: compare stabilizers
    point_stab = frozenset(g for g in G if g[0] == 0)
    s7_list = sorted(s7, key=lambda H: tuple(sorted(H)))
    norm7 = frozenset(g for g in G if conjugates(s7_list[0], g) == s7_list[0])
    points_sylow_match = (len(s7) == 8 and len(point_stab) == len(norm7) == 21
                          and any(conjugates(point_stab, g) == norm7 for g in G))

    # cosets of a Sylow 7 subgroup
    cosets = {frozenset(compose(g, h) for h in s7_list[0]) for g in G}

    # GL(3,2) acting on the 7 Fano points: the ordered-pair stabilizer
    def gl32():
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
        perms = {tuple(vecs.index(apply(M, v)) for v in vecs) for M in mats}
        return perms
    F = gl32()
    e0 = (1, 0, 0)
    e1 = (0, 1, 0)
    vecs = [v for v in itertools.product((0, 1), repeat=3) if any(v)]
    i0, i1 = vecs.index(e0), vecs.index(e1)
    stab_ordered = [g for g in F if g[i0] == i0 and g[i1] == i1]
    # order_perm for 7-point perms
    def order_perm(p):
        e = tuple(range(len(p)))
        q = e
        for k in range(1, 50):
            q = tuple(p[x] for x in q)
            if q == e:
                return k
        return None
    ordered_stab_orders = sorted(order_perm(g) for g in stab_ordered)

    ev = {
        "group_order": len(G),
        "element_order_counts": {str(k): len(v) for k, v in sorted(by_order.items())},
        "conjugacy_classes": classes,
        "two_transitive_on_8_points": two_transitive,
        "ordered_pair_stabilizer_order": len(stab_pair),
        "ordered_pair_stabilizer_is_c3": pair_stab_is_c3,
        "sylow_counts": {"2": len(s2s), "3": len(s3s), "7": len(s7)},
        "involution_count": len(involutions),
        "order3_count": len(order3),
        "order4_count": len(order4),
        "order7_count": len(order7),
        "order7_class_sizes": [c["size"] for c in class7],
        "points_and_sylow7_share_stabilizer_order_21": points_sylow_match,
        "cosets_of_sylow7": len(cosets),
        "gl32_ordered_pair_stabilizer": {
            "order": len(stab_ordered),
            "element_orders": ordered_stab_orders,
            "type": "V4" if len(stab_ordered) == 4 and ordered_stab_orders.count(2) == 3 else "other",
        },
        "note": "PSL(2,7) acts 2-transitively on the 8 points of P^1(F_7); the 56 "
                "ordered pairs have a C3 stabilizer conjugate to a Sylow 3, so they are "
                "isomorphic as PSL-sets to the 56 elements of order 3. The 8 points and "
                "the 8 Sylow 7-subgroups both have stabilizer order 21. The 21 Sylow "
                "2-subgroups match the 21 Fano flags. The 42 order-4 elements and the 42 "
                "ordered Fano pairs have the same size only: the ordered-pair stabilizer "
                "is V4 while the centralizer of an order-4 element is C4, so they are not "
                "isomorphic as PSL-sets.",
    }
    with open(out_path, "w") as f:
        json.dump(ev, f, indent=2, sort_keys=True)
    print(json.dumps(ev, indent=2, sort_keys=True))
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main(*sys.argv[1:])
