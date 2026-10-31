# Donaghey / De Bruijn–Morselt 变换与 AEG 树层：总览

## note 26–29 综合（098.1 · 098.1(b) · 098.2 的收束）

### Research Note v0.1 · 2026-10-31

**一句话结论**：Donaghey/De Bruijn–Morselt 的"一般树 ↔ 二叉树"变换，在**组合学层面**与 AEG 树层精确对应（右/左双射 = 左右梳；σ/θ/φ = 镜像/反演/词编码）；但它的**非交换（`Z₂*Z₂`）与双曲/长轨道结构**属于**平面树层**，**不**属于 AEG 的 comb 层，也**不**下降到底层（依赖偏序 / `O(P)`）。"PPCT 分配格"应读作**无限三叉树的 Birkhoff 下集格**，不是 Tamari 格。

**详细笔记**（本总览只综述，证明/见证在各篇）：
- `26-donaghey-general-to-binary-tree.md` — 变换本体与 `[对应]` 表；
- `27-mirror-reversal-tree-layer.md` — 098.1（comb 层 = Klein）；
- `28-ppct-lattice-attribution.md` — 098.2（格 = Birkhoff 下集格）；
- `29-branching-layer-descent.md` — 098.1(b)（τ 不下降）。
- 计算：`research/donaghey-orbits/`、`research/ppct-lattice/`。

---

## 0. 材料与路线图

**材料**（`temp/` 下三份，用户 2026-10-31 新增）：
- **Donaghey 1980**（*JCTB* 29, 75–90）：四族 Catalan、R/L 双射、$M_P$/$M_Z$、primitive/Motzkin。
- **Pushkarev–Byzov 2014**（*J. Math. Sci.* 196(2), 199–215）：三定义、右/左双射、σ/θ/φ、carousel、fringing、双曲性、轨道下界、`Z₂*Z₂`（Thm 6.4）。
- **OEIS A014486 图表**（Karttunen 2011）：Catalan 结构罗塞塔（一般树 ↔ 二叉树 ↔ Dyck ↔ 三角剖分）。

**路线图**：§1 数学核心 → §2 AEG 对应 → §3 群结构（098.1）→ §4 格归属（098.2）→ §5 下降障碍（098.1(b)）→ §6 总地位 → §7 开放问题。

---

## 1. 数学核心（Donaghey / Pushkarev–Byzov）

**四族**（皆 $c_n$）：一般括号化 g.b.、二叉括号化 b.b.、平面树 p.t.、三叉平面树 t.p.t.（= PPCT）；外加 zigzag 树 z.t. 与 +.b.b.。自然对应：`+.b.b. ↔ z.t.`、`(g.b.) ↔ p.t.`（De Bruijn–Morselt up-down code = Dyck 词）。

**右/左双射 R/L**：$g.b.\to +.b.b.$，R 换右括号、L 换左括号；递归上 R = **右梳**、L = **左梳**。树级为 PPCT ↔ PPT（顶点 ↔ 右/左路径）。

**三个等价定义**（Pushkarev–Byzov Thm 2.1）：
1. 归纳式（右分解 → 左分解）；
2. $T\to T^R$（右双射）$\to T'$（左双射逆）；
3. $\tau=\varphi^{-1}\circ\theta\circ\varphi\circ\sigma$：**σ = transposition**（左右子互换）、**θ = reflection**（Dyck 路径反向）、**φ = PPCT ↔ Dyck 路径**。

**轨道理论**：carousel effect（角类 SR/LL/RL/RN/LN 循环搬运，Thm 4.3）；fringing（Thm 6.1：$\Delta(Q(T))=3\Delta(T)$ 或 $\tfrac32\Delta(T)$）；轨道增长 $O(n^{\log_23})$（Cor 6.3）；轨道下界（Cor 6.5）；Thm 6.4：$\langle\sigma,\theta\rangle\cong\mathbb Z_2*\mathbb Z_2$。

---

## 2. `[对应]` 与 AEG 树层的精确对应

| Donaghey/PB | AEG | 状态 |
|---|---|---|
| **σ**（左右子互换）| 镜像 $m$：$C_{\omega,c}^{(\varepsilon)}\mapsto C_{\omega,c}^{(3-\varepsilon)}$（`def:mirror-temporal-reversal`）| 精确一致 |
| **θ**（Dyck 路径反向）| 时间反演 $r$：$\gamma\mapsto(g_n,\dots,g_1)$（`def:mirror-temporal-reversal`）| 精确一致（路径级）|
| **φ**（PPCT↔Dyck）| up-down 词编码（历史=词）| 精确一致 |
| **R/L 双射**（顶点↔右/左路径）| 左/右梳 `conv:p0-left-right-convention` | 精确一致 |
| **四族 Catalan** | 二叉树（顺序）vs 一般树（分支）| 精确一致 |
| **τ = φ⁻¹θφσ** | Donaghey 变换 | 结构对应（≠ AEG 的 $mr$，见 §3）|
| primitive/Motzkin、carousel、fringing | 与单脊/Hecke 周期轨道的关系 | **open** |

**关键要点**：AEG 在 §2 把"镜像 / 时间反演 / 路径逆"当成三个不同概念；σ/θ/φ 恰好给出它们的**具体 Catalan 模型**。

---

## 3. 群结构：AEG 的 `Z₂×Z₂` vs Donaghey 的 `Z₂*Z₂`（098.1）

| | AEG（词/comb 层）| Donaghey（树层）|
|---|---|---|
| 镜像 | $m$（换槽）| $\sigma$ |
| 反演 | $r$（词反向）| $\theta$（路径反向）|
| 关系 | **交换**：$mr=rm$ | **不交换** |
| 所生成群 | $\mathbb Z_2\times\mathbb Z_2$（Klein）| $\mathbb Z_2*\mathbb Z_2$（无限二面体，Thm 6.4）|
| 复合阶 | $mr$ 阶 2 | $\tau=\theta\sigma$ 无限阶（Cor 6.3）|

**定论（098.1）**：
1. AEG 的 $m,r$ 在词层交换（`def:mirror-temporal-reversal` 已证），生成 **Klein**；词↔comb 双射**保交换**，故 **comb 层也是 Klein**。
2. Donaghey 的 $\sigma=m$，但 $\tilde\theta=\varphi^{-1}\theta\varphi$ **不是** $r$（路径反向 ≠ 词反向）；$\tau\neq r\sigma$。
3. 长轨道/`Z₂*Z₂` 的构造（完全树 + fringing）是**分支树**；有限验证（`n≤10`）：**caterpillar 非 τ-不变**（$n$ 叶 $2^{n-2}$ 个中仅 $n-1$ 个 cat→cat），**所有长度 $>6$ 轨道全不含 caterpillar**。

**结论**：AEG 现有操作（$m,r$）生成 Klein，**不**自动出现 `Z₂*Z₂`；非交换扩展需要**另一个**反演 $\tilde\theta$（**098.1(a)，open**）。

---

## 4. 格归属：Birkhoff 下集格，不是 Tamari（098.2）

论文称"PPCTs form a **distributive** lattice whose irreducible elements are ordered as the vertices of the infinite cubic tree"。两个候选：

- **(A) Tamari / 旋转格**：$n=5$ 叶 = 14 棵 = $T_4$；计算验证**是格但非分配**（分配律反例已给，`research/ppct-lattice/`）。
- **(B) 无限三叉树的下集格**：由 Birkhoff **必分配**，并不可约元 = 顶点；$N$ 顶点下集数 $R(N)=C_N$（已验证 $N\le8$）；元素是 down-sets（有序二叉树），不是全二叉 PPCT。

**定论**：原话的"distributive + 不可约元=无限三叉树顶点"**逐字对应 (B)**；而"standard lattice ordering of all trees"是 **(A)**。二者**互斥**，故**论文混用**。AEG 的 $\mathcal O(P)$ 也是 **Birkhoff 下集格**（有限 $P$）——**同一构造、不同偏序、一般不同构**。

---

## 5. 下降障碍：τ 不下降到底层（098.1(b)）

AEG 的依赖偏序（`def:internal-dependency-poset`：$u\preccurlyeq v$ ⟺ 后代）对全二叉树 = **内部骨架**，**忘记平面（左/右）信息**；而 $\tau$ 恰好**使用**平面信息。

**计算定论**：$\tau$ **不保持依赖偏序同构类**。
- $n=4$ 见证：$T_1=N(L,N(L,N(L,L)))$ 与 $T_2=N(L,N(N(L,L),L))$ 依赖偏序同为 3-链，但 $\tau T_1$ 仍 3-链、$\tau T_2$ 变 V（分支）。
- $n\ge5$：**所有骨架类都多值**（已验证 $n\le8$：$n=5$:3/3、$n=6$:6/6、$n=7$:11/11、$n=8$:22/23）。

**推论**：$\tau$ **不诱导** $P$ 或 $\mathcal O(P)$ 上的映射（Birkhoff 单射）。**τ 的双曲/无限阶结构严格是平面树层现象**；把 `Z₂*Z₂` 搬到 $\mathcal O(P)$ 的路是**断的**。

**澄清"两种分支"**：树级"分支"（某内部点二内部子）在集合上 = 偏序级"$P$ 非链"，但 $\tau$ **不逐点保持**该划分（同属链类的两树一留一串变分支）。

---

## 6. 总地位表

| 命题 | 地位 |
|---|---|
| §1 四族、R/L、σ/θ/φ、carousel、fringing、轨道增长、Thm 6.4 | `CLASSICAL`（Donaghey 1980 / Pushkarev–Byzov 2014）|
| §2 σ↔m、θ↔r、φ↔up-down、R/L↔左右梳、四族↔两类树 | `[对应]` `structural proposal`（精确）|
| §3 AEG $m,r$ 交换 → Klein；双射保交换；comb 层 Klein | `CLASSICAL`（`def:mirror-temporal-reversal`）+ 计算 |
| §3 caterpillar 非 τ-不变、长轨道全分支（$n\le10$）| `COMPUTATIONALLY VERIFIED EXAMPLE` |
| §4 Tamari 非分配（$T_4$）；Birkhoff 下集分配、$R(N)=C_N$ | `CLASSICAL`（已知）+ 计算见证 |
| §4 原话 = Birkhoff 下集；AEG $\mathcal O(P)$ 同构造不同偏序 | `[对应]` `structural proposal` |
| §5 τ 不保持依赖偏序同构类（$n\le8$）| `COMPUTATIONALLY VERIFIED EXAMPLE` |
| §5 τ 不下降 → 双曲性是平面树现象 | `[对应]`（有限范围内精确）|

---

## 7. 开放问题（残余）

| 编号 | 问题 | 状态 |
|---|---|---|
| 098.1(a) | `θ̃` 是否有 AEG 内在定义（不借助 Donaghey，例如在 comb 的 up-down 码上定义"路径反射"），且与 $m$ 生成 `Z₂*Z₂`？| open |
| 098.2 残余 | $\mathcal O(P)$ 是否嵌入某个 $T_\infty$ 子偏序的下集格；原文"standard lattice ordering"的精确出处 | open |
| 098.1(b) 残余 | 一般 $n$ 的"所有骨架类多值"证明；AEG 分支层**自身**（非 τ）是否有双曲结构；τ 需多少平面信息才良定义 | open |
| 098.3 | carousel / fringing / $O(n^{\log_23})$ 轨道增长 ↔ AEG 的 Hecke 周期轨道 / "fractal rotation" | open |
| 098.4 | 右/左双射是否给出"分支层 → 顺序层"的函子，且尊重序缺陷 | open |

---

## 8. 参考

- **Donaghey 1980**：`J. Combin. Theory Ser. B` 29, 75–90（`temp/1-s2.0-0095895680900453-main.pdf`）。
- **Pushkarev–Byzov 2014**：`J. Math. Sci.` 196(2), 199–215（`temp/Pushkarev-Byzov2014_...pdf`）。
- **OEIS A014486 图表**：`temp/a014486.pdf`（Karttunen 2011）。
- **AEG 侧**：`paper-0/sections/03-aes-and-motion.tex`（`conv:p0-left-right-convention`）；`paper-1/sections/02-sequential-histories.tex`（`def:mirror-temporal-reversal`、`def:path-inverse`、`def:internal-dependency-poset`、`thm:sequential-tree-classification`、`thm:birkhoff-downset-spinal`）。
- **详细笔记**：`26`–`29`；**计算**：`research/donaghey-orbits/`（τ、轨道、下降）、`research/ppct-lattice/`（Tamari vs Birkhoff）。
