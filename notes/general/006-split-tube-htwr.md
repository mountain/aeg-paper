# Split-tube 的 HTWR 分解：VdP C11 的"主导线 + 扇出辅助导线"（OQ-103.4）

> **文档性质**：算术表达式几何（AEG）研究笔记（之五：OQ-103.4——把 VdP C11 的 split-tube 形式化为 HTWR 的"主导线 + 扇出辅助导线"分解，并检查其逐项包裹缩减）
> **前置依赖**：笔记一《HTWR Core》公理 I–IV（[001-htwr-core.md](001-htwr-core.md)）、笔记四《扇出成本与区间包裹》（[005-fanout-wrapping.md](005-fanout-wrapping.md)）、[aeglib docs 17](../../../aeglib/docs/17-vdp-c11-certification.md) §11–12
> **日期**：2026-11-14
> **可运行见证**：[006-split-tube-witness.py](006-split-tube-witness.py)（纯 Python RK4 + RHS 量级核对，无第三方依赖）
> **实现参照**：`aeglib/crates/aeg-hilbert16/src/vdp_certified/{model,taylor}.rs`（0.0.2，`f93947f`）

---

## 一、VdP 增广 8 维系统与块三角结构

VdP C11 认证把周期轨道、变分矩阵与水平作用量并成一个 8 维增广状态

```
z = (x, y, φ11, φ12, φ21, φ22, A_hor, I)
```

其向量场（`model.rs::rhs_interval`，`ε=1`）为

```
x'   = y                                    （相位）
y'   = ε(1−x²)y − x                          （相位）
φ11' = φ21
φ12' = φ22
φ21' = j21·φ11 + j22·φ21                     （变分，j21 = −1−2εxy, j22 = ε(1−x²)）
φ22' = j21·φ12 + j22·φ22                     （变分）
A_hor' = ε(1−x²)y − x − y²                    （水平作用量）
I'   = y²                                    （作用量）
```

**块三角性（定义性事实）**：相位/作用量分量 `(x', y', A_hor', I')` **只依赖** `(x, y)`，不读变分 `φ`；变分分量 `φ'` 依赖 `(x, y)` 与 `φ`。即

```
F₁(x, y)   = (x', y', A_hor', I')            依赖 (x,y) —— 主线
F₂(x, y, φ) = (φ11', …, φ22')                依赖 (x,y) 与 φ —— 辅线
```

`φ` **不回馈**进相位/作用量。这正是 `taylor.rs` 里 split-tube 的注释原文："phi does not feed back into the phase/action components, so its much larger RHS must not inflate the x/y tube."

## 二、HTWR 分解

把笔记四（005）的"扇出成本"读法套到这个系统：

| HTWR 对象 | VdP C11 分量 | 含义 |
| --- | --- | --- |
| **主导线（主载体导线）** | `(x, y)` 相位 + `(A_hor, I)` 作用量 | 推进实际状态、累积水平作用量 `A_hor=∫(Q−yP)dt`、`I=∫y²dt` 的 depth-1 主载体 |
| **扇出辅助导线** | `φ = ∂z/∂z₀` 变分矩阵 | 相位态的线性化切线响应：Jacobian `J(x,y)=[[0,1],[−1−2εxy, ε(1−x²)]]` 把 `(x,y)` **扇出**成其条目，再以 `Φ'=JΦ` 传播 |
| **横向催化通量 Σ_aux** | `φ` 四分量 | 必须与主载体并行的线性化"辅助导线"，即 HTWR 的扇出拷贝 |

关键：`J(x,y)` 正是笔记四里"`x` 被扇出多次"的 VdP 版本——相位 `(x,y)` 被扇出到 `j21=−1−2εxy`（读 `x,y` 两次）、`j22=ε(1−x²)`（读 `x` 两次）里，再乘上 `φ`。所以变分块是相位态的 **Δ 扇出**，其代价（包裹宽度）就是横向催化通量。

## 三、Split-tube 的逐项包裹缩减

`taylor.rs` 把 Picard 管拆成两组：

```
phase = [0,1,6,7]      r_phase = 0.5·h·max_{i∈phase}|F_i|
phi   = [2,3,4,5]      r_phi   = 0.5·h·max_{i∈phi}|F_i|
```

而未拆分（单半径）是 `r = 0.5·h·max_{0≤i≤7}|F_i|`。由块三角性，`F₁` 不读 `φ`，故 `r_phase` 完全由主线自身的 RHS 决定，**不承载扇出的代价**。于是：

```
r_phase ≤ r （严格当某个变分分量的 |F| 超过所有相位/作用量分量时）
```

**逐项结论**：split-tube 的主线管半径**从不比未拆分更宽**；它是"主导线不替扇出辅助导线付费"这一 HTWR 原则（公理 II.3：Δ 携带独立正作用量代价）在区间算术里的操作化。变分管 `r_phi` 则单独收费（辅助导线的横向通量）。

## 四、计算核对（006 见证）

1. **块三角性**：把 `φ` 置零重算 RHS，相位/作用量分量逐位不变 → `True`（定义性事实的数值复核）。
2. **半径缩减**：沿 C11 周期轨道（`y₀=2.1727126964`，RK4）逐点量 `max|F_phase|`、`max|F_phi|` 与 `r_phase/r_unsplit`：

| t | max\|F_phase\| | max\|F_phi\| | r_phase / r_unsplit |
| ---: | ---: | ---: | ---: |
| 0.00 | 4.7207 | 1.0000 | 1.0000 |
| 1.00 | 3.3237 | 3.2191 | 1.0000 |
| 2.00 | 0.9540 | 0.2807 | 1.0000 |
| 3.00 | 3.9221 | 1.5825 | 1.0000 |
| 3.62 | 7.7175 | **8.4773** | **0.9104** |
| 4.00 | 4.6078 | 3.2744 | 1.0000 |

**诚实的发现**：在**收敛后的 C11 周期轨道**上，变分 RHS 并不持续主导（`r_phase/r_unsplit` 多数为 1，仅在 `t≈3.62` 降到 0.91）。因此 split-tube 的**逐项包裹缩减是弱缩减**（`r_phase ≤ r`，周期轨道上实际 ≤ ~9%）。它的**决定性价值在打靶（shooting）阶段**：docs 17 §11 记录 pre-fix 时 `φ21'≈29.5`（`t≈3.62`），那时变分 RHS 远超相位 RHS，单半径被变分项拉大、反过来放大 `x,y` 的非线性项而发散；拆分才把主线管钉住。这与"周期轨道上 φ 有界、打靶中 φ 可暴涨"一致。

## 五、状态与边界

| 编号 | 结论 | 状态 |
| --- | --- | --- |
| S1 | VdP 增广 RHS 的块三角性（相位/作用量不读 φ） | `PROVED WITH STATED HYPOTHESES`（从定义方程显式算出 + 数值复核） |
| S2 | `r_phase ≤ r_unsplit`（split 从不加宽主线管） | `STANDARD CONSEQUENCE`（子集最大值 ≤ 全集最大值；由 S1 使其有意义） |
| S3 | split-tube = HTWR "主导线 + 扇出辅助导线" 分解 | `STRUCTURAL PROPOSAL`（解释性读法，非定理） |
| S4 | 周期轨道上逐项缩减"弱"、打靶中"强" | `COMPUTATIONALLY VERIFIED EXAMPLE`（有限 RK4 采样，非一般定理） |

**边界**：本笔记形式化的是**机制**（块三角性 + 半径不等式 + HTWR 读法），**不是** split-tube 最优性的证明，也不声称"变分 RHS 恒大于相位 RHS"（S4 明确这是数据依赖的）。OQ-103.4 据此从 `OPEN` 推进为**形式化完成 + 弱缩减确认**（见 [governance/08-open-questions.md](../../governance/08-open-questions.md) OQ-103.4）。

## 六、与既有治理的关系

本笔记不修改公理 I–IV、不修改任何论文正文、不升级任何既有 claim。它把 OQ-103.4 的"形式化 + 逐项检查"落地为可复现见证（[006-split-tube-witness.py](006-split-tube-witness.py)），并登记进 [governance/notes-reserve-audit.md](../../governance/notes-reserve-audit.md) §2.9。研究问题与方向：苑明理；本形式化、见证与状态标注：DeepSeekHarness，2026-11-14。
