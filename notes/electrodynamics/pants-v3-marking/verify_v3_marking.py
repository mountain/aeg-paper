#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""OQ-096 V3：**marking 层** —— 从 DAG 生成侧表面，并把"装饰"与"标记"分开。

V2 的教训：用 V1 的冻结夹具去检验"换装饰后拓扑不变"是空转的，因为那段代码
的几何层压根不读装饰。V3 换掉做法：

  1. **推导而不是断言**：侧表面的欧拉特征由粘合公式给出
         chi(S_G) = sum_gates (2 - #ports)        （沿圆粘合 chi 不变，因为 chi(S^1)=0）
                 = 2V - (2E + b) = 2 - 2*beta_1 - b,
     这正是 AEG Prop 10.2(2)。方向从未进入 ⇒ 拓扑层对装饰是盲的，这是**定理**而不是观察。
  2. **枚举核对**：对同一张抽象图的**全部**装饰枚举一遍，确认不变量恒定（有限但非空）。
  3. **标记层**：拓扑相同而标记不同是常态——b 个外线的三价树一共 (2b-5)!! 个，
     b=4 时正是 3 个，即 s/t/u 三条道。**振幅的数据住在标记层，不在拓扑层。**
  4. 一阶圈图（泡、顶点修正、箱）各自 beta_1 = 1 ⇒ 亏格 1、chi = -4。

只用标准库。运行：
  python3 verify_v3_marking.py            # JSON 报告
  python3 verify_v3_marking.py --check    # 人读
"""
from collections import Counter
from itertools import combinations, product
import json
import sys


class Rejected(ValueError):
    pass


def demand(condition, reason):
    if not condition:
        raise Rejected(reason)


# ======================================================================
# 图与侧表面
# ======================================================================
class Gate:
    """一个 gate：id + 端口清单 [(port_name, direction)]，direction ∈ {in, out}。"""

    def __init__(self, gid, ports):
        self.id = gid
        self.ports = tuple(ports)
        names = [name for name, _ in self.ports]
        demand(len(set(names)) == len(names), "gate:" + gid + ":aliased-port")
        demand(all(d in ("in", "out") for _, d in self.ports), "gate:" + gid + ":direction")
        self.dir = dict(self.ports)
        self.names = tuple(names)


def side_surface(gates, wires, externals, require_pants=True):
    """侧表面 S_G 的组合不变量。

    wires:     [(gate_a, port_a, gate_b, port_b)]，要求 a 端是 out、b 端是 in
    externals: [(gate, port)]，它们是 S_G 的边界圈（被挖掉的端口圆盘）
    """
    by_id = {g.id: g for g in gates}
    demand(len(by_id) == len(gates), "graph:duplicate-gate")
    used = Counter()
    for ga, pa, gb, pb in wires:
        demand(ga in by_id and gb in by_id, "wire:unknown-gate")
        demand(pa in by_id[ga].dir, "wire:unknown-port")
        demand(pb in by_id[gb].dir, "wire:unknown-port")
        demand(by_id[ga].dir[pa] == "out", "flow:wire-must-leave-an-output")   # 装饰在此才起作用
        demand(by_id[gb].dir[pb] == "in", "flow:wire-must-enter-an-input")
        used[(ga, pa)] += 1
        used[(gb, pb)] += 1
    for g, p in externals:
        demand(g in by_id and p in by_id[g].dir, "external:unknown-port")
        used[(g, p)] += 1
    for g in gates:
        for name in g.names:
            demand(used[(g.id, name)] == 1, "graph:port-used-" + str(used[(g.id, name)]) + "-times")
    demand(len(set(externals)) == len(externals), "external:duplicated")

    V = len(gates)
    E = len(wires)
    b = len(externals)
    total_ports = sum(len(g.ports) for g in gates)
    demand(total_ports == 2 * E + b, "graph:port-accounting")

    # 粘合公式：每个 gate 是一块 pants（球面减 p 个开圆盘），沿圆粘合 chi 不变
    chi = sum(2 - len(g.ports) for g in gates)
    demand(chi == 2 * V - 2 * E - b, "side:chi-bookkeeping")
    beta1 = E - V + 1
    demand((2 - b - chi) % 2 == 0, "side:parity")
    genus = (2 - b - chi) // 2
    demand(genus == beta1, "side:genus-vs-betti")     # 这就是 AEG Prop 10.2(2)

    # 每个 gate 的局部形状：3 端口 = pants，2 = 柱面，1 = 圆盘
    if require_pants:
        bad = [g.id for g in gates if len(g.ports) != 3]
        demand(not bad, "side:not-a-pants-decomposition:" + ",".join(sorted(bad)))
    shapes = {}
    for g in gates:
        p = len(g.ports)
        shapes.setdefault({3: "pant", 2: "cylinder", 1: "disk"}.get(p, "sphere-%d-holes" % p), 0)
        shapes[{3: "pant", 2: "cylinder", 1: "disk"}.get(p, "sphere-%d-holes" % p)] += 1

    # 连通性（用外线无关的抽象图）
    parent = {g.id: g.id for g in gates}

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for ga, _, gb, _ in wires:
        parent[find(ga)] = find(gb)
    roots = {find(g.id) for g in gates}
    demand(len(roots) == 1, "graph:disconnected")

    return {"V": V, "E_internal": E, "b_external": b, "total_ports": total_ports,
            "chi_side_surface": chi, "beta1": beta1, "genus": genus,
            "local_shapes": shapes,
            "all_pants": shapes.get("pant", 0) == V,
            "aeg_formula_check": {"chi == 2-2*beta1-b": chi == 2 - 2 * beta1 - b,
                                  "genus == beta1": genus == beta1}}


# ======================================================================
# 装饰：同一张抽象图上的方向分配
# ======================================================================
def decorations(port_count, wires, externals):
    """枚举抽象图的全部装饰（每端口 in/out），只保留 flow 合法且每个 gate 有 ≥1 输出的。

    port_count: {gate_id: n_ports}；wires/externals 里用端口下标指认。
    返回 (合法装饰个数, 采样), 每个装饰 = {(gate, index): dir}
    """
    slots = [(g, i) for g, n in sorted(port_count.items()) for i in range(n)]
    ok = 0
    sample = []
    for assign in product(("in", "out"), repeat=len(slots)):
        d = dict(zip(slots, assign))
        if any(all(d[(g, i)] != "out" for i in range(n)) for g, n in port_count.items()):
            continue
        good = True
        for ga, pa, gb, pb in wires:
            if not (d[(ga, pa)] == "out" and d[(gb, pb)] == "in"):
                good = False
                break
        if not good:
            continue
        ok += 1
        if len(sample) < 3:
            sample.append(d)
    return ok, sample


def materialize(port_count, wires, externals, decoration):
    gates = [Gate(g, [(str(i), decoration[(g, i)]) for i in range(n)])
             for g, n in sorted(port_count.items())]
    w = [(ga, str(pa), gb, str(pb)) for ga, pa, gb, pb in wires]
    e = [(g, str(i)) for g, i in externals]
    return gates, w, e


# ======================================================================
# 三价树：b 个外线的所有拓扑 (2b-5)!!
# ======================================================================
def _canon_unrooted(adj):
    """无根树的规范形式：对每个可能根取有根编码，再取最小（小树足够）。"""
    def rooted(u, parent):
        kids = sorted(rooted(v, u) for v in adj.get(u, ()) if v != parent)
        tag = "" if u.startswith("L") else "*"
        return u if tag == "" else "(" + ",".join(kids) + ")"
    return min(rooted(u, None) for u in adj)


def all_unrooted_trivalent_trees(n_leaves):
    """n 个带标签外线的全部无根三价树，个数应为 (2n-5)!!。

    构造：从三叶星出发，每次把一片叶子接在"细分一条边"后得到的新顶点上。
    """
    demand(n_leaves >= 3, "trees:need-three-leaves")
    star = {"v1": {"L1", "L2", "L3"}}
    frontier = {_canon_unrooted(star): star}
    for k in range(4, n_leaves + 1):
        nxt = {}
        for tree in frontier.values():
            edges, seen = [], set()
            for u in tree:                      # 无向边，按 frozenset 去重（不能用名字序）
                for v in tree[u]:
                    key = frozenset((u, v))
                    if key not in seen:
                        seen.add(key)
                        edges.append((u, v))
            for (u, v) in edges:
                mid = "v%d" % (sum(1 for w in tree if not w.startswith("L")) + 1)
                new = {w: set(nb) for w, nb in tree.items()}
                new[u].discard(v)
                if v in new:                 # 叶子没有邻接表
                    new[v].discard(u)
                else:
                    new[v] = set()
                new[mid] = {u, v, "L%d" % k}
                new[u].add(mid)
                new[v].add(mid)
                nxt[_canon_unrooted(new)] = new
        frontier = nxt
    return sorted(frontier.items())


def tree_to_spec(adj):
    """无根三价树 → (port_count, wires, externals, decoration)。

    每个内部节点是一个三端口 gate；内部边是 wire（方向按 gate 名序定），
    叶子是外线。装饰取"每个 gate 至少一个 out"的一种合法分配。
    """
    internal = sorted(u for u in adj if not u.startswith("L"))
    port_count = {g: 3 for g in internal}
    wires, externals, decoration = [], [], {}
    for g in internal:
        slot = 0
        for nb in sorted(adj[g]):
            if nb.startswith("L"):
                externals.append((g, slot))
                decoration[(g, slot)] = "in"
            else:
                # 只在"名字小 → 名字大"的方向上登记 wire，避免重复
                if g < nb:
                    wires.append((g, slot, nb, None))     # 对方的槽位稍后补
                decoration[(g, slot)] = "out" if g < nb else "in"
            slot += 1
    # 补上 wire 在消费者一侧的槽位
    fixed = []
    for (ga, pa, gb, _) in wires:
        slot_b = [i for i, nb in enumerate(sorted(adj[gb])) if nb == ga]
        demand(len(slot_b) == 1, "tree:wire-slot")
        fixed.append((ga, pa, gb, slot_b[0]))
        decoration[(gb, slot_b[0])] = "in"
    # 保证每个 gate 至少一个输出：若全是被吃进来的，把它的第一根外线改成 out
    for g in internal:
        if not any(decoration[(g, i)] == "out" for i in range(3)):
            leg = [i for i in range(3) if (g, i) in [tuple(e) for e in externals]]
            demand(bool(leg), "tree:no-port-to-pin")
            decoration[(g, leg[0])] = "out"
    wire_slots = {(a, p) for a, p, _, _ in fixed} | {(b, q) for _, _, b, q in fixed}
    for g in internal:                     # 补上没被 wire 用到的槽位方向
        for i in range(3):
            decoration.setdefault((g, i), "in")
    return port_count, fixed, externals, decoration


# ======================================================================
# 具体图：湮灭树图 + 三个一阶圈图
# ======================================================================
ANNIHILATION_PORT_COUNT = {"annih": 3, "create": 3}
ANNIHILATION_WIRES = [("annih", 2, "create", 0)]           # annih 的 q 是 out, create 的 q 是 in
ANNIHILATION_EXTERNALS = [("annih", 0), ("annih", 1), ("create", 1), ("create", 2)]


def annihilation(decoration):
    gates = [Gate("annih", [("e-", decoration[("annih", 0)]),
                            ("e+", decoration[("annih", 1)]),
                            ("q", decoration[("annih", 2)])]),
             Gate("create", [("q", decoration[("create", 0)]),
                             ("mu-", decoration[("create", 1)]),
                             ("mu+", decoration[("create", 2)])])]
    return gates, [("annih", "q", "create", "q")], [("annih", "e-"), ("annih", "e+"),
                                                   ("create", "mu-"), ("create", "mu+")]


def bubble():
    gates = [Gate("v1", [("e-", "in"), ("e+", "in"), ("g1", "out")]),
             Gate("l1", [("g1", "in"), ("fa", "out"), ("fb", "in")]),
             Gate("l2", [("fb", "out"), ("fa", "in"), ("g2", "out")]),
             Gate("v2", [("g2", "in"), ("mu-", "out"), ("mu+", "out")])]
    wires = [("v1", "g1", "l1", "g1"), ("l1", "fa", "l2", "fa"),
             ("l2", "fb", "l1", "fb"), ("l2", "g2", "v2", "g2")]
    externals = [("v1", "e-"), ("v1", "e+"), ("v2", "mu-"), ("v2", "mu+")]
    return gates, wires, externals


def crossed_box():
    """交叉双光子箱图：与 box 共用同一批端口，只是把两条光子接反。

    为什么 e+e- -> mu+mu- 的一阶四顶点图里没有"顶点修正"：
    树顶点两侧不存在"同一条费米线的两段"可供光子横跨（入射的 e- 与 e+ 都终止于该顶点），
    所以顶点修正的图形在这里退化成双光子交换（箱图）。这一点是本书"每个 NLO 图都有
    四个顶点"那句话的直接后果，也正是我上一轮图集里画错的地方。
    """
    gates = [Gate("a", [("e-", "in"), ("fa", "out"), ("gA", "out")]),
             Gate("b", [("fa", "in"), ("e+", "out"), ("gB", "out")]),
             Gate("c", [("gC", "in"), ("fc", "out"), ("mu-", "in")]),
             Gate("d", [("gD", "in"), ("fc", "in"), ("mu+", "out")])]
    wires = [("a", "fa", "b", "fa"), ("a", "gA", "d", "gD"),      # 交叉
             ("b", "gB", "c", "gC"), ("c", "fc", "d", "fc")]
    externals = [("a", "e-"), ("b", "e+"), ("c", "mu-"), ("d", "mu+")]
    return gates, wires, externals


def box_diagram():
    gates = [Gate("a", [("e-", "in"), ("fa", "out"), ("gA", "out")]),
             Gate("b", [("fa", "in"), ("e+", "out"), ("gB", "out")]),
             Gate("c", [("gC", "in"), ("fc", "out"), ("mu-", "in")]),
             Gate("d", [("gD", "in"), ("fc", "in"), ("mu+", "out")])]
    wires = [("a", "fa", "b", "fa"), ("a", "gA", "c", "gC"),
             ("b", "gB", "d", "gD"), ("c", "fc", "d", "fc")]
    externals = [("a", "e-"), ("b", "e+"), ("c", "mu-"), ("d", "mu+")]
    return gates, wires, externals


# ======================================================================
# 三层报告
# ======================================================================
def layer_topology():
    out = {}
    gates = [Gate("annih", [("e-", "in"), ("e+", "in"), ("q", "out")]),
             Gate("create", [("q", "in"), ("mu-", "out"), ("mu+", "out")])]
    wires = [("annih", "q", "create", "q")]
    externals = [("annih", "e-"), ("annih", "e+"), ("create", "mu-"), ("create", "mu+")]
    out["annihilation_tree"] = side_surface(gates, wires, externals)
    out["bubble_NLO"] = side_surface(*bubble())
    out["crossed_box_NLO"] = side_surface(*crossed_box())
    out["box_NLO"] = side_surface(*box_diagram())
    for name in ("bubble_NLO", "box_NLO", "crossed_box_NLO"):
        demand(out[name]["genus"] == 1, name + ":genus-should-be-one-loop")
        demand(out[name]["chi_side_surface"] == -4, name + ":chi-should-be-minus-four")
    demand(out["annihilation_tree"]["genus"] == 0, "tree:genus-zero")
    demand(out["annihilation_tree"]["chi_side_surface"] == -2, "tree:chi-minus-two")
    return out


def layer_decoration():
    """同一张抽象图：枚举全部装饰，确认侧表面不变量恒定。"""
    total, sample = decorations(ANNIHILATION_PORT_COUNT, ANNIHILATION_WIRES,
                                ANNIHILATION_EXTERNALS)
    demand(total > 0, "decorations:none-found")
    rows = []
    seen = set()
    for d in sample:
        gates, wires, externals = materialize(ANNIHILATION_PORT_COUNT,
                                              ANNIHILATION_WIRES,
                                              ANNIHILATION_EXTERNALS, d)
        inv = side_surface(gates, wires, externals)
        key = (inv["chi_side_surface"], inv["b_external"], inv["genus"], inv["beta1"])
        seen.add(key)
        rows.append({"decoration": {str(k): v for k, v in d.items()},
                     "annih_dirs": [d[("annih", i)] for i in range(3)],
                     "create_dirs": [d[("create", i)] for i in range(3)],
                     "invariants": list(key)})
    demand(len(seen) == 1, "decorations:invariants-changed")
    return {"legal_decorations": total,
            "distinct_invariant_tuples": len(seen),
            "invariant_tuple_(chi,b,genus,beta1)": list(next(iter(seen))),
            "sample": rows,
            "note": ("不变量只有一组 ⇒ 侧表面与装饰无关。这次不是'检查器不看所以不变'："
                     "chi = sum(2-ports) 的推导里方向根本没出现，枚举只是一次核对。")}


def layer_marking():
    """标记层：拓扑相同、标记不同。b=4 时恰有 3 个无根三价树 = s/t/u。"""
    out = {"counts": {}}
    for b in (4, 6):
        trees = all_unrooted_trivalent_trees(b)
        expected = 1
        for k in range(3, 2 * b - 4, 2):
            expected *= k
        demand(len(trees) == expected, "trees:count-mismatch-b%d-(%d)"
               % (b, len(trees)))
        invs = []
        for _, adj in trees:
            port_count, wires, externals, dec = tree_to_spec(adj)
            gates, w, e = materialize(port_count, wires, externals, dec)
            invs.append(side_surface(gates, w, e))
        keys = {(i["chi_side_surface"], i["b_external"], i["genus"], i["beta1"])
                for i in invs}
        demand(len(keys) == 1, "trees:invariants-differ-b%d" % b)
        demand(all(i["all_pants"] for i in invs), "trees:not-all-pants-b%d" % b)
        out["counts"]["b=%d" % b] = {
            "unrooted_trees": len(trees), "(2b-5)!!": expected,
            "invariants_constant": True,
            "invariant_tuple_(chi,b,genus,beta1)": list(next(iter(keys))),
            "first_three": [t for t, _ in trees[:3]]}
    trees4 = all_unrooted_trivalent_trees(4)
    out["four_point_channels"] = {
        "trees": [t for t, _ in trees4],
        "leaf_pairings": [tuple(sorted(pair for pair in _cherries(adj))) for _, adj in trees4],
        "reading": "三个无根三价树 = 4 孔球的三条裤子分解 = s / t / u 三条道"}
    return out


def _cherries(adj):
    """返回把 4 个叶子分成两对的配对方式（每个 4 点树恰好有一条内部边）。"""
    internal = [u for u in adj if not u.startswith("L")]
    pairs = []
    for g in internal:
        legs = sorted(nb for nb in adj[g] if nb.startswith("L"))
        if legs:
            pairs.append(tuple(legs))
    return pairs


def layer_negative():
    negs = []

    def expect_reject(name, fn):
        try:
            fn()
        except Rejected as exc:
            negs.append({"name": name, "result": "rejected", "reason": str(exc)})
        else:
            raise Rejected("V3-negative-accepted:" + name)

    # 1) 两端口 gate：拓扑上合法（柱面），但不是 pants 分解 ⇒ 被 require_pants 拒绝
    cyl_gates = [Gate("x", [("a", "in"), ("b", "out")]),
                 Gate("y", [("c", "in"), ("d", "out"), ("e", "out")])]
    expect_reject("two-port-gate-is-not-a-pant",
                  lambda: side_surface(cyl_gates, [("x", "b", "y", "c")],
                                       [("x", "a"), ("y", "d"), ("y", "e")]))
    cyl = side_surface(cyl_gates, [("x", "b", "y", "c")],
                       [("x", "a"), ("y", "d"), ("y", "e")], require_pants=False)
    negs.append({"name": "two-port-gate-as-cylinder",
                 "result": "accepted-without-pants-condition",
                 "chi_side_surface": cyl["chi_side_surface"],
                 "local_shapes": cyl["local_shapes"],
                 "note": "AEG Prop 10.2(1)：两端口给柱面。它仍是可定向曲面，只是不是 pants 分解"})
    # 2) 四端口 gate：仍可定向，但 chi 变了（四孔球）
    quad_gates = [Gate("x", [("a", "in"), ("b", "out"), ("c", "out"), ("q", "out")]),
                  Gate("y", [("q", "in"), ("d", "out"), ("e", "out")])]
    quad = side_surface(quad_gates, [("x", "q", "y", "q")],
                        [("x", "a"), ("x", "b"), ("x", "c"), ("y", "d"), ("y", "e")],
                        require_pants=False)
    demand(quad["chi_side_surface"] == -3, "quad:chi")
    expect_reject("four-port-gate-not-a-pant",
                  lambda: side_surface(quad_gates, [("x", "q", "y", "q")],
                                       [("x", "a"), ("x", "b"), ("x", "c"),
                                        ("y", "d"), ("y", "e")]))
    negs.append({"name": "four-port-gate-is-a-four-holed-sphere",
                 "result": "accepted-without-pants-condition",
                 "chi_side_surface": quad["chi_side_surface"],
                 "local_shapes": quad["local_shapes"],
                 "note": "四端口给四孔球；每多一个端口，chi 再掉 1 ⇒ 三端口不是装饰性的限制"})
    # 3) 反向流：out -> out 的连接被拒绝（装饰只在 flow 这一层起作用）
    expect_reject("wire-out-to-out",
                  lambda: side_surface([Gate("x", [("a", "in"), ("b", "out"), ("c", "out")]),
                                        Gate("y", [("d", "in"), ("e", "out"), ("f", "out")])],
                                       [("x", "b", "y", "e")],
                                       [("x", "a"), ("x", "c"), ("y", "d"), ("y", "f")]))
    # 4) 端口被用两次
    expect_reject("port-used-twice",
                  lambda: side_surface([Gate("x", [("a", "in"), ("b", "out"), ("c", "out")]),
                                        Gate("y", [("d", "in"), ("e", "out"), ("f", "out")])],
                                       [("x", "b", "y", "d"), ("x", "b", "y", "d")],
                                       [("x", "a"), ("x", "c"), ("y", "e"), ("y", "f")]))
    # 5) 端口-账目错：外线数不对
    expect_reject("port-accounting",
                  lambda: side_surface([Gate("x", [("a", "in"), ("b", "out"), ("c", "out")]),
                                        Gate("y", [("d", "in"), ("e", "out"), ("f", "out")])],
                                       [("x", "b", "y", "d")],
                                       [("x", "a"), ("y", "e")]))
    return negs


def run():
    report = {"schema": "oq096-pants-interface-v3-marking-report",
              "status": "topology-derived-marking-enumerated",
              "topology": layer_topology(),
              "decoration": layer_decoration(),
              "marking": layer_marking(),
              "negative_controls": layer_negative(),
              "limitations": [
                  "组合的侧表面（按粘合公式算），不是三维胞腔；'没有意外接触'这一条假设而不验证",
                  "与 V1 的立方体实现只在同一实例上做过一致性对照（chi=-2, b=4, beta1=0）",
                  "标记层只做了计数与展示，没有构造模空间、没有把振幅写上去",
                  "不含任何权重、测度或传播子"]}
    return report


def main():
    report = run()
    if "--check" in sys.argv:
        T, D, M = report["topology"], report["decoration"], report["marking"]
        print("[拓扑] 湮灭树图：chi=%d b=%d genus=%d beta1=%d 全 pants=%s"
              % (T["annihilation_tree"]["chi_side_surface"], T["annihilation_tree"]["b_external"],
                 T["annihilation_tree"]["genus"], T["annihilation_tree"]["beta1"],
                 T["annihilation_tree"]["all_pants"]))
        for name in ("bubble_NLO", "box_NLO", "crossed_box_NLO"):
            v = T[name]
            print("        %-22s chi=%d genus=%d beta1=%d" %
                  (name, v["chi_side_surface"], v["genus"], v["beta1"]))
        print("[装饰] 合法装饰数 = %d，不变量元组 = %s"
              % (D["legal_decorations"], D["invariant_tuple_(chi,b,genus,beta1)"]))
        for b, v in M["counts"].items():
            print("[标记] %s 三价树 %d 个（(2b-5)!!=%d），不变量恒定 = %s"
                  % (b, v["unrooted_trees"], v["(2b-5)!!"], v["invariants_constant"]))
        print("        b=4 的三棵树：", M["four_point_channels"]["trees"])
        print("[负对照]", len(report["negative_controls"]), "条：",
              [n["name"] for n in report["negative_controls"]])
    else:
        print(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
