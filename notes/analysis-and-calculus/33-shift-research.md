# shift 研究：iota frame 的螺旋结构，与 H 为何承载不了 index k

## note 32 的 `SR`/index 平移：`H`（Laplacian）能否承载？

### Research Note v0.1 · 2026-11-01

**结论**：iota frame **确实是"螺旋"**——`A=-JH`、`[J,H]=0`、`J²=-I`，且
$\exp(tA)=\cos(tH)-J\sin(tH)$，即**旋转角 ∝ H 的特征值**（已验）。但 carousel 的 **index `k`（= 左叶数）是"平面"量**，而 `H` 来自**割图**（= 依赖偏序的下集格，**忘记左/右**），故 **`H` 的谱不决定 `k`**：$n=4$ 时**同一割图谱**的四棵树 `k=3,2,2,1`（已验）。即 **shift 的载体不能是 `H`**；这与 note 29 的"平面障碍"同源。

---

## 0. 目标（note 32 §4 的 shift 项）

1. 精确化"shift"（carousel 的 `SR→LL` 入口 + index `k→k+1`）；
2. 检验 iota frame 的 `H`（Laplacian）能否承载它。

---

## 1. "shift" 的精确内容

- **index `k`** = "第 k 个 LL/RL/RN/LN"，其值 = 对应类的**计数**（`k = #LL`）。
- carousel：`LL(k)→RL(k)→RN(k)→LN(k)→LL(k+1)`——**类 4-循环 + 计数 `k` 递增**。
- 计数影子（Cor 4.4）：`(k,l,m,n)→(n+1,k,l-1,m)`，约束 `k=m+1, l=n+1`；在约束面上是**对合（阶 2）**（note 31）。
- 所以"shift" = **平面计数 `k` 的递增**；`k` 是**左叶数（planar）**，不是谱量。

---

## 2. iota frame 是"螺旋"（已验）

`J = [[0,-I],[I,0]]`，`J²=-I`；`H = diag(H0,H0)`（`H0` = 割图归一化 Laplacian）；`A = -JH`。

$$
[J,H]=0,\qquad J^2=-I,\qquad A^2=-H^2,\qquad \exp(tA)=\cos(tH)-J\sin(tH).
$$

**读法**：在 `J` 的 `±i` 本征空间上，`A = ∓iH`，故 `exp(tA)` 是**转角 `∝ H 本征值` 的旋转**——正是"螺旋（旋转 + 高度）"。**高度 = `H` 的本征值 λ**。

（脚本 `research/iota-carousel/verify_shift.py`，四项全 `True`。）

---

## 3. 检验：`H` 能否承载 index `k`？——**不能**

对 $n=4$ 的 5 棵 PPCT，构造**割图**（依赖偏序 $P$ 的下集格 $\mathcal O(P)$ 的 Hasse 图），
取 `H0 = L/(2 d_max)`，算谱并与 `k = #左叶` 对照：

| 树 | `k`(#LL) | #cuts | H 谱 |
|---|---|---|---|
| `N(L,N(L,N(L,L)))` | 3 | 4 | (0, .1464, .5, .8536) |
| `N(L,N(N(L,L),L))` | 2 | 4 | (0, .1464, .5, .8536) |
| `N(N(L,N(L,L)),L)` | 2 | 4 | (0, .1464, .5, .8536) |
| `N(N(N(L,L),L),L)` | 1 | 4 | (0, .1464, .5, .8536) |
| `N(N(L,L),N(L,L))` | 2 | 5 | (0, .1383, .3333, .4481, .7469) |

**同一谱 $(0,.1464,.5,.8536)$ 对应 `k=3,2,2,1`**。故 **`H` 的谱不决定 `k`**。

---

## 4. 诊断：与 note 29 同一"平面障碍"

- **割图** = 依赖偏序 $P$ 的下集格 $\mathcal O(P)$ 的 Hasse 图；$P$ **只记录"谁是后代"，忘记左/右（平面）**。
- **`k` = 左叶数**是**平面**量（交换某棵子树的左右会改变 `k`，但不改变 $P$）。
- 所以 `H`（由 $P$ 造出）**对平面操作不变，而 `k` 变**——二者不可能由 `H` 决定。
- 这与 **note 29**（τ 不下降到偏序层，因 τ 用平面信息、$P$ 丢失平面）**完全同源**：**`H` 是 unplanar 的，`k`/shift 是 planar 的**。

---

## 5. 结论与对 iota 的启示

**carousel–iota 的最终图景**：

| 部分 | iota 侧载体 | 状态 |
|---|---|---|
| **旋转**（类 4-循环）| `J`（复单位，代数、非平面）| 可对齐（非典范，note 32）|
| **shift**（index `k`、`SR` 入口）| 需要 **planar** 载体 | **`H` 不行**（unplanar）；候选未定 |

**对"iota 是否够丰富"的精确回答**：**iota 在"代数/旋转"侧丰富（J、Ω、螺旋），但在"平面/shift"侧缺失**。carousel 的 shift 需要一个**记住左/右**的、且**支持无界计数**的载体；`H`（Laplacian）两者都不满足。

**可用的 planar 线索**（供下一步）：
- **手性符号律的 Z/2**（偶/奇置换 → Ω 保持/反号）——但只是 Z/2，不够无界；
- **iota frame 的"双倍"结构**（`Q^{2n}` 实⊕虚、或 12 带号态）——提供 Z/2 覆盖；
- **`Λ¹↔Λ²` 分级**——Z-分级但只到 2；
- 要承载**无界**的 `k`，可能要把"平面"与"分级维数 `n`"结合（`n` 随树增长）。

---

## 6. 地位与残余

| 命题 | 地位 |
|---|---|
| §2 螺旋：`[J,H]=0`、`J²=-I`、`A²=-H²`、`exp(tA)=cos(tH)-J sin(tH)` | `CLASSICAL`（矩阵恒等）+ 计算验证 |
| §3 同谱不同 `k`（n=4）| `COMPUTATIONALLY VERIFIED EXAMPLE` |
| §4 `H` 是 unplanar、`k` 是 planar → `H` 不承载 `k` | `[对应]` 精确诊断 |
| §5 shift 需要 planar、无界载体 | `structural proposal` |

**残余（`open`）**：
1. **planar 载体**：是否存在 AEG/Adva 已有的对象同时"记住左/右"且"支持无界计数"？（候选：手性 Z/2 × 维数 `n`；或带号 12 态 + 外幂。）
2. **一般 `n`**：同谱不同 `k` 的构造能否一般化（预期：所有"链骨架"的树共享割图但 `k` 各异）。
3. **与 fringing 的关系**：$\Delta(Q(T))=3\Delta(T)$ 是否在 `H` 的谱（如最小正本征值）上有对应？

---

## 7. 参考

- AEG：`paper-5/sections/04-six-state-carrier.tex`（`Ω=TSR`、三平面、手性符号律）。
- Adva：`knowledge/received/iota-frame-knowledge-2026-09-17-v1/materials/{frame.md,algebra.py}`（`H=diag(H0,H0)`、`A=-JH`）。
- carousel：Pushkarev–Byzov 2014 Thm 4.3 / Cor 4.4。
- 计算：`research/iota-carousel/verify_shift.py`（螺旋 + 同谱不同 `k`）；`research/donaghey-orbits/verify_carousel.py`。
- 相关：note 29（平面障碍）、31、32；OQ-098.3。
