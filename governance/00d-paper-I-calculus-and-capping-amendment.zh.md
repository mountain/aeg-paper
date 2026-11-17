# Paper I 演算与封顶修正案

**文件：** `governance/00d-paper-I-calculus-and-capping-amendment.md`
**状态：** 权威范围修正案（修订 `00-authoritative-scope.md` §27 程序；在所述处取代
Paper I / Paper 0 边界）
**版本：** 1.0
**日期：** 2026-10-31
**依赖：** `governance/00-authoritative-scope.md`、`governance/00b-paper-0-geometric-foundation-amendment.md`、`governance/02-paper-I-outline.md`

---

## 1. 旧规则

按 `00-authoritative-scope.md`（及 `AGENTS.md` 的 Paper I / Paper 0 范围纪律）：

* **Paper 0** 拥有几何基础：算术表达式空间及其运动、基本双曲模型 `E_0`、穿孔模型
  `E_1`、累积交换空间（ACS）、仿射余循环与 torsion–Stokes 定理、带曲率 `μλ` 的接触结构，
  以及穿孔/紧化章节（§§11–12）。
* **Paper I** 拥有顺序语法、标记脊柱历史、射影语义、仿射/Borel 扇区、Hecke `q=4`
  子语言，以及正则/奇异零几何。它**不得**发展分析（微分/积分/级数）、序拓扑或孔–盖
  几何。

---

## 2. 提议的新规则

**Paper I 升级为自包含合卷**，标题为 *AEG I: Foundations of History Calculus and
Hole–Cap Geometry*，含九节与四个附录。它吸收以下内容作为自己的定理（状态记录于
`temp/paper_1_detailed_writing_plan.md` §4 的集成审计矩阵）：

1. 顺序与分支历史的 Scott–Lawson 序拓扑（笔记 `09`–`16`、OQ-091–094）；
2. 分析三支柱——微分（光滑化 Lie 函子、极小 DAG 缺陷、分次水平演算）、积分（混合仿射
   积分、对偶伴随配对、1-余循环、全息 Stokes）与级数（自由 Lie 代数 Magnus 展开、
   arity–胞腔对应、PBW 交换化）——建立于历史/DAG 层（笔记 `02`–`03`、`17`–`24`、
   OQ-095）；
3. 孔–盖精细几何（五重孔分类、球–管加厚、孔–盘互补、常边界封顶阻碍、认证密封）
   （笔记 `25`、OQ-096）；
4. Paper 0 §8（ACS、torsion–Stokes）、§9（接触形式、水平场、曲率 `μλ`）、§11（穿孔
   AES）与 §12（紧化/collar 下降）的**自包含重述**，使 Paper I 无需 Paper 0 后半部即可
   阅读。

**Paper 0** 保留其 §§1–7（表达式展开、算术运动、双曲/穿孔模型、作为运动的四则运算、
对偶读法、交换化、撕裂）作为几何来源；其 §§8–9、§§11–12 成为 Paper I 以相同标签重述其
结果的规范上游。

---

## 3. 数学理由

分析支柱建立于**历史/DAG 层**（下集 dcpo、线性扩张图、生成元的自由 Lie 代数）——这是
Paper I 的核心对象——而非仅建立于几何基础。Scott–Lawson 序拓扑提供了「求值连续性」所需
的域理论；接触曲率 `μλ` 是极小分支 DAG `{add, multiply}` 的序缺陷；孔–盖几何是下集格
`O(P)` 的几何伴侣（其极大链就是脊柱历史）。把它们拆分到两篇论文会割裂一条逻辑脊柱。

---

## 4. 受影响的论文

* **Paper 0** — §§8–9、§§11–12 成为被引用的上游；§§1–7 不变。
* **Paper I** — 从 6 节 + 2 附录扩展到 9 节 + 4 附录。

---

## 5. 所需迁移

* Paper 0 的 `thm:torsion-stokes`、`eq:arithmetic-contact-form`、
  `eq:horizontal-arithmetic-fields`、`thm:contact-curvature`、
  `def:p0-punctured-aes`、`def:p0-collar-contract`、`prop:p0-aes-collar-descent`
  在 Paper I 中以相同标签**重述**（每个结果一个规范来源移到 Paper I；Paper 0 前向引用）。
* 笔记 `02`–`03`、`09`–`25` 按集成审计矩阵记录的等级提升进 Paper I；任何 `STRUCTURAL
  PROPOSAL` 或 `COMPUTATIONALLY VERIFIED EXAMPLE` 未经 §4 集成审计不得提升为 `PROVED`。

---

## 6. 对定理依赖的影响

* 接触曲率 `μλ`、ACS 面积公式与 torsion–Stokes 现在位于 Paper I（其下游消费者是 Paper II
  的调和分析与 Paper III 的管几何）。
* Paper 0 的零几何章节（§§11–12）保留其对 Paper I 正则 AES 分裂的依赖；接触/ACS 内容的
  箭头反向。

---

## 7. 对当前草稿的影响

* `paper-0/aeg-paper-0.tex`：§§8–9、§§11–12 增加前向指针「在 Paper I 中重述」；源保留但
  不再是唯一规范之家。
* `paper-1/aeg-paper-1.tex`：`\input` 列表增至 9 节（`00`–`09`）+ 4 附录（`app-A`–`app-D`）；
  新文件 `04-differential-theory.tex`、`05-integral-theory.tex`、`06-series-theory.tex`、
  `07-holes-and-zero-geometry.tex`、`08-caps-and-interface-disks.tex`、`09-conclusion.tex`，
  以及 `appendices/app-C-magnus-sympy-verification.tex`、
  `appendices/app-D-pants-cellulation-verification.tex`。

---

**拟定：** 2026-10-31。本修正案修订 Paper I / Paper 0 边界；它本身不提升任何论断。提升
遵循写作计划的集成审计矩阵。
