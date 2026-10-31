# OQ-094a 证明骨架

## 把"Scott ⟷ affine sector、Lawson ⟷ PGL₂"从 structural proposal 升级为定理

### Research Note v0.3

**2026-10-31**（v0.3：更正 v0.1/v0.2 对 `⟨Aff^+⟩` 的刻画——`⟨Aff^+⟩ = B_∞^+`（单位分量），不是全 `B_∞`；反射 `D_{-1} = T_1¬T_{-1}¬T_1¬` 必须借道 `¬`，故 `B_∞` 已含"对偶数据"）

---

## 0. 目标与定位

`10` §2 提出主对应（`structural proposal`）：

> "affine sector → PGL₂" 就是 "Scott → Lawson"；补上第二槽除法 `¬` = 补上对偶侧。

OQ-094a 问：这条对应能否升级为定理。本笔记给出**证明骨架**：写清精确命题，按地位分组给出引理，定位"装配"步骤，并落到**半群 / 群、单位分量 / 全 affine 群**这两重区分。地位约定沿用 `09` §0。

**本版要点**（相对 v0.1/v0.2 的更正）：

1. `⟨Aff^+⟩ = B_∞^+ = {ka+s : k>0, s∈ℝ}` 是 `B_∞` 的**单位分量**（正伸缩 + 全实平移），**不是**全 `B_∞`——全 `B_∞` 还含反射 `D_{-1}`。
2. `D_{-1} = T_1¬T_{-1}¬T_1¬`（引理 F）：反射**必须借道 `¬`** 才能从 `Aff^+` 造出（`D_{-1}` 的对角元为负，`⟨T_s, D_k(k>0)⟩` 的对角元恒正）。故 `B_∞`（paper-1 的 affine sector）**已含一块对偶数据**——这正是 `10` §2 "Scott ⟷ B_∞" 措辞不精确的根源。

---

## 1. 记号与对象

固定 `L = [0,∞]`（非负扩张实数，通常序；连续格），Scott 拓扑 `σ`、下拓扑 `ω`、Lawson 拓扑 `λ`。把 `L` 等同于 `P^1(ℝ)` 中正半线的闭包。生成元：

\[
T_s(a)=a+s\ (s\ge0),\qquad D_k(a)=ka\ (k>0),\qquad \neg(a)=\frac1a\ (0\leftrightarrow\infty),\qquad J=\neg\circ D_{-1}.
\]

五个对象：

- `Aff^+ := {a ↦ ka+s : k>0, s≥0}` —— **正 affine 半群**（对合成闭，对逆不闭）。
- `B_∞^+ := ⟨Aff^+⟩ = {a ↦ ka+s : k>0, s∈ℝ}` —— **`B_∞` 的单位分量**（`Aff^+` 的群闭包；补入 `T_{-s}=T_s^{-1}`，但不含反射）。
- `B_∞ := {a ↦ ka+s : k∈ℝ^×, s∈ℝ} = Stab_{PGL_2(ℝ)}(∞) ≅ Aff(1,ℝ)` —— **affine/Borel sector**（全群，`B_∞ = B_∞^+ ⊔ D_{-1}B_∞^+`）。
- `PGL_2(ℝ)`，Bruhat 分解 `PGL_2 = B_∞ ⊔ B_∞ ¬ B_∞`。

**关键关系**（平凡核对 / 引理 F）：

\[
\boxed{\ \operatorname{Aff}^+ = B_∞ \cap \operatorname{Stab}([0,∞]),\qquad \langle \operatorname{Aff}^+\rangle = B_∞^+,\qquad B_∞ = \langle \operatorname{Aff}^+, D_{-1}\rangle,\qquad \langle \operatorname{Aff}^+, \neg\rangle = \operatorname{PGL}_2.\ }
\]

- `Aff^+ = B_∞ ∩ Stab([0,∞])`：`ka+s` 保持 `[0,∞]` ⟺ `k>0` 且 `s≥0`。`REFORMULATION`。
- `⟨Aff^+⟩ = B_∞^+`：群闭包补 `T_{-s}` 得全实平移，`D_k` 仍 `k>0`，故 `{ka+s : k>0, s∈ℝ}`。对角元恒正，不含 `D_{-1}`。
- `B_∞ = ⟨Aff^+, D_{-1}⟩`：`B_∞^+ ⊔ D_{-1}B_∞^+`。
- `⟨Aff^+, ¬⟩ = PGL_2`：引理 F 给 `D_{-1}∈⟨Aff^+,¬⟩`，故 `B_∞ ⊆ ⟨Aff^+,¬⟩`，再由 Bruhat（引理 D）。

**两重区分**：

- **半群 vs 群**：序论只看得见 Scott 连续自映射（半群 `Aff^+`，`T_s` 不可逆）；群论闭包补逆得 `B_∞^+`。
- **单位分量 vs 全 affine 群**：`B_∞^+ = ⟨Aff^+⟩`（对角正）不含反射；全 `B_∞` 含 `D_{-1}`，而 `D_{-1}` 必须借道 `¬`（引理 F）。

---

## 2. 目标命题（升级后的定理陈述）

**Theorem (OQ-094a, 目标).** 在上述记号下：

1. **(Scott 侧 = 正 affine 半群)** `Aff^+` 是 `L` 上保序、保定向并（Scott 连续）的自映射半群；way-below 由 `T_s` 见证，Scott 基 `{↑↑a}` 恰为 `{T_s}` 的前向轨道之并。
2. **(对偶侧 = 互反)** `¬:(L,σ) → (L,ω)` 是同胚且 `ω = ¬_*σ`；`¬D_k¬ = D_{1/k}`，`¬T_s¬(a) = a/(1+sa)`。
3. **(Lawson = 双侧)** `λ = σ ∨ ¬_*σ`，且 `λ` 是 `[0,∞]` 上的欧氏拓扑。
4. **(群侧)** `B_∞ = ⟨T_b, D_a⟩`；`⟨Aff^+⟩ = B_∞^+`；`PGL_2 = B_∞ ⊔ B_∞¬B_∞`；故 `⟨Aff^+, ¬⟩ = ⟨B_∞, ¬⟩ = PGL_2`。
5. **(装配)** 两种"补上 `¬`"是同一构造：拓扑格中 `λ = σ ∨ ¬_*σ`（join）；子群格中 `PGL_2 = ⟨Aff^+, ¬⟩`（join）。二者以同一 `¬ = C_{/,1}^{(2)}` 为第二操作数，单侧基底 `Aff^+` 由 §1 的关系联系。

**结论措辞（细化 `10` §2）**：`Scott ⟷ Aff^+`（半群，或等价地其群闭包 `B_∞^+`）；`Lawson ⟷ PGL₂ = ⟨Aff^+, ¬⟩`；而 paper-1 的 affine sector `B_∞` 介于二者之间，**已含反射 `D_{-1}`（一块对偶数据）**，故 `10` §2 的 "Scott ⟷ B_∞" 应改作 "Scott ⟷ `Aff^+`（=`B_∞ ∩ Stab([0,∞])`）"。

---

## 3. 引理与证明

### 3.1 引理 A（正 affine 半群，`CLASSICAL`/平凡）

**命题**：`Aff^+ = {ka+s : k>0, s≥0}` 是半群；每个元保序、保定向并，故 Scott 连续。

**证明**：合成 `(ka+s)∘(k'a+s') = kk'a + (ks'+s)`，闭。保序 `a≤b ⟹ ka+s ≤ kb+s`。保定向并 `sup_i(ka_i+s) = k·sup_i a_i + s`。∎

**way-below 见证**（`CLASSICAL`，`09` §9.2）：`a≪b ⟺ a<b`（`a>0`），`0≪0`；故 `a≪b ⟺ ∃s>0: T_s(a)=a+s≤b`。

**Scott 基**（`CLASSICAL`）：`{↑↑a}`，`a>0` 时 `↑↑a = ⋃_{s>0}↑T_s(a) = (a,∞]`，`↑↑0=[0,∞]`。故 Scott 开集 = `{∅,[0,∞],(r,∞]}`，由 `{T_s}` 前向轨道生成。∎

### 3.2 引理 B（互反 = 对偶侧，`CLASSICAL`）

**命题**：`¬` 是 `[0,∞]` 上反序双射；作为序同构 `L→L^op` 给出同胚 `¬:(L,σ)→(L,ω)`，且 `ω = ¬_*σ`。共轭 `¬D_k¬ = D_{1/k}`，`¬T_s¬(a)=a/(1+sa)`。

**证明**：开集核对 `¬((r,∞]) = [0,1/r)`（下拓扑基本开集 `L∖↑(1/r)`），故 `¬_*σ=ω`。∎

### 3.3 引理 C（Lawson = 欧氏，`CLASSICAL`）

**命题**：`λ = σ ∨ ω` 是 `[0,∞]` 上的欧氏拓扑。**证明**见 `09` §10.3（`(r,∞]` ∪ `[0,b)` 生成欧氏）。∎

### 3.4 引理 D（Bruhat，`proved in paper-1`）

**命题**：`B_∞ = ⟨T_b, D_a⟩`（`cor:affine-borel-sector`）；`PGL_2 = B_∞ ⊔ B_∞J B_∞`；因 `J = D_{-1}¬`、`D_{-1}∈B_∞`，`B_∞JB_∞ = B_∞¬B_∞`。故 `⟨B_∞, ¬⟩ = PGL_2`。∎

### 3.5 引理 E（交集与群闭包，平凡核对）

**命题**：`Aff^+ = B_∞ ∩ Stab([0,∞])`；`⟨Aff^+⟩ = B_∞^+ = {ka+s : k>0, s∈ℝ}`。**证明**见 §1。∎

### 3.6 引理 F（反射须借道 ¬，`computationally verified example`）

**命题**：`D_{-1} = T_1 ∘ ¬ ∘ T_{-1} ∘ ¬ ∘ T_1 ∘ ¬`（射影类）。故 `D_{-1} ∈ ⟨Aff^+, ¬⟩` 但 `D_{-1} ∉ ⟨Aff^+⟩ = B_∞^+`；从而 `⟨Aff^+, ¬⟩ = PGL_2`。

**证明**：逐点合成（最右先）

\[
z \xrightarrow{\neg} \frac1z \xrightarrow{T_1} \frac{1+z}{z} \xrightarrow{\neg} \frac{z}{1+z} \xrightarrow{T_{-1}} \frac{-1}{1+z} \xrightarrow{\neg} -(1+z) \xrightarrow{T_1} -z = D_{-1}(z).
\]

矩阵核对：`T_1·¬·T_{-1}·¬·T_1·¬ = [[1,0],[0,-1]] ≡ [[-1,0],[0,1]]`（差标量 `-1`）。`D_{-1} ∉ ⟨Aff^+⟩`：`⟨T_s(s∈ℝ), D_k(k>0)⟩` 的元皆 `[[a,b],[0,1]]` 且 `a>0`（对角正），`D_{-1}` 对角为 `-1`。故 `⟨Aff^+,¬⟩ ⊇ B_∞^+ ∪ {D_{-1}} = B_∞`，再由引理 D 得 `⟨Aff^+,¬⟩ = PGL_2`。∎

---

## 4. 装配：两种"补上 ¬"是同一构造

- **拓扑格** `Top(L)`：`σ` 与 `ω=¬_*σ` 的 join `λ = σ ∨ ω` 是最粗双侧拓扑 = 欧氏（引理 C）。
- **子群格** `Sub(PGL_2(ℝ))`：`Aff^+`（群闭包 `B_∞^+`）与 `¬` 的 join `⟨Aff^+, ¬⟩ = PGL_2`（引理 F + D）。

\[
\sigma \xrightarrow{\ \vee\ } \sigma\vee\neg_*\sigma = \lambda
\qquad\longleftrightarrow\qquad
\operatorname{Aff}^+ \xrightarrow{\ \langle -,\neg\rangle\ } \langle \operatorname{Aff}^+,\neg\rangle = \operatorname{PGL}_2 .
\]

两侧第二操作数都是 `¬ = C_{/,1}^{(2)}`；单侧基底 `Aff^+` 由 `Aff^+ = B_∞ ∩ Stab([0,∞])`、`⟨Aff^+⟩ = B_∞^+`、`B_∞ = ⟨Aff^+, D_{-1}⟩` 精确联系。

**这给出 OQ-094a 可证的核心**：两种"补上 ¬"是**同型构造**（各自格中的 join、同一第二操作数、单侧基底由交集/群闭包联系），两侧"双侧 = Hausdorff / 全体"由引理 C、D 分别证明。

---

## 5. 残余：从"平行构造"到"函子等价"还缺什么

定理第 5 条目前是**平行性**，不是**严格范畴等价**。要升级为"存在函子 `Φ` 使 `Φ(σ∨¬_*σ) ≅ ⟨Φ(σ-side), ¬⟩`"，仍需闭合（`open problem`，不阻塞第 1–4 条）：

1. **半群 / 群与单位分量 / 全群的函子化**：序论侧对象是**半群** `Aff^+ ⊆ End_Scott(L)`；其群闭包是 `B_∞^+`（单位分量）；全 `B_∞` 需反射 `D_{-1}`，而 `D_{-1}` 借道 `¬`（引理 F）。函子 `Φ` 必须声明它把"Scott 侧"映到哪一层：`Aff^+`（半群）、`B_∞^+`（群闭包）、还是 `B_∞`（全 affine 群）。本骨架取 `Φ(σ-side) = Aff^+`，把"群闭包 `⟨-⟩`"与"借道 ¬ 得反射"都算作装配步骤——这与"拓扑 join 不需要逆/反射、群 join 需要"的区别对应。**已解决**（2026-10-31，`13-functorial-language-oq094a.md`）：`Φ` 是"生成数据 + 补 ¬"层面的自然变换（交换方阵），取 `Φ(σ) = C(σ)∩B_∞ = Aff^+`。
2. **Galois 连接框架**：`X` 上拓扑 `τ ↦ Homeo(X,τ)` 与 `G ⊆ Homeo(X) ↦ G`-不变拓扑构成 Galois 连接。要证 `¬` 在两侧同角色，需检查 `Homeo(L,σ)`（是否 = 序自同构群 ⊇ `D_k(k>0)`）、`Homeo(L,λ)` 的射影子群与 `B_∞^+`、`Stab([0,∞])`、`PGL_2` 的关系。**已解决**（2026-10-31，`12-galois-connection-oq094a.md`）：`Homeo(L,σ)∩PGL₂ = {D_k}`，`Homeo(L,λ)∩PGL₂ = Stab([0,∞]) = ⟨D_k,¬⟩`（自同胚层只到 `Stab([0,∞])`）；`Aff^+ = C(L,σ)∩B_∞`，`⟨Aff^+,¬⟩ = PGL₂`（自映射层到全 `PGL₂`）。两条 Galois 映射"补上 ¬ 交换"（`12` §3 主定理）。
3. **最小性在 Galois 连接下的保持**：`λ` 是最粗拓扑、`PGL_2` 是最小子群（两侧皆由 join/生成定义保证最小）；但"join 映 join"需随第 1、2 条一并建立。**已解决**（2026-10-31，`13-functorial-language-oq094a.md` §3）：交换方阵 + 自然性 `Φ(σ∨¬_*σ) = ⟨Φ(σ), ¬⟩` 即"join 映 join"的精确形式；且 `13` §4 证明对应**不是**全 Galois 等价（`A` 坍缩、`H` 过小、`E` 过大三条可证理由）。

**结论**：OQ-094a 的**可证核心与函子语言均已闭合**（`11` §2 + §4、`12` §3、`13` §3），精确边界为"生成数据 + 补 ¬ 层面的自然变换，而非全 Galois 等价"（`13` §4）。仅剩 094b–094d 各自 open。

---

## 6. 对 `10` §2 的细化

`10` §2 的 `⟨T_s, D_k, ¬⟩ = PGL_2` 在**群生成**意义下**正确**（引理 F 保证 `s≥0, k>0` 也群生成 `PGL_2`）。需要细化的有两处：

1. **`⟨T_s, D_k⟩ = B_∞` 不准**：`T_s(s≥0), D_k(k>0)` 的**半群**闭包是 `Aff^+`，其**群**闭包是 `B_∞^+ = {ka+s : k>0}`（单位分量），二者都不含反射 `D_{-1}`。全 `B_∞ = B_∞^+ ⊔ D_{-1}B_∞^+` 需要 `D_{-1}`。
2. **反射 `D_{-1}` 是"对偶数据"**：`D_{-1} = T_1¬T_{-1}¬T_1¬`（引理 F），所以它借道 `¬` 才进得来。因此 paper-1 的 affine sector `B_∞` **已含一块对偶结构**，不是纯"序单侧"对象；纯序单侧是 `Aff^+`（或 `B_∞^+`）。

故 `10` §2 的核心断言（"Scott → Lawson" = "affine → PGL₂"）**成立**，只需把"Scott 侧"的载体从 `B_∞` 改为 `Aff^+`（=`B_∞ ∩ Stab([0,∞])`），并指出 `B_∞` 的反射 `D_{-1}` 已经是对偶数据。§2 的目标命题已按此写就。

---

## 7. 地位总表

| 命题 | 地位 |
|---|---|
| §1 记号、`Aff^+ = B_∞ ∩ Stab([0,∞])`、`⟨Aff^+⟩ = B_∞^+` | `REFORMULATION` + 平凡核对 |
| §2.1–2.2 Scott 侧、对偶侧 | `CLASSICAL`（`09` §9 实例化）|
| §2.3 Lawson = 欧氏 | `CLASSICAL` |
| §2.4 Bruhat / `⟨B_∞,¬⟩=PGL_2` | `proved in paper-1` |
| §3.6 引理 F（`D_{-1}=T_1¬T_{-1}¬T_1¬`，及 `D_{-1}∉⟨Aff^+⟩`）| `computationally verified example`（逐点 + 矩阵核对 + 对角不变式）|
| §2.5 装配（平行 join）| `structural proposal`（两侧 join 各自已证，对应为精确平行性）|
| §5 残余（层级函子化、Galois 连接、join 保持）| `open problem` |

---

**参考**（沿用 `09`）：

1. D. Scott, *Continuous lattices*, LNM 274, Springer (1972).
2. G. Gierz et al., *A Compendium of Continuous Lattices*, Springer (1980).
3. M.W. Warner, *Fuzzy topology with respect to continuous lattices*, Fuzzy Sets and Systems 35 (1990) 85–91.
4. `paper-1/sections/03-projective-affine.tex`（`cor:affine-borel-sector`、`thm:bilateral-pgl2-generation`、Bruhat 分解）。
