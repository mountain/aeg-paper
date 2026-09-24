#!/usr/bin/env python3
"""双向 90° 相位结构：正转与反转同时发生时的衔接条件。

用户给出的结构（这里做精确化）：
  * 相位是 90° 的四分之一转；正转 = 乘 i，反转 = 乘 i^{-1}；
  * 三台计算机占三个相位，第四个相位是两个方向相遇的地方；
  * term_rust^+ 跨一个 90° 相位到 Python 的同时，
    term_rust^- 跨一个 90° 相位到 Ada —— 两者互为反方向的一步；
  * 声称：term_python^- 的每一个词汇，与 term_rust^- → term_ada^- 的谱有直接相等关系。

本程序核验四件事：
  1. 相遇相位：几个相位下，正转与反转能在“非计算机”的相位上相遇？为什么是 90°；
  2. 闭合：四分之一转的四次幂 = 1；
  3. 谱对偶：边算子的谱 = 对面顶点的词汇（需要什么前提，什么时候失效）；
  4. 与上一轮“三片叠压”结果的同一性：每个相位上恰好三片在场，缺席的正是对面那片。
"""

import cmath
import math
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle

COMPUTERS = ["Rust", "Python", "Ada"]


def meeting_scan(phases_list):
    """给定相位个数 n，找正转 k 步与反转 m 步相遇（k+m ≡ 0 mod n）的所有情形。

    计算机固定在相位 0、+1、-1（即 0、1、n-1）。
    """
    out = []
    for n in phases_list:
        verts = {0, 1, n - 1}
        meets = []
        for k in range(1, n):
            for m in range(1, n):
                if (k + m) % n == 0:
                    ph = k % n
                    meets.append((k, m, ph, ph in verts, k == m, ph * 2 == n))
        # 最短的一次相遇（k+m 最小）
        first = min(meets, key=lambda t: (t[0] + t[1], abs(t[0] - t[1])))
        out.append((n, 360.0 / n, first, meets))
    return out


def main() -> None:
    print("1. 相遇相位扫描（三台计算机固定在相位 0、+1、-1）")
    print(f"   {'相位数':>5}{'每步':>8}   {'最短相遇 (k,m,相位)':<22}{'在计算机上?':<12}{'平衡?':<8}{'对面?':<8} 非计算机相遇相位")
    for n, ang, first, meets in meeting_scan([3, 4, 5, 6, 7, 8]):
        k, m, ph, on_v, bal, anti = first
        extra = sorted({t[2] for t in meets if not t[3]})
        print(f"   {n:>5}{ang:>7.1f}°   {f'({k},{m},{ph})':<22}{str(on_v):<12}"
              f"{str(bal):<8}{str(anti):<8} {extra if extra else '（没有）'}")
    print("   → 3 台计算机至少需要 3 个相位；而 3 个相位时两个方向只能在计算机相位上相遇，")
    print("     没有多余的会合点。相位数 4（90°）是最小的情形：出现一个专门的会合相位，")
    print("     且它同时是平衡相遇（k=m）与对面相位（φ=n/2）——90° 之所以是理想值就在这里。")
    print()

    print("2. 闭合：四分之一转的四次幂")
    z = 1 + 0j
    for k in range(5):
        print(f"   i^{k} = {z.real:+.0f}{z.imag:+.0f}j")
        z *= 1j
    print("   → i⁴ = 1：正转四步回到原处，反转四步同样；90° 是让两个方向各自整圈闭合的角度。")
    print()

    print("3. 谱对偶：边算子的谱 = 对面顶点的词汇")
    print("   模型：每台计算机的词汇按相位分级，第 φ 级词 w_φ；跨边界算子 = 相位平移 ±1。")
    n = 4
    shift = np.zeros((n, n), dtype=complex)
    for phi in range(n):
        shift[phi][(phi + 1) % n] = 1.0          # 正转一步
    inv = np.linalg.inv(shift)                   # 反转一步
    for name, T in (("正转 T+", shift), ("反转 T-", inv)):
        spec = sorted(np.linalg.eigvals(T), key=lambda w: (round(w.real, 6), round(w.imag, 6)))
        print(f"   {name} 的谱: " + ", ".join(f"{w.real:+.0f}{w.imag:+.0f}j" for w in spec))
    print("   → 两个方向的谱都是 {1, i, -1, -i}，正好是四个相位类；")
    print("     因此“对面那条边的谱 = 这个顶点的词汇（相位类）”成立，前提是：")
    print("     (a) 每个词汇都带相位分级；(b) 三家词汇的相位类数相同。")
    print()
    print("   反例：三家词汇规模不齐时对偶立刻失效（边谱恒有 4 个相位类）：")
    for sizes in [(4, 4, 4), (4, 4, 3), (6, 4, 4), (4, 5, 4)]:
        detail = ", ".join(f"{c}:{k}" for c, k in zip(COMPUTERS, sizes))
        ok = all(k == n for k in sizes)
        print(f"     ({detail}) → {'对偶成立' if ok else '对偶不成立（存在词汇数 ≠ 相位类数的顶点）'}")
    print("   → 双向谱对偶等价于一条硬约束：三家在相位层面的词汇必须等量（各 4 类）。")
    print()

    print("4. 与上一轮“三片叠压”是同一件事")
    SECTORS = {1: (-45, 45), 2: (45, 135), 3: (135, 225), 4: (225, 315)}
    SHEETS = {j: tuple(sorted({j, (j % 4) + 1, ((j - 2) % 4) + 1})) for j in (1, 2, 3, 4)}
    for j in (1, 2, 3, 4):
        missing = ({1, 2, 3, 4} - set(SHEETS[j])).pop()
        print(f"   相位 S{j}: 在场 {sorted(SHEETS[j])}，缺席 {missing} "
              f"= 对面相位 {(j + 1) % 4 + 1}")
    print("   → 每个相位上恰好三片在场、缺席的正是对面那片：这正是“两个方向在对面相位相遇”")
    print("     的覆盖说法。上一轮把它读成 Z₄ 扭转，这里读成相位推进本身，两者是同一件事。")
    print()

    # ---------------- 图
    fig, axes = plt.subplots(1, 2, figsize=(14, 7), facecolor="white")
    for ax in axes:
        ax.set_facecolor("white")
        ax.set_aspect("equal")
        ax.set_xticks([])
        ax.set_yticks([])

    ax = axes[0]
    R = 1.0
    phases = [cmath.exp(1j * math.pi / 2 * k) for k in range(4)]
    labels = ["Rust (phi=0)", "Python (phi=+1)", "meeting (phi=+2)", "Ada (phi=-1)"]
    for k, (p, lab) in enumerate(zip(phases, labels)):
        col = "#1f77b4" if k in (0, 1, 3) else "#d62728"
        ax.plot([p.real], [p.imag], marker="o", markersize=14, color=col)
        ax.text(p.real * 1.22, p.imag * 1.22, lab, fontsize=10, ha="center",
                va="center", color=col)
    for sgn, col, lab in ((+1, "#2ca02c", "forward +90 deg"), (-1, "#ff7f0e", "reverse -90 deg")):
        for k in range(4):
            a0, a1 = phases[k], phases[(k + sgn) % 4]
            ax.annotate("", xy=(a1.real * 0.92, a1.imag * 0.92),
                        xytext=(a0.real * 0.92, a0.imag * 0.92),
                        arrowprops=dict(arrowstyle="->", color=col, linewidth=1.6,
                                        connectionstyle="arc3,rad=0.28"))
        ax.plot([], [], color=col, linewidth=1.6, label=lab)
    ax.add_patch(Circle((0, 0), 1.0, fill=False, edgecolor="#cccccc", linewidth=1.0))
    ax.set_xlim(-1.6, 1.6)
    ax.set_ylim(-1.6, 1.6)
    ax.legend(loc="lower left", fontsize=9, frameon=False)
    ax.set_title("(1) four 90-degree phases: three computers + one meeting phase\n"
                 "forward R->P and reverse R->A cross one quarter turn each,\n"
                 "and both arrive at the antipodal phase", fontsize=10, color="#333333")

    ax = axes[1]
    ax.plot([0], [0], marker="o", markersize=6, color="#d62728")
    for k in range(4):
        a = math.pi / 2 * k
        ax.annotate("", xy=(math.cos(a) * 0.95, math.sin(a) * 0.95), xytext=(0, 0),
                    arrowprops=dict(arrowstyle="->", color="#1f77b4", linewidth=1.4))
        ax.text(1.05 * math.cos(a), 1.05 * math.sin(a), f"φ={k}", fontsize=10,
                ha="center", va="center", color="#1f77b4")
        ax.text(0.45 * math.cos(a + math.pi / 4), 0.45 * math.sin(a + math.pi / 4),
                ["spec 1", "spec i", "spec -1", "spec -i"][k], fontsize=9, color="#333333")
    ax.set_xlim(-1.4, 1.4)
    ax.set_ylim(-1.4, 1.4)
    ax.set_title("(2) the crossing operator's spectrum is the four phase classes\n"
                 "so the spectrum of the opposite edge grades the vertex vocabulary;\n"
                 "this forces the three vocabularies to be equal in size",
                 fontsize=10, color="#333333")

    fig.tight_layout()
    out = Path(__file__).with_name("bidirectional_phases.png")
    fig.savefig(out, dpi=150, facecolor="white")
    plt.close(fig)
    print(f"图已输出: {out}")


if __name__ == "__main__":
    main()
