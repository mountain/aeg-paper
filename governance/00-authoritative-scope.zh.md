# AEG 论文重组的权威范围

**文件：** `governance/00-authoritative-scope.md`
**状态：** 权威
**版本：** 1.1
**日期：** 2026-08-06
**适用于：** 算术表达式几何论文仓库的重组

---

## 1. 目的

本文件固定算术表达式几何（AEG）系列前四篇论文的权威研究与编辑范围。

其目的是防止范围漂移、意外加强数学论断、论文间重复与重组期间材料丢失。

四篇论文暂定题为：

1. **Arithmetic Expression Geometry I: Foundations**
2. **Arithmetic Expression Geometry II: Hyperbolic Real Function Theory**
3. **Arithmetic Expression Geometry III: Singular Zero Geometry and Tubes**
4. **Arithmetic Expression Geometry IV: Projective Condensation and Computational Complexity**

标题可后精化，但此处所述数学分工除非本文档显式修订否则有约束力。

---

## 2. 权威与冲突解决

本文件是四论文系列范围的最高层仓库规范。

当来源冲突时，用以下顺序：

1. 当前任务的显式指令；
2. 本文档；
3. `AGENTS.md`；
4. `governance/` 下其他权威文件；
5. 当前 Paper I 源；
6. 研究笔记、工作论文、会议笔记与归档讨论。

历史笔记与聊天转录可能含：

* 被取代定义；
* 废弃术语；
* 探索性类比；
* 中间猜想；
* 不完备证明；
* 后来被削弱或拒绝的论断。

它们不得覆盖本文档的决定。

冲突不得静默调和。未解决冲突记录于：

```text
governance/08-open-questions.md
```

---

## 3. 规范语言

术语 **must**、**must not**、**should**、**should not** 与 **may** 作规范使用。

* **Must** 表示论文或重组过程的必需部分。
* **Must not** 表示被排除的论断或发展。
* **Should** 表示除非数学理由要求否则优选处理。
* **May** 表示不改变范围的可选材料。

---

## 4. 共享概念架构

前四篇论文研究一个过程到结果层级的不同层：

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

论文必须保留以下区分：

* 语法与语义；
* 历史与诱导算子；
* 算子与端点值；
* 局部与全局缺陷；
* 仿射与射影理论；
* 正则与奇异几何；
* 解析结构与拓扑结构；
* 表示复杂度与计算成本。

无论文可静默坍缩这些层。

暂定依赖架构是：

[
\boxed{
\begin{aligned}
\text{Paper I}
&\longrightarrow
\text{Paper II},\
\text{Paper I}
&\longrightarrow
\text{Paper III},\
\text{Paper I}
&\longrightarrow
\text{Paper IV}.
\end{aligned}}
]

Paper II 可后提供 Paper III 所用的解析工具，但 Paper III 不得依赖未证明解析断言。

---

# 第一部分. Paper I

## 5. Paper I 标题与角色

### 暂定标题

**Arithmetic Expression Geometry I: Foundations**

推荐副标题：

**Sequential Histories, Affine Flow, Torsion, and Contact Geometry**

### 角色

Paper I 建立 AEG 的基础数学对象与仿射几何扇区，同时把该扇区置于更大双边射影理论内。

其目的不是呈现 AEG 所有已知或提议分支。其目的是提供稳定定义、已证明结构结果与 Papers II–IV
所需共同语言。

预期逻辑脊柱是：

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

---

## 6. Paper I 中心论题

Paper I 应建立以下论题：

> 顺序算术表达式承认基于标记脊柱树的历史敏感形式体系。非退化双边算术历史有射影求值，其像
> 生成 (PGL_2(K))，而先前发展的连续 AEG 理论是稳定无穷远点的仿射或 Borel 扇区。该仿射扇区
> 承载自然余循环、一个无穷小流、一个基本双曲实现、全局 torsion 公式、一个接触联络与一个正则
> 零集理论。

此论题必须带适当域、正性、正则性与非退化假设陈述。

Paper I 不得把仿射扇区描述为整个射影 AEG。

---

## 7. Paper I 所需内容

Paper I 必须包含以下分量。

### 7.1 顺序树与标记脊柱历史

Paper I 必须内在定义顺序算术历史。

它必须包括：

* 算术表达式树；
* 内部节点上的依赖偏序；
* 求值顺序唯一性；
* 按单个内部脊柱的顺序树分类；
* 标记累加器或种子；
* 操作数槽位标签；
* 标记单孔语境
  [
  C_{\omega,c}^{(1)}[z]=\omega(z,c),
  \qquad
  C_{\omega,c}^{(2)}[z]=\omega(c,z);
  ]
* 手性词；
* 有界与自由历史；
* 历史复合。

threadlike 表达式的现有非形式定义必须替换或修复，使其与树定向和示例一致。

论文必须区分：

* 平面镜像；
* 操作数槽交换；
* 时间反演；
* 路径逆；
* 语法相等；
* 历史相等；
* 算子相等；
* 端点相等。

镜像不得与反演等同。

---

### 7.2 双边算术的射影语义

Paper I 必须引入非退化双边单孔算术语境的射影语义。

它必须包括：

* 对 (\mathbb P^1(K)) 的作用；
* 射影矩阵表示；
* 除法的显式域限定；
* 普通算术求值与射影延拓的区分；
* 求值映射
  [
  \rho:\operatorname{Hist}^{\pm,\times}_K
  \longrightarrow PGL_2(K);
  ]
* 平移、非零缩放与反演生成 (PGL_2(K)) 的定理；
* 等同
  [
  B_\infty
  ========

  \operatorname{Stab}_{PGL_2(K)}(\infty)
  \cong \operatorname{Aff}(1,K);
  ]
* 当前实指数参数化覆盖正仿射分量而非每个实仿射映射的限定。

本节必须保持简明。它提供仿射理论的全局代数定位；它不发展完整射影商或双赋值理论。

---

### 7.3 仿射余循环

Paper I 必须推导仿射复合公式。

对仿射映射

[
f_i(x)=s_i x+t_i,
\qquad
s_i\neq0,
]

论文应建立：

[
\Phi_n=\prod_{i=1}^n s_i,
]

[
\xi_n
=====

\sum_{i=1}^n
t_i\prod_{j=i+1}^n s_j,
]

与

[
\widehat\xi_n
=============

# \frac{\xi_n}{\Phi_n}

\sum_{i=1}^n
\frac{t_i}{\prod_{j=1}^i s_j}.
]

两个平移坐标必须解释为不同自然余循环：

* 未来缩放或目标框架平移；
* 过去归一化或源框架平移。

论文必须清楚陈述所用乘法与矩阵约定。

---

### 7.4 连续仿射流

Paper I 必须从仿射群或其 Lie 代数推导连续仿射流。

核心方程是：

[
\frac{da}{ds}
=============

\mu\cos\theta
+
\lambda a\sin\theta.
]

等价形式可包括：

[
da=\mu,du+\lambda a,dv,
]

与指定相容度量后，

[
|\nabla a|^2
============

\mu^2+\lambda^2a^2.
]

推导必须区分：

* 左乘与右乘；
* 源与目标框架；
* (g^{-1}dg) 与 (dg,g^{-1})；
* 操作数槽手性与时间插入侧。

Paper I 必须陈述仿射流是射影 Riccati 流

[
\dot z=\beta+\alpha z+\kappa z^2.
]

的 (\kappa=0) 切片。

完整 Riccati 几何不在 Paper I 发展。

---

### 7.5 算术表达式空间

Paper I 必须提供正则算术表达式空间的精确定义。

正则 AES 至少必须指定：

* 光滑流形或曲面 (M)；
* 度量 (g)；
* 赋值函数 (a)；
* 生成元参数 (\mu,\lambda)；
* 流或 eikonal 方程成立所在域。

定义必须区分内在数据与依赖坐标或归一化的数据。

---

### 7.6 基本双曲模型

Paper I 必须构造基本仿射/双曲模型，暂记为 (\mathfrak E_0)。

模型应包括：

[
g_{\mu,\lambda}
===============

\frac{1}{y^2}
\left(
\frac{dx^2}{\mu^2}
+
\frac{dy^2}{\lambda^2}
\right),
\qquad
a(x,y)=-\frac{x}{y}.
]

论文必须证明赋值满足所需流或 eikonal 方程。

它可包括：

* 双曲解释；
* horocyclic 与测地坐标；
* 加法与乘法作用；
* 与仿射群的关系；
* Baumslag–Solitar 型网格关系；
* Laplace 特征函数计算；
* 局部 torsion 面积公式。

优选推导是从仿射群与归一化不变度量，而非把模型作为孤立灵感示例呈现。

Paper I 不得声称全局或共形唯一性定理，除非该定理被完全证明。

---

### 7.7 正则零轨迹

Paper I 必须建立零集基本正则性定理。

若光滑 AES 满足

[
|\nabla a|^2
============

\mu^2+\lambda^2a^2
]

带 (\mu\neq0)，则在 (a^{-1}(0)) 上，

[
|\nabla a|=|\mu|>0.
]

论文必须结论零是正则值且零集是光滑余一维子流形。

对二维 AES，这蕴含正则零集是不相交光滑曲线的并。

论文必须记录推论：

* 无孤立正则零点；
* 无正则零线交叉；
* 无正则分支或合并；
* 内部无正则零分量诞生或死亡。

违反这些结论的任何示例必须分类为奇异、退化、边界诱导、非真或假设之外。

---

### 7.8 奇异算术表达式空间

Paper I 必须引入奇异 AES 的奠基性定义。

奇异 AES 可由数据如

[
(M,S,g,a;\mu,\lambda),
]

表示，其中 (S\subset M) 是闭奇异集且正则 AES 方程在 (M\setminus S) 上成立。

定义必须允许以下一处或多处奇异：

* 赋值函数；
* 度量；
* 参数；
* 坐标图；
* 射影延拓；
* 普通算术求值域。

论文必须区分：

[
Z_{\mathrm{reg}}(a)
\qquad\text{and}\qquad
Z_{\mathrm{sing}}(a).
]

现记为 (\mathfrak E_1) 的孤立零模型只有显式作奇异模型处理且其正则性状态准确陈述时才可留在
Paper I。

---

### 7.9 极小多重零内容

Paper I 应含一个极小多重零示例，仅当它被完全验证。

多重零示例只有论文指定并验证以下才可接受：

1. 域；
2. 度量；
3. 赋值函数；
4. 正则与奇异集；
5. 正则域上的流方程；
6. 零分量的拓扑与个数。

一般 (E_k)、(E_{\log}) 或多重零分类不属于 Paper I。

若无示例当前满足这些验证要求，Paper I 必须陈述问题并把构造推迟到 Paper III。

---

### 7.10 参数零集引理

Paper I 可包括基础参数族构造。

对光滑族

[
a_t:M\to\mathbb R,
]

定义

[
A:M\times I\to\mathbb R,
\qquad
A(p,t)=a_t(p),
]

与总零集

[
\mathcal Z=A^{-1}(0).
]

在确保零集上 (d_p a_t\neq0) 的非退化条件下，Paper I 可证明 (\mathcal Z) 是 (M\times I) 的光滑
余一维子流形。

Paper I 可称此为基本正则零曲面或初步管结果。

Paper I 不得在无 properness 或等价假设下推断全局平凡、同痕不变、紧性或拓扑保持。

完整管理论属于 Paper III。

---

### 7.11 全局 torsion 与 ACS

Paper I 必须保留累积交换空间作为仿射历史的交换 charge 影子。

优选表述比较两个带相容总 charge 或共同线性部分的历史 (\gamma) 与 (\delta)。

相对 torsion 或端点缺陷应定义为

[
\tau(\gamma,\delta)
===================

\nu_x(\gamma)-\nu_x(\delta),
]

带其独立于 (x) 的显式条件。

论文应推导：

* 仿射余循环求值公式；
* 边界积分表示；
* 加权面积表示；
* 关联 Stokes 恒等式。

与时间反演的比较可留作重要特殊情形但不得是唯一一般定义。

ACS 不得被描述为完整表达式空间。它记录交换化 charge 数据且因此是历史演算的商或影子。

---

### 7.12 接触联络与水平微分

Paper I 必须构造局部接触或联络模型：

[
\alpha
======

da-(\mu,du+\lambda a,dv),
]

带水平场

[
D_u=\partial_u+\mu\partial_a,
\qquad
D_v=\partial_v+\lambda a\partial_a.
]

它必须建立：

[
[D_u,D_v]
=========

\mu\lambda\partial_a.
]

论文可定义水平协变微分

[
\delta_HF
=========

# dF-(\partial_aF)\alpha

(D_uF),du+(D_vF),dv.
]

它必须陈述此算子对曲率敏感且一般不幂零：

[
\delta_H^2F
===========

\mu\lambda(\partial_aF),du\wedge dv.
]

中心局部–全局比较应连接：

[
\text{finite affine defect},
\qquad
\text{ACS weighted area},
\qquad
\text{contact curvature}.
]

初级微分表与大量计算基应放附录或 Paper II，除非中心定理所需。

---

## 8. Paper I 所需定理级结果

Paper I 除非含以下结果的严格版本或显式记录为何一项仍待定，不应视为完成：

1. 顺序树分类；
2. 双边语境射影求值；
3. (PGL_2(K)) 生成；
4. 仿射/Borel 扇区识别；
5. 仿射余循环公式；
6. 连续仿射流推导；
7. 基本双曲模型构造与验证；
8. 广义 torsion 或余循环 Stokes 恒等式；
9. 接触曲率恒等式；
10. 正则零轨迹定理；
11. 奠基性奇异 AES 定义；
12. 基础正则参数族零曲面引理，若保留。

每个结果的权威数学状态将单独记录于：

```text
governance/05-mathematical-status.md
```

---

## 9. 排除于 Paper I 的材料

Paper I 不得把以下发展为主要理论。

### 9.1 完整射影凝聚理论

排除：

* 正则双赋值作为主要对象；
* 秩一幂等元分类作为主要定理序列；
* 完整齐次空间塔
  [
  G/H,\qquad G/B_\pm;
  ]
* 主 (H)-丛；
* 概念–谓词语义；
* 射影过程残差；
* 短展望之外的射影 holonomy。

这些属于 Paper IV。

### 9.2 完整解析函数论

排除：

* 完整算术全纯理论；
* Poisson 核；
* Green 函数；
* 最大原理；
* Harnack 不等式；
* Dirichlet 或 Neumann 理论；
* 谱分解；
* 全局延拓定理。

这些属于 Paper II。

### 9.3 完整奇异与管理论

排除：

* 一般 (E_k) 分类；
* 完整 (E_{\log}) 理论；
* 判别式分层；
* 局部分岔分类；
* 零线诞生、死亡、尖点与重连理论；
* 全局管拓扑；
* 穿线；
* 辫单值；
* 纽结不变量；
* Markov 归一化。

这些属于 Paper III。

### 9.4 计算复杂度断言

排除：

* 非交换性单独蕴含负曲率的断言；
* 负曲率单独蕴含指数算法复杂度的断言；
* AEG 证明复杂度下界的断言；
* 表示、时间与空间复杂度的一般等价；
* 仅由图或类比得出的复杂度结论。

这些属于 Paper IV 且需显式状态空间、度量、商映射与成本模型。

---

# 第二部分. Paper II

## 10. Paper II 标题与角色

### 暂定标题

**Arithmetic Expression Geometry II: Hyperbolic Real Function Theory**

推荐副标题：

**Horizontal Operators, Boundary Problems, and Arithmetic Holomorphicity**

### 角色

Paper II 发展 Paper I 所建立正则仿射/双曲空间的解析理论。

它必须回答：

> AEG 的度量、联络与水平算子支持什么真正的实与复函数论？

Paper II 必须从显式选择的解析数据开始。它不得声称仅接触形式唯一决定完整解析结构。

---

## 11. Paper II 所需范围

Paper II 应包括：

* 相容水平度量；
* 定向与近复结构；
* 一阶与二阶水平算子；
* 自然度量与能量形式；
* 形式伴随与域；
* 与双曲 Laplacian 比较；
* (\mathfrak E_0) 上的分析；
* 显式解族；
* 边值问题；
* 调和或扭曲调和理论；
* 算术 Cauchy–Riemann 方程；
* 因式分解恒等式；
* 与经典复分析与双曲调和分析的关系。

至少一个非平凡边界、核、谱或延拓结果必须被证明。

至少一个真正 (a)-依赖解族必须被构造。

---

## 12. Paper II 的排除

Paper II 不得成为：

* 与算术意义无关的接触分析一般导论；
* 多重零拓扑的主要位置；
* 管或纽结理论的主要位置；
* 计算复杂度论文；
* AEG 取代经典复分析的无证明断言的位置。

结点集结果可在解析相关处出现，但全局奇异零分类属于 Paper III。

---

# 第三部分. Paper III

## 13. Paper III 标题与角色

### 暂定标题

**Arithmetic Expression Geometry III: Singular Zero Geometry and Tubes**

推荐副标题：

**Branched Pullbacks, Arithmetic Zero Networks, and Topological Transport**

### 角色

Paper III 发展奇异赋值函数、多重零分量、参数族与总零集的几何与拓扑。

它必须回答：

> 正则性或非退化失败时零集如何改变，参数化零集如何形成管、单值、辫或类纽结结构？

---

## 14. Paper III 所需范围

Paper III 应包括：

* 完整奇异 AES 范畴或分层框架；
* 局部奇异零集模型；
* 正则对奇异零分量；
* 已验证多重零构造；
* (E_k) 计划，若严格化；
* (E_{\log}) 构造，若严格化；
* 参数空间；
* 判别式集如
  [
  \mathcal D
  ==========

  {t:\exists p,\ a_t(p)=0,\ d_pa_t=0};
  ]
* 判别式之外的稳定性；
* 正则管定理；
* properness 与局部平凡；
* 奇异纤维；
* 零分量单值；
* 有理由时的辫表示；
* 穿线构造。

每个显式模型必须指定：

1. 其域；
2. 其度量；
3. 其赋值函数；
4. 其奇异集；
5. 正则轨迹上满足的方程；
6. 零集拓扑；
7. 参数范围；
8. 所有声称不变量的状态。

---

## 15. 纽结理论的条件范围

纽结与辫材料只在严格条件下可进入 Paper III。

纽结论构造只有至少以下之一被证明才可作为主要结果呈现：

* 同痕不变；
* 所需辫或 Markov 移动下不变；
* 良定义单值表示；
* 非由已知更低层表示决定的非平凡不变量；
* 与 Alexander、Burau 或另一已建立不变量的精确比较。

否则纽结材料必须保持为：

* 示例；
* 结构提案；
* 猜想；
* 开放问题。

与纽结的视觉相似不足。

---

## 16. Paper III 的排除

Paper III 不得声称：

* 每个多重零族给纽结；
* 无 properness 管全局平凡；
* 无奇异或非真事件拓扑改变；
* 提议不变量无证明经 Markov 归一化存活；
* 数值示例建立一般分类。

计算复杂度属于 Paper IV。

---

# 第四部分. Paper IV

## 17. Paper IV 标题与角色

### 暂定标题

**Arithmetic Expression Geometry IV: Projective Condensation and Computational Complexity**

推荐副标题：

**From Histories and Quotients to Representation and Cost**

### 角色

Paper IV 发展完整过程到结果商架构并调查历史、算子、几何与语义压缩如何关联表示与计算复杂度。

它必须回答：

> 历史被凝聚为算子、商状态、规范形或端点值时损失什么信息，该损失在什么精确条件下可关联计算
> 资源？

---

## 18. Paper IV 所需范围

Paper IV 应包括：

* 完整历史范畴或群胚；
* 射影求值；
* 群值相对缺陷；
* 双赋值；
* 点–谓词对偶；
* 秩一幂等元；
* 齐次空间塔
  [
  G\to G/H\to G/B_\pm;
  ]
* 主丛解释；
* 射影凝聚；
* 商纤维；
* 规范形；
* 重写与归一化；
* 语法、词、表示、几何、时间与空间复杂度；
* 词球增长；
* 多项式对指数增长；
* 可证明处的拟等距比较；
* 资源或石子游戏模型；
* 时间–空间折中；
* 显式算法案例研究。

论文必须作复杂度断言前陈述成本模型。

每个复杂度结果必须指定：

* 状态空间；
* 生成元集；
* 等价或商；
* 度量；
* 编码；
* 计算模型；
* 被测资源。

---

## 19. Paper IV 的排除

Paper IV 不得无证明断言：

[
\text{noncommutativity}
\Rightarrow
\text{hyperbolicity},
]

[
\text{hyperbolicity}
\Rightarrow
\text{exponential time},
]

或

[
\text{expression growth}
\Rightarrow
\text{NP-hardness}.
]

这些蕴含需附加假设且一般不作无条件陈述成立。

Paper IV 必须区分：

* 群增长；
* 表示空间增长；
* 搜索树增长；
* 算法运行时间；
* 内存使用；
* 下界复杂度。

对热力学、时空、质量或曲率的类比可激励定义但不得取代它们。

---

# 第五部分. 跨论文分配

## 20. 权威概念分配

| 概念 | Paper I | Paper II | Paper III | Paper IV |
| --- | --- | --- | --- | --- |
| 表达式树 | 奠基性 | 继承 | 继承 | 继承 |
| 顺序树分类 | 主要结果 | 引用 | 引用 | 引用 |
| 标记脊柱历史 | 主要对象 | 继承 | 继承 | 主要历史输入 |
| 双边 (PGL_2) 生成 | 简明主定理 | 引用 | 引用 | 充分发展 |
| 仿射/Borel 扇区 | 主要设置 | 解析设置 | 局部设置 | 与射影扇区比较 |
| Riccati 完备化 | 简要定位 | 可能解析扩张 | 可能奇异动力学 | 完整射影语境 |
| 仿射余循环 | 主要结果 | 解析输入 | 传输输入 | 复杂度/凝聚输入 |
| 仿射流 | 主要结果 | 主要解析背景 | 局部族方程 | 几何成本模型 |
| 基本双曲模型 | 主要示例 | 主要解析背景 | 正则比较模型 | 度量示例 |
| ACS | 主要全局 charge 影子 | 可选解析使用 | 可能不变量源 | 商/凝聚示例 |
| Torsion | 主要局部–全局不变量 | 算子耦合 | 管或奇异不变量 | 相对过程缺陷 |
| 接触联络 | 主要结果 | 算子基础 | 管几何输入 | holonomy 输入 |
| 水平复结构 | 排除作主要理论 | 主要解析选择 | 可选工具 | 非主要 |
| 算术全纯性 | 排除于主体 | 主要理论 | 可选构造工具 | 非主要 |
| 正则零轨迹定理 | 主定理 | 结点输入 | 奠基输入 | 非主要 |
| 奇异 AES | 奠基定义 | 局部解析使用 | 主要理论 | 可能奇异商示例 |
| 多重零模型 | 至多一个验证示例 | 可选解析示例 | 主要理论 | 非主要 |
| 参数零曲面 | 基础引理 | 可选 | 主管理论 | 非主要 |
| 管拓扑 | 超出基础引理排除 | 非主要 | 主要理论 | 可能状态空间示例 |
| 辫与纽结结构 | 排除 | 排除 | 条件主要理论 | 非主要 |
| 双赋值/投影子理论 | 排除 | 可选展望 | 可选表示工具 | 主要理论 |
| 凝聚 | 仅简要展望 | 非主要 | 可能几何示例 | 主要理论 |
| 计算复杂度 | 排除作结论 | 排除 | 排除 | 主要理论 |

此表权威除非本文档修订。

---

# 第六部分. 迁移规则

## 21. 移动当前材料的规则

当前仓库含属若干未来论文的材料。

重组期间：

* 材料必须移动，非静默删除；
* 必须选择一个规范目的地；
* Paper I 只保留连续性所需最少陈述；
* 完整重复理论不得留在多篇论文；
* 标签与引用必须更新；
* 迁移材料必须记录。

预期迁移包括：

* 算术全纯性与关联算子计算到 Paper II；
* 多重零构造、(E_k)、(E_{\log})、奇异族与管材料到 Paper III；
* 双赋值、投影子理论、商塔、射影凝聚与复杂度材料到 Paper IV。

精确文件级映射维护于：

```text
governance/04-current-to-target-map.md
```

---

## 22. 附录处理

Paper I 附录可含：

* 坐标计算；
* 详细仿射余循环推导；
* 扩展 ACS 示例；
* 接触形式计算；
* 基本双曲模型证明细节；
* 正则零集计算；
* 分离相等或中性概念的补充示例。

附录不得用于在 Paper I 内藏第二篇论文。

若附录发展独立理论，必须移到适当后续论文。

---

# 第七部分. 数学论断纪律

## 23. 所需论断状态

重组期间考虑的每条实质论断必须赋以下之一：

* `proved`；
* `proved with stated hypotheses`；
* `standard consequence requiring an in-paper proof`；
* `computationally verified example`；
* `partially proved`；
* `structural proposal`；
* `conjecture`；
* `open problem`；
* `unsupported and excluded`。

每个结果当前状态必须维护于：

```text
governance/05-mathematical-status.md
```

无重组任务可静默提升论断到更强状态。

---

## 24. 显式禁止的推断

以下推断无独立证明不授权：

[
\text{noncommutativity}
\Rightarrow
\text{negative curvature};
]

[
\text{negative curvature}
\Rightarrow
\text{algorithmic hardness};
]

[
\text{multiple zero lines}
\Rightarrow
\text{knot structure};
]

[
\text{tube picture}
\Rightarrow
\text{isotopy invariant};
]

[
\text{symmetry of a model}
\Rightarrow
\text{uniqueness};
]

[
\text{projective continuation}
\Rightarrow
\text{ordinary arithmetic regularity};
]

[
\text{contact distribution}
\Rightarrow
\text{unique complex structure};
]

[
\text{numerical experiment}
\Rightarrow
\text{general theorem}.
]

讨论这些想法之一时，除非有证明，必须标为提案、猜想或开放计划。

---

# 第八部分. 完成判据

## 25. Paper I 完成判据

Paper I 只有以下条件满足才为数学审查就绪：

1. 基础对象一致定义；
2. 顺序树定理证明；
3. 射影双边语义带域限定陈述；
4. (PGL_2) 生成证明；
5. 仿射/Borel 扇区精确识别；
6. 余循环公式证明；
7. 仿射流带显式约定推导；
8. 基本双曲模型验证；
9. 正则零轨迹定理证明；
10. 奇异 AES 定义；
11. ACS torsion 定理以一般双历史形式呈现或其限制显式合理化；
12. 接触曲率证明；
13. 解析、管、射影凝聚与复杂度材料已迁移或约化为纪律性展望陈述；
14. PDF 构建无未解析引用或缺失引用；
15. 摘要与结论不断言强于正文所证。

---

## 26. Papers II–IV 计划判据

Papers II–IV 初始可作为结构化大纲或部分草稿存在。

它们不得仅因材料被迁移进去即视为已建立论文。

每个必须含：

* 声明范围；
* 定理依赖清单；
* 数学状态表；
* 已证明结果与研究计划的分离；
* 显式完成判据。

---

# 第九部分. 变更控制

## 27. 修订本范围

本文档只可由显式范围变更任务修订。

修订必须陈述：

1. 旧规则；
2. 提议新规则；
3. 数学理由；
4. 受影响论文；
5. 所需迁移；
6. 对定理依赖的影响；
7. 对当前草稿的影响。

例行编辑不得隐式改变四论文架构。

---

## 28. 不确定下的默认决定

当材料属 Paper I 还是后续论文不清时，用以下测试。

材料属 Paper I 仅当它需定义或证明以下之一：

* 顺序历史形式体系；
* 仿射扇区的射影定位；
* 仿射余循环；
* 仿射流；
* 基本正则 AES；
* 基本双曲模型；
* 正则零集理论；
* 奠基性奇异 AES 术语；
* 全局仿射 torsion；
* 接触联络与曲率。

发展分析、奇异分类、管拓扑、射影商、凝聚或复杂度的材料属 Papers II–IV。

当不确定仍存：

* 保留材料；
* 移到最可能后续论文草稿；
* Paper I 留短前向引用；
* 问题记录于 `governance/08-open-questions.md`。

---

## 29. 最终范围摘要

四论文系列固定如下：

[
\boxed{
\begin{array}{ll}
\textbf{Paper I:} &
\text{objects, histories, affine/projective placement, flow,}\
&
\text{basic space, torsion, contact curvature, and zero-set boundary};[2mm]

\textbf{Paper II:} &
\text{horizontal and hyperbolic real analysis, boundary theory,}\
&
\text{and arithmetic holomorphicity};[2mm]

\textbf{Paper III:} &
\text{singular assignment functions, multi-zero geometry,}\
&
\text{discriminants, tubes, monodromy, and conditional knot theory};[2mm]

\textbf{Paper IV:} &
\text{full projective condensation, quotient structures,}\
&
\text{representation growth, and computational cost}.
\end{array}}
]

Paper I 必须保持奠基且克制。其成功不由它提及多少 AEG 方向衡量，而由 Papers II–IV 能否依赖它
而不重定义其对象、修复其约定或削弱其论断衡量。

---

## 30. 算术–自守零网络修正案

以下跨论文接口自 2026-08-06 授权：

[
\text{restricted arithmetic histories}
\longrightarrow G_4
\longrightarrow \text{regular holomorphic pullback}
\longrightarrow \text{singular automorphic zero network}.
]

其拥有权固定如下。

### Paper I

Paper I 可证明射影语境

[
T_{\sqrt2}(z)=z+\sqrt2,
\qquad
J(z)=-1/z
]

生成 (\operatorname{PGL}_2(\mathbb Q(\sqrt2))) 的 (q=4) Hecke 三角子群。这是过程到算子商的
算子级示例。Paper I 必须保留字面历史、标记历史、射影算子、Hecke 群元、稳定子陪集与普通可允许
端点之间的区分。它不得把 Hauptmodul、dessins 或奇异零网络发展为 Paper I 理论。

Paper I 还拥有完备正则分裂定理：在带 (\mu\ne0) 的连通、完备、无边正则 AES 上，矫正赋值有单位
梯度且其完备流给

[
M\cong Z(a)\times\mathbb R.
]

结论是光滑非必 Riemannian 乘积。它蕴含这些假设下零层非空连通，并供激励奇异自守模型的全局
no-go 边界。

### Paper II

Paper II 拥有正则解析拉回接口。它可证明平面与柱面目标 AES 公式及其在全纯局部微分同胚下保持。
它必须陈述临界点、退化拉回度量、锥完备化与分支零集在正则轨迹之外且于 Paper III 处理。

### Paper III

Paper III 拥有：

* 全纯分支拉回奇点；
* (2m) 支与 (2\pi m) 锥局部定理；
* 归一化 ((2,4,\infty)) Hecke–Hauptmodul 零网络模型；
* 符号等变赋值及其线丛或指标二下降；
* 算术相对零除子、其归一化、判别式与几何单值；
* 提议的历史到相对除子函子。

末项在构造尊重声明历史等价、复合、定义域与参数基的函子前仍是结构提案。自守模型不得被宣传为
对全部 AEG 历史的此函子。

### 论断边界

本修正案不授权任何断言：

* 全部历史与瓦片或零支双射；
* 任意复零网络是数论的；
* 射影相等蕴含普通算术可允许性；
* (q=4) 模型在 (\mathbb Z[\sqrt2]) 供非唯一分解；
* 奇异零网络自动给真管、有限辫或纽结不变量。

详细证明与状态台账维护于
`governance/discussions/arithmetic-automorphic-zero-networks.md` 与数学状态登记。

---

## 31. 符号覆盖纽结与有限寄存器自然性修正案

以下两个下游扩展自 2026-08-06 授权。

### q=4 算子到纽结接口

Paper III 可从 (q=4) Hecke 算子商过渡到双曲单位切丛。对射影算子本原双曲的标记历史，它可定义
关联定向测地流周期轨道。映射允许穿过射影共轭分解，其导致的原始与标记历史坍缩必须显式陈述。

同一 Paper III 模型可用声明尖点紧化与打印周边斜率计算把符号特征覆盖等同为

[
T^1(\ker\chi\backslash\mathbb H)\cong S^3\setminus T(2,4).
]

零 dessin 可用作引用测地模板的一维编码脊柱。它不得被称为三维模板、零管或纽结。经典测地编码、
模板同痕、透镜空间紧化与尖点环绕公式必须作为外部输入引用。

### 提供寄存器除子接口

Paper III 可从显式提供的带型代数寄存器构造有限相对端点除子，含 (u^2=t) 与塔
(v^2=3)、(u^2=t+v)。它可对这些声明族证明等变、算术与几何不可约、判别式、单值、惰性与
Frobenius 陈述。它还可保留时间标记前缀迹与普通极点除子作为计算图装饰。

本修正案不把那些提供寄存器转换为 Paper I 四语境文法输出。穿过射影求值分解的末端端点除子非
历史忠实。一般历史到相对素除子函子仍开放直到寄存器源、历史等价、复合与非平凡迹数据下降被
构造。

### 附加论断边界

本修正案不授权断言：

* 局部四支度量芽有链环 (T(2,4))；
* 平坦粗柱面与双曲 orbifold 单位切丛是同一几何载体；
* 本原 Hecke 元对应素纽结；
* 历史到周期轨道映射单射；
* 引用 Hecke 环绕公式或模板是新 AEG 纽结不变量；
* 二次或四次寄存器由每个算术历史规范生成；
* 标记迹自动在表达式等价、环境同痕或 Markov 移动下不变。

---

## 32. 切片间多项式关系与水平核残差

Paper III 可以两种相容方式使用提供多项式族 (P(z,t))：实方程 (operatorname{Im}P=0) 定义零载体，
复方程 (P=0) 定义含于该载体的有限根线。此接口只在总光滑性、边界整齐、纤维式奇异层、根平方自由
与 properness 分别检查时授权。

对 (P_m(z,t)=z^2-t^m)、(tin S^1)、(mge 1) 与半径 (R>1) 的盘，Paper III 可证明：

* 载体是带四个边界分量、(2m) 个 Morse 鞍点、Euler 特征 (-2m) 与亏格 (m-1) 的紧连通光滑整齐
  关联；
* 其切片度量是带声明本质中心与 (4pi) 锥完备化的奇异 AES 度量；
* 根线是带闭包 (T(2,m)) 的闭辫 (sigma_1^m)；
* 算术素分量、线分量与链环分量由 (gcd(2,m)) 计数；
* 判别式阶、对数周期、辫指数、负半 Euler 特征与载体框架周期与打印符号约定一致。

载体投影因鞍点非真零管。辫指数与载体框架是呈现或平凡化级数据，非 Markov 不变量。

对 (m=4)，提升 q=4 尖点斜率与覆盖作用可用于导出周边环面除子 (u^2=t^4)，直到有序子午标记、
Laurent 单位、定向与特征规范。把该环面除子径向延伸到亏格三载体是附加提供数据。普通纯辫扩张
不与 q=4 单位切中心扩张或 Paper I 仿射 torsion 等同。

保留归一化 Hauptmodul、残差 orbifold 标记、覆盖对合与两个尖点，Paper III 可在复数上加强周边
陈述。紧化符号覆盖是标记加权对 (mathbb P(2,1),V(U^2-V^4))；其对数正切是 (mathcal O(-1))，其分次
截面环由权一与权二生成，尖点截面是四次二项式。加权 Hopf 圆丛给标准尖点填充与 (T(2,4)) 链环。
这是分次同构陈述，非预先存在仿射平面中的无坐标相等。在 (mathbb Q(sqrt2)) 上，分裂负形与非分裂
正形是常二次扭曲；两者算术下降在标记声明前都不得称规范。对数锥坐标不自动是径向载体外部切片
参数。

Paper III 还可记录四股中心扩张校准。对提供 Garside 半扭与四点旋转路径，两个 q=4 椭圆关系子有
相同全扭残差，且 (B_4) 中心扩张拉回在打印定向约定后与单位切中心扩张一致。自由词算子核上所得
共轭不变整数特征在 Lyndon–Hochschild–Serre 五项序列中有等于单位切 Euler 扩张类的推出类。这是
真正群扩张 transgression，非圆基上的 Serre transgression，该特征非 Paper I 仿射 torsion。这不
证明那些系数路径由无限制标记历史产生、不要求单射断言、不把逆全扭闭包 (T(4,-4)) 与 q=4 尖点
链环 (T(2,4)) 等同。

正确信息损失陈述是正合序列

[
1\longrightarrow P_2\longrightarrow B_2\longrightarrow S_2\longrightarrow1.
]

在 (m=4)，置换单值平凡而纯辫坐标与互相环绕数为二。未来历史到路径函子必须作用于完整标记系数
路径并通过中性词测试；在末端射影求值后附着此残差不被授权为自然性定理。

---

## 33. 有界六次 Lyashko–Looijenga 实验室

迁移 M-0008 授权一个基于提供首一中心六次的有界 Paper III 实验室

[
P_0(x)=x^6-x.
]

Paper III 可直接计算其临界值多项式、证明五个显示局部半扭形成生成 (B_6) 的跨星，并对无碰撞环
构造相容实载体、六根线与亏格二分支覆盖映射环面。它还可证明混合临界值/测试参数正合序列模型并
把引用算术判据特化到纤维 (y^2=x^6-x-1)。

以下仍是引用经典输入而非新 AEG 定理：

* 正则 Lyashko–Looijenga 映射的有限与平展性及其度；
* 焦散与 Maxwell 重数；
* 转置因式分解计数与局部 Picard–Lefschetz 单值；
* Birman–Hilden 提升与亏格二辛单值；
* 用于显示算术纤维的不可约、Galois 群与超椭圆自同态判据。

计数 (6^4=1296) 指归一化首一中心 LL 叶。自由残差 (\mu_6) 源旋转给 (216) 轨道。两数都不被授权为
两两非同构亏格二曲线计数。

两个辫层必须保持带型。临界值传输经 LL 覆盖作用，而测试参数运动供垂直 (F_5) 然后六根辫。其接口
是

[
1\longrightarrow F_5\longrightarrow B_{5,1}\longrightarrow B_5
\longrightarrow1
]

沿 LL 覆盖的拉回，或等价 Hurwitz 群胚。遗忘 LL 叶不授权同态 (B_5\to B_6)。

六次载体可有鞍墙且不因此是真零管。载体墙穿越、根碰撞、临界值碰撞与奇异超椭圆纤维不得等同。
同样，共同抽象目标 (\operatorname{Sp}_4(\mathbb F_2)\cong S_6) 不规范等同算术 Frobenius 元与
拓扑环。

来源修正案 M-0009 额外授权显式几何 LL–Igusa 孪生定理。显示的第二个首一中心六次与 (P_0) 有相同
事件多项式 (Q_0)、位于其残差 (\mu_6) 轨道之外，且在 (t=1) 有不同绝对 Igusa–Clebsch 比。Paper III
因此可陈述亏格二模读数在此纤维上不穿过 LL 事件多项式因式分解。这是 P3-L9 且是直接精确计算，
非经典 LL 定理。

P3-L9 还授权两个有界直接推论。第一，度 (216) 源旋转商承载叶可观测量的范谱多项式、迹–范与
对称函数下降与规范分裂平均序列。其零和范是带 (Q_0) 处打印精确正下界的非负单值不变有限纤维
方差。此环不变性不得加强为沿 LL 基任意开路径恒常。第二，沿两条显示 (t) 铅笔，比
((t-\beta)/t)^5 在两个正则纤维有除子 (5[\beta]-5[0])。其平衡对数残差非有限 Dirichlet 能量。

以下仍开放：

* 完整 (216) 轨道模普查、算术/Frobenius 与周期比较、更强标记单值/Hurwitz 孪生测试与任何 Hodge-
  或 Siegel-度量能量比较（P3-L10）；
* 从无限制 AEG 历史到规范六次、LL 叶、混合辫路径或六根辫的任何函子；
* 此奇异载体的真零管定理；
* 从实验室提取的 Markov 下降或新纽结不变量。

故 P3-L1–P3-L9 仅以其提供/计算对经典输入状态显示时授权，而 P3-L10 与一般历史自然性箭头仍开放。
计数 (1296) 与 (216) 仍是叶/轨道计数，非曲线计数；P3-L9 只证明模像至少含两点。
