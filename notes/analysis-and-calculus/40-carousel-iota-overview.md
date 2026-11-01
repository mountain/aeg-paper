# carousel ↔ iota：总览

## note 31–39 综合（从猜想到 planar 螺旋模 + 已证的典范化）

### Research Note v0.1 · 2026-11-01

**一句话结论**：用户猜想"carousel 与 iota 有关"——**方向成立**，且可拆成两半：
1. **旋转半**：carousel 的类级 4-循环与 iota 的**复单位 `J`**（`Ω=TSR`，`Ω²=-1`）同构于 `C₄`，但只在**非典范**意义下对齐（`J` 保平面、把正态送带号态，故不解 "SR→LL 入口 + index"）；
2. **shift 半**：`S` 是"**角序（preorder）后继**"，其"分支层"实现是**左优先 postorder**，且由"**与角序最少逆序**"**唯一典范化**（已给**一般 $n$ 归纳证明**）。

承载二者的是**planar 螺旋模** `V = V_class ⊗ V_index`，满足 `C⁴ = S`（carousel = 射影 `Z/4` = `S` 的四次根）。

**详细笔记**（本总览只综述；证明/见证在各篇）：
`31-carousel-and-iota.md`（三义辨析）· `32-carousel-iota-alignment.md`（对齐/证伪）·
`33-shift-research.md`（螺旋 + `H` 失败）· `34-planar-carrier.md`（载荷构造）·
`35-derive-shift.md`/`36-branching-layer-shift.md`（`S` 的导出）·
`37-corner-order-alignment.md`（角序对齐）· `38-canonical-cross-chain-choice.md`/`39-canonical-choice-general-proof.md`（典范化 + 证明）。
计算：`research/iota-carousel/`（`verify_omega/planar/shift/traversal/branching_shift/corner_order/canonical_choice.py`）。

---

## 0. 材料与路线图

- **AEG 侧**：`paper-5/sections/04-six-state-carrier.tex`（六态载体、`Ω=TSR`、手性符号律）。
- **Adva 侧**（`~/work/public/adva`）：`docs/research/0010-causal-cut-chirality-cube.md`、`knowledge/received/iota-frame-knowledge-2026-09-17-v1/materials/{frame.md,algebra.py}`、`docs/research/0168-...`、`murphy-iota-v0/`。
- **carousel**：Pushkarev–Byzov 2014 §4（Thm 4.1/4.2/4.3、Cor 4.4、Remark）——原由 OCR 读取。

---

## 1. 三个 iota（必须分开）

| | iota 是什么 | 关键 |
|---|---|---|
| **(A) AEG ι** | 六态载体的**切收缩/内积**：`c_i=ε_i+ι_i`，`Ω=TSR`，`Ω²=-1` | **手性符号律**：偶（循环）置换保持 Ω、奇（对换）反号 |
| **(B) Adva iota frame** | 割坐标上的**复结构** `J=[[0,-I],[I,0]]`，`J²=-I`；"e=指数、i=J" | 由割图 Laplacian 装出 |
| **(C) Adva iota 组合子** | SKI 单组合子基底 `ιx=xSK` | adva `0168` 已**否定**它承载辫子/swap（收敛 vs 发散）|

**关键发现**：**AEG 的六态载体与 Adva `0010` 的手性载体是同一个 6 维空间**（`W=Λ¹E⊕Λ²E=(T⊕SR)⊕(S⊕RT)⊕(R⊕TS)`，`J²=-I`，三个"面-对极面"平面逐项一致）。**即 AEG iota = Adva iota frame**——"iota"这一侧**足够丰富**。

---

## 2. carousel 的精确内容

- **类级核心**：`LL→RL→RN→LN→LL`（4-循环）；`SR` 为基点；`LL(k)→…→LN(k)→LL(k+1)`。
- **计数影子**（Cor 4.4）：`(k,l,m,n)→(n+1,k,l-1,m)`，约束 `k=m+1, l=n+1`；在约束面上是**对合（阶 2）**（note 31 计算）。
- **角序**：Thm 4.2——left natural traversal = 左标准遍历 = **preorder**（note 37 OCR）。

---

## 3. 对齐：强形式证伪、弱形式非典范（note 32）

- **强形式"carousel = J 在六态上"证伪**：`J` 把正态送带号态（`SR↦-T`），保三平面；carousel 是 5 类 + 4-循环。
- **类 4-循环 ↔ 单平面 4 带号态**：**可对齐但非典范**（3 平面 × 2 定向 = 6 候选）。
- **精确障碍**：`SR→LL` 入口与 index 平移在 `J` 中**无对应**（`J` 保平面、无跨平面/tail）。故 `carousel = (J-型旋转) + (shift)`。

---

## 4. iota frame 是"螺旋"，`H` 不承载 shift（note 33）

- 已验：`[J,H]=0`、`J²=-I`、`A=-JH`、`A²=-H²`、`exp(tA)=cos(tH)-J sin(tH)`（**旋转角 ∝ H 特征值**）——即"螺旋"。
- **`H` 不能承载 index `k`**：`H` 来自割图（= 依赖偏序 `O(P)` 的下集格，**忘记左/右**），而 `k=#左叶` 是**平面**量；$n=4$ 的四棵树同谱 `(0,.1464,.5,.8536)` 却 `k=3,2,1`。

---

## 5. planar 螺旋模（note 34）

$$
V=V_{\mathrm{class}}\otimes V_{\mathrm{index}},\quad
V_{\mathrm{class}}=\langle LL,RL,RN,LN\rangle\ (\text{planar}),\quad
V_{\mathrm{index}}=\langle e_k:k\ge1\rangle\ (\text{unbounded}),
$$
$$
J:(c,k)\mapsto(c+1,k),\quad S:(c,k)\mapsto(c,k+1),\quad C:(c,k)\mapsto(c+1\bmod4,\ k+[c=LN]).
$$
**已验**：`C⁴=S`（carousel = 射影 `Z/4` = `S` 的四次根）、`J⁴=id`、`[J,S]=0`、count 影子 `M²=id`（螺旋对计数不可见）。

---

## 6. shift 的导出：`S` = 角序后继（note 35–37）

- note 35 把 `S` 接为 AEG 的"时序后继"，但**用了 preorder**（note 36 修正）。
- note 37（OCR）确认：**corner = 顶点**（SR/LL/RL/LN/RN），**left standard traversal = preorder**。故 carousel 的 `k` 是 **preorder** 位置；求值序是 **postorder**。
- **对齐（原文 Remark + 计算）**：
$$
\text{求值序}=\begin{cases}\text{角序} & \text{叶（LL,RL）上},\\ \text{角序}^{-1} & \text{非叶链（LN,RN）内},\\ \text{选择} & \text{跨不可比链}.\end{cases}
$$
- 故 **`S`（carousel 的 `k` 的 shift）= 角序（preorder）后继**；note 36 的"左优先 postorder"是**求值序**，只在叶上与 `S` 一致、非叶上相反。

---

## 7. 典范化：唯一最少逆序 = 左优先 postorder（note 38–39）

**准则**（note 38）：典范线性扩张 = **与角序（preorder）逆序数（Kendall tau）最少**者。

**定理**（note 39，已证）：对**任意** PPCT，左优先 postorder `Q(t)` 是 `argmin_E inv(E,P(t))` 的**唯一**最小点。

**证明（归纳）**：$t=\mathrm{Node}(a,b)$，任何线性扩张 `E=M+[root]`（`M` 交错）；
$$
\mathrm{inv}(E,P(t))=(m-1)_{\text{根}}+\mathrm{inv}(E_a,P(a))+\mathrm{inv}(E_b,P(b))+\mathrm{cross}(M),
$$
根贡献常数；`cross(M)≥0` 且 `=0` **iff** `M=E_a+E_b`（块）；归纳给出 `Q(a)`、`Q(b)` 唯一。$\blacksquare$

**计算**：$n\le7$（193 棵树）全部一致。

**结论**：**"跨分支层选择"被唯一典范化**——`S` 不是任意的左优先，而是"与角序最贴合的、唯一的 canonical 求值序"。

---

## 8. 总地位表

| 命题 | 地位 |
|---|---|
| §1 三义 iota；AEG 六态 = Adva iota frame | `CLASSICAL`（Paper 5 / adva `0010`）+ `[对应]` |
| §2 carousel 公式、计数影子对合 | `CLASSICAL`（Thm 4.3/Cor 4.4）+ 计算 |
| §3 强形式 `carousel=J` 证伪、非典范对齐、plane-preserving 障碍 | `[对应]` 精确（note 32）|
| §4 螺旋结构；`H` 不承载 `k` | `CLASSICAL`/计算（note 33）|
| §5 planar 螺旋模 `C⁴=S` | `COMPUTATIONALLY VERIFIED EXAMPLE`（note 34）|
| §6 `S` = 角序后继；preorder/postorder 对齐 | `CLASSICAL`（OCR）+ 计算（note 37）|
| §7 典范化：唯一最少逆序 = 左优先 postorder（任意 $n$）| **`PROVED`（note 39）** |

---

## 9. 残余（`open`）

1. **`θ̃` 的内在 AEG 定义**（098.1a）：能否不借 Donaghey，在角序/词上定义"路径反射"，且与 `m` 生成 `Z₂*Z₂`？
2. **其他内蕴准则**：是否也给出同一唯一解（如"保留左→右子树叶序"）？多条准则同解则典范性更强。
3. **$\sigma$-等变性**：准则 $\sigma$-不变、解 $\sigma$-等变（左优先 ↔ 右优先）。
4. **与 note 29 的正式区分**：note 29 的障碍是"$\tau$ 不下降到 $O(P)$（多值）"；典范化是"**选一条**极大链"的准则——它把多值**单值化**，但 $\tau$ 本身仍不是 $O(P)$ 的映射（两件不同的事，需正式写清）。
5. **carousel 与 fringing / 轨道增长**（098.3 的另一半）：`Δ(Q(T))=3Δ(T)`、`O(n^{log₂3})` 与 Hecke 周期轨道的关系。
6. **098.4**：右/左双射的函子性。

---

## 10. 参考

- AEG：`paper-5/sections/04-six-state-carrier.tex`（`Ω=TSR`、三平面、手性符号律、`prop:sign-law`）。
- Adva：`docs/research/0010-causal-cut-chirality-cube.md`、`knowledge/received/iota-frame-knowledge-2026-09-17-v1/materials/{frame.md,algebra.py}`、`docs/research/0168-...`、`murphy-iota-v0/`。
- carousel：Pushkarev–Byzov 2014 §4。
- 计算：`research/iota-carousel/`（7 个脚本 + 证据 JSON）。
- 相关：note 26–30（Donaghey 总览）、note 31–39（本文综合）；OQ-098.3。
