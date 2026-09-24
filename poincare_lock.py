#!/usr/bin/env python3
"""把欧氏的 enclosing_circles 锁进双曲庞加莱圆盘，并核验奇点结构是否保持。

理想态（a -> 0）的四个极限圆：圆心 (0, ±R/2) 与 (±R/2, 0)，半径 R/2，
都过白圆圆心 O。用 φ1: z -> z/R 把白圆变成单位圆（庞加莱圆盘边界）后，
四个圆变成四个以 (±1,0)、(0,±1) 为切点的 horocycle，仍全部经过盘心。

本程序：
  1. 对 φ1（归一化）与 φ2（非平凡圆盘自同构）核验同一组结构量：
     交点个数、异色对的 90° 横截角、同色对的外切与二阶切触、内切点落在边界；
  2. 说明盘内两条配对直线是过 O 的正交测地线，把圆盘切成 4 个扇形，
     每个扇形共形等价于一个上半平面模型；
  3. 作出三幅图：欧氏图 / 锁入圆盘 / 顶部扇形用 w = -z² 展开。

依赖：pip install matplotlib
运行：python poincare_lock.py
"""

import math
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

GREEN = "#00ff88"
GRID = "#2b2b45"


# ---------------------------------------------------------------- Möbius
def mobius(m, z: complex) -> complex:
    a, b, c, d = m
    return (a * z + b) / (c * z + d)


def image_circle(m, center, r, samples=3):
    """把圆 (center, r) 映到圆；用三个像点定圆。"""
    pts = [mobius(m, complex(center[0], center[1]) + r * complex(math.cos(t), math.sin(t)))
           for t in (0.0, 2.0943951, 4.1887902)]
    return fit_circle(pts)


def fit_circle(pts):
    (x1, y1), (x2, y2), (x3, y3) = [(p.real, p.imag) for p in pts]
    d = 2 * (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
    ux = ((x1 ** 2 + y1 ** 2) * (y2 - y3) + (x2 ** 2 + y2 ** 2) * (y3 - y1)
          + (x3 ** 2 + y3 ** 2) * (y1 - y2)) / d
    uy = ((x1 ** 2 + y1 ** 2) * (x3 - x2) + (x2 ** 2 + y2 ** 2) * (x1 - x3)
          + (x3 ** 2 + y3 ** 2) * (x2 - x1)) / d
    return (ux, uy), math.hypot(x1 - ux, y1 - uy)


def circle_intersections(c1, r1, c2, r2, tol=1e-6):
    dx, dy = c2[0] - c1[0], c2[1] - c1[1]
    d = math.hypot(dx, dy)
    if d > r1 + r2 + tol or d < abs(r1 - r2) - tol:
        return []
    a_ = (r1 * r1 - r2 * r2 + d * d) / (2 * d)
    h2 = max(r1 * r1 - a_ * a_, 0.0)
    h = math.sqrt(h2)
    px, py = c1[0] + a_ * dx / d, c1[1] + a_ * dy / d
    if h < tol:
        return [(px, py)]
    ox, oy = -dy / d * h, dx / d * h
    return [(px + ox, py + oy), (px - ox, py - oy)]


def crossing_angle(c1, r1, c2, r2):
    """两圆交点处的夹角（度）；相切时为 0。"""
    ps = circle_intersections(c1, r1, c2, r2)
    if not ps:
        return None
    px, py = ps[0]
    u = (px - c1[0], py - c1[1])
    v = (px - c2[0], py - c2[1])
    nu, nv = math.hypot(*u), math.hypot(*v)
    cos = max(-1.0, min(1.0, (u[0] * v[0] + u[1] * v[1]) / (nu * nv)))
    ang = math.degrees(math.acos(cos))
    return min(ang, 180.0 - ang)


def contact_order(c1, r1, c2, r2, tangent_point, orders=(2, 3, 4, 5)):
    """两圆在切点处的切触阶：沿圆 1 取弧长 s，距离圆 2 的最小距离 ∝ s^k。"""
    data = []
    for k in orders:
        s = 10.0 ** (-k)
        # 在圆 1 上、离切点弧长 s 处取点（沿远离圆 2 的一侧）。
        ang_t = math.atan2(tangent_point[1] - c1[1], tangent_point[0] - c1[0])
        sgn = 1.0
        ang = ang_t + sgn * s / r1
        p = (c1[0] + r1 * math.cos(ang), c1[1] + r1 * math.sin(ang))
        dist = abs(math.hypot(p[0] - c2[0], p[1] - c2[1]) - r2)
        data.append((s, dist))
    xs = [math.log(s) for s, _ in data]
    ys = [math.log(d) for _, d in data]
    n = len(xs)
    mx, my = sum(xs) / n, sum(ys) / n
    slope = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sum((x - mx) ** 2 for x in xs)
    return slope


def verify(tag: str, m, radius: float):
    """对映射 m 核验：圆像、交点个数、夹角、切触阶、内切点是否在边界。"""
    rho = radius / 2.0
    src = {
        "C+": ((0.0, rho), rho),
        "C-": ((0.0, -rho), rho),
        "D+": ((rho, 0.0), rho),
        "D-": ((-rho, 0.0), rho),
    }
    img = {k: image_circle(m, c, r) for k, (c, r) in src.items()}
    o_img = mobius(m, 0j)
    print(f"  [{tag}]")
    for k, ((cx, cy), r) in img.items():
        print(f"    {k} 的像: 圆心 ({cx:+.6f}, {cy:+.6f})，半径 {r:.6f}")
    print(f"    奇点 O 的像: ({o_img.real:+.6f}, {o_img.imag:+.6f})")
    worst = max(math.hypot(cx, cy) + r for (cx, cy), r in img.values())
    print(f"    四个像仍落在单位圆盘内: max(|圆心| + 半径) = {worst:.6f}")

    for k1, k2 in (("C+", "D+"), ("C+", "D-"), ("C-", "D+"), ("C-", "D-")):
        ang = crossing_angle(*img[k1], *img[k2])
        n = len(circle_intersections(*img[k1], *img[k2]))
        print(f"    异色对 {k1}/{k2}: 交点数 {n}，夹角 {ang:.6f}°")
    for k1, k2 in (("C+", "C-"), ("D+", "D-")):
        n = len(circle_intersections(*img[k1], *img[k2]))
        ang = crossing_angle(*img[k1], *img[k2])
        order = contact_order(*img[k1], *img[k2], (o_img.real, o_img.imag))
        print(f"    同色对 {k1}/{k2}: 交点数 {n}（外切），夹角 {ang:.6f}°，"
              f"切触阶拟合 {order:.4f}")
    for k in ("C+", "C-", "D+", "D-"):
        # 原图中的内切点在 (±R, 0)、(0, ±R)。
        (cx, cy), r = src[k]
        tp = (cx * radius / rho, cy * radius / rho)
        w = mobius(m, complex(*tp))
        print(f"    {k} 与白圆的内切点像: |w| = {abs(w):.6f}")


def main(radius: float = 4.0, c: float = 0.4) -> None:
    print(f"归一化半径 R = {radius:g}，四个极限圆半径 ρ = R/2 = {radius / 2:g}")
    print()
    print("φ1: z -> z/R （把欧氏白圆锁成单位圆，即庞加莱圆盘边界）")
    verify("φ1", (1.0, 0.0, 0.0, radius), radius)
    print()
    print(f"φ2 = 圆盘自同构 ∘ φ1: z -> (z + cR)/(R + c z)，c = {c:g}"
          " （非平凡的圆盘自同构：把奇点挪开）")
    verify("φ2", (1.0, c * radius, c, radius), radius)
    print()

    print("四个上半平面模型")
    print("  两条配对直线在盘内是过 O 的测地线（直径），在 O 处正交，把圆盘切成 4 个扇形；")
    print("  每个扇形是单连通真域、在 O 处有直角顶点，由 Riemann 映射定理共形等价于上半平面。")
    print("  注意：这是共形等价，不是等距；O 是四个模型共用的角点，不是尖点或理想顶点。")
    inside = total = 0
    for i in range(20001):
        u = (i + 0.5) / 20001
        r = math.sqrt(u)
        th = 2 * math.pi * ((i * 7919) % 20001) / 20001
        z = complex(r * math.cos(th), r * math.sin(th))
        if not (math.pi / 4 < th < 3 * math.pi / 4):
            continue
        total += 1
        w = -z * z
        if w.real > 0 and abs(w) < 1:
            inside += 1
    print(f"  数值核对：顶部扇形内的采样点共 {total} 个，全部满足 Re w > 0 且 |w| < 1 "
          f"（{inside}/{total}），即扇形映到右半圆盘。")
    print(f"  扇形占圆盘的面积比 {total / 20001:.4f}（应为 1/4 = 0.25）")
    print("  扇形两条边（即 45°、135° 两条配对测地线）在 w = -z² 下映到正、负虚轴，")
    print("  合成右半平面的边界；扇形内部的切锥直径（90°）映到正实轴，")
    print("  O 映到 w = 0，成为该半平面模型的边界点。")
    print()

    # ------------------------------------------------------------ 作图
    fig, axes = plt.subplots(1, 3, figsize=(18, 6.4), facecolor="black")
    for ax in axes:
        ax.set_facecolor("black")
        ax.set_aspect("equal")
        ax.set_xticks([])
        ax.set_yticks([])

    # (1) 欧氏参考图
    ax = axes[0]
    rho = radius / 2.0
    for cy, col in ((rho, "#ff0000"), (-rho, "#ff0000")):
        ax.add_patch(Circle((0, cy), rho, fill=False, edgecolor=col, linewidth=1.0))
    for cx, col in ((rho, "#0000ff"), (-rho, "#0000ff")):
        ax.add_patch(Circle((cx, 0), rho, fill=False, edgecolor=col, linewidth=1.0))
    ax.add_patch(Circle((0, 0), radius, fill=False, edgecolor="#ffffff", linewidth=1.0))
    for sl in (+1, -1):
        ax.plot([-rho, rho], [-sl * rho, sl * rho], color=GREEN, linewidth=1.0,
                linestyle=(0, (6, 4)))
    ax.plot([0], [0], marker="o", markersize=4, color="#ffaa00")
    ax.set_xlim(-radius * 1.06, radius * 1.06)
    ax.set_ylim(-radius * 1.06, radius * 1.06)
    ax.set_title("(1) Euclidean ideal state\nwhite circle = frame", color="#dddddd", fontsize=10)

    # (2) 锁入庞加莱圆盘
    ax = axes[1]
    for i in range(24):
        t = math.pi * i / 24
        ax.plot([-math.cos(t), math.cos(t)], [-math.sin(t), math.sin(t)],
                color=GRID, linewidth=0.5)
    for hr in (0.2, 0.4, 0.6, 0.8):
        ax.add_patch(Circle((1 - hr, 0), hr, fill=False, edgecolor=GRID, linewidth=0.5))
        ax.add_patch(Circle((-1 + hr, 0), hr, fill=False, edgecolor=GRID, linewidth=0.5))
        ax.add_patch(Circle((0, 1 - hr), hr, fill=False, edgecolor=GRID, linewidth=0.5))
        ax.add_patch(Circle((0, -1 + hr), hr, fill=False, edgecolor=GRID, linewidth=0.5))
    for cy, col in ((0.5, "#ff0000"), (-0.5, "#ff0000")):
        ax.add_patch(Circle((0, cy), 0.5, fill=False, edgecolor=col, linewidth=1.6))
    for cx, col in ((0.5, "#0000ff"), (-0.5, "#0000ff")):
        ax.add_patch(Circle((cx, 0), 0.5, fill=False, edgecolor=col, linewidth=1.6))
    ax.add_patch(Circle((0, 0), 1.0, fill=False, edgecolor="#ffffff", linewidth=1.4))
    for sl in (+1, -1):
        ax.plot([-0.7071, 0.7071], [-sl * 0.7071, sl * 0.7071], color=GREEN,
                linewidth=1.4, linestyle=(0, (6, 4)))
        ax.plot([0.7071, 1.0], [sl * 0.7071, sl * 1.0], color=GREEN, linewidth=0.6)
        ax.plot([-0.7071, -1.0], [-sl * 0.7071, -sl * 1.0], color=GREEN, linewidth=0.6)
    ax.plot([0], [0], marker="o", markersize=4, color="#ffaa00")
    for lab, (lx, ly) in (("I", (0.62, 0.0)), ("II", (0.0, 0.62)),
                          ("III", (-0.62, 0.0)), ("IV", (0.0, -0.62))):
        ax.text(lx, ly, lab, color="#ffcc66", fontsize=11, ha="center", va="center")
    ax.set_xlim(-1.12, 1.12)
    ax.set_ylim(-1.12, 1.12)
    ax.set_title("(2) locked into the Poincare disk\n4 horocycles, tangent at (0,+-1),(+-1,0)",
                 color="#dddddd", fontsize=10)

    # (3) 顶部扇形展开
    ax = axes[2]
    ts = [i * 2 * math.pi / 4000 for i in range(4001)]
    half = [complex(0.5 * math.cos(t), 0.5 + 0.5 * math.sin(t)) for t in ts]
    im = [-z * z for z in half]
    ax.plot([p.real for p in im], [p.imag for p in im], color="#ff0000", linewidth=1.6)
    arc = [complex(math.cos(t), math.sin(t))
           for t in [math.pi * i / 720 for i in range(-180, 181)]]
    ax.plot([p.real for p in arc], [p.imag for p in arc], color="#ffffff", linewidth=1.2)
    ax.plot([0, 0], [-1, 1], color=GREEN, linewidth=1.6, linestyle=(0, (6, 4)))
    ax.plot([0, 1], [0, 0], color="#8888ff", linewidth=1.1, linestyle=(0, (3, 3)))
    ax.plot([0], [0], marker="o", markersize=5, color="#ffaa00")
    ax.plot([1], [0], marker="o", markersize=4, color="#ffffff")
    ax.text(0.04, 0.06, "O -> 0", color="#ffaa00", fontsize=9)
    ax.text(0.86, 0.06, "1", color="#ffffff", fontsize=9)
    ax.text(-0.09, 0.92, "i", color=GREEN, fontsize=9)
    ax.text(-0.12, -1.02, "-i", color=GREEN, fontsize=9)
    ax.set_xlim(-0.55, 1.30)
    ax.set_ylim(-1.15, 1.15)
    ax.set_title("(3) one sector unfolded: w = -z^2\ntop sector -> right half-disk, O -> 0",
                 color="#dddddd", fontsize=10)

    fig.tight_layout()
    out = Path(__file__).with_name("poincare_lock.png")
    fig.savefig(out, dpi=160, facecolor="black")
    plt.close(fig)
    print(f"图已输出: {out}")


if __name__ == "__main__":
    main()
