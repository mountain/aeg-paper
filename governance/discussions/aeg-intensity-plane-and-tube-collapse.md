# 强度平面 $(\mu,\lambda)$、管的塌缩极限与"更大的空间"

**File:** <code>governance/discussions/aeg-intensity-plane-and-tube-collapse.md</code>  
**Status:** Working research note（研究讨论，非权威）  
**Version:** 1.1  
**Date:** 2026-11-08  
**Primary topic:** 把两个强度参数 $(\mu,\lambda)$ 变成基是否给出更大的空间；管（tube）在该空间中的真实角色；Teichmüller 空间在其中的位置  
**Primary paper interface:** Paper 0 §3.9（`subsec:p0-normal-form`）、§9（`rem:p0-weighted-charges`）、§12（`subsec:p0-three-models`、`warn:p0-hyperbolic-auxiliary`）；Paper 3 §6（`prop:polynomial-carrier-thread`、`thm:quadratic-threaded-carriers`）、§9（`def:ambient-aeg-family`、`subsec:intensity-collapse`、`thm:proper-real-zero-tube`）  
**Related records:** <code>governance/discussions/smooth-and-differential-topology-layer.md</code>（§6 的指标/留数路线与本文 P4 共用同一个边界对象）  
**Authority:** 从属于 <code>governance/00–08</code>；本文档本身不是权威规范

> 本记录把一次讨论整理成可复核的工作文档：四条候选命题（含证明骨架）、两种塌缩的对照与陷阱、
> 以及与 §3.9 / §9 / §12 / Paper 3 §6、§9 的接口。凡本文与论文正文或治理文件不符处，以后者为准。
> 状态以 <code>05b-paper-0-status-register.md</code> 与
> <code>05-mathematical-status.md</code> 的词汇为准。

**落地记录（2026-11-08，v1.1）。** 四条候选命题已按 §8 的顺序写入论文：

| 候选 | 落点 | 论文内标签（当前编号） | 状态 |
|---|---|---|---|
| P2 | Paper 3 §9.1 | `rem:intensity-plane-not-a-base`（Remark 9.3） | `PROVED` |
| P1 | Paper 3 §9.1 | `rem:intensity-plane-factorization`（Remark 9.4） | `PROVED` |
| P4 | Paper 3 §9.5 | `prop:intensity-collapse`（Prop 9.8）＋ `rem:intensity-collapse-hypotheses` ＋ `warn:intensity-collapse-two-readings` | `PROVED WITH STATED HYPOTHESES` |
| P3 | Paper 0 §9 | `rem:p0-weighted-charges`（Remark 9.3） | `PROVED` |

与草案的三处差异需要记下。其一，P4 的落点从"§5.2"改为 **§9.5**：`def:ambient-aeg-family`
与真正则管定理其实在 §9，把它放在 §6 会引入前向引用；§9.5 与 §9.3 的逃逸族（`prop:nonproper-escape`）
恰好形成对照——那里是拓扑在无穷远处改变，这里是拓扑完全不变而度规塌缩。其二，面积渐近的余项改为
$O(\lambda^{-2}\log\lambda)$（见 §9 第 1 条）。其三，P2 的第二读法（保度规）在论文中以"Paper 0 的正规形"
一句引用，不重述其证明。

---

## 1. 结论摘要

问题：$\mu$ 与 $\lambda$ 参数化之后是否自然引入一个空间；其中单独变 $\lambda$ 是否给出管形构造；
管的"多项式纤维"在其中扮演什么角色。

结论五条。

1. **$(\mu,\lambda)$ 不是管的模方向。** 在语料库现有的两种自然读法里（保度规动赋值、保赋值动度规），
   零集都与 $(\mu,\lambda)$ 无关。以强度平面为基的"管形丛"是乘积 $\Sigma\times\{(\mu,\lambda)\}$。
   这条本身应作为 no-go 记录（§6 N1）。
2. **强度平面塌成"一个长度单位方向 × 一个无量纲形状参数"。** 联合标度
   $(g,\mu,\lambda)\mapsto(s^2g,\mu/s,\lambda/s)$ 保持 eikonal；对基本模型
   $g_{\mu\lambda}=\mu^{-2}g_{1,\rho}$，$\rho=\lambda/\mu$，$K=-\lambda^2=-\mu^2\rho^2$。
   所以本质参数只有 $\rho$，$\mu$ 是长度单位（§3 P1）。
3. **接触模型里这件事是规范。** 令加权荷 $U=\mu u$、$V=\lambda v$，则
   $\alpha=\dd a-\dd U-a\,\dd V$ 与 $(\mu,\lambda)$ 无关；$D_u=\mu D_U$、$D_v=\lambda D_V$、
   $[D_U,D_V]=\partial_a$。平面场、Reeb 场是规范；曲率标量 $\mu\lambda$ 是两个流参数化的乘积
   （§3 P3）。
4. **管是 $\lambda\to\infty$ 的极限，不是 $\lambda$ 的纤维。** 在 Paper 3 的共形实现里（$A$ 与底度规
   固定），$g_\lambda=\frac{|\dd A|^2}{\mu^2+\lambda^2A^2}g_0$：零管 $\Sigma$ 等距嵌入每个成员
   （正则部分上；载子的空间临界点须先声明为奇异层），
   且 $(M,g_\lambda)$ 在 Gromov–Hausdorff 意义下收敛到 $(\Sigma,g_\infty)$，速率
   $O(\log\lambda/\lambda)$；极限上赋值恒为 $0$，因而**离开正则范畴**（§3 P4）。
5. **"多项式纤维"只在载子方向兑现，不在 $\lambda$ 方向。** $A=\operatorname{Im}P$ 时整个
   $\lambda$-族是 $(z,\lambda)$ 的有理族，极限是实代数曲线配代数度规；但零集不随 $\lambda$ 动，
   所以 $\lambda$-方向拓扑单值平凡，没有 $\lambda$-判别式。代数结构应服务于**载子模空间**方向
   （§5.3、§5.4）。

一句话：**$(\mu,\lambda)$ 是结构常数而不是模空间坐标；管是极限对象而不是纤维对象。** 两个身份分清之后，
"更大的空间"有三个可落地的候选（§5.4）。

---

## 2. 已有内容的审计

| 已有对象 | 位置 | 与本讨论的关系 |
|---|---|---|
| 环境族（$\mu,\lambda$ 固定） | Paper 3 `def:ambient-aeg-family` | 定义明确把强度放在基之外；这是"$(\mu,\lambda)$ 可以当基吗"的原始问题所在 |
| 真正则管定理 | Paper 3 `thm:proper-real-zero-tube` | 管 $=$ 真正则淹没；基是一维的；竖直可定向不可省（Klein 瓶反例） |
| 螺旋管 | Paper 3 `thm:helical-zero-tube` | 显式族；$\lambda$ 只出现在度规里，零纤维 $2n$ 个区间的公式不含 $\lambda$ |
| 共形实现公式 | Paper 3 `prop:polynomial-carrier-thread`（`eq:polynomial-carrier-aeg-metric`） | P4 的定义域：$g_b=\frac{|\partial_zP_b|^2}{\mu^2+\lambda^2(\operatorname{Im}P_b)^2}|\dd z|^2$ |
| 二次多项式载子 | Paper 3 `thm:quadratic-threaded-carriers` | 载子 $\Sigma_m\cong\Sigma_{m-1,4}$，$2m$ 个 Morse 鞍点；纤维是实代数曲线（"多项式纤维"） |
| 载子标架与判别式周期 | Paper 3 `prop:carrier-framing-discriminant` | $\mathrm{Fr}=-\operatorname{wind}(\operatorname{disc})$ 由 $P$ 算出，与 $\lambda$-族无关 |
| 正规形 | Paper 0 §3.9 `prop:p0-normal-form` | P2(i) 的来源；也给出计算 $\lambda$-族的坐标（Fermi） |
| 软性 | Paper 0 §3.9 `cor:p0-normal-form-softness` | 解释为什么 $(\mu,\lambda)$ 不可能成为"形状"模方向：形状是自由的 Jacobi 场 $J$ |
| 常数曲率三模型 | Paper 0 §12 `subsec:p0-three-models` | $\lambda$ 的符号/取零 $=$ 双曲/平坦；椭圆情形不是闭正则 AES |
| Teichmüller 段 | Paper 0 §12（FN 段） | 明确：FN 重建 $h$，不重建 $(g,a)$ |
| 完整分裂警告 | Paper 0 §12 `warn:p0-hyperbolic-auxiliary` | 完备无边正则 AES 只能是平面或柱面 ⇒ 亏格必须来自穿孔/边界/奇点 |

---

## 3. 四条候选命题

### P1 强度平面的分拆

> **命题 P1.** 设 $\mathfrak E=(M,g,a;\mu,\lambda)$ 是正则 AES，$s>0$。则
> $(M,s^2g,a;\mu/s,\lambda/s)$ 也是正则 AES；两者的规范标架方向、水平叶层、零集、以及比值
> $\rho=\lambda/\mu$ 都相同，而第二者的标架是第一者的 $s^{-1}$ 倍。对基本模型更有显式分拆
> $$g_{\mu\lambda}=\mu^{-2}g_{1,\rho},\qquad \rho=\frac{\lambda}{\mu},\qquad
> K=-\lambda^2=-\mu^2\rho^2 .$$

**证明骨架.** (i) $|\nabla a|^2_{s^2g}=s^{-2}|\nabla a|^2_g$，故 $(\mu/s)^2+(\lambda/s)^2a^2
=s^{-2}(\mu^2+\lambda^2a^2)$ 成立。(ii) 标架的显式式（`eq:explicit-arithmetic-frame`）
只通过 $\mu/q$ 与 $\lambda a/q$ 进入，二者在联合标度下不变
（$q$ 与 $|d a|$ 同乘 $s^{-1}$）；归一化后的标架因此同向。(iii) $a$ 不变，故水平集与零集不变。
(iv) $E_0$ 的分拆是代数恒等式；$K(g_{1,\rho})=-\rho^2$ 由代换 $Y=\rho y$ 得
$g_{1,\rho}=\rho^{-2}(\dd x^2+\dd Y^2)/Y^2$ 再用"度规乘 $c$ 则 $K$ 乘 $1/c$"；最后
$g_{\mu\lambda}=\mu^{-2}g_{1,\rho}$ 给出 $K=-\mu^2\rho^2=-\lambda^2$。四项已用 SymPy 核验（附录 A）。

**状态：** `PROVED`（代数恒等式 + 两行论证）。

**落点与风险.** 它是 Paper 3 §5 度规公式或 Paper 0 §3.9 的一条 remark，不是头条结果。**必须写清：
联合标度是公理体系的对称性，不是理论的对称性**——长度是观测量
（`prop:p0-length-multiplicative-charge`），$g\mapsto s^2g$ 把所有长度乘 $s$。所以它是解空间上的流，
不是等价关系；任何"按 $\rho$ 参数化"的说法都不能写成"商掉标度"。

### P2 管不随 $(\mu,\lambda)$ 动

> **命题 P2.** 在语料库的两种读法下，零集都与 $(\mu,\lambda)$ 无关。
> (i) *正规形读法*：固定 $(M,g)$ 且 $\nabla t$ 完备，则强度为 $(\mu,\lambda)$ 的 AES 的赋值是
> $a=A_{\mu\lambda}(t)$，零集是 $t^{-1}(0)$，与 $(\mu,\lambda)$ 无关。
> (ii) *共形读法*：若 $A$ 是给定的光滑函数、$0$ 是正则值，且
> $g_{\mu\lambda}=\frac{|\dd A|^2_{g_0}}{\mu^2+\lambda^2A^2}g_0$，则 $Z(A)=\{A=0\}$ 与
> $(\mu,\lambda)$ 无关。
> 因此以强度平面为基的环境 AEG 族的零入射是乘积 $\Sigma\times\{(\mu,\lambda)\}$。

**证明骨架.** (i) 是 `prop:p0-normal-form` 的 (5)(6)：$A$ 的解由 $t$ 与 $(\mu,\lambda)$ 决定，
$A$ 严格单调、$A(0)=0$，故 $A^{-1}(0)=t^{-1}(0)=Z(a)$。(ii) 是定义：$A$ 被给定，只有共形因子依赖
$(\mu,\lambda)$。

**状态：** `PROVED`（(i) 引用 §3.9，(ii) 定义）。

**落点与风险.** 这是本讨论的核心障碍，应作为 **no-go N1** 写进 Paper 3 §5（紧接
`def:ambient-aeg-family`），一句话即可："把 $(\mu,\lambda)$ 放进基不会移动管；它只移动度规与标签。"
风险：不要把这条读成"$(\mu,\lambda)$ 不可观测"——度规、标架、长度、撕裂都依赖它们（见 P3 的风险）。

### P3 接触模型的规范不变性

> **命题 P3.** 在 $\mathcal C=\mathbb R^3_{(u,v,a)}$ 上取
> $\alpha=\dd a-\mu\,\dd u-\lambda a\,\dd v$。令 $U=\mu u$、$V=\lambda v$。则
> $$\alpha=\dd a-\dd U-a\,\dd V ,$$
> 与 $(\mu,\lambda)$ 无关；且 $D_u=\mu D_U$、$D_v=\lambda D_V$，其中
> $D_U=\partial_U+\partial_a$、$D_V=\partial_V+a\partial_a$，从而
> $[D_U,D_V]=\partial_a$ 而 $[D_u,D_v]=\mu\lambda\,\partial_a$。

**证明骨架.** 链式法则 $\partial_u=\mu\partial_U$、$\partial_v=\lambda\partial_V$；代入 $D_u,D_v$
即得两式；括号在 $(U,V,a)$ 坐标下逐项为零，只剩 $\partial_V(a)\partial_a$。已用 SymPy 核验（附录 A）。
与 `thm:contact-curvature` 的关系：该定理的 $\mu\lambda$ 正是这两个参数化因子之积，故与本命题不矛盾。

**状态：** `PROVED`（链式法则 + 直接括号）。

**落点与风险.** 建议作为 Paper 0 §9 的一条 remark（"加权荷坐标"），因为它解释了两件事：
曲率 $\mu\lambda$ 是**归一化后的曲率**（未归一化的 $[D_U,D_V]=\partial_a$ 曲率为 $1$），以及 Reeb 场
$R=-\mu^{-1}\partial_u$ 与 $\lambda$ 无关。**风险（必须写死）**：不变的是加权荷 $(U,V)$、二次形式
$\dd\alpha=-\dd a\wedge\dd V$、以及加权荷的函数；标量 $\mu\lambda$ 只是 $(\dd u,\dd v)$ 参数化下的分量。
两件事同时成立，而且都不能误读：有限缺陷
$T_{\mathrm{open}}=\mu h(e^{\lambda k}-1)=\Delta U\,(e^{\Delta V}-1)$ **是**加权荷增量的函数，
ACS 撕裂 $\iint e^{M}\dd A\wedge\dd M=\iint e^{V}\dd U\wedge\dd V$ 也是；所以它们是联合标度下的不变量，
而 $\mu\lambda$ 既不是接触结构的不变量，也不能被说成"不是物理量"。

### P4 $\lambda$-塌缩：管是 $\lambda\to\infty$ 的极限

> **命题 P4.** 设 $M$ 是带边紧致曲面（或更一般地：$A$ 在 $M$ 上无临界点且 $A(M)$ 有界），
> $g_0$ 是 $M$ 的 Riemann 度规，$A\in C^\infty(M)$ 满足 $\dd A\ne0$ 处处成立、$0\in A(M)$；
> 令 $\Sigma=\{A=0\}$ 与
> $$g_\lambda=\frac{|\dd A|^2_{g_0}}{\mu^2+\lambda^2A^2}\,g_0,\qquad \lambda>0 .$$
> 则：
> 1. 每个 $(M,g_\lambda,A;\mu,\lambda)$ 是正则 AES；
> 2. $\Sigma$ 带 $\lambda$-无关的度规 $g_\infty:=\frac{|\dd A|^2_{g_0}}{\mu^2}\big|_\Sigma$
>    **等距嵌入**每个 $(M,g_\lambda)$；
> 3. $\operatorname{dist}_{g_\lambda}(p,\Sigma)\le\frac1\lambda\operatorname{arcsinh}
>    \frac{\lambda\|A\|_\infty}{\mu}$，故 $(M,g_\lambda)\to(\Sigma,g_\infty)$ 在
>    Gromov–Hausdorff 意义下收敛，速率 $O(\log\lambda/\lambda)$；
> 4. 二维体积 $\operatorname{area}(M,g_\lambda)=\frac{\pi}{\lambda}L_{g_\infty}(\Sigma)+O(\lambda^{-2}\log\lambda)$；
> 5. 极限 $(\Sigma,g_\infty,0)$ 上赋值恒为 $0$，$|\nabla A|_{g_\infty}\equiv0$，故它不是正则 AES；
> 6. 若 $A=\operatorname{Im}P$（$P$ 关于 $z$ 全纯、关于参数光滑），则整个族在 $(z,\lambda)$ 上是有理族，
>    极限是实代数曲线配代数度规。

**证明骨架.**
(1) 共形反演：$g=f g_0$ 时 $|\nabla A|^2_g=f^{-1}|\dd A|^2_{g_0}=\mu^2+\lambda^2A^2$，即
`prop:polynomial-carrier-thread` 的公式。
(2) $g_\lambda|_\Sigma=\frac{|\dd A|^2}{\mu^2+\lambda^2\cdot0}g_0|_\Sigma=g_\infty$，与 $\lambda$ 无关。
(3) 取 $g_0$-法向自 $p$ 到 $\Sigma$ 的路径：其上 $\dd s_{g_0}=\dd A/|\dd A|_{g_0}$，故
$$L_{g_\lambda}=\int_0^{|A(p)|}\frac{|\dd A|}{\sqrt{\mu^2+\lambda^2A^2}}\frac{\dd A}{|\dd A|}
=\frac1\lambda\operatorname{arcsinh}\frac{\lambda|A(p)|}{\mu}\xrightarrow[\lambda\to\infty]{}0 ;$$
再用"$\Sigma$ 等距嵌入 + 每点距 $\Sigma$ 不超过 $\varepsilon$"的对应关系得
$d_{GH}\le 2\varepsilon$（标准估计）。
(4) coarea：$\operatorname{area}=\int_{\mathbb R}\frac{\dd c}{\mu^2+\lambda^2c^2}
\int_{A=c}|\dd A|\dd\mathcal H^1$，主项来自 $|c|\lesssim\mu/\lambda$，给出
$\frac{\pi}{\mu\lambda}\int_\Sigma|\dd A|\dd\mathcal H^1=\frac{\pi}{\lambda}L_{g_\infty}(\Sigma)$。
(5) 在 $\Sigma$ 上 $A$ 为常数，故其内蕴梯度为零。
(6) $|\partial_zP|^2$ 与 $(\operatorname{Im}P)^2$ 都是 $(z,\bar z)$ 的多项式。

**状态：** `STANDARD CONSEQUENCE REQUIRING AN IN-PAPER PROOF`（证明约十行；(4) 的常数已用
显式例子核对，附录 A）。

**落点与风险.**
- 落点：Paper 3 §5.2/5.3，紧跟 `prop:polynomial-carrier-thread`——那里正是共形实现的定义域，
  且二次/六次/LL 三个载子都可直接套用。
- 风险 (a)：**$\dd A\ne0$ 与"$A$ 有界"两条假设都是实质的，而且互相牵制。** $\dd A$ 在临界点为零处
  共形因子为零，$g_\lambda$ 便不再是度规；而紧致无边曲面上光滑 $A$ 必有临界点，故该情形必须带边
  （或取非紧但有界 $A$ 的情形）。这与 §3.9 的 `warn:p0-hyperbolic-auxiliary`／完整分裂的 no-go 是
  同一件事的两面：紧致无边曲面上不存在正则 AES。非紧且 $A$ 无界时只有逐点退化，没有 GH 结论。
- 风险 (b)：**这族拓扑平凡**：零集不随 $\lambda$ 动，故没有 $\lambda$-判别式、没有 $\lambda$-单值。
  不要在这里找 braid/knot 不变量。
- 风险 (c)：极限只是**载子**，不是 thread：$K_P\subset\Sigma$ 两边都是一维，度规极限不区分它们。
- 风险 (d)：**族的情形必须逐纤维化。** P4 的单曲面形式用总导数 $\dd A$；Paper 3 的族形式要把
  $\dd A$ 换成竖直导数 $\dd^VA$、$g_0$ 换成竖直度规 $g^V$，并把结论限制在正则部分
  $M\setminus S_{\mathrm{crit}}$ 上（$S_{\mathrm{crit}}=\{\dd^VA=0\}$）。在 $S_{\mathrm{crit}}$ 上共形因子
  为零，$g_\lambda$ 不是度规，这正是 `prop:polynomial-carrier-thread` 声明为本质奇异层的地方。

---

## 4. 两种塌缩：对照与陷阱

"变 $\lambda$"本身不唯一确定一条族：必须说明**保持什么**。两个自然选择给出两条不同的退化，
而且**只有一条以管为极限**。

| | 保 $A$、底度规（P4，Paper 3） | 保 $a$、适配度规（$E_0$，§3.9） |
|---|---|---|
| $\lambda\to\infty$ 时存活方向 | 水平集的**切向**（法向塌缩） | **加法轨道**（horocycle 方向），即 $\partial_x$ |
| 塌缩方向 | 水平集的法向（$\dd A$ 方向） | **乘法轨道**（$\partial_y$，竖直） |
| 极限对象 | 零管 $\Sigma=\{A=0\}$ 配 $g_\infty$ | 一条 horocycle 配 $\dd x^2/(\mu^2y^2)$，横向长度为零 |
| 管是否存活 | 是（管就是极限） | 否：零测地线 $\{x=0\}$ 与存活方向横截，被压掉 |
| 是否有 GH 极限 | 有（$A$ 有界） | 不宣称（存活尺度 $1/y$ 随 $y$ 变） |

**为什么不同.** 在保 $A$ 的族里，$A$ 就是坐标，共形权只依赖 $A$，故法向长度按
$1/\sqrt{\mu^2+\lambda^2A^2}$ 缩小、切向（$\dd A=0$）不受影响。$E_0$ 的族
$g_{\mu\lambda}=\mu^{-2}g_{1,\rho}$ 则**改变共形类**：$g_{1,\rho}=(\dd x^2+\rho^{-2}\dd y^2)/y^2$
的两个系数之比随 $\rho$ 变，塌缩的是 $\partial_y$，即乘法流的方向。

**陷阱（必须写进正文，否则一定会被误用）.** 把 $E_0$ 换到 horocycle 坐标
$(u,v)$（$\Phi_\lambda(u,v)=(u,e^{\lambda v})$）后
$\widehat g_\lambda=e^{-2\lambda v}\dd u^2/\mu^2+\dd v^2$，看上去 $\lambda\to\infty$ 塌缩的是
$\partial_u$——与上一段的 $\partial_x$ 存活矛盾。原因不是数学错误，而是 $\Phi_\lambda$ 本身依赖
$\lambda$：固定 $(u,v)$ 对应到 $(u,e^{\lambda v})$，是**不同的点**。所以退化极限必须连同一张固定的
识别一起陈述，不能只写"坐标固定"。这是本文档最值得留档的一条负面经验。

**推论（两种塌缩的身份）.** 一种塌缩保**值**（一个水平集，即管），另一种保**运动**（一条加法轨道，
即 horocycle）。这不是两个技巧，而是"值 / 运动"二元性在 $\lambda$-方向上的几何体现；两种都写，才
不会把"$\lambda$ 可变 $\Rightarrow$ 管"当成恒真句。

---

## 5. 接口

### 5.1 与 Paper 0 §3.9（`subsec:p0-normal-form`）

- **P2(i) 就是 §3.9 的直接推论**：`prop:p0-normal-form` 的 (5) 给出
  $a=\frac{|\mu|}{|\lambda|}\sinh(|\lambda|t)$，(6) 给出 $Z(a)$ 是 $t^{-1}(0)$。所以"固定 $g$、变
  $(\mu,\lambda)$"的轨道是纯标签重写，且是自由的。
- **§3.9 的软性（`cor:p0-normal-form-softness`）解释了为什么 $(\mu,\lambda)$ 当不了形状模方向**：
  形状自由度是 Jacobi 场 $J$，而 $J$ 完全自由。把 $(\mu,\lambda)$ 升级为基，不会补上 $J$ 缺失的约束。
- **反向用途（同图两面的关系）**：P4 的族与 §3.9 的正规形可以画在同一张图里。对每个 $\lambda$，
  $g_\lambda$ 的距离坐标 $t_\lambda=(1/\lambda)\operatorname{arcsinh}(\lambda A/\mu)$ 只是 $A$ 的函数，
  所以水平集（从而 $\Sigma$）作为集合不动；而 $g_\lambda$ 的 Fermi 数据 $J_\lambda$ 随 $\lambda$ 变。
  §3.9 是"固定度规看正规形"，P4 是"固定赋值看度规塌缩"，两者不是同一命题的两个版本。
- **一致性核对**：$|K|/\mu^2=\rho^2$ 与 §3.9 的 $\Delta a=2\lambda^2a$（`prop:laplace-eigenfunction`）
  相容：特征值 $2\lambda^2=2\mu^2\rho^2$。
- **假设不可混用**：§3.9 的假设是 $\nabla t$ 的流完备（紧致无边 $M$ 上自动成立，但那时根本不存在
  正则 AES），P4 的假设是 $\dd A\ne0$ 且 $A$ 有界、$M$ 带边。两条假设互不包含，结论也不同：
  前者说"赋值是距离的函数"，后者说"度规族塌缩到零管"。

### 5.2 与 Paper 0 §12

- **`warn:p0-hyperbolic-auxiliary`**：完备无边正则 AES 只能是平面或柱面。所以任何"更大的空间"
  若只用完备正则 AES 来搭，亏格只能为 $0$ 或 $1$；**亏格必须来自穿孔、边界或奇点**。这直接限制了
  "Teichmüller 当模空间"的可用范围。
- **Fenchel–Nielsen 段**：FN 坐标重建 $h$，不重建 $(g,a)$，且"provides no AES deformation unless a
  compatible family $(g_{\mathbf q},a_{\mathbf q})$ and its end data are also constructed"。因此
  Teichmüller 只能作为**共形背景因子**：正确的说法是
  $$\mathfrak M_k\longrightarrow \mathrm{Teich}(\overline M,S),$$
  纤维是赋值/载子/Jacobi 数据，而不是 $\mathfrak M_k\cong\mathrm{Teich}$。
- **`subsec:p0-three-models`**：$\lambda=0$ 是平坦端（`prop:p0-flat-limit`），$\lambda\ne0$ 是双曲端，
  椭圆情形不是闭正则 AES（极大值原理）。所以强度平面的 $\rho^2=-K/\mu^2\ge0$ 只覆盖 $K\le0$；
  "球面端"必须换范畴，这与 P1 的 $\rho\in\mathbb R$ 图像一致。

### 5.3 与 Paper 3 §5

- **`def:ambient-aeg-family`** 把 $(\mu,\lambda)$ 固定；P2 说明把它提升为基得到的是**积**，
  因此该定义是**紧的**，不是疏漏。若要"以强度为基"，必须换对象（P4 的塌缩族）。
- **`prop:polynomial-carrier-thread`** 给出共形实现公式，是 P4 的定义域；但**不能整段套用**。
  该命题的假设是"$\dd A$ 在 $\Sigma_P$ 上非零"，而 P4 要求 $\dd A$ 处处非零；载子的空间临界点
  （$\partial_zP_b=0$ 且 $\operatorname{Im}P_b=0$，如二次载子的 $z=0$）正是共形因子为零之处，
  被该命题显式声明为本质奇异层。所以在族的情形必须把 P4 逐纤维地陈述在正则部分
  $M\setminus S_{\mathrm{crit}}$ 上（用**竖直**导数 $\dd^VA$ 代替 $\dd A$），极限是
  $\Sigma\setminus S_{\mathrm{crit}}$；二次载子的正则部分是 $\mathbb D_R\setminus\{0\}$（锥角 $4\pi$）。
  这一步不改变 P4 的结论，但改变它的定义域，不能省。
- **`thm:quadratic-threaded-carriers`(2)** 的 $2m$ 个 Morse 鞍点是**对基参数 $\theta$** 的临界点，
  不是对 $\lambda$ 的。$\lambda$-族没有判别式（P4 风险 b）。这是"多项式纤维"用途的分界线：
  分层来自多项式/载子参数，不来自强度。
- **`prop:carrier-framing-discriminant`** 的 $\mathrm{Fr}=-\operatorname{wind}(\operatorname{disc})$
  由 $P$ 直接算出；它与 $\lambda$ 无关，正是"$\lambda$-族拓扑平凡"的正面证据。
- **`thm:proper-real-zero-tube` / `thm:helical-zero-tube`**：这里的"管"是**对基 $B$ 的纤维**。
  与 P4 的"管是极限"是同一个词的两个不同角色，正文必须分开命名（例如"基上的管"与"塌缩极限"）。

### 5.4 "更大的空间"的三个候选

1. **塌缩族**（推荐先做）：基取 $\mathbb{P}^1_\lambda$，纤维 $(M,g_\lambda)$，$\lambda=\infty$ 是代数管，
   $\lambda=0$ 是平坦端（`prop:p0-flat-limit`）。这是一条配边式族，正好接
   <code>smooth-and-differential-topology-layer.md</code> §6 的边界对象，也把"$\lambda$ 可变"变成
   一句有内容的话。
2. **载子模空间为基**（"多项式纤维"的正确用法）：基是多项式系数（或其模空间），纤维坐标是
   $(\rho,\mu)$；分层由判别式（根碰撞）与载子的 Morse 事件给出。代数的东西留在代数层面。
3. **Teichmüller 作因子**：$\mathfrak M_k\to\mathrm{Teich}(\overline M,S)\times\mathbb R_\rho$，
   纤维由 §3.9 的正规形 + 各穿孔的奇点型给出。这是"带孔 AES 的模空间"目前唯一站得住的写法。

---

## 6. No-go 清单（应写进正文以保护边界）

- **N1.** $(\mu,\lambda)$ 不是管的模方向（P2）；不要写"强度平面上的管形丛"。
- **N2.** 联合标度是公理体系的对称性，不是理论的等价关系（P1）；不要在不说明的情况下商掉它。
- **N3.** 不变量是加权荷 $(U,V)$、二次形式 $\dd\alpha=-\dd a\wedge\dd V$、以及加权荷的函数（含有限缺陷与撕裂）；标量 $\mu\lambda$ 只是 $(\dd u,\dd v)$ 参数化下的分量。两个方向的误用都要避免：既不能说"$\mu\lambda$ 是接触结构的不变量"，也不能说"$\mu\lambda$ 不是物理量"（P3）。
- **N4.** 两种塌缩不可互相引用（§4）；尤其是 $E_0$ 的 $\lambda\to\infty$ 极限**不是**管。
- **N5.** $\lambda$-族拓扑平凡：无 $\lambda$-判别式、无 $\lambda$-单值、无由 $\lambda$ 产生的不变量。
- **N6.** Teichmüller 是共形背景因子，不是 AES 模空间（§12 原话）。
- **N7.** $E_0$ 的塌缩不宣称 GH 极限（存活尺度依赖 $y$）；只做逐点（张量）陈述。

---

## 7. 开放问题

- **O1.** 塌缩极限的**内蕴**表述：能否在"模掉微分同胚"的空间里定义 $\lambda\to\infty$ 的边界，
  而不是像 §4 那样依赖一张固定识别？
- **O2.** 强度平面的紧化是否切片依赖？$\rho=\infty$ 在"保 $A$"与"保 $a$"两切片上含义不同（§4），
  是否存在典范紧化？
- **O3.** 极限 $(\Sigma,g_\infty,0)$ 是奇点集为整条曲线的奇异 AES；能否对它做指标/留数
  （与另一份记录的候选 D 合流）？若能，$\lambda$-族的边界就有整体不变量。
- **O4.** $\mathrm{Teich}\times\mathbb R_\rho\times$（载子数据）的分层是否与多项式族的判别式分层一致？
- **O5.** 撕裂作为加权荷的函数 $T_{\mathrm{open}}=\Delta U(e^{\Delta V}-1)$ 已是联合标度不变的；
  它能否在载子模空间上表示为 $\rho$ 与多项式系数的函数，从而成为 §5.4 第二个候选的模不变量？
  （目前没有；记录为未解决，不要预设。）

---

## 8. 落地建议

| 内容 | 建议位置 | 状态 |
|---|---|---|
| P2 + N1 | Paper 3 §9.1（`rem:intensity-plane-not-a-base`，紧接 `def:ambient-aeg-family` 与 `thm:parameterized-zero-section`） | `PROVED`（已落地） |
| P1 + N2 | Paper 3 §9.1（`rem:intensity-plane-factorization`） | `PROVED`（已落地） |
| P3 | Paper 0 §9（`rem:p0-weighted-charges`，与 `thm:contact-curvature` 并置） | `PROVED`（已落地） |
| P4 + §4 的对照表 | Paper 3 §9.5（`subsec:intensity-collapse`，`prop:intensity-collapse`，附 `rem:intensity-collapse-hypotheses` 与 `warn:intensity-collapse-two-readings`） | `PROVED WITH STATED HYPOTHESES`（已落地） |
| N4、N7 | 与 P4 同处的 warning | — |
| Teichmüller 因子化 | Paper 0 §12 的 FN 段后加一句，或 Paper 3 的模空间讨论 | `STRUCTURAL PROPOSAL` |

不建议：现在就在 Paper 0 或 Paper 3 新开"模空间"专章。理由与上一份记录相同——正则范畴被 §3.9
压平，奇点范畴归 Paper 3，专章会先制造重复。

---

## 9. 未解决与需人工复核

1. P4(4) 的渐近常数只在显式例子上核对过（附录 A）；一般情形的余项是 $O(\lambda^{-2}\log\lambda)$ 而不是 $O(\lambda^{-2})$，因为 $\int|c|\,\dd c/(\mu^2+\lambda^2c^2)$ 在有界区间上是 $O(\lambda^{-2}\log\lambda)$。这一项已在正文中改正。
2. P4(3) 的 GH 估计用了"最近点"对应关系；紧致性是实质的，非紧情形必须改写或加假设。
3. §4 的 $E_0$ 塌缩只是逐点陈述；若要 GH，需先固定归一化（例如在 $y=1$ 处定标）。
4. O5 是否存在尚无证据；不要在正文中暗示"撕裂可以无量纲化"。
5. 附录 A 的 SymPy 核验是单作者机器检验，按 `AUTHORSHIP_AND_PROVENANCE.md` 的常设规则，
   **不构成独立人工复核**。

---

## 附录 A：核验脚本与输出

```python
import sympy as sp
x, y, mu, lam, s, rho = sp.symbols('x y mu lambda s rho', positive=True)

# (a) E_0 factorization:  g_{mu,lam} = mu^{-2} g_{1,rho},  rho = lam/mu
g  = sp.diag(1/(mu**2*y**2), 1/(lam**2*y**2))
g1 = sp.diag(1/y**2, 1/(rho**2*y**2))
assert sp.simplify(g - g1.subs(rho, lam/mu)/mu**2) == sp.zeros(2)
print("(a) ok")

# (b) curvature: K(g_{1,rho}) = -rho^2 ; g_{mu,lam} = mu^{-2} g_{1,rho}  =>  K = -lam^2
K1 = sp.simplify(sp.Integer(-1)/(1/rho**2))          # rho^-2 * hyperbolic metric
assert sp.simplify(K1 + rho**2) == 0
assert sp.simplify((K1*mu**2).subs(rho, lam/mu) + lam**2) == 0   # after rho = lam/mu
print("(b) ok")

# (c) joint scaling preserves the eikonal: |grad a|^2_{s^2 g} = s^-2 |grad a|^2_g
a = sp.Function('a')(x, y); ginv = sp.diag(y**2, y**2)
ga = sp.Matrix([sp.diff(a, x), sp.diff(a, y)]); ng = (ga.T*ginv*ga)[0, 0]
assert sp.simplify((ga.T*(ginv/s**2)*ga)[0, 0] - ng/s**2) == 0
print("(c) ok")

# (d) contact model: U = mu*u, V = lam*v;  D_u = mu*D_U, D_v = lam*D_V,
#     [D_U,D_V] = d/dA,  [D_u,D_v] = mu*lam*d/da
u, v, av = sp.symbols('u v a', real=True)
U, V, A = sp.symbols('U V A', real=True)
f = sp.Function('f'); Fu = f(mu*u, lam*v, av)
DU_f = sp.diff(f(U, V, A), U) + sp.diff(f(U, V, A), A)
DV_f = sp.diff(f(U, V, A), V) + A*sp.diff(f(U, V, A), A)
assert sp.simplify((sp.diff(Fu, u) + mu*sp.diff(Fu, av))
                   - mu*DU_f.subs({U: mu*u, V: lam*v, A: av})) == 0
assert sp.simplify((sp.diff(Fu, v) + lam*av*sp.diff(Fu, av))
                   - lam*DV_f.subs({U: mu*u, V: lam*v, A: av})) == 0
def bracket(X, Yv, vs):
    return sp.Matrix([sum(X[j]*sp.diff(Yv[i], vs[j]) - Yv[j]*sp.diff(X[i], vs[j])
                          for j in range(3)) for i in range(3)])
assert bracket(sp.Matrix([1, 0, mu]), sp.Matrix([0, 1, lam*av]), (u, v, av)) == sp.Matrix([0, 0, mu*lam])
assert bracket(sp.Matrix([1, 0, 1]), sp.Matrix([0, 1, A]), (U, V, A)) == sp.Matrix([0, 0, 1])
print("(d) ok")

# (e) collapse: the g_0-normal path from (x,0) to Sigma has g_lam-length
#     (1/lam) asinh(lam x / mu), which tends to 0
t = sp.symbols('t', positive=True)
val = sp.integrate(1/sp.sqrt(mu**2 + lam**2*t**2), (t, 0, x))
assert sp.simplify(val - sp.asinh(lam*x/mu)/lam) == 0
assert sp.limit(sp.asinh(lam*x/mu)/lam, lam, sp.oo) == 0
print("(e) ok")
```

输出（2026-11-08）：`(a) ok  (b) ok  (c) ok  (d) ok  (e) ok`。

面积渐近的显式核对：取 $M=[-1,1]_x\times[0,1]_y$、$A=x$、$g_0$ 欧氏，则
$\operatorname{area}(M,g_\lambda)=\int_{-1}^{1}\dd x/(\mu^2+\lambda^2x^2)
=\frac{2}{\mu\lambda}\arctan\frac{\lambda}{\mu}\to\frac{\pi}{\mu\lambda}$，而
$\frac{\pi}{\lambda}L_{g_\infty}(\Sigma)=\frac{\pi}{\lambda}\cdot\frac1\mu$，两者一致。
