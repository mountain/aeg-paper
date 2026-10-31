# OQ-094b：ρ 的 Scott 连续性边界

## "无限矩阵乘积收敛 ⟷ 越界"的精确负结果

### Research Note v0.1

**2026-10-31**（v0.1：闭合 OQ-094b。证明射影求值 `ρ: Hist^nd → PGL₂` 无 Scott 连续扩张，唯一候选扩张是无限矩阵乘积 = 连分数收敛，从而给出 Paper I "只做有限词"这一 scope 边界的序拓扑理由）

---

## 0. 目标与结论

`10` §5 观察：`ρ(γδ)=ρ(δ)ρ(γ)` 不单调、`PGL₂` 不带 dcpo 序，无限历史 `γ_∞` 的"射影值"是无限矩阵乘积。本笔记把它写成**精确的定理与证明**。

**结论预告**：

1. **定理 1（序论负结果）**：`ρ` 在非平凡序下**不单调**（唯一使 `ρ` 单调的序是平凡预序）；故由自由 dcpo 泛性质，`ρ` **无** Scott 连续扩张到历史 dcpo `Γ^≤ω`。
2. **定理 2（分析边界）**：唯一候选"极限扩张"是无限矩阵乘积 `lim_n [M_n⋯M_1]`，其收敛恰为**无限乘积 / 连分数收敛**——即 Paper I（与 Paper 0 scope）明确排除的"infinite arithmetic expressions 的一般收敛理论"，属 Paper II/III。
3. **推论（scope 的序拓扑理由）**：`ρ` 的 Scott 连续性 ⟺ 无限算术表达式的收敛性 ⟺ 越出 Paper I 主体。Scott 拓扑本身**不**产生收敛的算子语义；那需要被排除的解析收敛理论。

---

## 1. 记号与对象

- `Γ` = 非退化初等 context 的字母表（`paper-1` §3 的表；`c≠0` 的乘法、`z/c`、`c/z` 等）。`H = Γ^*`（有限词）。
- 前缀序 `γ ⊑ γδ`（`eq:chronological-history-concatenation`）。ideal completion `Idl(H) ≅ Γ^≤ω = Γ^* ∪ Γ^ω`（有限 + 可数无限历史），紧致元 = 有限词（`09` §8）。
- Scott 拓扑 `σ` 于 `Γ^≤ω`：基 `{↑γ}`（"前缀 γ 已发生"）。
- 射影求值 `ρ: H → PGL₂(K)`，`ρ(γ) = [M_n⋯M_1]`，`ρ(∅)=1`，满足反同态 `ρ(γδ) = ρ(δ)ρ(γ)`（`paper-1` `def:projective-evaluation`、`prop:projective-evaluation-chronology`）。
- `ρ` 满射到 `PGL₂(K)`（`paper-1` `thm:bilateral-pgl2-generation`）。

---

## 2. 定理 1：`ρ` 无 Scott 连续扩张（序论负结果）

**Theorem 1.** 设 `≤` 是 `PGL₂(K)` 上的任一偏序。若 `ρ:(Γ^*, ⊑) → (PGL₂(K), ≤)` 单调，则 `≤` 是平凡预序（`x ≤ y` 对一切 `x,y`）。因此 `ρ` 没有取值于非平凡 dcpo 的 Scott 连续扩张。

**证明**：单调性给

\[
\gamma \sqsubseteq \gamma\delta \implies \rho(\gamma) \le \rho(\gamma\delta) = \rho(\delta)\rho(\gamma).
\]

因 `ρ` 满射，令 `h = ρ(γ)`、`g = ρ(δ)` 遍历 `PGL₂(K)`，得

\[
\forall g,h:\quad h \le g\,h .\tag{1}
\]

- 取 `g = h^{-1}`：`h ≤ h^{-1}h = 1`，即 `h ≤ 1` 对一切 `h`。
- 取 `h = 1`（`γ = ∅`，`ρ(∅)=1`）：`1 ≤ g·1 = g`，即 `1 ≤ g` 对一切 `g`。

故 `h ≤ 1 ≤ g` 对一切 `h,g`，即 `x ≤ y` 对一切 `x,y`——`≤` 是平凡预序。∎

**推论**：由自由 dcpo 泛性质（`09` §8.3：`f:H→D` 可 Scott 连续扩张到 `Idl(H)` ⟺ `f` 单调），`ρ` 单调仅对平凡序成立，而平凡预序不构成（非平凡）dcpo；故 `ρ` **没有**非退化的 Scott 连续扩张 `ρ̂: Γ^≤ω → D`（`D` 为任一非平凡 dcpo，经单射单调嵌入含 `PGL₂` 的像）。

**注（为何必须平凡）**：障碍不是"值域选错"，而是**前缀序与左乘反同态的结构性冲突**——`γ ⊑ γδ` 是"追加"，而 `ρ(γδ)=ρ(δ)ρ(γ)` 是"左乘"；任何群上与其左乘作用兼容的序都只能是平凡序（`h ≤ gh` 对一切 `g` 迫使一切元等价于 `1`）。

---

## 3. 定理 2：唯一候选扩张 = 无限矩阵乘积 = 连分数（分析边界）

**Theorem 2.** 在 Lawson（乘积）拓扑下对 `ρ` 作"极限扩张"时，唯一候选值是

\[
\hat\rho(\gamma_\infty) = \lim_{n} \rho(\gamma_n) = \lim_{n} [M_n\cdots M_1] ,
\qquad \gamma_n = (g_1,\dots,g_n),\ \ \gamma_\infty = \bigsqcup_n \gamma_n .
\]

这个极限的存在性（于 `PGL₂(K)` 或逐点于 `P^1(K)`）**正是**无限矩阵乘积 / 无限连分数的收敛问题，属于被排除的收敛理论。

**证明（结构）**：

1. `γ_∞ = ⊔_n γ_n` 是有限前缀的定向并（`09` §8.2）。任何把 `ρ` 连续延拓到 `γ_∞` 的尝试，都必须把 `ρ(γ_∞)` 定义为 `ρ(γ_n)` 的极限（Scott 连续 = 保定向并；乘积拓扑下的连续 = 逐坐标极限）。
2. `ρ(γ_n) = [M_n⋯M_1]` 是有限矩阵乘积的射影类。其 `n→∞` 极限 `[⋯M_n⋯M_1]` 是**无限矩阵乘积**，一般不存在于 `PGL₂`（例：`M_n` 平移 `T_{a_n}` 时乘积发散到 `∞`；`M_n` 交替 `J,T` 时给出连分数收敛域）。
3. **连分数对应（`CLASSICAL`）**：无限 Möbius 映射复合（在基点上取值）＝ 广义连分数。显式实例（`computationally verified example`）：取 `γ_i = (\neg, T_{a_i})`（时序：先 `¬(z)=1/z` 再 `T_{a_i}(z)=z+a_i`），则 `ρ(γ_i) = T_{a_i}∘¬ = f_i`，`f_i(z) = a_i + 1/z`。于是

\[
\rho(\gamma_0\gamma_1\cdots\gamma_n)(\infty)
= f_n\circ\cdots\circ f_1\circ f_0(\infty)
= a_n + \frac{1}{a_{n-1} + \frac{1}{\ddots + \frac{1}{a_0}}}
= [a_n; a_{n-1},\dots,a_0],
\]

其 `n→∞` 极限正是连分数 `[a_0;a_1,a_2,\dots]`（反向索引）的收敛性——经典连分数收敛理论。

**结论**：`ρ̂(γ_∞)` 的存在与取值，等价于"无限算术表达式（无限矩阵乘积 / 连分数）是否收敛"；后者是 `AGENTS.md`（Paper 0 scope）与 Paper I 明确**排除**的"a general convergence theory for infinite arithmetic expressions"，属于 Paper II（解析函数理论）/ III（奇点与零几何）。∎

---

## 4. 推论：Scott 连续性 ⟺ 越界

**Corollary（094b 的边界）**。以下三者等价（在"把 `ρ` 延拓到无限历史"这个意义下）：

\[
\rho\ \text{的 Scott 连续性}\ \Longleftrightarrow\ \text{无限矩阵乘积的收敛性}\ \Longleftrightarrow\ \text{越出 Paper I 主体范围}.
\]

因此 Paper I 把历史限制为**有限词**（§2 `def:marked-spinal-history`、§3 `Hist^nd`），并声明"no general convergence theory for infinite arithmetic expressions"（scope 边界），**有精确的序拓扑理由**：Scott 拓扑（前缀可观测）本身不产生收敛的算子语义；从有限历史到无限历史的算子极限需要解析收敛理论，而那在域论层不可得、需交给下游。

**正反两面的对照**（把 `09`–`13` 与 094b 统一）：

| 层 | 单调？| Scott 连续延拓？| 归宿 |
|---|---|---|---|
| 正 / 单侧 sector（`Aff^+`，值格 `[0,∞]`）| 是（在加性 sector）| **有**（`09` §9、`11`/`12`/`13`）| Paper 0 分析层 |
| 全射影（`PGL₂`）| 否（定理 1）| **无**（定理 1），唯一候选 = 连分数收敛（定理 2）| Paper II/III |

即：Scott 连续性**恰好**在"单侧 / 正 sector"上成立，**恰好**在"双侧 / 全射影"上失败——失败处即连分数收敛，即 scope 边界。这与 `09`–`13` 的"Scott ⟷ 单侧、Lawson ⟷ 双侧"完全一致。

---

## 5. 地位总表

| 命题 | 地位 |
|---|---|
| §2 定理 1（ρ 单调 ⟹ 平凡序；无 Scott 连续扩张）| `proved`（满射 + 反同态 + 自由 dcpo 泛性质；`09` §8.3 为 `CLASSICAL`）|
| §3 定理 2（唯一候选 = 无限矩阵乘积）| `proved with stated hypotheses`（定向并 = 前缀极限的结构事实）|
| §3 连分数对应 | `CLASSICAL`（无限 Möbius 复合 = 连分数）+ `computationally verified example`（显式 `γ_i=(¬,T_{a_i})` 与收敛式）|
| §4 推论（三等价 + scope 理由）| `structural proposal`（scope 归属是系列约定，等价关系本身由定理 1/2 支撑）|

---

## 6. 收尾

094b 闭合：**`ρ` 的 Scott 连续性 = 无限矩阵乘积收敛 = 越界**，以两个定理（序论负结果 + 分析边界）精确成立；连分数是"无限历史算子极限"的具体化身。Paper I "只做有限词"的边界由此获得序拓扑 + 解析的双重理由。

**参考**（沿用）：

1. D. Scott, *Continuous lattices*, LNM 274, Springer (1972).
2. G. Gierz et al., *A Compendium of Continuous Lattices*, Springer (1980).
3. M.W. Warner, *Fuzzy topology with respect to continuous lattices*, Fuzzy Sets and Systems 35 (1990) 85–91.
4. `paper-1/sections/02-sequential-histories.tex`、`03-projective-affine.tex`（`def:projective-evaluation`、`prop:projective-evaluation-chronology`、`thm:bilateral-pgl2-generation`）。
5. `notes/analysis-and-calculus/09-order-topology-scott-lawson.md` §8（自由 dcpo 泛性质）。
