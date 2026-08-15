# 对坐标的反思

## 从笛卡尔坐标到运算网格、相对线性化与过程生成的坐标

### Research Note v0.2

**2026-08-16**

---

## 0. 位置、目标与方法

这是一份工作笔记，不试图过早宣布一种已经完成的“新坐标理论”。它整理近期围绕 Arithmetic Expression Geometry（AEG）、Hyperoperation、Paper 0、过程表征、尺子与测量的一系列讨论，把其中与“坐标”直接相关的结构尽可能完整地保存下来，同时明确哪些部分只是候选解释。

本文维持三种状态：

- **既有**：已经在现有 AEG / Hyperoperation 笔记或 Paper 0 中明确建立的公式、构造与结果；
- **推导**：从既有结果可以较直接得到，但尚未正式写成理论的结构解释；
- **候选**：目前有较强内在协调性、值得继续形式化，却仍可能被未来更好的理论重写的判断。

核心问题不是“怎样把笛卡尔坐标推广到非交换情形”，而是更向下追问：

> **坐标为什么存在？它由什么生成？坐标所依赖的网格、单位、尺子、尺度与读数之间究竟是什么关系？**

目前逐渐显现的工作图景是：

\[
\boxed{
\text{process grammar}
\to
\text{history grid}
\to
\text{distinguished linearizations}
\to
\text{rulers / scales}
\to
\text{coordinate readings}
}
\]

传统坐标把这条链的末端当作起点。我们现在尝试把它重新展开。

---

## 1. 笛卡尔坐标真正种下了什么？

### 1.1 坐标不只是“用数标点”

教科书把笛卡尔坐标写成：

\[
p\longmapsto (x^1,\ldots,x^n).
\]

但真正强大的地方不是编号，而是建立了一层统一的中介表示：几何对象可以被送到一个可计算的数值空间，几何关系可以被压缩成方程，方程上的代数运算又能返回几何结论。

在最基本的一维/二维模型中，坐标背后存在一组可重复移动：

\[
T_x(s):(x,y)\mapsto(x+s,y),
\qquad
T_y(t):(x,y)\mapsto(x,y+t).
\]

它们满足：

\[
T_x(s)T_y(t)=T_y(t)T_x(s).
\]

离散网格对应 \(\mathbb Z^2\)，连续运动对应 \((\mathbb R^2,+)\)。

所以笛卡尔坐标首先是一张**交换平移网格的压缩地址系统**。

### 1.2 坐标数对是 history compression

若从基点出发，经历历史：

\[
T_x(s_1)T_y(t_1)T_x(s_2)T_y(t_2)\cdots,
\]

因为所有基本移动交换，历史可以压缩为：

\[
\left(\sum_i s_i,\sum_i t_i\right).
\]

次序信息完全消失，但终点没有丢失任何必要信息。

因此普通坐标数对可以理解成：

\[
\boxed{
\text{operation history}
\longrightarrow
\text{relations quotient}
\longrightarrow
\text{normal form / coordinate}.
}
\]

这为后来思考一般运算网格提供了一个重要反转：

> **点的坐标并不一定是原初数据；它可以是历史在一组关系下的正规形。**

### 1.3 加法性是传统坐标的深层局部模型

笛卡尔传统最深的限制并不是“只能研究线性函数”。它当然可以描述高度非线性的曲线、方程和动力系统。

真正稳定地保留下来的，是一个更深的假设：

\[
\boxed{
\text{所有局部变化最终都放到一个共同的加法性线性空间中比较。}
}
\]

坐标差是 \(x'-x\)；切向量可以相加；导数是线性映射；微分形式是切空间的线性对偶；积分是加法性的累计。

即使进入 manifold、Lie group、connection、frame、coframe、curvature，典型模式仍然是：

\[
\text{nonlinear object}
\to
\text{local linearization}
\to
\text{linear calculation}
\to
\text{global reconstruction / obstruction}.
\]

因此，笛卡尔种下的不只是二维坐标轴，而是一种**唯一的加法性元语言**。

---

## 2. 从坐标退回到网格

### 2.1 更原初的对象是生成元与关系

设有 primitive processes：

\[
S=\{F_\alpha\}.
\]

一个有限 history 是：

\[
w=F_{\alpha_n}\cdots F_{\alpha_1}.
\]

若存在 relations：

\[
R_i:w_i\sim w_i',
\]

则网格首先应由：

\[
\boxed{\mathcal G=(S,R)}
\]

描述。

根据操作是否可逆、局部、带分支、带 rewrite coherence，这个对象可能是：

- monoid；
- group；
- groupoid；
- pseudogroup；
- category；
- higher rewrite / polygraphic structure。

因此“坐标网格”不应被预先等同于某个 Lie 群。

### 2.2 坐标是网格的一种商与正规化

选择基点 \(p_0\)，history word 给出：

\[
w\cdot p_0.
\]

如果 relations 足以将每个 history 压缩成唯一正规形，坐标便出现了。

笛卡尔网格的关系极强且极简单：所有独立方向交换，于是历史唯一压缩成一个向量。

一般网格中则可能出现：

- 不同 histories 到达同一终点；
- 同一终点仍保留不同 holonomy；
- 不同路径只有局部或高阶等价；
- 无全局正规形；
- 坐标只能是 group element、word、chart family 或局部 section。

这与 AEG 的根本立场一致：semantic value 并不能代表 computation history 的全部结构。

---

## 3. 两种最基本的二维网格：Cartesian 与 affine

### 3.1 Cartesian：所有基本尺子彼此透明

笛卡尔情形中：

\[
[\partial_x,\partial_y]=0.
\]

相应的 infinitesimal rulers：

\[
dx,\qquad dy
\]

在彼此方向上的运输都是平凡的。

因此：

1. 两个方向可以同时成为平移；
2. 一个方向不会改变另一方向的单位；
3. 小矩形闭合；
4. history 只需要净位移；
5. “网格”“尺子”“坐标值”几乎可以被无缝识别。

这是一种非常特殊而高度刚性的情形。

### 3.2 \(E_0\)：加法与乘法第一次产生非平凡运输

Paper 0 的基本模型取：

\[
E_0=\{(x,y):y>0\},
\qquad
a=-\frac{x}{y}.
\]

定义：

\[
X_s(x,y)=(x-sy,y),
\]

\[
Y_k(x,y)=\left(x,\frac yk\right).
\]

它们在 arithmetic reading \(a\) 上分别实现：

\[
a\circ X_s=a+s,
\qquad
a\circ Y_k=ka.
\]

所以 \(X_s\) 是 additive step，\(Y_k\) 是 scale/multiplicative step。

对整数 \(m\ge2\)：

\[
Y_m^{-1}X_s^mY_m=X_s.
\]

等价地，在另一方向约定下：

\[
Y_mX_sY_m^{-1}=X_{ms}.
\]

它是 Baumslag–Solitar 型关系的最初算术原型。

### 3.3 这个关系真正表达的是“尺子运输”

若在某一层尺度上，一次加法单位是 \(X_s\)，经过乘法尺度变化后，同一个加法过程的有效分辨率改变。

因此：

\[
\boxed{
\text{multiplicative/scale motion transports the additive ruler.}
}
\]

这与笛卡尔结构有本质差异：在那里，一把尺子沿另一方向移动不会发生任何变化。

所以 \(E_0\) 的最深意义不只是“发现了一个非交换群”，而是：

> **基本运算方向之间存在非平凡的单位运输律。**

### 3.4 \(E_0\) 与正向 affine group

把点写成：

\[
g(x,y)=
\begin{pmatrix}
y&x\\
0&1
\end{pmatrix},
\qquad y>0,
\]

则：

\[
(x,y)\cdot(x',y')=(x+yx',yy').
\]

这正是 \(\operatorname{Aff}^+(1)\) 的群乘法。

因此 \(E_0\) 可以被实现成 affine group 的群流形，而 \(X_s,Y_k\) 是其中两类自然操作。

这给出一个有用但必须克制的低维事实：笛卡尔平移网格与加乘 affine 网格恰好对应二维 Lie algebra 的阿贝尔型与唯一非阿贝尔型。这个分类说明它们是最低维度中极自然的两个原型，但不应被误解为一般“坐标理论”的最终分类。

---

## 4. Hyperoperation：坐标由过程内生生成

### 4.1 Abel coordinate 不是任意换元

对 rank-\(r\) unary process \(F_r\)，寻找：

\[
\boxed{
A_r(F_r(x))=A_r(x)+1.
}
\]

\(A_r\) 是 step-count / linearizing coordinate。

在这个坐标中，复杂过程变成：

\[
\tau(t)=t+1.
\]

令：

\[
E_r=A_r^{-1}.
\]

在标准 Hyperoperation normalization 中：

\[
E_r\sim F_{r+1}.
\]

于是：

\[
F_r
\longrightarrow
A_r
\longrightarrow
A_r^{-1}\sim F_{r+1}.
\]

这说明线性化不是分析的终点；**线性化坐标的逆可以被重新对象化为下一阶 primitive**。

### 4.2 加法的新地位：通用正规形，而非唯一原生结构

每一级 process 在自己的 Abel coordinate 中都成为：

\[
t\mapsto t+1.
\]

所以加法并没有消失。

但它的地位发生了变化：

\[
\boxed{
\text{加法不再被预设为所有对象的唯一原生局部结构，}
}
\]

而成为：

\[
\boxed{
\text{可线性化过程的通用正规形。}
}
\]

真正携带 rank 信息的，是 distinguished coordinates：

\[
A_1,A_2,A_3,\ldots
\]

以及它们的生成关系和相对位置。

### 4.3 time sort 与 value sort 必须分开

严格地说：

\[
A_r:X_r\to T_r,
\qquad
E_r:T_r\to X_r.
\]

其中 \(T_r\) 是 iteration-time/process-clock object，\(X_r\) 是 state/value object。

二者在传统 Hyperoperation 里都常由实数表示，所以容易被无意识地识别。但未来理论不应依赖这种巧合。

因此 rank raising 不是普通单类型 endofunctor，而至少需要：

- time/value retyping；
- normalization；
- seed；
- branch/sector data；
- 局部或形式 realization。

这为后面完全放弃实数作为基础读数留下了空间。

---

## 5. 几何可能来自“不能同时线性化”

### 5.1 单个过程可以平移化，不代表多个过程可以共同平移化

若每个 \(F_r\) 都有自己的 \(A_r\)，则每个过程单独看都可以被线性化为 translation。

但一般不存在一个共同坐标 \(A\)，使：

\[
A\circ F_r\circ A^{-1}
\]

对所有 \(r\) 同时成为独立平移。

因此一个非常重要的候选命题是：

\[
\boxed{
\text{几何来自多个过程各自可线性化，}
\text{却不能被同一个线性化同时容纳。}
}
\]

笛卡尔网格正是 simultaneous linearization 完全成立的退化情形。

### 5.2 rank transition atlas

在共同可比较的局部或 sectorial domain 上定义：

\[
T_{rs}=A_s\circ A_r^{-1}.
\]

它满足 cocycle composition：

\[
T_{rt}=T_{st}\circ T_{rs}.
\]

若：

\[
G_r=\frac1{A_r'},
\]

则：

\[
\Omega_{rs}=G_rG_s'-G_sG_r'
\]

测量不同 rank linearizing coordinates 之间的 affine incompatibility。

这一点非常关键：未来的几何不一定首先建立在一个统一 tangent space 上，而可以建立在**多个由过程内生选择的线性化之间的 transition geometry**上。

### 5.3 rank 1–2 与 rank 3 的结构门槛

rank 1–2 的基本生成元可由：

\[
\partial_x,
\qquad
x\partial_x
\]

表达，并闭合为 affine algebra。

rank 3 的 exponentiation 在二阶 jet 上出现：

\[
z^2\partial_z
\]

的 projective shadow，与前两级共同形成 \(\mathfrak{sl}_2\) 的最低阶轮廓；但真实 iterative logarithm 包含更高 modes，三阶 Schwarzian 首次检测到越出 projective closure 的部分，formal closure 进一步打开 completed Witt ambient algebra。

这提示：

\[
\boxed{
\text{affine}
\to
\text{projective shadow}
\to
\text{higher diffeomorphic / sectorial structures}
}
\]

可能是 process-generated coordinate systems 的一个低阶谱系。

但这里必须保持谨慎：ambient Lie algebra 不是 Hyperoperation tower 本身。rank 3 以后 Lie closure 很快饱和，真正的信息仍在 distinguished generators、rank labels、iteration relations 与 relative positions 中。

---

## 6. Frame、coframe 与 Lie algebra 应当被重新定位

### 6.1 传统依赖顺序

经典微分几何通常从：

\[
\text{manifold}
\to
\text{tangent space}
\to
\text{frame/coframe}
\to
\text{connection/curvature}
\]

开始。

### 6.2 候选的新依赖顺序

如果坐标和尺子由过程生成，那么更原初的顺序应是：

\[
\boxed{
\text{process grammar}
\to
\text{finite histories}
\to
\text{relations / transport}
\to
\text{process coordinates}
\to
\text{rulers}
\to
\text{frame/coframe}.
}
\]

因此：

- tangent vector 是有限 process step 的一阶阴影；
- Lie bracket 是有限 history commutator 的最低阶阴影；
- coframe 是有限 process counting 的 infinitesimal density；
- Maurer–Cartan equation 是有限群关系的微分阴影；
- metric 是在若干 process rulers 上选择的比较结构；
- curvature 是有限 transport/coherence 失败的局部投影。

这些经典对象仍然重要，但它们不再自动拥有本体论优先级。

### 6.3 有限 process cocycle 比 \(dA_r\) 更原初

对 rank \(r\)，定义：

\[
c_r(g,x)=A_r(gx)-A_r(x).
\]

它满足：

\[
c_r(gh,x)=c_r(g,hx)+c_r(h,x).
\]

且 native step 满足：

\[
c_r(F_r,x)=1.
\]

这首先是一个有限尺度的 process cocycle。

只有在平滑 realization 中，它才产生：

\[
\omega_r=dA_r.
\]

同样，对另一个 operation \(F_\alpha\)，可以定义 ruler transport：

\[
K_{\alpha|r}(x)
=
\frac{F_\alpha^*\omega_r}{\omega_r}.
\]

native ruler 满足：

\[
K_{r|r}=1.
\]

非对角项则记录“一个 process 怎样改变另一种 ruler”。

笛卡尔情形是所有这些交叉运输都平凡的极特殊情形。

---

## 7. 两条轴：operation direction 与 representation scale

在此前讨论中，一个重要澄清是：

\[
\boxed{
\text{operation direction}
\neq
\text{calculus / representation scale}.
}
\]

### 7.1 水平轴：process direction / history

\[
+,
\times,
\uparrow,
\ldots
\]

可以作为不同 primitive processes，生成不同 history directions。

AEG 关注：

- 顺序；
- operand slot；
- branching；
- rewrite；
- commutator；
- holonomy；
- history residual。

### 7.2 垂直轴：representation rank / ruler

\[
d_1,
d_2,
d_3,\ldots
\]

回答的是：变化在哪一种 process representation 中被测量。

Hyperoperation calculus 进一步有：

\[
\omega_r
\to
A_r
\to
A_r^{-1}=F_{r+1}
\to
\omega_{r+1}.
\]

因此理论中至少存在：

- 水平的 history calculus；
- 垂直的 rank-raising calculus；
- 二者之间的混合 transport。

未来一个真正成熟的理论，很可能需要把这两条轴同时保留，而不能把它们提前压成一个单一的 tangent bundle。

---

## 8. AEG 的 path / ripple 与“坐标作为历史”的关系

Paper 0 已经建立：同一个 one-hole operator word 可以有两种读取方式。

给 prefix operators：

\[
G_k=F_k\circ\cdots\circ F_1,
\]

可以：

1. covariantly 推进一点：
   \[
   z_k=G_k(z_0);
   \]
2. contravariantly 拉回输出条件：
   \[
   \Sigma_{k,t}=G_k^{-1}(\Sigma_t).
   \]

因此 point path 与 ripple history 不是两种互不相关的几何，而是同一个 chronological operator word 的两种 observable。

矩阵 realization 又把：

- point path；
- pole；
- fixed points；
- ripple pencil；

统一到同一个 prefix matrix 上。

这意味着：

\[
\boxed{
\text{坐标不能只保存终点；
更完整的 coordinate object 可以保存 operator history 及其多个读取。}
}
\]

AEG 的一个核心任务正是研究：

\[
\text{history}
\longrightarrow
\text{semantic realization}
\]

过程中丢失了什么，以及这些丢失信息能否被重新组织成几何、拓扑与复杂性不变量。

---

## 9. Projective closure 的新位置

Paper 0 中，加法、非零乘法与 right-slot reciprocal 共同生成 \(PGL_2\)。其中 affine sector 是：

\[
\operatorname{Aff}(1)=\operatorname{Stab}(\infty)\subset PGL_2.
\]

从当前视角看，这个结果仍然重要，但其解释需要收紧。

它更接近：

\[
\boxed{
\text{one-hole arithmetic 的 projective closure}
}
\]

而不是所有 operation geometry 的最终统一空间。

这里存在两条完全不同的扩展：

### 横向 projective completion

加入 reciprocal / finite pole：

\[
\operatorname{Aff}(1)
\to
PGL_2.
\]

### 纵向 rank raising

把 repeated process 压缩为新的 primitive：

\[
+
\to
\times
\to
\exp
\to
\text{tetration}
\to\cdots.
\]

前者扩大一个 rank 内的 operator class；后者改变 primitive representation 本身。

这两条轴未来必须严格区分。

---

## 10. 从 Cartesian 到 post-Cartesian：应怎样重新理解“坐标”？

到目前为止，可以形成一个仍属候选的定义方向。

一个 **operational coordinate system** 不只是 chart，而至少包含：

1. primitive processes；
2. history composition；
3. relations/coherence；
4. base state 或 reference object；
5. distinguished process clocks；
6. unit / calibration transformations；
7. process 对 ruler 的 transport；
8. external realization；
9. reading / precision structure；
10. 不同 ranks / charts 之间的 transition data。

在这个框架中：

### Cartesian coordinate system

是所有 primitive directions：

- 可同时平移化；
- 彼此交换；
- cross-ruler transport 平凡；
- history 可压缩为向量；
- 读数与外在位置线性同构；

的退化情形。

### \(E_0\)

是第一个：

- basic directions 不交换；
- scale direction 运输 additive ruler；
- history 不能只用独立坐标和来压缩；
- 但仍有有限维 affine closure；

的运算坐标原型。

### higher Hyperoperation systems

则允许：

- 每个 rank 有自己的 linearizing clock；
- 不同 clocks 之间只有局部、formal 或 sectorial transition；
- 同时线性化出现更高 obstruction；
- reading carrier 不必预先是实数。

---

## 11. 对笛卡尔传统的一次更深反思

可以把数学史中的一条主线概括为：

\[
\text{Cartesian coordinates}
\to
\text{linear algebra}
\to
\text{calculus}
\to
\text{manifolds}
\to
\text{frames/coframes}
\to
\text{Lie/Cartan geometry}.
\]

这当然不是严格的单线历史，但这些理论长期共享一个非常稳定的底层语言：局部线性化和加法性差分。

我们现在真正可能跳出的，不只是“交换性”，而是：

\[
\boxed{
\text{唯一预设线性化的历史限制。}
}
\]

新的问题不再只是：

> 对一个非线性对象，如何在线性切空间中研究它？

而是：

> **不同 primitive processes 如何各自生成一种自然线性化？这些线性化为什么不能同时成立？它们之间的冲突、运输和 rank raising 本身能否形成几何？**

这可以暂时称为：

\[
\boxed{
\text{geometry of recursively generated relative linearizations}.
}
\]

这个名称不是最终术语，只用于标记当前思路的重心。

---

## 12. 对 Paper 0 的直接影响

Paper 0 当前 Section 3 的叙事容易被读成：

\[
\text{choose upper-half-plane geometry}
\to
\text{place arithmetic moves in it}.
\]

按照目前理解，更自然的逻辑顺序是：

\[
\boxed{
\begin{aligned}
+,&\times
\to
\text{primitive moves}
\\
&\to
\text{addition–scale grid}
\\
&\to
\text{BS-type ruler transport}
\\
&\to
\text{assignment / readout}
\\
&\to
\text{natural rulers and metric}
\\
&\to
\text{path / geometric residual}.
\end{aligned}
}
\]

因此 \(E_0\) 的概念位置可以从“zeroth-kind background”提升为：

> **addition–scaling 的 elementary operational coordinate grid。**

但 Paper 0 仍应保持初等，不宜把完整 measurement theory、rank-raising、sectorial analysis 全部塞入正文。更合理的做法是：

- 在 Paper 0 中把网格先于 metric 的生成顺序说明清楚；
- 把 BS relation 提升为 add/scale transport 的核心结构；
- 把 Hyperoperation 与 measurement-system 扩展留给后续专门文章或研究笔记。

---

## 13. 当前仍需保持开放的问题

### 13.1 “坐标”的 universal property

能否用一个真正的 universal property 定义 operational coordinate system，而不是人工拼装 group action、clock、ruler 和 reading？

### 13.2 simultaneous linearization obstruction

能否把：

- commutator；
- BS relation；
- \(\Omega_{rs}\)；
- Schwarzian；
- sectorial / Stokes-type data；

组织成一座统一的 obstruction tower？

### 13.3 history 与 coordinate normal form

什么条件保证 history grid 有：

- canonical normal form；
- finite presentation；
- efficient reduction；
- geometry-compatible quotient？

### 13.4 operation group 与 calibration group 是否应分离

在 \(E_0\) 中，乘法既可以被理解成 arithmetic operation，也可以被理解成改变加法单位的 scaling action。高 rank 以后这两种角色是否仍能自然统一，还是应形成两个不同但相互作用的 groupoid？

### 13.5 数是否必要

如果 coordinate 的更原初对象是 process clock、history class 与 ruler realization，那么读数 carrier 是否必须是 \(\mathbb R\)？是否可以是：

- ordered group；
- groupoid；
- symbolic sequence；
- local section；
- formal/sectorial object；
- filtered completion？

这个问题直接通向下一份“测量体系”笔记。

---

## 14. 阶段性结论

当前最值得保存的判断有五条。

第一：

\[
\boxed{
\text{笛卡尔坐标是交换平移网格的极特殊而完美的压缩实现。}
}
\]

第二：

\[
\boxed{
\text{坐标可以被还原为 primitive processes、history relations 与 normal forms。}
}
\]

第三：

\[
\boxed{
\text{Hyperoperation 表明自然坐标可以由 process 本身递归生成。}
}
\]

第四：

\[
\boxed{
\text{几何可能存在于多个 distinguished linearizations 不能同时成立之处。}
}
\]

第五：

\[
\boxed{
\text{frame、coframe、Lie algebra 与 metric 可能只是有限 process structure 的导出阴影。}
}
\]

因此，当前最凝练的工作图景不是“发明一种非交换坐标”，而是：

> **从一个先验给定的坐标世界，转向研究坐标如何由过程、关系、尺度与线性化本身生长出来。**

---

## 15. 与下一份笔记的接口

一旦坐标被还原为网格，立即出现一个更根本的问题：

- 什么是“一个单位”？
- 为什么换单位后读数改变，而测量方法不变？
- 理想网格怎样映射到外在几何？
- 精度和误差怎样参与这套结构？
- 数是测量的前提，还是测量体系的完成产物？
- 为什么量纲分析自然进入 Lie 群与表示论？

这些问题不应继续塞在“坐标”之下，而应作为独立主题进入：

\[
\boxed{
\text{对测量体系的反思。}
}
\]

---

## 参考现有材料与讨论线索

- `aeg-paper-0.pdf`：one-hole history、point/condition propagation、\(E_0\) addition–multiplication grid、BS 型关系、affine/projective realization。
- `05-hyperoperation-calculus.md`：Abel coordinate、operation-generated rulers、ranked calculus、rank-raising recursion。
- `04-hyperoperation.md`：relative linearization、rank tower、affine → projective → Witt、typing 与 sectorial boundary。
- `06-process-concept-representation.md`：history/semantics、process compression、operational geometry、direction 与 scale 的区分。
- 2026-08-16 本轮讨论：Cartesian 坐标的加法性元语言、网格优先、尺子运输、同时线性化障碍、frame/coframe 的重新定位，以及从坐标通向 measurement system 的思路。
