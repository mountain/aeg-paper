# 分支层的 S：左优先 postorder = 线性扩张，S = 沿典范 spinal history 前进

## 修正 note 35 的序混淆，并给出分支层 shift

### Research Note v0.1 · 2026-11-01

**核心结果**：note 35 把"左遍历"当成了 **preorder**（根先），而**求值/时序**是 **postorder**（子先）。纠正后：

> **左优先 postorder 对任意 PPCT 都是依赖偏序的线性扩张**（已计算验证 $n\le5$ 全部），且对**左梳、右梳都等于时序序**（`[2,1,0]`）。
>
> 所以**分支层 S = "左优先 postorder 的后继" = "沿典范（左优先）spinal history 前进"**。它同时是**遍历**与**求值序**，是 planar（左优先）且 unbounded 的，且是 AEG 原生对象（`thm:birkhoff-downset-spinal` 的极大链 = spinal history）。

---

## 0. 目标

note 35 把 `S` 接成"时序后继"，但分层精确性（左梳精确、右梳差翻转、分支层分道）。本笔记**推导分支层的 `S`**。

---

## 1. 三个序必须分清（note 35 的混淆在此）

对一棵 PPCT（内部点的依赖偏序：$u\preccurlyeq v$ ⟺ $u$ 是 $v$ 的后代）：

| 序 | 定义 | 是否线性扩张 | 备注 |
|---|---|---|---|
| **preorder**（先根）| 根、左、右 | **否**（根先，违反"子先父"）| note 35 的"左遍历"用的这个 → **反了** |
| **postorder**（后根）| 左、右、根 | **是**（子先父）| **= 求值序** |
| 线性扩张 | 任意合法求值序 | 是 | = spinal history（`~O(P)` 极大链）|

**关键**：note 35 的"左梳 DFS = 脊序 = 时序"用的是 **preorder**（顶到底），它其实是时序的**反序**；正确的"时序"= **postorder**（底到顶）。

---

## 2. 核心事实：左优先 postorder 是线性扩张（已计算）

对 $n=3,4,5$ 的**全部** PPCT，计算左优先 postorder 并检查"$u$ 是 $v$ 后代 ⟹ $u$ 在 $v$ 前"：

- $n=3$：2/2 成立；
- $n=4$：5/5 成立；
- $n=5$：14/14 成立。

**全部是线性扩张。**（`research/iota-carousel/verify_branching_shift.py`）

**并对左梳、右梳**：左优先 postorder 都是 `[最内, …, 根]` = **时序序**（左梳 `N(N(N(L,L),L),L)`、右梳 `N(L,N(L,N(L,L)))` 都给出 `[2,1,0]`）。

---

## 3. 分支层 S = postorder 后继

**定义**：对 PPCT $T$，令 $\mathrm{hp}(T)$ = 左优先 postorder 的内部点序列。由 §2，它是依赖偏序的**线性扩张**，即一条 **spinal history**（$\mathcal O(P)$ 的极大链，`thm:birkhoff-downset-spinal`）。

**定义（分支层 shift）**：
$$
S:\ \text{postorder 位置 } i \mapsto i+1
$$
即"**沿典范（左优先）spinal history 前进一位**"。

**性质**：
- **线性扩张**：$S$ 走的是合法求值序（§2）；
- **planar**：左优先（用左/右结构决定 visit 次序）；
- **unbounded**：位置 $i$ 无界（随树增大）；
- **AEG 原生**：$\mathrm{hp}(T)$ 就是一条 spinal history。

---

## 4. 与 note 34 螺旋的衔接

note 34 的螺旋模 `V = V_class ⊗ V_index`，`S` 取"`V_index` 层前进"。分支层把 `V_index` 具体化为 **postorder 位置**，即：

$$
S\ =\ \text{“沿 } \mathrm{hp}(T) \text{ 前进一位”}\ =\ \text{AEG 的“取该 spinal history 的下一事件”}.
$$

`[J,S]=0`、`C⁴=S`、`J⁴=id` 保持（`S` 只动 postorder 位置，`J` 只动类）。

---

## 5. 诚实的对应（残余）

- **carousel 的 `k` 是"角/遍历位置"**（Thm 4.2 的 "left natural traversal"），而 **postorder 是"内部点求值序"**；**角/叶**与**内部点**是两类对象。二者"第 k 个"的**逐点对应**（角序 vs 求值序）**尚未逐项建立**——这是真正的残余。
- 但**"postorder 既是遍历又是线性扩张"**这一事实（§2）说明：**"遍历"与"时序"之间确有桥**（postorder），所以 note 35 的"分道"不是绝对的，而是"preorder vs postorder"的混淆。
- **右优先 postorder** 是另一条典范 spinal history（另一平面选择）；carousel 取"左优先"。

---

## 6. 地位与残余

| 命题 | 地位 |
|---|---|
| §1 preorder 非线性扩张、postorder 是 | `CLASSICAL`（定义即证）|
| §2 左优先 postorder 是线性扩张（n≤5 全部）| `COMPUTATIONALLY VERIFIED EXAMPLE` |
| §2 对左梳/右梳等于时序序 | `COMPUTATIONALLY VERIFIED EXAMPLE` |
| §3 分支层 S = postorder 后继 = 沿 spinal history 前进 | `[对应]`（构造 + 验证）|
| §5 carousel 的"角序" ↔ "postorder 求值序" | **open**（真正的残余）|

**残余（`open`）**：
1. **角序 ↔ 求值序**：把 carousel 的"第 k 个 LL/RL/RN/LN"与 postorder 的第 k 个内部点**逐点对齐**（需要 Thm 4.2 的精确遍历定义）。
2. **右优先 vs 左优先**：两条典范 spinal history；carousel 用左优先，右优先是镜像——这是平面选择，需固定。
3. **一般 `n` 的严格证明**：`S` = postorder 后继 与 `C⁴=S` 的严格形式化。
4. **与 note 29 的关系**：note 29 说 τ 不下降到 $O(P)$；而 postorder 是 $O(P)$ 的极大链。所以"下降"的障碍是"多值"（一条 $P$ 有多条极大链），而 **"选一条典范链（左优先 postorder）"恰是"下降的有值化"**——这可能是化解 note 29 障碍的一条路。

---

## 7. 参考

- AEG：`paper-1/sections/02-sequential-histories.tex`（`def:internal-dependency-poset`、`thm:sequential-tree-classification`、`thm:birkhoff-downset-spinal`）。
- carousel：Pushkarev–Byzov 2014 Thm 4.2 / 4.3 / Cor 4.4。
- 计算：`research/iota-carousel/verify_branching_shift.py`；`verify_traversal.py`（note 35）。
- 相关：note 29（下降障碍）、34（螺旋模）、35（S 的初导出）；OQ-098.3。
