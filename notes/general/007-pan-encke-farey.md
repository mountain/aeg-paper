# Pan 与 Encke 缝隙边缘波：Lindblad 共振阶梯的 Farey/Ford 结构（AEG 应用）

> **文档性质**：算术表达式几何（AEG）研究笔记（之六：把 Pan/Encke 缝隙边缘波的 Lindblad 共振阶梯读作 Farey/Ford 结构，并用 aeglib 认证核心代数数）
> **前置依赖**：笔记一《HTWR Core》公理 I–IV（[001-htwr-core.md](001-htwr-core.md)）、笔记四《扇出成本与区间包裹》（[005-fanout-wrapping.md](005-fanout-wrapping.md)）
> **日期**：2026-11-14
> **可运行见证**（aeglib 0.0.2，均用 `ArbBall` 认证代数数）：
> - [pan_encke_resonance_ladder.py](../../../aeglib/python/examples/pan_encke_resonance_ladder.py)（共振阶梯）
> - [pan_encke_gap_criterion.py](../../../aeglib/python/examples/pan_encke_gap_criterion.py)（Hill 半径 + 共振重叠判据）

---

## 一、物理对象

Pan 是土星 Encke 缝隙内的卫星（质量 `M_P≈4.95×10¹⁵ kg`，`GM_P≈3.3×10⁻⁴ km³/s²`，半长轴 `a_P=133,584 km`）。它的引力在缝隙边缘激发**边缘波**（edge waves），观测到边缘呈波纹状。本笔记用线性本轮（epicyclic）天体力学定位这些共振，并把它们的**频率结构**读作 AEG/HTWR 的 Farey/Ford 结构。

## 二、Lindblad 共振阶梯 = Farey 序列

Pan 的第 m 阶引力分量以角速度 `Ω_P` 驱动环粒子，在 **Lindblad 共振**处激发本轮运动：

```
m(Ω − Ω_P) = ±κ ,   Ω = κ = Ω_P (r/a_P)^{−3/2}
```

令 `x := Ω/Ω_P`，得 `m(x−1)=±x`，即

```
内共振 (r<a_P)：x = m/(m−1)      外共振 (r>a_P)：x = m/(m+1)
共振半径：r/a_P = x^{−2/3}
```

**核心观察**：共振频率比 `x = m/(m±1)` 正是共转点 `x=1` 的 **Farey 邻居**，`m→∞` 时 `x→1`。aeglib `ArbBall` 认证的共振半径（部分）：

| m | 外共振 x | r_外/a_P (Arb) | Ford 圆半径 1/(2q²) |
| ---: | --- | --- | --- |
| 1 | 1/2 | 1.58740 | 1.25e-1 |
| 2 | 2/3 | 1.31037 | 5.56e-2 |
| 10 | 10/11 | 1.06560 | 4.13e-3 |
| 100 | 100/101 | 1.00666 | 4.90e-5 |
| **551** | 551/552 | **1.00121** | 1.64e-6 |

**核心结果**：`m=551` 外共振半径 = `a_P + 161.6 km`，恰好落在 Encke 外缘（约 `+162 km`）。即缝隙边缘正是 Pan 的高 m 共振开始密集堆积处。

## 三、缝隙开启判据（Chirikov 共振重叠）

aeglib 认证的两个代数数与一个精确有理间距：

| 量 | 公式 | 值（Arb 认证） |
| --- | --- | --- |
| Hill 半径 | `R_H = a_P (μ/3)^{1/3}` | **19.05 km** |
| 共振宽度 | `dr ~ a_P √μ`（O(1) 系数略） | **0.394 km** |
| 共振间距（m=551） | `dR_m = 2a_P/(3m²)` | **0.293 km**（精确有理 `89056/303601`） |
| 重叠 m | `dr = dR_m ⇒ m ≈ √(2/(3√μ))` | **≈ 475** |

**结论**：`dr ≈ dR_m`（0.394 km ≈ 0.293 km）在 `m≈500–550` 处成立——缝隙边缘是 Pan 的高 m 共振**开始重叠**（Chirikov 判据）处。缝隙半宽 `≈ 8.5 R_H`，说明缝隙由**共振森林重叠**开启，而非 Hill 球直接清空（Hill 半径只有 19 km）。`m_overlap≈475` 与边缘 `m≈551` 相符到 O(1) 系数。

## 四、AEG/HTWR 读法

1. **Farey 结构（精确）**：共振频率比 `x=m/(m±1)` 是共转点 `x=1` 的 Farey 邻居，`m→∞` 堆积在 `1`。这与 HTWR 的 `P¹(Q)` 模型（Ford 圆、连分数）是同一套有理逼近——**不是类比**。
2. **Ford 圆几何（`STRUCTURAL PROPOSAL`）**：每个共振 `x=p/q` 带半径 `1/(2q²)` 的 Ford 圆；`x=m/(m±1)` 时半径 `≈1/(2m²)`，随 m 坍缩并堆积在共转尖点 `x=1`。这就是"共振森林"的几何；共振间距 `d(r/a_P)/dm≈−2/(3m²)` 与 Ford 圆 `~1/m²` 堆积律一致。
3. **HTWR 深度（`STRUCTURAL PROPOSAL`）**：第 m 阶共振的"信息高度" `I = ln max(|p|,|q|) = ln(m+1)` 即方位角波数 m 的对数——卫星的**单个**驱动频率被"扇出"成 m 个方位角谐波，m 正是 HTWR 的扇出数。

## 五、状态与边界

| 编号 | 结论 | 状态 |
| --- | --- | --- |
| P1 | 共振阶梯 `x=m/(m±1)` 与半径 `r/a_P=x^{−2/3}` | `PROVED WITH STATED HYPOTHESES`（Kepler/epicyclic 线性理论的直接计算 + Arb 认证） |
| P2 | 外缘 m≈551 重合（`a_P+161.6 km`） | `COMPUTATIONALLY VERIFIED EXAMPLE`（Arb 认证 + 与观测边缘半径对照） |
| P3 | 共振重叠判据 `dr≈dR_m`、`m_overlap≈475`、`gap≈8.5 R_H` | `STANDARD CONSEQUENCE REQUIRING AN IN-PAPER PROOF`（Chirikov 判据的标准标度）+ `COMPUTATIONALLY VERIFIED` |
| P4 | Farey/Ford 读法（共振森林 = 共转尖点堆积） | `STRUCTURAL PROPOSAL` |
| P5 | HTWR 深度 `I=ln(m+1)` 读法 | `STRUCTURAL PROPOSAL` |

**边界**：本笔记建立的是**共振阶梯的骨架**（频率/半径/重叠判据）。边缘波的**具体波长与振幅**需要密度波色散关系（自引力 `2πGΣ|k|` + 边缘模式），观测波长约几十 km（对应 m~10⁴），不是 m≈551 共振本身——这超出当前覆盖，登记为 OQ-104。

## 六、登记

本笔记不修改公理 I–IV、不修改论文正文、不升级既有 claim。它把 Pan/Encke 现象做成 aeglib 的两个可复现认证计算，并把 Farey/Ford 读法登记进 [governance/notes-reserve-audit.md](../../governance/notes-reserve-audit.md) §2.9；开放项登记为 [governance/08-open-questions.md](../../governance/08-open-questions.md) OQ-104。研究问题与方向：苑明理；本分析、认证与状态标注：DeepSeekHarness，2026-11-14。
