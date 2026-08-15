# Process, Representation, and Hyperoperation Calculus

## 从 AEG 的过程表征到分层算术微积分

### Research Note v0.2

**2026-08-14**

## 0. 这份笔记的位置

Arithmetic Expression Geometry（AEG）的出发点之一，是拒绝把算术表达式仅仅理解为其最终数值。一个表达式同时携带着：

[
\text{expression}
\longrightarrow
\text{evaluation history}
\longrightarrow
\text{relations between histories}
\longrightarrow
\text{semantic value}.
]

数值是计算的结果，却不是计算对象的全部结构。

最近围绕 Hyperoperation、无穷小、微分与积分的一系列讨论，逐渐形成了另一条看似独立、实际上与这一思想深刻呼应的路线：

[
+;\longrightarrow;\times;\longrightarrow;\uparrow
;\longrightarrow;\uparrow\uparrow;\longrightarrow\cdots
]

每一次 Hyperoperation 升阶，都可以理解为把前一级反复发生的过程压缩成一个新的基本运算；而每一级运算又选择一种自己的“单位变化”和无穷小尺度，由此形成一族彼此关联的微积分。

这份笔记总结目前形成的数学结构与哲学理解。它不试图过早决定最终理论究竟应当分成几层，也不主张现有结果已经构成一种完整的新分析学。更合适的态度是：

> 我们已经发现了一组彼此高度协调的结构。现在首先需要理解它们为什么协调，再判断它们最终属于一个理论、两个层次，还是几个彼此作用的理论。

---

# 1. AEG 的基本哲学：显式表征计算历史

传统算术倾向于把：

[
E\longmapsto \operatorname{ev}(E)
]

视作一个从表达式到数值的映射。

一旦：

[
\operatorname{ev}(E_1)
======================

\operatorname{ev}(E_2),
]

两条过程在语义层便不可区分。

AEG 的基本立场恰恰是：在 evaluation 以前，(E_1,E_2) 仍然可能具有完全不同的结构。

例如：

[
(x+1)\times2
]

和

[
x\times2+1
]

不是同一条计算历史。

其数值差异固然重要，更根本的是：

[
+\quad\text{与}\quad\times
]

以不同顺序参与了计算。

因此 AEG 所做的第一件事情，可以理解为：

[
\boxed{
\text{给 computation history 一个显式数学表征。}
}
]

这也是 arithmetic torsion、expression path、ACS、contact structure 等构造背后的共同问题意识。

---

# 2. 概念表征与过程表征

这个观点可以继续向前推一步。

“概念”与“过程”未必是静态对象与动态对象的简单二分。

一个概念往往可以理解为：

[
\boxed{
\text{对一类稳定、反复出现的过程结构的压缩。}
}
]

反过来，一个概念的意义也往往可以通过展开它所压缩的过程来解释。

Hyperoperation 给出了一个极为纯净的模型：

[
\begin{aligned}
\text{multiplication}
&=
\text{repeated addition},\
\text{exponentiation}
&=
\text{repeated multiplication},\
\text{tetration}
&=
\text{repeated exponentiation}.
\end{aligned}
]

例如：

[
\underbrace{
a+a+\cdots+a
}_{n}
]

可以压缩成：

[
na.
]

而：

[
\underbrace{
a\times a\times\cdots\times a
}_{n}
]

又可以压缩成：

[
a^n.
]

因此：

[
\boxed{
\text{long process history}
\longrightarrow
\text{short higher-rank representation}.
}
]

Hyperoperation rank 因而可以暂时理解为一种非常特殊、非常规整的：

[
\boxed{
\text{process-compression depth}.
}
]

这不是一般“概念复杂性”的完整理论，但提供了一个可计算的原型。

---

# 3. 表征复杂性与计算复杂性

这与此前关于时空计算复杂性和表征复杂性的讨论直接相关。

若 primitive vocabulary 只有：

[
{+},
]

则表示 (na) 可能需要 (O(n)) 长度的过程。

加入：

[
\times
]

以后，同一计算可以用常数尺寸表达。

再加入：

[
\uparrow,
]

又可以把长乘法过程压缩。

因此复杂度应至少部分地写成相对于表示语言的量：

[
\boxed{
C(x\mid\mathcal V),
}
]

其中 (\mathcal V) 是允许使用的 primitive operations。

令：

[
\mathcal V_r
============

{H_1,\ldots,H_r}.
]

可以定义：

[
C_r(x)
======

\min
{
\operatorname{cost}(E):
\operatorname{ev}(E)=x,;
E\text{ uses ranks }\le r
}.
]

于是：

[
C_{r+1}(x)
\le
C_r(x).
]

更有意义的是 compression gap：

[
\boxed{
\Delta C_r(x)
=============

C_r(x)-C_{r+1}(x).
}
]

某些对象可能在引入新的 primitive concept 后发生巨大的表征相变。

因此：

> 表征复杂性不是附属于计算复杂性的装饰变量；在某些情况下，一段时间过程本身可以被重新编码为空间中的一个短结构，二者可能是同一种复杂性的不同表现。

Hyperoperation 是检验这一思想的最简单模型之一。

---

# 4. Hyperoperation 的连续化：过程坐标与概念坐标

固定一个 rank-(r) unary operation：

[
F_r.
]

寻找 Abel / linearizing coordinate：

[
\boxed{
A_r(F_r(x))
===========

A_r(x)+1.
}
]

这条式子的意义非常丰富。

在 (A_r) 坐标中：

[
F_r
]

不再是复杂运算，而只是：

[
t\mapsto t+1.
]

因此：

[
\boxed{
A_r(x)
}
]

可以解释为第 (r) 种 computation process 的 **step-count coordinate**：

> 状态 (x) 相当于在这种计算方式中走到了第几步？

另一方面：

[
E_r:=A_r^{-1}
]

则把 process coordinate 重新压缩成 state：

[
\boxed{
\text{process coordinate}
\overset{E_r}{\longrightarrow}
\text{compressed representation}.
}
]

在标准 Hyperoperation normalization 中：

[
E_r
\sim
F_{r+1}.
]

于是出现：

[
\boxed{
A_r
\quad\leftrightarrow\quad
A_r^{-1}
}
]

这一非常简洁的 process/concept duality：

[
\boxed{
\text{unfold process}
\quad\leftrightarrow\quad
\text{compress process}.
}
]

更进一步：

[
\boxed{
F_{r+1}^{-1}
\circ
F_r
\circ
F_{r+1}
=======

\tau,
\qquad
\tau(t)=t+1.
}
]

也就是说：

> 每一级 Hyperoperation 都被下一级 Hyperoperation 自身线性化成单位平移。

---

# 5. 尺度从哪里来？

一旦：

[
A_r(F_r(x))-A_r(x)=1,
]

我们便获得了“一个 rank-(r) 单位步骤”的定义。

因此自然定义：

[
\boxed{
\mathrm d_r x
:=
dA_r(x).
}
]

也记：

[
\omega_r:=\mathrm d_r x.
]

它不是一个人为选择的 metric。

它来自一个非常直接的原则：

[
\boxed{
\text{process unit}
\Longrightarrow
\text{measurement unit}.
}
]

不同概念/过程表征认为“一步”意味着不同的变化，因此自然产生不同的 infinitesimal rulers。

前三层给出：

[
\mathrm d_1x=dx,
]

[
\mathrm d_2x=d\log x=\frac{dx}{x},
]

而临界 rank-3 指数迭代给出：

[
\mathrm d_3x
============

# dA_3(x)

\frac{dx}{j(x)},
]

其中 (j) 是 exponentiation germ 的 iterative logarithm。

在临界模型：

[
h(z)=e^z-1,
]

有：

[
j(z)
====

\frac12z^2
-\frac1{12}z^3
+\frac1{48}z^4-\cdots,
]

所以：

[
\boxed{
\mathrm d_3z
============

\left(
\frac2{z^2}
+\frac1{3z}
-\frac1{36}
+\frac{z}{270}
+\cdots
\right)dz.
}
]

这已经不是普通平滑换元的简单例子，而进入了 parabolic / Abel / sectorial dynamics。

---

# 6. Hyperoperation calculus 的核心符号

现在最自然的 Leibniz 型记法是：

[
\boxed{
\frac{\mathrm d_s y}
{\mathrm d_r x}
:=
\frac{dA_s(y)}
{dA_r(x)}.
}
]

如果：

[
y=f(x),
]

则：

[
\boxed{
\frac{\mathrm d_s f}
{\mathrm d_r x}
===============

\frac{G_r(x)}
{G_s(f(x))}
f'(x),
}
]

其中：

[
G_r(x)
======

\frac1{A_r'(x)}.
]

也可以写成更几何的形式：

[
\boxed{
\frac{\mathrm d_sy}{\mathrm d_rx}
=================================

\frac{f^*\omega_s}{\omega_r}.
}
]

这个符号具有一个极强的优点：

[
\boxed{
\frac{\mathrm d_tz}{\mathrm d_rx}
=================================

\frac{\mathrm d_tz}{\mathrm d_sy}
\frac{\mathrm d_sy}{\mathrm d_rx}.
}
]

中间的：

[
\mathrm d_sy
]

像莱布尼茨微商一样自然消去。

因此 (r,s) calculus 可以理解为：

[
\boxed{
\text{不同 process representations 之间的局部 Jacobian calculus}.
}
]

---

# 7. (r,s) 的表征含义

技术上：

[
r
]

和：

[
s
]

表示 source/target infinitesimal scales。

但从表征观点，可以更具启发性地理解：

[
\boxed{
r=
\text{source process-representation depth},
}
]

[
\boxed{
s=
\text{target process-representation depth}.
}
]

于是：

[
\frac{\mathrm d_2y}{\mathrm d_1x}
=================================

\frac{d\log y}{dx}
]

不只是 logarithmic derivative。

它可以被读成：

> 输入按 additive process language 测量时，输出在 multiplicative process language 中每发生一个微小单位需要多少输入变化。

同样：

[
\frac{\mathrm d_2y}{\mathrm d_2x}
=================================

\frac{d\log y}{d\log x}
]

就是 multiplicative representation 到 multiplicative representation 的局部 conversion rate。

而：

[
\frac{\mathrm d_3y}{\mathrm d_2x}
]

则开始比较 multiplicative process representation 与 exponentiation-iteration representation。

这让 (r,s) 不再只是技术下标，而成为一种 **representation transition calculus**。

---

# 8. 与经典微积分的统一

取：

[
A_1(x)=x,
\qquad
A_2(x)=\log x.
]

则：

[
\frac{\mathrm d_1y}{\mathrm d_1x}
=================================

\frac{dy}{dx},
]

普通导数；

[
\frac{\mathrm d_2y}{\mathrm d_1x}
=================================

\frac{y'}{y},
]

logarithmic derivative；

[
\frac{\mathrm d_1y}{\mathrm d_2x}
=================================

xy',
]

Euler dilation derivative；

以及：

[
\frac{\mathrm d_2y}{\mathrm d_2x}
=================================

\frac{xy'}y,
]

elasticity。

所以：

[
\boxed{
\left(
\frac{\mathrm d_sy}{\mathrm d_rx}
\right)_{r,s=1,2}
}
]

已经把几个熟悉的 classical operators 放进一个统一的矩阵。

---

# 9. 原生算术中的导数与不定式

[
\frac{\mathrm d_sy}{\mathrm d_rx}
]

是在共同 additive/linearized coordinate 中得到的 coefficient。

如果需要把结果重新解释成 rank-(s) arithmetic 中的原生量，可以使用：

[
E_s
\left(
\frac{\mathrm d_sy}{\mathrm d_rx}
\right).
]

例如：

[
E_2
\left(
\frac{\mathrm d_2y}{\mathrm d_1x}
\right)
=======

\exp\left(\frac{y'}y\right),
]

这就是 multiplicative derivative。

它的极限形式是：

[
\lim_{h\to0}
\left(
\frac{f(x+h)}{f(x)}
\right)^{1/h}.
]

在普通实数表达中，这是：

[
1^\infty
]

型。

这重新连接了最初关于不定式的直觉。

普通 additive derivative 对应：

[
0/0;
]

multiplicative derivative 对应：

[
1^\infty.
]

更准确地说，它们可以被视为同一个 abstract singular quotient：

[
\boxed{
0_s\oslash_s0_s
}
]

在不同 arithmetic realization 中的表现。

因此值得研究的不是传统不定式字符串本身，而是：

[
\boxed{
\text{不同 process representations 在其边界上产生哪些不等价的 singular normal forms？}
}
]

---

# 10. 积分：过程重新累积

若：

[
\mathrm d_sy
============

q,\mathrm d_rx,
]

则：

[
dA_s(y)
=======

q,dA_r(x).
]

因此：

[
A_s(y)
======

C+\int q,\mathrm d_rx,
]

以及：

[
\boxed{
y
=

E_s
\left(
C+\int q,\mathrm d_rx
\right).
}
]

这就是 ranked fundamental theorem 的自然形式。

于是微分与积分可以分别理解成：

[
\boxed{
\text{differentiate}
====================

\text{compare elementary process increments},
}
]

[
\boxed{
\text{integrate}
================

\text{accumulate elementary process increments}.
}
]

---

# 11. 更高 Hyperoperation 是“常数的积分”

这是目前 Hyperoperation calculus 中最漂亮的结构之一。

由于：

[
A_r(E_r(t))=t,
]

所以：

[
\boxed{
\frac{\mathrm d_rE_r(t)}
{\mathrm d_1t}
==============

1.

}
]

因此：

[
\boxed{
E_r(t)
======

\int^{\to r}1,dt.
}
]

在 Hyperoperation normalization 下：

[
E_r\sim H_{r+1}.
]

于是：

[
\int^{\to1}1,dt=t,
]

[
\int^{\to2}1,dt=e^t,
]

[
\int^{\to3}1,dt=\operatorname{tet}(t),
]

等等。

换言之：

[
\boxed{
\text{higher Hyperoperation}
============================

\text{primitive of a constant in the preceding calculus}.
}
]

这是一种比“乘法是重复加法”更接近连续分析的递归表达。

---

# 12. Calculus-raising recursion

令：

[
\omega_r=q_r(x),dx.
]

由于下一阶 operation：

[
F_{r+1}=A_r^{-1},
]

而 (\omega_{r+1}) 必须在 (F_{r+1}) 下保持不变：

[
F_{r+1}^*\omega_{r+1}=\omega_{r+1},
]

可以推出：

[
\boxed{
q_{r+1}(x)
==========

q_r(x),
q_{r+1}(A_r(x)).
}
]

这是一条重要递推。

它意味着：

> 下一阶 infinitesimal ruler 不是任意定义，而是上一阶 ruler 的 primitive 所生成的新 dynamics 的 invariant differential。

因此：

[
\boxed{
\omega_r
\longrightarrow
A_r=\int\omega_r
\longrightarrow
A_r^{-1}=F_{r+1}
\longrightarrow
\omega_{r+1}.
}
]

这是一个闭环。

---

# 13. Rank raising 作为第二种“积分”

令：

[
u_r=\log q_r.
]

则上式化为：

[
u_{r+1}(x)
----------

# u_{r+1}(A_r(x))

u_r(x).
]

定义：

[
\boxed{
\mathsf B_r:=I-A_r^*
}
]

其中：

[
A_r^*u=u\circ A_r.
]

则：

[
\boxed{
\mathsf B_ru_{r+1}=u_r.
}
]

这意味着除了固定 rank 内：

[
d/\int
]

这一横向微积分之外，还存在一条纵向的：

[
\boxed{
\text{rank-raising cohomological calculus}.
}
]

固定 rank 的积分累计某种变化；

而 rank raising 则通过解一个 dynamical cohomological equation，**生成下一种变化尺度本身**。

这也许是 Hyperoperation calculus 最不同于普通 non-Newtonian coordinate transport 的地方之一。

---

# 14. 为什么更高 rank 会产生越来越复杂的分析语言？

前三层给出了：

[
\omega_1
========

dx,
]

[
\omega_2
========

\frac{dx}{x},
]

以及：

[
\omega_3
========

\left(
\frac2{x^2}
+\frac1{3x}
+\cdots
\right)dx.
]

于是其 primitive 依次出现：

[
x,
]

[
\log x,
]

[
-\frac2x+\frac13\log x+\cdots.
]

到了 rank 3，普通 convergent Taylor language 已经不足，需要：

* Laurent-type singularities；
* logarithmic resonance；
* formal/asymptotic expansions；
* sectorial Fatou coordinates；
* 更高阶段可能出现 power-log transseries 与 resurgence。

这提示：

[
\boxed{
\text{Hyperoperation complexity
可能体现为其 natural linearizing representation
需要越来越丰富的函数语言。}
}
]

也就是说：

> operation 在自己的坐标中永远只是 (t\mapsto t+1)；
> 真正复杂的是找到并表达这个坐标。

这与“表征复杂性”再次形成直接呼应。

---

# 15. 两种不同来源的几何

这一点必须与 ranked calculus 区分开来。

## 15.1 Spatial Geometry

传统几何的维数来自空间本身允许多个独立方向：

[
x^1,\ldots,x^n.
]

逻辑通常是：

[
\text{space}
\to
\text{directions}
\to
\text{coordinates}.
]

人类的几何直觉主要源于这种 physical/spatial extension。

---

## 15.2 Operational Geometry

AEG 加乘几何的二维性不是从一个已有二维物理空间开始。

它来自两种独立计算方法：

[
+,\qquad\times.
]

为了显式记录：

> 一个 computation history 究竟沿哪个 operation generator 推进，

才引入：

[
u,\qquad v.
]

所以：

[
\boxed{
\text{operations}
\to
\text{process directions}
\to
\text{operational coordinates}
\to
\text{geometry}.
}
]

这里：

[
u
]

不是 physical x-axis，

[
v
]

也不是 physical y-axis。

它们分别是：

[
\boxed{
u\leftrightarrow\text{addition process},
\qquad
v\leftrightarrow\text{multiplication process}.
}
]

因此 AEG 的二维空间首先是一个 **typed process space**。

---

# 16. “方向”与“尺度”必须分开

最近讨论中一个重要澄清是：

[
\boxed{
\text{operation direction}
\neq
\text{calculus scale}.
}
]

AEG 中：

[
u,v
]

回答：

> 计算沿哪一种独立 operation 进行？

而 Hyperoperation calculus 中：

[
r,s
]

回答：

> 一个变化采用哪一种 process representation / infinitesimal scale 测量？

这是两个不同轴线。

例如理论未来可能同时存在：

[
\boxed{
\omega_r^{\alpha},
}
]

其中：

* (\alpha)：operation direction；
* (r)：representation/calculus scale。

因此：

[
+,\times,\uparrow
]

作为 process generators 可以产生三个 operational dimensions；

而：

[
d_1,d_2,d_3
]

又是另一套 scale hierarchy。

二者不能提前等同。

---

# 17. AEG 几何如何从操作历史产生？

Paper I 的：

[
D_u
===

\partial_u+\mu\partial_a,
]

[
D_v
===

\partial_v+\lambda a\partial_a
]

正表达：

[
+,\times
]

是两个独立 process directions，而它们共同作用于 state (a)。

交换顺序：

[
[D_u,D_v]
=========

\mu\lambda\partial_a
\neq0.
]

因此：

> 不同 calculation histories 在 process space 中形成不同路径，并且其路径差留下可测 residual。

于是：

* path；
* area；
* torsion；
* contact；
* curvature；

才自然出现。

所以 AEG operational geometry 可以理解为：

[
\boxed{
\text{显式表示多个 computation histories，
并研究这些 histories 之间的 invariant relations}.
}
]

这种几何不是物理空间的翻版。

它是：

[
\boxed{
\text{geometry generated by ways of computation}.
}
]

---

# 18. Ranked calculus 与 operational geometry 的关系目前应保持开放

一种诱人的猜测是：

[
\text{Hyperoperation infinitesimal algebra}
\to
\text{rulers}
\to
\text{operational geometry}.
]

它可能成立。

但目前不应该把它宣布为唯一层次关系。

更安全的工作图景是三条相互关联的研究线：

[
\boxed{
\text{Ranked Calculus}
}
]

研究：

[
d_r,\quad
\frac{d_s}{d_r},\quad
\mathfrak R,
\quad
\text{singular scales}.
]

[
\boxed{
\text{Operational Geometry}
}
]

研究：

[
+,\times,\uparrow,\ldots
]

作为 independent process directions 以后产生的：

[
\text{paths, brackets, torsion, curvature, topology}.
]

以及：

[
\boxed{
\text{Spatial Geometry},
}
]

研究外在 configuration/physical space。

三者之间应当逐步发现自然桥梁，而不强行预设谁必须是谁的第二层。

---

# 19. 一个更大的表征图景

目前可以暂时用四个词组织整个研究：

[
\boxed{
\text{History}
\to
\text{Compression}
\to
\text{Representation}
\to
\text{Geometry}.
}
]

### History

实际 computation trace / expression tree。

### Compression

把反复出现的稳定过程结构变成新的 primitive。

Hyperoperation 是最简单实例。

### Representation

选择 primitive vocabulary 后，一个对象与变化如何被表达和测量。

这里出现：

[
A_r,\qquad d_r,\qquad \frac{d_s}{d_r}.
]

### Geometry

当多个 process directions、多个 histories、多个 representation systems 相互作用时，研究其中与具体表达无关的结构：

* area；
* holonomy；
* curvature；
* topology；
* symmetry。

这四个阶段不是最终的理论分层，只是一张研究地图。

---

# 20. 一个可能的核心哲学命题

目前最值得保留的哲学判断或许是：

[
\boxed{
\textbf{概念可以是过程的压缩表示；
过程可以是概念的展开解释。}
}
]

Hyperoperation tower 给出了这件事情的一个极简模型：

[
\boxed{
A_r
\quad\leftrightarrow\quad
A_r^{-1}.
}
]

AEG 则强调：

> 压缩不能意味着彻底遗忘 history；被压缩掉的过程结构仍可能携带几何、拓扑和复杂性信息。

于是两个方向正好互补：

[
\boxed{
\text{AEG: decompress the history;}
}
]

[
\boxed{
\text{Hyperoperation: compress the history into a primitive.}
}
]

---

# 21. “尺度”在这个框架中的最终直觉

尺度并不是后来强加给数字的一个 metric。

它来自：

[
\boxed{
\text{在某一种 representation 中，什么算作一个 elementary step？}
}
]

一旦 elementary process unit 改变：

[
+\to\times\to\uparrow,
]

局部变化的自然单位也改变：

[
dx
\to
d\log x
\to
dA_3(x)
\to\cdots.
]

因此：

[
\boxed{
\text{process grammar}
\to
\text{process compression}
\to
\text{elementary step}
\to
\text{scale}
\to
\text{calculus}.
}
]

这可能是 Hyperoperation calculus 最简单的直观内核。

---

# 22. 当前最值得认真追问的几个问题

第一，Hyperoperation 是否只是“process compression”的一个漂亮例子，还是在某种合适的公理下具有 universal 性？

第二，能否定义真正的 representation complexity：

[
C_r(E)
]

并证明它与：

[
A_r,\qquad d_r
]

之间存在非偶然联系？

第三，rank-raising：

[
\omega_r
\to
\omega_{r+1}
]

能否不依赖具体 Abel coordinate 的选择，而在一个更抽象的 process-representation category 中定义？

第四，AEG operational directions：

[
+,\times,\uparrow,\ldots
]

与 calculus scales：

[
d_1,d_2,d_3,\ldots
]

何时真正汇合？

第五，当 operation histories 不再是 Hyperoperation 那样的简单重复，而是一般 binary tree、rewrite graph、proof/computation DAG 时，“概念压缩—过程展开”的 calculus 是否仍然存在？

这最后一个问题尤其重要，因为它决定整个方向能否从 Hyperoperation 的漂亮玩具模型扩展成真正一般的 process-representation theory。

---

# 23. 阶段性结论

我们目前看到的 Hyperoperation calculus 可以压缩成：

[
\boxed{
F_r
\overset{A_r}{\longrightarrow}
\text{unit translation}
}
]

和：

[
\boxed{
\mathrm d_r x=dA_r(x),
}
]

以及：

[
\boxed{
\frac{\mathrm d_sy}
{\mathrm d_rx}
==============

\frac{dA_s(y)}{dA_r(x)}.
}
]

它的优美之处不只在于统一了 ordinary、logarithmic、multiplicative、bigeometric 等已有 calculus。

更深的是：

[
\boxed{
A_r^{-1}\sim F_{r+1},
}
]

即：

> 前一级过程的坐标化，本身可以重新被压缩成下一阶概念。

由此产生：

[
\boxed{
\text{process}
\to
\text{measure}
\to
\text{compression}
\to
\text{new process}
\to
\text{new measure}.
}
]

AEG 则从另一个方向提醒我们：

> 每一次 compression 背后都有 history；只要不同 histories 不完全等价，它们之间便可能生成新的几何和复杂性结构。

这两个观点相遇以后，或许指向一个更大的主题：

[
\boxed{
\textbf{the mathematics of explicit process representation,
compression, and change of representation.}
}
]

Hyperoperation calculus 目前是其中最清晰、最可计算的一条切入路径；AEG operational geometry 则提供了一个关于“当 process histories 被显式保留以后，几何如何生成”的更广阔实验场。

现阶段最合适的策略仍然是保持理论结构上的开放性，同时继续把能够严格证明的局部机制——ranked differential、rank raising、singular scales、process compression 与 representation complexity——逐一坐实。
