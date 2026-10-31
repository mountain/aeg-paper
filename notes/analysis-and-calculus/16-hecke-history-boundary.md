# OQ-094d：Hecke 历史空间（Cantor）与 `G₄` 的边界

## 历史层拓扑实现，及对 `10` §4 一处措辞的更正

### Research Note v0.1

**2026-10-31**（v0.1：闭合 OQ-094d。证明历史空间是 Cantor 空间；更正 `10` §4 "`G₄` 作用在其 Cantor 边界上"的不精确措辞——`G₄ = H(√2)` 是**第一类** Fuchsian 格（极限集 = 整个圆周 `P^1(ℝ)`，非 Cantor 集），Cantor 集是**端空间（space of ends）**，因 `G₄ ≅ C₂ * C₄` 殆自由）

---

## 0. 目标与结论

`10` §4 观察：Hecke 子语言 `Hist_4`（3 个生成元 `t_+, t_-, j`）的历史空间是 Cantor 空间，并猜测它对应 `G₄` 的边界。本笔记把它落实，并**更正一处措辞**。

**结论预告**：

1. **[Proved]** `Hist_4^{≤ω} = Γ_4^* ∪ Γ_4^ω`（`Γ_4 = {t_+, t_-, j}`）的 Lawson 拓扑 = 乘积拓扑，`Γ_4^ω ≅ 3^ω` 是 **Cantor 空间**（`10` §4、`12`）。
2. **[CLASSICAL]** `G_4 = ⟨T, J⟩`，`T(z)=z+√2`、`J(z)=-1/z`，`J²=1, (JT)⁴=1`（`paper-1` `prop:hecke-four-arithmetic-relation`），**代数上** `G_4 ≅ C_2 * C_4`（自由积）。故 `G_4` **殆自由**，其**端空间** = Cantor 集（Bass–Serre / 端理论）。
3. **[CLASSICAL]** `G_4 = H(√2)`（q=4 Hecke 三角群）是 **Fuchsian 格**（`λ₄ = √2 ≤ 2`，有限余体积），故**第一类**：极限集 `Λ = P^1(ℝ)`（整个圆周），**不是 Cantor 集**。
4. **[更正]** `10` §4 "`G₄` 作用在其 Cantor 边界上"**不精确**：Cantor 集是**端空间**（组合 / 象征边界），不是极限集（几何边界 = 圆周）。历史 Cantor 空间 `Γ_4^ω` 是**端空间的象征模型**，经 `ρ` 实现"历史 → 端"的通道——这是 `rem:hecke-history-operator-coset` 在历史层的对应（`structural proposal`），而完整 cellulation 与极限集对应属 Paper II/III。

---

## 1. 历史空间是 Cantor 空间（`proved`，沿用 `10`/`12`）

`Γ_4 = {t_+, t_-, j}`（3 字母）。历史空间 `Γ_4^{≤ω} = Γ_4^* ∪ Γ_4^ω` 按前缀序 `γ ⊑ γδ` 成 dcpo，紧致元 = 有限词（`09` §8）。Lawson 拓扑 = 乘积拓扑：`Γ_4^ω` 是 **Cantor 空间** `3^ω`，有限词作为（孤立）紧致点（`10` §4、`12`）。`CLASSICAL` / `proved`。

**含义**：历史层的"边界"（无限历史）`Γ_4^ω` 是标准 Cantor 集；"有限历史 = 紧致 = 可计算"在此有拓扑实现。

---

## 2. `G₄ ≅ C₂ * C₄`，端空间 = Cantor（`CLASSICAL`）

**命题**：`G_4 = ⟨T, J | J² = 1, (JT)⁴ = 1⟩ ≅ C_2 * C_4`（自由积）。

**证明**：令 `x = J`（阶 2）、`y = JT`（阶 4）。则 `T = J^{-1}(JT) = xy`（`J = J^{-1}`），故 `G_4 = ⟨x, y | x² = 1, y⁴ = 1⟩ = C_2 * C_4`。∎（`CLASSICAL`，`paper-1` 关系的重参数化。）

**推论（端空间）**：自由积 `C_2 * C_4` 是**殆自由**的（`C_2 * C_4` 有有限指标自由子群），其**端空间**（space of ends）是 **Cantor 集**，等于其 Bass–Serre 树（`C_2` 与 `C_4` 的无边连接树的商）的边界。`CLASSICAL`（端理论 / Bass–Serre）。

**象征编码（`CLASSICAL`，子位移）**：`C_2 * C_4` 关于 `{T, J}` 的**约化词** = 不含 `JJ` 与 `(JT)⁴`（及其循环变体）的无限词，构成一个**有限型子位移（SFT）**，是 Cantor 集，编码端空间。这正是"历史词的等价关系 = 群关系"的象征形式：`ρ` 的纤维由 `J²=1, (JT)⁴=1` 生成。

---

## 3. `G₄ = H(√2)` 是第一类 Fuchsian 格，极限集 = 圆周（`CLASSICAL`）

**命题**：`H(λ₄)`，`λ₄ = 2cos(π/4) = √2`，是 **Fuchsian 格**（有限余体积，第一类），极限集 `Λ(H(√2)) = P^1(ℝ)`（整个圆周），**不是 Cantor 集**。

**依据**：Hecke 三角群 `H(λ)` 中恰有 `λ ≤ 2` 者为格（有限余体积）——`λ₄ = √2 < 2`，故 `H(√2)` 是格，第一类（极限集 = 全圆周）。参见 [Among the Fuchsian Hecke triangle groups precisely those with parameter λ ≤ 2 are lattices](https://pure.mpg.de/rest/items/item_3119640_1/component/file_3119641/content)。`CLASSICAL`（Hecke 群理论）。

**更正 `10` §4**：`10` §4 写"`G_4` 作用在其边界（Cantor 集）上"是**不精确**的。正确区分两个不同的"边界"：

| 边界 | 对象 | 拓扑 | 出处 |
|---|---|---|---|
| **端空间**（组合 / 象征）| `C_2*C_4` 的端 = Bass–Serre 树边界 | **Cantor 集** | §2 |
| **极限集**（几何）| `H(√2)` 的极限集 | **圆周 `P^1(ℝ)`**（第一类）| §3 |

历史 Cantor 空间 `Γ_4^ω` 编码的是**端空间**（象征边界），不是极限集。

---

## 4. 历史层拓扑实现：`Hist_4 → G₄ → 端`（`structural proposal`）

**Theorem（历史层实现，`structural proposal`）**：射影求值 `ρ: Hist_4 → G_4`（`paper-1` `def:projective-evaluation`）连同约化词编码，给出历史层的合成：

\[
\Gamma_4^{\omega}\ \supseteq\ \{\text{约化无限词}\}\ \xrightarrow{\ \text{编码}\ }\ \operatorname{Ends}(G_4)\ \cong\ \text{Cantor 集},
\]

其纤维恰为 Hecke 关系（`J²=1`、`(JT)⁴=1` 及其循环）。这实现 `paper-1` `rem:hecke-history-operator-coset` 的"历史 → 算子 → 胞腔"分解在**历史层**的版本：

- 历史（Cantor `Γ_4^ω`）→ 算子（`G_4 ≅ C_2*C_4`）→ 端（Cantor）→（极限集 `P^1(ℝ)`，下游）。
- 中间两步的纤维 = 关系（`(JT)⁴=1`）与 stabilizer（`H_C`），均非单射，与 `rem:hecke-history-operator-coset` 的声明一致。

**地位**：历史空间（§1）与群 / 端 / 极限集（§2、§3）各自 `proved`/`CLASSICAL`；把它们串成"历史层实现"是 `structural proposal`（对应关系），**完整**的 `G₄`-等变 cellulation、极限集 `P^1(ℝ)` 上的自动形函数与奇点零集，属 Paper II/III（`paper-1` §3 与 `06-conclusion` 的接口声明）。

---

## 5. 地位总表与残余

| 命题 | 地位 |
|---|---|
| §1 历史空间 = Cantor | `proved`（`10` §4、`12`）|
| §2 `G₄ ≅ C₂*C₄`、端空间 = Cantor、约化词 SFT | `CLASSICAL`（自由积 + 端理论）+ 平凡核对 |
| §3 `H(√2)` 第一类、极限集 = 圆周 | `CLASSICAL`（Hecke 群理论，引用上述文献）|
| §3 更正 `10` §4 的"Cantor 边界"措辞 | 更正（端空间 vs 极限集）|
| §4 历史层实现（`Hist_4 → G₄ → 端`）| `structural proposal`（对应）|
| 完整 cellulation + 极限集对应 | 属 Paper II/III（`open`，已移交）|

**残余**（`open problem`，不阻塞本节结论）：

1. **端 → 极限集的精确映射**：端空间（Cantor）到极限集（圆周 `P^1(ℝ)`）的标准连续映射（Cannon–Thurston / Bowditch 型），把"象征边界"映到"几何边界"，其像为稠密子集或满射——需在 q=4 情形写出精确形式。属 Paper II/III 几何。
2. **约化词的精确 SFT 结构**：`{JJ, (JT)⁴, (TJ)⁴}` 作为禁止词的子位移及其到端空间的双射，需写清（`(JT)⁴=1 ⟹ (TJ)⁴=1` 的循环闭包）。

---

## 6. 收尾

094d 的**可证核心**闭合：历史空间是 Cantor 空间；`G₄ ≅ C₂*C₄` 殆自由、端空间 = Cantor、极限集 = 圆周（第一类）；历史 Cantor 空间是**端空间的象征模型**，实现"历史 → 端"通道。同时**更正 `10` §4** 的"Cantor 边界"措辞（Cantor 是端空间，非极限集）。完整 cellulation 与极限集对应移交 Paper II/III。

至此 **OQ-094 全部四子项（094a–094d）均已处理**：094a（拓扑对应）、094b（ρ 边界）、094c（分支 dcpo）、094d（Hecke 历史层）各自给出可证核心 + 诚实边界。

**参考**：

1. D. Scott, *Continuous lattices*, LNM 274, Springer (1972).
2. G. Gierz et al., *A Compendium of Continuous Lattices*, Springer (1980).
3. M.W. Warner, *Fuzzy topology with respect to continuous lattices*, Fuzzy Sets and Systems 35 (1990) 85–91.
4. [Among the Fuchsian Hecke triangle groups precisely those with parameter λ ≤ 2 are lattices](https://pure.mpg.de/rest/items/item_3119640_1/component/file_3119641/content)（`H(√2)` 为格的依据）。
5. `paper-1/sections/03-projective-affine.tex`（`prop:hecke-four-arithmetic-relation`、`rem:hecke-history-operator-coset`）。
6. `notes/analysis-and-calculus/10-scott-lawson-on-paper-1-main-body.md` §4（历史空间 = Cantor；本笔记 §3 更正其措辞）。
