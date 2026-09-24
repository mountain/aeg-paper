#!/usr/bin/env python3
"""理想状态（a -> 0 极限）下奇点 O 的局部结构。

四个极限圆（半径 ρ = R/2，圆心 (0, ±ρ) 与 (±ρ, 0)）全部经过 O：
    C±: x² + y² ∓ 2ρ y = 0      （红，中心在 y 轴上）
    D±: x² + y² ∓ 2ρ x = 0      （蓝，中心在 x 轴上）

本程序给出：
  1. 每个圆在 O 的切线方向；
  2. O 附近的二阶局部形状 y = ±x²/R、x = ±y²/R；
  3. 同色两圆的相切阶（外切，二阶切触）与异色两圆的横截正交性；
  4. 四圆并集的切锥多项式（最低次齐次部分）及其数值验证；
  5. O 附近的放大图，以及 a > 0 时焦点处“方向笔束”的对照图。

依赖：pip install matplotlib
运行：python ideal_singularity.py
"""

import math
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle


def union_polynomial(x: float, y: float, rho: float) -> float:
    """四圆并集的乘积多项式 ∏(x²+y² ∓ 2ρy)(x²+y² ∓ 2ρx)。"""
    s = x * x + y * y
    return (s * s - 4 * rho * rho * y * y) * (s * s - 4 * rho * rho * x * x)


def lower_arc(x: float, rho: float, sign: int) -> float:
    """圆心 (0, sign*ρ)、过 O 的圆在横坐标 x 处的纵坐标（取过 O 的分支）。"""
    return sign * (rho - math.sqrt(rho * rho - x * x))


def main(radius: float = 4.0) -> None:
    rho = radius / 2.0
    print(f"理想状态局部结构：R = {radius:.6f}，ρ = R/2 = {rho:.6f}")
    print()
    print("1. 四个极限圆与它们在 O 的切线")
    circles = [("C+ (0, +ρ)", (0.0, rho), "红"), ("C- (0, -ρ)", (0.0, -rho), "红"),
               ("D+ (+ρ, 0)", (rho, 0.0), "蓝"), ("D- (-ρ, 0)", (-rho, 0.0), "蓝")]
    for name, (cx, cy), color in circles:
        # O 到圆心的向量即法向，切线与之垂直。
        tx, ty = -cy, cx
        n = math.hypot(tx, ty)
        print(f"   {name:12s} {color}  法向 ({cx:+.4f}, {cy:+.4f})/ρ  "
              f"切线方向 ({tx / n:+.6f}, {ty / n:+.6f})  "
              f"切线 {'y = 0' if abs(ty) < 1e-12 else 'x = 0'}")
    print("   两条切线各被两圆共用：切锥是坐标轴 x = 0 与 y = 0，各重数 2。")
    print()

    print("2. O 附近的二阶局部形状（y = ρ - sqrt(ρ²-x²) 的展开）")
    print(f"   C+ : y = +x²/R + x⁴/R³ + O(x⁶) = +x²/{radius:g} + x⁴/{radius ** 3:g} + ...")
    print(f"   C- : y = -x²/R - x⁴/R³ + O(x⁶)")
    print(f"   D+ : x = +y²/R + y⁴/R³ + O(y⁶)")
    print(f"   D- : x = -y²/R - y⁴/R³ + O(y⁶)")
    print("   数值核对（x 很小时，圆弧与二阶抛物线的差应为 O(x⁴)）：")
    for x in (0.4, 0.2, 0.1, 0.05):
        arc = lower_arc(x, rho, +1)
        para = x * x / radius
        print(f"     x = {x:5.3f}: 圆弧 y = {arc:.8f}，二阶抛物线 {para:.8f}，"
              f"差 {arc - para:.3e}（x⁴/R³ = {x ** 4 / radius ** 3:.3e}）")
    print()

    print("3. 相切阶")
    d_red = 2 * rho
    print(f"   同色对：圆心距 2ρ = {d_red:g}，半径和 ρ+ρ = {2 * rho:g} -> 外切于 O")
    print("   C+ 与 C- 只在 O 相交；把两者都用 x 参数化，差为")
    print(f"     2x²/R + 2x⁴/R³ + ... ，消没阶为 2 -> 二阶切触，且分别位于 x 轴两侧。")
    print("   异色对：D+ 与 C+ 的圆心距 ρ√2 = %.6f，半径和 2ρ = %g -> 两个交点"
          % (rho * math.sqrt(2), 2 * rho))
    print(f"      (0, 0) 与 (ρ, ρ) = ({rho:g}, {rho:g})；两处切线分别为 x = 0 与 y = 0，"
          "均为 90° 横截。")
    print()

    print("4. 切锥")
    print("   并集多项式 P = [(x²+y²)² - 4ρ²y²][(x²+y²)² - 4ρ²x²]")
    print("              = 16ρ⁴x²y² - 4ρ²(x²+y²)³ + (x²+y²)⁴")
    print("   最低次齐次部分为 16ρ⁴x²y²，即切锥 (xy)² = 0：两条坐标轴，各重数 2。")
    print("   数值核对  P / (16ρ⁴x²y²) -> 1：")
    for t in (0.2, 0.05, 0.01):
        for slope in (1.0, 2.0, 0.3):
            x, y = t, slope * t
            ratio = union_polynomial(x, y, rho) / (16 * rho ** 4 * x * x * y * y)
            print(f"     t = {t:5.3f}, y = {slope:>3}x: P/(16ρ⁴x²y²) = {ratio:.8f}")
    print("   切锥的两条直线夹角 90°；其角平分线为 y = ±x，正是两条配对连线。")
    print()

    print("5. 对照：a > 0 时焦点处的方向笔束")
    a = 0.6
    v_min = 2 * math.atan(a / radius)
    print(f"   a = {a:g}, R = {radius:g}: 红族每个圆都过焦点 (±a, 0)。")
    print("   第 k 个红圆在焦点 (a, 0) 处的切线方向为 (cot v, 1)，其方向角恰等于 v：")
    for k in (0, 2, 5, 8, 10):
        v = v_min + k * (math.pi - 2 * v_min) / 10
        print(f"     k = {k:2d}: v = {math.degrees(v):7.3f}° -> 切线方向角 "
              f"{math.degrees(math.atan2(1.0, 1.0 / math.tan(v))):7.3f}°")
    print("   即：焦点处红族给出扫过整个上半平面的切线笔束；a -> 0 时该笔束")
    print("   塌缩为单一的 x 轴方向，与蓝族的单一 y 轴方向合起来成为切锥 (xy)² = 0。")
    print()

    # ---------------------------------------------------------------- 作图
    fig, axes = plt.subplots(1, 2, figsize=(13, 6.5), facecolor="black")
    for ax in axes:
        ax.set_facecolor("black")
        ax.set_aspect("equal")

    ax = axes[0]
    for (cx, cy), color in (((0, rho), "#ff0000"), ((0, -rho), "#ff0000"),
                            ((rho, 0), "#0000ff"), ((-rho, 0), "#0000ff")):
        ax.add_patch(Circle((cx, cy), rho, fill=False, edgecolor=color,
                            linewidth=1.0, antialiased=True))
    w = 0.7 * rho
    xs = [i * w / 400 for i in range(-400, 401)]
    ax.plot(xs, [x * x / radius for x in xs], color="#ffaa00", linewidth=0.8,
            linestyle=(0, (4, 3)))
    ax.plot(xs, [-x * x / radius for x in xs], color="#ffaa00", linewidth=0.8,
            linestyle=(0, (4, 3)))
    ys = xs
    ax.plot([y * y / radius for y in ys], ys, color="#ffaa00", linewidth=0.8,
            linestyle=(0, (4, 3)))
    ax.plot([-y * y / radius for y in ys], ys, color="#ffaa00", linewidth=0.8,
            linestyle=(0, (4, 3)))
    for slope in (+1, -1):
        ax.plot([-w, w], [-slope * w, slope * w], color="#00ff88", linewidth=1.0,
                linestyle=(0, (6, 4)))
    ax.plot([0], [0], marker="o", markersize=4.0, color="#ffaa00")
    ax.set_xlim(-w, w)
    ax.set_ylim(-w, w)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title("ideal  a -> 0 :  neighbourhood of O\n(green: pairing lines, orange: 2nd-order parabolas)",
                 color="#dddddd", fontsize=10)

    ax = axes[1]
    for k in range(11):
        v = v_min + k * (math.pi - 2 * v_min) / 10
        cx, cy = 0.0, a / math.tan(v)
        r = a / math.sin(v)
        ax.add_patch(Circle((cx, cy), r, fill=False, edgecolor="#ff0000",
                            linewidth=0.9, antialiased=True))
        # 焦点 (a, 0) 处的切线方向为 (cot v, 1)。
        tx, ty = 1.0 / math.tan(v), 1.0
        n = math.hypot(tx, ty)
        half = 0.22
        ax.plot([a - half * tx / n, a + half * tx / n],
                [0 - half * ty / n, 0 + half * ty / n],
                color="#8888ff", linewidth=0.8)
    ax.plot([a], [0], marker="o", markersize=4.0, color="#00ff88")
    ax.set_xlim(a - 0.7, a + 0.7)
    ax.set_ylim(-0.7, 0.7)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title(f"resolved  a = {a:g} :  tangent pencil at the focus",
                 color="#dddddd", fontsize=10)

    fig.tight_layout()
    out = Path(__file__).with_name("ideal_singularity.png")
    fig.savefig(out, dpi=160, facecolor="black")
    plt.close(fig)
    print(f"图已输出: {out}")


if __name__ == "__main__":
    main()
