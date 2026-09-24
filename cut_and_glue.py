#!/usr/bin/env python3
"""把 S1,S2,S3,S4 沿坐标轴切开、再重新粘合：这个操作的完整不变量计算。

切法：四个 90° 扇区 S1..S4 由两条对角缝（±45°）分开；坐标轴（0°/90°/180°/270°）
各落在其中一个扇区内部，所以沿坐标轴切 = 把每个扇区劈成两个 45° 的三角形片。
一共 8 片 P0..P7，每片三个顶点：圆心 O、两个单位圆上的端点；三条边：
左半径 L、外弧 A、右半径 R。

重新粘合：把 8 条半径边 L 与 8 条半径边 R 配对，即给出一个置换 σ ∈ S_8：
    L_p  ── 粘 ──  R_{σ(p)}        端点上配对 O_p ≡ O_{σ(p)}，U_p ≡ W_{σ(p)}

于是本程序算出（都可以手算核对的量）：
  * 圆心顶点轨道数 = σ 的循环个数；
  * 外弧连成的边界分量数 b = σ 的循环个数；
  * χ = V − E + F = b；
  * 连通分量数 = σ 的循环个数；
  * 每个结果的曲面类型；
并穷举全部 8! = 40320 种 σ，给出分布。
最后算出“要得到三孔，还差什么”。
"""

import itertools
import math
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Wedge

N = 8  # 片数


def cycles(perm):
    """置换的循环分解。"""
    seen = [False] * len(perm)
    out = []
    for i in range(len(perm)):
        if seen[i]:
            continue
        cyc, j = [], i
        while not seen[j]:
            seen[j] = True
            cyc.append(j)
            j = perm[j]
        out.append(cyc)
    return out


def invariants(sigma):
    """给定粘合置换 σ，算出这个粘合结果的各不变量。"""
    cyc = cycles(sigma)
    c_center = len(cyc)          # 圆心顶点轨道数
    b = len(cyc)                 # 边界分量数（外弧被 σ 串起来）
    F = N                        # 8 个三角形面
    E = 2 * N                    # 8 条外弧 + 8 条粘好的半径边
    V = c_center + N             # 圆心轨道 + 外顶点轨道（16 个外顶点两两配对成 8 个）
    chi = V - E + F
    return dict(cycles=cyc, chi=chi, boundary=b, components=len(cyc),
                orientable=True, V=V, E=E, F=F)


def surface_name(info):
    chi, b, comp = info["chi"], info["boundary"], info["components"]
    if comp > 1:
        return f"{comp} 个互不相连的圆盘"
    if chi == 1 and b == 1:
        return "圆盘"
    return f"χ={chi}, b={b}"


def main() -> None:
    print("切完的片段：8 个 45° 三角形，每片三顶点 (O, U_p, W_p)，三边 L_p / A_p / R_p")
    print("重新粘合的参数：置换 σ ∈ S_8，把 L_p 粘到 R_{σ(p)}")
    print()

    ident = tuple(range(N))
    info = invariants(ident)
    print(f"恒等粘合 σ = id：循环 {[c for c in info['cycles']]}，"
          f"χ = {info['chi']}，边界分量 {info['boundary']}，曲面 = {surface_name(info)}")
    cyc8 = tuple((i + 1) % N for i in range(N))
    info8 = invariants(cyc8)
    print(f"整体轮转 σ = (0 1 2 ... 7)：循环 {info8['cycles']}，"
          f"χ = {info8['chi']}，边界分量 {info8['boundary']}，曲面 = {surface_name(info8)}")
    print()

    # ---- 穷举全部 8! 个粘合
    dist = {}
    for sigma in itertools.permutations(range(N)):
        inf = invariants(sigma)
        key = (inf["components"], inf["chi"], inf["boundary"])
        dist[key] = dist.get(key, 0) + 1
    print(f"穷举全部 {math.factorial(N)} = {math.factorial(N)} 种 σ：")
    print(f"  {'连通分量':>8} {'χ':>4} {'边界分量':>8} {'种数':>8}   曲面")
    for (comp, chi, b), cnt in sorted(dist.items()):
        name = "圆盘" if (comp == 1 and chi == 1) else f"{comp} 个圆盘"
        print(f"  {comp:>8} {chi:>4} {b:>8} {cnt:>8}   {name}")
    print("  → 只有两种结果：单个圆盘（σ 是 8-循环，共 8!/8 = 5040 种），")
    print("    或若干互不相连的圆盘（σ 的每个循环给一个）。没有任何 3 孔曲面。")
    print()

    # ---- 为什么必然如此
    print("为什么必然如此：")
    print("  粘合不改变 χ（两条边并成一条、两个顶点并成一个，χ 不变）。")
    print("  圆心顶点轨道数 = σ 的循环数 C；外顶点两两配对后恒为 8 个轨道，")
    print("  于是 V = C + 8, E = 16, F = 8，χ = V − E + F = C。")
    print("  边界分量数同样等于 C（外弧被 σ 串成 C 条环）。")
    print("  若曲面连通且可定向，则 χ = 2 − 2g − b；代入 χ = b = C 得 g = 1 − C：")
    print("    C = 1 → g = 0, b = 1：圆盘；")
    print("    C ≥ 2 → g < 0，不可能，故这些情形必然不连通（每个循环一个圆盘）。")
    print("  结论：这个操作**只能产出圆盘**，它的全部信息在置换 σ 里，不在拓扑里；")
    print("        三孔曲面（χ = −1, b = 3）在这个族里根本不可达。")
    print()

    # ---- σ 里的“三”
    sigma3 = (1, 2, 0, 4, 5, 3, 7, 6)   # (0 1 2)(3 4 5)(6 7)
    inf3 = invariants(sigma3)
    print("σ 里确实可以放进一个 3：例如 σ = (0 1 2)(3 4 5)(6 7)，")
    print(f"  循环 {inf3['cycles']}，χ = b = {inf3['chi']}，结果仍是 {inf3['components']} 个圆盘。")
    print("  这个 3 体现在绕 O 一周的**单值化/标签循环**上（三片一循环），而不是孔数上。")
    print()

    # ---- 要拿到三孔还差什么
    print("要拿到三孔还差什么：从 χ 出发算。")
    print(f"  {'操作':<34}{'χ':>5}{'边界分量 b':>12}")
    rows = [("切完再粘回（圆盘）", 1, 1),
            ("挖掉圆心 O 一个点", 0, 2),
            ("再挖掉一个点", -1, 3),
            ("再挖第三个点", -2, 4)]
    for name, chi, b in rows:
        print(f"  {name:<34}{chi:>5}{b:>12}")
    print("  三孔（χ = −1, b = 3）恰好等于：圆盘 + 2 个挖点。")
    print("  其中一个挖点自然就是奇点 O —— 在这个图像里，奇点正好成为三个孔之一。")
    print()

    # ---------------- 图
    fig, axes = plt.subplots(1, 3, figsize=(19, 6.4), facecolor="white")
    for ax in axes:
        ax.set_facecolor("white")
        ax.set_aspect("equal")
        ax.set_xticks([])
        ax.set_yticks([])

    # (1) 切开：8 片
    ax = axes[0]
    colors = plt.get_cmap("tab10")
    for p in range(N):
        lo, hi = 45 * p, 45 * (p + 1)
        ax.add_patch(Wedge((0, 0), 1.0, lo + 1.2, hi - 1.2,
                           facecolor=colors(p % 10), edgecolor="white",
                           linewidth=0.8, alpha=0.55))
        mid = math.radians((lo + hi) / 2)
        ax.text(0.72 * math.cos(mid), 0.72 * math.sin(mid), f"P{p}",
                fontsize=10, ha="center", va="center", color="#111111")
    for a in (0, 90, 180, 270):
        r = math.radians(a)
        ax.plot([0, math.cos(r)], [0, math.sin(r)], color="#888888",
                linewidth=1.0, linestyle=(0, (5, 3)))
    for a in (45, 135, 225, 315):
        r = math.radians(a)
        ax.plot([0, math.cos(r)], [0, math.sin(r)], color="#222222", linewidth=1.3)
    ax.add_patch(Circle((0, 0), 1.0, fill=False, edgecolor="#222222", linewidth=1.2))
    ax.plot([0], [0], marker="o", markersize=5, color="#ff7f0e")
    ax.set_xlim(-1.12, 1.12)
    ax.set_ylim(-1.12, 1.12)
    ax.set_title("(1) cut along the two coordinate axes\neight 45-degree triangles; "
                 "solid = diagonal seams, dashed = axes", fontsize=10, color="#333333")

    # (2) 两种粘合
    ax = axes[1]
    for idx, (sig, lab) in enumerate(((ident, "sigma = id  ->  8 disks"),
                                      (cyc8, "sigma = 8-cycle  ->  one disk"))):
        yy = 0.5 - idx
        for p in range(N):
            lo = 45 * p
            ax.add_patch(Wedge((0, yy), 0.36, lo + 3, lo + 45 - 3,
                               facecolor=colors(p % 10), edgecolor="white",
                               linewidth=0.6, alpha=0.6))
        ax.add_patch(Circle((0, yy), 0.36, fill=False, edgecolor="#222222", linewidth=1.0))
        ax.text(0.0, yy + 0.52, lab, fontsize=10, ha="center", color="#333333")
        # σ 的循环画成弧
        for c in cycles(sig):
            rad = 0.62 + 0.10 * len(c)
            for i, p in enumerate(c):
                a0 = math.radians(45 * p + 22.5)
                ax.plot([0.40 * math.cos(a0), rad * math.cos(a0)],
                        [yy + 0.40 * math.sin(a0), yy + rad * math.sin(a0)],
                        color="#d62728", linewidth=0.9)
    ax.set_xlim(-1.12, 1.12)
    ax.set_ylim(-1.12, 1.12)
    ax.set_title("(2) re-gluing is exactly a permutation sigma of the 8 pieces\n"
                 "number of disks = number of cycles of sigma; no new topology",
                 fontsize=10, color="#333333")

    # (3) 三孔 = 圆盘 + 2 个挖点
    ax = axes[2]
    ax.add_patch(Circle((0, 0), 1.0, facecolor="#eef3fb", edgecolor="#222222",
                        linewidth=1.4))
    ax.add_patch(Circle((0.0, 0.34), 0.22, facecolor="white", edgecolor="#d62728",
                        linewidth=1.4))
    ax.add_patch(Circle((-0.45, -0.36), 0.20, facecolor="white", edgecolor="#d62728",
                        linewidth=1.4))
    ax.text(0.0, 0.34, "O", ha="center", va="center", fontsize=10, color="#d62728")
    ax.text(-0.45, -0.36, "p", ha="center", va="center", fontsize=10, color="#d62728")
    ax.text(0.0, -0.95, "outer boundary", ha="center", fontsize=9, color="#333333")
    ax.set_xlim(-1.12, 1.12)
    ax.set_ylim(-1.12, 1.12)
    ax.set_title("(3) three holes = the glued disk with 2 punctures\n"
                 "chi = 1 - 2 = -1, b = 3 (pair of pants); one hole is the singularity O",
                 fontsize=10, color="#333333")

    fig.tight_layout()
    out = Path(__file__).with_name("cut_and_glue.png")
    fig.savefig(out, dpi=150, facecolor="white")
    plt.close(fig)
    print(f"图已输出: {out}")


if __name__ == "__main__":
    main()
