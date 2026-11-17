# AES 笔记：几何、连续性与度量实现

**状态：** 设计与研究笔记，创建于 2026-11-07。这些不是论文论断，不是治理记录，也不
改变任何数学状态登记。笔记 01–02 记录椭圆 AES 计划（正曲率、紧化、分析）。笔记 03–04
（2026-11-10 添加）记录有理邻域数据、显式基本模型中的连续性，以及几何度量实现的独立
开放问题。笔记 05 记录邻域质量、Haar 传输、条件概率、信息及其面积联系。

## 为什么有独立的 `aes/` 目录

`analysis-and-calculus/` 与 `foundations-and-geometry/` 下的笔记发展现有 AES 理论，其
几何核心是 Paper 0 的基本双曲模型。该目录始于**椭圆 AES 计划**：选择 Cayley–Klein
实形式族作为骨架、对同名三分法的审计，以及这一选择所打开的算术/表达式侧问题。它还
持有所要求的 AES 结构数据笔记：局部邻域基与关系传输，连同度量实现问题。

## 内容

- [01 – Trichotomy audit and the Cayley–Klein skeleton](01-trichotomy-audit-and-cayley-klein-skeleton.md)
- [02 – The arithmetic side of the elliptic AES](02-arithmetic-side-of-the-elliptic-aes.md)
- [03 – Quadrilateral neighborhoods and Scott continuity](03-quadrilateral-neighborhoods-and-scott-continuity.md)
- [04 – Structural data, metric unification and the catenoid example](04-structural-data-metric-unification-and-catenoid.md)
- [05 – Measure, probability, information and area](05-measure-probability-information-and-area.md)

## 椭圆 AES 计划摘要（笔记 01–02）

仓库中五个不同的三分法共享名称 elliptic / parabolic / hyperbolic。在论文系列内，只有
Paper 0 的射影迹三分法是完整的分类级几何理论，但它分类的是分裂实形式
$\mathrm{PSL}_2(\mathbb R)$ 的等距；它不产生正曲率 AES。Paper 0 §12.6 的常曲率三分法有
已发展的双曲条目、一个抛物退化，以及一个被明确标注为「未发展」的椭圆条目。此处提议的
骨架是 Cayley–Klein 族

$$
g_c=\frac{4\,|dz|^2}{(1+c|z|^2)^2},
\qquad
a_c=\frac{2\mu\operatorname{Im}z}{1+c|z|^2},
\qquad
K_{g_c}=c,
$$

其中 $c<0$ 是基本双曲模型，$c=0$ 是平坦模型，$c>0$ 是球面模型。对 $c>0$，赋值有界，
两个极点形成临界（转向）轨迹，算术运动是部分的，表达式侧获得一个新的「值域」。

## 连续性与度量实现（笔记 03–04）

笔记 03 在指定的正仿射基本模型中给出证明：有理四边形基、传输的参考值、闭包关系、一个
标记连续族，以及 Scott 连续盒观测。精确共享参数关系与其区间包络保持区分。这不是对任意
表达式历史、奇异管粘合或二元结构复合的完整理论。

笔记 04 保留度量统一问题及其来自链接讨论 Page 的 catenoid 例子。有理根括号是被认证的；
显示的面积是数值近似。一般的 AES 度量实现与结构质量的几何解释仍开放。

## 邻域质量、概率与信息（笔记 05）

笔记 05 分离结构质量、条件概率、对数信息、正面积与带符号 ACS 序缺陷。它固定左/右 Haar
约定，证明基本传输定律与跨层运动的条件选择，并包含一个带认证对数界的有理分割例子。
一个固定叶构造把这些数据连接到 Scott 开集上的连续赋值。一般度量实现与任意历史的概率
语义仍开放。

## 与论文的关系

- Paper 0 §3.6 命题 3.13（`prop:p0-projective-trichotomy`）：射影运动的迹分类与长度。
- Paper 0 §12.6：三个常曲率模型；椭圆条目被明确标注为「未发展」。
- Paper 3 §4：$\Gamma_4=\langle J,T\rangle$，二阶与四阶椭圆点、锥角与尖点；论文系列中
  唯一被算出的椭圆构型。
- Paper 5 §3–§4：二次标量与签名三分法。§8 仍说 Paper 0 未发展迹三分法；该陈述相对于
  Paper 0 已过时。
- Note 49：有限域圆锥三分法；它明确否认曲率读法。
- `governance/discussions/three-branch-arithmetic-tubes-and-complexity.md`：$c$-族公式与
  实形式提案。讨论级，不是论文论断。

## 椭圆计划开放问题

1. 定义一个**紧/临界 AES**，承认 $c>0$ 模型而不把它强塞进 Papers 0 与 I 的正则/奇异二分。
2. 为 $c>0$ 重新推导算术框架与接触括号；当 $\lambda^2=-c<0$ 时规范框架
   $X_u a=\mu$、$X_v a=\lambda a$ 无实解。
3. 定义**值域**，并与 Papers I 与有限域笔记的普通域、射影域比较。
4. 发展球面分析：$a_c$ 是 $\ell=1$ 球谐函数，零集是赤道，临界轨迹是两个极点。
5. 决定椭圆 AES 是复化 AES 的实形式，还是带自身公理的独立范畴。

## 溯源

2026-11-07 由三部分工作讨论写成。路径与行号指仓库在 commit `f1fe625`（2026-11-07）的
状态。未修改任何论文源。

2026-11-10 的补充由苑明理指导，并由 ChatGPT / Codex（OpenAI）形式化/起草。其逐笔记溯源、
证明、来源与论断边界记录于笔记 03–04。来源 Page 被保留；未修改任何手稿或数学状态登记。

笔记 05 记录同一 2026-11-10 讨论的独立测量/概率线程。其附加假设、推导与用户报告的模型
动机在其溯源节中区分。
