# 研究笔记（Research notes）

笔记按主题分组，并在每个主题目录内独立排序。源文件名使用：

```text
NN-descriptive-topic-slug.tex
```

`NN` 是该目录内的两位阅读/顺序码。它不是数学状态、权威、年代或论文分配码。渲染 PDF 与
本地编译伴侣使用与其源相同的 basename。本地 `references.bib` 保持无编号，因为它是共享
支持文件而非笔记。

主题目录为：

1. `analysis-and-calculus/`
2. `computation-and-resources/`
3. `foundations-and-geometry/`
4. `knots-and-loops/`
5. `projective-condensation/`
6. `thermodynamics-and-renormalization/`
7. `electrodynamics/`
8. `aes/`
9. `general/`

`electrodynamics/` 是归档工作目录而非编号笔记：它持有一份关于经典电动力学接触几何读法
的渲染手稿、插入 Papers 0 与 IV 的两个小节、该工作对话的五份中文源笔记，以及 Paper I
封顶与界面盘计算的一条支线。它的 `NN-` 文件名约定不适用于此；其内容登记与已知过时性
记录于 `electrodynamics/SNAPSHOT.md`。

除非某份治理记录明确赋予更强状态，这些文件仍是历史或探索性研究材料。文件名顺序不把
笔记提升为定理权威。

## 有限域差分与调和分析

- [48 — 有限 F7 上的有限三角学](analysis-and-calculus/48-finite-field-trigonometry.tex)：
  圆锥、角群、ripple 铅笔与有限域 Fourier 分析。
- [49 — 圆锥运动、算术历史与三种有限演算](analysis-and-calculus/49-conic-histories-and-finite-calculi.tex)：
  显式椭圆历史、普通/射影域，以及非分裂、分裂与幂幺运动的 Fourier/Jordan 比较。
- [资源、构建说明、溯源与数学状态](analysis-and-calculus/finite-field-calculi/README.md)。

这两条笔记于 2026-11-06 从 `mountain/math-notes` 的 `7ece143` 迁移而来。AEG 是它们的
维护之家；纳入 Paper I 与椭圆 AES 定义仍是研究任务。

## 复与任意域扩张

- [50 — Paper II：复与任意域扩张](analysis-and-calculus/50-complex-and-arbitrary-field-extension.md)：
  对 Paper II 的三层读法（任意域上的代数骨架、C1 全纯复化、C2 Hermitian 复化、实层）、
  任意域三分法、双赋值字典与路线图。设计笔记；它不改变任何论文源与数学状态登记。
  同伴见证：`analysis-and-calculus/50-complex-arbitrary-field-witness.py`。
- [51 — 复化基本模型与 Riemann–Hilbert 边界](analysis-and-calculus/51-complexified-model-and-rh.md)：
  C1 复化双曲模型（`PGL_2(C)` 不变度量、曲率 $-\lambda^2$、实切片）、Riemann–Hilbert/
  Schwarz 边界理论（Poisson 作为 Cauchy 跳跃、DtN 作为 Hilbert 变换、$C_0\cap L^1$
  定理），以及 C2 Hermitian 伴侣（带 $a(z)=z$ 的完备模型、正曲率、总曲率 $2\pi$、离散
  零轨迹）。同伴见证：`analysis-and-calculus/51-complexified-model-and-rh-witness.py`。

## 序拓扑与区间词汇

- [52 — Scott/Lawson 拓扑与 Adva 区间词汇的相容边界](analysis-and-calculus/52-scott-lawson-adva-interval-boundary.md)：
  把值格 Scott/lower/Lawson 词汇与区间域的反包含信息序分开；记录常量生成元
  `T_s, D_k, ¬` 在何处与端点区间运算一致、项级 `+,-,*,/` 在何处失去锐度/依赖，以及为何
  `ExactZero` 不是 Scott 开集。它还区分区间 Newton 的 `RootExists` 与 `ExactZero`，并把
  观测到的 `contracted=true` 但 `delta_y ∌ 0` 矛盾记录为 `InvalidWitness`。带显式开放问题
  清单的结构性提案；不提升任何论断状态。

## 穿孔 AES 流与约化

- [53 — 穿孔 AES 上的流、三种完备化与约化为 ODE](analysis-and-calculus/53-punctured-aes-flows-and-reduction.md)：
  把穿孔 AES 几何与额外流数据分开；记录三种完备化（拓扑/共形、度量、算术）、规范穿孔
  holonomy 的缺失、可选 `Mon_extra`、作为附加接触/Legendre 结构的 Hamilton/Lagrange 联合
  读法，以及返回 ODE 的约化数据 `(π,τ,σ,U_reg)`。根存在经提升管重放 + Newton 再约化；
  exact-zero 留在值层。带显式开放问题清单的结构性提案。

## 椭圆 AES 计划

- [AES 笔记：椭圆 AES 计划](aes/README.md)：以 Cayley–Klein 实形式族为骨架的真正椭圆
  AES（正曲率、紧化、分析）的设计笔记。
- [01 — 三分法审计与 Cayley–Klein 骨架](aes/01-trichotomy-audit-and-cayley-klein-skeleton.md)：
  五个同名三分法、迹对曲率的区分，以及为何迹三分法在正曲率下坍缩。
- [02 — 椭圆 AES 的算术侧](aes/02-arithmetic-side-of-the-elliptic-aes.md)：
  三层语法/值/实现分裂、有界球面赋值、临界/转向轨迹与值域。

## 双曲热带波前-残差核（HTWR）

> HTWR 笔记以英文为主：每条笔记的规范文件是 `NN-*.md`（英文），与之并排的中文译件为
> `NN-*.zh.md`（2026-11-14 添加），因此整条 HTWR 主线 001–010、014–020 均以双语提供。
> 001 的英文编译渲染为 `003-htwr-core.en.tex` + `003-htwr-core.en.pdf`（pdflatex）。脚本
> 011–046 是笔记 002 与 015–020 的同伴计算/图件。

- [001 — HTWR Core](general/001-htwr-core.md)：极简 quantale→AEG 核心，公理 I–IV（带
  对数 Weil 高度双曲校准的状态 `P¹(Q)`；带成本生成元 fanout `Δ`/erasure `ε` 的装配世界面
  语法；热带波前/Bellman 传输；Bellman–Galois 残差对偶）。`STRUCTURAL PROPOSAL`。
- [002 — 精确时空 Pareto 边界](general/002-htwr-example.md)：条件于公理 I–IV 的定理 1
  （时空不确定下界）与定理 2（Pell 收敛子两相 Pareto 边界）；催化虫洞 Möbius 大步与
  naive 对 Heron 的 fanout 比较。`STRUCTURAL PROPOSAL`（+ 恒等式的 `STANDARD CONSEQUENCE`）。
- [003 — HTWR Core（编译版）](general/003-htwr-core.tex)：001 的 LaTeX 渲染；英文渲染
  [003-htwr-core.en.tex](general/003-htwr-core.en.tex) +
  [003-htwr-core.en.pdf](general/003-htwr-core.en.pdf)。
- [004 — 测试序列](general/004-test-sequences.md)：Pell/Fibonacci 统一到金属均值族、
  Sylvester 与 Recamán；结构定位与状态标签。`STRUCTURAL PROPOSAL` +
  `COMPUTATIONALLY VERIFIED EXAMPLE`。
- [005 — Fanout 成本与区间环绕](general/005-fanout-wrapping.md)：Level-C 见证，naive 对
  Heron 的 fanout 差被再现为精确有理区间环绕差。`STRUCTURAL PROPOSAL` +
  `COMPUTATIONALLY VERIFIED EXAMPLE`；同伴见证
  [005-fanout-wrapping-witness.py](general/005-fanout-wrapping-witness.py)。
- [006 — Split-tube 作为 HTWR 分解](general/006-split-tube-htwr.md)：把 VdP C11 split-tube
  形式化为 HTWR「主线 + fanout 辅助」分解；证明块三角性（phase/action 不读变分 `φ`）并
  检查逐项环绕约化。同伴见证 [006-split-tube-witness.py](general/006-split-tube-witness.py)。
- [007 — Pan 与 Encke 缝边缘波](general/007-pan-encke-farey.md)：把 Pan Lindblad 共振阶梯
  `x=m/(m±1)` 读作 Farey/Ford 结构；aeglib 认证共振半径（Encke 外缘 m=551）与共振重叠开缝
  判据。`STRUCTURAL PROPOSAL` 读法；同伴见 `aeglib/python/examples/pan_encke_*.py`。
- [008 — Encke 密度波色散与波长](general/008-encke-density-wave.md)：闭式解出紧绕密度波
  色散；径向波长为 `c²/(GΣ) ≈ 0.75 km`，在共振处并向外递减（环绕），匹配观测到的
  「波长平滑变化」签名。同伴见证 [008-encke-density-wave-witness.py](general/008-encke-density-wave-witness.py)。
- [009 — Encke 边缘模冷 WKB 测试（负）](general/009-encke-edge-mode-wkb.md)：在冷 WKB 极限
  测试 Papaloizou–Lin 边缘模；仅当 `m < 551` 时转向点位于边缘之外，故测得的 `m ≈ 2800`
  边缘波**不是**冷 WKB 边缘模（evanescent 衰减 ≈ 0.5 m）。同伴见证
  [008-encke-edge-mode-wkb.py](general/008-encke-edge-mode-wkb.py)。
- [010 — Encke 扇贝边缘作为 Pan 的潮汐畸变](general/010-encke-scalloped-edge-tidal.md)：
  最终闭合——边缘波是 Pan 的**静态潮汐畸变**（受迫本轮）：振幅 `GM_P/(κ²d²) ≈ 0.79 km`、
  方位 FWHM ≈ 249 km，匹配图像（0.65 km、~300 km）。同伴见证
  [010-encke-scalloped-edge-tidal.py](general/010-encke-scalloped-edge-tidal.py)。
- [014 — Pell 主图](general/014-pell-master-figure.md)：集成 2×3 图——Ford 圆 + HTWR 高度
  （公理 I）、`{∞,4}` Poincaré 圆盘镶嵌（尖点 `w(±(√2−1))`）、`P²−2Q²=±1` 上 `Z[√2]` 的
  单位、收敛律 `|x_n−√2| = 2√2 kⁿ`、k=8 催化虫洞深度剖面，以及 Sylvester 无虫洞对照——
  由 `k = 3−2√2 = (√2−1)² = λ⁻²` 统一；推导四门交叉的两个 `ln Q_k` 抵消（各省 `ln Q_k`）。
  `STRUCTURAL PROPOSAL` 读法 + `COMPUTATIONALLY VERIFIED EXAMPLE` 恒等式。同伴
  [014-pell-master-figure.py](general/014-pell-master-figure.py) +
  [014-pell-master-figure.png](general/014-pell-master-figure.png)；发展轨迹
  [011-wormhole-acceleration-witness.py](general/011-wormhole-acceleration-witness.py)、
  [012-pell-hyperbolic-viz.py](general/012-pell-hyperbolic-viz.py)、
  [013-pell-poincare-wormhole.py](general/013-pell-poincare-wormhole.py)。
- [015 — Pell、{∞,4}、Hecke Hauptmodul 与 Belyi 映射](general/015-pell-hecke-belyi-thread.md)：
  Pell 主线的整合——统一常数 `k = 3−2√2 = (√2−1)² = λ⁻²`；作为 Hecke Hauptmodul 零网络
  `β⁻¹([0,1])` 的 `{∞,4}` 镶嵌（在 `ε₄` 处 4-价、锥 `4π`）；对偶网格 `{∞,4}` 对 `{4,∞}`
  （`a=0` 线的轨道）；带径向赋值 `a₄=(μ/λ)sinh(λs)` 的平坦度量 `g₄=|dζ|²`；顶点 a 值
  `Z√2 ∪ (2Z+1)`；非平凡零集 = Belyi 映射 / dessins d'enfants（LMFDB）；以及穿线多项式
  `p(u) = P_λ(0)`（`u=e^λ`），用 Chebyshev `T_n` 统一穿线与 Belyi。同伴 015–027
  （`*.py`/`*.png`）；状态 `PROVED` + `COMPUTATIONALLY VERIFIED EXAMPLE` +
  `STRUCTURAL PROPOSAL`，开放 OQ-073/074/076。
- [016 — C₂*C₄ 正规形、撕裂、偶阶 Belyi、{7,4}](general/016-c2c4-tearing-belyi-f7.md)：
  `{∞,4}` 的四个构造接口——固定 `013` 非自由 IFS（`F₃=F₂⁻¹, F₄=F₁⁻¹`）并给出无碰撞
  Bass–Serre 树 `T₄` 的 `C₂*C₄` 正规形；`F₂⋊C₄` 撕裂交换子 `[α̃,β̃_⊥]=T⁴`；偶分支 Belyi
  判据（q=4 符号保护）；以及 `Γ₄↠PSL₂(F₇)` `{7,4}` 紧化（亏格 10、`F=24,E=84,V=42`）。
  同伴 [028-c2c4-tree.py](general/028-c2c4-tree.py) + [028-c2c4-tree.png](general/028-c2c4-tree.png)；
  状态 `PROVED` + `STRUCTURAL PROPOSAL`。
- [017 — Cayley 模型与共形双曲统一](general/017-cayley-model-conformal-hyperbolic.md)：
  带分形边界的 Cayley 树 4-边（= `F₂` 4-正则树 = `T₄`）、双曲度量 `g=(dx²+dy²)/L²`
  （`L` = Manhattan 深度，`K=−2`）；统一三个 `{∞,4}` 实现的引理
  `K=fΔf−|∇f|²`（调和深度 ⟹ 常曲率）——Poincaré（`f=y`，`K=−1`）、Cayley（`f=L`，`K=−2`，
  `g_C=½g_P` 位似）、Hecke（`f=|W|=e^s`，`K=0`，平坦展开映射）——带深度对应
  `y ∼ L ∼ e^s`。同伴 [030-cayley-model-hyperbolic.py](general/030-cayley-model-hyperbolic.py)、
  [031-conformal-hyperbolic-proof.py](general/031-conformal-hyperbolic-proof.py)；状态
  `PROVED` + `STRUCTURAL PROPOSAL`。
- [018 — Cayley 模型上的赋值、对偶、加乘、Eikonal](general/018-cayley-assignment-duality-eikonal.md)：
  Cayley 树上 `a` 的分布（`a(gε₄)=(AD+BC)−√2(AC+BD)`、奇整数、坍缩、Pell 轴
  `P_{2d+3}`）；原 `{∞,4}` 对偶 `{4,∞}`（垂直平分线、零线）；水平线（射线）⊥ 梯度线
  （圆、`H²` 测地线）；加乘分解（蓝 = 加零、原点 = 乘零、绿圆 = 乘尺度 `1/2,1/4,1/8`、
  45°/135° 对角线 = 加轴 `a=∓1`）；Eikonal 方程 `|∇a|²=μ²+λ²a²`（= AES 公理）及其角（射线）
  与径（圆、`e^s`）面；以及 Cayley 模型上的 Eikonal 填充 `a=(μ/λ)sinh(λL)`，带可数多个
  脊（中轴）奇点。同伴 032–038；状态 `PROVED` + `COMPUTATIONALLY VERIFIED EXAMPLE` +
  `STRUCTURAL PROPOSAL`。
- [019 — Schwarz–Christoffel 方形、`{∞,4}` 嵌入、光滑 Eikonal 填充](general/019_sc_square_eikonal.md)：
  lemniscatic Schwarz–Christoffel 映射 `S(w)=(e/K₊)∫₀^w dζ/√(1+ζ⁴)`（`K₊=Γ(1/4)²/(8√π)`）
  把单位圆盘映到 `Q_e=[−e,e]²`；四个尖点与 Pell 角相位锁；带四线 Wirtinger 证明 `K≡−1`
  的共形深度 `f_SC`；两个无冲击正交 Eikonal 填充（径向 squircle 与全局尖点到尖点）；以及
  上包络穿透 `L_true`（在星形假设下固定 `038` 的内部伪零，一般情形为下界）。同伴
  [039-sc-square-eikonal.py](general/039-sc-square-eikonal.py) +
  [039-sc-square-eikonal.png](general/039-sc-square-eikonal.png)；状态 `PROVED`
  （`K≡−1`、Eikonal、假设下 `L_true`）+ `STRUCTURAL PROPOSAL`（加乘重整化）。
- [020 — 加/乘线、图势、边界值、尖点 4-边形](general/020-cayley-add-multiply-potential-boundary.md)：
  paper-0 框架 `X_u=(−μy,0)`（水平、ADD）⊥ `X_v=(0,−λy)`（垂直、MULTIPLY）——修正
  `040`，带随 `a` 变化的水平对加角 `arctan(1/|a|)`；图势 `a(node)=(μ/λ)sinh(λd)`
  （node = 分支奇点、edge = Eikonal 流、根 `a=0`、值 `0→16→1023`）；边界值判据
  `ℓ_e=|β(Δa)|/λ` 与 E₀/Cayley 比较（奇整数在 E₀ 中以 1D 松弛 2D 可实现、在 Cayley 中
  不可实现）；势染色；E₁ 型蓝方形（`inradius=ln2`、无源中心 `15/16`、不同源强度 =
  `a(node)`）；以及尖点 4-边形升级（4 角 = 抛物尖点 → 几何/势/值全变）。同伴 041–046；
  状态 `PROVED` + `COMPUTATIONALLY VERIFIED` + `STRUCTURAL PROPOSAL`（一个反驳：`1/a` 不是
  Eikonal 解）。
