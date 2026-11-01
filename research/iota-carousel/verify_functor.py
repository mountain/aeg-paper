#!/usr/bin/env python3
"""
Obstruction to functoriality of the right/left bijection, accompanying
notes/analysis-and-calculus/44-functoriality-rl.md (OQ-098.4).

The right/left bijection is a set bijection PPCT(n leaves) <-> PPT(n-1 edges)
(Catalan c_{n-1}).  Functoriality "preserving AEG's order defect / linear
extension structure" requires preserving the *operation poset*, hence at least
the *number of operations* (= internal, non-leaf nodes).

This script enumerates plane planted trees with m edges (as nested tuples; a
tree is a tuple of its children) and counts non-leaf nodes.  Result: the number
of operations on the PPT side ranges over {1, ..., m}, whereas every PPCT with
n = m+1 leaves has exactly n-1 = m operations.  The multisets differ, so no
bijection can preserve the operation count.
"""

from collections import Counter
from functools import lru_cache
import json
import sys


@lru_cache(maxsize=None)
def trees_with_edges(m):
    """Plane planted trees with m edges, as nested tuples (children tuples)."""
    if m == 0:
        return ((),)
    res = []
    # root + k subtrees; subtrees have e_i edges, sum(e_i + 1) = m  =>  sum e_i = m - k
    for k in range(1, m + 1):
        rest = m - k
        # compositions of rest into k nonnegative parts
        comps = []

        def comp(rem, idx, acc):
            if idx == 1:
                comps.append(acc + [rem])
                return
            for e in range(rem + 1):
                comp(rem - e, idx - 1, acc + [e])

        comp(rest, k, [])
        for e_list in comps:
            lists = [trees_with_edges(e) for e in e_list]
            stack = [[]]
            for lst in lists:
                stack = [s + [t] for s in stack for t in lst]
            res.extend(tuple(s) for s in stack)
    return tuple(dict.fromkeys(res))


def internal_count(g):
    if not g:
        return 0
    return 1 + sum(internal_count(c) for c in g)


def nodes(g):
    return 1 + sum(nodes(c) for c in g)


def main(out_path="/tmp/functor.json"):
    ev = {}
    catalan = [1, 1, 2, 5, 14, 42, 132]
    for m in range(0, 6):
        ts = trees_with_edges(m)
        c = Counter(internal_count(g) for g in ts)
        ev[str(m)] = {
            "num_trees": len(ts),
            "catalan_expected": catalan[m],
            "internal_distribution": {str(k): v for k, v in sorted(c.items())},
        }
    # the decisive comparison for n = 4 leaves  (m = 3 edges)
    m = 3
    ppt_internal = sorted(internal_count(g) for g in trees_with_edges(m))
    ppct_internal = [3] * catalan[m]  # every PPCT with 4 leaves has 3 internal nodes
    ev["comparison_n4"] = {
        "ppct_operation_multiset": ppct_internal,
        "ppt_operation_multiset": ppt_internal,
        "multisets_equal": sorted(ppct_internal) == sorted(ppt_internal),
        "conclusion": "PPCT: all trees have n-1 operations; PPT: operation count "
                      "ranges over {1,...,n-1}. Multisets differ, so no bijection "
                      "preserves the operation count, hence none preserves the "
                      "operation poset / linear extensions / order defect.",
    }
    with open(out_path, "w") as f:
        json.dump(ev, f, indent=2, sort_keys=True)
    print(json.dumps({"comparison_n4": ev["comparison_n4"]}, indent=2))
    print("distributions:", {k: ev[k]["internal_distribution"] for k in ev if k.isdigit()})
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main(*sys.argv[1:])
