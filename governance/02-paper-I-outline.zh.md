# Paper I 详细大纲

**文件：** `governance/02-paper-I-outline.md`
**状态：** 权威
**版本：** 1.1
**日期：** 2026-08-06
**依赖：**

* `AGENTS.md`
* `governance/00-authoritative-scope.md`
* `governance/01-paper-series-architecture.md`

**适用于：**
**Arithmetic Expression Geometry I: Foundations**

---

## 1. 本文档目的

本文档在以下层面固定 Paper I 目标结构：

* 节与小节；
* 定义与定理槽位；
* 逻辑依赖；
* 所需示例；
* 来源材料迁移；
* 排除；
* 验证判据。

它是当前 `paper-1/aeg-paper-1.tex` 的权威章级规范。

它不确定论文最终措辞。它确定论文必须建立什么、以什么依赖顺序，以及什么材料必须移到别处。

---

# 第一部分. 论文身份

## 2. 暂定标题

### 主标题

**Arithmetic Expression Geometry I: Foundations**

### 推荐副标题

**Sequential Histories, Affine Flow, Torsion, and Contact Geometry**

替代副标题：

**From Arithmetic Histories to Affine Geometry**

标题不得暗示 Paper I 发展完整射影、解析、奇异或计算理论。

---

## 3. 预期读者

论文应由有某些组合背景的数学家可读：

* 代数；
* 微分几何；
* 几何群论；
* 动力系统；
* 形式语言或重写；
* 接触几何。

论文不得假定 AEG 先验知识。

所有 AEG 特定术语必须从第一原则定义。

---

## 4. 中心论题

Paper I 建立以下链条：

[
\boxed{
\text{sequential expression syntax}
\longrightarrow
\text{marked arithmetic histories}
\longrightarrow
\text{projective operator semantics}
\supset
\text{affine/Borel sector}
}
]

[
\boxed{
\text{affine sector}
\longrightarrow
\text{cocycles and flow}
\longrightarrow
\text{hyperbolic realization}
\longrightarrow
\text{torsion and contact curvature}.
}
]

论文应辩护以下中心陈述：

> 带顺序依赖结构的算术表达式可被视为标记历史而非仅是带端点值的树。其非退化双边单孔语境
> 射影作用于 (\mathbb P^1(K)) 并生成 (PGL_2(K))。先前发展的连续 AEG 理论是此射影语义的
> 仿射/Borel 扇区。该扇区内，算术历史承载自然余循环、无穷小流、双曲实现、全局 torsion 公式、
> 正则零集结构与一个其曲率记录局部非交换性的接触联络。

---

## 5. 主要数学贡献

最终论文应呈现以下作为其主要贡献。

1. **顺序树分类。**

   二叉表达式树有唯一合法内部求值顺序当且仅当其内部节点形成单个脊柱。

2. **标记脊柱历史形式体系。**

   顺序树转换为带显式操作数槽数据的单孔语境历史。

3. **射影完备化定理。**

   非退化双边算术语境生成 (PGL_2(K))。

4. **仿射扇区识别。**

   现有 AEG 加–乘理论与稳定无穷远点的仿射/Borel 子群等同。

5. **仿射余循环公式。**

   目标框架与源归一化平移坐标被推导并区分。

6. **连续仿射流。**

   算术流方程从仿射 Lie 代数推导。

7. **基本双曲实现。**

   模型 (\mathfrak E_0) 被推导并验证为正则算术表达式空间。

8. **正则零轨迹定理。**

   非退化流方程下，零集是光滑余一维子流形。

9. **奇异 AES 基础。**

   奇异赋值函数与奇异零集被给予精确初始定义。

10. **广义仿射 torsion 定理。**

    ACS 比较从路径对反演扩展到相容历史对。

11. **接触曲率定理。**

    局部水平分布有正比于 (\mu\lambda) 的曲率，复现无穷小算术 torsion。

---

## 6. 刻意不做的断言

Paper I 不得声称：

* 所有算术表达式树顺序；
* 所有算术历史仿射；
* 射影延拓等价于普通算术求值；
* 仿射流是完整射影流；
* 每个 AES 双曲；
* 基本双曲模型唯一；
* 非交换性蕴含双曲性；
* 双曲性蕴含计算困难性；
* 接触形式唯一决定复结构；
* 算术全纯性已是完整函数论；
* 每个多重零构造产管或纽结；
* 无 properness 正则参数族全局拓扑平凡。

---

# 第二部分. 全局叙事

## 7. 推荐节序列

> **版本 2.0（2026-10-31）。** 此序列按
> `governance/00d-paper-I-calculus-and-capping-amendment.md`（计划 B：自包含合卷）取代版本 1.x
> 十节序列。分析三支柱与孔–盖几何现是 Paper I 自己的章节。

目标 Paper I 应有以下主结构：

```text
Section 0. Interface: Imported Geometric Primitives from Paper 0
Section 1. Introduction: From Process Histories to Order-Topological Calculus
           and Hole–Cap Geometry
Section 2. Sequential and Branching Arithmetic Histories: Spine Classification,
           Down-Set DCPOs, and Birkhoff Duality
Section 3. Bilateral Projective Semantics, the Affine Sector, and the
           Scott–Lawson Topological Correspondence
Section 4. Analytical Pillar I — Differential Theory: the Smoothing Lie Functor,
           Minimal DAG Defects, and Graded Horizontal Calculus
Section 5. Analytical Pillar II — Integral Theory: Mixed Affine Integration,
           Dual Adjoint Pairing, 1-Cocycles, and Holographic Stokes
Section 6. Analytical Pillar III — Series Theory: Free Lie Algebra Magnus
           Expansion, Arity–Cell Correspondence, and Abelianization
Section 7. Geometric Characterization I — Taxonomy of Holes, Essential
           Punctures, and Regular Zero Rigidity
Section 8. Geometric Characterization II — Theory of Caps: Ball-and-Tube
           Thickening, Hole–Disk Complementarity, Capping Obstructions, and
           Certified Sealing
Section 9. Conclusions, Claim-Status Ledger, and Downstream Research Interfaces
```

推荐附录：

```text
Appendix A. Chronological Composition, Matrix Actions, and Orientation Conventions
Appendix B. Equality, Neutrality, and Residual Separation Examples
Appendix C. Symbolic and Computational Verifications for the Magnus Series
            (Up to Order 3) and PBW Abelianization
Appendix D. Finite Cellulation and Mod-2 Homology Verification Protocol for
            Pants Gluing and Interface Disks (V1–V4)
```

---

## 8. 高层依赖顺序

内部定理依赖是：

```text
Sequential-tree classification
        ↓
Marked spinal histories
        ↓
Projective evaluation of contexts
        ↓
PGL2 generation
        ↓
Affine/Borel restriction
        ↓
Affine cocycle formulas
        ↓
Continuous affine flow
       ↙ ↓ ↘
Hyperbolic model   ACS torsion   Contact connection
       ↓                              ↓
Regular zero theorem            Curvature theorem
```

无章可在其定义章前用一概念，除非该使用显式前瞻。

---

# 第三部分. 详细章大纲

# 1. 引言

## 1.1 目的

引入问题：

> 普通求值把表达式送到值并丢弃值经以产出的路径。AEG 研究保留的求值历史并问该历史承载什么
> 代数与几何结构。

引言必须解释为何论文从顺序树而非任意表达式树开始。

---

## 1.2 过程到结果层级

引入层级：

[
\text{tree}
\longrightarrow
\text{marked history}
\longrightarrow
\text{operator}
\longrightarrow
\text{endpoint value}.
]

解释每支箭头遗忘信息。

尚不引入 Paper IV 完整凝聚理论。

---

## 1.3 为何双边完备化重要

简述：

* 现有 AEG 用定手性仿射语言；
* 允许累加器占任一操作数槽给射影变换；
* 仿射理论未被无效而是正确定位为 Borel 扇区。

引言应陈述射影完备化结果而不发展其证明。

---

## 1.4 Paper I 建立什么

给简明定理级摘要：

* 顺序语法；
* 射影定位；
* 仿射余循环；
* 连续流；
* 双曲实现；
* 正则零；
* 全局 torsion；
* 接触曲率。

---

## 1.5 Paper I 不建立什么

命名后续论文接口：

* 水平与双曲函数论：Paper II；
* 多重零奇异与管：Paper III；
* 射影凝聚与复杂度：Paper IV。

这些陈述必须框为范围边界，非声称未来理论已完整。

---

## 1.6 历史与数学定位

保留对以下内容的克制讨论：

* 形式生成与重写；
* 仿射与射影群作用；
* Hamilton–Jacobi 型一阶方程；
* 双曲几何；
* Pfaffian 与接触结构；
* Stokes 型恒等式。

不声称 AEG 是这些传统任一者的直接应用。

---

## 1.7 论文结构

给一个匹配最终结构的一段式章节指南。

---

## 第 1 章所需输出

读者应理解：

1. AEG 保留什么信息；
2. 为何顺序历史是第一个可处理类；
3. 为何仿射理论坐于射影完备化内；
4. 论文证明什么；
5. 后续研究计划从哪里开始。

---

## 现有来源材料

主要来源：

* `sections/sec01.tex`
* `paper-1/aeg-paper-1.tex` 中的摘要与引言
* `notes/projective-condensation/01-bilateral-projective-condensation.tex` 选定引言材料

---

## 所需变更

* 重写当前贡献清单。
* 移除接触几何直接强制完整函数论的声称。
* 用结束于接触曲率与零集边界的新奠基叙事取代结束于算术全纯性的现有线性叙事。
* 开头陈述仿射/射影关系。

---

# 2. 顺序算术历史

## 2.1 算术表达式树

定义域或指定系数集上的算术表达式。

推荐初始代数设置：

[
K
]

一个域，用除法时普通算术域显式限制。

定义：

* 叶；
* 内部顶点；
* 运算标签；
* 求值依赖；
* 合法求值顺序。

论文可初始描述普通有理表达式供直觉，但定理陈述应用适当一般域假设。

---

## 2.2 依赖偏序

对表达式树 (T)，定义：

[
I(T)
]

为内部顶点集，按依赖排序。

顶点 (u) 先于 (v) 若 (u) 的输出在求值 (v) 前所需。

---

## 2.3 顺序树分类

### 定理槽位

**定理：顺序树分类**

对有限二叉表达式树 (T)，以下等价：

1. (I(T)) 有唯一线性扩张；
2. (I(T)) 是链；
3. 每个内部顶点至多一个内部子；
4. 内部顶点形成单个脊柱。

证明必须含于正文。

---

## 2.4 标记累加器

解释为何未标记最内二叉节点不唯一决定哪叶是演化状态。

定义标记初始累加器。

此标记把顺序树转换为单孔语境历史。

---

## 2.5 单孔算术语境

定义：

[
C_{\omega,c}^{(1)}[z]
=====================

\omega(z,c),
]

[
C_{\omega,c}^{(2)}[z]
=====================

\omega(c,z).
]

定义标记脊柱历史：

[
\gamma
======

\bigl(
x_0;
(\omega_i,c_i,\varepsilon_i)_{i=1}^{n}
\bigr).
]

定义手性词：

[
\varepsilon(\gamma)
===================

\varepsilon_1\cdots\varepsilon_n.
]

---

## 2.6 自由与有界历史

定义：

* 自由历史；
* 有界历史；
* 初始状态；
* 年代复合；
* 可允许性。

固定约定：

[
\nu_x(\gamma)
=============

g_n\circ\cdots\circ g_1(x).
]

---

## 2.7 镜像、反演与逆

分别定义：

* 镜像 (m\gamma)；
* 时间反演 (r\gamma)；
* 路径逆 (\gamma^{-1})，有定义时。

含一个小示例显示：

[
m\gamma\neq r\gamma.
]

显式陈述现有仿射 torsion 是序比较效应且不自动是镜像不变量。

---

## 2.8 相等层级

保留并锐化当前层级：

1. 字面相等；
2. 标记历史相等；
3. 算子相等；
4. charge 相等；
5. 端点相等；
6. 商或关系相等。

不发展完整关系或环理论。

---

## 2.9 示例

所需示例：

1. 一个非顺序分支表达式；
2. 一个纯槽-(1) 历史；
3. 一个纯槽-(2) 历史；
4. 一个混合手性历史；
5. 镜像对时间反演；
6. 两个不同历史同端点值。

---

## 第 2 章所需输出

本章必须产出一个稳定奠基对象：

[
\boxed{\text{marked spinal history}.}
]

所有后续章必须用此对象而非「threadlike expression」的含糊先前定义。

---

## 现有来源材料

主要来源：

* `sections/sec02-00.tex`
* `sections/sec02-01.tex`
* `notes/projective-condensation/01-bilateral-projective-condensation.tex`

---

## 移除或替换材料

* 替换现有左子/右子定义。
* 除非伴槽记号，避免含糊「left-expanded」与「right-expanded」术语。
* 把大量环与中性讨论移到附录或未来工作。

---

# 3. 射影语义与仿射扇区

## 3.1 普通与射影语义

定义：

[
\mathbb P^1(K)=K\cup{\infty}.
]

解释非退化单孔语境按分式线性变换作用。

区分：

* 普通算术可允许性；
* 射影延拓；
* 极点；
* 图转换；
* 常量或退化映射。

---

## 3.2 初等语境矩阵表示

为以下提供表：

* (z\mapsto z+c)；
* (z\mapsto z-c)；
* (z\mapsto c-z)；
* (z\mapsto cz)；
* (z\mapsto z/c)；
* (z\mapsto c/z)。

陈述可逆性假设。

---

## 3.3 射影求值映射

定义：

[
\rho:
\operatorname{Hist}^{\pm,\times}_K
\longrightarrow
PGL_2(K).
]

陈述年代矩阵复合约定。

---

## 3.4 双边生成定理

### 定理槽位

**定理：双边算术生成 (PGL_2(K))**

显示平移、非零缩放与 Weyl 反演生成全部分式线性变换。

用显式分解如：

[
\frac{Az+B}{Cz+D}
=================

T_{A/C}
\circ
D_{(AD-BC)/C^2}
\circ
J
\circ
T_{D/C}
]

当 (C\neq0)。

单独处理 (C=0)。

---

## 3.5 仿射/Borel 扇区

### 推论槽位

显示限制到仿射相容语境给：

[
B_\infty
========

\operatorname{Stab}_{PGL_2(K)}(\infty)
\cong
\operatorname{Aff}(1,K).
]

精确陈述哪个受限历史语言映射到此子群。

---

## 3.6 (q=4) Hecke 算术子语言

在 (K=\mathbb Q(\sqrt2)) 上，隔离射影语境

[
T(z)=z+\sqrt2,
\qquad
J(z)=-1/z.
]

在射影群中证明矩阵关系 (J^2=(JT)^4=1) 并引用其像与 (q=4) Hecke 三角群的标准等同。对选定胞腔
稳定子记录因式分解

[
\text{marked history}
\longrightarrow G_4
\longrightarrow G_4/H_{\mathcal C}
]

两箭头都不一般单射。实种子处普通算术可允许性保持与射影 Fuchs 作用分离。

---

## 3.7 正实扇区

解释当前连续参数化：

[
z\mapsto e^\lambda z
]

带 (\lambda\in\mathbb R) 覆盖正实缩放。

故后来发展的微分几何理论对应：

[
\operatorname{Aff}^{+}(1,\mathbb R),
]

不自动对应全部 (\operatorname{Aff}(1,\mathbb R))。

---

## 3.8 Bruhat 定位

简明注可陈述：

[
PGL_2(K)=B\sqcup BJB.
]

把双边完备化解释为仿射扇区的秩一 Bruhat 完备化。

不发展定位所需之外的表示论。

---

## 3.9 Riccati 展望

无完整发展陈述射影向量场 Lie 代数含：

[
\partial_z,\qquad
z\partial_z,\qquad
z^2\partial_z.
]

故一般射影流有形式：

[
\dot z
======

\beta+\alpha z+\kappa z^2.
]

Paper I 发展的仿射理论是切片：

[
\kappa=0.
]

---

## 第 3 章所需输出

读者应理解：

[
\boxed{
\text{current AEG}
==================

\text{a natural affine/Borel sector of bilateral projective arithmetic}.
}
]

---

## 现有来源材料

主要来源：

* `notes/projective-condensation/01-bilateral-projective-condensation.tex`

支持来源：

* `sections/sec02-01.tex` 仿射群材料
* `sections/sec03.tex` 矩阵 Lie 材料

---

## 本章排除材料

移到 Paper IV：

* 双赋值；
* 秩一投影子定理；
* (G/H)；
* (G/B_\pm)；
* 过程结果丛；
* 概念–谓词语义；
* 有限域商计数；
* 射影凝聚。

---

# 4. 仿射余循环与相对缺陷

## 4.1 仿射历史求值

对仿射语境：

[
f_i(x)=s_i x+t_i,
\qquad s_i\in K^\times,
]

定义：

[
f_n\circ\cdots\circ f_1(x)
==========================

\Phi_nx+\xi_n.
]

---

## 4.2 目标框架余循环

### 命题槽位

证明：

[
\Phi_n
======

\prod_{i=1}^n s_i,
]

[
\xi_n
=====

\sum_{i=1}^n
t_i\prod_{j=i+1}^n s_j.
]

把每个加法事件解释为被所有未来尺度加权。

---

## 4.3 源归一化余循环

定义：

[
\widehat\xi_n
=============

\Phi_n^{-1}\xi_n.
]

证明：

[
\widehat\xi_n
=============

\sum_{i=1}^n
\frac{t_i}{\prod_{j=1}^i s_j}.
]

把每个加法事件解释为被累积过去尺度归一化。

---

## 4.4 左与右 Maurer–Cartan 读法

对：

[
g=
\begin{pmatrix}
e^\lambda & \xi\
0&1
\end{pmatrix},
]

推导：

[
(g^{-1}dg)_{\mathrm{tr}}
========================

e^{-\lambda}d\xi,
]

[
(dg,g^{-1})_{\mathrm{tr}}
=========================

d\xi-\xi,d\lambda.
]

解释源/体与目标/空间读法。

不把这些与操作数槽手性等同。

---

## 4.5 相对仿射缺陷

对两个仿射历史：

[
\rho(\gamma)(x)=\Phi_\gamma x+\xi_\gamma,
]

[
\rho(\delta)(x)=\Phi_\delta x+\xi_\delta,
]

定义相对比较。

当：

[
\Phi_\gamma=\Phi_\delta,
]

端点差独立于 (x)：

[
\nu_x(\gamma)-\nu_x(\delta)
===========================

\xi_\gamma-\xi_\delta.
]

也记录归一化相对仿射变换：

[
\rho(\delta)^{-1}\rho(\gamma).
]

---

## 4.6 初等 torsion 作余循环缺陷

恢复：

[
(x+\mu)e^\lambda
----------------

# (xe^\lambda+\mu)

\mu(e^\lambda-1).
]

解释为初等仿射平移缺陷。

---

## 4.7 扰动传播

保留交替历史有用扰动公式：

[
\frac{\alpha(\widetilde x)-\alpha(x)}
{\widetilde x-x}
================

\Phi_\alpha.
]

此应作为仿射求值直接推论而非独立理论呈现。

---

## 第 4 章所需输出

本章必须建立后来 ACS 中出现的加权核非手工几何插入。它们由仿射余循环强制。

---

## 现有来源材料

主要来源：

* `sections/sec02-01.tex`
* `sections/sec03.tex`
* `notes/projective-condensation/01-bilateral-projective-condensation.tex`

---

## 移动材料

把大量自由群、环与凝聚解释移到 Paper IV。

---

# 5. 连续算术流

## 5.1 从离散历史到无穷小生成元

引入局部坐标：

[
(u,v),
]

表加法与乘法方向。

固定实参数：

[
\mu,\lambda.
]

解释从以下取极限：

[
a\mapsto a+\mu,du,
]

[
a\mapsto e^{\lambda,dv}a.
]

---

## 5.2 仿射 Lie 代数推导

用：

[
E=\partial_a,
\qquad
H=a\partial_a.
]

对方向：

[
\Omega(\theta)
==============

\mu\cos\theta,E
+
\lambda\sin\theta,H,
]

推导：

[
\frac{da}{ds}
=============

\mu\cos\theta
+
\lambda a\sin\theta.
]

Lie 论推导应为主要。

两阶 Taylor 展开可留作直觉或补充检查。

---

## 5.3 Pfaffian 形式

写：

[
da
==

\mu,du
+
\lambda a,dv.
]

清楚陈述此关系描述可允许水平传播且非整个三维状态空间上全局可积。

---

## 5.4 方向解

对固定 (\theta)，解：

[
\frac{da}{ds}
=============

\mu\cos\theta+\lambda a\sin\theta.
]

含特殊加法与乘法方向。

---

## 5.5 梯度与 eikonal 形式

引入相容正交框架后，推导：

[
|\nabla a|^2
============

\mu^2+\lambda^2a^2.
]

澄清此方程依赖度量选择。

---

## 5.6 矫正坐标

定义：

[
r(a)
====

\operatorname{arcsinh}
\left(
\frac{\lambda a}{\mu}
\right)
]

在适当假设下。

显示沿梯度轨迹：

[
|\nabla r|
==========

|\lambda|.
]

分别处理或显式排除 (\mu=0) 或 (\lambda=0) 符号与情形。

---

## 5.7 局部 torsion 密度

比较无穷小加–乘顺序并得：

[
d\tau
=====

\mu\lambda,du,dv
+
\text{higher-order terms}.
]

陈述这是无穷小公式，非精确有限公式。

---

## 5.8 仿射对 Riccati 流

以定位结束本章：

[
\dot z
======

\beta+\alpha z
]

于：

[
\dot z
======

\beta+\alpha z+\kappa z^2.
]

---

## 第 5 章所需输出

本章必须提供流方程的一个清楚、约定受控推导。

它不得呈现若干不相容推导而不识别其关系。

---

## 现有来源材料

主要来源：

* `sections/sec03.tex`

支持来源：

* `notes/projective-condensation/01-bilateral-projective-condensation.tex`

---

## 缩减材料

* 压缩中断主逻辑的扩展围角代数。
* 把重复坐标计算移到附录。
* 仅保留后来所用公式。

---

# 6. 基本双曲表达式空间

## 6.1 从仿射群到齐次曲面

把：

[
\operatorname{Aff}^{+}(1,\mathbb R)
]

与二维可解 Lie 群等同。

选归一化不变度量使加法与乘法生成元方向有指定长度。

推导坐标形如：

[
g_{\mu,\lambda}
===============

e^{-2\lambda v}
\frac{du^2}{\mu^2}
+
dv^2.
]

---

## 6.2 上半平面形式

变换到坐标 ((x,y)) 并得：

[
g_{\mu,\lambda}
===============

\frac1{y^2}
\left(
\frac{dx^2}{\mu^2}
+
\frac{dy^2}{\lambda^2}
\right).
]

定义：

[
a(x,y)
======

-\frac{x}{y}.
]

---

## 6.3 验证定理

### 定理槽位

**定理：基本双曲 AES**

证明：

[
|\nabla a|*{g*{\mu,\lambda}}^2
==============================

\mu^2+\lambda^2a^2.
]

定义：

[
\mathfrak E_0(\mu,\lambda)
==========================

(\mathcal H,g_{\mu,\lambda},a).
]

陈述所有假设。

---

## 6.4 曲率与归一化

计算 Gauss 曲率。

解释哪个参数控制：

* 曲率尺度；
* 加法单位；
* 坐标归一化。

避免过度声称唯一性。

---

## 6.5 Horocyclic 几何

描述：

* horocycles；
* 正交测地线；
* 乘法坐标水平集；
* 赋值等高线。

解释加法与乘法如何几何作用。

---

## 6.6 算术网格

定义实现以下有限变换：

[
a\mapsto a+s,
]

[
a\mapsto ka.
]

直接验证它们。

---

## 6.7 Baumslag–Solitar 关系

正确表述时保留精确关系：

[
Y_k^{-1}X_s^{,k}Y_k=X_s,
]

或约定等价形式。

仔细检查复合顺序。

陈述关系由网格作用实现。

不从它推断计算复杂度。

---

## 6.8 Laplace 特征函数

计算适当 Laplace–Beltrami 算子并证明 (a) 的特征值关系。

陈述 (\Delta) 符号约定。

---

## 6.9 局部面积解释

仅把阶梯示例保留为局部 torsion 面积原则的说明。

全局定理属第 8 章。

---

## 第 6 章所需输出

基本双曲模型必须作为仿射理论的结构实现出现，非孤立 ansatz。

---

## 现有来源材料

主要来源：

* `sections/sec04.tex`

支持来源：

* `sections/sec02-00.tex`
* `sections/sec03.tex`
* `notes/projective-condensation/02-projective-geometric-frameworks.tex`

---

## 移动材料

移到 Paper III：

* 一般参数族管推测；
* 一般 (E_k) 讨论；
* 多重零分类。

---

# 7. 零轨迹与奇异表达式空间

## 7.1 正则零集

对满足：

[
|\nabla a|^2
============

\mu^2+\lambda^2a^2,
]

的正则 AES，显示在：

[
Z(a)=a^{-1}(0),
]

上有：

[
|\nabla a|
==========

|\mu|.
]

---

## 7.2 正则零定理

### 定理槽位

**定理：正则零轨迹**

若 (\mu\neq0)，则 (0) 是 (a) 的正则值。

因此：

[
Z(a)
]

是光滑余一维子流形。

对二维 AES，是不相交光滑曲线并。

---

## 7.3 推论

记录显式推论：

* 无孤立正则零；
* 无正则交叉；
* 无正则分支；
* 无正则内部端点；
* 固定光滑非退化模型内无正则诞生或死亡。

每个陈述必须在正确假设下表述。

---

## 7.4 完备正则分裂

对连通、完备、无边正则 AES，定义

[
r(a)=\int_0^a\frac{ds}{\sqrt{\mu^2+\lambda^2s^2}}.
]

证明 (|\nabla r|=1)、其梯度场有完备流，且

[
Z(a)\times\mathbb R\longrightarrow M,
\qquad
(q,t)\longmapsto\Phi_t(q)
]

是微分同胚。显式陈述这不必是 Riemannian 乘积。结论 (a) 满射且 (Z(a)) 非空连通。解释为何边界
或不完备度量使全局流证明无效。

---

## 7.5 奇异算术表达式空间

定义奇异 AES：

[
(\mathcal M,S,g,a;\mu,\lambda),
]

其中正则方程在：

[
\mathcal M\setminus S.
]

上成立。

允许以下奇异行为：

* (a)；
* (g)；
* (\mu,\lambda)；
* 图结构；
* 域；
* 射影延拓。

---

## 7.6 正则与奇异零集

定义：

[
Z_{\mathrm{reg}}(a),
\qquad
Z_{\mathrm{sing}}(a).
]

澄清一点可位于零集但非正则零，因函数、度量、参数或域奇异。

---

## 7.7 孤立零模型

重估现记为 (\mathfrak E_1) 的模型。

所需处理：

1. 陈述其域；
2. 陈述中心是否含；
3. 陈述 (a) 那里是否光滑；
4. 陈述度量那里是否正则；
5. 陈述流方程哪里成立；
6. 把中心分类为奇异零。

不作为带孤立零的正则 AES 呈现。

---

## 7.8 极小多重零示例

仅完全验证时含。

所需清单：

* 显式域；
* 显式度量；
* 显式赋值；
* 完整奇异集；
* 流验证；
* 精确零拓扑。

若无示例通过此清单，从正文省略并在展望陈述构造问题。

---

## 7.9 参数族

设：

[
a_t:\mathcal M\to\mathbb R,
]

并定义：

[
A(p,t)=a_t(p).
]

定义：

[
\mathcal Z=A^{-1}(0).
]

---

## 7.10 正则总零集引理

### 命题槽位

若：

[
d_pa_t\neq0
]

在每个零，则：

[
\mathcal Z
]

是 (\mathcal M\times I) 的光滑余一维子流形。

若 (\dim\mathcal M=2)，则 (\mathcal Z) 是曲面。

尚不称其为全局平凡管。

---

## 7.11 Properness 警告

陈述：

[
\pi:\mathcal Z\to I
]

的拓扑保持或局部平凡需附加假设如 properness。

完整定理属 Paper III。

---

## 第 7 章所需输出

本章必须建立以下之间边界：

[
\text{regular zero geometry}
]

与：

[
\text{singular multi-zero/tube geometry}.
]

此边界是 Paper I 中心奠基结果之一。

---

## 现有来源材料

主要来源：

* `sections/sec04.tex` 奇异与零集部分

支持来源：

* 多重零与管笔记，仅用于分类与迁移；
* `governance/discussions/` 下近期研究摘要。

---

## 移动材料

移到 Paper III：

* 完整多重零构造；
* (E_k)；
* (E_{\log})；
* 零线分岔；
* 管穿线；
* 辫；
* 纽结；
* Markov 归一化。

---

# 8. 全局 Torsion 与累积交换空间

## 8.1 ACS 目的

解释 ACS 记录总加法与乘法 charge 而遗忘完整非交换历史。

定义：

[
(A,M).
]

陈述它是交换影子，非完整表达式空间。

---

## 8.2 ACS 路径

对仿射历史 (\gamma)，定义折线路径：

[
C_\gamma.
]

固定定向与年代约定。

---

## 8.3 求值作加权路径积分

直接从仿射余循环推导求值公式。

选一个规范定向约定。

优选形式是：

[
\nu_x(\gamma)
=============

e^{M_\gamma}
\left(
x+
\int_{C_\gamma}e^{-M},dA
\right).
]

若保留反路径表述，证明其等价并解释定向变化。

---

## 8.4 相容历史

定义两历史 (\gamma,\delta) charge 相容当它们有相同总加法与乘法 charge，或仅需端点独立时至少
相同总乘法尺度。

陈述每个定理所用精确相容条件。

---

## 8.5 相对 torsion

定义：

[
\tau(\gamma,\delta)
===================

\nu_x(\gamma)-\nu_x(\delta).
]

在所述相容条件下证明独立于 (x)。

时间反演成为特殊情形：

[
\tau(\gamma,r\gamma).
]

---

## 8.6 边界积分定理

### 命题槽位

把：

[
\tau(\gamma,\delta)
]

表达为围绕：

[
C_\gamma-C_\delta.
]

的加权围线积分。

显式固定符号。

---

## 8.7 加权面积定理

### 定理槽位

对定向填充：

[
\partial\Sigma_{\gamma,\delta}
==============================

C_\gamma-C_\delta,
]

证明：

[
\tau(\gamma,\delta)
===================

# \oint_{\partial\Sigma_{\gamma,\delta}}\eta

\iint_{\Sigma_{\gamma,\delta}}d\eta.
]

陈述一形式 (\eta) 与定向约定。

---

## 8.8 示例

所需示例：

1. 一个加–乘方形；
2. 一个四步阶梯；
3. 两个非反演历史等总 charge；
4. 一个带符号 charge 示例，若定向形式体系干净支持。

---

## 8.9 代数解释

简述 ACS 关联交换化 charge 数据。

不声称整个求值仿射群是自由群 (F_2)。

区分：

* 自由符号历史；
* 求值仿射算子；
* 交换化 charge 路径。

---

## 第 8 章所需输出

本章必须建立精确局部–全局关系：

[
\boxed{
\text{affine cocycle difference}
================================

# \text{weighted boundary integral}

\text{weighted area}.
}
]

---

## 现有来源材料

主要来源：

* `sections/sec05.tex`

支持来源：

* 第 4 章来源的仿射余循环材料。

---

## 所需变更

* 推广到路径对反演之外。
* 用余循环简化求值公式。
* 固定一个一致符号与定向约定。
* 移除保留给 Paper IV 的推测商理论。

---

# 9. 接触联络与水平曲率

## 9.1 状态空间

定义：

[
\mathcal C
==========

\mathbb R^3_{(u,v,a)}
]

或 ((u,v)) 平面上适当局部丛。

---

## 9.2 接触形式

定义：

[
\alpha
======

da-(\mu,du+\lambda a,dv).
]

证明：

[
\alpha\wedge d\alpha\neq0
]

当：

[
\mu\lambda\neq0.
]

---

## 9.3 水平分布

定义：

[
\mathcal H=\ker\alpha.
]

引入：

[
D_u
===

\partial_u+\mu\partial_a,
]

[
D_v
===

\partial_v+\lambda a\partial_a.
]

显示：

[
\alpha(D_u)=\alpha(D_v)=0.
]

---

## 9.4 Legendrian 算术流

显示切于：

[
\cos\theta D_u+\sin\theta D_v
]

的曲线满足算术流方程。

这建立接触结构打包仿射传播律。

---

## 9.5 曲率括号

### 定理槽位

证明：

[
[D_u,D_v]
=========

\mu\lambda\partial_a.
]

解释括号为水平分布不闭合的垂直失败。

---

## 9.6 精确有限交换子

计算有限加–乘比较：

[
\mu h(e^{\lambda k}-1).
]

单独计算闭环垂直漂移。

显式陈述：

* 开双路径缺陷；
* 闭环 holonomy；
* 无穷小括号

相关但有限尺度不等同。

---

## 9.7 水平协变微分

定义：

[
\delta_HF
=========

dF-(\partial_aF)\alpha.
]

等价：

[
\delta_HF
=========

(D_uF),du+(D_vF),dv.
]

---

## 9.8 水平微分曲率

证明：

[
\delta_H^2F
===========

\mu\lambda(\partial_aF),du\wedge dv.
]

特别：

[
\delta_H^2a
===========

\mu\lambda,du\wedge dv.
]

清楚陈述 (\delta_H) 非幂零微分。

---

## 9.9 局部–全局比较

以结构对应结束：

[
\boxed{
\begin{aligned}
\text{finite affine history defect}
&\longleftrightarrow
\text{ACS weighted area},\
\text{infinitesimal history defect}
&\longleftrightarrow
\text{contact curvature}.
\end{aligned}}
]

澄清有限与无穷小公式相差指数加权与高阶效应。

---

## 9.10 尚未解析

陈述接触分布本身不供：

* 唯一水平度量；
* 唯一复结构；
* 规范 (\bar\partial)-算子；
* 完整调和理论。

这些在 Paper II 发展。

---

## 第 9 章所需输出

本章必须完成主要奠基弧：

[
\text{history order defect}
\longrightarrow
\text{curvature}.
]

---

## 现有来源材料

主要来源：

* `sections/sec06.tex`
* `sections/sec07.tex` 基础部分

---

## 移动材料

移到 Paper II：

* 大量链规则表；
* affine–Appell 基；
* 反微分程序；
* 算术 Cauchy–Riemann 方程；
* 算术全纯性；
* 扭曲调和性。

---

# 10. 结论与研究接口

## 10.1 已建立什么

总结实际证明链：

[
\text{sequential histories}
\to
PGL_2
\supset
\operatorname{Aff}(1)
\to
\text{flow}
\to
\mathfrak E_0
\to
\text{torsion/contact curvature}.
]

含正则零集结构作为单独奠基推论。

---

## 10.2 到 Paper II 的接口

陈述 Paper II 加：

* 水平度量与相容复结构；
* 二阶算子；
* 边值理论；
* 算术全纯性。

不把未来解析结果陈述为已证明。

---

## 10.3 到 Paper III 的接口

陈述 Paper III 研究正则零假设失败：

* 奇异零；
* 多重零模型；
* 参数判别式；
* 正则与奇异管；
* 单值与条件纽结结构。

---

## 10.4 到 Paper IV 的接口

陈述 Paper IV 发展：

* 完整射影过程结果层级；
* 双赋值；
* 商塔；
* 凝聚；
* 表示与计算复杂度。

---

## 10.5 开放奠基问题

Paper I 可以克制清单结束：

1. 正则仿射 AES 模型分类；
2. ACS 的射影替代；
3. 仿射接触曲率与射影 holonomy 比较；
4. 完全验证多重零模型构造；
5. 几何与计算复杂度精确关系。

这些必须标为开放。

---

## 第 10 章所需输出

结论不得重复 Paper I 已建立函数论的旧声称。

它应以稳定基础与清楚标记接口结束。

---

# 第四部分. 附录

# 附录 A. 复合与作用约定

含：

* 年代复合；
* 矩阵乘法顺序；
* 左对右作用；
* 普通对射影域；
* 记号转换表。

此附录应消除正文约定歧义。

---

# 附录 B. 仿射余循环计算

含：

* 归纳证明；
* 交替历史展开；
* 扰动传播；
* (\xi) 与 (\widehat\xi) 转换；
* 选定显式示例。

---

# 附录 C. 双曲模型计算

含：

* 坐标变换；
* 逆度量；
* 梯度计算；
* 曲率计算；
* Laplacian 计算；
* 网格变换；
* Baumslag–Solitar 关系检查。

---

# 附录 D. ACS 与接触计算

含：

* 带符号路径示例；
* 有限交换子计算；
* Stokes 符号检查；
* 接触形式 Darboux 归一化；
* Reeb 场，若保留；
* 详细 (\delta_H^2) 计算。

---

# 附录 E. 相等与中性示例

保留一小组示例区分：

* 同值不同算子；
* 同算子不同历史；
* 同 charge 不同 torsion；
* 零端点缺陷非平凡历史；
* 局部 torsion 对闭环 holonomy。

不发展完整环理论。

---

# 第五部分. 目标源文件组织

## 11. 推荐 LaTeX 结构

可能目标组织是：

```text
paper-1/
├── aeg-paper-1.tex
├── sections/
│   ├── 01-introduction.tex
│   ├── 02-sequential-histories.tex
│   ├── 03-projective-affine.tex
│   ├── 04-affine-cocycles.tex
│   ├── 05-affine-flow.tex
│   ├── 06-hyperbolic-model.tex
│   ├── 07-zero-geometry.tex
│   ├── 08-acs-torsion.tex
│   ├── 09-contact-curvature.tex
│   └── 10-conclusion.tex
├── appendices/
│   ├── app-A-conventions.tex
│   ├── app-B-cocycles.tex
│   ├── app-C-hyperbolic.tex
│   ├── app-D-acs-contact.tex
│   └── app-E-equality.tex
└── images/
```

仓库现用 `paper-1/` 下此逻辑划分，附录存于兄弟 `paper-1/appendices/` 目录。

重组任务不得在数学审计完成前重命名每个文件。

---

# 第六部分. 当前到目标迁移摘要

## 12. 现有源映射

| 当前源 | 目标目的地 |
| --- | --- |
| `sections/sec01.tex` | 第 1 章，重度重写 |
| `sections/sec02-00.tex` | 第 2 章，表达式树材料保留 |
| `sections/sec02-01.tex` | 第 2 与 4 章间分割 |
| `sections/sec03.tex` | 第 5 章；仿射群材料也第 4 章 |
| `sections/sec04.tex` | 第 6 与 7 章 |
| `sections/sec05.tex` | 第 8 章，推广 |
| `sections/sec06.tex` | 第 9 章 |
| `sections/sec07.tex` | 基础部分到第 9 章；解析材料到 Paper II |
| `sections/sec08.tex` | 移到 Paper II |
| `sections/sec09.tex` | 由第 10 章取代 |
| `notes/projective-condensation/01-bilateral-projective-condensation.tex` | 第 2 与 3 章基础；余下到 Paper IV |
| 多重零与管笔记 | 仅第 7 章定义；余下到 Paper III |
| 资源/复杂度笔记 | Paper IV |
| 旧环笔记 | 附录 E 或后续关系论工作 |

详细行级迁移属：

```text
governance/04-current-to-target-map.md
```

---

# 第七部分. 建议长度预算

## 13. 正文预算

推荐正文目标：

| 章 | 大约页数 |
| --- | ---: |
| 1. 引言 | 4–6 |
| 2. 顺序历史 | 8–10 |
| 3. 射影与仿射语义 | 7–9 |
| 4. 仿射余循环 | 6–8 |
| 5. 连续流 | 7–9 |
| 6. 双曲模型 | 9–12 |
| 7. 零几何 | 7–10 |
| 8. ACS torsion | 8–10 |
| 9. 接触曲率 | 8–10 |
| 10. 结论 | 3–4 |

推荐正文：

[
65\text{–}85\ \text{pages}
]

含图不含附录。

若草稿显著超此范围，把计算或次要示例移到附录。

---

# 第八部分. 图计划

## 14. 所需概念图

Paper I 应含一组带清楚数学功能的有限图。

### 图 1：过程到结果塔

[
\text{tree}
\to
\text{history}
\to
\text{operator}
\to
\text{value}.
]

### 图 2：顺序对分支树

显示依赖链判据。

### 图 3：槽-(1)、槽-(2) 与混合历史

显示手性而不依赖左/右行文。

### 图 4：射影变换内的仿射扇区

示意显示：

[
B_\infty\subset PGL_2.
]

### 图 5：双曲算术网格

保留并改进现有加–乘网格。

### 图 6：正则零线对奇异孤立零

显示为何后者在正则定理之外。

### 图 7：两相容 ACS 历史与加权填充

用推广双历史表述。

### 图 8：接触交换子方形

区分开双路径缺陷与闭环 holonomy。

无图应用作未证明定理证据。

---

# 第九部分. 定理清单

## 15. 所需定理与命题槽位

目标论文应含至少以下稳定标签：

```text
thm:sequential-tree-classification
def:marked-spinal-history
def:projective-evaluation
thm:bilateral-pgl2-generation
cor:affine-borel-sector
prop:affine-cocycle-formulas
prop:left-right-affine-differentials
thm:continuous-affine-flow
def:regular-aes
thm:basic-hyperbolic-aes
prop:laplace-eigenfunction
thm:regular-zero-locus
def:singular-aes
prop:regular-total-zero-set
def:acs
def:relative-torsion
thm:torsion-stokes
prop:contact-form
thm:contact-curvature
prop:horizontal-differential-curvature
```

标签可精化，但 `final_revised_enhanced` 等叙事标签必须移除。

---

# 第十部分. 验证清单

## 16. 数学验证

Paper I 视为结构完整前，验证：

* [ ] 顺序树定义与所有示例一致。
* [ ] 镜像与反演绝不混淆。
* [ ] 射影矩阵复合匹配年代求值。
* [ ] 除法域已陈述。
* [ ] (PGL_2) 生成证明处理所有情形。
* [ ] 仿射扇区带正确域与定向限定陈述。
* [ ] (\xi) 与 (\widehat\xi) 不交换。
* [ ] 流推导用一个显式左/右约定。
* [ ] eikonal 方程仅在度量指定后陈述。
* [ ] 双曲模型梯度计算正确。
* [ ] Laplacian 符号约定固定。
* [ ] Baumslag–Solitar 关系用正确作用顺序。
* [ ] 正则零定理含 (\mu\neq0)。
* [ ] 孤立零模型分类为奇异。
* [ ] 总零集结果不过度陈述为全局管定理。
* [ ] 相对 torsion 假设显式。
* [ ] ACS 定向与符号约定一致。
* [ ] 开缺陷与闭 holonomy 区分。
* [ ] (\delta_H) 不被描述为幂零。
* [ ] 无解析复结构被声称接触规范。

---

## 17. 编辑验证

* [ ] 摘要匹配最终定理集。
* [ ] 引言无未来论文结果作已确立定理。
* [ ] 所有符号使用前引入。
* [ ] (\mathfrak E_0) 与 (\mathfrak E_1) 一致使用。
* [ ] `u` 与 `\nu` 不混淆。
* [ ] 示例用 `Example` 定理环境。
* [ ] 重复标签移除。
* [ ] 未定义引用解析。
* [ ] 引用相关且准确。
* [ ] 移到 Papers II–IV 的材料记录。
* [ ] PDF 成功构建。

---

# 第十一部分. 重组阶段

## 18. 推荐实现顺序

### 阶段 0：审计

不修改正文。

产出：

```text
governance/audit-report.md
```

---

### 阶段 1：骨架

创建目标章结构同时临时位置保留当前内容。

确保 PDF 构建。

---

### 阶段 2：顺序与射影基础

实现第 2 与 3 章。

不修改后续几何章超出必要引用。

---

### 阶段 3：仿射余循环与流

实现第 4 与 5 章。

归一化复合约定。

---

### 阶段 4：双曲与零几何

实现第 6 与 7 章。

解决 (\mathfrak E_0/\mathfrak E_1) 状态。

---

### 阶段 5：ACS 与接触几何

实现第 8 与 9 章。

推广 torsion 并归一化曲率术语。

---

### 阶段 6：迁移

移动：

* 函数论到 Paper II；
* 多重零/管理论到 Paper III；
* 射影凝聚与复杂度到 Paper IV。

---

### 阶段 7：全局重写

重写：

* 摘要；
* 引言；
* 结论；
* 节过渡；
* 参考文献引用；
* 图注。

---

### 阶段 8：数学审计

对照以下检查每个定理：

```text
governance/05-mathematical-status.md
```

不以编辑重写解决开放数学问题。

---

## 19. 最终结构判据

Paper I 只有读者能跟随完整链才成功：

[
\boxed{
\begin{aligned}
\text{Why is a sequential expression a history?}\
\Downarrow\
\text{What operator does that history induce?}\
\Downarrow\
\text{Why is the current theory affine inside a projective completion?}\
\Downarrow\
\text{How do affine histories produce flow and geometry?}\
\Downarrow\
\text{How does order defect become torsion and curvature?}\
\Downarrow\
\text{Where do regular geometry and singular extensions separate?}
\end{aligned}}
]

任何不推进此链的节应缩短、移到附录或分配给后续论文。
