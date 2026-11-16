# 开放问题与决定登记

**文件：** `governance/08-open-questions.md`
**状态：** 权威问题登记
**版本：** 1.1
**日期：** 2026-08-06
**依赖：**

* `AGENTS.md`
* `governance/00-authoritative-scope.md`
* `governance/01-paper-series-architecture.md`
* `governance/02-paper-I-outline.md`
* `governance/03-theorem-dependency-graph.md`
* `governance/04-current-to-target-map.md`
* `governance/05-mathematical-status.md`
* `governance/06-editorial-rules.md`
* `governance/07-acceptance-checklist.md`

**适用于：** 影响 Papers I–IV 的开放数学、结构、编辑与迁移问题。

---

## 1. 目的

本文档记录重组期间不得静默解决的未解决问题。

它区分：

* 阻塞 Paper I 的决定；
* 阻塞依赖定理的证明义务；
* 记号与约定选择；
* 模型分类问题；
* 包含依赖验证的可选材料；
* 分配给 Papers II–IV 的研究问题。

一项保持开放直到它有：

1. 记录决定或证明；
2. 识别来源变更；
3. `05-mathematical-status.md` 状态更新；
4. 传播到所有受影响文档与定理节点。

---

# 第一部分. 问题协议

## 2. 优先级层

### `P0 — 阻塞`

问题解决前 Paper I 不能数学闭包。

### `P1 — 高`

问题不阻塞全部写作，但阻塞一章、定理支、摘要断言或迁移决定。

### `P2 — 中`

问题影响阐述、可选定理、附录或后续论文接口。

### `P3 — 研究`

问题主要属 Papers II–IV 或后续研究，若正确推迟则不阻塞 Paper I。

---

## 3. 问题状态

用以下之一：

* `OPEN`
* `UNDER REVIEW`
* `DECISION PROPOSED`
* `PROOF IN PROGRESS`
* `RESOLVED`
* `DEFERRED TO PAPER II`
* `DEFERRED TO PAPER III`
* `DEFERRED TO PAPER IV`
* `REJECTED`
* `DUPLICATE`

---

## 4. 所需问题字段

每个问题应含：

* **ID**
* **优先级**
* **状态**
* **问题**
* **为何重要**
* **当前证据**
* **开放时默认规则**
* **解决条件**
* **受影响文件**
* **受影响定理节点**
* **拥有者**
* **决定记录**

---

## 5. 关闭问题

问题解决时追加：

```markdown
### Resolution

- Decision:
- Mathematical justification:
- Source changes:
- Status changes:
- Downstream nodes rechecked:
- Reviewer:
- Date:
```

不删已解决问题。它们形成重组决定历史。

---

# 第二部分. Paper I 阻塞问题

## OQ-001 — 正则 AES 规范定义

**优先级：** P0
**状态：** CLOSED — 2026-08-06 于 Paper I 解决

### 问题

正则算术表达式空间规范原始定义是什么？

候选形式含：

#### 选项 A — Eikonal 定义

[
\mathfrak E=(\mathcal M,g,a;\mu,\lambda),
\qquad
|\nabla a|_g^2=\mu^2+\lambda^2a^2.
]

#### 选项 B — 框架流定义

装备区分加法与乘法方向的曲面使得：

[
da(X_u)=\mu,
\qquad
da(X_v)=\lambda a.
]

#### 选项 C — 相容组合定义

满足方向流与度量相容两者的框架 Riemannian 曲面。

### 为何重要

此定义控制：

* eikonal 方程逻辑状态；
* 正则零定理一般性；
* 度量原始或导出；
* 到 Paper II 接口；
* 到 Paper III 奇异 AES 接口。

### 当前证据

当前论文在流优先与 eikonal 优先表述间交替。

接触模型自然供优选水平方向，而上半平面模型供度量实现。

### 开放时默认规则

不定稿 `def:regular-aes`。

用条件措辞：

> In the metric formulation considered here …

### 解决条件

选一个定义并在显式相容假设下证明与其他表述等价。

### 受影响文件

* `sections/sec03.tex`
* `sections/sec04.tex`
* 目标第 5–7 章

### 受影响节点

* E1
* F3
* T6
* T7
* Z3

### 拥有者

作者

### 决定记录

待定。

---

## OQ-002 — 年代复合约定

**优先级：** P0
**状态：** CLOSED — 2026-08-06 于 Paper I 解决

### 问题

对历史 (\gamma) 与 (\delta)，

[
\gamma\delta
]

年代上意味什么？

意味：

1. 先应用 (\gamma) 再 (\delta)；或
2. 先应用 (\delta) 再 (\gamma)？

### 为何重要

影响：

* 矩阵乘法；
* 余循环符号与顺序；
* 射影分解；
* ACS 定向；
* Baumslag–Solitar 关系；
* 有限接触交换子。

### 当前证据

当前来源用函数复合与词序语言，可能不总一致。

### 开放时默认规则

不重写约定敏感证明。

用显式表达式：

[
g_n\circ\cdots\circ g_1
]

而非压缩积。

### 解决条件

选一个约定并验证：

* 一个两步仿射示例；
* 一个 Möbius 分解；
* 一个 ACS 示例；
* 一个接触交换子。

### 受影响节点

* C0
* P2
* T2
* T3
* E5
* T9–T12
* K3

### 拥有者

作者与数学审查者

### 决定记录

待定。

---

## OQ-003 — 射影矩阵作用约定

**优先级：** P0
**状态：** CLOSED — 2026-08-06 于 Paper I 解决

### 问题

采纳作用是否是：

[
\begin{pmatrix}
A&B\
C&D
\end{pmatrix}
\cdot z
=======

\frac{Az+B}{Cz+D},
]

且年代历史对应矩阵左乘还是右乘？

### 为何重要

(PGL_2) 生成公式必须精确匹配历史顺序。

### 开放时默认规则

每个射影计算必须既写为复合映射又写为矩阵积。

### 解决条件

附录 A 固定约定并验证每个初等语境。

### 受影响节点

* C0
* P1
* P2
* T2
* P3

### 拥有者

数学审查者

---

## OQ-004 — (PGL_2) 生成定理精确域假设

**优先级：** P0
**状态：** CLOSED — 2026-08-06 于 Paper I 解决

### 问题

当前定理与分解是否对每个域 (K)（含特征 (2)）一致成立？

### 为何重要

当前用：

[
J(z)=-1/z
]

在特征 (2)（(-1=1)）改变形式。

定理可能仍真，但证明与生成元措辞需检查。

### 当前证据

平移、非零缩放与反演仍应生成秩一射影群，但现有公式以实型符号书写。

### 开放时默认规则

对特征不等于 (2) 的域陈述定理，或显式标任意域版本待定。

### 解决条件

供全特征有效证明或限制定理。

### 受影响节点

* T2
* P3
* Paper IV 有限域模型

### 拥有者

代数审查者

---

## OQ-005 — 精确仿射历史子语言

**优先级：** P0
**状态：** CLOSED — 2026-08-06 于 Paper I 解决

### 问题

哪些语法限制刻画其射影像位于：

[
B_\infty\cong\operatorname{Aff}(1,K)?
]

的历史语言？

是否恰是：

* 纯槽-(1) 历史；
* 排除第二槽除法的历史；
* 所有保持 (\infty) 的语境；
* 另一定义类？

### 为何重要

Paper I 中心定位论断是：

[
\text{existing AEG}=\text{an affine/Borel sector}.
]

这需精确语法到群对应。

### 开放时默认规则

只陈述算子级结果：

> The transformations fixing (\infty) form the affine Borel subgroup.

尚不声称完整语法刻画。

### 解决条件

按是否固定 (\infty) 分类每个初等单孔语境，然后刻画生成子语言。

### 受影响节点

* P3
* P4
* 第 2–4 章

### 拥有者

作者

---

## OQ-006 — 正仿射分量对完整实仿射群

**优先级：** P1
**状态：** CLOSED — 2026-08-06 于 Paper I 解决

### 问题

Paper I 应只发展：

[
\operatorname{Aff}^{+}(1,\mathbb R),
]

还是含方向反转仿射映射作不连通扩张？

### 为何重要

微分流用：

[
e^\lambda>0.
]

负乘子不在恒等分量且需离散反射。

### 开放时默认规则

在 (\operatorname{Aff}^{+}(1,\mathbb R)) 上发展连续几何。

代数提及完整实仿射群。

### 解决条件

决定反射是否贡献任何本质 Paper I 几何。

### 受影响节点

* P4
* F1
* E2
* T6

### 拥有者

作者

---

## OQ-007 — “torsion”含义

**优先级：** P0
**状态：** CLOSED — 2026-08-06 于 Paper I 解决

### 问题

主术语 `arithmetic torsion` 应指：

1. 初等端点序缺陷；
2. 相对仿射平移缺陷；
3. ACS 加权面积；
4. 闭环垂直 holonomy；
5. 接触曲率；
6. 一族相关不变量？

### 为何重要

当前论文对相关但非字面等同的有限与无穷小量用同一词。

它也可能与 Riemannian torsion 混淆。

### 开放时默认规则

用限定术语：

* elementary affine torsion；
* relative affine defect；
* global ACS torsion；
* commutator holonomy；
* horizontal curvature。

### 解决条件

选主要定义并陈述剩余量如何从它导出或逼近它。

### 受影响节点

* A4
* T10–T12
* K3
* T15–T17
* 摘要与标题

### 拥有者

作者

---

## OQ-008 — 直接 ACS 定向与权重约定

**优先级：** P0
**状态：** CLOSED — 2026-08-06 于 Paper I 解决

### 问题

规范 ACS 求值应用：

[
\nu_x(\gamma)
=============

e^{M_\gamma}
\left(
x+\int_{C_\gamma}e^{-M},dA
\right),
]

还是保留反路径形式带：

[
e^M,dA?
]

### 为何重要

选择控制：

* 定向；
* Stokes 符号；
* 示例值；
* 与源、目标框架余循环比较。

### 当前证据

两表述在适当反转或归一化后编码同一未来缩放。

直接路径公式概念上更干净。

### 开放时默认规则

不全局替换现有 ACS 公式。

### 解决条件

证明等价并对照测试两约定：

* 一个加法；
* 加法后乘法；
* 乘法后加法；
* 四步示例。

### 受影响节点

* T3
* G1
* T9–T12
* T17

### 拥有者

作者与符号约定审查者

---

## OQ-009 — 广义 torsion 相容条件

**优先级：** P0
**状态：** CLOSED — 2026-08-06 于 Paper I 解决

### 问题

[
\tau(\gamma,\delta)?
]

的规范域是什么？

可能：

1. 等累积尺度历史；
2. 等完整 ACS 端点历史；
3. 同射影端点作用历史；
4. 带基点依赖缺陷的任意历史。

### 为何重要

不同结论需不同条件：

* 等尺度给独立于 (x)；
* 等 charge 给闭 ACS 链；
* 等算子给零相对算子缺陷。

### 开放时默认规则

保持两个定义：

* scale-compatible；
* charge-compatible。

不称它们等价。

### 解决条件

每个相容层陈述单独命题。

### 受影响节点

* A3
* G2
* G3
* T10–T12

### 拥有者

作者

---

## OQ-010 — 奇异 AES 定义

**优先级：** P0
**状态：** CLOSED — 2026-08-06 于 Paper I 解决

### 问题

奇异 AES 定义应多宽？

奇异应允许：

* 非光滑 (a)；
* 退化 (g)；
* 删除点；
* 变或消失 (\mu,\lambda)；
* 射影极点；
* 边界；
* 图转换？

### 为何重要

太窄定义排除意图示例。

太宽定义无数学推论。

### 开放时默认规则

要求：

1. 声明闭奇异集 (S)；
2. (\mathcal M\setminus S) 上正则 AES；
3. (S) 附近显式局部行为。

### 解决条件

对照测试定义：

* (\mathfrak E_0)；
* 孤立零模型；
* 一个多重零构造；
* 一个射影极点示例。

### 受影响节点

* Z3
* Z4
* Paper III 架构

### 拥有者

作者

---

## OQ-011 — 当前孤立零模型分类

**优先级：** P0
**状态：** CLOSED — 2026-08-06 于 Paper I 解决

### 问题

当前盘模型中心状态究竟如何？

它是：

* 含非光滑赋值；
* 从流形移除；
* 度量奇异；
* 参数退化点；
* 无效扩张？

### 当前证据

径向赋值行为如：

[
a(r)\sim Cr,
]

且 (r=\sqrt{x^2+y^2}) 在原点不可微。

### 开放时默认规则

不称模型为正则 AES。

### 解决条件

用局部笛卡尔坐标重写模型并审计：

* (a) 光滑性；
* (g) 光滑性；
* 流方程有效性；
* 穿孔域拓扑。

### 受影响节点

* Z4
* (\mathfrak E_1) 命名
* Paper III 奇异示例

### 拥有者

几何审查者

---

## OQ-012 — (\mathfrak E_0,\mathfrak E_1,\ldots) 规范编号

**优先级：** P0
**状态：** CLOSED — 2026-08-06 采纳描述名

### 问题

[
\mathfrak E_0,\mathfrak E_1,\mathfrak E_k?
]

中什么不变量决定索引？

历史用法变化。

可能含义含：

* 正则对奇异层级；
* 零分量数；
* 构造顺序；
* 奇异索引。

### 为何重要

盲重命名风险破坏旧证明与图。

### 开放时默认规则

用描述名：

* basic regular hyperbolic model；
* isolated-zero singular model；
* multi-zero model。

保留历史符号仅带限定。

### 解决条件

创建模型登记含：

| Formula | Domain | Zero set | Singular set | Historical name | Final name |

### 受影响文件

整个仓库

### 拥有者

作者

---

# 第三部分. Paper I 高优先级证明问题

## OQ-013 — 不变仿射度量推导

**优先级：** P1
**状态：** CLOSED — 2026-08-06 于 Paper I 证明

### 问题

度量：

[
g_{\mu,\lambda}
===============

e^{-2\lambda v}\frac{du^2}{\mu^2}+dv^2
]

能否从仿射群与归一化生成元框架规范导出？

### 为何重要

这把上半平面模型从 ansatz 转为齐次实现。

### 当前证据

选生成元长度后仿射群有自然左不变度量。

### 开放时默认规则

呈现度量为有动机显式模型，非唯一强制。

### 解决条件

指定群坐标、Maurer–Cartan 形式与度量不变性。

### 受影响节点

* E2
* T6
* E3

### 拥有者

微分几何审查者

---

## OQ-014 — 曲率归一化

**优先级：** P1
**状态：** CLOSED — 2026-08-06 于 Paper I 证明

### 问题

对一般度量归一化，Gauss 曲率是否恰是：

[
-\lambda^2,
]

还是出现附加因子？

### 开放时默认规则

摘要或主要结果清单不陈述广义曲率。

### 解决条件

直接曲率计算或经显式坐标缩放约化到标准双曲度量。

### 受影响节点

* E3
* Paper II 分析

### 拥有者

几何审查者

---

## OQ-015 — Laplace–Beltrami 特征值

**优先级：** P1
**状态：** CLOSED — 2026-08-06 于 Paper I 证明

### 问题

对一般归一化度量，所选符号约定下是否：

[
\Delta_g a=2\lambda^2a
]

### 为何重要

当前文本陈述归一化情形：

[
\Delta a=2a.
]

### 开放时默认规则

只陈述显式验证归一化公式。

### 解决条件

计算完整 Laplace–Beltrami 算子并固定符号约定。

### 受影响节点

* E6
* Paper II 算子比较

### 拥有者

分析审查者

---

## OQ-016 — 算术网格作用是否等距？

**优先级：** P1
**状态：** CLOSED — 2026-08-06 于 Paper I 分类

### 问题

实现：

[
a\mapsto a+s,
\qquad
a\mapsto ka
]

的变换是否保持：

* 仅赋值；
* 度量；
* 框架 AES 结构；
* 某些子集？

### 为何重要

当前阐述可能暗示比已验证更强的几何对称。

### 开放时默认规则

称它们赋值相容变换，非等距。

### 解决条件

计算度量拉回。

### 受影响节点

* E4
* E5
* 双曲网格图

### 拥有者

几何审查者

---

## OQ-017 — 正确 Baumslag–Solitar 关系

**优先级：** P1
**状态：** CLOSED — 2026-08-06 于 Paper I 检查

### 问题

最终作用与复合约定下 (X_s) 与 (Y_k) 满足什么精确关系？

可能相差逆与生成元命名。

### 开放时默认规则

把关系移到附录或省略。

### 解决条件

把两边算为显式映射并比较。

### 受影响节点

* E5

### 拥有者

代数审查者

---

## OQ-018 — 边界处正则零定理

**优先级：** P1
**状态：** CLOSED — 2026-08-06 采纳无边/内部定理

### 问题

(\mathcal M) 有边时 Paper I 应如何陈述正则零定理？

### 为何重要

内部正则零是余一维子流形，但零集可遇或终止于边界。

### 开放时默认规则

对内部零点或无边流形陈述主定理。

### 解决条件

加单独边界表述或显式排除。

### 受影响节点

* T7
* Z2
* Paper III 拓扑改变机制

### 拥有者

微分拓扑审查者

---

## OQ-019 — 正则零分量数与全局拓扑

**优先级：** P2
**状态：** PARTIALLY RESOLVED BY THE COMPLETE REGULAR SPLITTING THEOREM

### 问题

什么假设下可结论零分量是：

* 真嵌入线；
* 圆；
* 有限数？

### 当前证据

正则值定理只局部给一维子流形。新全局结果证明若 AES 连通、完备、无边，则

[
M\cong Z(a)\times\mathbb R,
]

故零层非空连通。这不分类高维载体中其内在一维流形拓扑，也不适用于不完备模型或有边流形。

### 开放时默认规则

完备无边假设之外不作全局分类。

### 解决条件

加紧性、完备性、properness 或模型特定假设。

### 受影响节点

* Z2
* Paper III 多重零理论

### 拥有者

拓扑审查者

---

## OQ-020 — 正则总零集定理与投影淹没

**优先级：** P1
**状态：** CLOSED — 2026-08-06 于 Paper I 证明

### 问题

零集上：

[
d_pa_t\neq0
]

是否自动蕴含：

[
\pi:\mathcal Z\to I
]

是淹没？

### 预期答案

是：可在空间方向修正求带任意参数分量的切向量。

### 开放时默认规则

只声称 (\mathcal Z) 是光滑子流形。

### 解决条件

显式写切空间证明。

### 受影响节点

* T8
* Paper III 管定理

### 拥有者

微分拓扑审查者

---

## OQ-021 — Paper I 含多重零示例

**优先级：** P1
**状态：** CLOSED — 从 Paper I 省略并推迟到 Paper III

### 问题

当前是否有通过全部六要求的多重零模型？

1. 显式域；
2. 显式度量；
3. 显式赋值；
4. 奇异集分类；
5. 流验证；
6. 精确零拓扑。

### 开放时默认规则

Paper I 主定理序列不含多重零示例。

### 解决条件

对照清单认证一个模型。

### 受影响节点

* Z7
* Paper I 图
* Paper III 迁移

### 拥有者

作者

---

## OQ-022 — 局部全局综合定理表述

**优先级：** P1
**状态：** CLOSED — 2026-08-06 采纳分层综合

### 问题

T17 能否写为一个定理而不错误等同：

* 仿射端点缺陷；
* ACS 加权面积；
* 有限接触 holonomy；
* 无穷小曲率？

### 开放时默认规则

呈现关系为最终综合小节而非定理。

### 解决条件

分离：

1. 精确仿射/ACS 恒等式；
2. 精确有限接触公式；
3. 共同无穷小极限。

### 受影响节点

* T17
* 摘要
* 结论

### 拥有者

作者与审查者

---

# 第四部分. 编辑与记号问题

## OQ-023 — 赋值空间记号对水平分布记号

**优先级：** P1
**状态：** CLOSED — 2026-08-06 记号固定

### 问题

[
\mathcal H
]

应表上半平面还是水平分布？

### 开放时默认规则

用：

[
\mathbb H^2
]

表上半平面且：

[
\mathcal D=\ker\alpha
]

表水平分布。

### 解决条件

系列范围采纳一个约定。

### 受影响文件

Papers I–III

### 拥有者

编辑

---

## OQ-024 — (\lambda) 作强度对累积对数尺度

**优先级：** P1
**状态：** CLOSED — 2026-08-06 记号固定

### 问题

累积乘法 charge 应用：

[
M
]

还是 (\Lambda)，保留 (\lambda) 给固定无穷小强度？

### 为何重要

当前 Maurer–Cartan 与流公式有重载 (\lambda) 风险。

### 开放时默认规则

保留：

* (\lambda)：固定强度；
* (M)：累积对数 charge。

### 解决条件

审计所有当前公式并更新记号。

### 拥有者

编辑

---

## OQ-025 — (\delta) 对 (\delta_H)

**优先级：** P1
**状态：** CLOSED — 2026-08-06 记号固定

### 问题

Paper I 是否应把当前 (\delta)-算子改名为：

[
\delta_H
]

以强调其水平与非幂零性质？

### 开放时默认规则

行文用 `horizontal covariant differential`，新材料用 (\delta_H)。

### 解决条件

确定与先前论文及未来 Paper II 记号相容。

### 受影响节点

* K4
* T16
* Paper II 算子

### 拥有者

作者与编辑

---

## OQ-026 — 术语“contact connection”使用

**优先级：** P2
**状态：** OPEN

### 问题

接触构造应称：

* arithmetic contact manifold；
* contact connection；
* 带接触水平分布的 Ehresmann connection；
* arithmetic contact model？

### 为何重要

投影：

[
(u,v,a)\mapsto(u,v)
]

带水平分布是 Ehresmann connection，而 (\alpha) 也是接触形式。

### 开放时默认规则

用：

> arithmetic contact model with its associated horizontal connection.

### 解决条件

选区分两结构的术语。

### 拥有者

几何编辑

---

## OQ-027 — Paper I 标题与副标题

**优先级：** P2
**状态：** OPEN

### 选项

1. **Arithmetic Expression Geometry I: Foundations**
2. **Arithmetic Expression Geometry I: Affine Foundations**
3. **Arithmetic Expression Geometry I: Sequential Histories and Affine Geometry**

### 为何重要

`Foundations` 宽，而大多数发展几何是仿射。

### 开放时默认规则

用：

**Arithmetic Expression Geometry I: Foundations**

带副标题：

**Sequential Histories, Affine Flow, Torsion, and Contact Geometry**

### 解决条件

最终定理集固定后决定。

### 拥有者

作者

---

## OQ-028 — “foundations”对“affine foundations”角色

**优先级：** P2
**状态：** OPEN

### 问题

含 (PGL_2) 完备化定理是否合理化更宽标题 `Foundations`，尽管发展微分几何仍仿射？

### 开放时默认规则

摘要显式陈述 Paper I 在射影语境中发展仿射基础扇区。

### 拥有者

作者

---

## OQ-029 — 历史术语“arithmetic torsion”

**优先级：** P2
**状态：** OPEN

### 问题

论文是否应保留已建立术语尽管可能与 torsion 张量混淆？

### 开放时默认规则

保留术语带早警告：

> Arithmetic torsion is an order defect and is unrelated to the torsion tensor of an affine connection unless explicitly compared.

### 解决条件

评估替代如 `arithmetic commutation defect` 是否更优。

### 拥有者

作者

---

## OQ-030 — 相等与中性层级放置

**优先级：** P2
**状态：** OPEN

### 问题

当前中性分类多少属 Paper I？

### 开放时默认规则

第 2 章只保留相等层级与附录 E 少量示例。

推迟完整中性理论。

### 解决条件

识别后续理论属 Paper IV 还是单独关系论论文。

### 拥有者

作者

---

# 第五部分. Paper II 接口问题

## Paper II 解决更新 — 2026-08-06

第一规范 Paper II 手稿在数学审查层关闭 OQ-031–OQ-036。原始问题作为溯源保留下方。

| 问题 | 状态 | 解决 |
|---|---|---|
| OQ-031 | **CLOSED** | 二维正则 AES 已有 (g) 与定向。接触支单独声明使 (D_u,D_v) 正交的水平度量。 |
| OQ-032 | **CLOSED WITH SCOPE LIMIT** | 曲面 (J) 内在。接触 (J) 与声明归一化度量及水平定向相容；不声称任意接触同胚下不变。 |
| OQ-033 | **CLOSED FOR THE CHOSEN REALIZATIONS** | 曲面分析用 Riemannian 面积与极小 Dirichlet 形式。接触分析用正接触体积与 (-D_u^2-D_v^2-lambda D_v) 的 Friedrichs 实现。原始平方和被单独处理且不作本质自伴声称。 |
| OQ-034 | **CLOSED** | 修正对数接触场在含 (mu+ilambdamathbb R) 的支半平面验证；其域与 CR 方程显式。 |
| OQ-035 | **CLOSED BY CORRECTION** | 规范对象是有限滤过 (C^infty(u,v))-模，非未指定基。 |
| OQ-036 | **CLOSED** | 决定性结果是基本双曲 AES 上 (C_0) 理想边界 Poisson–Dirichlet 定理，由精确 Dirichlet-to-Neumann 与能量恒等式加强。 |

## OQ-031 — 分析规范水平度量

**优先级：** P3
**状态：** DEFERRED TO PAPER II

### 问题

接触分布是否承认从 Paper I 继承的优选水平度量，还是 Paper II 必须独立选一个？

### 当前默认

Paper II 必须显式陈述附加度量数据。

### 研究意义

控制算术全纯性规范还是模型依赖。

---

## OQ-032 — 规范近复结构

**优先级：** P3
**状态：** DEFERRED TO PAPER II

### 问题

给定定向二维水平度量，相容 (J) 局部决定。该结构在意图 AEG 范畴中是否全局规范？

### 当前默认

Paper I 不声称规范性。

---

## OQ-033 — (\Delta_H) 正确解析域

**优先级：** P3
**状态：** DEFERRED TO PAPER II

### 问题

[
\Delta_H=D_u^2+D_v^2
]

应在哪个函数空间与测度研究？

### 所需未来决定

* 参考测度；
* 形式伴随；
* 边界条件；
* 自伴实现；
* 完备性假设。

---

## OQ-034 — 算术全纯坐标

**优先级：** P3
**状态：** DEFERRED TO PAPER II

### 问题

意图公式是否是：

[
\zeta(u,v,a)
============

u+\frac{i}{\lambda}\log(\mu+i\lambda a)?
]

### 所需验证

* 支域；
* 错字修正；
* 水平 Cauchy–Riemann 方程；
* 全局对局部定义。

---

## OQ-035 — affine–Appell“基”状态

**优先级：** P3
**状态：** DEFERRED TO PAPER II

### 问题

族在什么环境空间是基？

### 默认规则

完备性建立前称算子稳定族或有限三角系。

---

## OQ-036 — 双曲实函数论第一决定性定理

**优先级：** P3
**状态：** DEFERRED TO PAPER II

### 问题

哪个结果使 Paper II 成为真正函数论而非形式算子笔记？

候选：

* Poisson 核；
* Dirichlet 问题；
* 最大原理；
* Green 函数；
* 谱定理；
* 延拓结果。

### 拥有者

作者

---

# 第六部分. Paper III 接口问题

## OQ-037 — 参数判别式定义

**优先级：** P3
**状态：** DEFERRED TO PAPER III

### 问题

判别式应只含：

[
a_t(p)=0,
\qquad
d_pa_t=0,
]

还是也：

* 度量退化；
* 参数退化；
* 边界碰撞；
* properness 失败；
* 射影极点？

### 当前默认

用带单独分量的分层判别式。

---

## OQ-038 — 一般 (E_k) 索引原则

**优先级：** P3
**状态：** DEFERRED TO PAPER III

### 问题

(k) 记录：

* 零分量数；
* 奇异阶；
* 构造层；
* 绕数；
* 另一不变量？

### 默认规则

解决前不稳定 (E_k) 记号。

---

## OQ-039 — 普遍多重零构造存在

**优先级：** P3
**状态：** DEFERRED TO PAPER III

### 问题

是否有产生带 (k) 正则零分量验证 AES 的一致构造？

### 所需未来证明

* 公式；
* 度量；
* 流方程；
* 零拓扑；
* 奇异控制。

---

## OQ-040 — (E_0,E_1,E_k) 共形唯一性

**优先级：** P3
**状态：** DEFERRED TO PAPER III

### 问题

什么数据下此类唯一性陈述有意义？

候选：

* 固定零除子；
* 固定曲率；
* 固定渐近；
* 固定边界行为；
* 固定流参数。

### 当前状态

开放。

---

## OQ-041 — 局部奇异正规形

**优先级：** P3
**状态：** DEFERRED TO PAPER III

### 问题

哪些奇异类型与 AEG 流和度量结构相容？

候选含：

* fold；
* cusp；
* crossing；
* branch point；
* birth/death；
* reconnection。

### 当前默认

导出相容正规形前不导入一般灾变理论标签。

---

## OQ-042 — 显式零族 properness

**优先级：** P3
**状态：** DEFERRED TO PAPER III

### 问题

对每个提议族，是否：

[
\pi:\mathcal Z\to B
]

proper？

### 为何重要

无 properness，纤维拓扑可经逃向无穷改变。

---

## OQ-043 — 从零分量置换到辫

**优先级：** P3
**状态：** DEFERRED TO PAPER III

### 问题

单值何时从：

[
S_n
]

提升到：

[
B_n?
]

### 所需未来数据

* 嵌入移动点或曲线；
* 无碰撞参数路径；
* 环境同痕类；
* 基空间拓扑。

---

## OQ-044 — 穿线定义

**优先级：** P3
**状态：** DEFERRED TO PAPER III

### 问题

线是：

* 管截面；
* 独立嵌入曲线；
* 标记历史；
* 零支；
* 单值携带装饰？

### 默认规则

被穿线对象固定前不定义纽结不变量。

---

## OQ-045 — Markov 不变

**优先级：** P3
**状态：** DEFERRED TO PAPER III

### 问题

任何管/线量能否存活辫稳定化与共轭？

### 当前状态

开放且决定性。

---

## OQ-046 — 超出 Alexander/Burau 的新信息

**优先级：** P3
**状态：** DEFERRED TO PAPER III

### 问题

归一化 AEG 管不变量能否区分非由 Alexander 多项式或 Burau 表示决定的示例？

### 当前状态

开放成功判据。

---

# 第七部分. Paper IV 接口问题

## OQ-047 — 历史精确范畴

**优先级：** P3
**状态：** DEFERRED TO PAPER IV

### 问题

主要对象应是：

* 部分语境自由范畴；
* 作用群胚；
* 路径群胚；
* 重写 (2)-范畴？

### 为何重要

这决定关系与凝聚如何表示。

### 部分仿射扇区注（2026-10-24）

Paper 0 §3.6（`subsec:p0-operation-to-length`）现陈述仿射扇区回答什么而不解决此问题。源是
`def:p0-left-right-combs` 梳文法；到运动的赋值是 `prop:p0-history-homomorphisms` 的求值同态
`nu`；到长度的复合是 `prop:p0-length-multiplicative-charge` 的 `ell = |log o L o nu|`，它是诱导
运动的函数故历史不单射（`prop:p0-length-losses`）。因 `|.|` 非同态（`eq:p0-length-not-additive`），
长度*非*函子目标：函子对象是 `(R,+)` 中乘法 charge `M = log o L o nu`，加法 charge 是不下降部分
（`thm:p0-descent`(4)）。两扩张被他处阻塞而非此问题：`Aff^+(1,R) -> PGL_2(K)` 需迹三分，Paper 0
不发展；梳到任意二叉树需 Paper I `thm:sequential-tree-classification`。OQ-047 本身状态未变。

---

## OQ-048 — 普通对射影历史群胚

**优先级：** P3
**状态：** DEFERRED TO PAPER IV

### 问题

普通可允许性与射影延拓应形成：

* 分离范畴；
* 带域标签范畴；
* 部分函子；
* 局部化？

---

## OQ-049 — 商后规范过程残差

**优先级：** P3
**状态：** DEFERRED TO PAPER IV

### 问题

给定：

[
G\to G/H,
]

纤维 (H) 本身是否过程残差，还是仅参考提升与规范选择后？

### 当前证据

无截面 (H)-值坐标不规范。

---

## OQ-050 — 双赋值语义含义

**优先级：** P3
**状态：** DEFERRED TO PAPER IV

### 问题

什么数学语义合理化把有序点–余点对解释为概念–谓词结构？

### 默认规则

代数处理投影子定理，无语义过度声称。

---

## OQ-051 — 凝聚定义

**优先级：** P3
**状态：** DEFERRED TO PAPER IV

### 问题

凝聚是：

* 历史等价商；
* 规范归一化；
* 历史到算子传递；
* 算子到齐次商传递；
* 一般遗忘映射族？

### 默认规则

显式定义每个凝聚映射而非用普遍隐喻。

---

## OQ-052 — 度量凝聚损失信息

**优先级：** P3
**状态：** DEFERRED TO PAPER IV

### 问题

可能度量含：

* 纤维基数；
* 轨道维；
* 熵；
* 最短代表长度；
* 稳定子大小；
* 编码长度。

当前未建立规范度量。

---

## OQ-053 — 规范代表复杂度

**优先级：** P3
**状态：** DEFERRED TO PAPER IV

### 问题

商类何时承认：

* 规范代表；
* 可计算正规形；
* 最短代表？

### 为何重要

复杂度断言依赖此区分。

---

## OQ-054 — 几何度量对计算成本

**优先级：** P3
**状态：** DEFERRED TO PAPER IV

### 问题

什么假设下几何路径度量可比于实际计算成本？

### 所需未来结构

* 状态图；
* 编码；
* 转换成本；
* 模拟定理；
* 拟等距比较。

---

## OQ-055 — 表示复杂度作统一量

**优先级：** P3
**状态：** DEFERRED TO PAPER IV

### 问题

时间与空间复杂度能否导出为表示几何不同投影？

### 当前状态

研究假设，非定理。

---

## OQ-056 — 非交换性增长推论

**优先级：** P3
**状态：** DEFERRED TO PAPER IV

### 问题

哪些显式 AEG 相关群或半群有：

* 多项式增长；
* 指数增长；
* 中间增长？

### 默认规则

无来自非交换性的一般蕴含。

---

## OQ-057 — 历史空间与 AES 拟等距

**优先级：** P3
**状态：** DEFERRED TO PAPER IV

### 问题

任何自然历史图是否拟等距嵌入或映射到双曲 AES？

### 为何重要

无此定理，几何距离不能与表达式复杂度等同。

---

## OQ-058 — 复杂度案例研究选择

**优先级：** P3
**状态：** DEFERRED TO PAPER IV

### 候选案例

* Horner 形式对展开多项式；
* FFT 或大整数乘法；
* 重写归一化；
* 证明搜索；
* 石子游戏。

### 选择判据

选带显式状态空间、度量与成本定理的示例。

---

# 第八部分. 迁移与仓库问题

## OQ-059 — 最终仓库布局

**优先级：** P1
**状态：** CLOSED — 采纳顶层 `paper-1/` 规范入口

### 问题

Paper I 是否应立即从：

```text
aeg-paper.tex
sections/
```

移到当时提议罗马编号形式：

```text
paper-I/paper-I.tex
paper-I/sections/
```

还是应先当前路径内重组？

### 默认规则

大路径重命名前先数学重组。

### 解决条件

完成审计并确认构建策略。

### 拥有者

仓库维护者

### 最终解决

数学审计与构建闭包后，仓库维护者授权阿拉伯编号顶层布局。规范路径现为
`paper-1/aeg-paper-1.tex`、`paper-1/sections/` 与 `paper-1/appendices/`。

---

## OQ-060 — 共享对论文特定参考文献

**优先级：** P2
**状态：** OPEN

### 问题

四篇论文应用一个共享 `.bib` 还是分离参考文献？

### 默认规则

迁移期间保留一个共享参考文献。

论文边界稳定后才分割。

---

## OQ-061 — 共享图

**优先级：** P2
**状态：** OPEN

### 问题

哪些图真正跨论文共享，哪些应有论文特定版本？

### 默认规则

用共享源资产但含义不同处用论文特定渲染副本或图注。

---

## OQ-062 — 遗留 `aeg-lemma.tex` 命运

**优先级：** P2
**状态：** OPEN

### 问题

此文件含唯一证明还是仅过时重复？

### 默认规则

不删。

### 解决条件

对照活跃节与笔记比较每个引理。

---

## OQ-063 — 生成讨论文件状态

**优先级：** P2
**状态：** CLOSED — 固定基线或当前树无跟踪 `gpt/` 目录

### 问题

跟踪 `gpt/` 目录应带归档状态原地保留还是移到 `governance/archive/`？

### 解决

来源清单未发现可迁移的跟踪 `gpt/` 目录。历史引用仅溯源。未来生成讨论材料添加时必须分类，
而非创建隐含当前路径。

---

## OQ-064 — 已发布 DOI 对重组手稿

**优先级：** P1
**状态：** CLOSED FOR PAPER I — 版本显式区分

### 问题

仓库应如何区分：

* 现有 DOI 版本；
* 活跃重组草稿；
* 最终新预印本？

### 默认规则

不暗示 DOI 指向重组版本除非更新。

### 拥有者

作者

---

## OQ-065 — 多论文构建系统

**优先级：** P2
**状态：** CLOSED — 实现根选择器构建

### 问题

`build.sh` 应支持论文选择，还是每论文自有构建脚本？

### 解决

根 `build.sh` 接受 `1`、`2`、`3`、`4` 或 `all` 并保留系列一个规范构建接口。除非未来论文发展
真不同工具需求，逐论文脚本不必要。

---

# 第九部分. 文献与新颖性问题

## OQ-066 — 表达式历史几何文献

**优先级：** P2
**状态：** OPEN

### 问题

什么先前工作最接近研究：

* 表达式求值历史作几何路径；
* 算术语境生成仿射作用；
* 求值过程接触几何？

### 为何重要

Paper I 新颖性断言必须克制且准确放置。

### 默认规则

专用文献审计后只用：

> We are not aware of …

---

## OQ-067 — 与仿射控制系关系

**优先级：** P2
**状态：** OPEN

### 问题

仿射流与接触提升是否已是另一名下标准控制系模型？

### 为何重要

数学新颖性可能在算术解释与综合而非局部接触形式本身。

---

## OQ-068 — 与 Riccati 控制及射影动力学关系

**优先级：** P2
**状态：** OPEN

### 问题

应引用哪些已建立 Riccati/射影流文献准确放置双边完备化？

---

## OQ-069 — 与余循环及半直积关系

**优先级：** P2
**状态：** OPEN

### 问题

仿射余循环是否应显式框为半直积作用标准 (1)-余循环？

### 潜在益处

可简化证明并澄清 ACS 加权。

### 潜在风险

过度抽象可能模糊算术起源。

---

## OQ-070 — 与接触化及 jet 空间关系

**优先级：** P2
**状态：** OPEN

### 问题

算术接触模型最好理解为：

* 接触化；
* 一阶 jet 空间模型；
* Ehresmann connection；
* 带算术坐标的标准 Darboux 接触结构？

### 默认规则

陈述标准接触等价并强调算术框架。

---

# 第十部分. 发布阻塞登记

## 71. 当前 P0 阻塞

以下任何未解决 Paper I 不能达数学闭包。勾选项由第十四部分解决台账关闭：

* [x] OQ-001 — 正则 AES 定义
* [x] OQ-002 — 年代复合
* [x] OQ-003 — 矩阵作用约定
* [x] OQ-004 — (PGL_2) 定理域范围
* [x] OQ-005 — 仿射语法扇区
* [x] OQ-007 — torsion 主含义
* [x] OQ-008 — ACS 定向与权重
* [x] OQ-009 — 广义 torsion 相容
* [x] OQ-010 — 奇异 AES 定义
* [x] OQ-011 — 孤立零模型分类
* [x] OQ-012 — 模型编号

无发布任务可豁免这些项。

---

## 72. 当前 P1 章阻塞

以下阻塞特定章或可选主结果且由对应第十四部分解决关闭：

* [x] OQ-013 — 不变仿射度量
* [x] OQ-014 — 曲率归一化
* [x] OQ-015 — Laplace 特征值
* [x] OQ-016 — 网格对称状态
* [x] OQ-017 — Baumslag–Solitar 约定
* [x] OQ-018 — 边界零表述
* [x] OQ-020 — 投影淹没证明
* [x] OQ-021 — 多重零示例包含
* [x] OQ-022 — 局部全局综合表述
* [x] OQ-023 — (\mathcal H) 记号碰撞
* [x] OQ-024 — (\lambda/M) 记号
* [x] OQ-025 — (\delta/\delta_H) 记号
* [x] OQ-059 — 仓库迁移时机
* [x] OQ-064 — DOI/版本区分

可选结果可移除而非阻塞发布，凡范围授权处。

---

# 第十一部分. 推荐解决顺序

## 73. 决定序列

按此顺序解决问题：

### 阶段 1 — 约定

```text
OQ-002
OQ-003
OQ-004
OQ-005
OQ-006
OQ-024
```

### 阶段 2 — 基础定义

```text
OQ-001
OQ-007
OQ-009
OQ-010
OQ-012
OQ-025
OQ-026
```

### 阶段 3 — 代数与 ACS 证明

```text
OQ-008
OQ-017
OQ-022
```

### 阶段 4 — 几何模型

```text
OQ-013
OQ-014
OQ-015
OQ-016
```

### 阶段 5 — 零几何

```text
OQ-011
OQ-018
OQ-019
OQ-020
OQ-021
```

### 阶段 6 — 编辑与仓库决定

```text
OQ-023
OQ-027
OQ-028
OQ-029
OQ-030
OQ-059–OQ-065
```

### 阶段 7 — 后续论文研究

```text
OQ-037–OQ-058
```

由规范数学审查手稿关闭且仅作溯源保留的 Paper II 问题：

```text
OQ-031–OQ-036 — CLOSED
```

---

# 第十二部分. 决定模板

## 74. 定义决定

```markdown
## Decision D-XXXX — [Definition name]

- Issue:
- Adopted definition:
- Rejected alternatives:
- Reason:
- Primitive data:
- Derived data:
- Required hypotheses:
- Examples tested:
- Affected theorem nodes:
- Source files updated:
- Reviewer:
- Date:
```

---

## 75. 约定决定

```markdown
## Decision C-XXXX — [Convention name]

- Issue:
- Adopted convention:
- Two-step verification:
- Matrix verification:
- ACS verification:
- Contact verification:
- Affected formulas:
- Files updated:
- Reviewer:
- Date:
```

---

## 76. 证明闭包

```markdown
## Proof closure P-XXXX — [Result]

- Issue:
- Final theorem statement:
- Hypotheses:
- Proof location:
- Independent verification:
- Status before:
- Status after:
- Downstream nodes released:
- Date:
```

---

## 77. 推迟决定

```markdown
## Deferral F-XXXX — [Topic]

- Issue:
- Deferred to:
- Minimal statement retained in Paper I:
- Material moved:
- Mathematical status:
- Reason for deferral:
- Re-entry condition:
- Date:
```

---

# 第十三部分. 最终支配规则

## 78. 前沿纪律

开放问题是数学结果一部分，非编辑残渣。

重组必须保持三层分离：

[
\boxed{
\text{resolved foundation}
\quad\subset\quad
\text{conditional extension}
\quad\subset\quad
\text{open research frontier}.
}
]

Paper I 可提及前沿，但必须只从已解决基础建立。

证据不完备时默认动作是：

1. 保留来源；
2. 削弱论断；
3. 记录问题；
4. 推迟依赖理论；
5. 不猜。

---

# 第十四部分. Paper I 解决台账（2026-08-06）

详细决定记录于 `decisions-paper-I.md`；逐定理证据记录于 `paper-I-closure-report.md`。下方条目
关闭其 `State` 字段上方已变的问题而不删其原始问题或默认规则。

## Resolution — OQ-001

- **决定：** 正则 AES 是内在元组 \((M,g,a;\mu,\lambda)\)，\(M\) 定向、\(g\) Riemannian、\(a\)
  光滑、\(\mu\ne0\)，且 \(|\nabla a|_g^2=\mu^2+\lambda^2a^2\)。
- **数学理由：** 第 5 节证明与满足 \(X_ua=\mu\)、\(X_va=\lambda a\) 的唯一正定向正交算术框架等价。
- **来源变更：** `05-affine-flow.tex`、`decisions-paper-I.md`。
- **状态变更：** E1 与 F3 提升为已证明 Paper I 基础。
- **重查下游节点：** T5–T8、Paper II 框架接口。
- **审查者：** 独立几何与最终数学审查。
- **日期：** 2026-08-06。

## Resolution — OQ-002 与 OQ-003

- **决定：** 历史时间上左到右作用；\(\gamma\delta\) 意味先 \(\gamma\) 再 \(\delta\)；矩阵作用于列
  齐次坐标且 \(\rho(\gamma\delta)=\rho(\delta)\rho(\gamma)\)。
- **数学理由：** 显式两步仿射、Möbius、ACS 矩形与接触矩形检查一致。
- **来源变更：** 第 2–4 节与附录 A–B。
- **状态变更：** C0–C2 与 P2 关闭。
- **重查下游节点：** PGL 生成、所有余循环、ACS 与接触符号。
- **审查者：** 独立代数与 torsion/接触审查。
- **日期：** 2026-08-06。

## Resolution — OQ-004

- **决定：** 双边生成定理对每个域有效，含特征二。
- **数学理由：** 第 3 节给分离 \(C=0\) 与 \(C\ne0\) 分解；每个除数显式非零且同恒等式存活
  \(-1=1\)。
- **来源变更：** `03-projective-affine.tex`、附录 A。
- **状态变更：** T2 提升为已证明。
- **重查下游节点：** Borel 放置与 Paper IV 域接口。
- **审查者：** 独立代数与最终数学审查。
- **日期：** 2026-08-06。

## Resolution — OQ-005 与 OQ-006

- **决定：** 初等仿射子语言由逐个固定 \(\infty\) 的非退化初等语境生成；其像是 \(B_\infty\)，
  不声称等于完整逆像。连续几何用 \(\operatorname{Aff}^+(1,\mathbb R)\)；负乘子仍是不连通代数
  扩张。
- **数学理由：** 初等矩阵表与正规形 \(z\mapsto az+b\) 证明像陈述。
- **来源变更：** 第 3 节。
- **状态变更：** P3 与 P4 关闭。
- **重查下游节点：** 第 4–9 节。
- **审查者：** 独立代数与范围审查。
- **日期：** 2026-08-06。

## Resolution — OQ-007、OQ-008 与 OQ-009

- **决定：** 主算术 torsion 是两尺度相容正加–尺度历史的目标框架平移缺陷。Charge 相容是用于闭
  ACS 链的更强条件。ACS 用 \(dA\wedge dM\)、\(C_\gamma-C_\delta\) 与 \(\eta_*=e^{M_*-M}dA\)。
- **数学理由：** 第 8 节证明直接求值与加权 Stokes；正矩形给声明符号的 \(p(e^q-1)\)。
- **来源变更：** `08-acs-torsion.tex`、附录 D–E。
- **状态变更：** G1–G3 与 T9–T12 于所述语言提升为已证明。
- **重查下游节点：** 有限接触比较与结论。
- **审查者：** 独立几何、代数与 torsion/接触审查。
- **日期：** 2026-08-06。

## Resolution — OQ-010 与 OQ-011

- **决定：** 奇异 AES 有闭无处稠密、局部本质奇异集且在其非空稠密补上正则。盘中心是赋值奇异：
  度量那里光滑，但径向赋值非 \(C^1\) 且无光滑局部扩张。
- **数学理由：** 第 7 节验证笛卡尔光滑性、穿孔 eikonal 方程与精确正则/奇异零分解。
- **来源变更：** `07-zero-geometry.tex`、附录 C。
- **状态变更：** 孤立零模型 Z3–Z5 关闭。
- **重查下游节点：** Paper III 奇异接口。
- **审查者：** 独立代数与几何审查。
- **日期：** 2026-08-06。

## Resolution — OQ-012

- **决定：** Paper I 用「basic regular hyperbolic model」与「isolated-zero singular model」；
  历史 \(\mathfrak E_k\) 索引不规范。
- **数学理由：** 无不变量索引规则存在，而描述名编码已验证正则类。
- **来源变更：** 第 6–7 节、根 README、决定模型登记。
- **状态变更：** 模型编号冲突以移除而非重编号关闭。
- **重查下游节点：** Papers II–III README 文件。
- **审查者：** 独立范围审查。
- **日期：** 2026-08-06。

## Resolution — OQ-013、OQ-014 与 OQ-015

- **决定：** 用归一化左不变仿射度量；其完备上半平面实现有 \(K=-\lambda^2\)，且带
  \(\Delta=\operatorname{div}\nabla\)，赋值满足 \(\Delta a=2\lambda^2a\)。
- **数学理由：** 第 6 节与附录 C 导出不变余框架并显式约化到缩放标准双曲度量；Laplacian 在坐标
  中计算。
- **来源变更：** `06-hyperbolic-model.tex`、附录 C。
- **状态变更：** E2、E3、E6 与 T6 提升为已证明。
- **重查下游节点：** Paper II 算子接口。
- **审查者：** 独立代数与几何审查。
- **日期：** 2026-08-06。

## Resolution — OQ-016 与 OQ-017

- **决定：** 显示网格映射赋值相容且一般不非等距。其映射级关系是
  \(\mathsf Y_n^{-1}\mathsf X_s^n\mathsf Y_n=\mathsf X_s\)，\(n\ge2\)。
- **数学理由：** 度量拉回与关系两边显式计算。
- **来源变更：** 第 6 节与附录 C。
- **状态变更：** E4–E5 关闭且等距声称削弱。
- **重查下游节点：** 摘要与结论无复杂度推断。
- **审查者：** 独立代数审查。
- **日期：** 2026-08-06。

## Resolution — OQ-018 与 OQ-020

- **决定：** 零定理对无边曲面与有边时内部零点陈述。光滑族中空间正则性给光滑总零集与淹没投影，
  但无附加假设无全局管。
- **数学理由：** 第 7 节应用正则值定理并供任意参数向量缺失切空间修正。
- **来源变更：** `07-zero-geometry.tex`。
- **状态变更：** T7 与 T8 于其所述范围提升为已证明。
- **重查下游节点：** Paper III properness 警告。
- **审查者：** 独立代数与几何审查。
- **日期：** 2026-08-06。

## Resolution — OQ-021

- **决定：** Paper I 不含多重零示例。
- **数学理由：** 无候选有完整域/度量/赋值/奇异/流/拓扑审计。
- **来源变更：** 第 7 节陈述推迟；Paper III 记录溯源。
- **状态变更：** Z7 推迟到 Paper III，从 Paper I 闭包移除。
- **重查下游节点：** 摘要、引言、结论。
- **审查者：** 独立范围审查。
- **日期：** 2026-08-06。

## Resolution — OQ-022

- **决定：** 用分层综合：精确开仿射/ACS 缺陷、精确目标归一化闭漂移与其共同无穷小极限。
- **数学理由：** 第 9 节分别证明两有限公式与归一化 \((h,k)\to(0,0)\) 极限。
- **来源变更：** `09-contact-curvature.tex`、附录 D。
- **状态变更：** T17 关闭为综合命题而非所有有限量相等。
- **重查下游节点：** 摘要与结论。
- **审查者：** 独立几何与最终数学审查。
- **日期：** 2026-08-06。

## Resolution — OQ-023、OQ-024 与 OQ-025

- **决定：** \(\mathbb H^2\) 表上半平面、\(\mathcal D=\ker\alpha\) 表水平分布、\(\lambda\) 固定
  强度、\(M\) 累积对数尺度、\(\delta_H\) 标量水平协变微分。
- **数学理由：** 记号跨第 4–9 节一致；\(\delta_H^2\) 显式仅是反对称化标量简写且非幂零分次复形。
- **来源变更：** 第 4–9 节与附录 A–D。
- **状态变更：** Paper I 记号冲突关闭。
- **重查下游节点：** Paper II README 接口。
- **审查者：** 独立范围与数学审查。
- **日期：** 2026-08-06。

## Resolution — OQ-059 与 OQ-064

- **决定：** 数学重组期间保留 `aeg-paper.tex` 作根规范 Paper I 入口；闭包后在数学重组期间移到
  `paper-1/aeg-paper-1.tex`。识别 Zenodo DOI 为较早归档版本，非当前手稿。
- **数学理由：** 最小化路径波动并防发布元数据过度陈述现有 DOI 代表什么。
- **来源变更：** 根 README、手稿日期块、来源清单。
- **状态变更：** 仓库布局与 DOI 区分对 Paper I 关闭；未来出版元数据仍需作者批准。
- **重查下游节点：** 构建脚本与后续论文 README 文件。
- **审查者：** 独立仓库与范围审查。
- **日期：** 2026-08-06。

## Paper III 处置 — OQ-037 至 OQ-046

规范 Paper III 手稿如下改变此簇处置。标 partial 的处置关闭打印构造问题但保留更强自然性或分类
问题。

### OQ-037 — 部分解决

Paper III 定义带分离临界零、边界、奇异/度量、域/范畴与非真逃逸轨迹的结构判别式。它在真垂直
横截区域证明稳定性。完整并规范 Whitney 分层仍开放。

### OQ-038 — 以描述命名解决

未发现规范历史 `E_k` 索引原则。手稿从定理名移除符号并称验证对象为平行 `k`-零、对数覆盖、积管
与螺旋模型。受限自然范畴是否后支持索引仍开放。

### OQ-039 — 于度量灵活范畴解决

共形实现定理把每个光滑淹没转为正则 AES。显式选择 `a=e^x product_j(y-c_j)` 实现恰 `k` 零分量，
`a=e^x sin y` 实现局部有限可数族。规范或完备普遍模型仍开放且与裸存在分离。

### OQ-040 — 仍开放；证明灵活阻碍

共形实现反驳度量可变时任何无限定唯一性期望。固定度量、完备性、曲率、渐近、齐次或历史自然约束
下唯一性仍开放。

### OQ-041 — 以示例部分解决

定号与不定参数化 Morse 函数给验证 AEG 相容诞生/死亡与重连示例。横截简单复多项式判别式给
`w^2=tau`。这些不声称 AEG 度量芽完整分类。

### OQ-042 — 部分解决

柱面积与紧螺旋族证明真。逃向无穷族证明为何无一般 properness 推断可用。更广非紧族判据仍开放。

### OQ-043 — 复根解决，实零函子性开放

秩二零截面定理与平方自由多项式接口产 `B_n`-值单值，且每条辫由算术全纯场在基本双曲 AES 上实现。
实赋值有曲线零且不自动产 `B_n`；自然赋值到根或探针函子仍开放。

### OQ-044 — 定义固定；内在选择仍开放

一维流形基上有限零线现是真零管中真嵌入一维子流形，其参数投影是有限叶覆盖，需要时带相对边界
条件。螺旋切片供显式所选线。从 AEG 数据函子式、探针无关选择仍开放。

### OQ-045 — 新 AEG 装饰仍开放

手稿打印共轭与两稳定化门禁，证明无状态标量坍缩，并在精确有限域假设下导入标准扭曲 quandle 态和
不变。无新历史导出 AEG 装饰通过 Markov 下降。

### OQ-046 — 仍开放

固定仿射支是 Alexander quandle。普通 torsion 精确；共振扭曲 torsion 是非零上同调类，但其平面态和
坍缩到 Alexander-quandle 着色计数。不声称超出 Alexander/Burau 的闭包级分离。

---

## OQ-071 — (q=4) 自守赋值精确下降

**状态：** CLOSED WITH AN OBJECT-TYPE DISTINCTION

Paper III 计算算术生成元符号特征：

[
\chi(J)=-1,
\qquad
\chi(JT)=-1,
\qquad
\chi(T)=+1.
]

故完整 orbifold 商上无标量归一化可移除非平凡特征。数学自然替代现固定：

1. (\ker\chi\backslash\mathbb H) 上标量赋值；或
2. 完整商上关联实符号线丛截面。

度量与零图下降到完整商。两等价呈现间选择是对象类型约定，非未解决特征计算。

## OQ-072 — Hecke 零网络尖点、完备化与 properness 审计

**状态：** PARTIALLY RESOLVED；一般 properness 仍开放

活跃定理证明

[
g=|dW/W|^2
]

到四阶轨道有限距离且沿尖点无限距离。楼上完备化加 (4\pi) 锥点；完备完整 orbifold 长度商完备，
其粗椭圆像角 (\pi)。

符号特征覆盖现于模型特定意义完全识别。它有签名 ((0;2;\infty,\infty))；粗 AEG 完备化后 (W) 把
它与完备平圆柱 (\mathbb C^\times) 等同。保留双曲 orbifold 结构，其单位切丛是

[
T^1\mathcal O_4^\chi\cong S^3\setminus T(2,4)
]

于声明尖点紧化下。这关闭那一个指标二覆盖拓扑。仍需证明或反驳万有覆盖与其他有限指标商上局部
有限性与 properness，并识别零关联为真管的任何参数族。完备化或链环补陈述无一是真管定理。

## OQ-073 — 历史到相对除子函子

**状态：** PARTIALLY RESOLVED FOR SUPPLIED REGISTERS；一般函子开放

从声明标记算术历史范畴构造到参数基上算术截面或多项式的函子，

[
H\longmapsto P_H\longmapsto (P_H)_0,
]

使得表达式等价、复合、定义域、手性与参数拼接被尊重。确定射影求值哪个核（若有）在除子中仍
可见。

(q=4) Hecke 构造当前是特殊算子商示例，非所有历史解。Paper III 现给极小有限测试：提供寄存器
(u^2=t) 强制等变二次端点除子，而其标记前缀迹与极点余循环保留严格多于终端算子的信息。特别它们
区分 (\omega_4) 与空历史即使其终端除子一致。构造仍依赖提供带型寄存器且其终端除子穿过 (\rho)
分解；故不关闭一般问题。

## OQ-074 — 零路径算术对几何不可约

**状态：** FINITE ALGEBRAIC TEST RESOLVED；规范 AEG 起源开放

找有限整 AEG 族：

* 一般多项式或截面在 (K(B)) 上不可约；
* 其 (\overline K(B)) 上几何因式分解显式；
* 几何单值、算术 Galois 作用、惰性与 Frobenius 循环型全可计算；
* 所得叶承认非事后强加的 AEG 解释。

有限代数测试现显式。二次寄存器给带可计算 Frobenius 的常几何整 Kummer 覆盖，而

[
(u^2-t)^2-3
]

在 (\mathbb Q(\sqrt2)(t)) 上不可约，扩展常量后分裂为两个不可约几何分量，判别式
(256\cdot3^2(t^2-3))、局部叶单值与显式 Frobenius 循环型。仍开放的是上最后一点：这些寄存器是提供
输入，非无限制 AEG 历史规范输出。

## OQ-075 — 因式分解论零历史

**状态：** OPEN

若到零不等价路径意味编码不等价不可约因式分解，用带非平凡类或因式分解数据的整环或序替换唯一
因式分解 (\mathbb Z[\sqrt2]) 测试用例。确定理想类、长度集、弹性或悬链结构能否实现为相对 AEG
零除子标签或单值不变量。

此问题异于 Hecke 镶嵌问题：后者供算术对称与自守一致化，非本身非唯一因式分解。

## OQ-076 — Hecke 周期轨道纽结标记历史增强

**状态：** OPEN AFTER AN OPERATOR-LEVEL SURJECTION

对每个射影算子本原双曲的 (q=4) 标记历史，Paper III 现定义周期轨道纽结 (K_{\rho(h)})。映射满射，
在算子共轭层循环词平移下不变，且把路径逆送到时间反演轨道。它必然坍缩中性词 (\omega_4) 每个
插入与每个保持算子共轭类的其他标记改变。

构造经典切割码或周期轨道非重言装饰，保留部分标记迹、普通域、除子、框架或局部系数数据，并证明
其在声明历史等价下行为。仅环境同痕或 Markov 下降后此装饰可称新纽结不变量。

## OQ-077 — 混合切片–管自然性与中性词测试

**状态：** EXPLICIT HORIZONTAL MODEL PROVED；HISTORY-NATURAL LIFT OPEN

提供族 (P_m(z,t)=z^2-t^m) 证明单个多项式可同时控制实奇异载体、有限根线、判别式周期、辫与
（偶 (m)）环绕数。它也展示精确信息损失

[
1\longrightarrow P_2\longrightarrow B_2\longrightarrow S_2\longrightarrow1.
]

这尚未连接 Paper I 切片 torsion 与管单值。圆基上 `Serre transgression' 非正确语言；已证明数据
是单值与纯辫核残差。Paper I 现有仿射 torsion 实值、定义于受限加–尺度核对、完整仿射算子一致时
消失，且不自动穿过 q=4 反演生成元扩张。

构造可逆标记历史群或群胚带系数路径赋值，其置换作用穿过 q=4 符号特征且其同算子纤维自然映射到
纯辫或框架辫。第一硬测试是中性词

[
\omega_4=(JT)^4.
]

其终端射影除子等于空历史。确定规范完整历史系数路径是否仍给两叶尖点线目标中 (sigma_1^4)、
四叶单位切目标中 (z_4^{-1})、阶加权框架类或零。两目标不同且不必一致。用输出作 AEG 数据前证明
声明历史关系与每个坐标/寄存器规范下不变。

普通两辫扩张不能同时把两 q=4 椭圆关系子与一个单位切纤维绕等同。正解因此必须用 orbifold 加权
归一化、高股框架构型，或证明单位切与多项式残差真正不同结构。提供四股 Garside/旋转校准现精确
匹配单位切中心扩张，但它不从 q=4 dessin 或无限制标记历史导出那些系数路径。该路径选择自然性是
剩余测试。

---

# 第十部分. 笔记储备（由笔记储备审计添加，2026-08-10）

以下三条由 `governance/notes-reserve-audit.md` 登记。完整清单、分级、冲突台账与处置建议在该
文件。

## OQ-078 — 笔记储备：提升候选及其集成审计

**优先级：** P3
**状态：** OPEN

八个笔记簇带完整工作笔记证明尚未在任何论文：

1. `notes/analysis-and-calculus/02` — 混合加乘积分（传输、分裂、伴随配对、连续 ACS 三重恒等）；
2. `notes/analysis-and-calculus/03` — 分次协变 delta 演算、扭曲积、扭曲 Rota–Baxter 恒等、对偶
   权线几何；
3. `notes/thermodynamics-and-renormalization/05` — AEG/热力学接触同胚、AEG 变量 Maxwell 关系、
   常数 (λ,μ) 不相容注、Massieu 表示；
4. `notes/thermodynamics-and-renormalization/07` — 固定 N 算法热力学接触同胚；
5. `notes/foundations-and-geometry/04` — 仿射环面 holonomy 玩具模型；
6. `notes/foundations-and-geometry/05`（初级部分）— charge 同态、ℤ 理想与 F₂ 中正规子群格；
7. `notes/knots-and-loops/06` — Fox 演算与仿射余循环字典（BS(1,2) 部分超出 Paper III §8）；
8. `notes/knots-and-loops/08` — 三参数算术表达式群中小纽结嵌入。

每簇进入任何论文或标 `PROVED` 超出工作笔记层前需完整集成审计（陈述/证明匹配、年代与符号约定、
域与正则假设、对照当前论文框架约定）。

## OQ-079 — 笔记储备：冲突与修正台账

**优先级：** P3
**状态：** OPEN

审计记录历史来源与当前论文间九冲突或修正陈述：E₀/E₁ 命名倒置 (C-1)、"threadlike = 左子叶"定义
(C-2)、反路径 ACS 公式 (C-3)、−2 Laplace 特征值 (C-4)、坐标扩展 δ (C-5)、仅反演 torsion (C-6)、
Paper I 中管 (C-7)、`notes/knots-and-loops/05` 错误「稠密奇点」(C-8) 与 CR/扭曲调和性/Appell
材料先前 Paper I 放置 (C-9)。

这些记录非调和。关闭任一需授权任务更新受影响笔记头、治理登记与任何依赖引用。

## OQ-080 — 笔记储备：带通过/失败判据的开放计划

**优先级：** P3
**状态：** OPEN

审计识别五个其通过/失败判据已陈述于笔记的开放计划：

1. **PD₃ 里程碑 1**（`notes/computation-and-resources/05`）：在环面阶段 T²×(a₋,a₊) 展示
   `[κ]=μλ[du∧dv]≠0` 并计算其 Poincaré–Lefschetz 对偶相对 1-类；不尝试则显式退役里程碑。
2. **图灵机资源 torsion**（`notes/computation-and-resources/03`）：分类可由语义保持程序变换实现
   的内存增量重排；无此 torsion 只是诊断。
3. **Cayley 模型曲率**（`notes/foundations-and-geometry/01`）：验证或证伪 Manhattan 距离共形
   因子 K=−2 几乎处处。
4. **算法热力学桥**（`notes/thermodynamics-and-renormalization/06`、`08`）：完成超出固定 N 接触
   同胚的 Gibbs/配分对应，带笔记 09 记录修正。
5. **接触比较猜想**（`notes/projective-condensation/01`、§10）：经显式 Gauss/Iwasawa 图关联 AEG
   水平分布与 T¹H² 规范接触结构，交织算术生成元、括号与基投影。

---

## OQ-081 — ripple 几何是否内在于算术词？

**优先级：** P2
**状态：** OPEN

**问题：** Paper 0 §§4–6 发展对偶读法经射影算术算子拉回标准 horocycles。那里每条已证明陈述都
对标准 horocycle 族 `H_t` 陈述故对一图。是否存在极点、拉回族与不动点附于*词*而非所选实现的
表述？

**为何重要：** 名字 *ripple geometry* 在 Paper 0 只作描述标签（`STRUCTURAL PROPOSAL`）。正答案
把它转为定理级陈述并供 `00a` §5 与 Paper 0 §12.4 列出的射影 AES 开放计划。

**当前证据：** `thm:p0-ripple-pencil-formula`（线/圆二分）、`thm:p0-four-matrix-readings`
（一矩阵四读法）与 `prop:p0-path-ripple-duality` 已证明；仓库无图无关表述。

**开放时默认规则：** 引用已证明公式，从不用名字，作数学内容。

**解决条件：** 带证明 horocycle 图构造为特殊情形的内在定义，或显示同算子两词有不等价对偶族的
反例。

**受影响文件：** `paper-0/sections/04-ripple-geometry.tex`、
`paper-0/sections/06-projective-unification.tex`、`paper-0/sections/12-interface.tex`。
**受影响定理节点：** `def:p0-ripple-pencil`、`thm:p0-ripple-pencil-formula`、
`prop:p0-path-ripple-duality`。
**拥有者：** 作者。
**决定记录：** `governance/00b-paper-0-geometric-foundation-amendment.md` §4。

## OQ-082 — 穿孔规范选择

**优先级：** P2
**状态：** REOPENED (2026-09-29)。曾对光滑延拓赋值 RESOLVED (2026-09-22)，非延拓情形重开为
OQ-088。解决按写不成立；见本条末修正案。

**问题：** `def:p0-punctured-aes` 声明有限穿孔集 `S`。`S` 能否由算术数据决定而非规定，且存在时
选择是否唯一？

**解决。** `决定：` 当赋值延拓到环境曲面上光滑函数 `a~`，穿孔集非选择：恰是 `a~` 临界集。
`数学理由：` `thm:p0-punctures-are-critical` 证明两包含。若 `p` 是穿孔且 `d a~(p) != 0`，则用
任何光滑背景度量 `g_0` 构造的模板度量 `g~ = |d a~|^2_{g_0} g_0 / (mu^2 + lambda^2 a~^2)` 是 `p`
邻域满足 eikonal 恒等的光滑非退化度量，故正则结构穿过 `p` 延拓，矛盾局部本质性。反之若
`d a~(p) = 0` 且 `p` 非穿孔，`p` 处读 eikonal 恒等给 `0 = mu^2 + lambda^2 a(p)^2 >= mu^2 > 0`，
矛盾。故 `S = {d a~ = 0}`。
`来源变更：` Paper 0 §11 获 `lem:p0-gradient-nonvanishing`、`thm:p0-punctures-are-critical`、
`rem:p0-puncture-hypothesis` 与 `cor:p0-puncture-count`。
`状态变更：` 新节点 `PROVED`；`thm:p0-four-circle-model` 现被迫而非规定穿孔集，因其赋值满足
`Crit(P) ∩ D_r = {0}`；且 `k`-穿孔问题成为带恰 `k` 临界点光滑函数问题。
`重查下游节点：` `def:p0-punctured-aes`、`prop:p0-puncture-tangent-cone`、
`thm:p0-four-circle-model`、`op:p0-four-circle` 与 Paper I `prop:isolated-zero-singular-model`，
后者*不*满足假设（其赋值在穿孔非 `C^1`）故是 OQ-088 主题。
`审查者：` 作者。
`日期：` 2026-09-22（晚）。

**修正案（2026-09-29）— 上理由无效。**
`决定：` 精神不变，但**未**对光滑延拓赋值建立，且问题重开。
`理由：` 模板度量 `g~ = |d a~|^2_{g_0} g_0 / (mu^2 + lambda^2 a~^2)` 满足 eikonal 恒等，但无使
它在穿孔邻域与**给定** `g` 一致；`def:p0-punctured-aes` 条件 (ii) 要求延拓 `g` 本身。缺失步是上
「故正则结构穿过 `p` 延拓」子句全部内容。
`反例（验证）：` 单位盘减去原点带 `a = x`、`mu = lambda = 1` 与
`g = dx^2/(1+x^2) + dy^2/(x^2+y^2)`，对 `(M,g,a;1,1)` 是正则 AES 带
`|grad a|_g^2 = 1 + x^2 = mu^2 + lambda^2 a^2`；`a` 光滑延拓到整个盘；`g` 完全不延拓，因
`g_yy = 1/(x^2+y^2)` 在原点无界，故条件 (ii) 成立；却 `S = {0}` 而 `Crit(a~) = emptyset`。同
模型平移到任何内部点，故此类中穿孔无处被迫。
`存活：` 反向包含 `Crit(a~) subseteq S`（其证明只在 `M` 点用 eikonal 恒等）与
`thm:p0-four-circle-model`（那里 `d a~(0) = 0`，故缺陷支从不进入）。
`充分修复：` 若另 `g` 在每个穿孔附近共形于光滑非退化延拓度量，则 eikonal 恒等强制 `g` *是*模板
度量且原论证通过。反例逃避此因 `g_yy/g_xx = (1+x^2)/(x^2+y^2)` 在原点无有限非零极限。此假设是否
也必要开放。
`状态变更：` `thm:p0-punctures-are-critical` 与 `cor:p0-puncture-count` 现于
`governance/05b-paper-0-status-register.md` 按打印 `UNSUPPORTED AND EXCLUDED`；
`rem:p0-puncture-hypothesis` 是 `PARTIALLY PROVED`。无论文源被编辑。
`证据：` 根审查 `AEG-Paper-0-review-2026-09-29-thm-punctures-are-critical-v0.1.md`；保留记录
`notes/foundations-and-geometry/10`；`governance/notes-reserve-audit.md` 台账条目 C-10。
`审查者：` DeepSeek Harness Agent（外部审查），2026-09-29。
`日期：` 2026-09-29。

**保留正文（被取代默认规则）。**

**为何重要：** Paper 0 §11 背后探索登记陈述作为其第一未完成项，切割–胶合记账中两额外穿孔选择
不知是否规范。

**当前证据：** 登记拓扑见证（χ = #cycles(σ) = b，穷举 40320 胶合）与 Paper I 验证单穿孔模型
`prop:isolated-zero-singular-model`。

**开放时默认规则：** 穿孔总声明，从不导出。（对光滑延拓赋值此默认现被定理取代。）

**受影响文件：** `paper-0/sections/11-holed-aes.tex`、
`notes/foundations-and-geometry/06-hole-obstructions-ledger.md`。
**受影响定理节点：** `def:p0-punctured-aes`、`prop:p0-puncture-tangent-cone`、
`thm:p0-punctures-are-critical`。
**拥有者：** 作者。
**决定记录：** 迁移 M-0022。

---

## OQ-088 — 赋值不延拓时规范穿孔

**优先级：** P2
**状态：** OPEN

**问题：** `thm:p0-punctures-are-critical` 本应在赋值光滑延拓到环境曲面时规范化穿孔集（2026-09-29
修正：该定理按打印被反驳；故问题*不*限于非延拓情形——见 OQ-082 修正案）。从 Paper I 导入盘模型
不延拓：那里度量光滑穿过中心而赋值连续但非 `C^1`。该情形什么扮演临界集角色，且穿孔是否唯一？

**为何重要：** 两验证穿孔模型不同物种。四圆模型中*度量*不能非退化延拓且穿孔由赋值被迫；盘模型
中*赋值*失败，穿孔集仍是规定。
*（**2026-09-29 修正。** 所画对比对第一物种太慷慨。「度量不能延拓」本身不强制穿孔：OQ-082 修正
案记录反例恰是该物种且其穿孔无处被迫。区分四圆模型的是非物种而是那里 `d a~(0) = 0`。存活的
分界线是 `g` 在穿孔附近共形于延拓度量。）*

**当前证据：** ~~`thm:p0-punctures-are-critical`~~（2026-09-29 修正：按打印被反驳，**不**依赖；
见 OQ-082 修正案）与 `rem:p0-puncture-hypothesis`（Paper 0 §11，现 `PARTIALLY PROVED`）；Paper I
`prop:isolated-zero-singular-model`，那里 `a_D` 中心附近行为如 `rho` 且单侧导数不同。

**开放时默认规则：** 赋值不延拓模型 `S` 声明，Paper 0 §11「hole」语言保持描述。

**解决条件：** 临界集替代（例如 jet 级、爆炸或单侧导数判据），为带规定不可微失败的赋值决定
`S`，带唯一性证明或反例。

**受影响文件：** `paper-0/sections/11-holed-aes.tex`。
**受影响定理节点：** `def:p0-punctured-aes`、`thm:p0-punctures-are-critical`。
**拥有者：** 作者。
**决定记录：** 迁移 M-0022。

## OQ-083 — 撕裂是否承认正非线性描述？

**优先级：** P3
**状态：** OPEN

**问题：** Paper 0 §10 证明算术生成元不闭入有限维 Lie 代数且交换化 charge 无可观测量检测撕裂。
是否存在撕裂非阻碍而是可计算对象的代数结构，且能否为 AES 内在定义而非导入词汇？

**为何重要：** 两命题是拒绝；正描述会把方法立场替换为理论。

**当前证据：** `prop:p0-arithmetic-generators` 与 `prop:p0-characters-cannot-see-tearing`
（此处证明）；`Yuan2026ProcessGeometry` 结构提案与匹配 `eq:p0-bs-relation` 的精确校准（研究本地，
带该仓库自身成熟度标签）。

**开放时默认规则：** 导入词汇标 `STRUCTURAL PROPOSAL` 且从不用作定理假设。

**解决条件：** AES 上内在结构其对象是双历史缺陷，带至少一个交换化不能复现的非平凡计算。

**受影响文件：** `paper-0/sections/10-beyond-linear.tex`、`paper-0/sections/08-acs-tearing.tex`。
**受影响定理节点：** `def:p0-tearing`、`prop:p0-arithmetic-generators`、
`prop:p0-characters-cannot-see-tearing`。
**拥有者：** 作者。
**决定记录：** `governance/00b-paper-0-geometric-foundation-amendment.md` §4。

## OQ-084 — 孔阻碍登记两精度缺陷

**优先级：** P3
**状态：** OPEN

**问题：** 探索登记记录六阻碍而其摘要句说五类，且它把其框架见证 `Z_3` 单值与不同计算中出现的
叶标签 `Z_4` 扭曲等同。两点未解决。

**为何重要：** Paper 0 §11 复现六见证并显式拒绝两等同；若等同实正确，未来修订须带证明说，若否
登记应带修正。

**当前证据：** 登记表六行而头说 五类；两计算涉不同群且仓库无来源关联它们。

**开放时默认规则：** Paper 0 计六并记录差异（`rem:p0-holed-register-bookkeeping`）；等同列于
`subsec:p0-holed-nonclaims` 非断言中。

**解决条件：** 等同证明或反驳，与登记中修正计数。

**受影响文件：** `paper-0/sections/11-holed-aes.tex`、
`notes/foundations-and-geometry/06-hole-obstructions-ledger.md`、
`temp/孔的不可避免性_v0.1.md`（工作原始，此任务不编辑）。
**受影响定理节点：** 无；项仅登记为 `COMPUTATIONALLY VERIFIED EXAMPLE`。
**拥有者：** 作者。
**决定记录：** `governance/migration-log.md` 迁移 M-0019。

---

## OQ-085 — 把 AES 数据附到四圆构型

**优先级：** P2
**状态：** RESOLVED (2026-09-22)

**问题：** 构造定向曲面、含原点的有限穿孔集与补上数据 `(g,a)` 使得所得对象是穿孔 AES、使
`prop:p0-puncture-tangent-cone` 四极限圆自然来自该数据、且原点不可延拓。

**为何重要：** 2026-09-22 审查正确观察到切锥计算是关于曲线构型的陈述且无 AES 结构附于它。

**解决。** `决定：` 构型实现为显式穿孔 AES 的*零轨迹*，非辅助曲线族。
`数学理由：` 取半径 `r < rho` 穿孔盘、赋值 `a = P`（`P` 是四圆并多项式）与度量
`g = |grad a|^2 (dx^2+dy^2)/(mu^2+lambda^2 a^2)`，恰是 eikonal 恒等强制度量。`P` 临界集精确计算
（`grad P = 0` 该盘上仅原点，由证明中情形分析），故 `g` 是光滑 Riemannian 度量且 `(M,g,a)` 是
正则 AES；`P` 因式分解显示其零轨迹恰是四圆；原点不可延拓因正则 AES 有
`|\nabla a| >= |mu| > 0`（`lem:p0-gradient-nonvanishing`），而 `P` 在原点临界且 `a` 任何光滑延拓
由连续性必须那里一致于 `P`。度量不完备且穿孔有限距离。
`来源变更：` Paper 0 §11.2 获 `lem:p0-gradient-nonvanishing` 与 `thm:p0-four-circle-model`；
陈述无 AES 数据附着的段被替换；§11.6 获推广问题。
`状态变更：` `lem:p0-gradient-nonvanishing` 与 `thm:p0-four-circle-model` 是 `PROVED`；此问题
解决；`op:p0-four-circle` 现命名推广问题而非构造。
`重查下游节点：` `prop:p0-puncture-tangent-cone`（现为显式模型零轨迹切锥）、
`def:p0-punctured-aes`（第二验证实例）、Paper I 完备分裂定理（其完备性假设此模型失败，正允许
分支）。
`审查者：` 作者，于代理构造。
`日期：` 2026-09-22。

**被取代文本（保留记录）。** 此问题早期正文其 `Default rule while open` 是「引用切锥计算仅作
构型代数陈述」，保留于此因仓库不删已解决问题：

**当前证据：** 精确展开
`(S_2^2-4rho^2y^2)(S_2^2-4rho^2x^2) = S_2^4-4rho^2S_2^3+16rho^4x^2y^2` 与 Paper I 验证单穿孔
盘模型；两者间无桥。

**受影响文件：** `paper-0/sections/11-holed-aes.tex`。
**受影响定理节点：** `def:p0-punctured-aes`、`prop:p0-puncture-tangent-cone`。
**拥有者：** 作者。
**决定记录：** 2026-09-22 审查响应项 R7；迁移 M-0021。

---

## OQ-087 — 推广四圆模型

**优先级：** P3
**状态：** OPEN

**问题：** `thm:p0-four-circle-model` 从规定多项式赋值产一个穿孔与四零支。哪些曲线构型以这种
方式出现为穿孔 AES 零轨迹，能否不规定 `S` 构造 `k`-穿孔模型，且若赋值必须来自算术运动而非规定
构造是否存活？

**为何重要：** 构造显示构型可实现为零轨迹；不显示可实现为*表达式*。差异恰是 AEG 问题。

**开放时默认规则：** 引用 `thm:p0-four-circle-model` 仅作单穿孔构造，从不作运动生成赋值陈述。

**解决条件：** 曲线构型为穿孔 AES 零轨迹判据，带 `k >= 2` 构造或赋值不能运动生成证明。

**受影响文件：** `paper-0/sections/11-holed-aes.tex`。
**受影响定理节点：** `thm:p0-four-circle-model`。
**拥有者：** 作者。
**决定记录：** `governance/migration-log.md` 迁移 M-0021。

## OQ-086 — 带声明关系历史幺半群与 charge 映射下降

**优先级：** P2
**状态：** RESOLVED (2026-09-22)

**问题：** 历史幺半群应带哪些关系，且 charge 映射是否下降到所得商？

**解决。** `决定：` 采纳*自由积*选择：历史形成由加法与乘法步族生成的群 `G = (R,+) * (R,+)`，
关系仅每族内强加（同族复合与恒等）。不强加跨族关系。
`数学理由：` 此选择下 (i) charge 端点与求值是满同态 `c: G -> R^2` 与 `nu: G -> Aff^+(1,R)`
（`prop:p0-history-homomorphisms`）；(ii) `c` 是交换化，`ker c = [G,G]`，故 ACS 端点是
`G_ab = R^2`（`prop:p0-acs-is-abelianization`）；(iii) 下降问题有 `thm:p0-descent` 非对称答案：
*乘法* charge 穿过 `nu` 因式分解（等于线性部分 `log`，运动群同态），而*加法* charge 不。见证是
传输元 `h(p,q) = M_q A_p M_{-q} A_{-e^{-q}p}`，求值为恒等运动（年代计算在证明中）却带 charge
`(p(1-e^{-q}), 0)` 带 `p(1-e^{-q}) != 0`；故 `c` 在 `ker nu` 上不消失且不能穿过 `nu` 因式分解。
这是审查者要求执行：关系幺半群现显式，下降逐关系验证——乘法 charge 成立且加法可证明失败。
`来源变更：` Paper 0 §8 获 `conv:p0-history-group`、`prop:p0-history-homomorphisms`、
`prop:p0-acs-is-abelianization` 与 `thm:p0-descent`，连同三陈述推论（ACS 是历史语言交换化；charge
路径是端点遗忘；两失败方向对偶）。
`状态变更：` 四新节点 `PROVED`（约定是 `STANDARD CONSEQUENCE REQUIRING AN IN-PAPER PROOF`）；
此问题解决。
`重查下游节点：` `def:acs`、`prop:acs-evaluation`、`ex:p0-distributive-charge-transport`
（现是 `h(p,q)` 型传输实例）、`def:p0-tearing`（其假设未变）、`prop:p0-characters-cannot-see-tearing`。
`审查者：` 作者。
`日期：` 2026-09-22。

**保留正文。**

**当前证据：** `prop:p0-distributive-operator-identity` 与 `ex:p0-distributive-charge-transport`
（两展开共享算子且有 charge `(p,q)` 与 `(kp,q)`）；Paper 0 §8 交换化计算（`Aff^+(1,R)_ab ≅
R_{>0}`）。

**受影响文件：** `paper-0/sections/08-acs-tearing.tex`、`paper-0/sections/02-expansion.tex`。
**受影响定理节点：** `def:acs`、`prop:acs-evaluation`、`ex:p0-distributive-charge-transport`。
**拥有者：** 作者。
**决定记录：** `governance/migration-log.md` M-0020 与 M-0021。

---

## OQ-089 — 跨穿孔撕裂由 ACS 面积还是 holonomy 度量？

**优先级：** P2
**状态：** RESOLVED (2026-09-22)

**问题：** 穿孔空间上两运动比较可能须绕穿孔而非穿过。相对 torsion 由 ACS 面积、绕穿孔环 holonomy
还是两者皆非度量；第一情形什么可允许填充类？

**解决。** `决定：` 它由 ACS 面积度量，在每个模型；AES 数据中无绕穿孔规范 holonomy；穿孔改变仅
*曲面上*执行比较的可允许性。
`数学理由：` Paper 0 §11.4 三命题。
(1) `tau(gamma,delta) = xi_gamma - xi_delta` 是两词函数（`prop:affine-cocycle-formulas`、
`def:relative-torsion`），故穿孔、改模型或改实现不变。
(2) 任何正则 AES 中矩形两排序终止于赋值相差 `mu*h*(e^{lambda k}-1) != 0` 的点
（`prop:p0-surface-does-not-close`），故对应曲面路径不围区域：ACS 比较在每个 AES 规范，非避孔
装置。
(3) 无规范 holonomy：水平集叶层 `ker d_a` 可积故平坦；弯曲联络需附加数据，论文加的（接触模型）
有其相对 charge 投影的规范曲率形式（`prop:p0-curvature-form`），其基环上 holonomy 是 §9 矩形
漂移；规范穿孔模型中赋值在环境曲面单值，故无单值（`prop:p0-no-puncture-holonomy`）。
(4) 可允许填充是带给定边界的 charge 平面定向二链；由 `thm:torsion-stokes` 值独立于所选填充，
穿孔既不加减类。
`来源变更：` Paper 0 §11.4 重写（此前不证明任何且登记问题）；加 `prop:p0-puncture-local-picture`，
计算穿孔局部几何。
`状态变更：` 四新节点 `PROVED`；OQ-089 解决；§11.6 第二开放问题收窄到赋值不延拓模型（OQ-088）。
`重查下游节点：` `def:p0-tearing`、`thm:torsion-stokes`、
`prop:p0-tearing-puncture-independent`、`thm:p0-punctures-are-critical`、
`prop:p0-curvature-form`。
`审查者：` 作者。
`日期：` 2026-09-22（当日第四次修订）。

## 有限型与移植 AES 更新 — 2026-10-09

此更新只取代 OQ-082/OQ-088 受影响结论与多重穿孔/多线条目；较旧带日期研究与审查记录保留。

**带假设解决：** 打印临界集定理用给定度量延拓共形背景修复；每个 k≥1 存在某共形可紧化 AES；
完整 collar 数据重构原始有限型 AES；严格有限程序替换保持精确求值域；语境特征因式分解与右同余
在线特征更新被区分并证明。

**仍开放：**

1. 描述带规定共形模、规定穿孔位置或零构型、或运动内在生成赋值的 AES。
2. 构造 AES 相容 plumbing/退化族。标准 FN 与 plumbing 数据重构辅助共形/双曲几何，非 g,a。
3. 关联具体圆形变与三叶分支模型到忠实算术数据。两者非切环 AES 证明。
4. 在声明 Adva 实验中构造实际对边特征对象；证明观测充分性，需要处右同余或保留分离过程残差。
5. 在合适构型/纤维载体上以 AES 运动实现一般多输入算术门，保留来源、出现、部分域、共轭/传输
   与声明历史等价。
6. 定义循环三元输入的生产反馈或不动点语义。有限 DAG 替换刻意不供此定理。
7. 恢复并归档原始 k4 与移植程序 ZIP 源/检查包以复现其历史 39/55 检查证据。当前证明改编与新
   独立验证器不关闭此任务。

标量撕裂恒等依赖词，而新 k4 示例对标量恒等词有非零全态水平集残差。这些是不同可观测量，故新
结果不矛盾标量穿孔独立或断言规范穿孔 holonomy。

## OQ-090 — 分配标记数据子句意图什么相等？

**优先级：** P1 — 阻塞完整 §2 命题完成，非其算子恒等分量。

**状态：** RESOLVED (2026-10-20 continuation)。

**受影响节点：** `paper-0/sections/02-expansion.tex` 中 `prop:p0-distributive-operator-identity`。

**记录：** 2026-10-20，Codex（OpenAI）。

**问题：** 命题允许域中所有 `p,k` 且说两词作标记数据恰在 `p=k=1` 重合。其证明只比较年代常量对
`(p,k)` 与 `(k,k*p)`。论断意图保留哪些数据与相等？

**当前证据：** `p=k=0` 时两常量对都是 `(0,0)`，尽管证明只结论 `(1,1)`。假设 `k` 非零的步在命题
无此假设。若比较运算标记历史，`add(1); multiply(1)` 与 `multiply(1); add(1)` 仍在首位置不同运算
标签。常量对相等不供这些标记词相等。

算子方程 `k*(z+p)=k*z+k*p` 不受影响。其符号半环分量由 Adva 程序与 `paper-0/formal/` 中单独 Lean
定理检查；零对计算是单独 Lean 陈述。此发现不把算子、历史、charge 或端点值彼此等同。

**开放时历史默认：** 保留手稿；整命题登记为 `PARTIALLY PROVED`，算子分量保留。不把其重合子句附
到成功形式回执。

**解决条件：** 显式选常量对相等或完整标记历史相等，修正参数范围与结论，供含零/单位情形的对应
证明，然后更新源、状态登记、陈述映射与任何下游使用。非零缩放限制可修复常量对计算但不使运算
标记词相等。

### Resolution — 2026-10-20

修正手稿按运算标签、操作数槽与常量定义标记步。两分配词总在首运算标签不同。其分离年代标量投影
遗忘那些标签且恰在 `(p,k)=(0,0)` 或 `(1,1)` 一致。源证明现在非零情形用消去前处理 `k=0`。不删零
算术输入使群陈述通过。

`paper-0/formal/Chapter02Domains.lean` 中 `marked_words_distinct`、`constant_pair_coincidence`
与 `nonzero_constant_pair_coincidence` 在显式域律上形式化这些不同论断。原始符号算子证书与初始
零反例证据保留。状态登记现标**修正**命题 `PROVED` 并保留先前失败子句作带日期发现。charge 传输
示例用 `p=1, k=exp(q)` 且只需不变算子恒等与其所述非零 charge 条件；其下游解释不被此修复扩大。

同源修订区分仿射自映射与仿射群元，以及普通部分除法与非退化射影延拓。`c=0` 在 `K\{0}` 留部分
零映射，非 Möbius 映射。源到形式对应仍是显式审查映射，非声称 TeX 行文被机械翻译。实现与审查由
Codex（OpenAI）；不断言独立人工数学审查。

## OQ-091 — AEG 历史信息序与有向完备

**优先级：** P3
**状态：** PARTIALLY RESOLVED (2026-10-31) — 标记脊柱历史情形解决；分支情形与具体值域实例化仍
开放。

**问题：** `notes/analysis-and-calculus/09-order-topology-scott-lawson.md` 处理的历史——表达式树、
重写图、计算 DAG——能否给信息序 `h ⊑ h'`（"`h'` 精化 / 扩展 `h`"）使它们形成 dcpo（有向完备偏序），
使求值 `ev` 成为 Scott 连续（保持有向并）映射？

**为何重要：** 这是把 Scott 拓扑机制导入 AEG「历史 → 压缩 → 表示 → 几何」阶梯的前置条件。无它，
「极限过程的值是其有限历史值的极限」（`ev` 连续）无连续性定义域。

**当前证据：** `09` §8 现解决标记脊柱历史情形：信息序是年代前缀序 `γ ⊑ γδ`；其理想完备化是有限
与无穷历史 dcpo（有限历史 = 紧元素）；自由 dcpo 普遍性质使 `ev` Scott 连续延拓当且仅当 `ev` 单调。
普通算术求值失败该测试（值域非 dcpo，且 `ev` 部分非单调）。

**开放时默认规则：** 把「求值 Scott 连续」当结构提案非定理；不陈述历史极限收敛结果。

**解决条件：** 在固定历史类上展示信息序、证明有向完备、识别紧（有限）元素、证明 `ev` 保持有向
并（或记录阻碍）。

**受影响文件：** `notes/analysis-and-calculus/09-order-topology-scott-lawson.md`。
**受影响定理节点：** 无（研究笔记；无论文节点依赖）。
**拥有者：** 作者。
**决定记录：** `governance/notes-reserve-audit.md` §2.7（覆盖缺口）。

### 部分解决 — 2026-10-31

对 `def:marked-spinal-history` 的标记脊柱历史（`paper-1/sections/02-sequential-histories.tex`）：

1. **信息序** = 年代前缀序 `γ ⊑ γ' ⟺ γ' = γδ`，从 `eq:chronological-history-concatenation` 直接
   读。
2. **有向完备**：前缀序自由幺半群理想完备化是 `Idl(H) ≅ Γ^∞ = Γ^* ∪ Γ^ω`，有限与可数无穷历史
   dcpo；有限历史恰是紧元素，每条无穷历史是其有限前缀有向并（经典理想完备化定理，实例化）。
3. **求值**：由自由 dcpo 普遍性质，`ev` 对所有历史延拓为 Scott 连续映射当且仅当 `ev` 单调。普通
   算术求值不单调（且部分，值域非 dcpo），故**非**序连续；这记录为阻碍，并激励下半连续/单调扇区
   与 `paper-1/sections/03-projective-affine.tex` 射影延拓。

仍开放：分支（非脊柱）情形、具体单调扇区 + 值 dcpo 实例化，与射影延拓调和。

## OQ-092 — 加法对乘法侧序论放置

**优先级：** P3
**状态：** RESOLVED (2026-10-31) — 对应在值格 `[0,∞]` 上精确，带对 `09` §6 修正（对偶侧由倒数
对合携带，非乘法本身）。算子级后向伴随对接折入 OQ-093。

**问题：** `09` §6 对应（"Scott ⟷ 加法 / 前向 / 累积侧；下拓扑 ⟷ 乘法 / 后向 / 缩放侧"）当前是
直觉。什么映射或实现把 AEG 加/尺度过程结构送到值格序使对应成为定理（或被反驳）？

**为何重要：** 这是合理化读 AEG 单侧累积为下半连续（`[0,1]`-值，Scott 拓扑）且其后向伴随为对偶/
下侧而非松散类比的桥。

**当前证据：** `09` §9 现构造映射。连续格 `L=[0,∞]` 上，加法生成元 `T_s(a)=a+s` 是 Scott 连续
嵌入且恰是 way-below 见证（`a ≪ b ⟺ ∃s>0: a+s ≤ b`）；乘法生成元 `D_k(a)=ka` 是 Scott 自同构
（序自同构）。对偶/下侧由序反转倒数 `¬(a)=1/a` 携带，是 `(L,σ) → (L,ω)` 同胚共轭 `D_k` 到
`D_{1/k}`。§6 措辞「下拓扑 ⟷ 乘法」故不精确且被修正。

**开放时默认规则：** 保持 Scott/下对应为启发式；仅如此引用。

**解决条件：** 从加/尺度过程到连续 frame 的具体映射（或反例），加证明该映射下 Scott 连续 ↔
下半连续累积且对偶拓扑 ↔ 后向侧成立。

**受影响文件：** `notes/analysis-and-calculus/09-order-topology-scott-lawson.md`、
`notes/analysis-and-calculus/02-mixed-affine-integration.tex`。
**受影响定理节点：** 无。
**拥有者：** 作者。
**决定记录：** `governance/notes-reserve-audit.md` §2.7（覆盖缺口）。

### Resolution — 2026-10-31

在带 Scott 拓扑 `σ` 与下拓扑 `ω` 的连续格 `L=[0,∞]` 上：

1. **加法侧**：加法生成元 `T_s(a)=a+s`（`s≥0`）是 Scott 连续嵌入（`s>0` 非满）且恰是 way-below
   见证：`a ≪ b ⟺ a < b ⟺ ∃s>0, a+s ≤ b`（紧底 `0` 为唯一例外）。故加法 = Scott 拓扑逼近 /
   way-below 原语——「从下累积」方向。
2. **乘法侧**：`D_k(a)=ka`（`k>0`）是序自同构，故 Scott 同胚（「尺度对称」原语）；对数坐标中是
   平移。
3. **对偶侧**：倒数 `¬(a)=1/a`（`0↔∞`）是序反转双射，故 `(L,σ) → (L,ω)` 同胚，且
   `¬∘D_k∘¬ = D_{1/k}`，即互换前向尺度 `e^M` 与后向乘子 `e^{-M}`。故下/后向侧由对合携带，且
   `ω = ¬_*σ`；这恰是 Warner 遗漏对合。

故 §6 对应以精化形式成立：加法 ⟷ Scott（way-below / 前向累积）；乘法 ⟷ Scott 自同构（尺度对称）；
下/后向 ⟷ 倒数对合。先前「乘法本身是下拓扑侧」陈述被修正。剩余任务——把 `¬` 与
`02-mixed-affine-integration` 后向伴随 `p(b)=1` 在算子方程层匹配——折入 OQ-093。

## OQ-093 — Scott ∨ 下 = Lawson 作后向伴随完备化拓扑形式

**优先级：** P3
**状态：** RESOLVED (2026-10-31) — 后向伴随乘子是前向尺度倒数对合像，其并恰是 Lawson（Euclid/
Hausdorff）拓扑；见下解决。

**问题：** 把对偶（下）拓扑并到 Scott——即升到 Lawson 拓扑——是否实现 AEG 双边（加 × 乘，前向 ×
后向）结构，Hausdorff/Euclid 拓扑恢复对应 `02-mixed-affine-integration` 后向伴随完备化？

**为何重要：** 这是 Warner 导入最强潜在回报：它把「补上 Warner 故意丢掉的对合」解释为「从 Scott
升到 Lawson」，即缺失对合侧 = 后向伴随乘子 = 下拓扑。当前是猜想。

**当前证据：** `09` §10 现证明对应。从 `02-mixed-affine-integration.tex`，前向尺度是
`K(t)=e^{M(t)}` 且后向伴随是 `p(t)=exp(∫_t^b v)`、`p(b)=1`；直接计算给
`p(t)=e^{M(b)}·¬(K(t))` 带 `¬(a)=1/a`。由 `09` §9.3，`¬` 是序反转同胚 `(L,σ)→(L,ω)`。故前向尺度
是 Scott（从下）侧，后向伴随是下（从上）侧，其并是 Lawson = Euclid。

**开放时默认规则：** 不声称加/乘双边结构是 Scott/Lawson 双边结构。

**解决条件：** 证明（或反例）AEG 混合演算后向伴随/对偶侧在 OQ-092 映射下对应下拓扑，使其并恢复
经典对称几何。

**受影响文件：** `notes/analysis-and-calculus/09-order-topology-scott-lawson.md`、
`notes/analysis-and-calculus/02-mixed-affine-integration.tex`。
**受影响定理节点：** 无。
**拥有者：** 作者。
**决定记录：** `governance/notes-reserve-audit.md` §2.7（覆盖缺口）。

### Resolution — 2026-10-31

从 `02-mixed-affine-integration.tex`（`eq:acs-path`、`eq:adjoint-solution`），带乘法 charge
`M(t)=∫_a^t v`：

1. 前向尺度 `K(t)=e^{M(t)}`（直接 / 过去加权）；
2. 后向伴随 `p(t)=exp(∫_t^b v)`、`p(b)=1`，解 `-p'(t)=v(t)p(t)`；
3. 直接计算：`p(t)=e^{M(b)-M(t)}=e^{M(b)}·¬(K(t))`、`¬(a)=1/a`。

由 `09` §9.3，`¬` 是序反转同胚 `(L,σ)→(L,ω)` 带 `ω=¬_*σ`。因此：

- 前向尺度 `K` = Scott / 下（从下）侧：`K(t)>a ⟺ M(t)>log a`；
- 后向伴随 `p=¬(K)`（模常量 `K(b)`）= 下 / 对偶（从上）侧：`p(t)>a ⟺ M(t)<M(b)-log a`；
- 其并 `σ ∨ ω = λ` = Lawson = `[0,∞]` / `[−∞,+∞]` 上 Euclid 拓扑（经典）。

故后向伴随完备化 = 并 `¬(K)` = 过 Scott → Lawson = 恢复 Hausdorff/Euclid 拓扑，恰如 OQ-093 猜想。
常量 `K(b)=e^{M(b)}` 是终端条件 `p(b)=1` 固定的参考尺度。

残差（非阻塞注）：混合积分 `𝔐[u;v]=∫_a^b p·u` 本身在双边数据上 Lawson 连续的泛函级陈述尚未表述；
加法源 `u` 经 `09` §9.2 way-below 原语与配对 `eq:adjoint-pairing` 进入。

`09` §11 处理（2026-10-31）：`𝔐` 在 `u` 与 `v` 分别 Scott 连续（非负密度），`∫u·p` 是双边对偶
配对——Scott ∨ 下 = Lawson 的泛函级形式。

## OQ-094 — Paper I 仿射扇区与 PGL₂ 的 Scott/Lawson 读法

**优先级：** P3
**状态：** 094a RESOLVED (2026-10-31) — 可证明核心、Galois 连接步与函子语言全关闭
（`11-oq094a-proof-skeleton.md`、`12-galois-connection-oq094a.md`、
`13-functorial-language-oq094a.md`）。094a 精确形式是：`Scott ⟷ Aff^+ = C(σ)∩B_∞ =
{ka+s : k>0, s≥0}`、`Lawson ⟷ PGL₂ = ⟨Aff^+, ¬⟩`，带「并 ¬」交换（`Φ(σ∨¬_*σ) = ⟨Φ(σ),¬⟩`），
且是「生成数据 + 并 ¬」自然同构，*非* `Top(L)` 上完整 Galois 等价（三证明理由：`A(σ)=A(λ)`、
`H(λ)=Stab([0,∞])⊊PGL₂`、`¬T_s¬∈E(σ)∖Aff^+`）。

094b RESOLVED (2026-10-31) — `14-rho-scott-continuity-boundary.md` 证明干净否定：`ρ` 仅对平凡
预序单调（故无到历史 dcpo `Γ^≤ω` 的 Scott 连续延拓），唯一候选极限延拓是无穷矩阵积 = 连分数
收敛，即被排除的「无穷算术表达式一般收敛理论」（Paper II/III）。这给 Paper I 有限词范围序拓扑 +
解析理由。

094c RESOLVED (2026-10-31，核心) — `15-branching-history-dcpo.md` 给分支历史 dcpo：信息序 = 下集
（序理想）嵌入（"子计算"）、理想完备化 = 有限 ∪ 无穷计算 DAG（每运算有限多前驱）、紧 = 有限；脊柱
前缀序是链特化（定理 2）；部分求值形成有限分配格 `O(P)` 且合法求值序 = 线性扩张 = 极大链 = 脊柱
历史（定理 3，Birkhoff）。残差（非阻塞）：携带运算/常量/手性标签，与分支 `ev` Scott 连续扇区。

094d RESOLVED (2026-10-31) — `16-hecke-history-boundary.md`：Hecke 历史空间 `Γ_4^≤ω` 是 Cantor
空间（于 `10`/`12` 证明）；`G_4 ≅ C₂*C₄` 几乎自由故其端空间是 Cantor 集，而 `G_4 = H(√2)` 是
第一类 Fuchsian 格其极限集是全圆 `P^1(ℝ)`（非 Cantor）。历史 Cantor 空间编码端空间（符号边界），
实现 `rem:hecke-history-operator-coset` 历史级形式。这修正 `10` §4「Cantor 边界」措辞（Cantor =
端，非极限集）。完整胞腔化 + 极限集对应推迟到 Paper II/III。

OQ-094（094a–094d）现全处理。

**问题：** `09` 笔记关闭其值格链，但该链在 `[0,∞]` 与解析层（`02-mixed-affine-integration`）上
工作。同 Scott/Lawson 框架能否读回 Paper I *主体*——历史层
（`paper-1/sections/02-sequential-histories.tex`）与射影语义
（`paper-1/sections/03-projective-affine.tex`）——使仿射/射影二分与 Bruhat 分解获序拓扑含义？

**为何重要：** `09` §9.1 三生成元字面是 Paper I 三初等语境（`T_s = C_{+,s}^{(1)}`、
`D_k = C_{×,k}^{(1)}`、`¬ = C_{/,1}^{(2)}`），故「Scott → Lawson」（并倒数对合）群论上是「仿射扇区
`B_∞` → `PGL₂`」（并射影步 `J = -1/z`）同移动。若精确则给 Paper I §3 仿射/Borel 放置与秩一 Bruhat
分解拓扑理由而非纯代数。

**当前证据：** `10` §1–§5 记录精确对应与诚实否定结果（算子映射 `ρ` 在 `PGL₂` 上不带 dcpo 序，故
「ρ 的 Scott 连续」在固定序前不适定；`ρ` 的无穷历史极限是无穷矩阵积 = 连分数收敛，即被排除的
Paper II/III 收敛论）。历史层拓扑经典：`Γ^∞ = Γ^* ∪ Γ^ω` 上前缀 dcpo 的 Lawson 拓扑是积拓扑
（有限 `Γ` Cantor 空间，可数 `Γ` Baire 空间）。

**开放时默认规则：** 保持「Scott ⟷ 仿射扇区，Lawson ⟷ PGL₂」对应为 `structural proposal`；仅如此
引用；不陈述 `B_∞` 与 Scott 空间或 `PGL₂` 与 Lawson 空间拓扑等价。按 `11` §2/§6，精确读法是
`Scott ⟷ Aff^+`（正仿射*半群* `{ka+s : k>0, s≥0}`，= `B_∞ ∩ Stab([0,∞])`）与
`Lawson ⟷ PGL₂ = ⟨Aff^+, ¬⟩`；群 `⟨T_s(s≥0), D_k(k>0), ¬⟩` *确*等于 `PGL₂`（因
`D_{-1} = T_1¬T_{-1}¬T_1¬`），但 Scott *侧*是半群 `Aff^+`，其群闭包是恒等分量
`B_∞^+ = {ka+s : k>0, s∈ℝ}`，非全部 `B_∞`；反射 `D_{-1}` 需 `¬`。写这些时区分半群与群闭包，及
`B_∞^+` 与 `B_∞`。

**解决条件：** 对 094a，在生成元与 Bruhat 胞腔层匹配 `[0,∞]` Scott/Lawson 结构到 `B_∞`/`PGL₂` 的
显式函子/序，尊重 `10` §3 三域警告。对 094b，「无穷矩阵积 = 范围外收敛」边界干净陈述与证明。对
094c，分支历史上带识别紧元素的有向完备子 DAG 精化序。对 094d，Hecke 胞腔/陪集接口
`rem:hecke-history-operator-coset` 历史级拓扑实现。

**受影响文件：**
`notes/analysis-and-calculus/10-scott-lawson-on-paper-1-main-body.md`、
`notes/analysis-and-calculus/11-oq094a-proof-skeleton.md`、
`notes/analysis-and-calculus/12-galois-connection-oq094a.md`、
`notes/analysis-and-calculus/13-functorial-language-oq094a.md`、
`notes/analysis-and-calculus/14-rho-scott-continuity-boundary.md`、
`notes/analysis-and-calculus/15-branching-history-dcpo.md`、
`notes/analysis-and-calculus/16-hecke-history-boundary.md`、
`notes/analysis-and-calculus/09-order-topology-scott-lawson.md`。
**受影响定理节点：** 无（研究笔记；无 Paper I 定理节点依赖）。
**拥有者：** 作者。
**决定记录：** `11` §6（2026-10-31，v0.3）精化 `10` §2：正确层是半群 `Aff^+ = {ka+s : k>0, s≥0}`
（= `B_∞ ∩ Stab([0,∞])`）、其群闭包 `B_∞^+ = {ka+s : k>0, s∈ℝ}`（恒等分量）、完整仿射群
`B_∞ = B_∞^+ ⊔ D_{-1}B_∞^+` 与经 `D_{-1} = T_1¬T_{-1}¬T_1¬` 的 `PGL₂ = ⟨Aff^+, ¬⟩`。反射
`D_{-1}` 是对偶数据（需 `¬`），故 `B_∞` 非纯序单侧。`12` §3（2026-10-31）证明 Galois 连接交换性：
同胚层 `Homeo(L,σ)∩PGL₂ = {D_k}` 与 `Homeo(L,λ)∩PGL₂ = Stab([0,∞]) = ⟨D_k,¬⟩`（仅达真子群），
而自同态层 `Aff^+ = C(L,σ)∩B_∞` 与 `⟨Aff^+,¬⟩ = PGL₂`（完整群）；后者使「Lawson ⟷ PGL₂」成立。
`13`（2026-10-31）完成函子语言：对应是生成集 `S_0 = {T_s, D_k}` 上交换方带「并 ¬」自然性
`Φ(σ∨¬_*σ) = ⟨Φ(σ),¬⟩`，且*非* `Top(L)` 上完整 Galois 等价（三函子 `A, E, H` 分别坍缩
`σ`/`λ`、过冲或欠冲——于 `13` §4 证明）。`14`（2026-10-31）解决 094b：`ρ` 仅对平凡预序单调
（Thm 1），故无到历史 dcpo 的 Scott 连续延拓；唯一候选极限延拓是无穷矩阵积 = 连分数收敛（Thm 2），
即被排除收敛论。`15`（2026-10-31）解决 094c（核心）：分支历史在下集（序理想）嵌入下形成 dcpo
`Idl(FinDAG)` = 有限 ∪ 无穷计算 DAG，紧 = 有限；脊柱前缀序是链特化；部分求值 = 有限分配格
`O(P)` 带线性扩张 = 极大链 = 脊柱历史（Birkhoff）。`16`（2026-10-31）解决 094d：Hecke 历史空间是
编码几乎自由群 `G₄ ≅ C₂*C₄` 端空间的 Cantor 空间（非极限集——`H(√2)` 第一类带极限集 `P^1(ℝ)`），
修正 `10` §4。

## OQ-095 — 宏观 Stokes 与完整 DAG Lie 实现（Scott–Lawson 主线残差）

**优先级：** P3
**状态：** OPEN (2026-10-31) — 从 `governance/scott-lawson-paper-1-integration-2026-10-31.md`
§5 登记；子项 095.1–095.4。

**问题：** Scott/Lawson 主线（`notes/analysis-and-calculus/09`–`20`）建立可证明核心：接触曲率
`μλ` 是最小分支 DAG `{A,M}` 的序缺陷，集成为群值 1-余循环（`20`）。宏观推广——任意分支 DAG 的
「`O(P)` 上离散 Stokes」与完整 DAG Lie 实现——尚未建立。

**为何重要：** 这是把「接触 = 最小 DAG 无穷小形式」（`17`）升级为「曲率 `μλ` 在任意 `O(P)` 上
积分到任两线间序缺陷」（`19` §3）的步。它是连接无穷小（接触）到宏观（DAG）的积分论，是超出最小
反链的忠实体边界对应门。

**当前证据：** `20` 证明缺陷是线性扩张图上 1-余循环（telescoping 可加性、局部缺陷 = 共轭交换子、
六边形 = Jacobi 恒等）。`19` §2 证明最小情形全息 Stokes。下方四残差开放。

**开放时默认规则：** 引用宏观 Stokes 与完整 DAG Lie 实现仅作 `structural proposal` / `open
problem`；不陈述任意 `P` 缺陷积分为已证明。

**解决条件：**
- 095.1（高阶括号）：识别 BCH 高阶项 `[X,[X,Y]]`、`[Y,[X,Y]]`、… 与 `O(P)` 高维胞腔中嵌套反链
  边缺陷。
- 095.2（完整 DAG Lie 实现）：从分支历史 dcpo（`15`）到自由 Lie 代数 / 自由流群的函子，把 `18`
  的 `F` 从两生成元推广到任意生成元集。
- 095.3（宏观 Stokes）：用 1-余循环（`20`）与可加性/精确性/谱对接把 `19` §3 组装为完整陈述——
  任意 `P` 两线间缺陷 = 区域上 `∫∫ μλ`。
- 095.4（谱对接）：`O(P)` 的 Scott/Lawson 拓扑（`15` §6）作离散 Stokes 复形谱空间。

**受影响文件：**
`notes/analysis-and-calculus/15-branching-history-dcpo.md`、
`notes/analysis-and-calculus/18-limit-smoothing-functor.md`、
`notes/analysis-and-calculus/19-integration-and-bulk-boundary.md`、
`notes/analysis-and-calculus/20-defect-1-cocycle-bch.md`。
**受影响定理节点：** 无（研究笔记；无论文定理依赖）。
**拥有者：** 作者。
**决定记录：** `governance/scott-lawson-paper-1-integration-2026-10-31.md`。

## OQ-096 — 裤、界面盘与认证封顶

**优先级：** P2
**状态：** OPEN (更新 2026-11-05)；096.1 已完成 V1 与 V3 有限校准及带显式假设的固定链证明；
一般装饰 DAG 复合与分解相容仍开放。096.2 有完成 V2 有限观测示例，但其一般状态/谱问题仍开放。
子项 096.3–096.4 仍开放；096.5 记录 handle/环向。
**起源：** 苑明理要求澄清裤、DAG 替换、共享边界帽及其谱值后再赋 Adva 封顶几何含义。Codex
（OpenAI）在笔记 25 形式化初始提案与有限阻碍；不断言独立人工数学审查。

**问题：** 装饰有限程序能否由相容球–管加厚呈现，其曲面裤沿内部界面盘边界胶合，界面态由精确
替换复合且保留证据支持精确范围闭包证书？

**当前证据：** `notes/analysis-and-calculus/25-pants-interface-disks-and-substitution.md` 对指定
拓扑模型、多项式界面示例与 `mu` 非零时整边界常量赋值紧正则 AES 盘不可能性给短证明。Paper IV
PIV-S1–S4 已供有限程序替换与条件 collar 下降。模型规范 AEG 状态及其与原生 Seal 关系开放。

**子项与解决条件：**

- **096.1 — 装饰有限加厚与复合。** 从两节点示例 `z=x+y; w=zt` 开始：构造并检查有限胞腔化、
  局部流形链环、盘/缝边界恒等、四外部端口与对替换精确对应。然后扩展到相容复合，保持槽、来源、
  出现与不同回执；拒绝全局反馈。单示例不关闭此子项。
- **096.2 — 界面态、谱与重开。** 定义观测代数/状态载体；区分相等数值与生产身份；在更强观测者
  下展示保留残差恢复。普通算子谱、序谱与界面特征空间不由术语等同。从代数谱 `Spec Q[z]`（值层）
  到下集格 `O(P)` Stone 谱（序层）无桥建立；前者紧开格是否关联后者下集格 `O(P)` 开放。缝圆
  holonomy 是序缺陷解析实现（经曲率 + Stokes 从 `P` 导出），仅由常量边界封顶阻碍链接到代数谱，非
  导出（`rem:three-interface-layers`）。
- **096.3 — AES 扩张或显式奇异封顶。** 指定实际度量/赋值 collar 并证明其扩张或精确阻碍。尊重
  笔记 25 常量边界阻碍与 Paper 0 本质穿孔定义；数值端口标签非常量几何边界数据。
- **096.4 — 保证据原生 Seal 桥。** 定义从一个显式几何闭包义务到当前见证核的映射并证明其加法/
  乘法残差检查认证什么。保留体、源历史与非零义务。仅盘或匹配值不能签发 Seal。
- **096.5 — Handle 手术与环向界面相容。** 显式积隧道、从 boundary(D)=C 到 boundary(A)=C-c 变更、
  双裤胶合与条件环向 Stokes 平衡有论文内证明。定义两边界状态空间与其算术相容关系，保持槽/出现/
  生产残差，确定哪些装饰手术承认正则 AES 数据或指定奇异扩张。指定所选手术是否保持数值函数；
  仅拆分–合并不必。事件偏序或端点值相等都不决定这些几何数据。

**开放时默认规则：** 指定加厚仅作研究呈现。不与正则 AES、理想完备化边界、TQFT 或原生 Adva 接纳
等同。保持纯数据流调度与共享累加器上非交换作用分离。OQ-095 仍开放且非有限拓扑示例前置。

**有限更新（2026-10-31）：** V1 于 `research/pants-interface-disks/` 实现：56 立方、336 四面体、
全部 132 整体顶点链环检查、两三边界裤与一四边界侧曲面。显式内部盘填缝圆，而侧曲面模二边界矩阵
秩 110 增广秩 111：同圆不围曲面二链。精确替换给界面 5 与输出 20。十负控制拒绝；普通/优化输出与
新进程保存候选接收一致。这是同一作者有限校准，非一般加厚函子或原生 Adva 执行。它记录苑明理互补
曲面孔/体盘观为精确界定结果。

**手稿更新（2026-10-31）：** Main 合卷修订已把笔记 25 集成进 Paper I 帽章。handle 后继加
`prop:tunnel-boundary-surgery`、`prop:pierced-cap-annulus`、`prop:double-pants-dag-handle` 与
`prop:annular-stokes-balance`，带界审计与 PI-H1–PI-H6 状态记录于
`paper-I-handles-integration-2026-10-31.md` 与 `05-mathematical-status.md`。27/26/24 立方球、凹痕
与隧道校准补充那些证明；非计划等值残差实验 V2。

**受影响文件：** 笔记 25、`research/pants-interface-disks/`、
`paper-1/sections/08-caps-and-interface-disks.tex` 与附录 D。
**受影响定理节点：** 上四 handle/环向命题；这些集成论断取代先前仅笔记处置。
**拥有者：** 作者。
**V2 有限更新（2026-11-02）：** `research/pants-interface-disks/v2/` 冻结五两门实例独立契约，保持
所有 V1 文件未变。A=`2+3` 与 B=`1+4` 有同数值观测 `(5,20)` 但不同保留源历史。等操作数/不同源 C
仍分离；新出现/同源 A-copy 保持等价于 A。第五实例产 `(6,24)`。数值划分两类源划分四类；全部 30
端口出现与 10 事件出现不同。二十包突变拒绝，含重哈希等值源替换、恒等坍缩、错误槽与缺失残差。
保存回执与四改变证据文件在新进程检查；普通/优化重放一致。这是同一作者 COMPUTATIONALLY VERIFIED
EXAMPLE，非独立实现审查。重开读保留源界残差；不反转数值商。不认证 DAG 形变、谱桥、AES 扩张或
原生 Adva Seal。

**V3 有限更新（2026-11-05）：** `research/pants-interface-disks/v3/` 实现前冻结契约（commit
`79059293934caa0e0b1e674ac4c51e336f01a433`）并保留全部 15 先前 V1/V2 文件。三块是 Q(x,y)=x+y、
P(z)=4z、R(w)=1/w 带严格 w!=0。对 41 请求（五 V2 赋值加 6x6 有理网格），两括号对 36 可允许请求
产相同装饰记录且两者拒绝五零域请求。980 源对尝试接受五拒绝 975，含 107 数值未变拒绝；32 保存负
包拒绝。全部 18 额外边候选拒绝，含 12 有向环。分离 JavaScript 与 Python/Fraction 路径一致；各在
新进程接收 68 保存包。同模型作者，非独立人工审查。

`v3/MATHEMATICS.md` 给 F1（带预分配不相交出现、不可变源、序带型槽、完整残差保留与严格域的固定三
块链）、F2（一个等值源绑定可违反调用者请求）与 F3（只保留最新缝产非结合残差尽管数值函数结合）的
显式证明。这些是有限模型命题，非一般装饰 DAG 定理。窄 Paper I 命题数学合格；此实验不改 LaTeX
陈述。不认证新几何加厚、AES 扩张、谱桥或原生 Adva Seal。

**下一有界目标：** 带显式复制与区分复用源与共享事件出现的固定规则的四块菱形；声称一般相容前比较
两声明分解并审计重叠子图。096.2 一般状态/谱义务仍分离。AES/Seal 桥仍分离 V4 义务。

---

## OQ-097 — 曲面级数（Magnus 级数投影到 Legendre 商）

**优先级：** P2
**状态：** OPEN (2026-10-31) — 随演算字典曲面列重写登记；级数支柱为体发展，非曲面。

**问题：** 级数支柱（Paper I §6）的 Magnus 级数 `Ω(γ)` 在体接触模型自由 Lie 代数中展开。它到两
Legendre 商——charge 平面 `π` 与 Reeb 商 `Q`——的约化是什么，且何意义下该约化是「曲面级数」？

**为何重要：** 演算字典曲面列现是 Legendre 对 `(π, Q)`，其微分与积分演算符号（`π` 上
`e^{M_*−M} dA∧dM`、`Q` 上 `dvol`）。级数列无对应符号曲面形式：唯一候选约化是连分数作规范
`Q`-边界形式（`prop:bulk-boundary-series-reduction`），是结构提案非定理。符号曲面级数会完成四列
字典（经典 / 体 / 曲面 / 级数）Taylor 行。

**当前证据：** `prop:bulk-boundary-series-reduction` 记录度下降（二形式曲率 → 一形式势，Stokes）
与余循环约化（1-余循环闭内消），两者证明，及连分数规范形式，结构提案。PBW 交换化
（`thm:pbw-abelianization-difference-substitution`）是体交换化，非投影到 `π` 或 `Q`。

**开放时默认规则：** 不陈述符号「曲面级数」为已证明。引用连分数仅作结构提案；保持级数列曲面胞
标开放（OQ-097）。

**解决条件：**
- 097.1：`Ω(γ)` 到 charge 平面 `π` 的良定义约化（`e^{−M}`-归一化 / 加权级数）带收敛或渐近陈述。
- 097.2：到 Reeb 商 `Q`（双曲 / 连分数侧）的良定义约化及其与 097.1 在 Legendre 对偶下关系。

**受影响文件：** `paper-1/sections/07-calculus-dictionary.tex`、`paper-1/sections/06-series-theory.tex`。
**受影响定理节点：** 无（无 Paper I 定理依赖曲面级数）。
**拥有者：** 作者。
**决定记录：** 曲面级数是 OQ-095.3/OQ-095.4（宏观 Stokes 与谱对接）级数侧对应；随 2026-10-31
演算字典曲面列重写登记。

---

## OQ-098 — Donaghey / De Bruijn–Morselt 变换与 AEG 树层

**优先级：** P2
**状态：** OPEN (2026-10-31)；098.1 于梳层 RESOLVED (2026-10-31) — AEG 的 `m,r` 交换且在词与梳
两层都给 `Z₂×Z₂`（Klein）（笔记 27），故非交换 `Z₂*Z₂` *非*由传输 AEG 现有运算获得；问题转向分支
层（`θ̃` 自然性、分支树 `τ`）。098.1(b) RESOLVED NEGATIVE (2026-10-31) — `τ` 不下降到依赖偏序 /
`O(P)`（笔记 29）。098.2 ADVANCED (2026-10-31) — 「分配格」短语是无穷立方树 Birkhoff 下集格，非
Tamari（旋转）格；AEG 的 `O(P)` 是有限偏序上同构造（笔记 28）。098.3–098.4 仍开放。纯组合对应
于笔记 26 建立。

**问题：** 经典一般树 ↔ 二叉树双射（De Bruijn–Morselt / Donaghey）与 Donaghey 变换
`τ = φ⁻¹θφσ` 是 AEG 保持不同运算（镜像 `m`、时间反演 `r`、路径逆）的精确组合模型。随之两事且
部分开放：**非交换扩张**与**格/轨道对应**。

**为何重要：** 笔记 26（§6）记录真正结构差异。AEG 词级镜像 `m` 与反演 `r` 交换，故
`⟨m,r⟩ ≅ Z₂×Z₂`（Klein）。但 Donaghey 树级转置 `σ` 与（共轭）反射 `θ` 不交换：Pushkarev–Byzov
定理 6.4 证明 `⟨σ,θ⟩ ≅ Z₂*Z₂`（无限二面）且 `τ` 无限阶（推论 6.3：任意长轨道）。两「反演」运算
不同——词反演 `r` 是纯序列反演，而路径反演诱导树对合 `φ⁻¹θφ` 是真正树重构——恰是 Donaghey 论文
「双曲性」来源。若 AEG 树层展示非交换（`Z₂*Z₂`，无限阶）版本，路径逆/反演区分比词级 Klein 结构
丰富。

**当前证据：** 笔记 26、`notes/analysis-and-calculus/26-donaghey-general-to-binary-tree.md`。
紧 `[对应]` 项：`σ ↔ m`、`θ ↔ r`、`φ ↔` 上下码、右/左双射 ↔ `conv:p0-left-right-convention`
（右/左梳）、四 Catalan 族 ↔ 二叉对一般树。差异 `Z₂×Z₂` 对 `Z₂*Z₂` 是精确群论事实；树级实现
开放。

**子项与解决条件：**

- **098.1 — 非交换扩张。** *于梳层解决（笔记 27）。* AEG 镜像 `m` 与反演 `r` 交换
  （`def:mirror-temporal-reversal`），且词 ↔ 梳双射（`prop:marked-tree-history-correspondence`）
  保持交换，故对在两层生成 `Z₂×Z₂`（Klein）；相容 `n=2` 梳计算确认 `mr=rm`。Donaghey `σ` 等于
  `m`，但其反演 `θ̃=φ⁻¹θφ`（Dyck 路径反射）**非** AEG 的 `r`（词反演），且 `τ` 无限阶 / 任意长
  轨道构造于*分支*树（完全树 + fringing，Cor 6.3），非梳。故非交换 `Z₂*Z₂` 非 AEG 现有运算扩张。
  *转移残差*：(a) [RESOLVED，笔记 43] 是否有「路径反射」`θ̃ ≠ r` 内在 AEG 定义，且它与 `m` 生成
  `Z₂*Z₂`？——是：因 `τ = φ⁻¹θφσ` 且 `σ = m`，有 `θ̃ := φ⁻¹θφ = τ∘m`（经 `τ` 与 `m` 定义，无
  Dyck 路径）。它是对合，且 `m∘θ̃ = τ⁻¹`，故 `⟨m,θ̃⟩ = ⟨m,τ⟩ ≅ Z₂*Z₂`（Donaghey Thm 6.4）。对
  `n ≤ 6` 验证（`research/iota-carousel/verify_theta.py`：`θ̃²=id`、`m∘θ̃=τ⁻¹`、`θ̃` 轨道长 1 或
  2）。内在词级公式与直接「轮廓反射」描述仍开放。(b) [RESOLVED NEGATIVE，笔记 29] 分支层（依赖
  偏序 `P`、`O(P)`）是否复现 `τ` 无限阶 / 「双曲」行为？——否：`τ` **不**下降到依赖偏序 / `O(P)`；
  同构依赖偏序两树可映射到依赖偏序不同树（显式 `n = 4` 见证：一 3 链类树映射到 3 链另一到「V」；
  每骨架类对 `n ≥ 5` 有非唯一 `τ` 像，验证 `n ≤ 8`，`research/donaghey-orbits/verify_descent.py`）。
  双曲/长轨行为严格是**平面树**现象，非偏序层。
  *提升残差，有限证据（笔记 46，2026-11-01；一般 `n` 开放）：* 即使*粗*偏序统计也非 `τ` 不变。
  对所有 `n ≤ 6`，`e(P)`（线性扩张）、`|O(P)|`（下集）、`height(P)`、`incomp(P)`（不可比对）无一
  被 `τ` 保持——`n = 4` 见证：`N(L,N(N(L,L),L))` 有 `e = 1` 但其 `τ` 像 `N(N(L,L),N(L,L))` 有
  `e = 2`（链类 -> 分支）（`research/iota-carousel/verify_lifting_trace.py`）。真正不变量是**平面**
  角型 `(k,l) = (#LL, #RL)`，沿每轨道到交换保持（Pushkarev–Byzov Cor 4.5，验证）。故**在检查范围
  `n ≤ 6` 内** `τ` 在 `O(P)` 层不留粗 trace；其那里 trace 是平面的。残差：一般 `n` 陈述（有限检查
  不证明）；偏序统计轨道级*分布*是否保持；笔记 41 平面性阻碍第五次出现。
  (c) [开放] `τ` 在毛虫上一般 `n` 结构（「`2^{n-2}` 中仅 `n-1` 映射到毛虫」对 `n ≤ 10` 验证但未
  一般证明）。**有限更新（2026-10-31）：** `research/donaghey-orbits/` 实现 `τ`（Pushkarev–Byzov
  Def. 2.1）并对 `n = 1..10` 复现 Donaghey `M_n(x)`；毛虫（单脊柱 / 梳树）**不**被 `τ` 保持
  （`2^{n-2}` 中 `n-1` 猫→猫），且每条长度 `> 6` 轨道全分支。这是同一作者有限计算
  （`COMPUTATIONALLY VERIFIED EXAMPLE`，`n ≤ 10`），非一般证明。
- **098.2 — PPCT 格对 `O(P)`。** *ADVANCED（笔记 28）。* Pushkarev–Byzov 文本说 PPCT 形成「其
  不可约元按无穷立方树顶点排序的分配格」。此短语混淆两不同格。(A) PPCT 上 **Tamari / 旋转格**是格
  但**非分配**（对 `T_4`、`n = 5` 叶验证：`research/ppct-lattice/`）。(B) 无穷二叉（立方）树
  **Birkhoff 下集格**由构造分配，join-不可约元 = 顶点且大小 `N` 下集 `R(N) = Catalan(N)`；其
  *元素*是下集（有序二叉树 / 平面树），非直接完整二叉 PPCT。故「分配 + 不可约 = 无穷立方树」匹配
  (B)；笔记 28 把「所有树标准格排序」读为 (A)，下 (i) OCR 把该读修正为 (B)。两格作对象互斥。AEG
  的 `O(P)`（`thm:birkhoff-downset-spinal`）是有限依赖偏序 `P` 上**同 Birkhoff 构造**，故分配读
  与 AEG 对齐；两者一般**不同构**（不同偏序）。*残差及其解决（笔记 45，2026-11-01）*：(i)
  Pushkarev–Byzov §5 OCR 句读「not monotone with respect to the **standard lattice ordering of
  all trees**（**recall that the PPCTs form a distributive lattice whose irreducible elements
  are ordered as the vertices of the infinite cubic tree**）」——括号**定义**「标准格排序」为分配
  （下集）格序，**非 Tamari**；这修正笔记 28「最可能 Tamari」读法（无论如何「分配 + 不可约」对象
  是 `Down(T_∞)`）。(ii) `O(P)` 对 `Down(T_∞)` 精确关系：`O(P) = Down(P)` 是 `Down(T_∞)`（更精确
  地，含 `P` 的有限子树 `Q ⊂ T_∞` 的 `Down(Q)`）的**格商**：限制 `ρ: S ↦ S ∩ P` 是**满射格同态**，
  对四小 `P` 验证（`research/iota-carousel/verify_downset_quotient.py`）。它**非子集子格**
  （`Down(P) ⊄ Down(Q)`）；是否作为某 `Down(Q)` **抽象子格**嵌入仍开放。现残差：嵌入问题；子集子格
  精确条件；「标准格排序」原始来源（Donaghey 1980 无「分配格」陈述，只有 Huang–Tamari「格性质」
  引用）。
- **098.3 — Carousel / fringing / 轨道增长。** 决定 carousel 效应（角类 SR/LL/RL/RN/LN 循环运动）、
  fringing 定理（`Δ(Q(T)) = 3Δ(T)` 或 `(3/2)Δ(T)`）与 `O(n^{log₂ 3})` 轨道增长是否对应 AEG Hecke
  周期轨道 / 「分形旋转」（Pushkarev 名）。这需 AEG 自身轨道/周期结构。*Iota 方向加（笔记 31，
  2026-11-01）：* carousel **类级核心是 4-环**（`LL→RL→RN→LN→LL`，`SR` 基，指标平移），而其
  **计数影子是对合**（阶 2，计算）。AEG **iota**（六态载体，`Ω=TSR`，`Ω²=-1`）与 Adva **iota
  框架**（`J²=-I`）是**同手性载体**（`W=Λ¹E⊕Λ²E`，`(T⊕SR)⊕(S⊕RT)⊕(R⊕TS)`）；两者给带手性符号律
  的 Z/4 复单位（偶/循环保持 `Ω`，奇/转置翻转）。故自然猜想：carousel 4-环是 iota 复单位离散影子，
  指标 `k` 是单独高度/平移。状态：`structural proposal`/猜想；阶 2 对阶 4 不匹配开放。Adva **iota
  组合子**（SKI 单组合子基）*非*载体：adva `0168` 已排除其下辫/开关/交换（收敛对发散）。*对齐结果
  （笔记 32，2026-11-01）：* 强形式「六态上 carousel = J」被**反驳**——J 把正状态送到带符号状态
  （`SR↦-T`）并保持每平面 `W_T,W_S,W_R`，而 carousel 有 5 类与类级 4-环 `LL→RL→RN→LN→LL` 加
  `SR` 条目。carousel 4-环**可**对齐（非规范，3 平面选择 × 2 定向 = 6 候选）到一平面四带符号状态
  上 J 4-环；但 `SR→LL` 条目与指标平移**无 J 对应**（J 保平面）。故 carousel =（J 型旋转）+（平移），
  平移 iota 载体开放（候选：Laplacian `H` 或 `Λ¹↔Λ²` 分次）。*平移结果（笔记 33，2026-11-01）：*
  iota 框架**是**螺旋——`[J,H]=0`、`J²=-I`、`A²=-H²`，且 `exp(tA)=cos(tH)-J sin(tH)`（旋转角 ∝
  H 特征值）。但 `H` **不能**携带平移：切割图是依赖偏序下集 Hasse 图（遗忘左/右），而
  `k = #左叶` 是平面的。`n=4` 验证：四树共享同切割图谱 `(0,.1464,.5,.8536)` 却有 `k = 3,2,1`。这是
  与笔记 29 同平面性阻碍。故平移需**平面、无界**载体（候选：手性 Z/2 × 维 `n`，或带符号 12 态载体
  + 外幂）；无建立。残差：一般 `n` 同谱不同 `k`；fringing `3×` 对 H 谱；平面载体。
  *平面载体构造（笔记 34，2026-11-01）：* 显式**螺旋模** `V = V_class ⊗ V_index`，`V_class =
  ⟨LL,RL,RN,LN⟩`（平面：左/右 × 叶/非叶）与 `V_index = ⟨e_k : k ≥ 1⟩`（无界）。算子
  `J:(c,k)↦(c+1,k)`（iota 复单位，阶 4）、`S:(c,k)↦(c,k+1)`（平移/高度）与 carousel
  `C:(c,k)↦(c+1 mod 4, k+[c=LN])`。验证：`C⁴=S`（carousel 是**螺旋**，平移射影 Z/4 / 四次根）、
  `J⁴=id`、`[J,S]=0`、计数影子 `M²=id`（螺旋对计数不可见）。故平面载体**存在**；iota 供 `J`（旋转
  半），而 `S`（高度）是独立结构**非**由 iota/`H` 供。残差：从 AEG/Adva 导出 `S`；吸收 `SR`/环绕入
  `V`；测试词/历史载体 Z/4；一般 `n` 对齐角级 Thm 4.3。
  *`S` 导出（笔记 35，2026-11-01）：* carousel 指标 `k` 是**遍历位置**（Pushkarev–Byzov Thm 4.2），
  且 AEG 标记历史**年代指标**（`def:marked-spinal-history`、`eq:chronological-history-concatenation`）
  是自然 AEG 原生「无界位置 + 后继」。故 `S` = **年代后继**（追加一语境）。验证：**左梳**——DFS
  「左自然遍历」先访内部脊柱，故与脊柱/年代序一致（精确匹配）；**右梳**——DFS 先访离脊柱*左*叶，
  故差左/右翻转（`research/iota-carousel/verify_traversal.py`）。故 `S` 左梳上精确匹配 carousel
  遍历，右/一般梳树上差平面性翻转，分支层分道（与笔记 29 同缺口）。残差：分支层 `S`；
  `V_class`⊗`V_index` 直积对半直（左/右翻顺序）；一般 `n`；切割基/时钟指标对词指标。
  *分支层 `S` 导出（笔记 36，2026-11-01）：* 笔记 35「左遍历」是**先序**；年代/求值序是**后序**。
  验证：内部节点**左优先后序**是每 PPCT（`n≤5`）依赖偏序**线性扩张**，且对**左与右**梳都等于年代
  序 `[2,1,0]`（`research/iota-carousel/verify_branching_shift.py`）；先序**非**线性扩张。故分支层
  `S` = **「左优先后序线性扩张后继」** = 「沿规范（左优先）脊柱历史前进」
  （`thm:birkhoff-downset-spinal`）。它平面（左优先）、无界、AEG 原生。残差：对齐 carousel *角*序
  与后序*求值*序（Thm 4.2 约定）；左对右优先选择；一般 `n` 证明；与笔记 29 下降阻碍关系（选一规范
  链是「单值下降」）。
  *角序 ↔ 求值序对齐（笔记 37，2026-11-01）：* OCR Pushkarev–Byzov 定义确认「角」此指**顶点**
  （SR/LL/RL/LN/RN 分类顶点）且**左标准遍历是先序**（访顶点，再左子树，再右）。故 carousel 的
  `k` 是**先序（角）位置**，而求值序是**后序**。其对齐（论文自身 Remark + 计算）是：**叶**——先序 =
  后序 = 左到右前沿序；**非叶链**——先序 = 后序⁻¹（反转）；**跨不可比链**——相对序是选择（平衡树
  显示全局反转失败）。故 carousel `k` 的 `S` 应是**先序（角）后继**，笔记 36 `S` = 后序是**求值序**，
  仅叶上等于角序且非叶反转。残差：跨链规范选择；一般 `n`；`S` 到螺旋链；区分笔记 29 多值下降阻碍
  与「角序非线性扩张」缺口（两不同阻碍）。
  *跨链选择规范化（笔记 38，2026-11-01）：* 定义规范线性扩张为**最小化对角序（先序）逆序数
  （Kendall tau）**者。对所有 PPCT `n = 4, 5` 验证：极小者**唯一**且等于**左优先后序**
  （`research/iota-carousel/verify_canonical_choice.py`）。故「选择」解决——`S`（笔记 36）非任意左
  优先选择而是最接近角序的唯一求值序。残差：一般 `n` 证明；其他内在判据（叶序保持）给同极小者；
  `σ`-等变（判据 σ 不变，输出 σ 等变）；与笔记 29 多值下降形式分离。
  *一般 `n` 证明（笔记 39，2026-11-01）：* 树上归纳。对 `t = Node(a,b)`，任何线性扩张是
  `M+[root]` 带 `M` 是 `a,b` 扩张交错；根贡献常量 `m-1` 逆序，跨 `a`/`b` 逆序 `≥0` 且等号**当且
  仅当** `M = E_a + E_b`（块），归纳假设给唯一 `Q(a)`、`Q(b)`。故 `Q(t)` 是每 PPCT **唯一**逆序
  极小者。计算扩到 `n ≤ 7`（193 树）一致。故跨链规范化**证明**，非仅验证。现残差：其他内在判据、
  σ 等变与笔记 29 形式分离。
  *Fringing / 增长对 Hecke 周期轨道（笔记 42，2026-11-01）：* 答案分层。**结构对应成立**：两侧都是
  「自由积作用本原周期轨道编码」——AEG `Γ_4 = C₂*C₄`（`eq:q4-sign-kernel-presentation`）带本原
  双曲类 ↔ 周期轨道（`prop:q4-hyperbolic-class-knot`）与零 dessin 作编码脊柱
  （`thm:q4-zero-dessin-coding-spine`），对 Pushkarev–Byzov `⟨σ,θ⟩ = Z₂*Z₂` 带 `τ`-轨道与角序
  编码。共享：自由积、本原、编码脊柱、周期轨道、**阶 4 旋转**（carousel `J`/`C⁴=S` ↔ Hecke `C₄`
  椭圆旋转）。**增长率对应不成立**：fringing `O(n^{log₂3})` 是*轨道长度*替换增长（验证
  `Δ(Q(T)) = 3Δ(T)` 或 `(3/2)Δ(T)`，`research/iota-carousel/verify_fringing.py`），而 Hecke 侧是
  周期轨道*计数*（指数，熵 1）。不同量、不同率。残差：精确阶 4 同构/嵌入；码翻译（dessin 切割对
  类 4-环）；正确增长率配对（替换 Perron 值）；`Hist_4^{ph}` 对 `τ`-轨道类。
  *精确阶 4 匹配（笔记 47，2026-11-01）：* carousel `J` 不**直接**与 Hecke `C₄` 生成元 `R` 对齐——
  其特征多项式不同（`λ²+1` 对 `λ²-√2λ+1`）。精确对齐是**`J|_plane ~ R²`**：两者都是复结构
  （`(·)² = -I`、特征多项式 `λ²+1`、特征值 `±i`、线性阶 4 / 射影阶 2），且 `R`（带 `R⁴ = -I`，
  `SL₂` 阶 8 / `PGL₂` 阶 4）是 carousel 复结构**平方根**。故 carousel「阶 4 旋转」是 Hecke `C₄`
  生成元**平方**，非生成元本身。验证（`research/iota-carousel/verify_order4.py`）。残差：同构自然性
  （需 `W ≅ ℂ³` 与 `H²` 切平面共同空间）；「三平面对一切平面」多重性；Hecke `χ` 与 carousel `sgn`
  是否同符号特征；carousel 侧什么扮演「`J` 平方根」。
- **098.4 — 右/左双射函子性。** 确定右/左双射是否给从分支层到顺序层函子，尊重 AEG 序缺陷与线性
  扩张结构。当前仅集合双射；无函子性建立。
  *结构阻碍（笔记 44，2026-11-01）：* 保持序缺陷 / 线性扩张结构的函子性需保持**运算偏序**，故至少
  **运算数**。计算：右/左双射映射 `PPCT(n leaves)`（总 `n-1` 二叉内部节点）到 `PPT(n-1 edges)`，
  其内部节点数范围 `{1, …, n-1}`。对 `n = 4` 多重集 `{3,3,3,3,3}` 对 `{1,2,2,2,3}`
  （`research/iota-carousel/verify_functor.py`）。**无双射可保持运算数**，故这些族上无保持运算偏序
  / 线性扩张 / 序缺陷。故答案在运算偏序层**否定**（非「尚未建立」）；`R/L` 双射仍真正*集合*
  （Catalan）双射。残差：(i) 构造 `R/L` 映射本身并检查其特定像与缺陷行为（多重集论证排除任何保持
  运算数双射，含 `R/L`，但映射未在验证器构造）；(ii) 找不同对象（下集格 `O(P)`、历史词 `Hist_4`）
  函子；(iii) 关联「运算数不保持」阻碍与笔记 29/33 同族（见笔记 41 平面性阻碍）。

**开放时默认规则：** 用 Donaghey/De Bruijn–Morselt 仅作 `structural proposal` / `open`；不陈述
函子桥、轨道对应或格等同为已证明。纯 Catalan 双射本身经典且可如此引用。

**受影响文件：**
`notes/analysis-and-calculus/26-donaghey-general-to-binary-tree.md`；
`notes/analysis-and-calculus/27-mirror-reversal-tree-layer.md`；
`notes/analysis-and-calculus/28-ppct-lattice-attribution.md`；
`notes/analysis-and-calculus/29-branching-layer-descent.md`；
`notes/analysis-and-calculus/31-carousel-and-iota.md`；
`notes/analysis-and-calculus/32-carousel-iota-alignment.md`；
`notes/analysis-and-calculus/33-shift-research.md`；
`notes/analysis-and-calculus/34-planar-carrier.md`；
`notes/analysis-and-calculus/35-derive-shift.md`；
`notes/analysis-and-calculus/36-branching-layer-shift.md`；
`notes/analysis-and-calculus/37-corner-order-alignment.md`；
`notes/analysis-and-calculus/38-canonical-cross-chain-choice.md`；
`notes/analysis-and-calculus/39-canonical-choice-general-proof.md`；
`notes/analysis-and-calculus/40-carousel-iota-overview.md`；
`notes/analysis-and-calculus/41-donaghey-iota-grand-overview.md`；
`notes/analysis-and-calculus/42-fringing-hecke.md`；
`notes/analysis-and-calculus/43-theta-tilde-intrinsic.md`；
`notes/analysis-and-calculus/44-functoriality-rl.md`；
`notes/analysis-and-calculus/45-downset-lattice-residual.md`；
`notes/analysis-and-calculus/46-lifting-trace-planar.md`；
`notes/analysis-and-calculus/47-order4-alignment.md`；
`research/donaghey-orbits/`（有限验证）；
`research/ppct-lattice/`（有限验证）；
`paper-0/sections/03-aes-and-motion.tex`（左/右梳约定）；
`paper-1/sections/02-sequential-histories.tex`（镜像 / 反演 / 路径逆，Birkhoff）。
**受影响定理节点：** 无（研究笔记；无 Paper I 定理依赖 Donaghey 对应）。
**拥有者：** 作者。
**决定记录：** 笔记 26（2026-10-31）读三来源并记录紧 `[对应]` 与 `Z₂×Z₂` 对 `Z₂*Z₂` 差异。笔记
27（2026-10-31）于梳层解决 098.1（AEG `m,r` 给 Klein；`θ̃≠r`；无限阶需分支）并转移残差到 `θ̃`
自然性、分支层与 `τ` 在梳上精确阶。笔记 28（2026-10-31）推进 098.2（「分配格」是无穷立方树
Birkhoff 下集格，非 Tamari 格；`O(P)` 是有限偏序上同构造）。笔记 29（2026-10-31）否定解决
098.1(b)（`τ` 不下降到依赖偏序 / `O(P)`；双曲行为严格平面树）。笔记 30（2026-10-31）是 26–29 综合。
笔记 40（2026-11-01）是 31–39 综合（carousel ↔ iota 主线）。笔记 41（2026-11-01）是整条 26–40 大
综合（树层 + carousel–iota；一个对象 `τ`，两正交半，一个平面性阻碍，一个已证明规范化）。后续笔记
关闭剩余 OQ-098 子项：笔记 42（098.3）——与 Hecke 周期轨道结构对应成立，增长率不；笔记 43
（098.1a）——`θ̃ = τ∘m` 是内在路径反射，对合，带 `⟨m,θ̃⟩ ≅ Z₂*Z₂`；笔记 44（098.4）——**否定**：
右/左双射不保持运算数（PPCT 总 `n-1`，PPT 范围 `{1,…,n-1}`），故无函子保持运算偏序 / 序缺陷。
剩余残差：098.2 子格嵌入 / 来源含义；098.1(b) 一般 `n` 与分支层自身动力学；098.3 精确阶 4 同构/
嵌入与正确增长率配对；098.4 `R/L` 像构造与检查，及其他对象（`O(P)`、`Hist_4`）函子。

---

## OQ-099 — 常量边界封顶阻碍范围与缝标签（平凡表示）读法

**优先级：** P2
**状态：** PARTIALLY RESOLVED (2026-11-01)。范围陈述与显式奇异帽在论文中作 Remark 10.13 与
Remark 10.15；缝表示论读法是 `STRUCTURAL PROPOSAL` 且仍开放（099.2）。099.1 对平盘解决，阻碍方向
对任意光滑 `g` 解决。
**起源：** 苑明理问（2026-11-01）封顶阻碍哪个假设尖锐，并分别问阻碍与 QED 侧「缺失缝权重」是否同
缺陷。构造、检查器与文本：DeepSeek Harness 代理（deepseek-v4-flash-vision-exp）。不断言独立人工
数学审查。

**问题（099.1）。** `thm:constant-boundary-capping-obstruction` 哪些假设尖锐，且
`cor:capping-dichotomy` 支 (2) 是否非空？

**当前证据（099.1）。** `research/capping-scope/`（README、`verify_capping.py`、
`evidence-capping.json`）建立：

* `A1`（带所述假设证明）：已发布证明只用 `mu != 0`，经 `|da|_g^2 >= mu^2 > 0`；`lambda` 与 `g`
  都不进入，故按证明阻碍度量与 `lambda` 无关。
* `A2`（证明）：退化情形 `mu = 0 = lambda`（`a ≡ c`）与 `mu = 0, c = 0`（`a ≡ 0`）中光滑帽确
  存在，故结论不扩展到全部 `mu = 0`。
* `A3`（部分证明）：`mu = 0`、`lambda != 0`、`c != 0` 也无光滑帽。`{a != 0}` 上
  `u = log|a|/|lambda|` 满足 `|du|_g = 1`，故其水平集是 `partial D` 等距；常量边界值强制
  `u = k ∓ d_g(., partial D)`，在内部切割轨迹不光滑。笔记用并引用两标准事实，非证明。
* 尖锐陈述（`A4`，组合 A1–A3）：光滑帽存在当且仅当 `mu = 0` 且 `lambda c = 0`。故 `mu != 0` 是
  **充分但非必要**。
* `A5`/`A6`（证明；计算验证示例）：`mu != 0` 带 `a(r) = (mu/lambda) sinh(lambda (r+C))` 在穿孔平
  盘上精确解方程，有 `a(1) = c`，且在单个内部锥点 `C^0` 但非 `C^1`，可规定于 `int D` 任何处。故
  推论支 (2) **非空**，非仅允许。

**问题（099.2）。** 是否有缝表示论读法统一封顶阻碍与 QED 缝权重问题？

**当前证据（099.2），仅 `STRUCTURAL PROPOSAL`。** `public/electrodynamics/pants-v7-translation/`
注「`a|_dD` 常量」是陈述「边界数据位于平凡表示」（圆上 Fourier 分解），故阻碍关乎标签 `j = 0`，
而光子缝带 `j = 1` 两物理横截态。该读法中阻碍与缺失缝权重是「界面只有单个数，故角数据无处安放」
两面。这显式记录为带证伪者的提案，且**非**论文陈述。

**为何重要。** 若 099.2 建立，帽/界面章与「标记界面」扩张会是一个构造而非两个；`dim V_e` 封顶计数
与定理 10.12 会是一标签两层而非竞争论断。

**残差。** 099.1：`A3` 是依赖两引用标准事实的机制；支 (2) 内「内部临界点」替代未构造；示例平度量。
099.2：论文无标记界面定义；无定理；与 `notes/analysis-and-calculus/25-*` 关系未逐陈述检查。

**下一步。** (i) 要么把 `A4` 提升为带 `A3` 完整证明的命题，要么保持 Remark 10.13；(ii) 构造内部临界
点支；(iii) 决定标记界面是否属论文范围。

---

## OQ-100 — 过程几何与算术–过程等价（Paper VI）

**优先级：** 对 Paper VI P1；不阻塞 Papers 0–V。
**状态：** OPEN (2026-11-01)。
**范围：** `governance/00e-paper-VI-process-geometry-scope.md`、`paper-6/`。
**依赖：** `governance/00-authoritative-scope.md`、`governance/01-paper-series-architecture.md`、
`governance/00c-paper-V-triadic-aperture-scope.md`、
`governance/00e-paper-VI-process-geometry-scope.md`、`governance/05-mathematical-status.md`、
`governance/05c-paper-VI-status-register.md`、`notes/analysis-and-calculus/26`–`40`、
`research/iota-carousel/`、`research/donaghey-orbits/`、`research/process-representation-gap/`。

**问题。** Paper VI 开系列过程侧：开放有限程序、作线性扩张的调度、arity-1 载体、规范求值序、
carousel 对应与带算术表达式几何的带型字典。下方项是该计划开放部分；无一 Paper VI 论断，无一阻塞
Papers 0–V 已证明节点。

**100.1 — 一般赋值（`CONJECTURE`）。** 从带角序与依赖序的平面二叉树构造猜想 5.3
（`paper-6/sections/05-equivalence.tex`）自然赋值到带平面调度结构的开放有限程序，并证明它保持规范
序；或用调度结构无过程像的树反驳。顺序片段证明（手稿定理 5.2）；一般情形开放。

**100.2 — 导出平移（`OPEN`）。** 指标平移 `S` 在平面螺旋模（`V_class ⊗ V_index`、`C^4 = S`）中
假定。切割 Laplacian 候选由 `paper-6/sections/04-carousel.tex` 有限阻碍排除；从 AEG 或过程数据导出
`S` 的平面数据未找到。

**100.3 — 吸收基角（`OPEN`）。** 扩展平面模使基角 `SR` 被表示而非加为条目，并检查 `C^4 = S` 是否
存活。

**100.4 — 判据规范性（`OPEN`）。** 定理 3.6 证明左优先后序唯一最小化对角序逆序。决定另一自然判据
（叶序、镜像不变）是否选同唯一扩张；一致加强规范性，不一致强制声明判据。

**100.5 — 平面与偏序层（`OPEN`）。** 规范序是平面层陈述；`OQ-098` 变换 `τ` 不下降到下集格
`O(P)`。两陈述必须显式关联非混淆：第一选一个线性扩张，第二记录偏序层阻碍。

**100.6 — Fringing 与轨道增长（`OPEN`）。** 决定 carousel 效应、fringing 律 `Δ(Q(T)) = 3Δ(T)` 与
轨道增长 `O(n^{log₂ 3})` 是否对应算术周期轨道（`OQ-098.3`）。这需算术轨道结构且不被载体对应解决。

**100.7 — 程序侧装置（`OPEN`）。** 把 `paper-6/sections/05-equivalence.tex` 三验收测试存为过程侧
执行装置：树普查、调度计数、载体检查。一般赋值仍猜想；定理 5.2 保留其已证明抽象顺序范围。

**执行部分结果（2026-11-01；非闭包）。** `research/program-side-fixtures/` 在
`mountain/adva@87a1a6933bca3fdb5c176cbf612729e278d172f7` 测试一个自由三语境脊柱。两声明乘负一语境
用原生 `neg`，而检查调用与嫁接保留其槽 `(1,2,1)`。树与三事件程序都有一个调度、规范年代序与逆序数
3。全部 6 置换原生检查。字面常量/二元 `mul` 编码有 6 事件、15 调度（全部 720 置换测试）与最小逆序
数 9。其到算术词的 15 到 1 投影保留为残差，非静默作双射。这只拒绝该字面编码。九原生/研究层控制
与六编辑保存候选控制拒绝错误槽、非法序、缺失事件与替换身份。Rust 接收与分离 Python oracle 重放冻结
证据。

193 树目录含 60 单脊柱与 133 分支形；这是范围分类，非 193 原生装置。适配器拒绝分支且尚未在其他
顺序形运行。扩张需显式标记、事件粒度契约、分支赋值与替换相容。一般 Schedule 计数需事件/序同构或
带自身理由的显式替代调度定义。载体检查仍需程序导出三平面载体、所选带符号对齐、`J` 与置换作用，含
转置反演。它未运行。见研究 README 源引脚、精确拒绝层与残差。

**100.8 — 呈现与对象化（`OPEN`）。** 把过程语料呈现与对象化层带入 Paper VI 范围，或显式陈述其外。
当前草稿只导入原生过程、三读法与切片律。

**开放时默认规则。** 引用 Paper VI 已证明陈述仅在其登记强度；不用等价作 Papers 0–V 依赖；不把有限
校准提升为定理。

## OQ-101 — 穿孔 AES 上流与约化为 ODE

**优先级：** P3
**状态：** OPEN (2026-11-11；对齐笔记 53 v0.2)。
**范围：** `paper-0/sections/11-holed-aes.tex`（`subsec:p0-punctured-flow-proposal`）、
`governance/05b-paper-0-status-register.md`。
**依赖：** `governance/00b-paper-0-geometric-foundation-amendment.md`、
`governance/05b-paper-0-status-register.md`、
`notes/analysis-and-calculus/53-punctured-aes-flows-and-reduction.md`。

**问题。** Paper 0 §11 带所述假设证明动力学载体上声明严格或相对返回到基础 ODE 周期轨道下降
（`prop:p0-reduction-descent`/`-reverse`/`-section`/`-transport`），并作结构提案记录该约化在实际穿孔
AES 上实现。解决与开放部分随笔记 53 v0.2 §9。

**已解决（带所述假设证明）。** R-A 下降；R-B 等变下反向相对提升与漂移迭代；R-C 截面根推论；平面
首次返回局部隔离对应；van der Pol 提升严格负漂移（条件于周期轨道）；R-D 到基本模型传输；Krawczyk
根存在充分条件（笔记 53 §6.3）。

**101.1 — 端数据与端管（`OPEN`）。** 正则与端层区间邻域语义，与端管有效表示。

**101.2 — 极小端数据（`OPEN`）。** 具体 AES 端模型极小动力学数据与其扩张唯一性；拓扑或共形完备化
不供。

**101.3 — 实现载体假设（`OPEN`）。** 所选穿孔载体是否满足全轨道合法性、主丛或纤维作用与约化命题
时间相容假设。

**101.4 — Hamilton–Lagrange 退化（`OPEN`）。** 真正 Hamiltonian/Lagrangian 表示与其 Legendre 变换
退化；非仅水平性蕴含。

**101.5 — 锐化约化假设（`PARTIALLY RESOLVED`）。** 光滑/正时钟/合法域约化定理证明；非自由作用、
奇异商、非唯一端扩张、重置与更弱正则在其外，且假设不声称极小。

**101.6 — 覆盖与联络语义（`OPEN`）。** 并覆盖/局部系数与联络 holonomy 严格区间语义；一般弯曲联络
闭环漂移依赖路径且不产仅 `π₁` 表示。

**101.7 — AES 原生实现（`PARTIALLY RESOLVED`）。** van der Pol 提升与基本模型传输显式；任意穿孔
AES 全局实现、算术运动有限原时等价与 AES 原生区间认证未完成。

**开放时默认规则。** 引用约化定理仅在 `PROVED WITH STATED HYPOTHESES` 且应用仅在 `STRUCTURAL
PROPOSAL`；不断言规范穿孔单值，不把含零区间读为根证明，不断言底空间周期严格提升。

## OQ-102 — Scott/Lawson 词汇与 Adva 区间边界

**优先级：** P3
**状态：** OPEN (2026-11-11；对齐笔记 52 v0.2)。
**范围：** `notes/analysis-and-calculus/52-scott-lawson-adva-interval-boundary.md`、
`notes/analysis-and-calculus/09-order-topology-scott-lawson.md`、
`notes/aes/03-quadrilateral-neighborhoods-and-scott-continuity.md`、
`notes/aes/05-measure-probability-information-and-area.md`。
**依赖：** `governance/scott-lawson-paper-1-integration-2026-10-31.md`、
`governance/notes-reserve-audit.md`。

**问题。** 笔记 52 v0.2 分离三层——有限有理表示、实区间完备化（连续 dcpo）与有效名称——并分离
区间 Newton `RootExists` 与 `ExactZero`。它是边界/纪律文档：登记于此，不提升进 Paper 0/1/2 正文。
有理有限区间**非** dcpo；只有实端点区间形成连续 dcpo。回答与开放部分随笔记 52 §10。

**已回答（`CLASSICAL`）。** Q1（实区间域及其 dcpo/基，§1）、Q3（精确有限项 `+,-,*,/` Scott 连续对
固定网格舍入不连续，§4–§5）、Q4（纯区间谓词；严格正/负与零排除 Scott 开，精确零非，§2/§6）、Q6
（极大元相对 Scott 拓扑恢复点拓扑；`E` 极大元恢复 Lawson 拓扑）。

**102.1 — 生成元级函子（`PARTIAL REFORMULATION`，余 `OPEN`）。** 固定平移、正缩放与零排除倒数在
§3 匹配；函子结论需两范畴、态射与关系保持陈述，非仅端点公式。

**102.2 — 项级同态与共享语义（`OPEN`）。** 所有实函数恒等商上自然区间同态被反例反驳；哪些守卫重写、
关系域或共享语义改进精度开放。

**102.3 — 精确零与契约设计（`OPEN`）。** 分别指定 C11 需恒等、存在与误差界；精确零论断需检查恒等、
单例包围或离散间隙见证。

**102.4 — Newton/证书实现（`OPEN`；实现验收）。** 重放 Newton 所用 `F(c)`、全盒 Jacobian 与管源；
证书模式中分离零状态、根状态、源有效性与目标命题。

**102.5 — 结构质量与尺度（`OPEN`）。** 定义结构质量、其精化与传输、有效性与几何实现（链到 AES 笔记
04）；AES 笔记 05 特定 Haar 质量与固定叶赋值有证明，但其一般结构推广开放。

**开放时默认规则。** 不把有理有限表示与实区间 dcpo 等同；不把固定网格舍入当 Scott 连续；不把
`ZeroUndetermined` 提升为 `ExactZero`；无健全重放 `F(c)`/`J(X)` 把 `contracted=true` 当无效见证。

## OQ-103 — HTWR 框架与 fanout 成本 / 包裹桥（Level C）

**优先级：** P3
**状态：** OPEN (2026-11-14)。
**范围：** `notes/general/001-htwr-core.md`、`002-htwr-example.md`、`004-test-sequences.md`、
`005-fanout-wrapping.md` 及其见证 `005-fanout-wrapping-witness.py`；交叉读 `aeglib/docs/17`、
`aeglib/docs/18`、`aeglib/docs/19`（VdP C11 包裹/审计）。
**依赖：** `governance/notes-reserve-audit.md` §2.9；`governance/05-mathematical-status.md`（状态
词汇）。

**问题。** HTWR（双曲热带波前残差）核心是 `STRUCTURAL PROPOSAL` 框架：`P¹(Q)` 上算术求值的资源/
复杂度读法，由对数 Weil 高度校准，带 fanout `Δ` 与 erasure `ε` 作成本生成元。其定理 1–2（时空不确定
下界与 Pell/Fibonacci 收敛子两相 Pareto 边界）仅**条件于**公理 I–IV 证明。Level-C 见证（`005`）
显示 naive 对 Heron fanout 差——两对一 `Δ`——在精确有理区间算术中复现为单调包裹宽差
（`W_true < W_heron < W_naive`，`x=17/12` 处精确首阶过量比 `577/288`）。这登记框架与其桥；不提升。

**103.1 — 框架登记（`STRUCTURAL PROPOSAL`）。** 公理 I–IV 与条件定理 1–2 是公理提案，非已发布
定理。不得引用为 Papers 0–IV 结果。

**103.2 — 区间宽 ↔ 信息高（`OPEN`；Level-C 核心）。** HTWR 的 `I(u) = ln max(|p|,|q|)` 是有理
*大小*（Weil 高度），而包裹过量是实*区间宽*。`I(u)` 能否替换为精度对数 `log(1/width)` 使
`c_Δ = α·I(u)` 成为精确首阶包裹系数——把「fanout 单调」升级为定量律——开放。`005` 显示过量单调但
**非** fanout 计数简单倍数（`577/288 ≠ 2`），故对应不自动。

**103.3 — 包裹下界（`STRUCTURAL PROPOSAL` / `OPEN`）。** 把定理 1 翻译为精度 `ε` 下验证 ODE 管宽
或工作下界是结构提案。证明需当前缺失的纤维式包围论证；按 AGENTS.md，计算下界不得仅从几何增长推断。

**103.4 — 分管形式化（`ADVANCED`，2026-11-14）。** 于 `notes/general/006-split-tube-htwr.md` 带
见证 `006-split-tube-witness.py` 形式化。VdP 增广 RHS 块三角：相位/作用分量 `(x,y,A_hor,I)` **不**读
变分 `φ`，故 `F₁(x,y)` 独立于 `F₂(x,y,φ)`。故分管相位半径 `r_phase ≤ r_unsplit`（严格当且仅当一变分
RHS 分量主导）。HTWR 读法——相位/作用作「主线」、`φ` 作「fanout 辅助线」（`(x,y)` 到 `J(x,y)` 的
`Δ` fanout）——是 `STRUCTURAL PROPOSAL`。诚实发现（`COMPUTATIONALLY VERIFIED EXAMPLE`）：收敛 C11
周期轨道上变分 RHS **不**持续主导，故逐项包裹约化弱（`r_phase/r_unsplit ∈ {0.91, 1.0}`）；其决定性
价值在打靶期间（`docs/17` §11，`φ21'≈29.5`）。不提升为定理。

**为何重要。** VdP C11 认证被依赖爆炸（包裹）阻塞；该爆炸资源论读法会把数值麻烦转为有界成本，并把
AEG 资源/复杂度层（Paper IV 展望）连到 hilbert-16 垂直切片。

**当前证据。** `005` 精确有理见证；笔记 001/002/004 恒等验证；`aeglib/docs/18/19` 两确认算术 bug 与
分管观测。全有限/条件；无一一般定理。

**开放时默认规则。** 把 HTWR 公理 I–IV 与定理 1–2 当 `STRUCTURAL PROPOSAL`；不声称定量 fanout→包裹
律；不从不确定原理推断包裹或复杂度下界；不把分管启发式提升为认证约化。

**解决条件。** 103.1 框架被分配论文或显式归档时解决；103.2 带证明对应（或反例）解决；103.3 带纤维
式包围证明解决；103.4 带重放逐项分管包围解决。

**受影响文件。** `notes/general/001–005`；`governance/notes-reserve-audit.md` §2.9；本条。

**拥有者。** 苑明理（研究方向）；状态与见证：DeepSeekHarness。

**决定记录。** 尚无。

## OQ-104 — Pan / Encke 缝边缘波：密度波色散与振幅

**优先级：** P3
**状态：** OPEN (2026-11-14)。
**范围：** `notes/general/007-pan-encke-farey.md`；见证
`aeglib/python/examples/pan_encke_resonance_ladder.py`、
`aeglib/python/examples/pan_encke_gap_criterion.py`。

**问题。** 笔记 007 固定 Pan/Encke 缝边缘波*骨架*：Lindblad 共振阶梯 `x=m/(m±1)`（共转 Farey 邻）、
共振半径（`m=551` 于 Encke 外缘）与缝开 Chirikov 共振重叠读法（Hill 半径 19 km、重叠 `m≈475`、缝
`≈8.5 R_H`）。它**未**计算观测边缘波波长/振幅（数十 km，即方位 `m~10⁴`），因那需带自引力线性密度波
色散关系 `(ω − mΩ)² = κ² − 2πGΣ|k| + c²k²`，加缝边边界/模结构。这登记开放物理。

**104.1 — 色散与波长（`ADVANCED`，2026-11-14）。** 于 `notes/general/008-encke-density-wave.md` 带
见证 `008-encke-density-wave-witness.py` 解决。紧绕色散 `(ω−mΩ)² = κ² − 2πGΣ|k| + c²k²` 是径向波数
`k` 闭式二次；径向波长 `λ₀ = c²/(GΣ) ≈ 0.75 km` 于共振（`Σ=500 kg/m²`、`c=0.5 cm/s`）且**离开共振
减小**（包裹螺旋）。这匹配观测「波长平滑变化」签名（Tiscareno et al., DPS 2005）。测量（PIA08257，
笔记 008 §4.6，见证 `008-encke-edge-wave-image.py`）：边缘波方位波长 `λ_θ ≈ 260–320 km`、径向振幅
`A ≈ 0.65 km`，故 `m = 2πr/λ_θ ≈ 2600–3200`——清空缝**内**共振（`a_P + 28 km`），非 `m≈551` 边缘
共振（`a_P + 162 km`）。这确认观测边缘波是捕获**边缘模**（Papaloizou–Lin），非自由 `m=551` 密度波；
较早 `~50–100 km` 估计被取代。残差（`D4`）：边缘模色散定量解（现登记为 OQ-104.3）。

**104.2 — aeglib 能力缺口（`OPEN`）。** 色散关系是多变量根/参数连续问题；aeglib 0.0.2 有单变量
Sturm + Arb 包围但无色散求解器。推进 104.1 需 `ArbBall` 上多变量 Newton/Krawczyk + 参数连续
（aeg-certify 有 `krawczyk.rs`，尚未暴露 Python）。注（2026-11-14）：紧绕色散是 `k` 闭式二次，故
104.1 **不**需此；多变量求解器只为完整 `(m,k)` 联合 + 边界条件问题。

**104.3 — 边缘模（Papaloizou–Lin）色散（`RESOLVED`，2026-11-14）。** (i) 冷 WKB
（`σ² = κ² − 2πGΣ|k|`，`notes/general/009-encke-edge-mode-wkb.md`）：转向点
`r_L = a_P((m+1)/m)^{2/3}` 仅对 `m < 551` 在边缘外；对 `m ≥ 551`（测量 `m ≈ 2800`）共振在清空缝内
（evanescent 衰减 `≈ 0.5 m`）。(ii) 压力（`c > 0`，Q ≈ 6）：模存在条件几何（`m < 548`），独立于压力；
`m = 2800` 处压力只给短波 `≈ 47 m`。(iii) **最终解决**
（`notes/general/010-encke-scalloped-edge-tidal.md`，见证 `010-encke-scalloped-edge-tidal.py`）：观测
边缘波是线性区 `d ≈ 8.5 R_H` 中 Pan **静态潮汐畸变**（受迫本轮）；受迫偏心率
`e_f = (M_P/M_S)(a_P/d)² ≈ 5.9e-6`、径向振幅 `GM_P/(κ²d²) ≈ 0.785 km`（观测 0.65 km）、方位 FWHM
≈ 249 km（观测 ~300 km）。**核心（振幅 + 尺度）现匹配。** 残差（次级）：「变化平滑」/增-减/无阻尼
签名需完整动力学（碰撞阻尼 + 多 m 叠加），非静态力平衡。

**为何重要。** 它关闭共振骨架（Farey/Ford、共振重叠）与实际观测波间缺口，把 AEG 读法从结构类比转为
预测计算。

**当前证据。** 笔记 007 认证共振阶梯与重叠数；笔记 008 自由色散 `λ(Δr)` 与径向/方位比较。尚无边缘
模色散计算；精确观测波长（径向对方位，值）仍需从主要文献取回（Cuzzi & Scargle 1985；Porco et al.
2005；Tiscareno et al. 2007）。

**开放时默认规则。** 不声称波长/振幅结果；不把 m=551 共振与观测边缘波等同；保持 Farey/Ford 读法为
`STRUCTURAL PROPOSAL`。

**解决条件。** 104.1 带色散导出波长达量级匹配观测值解决；104.3 带量子化边缘模频率/径向范围匹配
观测受限边缘波解决。

**受影响文件。** `notes/general/007-pan-encke-farey.md`、`notes/general/008-encke-density-wave.md`；
本条。

**拥有者。** 苑明理（研究方向）；DeepSeekHarness（见证）。

**决定记录。** 尚无。
