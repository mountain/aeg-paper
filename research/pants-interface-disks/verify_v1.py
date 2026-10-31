#!/usr/bin/env python3
"""Exact finite OQ-096 V1 calibration; standard library only.

Codex (OpenAI), under Mingli Yuan's research direction, 2026-10-31.
Construction and reception have the same author, not independent provenance.
No native Adva operation is invoked.
"""
from collections import Counter, defaultdict, deque
from copy import deepcopy
from fractions import Fraction
from itertools import combinations, permutations, product
from pathlib import Path
import hashlib
import json
import sys


class Rejected(ValueError):
    pass


def demand(condition, reason):
    if not condition:
        raise Rejected(reason)


def canonical_bytes(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":")).encode()


def clean(chain):
    return {k: v for k, v in chain.items() if v}


def add(*chains):
    result = Counter()
    for chain in chains:
        for cell, coefficient in chain.items():
            result[cell] += coefficient
    return clean(result)


def scale(chain, coefficient):
    return {cell: coefficient * value for cell, value in chain.items() if coefficient * value}


def boundary(chain):
    """Cubical boundary, with increasing coordinate-axis orientation."""
    result = Counter()
    for cell, coefficient in chain.items():
        anchor, mask = cell[:3], cell[3]
        axes = [axis for axis in range(3) if mask & (1 << axis)]
        for ordinal, axis in enumerate(axes):
            lower = (*anchor, mask ^ (1 << axis))
            upper_anchor = list(anchor)
            upper_anchor[axis] += 1
            upper = (*upper_anchor, mask ^ (1 << axis))
            sign = coefficient * (-1 if ordinal % 2 else 1)
            result[upper] += sign
            result[lower] -= sign
    return clean(result)


def closure(cells):
    result = set(cells)
    frontier = set(cells)
    while frontier:
        children = {face for cell in frontier for face in boundary({cell: 1})}
        frontier = children - result
        result.update(frontier)
    return result


def cubical_counts(cells):
    all_cells = closure(cells)
    counts = [sum(cell[3].bit_count() == dim for cell in all_cells) for dim in range(4)]
    return {"vertices": counts[0], "edges": counts[1], "faces": counts[2],
            "cubes": counts[3], "chi": sum((-1)**d * n for d, n in enumerate(counts))}


def components(vertices, edges):
    adjacency = {vertex: set() for vertex in vertices}
    for a, b in edges:
        adjacency[a].add(b)
        adjacency[b].add(a)
    unseen = set(vertices)
    count = 0
    while unseen:
        count += 1
        start = min(unseen)
        unseen.remove(start)
        queue = deque([start])
        while queue:
            for other in adjacency[queue.popleft()]:
                if other in unseen:
                    unseen.remove(other)
                    queue.append(other)
    return count


def simplex_faces(simplex):
    return [tuple(sorted(face)) for face in combinations(simplex, len(simplex) - 1)]


def surface_check(triangles, expected_chi, expected_boundary, label):
    """Connected orientable 2-manifold: incidence, vertex links and boundary."""
    triangles = {tuple(sorted(triangle)) for triangle in triangles}
    demand(bool(triangles), label + ":empty")
    vertices = set().union(*map(set, triangles))
    edges = Counter(edge for triangle in triangles for edge in simplex_faces(triangle))
    demand(all(count in (1, 2) for count in edges.values()), label + ":edge-incidence")
    demand(components(vertices, edges) == 1, label + ":disconnected")
    boundary_edges = {edge for edge, count in edges.items() if count == 1}
    boundary_vertices = set().union(*map(set, boundary_edges)) if boundary_edges else set()
    boundary_degree = Counter(vertex for edge in boundary_edges for vertex in edge)
    demand(all(degree == 2 for degree in boundary_degree.values()), label + ":boundary-not-circles")
    boundary_count = components(boundary_vertices, boundary_edges) if boundary_edges else 0
    demand(boundary_count == expected_boundary, label + ":boundary-count")
    for vertex in vertices:
        link_edges = {tuple(v for v in triangle if v != vertex) for triangle in triangles if vertex in triangle}
        link_vertices = set().union(*map(set, link_edges))
        degree = Counter(v for edge in link_edges for v in edge)
        demand(components(link_vertices, link_edges) == 1, label + ":vertex-link-disconnected")
        actual = sorted(degree.values())
        if vertex in boundary_vertices:
            demand(actual.count(1) == 2 and all(n in (1, 2) for n in actual), label + ":vertex-link-not-interval")
        else:
            demand(all(n == 2 for n in actual), label + ":vertex-link-not-circle")
    # Propagate signs across triangles to check orientability.
    by_edge = defaultdict(list)
    for triangle in triangles:
        for omitted in range(3):
            edge = triangle[:omitted] + triangle[omitted+1:]
            by_edge[edge].append((triangle, (-1)**omitted))
    orientation = {}
    for start in sorted(triangles):
        if start in orientation:
            continue
        orientation[start] = 1
        queue = deque([start])
        while queue:
            triangle = queue.popleft()
            for omitted in range(3):
                edge = triangle[:omitted] + triangle[omitted+1:]
                own = orientation[triangle] * (-1)**omitted
                for other, other_sign in by_edge[edge]:
                    if other == triangle:
                        continue
                    needed = -own * other_sign
                    if other in orientation:
                        demand(orientation[other] == needed, label + ":nonorientable")
                    else:
                        orientation[other] = needed
                        queue.append(other)
    chi = len(vertices) - len(edges) + len(triangles)
    demand(chi == expected_chi, label + ":chi")
    return {"vertices": len(vertices), "edges": len(edges), "triangles": len(triangles),
            "chi": chi, "boundary_components": boundary_count, "connected": True,
            "orientable": True, "vertex_links_checked": len(vertices)}


def triangulate_cell(cell):
    anchor, mask = cell[:3], cell[3]
    axes = [axis for axis in range(3) if mask & (1 << axis)]
    simplices = set()
    for order in permutations(axes):
        point = list(anchor)
        vertices = [tuple(point)]
        for axis in order:
            point[axis] += 1
            vertices.append(tuple(point))
        simplices.add(tuple(sorted(vertices)))
    return simplices


def triangulate(cells):
    return set().union(*(triangulate_cell(cell) for cell in cells))


def volume_check(cubes, label):
    """Check tetrahedral vertex links, rather than only an Euler number."""
    tets = triangulate(cubes)
    faces = Counter(face for tet in tets for face in simplex_faces(tet))
    demand(all(count in (1, 2) for count in faces.values()), label + ":face-incidence")
    boundary_triangles = {face for face, count in faces.items() if count == 1}
    sphere = surface_check(boundary_triangles, 2, 0, label + ":boundary")
    boundary_vertices = set().union(*map(set, boundary_triangles))
    links = defaultdict(set)
    for tet in tets:
        for vertex in tet:
            links[vertex].add(tuple(v for v in tet if v != vertex))
    kinds = Counter()
    for vertex, triangles in sorted(links.items()):
        on_boundary = vertex in boundary_vertices
        surface_check(triangles, 1 if on_boundary else 2, 1 if on_boundary else 0,
                      label + ":vertex-link:" + str(vertex))
        kinds["disk" if on_boundary else "sphere"] += 1
    counts = cubical_counts(cubes)
    demand(counts["chi"] == 1, label + ":volume-chi")
    # General ballhood is not inferred just from this check. The fixture is
    # explicitly two solid boxes joined by a straight tube (note 25, Prop. B).
    return {"cubical": counts, "tetrahedra": len(tets), "boundary": sphere,
            "vertex_links": dict(sorted(kinds.items()))}


def box(xrange, yrange, zrange):
    return [(*point, 7) for point in product(xrange, yrange, zrange)]


def encode_chain(chain):
    return [{"cell": list(cell), "coefficient": value} for cell, value in sorted(chain.items())]


def mod2_surface_filling(surface, cycle):
    """Test C in im(d_2) over F_2 using exact bit-column elimination."""
    edges = sorted(cell for cell in closure(surface) if cell[3].bit_count() == 1)
    positions = {edge: index for index, edge in enumerate(edges)}
    demand(set(cycle) <= set(edges), "surface-cycle:outside")
    def vector(chain):
        value = 0
        for edge, coefficient in chain.items():
            if coefficient % 2:
                value ^= 1 << positions[edge]
        return value
    basis = {}
    def reduce(value):
        while value:
            pivot = value.bit_length() - 1
            if pivot not in basis:
                break
            value ^= basis[pivot]
        return value
    for face in sorted(surface):
        value = reduce(vector(boundary({face: 1})))
        if value:
            basis[value.bit_length() - 1] = value
    demand(not any(coefficient % 2 for coefficient in boundary(cycle).values()),
           "surface-cycle:not-closed")
    # Positive controls for the same span implementation.
    demand(reduce(0) == 0, "surface-cycle:zero-control")
    for face in surface:
        demand(reduce(vector(boundary({face: 1}))) == 0, "surface-cycle:face-control")
    remainder = reduce(vector(cycle))
    vertices = sum(cell[3] == 0 for cell in closure(surface))
    return {"coefficient_field": "F_2", "boundary_matrix_rank": len(basis),
            "augmented_rank": len(basis) + bool(remainder),
            "cycle_bounds_in_side_surface": remainder == 0,
            "side_first_betti_number": len(edges) - vertices + 1 - len(basis),
            "face_boundary_positive_controls": len(surface)}


def decode_chain(rows):
    result = {}
    for row in rows:
        demand(set(row) == {"cell", "coefficient"}, "chain:fields")
        cell = tuple(row["cell"])
        demand(len(cell) == 4 and all(type(n) is int for n in cell), "chain:cell-type")
        demand(0 <= cell[3] <= 7, "chain:mask")
        demand(cell not in result, "chain:duplicate-cell")
        value = row["coefficient"]
        demand(type(value) is int and value in (-1, 1), "chain:coefficient")
        result[cell] = value
    return result


PORTS = {"x": (0, 1, 1, 6), "y": (1, 0, 1, 5),
         "t": (6, 0, 1, 5), "w": (8, 1, 1, 6)}
SEAM = (4, 1, 1, 6)


def build():
    left = {cell: 1 for cell in box(range(3), range(3), range(3)) + [(3, 1, 1, 7)]}
    right = {cell: 1 for cell in box(range(5, 8), range(3), range(3)) + [(4, 1, 1, 7)]}
    whole = add(left, right)
    exterior = boundary(whole)
    ports = {name: {cell: exterior[cell]} for name, cell in PORTS.items()}
    side = add(exterior, scale(add(*ports.values()), -1))
    left_pants = add(boundary(left), scale(add(ports["x"], ports["y"], {SEAM: 1}), -1))
    right_pants = add(boundary(right), scale(add(ports["t"], ports["w"], {SEAM: -1}), -1))
    return {"schema": "oq096-pants-interface-v1", "left": encode_chain(left),
            "right": encode_chain(right), "ports": {k: encode_chain(v) for k, v in ports.items()},
            "seam": encode_chain({SEAM: 1}), "circle": encode_chain(boundary({SEAM: 1})),
            "left_pants": encode_chain(left_pants), "right_pants": encode_chain(right_pants),
            "side": encode_chain(side), "program": {
                "inputs": {"x": "2", "y": "3", "t": "4"},
                "events": [{"id": "plus#1", "source": "Q:add", "op": "add", "inputs": ["x", "y"], "output": "z"},
                           {"id": "times#1", "source": "P:mul", "op": "mul", "inputs": ["z", "t"], "output": "w"}],
                "binding": {"producer": "plus#1", "output_slot": 0, "wire": "z",
                            "consumer": "times#1", "input_slot": 0, "type": "rational",
                            "output_occurrence": "Q:z:out", "input_occurrence": "P:z:in"},
                "patch_events": {"left": "plus#1", "right": "times#1"},
                "external_order": ["x", "y", "t", "w"]}}


def receive(candidate):
    demand(candidate["schema"] == "oq096-pants-interface-v1", "schema")
    left, right = decode_chain(candidate["left"]), decode_chain(candidate["right"])
    demand(not set(left) & set(right), "volumes:overlap")
    demand(all(cell[3] == 7 and coefficient == 1 for cell, coefficient in add(left, right).items()), "volumes:orientation")
    demand(len(left) + len(right) <= 100, "budget:cubes")
    whole = add(left, right)
    exterior = boundary(whole)
    demand(all(abs(n) == 1 for n in exterior.values()), "volumes:boundary-multiplicity")
    demand(not boundary(exterior), "volumes:boundary-squared")
    disk = decode_chain(candidate["seam"])
    circle = decode_chain(candidate["circle"])
    demand(disk == {SEAM: 1}, "seam:fixed-interface")
    demand(boundary(disk) == circle, "seam:boundary-circle")
    demand(not boundary(circle), "seam:circle-not-cycle")
    demand(not set(disk) & set(exterior), "seam:not-interior")
    left_boundary, right_boundary = boundary(left), boundary(right)
    demand(set(left_boundary) & set(right_boundary) == set(disk), "seam:intersection")
    demand(all(left_boundary[c] == disk[c] and right_boundary[c] == -disk[c] for c in disk), "seam:opposite-orientations")
    demand(set(candidate["ports"]) == set(PORTS), "ports:inventory")
    ports = {name: decode_chain(rows) for name, rows in candidate["ports"].items()}
    port_closures = []
    for name, cell in PORTS.items():
        demand(cell in exterior, "ports:not-external")
        demand(ports[name] == {cell: exterior[cell]}, "ports:identity-or-orientation")
        closed = closure(ports[name])
        demand(all(not closed & previous for previous in port_closures), "ports:touching")
        port_closures.append(closed)
    left_pants = decode_chain(candidate["left_pants"])
    right_pants = decode_chain(candidate["right_pants"])
    side = decode_chain(candidate["side"])
    demand(add(left_pants, ports["x"], ports["y"], disk) == left_boundary, "left:boundary-decomposition")
    demand(add(right_pants, ports["t"], ports["w"], scale(disk, -1)) == right_boundary, "right:boundary-decomposition")
    demand(add(left_pants, right_pants) == side, "side:assembly")
    demand(add(side, *ports.values()) == exterior, "side:external-decomposition")
    demand(set(circle) <= closure(side), "circle:not-on-side")
    demand(not set(circle) & set(boundary(side)), "circle:still-external-boundary")
    demand(boundary(left_pants) == scale(add(boundary(ports["x"]), boundary(ports["y"]), circle), -1), "left:seam-sign")
    demand(boundary(right_pants) == add(scale(add(boundary(ports["t"]), boundary(ports["w"])), -1), circle), "right:seam-sign")
    volume = volume_check(whole, "whole")
    halves = {"left": volume_check(left, "left"), "right": volume_check(right, "right")}
    surfaces = {}
    for name, chain, chi, boundaries in [("left_pants", left_pants, -1, 3),
                                        ("right_pants", right_pants, -1, 3),
                                        ("side", side, -2, 4), ("disk", disk, 1, 1)]:
        surfaces[name] = {"cubical": cubical_counts(chain),
                          "simplicial": surface_check(triangulate(chain), chi, boundaries, name)}
    filling = mod2_surface_filling(side, circle)
    demand(not filling["cycle_bounds_in_side_surface"], "circle:unexpected-surface-filling")
    demand(filling["side_first_betti_number"] == 3, "side:homology")
    program = candidate["program"]
    # Structural identity is checked separately from multiplication's
    # symmetric scalar output, against a frozen finite contract.
    expected_program = {
        "inputs": {"x": "2", "y": "3", "t": "4"},
        "events": [{"id": "plus#1", "source": "Q:add", "op": "add", "inputs": ["x", "y"], "output": "z"},
                   {"id": "times#1", "source": "P:mul", "op": "mul", "inputs": ["z", "t"], "output": "w"}],
        "binding": {"producer": "plus#1", "output_slot": 0, "wire": "z", "consumer": "times#1",
                    "input_slot": 0, "type": "rational", "output_occurrence": "Q:z:out", "input_occurrence": "P:z:in"},
        "patch_events": {"left": "plus#1", "right": "times#1"}, "external_order": ["x", "y", "t", "w"]}
    demand(program == expected_program, "program:frozen-slot-source-contract")
    environment = {name: Fraction(value) for name, value in program["inputs"].items()}
    for event in program["events"]:
        demand(event["output"] not in environment, "program:multiple-producers")
        demand(all(name in environment for name in event["inputs"]), "program:dependency")
        a, b = [environment[name] for name in event["inputs"]]
        environment[event["output"]] = a + b if event["op"] == "add" else a * b
    direct = (Fraction(2) + Fraction(3)) * Fraction(4)
    demand(environment["z"] == 5 and environment["w"] == direct == 20, "program:evaluation")
    expected_left = set(box(range(3), range(3), range(3)) + [(3, 1, 1, 7)])
    expected_right = set(box(range(5, 8), range(3), range(3)) + [(4, 1, 1, 7)])
    demand(set(left) == expected_left and set(right) == expected_right, "geometry:frozen-voxel-inventory")
    return {"volume": volume, "halves": halves, "surfaces": surfaces,
            "hole_disk_complement": {
                "surface_homology": filling, "bulk_has_explicit_filling_disk": True,
                "cut_pants_have_circle_in_boundary": True,
                "glued_side_has_circle_as_interior_seam": True},
            "oriented_chain_identities": "pass", "circle_edges": len(circle),
            "program": {"events": 2, "binding": program["binding"], "interface_value": str(environment["z"]),
                        "output_value": str(environment["w"]), "direct_substitution": str(direct),
                        "distinct_interface_occurrences_retained": True}}


def run():
    candidate = build()
    accepted = receive(candidate)
    negatives = []
    mutations = []
    bad = deepcopy(candidate); bad["circle"][0]["coefficient"] *= -1
    mutations.append(("reverse-one-circle-edge", bad))
    bad = deepcopy(candidate); bad["left_pants"].pop()
    mutations.append(("remove-one-pants-face", bad))
    bad = deepcopy(candidate); bad["left_pants"][0]["coefficient"] *= -1
    mutations.append(("reverse-one-pants-face", bad))
    bad = deepcopy(candidate); bad["seam"] = deepcopy(bad["ports"]["w"])
    mutations.append(("external-port-as-internal-disk", bad))
    bad = deepcopy(candidate); bad["ports"]["y"] = deepcopy(bad["ports"]["x"])
    mutations.append(("alias-two-port-disks", bad))
    bad = deepcopy(candidate); bad["program"]["binding"]["input_slot"] = 1
    mutations.append(("wrong-slot-despite-commutative-output", bad))
    bad = deepcopy(candidate); bad["program"]["binding"]["input_occurrence"] = "Q:z:out"
    mutations.append(("collapse-interface-occurrences", bad))
    bad = deepcopy(candidate); bad["program"]["events"].pop(0)
    mutations.append(("erase-producer-event", bad))
    for name, altered in mutations:
        try:
            receive(altered)
        except Rejected as exc:
            negatives.append({"name": name, "result": "rejected", "reason": str(exc)})
        else:
            raise Rejected("mutation-accepted:" + name)
    # Direct controls for the topology validator, independent of the frozen
    # fixture-identity guard: global counts must not certify manifolds.
    for name, cells in [
        ("vertex-only-cube-contact", {(0, 0, 0, 7): 1, (1, 1, 1, 7): 1}),
        ("internal-cavity", {cell: 1 for cell in box(range(3), range(3), range(3)) if cell != (1, 1, 1, 7)}),
    ]:
        try:
            volume_check(cells, name)
        except Rejected as exc:
            negatives.append({"name": name, "result": "rejected", "reason": str(exc)})
        else:
            raise Rejected("mutation-accepted:" + name)
    return {"schema": "oq096-pants-interface-evidence-v1", "status": "finite-example-verified",
            "verifier_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "baseline_aeg": "b77ca915902670863cd718e1df3f308defa59ad2",
            "baseline_adva_read_only": "87a1a6933bca3fdb5c176cbf612729e278d172f7",
            "candidate_sha256": hashlib.sha256(canonical_bytes(candidate)).hexdigest(),
            "candidate": candidate, "accepted": accepted, "negative_controls": negatives,
            "limitations": ["one fixed two-event example", "one author; no independent implementation",
                            "no general decorated-composition theorem", "no AES metric or motion realization",
                            "no native Adva execution or Seal", "no ideal-boundary identification"]}


if __name__ == "__main__":
    if len(sys.argv) == 3 and sys.argv[1] == "--receive":
        path = Path(sys.argv[2])
        demand(path.stat().st_size <= 2_000_000, "evidence:byte-limit")
        saved = json.loads(path.read_text())
        demand(saved["schema"] == "oq096-pants-interface-evidence-v1", "evidence:schema")
        demand(saved["verifier_sha256"] == hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
               "evidence:verifier-binding")
        demand(saved["candidate_sha256"] == hashlib.sha256(canonical_bytes(saved["candidate"])).hexdigest(),
               "evidence:candidate-binding")
        demand(receive(saved["candidate"]) == saved["accepted"], "evidence:reception-mismatch")
        print(json.dumps({"status": "saved-candidate-received",
                          "candidate_sha256": saved["candidate_sha256"]}, sort_keys=True))
    else:
        demand(len(sys.argv) == 1, "usage: verify_v1.py [--receive evidence.json]")
        print(json.dumps(run(), sort_keys=True, indent=2))
