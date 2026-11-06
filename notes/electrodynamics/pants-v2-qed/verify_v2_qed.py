#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""OQ-096 V2-QED：把 V1 的同一台检查器用到 e+e- -> mu+mu- 的接线（2->1 拼 1->2）。

本文件做三件事，三层各自独立报告：
  L1 拓扑层：用 QED 的程序记录重跑 V1 的全部拓扑检查，并与 V1 已保存的基线逐字段比对；
  L2 装饰层：证明 V1 的"装饰"从不进入几何——程序记录只是冻结字面量，求值器是二元的；
  L3 语义层（V1 没有这一层）：每个 pants 上的荷/动量守恒、缝上接口状态的一致性、
      以及 2->1 的确定性与 1->2 的前像计数；并用负对照证明这一层不是空的。

来源与功劳归属
  - 几何层（本文件 "geometry layer" 一节）**逐字**取自 AEG 仓库
    `~/AEG/aeg-paper/research/pants-interface-disks/verify_v1.py`
    （sha256 fac64f82cea293ef58de9d0f1929ab4d3164d380b4d63f37be7a15b6fcfe644f；
      作者 Codex (OpenAI)，研究方向 Mingli Yuan，2026-10-31）。
  - L1/L2/L3 的包装、QED 程序记录与语义层，由本轮（DeepSeek Harness, 2026-10-31）新写。
  - 没有调用 Adva 的任何原生操作；没有改写 AEG 仓库内的任何文件。

只用标准库。运行：
  python3 verify_v2_qed.py            # 打印 JSON 报告
  python3 verify_v2_qed.py --check    # 只打印各层判决（人读）
"""
from collections import Counter, defaultdict, deque
from copy import deepcopy
from fractions import Fraction
from itertools import combinations, permutations, product
from pathlib import Path
import hashlib
import json
import sys


# ----------------------------------------------------------------------
# geometry layer (verbatim from V1)
# ----------------------------------------------------------------------
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




# ======================================================================
# 冻结的几何：端口圆盘与缝圆（取自 V1，坐标一个都没动）
# ======================================================================
PORTS = {"x": (0, 1, 1, 6), "y": (1, 0, 1, 5),
         "t": (6, 0, 1, 5), "w": (8, 1, 1, 6)}
SEAM = (4, 1, 1, 6)


def build_geometry(program):
    """V1 的 build()，**只把 program 提为参数**；胞腔清单与 V1 完全相同。"""
    left = {cell: 1 for cell in box(range(3), range(3), range(3)) + [(3, 1, 1, 7)]}
    right = {cell: 1 for cell in box(range(5, 8), range(3), range(3)) + [(4, 1, 1, 7)]}
    whole = add(left, right)
    exterior = boundary(whole)
    ports = {name: {cell: exterior[cell]} for name, cell in PORTS.items()}
    side = add(exterior, scale(add(*ports.values()), -1))
    left_pants = add(boundary(left), scale(add(ports["x"], ports["y"], {SEAM: 1}), -1))
    right_pants = add(boundary(right), scale(add(ports["t"], ports["w"], {SEAM: -1}), -1))
    return {"schema": "oq096-pants-interface-v2-qed", "left": encode_chain(left),
            "right": encode_chain(right), "ports": {k: encode_chain(v) for k, v in ports.items()},
            "seam": encode_chain({SEAM: 1}), "circle": encode_chain(boundary({SEAM: 1})),
            "left_pants": encode_chain(left_pants), "right_pants": encode_chain(right_pants),
            "side": encode_chain(side), "program": program}


def receive_geometry(candidate):
    """V1 的 receive() 中**几何的那一半**，逐条照抄；程序记录不参与。

    这一半是真正在做事的：胞腔链、定向、缝圆双侧反向、孔–盘互补、局部 link、
    模 2 秩、voxel 清单。它从不询问哪个端口是输入、哪个是输出。
    """
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
        demand(ports[name] == {cell: exterior[cell]}, "ports:identity-orientation")
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
    expected_left = set(box(range(3), range(3), range(3)) + [(3, 1, 1, 7)])
    expected_right = set(box(range(5, 8), range(3), range(3)) + [(4, 1, 1, 7)])
    demand(set(left) == expected_left and set(right) == expected_right, "geometry:frozen-voxel-inventory")
    return {"volume": volume, "halves": halves, "surfaces": surfaces,
            "hole_disk_complement": {
                "surface_homology": filling, "bulk_has_explicit_filling_disk": True,
                "cut_pants_have_circle_in_boundary": True,
                "glued_side_has_circle_as_interior_seam": True},
            "oriented_chain_identities": "pass", "circle_edges": len(circle)}


def receive_program_v1(candidate, expected_program):
    """V1 的 receive() 中**程序的那一半**，逐条照抄（含二元求值器）。"""
    program = candidate["program"]
    demand(program == expected_program, "program:frozen-slot-source-contract")
    environment = {name: Fraction(value) for name, value in program["inputs"].items()}
    for event in program["events"]:
        demand(event["output"] not in environment, "program:multiple-producers")
        demand(all(name in environment for name in event["inputs"]), "program:dependency")
        a, b = [environment[name] for name in event["inputs"]]
        environment[event["output"]] = a + b if event["op"] == "add" else a * b
    return {"events": len(program["events"]), "environment": {k: str(v) for k, v in environment.items()}}


# ======================================================================
# 两种"装饰"（同一批圆盘上的两次命名）
# ======================================================================
PROGRAM_V1 = {
    "inputs": {"x": "2", "y": "3", "t": "4"},
    "events": [{"id": "plus#1", "source": "Q:add", "op": "add", "inputs": ["x", "y"], "output": "z"},
               {"id": "times#1", "source": "P:mul", "op": "mul", "inputs": ["z", "t"], "output": "w"}],
    "binding": {"producer": "plus#1", "output_slot": 0, "wire": "z", "consumer": "times#1",
                "input_slot": 0, "type": "rational", "output_occurrence": "Q:z:out",
                "input_occurrence": "P:z:in"},
    "patch_events": {"left": "plus#1", "right": "times#1"},
    "external_order": ["x", "y", "t", "w"]}

# QED：左 pants = 湮灭顶点（2 进 1 出），右 pants = 产生顶点（1 进 2 出）
PROGRAM_QED = {
    "inputs": {"e-": "[2,2]", "e+": "[3,3]", "mu-": "[3,2]", "mu+": "[2,1]"},
    "events": [{"id": "annih#1", "source": "QED:eeA", "op": "sum4",
                "inputs": ["e-", "e+"], "outputs": ["q"]},
               {"id": "create#1", "source": "QED:Amumu", "op": "split4",
                "inputs": ["q"], "outputs": ["mu-", "mu+"]}],
    "binding": {"producer": "annih#1", "output_slot": 0, "wire": "q", "consumer": "create#1",
                "input_slot": 0, "type": "four-momentum", "output_occurrence": "QED:q:out",
                "input_occurrence": "QED:q:in"},
    "patch_events": {"left": "annih#1", "right": "create#1"},
    "external_order": ["e-", "e+", "mu-", "mu+"]}

# 故意荒谬的装饰：四个外线端口全挂在左 pants 上，缝被"同一个 pants 生出又吃掉"
PROGRAM_ABSURD = {
    "inputs": {"a": "1"},
    "events": [{"id": "x1", "source": "nonsense", "op": "sum4",
                "inputs": ["e-", "e+", "mu-", "mu+"], "outputs": ["q"]},
               {"id": "x2", "source": "nonsense2", "op": "split4",
                "inputs": [], "outputs": ["q", "e-"]}],
    "binding": {"producer": "x2", "output_slot": 0, "wire": "q", "consumer": "x2",
                "input_slot": 0, "type": "whatever", "output_occurrence": "o", "input_occurrence": "i"},
    "patch_events": {"left": "x1", "right": "x2"},
    "external_order": ["e-", "e+", "mu-", "mu+"]}

# 同一套 QED 接线，但把四动量换成标量值：用来单独暴露"求值器是二元的"这一条
PROGRAM_QED_SCALAR = {
    "inputs": {"e-": "2", "e+": "3", "mu-": "1", "mu+": "0"},
    "events": [{"id": "annih#1", "source": "QED:eeA", "op": "add",
                "inputs": ["e-", "e+"], "outputs": ["q"]},
               {"id": "create#1", "source": "QED:Amumu", "op": "sub",
                "inputs": ["q"], "outputs": ["mu-", "mu+"]}],
    "binding": {"producer": "annih#1", "output_slot": 0, "wire": "q", "consumer": "create#1",
                "input_slot": 0, "type": "scalar", "output_occurrence": "QED:q:out",
                "input_occurrence": "QED:q:in"},
    "patch_events": {"left": "annih#1", "right": "create#1"},
    "external_order": ["e-", "e+", "mu-", "mu+"]}

PORT_BAPTISM_V1 = {"x": "x", "y": "y", "t": "t", "w": "w"}
PORT_BAPTISM_QED = {"x": "e-", "y": "e+", "t": "mu-", "w": "mu+"}


# ======================================================================
# L1 拓扑层：同一台检查器，QED 的装饰，与 V1 基线逐字段比对
# ======================================================================
GEOMETRY_KEYS = ("volume", "halves", "surfaces", "hole_disk_complement",
                 "oriented_chain_identities", "circle_edges")


def layer1(baseline_path=None):
    v1 = receive_geometry(build_geometry(PROGRAM_V1))
    v2 = receive_geometry(build_geometry(PROGRAM_QED))
    identical = all(v1[k] == v2[k] for k in GEOMETRY_KEYS)
    report = {"V1_decor_accepted": True, "QED_decor_accepted": True,
              "geometry_fields_identical": identical,
              "fields": list(GEOMETRY_KEYS),
              "side_homology": v2["hole_disk_complement"]["surface_homology"],
              "surfaces": {k: {"chi": v["simplicial"]["chi"],
                               "boundary_components": v["simplicial"]["boundary_components"]}
                           for k, v in v2["surfaces"].items()},
              "volume_chi": v2["volume"]["cubical"]["chi"],
              "cubes": v2["volume"]["cubical"]["cubes"]}
    if baseline_path and Path(baseline_path).exists():
        saved = json.loads(Path(baseline_path).read_text())["accepted"]
        diffs = [k for k in GEOMETRY_KEYS if saved[k] != v2[k]]
        report["baseline_file"] = str(baseline_path)
        report["diff_vs_saved_V1_baseline"] = diffs
        report["matches_saved_V1_baseline"] = not diffs
    return report


# ======================================================================
# L2 装饰层：证明 V1 的装饰从不进入几何
# ======================================================================
def layer2():
    findings = {}

    # (a) 正确的 QED 记录会被 V1 的冻结字面量挡掉
    try:
        receive_program_v1(build_geometry(PROGRAM_QED), PROGRAM_V1)
    except Rejected as exc:
        findings["a_correct_QED_record_vs_V1_frozen_literal"] = {
            "result": "rejected", "reason": str(exc)}
    else:
        findings["a_correct_QED_record_vs_V1_frozen_literal"] = {"result": "accepted"}
        raise Rejected("L2a:QED-record-should-hit-the-frozen-contract")

    # (b) 荒谬装饰照样通过几何层 ⇒ 几何对装饰完全盲
    absurd = receive_geometry(build_geometry(PROGRAM_ABSURD))
    findings["b_absurd_decoration_through_geometry"] = {
        "result": "accepted",
        "side_chi": absurd["surfaces"]["side"]["simplicial"]["chi"],
        "note": "四个外线端口全算作一个 pants 的输入、缝由同一 pants 生出又吃掉，几何检查毫发无伤"}

    # (c1) 四动量取值的接口：V1 的求值器连"摄入"都做不到（它把每个端口当有理数）
    try:
        receive_program_v1(build_geometry(PROGRAM_QED), PROGRAM_QED)
    except Rejected as exc:
        findings["c1_four_momentum_interface"] = {"result": "rejected", "reason": str(exc)}
    except (KeyError, TypeError, ValueError) as exc:
        findings["c1_four_momentum_interface"] = {
            "result": "crash", "exception": type(exc).__name__, "detail": repr(exc),
            "note": "求值器把每个端口读成 Fraction：四动量取值的接口在摄入阶段就失败"}
    else:
        findings["c1_four_momentum_interface"] = {"result": "accepted"}
        raise Rejected("L2c1:four-momentum-interface-should-not-ingest")

    # (c2) 换成标量值，暴露第二个、独立的问题：求值器假设每个事件恰有 1 个 output
    try:
        receive_program_v1(build_geometry(PROGRAM_QED_SCALAR), PROGRAM_QED_SCALAR)
    except Rejected as exc:
        findings["c2_binary_evaluator"] = {"result": "rejected", "reason": str(exc)}
    except (KeyError, TypeError, ValueError) as exc:
        findings["c2_binary_evaluator"] = {
            "result": "crash", "exception": type(exc).__name__, "detail": repr(exc),
            "note": "冻结字面量这一关过了，但循环里 environment[event['output']] 假定"
                    "每个事件恰有一个 output；1->2 事件在 V1 的求值语义里没有表达"}
    else:
        findings["c2_binary_evaluator"] = {"result": "accepted"}
        raise Rejected("L2c2:binary-evaluator-should-not-digest-a-1-to-2-event")

    # (d) 几何对"哪一侧是哪个 pants"也只是靠 slot 清单，与方向无关
    findings["d_port_direction_never_read"] = {
        "grep_in_geometry_layer": [
            "ports:inventory / ports:identity-orientation（只比圆盘身份与定向）",
            "left:boundary-decomposition / right:boundary-decomposition（只用 x,y 与 t,w）",
            "无任何 'in'/'out'/'input'/'output' 字段被读取"],
        "conclusion": "装饰（谁进谁出）只存在于 program 记录，而 program 被冻结字面量比较"}
    return findings


# ======================================================================
# L3 语义层（V1 没有）：守恒、缝上状态一致性、确定性与前像计数
# ======================================================================
CHARGES = {"e-": -1, "e+": +1, "mu-": -1, "mu+": +1, "q": 0}

DECOR_QED = {"left": {"in": ["e-", "e+"], "out": ["q"]},
             "right": {"in": ["q"], "out": ["mu-", "mu+"]}}

GRID = tuple(range(-6, 7))          # 一维动量格，质量为零 ⇒ E=|p|


def onshell(k):
    return (Fraction(abs(k)), Fraction(k))


def pant_ports(pant):
    return list(pant["in"]) + list(pant["out"])


def pant_shape(pant, label):
    """AEG Prop 10.2(1)：总端口数 3 ⇒ pants（2 端口是柱面，1 端口是圆盘）。"""
    ports = pant_ports(pant)
    demand(len(ports) == 3, label + ":not-three-ports")
    demand(len(set(ports)) == 3, label + ":aliased-port")
    demand(len(set(pant["in"])) == len(pant["in"]), label + ":aliased-input")
    demand(len(set(pant["out"])) == len(pant["out"]), label + ":aliased-output")
    demand(not (set(pant["in"]) & set(pant["out"])), label + ":port-on-both-sides")


def conservation(pant, momenta, label):
    """每个 pants 上：Σ_入 p − Σ_出 p = 0（四动量），且 Σ_入 Q − Σ_出 Q = 0（电荷）。"""
    mom = [Fraction(0), Fraction(0)]
    charge = 0
    for name in pant["in"]:
        mom = [a + b for a, b in zip(mom, momenta[name])]
        charge += CHARGES[name]
    for name in pant["out"]:
        mom = [a - b for a, b in zip(mom, momenta[name])]
        charge -= CHARGES[name]
    demand(mom[0] >= 0, label + ":energy-residual-negative")
    demand(mom == [0, 0], label + ":momentum-not-conserved")
    demand(charge == 0, label + ":charge-not-conserved")
    return {"momentum_residual": [str(x) for x in mom], "charge_residual": charge}


def splits(q, grid=GRID):
    """给定缝上的四动量 q，返回全部 (k3,k4) 使两条在壳外线之和 = q。"""
    out = []
    for k3 in grid:
        p3 = onshell(k3)
        for k4 in grid:
            p4 = onshell(k4)
            if (p3[0] + p4[0], p3[1] + p4[1]) == q:
                out.append((k3, k4))
    return out


def layer3():
    result = {}

    # --- 装饰良构性 ---
    for label, pant in DECOR_QED.items():
        pant_shape(pant, label)
    result["pant_shape"] = "pass: 两个 pants 各 3 端口，2->1 与 1->2"

    # --- 端口洗礼：四个冻结圆盘各被命名一次 ---
    demand(sorted(PORT_BAPTISM_QED) == sorted(PORTS), "baptism:inventory")
    demand(len(set(PORT_BAPTISM_QED.values())) == 4, "baptism:aliased-leg")
    result["port_baptism"] = {k: PORT_BAPTISM_QED[k] for k in sorted(PORT_BAPTISM_QED)}

    # --- 选一对在壳初态，算出缝上状态与"产生顶点"的前像集合 ---
    cases = {}
    for (k1, k2) in [(2, 3), (2, -1)]:
        p1, p2 = onshell(k1), onshell(k2)
        q = (p1[0] + p2[0], p1[1] + p2[1])
        sol = splits(q)
        cases[f"e-={k1},e+={k2}"] = {
            "q": [str(q[0]), str(q[1])],
            "s_on_shell": str(q[0] ** 2 - q[1] ** 2),
            "preimage_count": len(sol),
            "splits_(mu-,mu+)": sol,
            "seam_on_shell": q[0] ** 2 - q[1] ** 2 == 0,
        }
    result["annihilation_to_seam"] = cases

    # --- 确定性：2->1 唯一；1->2 是多重前像 ---
    k1, k2 = 2, 3
    p1, p2 = onshell(k1), onshell(k2)
    q = (p1[0] + p2[0], p1[1] + p2[1])
    sol = splits(q)
    mom_a = {"e-": p1, "e+": p2, "q": q}
    result["conservation_left"] = conservation(DECOR_QED["left"], mom_a, "left")

    N = len(sol)
    result["determinism"] = {
        "annihilation_2_to_1": "deterministic: 输入 (p1,p2) 唯一决定 q",
        "creation_1_to_2_preimages": N,
        "is_a_function": N == 1,
        "verdict": ("1->2 不是确定偏函数：给定 q 有 %d 组在壳拆分 ⇒ 只能是关系 + 权重" % N),
    }

    # --- 权重必须住在哪：前像集合上的 (1+cos^2θ) ---
    weight_tables = {}
    for (k1, k2) in [(2, 3), (2, -1)]:
        p1c, p2c = onshell(k1), onshell(k2)
        qc = (p1c[0] + p2c[0], p1c[1] + p2c[1])
        solc = splits(qc)
        rows = []
        for (k3, k4) in solc:
            e3, e4 = Fraction(abs(k3)), Fraction(abs(k4))
            z = e3 / (e3 + e4)
            cos = 2 * z - 1                      # 三维里 z = (1+cosθ)/2
            rows.append({"mu-_k": k3, "mu+_k": k4, "z": str(z), "cos_theta": str(cos),
                         "weight_1+cos^2": str(1 + cos * cos)})
        ws = [Fraction(r["weight_1+cos^2"]) for r in rows]
        weight_tables["e-=%d,e+=%d" % (k1, k2)] = {
            "seam_q": [str(qc[0]), str(qc[1])],
            "seam_s": str(qc[0] ** 2 - qc[1] ** 2),
            "rows": rows,
            "sum_of_physical_weights": str(sum(ws)),
            "sum_if_no_weight (flat)": str(len(ws)),
            "max_over_min": str(max(ws) / min(ws)),
        }
    result["weight_on_preimage_set"] = {
        "cases": weight_tables,
        "note": ("若 Pant 的拼接只按相等粘、不带核，等价于在前像集合上取常权 ⇒ 预言平的 cosθ 分布；"
                 "而 QED 给 (1+cos^2θ)。缺的那个东西的定义域，正好就是这个前像集合。"),
    }

    # --- 负对照：装饰被改坏时必须被这一层拒绝 ---
    negatives = []

    def expect_reject(name, decor, mom):
        try:
            for label, pant in decor.items():
                pant_shape(pant, label)
                conservation(pant, mom, label)
        except Rejected as exc:
            negatives.append({"name": name, "result": "rejected", "reason": str(exc)})
        else:
            raise Rejected("L3-negative-accepted:" + name)

    mu_m, mu_p = onshell(2), onshell(3)
    mom_full = {"e-": p1, "e+": p2, "q": q, "mu-": mu_m, "mu+": mu_p}
    # 1) 把 mu- 翻成输入（电荷 + 动量都不守恒）
    expect_reject("flip-mu-minus-to-input",
                  {"right": {"in": ["q", "mu-"], "out": ["mu+"]}}, mom_full)
    # 2) 缝改由右 pants 生出（无输入却输出三个）
    expect_reject("seam-as-output-of-right-pant",
                  {"right": {"in": [], "out": ["q", "mu-", "mu+"]}}, mom_full)
    # 3) 少一个端口：2 端口 = 柱面，不是 pants（AEG Prop 10.2(1)）
    expect_reject("two-port-right-pant-becomes-cylinder",
                  {"right": {"in": ["q"], "out": ["mu-"]}}, mom_full)
    # 4) 端口别名
    expect_reject("aliased-port-on-right-pant",
                  {"right": {"in": ["q"], "out": ["q", "mu-"]}}, mom_full)
    # 5) 四个外线端口全挤到一个 pants 上（5 端口 = 五孔球，不是 pants）
    expect_reject("five-port-left-pant",
                  {"left": {"in": ["e-", "e+", "mu-", "mu+"], "out": ["q"]}}, mom_full)
    result["negative_controls"] = negatives

    # --- 正对照：正确的装饰要能一路通过 ---
    for label, pant in DECOR_QED.items():
        conservation(pant, mom_full, label)
    result["positive_control"] = "两个 pants 的动量与电荷残差全为零"
    return result


# ======================================================================
# 总报告
# ======================================================================
def run(baseline_path=None):
    report = {"schema": "oq096-pants-interface-v2-qed-report",
              "status": "three-layers-reported",
              "provenance": {
                  "geometry_layer": "verbatim from ~/AEG/aeg-paper/research/pants-interface-disks/verify_v1.py",
                  "v1_sha256": "fac64f82cea293ef58de9d0f1929ab4d3164d380b4d63f37be7a15b6fcfe644f",
                  "verifier_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  "aeg_baseline_read_only": "b77ca915902670863cd718e1df3f308defa59ad2"},
              "L1_topology": layer1(baseline_path),
              "L2_decoration": layer2(),
              "L3_semantics": layer3(),
              "limitations": [
                  "L1 的几何是 V1 的固定夹具（两盒一管），不是通用构造：它只证明这一个有限对象",
                  "L3 的动量模型是一维格点、质量为零；三维角度只用 z=(1+cosθ)/2 的对应关系表述",
                  "L3 只检查荷/动量守恒与确定性，不含任何传播子权重或振幅",
                  "没有 Adva 原生执行、没有 Seal、没有修改 AEG 仓库"]}
    return report


def main():
    baseline = str(Path(__file__).with_name("..") / "pants-v2-qed-baseline-v1.json")
    report = run(baseline)
    if "--check" in sys.argv:
        L1, L2, L3 = report["L1_topology"], report["L2_decoration"], report["L3_semantics"]
        print("[L1] 拓扑层：两种装饰下几何字段完全相同 =", L1["geometry_fields_identical"],
              "| 与 V1 已存基线一致 =", L1.get("matches_saved_V1_baseline"))
        print("     side χ =", L1["surfaces"]["side"]["chi"], "| 秩 =",
              L1["side_homology"]["boundary_matrix_rank"], "->",
              L1["side_homology"]["augmented_rank"], "| 体 χ =", L1["volume_chi"])
        print("[L2] 装饰层：")
        for k, v in L2.items():
            if k != "d_port_direction_never_read":
                print("     ", k, "->", v.get("result"), v.get("reason", v.get("exception", "")))
        print("[L3] 语义层：前像数 =", L3["determinism"]["creation_1_to_2_preimages"],
              "| 是否函数 =", L3["determinism"]["is_a_function"])
        for name, tbl in L3["weight_on_preimage_set"]["cases"].items():
            print("     %-16s q=%s s=%s N=%d 权重和=%s 常权和=%s 峰谷比=%s"
                  % (name, tbl["seam_q"], tbl["seam_s"], len(tbl["rows"]),
                     tbl["sum_of_physical_weights"], tbl["sum_if_no_weight (flat)"],
                     tbl["max_over_min"]))
        print("     负对照拒绝数 =", len(L3["negative_controls"]), "/ 5")
    else:
        print(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
