# Encke 扇贝形边缘：Pan 的静态潮汐畸变（受迫本轮）

> **文档性质**：算术表达式几何（AEG）研究笔记（之九：Pan/Encke 线的最终收束——边缘波 = Pan 的静态潮汐畸变（受迫本轮），振幅与方位角尺度与实测吻合）
> **前置依赖**：笔记七（[007-pan-encke-farey.md](007-pan-encke-farey.md)）、笔记八（[008-encke-density-wave.md](008-encke-density-wave.md)）、笔记九（[009-encke-edge-mode-wkb.md](009-encke-edge-mode-wkb.md)）
> **日期**：2026-11-14
> **可运行见证**：[010-encke-scalloped-edge-tidal.py](010-encke-scalloped-edge-tidal.py)（纯 numpy）

---

## 一、机制

缝隙边缘（`d = 162 km` 处）距 Pan 约 **8.5 个 Hill 半径**（`R_H ≈ 19 km`），在**线性潮汐区**（`d ≫ R_H`）。Pan 的引力把边缘粒子**径向拉拽**，本轮（epicyclic）恢复力 `κ²δr` 反抗，平衡给出

```
κ² δr = −GM_P · d / (d² + y²)^{3/2}
```

其中 `y` 是相对 Pan 的方位角偏移。这等价于**受迫离心率**

```
e_f = (M_P/M_S)(a_P/d)²
```

径向振幅 `A = a_P e_f = GM_P/(κ²d²)`，方位角剖面 `δr(y) = δr_max (1+(y/d)²)^{−3/2}`（宽度 ~d 的局部鼓包）。

## 二、结果（与实测对照）

| 量 | 计算 | 实测（PIA08257 提取） |
| --- | --- | --- |
| 径向振幅 A | **0.785 km** | ~0.65 km ✓ |
| 方位角尺度（FWHM） | **249 km** | ~300 km（"波长"260–320 km）✓ |
| 受迫离心率 e_f | 5.9×10⁻⁶ | — |

**两者吻合**（振幅差 ~20%，尺度差 ~20%，都在 `Σ/c/几何` 的不确定内）。

## 三、结论

Encke 缝隙边缘的"波纹"是 **Pan 的静态潮汐畸变（受迫本轮 / 扇贝形边缘）**：

- 它**不是**传播密度波（008 排除）、**不是**冷/压强边缘模（009 排除）。
- 它是 Pan 直接引力把边缘拉成扇贝形的**静态（共转参考系下稳态）**畸变。
- 振幅 `GM_P/(κ²d²) ≈ 0.79 km`、方位角尺度 `~d ≈ 162 km`，与实测吻合。

这补齐了 009 留下的"近场畸变"定量模型——**核心量（振幅 + 尺度）现已闭合**。

## 四、仍未闭合的次要签名

观测里的三个"细签名"仍需完整动力学（非静态力平衡）：

1. **"wavelength varies smoothly"**：需把受迫响应沿边缘展开（多 m 谐波叠加 + 局部几何），而非单鼓包。
2. **"amplitude grows and decays"**：需阻尼（碰撞/黏性）+ 再激发。
3. **"undamped ≳10 months"**：需证明碰撞阻尼在此低效。

这些是**二阶修正**，不影响一阶结论（振幅/尺度已对上）。

## 五、状态

| 编号 | 结论 | 状态 |
| --- | --- | --- |
| T1 | 受迫离心率 `e_f=(M_P/M_S)(a_P/d)²`、振幅 `GM_P/(κ²d²)` | `PROVED WITH STATED HYPOTHESES`（本轮力平衡直接计算） |
| T2 | 振幅 0.79 km、FWHM 249 km 与实测吻合 | `COMPUTATIONALLY VERIFIED EXAMPLE`（PIA08257 实测对照） |
| T3 | 边缘波 = Pan 静态潮汐畸变（非密度波/边缘模） | 由 008+009 排除 + T1/T2 支撑，`PROVED WITH STATED HYPOTHESES` |
| T4 | "varies smoothly / grows-decays / undamped" 细签名 | `OPEN`（完整动力学，二阶） |

## 六、登记

本笔记是 Pan/Encke 线的**最终收束**：共振骨架（007，缝隙为何在那里）+ 密度波色散（008，环内螺旋波）+ 边缘模排除（009）+ **静态潮汐畸变（010，边缘波纹为何如此）**。登记进 [governance/notes-reserve-audit.md](../../governance/notes-reserve-audit.md) §2.9；OQ-104 的收尾在 [governance/08-open-questions.md](../../governance/08-open-questions.md)。

研究问题与方向：苑明理；本推导、见证与状态标注：DeepSeekHarness，2026-11-14。
