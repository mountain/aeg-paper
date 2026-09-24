#!/usr/bin/env python3
"""把 Apollonian_gasket / Cicle_inversion 里的每个圆，用上一轮的“理想圆盘”补上。

上一轮得到的理想圆盘：外圆内放四个半径减半的圆，它们内切于外圆于四个等分点、
并全部经过外圆圆心；再加两条过圆心的配对直线，奇点就在圆心。

本程序：
  1. 用 Descartes 定理生成标准 cross 型 Apollonian 密铺
     （外圆 + 4 个种子圆 + 中心圆，再递归填满所有曲边三角形）；
  2. 统计每个圆的相切点数——外圆 4、4 个种子圆各 4、中心圆 4，其余圆 3；
  3. 两种“补上”方式：
     (A) 字面读法：每个圆内放一个同构的理想圆盘（四条半尺寸圆切在
         0°/90°/180°/270°，加两条过圆心的配对直线）；
     (B) 相切对齐：每个圆在自己的每个相切点处放一条半径减半的圆（必过该圆圆心）；
         在外圆上 (B) 与 (A) 完全重合，因为外圆的四个相切点正是四个基点。
  4. 出图：参考密铺 / (A) / (B) / (B) 的局部放大（自相似）。

依赖：pip install matplotlib
运行：python apollonian_disk.py
"""

import argparse
import cmath
import math
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

GRAY = "#333333"
DECO = "#d62728"
PAIR = "#2ca02c"
DOT = "#ff7f0e"
TOL = 1e-7


# ------------------------------------------------------------ Descartes 密铺
def _is_tangent(z4, r4, z, r):
    d = abs(z4 - z)
    return abs(d - (r4 + r)) < TOL or abs(d - abs(r - r4)) < TOL


def _soddy(k1, z1, k2, z2, k3, z3, circles):
    """给定三个两两相切的圆，返回内切于该曲边三角形的那个圆 (z, r, k)。"""
    s = k1 * k2 + k2 * k3 + k3 * k1
    if s <= 0:
        return None
    base = k1 * k2 * z1 * z2 + k2 * k3 * z2 * z3 + k3 * k1 * z3 * z1
    best = None
    for s1 in (+1, -1):
        k4 = k1 + k2 + k3 + s1 * 2 * math.sqrt(s)
        if abs(k4) < 1e-12:
            continue
        for s2 in (+1, -1):
            z4 = (k1 * z1 + k2 * z2 + k3 * z3 + s2 * 2 * cmath.sqrt(base)) / k4
            r4 = 1.0 / k4
            if r4 <= 0:
                continue
            if not (_is_tangent(z4, r4, z1, 1.0 / k1)
                    and _is_tangent(z4, r4, z2, 1.0 / k2)
                    and _is_tangent(z4, r4, z3, 1.0 / k3)):
                continue
            if any(abs(z4 - z) < 1e-9 and abs(r4 - r) < 1e-9 for z, r, _k, _g in circles):
                continue
            if best is None or r4 < best[1]:
                best = (z4, r4, k4)
    return best


def build_packing(min_radius=0.006, max_circles=4000):
    """返回 [(z, r, k, gen)]，含外圆（半径 1、曲率 -1）。gen 为“代”。"""
    circles = [(0j, 1.0, -1.0, 0)]
    r_seed = math.sqrt(2) - 1
    seeds = []
    for i in range(4):
        ang = math.pi / 2 * i
        z = (1 - r_seed) * complex(math.cos(ang), math.sin(ang))
        seeds.append((z, r_seed, 1.0 / r_seed, 1))
    circles.extend(seeds)
    r_cen = 3 - 2 * math.sqrt(2)
    central = (0j, r_cen, 1.0 / r_cen, 2)
    circles.append(central)

    outer = circles[0]
    gaps = []
    for i in range(4):
        a, b = seeds[i], seeds[(i + 1) % 4]
        gaps.append((outer, a, b))
        gaps.append((central, a, b))

    while gaps and len(circles) < max_circles:
        a, b, c = gaps.pop()
        new = _soddy(a[2], a[0], b[2], b[0], c[2], c[0], circles)
        if new is None or new[1] < min_radius:
            continue
        new = (new[0], new[1], new[2], 1 + max(a[3], b[3], c[3]))
        circles.append(new)
        gaps.append((new, a, b))
        gaps.append((new, b, c))
        gaps.append((new, c, a))
    return circles


def tangency_points(circles):
    """每个圆与所有邻居的相切点，按角度排序。

    返回 {index: [(角度, 点, 邻居半径), ...]}。注意 Apollonian 密铺中每个圆
    会与越来越多的更小圆相切，所以相切点总数随截断尺度增长；其中只有少数
    几个是“结构性”的（与同代或更大圆的相切）。
    """
    pts = {i: [] for i in range(len(circles))}
    for i in range(len(circles)):
        zi, ri, _k, _g = circles[i]
        for j in range(i + 1, len(circles)):
            zj, rj, _k2, _g2 = circles[j]
            d = abs(zi - zj)
            if abs(d - (ri + rj)) < TOL:          # 外切
                p = zi + ri * (zj - zi) / d
            elif abs(d - abs(ri - rj)) < TOL:     # 内切
                p = zi + ri * (zj - zi) / d if ri > rj else zj + rj * (zi - zj) / d
            else:
                continue
            pts[i].append((cmath.phase(p - zi) % (2 * math.pi), p, rj))
            pts[j].append((cmath.phase(p - zj) % (2 * math.pi), p, ri))
    for i in pts:
        pts[i].sort(key=lambda t: t[0])
    return pts


def structural_dirs(tps, r_self, ratio=0.3, k=4):
    """结构性的相切方向：邻居半径不小于自身半径 ratio 倍的那些（至多 k 个）。

    密铺中一个圆会与无穷多更小的圆相切；只有同尺度及更大的邻居才对应
    曲边三角形的“边”，也就是这个圆在密铺中的结构性相切。
    """
    order = [t for t in tps if t[2] >= ratio * r_self]
    order = sorted(order, key=lambda t: -t[2])[:k]
    return sorted(order, key=lambda t: t[0])


# ------------------------------------------------------------------- 作图
def draw_parent(ax, z, r, color=GRAY, lw=0.7, alpha=1.0):
    ax.add_patch(Circle((z.real, z.imag), r, fill=False, edgecolor=color,
                        linewidth=lw, alpha=alpha, antialiased=True))


def fill_literal(ax, z, r, lw=0.35):
    """(A) 字面理想圆盘：4 条半尺寸圆 + 两条配对直线 + 圆心奇点。"""
    for k, ang in enumerate((0.0, math.pi / 2, math.pi, 3 * math.pi / 2)):
        c = z + (r / 2) * complex(math.cos(ang), math.sin(ang))
        draw_parent(ax, c, r / 2, DECO if k % 2 == 0 else "#1f77b4", lw, alpha=0.8)
    if r >= 0.05:                      # 配对直线只画在大圆上，否则碎线过多
        for sl in (+1, -1):
            p1 = z + (r / 2) * complex(-1, -sl)
            p2 = z + (r / 2) * complex(+1, sl)
            ax.plot([p1.real, p2.real], [p1.imag, p2.imag], color=PAIR, linewidth=lw,
                    linestyle=(0, (3, 3)))
    ax.plot([z.real], [z.imag], marker="o", markersize=1.2, color=DOT)


GEN_COLORS = ["#d62728", "#1f77b4", "#2ca02c", "#9467bd", "#ff7f0e", "#17becf", "#8c564b"]


def fill_aligned(ax, z, r, dirs, color=DECO, lw=0.35):
    """(B) 相切对齐：在每个（结构性）相切方向放一条半径减半、过圆心的圆。"""
    for ang, _p, _rn in dirs:
        c = z + (r / 2) * complex(math.cos(ang), math.sin(ang))
        draw_parent(ax, c, r / 2, color, lw, alpha=0.8)
    ax.plot([z.real], [z.imag], marker="o", markersize=1.2, color=DOT)


def main(min_radius: float = 0.0005, decorate_above: float = 0.0) -> None:
    circles = build_packing(min_radius=min_radius)
    tps = tangency_points(circles)
    gens = sorted({c[3] for c in circles})
    all_counts = sorted(len(tps[i]) for i in range(len(circles)))
    struct = {i: structural_dirs(tps[i], circles[i][1]) for i in range(len(circles))}
    struct_counts = {}
    for i in range(len(circles)):
        struct_counts[len(struct[i])] = struct_counts.get(len(struct[i]), 0) + 1
    print(f"Apollonian 密铺：{len(circles)} 个圆，半径 {circles[0][1]:.4f} .. "
          f"{min(c[1] for c in circles):.6f}，代数（generation）{gens[0]} .. {gens[-1]}")
    print(f"每个圆与邻居的相切点总数（含越来越小的圆）：{all_counts[0]} .. {all_counts[-1]}，"
          f"中位数 {all_counts[len(all_counts) // 2]}")
    print("  说明：密铺中一个圆会与无穷多个更小的圆相切，所以“切点总数”随截断尺度增长，"
          "不是结构不变量。")
    print(f"其中只有少数是结构性相切（邻居半径 ≥ 自身 0.3 倍者，至多取 4 个）："
          + ", ".join(f"{n} 个方向: {c} 个圆" for n, c in sorted(struct_counts.items())))
    print()

    angs0 = [math.degrees(a) % 360 for a, _p, _r in sorted(struct[0])]
    print(f"外圆的结构性相切方向："
          + ", ".join(f"{a:.4f}°" for a in angs0))
    print("  这正是上一轮理想圆盘的四个基点 0°/90°/180°/270°；")
    sd = struct[1]
    print("  再看一个种子圆（圆 1，半径 %.4f）的结构性相切方向：" % circles[1][1]
          + ", ".join(f"{math.degrees(a) % 360:.4f}°(邻居半径 {rn:.4f})"
                      for a, _p, rn in sorted(sd)))
    print("    其中与白圆、与左右两个种子圆的三个方向，正是 Cicle_inversion 里")
    print("    那个红色虚线三角形的三个顶点；第四个方向指向中心圆。")
    print("  所以在外圆上，「按结构相切补」与「按字面理想圆盘补」是同一个图形。")

    # 构造性核验：每条补上的圆都内切于母圆且过母圆圆心
    worst = 0.0
    for i in range(len(circles)):
        z, r, _k, _g = circles[i]
        for ang, _p, _rn in struct[i]:
            c = z + (r / 2) * complex(math.cos(ang), math.sin(ang))
            worst = max(worst, abs(abs(c - z) - r / 2), abs(abs(c - z) - r / 2))
    print(f"  核验：所有补上的圆都满足 |圆心-母圆心| = 母半径/2 = 自身半径 "
          f"（最大偏差 {worst:.3e}）→ 既内切母圆，又过母圆圆心。")
    print()

    print("每个圆心处的切锥（补圆在圆心处的切线方向 = 相切方向 + 90°，按直线取模 180°）：")
    deep = min((i for i in range(len(circles)) if 0.01 < circles[i][1] < 0.02),
               key=lambda i: abs(circles[i][1] - 0.014), default=None)
    for label, idx in (("外圆", 0), ("种子圆", 1), ("中心圆", 5), ("深处的圆", deep)):
        if idx is None:
            continue
        dirs = sorted({round((math.degrees(a) + 90.0) % 180.0, 6) for a, _p, _rn in struct[idx]})
        mult = {}
        for a, _p, _rn in struct[idx]:
            k = round((math.degrees(a) + 90.0) % 180.0, 6)
            mult[k] = mult.get(k, 0) + 1
        txt = ", ".join(f"{k:.4f}°×{v}" for k, v in sorted(mult.items()))
        r_i = circles[idx][1]
        print(f"  {label} (半径 {r_i:.4f}, {len(struct[idx])} 条补圆): 切线方向 {txt}")
    print("  外圆与中心圆给出两条正交方向各重数 2（上一轮的切锥），配对的平分线成 90°；")
    print("  种子圆的切锥是三线 {45°, 90°, 135°}，其中 90° 重数 2——与白圆、中心圆的那对")
    print("  反向相切被压成同一条切线，而它与左右邻居的那对补圆仍正交。")
    print()

    decorated = [i for i, c in enumerate(circles) if c[1] >= decorate_above]
    print(f"被补上圆盘的圆（半径 ≥ {decorate_above:g}）: {len(decorated)} / {len(circles)}")
    print()

    # ------------------------------------------------------------ 图
    fig, axes = plt.subplots(2, 2, figsize=(15, 15), facecolor="white")
    for ax in axes.ravel():
        ax.set_facecolor("white")
        ax.set_aspect("equal")
        ax.set_xticks([])
        ax.set_yticks([])

    ax = axes[0][0]
    for z, r, _k, _g in circles:
        draw_parent(ax, z, r, "#1a1a1a", 0.6)
    ax.set_xlim(-1.03, 1.03)
    ax.set_ylim(-1.03, 1.03)
    ax.set_title("(1) Apollonian packing (Descartes)\nreference: outlines only",
                 color="#333333", fontsize=10)

    ax = axes[0][1]
    for z, r, _k, _g in circles:
        draw_parent(ax, z, r, "#bbbbbb", 0.3)
    for i in decorated:
        z, r, _k, _g = circles[i]
        fill_literal(ax, z, r)
    ax.set_xlim(-1.03, 1.03)
    ax.set_ylim(-1.03, 1.03)
    ax.set_title("(A) every circle filled with the ideal disk (literal)\n"
                 "4 half-size circles at 0/90/180/270 + 2 pairing lines",
                 color="#333333", fontsize=10)

    ax = axes[1][0]
    for z, r, _k, _g in circles:
        draw_parent(ax, z, r, "#bbbbbb", 0.3)
    for i in decorated:
        z, r, _k, g = circles[i]
        fill_aligned(ax, z, r, struct[i], GEN_COLORS[g % len(GEN_COLORS)])
    ax.set_xlim(-1.03, 1.03)
    ax.set_ylim(-1.03, 1.03)
    ax.set_title("(B) filled along structural tangencies\n"
                 "outside circle: identical to (A); deeper circles: 3 directions",
                 color="#333333", fontsize=10)

    ax = axes[1][1]
    target = min((i for i in decorated if 0.008 < circles[i][1] < 0.03),
                 key=lambda i: abs(circles[i][1] - 0.016), default=decorated[-1])
    z0, r0, _k, _g = circles[target]
    for z, r, _k, _g2 in circles:
        draw_parent(ax, z, r, "#bbbbbb", 0.45)
    for i in decorated:
        z, r, _k, g = circles[i]
        fill_aligned(ax, z, r, struct[i], GEN_COLORS[g % len(GEN_COLORS)])
    w = 2.4 * r0
    ax.set_xlim(z0.real - w, z0.real + w)
    ax.set_ylim(z0.imag - w, z0.imag + w)
    ax.set_title(f"(B) zoom on a circle of radius {r0:.4f}\n"
                 "same structure, one scale down", color="#333333", fontsize=10)

    fig.tight_layout()
    out = Path(__file__).with_name("apollonian_disk.png")
    fig.savefig(out, dpi=150, facecolor="white")
    plt.close(fig)
    print(f"图已输出: {out}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--min-radius", type=float, default=0.0005)
    ap.add_argument("--decorate-above", type=float, default=0.0)
    args = ap.parse_args()
    main(min_radius=args.min_radius, decorate_above=args.decorate_above)
