#!/usr/bin/env python3
"""三孔表达式语言：孔 = 调用位置，词汇 = 相邻两台计算机的公共词汇。

结构：三台计算机（Rust / Python / Ada）是三角形的三个顶点；
三个相邻对 (Rust-Python)、(Python-Ada)、(Ada-Rust) 是三条边；
所谓“一个孔”就是一条边上的调用位置，能被填入的东西就是这一对语言的公共词汇。

于是三孔表达式 = 在三条边上各留一个待带入的位置：
    h_RP 的词汇 = V_Rust ∩ V_Python
    h_PA 的词汇 = V_Python ∩ V_Ada
    h_AR 的词汇 = V_Ada ∩ V_Rust

本程序算三件事：
  1. 三个孔的词汇、三重交集（有共同核心吗）；
  2. 填充自由度：各孔独立填 vs 三个填充必须互相兼容，各有多少种；
  3. 绕三角形一圈 R→P→A→R 的单值化：哪些词汇能走完一圈，哪些只能待在一条边上。

依赖：pip install matplotlib
运行：python three_hole_language.py
"""

import itertools
import math
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, Wedge

# 词汇分两层，写法上按“两边都能表达”来列。
# 数据层：三家都能如实表达（走 C ABI / 序列化）。
DATA = {"int", "float", "array", "record"}
# 控制/结构层：只有某些相邻对共有。
CONTROL = {
    "closure",     # Rust 闭包 ~ Python 闭包
    "exception",   # Python 异常 ~ Ada 异常
    "generic",     # Ada 泛型 ~ Rust 泛型
    "task",        # Ada 任务 ~ Rust 线程
    "protocol",    # Python 协议 ~ Rust trait（同为“结构化接口”）
}

V = {
    "Rust": DATA | {"closure", "generic", "protocol", "result", "ownership"},
    "Python": DATA | {"closure", "exception", "protocol", "dynamic"},
    "Ada": DATA | {"exception", "generic", "task"},
}

EDGES = [("Rust", "Python"), ("Python", "Ada"), ("Ada", "Rust")]
EDGE_LABEL = {("Rust", "Python"): "h_RP", ("Python", "Ada"): "h_PA", ("Ada", "Rust"): "h_AR"}


def main() -> None:
    vocab = {e: V[e[0]] & V[e[1]] for e in EDGES}
    triple = V["Rust"] & V["Python"] & V["Ada"]
    edge_only = {e: vocab[e] - triple for e in EDGES}

    print("三个孔的词汇（= 相邻两家的公共词汇）：")
    for e in EDGES:
        print(f"  {EDGE_LABEL[e]}  ({e[0]}–{e[1]}): {sorted(vocab[e])}")
    print(f"三重交集（三家都懂的核心词汇）: {sorted(triple)}")
    print()

    print("只能待在某一条边上的词汇（过了这条边就没人懂）：")
    for e in EDGES:
        print(f"  {EDGE_LABEL[e]}: {sorted(edge_only[e])}")
    print()

    # ---- 1. 三重交集为空的情形（Borromean）
    print("1. 控制/结构层的三重交集 =", sorted(triple & CONTROL),
          "→", "空" if not (triple & CONTROL) else "非空")
    print("   控制层在三家上的分布：")
    for name in ("Rust", "Python", "Ada"):
        print(f"     {name}: {sorted(V[name] & CONTROL)}")
    print("   逐对看：")
    for e in EDGES:
        print(f"     {EDGE_LABEL[e]}: {sorted(vocab[e] & CONTROL)}")
    print("   两两都有公共词汇，但三家没有共同词汇 —— 这就是 Borromean 形：")
    print("   任意一对可以自由交换，却没有任何一个词能同时出现在三条边上的同一个位置。")
    print()

    # ---- 2. 填充自由度
    sizes = {e: len(vocab[e]) for e in EDGES}
    indep = math.prod(sizes.values())
    coherent = len(triple) ** 3
    print("2. 填充自由度：")
    print(f"   各孔独立填（只要落在那条边的词汇里）: {sizes['Rust','Python']} × "
          f"{sizes['Python','Ada']} × {sizes['Ada','Rust']} = {indep} 种")
    print(f"   三个填充必须互相兼容（都取三重交集）: {len(triple)}³ = {coherent} 种")
    print(f"   差额 {indep - coherent} 种 = “更自由”的那部分，代价是每一次跨孔传递都要带适配器")
    print()

    # ---- 3. 绕一圈的单值化
    print("3. 绕三角形一圈 R→P→A→R，哪些词汇能走完：")
    ring = [("Rust", "Python"), ("Python", "Ada"), ("Ada", "Rust")]
    rows = []
    for w in sorted(V["Rust"] | V["Python"] | V["Ada"]):
        hops = [w in vocab[e] for e in ring]
        rows.append((w, hops, all(hops)))
    for w, hops, full in rows:
        mark = "".join("◎" if h else "×" for h in hops)
        print(f"     {w:<10} 三跳 {mark}   {'可绕一圈' if full else '走不完一圈'}")
    full_ok = [w for w, _h, f in rows if f]
    print(f"   能绕一圈的词汇: {sorted(full_ok)}（恰好就是三重交集）")
    print("   走不完一圈的词汇必须在每次换边时落回核心词汇，或者显式记下这次的“扭转”，")
    print("   否则实现里会出现“同一个孔两处填充拿到不同词汇”的不一致。")
    print()

    # ---------------- 图
    fig, axes = plt.subplots(1, 3, figsize=(19, 6.6), facecolor="white")
    for ax in axes:
        ax.set_facecolor("white")
        ax.set_aspect("equal")
        ax.set_xticks([])
        ax.set_yticks([])

    # (1) 三角形：顶点=计算机，边=孔
    ax = axes[0]
    pos = {"Rust": (0.0, 0.9), "Python": (-0.8, -0.6), "Ada": (0.8, -0.6)}
    for e in EDGES:
        (a, b) = e
        ax.plot([pos[a][0], pos[b][0]], [pos[a][1], pos[b][1]],
                color="#222222", linewidth=2.0)
        mx, my = (pos[a][0] + pos[b][0]) / 2, (pos[a][1] + pos[b][1]) / 2
        lab = EDGE_LABEL[e]
        ax.plot([mx], [my], marker="o", markersize=11, color="#d62728")
        ax.text(mx, my, "h", color="white", fontsize=9, ha="center", va="center")
        ax.text(mx * 1.22, my * 1.22, f"{lab}\n{len(vocab[e])} words",
                fontsize=9, ha="center", va="center", color="#333333")
    for name, (x, y) in pos.items():
        ax.plot([x], [y], marker="s", markersize=13, color="#1f77b4")
        ax.text(x, y, name, color="white", fontsize=9, ha="center", va="center")
    ax.set_xlim(-1.4, 1.4)
    ax.set_ylim(-1.3, 1.4)
    ax.set_title("(1) three computers = vertices, three holes = edges\n"
                 "each hole is a call site filled by that pair's shared vocabulary",
                 fontsize=10, color="#333333")

    # (2) 三个词汇的文氏图
    ax = axes[1]
    centers = {"Rust": (-0.30, 0.22), "Python": (0.30, 0.22), "Ada": (0.0, -0.34)}
    cols = {"Rust": "#d62728", "Python": "#1f77b4", "Ada": "#2ca02c"}
    for name, (cx, cy) in centers.items():
        ax.add_patch(Circle((cx, cy), 0.62, facecolor=cols[name], alpha=0.16,
                            edgecolor=cols[name], linewidth=1.4))
    ax.text(-0.62, 0.62, "Rust", color=cols["Rust"], fontsize=11)
    ax.text(0.42, 0.62, "Python", color=cols["Python"], fontsize=11)
    ax.text(-0.06, -1.02, "Ada", color=cols["Ada"], fontsize=11)
    ax.text(0.0, 0.02, "core\n" + "\n".join(sorted(triple)), fontsize=8,
            ha="center", va="center", color="#111111")
    ax.text(0.0, 0.62, "closure", fontsize=8, ha="center", color="#111111")
    ax.text(-0.62, -0.34, "generic\ntask", fontsize=8, ha="center", color="#111111")
    ax.text(0.62, -0.34, "exception", fontsize=8, ha="center", color="#111111")
    ax.set_xlim(-1.35, 1.35)
    ax.set_ylim(-1.2, 1.15)
    ax.set_title("(2) the three vocabularies\n"
                 "control vocabulary overlaps pairwise,\n"
                 "but the triple intersection is empty",
                 fontsize=10, color="#333333")

    # (3) 几何：三条射线分出三个区域，三条边界就是三个孔
    ax = axes[2]
    for i in range(3):
        a0 = 90 + 120 * i
        ax.add_patch(Wedge((0, 0), 1.0, a0, a0 + 120, facecolor=cols[["Rust", "Python", "Ada"][i]],
                           alpha=0.14, edgecolor="none"))
    for i in range(3):
        a = math.radians(90 + 120 * i)
        ax.plot([0, math.cos(a)], [0, math.sin(a)], color="#d62728", linewidth=2.2)
        ax.text(0.42 * math.cos(a) - 0.10 * math.sin(a),
                0.42 * math.sin(a) + 0.10 * math.cos(a), "h", color="#d62728",
                fontsize=10, ha="center", va="center")
    ax.add_patch(Circle((0, 0), 1.0, fill=False, edgecolor="#222222", linewidth=1.4))
    ax.plot([0], [0], marker="o", markersize=5, color="#ff7f0e")
    for i, name in enumerate(["Python", "Ada", "Rust"]):
        a = math.radians(90 + 120 * i + 60)
        ax.text(0.62 * math.cos(a), 0.62 * math.sin(a), name, fontsize=11,
                ha="center", va="center", color="#111111")
    ax.set_xlim(-1.25, 1.25)
    ax.set_ylim(-1.25, 1.25)
    ax.set_title("(3) the matching geometry: three regions meeting pairwise\n"
                 "three rays = three interfaces = the three holes;\n"
                 "this is the 3-line tangent cone we measured at a packing centre",
                 fontsize=10, color="#333333")

    fig.tight_layout()
    out = Path(__file__).with_name("three_hole_language.png")
    fig.savefig(out, dpi=150, facecolor="white")
    plt.close(fig)
    print(f"图已输出: {out}")


if __name__ == "__main__":
    main()
