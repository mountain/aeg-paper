# planar 载体构造：螺旋模，与 carousel = 螺旋

## 推进 note 33 的"planar 载体"：显式构造 + 三要求检验

### Research Note v0.1 · 2026-11-01

**结论**：构造出显式的 **planar 螺旋模**
$$
V \;=\; V_{\mathrm{class}}\otimes V_{\mathrm{index}},
\qquad
V_{\mathrm{class}}=\langle LL,RL,RN,LN\rangle,\quad
V_{\mathrm{index}}=\langle e_k:k\ge1\rangle ,
$$
它**同时满足三个要求**：**planar**（class 纤维编码左/右 × 叶/非叶）、**unbounded**（index 无界）、**Z/4 旋转**（`J`）。在其上：
- **纯旋转** `J`（阶 4）= iota 复单位；
- **shift** `S`（index 递增）= 高度；
- **carousel** `C` 是它们之上的**螺旋**：`C⁴ = S`（四次类旋转 = 一次 index 平移），`C` 是 `S` 的四次根，即一个**射影 Z/4**；
- **count 影子** `M`（Cor 4.4）是**对合**（`M²=id`）——**螺旋在计数层不可见**。

**iota 的关系**：`J` = 旋转半（iota 提供）；`S` = 高度半（iota **不**提供）。故 **planar 载体 = (iota 的 J) ⊗ (index 分级)**，carousel 是它的 "螺旋提升"。

---

## 0. 目标与三要求（note 33 结论）

要承载 carousel，载体须同时：
1. **planar**：区分左/右（叶/非叶）；
2. **unbounded**：index `k` 随树增大无界；
3. **Z/4 旋转**：`J`（复单位，`J²=-I`、`J⁴=I`）。

---

## 1. 障碍回顾

| 候选 | 失败点 |
|---|---|
| `H`（割图 Laplacian）| **unplanar**（割图来自依赖偏序，忘左/右）；同谱不同 `k`（note 33）|
| 六态载体 `W=Λ¹E⊕Λ²E` 的 `J` | **bounded**（6 态）；`J` 把正态送带号态（note 32）|
| marked history / 词 | planar + 无界，但**缺自然 Z/4**（待验证）|

---

## 2. 构造：螺旋模 `V = V_class ⊗ V_index`

**基向量** `e_{c,k}`，`c ∈ {LL,RL,RN,LN}`，`k ∈ ℤ_{≥1}`：

- **planar 纤维** `V_class`：四个角类按 **(左/右) × (叶/非叶)** 分组——
  `LL`(左叶)、`RL`(右叶)、`RN`(右非叶)、`LN`(左非叶)。这**正是**平面（左/右）信息。
- **index 分级** `V_index`：`k` = "第 k 个同类角"，**无界**。
- `SR` 是**基点**（不在 4-循环里；由 `C` 的入口/回绕处理）。

**算子**（在 `e_{c,k}` 上）：
$$
J:\ (c,k)\mapsto (c+1 \bmod 4,\ k),
\qquad
S:\ (c,k)\mapsto (c,\ k+1),
\qquad
C:\ (c,k)\mapsto (c+1 \bmod 4,\ k+\mathbf 1_{c=LN}).
$$

---

## 3. 验证（`research/iota-carousel/verify_planar.py`，全 `True`）

- **`C⁴ = S`**：四次类旋转 = 一次 index 平移（**螺旋**）；故 `C` 是 `S` 的**四次根**，是**射影 Z/4**。
- **`J⁴ = id`**：纯旋转阶 4。
- **`[J,S] = 0`**：旋转与平移交换（经典螺旋）。
- **`M² = id`**（count 影子，Cor 4.4）：**螺旋在计数层坍缩为对合**（`S ↦ id`）。

**轨道**（从 `(LL,1)` 起）：
$$
(LL,1)\to(RL,1)\to(RN,1)\to(LN,1)\to(LL,2)\to(RL,2)\to\cdots
$$
——干净的螺旋：类绕 4、每绕一圈 `k` 加一。

---

## 4. 三要求全部满足

| 要求 | `V` 上的实现 |
|---|---|
| planar | `V_class` 的四个标签 = (左/右, 叶/非叶) |
| unbounded | `V_index` 的 `k ∈ ℤ_{≥1}` |
| Z/4 | `J`（阶 4），`C` 是 `S` 的 4 次根（射影 Z/4）|

**所以"planar 载体"存在且显式**：它就是**螺旋模** `V = V_class ⊗ V_index`。

---

## 5. 与 iota 的关系（哪一半来自 iota）

- **`J` = iota 复单位**：六态载体的 `Ω/J`（`Ω²=-I`）给出 Z/4；在 `V` 上它作用于 `V_class`（纯旋转）。
- **`S` = 高度/平移**：**不在** `J`、`Ω`、`H` 里。它是"index 分级"。
- **carousel `C`** = 把 `J` **提升**为 `S` 的四次根（螺旋）——即 $C$ 是 $\mathrm{mod}\ S$ 意义下的 $J$。

**精确表述**：
$$
C \equiv J \pmod{S}\quad(\text{射影 Z/4}),\qquad C^4=S .
$$
iota 只给出**右侧（旋转半）**；**左侧（shift 半）是独立的"高度"结构**。

---

## 6. 地位与残余

| 命题 | 地位 |
|---|---|
| §2 螺旋模 `V` 的构造与三要求 | `[对应]` **构造**（显式、可验）|
| §3 `C⁴=S`、`J⁴=id`、`[J,S]=0`、`M²=id` | `COMPUTATIONALLY VERIFIED EXAMPLE` |
| §5 `J` = iota 复单位；`S` 独立 | `[对应]`（J 精确；S 独立是诚实标注）|
| §5 `C ≡ J (mod S)` 且 `C⁴=S` | `[对应]` 精确（射影 Z/4）|

**残余（`open`）**：
1. **`S` 的 AEG/Adva 来源**：`V_index` 是**构造**的（"最小/万有"），尚未**导出**自 AEG/Adva 的已有对象。候选：`H` 的分级维数（`n`）、事件时钟、外幂/张量幂。
2. **`SR` 与回绕**：螺旋模把 `SR` 当"基点"外置；严格的 corner 级（`SR→LL`、`last RL→SR`）需要把 `SR` 纳入（可能是 `V` 的"零点/截面"）。
3. **词/历史作为 planar 载体**：marked history 是 planar + 无界；其上的 **Z/4** 是否 = `J`（`θ` 的四分之一转？）值得单独验证。
4. **一般 `n` 与 `C⁴=S` 的严格证明**：本构造是"结构级"；把它与 Pushkarev–Byzov 的 **corner 级 Thm 4.3** 逐项对齐仍待做。

---

## 7. 参考

- AEG：`paper-5/sections/04-six-state-carrier.tex`（`Ω=TSR`、`J`）。
- Adva：`knowledge/received/iota-frame-knowledge-2026-09-17-v1/materials/{frame.md,algebra.py}`。
- carousel：Pushkarev–Byzov 2014 Thm 4.3 / Cor 4.4。
- 计算：`research/iota-carousel/verify_planar.py`（螺旋模）；`verify_shift.py`（螺旋 frame + 同谱不同 k）；`research/donaghey-orbits/verify_carousel.py`（count 影子）。
- 相关：note 29/31/32/33；OQ-098.3。
