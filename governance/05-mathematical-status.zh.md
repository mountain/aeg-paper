# 数学状态登记

**文件：** `governance/05-mathematical-status.md`
**状态：** 权威
**版本：** 1.1
**日期：** 2026-08-06
**依赖：**

* `AGENTS.md`
* `governance/00-authoritative-scope.md`
* `governance/01-paper-series-architecture.md`
* `governance/02-paper-I-outline.md`
* `governance/03-theorem-dependency-graph.md`
* `governance/04-current-to-target-map.md`

**适用于：** Papers I–IV 及其支持笔记中的数学论断。

**修正案（2026-09-22）：** Paper 0 的论断单独登记于
`governance/05b-paper-0-status-register.md`，由权威修正案
`00b-paper-0-geometric-foundation-amendment.md` 创建。凡结果从 Paper I 移到 Paper 0，此处对
Paper I 记录的状态被 `05b` 条目取代；结果的数学内容与状态不因移动而变。

---

## 1. 目的

本文档记录 AEG 仓库主要定义、论断、命题、定理、构造与研究计划的当前数学状态。

其目的是：

* 防止猜想与提案在编辑重组期间被提升为定理；
* 区分已有证明与仅看似合理或标准的结果；
* 记录必须附着于结果的假设；
* 在依赖结果可标完成前识别证明义务；
* 决定哪些论断可出现在摘要、引言与结论；
* 为 Codex 与人类合作者提供共同状态词汇。

本文件记录数学状态，非仅编辑目的地。

论断可属 Paper I 而仍未证明。反之，已证明论断可因在 Paper I 范围之外而移到 Paper IV。

---

# 第一部分. 状态词汇

## 2. 权威状态标签

每条实质数学论断必须用以下之一标签。

### `PROVED`

完整证明存在于仓库或已被独立检查，且定理按陈述正确。

带此标签结果可能仍需编辑迁移或记号归一化。

---

### `PROVED WITH STATED HYPOTHESES`

完整证明可用，但结果仅在必须保持显式的假设下有效。

典型假设含：

* (K) 是域；
* 语境非退化；
* 乘子非零；
* (\mu\lambda\neq0)；
* 度量与赋值光滑；
* 陈述局部而非全局。

---

### `STANDARD CONSEQUENCE REQUIRING AN IN-PAPER PROOF`

结果直接来自标准定理或短计算，但所需证明或引用尚未存在于目标论文。

此状态不授权省略假设。

---

### `COMPUTATIONALLY VERIFIED EXAMPLE`

论断已对有限参数集、符号计算或绘制示例检查，但无一般证明。

它可作示例出现，非一般定理证据。

---

### `PARTIALLY PROVED`

证明存在于受限情形或若干分量已证明，但完整目标陈述未建立。

必须记录精确已证明子情形。

---

### `STRUCTURAL PROPOSAL`

论断定义潜在有用框架、解释或对象，但无存在、唯一、不变或完备定理已证明。

定义稳定期间可有此状态。

---

### `CONJECTURE`

数学精确的未证明断言，带陈述的支持证据。

---

### `OPEN PROBLEM`

无候选陈述或答案方向的问题。

---

### `UNSUPPORTED AND EXCLUDED`

断言被反驳、无支持或已从活跃理论排除。

它可能出现在：

* 历史讨论；
* 拒绝登记；
* 显式反例。

它不得出现在活跃定理链。

---

# 第二部分. 解释规则

## 3. 状态与证明

`PROVED` 标签指证明存在于仓库或独立验证。

它不意味：

* 证明从外部来源正确引用；
* 结果自动属 Paper I；
* 结果不需迁移。

当证明依赖未在状态文件中记录的外部或口头来源时，必须标：

```text
STANDARD CONSEQUENCE REQUIRING AN IN-PAPER PROOF
```

或

```text
PROVED WITH STATED HYPOTHESES
```

连同缺失引用。

---

## 4. 状态与目的地位

数学状态与编辑目的地是不同轴。

| 状态 | 目的地 |
| --- | --- |
| `PROVED` | 可能属 Paper I 或后续论文 |
| `PROVED WITH STATED HYPOTHESES` | 可能属任何论文 |
| `CONJECTURE` | 可能属任何论文 |
| `STRUCTURAL PROPOSAL` | 通常后续论文 |
| `OPEN PROBLEM` | 任何论文或开放问题文件 |

编辑重组不得因结果移动到另一论文而提升其状态。

---

## 5. 状态提升

从较弱到较强状态的提升仅在以下情况允许：

* 提供完整证明；
* 验证或移除所需假设；
* 独立审查确认；
* 变更记录于本文件。

不通过重写被提升陈述的编辑重组。

---

## 6. 状态降级

状态降级是允许的当：

* 反例发现；
* 缺口识别；
* 假设显示被遗漏；
* 引用来源不充分；
* 表述后来显示无支持。

降级必须记录于本文件并解释。

---

# 第三部分. Paper I 基础状态

## 7. 顺序语法支

以下节点属于 Paper I 顺序语法支。

| 节点 | 状态 |
| --- | --- |
| S1 算术表达式树 | `PROVED`（定义） |
| S2 依赖偏序 | `PROVED`（定义） |
| T1 顺序树分类 | `PROVED` |
| S3 标记脊柱历史 | `PROVED`（定义与对应） |
| S4 镜像/反演/逆 | `PROVED`（定义与区分） |
| S5 相等层级 | `PROVED`（定义） |

### 剩余义务

* 完全移除「threadlike」定义；
* 证明标记树到历史对应逆；
* 审计所有镜像/反演示例。

---

## 8. 射影支

| 节点 | 状态 |
| --- | --- |
| P1 单孔语境射影语义 | `PROVED WITH STATED HYPOTHESES` |
| P2 射影求值映射 | `PROVED WITH STATED HYPOTHESES` |
| T2 双边生成定理 | `PROVED WITH STATED HYPOTHESES` |
| P3 仿射/Borel 扇区 | `PROVED` |
| P4 正实仿射扇区 | `PROVED` |

---

## 9. 仿射余循环支

| 节点 | 状态 |
| --- | --- |
| A1/T3 目标框架余循环 | `PROVED` |
| T4 源归一化余循环 | `PROVED` |
| A2 Maurer–Cartan 形式 | `PROVED`（符号约定审计需） |
| A3 相对仿射缺陷 | `PROVED WITH STATED HYPOTHESES` |
| A4 初等 torsion | `PROVED` |

---

## 10. 流支

| 节点 | 状态 |
| --- | --- |
| F1 仿射 Lie 代数 | `PROVED` |
| T5 连续仿射流 | `PROVED` |
| F2 Pfaffian 形式 | `PROVED` |
| F3 eikonal 方程 | `PROVED WITH STATED HYPOTHESES` |
| F4 矫正坐标 | `PROVED`（可选） |
| F5 无穷小 torsion | `PARTIALLY PROVED`（渐近） |

---

## 11. 模型支

| 节点 | 状态 |
| --- | --- |
| E1 正则 AES | `PROVED`（定义） |
| E2 不变仿射度量 | `PROVED` |
| T6 基本双曲 AES | `PROVED` |
| E3 曲率 | `PROVED` |
| E4 网格作用 | `PROVED` |
| E5 Baumslag–Solitar | `PROVED`（可选） |
| E6 Laplace 特征函数 | `PROVED` |

---

## 12. 零几何支

| 节点 | 状态 |
| --- | --- |
| Z1 零集 | `PROVED`（定义） |
| T7 正则零轨迹 | `PROVED WITH STATED HYPOTHESES` |
| Z2 刚性推论 | `PROVED` |
| Z3 奇异 AES | `PROVED`（定义） |
| Z4 孤立零 | `PROVED`（示例，重新分类） |
| Z5 参数族 | `PROVED`（定义） |
| T8 正则总零集 | `PROVED WITH STATED HYPOTHESES`（可选） |
| Z6 Properness 警告 | `PROVED` |
| Z7 极小多重零 | `OPEN` 或 `COMPUTATIONALLY VERIFIED` |

---

## 13. ACS 与 torsion 支

| 节点 | 状态 |
| --- | --- |
| G1 ACS | `PROVED`（定义） |
| T9 ACS 求值 | `PROVED` |
| G2 尺度相容 | `PROVED`（定义） |
| G3 charge 相容 | `PROVED`（定义） |
| T10 相对 torsion | `PROVED WITH STATED HYPOTHESES` |
| T11 边界积分 | `PROVED` |
| T12 torsion–Stokes | `PROVED WITH STATED HYPOTHESES` |

---

## 14. 接触支

| 节点 | 状态 |
| --- | --- |
| K1 接触形式 | `PROVED`（定义） |
| T13 非退化 | `PROVED WITH STATED HYPOTHESES` |
| K2 水平提升 | `PROVED`（定义） |
| T14 Legendrian 流 | `PROVED` |
| T15 曲率括号 | `PROVED` |
| K3 有限交换子 | `PROVED`（符号审计需） |
| K4 水平微分 | `PROVED`（标量场上） |
| T16 水平曲率 | `PROVED` |
| T17 局部全局综合 | `PARTIALLY PROVED`（表述需） |

---

# 第四部分. 需要验证的节点

## 15. 需要额外验证的关键节点

以下节点已标 `PROVED` 但需独立验证。

### 顺序树分类

* [ ] 依赖偏序构造一致；
* [ ] 唯一线性扩张判据；
* [ ] 脊柱判据；
* [ ] 与「threadlike」示例一致。

### 双边生成

* [ ] (C=0) 与 (C\neq0) 情形；
* [ ] 特征二行为；
* [ ] 历史语言域；
* [ ] 矩阵作用约定。

### 正则零轨迹

* [ ] 边界情形；
* [ ] 全局对局部陈述；
* [ ] (\mu\neq0) 假设；
* [ ] 非光滑度量行为。

### Torsion–Stokes

* [ ] 定向约定；
* [ ] 带符号路径；
* [ ] 非简单路径；
* [ ] 退化情形。

---

# 第五部分. 射影支状态

## 16. P1/P2 — 射影语义与求值

### 当前状态

```text
PROVED WITH STATED HYPOTHESES
```

### 建立陈述

非退化单孔语境作用为 (\mathbb P^1(K)) 上分式线性变换。

### 剩余义务

* 明确记录域排除；
* 陈述矩阵作用约定；
* 区分普通与射影语义。

---

## 17. T2 — 双边生成

### 当前状态

```text
PROVED WITH STATED HYPOTHESES
```

### 建立陈述

平移、非零缩放与反演生成 (PGL_2(K))。

（2026-10-29 说明：Paper 0 的 `thm:p0-pgl2-generation` 带完整因式分解证明（含 (C=0) 情形、
特征二注与显式历史词），Paper I 的 `thm:bilateral-pgl2-generation` 对非退化双边历史语言陈述同一
事实并从该定理三行导出。结果状态标签不变，`PROVED WITH STATED HYPOTHESES`；移动的是证明而非
论断。历史级陈述、仿射扇区推论 `cor:affine-borel-sector`（语法仿射子语言到 `B_inf` 的满射，
Paper 0 不陈述）与 `q=4` Hecke 子语言仍属 Paper I。无论断削弱，读者不需 Paper I 得生成定理，
也不需 Paper 0 得 Hecke 子语言。）

---

## 18. P3 — 仿射/Borel 扇区识别

### 当前状态

```text
PROVED
```

### 建立陈述

[
\operatorname{Stab}_{PGL_2(K)}(\infty)
\cong
\operatorname{Aff}(1,K).
]

第一槽非退化算术扇区仿射，服从精确语境限制。

### 剩余义务

* 陈述是否含反射 (z\mapsto c-z)；
* 区分代数 Borel 与其恒等分量；
* 生成元覆盖证明前避免等同所有定手性语法历史与所有仿射映射。

---

## 19. P4 — 正实仿射扇区

### 当前状态

```text
PROVED
```

### 陈述

实参数化：

[
z\mapsto e^\lambda z
]

用正乘子，故连续理论位于：

[
\operatorname{Aff}^{+}(1,\mathbb R).
\]

### 剩余义务

Paper I 中一致用此限定。

---

## 20. Bruhat 解释

### 当前状态

```text
PROVED AS A STANDARD GROUP-THEORETIC FACT
OPTIONAL IN PAPER I
```

### 允许陈述

[
PGL_2(K)=B\sqcup BJB
]

于秩一 Bruhat 胞腔层。

### 剩余义务

不用此注作显式生成证明替代。

---

## 21. P5 — Riccati 完备化

### 当前状态

```text
PROVED AS AN INFINITESIMAL LIE-ALGEBRA STATEMENT
PARTIALLY DEVELOPED AS GEOMETRY
```

### 建立陈述

射影向量场：

[
E=\partial_z,
\qquad
H=z\partial_z,
\qquad
F=z^2\partial_z
]

张局部射影 Lie 代数，产：

[
\dot z=\beta+\alpha z+\kappa z^2.
\]

当前仿射流是切片：

[
\kappa=0.
\]

### 未建立

* 完整射影 AES；
* 替换仿射双曲模型的射影度量；
* 射影接触联络；
* ACS 面积公式射影替代。

这些仍开放或属 Paper IV。

---

# 第六部分. 仿射余循环状态

## 22. A1/T3 — 仿射复合与目标框架余循环

### 当前状态

```text
PROVED
```

### 建立公式

对：

[
f_i(x)=s_ix+t_i,
]

[
f_n\circ\cdots\circ f_1(x)
==========================

\Phi_nx+\xi_n,
]

带：

[
\Phi_n=\prod_{i=1}^{n}s_i,
]

[
\xi_n
=====

\sum_{i=1}^{n}
t_i\prod_{j=i+1}^{n}s_j.
\]

### 剩余义务

最终年代约定下重写。

---

## 23. T4 — 源归一化余循环

### 当前状态

```text
PROVED
```

### 建立公式

[
\widehat\xi_n
=============

# \frac{\xi_n}{\Phi_n}

\sum_{i=1}^{n}
\frac{t_i}{\prod_{j=1}^{i}s_j}.
\]

### 剩余义务

陈述域任意或实，且要求 (s_i\neq0)。

---

## 24. A2 — 左右 Maurer–Cartan 平移形式

### 当前状态

```text
PROVED
SIGN CONVENTION AUDIT REQUIRED
```

### 建立公式

对：

[
g=
\begin{pmatrix}
e^\lambda&\xi\
0&1
\end{pmatrix},
]

[
(g^{-1}dg)_{\mathrm{tr}}
========================

e^{-\lambda}d\xi,
]

[
(dg,g^{-1})_{\mathrm{tr}}
=========================

d\xi-\xi,d\lambda.
\]

---

# 第七部分. ACS 状态

## 25. ACS 与求值

### 当前状态

```text
PROVED
```

### 建立公式

[
\nu_x(\gamma)
=============

e^{M_\gamma}
\left(
x+\int_{C_\gamma}e^{-M},dA
\right).
\]

---

## 26. 相对 torsion

### 当前状态

```text
PROVED WITH STATED HYPOTHESES
```

### 假设

* 尺度相容；
* charge 相容（面积表示需）。

---

## 27. 加权 torsion–Stokes

### 当前状态

```text
PROVED WITH STATED HYPOTHESES
```

### 建立

[
\tau(\gamma,\delta)
===================

\iint_{\Sigma_{\gamma,\delta}}d\eta.
\]

### 剩余义务

* 固定 (\eta) 符号；
* 审计 (dA\wedge dM) 对 (dM\wedge dA)；
* 验证所有示例。

---

# 第八部分. 双曲模型状态

## 28. 基本双曲模型

### 当前状态

```text
PROVED
```

### 建立

[
|\nabla a|^2
============

\mu^2+\lambda^2a^2
]

于上半平面带：

[
a(x,y)=-\frac{x}{y}.
\]

---

## 29. 曲率与归一化

### 当前状态

```text
PROVED
```

### 建立

[
K=-\lambda^2.
\]

---

## 30. Laplace 特征函数

### 当前状态

```text
PROVED
```

### 建立

[
\Delta_g a
==========

2\lambda^2a
\]

于梯度散度约定下。

---

# 第九部分. 零几何状态

## 31. 正则零轨迹

### 当前状态

```text
PROVED WITH STATED HYPOTHESES
```

### 建立

(\mu\neq0) 时 (Z(a)) 是光滑余一维子流形。

---

## 32. 奇异 AES

### 当前状态

```text
PROVED（定义）
```

---

## 33. 孤立零模型

### 当前状态

```text
COMPUTATIONALLY VERIFIED EXAMPLE
RECLASSIFIED AS SINGULAR
```

---

## 34. 参数族

### 当前状态

```text
PROVED WITH STATED HYPOTHESES（可选）
```

---

# 第十部分. 接触状态

## 35. 接触非退化

### 当前状态

```text
PROVED
```

### 公式

[
\alpha
======

da-(\mu,du+\lambda a,dv),
]

[
\alpha\wedge d\alpha
====================

\mu\lambda,du\wedge da\wedge dv
]

到定向。

### 假设

[
\mu\lambda\neq0.
\]

---

## 36. 水平提升与 Legendrian 流

### 当前状态

```text
PROVED
```

### 建立场

[
D_u=\partial_u+\mu\partial_a,
]

[
D_v=\partial_v+\lambda a\partial_a.
\]

切于：

[
\cos\theta D_u+\sin\theta D_v
]

的曲线满足仿射流方程。

---

## 37. 水平曲率括号

### 当前状态

```text
PROVED
```

### 公式

[
[D_u,D_v]
=========

\mu\lambda\partial_a.
\]

### 建立解释

水平分布不可积，且括号缺陷垂直。

---

## 38. 精确有限交换子公式

### 当前状态

```text
PROVED UNDER THE CURRENT FLOW ORDER
SIGN AND COMPOSITION AUDIT REQUIRED
```

### 建立开路径缺陷

[
\mu h(e^{\lambda k}-1).
\]

### 剩余义务

* C0 固定后重算；
* 符号对齐 ACS 定向；
* 避免等同开与闭有限缺陷。

---

## 39. 水平协变微分

### 当前状态

```text
PROVED ON SCALAR FIELDS
```

### 公式

[
\delta_HF
=========

# dF-(\partial_aF)\alpha

(D_uF),du+(D_vF),dv.
\]

定义：

[
\delta_H^2F
:=
(D_uD_vF-D_vD_uF),du\wedge dv.
\]

则：

[
\delta_H^2F
===========

\mu\lambda(\partial_aF),du\wedge dv.
\]

### 所需限制

这尚非形式上完整分次微分演算。

其扩张定义前不声称算子字面 de Rham 意义平方。

---

## 40. 局部全局 torsion 综合

### 当前状态

```text
PARTIALLY PROVED
FORMULATION REQUIRED
```

### 建立分量

* 有限仿射相对缺陷；
* 特殊情形 ACS 加权面积恒等式；
* 精确接触交换子公式；
* 无穷小水平曲率。

### 尚未作为一个定理建立

分离：

1. 精确仿射/ACS 相等；
2. 精确有限接触修正；
3. 无穷小曲率相等。

的单一精确陈述。

### 目标建议

三层无混淆陈述后才把 T17 呈现为综合定理或命题。

### 依赖限制

T17 不得声称所有有限量间字面相等。

---

## 41. Reeb 场与 Darboux 形式

### 当前状态

```text
PROVED BY DIRECT CALCULATION
OPTIONAL IN PAPER I
```

### 范围警告

算术意义在于所选坐标与水平框架，非新接触同构类。

---

# 第十一部分. Paper II 解析状态

## 42. Paper II 集成更新 — 2026-08-06

规范手稿 `paper-2/aeg-paper-2.tex` 现解决下方解析清单。此表取代第 43–52 条预手稿状态描述，后者
作为原始开放问题溯源保留其后。

---

# 第十二部分. Paper III 状态

（Paper III 各节点状态记录于其决定记录与闭包报告；此处保留概述与关键状态变更。）

---

# 第十三部分. Paper IV 状态

（Paper IV 各节点状态记录于其决定记录、红队报告与闭包报告。）

---

# 第十四部分. 状态变更台账

## 43. 状态变更 S-0001 至 S-0009

（历史状态变更记录于带日期治理记录与迁移日志。）

---

## 44. 状态变更 S-0010

（历史强度平面讨论状态；由 S-0011 取代。见下。）

---

## 45. 状态变更 S-0011

- **论断 ID：** P3-L11 与 P3-L12，替换 S-0010 中受影响陈述。
- **先前状态：** P3-L11 `PROVED`；P3-L12 `PROVED WITH STATED HYPOTHESES`。
- **新状态：** 无限制固定度量/共同载体推断与到内在零载体的 GH 收敛、无限制距离上界、环境等距
  与普遍双侧面积系数是 `UNSUPPORTED AND EXCLUDED`（被显式示例反驳）。修正 P3-L11 固定数据陈述
  与修正 P3-L12 是 `PROVED WITH STATED HYPOTHESES`。
- **精确陈述，P3-L11：** 固定赋值给乘积零关联；固定度量连同固定矫正赋值 t、|grad t|=1 给
  a=(|mu|/|lambda|)sinh(|lambda|t) 的共同水平集。仅固定度量不。移动零 Euclid 示例保留于
  `eq:intensity-moving-zero`。联合重标仍保持 eikonal 方程、零集、框架方向与 lambda/mu；框架本身
  按 s^{-1} 缩放，非 1。基本模型因式分解不变。
- **精确陈述（续），P3-L12：** 对带边紧连通定向光滑 M、光滑 h、mu>0、dA 处处非零且非空
  Sigma=A^{-1}(0)，共形实现正则且诱导张量在 Sigma 光滑部分固定。普遍距离估计是**下界**；等号对
  到达 M 内零的归一化梯度轨迹成立。若所有此轨迹留在 M，用 Sigma 的 GH 逼近用 lambda 依赖的**环境
  限制**距离。独立于此流条件，diam(M,g_lambda) 趋于零，故 GH 极限是点。不声称一般速率或固定非
  恒定赋值收敛。带单侧 coarea 密度 I(c)=I_+ + O(c) 与 I(c)=I_- + O(|c|)，面积等于
  pi(I_++I_-)/(2 mu lambda)+O(lambda^{-2} log lambda)。
- **假设：** 直径证明用连通性与紧性；有界赋值范围非等价替代。梯度访问与单侧密度正则性是分开
  条件。正则微分不使边界零成为全局曲线。旧系数只在两侧密度等于 mu 倍内在零曲线长时恢复。限制到
  环境族非紧正则轨迹不自动继承紧坍缩定理。
- **证明位置：** `paper-3/sections/04-parameter-discriminants.tex`、`rem:intensity-plane-not-a-base`、
  `prop:intensity-collapse`、`ex:intensity-cylinder-shortcut`、`ex:intensity-boundary-controls`、
  `rem:intensity-collapse-hypotheses`。直径证明用有限内部网、横截路径与支配收敛，非内在零长度。
- **执行验证：** `paper-3/scripts/verify-intensity-collapse.py` 21 个显式符号/几何检查，普通与
  优化 Python 输出相同。规范 Paper III 构建与最终源审查记录于
  `paper-III-intensity-revision-2026-11-09.md`。
- **受影响下游节点：** S-0010 的 P3-L11/P3-L12 描述与强度讨论注。审计源中无其他定理依赖这些
  节点。依赖图现记录其修正箭头。
- **受影响论文：** 仅 Paper III。无 Paper 0 论断被提升或修改。
- **审查者：** 起草 AI 加单独 AI 数学审查；非独立人工审查且不断言作者验收或发布授权。
- **日期：** 2026-11-09。

---

# 第十五部分. 显式拒绝登记

## 46. 被拒表述

以下表述无论出现在哪必须移除或重写。

### R1

> 每个算术表达式有唯一求值历史。

```text
UNSUPPORTED AND FALSE IN GENERAL
```

只有顺序树有唯一合法内部求值顺序。

---

### R2

> Threadlike 指每个左子是叶。

```text
REJECTED AS CURRENT CANONICAL DEFINITION
```

措辞与示例冲突或依赖树定向。

用内在顺序树与标记脊柱定义替换。

---

### R3

> 现有 AEG 是算术表达式完整几何。

```text
REJECTED
```

现有连续 AEG 是双边射影语义的仿射/Borel 扇区。

---

### R4

> 射影延拓解决普通算术除零。

```text
REJECTED
```

它改变语义范畴且必须保留域标签。

---

### R5

> 接触形式唯一强制算术全纯性。

```text
REJECTED
```

水平度量、定向与相容复结构是附加选择。

---

### R6

> (\delta) 是普通幂零微分。

```text
REJECTED
```

标量场上：

[
\delta_H^2F
===========

\mu\lambda(\partial_aF),du\wedge dv.
\]

---

### R7

> 光滑非退化 AES 可有孤立正则零。

```text
REJECTED
```

当 (\mu\neq0) 时矛盾正则零定理。

---

### R8

> 每个光滑总零集是全局平凡管。

```text
REJECTED
```

需 properness 或等价假设。

---

### R9

> 带线管定义纽结不变量。

```text
REJECTED AS AN ESTABLISHED CLAIM
```

不变性与归一化仍开放。

---

### R10

> 非交换性蕴含双曲几何与指数复杂度。

```text
REJECTED
```

每个蕴含需独立假设与证明。

---

# 第十六部分. Paper I 完成门禁

## 47. 门 A — 基础语法

Paper I 只有以下条件才可标语法支完成：

* [ ] C0 与 C1 固定；
* [ ] T1 集成并检查；
* [ ] 标记历史对应证明；
* [ ] 镜像与反演分离；
* [ ] 旧 threadlike 定义移除或显式取代。

---

## 48. 门 B — 射影与仿射语义

只有以下条件完成：

* [ ] 初等矩阵域审计；
* [ ] T2 最终复合约定下检查；
* [ ] P3 与 P4 精确陈述；
* [ ] 普通与射影语义分离；
* [ ] Paper I 主要理论无残留双赋值语义。

---

## 49. 门 C — 仿射余循环与流

只有以下条件完成：

* [ ] T3 与 T4 用最终约定；
* [ ] 相对仿射缺陷与端点相等区分；
* [ ] T5 有一个主要推导；
* [ ] 流参数与累积坐标不重载；
* [ ] 度量 eikonal 依赖显式。

---

## 50. 门 D — 双曲模型

只有以下条件完成：

* [ ] E1 固定；
* [ ] E2 推导；
* [ ] T6 最终归一化下证明；
* [ ] 曲率与 Laplacian 公式检查；
* [ ] 模型编号稳定；
* [ ] 无残留无证明唯一性声称。

---

## 51. 门 E — 零几何

只有以下条件完成：

* [ ] T7 证明；
* [ ] 边界限定显式；
* [ ] Z3 定义；
* [ ] 孤立零模型重新分类；
* [ ] T8 不过度陈述为全局管平凡；
* [ ] 多重零示例验证或移除。

---

## 52. 门 F — ACS 与 torsion

只有以下条件完成：

* [ ] T9 最终符号约定下推导；
* [ ] T10 假设显式；
* [ ] T12 符号与定向一致；
* [ ] 所有示例重算；
* [ ] 无残留商理论。

---

## 53. 门 G — 接触

只有以下条件完成：

* [ ] T15 证明；
* [ ] K3 重算；
* [ ] T16 限制陈述；
* [ ] T17 三层无混淆陈述；
* [ ] 解析材料移到 Paper II。

---

# 第十七部分. 最终状态摘要

## 54. 支配原则

数学状态登记以以下方式支配重组：

[
\boxed{
\text{no claim is promoted by editing}
\quad+\quad
\text{no theorem is used before its proof}
\quad+\quad
\text{no hypothesis is silently dropped}.
}
]

已证明定理与结构性、推测或开放材料之间的边界必须保持在行文可见。
