# Paper 0 — Arithmetic Expression Spaces（算术表达式空间）

[形式化推导工作](formal/README.md) 用 Adva 编写的相等 checker、独立的 Lean 陈述与显式覆盖
清单，开始对当前手稿逐章验证。初步证据覆盖命名的代数分量，并有第 2 章语法与受保护的普通
定义域的后续工作。其首个来源发现 OQ-090 由修正命题中的「标记数据/标量投影」区分解决。
每一条论断的范围请查阅当前数学状态登记。

第 2 章还恢复了「可求值表达式」的早期概念，并把部分语义与有效有理求值及语义判定问题分开。
[历史讨论](../governance/discussions/evaluable-expressions-and-effective-presentations.md)
记录了恢复的草稿、Richardson 限定，以及与 Adva 有限构造观点的联系。

附录 C 在一般仿射计算之前恢复了交替表达式及其纯算术扰动推导。其
[历史记录](../governance/discussions/alternating-expressions-perturbation-acs-rg.md)
追踪到 ACS 的路径与后来的 scale/RG 解释，精确恒等式与解释性论断各自保持在其范围内。
[形式化延续](formal/README.md#appendix-c-induction-successor) 为恢复的展开、扰动与受保护的
差商提供有限归纳证明与显式源映射。

附录 F 汇集了[关于切割与表达式基础的背景](appendices/app-F-cuts-and-expression-foundations.tex)：
Bauer–Taylor 的可观测双侧切割、Conway 的递归简单性构造，以及有限名称、指称与观测之间的
区分。Adva 的有限 through 适配器是一个独立的研究先例。所提议的形式化计划仍开放，且不
增加证书覆盖。

**暂定标题：** *Arithmetic Expression Geometry 0*  
**副标题：** *Arithmetic Expression Spaces: Expansion and Motion, Eikonal
Equation, Horocycle Pullbacks, Commutativization, Contact Structure, and
Tearing*  
**MSC 2020：** 53D10（主）；53C22、20F65；30F45、32G15、11J70、03F60

副标题于 2026-10-29 修订，以保守强度只使用两类词：本论文定义的名称（expansion、
motion、commutativization、tearing）与按字面使用的标准数学名称（eikonal equation、
`def:regular-aes`；horocycle pullback、`thm:p0-ripple-pencil-formula`；contact
structure、`prop:contact-form`，当且仅当 `mu*lambda != 0` 时非退化）。两个更早的候选被
否决为夸大了已证明内容：*eikonal metrics*，因为度量是元组的一部分，是恒等式
`|grad a|^2 = mu^2 + lambda^2 a^2` 才是 eikonal 的；以及 *contact curvature*，因为
`rem:p0-curvature-invariance` 表明系数 `mu*lambda` 是所声明算术框架与水平度量的曲率标量，
不是接触同构不变量。此前的副标题是 *Arithmetic Expression Spaces: Expansion, Motion,
Ripple Duals, Commutativization, and Tearing*。名称 *ripple geometry* 与 *tearing* 在正文中
不变，保留其记录的状态。扉页将苑明理列为作者与通讯作者，并把 DeepSeek Harness 列为
形式化与计算协助；这与 Papers II–V 一致，后者已只载单一人类作者。

Paper 0 是系列的几何基础。它发展：

1. 算术展开：显式操作数槽位约定下的左/右展开梳、单孔截面，以及作为联系同一表达式不同
   展开的重写规则的分配律；
2. 算术表达式空间：正则 AES 公理、规范算术框架、作为运动的四则运算、基本双曲模型
   `E_0`、单穿孔模型 `E_1`，以及连续算术运动；
3. 射影对偶读法——极点、horocycle 拉回、倒数、无穷、不动点与矩阵综合——其对偶名称为
   *ripple geometry*（描述性与暂定）；
4. 交换化：仿射余循环、相对缺陷、累积交换空间（ACS）、加权 torsion–Stokes 定理，以及把
   该缺陷读作 *tearing*；
5. 撕裂的接触结构：接触形式、水平场、曲率括号、有限开闭缺陷与标量水平微分；
6. 对线性语言的两类方法论阻碍，以及从过程几何导入的结构性提案；
7. 穿孔算术表达式空间、穿孔的切锥，以及六个已计算见证的登记；
8. 有限型端条件、任意正穿孔数示例、三端 collar 重构、一个精确的四穿孔运动残差，以及
   被仔细分开的圆模型与分支叶模型。

本论文**不**修订 Paper I 的标记脊柱历史术语。Paper I 仍负责内在顺序树分类、混合手性、
年代标记历史、射影求值、Hecke `q=4` 子语言与零几何。

## 规范源闭包

```text
paper-0/
  aeg-paper-0.tex
  sections/
    01-introduction.tex
    02-expansion.tex
    02a-evaluation-and-effectivity.tex
    03-aes-and-motion.tex
    04-ripple-geometry.tex
    05-reciprocals-fixed-points.tex
    06-projective-unification.tex
    07-affine-cocycles.tex
    08-acs-tearing.tex
    09-contact-of-tearing.tex
    10-beyond-linear.tex
    11-holed-aes.tex
    12-compactification.tex
    12-interface.tex
  appendices/
    app-A-calculations.tex
    app-B-hyperbolic-calculations.tex
    app-C-affine-cocycles.tex
    app-D-acs-contact.tex
    app-E-circle-surgery.tex
    app-F-cuts-and-expression-foundations.tex
```

第 7–9 节与附录 B–D 由修正案 `governance/00b-paper-0-geometric-foundation-amendment.md`
从 Paper I 移入；它们保留其标签、假设与状态。本论文使用共享参考文献
`bibliography/aeg-paper.bib`。

## 论断边界

本手稿中已证明（状态记录于 `governance/05b-paper-0-status-register.md`）：

- 两个纯梳都有唯一的内部求值顺序；
- 右梳在对偶运算下变成左梳；
- 分配律在保持算子的同时改变展开的 charge；
- 基本双曲模型是常曲率的完备正则 AES；
- 四则运算作为运动作用，加法尺带 Baumslag–Solitar 型传输关系；
- 水平 horocycle 被实保向 Möbius 映射的拉回是在算子极点处相切的一条线或圆；
- 几何级数与连分数截断满足所述递推与矩阵公式，收敛只在显式假设下声称；
- 平移、非零缩放与反演生成 `PGL_2(K)`；
- ACS 求值公式与加权 torsion–Stokes 定理；
- 历史群是两个步族的自由积，charge 端点是其交换化，且两个 charge 中只有乘法的一个
  下降到运动（`thm:p0-descent`）；
- 接触形式当且仅当 `mu*lambda != 0` 时非退化，水平场满足 `[D_u,D_v] = mu*lambda*d_a`；
  括号缺陷是分布上的规范 2-形式，且 `mu*lambda` 是它在所声明水平度量的正交标架上的值；
- 基本模型是接触模型的 Reeb 商，水平场下降到规范框架，且 `d(alpha)` 等于
  `-mu*lambda` 乘以双曲面积形式；
- 算术生成元不闭合成有限维 Lie 代数（故没有有限维 Lie 群作用携带全部三个秩），且
  交换化电荷的可观测量检测不到撕裂；
- 在正则 AES 中赋值无临界点，故每个水平集都是光滑曲线；
- 四圆构型是一个显式穿孔 AES 的零轨迹，其度量由 eikonal 恒等式强制，穿孔不可延拓且
  位于有限距离（`thm:p0-four-circle-model`）；
- 对每个 `k >= 1` 存在恰有 `k` 个本质穿孔的共形可紧化穿孔 AES
  （`thm:p0-arbitrary-k-punctures`）；这是存在性结果，不是按穿孔数的分类；
- 对赋值光滑延拓、且所给度量在每个穿孔附近共形于一个光滑非退化延拓背景度量的穿孔空间，
  穿孔集恰是赋值的临界集，从而规范且唯一，孔数等于临界点数（`thm:p0-punctures-are-critical`、
  `cor:p0-puncture-count`；在 `governance/05b-paper-0-status-register.md` 第 8 节为
  `PROVED WITH STATED HYPOTHESES`）。同一陈述在 9 月 22 日无共形背景假设的无限制形式
  仍被反驳，在该登记第 6 节为 `UNSUPPORTED AND EXCLUDED`；本论文摘要不声称任一形式；
- 撕裂与穿孔无关，不存在穿孔的规范 holonomy，且在每一个正则 AES 中矩形的两种排序终止于
  赋值不同的点，故 ACS 比较是规范的而非对孔洞的权宜之计；
- 在四圆模型中绕穿孔的小圆与零轨迹交于八个变号点，共形类可延拓而度量不可，穿孔位于
  有限距离；
- 该零轨迹在穿孔处的切锥是 `(xy)^2 = 0`。

作为提案而非定理标注：名称 *ripple geometry*、*tearing* 语言、模型标签约定 `E_k`，以及
从过程几何导入的词汇。开放延拓包括 ripple geometry 的内在射影 AES、商稳定路径/ripple
不变量、穿孔的规范选择、多线推广，以及无穷算术表达式的一般理论。

## 2026-10-09 的紧化集成

移植 AES 的几何基础是第 12 节。几何穿孔、共形点填充、边界圆与计算输入仍是不相同的对象。
临界穿孔定理现在包含 9 月 29 日审查所要求的延拓共形背景假设。

用以下命令运行新编写的、标准库精确有限检查：

```bash
python paper-0/scripts/verify-compactification.py
```

这些检查补充手稿证明。它们不是对原始 39 项研究档案的重跑，该档案的字节在此次集成期间
不可用。参见 `governance/h2-integration-2026-10-09.md` 了解源覆盖、数学状态与剩余的原始
产物恢复任务。


## 平坦极限与二次秩修复（2026-11-07）

第 3 节现在在坐标变换 `y = exp(lambda v)` 后证明一个光滑尖 Euclid 极限，包括赋值与规范
框架收敛。第 12.6 节区分该极限与固定图表发散、以及亏格零紧化上选定的圆度量。其复化论断
现在保持二次秩：只有两个非退化实签名在复数上变得等价。

在安装 SymPy 后运行附加符号回归检查：

```bash
python paper-0/scripts/verify-model-limits.py
python -O paper-0/scripts/verify-model-limits.py
```

这些有限检查补充论文内的一般证明；它们不扩展 Adva/Lean 证书。活跃形式化清单及其源锁定
摘要被刷新，而不改变已归档的证明或执行回执。
