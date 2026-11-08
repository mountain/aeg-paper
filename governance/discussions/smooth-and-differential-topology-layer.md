# 光滑层与微分拓扑层：在序拓扑与分析之上能加什么、不能加什么

**File:** `governance/discussions/smooth-and-differential-topology-layer.md`
**Status:** Working research note（研究讨论，非权威）
**Version:** 1.0
**Date:** 2026-11-08
**Primary topic:** 是否/如何在 Paper 0 与 Paper I 已有的序拓扑层与分析层之上引入光滑结构与微分拓扑
**Primary paper interface:** Paper 0 §§3, 9, 11--12；Paper I §§3, 5, 7
**Related records:** `governance/discussions/aeg-intensity-plane-and-tube-collapse.md`（其 P4 的
$\lambda$-塌缩族就是本文 §6 候选 D 的那个边界对象；候选 A/B 已落地为 Paper 0 §3.9）
**Authority:** 从属于 `governance/00–08`；本文档本身不是权威规范。所有候选结果的
状态以 `05b-paper-0-status-register.md` 与 `05-mathematical-status.md` 为准；本文
未改动任何论文源码。

> 本记录把一次阅读与推演整理成可复核的工作文档。其中 A、B 两条是初等推论
> （附证明梗概与数值核验），C 条部分证明、D 条是开放问题的重述，E 条是低优先级
> 的重述性观察。凡本文与论文正文不符处，正文与治理文件优先。

**落地记录（2026-11-08）。** 候选 A 与 B 已按本记录第 9 节的落点建议写入
`paper-0/sections/03-aes-and-motion.tex` 的 §3.9
（`subsec:p0-normal-form`）：`prop:p0-leaf-curvature`（叶曲率）、
`prop:p0-normal-form`（正规形）、`rem:p0-normal-form-hypotheses`（假设的适用范围）、
`prop:p0-normal-form-realization`（反向实现）、`cor:p0-normal-form-softness`
（软性）。状态登记于 `05b-paper-0-status-register.md` §2（2026-11-08 amendment）。
与草案的差异有一处需要记下：正规形的假设改为**结构性的**（"每点所在轨道与
`Z(a)` 恰交一次"），而不是"`∇t` 的流完备"，目的是让 Paper I 的
`thm:complete-regular-aes-splitting` 继续作为乘积分解的规范陈述，避免同一个
定理在两篇论文里各留一个版本。候选 C（谱刚性）按本记录保持为未写入的后续项：
其证明现在只差把 `K = κ′ - κ²` 与 `κ = -λ²a/q` 两步按正文记号写出。

---

## 1. 结论摘要

问题问的是"能否在序拓扑与分析技术之上，引入光滑与微分拓扑"。回答分两句。

**第一句（分层判断）。** 光滑不在分析之上，它在分析之下：`∇a`、`Δa`、`dα`、
`[D_u,D_v]` 全部预设光滑性；Paper 0 的底流形本来就是一个光滑定向 Riemann 曲面。
真正能放在"分析之上"的是**微分拓扑**（整体结构、横截性、分层、指标），而不是
光滑性。所以问题应改写为：*在序拓扑层与分析层之间/之上，微分拓扑能贡献什么
整体结构？*

**第二句（内容判断）。** 微分拓扑在 AEG 里有两个真实入口，一个已经被证明堵死，
一个是开着的：

1. **正则范畴被堵死。** 一条正规形定理（候选 A）说明：完备无边正则 AES 的
   assignment 不是独立场，而是"到零集的距离"经 `(μ,λ)` 重参数化：
   `a = (μ/λ)·sinh(λ·dist(·,Z(a)))`（`λ=0` 时为 `a = μ·dist`）。加上软性定理
   （候选 B），正则范畴里**没有**可分类的整体微分拓扑——它等价于"曲面 + 一条
   曲线 + 两个参数"，模空间无穷维。于是 Morse / 配边 / 柄分解在正则范畴必然是
   空的（这与 Paper I 已证的 `M ≅ Z(a) × R` 是同一件事的几何化版本）。
2. **奇点范畴开着，而且缺口正是论文自己标出的。** Paper I §7.6 明说
   "holonomy 是否收敛为 well-defined residue、以及 residue 如何分类两种穿孔机制，
   是开放的（OQ-096.3 的一部分）"。这正是**指标/留数理论**的位置——微分拓扑在
   这里能给出的是一条 Poincaré–Hopf 型整体平衡，而不是又一层光滑假设。

另有一条附带的分层结论（候选 F，可证但很浅）：**光滑结构只能落在 Lawson 侧，
不能落在 Scott 侧**。Scott 拓扑是 T0 非 T1，而任何流形结构（按定义 Hausdorff）
只能细化一个 Hausdorff 拓扑；`[0,∞]` 上与序相容的 Hausdorff 拓扑正是
Lawson/区间拓扑（= Scott ∨ lower）。这条与论文"`Aff⁺` 单侧 → `PGL₂` 双侧"的
主线同构，但它只是**结构性说明**，不是新定理。

---

## 2. 审计：两篇论文里已经有的"光滑"内容

先排除重复劳动。已有的光滑/微分拓扑内容（按论文自身状态）：

| 对象 | 位置 | 状态 |
|---|---|---|
| 正则 AES 公理（光滑定向曲面 + 光滑 `a` + eikonal） | Paper 0 `def:regular-aes` | `PROVED`（定义） |
| 规范算术标架、`X_u a = μ`、`X_v a = λa` | Paper 0 `prop:canonical-arithmetic-frame` | `PROVED` |
| `E_0`：`K = -λ²`、完备、`Δa = 2λ²a` | Paper 0 `thm:basic-hyperbolic-aes`、`prop:laplace-eigenfunction` | `PROVED` |
| 正则零点集是光滑超曲面（正则值定理） | Paper I `thm:regular-zero-locus` | `PROVED` |
| 完备正则分裂 `M ≅ Z(a) × R`（整体微分同胚） | Paper I `thm:complete-regular-aes-splitting` | `PROVED` |
| 参数族零集的淹没性 + 真正性警告 | Paper I `prop:regular-total-zero-set`、`rem:zero-family-properness` | `PROVED WITH STATED HYPOTHESES` |
| 领口（collar）粘贴、过渡微分同胚、剪开/重组 | Paper 0 `def:p0-collar-contract`、`prop:p0-aes-collar-descent` | `PROVED WITH STATED HYPOTHESES` |
| 球管增厚、亏格、柄、洞-盘互补（mod 2 同调） | Paper I §§8.1--8.3 | `PROVED` |
| 锥点、长度完备化、`4π` 锥角 | Paper III（`app-A`、`06-singular-fibers`） | `PROVED`（局部模型） |

**结论：** "引入光滑性"这件事已经完成了；缺的是 (i) 正则范畴的**正规形**，
(ii) 奇点处的**指标结构**。下文的候选 A--D 就针对这两处。

---

## 3. 候选 A：正则范畴的正规形（平行叶层 + 距离表示）

**命题 A（正规形）。** 设 `𝔈 = (M,g,a;μ,λ)` 是正则 AES，`M` 连通、无边、完备。
令 `R(a) = ∫₀^a ds/√(μ²+λ²s²)`，`r = R∘a`。则：

1. `r` 恰是到零集的有符号距离：`r(p) = ±dist_g(p, Z(a))`，符号由 `∇r` 定向决定。
2. `∇r` 的积分曲线是**极小测地线**，且处处正交于水平集。
3. 水平集两两平行：`dist({a=c}, {a=c'}) = |R(c') - R(c)|`，与叶上基点无关。
4. 在 Fermi 坐标 `(t,s)`（`t` 为有符号距离，`s` 为 `Z(a)` 上弧长）中
   `g = dt² + J(t,s)² ds²`，其中 `J(0,·)=1`、`∂_tJ(0,·) = k_g(Z(a))`、
   `∂_t²J = -K(t,s)·J`（Jacobi 方程）。
5. **assignment 没有独立自由度**：`a = (μ/λ)sinh(λt)`（`λ≠0`）或 `a = μt`（`λ=0`），
   即算术值只由"到零集的距离"与 `(μ,λ)` 决定。等价地 `t = R(a)` 与论文的
   `eq:complete-aes-rectification` 是同一个函数。
6. `Z(a)` 是完备测地线（`R`）或闭测地线（`S¹`）；闭的情形 `M` 是柱面，
   且 `Z(a)` 是测地线当且仅当 `Δa|_{Z(a)} = 0`。

**证明梗概。** `|∇r| = 1` 由链式法则与 eikonal 直接得到（论文已证）。对任意向量
`Y`，`⟨∇_{∇r}∇r, Y⟩ = Hess r(∇r,Y) = ½ Y|∇r|² = 0`，故 `∇_{∇r}∇r = 0`，梯度线是
测地线。又 `r` 在 `Z(a)` 上为零、沿梯度线以单位速率增长，故对任意路径
`length ≥ |r(p)|`，而法测地线达到 `|r(p)|`，于是 `dist = |r(p)|`（此步用完备性
保证流整体存在，即论文 `thm:complete-regular-aes-splitting` 的证明已给的完备流）。
平行性由 `∫ da/q` 只依赖端点值得到。Fermi 形式与 Jacobi 方程是法指数映射的标准
公式。第 5 条由 `da/dt = |∇a| = q(a)` 的 ODE 解出。第 6 条由分裂定理 + 一维流形
分类。

**核验（已执行）。** 用 SymPy 在 `E_0` 上逐项验证：
`|∇a|² = μ²+λ²a²`；`Δa = 2λ²a`；水平集（`a=c`）的测地曲率
`k_g = λ²x/√(λ²x²+μ²y²) = -λ²a/q`，与通式 `k_g = (λ²a-Δa)/q` 完全一致；
并且 `k_g` 只依赖 `a`（等参性）。另在欧氏圆环（`λ=0`、`a=μ·dist` 到中圈）上
核验 `J(t) = 1 + t/r₀`，与 `J(0)=1, J'(0)=k_g=1/r₀` 一致。

**状态：** `STANDARD CONSEQUENCE REQUIRING AN IN-PAPER PROOF`。
数学内容不是新的（射流几何/距离函数的标准事实），**价值在它把正则范畴压成一个
分类**，并因此解释了为什么论文的结果都落在具体模型上。

**落点：** Paper 0 §3 新增一小节（如 `subsec:p0-normal-form`），紧跟
`thm:continuous-affine-flow`；或在附录 B 放完整坐标推导、正文只留命题与两条推论。

---

## 4. 候选 B：软性定理（无刚性）

**命题 B（正则范畴是软的）。** 设 `(M,g)` 是连通完备无边曲面，`γ ⊂ M` 是完备
测地线，且法指数 `γ × R → M` 是微分同胚。则对任意 `μ≠0`、`λ`，
`a := (μ/λ)sinh(λ·dist(·,γ))`（`λ=0` 时 `a := μ·dist`）使 `(M,g,a;μ,λ)` 成为
正则 AES；反之由命题 A 每条正则 AES 如此得到。

**推论 B′。** 固定曲面 `M` 上正则 AES 的模空间 = {满足上述条件的测地线} ×
`(μ≠0, λ)`。一般情形**无穷维**；有限维只在空间形式（`K≡const`）时出现。
因此"正则 AES 的分类定理"若不附加条件不可能存在。

**状态：** `PROVED`（依赖命题 A 与法指数的正则性）。
**意义：** 这是一条**负结果**，正好符合仓库的 claim 纪律：它说明正则范畴不能
承载 Paper III 式的构造，必须换范畴（奇点、边界、不完全、或族）。

---

## 5. 候选 C：谱刚性——`E_0` 的唯一性（部分证明）

**命题 C（候选）。** 在命题 A 的假设下再加 `Δ_g a = 2λ²a`（`E_0` 满足，
`prop:laplace-eigenfunction`）。则：

1. 每个水平集的测地曲率为 `k_g = -λ²a/q(a)`，只依赖 `a`（等参族）；
2. 由平行族的 Riccati 方程 `k' = ∓(K + k²)` 与 `a = (μ/λ)sinh(λt)` 得
   `K ≡ -λ²`；
3. 故 `(M,g)` 是 `K=-λ²` 的完备常曲率曲面，`(M,g,a)` 或同构于 `E_0(μ,λ)`，
   或同构于 `E_0` 被一个双曲平移（即一个伸缩 `z↦kz`，属 `Aff⁺(1,R)`）自由
   真不连续作用后的商（柱面）。

**意义：** 这把 `E_0` 从"基本模型"升级为"**唯一**满足谱条件的完备无边正则
AES"，从而给出"为什么是 `E_0`"的答案；同时说明谱条件正是把无穷维软模空间
切成有限维的那一刀。

**状态：** `PARTIALLY PROVED`。第 1 条已证（SymPy 核验）；第 2 条依赖 Riccati
方程的符号约定与平行族的标准公式，需在正文中固定法向符号后逐行写出；第 3 条
需要单独处理闭测地线（柱面）情形与等距群的离散子群论证。
**风险：** 符号约定；柱面情形的等距群是否恰为伸缩子群需再核。
**不得**在未补完全部三步前写成定理。

---

## 6. 候选 D：微分拓扑真正的入口——奇点指标 / 留数

这是本文认为**最值得做**的一条，因为它填的是论文自己声明的空缺。

**现状。** Paper I `prop:puncture-holonomy` 定义 `∮_γ β`（`β = -λa dv`）为穿孔
holonomy，并明说：极限 `γ ↓ p` 是否收敛为 residue、residue 如何分类两种机制
—— 开放（`rem:puncture-holonomy-declared`，属 OQ-096.3）。Paper 0 §12 的
`prop:p0-k4-motion-residue` 是另一件事（assignment 恒等但全状态位移），不可混同。

**第一步（可立即证的小引理）。** `β = -λa dv` 在 `v ↦ v + f(a)` 下只差一个恰当
形式：`β ↦ β - λa f'(a) da = β - d(∫λa f'(a)da)`。故绕单个穿孔的回路积分不变。
因此 residue（若存在）不依赖乘法坐标沿 `a` 方向的选取。这是使该对象良定义的
必要引理，且是初等的。

**第二步（可计算的例子）。** 对 type 1（`prop:isolated-zero-singular-model` 的
圆盘，`a = (2μ/λ)ρ/(1-ρ²) = (μ/λ)sinh(λs)`，`s` 为到圆心的双曲距离），
一旦**声明** `v`（例如取角向坐标，即乘法运动为旋转），回路积分可精确算出。
注意：`v` 不属于奇异 AES 的定义数据，所以"声明 `v`"是实质性的结构选择，
必须像 `rem:puncture-holonomy-declared` 那样显式写出。

**第三步（猜想：算术 Poincaré–Hopf）。** 存在局部指标
`ind_p(a) ∈ R`（或某个加法群），使得对紧化后的奇异 AES

```
Σ_{p∈S} ind_p(a)  =  (1/2π)∫_M K_g dA  +  (边界项)
```

并且 `ind_p` 在两种本质穿孔机制下取可区分的值。这将把
`thm:torsion-stokes`（把体曲率推到边界）与 `prop:puncture-holonomy`
（把边界 holonomy 收缩到点）接成一条整体平衡。

**与已撤回定理的关系。** `thm:p0-punctures-are-critical` 已由
`05b` 的 2026-09-29 修正判为"as printed 为假"（构造的新度量不等于给定 `g`）。
指标路线**不修复**那条定理；它换了一个不依赖"度量可延拓"假设的不变量。
若成立，它可能给出该定理"应当是什么"的正确版本。

**状态：** `OPEN PROBLEM`（第一步除外，第一步为 `PROVED` 级别的初等引理）。
**风险：** (a) `v` 的声明可能不唯一，需证明 residue 对全部允许的 `v` 不变，
而不只是 `v↦v+f(a)`；(b) 指标可能依赖紧化方式（`12-compactification` 已警告
"reconstruction 依赖记录的 atlas"）；(c) type 2 的共形因子以 `|x|^10` 退化，
留数可能发散而非收敛——这本身会是一个有价值的二分结论。

---

## 7. 候选 E：过程侧（半代数分层）——低优先级，只值得一条 remark

历史空间（固定长度 `n`、实常数）是流形 `R^{2n}`，求值映射是**有理映射**
`E_n : R^{2n} × R ⇢ P¹(R)`；非退化轨迹是开子流形，普通可容许域是半代数开集，
极点轨迹是余维一的实解析超曲面。于是：Whitney 分层、三角可剖分、Łojasiewicz
型结论可免费获得；而"普通算术 vs 投影延拓"的区分恰好是**穿墙**（wall crossing）
的语言，与 Paper I `warn:projective-not-ordinary`、`04b` 的 `lem:p0-pole-covariance`
吻合。

**判断：** 这是**重述**而非新定理，收益有限。只建议在 Paper I §3 加一条 remark
（"普通可容许域 = 极点除子的补集；投影延拓 = 穿墙"），不要为此新开一节。

---

## 8. 必须写进论文的 no-go（保护边界）

1. **正则范畴无整体微分拓扑。** 由 A/B，`M ≅ Z(a)×R` 且 assignment 由距离决定；
   配边、柄分解、Morse 理论在该范畴为空（`a` 无临界点）。因此 Paper I 的
   球管/柄/亏格结果是**增厚模型的拓扑**，不是 AES 的内在微分拓扑不变量
   （论文 §8 已如此声明，应在此处复述为 no-go）。
2. **电荷平面可缩 ⇒ 撕裂只是相对周期。** 撕裂 = 曲率 2-形式在两条历史所夹
   2-链上的积分，只依赖相对同调类；`H₂(R²)=0`、`H₂(R³)=0`，故没有闭链周期、
   没有特征类、没有离散不变量。离散性只能来自算术格 `Z²` 或商空间的 `π₁`。
   这与 Paper 0 §10"电荷端点的任何可观察量都探测不到撕裂"是同一条边界的两面。
   **反过来**：`M∖S` 上的穿孔 holonomy 是**真闭链周期**（`H₁(M∖S) ≠ 0`），
   所以微分拓扑的不变量住在 **AES 空间侧**，不在电荷侧。
3. **对 `a` 本身做 Morse 理论是空的**；Morse 只能来自扰动 `a+εf` 或奇点范畴
   （那是 Paper III 的范围）。
4. **接触形式不决定复结构**（已有 `12-interface` 的 open extension 与根
   `AGENTS.md` 的禁令，此处只复述）。
5. **穿孔点不是光滑点。** 不得在光滑范畴内"分类穿孔"；type 1 是距离函数的
   **焦点**（`Z(a)` 从曲线退化为一点，`a=(μ/λ)sinh(λs)` 而 `s` 在焦点不可微），
   type 2 是**焦散/共形退化**（`Crit(ã)` 处 `g` 退化）。正确范畴是层化空间/
   锥流形（Paper III 已在用锥角语言），不是流形。

---

## 9. 落点建议（最小改动）

| 论文 | 位置 | 内容 | 状态 |
|---|---|---|---|
| Paper 0 | §3 新增 `subsec:p0-normal-form` | 命题 A（1–6）+ 推论（`a = (μ/λ)sinh(λ dist)`） | `STANDARD CONSEQUENCE REQUIRING AN IN-PAPER PROOF` |
| Paper 0 | 同上，一条 corollary | 命题 B / B′（软性、模空间无穷维） | `PROVED` |
| Paper 0 | 同上，一条 remark | 光滑≠Scott（候选 F）：光滑只能落在 Lawson 侧 | `STRUCTURAL PROPOSAL`（T0 论证部分为定理） |
| Paper 0 | §12 "Open extensions" | 候选 D 的猜想（算术 Poincaré–Hopf）登记为 open problem | `OPEN PROBLEM` |
| Paper I | §7.6 `prop:puncture-holonomy` 之后 | 第一步引理（`v↦v+f(a)` 不变性）+ 把 residue 问题重述为指标问题 | `PROVED`（引理）/ `OPEN PROBLEM`（指标） |
| Paper I | §3 一条 remark | 候选 E：极点除子、可容许域、穿墙 | `STRUCTURAL PROPOSAL` |
| Paper II | §2 结构函数 | 叶曲率公式 `k_g = (λ²a-Δa)/q` 作为第二条结构恒等式 | `PROVED` |
| Paper III | 已有小节 | 把锥点/焦点语言显式接到"距离函数奇异点" | 保持现有状态 |

不建议：在 Paper 0 或 Paper I 新开"微分拓扑"专章。理由：正则范畴被 A/B 压平，
奇点范畴归 Paper III，专章会与 Paper III 的已证内容重复，违反 `AGENTS.md`
的"避免重复理论"。

---

## 10. 未解决与需人工复核

1. 命题 A(2) 的"极小性"依赖完备性；有边界或不完备时必须降为局部陈述，
   与 `rem:complete-splitting-boundary-warning` 同一处理。
2. 命题 C 的 Riccati 符号约定、柱面情形、等距群论证均未写；不得提前引用。
3. 候选 D 的最大障碍是 `v` 的声明自由度，其次是指标对紧化方式的独立性。
4. 候选 E 是否只是重述，需一次独立审阅裁定；本文倾向"是"。
5. 本文的 SymPy 核验是单作者机器检验，按 `AUTHORSHIP_AND_PROVENANCE.md`
   的常设规则，**不构成独立人工复核**。

---

## 附录：核验脚本（SymPy）

```python
import sympy as sp
x, y, mu, lam = sp.symbols('x y mu lambda', positive=True)
a = -x/y
g11 = 1/(mu**2*y**2); g22 = 1/(lam**2*y**2)
g = sp.Matrix([[g11, 0], [0, g22]]); ginv = g.inv(); detg = g.det()

def grad(f):  return sp.Matrix([sum(ginv[i,j]*sp.diff(f,[x,y][j]) for j in range(2)) for i in range(2)])
def lap(f):
    ga = grad(f)
    return sp.simplify(1/sp.sqrt(detg)*sum(sp.diff(sp.sqrt(detg)*ga[i],[x,y][i]) for i in range(2)))

ga = grad(a); q = sp.sqrt(mu**2+lam**2*a**2)
# 1. eikonal
assert sp.simplify((ga.T*g*ga)[0,0] - (mu**2+lam**2*a**2)) == 0
# 2. Laplace eigenfunction
assert sp.simplify(lap(a) - 2*lam**2*a) == 0
# 3. leaf geodesic curvature = (lam^2 a - Delta a)/q, and = -lam^2 a/q
n = ga/sp.sqrt((ga.T*g*ga)[0,0])
kg = sp.simplify(-(1/sp.sqrt(detg)*sum(sp.diff(sp.sqrt(detg)*n[i],[x,y][i]) for i in range(2))))
assert sp.simplify(kg - (lam**2*a - lap(a))/q) == 0
assert sp.simplify(kg - (-lam**2*a/q)) == 0
print("all checks passed")
```

（输出：`all checks passed`。）
