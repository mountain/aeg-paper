#!/usr/bin/env python3
"""把三计算上流动的形态，固定成三孔算术 IR 的静态表征。

流动（动态）：
    状态 = (计算机 c ∈ {Rust,Python,Ada} = Z_3, 方向 σ ∈ {+1,-1}, 相位 φ ∈ Z_n)
    一步 = (c, σ, φ) → (c + σ mod 3, σ, φ + σ mod n)
其中正转是 c→c+1（R→P→A→R），反转是 c→c-1（R→A→P→R）。

静态 IR：
    流动是确定性、单调的，所以把轨道商下来就是 IR。
    关键：c 的周期是 3，φ 的周期是 4，二者互素 ⇒ 由中国剩余定理，
    (c, φ) 与单个计数器 k ∈ Z_12 一一对应。于是

        IR = 每个方向一个 mod-12 计数器，加上 (k mod 3, k mod 4) 的解码。

    流动在 IR 上只剩下 ±1；IR 本身是静态表。

本程序核验：
  1. 静态化何时可能：相位角是单位根时轨道闭合、IR 有限；无理角时永不闭合；
  2. n = 4（90°）时的轨道长度、IR 规模、会合槽位置；
  3. CRT 等价（(c,φ) ↔ k mod 12）与 IR 对流动的模拟等价（长程核验）；
  4. 会合：两个方向各走 6 步后在同一个 (计算机, 相位) 上相遇；
  5. 三个孔在 IR 里的位置：3 个相邻对 × 2 个方向 = 6 条有向转移；
  6. 工程隐患：把相位与计算机合并成一个模 3 索引会立刻出错。
"""

import math
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

NAMES = {0: "Rust", 1: "Python", 2: "Ada"}
NC, NPH = 3, 4


def step(state, n_ph=NPH):
    c, sigma, phi = state
    return ((c + sigma) % NC, sigma, (phi + sigma) % n_ph)


def orbit(start, limit=10000):
    seen, order, s = {}, [], start
    while s not in seen and len(order) < limit:
        seen[s] = len(order)
        order.append(s)
        s = step(s)
    return order, (s == start)


def main() -> None:
    print("1. 静态化何时可能：轨道闭合性")
    print(f"   {'相位角':>9}{'n':>4}{'单方向轨道长度':>16}{'闭合?':>8}   IR")
    for n in (3, 4, 5, 6, 8):
        order, closed = orbit((0, +1, 0)) if n == NPH else orbit((0, +1, 0), limit=10 ** 6)
        # 对一般 n 重新算（相位模 n）
        seen, s, cnt = set(), (0, +1, 0), 0
        while s not in seen and cnt < 10 ** 6:
            seen.add(s)
            s = ((s[0] + s[1]) % NC, s[1], (s[2] + s[1]) % n)
            cnt += 1
        closed = (s in seen) and s == (0, +1, 0)
        size = cnt if closed else None
        print(f"   {360.0 / n:>8.1f}°{n:>4}{cnt:>16}{str(closed):>8}   "
              f"{'有限（' + str(size) + ' 格/方向）' if closed else '无限'}")
    # 无理角：相位永不重复
    theta = 2 * math.pi / math.sqrt(2)
    ph = 0.0
    seen = set()
    for _ in range(2000):
        ph = (ph + theta) % (2 * math.pi)
        seen.add(round(ph, 9))
    print(f"   无理角 θ/2π ∉ Q: 2000 步内不同相位 {len(seen)} 个（线性增长）→ 永不闭合，"
          f"不存在有限静态 IR")
    print()

    fwd, closed_f = orbit((0, +1, 0))
    bwd, closed_b = orbit((0, -1, 0))
    print("2. n = 4（90°）的 IR")
    print(f"   单方向轨道长度 = lcm(3, 4) = {len(fwd)}；正转闭合 {closed_f}，反转闭合 {closed_b}")
    print(f"   IR 规模 = 12 + 12 = {len(fwd) + len(bwd)} 格")
    print("   解码表 (k → 计算机, 相位)：")
    for k, (c, _s, phi) in enumerate(fwd):
        mark = "  ← 会合" if k == 6 else ""
        print(f"     k={k:>2}  {NAMES[c]:<7} φ={phi}{mark}")
    print()

    print("3. CRT 等价与模拟等价")
    ok_crt = all(
        (k % NC) == fwd[k][0] and (k % NPH) == fwd[k][2] for k in range(12))
    print(f"   (k mod 3, k mod 4) 与轨道上的 (计算机, 相位) 逐格一致: {ok_crt}"
          f"  （gcd(3,4)=1）")
    s, ok = (0, +1, 0), True
    for t in range(1000):
        if fwd[t % 12] != s:
            ok = False
            break
        s = step(s)
    print(f"   用“mod-12 计数器 + 解码表”重放 1000 步与逐步推进一致: {ok}")
    print()

    print("4. 会合")
    s_plus, s_minus = (0, +1, 0), (0, -1, 0)
    for _ in range(6):
        s_plus, s_minus = step(s_plus), step(s_minus)
    print(f"   正转走 6 步 → ({NAMES[s_plus[0]]}, φ={s_plus[2]}, +)")
    print(f"   反转走 6 步 → ({NAMES[s_minus[0]]}, φ={s_minus[2]}, -)")
    print(f"   同一计算机、同一相位（φ = n/2 = 对面相位），只差方向: "
          f"{s_plus[0] == s_minus[0] and s_plus[2] == s_minus[2]}")
    print(f"   6 = lcm(3,4)/2：两个方向各走半圈就回到出发的那台计算机上相遇。")
    print()

    print("5. 三个孔在 IR 里的位置")
    pairs = [("Rust", "Python"), ("Python", "Ada"), ("Ada", "Rust")]
    print("   相邻对（无向孔）: " + "、".join(f"{a}–{b}" for a, b in pairs))
    print("   有向转移（孔在 IR 里的实际形态）: 3 对 × 2 方向 = 6 条")
    for c in range(NC):
        print(f"     {NAMES[c]} → {NAMES[(c + 1) % NC]}   正转，孔 {NAMES[c]}–{NAMES[(c + 1) % NC]}")
    for c in range(NC):
        print(f"     {NAMES[c]} → {NAMES[(c - 1) % NC]}   反转，孔 {NAMES[c]}–{NAMES[(c - 1) % NC]}")
    cnt = {}
    for k in range(12):
        c = fwd[k][0]
        cnt[(c, (c + 1) % NC)] = cnt.get((c, (c + 1) % NC), 0) + 1
    print(f"   mod-12 一圈里每条有向孔出现 {set(cnt.values())} 次"
          f"（12 格 = 3 对 × 4 圈相位）")
    print("   → 孔 = 权重 ±1 的转移；填孔 = 括号里系数相乘，分级支撑不变。")
    print()

    print("6. 工程隐患：只保留计算机索引（丢掉相位维）")
    groups = {}
    for k, (c, _s, phi) in enumerate(fwd):
        groups.setdefault(c, []).append((k, phi))
    for c, items in sorted(groups.items()):
        print(f"   {NAMES[c]}: " + ", ".join(f"k={k}(φ={phi})" for k, phi in items)
              + f"   → 被并成同一状态（{len(items)} 合 1）")
    print(f"   压缩比: 每方向 12 格 → 3 格；两个方向合计 24 → 6")
    print("   后果：k=6（Rust, φ=2，会合）与 k=0/3/9（同为 Rust）无法区分，")
    print("         会合与填孔的时机在 IR 里就丢了；这正是必须同时携带两个模数的原因。")
    print()

    # ---------------- 图
    fig, axes = plt.subplots(1, 2, figsize=(15, 7), facecolor="white")
    for ax in axes:
        ax.set_facecolor("white")

    ax = axes[0]
    ax.set_aspect("equal")
    for idx, (orbit_list, R, col) in enumerate(((fwd, 0.92, "#2ca02c"),
                                                (bwd, 0.60, "#ff7f0e"))):
        for k, (c, _s, phi) in enumerate(orbit_list):
            a = math.pi / 2 - 2 * math.pi * k / 12
            x, y = R * math.cos(a), R * math.sin(a)
            ax.plot([x], [y], marker="o", markersize=13, color=col)
            ax.text(x, y, f"{NAMES[c][0]}", color="white", fontsize=8,
                    ha="center", va="center")
            if k == 6:
                ax.text(x * 1.20, y * 1.20, f"k=6\nφ={phi}", fontsize=8,
                        ha="center", va="center", color="#d62728")
    ax.plot([0], [0], marker="x", color="#333333")
    ax.text(0, -0.06, "IR:\nmod-12 counter\nper direction", ha="center", va="top",
            fontsize=9, color="#333333")
    ax.set_xlim(-1.45, 1.45)
    ax.set_ylim(-1.45, 1.45)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title("(1) each direction is a 12-cell cycle  (lcm(3,4)=12)\n"
                 "outer = forward, inner = reverse; k=6 is where they meet",
                 fontsize=10, color="#333333")

    ax = axes[1]
    ax.set_xlim(-0.5, 12.5)
    ax.set_ylim(-1.2, 4.4)
    ax.set_xticks([])
    ax.set_yticks([])
    for k, (c, _s, phi) in enumerate(fwd):
        ax.add_patch(plt.Rectangle((k + 0.08, 2.4), 0.84, 0.6,
                                   facecolor="#2ca02c", alpha=0.22,
                                   edgecolor="#2ca02c"))
        ax.text(k + 0.5, 2.7, NAMES[c], ha="center", va="center", fontsize=8,
                color="#111111")
        ax.text(k + 0.5, 3.16, f"φ={phi}", ha="center", va="center", fontsize=7,
                color="#333333")
        ax.text(k + 0.5, 3.62, f"k={k}", ha="center", va="center", fontsize=7,
                color="#666666")
        nxt = (c + 1) % NC
        ax.add_patch(plt.Rectangle((k + 0.08, 1.2), 0.84, 0.6,
                                   facecolor="#ff7f0e", alpha=0.18,
                                   edgecolor="#ff7f0e"))
        ax.text(k + 0.5, 1.5, f"{NAMES[c][0]}→{NAMES[nxt][0]}", ha="center",
                va="center", fontsize=8, color="#111111")
    ax.add_patch(plt.Rectangle((6.02, 1.14), 0.96, 2.92, fill=False,
                               edgecolor="#d62728", linewidth=1.8))
    ax.text(6.5, 0.75, "rendezvous (k=6, φ=2):\nforward and reverse arrive together",
            ha="center", fontsize=9, color="#d62728")
    ax.text(6, 4.15, "top row: static decode table (k → computer, phase)\n"
                     "bottom row: the six directed hole transitions",
            ha="center", fontsize=9, color="#333333")
    ax.set_title("(2) the three-hole arithmetic IR", fontsize=10, color="#333333")

    fig.tight_layout()
    out = Path(__file__).with_name("three_hole_ir.png")
    fig.savefig(out, dpi=150, facecolor="white")
    plt.close(fig)
    print(f"图已输出: {out}")


if __name__ == "__main__":
    main()
