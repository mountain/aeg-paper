# Carousel ↔ iota：猜想与材料勘察

## carousel（角类 4-循环）与 iota（复结构 Ω/J）能否对接？

### Research Note v0.1 · 2026-11-01

**结论先说**：用户猜想"carousel 与 iota 有关"——**方向成立、且比预期更具体**：AEG 的 **iota（六态载体的收缩）** 与 Adva 的 **iota frame** 是**同一个对象**（手性载体 + 复单位 `Ω²=-1`），其**手性符号律**（循环置换保持 Ω、对换反号）正是 carousel 的"循环搬运"所对应的结构。但**精确识别尚未建立**：carousel 的计数影子是**阶 2**（Klein 侧），而 Ω/J 是**阶 4**（复单位侧）；角级 carousel 是"4-循环 + 指标平移（screw）"，复结构只解释其**旋转部分**。

---

## 0. 材料

- **AEG 侧**：`paper-5/sections/04-six-state-carrier.tex`（六态载体、`Ω=TSR`、手性符号律）；`paper-5/sections/06-multiplicity-equivariance.tex`。
- **Adva 侧**（`~/work/public/adva`）：
  - `docs/research/0010-causal-cut-chirality-cube.md`（手性载体的因果割推导，`J²=-I`）；
  - `knowledge/received/iota-frame-knowledge-2026-09-17-v1/materials/{frame.md,algebra.py}`（iota frame = 复结构 J）；
  - `docs/research/0224-four-left-nested-iota-frames.md`（`{e,i,iota}` 框架）；
  - `docs/research/0168-switch-swap-and-braid-under-the-iota-substrate.md`（iota 组合子不承载辫子）；
  - `murphy-iota-v0/`、`trials/iota-projection-round-01/`（iota 组合子 / SKI 基底）。
- **carousel**：Pushkarev–Byzov 2014 Thm 4.3、Cor 4.4（见 note 26/30）。

---

## 1. 三个 "iota"（必须分开）

### (A) AEG 的 iota：切收缩 / 内积（六态载体）

`c_i = ε_i + ι_i`（`ε` = 有向交换的外积、`ι` = 切收缩/内积），满足
`c_ic_j + c_jc_i = 2δ_ij I`。于是
`Ω = c_1c_2c_3 = TSR`，`Ω² = -1`，`J = Ω·` 在三个面
`W_T=⟨T,SR⟩, W_S=⟨S,RT⟩, W_R=⟨R,TS⟩` 上各取
`[[0,-1],[1,0]]`，`χ_J(λ)=(λ²+1)³`。

**手性符号律**（`prop:sign-law`）：对三方向置换 π，
`P_π Ω P_π^{-1} = sgn(π)Ω`。即**循环（偶）置换保持 Ω，对换（奇）置换把 Ω 反号**。

### (B) Adva 的 iota frame：割坐标上的复结构

`J = [[0,-I],[I,0]]`，`J² = -I`，作用在**双倍割坐标** `Q^{2n}` 上（实块 + 虚块）；
`H0 = L/(2d_max)`（割图的组合 Laplacian）、`H = diag(H0,H0)`；
`A = -JH`（实时生成元），`U(t) = exp(tA)`；
**"e = 自然指数、i = J"**（`frame.md §"Real paired coordinates"`）。

**关键**：Adva `0010` 的手性载体
`W = (T⊕SR) ⊕ (S⊕RT) ⊕ (R⊕TS)` 与 AEG Paper 5 的
`W = Λ¹E ⊕ Λ²E`（`E=⟨T,S,R⟩`）**是同一个 6 维空间**，`J²=-I` 与三个"面-对极面"平面逐项一致。**即 AEG 的 iota 与 Adva 的 iota frame 是同一对象的两种写法。**

### (C) Adva 的 iota 组合子：SKI 单组合子基底

`ιx = xSK`，`I=ιι`、`K=ι(ι(ιι))`、`S=ι(ι(ι(ιι)))`；`murphy.iota`、`iota-lang`。
**0168 已明确否定**它承载"辫子/switch/swap"：iota 的诉求是**收敛（唯一范式）**，而辫子记录**发散（不同路线）**——"一台以抹除路线为目标的机器不能承载路线"。

---

## 2. carousel 的精确内容（含计算）

**Thm 4.3（细分 carousel）**：τ 把角类搬运：
`SR → LL(1)`，`LL(k) → RL(k)`，`RL(k) → RN(k)`，`RN(k) → LN(k)`，`LN(k) → LL(k+1)`，末 `RL → SR`。
即：**核心是 {LL,RL,RN,LN} 上的 4-循环，SR 为基点，指标 k 在绕一圈后 +1**。

**Cor 4.4（计数影子）**：`(k',l',m',n') = (n+1, k, l-1, m)`，且恒有 `k=m+1, l=n+1`。

**本次计算验证**（`research/` 脚本，$n\le6$）：
- 公式与约束 `k=m+1, l=n+1` 对全部树成立；
- 计数映射 `M` 在约束面上是**对合（阶 2）**：`(2,3,1,2) ↔ (3,2,2,1)`。

**读法**：carousel 在**类级**是 4-循环（与 `Ω`/`J` 的阶 4 对齐），但在**计数级**因约束退化为**阶 2**（Klein）。

---

## 3. 猜想评估

**成立的部分（强连接）**：
1. **iota 与 carousel 都是"手性/定向"结构**：AEG iota 的手性符号律 `sgn(π)` 与 carousel 的左右（LL/RL/LN/RN）是同一"定向双覆叠"。
2. **iota 给出复单位 Ω（阶 4）**，carousel 的类级核心是 **4-循环**——两者阶数一致（4）。
3. **AEG iota = Adva iota frame**（同一 6 维载体），所以"iota"这一侧是**丰富且一致的**，不需要再借外部。

**未成立 / 错位的部分（诚实标注）**：
1. **计数影子阶 2 ≠ Ω 阶 4**：carousel 在 `(k,l,m,n)` 上是**对合**，而 Ω 是**复单位**。所以"carousel = Ω-作用"若指计数级，**不成立**。
2. **"指标平移"无对应**：carousel 是"4-旋转 + k 平移"的 **screw**；复结构 J/Ω 只提供**纯旋转**，不提供平移。故 iota 至多解释 carousel 的**旋转部分**，不解释**平移（指标）部分**。
3. **iota 组合子（C）不是载体**：0168 已否定它承载辫子类结构；若把"iota"读成组合子，则方向相反（收敛 vs carousel 的循环/发散）。

**最可能成立的精确表述（待证）**：
> carousel 的**类级 4-循环** = 手性载体复单位 `Ω`（或 iota frame 的 `J`）的 **Z/4 旋转**在角类上的**离散影子**；指标 k 的平移是**另加的高度/分级**，不在 `J` 内。

---

## 4. 要精确化需要什么（open）

1. **映射**：给出"角类 {SR,LL,RL,RN,LN} → 六态载体 {T,S,R,SR,RT,TS}"的显式映射（或证明不存在这样的自然映射）。
2. **作用对齐**：在此映射下，验证 τ 的 carousel = `J`（纯旋转）**或** `J`∘(指标平移)。若为前者，则 4-循环可解释；若为后者，需要给"平移"一个载体侧的对象（例如 iota frame 的 `H`/分级）。
3. **阶数矛盾**：解释"计数级阶 2 vs 类级阶 4 vs Ω 阶 4"三者的关系（预期：计数量是类级 4-循环的**商**，商掉指标后坍缩为阶 2）。
4. **carousel 与 fringing 的关系**：fringing 使轨道长三倍（`Δ(Q(T))=3Δ(T)`），这与 `O(n^{log₂3})` 是否与 iota frame 的 `exp(tA)` 有谱对应？（098.3 的另一半。）

---

## 5. 地位与残余

| 命题 | 地位 |
|---|---|
| §1 AEG iota = 切收缩、`Ω²=-1`、手性符号律 | `CLASSICAL`（Paper 5 `prop:one-complex-unit`、`prop:sign-law`）|
| §1 Adva iota frame = 复结构 J、`J²=-I` | `CLASSICAL`（adva `frame.md`、`0010`）|
| §1 AEG iota = Adva iota frame（同一载体）| `[对应]` `structural proposal`（逐项一致，但作为"同一对象"的正式声明需审计）|
| §2 carousel 公式与计数影子阶 2 | `COMPUTATIONALLY VERIFIED EXAMPLE`（$n\le6$）+ `CLASSICAL`（Cor 4.4）|
| §3 carousel 类级 4-循环 ↔ iota 复单位 | `[对应]` **conjecture / structural proposal** |
| §3 计数影子阶 2 与 Ω 阶 4 的错位 | 诚实标注（**不**声称相等）|

**残余（`open`）**：§4 的 1–4；以及"iota 组合子是否另有 carousel 读法"（0168 的否定是针对辫子，未针对 carousel，但同属"发散 vs 收敛"张力，需单独考察）。

---

## 6. 参考

- AEG：`paper-5/sections/04-six-state-carrier.tex`（六态载体、`Ω=TSR`、`prop:sign-law`）；`paper-5/sections/06-multiplicity-equivariance.tex`。
- Adva：`docs/research/0010-causal-cut-chirality-cube.md`、`docs/research/0224-four-left-nested-iota-frames.md`、`docs/research/0168-switch-swap-and-braid-under-the-iota-substrate.md`、`knowledge/received/iota-frame-knowledge-2026-09-17-v1/materials/{frame.md,algebra.py}`、`murphy-iota-v0/`。
- carousel：Pushkarev–Byzov 2014 Thm 4.3 / Cor 4.4；note 26/30。
- 本次计算脚本与 carousel 计数影子：见 §2 所述（`research/` 下随附）。
