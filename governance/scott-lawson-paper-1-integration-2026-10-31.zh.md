# Scott–Lawson 拓扑落回 Paper I 主体：整合登记

**文件：** `governance/scott-lawson-paper-1-integration-2026-10-31.md`
**状态：** 集成记录（研究主线摘要与登记；不修订范围、不提升任何论断）
**日期：** 2026-10-31
**拟定：** DeepSeek Harness（AI 编码代理），在仓库作者指导下；所有数学状态使用
`governance/05-mathematical-status.md` 与 `governance/notes-reserve-audit.md` 的词汇，此处不
改变任何论断状态。
**依赖：**

* `AGENTS.md`
* `governance/00-authoritative-scope.md`
* `governance/05-mathematical-status.md`
* `governance/08-open-questions.md`
* `governance/notes-reserve-audit.md`

**适用于：** `notes/analysis-and-calculus/09`–`20`，及其与
`paper-1/sections/02-sequential-histories.tex`、`paper-1/sections/03-projective-affine.tex`
与 `paper-0/sections/09-contact-of-tearing.tex` 的接触。

---

## 1. 目的与溯源

本记录登记 2026-10-31 进行的一条连续研究主线：把最近的 Scott/Lawson 词汇笔记
`notes/analysis-and-calculus/09-order-topology-scott-lawson.md` 读回 **Paper I 主体**（历史层
与射影语义），并从那里进入 **Paper 0 §9 的接触结构**。该主线产生十二条新笔记（`10`–`20`）并
关闭 OQ-094 的四个子项，且终结于一条精确陈述：

> **接触曲率 `μλ` 是极小分支 DAG `{add, multiply}` 的序缺陷，在两条线程之间区域上（作为
> 1-余循环）积分；体（有限 DAG）是平坦的，缺陷是活在理想边界（曲面）上的边界 holonomy。**

该主线不改变、添加或提升任何 Paper I 或 Paper 0 定理。该主线是连接现有已证明事实（Paper 0
的 `thm:contact-curvature`、`thm:torsion-stokes`、`thm:legendre-dual-tearing`；Paper I 的
`thm:bilateral-pgl2-generation`、`cor:affine-borel-sector`）到 Paper I 历史域论结构的
**结构读法**。

---

## 2. 脊柱（笔记 09–20）

| 笔记 | 内容 | 状态（等级） |
|---|---|---|
| `09` | Scott/Lawson 词汇；前缀序信息序；加法 = way-below、乘法 = Scott 自同构、对偶 = 倒数；理想完备化 = 有限∪无穷历史 | STRUCTURAL PROPOSAL + REFORMULATION（OQ-091 部分、OQ-092/093 解决） |
| `10` | 生成元对应：`T_s = C_{+,s}^{(1)}`、`D_k = C_{×,k}^{(1)}`、`¬ = C_{/,1}^{(2)}`；映射到 Paper I §2–§3 | STRUCTURAL PROPOSAL + REFORMULATION |
| `11` | OQ-094a 证明骨架：Scott ⟷ `Aff^+`、Lawson ⟷ `PGL₂`；`10` §2 修正（`Aff^+`、`B_∞^+`、`B_∞`、`PGL₂` 层级；`D_{-1} = T_1¬T_{-1}¬T_1¬`） | 094a RESOLVED |
| `12` | Galois 连接：同胚层 `{D_k}` ↦ `Stab([0,∞])`、内层 `Aff^+` ↦ `PGL₂` | 094a RESOLVED |
| `13` | 函子语言：交换图 + 自然性 `Φ(σ∨¬_*σ)=⟨Φ(σ),¬⟩`；非完整 Galois 等价 | 094a RESOLVED |
| `14` | 094b：`ρ` 仅对平凡预序单调；无 Scott 连续延拓；唯一候选 = 无穷矩阵积 = 连分数（范围外） | 094b RESOLVED |
| `15` | 094c：分支历史 dcpo；信息序 = 下集（理想）嵌入；`Idl(FinDAG)` = 有限∪无穷 DAG；Birkhoff `O(P)`；前缀 = 链特化 | 094c RESOLVED（核心） |
| `16` | 094d：Hecke 历史空间 = Cantor；`G₄ ≅ C₂*C₄` 虚拟自由（端 = Cantor）；`H(√2)` 第一类（极限集 = 圆）；`10` §4 修正 | 094d RESOLVED |
| `17` | 接触曲率 = `{A,M}` 的序缺陷；Birkhoff `Stone(O({A,M}))={A,M}`；细化：DAG 平坦、曲率来自非交换实现 | REFORMULATION + STRUCTURAL PROPOSAL |
| `18` | 极限/光滑化函子：生成元 = 精确流；词 = 复合；序缺陷 = 流交换子 = Lie 括号 `[D_u,D_v]=μλ∂a`（BCH） | proved（成分） |
| `19` | 积分 + 体边界：全息 Stokes；体平坦、曲率 = 边界 holonomy；`O(P)` 上离散 Stokes（开放） | STRUCTURAL PROPOSAL + open |
| `20` | 缺陷是群值 1-余循环：telescoping 可加性；局部缺陷 = 后缀共轭交换子；BCH 展开；六边形 = Jacobi 恒等式 | proved（成分） |

链条是：**09（词汇）→ 10（生成元对应）→ 11–16（OQ-094 a–d）→ 17–18（接触 = DAG 缺陷）→
19（体边界）→ 20（1-余循环）**。

---

## 3. 可证明核心（本主线确立什么）

以下**由现有来源**（Paper 0、Paper I）加 `CLASSICAL` 域论 / Lie 论证明；无一个是新论文定理，
全部是已证明事实的读法或组装：

1. **生成元对应**（`10` §1）：`T_s`、`D_k`、`¬` 字面上就是 Paper I 的初等语境
   `C_{+,s}^{(1)}`、`C_{×,k}^{(1)}`、`C_{/,1}^{(2)}`。
2. **Scott ⟷ Aff⁺、Lawson ⟷ PGL₂**（`11`–`13`）：在 `L=[0,∞]` 上，仿射 Scott 连续幺半群是
   `Aff^+ = C(σ)∩B_∞ = {ka+s : k>0, s≥0}`；群 `⟨Aff^+,¬⟩ = PGL₂`；「邻接 ¬」交换
   （`Φ(σ∨¬_*σ)=⟨Φ(σ),¬⟩`）。它是生成数据的自然同构，**不是**完整 Galois 等价（三个已证明
   理由：`A(σ)=A(λ)`、`H(λ)=Stab([0,∞])⊊PGL₂`、`¬T_s¬∈E(σ)∖Aff^+`）。
3. **ρ 无 Scott 连续延拓**（`14`）：`ρ` 仅对平凡预序单调；唯一候选极限延拓是无穷矩阵积 =
   连分数（Paper I 范围外）。
4. **分支历史 dcpo**（`15`）：信息序 = 下集嵌入；`Idl(FinDAG)` = 有限∪无穷计算 DAG；紧 =
   有限；前缀序是链特化；`O(P)` 是有限分配格，线性扩张 = 极大链 = 脊柱历史（Birkhoff）。
5. **Hecke 历史空间**（`16`）：`Γ_4^≤ω` 是 Cantor 空间；`G₄ ≅ C₂*C₄`（端 = Cantor），而
   `H(√2)` 是第一类（极限集 = `P^1(ℝ)`，非 Cantor）。
6. **接触曲率 = 极小 DAG 序缺陷**（`17`–`18`）：生成元是 `D_u, D_v` 的精确流；`{A,M}` 的序
   缺陷有无穷小密度 `μλ = [D_u,D_v](a)`（BCH；非平凡步是 Paper 0 的
   `prop:torsion-curvature-synthesis`）。
7. **缺陷是 1-余循环**（`20`）：telescoping 可加性（精确）；局部缺陷 = 后缀共轭交换子；六边形
   闭包 = Jacobi 恒等式。

---

## 4. 结构提案（整合读法）

这些是给主线形状的「读法」；它们是连贯的但**不是定理**，只能作为 `structural proposal` 引用：

1. **「接触 = 体积计算的 DAG 语言」**（`17` §4）：接触结构是极小分支 DAG `{A,M}` 的无穷小
   形式；完整 DAG 语言（笔记 `15`）是其宏观推广。
2. **体边界对应**（`19`）：体 = 有限 DAG（平坦、紧）；曲面 = 理想边界（无穷历史 = 「极限」）；
   缺陷是活在曲面上的边界 holonomy。这是「全息」读法。
3. **Alexandrov 对 Scott = 展平对保留曲面**（`19` §4，来自其前讨论）：Alexandrov 把理想边界
   物化为孤立点；Scott 把它保持为真正极限。体边界对应只在 Scott 读法下成立。

---

## 5. 开放问题（残差；登记 OQ-095）

主线留下以下**开放**项（无一阻塞 §3 的可证明核心）：

1. **高阶括号**（`18` §8、`20` §8）：BCH 高阶项 `[X,[X,Y]]`、`[Y,[X,Y]]`、… 是否对应多反链
   边的嵌套缺陷？需要把单菱形缺陷推广到 `O(P)` 的高维胞腔。
2. **完整 DAG Lie 实现**（`18` §8）：函子 `F` 定义在两个生成元 `{A,M}` 上；推广到任意生成元
   集需要自由 Lie 代数 / 自由流群实现（DAG dcpo → 自由 Lie 代数）。
3. **宏观 Stokes**（`19` §3）：「`O(P)` 上的离散 Stokes」——两线程间缺陷 = 区域上 `∫∫ μλ`，对
   任意 `P`——在 1-余循环层（`20`）确立，但组装成任意 `P` 的完整陈述（可加性 + 精确性 + 与
   `15` §6 的谱对接）尚未写出。
4. **谱对接**（`19` §3、`20` §8）：`O(P)` 的 Scott/Lawson 拓扑作为离散 Stokes 复形的谱空间。

---

## 6. 范围映射（哪篇论文拥有什么）

| 内容 | 拥有者 | 状态 |
|---|---|---|
| 标记脊柱历史、前缀序、`PGL₂` 生成、仿射/Borel、Bruhat、Hecke `q=4` | Paper I | proved（已有） |
| 接触形式、水平场、曲率 `[D_u,D_v]=μλ∂a`、torsion-Stokes、Legendre 对偶 | Paper 0 | proved（已有） |
| Paper I §2–§3 的 Scott/Lawson 读法（`11`–`16`） | 笔记储备（非论文） | 作为笔记解决 |
| 接触 = DAG 缺陷、体边界、1-余循环（`17`–`20`） | 笔记储备（非论文） | structural proposal + open |
| 无穷表达式（连分数）的一般收敛 | Paper II/III | 从 Paper I 排除（094b） |
| 高阶括号、宏观 Stokes、谱对接 | 笔记储备 → 未来 | open（OQ-095） |

---

## 7. 论断纪律（不得说什么）

* 「Scott ⟷ 仿射扇区」必须读作 `Scott ⟷ Aff^+`（正仿射**半群** `{ka+s : k>0, s≥0}`），而非
  `B_∞`（完整仿射群，已含反射 `D_{-1} = T_1¬T_{-1}¬T_1¬`）。
* 「Lawson ⟷ PGL₂」是**生成数据的自然同构**，不是 `Top(L)` 上的 Galois 等价（`13` §4）。
* 「接触 = DAG 语言」是在极小反链 `{A,M}` 处的**无穷小**形式，不是声称接触结构分类任意分支
  DAG。
* 体边界（「全息」）读法是 `structural proposal`；缺陷是边界 holonomy **已被证明**
  （Stokes + `dα` 精确），但「曲面 = 理想边界 = 曲率所在」是读法。
* Alexandrov/Scott「展平对保留」对比是读法，不是 Paper I 定理。

---

## 8. 处置（推荐下一步）

1. 在 `governance/08-open-questions.md` **登记 OQ-095**（§5 的四个残差）。[本记录命名它们；
   登记条目随后。]
2. 在 `governance/notes-reserve-audit.md` §2.2 **给笔记 10–20 定级**（当前只有 `09` 在那里
   定级；`10`–`20` 是新的且未定级）。
3. **决定提升问题**：§3 的可证明核心（第 6–7 项，经函子接触曲率 = DAG 缺陷）是否值得在
   Paper I §3 或 Paper 0 §9 有一个短「序拓扑读法」小节，按记录状态。此处不执行提升。
4. 下一步**攻克 OQ-095.1**（高阶括号）：这是宏观 Stokes（OQ-095.3）与完整 DAG Lie 实现
   （OQ-095.2）的门。

---

**拟定：** 2026-10-31。本记录不改变论文源与论断状态；它登记主线、其可证明核心、其提案与其
残差，并命名后续登记步骤。
