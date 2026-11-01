# 角序 ↔ 求值序的对齐：叶上一致、非叶链内反转、跨链是选择

## 修正 note 36 的"S = postorder"，并把 align 精确化（OCR 原文 + 计算）

### Research Note v0.1 · 2026-11-01

**结论**：从 Pushkarev–Byzov 原文（OCR）确认——**"corner"其实是顶点**（SR/LL/RL/LN/RN 是顶点分类），**left standard traversal = preorder**（先自身、再左子树、再右子树）。于是 **carousel 的 `k` 是按 preorder 编号的"角序"**，而 **求值序是 postorder**。两者的对齐（= 原文 Remark）为：

> **叶上两者一致（preorder = postorder = 左→右叶序）；非叶链内两者相反（preorder = postorder⁻¹）；跨不可比链的相对序是"选择"（不典范）。**

**对 `S` 的修正/细化**：carousel 的 `k` 是**角序（preorder）位置**，故分支层 `S` 应取 **"preorder 后继"（角序后继）**；note 36 取的 **postorder 是"求值序"**，它只在**叶（LL/RL）**上与 `k` 一致，在**非叶（LN/RN）**上是 `k` 的**逆**。

---

## 0. 目标

把 carousel 的"角序"（Thm 4.2 的 left natural traversal）与 postorder 的"求值序"**对齐**（note 36 的残余）。

---

## 1. 精确定义（OCR 原文）

- **"corner"= 顶点**（不是"角形"）。原文 §4："We can consider a more detailed classification of **nonroot vertices** of a PPCT ... the one-element class consisting of the son of the root (**SR**); the left leaves (**LL**); the right leaves (**RL**); the left and right nonleaves (**LN, RN**)."
  （"corners" 是 **PPT（非三叉树）** 的概念，分 left/right/lower/flat；PPCT 这边分的是**顶点**。）
- **left standard traversal = preorder**：原文 Thm 4.2 前："arriving at a vertex a, we first visit this vertex, then the tree of its left descendants, and, finally, the tree of its right descendants."
- **Thm 4.2**：left natural traversal = **standard left traversal（preorder）**。
- **Thm 4.3**：在 T 上用 **standard left traversal（preorder）** 给顶点编号（`k`-th LL/RL/LN/RN）；在 T' 上用 **right inverse traversal**。

---

## 2. 原文 Remark（对齐的核心）

> "the traversals under consideration **coincide on the set of leaves**, because leaves are always incomparable, i.e., no leaf is a descendant of another one. On the other hand, right (respectively, left) nonleaves form right (respectively, left) **chains** the order of vertices in which ... is **inverted** under each transformation."

即：
- **叶**：不可比 ⟹ 遍历序一致（左→右叶序）；
- **非叶**：形成**链** ⟹ 链内序**反转**；
- **跨链**：不可比 ⟹ 相对序由遍历决定（**选择**）。

---

## 3. 计算验证（`research/iota-carousel/verify_corner_order.py`）

| 树 | 叶序 preorder = postorder | 非叶 preorder = reverse(postorder) |
|---|---|---|
| 左梳 `N(N(N(L,L),L),L)` | ✓ | ✓（链）|
| 右梳 `N(L,N(L,N(L,L)))` | ✓ | ✓（链）|
| 平衡 `N(N(L,L),N(L,L))` | ✓ | **✗（跨链，非全局反转）** |

**平衡树**：preorder 非叶 `[root, L, R]`，postorder `[L, R, root]`，reverse = `[root, R, L]` ≠ preorder。**正是"跨链是选择"**。

---

## 4. 对齐结论

设 `角序` = 左标准遍历（preorder），`求值序` = postorder（依赖偏序的线性扩张）。则

$$
\text{求值序} \;=\; \begin{cases}
\text{角序} & \text{在叶（LL, RL）上},\\[2pt]
\text{角序}^{-1} & \text{在非叶链（LN, RN）内},\\[2pt]
\text{未定（选择）} & \text{跨不可比链}.
\end{cases}
$$

**这就是"角序 ↔ 求值序"的精确对齐**（原文 Remark + 计算）。

---

## 5. 对 `S` 的修正（note 36）

- note 36 取 `S` = **postorder 后继**（求值序）。但 carousel 的 `k` 是 **preorder（角序）** 位置。
- **正确**的分支层 `S` = **"preorder 后继"（角序后继）**——它才是 carousel 的 `k` 的"前进"。
- **postorder（求值序）** 与 `S` 的关系 = §4 的分段：**叶上一致、非叶链内相反、跨链选择**。
- 因此：**`S` = 角序后继（preorder）**；它是"遍历"（planar、左优先、unbounded），但**不是**线性扩张（preorder 非求值序）。"求值序"是 postorder，只在叶上与 `S` 一致。

---

## 6. 地位与残余

| 命题 | 地位 |
|---|---|
| §1 corner=顶点；left standard traversal=preorder | `CLASSICAL`（Pushkarev–Byzov 原文，OCR）|
| §2 Remark：叶上一致、非叶链内反转、跨链选择 | `CLASSICAL`（原文 Remark）|
| §3 计算验证（左/右梳 vs 平衡） | `COMPUTATIONALLY VERIFIED EXAMPLE` |
| §4 对齐分段公式 | `[对应]` 精确（原文 + 计算）|
| §5 `S` = 角序(preorder)后继；postorder 是求值序 | `[对应]` **修正 note 36** |

**残余（`open`）**：
1. **跨链选择的典范化**：跨不可比链的相对序要"选"（左优先/右优先），如何典范化？
2. **一般 `n` 的严格证明**：§4 分段公式对一般 PPCT。
3. **`S` 与螺旋**：`S = preorder 后继` 与 note 34 螺旋模 `C⁴=S` 的衔接（`S` 只动 `V_index`，与 `V_class` 独立）。
4. **与 note 29 的关系**：note 29 的"下降障碍"是"多值（多条极大链）"；而 carousel 的角序（preorder）**不是**极大链，它是**遍历**，所以"下降"的障碍在"角序不是线性扩张"这一层——这与 note 29 的"多值"是**两个不同**的障碍，需分清。

---

## 7. 参考

- Pushkarev–Byzov 2014 §4（Thm 4.1/4.2/4.3、Cor 4.4、Remark）——原文由 OCR 读取。
- carousel 的 `k` 编号：Thm 4.3。
- 计算：`research/iota-carousel/verify_corner_order.py`。
- 相关：note 29（下降障碍）、34（螺旋模）、35/36（`S` 的初/分支导出）；OQ-098.3。
