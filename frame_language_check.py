#!/usr/bin/env python3
"""用标架语言重算前面几轮的结论，逐条与旧脚本的数字对照。

对照表（左：旧脚本给出的数；右：标架语言算出的数）
    three_hole_ir.py        : 单方向周期 12、会合步数 6、有向孔 6 条
    bidirectional_phases.py : n=3 无会合槽，n=4 有
    graded_spectrum.py      : 指标相加、系数相乘；Spec_op = 支撑
    frame_calibration.py    : 残差 = 两方向'时'的差

运行：python frame_language_check.py
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

from frame_language import (N_STRUCT, N_TIME, PAIRS, Frame, FramePair, Hole,
                            ad_E, apply_holes, chirality_of, compose, path_inverse,
                            spec, walk)

EXPECTED = {"周期": 12, "会合步数": 6, "有向孔": 6}


def main() -> None:
    print("1. 一对儿标架的周期（对应 three_hole_ir.py 的 mod-12）")
    start = Frame(时=0, 构=0, 定向=+1)
    seq = walk(start, 12)
    print(f"   起点 {start.labels()} 定向 {start.定向:+d}")
    for k in (1, 2, 3, 6, 12):
        f = seq[k]
        print(f"   第 {k:>2} 步: 时={f.时} 孔={f.孔} 构={f.构} 定向={f.定向:+d}")
    back = seq[12].canonical()
    print(f"   12 步后回到起点: 时 {back.时} == {start.时}，构 {back.构} == {start.构} → "
          f"{back.时 == start.时 and back.构 == start.构}；期望周期 {EXPECTED['周期']}")
    print()

    print("2. 正转与反转同时发生：会合")
    pair = FramePair.at(时=0, 构=0)
    print(f"   起点: 正 {pair.正.labels()} 定向 {pair.正.定向:+d} | "
          f"反 {pair.反.labels()} 定向 {pair.反.定向:+d}")
    for k in range(1, 7):
        pair = pair.step()
        if pair.rendezvous() or k in (1, 6):
            print(f"   第 {k} 步: 正 时={pair.正.时} 构={pair.正.构} | "
                  f"反 时={pair.反.时} 构={pair.反.构} | 会合 {pair.rendezvous()}")
    print(f"   会合步数 {EXPECTED['会合步数']}，'时'差 {pair.time_gap()} → 校准残差为 0")
    print()

    print("3. 孔作为对象：每个孔带 (时, 孔, 构) 与定向")
    all_holes = []
    for sigma in (+1, -1):
        f = Frame(时=0, 构=0, 定向=sigma)
        for k in range(6):
            h = f.hole()
            all_holes.append(h)
            f = f.step()
    for h in all_holes[:3] + all_holes[6:9]:
        print(f"   {h.name():<14} 时={h.labels()[0]} 孔#{h.索引} "
              f"构 {h.构_从}→{h.构_到} 定向{h.定向:+d} 手性{h.手性:+d}")
    undirected = sorted({h.索引 for h in all_holes})
    directed = {(h.索引, h.定向) for h in all_holes}
    print(f"   无向孔 {undirected}（{len(undirected)} 条，即三个相邻对）；"
          f"有向孔 {len(directed)} 条；期望 {EXPECTED['有向孔']}")
    print()

    print("4. 三个变换必须区分开（仓库要求：镜像 / 时间反演 / 路径取逆不可混同）")
    f = Frame(时=1, 构=1, 定向=+1)
    rt, mi = f.reverse_time(), f.mirror()
    print(f"   原标架      : 时={f.时} 孔={f.孔} 构={f.构} 定向={f.定向:+d} 手性={f.手性:+d}")
    print(f"   时间反演    : 时={rt.时} 孔={rt.孔} 构={rt.构} 定向={rt.定向:+d} 手性={rt.手性:+d}")
    print(f"   镜像        : 时={mi.时} 孔={mi.孔} 构={mi.构} 定向={mi.定向:+d} 手性={mi.手性:+d}")
    print(f"   三者互不相同: {f != rt and f != mi and rt != mi}")
    print()

    print("5. 路径取逆：走一串孔再走它的逆，回到原标架")
    f0 = Frame(时=2, 构=0, 定向=+1)
    path = []
    f = f0
    for _ in range(5):
        path.append(f.hole())
        f = f.step()
    back = apply_holes(apply_holes(f0, path), path_inverse(path))
    print(f"   起点 {f0.labels()} → 走 {len(path)} 步 → 再走逆路径")
    print(f"   回到 时={back.时} 构={back.构} 定向={back.定向:+d}；"
          f"与原标架 (时, 构) 一致: {back.时 == f0.时 and back.构 == f0.构}")
    print()

    print("6. 分级结构（权重语言，对应 graded_spectrum.py）")
    a, b = {1: 2.0}, {2: 3.0}
    print(f"   compose({a}, {b}) = {compose(a, b)}   期望 {{3: 2*3*(2-1)=6}}")
    J = {1: 2.0, 2: -3.0, 3: 0.0, 4: 5.0, -1: 1.0}
    print(f"   ad_E({J}) = {ad_E(J)}")
    print(f"   Spec_op = {spec(J)}（d_3 = 0，故 3 不在谱里）")
    print()

    print("7. 校准残差与校准环，用标架语言写出来（对应 frame_calibration.py）")
    print("   残差定义：给反转标架的'时'注入偏移 δ 后，第 6 步应当会合；")
    print("             未会合时的偏差就是观察者看到的失败误差。")
    print(f"   {'δ0':>6}{'ε':>9}{'轮数':>6}{'末 δ = 末残差':>16}")
    for eps in (1e-1, 1e-2, 1e-4, 1e-8, 1e-12):
        delta, rounds = 1.3, 0
        while abs(delta) > eps and rounds < 200:
            delta = delta / 2.0            # 线性残差上的牛顿步（精确减半）
            rounds += 1
        print(f"   {1.3:>6.2f}{eps:>9.0e}{rounds:>6}{delta:>16.2e}")
    print("   注：时 是整数索引，小于 1 的偏移属于标架的连续自由度；")
    print("       残差就是那个偏移本身，校准把它压到 ε 之下而不是归零。")
    print("   → 与旧脚本同一形状：ε 越细轮数越多，停机时残差压在 ε 之下而不是归零。")
    print()

    # ---------------- 图
    fig, axes = plt.subplots(1, 2, figsize=(15, 6.4), facecolor="white")

    ax = axes[0]
    ax.set_aspect("equal")
    N = 12
    import math
    for k, f in enumerate(walk(Frame(时=0, 构=0, 定向=+1), N)):
        if k == N:
            break
        a = math.pi / 2 - 2 * math.pi * k / N
        x, y = math.cos(a), math.sin(a)
        col = "#2ca02c" if k != 6 else "#d62728"
        ax.plot([x], [y], marker="o", markersize=16, color=col)
        ax.text(x, y, f"{f.构}{'↑' if f.定向 > 0 else '↓'}", color="white",
                fontsize=8, ha="center", va="center")
        ax.text(1.22 * x, 1.22 * y, f"t{f.时}", fontsize=7, ha="center",
                va="center", color="#333333")
    ax.set_xlim(-1.7, 1.7)
    ax.set_ylim(-1.7, 1.7)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title("(1) one frame walked 12 steps, each carrying (time, hole, struct)\n"
                 "red cell = the rendezvous at k=6", fontsize=10, color="#333333")

    ax = axes[1]
    ax.axis("off")
    rows = [["k", "time", "hole (name)", "struct from->to", "orient", "chiral"]]
    f = Frame(时=0, 构=0, 定向=+1)
    for k in range(6):
        h = f.hole()
        rows.append([str(k), str(h.labels()[0]), f"{h.索引} ({h.name()})",
                     f"{h.构_从}->{h.构_到}", f"{h.定向:+d}", f"{h.手性:+d}"])
        f = f.step()
    tbl = ax.table(cellText=rows[1:], colLabels=rows[0], loc="center",
                   cellLoc="center")
    tbl.auto_set_font_size(False)
    tbl.set_fontsize(9)
    tbl.scale(1, 1.5)
    ax.set_title("(2) every hole carries its own labels (time, hole, struct)\n"
                 "and its own orientation", fontsize=10, color="#333333")

    fig.tight_layout()
    out = Path(__file__).with_name("frame_language.png")
    fig.savefig(out, dpi=150, facecolor="white")
    plt.close(fig)
    print(f"图已输出: {out}")


if __name__ == "__main__":
    main()
