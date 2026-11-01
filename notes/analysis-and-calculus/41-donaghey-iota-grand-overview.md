# Donaghey ↔ AEG ↔ iota：总地图

## note 26–46 的大收束（两篇总览 note 30 与 note 40 之上，纳入 42–46）

### Research Note v0.3 · 2026-11-01

**一句话**：note 26–46 是**一个对象（Donaghey 变换 `τ`）的两条正交线索**——
- **树层线（26–30、42–46）**：`τ` 把"一般树 ↔ 二叉树"（`R/L`=左右梳、`σ/θ/φ`=镜像/反演/词编码），及其轨道/双曲/下降/函子性/提升；
- **carousel–iota 线（31–40）**：`τ` 的 **carousel 效应**（Thm 4.3）拆成 **旋转半**（↔ iota 复单位 `J`）与 **shift 半**（↔ 角序后继 `S`）。

**两条主线**贯穿全部：
1. **一个障碍——平面（左/右）信息不可丢（五次现身）**：在 `τ` 下降（note 29）、`J`（note 32）、`H`（note 33）、`R/L` 双射的操作数（note 44）、**以及 `τ` 的粗不变量（note 46）** 上五次现身；
2. **已证的正结果**——shift 半的唯一典范化（note 39，任意 `n`）、`θ̃ = τ∘m`（note 43）、`O(P)` 是下集格的**格商**（note 45；非子格）。

**入口**：本笔记（大收束）→ `30`（树层总览）→ `40`（carousel–iota 总览）→ 各详细笔记。

---

## 0. 材料与两篇总览

| 材料 | 内容 |
|---|---|
| Donaghey 1980 | 四族 Catalan、R/L 双射、$M_P$/$M_Z$、primitive/Motzkin |
| Pushkarev–Byzov 2014 | 三定义（右分解/双射/`φ⁻¹θφσ`）、carousel、fringing、轨道、`Z₂*Z₂` |
| OEIS A014486 图表 | Catalan 结构罗塞塔 |
| AEG Paper 5 | 六态载体、`Ω=TSR`、`Ω²=-1`、手性符号律 |
| AEG Paper 3 | Hecke 周期轨道、零 dessin 编码脊（§5-q4-geodesic-knots）|
| Adva | `0010` 手性载体、iota frame（`J`,`H`,`A=-JH`）、iota 组合子、`0168` |

- `30` = 26–29 综合（树层）；`40` = 31–39 综合（carousel–iota）；**本笔记 = 二者之上，并入 42–46。**

---

## 1. 一个变换：Donaghey `τ`

**四族**（皆 $c_n$）：g.b.、b.b.、p.t.、t.p.t.(=PPCT)；外加 z.t.、+.b.b.。自然对应：`+.b.b.↔z.t.`、`(g.b.)↔p.t.`（up-down code = Dyck 词）。

**R/L 双射**：`g.b.→+.b.b.`，R=右梳、L=左梳；树级 PPCT↔PPT（顶点↔右/左路径）。

**三定义**（Thm 2.1）：归纳式（右分解→左分解）；`T→T^R→T'`；`τ=φ⁻¹θφσ`（σ=transposition、θ=reflection、φ=PPCT↔Dyck）。

**轨道**：carousel（Thm 4.3）；fringing（$\Delta(Q(T))=3\Delta(T)$ 或 $\tfrac32$）；轨道增长 $O(n^{\log_23})$；Thm 6.4 `⟨σ,θ̃⟩≅Z₂*Z₂`。

---

## 2. 与 AEG 树层的精确对应（note 30 §2；`θ̃` 见 note 43）

| Donaghey/PB | AEG | 状态 |
|---|---|---|
| **σ**（左右子互换）| 镜像 $m$（`def:mirror-temporal-reversal`）| 精确 |
| **θ**（Dyck 反向）| 时间反演 $r$ | 精确（路径级）|
| **θ̃ = φ⁻¹θφ**（路径反射）| **`τ∘m`**（note 43）| **精确（内在定义）** |
| **φ**（PPCT↔Dyck）| up-down 词编码 | 精确 |
| **R/L 双射** | 左/右梳 `conv:p0-left-right-convention` | 精确（集合层）|
| **四族** | 二叉树（顺序）vs 一般树（分支）| 精确 |
| **τ=φ⁻¹θφσ** | Donaghey 变换 | 结构对应（≠$mr$）|

**群结构**（note 30 §3；note 43）：AEG 的 $m,r$ 交换 → `Z₂×Z₂`（Klein）；Donaghey 的 $σ,\tilde θ$ 不交换 → `Z₂*Z₂`（无限二面体）。**note 43** 给出 `θ̃ = τ∘m` 的内在定义（`θ̃²=id`、`m∘θ̃=τ⁻¹`），从而**树层的 `Z₂*Z₂` 不再需要外部构造**。

**下降障碍**（note 29）：`τ` **不保持依赖偏序同构类** → **`τ` 不下降到 $O(P)$**；双曲性严格是平面树层现象。

**格归属**（note 28）：论文"分配格"= **无限三叉树的 Birkhoff 下集格**，非 Tamari（$T_4$ 非分配）；AEG `O(P)` 是同构造、不同偏序。**修正与收口**（note 45，OCR）：§5 原句的"standard lattice ordering"由括号解释为**分配（下集）格序**，非 Tamari；且 `O(P)=Down(P)` 是 `Down(T_∞)` 的**格商**（restriction `S↦S∩P` 满射保 ∪/∩），**不是包含子格**；抽象子格嵌入仍 open。

**函子性障碍**（note 44）：`R/L` 是集合双射 `PPCT(n叶) ↔ PPT(n-1边)`，但**操作数不保持**（PPCT 恒 `n-1`；PPT 分布 `{1,…,n-1}`），故**无"保序缺陷/保线性扩张"的函子性**——结构性否定。

**提升障碍**（note 46）：在 $n\le6$ 的检查中，`τ` 在 `O(P)` 层没有粗痕迹——不仅精确层不下降（note 29），连粗不变量 `e(P)`、`|O(P)|`、`height`、`incomp` **也全不保持**（$n\le6$）；真正的不变量是**平面** corner-type `(k,l)`（换对称，Cor 4.5）。一般 $n$ 仍 open。

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

## 4. 同一个障碍：平面/结构信息不可丢（五次现身）

这是把全部笔记串起来的**主线**：

- **note 29**：`τ` 不下降到 $O(P)$——`τ` 用左/右（平面）信息，而 `O(P)` **忘记**左/右。$n=4$ 见证。
- **note 32**：carousel = `J` 强形式证伪——`J` **保平面**，不能做 `SR→LL` 的**跨平面**入口。
- **note 33**：`H` 不能承载 index `k`——`H` 来自割图（unplanar），而 `k=#左叶` 是 planar；同谱不同 `k` 见证。
- **note 44**：`R/L` 双射**不保持操作数**（PPCT `n-1`，PPT `{1,…,n-1}`），故无保操作偏序的函子——"结构量不保"在**双射**上的现身。
- **note 46**：`τ` 的**粗不变量全不保**（`e`、`|O|`、`height`、`incomp`），真正不变量是平面的 `(k,l)`——"痕迹只在平面层"的现身。

> **同一个"结构量不可丢"的障碍，在 $\tau$、$J$、$H$、$R/L$、$\tau$ 的粗不变量上五次现身。** 这不是五个巧合，而是**一个结构性事实**：AEG 的"树层"是 planar 的，"偏序/割图/谱/一般树"层是 unplanar 的，二者不能互相完全承载。

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

## 6. 大收束：一张地图（26–46）

| # | 问题 | 结论 | 类型 | 笔记 |
|---|---|---|---|---|
| 1 | 一般树↔二叉树 | R/L=左右梳；σ/θ/φ=镜像/反演/词编码 | 精确对应 | 26/30 |
| 2 | `τ` 的群 | `⟨σ,θ̃⟩≅Z₂*Z₂`；AEG `⟨m,r⟩≅Z₂×Z₂` | 经典+对应 | 30 |
| 3 | comb 层 | AEG 操作给 Klein，非 `Z₂*Z₂` | 解决（note 27）| 27 |
| 4 | 依赖偏序下降 | `τ` 不保持偏序同构类 → 不下降 | 解决（负面）| 29 |
| 5 | 格归属 | = Birkhoff 下集格，非 Tamari | 解决 | 28 |
| 6 | carousel ↔ iota 三义 | 收缩 / frame / 组合子 | 辨析 | 31 |
| 7 | 旋转半 = `J`？ | 强形式证伪；非典范对齐；平面障碍 | 精确障碍 | 32 |
| 8 | iota frame | 螺旋；`H` 不承载 index | 计算 | 33 |
| 9 | planar 载体 | 螺旋模 `C⁴=S` | 计算 | 34 |
| 10 | `S` 的导出 | 角序后继；分支层=左优先 postorder | 对应 | 35/36/37 |
| 11 | 跨链典范化 | 唯一最少逆序 = 左优先 postorder | **PROVED（任意 $n$）** | 38/39 |
| 12 | `θ̃` 内在定义（098.1a）| **`θ̃ = τ∘m`**；`θ̃²=id`、`m∘θ̃=τ⁻¹`；`⟨m,θ̃⟩≅Z₂*Z₂` | **PROVED + 计算** | **43** |
| 13 | fringing/增长（098.3）| **结构对应成立**（自由积/原始/编码脊/order-4 旋转）；**增长律不成立**（长度 vs 计数）| 计算 | **42** |
| 14 | `R/L` 函子性（098.4）| **否定**：操作数不保持（`{3,3,3,3,3}` vs `{1,2,2,2,3}`）| **PROVED（负面）** | **44** |
| 15 | `O(P)` vs `Down(T_∞)`（098.2 残余）| **格商**（restriction 满射格同态），**非子格**；"standard"=下集格序 | **PROVED + 计算** | **45** |
| 16 | `τ` 的提升（098.1b）| **无偏序痕迹**：`e`/`|O|`/`height`/`incomp` 全不保；痕迹在平面 `(k,l)` | **计算** | **46** |
| 17 | 总览 | 树层 / carousel–iota / 大收束 | 收束 | 30/40/41 |

---

## 7. 地位总表（跨全部笔记）

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
| **`θ̃ = τ∘m` 内在定义 + `⟨m,θ̃⟩≅Z₂*Z₂`（098.1a）** | **`PROVED`（note 43）+ 计算（$n\le6$）** |
| **fringing/增长 ↔ Hecke 周期轨道（098.3）** | **结构 `[对应]`；增长律 `COMPUTATIONALLY VERIFIED` 的否定** |
| **`R/L` 函子性（098.4）** | **`PROVED`（负面，note 44）+ 计算（$m\le5$）** |
| **`O(P)` 是 `Down(T_∞)` 的格商（098.2 残余）** | **`PROVED`（集合论，note 45）+ 计算（$n\le7$ 节点）** |
| **`τ` 的提升：无偏序痕迹（098.1b）** | **`COMPUTATIONALLY VERIFIED EXAMPLE`（$n\le6$，note 46）** |

---

## 8. 开放问题（统一，2026-11-01 更新）

| 编号 | 问题 | 状态 |
|---|---|---|
| 098.1(a) | `θ̃` 内在定义 + 与 `m` 生成 `Z₂*Z₂` | **RESOLVED（note 43）** |
| 098.1(b) | `τ` 不下降（note 29）+ 提升无偏序痕迹（note 46）| **$n\le6$ 负面证据**；一般 `n`、轨道级分布、`O(P)` 商上的多值痕迹 open |
| 098.2 | 格商与非包含子格（note 45）；"standard"=下集格序（OCR）| **文本与商关系解决**；抽象子格嵌入、精确条件、`O(P)` 的 Galois 细结构 open |
| 098.3 残余 | 精确 order-4 对接（carousel `J` ∼ Hecke `R²`）；码的翻译；增长律正确配对（替换 Perron 值）；`Hist_4^{ph}` ↔ `τ`-轨道 | open |
| 098.4 残余 | `R/L` 映射本身的构造与像的核对；换对象的函子性（`O(P)`、`Hist_4`）| open |
| 新 | 平面/结构障碍的"必然性"：能否证明**不存在** unplanar 载体承载 carousel / 不存在保结构的 `R/L` 函子？| open |
| 新 | 典范化的 $\sigma$-等变性；其他内蕴准则同解性 | open |
| 新 | `θ̃` 的词层直接公式；`θ̃ = r` 的精确条件；`⟨m,θ̃⟩` 的几何实现 | open |

---

## 9. 参考

- Donaghey 1980；Pushkarev–Byzov 2014；OEIS A014486。
- AEG：`paper-5/sections/04-six-state-carrier.tex`；`paper-1/sections/02-sequential-histories.tex`；`paper-0/sections/03-aes-and-motion.tex`；`paper-3/sections/05-q4-geodesic-knots.tex`（Hecke 周期轨道、零 dessin 编码脊）。
- Adva：`docs/research/0010-causal-cut-chirality-cube.md`、`knowledge/received/iota-frame-knowledge-2026-09-17-v1/materials/{frame.md,algebra.py}`、`docs/research/0168-...`、`murphy-iota-v0/`。
- 详细笔记：`26`–`46`（两篇总览 `30`/`40`；大收束 `41`）；计算：`research/donaghey-orbits/`、`research/ppct-lattice/`、`research/iota-carousel/`。
