# AGENTS.md

## 仓库目的

本仓库包含算术表达式几何（AEG）论文系列的源、笔记、图、参考文献与构建工具。

当前重组把材料分为五篇论文：

0. **Arithmetic Expression Geometry 0 — Arithmetic Expression Spaces**（几何基础；范围由
   `governance/00b-paper-0-geometric-foundation-amendment.md` 固定）
1. **Arithmetic Expression Geometry I: Foundations**（历史、射影、Hecke 与零层）
2. **Arithmetic Expression Geometry II: Hyperbolic Real Function Theory**
3. **Arithmetic Expression Geometry III: Singular Zero Geometry and Tubes**
4. **Arithmetic Expression Geometry IV: Projective Condensation and Computational Complexity**

仓库含不同开发阶段写的研究笔记。有些笔记含探索性、被取代、猜想或错误表述。不把每个文件视为
同等权威。

---

## 指令层级

指令冲突时用以下优先顺序：

1. 显式任务提示。
2. 本 `AGENTS.md`。
3. `governance/` 下权威文件。
4. 当前主论文源。
5. `notes/`、`gpt/`、`../archive/plans/` 或其他归档目录下研究笔记。

`governance/` 下文件应显式识别它们是权威规范、状态记录、审计还是归档讨论。

聊天转录与历史笔记是开发过程证据，非最终规范。

不静默调和冲突来源。记录冲突并遵循最高优先来源。

---

## 文档语言政策

文档材料 —— 仓库与论文 `README`、索引文件、`AGENTS.md` 与权威治理记录 —— 双语，以**英文为主
文档**。

* 规范文件保持普通名：`X.md` 为英文。
* 中文译件并排存放为 `X.zh.md`（同 basename + `.zh`）。
* 现有双语对迁移：中文 `X.md` 改名为 `X.zh.md`，英文 `X.en.md` 改名为 `X.md`（先把
  `X_en.md`/`X-en.md` 归一化为 `.en.md`）。
* 交叉引用总指向主 `X.md` 名。

研究笔记正文（`notes/` 及其他探索性或讨论材料）**不强制双语**。它们可按原文保持中文或英文，
与 `governance/06-editorial-rules.md` 中「出版语言」规则一致。已带两种语言的笔记保持上述归一化
命名；不需新翻译单语言笔记正文。

译文必须精确保留数学含义：保持每个公式、记号、LaTeX、代码块、图/引用引用与状态标签不变，并
遵循 `governance/06-editorial-rules.md` 中「出版语言」规则。翻译时不改述证明或改论断状态；译文
是忠实呈现，非重写。

---

## 一般工作原则

### 保留数学含义

这是研究数学仓库，非一般行文编辑项目。

修改论文时：

* 保留定义、引理、命题、定理、示例、注、猜想、提案与开放问题之间的区分；
* 不把直觉、类比、计算观测或结构提案转为定理；
* 无显式证明不加强假设或结论；
* 不只为简化阐述移除假设；
* 未建立不推断唯一性、存在、正则性、紧性、properness 或不变性；
* 不用润色行文掩盖数学缺口；
* 显式陈述未解决点。

若证明不完备，按权威数学状态文件标结果为不完备、提议、猜想或条件。

### 过程先于结果

AEG 区分几个不得坍缩的层：

[
\text{expression tree}
\longrightarrow
\text{marked history}
\longrightarrow
\text{operator}
\longrightarrow
\text{endpoint value}.
]

编辑定义或论证时保留以下区分：

* 字面语法相等；
* 标记历史相等；
* 诱导算子相等；
* 总 charge 相等；
* 端点值相等；
* 商、归一化或凝聚后相等。

不因两历史求值为同值即等同它们。

### 保留溯源

不因材料不再是 Paper I 一部分即删研究材料。

材料移出主论文时：

* 移到适当论文草稿、笔记、附录或归档；
* 保留有用标签、引用、公式、示例与证明片段；
* 重组日志记录来源与目的地；
* 避免使开发历史不可恢复的破坏性重写。

---

## 权威重组文档

执行任何重组任务前，读 `governance/` 下相关文件。

预期权威文件含：

* `governance/00-authoritative-scope.md`
* `governance/01-paper-series-architecture.md`
* `governance/02-paper-I-outline.md`
* `governance/03-theorem-dependency-graph.md`
* `governance/04-current-to-target-map.md`
* `governance/05-mathematical-status.md`
* `governance/06-editorial-rules.md`
* `governance/07-acceptance-checklist.md`
* `governance/08-open-questions.md`

若这些文件一个或多个尚不存在，不发明其内容。只任务显式提供的范围内工作。

`governance/discussions/` 下文件总结研究路线但从属于权威范围与数学状态文件。

`governance/archive/` 下文件归档且不得视为当前决定。

---

## Paper 0 范围纪律

Paper 0 是系列几何基础。其范围权威于
`governance/00b-paper-0-geometric-foundation-amendment.md`，其论断状态登记于
`governance/05b-paper-0-status-register.md`。

Paper 0 可含：

* 左、右展开梳文法、单孔截面与关联同一表达式不同展开的分配展开；
* 正则 AES 公理、规范算术框架与作运动的四运算；
* 基本双曲模型 `E_0`、单穿孔模型 `E_1` 与连续算术运动；
* 对偶读法（极点、horocycle 拉回、ripple 铅笔）、倒数、无穷、不动点与矩阵综合；
* 仿射余循环、相对仿射缺陷、累积交换空间、加权 torsion–Stokes 定理与撕裂；
* 接触结构、水平场、曲率与标量水平微分；
* 替换线性语言的结构提案，与带计算见证的穿孔空间。

Paper 0 不得作为主要理论发展：

* 任意顺序树内在依赖偏序分类（那留 Paper I；Paper 0 引用）；
* 混合手性标记历史作主要对象；
* Hecke `q=4` 历史语言；
* 正则零刚性、奇异零分类、零网络、管、辫或纽结不变量；
* 算术全纯函数论、边值理论或谱理论；
* 射影双赋值、商塔、凝聚或计算复杂度；
* 无穷算术表达式一般收敛理论；
* 任何 ripple 几何是新几何同构类或接触形式强制相容复结构的声称。

---

## Paper I 范围纪律

Paper I 建立 AEG 语法与射影基础。其几何章节——算术表达式空间、运动、双曲模型、仿射余循环、
ACS torsion 与接触曲率——在 Paper 0 发展，其范围文件对它们权威。

其意图逻辑脊柱是：

[
\text{sequential syntax}
\longrightarrow
\text{projective semantics}
\supset
\text{affine sector}
\longrightarrow
\text{expression geometry (Paper 0)}
\longrightarrow
\text{zero geometry}.
]

Paper I 可含：

* 顺序树分类；
* 标记脊柱历史；
* 操作数槽手性；
* 镜像、时间反演与路径逆；
* 非退化双边历史射影求值；
* 生成 (PGL_2(K))；
* 仿射/Borel 扇区识别；
* `q=4` Hecke 子语言及其历史级关系；
* 从 Paper 0 导入的正则 AES 接口，用于其自身陈述；
* 正则零轨迹结果；
* 奇异算术表达式空间基础定义；
* 极小多重零示例，若完全验证；
* 基础参数族零曲面引理。

Paper I 不得作为主要理论发展：

* 算术表达式空间几何构造、其运动、其交换化或接触结构（Paper 0 拥有）；
* 完整双赋值或秩一投影子理论；
* 完整 (G/H) 与 (G/B_\pm) 商塔；
* 概念–谓词语义；
* 完整算术全纯函数论；
* Poisson 核、Green 函数或边值理论；
* 一般 (E_k) 或 (E_{\log}) 分类；
* 奇异管分岔理论；
* 辫、纽结、Markov 移动或新纽结不变量；
* 一般计算复杂度结论。

这些属后续论文除非权威范围文件另说。

---

## 重要数学区分

### 顺序树

含糊时不使用非形式 left-expanded/right-expanded 术语。

优选基于以下的内在定义：

* 内部顶点依赖偏序；
* 求值顺序唯一性；
* 单个内部脊柱存在；
* 标记累加器；
* 显式操作数槽标签。

用：

[
C_{\omega,c}^{(1)}[z]=\omega(z,c),
\qquad
C_{\omega,c}^{(2)}[z]=\omega(c,z).
]

不把树平面定向与求值时间顺序混淆。

### 镜像与反演

保持以下不同：

* **mirror**：交换操作数槽位置；
* **temporal reversal**：反演语境词；
* **path inverse**：反演词并把每个可逆语境替换为其逆。

从序比较定义的算术 torsion 不自动检测树镜像。

### 射影与普通算术语义

射影延拓改变语义范畴。

例如 Möbius 映射可把 (0) 送到 (\infty)，而普通算术声明除零未定义。

总区分：

* 普通可允许算术求值；
* 射影延拓；
* 图转换；
* 极点与域排除。

不无限定陈述射影完备化移除普通算术奇异。

### 仿射与射影流

现有连续 AEG 流是射影 Riccati 流仿射/Borel 切片。

保持不同：

[
\dot z=\beta+\alpha z
]

与

[
\dot z=\beta+\alpha z+\kappa z^2.
]

不把仅仿射扇区证明的结论当作自动在完整射影理论成立。

### 左与右群约定

凡用矩阵演化或 Maurer–Cartan 形式，显式陈述约定。

区分：

[
g^{-1}dg
\qquad\text{与}\qquad
dg,g^{-1}.
]

也区分：

* 源/体框架坐标；
* 目标/空间框架坐标；
* 左乘法；
* 右乘法；
* 操作数槽手性。

这些是相关结构但定义上不同一。

### Torsion

可能时优选双历史表述。

若历史 (\gamma) 与 (\delta) 有相容总 charge 或线性部分，显式定义并分析其相对缺陷。

除非定理或示例特别要求，不特权反演。

保持不同：

* 端点差；
* 仿射平移坐标；
* 群值相对缺陷；
* 开两步 torsion；
* 闭环 holonomy；
* 无穷小曲率密度；
* ACS 加权面积。

### 接触结构与分析

接触形式与水平分布本身不唯一决定复结构。

保持不同：

* 接触形式；
* 水平分布；
* 水平度量；
* 定向；
* 相容近复结构；
* 算术 Cauchy–Riemann 算子。

除非供唯一性定理，不声称算术全纯性由接触形式唯一强制。

### 水平微分

当前记 (\delta) 的算子对曲率敏感且一般不幂零。

优选术语如：

* horizontal covariant differential；
* horizontal differential；
* connection-induced differential。

当

[
\delta^2\neq0.
]

时不把它描述为普通微分复形。

### 零轨迹与奇异

对满足

[
|\nabla a|^2=\mu^2+\lambda^2a^2
]

带 (\mu\neq0) 的光滑非退化算术表达式空间，零集正则因

[
|\nabla a|=|\mu|
\quad\text{于 }a^{-1}(0).
\]

故光滑非退化设置中，未识别必要奇异、退化、边界效应、properness 失败或范畴改变前，不引入：

* 孤立零点；
* 零线交叉；
* 分支零线；
* 零线诞生或死亡。

用显式记号：

[
Z_{\mathrm{reg}}(a)
\qquad\text{与}\qquad
Z_{\mathrm{sing}}(a).
]

### 管结构

正则参数族可产光滑总零集，但更强结论需附加假设。

不声称：

* 全局积结构；
* 拓扑保持；
* 紧性；
* properness；
* 同痕不变；
* 辫或纽结不变；

除非陈述并证明所需假设。

---

## 数学状态标签

重组期间引入或移动的每条实质结果必须有以下之一状态：

* `proved`；
* `proved with stated hypotheses`；
* `standard consequence requiring an in-paper proof`；
* `computationally verified example`；
* `partially proved`；
* `structural proposal`；
* `conjecture`；
* `open problem`；
* `unsupported and excluded`。

用权威数学状态文件确定状态。

若状态不清，不猜。把问题加到开放问题或审计文件。

---

## 编辑规则

### 做小、可审查变更

优选窄 commit 序列而非单一全局重写。

每任务只修改其范围所需文件。

一个 commit 不结合：

* 基础定义变更；
* 章重排；
* 记号归一化；
* 证明修复；
* 参考文献清理；
* 图重设计；
* 迁移到另一论文；

除非任务显式要求该组合。

### 保持依赖顺序

定义或定理必须使用前出现，除非引用显式前瞻。

重组时用定理依赖图。

移动结果后检查：

* 所有引用；
* 标签；
* 定理编号；
* 记号依赖；
* 参考文献条目；
* 引言摘要；
* 摘要断言；
* 结论断言。

### 避免重复理论

结果移到另一论文时：

* 只留 Paper I 所需最少陈述或前向引用；
* 不在两位置维护分歧完整版本；
* 识别一个规范源文件。

### 保持记号一致

引入新记号前，搜索仓库现有使用。

特别注意：

* (\mathfrak E_0) 对 (\mathfrak E_1)；
* (u) 对视相似符号如 (\nu)；
* (A,M) 作 ACS 坐标；
* (a) 作赋值；
* (\lambda,\mu) 作生成元强度；
* 源归一化对目标归一化仿射坐标；
* (E_k)、(E_{\log}) 与其他模型标签；
* 左/右、槽 (1)/槽 (2)、源/目标、镜像/反演。

无显式迁移计划不全局重命名已建立记号。

### 证明纪律

编辑证明时：

* 保留所有假设；
* 检查正则性、正性、可逆性、紧性与域假设每个使用；
* 区分实、复、特征零与任意域论证；
* 区分局部与全局结论；
* 区分有限与无穷小恒等；
* 区分精确公式与渐近展开。

不用「clearly」「naturally」「it follows」等短语替换证明，除非省略步真例行且仍可恢复。

---

## LaTeX 规则

### 源组织

适当处用现有节文件。

章实质重组时，优选清楚新节文件而非一文件堆积无关材料。

附录用于：

* 长计算；
* 扩展示例；
* 坐标检查；
* 情形表；
* 次要推导。

主文专注定义、中心示例、命题、定理与概念转换。

### 标签与引用

用语义标签，例如：

```latex
\label{thm:sequential-tree-classification}
\label{def:marked-spinal-history}
\label{prop:affine-cocycle}
\label{thm:regular-zero-locus}
```

避免含 `final`、`revised` 或 `enhanced` 等词的自动或叙事标签。

不重用标签。

结构变更后搜索断引用与重复标签。

### 定理环境

用正确定理标题。

特别示例必须用 `example` 环境其打印标题是 `Example`，非 `Theorem`。

无清楚编辑理由不引入无编号定理类断言。

### 方程

数学内容用精确方程。

不用显示方程仅作装饰。

陈述恒等式是否：

* 精确；
* 局部；
* 渐近；
* 无穷小；
* 仅水平分布上有效；
* 仅远离奇异有效。

### 参考文献

不只为使节显得更广加引用。

历史或技术比较用主要或标准数学引用。

不引用不含相关结果的来源支持定理。

不删别处仍用参考文献条目。

---

## 构建与验证

正常本地构建命令：

```bash
./build.sh
```

Docker 构建路径也可用：

```bash
docker build -t aeg-paper .
docker run --rm -v "$(pwd):/work" aeg-paper
```

修改 LaTeX 源每任务：

1. 运行可用构建过程；
2. 报告 PDF 是否产出；
3. 检查构建错误与重要警告；
4. 检查未定义引用；
5. 检查缺失引用；
6. 检查重复标签；
7. 检查缺失图或资产。

不因命令无明显错误退出即报成功。确认预期 PDF 产物存在。

若环境不能构建论文，报精确限制且仍执行静态检查。

---

## 所需任务报告

重组任务末，提供简明报告含：

1. 改变文件；
2. 添加、移除、削弱或迁移的数学论断；
3. 引入或显式化的假设；
4. 未解决数学问题；
5. 移到另一论文或归档的材料；
6. 构建结果；
7. 剩余警告；
8. 推荐下一任务。

仓库含证明前不把数学缺口描述为已解决。

---

## 禁止行为

不：

* 一次失控重写整篇论文；
* 静默丢弃研究笔记；
* 静默合并不一致定义；
* 发明缺失证明；
* 把类比转为数学等价；
* 把实验证据转为一般定理；
* 仅从几何增长推断计算下界；
* 仅从非交换性推断双曲性；
* 从视觉暗示管构造推断纽结不变；
* 从对称示例推断唯一性；
* 无 properness 或等价假设声称参数族拓扑平凡；
* 把射影延拓当普通算术求值；
* 把当前仿射理论当完整射影理论；
* 把归档讨论当权威规范。

---

## 不确定时安全默认

当数学或编辑决定不能从权威文件解决：

1. 保留现有源；
2. 任务报告或开放问题文件加精确注；
3. 提议最小可行变更；
4. 不猜作者意图定理。

重组目标非仅改善呈现。它是要产出一个其定义、证明、依赖与研究边界显式、稳定、可审计的论文系列。
