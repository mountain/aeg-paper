# 权威修正案：Paper 0 作为几何基础

**状态：** 权威修正案  
**版本：** 1.0  
**日期：** 2026-09-22  
**适用于：** `governance/00-authoritative-scope.md`、`governance/00a-paper-0-amendment.md`、
`governance/01-paper-series-architecture.md`、`AGENTS.md`，以及 Paper 0 / Paper I 手稿  
**优先性：** 本修正案取代 `00a-paper-0-amendment.md` §§2–5，以及
`00-authoritative-scope.md` §20 与 `01-paper-series-architecture.md` 中涉及下文 §1.5 重新
分配对象的拥有权行。凡 `00a` 禁止 Paper 0 发展仿射余循环、全局 torsion、连续算术流、基本
双曲模型或接触几何之处，该禁令被解除，拥有权按此处所述重新分配。`00`、`00a` 与 `01` 的
其余所有限制仍有效。

---

## 1. 范围修订陈述

`governance/00-authoritative-scope.md` §27 只允许通过陈述七项的显式范围变更任务修订该文档。
此处针对 Paper 0 与 Paper I 之间修订后的边界陈述这七项。

### 1.1 旧规则

`00a-paper-0-amendment.md` 固定以下边界。

* §2 使 Paper 0 成为*初级前奏*：两个纯梳约定、仿射点路径图景、ripple 铅笔图景、倒数、
  极点、无穷、迭代不动点、初等矩阵，以及 `Aff(1,K) = Stab(infinity) < PGL_2(K)`。
* §3 使 Paper 0「不得作为主要理论发展」：超出纯梳证明的内在依赖偏序分类；混合手性标记
  脊柱历史；Hecke `q=4` 历史语言；**仿射余循环与全局 torsion**；**作为完整内在理论的连续
  仿射流**；正则零刚性或奇异零分类；**接触几何、水平演算或函数论**；射影双赋值、商塔或
  计算复杂度；以及无穷算术表达式的一般收敛理论。
* §4 保持 Paper I 作为（除其他外）仿射余循环、连续流、正则 AES 定义、完整齐次双曲模型、
  ACS torsion 与接触曲率的规范拥有者。
* §5 记录八个初等 Paper 0 项的 `proved with stated hypotheses` 状态，并记录四个开放计划：
  ripple 几何内在的射影算术表达式空间；商稳定 path/ripple 不变量；多线 path/ripple 语义；
  以及无穷算术表达式的一般理论。

因此 `00-authoritative-scope.md` §20 没有 Paper 0 列，且 `05-mathematical-status.md`、
`06-editorial-rules.md`、`07-acceptance-checklist.md`、`source-inventory.md` 与 `AGENTS.md`
描述一个四论文系列。

### 1.2 提议的新规则

Paper 0 成为系列的**规范几何基础**。它以自身的定义、证明、示例与图件发展：

1. 算术表达式的展开代数：显式操作数槽位约定下的左/右展开梳、作为联系同一表达式不同展开
   的重写规则的分配律，以及机械展开的机械化谱系；
2. 作为加、减、乘、除作为*运动*作用其中的空间的算术表达式空间（AES）：正则 AES 公理、
   规范算术框架、基本双曲模型 `E_0`、连续算术流，以及按其穿孔数索引的模型族 `E_k`；
3. AES 的射影对偶读法，称为 **ripple geometry**；
4. AES 的**交换化**、累积交换空间（ACS）、双历史仿射余循环，以及把算术 torsion 重新解释
   为对照 ACS 度量的 AES *撕裂*；
5. 该撕裂的**接触结构**：算术接触形式、水平场、曲率括号与有限开/闭缺陷比较；
6. 走出线性语言（流形、切空间、Lie 群、模）的结构性提案，记录为提案而非定理；
7. **有孔（穿孔）算术表达式空间**与撕裂词汇，按 §1.5 与 `05b` 的论断状态记录。

Paper I 保留历史层：顺序树与标记脊柱历史、镜像 / 时间反演 / 路径逆、年代历史的射影求值、
`q=4` Hecke 子语言、正则与奇异零理论，以及与 Papers II–IV 的接口。Paper I 导入 Paper 0 的
几何对象，并只把它们陈述为其自身定理所需的简明重述。

系列架构在箭头层面不变：`Paper 0 -> Paper I -> {Paper II, Paper III}` 与
`Paper I -> Paper IV`。

### 1.3 数学理由

`00a` §3 从 Paper 0 撤回的对象不是初级前奏：它们形成一个连贯的几何理论，其中每个后续对象
都由前一个对象*定义*。

* 算术 torsion 不是单独历史语言的不变量。在双历史表述中，它是共享一个尺度的两次求值之间
  的缺陷，其精确值是交换 charge 平面上的 `e^{M_*-M}` 加权面积。ACS 不是几何之后添加的记账
  装置；它是非交换 AES 的交换化，torsion 是 AES 求值通过该交换化下降的阻碍。
* 接触形式 `da - mu du - lambda a dv` 是*同一个*缺陷的局部形式。其曲率
  `[D_u,D_v] = mu lambda d/d a` 是该阻碍的无穷小密度，水平分布不可积恰是「没有局部校准能
  让两个算术方向同时变直」的陈述。那是关于 AES 的陈述，不是关于后续分析理论的陈述。
* 双曲模型 `E_0` 是加法与乘法首次非平凡地互相传输彼此尺子的地方。其框架、度量、曲率、
  horocyclic 坐标与赋值 Laplacian 是后续每个关于 AES 论断得以检验的模型数据。
* 把模型、流、余循环、交换化与接触形式拆分到两篇论文会迫使读者持有一个半定义的对象，并
  产生恰是 `AGENTS.md` 所禁止的「竞争的规范版本」。

因此这一移动保留数学含义：它把单一理论迁移到引入其初等情形的论文，并把历史层留给 Paper I。

### 1.4 受影响的论文

| 论文 | 影响 |
|---|---|
| Paper 0 | 吸收 §1.5 所列的几何章节与附录；获得下文 §§7–10。 |
| Paper I | 失去那些章节；保留历史、射影语义、Hecke 与零几何章节；获得一个简短导入接口。 |
| Paper II | 其对正则 AES 定义、规范框架、双曲模型与接触模型的引用重新指向对象移动后的 Paper 0；其数学内容不变。 |
| Paper III | 其对正则 AES 定义、双边初等算子与孤立零盘的引用重新指向对象移动后的位置；不改论断。 |
| Paper IV | 其对仿射 torsion 的两处引用重新指向 Paper 0；不改论断。 |
| `AGENTS.md`、`README.md`、`governance/README.md`、`source-inventory.md` | 更新为描述五论文系列。 |

### 1.5 所需迁移

迁移状态遵循 `00-authoritative-scope.md` §21：材料被移动，而非静默删除；选择一个规范目的
地；Paper I 只保留连续性所需的最少陈述。

| 来源（Paper I） | 目的地（Paper 0） | 迁移状态 | 论断处理 |
|---|---|---|---|
| `sections/04-affine-cocycles.tex` | `sections/07-acs-tearing.tex` | `MOVE` | `PRESERVE` |
| `sections/05-affine-flow.tex` | `sections/03-aes-and-motion.tex` | `MOVE` | `PRESERVE` |
| `sections/06-hyperbolic-model.tex` | `sections/03-aes-and-motion.tex` | `MOVE` | `PRESERVE` |
| `sections/08-acs-torsion.tex` | `sections/07-acs-tearing.tex` | `MOVE` | `PRESERVE` |
| `sections/09-contact-curvature.tex` | `sections/08-contact-of-tearing.tex` | `MOVE` | `PRESERVE` |
| `appendices/app-B-affine-cocycles.tex` | `appendices/app-C-affine-cocycles.tex` | `MOVE` | `PRESERVE` |
| `appendices/app-C-hyperbolic-calculations.tex` | `appendices/app-B-hyperbolic-calculations.tex` | `MOVE` | `PRESERVE` |
| `appendices/app-D-acs-contact.tex` | `appendices/app-D-acs-contact.tex` | `MOVE` | `PRESERVE` |
| `sections/02-sequential-histories.tex` | --- | `KEEP` | `PRESERVE` |
| `sections/03-projective-affine.tex` | --- | `KEEP` | `PRESERVE` |
| `sections/07-zero-geometry.tex` | --- | `KEEP` | `PRESERVE` |
| `sections/10-conclusion.tex` | --- | `REWRITE` | `PRESERVE` |
| `sections/01-introduction.tex`, `sections/00-paper-zero-interface.tex` | --- | `REWRITE` | `PRESERVE` |
| `appendices/app-A-conventions.tex`, `appendices/app-E-equality-neutrality.tex` | --- | `KEEP` | `PRESERVE` |

Paper I 恰好保留一个导入定义：带其规范算术框架的 `def:regular-aes`，简明重述并标记为从
Paper 0 导入。这是 `00a` §4 为初等矩阵表已认可的刻意接口重复，且是必需的，因为 Paper I 的
零定理是用该定义陈述的。Paper 0 的其他定理不在 Paper I 中重复。

### 1.6 对定理依赖的影响

* 本次迁移不改变任何已证明陈述的数学内容、假设或标签。标签随其源文件移动，故被移动的
  标签（`def:acs`、`thm:torsion-stokes`、`thm:contact-curvature`、`def:regular-aes`、
  `thm:continuous-affine-flow`、`thm:basic-hyperbolic-aes`、`` `prop:affine-cocycle-formulas` ``
  与 §1.5 列表其余）现在在 Paper 0 内解析。
* Paper I 获得对 Paper 0 的前向依赖：正则 AES 定义、规范算术框架、基本双曲模型、算术流、
  仿射余循环、ACS 与接触结构。这与架构箭头 `Paper 0 -> Paper I` 一致。
* Paper 0 只在顺序树分类 `thm:sequential-tree-classification` 与标记历史层上获得反向依赖，
  它们留在 Paper I。因此 Paper 0 前瞻性引用 Paper I 且不重述该分类；其自身梳陈述
  `prop:p0-combs-unique-order` 有意保持较弱，与之前完全一致。
* Papers II–IV 继续从系列导入而非重定义几何；§1.4 的重新指向引用是编辑性的，不是数学性的。

### 1.7 对当前草稿的影响

* Paper 0 从 7 节重建为 11 节、从 1 附录重建为 4；其标题与摘要改变以匹配其新角色。早先
  paper-0 结果集原地保留（同标签、同证明）并被扩展，而非被替换。
* Paper I 从 10 节重建为 5 节、从 5 附录重建为 2。每个被移除的数学陈述在 Paper 0 中以相同
  标签与状态保留。
* Papers II、III、IV 只接受引用重新指向。
* `AGENTS.md` 更新为描述五篇论文；其 Paper I 范围纪律节由显式 Paper 0 范围纪律节扩展。
  `paper-0/AGENTS.md` 相应重写。
* 每个实质性 Paper 0 结果（包括被移动者）的状态记录于新登记
  `governance/05b-paper-0-status-register.md`；迁移条目记录于 `governance/migration-log.md`，
  源映射记录于 `governance/04-current-to-target-map.md`。

---

## 2. 本修正案后 Paper 0 拥有什么

Paper 0 是以下内容的规范来源：

1. `L_k`/`R_k` 操作数槽位递归下的左/右展开梳文法、单孔截面、对偶运算对应，以及第二槽
   除法的仿射/射影断裂；
2. 作为同一表达式不同展开之间重写的分配律，以及随之而来的表达式、其展开、其诱导算子与
   其值之间的区分；
3. 正则算术表达式空间、其 eikonal 恒等式与规范算术框架；
4. 作为 AES 运动的四则运算，包括仿射网格移动、Baumslag–Solitar 型关系与第二槽除法的射影
   运动；
5. 基本双曲模型 `E_0`（与 Paper I 旧记号 `E_{\mathrm{hyp}}` 恰好等同一次）、其 horocyclic
   坐标、曲率与赋值 Laplacian；
6. 连续算术流及其矫正；
7. 一个年代矩阵乘积的点路径与 ripple 铅笔读法；
8. 仿射余循环、相对仿射缺陷与离散双历史比较；
9. 累积交换空间（ACS）、直接 ACS 求值公式、加权 torsion–Stokes 定理，以及把 torsion 解释为
   撕裂；
10. 算术接触形式、水平场、曲率括号、有限开闭缺陷与标量水平微分；
11. 用显式非线性代数结构取代线性语言的结构性提案，包括过程几何接口；
12. 有孔算术表达式空间 `E_k`、其穿孔与撕裂词汇。

## 3. Paper 0 仍不得发展什么

Paper 0 仍不得作为主要理论发展：

* 任意顺序树的内在依赖偏序分类（`thm:sequential-tree-classification` 仍是 Paper I 结果；
  Paper 0 引用它）；
* 作为其主要对象的混合手性标记脊柱历史；
* Hecke `q=4` 历史语言；
* 正则零刚性、奇异零分类、零网络、管、辫或纽结不变量；
* 算术全纯函数论、边值理论或谱理论；
* 射影双赋值、商塔、凝聚或计算复杂度；
* 无穷算术表达式的一般收敛理论；
* 任何声称射影 ripple 族是新的几何同构类、或接触形式强制相容复结构的论断。

## 4. 论断状态政策

每个实质性 Paper 0 结果带 `00-authoritative-scope.md` §23 的九个标签之一。登记
`governance/05b-paper-0-status-register.md` 对 Paper 0 权威，并与 `05-mathematical-status.md`
一起维护。被移动结果保留其在 Paper I 中的状态；被移动不提升任何结果。

本修正案固定的术语：

* `ripple geometry` 是对通过射影算术算子拉回输出条件所得条件族的**描述性名称**。其进一步
  结构是开放计划，记录于 `08-open-questions.md`。
* `tearing` 是**结构性提案**：对照交换化 ACS 读出的 AES 求值双历史缺陷的名称，其精确值是
  `thm:torsion-stokes` 的已证明加权面积，其无穷小密度是 `thm:contact-curvature` 的已证明
  曲率 `mu lambda`。
* `holed arithmetic expression space` 是对其穿孔为其已声明奇异点的穿孔 AES 的**描述性定义**；
  已验证实例仍是孤立零盘，从探索登记导入的不可能性陈述保留 `computationally verified
  example` 状态。

## 5. 所需仓库变更

1. `paper-0/aeg-paper-0.tex` 仍是规范入口，`./build.sh 0` 是规范构建；产物仍是
   `paper-0/aeg-paper-0.pdf`。
2. `paper-1/aeg-paper-1.tex` 仍是 Paper I 入口。
3. `AGENTS.md` 描述五篇论文并带显式 Paper 0 范围节。
4. `README.md`、`governance/README.md` 与 `source-inventory.md` 把 Paper 0 列在最前。
5. `governance/migration-log.md` 为每个被移动章节与附录记录一条迁移条目；
   `governance/04-current-to-target-map.md` 记录每个所列源块的迁移状态。
6. `governance/paper-0-closure-report.md` 接受一个记录本修正案的带日期闭包后节；更早的带日期
   记录不被编辑。
7. `bibliography/aeg-paper.bib` 只增加实际使用的引用，历史或技术比较用一手参考文献。

## 6. 已记录冲突

遵循 `AGENTS.md`（「不静默调和冲突来源」），以下冲突存在并被记录而非隐藏：

* **C-10.** 本修正案之前，`AGENTS.md` 与 `governance/README.md` 描述四论文系列，而 `00a`
  插入第五篇。本修正案更新那些文件并在一个地方一次性陈述五论文系列。
* **C-11.** `00-authoritative-scope.md` §20 把「基本双曲模型」、「torsion」与「接触联络」
  分配给 Paper I。本修正案把那些行重新分配给 Paper 0，并是对它们的更高优先来源；§20 表
  不另行修订。
* **C-1（既有）。** 历史标签 `E_0` 与 `E_1` 在 `notes/` 中使用不一致。Paper 0 采纳 §7 的
  对应表并恰好一次把 `E_0` 与旧 `E_{\mathrm{hyp}}` 等同。本修正案不编辑任何笔记。

## 7. 模型名对应表

`06-editorial-rules.md` §28 与 §89 在任何模型名编辑前所要求。

| 标签 | 本修正案后的含义 | 旧名 |
|---|---|---|
| `E_0` | 上半平面上的基本**正则**双曲模型，无穿孔 | `E_0`（Paper 0）、`E_{\mathrm{hyp}}(\mu,\lambda)`（Paper I）、「第零类模型」、`notes/analysis-and-calculus/04-hyperoperation.md` 中的 `E_1`（倒置用法，记录为 C-1） |
| `E_1` | **单穿孔**盘模型：单位盘，中心孤立零从正则轨迹移除 | 「孤立零盘」（Paper I §7）、某些 `notes/` 源中的 `E_1` |
| `E_k` | 描述性族标签：带 `k` 个已声明穿孔的 AES；**不是**已确定分类 | 历史 `E_k` 研究标签（Paper III README） |
| `E_{\log}` | 保留的历史标签，本修正案**不**定义 | 历史 `E_{\log}` 研究标签 |

`E_k` 与 `E_{\log}` 仍是历史研究标签。本修正案不定义按 `k` 的分类；它只固定 `E_0` 与 `E_1`
的含义，并描述性使用 `E_k`。
