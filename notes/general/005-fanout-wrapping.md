# 扇出成本与区间包裹：HTWR 横向催化通量的区间算术读数（Level C 见证）

> **文档性质**：算术表达式几何（AEG）研究笔记（之四：Level C——把 HTWR 核的"扇出成本 / 横向催化通量"读作区间算术的依赖膨胀（wrapping）代价）
> **前置依赖**：笔记一《双曲热带波前-残差核（HTWR Core）》公理 I–IV（[001-htwr-core.md](001-htwr-core.md)）、笔记二《精确时空帕累托边界》（[002-htwr-example.md](002-htwr-example.md)）
> **日期**：2026-11-14
> **可运行见证**：[005-fanout-wrapping-witness.py](005-fanout-wrapping-witness.py)（Python 标准库 `fractions.Fraction`，**精确有理算术，无浮点、无舍入**）
> **aeglib 见证**（2026-11-14）：[aeglib/python/examples/level_c_fanout_wrapping.py](../../../aeglib/python/examples/level_c_fanout_wrapping.py)（用 aeglib 0.0.2 的 `ArbBall` 区间类型复现同一「fanout → wrapping」现象；`ArbBall` 正是 VdP C11 认证使用的区间类型）

---

## 一、问题

笔记二 §二给出一个精确的几何事实：Pell 倍增映射
`k(x_n) = x_{2n} = (x_n² + 2)/(2x_n)` 有两种**语义相等**但**世界面度量不同**的写法：

| 形式 | 表达式 | Δ 扇出 | 截面 | 峰值横向催化通量 Σ_aux |
| --- | --- | ---: | --- | ---: |
| naive | `(x² + 2)/(2x)` | 2 | `(x, x, x)` | `3I_*/2` |
| Heron（部分分式） | `(x + 2/x)/2` | 1 | `(x, 2/x)` | `I_*` |

问题：这个"扇出次数不同"，能否在**区间算术**里被精确复现为**包裹宽度（wrapping）不同**？若能，则 HTWR 的"扇出成本 `c_Δ` / 横向催化通量 `Σ_aux`"就获得一个独立于世界面图景的、可精确计算的算术见证，并直接对接 VdP C11 认证当前最硬的阻塞——区间/仿射 Taylor 管的**依赖膨胀**（[aeglib docs 17 §10–12](../../../aeglib/docs/17-vdp-c11-certification.md)、[18](../../../aeglib/docs/18-vdp-tube-replay-audit.md)、[19](../../../aeglib/docs/19-c11-independent-review.md)）。

## 二、状态标签

本笔记遵循 [governance/05-mathematical-status.md](../../governance/05-mathematical-status.md) 的权威标签：

- 恒等式 `k_naive = k_Heron`（部分分式分解）：`STANDARD CONSEQUENCE REQUIRING AN IN-PAPER PROOF`。
- 区间包裹单调性（fanout 越多包裹越宽）：`COMPUTATIONALLY VERIFIED EXAMPLE`（有限 δ 精确验证 + δ→0 首项精确系数）。
- "扇出成本 = 包裹"的一般对应（interval-width ↔ information-height）：`STRUCTURAL PROPOSAL`，`OPEN PROBLEM`。

据 AGENTS.md：HTWR 公理 I–IV 本身是 `STRUCTURAL PROPOSAL`；本笔记的"包裹见证"是**在其公理化框架外**的独立算术事实，但它与 HTWR 的**对应关系**是结构提议，不是定理。

## 三、精确计算

设 `c = x_4 = 17/12`，`c² = 289/144`。取 `δ < √2 − 17/12 ≈ 0.002453`，保证 `k` 在 `[c−δ, c+δ]` 上单调增（`k'(x) = (x²−2)/(2x²) > 0`），故真像宽度精确为 `W_true = k(c+δ) − k(c−δ)`。

用精确有理区间算术（`±×÷` 对有理端点封闭）计算三种宽度：

| δ | `W_true` | `W_naive` | `W_heron` |
| ---: | ---: | ---: | ---: |
| `1/10³` | `62491/18062491000` | `72187509/18062491000` | `36062491/18062491000` |
| `1/10⁴` | `6249991/18062499910000` | `379934211/950657890000` | `3606249991/18062499910000` |
| `1/10⁵` | `624999991/18062499999100000` | `721875000009/18062499999100000` | `360624999991/18062499999100000` |

**结论（精确）**：

1. 两式在中心精确相等：`k_naive(17/12) = k_Heron(17/12) = 577/408`。
2. 对一切小 δ：`W_true < W_heron < W_naive`。
3. δ→0 首项（精确有理）：
   - `W_true/δ = 1 − 2/c² = 1/289`；
   - `W_heron/δ = 1 + 2/c² = 577/289`；
   - `W_naive/δ = 3 + 2/c² = 1155/289`。
4. 因此包裹 excess（宽度 − 真像宽度）：
   - `excess_heron/δ = 4/c² = 576/289`；
   - `excess_naive/δ = 2 + 4/c² = 1154/289`；
   - **`excess_naive / excess_heron = (c²+2)/2 = 577/288 ≈ 2.0035`**。

## 四、解释：为什么这是"扇出成本"

naive 形式中 `x` 出现 **3 次**（`x·x` 里 2 次、`2x` 里 1 次）= 2 个 Δ 扇出；Heron 形式中 `x` 出现 **2 次**（`x` 与 `2/x`）= 1 个 Δ 扇出。在区间算术里，"变量复用"恰恰就是"扇出"：每扇出一份拷贝，区间算术就把两份拷贝当作**相互独立**的区间处理，从而丢失相关性，产生包裹宽度。因此包裹 excess 随 fanout 数**单调增长**——这正是 HTWR 把 Δ 立为"携带正作用量代价的基本生成元"（公理 II.3）的算术影子。

**关键精度（勿误导）**：这里的包裹 excess 是**一阶**（∝ δ），不是二阶。它的首项系数随 fanout 数单调，但**不是** fanout 数的简单倍数——`excess_naive/excess_heron = 577/288`，而非精确的 `2`。原因在于扇出发生的**位置**（分子 vs 分母 vs 混合）影响包裹系数。因此可安全断言的是**单调对应**（fanout 多 → 包裹宽），不是"包裹 ∝ fanout 数"的线性律。后者的成立需要额外的结构假设，属开放问题。

## 五、与 VdP C11 的对接（Level C 的真正目标）

VdP 变分方程 `Φ' = J(x,y)Φ` 中，状态 `(x,y)` 被扇出到 Jacobian `J` 的四个分量里，**又**被扇出到 `Φ` 自身的传播里；这是 [docs 17/18/19](../../../aeglib/docs/17-vdp-c11-certification.md) 记录的"依赖膨胀 / wrapping"的算术来源。doc 17 §12 手工做的 **split-tube**（phase/action 与 variational φ 分块），在 HTWR 语言里就是**把主载体导线与扇出辅助导线分开**：phase/action 是"主导线"，变分 φ 是"扇出辅助导线"，分开后才不对主线重复收费。

本笔记的 Pell 见证是这条链的**最小玩具版**：它证明"同值不同式 → 不同扇出 → 不同包裹"能在库里被**精确有理**复现（不是浮点、不是类比），从而把 Level C 从一个概念桥降为一个**可复现的算术事实**。2026-11-14 已把同一见证接到 aeglib 0.0.2 上：`aeglib/python/examples/level_c_fanout_wrapping.py` 用 `ArbBall`（VdP C11 认证的同一个区间类型）复现 `width_naive > width_heron`（比值 ≈ 2.002，与精确有理首项一致），`fractions` 部分验证中心恒等式 `577/408`。但注意状态空间的鸿沟仍在：HTWR 的 `I(u) = ln max(|p|,|q|)` 是**有理数大小**（Weil 高度），而 VdP 的包裹宽度是**实区间宽度**。"区间宽度 ↔ 信息高度"的对应尚未建立，这是 Level C 的核心未解项（见 §六 W4）。

## 六、状态总表与开放问题

| 编号 | 结论 | 状态 | 备注 |
| --- | --- | --- | --- |
| W1 | `k_naive = k_Heron`（部分分式恒等式） | `STANDARD CONSEQUENCE REQUIRING AN IN-PAPER PROOF` | 经典；本笔记精确验证 |
| W2 | `W_true < W_heron < W_naive`，excess 随 fanout 单调 | `COMPUTATIONALLY VERIFIED EXAMPLE` | 有限 δ + δ→0 首项精确 |
| W3 | `excess_naive/excess_heron = 577/288`（`c=17/12` 处首项） | `COMPUTATIONALLY VERIFIED EXAMPLE` | 精确有理；非 fanout 数的简单倍数 |
| W4 | "扇出成本 = 包裹"、interval-width ↔ information-height 的一般对应 | `STRUCTURAL PROPOSAL` / `OPEN PROBLEM` | 状态空间鸿沟未填；见下 |

**开放问题**：

1. **（开放）** 建立 `interval-width ↔ information-height` 的精确对应：HTWR 的 `I(u)`（对数 Weil 高度）能否被一个"区间精度的对数"`log(1/width)` 替换，使得 `c_Δ = α·I(u)` 成为包裹 excess 的首项系数？——这决定 Level C 是"单调对应"还是"定量律"。
2. **（开放）** 由 HTWR 定理 1（时空不确定性下界）推出一个"certify 到精度 ε 的管宽/工作量下界"。当前只有 Pell 单调见证；VdP 的 wrapping 下界是 `STRUCTURAL PROPOSAL`，逐纤维证明未做（不得从几何增长直接推出计算下界，AGENTS.md 明令）。
3. **（开放）** 把 doc 17 §12 的 split-tube 形式化为 HTWR 的"主导线 + 扇出辅助导线"分解，并检查它对 VdP 变分方程 `Φ'=JΦ` 是否逐项减少包裹。

---

## 七、与既有治理的关系

本笔记不修改公理 I–IV、不修改任何论文正文、不升级任何既有 claim 状态。它把笔记二 §二的"扇出不同"从世界面图景**独立落地**为一个精确算术见证，并把 Level C 的开放项登记进 [governance/08-open-questions.md](../../governance/08-open-questions.md)（OQ-103）与 [governance/notes-reserve-audit.md](../../governance/notes-reserve-audit.md) §2.9。研究问题与方向：苑明理；本见证、状态标注与开放项：DeepSeekHarness，2026-11-14。
