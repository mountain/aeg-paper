#!/usr/bin/env python3
"""
Corner order (left standard traversal = PREORDER) vs evaluation order (POSTORDER).
Accompanying notes/analysis-and-calculus/37-corner-order-alignment.md.

Pushkarev-Byzov Thm 4.2: the left natural traversal is the standard left
traversal, defined recursively as "visit the vertex, then the left subtree, then
the right subtree" -- i.e. PREORDER.

Their Remark after Thm 4.3: the traversals coincide on the set of leaves (leaves
are incomparable), while on chains of nonleaves the order is inverted; across
incomparable chains the relative order is a choice.

The script checks, for representative trees:
  * leaves: preorder order == postorder order,
  * nonleaves: preorder order == reverse(postorder order) (chain case),
  * and records the balanced tree, where the two chains are incomparable so the
    global reversal fails (the "choice").
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


def preorder(t):
    out = []

    def walk(x, path):
        if isinstance(x, Leaf):
            out.append(("leaf", path))
            return
        out.append(("node", path))
        walk(x.l, path + "L")
        walk(x.r, path + "R")

    walk(t, "")
    return out


def postorder(t):
    out = []

    def walk(x, path):
        if isinstance(x, Leaf):
            out.append(("leaf", path))
            return
        walk(x.l, path + "L")
        walk(x.r, path + "R")
        out.append(("node", path))

    walk(t, "")
    return out


def kinds(order, kind):
    return [p for (k, p) in order if k == kind]


def check(name, t):
    pre, post = preorder(t), postorder(t)
    return {
        "tree": repr(t),
        "preorder_leaves": kinds(pre, "leaf"),
        "postorder_leaves": kinds(post, "leaf"),
        "preorder_nodes": kinds(pre, "node"),
        "postorder_nodes": kinds(post, "node"),
        "leaves_agree": kinds(pre, "leaf") == kinds(post, "leaf"),
        "nodes_reversed": kinds(pre, "node") == list(reversed(kinds(post, "node"))),
    }


def main(out_path="/tmp/corner_order.json"):
    trees = {
        "left_comb": Node(Node(Node(LEAF, LEAF), LEAF), LEAF),
        "right_comb": Node(LEAF, Node(LEAF, Node(LEAF, LEAF))),
        "balanced": Node(Node(LEAF, LEAF), Node(LEAF, LEAF)),
    }
    ev = {name: check(name, t) for name, t in trees.items()}
    ev["summary"] = {
        "leaves_agree_all": all(ev[n]["leaves_agree"] for n in trees),
        "nodes_reversed_in_chains": all(ev[n]["nodes_reversed"] for n in ("left_comb", "right_comb")),
        "balanced_is_choice": not ev["balanced"]["nodes_reversed"],
        "comment": "Leaves: preorder = postorder (frontier). Nonleaf chains: reversed. "
                   "Balanced (incomparable chains): global reversal fails -> a choice. "
                   "So S for the carousel k should be the PREORDER (corner) successor; "
                   "postorder is the evaluation order. See note 37.",
    }
    with open(out_path, "w") as f:
        json.dump(ev, f, indent=2, sort_keys=True)
    print(json.dumps(ev["summary"], indent=2))
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main(*sys.argv[1:])
