#!/usr/bin/env python3
"""四个上半平面模型、四个 90° 扇区、以及“刚好三片叠压”的核验。

设定（沿用理想态）：单位圆盘，两条过圆心的正交测地线（45° 与 135° 直径）
把圆盘切成四个 90° 扇区 S1..S4。每个扇区有一个共形模型（映到半平面）。

“一片/一页”的取法：把每个扇区的模型沿它的两条测地线边做一次共形延拓
（Schwarz 反射），得到它覆盖的扇区集合：

    sheet_j := S_j ∪ (与 S_j 相邻的两个扇区) = 圆盘去掉正对面的那个扇区。

于是四片是：
    sheet1 = {S1,S2,S4}   sheet2 = {S1,S2,S3}
    sheet3 = {S2,S3,S4}   sheet4 = {S1,S3,S4}

本程序核验：
  1. 每个点的叠压片数（随机采样）——是不是刚好 3；
  2. 每个扇区缺的是哪一片（是不是正对面那一片）；
  3. 每条边界（两条测地线缝）上哪两片继续、哪两片被截断；
  4. 绕奇点 O 一周，片的标签如何置换（单值化障碍 = 多出来的那个自由度）。

依赖：pip install matplotlib
运行：python sector_sheets.py
"""

import math
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, Wedge

# 扇区：以角度区间给出（弧度），S1 是右侧扇区，逆时针编号
SECTORS = {
    1: (-math.pi / 4, math.pi / 4),
    2: (math.pi / 4, 3 * math.pi / 4),
    3: (3 * math.pi / 4, 5 * math.pi / 4),
    4: (5 * math.pi / 4, 7 * math.pi / 4),
}
# 一页 = 本扇区 + 两个相邻扇区 = 去掉正对面扇区
SHEETS = {j: tuple(sorted({j, (j % 4) + 1, ((j - 2) % 4) + 1})) for j in (1, 2, 3, 4)}
SEAM_ANGLES = [math.pi / 4, 3 * math.pi / 4, 5 * math.pi / 4, 7 * math.pi / 4]


def sector_of(angle: float) -> int:
    a = angle % (2 * math.pi)
    for j, (lo, hi) in SECTORS.items():
        lo2 = lo % (2 * math.pi)
        hi2 = hi % (2 * math.pi)
        if lo2 < hi2:
            if lo2 <= a < hi2:
                return j
        elif a >= lo2 or a < hi2:
            return j
    return 4


def main(samples: int = 400000, seed: int = 20240607) -> None:
    print("页的定义：sheet_j = 本扇区 + 两个相邻扇区（= 圆盘去掉正对面扇区）")
    for j in (1, 2, 3, 4):
        missing = ({1, 2, 3, 4} - set(SHEETS[j])).pop()
        print(f"  sheet{j} = {{S{SHEETS[j][0]}, S{SHEETS[j][1]}, S{SHEETS[j][2]}}}"
              f"   缺 S{missing}"
              f"   正对面 = S{(j + 1) % 4 + 1}")
    print()

    # ---- 1. 随机采样核验叠压片数
    rng = np.random.default_rng(seed)
    r = np.sqrt(rng.random(samples))
    th = rng.random(samples) * 2 * math.pi
    pts = np.stack([r * np.cos(th), r * np.sin(th)], axis=1)
    idx = np.array([sector_of(t) for t in th])
    cover = np.zeros(samples, dtype=int)
    for j, mem in SHEETS.items():
        cover += np.isin(idx, mem).astype(int)
    vals, counts = np.unique(cover, return_counts=True)
    print(f"1. 在圆盘内随机采样 {samples} 点，叠压片数分布："
          + ", ".join(f"{v} 片: {c} ({100 * c / samples:.4f}%)" for v, c in zip(vals, counts)))
    print()
    print("2. 每个扇区里在场/缺席的页：")
    for j in (1, 2, 3, 4):
        present = sorted(k for k, mem in SHEETS.items() if j in mem)
        absent = sorted(set(SHEETS) - set(present))
        print(f"  S{j}: 在场 {present}（3 片），缺席 {absent} —— 缺席的正是以正对面扇区为基的那一片")
    print()

    # ---- 3. 缝上的情形
    print("3. 每条缝（两条测地线共 4 条射线）上：两侧各有 3 片，其中 2 片继续、2 片被截断")
    for a in SEAM_ANGLES:
        left = sector_of(a - 1e-6)
        right = sector_of(a + 1e-6)
        same = sorted(set(SHEETS[left]) & set(SHEETS[right]))
        only_l = sorted(set(SHEETS[left]) - set(SHEETS[right]))
        only_r = sorted(set(SHEETS[right]) - set(SHEETS[left]))
        print(f"  {math.degrees(a):6.1f}° 缝: S{left} | S{right}   "
              f"两侧: {sorted(SHEETS[left])} | {sorted(SHEETS[right])}   "
              f"继续 {same}，S{left} 侧止于 {only_l}，S{right} 侧始自 {only_r}")
    print()

    # ---- 4. 绕 O 一周的标签置换
    print("4. 绕奇点 O 一周（依次穿过 4 条缝），在场页集合的演变：")
    seq = [1, 2, 3, 4]
    for j in seq:
        print(f"  S{j}: 在场 {sorted(SHEETS[j])}")
    perm = {}
    for i, j in enumerate(seq):
        nxt = seq[(i + 1) % 4]
        lost = sorted(set(SHEETS[j]) - set(SHEETS[nxt]))
        gain = sorted(set(SHEETS[nxt]) - set(SHEETS[j]))
        if lost and gain:
            perm[lost[0]] = gain[0]
    order, cur, steps = 1, perm[1], 1
    while cur != 1 and steps < 10:
        cur = perm[cur]
        steps += 1
    print(f"  标签置换: " + " -> ".join(f"{k}->{v}" for k, v in sorted(perm.items()))
          + f"，阶 = {steps}（4-循环，故是 Z_4 扭转）")
    print("  对照：只有两个半平面、两条扇区时，两侧在场页集合相同，绕一周置换是恒等（Z_1），")
    print("        即“片”的标签是刚性的；三片叠压才让标签可以整体扭转一圈 —— 这就是多出来的那个自由度。")
    print()

    # ---------------- 图
    fig, axes = plt.subplots(1, 3, figsize=(19, 6.6), facecolor="white")
    for ax in axes:
        ax.set_facecolor("white")
        ax.set_aspect("equal")
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_xlim(-1.08, 1.08)
        ax.set_ylim(-1.08, 1.08)

    colors = {1: "#d62728", 2: "#1f77b4", 3: "#2ca02c", 4: "#9467bd"}

    # (1) 四片半透明叠压
    ax = axes[0]
    for j, mem in SHEETS.items():
        # 一页 = 若干个 90° 楔形，画成半透明色块
        for s in mem:
            lo, hi = SECTORS[s]
            ax.add_patch(Wedge((0, 0), 1.0, math.degrees(lo), math.degrees(hi),
                               facecolor=colors[j], edgecolor="none", alpha=0.22))
    for a in SEAM_ANGLES:
        ax.plot([-math.cos(a), math.cos(a)], [-math.sin(a), math.sin(a)],
                color="#222222", linewidth=1.2)
    ax.add_patch(Circle((0, 0), 1.0, fill=False, edgecolor="#222222", linewidth=1.2))
    ax.plot([0], [0], marker="o", markersize=5, color="#ff7f0e")
    for j, (lo, hi) in SECTORS.items():
        mid = (lo + hi) / 2
        ax.text(0.62 * math.cos(mid), 0.62 * math.sin(mid), f"S{j}",
                color="#111111", fontsize=12, ha="center", va="center")
    ax.set_title("(1) four model sheets overlaid\n"
                 "each point is covered by exactly three of them\n"
                 "(colours blend to a uniform tint)",
                 color="#333333", fontsize=10)

    # (2) 缺席页编号图 + 叠压片数
    ax = axes[1]
    n = 700
    xs = np.linspace(-1, 1, n)
    X, Y = np.meshgrid(xs, xs)
    RR = np.hypot(X, Y)
    TT = np.mod(np.arctan2(Y, X), 2 * math.pi)
    img = np.zeros_like(X)
    idx_grid = np.zeros_like(X, dtype=int)
    # 注意 S1 的角度区间跨 0，需要处理回绕
    idx_grid = np.zeros_like(X, dtype=int)
    for j, (lo, hi) in SECTORS.items():
        lo2, hi2 = lo % (2 * math.pi), hi % (2 * math.pi)
        if lo2 < hi2:
            m = (TT >= lo2) & (TT < hi2)
        else:
            m = (TT >= lo2) | (TT < hi2)
        idx_grid[m] = j
    missing = np.zeros_like(X)
    for j in (1, 2, 3, 4):
        missing[idx_grid == j] = ({1, 2, 3, 4} - set(SHEETS[j])).pop()
    rgb = np.ones((n, n, 3))
    for j in (1, 2, 3, 4):
        c = np.array(matplotlib.colors.to_rgb(colors[j]))
        m = (missing == j) & (RR <= 1.0)
        rgb[m] = 0.35 + 0.5 * c
    rgb[RR > 1.0] = 1.0
    ax.imshow(rgb, extent=[-1, 1, -1, 1], origin="lower")
    for a in SEAM_ANGLES:
        ax.plot([-math.cos(a), math.cos(a)], [-math.sin(a), math.sin(a)],
                color="#111111", linewidth=0.8)
    ax.add_patch(Circle((0, 0), 1.0, fill=False, edgecolor="#111111", linewidth=1.0))
    ax.set_title("(2) which sheet is missing\n"
                 "the missing one is always the sheet based on the opposite sector;\n"
                 "coverage count = 3 everywhere (measured)",
                 color="#333333", fontsize=10)

    # (3) 绕 O 的标签置换
    ax = axes[2]
    ax.add_patch(Circle((0, 0), 1.0, fill=False, edgecolor="#222222", linewidth=1.0))
    for a in SEAM_ANGLES:
        ax.plot([-math.cos(a), math.cos(a)], [-math.sin(a), math.sin(a)],
                color="#aaaaaa", linewidth=0.8, linestyle=(0, (4, 3)))
    for j, (lo, hi) in SECTORS.items():
        mid = (lo + hi) / 2
        ax.text(0.72 * math.cos(mid), 0.72 * math.sin(mid),
                "\n".join([f"S{j}", ",".join(f"{k}" for k in sorted(SHEETS[j]))]),
                color="#111111", fontsize=9, ha="center", va="center")
    for i in range(4):
        a0 = math.pi / 4 + i * math.pi / 2 + 0.30
        a1 = a0 + math.pi / 2 - 0.60
        th = np.linspace(a0, a1, 60)
        ax.plot(0.34 * np.cos(th), 0.34 * np.sin(th), color="#d62728", linewidth=1.2)
        ax.annotate("", xy=(0.34 * math.cos(a1), 0.34 * math.sin(a1)),
                    xytext=(0.34 * math.cos(a1 - 0.06), 0.34 * math.sin(a1 - 0.06)),
                    arrowprops=dict(arrowstyle="->", color="#d62728", linewidth=1.2))
    ax.plot([0], [0], marker="o", markersize=5, color="#ff7f0e")
    ax.text(0.0, -1.045, "one turn around O: labels shift by a 4-cycle (order 4)",
            color="#333333", fontsize=9, ha="center")
    ax.set_title("(3) the seam bookkeeping\n"
                 "2 sheets continue across each seam, 2 are cut;\n"
                 "after a full turn the sheet labels come back twisted",
                 color="#333333", fontsize=10)

    fig.tight_layout()
    out = Path(__file__).with_name("sector_sheets.png")
    fig.savefig(out, dpi=150, facecolor="white")
    plt.close(fig)
    print(f"图已输出: {out}")


if __name__ == "__main__":
    main()
