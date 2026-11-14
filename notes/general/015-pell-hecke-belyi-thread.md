# 015 — Pell、{∞,4}、Hecke Hauptmodul 与 Belyi 映射：非平凡零集与穿线多项式

> **文档性质**：算术表达式几何（AEG）研究笔记（015：Pell 线程的整合——统一常数、Hecke 零网络、对偶网格、平坦结构、Belyi/dessin 与穿线多项式）
> **前置依赖**：笔记一《HTWR Core》公理 I–IV（[001-htwr-core.md](001-htwr-core.md)）、笔记二《精确时空帕累托边界》（[002-htwr-example.md](002-htwr-example.md)）、笔记四《试验场序列选型》（[004-test-sequences.md](004-test-sequences.md)）、笔记十四《Pell 主图》（[014-pell-master-figure.md](014-pell-master-figure.md)）
> **日期**：2026-11-15
> **备注**：本笔记整合 011–027 号可视化/计算脚本（附各 `.py`/`.png`），是这条线程的收敛点；每个陈述标注状态（`PROVED`/`COMPUTATIONALLY VERIFIED EXAMPLE`/`STRUCTURAL PROPOSAL`/`OPEN`）。

---

## 一、统一常数 k

$$k := 3-2\sqrt2 = (\sqrt2-1)^2 = \lambda^{-2} = \left|\frac{\mu}{\lambda}\right|,\qquad \lambda=1+\sqrt2,\ \mu=1-\sqrt2.$$

`k` 同时是：Pell 闭式的收缩因子 `|μ/λ|`；银比的逆平方 `λ⁻²`；`{∞,4}` 铺砌的基本常数（Math.SE 构造）；收敛速率 `|x_n − √2| = 2√2·kⁿ(1+o(1))`。**状态**：恒等式精确（`COMPUTATIONALLY VERIFIED EXAMPLE`）。

## 二、{∞,4} 铺砌 = Hecke 零网络

Hecke 三角形群 `Γ₄ = ⟨J, T⟩`（`q=4`，`λ₄=√2`）：`J: z→−1/z`（2 阶椭圆）、`T: z→z+√2`（抛物），`J²=(JT)⁴=1`。椭圆点 `ε₂=i`（2 阶）、`ε₄=(−1+i)/√2`（4 阶）。Hauptmodul `β` 归一化 `β(ε₂)=0, β(ε₄)=1, β(尖点)=∞`。**paper-3 `thm:q4-hecke-zero-network`（PROVED）**：

- 零网络 `Z(a₄) = β⁻¹([0,1])` = `{∞,4}` Hecke 图；
- `ε₄` 四价奇异零点（锥角 `4π`）、`ε₂` 二价正则零点；
- `a₄=(μ/λ)sinh(λs)`、`g₄=|dW/W|²`、`F²=β/(1−β)`、`W=(F−i)/(F+i)`、`s=log|W|`。

## 三、对偶网格 {∞,4} vs {4,∞}

- **`{∞,4}`（原始）** = `ε₂–ε₄` 弧在 `Γ₄` 下的轨道（零网络）；
- **`{4,∞}`（对偶）** = `a=0` 线（虚轴，E₀ 零线）在 `Γ₄` 下的轨道，在 `ε₂` 处与 `{∞,4}` **垂直相交**。

故 `a=0`（E₀ 的平凡零线）是一条 `{4,∞}` 对偶边；加/乘分叉 `1→2→4→8→20→…` 把它铺成整张对偶网格。**状态**：轨道分叉、垂直相交为精确计算；「`{4,∞}=a=0` 的轨道」为 `STRUCTURAL PROPOSAL`。

## 四、平坦度量与赋值（简单算术解释）

**paper-3（PROVED）**：`g₄ = |dW/W|² = |dζ|²` 是**平坦**度量（`ζ = log W = s + iθ`）。故

- 零集 `a₄=0` ⟺ `s=0`（径向水平线）；对偶 = `θ=const`（角向水平线）；
- `a₄=(μ/λ)sinh(λs)` 只依赖径向坐标 `s`（与 `E₁` 圆盘 `a_D=(μ/λ)sinh(λ·dist)` 同形）；
- 两族垂直网格 = 平坦结构的**径向/角向坐标族**。

这就是「两族相互垂直测地线 + 加乘推进」的几何地基：加/乘 = 平坦坐标的两个方向。

## 五、顶点 a-值（Z[√2] 结构）

`a = −x/y`（E₀ 赋值）在 Hecke 顶点上的取值（`COMPUTATIONALLY VERIFIED EXAMPLE`，矩阵公式 `a(g(i)) = −(ac+bd)`，`g=[[a,b],[c,d]]`）：

$$a(\varepsilon_2\text{-轨道}) = \mathbb Z\sqrt2,\qquad a(\varepsilon_4\text{-轨道}) = 2\mathbb Z+1.$$

特别地 `a(ε₂)=0, a(ε₄)=1`（Hauptmodul 分支值）；`w(ε₄)=|μ|i`；基本单位 `λ,μ = 1±√2` = 「奇数 ± √2」。

## 六、正则 vs 非平凡零集

- **正则 AES 零集恒平凡**（`thm:regular-zero-locus`，PROVED）：`μ≠0` ⟹ 零集光滑，无分支/交叉/多条。`a=(μ/λ)sinh(λs)` 是整流后的普适局部形式，`μ=1, λ=2,3,4,5` 均退化为一条零线。
- **非平凡零集（多条、4 价）必须奇异**：`thm:branched-pullback-zero-germ`（PROVED）——全纯映射 `Φ` 局部次数 `m` 给 `2m` 个半支、锥角 `2πm`。

## 七、一族 = Belyi 映射 / dessins d'enfants

非平凡 AES 零集 = **Belyi 映射的 dessin**：`β: X→P¹`（只在 `{0,1,∞}` 分歧），取 `a=Im β`、`g=|dβ|²/(μ²+λ²a²)`，零集 `β⁻¹(ℝ)`、dessin `β⁻¹([0,1])`。

- `β=zⁿ`：零集 = 过原点 `n` 条直线（`2n` 支）；`n=2`（4 支、锥角 `4π`）是 `{∞,4}` 的 `ε₄` 局部芽；
- `β=T_n`（Chebyshev）：零集 = 节点集（`T_n⁻¹(ℝ)`），根 `u=cos((2k+1)π/2n)` 为**代数数**；
- **LMFDB**（[Belyi maps](https://www.lmfdb.org/Belyi/)）收 1111 个 Belyi 映射（次数 ≤9），按分支三元组 `[a,b,c]`、数域（含 `Q(√2)`）检索——即「一族」的算术目录。

**Belyi 定理 + Grothendieck 纲领**：Belyi 映射 ⟺ 算术曲线；`Gal(Q̄/Q)` 忠实作用于 dessins。非平凡零集（dessin）= 数论的几何表达。**状态**：dessin=零集为已证机制；「可数有理参数几何体 ↔ 数论」为结构图景。

## 八、穿线多项式

**对齐定义**：路径 `P` = 四则运算的群字。搬运 `a`：`+ : a↦a+μ`、`− : a↦a−μ`、`× : a↦a·u`、`÷ : a↦a/u`，`u=e^λ`。从 `a=0` 出发，`P_λ(0) = p(u)`（`u=e^λ` 的（Laurent）多项式）。`μ=1`、`λ=ln n` ⟺ `u=n`。

例（`μ=1`）：`+x`→`u`；`+x+`→`u+1`；`+xx`→`u²`；`++x`→`2u`；`+x+x`→`u(u+1)`；`+x−x`→`u(u−1)`（在 `u=2,3,4` 给 `2,6,12` 矩形数）。

**Chebyshev `T_n` 是穿线多项式与 Belyi 映射的统一**：`T_n(u)` 是 `u` 的多项式（穿线），同时是 Belyi 映射（dessin），根 `cos((2k+1)π/2n)` 为代数数（`T_2` 的根 `±√2/2 ∈ Q(√2)`）。**「多项式根 ↔ 几何体」** = 根标记穿线归零（`a` 回到 0）的特殊 `λ`。

## 九、大图景

$$\lambda = \ln n \ \Longrightarrow\ u = e^{\lambda} = n \in \mathbb Q \ \Longrightarrow\ \text{可数多个几何体，被 } p(u) \text{ 穿线；}$$

`p(u)` 的根 = 使穿线归零的 `λ`（退化/共振几何）。`λ=ln2,ln3,ln4` 在 `u>1`（非退化区），根全在 `u≤1`（`λ≤0`）。

## 十、状态标注汇总

| 结果 | 状态 |
|---|---|
| 统一常数 `k`、收敛率 `2√2kⁿ` | `COMPUTATIONALLY VERIFIED EXAMPLE` |
| `g₄=|dζ|²` 平坦、`a₄` 径向、`thm:q4-hecke-zero-network` | `PROVED`（paper-3）|
| 分支拉回、`thm:regular-zero-locus` | `PROVED`（paper-3/paper-1）|
| 顶点 a-值 `Z√2 ∪ (2Z+1)`、`w(ε₄)=|μ|i`、对偶垂直、各图 | `COMPUTATIONALLY VERIFIED EXAMPLE` |
| `{4,∞}=a=0` 轨道、`A₀=Z(a)`、同一 `k` 贯通 | `STRUCTURAL PROPOSAL` |
| history-to-divisor 函子、canonical 来源、非重言装饰 | `OPEN`（OQ-073/074/076）|

## 附：脚本/图索引（011–027）

`011` wormhole 加速见证 · `012` Pell 四面板 · `013` Poincaré 圆盘 + Ford 虫洞 · `014` 主图 · `015/016` E₀ 赋值分布(+骨架) · `017` Hecke 零网络 vs IFS · `018` 顶点 a-值 + 等值线 · `019` 0 线分叉 · `020` 对偶网格 + 赋值 · `021` 平坦 Hecke 网格 · `022` a₄ 分布（Schwarz 映射）· `023` λ 族分布 + 穿线 · `024` zⁿ Belyi 零集 · `025` 穿线多项式 + 网格 · `026` 大图景穿线 · `027` Chebyshev dessins。
