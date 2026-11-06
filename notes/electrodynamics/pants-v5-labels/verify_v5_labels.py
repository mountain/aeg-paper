#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""OQ-096 V5：M2 的最小尝试 —— 端口标签 + 不变量张量 + 缝上的表示空间与转动。

V4 的结论是：缺的权重是**纤维上的测度**，且它不是接口值 sigma 的函数。V5 检验一个具体的
正面猜想：那个测度是不是"缝上表示空间的缩并 + 沿缝的转动"。

三个问题，全部用精确符号代数（sympy，系数含 sqrt2 也保持精确）：

  P1  单看 SU(2) 标签规则，能定出哪些顶点存在吗？        —— 整数总自旋 + 三角不等式；
                                                            反例：它允许 (1,1,1)，而 QED 由 C 宇称禁止。
  P2  "16 种螺旋度组合只剩 4 种"是标签层的事还是动力学的事？—— 在每个 pants 上做 m 求和，
                                                            并区分"缝有 3 个态"与"缝只有横模 2 个态"。
  P3  角度依赖能不能从标签一侧算出来？                  —— 把缝上的转动写成 Wigner d^1(theta)，
                                                            看四个非零振幅是否恰好等于 (1±cos)/2。

结论预告：能。而这个结果**不含 s**——与 V4 的 K5（权重不是 sigma 的函数）互相印证。
"""
import json
import sys

import sympy as sp

c, s = sp.symbols("c s", real=True)          # c = cos(theta), s = sin(theta)
sqrt2 = sp.sqrt(2)


# ======================================================================
# P1：SU(2) 标签规则（用 2j 的整数运算，完全精确）
# ======================================================================
def allowed_triple(d1, d2, d3):
    """三价顶点存在不变量的充要条件（SU(2)）：总自旋为整数 + 三角不等式。"""
    if (d1 + d2 + d3) % 2 != 0:              # j1+j2+j3 必须是整数
        return False
    return abs(d1 - d2) <= d3 <= d1 + d2


def p1_selection_rules():
    labels = {1: "1/2", 2: "1", 3: "3/2", 4: "2"}
    allowed, forbidden = [], []
    for d1 in sorted(labels):
        for d2 in sorted(labels):
            for d3 in sorted(labels):
                trip = tuple(sorted((d1, d2, d3)))
                entry = tuple(labels[d] for d in trip)
                if allowed_triple(*trip):
                    if entry not in allowed:
                        allowed.append(entry)
                else:
                    if entry not in forbidden:
                        forbidden.append(entry)
    # QED 顶点与几个"被别的定则禁掉"的对照
    qed_ok = allowed_triple(1, 1, 2)          # (1/2, 1/2, 1)
    half_half_half = allowed_triple(1, 1, 1)  # (1/2, 1/2, 1/2)：总自旋 3/2 不是整数
    three_photon = allowed_triple(2, 2, 2)    # (1, 1, 1)：SU(2) 允许，QED 由 C 宇称禁止
    return {
        "rule": "allowed(d1,d2,d3) <=> (d1+d2+d3) 为偶数 且 |d1-d2| <= d3 <= d1+d2   [d = 2j]",
        "allowed_triples_up_to_j=2": [list(t) for t in allowed],
        "forbidden_triples_up_to_j=2": [list(t) for t in forbidden],
        "qed_vertex_(1/2,1/2,1)_allowed": qed_ok,
        "(1/2,1/2,1/2)_allowed": half_half_half,
        "(1,1,1)_allowed_by_SU2": three_photon,
        "verdict": ("SU(2) 标签规则能排除 (1/2,1/2,1/2)，但**允许 (1,1,1)**；"
                    "QED 里三光子顶点由 C 宇称（Furry 定理）禁止，不由 SU(2) 禁止。"
                    "⇒ 标签规则**不足以**定出顶点集合，还必须带一个额外的选择定则（C 奇偶）。"),
    }


# ======================================================================
# P2/P3：缝上的表示空间、CG 系数与沿缝的转动
# ======================================================================
# CG：<1 m | 1/2 h1 ; 1/2 h2>，h 用 ±1 表示 ±1/2（倍乘 2）
#   只有总 m = (h1+h2)/2 的那个 m 非零
CG = {
    (+1, +1): {+1: sp.Integer(1)},                                   # |1,1>  = |++>
    (+1, -1): {0: 1 / sqrt2},                                        # |1,0>  = (|+->+| -+>)/sqrt2
    (-1, +1): {0: 1 / sqrt2},
    (-1, -1): {-1: sp.Integer(1)},                                    # |1,-1> = |-->
}


def d1_matrix():
    """spin-1 的 Wigner 小 d 矩阵（螺旋度基），索引顺序 m = +1, 0, -1。"""
    return sp.Matrix([
        [(1 + c) / 2, -s / sqrt2, (1 - c) / 2],
        [s / sqrt2, c, -s / sqrt2],
        [(1 - c) / 2, s / sqrt2, (1 + c) / 2],
    ])


M_INDEX = {+1: 0, 0: 1, -1: 2}


def amplitude(h1, h2, h3, h4, transverse_only=True):
    """A(h1,h2 -> h3,h4) = sum_{m,m'} CG_e(m) * d^1_{m,m'}(theta) * CG_mu(m')。

    两边都是"粒子-反粒子对"，反粒子腿的 m 取反（h -> -h）；这是配对进入不变量的标准约定。
    """
    e_side = CG[(h1, -h2)]                  # e-:h1（粒子）, e+: -h2（反粒子取反）
    mu_side = CG[(h3, -h4)]                 # mu-:h3, mu+: -h4
    D = d1_matrix()
    m_modes = (+1, -1) if transverse_only else (+1, 0, -1)
    total = sp.Integer(0)
    for m in m_modes:
        for mp in m_modes:
            ce = e_side.get(m, 0)
            cm = mu_side.get(mp, 0)
            if ce == 0 or cm == 0:
                continue
            total += ce * D[M_INDEX[m], M_INDEX[mp]] * cm
    return sp.simplify(total)


def p2_p3_amplitudes():
    helicities = (+1, -1)          # ±1/2（倍乘 2）
    rows = []
    nonzero = 0
    for h1 in helicities:
        for h2 in helicities:
            for h3 in helicities:
                for h4 in helicities:
                    a = amplitude(h1, h2, h3, h4, transverse_only=True)
                    label = "%s%s->%s%s" % tuple("↑" if h > 0 else "↓"
                                                 for h in (h1, h2, h3, h4))
                    if sp.simplify(a) != 0:
                        nonzero += 1
                    rows.append({"helicities": label,
                                 "A": sp.simplify(a),
                                 "A_over_(1±c)/2": (sp.simplify(a / ((1 + c) / 2)) if sp.simplify(a) != 0 and
                                                    sp.simplify(sp.diff(a, c)) != 0 and
                                                    sp.simplify(a - (1 + c) / 2) == 0 else
                                                    (sp.simplify(a / ((1 - c) / 2)) if sp.simplify(a - (1 - c) / 2) == 0 else
                                                     (sp.simplify(a / (-(1 + c) / 2)) if sp.simplify(a + (1 + c) / 2) == 0 else
                                                      (sp.simplify(a / (-(1 - c) / 2)) if sp.simplify(a + (1 - c) / 2) == 0 else None))))})
    # 自旋平均
    total_sq = sp.simplify(sum(sp.simplify(r["A"] ** 2) for r in rows) / 4)
    over = sp.simplify(total_sq / (1 + c ** 2))
    # 刻画：非零是否恰好等价于"两个费米子对各自螺旋度反平行（|m|=1）"
    def aligned(h_a, h_b):
        return h_a == -h_b

    pattern_ok = True
    for h1 in helicities:
        for h2 in helicities:
            for h3 in helicities:
                for h4 in helicities:
                    a = sp.simplify(amplitude(h1, h2, h3, h4, transverse_only=True))
                    predicted = aligned(h1, h2) and aligned(h3, h4)
                    if (a != 0) != predicted:
                        pattern_ok = False

    # 对照：若缝允许 3 个态（含纵模/标量模）
    n_all = sum(1 for h1 in helicities for h2 in helicities for h3 in helicities
                for h4 in helicities
                if sp.simplify(amplitude(h1, h2, h3, h4, transverse_only=False)) != 0)
    return {
        "P2_nonzero_count_transverse_seam": nonzero,
        "P2_nonzero_count_three_state_seam": n_all,
        "P2_nonzero_iff_both_pairs_aligned": pattern_ok,
        "P2_characterisation": ("非零 <=> 每个费米子对各自处于 |m|=1 的组合（h1=-h2 且 h3=-h4）。"
                                "理由：pants 的 CG 在 h1=-h2 时给出 m=±1，在 h1=h2 时给出 m=0；"
                                "而缝只带横模 m=±1 ⇒ h1=h2 的那 12 组全部被剔除。"),
        "P2_verdict": ("缝只带横模（m=±1）时恰有 %d 个非零组合；若缝带全部三个态，"
                       "则会有 %d 个非零 —— 多出来的正是'标量光子'那一类，物理上不存在。"
                       "⇒ '16 剩 4' 是**标签 + 缝的态空间维数**的事，不是动力学。" % (nonzero, n_all)),
        "P3_rows": rows,
        "P3_sum_over_4_avg|A|^2": total_sq,
        "P3_ratio_to_(1+c^2)": over,
        "P3_verdict": ("四个非零振幅精确等于 ±(1+cos)/2 与 ±(1-cos)/2 —— "
                       "也就是 spin-1 的 Wigner d 函数 d^1_{±1,±1}，与书 661 页写的 "
                       "M_RL->RL ∝ ½(1+cos) 同归一化。自旋平均 (1/4)Σ|A|² = (1+cos^2)/4，"
                       "与 (6.2.22) 的 e^4(1+cos^2) 结构逐项一致，差一个常数因子 4（CG 约定）。"),
    }


# ======================================================================
# P4：这个权重依赖 sigma 吗？（与 V4 的 K5 对照）
# ======================================================================
def p4_no_sigma_dependence():
    a = amplitude(+1, -1, +1, -1)
    return {
        "A(↑↓->↑↓)": a,
        "free_symbols": sorted(str(x) for x in a.free_symbols),
        "verdict": ("上面四个振幅只含 cos(theta)（和 sin，但在非零解里都约掉了），"
                    "**不含 s = sigma**。这与 V4 的 K5（权重不是接口值的函数）互相印证："
                    "角度依赖来自缝上的转动，不来自接口值。"),
    }


def run():
    report = {"schema": "oq096-pants-interface-v5-labels-report",
              "status": "m2-minimal-attempt",
              "P1_selection_rules": p1_selection_rules(),
              "P2_P3_amplitudes": p2_p3_amplitudes(),
              "P4_sigma_independence": p4_no_sigma_dependence(),
              "conclusion": {
                  "what_M2_turns_out_to_be": (
                      "M2 不是'给端口贴一个表示标签'这一件事，而是**四件**："
                      "(i) 表示标签；(ii) 额外的选择定则（C 奇偶——SU(2) 允许 (1,1,1)，QED 不允许）；"
                      "(iii) 每个 pants 上的不变量张量（CG 系数）；"
                      "(iv) 缝上带一个**表示空间**（维数 2j+1，物理上只取横模 2 维）"
                      "与沿缝的**转动**（Wigner d^1(theta)）。"),
                  "what_this_buys": (
                      "有了 (i)-(iv)，角度依赖就能**从标签一侧算出来**：四个非零振幅精确等于 "
                      "±(1±cos)/2，自旋平均 ∝ (1+cos^2)。整个过程没有用到任何旋量、gamma 矩阵或传播子。"),
                  "what_this_costs_AEG": (
                      "AEG 的等值粘合（fiber product）在缝上只有**一个值、没有态空间、没有转动**，"
                      "等价于 d^1 = 恒等，只在 theta = 0 时成立。"
                      "所以 M1 与 M2 在这一点上合流：缝需要的是'态空间 + 平行的移动 + 缩并'，"
                      "而不是'一个相等的值'。"),
              },
              "limitations": [
                  "只到树级；不含传播子、不含 sigma、不含 s 依赖",
                  "缝的'横模优先'是物理输入（规范/无质量），不是从标签推出来的",
                  "C 奇偶那条只陈述了必要性，没有实现成一个可执行的标签定则",
                  "CG 与 d^1 用的是标准约定；换相位约定不改变 |A|^2，但这里没有逐一核对",
              ]}
    return report


def main():
    report = run()
    if "--check" in sys.argv:
        a = report["P1_selection_rules"]
        print("[P1] SW(2) 规则：QED 顶点 (1/2,1/2,1) ->", a["qed_vertex_(1/2,1/2,1)_allowed"],
              "| (1/2,1/2,1/2) ->", a["(1/2,1/2,1/2)_allowed"],
              "| (1,1,1) ->", a["(1,1,1)_allowed_by_SU2"], "（C 宇称才禁）")
        b = report["P2_P3_amplitudes"]
        print("[P2]", b["P2_nonzero_count_transverse_seam"], "个非零（横模缝） vs",
              b["P2_nonzero_count_three_state_seam"], "个（三态缝）")
        print("[P3] 自旋平均 / (1+cos^2) =", b["P3_ratio_to_(1+c^2)"])
        for r in b["P3_rows"]:
            if r["A"] != 0:
                print("     ", r["helicities"], "A =", r["A"])
        print("[P4] A 的自由符号：", report["P4_sigma_independence"]["free_symbols"])
    else:
        print(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True, default=str))


if __name__ == "__main__":
    main()
