# fringing / 轨道增长 ↔ Hecke 周期轨道：结构对应，非增长律对应

## OQ-098.3 推进（carousel / fringing / 轨道增长 对 AEG 的 Hecke 周期轨道）

### Research Note v0.1 · 2026-11-01

**结论（诚实分层）**：
- **成立（结构层）**：两边都是"**自由积作用下的原始周期轨道的编码**"——
  - AEG：`Γ_4=⟨J,R|J²=R⁴=1⟩=C₂*C₄`，**原始双曲类 ↔ 周期轨道**（Paper 3 `prop:q4-hyperbolic-class-knot`），**零 dessin = 编码脊**（`thm:q4-zero-dessin-coding-spine`）；
  - PB：`⟨σ,θ⟩≅Z₂*Z₂`（Thm 6.4），`τ`-轨道，**树遍历/角序 = 编码**。
  - 共同点：**自由积**（`C₂*C₄` vs `Z₂*Z₂`）、**原始**（primitive）、**编码脊**、**周期轨道**，以及**order-4 旋转**（PB 的 `J`/carousel ↔ AEG 的 `C₄` 椭圆旋转）。
- **不成立（增长律层）**：PB 的 `O(n^{log₂3})`（Cor 6.3）是"**轨道长度 vs 树规模**"（fringing 替换增长）；AEG 的是"**周期轨道的计数**"（指数、熵 1）。**不同量、不同率**，故**无增长律对应**——这是精确的负结果，不是含糊的"待定"。

---

## 0. 目标

OQ-098.3：carousel / fringing / `O(n^{log₂3})` 是否对应 AEG 的 Hecke 周期轨道 / "fractal rotation"？

---

## 1. AEG 的 Hecke 周期轨道（Paper 3 `05-q4-geodesic-knots`）

- **群**：`Γ_4=⟨J,R∣J²=R⁴=1⟩=C₂*C₄`（`eq:q4-sign-kernel-presentation`），`R=JT`、`T=JR`、`H_4=ker χ`；orbifold `𝒪_4=Γ_4\H`。
- **原始类 ↔ 周期轨道**：`prop:q4-hyperbolic-class-knot`——`Γ_4` 的**原始双曲共轭类**与 geodesic flow 的**原始有向周期轨道**一一对应；单位切丛中的 `K_γ` 是嵌入圆。
- **编码脊**：`thm:q4-zero-dessin-coding-spine`——零 dessin `Z(a_4)` = Dehornoy–Pinsky 图 `G[2,4,∞]`；双曲轴 → 容许双无限路径 → 周期约化码 → template 轨道；"**脊不是 template**"（`warn:q4-spine-not-template`）。
- **历史 → 轨道**：`prop:q4-operator-history-knot-map`——`Hist_4^{ph}`（原始双曲的 Paper I 词）→ 周期轨道。

**要点**：AEG 侧是"**自由积 `C₂*C₄` 下的原始周期轨道的编码**"。

---

## 2. Pushkarev–Byzov 的 fringing / 轨道

- **群**：`⟨σ,θ⟩≅Z₂*Z₂`（Thm 6.4）；`τ=φ⁻¹θφσ` 是**射影 Z/4**（note 34/39）。
- **fringing**（Def 6.1）：`Q(T)` 给每个叶加左右二子；**`Δ(Q(T))=3Δ(T)`**（偶时 `3/2`）（Thm 6.1）。
- **轨道增长**：迭代 fringing → `Δ ~ n^{log₂3}`（Cor 6.3）——**替换（substitution）增长**，`log₂3≈1.585`（Sierpinski 维数型）。
- **"fractal rotation"**：Pushkarev 对 `τ` 的命名。

**计算验证**（`research/iota-carousel/verify_fringing.py`）：

| 树 | 叶数 | `Δ` | `Q(T)` 叶数 | `Δ(Q(T))` | Thm 6.1 预测 | 一致 |
|---|---|---|---|---|---|---|
| `N(L,L)` | 2 | 1 | 4 | 3 | `3·1=3` | ✓ |
| `N(L,N(L,L))` | 3 | 2 | 6 | 3 | `3/2·2=3` | ✓ |
| `N(N(L,L),L)` | 3 | 2 | 6 | 3 | `3/2·2=3` | ✓ |
| `N(N(L,L),N(L,L))` | 4 | 3 | 8 | 9 | `3·3=9` | ✓ |

**读法**：`Q` 使叶数 `L→2L`、轨道长 `×3`（偶时 `×3/2`），故 `Δ ~ L^{log₂3}`——**替换（substitution）增长**，与 geodesic 的**计数**增长是不同量。

---

## 3. 成立的对应（结构层）

| AEG Hecke | Pushkarev–Byzov | 性质 |
|---|---|---|
| `Γ_4=C₂*C₄`（自由积）| `⟨σ,θ⟩=Z₂*Z₂`（自由积）| 同为"自由积的有限循环" |
| **原始双曲类** | **primitive 元素**（Donaghey §V）| 同为"原始"筛选 |
| **零 dessin = 编码脊** | **树遍历/角序 = 编码** | 同为"编码脊" |
| **周期轨道**（closed geodesics）| **`τ`-轨道**（cyclic）| 同为"周期/循环轨道" |
| **`C₄` 椭圆旋转**（order 4）| **`J`（order 4）**，carousel `C⁴=S` | 同为"order-4 旋转" |
| **有向周期的编码**（`Hist_4^{ph}→orbits`）| **角序后继 `S`**（note 37）| 同为"周期编码的前进" |

**最紧的一条**：**carousel 的 order-4 旋转（`J`，`C⁴=S`）↔ Hecke `C₄`（order-4 椭圆旋转）**——两边都是"90° 旋转"，且都嵌在"自由积"里。这是"carousel ↔ Hecke"的**结构性对接点**。

---

## 4. 不成立的（增长律层）

- PB 的 `O(n^{log₂3})` = **轨道长度**（一个 `τ`-轨道有多长）随**树规模** `n` 的替换增长。
- AEG 的 = **周期轨道的计数**（有多少原始类/轨道），对双曲格点是**指数**（熵 1，常数曲率 −1）。
- **不同量**（长度 vs 计数）、**不同率**（`log₂3` vs 1）。
- 故 **"fringing 增长 = Hecke 周期增长"不成立**。若要找增长对应，应把 **fringing 替换矩阵的 Perron 特征值**与 **`𝒪_4` 上的替换/编码增长的 Perron 值**相比——两者都需先算出，且目前**没有理由相等**（`log₂3` 是"二分支三级"的 Sierpinski 值，而 `𝒪_4` 的熵是 1）。

---

## 5. 结论与地位

| 命题 | 判定 |
|---|---|
| 结构层：两者都是"自由积下原始周期轨道的编码" | `[对应]` `structural proposal`（多项吻合，非同一对象）|
| **carousel `J`（order 4）↔ Hecke `C₄`（order 4）** | `[对应]` 结构性对接点（精确的"同阶旋转"，但非同一空间）|
| 增长律层：fringing `O(n^{log₂3})` = Hecke 周期增长 | **不成立**（不同量、不同率）|

**对 098.3 的回答**：**carousel 对 Hecke 周期轨道——结构性对应成立（自由积/原始/编码脊/order-4 旋转）；fringing 增长——不成立（不同量、不同率）。**"fractal rotation" 与 geodesic flow 都是"旋转型动力学 + 编码"，但**增长律不可直接对接**。

---

## 6. 残余（`open`）

1. **精确的 order-4 对接**：carousel `J`（六态载体的复单位）↔ Hecke `C₄`（`H²` 上的椭圆旋转）——两者都是"90°"，但**空间不同**（六维代数 vs 双曲面）。是否存在自然同构/嵌入？
2. **编码的精确对应**：零 dessin（`G[2,4,∞]`）↔ 角序（preorder）——都是"编码脊"，但**码的字母表不同**（(2,4,∞) 切割 vs 类 4-循环）。是否有"码的翻译"？
3. **增长律的正确配对**：fringing 替换的 Perron 值 vs `𝒪_4` 替换/编码的 Perron 值——需先各自算出，再比较。
4. **`Hist_4^{ph}` ↔ `τ`-轨道**：`prop:q4-operator-history-knot-map` 的纤维（哪些词给同一轨道）与 `τ`-轨道的等价类（`k,l,m,n` 不变量）是否同构？

---

## 7. 参考

- AEG Paper 3：`paper-3/sections/05-q4-geodesic-knots.tex`（`eq:q4-sign-kernel-presentation`、`prop:q4-hyperbolic-class-knot`、`thm:q4-zero-dessin-coding-spine`、`warn:q4-spine-not-template`、`prop:q4-operator-history-knot-map`）。
- Pushkarev–Byzov 2014：Thm 6.1、Cor 6.3、Thm 6.4。
- 相关：note 26/30（Donaghey 树层）、note 34/39（carousel/典范化）、note 40/41（总览）；OQ-098.3。
