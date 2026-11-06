#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""OQ-096 V4：M1 的最小尝试 —— 值层能不能承载缝上的核？

M1 原本的措辞是"缺缝上的权重（传播子核）"。本文件把它拆成三个可判定的问题，
用精确代数（sympy）与精确有理数回答：

  K1  未加权的拼接是什么？            —— 消去接口变量，核对 AEG Prop 10.9 的 fiber product。
  K2  有理核能不能放进值层？          —— 用局部化表示 1/sigma，检查拼接是否还与它相容。
  K3  局部化与拼接可交换吗？          —— 即"先加权后拼接"是否等于"先拼接后加权"。
  K4  极点处会发生什么？              —— 在 sigma = m^2 处取纤维，看值层还剩什么。
  K5  物理权重是不是接口值的函数？    —— 用 V2 的有限运动学精确枚举：
                                         同一个 sigma 下不同拆分的权重是否相同。

结论预告（见 §4）：M1 的真内容不是"adjoin 1/sigma"，而是"在纤维上放一个测度"。
AEG 的拼接是 colimit，它把纤维压成一点；而物理的权重是定义在纤维上的函数。
"""
import json
import sys
from fractions import Fraction

import sympy as sp

x, y, z, t, w, zi, sigma, m2 = sp.symbols("x y z t w zi sigma m2")


def groebner_basis(gens, order_vars):
    return sp.groebner(gens, *order_vars, order="lex")


def is_one_in_ideal(gens, variables):
    """1 是否落在理想里（⇒ 商环是零环）。"""
    G = sp.groebner(gens, *variables, order="lex")
    remainder = G.reduce(sp.Integer(1))[1]
    return sp.simplify(remainder) == 0


def same_ideal(gens_a, gens_b, variables):
    """两个理想是否相等（互相归约都为零）。"""
    Ga = sp.groebner(gens_a, *variables, order="lex")
    Gb = sp.groebner(gens_b, *variables, order="lex")
    a_in_b = all(sp.simplify(Gb.reduce(g)[1]) == 0 for g in gens_a)
    b_in_a = all(sp.simplify(Ga.reduce(g)[1]) == 0 for g in gens_b)
    return a_in_b and b_in_a


# ======================================================================
# K1：有理核放在值层里 —— 局部化表示 1/sigma，且与拼接可交换
# ======================================================================
def k1_localisation():
    # 拼接前的两块代数（AEG Prop 10.9）
    left = [z - (x + y)]                    # Q[x,y,z]/(z-x-y)      加法 gate
    right = [w - z * t]                     # Q[z,t,w]/(w-zt)       乘法 gate
    # 未加权的拼接：消去 z
    glued = left + right
    eliminated = sp.groebner(glued, z, x, y, t, w, order="lex")
    expected = [w - (x + y) * t]
    unweighted_ok = same_ideal(glued, expected + [z - (x + y)], [x, y, z, t, w])

    # 加权：把接口 z 换成可逆的（局部化 = 附加 zi 与关系 z*zi-1）
    localize = [z * zi - 1]
    left_loc = [z - (x + y)] + localize
    right_loc = [w - z * t] + localize
    glued_loc = left_loc + right_loc
    # 期望：Q[x,y,t,w,zi]/(w-(x+y)t, (x+y)zi-1)
    expected_loc = [w - (x + y) * t, (x + y) * zi - 1]
    weighted_ok = same_ideal(glued_loc, expected_loc + [z - (x + y)], [x, y, z, t, w, zi])

    # 交换性：先拼接后局部化 == 先局部化后拼接
    composite_unweighted = [w - (x + y) * t]           # 已无 z
    localised_after = composite_unweighted + [(x + y) * zi - 1]
    commute_ok = same_ideal(localised_after, expected_loc, [x, y, t, w, zi])

    return {"K1_unweighted_gluing": {
                "claim": "glue(Q[x,y,z]/(z-x-y), Q[z,t,w]/(w-zt)) = Q[x,y,t,w]/(w-(x+y)t)",
                "result": "PASS" if unweighted_ok else "FAIL"},
            "K2_pole_in_the_value_layer": {
                "claim": "局部化后拼接 = Q[x,y,t,w,zi]/(w-(x+y)t, (x+y)zi-1)，"
                         "即权重 1/sigma 是环里的一**个元素**",
                "result": "PASS" if weighted_ok else "FAIL"},
            "K3_localisation_commutes_with_gluing": {
                "claim": "局部化与 fiber product 可交换（局部化是平坦的）",
                "result": "PASS" if commute_ok else "FAIL"},
            "note": ("有理核能被值层承载：1/sigma 只是把接口代数局部化。"
                     "但注意它进的是**环**，不是拼接的权重——它乘在整个拼接结果上，"
                     "并且在 sigma 固定时是一个常数。")}


# ======================================================================
# K2：极点处值层塌掉（这才是 1/sigma 真正的代价）
# ======================================================================
def k2_pole():
    # 在 sigma = 0 处取接口的纤维：把 z=0 加进局部化理想，看是否为零环
    localized_interface = [z * zi - 1]
    fiber_at_zero = localized_interface + [z]
    zero_ring = is_one_in_ideal(fiber_at_zero, [z, zi])
    # 未局部化时，z=0 是正常点：Q[z]/(z) = Q，非零环
    plain_fiber = is_one_in_ideal([z], [z])
    # 有质量的情形：局部化在 (sigma - m^2)，纤维在 sigma = m^2 同样塌掉
    massive = [(z - m2) * zi - 1]
    massive_fiber = massive + [z - m2]
    massive_zero = is_one_in_ideal(massive_fiber, [z, zi, m2])
    return {"K4_fiber_over_the_pole": {
                "claim": "局部化接口在 sigma=0 上的纤维是零环（1 in ideal）",
                "result": "PASS（零环）" if zero_ring else "FAIL（仍是非零环）",
                "plain_fiber_nonzero": (not plain_fiber),
                "massive_pole_also_collapses": massive_zero},
            "reading": ("把 1/sigma 放进环里，代价是**恰好那一点（光子极点 sigma=0）从谱里消失**。"
                        "无质量光子的在壳点就是这里；有质量时是 sigma=m^2。"
                        "所以 AEG 值层（Spec 字符）与传播子核**在极点上不相容**："
                        "要么放弃 1/sigma，要么放弃那一点的字符读数。")}


# ======================================================================
# K3：物理权重是不是接口值的函数？（V2 的有限运动学，精确有理数）
# ======================================================================
GRID = tuple(range(-6, 7))


def onshell(k):
    return (Fraction(abs(k)), Fraction(k))


def splits(q):
    out = []
    for k3 in GRID:
        p3 = onshell(k3)
        for k4 in GRID:
            p4 = onshell(k4)
            if (p3[0] + p4[0], p3[1] + p4[1]) == q:
                out.append((k3, k4))
    return out


def k3_weight_is_not_a_function_of_sigma():
    table = {}
    for (k1, k2) in [(2, 3), (2, -1)]:
        p1, p2 = onshell(k1), onshell(k2)
        q = (p1[0] + p2[0], p1[1] + p2[1])
        s = q[0] ** 2 - q[1] ** 2
        rows = []
        for (k3, k4) in splits(q):
            e3, e4 = Fraction(abs(k3)), Fraction(abs(k4))
            zz = e3 / (e3 + e4)
            cos = 2 * zz - 1
            rows.append({"split": [k3, k4], "z": str(zz), "cos": str(cos),
                         "weight": str(1 + cos * cos)})
        ws = [Fraction(r["weight"]) for r in rows]
        table["e-=%d,e+=%d" % (k1, k2)] = {
            "sigma_s": str(s), "n_splits": len(rows),
            "weights": [str(v) for v in ws],
            "distinct_weights": len(set(ws)),
            "max_over_min": str(max(ws) / min(ws)) if ws else None,
            "rows": rows}
    # 判定：同一个 sigma 下若权重大小不同，则权重不是 sigma 的函数
    decisive = [k for k, v in table.items() if v["distinct_weights"] > 1]
    same = all(v["distinct_weights"] == 1 for v in table.values())
    return {"K5_weight_is_not_a_function_of_the_interface_value": {
                "claim": "若权重只是接口值 sigma 的函数，则同一 sigma 下所有权重必相等",
                "result": "PASS（被否证）" if decisive else ("FAIL（未否证）" if not same else "权重相等"),
                "counterexamples": decisive,
                "detail": table},
            "reading": ("sigma=0 那一格有 6 个拆分，权重从 26/25 到 2（峰谷比 25/13），"
                        "而它们共享同一个接口值。⇒ 任何 f(sigma) 都给不出这个权重。"
                        "缺失的权重不是接口值的函数，而是**纤维（拆分）上的函数**。")}


# ======================================================================
# §4：结论与下一步的形态
# ======================================================================
def conclusion():
    return {
        "what_M1_really_is": (
            "M1 不是'把 1/sigma 加到缝上'——那件事值层已经能做（K2）。"
            "M1 是'在纤维上放一个测度'：AEG 的拼接是 colimit（把两侧的接口值等同，"
            "纤维被压成一点），而物理权重是定义在**纤维**（同一接口值下的全部拆分）上的函数。"
            "colimit 在范畴层面就丢掉了它，所以这不是补一个系数的问题。"),
        "when_a_fiber_sum_actually_appears": (
            "必须说清楚：树级、且末态全部被探测时，**没有对纤维的求和**——"
            "振幅就是顶点缩并在那个（唯一的）末态上的取值，此时需要的是 M2（标签缩并），"
            "不是 M1（核）。对纤维的求和只在'有东西没被观测/被量子化'时出现："
            "总截面（对末态求和）、圈图（对缝上动量求和）。K5 的反例正是总截面这一侧。"),
        "consequence_for_the_gap_list": (
            "M1 与 M2 不是两个独立缺口：树级振幅里传播子 1/s 对外线固定时是常数，"
            "角度依赖全部来自顶点张量（标签缩并）。所以'tree 级缺权重'应改写为"
            "'缺 M2 的标签缩并，而它表现为纤维上的非平凡权重'。"
            "M1（核）真正必需的场合是**圈图**：那里缝上的动量不被外线固定，"
            "1/(sigma-m^2) 随积分变量变化，f(sigma) 这一形态才是对的。"),
        "what_a_positive_construction_must_look_like": [
            "在接口上放一个配对/迹（bimodule + trace），而不是只放一个同构 z ↦ x+y；",
            "拼接后用该配对取值，而不是用字符取值（字符在极点处恰好消失，见 K4）；",
            "顶点的表示标签（M2）进入这个配对，角度依赖才可能出现。",
        ],
        "what_this_does_not_do": [
            "没有构造出任何振幅；连一个标量因子都没算进截面",
            "没有处理 iε：局部化是代数的，没有解析延拓",
            "没有把 (1+cos^2 theta) 从 Pant 结构里推出来——K5 只是证明它**不能**来自 f(sigma)",
        ],
    }


def run():
    report = {"schema": "oq096-pants-interface-v4-kernel-report",
              "status": "m1-minimal-attempt",
              "k1_localisation": k1_localisation(),
              "k2_pole": k2_pole(),
              "k3_kinematics": k3_weight_is_not_a_function_of_sigma(),
              "conclusion": conclusion(),
              "limitations": [
                  "只处理有理核 1/sigma 与 1/(sigma-m^2)，不含 iε、不含色散关系",
                  "局部化的'交换性'检验在多项式环片段内完成，未讨论解析完备化",
                  "运动学仍是一维格点、质量为零（沿用 V2），三维角度只经 z=(1+cos)/2 对应",
                  "没有 Adva 原生执行，没有修改 AEG 仓库"]}
    return report


def main():
    report = run()
    if "--check" in sys.argv:
        a = report["k1_localisation"]
        for key in ("K1_unweighted_gluing", "K2_pole_in_the_value_layer",
                    "K3_localisation_commutes_with_gluing"):
            print("[值层]", key, "->", a[key]["result"])
        b = report["k2_pole"]
        print("[极点]", b["K4_fiber_over_the_pole"]["result"],
              "| 未局部化时纤维非零:", b["K4_fiber_over_the_pole"]["plain_fiber_nonzero"],
              "| 有质量时同样塌:", b["K4_fiber_over_the_pole"]["massive_pole_also_collapses"])
        c = report["k3_kinematics"]["K5_weight_is_not_a_function_of_the_interface_value"]
        print("[判据]", c["result"], "| 反例:", c["counterexamples"])
        for k, v in report["k3_kinematics"]["K5_weight_is_not_a_function_of_the_interface_value"]["detail"].items():
            print("        %-14s sigma=%s 拆分 %d 个，权重 %d 种，峰谷比 %s"
                  % (k, v["sigma_s"], v["n_splits"], v["distinct_weights"], v["max_over_min"]))
        print("[结论]", report["conclusion"]["what_M1_really_is"][:120], "...")
    else:
        print(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
