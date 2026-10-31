# 镜像 + 反演在树层：AEG 的 `Z₂×Z₂`（Klein）与 Donaghey 的 `Z₂*Z₂`（无限二面体）

## OQ-098.1 推进：非交换扩展不在 comb 层，而在分支层

### Research Note v0.1

**2026-10-31**（v0.1：推进 OQ-098.1。结论：(1) **AEG 的镜像 `m` 与反演 `r` 在词层交换**（§2.9 已证），生成 `Z₂×Z₂`（Klein）；(2) **词↔comb 双射保交换**，故 **AEG 的 marked-history（单脊 comb）层就是 Klein，不会自动出现 `Z₂*Z₂`**；(3) **Donaghey 的 `σ` 重合 AEG 的 `m`，但 `θ̃=φ⁻¹θφ`（Dyck 路径反向）不是 AEG 的 `r`（词反向）**；(4) **`Z₂*Z₂`/无限阶依赖分支**（Cor 6.3 的长轨道构造在完全树+fringing 上，是分支的），故它属于 **依赖偏序/线性扩张的分支层**，不属于 comb 层。核心定论：**098.1 在 comb 层是否定回答；真正的问题转移到分支层**）

---

## 0. 问题精确化

**问题**（OQ-098.1）：AEG 的镜像+反演搬到**树层**后，是否生成 `Z₂*Z₂`（无限二面体）而非词层的 `Z₂×Z₂`（Klein）？

**三个必须区分的东西**：

| 操作 | 定义 | 对象 | 已证群 |
|---|---|---|---|
| **AEG 镜像 `m`** | $m(C_{\omega,c}^{(\varepsilon)})=C_{\omega,c}^{(3-\varepsilon)}$（逐元素换槽）| marked history（词）| 与 `r` 交换 |
| **AEG 反演 `r`** | $r\gamma=(g_n,\dots,g_1)$（逆序）| marked history（词）| 与 `m` 交换 |
| **Donaghey `σ`** | 每个内部点左右儿子互换（树镜像）| PPCT（一般二叉树）| 与 `θ` 生成 `Z₂*Z₂` |
| **Donaghey `θ`** | Dyck 路径反向（`reflection`）| 正 Dyck 路径 | 与 `σ` 生成 `Z₂*Z₂` |

**要点**：`σ` 与 `m` 是**同一个**（都是"每点换左/右"）。分歧只在反演：AEG 的 `r`（词反向）vs Donaghey 的 `θ̃:=φ⁻¹θφ`（Dyck 路径反向落到树上）。

---

## 1. `[AEG]` 词层：`m`、`r` 交换 → Klein（含具体 comb 验算）

**命题（已证，`def:mirror-temporal-reversal`）**：$m,r$ 都是对合，且 $m(r\gamma)=r(m\gamma)$。故 $\langle m,r\rangle\cong\mathbb Z_2\times\mathbb Z_2$（Klein），$mr$ 阶为 2。

**为什么交换**：`m` 作用在**槽标号**（逐元素），`r` 作用在**位置**（序列）——两个正交坐标，故交换。

**具体 comb 验算**（$n=2$，上下文 $g_1=(+,a,\varepsilon_1)$、$g_2=(\times,b,\varepsilon_2)$，逐个 slot）：

| $\varepsilon$ | 树 $T$ | $m r(T)$ | $r m(T)$ | 交换 |
|---|---|---|---|---|
| (1,1) | $*(\!+(x_0,a),b)$ | $+(a,*(b,x_0))$ | $+(a,*(b,x_0))$ | ✓ |
| (1,2) | $*(b,\!+(x_0,a))$ | $+(a,*(x_0,b))$ | $+(a,*(x_0,b))$ | ✓ |
| (2,1) | $*(\!+(a,x_0),b)$ | $+(*(b,x_0),a)$ | $+(*(b,x_0),a)$ | ✓ |
| (2,2) | $*(b,\!(a,x_0))$ | $+(*(x_0,b),a)$ | $+(*(x_0,b),a)$ | ✓ |

`[AEG]`（`CLASSICAL`，词层自证；comb 部分是计算见证）。

---

## 2. `[AEG]` 词↔comb 双射保交换 → comb 层就是 Klein

**`prop:marked-tree-history-correspondence`** 给出 **bounded marked spinal history ↔ marked planar sequential tree** 的双射；sequential tree = 单脊 = comb（caterpillar）。

**命题**：若 $m,r$ 在词上交换，则沿任何集合双射 $\varphi$ 搬运后的 $\varphi m\varphi^{-1}$、$\varphi r\varphi^{-1}$ 仍交换：
$$
(\varphi m\varphi^{-1})(\varphi r\varphi^{-1})=\varphi(mr)\varphi^{-1}=\varphi(rm)\varphi^{-1}=(\varphi r\varphi^{-1})(\varphi m\varphi^{-1}).
$$

**结论**：**AEG 的 marked-history（comb）层在搬运后仍是 `Z₂×Z₂`（Klein）。** 非交换的 `Z₂*Z₂` 不会仅仅因为"搬到树层"而出现。`[AEG]`（`CLASSICAL` 双射 + 群论恒等式）。

---

## 3. `[Donaghey]` `σ` = `m`，而 `θ̃` ≠ `r`

- **`σ = m`**：Donaghey 的 transposition（"sends all left sons to right ones and vice versa"）就是 AEG 的树镜像；两者逐点换左/右，故相等。`[对应]`（精确一致）。
- **`θ̃ ≠ r`**：`r` 是**词反向**（序列 $g_1,\dots,g_n\mapsto g_n,\dots,g_1$，每个上下文保留自己的槽和常数）；`θ` 是**Dyck 路径反向**，经 `φ` 落到树上得 `θ̃`，是一次**全局树重排**，不是简单序列反转。Pushkarev–Byzov 自己说（§3）："in terms of plane trees, Donaghey's transformation looks rather complicated"——正是 `θ̃` 不是简单词操作的旁证。

**推论**：$\tau=\varphi^{-1}\theta\varphi\sigma=\tilde\theta\,\sigma$ **不等于** AEG 的 $r\sigma=rm$。所以 Donaghey 变换不是 AEG 词层复合的搬运。`[对应]`（`structural proposal`；"σ=m"精确，"θ̃≠r"由定义差异支撑）。

---

## 4. `[Donaghey]` `Z₂*Z₂`/无限阶依赖**分支**，不属于 comb 层

- **Theorem 6.4**（Pushkarev–Byzov）：$\langle\sigma,\tilde\theta\rangle\cong\mathbb Z_2*\mathbb Z_2$；$\tau$ 无限阶（Cor 6.3：存在任意长轨道）。
- **关键观察**：Cor 6.3 的长轨道构造是"**完全 $n$ 层树**"的**迭代 fringing**（$Q(T)$）。fringing 给每个叶加左右二子——把 **comb 的叶**变成带子的内部点，**产生分支**。故长轨道 / `Z₂*Z₂` 只出现在**分支树**上，而 **comb（单脊）上 $\tau$ 是温顺的**（阶有界）。
- 也就是说：**Donaghey 的"双曲性"是分支层的现象**，对应 AEG 的**分支层**（依赖偏序 $P$、线性扩张、$\mathcal O(P)$），**不是** marked-history（comb）层。

`[Donaghey]`（`CLASSICAL`，Theorem 6.4 / Cor 6.3；"comb 层温顺"是从 fringing 构造推出的观察，**需独立验证**，见 §6 残余）。

---

## 5. 结论与问题转移

**098.1 的定论（comb 层）**：

> AEG 现有的镜像 `m` 与反演 `r`，**无论放在词层还是 comb 层，都生成 `Z₂×Z₂`（Klein），不会出现 `Z₂*Z₂`**。Donaghey 的 `Z₂*Z₂` 需要**另一个**反演 `θ̃`（Dyck 路径反向），它**不是** AEG 的 `r`；而 `τ` 的无限阶行为是**分支树**的现象，属于分支层。

**问题转移**（这才是真正开放的）：

1. **`θ̃` 是否有 AEG 的内在意义？** 若 AEG 能定义一个与 `r` 不同的"路径反射"（例如在 comb 的 up-down 码上反向），它与 `m` 是否生成 `Z₂*Z₂`？这需要先给 `θ̃` 一个不依赖 Donaghey 的 AEG 定义。
2. **AEG 的分支层（$\mathcal O(P)$、线性扩张）是否复现 `τ` 的无限阶/双曲行为？** 若把 Donaghey 的 `τ` 提升到"依赖偏序 → 其线性扩张"的层面，是否得到对应的无限二面体结构？这是"分支层的非交换扩展"。

`[对应]`（`structural proposal`；核心定论在 comb 层是精确的，问题转移是 open）。

---

## 6. 地位总表与残余

| 命题 | 地位 |
|---|---|
| §1 `m,r` 交换、Klein | `CLASSICAL`（`def:mirror-temporal-reversal`）+ 计算见证 |
| §2 双射保交换、comb 层 Klein | `CLASSICAL` 双射 + 群论恒等式 |
| §3 `σ=m` | `[对应]` 精确 |
| §3 `θ̃≠r` | `[对应]` `structural proposal` |
| §4 `Z₂*Z₂`/无限阶在分支 | `CLASSICAL`（Thm 6.4/Cor 6.3）；"comb 温顺"待证 |
| §5 098.1 comb 层否定 | `[对应]`（精确） |

**残余（`open`）**：

1. **comb 上 `τ` 的确切阶**（§4 的"温顺"断言）：需实现 Definition 2.1/2.2（右分解→左分解）并在 $n\le 4$ 的 PPCT 上验证轨道长与 Donaghey 的 $M_n(x)$ 一致；再单独看 comb 子集的阶是否 ≤2。
2. **`θ̃` 的 AEG 内在定义**（§5.1）：能否不借助 Donaghey，在 comb 的 up-down 码上定义"路径反射"，并证明它与 `m` 生成 `Z₂*Z₂`？
3. **分支层的提升**（§5.2）：Donaghey 的 `τ` 在"依赖偏序 → 线性扩张"层面是否有对应？这会把 §5.2 与 OQ-098.2（$\mathcal O(P)$ 格）连起来。

---

## 7. 参考

- AEG：`paper-1/sections/02-sequential-histories.tex`（`def:mirror-temporal-reversal`、`def:path-inverse`、`prop:marked-tree-history-correspondence`、`thm:sequential-tree-classification`、`thm:birkhoff-downset-spinal`）。
- Donaghey 1980；Pushkarev–Byzov 2014（`temp/` 下两份 PDF，见 note 26）；OEIS A014486 图表。
- 相关：note 26（`26-donaghey-general-to-binary-tree.md`）、OQ-098。
