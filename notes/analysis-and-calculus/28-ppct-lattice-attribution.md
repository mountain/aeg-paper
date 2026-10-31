# PPCT 格的归属：Tamari/旋转格 vs Birkhoff 下集格

## OQ-098.2 推进：把"PPCTs form a distributive lattice"厘清

### Research Note v0.1

**2026-10-31**（v0.1：推进 OQ-098.2。结论：(1) **PPCT 上"标准格序"（旋转序）是 Tamari 格，是格但非分配**（$T_4$ 反例已验）；(2) **Pushkarev–Byzov 原话"distributive lattice whose irreducibles are ordered as the vertices of the infinite cubic tree"精确对应的是 Birkhoff 下集格**（无限三叉树的下集，分配，由 Birkhoff 自动），其元素是 down-sets（有序二叉树/平面树），不是全二叉 PPCT 本身；(3) **论文把这二者混用**（"standard lattice ordering of all trees" = Tamari，"distributive" = Birkhoff 下集，二者互斥）；(4) **AEG 的 $\mathcal O(P)$ 也是 Birkhoff 下集格**（有限依赖偏序 $P$），故"分配"一侧与 AEG 同构构造、不同偏序，一般不同构）

---

## 0. 问题

OQ-098.2：Pushkarev–Byzov（§5）说"the PPCTs form a **distributive lattice** whose irreducible elements are ordered as the vertices of the **infinite cubic tree**"，并说 Donaghey 变换对此"standard lattice ordering of all trees"**非单调**。问题是：这个格到底是哪个？与 AEG 的 Birkhoff 格 $\mathcal O(P)$ 什么关系？

**两个候选**：
- **(A) Tamari / 旋转格**：PPCT（全二叉树）按"旋转"（结合律重排）的偏序。这是组合学里的"标准树格"。
- **(B) Birkhoff 下集格**：某偏序 $P$ 的下集（order ideal）按包含的格。由 Birkhoff 对偶，必为分配格，且并不可约元恰是 $P$ 的元素。

---

## 1. 候选 (A)：Tamari 格是格，但**非分配**（已计算）

**计算**（`research/ppct-lattice/`，$n=5$ 叶 = 14 棵 = Tamari $T_4$）：
- 按"旋转" $N(N(a,b),c)\to N(a,N(b,c))$ 的传递闭包建序，验证 **任意两元的交/并存在**（是格）；
- 对全部 $14^3$ 三元组验分配律 $a\wedge(b\vee c)=(a\wedge b)\vee(a\wedge c)$，**失败**。

**反例**（$T_4$）：
$$
a=N(L,N(L,N(N(L,L),L))),\quad
b=N(L,N(N(L,L),N(L,L))),\quad
c=N(L,N(N(L,N(L,L)),L)),
$$
$$
a\wedge(b\vee c)\ \neq\ (a\wedge b)\vee(a\wedge c).
$$

即 **Tamari 格不是分配格**。因此，若把"standard lattice ordering of all trees"读作 Tamari 格，则**原话的"distributive"是错的**。`[Donaghey]`（`CLASSICAL`：Tamari 格是格、非分配——这是已知事实，计算给出 $T_4$ 显式见证）。

---

## 2. 候选 (B)：无限三叉树的下集格**是**分配格，且不可约元=顶点

设 $T_\infty$ = 无限三叉/二叉树（每个顶点二子），以"祖先后代"为偏序。其**下集**（order ideal：含某点则含其祖先）按包含构成格。

- **分配性**：由 Birkhoff 对偶，任意偏序的下集格都是分配格，且其**并不可约元 = 主下集 $\downarrow v$**（$v\in T_\infty$），按包含排序即与原偏序同构。这正是原话"distributive lattice whose irreducible elements are ordered as the vertices of the infinite cubic tree"的**逐字对应**。
- **元素计数**：下集（含根）的大小为 $N$ 的个数满足 $R(N)=\sum_{i=0}^{N-1}R(i)R(N-1-i)$，$R(0)=1$，故 $R(N)=C_N$（Catalan）。即 $N$ 个顶点的下集 ↔ $N$ 顶点的有序二叉树，共 $C_N$ 个。
- **注意**：下集是"每点 0/1/2 子"的有序二叉树，而 **PPCT 是"每内部点恰 2 子"的全二叉树**。两者都 $C_N$ 计数，经"旋转"双射对应，但**不是同一个集合**。

`[Donaghey]`（`CLASSICAL`：Birkhoff 对偶 + Catalan 计数）。

---

## 3. 原话的归属：应读作 (B)，但论文混用了 (A)

原句有两个成分：
1. "standard lattice ordering of all trees" —— 这通常指 **Tamari/旋转格**（非分配）；
2. "distributive lattice whose irreducibles are ordered as the vertices of the infinite cubic tree" —— 这只对应 **Birkhoff 下集格**（分配）。

二者**互斥**（Tamari 非分配，Birkhoff 分配）。故最诚实的读法是：

> 论文的"distributive + 不可约元=无限三叉树顶点"精确描述的是 **Birkhoff 下集格** (B)；但作者同时称它是"standard lattice ordering of all trees"，而那个"standard"通常是 **Tamari** (A)。**论文把两个不同的格混用**；"PPCT 形成分配格"应理解为"经旋转双射后，与无限三叉树的下集格（分配）同构/对应"，而**不是**说 Tamari 格分配。

`[对应]`（`structural proposal`；这是对原文措辞的澄清，不是对论文的数学推广）。

---

## 4. 与 AEG 的 $\mathcal O(P)$ 的关系

AEG 的 $\mathcal O(P)$（`thm:birkhoff-downset-spinal`）= 有限依赖偏序 $P$ 的下集格，也是 **Birkhoff 下集格**，故同样分配、同样"并不可约元 = $P$ 的元素"。

| | 论文 (B) | AEG $\mathcal O(P)$ |
|---|---|---|
| 构造 | 无限三叉树 $T_\infty$ 的下集格 | 有限依赖偏序 $P$ 的下集格 |
| 分配性 | 是（Birkhoff）| 是（Birkhoff）|
| 不可约元 | 顶点 of $T_\infty$ | $P$ 的元素 |
| 元素 | 有限下集（有序二叉树）| 偏序 $P$ 的下集 |
| 与 AEG | **同一构造（Birkhoff），不同偏序** | — |

**结论**：论文的"分配格"与 AEG 的 $\mathcal O(P)$ **是同一构造（Birkhoff 下集格）的两个实例，但偏序不同（$T_\infty$ vs 有限 $P$），一般不同构**。$T_\infty$ 是"万有"（所有二叉串/平面树）的情形；$\mathcal O(P)$ 是"给定计算 DAG"的有限情形。

`[对应]`（`structural proposal`；"同一构造、不同偏序、一般不同构"是精确陈述）。

---

## 5. 对 OQ-098.1(b) 的地基

- **"分支层"在 AEG 里就是 $\mathcal O(P)$（Birkhoff 下集格）**，不是 Tamari 格。
- 论文的"分配格 + 无限三叉树"读法说的是 **Birkhoff 下集格**，与 AEG 的 $\mathcal O(P)$ 是**同一类对象**。
- 所以 OQ-098.1(b)（把 Donaghey 的 $\tau$ 提升到分支层）应表述为：**$\tau$ 在 PPCT（Tamari 格元素）上的作用，是否诱导出"依赖偏序 → 其下集格"层面的对应？** 而"分配格"这一侧（$\mathcal O(P)$）是地基，但不能误用 Tamari 格的"非分配"性质。

---

## 6. 地位总表与残余

| 命题 | 地位 |
|---|---|
| §1 Tamari/旋转格是格、非分配 | `CLASSICAL`（已知）；$T_4$ 显式见证为计算 |
| §2 无限三叉树下集格分配、不可约元=顶点、$R(N)=C_N$ | `CLASSICAL`（Birkhoff + Catalan）|
| §3 论文混用 Tamari 与 Birkhoff 下集 | `[对应]` `structural proposal`（措辞澄清）|
| §4 论文分配格与 $\mathcal O(P)$ 同构构造、不同偏序、一般不同构 | `[对应]` `structural proposal` |

**残余（`open`）**：

1. **$T_\infty$ 的下集格与 $\mathcal O(P)$ 的精确关系**：是否存在"$P$ 嵌入 $T_\infty$ 的某子偏序"使得 $\mathcal O(P)$ 是下集格的子格？目前已证"一般不同构"，但"何时同构/嵌入"仍 open。
2. **"标准树格"的精确出处**：论文的"standard lattice ordering of all trees"具体指 Tamari 还是某个"下集格"变体，需查原始文献（Donaghey 1980 / 相关）；本文暂按"最可能 = Tamari"处理，并标注混用风险。
3. **098.1(b) 的提升**：$\tau$ 作为 Tamari 格上的置换，是否在 $\mathcal O(P)$ 层面留下痕迹？这依赖 §5 的地基，仍是 open。

---

## 7. 参考

- Pushkarev–Byzov 2014（§5，`temp/` 下 PDF）；Donaghey 1980。
- AEG：`paper-1/sections/02-sequential-histories.tex`（`thm:birkhoff-downset-spinal`）；note 15（`15-branching-history-dcpo.md`）。
- Tamari 格：组合学标准事实（旋转序、非分配）；计算见证见 `research/ppct-lattice/`。
- 相关：note 26/27、OQ-098。
