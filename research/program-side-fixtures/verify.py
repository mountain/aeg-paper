#!/usr/bin/env python3
"""Independent combinatorial oracle over Rust-emitted data, no semantic authority."""
import argparse
import importlib.util
import itertools
import json
import math
from pathlib import Path

HERE = Path(__file__).resolve().parent


def require(ok, message):
    if not ok:
        raise ValueError(message)


def inversions(order, reference):
    rank = {x: i for i, x in enumerate(order)}
    return sum(rank[u] > rank[v] for u, v in itertools.combinations(reference, 2))


def closure(ids, edges):
    relation = set(map(tuple, edges))
    for k in ids:
        for u in ids:
            for v in ids:
                if (u, k) in relation and (k, v) in relation:
                    relation.add((u, v))
    require(not any((v, v) in relation for v in ids), "cycle")
    return relation


def extensions(ids, relation):
    require(len(ids) <= 6, "permutation budget")
    return [p for p in itertools.permutations(ids)
            if all(p.index(u) < p.index(v) for u, v in relation)]


def tree_data(t):
    preorder, postorder, edges, sizes, contexts = [], [], [], {}, []

    def visit(node):
        if "id" not in node:
            return None, 0
        v = node["id"]
        preorder.append(v)
        left, nl = visit(node["left"])
        right, nr = visit(node["right"])
        edges.extend((c, v) for c in (left, right) if c is not None)
        sizes[v] = 1 + nl + nr
        postorder.append(v)
        require(node["op"] == "mul", "tree operation")
        slot = 2 if "constant" in node["left"] else 1
        const = node["left"] if slot == 2 else node["right"]
        require(const == {"constant": -1}, "single-spine signature")
        contexts.append((v, slot))
        return v, sizes[v]

    visit(t)
    relation = closure(preorder, edges)
    exts = extensions(preorder, relation)
    hook = math.factorial(len(preorder)) // math.prod(sizes.values())
    require(hook == len(exts), "tree hook-length count")
    best = min(inversions(p, preorder) for p in exts)
    minimizers = [p for p in exts if inversions(p, preorder) == best]
    require(minimizers == [tuple(postorder)], "tree canonical order")
    return dict(corner=preorder, canonical=postorder, edges=sorted(edges),
                strict_order=sorted(relation), linear_extensions=exts,
                schedule_count=len(exts), hook_length_count=hook,
                inversions=best, contexts=contexts)


def program_data(part):
    d, claimed = part["artifact"]["result"], part["orders"]
    nodes = {n["id"]: n for n in d["nodes"]}
    require(len(nodes) == len(d["nodes"]), "duplicate native id")
    edges = [(w["producer"]["node"], v) for v, n in nodes.items()
             for w in n["inputs"] if w["producer"]["kind"] == "node"]
    relation = closure(nodes, edges)
    corner = []

    def visit(v):
        require(v not in corner, "non-tree native body")
        corner.append(v)
        for w in nodes[v]["inputs"]:
            if w["producer"]["kind"] == "node":
                visit(w["producer"]["node"])

    visit(d["outputs"][0]["producer"]["node"])
    require(set(corner) == set(nodes), "hidden or missing event")
    exts = extensions(sorted(nodes), relation)
    best = min(inversions(p, corner) for p in exts)
    minimizers = [p for p in exts if inversions(p, corner) == best]
    require(len(minimizers) == 1, "native canonical minimizer")
    expected = {"event_ids": sorted(nodes), "dependency_edges": sorted(set(edges)),
                "strict_order": sorted(relation), "corner_order": corner,
                "linear_extensions": exts, "canonical_schedule": minimizers[0],
                "canonical_inversions": best, "schedule_count": len(exts),
                "permutations_tested": math.factorial(len(nodes)),
                "rejected_permutations": math.factorial(len(nodes)) - len(exts)}
    for key, value in expected.items():
        require(claimed[key] == json.loads(json.dumps(value)), f"native {key} mismatch")
    return expected


def catalogue_scope():
    # Reuse the existing catalogue only to classify scope, not to map programs.
    path = HERE.parent / "iota-carousel/verify_canonical_choice.py"
    spec = importlib.util.spec_from_file_location("tree_catalogue", path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    counts = []
    for leaves in range(4, 8):
        trees = m.ppcts(leaves)
        sequential = sum(all(l is None or r is None for l, r in m.internals(t).values()) for t in trees)
        counts.append({"internal_vertices": leaves - 1, "trees": len(trees),
                       "sequential_shapes": sequential, "branching_shapes": len(trees) - sequential})
    return counts


def verify(ev):
    require(ev["tree"] == json.loads((HERE / "fixtures/tree.json").read_text()), "fixed tree binding")
    tree = tree_data(ev["tree"])
    spine = program_data(ev["spine"])
    expanded = program_data(ev["expanded"])
    mapping = ev["spine"]["mapping"]
    require([(r["tree_vertex"], r["slot"]) for r in mapping] == tree["contexts"], "slot word mismatch")
    association = {r["tree_vertex"]: r["event"] for r in mapping}
    require(len(association) == 3 and len(set(association.values())) == 3, "event bijection")
    require(set(association.values()) == set(spine["event_ids"]), "all native events accounted for")
    require({(association[u], association[v]) for u, v in tree["strict_order"]}
            == set(spine["strict_order"]), "order isomorphism on fixed specimen")
    require([association[v] for v in tree["corner"]] == spine["corner_order"], "corner transport")
    require([association[v] for v in tree["canonical"]] == list(spine["canonical_schedule"]), "canonical transport")
    require(tree["inversions"] == spine["canonical_inversions"], "inversion transport")
    require(tree["schedule_count"] == spine["schedule_count"] == 1, "spine schedule count")
    mul_ids = {n["id"] for n in ev["expanded"]["artifact"]["result"]["nodes"] if n["operation"]["name"] == "mul"}
    projections = sorted({tuple(v for v in p if v in mul_ids) for p in expanded["linear_extensions"]})
    require(ev["expanded"]["arithmetic_event_projections"] == [list(p) for p in projections], "projection residual")
    require(len(projections) == 1 and expanded["schedule_count"] == 15, "constant-event obstruction")
    controls = ev["negative_controls"]
    require(len(controls) == 9 and all(c["outcome"] == "rejected" for c in controls), "mutation outcomes")
    return {"tree": tree, "spine_event_count": 3, "spine_schedule_count": 1,
            "spine_inversions": 3, "expanded_event_count": 6,
            "expanded_schedule_count": 15,
            "expanded_inversions": expanded["canonical_inversions"],
            "expanded_projection_fibre_size": 15,
            "rejected_controls": len(controls), "catalogue_scope": catalogue_scope(),
            "full_193_native_census": "not_run", "carrier_check": "not_run",
            "authority": "combinatorial cross-check only; native import/replay is Rust-owned"}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("evidence", type=Path)
    args = parser.parse_args()
    require(args.evidence.stat().st_size <= 1024 * 1024, "evidence size budget")
    print(json.dumps(verify(json.loads(args.evidence.read_bytes())), indent=2, sort_keys=True))
