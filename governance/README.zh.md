# Arithmetic Expression Geometry（算术表达式几何）

算术表达式几何（AEG）通过其**有序求值历史**来研究算术表达式，而不是把一个表达式视为被
其最终数值所穷尽。

中心层级是：

[
\text{expression tree}
\longrightarrow
\text{marked history}
\longrightarrow
\text{operator}
\longrightarrow
\text{geometric or quotient state}
\longrightarrow
\text{endpoint value}.
]

每支箭头遗忘信息。AEG 研究最终求值之前各层所承载的代数、几何、分析、拓扑与计算结构。

---

## 仓库状态

> **受控重组已产出 Papers I–IV 的四份规范数学审查手稿，以及作为几何基础的 Paper 0。
> 它们都仍是编辑与出版草稿。**
>
> **此后又开设了第五个槽位，Paper V。** 其范围固定于
> [`governance/00c-paper-V-triadic-aperture-scope.md`](00c-paper-V-triadic-aperture-scope.md)；
> 其手稿是 `paper-5/aeg-paper-5.tex`。它是草稿，不计入四手稿重组数。
>
> **此后又开设了第六个槽位，Paper VI。** 其范围固定于
> [`governance/00e-paper-VI-process-geometry-scope.md`](00e-paper-VI-process-geometry-scope.md)；
> 其手稿是 `paper-6/aeg-paper-6.tex`，其论断登记是
> [`governance/05c-paper-VI-status-register.md`](05c-paper-VI-status-register.md)。
> 它是草稿。

当前源包含在研究计划不同阶段发展的材料。有些笔记是已证明的数学；其他是探索性构造、
结构性提案、猜想、被取代的表述或开放问题。

不要把每个文件都视为同等权威。

支配性规范是：

* [`AGENTS.md`](../AGENTS.md)
* [`governance/00-authoritative-scope.md`](00-authoritative-scope.md)
* [`governance/00b-paper-0-geometric-foundation-amendment.md`](00b-paper-0-geometric-foundation-amendment.md)
* [`governance/00c-paper-V-triadic-aperture-scope.md`](00c-paper-V-triadic-aperture-scope.md)
* [`governance/00e-paper-VI-process-geometry-scope.md`](00e-paper-VI-process-geometry-scope.md)
* [`governance/01-paper-series-architecture.md`](01-paper-series-architecture.md)
* [`governance/02-paper-I-outline.md`](02-paper-I-outline.md)
* [`governance/03-theorem-dependency-graph.md`](03-theorem-dependency-graph.md)
* [`governance/04-current-to-target-map.md`](04-current-to-target-map.md)
* [`governance/05-mathematical-status.md`](05-mathematical-status.md)
* [`governance/05c-paper-VI-status-register.md`](05c-paper-VI-status-register.md)
* [`governance/06-editorial-rules.md`](06-editorial-rules.md)
* [`governance/07-acceptance-checklist.md`](07-acceptance-checklist.md)
* [`governance/08-open-questions.md`](08-open-questions.md)

当仓库来源冲突时，这些文档决定当前范围、术语、论断状态与迁移政策。

已完成的数学审查集成记录于：

* [`paper-I-closure-report.md`](paper-I-closure-report.md)
* [`paper-II-closure-report.md`](paper-II-closure-report.md)
* [`paper-III-closure-report.md`](paper-III-closure-report.md)
* [`paper-IV-closure-report.md`](paper-IV-closure-report.md)

Paper III 的修正历史溯源与定理决定记录于
[`paper-III-source-audit.md`](paper-III-source-audit.md) 与
[`decisions-paper-III.md`](decisions-paper-III.md)。
Paper IV 的相应记录是
[`paper-IV-source-audit.md`](paper-IV-source-audit.md)、
[`decisions-paper-IV.md`](decisions-paper-IV.md) 与
[`paper-IV-red-team-report.md`](paper-IV-red-team-report.md)。

闭包后跨 Papers I–III 的算术–自守集成记录于
[`discussions/arithmetic-automorphic-zero-networks.md`](discussions/arithmetic-automorphic-zero-networks.md)。
其已证明分量只通过权威范围、依赖、状态与逐论文决定记录提升；一般历史到除子的函子仍是
开放问题。

研究笔记的清单与就绪度分级，连同冲突与修正台账，记录于
[`notes-reserve-audit.md`](notes-reserve-audit.md)。其新的开放项登记为 OQ-078–OQ-080，见
[`08-open-questions.md`](08-open-questions.md)。

---

# AEG 论文系列

该计划组织为七篇论文，编号 0 与 I–VI。

| 论文 | 当前手稿标题 | 首要问题 |
| ----- | --- | --- |
| 0 | **Arithmetic Expression Geometry 0 — Arithmetic Expression Spaces** | 算术表达式如何成为几何，其运算顺序的代价是什么？ |
| I | **Arithmetic Expression Geometry I: Foundations** | 顺序算术历史如何获得射影结构，其零几何有多刚性？ |
| II | **Arithmetic Expression Geometry II: Hyperbolic Real Function Theory** | 正则 AEG 空间上存在哪些解析与函数论结构？ |
| III | **Arithmetic Expression Geometry III: Singular Zero Geometry and Tubes** | 多重零、奇点、参数族与管拓扑如何产生？ |
| IV | **Arithmetic Expression Geometry IV: Projective Condensation and Computational Complexity** | 商与凝聚下损失了什么信息，它如何与表示和计算相关？ |

依赖架构是：

```text
Paper 0 ──→ Paper I ──→ Paper II
                    ──→ Paper III
                    ──→ Paper IV
Paper II ──→ Paper III  [bounded holomorphic-pullback interface]
Paper IV ──→ Paper V
Paper 0, Paper I, Paper V ──→ Paper VI
```

Paper 0 是几何基础：它拥有算术表达式空间、作为运动的四则运算、双曲与穿孔模型、ripple
几何、仿射余循环、带撕裂的累积交换空间，以及接触结构。其范围由
`00b-paper-0-geometric-foundation-amendment.md` 固定，其论断状态登记于
`05b-paper-0-status-register.md`；该修正案把那些对象从 Paper I 重新分配，Paper I 现在拥有
顺序历史、射影、Hecke 与零层。

Paper II 现在提供 Paper III 所使用的已声明平面/柱面拉回接口。依赖是单向且有界的：
Paper II 不证明任何奇异、管或纽结结论，故基础架构保持无环。

---

# Paper I: Foundations

## 暂定标题

**Arithmetic Expression Geometry I: Foundations**

推荐副标题：

**Sequential Histories, Affine Flow, Torsion, and Contact Geometry**

## 中心论题

Paper I 发展以下链条：

[
\boxed{
\text{sequential syntax}
\longrightarrow
\text{projective semantics}
\supset
\text{affine sector}
\longrightarrow
\text{affine flow}
\longrightarrow
\text{expression geometry}
\longrightarrow
\text{torsion and contact curvature}.
}
]

预期的奠基性结果是：

> 顺序算术表达式承认基于标记脊柱树的历史敏感形式体系。非退化双边算术历史射影地作用于
> (\mathbb P^1(K)) 并生成 (PGL_2(K))，而本论文发展的连续 AEG 理论是稳定无穷远点的仿射
> 或 Borel 扇区。该仿射扇区承载自然余循环、一个无穷小流、一个基本双曲实现、全局 torsion
> 公式、一个正则零集理论，以及一个其曲率记录局部序缺陷的接触联络。

---

## 所需奠基性结果

Paper I 旨在建立以下各项的严格版本：

1. 顺序树分类；
2. 标记脊柱历史与手性词；
3. 镜像、时间反演与路径逆的区分；
4. 双边单孔算术语境的射影求值；
5. (PGL_2(K)) 的生成；
6. 仿射/Borel 扇区的识别；
7. 目标框架与源归一化仿射余循环；
8. 连续仿射流方程；
9. 基本双曲模型 (\mathfrak E_0)；
10. 正则零轨迹定理；
11. 奇异 AES 的奠基性定义；
12. ACS 中的广义双历史 torsion；
13. 接触曲率与水平微分恒等式。

---

## Paper I 章节计划

```text
1. Introduction
2. Sequential Arithmetic Histories
3. Projective Semantics and the Affine Sector
4. Affine Cocycles and Relative Defects
5. Continuous Arithmetic Flow
6. The Basic Hyperbolic Expression Space
7. Zero Loci and Singular Expression Spaces
8. Global Torsion and the Accumulative Commutative Space
9. Contact Connection and Horizontal Curvature
10. Conclusions and Research Interfaces
```

推荐附录：

```text
Appendix A. Composition and action conventions
Appendix B. Affine-cocycle calculations
Appendix C. Hyperbolic-model calculations
Appendix D. ACS and contact calculations
Appendix E. Equality and neutrality examples
```

---

## Paper I 范围边界

Paper I 为后续论文提供共同基础。它**不**作为主要理论发展：

* 完整双赋值与秩一投影子理论；
* 完整 (G/H) 与 (G/B_\pm) 商塔；
* 射影凝聚语义；
* 完整算术全纯函数理论；
* Poisson 核、Green 函数或边值分析；
* 一般 (E_k) 或 (E_{\log}) 分类；
* 奇异管分岔理论；
* 辫、纽结或 Markov 不变量；
* 一般计算复杂度推论。

这些属于 Papers II–IV。

---

# 核心数学架构

## 顺序历史

一棵二叉表达式树当其内部节点依赖偏序有唯一合法求值顺序时称为顺序的。

目标分类定理是：

[
\text{unique linear extension}
\iff
\text{dependency poset is a chain}
\iff
\text{internal vertices form one spine}.
]

在标记演化的累加器后，顺序树变成单孔语境的历史：

[
C_{\omega,c}^{(1)}[z]=\omega(z,c),
\qquad
C_{\omega,c}^{(2)}[z]=\omega(c,z).
]

操作数槽位序列形成**手性词**。

重组用这种内在标记脊柱形式体系取代了此前对「threadlike expression」的含糊使用。

---

## 射影与仿射语义

非退化单孔算术语境通过分式线性变换作用于：

[
\mathbb P^1(K).
]

平移、非零缩放与反演生成：

[
PGL_2(K).
]

固定所选无穷远点的变换形成：

[
B_\infty
========

\operatorname{Stab}_{PGL_2(K)}(\infty)
\cong
\operatorname{Aff}(1,K).
]

连续实 AEG 理论使用正缩放：

[
z\mapsto e^\lambda z,
]

因此位于：

[
\operatorname{Aff}^{+}(1,\mathbb R).
]

一般无穷小射影流是 Riccati：

[
\dot z=\beta+\alpha z+\kappa z^2,
]

而 Paper I 发展仿射切片：

[
\kappa=0.
]

射影延拓与普通算术求值保持区分：射影映射可以穿过 (\infty)，而普通算术表达式可能因
除以零而未定义。

---

## 仿射余循环

对仿射步：

[
f_i(x)=s_ix+t_i,
\qquad
s_i\neq0,
]

其年代复合具有形式：

[
f_n\circ\cdots\circ f_1(x)
==========================

\Phi_nx+\xi_n,
]

其中：

[
\Phi_n=\prod_{i=1}^n s_i,
]

[
\xi_n
=====

\sum_{i=1}^n
t_i\prod_{j=i+1}^n s_j.
]

源归一化平移是：

[
\widehat\xi_n
=============

# \frac{\xi_n}{\Phi_n}

\sum_{i=1}^n
\frac{t_i}{\prod_{j=1}^i s_j}.
]

这两个余循环分别编码未来缩放与过去归一化。它们决定后来在 ACS 中使用的加权核。

---

## 连续仿射流

无穷小加与乘方向产生：

[
\frac{da}{ds}
=============

\mu\cos\theta+\lambda a\sin\theta.
]

在局部加与乘坐标中：

[
da=\mu,du+\lambda a,dv.
]

在指定相容度量框架后：

[
|\nabla a|_g^2
==============

\mu^2+\lambda^2a^2.
]

度量是几何结构的一部分；eikonal 方程不是无度量的。

---

## 基本双曲模型

主要正则模型是配备以下结构的上半平面：

[
g_{\mu,\lambda}
===============

\frac1{y^2}
\left(
\frac{dx^2}{\mu^2}
+
\frac{dy^2}{\lambda^2}
\right),
]

与赋值：

[
a(x,y)=-\frac{x}{y}.
]

直接计算给出：

[
|\nabla a|*{g*{\mu,\lambda}}^2
==============================

\mu^2+\lambda^2a^2.
]

重组寻求从仿射群与一个归一化不变度量推导该模型，而不是仅把它作为孤立 ansatz 呈现。

目前不声称该模型的唯一性定理。

---

## 正则与奇异零点

若光滑正则 AES 满足：

[
|\nabla a|^2
============

\mu^2+\lambda^2a^2
]

且：

[
\mu\neq0,
]

则在：

[
Z(a)=a^{-1}(0),
]

上有：

[
|\nabla a|=|\mu|>0.
]

故 (0) 是正则值，零集是光滑余一维子流形。

在二维正则 AES 上，正则零点形成不相交光滑曲线。特别是正则内部不能包含：

* 一个孤立零点；
* 零线交叉；
* 一个分支点；
* 一个诞生或死亡事件。

这种行为需要奇异性、退化、边界效应、properness 失败或语义范畴变化。

Paper I 引入初始的正则/奇异区分。完整多重零与管理论属于 Paper III。

---

## 全局 torsion 与 ACS

累积交换空间记录：

[
(A,M),
]

其中 (A) 是累积加法 charge，(M) 是累积对数乘法 charge。

它是仿射历史的交换影子，不是完整表达式空间。

首选直接路径求值公式是：

[
\nu_x(\gamma)
=============

e^{M_\gamma}
\left(
x+\int_{C_\gamma}e^{-M},dA
\right).
]

对相容历史 (\gamma,\delta)，相对 torsion 预期满足一个精确恒等式序列：

[
\text{affine cocycle difference}
================================

# \text{weighted boundary integral}

\text{weighted area}.
]

时间反演仍是重要的特殊情形，但不再是唯一的一般比较。

最终符号与定向约定仍是活跃数学审计的一部分。

---

## 接触联络与曲率

算术接触形式是：

[
\alpha
======

da-(\mu,du+\lambda a,dv).
]

其水平场是：

[
D_u=\partial_u+\mu\partial_a,
\qquad
D_v=\partial_v+\lambda a\partial_a.
]

它们满足：

[
[D_u,D_v]
=========

\mu\lambda\partial_a.
]

对标量场，水平协变微分是：

[
\delta_HF
=========

# dF-(\partial_aF)\alpha

(D_uF),du+(D_vF),dv.
]

其反对称二阶水平导数是：

[
\delta_H^2F
===========

\mu\lambda(\partial_aF),du\wedge dv.
]

这是一个对曲率敏感的水平算子，不是普通的幂零 de Rham 微分。

Paper II 添加水平度量、相容复结构、解析域与函数论。

---

# 当前数学状态

Papers I–IV 现在有规范数学审查手稿与逐论文闭包记录。这不使每个研究计划完整，也不授权
公开发布。手稿与治理登记保留的开放问题仍开放，探索性笔记不保留自动定理权威。

论断级状态（包括已证明、条件、提议、猜想与被排除陈述的假设与边界）由数学状态登记与
逐论文闭包与决定记录控制，而非由手稿的编辑 `draft` 标签控制。

完整状态登记是：

[`governance/05-mathematical-status.md`](05-mathematical-status.md)

未解决决定登记是：

[`governance/08-open-questions.md`](08-open-questions.md)

---

# 未确立的论断

仓库不得被读作证明以下任何无条件蕴含：

[
\text{noncommutativity}
\Rightarrow
\text{negative curvature},
]

[
\text{negative curvature}
\Rightarrow
\text{algorithmic hardness},
]

[
\text{multiple zero lines}
\Rightarrow
\text{knot invariant},
]

[
\text{contact structure}
\Rightarrow
\text{unique complex structure},
]

[
\text{projective continuation}
\Rightarrow
\text{ordinary arithmetic regularity}.
]

这些要么一般情形为假，要么需要附加假设，要么仍是开放研究计划。

---

# 仓库组织

## 当前活跃布局

仓库当前使用以下顶层组织：

```text
aeg-paper/
├── AGENTS.md
├── README.md
├── LICENSE
├── build.sh
├── Dockerfile
├── bibliography/
├── governance/
├── images/
│   └── sources/
├── notes/
├── paper-0/
├── paper-1/
├── paper-2/
├── paper-3/
├── paper-4/
├── paper-5/
└── archive/
```

从历史布局的已完成迁移记录于：

[`governance/04-current-to-target-map.md`](04-current-to-target-map.md)
与 [`migration-log.md`](migration-log.md)。

实质性研究材料被移动或归档，而非静默删除。

---

# 构建规范手稿

一个可用的 LaTeX 安装应至少提供：

* `pdflatex`；
* `bibtex`；
* 手稿导入的宏包。

用以下命令构建全部四份规范手稿：

```bash
./build.sh
```

要构建单份手稿，运行 `./build.sh 1`、`./build.sh 2`、`./build.sh 3` 或 `./build.sh 4`。
相应入口与产物是 `paper-k/aeg-paper-k.tex` 与 `paper-k/aeg-paper-k.pdf`。

## Docker 构建

```bash
docker build -t aeg-paper .
docker run --rm -v "$(pwd):/work" aeg-paper
```

只有在预期 PDF 实际产出时，构建才被视为成功。

必须审查的构建警告包括：

* 未定义引用；
* 缺失引用；
* 重复标签；
* 缺失图件；
* 归一化或编号不一致。

# 与 Codex 协作

不应要求 Codex 一次性重写整篇论文。

在执行重组任务前，阅读：

1. `AGENTS.md`；
2. 权威重组文件；
3. 数学状态登记；
4. 开放问题登记；
5. 任务特定的文件权限。

第一个 Codex 任务应只是审计。

预期输出：

```text
governance/audit-report.md
```

审计必须：

* 清点当前论文；
* 比较当前与目标结构；
* 识别定义与记号冲突；
* 按数学状态分类论断；
* 识别缺失证明；
* 推荐一串小提交的顺序；
* 运行当前构建作为基线；
* 保持论文正文不变。

每个后续任务必须陈述：

```text
1. Scope
2. Files allowed to change
3. Files forbidden to change
4. Theorem nodes in scope
5. Claim statuses allowed to change
6. Required validation
7. Expected output
```

Codex 任务若出现以下情形必须被拒绝：

* 发明缺失证明；
* 未经授权加强论断；
* 静默改变复合约定；
* 未经归档处置删除研究材料；
* 混淆镜像与反演；
* 把射影延拓当作普通求值；
* 把孤立奇异零点称为正则；
* 在无 properness 下把光滑总零集提升为全局平凡管；
* 未产出 PDF 即报告构建成功。

---

# 贡献与审查规则

这是一个研究数学仓库。贡献必须保留：

* 证明状态；
* 假设；
* 域限制；
* 记号所有权；
* 论文边界；
* 来源溯源。

在修改活跃论文源之前，阅读：

[`AGENTS.md`](../AGENTS.md)

支配性编辑原则是：

[
\boxed{
\text{state less, define more, prove exactly, and mark the frontier}.
}
]

必须保持可见的四个区分是：

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

---

# 验收与发布

Paper I 经过五个验收层推进：

1. 仓库基线；
2. 结构迁移；
3. 数学闭包；
4. 编辑闭包；
5. 发布候选。

完整清单是：

[`governance/07-acceptance-checklist.md`](07-acceptance-checklist.md)

Paper I 只有在以下条件满足时才可发布：

* 所有关键定理节点已证明；
* 所有 P0 开放问题已解决；
* 源迁移完整；
* 后续论文材料已无损分离；
* PDF 可复现构建；
* 独立数学与范围审查已通过；
* 摘要与结论可追溯到正文。

---

# 版本与 DOI 说明

仓库可能包含手稿的较早 DOI 关联版本。

DOI 版本、活跃重组分支与任何未来重组预印本必须被明确区分。

不要假设现有 DOI 自动指向当前工作手稿。

当发布新的稳定预印本时，应更新根 README 与手稿元数据。

---

# 研究前沿

四论文计划围绕一个稳定基础组织：

[
\text{history-sensitive arithmetic}
\longrightarrow
\text{operator semantics}
\longrightarrow
\text{geometric realization}.
]

从这一基础出发：

* Paper II 问什么可以被分析；
* Paper III 问正则几何如何变得奇异且拓扑非平凡；
* Paper IV 问商下损失了什么信息，以及该损失如何与计算相关。

该计划刻意区分：

[
\text{what has been imagined}
\neq
\text{what has been constructed}
\neq
\text{what has been verified}
\neq
\text{what has been proved}.
]

该区分是计划数学架构的一部分，而非仅是编辑约定。

## 有限型与移植 AES 更新（2026-10-09）

新的 Paper 0 紧化/collar 接口、Paper IV 有限替换与特征判据、直接必要的临界穿孔修复与
原始产物恢复边界，见[集成与源映射](h2-integration-2026-10-09.md)。当前论断修正出现在
`05b-paper-0-status-register.md` 与 `05-mathematical-status.md` 的末尾。
