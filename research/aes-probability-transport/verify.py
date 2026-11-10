#!/usr/bin/env python3
"""Exact finite witnesses for AES note 06; no training/model claim is tested.

Run from the repository root:
    python3 research/aes-probability-transport/verify.py
"""

from fractions import Fraction as F
from itertools import product
import json


def matrix(rows):
    return tuple(tuple(F(x) for x in row) for row in rows)


def identity(n):
    return matrix([[int(i == j) for j in range(n)] for i in range(n)])


def mm(a, b):
    if not a or not b or len(a[0]) != len(b):
        raise ValueError("matrix interface mismatch")
    if any(len(row) != len(a[0]) for row in a):
        raise ValueError("ragged source matrix")
    if any(len(row) != len(b[0]) for row in b):
        raise ValueError("ragged target matrix")
    return tuple(
        tuple(sum((a[i][t] * b[t][j] for t in range(len(b))), F(0))
              for j in range(len(b[0])))
        for i in range(len(a))
    )


def stochastic(k, allowed=None):
    if not k or not k[0] or any(len(row) != len(k[0]) for row in k):
        raise ValueError("invalid kernel shape")
    for i, row in enumerate(k):
        if any(x < 0 for x in row) or sum(row) != 1:
            raise ValueError("invalid stochastic row")
        if allowed is not None:
            for j, x in enumerate(row):
                if x > 0 and (i, j) not in allowed:
                    raise ValueError("positive mass on forbidden edge")


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def expect_rejected(name, operation, error=ValueError):
    try:
        operation()
    except error:
        return name
    raise AssertionError("negative control was accepted: " + name)


def tv(a, b):
    return sum((abs(x - y) for x, y in zip(a, b)), F(0)) / 2


def block_signature(row, partition):
    return tuple(sum((row[j] for j in block), F(0)) for block in partition)


def quotient(k, partition):
    """Reject unless the same quotient works for every microstate prior."""
    rows = []
    for block in partition:
        signatures = {block_signature(k[i], partition) for i in block}
        if len(signatures) != 1:
            raise ValueError("observation is not strongly lumpable")
        rows.append(signatures.pop())
    return tuple(rows)


def refine(kernels, partition):
    while True:
        result = []
        for block in partition:
            groups = {}
            for i in block:
                key = tuple(block_signature(k[i], partition) for k in kernels)
                groups.setdefault(key, []).append(i)
            result.extend(tuple(group) for group in groups.values())
        result = tuple(result)
        if result == partition:
            return result
        partition = result


def all_partitions(items):
    """Enumerate all set partitions, for an independent four-state check."""
    if not items:
        yield ()
        return
    first, *rest = items
    for partition in all_partitions(rest):
        yield ((first,),) + partition
        for j in range(len(partition)):
            yield partition[:j] + ((first,) + partition[j],) + partition[j+1:]


def area(q):
    theta, left, right, low, high = q
    require(left < right and 0 < low < high, "invalid quadrilateral")
    return (right - left) * (1 / low - 1 / high)


def horizontal(q, s):
    theta, left, right, low, high = q
    return (theta + s, left, right, low, high)


def vertical(q, k):
    theta, left, right, low, high = q
    require(k > 0, "scale must be positive")
    return (k * theta, left, right, low / k, high / k)


def main():
    negatives = []
    checks = []
    # Bridge example: compare matrix products with explicit path enumeration.
    swap = matrix([[0, 1, 0], [1, 0, 0], [0, 0, 1]])
    bridge = matrix([[1, 0, 0], [0, F(1, 2), F(1, 2)], [0, 0, 1]])
    support = {(0, 0), (1, 1), (1, 2), (2, 2)}
    stochastic(swap)
    stochastic(bridge, support)
    sk, ks = mm(swap, bridge), mm(bridge, swap)
    defect = tuple(tuple(a - b for a, b in zip(x, y)) for x, y in zip(sk, ks))
    require(defect == matrix([[0, -F(1, 2), F(1, 2)],
                              [F(1, 2), 0, -F(1, 2)], [0, 0, 0]]),
            "bridge defect changed")
    direct_sk = [F(0)] * 3
    direct_ks = [F(0)] * 3
    for middle, end in product(range(3), repeat=2):
        direct_sk[end] += swap[0][middle] * bridge[middle][end]
        direct_ks[end] += bridge[0][middle] * swap[middle][end]
    require(tuple(direct_sk) == sk[0] and tuple(direct_ks) == ks[0],
            "path enumeration disagrees with matrix composition")
    require(tv(sk[0], ks[0]) == F(1, 2), "unexpected bridge distance")

    window = tuple(map(F, [0, 0, 1, 1, 2]))
    path_sk = vertical(horizontal(window, F(1)), F(2))
    path_ks = horizontal(vertical(window, F(2)), F(2))
    require(path_sk == path_ks == tuple(map(F, [2, 0, 1, F(1, 2), 1])),
            "geometric square does not close")
    require(area(window) == F(1, 2) and area(path_sk) == 1,
            "reference area scale failed")
    for row in (sk[0], ks[0]):
        scaled = tuple(2 * area(window) * p for p in row)
        conservative = tuple(area(window) * p for p in row)
        require(sum(scaled) == area(path_sk), "reference mass was lost")
        require(sum(conservative) == area(window), "conserved mass was lost")
        require(tuple(x / sum(scaled) for x in scaled) == row,
                "common scale did not cancel")
    checks.append("bridge square: same geometry/mass, TV = 1/2")

    # Bayes reversal restores one prior, but fails the identity channel.
    prior = (F(1, 3),) * 3
    target = mm((prior,), bridge)[0]
    bayes = tuple(tuple(prior[i] * bridge[i][j] / target[j] for i in range(3))
                  for j in range(3))
    require(bayes == matrix([[1, 0, 0], [0, 1, 0], [0, F(1, 3), F(2, 3)]]),
            "unexpected Bayes reverse")
    stochastic(bayes)
    roundtrip = mm(bridge, bayes)
    require(mm((prior,), roundtrip)[0] == prior and roundtrip != identity(3),
            "prior restoration was confused with inversion")
    checks.append("Bayes reverse: prior restored, channel not identity")

    # Hidden memory: four states, deterministic involution.
    states = tuple(product((0, 1), repeat=2))
    def flip(state):
        b, h = state
        return (b ^ h, h)
    full = matrix([[int(flip(source) == target) for target in states]
                   for source in states])
    observation = matrix([[int(b == j) for j in (0, 1)] for b, h in states])
    initialize = matrix([[F(1, 2) if b == i else 0 for b, h in states]
                         for i in (0, 1)])
    observed = mm(mm(initialize, full), observation)
    require(observed == matrix([[F(1, 2)] * 2] * 2),
            "unexpected one-step average")
    require(mm(full, full) == identity(4), "full process is not an involution")
    require(mm(mm(initialize, mm(full, full)), observation) == identity(2),
            "shared-memory closure failed")
    require(mm(observed, observed) == observed != identity(2),
            "independent reinitialization accidentally closed")
    shared_rows, reset_rows = [], []
    for initial_b in (0, 1):
        shared, reset = [F(0), F(0)], [F(0), F(0)]
        for h in (0, 1):
            b1 = initial_b ^ h
            shared[b1 ^ h] += F(1, 2)
            for fresh_h in (0, 1):
                reset[b1 ^ fresh_h] += F(1, 4)
        shared_rows.append(tuple(shared))
        reset_rows.append(tuple(reset))
    require(tuple(shared_rows) == identity(2), "shared-path enumeration failed")
    require(tuple(reset_rows) == mm(observed, observed),
            "reset-path enumeration failed")
    uniform = ((F(1, 2), F(1, 2)),)
    require(mm(uniform, tuple(shared_rows)) == mm(uniform, tuple(reset_rows)),
            "uniform marginal counterexample failed")
    checks.append("shared-memory return = 1; independent-reset return = 1/2")

    # Strong lumpability and minimal finite refinement.
    initial_partition = ((0, 1), (2, 3))
    negatives.append(expect_rejected(
        "forgetting hidden bit is not lumpable",
        lambda: quotient(full, initial_partition)))
    refined = refine((full,), initial_partition)
    require(refined == ((0,), (1,), (2,), (3,)),
            "unexpected minimal refinement")
    require(quotient(full, refined) == full, "refined quotient failed")
    admissible = []
    for partition in all_partitions(tuple(range(4))):
        if any(len({states[i][0] for i in block}) != 1 for block in partition):
            continue
        try:
            quotient(full, partition)
        except ValueError:
            continue
        admissible.append(partition)
    require(len(admissible) == 1 and len(admissible[0]) == 4,
            "partition enumeration refutes minimality")
    # Positive control: flipping the visible bit descends without hidden memory.
    visible_flip = matrix([[int((b ^ 1, h) == target) for target in states]
                           for b, h in states])
    descended = quotient(visible_flip, initial_partition)
    require(descended == matrix([[0, 1], [1, 0]]), "positive quotient failed")
    require(mm(visible_flip, observation) == mm(observation, descended),
            "intertwining equation failed")
    require(mm(descended, descended) == identity(2), "descended inverse failed")
    checks.append("all four-state partitions: unique compatible refinement has 4 blocks")

    # Rational scale subgroup: keep the same hidden bit at every step.
    def lift(state, n):
        x, y, b, h = state
        return (x, y / (F(2) ** n), b ^ ((n % 2) * h), h)
    for b, h, n, m in product((0, 1), (0, 1), range(-3, 4), range(-3, 4)):
        state = (F(2, 3), F(5, 4), b, h)
        require(lift(lift(state, n), m) == lift(state, n + m),
                "scale-group relation failed")
    require(vertical(vertical(window, F(2)), F(1, 2)) == window,
            "geometric return failed")
    checks.append("196 rational lifted group-composition cases")

    # A finite independent check of the proved stability bound.
    distributions = [tuple(F(v, 4) for v in (a, b, 4-a-b))
                     for a in range(5) for b in range(5-a)]
    delta = max(sum(abs(x-y) for x, y in zip(r, s))
                for r, s in zip(swap, bridge))
    for p, q in product(distributions, repeat=2):
        left = mm((p,), bridge)[0]
        right = mm((q,), bridge)[0]
        require(tv(left, right) <= tv(p, q), "TV contraction failed")
        mixed = mm((p,), swap)[0]
        require(2 * tv(mixed, right) <= 2 * tv(p, q) + delta,
                "joint stability bound failed")
    checks.append("225 rational prior pairs: contraction and joint bound")

    # These failures are intended; accepting them would invalidate the model.
    negatives.append(expect_rejected("bad row sum",
        lambda: stochastic(matrix([[F(1, 4), F(1, 2)], [0, 1]]))))
    negatives.append(expect_rejected("forbidden relation edge",
        lambda: stochastic(bridge, {(0, 0), (1, 1), (2, 2)})))
    rectangular = matrix([[F(1, 8)] * 8] * 12)
    stochastic(rectangular)
    negatives.append(expect_rejected("12x8 self-composition",
        lambda: mm(rectangular, rectangular)))
    negatives.append(expect_rejected("independent-reset closure",
        lambda: require(mm(observed, observed) == identity(2),
                        "reset channel is not the identity"), AssertionError))
    negatives.append(expect_rejected("Bayes reverse as exact inverse",
        lambda: require(roundtrip == identity(3), "not an inverse"), AssertionError))
    print(json.dumps({"status": "PASS", "arithmetic": "exact rational",
                      "checks": checks, "negative_controls_rejected": negatives},
                     ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
