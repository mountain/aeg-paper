# 从加乘几何到 Hyperoperation 线性化塔
## AEG 新分析框架研究笔记 v0.1

**日期：2026-08-14**

本文是一份工作笔记。目标不是宣布一种已经完成的新理论，而是把目前逐渐显现的数学结构压缩成一条可审计、可证伪、可继续计算的研究纲领。

全文区分三种状态：**既有**表示成熟数学理论中的已知结果；**推导**表示从现有 AEG 定义及既有理论中可以直接得到、但尚未正式写入论文的结果；**候选**表示值得继续验证的结构性判断或研究方向。

---

## 1. 动机：我们究竟在寻找什么？

AEG 最初的立场是：算术表达式不应只被看成一个最终数值，而应该保留其求值过程。Paper I 从 threadlike expressions 出发，把加法与乘法交错的计算历史几何化；在连续极限中得到 flow、双曲模型、contact structure 与 \(\delta\)-calculus。论文明确把 expression evaluation dynamics 提升为一级几何对象，并把加乘次序造成的残余理解为 arithmetic torsion。

最近几轮讨论进一步提出一个问题：

> 如果传统分析的巨大力量来自线性理论，那么 AEG 所指向的新分析是否也应该有一个足够丰富、能够长期生长的代数底座？

线性理论之所以丰富，不只是因为存在向量空间。它有一整套彼此兼容的结构：线性组合、基、坐标、线性映射、对偶、张量、商、分次、Lie 代数、表示、谱理论、同调等。

因此，我们不满足于找到一个新的导数公式或一个新的非交换括号。真正的问题是：

\[
\boxed{
\text{是否存在一套以“计算过程”为基本对象，
像线性理论一样具有生成、组合、分解、坐标、表示与不变量的结构？}
}
\]

目前逐渐形成的判断是：这种理论若存在，其基本生成原则不会是 linear combination，而更可能是

\[
\boxed{
\text{substitution}
+
\text{copying}
+
\text{iteration},
}
\]

并且必须额外保存

\[
\boxed{\text{relative structure}}
\]

——即一个高阶运算相对于已经建立的低阶运算处在什么位置。

---

## 2. Rank 1–2：Paper I 的真正数学位置

Paper I 的局部 contact model 使用

\[
\alpha
=
da-(\mu\,du+\lambda a\,dv),
\]

以及水平向量场

\[
D_u
=
\partial_u+\mu\partial_a,
\qquad
D_v
=
\partial_v+\lambda a\partial_a.
\]

它们满足

\[
[D_u,D_v]
=
\mu\lambda\partial_a.
\]

这些公式及其作为 horizontal lifts、connection curvature 的解释已经在 Paper I 中明确建立。

另一方面，Paper I 的第一类空间 \(\mathfrak E_1\) 是双曲上半平面

\[
ds^2=\frac{dx^2+dy^2}{y^2},
\qquad
a=-\frac{x}{y}.
\]



### 2.1 一个已经得到的统一化

在自然单位

\[
\tilde u=\mu u,\qquad
\tilde v=\lambda v
\]

下作变换

\[
y=e^{-\tilde v},
\qquad
x=-a e^{-\tilde v},
\]

则

\[
a=-\frac{x}{y}.
\]

而且

\[
\frac{dx}{y}
=
-da+a\,d\tilde v,
\]

所以

\[
\alpha
=
da-d\tilde u-a\,d\tilde v
=
-\left(
d\tilde u+\frac{dx}{y}
\right).
\]

因此 AEG contact manifold 可以看作双曲 \(\mathfrak E_1\) 上的一个自然 contactization：

\[
\boxed{
\mathbb R
\longrightarrow
\mathcal C_{\rm AEG}
\longrightarrow
\mathfrak E_1.
}
\]

并且

\[
d\left(\frac{dx}{y}\right)
=
\frac{dx\wedge dy}{y^2},
\]

恰好是双曲面积形式。

于是 Paper I 中原先分别出现的

\[
\mu\lambda\,du\wedge dv,
\qquad
\text{contact curvature},
\qquad
\frac{dx\wedge dy}{y^2}
\]

在 horizontal distribution 上其实是同一个二形式的不同坐标表达。

这是一个重要的简化：

\[
\boxed{
\text{arithmetic torsion density}
=
\text{contact curvature}
=
\text{hyperbolic area density}.
}
\]

### 2.2 Lie algebra 本身并不是新结构的来源

令

\[
e_1=D_u,\qquad
e_2=D_v,\qquad
e_3=\partial_a.
\]

Paper I 已算得

\[
[e_1,e_2]=\mu\lambda e_3,
\qquad
[e_1,e_3]=0,
\qquad
[e_2,e_3]=-\lambda e_3.
\]



但令

\[
z=e_1-\mu e_3=\partial_u,
\]

则 \(z\) 是中心元，因此实际上

\[
\boxed{
\mathfrak g_{\rm AEG}
\simeq
\mathbb R\oplus\mathfrak{aff}(1).
}
\]

所以真正重要的不是这个三维 Lie algebra 的同构类，而是：

\[
\boxed{
H=\operatorname{span}\{D_u,D_v\}
}
\]

这个由算术过程挑出来的非可积分二维分布。

这一点为后面的研究提供了一个原则：

> 不要把“ambient algebra 很丰富”误认为“算术结构本身很丰富”；真正的信息往往存在于被算术选择出来的 distinguished structure 中。

---

## 3. 为什么 Hyperoperation 应该进入理论核心？

采用约定

\[
H_1=+,\qquad
H_2=\times,\qquad
H_3=\exp,\qquad
H_4=\text{tetration},\ldots
\]

Hyperoperation 的根本结构不是“拥有越来越大的函数”，而是：

\[
\boxed{
\text{第 }r+1\text{ 级运算由第 }r\text{ 级运算的迭代产生。}
}
\]

固定第一个参数以后，设第 \(r\) 级 unary step map 为 \(F_r\)。离散递归具有形式

\[
H_{r+1}(a,n+1)
=
F_r(H_{r+1}(a,n)).
\]

因此 Hyperoperation rank 可以初步理解成：

\[
\boxed{
\text{recursive compression depth of computation history}.
}
\]

这使 Hyperoperation 与 AEG 的过程观点天然一致。

---

## 4. Rank raising：从迭代到下一阶运算

设一个局部可迭代映射为

\[
f:X\to X.
\]

若它具有 composition logarithm

\[
\log_\circ f
=
g(x)\partial_x,
\]

则 \(g\partial_x\) 的 time-one map 为 \(f\)。

寻找坐标 \(A_f\) 使

\[
A_f(f(x))=A_f(x)+1.
\]

对 Abel 方程求导得到 Julia equation；在形式迭代理论中，如果 \(j\) 是 iterative logarithm，则 Abel coordinate 可以由

\[
A_f'(x)=\frac1{j(x)}
\]

构造。对于 \(e^x-1\)，这一关系及 iterative logarithm 的具体展开已有系统研究。

于是形式上有

\[
A_f(x)
=
\int^x\frac{du}{g(u)}.
\]

令

\[
S_f=A_f^{-1}.
\]

则

\[
S_f(t+1)=f(S_f(t)).
\]

因此可以定义一个候选 rank-raising transformation：

\[
\boxed{
\mathcal R(f)
=
\left(
\int\frac{dx}{\log_\circ f}
\right)^{-1}.
}
\]

这不是目前意义上的全局单值函数公式；Abel coordinate 可能只有局部、形式或 sectorial 意义，而且存在规范化与分支选择。但是它把三个步骤统一起来：

\[
\boxed{
\text{composition logarithm}
\to
\text{rectifying coordinate}
\to
\text{inverse Abel map}.
}
\]

对最初两级，它给出：

\[
x\mapsto x+a
\quad\Rightarrow\quad
A_1(x)=x/a
\quad\Rightarrow\quad
S_1(t)=at,
\]

即 multiplication；以及

\[
x\mapsto ax
\quad\Rightarrow\quad
A_2(x)=\log_a x
\quad\Rightarrow\quad
S_2(t)=a^t,
\]

即 exponentiation。

第三次应用则进入 tetration。

---

## 5. Hyperoperation tower 的另一种解释：嵌套的线性化坐标

由

\[
S_r(t+1)=F_r(S_r(t))
\]

可写为

\[
F_r\circ S_r
=
S_r\circ\tau,
\qquad
\tau(t)=t+1.
\]

若局部可逆，则

\[
\boxed{
S_r^{-1}\circ F_r\circ S_r
=
\tau.
}
\]

在标准 Hyperoperation normalization 下，把 \(S_r\) 识别为下一阶运算 \(F_{r+1}\)，则有：

\[
\boxed{
F_{r+1}^{-1}
\circ
F_r
\circ
F_{r+1}
=
\tau.
}
\]

因此可以把 Hyperoperation hierarchy 重新理解为：

\[
\boxed{
\text{一列递归嵌套的 linearizing coordinates}.
}
\]

乘法在适当意义下是加法的线性化坐标；

指数是乘法的线性化坐标；

tetration 是指数的 Abel/Fatou 线性化坐标。

这一观点比“不断重复前一级运算”更接近几何语言。

---

## 6. 一个必须认真处理的类型问题

这里存在一个此前容易被整数 Hyperoperation 掩盖的问题。

Abel inverse

\[
S_r
\]

天然是

\[
S_r:T_r\to X_r,
\]

其中 \(T_r\) 是 iteration-time coordinate，而 \(X_r\) 是 state/value coordinate。

它并非天然就是

\[
X_r\to X_r.
\]

普通 Hyperoperation 在 \(\mathbb N\) 或 \(\mathbb R\) 上把 iteration count 与 arithmetic value 都表示为“数”，于是默认把两个 carrier 识别起来。

连续几何中，这种识别必须成为显式数据。

因此：

\[
\boxed{
\text{rank raising 不是普通的单类型 endofunctor。}
}
\]

更自然的代数底座应当是 multi-sorted 的，并带有一个从 time sort 到 value sort 的 rank bridge / retyping datum。

这意味着我们最终寻找的母体可能不是“一种新的代数”，而是一种**纤维化的 operation tower**。

---

## 7. Rank 3：临界指数映射

固定指数底数

\[
f_b(a)=b^a.
\]

固定点 \(p\) 满足

\[
b^p=p.
\]

其 multiplier 为

\[
f_b'(p)
=
(\log b)b^p
=
p\log b
=
\log p.
\]

要求 parabolic 临界：

\[
f_b'(p)=1,
\]

于是

\[
p=e,
\qquad
b_*=e^{1/e}.
\]

因此

\[
\boxed{
b_*=e^{1/e}
}
\]

不是任意方便的底数，而是实指数族进入 parabolic fixed-point regime 的临界值。

令

\[
z=\frac ae-1.
\]

则

\[
b_*^a
=
e^{a/e}
=
e^{1+z},
\]

所以新的局部坐标中：

\[
\boxed{
h(z)=e^z-1.
}
\]

Rank-3 的核心局部模型因此被降到一个极为标准的 parabolic germ。

---

## 8. Rank-3 iterative logarithm

\(h(z)=e^z-1\) 的 iterative logarithm 为

\[
\boxed{
j(z)
=
\frac12z^2
-\frac1{12}z^3
+\frac1{48}z^4
-\frac1{180}z^5
+\frac{11}{8640}z^6
-\frac1{6720}z^7+\cdots.
}
\]

这一展开以及

\[
A'(z)=1/j(z)
\]

在既有迭代理论文献中有明确计算。

值得注意的是：

\[
j(0)=j'(0)=0.
\]

所以 rank-3 在 parabolic point 根本不是普通的一阶 tangent direction。

它第一次出现在：

\[
\boxed{\text{second jet}.}
\]

这与我们此前提出的 semantic contact filtration 发生了直接汇合：高阶运算可能在一阶切空间中完全不可见。

---

## 9. 第一个 rank-3 phase transition：有限维到无限维

考虑

\[
\mathfrak L
=
\operatorname{Lie}
\langle
\partial_z,\,
z\partial_z,\,
j(z)\partial_z
\rangle.
\]

这里有一个可以独立证明的命题：

### 命题

若解析函数 \(g\) 满足

\[
\operatorname{Lie}
\langle
\partial_z,\,
z\partial_z,\,
g(z)\partial_z
\rangle
\]

有限维，则 \(g\) 必须是次数至多二次的多项式。

### 证明思路

令 \(V\) 为该 Lie algebra 中所有向量场系数函数组成的有限维空间。

因为

\[
[\partial_z,g\partial_z]
=
g'\partial_z,
\]

所以 \(V\) 对

\[
D=\frac d{dz}
\]

封闭。

又因为

\[
[z\partial_z,g\partial_z]
=
(zg'-g)\partial_z,
\]

所以 \(V\) 对 \(zD-1\) 封闭。

在有限维空间中

\[
[zD-1,D]=-D.
\]

因此 \(D\) 把 \(zD-1\) 的广义特征空间沿整数方向平移；有限维性迫使足够高次的 \(D\) 为零。所以 \(V\) 中所有元素都是多项式。

若存在最高次数 \(n\ge3\) 的元素 \(p\)，则 \(p'\in V\)，而

\[
[p\partial_z,p'\partial_z]
\]

的最高次数为 \(2n-2>n\)，矛盾。

故最高次数不超过二次。

---

而 rank-3 generator \(j\) 满足 Julia equation，不可能是非零二次多项式。因此：

\[
\boxed{
\mathfrak L
\text{ 必然无限维。}
}
\]

这是 rank-2 到 rank-3 的第一个严格 phase transition：

\[
\boxed{
+\,,\times
\quad\leadsto\quad
\mathfrak{aff}(1),
}
\]

而

\[
\boxed{
+\,,\times,\exp
\quad\leadsto\quad
\text{infinite-dimensional local derivation algebra}.
}
\]

---

## 10. Affine → projective → Witt

定义

\[
L_n=z^{n+1}\partial_z,
\qquad n\ge-1.
\]

则

\[
[L_m,L_n]
=
(n-m)L_{m+n}.
\]

rank-1 和 rank-2 给出：

\[
L_{-1}=\partial_z,
\qquad
L_0=z\partial_z.
\]

如果 rank-3 generator 只有首项

\[
J_{\rm proj}
=
\frac12L_1,
\]

那么

\[
L_{-1},L_0,L_1
\]

恰好闭合成：

\[
\boxed{\mathfrak{sl}_2.}
\]

因此 rank-3 的 **2-jet shadow** 是 projective geometry。

但是实际的 iterative logarithm 为：

\[
J_3
=
\frac12L_1
-\frac1{12}L_2
+\frac1{48}L_3-\cdots.
\]

只要 \(L_2\) 出现，

\[
[L_1,L_2]=L_3,
\qquad
[L_1,L_3]=2L_4,
\]

所有更高 mode 被逐步打开。

在 \(z\)-adic completion 中，可利用

\[
[L_0,L_n]=nL_n
\]

及 polynomial spectral projection 逐阶隔离 \(L_1,L_2,\ldots\)，从而得到：

\[
\boxed{
\overline{
\operatorname{Lie}
\langle
L_{-1},L_0,J_3
\rangle
}
=
\mathbb C[[z]]\partial_z.
}
\]

也就是 completed one-sided Witt algebra。

但必须强调：

> **completed Witt 是 ambient algebra，不是 rank-3 germ 的完整不变量空间。**

一维 parabolic germ 的 formal conjugacy classification 远比整个 Witt algebra 刚性；真正的 analytic classification 还涉及 sectorial Écalle–Voronin modulus。

因此不能从“ambient algebra 无限维”直接推出“rank-3 有无限多个独立 formal invariants”。

---

## 11. 相对结构：为什么 AEG 不应孤立分类 rank-3

若单独研究 \(J_3\)，可以使用很大的 formal coordinate-change group 把许多高阶项正规化掉。

但是 AEG/Hyperoperation 已经拥有 rank-1、2：

\[
\mathfrak a
=
\operatorname{span}
\{\partial_z,z\partial_z\}.
\]

所以真正对象不是 \(J_3\)，而是：

\[
\boxed{
(\mathfrak a,J_3).
}
\]

要求局部坐标变换保持基点 \(0\) 和 lower-rank affine structure：

\[
\phi_*\mathfrak a=\mathfrak a.
\]

由

\[
\phi_*(z\partial_z)
=
z\phi'(z)\partial_w
\]

可得

\[
z\phi'(z)=\phi(z),
\]

因而：

\[
\boxed{
\phi(z)=\lambda z.
}
\]

即一旦 lower ranks 被固定，gauge group 从任意 formal diffeomorphism 急剧下降为 scaling。

这一点非常关键：

\[
\boxed{
\text{复杂性不在单个 operation 的孤立共轭类，
而在不同 operation ranks 的相对位置。}
}
\]

---

## 12. Rank-3 operation frame 与相对坐标

定义一个初步的 rank-3 operation frame：

\[
\boxed{
\mathfrak F_3
=
(\partial_z,\,
z\partial_z,\,
J_3).
}
\]

写

\[
J_3
=
\left(
c_2z^2+c_3z^3+c_4z^4+\cdots
\right)\partial_z.
\]

尺度变换 \(w=\lambda z\) 使

\[
c_n
\mapsto
\lambda^{1-n}c_n.
\]

因此无量纲组合

\[
\boxed{
\kappa_n
=
\frac{c_n}{c_2^{\,n-1}},
\qquad n\ge3
}
\]

在 lower-rank preserving coordinate changes 下保持不变。

对 \(e^z-1\)：

\[
\kappa_3=-\frac13,
\qquad
\kappa_4=\frac16,
\qquad
\kappa_5=-\frac4{45},
\ldots
\]

这些数不应被立即宣布为最终 canonical invariants；未来更自然的表达可能来自 Schwarzian、higher Schwarzian 或 Cartan-type differential invariants。但它们已经提供一个明确的 relative coordinate system。

---

## 13. 第三阶门槛与 Schwarzian

设一般 simple parabolic germ：

\[
f(z)
=
z+az^2+bz^3+O(z^4).
\]

与它具有相同二阶 jet 的 projective/Möbius germ 为

\[
m_a(z)
=
\frac{z}{1-az}
=
z+az^2+a^2z^3+\cdots.
\]

因此偏离 projective geometry 的第一次差异为：

\[
b-a^2.
\]

Schwarzian derivative 为

\[
\mathcal S(f)
=
\frac{f'''}{f'}
-\frac32
\left(\frac{f''}{f'}\right)^2.
\]

代入 \(0\)：

\[
\boxed{
\mathcal S(f)(0)
=
6(b-a^2).
}
\]

Schwarzian 是 projective line 上的三阶完整微分不变量，其 kernel 正是 Möbius/projective transformations。

另一方面，若 composition logarithm 写成

\[
\log_\circ f
=
(az^2+cz^3+\cdots)\partial_z,
\]

展开 time-one map 得

\[
c=b-a^2.
\]

所以：

\[
\boxed{
c
=
\frac16\mathcal S(f)(0).
}
\]

这意味着我们此前发现的 rank-3 third-order obstruction，其经典几何本质就是：

\[
\boxed{\text{projective Schwarzian defect}.}
\]

对于 \(e^z-1\)，

\[
\mathcal S(e^z-1)=-\frac12.
\]

在本文 normalization 下：

\[
\kappa_3=-\frac13.
\]

它与 simple parabolic dynamics 中的 iterative residue/resiter 是同一类三阶形式数据；文献中的符号和 normalization 有数种约定，正式论文需要统一 convention，而本文暂时采用

\[
\gamma:=-\kappa_3
\]

作为 residue parameter。parabolic germ 的 formal class 由 tangency order 与 residue-type data 控制，而完整 holomorphic classification 还需要无限维 sectorial invariants。

---

## 14. 一个“operation spectrum”

lower-rank dilation generator

\[
E=z\partial_z
\]

作用在

\[
L_n=z^{n+1}\partial_z
\]

上满足：

\[
\boxed{
[E,L_n]=nL_n.
}
\]

因此 \(L_n\) 是 \(\operatorname{ad}_E\) 的 weight mode。

于是

\[
J_3
=
\sum_{n\ge1}d_nL_n
\]

可以被理解成相对于 lower-rank scale operation 的一个谱分解。

这提示定义：

\[
\boxed{
\operatorname{Spec}_{\rm op}(J_3)
=
\{n:d_n\neq0\}.
}
\]

这里不是把状态向量分解成 eigenvectors，而是：

> **把一个高阶 operation 相对于 lower-rank dilation frame 分解成不同的 operation-scale modes。**

而

\[
[L_m,L_n]
=
(n-m)L_{m+n}
\]

说明不同 weight 在 bracket 下发生加法组合。

这可能是未来与线性谱理论对应最有潜力的一根梁。

---

## 15. Rank 3 的 analytic 层：formal theory 并不够

对于

\[
h(z)=e^z-1,
\]

iterative logarithm 不只是复杂，而且具有很强的 transcendence 性质。已知结果表明，非线性 entire function 的 iterative logarithm 在适当意义下是 differential-transcendental；\(e^z-1\) 是其中的重要例子。

另一方面，simple parabolic germ 的 Fatou coordinate 不是一个全局普通 Taylor series。它自然在不同 petals 上形成 sectorial Abel coordinates；不同 sectorial coordinates 之间的差异产生 Écalle–Voronin invariants，而这些 functional invariants完成了 analytic conjugacy classification。

所以 rank-3 至少包含三层：

\[
\boxed{
\begin{array}{c}
\text{2-jet}\\
\downarrow\\
\text{projective shadow}
\\[2mm]
\text{formal germ}\\
\downarrow\\
\text{iterative logarithm / residue / Witt ambient algebra}
\\[2mm]
\text{analytic germ}\\
\downarrow\\
\text{Fatou sectors / Écalle--Voronin modulus}.
\end{array}
}
\]

AEG 若继续发展，必须明确自己在哪一层工作，而不能把 formal、analytic 和 global structure 混为一谈。

---

## 16. Rank 3 → Rank 4：jet 变成 transseries

将 rank-3 generator 归一化为：

\[
J_3
=
\left(
u^2+\kappa_3u^3+\kappa_4u^4+\cdots
\right)\partial_u.
\]

则 Abel coordinate 满足：

\[
A'(u)
=
\frac1{
u^2+\kappa_3u^3+\kappa_4u^4+\cdots
}.
\]

形式展开：

\[
A'(u)
=
u^{-2}
-\kappa_3u^{-1}
+
(\kappa_3^2-\kappa_4)
+O(u).
\]

积分得：

\[
\boxed{
A(u)
=
-\frac1u
-\kappa_3\log u
+
(\kappa_3^2-\kappa_4)u
+O(u^2).
}
\]

在 parabolic dynamics 中，Fatou coordinates 具有“principal inverse-power term + residue \(\times\log\) + 后继渐近项”的标准结构；其逆函数自然产生 power-log asymptotics。

现在令

\[
S=A^{-1}.
\]

固定 additive normalization 与 log branch 后，反演的开头为：

\[
\boxed{
S(t)
=
-\frac1t
-\kappa_3\frac{\log t}{t^2}
+
O(t^{-2}).
}
\]

更高阶会产生：

\[
\frac{(\log t)^2}{t^3},
\qquad
\frac{\log t}{t^3},
\qquad
\frac1{t^3},
\ldots
\]

且系数由

\[
\kappa_3,\kappa_4,\ldots
\]

以三角方式递归决定。

因此出现一个很值得继续正式化的 transfer principle：

\[
\boxed{
\text{rank-3 power-jet data}
\quad\longrightarrow\quad
\text{rank-4 power-log transseries data}.
}
\]

尤其：

\[
\boxed{
\text{rank-3 的三阶 projective obstruction}
\longrightarrow
\text{rank-4 的首个 logarithmic asymptotic correction}.
}
\]

这意味着 rank raising 并不会简单“忘掉”低 rank 的相对不变量，而可能把它们转换成更高 rank 的不同类型数据。

---

## 17. 为什么 rank-4 以后不能只研究 Lie closure？

Rank-3 相对于 affine pair 已经在形式闭包意义下打开 completed Witt algebra。

因此如果只问：

\[
\text{加入 rank-4 后 Lie algebra 是否变得更大？}
\]

这个问题很可能已经失去区分能力。

换言之：

\[
\boxed{
\text{Lie closure 在 rank-3 已基本饱和。}
}
\]

所以 Hyperoperation rank 不能由 ambient Lie algebra 的维数来编码。

真正需要保存的是：

\[
\boxed{
\text{distinguished generators}
+
\text{rank labels}
+
\text{iteration relations}
+
\text{relative positions}.
}
\]

这进一步支持 operation frame / operation tower 而不是单一 Lie algebra 作为基础对象。

---

## 18. “线性化 atlas”及其 transition geometry

设不同 rank 的 Abel coordinates 为

\[
A_r.
\]

在共同可比较的局部或 sectorial domain 上，可以定义 transition map：

\[
\boxed{
T_{rs}
=
A_s\circ A_r^{-1}.
}
\]

显然：

\[
T_{rt}
=
T_{st}\circ T_{rs}.
\]

所以 Hyperoperation ranks 可以形成一套 rank-dependent linearizing atlas。

若

\[
G_r=\frac1{A_r'},
\]

定义：

\[
\Omega_{rs}
=
G_rG_s'-G_sG_r'.
\]

令

\[
t=A_r(x).
\]

由于：

\[
T_{rs}'(t)
=
\frac{G_r(x)}{G_s(x)},
\]

得到：

\[
\boxed{
\partial_{A_r}
\log T_{rs}'
=
-\frac{\Omega_{rs}}{G_s}.
}
\]

因此此前从 Lie bracket 得到的

\[
\Omega_{rs}
\]

具有一个更精确的几何解释：

> **它测量不同 rank linearizing coordinates 之间的 affine incompatibility。**

Paper I 的

\[
\mu\lambda
\]

正是 rank-1 / rank-2 情形中的最低级实例。

这可能是连接 AEG 与 Hyperoperation theory 最直接的一条公式。

---

## 19. 重新审视代数底座

到目前为止，至少出现了两个不同但必须耦合的世界。

### History side

算术表达式天然是树，而且 distributivity

\[
x(y+z)\to xy+xz
\]

会复制变量 \(x\)。

因此普通 operad 并不是最自然的母体，因为 operadic substitution 本身不负责变量任意复制与删除。clone / cartesian operad / Lawvere theory 正是处理这种 cartesian variable management 的标准结构；clones 与 Lawvere theories 有直接等价关系。

而若不把 rewrite equality 立即 quotient 掉，而保存

\[
E\Rightarrow F
\]

及不同 rewrite paths 之间的 relations，则自然进入 polygraph / higher rewriting。该理论专门把 generators、rewrites、relations-among-rewrites 与 coherence/homotopy 组织为高维结构。

表达式树线性化后又自然与 rooted-tree pre-Lie 和 Hopf algebra 接轨；rooted trees 是 free pre-Lie structures 与多个经典 tree Hopf algebras 的基本组合模型。

### Semantic side

局部函数复合自然由 formal diffeomorphism group 与 Faà di Bruno 型 Hopf algebra 控制；Faà di Bruno Hopf algebra 的基本功能正是编码 formal diffeomorphism composition。

iterative logarithm 又和 pre-Lie Magnus expansion 有直接关系。

因此 history side 与 semantic iteration side 并非只有表面类比。它们之间可能存在一个真正值得寻找的 pre-Lie / Hopf realization bridge。

---

## 20. 一个更合适的母体：纤维化 operation tower

目前最小候选不再是“一个带 iteration 的 Lawvere theory”，而是一个跨 rank 的纤维化结构：

\[
\boxed{
\mathcal T
\longrightarrow
\mathbb N_{\rm rank}.
}
\]

每个 rank fiber \(\mathcal T_r\) 中有：

\[
\text{substitution},
\quad
\text{copying},
\quad
\text{rewrite/coherence},
\]

而 rank 之间存在一个非平凡的 rank-raising correspondence：

\[
\mathcal R_r:
\mathcal T_r
\dashrightarrow
\mathcal T_{r+1},
\]

它需要 Abel normalization、branch/sector choice 以及 time/value retyping data。

同时存在 semantic realization：

\[
\boxed{
\rho:
\mathcal T
\longrightarrow
\mathcal S,
}
\]

把 computation histories 送到 semantic maps、jets、flows、transseries 与 sectorial objects。

这里的虚线箭头是有意的：rank raising 很可能不是普通单值 functor，而更接近带 gauge/normalization 的 correspondence。

---

## 21. History → semantics：可能真正属于 AEG 的地方

这是目前最需要与既有理论区分开的部分。

单独研究：

\[
e^z-1,
\]

其 parabolic dynamics、iterative logarithm、Fatou coordinates、Écalle–Voronin classification 都属于成熟的迭代理论。

单独研究：

\[
\text{rooted trees},
\]

其 operad、pre-Lie、Hopf structure 也已有成熟理论。

真正可能属于 AEG 的问题是：

\[
\boxed{
\text{Arithmetic History Theory}
\xrightarrow{\rho}
\text{Semantic Dynamics}
}
\]

并研究这个 realization map 如何同时尊重：

\[
\text{substitution},
\quad
\text{copying},
\quad
\text{iteration},
\quad
\text{rewrite},
\quad
\text{rank raising},
\quad
\text{jet filtration}.
\]

此前得到的几个 AEG 量都可能重新解释成这个 realization 的不同信息损失：

\[
\text{multiplicity}
\]

测量多个 histories 向同一 semantic object 的坍缩；

\[
(\nu,\sigma)
\]

测量两个 histories 在 semantic jet filtration 中第一次分开的阶数和 principal defect；

\[
\mu\lambda
\]

是 add/multiply process 在二阶留下的最初 infinitesimal residue；

而 Hyperoperation relative invariants 则描述不同 rank operations 在同一 semantic geometry 中的相对位置。

---

## 22. 与线性理论的更准确对照

现在可以作一个比最初更成熟的比较：

| 线性理论 | 候选 operation theory |
|---|---|
| vector | computation / operation |
| vector space | history/operation fiber |
| basis | lower-rank operation frame |
| coordinates | rank-dependent Abel coordinates |
| change of basis | transition \(A_sA_r^{-1}\) |
| linear combination | substitution + copying + iteration |
| linear map | history/semantic realization |
| kernel | histories invisible to a semantic representation |
| grading | operation rank / jet weight |
| eigenmode | \(\operatorname{ad}_{z\partial_z}\)-weight mode |
| spectrum | relative operation spectrum |
| affine/projective structure | lower-rank operation geometry |
| curvature | transition cocycle / \(\Omega_{rs}\) |
| Taylor expansion | relative jet profile |
| asymptotic analysis | rank-raised transseries |
| monodromy/Stokes | sectorial/horn-map data |
| homological algebra | rewrite coherence / polygraphic homology |

这个对照目前仍是研究导航，不是定义。

但它指出一个重要的目标：

> 最终理论必须像线性理论一样，让这些对象不是人工拼接，而是从少数几个基本公理或 universal property 自然导出。

---

## 23. 当前最重要的四个阶段性结果

目前最值得正式证明和写入未来论文的工作命题，可以压成下面四个。

**A. Rank-raising principle**

\[
\boxed{
\mathcal R(f)
=
\left(
\int dx/\log_\circ f
\right)^{-1}
}
\]

在明确的 formal/sectorial category、normalization 与 typing 条件下成立。

**B. Rank-3 phase-transition theorem**

\[
\boxed{
\operatorname{Lie}
\langle
\partial_z,z\partial_z,J_3
\rangle
}
\]

对临界 exponentiation 不可能有限维，并在 formal-jet closure 中产生 completed Witt algebra。

**C. Relative projective-obstruction theorem**

若

\[
f=z+az^2+bz^3+\cdots,
\]

则

\[
\boxed{
b-a^2
=
\frac16\mathcal S(f)(0)
}
\]

同时也是 composition logarithm 的首个 non-projective coefficient；在适当 normalization 中对应 iterative residue。

**D. Jet-to-transseries transfer principle**

若

\[
J
=
u^2+\kappa_3u^3+\kappa_4u^4+\cdots,
\]

则 rank raising 产生

\[
\boxed{
A(u)
=
-\frac1u-\kappa_3\log u+\cdots,
}
\]

并进一步使 \(A^{-1}\) 出现

\[
\boxed{
-\kappa_3\frac{\log t}{t^2}
}
\]

等 power-log terms。

这意味着低 rank 的 jet obstruction 会以新的形式进入高 rank asymptotics。

---

## 24. 下一阶段研究计划

接下来不宜直接追求 pentation 的数值计算。优先顺序应当是：首先完成 rank-3 formal foundations，包括 operation frame 的严格定义、允许的 gauge group、finite-dimensional obstruction theorem、relative spectrum 以及 Schwarzian/residue 关系；随后完成 rank-3 analytic layer，明确 \(e^z-1\) 的 sectorial Fatou coordinates、formal data 与 Écalle–Voronin modulus 在“relative to affine frame”条件下究竟保留哪些信息；第三步正式建立 rank-raising category，区分 time/value sorts，处理 normalization、seed、branch 和 sector choices，并证明 rank-3 jet 到 rank-4 transseries 的一般递推公式；第四步再回到 history side，构造最小 multi-sorted cartesian arithmetic theory 与 higher rewrite structure，寻找从 expression trees/pre-Lie structures 到 semantic iteration/pre-Lie Magnus structures 的自然 realization；最后才进入 rank-4、rank-5，检查 higher Hyperoperations 是否产生新的不变量类型，而不是简单落入 rank-3 已经打开的 completed Witt ambient algebra。

---

## 25. 必须主动攻击的几个风险

这条路线当前最大的危险不是计算困难，而是“把很多漂亮的成熟理论拼起来以后误认为产生了新理论”。

因此以后每一步都必须问：

**第一，arithmetical specificity 在哪里？**

如果结果对任意 parabolic germ 都成立，那么它属于迭代理论，不属于 AEG 的新内容。AEG 的特殊性必须来自：

\[
+\to\times\to\exp\to\cdots
\]

这条 arithmetic rank relation，或者来自 expression-history realization。

**第二，rank raising 是否足够 canonical？**

Abel functions 通常涉及 normalization、branch 和 sector。若没有自然的 arithmetic normalization，那么所谓 Hyperoperation geometry 可能依赖人为 gauge choice。

**第三，relative invariants 是否真的有 universal meaning？**

固定 lower-rank frame 会保留更多 jet 信息，但必须证明这种 frame 是由 arithmetic structure 内禀决定，而不是为了保留信息而人为限制 coordinate group。

**第四，rank-4 是否真的增加新结构？**

Lie closure 已在 rank-3 饱和。rank-4 的价值必须表现为新的 filtration、transseries、sectorial data、typing structure 或 history relation，而不能只是“又一个 Witt algebra 元素”。

**第五，history side 与 semantic side 是否存在自然的兼容映射？**

这是目前最关键的成败点。若不存在一个自然 transformation/universal property 把 tree/rewrite/iteration 与 semantic jet/flow/Abel structures 联结起来，那么整个“大代数底座”仍可能只是一组并列的工具。

---

## 26. 当前工作假说

综合目前结果，可以提出一个相对克制但足够明确的工作假说：

\[
\boxed{
\textbf{Arithmetic operations form a ranked hierarchy of mutually
linearizing processes.}
}
\]

每一级 operation：

1. 有自己的 natural linearizing coordinate；
2. 相对于低阶 operation frame 具有不可约的 relative differential data；
3. rank raising 会把这些 data 转化为下一层不同类型的渐近或 sectorial structure；
4. 一般 arithmetic expressions 又把这些 unary operation processes 组合成 branching histories；
5. evaluation 将 history structure 投影到 semantic dynamics，产生 multiplicity、contact defects、curvature 与其他信息残余。

因此候选的新分析学不应定义为“非线性版线性分析”，而更可能是：

\[
\boxed{
\textbf{an analysis of ranked computation histories
through their relative linearizations and semantic realizations.}
}
\]

---

## 27. 最核心的图景

目前整个研究可以压缩成：

\[
\boxed{
\begin{array}{cccccc}
\text{History}
&\to&
\text{Operation}
&\to&
\text{Iteration}
&\to
\\[1mm]
\text{tree/rewrite}
&&
\text{rank frame}
&&
\text{Abel linearization}
&
\\[1mm]
&&\downarrow&&\downarrow&
\\[-1mm]
&&
\text{relative jet}
&\to&
\text{rank raising}
&\to
\text{transseries/sectorial data}
\\[1mm]
&&\downarrow&&&
\\[-1mm]
&&
\text{semantic realization}
&&&
\end{array}
}
\]

Paper I 的

\[
\mu\lambda
\]

位于这张图的最低非平凡处。

Rank-3 的

\[
-\frac1{12}
\]

则是第一次越出 projective closure 的三阶信号。

而 tetration 中出现的 logarithmic asymptotics 告诉我们：**rank raising 不只是让函数增长得更快，而会改变描述运算所需要的数学语言本身。**

从 affine geometry 到 projective geometry，从 formal diffeomorphisms 到 transseries/resurgence，这种“描述语言随 operation rank 升级”的现象，可能正是下一阶段最值得追踪的主轴。

---

## 28. 问答阶段建议

后续理解与质疑可以从任意层进入，但最值得重点盘问的其实只有几个核心节点：为什么 rank raising 等价于 Abel inverse；为什么 lower-rank frame 应被视为结构而不能任意坐标化掉；为什么 rank-3 的二阶 shadow 是 projective 而三阶 Schwarzian第一次破坏 projective closure；为什么 completed Witt 只是 ambient algebra；为什么 rank raising 会把 jet data 转换成 logarithmic/transseries data；以及 history side 的 copying/rewrite structure 如何可能与 semantic pre-Lie/iteration structure 真正连接。

如果这些节点经得住反复质疑，那么这条研究路线值得继续发展；若其中任一关键兼容性失败，也能相当明确地指出理论应当在哪一层收缩。