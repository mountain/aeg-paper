#!/usr/bin/env python3
"""
Left vs right comb: does the "left natural traversal" (DFS, left first) agree
with the spine / chronological order?  Accompanying
notes/analysis-and-calculus/35-derive-shift.md.

Result: for a LEFT comb the DFS visits the internal spine first (so it agrees
with the spine/chronological order); for a RIGHT comb the DFS visits the
off-spine LEFT leaf first, so it does NOT agree with the spine order.  This is
the precise place where S = "chronological successor" matches (left) or differs
by a left/right flip (right).
"""

import json
import sys


class Leaf:
    __slots__ = ()

    def __repr__(self):
        return "L"


LEAF = Leaf()


class Node:
    __slots__ = ("l", "r")

    def __init__(self, l, r):
        self.l, self.r = l, r

    def __repr__(self):
        return f"N({self.l},{self.r})"


def left_traversal(t):
    seq = []

    def walk(x, side):
        if isinstance(x, Leaf):
            seq.append(("leaf", side))
            return
        seq.append(("node", side))
        walk(x.l, "L")
        walk(x.r, "R")

    walk(t, None)
    return seq


def spine_dirs(t):
    steps, cur = [], t
    while isinstance(cur, Node):
        li = isinstance(cur.l, Node)
        ri = isinstance(cur.r, Node)
        if li and not ri:
            steps.append("L")
            cur = cur.l
        elif ri and not li:
            steps.append("R")
            cur = cur.r
        else:
            break
    return steps


def first_after_root(seq):
    """What the DFS visits immediately after the root: a node or a leaf, and side."""
    return seq[1] if len(seq) > 1 else None


def main(out_path="/tmp/traversal.json"):
    left_comb = Node(Node(Node(LEAF, LEAF), LEAF), LEAF)
    right_comb = Node(LEAF, Node(LEAF, Node(LEAF, LEAF)))
    ev = {}
    for name, t in (("left_comb", left_comb), ("right_comb", right_comb)):
        seq = left_traversal(t)
        ev[name] = {
            "tree": repr(t),
            "left_traversal": seq,
            "spine_dirs": spine_dirs(t),
            "first_after_root": first_after_root(seq),
            "agrees_with_spine_order": first_after_root(seq) == ("node", spine_dirs(t)[0])
            if spine_dirs(t) else None,
        }
    ev["note"] = ("Left comb: DFS first visits the internal spine (agrees with spine/"
                  "chronological order). Right comb: DFS first visits the off-spine "
                  "LEFT leaf (disagrees by a left/right flip). See note 35 section 5.")
    with open(out_path, "w") as f:
        json.dump(ev, f, indent=2, sort_keys=True)
    print(json.dumps({k: v for k, v in ev.items() if k != "note"}, indent=2))
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main(*sys.argv[1:])
