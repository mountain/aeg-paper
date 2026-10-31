# 差分代换 ↔ Magnus 展开：阿贝尔化同构（PBW）

## 待办 2 的推进：杨路差分代换是 Magnus 展开的阿贝尔化

### Research Note v0.1（跨项目）

**2026-10-31**（v0.1：推进 `22` 待办 2。结论：**差分代换的"累积和"`x_j=d₁+⋯+d_j` 是 Magnus 展开 `log(e^{X₁}⋯e^{Xₙ})` 在阿贝尔化（所有括号=0）下的形式**；两者经 PBW 定理联系——单项式基 = 李字基的 associated graded。括号项正是 AEG 的缺陷 `μλ`，故"差分代换 = 缺陷为零时的 Magnus"）

---

## 0. 目标与结论

`22` 待办 2 问：杨路"差分代换 = 单项式展开"与 AEG"Magnus = 自由李代数展开"（`21`）是否同构。

**结论预告**：**是，且同构的精确形式是"阿贝尔化"**——

1. **差分代换的"累积和" = 阿贝尔 Magnus**：`x_j = d₁+⋯+d_j` 就是 `log(e^{d₁}⋯e^{d_j}) = d₁+⋯+d_j`（标量交换，无括号）。
2. **Magnus 展开 = 非交换累积和**：`log(e^{X₁}⋯e^{Xₙ}) = ΣX_i + 括号`，括号正是 AEG 的缺陷 `μλ`。
3. **PBW 桥梁**：自由李代数的包络代数 `U(Lie(g)) = T(g)`（字），其 associated graded `gr = S(g)`（单项式）——**单项式基 = 李字基的阿贝尔化**。
4. **一句话**：**差分代换是缺陷 `μλ=0` 时的 Magnus 展开。**

---

## 1. `[Adva]` 差分代换的机制（回顾 `0185`）

变量非负时，把第 `j` 小变量换成前 `j+1` 个差分变量之和：

\[
x_1=d_1,\quad x_2=d_1+d_2,\quad \dots,\quad x_j=d_1+\cdots+d_j,
\]

代换后**展开成单项式**（分配律），**系数全非负 ⟹ 锥上非负**；全 `n!` 次序通过 ⟹ 全象限非负。`[Adva]`（`0185` §3）。

**关键结构**：代换 `x_j = d₁+⋯+d_j` 是**累积和**（离散积分）；展开是**分配律**（把累积和压成单项式）。

---

## 2. `[AEG]` Magnus 展开的机制（回顾 `21`）

对词 `γ=(X₁,…,Xₙ)`，`log(e^{X_n}⋯e^{X_1})` 是 Lie 级数：

\[
\log\big(e^{X_n}\cdots e^{X_1}\big)
= \underbrace{\textstyle\sum_i X_i}_{\text{1 阶（和）}}
+ \underbrace{\tfrac12\textstyle\sum_{i<j}[X_i,X_j]}_{\text{2 阶（交换子）}}
+ \underbrace{\text{3 阶及以上（嵌套括号）}}_{\text{高阶}}
\]

项 = 嵌套括号，系数在自由李代数 `Lie(X₁,…,Xₙ)`（Hall/Lyndon 基）。`[AEG]`（`21` §2，`CLASSICAL` Magnus/BCH）。

**关键结构**：Magnus = **非交换累积和**——1 阶是"和"（阿贝尔部分），2 阶及以上是"括号"（非交换部分，即缺陷）。

---

## 3. `[对应]` 同构：差分代换 = 阿贝尔化的 Magnus

**Theorem（阿贝尔化同构，`structural proposal` + `CLASSICAL`）**：差分代换的"累积和" `x_j = d₁+⋯+d_j` 是 Magnus 展开在**阿贝尔化**（令所有括号 `[X,Y]=0`）下的形式：

\[
\text{阿贝尔化}:\quad \log\big(e^{X_1}\cdots e^{X_n}\big)\ \longmapsto\ \sum_i X_i
\qquad（\text{BCH 中所有 }[X,Y]=0 \Longrightarrow e^Xe^Y=e^{X+Y}）.
\]

**证明**：阿贝尔李代数里 `[X,Y]=0`，BCH 给 `e^X e^Y = e^{X+Y}`，故 `log(e^{X₁}⋯e^{Xₙ}) = ΣX_i`（无括号）。而 `Σ_{i≤j} d_i` 正是差分代换的累积和。∎（`CLASSICAL` BCH + 平凡核对。）

**含义**：

- **差分代换 = 阿贝尔（无缺陷）的 Magnus**：增量为标量 `d_i`（交换），故累积和只有 1 阶（和），无括号。
- **AEG 的 Magnus = 非交换（有缺陷）的累积和**：增量为运算 `X_i`（不交换），故累积和有括号，括号 = 缺陷 `μλ`。
- **缺陷 `μλ` 是 Magnus 与差分代换之间的"差"**：`μλ=0 ⟺` 括号全零 ⟺ Magnus 退化为差分代换。

---

## 4. `[对应]` PBW 桥梁：单项式基 = 李字基的阿贝尔化

两者的"展开进基"由 PBW 定理精确联系：

- **Magnus 侧**：自由李代数 `Lie(g)`，其包络代数 `U(Lie(g)) = T(g)`（**字** = 生成元的有序积），基 = 李字（Hall/Lyndon）。
- **差分代换侧**：对称代数 `S(g)`（**单项式** = 生成元的无序积），是 `U(Lie(g))` 的 **associated graded**。
- **PBW**：`gr(U(Lie(g))) = S(g)`——**单项式基 = 李字基的阿贝尔化**（把字 `X_{i₁}⋯X_{iₖ}` 重排并合并同类项成 `X₁^{α₁}⋯Xₙ^{αₙ}`）。

`[对应]`（`CLASSICAL` PBW 定理 + `structural proposal` 的对应读法）。

**所以**：Magnus（李括号展开）经 PBW/阿贝尔化 → 交换多项式（单项式展开）→ 差分代换的展开对象。两者是**同一"展开进基"操作在两个层上的形式**：非交换层（字/李括号）与交换层（单项式）。

---

## 5. `[对应]` 系数查：同一结构，不同用途

| | `[Adva]` 差分代换 | `[AEG]` Magnus |
|---|---|---|
| 展开的基 | 单项式 `d_1^{α₁}⋯d_n^{αₙ}`（`S(g)`）| 李字 `[X_{i₁},[…]]`（`Lie(g)` Hall 基）|
| 系数查 | 系数 ≥ 0（**正性**）| Magnus 系数（**缺陷**）|
| 用途 | 证明不等式非负 | 度量非交换性 `μλ` |
| 阿贝尔/非交换 | 阿贝尔（无括号）| 非交换（有括号）|

**同一结构**：都是"展开进基 + 提取系数"。
**不同用途**：杨路用**系数非负**证正性（不等式）；Magnus 用**系数**度量缺陷（非交换性）。

`[对应]`（`structural proposal`：结构同构成立，用途不同。）

---

## 6. 地位总表与残余

| 命题 | 地位 | 来源 |
|---|---|---|
| §1 差分代换机制 | `[Adva]` 原文 | `0185` |
| §2 Magnus 机制 | `[AEG]` + `CLASSICAL` | `21` |
| §3 阿贝尔化同构（差分代换 = 阿贝尔 Magnus）| `[对应]` `CLASSICAL`（BCH 阿贝尔化）+ `structural proposal` | 本笔记 |
| §4 PBW 桥梁（单项式基 = 李字基的 associated graded）| `[对应]` `CLASSICAL`（PBW）+ `structural proposal` | 本笔记 |
| §5 系数查（正性 vs 缺陷）| `[对应]` `structural proposal` | 本笔记 |

**残余（`open`）**：

1. **正性 ↔ 缺陷的精确对偶**：杨路"系数非负 ⟹ 正性"与 AEG"括号系数 ⟹ 缺陷"是否有更深的对偶（如"非负系数 = 无缺陷"的某种形式）？目前只有"阿贝尔化 ⟹ 括号消失"，没有"正性 ⟺ 无缺陷"的精确陈述。
2. **差分代换的 `n!` 次序 ↔ Magnus 的字**：杨路要遍历 `n!` 个次序（置换），Magnus 要遍历字（自由李代数的 Hall 基）——两者都是"遍历一个组合结构"，是否有精确对应（`n!` 次序 = 对称群的元素，Hall 基 = 自由李代数的基）？
3. **落到 AEG**：把"差分代换 = 缺陷 μλ=0 的 Magnus"落成 AEG 命题——即"当加乘交换（`μλ=0`）时，DAG 计算的缺陷为零，级数退化为累积和"，与 `17`/`20` 的"缺陷 = 朴素交换失败"对齐。

---

**参考**：

- **Adva 侧**：`~/work/public/adva/docs/research/0185-yang-difference-substitution-inequalities.md`。
- **AEG 侧**：`aeg-paper/notes/analysis-and-calculus/21-series-theory-free-lie-algebra.md`、`17-contact-curvature-as-dag-defect.md`、`20-defect-1-cocycle-bch.md`。
- 标准：BCH 公式、Poincaré–Birkhoff–Witt 定理、自由李代数的 Hall/Lyndon 基。
