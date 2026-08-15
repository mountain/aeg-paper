# Hyperoperation Calculus

## 分层运算、无穷小尺度与微积分递归

### Technical Research Note v0.3

**2026-08-14**

---

## 0. 目的与范围

这份笔记专门整理近期讨论中逐渐形成的 **Hyperoperation Calculus**。

重点不是重新解释 AEG 的完整哲学背景，而是把目前已经出现的数学结构、公式、例子和递推机制尽量完整地保留下来，形成一份后续可以直接继续计算的技术参照。

核心问题是：

> 如果加法、乘法、指数、tetration……分别代表不同层次的算术过程，那么每一种过程是否自然选择一种自己的无穷小尺度？这些尺度之间能否形成一套统一的微分、积分和升阶理论？

目前形成的核心链条是：

[
\boxed{
F_r
\longrightarrow
A_r
\longrightarrow
\omega_r=dA_r
\longrightarrow
\text{ranked calculus}
}
]

以及更深的递归：

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

这构成了一个候选的 **calculus-generating mechanism**。

---

# 1. Hyperoperation 的编号约定

本文采用：

[
H_1=\text{addition},
]

[
H_2=\text{multiplication},
]

[
H_3=\text{exponentiation},
]

[
H_4=\text{tetration},
]

依次类推。

固定第一个参数 (a)，把第 (r) 级运算写成 unary step map：

[
\boxed{
F_{r;a}(x):=H_r(a,x).
}
]

在上下文明确时简写为：

[
F_r.
]

基本直觉是：

[
H_{r+1}
=======

\text{iteration/compression of }H_r.
]

例如：

[
\text{multiplication}
=====================

\text{repeated addition},
]

[
\text{exponentiation}
=====================

\text{repeated multiplication},
]

[
\text{tetration}
================

\text{repeated exponentiation}.
]

---

# 2. Abel 坐标：运算的步数坐标

对于 (F_r)，寻找一个线性化坐标：

[
\boxed{
A_r(F_r(x))
===========

A_r(x)+1.
}
\tag{2.1}
]

(A_r) 称为 rank-(r) 的 Abel coordinate、linearizing coordinate 或 step-count coordinate。

在这个坐标中，任意复杂的 (F_r) 都变成最简单的：

[
t\mapsto t+1.
]

这意味着 (A_r(x)) 可以理解为：

> 状态 (x) 在第 (r) 种运算方式下相当于走到了多少个单位步骤。

记：

[
\boxed{
E_r:=A_r^{-1}.
}
]

则：

[
A_r(E_r(t))=t.
]

在标准 Hyperoperation normalization 下：

[
\boxed{
E_r\sim F_{r+1}.
}
]

于是：

[
\boxed{
F_{r+1}^{-1}\circ F_r\circ F_{r+1}
==================================

\tau,
\qquad
\tau(t)=t+1.
}
\tag{2.2}
]

每一级 Hyperoperation 都被下一级 Hyperoperation 本身共轭成平移。

---

# 3. 前两级的精确例子

## 3.1 加法

取：

[
F_1(x)=x+a.
]

可以选择：

[
A_1(x)=\frac{x}{a}.
]

于是：

[
A_1(F_1(x))
===========

# \frac{x+a}{a}

A_1(x)+1.
]

其逆：

[
E_1(t)=at.
]

这就是 multiplication。

---

## 3.2 乘法

取：

[
F_2(x)=ax.
]

选择：

[
A_2(x)=\log_a x
===============

\frac{\log x}{\log a}.
]

则：

[
A_2(ax)
=======

A_2(x)+1.
]

逆函数：

[
E_2(t)=a^t.
]

即 exponentiation。

---

## 3.3 指数

取：

[
F_3(x)=a^x.
]

其 Abel coordinate：

[
A_3(a^x)=A_3(x)+1
]

就是相应的 superlog / Fatou coordinate。

逆函数：

[
E_3=A_3^{-1}
]

则是 tetration / superfunction。

因此：

[
\boxed{
x
;\xrightarrow{\ A_1^{-1}\ };
ax
;\xrightarrow{\ A_2^{-1}\ };
a^x
;\xrightarrow{\ A_3^{-1}\ };
{}^xa
;\cdots
}
]

不是偶然函数列表，而是一列递归的 linearization inverses。

---

# 4. 每一级运算选择自己的无穷小

定义：

[
\boxed{
\mathrm d_r x
:=
dA_r(x).
}
\tag{4.1}
]

也记：

[
\boxed{
\omega_r:=\mathrm d_r x.
}
]

这是 rank-(r) operation 的自然 infinitesimal ruler。

由于：

[
A_r\circ F_r=A_r+1,
]

立即得到：

[
\boxed{
F_r^*\omega_r=\omega_r.
}
\tag{4.2}
]

所以 (\omega_r) 是被该 operation 自身保持的不变微分。

若定义 infinitesimal generator：

[
G_r(x):=\frac1{A_r'(x)},
]

则：

[
\boxed{
\omega_r
========

\frac{dx}{G_r(x)}.
}
\tag{4.3}
]

---

# 5. 前三级尺度

忽略 normalization constants 时：

### rank 1

[
A_1(x)=x,
\qquad
G_1=1,
]

因此：

[
\boxed{
\mathrm d_1x=dx.
}
]

### rank 2

[
A_2(x)=\log x,
\qquad
G_2=x,
]

因此：

[
\boxed{
\mathrm d_2x
============

# d\log x

\frac{dx}{x}.
}
]

### rank 3

若 (j(x)\partial_x) 是 exponentiation 的 iterative logarithm，则：

[
G_3=j,
]

所以：

[
\boxed{
\mathrm d_3x
============

\frac{dx}{j(x)}.
}
]

已经可以看到：

[
\boxed{
dx
\longrightarrow
\frac{dx}{x}
\longrightarrow
\frac{dx}{j(x)}
}
]

是一列 operation-generated infinitesimal scales。

---

# 6. Ranked Leibniz quotient

若：

[
y=f(x),
]

定义：

[
\boxed{
\frac{\mathrm d_s y}{\mathrm d_r x}
:=
\frac{dA_s(y)}{dA_r(x)}.
}
\tag{6.1}
]

等价地：

[
\boxed{
\frac{\mathrm d_s f}{\mathrm d_r x}
===================================

\frac{G_r(x)}
{G_s(f(x))}
f'(x).
}
\tag{6.2}
]

还可以写成几何形式：

[
\boxed{
\frac{\mathrm d_sy}{\mathrm d_rx}
=================================

\frac{f^*\omega_s}{\omega_r}.
}
\tag{6.3}
]

这里 (r) 表示 source scale，(s) 表示 target scale。

---

# 7. Chain rule：符号的第一个检验

若：

[
x\xrightarrow{f}y\xrightarrow{g}z,
]

并分别采用 ranks：

[
r,\ s,\ t,
]

则：

[
\boxed{
\frac{\mathrm d_tz}{\mathrm d_rx}
=================================

\frac{\mathrm d_tz}{\mathrm d_sy}
\frac{\mathrm d_sy}{\mathrm d_rx}.
}
\tag{7.1}
]

中间的：

[
\mathrm d_sy
]

形式上自然约去。

这也是选择 Leibniz 型 notation 的主要理由。

---

# 8. (2\times2) calculus

取：

[
A_1(x)=x,
\qquad
A_2(x)=\log x.
]

则有：

[
\boxed{
\begin{array}{c|cc}
&s=1&s=2\
\hline
r=1
&
f'
&
\dfrac{f'}f
[3mm]
r=2
&
xf'
&
\dfrac{xf'}f
\end{array}}
\tag{8.1}
]

即：

### 普通导数

[
\boxed{
\frac{\mathrm d_1f}{\mathrm d_1x}
=f'.
}
]

### logarithmic derivative

[
\boxed{
\frac{\mathrm d_2f}{\mathrm d_1x}
=================================

\frac{f'}f.
}
]

### Euler dilation derivative

[
\boxed{
\frac{\mathrm d_1f}{\mathrm d_2x}
=================================

xf'.
}
]

### elasticity

[
\boxed{
\frac{\mathrm d_2f}{\mathrm d_2x}
=================================

\frac{xf'}f.
}
]

因此几个经典算子只是：

[
\frac{\mathrm d_sy}{\mathrm d_rx},
\qquad
r,s\in{1,2}
]

的不同格子。

---

# 9. 原生 arithmetic 中的导数

[
\frac{\mathrm d_sy}{\mathrm d_rx}
]

是在 common additive / linearized coordinate 中的数值。

若要把结果重新解释为 rank-(s) arithmetic 中的量，可以施：

[
\boxed{
E_s
\left(
\frac{\mathrm d_sy}{\mathrm d_rx}
\right).
}
\tag{9.1}
]

例如：

[
E_2(u)=e^u.
]

所以：

[
\boxed{
E_2
\left(
\frac{\mathrm d_2f}{\mathrm d_1x}
\right)
=======

e^{f'/f}.
}
\tag{9.2}
]

这是 multiplicative derivative。

同理：

[
\boxed{
E_2
\left(
\frac{\mathrm d_2f}{\mathrm d_2x}
\right)
=======

e^{xf'/f},
}
\tag{9.3}
]

对应 bigeometric / proportional derivative。

---

# 10. 不定式的统一解释

普通导数：

[
f'(x)
=====

\lim_{h\to0}
\frac{f(x+h)-f(x)}{h}
]

处理：

[
0/0.
]

multiplicative derivative：

[
e^{f'/f}
========

\lim_{h\to0}
\left(
\frac{f(x+h)}{f(x)}
\right)^{1/h}
]

处理：

[
1^\infty.
]

这提示：

[
0/0
]

和：

[
1^\infty
]

并非完全无关的两个技巧，而可以视为同一个抽象 singular quotient 在不同 arithmetic realizations 中的表现。

若通过 (A_s) 搬运普通加法和乘法，定义：

[
x\oplus_s y
===========

E_s(A_s(x)+A_s(y)),
]

以及相应的：

[
\ominus_s,\quad
\otimes_s,\quad
\oslash_s,
]

则 rank-(s) 的 additive zero 为：

[
0_s:=E_s(0).
]

抽象 singular derivative 原型可以写成：

[
\boxed{
0_s\oslash_s0_s.
}
]

rank 1 中显成：

[
0/0;
]

rank 2 中则在普通 arithmetic 表示里显成：

[
1^\infty.
]

因此真正需要分类的不是经典不定式字符串，而是：

[
\boxed{
\text{不同 arithmetic scales 的 singular normal forms}.
}
]

---

# 11. Ranked integration

若：

[
\boxed{
\mathrm d_sy
============

q(x),\mathrm d_rx,
}
\tag{11.1}
]

则：

[
dA_s(y)
=======

q(x),dA_r(x).
]

积分：

[
\boxed{
A_s(y)
======

C+\int q(x),\mathrm d_rx,
}
\tag{11.2}
]

其中：

[
\int q,\mathrm d_rx
:=
\int q(x),dA_r(x).
]

因此：

[
\boxed{
y
=

E_s
\left(
C+\int q,\mathrm d_rx
\right).
}
\tag{11.3}
]

这就是 ranked primitive。

---

# 12. Ranked Fundamental Theorem

若：

[
q
=

\frac{\mathrm d_sf}{\mathrm d_rx},
]

则：

[
\boxed{
\int_{x_0}^{x_1}
\frac{\mathrm d_sf}
{\mathrm d_rx}
,
\mathrm d_rx
============

## A_s(f(x_1))

A_s(f(x_0)).
}
\tag{12.1}
]

这只是普通 fundamental theorem 在：

[
u=A_r(x),
\qquad
v=A_s(f(x))
]

坐标中的表达。

因此 regular (A_r,A_s) 情形本身属于一般的 transported / non-Newtonian calculus。

Hyperoperation calculus 的特殊性不在这一条定理，而在：

[
\boxed{
{A_r}
\text{ 不是任意坐标族，
而由 Hyperoperation iteration 递归决定。}
}
]

---

# 13. 更高 Hyperoperation 是“对常数的积分”

因为：

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
\tag{13.1}
]

因此：

[
\boxed{
E_r(t)
======

\text{rank-}r\text{ primitive of }1.
}
\tag{13.2}
]

在标准 normalization 下：

[
E_r\sim F_{r+1}.
]

所以：

[
\boxed{
\begin{aligned}
\int^{\to1}1,dt&=t,\
\int^{\to2}1,dt&=e^t,\
\int^{\to3}1,dt&=\operatorname{tet}(t),\
&\vdots
\end{aligned}}
\tag{13.3}
]

这给出了一个极简而重要的观点：

[
\boxed{
\text{Higher Hyperoperation}
============================

\text{constant primitive in a higher calculus}.
}
]

---

# 14. Constant ranked derivative 的一般解

解：

[
\boxed{
\frac{\mathrm d_sy}{\mathrm d_rx}
=================================

c
}
\tag{14.1}
]

等价于：

[
dA_s(y)
=======

c,dA_r(x).
]

所以：

[
A_s(y)=cA_r(x)+C.
]

因此：

[
\boxed{
y
=

E_s(cA_r(x)+C).
}
\tag{14.2}
]

这可以视为 ranked calculus 中的“直线”。

定义：

[
L_{r,s}^{c,C}(x)
:=
E_s(cA_r(x)+C).
]

则：

[
\boxed{
L_{s,t}^{d,E}
\circ
L_{r,s}^{c,C}
=============

L_{r,t}^{dc,dC+E}.
}
\tag{14.3}
]

因此 constant-derivative maps 自然形成一种 ranked affine composition law。

几个例子：

[
r=s=1:
\qquad
cx+C;
]

[
r=1,s=2:
\qquad
Ce^{cx};
]

[
r=s=2:
\qquad
Cx^c;
]

[
r=1,s=3:
\qquad
E_3(cx+C).
]

指数函数和 tetration 因而都可以在适当 ranked calculus 中成为“直线”。

---

# 15. 高阶导数

一阶 Leibniz quotient 很自然，但高阶不宜简单写成：

[
\frac{\mathrm d_s^ny}
{\mathrm d_rx^n},
]

因为第一次求导以后结果已落到 common scalar coordinate。

更稳妥的定义是：

[
\boxed{
D_{r\to s}^{(n)}f(x)
:=
\left.
\frac{d^n}{du^n}
\left(
A_s\circ f\circ E_r
\right)(u)
\right|_{u=A_r(x)}.
}
\tag{15.1}
]

于是有 ranked Taylor expansion：

[
\boxed{
A_s(f(x'))
==========

\sum_{n=0}^{\infty}
\frac{
D_{r\to s}^{(n)}f(x)
}{n!}
\left(
A_r(x')-A_r(x)
\right)^n.
}
\tag{15.2}
]

再施 (E_s) 即得到 target arithmetic 中的表达。

---

# 16. Rank raising：从一种 calculus 生成下一种 calculus

写：

[
\boxed{
\omega_r=q_r(x),dx.
}
\tag{16.1}
]

于是：

[
A_r'(x)=q_r(x).
]

定义：

[
F_{r+1}:=A_r^{-1}.
]

下一阶 invariant differential 必须满足：

[
\boxed{
F_{r+1}^*\omega_{r+1}
=====================

\omega_{r+1}.
}
\tag{16.2}
]

写：

[
\omega_{r+1}
============

q_{r+1}(x),dx.
]

由：

[
F_{r+1}=A_r^{-1}
]

消去 (F_{r+1})，可以得到：

[
\boxed{
q_{r+1}(x)
==========

q_r(x)
q_{r+1}(A_r(x)).
}
\tag{16.3}
]

这是目前最核心的 **calculus-generating recursion**。

---

# 17. 为什么这条递推很重要？

它说：

> 下一种 infinitesimal ruler 并不是另外发明的，而是由上一种 ruler 的 primitive 所定义的新 dynamics 的不变微分。

完整循环：

[
\boxed{
\omega_r
\xrightarrow{\int}
A_r
\xrightarrow{^{-1}}
F_{r+1}
\xrightarrow{\text{invariant differential}}
\omega_{r+1}.
}
\tag{17.1}
]

因此：

[
\boxed{
\text{measure}
\to
\text{coordinate}
\to
\text{new operation}
\to
\text{new measure}.
}
]

---

# 18. Rank 1 → 2 的直接计算

取：

[
F_1(x)=x+a.
]

选择：

[
A_1(x)=\frac xa,
]

所以：

[
q_1(x)=\frac1a.
]

递推：

[
q_2(x)
======

\frac1a
q_2(x/a).
]

一个 canonical homogeneous solution 为：

[
q_2(x)=\frac{C}{x}.
]

要求：

[
A_2(ax)-A_2(x)=1
]

给出：

[
C=\frac1{\log a}.
]

因此：

[
\boxed{
\omega_2
========

\frac{dx}{x\log a},
}
]

并：

[
\boxed{
A_2(x)=\log_a x.
}
]

所以：

[
\boxed{
dx
\xRightarrow{\text{rank raise}}
\frac{dx}{x}
}
]

由递推本身生成。

---

# 19. Rank 2 → 3：临界指数模型

选择指数 family 中的 parabolic 临界点。

固定：

[
b_*=e^{1/e}.
]

其固定点为：

[
a=e.
]

令：

[
z=\frac ae-1.
]

指数 step：

[
a\mapsto b_*^a
]

在 (z) 坐标中变成：

[
\boxed{
h(z)=e^z-1.
}
\tag{19.1}
]

而对应的 rank-2 Abel map 在同一 centered bridge 中为：

[
\boxed{
A_2(z)=\log(1+z).
}
\tag{19.2}
]

因为：

[
A_2^{-1}(z)=e^z-1.
]

相应：

[
\boxed{
\omega_2
========

\frac{dz}{1+z}.
}
\tag{19.3}
]

---

# 20. 不预设 iterative logarithm，直接生成 (\omega_3)

rank-raising recursion 为：

[
\boxed{
q_3(z)
======

\frac1{1+z}
q_3(\log(1+z)).
}
\tag{20.1}
]

设 Laurent ansatz：

[
q_3(z)
======

\frac{c_{-2}}{z^2}
+
\frac{c_{-1}}z
+
c_0
+
c_1z
+
c_2z^2
+\cdots.
]

逐阶代入可得：

[
\boxed{
c_{-1}
======

\frac16c_{-2},
}
]

[
\boxed{
c_0
===

-\frac1{72}c_{-2},
}
]

[
\boxed{
c_1
===

\frac1{540}c_{-2},
}
]

[
\boxed{
c_2
===

\frac1{5184}c_{-2}.
}
]

再用单位步 normalization：

[
\boxed{
\int_z^{e^z-1}
q_3(\zeta)d\zeta
================

1.

}
\tag{20.2}
]

最低阶给：

[
c_{-2}=2.
]

所以：

[
\boxed{
q_3(z)
======

\frac2{z^2}
+
\frac1{3z}
----------

\frac1{36}
+
\frac1{270}z
+
\frac1{2592}z^2
+\cdots.
}
\tag{20.3}
]

即：

[
\boxed{
\omega_3
========

\left(
\frac2{z^2}
+
\frac1{3z}
----------

\frac1{36}
+
\frac1{270}z
+\cdots
\right)dz.
}
\tag{20.4}
]

这一计算非常关键：

> rank-3 calculus 可以直接从 rank-2 calculus 的 raising equation 得到，而不必先把 rank-3 derivative 当成外部已知对象塞进去。

---

# 21. 与 iterative logarithm 的精确符合

对于：

[
h(z)=e^z-1,
]

iterative logarithm：

[
j(z)
====

## \frac12z^2

\frac1{12}z^3
+
\frac1{48}z^4
-------------

\frac1{180}z^5
+
\frac{11}{8640}z^6
-\cdots.
]

而：

[
\boxed{
\omega_3
========

\frac{dz}{j(z)}.
}
]

展开 (1/j) 正好得到：

[
2z^{-2}
+
\frac13z^{-1}
-------------

\frac1{36}
+
\frac1{270}z
+\cdots.
]

所以 calculus-raising recursion 与 classical iterative-logarithm construction 完全一致。

---

# 22. Rank-3 Abel coordinate

积分：

[
A_3(z)
======

\int \omega_3.
]

得到：

[
\boxed{
A_3(z)
======

-\frac2z
+
\frac13\log z
-------------

\frac1{36}z
+
\frac1{540}z^2
+\cdots.
}
\tag{22.1}
]

这里出现三种质变：

1. (1/z) 主奇异项；
2. (\log z) resonance；
3. 后面的 formal/asymptotic tail。

所以：

[
\boxed{
x
\to
\log x
\to
-\frac2x+\frac13\log x+\cdots
}
]

不仅是函数越来越复杂，而是自然坐标所需要的分析语言在升级。

---

# 23. (3\times3) calculus

在 centered rank-3 model 中取：

[
G_1(z)=1,
]

[
G_2(z)=1+z,
]

[
G_3(z)=j(z).
]

于是对任意 (f(z))：

[
\boxed{
\begin{array}{c|ccc}
&s=1&s=2&s=3\
\hline
r=1
&
f'
&
\dfrac{f'}{1+f}
&
\dfrac{f'}{j(f)}
[4mm]
r=2
&
(1+z)f'
&
\dfrac{(1+z)f'}{1+f}
&
\dfrac{(1+z)f'}{j(f)}
[4mm]
r=3
&
j(z)f'
&
\dfrac{j(z)f'}{1+f}
&
\dfrac{j(z)f'}{j(f)}
\end{array}}
\tag{23.1}
]

这是目前 rank-3 calculus 最直接的计算表。

---

# 24. 把 (h(z)=e^z-1) 代入

利用：

[
h'(z)=e^z,
]

[
1+h(z)=e^z,
]

以及 Julia relation：

[
j(h(z))
=======

e^zj(z),
]

得到：

[
\boxed{
\begin{array}{c|ccc}
&s=1&s=2&s=3\
\hline
r=1
&
e^z
&
1
&
\dfrac1{j(z)}
[4mm]
r=2
&
(1+z)e^z
&
1+z
&
\dfrac{1+z}{j(z)}
[4mm]
r=3
&
j(z)e^z
&
j(z)
&
1
\end{array}}
\tag{24.1}
]

其中两项尤其漂亮：

[
\boxed{
\frac{\mathrm d_2h}{\mathrm d_1z}=1
}
]

说明 exponentiation 是 additive-input / multiplicative-output calculus 中的“直线”；

同时：

[
\boxed{
\frac{\mathrm d_3h}{\mathrm d_3z}=1
}
]

说明 exponentiation step 在自己的 Abel calculus 中就是单位速度平移。

---

# 25. Rank 3 的 (1/3)：四种意义的汇合

在：

[
\omega_3
========

\left(
2z^{-2}
+
\frac13z^{-1}
+\cdots
\right)dz
]

中出现：

[
\frac13.
]

它积分成：

[
\frac13\log z.
]

另一方面：

[
j(z)
====

\frac12z^2
-\frac1{12}z^3+\cdots.
]

于是：

[
\frac{
-1/12
}{
(1/2)^2
}
=

-\frac13.
]

这个 (\frac13) 同时关联：

1. iterative logarithm 的三阶 relative coefficient；
2. parabolic iterative residue / resiter；
3. projective Schwarzian obstruction；
4. Abel differential 中 (dz/z) 的 logarithmic residue。

这是 rank-3 最美的一处结构汇合。

---

# 26. Projective shadow

对于一般 simple parabolic germ：

[
f(z)
====

z+az^2+bz^3+O(z^4),
]

与其具有相同二阶 jet 的 Möbius map 是：

[
m_a(z)
======

# \frac{z}{1-az}

z+az^2+a^2z^3+\cdots.
]

所以第一次离开 projective family 的量为：

[
\boxed{
b-a^2.
}
]

Schwarzian：

[
\mathcal S(f)
=============

\frac{f'''}{f'}
-\frac32
\left(
\frac{f''}{f'}
\right)^2
]

满足：

[
\boxed{
\mathcal S(f)(0)
================

6(b-a^2).
}
]

另一方面 composition logarithm：

[
\log_\circ f
============

(az^2+cz^3+\cdots)\partial_z
]

满足：

[
c=b-a^2.
]

因此：

[
\boxed{
c
=

\frac16\mathcal S(f)(0).
}
]

这说明：

> rank-3 二阶近似仍处于 projective world；三阶 Schwarzian 第一次检测到 exponentiation 真正越出 projective closure。

---

# 27. Affine → projective → Witt

定义：

[
L_n=z^{n+1}\partial_z.
]

则：

[
\boxed{
[L_m,L_n]
=========

(n-m)L_{m+n}.
}
]

rank 1、2 对应：

[
L_{-1}=\partial_z,
\qquad
L_0=z\partial_z.
]

二者形成：

[
\mathfrak{aff}(1).
]

如果 rank-3 只有首项：

[
\frac12L_1,
]

则：

[
L_{-1},L_0,L_1
]

闭合成：

[
\boxed{
\mathfrak{sl}_2.
}
]

所以：

[
\boxed{
\text{2-jet exponentiation}
\sim
\text{projective geometry}.
}
]

但真实 iterative logarithm：

[
J_3
===

\frac12L_1
-\frac1{12}L_2
+\frac1{48}L_3-\cdots.
]

一旦 (L_2) 出现：

[
[L_1,L_2]=L_3,
]

[
[L_1,L_3]=2L_4,
]

等等。

所以 formal-jet closure 打开 completed one-sided Witt algebra。

这里要保持一个重要区分：

[
\boxed{
\text{Witt 是 ambient algebra，
不是 rank-3 germ 的完整 invariant classification}.
}
]

---

# 28. Rank raising 的 cohomological form

由：

[
q_{r+1}(x)
==========

q_r(x)q_{r+1}(A_r(x))
]

定义：

[
u_r:=\log q_r.
]

则：

[
\boxed{
u_{r+1}(x)
----------

# u_{r+1}(A_r(x))

u_r(x).
}
\tag{28.1}
]

定义 Abel coboundary operator：

[
\boxed{
\mathsf B_r
:=
I-A_r^*,
}
]

其中：

[
A_r^*u=u\circ A_r.
]

于是：

[
\boxed{
\mathsf B_ru_{r+1}
==================

u_r.
}
\tag{28.2}
]

形式上：

[
\boxed{
u_{r+1}
=======

\mathsf B_r^{-1}u_r.
}
\tag{28.3}
]

这给出了固定 rank 内微积分之外的第二种“纵向积分”。

---

# 29. 两种积分

### 横向积分

固定 rulers (r,s)：

[
\mathrm d_sy=q,\mathrm d_rx.
]

求：

[
y.
]

这是：

[
\boxed{
\text{accumulation within a fixed representation system}.
}
]

### 纵向积分

求解：

[
\mathsf B_ru_{r+1}=u_r.
]

这里未知量本身是下一种 ruler density。

这是：

[
\boxed{
\text{integration that creates the next representation system}.
}
]

因此 Hyperoperation calculus 不只是“很多种导数”。

它至少包含：

[
\boxed{
\text{horizontal calculus}
+
\text{vertical rank-raising calculus}.
}
]

---

# 30. Rank raising 的形式无限乘积

反复展开：

[
u_{r+1}
=======

u_r
+
u_{r+1}\circ A_r
]

得到：

[
u_{r+1}(x)
==========

\sum_{k=0}^{n-1}
u_r(A_r^{\circ k}(x))
+
u_{r+1}(A_r^{\circ n}(x)).
]

若在适当 orbit、函数空间和 normalization 下尾项有极限，可形式理解为：

[
u_{r+1}(x)
\sim
C+
\sum_{k\ge0}
u_r(A_r^{\circ k}(x)).
]

于是：

[
\boxed{
q_{r+1}(x)
\sim
C
\prod_{k\ge0}
q_r(A_r^{\circ k}(x)).
}
\tag{30.1}
]

这提供一个很直观的解释：

> 下一阶尺度是上一阶局部尺度畸变沿 Abel dynamics 的无限累积。

---

# 31. Rank 1 → 2 的 cohomological resonance

rank 1：

[
A_1(x)=x/a.
]

而：

[
u_1=-\log a
]

是常数。

方程：

[
u_2(x)-u_2(x/a)
===============

-\log a
]

的 canonical 解为：

[
u_2(x)
======

-\log x+\text{const}.
]

因此：

[
q_2(x)\propto\frac1x.
]

所以第一次 rank raising 就产生：

[
\boxed{
\log x.
}
]

---

# 32. Rank 2 → 3 的更强 resonance

rank 2：

[
A_2(z)
======

# \log(1+z)

z-\frac12z^2+\frac13z^3-\cdots.
]

有：

[
A_2(0)=0,
\qquad
A_2'(0)=1.
]

即：

[
A_2
]

在固定点 tangent to identity。

于是：

[
I-A_2^*
]

在 local jets 上更加退化。

解出来的：

[
q_3
]

不再只是简单 (1/x)，而成为：

[
\boxed{
\frac2{x^2}
+
\frac1{3x}
+\cdots.
}
]

因此：

[
\boxed{
\text{regular}
\longrightarrow
\text{logarithmic}
\longrightarrow
\text{parabolic Laurent}.
}
]

这一奇异性升级可以被理解成连续两次 cohomological inversion 的结果。

---

# 33. Rank 3 → 4：为什么 transseries 自然出现？

Rank 3 Abel coordinate：

[
A_3(z)
======

-\frac2z
+
\frac13\log z
+\cdots.
]

当：

[
z\to0
]

时：

[
A_3(z)\to\infty.
]

下一阶 recursion：

[
\boxed{
q_4(z)
======

q_3(z)q_4(A_3(z))
}
\tag{33.1}
]

因此把：

[
q_4\text{ near }0
]

直接连接到：

[
q_4\text{ near }\infty.
]

从 rank 3 到 rank 4，纯粹 local germ category 已经不再闭合。

若测试：

[
q_4(t)\sim Ct^\beta
]

在 infinity 的行为，则：

[
A_3(z)
======

-\frac2z
\left(
1-\frac z6\log z+\cdots
\right)
]

导致：

[
q_4(A_3(z))
]

自动产生：

[
z^\alpha(\log z)^k
]

型项。

所以：

[
\boxed{
\text{rank-3 power/Laurent data}
\longrightarrow
\text{rank-4 power-log transseries}.
}
]

这解释了为什么 calculus rank 的增长可能迫使分析语言本身升级。

---

# 34. 目前看到的分析范畴升级

可以暂时写成：

[
\boxed{
\begin{array}{rcl}
r=1
&:&
\text{regular / smooth},
\
r=2
&:&
\text{logarithmic},
\
r=3
&:&
\text{meromorphic + parabolic + sectorial},
\
r=4
&:&
\text{power-log / transserial / }0\leftrightarrow\infty,
\
\vdots&&
\end{array}}
]

这还不是正式定理。

但目前的计算强烈提示：

> Hyperoperation rank 的增加，不只是数值增长速度升级，还会使自然 linearizing coordinates 所需的函数范畴逐级扩大。

---

# 35. Calculus 与过程表征

从过程表征角度：

[
A_r
]

把 rank-(r) operation 展开成：

[
\text{explicit process coordinate}.
]

而：

[
E_r=A_r^{-1}
]

把 process coordinate 重新压缩为高一级 primitive。

因此：

[
\boxed{
A_r:
\text{unfold process},
}
]

[
\boxed{
E_r:
\text{compress process}.
}
]

Hyperoperation calculus 中：

[
\mathrm d_rx=dA_r
]

便是在测量：

> rank-(r) 展开语言中的 infinitesimal process increment。

所以：

[
\frac{\mathrm d_sy}
{\mathrm d_rx}
]

可以理解为：

[
\boxed{
\text{不同过程表征层级之间的局部 conversion rate}.
}
]

---

# 36. 尺度的核心直觉

Hyperoperation calculus 中的“尺度”不是外加的 metric。

它来自：

[
\boxed{
\text{什么算作一个 elementary process step？}
}
]

rank 1：

[
x\mapsto x+a
]

是一步；

rank 2：

[
x\mapsto ax
]

是一步；

rank 3：

[
x\mapsto a^x
]

是一步。

因此：

[
\boxed{
\text{change of primitive process}
\Longrightarrow
\text{change of unit step}
\Longrightarrow
\text{change of infinitesimal ruler}.
}
]

也就是：

[
\boxed{
F_r
\to
A_r
\to
\mathrm d_rx.
}
]

---

# 37. 与普通 non-Newtonian calculus 的边界

如果任取若干光滑 bijections：

[
A_r,
]

然后定义：

[
\frac{dA_s(y)}{dA_r(x)},
]

那么这种 transported calculus 本身属于成熟的 non-Newtonian calculus 思路。

所以 Hyperoperation calculus 真正特殊的地方不能只是：

[
\text{“换一组坐标再做普通微积分”。}
]

它的特殊性必须来自：

[
\boxed{
{A_r}
\text{ 是由 Hyperoperation iteration 递归生成的一族 distinguished coordinates}.
}
]

更具体地：

[
\boxed{
A_r^{-1}\sim F_{r+1}.
}
]

以及：

[
\boxed{
\omega_r
\mapsto
\omega_{r+1}
}
]

具有 calculus-generating recursion。

这是目前最重要的原创性边界。

---

# 38. 与普通迭代理论的边界

对于：

[
e^z-1,
]

其：

* iterative logarithm；
* Abel/Fatou coordinate；
* parabolic residue；
* sectorial structure；
* Écalle–Voronin theory；

都是成熟数学。

Hyperoperation calculus 的问题不是重新发现这些对象，而是问：

> 为什么它们会在 rank-(1\to2\to3) 的微积分递推中自动出现？

以及：

> 能否把这一现象推广成一个统一的 calculus-raising theory？

所以重点从：

[
\text{classify one dynamical germ}
]

转成：

[
\boxed{
\text{classify an entire rank-generated tower of calculi}.
}
]

---

# 39. 当前最核心的公式集合

如果必须把整份笔记压成七行，我会留下：

[
\boxed{
A_r(F_r(x))=A_r(x)+1
}
]

[
\boxed{
E_r=A_r^{-1}\sim F_{r+1}
}
]

[
\boxed{
\mathrm d_rx=dA_r(x)
}
]

[
\boxed{
\frac{\mathrm d_sy}{\mathrm d_rx}
=================================

\frac{dA_s(y)}{dA_r(x)}
}
]

[
\boxed{
\mathrm d_sy=q,\mathrm d_rx
\iff
A_s(y)=C+\int q,\mathrm d_rx
}
]

[
\boxed{
q_{r+1}(x)
==========

q_r(x)q_{r+1}(A_r(x))
}
]

[
\boxed{
(I-A_r^*)\log q_{r+1}
=====================

\log q_r.
}
]

这七个式子已经包含：

* operation；
* scale；
* derivative；
* integral；
* rank raising；
* cohomological obstruction。

---

# 40. 当前最值得继续研究的问题

接下来的技术工作可以围绕几条主线展开。

第一，严格定义一个允许：

[
\omega_r\mapsto\omega_{r+1}
]

的函数范畴，并建立 existence / uniqueness / normalization theory。

第二，研究：

[
\mathsf B_r=I-A_r^*
]

的 kernel、cokernel 与 resonance，理解不同 rank 为什么产生不同 singularity classes。

第三，从 recursion：

[
q_4=q_3(q_4\circ A_3)
]

直接构造 rank-4 的第一个 power-log/transseries 解，而不是先调用既有 tetration。

第四，研究 ranked Taylor、ODE、variation、spectral decomposition 等普通分析骨架是否在：

[
r,s
]

体系中出现新的统一结构。

第五，把 representation complexity 引入，研究：

[
A_r
]

作为 process coordinate 与：

[
C_r
]

作为 optimal representation cost 之间是否存在定量联系。

---

# 41. 当前工作判断

Hyperoperation calculus 最值得重视的地方，并不是它产生了几个新的“特殊导数”。

真正值得关注的是：

[
\boxed{
\text{每一种 process representation
都会产生自己的 infinitesimal scale；
而上一种 calculus 的 primitive
又可以生成下一种 process representation。}
}
]

因此出现一个自生长回路：

[
\boxed{
\text{process}
\to
\text{scale}
\to
\text{calculus}
\to
\text{primitive}
\to
\text{new process}
\to
\text{new scale}.
}
]

如果这一循环最终可以在一个自然的代数或分析范畴中被严格公理化，那么 Hyperoperation calculus 就不再只是 ordinary calculus 的若干换元版本，而会成为：

[
\boxed{
\textbf{a calculus of recursively generated representations and scales}.
}
]

这正是下一阶段最值得检验的核心。
