# 算术表达式几何（Arithmetic Expression Geometry）

本仓库包含算术表达式几何（AEG）研究计划的手稿、笔记、图件、参考文献与构建工具。
AEG 不是只看表达式的最终数值，而是通过其**有序求值历史**来研究算术表达式。

当前活跃的手稿系列为：

> **Arithmetic Expression Geometry 0**  
> *Arithmetic Expression Spaces: Expansion and Motion, Eikonal Equation,
> Horocycle Pullbacks, Commutativization, Contact Structure, and Tearing*

> **Arithmetic Expression Geometry I: Foundations**  
> *Sequential Histories, Projective Semantics, and Zero Geometry*

> **Arithmetic Expression Geometry II: Hyperbolic Real Function Theory**  
> *Horizontal Operators, Boundary Problems, and Arithmetic Holomorphicity*

> **Arithmetic Expression Geometry III: Singular Zero Geometry and Tubes**  
> *Branched Pullbacks, Arithmetic Zero Networks, and Topological Transport*

> **Arithmetic Expression Geometry IV: Projective Condensation and Computational Complexity**  
> *From Histories and Quotients to Representation and Cost*

> **Arithmetic Expression Geometry V: Triadic Characteristics and Threaded Apertures**  
> *Three Readings, Observation Fibres, and the Syntax of Apertures*

> **Arithmetic Expression Geometry VI: Process Geometry**  
> *Native Programs, Evaluation Orders, and the Arithmetic--Process Equivalence*

它们的规范入口分别是
[`paper-0/aeg-paper-0.tex`](paper-0/aeg-paper-0.tex)、
[`paper-1/aeg-paper-1.tex`](paper-1/aeg-paper-1.tex)、
[`paper-2/aeg-paper-2.tex`](paper-2/aeg-paper-2.tex)、
[`paper-3/aeg-paper-3.tex`](paper-3/aeg-paper-3.tex)、
[`paper-4/aeg-paper-4.tex`](paper-4/aeg-paper-4.tex)、
[`paper-5/aeg-paper-5.tex`](paper-5/aeg-paper-5.tex) 与
[`paper-6/aeg-paper-6.tex`](paper-6/aeg-paper-6.tex)。
起支配作用的范围、数学状态登记、迁移映射与验收标准位于
[`governance/`](governance/README.md)。Paper 0 由权威修正案
[`governance/00a-paper-0-amendment.md`](governance/00a-paper-0-amendment.md) 引入，
其现行范围由
[`governance/00b-paper-0-geometric-foundation-amendment.md`](governance/00b-paper-0-geometric-foundation-amendment.md)
固定——该文件使 Paper 0 成为系列的几何基础，并把 Paper I 的几何各章移入其中。

## 一个开放的研究项目——欢迎合作者

AEG 是一个**开放研究项目**，我们正在积极寻找合作研究者。手稿以草稿形式发布，
正是为了让这个计划可以在适合新读者的任意位置进入，而不必非从开头读起。

新读者不必接受整套架构即可作出贡献。每篇论文都陈述了自身的范围、每条论断的状态，
并且——有意地——标出该计划尚未完成之处。那些未完成之处正是设想的切入点。当前示例：

* Paper IV——实际的对边特征见证、所有多输入门由 AES 运动的忠实实现、以及非平坦的
  射影传输。
* Paper V——由周期–能量数据导出序关系、一个不可分解的三元缺陷、`M_6` 边界缺失的
  填充子、以及一个带类型的反馈算子。Paper V §17 按依赖顺序列出了这些内容。

贡献方式包括：证明或反驳某条已陈述的猜想、为某次校准提供反例、收紧某个假设、用更短的
论证替换某段论证，或报告某条论断状态的错误。反驳与扩展同样受欢迎：这个系列的编排方式
使得一个诚实的否定结果是一项贡献，而不是一次挫折。

请在本仓库提出 issue 或 pull request。由于论断状态是被明确治理的（见
[`governance/`](governance/README.md)），一项提议的改动应当说明它触及哪条论断，以及
它是加强了、削弱了还是反驳了该论断。

## 穿孔与移植的 AES 集成

2026-10-09 的集成把可复用的有限型几何加入 Paper 0，并把程序替换、精确部分求值与
特征充分性加入 Paper IV。[来源与论断映射](governance/h2-integration-2026-10-09.md)。
实际的对边特征见证、以及所有多输入门由 AES 运动的忠实实现，仍保持开放。

## 草稿状态

所有活跃手稿在通常的编辑与出版意义上都是草稿。它们的概念组织、行文、图件以及
正文–图件的整合仍在开发中。这一成熟度标签不提升也不削弱任何定理、命题、猜想、计算或
开放问题；论断级别的状态是被单独治理的。

## 版本与 DOI

[![Earlier DOI version](https://zenodo.org/badge/DOI/10.5281/zenodo.18887455.svg)](https://doi.org/10.5281/zenodo.18887455)

Zenodo DOI 标识的是手稿的一个较早归档版本。它不会自动标识任何正在重组中的论文。未来的
发布必须在 DOI 元数据被改动之前获得作者明确批准。

## 七论文架构

0. **Paper 0 — Arithmetic Expression Spaces。** 显式操作数槽位约定下的算术展开，
   作为联系不同展开的重写规则的分配律，作为运动的算术表达式空间与四则运算，模型
   `E_0` 与 `E_1`，连续算术运动，被称为 ripple geometry 的对偶读法，仿射余循环
   （affine cocycles），带加权 torsion–Stokes 定理的累积交换空间，撕裂（tearing），
   该缺陷的接触结构，对线性语言的两类阻碍，带已计算见证登记的穿孔空间，有限型紧化，
   任意正穿孔数与全领三端重构。Paper 0 是系列的几何基础；它不修订 Paper I 的
   标记历史形式体系。

1. **Paper I — Foundations。** 内在顺序树分类、标记脊柱历史、双边射影语义、仿射扇区、
   `q=4` Hecke 算术子语言、正则零刚性、奇异算术表达式空间，以及与后续各论文的接口。
   本论文早期版本中发展的仿射余循环、连续流、双曲模型、ACS 挠率与接触曲率，现归属于
   Paper 0。

2. **Paper II — Hyperbolic Real Function Theory。** 水平复结构与解析结构、算子域、核、
   边值问题、平面与柱面全纯拉回，以及谱问题。

3. **Paper III — Singular Zero Geometry and Tubes。** 多重零构造、分支拉回、算术零网络、
   相对除子、符号覆盖、穿线载体（threaded carriers）、Lyashko–Looijenga 遗忘、真管
   （proper tubes）、单值、辫与条件性纽结不变量计划。

4. **Paper IV — Projective Condensation and Computational Complexity。** 射影商塔、
   双赋值、对年代敏感的延拓、语境残差、极小精确状态、操作式活配置、纤维与熵不等式、
   重写阻碍，以及固定模型校准。

5. **Paper V — Triadic Characteristics and Threaded Apertures。** 观察者契约与观察纤维、
   作为「商加残差」的特征、二次标量三分法与作为被保留中心符号的手性、带其导出
   Clifford 关系的六态载体、三元特征推断、带型多重性、带解析 torsor 与导出单值的
   贯穿交叉（through-crossings）、由满足形式生成的逻辑、非忠实影子目录，以及——在其
   第二部分——带型孔径（typed apertures）、穿线充分性、带强规范化的有序线性演绎、
   汇合与可判定可导性、以及六端口整切核。其范围由
   [`governance/00c-paper-V-triadic-aperture-scope.md`](governance/00c-paper-V-triadic-aperture-scope.md)
   固定。

6. **Paper VI — Process Geometry。** 带有序孔洞与保留构造历史的原生开放程序、三种读法
   K/C/F、作为构造序线性扩张的调度、arity-1 载体与脊柱/梳序的恢复、平面树的规范求值
   顺序、旋转木马对应与平面螺旋模，以及把过程几何与 Papers I、V 联系起来的带型字典与
   等价陈述。其范围由
   [`governance/00e-paper-VI-process-geometry-scope.md`](governance/00e-paper-VI-process-geometry-scope.md)
   固定。

依赖架构为

```text
Paper 0 -> Paper I -> Paper II
                   -> Paper III
                   -> Paper IV -> Paper V
Paper I -> Paper VI
Paper V -> Paper VI
Paper 0 -> Paper VI
```

## Path–ripple 研究主线

Paper 0 激活了基本接口

```text
left-expanded comb
  -> affine one-hole maps
  -> arithmetic motion in E0
  -> matrices with pole at infinity

right-expanded comb
  -> reciprocal one-hole maps
  -> finite pole and ripple pencil
  -> general Möbius matrices
```

同一个前缀矩阵决定了被传播的点、算子极点、其不动点，以及标准 horocycle 的拉回。
算术倒数也与迭代相关：有限几何级数与连分数截断都是矩阵乘积，而无穷值只在显式的形式或
解析收敛假设下才被断言。即使射影延拓到达无穷，普通的除以零仍不被允许。

## Tearing 主线

算术运动的序缺陷在 Paper 0 中被发展为一条精确陈述的链，而不是一个隐喻：

```text
distributive expansion
  -> same operator, different charges
  -> affine cocycles and the relative defect
  -> commutativization: the accumulative commutative space
  -> weighted torsion--Stokes: the defect is an area
  -> contact structure: the same defect has density mu*lambda
  -> punctured spaces: tearing carried at a declared singular point
```

*ripple geometry* 与 *tearing* 这两个名称是描述性的；它们所命名的计算在 Paper 0 中
被证明，而所计算孔洞见证的读法被保持在状态 `COMPUTATIONALLY VERIFIED EXAMPLE`。

## Arithmetic–automorphic 研究主线

后续跨论文的发展保持单向：

```text
Paper I arithmetic histories
  -> q=4 Hecke projective operators
  -> Paper II holomorphic pullback targets
  -> Paper III branched automorphic zero networks
  -> sign-cover geodesic knots and peripheral polynomial threads.
```

每支箭头具有不同的信息层级。字面历史不与算子、单元、端点、几何叶或纽结等同。
六次 Lyashko–Looijenga 实验室证明，一个有限的遗忘映射可以丢失真正的亏格二模量，但从
标记历史到算术素除子的一般函子仍保持开放。

## Arithmetic–computational 研究主线

Paper IV 激活了第二个条件接口：

```text
Paper I marked histories
  -> PGL2 operator evaluation
  -> projective quotient G/H
  -> future-relative contextual residual
  -> encoded online state
  -> operational live-configuration trace.
```

只有当未来作用下降且观察穿过商时，商才是一个精确的在线状态。残差基数给出一个固定宽度的
状态选择界；实际工作量、工作空间、内存–时间与通信需要一个被声明的机器模型。不能仅由
非交换性、负曲率、群增长或原始历史纤维大小就推断出任何困难性结果。

## 构建手稿

本地构建需要 `pdflatex` 与 `bibtex`：

```bash
./build.sh
```

这将构建 Papers 0–VI。要只构建一篇手稿，运行

```bash
./build.sh 0
./build.sh 1
./build.sh 2
./build.sh 3
./build.sh 4
./build.sh 5
./build.sh 6
```

预期产物为 `paper-k/aeg-paper-k.pdf`，其中 `k = 0,1,2,3,4,5,6`。

对于有 Docker 的环境，仍可用容器构建：

```bash
docker build -t aeg-paper .
docker run --rm -v "$(pwd):/work" aeg-paper
```

Paper IV 的有限验证套件为：

```bash
python paper-4/scripts/verify-paper4.py
```

## 仓库权威性

并非本仓库中的每条笔记都是现行数学。当来源冲突时，请按 [`AGENTS.md`](AGENTS.md) 中
规定的顺序，并连同上面提到的 Paper 0 修正案一起处理。特别是，`notes/`、
`images/sources/`、`archive/revision-*`、`archive/arxiv/`、`archive/paper4p/` 以及
历史的纽结或热学笔记保留的是探索性材料，除非某份迁移或来源审计记录另有说明，否则它们
不是规范的论文来源。
