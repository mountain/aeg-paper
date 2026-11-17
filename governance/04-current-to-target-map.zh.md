# 当前到目标材料映射

**文件：** `governance/04-current-to-target-map.md`
**状态：** 权威
**版本：** 1.0
**日期：** 2026-08-06
**依赖：**

* `AGENTS.md`
* `governance/00-authoritative-scope.md`
* `governance/01-paper-series-architecture.md`
* `governance/02-paper-I-outline.md`
* `governance/03-theorem-dependency-graph.md`

**适用于：** `aeg-paper` 仓库所有现有材料的迁移与重组。

**当前状态说明（2026-08-07）：** 本映射所述迁移已执行。下文「current path」「target」
「transitional」等历史短语指固定迁移基线，非当前工作树。当前布局与活跃源闭包记录于
`README.md`、`governance/README.md` 与 `governance/source-inventory.md`；已完成路径变更记录于
`governance/migration-log.md` 迁移 M-0010–M-0017。

**更新（2026-09-22，M-0019）：** 第二次迁移在 `00b-paper-0-geometric-foundation-amendment.md`
下把 Paper I 几何章节重新分配给 Paper 0。其文件级状态记录于下表；Paper 0 目的地是
`paper-0/sections/03-aes-and-motion.tex`（从 Paper I §§5–6）、
`paper-0/sections/07-affine-cocycles.tex`（从 §4）、
`paper-0/sections/08-acs-tearing.tex`（从 §8）、
`paper-0/sections/09-contact-of-tearing.tex`（从 §9），以及 Paper 0 附录 B、C、D（从 Paper I
附录 C、B、D）。

| 来源（Paper I，M-0019 前） | 迁移状态 | 论断处理 | 目的地 |
|---|---|---|---|
| `sections/04-affine-cocycles.tex` | `MOVE` | `PRESERVE` | `paper-0/sections/07-affine-cocycles.tex` |
| `sections/05-affine-flow.tex` | `MOVE` | `PRESERVE` | `paper-0/sections/03-aes-and-motion.tex` |
| `sections/06-hyperbolic-model.tex` | `MOVE` | `PRESERVE` | `paper-0/sections/03-aes-and-motion.tex` |
| `sections/08-acs-torsion.tex` | `MOVE` | `PRESERVE` | `paper-0/sections/08-acs-tearing.tex` |
| `sections/09-contact-curvature.tex` | `MOVE` | `PRESERVE` | `paper-0/sections/09-contact-of-tearing.tex` |
| `appendices/app-A`（仿射群小节） | `SPLIT` | `PRESERVE` | `paper-0/appendices/app-C-affine-cocycles.tex` |
| `appendices/app-B-affine-cocycles.tex` | `MOVE` | `PRESERVE` | `paper-0/appendices/app-C-affine-cocycles.tex` |
| `appendices/app-C-hyperbolic-calculations.tex` | `MOVE` | `PRESERVE` | `paper-0/appendices/app-B-hyperbolic-calculations.tex` |
| `appendices/app-D-acs-contact.tex` | `MOVE` | `PRESERVE` | `paper-0/appendices/app-D-acs-contact.tex` |
| `sections/02-sequential-histories.tex` | `KEEP` | `PRESERVE` | 不变 |
| `sections/03-projective-affine.tex` | `KEEP` | `PRESERVE` | 不变 |
| `sections/07-zero-geometry.tex` | `KEEP` | `PRESERVE` | 重编号 `05-zero-geometry.tex` |
| `sections/00`、`01`、`10` | `REWRITE` | `PRESERVE` | 接口、引言、结论 |
| `appendices/app-E` | `KEEP` | `PRESERVE` | 重编号 `app-B-equality-neutrality.tex` |
| Paper 0 `02-two-combs`、`03-paths`、`04-ripple-pencils`、`07-interface` | `REWRITE` | `PRESERVE` | `02-expansion`、`03-aes-and-motion`、`04-ripple-geometry`、`12-interface` |

---

## 1. 目的

本文档把现有仓库材料分配给四论文 AEG 系列中其目标位置。

它指定每个当前来源：

* 其规范目的地；
* 是否保留、拆分、重写、迁移或归档；
* 哪些数学论断可保留；
* 哪些论断需削弱、验证或移除；
* 它支持哪些目标定理节点；
* 哪些下游论文拥有详细发展。

本文档防止三种失败模式：

1. 有价值研究材料被静默删除；
2. 被取代表述留在主论文；
3. 同理论在多篇论文不一致发展。

---

# 第一部分. 迁移词汇

## 2. 迁移状态

每个实质来源块必须恰收一个主迁移状态。

### `KEEP`

仅局部编辑保留在当前论文。

用当：

* 数学角色不变；
* 结果属目标论文；
* 假设或含义无需实质改变。

---

### `REWRITE`

保留数学主题但重写其定义、定理陈述、证明或叙事。

用当：

* 当前表述含糊；
* 结果属目标论文；
* 其角色或假设必须实质改变。

---

### `SPLIT`

把来源分割到两个或更多目标位置。

用当当前节含：

* 基础与后续论文材料；
* 定理与推测展望；
* 局部计算与独立理论。

每个分割必须为每个分量识别一个规范目的地。

---

### `MOVE`

把材料迁到另一论文而不在 Paper I 保留完整副本。

Paper I 可保留：

* 短摘要；
* 作语境所需的定理陈述；
* 前向引用。

---

### `APPENDIX`

把技术细节、长计算或次要示例移到同论文附录。

---

### `ARCHIVE`

把来源保留为研究历史但从活跃论文草稿移除。

用于：

* 被取代表述；
* 废弃术语；
* 探索性对话；
* 错误或不完整但仍对溯源有用的方法。

---

### `REMOVE`

仅当内容可证明为以下时才删除：

* 别处重复且无额外溯源价值；
* 机械生成噪声；
* 错误且作归档也无用；
* 不应版本化的构建产物。

实质数学材料不得无归档记录移除。

---

### `HOLD`

审计解决其状态前不迁移。

用当：

* 目标论文不清；
* 数学正确性不确定；
* 来源被引用但未定位；
* 存在两个不相容版本。

---

## 3. 论断处理状态

迁移状态与数学论断状态是不同。

每个迁移论断还必须赋以下之一：

* `PRESERVE`；
* `REPROVE`；
* `WEAKEN`；
* `CONDITIONALIZE`；
* `RECLASSIFY`；
* `OPEN`；
* `REJECT`。

示例：

```text
Migration: MOVE to Paper III
Claim treatment: OPEN
```

```text
Migration: REWRITE in Paper I
Claim treatment: REPROVE
```

权威论断状态维护于：

```text
governance/05-mathematical-status.md
```

---

# 第二部分. 已实现仓库结构

## 4. 当前顶层结构

已实现组织是：

```text
aeg-paper/
├── AGENTS.md
├── README.md
├── LICENSE
├── build.sh
├── Dockerfile
├── bibliography/
│   └── aeg-paper.bib
│
├── paper-1/
│   ├── aeg-paper-1.tex
│   ├── sections/
│   └── appendices/
│
├── paper-2/
│   ├── README.md
│   ├── aeg-paper-2.tex
│   ├── sections/
│   └── appendices/
│
├── paper-3/
│   ├── README.md
│   ├── aeg-paper-3.tex
│   ├── sections/
│   ├── appendices/
│   └── computations/
│
├── paper-4/
│   ├── README.md
│   ├── aeg-paper-4.tex
│   ├── sections/
│   ├── appendices/
│   └── scripts/
│
├── notes/
├── images/
│   └── sources/
├── governance/
│   └── discussions/
└── archive/
```

共享参考文献是 `bibliography/aeg-paper.bib`；历史样式归档于
`archive/legacy-latex-styles/`。研究笔记按主题分类于 `notes/` 且在全部规范 TeX 依赖闭包之外。

---

## 5. 历史过渡结构

重组期间，仓库临时保留：

```text
aeg-paper.tex
sections/
notes/
images/
```

作活跃遗留路径。它们不再是活跃路径：旧根手稿在 `archive/legacy-root-manuscript/`，其旧
`sections/` 树随之移动。

那时：

* `paper-1/aeg-paper-1.tex` 成为 Paper I 入口；
* 规范 Paper I 节移到 `paper-1/sections/` 与 `paper-1/appendices/`；
* 迁移材料分配给 `paper-2/`、`paper-3/` 与 `paper-4/`；
* 旧源保留到新目的地构建且审查。

源不得仅因目标目录已创建即被删除。

---

# 第三部分. 根级文件

## 6. `README.md`

### 当前角色

当前 README 把 AEG 主要呈现为以下之间联系：

* 算术表达式；
* 双曲几何；
* 流方程；
* 算术 torsion；
* 基本表达式空间。

它可能用较早 (\mathfrak E_0/\mathfrak E_1) 命名方案且尚未反映双边完备化或四论文架构。

### 迁移状态

```text
REWRITE
```

### 目标角色

根 README 应描述：

* 仓库作为 AEG 论文系列来源；
* Paper I 作为活跃基础手稿；
* Papers II–IV 作为结构化研究草稿；
* 构建命令；
* 权威重组文档；
* 活跃论文与探索性笔记的区分。

### 所需变更

* 移除或更新任何不一致模型编号；
* 避免把当前仿射理论描述为完整 AEG 理论；
* 加四论文系列图；
* 链接到 `governance/00-authoritative-scope.md`；
* 仅当 DOI 信息仍关联正确发布版本时保留；
* 区分发布或归档版本与当前重组分支。

### 论断处理

```text
WEAKEN and UPDATE
```

README 不得声称所有算术表达式已嵌入发展几何。

---

## 7. `paper-1/aeg-paper-1.tex`

### 当前角色

主 Paper I 入口，含：

* 标题与作者；
* 摘要；
* 定理环境；
* 节序；
* 附录；
* 参考文献。

### 迁移状态

```text
REWRITE, then MOVE to `paper-1/aeg-paper-1.tex`
```

### 目标角色

它必须实现以下中的章序：

```text
governance/02-paper-I-outline.md
```

### 所需结构变更

用以下替换当前节序：

```text
1. Introduction
2. Sequential Arithmetic Histories
3. Projective Semantics and the Affine Sector
4. Affine Cocycles and Relative Defects
5. Continuous Arithmetic Flow
6. The Basic Hyperbolic Expression Space
7. Zero Loci and Singular Expression Spaces
8. Global Torsion and the ACS
9. Contact Connection and Horizontal Curvature
10. Conclusions and Research Interfaces
```

### 所需元数据修复

* 验证作者单位；
* 验证标题与副标题；
* 更新关键词；
* 修复 `example` 定理标题；
* 移除重复包导入；
* 归一化定理环境；
* 所有定理迁移后更新摘要；
* 需要时更新目录深度。

### 论断处理

```text
REWRITE and REAUDIT
```

当前摘要不得无修订保留。

---

## 8. `aeg-lemma.tex`

### 当前角色

遗留或补充定理源。

### 迁移状态

```text
HOLD pending audit
```

### 所需审计

确定：

* 当前是否被构建包含；
* 哪些引理仍唯一；
* 任何结果是否重复当前节证明；
* 其记号是否早于当前 (\mathfrak E_0/\mathfrak E_1) 方案。

### 可能目的地

* Paper I 附录；
* `notes/archive/`；
* 共享技术笔记；
* 若完全重复且机械过时则移除。

无定理可保持经未使用遗留文件隐式被依赖。

---

## 9. `bibliography/aeg-paper.bib`

### 迁移状态

```text
KEEP and CLEAN
```

### 目标角色

初始保持共享参考文献。

### 所需工作

* 识别未使用条目；
* 识别仅后续论文使用的引用；
* 迁移论文有其参考文献前不删条目；
* 为以下加主要引用：

  * 射影变换；
  * 仿射群；
  * 正则值定理；
  * 若引用的 Ehresmann 型真淹没定理；
  * 接触几何；
  * 双曲几何。

### 禁止

不用参考文献清理作机会无相关性地拓宽文献综述。

---

## 10. `build.sh`

### 迁移状态

```text
KEEP, then EXTEND
```

### 所需行为

过渡期间必须继续构建 Paper I。

后可支持：

```bash
./build.sh
```

### 验证

当前基线构建结果记录于以下前不改脚本：

```text
governance/audit-report.md
```

---

## 11. `Dockerfile`

### 迁移状态

```text
KEEP and VERIFY
```

### 所需审计

* 确认它构建当前 PDF；
* 确认重组后路径仍有效；
* 验证图与参考文献依赖；
* 避免加无关包。

---

# 第四部分. 当前 Paper I 节

## 12. `sections/sec01.tex`

### 当前内容

* 求值历史而非端点值；
* 引导问题；
* 历史定位；
* threadlike 表达式；
* 算术 torsion；
* 流方程；
* AES；
* ACS；
* 接触结构；
* (\delta)-演算；
* 算术全纯性；
* 贡献清单；
* 论文组织。

### 迁移状态

```text
REWRITE
```

### 目标目的地

| 当前分量 | 目标 |
| ---------------------------------------- | ----------------------------- |
| 端点值对求值历史 | Paper I，第 1 章 |
| 历史定位 | Paper I，第 1 章，缩短 |
| Threadlike 表达式引入 | Paper I，第 2 章，替换 |
| Torsion 动机 | Paper I，第 1 与 4 章 |
| 流概览 | Paper I，第 5 章 |
| AES 概览 | Paper I，第 6–7 章 |
| ACS 概览 | Paper I，第 8 章 |
| 接触概览 | Paper I，第 9 章 |
| 算术全纯性概览 | MOVE 到 Paper II |
| 当前贡献清单 | 替换 |
| 当前结构段 | 替换 |

### 所需变更

* 引入双边/射影定位；
* 用标记脊柱历史替换「threadlike expression」；
* 移除论文建立函数论开端作为主要贡献的声称；
* 加正则/奇异零边界；
* 区分精确有限 torsion 与无穷小曲率；
* 加到 Papers II–IV 的显式范围接口。

### 论断处理

```text
PRESERVE core motivation
REWRITE architecture
MOVE analytic claims
```

---

## 13. `sections/sec02-00.tex`

### 当前内容

* 算术表达式文法；
* 求值；
* 求值顺序；
* 树示例；
* threadlike 表达式定义；
* currying；
* 路径记号；
* 网格；
* 把历史编码为路径；
* 规范路径示例。

### 迁移状态

```text
SPLIT and REWRITE
```

### 目标映射

#### Paper I，第 2 章

保留并重写：

* 表达式树；
* 普通求值；
* 合法求值顺序；
* 分支对顺序树示例；
* 路径复合；
* 有界与自由历史。

替换：

* 当前 threadlike 定义；
* 含糊左/右术语；
* 任何无证明唯一求值顺序从当前子条件得出的陈述。

添加：

* 依赖偏序；
* 顺序树分类；
* 标记种子；
* 槽-(1)/槽-(2) 语境；
* 手性词。

#### Paper I，第 6 章

移动或保留选定几何示例：

* 算术网格；
* 在 (\mathfrak E_0) 中绘表达式路径；
* 规范对说明。

这些示例应只在双曲模型构造后出现。

#### 附录 E

移动区分示例：

* 同端点；
* 不同历史；
* 不同规范重排。

### 需谨慎材料

当前路径示例可能混合：

* 语法；
* 代数重写；
* 几何路径；
* 语义相等。

每个示例必须按相等层重新标注。

### 论断处理

```text
REWRITE definitions
PRESERVE elementary examples after reclassification
```

---

## 14. `sections/sec02-01.tex`

### 当前内容

* 交替历史；
* 累积乘法参数；
* 扰动传播；
* 算术 torsion；
* 仿射群表示；
* 相等层级；
* 早期中性讨论。

### 迁移状态

```text
SPLIT
```

### 目标映射

#### Paper I，第 4 章

移动并重写：

* 交替仿射历史；
* 累积尺度；
* 精确求值公式；
* 扰动传播；
* 仿射矩阵表示；
* 初等 torsion。

围绕以下重组：

[
f_i(x)=s_ix+t_i,
\qquad
\Phi_n,\xi_n,\widehat\xi_n.
]

交替公式成为一般仿射余循环特殊情形。

#### Paper I，第 2 章

移动：

* 相等层级；
* 路径/算子/值区分。

#### 附录 B

移动：

* 扩展索引记号；
* 详细扰动递推；
* 特殊交替示例。

#### 附录 E 或未来关系理论

移动：

* 中性分类；
* 闭词讨论。

#### Paper IV

移动完整讨论：

* 自由群影子；
* 关系商；
* 凝聚推论。

### 所需变更

* 不单独由路径反演定义 torsion；
* 区分共同尺度与共同总 charge；
* 陈述年代复合约定；
* 避免混淆符号自由历史与其求值仿射群。

### 论断处理

```text
PRESERVE affine formulas after rederivation
GENERALIZE torsion
MOVE relation theory
```

---

## 15. `sections/sec03.tex`

### 当前内容

* 流方程推导；
* 仿射矩阵 Lie 代数；
* 离散生成方向；
* 等高梯度形式；
* 矫正坐标；
* 算术坐标；
* 局部面积公式；
* 无坐标 eikonal 形式；
* 度量矫正。

### 迁移状态

```text
SPLIT and REWRITE
```

### 目标映射

#### Paper I，第 5 章

保留：

* 仿射 Lie 代数推导；
* 连续流方程；
* Pfaffian 形式；
* 方向解；
* 加法与乘法轴；
* eikonal 形式；
* 局部 torsion 渐近。

Lie 论推导应成为主要。

#### Paper I，第 4 章

移动：

* 仿射矩阵演化；
* 扭曲平移律；
* 与仿射余循环关系。

#### 附录 C

移动：

* 长等高角推导；
* 矫正坐标详细积分；
* 后续定理未用坐标变换。

#### Paper II

仅按引用移动或复制：

* 矫正坐标解析使用；
* 二阶或算子解释。

### 所需变更

* 显式陈述左/右乘法约定；
* 区分精确公式与展开；
* 指定度量前不称 eikonal 方程无坐标；
* 区分 (\mu,\lambda) 假设；
* 加 Riccati 完备化注。

### 论断处理

```text
REPROVE under fixed conventions
```

---

## 16. `sections/sec04.tex`

### 当前内容

* 归一化上半平面模型；
* 一般 ((\mu,\lambda))-模型；
* 流验证；
* Laplace 特征函数；
* horocyclic 坐标；
* 网格作用；
* Baumslag–Solitar 关系；
* torsion 与面积；
* 孤立零 (\mathfrak E_1)；
* 早期参数族/管注。

### 迁移状态

```text
SPLIT and REWRITE
```

### 目标映射

#### Paper I，第 6 章

保留并加强：

* 上半平面模型；
* 度量；
* 赋值 (a=-x/y)；
* 梯度验证；
* horocyclic 几何；
* 网格作用；
* 可选 Baumslag–Solitar 关系；
* 可选 Laplace 特征函数；
* 局部 torsion 面积示例。

添加：

* 从仿射群与不变度量推导；
* 显式曲率归一化；
* (\mathfrak E_0) 清楚定义。

#### Paper I，第 7 章

移动并重新分类：

* 孤立中心模型；
* 正则对奇异零比较。

孤立中心必须按实际模型描述为奇异零或排除点。

#### Paper III

移动：

* 一般参数族管推测；
* 更高 (E_k) 与零轨迹计划；
* 拓扑改变预期。

### 所需修正

* 通篇验证 (\mathfrak E_0/\mathfrak E_1) 命名；
* 检查 Baumslag–Solitar 作用顺序；
* 对实际归一化度量计算 Laplacian；
* 避免唯一性声称；
* 避免称孤立零正则。

### 论断处理

```text
PRESERVE basic model
REPROVE normalization-dependent formulas
RECLASSIFY isolated zero
MOVE tube program
```

---

## 17. `sections/sec05.tex`

### 当前内容

* ACS 定义；
* 路径与反路径；
* 用未来乘法 charge 的求值公式；
* 全局 torsion；
* 四步示例；
* 三重恒等式；
* 交换化解释。

### 迁移状态

```text
REWRITE
```

### 目标目的地

Paper I，第 8 章。

### 所需重组

用相容历史一般比较：

[
\gamma,\delta.
]

替换特权比较：

[
\gamma\quad\text{versus}\quad\bar\gamma
]

区分：

* 尺度相容：
  [
  M_\gamma=M_\delta;
  ]
* charge 相容：
  [
  (A_\gamma,M_\gamma)=(A_\delta,M_\delta).
  ]

从仿射余循环推导求值：

[
\nu_x(\gamma)
=============

e^{M_\gamma}
\left(
x+\int_{C_\gamma}e^{-M},dA
\right).
]

然后推导：

* 相对端点独立；
* 围线公式；
* 加权 Stokes 公式。

### 保留为示例材料

* 当前四步示例；
* 路径对反演作特殊情形；
* 单调正 charge 区域。

### 移到 Paper IV 材料

* 完整商解释；
* 凝聚；
* 过程结果信息损失；
* 群胚级含义。

### 所需修正

* 固定定向与符号约定；
* 带符号或自交路径用 (2)-链；
* 不称每对路径为简单封闭区域；
* 避免等同符号历史群与其求值仿射群。

### 论断处理

```text
GENERALIZE and REPROVE
```

---

## 18. `sections/sec06.tex`

### 当前内容

* 接触形式；
* 非退化；
* Darboux 坐标；
* Reeb 场；
* 水平提升；
* Legendrian 流；
* 曲率括号；
* 有限交换子；
* 闭环 holonomy；
* 边界积分；
* Lie 代数注。

### 迁移状态

```text
KEEP core, REWRITE organization
```

### 目标目的地

Paper I，第 9 章与附录 D。

### 正文内容

保留：

* 接触形式；
* 接触非退化；
* 水平分布；
* 水平提升；
* 仿射流 Legendrian 实现；
* 曲率括号；
* 简明有限缺陷比较。

### 附录 D 内容

移动：

* 详细 Darboux 坐标转换；
* Reeb 场计算，除非后续用；
* 长有限交换子计算；
* 详细 Stokes 曲面计算；
* 可解 Lie 代数分解。

### 所需变更

* 称结构为接触联络或算术接触模型而不暗示新接触同构类；
* 区分：

  * 开双路径缺陷；
  * 闭交换子 holonomy；
  * 无穷小曲率；
* 确保符号匹配第 8 章；
* 不用接触几何声称规范复结构。

### 论断处理

```text
PRESERVE and CLARIFY
```

---

## 19. `sections/sec07.tex`

### 当前内容

* (\delta) 定义；
* 等价水平公式；
* 链规则；
* 初等示例；
* 曲率包；
* 联络视角；
* 自然单位；
* affine–Appell 基；
* 反微分。

### 迁移状态

```text
SPLIT
```

### 目标映射

#### Paper I，第 9 章

仅保留：

* 水平协变微分；
* 公式：
  [
  \delta_HF=dF-(\partial_aF)\alpha;
  ]
* 水平导数；
* 曲率：
  [
  \delta_H^2F
  ===========

  \mu\lambda(\partial_aF),du\wedge dv;
  ]
* 联络解释。

#### 附录 D

移动：

* 选定坐标检查；
* 验证所需初等链规则示例。

#### Paper II

移动：

* 大量微分表；
* affine–Appell 基；
* 算子稳定函数类；
* 反微分；
* 自然单位解析使用。

### 所需术语变更

优选：

```text
horizontal covariant differential
```

或：

```text
horizontal differential
```

超过无限定「differential calculus」。

若保留记号 (\delta)，显式陈述它一般不幂零。

### 论断处理

```text
PRESERVE curvature core
MOVE analytic machinery
```

---

## 20. `sections/sec08.tex`

### 当前内容

* 算术 Cauchy–Riemann 方程；
* (\partial_{\mathrm{AEG}}) 与 (\bar\partial_{\mathrm{AEG}})；
* 水平共形性；
* 算术全纯坐标；
* 复合；
* 刚性；
* 因式分解；
* 扭曲调和性；
* affine–Appell 基。

### 迁移状态

```text
MOVE to Paper II
```

### 目标目的地

建议：

```text
paper-2/sections/
├── 01-analytic-data.tex
├── 02-horizontal-operators.tex
├── 05-arithmetic-holomorphicity.tex
└── 06-explicit-families.tex
```

### Paper I 保留

Paper I 可保留一个结尾注：

> A compatible horizontal metric and almost-complex structure support Cauchy–Riemann-type operators, developed in Paper II.

当前 `sec08.tex` 无完整定理应留 Paper I。

### 复用前所需修正

* 修复算术坐标中 `u` 对 `\nu`；
* 显式定义所选水平度量与复结构；
* 验证因式分解符号；
* 定义解析域与函数空间；
* 区分形式算子恒等式与泛函分析结果。

### 论断处理

```text
RECLASSIFY as Paper II prototype
REPROVE after analytic data are fixed
```

---

## 21. `sections/sec09.tex`

### 当前内容

* 当前论文摘要；
* 路径到关系展望；
* 中性类；
* 解析未来；
* 奇异背景；
* 更高结构；
* 未来研究目标。

### 迁移状态

```text
REWRITE and SPLIT
```

### 目标映射

#### Paper I，第 10 章

仅保留：

* 已证明基础摘要；
* 到 Paper II 接口；
* 到 Paper III 接口；
* 到 Paper IV 接口；
* 简明开放基础问题。

#### Paper II

移动：

* 解析计划；
* 核；
* 边值；
* 显式解析族。

#### Paper III

移动：

* 奇异背景；
* 更高零结构；
* 管；
* 拓扑与单值。

#### Paper IV 或未来关系论文

移动：

* 完整环与中性理论；
* 关系论凝聚。

### 所需变更

用以下替换结束于算术全纯性的当前链：

[
\text{history}
\to
\text{projective placement}
\to
\text{affine flow}
\to
\text{torsion/contact curvature}.
]

### 论断处理

```text
REWRITE
```

---

## 22. `sections/sec10.tex`

### 当前角色

补充模型与 ACS 计算。

### 迁移状态

```text
SPLIT and APPENDIX
```

### 目标映射

* 双曲模型计算 → 附录 C；
* ACS 计算 → 附录 D 或第 8 章示例；
* 过时命名或重复计算 → 比较后归档。

### 审计要求

* 检查所有参数归一化；
* 对照新 ACS 约定检查符号；
* 识别后续论文所用公式。

---

## 23. `sections/sec11.tex`

### 当前角色

补充接触、(\delta) 与全纯计算。

### 迁移状态

```text
SPLIT
```

### 目标映射

* 接触计算 → Paper I，附录 D；
* 水平微分曲率 → Paper I，附录 D；
* 全纯计算 → Paper II；
* 扩展解析示例 → Paper II 笔记或附录。

### 禁止

不留 Paper II 解析结果藏于 Paper I 附录。

---

## 24. `sections/sec12.tex`

### 当前角色

涉及相等层级与中性的示例。

### 迁移状态

```text
APPENDIX and SPLIT
```

### 目标映射

#### Paper I，附录 E

保留区分所需示例：

* 同端点对同算子；
* 同 charge 对同历史；
* 零端点缺陷对平凡历史。

#### 未来关系理论或 Paper IV

移动主要目的是：

* 闭词分类；
* 规范商；
* 凝聚；
* 超出 Paper I 需要的中性层级。

的示例。

### 论断处理

```text
PRESERVE examples after reclassification
```

---

# 第五部分. 双边与射影笔记

## 25. `notes/projective-condensation/01-bilateral-projective-condensation.tex`

### 当前内容

* 标记脊柱历史；
* 顺序树定理；
* 镜像对反演；
* 双边递归；
* 射影语义；
* (PGL_2) 生成；
* 仿射/Borel 扇区；
* Bruhat 定位；
* 商前历史；
* 相对射影缺陷；
* 仿射 Maurer–Cartan 公式；
* Riccati 流；
* 双赋值；
* 秩一投影子；
* 商塔；
* 过程结果丛；
* 有限域模型；
* 联络与 holonomy 提案。

### 迁移状态

```text
SPLIT
```

### Paper I 目的地

#### 第 2 章

移动并归一化：

* 标记脊柱历史定义；
* 顺序树分类；
* 标记种子解释；
* 镜像对时间反演；
* 结合律作 (2)-胞腔注，仅当简明。

#### 第 3 章

移动：

* 射影语境表；
* 射影求值；
* (PGL_2) 生成定理；
* 仿射/Borel 推论；
* 正实限定；
* 短 Bruhat 注；
* Riccati 定位。

#### 第 4 章

移动：

* 仿射未来/过去余循环公式；
* 左/右 Maurer–Cartan 公式；
* 仿射相对缺陷。

### Paper IV 目的地

移动：

* 历史群胚；
* 求值函子；
* 群值射影缺陷；
* 双赋值；
* 点–谓词对偶；
* 秩一投影子定理；
* 商塔；
* 主 (H)-丛；
* 过程结果残差；
* 有限域计数；
* 射影凝聚；
* holonomy 提案。

### 归档或开放问题目的地

* telescoping 阻碍；
* 不完整语境传输 ansatz；
* 尚未形式化的语义概念/谓词解释。

### 所需预防

* Paper I 不得继承推测语义断言；
* 射影延拓必须保留普通域警告；
* PGL 定理必须检查所有声称特征；
* 操作数槽手性不得与对偶传输等同；
* `PGL_2` 记号与矩阵作用约定必须统一。

### 论断处理

```text
PRESERVE proved algebraic core
MOVE full quotient theory to Paper IV
OPEN geometric bridges
```

---

# 第六部分. 解析笔记

## 26. 当前解析与 (\delta)-演算笔记

此类别含主要内容涉及：

* 算术全纯性；
* 扭曲调和性；
* 水平算子；
* affine–Appell 基；
* 双曲实函数论；
* 核与边界问题。

的笔记。

### 迁移状态

```text
MOVE to Paper II
```

### 目标组织

```text
paper-2/
├── README.md
├── aeg-paper-2.tex
├── sections/
│   ├── 01-analytic-data.tex
│   ├── 02-horizontal-operators.tex
│   ├── 03-hyperbolic-real-analysis.tex
│   ├── 04-boundary-problems.tex
│   ├── 05-arithmetic-holomorphicity.tex
│   └── 06-explicit-families.tex
└── notes/
```

### Paper I 保留

仅基础算子恒等式留 Paper I。

### 审计规则

每个解析笔记必须检查是否假设：

* 水平度量；
* 度量；
* 复结构；
* 算子域；
* 完备性；
* 边界正则性。

定理状态赋前必须加未陈述假设。

---

# 第七部分. 多重零、奇异与管笔记

## 27. 多重零构造笔记

此类别含：

* (E_k)；
* (E_{\log})；
* 多重零线；
* 共形唯一性；
* 零线分类；
* 解析构造。

的笔记。

### 迁移状态

```text
MOVE to Paper III, with one possible minimal example retained in Paper I
```

### Paper I 资格测试

多重零模型仅当以下全部完整才可留 Paper I：

```text
[ ] domain
[ ] metric
[ ] assignment function
[ ] singular set
[ ] flow verification
[ ] zero topology
```

否则完全移到 Paper III。

### Paper III 目标组织

```text
paper-3/sections/
├── 01-singular-aes.tex
├── 02-local-zero-models.tex
├── 03-multi-zero-constructions.tex
├── 04-parameter-discriminants.tex
├── 05-regular-tubes.tex
├── 06-singular-fibers.tex
├── 07-monodromy-and-braids.tex
└── 08-threading-and-knot-questions.tex
```

### 论断处理

* 存在公式 → `REPROVE`；
* 唯一性声称 → `HOLD` 除非证明；
* 视觉零计数 → `COMPUTATIONAL EXAMPLE` 直到解析验证；
* 一般 (E_k) 分类 → `OPEN` 除非完成。

---

## 28. 管笔记

此类别含：

* 参数化零集；
* 管构造；
* 穿线；
* 零线传输；
* 拓扑改变；
* 类纽结图。

### 迁移状态

```text
MOVE to Paper III
```

### Paper I 保留

仅一般构造：

[
\mathcal Z
==========

{(p,t):a_t(p)=0}
]

与正则值引理可留。

### 所需重新分类

区分：

1. 总零集；
2. 光滑零曲面；
3. 局部平凡管；
4. 嵌入管；
5. 穿线管；
6. 辫闭包；
7. 纽结不变量。

这些非同义。

### 主定理状态前需证明断言

* properness；
* 局部平凡；
* 同痕不变；
* 辫表示；
* Markov 不变；
* 新纽结不变量；
* 独立于 Alexander/Burau 数据。

---

## 29. 纽结相关笔记

已知类别含：

* 纽结构造；
* 管穿线；
* Alexander/Burau 比较；
* Markov 归一化；
* 潜在新不变量。

的笔记。

### 迁移状态

```text
MOVE to Paper III notes; HOLD from main paper
```

### Paper III 正文进入条件

至少其一：

* 同痕不变；
* 辫单值定理；
* Markov 不变；
* 非平凡比较定理；
* 严格定义不变量。

无此，保留为：

* 示例；
* 提案；
* 猜想；
* 开放问题。

---

# 第八部分. 复杂度与资源几何笔记

## 30. `notes/thermodynamics-and-renormalization/02-aeg-flow-and-renormalization-en.tex`

### 当前角色

英文资源几何材料，可能含：

* 计算资源；
* 几何解释；
* 时空关系；
* 石子游戏想法。

### 迁移状态

```text
MOVE to Paper IV
```

### 目标目的地

建议：

```text
paper-4/sections/
├── 06-representation-growth.tex
├── 07-cost-models.tex
└── 08-time-space-relations.tex
```

### 论断处理

所有连接几何与复杂度的陈述必须按显式成本模型重新分类。

无 Paper I 定理可依赖此笔记。

---

## 31. `notes/thermodynamics-and-renormalization/03-aeg-flow-and-renormalization-zh.tex`

### 迁移状态

```text
MOVE to Paper IV notes or archive as Chinese source
```

### 所需处理

* 与 `notes/thermodynamics-and-renormalization/02-aeg-flow-and-renormalization-en.tex` 比较；
* 识别唯一内容；
* 保留溯源；
* 避免维护两个分歧定理版本。

英文论文源应有一个规范数学表述。

---

## 32. 资源几何与计算时空笔记

此类别含：

* 图灵机；
* 石子游戏；
* 计算时空对偶；
* torsion 与重写曲面；
* de Rham 配对；
* 算法热力学；
* 规范形作计算质量；
* 时空复杂度关系。

的笔记。

### 迁移状态

```text
MOVE to Paper IV
```

### Paper IV 分类

| 主题 | 目标章 |
| ----------------------------- | ------------------------------- |
| 历史与重写图 | 历史范畴 |
| 规范形与商 | 凝聚 |
| 词球增长 | 表示增长 |
| 石子游戏 | 时空成本模型 |
| 计算时空 | 研究综合 |
| 算法热力学 | 动机或条件模型 |
| 计算质量/曲率 | 除非形式化则提案 |

### 禁止迁移到 Paper I

不用这些笔记辩护：

* AES 双曲性；
* 度量唯一性；
* 复杂度下界；
* 物理类比作数学推论。

---

## 33. `notes/projective-condensation/02-projective-geometric-frameworks.tex`

### 当前内容

* (a=-x/y) 射影相容；
* 双曲几何与组合复杂度；
* 紧化；
* 射影边界；
* 射影/双曲相互作用。

### 迁移状态

```text
SPLIT
```

### Paper I 使用

仅保留作概念支持：

* 射影定位；
* 齐次零度赋值；
* 射影边界动机。

Paper I 所用任何断言必须独立重新推导。

### Paper IV 使用

移动：

* 射影紧化；
* 历史到边界解释；
* 商与凝聚联系。

### 论断处理

如：

> combinatorial complexity makes hyperbolicity unavoidable

必须：

```text
REJECT as theorem
RETAIN as research motivation only
```

---

## 34. `notes/projective-condensation/03-canonical-forms-and-condensation.tex`

### 当前内容

* (F_2) 作复杂度来源；
* 规范形；
* 凝聚；
* 空间从时间出现；
* 计算能量与质量；
* 群商示例；
* 交换子 torsion；
* 曲率类比。

### 迁移状态

```text
MOVE to Paper IV and ARCHIVE original
```

### Paper IV 目的地

* 凝聚章；
* 规范形讨论；
* 商空间示例；
* 复杂度度量动机。

### 论断处理

| 论断 | 处理 |
| ------------------------------------------- | ---------------------------------- |
| 关系商作凝聚模型 | 结构提案 |
| (F_2) 作复杂度普遍来源 | 削弱/开放 |
| 复杂度作路径长 | 条件于度量与模型 |
| 计算质量诱导曲率 | 类比/开放 |
| 群增长给算法下界 | 无证明拒绝 |
| 交换子 torsion 公式 | 当前约定下重算 |

### Paper I 使用

无，除可能 ACS 作 charge 影子的短历史注。

---

# 第九部分. 环与关系笔记

## 35. `notes/knots-and-loops/02-zero-taxonomy-and-arithmetic-loops.tex`

### 当前角色

算术环、零分类或中性类。

### 迁移状态

```text
SPLIT and HOLD
```

### Paper I 目的地

仅附录 E 所需极小示例：

* 同端点但非平凡历史；
* 不同中性层级。

### 后续目的地

未来关系论论文或 Paper IV，取决于焦点是：

* 代数环关系；
* 商与凝聚；
* 语义中性。

### 禁止

Paper I 不得发展完整环理论。

---

## 36. 其他 `notes/note_*.tex`

### 迁移状态

```text
HOLD pending semantic audit
```

### 所需审计程序

对每个笔记：

1. 识别其主主题；
2. 识别是否含唯一定理；
3. 分配 Paper I、II、III、IV、未来论文或归档；
4. 分配数学状态；
5. 记录依赖；
6. 记录任何当前正文断言是否隐式引用它。

### 默认路由规则

| 内容 | 目的地 |
| ------------------------- | ------------- |
| 顺序语法 | Paper I |
| 仿射/射影代数 | Paper I 或 IV |
| 双曲模型 | Paper I |
| 函数论 | Paper II |
| 多重零/奇异 | Paper III |
| 管/纽结 | Paper III |
| 凝聚/复杂度 | Paper IV |
| 被取代头脑风暴 | 归档 |

无 `note_*.tex` 文件应批量删除。

---

# 第十部分. 图与资产

## 37. `images/`

### 迁移状态

```text
AUDIT, then KEEP/MOVE/ARCHIVE per figure
```

### 所需图清单

对每个图记录：

* 文件名；
* 源格式；
* 当前图注；
* 当前节；
* 目标论文；
* 数学是否仍有效；
* 是否依赖被取代记号；
* 是否可复现。

### Paper I 图类

保留或重设计：

1. 表达式树；
2. 顺序对分支树；
3. 标记槽-(1)/槽-(2) 历史；
4. 射影对仿射扇区示意；
5. 双曲算术网格；
6. 正则对奇异零集；
7. 双历史 ACS 填充；
8. 接触交换子方形。

### Paper II 图

移动：

* 算子图；
* 解析解族；
* 全纯坐标可视化；
* 边界核。

### Paper III 图

移动：

* 多重零图；
* 管曲面；
* 穿线；
* 纽结与辫图。

### Paper IV 图

移动：

* 商塔；
* 凝聚图；
* 资源图；
* 复杂度增长图。

### 禁止

图不得仅因宣传后续论文理论而留 Paper I。

---

# 第十一部分. 历史与生成材料

## 38. `gpt/`

### 当前角色

生成讨论、会议纪要、提示与探索草稿。

### 迁移状态

```text
ARCHIVE
```

### 目标

```text
governance/archive/generated-discussions/
```

或带归档头原地保留。

### 所需头

每个保留文件应理解为：

```text
STATUS: archival discussion, not authoritative.
```

### 使用政策

材料可挖掘：

* 示例；
* 参考文献线索；
* 遗忘证明想法；
* 溯源。

它不得覆盖权威重组文档。

---

## 39. `../archive/plans/`

### 迁移状态

```text
ARCHIVE or SPLIT
```

### 所需处理

* 活跃重组计划 → `governance/`；
* 历史研究计划 → 归档；
* 未解决研究计划 → 对应 Paper II–IV `README.md`。

---

## 40. 交互 HTML 或实验室文件

示例含资源几何实验室或可视化原型。

### 迁移状态

```text
MOVE to experiments/ or Paper IV supplements
```

### 政策

交互演示非论文证明。

它们可支持：

* 示例；
* 可复现性；
* 计算验证。

其数学断言必须单独重述并证明。

---

# 第十二部分. 要创建的新目标文件

## 41. Paper I 新节文件

推荐创建：

```text
paper-1/sections/
├── 01-introduction.tex
├── 02-sequential-histories.tex
├── 03-projective-affine.tex
├── 04-affine-cocycles.tex
├── 05-affine-flow.tex
├── 06-hyperbolic-model.tex
├── 07-zero-geometry.tex
├── 08-acs-torsion.tex
├── 09-contact-curvature.tex
└── 10-conclusion.tex
```

这些文件应初始与遗留 `sec*.tex` 文件共存。

遗留文件不得删除直到：

* 所有保留内容已映射；
* 新节构建；
* 迁移已记录；
* 人工审查完成。

---

## 42. Paper I 附录

按需创建：

```text
paper-1/appendices/
├── app-A-conventions.tex
├── app-B-affine-cocycles.tex
├── app-C-hyperbolic-calculations.tex
├── app-D-acs-contact.tex
└── app-E-equality-neutrality.tex
```

---

## 43. 后续论文入口文件

创建轻量入口：

```text
paper-2/README.md
paper-3/README.md
paper-4/README.md
```

每个 README 必须含：

* 暂定标题；
* 权威范围引用；
* 导入 Paper I 节点；
* 迁移来源清单；
* 论断状态警告；
* 完成判据。

Papers II–IV 定理集稳定前不创建润色摘要。

---

# 第十三部分. 逐文件迁移表

## 44. 摘要表

| 当前路径 | 主状态 | 规范目标 |
| --------------------------------------------- | -------------- | ------------------------------------------ |
| `README.md` | REWRITE | 根系列 README |
| `paper-1/aeg-paper-1.tex` | REWRITE | Paper I 入口 |
| `aeg-lemma.tex` | HOLD | 审计、附录或归档 |
| `bibliography/aeg-paper.bib` | KEEP/CLEAN | 共享参考文献 |
| `build.sh` | KEEP/EXTEND | 多论文构建 |
| `Dockerfile` | KEEP/VERIFY | 可复现构建 |
| `sections/sec01.tex` | REWRITE | Paper I 第 1 章 |
| `sections/sec02-00.tex` | SPLIT/REWRITE | Paper I 第 2 与 6 章 |
| `sections/sec02-01.tex` | SPLIT | Paper I 第 2 与 4 章；Paper IV |
| `sections/sec03.tex` | SPLIT/REWRITE | Paper I 第 4 与 5 章 |
| `sections/sec04.tex` | SPLIT/REWRITE | Paper I 第 6 与 7 章；Paper III |
| `sections/sec05.tex` | REWRITE | Paper I 第 8 章 |
| `sections/sec06.tex` | KEEP/REWRITE | Paper I 第 9 章 |
| `sections/sec07.tex` | SPLIT | Paper I 第 9 章；Paper II |
| `sections/sec08.tex` | MOVE | Paper II |
| `sections/sec09.tex` | REWRITE/SPLIT | Paper I 第 10 章；Papers II–IV |
| `sections/sec10.tex` | SPLIT/APPENDIX | Paper I 附录 C–D |
| `sections/sec11.tex` | SPLIT | Paper I 附录 D；Paper II |
| `sections/sec12.tex` | SPLIT/APPENDIX | Paper I 附录 E；未来关系理论 |
| `notes/projective-condensation/01-bilateral-projective-condensation.tex` | SPLIT | Paper I 第 2–4 章；Paper IV |
| `notes/thermodynamics-and-renormalization/02-aeg-flow-and-renormalization-en.tex` | MOVE | Paper IV |
| `notes/thermodynamics-and-renormalization/03-aeg-flow-and-renormalization-zh.tex` | MOVE/ARCHIVE | Paper IV 笔记 |
| `notes/projective-condensation/02-projective-geometric-frameworks.tex` | SPLIT | Paper I 动机；Paper IV |
| `notes/projective-condensation/03-canonical-forms-and-condensation.tex` | MOVE/ARCHIVE | Paper IV |
| `notes/knots-and-loops/02-zero-taxonomy-and-arithmetic-loops.tex` | SPLIT/HOLD | Paper I 附录 E；未来关系理论 |
| 多重零笔记 | MOVE | Paper III |
| 管笔记 | MOVE | Paper III |
| 纽结笔记 | MOVE/HOLD | Paper III 笔记 |
| 解析笔记 | MOVE | Paper II |
| 复杂度/资源笔记 | MOVE | Paper IV |
| `gpt/` | ARCHIVE | 生成讨论归档 |
| `../archive/plans/` | ARCHIVE/SPLIT | 重组或论文 README |
| `images/` | AUDIT | 按图角色 Papers I–IV |

---

# 第十四部分. 迁移记录

## 45. 所需迁移日志

创建：

```text
governance/migration-log.md
```

每个实质移动必须加一条目：

```markdown
## Migration M-XXXX

- Date:
- Source:
- Source section or line range:
- Destination:
- Migration state:
- Claim treatment:
- Theorem nodes affected:
- Notation changes:
- Content retained in source:
- Content removed from source:
- Build result:
- Reviewer notes:
```

---

## 46. 内容保留规则

从活跃源移除文本前，验证以下其一为真：

1. 它存在于规范目的地；
2. 它保留于归档；
3. 它记录为可证明重复；
4. 它记录为拒绝且理由陈述。

「不再在 Paper I」非删除充分理由。

---

## 47. 重复源规则

过渡期间，临时重复允许。

每个重复块必须含或伴迁移注识别：

* 规范版本；
* 临时版本；
* 计划删除点。

审查后，只可留一个规范活跃版本。

---

# 第十五部分. Codex 执行边界

## 48. 审计任务权限

对初始审计，Codex 可：

* 读所有仓库文件；
* 运行构建；
* 创建 `governance/audit-report.md`；
* 创建来源清单。

它不得：

* 重写论文；
* 移动文件；
* 重命名模型；
* 静默修复证明；
* 删除材料。

---

## 49. 骨架任务权限

对骨架阶段，Codex 可：

* 创建目标节文件；
* 更新 Paper I 入口；
* 加占位引言；
* 在临时 include 中保留遗留节。

它不得：

* 删除遗留文件；
* 实质改变定理断言；
* 破坏性迁移 Paper II–IV 材料。

---

## 50. 章迁移权限

每个章迁移任务必须指定：

```text
Allowed source files
Allowed target files
Forbidden files
Theorem nodes in scope
Claim statuses allowed to change
Required build checks
```

任务不得从此映射推断权限去重写无关文件。

---

# 第十六部分. 已知高风险迁移

## 51. Threadlike 表达式迁移

### 风险

现有子定向定义与示例不一致。

### 所需动作

* 不审计所有示例不补一词；
* 用依赖偏序与标记脊柱定义替换；
* 需要时仅作历史评论保留旧术语。

### 受影响节点

```text
S1, S2, T1, S3, S4
```

---

## 52. (\mathfrak E_0/\mathfrak E_1) 迁移

### 风险

模型编号跨仓库版本改变。

### 所需动作

全局替换前创建模型名审计表：

| Formula/domain | Historical name | Target name | Status |
| -------------- | --------------- | ----------- | ------ |

不用盲搜索替换。

---

## 53. ACS 定向迁移

### 风险

当前公式用反演历史编码未来加权；目标公式用直接余循环积分。

### 所需动作

* 证明等价；
* 选一个规范定向；
* 重算所有示例；
* 更新每个符号与图注；
* 保留反演作特殊情形。

### 受影响节点

```text
T3, G1, T9, T10, T11, T12, T17
```

---

## 54. 接触对全纯迁移

### 风险

当前叙事使解析结构看起来内在于接触几何。

### 所需动作

* Paper I 保留接触与水平曲率；
* 复结构依赖结果移到 Paper II；
* 陈述附加解析选择；
* 防 Paper I 摘要与结论声称完整函数论。

---

## 55. 孤立零迁移

### 风险

孤立零模型若呈现为光滑非退化可能矛盾正则零定理。

### 所需动作

审计：

* 域；
* 光滑性；
* 度量；
* 参数行为；
* 方程域。

然后分类为：

* 奇异点；
* 删除点；
* 退化参数点；
* 边界产物；
* 无效模型。

不编辑性选分类；数学建立。

---

## 56. 管迁移

### 风险

「总零集」「光滑管」「纽结」当前太易混淆。

### 所需动作

Paper I 仅保留正则值构造。

Paper III 必须单独证明：

* 淹没；
* properness；
* 局部平凡；
* 嵌入；
* 单值；
* 纽结不变。

---

## 57. 复杂度迁移

### 风险

概念类比可能表述为数学推论。

### 所需动作

把此类材料移到 Paper IV 并按状态标每个断言。

无形式：

[
\text{noncommutativity}
\Rightarrow
\text{computational hardness}
]

的陈述可留 Paper I。

---

# 第十七部分. 完成判据

## 58. Paper I 迁移完备性

Paper I 当前到目标迁移完成。其闭包报告记录以下判据证据：

* [x] 每个基线 `sec*.tex` 文件有记录处置；
* [x] 所有 Paper I 目标章存在；
* [x] 所有保留数学内容有一个规范位置；
* [x] Paper II 解析材料已移动或清楚隔离；
* [x] Paper III 奇异/管材料已移动或清楚隔离；
* [x] Paper IV 商/复杂度材料已移动或清楚隔离；
* [x] 无遗留节仍意外包含；
* [x] 迁移期间无定理丢失；
* [x] 模型编号一致；
* [x] ACS 符号一致；
* [x] Paper I PDF 构建；
* [x] 摘要与结论匹配迁移定理集。

---

## 59. 仓库范围迁移完备性

仓库范围映射只有每个实质文件赋以下之一才完整：

```text
Paper I
Paper II
Paper III
Paper IV
future paper
shared support
active note
archive
remove
hold
```

无文件可仅因文件名不透明即保持未分类。

---

## 60. 最终迁移原则

迁移必须把仓库从发现的时间堆积转变为依赖控制论文系列。

支配规则是：

[
\boxed{
\text{preserve research provenance}
\quad+\quad
\text{choose one canonical mathematical location}
\quad+\quad
\text{state every unresolved claim honestly}.
}
]

Paper I 应只保留建立以下所需：

[
\text{marked histories}
\to
PGL_2
\supset
\operatorname{Aff}(1)
\to
\text{flow}
\to
\mathfrak E_0
\to
\text{torsion and contact curvature},
]

连同正则与奇异零几何之间的基础边界。

其余一切必须不丢失迁移。

## 2026-10-09 有限型与移植 AES 来源映射

| 来源 | 活跃目标 | 迁移状态与论断边界 |
|---|---|---|
| 2026-10-09 紧化研究 | Paper 0 `12-compactification.tex` | 新审查几何集成；证明有显式有限型/端/collar 假设 |
| 同研究的圆与叶比较 | Paper 0 `app-E-circle-surgery.tex` | 精确局部比较；无未证明 AES 手术提升 |
| 可读八页 *Ported Arithmetic Expression Spaces* v0.1 | Paper IV `05b-ported-aes-programs.tex` | 语境残差后 PDF 文本改编；严格有限 DAG 与特征判据 |
| 9 月 29 日临界穿孔审查 | Paper 0 `11-holed-aes.tex` | 极小延拓共形背景修复；原始证据仍归档且未变 |
| 原始 k4/ported ZIP 证明、脚本与证据 | 尚无字节导入 | HOLD：不可读原始归档；原始 39/55 检查未重跑 |
| 新编写精确有限检查 | Paper 0 / Paper IV `scripts/` | 独立回归证据，与原始包分开识别 |
