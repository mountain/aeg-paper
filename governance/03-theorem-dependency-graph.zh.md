# Paper I 核心定理依赖图与跨论文扩展节点

**文件：** `governance/03-theorem-dependency-graph.md`
**状态：** 权威
**版本：** 1.1
**日期：** 2026-08-06
**依赖：**

* `AGENTS.md`
* `governance/00-authoritative-scope.md`
* `governance/01-paper-series-architecture.md`
* `governance/02-paper-I-outline.md`

**适用于：** **Arithmetic Expression Geometry I: Foundations** 的定理核心，连同第二十部分
显式分离的 Paper II–III 扩展节点。

---

## 1. 目的

本文档定义 Paper I 所需定义、引理、命题与定理的逻辑依赖图，并在不改 Paper I 证明顺序下记录
下游扩展节点。

其目的是：

* 防止结果在其假设与定义建立前被使用；
* 区分严格证明依赖与叙事或动机依赖；
* 暴露缺失引理与约定选择；
* 防止循环依赖；
* 识别 Paper I 所需关键路径；
* 识别可移除而不破坏基础论证的可选结果；
* 为 Codex 与人类编辑提供机器可读实现顺序。

本文档不赋每个结果最终证明状态。当前证明状态必须记录于：

```text
governance/05-mathematical-status.md
```

---

# 第一部分. 依赖约定

## 2. 边类型

图用四种边类型。

### 2.1 严格证明依赖

记号：

```text
A ==> B
```

含义：

* 结果 (B) 用 (A) 的陈述、定义或证明；
* (A) 可用前 (B) 不得被证明或形式陈述；
* 改变 (A) 需重查 (B)。

---

### 2.2 定义依赖

记号：

```text
A --> B
```

含义：

* 对象 (B) 用对象 (A) 定义；
* (B) 定稿前 (A) 定义必须稳定。

定义依赖通常也是严格序约束。

---

### 2.3 叙事依赖

记号：

```text
A -.-> B
```

含义：

* (A) 解释 (B) 的概念定位或动机；
* (B) 的证明可不逻辑要求 (A)；
* 论文通常应为连贯先呈现 (A)。

---

### 2.4 可选或条件依赖

记号：

```text
A ~~~> B
```

含义：

* (B) 可选、条件或依赖附加验证；
* 移除 (B) 不破坏 Paper I 关键路径。

---

## 3. 节点类

每个图节点有以下之一类：

* `CONV`：约定；
* `DEF`：定义；
* `LEM`：引理；
* `PROP`：命题；
* `THM`：定理；
* `COR`：推论；
* `EX`：示例；
* `REM`：结构注；
* `OPEN`：开放问题或推迟义务。

只有 `DEF`、`LEM`、`PROP`、`THM` 与 `COR` 可出现在严格定理依赖路径。

示例与注不得作证明替代。

---

## 4. 关键路径记号

标记：

```text
[CRITICAL]
```

的节点是 Paper I 基础论证所需。

标记：

```text
[SUPPORTING]
```

的节点加强或澄清论文但中心定理链不需。

标记：

```text
[OPTIONAL]
```

的节点若不完整、太长或超出长度预算可省略。

---

# 第二部分. 约定节点

## 5. C0 — 年代复合与作用约定

**类：** `CONV`
**优先级：** `[CRITICAL]`

### 所需内容

固定相应矩阵积约定。

固定拼接记号：

[
\gamma\delta.
]

论文必须陈述这意味：

* 先应用 (\gamma) 再 (\delta)，或
* 先应用 (\delta) 再 (\gamma)。

每个余循环与相对缺陷公式依赖此选择。

### 下游依赖

```text
C0 --> S3
C0 --> P2
C0 --> A1
C0 --> G1
C0 --> K3
```

### 失败条件

若 C0 仍含糊，以下不可视为已验证：

* 仿射余循环公式；
* 矩阵分解；
* Baumslag–Solitar 关系；
* ACS 路径定向；
* 有限接触交换子。

---

## 6. C1 — 代数域与可允许性约定

**类：** `CONV`
**优先级：** `[CRITICAL]`

### 所需内容

区分：

* 一般域 (K)；
* 普通算术求值；
* 非退化射影求值；
* 除域排除；
* 常量与非可逆语境；
* 作射影延拓的 (\mathbb P^1(K))。

### 下游依赖

```text
C1 --> S1
C1 --> P1
C1 --> T2
```

---

## 7. C2 — 微分几何假设

**类：** `CONV`
**优先级：** `[CRITICAL]`

### 所需内容

指定何时：

* (\mu,\lambda) 是实常量；
* (\mu\neq0)；
* (\lambda\neq0)；
* (\mu,\lambda>0)；
* 度量光滑非退化；
* 赋值光滑；
* 流形有边；
* 完备性假设与否。

### 下游依赖

```text
C2 --> F3
C2 --> E1
C2 --> T6
C2 --> T7
C2 --> Z3
C2 --> T13
```

---

# 第三部分. 顺序语法支

## 8. S1 — 算术表达式树

**类：** `DEF`
**优先级：** `[CRITICAL]`

定义二叉算术表达式树带：

* 原子叶；
* 内部运算标签；
* 可允许普通求值。

### 依赖

```text
C1
```

### 导出

* 树 (T)；
* 内部节点集 (I(T))；
* 递归求值关系。

---

## 9. S2 — 依赖偏序

**类：** `DEF`
**优先级：** `[CRITICAL]`

定义内部节点偏序：

[
u\preceq v
]

当求值 (v) 需 (u) 的输出。

### 依赖

```text
S1
```

### 导出

* 内部依赖偏序；
* 作线性扩张的合法求值顺序。

---

## 10. T1 — 顺序树分类

**类：** `THM`
**优先级：** `[CRITICAL]`
**目标标签：** `thm:sequential-tree-classification`

### 陈述

对有限二叉表达式树 (T)，以下等价：

1. 其内部依赖偏序有唯一线性扩张；
2. 内部依赖偏序是链；
3. 每个内部顶点至多一个内部子；
4. 内部顶点形成单个脊柱。

### 严格依赖

```text
S1
S2
```

### 证明义务

* 证明唯一线性扩张有限偏序是链；
* 证明一个顶点两个内部子不可比；
* 证明一内部子性质产唯一脊柱；
* 单独处理仅叶树。

### 导出

* 顺序树内在定义；
* 含糊历史「threadlike」定义的替换。

---

## 11. S3 — 标记脊柱历史

**类：** `DEF`
**优先级：** `[CRITICAL]`
**目标标签：** `def:marked-spinal-history`

### 定义

标记脊柱历史是：

[
\gamma
======

\bigl(
x_0;
(\omega_i,c_i,\varepsilon_i)_{i=1}^{n}
\bigr),
\qquad
\varepsilon_i\in{1,2},
]

带：

[
C_{\omega,c}^{(1)}[z]=\omega(z,c),
\qquad
C_{\omega,c}^{(2)}[z]=\omega(c,z).
]

### 严格依赖

```text
C0
T1
```

### 证明或构造义务

证明带标记种子的顺序树决定唯一标记脊柱历史。

若声称双射，证明逆构造。

### 导出

* 自由与有界历史；
* 手性词；
* 年代语境词。

---

## 12. S4 — 镜像、反演与逆

**类：** `DEF`
**优先级：** `[CRITICAL]`

### 定义

分别定义：

* 镜像 (m\gamma)；
* 时间反演 (r\gamma)；
* 路径逆 (\gamma^{-1})。

### 严格依赖

```text
C0
S3
```

### 证明义务

证明这些运算不同，含 (m\gamma\neq r\gamma) 示例。

---

## 13. S5 — 相等层级

**类：** `DEF`
**优先级：** `[SUPPORTING]`

定义并区分：

1. 字面相等；
2. 标记历史相等；
3. 算子相等；
4. charge 相等；
5. 端点相等；
6. 商或关系相等。

### 依赖

```text
S3
P2
G1
```

---

# 第四部分. 射影语义支

## 14. P1 — 单孔语境射影语义

**类：** `DEF`
**优先级：** `[CRITICAL]`

定义非退化单孔语境在 (\mathbb P^1(K)) 上的分式线性作用。

### 依赖

```text
C1
S3
```

---

## 15. P2 — 射影求值映射

**类：** `DEF`
**优先级：** `[CRITICAL]`

定义：

[
\rho:
\operatorname{Hist}^{\pm,\times}_K
\longrightarrow
PGL_2(K).
]

### 严格依赖

```text
C0
P1
S3
```

### 义务

陈述年代矩阵复合约定。

---

## 16. T2 — 双边生成定理

**类：** `THM`
**优先级：** `[CRITICAL]`
**目标标签：** `thm:bilateral-pgl2-generation`

### 陈述

平移、非零缩放与反演生成 (PGL_2(K))。

### 严格依赖

```text
C1
P1
P2
```

### 证明义务

* 显式分解 (C\neq0) 情形；
* 处理 (C=0)；
* 检查特征二，若声称全部 (K)。

---

## 17. P3 — 仿射/Borel 推论

**类：** `COR`
**优先级：** `[CRITICAL]`

证明：

[
B_\infty
========

\operatorname{Stab}_{PGL_2(K)}(\infty)
\cong
\operatorname{Aff}(1,K).
]

### 严格依赖

```text
P1
T2
```

---

## 18. P4 — 正实仿射扇区

**类：** `PROP`
**优先级：** `[CRITICAL]`

陈述当前连续理论对应 (\operatorname{Aff}^{+}(1,\mathbb R)) 而非全部
(\operatorname{Aff}(1,\mathbb R))。

### 严格依赖

```text
C2
P3
```

---

## 19. P5 — Riccati 完备化

**类：** `REM`
**优先级：** `[SUPPORTING]`

注 (z^2\partial_z) 完成仿射 Lie 代数到射影 Lie 代数，给：

[
\dot z
======

\beta+\alpha z+\kappa z^2.
]

### 依赖

```text
T2
P3
F1
```

---

# 第五部分. 仿射余循环支

## 20. A1 — 仿射复合律

**类：** `PROP`
**优先级：** `[CRITICAL]`

证明：

[
\Phi_{\gamma\delta}
===================

\Phi_\delta\Phi_\gamma.
]

### 严格依赖

```text
C0
P3
```

---

## 21. T3 — 目标框架仿射余循环

**类：** `PROP`
**优先级：** `[CRITICAL]`

证明：

[
\Phi_n
======

\prod_{i=1}^n s_i,
\qquad
\xi_n
=====

\sum_{i=1}^n
t_i\prod_{j=i+1}^n s_j.
]

### 严格依赖

```text
A1
C0
```

---

## 22. T4 — 源归一化仿射余循环

**类：** `PROP`
**优先级：** `[CRITICAL]`

证明：

[
\widehat\xi_n
=============

\Phi_n^{-1}\xi_n
================

\sum_{i=1}^n
\frac{t_i}{\prod_{j=1}^i s_j}.
]

### 严格依赖

```text
T3
```

---

## 23. A2 — 左右仿射微分

**类：** `PROP`
**优先级：** `[SUPPORTING]`

计算 (g^{-1}dg) 与 (dg,g^{-1}) 平移分量。

### 依赖

```text
C0
T3
T4
```

---

## 24. A3 — 相对仿射缺陷

**类：** `PROP`
**优先级：** `[CRITICAL]`

定义并证明等尺度历史端点差独立于 (x)。

### 严格依赖

```text
P3
T3
```

---

## 25. A4 — 初等算术 torsion

**类：** `PROP`
**优先级：** `[CRITICAL]`

证明：

[
(x+\mu)e^\lambda
----------------

# (xe^\lambda+\mu)

\mu(e^\lambda-1).
]

### 严格依赖

```text
A3
T3
```

---

# 第六部分. 连续流支

## 26. F1 — 仿射 Lie 代数生成元

**类：** `DEF`
**优先级：** `[CRITICAL]`

定义 (E=\partial_a)、(H=a\partial_a)，计算 ([E,H]=E)。

### 严格依赖

```text
C2
P4
```

---

## 27. T5 — 连续仿射流

**类：** `THM`
**优先级：** `[CRITICAL]`
**目标标签：** `thm:continuous-affine-flow`

证明：

[
\frac{da}{ds}
=============

\mu\cos\theta+\lambda a\sin\theta.
]

### 严格依赖

```text
C2
F1
```

---

## 28. F2 — Pfaffian 传播律

**类：** `PROP`
**优先级：** `[CRITICAL]`

推导：

[
da=\mu,du+\lambda a,dv.
]

### 严格依赖

```text
T5
```

---

## 29. F3 — 度量相容 eikonal 方程

**类：** `PROP`
**优先级：** `[CRITICAL]`

指定度量后证明：

[
|\nabla a|_g^2
==============

\mu^2+\lambda^2a^2.
]

### 严格依赖

```text
C2
E1
T5
```

---

## 30. F4 — 矫正坐标

**类：** `PROP`
**优先级：** `[OPTIONAL]`

定义 (r(a)) 并证明 (|\nabla r|=|\lambda|)。

### 依赖

```text
F3
```

---

## 31. F5 — 无穷小 torsion 密度

**类：** `PROP`
**优先级：** `[OPTIONAL]`

证明渐近：

[
d\tau
=====

\mu\lambda,du,dv
+
O(|(du,dv)|^3).
]

### 依赖

```text
A4
T5
```

---

# 第七部分. 模型支

## 32. E1 — 正则算术表达式空间

**类：** `DEF`
**优先级：** `[CRITICAL]`
**目标标签：** `def:regular-aes`

定义 (\mathfrak E=(M,g,a;\mu,\lambda)) 带定义方程成立声明域。

### 严格依赖

```text
C2
T5
```

---

## 33. E2 — 不变仿射度量

**类：** `PROP`
**优先级：** `[CRITICAL]`

推导归一化不变度量。

### 严格依赖

```text
C2
P4
```

---

## 34. T6 — 基本双曲 AES

**类：** `THM`
**优先级：** `[CRITICAL]`
**目标标签：** `thm:basic-hyperbolic-aes`

### 陈述

在上半平面：

[
\mathcal H={(x,y):y>0},
]

带：

[
g_{\mu,\lambda}
===============

\frac1{y^2}
\left(
\frac{dx^2}{\mu^2}
+
\frac{dy^2}{\lambda^2}
\right),
\qquad
a(x,y)=-\frac{x}{y},
]

有：

[
|\nabla a|*{g*{\mu,\lambda}}^2
==============================

\mu^2+\lambda^2a^2.
]

### 严格依赖

```text
E1
E2
F3
```

### 证明义务

* 计算逆度量；
* 计算 (a_x,a_y)；
* 精确验证方程；
* 陈述参数假设。

### 导出

定义：

[
\mathfrak E_0(\mu,\lambda).
]

---

## 35. E3 — 曲率计算

**类：** `PROP`
**优先级：** `[SUPPORTING]`

### 陈述

计算归一化度量 Gauss 曲率。

所述归一化下预期结果：

[
K=-\lambda^2.
]

### 依赖

```text
T6
```

### 验证义务

仔细检查坐标重标。

---

## 36. E4 — 算术网格作用

**类：** `PROP`
**优先级：** `[SUPPORTING]`

定义实现：

[
a\mapsto a+s,
\qquad
a\mapsto ka.
]

的变换。

### 依赖

```text
T6
C0
```

### 证明义务

* 验证赋值变换；
* 陈述每映射是否等距；
* 固定作用顺序。

---

## 37. E5 — Baumslag–Solitar 关系

**类：** `PROP`
**优先级：** `[OPTIONAL]`

### 陈述

验证所选关系，例如：

[
Y_k^{-1}X_s^{,k}Y_k=X_s,
]

于采纳变换约定下。

### 依赖

```text
E4
C0
```

### 警告

作用顺序约定未完全检查时此命题必须省略。

Paper I 中无复杂度结论随之。

---

## 38. E6 — Laplace 特征函数

**类：** `PROP`
**优先级：** `[SUPPORTING]`

### 陈述

计算：

[
\Delta_g a
==========

c_\lambda a
]

带由度量与 Laplacian 符号约定决定的精确特征值。

### 依赖

```text
T6
C2
```

### 证明义务

* 定义 (\Delta_g)；
* 用实际各向异性归一化度量计算；
* 不无重标复用归一化 (\mu=\lambda=1) 结果。

---

# 第八部分. 零几何支

## 39. Z1 — 零集定义

**类：** `DEF`
**优先级：** `[CRITICAL]`

定义：

[
Z(a)=a^{-1}(0).
]

### 依赖

```text
E1
```

---

## 40. T7 — 正则零轨迹定理

**类：** `THM`
**优先级：** `[CRITICAL]`
**目标标签：** `thm:regular-zero-locus`

### 陈述

若：

[
|\nabla a|^2
============

\mu^2+\lambda^2a^2
]

且：

[
\mu\neq0,
]

则在 (Z(a)) 上：

[
|\nabla a|=|\mu|>0.
]

因此 (0) 是正则值且：

[
Z(a)
]

是光滑余一维子流形。

### 严格依赖

```text
F3
Z1
C2
```

### 证明义务

* 调用正则值定理；
* 陈述流形与边界假设；
* 区分内部零点与可能边界行为。

---

## 41. Z2 — 零集刚性推论

**类：** `COR`
**优先级：** `[CRITICAL]`

对二维正则 AES，结论正则零集是不相交光滑一维流形并。

服从精确假设，记录：

* 无孤立正则零；
* 无正则交叉；
* 无正则分支点；
* 无正则内部端点。

### 严格依赖

```text
T7
```

---

## 42. Z3 — 奇异算术表达式空间

**类：** `DEF`
**优先级：** `[CRITICAL]`

定义 (\mathcal M,S,g,a;\mu,\lambda)，正则方程在 (\mathcal M\setminus S) 成立。

### 严格依赖

```text
C2
E1
```

---

## 43. Z4 — 孤立零模型

**类：** `EX`
**优先级：** `[OPTIONAL]`

重新分类孤立中心模型。

### 依赖

```text
T6
T7
Z3
```

---

## 44. Z5 — 光滑参数族

**类：** `DEF`
**优先级：** `[SUPPORTING]`

定义 (A(p,t)=a_t(p)) 与 (\mathcal Z=A^{-1}(0))。

### 依赖

```text
C2
Z3
```

---

## 45. T8 — 正则总零集定理

**类：** `PROP`
**优先级：** `[OPTIONAL]`

证明 (\mathcal Z) 在非退化条件下是光滑子流形。

### 依赖

```text
Z5
```

---

## 46. Z6 — Properness 与管边界

**类：** `WARNING`
**优先级：** `[CRITICAL]`

陈述总零集拓扑保持需 properness。

### 依赖

```text
T8
```

---

## 47. Z7 — 极小多重零示例

**类：** `EX`
**优先级：** `[OPTIONAL]`

仅完全验证时含。

### 依赖

```text
T7
Z3
```

---

# 第九部分. ACS 与 torsion 支

## 48. G1 — ACS charge 映射与路径

**类：** `DEF`
**优先级：** `[CRITICAL]`

定义 (A,M)、(C_\gamma) 与总 charge 映射。

### 严格依赖

```text
C0
T3
```

---

## 49. T9 — ACS 求值公式

**类：** `PROP`
**优先级：** `[CRITICAL]`

证明：

[
\nu_x(\gamma)
=============

e^{M_\gamma}
\left(
x+\int_{C_\gamma}e^{-M},dA
\right).
\]

### 严格依赖

```text
G1
T3
```

---

## 50. G2 — 尺度相容历史

**类：** `DEF`
**优先级：** `[CRITICAL]`

定义 (M_\gamma=M_\delta)。

### 严格依赖

```text
A3
T9
```

---

## 51. G3 — Charge 相容历史

**类：** `DEF`
**优先级：** `[CRITICAL]`

定义 ((A_\gamma,M_\gamma)=(A_\delta,M_\delta))。

### 严格依赖

```text
G1
```

---

## 52. T10 — 相对 torsion 独立

**类：** `PROP`
**优先级：** `[CRITICAL]`

证明尺度相容历史下 (\tau(\gamma,\delta)) 独立于 (x)。

### 严格依赖

```text
A3
G2
T9
```

---

## 53. T11 — 边界积分公式

**类：** `PROP`
**优先级：** `[CRITICAL]`

把 (\tau) 表达为加权围线积分。

### 严格依赖

```text
G1
G3
T10
```

---

## 54. T12 — 加权 torsion–Stokes 定理

**类：** `THM`
**优先级：** `[CRITICAL]`
**目标标签：** `thm:torsion-stokes`

证明：

[
\tau(\gamma,\delta)
===================

\iint_{\Sigma_{\gamma,\delta}}d\eta.
\]

### 严格依赖

```text
T11
```

---

# 第十部分. 接触支

## 55. K1 — 算术接触形式

**类：** `DEF`
**优先级：** `[CRITICAL]`

定义：

[
\alpha
======

da-(\mu,du+\lambda a,dv).
\]

### 严格依赖

```text
C2
F2
```

---

## 56. T13 — 接触非退化

**类：** `PROP`
**优先级：** `[CRITICAL]`

证明当 (\mu\lambda\neq0) 时：

[
\alpha\wedge d\alpha\neq0.
\]

### 严格依赖

```text
C2
K1
```

---

## 57. K2 — 水平提升

**类：** `DEF`
**优先级：** `[CRITICAL]`

定义：

[
D_u=\partial_u+\mu\partial_a,
\qquad
D_v=\partial_v+\lambda a\partial_a.
\]

### 严格依赖

```text
K1
```

---

## 58. T14 — 流 Legendrian 实现

**类：** `PROP`
**优先级：** `[CRITICAL]`

证明切于 (\cos\theta D_u+\sin\theta D_v) 的曲线满足流方程。

### 严格依赖

```text
K2
T5
```

---

## 59. T15 — 水平曲率括号

**类：** `THM`
**优先级：** `[CRITICAL]`
**目标标签：** `thm:contact-curvature`

证明：

[
[D_u,D_v]
=========

\mu\lambda\partial_a.
\]

### 严格依赖

```text
C2
K2
```

---

## 60. K3 — 精确有限交换子公式

**类：** `PROP`
**优先级：** `[OPTIONAL]`

计算 (mh(e^{lk}-1)) 与闭环垂直漂移。

### 依赖

```text
C0
K2
T15
```

---

## 61. K4 — 水平协变微分

**类：** `DEF`
**优先级：** `[CRITICAL]`

定义：

[
\delta_HF
=========

dF-(\partial_aF)\alpha.
\]

### 严格依赖

```text
K1
K2
```

---

## 62. T16 — 水平微分曲率

**类：** `PROP`
**优先级：** `[CRITICAL]`

证明：

[
\delta_H^2F
===========

\mu\lambda(\partial_aF),du\wedge dv.
\]

### 严格依赖

```text
K4
T15
```

---

## 63. T17 — 局部全局 torsion 综合

**类：** `THM`
**优先级：** `[CRITICAL]`

陈述对应：

[
\text{finite defect}\longleftrightarrow\text{weighted area},
\qquad
\text{infinitesimal defect}\longleftrightarrow\text{curvature}.
\]

### 严格依赖

```text
A4
K3
T12
T15
T16
```

---

# 第十一部分. 叙事边

## 64. 射影定位在仿射理论前

```text
T2 PGL₂ generation -.-> T5 affine flow
```

流可独立定义，但射影定位先解释为何仿射是自然扇区。

---

## 65. 正则零定理在奇异定义前

```text
T7 Regular zero-locus theorem -.-> Z3 Singular AES
```

奇异定义可独立陈述，但定理解释为何奇异对孤立或分支零必要。

---

## 66. ACS 在接触综合前

```text
T12 Torsion–Stokes -.-> T17 Local-global synthesis
```

接触括号不依赖 ACS，但最终解释依赖。

---

# 第十二部分. 可选节点与删除政策

## 67. 可选节点

以下节点可移除主文而不破坏关键路径：

| 节点 | 结果 | 推荐回退 |
| ---- | ----------------------------------- | -------------------------- |
| A2   | Maurer–Cartan 公式 | 附录 B |
| F4   | 矫正坐标 | 附录 C 或 Paper II |
| F5   | Taylor 导出 torsion 密度 | 接触章比较 |
| E3   | 曲率归一化 | 附录 C |
| E5   | Baumslag–Solitar 关系 | 注或附录 |
| E6   | Laplace 特征函数 | 太长则 Paper II |
| Z4   | 孤立零模型 | 示例或附录 |
| Z7   | 多重零示例 | Paper III |
| K3   | 长有限交换子计算 | 附录 D |

可选节点不得被关键节点引用为前置。

---

## 68. 条件包含测试

可选节点只有以下条件进入主文：

1. 其陈述数学稳定；
2. 其证明完整；
3. 其记号一致；
4. 它实质推进中心叙事；
5. 它不使 Paper I 超出范围或长度预算。

---

# 第十三部分. 机器可读邻接表

## 69. 严格与定义依赖

以下列表意图供 Codex 与审计脚本。

```yaml
nodes:
  C0:
    type: convention
    title: chronological composition and action conventions
    critical: true
    depends_on: []

  C1:
    type: convention
    title: algebraic domains and admissibility
    critical: true
    depends_on: []

  C2:
    type: convention
    title: differential-geometric hypotheses
    critical: true
    depends_on: []

  S1:
    type: definition
    title: arithmetic expression trees
    critical: true
    depends_on: [C1]

  S2:
    type: definition
    title: internal-node dependency poset
    critical: true
    depends_on: [S1]

  T1:
    type: theorem
    title: sequential-tree classification
    critical: true
    depends_on: [S1, S2]

  S3:
    type: definition
    title: marked spinal histories
    critical: true
    depends_on: [C0, T1]

  S4:
    type: definition
    title: mirror reversal and path inverse
    critical: true
    depends_on: [C0, S3]

  S5:
    type: definition
    title: levels of equality
    critical: false
    depends_on: [S3, P2, G1]

  P1:
    type: definition
    title: projective semantics of one-hole contexts
    critical: true
    depends_on: [C1, S3]

  P2:
    type: definition
    title: projective evaluation map
    critical: true
    depends_on: [C0, P1, S3]

  T2:
    type: theorem
    title: bilateral arithmetic generates PGL2
    critical: true
    depends_on: [C1, P1, P2]

  P3:
    type: corollary
    title: affine Borel sector
    critical: true
    depends_on: [P1, T2]

  P4:
    type: proposition
    title: positive real affine sector
    critical: true
    depends_on: [C2, P3]

  P5:
    type: remark
    title: Riccati completion
    critical: false
    depends_on: [T2, P3, F1]

  A1:
    type: proposition
    title: affine composition law
    critical: true
    depends_on: [C0, P3]

  T3:
    type: proposition
    title: target-frame affine cocycle
    critical: true
    depends_on: [A1, C0]

  T4:
    type: proposition
    title: source-normalized affine cocycle
    critical: true
    depends_on: [T3]

  A2:
    type: proposition
    title: left and right affine differentials
    critical: false
    depends_on: [C0, T3, T4]

  A3:
    type: proposition
    title: relative affine defect
    critical: true
    depends_on: [P3, T3]

  A4:
    type: proposition
    title: elementary arithmetic torsion
    critical: true
    depends_on: [A3, T3]

  F1:
    type: definition
    title: affine Lie algebra generators
    critical: true
    depends_on: [C2, P4]

  T5:
    type: theorem
    title: continuous affine flow
    critical: true
    depends_on: [C2, F1]

  F2:
    type: proposition
    title: Pfaffian propagation law
    critical: true
    depends_on: [T5]

  E1:
    type: definition
    title: regular arithmetic expression space
    critical: true
    depends_on: [C2, T5]

  F3:
    type: proposition
    title: metric-compatible eikonal equation
    critical: true
    depends_on: [C2, E1, T5]

  F4:
    type: proposition
    title: rectifying coordinate
    critical: false
    depends_on: [F3]

  F5:
    type: proposition
    title: infinitesimal torsion density
    critical: false
    depends_on: [A4, T5]

  E2:
    type: proposition
    title: invariant affine metric
    critical: true
    depends_on: [C2, P4]

  T6:
    type: theorem
    title: basic hyperbolic AES
    critical: true
    depends_on: [E1, E2, F3]

  E3:
    type: proposition
    title: Gaussian curvature
    critical: false
    depends_on: [T6]

  E4:
    type: proposition
    title: arithmetic grid actions
    critical: false
    depends_on: [C0, T6]

  E5:
    type: proposition
    title: Baumslag-Solitar relation
    critical: false
    depends_on: [C0, E4]

  E6:
    type: proposition
    title: Laplace eigenfunction
    critical: false
    depends_on: [C2, T6]

  Z1:
    type: definition
    title: zero set
    critical: true
    depends_on: [E1]

  T7:
    type: theorem
    title: regular zero-locus theorem
    critical: true
    depends_on: [C2, F3, Z1]

  Z2:
    type: corollary
    title: zero-set rigidity
    critical: true
    depends_on: [T7]

  Z3:
    type: definition
    title: singular arithmetic expression space
    critical: true
    depends_on: [C2, E1]

  Z4:
    type: example
    title: isolated-zero model
    critical: false
    depends_on: [T6, T7, Z3]

  Z5:
    type: definition
    title: smooth parameter family and total zero set
    critical: false
    depends_on: [C2, Z3]

  T8:
    type: proposition
    title: regular total-zero-set theorem
    critical: false
    depends_on: [Z5]

  Z6:
    type: warning
    title: properness and tube boundary
    critical: true
    depends_on: [T8]

  Z7:
    type: example
    title: minimal multi-zero example
    critical: false
    depends_on: [T7, Z3]

  G1:
    type: definition
    title: ACS charge map and path
    critical: true
    depends_on: [C0, T3]

  T9:
    type: proposition
    title: ACS evaluation formula
    critical: true
    depends_on: [G1, T3]

  G2:
    type: definition
    title: scale-compatible histories
    critical: true
    depends_on: [A3, T9]

  G3:
    type: definition
    title: charge-compatible histories
    critical: true
    depends_on: [G1]

  T10:
    type: proposition
    title: relative torsion independence
    critical: true
    depends_on: [A3, G2, T9]

  T11:
    type: proposition
    title: boundary-integral formula
    critical: true
    depends_on: [G1, G3, T10]

  T12:
    type: theorem
    title: weighted torsion-Stokes theorem
    critical: true
    depends_on: [T11]

  K1:
    type: definition
    title: arithmetic contact form
    critical: true
    depends_on: [C2, F2]

  T13:
    type: proposition
    title: contact nondegeneracy
    critical: true
    depends_on: [C2, K1]

  K2:
    type: definition
    title: horizontal lifts
    critical: true
    depends_on: [K1]

  T14:
    type: proposition
    title: Legendrian realization of flow
    critical: true
    depends_on: [K2, T5]

  T15:
    type: theorem
    title: horizontal curvature bracket
    critical: true
    depends_on: [C2, K2]

  K3:
    type: proposition
    title: exact finite commutator formulas
    critical: false
    depends_on: [C0, K2, T15]

  K4:
    type: definition
    title: horizontal covariant differential
    critical: true
    depends_on: [K1, K2]

  T16:
    type: proposition
    title: horizontal differential curvature
    critical: true
    depends_on: [K4, T15]

  T17:
    type: theorem
    title: local-global torsion synthesis
    critical: true
    depends_on: [A4, K3, T12, T15, T16]
```

---

# 第十四部分. 拓扑实现顺序

## 70. 所需实现序列

一个有效拓扑实现顺序是：

```text
1.  C0, C1, C2
2.  S1
3.  S2
4.  T1
5.  S3
6.  S4
7.  P1
8.  P2
9.  T2
10. P3
11. P4
12. A1
13. T3
14. T4
15. A3
16. A4
17. F1
18. T5
19. F2
20. E1
21. F3
22. E2
23. T6
24. Z1
25. T7
26. Z2
27. Z3
28. G1
29. T9
30. G2
31. G3
32. T10
33. T11
34. T12
35. K1
36. T13
37. K2
38. T14
39. T15
40. K4
41. T16
42. K3
43. T17
```

支持与可选节点可在其前置后插入：

```text
S5, P5, A2, F4, F5, E3, E4, E5, E6, Z4, Z5, T8, Z6, Z7.
```

---

# 第十五部分. 审计义务

## 71. 依赖审计问题

对每个定理或命题，审计必须回答：

1. 所有符号在陈述前定义？
2. 所有假设显式继承？
3. 结果局部还是全局？
4. 它需普通还是射影可允许性？
5. 它需 (\mu\neq0)、(\lambda\neq0) 或正性？
6. 它需度量？
7. 它需完备性或 properness？
8. 它依赖尚未固定约定？
9. 证明独立于后续论文材料？
10. 结果被任何更早节点使用，创建循环？

---

## 72. 缺失证明处理

若所需节点未完全证明：

* 不静默移除节点；
* 在 `05-mathematical-status.md` 标其状态；
* 列出缺失证明义务；
* 防下游节点被标完成；
* 需要时草稿用条件措辞。

润色但不完整证明不满足依赖。

---

## 73. 变更传播规则

节点改变时，重查所有后代。

示例：

### 若 C0 改变

重查：

* P2；
* T2；
* T3；
* E4–E5；
* G1 与 T9–T12；
* K3。

### 若正则 AES 定义改变

重查：

* F3；
* T6；
* T7；
* Z3；
* Paper II 导入；
* Paper III 导入。

### 若 torsion 符号约定改变

重查：

* A4；
* T10–T12；
* K3；
* T17；
* 每个 ACS 图与示例。

### 若 (\mathfrak E_0) 归一化改变

重查：

* E3；
* E4；
* E6；
* 零集示例；
* Paper II 算子公式。

### 若盖/界面注改变

`rem:capping-scope-mu-essential`（注 10.13）与 `rem:capping-singular-branch-nonempty`（注 10.15）
是 `thm:constant-boundary-capping-obstruction`（定理 10.12）与 `cor:capping-dichotomy`（推论
10.14）的范围注。它们给此图**不加节点不加边**，且不改其所评论两陈述的任何假设。编辑它们仍需
重查：

* 定理 10.12 下游打印编号（两注共享章计数器：插入或移除一个平移 `cor:capping-dichotomy` 与
  `def:certified-cap-tuple`，及对其打印号的任何文本交叉引用）；
* `governance/08-open-questions.md` OQ-099 状态表；
* `research/capping-scope/`（其 README 引打印号）与 `verify_capping.py` 的 `paper_action_taken` 字段。

### 登记缺口：盖/界面支

封顶界面材料（定理 10.4 孔盘互补、命题 10.7 接缝圆 holonomy、命题 10.9 多项式界面谱、定理 10.12
封顶阻碍、推论 10.14 封顶二分、定义 10.16 认证盖元组）**尚未登记为此图节点**。两后果随之且被
记录而非静默修复：

* 上述变更传播规则尚不能按节点重查此材料；
* 其证明状态未录入 `governance/05-mathematical-status.md`。

2026-11-01 添加的两注都是**范围注**：它们既不创建节点也不改假设，故第一至十七部分无边改变。把
此支登记为节点（带显式「AES 盘有常边界」假设节点，即阻碍实际消耗者）是单独任务。

---

# 第十六部分. 导出到后续论文

## 74. Paper II 导出边界

Paper II 只可导入完成版本：

```text
E1  Regular AES
F3  Eikonal equation
T6  Basic hyperbolic model
T7  Regular zero-locus theorem
K1  Contact form
K2  Horizontal lifts
T15 Horizontal curvature bracket
K4  Horizontal covariant differential
T16 Horizontal curvature formula
```

Paper II 必须添加而非假定：

* 超出 Paper I 的水平度量选择；
* 相容复结构；
* 解析算子域；
* 伴随；
* 边界理论；
* 算术全纯性。

---

## 75. Paper III 导出边界

Paper III 可导入：

```text
E1  Regular AES
T7  Regular zero-locus theorem
Z3  Singular AES
Z5  Parameter-family notation
T8  Regular total-zero-set theorem, if retained
K1–T16 Contact and horizontal structures
```

Paper III 必须证明：

* 判别式理论；
* 真管定理；
* 拓扑改变；
* 单值；
* 辫或纽结不变。

---

## 76. Paper IV 导出边界

Paper IV 可导入：

```text
S3  Marked spinal histories
S4  Mirror/reversal/inverse
P2  Projective evaluation
T2  PGL₂ generation
P3  Affine/Borel sector
T3–T4 Affine cocycles
A3  Relative affine defect
G1  ACS
T12 Torsion–Stokes theorem
```

Paper IV 必须发展：

* 历史群胚；
* 双赋值；
* 商塔；
* 射影凝聚；
* 复杂度度量与成本模型。

---

# 第十七部分. 完成判据

## 77. 图完成测试

定理依赖图只有以下条件满足：

* 每个 `[CRITICAL]` 节点有稳定定义或已证明陈述；
* 每个严格依赖在最终论文中向后指；
* 无关键定理依赖可选示例；
* 无 Paper II–IV 结果用于证明 Paper I 结果；
* 所有约定敏感公式在 C0 下检查；
* 所有零集陈述在 C2 下检查；
* 所有 ACS 符号在一个定向约定下检查；
* T17 区分精确有限恒等式与无穷小对应。

---

## 78. 最终依赖摘要

Paper I 有一个基础主干：

[
\boxed{
\text{sequential tree}
\to
\text{marked history}
\to
PGL_2
\supset
\operatorname{Aff}(1)
\to
\text{cocycle}
\to
\text{flow}.
}
]

从此主干出现三个大体独立几何支：

[
\boxed{
\begin{array}{lll}
\textbf{Model branch:}
&
\text{flow}
\to
\text{regular AES}
\to
\mathfrak E_0
\to
\text{regular zeros};
[2mm]
\textbf{Global branch:}
&
\text{affine cocycle}
\to
\text{ACS}
\to
\text{relative torsion}
\to
\text{weighted area};
[2mm]
\textbf{Local branch:}
&
\text{flow}
\to
\text{contact connection}
\to
\text{horizontal curvature}.
\end{array}
}
]

论文以结合全局与局部支结束：

[
\boxed{
\text{history-order defect}
\longleftrightarrow
\text{ACS weighted area}
\longleftrightarrow
\text{contact curvature},
}
]

精确有限恒等式与无穷小对应分开陈述。

---

## 79. 算术–自守扩展节点

以下节点扩展闭 Paper I 图而不改其内部证明顺序。

```text
P1-H1  Paper I projective arithmetic contexts T_s and J
P1-H2  q=4 Hecke subgroup identification
P1-Z9  complete boundaryless regular-AES splitting

P2-A1  planar harmonic AES target
P2-A2  cylindrical AES target
P2-A3  holomorphic local-diffeomorphism pullback

P3-S1  critical-point essentiality
P3-S2  2m-prong / 2 pi m cone theorem
P3-S3  normalized (2,4,infinity) Hauptmodul input
P3-S4  exact Hecke zero-dessin AES

P3-K1  sign-cover signature and coarse cylindrical completion
P3-K2  hyperbolic unit-tangent sign cover as S3 minus T(2,4)
P3-K3  primitive Hecke classes and periodic-orbit knots
P3-K4  zero-dessin coding spine and template boundary

P3-R1  relative prime-divisor normalization
P3-R2  arithmetic/geometric irreducibility separation
P3-R3  history-to-divisor naturality [RESTRICTED MODEL PROVED; GENERAL OPEN]
P3-R4  quadratic supplied-register divisor, collapse kernel, and Frobenius
P3-R5  quartic arithmetic/geometric splitting and Frobenius test

P3-H1  polynomial carrier and intrinsic root thread
P3-H2  quadratic threaded-carrier topology and torus-link thread
P3-H3  discriminant--framing--braid--Euler identity
P3-H4  q=4 marked peripheral toric binomial
P3-H5  q=4 logarithmic-tangent weighted cone and cusp link
P3-H6  supplied four-strand braid-center and LHS-transgression calibration
P3-H7  unrestricted history-to-coefficient-path naturality [OPEN]

P3-L1  supplied sextic event-polynomial calculation
P3-L2  regular sextic LL cover: 1296 normalized sheets / 216 rotation orbits
P3-L3  caustic-cubed / Maxwell-squared bifurcation divisor
P3-L4  displayed spanning-star surjection onto B6
P3-L5  compatible carrier, six-root thread, and genus-two mapping torus
P3-L6  genus-two mapping-class and symplectic monodromy specialization
P3-L7  mixed-braid exact sequence and LL pullback
P3-L8  displayed arithmetic fiber: S6 Galois and geometric End = Z
P3-L9  explicit geometric LL--Igusa twin; spectral descent, forgetting variance,
       and balanced moving-slice divisor charge [PROVED]
P3-L10 full 216-orbit census; arithmetic/period/marked/Hodge-energy refinements [OPEN]
```

新依赖边是：

```text
P1-H1 -> P1-H2
T7 regular zero theorem -> P1-Z9
complete metric + boundaryless carrier -> P1-Z9
P1-H2 -> P3-S3

P2-A1 -> P2-A3
P2-A2 -> P2-A3
P2-A3 -> P3-S1 -> P3-S2
P2-A3 -> P3-S4
P3-S3 -> P3-S4

P3-S4 -> P3-K1
P3-K1 + classical lens-space input -> P3-K2
P1-H2 -> P3-K3
P3-S4 + classical geodesic coding -> P3-K4

P3-R1 -> P3-R2
P1-H2 + supplied quadratic register -> P3-R4
P3-R1 + supplied quartic registers -> P3-R5
P3-R4 -. restricted naturality evidence .-> P3-R3
P3-R5 -. finite arithmetic test .-> P3-R3

P2-A3 -> P3-H1 -> P3-H2
P3-H1 -> P3-H3
P3-K2 -> P3-H4 -> P3-H5
P3-K1 -> P3-H5
P1-H2 + braid-center input -> P3-H6
P3-H4 -. marked toric evidence .-> P3-H7
P3-H5 -. logarithmic-cone evidence .-> P3-H7
P3-H6 -. extension-class evidence .-> P3-H7

supplied P0 + direct discriminant calculation -> P3-L1
classical LL theorem + normalized sextic space -> P3-L2
classical LL local bifurcation models -> P3-L3
P3-L1 + classical local half-twist input -> P3-L4
P3-H1 + P3-L1 + collision-free loop -> P3-L5
P3-L4 + classical Birman--Hilden/symplectic input -> P3-L6
P3-L2 + mixed configuration-space extension -> P3-L7
P3-L4 -> P3-L7
supplied arithmetic fiber + classical Galois/Zarhin criteria -> P3-L8
P3-L2 + exact sparse resultant + Clebsch invariant -> P3-L9
P3-L2 + finite-etale quotient + sheet observable -> P3-L9
P3-L9 + moving t-slices -> P3-L9 divisor charge
P3-L9 -. existence input for deeper census .-> P3-L10
P3-L7 -. typed path target evidence .-> P3-H7
```

虚边不授权定理。特别 `P3-R3` 非 `P3-S4` 的依赖：精确 Hecke 模型由算子子群与其标准 Hauptmodul
构造，无一般历史函子。

## 80. 状态与非蕴含门禁

* `P1-H2` 由初等矩阵计算与引用标准 Hecke 群等同证明。
* `P1-Z9` 由矫正赋值、完备 Riemannian 流形上有界向量场完备性，与全局流映射证明。它只给微分同胚
  乘积，非等距分裂。
* `P2-A1`–`P2-A3` 是正则轨迹上直接解析计算。
* `P3-S1`–`P3-S2` 是奇异 AES 范畴局部计算。
* `P3-S3` 是外部标准一致化输入且必须引用。
* `P3-S4` 是条件于归一化输入的 AEG 构造。
* `P3-R1`–`P3-R2` 是带所述假设的标准相对除子事实。
* `P3-K1` 由显式符号特征与 Hauptmodul–Cayley 坐标证明。其粗平坦柱面非双曲单位切丛。
* `P3-K2` 组合显式指标二覆盖与斜率计算与引用经典透镜空间紧化。楼上局部锥角非环面链环不变量。
* `P3-K3`–`P3-K4` 特化引用测地流编码定理并证明此处所需对象类型等同。它们不产新纽结不变量。
* `P3-R4`–`P3-R5` 对显式提供带型寄存器证明。它们测试除子等变、坍缩、不可约、单值与 Frobenius 而
  不从无限制历史导出那些寄存器。
* `P3-R3` 因此在受限模型部分解决，而一般历史到除子函子仍开放且不能支持一般自然性或忠实性断言。
* `P3-L1`、`P3-L4`、`P3-L5` 与 `P3-L7` 对提供六次与打印环/构型假设证明。它们不在无限制历史上
  定义构造。
* `P3-L2`、`P3-L3`、`P3-L6` 与 `P3-L8` 是六次实验室中特化并审计的经典结果或判据。(1296) 归一化
  LL 叶与其 (216) 源旋转轨道非非同构曲线计数。
* `P3-L9` 由显示精确第二叶证明：LL 事件多项式相等由精确结式与缩放恒等式得出，而 (t=1) 处不同
  绝对 Igusa–Clebsch 比证明两曲线在 (\mathbb C) 上非同构。在度 (216) 商覆盖上，有限平坦范下降给
  谱多项式，置换平均给规范常数/零和正合序列与单值不变方差。孪生供其精确正下界。沿两条显式切片
  铅笔，同不变比在正则纤维有除子 (5[\beta]-5[0])。
* `P3-L10` 仍开放。定理不枚举全部 (216) 旋转轨道、不比 Frobenius 多项式或约化 Siegel 周期、不
  固定并商标记局部辛单值/Hurwitz 数据。它也不构造 Hodge- 或 Siegel-度量能量。
* P3-L9 方差在闭环置换单值下不变但不必沿事件多项式任意开路径恒常。移动切片除子是平衡对数
  charge，非有限 Dirichlet 能量。
* 进 `P3-L7` 的实边是混合辫扩张的拉回。它非且不得重绘为遗忘 LL 叶后的同态 (B_5\to B_6)。
* 从 `P3-L7` 到 `P3-H7` 的虚边记录未来历史函子的带型目标，非该函子存在或自然性。

以下蕴含禁止：

```text
Hecke subgroup generation =/=> histories are tiles
rich zero dessin          =/=> history-derived arithmetic divisor
local four-prong cone      =/=> the global T(2,4) link
bare zero dessin           =/=> the three-dimensional flow template
primitive Hecke element    =/=> prime knot
terminal endpoint divisor  =/=> marked-history faithfulness
arithmetic divisor        =/=> proper zero tube
singular zero tube        =/=> Markov invariant
1296 normalized LL sheets =/=> 1296 nonisomorphic genus-two curves
216 source-rotation orbits =/=> 216 nonisomorphic genus-two curves
critical-value braid      =/=> unmarked B5-to-B6 homomorphism
common Sp4(F2) = S6 target =/=> Frobenius/topological-loop identification
full B6 monodromy         =/=> new knot invariant.
```

## 有限型/移植集成依赖 — 2026-10-09

添加链有显式依赖：

```text
regular AES + nonvanishing differential
  -> critical-set theorem WITH extending conformal background
  -> restricted critical-count construction
regular AES definition + explicit polynomial a
  -> arbitrary-k example (direct proof, independent of critical-set theorem)
finite-type carrier + punctured-disc ends
  -> conformal point compactification
regular AES + full oriented collar atlas + fixed signed μ,λ
  -> geometric descent + canonical-frame and local-flow compatibility
explicit k4 a,g + canonical frame + smooth local flows
  -> nonzero level-set residue for a scalar-identity word
finite strict typed DAG + explicit copy/discard + occurrence-safe substitution
  -> exact partial-domain substitution/evaluation compatibility
geometric collar descent + complete port/interface inventory + GLOBAL DAG
  -> joint geometric/computational descent
contextual residual experiment + feature map
  -> observation factorization iff contextual refinement
  -> exact online feature machine only with right congruence and output factorization
```

无箭头从裤拓扑、FN 坐标、圆关联或有限标量示例跑到忠实多输入 AES 运动实现。完备度量阻碍从
Paper I 现有分裂定理导入，非重证或加强为新分类。

## Paper III 强度修正（2026-11-09）

历史 S-0010 箭头由 S-0011 替换：

```text
fixed A + conformal realization -> fixed zero incidence (P3-L11)
fixed g + fixed rectified t -> common level foliation (P3-L11)
fixed g alone -/-> fixed zero carrier (moving-line counterexample)
compact connected M + dA nonzero -> diam(g_lambda) -> 0 (P3-L12)
admissible gradient access -> exact distance to zero (P3-L12)
one-sided Lipschitz coarea densities -> sided area coefficient (P3-L12)
fixed induced zero tensor -/-> ambient distance isometry (cylinder counterexample)
```

P3-L12 从 `thm:conformal-realization` 导入共形实现；其紧坍缩证明在命题自身。它不从 Paper 0 导入
GH 载体极限定理。无箭头从仅度量收敛产极限赋值。未变单位缩放恒等式与固定载体和紧坍缩陈述都分开。
