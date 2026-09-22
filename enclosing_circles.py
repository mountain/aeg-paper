#!/usr/bin/env python3
"""双极圆族的几何重绘：红、蓝圆族，以及与四个最外侧圆相切的白圆。

依赖：pip install matplotlib
运行：python enclosing_circles.py
输出：程序所在目录的 enclosing_circles.png
"""

import argparse
import math
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle


def draw(output: Path, a: float = 1.0, radius: float = 4.0) -> None:
    """两个焦点为 (±a, 0)，白色外圆的圆心为原点、半径为 radius。"""
    if not (math.isfinite(a) and math.isfinite(radius) and 0 < a < radius):
        raise ValueError("参数须满足 0 < a < radius，且均为有限数。")

    fig, ax = plt.subplots(figsize=(8, 8), dpi=160, facecolor="black")
    fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
    ax.set_facecolor("black")
    ax.set_aspect("equal")
    ax.set_axis_off()

    def circle(x: float, y: float, r: float, color: str, width=0.9):
        ax.add_patch(Circle((x, y), r, fill=False, edgecolor=color,
                            linewidth=width, antialiased=True))

    # 红圆经过两个焦点：圆心 (0, a cot(v))，半径 a/sin(v)。
    # 首尾两个圆的外端恰好到达 y = ±radius。
    v_min = 2 * math.atan(a / radius)
    for k in range(11):
        v = v_min + k * (math.pi - 2 * v_min) / 10
        circle(0, a / math.tan(v), a / math.sin(v), "#ff0000")

    # 蓝圆与红圆正交：圆心 (±a coth(u), 0)，半径 a/sinh(u)。
    # 第一对蓝圆的外端恰好到达 x = ±radius。
    u_min = math.log((radius + a) / (radius - a))
    for k in range(11):
        u = u_min + 0.3 * k
        x = a / math.tanh(u)
        r = a / math.sinh(u)
        circle(-x, 0, r, "#0000ff")
        circle(x, 0, r, "#0000ff")

    circle(0, 0, radius, "#ffffff", width=1.0)
    limit = radius * 1.06
    ax.set_xlim(-limit, limit)
    ax.set_ylim(-limit, limit)
    output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output, dpi=160, facecolor="black")
    plt.close(fig)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path,
                        default=Path(__file__).with_suffix(".png"))
    args = parser.parse_args()
    draw(args.output)
