# Scott/Lawson 拓扑与 Adva 区间词汇的相容性边界

## 从值格上的加/乘分离，到区间 domain 上的 exact-zero 判断

### Research Note v0.1

**2026-11-10**

**地位约定**：domain theory 与区间算术的经典事实标 `CLASSICAL`；把 AEG 的
`T_s, D_k, ¬` 对到 Adva 区间操作标 `REFORMULATION`（仅在常值生成元层面）或
`STRUCTURAL PROPOSAL`；任何“区间 domain 的 Scott 拓扑 = 值格 Scott/Lawson”
或“term-level interval +,* 连续”的断言标 `OPEN PROBLEM`。本笔记不改变
`09`–`20` 的任何 claim status，也不把 Adva 的 `ZeroUndetermined` 升级成
`ExactZero`。

---

## 0. 问题

`09` 在值格 `L=[0,∞]` 上给出：

- 加法 `T_s(a)=a+s` 是 Scott 连续嵌入，且 `a≪b ⇔ ∃s>0: a+s≤b`；
- 乘法 `D_k(a)=ka`（`k>0`）是 Scott 自同构；
- 互反 `¬(a)=1/a` 是反序对合，把 Scott 拓扑送到 lower topology；
- Lawson = Scott ∨ lower，恢复 Hausdorff/欧氏拓扑。

`adva` 的 interval enclosure 使用：

- 有理闭区间 `[l,u]`，外向舍入；
- `ExactZero`、`StrictPositive`、`ZeroUndetermined`、`UnknownDomain` 等判断；
- `x-x`、`x/x` 的 dependency 例子；
- exact-zero bridge：`R=N/D`、`0<D≤B`、严格 `|R|<1/B` 才推出 `N=0`。

问题不是“两者是否都叫拓扑”，而是：

> **AEG 的值格 Scott/Lawson 词汇，能否、以何种强度，解释 Adva 的区间对象、
> 区间运算和 exact-zero 判断？**

本笔记只给边界和问题清单，不给“相容性定理”。

---

## 1. 两个载体不是同一个偏序集

### 1.1 AEG 侧：数值序

`L=[0,∞]`，序是通常数值序 `≤`。信息序读作“从下逼近”：

```text
a ⊑ b  ⇔  a ≤ b
```

Scott 开集由 `(a,∞]` 生成；lower topology 由 `[0,b)` 生成；Lawson 是两者的
join，在 `[0,∞]` 上就是通常拓扑。

### 1.2 Adva 侧：区间信息序

候选对象是

```text
I(L) = { [l,u] : 0 ≤ l ≤ u ≤ ∞ }.
```

区间不是数值点；自然的信息序是**反向包含**：

```text
I ⊑ J  ⇔  J ⊆ I
```

即“更窄的区间 = 更多信息”。这与 `L` 的数值序不是同一个偏序集。

因此：

```text
(L, ≤) 与 (I(L), ⊇) 的 Scott 拓扑不是同一个拓扑；
不能把 [l,u] 直接当作 L 的 Scott 开集。
```

这是本笔记的第一个边界。

---

## 2. 区间是双侧对象，不是 Scott 开集

`[l,u]` 同时给出下界和上界：

```text
x ∈ [l,u]  ⇔  l ≤ x 且 x ≤ u.
```

- 下界侧是“从下超过阈值”的信息，接近 Scott 侧；
- 上界侧是“从上低于阈值”的信息，接近 lower topology 侧；
- 闭区间本身在 Lawson 拓扑里是闭的，不是开集；
- 开区间 `(l,u)` 才是两侧开约束的交。

所以准确说法是：

> **Adva interval 是一个双侧约束对象；它的 exact/undetermined 判断是区间上的
> judgment，不是“某点是 Scott 开集成员”。**

这解释了为什么 Adva 要单独区分：

```text
[0,0]        ExactZero
[-ε,ε]       ZeroUndetermined
[1/64,1/64]  StrictPositive
```

`ExactZero` 不是 Scott 开集能表达的；`ZeroUndetermined` 也不是“Scott 开集含 0”，
而是“两侧信息都没有排除 0”。

---

## 3. 常值生成元层面：相容

在 `I(L)` 上定义端点作用：

```text
T_s([l,u]) = [l+s, u+s]
D_k([l,u]) = [kl, ku]          (k>0)
¬([l,u])   = [1/u, 1/l]        (0 ∉ [l,u])
```

`REFORMULATION`：这三条逐字对应 `09` §9 的 `T_s, D_k, ¬`。

- `T_s` 是 `I(L)` 的序同构（反向包含保持），对应加法平移；
- `D_k` 是 `I(L)` 的序同构，对应正尺度自同构；
- `¬` 在**不跨 0** 的区间上是反序对合，把下界/上界互换；
- 跨 0 时没有定义，对应 Adva 的 `UnknownDomain`，而不是“证明有极点”。

因此：

> **AEG 的三个常值生成元与 Adva 的常数平移、正缩放、倒数（零域排除）
> 在端点运算层面相容。**

这是本笔记唯一接近“相容性”的正面结论；它仍是 `REFORMULATION`，不是拓扑定理。

---

## 4. 项级 `+`/`*`：不相容为同态

AEG 的 `T_s` 是**值上的平移**；Adva 的 `x+y` 是**项上的区间运算**。后者有
dependency：

```text
x ∈ [1,2]  ⇒  x - x ∈ [-1,1]，不是 [0,0]
x ∈ [1,2]  ⇒  x / x ∈ [1/2,2]，不是 [1,1]
```

Adva 明确拒绝把这两个 trace 改成 `[0,0]`/`[1,1]`：那些更窄的区间数学上正确，
但不是所选 interval interpreter 的结果。

由此：

1. **项级区间加法不是值格加法的同态。** `T_s` 只加一个常值；`x+y` 同时引入
   两个变量的相关性，区间传播只能给 sound over-approximation。
2. **项级区间乘法不是 Scott 自同构。** `D_k` 是常值正缩放；`x*y` 是双线性
   运算，区间乘法丢失相关性（`x/x` 例子）。
3. **`x-x` 的 `[-1,1]` 不是错误，而是 dependency 的正确记录。** 把它改写成
   `[0,0]` 需要额外的 symbolic identity/rewrite，不是 interval arithmetic 本身。

所以“加法和乘法分开”在 AEG 里是：

```text
加法 T_s  = way-below / Scott 侧
乘法 D_k  = Scott 自同构 / 尺度对称
互反 ¬    = 对偶侧
```

在 Adva 里必须改写成：

```text
常值平移/正缩放 = 生成元层面的相容操作
项级 +,*        = sound over-approximation，不是生成元同态
倒数            = 对偶侧，但要求零域排除
```

这是本笔记的第二个边界，也是最重要的边界。

---

## 5. 区间 domain 的拓扑仍是开放问题

`I(L)` 带反向包含序，是否是连续 domain、紧致元是什么、Scott 拓扑如何描述，
这些是 standard interval domain 的问题，但在本笔记中**尚未逐条核对**。即便它们
成立，也不等于：

```text
I(L) 的 Scott 拓扑 = L 的 Scott 拓扑
```

更不自动给出：

```text
term-level interval +,* 对 I(L) 的 Scott 连续
```

因此下面这些都必须标 `OPEN PROBLEM`：

1. `I(L)` 的反向包含序是否定向完备；定向并是否就是区间交；
2. `I(L)` 的紧致元是否对应“有理端点/有限精度”的区间；
3. `T_s, D_k` 是否是 `I(L)` 上的 Scott 同胚；
4. `¬` 在零域排除的子空间上是否是 Scott/lower 同胚；
5. 项级 `+,-,*,/` 是否 Scott 连续；若不连续，最大连续子代数是什么；
6. Adva 的 `ExactZero/ZeroUndetermined/StrictPositive/UnknownDomain` 与
   Scott/Lawson 开集、闭集、闭包的关系是什么。

第 5 条尤其重要：`x-x` 和 `x/x` 已经说明，**sharpness 的丢失不是拓扑细节，
而是 dependency 的结构性结果**。

---

## 6. exact-zero 判断不能由拓扑开集替代

Adva 的口径：

```text
[0,0]        ExactZero
[-ε,ε]       ZeroUndetermined
```

`simplex... §4` 的 exact-zero bridge：

```text
R = N/D,  N,D ∈ Z,  0 < D ≤ B
若严格证明 |R| < 1/B，则 N=0，R=0。
```

要点：

- floating 值不行；
- 仅“区间含 0”不行；
- 仅“小 residual”不行；
- 必须同时有 denominator bound 和 certified strict residual bound。

这与 Scott 拓扑的关系是：

- `ExactZero` 不是 Scott 开集；
- `ZeroUndetermined` 不是“Scott 开集包含 0”；
- interval containing zero 不证明存在零点；
- Lawson 拓扑可以提供双侧邻域，但不提供 equality proof。

因此 AEG 的恒等式（例如 C11 的 `Δy=0`、`A_hor+∫y²=0`）如果要 exact-zero，
必须额外给出 exact-zero bridge，或者明确保留 `ZeroUndetermined`。

---

## 7. 对 C11 的直接后果

当前证书的输出：

```text
delta_y              = [+/- 1.9e-5]
horizontal_residual  = [+/- 1.2e-4]
```

在 Adva 口径下是：

```text
ZeroUndetermined
```

不是 `ExactZero`，也不是“存在周期轨道”的证明。

- 真正承担存在性的是 Newton inclusion；
- `NewtonWitness` 目前只重放 Newton 代数，`image/J` 仍来自 tube；
- tube 的 soundness 需要独立 replay；
- f64 `vdp_reference` 没有误差界，只是 seed；
- `contains_zero` 不能替代 exact-zero bridge。

所以在补齐 tube replay 和 zero-status 之前，C11 仍是 `PARTIAL`，不是
`CERTIFIED`。

---

## 8. 必须禁止的说法

1. “Adva interval = Scott 开集” —— 错。区间是双侧对象；闭区间在 Lawson 中
   是闭的，不是开集。
2. “interval 含 0 ⇒ 存在零点” —— 错。Adva 明确把它标为 `ZeroUndetermined`。
3. “term-level interval +,* 是 Scott 连续/同态” —— 未证明，且 `x-x`/`x/x`
   显示 dependency 导致 sharpness 丢失。
4. “乘法 = 对偶侧” —— 错。`D_k` 是 Scott 自同构；对偶侧是 `¬`。
5. “AEG 的 Scott/Lawson 已经解释了 Adva 区间算术” —— 目前只有常值生成元
   层面的 `REFORMULATION`；整体解释是 `STRUCTURAL PROPOSAL`/`OPEN PROBLEM`。
6. “`ZeroUndetermined` 可以当 `ExactZero` 用” —— 错。

---

## 9. 开放问题清单

- **Q1**：`I(L)` 的反向包含序的 dcpo/连续 domain 结构；定向并 = 交？
- **Q2**：是否存在 `R: I(L) →` 双侧约束对象的函子，逐字保持 `T_s, D_k, ¬`？
- **Q3**：项级 `+,-,*,/` 的 Scott 连续性；最大连续子代数是什么？
- **Q4**：`ExactZero/ZeroUndetermined/StrictPositive/UnknownDomain` 与
  Scott/Lawson 开集、闭集、闭包的精确关系。
- **Q5**：AEG 恒等式（C11 的 `Δy=0`、`A_hor+∫y²=0`）需要 exact-zero
  bridge 还是只需 `ZeroUndetermined`？如果只需要后者，contract 应如何写？
- **Q6**：`I(L)` 的 Scott 拓扑与 AEG 的 Lawson 拓扑之间是否存在
  reading functor；如果有，它是否是满/忠实？

在 Q1–Q6 有结论前，任何“AEG 拓扑 = Adva 区间词汇”的断言都不成立。

---

## 10. 参考

- `notes/analysis-and-calculus/09-order-topology-scott-lawson.md` §9–§11
  （`T_s, D_k, ¬`、Scott/lower/Lawson、backward adjoint）。
- `notes/analysis-and-calculus/10-scott-lawson-on-paper-1-main-body.md` §1–§3
  （生成元对应、`Aff^+`/`PGL₂` 的 status）。
- `adva/experiments/interval_enclosure/README.md`（区间、外向舍入、exact zero、
  `UnknownDomain`、dependency）。
- `adva/docs/research/simplex-contraction-pascal-calabi-reduction.md` §4
  （exact-zero bridge：`R=N/D`、`D≤B`、严格 residual bound）。
- `adva/docs/research/applied-mathematics-contract-roadmap.md` priority 4
  （区间、舍入、exact-zero/uncertainty 的区分）。
