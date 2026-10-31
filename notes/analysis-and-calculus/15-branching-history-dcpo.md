# OQ-094c：分支历史的 dcpo

## 子-DAG 加细序：信息序 = 下集（理想）嵌入，及 Birkhoff 对偶

### Research Note v0.1

**2026-10-31**（v0.1：闭合 OQ-094c。给出分支历史的信息序 = 下集嵌入、ideal completion = 有限 ∪ 无限计算 DAG、紧致 = 有限，并证明脊髓情形的前缀序是其链特例、线性扩展 = 极大链 = 脊髓历史）

---

## 0. 目标与结论

`09` §8 对**标记脊髓历史**给出 dcpo（前缀序 + ideal completion = 有限 ∪ 无限历史），并留"分支（非脊髓）历史"为开放（§8.4 问题 1）。`10` §6 给出候选方向（子-DAG/子树加细、依赖偏序、Birkhoff 入口）。本笔记把它落实为精确构造。

**结论预告**：

1. **对象**：有限计算 DAG = 有限依赖偏序集 `P = (I(T), ≼)`（`paper-1` `def:internal-dependency-poset`）。
2. **信息序**：`P ⊑ Q ⟺ P` 是 `Q` 的**下集（序理想）**——"`P` 是 `Q` 的一个已完成的子计算"。
3. **定向完备**：`Idl(FinDAG, ⊑) ≅` 有限 ∪ 无限计算 DAG；紧致元 = 有限 DAG。
4. **统一**：脊髓情形的**前缀序 = 链上的下集序**（`09` §8 是本节 `P` 为链的特例）。
5. **Birkhoff 对偶**：固定 `P` 的偏求值 = 下集格 `O(P)`（有限分配格）；合法求值序 = 线性扩展 = `O(P)` 的极大链 = 脊髓历史。

---

## 1. 对象：有限计算 DAG

**Definition 1（有限计算 DAG）**：一个有限计算 DAG 是一个有限偏序集 `(P, ≤)`，元素为运算，`u ≤ v` 意为"`u` 的产出是 `v` 的输入"（`u` 先于 `v`）。对 `paper-1` 的表达式树 `T`，取 `P = I(T)`，`≤ = ≼_T`（祖先序，`def:internal-dependency-poset`）。

（标注：本节先做**序结构**；运算符号 / 常数 / 槽位是附着在偏序集上的标签，§7 述其承载。`REFORMULATION`：这是 `paper-1` §2 的依赖偏序的直接复用。）

---

## 2. 信息序 = 下集（理想）嵌入

**Definition 2（信息序）**：`(P, ≤_P) ⊑ (Q, ≤_Q)` ⟺ `P` 是 `Q` 的**下集**：`P ⊆ Q`、`≤_P = ≤_Q|_P`、且 `∀x∈P, y∈Q: y ≤_Q x ⟹ y ∈ P`。

**直觉**：`P ⊑ Q` 读作"`P` 是 `Q` 的一个**已完成的子计算**"——你只有完成了 `x` 的全部输入 `y` 才能完成 `x`，故已完成的运算集必须是下集。这是 `09` §8 "前缀 = 有限逼近"在分支情形的忠实推广，不引入新数据。`REFORMULATION`（外加序是 `paper-1` 自己的依赖序）。

**Lemma 1**：`⊑` 是偏序（自反 / 反对称 / 传递——下集关系的标准性质）。`CLASSICAL`。

**Lemma 2（定向族的并）**：`(FinDAG, ⊑)` 中任一定向族 `{P_i}` 有良定义的**直并** `⋃_i P_i`（一个可能无限的偏序集）：任两个 `P_i, P_j` 有公共上界 `Q`，二者皆为 `Q` 的下集，故其并仍是 `Q` 的下集，序一致。`CLASSICAL`。

（注意：定向族**不必是链**——两个同为 `Q` 下集的有限 DAG 可互不包含。这与词情形不同：词的前缀线性有序，故词上"定向 = 链"；DAG 的下集偏序则允许多个互不可比的方向同时增长。）

---

## 3. 定向完备：ideal completion = 有限 ∪ 无限 DAG

**Theorem 1（理想完备）**：`Idl(FinDAG, ⊑)`（自由 dcpo）同构于**每个运算都只有有限多个前驱**的计算 DAG（"有限下集生成的" DAG；等价地，是其有限子 DAG 的直并的那类 DAG）。经理想 `I ↦ ⋃ I`；其逆为 `Q ↦` `Q` 的全部有限下集。紧致元 = 有限 DAG；每个这样的无限 DAG `Q` 是其有限下集的定向并：

\[
Q = \bigsqcup\{\,P \subseteq Q : P \text{ 有限下集}\,\}.
\]

**证明**（`CLASSICAL`，理想完备定理实例化）：理想 `I`（定向且下闭）的直并 `⋃I` 是良定义偏序（Lemma 2），且其每个元素都在某有限下集里（因该元素先属于某个 `P_i ∈ I`）。每个有限下集 `P ⊆ ⋃I` 都含于某 `P_i ∈ I`（定向 + 有限），故 `I` = `⋃I` 的全部有限下集。反向，若 `Q` 的每个元素都在某有限下集里（即每个运算只有有限多个前驱），则 `Q` 的有限下集族定向（两有限下集之并仍是有限下集），且直并 = `Q`。故 `I ↦ ⋃I` 是双射。紧致元 = 主理想 `↓P`（`P` 有限）= 有限 DAG。∎

**排除的情形（有意义）**：无限多极小运算共同供给一个顶运算的"扫帚"DAG（`q_n ≤ q_∞`，`n ∈ ℕ`）**不在** `Idl(FinDAG)` 中——顶运算 `q_∞` 有无限多前驱，不在任何有限下集里，故不可由有限子计算定向逼近。这与词情形完全平行：无限词 `(g_1,g_2,\dots)` 每个位置只有有限多前驱（前面的位置），而"第一个位置之前有无限多字母"的对象不存在。`CLASSICAL` / `REFORMULATION`。

\[
\boxed{
  \text{有限计算 DAG}\ \subset\ \text{有限} \cup \text{（前驱有限化的）无限计算 DAG}\ \cong\ \operatorname{Idl}(\mathrm{FinDAG}),
  \qquad
  \text{有限} = \text{紧致} = \text{可计算逼近}.
}
\]

这是 `09` §8 的"有限历史 ⊂ 有限 ∪ 无限历史 ≅ Idl(H)"在分支情形的逐字推广。`REFORMULATION` + `CLASSICAL`。

---

## 4. 统一：前缀序 = 链上的下集序

**Theorem 2（脊髓是链特例）**：当 `P` 是**链**（sequential tree 的依赖偏序，`thm:sequential-tree-classification`）时，`P` 的下集格 `O(P)` 是一条链 `∅ ⊂ \{g_1\} ⊂ \{g_1,g_2\} ⊂ ⋯ ⊂ P`，且下集序恰为词的前缀序。故 `09` §8 的"时序前缀序"是本节"下集序"在链上的特例。

**证明**：链 `g_1 ≤ g_2 ≤ ⋯ ≤ g_n` 的下集恰为前段 `\{g_1,\dots,g_k\}`（`k=0,\dots,n`），按包含序即前缀序。∎（`REFORMULATION` + 平凡核对。）

**含义**：`09`–`14` 对脊髓历史建立的整套 dcpo / Scott / Lawson / ρ 边界，是分支理论沿"依赖偏序 = 链"这一退化方向的投影；本节给出覆盖全分支树的推广。

---

## 5. 偏求值与 Birkhoff 对偶：线性扩展 = 极大链 = 脊髓历史

**Theorem 3（固定 DAG 的偏求值）**：对固定有限 DAG `P`：

1. **偏求值** = 下集 `O(P)`（"已完成运算的集合"），按包含序成**有限分配格**（Birkhoff 表示定理的对象）。`CLASSICAL`。
2. **合法求值序** = `P` 的线性扩展 = `O(P)` 的**极大链** `∅ = D_0 ⊂ D_1 ⊂ ⋯ ⊂ D_{|P|} = P`（每步加一个极小元）。`CLASSICAL`。
3. **每条极大链 = 一条脊髓历史**：极大链给出一个全序（线性化）`v_1 < v_2 < ⋯ < v_{|P|}`，即一条 sequential 求值序；标记累加器后即 `paper-1` 的 marked spinal history（`prop:marked-tree-history-correspondence` 的推广）。

**证明**：下集格是分配格（`CLASSICAL`）。线性扩展 ↔ 极大链：极大链每步 `D_i ↦ D_{i+1}` 加一极小元，累积顺序即线性扩展。∎

**含义（branching 的语义）**：

- **脊髓树**（`P` 链）→ `O(P)` 是链 → **唯一**极大链 = **唯一**脊髓历史（`paper-1` §2 已证）。
- **分支树**（`P` 非链）→ `O(P)` 是分配格 → **多条**极大链 = **多条**脊髓历史 = 多个合法求值序。分支树的"完整空间" = `O(P)`（偏求值格），其极大链 = 全部脊髓线性化。

这把 `paper-1` §2 的"链 vs 分支"二分，深化为：**单条脊髓历史 = `P` 的线性扩展 = `O(P)` 的极大链；分支树的完整空间 = `O(P)` 上的 Scott 拓扑**。`structural proposal`（对应关系），其中下集格 / 线性扩展事实为 `CLASSICAL`。

---

## 6. Scott / Lawson 拓扑

**Theorem 4（拓扑）**：在 `Idl(FinDAG)` 上：

- **Scott 拓扑**：基 `{↑P : P 有限}`，`↑P = {Q : P ⊑ Q}` = "`P` 这个子计算**已**完成"。
- **Lawson 拓扑** = Scott ∨ lower = 加补集 `{Idl ∖ ↑P}` = "`P` 这个子计算**未**完成"。

这是 `10` §4（词空间上的乘积/康托拓扑）的分支推广：Scott 基仍是"有限子计算已发生"的可观测量；Lawson 补上"未发生"侧。`structural proposal`（对应），Scott/Lawson 定义本身 `CLASSICAL`。

（当 `P` 限制为链时，`↑P` = `↑γ`（前缀已发生），退回 `10` §4 的词空间情形；§4 的统一保证。）

---

## 7. 地位总表与残余

| 命题 | 地位 |
|---|---|
| §1 对象（依赖偏序 = 计算 DAG）| `REFORMULATION`（`paper-1` `def:internal-dependency-poset`）|
| §2 信息序 = 下集嵌入、Lemma 1/2 | `REFORMULATION`（下集序）+ `CLASSICAL`（下集关系）|
| §3 定理 1（`Idl(FinDAG) ≅` 有限 ∪ 无限 DAG，紧致 = 有限）| `CLASSICAL`（理想完备定理实例化）|
| §4 定理 2（前缀 = 链上下集序）| `REFORMULATION` + 平凡核对 |
| §5 定理 3（`O(P)` 分配格、线性扩展 = 极大链 = 脊髓历史）| `CLASSICAL`（Birkhoff / 线性扩展）+ `structural proposal`（与脊髓历史的对应）|
| §6 定理 4（Scott/Lawson 拓扑）| `structural proposal`（对应）+ `CLASSICAL`（定义）|

**残余**（`open problem`，不阻塞本节结论）：

1. **标签承载**：本节在**无标偏序**上做 dcpo；运算符号 / 常数 / 槽位标签需显式承载（把 `P` 换成"带标签偏序"，`⊑` 要求标签一致）。这是机械的，但需写出以对接 `paper-1` 的 `C_{ω,c}^{(ε)}`。
2. **求值语义**：分支历史的求值 `ev` 是否 / 在何种 sector 上 Scott 连续，与 `09` §8.3 的脊髓情形平行，但值格需取 dcpo（如 `[0,∞]`），且偏性（除法零点）与不单调障碍同 §8.4 问题 2——需在分支框架重述。
3. **与 paper-1 §2 的对接**：Theorem 3 把"线性扩展 = 脊髓历史"落到 `O(P)` 的极大链，但尚未写出把 `O(P)`（偏求值格）作为 paper-1 新对象引入正文的最小改动。

---

## 8. 收尾

094c 的**核心**（信息序、定向完备、紧致元、统一、Birkhoff 对偶）已闭合：**分支历史的 dcpo = 有限 ∪ 无限计算 DAG，信息序 = 下集嵌入，紧致 = 有限**；脊髓情形的前缀序是链特例；分支树的完整空间是下集格 `O(P)`，其极大链 = 全部脊髓历史。剩余为标签承载与求值语义的对接（§7 残余）。

**参考**（沿用）：

1. D. Scott, *Continuous lattices*, LNM 274, Springer (1972).
2. G. Gierz et al., *A Compendium of Continuous Lattices*, Springer (1980).
3. G. Birkhoff, *Lattice Theory*, AMS (1967)（下集格 / 有限分配格表示）。
4. `paper-1/sections/02-sequential-histories.tex`（`def:internal-dependency-poset`、`thm:sequential-tree-classification`、`prop:marked-tree-history-correspondence`）。
5. `notes/analysis-and-calculus/09-order-topology-scott-lawson.md` §8。
