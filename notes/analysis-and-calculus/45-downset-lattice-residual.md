# 098.2 残余：`O(P)` 与无限二叉树下集格——是"格商"而非"子格"；并修正"标准格序"的含义

## OQ-098.2 推进（note 28 的残余收口）

### Research Note v0.1 · 2026-11-01

**结论**：
1. **修正 note 28**：Pushkarev–Byzov §5 的"**standard lattice ordering of all trees**"由同一句的括号**自我解释**为"**distributive lattice**"——即**下集格序**，**不是 Tamari**（note 28 曾按"最可能 = Tamari"处理）。
2. **该分配格 = `Down(T_∞)`**：无限二叉树 `T_∞` 的下集格；元素是 **0/1/2 子有序二叉树（plane forests）**，经 rotation 双射与 PPCT 对应（二者**不是同一集合**，note 28 §2）。
3. **`O(P)` 与 `Down(T_∞)` 的精确关系**：`O(P)=Down(P)` 是 `Down(T_∞)`（的有限截断）的**格商（lattice quotient）**——restriction `S↦S∩P` 是**满射格同态**；但它**不是 `Down(Q)` 的包含子格**（`Down(P) ⊄ Down(Q)`）。故 "quotient"版本为**真**；"以包含方式成为子格"为**假**；而 note 28 残余所问的**抽象子格嵌入**仍 **open**（已计算验证的是非包含，`n≤7` 节点）。

---

## 0. 目标

OQ-098.2 残余（note 28 §6）：
1. `O(P)` 与 `Down(T_∞)` 的精确关系（是否"$P$ 嵌入 $T_∞$ 的子偏序使 $\mathcal O(P)$ 为子格"）？
2. "standard lattice ordering of all trees"的精确出处/含义。

---

## 1. 精确原文（OCR，pb-09）与修正

Pushkarev–Byzov 2014 §5 开头（OCR 逐字）：

> "The hyperbolicity of a transformation means that a small change in the initial point drastically changes the result after several iterations of the transformation. In our case this means that the transformation is **not monotone with respect to the standard lattice ordering of all trees** (**recall that the PPCTs form a distributive lattice whose irreducible elements are ordered as the vertices of the infinite cubic tree**)."

**读法**：括号紧接"standard lattice ordering"，是在**解释**它——即"标准格序"= **那个分配格的序**。所以：

> **"standard lattice ordering" = 分配（下集）格序，不是 Tamari 旋转格。**

**修正 note 28**：note 28 §3 把"standard = Tamari"作为"最可能"读法、并据此断言"论文混用 (A) 与 (B)"。现在原文显示：**作者用括号把"standard"锚定到"distributive"**。两种可能：
- **(i) 作者的"standard"确指下集格**（按 OCR 的最自然读法）→ 无"混用"，note 28 的"standard = Tamari"是误读；
- **(ii) 作者的"standard"指 Tamari**，则"distributive"是**错误**（Tamari 非分配，note 28 §1 已算 $T_4$ 见证）。

**两种情况下，"distributive lattice whose irreducibles are the cubic-tree vertices" 都精确等于 `Down(T_∞)`**（Birkhoff）。所以"混用"风险仍应标注，但**"标准格序"的最诚实含义 = 下集格序**。

---

## 2. 这个"分配格"是什么：`Down(T_∞)`

- `T_∞` = 无限二叉树（每点 2 子；按"后代 $$\preceq$$ 祖先"或反之，取一个定向）。
- `Down(T_∞)` = `T_∞` 的**下集**（order ideal）按包含的格。
- **Birkhoff**：`Down(T_∞)` 是分配格；**并不可约元 = 主下集 `↓v`**，按包含排序与 `T_∞` 同构——正是原文"irreducible elements are ordered as the vertices of the infinite cubic tree"。
- **元素 = 0/1/2 子有序二叉树**（"plane forests"）：每点 0/1/2 子，闭于祖先。计数 `R(N)=C_N`（Catalan）。
- **与 PPCT 的关系**：PPCT 是**全**二叉树（每内部点 2 子），经"rotation"双射与"0/1/2 子有序二叉树"对应。**两者都 Catalan 计数，但不同集合。**

> 所以原文"the **PPCTs** form a distributive lattice"是**措辞宽松**：真正形成分配格的是 **down-sets（0/1/2-子树）**；PPCT 经 rotation 与之对应。

---

## 3. `O(P)` 与 `Down(T_∞)`：格商，非子格（已计算）

`P` = 二叉树依赖偏序 = **有限二叉树偏序** ⟹ `P` 序嵌入 `T_∞`（作有限子树）。取 `Q ⊂ T_∞` 为含 `P` 的有限子树。

**restriction 映射**
$$
\rho:\ \mathrm{Down}(Q)\longrightarrow \mathrm{Down}(P),\qquad S\longmapsto S\cap P .
$$

**计算（`research/iota-carousel/verify_downset_quotient.py`，`Q` = 高度 2 的二叉树，7 节点，26 个下集）**：

| `P` | `#Down(P)` | `ρ` 满射 | 保 `∪` | 保 `∩` | `Down(P) ⊆ Down(Q)`（字面子格）|
|---|---|---|---|---|---|
| `V`（根+2子）| 5 | ✓ | ✓ | ✓ | ✗ |
| `chain 3<1<0` | 4 | ✓ | ✓ | ✓ | ✗ |
| `L`（1→0, 2→0, 3→1）| 7 | ✓ | ✓ | ✓ | ✗ |
| `根+2子, 左有2子` | 11 | ✓ | ✓ | ✓ | ✗ |

**结论**：
$$
\boxed{\mathcal O(P)=\mathrm{Down}(P)\ \text{是}\ \mathrm{Down}(T_\infty)\ \text{的格商（限制映射的满射同态像），且不是}\ \mathrm{Down}(Q)\ \text{的包含子格。}}
$$

这里能证明的是"**非包含子格**"（$\mathrm{Down}(P)\not\subseteq\mathrm{Down}(Q)$）；它不排除 $O(P)$ 作为抽象格**嵌入**某个 $\mathrm{Down}(Q)$。后者正是 OQ-098.2 原来的问题，仍 open（见 §5 残余 1）。

**理由**：
- `ρ` 满射：对任意 `P` 的下集 `S'`，取 `S'` 在 `Q` 中的下闭包 `↓_Q(S') = {q∈Q : q≤s 对某 s∈S'}`；它是 `Q` 的下集且 `↓_Q(S') ∩ P = S'`（因 `P` 序嵌入、`S'` 对 `P` 下闭）。注意不能用 `↓_{T_∞}(S')`——它一般不在 `Q` 内。
- `ρ` 保 `∪,∩`：`(S∪T)∩P=(S∩P)∪(T∩P)`、`(S∩T)∩P=(S∩P)∩(T∩P)`。
- **非包含子格**：`P` 的下集（如 `{a}`）一般**不是** `Q` 的下集（`Q` 中有下方元素），故 `Down(P) ⊄ Down(Q)`。这只排除了"以包含方式成为子格"，不排除抽象嵌入。

---

## 4. 对 note 28 残余的收口

| note 28 残余 | 本轮结论 |
|---|---|
| 1. `O(P)` 与 `Down(T_∞)` 的精确关系 | **格商（restriction），非包含子格**（§3，已验）；抽象嵌入 open |
| 2. "standard lattice ordering"的出处 | **= 下集格序（分配），非 Tamari**（§1，OCR）|
| 3. 098.1(b) 的提升 | 仍 open（见 note 29 与 note 41）|

**为什么"商"而非"子格"是自然的**：`O(P)` 是"给定计算 DAG 的偏序"的下集格，`Down(T_∞)` 是"万有（无限二叉树）"的下集格。给定 `P ↪ T_∞`，`O(P)` 自然作为 `Down(T_∞)` 的**商**（按"限制到 `P`"）出现，而不是作为子格——因为下集是"相对于某个偏序"的概念，`P` 的下集不是 `T_∞` 的下集。

---

## 5. 地位与残余

| 命题 | 地位 |
|---|---|
| §1 OCR 原文；"standard"由括号解释为"distributive" | `CLASSICAL`（原文）|
| §1 "standard = 下集格序，非 Tamari"（修正 note 28）| `[对应]` `structural proposal`（措辞澄清）|
| §2 该分配格 = `Down(T_∞)`；元素 = 0/1/2-子树 | `CLASSICAL`（Birkhoff + Catalan）|
| §3 `O(P)` 是 `Down(T_∞)` 的格商，非包含子格 | **`PROVED`（集合论）+ `COMPUTATIONALLY VERIFIED EXAMPLE`** |
| §3 抽象嵌入：`O(P)` 是否嵌入某个 `Down(Q)` 作子格 | **`OPEN`**（本笔记未回答）|

**残余（`open`）**：
1. **抽象子格嵌入（OQ-098.2 原问题）**：`O(P)` 是否作为抽象格嵌入某个 `Down(Q)`？非包含只排除了一种实现；完整嵌入问题仍 open。"quasi-sublattice" 的精确条件（如 `P` 为 `Q` 的上闭子偏序）也未有完整刻画。
2. **"standard lattice ordering"的原始出处**：Donaghey 1980 并无"distributive lattice"（只引 Huang–Tamari "lattice property"）；PB 的"standard"指什么、引自何处，仍需查更早文献。
3. **对偶方向**：`O(P)` 是否也是 `Down(T_∞)` 的**同态像**的更细结构（如"Galois 连接"）？
4. **098.1(b) 的提升**：`τ`（Tamari 格上）是否在 `O(P)` 的**商结构**上留下痕迹？（仍 open。）

---

## 6. 参考

- Pushkarev–Byzov 2014 §5（OCR，pb-09）；Donaghey 1980（无"分配格"表述）。
- AEG：`paper-1/sections/02-sequential-histories.tex`（`thm:birkhoff-downset-spinal`）。
- 计算：`research/iota-carousel/verify_downset_quotient.py`；`research/ppct-lattice/`。
- 相关：note 28（格归属）、note 15（branching dcpo）、note 41（大收束）；OQ-098.2。
