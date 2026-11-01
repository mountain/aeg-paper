# 跨分支选择的典范化：一般 $n$ 的归纳证明

## note 38 的一般化：唯一最少逆序 = 左优先 postorder，对所有 PPCT 成立

### Research Note v0.1 · 2026-11-01

**结论**：note 38 的典范化（"最少逆序的线性扩张 = 左优先 postorder"）**对任意 PPCT 成立且唯一**，证明是对树结构的**归纳证明**（不是有限验证）。同时把计算证据扩到 $n\le7$（193 棵树）。

**定理**：设 $t$ 为 PPCT，$P(t)$ 为内部点的 preorder（角序），$Q(t)$ 为左优先 postorder。则在 $t$ 依赖偏序的**所有线性扩张** $E$ 中，
$$
Q(t)\;=\;\arg\min_E\ \mathrm{inv}(E,P(t))
$$
且**唯一**。

---

## 0. 记号

- $I(t)$ = $t$ 的内部点集；$t$ 为 full binary tree，内部点有左/右子（叶或内部点）。
- $P(t)$ = $I(t)$ 的 **preorder**（左标准遍历：自身、左子树、右子树）。
- $Q(t)$ = $I(t)$ 的 **左优先 postorder**（左子树、右子树、自身）。
- $\mathcal L(t)$ = $I(t)$ 上依赖偏序（后代 $\le$ 祖先）的线性扩张集。
- 对 $E\in\mathcal L(t)$，$\mathrm{inv}(E,P(t))=\#\{(u,v):u\text{ 在 }P\text{ 先于 }v,\ v\text{ 在 }E\text{ 先于 }u\}$。

---

## 1. 关键引理（父子分解）

设 $t=\mathrm{Node}(a,b)$，$m=|I(t)|$。则 $I(t)=\{t\}\sqcup I(a)\sqcup I(b)$，且
$$
P(t)=[t]+P(a)+P(b),\qquad Q(t)=Q(a)+Q(b)+[t],
$$
且 $E\in\mathcal L(t)$ **当且仅当** $E=M+[t]$，其中 $M$ 是某个 $E_a\in\mathcal L(a)$、$E_b\in\mathcal L(b)$ 的**交错**（interleaving）。

**分解**：对任意 $E=M+[t]$，
$$
\mathrm{inv}(E,P(t))\;=\;\underbrace{(m-1)}_{\text{根}}
\;+\;\mathrm{inv}(E_a,P(a))\;+\;\mathrm{inv}(E_b,P(b))
\;+\;\underbrace{\mathrm{cross}(M)}_{\text{a/b 交叉逆序}} .
$$
理由：$t$ 在 $P$ 中最先、在 $E$ 中最后，故与其余 $m-1$ 个点全逆序（**常数**）；$P$ 中所有 $a$ 点先于所有 $b$ 点，故 $M$ 中"$b$ 点先于 $a$ 点"的对即交叉逆序。

**引理**：$\mathrm{cross}(M)\ge 0$，且 $=0$ **当且仅当** $M=E_a+E_b$（块拼接：所有 $a$ 先于所有 $b$）。任何交错只要有一对 $b$ 在 $a$ 前，就产生 $\ge1$ 个交叉逆序。

**证明**：$P(a)+P(b)$ 中每个 $a$ 点都在每个 $b$ 点前。$M$ 若把某 $b$ 点放在某 $a$ 点前，则 $P$ 中该 $a$ 先于该 $b$、$M$ 中该 $b$ 先于该 $a$，构成逆序。故只有"全 $a$ 先于全 $b$"才为 0，即块 $E_a+E_b$。∎

---

## 2. 定理的归纳证明

对 $t$ 的大小归纳。

**基**：$t$ 为叶（$I(t)=\varnothing$）时平凡；$t$ 为单内部点（$|I|=1$）时唯一扩张即 $Q$。

**步**：$t=\mathrm{Node}(a,b)$，$|I(t)|=m$。对任意 $E=M+[t]\in\mathcal L(t)$，
$$
\mathrm{inv}(E,P(t))
=(m-1)+\mathrm{inv}(E_a,P(a))+\mathrm{inv}(E_b,P(b))+\mathrm{cross}(M).
$$
由归纳假设，$\mathrm{inv}(E_a,P(a))\ge\mathrm{inv}(Q(a),P(a))$（等号 iff $E_a=Q(a)$），$b$ 同理；由引理，$\mathrm{cross}(M)\ge0$（等号 iff $M=E_a+E_b$）。故
$$
\mathrm{inv}(E,P(t))\;\ge\;(m-1)+\mathrm{inv}(Q(a),P(a))+\mathrm{inv}(Q(b),P(b))\;=\;\mathrm{inv}(Q(t),P(t)),
$$
且**等号成立 iff** $E_a=Q(a)$、$E_b=Q(b)$、$M=E_a+E_b$，即 $E=Q(a)+Q(b)+[t]=Q(t)$。

故 $Q(t)$ 是**唯一**最小值点。$\blacksquare$

---

## 3. 计算证据（$n\le7$）

`research/iota-carousel/verify_canonical_choice.py` 对 $n=4,5,6,7$ 的**全部** PPCT（$5+14+42+132=193$ 棵）枚举所有线性扩张并取最少逆序者：

| $n$ | 树数 | `max #exts` | 最小者唯一 | = 左优先 postorder |
|---|---|---|---|---|
| 4 | 5 | 2 | ✓ | ✓ |
| 5 | 14 | 3 | ✓ | ✓ |
| 6 | 42 | 8 | ✓ | ✓ |
| 7 | 132 | 20 | ✓ | ✓ |

与 §2 的归纳证明一致（证明已覆盖所有 $n$）。

---

## 4. 与 note 36/37/38 的衔接

- note 37：角序 = preorder（carousel 的 `k`）；
- note 38：典范化准则 = 最少逆序；
- **本笔记：该准则对任意 $n$ 的唯一解 = 左优先 postorder（归纳证明）**；
- note 36：分支层 `S` = 左优先 postorder 后继。

**结论**：**`S` 就是"与角序最贴合的、唯一的 canonical 求值序"，对任意 PPCT 成立。** 跨分支层选择的典范化**完成**。

---

## 5. 地位与残余

| 命题 | 地位 |
|---|---|
| §1 父子分解 + 交叉引理 | `[对应]` 精确（直接计数）|
| §2 归纳定理（唯一最少逆序 = Q，任意 $n$）| **`PROVED`（本笔记）**——证明完整，无遗漏假设 |
| §3 $n\le7$ 计算一致 | `COMPUTATIONALLY VERIFIED EXAMPLE` |
| §4 `S` = canonical 求值序 | `[对应]` 精确 |

**残余（`open`）**：
1. **其他内蕴准则**：是否也有同一唯一解（如"保留左→右子树叶序"）？若有，典范性更强（多条准则同解）。
2. **与 $\sigma$ 的等变性**：准则 $\sigma$-不变、解 $\sigma$-等变（左优先 ↔ 右优先）。
3. **与 note 29 的正式区分**：note 29 的障碍是"$\tau$ 不下降到 $O(P)$（多值）"；本典范化是"选一条极大链"的准则。二者关系：典范化把"多值"**单值化**，但 $\tau$ 本身仍不是 $O(P)$ 的映射（note 29 的障碍是 $\tau$ 的，不是选链的）。需正式写清。
4. **Kendall tau 之外的距离**：Spearman footrule 等是否给同一解？

---

## 6. 参考

- Pushkarev–Byzov 2014 §4（Thm 4.2/4.3、Remark）：corner=顶点、left standard traversal=preorder。
- 计算：`research/iota-carousel/verify_canonical_choice.py`（$n\le7$，193 棵）。
- 相关：note 29（下降障碍）、34（螺旋模）、36（分支层 S）、37（角序对齐）、38（典范化准则）；OQ-098.3。
