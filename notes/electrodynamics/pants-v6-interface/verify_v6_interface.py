#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""OQ-096 V6：把"缝的态空间 + 沿缝的转动"装进接口记录，并检验相容性。

V4 说缺的是"纤维上的测度"；V5 说那个测度的形状是"缝上的表示空间 + 沿缝的 Wigner 转动"。
V6 把这两句落成一个**扩展的接口记录**，然后问三个尖锐的问题：

  X1  退化：当态空间是一维、转动是恒等时，扩展是否**精确退回** AEG 现有表述？
      （若不是，说明这是破坏性扩张而不是相容扩张。）
  X2  极点：V4 的 K4 说"把 1/sigma 放进值层会让 sigma=0 处的谱塌掉"。
      态空间能否绕开？物理在极点处用的到底是什么？
  X3  配对：AEG 已有"缝两侧定向相反"。加上态空间后这个"相反"是什么？
      以及为什么只留下两个横模。

三个问题的答案（见 §5 与 README）：
  X1 能退回；X2 绕不开但可以**分层**——极点处物理用的是留数，留数住在态空间层且有限；
  X3 "定向相反"正好是配对 V ⊗ V* -> C 所需要的，但光子给的配对是**不定号**的 (2,1)，
     取正定部分 = 规范输入。
"""
import json
import sys

import sympy as sp

c, s = sp.symbols("c s", real=True)
sigma = sp.symbols("sigma")
phi = sp.symbols("phi", real=True)
sqrt2 = sp.sqrt(2)


# ======================================================================
# 扩展的接口记录
# ======================================================================
class SeamSpace:
    """缝上的表示空间：标签 j（用 2j 的整数 d）、配对、转动。

    pairing 用矩阵给出；转动用 spin-j 的 Wigner d 矩阵（这里只需要 j=0 与 j=1）。
    """

    def __init__(self, d, name=""):
        if d < 0:
            raise ValueError("seam:negative-label")
        self.d = d
        self.j = sp.Rational(d, 2)
        self.dim = d + 1
        self.name = name

    def trivial(self):
        return self.d == 0

    def pairing_signature(self, kind):
        if kind == "definite":                       # 正定内积（数学上的 Hilbert 空间）
            return [1] * self.dim
        if kind == "photon":                         # 光子：两个横模 +1，标量模 -1
            if self.d != 2:
                raise ValueError("photon-pairing:needs-j=1")
            return [1, 1, -1]
        raise ValueError("pairing:unknown-kind")

    def transport(self, kind="identity"):
        """沿缝的平行移动：j=0 只有相位；j=1 是 spin-1 的 d 矩阵。"""
        if self.d == 0:
            return sp.Matrix([[sp.Integer(1) if kind == "identity" else sp.exp(sp.I * phi)]])
        if self.d == 2:
            D = sp.Matrix([
                [(1 + c) / 2, -s / sqrt2, (1 - c) / 2],
                [s / sqrt2, c, -s / sqrt2],
                [(1 - c) / 2, s / sqrt2, (1 + c) / 2],
            ])
            return sp.eye(3) if kind == "identity" else D
        raise ValueError("transport:only-j=0-and-1-implemented")

    def describe(self):
        return {"d=2j": self.d, "j": str(self.j), "dim": self.dim}


# ======================================================================
# X1：退化 —— 一维态空间 + 恒等转动 ⇒ 回到值层读数
# ======================================================================
def x1_degeneration():
    trivial = SeamSpace(0, "trivial")
    T = sp.Symbol("T")                      # 值层读数（一个数）
    w_id = (trivial.transport("identity") * sp.Matrix([[T]]))[0, 0]
    w_phase = sp.simplify((trivial.transport("phase") * sp.Matrix([[T]]))[0, 0])
    modulus = sp.simplify(sp.Abs(w_phase.subs(T, 1)))
    # 有标签时：读数不再是"一个数"，而是"一个数 + 一个离散标签"，且权重是迹
    photon = SeamSpace(2, "photon")
    return {
        "X1_trivial_seam_identity_transport": {
            "weight": str(w_id),
            "reduces_to_value_layer": sp.simplify(w_id - T) == 0},
        "X1_trivial_seam_phase_transport": {
            "weight": str(w_phase),
            "modulus_with_T=1": str(modulus),
            "reading": ("一维态空间 + 相位转动时，权重 = e^{i phi} T：**一个相位乘一个数**。"
                        "这正是 11 天前那份电动力学稿 Remark 2.9 的说法"
                        "（同终点不同 Reeb 高度 ⇒ 差一个相位；以 e^{iA} 为权求和作为路径积分的候选）。"
                        "于是 AEG 的缝圆 holonomy（Prop 10.7 的一个标量）与那个相位是同一个东西，"
                        "扩展只是把相位换成矩阵。")},
        "X1_labelled_seam_changes_the_reading": {
            "photon_seam": photon.describe(),
            "reading": ("j=0 时接口读数是'一个数'；j=1 时读数变成'一个数 + 离散标签 + 一个 3x3 转动'。"
                        "所以扩展加入的连续数据只有转动，标签是**离散**的。")},
    }


# ======================================================================
# X2：极点处的留数 —— 物理用的是留数，它住在态空间层且有限
# ======================================================================
# CG：<1 m | 1/2 h1 ; 1/2 h2>，h = ±1（倍乘 2）
CG = {
    (+1, +1): {+1: sp.Integer(1)},
    (+1, -1): {0: 1 / sqrt2},
    (-1, +1): {0: 1 / sqrt2},
    (-1, -1): {-1: sp.Integer(1)},
}
M_INDEX = {+1: 0, 0: 1, -1: 2}


def spin_factor(h1, h2, h3, h4, transverse_only=True):
    """态空间上的缩并（V5 的结果）：A = sum CG_e d^1 CG_mu。"""
    e_side = CG[(h1, -h2)]
    mu_side = CG[(h3, -h4)]
    D = SeamSpace(2).transport("rotation")
    modes = (+1, -1) if transverse_only else (+1, 0, -1)
    total = sp.Integer(0)
    for m in modes:
        for mp in modes:
            ce, cm = e_side.get(m, 0), mu_side.get(mp, 0)
            if ce and cm:
                total += ce * D[M_INDEX[m], M_INDEX[mp]] * cm
    return sp.simplify(total)


def x2_pole():
    # 传播子给出 1/sigma；态空间给一个有限的转动因子
    F = spin_factor(+1, -1, +1, -1)                    # = (1+c)/2
    A = F / sigma                                       # 完整振幅形状（略去常数）
    residue = sp.simplify(sp.limit(sigma * A, sigma, 0))
    # 关键判断：留数是否有限、是否与 sigma 无关、是否等于态空间缩并
    finite = residue.is_finite is not False and sigma not in residue.free_symbols
    return {
        "X2_amplitude_shape": "A(sigma,theta) = (1/sigma) * F(theta)，F 来自态空间缩并",
        "X2_F": str(F),
        "X2_residue_sigma_times_A": str(residue),
        "X2_residue_is_finite_and_sigma_free": bool(finite),
        "X2_residue_equals_state_space_contraction": sp.simplify(residue - F) == 0,
        "reading": ("V4 的 K4：把 1/sigma 放进**值层**（局部化）会让 sigma=0 处的谱塌成零环。"
                    "但物理在极点处用的不是'接口的值'，而是**留数**；留数 = 态空间上的缩并，"
                    "它在 sigma=0 处完全有限，且不依赖 sigma。"
                    "⇒ K4 的障碍没有被绕开，而是被**分层**："
                    "值层负责 1/sigma（并在极点上失效），态空间层负责留数（在极点上良好）。"
                    "两条读法不是竞争关系，而是分别管不同的东西。"),
        "caveat": ("这不是'解决了极点'。留数有限是微扰论里把极点因子提出去的结果；"
                   "AEG 若要在 sigma=0 处**直接用字符读数**，K4 依然成立。"),
    }


# ======================================================================
# X3：配对 —— "定向相反"是什么，以及为什么只剩两个横模
# ======================================================================
def x3_pairing():
    photon = SeamSpace(2)
    sig = photon.pairing_signature("photon")
    n_pos = sum(1 for v in sig if v > 0)
    n_neg = sum(1 for v in sig if v < 0)
    det = sp.Integer(1)
    for v in sig:
        det *= v
    trivial_pairing = photon.pairing_signature("definite")
    n_all = sum(1 for h1 in (+1, -1) for h2 in (+1, -1) for h3 in (+1, -1) for h4 in (+1, -1)
                if spin_factor(h1, h2, h3, h4, transverse_only=False) != 0)
    n_pos_only = sum(1 for h1 in (+1, -1) for h2 in (+1, -1) for h3 in (+1, -1) for h4 in (+1, -1)
                     if spin_factor(h1, h2, h3, h4, transverse_only=True) != 0)
    return {
        "X3_pairing_signature_photon": sig,
        "X3_positive_count": n_pos, "X3_negative_count": n_neg,
        "X3_nondegenerate": det != 0,
        "X3_all_three_modes_nonzero_amplitudes": n_all,
        "X3_positive_part_only_nonzero_amplitudes": n_pos_only,
        "reading": ("AEG 已经有'缝两侧定向相反'（V1/V2 的 seam:opposite-orientations）。"
                    "加上态空间后，那个'相反'正好是配对 V ⊗ V* -> C 所需要的东西 —— "
                    "所以扩展不是新加一条要求，而是给已有的一条要求**赋予内容**。"
                    "但光子给的配对不是正定的：号差 (2,1)，行列式 -1。"
                    "取正定部分（两个横模）才得到 4/16；三个模全要则 16/16 全非零。"
                    "⇒ '横模优先' = 取配对的正定部分，这是**规范输入**，不是从配对推出来的。"),
        "signature_note": ("正定内积（%s）无法承载光子的不定号配对；"
                           "所以扩展必须允许**非正定**的配对，并显式声明取哪一部分。"
                           % trivial_pairing),
    }


# ======================================================================
# X4：与 AEG 现有定理的相容性清单（含一处真实张力）
# ======================================================================
def x4_compatibility():
    photon = SeamSpace(2)
    dim = photon.dim
    return {
        "unchanged_by_the_extension": [
            "孔–盘互补（Thm 10.4）：标签与转动不进入同调，[C_e] != 0 与 i_*[C_e] = 0 原样成立",
            "局部 pants 与亏格（Prop 10.2）：只依赖端口数与图，V3 已把这些量算成纯组合量",
            "pants 沿接口圆盘拼接（Prop 10.3）：曲面结论不变；变的是接口上放什么",
        ],
        "must_be_rewritten": [
            "缝圆 holonomy（Prop 10.7）：标量 ∮β 应升级为态空间上的算子；"
            "一维情形退化为一个 U(1) 相位（X1 已核）",
            "接口谱（Prop 10.9）：j=0 时字符读数 χ_c 原样；j!=0 时'值'要换成"
            "'标量值 + 离散标签 + 转动'三元组",
            "接口记录（Def 10.11）：I_e = (D_e,C_e;σ_e,r_e,β_e) 需增加 (V_e,U_e,配对) 三个字段",
        ],
        "real_tension": {
            "capping": "常值边界封盖阻碍（Thm 10.12 / Cor 10.13）说：正则圆盘不能有常值边界。"
                       "而态空间的读法给出：封盖一条缝应贡献 dim V_e = %d（取迹），是个非零常数。"
                       "两者一个说'不可能'、一个说'等于一个数'。"
                       "**这个张力我没有解决**：也许'常值边界'与'取迹'不是同一件事，"
                       "也许封盖在态空间层要做的是投影而不是求迹。列为开放问题。" % dim,
            "proposed_resolution_my_reading": (
                "张力可能是假的，而且理由与 X2 是同一个分层。"
                "把'封盖'读成态空间上的收缩：收缩一条缝 = 用真空 <0| 去缩它的边界态，"
                "而这要求标签平凡（j=0）。于是："
                "（代数层）j=0 的缝**可以**被封盖，贡献 dim V_e；"
                "（解析层）把它实现成**正则 AES 圆盘**（带度规 a 与 |da|^2 = mu^2 + lambda^2 a^2）"
                "则被 Thm 10.12 挡住。"
                "也就是说 Thm 10.12 大概是关于**解析厚化**（Remark 10.8，AEG 自己写着"
                "'a declared structure not yet constructed in general'）的阻碍，"
                "而不是关于拓扑/代数接口的阻碍。若这个读法成立，Cor 10.13 应读作"
                "'**解析**封盖不可能'。"),
            "falsifier": ("若把解析数据全部去掉、只留拓扑 + 代数接口，封盖仍然不可能，"
                          "则这个读法错，Thm 10.12 确实管拓扑层。"),
            "what_would_settle_it": ("在态空间层写出封盖的显式构造，并把它与 Thm 10.12 的"
                                     "解析数据对照，看阻碍到底出现在哪一步。"),
        },
    }


def run():
    report = {"schema": "oq096-pants-interface-v6-extension-report",
              "status": "interface-record-extended",
              "X1_degeneration": x1_degeneration(),
              "X2_pole_residue": x2_pole(),
              "X3_pairing": x3_pairing(),
              "X4_compatibility": x4_compatibility(),
              "conclusion": {
                  "the_extension": ("接口记录由 (D_e, C_e; σ_e, r_e, β_e) 扩为"
                                    " (D_e, C_e; σ_e, r_e, β_e; V_e, ⟨·,·⟩_e, U_e)："
                                    "缝上一个有限维表示空间、一个（可不定号的）非退化配对、"
                                    "一个沿缝的平行移动。"),
                  "what_it_buys": ("(1) 退化良：一维 + 恒等时精确退回 AEG 的标量读数；"
                                   "(2) 极点分层：1/σ 归值层（在 σ=0 失效），留数归态空间层（有限）；"
                                   "(3) 已有条款获得内容：'缝两侧定向相反' = 配对 V⊗V*→C；"
                                   "(4) 角度依赖有出处：V5 已算出它 = CG·d^1·CG。"),
                  "what_stays_open": ("封盖与 dim V_e 的张力（X4）没有解决；"
                                      "C 奇偶仍不在标签层里；横模优先仍是规范输入。"),
              },
              "limitations": [
                  "只实现 j=0 与 j=1 的转动；更高自旋未写",
                  "留数那条是微扰论的分层，不是对 AEG 值层的修补",
                  "没有把扩展做成 AEG 仓库里的补丁；没有跑 AEG 的定理检查器",
                  "封盖张力只提出，未解决",
              ]}
    return report


def main():
    report = run()
    if "--check" in sys.argv:
        a = report["X1_degeneration"]
        print("[X1] 一维+恒等 -> 退回值层:", a["X1_trivial_seam_identity_transport"]["reduces_to_value_layer"])
        print("     一维+相位 -> 权重 =", a["X1_trivial_seam_phase_transport"]["weight"],
              "| 模 =", a["X1_trivial_seam_phase_transport"]["modulus_with_T=1"])
        b = report["X2_pole_residue"]
        print("[X2] 振幅形状:", b["X2_amplitude_shape"])
        print("     留数 =", b["X2_residue_sigma_times_A"], "| 有限且无 σ:", b["X2_residue_is_finite_and_sigma_free"],
              "| 等于态空间缩并:", b["X2_residue_equals_state_space_contraction"])
        d = report["X3_pairing"]
        print("[X3] 光子配对号差:", d["X3_pairing_signature_photon"], "非退化:", d["X3_nondegenerate"])
        print("     三模非零数:", d["X3_all_three_modes_nonzero_amplitudes"],
              "| 只取正定部分:", d["X3_positive_part_only_nonzero_amplitudes"])
        print("[X4] 张力:", report["X4_compatibility"]["real_tension"]["capping"][:80], "...")
    else:
        print(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True, default=str))


if __name__ == "__main__":
    main()
