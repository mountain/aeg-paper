# Scott/Lawson 拓扑与 Adva 区间词汇的相容性边界

## 有理有限表示、实区间完备化与可执行运算

### Research Note v0.2

**2026-11-10；2026-11-11 核对后续进展并整合**

**地位约定**：本文明确载体后的域论、区间算术与反例标为 `CLASSICAL`，
并给出证明；将这些操作对应到 AEG 固定生成元标为 `REFORMULATION`；
一般表达式结构、邻域质量及其几何实现标为 `STRUCTURAL PROPOSAL` 或
`OPEN PROBLEM`。数学证明不是接收器实现已通过验证的声明。
本笔记不改变 `09`–`20`、论文正文或 governance 中既有 claim status。

修订起点为 `mountain/aeg-paper@52fb677e68709276e4ff5e3b4b1cc23044415423`；
整合前主线为 `74ad9ed82d72239a4263225c73fab2bdd6501a8d`，其中 note 52 原文未变。
本版以 [AES note 03](../aes/03-quadrilateral-neighborhoods-and-scott-continuity.md)
§6 的有限实区间域为主载体，补全有理表示与完备化的接口。
原稿已经区分 dependency 与连续性；本版消除其余章节和问题清单中的冲突。
已合并的 AES note 05 所给具体质量与 valuation 构造见 §6.3；
不把这些已完成的限定模型重新列作未建立，也不外推为一般结构质量定理。

---

## 0. 问题与三个层次

本文区分三种对象：

| 层次 | 对象 | 本文允许的结论 |
|---|---|---|
| 有限表示 | 有理端点闭区间、有限表达式、域证据 | 每一步精确有理运算及有限比较 |
| 完备语义 | 实端点区间构成的连续 dcpo | 任意非空定向族的上确界、Scott 连续性 |
| 有效名字 | 可执行的有理区间细化流及其收敛保证 | 按所需精度计算；不等于任意实数都可计算 |

值格 $L=[0,\infty]$ 仍使用**数值序**；区间域使用**反包含信息序**。
两者不得共用未经说明的“反序”“同构”或“对偶侧”。
有限端点表示、way-below 近似与序论紧致元也不是同一概念。

具体目标是证明：有限有理数据如何提供连续区间域的近似基；
哪些端点操作保持定向上确界；何时倒数封闭；为何 dependency 和固定网格舍入
分别构成不同的边界。Newton 与 exact-zero 仍须使用各自独立的证据。

## 1. 载体、信息序与有理完备化

### 1.1 值格只用于比较

在 $L=[0,\infty]$ 上，Scott 开集为 $\varnothing,L$ 及 $(a,\infty]$
（$0\le a<\infty$）；lower 拓扑由 $[0,b)$（$0<b\le\infty$）生成。
两者的 join 是 $L$ 的通常序拓扑，即含无穷端点的紧化拓扑。

**命题 1.1（CLASSICAL；修正端点例外）。**

$$
a\ll_L b\iff (a=0)\ \text{或}\ (a<b).
$$

对 $0<a<\infty$，$a<b$ 又等价于存在**有限** $s>0$ 使 $a+s\le b$。
不能把后一公式不加限制地用于全部 $L$：$0\ll0$，而 $\infty\not\ll\infty$，
尽管 $\infty+s=\infty$。

**证明。** 底元 $0$ 在任意非空定向集中均已有上界见证。
若 $a<b\le\sup S$，则不可能所有 $s\in S$ 均小于 $a$，故有 $s\ge a$。
若 $a=b>0$ 有限，用严格从下趋于 $a$ 的序列否定 $a\ll a$；
若 $a=b=\infty$，用自然数链否定。$a>b$ 被单元素定向集 $\{b\}$ 排除。
有限平移余量的等价由实数稠密性得到。证毕。

因此 [note 09](09-order-topology-scott-lawson.md) §9 的生成元比较在本文按
上述端点限定引用；本文不继承该笔记其他未在此证明的一般域论断言。

### 1.2 普通算术采用带符号的有限区间

定义

$$
\mathcal I_{\mathbb R}
=\{[l,u]:l,u\in\mathbb R,\ l\le u\},\qquad
\mathcal I_{\mathbb Q}
=\{[p,q]:p,q\in\mathbb Q,\ p\le q\}.
$$

每个区间均为非空、有界、闭区间；后者的端点有理，所表示的集合仍可按实数
解释。实际 Adva profile 的量词范围另见 §5.3。
统一定义

$$
[l,u]\sqsubseteq[l',u']\iff[l',u']\subseteq[l,u]
\iff l\le l'\le u'\le u.
$$

信息增多意味着区间缩小。$\mathcal I_{\mathbb R}$ 没有最小元；本文的 dcpo
只要求**非空**定向集有上确界，不要求最小元。若另需未知对象 $\bot$，
须显式添加并另定运算，不能把报错状态或空区间悄悄当作其中元素。

非负载体对减法不封闭：$[1,2]-[1,2]=[-1,1]$。
所以 §2、§4 的带符号算术全部在 $\mathcal I_{\mathbb R}$ 中进行。

### 1.3 有理区间不是 dcpo

**反例 1.2（CLASSICAL）。** 取

$$
a_n=2^{-n}\lfloor 2^n\sqrt2\rfloor,\quad
b_n=a_n+2^{-n},\quad I_n=[a_n,b_n].
$$

则 $a_n\uparrow\sqrt2$、$b_n\downarrow\sqrt2$，$I_n$ 是有理区间的定向链。
其端点可由整数平方比较计算，不必先计算实数 $\sqrt2$。
若它在 $\mathcal I_{\mathbb Q}$ 中有上界 $J$，则

$$
\varnothing\ne J\subseteq\bigcap_n I_n=\{\sqrt2\},
$$

迫使 $J=[\sqrt2,\sqrt2]$，与端点有理矛盾。故该链甚至没有有理区间上界。
这不是算法精度不足，而是载体没有定向完备性。

### 1.4 实区间域、way-below 与可数基

**命题 1.3（CLASSICAL）。** $\mathcal I_{\mathbb R}$ 是连续 dcpo，且

$$
\bigsqcup_{i\in A}[l_i,u_i]
=\bigcap_{i\in A}[l_i,u_i]
=[\sup_i l_i,\inf_i u_i],
$$

$$
[a,b]\ll[l,u]\iff a<l\le u<b.
$$

所有有理端点非退化区间组成可数近似基
$\mathcal B=\{[p,q]:p,q\in\mathbb Q,p<q\}$。
这里没有任何紧致元：没有 $I\ll I$，包括有理单点区间。

**证明。** 任取非空定向族，固定成员 $I_0$。
满足 $J\subseteq I_0$ 的族内成员构成共尾定向子族。
它们在紧集 $I_0$ 中有有限交性质，故交非空且有界。
原族与共尾子族的交相同，并由反包含序立即验证最小上界公式。

若 $a<l\le u<b$ 且 $[l,u]\sqsubseteq\bigsqcup_i I_i$，
则 $\sup l_i\ge l>a$、$\inf u_i\le u<b$。
各有一个成员见证左、右严格不等式；定向性给出同时满足两者的成员，
因而 $[a,b]\ll[l,u]$。
反过来，$\ll$ 蕴含 $\sqsubseteq$；若 $a=l$ 或 $b=u$，
链 $[l-1/n,u+1/n]$ 的上确界为 $[l,u]$，却没有成员包含于 $[a,b]$。
故两侧必须严格。最后，严格包围 $[l,u]$ 的有理区间组成定向族，
其交恰为 $[l,u]$；两个外近似可用有理中间端点共同严格细化。证毕。

对 $\mathcal I(\mathbb R_{>0})=\{[l,u]:0<l\le u<\infty\}$，同一证明成立：
共尾子族有 $I_0$ 提供的正下界。有限乘积逐坐标成立。
这就是 AES note 03 §6 的

$$
D=\mathcal I_{\mathbb R}\times\mathcal I(\mathbb R_{>0})
\times\mathcal I_{\mathbb R}\times\mathcal I(\mathbb R_{>0})
$$

所需的严格载体，坐标仍按 $(\xi,y,\theta,\lambda)$ 排列。

### 1.5 用严格近似关系重建完备化

在 $\mathcal B$ 上定义

$$
B\prec C\iff C\subset\operatorname{int}B.
$$

定义 rounded ideal 为非空子集 $A\subseteq\mathcal B$，满足：
（i）$B\prec C\in A$ 蕴含 $B\in A$；
（ii）任意 $B,C\in A$ 都有 $E\in A$ 使 $B\prec E$ 且 $C\prec E$。
（ii）取 $B=C$ 已包含 roundedness。理想按包含排序。

**命题 1.4（CLASSICAL）。** 以下互逆映射给出序同构：

$$
I\longmapsto A_I=\{B\in\mathcal B:I\subset\operatorname{int}B\},
\qquad A\longmapsto\bigcap_{B\in A}B.
$$

因此这里的 rounded ideal completion 恰为 $\mathcal I_{\mathbb R}$。

**证明。** 有理端点插值证明 $A_I$ 满足（i）（ii），且 $\bigcap A_I=I$。
任一 $A$ 在反包含序下定向，故命题 1.3 给出非空有限区间 $I=\bigcap A$。
对 $B\in A$，选择 $B\prec E\in A$，得到 $I\subseteq E\subset\operatorname{int}B$，
所以 $A\subseteq A_I$。
若 $I\subset\operatorname{int}B$，端点的严格余量及定向性给出 $E\in A$
使 $E\subset\operatorname{int}B$；于是 $B\prec E$，由（i）得 $B\in A$。
因此 $A=A_I$。$I\supseteq J$ 当且仅当 $A_I\subseteq A_J$，证明序同构。证毕。

不能用仅按 $\sqsubseteq$ 作的普通理想完备化替代上述构造：普通理想完备化中，
每个主理想是紧致元，因为它若包含于定向理想之并，其生成元已出现在某个成员中。
命题 1.3 中却没有紧致元；二者不是同一个完备化。

数学上所有上述理想都被纳入；可执行名字只覆盖其中的有效对象。
对一个点，可要求算法按输入 $n$ 返回包含该点、宽度不超过 $2^{-n}$ 的有理区间，
并通过有限交使名字嵌套。给定有效嵌套流及宽度趋零保证时，也可搜索达到目标精度的阶段。
任意实点虽有这样的数学近似族，却未必有生成它的算法。
一个不缩成单点的理想表示部分区间信息，不表示已知的精确点。

## 2. Scott/Lawson 拓扑与判断的精确位置

### 2.1 区间对象与开邻域

**命题 2.1（CLASSICAL）。** 对有理 $p<q$，

$$
\mathcal O_{p,q}=\{[l,u]:p<l\le u<q\}
$$

构成 $\mathcal I_{\mathbb R}$ 的 Scott 拓扑基。
极大元恰为 $[x,x]$；映射 $x\mapsto[x,x]$ 将实数通常拓扑同胚到极大元的
相对 Scott 拓扑。

**证明。** $\mathcal O_{p,q}$ 上闭；若定向上确界在其中，端点严格余量给出
有限阶段已在其中。若 Scott 开集 $V$ 含 $I$，有理外近似族的上确界是 $I$，
故有 $B=[p,q]\in V$ 且 $I\subset\operatorname{int}B$。
由上闭性 $I\in\mathcal O_{p,q}\subseteq V$，证明基性质。
单点区间恰为极大元，$\mathcal O_{p,q}$ 在其上的拉回为 $(p,q)$。证毕。

这提供了**点空间的同胚**，不是整个区间域与值格的字面拓扑相等。
例如 $0<1$，但 $[0,0]$ 与 $[1,1]$ 在信息序中不可比；单点映射不是从
数值序到反包含序的单调映射。区间 $[l,u]\subset\mathbb R$ 是闭约束，
而 $\mathcal O_{p,q}\subset\mathcal I_{\mathbb R}$ 是一族信息对象；二者类型不同。

**命题 2.2（CLASSICAL）。** $\mathcal I_{\mathbb R}$ 的 Lawson 拓扑恰为
端点三角域 $\{(l,u)\in\mathbb R^2:l\le u\}$ 的通常子空间拓扑。

**证明。** Scott 基元为端点严格不等式，lower 开子基
$\mathcal I_{\mathbb R}\setminus\uparrow[a,b]=\{l<a\ \text{或}\ u>b\}$
也在端点拓扑中开，故 Lawson 不更细。
反之，在 $[l,u]$ 的任一端点邻域内取 $\varepsilon>0$ 使对应端点矩形内含。
先取 Scott 邻域 $l'>l-\varepsilon,u'<u+\varepsilon$；
再排除 $\uparrow[l+\varepsilon,B]$ 与 $\uparrow[A,u-\varepsilon]$，
其中 $B>u+\varepsilon,A<l-\varepsilon$。
所得 Lawson 邻域额外满足 $l'<l+\varepsilon,u'>u-\varepsilon$，落在该矩形内。
故两拓扑相同。证毕。

### 2.2 区间判断不全是同一种拓扑性质

仅对**已经有健全区间结果**的情形，定义

$$
P=\{[l,u]:l>0\},\quad M=\{[l,u]:u<0\},\quad
Z=\{I:0\in I\},\quad E=\{[0,0]\}.
$$

**命题 2.3（CLASSICAL）。** $P,M,P\cup M$ 是 Scott 开集；$Z$ 是 Scott 闭集；
$E$ 不是 Scott 开集，也不是 Scott 闭集，但为 Lawson 闭集。
$Z\setminus E$ 既非 Scott 开集也非 Scott 闭集。

**证明。** 严格正负条件上闭，并由端点上确界/下确界的严格余量在有限阶段见证。
$Z$ 是 $P\cup M$ 的补集。
链 $[-1/n,1/n]$ 的上确界为 $[0,0]$，没有成员在 $E$，所以 $E$ 不开；
它不下闭，故不 Scott 闭。它在端点拓扑中为单点闭集，故 Lawson 闭。
$Z\setminus E$ 不是上闭的，例如 $[-1,1]\sqsubseteq[1/2,1]$；
同一趋零链又证明它不对定向上确界封闭。证毕。

因此 `StrictPositive`/`StrictNegative` 的纯区间条件是 Scott 开性质；
`ExactZero` 和 `ZeroUndetermined` 不能概括成“所有 judgment 都不是开集”。
分母包含零时的 `UnknownDomain` 是求值器的域阻塞状态；其局部触发条件是 $Z$，
进一步细化可能解除它。它不证明真实函数有极点，也不是数值区间的另一个元素。

## 3. 平移、缩放与倒数：必须说明在哪个载体上

### 3.1 有限带符号区间上的生成元

令 $s\in\mathbb R$ 有限，$0<k<\infty$，并定义

$$
T_s([l,u])=[l+s,u+s],\qquad D_k([l,u])=[kl,ku].
$$

**命题 3.1（CLASSICAL；AEG 对应为 REFORMULATION）。**
$T_s,D_k$ 是 $\mathcal I_{\mathbb R}$ 上的序自同构，因而是 Scott 同胚。
其逆分别是 $T_{-s},D_{1/k}$。参数有理时，它们及其逆可在有理端点层面精确执行。

**证明。** 端点不等式保持且反映包含；逆公式成立。
序同构将任意上确界及其最小性运输为上确界，故正反映射都保持定向上确界。证毕。

定义普通倒数的域

$$
\mathcal U_0=\{[l,u]\in\mathcal I_{\mathbb R}:0\notin[l,u]\}
=\{u<0\}\cup\{l>0\}.
$$

**命题 3.2（CLASSICAL）。** $\mathcal U_0$ 为 Scott 开子 dcpo，且

$$
\rho([l,u])=[1/u,1/l]
$$

是 $\mathcal U_0$ 上的**保序对合**，从而是 Scott 到 Scott 的同胚。
其 Scott 拓扑也等于环境域的相对 Scott 拓扑。

**证明。** 开性由命题 2.3；定向族固定一个成员后的共尾部分在同一符号侧，
并有该成员提供的正距离零下界，故交仍在 $\mathcal U_0$。
倒数把每个区间作为集合映到相应倒数区间，因此保持并反映包含，且 $\rho^2=\mathrm{id}$。
零外区间可以选择仍排除零的严格有理外近似，故命题 2.1 的局部基证明也适用，
给出子域与相对 Scott 拓扑的一致。证毕。

例如 $[1,3]\sqsubseteq[1,2]$ 给出 $[1/3,1]\sqsubseteq[1/2,1]$，
方向未反转。数值序中的 $x\mapsto1/x$ 反序，不意味着区间信息序反序。
“倒数交换端点角色”与“倒数把 Scott 送往 lower”是不同命题，后者只适用于
已指定的数值序情形，不能搬到这里。

### 3.2 原非负扩张载体的边界

为与 note 09 比较，另记

$$
\mathcal E=\mathcal I([0,\infty])
=\{[l,u]:0\le l\le u\le\infty\},
$$

其中区间按紧化序拓扑理解，允许 $[\infty,\infty]$。
它不承担本文的减法或任意扩张实数乘除法。

**命题 3.3（CLASSICAL）。** $\mathcal E$ 是连续 dcpo，定向上确界为交，且

$$
[a,b]\ll_{\mathcal E}[l,u]
\iff (a=0\ \text{或}\ a<l)\ \text{且}\ (b=\infty\ \text{或}\ u<b).
$$

**证明。** $[0,\infty]$ 通过 $t\mapsto t/(1+t)$、$\infty\mapsto1$ 同胚且序同构于
$[0,1]$。紧性与定向有限交性质给出交及其上确界性质。
右式正是 $[l,u]\subset\operatorname{int}_{[0,\infty]}[a,b]$；严格余量证明充分性。
必要性先由 $\ll$ 蕴含 $\sqsubseteq$ 得到包含关系。
若有限左边界 $a>0$ 与 $l$ 相等，向左外扩逼近 $[l,u]$ 否定 way-below；
若 $a=l=\infty$，用 $[n,\infty]$。有限右边界 $b=u$ 用向右外扩同样否定。
有理端点与边界 $0,\infty$ 提供定向外近似基，证明连续性。证毕。

因此 $\mathcal E$ 的底元 $[0,\infty]$ 是紧致元；这与
$\mathcal I_{\mathbb R}$ 没有紧致元不冲突，载体不同。
极大元上的相对 Scott 拓扑恢复 $L$ 的通常序拓扑，即 §1.1 的 Lawson 拓扑：
证明与命题 2.1 相同，只须使用 $L$ 的相对开区间。

在 $\mathcal E$ 上，有限 $s\ge0$ 的 $T_s$ 是序嵌入，像恰为
$\mathcal I([s,\infty])$，只对该像为序同构；$s>0$ 时 $[0,0]$ 没有原像。
平移保持端点定向极限，故仍 Scott 连续；不能称为整个 $\mathcal E$ 的自同胚。
有限 $k>0$ 的 $D_k$ 才是整个 $\mathcal E$ 的序自同构。

对普通倒数，仅要求 $0\notin I$ 不保证扩张载体中的域封闭：

$$
[1,\infty]\longmapsto[0,1],\qquad
[\infty,\infty]\longmapsto[0,0].
$$

若要在正区间上保留普通倒数的自映射对合，必须限制为 $0<l\le u<\infty$。
另一种**不同语义**是显式规定 $r(0)=\infty,r(\infty)=0$，
并对全部 $\mathcal E$ 定义 $\rho_e([l,u])=[r(u),r(l)]$。
由于 $r$ 是 $L$ 的双射，$\rho_e$ 保持并反映集合包含，是信息序的保序对合。
这不能被解释为 Adva 普通算术已允许除零。

## 4. 项级运算：连续性与依赖性分别判断

### 4.1 精确区间原语的 Scott 连续性

对 $I=[a,b],J=[c,d]$ 定义

$$
I+J=[a+c,b+d],\qquad I-J=[a-d,b-c],
$$

$$
I\cdot J=[\min(ac,ad,bc,bd),\max(ac,ad,bc,bd)],
\qquad I/J=I\cdot\rho(J)\quad(J\in\mathcal U_0).
$$

**命题 4.1（CLASSICAL）。** $+,-,\cdot:\mathcal I_{\mathbb R}^2\to\mathcal I_{\mathbb R}$
及 $/:\mathcal I_{\mathbb R}\times\mathcal U_0\to\mathcal I_{\mathbb R}$ 联合 Scott 连续。
这里使用精确端点公式，不包含固定网格舍入、溢出截断或预算中止。

**证明。** 每个公式都是独立操作数矩形 $I\times J$ 的真实值域：
加减取相应端点；双线性乘法在矩形上的极值在角点；倒数在每个零外区间上
连续且单调，除法归于乘法。连续函数将连通紧矩形映为闭区间，故极值之间没有遗漏。
缩小矩形只缩小真实值域，因此各原语对信息序单调。

任取定义域中的非空定向族。选定一个输入对后，在其共尾细化族中，
所有端点有共同有限界，左端点单调上升，右端点单调下降；除法的分母还有
共同的零外距离 $\delta>0$。这些端点作为同一索引集上的网收敛到上确界输入
的端点：任意有限组误差要求可由定向性同时达到。
加、减、乘、有限 min/max 及零外倒数是这些端点的通常连续函数，
所以输出端点极限等于把公式作用于输入端点极限。
输出族又已单调，故其区间交恰为上确界输入的输出。这证明保持定向上确界。证毕。

**推论 4.2（CLASSICAL）。** 任意固定有限表达式/DAG 的自然区间解释，
在“逐节点分母区间都排除零”的成功定义域内 Scott 连续；该定义域为 Scott 开集。

**证明。** 变量投影、常值映射和对角映射 $I\mapsto(I,I)$ 都保持定向上确界。
按有限求值次序复合命题 4.1。遇除法时，成功域再与分母映射下
$\mathcal U_0$ 的原像相交；由归纳得到 Scott 开性。该开子域的定向上确界与环境一致，
连续性在限制与复合中保持。证毕。

**健全性也须单独陈述。** 对成功求值的输入盒及其中任一实赋值，
变量和常数落在各自叶子区间内；若子表达式真值已落在子区间内，
命题 4.1 的矩形值域公式就包含父节点真值。
分母区间排除零保证该次实际除法有定义。对有限节点归纳得到
$t(x)\in\widehat t(B)$，即使共享变量使合法操作数对只占矩形的一个子集。

重复变量的对角映射连续，不意味着后续区间原语保留了两个 occurrence 必须相等的关系。

### 4.2 dependency 的正确反例

令 $I=[1,2]$。自然区间求值给出

$$
I-I=[-1,1],\qquad I/I=[1/2,2],\qquad I+[0,0]=I.
$$

但对同一个实变量 $x\in I$，$x-x$ 的真实像为 $\{0\}$，$x/x$ 的真实像为 $\{1\}$。
自然区间求值每次原语使用整个操作数矩形，包含了非对角的组合，因而失去精度。
它没有记录或恢复完整的依赖关系。

**反例 4.3（CLASSICAL）。** 自然区间解释不下降为按实函数恒等式取商后的同态。
若能够下降，实函数恒等的表达式 $x-x$ 与常数 $0$ 应给出相同区间，
与上述 $[-1,1]\ne[0,0]$ 矛盾。$x/x$ 与 $1$ 给出第二个反例，域条件是 $x\ne0$。

这个结论不否定三件事：原语对**独立矩形**的值域精确性；
解释器在成功求值范围内对未取商的表达式语法按节点构造的性质；
命题 4.1–4.2 的 Scott 连续性。
因此不能笼统写“项级加法不是同态”，更不能以 $x-x$ 推出不连续。

有直接的收敛例子：$I_n=[1,1+1/n]$，则

$$
I_n-I_n=[-1/n,1/n]\uparrow_{\sqsubseteq}[0,0],
$$

$$
I_n/I_n=[n/(n+1),(n+1)/n]\uparrow_{\sqsubseteq}[1,1].
$$

有限阶段不精确与定向极限相容可以同时成立。
Adva 选定解释器的 trace 不能被无声替换成符号化简结果；接受化简需要另有受检证明与 profile。

## 5. 有限可执行操作、舍入及有效性

### 5.1 哪些工作不需要完成无限对象

**命题 5.1（CLASSICAL）。** 有理输入上的 $+,-,\cdot$、零外倒数/除法，
有理参数的平移/正缩放、包含/严格内含比较、有限区间交的相容性检查，
均可用有限次整数运算精确执行。非空有限交仍有有理端点；空交作为不相容结果另行报告。

**证明。** 有理数的四则运算在非零除数下封闭；顺序比较归于正分母交叉相乘；
有限 min/max 从有限多个有理数中选取。含零与否由端点符号决定。
交集端点为最大左端点和最小右端点；前者大于后者时交为空。证毕。

这不意味着有限有理表达式能输出 $[\sqrt2,\sqrt2]$。
无穷交、任意定向上确界和全体 rounded ideals 属于完备化语义。
可计算无理点通过有效近似名参与计算；一般实参数本身不自动可计算。

对有理系数有限表达式和有效点名字，若每个实际除数都非零，则不断细化输入区间
最终能在所有除法节点取得零外证据：在该点附近，有限个端点运算通常连续，
单点输出等于真实子表达式值，非零值有正余量；逐节点归纳给出一个成功邻域。
在成功域内，推论 4.2 保证输出细化到真实点值。
可以搜索输出宽度达到给定精度的阶段，但此论证不提供统一时间界，
也不保证受固定预算约束的接收器完成该搜索。

### 5.2 固定网格舍入：健全、单调，但一般不 Scott 连续

对固定正整数 $N$，外向舍入为

$$
Q_N([l,u])=
\left[\frac{\lfloor Nl\rfloor}{N},\frac{\lceil Nu\rceil}{N}\right].
$$

**反例 5.2（CLASSICAL）。** 作为 $\mathcal I_{\mathbb R}\to\mathcal I_{\mathbb R}$
的映射，$Q_N$ 健全且信息序单调，但不 Scott 连续。

**证明。** $Q_N(I)\supseteq I$；floor/ceil 的单调性证明它保持信息序。
对有理链 $I_n=[-1/(Nn),1/(Nn)]$，

$$
\bigsqcup_n I_n=[0,0],\qquad Q_N(I_n)=[-1/N,1/N]\quad(n\ge1),
$$

而 $Q_N([0,0])=[0,0]$，故不保持该定向上确界。证毕。

该链及其上确界甚至全部有理；所以 $Q_N$ 在有理表示层也不保持所有已存在的
定向上确界，不能仅以“实现层不含无理数”回避这个反例。

所以“原语精确区间解释 Scott 连续”不能升级为
“逐节点采用固定网格外向舍入的实际解释器 Scott 连续”。
固定网格自身的离散载体可以另作序论分析，但不能替代到实区间域的延拓结论。

若另选无界细化网格 $N_n\mid N_{n+1}$、$N_n\to\infty$，
则嵌套输入的单步 $Q_{N_n}(I_n)$ 仍嵌套；两侧舍入误差均小于 $1/N_n$，
因此其极限与精确端点极限一致。有限表达式在共同有限界、分母共同排除零的
阶段以后，也可逐节点用端点连续性与消失的舍入误差证明同样的收敛结论。
这是带额外精度策略的结论，不是固定网格反例的撤销。

### 5.3 与当前 Adva profile 的接收边界

固定读取的
[Adva interval README](https://github.com/mountain/adva/blob/17e1842addcd9f9262eef87bd19c5eabcdc843e1/experiments/interval_enclosure/README.md)
规定：`exact-rational` 不舍入；`outward-grid` 在叶子和每个运算节点都舍入，
网格 $N\in\{1,2,4,8,16,32,64\}$；数学量词范围为输入盒内的全部有理赋值。
该 profile 还有节点、深度、整数位数和工作量限制，且不自动细化网格。

本文精确端点公式的健全性证明同样适用于实赋值，但这不改变该 profile 的接收合同。
它所允许的有限网格集合不支持 $N\to\infty$；理论上需要的无界精度流不能直接
宣称已被这个有限接收器实现。`UnknownDomain`、`UnknownBudget` 与成功区间输出
也不是同一类对象，若要把全部状态组成 dcpo，须先定义状态序及证明映射性质。

## 6. exact-zero 与邻域质量的边界

### 6.1 零值证明需要额外离散信息或恒等式

**命题 6.1（CLASSICAL；exact-zero bridge）。** 若

$$
R=N/D,\qquad N,D\in\mathbb Z,\qquad 0<D\le B<\infty,
$$

且已严格认证 $|R|<1/B$，则 $R=0$。

**证明。** 若 $N\ne0$，则 $|N|\ge1$，从而 $|R|\ge1/D\ge1/B$，矛盾。证毕。

$N$ 的整性、分母上界和严格不等式缺一不可。一般实残量没有这个结论。
健全的有理包络 $[l,u]\subset(-1/B,1/B)$ 可提供严格残量证据；
区间仅含 $0$，或浮点数看起来很小，都不能替代它。

这与 $\{[0,0]\}$ 非 Scott 开并不矛盾：bridge 引入了额外的离散间隙证据，
不再只使用任意实数近似流。有限有理端点 $l=u=0$ 也可作有限符号比较，
但不能据此判定任意有效实数名字是否表示零。
若有独立受检的符号恒等式，也可证零；该证明与指定区间 trace 必须分别登记。

### 6.2 宽度与尺度：可证的部分

**命题 6.2（CLASSICAL）。** 令 $w([l,u])=u-l$，值域取反向数值序
$([0,\infty],\ge)$。则 $w$ Scott 连续，且

$$
w(T_sI)=w(I),\qquad w(D_kI)=k\,w(I)\quad(k>0),
$$

$$
w(\rho I)=\frac{w(I)}{|lu|}\quad(0\notin I).
$$

**证明。** 包含细化使宽度不增；对定向族，端点共同趋于其上下极限，
$w(\bigcap I_i)=\inf_i w(I_i)$。后三式由端点公式直接计算，
零外区间的 $lu>0$。证毕。

这里的宽度是给定坐标中的不确定性指标，不是由 Scott 拓扑唯一选出的量。
这里的 $D_k$ 也是数值区间缩放，不能与 AES 的几何运动
$Y_k(x,y)=(x,y/k)$ 混为一谈；后者还须运输相关标记，且 $k\downarrow0$
时 $y/k$ 可能逃向无穷。本文不由数值乘法的连续性给 AES 补上零乘数。
有限维盒的逐坐标宽度可同时控制点近似；仅控制体积则不足。
例如

$$
K_n=[-1,1]\times[-1/n,1/n],\qquad
\operatorname{Area}(K_n)=4/n\to0,
$$

但交为 $[-1,1]\times\{0\}$，并未缩成一点。这是普通欧氏面积的反例，
没有给一般 AES 定义面积或质量。

**STRUCTURAL PROPOSAL。** 可将“邻域质量”作为与细化、有限分割和运输相容的
额外赋值，但必须先规定它的定义域、值序、归一化及所需的加性/连续性。
若讨论开集上的连续 valuation，还须另列空集值、单调性、模律和定向并连续性；
若讨论闭邻域上的质量沿收缩的极限，则涉及另一组条件。
不得将宽度的命题自动转写为这些赋值已经存在、唯一或可计算。

**OPEN PROBLEM。** 结构质量与几何面积、长度、度量的实现及标定，仍按
[AES note 04](../aes/04-structural-data-metric-unification-and-catenoid.md)
处理。该笔记的相同面积密度/不同度量反例说明额外标定的重要性。
本次修订支持先建立细化与连续性，再研究质量实现；不以一般结构上的测度已成立为前提。

### 6.3 与已合并 AES note 05 的具体构造相衔接

**REFORMULATION（明确模型的已有进展）。**
[AES note 05](../aes/05-measure-probability-information-and-area.md) §5 已在
所选正仿射实群上，利用左 Haar 密度 $dx\,dy/y^2$ 定义四边形质量

$$
m_A(Q_\theta(\ell,r;h,H))
=(r-\ell)\left(\frac1h-\frac1H\right),\qquad \ell\le r,\quad 0<h\le H<\infty.
$$

其 §9.1 证明固定叶上闭盒的质量作为到反向数值序的映射 Scott 连续；
§9.2 又通过固定叶到 $D$ 极大元的连续嵌入 $i_{\theta,\lambda}$，构造

$$
\nu_D(\mathcal U)
=\mu_L\bigl(i_{\theta,\lambda}^{-1}(\mathcal U)\bigr)
$$

这个 Scott 开事件上的连续 valuation，也可先在有限正质量窗口中归一化为概率。
闭盒收缩的极限使用质量下确界，开事件定向并使用质量上确界；二者的序不同。
上述具体构造及其证明与本文相容，不依赖有理端点集合本身已经定向完备。
一般带孔、带历史或跨叶对象的质量选择、粘合、有效性及度量统一仍保持开放。

## 7. Newton 方法：存在性证明与 exact-zero 分开

### 7.1 明确的区间 Newton 命题

本节仅整理数学合同，不重新认证 C11 的实现或运行记录。
Newton 与 Krawczyk 是不同的算子；本文为原稿的 Newton 公式明确假设。

**命题 7.1（CLASSICAL）。** 设 $X\subset\mathbb R^m$ 为非退化紧盒，
$F$ 在 $X$ 的开邻域上为 $C^1$，$c\in X$。
设区间矩阵 $\boldsymbol J$ 包含全部 $DF(x)$，$x\in X$，并且其中
**每个矩阵都可逆**；$\boldsymbol f$ 包含真实 $F(c)$。
令经认证的区间盒 $\boldsymbol N$ 包含集合

$$
\{c-A^{-1}v:A\in\boldsymbol J,\ v\in\boldsymbol f\}.
$$

则：

1. $X$ 中每个零点均在 $\boldsymbol N$ 中。
2. 若 $\boldsymbol N\subseteq X$，则 $X$ 中存在唯一零点；严格内含是常用充分条件。
3. 若 $\boldsymbol N\cap X=\varnothing$，则 $X$ 中没有零点。

**证明。** 对 $z\in X$，平均 Jacobian

$$
A_z=\int_0^1 DF(c+t(z-c))\,dt\in\boldsymbol J
$$

满足 $F(z)-F(c)=A_z(z-c)$。若 $F(z)=0$，则
$z=c-A_z^{-1}F(c)\in\boldsymbol N$，证明 1、3。
若 $\boldsymbol N\subseteq X$，连续映射 $P(z)=c-A_z^{-1}F(c)$ 将 $X$ 映入自身，
Brouwer 定理给出不动点；代入平均值等式得到零点。
两个零点之间也有属于 $\boldsymbol J$ 的平均 Jacobian，其可逆性迫使两点相等。证毕。

二维时，健全的行列式区间排除零可认证矩阵族全部可逆；
只有中心矩阵可逆或近似逆存在不够。$\boldsymbol J^{-1}$ 若出现于实现，
必须是整个逆矩阵族的健全包络，不能只是逐项求倒数。
使用 Krawczyk 时须另写其算子和相应假设，不能只引用同一个 `contracted` 标志。

### 7.2 正确的结果分类

- $\boldsymbol N$ 未能内含、可逆性未认证或预算耗尽：本次证据给 `RootUnknown`。
- **认证的** $\boldsymbol N\cap X=\varnothing$：命题 7.1 给 `RootExcluded`。
- 健全 $F(X)$ 包络排除零向量：也给 `RootExcluded`。
- $F(X)$ 包络含零：本身不证明存在根。
- 内含与排除结论均依赖真实 $F(c)$、全盒 Jacobian 以及同一个输入盒的健全包络。

原稿把“Newton 像与原盒交为空”也列为只能未知，须据命题 7.1 删除该说法。
若输入包络未受认证，既不能用内含证存在，也不能用空交证不存在。
浮点 seed 可以选择一个随后按精确端点解释和检查的盒；
seed 未经认证的近似误差不能被当作根误差界。

### 7.3 状态及 C11 的历史例子

```text
ZeroStatus  = ExactZero | ZeroUndetermined | StrictPositive | StrictNegative | UnknownDomain
RootStatus  = RootExists | RootExcluded | RootUnknown
```

这些是应用层状态名，不是本文给出的新 dcpo。
`RootExists` 不等于“对整个盒的残量求值返回 `[0,0]`”；
有效的存在性证书完全可以与盒上 `ZeroUndetermined` 并存。
认证应明确对象是区间包络、零点存在性、恒等式还是周期轨道，不能互相代替。

原 v0.1 记录过 `contracted=true`，但最终结果报告

```text
x(T)     = -5.2e-7
y(T)-y0  =  5.1e-7
```

并称两者区间均不含零。本次只保留该历史报告，未独立重放其原始证据。
若这些确为同一 $F$、同一盒及同一时间上的健全区间排除，同时又有命题 7.1
的有效内含证书，则两者矛盾，该组合证据应标 `InvalidWitness`。
若这里只是显示的近似中心值，没有区间端点，则尚不能据此判定“排除零”。

可能的检查项仍是：$F(c)$ 或 Jacobian 来源不健全、tube 重定心错误、
最终 state 与 Newton 盒/时间不一致，或区间取点错误。
它们是待核验路径，不是本次已定位的实现缺陷。

### 7.4 合同需要保留的证据

**STRUCTURAL PROPOSAL。** 对需要 tube 的 C11 证书，建议分别携带：

1. 从已绑定输入重放所得的 $F(c)$、全盒 Jacobian 及其健全性证据；
2. 同一盒上的 Newton 算子、可逆性证据与内含或排除检查；
3. `RootStatus` 与 `ZeroStatus`，以及每项被认证的具体命题；
4. 与 C11 目标对应的额外证据：例如根所在的认证盒内含于允许目标集，
   或另有能锁定目标根的证明；仅仅两个盒相交不足以认定根就在目标集；
5. 若主张周期性、最小周期或横截性，须分别提交相应证据。

`InvalidWitness`、缺失的必要来源或 `RootUnknown` 不能被写成已证存在。
但 `ZeroUndetermined` 本身不是健全包络或有效存在性证书失败的理由。

## 8. 对 C11 的后果与本次验证范围

原 v0.1 还记录了

```text
delta_y              = [+/- 1.9e-5]
horizontal_residual  = [+/- 1.2e-4]
```

仅按这两个包络，它们的零状态仍是 `ZeroUndetermined`；既不是 exact-zero 证明，
也没有单独证明或否定周期轨道存在。
若 tube 的健全来源尚未认证，Newton 的代数内含不能独自证明 `RootExists`。

本次不更新 C11 的项目状态；这些数值和 tube replay 缺口是原稿的历史记录，
不是本次对当前实现的独立核查。判断当前状态须读取对应版本、合同和可重放证据。

## 9. 修订后的使用边界

| 不可使用的推断 | 正确边界 |
|---|---|
| 有理区间集合已经是连续 dcpo | 有理区间是有限表示；§1 给出其指定的完备化 |
| 有理有限表示就是紧致元 | $\mathcal I_{\mathbb R}$ 没有紧致元；严格外包含才给 way-below |
| $T_s$ 是整个非负扩张区间域的自同构 | $s>0$ 时仅为到其像的序同构；带符号有限载体上才有平移逆 |
| 区间倒数在信息序上反序 | 普通零外倒数为保序对合；扩张端点另有域约定 |
| dependency 说明区间运算不连续 | 精确原语及成功域上的有限项解释 Scott 连续，但一般不保持实函数恒等式商 |
| 健全外向舍入必然 Scott 连续 | 固定网格 $Q_N$ 有 §5.2 的反例 |
| 所有区间判断都不是开性质 | 严格正负与排除零是 Scott 开性质；精确零不是 |
| 质量趋零已经给出完整邻域基 | 还须控制各相关方向、细化与共尾性，不能只看一个标量 |
| Newton 检查未通过就能排除根 | 未决不能排除；但受认证的空交确能排除 |
| `RootExists` 必须使整个盒残量为 `[0,0]` | 存在性与整个盒上的区间零状态是不同命题 |

## 10. 开放问题清单：保留原编号，明确已答范围

- **Q1 — 本文载体已答（CLASSICAL）**：$\mathcal I_{\mathbb R}$、正有限区间、
  有限乘积及 $\mathcal E$ 的 dcpo/连续性、交与有理近似基见 §1、§3。
  有理有限表示本身不是 dcpo。其他奇异层或结构对象的完备化仍待定义。
- **Q2 — 部分 REFORMULATION，其余 OPEN PROBLEM**：数值区间的固定平移、
  正缩放与零外倒数已在 §3 对应。若要“函子”结论，须先指定两侧范畴、态射、
  接口和关系保留条件，不能仅凭端点公式称满或忠实。
- **Q3 — 精确有限项连续性已答（CLASSICAL）**：见 §4；固定网格延拓不连续见 §5。
  对所有实函数恒等式取商后的自然区间同态性已被反例否定，不能继续列为可能成立的猜想。
  选择哪些受检重写、关系域或共享语义能改善精度，仍为 OPEN PROBLEM。
- **Q4 — 纯区间谓词已答（CLASSICAL）**：见 §2、§6。
  带来源、预算、报错和证明对象的完整状态空间及其序论接口仍为 OPEN PROBLEM。
- **Q5 — 合同设计 OPEN PROBLEM**：分别指定 C11 需要的恒等式、存在性与误差界；
  给 exact-zero 时须提供受检恒等式、单点包络或适用的离散间隙证据。
- **Q6 — 点空间拓扑已答，一般观察接口 OPEN PROBLEM**：极大元上的相对 Scott
  拓扑恢复通常点拓扑；$\mathcal E$ 的极大元恢复 $L$ 的 Lawson 拓扑。
  一般表达式历史/关系的观察映射及其忠实性不由该结果推出。
- **Q7 — OPEN PROBLEM（实现验收）**：指定并重放 Newton 所用 $F(c)$、
  全盒 Jacobian 与 tube 来源；本次不把数学定理当作实现已验收。
- **Q8 — STRUCTURAL PROPOSAL / OPEN PROBLEM**：按 §7 分离零状态、根状态、
  来源有效性与目标命题，落实并验证证书 schema。
- **Q9 — OPEN PROBLEM（质量与尺度）**：给出结构质量的定义、细分与运输规律、
  有效性及几何实现条件；与 AES note 04 联动，不从宽度直接推出测度结构。
  AES note 05 的指定 Haar 质量与固定叶 valuation 已有构造和证明，见 §6.3；
  开放的是其一般结构推广及选择条件，不是该限定实例的存在性。

## 11. 交叉引用、来源与归属

1. [analysis note 09](09-order-topology-scott-lawson.md) §9：值格生成元的背景；
   本文 §1.1 明确其 way-below 公式的底元与无穷端点例外。
2. [analysis note 10](10-scott-lawson-on-paper-1-main-body.md)：既有生成元与主文边界背景；
   本文不改变其 claim status。
3. [AES note 03](../aes/03-quadrilateral-neighborhoods-and-scott-continuity.md) §§6–7：
   四坐标区间域、有理严格外近似、Scott 连续性及关系保留边界。
4. [AES note 04](../aes/04-structural-data-metric-unification-and-catenoid.md)：
   结构质量、尺度与度量实现的开放问题及非唯一性反例。
5. [Adva interval enclosure](https://github.com/mountain/adva/blob/17e1842addcd9f9262eef87bd19c5eabcdc843e1/experiments/interval_enclosure/README.md)：
   本次固定读取的有限接收合同、两种舍入模式及 dependency 例子。
6. [Adva exact-zero bridge](https://github.com/mountain/adva/blob/17e1842addcd9f9262eef87bd19c5eabcdc843e1/docs/research/simplex-contraction-pascal-calabi-reduction.md)：
   原 note 52 所引的算术间隙背景；本文命题 6.1 自含证明。
7. Samson Abramsky and Achim Jung, *Domain Theory*, Handbook of Logic in Computer Science 3,
   1994，[修订版](https://cs.uwaterloo.ca/~david/cs442/domain-theory.pdf) §2.2.6：
   abstract basis 与 rounded ideal completion 的标准框架。
8. Niels van der Weide and Dan Frumin,
   [The Interval Domain in Homotopy Type Theory](https://nmvdw.github.io/pubs/geuversfest-paper.pdf)，
   §§2–3、5：有理区间基、rounded ideals 与区间运算背景。
   本文使用经典实数语义并给出独立的显式证明，不将该引用当作本笔记的机器验证。
9. Andrej Bauer and Iztok Kavkler,
   [A Constructive Theory of Continuous Domains Suitable for Implementation](https://math.andrej.com/wp-content/uploads/2008/01/constructive-domains.pdf)，
   §§3、7–8：有效近似与实现的背景；其构造性基础约定不自动等同于本文的经典 dcpo 约定。
10. [Interval Krawczyk and Newton method](https://ww2.ii.uj.edu.pl/~zgliczyn/cap07/krawczyk.pdf)，
    2007，Theorem 1：区间 Newton 包含、唯一性与空交排除的标准结论。
11. [AES note 05](../aes/05-measure-probability-information-and-area.md) §§5、9：
    指定 Haar 密度的四边形质量、反向质量序上的连续性及固定叶概率 valuation。

**来源与验证范围。** 苑明理提出本次四项数学校正及有理可计算边界的优先要求；
ChatGPT / Codex（OpenAI）据固定 main 整理上述命题、证明、反例与修订文字。
这是针对所声明载体的数学修订，不是独立人类审阅或形式化证明证书。
有限有理算例只用于核对公式，不替代任意定向族的证明。
