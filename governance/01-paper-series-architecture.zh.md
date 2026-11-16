# AEG 论文系列架构

**文件：** `governance/01-paper-series-architecture.md`
**状态：** 权威
**版本：** 1.1
**日期：** 2026-08-06
**依赖：** `governance/00-authoritative-scope.md`
**适用于：** 算术表达式几何系列 Papers I–IV

**后续槽位。** Papers V 与 VI 由其自身范围文件 `governance/00c-paper-V-triadic-aperture-scope.md`
与 `governance/00e-paper-VI-process-geometry-scope.md` 支配。本文档对 Papers I–IV 仍权威且既不
约束也不描述后续槽位。

---

## 1. 目的

本文档定义算术表达式几何系列前四篇论文之间的架构关系。

它指定：

* 论文间依赖图；
* 每篇论文拥有的数学对象；
* 后续论文依赖先前论文所经接口；
* 共享记号与约定；
* 导入、扩展或替换先前定义的规则；
* 现有仓库材料的迁移；
* 结果可跨论文引用的条件。

本文档不取代每篇论文的详细范围。权威范围仍是：

```text
governance/00-authoritative-scope.md
```

此处目的是确保四篇论文形成一个连贯研究计划而非四篇部分重叠的阐述。

---

## 2. 系列级论题

前四篇论文研究一个过程到结果架构的连续层：

[
\boxed{
\text{syntax}
\longrightarrow
\text{history}
\longrightarrow
\text{operator}
\longrightarrow
\text{geometry}
\longrightarrow
\text{quotient or observable}.
}
]

四篇论文划分此架构如下：

[
\begin{array}{ll}
\textbf{Paper I:} &
\text{foundational objects and the affine geometric sector};[2mm]
\textbf{Paper II:} &
\text{analysis on the regular affine/hyperbolic geometry};[2mm]
\textbf{Paper III:} &
\text{singular zero geometry and parameterized topology};[2mm]
\textbf{Paper IV:} &
\text{projective quotients, condensation, and complexity}.
\end{array}
]

论文必须保留以下层次之间的区分：

[
\text{expression tree}
\longrightarrow
\text{marked spinal history}
\longrightarrow
\text{projective or affine operator}
\longrightarrow
\text{assignment state}
\longrightarrow
\text{endpoint value}.
]

后续论文可商、丰富或分析先前对象，但不得静默等同两个不同层次。

---

## 3. 全局依赖图

主论文依赖图是：

[
\boxed{
\begin{tikzcd}[column sep=large,row sep=large]
& \text{Paper II: Hyperbolic Analysis}
\
\text{Paper I: Foundations}
\arrow[ur]
\arrow[r]
\arrow[dr]
&
\text{Paper IV: Projective Condensation and Complexity}
\
& \text{Paper III: Singular Zeros and Tubes}
\end{tikzcd}
}
]

普通形式：

```text
Paper I ──→ Paper II
Paper I ──→ Paper III
Paper I ──→ Paper IV
```

后续可用次级依赖：

```text
Paper II ──→ selected analytic tools in Paper III
```

此次级依赖可选。Paper III 不得依赖 Paper II 的未证明或未发表解析定理，除非该定理被复现或条件
陈述。

无所需依赖：

```text
Paper III ──→ Paper IV
```

或

```text
Paper IV ──→ Paper II.
```

可加交叉引用，但主定理架构必须保持无环。

---

## 4. 架构层

系列组织为四层。

### 层 A：历史语法

对象：

* 算术表达式树；
* 依赖偏序；
* 顺序树；
* 标记脊柱历史；
* 手性词；
* 单孔语境；
* 历史复合；
* 时间反演；
* 镜像；
* 路径逆。

拥有者：

```text
Paper I
```

所有后续论文继承这些定义。

---

### 层 B：算子语义

对象：

* 仿射变换；
* Möbius 变换；
* 射影求值；
* 仿射余循环；
* 相对算子缺陷；
* 仿射/Borel 扇区；
* 射影完备化。

主要拥有者：

```text
Paper I: foundational semantics
Paper IV: full quotient and condensation theory
```

Paper I 定义定位仿射理论所需算子语义。Paper IV 发展完整射影与商推论。

---

### 层 C：几何实现

对象：

* 算术流；
* 赋值函数；
* 正则 AES；
* 基本双曲模型；
* ACS；
* torsion；
* 接触联络；
* 水平微分；
* 零轨迹。

主要拥有者：

```text
Paper I
```

扩展：

```text
Paper II: analytic geometry
Paper III: singular and parametric geometry
Paper IV: metric and quotient complexity
```

---

### 层 D：导出结构

对象：

* 水平调和分析；
* 算术全纯性；
* 奇异层；
* 管几何；
* 单值；
* 射影凝聚；
* 复杂度度量。

拥有者：

```text
Paper II: analysis
Paper III: singular topology
Paper IV: quotient and complexity
```

这些对象必须用 Paper I 导出的接口定义。

---

# 第一部分. 论文拥有权

## 5. Paper I 拥有权

Paper I 拥有以下内容的规范定义：

* 顺序算术树；
* 标记脊柱历史；
* 手性词；
* 单孔算术语境；
* 普通算术求值；
* 射影求值；
* 仿射扇区；
* 仿射余循环；
* 算术流；
* 正则算术表达式空间；
* 基本双曲模型；
* 正则零轨迹；
* 奠基性奇异 AES；
* ACS；
* 相对仿射 torsion；
* 算术接触联络；
* 水平协变微分。

后续论文必须引用或导入这些定义而非重新引入竞争版本。

Paper I 还拥有与这些定义关联的记号与假设，除非扩展被显式声明。

---

## 6. Paper II 拥有权

Paper II 拥有以下内容的规范定义：

* 相容水平度量；
* 水平定向；
* 相容近复结构；
* 水平体积形式；
* 解析域与函数空间；
* 水平 Laplacian；
* 形式伴随算子；
* AEG Dirichlet 与 Neumann 问题；
* 算术调和性；
* 扭曲调和性；
* 算术 Cauchy–Riemann 算子；
* 算术全纯性；
* 解析核与延拓结果。

Paper II 不得重定义接触分布或仿射流。

它可给 Paper I 结构加解析数据：

[
(M,g,a,\alpha,\mathcal H)
\quad\leadsto\quad
(M,g,a,\alpha,\mathcal H,g_H,J,d\mathrm{vol}_H).
]

此丰富必须显式陈述。

---

## 7. Paper III 拥有权

Paper III 拥有以下内容的规范定义：

* 分层奇异 AES；
* 奇异零芽；
* 多重零模型；
* 零集判别式；
* 参数空间正则层；
* 正则零管；
* 奇异纤维；
* 零分量单值；
* 辫传输；
* 穿线；
* 任何严格定义的纽结相关不变量。

Paper III 扩展 Paper I 的奠基性奇异 AES 定义。

它不得重定义正则 AES 或正则零轨迹。

扩展应有形式：

[
(M,S,g,a;\mu,\lambda)
\quad\leadsto\quad
(M,\mathcal S,g,a;\mu,\lambda),
]

其中 (\mathcal S) 是指定分层或奇异结构。

---

## 8. Paper IV 拥有权

Paper IV 拥有以下内容的规范定义：

* 历史范畴或群胚；
* 求值函子；
* 算子核对；
* 射影相对缺陷；
* 双赋值；
* 点–谓词传输；
* 秩一幂等元表示；
* 商塔；
* 凝聚映射；
* 商纤维复杂度；
* 规范代表复杂度；
* 表示复杂度；
* 几何复杂度；
* 计算成本模型；
* 时间与空间复杂度比较。

Paper IV 必须复用 Paper I 引入的射影求值。

它可把算子级对象从：

[
\operatorname{Aff}(1,K)
]

扩大到：

[
PGL_2(K)
]

且可研究商结构如：

[
G/H,\qquad G/B_\pm.
]

---

# 第二部分. 导出接口

## 9. Paper I 导出接口

Paper I 向所有后续论文导出以下数据。

### 9.1 语法接口

标记脊柱历史示意表示为：

[
\gamma
======

\bigl(
x_0;
(\omega_i,c_i,\varepsilon_i)_{i=1}^{n}
\bigr),
]

带：

[
\varepsilon_i\in{1,2}.
]

语法接口包括：

* 历史长度；
* 手性词；
* 语境复合；
* 有界与自由历史；
* 可允许条件；
* 时间反演；
* 路径逆。

---

### 9.2 算子接口

射影求值：

[
\rho:
\operatorname{Hist}^{\pm,\times}_K
\longrightarrow
PGL_2(K).
]

仿射限制：

[
\rho_{\mathrm{aff}}:
\operatorname{Hist}^{\mathrm{aff}}_K
\longrightarrow
\operatorname{Aff}(1,K).
]

算子接口必须指定：

* 域假设；
* 可逆性假设；
* 域限制；
* 普通对射影语义；
* 年代复合约定。

---

### 9.3 余循环接口

对：

[
\rho_{\mathrm{aff}}(\gamma)(x)
==============================

\Phi_\gamma x+\xi_\gamma,
]

Paper I 导出：

[
\Phi_{\gamma\delta}
===================

\Phi_\delta\Phi_\gamma,
]

带论文所述精确复合约定，与对应平移余循环律。

它还导出源归一化坐标：

[
\widehat\xi_\gamma
==================

\Phi_\gamma^{-1}\xi_\gamma.
]

后续论文不得无显式转换交换 (\xi) 与 (\widehat\xi)。

---

### 9.4 流接口

Paper I 导出仿射流方程：

[
\frac{da}{ds}
=============

\mu\cos\theta+\lambda a\sin\theta.
]

坐标形式：

[
da=\mu,du+\lambda a,dv.
]

指定相容度量时：

[
|\nabla a|_g^2
==============

\mu^2+\lambda^2a^2.
]

后续论文必须陈述它们假设哪种表述。

---

### 9.5 正则 AES 接口

正则 AES 必须至少包括：

[
\mathfrak E
===========

(M,g,a;\mu,\lambda),
]

连同定义方程成立所在声明域。

Paper I 必须指定是否：

* (\mu,\lambda) 是常量；
* (\mu,\lambda) 可变；
* (M) 连通；
* (M) 有边；
* (g) 完备；
* (a) 全局定义。

后续论文不得静默添加这些性质。

---

### 9.6 零集接口

Paper I 导出：

[
Z(a)=a^{-1}(0),
]

与奇异设置中：

[
Z_{\mathrm{reg}}(a),
\qquad
Z_{\mathrm{sing}}(a).
]

正则零定理只在所述假设下适用，包括：

[
\mu\neq0.
]

Paper III 必须精确识别那些假设失败处。

---

### 9.7 ACS 接口

Paper I 导出：

* 加法 charge (A)；
* 乘法对数 charge (M)；
* ACS 路径 (C_\gamma)；
* 总 charge 映射；
* 加权一形式；
* 相容历史相对 torsion。

精确符号与定向约定必须固定一次并复用。

---

### 9.8 接触接口

Paper I 导出：

[
\alpha
======

da-(\mu,du+\lambda a,dv),
]

[
\mathcal H=\ker\alpha,
]

[
D_u=\partial_u+\mu\partial_a,
\qquad
D_v=\partial_v+\lambda a\partial_a,
]

[
[D_u,D_v]
=========

\mu\lambda\partial_a.
]

它还导出：

[
\delta_HF
=========

(D_uF),du+(D_vF),dv.
]

Paper II 可给 (\mathcal H) 装备附加解析结构。Paper III 可把 (\mathcal H) 拉到管或奇异层。Paper
IV 可把括号或 holonomy 解释为过程残差。

---

## 10. Paper II 导入契约

Paper II 可假定以下 Paper I 结果：

* 正则仿射 AES 框架存在；
* 基本双曲模型；
* 接触分布；
* 水平场；
* 曲率括号；
* 正则零定理；
* 仿射流。

Paper II 不得假定：

* 规范水平复结构；
* 任何算子本质自伴；
* Green 或 Poisson 核存在；
* 边界正则性；
* 谱完备性；
* 全局函数论。

这些必须在 Paper II 建立。

---

## 11. Paper III 导入契约

Paper III 可假定：

* 正则与奇异 AES 术语；
* 正则零定理；
* 基础参数族零曲面引理；
* 仿射流；
* 接触联络；
* 基本双曲模型。

Paper III 不得假定：

* 零族全局 properness；
* 奇异参数间拓扑保持；
* 零分量有限；
* 全局管存在；
* 辫或纽结不变；
* 所有奇点正规形。

这些必须证明或作为假设施加。

---

## 12. Paper IV 导入契约

Paper IV 可假定：

* 标记脊柱历史；
* 射影求值；
* (PGL_2) 生成；
* 仿射/Borel 限制；
* 仿射余循环；
* 相对仿射缺陷；
* 历史、算子与端点值的区分。

Paper IV 不得假定：

* 每个历史商有规范代表；
* 最短代表可计算；
* 商距离等于计算成本；
* 指数群增长蕴含计算困难性；
* 几何曲率给复杂度下界。

这些是 Paper IV 的研究问题。

---

# 第三部分. 共享记号

## 13. 基域与数系

用：

[
K
]

表一般域。

用：

[
\mathbb R
]

表实微分几何。

用：

[
\mathbb C
]

表复化或解析理论。

用：

[
\mathbb F_q
]

表有限域模型。

一般域上的定理不得无限定用解析指数或实微分演算。

记号：

[
e^\lambda
]

保留给特征零实或复设置，除非形式引入。

---

## 14. 表达式与历史

推荐记号：

[
T
]

表表达式树。

[
I(T)
]

表内部节点依赖偏序。

[
\gamma,\delta
]

表历史。

[
\varepsilon(\gamma)
]

表手性词。

[
r\gamma
]

表时间反演，若采纳。

[
m\gamma
]

表镜像，若采纳。

[
\gamma^{-1}
]

表路径逆，仅当每个语境可逆。

记号不得重载反演与逆。

---

## 15. 算子

用：

[
\rho(\gamma)
]

表射影求值。

用：

[
\nu_x(\gamma)
]

表历史在初值 (x) 的求值，当普通求值可允许。

用：

[
\operatorname{Aff}(1,K)
]

表仿射群。

用：

[
PGL_2(K)
]

表射影线性群。

用：

[
B_\infty
]

表 (\infty) 的稳定子，除非另一 Borel 记号全局采纳。

用：

[
J(z)=-\frac1z
]

表 Weyl 反演，若该约定保留。

---

## 16. 仿射坐标

对仿射映射：

[
x\mapsto\Phi x+\xi,
]

用：

[
\Phi
]

表累积尺度。

用：

[
\xi
]

表目标框架或未来缩放平移。

用：

[
\widehat\xi=\Phi^{-1}\xi
]

表源归一化平移。

同一论证中不得同时用 (a) 表仿射平移坐标与 AES 赋值场。

---

## 17. AES 记号

用：

[
a
]

表赋值函数或赋值坐标。

用：

[
M
]

表底层流形，仅当与 ACS 乘法坐标无冲突时。

可能混淆处用：

[
\mathcal M
]

表流形并保留：

[
M
]

表乘法 charge。

用：

[
g
]

表 Riemannian 度量。

用：

[
\mathfrak E
]

表一般算术表达式空间。

用：

[
\mathfrak E_0
]

表基本正则双曲模型。

用：

[
\mathfrak E_1
]

仅在其奇异状态与定义已固定后。

不随意重编号 (\mathfrak E_k)。

---

## 18. 流参数

用：

[
\mu
]

表加法强度。

用：

[
\lambda
]

表对数乘法强度。

陈述：

[
\mu,\lambda
]

是否：

* 常量；
* 函数；
* 参数；
* 非零；
* 正。

不从非消失推断正性。

---

## 19. ACS 记号

用：

[
(A,M)
]

表 ACS 坐标：

* (A)：累积加法 charge；
* (M)：累积对数乘法 charge。

用：

[
C_\gamma
]

表 (\gamma) 的 ACS 路径。

用：

[
\Sigma_{\gamma,\delta}
]

表两相容历史间定向填充。

用一个规范记号表加权一形式，优选：

[
\eta.
]

[
d\eta
]

的符号约定必须跨 Papers I、III 与 IV 一致。

---

## 20. 接触记号

用：

[
\alpha
]

表接触形式。

用：

[
\mathcal H=\ker\alpha
]

表水平分布。

用：

[
D_u,D_v
]

表优选水平提升。

用：

[
\delta_H
]

表水平协变微分，除非后编辑决定保留 (\delta)。

若保留 (\delta)，其非幂零性必须在相关处陈述。

用：

[
\Delta_H
]

表水平二阶算子，仅在 Paper II 固定其精确解析定义后。

Paper I 可用形式表达式，但不得过早赋解析性质。

---

## 21. 零集记号

用：

[
Z(a)=a^{-1}(0).
]

用：

[
Z_{\mathrm{reg}}(a)
]

表正则零点。

用：

[
Z_{\mathrm{sing}}(a)
]

表奇异零点。

对族 (a_t)，用：

[
\mathcal Z
==========

{(p,t):a_t(p)=0}
]

表总零集。

用：

[
\mathcal D
]

表参数空间判别式。

不对每个总零集用「管」。保留给满足 Paper III 采纳正则性与局部平凡条件的总零集。

---

## 22. 射影凝聚记号

Paper IV 应用：

[
G=PGL_2(K)
]

除非需更广群。

用：

[
H
]

表有序对或参考结构稳定子。

用：

[
B_\pm
]

表两个特殊射影点存在时的点稳定子。

用：

[
G/H
]

表双赋值或有序对商，仅在稳定子已定义后。

用：

[
\Pi
]

表秩一幂等投影子。

用：

[
\mathcal K(\gamma,\delta)
]

表群值相对缺陷，若保留。

---

## 23. 复杂度记号

Paper IV 应区分：

[
C_{\mathrm{syn}}
]

语法复杂度，

[
C_{\mathrm{word}}
]

词复杂度，

[
C_{\mathrm{op}}
]

算子表示复杂度，

[
C_{\mathrm{geo}}
]

几何复杂度，

[
C_{\mathrm{time}}
]

时间复杂度，

[
C_{\mathrm{space}}
]

空间复杂度。

记号不应假定这些量间任何相等。

若复杂度依赖模型，把模型含于下标或参数。

---

# 第四部分. 共享约定

## 24. 复合约定

系列必须采纳一个年代复合约定。

推荐约定：

若历史 (\gamma) 先应用 (g_1) 后应用 (g_n)，则：

[
\nu_x(\gamma)
=============

g_n\circ\cdots\circ g_1(x).
]

矩阵积必须遵循同约定。

每个用群乘法的论文必须含一个简短约定陈述。

不单独依赖图定向。

---

## 25. 左与右作用

系列必须区分：

* 左群乘法；
* 右群乘法；
* 左 Maurer–Cartan 形式；
* 右 Maurer–Cartan 形式；
* 源框架坐标；
* 目标框架坐标。

无论文可无显式定理把操作数槽手性与左/右群乘法等同。

---

## 26. 普通与射影域

每个射影算术语境必须带域信息。

至少区分：

1. 普通算术域；
2. 射影域；
3. 例外点或极点；
4. 图转换。

射影恒等式不蕴含每个中间普通算术表达式有定义。

---

## 27. 局部与全局陈述

每个结果必须陈述其是：

* 局部；
* 全局；
* 图依赖；
* 仅正则轨迹上定义；
* 仅完备性下有效；
* 仅 properness 下有效；
* 仅紧纤维下有效。

局部接触模型不得提升为全局分类。

局部零曲面结果不得提升为全局管定理。

---

## 28. 精确与无穷小缺陷

系列必须区分：

* 精确有限仿射端点缺陷；
* 相对仿射 holonomy 平移坐标；
* 交换子环漂移；
* 无穷小括号；
* 曲率二形式；
* ACS 加权面积。

这些量可一阶一致而不在有限尺度相等。

该区分必须跨 Papers I、III 与 IV 保留。

---

# 第五部分. 跨论文定理复用

## 29. 先前结果引用

后续论文只有以下条件可引用先前定理：

* 定理已发表或稳定预印本可用；
* 陈述与假设匹配；
* 记号变化显式翻译；
* 不推断更强结论。

若先前结果重组期间改变，依赖草稿必须更新。

---

## 30. 条件导入

若 Paper II、III 或 IV 在 Paper I 定稿前起草，导入结果必须标为：

```text
Assuming Theorem X of Paper I.
```

或：

```text
Conditional on the current formulation of the regular AES theorem.
```

草稿依赖必须跟踪于数学状态文件。

---

## 31. 无循环证明依赖

以下模式禁止：

```text
Paper I cites a theorem proved only in Paper II,
while Paper II assumes Paper I's result to prove that theorem.
```

若结果真正奠基，必须移到 Paper I 或在所需限制形式那里重证。

---

## 32. 共享引理

多篇论文实质使用的技术引理应以三种方式之一处理：

1. 奠基则放 Paper I；
2. 在独立技术笔记证明；
3. 短且标准则在每篇论文带引用重述。

不维护同引理分歧版本。

---

# 第六部分. 材料迁移架构

## 33. 规范目的地

现有仓库材料应赋一个规范目的地。

### Paper I 目的地类

* 表达式语法；
* 标记历史；
* 仿射/射影定位；
* 仿射流；
* (\mathfrak E_0)；
* 正则零；
* ACS；
* torsion；
* 接触几何。

### Paper II 目的地类

* 基础曲率之外的 (\delta)-演算；
* 算术全纯性；
* 扭曲调和性；
* 显式解析基；
* 边值想法；
* 解析核。

### Paper III 目的地类

* 奇异 AES 展开；
* (E_k)；
* (E_{\log})；
* 多重零构造；
* 管结构；
* 穿线；
* 辫与纽结方向。

### Paper IV 目的地类

* 双赋值；
* 投影子；
* 商塔；
* 过程残差；
* 凝聚；
* 资源几何；
* 时间–空间对偶；
* 复杂度案例。

---

## 34. 迁移状态

每个迁移块应有以下状态之一：

* `moved unchanged`；
* `moved and edited`；
* `split across papers`；
* `retained as summary only`；
* `archived as superseded`；
* `discarded as incorrect`。

状态应记录于：

```text
governance/04-current-to-target-map.md
```

无实质材料应无记录状态消失。

---

## 35. 前向引用

Paper I 可含纪律性前向引用如：

* 「相容水平复结构在 Paper II 发展。」
* 「奇异参数轨迹与管拓扑在 Paper III 发展。」
* 「完整射影商塔在 Paper IV 发展。」

前向引用不得把未证明未来结果总结为已确立事实。

---

## 36. 避免重复阐述

材料移动时：

* Paper I 应只保留基础所需最少定义或定理；
* 后续论文应拥有详细发展；
* 相同完整证明不得复制进多篇论文；
* 若论文独立可读可引用共享证明。

---

# 第七部分. 逐论文架构

## 37. Paper I 内部架构

推荐 Paper I 进程：

```text
1. Introduction and architecture
2. Sequential trees and marked spinal histories
3. Projective semantics and the affine sector
4. Affine cocycles
5. Continuous affine flow
6. The basic hyperbolic model
7. Regular and singular zero geometry
8. Global torsion and the ACS
9. Contact connection and horizontal differential
10. Outlook and interfaces to Papers II–IV
```

精确章编号可变，但依赖顺序应保留。

接触几何不得出现在流与仿射余循环基础之前。

零轨迹定理必须出现在正则 AES 与 eikonal 方程定义之后。

---

## 38. Paper II 内部架构

推荐进程：

```text
1. Analytic data added to the Paper I geometry
2. Horizontal metrics, measures, and adjoints
3. First- and second-order operators
4. Analysis on the basic hyperbolic model
5. Harmonic and boundary-value theory
6. Explicit solution families
7. Arithmetic Cauchy–Riemann theory
8. Relation to classical and hyperbolic complex analysis
```

算术全纯性应跟随而非先于实算子理论。

---

## 39. Paper III 内部架构

推荐进程：

```text
1. Singular AES and stratified regular loci
2. Local zero-set singularities
3. Verified multi-zero constructions
4. Parameter spaces and discriminants
5. Regular zero tubes
6. Singular fibers and topology change
7. Monodromy and braid transport
8. Conditional threading and knot invariants
```

纽结材料必须留在判别式与单值理论下游。

---

## 40. Paper IV 内部架构

推荐进程：

```text
1. History categories and evaluation
2. Full bilateral projective semantics
3. Bivaluations and projectors
4. Quotient towers and process residue
5. Condensation and canonical forms
6. Representation growth
7. Geometric and computational cost models
8. Time–space–representation relations
9. Case studies
```

复杂度断言必须出现在商与成本模型固定后。

---

# 第八部分. 架构不变量

## 41. 定义必须跨论文单调

后续论文可丰富先前定义但不得矛盾它。

允许：

[
\text{regular AES}
\longrightarrow
\text{regular AES with analytic data}.
]

允许：

[
\text{singular AES}
\longrightarrow
\text{stratified singular AES}.
]

不允许：

* 改变标记历史含义；
* 无警告反转复合顺序；
* 改变 (\mu) 与 (\lambda) 角色；
* 独立重编号 (\mathfrak E_0) 与 (\mathfrak E_1)；
* 用不相容符号约定重定义 torsion。

---

## 42. 假设必须单调

后续论文可加假设。

例如：

[
\text{smooth AES}
\quad\leadsto\quad
\text{complete smooth AES with bounded geometry}.
]

后续论文不得在丢弃所需假设后引用定理。

---

## 43. 猜想必须保留身份

跨论文出现的猜想应保留：

* 稳定名称；
* 稳定标识符；
* 陈述历史；
* 当前状态。

若修订，新旧形式必须区分。

---

## 44. 示例不得控制定义

无论文应仅为了适配以下而定义一般对象：

* (\mathfrak E_0)；
* 一个 (E_k) 模型；
* 一个管图；
* 一个有限域计数；
* 一个复杂度示例。

定义必须独立于示例陈述其意图一般性。

---

# 第九部分. 架构验证

## 45. 重大重组前所需检查

移动或重写一章前，验证：

1. 哪篇论文拥有材料；
2. 它导入哪些定义；
3. 哪些结果依赖它；
4. 记号是否共享；
5. 当前论断状态是否已知；
6. 移动它是否创建循环依赖；
7. 摘要或结论是否须更新；
8. 目的地论文是否已含竞争版本。

---

## 46. 架构审计所需输出

架构审计应列出：

* 重复定义；
* 冲突记号；
* 循环依赖；
* 定义前使用结果；
* 结果分配给错论文；
* 带更弱假设导入的论断；
* 缺规范目的地的材料；
* 未解决拥有权问题。

审计不得静默修复这些问题。

---

## 47. 系列级完成测试

前四篇论文只有以下条件才形成连贯系列：

1. Paper I 可独立读为基础；
2. Paper II 导入 Paper I 而不重定义几何；
3. Paper III 导入 Paper I 而不重定义正则零；
4. Paper IV 导入 Paper I 而不重定义射影求值；
5. 无主定理有循环依赖；
6. 每个共享符号有一个规范含义；
7. 每个实质仓库笔记有规范目的地或归档状态；
8. 猜想与开放计划与已证明结果清楚分离。

---

# 第十部分. 接口摘要

## 48. 论文接口一览

### Paper I → Paper II

导出：

[
(M,g,a;\mu,\lambda),
\quad
\alpha,
\quad
\mathcal H,
\quad
D_u,D_v,
\quad
[D_u,D_v].
]

Paper II 加：

[
g_H,
\quad
J,
\quad
d\mathrm{vol},
\quad
\Delta_H,
\quad
\partial_{\mathrm{AEG}},
\quad
\bar\partial_{\mathrm{AEG}}.
]

---

### Paper I → Paper III

导出：

[
Z_{\mathrm{reg}}(a),
\quad
Z_{\mathrm{sing}}(a),
\quad
\text{regular-zero theorem},
\quad
\mathcal Z=A^{-1}(0).
]

Paper III 加：

[
\mathcal D,
\quad
\text{singular strata},
\quad
\text{tube topology},
\quad
\text{monodromy}.
]

---

### Paper I → Paper IV

导出：

[
\operatorname{Hist},
\quad
\rho,
\quad
PGL_2,
\quad
B_\infty,
\quad
\Phi,\xi,\widehat\xi,
\quad
\tau.
]

Paper IV 加：

[
G/H,
\quad
G/B_\pm,
\quad
\Pi,
\quad
\text{condensation},
\quad
C_{\mathrm{rep}},
\quad
C_{\mathrm{time}},
\quad
C_{\mathrm{space}}.
]

---

## 49. 最终架构原则

系列必须从一个稳定中心向外发展：

[
\boxed{
\text{history-sensitive arithmetic}
\longrightarrow
\text{operator semantics}
\longrightarrow
\text{geometric realization}.
}
]

Paper II 问该几何上可分析什么。

Paper III 问该几何如何变得奇异且拓扑非平凡。

Paper IV 问历史被商时损失什么信息且该损失如何关联表示与计算。

架构只有每个后续论文扩展 Paper I 而不迫使 Paper I 基础对象被重定义才成功。

---

## 50. 激活的 Paper I–II–III 解析接口

可选 Paper II 到 Paper III 依赖现只对一个有界接口激活：

```text
Paper I:
  projective histories and the q=4 Hecke subgroup
          |
          v
Paper II:
  planar/cylindrical regular AES targets
  + holomorphic local-diffeomorphism pullback
          |
          v
Paper III:
  critical-set singularities
  + Hecke-Hauptmodul zero dessin
  + sign-cover and geodesic-knot interfaces
  + restricted relative arithmetic zero divisors.
```

依赖保持无环。Paper II 不证明奇异结论，Paper I 不用 Papers II 或 III 的解析或自守定理。

### Paper I 导出契约

Paper I 导出显式射影算子 (T_{\sqrt2}) 与 (J)、其矩阵关系与生成子群与 (G_4) 的等同。它不导出
历史到零集函子。

### Paper II 导出契约

Paper II 导出：

1. 平面调和 AES 目标；
2. 柱面 AES 目标；
3. 全纯局部微分同胚的函子式拉回；
4. 关联正则轨迹 Laplacian 与曲率恒等式。

导出显式排除临界点与奇异度量完备化。

### Paper III 附加

Paper III 可把那些导出与标准三角群一致化组合。它必须在活跃源证明所有 AEG 特定零集与锥计算。
它必须区分标准外部 Hauptmodul 输入与新推导 AEG 拉回构造。

q=4 符号覆盖有两个不同下游实现且不得等同。其完备粗 AEG 商是平坦柱面。双曲 Hecke orbifold 的
单位切丛相反是周期轨道纽结的三维载体；在同一指标二覆盖上其尖点紧化产出二分量环面链环
T(2,4) 的补。覆盖特征相等是结构的，但经典测地流编码与透镜空间紧化仍是引用外部输入。

在算子商，本原双曲 q=4 历史满射到定向本原周期轨道纽结。循环历史平移变共轭，路径反演给时间
反演轨道，中性关系子显式坍缩。任何记住这些纤维内标记历史的增强仍开放。

### 算术除子层

相对除子层级是：

[
\text{history presentation}
\to \text{operator}
\to \text{section over a field of definition}
\to \text{relative prime divisor}
\to \text{geometric sheets}.
]

(K(B)) 上算术不可约、(\overline K(B)) 上几何不可约、拓扑单值与 Galois 作用不得等同。对提供带型
二次与四次寄存器，Paper III 现证明在所述判别式补上有限平展的显式有限平坦模型，连同等变、坍缩
核、判别式、几何分裂与 Frobenius 循环测试。这些是极小自然性模型，非从任意历史构造寄存器。从
历史语法到规范算术截面的一般箭头因此仍开放。

---

## 51. M-0008 有界六次实验室接口

六次 Lyashko–Looijenga 附加在不改 Papers I 或 II 导入契约下跨四个带型层水平扩展 Paper III：

```text
supplied monic-centered sextic
  |-- critical-value polynomial and LL sheet
  |-- real carrier and six-root thread
  |-- genus-two branched-cover monodromy
  `-- one arithmetic genus-two fiber.
```

直接 Paper III 贡献有界：它计算 (x^6-x) 的事件多项式、证明显示的跨星 (B_6) 单值、构造载体/线/
映射环面读法并安装混合辫拉回。LL 度与分岔理论、Birman–Hilden 与辛单值，以及 Galois/自同态判据
仍是引用经典输入。

有两个连续遗忘运算且不得坍缩：

[
\text{normalized sextic sheet}
\longrightarrow
\text{critical-value configuration}
\longrightarrow
\text{double LL discriminant}.
]

第一个正则纤维有 (1296) 坐标归一化叶与 (216) 自由源旋转轨道，非 (1296) 或 (216) 个非同构亏格二
曲线。第二箭头遗忘更多事件数据。显式 P3-L9 孪生现证明第一遗忘箭头损失真正亏格二复模：一个事件
五次上的两个源旋转轨道在同一正则切片给不同 Igusa 点。这不把任一叶计数变成曲线计数；完整 (216)
轨道像是开放 P3-L10 普查。

商覆盖仍有规范信息分解。逐叶模比经其范谱多项式与对称迹数据下降，而平均把常数与零和置换表示
分开。零和范平方单值不变且在 (Q_0) 严格正，但非沿任意开路径的平坦能量。在正交切片方向，两条
显示铅笔给比 ((t-\beta)/t)^5 与平衡正则纤维除子 (5[\beta]-5[0])。这是对数电荷而非有限 Dirichlet
或 Hodge 能量。

临界值编织与根编织占不同层。其架构接口是混合构型空间扩张及其 LL 拉回（或等价 Hurwitz 群胚），
绝非无标记同态 (B_5\to B_6)。这保持信息损失方向：

[
\text{LL sheet plus moving test parameter}
\longrightarrow
\text{mixed braid path}
\longrightarrow
\text{six-root braid}.
]

亏格二映射类、整辛、模二置换与算术 Galois 层只能经其声明映射比较。抽象同构
(\operatorname{Sp}_4(\mathbb F_2)\cong S_6) 是共同有限目标，非单个 Frobenius 元与拓扑环之间的
规范匹配。

此实验室供强证据一个多项式可协调实、复、拓扑与算术读法。它现供显式几何 LL–Igusa 孪生且因此
纤维式非因式分解定理。它不供从一般历史到 LL 叶的函子、真零管、完整 (216) 轨道普查、算术或周期
孪生、标记单值孪生、Hodge/Siegel 度量能量、Markov 下降或新纽结不变量。那些剩余箭头保持虚线/开放
且不能用作已证明 P3-L1–P3-L9 节点的依赖。
