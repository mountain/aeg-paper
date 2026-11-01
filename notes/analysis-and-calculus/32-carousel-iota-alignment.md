# carousel 与 iota 的作用对齐：尝试与障碍

## note 31 §4 的落地：类→态映射 + τ 的 carousel 是否 = J

### Research Note v0.2 · 2026-11-01

**结论**：**强形式（carousel = J 在六态载体上）不成立**，但失败点**精确且可定位**：carousel 的类级 4-循环（`LL→RL→RN→LN→LL`）**可以**（非典范地）对齐到 J 在**单个平面 4 个带号态**上的 4-循环；但 carousel 的**入口步 `SR→LL`（以及指标 `k` 的平移）**在 J 中没有对应——因为 **J 保持三个平面 `W_T,W_S,W_R` 各自不变**，不能把"根角 SR"送到 4-循环所在的平面。故 **J 解释 carousel 的"旋转部分"，不解释其"入口/平移部分"**。

---

## 0. 目标（note 31 §4 的 1、2 项）

1. 给出"角类 {SR,LL,RL,RN,LN} → 六态载体 {T,S,R,SR,RT,TS}"的显式映射；
2. 在该映射下验证 τ 的 carousel = `J`（纯旋转）还是 `J`∘(指标平移)。

---

## 1. 两边的精确结构

**iota 侧（六态载体）**：`W = Λ¹E ⊕ Λ²E`，`E=⟨T,S,R⟩`；`Λ²E=⟨SR,RT,TS⟩`。
`Ω = TSR`，`Ω² = -I`，`Ω⁴ = I`（已用 6×6 矩阵验证）。`J = Ω·` 的作用：
$$
J(T)=SR,\ J(SR)=-T;\quad J(S)=RT,\ J(RT)=-S;\quad J(R)=TS,\ J(TS)=-R .
$$
三个平面 `W_T=⟨T,SR⟩`、`W_S=⟨S,RT⟩`、`W_R=⟨R,TS⟩`**各自不变**；在每个平面上，J 对**带号态**
`{e,Je,-e,-Je}` 是**单 4-循环**（如 `T→SR→-T→-SR→T`）。

**carousel 侧**：τ 把角类搬运（Thm 4.3）：
$$
SR\to LL(1),\quad LL(k)\to RL(k),\quad RL(k)\to RN(k),\quad RN(k)\to LN(k),\quad LN(k)\to LL(k+1),
$$
末 `RL(m)→SR`。**类级**：核心是 4-循环 `LL→RL→RN→LN→LL`，`SR` 是**入口/基点**，指标 `k` 每绕一圈 +1。

---

## 2. 尝试 1：类 → 6 态的双射？——**不可能**

- 计数不匹配：5 类 vs 6 态，双射不存在。
- 更根本：**J 不是 6 个"正态"上的置换**——它把 `SR ↦ -T`（正态送到带号态），把 `T ↦ SR`，所以 `{T,S,R,SR,RT,TS}` 这个 6 元集**不被 J 保持**。要谈"J 的置换"，必须升到**12 个带号态**（每个平面 4 个）。

**结论**：态级双射（5↔6）在结构上就无解。需要换一种"对齐"的对象。

---

## 3. 尝试 2：类 → 单平面的 4 个带号态（可行，但非典范）

取一个平面（如 `W_T = {T,SR,-T,-SR}`）。它的 J-作用是一个 4-循环：
$$
T \xrightarrow{J} SR \xrightarrow{J} -T \xrightarrow{J} -SR \xrightarrow{J} T .
$$
把 4 个非根类 `{LL,RL,RN,LN}` 依次映到这四个带号态，即可让 **carousel 的类 4-循环 = J 的 4-循环**。例如：
$$
LL\mapsto T,\quad RL\mapsto SR,\quad RN\mapsto -T,\quad LN\mapsto -SR .
$$
则 `LL→RL→RN→LN→LL` 与 `T→SR→-T→-SR→T` 同构（都是 C₄）。

**但**：这是**非典范的**——
- **平面选择 3 个**（`W_T`、`W_S`、`W_R` 完全对称），J 本身不区分；
- **起点/定向 2 种**（`e↦LL` 还是 `e↦RL`）；
- 共 `3×2 = 6` 个候选映射，且**没有内蕴准则**选出其一。

---

## 4. 障碍（精确）：`SR→LL` 的入口步在 J 中没有对应

carousel 不是"纯 4-循环"，而是"**4-循环 + 入口 `SR`**"：
$$
SR \to LL \to RL \to RN \to LN \to LL \to \cdots
$$
其中 `SR→LL` 是**入口**、`...→RL(m)→SR` 是**回绕**、指标 `k` 是**平移**。

在尝试 2 的映射下，`SR` 必须映到某个态。两种可能：
- 若 `SR` 也映到该平面的 4 个带号态之一：则 5 类 → 4 态，**不可单射**；
- 若 `SR` 映到**另一个平面**（如 `W_S` 或 `W_R`）的态：则 `SR→LL` 是**跨平面**的，而 **J 保持每个平面不变**，无法实现跨平面映射。

故：

> **J（纯旋转、保持平面）不能产生 carousel 的入口/平移步 `SR→LL`（及 `LN→LL` 的指标 `k→k+1`）。**

这与 note 31 的预判一致：**J 解释"旋转部分"，`SR` 入口与指标平移是 J 之外的"shift"**。

---

## 5. 结果与意义

| 断言 | 判定 |
|---|---|
| carousel = J 在 6 正态上的置换 | **不成立**（J 把正态送到带号态；5≠6）|
| carousel 的**类 4-循环** = J 在**单平面 4 带号态**上的 4-循环 | **成立（但非典范，6 个候选）** |
| carousel 的**入口/平移步**（`SR→LL`、`k→k+1`）| **J 无法实现**（J 保持平面）|

**最强可证表述**（把 note 31 的 conjecture 精确化）：

> carousel 的**类级 4-循环**是 iota 复单位 `Ω`（或 iota frame 的 `J`）的 **C₄ 旋转**在角类上的**非典范离散影子**（同构于 J 在单平面带号态上的 4-循环）；而 carousel 的 **`SR` 入口与指标平移**是**独立的"shift"结构**，不在 `J`/`Ω` 中。因此 **carousel ≠ J**；是 **carousel = (J-型旋转) + (shift)**，其中 shift 尚未在 iota 侧找到载体。

**对"iota 是否够丰富"的回答**：**够了，但只够到"旋转"这一半**。若要让 shift 也进入 iota 侧，需要 iota 结构里已有的"**分级/高度**"对象——候选是 **Adva iota frame 的 `H`（Laplacian）**（`A=-JH` 的 `H` 部分）或**六态载体的 `Λ¹E↔Λ²E` 分级**。这是一个**新的、可检验的**方向。

---

## 6. 地位与残余

| 命题 | 地位 |
|---|---|
| §1 `Ω²=-I`、`Ω⁴=I`、J 保持三平面、每平面对带号态 4-循环 | `CLASSICAL`（Paper 5 `prop:one-complex-unit`）+ 矩阵验证 |
| §1 carousel 公式与类 4-循环 | `CLASSICAL`（Thm 4.3/Cor 4.4）+ 计算（note 31）|
| §2 态级 5↔6 双射不可能 | 精确（计数 + J 送正态到带号态）|
| §3 类 4-循环 ↔ 单平面 4 带号态（同构 C₄）| `[对应]` 精确（同构）但不典范 |
| §4 入口/平移步无 J 对应 | `[对应]` 精确障碍（J 保持平面）|

**残余（`open`）**：
1. **shift 的 iota 载体**：`H`（Laplacian）或分级 `Λ¹↔Λ²` 能否承载 `SR→LL` 的入口与 `k` 平移？
2. **典范性**：6 个候选映射中是否有某准则（如与 τ 的 σ/θ 交换）选出唯一一个？
3. **carousel 与 fringing**：fringing 使 $\Delta$ 变 3 倍——是否对应 `H` 的某个谱量？

---

## 7. 参考

- AEG：`paper-5/sections/04-six-state-carrier.tex`（`Ω=TSR`、`prop:one-complex-unit`、三平面、`prop:sign-law`）。
- Adva：`knowledge/received/iota-frame-knowledge-2026-09-17-v1/materials/{frame.md,algebra.py}`（`H=diag(H0,H0)`、`A=-JH`）；`docs/research/0010-causal-cut-chirality-cube.md`。
- carousel：Pushkarev–Byzov 2014 Thm 4.3 / Cor 4.4。
- 计算：`research/donaghey-orbits/verify_carousel.py`；本笔记 §1 的 6×6 矩阵检查（`Ω²=-I`、`Ω⁴=I`）。
- 相关：note 31、OQ-098.3。
