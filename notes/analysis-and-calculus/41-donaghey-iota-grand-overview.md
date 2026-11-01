# Donaghey ↔ AEG ↔ iota：总地图

## note 26–40 的大收束（两篇总览 note 30 与 note 40 之上）

### Research Note v0.1 · 2026-11-01

**一句话**：note 26–40 是**一个对象（Donaghey 变换 `τ`）的两条正交线索**——
- **树层线（26–30）**：`τ` 把"一般树 ↔ 二叉树"（`R/L`=左右梳，`σ/θ/φ`=镜像/反演/词编码），其轨道/双曲/下降性质；
- **carousel–iota 线（31–40）**：`τ` 的 **carousel 效应**（Thm 4.3）拆成 **旋转半**（↔ iota 复单位 `J`）与 **shift 半**（↔ 角序后继 `S`）。
两条线被**同一个障碍**串起——**平面（左/右）信息不可丢**（note 29 与 note 32 是同一障碍的两次现身）；并有一个**已证的定论**——shift 半的唯一典范化（note 39）。

**入口**：本笔记（大收束）→ `30`（树层总览）→ `40`（carousel–iota 总览）→ 各详细笔记。

---

## 0. 材料与两篇总览

| 材料 | 内容 |
|---|---|
| Donaghey 1980 | 四族 Catalan、R/L 双射、$M_P$/$M_Z$、primitive/Motzkin |
| Pushkarev–Byzov 2014 | 三定义（右分解/双射/`φ⁻¹θφσ`）、carousel、fringing、轨道、`Z₂*Z₂` |
| OEIS A014486 图表 | Catalan 结构罗塞塔 |
| AEG Paper 5 | 六态载体、`Ω=TSR`、`Ω²=-1`、手性符号律 |
| Adva | `0010` 手性载体、iota frame（`J`,`H`,`A=-JH`）、iota 组合子、`0168` |

- `30` = 26–29 综合（树层）；`40` = 31–39 综合（carousel–iota）。**本笔记 = 二者之上。**

---

## 1. 一个变换：Donaghey `τ`

**四族**（皆 $c_n$）：g.b.、b.b.、p.t.、t.p.t.(=PPCT)；外加 z.t.、+.b.b.。自然对应：`+.b.b.↔z.t.`、`(g.b.)↔p.t.`（up-down code = Dyck 词）。

**R/L 双射**：`g.b.→+.b.b.`，R=右梳、L=左梳；树级 PPCT↔PPT（顶点↔右/左路径）。

**三定义**（Thm 2.1）：归纳式（右分解→左分解）；`T→T^R→T'`；`τ=φ⁻¹θφσ`（σ=transposition、θ=reflection、φ=PPCT↔Dyck）。

**轨道**：carousel（Thm 4.3）；fringing（$\Delta(Q(T))=3\Delta(T)$ 或 $\tfrac32$）；轨道增长 $O(n^{\log_23})$；Thm 6.4 `⟨σ,θ⟩≅Z₂*Z₂`。

---

## 2. 与 AEG 树层的精确对应（note 30 §2）

| Donaghey/PB | AEG | 状态 |
|---|---|---|
| **σ**（左右子互换）| 镜像 $m$（`def:mirror-temporal-reversal`）| 精确 |
| **θ**（Dyck 反向）| 时间反演 $r$ | 精确（路径级）|
| **φ**（PPCT↔Dyck）| up-down 词编码 | 精确 |
| **R/L 双射** | 左/右梳 `conv:p0-left-right-convention` | 精确 |
| **四族** | 二叉树（顺序）vs 一般树（分支）| 精确 |
| **τ=φ⁻¹θφσ** | Donaghey 变换 | 结构对应（≠$mr$）|

**群结构**（note 30 §3）：AEG 的 $m,r$ 交换 → `Z₂×Z₂`（Klein）；Donaghey 的 $σ,\tilde θ$ 不交换 → `Z₂*Z₂`（无限二面体）。

**下降障碍**（note 29）：`τ` **不保持依赖偏序同构类**（$n=4$ 见证；$n\ge5$ 全骨架类多值）→ **`τ` 不下降到 $O(P)$**；双曲性严格是平面树层现象。

**格归属**（note 28）：论文"分配格"= **无限三叉树的 Birkhoff 下集格**，非 Tamari（$T_4$ 非分配）；AEG `O(P)` 是同构造、不同偏序。

---

## 3. 两条正交的"半"：旋转 vs shift

carousel（Thm 4.3）是 `τ` 的一个**具体效应**，可拆成两半：

| 半 | 内容 | iota 侧 |
|---|---|---|
| **旋转半** | 类级 4-循环 `LL→RL→RN→LN→LL`；`σ`（换左右）、`θ`（路径反向） | 复单位 `J`（六态载体 `Ω=TSR`，`Ω²=-1`，`J` 在每平面 4-循环）|
| **shift 半** | index `k` 递增（$LL(k)\to\cdots\to LN(k)\to LL(k+1)$）；`SR` 入口 | 角序后继 `S` |

**旋转半的对齐**（note 32）：**非典范**——类 4-循环可对到 `J` 在**单平面 4 带号态**上的 4-循环（3 平面 × 2 定向 = 6 候选），但 `J` **保平面、把正态送带号态**，**解不了 `SR→LL` 入口与 index**。

**shift 半的导出**（note 35–39）：`S` = **角序（preorder）后继**；分支层 = **左优先 postorder**；唯一典范化 = **与角序最少逆序**（note 39 **已证一般 $n$**）。

---

## 4. 同一个障碍：平面信息不可丢

这是把两篇总览串起来的**主线**：

- **note 29**：`τ` 不下降到 $O(P)$——因为 `τ` 用左/右（平面）信息，而 $O(P)$（依赖偏序的下集格）**忘记**左/右。$n=4$ 见证：同属链类的两树，`τ` 后一留串行、一变分支。
- **note 32**：carousel = `J` 强形式证伪——因为 `J` **保平面**（三平面各自不变），不能做 `SR→LL` 的**跨平面**入口。
- **note 33**：`H` 不能承载 index `k`——`H` 来自割图（unplanar），而 `k=#左叶` 是 planar；同谱不同 `k` 见证。

> **同一个"平面（左/右）不可丢"的障碍，在 $\tau$、在 $J$、在 $H$ 上三次现身。** 这不是三个巧合，而是**一个结构性事实**：AEG 的"树层"是 planar 的，"偏序/割图/谱"层是 unplanar 的，二者不能互相完全承载。

---

## 5. 载体：从六态/i ota frame 到 planar 螺旋模

- **AEG 六态载体 = Adva iota frame**（note 31）：`W=Λ¹E⊕Λ²E=(T⊕SR)⊕(S⊕RT)⊕(R⊕TS)`，`J²=-I`，三平面逐项一致——**同一个对象**。
- **iota frame 是螺旋**（note 33）：`A=-JH`，`exp(tA)=cos(tH)-J sin(tH)`（转角∝H 特征值）。
- **planar 螺旋模**（note 34）：
$$
V=V_{\mathrm{class}}\otimes V_{\mathrm{index}},\quad V_{\mathrm{class}}=\langle LL,RL,RN,LN\rangle,\quad V_{\mathrm{index}}=\langle e_k\rangle,
$$
$$
J:(c,k)\mapsto(c+1,k),\quad S:(c,k)\mapsto(c,k+1),\quad C:(c,k)\mapsto(c+1\bmod4,k+[c=LN]).
$$
**已验**：`C⁴=S`、`J⁴=id`、`[J,S]=0`、count 影子 `M²=id`。

**结论**：**`V` 是 carousel 的最小 planar 载体**；iota 供 `J`（旋转半），`S`（shift 半）由角序给。

---

## 6. 大收束：一张地图

| # | 问题 | 结论 | 类型 | 笔记 |
|---|---|---|---|---|
| 1 | 一般树↔二叉树 | R/L=左右梳；σ/θ/φ=镜像/反演/词编码 | 精确对应 | 26/30 |
| 2 | `τ` 的群 | `⟨σ,θ⟩≅Z₂*Z₂`；AEG `⟨m,r⟩≅Z₂×Z₂` | 经典+对应 | 30 |
| 3 | comb 层 | AEG 操作给 Klein，非 `Z₂*Z₂` | 解决（note 27）| 27 |
| 4 | 依赖偏序下降 | `τ` 不保持偏序同构类 → 不下降 | 解决（负面）| 29 |
| 5 | 格归属 | = Birkhoff 下集格，非 Tamari | 解决 | 28 |
| 6 | carousel ↔ iota 三义 | 收缩 / frame / 组合子 | 辨析 | 31 |
| 7 | 旋转半 = `J`？ | 强形式证伪；非典范对齐；平面障碍 | 精确障碍 | 32 |
| 8 | iota frame | 螺旋；`H` 不承载 index | 计算 | 33 |
| 9 | planar 载体 | 螺旋模 `C⁴=S` | 计算 | 34 |
| 10 | `S` 的导出 | 角序后继；分支层=左优先 postorder | 对应 | 35/36/37 |
| 11 | 跨链典范化 | 唯一最少逆序 = 左优先 postorder | **PROVED（任意 $n$）** | 38/39 |
| 12 | 总览 | 树层 / carousel–iota | 收束 | 30/40 |

---

## 7. 地位总表（跨两篇）

| 命题 | 地位 |
|---|---|
| Donaghey/PB 的变换、轨道、`Z₂*Z₂`、fringing | `CLASSICAL` |
| AEG ↔ Donaghey 的 `[对应]`（σ/θ/φ、R/L、四族）| `[对应]` 精确 |
| comb 层 Klein（098.1）| `CLASSICAL` + 计算 |
| `τ` 不下降（098.1b）| `COMPUTATIONALLY VERIFIED EXAMPLE`（$n\le8$）|
| 格 = Birkhoff 下集格（098.2）| `CLASSICAL` + 计算 |
| AEG 六态 = Adva iota frame | `CLASSICAL` + `[对应]` |
| `carousel = J` 证伪 / 非典范对齐 | `[对应]` 精确 |
| 螺旋模 `C⁴=S` | `COMPUTATIONALLY VERIFIED EXAMPLE` |
| 角序 ↔ 求值序 对齐 | `CLASSICAL`（OCR Remark）+ 计算 |
| 典范化（唯一最少逆序）| **`PROVED`（note 39，任意 $n$）** |

---

## 8. 开放问题（统一）

| 编号 | 问题 | 状态 |
|---|---|---|
| 098.1(a) | `θ̃` 的 AEG 内在定义；与 `m` 生成 `Z₂*Z₂`？ | open |
| 098.1(b) 残余 | 一般 $n$ 的下降障碍证明；分支层**自身**（非 τ）的双曲结构 | open |
| 098.2 残余 | `O(P)` 嵌入 $T_∞$ 子偏序的下集格；原文"standard lattice ordering"出处 | open |
| 098.3 | fringing（$\Delta$ 三倍）、$O(n^{\log_23})$ 轨道 ↔ Hecke 周期轨道 / "fractal rotation" | open |
| 098.4 | 右/左双射的函子性（尊重序缺陷） | open |
| 新 | 平面障碍的"必然性"：能否证明**不存在** unplanar 载体承载 carousel？（即 note 4 的"一个结构性事实"的严格版）| open |
| 新 | 典范化的 $\sigma$-等变性；其他内蕴准则同解性 | open |

---

## 9. 参考

- Donaghey 1980；Pushkarev–Byzov 2014；OEIS A014486。
- AEG：`paper-5/sections/04-six-state-carrier.tex`；`paper-1/sections/02-sequential-histories.tex`；`paper-0/sections/03-aes-and-motion.tex`。
- Adva：`docs/research/0010-causal-cut-chirality-cube.md`、`knowledge/received/iota-frame-knowledge-2026-09-17-v1/materials/{frame.md,algebra.py}`、`docs/research/0168-...`、`murphy-iota-v0/`。
- 详细笔记：`26`–`40`（两篇总览 `30`/`40`）；计算：`research/donaghey-orbits/`、`research/ppct-lattice/`、`research/iota-carousel/`。
