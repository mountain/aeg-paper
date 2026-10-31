# OQ-094a §5.1/§5.3：函子语言的完成

## 把 Scott/Lawson ↔ affine/PGL₂ 对应写成函子（并诚实标出它不是全 Galois 等价）

### Research Note v0.1

**2026-10-31**（v0.1：闭合 `11` §5.1/§5.3 与 `12` §5 的函子化残余；给出三个射影限制函子、交换方阵，并证明对应是"生成数据的自然同构"而非全 Galois 等价）

---

## 0. 目标与结论预告

`12` 证明了"补上 ¬"在对象 `σ, λ` 上交换。本笔记完成**函子语言**：写清环境 Galois 连接、三个射影限制函子、交换方阵，并精确定位对应在哪一层是函子、在哪一层不是。

**结论预告**（三条）：

1. 环境是自映射上的反调 Galois 连接 `C ⊣ Top`（`τ ↦ C(τ)` = 连续自映射幺半群）。它限制到射影映射给出三个函子 `E, A, H`。
2. 三个函子在 `σ, λ` 上的值是精确可算的（下表），其中只有 `A(σ) = Aff^+` 是能经"补 ¬"到全 `PGL₂` 的**最小典范** Scott 侧对象。
3. **对应是一个"生成数据 + 补 ¬"层面的自然同构（交换方阵），不是全 Galois 等价**——因为 `A` 不区分 `σ` 与 `λ`、`H` 只到真子群 `Stab([0,∞])`、`E` 的像过大（含 ¬-共轭）。这是函子语言能完成的**最精确**形式。

---

## 1. 环境：自映射上的反调 Galois 连接

设 `L = [0,∞]`。记 `Map(L)` 为 `L` 的全部自映射。定义

- `C(τ) := {f ∈ Map(L) : f 是 (L,τ)→(L,τ) 连续}`（`τ` 的**自映射幺半群**）；
- `Top(S) :=` 使 `S ⊆ C(τ)` 的**最粗**拓扑 `τ`（`S` 的初始拓扑）。

这是反调 Galois 连接：

\[
S \subseteq C(\tau)\ \Longleftrightarrow\ \operatorname{Top}(S) \subseteq \tau .
\]

`CLASSICAL`（初始拓扑 / Galois 连接的标准事实）。两侧闭包 `Top∘C` 与 `C∘Top` 给出 Galois 闭对象。

**射影限制**：`PGL_2(ℝ)` 以 Möbius 映射作用于 `P^1(ℝ) ⊃ L`；`B_∞ = Stab(∞)` 是仿射子群。定义三个函子（`Top(L) → Sub(PGL_2)` 或 `Sub(B_∞)`，均反调）：

\[
E(\tau) := C(\tau) \cap \operatorname{PGL}_2(\mathbb R),
\qquad
A(\tau) := C(\tau) \cap B_∞,
\qquad
H(\tau) := \operatorname{Homeo}(L,\tau) \cap \operatorname{PGL}_2(\mathbb R).
\]

（`Homeo ⊆ C`，故 `H(τ) ⊆ E(τ)`；`A(τ)` 是 `E(τ)` 的仿射部分。）

---

## 2. 三个函子在 `σ, λ` 上的精确值（全可证）

沿用 `11`/`12` 的记号与引理：

| 函子 | `τ = σ`（Scott）| `τ = λ`（Lawson）| 证据 |
|---|---|---|---|
| `A(τ) = C(τ)∩B_∞` | `Aff^+ = {ka+s : k>0, s≥0}` | `Aff^+`（同值）| `12` §2.1；仿射自映射不区分 σ/λ |
| `E(τ) = C(τ)∩PGL₂` | 非负系数且 `det>0` 的 Möbius 映射 | 非负系数 Möbius 映射（全 det）| `12` §2.2/2.3 的推广 |
| `H(τ) = Homeo∩PGL₂` | `{D_k : k>0}` | `Stab([0,∞]) = {D_k, D_k¬}` | `12` §2.2/2.3 |

关键观察（本笔记新内容）：

- **`A(σ) = A(λ) = Aff^+`**：仿射 Scott 连续自映射与仿射 Lawson 连续自映射是同一集合（`ka+s`，`k>0, s≥0`）。故 `A` **单独不探测双侧性**。
- **`H(σ) = {D_k}`, `H(λ) = Stab([0,∞])`**：`H` 探测到双侧性（补入 `¬` 使自同胚从 `{D_k}` 扩到 `Stab([0,∞])`），但**只到真子群**（丢掉了不可逆平移 `T_s`）。
- **`E(σ) ⊋ Aff^+`**：`E(σ)` 含 ¬-共轭（如 `¬T_s¬(a)=a/(1+sa)`，递增、非负系数、det>0），故 `E(σ)` 不是"纯单侧"对象。

于是"能经补 ¬ 到全 `PGL₂` 的**最小典范** Scott 侧对象"是 `A(σ) = Aff^+`（仿射部分），不是 `E(σ)`（过大）也不是 `H(σ)`（过小）。

---

## 3. 交换方阵：函子语言的核心

**Theorem (函子语言).** 令 `S_0 := {T_s : s≥0} ∪ {D_k : k>0}`（= `Aff^+` 的生成集）。两侧"补上 ¬"构成**交换图**：

\[
\begin{array}{rccc}
\text{拓扑侧：} & \sigma\ \ (\text{由}\ \{\mathord{\uparrow\uparrow} a\}=\{\textstyle\bigcup_{s>0}\uparrow T_s(a)\}\ \text{生成})
  & \xrightarrow{\ \text{补上}\ \neg:\ \tau\mapsto\tau\vee\neg_*\tau\ }
  & \lambda = \sigma\vee\neg_*\sigma \\[2pt]
  & \Big\uparrow \Phi & & \Big\uparrow \Phi \\[2pt]
\text{群侧：} & \operatorname{Aff}^+ = \langle S_0\rangle\ (=C(\sigma)\cap B_∞)
  & \xrightarrow{\ \text{补上}\ \neg:\ S\mapsto\langle S,\neg\rangle\ }
  & \operatorname{PGL}_2 = \langle \operatorname{Aff}^+,\neg\rangle
\end{array}
\]

其中对应 `Φ` 由生成元识别给出：`Φ(σ) = C(σ)∩B_∞ = Aff^+`，`Φ(λ) = ⟨C(σ)∩B_∞, ¬⟩ = PGL₂`，且满足**自然性**

\[
\Phi\big(\sigma \vee \neg_*\sigma\big) = \big\langle \Phi(\sigma), \neg \big\rangle .
\]

**证明**（全由前序笔记拼合）：

- 左上：`σ` 由 `{↑↑a}` 生成，`↑↑a = ⋃_{s>0}↑T_s(a)`（`09` §9.2：way-below 由加法见证）。`REFORMULATION`/`CLASSICAL`。
- 左下：`Aff^+ = ⟨S_0⟩_{半群} = C(σ)∩B_∞`（`12` §2.1）。`REFORMULATION`/`proved`。
- 顶行（补 ¬）：`λ = σ ∨ ¬_*σ`（`11` 引理 B/C）。`proved`。
- 底行（补 ¬）：`PGL_2 = ⟨Aff^+, ¬⟩`（`11` 引理 F + Bruhat）。`proved`。
- 自然性：`Φ(λ) = ⟨Aff^+, ¬⟩ = ⟨Φ(σ), ¬⟩`（代入）。∎

**一句话**：拓扑侧"补 ¬"（`τ ↦ τ ∨ ¬_*τ`）与群侧"补 ¬"（`S ↦ ⟨S, ¬⟩`）是**同一生成集 `S_0` 上的两个闭包运算**，在对应 `Φ` 下交换——这就是 `11` §4"平行构造"的函子化精确形式。

---

## 4. 诚实边界：为什么**不是**全 Galois 等价

函子语言完成到 §3 为止是**精确且可证的**。但它**不是** `Top(L)` 与 `Sub(PGL₂)` 之间的 Galois 等价，原因是三个函子各有缺陷（均为可证事实）：

1. **`A` 不单射**：`A(σ) = A(λ) = Aff^+`，故 `A` 把 `σ`、`λ` 坍缩为同一值。`A` 只能给出"Scott 侧"的载体，不能探测双侧性。
2. **`H` 探测双侧性但射程过小**：`H(λ) = Stab([0,∞]) ⊊ PGL₂`，因为平移 `T_s` 不是自同胚。`H` 给的是"自同胚层"的对应（`12` §3 自同胚层），到不了 `PGL₂`。
3. **`E` 的像过"大"**：`E(σ)` 已含 ¬-共轭（`¬T_s¬`），不是纯单侧；`E` 不能给出"最小 Scott 侧"。

故**不存在**单个函子 `Top(L) → Sub(PGL₂)` 同时满足：把 `σ` 映到"最小 Scott 侧"、把 `λ` 映到 `PGL₂`、且在 `σ, λ` 上单射。对应本质上是**"生成集 + 补 ¬"两个闭包运算之间的自然变换**（§3 的交换图），而非对象层面的 Galois 等价。

**可证的正结论**（这就是"函子语言的完成"）：存在一个**在生成数据层定义的函子** `Φ : P(S_0 ∪ {¬}) →` （对应闭对象），它把每个生成子集 `S ⊆ S_0 ∪ {¬}` 同时映到它的拓扑闭包（Scott/Lawson）与群闭包，且**这两个闭包在 `Φ` 下交换**；`Φ` 的取值在 `S_0 ↦ (σ, Aff^+)`、`S_0∪{¬} ↦ (λ, PGL₂)` 两处给出主对应。这是完整、可证、且**不越界**（不声称全 Galois 等价）的函子语言。

---

## 5. 地位总表

| 命题 | 地位 |
|---|---|
| §1 `C ⊣ Top` 反调 Galois 连接 | `CLASSICAL` |
| §2 三函子 `E,A,H` 在 `σ,λ` 上的值 | `proved with stated hypotheses`（`12` §2 各引理 + 平凡核对）|
| §2 关键观察（`A` 坍缩、`H` 过小、`E` 过大）| 平凡核对 + `computationally verified example` |
| §3 交换方阵 + 自然性 `Φ(σ∨¬_*σ)=⟨Φ(σ),¬⟩` | `proved`（拼合 `09`/`11`/`12`）|
| §4 非 Galois 等价的三条理由 | `proved`（反例：`A(σ)=A(λ)`、`T_1∉Stab([0,∞])`、`¬T_s¬∈E(σ)∖Aff^+`）|

---

## 6. 收尾：OQ-094a 的最终状态

至此 OQ-094a（"Scott ⟷ affine sector、Lawson ⟷ PGL₂ 能否升级为定理"）的函子语言**完成**：

- **可证核心**（`11` §2 的 1–4 条 + `12` §3 的 Galois 交换 + 本笔记 §3 的交换方阵）：`Scott ⟷ Aff^+`、`Lawson ⟷ PGL₂`、"补 ¬"逐点交换——**全部有证明或机器核对**。
- **精确边界**（本笔记 §4）：对应是"生成数据 + 补 ¬"层面的自然变换，**不是**全 Galois 等价（三条可证理由）。
- **残余**（仅剩表述性，不再阻塞）：若坚持要一个 `Top(L) → Sub(PGL₂)` 的函子等价，必须先"扩大"群侧对象（用含不可逆元的幺半群/半群，而非子群格）——但这已超出"把 paper-1 的 affine sector 读回拓扑"的需求；主对应本身已闭合。

**建议**：OQ-094a 可从 `PARTIALLY RESOLVED` 提升为 `RESOLVED`（可证核心 + 精确边界均已给出）；剩余 094b–094d 仍各自 open。

---

**参考**（沿用 `09`/`11`/`12`）：

1. D. Scott, *Continuous lattices*, LNM 274, Springer (1972).
2. G. Gierz et al., *A Compendium of Continuous Lattices*, Springer (1980).
3. M.W. Warner, *Fuzzy topology with respect to continuous lattices*, Fuzzy Sets and Systems 35 (1990) 85–91.
4. `paper-1/sections/03-projective-affine.tex`；`notes/analysis-and-calculus/11-oq094a-proof-skeleton.md`、`12-galois-connection-oq094a.md`。
