# 带孔 AES 上的流、三种完成与约化回 ODE

## 从正则 AES 的拓扑/度量，到 punctures 的端数据，再到根存在

### Research Note v0.1

**2026-11-10**

**地位约定**：Paper 0 的 punctured AES、局部形状、端填充、tearing 与
“无 canonical puncture holonomy”按其既有定理引用；本文把流、约化和根存在
写成 `STRUCTURAL PROPOSAL` 或 `OPEN PROBLEM`，不改变 Paper 0/Paper I 的
claim status。本文不把 punctured AES 说成自带 monodromy，也不把
`contains_zero` 说成根存在。

---

## 0. 问题

已有两层对象：

```text
正则 AES:       (M, g, a; μ, λ),  eikonal |∇a|² = μ² + λ²a²
punctured AES:  (M̄, S, g, a; μ, λ),  M = M̄ \ S
```

Paper 0 已给出 punctured AES 的定义、puncture 的局部形状、共形端填充、
任意有限孔数的构造，以及一条关键负结果：

> **AES 数据没有 canonical puncture holonomy。**
> `a` 是 `M` 上的单值函数；水平结构是 `a` 的水平集叶状结构；AES 数据
> 不额外给出连接。contact holonomy 是**加入 charge projection 之后**的
> 结构，活在 charge plane，不是 puncture 的 holonomy。

因此“带孔 AES 上的流”不能写成：

```text
(M, g, a) 自动决定一个带 monodromy 的流
```

流是额外的动力数据；monodromy 如果要出现，也必须是额外声明的结构，
不能归给 AES 本身。

---

## 1. Paper 0 已经建立的东西

### 1.1 Punctured AES 的定义

`def:p0-punctured-aes`：`M = M̄ \ S`，`(M,g,a;μ,λ)` 是 regular AES；
每个 `p∈S` 都没有邻域能把 `g,a` 同时延拓成 regular AES。
所以 puncture 不是“随便删掉的点”，而是 regular structure 真正不能延拓的点。

### 1.2 局部形状与三种“完成”不同

Paper 0 明确区分：

1. **拓扑完成**：把 end 加回 `M̄`；
2. **共形完成**：加一个点并延拓共形结构（`prop:p0-conformal-end-filling`）；
3. **度量/算术完成**：`g` 或 `a` 是否光滑延拓，是否仍满足 regular AES。

单孔模型已经显示：`g` 可以跨 puncture 光滑延拓，而 `a` 不能；
`M` 在 `g` 下可以不完备，但 puncture 距内部点有限距离。
`oriented real blow-up` 保留方向，但不自动延拓算术数据。

### 1.3 Tearing 不被 puncture 改变

`prop:p0-tearing-puncture-independent`：tearing 只依赖 add–scale word；
puncturing 不改变它的值。puncture 改变的是**在曲面上能否完成比较**，
不是 tearing 的值。比较的 canonical 场所是 charge plane，不是曲面。

### 1.4 没有 canonical puncture holonomy

`prop:p0-no-puncture-holonomy`：

- `ker da` 可积，水平结构 flat，无 holonomy；
- AES 数据不额外给连接；
- `a` 单值，所以绕 puncture 一圈不改变 `a`；
- contact holonomy 是 added charge projection 的 holonomy，不是 puncture 的。

这条是本文的硬边界：**不能把 `Mon: π₁(M°)→G` 写成 punctured AES 的 canonical 数据。**
如果流/约化需要 monodromy，它必须是显式附加的 `Mon_extra`。

---

## 2. 带孔 AES 上的流由什么刻画

建议的对象：

```text
PuncturedAESFlow = (E, X, D, End, optional H/L, optional Mon_extra)
```

- `E = (M̄,S,g,a;μ,λ)`：punctured AES；
- `X`：`M° = M̄\S` 上的流/向量场；
- `D`：动力学数据（时钟、截面、返回规则等）；
- `End`：每个 puncture 的端模型（cusp/cone/collar/direction）；
- `optional H/L`：Hamiltonian/Lagrangian/contact 数据；
- `optional Mon_extra`：额外声明的单值性/local system。

重点：

1. **`X` 不由 `(M,g,a)` 决定。** AES 只给 canonical frame / contact
   structure / horizontal distribution；具体流是额外选择。
2. **`X` 可以是单值的。** Paper 0 的 `a` 单值，没有 canonical monodromy；
   不要把“带孔”自动读成“多值”。
3. **若 `X` 在 puncture 有限时间到达，需要端条件。** 因为 puncture 距内部点
   可以有限距离，流可能在有限时间碰到端；此时 `X` 在 `M°` 上可能不完整，
   需要 `End` 指定继续/停止/爆破规则。
4. **`Mon_extra` 是额外结构。** 只有显式选择 cover/local system 时才有；
   不能从 AES 数据推出。

### 2.1 与 canonical frame 的关系

正则 AES 的 canonical frame `(X_u, X_v)` 给两个 canonical 方向；
contact model 给 `α`、Reeb/水平场、charge projection。  
但一个一般流 `X` 不一定是 `X_u,X_v` 的组合，也不一定是 contact 流。
所以：

```text
canonical frame/contact structure 给“可用的方向/分解”；
具体 X 需要额外声明，并检查它是否 respect 这些结构。
```

## 3. Hamiltonian / Lagrangian 联合观点

在正则部分，若有额外 symplectic/contact 结构，可以写：

```text
X_H = ω^{-1} dH          (Hamiltonian)
L: TM° → R, FL: TM° → T*M° (Lagrangian)
```

联合观点不是“`H` 和 `L` 都全局存在”，而是：

```text
contact Hamiltonian (α, H) + Legendre transform + end/boundary data
```

- `α` 是 Paper 0 的 contact form；`H` 是额外选择的 Hamiltonian；
- Legendre 变换在正则部分局部连接 `H` 和 `L`；
- 到 puncture，Legendre 可能退化，作用量可能多值；
- 多值性若出现，来自**附加的 cover/action**，不是 AES 的 canonical monodromy；
- contact holonomy 活在 charge plane，不是 puncture 的 holonomy（Paper 0）。

对 VdP 要特别声明：VdP 是耗散 Liénard 系统，**不是 Hamiltonian**。
H/L 联合观点可用于其某些提升/比较，但不能把 VdP 直接当 Hamilton–Lagrange 流。
AES-native 的 VdP 流应走 Liénard/AM 提升，而不是强行套 `H/L`。

## 4. 拓扑与度量如何从正则 AES 推广到 punctures

必须分三层，且分别声明：

### 4.1 拓扑层

```text
M° = M̄ \ S  →  stratified end compactification
```

- regular stratum：note 03 的四边形/区间邻域基；
- end strata：cusp/cone/collar/direction 的邻域；
- oriented real blow-up 保留方向，但不延拓 `a`；
- 普通点紧化丢掉方向；`M̄` 的点紧化与 real blow-up 不是同一操作。

所以 punctured AES 的拓扑不是“note 03 的 D 再加一个点”，而是
**regular stratum + end stratum** 的分层空间。note 03 的 Scott 区间域只覆盖
regular chart；端部的区间域/邻域语义仍是 open。

### 4.2 度量层

在端部取局部模型：

```text
cusp:   ds² = (du² + dv²)/v²
cone:   ds² = dr² + r² dθ²
collar: ds² = du² + dv²/v²
```

用 `\bar g = ρ² g` 做共形/加权完成，并分别验证：

- `g` 是否完备；
- `ρ²g` 是否光滑延拓；
- 端部曲率/体积行为；
- puncture 是否有限距离。

Paper 0 已经说明：拓扑/共形完成不等于度量完成；`g` 可以延拓而 `a` 不可以。

### 4.3 算术层

regular AES 的 eikonal 只在 `M°` 上要求：

```text
|∇a|²_g = μ² + λ²a²
```

到 puncture，`a` 可能：

- 有有限极限但不可微；
- 发散；
- 有分支/多值（若额外 cover）；
- 或根本不能延拓。

因此 punctured AES 的“算术完成”必须作为 `End` 数据显式给出；
不能从 `g` 的延拓自动推出。

## 5. 约化回 ODE 的数据

要谈“回到 ODE 流”，需要显式 reduction datum：

```text
R = (π: Ẽ → E_ODE, τ, σ, U_reg, optional Mon_extra)
```

- `π`：从 lift/cover 到 ODE 相空间/截面的投影；
- `τ`：时钟；
- `σ`：返回截面；
- `U_reg`：约化有定义的开集（避开 punctures）；
- `Mon_extra`：若 lift 有额外单值性，显式声明；AES 本身没有 canonical Mon。

约化条件：

```text
dπ · X_Ẽ = X_ODE ∘ π
dτ · X_Ẽ = 1
```

若 `Mon_extra` 非平凡：

- 它作用在纤维上；
- 周期轨道可以是普通周期，也可以是相对周期/多值返回；
- 必须在 cover 上解，或取周期的最小公倍；
- 不能把多值返回当成单值 ODE 周期。

若 `Mon_extra` 不存在（AES canonical 情形）：

- `a` 单值，流可单值；
- 约化不需要 monodromy 语言；
- 但仍需要 `π,τ,σ,U_reg`。

## 6. 根存在怎么衔接

在 lift/cover 的正则 chart 上：

```text
TubeWitness: seed → z(T) → F(c), J(X)
```

然后：

1. 区间 Newton 在 `Ẽ` 上证明 `RootExists in X`；
2. 检查 root 落在 `U_reg`，不落在 punctures；
3. 用 `π` 映回 ODE：
   ```text
   p = π(root)
   ```
4. 若 `Mon_extra` 非平凡，取 cover 上的周期/相对周期，不能用单值 `F` 冒充；
5. 值层再给 `ZeroStatus`；`ExactZero` 只在 `[0,0]` 或 exact-zero bridge 下。

关键顺序：

```text
lift 上 tube replay
  → RootExists on Ẽ
  → reduction π
  → ODE periodic orbit
  → 值层 ZeroStatus
```

不能反过来：不能先在 ODE 值层看到 `delta_y` 区间含 0，再说“AES 流有根”。

## 7. 对 C11 的具体判断

当前 C11 tube 在 `(x,y,T)` 的 **ODE chart** 里，不在 punctured AES 上。

- 若 VdP 的有限周期轨道不经过 puncture/端部，ODE tube replay + Newton
  可以在 **ODE chart** 上证明根存在；
- 这仍不是 AES-native 的根证明，因为没有给出 `(π,τ,σ,U_reg)` 和
  `dπ X = X_ODE`；
- 若轨道经过 puncture，必须先用 `End` 数据决定流是否继续；否则只能
  `UnknownDomain`，不能声称根存在；
- 若引入 lift 的 `Mon_extra`，还要证明它不改变返回截面/时钟，或显式处理
  相对周期。

所以 C11 当前仍是：

```text
ODE chart 的 partial/numeric+Newton witness，
不是 punctured AES 上的 root certificate。
```

## 8. 必须禁止的说法

1. “punctured AES 自带 puncture monodromy” —— 错；Paper 0 证明没有
   canonical puncture holonomy。`Mon_extra` 只能是额外声明。
2. “拓扑补点 = 度量完成 = 算术完成” —— 错；三者必须分开。
3. “`(M,g,a)` 决定流” —— 错；流是额外动力数据。
4. “VdP 是 Hamiltonian” —— 错；VdP 是耗散 Liénard。
5. “interval 含 0 ⇒ 根存在” —— 错；根存在靠 Newton replay，exact-zero 是值层。
6. “charge plane 的 holonomy 是 puncture 的 holonomy” —— 错；Paper 0 明确
   这是 added charge projection 的 holonomy。

## 9. 开放问题

- **Q1**：punctured AES 的 regular stratum + end strata 上，note 03 的区间域
  如何分层？端部是否需要单独的 cusp/cone interval domain？
- **Q2**：`End` 数据的最小充分集是什么（方向、共形类、度量渐近、`a` 的极限/
  分支）？不同端模型何时给出同一流？
- **Q3**：`PuncturedAESFlow` 中 `X` 的端条件如何写，才能保证有限时间/有限
  距离行为可判定？
- **Q4**：H/L 联合在端部退化的分类；作用量多值性何时来自 `Mon_extra`，
  何时只是 coordinate artifact？
- **Q5**：reduction datum `(π,τ,σ,U_reg)` 的最小条件，以及
  `RootExists` 经 `π` 保持的定理。
- **Q6**：`Mon_extra` 的 Scott/区间语义；多值返回如何用 tube replay 表达。
- **Q7**：VdP 的 AES-native lift 是否存在显式 `(π,τ,σ)`，并且轨道避开 punctures？

## 10. 参考

- Paper 0 §11 `sec:p0-holed`：`def:p0-punctured-aes`、
  `prop:p0-puncture-tangent-cone`、`prop:p0-tearing-puncture-independent`、
  `prop:p0-no-puncture-holonomy`、`prop:p0-puncture-local-picture`。
- Paper 0 §12 `sec:p0-compactification`：`prop:p0-conformal-end-filling`、
  `thm:p0-arbitrary-k-punctures`、`def:p0-collar-contract`。
- `notes/analysis-and-calculus/09-order-topology-scott-lawson.md`
  （Scott/lower/Lawson、`T_s,D_k,¬`）。
- `notes/analysis-and-calculus/52-scott-lawson-adva-interval-boundary.md`
  （区间域、exact-zero、Newton 存在性边界）。
- `notes/aes/03-quadrilateral-neighborhoods-and-scott-continuity.md`
  （regular chart 的区间域与 Scott 连续性）。
- `hilbert-16/notes/2026-11-07_30_AM生成与带孔AES.md`
  （AM 生成、punctured AES、约化与孔数非计数不变量）。
