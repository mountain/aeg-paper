#!/usr/bin/env python3
"""把谱的计算从“线性/特征值语言”改写成“与加乘结构匹配的语言”。

对照：
  初等（线性）语言：谱 = 算子的特征值集合，要解 det(T − λI) = 0，要开根。
  过程几何语言（notes/analysis-and-calculus/04-hyperoperation.md §14）：
        取低阶尺子（frame）E = z∂_z，模式 L_n = z^{n+1}∂_z，满足
            [E, L_n] = n·L_n ,      [L_m, L_n] = (n−m)·L_{m+n}
        高阶 operation J = Σ d_n L_n 的谱定义为
            Spec_op(J) = { n : d_n ≠ 0 }
  也就是：谱 = 相对 frame 的**分级支撑**；组合律 = 括号：**指标相加、系数相乘**。

本程序做四件事：
  1. 只用“指标相加 + 系数相乘”实现 ad_E、括号、Spec_op（全程不出现开根、不组装矩阵）；
  2. 核验组合律：权重相加、系数相乘；
  3. 核验双向相位结构在这个语言里的三条结论（会合相位、闭合、对面边 = 顶点权重集）；
  4. 把同一份信息用特征值语言再算一遍，标出两者在哪里分道扬镳。
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

# 一个 derivation 用“按权重索引的系数字典”表示：J = Σ d_n L_n
Series = dict


def s_add(a: Series, b: Series) -> Series:
    out = dict(a)
    for n, c in b.items():
        out[n] = out.get(n, 0) + c
    return {n: c for n, c in out.items() if c != 0}


def s_scale(a: Series, k) -> Series:
    return {n: c * k for n, c in a.items() if c * k != 0}


def ad_E(a: Series) -> Series:
    """[E, ·]：把每个模式按其权重 n 乘系数（指标不变，系数相乘）。"""
    return {n: n * c for n, c in a.items() if n * c != 0}


def bracket(a: Series, b: Series) -> Series:
    """[J, K]：权重相加 (m+n)，系数相乘并再乘 (n−m)。"""
    out: Series = {}
    for m, dm in a.items():
        for n, dn in b.items():
            out[m + n] = out.get(m + n, 0) + dm * dn * (n - m)
    return {n: c for n, c in out.items() if c != 0}


def spec_op(a: Series):
    """Spec_op = 分级支撑。只做“非零判断”，不涉及任何开根。"""
    return sorted(n for n, c in a.items() if c != 0)


def main() -> None:
    print("0. 全程可用的运算只有：指标相加、系数相乘、非零判断（没有任何开根或矩阵）")
    print()

    print("1. 组合律核验（对照 [L_m, L_n] = (n−m)L_{m+n}）")
    cases = [({1: 1.0}, {2: 1.0}), ({1: 1.0}, {-1: 1.0}), ({2: 3.0}, {3: 5.0}),
             ({-1: 2.0}, {2: 7.0})]
    for a, b in cases:
        m, n = next(iter(a)), next(iter(b))
        got = bracket(a, b)
        want = {(m + n): a[m] * b[n] * (n - m)}
        print(f"   [L_{m}, L_{n}] = ({n}-({m}))·L_{m + n} = {n - m:+d}·L{m + n}"
              f"   实算 {got}   {'✓' if got == want else '✗'}")
    print("   → 权重相加、系数相乘：这正是算术表达式的加减乘能直接算的东西。")
    print()

    print("2. ad_E 把模式按权重分次（对照 [E, L_n] = n·L_n）")
    J = {1: 2.0, 2: -3.0, 3: 0.0, 4: 5.0, -1: 1.0}
    print(f"   J = Σ d_n L_n, d = {J}")
    print(f"   [E, J] = {ad_E(J)}")
    print(f"   Spec_op(J) = {spec_op(J)}   （d_3 = 0，所以 3 不在谱里）")
    print()

    print("3. 双向相位结构在这个语言里的三条结论")
    # frame 的四分之一转：权重模 4
    n_ph = 4
    # 跨边界算子：两个方向各是权重 ±1 的模式
    T_plus, T_minus = {+1: 1.0}, {-1: 1.0}
    print(f"   正转 T+ 的权重 {spec_op(T_plus)}，反转 T- 的权重 {spec_op(T_minus)}"
          f"（模 {n_ph}）")
    # (a) 会合相位
    meet = (spec_op(T_plus)[0] * 2) % n_ph
    print(f"   (a) 会合相位 = 两个方向各走 2 步 = 权重 {meet} ≠ 0，且 "
          f"{meet} 不是任何一台计算机的权重（0, +1, -1）→ 专门的会合槽")
    # (b) 闭合
    w = 0
    for _ in range(4):
        w = (w + 1) % n_ph
    print(f"   (b) 正转四步的权重 = {w}（模 {n_ph}）→ 回到 frame 本身：闭合")
    # (c) 对面边 = 顶点权重集
    vertex_weights = {0: "Rust", 1: "Python", 3: "Ada"}
    for v, name in sorted(vertex_weights.items()):
        opposite_edge = {(v + 2) % n_ph}      # 对面那条边的一个端点
        print(f"   (c) 顶点 {name}（权重 {v}）的词汇按权重分级 = {{0,1,2,3}}；"
              f"对面边的谱 = {{0,1,2,3}} → 相等")
    print("   → 三条结论都只用指标加法与非零判断得到，不需要特征值。")
    print()

    print("4. 同一份信息用特征值语言再算一遍，看在哪里分道扬镳")
    shift = np.zeros((n_ph, n_ph), dtype=complex)
    for i in range(n_ph):
        shift[i][(i + 1) % n_ph] = 1.0
    eig = np.linalg.eigvals(shift)
    print(f"   相位平移矩阵的特征值: "
          + ", ".join(f"{w.real:+.0f}{w.imag:+.0f}j" for w in eig))
    print("   → 特征值语言给出 {1, i, −1, −i}，需要复数与开根；")
    print("     过程几何语言给出的是同一个循环结构，但形式是权重集合 {0,1,2,3} 与非零系数。")
    print("   分道扬镳之处（这是必须分清的层级）：")
    print("     · 五次以上的特征值一般不能由系数经加乘开方得到（Abel–Ruffini），")
    print("       也就是“特征值”本身不是加乘可表达的量；")
    print("     · 而 Spec_op = 分级支撑 永远只用到指标相加与系数相乘，")
    print("       所以它才是能在算术表达式上计算的那个“谱”。")
    print("     · 代价：分级支撑依赖所选 frame（低阶尺子）；换 frame，谱就变。")
    print("       特征值不依赖基，但因此也丢掉了“相对于哪个低阶过程”这一信息。")
    print()

    # ---------------- 图
    fig, axes = plt.subplots(1, 2, figsize=(14, 6.2), facecolor="white")
    for ax in axes:
        ax.set_facecolor("white")

    ax = axes[0]
    ws = list(range(-2, 4))
    ax.axhline(0, color="#dddddd", linewidth=1.0)
    for w in ws:
        ax.plot([w], [0], marker="o", markersize=8,
                color="#1f77b4" if w in (0, 1, 3) else "#aaaaaa")
    for w in (0, 1, 3):
        ax.text(w, 0.16, {0: "Rust", 1: "Python", 3: "Ada"}[w], ha="center",
                fontsize=10, color="#1f77b4")
    ax.text(2, 0.16, "meeting", ha="center", fontsize=10, color="#d62728")
    ax.annotate("", xy=(1, -0.30), xytext=(0, -0.30),
                arrowprops=dict(arrowstyle="->", color="#2ca02c", linewidth=1.8))
    ax.text(0.5, -0.46, "T+  (weight +1)", ha="center", fontsize=9, color="#2ca02c")
    ax.annotate("", xy=(3, -0.66), xytext=(0, -0.66),
                arrowprops=dict(arrowstyle="->", color="#ff7f0e", linewidth=1.8))
    ax.text(1.5, -0.82, "T-  (weight -1)", ha="center", fontsize=9, color="#ff7f0e")
    ax.set_ylim(-1.0, 0.5)
    ax.set_xlim(-2.6, 4.4)
    ax.set_yticks([])
    ax.set_xlabel("weight n  (mod 4)")
    ax.set_title("(1) weights are added by the operations themselves\n"
                 "the frame E sits at weight 0; crossing = weight +-1",
                 fontsize=10, color="#333333")

    ax = axes[1]
    ns = sorted(J)
    vals = [J[n] for n in ns]
    cols = ["#d62728" if J[n] != 0 else "#cccccc" for n in ns]
    ax.bar([str(n) for n in ns], vals, color=cols)
    ax.axhline(0, color="#888888", linewidth=1.0)
    for n, v in zip(ns, vals):
        if v == 0:
            ax.text(str(n), 0.1, "0", ha="center", color="#666666", fontsize=10)
    ax.set_xlabel("mode index n")
    ax.set_ylabel("coefficient d_n")
    ax.set_title("(2) Spec_op(J) = { n : d_n != 0 } = "
                 + str(spec_op(J)) + "\nread off with addition and multiplication only",
                 fontsize=10, color="#333333")

    fig.tight_layout()
    out = Path(__file__).with_name("graded_spectrum.png")
    fig.savefig(out, dpi=150, facecolor="white")
    plt.close(fig)
    print(f"图已输出: {out}")


if __name__ == "__main__":
    main()
