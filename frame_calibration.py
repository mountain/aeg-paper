#!/usr/bin/env python3
"""标架校准环：从失败的误差反复学习，直到残差小于可观察者的分辨率。

标架（frame）：本轮的待校准量取
    θ      —— 每次跨界相位的推进量（理想值 π/2 = 90°）
    δ_i    —— 第 i 条边界上的标架偏置（i = 1,2,3，理想值 0）

两侧的导数：
    三计算侧（流动）  ：残差由“依次穿越四条边界”的相位复合给出，
                        只能靠模拟 + 差商得到导数；
    三孔表达式几何侧  ：残差有闭式，导数解析可得。
    两者必须一致 —— 这是“两侧都有导数”的可检查形式。

失败驱动的学习：
    可观察者只看得见 |残差| ≥ ε 的失败事件。每一轮用这些失败事件的
    残差做一步阻尼 Gauss–Newton；当没有任何残差超过 ε 时停机 ——
    此时标架已经校准到“观察者分辨不出来”的程度（而不是误差为零）。
"""

import cmath
import math
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

THETA_STAR = math.pi / 2          # 理想推进：90°
ETA = 0.4                         # 阻尼（学习率）


# ---------------------------------------------------------------- 流动侧
def flow_residuals(theta, deltas):
    """模拟穿越：正转四条边、反转四条边，取复合后的偏差。

    正转第 i 条边推进 θ + δ_i，反转第 i 条边推进 −θ + δ_i。
    会合要求正反相消；闭合要求四条边走完回到原相位。
    """
    z = 1 + 0j
    for i in range(3):                       # 正转穿过三条边
        z *= cmath.exp(1j * (theta + deltas[i]))
    z *= cmath.exp(1j * theta)               # 第 4 次穿越：会合槽（参考边界，δ 定为 0）
    closure = abs(z - 1.0)                   # 四条边走完回到原相位的偏差
    joints = []
    for i in range(3):                       # 每条边上正反相消的偏差
        w = cmath.exp(1j * (theta + deltas[i])) * cmath.exp(1j * (-theta + deltas[i]))
        joints.append(abs(w - 1.0))
    return np.array(joints + [closure])


# ------------------------------------------------------- 表达式几何侧（闭式）
def geom_residuals(theta, deltas):
    """闭式残差：会合项 2|sin δ_i|，闭合项 2|sin(2θ + Σδ/2)|。"""
    r = [abs(2 * math.sin(d)) for d in deltas]
    r.append(abs(2 * math.sin(2 * theta + sum(deltas) / 2)))
    return np.array(r)


def geom_jacobian(theta, deltas):
    """闭式残差的解析 Jacobian（对角 + 一个 θ 列）。"""
    J = np.zeros((4, 4))                     # 参数顺序 [θ, δ1, δ2, δ3]
    for i in range(3):
        J[i, i + 1] = 2 * math.cos(deltas[i]) * (1 if math.sin(deltas[i]) >= 0 else -1)
    u = 2 * theta + sum(deltas) / 2
    sgn = 1 if math.sin(u) >= 0 else -1
    J[3, 0] = 4 * math.cos(u) * sgn
    for i in range(3):
        J[3, i + 1] = math.cos(u) * sgn
    return J


def flow_jacobian(theta, deltas, h=1e-7):
    """流动侧 Jacobian：只能靠差商。"""
    J = np.zeros((4, 4))
    base = flow_residuals(theta, deltas)
    for k in range(4):
        p = [theta, *deltas]
        p[k] += h
        J[:, k] = (flow_residuals(p[0], p[1:]) - base) / h
    return J


def calibrate(eps, theta0=1.15, deltas0=(0.30, -0.20, 0.42), max_iter=200):
    """失败驱动的阻尼 Gauss–Newton。返回 (参数, 历史, 失败事件数历史)。"""
    theta, deltas = theta0, list(deltas0)
    hist_res, hist_fail = [], []
    for _ in range(max_iter):
        r = geom_residuals(theta, deltas)
        hist_res.append(float(np.linalg.norm(r, ord=np.inf)))
        fails = np.abs(r) >= eps
        hist_fail.append(int(fails.sum()))
        if not fails.any():                  # 观察者看不到任何失败 → 停机
            break
        J = geom_jacobian(theta, deltas)
        Jf, rf = J[fails], r[fails]
        step = np.linalg.lstsq(Jf.T @ Jf + 1e-12 * np.eye(4), Jf.T @ rf, rcond=None)[0]
        p = np.array([theta, *deltas]) - ETA * step
        theta, deltas = p[0], list(p[1:])
    return (theta, deltas), hist_res, hist_fail


def main() -> None:
    print("0. 两侧导数一致性核验（流动＝模拟+差商；几何＝闭式解析）")
    theta, deltas = 1.15, [0.30, -0.20, 0.42]
    Jf, Jg = flow_jacobian(theta, deltas), geom_jacobian(theta, deltas)
    print("   流动侧 Jacobian:")
    print("   " + np.array2string(Jf, precision=4).replace("\n", "\n   "))
    print("   几何侧 Jacobian:")
    print("   " + np.array2string(Jg, precision=4).replace("\n", "\n   "))
    print(f"   最大差异 {np.abs(Jf - Jg).max():.2e} → 两侧导数一致")
    print()

    print("1. 残差定义（理想标架 θ = π/2, δ = 0 时为零）")
    for th, dd in ((math.pi / 2, [0, 0, 0]), (1.15, [0.30, -0.20, 0.42])):
        r = geom_residuals(th, dd)
        print(f"   θ={th:.4f}, δ={dd} → 残差 {np.round(r, 6)}，∞-范数 {np.abs(r).max():.6f}")
    print()

    print("2. 失败驱动校准：不同观察者分辨率 ε 下的结果")
    print(f"   {'ε':>8}{'迭代':>6}{'最终 θ':>12}{'θ−π/2':>12}"
          f"{'|δ|max':>10}{'末残差':>12}{'失败事件总数':>14}")
    for eps in (1e-1, 3e-2, 1e-2, 1e-3, 1e-5, 1e-8, 1e-12):
        (th, dd), res, fails = calibrate(eps)
        print(f"   {eps:>8.0e}{len(res):>6}{th:>12.8f}{th - THETA_STAR:>12.2e}"
              f"{max(abs(x) for x in dd):>10.2e}{res[-1]:>12.2e}{sum(fails):>14}")
    print("   → ε 越细，迭代越多、标架越准；ε 粗时早早停机，因为再精确观察者也分辨不出。")
    print()

    print("3. 典型一轮的失败信号衰减（ε = 1e-6）")
    (th, dd), res, fails = calibrate(1e-6)
    for k, (r, f) in enumerate(zip(res, fails)):
        print(f"   第 {k:>2} 轮: 残差 {r:.3e}，失败事件 {f} 个")
    print(f"   停机标架: θ = {th:.10f}（π/2 = {THETA_STAR:.10f}），"
          f"δ = {[round(x, 12) for x in dd]}")
    print()

    # ---------------- 图
    fig, axes = plt.subplots(1, 2, figsize=(15, 6.2), facecolor="white")

    ax = axes[0]
    for eps, col in ((1e-2, "#1f77b4"), (1e-6, "#2ca02c"), (1e-12, "#d62728")):
        _, res, _ = calibrate(eps)
        ax.semilogy(range(len(res)), res, marker="o", markersize=4, color=col,
                    label=f"eps = {eps:g}")
        ax.axhline(eps, color=col, linewidth=0.8, linestyle=(0, (4, 3)))
    ax.set_xlabel("learning round")
    ax.set_ylabel("residual (inf-norm)")
    ax.set_title("(1) failure-driven calibration\n"
                 "each round uses only the events above the observer's threshold;\n"
                 "the loop stops when nothing is observable any more",
                 fontsize=10, color="#333333")
    ax.legend(fontsize=9, frameon=False)

    ax = axes[1]
    eps = 1e-6
    theta, deltas = 1.15, [0.30, -0.20, 0.42]
    traj = [(theta, sum(deltas) / 3)]
    for _ in range(200):
        r = geom_residuals(theta, deltas)
        if not (np.abs(r) >= eps).any():
            break
        J = geom_jacobian(theta, deltas)
        Jf, rf = J, r
        step = np.linalg.lstsq(Jf.T @ Jf + 1e-12 * np.eye(4), Jf.T @ rf, rcond=None)[0]
        p = np.array([theta, *deltas]) - ETA * step
        theta, deltas = p[0], list(p[1:])
        traj.append((theta, sum(deltas) / 3))
    for eps_band, col in ((1e-1, "#9999ff"), (2e-2, "#66cc66")):
        db = math.asin(min(1.0, eps_band / 2))          # |2 sin δ| < ε
        tb = math.asin(min(1.0, eps_band / 2)) / 2      # |2 sin(2θ)| < ε
        ax.axhspan(-db, db, color=col, alpha=0.25,
                   label=f"observer box eps={eps_band:g}")
        ax.axvspan(THETA_STAR - tb, THETA_STAR + tb, color=col, alpha=0.25)
    ax.plot([THETA_STAR], [0], marker="*", markersize=16, color="#d62728",
            label="ideal frame (pi/2, 0)")
    ax.plot([p[0] for p in traj], [p[1] for p in traj], marker="o", markersize=5,
            color="#1f77b4", linewidth=1.6, label="calibration path")
    ax.set_xlim(1.0, 1.75)
    ax.set_ylim(-0.45, 0.45)
    ax.set_xlabel("theta")
    ax.set_ylabel("mean delta")
    ax.set_title("(2) the frame converges into the observer's band\n"
                 "the star is the ideal frame; the bands are what an observer\n"
                 "with resolution eps cannot distinguish",
                 fontsize=10, color="#333333")
    ax.legend(fontsize=8, frameon=False, loc="lower left")

    fig.tight_layout()
    out = Path(__file__).with_name("frame_calibration.png")
    fig.savefig(out, dpi=150, facecolor="white")
    plt.close(fig)
    print(f"图已输出: {out}")


if __name__ == "__main__":
    main()
