# θ̃ 的内在定义：θ̃ = τ∘m，对合，且 ⟨m, θ̃⟩ = ⟨m, τ⟩ ≅ Z₂*Z₂

## OQ-098.1(a) 推进：路径反射的内在 AEG 定义

### Research Note v0.1 · 2026-11-01

**结论**：OQ-098.1(a) 的答案是**肯定的**，且定义极简：

> 由 Donaghey/Pushkarev–Byzov 的第三定义 `τ = φ⁻¹θφσ`，而 `σ = m`（transposition = AEG 镜像，note 32），故
> $$
> \boxed{\tilde\theta \;:=\; \varphi^{-1}\theta\varphi \;=\; \tau\circ m .}
> $$
> 即 **θ̃ = "先施加镜像 m，再施加 Donaghey 变换 τ"**——**不借 Dyck 路径 φ** 的内在 AEG 定义。

**代数事实**（全部已算验证 $n\le6$）：
$$
\tilde\theta^2=\mathrm{id},\qquad m\circ\tilde\theta=\tau^{-1},\qquad
\langle m,\tilde\theta\rangle=\langle m,\tau\rangle\cong \mathbb Z_2*\mathbb Z_2 .
$$
所以 **θ̃ 是"路径反射"的内在 AEG 定义，且与 `m` 生成 `Z₂*Z₂`（无限二面体）**——这正是 note 27/30 里"词层 Klein vs 树层无限二面体"的**树层**结构。

---

## 0. 目标

OQ-098.1(a)：是否存在与 `r`（词反向）**不同**的"路径反射" `θ̃` 的**内在 AEG 定义**，且它与镜像 `m` 生成 `Z₂*Z₂`？

---

## 1. 代数推导：`θ̃ = τ∘m`

Pushkarev–Byzov Thm 2.1（第三定义）：
$$
\tau \;=\; \varphi^{-1}\circ\theta\circ\varphi\circ\sigma,
$$
其中 `σ` = transposition（左右子互换），`θ` = Dyck 路径 reflection，`φ` = PPCT ↔ Dyck。

note 32 已确认 **`σ = m`**（AEG 的镜像，`def:mirror-temporal-reversal`）。于是
$$
\tau = \tilde\theta\circ m,\qquad\text{即}\qquad \tilde\theta = \tau\circ m
$$
（用 $m^2=\mathrm{id}$）。**这是 `θ̃` 的内在定义**：`τ` 与 `m` 都是 AEG 内在的（`m` 是镜像，`τ` 是"一般树↔二叉树"变换），**不需要 Dyck 路径 φ**。

---

## 2. 代数事实

- **对合**：$\tilde\theta^2=(\tau m)(\tau m)=\tau m\tau m$。代入 $\tau=\tilde\theta m$：$=(\tilde\theta m)m(\tilde\theta m)m=\tilde\theta^2=\mathrm{id}$。∎
- **`m∘θ̃ = τ⁻¹`**：$m\tilde\theta=m(\tau m)=m\tau m$；而 $\tau=\tilde\theta m$ 取逆（两者都是对合）得 $\tau^{-1}=m\tilde\theta$。故 $m\tilde\theta=\tau^{-1}$。∎
- **群**：由 `m∘θ̃ = τ⁻¹`，$\langle m,\tilde\theta\rangle=\langle m,\tau\rangle$；由 Donaghey **Thm 6.4**，$\langle\sigma,\tilde\theta\rangle\cong\mathbb Z_2*\mathbb Z_2$，而 $\sigma=m$，故 $\langle m,\tilde\theta\rangle\cong\mathbb Z_2*\mathbb Z_2$。

---

## 3. 计算验证（`research/iota-carousel/verify_theta.py`）

对 $n\le6$ 的**全部** PPCT（$1+2+5+14+42+132=\dots$ 棵，含 $n=2..6$）：

| 检查 | 结果 |
|---|---|
| `θ̃² = id` | **全部成立** |
| `m∘θ̃ = τ⁻¹`（即 `m(θ̃(τ(T)))=T`）| **全部成立** |
| `θ̃` 轨道长 ∈ {1,2}（对合）| $n=3$: [1,1]；$n=4$: [1,1,1,2]；$n=5$: [1,1,1,1,1,1,2,2,2,2] |
| `τ` 与 `m∘θ̃` 的轨道长一致 | $n=4,5$：一致 |

---

## 4. 与 note 27/30 的衔接

note 27 的结论是：
- **词层**：`m, r` 交换 → `Z₂×Z₂`（Klein）；
- **树层**：`σ, θ̃` 不交换 → `Z₂*Z₂`（无限二面体）。

**本笔记给出 `θ̃` 的内在定义**（`θ̃ = τ∘m`），从而**"树层 `Z₂*Z₂`" 不再是外部构造**——`θ̃` 就在 AEG 的树操作里（`τ` 与 `m` 的复合）。所以：

> **AEG 的树层确实有 `Z₂*Z₂` 结构**（`⟨m, θ̃⟩`），而词层只有 Klein（`⟨m, r⟩`）。两层的差别由"`θ̃ ≠ r`"体现：`θ̃ = τ m` 用树结构，`r` 只用词序。

---

## 5. 关于"`θ̃ ≠ r`"

- `r`（词反向）是**纯词序**操作；
- `θ̃ = τ m` 用**树结构**（`τ` 是树变换）。
- 故 **`θ̃` 一般不等于 `r`**（note 27 已指出：词反向 ≠ 路径反向诱导的树重排）。
- 本笔记的贡献是：**`θ̃` 有了内在定义（`τ m`），不必再借 `φ`**；且它确实是"与 `m` 生成 `Z₂*Z₂` 的那个反演"。

---

## 6. 地位与残余

| 命题 | 地位 |
|---|---|
| §1 `θ̃ = τ∘m`（内在定义）| `[对应]` 精确（由 `τ=φ⁻¹θφσ`、`σ=m`）|
| §2 `θ̃²=id`、`m∘θ̃=τ⁻¹` | **`PROVED`**（代数恒等式）|
| §2 `⟨m,θ̃⟩=⟨m,τ⟩≅Z₂*Z₂` | `CLASSICAL`（Donaghey Thm 6.4）+ 本定义 |
| §3 计算验证（$n\le6$）| `COMPUTATIONALLY VERIFIED EXAMPLE` |

**残余（`open`）**：
1. **词层公式**：`θ̃ = τ m` 在**词（marked history）**上的直接公式（不经树）——对 comb 子族可能可写，但 `τ` 不保 comb（note 27），故一般无简单词公式。
2. **`θ̃` 的"自然性"**：`θ̃ = τ m` 依赖"τ 与 m"的定义；是否存在**更等价、更自然**的定义（如"轮廓反射"的直接树操作）？
3. **与 `r` 的精确关系**：何时 `θ̃(T) = r(T)`？（应对应"词反向恰等于路径反向"的特殊子族。）
4. **`Z₂*Z₂` 的几何实现**：`⟨m, θ̃⟩` 作为树上的群，其"轨道/基本域"能否与 note 34 的 planar 螺旋模 / Hecke 的 `C₂*C₄` 对接？

---

## 7. 参考

- Donaghey 1980；Pushkarev–Byzov 2014（Thm 2.1、Thm 6.4）。
- AEG：`paper-1/sections/02-sequential-histories.tex`（`def:mirror-temporal-reversal`、`def:path-inverse`）。
- 计算：`research/iota-carousel/verify_theta.py`。
- 相关：note 27（Klein vs 无限二面体）、note 30（树层总览）、note 32（σ=m）、note 41（大收束）；OQ-098.1(a)。
