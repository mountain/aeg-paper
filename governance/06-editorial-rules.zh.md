# AEG 论文系列编辑规则

**文件：** `governance/06-editorial-rules.md`
**状态：** 权威
**版本：** 1.0
**日期：** 2026-08-06
**依赖：**

* `AGENTS.md`
* `governance/00-authoritative-scope.md`
* `governance/01-paper-series-architecture.md`
* `governance/02-paper-I-outline.md`
* `governance/03-theorem-dependency-graph.md`
* `governance/04-current-to-target-map.md`
* `governance/05-mathematical-status.md`

**适用于：** Papers I–IV、其附录与意图最终出版的活跃技术笔记。

---

## 1. 目的

本文档定义算术表达式几何论文系列的编辑与阐述标准。

其目的是：

* 跨论文保持术语与记号稳定；
* 确保数学状态在行文中可见；
* 防止探索性语言被误认为已证明数学；
* 执行一致定理、定义、方程、图与引用实践；
* 使论文独立可读同时保持连贯系列架构；
* 支持人类合作者与 Codex 的精确审查。

这些规则支配呈现。它们不覆盖数学范围或状态。

当编辑偏好与数学准确冲突时，数学准确优先。

---

# 第一部分. 一般行文原则

## 2. 出版语言

主论文用英文书写。

研究笔记可保持中文或双语，但任何迁移进论文的材料必须重写为出版质量数学英文。

英文应：

* 直接；
* 正式；
* 经济；
* 假设显式；
* 论断克制；
* 无宣传语言。

避免从中文直译产生不自然英文语法时。

---

## 3. 默认段落结构

数学段落通常应执行一个主要功能：

1. 定义对象；
2. 陈述论断；
3. 证明论断；
4. 解释结果；
5. 连接两节；
6. 划定范围。

不在一段结合定义、证明、推测与历史评论。

长段落含多个逻辑步时应拆分。

---

## 4. 论断优先阐述

引入实质结果时用顺序：

1. 动机；
2. 精确陈述；
3. 证明；
4. 解释；
5. 局限或下游使用。

读者知道陈述前不花数页动机定理。

不把定理解释得强于其形式结论。

---

## 5. 显示逻辑链

每节应清楚：

* 哪些对象已可用；
* 引入什么新对象或结果；
* 加什么假设；
* 什么下游结果依赖它。

用显式过渡句如：

> 前述余循环公式供 ACS 构造所用加权核。

或：

> 正则零定理显示孤立零需正则假设失败；这激励奇异 AES 定义。

避免模糊过渡如：

> 这自然导致许多有趣方向。

---

## 6. 避免修辞膨胀

不用宣传短语如：

* “revolutionary”；
* “groundbreaking”；
* “deeply profound”；
* “completely new geometry”；
* “unavoidable”；
* “obviously fundamental”；
* “the ultimate theory”；
* “a universal principle”；

除非陈述被数学定义与证明。

优选替代：

* “provides”；
* “suggests”；
* “gives a model of”；
* “defines”；
* “establishes under the stated hypotheses”；
* “raises the question whether”；
* “serves as a first example.”

---

## 7. 区分数学与解释

用显式标记。

### 对已证明数学内容

> Proposition 4.2 shows that …

### 对解释

> This may be interpreted as …

### 对结构提案

> We propose to regard …

### 对猜想

> We conjecture that …

### 对开放问题

> It remains open whether …

不无信号从一个语域移到另一个。

---

## 8. 避免拟人因果语言

优选：

> The multiplicative steps rescale earlier additive contributions.

避免：

> Each additive step remembers the future.

隐喻语言可在精确公式建立后少量出现。

---

# 第二部分. 状态敏感写作

## 9. 已证明结果

状态 `PROVED` 或 `PROVED WITH STATED HYPOTHESES` 的结果可陈述性写。

例：

> The horizontal fields satisfy
> [
> [D_u,D_v]=\mu\lambda\partial_a.
> ]

陈述必须在定理或清楚活跃常设假设中含每个所需假设。

---

## 10. 标准推论

状态 `STANDARD CONSEQUENCE REQUIRING AN IN-PAPER PROOF` 的结果在证明或精确引用出现前不得描述为
已确立。

集成前，用：

> Under the regularity assumptions, the regular-value theorem is expected to imply that (Z(a)) is a smooth submanifold.

证明集成后，允许陈述措辞。

---

## 11. 部分证明论断

在意图推广前陈述已证明范围。

优选形式：

> We prove the statement for the basic model (\mathfrak E_0). Its extension to general regular AES remains open.

避免：

> The theorem holds generally, as illustrated by (\mathfrak E_0).

---

## 12. 结构提案

结构提案必须用如下语言引入：

* “We define provisionally …”
* “We propose the following framework …”
* “The following construction is intended as …”
* “This section formulates, but does not yet prove, …”

提案不得包于 `theorem`、`proposition` 或 `corollary` 环境。

视适用用 `definition`、`construction`、`program` 或 `remark` 环境。

---

## 13. 猜想

猜想必须数学精确。

它必须陈述：

* 环境范畴；
* 所有假设；
* 精确结论；
* 已知特殊情形；
* 已知阻碍，若有。

不把广泛抱负标为猜想。

无确定答案提议时用 `openproblem` 环境。

---

## 14. 开放问题

开放问题应短且可能处可证伪。

优选形式：

> **Open Problem.** Classify the regular affine AES models that are homogeneous under a transitive two-dimensional Lie-group action.

避免模糊抱负清单如：

> Develop the whole theory and understand all its applications.

---

## 15. 无支持断言

标 `UNSUPPORTED AND EXCLUDED` 的断言不得出现于活跃论文行文，除以下形式之一：

* 解释为何表述被弃的历史注；
* 显式警告；
* 答案不预设的问题。

例：

> Noncommutativity alone does not imply negative curvature; any such relation must be established for a specified metric model.

---

# 第三部分. 术语

## 16. 规范基础术语

一致用以下术语。

### `arithmetic expression tree`

内部节点是算术运算的二叉语法树。

### `sequential tree`

内部节点依赖偏序是链的有限二叉表达式树。

### `marked spinal history`

带标记累加器的顺序树，表示为单孔语境年代词。

### `chirality word`

操作数槽序列：

[
\varepsilon_1\cdots\varepsilon_n,
\qquad
\varepsilon_i\in{1,2}.
]

### `ordinary arithmetic evaluation`

受普通域限制（含除零）的求值。

### `projective evaluation`

作为 (\mathbb P^1(K)) 上分式线性变换的求值。

### `affine sector`

固定所选无穷远点的子群。

### `assignment function`

算术表达式空间上的标量场 (a)。

### `regular AES`

满足所选光滑正则定义的算术表达式空间。

### `singular AES`

带声明奇异轨迹且补上正则 AES 结构的空间。

### `ACS`

记录加法与对数乘法 charge 的累积交换空间。

### `relative torsion`

比较两相容历史的缺陷。

### `horizontal covariant differential`

记为 (\delta_H) 的算子，除非后范围决定改记号。

---

## 17. 废弃术语

除非讨论历史用法，避免以下。

### `threadlike expression`

此术语作主要定义被废弃因与含糊子定向关联。

可在规范定义后括注用：

> marked spinal histories, called threadlike expressions in earlier drafts.

### `left-expanded` 与 `right-expanded`

除非精确树定向图与操作数槽指定，避免。

用：

* slot-(1) history；
* slot-(2) history；
* pure-chirality history；
* mixed-chirality history。

### `arithmetic holomorphicity is forced by contact geometry`

不用。

优选：

> After choosing compatible horizontal metric and complex data, one may define an arithmetic Cauchy–Riemann operator.

### `tube`

不对每个参数化零集用。

用层级：

1. 总零集；
2. 正则零曲面；
3. 局部平凡零族；
4. 零管；
5. 穿线管。

---

## 18. 镜像、反演与逆

如下精确用术语。

* **mirror:** 操作数槽交换；
* **temporal reversal:** 语境词反演；
* **path inverse:** 反演连同每个可逆语境求逆。

歧义可能时不无限定用“reverse”。

---

## 19. 正则与奇异零

用：

[
Z(a)=a^{-1}(0),
]

[
Z_{\mathrm{reg}}(a),
\qquad
Z_{\mathrm{sing}}(a).
]

正则零定理带 (\mu\neq0) 适用时不把孤立零称“正则”。

仅指定相关机制后用：

* 奇异零；
* 删除零；
* 边界零；
* 退化零。

---

# 第四部分. 记号

## 20. 一般记号政策

每个符号在一篇论文内必须有一个规范角色。

一章内不给同符号赋两个概念不同含义。

继承记号可能歧义时，重命名次要量而非依赖语境。

---

## 21. 域与空间

用：

[
K
]

表一般域。

用：

[
\mathbb R,\quad \mathbb C,\quad \mathbb F_q
]

表标准特化。

用：

[
\mathbb P^1(K)
]

表射影线。

用：

[
\operatorname{Aff}(1,K),
\qquad
PGL_2(K)
]

带一致罗马算子排版。

一篇论文内不在 `\PGL`、`\operatorname{PGL}` 与普通斜体 (PGL) 间交替。

---

## 22. 历史与求值

用：

[
\gamma,\delta
]

表历史。

用：

[
\rho(\gamma)
]

表射影或算子求值。

用：

[
\nu_x(\gamma)
]

表初值 (x) 普通端点求值。

用：

[
C_\gamma
]

表 ACS 路径。

用：

[
\Sigma_{\gamma,\delta}
]

表相容 ACS 路径间填充。

---

## 23. 仿射数据

对：

[
x\mapsto \Phi x+\xi,
]

用：

* (\Phi)：累积尺度；
* (\xi)：目标框架平移；
* (\widehat\xi=\Phi^{-1}\xi)：源归一化平移。

(a) 已是赋值函数时不把 (a) 用仿射平移。

---

## 24. 流数据

用：

* (u)：加法坐标；
* (v)：乘法坐标；
* (a)：赋值；
* (\mu)：加法强度；
* (\lambda)：对数乘法强度；
* (\theta)：方向角；
* (s)：曲线参数或弧长。

避免同时把 (\lambda) 用于：

* 固定流强度；
* 累积对数尺度；
* 特征值。

若同章需累积尺度，用另一符号如：

[
M
\quad\text{or}\quad
\Lambda.
]

---

## 25. 流形记号

当字母 (M) 也用于乘法 charge 时，优选：

[
\mathcal M
]

表流形。

用：

[
g
]

表 Riemannian 度量。

用：

[
\mathcal H
]

表水平分布，仅当不与上半平面混淆时。

对上半平面，优选：

[
\mathbb H
\quad\text{or}\quad
\mathbb H^2.
]

若两者同章出现，保留：

[
\mathcal D=\ker\alpha
]

表接触分布。

---

## 26. ACS 记号

用：

[
(A,M)
]

表加法与乘法 charge。

用一个规范加权形式。

例如：

[
\eta=e^{-M},dA
]

或其末端归一化变体。

一旦选定，不无显式坐标或定向转换在 (e^M dA) 与 (e^{-M}dA) 间切换。

---

## 27. 接触记号

用：

[
\alpha
======

da-(\mu,du+\lambda a,dv).
]

用：

[
D_u,\quad D_v
]

表水平提升。

用：

[
\delta_H
]

表水平协变微分。

用：

[
\Delta_H
]

仅在其精确定义固定后。

---

## 28. 模型记号

模型名审计完成后用：

[
\mathfrak E_0
]

表基本正则双曲模型。

用：

[
\mathfrak E_1
]

仅在其奇异定义固定后。

不单独基于可见零线数赋 (E_k) 标签，除非该索引约定已被正式采纳。

---

# 第五部分. 定义

## 29. 定义风格

定义应：

* 识别环境范畴；
* 陈述所有数据；
* 陈述所有所需条件；
* 避免嵌入未证明推论；
* 避免形式句内动机。

优选：

> **Definition 3.1.** A marked spinal history over (K) consists of an initial value (x_0) and a finite sequence ((\omega_i,c_i,\varepsilon_i)), where …

然后单独段落跟解释。

---

## 30. 避免循环定义

不定义：

* 算术流定义前用“arithmetic flow”定义 AES；
* 声明正则轨迹前用“singular”定义奇异 AES；
* 相关定理前用拓扑不变定义管；
* 复杂度定义前用复杂度损失定义凝聚。

---

## 31. 定义对示例

激励示例可先于定义，但不得取代它。

定义后，回到示例并验证它满足每个条件。

---

## 32. 暂定定义

暂定定义必须在笔记标为如此。

出版论文中，仅稳定定义应无限定出现。

定义仍在发展时，用：

> For the purposes of this paper, we use the following restricted definition.

---

# 第六部分. 定理环境

## 33. 标准环境

用一致环境集：

```latex
\newtheorem{theorem}{Theorem}[section]
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{corollary}[theorem]{Corollary}

\theoremstyle{definition}
\newtheorem{definition}[theorem]{Definition}
\newtheorem{construction}[theorem]{Construction}
\newtheorem{example}[theorem]{Example}
\newtheorem{conjecture}[theorem]{Conjecture}
\newtheorem{openproblem}[theorem]{Open Problem}

\theoremstyle{remark}
\newtheorem{remark}[theorem]{Remark}
\newtheorem{warning}[theorem]{Warning}
```

精确编号方案可变，但所有定理类环境应共享连贯计数器。

---

## 34. 环境选择

用：

* `theorem` 对带显著推论的中心结果；
* `proposition` 对实质但局部或计算性结果；
* `lemma` 对支持结果；
* `corollary` 对立即推论；
* `definition` 对稳定对象；
* `construction` 对定义过程或模型；
* `example` 对显式实例；
* `conjecture` 对精确未证明断言；
* `openproblem` 对问题；
* `remark` 对解释；
* `warning` 对范围或域危险。

不把提案放定理环境。

---

## 35. 定理标题

用简明语义定理标题。

优选：

* Sequential-tree classification
* Bilateral generation theorem
* Regular zero-locus theorem
* Weighted torsion–Stokes theorem

避免标题如：

* Main theorem
* Revised theorem
* Improved final theorem
* Fundamental groundbreaking identity

---

## 36. 定理标签

用语义标签：

```latex
\label{thm:sequential-tree-classification}
\label{prop:target-affine-cocycle}
\label{def:singular-aes}
```

避免：

```latex
\label{eq:final_revised_enhanced_acs_AM_lc}
```

标签必须描述数学内容，非编辑历史。

---

## 37. 常设假设

常设假设可在节首声明。

例：

> Throughout this section, (K) is a field and all affine multipliers are nonzero.

不依赖数章前声明的假设当它们对定理必需时。

在定理陈述中重复关键假设。

---

# 第七部分. 证明风格

## 38. 证明完备性

每个证明应暴露关键数学步。

不以以下取代本质推理：

* “it is easy to see”；
* “obviously”；
* “clearly”；
* “by standard arguments”；

除非有精确引用或立即可恢复计算。

---

## 39. 证明分解

长证明用短内部段落：

* `Existence.`
* `Uniqueness.`
* `Injectivity.`
* `Surjectivity.`
* `Regularity.`
* `Compatibility with composition.`

连续行文更清时不用过度条目化。

---

## 40. 计算证明

计算中：

1. 陈述被计算公式；
2. 显示非平凡中间步；
3. 识别每个假设用在哪里；
4. 陈述所得结论。

例：

[
|\nabla a|_g^2
==============

# g^{xx}a_x^2+g^{yy}a_y^2

\mu^2+\lambda^2a^2.
]

归一化非标准时不省略逆度量。

---

## 41. 约定敏感证明

任何涉及：

* 群复合；
* 路径顺序；
* 矩阵乘法；
* 定向；
* Stokes 定理；
* 交换子；

的证明必须显式引用采纳约定。

至少一个显式示例应用来验证符号。

---

## 42. 局部对全局结论

证明末尾，陈述实际范围。

优选：

> Thus (Z(a)) is a smooth one-dimensional submanifold near every interior zero.

不结论：

> Hence the zero set is globally a finite collection of circles.

除非紧性与全局拓扑已确立。

---

## 43. 标准定理调用

调用标准定理时，陈述：

* 定理；
* 应用于的映射或对象；
* 已验证假设；
* 结论。

例：

> Since (d_pa_t\neq0) on (\mathcal Z), the value (0) is regular for (A(p,t)=a_t(p)). The regular-value theorem therefore implies that (\mathcal Z) is a codimension-one submanifold.

---

# 第八部分. 方程

## 44. 显示方程政策

方程在以下情形显示：

* 后引用；
* 结构重要；
* 太长不适合行内行文；
* 推导中心。

不为视觉强调显示平凡方程。

---

## 45. 方程编号

仅后引用时编号方程。

用语义标签：

```latex
\label{eq:affine-flow}
\label{eq:target-cocycle}
\label{eq:contact-form}
```

除非外部格式要求，不手动给方程暂定号如 `\tag{7}`。

让 LaTeX 管理编号。

---

## 46. 精确对渐近公式

显式标记渐近公式：

[
\Delta\tau
==========

\mu\lambda,du,dv
+
O(|(du,dv)|^3).
]

不把渐近展开重写为精确微分形式恒等式。

按其精确含义用：

* `=`；
* `\sim`；
* `O(\cdot)`；
* `o(\cdot)`。

---

## 47. 微分形式定向

对楔积与 Stokes 公式：

* 固定定向；
* 陈述边界定向；
* 避免静默切换 (dM\wedge dA) 与 (dA\wedge dM)；
* 用初级矩形验证符号。

---

## 48. 范记号

度量重要时用：

[
|\nabla a|_g
]

除非度量在直接语境无歧义，避免：

[
|\nabla a|
]

---

## 49. 算子记号

陈述算子作用：

* 于标量场；
* 于微分形式；
* 局部；
* 于紧支光滑函数；
* 于 Hilbert 空间域。

形式微分恒等式不得无域呈现为算子论结果。

---

# 第九部分. 示例

## 50. 示例功能

每个示例应有一个声明目的：

* 演示定义；
* 分离两个概念；
* 验证符号；
* 显示假设必要性；
* 说明定理；
* 展示开放现象。

首句应陈述该目的。

---

## 51. 示例非证明

不从以下推断一般断言：

* 一个绘制零集；
* 一个有限计算；
* 一个符号模型；
* 一个纽结图；
* 一个有限域计数。

用短语如：

> This example shows that the phenomenon can occur.

非：

> This proves that the phenomenon is general.

---

## 52. 已算示例

已算示例应包括：

1. 输入历史或模型；
2. 算子求值；
3. 几何表示；
4. 最终不变量或结论；
5. 与被说明定理的关系。

---

## 53. 反例与警告

用显式反例防常见误读。

重要示例包括：

* 同端点不同算子；
* 同算子不同历史；
* 镜像不等于反演；
* 射影定义值但普通未定义中间步；
* 奇异致孤立零；
* 无真全局管行为的光滑总零集。

---

# 第十部分. 图

## 54. 图数学角色

图必须服务以下之一：

* 定义或澄清构造；
* 显示几何模型；
* 说明定理；
* 比较不同概念；
* 可视化参数族。

不为视觉冲击含图。

---

## 55. 图注

图注必须数学自包含。

它应陈述：

* 显示什么对象；
* 颜色或线型含义；
* 哪个结论是说明而非证明；
* 所用任何参数值。

避免图注如：

> A beautiful arithmetic universe.

优选：

> The two ACS paths have equal total charge and bound an oriented (2)-chain. The weighted area represents their relative affine torsion.

---

## 56. 图引用

行文中在每图出现前或紧接后引入。

不写：

> The result is obvious from Figure 6.

用：

> Figure 6 illustrates the geometry; the proof is given in Proposition 7.3.

---

## 57. 图溯源

每图应有：

* 源文件；
* 适用处生成脚本；
* 参数记录；
* 目标论文；
* 外部来源时许可或作者信息。

手工编辑图应保留可编辑源格式。

---

## 58. 坐标一致性

图必须用与文本相同的：

* 轴定向；
* 符号约定；
* 颜色图例；
* 模型编号；
* 记号。

若历史图用被取代记号，重绘而非依赖图注修正。

---

# 第十一部分. 表

## 59. 表适当使用

表用于：

* 语境到矩阵对应；
* 状态登记；
* 记号比较；
* 假设与结论；
* 迁移摘要。

不用表于长证明或密集概念阐述。

---

## 60. 表注与标题

列标题必须精确描述数学角色。

优选：

| Context | Ordinary map | Projective matrix | Domain condition |

避免含义歧义时：

| Type | Formula | Notes |

---

# 第十二部分. 引用

## 61. 引用目的

为以下引用来源：

* 标准定理；
* 历史归属；
* 已建立术语；
* 与已知结构比较；
* 外部计算模型。

不引用一般教科书作新 AEG 定理正确的证据。

---

## 62. 主要与标准来源

优选：

* 命名结果用原始论文；
* 背景用标准专著；
* 历史定位用权威综述。

对高度标准事实，一个合适引用足够。

---

## 63. 历史断言

避免广泛历史断言如：

> No previous theory has considered arithmetic geometrically.

除非文献综述合理化该陈述。

优选：

> The present construction differs from the cited approaches in treating ordered arithmetic evaluation histories as the primary objects.

---

## 64. 新颖性断言

用克制语言。

优选：

> We are not aware of a prior formulation of this particular history-to-contact construction.

更强新颖性断言需专门文献审计。

---

## 65. 引用放置

把引用放在被支持陈述紧后。

避免在长段落末收集若干无关引用。

---

# 第十三部分. 摘要

## 66. 摘要内容

摘要应含：

1. 问题；
2. 主要对象；
3. 中心代数定位；
4. 主要几何构造；
5. 主要定理级结论；
6. 论文范围边界。

它不应含：

* 详细文献讨论；
* 局部可理解之外的未定义记号；
* 未来论文承诺；
* 猜想应用；
* 论文未证明的复杂度或纽结断言。

---

## 67. 摘要状态纪律

仅含状态：

* `PROVED`；
* `PROVED WITH STATED HYPOTHESES`；
* 证明集成后的 `STANDARD CONSEQUENCE`。

极小多重零示例除非通过验证清单，不提及。

---

## 68. 摘要长度

目标约 180–280 词。

摘要不应试图总结每章。

---

# 第十四部分. 引言

## 69. 引言架构

推荐顺序：

1. 问题与视角；
2. 过程到结果层级；
3. 顺序历史限制；
4. 双边射影定位；
5. 仿射几何计划；
6. 主要结果；
7. 范围排除；
8. 节指南。

---

## 70. 主要结果清单

引言可含一个主要结果短编号清单。

每项必须对应正文实际定理或命题。

不列：

* 广泛研究抱负；
* 后续论文计划；
* 推测应用。

---

## 71. 历史定位

保持历史定位简明且数学相关。

避免把引言变成以下综述：

* 形式语言理论；
* 全部双曲几何；
* 全部接触几何；
* 计算哲学。

---

# 第十五部分. 节开与节闭

## 72. 节开

每个主节应以两短段开始：

1. 节处理什么问题；
2. 它建立什么与假定什么。

例：

> The previous section identifies the affine operator sector. We now derive the two natural translation cocycles carried by an affine history. These formulas will later determine the weight appearing in the ACS integral.

---

## 73. 节闭

每个主节应以以下结束：

* 现可用结果；
* 下一依赖。

例：

> We have therefore obtained the affine flow independently of any chosen surface model. The next section constructs a homogeneous metric realization of this flow.

避免每个小节重复摘要。

---

## 74. 跨论文过渡

Paper I 末尾用精确接口。

优选：

> Paper II adds compatible horizontal metric and complex data and studies the resulting analytic operators.

避免：

> In the next paper we will solve the complete analytic theory.

---

# 第十六部分. 附录

## 75. 附录角色

附录可含：

* 约定细节；
* 长坐标计算；
* 次要示例；
* 符号检查；
* 对主线太技术的证明。

附录不得含先前未陈述即用的基础定义。

---

## 76. 附录引用

正文应陈述为何附录相关。

例：

> The full coordinate verification of the Laplace eigenvalue is given in Appendix C.

---

## 77. 无隐藏第二篇论文

材料发展独立理论时应移到 Paper II–IV 而非留于超大 Paper I 附录。

---

# 第十七部分. 逐论文编辑规则

## 78. Paper I

Paper I 应强调：

* 定义；
* 精确代数结构；
* 约定控制；
* 有限对无穷小区分；
* 奠基范围。

避免扩展解析、纽结论或复杂度讨论。

---

## 79. Paper II

Paper II 必须区分：

* 形式算子恒等式；
* PDE 结果；
* 泛函分析；
* 全局边界理论。

术语 `basis` 需声明环境向量空间或函数空间。

术语 `harmonic` 需指定算子。

---

## 80. Paper III

Paper III 必须区分：

* 正则零集；
* 奇异芽；
* 总零集；
* 管；
* 辫；
* 纽结。

每个视觉拓扑断言需数学不变量或分类论证。

---

## 81. Paper IV

Paper IV 用词 `complexity` 前必须指定成本模型。

区分：

* 词增长；
* 表示大小；
* 搜索复杂度；
* 运行时间；
* 内存；
* 下界。

术语 `condensation` 必须伴显式映射或商。

---

# 第十八部分. 格式与 LaTeX

## 82. 包纪律

移除重复包导入。

仅需时加包。

避免不可预测重定义定理、图注或超链行为的包组合。

---

## 83. 宏

为频繁用算子与空间创建宏。

例：

```latex
\newcommand{\Aff}{\operatorname{Aff}}
\newcommand{\PGL}{\operatorname{PGL}}
\newcommand{\Hist}{\operatorname{Hist}}
\newcommand{\AES}{\mathrm{AES}}
```

不为一次性表达式创建宏。

宏名必须语义且稳定。

---

## 84. 排版

用：

* `\operatorname{}` 对命名算子；
* `\mathbb{}` 对标准数系；
* `\mathfrak{}` 对命名表达式空间；
* `\mathcal{}` 对几何结构与族；
* 一致正体微分 (d)，若采纳宏。

一篇论文内不混风格约定。

---

## 85. 引文

引文环境仅用于：

* 中心引导问题；
* 短引用陈述。

不用引文格式作视觉装饰。

---

## 86. 列表

项真平行时用列表。

避免证明与概念讨论中长嵌套条目化。

列表编码逻辑替代时，编号项供引用。

---

## 87. 脚注

少量用脚注。

不把本质数学假设放脚注。

---

# 第十九部分. 术语审计清单

## 88. 定稿前强制搜索词

搜索完整 Paper I 源：

```text id="0qpg4h"
threadlike
left-expanded
right-expanded
reverse
canonical
unique
natural
forced
obvious
clearly
torsion
curvature
holomorphic
tube
knot
complexity
hyperbolic
projective
singular
```

每个出现必须检查：

* 当前规范含义；
* 无理由强度；
* 歧义；
* 范围漂移。

---

## 89. 模型名审计

搜索：

```text id="ap59kk"
\mathfrak{E}_0
\mathfrak{E}_1
E_0
E_1
zeroth kind
first kind
```

全局编辑前创建一个权威对应表。

---

## 90. 符号审计

搜索：

```text id="8uxt3v"
u
\nu
M
\mathcal M
\lambda
\Lambda
a
A
\delta
\delta_H
```

检查视觉与语义碰撞。

---

# 第二十部分. 编辑审查协议

## 91. 第一遍审查

审查：

* 结构；
* 定理顺序；
* 范围；
* 重复阐述；
* 无支持断言。

第一遍不在数学不稳定内容周围花时间润句。

---

## 92. 第二遍审查

审查：

* 记号；
* 假设；
* 符号；
* 复合顺序；
* 局部/全局区分；
* 状态标签。

---

## 93. 第三遍审查

审查：

* 行文；
* 段落节奏；
* 过渡；
* 图注；
* 引用；
* 排版一致。

---

## 94. 最终摘要-结论审计

对照正文比较每个摘要与结论句。

对每个断言，识别：

* 定理号；
* 命题号；
* 定义；
* 显式标签解释。

删除或削弱任何缺支持句。

---

# 第二十一部分. Codex 特定编辑约束

## 95. 无静默加强

Codex 不得把：

> may suggest

替换为：

> proves

或把：

> appears to

替换为：

> is

除非状态文件授权变更。

---

## 96. 无审计不全局术语替换

Codex 不得盲替换：

* `threadlike`；
* `left`；
* `right`；
* `E_0`；
* `E_1`；
* `torsion`；
* `delta`。

每个替换需语义语境。

---

## 97. 保留数学注释

移动证明或定理时，保留解释注释：

* 缺失假设；
* 替代约定；
* 未解决符号；
* 意图后续论文目的地。

不解决或迁移前不删 TODO 标记。

---

## 98. 编辑任务后所需报告

每个编辑任务报告必须陈述：

1. 改变术语；
2. 改变定理环境；
3. 改变标签；
4. 改变记号；
5. 削弱或加强断言；
6. 移动材料；
7. 未解决歧义；
8. 构建结果。

---

# 第二十二部分. 验收规则

## 99. 一章编辑验收条件

一章只有以下条件才编辑可接受：

* 每个对象使用前定义；
* 每个定理有显式假设；
* 每个证明支持精确结论；
* 数学状态匹配 `05-mathematical-status.md`；
* 术语匹配本文件；
* 记号匹配系列架构；
* 图与图注用当前约定；
* 后续论文材料约化为前向引用；
* 所有引用与引用解析；
* 无已知被拒表述残留。

---

## 100. 系列级编辑原则

AEG 系列应听起来雄心勃勃因其对象与结果精确，非因其行文铺张。

支配编辑规则是：

[
\boxed{
\text{state less, define more, prove exactly, and mark the frontier}.
}
]

成功阐述使四个边界可见：

[
\text{history}\neq\text{value},
]

[
\text{affine}\neq\text{projective},
]

[
\text{regular}\neq\text{singular},
]

[
\text{proved}\neq\text{proposed}.
]
