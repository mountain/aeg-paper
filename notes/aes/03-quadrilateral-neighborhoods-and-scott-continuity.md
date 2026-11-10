# 03 – 四边形邻域基、关系运输与 Scott 连续性

**Status:** research note，2026-11-10。本文给出一个明确的基本模型及其证明；
把它用作一般表达式空间的底层框架仍是 **STRUCTURAL PROPOSAL**。
本文不改变论文正文、数学状态登记或既有开放问题的状态。

**范围：** 基本上半平面模型、有限正仿射 A/M 片段、有限有理边界。
实际无限对象由有理近似的完备化解释；不引入无穷小数系。
几何度量统一问题单独保存在
[04 – 结构数据与几何度量统一问题及悬链面算例](04-structural-data-metric-unification-and-catenoid.md)。

## 1. 问题与约定

出发点是 [analysis note 52](../analysis-and-calculus/52-scott-lawson-adva-interval-boundary.md)
所列的区间信息序、Scott/Lawson 比较与项级区间运算问题。本讨论最初称其为
note 53；此处按实际文件编号引用。

本笔记采用 Paper 0 的赋值及正仿射运动：

$$
E_0=\{(x,y):y>0\},\qquad a(x,y)=-x/y,
$$

$$
X_s(x,y)=(x-sy,y),\qquad Y_k(x,y)=(x,y/k),\qquad k>0.
$$

因此 $a\circ X_s=a+s$、$a\circ Y_k=ka$。有限输入和边界先取有理数；
拓扑和定向极限的语义载体允许实数。这里没有断言所有实数或所有理想都可计算；
有效计算必须给出可执行的有理近似名及所需的域证据。

固定 $\mu>0$，Paper 0 的度量为

$$
g_{\mu,\lambda}
=\frac1{y^2}\left(\frac{dx^2}{\mu^2}+\frac{dy^2}{\lambda^2}\right),
\qquad \lambda>0,\qquad K=-\lambda^2.
$$

赋值与上述运动不依赖 $\lambda$。可以把整个 $\lambda$ 连续族作为对象，
但不同成员的度量并不因此相同；$\lambda=0$ 的平直极限需要 Paper 0 中
依赖 $\lambda$ 的坐标识别，不直接包含在本笔记的正参数模型中。

下文的闭合词按**从左到右的时间顺序**执行。$A_t$ 表示运动 $X_t$；
闭合词中的参数记为 $\alpha,\beta,\gamma,\delta$，避免与赋值 $a$ 混用。
$\theta$ 是本笔记的乘法参照值，也可记为 $a_\ast$，不是 Paper 0 连续流中的方向角。

## 2. 带参照值的四边形与闭合关系

### 2.1 邻域的有限边界

定义闭四边形及其内部

$$
Q_\theta(\ell,r;h,H)
=\{(x,y):h\le y\le H,\ \ell\le x+\theta y\le r\},
\qquad U_\theta=\operatorname{int}Q_\theta,
$$

其中 $\ell<r$、$0<h<H$。当五个参数均有理时，其边界可以精确计算。
在坐标 $\xi=x+\theta y$ 中，$Q_\theta$ 就是矩形。
$\theta$ 规定线性边界，不是度量角度。

闭合线索是边界；内部 $U_\theta$ 才是点空间的开邻域。
待研究的点位于内部，闭合线索的起终点可以取为顶点，两者不混同。

### 2.2 乘法边与参照赋值

定义运动族

$$
M_b^{(\theta)}(x,y)
=\left(x+\theta(1-b^{-1})y,\ y/b\right),\qquad b>0.
$$

它保持 $\xi$，并满足

$$
a(M_b^{(\theta)}p)-\theta=b(a(p)-\theta).
$$

所以 $M_b^{(0)}=Y_b$；一般的 $M_b^{(\theta)}$ 是相对参照值的缩放。
作为点映射，它等于 $X_\theta\circ Y_b\circ X_{-\theta}$。
此处运输一条边，是推送整条运动轨迹；不把三段拼接路径与一条推送后的边
自动认作同一 marked history。

### 2.3 闭合证据

**命题 2.1（PROVED WITH STATED HYPOTHESES）。**
固定同一个 $\theta$，并设 $\beta,\delta>0$。
从任意 $p_0=(x_0,y_0)$ 出发，闭合词

$$
A_\alpha M_\beta^{(\theta)} A_\gamma M_\delta^{(\theta)}
$$

返回 $p_0$，当且仅当

$$
\alpha\beta+\gamma=0,\qquad \beta\delta=1.
$$

**证明。** 在 $(\xi,y)$ 坐标中，终点为

$$
\left(\xi_0-y_0(\alpha+\gamma/\beta),\
      y_0/(\beta\delta)\right).
$$

由于 $y_0>0$ 且 $\beta>0$，返回条件恰好是上述两式。证毕。

特别地，从 $p_0=(\ell-\theta h,h)$ 出发，取

$$
\alpha=-\frac{r-\ell}{h},\quad
\beta=\frac hH,\quad
\gamma=\frac{r-\ell}{H},\quad
\delta=\frac Hh,
$$

四个顶点在 $(\xi,y)$ 坐标中依次为

$$
(\ell,h),\quad(r,h),\quad(r,H),\quad(\ell,H),
$$

最后返回 $(\ell,h)$，故恰好走过 $Q_\theta$ 的四条边。
$\alpha<0$、$0<\beta<1$ 保证此例非退化。
闭合等式是有效性证据，不把不同闭合词、基点或路径历史都商为同一个对象。

## 3. 参数套、共同细化与邻域基

有两种需要分别记录的细化。

**表达式参数的细化。** 若 $P$ 是 $(\alpha,\beta)$ 的参数范围且 $\beta>0$，
保留关系族

$$
\mathcal R(P)=
\{(\alpha,\beta,\gamma,\delta):
(\alpha,\beta)\in P,\ \gamma=-\alpha\beta,\ \delta=\beta^{-1}\}.
$$

$P'\subseteq P$ 蕴含 $\mathcal R(P')\subseteq\mathcal R(P)$，
每个实例都闭合。把四个参数分别换成互不相关的区间，会混入不闭合的组合。

**围出区域的细化。** 参数范围缩小本身不保证每个实例围出的区域缩小。
固定 $\theta$，应直接检查

$$
\ell\le\ell',\quad r'\le r,\quad h\le h',\quad H'\le H,
$$

这四条恰好保证 $Q_\theta(\ell',r';h',H')\subseteq Q_\theta(\ell,r;h,H)$。
围绕 $p$ 令 $\ell_n\uparrow\xi_p$、$r_n\downarrow\xi_p$、
$h_n\uparrow y_p$、$H_n\downarrow y_p$，始终严格包围，
就得到内部构成邻域基、交集为 $\{p\}$ 的四边形套。
每层通过命题 2.1 的参数公式保留闭合证据。

**命题 3.1（PROVED WITH STATED HYPOTHESES）。**
所有有理参数的 $U_\theta$ 构成 $E_0$ 通常拓扑的可数基。
不同参照方向的两个基元在任一共同内点附近都有更小的有理四边形基元。

**证明。** 每个 $U_\theta$ 是开集，$\theta=0$ 的有理矩形已经构成通常拓扑的基。
还可直接给出有理共同细化：若有理点 $p=(x_0,y_0)$ 位于
$U_{\theta_i}(\ell_i,r_i;h_i,H_i)$，$i=1,2$，取正有理数

$$
\varepsilon<
\min_{i=1,2}
\left\{
y_0-h_i,\ H_i-y_0,\
\frac{x_0+\theta_i y_0-\ell_i}{1+|\theta_i|},\
\frac{r_i-x_0-\theta_i y_0}{1+|\theta_i|}
\right\}.
$$

以 $p$ 为中心、两个坐标半宽均为 $\varepsilon$ 的闭矩形严格内含于两个开集。
对一般实点，先在严格余量内选择足够近的有理中心和有理半宽；
有理数的稠密性给出同样结论。对有效点，此选择依赖其可计算近似名。证毕。

因此交集或运算像集不必本身是四边形；在每个相关点附近可由四边形细化即可。
两套邻域基表示同一个邻域滤子，恰好在它们互相共尾时成立：

$$
(\forall i)(\exists j)\ V_j\subseteq U_i,\qquad
(\forall j)(\exists i)\ U_i\subseteq V_j.
$$

这是所选观察空间中的同一性，不是表达式历史的同一性。
它也不意味着存在一个算法，可以判定任意两条无限计算名是否相等。

## 4. 带标记总空间与遗忘观察

选择以下显式模型承载参照值和度量参数：

$$
\widetilde E
=\{(x,y,\theta,\lambda):x,\theta\in\mathbb R,\ y,\lambda>0\},
\qquad
\pi(x,y,\theta,\lambda)=(x,y).
$$

把它用于一般 tube 的解释是 **STRUCTURAL PROPOSAL**；
这里的乘积形状是所选模型的定义，不是任意 tube 全局平凡性的结论。
不同参照值可以标记不同叶；这本身不证明发生了分支奇点或非平凡单值性。

**命题 4.1（PROVED WITH STATED HYPOTHESES）。**
坐标映射

$$
\Phi(x,y,\theta,\lambda)=(x+\theta y,y,\theta,\lambda)
=(\xi,y,\theta,\lambda)
$$

是全局微分同胚，且它和逆映射都由有理运算给出。
在此坐标中取四个有理开区间 $I,J,T,L$，其中 $J,L$ 有正下界，则

$$
B(I,J,T,L)=\Phi^{-1}(I\times J\times T\times L)
$$

构成 $\widetilde E$ 的可数基。固定 $\theta,\lambda$ 后，每个非空截面是
第 2 节的开四边形。

**证明。** 逆映射为 $(\xi,y,\theta,\lambda)\mapsto(\xi-\theta y,y,\theta,\lambda)$。
有理开盒构成坐标空间的基；其非空有限交仍为有理开盒，拉回即得结论。证毕。

$\pi$ 是连续开满射，因而是到 $E_0$ 通常拓扑的商映射。
可以在总空间保留参照值，在投影空间遗忘它；也可以只忘掉其中一个标签。
遗忘 $\lambda$ 不保持全部度量观测，遗忘 $\theta$ 也不保证所有相对参照运算都能下降。
具体操作必须满足下降方程，而不是只凭“不同表示”一词认定相容。

## 5. 运算运输闭合关系

### 5.1 固定参数的精确运输

**命题 5.1（PROVED WITH STATED HYPOTHESES）。**
对 $s\in\mathbb R$、$k>0$，

$$
X_s Q_\theta(\ell,r;h,H)=Q_{\theta+s}(\ell,r;h,H),
$$

$$
Y_k Q_\theta(\ell,r;h,H)=Q_{k\theta}(\ell,r;h/k,H/k).
$$

闭合参数分别变换为

| 运输 | 参照值 | $(\alpha,\beta,\gamma,\delta)$ |
|---|---|---|
| $X_s$ | $\theta+s$ | $(\alpha,\beta,\gamma,\delta)$ |
| $Y_k$ | $k\theta$ | $(k\alpha,\beta,k\gamma,\delta)$ |

**证明。** 第一式中 $x'=x-sy$、$y'=y$，于是
$x'+(\theta+s)y'=x+\theta y$。
第二式中 $x'=x$、$y'=y/k$，于是
$x'+k\theta y'=x+\theta y$。
逆变换给出集合等式而非仅包含。
将新边界代入命题 2.1 的参数公式，得到表中的变换；
闭合残量分别保持或变成
$k(\alpha\beta+\gamma)$，而 $\beta\delta$ 不变。证毕。

对于 $\theta=0$，$X_s$ 一般把竖直乘法边剪切为斜边。
精确保留四边形形态需要运输参照值；“同型”在这里指相对于所携标记的
A/M 四边形形态，不是宣称全局固定方向的原始 AMAM 字面词不变。
即使不采用这项扩充，固定方向的矩形仍可作为邻域基。

### 5.2 总空间上的联合连续性

把同一运输提升为

$$
\widetilde X_s(x,y,\theta,\lambda)=(x-sy,y,\theta+s,\lambda),
$$

$$
\widetilde Y_k(x,y,\theta,\lambda)=(x,y/k,k\theta,\lambda).
$$

在 $\Phi$ 坐标中，它们成为

$$
\widetilde X_s(\xi,y,\theta,\lambda)=(\xi,y,\theta+s,\lambda),\qquad
\widetilde Y_k(\xi,y,\theta,\lambda)=(\xi,y/k,k\theta,\lambda).
$$

**命题 5.2（PROVED WITH STATED HYPOTHESES）。**
上述两种作用关于状态及参数联合连续，且满足

$$
\pi\circ\widetilde X_s=X_s\circ\pi,\qquad
\pi\circ\widetilde Y_k=Y_k\circ\pi.
$$

赋值在总空间中为 $a=\theta-\xi/y$，故分别变为 $a+s$、$ka$。

**证明。** 下降方程和赋值等式由代入得到。
加法坐标式是仿射的。乘法坐标式的除数 $k$ 在任一正参数点附近
有正下界 $\kappa$。在有限范围 $y\le H$、$|\theta|\le C$、$k\le M$ 内，

$$
\left|\frac yk-\frac{\bar y}{\bar k}\right|
\le \frac{|y-\bar y|}{\kappa}
+\frac{H|k-\bar k|}{\kappa^2},
$$

$$
|k\theta-\bar k\bar\theta|
\le M|\theta-\bar\theta|+C|k-\bar k|.
$$

这些界为每个输出基本邻域给出输入及参数的有限精度要求。
当界和严格余量有有理证据时，精度要求也可有理计算。证毕。

此下降结论专指所定义的提升。相对运动 $M_b^{(\theta)}$ 若保留 $\theta$
不变，一般不能通过 $\pi$ 下降：在 $(x,y)=(0,1)$、$b=2$ 时，
$\theta=0$ 和 $\theta=1$ 分别给出 $(0,1/2)$ 与 $(1/2,1/2)$。

$\lambda$ 在这两个算术作用下保持不变。连续改变 $\lambda$ 是另外的
模型参数变化；本笔记不把一个全空间上的变系数 $\lambda(x,y)$ 直接当成
常曲率公式中的常数，也不由此产生新的 tube 结论。

### 5.3 有理算例

令

$$
Q^{(0)}=Q_0(-1,1;1/2,3/2),\qquad
Q^{(1)}=Q_0(-1/2,1/2;3/4,5/4).
$$

它们围绕 $(0,1)$ 严格嵌套。先执行 $X_1$，再执行 $Y_2$，得到

$$
\widetilde Q^{(0)}=Q_2(-1,1;1/4,3/4),\qquad
\widetilde Q^{(1)}=Q_2(-1/2,1/2;3/8,5/8),
$$

仍严格嵌套，包围 $(-1,1/2)$。闭合参数如下：

| 层 | 原参数 | 运输后参数 |
|---|---|---|
| 外层 | $(-4,1/3,4/3,3)$ | $(-8,1/3,8/3,3)$ |
| 内层 | $(-4/3,3/5,4/5,5/3)$ | $(-8/3,3/5,8/5,5/3)$ |

两层都满足 $\alpha\beta+\gamma=0$、$\beta\delta=1$。
此例核对时间顺序和符号；一般证明是命题 5.1，而不是由该有限实例推出。

## 6. Scott 信息域及其邻域表述

### 6.1 明确的完备化

令 $\mathcal I(\mathbb R)$ 为非空有界闭实区间按反包含排序的集合，
$\mathcal I(\mathbb R_{>0})$ 限制为具有正下界的闭区间。定义

$$
D=\mathcal I(\mathbb R)\times\mathcal I(\mathbb R_{>0})
  \times\mathcal I(\mathbb R)\times\mathcal I(\mathbb R_{>0}),
$$

四个分量按 $(\xi,y,\theta,\lambda)$ 排列。它描述这些坐标的有限区间观测，
不是全部表达式历史或全部关系对象的无损编码。

**命题 6.1（PROVED WITH STATED HYPOTHESES）。**
$D$ 是连续 dcpo，定向上确界逐坐标为区间交；
有理端点的非退化外盒构成可数近似基，有限盒 $B$ 严格包围 $C$ 时 $B\ll C$。

**证明。** 对任一非空定向族，选取一个成员后，在其所有细化组成的共尾子族上，
各下端点上升、上端点下降，且始终落在选定的紧区间内。
有限交性质给出非空交；正坐标仍有选定成员提供的正下界。
该交就是反包含序的最小上界。

若 $C$ 严格内含于 $B$，并且一个定向族的交内含于 $C$，逐坐标的严格余量
保证存在有限阶段的端点已进入 $B$；定向性将有限多个要求合并在一个成员中，
故 $B\ll C$。反之，用逐步缩小到 $C$ 的外扩盒检验，缺少某侧严格余量时
不能满足 way-below 条件。所有严格包围 $C$ 的有理盒构成定向族，其交为 $C$，
所以 $D$ 连续且该基可数。证毕。

这也等价于对有理非退化盒的关系
$B\prec C\iff C\subset\operatorname{int}B$
作 rounded ideal completion。有限插值由端点间的有理中间值给出；
参见文末的区间域来源。这里不能把“有理有限表示”直接称为 dcpo 的紧致元：
在此区间域中，一个盒一般不满足 $B\ll B$。

### 6.2 Scott 开集和点空间

若 $U$ 是有理开盒，则

$$
\mathcal O_U=\{K\in D:K\subset U\}
$$

是 Scott 开集，这些集合构成 Scott 拓扑的基。
上闭性由反包含序直接得到；定向不可达性由上述严格余量论证得到。
若 $K$ 属于任一 Scott 开集 $\mathcal V$，它的有理外盒近似族中必有
一个 $B\in\mathcal V$，且 $K\subset\operatorname{int}B$。
于是 $K\in\mathcal O_{\operatorname{int}B}\subseteq\mathcal V$，证明基性质。

$D$ 的极大元是单点盒。把 $\widetilde E$ 经 $\Phi$ 嵌为单点盒，
$\mathcal O_U$ 的拉回恰好是 $\Phi^{-1}(U)$，
故极大元上的相对 Scott 拓扑就是第 4 节构造的通常拓扑。
这不把整个 $D$ 的 Scott 拓扑与值格的 Scott 或 Lawson 拓扑直接等同。

同一理想有多种共尾近似名；不能把每一个任意理想称为一个精确点。
本模型中，只有所有坐标区间均缩为单点的极大理想才对应完整的点状态。
可计算点进一步要求有效的名字；此要求与纯拓扑连续性不同。

### 6.3 包络解释的 Scott 连续性

对闭区间观测 $B=(I,J,T,L)$、加数区间 $S$ 和正乘数区间
$K=[k_-,k_+]$，定义

$$
\widehat{\widetilde X}(B,S)=(I,J,T+S,L),
$$

$$
\widehat{\widetilde Y}(B,K)=(I,J/K,KT,L).
$$

若 $J=[h,H]$，则 $J/K=[h/k_+,H/k_-]$；$KT$ 使用四个端点乘积的最小值和最大值。

**命题 6.2（PROVED WITH STATED HYPOTHESES）。**
这两个包络解释关于输入盒和参数区间联合 Scott 连续，
且在单点状态和单点参数上恢复命题 5.2 的精确作用。

**证明。** 区间加法、乘法及正除法保持集合包含，故两映射单调。
任一定向输入族在选定成员后的共尾部分都有有限端点界，且乘数有共同正下界。
输出端点由有限次加法、乘法、除法和最小/最大值给出，
所以与各端点的定向极限相容。于是逐坐标保持交，即保持定向上确界。
单点情形由公式直接给出。证毕。

固定有理 $s$、$k>0$ 时，两种运输还是基上的可计算序同构，
其逆分别为 $-s$ 和 $1/k$，故给出 Scott 同胚。
对任意固定有限 A/M 词，包络解释的连续性由复合得到；
有限精度算法则逐节点使用有理区间运算。

**关系边界。** 包络不是完整关系像。必须另存同一次乘法的联合条件

$$
y'k=y,\qquad \theta'=k\theta,\qquad
\alpha'=k\alpha,\quad \gamma'=k\gamma,\quad
h'k=h,\quad H'k=H,
$$

各处共用同一个 $k$。例如输入 $y=\theta=1$、$k\in[1,2]$，
精确输出满足 $y'\theta'=1$；包络
$y'\in[1/2,1]$、$\theta'\in[1,2]$ 却包含不满足该关系的点。
因此命题 6.2 是有限盒观测的 Scott 连续性，不是对全部关系语义的完整性定理。

## 7. 与原开放问题的接口及未完成部分

当前结论是：所定义的 $E_0$ 带标记连续族具有有理邻域基、共同细化、
显式观察映射、正仿射生成元的联合连续性及其区间观测的 Scott 连续提升。
度量统一不是这些证明的前提。

对任何已经定义的二元结构操作 $F$，连续性可以约化到基元条件

$$
F(p,q)\in V
\Longrightarrow
\exists U\ni p,\ W\ni q:\ F(U\times W)\subseteq V.
$$

但邻域基本身不定义两个完整表达式之间的接口、复制、共享和拼接规则。
普通有限闭区间上的数值 $+,-,\times$，以及分母区间排除零时的除法，
由同样的端点证明得到 Scott 连续性；dependency 导致的不精确并不构成不连续的反例。
这仍不意味着它们对任意表达式重写或历史商都是同态。

以下问题保持 **OPEN PROBLEM**：

1. 将保留 occurrence、类型化孔、共享参数和历史的结构对象与本信息域连接，
   并指定哪些观察允许遗忘哪些关系。
2. 对一般 tube、奇异层和带孔拼接提供实际的相容局部图及过渡；
   本模型的全局坐标不证明这些对象全局乘积化。
3. 为一般二元结构运算列出生成规则，并逐一证明上述基元条件。
4. 明确与值格 Lawson 拓扑的具体观察或嵌入命题；不写成两个载体的字面拓扑相等。
5. 单独处理零乘数、负乘数和跨零除法的载体及域条件。
   $Y_k$ 在 $k\downarrow0$ 时把 $y$ 送往无穷，不能在当前 $E_0$ 内直接连续补上 $k=0$。
6. 结构尺度、质量与几何度量的实现问题，见 note 04。

参照值在本构造中运输边界方向，不自动给出原 $g_{\mu,\lambda}$ 下新的正交算术标架；
任何相应度量运输需另作定义与验证。本文也不把“所有闭合词的终点算子为恒等”
升级成所有闭合历史相同。

## 8. 来源、归属与验证范围

- **Human origin/direction:** 苑明理提出以同型闭合四边形组织邻域、
  使用参数套与闭合关系、坚持乘法跨层运输，以及让参照值既可保留为叶信息、
  又可通过观察映射遗忘；并指定有理可计算边界和本笔记的保存位置。
- **Model assistance:** ChatGPT / Codex（OpenAI）整理显式坐标构造、证明、
  反例、算例、区间域边界及本文文字。上述自检不构成独立的人类数学审阅。
- **讨论日期：** 2026-11-10。仓库核对基线：
  f1525118d31c656593869feba668ed49c651c61d。
- [Paper 0 AES 与运动](../../paper-0/sections/03-aes-and-motion.tex)：
  基本赋值、正仿射运动、度量与平直极限。
- [Paper III 正则 tubes](../../paper-3/sections/05-regular-tubes.tex)：
  proper tube 的额外假设；本笔记不替代它们。
- [Paper VI](../../paper-6/)：仅借鉴类型化接口与组合的概念，
  不假定一般过程—表达式对应已证明。
- Niels van der Weide and Dan Frumin,
  [The Interval Domain in Homotopy Type Theory](https://nmvdw.github.io/pubs/geuversfest-paper.pdf)，
  §§2–3、5：abstract basis、rounded ideals 与区间运算。
  该版本注明部分区间算术形式化尚有 admitted results；
  本文没有把引用称为整个 AEG 构造的机器证明。

命题中的一般结论依赖正文给出的证明。
有理四边形实例与符号恒等式的重放只用于检查约定、符号和实现，
不替代关于任意定向族的论证。论文正文和状态登记均未在此次笔记中修改。
