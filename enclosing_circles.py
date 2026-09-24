#!/usr/bin/env python3
"""双极圆族的几何重绘。

默认模式：红、蓝圆族，与四个最外侧圆相切的白圆，
以及最外层四圆交点按“左下—右上”“右下—左上”配对所得的连线。

理想模式（--ideal）：只画 a -> 0 的精确极限。此时红族与蓝族的中间圆
全部塌缩到原点（奇点），剩下的“极限圆”是四个半径 R/2、内切于白圆且
全部过原点的圆；四个非原点交点构成正方形，两条配对连线夹角恰为 90 度。

依赖：pip install matplotlib
运行：python enclosing_circles.py [--ideal]
输出：程序所在目录的 enclosing_circles.png，并在终端打印坐标与夹角。
"""

import argparse
import math
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

GREEN = "#00ff88"


def circle_intersections(c1, r1, c2, r2):
    """两圆交点，返回 0、1 或 2 个点。"""
    dx, dy = c2[0] - c1[0], c2[1] - c1[1]
    d = math.hypot(dx, dy)
    if d == 0.0 or d > r1 + r2 or d < abs(r1 - r2):
        return []
    a_ = (r1 * r1 - r2 * r2 + d * d) / (2 * d)
    h2 = r1 * r1 - a_ * a_
    if h2 <= 0.0:
        return [(c1[0] + a_ * dx / d, c1[1] + a_ * dy / d)]
    h = math.sqrt(h2)
    px, py = c1[0] + a_ * dx / d, c1[1] + a_ * dy / d
    ox, oy = -dy / d * h, dx / d * h
    return [(px + ox, py + oy), (px - ox, py - oy)]


def outermost(points):
    """交点中离原点更远者，即落在最外一层的那个交点。"""
    return max(points, key=lambda p: math.hypot(p[0], p[1]))


def line_data(name1, name2, corners, ax):
    """画一条配对连线的线段与端点，并返回其方向向量。"""
    (x1, y1), (x2, y2) = corners[name1], corners[name2]
    ax.plot([x1, x2], [y1, y2], color=GREEN, linewidth=1.0,
            linestyle=(0, (6, 4)), solid_capstyle="round")
    dist = abs(x1 * y2 - x2 * y1) / math.hypot(x2 - x1, y2 - y1)
    print(f"{name1}—{name2}: 方向 ({x2 - x1:.6f}, {y2 - y1:.6f})，"
          f"斜率 {(y2 - y1) / (x2 - x1):.6f}，到原点距离 {dist:.3e}")
    return (x2 - x1, y2 - y1)


def line_angle(v1, v2):
    """两方向向量所张的两条直线夹角（取锐角或直角）。"""
    cross = v1[0] * v2[1] - v1[1] * v2[0]
    dot = v1[0] * v2[0] + v1[1] * v2[1]
    angle = math.degrees(math.atan2(abs(cross), dot))
    return min(angle, 180.0 - angle)


def new_axes(radius: float):
    fig, ax = plt.subplots(figsize=(8, 8), dpi=160, facecolor="black")
    fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
    ax.set_facecolor("black")
    ax.set_aspect("equal")
    ax.set_axis_off()
    limit = radius * 1.06
    ax.set_xlim(-limit, limit)
    ax.set_ylim(-limit, limit)
    return fig, ax


def circle(ax, x: float, y: float, r: float, color: str, width=0.9):
    ax.add_patch(Circle((x, y), r, fill=False, edgecolor=color,
                        linewidth=width, antialiased=True))


def draw(output: Path, a: float = 1.0, radius: float = 4.0) -> None:
    """两个焦点为 (±a, 0)，白色外圆的圆心为原点、半径为 radius。"""
    if not (math.isfinite(a) and math.isfinite(radius) and 0 < a < radius):
        raise ValueError("参数须满足 0 < a < radius，且均为有限数。")

    fig, ax = new_axes(radius)

    # 红圆经过两个焦点：圆心 (0, a cot(v))，半径 a/sin(v)。
    # 首尾两个圆的外端恰好到达 y = ±radius。
    v_min = 2 * math.atan(a / radius)
    reds = []
    for k in range(11):
        v = v_min + k * (math.pi - 2 * v_min) / 10
        reds.append(((0.0, a / math.tan(v)), a / math.sin(v)))
    for center, r in reds:
        circle(ax, center[0], center[1], r, "#ff0000")

    # 蓝圆与红圆正交：圆心 (±a coth(u), 0)，半径 a/sinh(u)。
    # 第一对蓝圆的外端恰好到达 x = ±radius。
    u_min = math.log((radius + a) / (radius - a))
    blues = []
    for k in range(11):
        u = u_min + 0.3 * k
        blues.append(((a / math.tanh(u), 0.0), a / math.sinh(u)))
    for center, r in blues:
        circle(ax, -center[0], 0, r, "#0000ff")
        circle(ax, center[0], 0, r, "#0000ff")

    circle(ax, 0, 0, radius, "#ffffff", width=1.0)

    # 最外一层四圆：红族首尾两个（上、下）与蓝族首对（右、左）。
    top, bottom = reds[0], reds[-1]
    right = blues[0]
    left = ((-right[0][0], 0.0), right[1])

    corners = {
        "右上": outermost(circle_intersections(*top, *right)),
        "左上": outermost(circle_intersections(*top, *left)),
        "右下": outermost(circle_intersections(*bottom, *right)),
        "左下": outermost(circle_intersections(*bottom, *left)),
    }

    for name, (px, py) in corners.items():
        ax.plot([px], [py], marker="o", markersize=3.0, color=GREEN)
        print(f"{name}交点: ({px:.6f}, {py:.6f})  |P| = {math.hypot(px, py):.6f}")

    v1 = line_data("左下", "右上", corners, ax)
    v2 = line_data("右下", "左上", corners, ax)
    print(f"两条直线的夹角: {line_angle(v1, v2):.6f} 度")
    print("解析值 2*atan((R^2-a^2)/(R^2+a^2)) = "
          f"{math.degrees(2 * math.atan((radius ** 2 - a ** 2) / (radius ** 2 + a ** 2))):.6f} 度")

    output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output, dpi=160, facecolor="black")
    plt.close(fig)


def draw_ideal(output: Path, radius: float = 4.0) -> None:
    """a -> 0 的精确极限（理想状态）。

    红族极限圆：圆心 (0, ±R/2)，半径 R/2；蓝族极限圆：圆心 (±R/2, 0)，半径 R/2。
    四个圆都过原点，并分别内切白圆于 (0, ±R) 与 (±R, 0)。
    相邻两圆的两个交点之一是原点（奇点、四圆公共点），另一个是 (±R/2, ±R/2)。
    """
    if not (math.isfinite(radius) and radius > 0):
        raise ValueError("radius 须为正的有限数。")

    r = radius / 2.0
    fig, ax = new_axes(radius)

    for sy in (+1, -1):
        circle(ax, 0.0, sy * r, r, "#ff0000")
    for sx in (+1, -1):
        circle(ax, sx * r, 0.0, r, "#0000ff")
    circle(ax, 0, 0, radius, "#ffffff", width=1.0)

    corners = {(sx, sy): (sx * r, sy * r)
               for sx in (+1, -1) for sy in (+1, -1)}

    print(f"理想状态（a -> 0 的精确极限），白圆半径 R = {radius:.6f}：")
    print(f"  红族极限圆: 圆心 (0, ±{r:.6f})，半径 {r:.6f}")
    print(f"  蓝族极限圆: 圆心 (±{r:.6f}, 0)，半径 {r:.6f}")
    print(f"  四个圆均过原点 O（奇点），并内切白圆于 (0, ±{radius:.6f}) 与 (±{radius:.6f}, 0)")

    for (sx, sy), (px, py) in sorted(corners.items()):
        print(f"  交点 ({'+' if sx > 0 else '-'}{abs(px):.6f}, "
              f"{'+' if sy > 0 else '-'}{abs(py):.6f})")

    named = {
        "右上": corners[(+1, +1)],
        "左上": corners[(-1, +1)],
        "右下": corners[(+1, -1)],
        "左下": corners[(-1, -1)],
    }
    for name, (px, py) in named.items():
        ax.plot([px], [py], marker="o", markersize=3.0, color=GREEN)
    v1 = line_data("左下", "右上", named, ax)
    v2 = line_data("右下", "左上", named, ax)
    ax.plot([0.0], [0.0], marker="o", markersize=3.0, color="#ffaa00")
    print(f"  两条直线的夹角: {line_angle(v1, v2):.6f} 度")
    print("  解析值 2*atan(R^2/R^2) = 2*atan(1) = 90.000000 度")

    output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output, dpi=160, facecolor="black")
    plt.close(fig)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=None)
    parser.add_argument("--radius", type=float, default=4.0)
    parser.add_argument("--a", type=float, default=1.0)
    parser.add_argument("--ideal", action="store_true",
                        help="只画 a -> 0 的精确极限（理想状态）")
    args = parser.parse_args()

    if args.ideal:
        target = args.output or Path(__file__).with_name("enclosing_circles_ideal.png")
        draw_ideal(target, radius=args.radius)
    else:
        target = args.output or Path(__file__).with_suffix(".png")
        draw(target, a=args.a, radius=args.radius)
