# 51 — 复化基本模型与 Riemann–Hilbert 边界：C1 主文与 C2 伴随模型

**状态**：研究笔记（research note），承接
[50 — Paper II 的复域与任意域扩充](50-complex-and-arbitrary-field-extension.md)。
它不是论文源文件，不进入 `governance/` 的状态登记，不改变 Paper II 的任何
定理状态。文中的新陈述逐条标注状态；证明写到笔记所需的程度，正式论文必须另写。

**日期**：2026-11-07

**依赖**：note 50 的三层框架（Layer A/B/C）与 C1/C2 区分；Paper 0 的
`prop:canonical-arithmetic-frame`、`prop:p0-projective-trichotomy`；Paper II 的
`prop:hyperbolic-analytic-normalization`、`thm:C0-poisson-dirichlet` 及其
DtN/能量结果；Paper III 的奇异零轨迹接口。

**配套脚本**：`51-complexified-model-and-rh-witness.py`（本目录；21 项全部通过）。

---

## 0. 摘要与结论

本篇把 note 50 的两条主线具体化：

1. **C1 复化基本模型**。它是实双曲平面 $\mathbb H^2$ 的复化，而不是
   $\mathbb H^3$：
   $$
   M=\{(w,\bar w)\in\mathbb C^2:w\ne\bar w,\ w\bar w\ne0\},
   $$
   $$
   g=-\frac{4}{\lambda^2}\frac{dw\,d\bar w}{(w-\bar w)^2},
   \qquad
   a=-\frac{i\mu}{\lambda}\frac{w+\bar w}{w-\bar w}.
   $$
   我们证明：eikonal、框架、括号、Laplace 公式、$q^2$ 公式、
   $\bar\partial_{\!AEG}=-\lambda y\partial_{\bar w}$、曲率 $K=-\lambda^2$ 全部
   是实模型的复化；$g$ 在对角 $\operatorname{PGL}_2(\mathbb C)$ 作用下不变；
   实切片 $w=X+iy$（$y>0$）逐字回到 Paper II 的基本模型。
   $q=0$ 的除子是 $w\bar w=0$，在 $w=0$ 处 $\nabla a\ne0$ 但迷向——这是实理论
   不可能出现的新现象，只能在奇异延拓中见到。

2. **C1 的边界理论是 Riemann–Hilbert，不是 $L^2$ Dirichlet**。
   Poisson 核是 Cauchy 核的跳跃；Dirichlet 问题就是跳矩阵 $G=-1$ 的
   Riemann–Hilbert 问题；Schwarz 积分给出全纯解；DtN 是 Hilbert 变换
   $|D|=HD$；能量仍是 $H^{1/2}$。在 $C_0\cap L^1$ 类上我们证明 C1 版本的
   Dirichlet/Schwarz 定理。矩阵跳与"内禀复边界"（对角线
   $D=\{w=\bar w\}$ 上的 RH 问题）是 `STRUCTURAL PROPOSAL`/`OPEN`。

3. **C2 不只是 no-go，它有一个完备的基本模型**。取
   $$
   M=\mathbb C,\qquad a(z)=z,\qquad
   g=\frac{|dz|^2}{\mu^2+\lambda^2|z|^2}.
   $$
   则它是 Hermitian 正则 AES：
   $$
   |\nabla a|^2=\mu^2+\lambda^2|a|^2,\qquad
   K=\frac{2\lambda^2\mu^2}{\mu^2+\lambda^2|a|^2}>0,
   $$
   度量完备，总曲率 $2\pi$，零轨迹是单点 $\{0\}$，且度在 $0$ 处光滑。
   这是与实基本模型（$K=-\lambda^2<0$，零轨迹是测地线）完全不同的 Hermitian
   模型。对任意 Hermitian 度量，全纯场仍调和（二维共形不变性），所以 C2 有
   真正的函数论，只是它的边界问题是正定椭圆的 Dirichlet/Poisson，而不是 RH。

**三种基本模型的对照**（详见 §5）：

| | 实基本模型 | C1 复化 | C2 Hermitian |
|---|---|---|---|
| 曲率 | $-\lambda^2<0$ | $-\lambda^2$（全纯） | $>0$，趋向 $0$ |
| 零轨迹 | 测地线 $X=0$ | 复曲线 $\operatorname{Re}w=0$ | 单点 $\{0\}$ |
| 完备性 | 完备 | 无正定距离 | 完备 |
| 边界理论 | Poisson/Dirichlet | Riemann–Hilbert/Schwarz | Dirichlet/Poisson |
| 总曲率 | $-\infty$（无限面积） | — | $2\pi$ |

---

## 1. C1：复化基本模型

### 1.1 定义

**定义 1.1（复化基本模型）**。固定 $\mu\in\mathbb C^\times$、$\lambda\in\mathbb C^\times$
（本篇只处理 $\lambda\ne0$；$\lambda=0$ 时 $g$ 的公式退化，是另一个平坦模型）。
取
$$
M=\{(w,\bar w)\in\mathbb C^2:\ w\ne\bar w,\ w\bar w\ne0\},
$$
$$
g=-\frac{4}{\lambda^2}\frac{dw\,d\bar w}{(w-\bar w)^2},
\qquad
a=-\frac{i\mu}{\lambda}\frac{w+\bar w}{w-\bar w},
\qquad
q^2:=\mu^2+\lambda^2a^2 .
$$
这里 $dw\,d\bar w$ 是对称双线性积；$(w,\bar w)$ 是两个独立复坐标，直到取
实切片时才令 $\bar w$ 为 $w$ 的复共轭。令
$$
y=\frac{w-\bar w}{2i},\qquad X=\frac{w+\bar w}{2}.
$$
取 $q=2i\mu\sqrt{w\bar w}/(w-\bar w)$ 的一个全纯分支（在 $w\bar w\ne0$ 上），
并取 $\mathbb C^2$ 的标准复结构 $J$。称
$(M,g,a;\mu,\lambda;q,J)$ 为**复化基本模型**。

**注 1.1**。$M$ 排除 $w=\bar w$（对角线，理想边界的复化）与 $w\bar w=0$
（$q$-正规化的极除子）。在 $M$ 上 $q\ne0$，所以
$(\nabla a)^2=q^2\ne0$，故 $\nabla a\ne0$：$a$ 是浸没，水平集是复曲线。

### 1.2 基本计算

**命题 1.1**。在定义 1.1 的数据下：

1. $(\nabla a)^2=\mu^2+\lambda^2a^2$；
2. $\Delta_g a=2\lambda^2a$；
3. 框架
   $$
   X_u=-\lambda y(\partial_w+\partial_{\bar w}),\qquad
   X_v=-i\lambda y(\partial_w-\partial_{\bar w})
   $$
   满足 $X_u a=\mu$、$X_v a=\lambda a$，且
   $$
   [X_u,X_v]=\lambda X_u;
   $$
4. $\Delta_g=X_u^2+X_v^2+\lambda X_v$；
5. $\bar\partial_{\!AEG}=\tfrac12(X_u+iX_v)=-\lambda y\,\partial_{\bar w}$，
   所以 arithmetic holomorphic 场就是 $F(w)$；
6. $q^2=-\dfrac{4\mu^2w\bar w}{(w-\bar w)^2}$；
7. 曲率 $K=-\lambda^2$（全纯）。

**证明**。1--6 是直接计算，已由 witness A1--A6 检查。7 用共形曲率公式：
写成 $g=e^{2\rho}dw\,d\bar w$，其中
$$
e^{2\rho}=-\frac{4}{\lambda^2(w-\bar w)^2},
\qquad
\rho=\tfrac12\log e^{2\rho},
$$
则 $K=-4e^{-2\rho}\partial_w\partial_{\bar w}\rho=-\lambda^2$；
witness A8 检查。$\square$

**注 1.2（实切片）**。取 $w=X+iy$、$\bar w=X-iy$（$X,y\in\mathbb R$，
$y>0$），则
$$
g=\frac1{\lambda^2}\frac{dX^2+dy^2}{y^2},
\qquad
a=-\frac{\mu}{\lambda}\frac{X}{y},
\qquad
X_u=-\lambda y\partial_X,\quad X_v=-\lambda y\partial_y .
$$
这正是 Paper II 的基本模型（相差 $\mu$ 的归一化：Paper II 用
$X=(\lambda/\mu)x$）。witness A9--A10 检查。**注意**：$y>0$ 是开条件；
$\mathbb H^2$ 是复曲面 $M$ 的一个实子流形（实切片），而不是某个全局反全纯
对合在 $M$ 上的不动点集。这不影响公式的限制。**状态**：`PROVED`（显式计算）。

### 1.3 对角 $\operatorname{PGL}_2(\mathbb C)$ 不变性

**定理 1.2**。设 $M=\begin{pmatrix}a&b\\c&d\end{pmatrix}\in\operatorname{GL}_2(\mathbb C)$，
$M$ 在对角作用下
$$
w\longmapsto \frac{aw+b}{cw+d},\qquad
\bar w\longmapsto \frac{a\bar w+b}{c\bar w+d}.
$$
则 $g$ 不变；等价地，复化基本模型带有
$\operatorname{PGL}_2(\mathbb C)$ 的等距作用。实切片上的作用就是
$\operatorname{PSL}_2(\mathbb R)$ 在 $\mathbb H^2$ 上的标准作用。

**证明**。记 $\Delta=ad-bc\ne0$。则
$$
dw'=\frac{\Delta}{(cw+d)^2}dw,\qquad
d\bar w'=\frac{\Delta}{(c\bar w+d)^2}d\bar w,
$$
$$
w'-\bar w'
=\frac{\Delta(w-\bar w)}{(cw+d)(c\bar w+d)}.
$$
于是
$$
\frac{dw'\,d\bar w'}{(w'-\bar w')^2}
=\frac{dw\,d\bar w}{(w-\bar w)^2},
$$
故 $g'=g$。实切片上的作用就是把 $M\in\operatorname{PSL}_2(\mathbb R)$ 作用于
$w=X+iy$ 的标准 Möbius 作用；$g$ 的限制是双曲度量。$\square$

**状态**：`PROVED`（初等）+ witness A7。

**注 1.3**。这是"复化 $\mathbb H^2$"的精确含义：实模型有等距群
$\operatorname{PSL}_2(\mathbb R)$，复化模型有复化群
$\operatorname{PGL}_2(\mathbb C)$；$g$ 是复化的双曲度量，曲率仍是
$-\lambda^2$。它不是 $\mathbb H^3$：$\mathbb H^3$ 的等距群是
$\operatorname{PSL}_2(\mathbb C)$ 作为**实**群，度量为 Hermitian 正定；
这里的 $g$ 是复双线性，没有正定距离。

**注 1.4（赋值不不变）**。$a$ 在 $\operatorname{PGL}_2(\mathbb C)$ 下不是
不变的，也不是 $a$ 的线性分式函数：直接计算给出
$$
a'=-\frac{i\mu}{\lambda}\,
\frac{2ac\,w\bar w+(ad+bc)(w+\bar w)+2bd}
{\Delta(w-\bar w)},
$$
它同时依赖 $a$ 与 $w\bar w$（即 $q^2$）。所以 $a$ 是"赋值坐标"，不是等距
不变量；这与实模型中 $a=-(\mu/\lambda)X/y$ 在 $\operatorname{PSL}_2(\mathbb R)$
下按非线性方式变换是一致的。**状态**：`PROVED`（直接计算；不用于后续定理）。

### 1.4 $q=0$ 除子与迷向梯度

**命题 1.3**。在 $M$ 的补集（奇异延拓）上：

1. $q^2=0\iff w\bar w=0\iff w=0$ 或 $\bar w=0$；
2. 在 $w=0$（$\bar w\ne0$）处，$\partial_{\bar w}a=0$、$\partial_w a\ne0$，
   故 $\nabla a\ne0$ 但 $(\nabla a)^2=0$；
3. 在 $w=0$ 处框架 $X_u,X_v$ 与 $g$ 仍可延拓，但 $q$-正规化（单位梯度
   $E_a=\nabla a/q$）失效；
4. 零轨迹 $Z(a)=\{\operatorname{Re}w=0\}$ 是 $M$ 内的光滑复曲线，且
   $Z(a)\cap\{q=0\}=\varnothing$（在 $M$ 内 $q\ne0$）。

**证明**。1 由 $q^2=-4\mu^2w\bar w/(w-\bar w)^2$ 得到。2 由
$a=-(i\mu/\lambda)(w+\bar w)/(w-\bar w)$ 直接求导：在 $w=0$ 处
$$
\partial_w a=\frac{2i\mu}{\lambda\bar w}\ne0,\qquad
\partial_{\bar w}a=0 .
$$
3 是代入 $y=(w-\bar w)/(2i)$ 后 $X_u,X_v,g$ 的表达式在 $w=0$ 处有定义。
4 由 $\operatorname{Re}w=0$ 与 $w\bar w=y^2\ne0$（$y\ne0$）得到。$\square$

**状态**：`PROVED`（初等）。

**意义**。在 $M$ 内，C1 与实理论一样是"正则"的：$\nabla a\ne0$、零轨迹光滑。
新现象在 $M$ 的补集 $q=0$：梯度可以非零但迷向，水平集成为特征的。这正是
note 50 §4.3 的观察，也是接 Paper III 奇异延拓的入口。**不要把 $q=0$ 说成
零轨迹的奇点**：零轨迹在 $q=0$ 处仍可光滑，只是法向迷向。

---

## 2. 全纯场与复长度

### 2.1 arithmetic holomorphic 场

**命题 2.1**。在复化基本模型上：

1. $\bar\partial_{\!AEG}F=0\iff F=F(w)$ 全纯（在 $M$ 的每个连通片上）；
2. 对角 $\operatorname{PGL}_2(\mathbb C)$ 作用把 $F(w)$ 送到
   $F\bigl((aw+b)/(cw+d)\bigr)$，仍是全纯场；所以全纯场的类在等距作用下稳定；
3. 全纯场自动 $\Delta_g$-调和（命题 1.1(4) 与 note 50 定理 3.2 的代数因子
   分解，或直接 $\Delta_g=4\lambda^2y^2\partial_w\partial_{\bar w}$）。

**证明**。1 由 $\bar\partial_{\!AEG}=-\lambda y\partial_{\bar w}$ 与
$\lambda y\ne0$ 得到。2 是链式法则。3 是
$\Delta_g=4\lambda^2y^2\partial_w\partial_{\bar w}$ 与
$\partial_{\bar w}F=0$。$\square$

**状态**：`PROVED`。

### 2.2 复长度

**命题 2.2**。设 $M\in\operatorname{PGL}_2(\mathbb C)$，提升
$\widetilde M$ 的特征值为 $\lambda_1,\lambda_2$，令 $\kappa=\lambda_1/\lambda_2$。
则：

1. 非恒等 $M$ 在 $\mathbb P^1(\mathbb C)$ 上总有两个不动点（计重数）；
   只有分裂（$\kappa\ne1$）与抛物（$\kappa=1$）两类。
2. 复长度
   $$
   \ell=\log\kappa\pmod{2\pi i,\ \kappa\leftrightarrow\kappa^{-1}},
   \qquad
   \frac{\tau}{2}=\cosh\frac{\ell}{2},
   \qquad
   \ell=2\operatorname{arccosh}\frac{\tau}{2}.
   $$
3. $|\operatorname{Re}\ell|$（取 $\operatorname{Re}\ell\ge0$ 的分支）是 $M$
   作为 $\mathbb H^3$ 等距变换的平移长度，$\operatorname{Im}\ell$ 是旋转角。

**状态**：`STANDARD CONSEQUENCE`（标准双曲几何；见 note 50 §4.5 与 witness
D2--D3）。**警告**：$\ell$ 不是复化模型 $M$ 上的"距离"——$g$ 是复双线性，
没有正定距离；$\ell$ 是代数不变量/$\mathbb H^3$ 的复长度。**不要**把
复化 $\mathbb H^2$ 与 $\mathbb H^3$ 混为一谈。

### 2.3 三分塌缩

在 $\mathbb C$ 上，"非分裂"不存在（代数闭），只剩分裂/抛物。实三分是
$\operatorname{Gal}(\mathbb C/\mathbb R)$ 对不动点对的作用：两个实不动点 =
双曲/分裂，一个实重不动点 = 抛物，共轭对 = 相对实结构的椭圆。详见
note 50 §4.5；本篇不重复证明。

---

## 3. Riemann–Hilbert 边界理论

### 3.1 经典标量 RH 问题与指标

先陈述经典结果（外部标准；若进正式论文，需按 `STANDARD CONSEQUENCE` 另写
证明或引用）。

**经典 RH 问题（实轴版本）**。设 $G\in C^\mu(\mathbb R)$ 处处非零且
$G(\pm\infty)=1$，$g\in C^\mu(\mathbb R)$ 在无穷远处衰减。求 $F$ 在
$\mathbb C\setminus\mathbb R$ 全纯，边界值 $F_\pm\in C^\mu(\mathbb R)$，
$F(\infty)=0$，满足
$$
F_+(x)=G(x)F_-(x)+g(x),\qquad x\in\mathbb R .
$$
称
$$
\kappa=\frac{1}{2\pi}\bigl[\arg G\bigr]_{-\infty}^{\infty}\in\mathbb Z
$$
为**指标**（$G$ 沿实轴的绕数）。经典结论（定性）：若 $\kappa\ge0$，问题在
适当的增长条件下可解，解的自由度由 $\kappa$ 决定；若 $\kappa<0$，问题一般
无解，需 $-\kappa$ 个相容条件才有唯一解。（Muschelischwili、Gakhov、
Clancey--Gohberg 的标准理论；精确计数依规范化/增长条件而异，本篇只用
$G=-1$、$\kappa=0$ 的初等情形。）

**状态**：`STANDARD CONSEQUENCE`（外部标准；本篇只用 $G=-1$ 的初等情形）。

### 3.2 Dirichlet 问题是 $G=-1$ 的 RH 问题

**命题 3.1**。设 $f:\mathbb R\to\mathbb R$ 充分光滑。Dirichlet 问题
$$
\Delta U=0\ \text{在}\ \mathbb H^2,\qquad U|_{\mathbb R}=f
$$
等价于 RH 问题
$$
F_+(x)+F_-(x)=2f(x),\qquad x\in\mathbb R,
$$
其中 $F$ 在 $\mathbb H^2$ 全纯，$F_-(z)=\overline{F(\bar z)}$ 是它在
下半平面的反射。等价地
$$
F_+=(-1)F_-+2f,
$$
即 $G=-1$、$g=2f$；$G=-1$ 的指标为 $0$。

**证明**。若 $U=\operatorname{Re}F$，则 $F_-=\overline{F_+}$，故
$F_++F_-=2\operatorname{Re}F_+=2f$。反之，若 $F_++F_-=2f$，取
$U=\operatorname{Re}F$，则 $U$ 在 $\mathbb H^2$ 调和且边界值为 $f$。
$G=-1$ 的绕数为 $0$。$\square$

**状态**：`PROVED`（初等）。

### 3.3 Poisson 核、Schwarz 积分与 DtN

**命题 3.2**。在 $\mathbb H^2=\{w=X+iy:y>0\}$ 上：

1. Poisson 核是 Cauchy 核的跳跃：
   $$
   P_y(X-t)=\frac1\pi\frac{y}{(X-t)^2+y^2}
   =\frac{1}{2\pi i}\left(\frac1{t-w}-\frac1{t-\bar w}\right).
   $$
2. 对 $f\in C_0(\mathbb R)\cap L^1(\mathbb R)$（或 Schwartz），Schwarz 积分
   $$
   F(w)=\frac1{\pi i}\int_{\mathbb R}\frac{f(t)}{t-w}\,dt
   $$
   在 $\mathbb H^2$ 全纯，$\operatorname{Re}F$ 是 $f$ 的 Poisson 积分，
   $\operatorname{Im}F$ 是共轭调和函数，$F(\infty)=0$；若 $f$ 还是 Hölder
   连续（或 Schwartz），则 $F$ 连续到边界，边界值为 $f+iHf$（$H$ 为 Hilbert
   变换；符号依约定）。
3. Dirichlet-to-Neumann 映射是 Hilbert 变换与切向导数的复合：
   $$
   \mathcal N=|D_X|=H_XD_X=D_XH_X;
   $$
   在 $x$ 坐标中 $\mathcal N=|D_x|=(\lambda/\mu)|D_X|$。
4. 能量恒等式（相差常数因子）：
   $$
   \int_{\mathbb R}|k|\,|\hat f(k)|^2\,dk
   =\int_{\mathbb H^2}|\nabla U|^2\,dX\,dy,
   \qquad U=\operatorname{Re}F .
   $$

**证明**。1 是恒等式
$$
\frac1{t-w}-\frac1{t-\bar w}
=\frac{w-\bar w}{(t-w)(t-\bar w)}
=\frac{2iy}{(t-X)^2+y^2}.
$$
2 由 Cauchy 积分与 Plemelj 公式；$F(\infty)=0$ 由 $f\in L^1$ 与
$1/(t-w)\sim-1/w$。3 由 Cauchy--Riemann：$\partial_yU=-\partial_XV$，故
$-\partial_yU=\partial_XV=\partial_X(Hf)=HD_Xf=|D_X|f$；$H$ 与 $D$ 交换。
4 是 $U$ 的 Fourier 乘子 $(ik,-|k|)e^{-|k|y}$ 的 $L^2$ 积分。$\square$

**状态**：1 是初等（witness C1）；2--4 是标准复分析/调和分析，需写清函数类
与 $\infty$ 行为。**注意**：对一般 $f\in C_0$ 但不 $L^1$，Schwarz 积分在
$\infty$ 处不一定趋于 $0$；正式论文必须把类写成 $C_0\cap L^1$ 或 Schwartz，
或单独陈述 $\infty$ 条件。

### 3.4 $C_0\cap L^1$ 类的 C1 Dirichlet/Schwarz 定理

**定理 3.3**。对每个 $f\in C_0(\mathbb R)\cap L^1(\mathbb R)$，令 $F$ 为
命题 3.2(2) 的 Schwarz 积分，$U=\operatorname{Re}F$。则：

1. $F\in\mathcal O(\mathbb H^2)$；$U$ 是 $\Delta$-调和，连续到
   $\overline{\mathbb H^2}^{\,\mathrm{conf}}$，且 $U|_{\mathbb R}=f$、
   $U(\infty)=0$；
2. $U$ 是 $C^2(\mathbb H^2)\cap C(\overline{\mathbb H^2}^{\,\mathrm{conf}})$ 中
   唯一满足这些边界条件的有界调和函数；
3. $F$ 在"相差一个虚常数"的意义下唯一；
4. 若 $f$ 还是 Hölder 连续（或 Schwartz），则 $F$ 连续到边界，边界值为
   $f+iHf$；对 Schwartz 数据，DtN 与能量由命题 3.2(3)(4) 给出。

**证明**。1 的全纯性与 $U$ 的调和性是命题 3.2；$U$ 的连续性与边界值是经典
Poisson 定理（Paper II 的 `thm:C0-poisson-dirichlet` 的实部分）；$U(\infty)=0$
由 $f\in L^1$。2 是极大值原理：两个解之差是有界调和、边界值为 $0$，故为
$0$。3 是两个全纯解之差为全纯、实部为 $0$，故为纯虚常数。4 是 Plemelj 公式
（Hölder 数据）与命题 3.2(3)(4)。$\square$

**状态**：`STANDARD CONSEQUENCE REQUIRING AN IN-PAPER PROOF`（若进正式论文）。
它与 Paper II 的 `thm:C0-poisson-dirichlet` 是同一实定理的复分析读法；区别是
这里的函数类更窄（$C_0\cap L^1$，因为要控制全纯部分的 $\infty$ 行为），
且唯一性用极大值原理而非 RH 指标。

**与 Paper II 的关系**。Paper II 的定理对 $f\in C_0$（不要求 $L^1$）给出
实 Poisson 解；C1 的 Schwartz 版本需要 $L^1$ 来控制 $F(\infty)$。所以
**Paper II 的实定理更强，C1 的全纯定理更结构化**：它把解写成 Cauchy 积分，
把 DtN 写成 Hilbert 变换，把边界问题写成 $G=-1$ 的 RH 问题。

### 3.5 矩阵 RH 与内禀复边界（提案）

**矩阵 RH 问题**。设 $G:\mathbb R\to\operatorname{GL}_n(\mathbb C)$ 充分光滑、
$G(\pm\infty)=I$，求 $\mathbb C\setminus\mathbb R$ 上的全纯矩阵函数
$F_\pm$ 使 $F_+=GF_-$。解的存在性由 $G$ 的 Birkhoff 分解
$G=G_+G_-$（或等价的 Toeplitz 算子可逆性）控制；标量情形由指标 $\kappa$ 控制。

**AES 翻译（`STRUCTURAL PROPOSAL`）**。把 $G$ 读成"边界散射数据"：$f$ 是
赋值在边界上的值，$G$ 是赋值坐标变换的跳跃。标量指标 $\kappa$ 是"绕数
障碍"；矩阵情形是"分解障碍"。**没有证明**：AES 的边界数据是否总给出
Birkhoff 可分解的 $G$；这是 `OPEN`。

**内禀复边界（`OPEN`）**。C1 模型的"边界"是对角线
$$
D=\{w=\bar w\}\subset\mathbb P^1\times\mathbb P^1 .
$$
实理想边界 $\mathbb R$ 是 $D$ 的实轨迹。更内禀的 RH 问题应提在 $D$ 上：
求 $M$ 上的全纯场，使其跨越 $D$ 的跳跃满足给定的矩阵条件；Cauchy 核应是
复曲面上的 Cauchy--Fantappiè 核；指标应升级为 $D$ 上的除子类/线丛类
（$\operatorname{Pic}(D)$ 的元素），而不是一个整数。**这是提案，不是定理**；
本笔记不声称任何存在性/唯一性。

### 3.6 与 Paper II 的对照

| | Paper II（实） | C1（复） |
|---|---|---|
| 边界 | 理想边界 $y=0$ | 实切片 $\mathbb R\subset D$ |
| 方程 | $\Delta_gU=0$ | $\operatorname{Re}F$ 调和，$F$ 全纯 |
| 核 | Poisson 核 | Cauchy 核的跳跃 |
| 边界算子 | DtN $=\lvert D\rvert$ | Hilbert 变换 $H$，$\lvert D\rvert=HD$ |
| 唯一性 | 极大值原理 | 极大值原理 + 虚常数 |
| 函数类 | $C_0$ | $C_0\cap L^1$ 或 Schwartz |
| 一般化 | 无 | 矩阵 RH / 指标 / Birkhoff 分解 |

---

## 4. C2：Hermitian 伴随模型

### 4.1 定义

**定义 4.1（Hermitian AES）**。设 $M$ 是连通复曲线，
$g=e^{2\rho}|dz|^2$ 是 Hermitian 正定度量，$a\in\mathcal O(M)$，满足
$$
|\nabla a|_g^2=\mu^2+\lambda^2|a|^2,
\qquad \mu\in\mathbb R^\times,\ \lambda\in\mathbb R .
$$
在局部坐标中
$$
e^{-2\rho}|a'(z)|^2=\mu^2+\lambda^2|a(z)|^2,
$$
所以度量由 $a$ 反解：
$$
\rho(z)=\frac12\log\frac{|a'(z)|^2}{\mu^2+\lambda^2|a(z)|^2}
\qquad(a'(z)\ne0).
$$
**状态**：`DEFINITION/PROPOSAL`。这不是 Paper II 的 eikonal；它是 note 50 §5.2
的 Hermitian 化版本。

### 4.2 未 Hermitian 化 eikonal 的 no-go

**命题 4.1**（note 50 命题 5.1 的重述）。设 $M$ 连通复曲线，$g$ Hermitian
正定，$a:M\to\mathbb C$ 全纯，$\mu\ne0$、$\lambda\ne0$ 实。若
$$
|\nabla a|_g^2=\mu^2+\lambda^2a^2
$$
成立（左边实 $\ge0$），则 $a$ 是常数。

**证明**。左边实 $\ge0$，故 $\mu^2+\lambda^2a^2$ 实 $\ge0$；于是 $a^2$ 实值，
$a(M)\subset\mathbb R\cup i\mathbb R$；开映射定理迫使 $a$ 常数。$\square$

**状态**：`PROVED`（初等）。

### 4.3 全纯 $\Rightarrow$ 调和（C2 版本）

**命题 4.2**。设 $g=e^{2\rho}|dz|^2$ 是任意 Hermitian 度量，$F$ 全纯。
则 $\Delta_gF=0$，所以 $\operatorname{Re}F$、$\operatorname{Im}F$ 是实调和
函数。

**证明**。在局部坐标中
$$
\Delta_g=e^{-2\rho}\Delta_0,\qquad
\Delta_0=4\partial_z\partial_{\bar z}.
$$
$F$ 全纯故 $\partial_{\bar z}F=0$，于是 $\Delta_0F=0$，故
$\Delta_gF=0$。$\square$

**状态**：`PROVED`（初等）。**注**：这与 Paper II 的因子分解证明不同：C2 的
原因是二维共形不变性，而不是 $\bar\partial^*\bar\partial$ 的伴随分解。所以
C2 的"全纯 ⇒ 调和"对**任意** Hermitian 度量成立，不需要 AES eikonal；
eikonal 只用来把度量与 $a$ 绑定。

### 4.4 Hermitian 基本模型

**定理 4.3（Hermitian 基本模型）**。取
$$
M=\mathbb C,\qquad a(z)=z,\qquad
g=\frac{|dz|^2}{\mu^2+\lambda^2|z|^2},
\qquad \mu,\lambda>0 .
$$
则：

1. $(M,g,a;\mu,\lambda)$ 是 Hermitian 正则 AES：
   $$
   |\nabla a|^2=\mu^2+\lambda^2|a|^2;
   $$
2. 曲率
   $$
   K=\frac{2\lambda^2\mu^2}{\mu^2+\lambda^2|a|^2}>0;
   $$
3. 度量完备；
4. 总曲率 $\displaystyle\int_MK\,dA=2\pi$；
5. 零轨迹 $Z(a)=\{0\}$ 是单点；度量在 $0$ 处光滑（因子 $1/\mu^2$），
   所以零不是度量奇点，也不是 puncture；
6. 全纯场就是整函数，自动 $\Delta_g$-调和。

**证明**。1：$g=e^{2\rho}|dz|^2$，
$e^{2\rho}=1/(\mu^2+\lambda^2r^2)$，故
$|\nabla a|^2=e^{-2\rho}|a'|^2=\mu^2+\lambda^2r^2=\mu^2+\lambda^2|a|^2$。
2：$\rho=-\tfrac12\log(\mu^2+\lambda^2r^2)$，
$K=-e^{-2\rho}\Delta_0\rho$；直接计算
$\Delta_0\rho=-2\lambda^2\mu^2/(\mu^2+\lambda^2r^2)^2$，故
$K=2\lambda^2\mu^2/(\mu^2+\lambda^2r^2)$。3：从 $0$ 到 $R$ 的长度为
$$
\int_0^R e^{\rho}\,dr
=\int_0^R\frac{dr}{\sqrt{\mu^2+\lambda^2r^2}}
=\frac1{\lambda}\operatorname{arcsinh}\frac{\lambda R}{\mu}
\longrightarrow\infty,
$$
且在 $0$ 处被积函数为 $1/\mu>0$；故完备。4：
$$
\int_MK\,dA
=\int_0^\infty K\,e^{2\rho}\,2\pi r\,dr
=\int_0^\infty
\frac{2\lambda^2\mu^2}{(\mu^2+\lambda^2r^2)^2}\,2\pi r\,dr
=2\pi .
$$
5：$a(z)=z$ 的零点是 $0$；$e^{2\rho}(0)=1/\mu^2$。6：命题 4.2。$\square$

**状态**：`PROVED`（显式计算）+ `COMPUTATIONALLY VERIFIED EXAMPLE`
（witness B1--B7）。

**读法**。这是 C2 的"基本模型"，但它与实基本模型**不同**：

- 实模型：$K=-\lambda^2<0$，零轨迹是测地线，完备，函数论是 Poisson/Dirichlet；
- C2 模型：$K>0$，零轨迹是点，完备，函数论是整函数/正定椭圆 Dirichlet；
- C1 模型：$K=-\lambda^2$（全纯），零轨迹是复曲线，无正定距离，函数论是
  Riemann–Hilbert/Schwarz。

C2 模型的曲率在 $0$ 处为 $2\lambda^2$，在 $\infty$ 处趋于 $0$；总曲率 $2\pi$
是 Cohn--Vossen 不等式对平面型完备曲面的极值（标准事实；本笔记只做计算，
不把"极值"作为定理）。

### 4.5 C2 的边界理论

C2 的度量正定，所以 $\Delta_g$ 在带光滑边界的区域上是**一致椭圆**的：
经典 Dirichlet 问题在 $C^{2,\alpha}(\overline\Omega)$ 中适定（标准 PDE）。
这与 C1 的 RH 问题形成对照：

| | C1 | C2 |
|---|---|---|
| 方程 | 全纯/CR，非椭圆 | 实椭圆 |
| 边界问题 | Riemann–Hilbert | Dirichlet/Poisson |
| 边界算子 | Hilbert 变换 | 正定椭圆的 DtN |
| 数据类 | 全纯跳跃 | 实 Sobolev/Hölder |
| 指标障碍 | 有 | 无（Lax–Milgram） |

**开放问题**。在完备的 Hermitian 基本模型上，"边界"是点 $\infty$；有界
调和函数是否必为常数（Liouville/parabolicity）？DtN 的显式核是什么？本文
不声称。**状态**：`OPEN`。

### 4.6 C2 的零轨迹与 puncture

**命题 4.4**。设 $M$ 连通复曲线，$a$ 是非恒定全纯函数。则 $Z(a)$ 是离散
闭集；在 $Z(a)$ 的每个点 $p$，若 $a$ 的零点阶为 $m$，则局部
$a(z)=z^m u(z)$（$u$ 非零），度量的共形因子为
$$
e^{2\rho}
=\frac{|a'(z)|^2}{\mu^2+\lambda^2|a(z)|^2}
=\frac{|mz^{m-1}u+O(z^m)|^2}{\mu^2+\lambda^2|z|^{2m}|u|^2}
\sim \frac{m^2|u(0)|^2}{\mu^2}|z|^{2m-2}.
$$
所以：

1. $m=1$：$e^{2\rho}(0)=|u(0)|^2/\mu^2>0$，度光滑；零点不是奇点；
2. $m\ge2$：$e^{2\rho}\sim C|z|^{2m-2}\to0$，度在 $0$ 处退化；到 $0$ 的距离
   $\int_0|z|^{m-1}d|z|$ 有限，故通常不完备（锥形端）；
3. 因而 C2 的"puncture"不是零点的自动后果，而是 $m\ge2$ 或额外边界
   选择的结果。

**状态**：`PROVED`（初等展开）+ `STRUCTURAL PROPOSAL`（"puncture"的术语）。
这与 C1/实理论的对比很重要：C1 的 $q=0$ 是除子，实理论的零轨迹是曲线；
C2 的零点通常是光滑点，只有在高阶零点或额外边界条件下才成为 puncture。

---

## 5. 三种基本模型的对照

| | 实基本模型 $\mathfrak E_0$ | C1 复化基本模型 | C2 Hermitian 基本模型 |
|---|---|---|---|
| 载体 | $\mathbb H^2$ | $\mathbb C^2$：$w\ne\bar w,\ w\bar w\ne0$ | $\mathbb C$ |
| 度量 | $\lambda^{-2}(dX^2+dy^2)/y^2$ | $-(4/\lambda^2)dw\,d\bar w/(w-\bar w)^2$ | $\lvert dz\rvert^2/(\mu^2+\lambda^2\lvert z\rvert^2)$ |
| 赋值 | $-(\mu/\lambda)X/y$ | $-(i\mu/\lambda)(w+\bar w)/(w-\bar w)$ | $z$ |
| eikonal | $\lvert\nabla a\rvert^2=\mu^2+\lambda^2a^2$ | $(\nabla a)^2=\mu^2+\lambda^2a^2$ | $\lvert\nabla a\rvert^2=\mu^2+\lambda^2\lvert a\rvert^2$ |
| 曲率 | $-\lambda^2$ | $-\lambda^2$（全纯） | $2\lambda^2\mu^2/(\mu^2+\lambda^2\lvert a\rvert^2)>0$ |
| 零轨迹 | 测地线 | 复曲线 | 单点 |
| 完备性 | 完备 | 无正定距离 | 完备 |
| 总曲率 | $-\infty$ | — | $2\pi$ |
| 函数论 | Poisson/Dirichlet | Riemann–Hilbert/Schwarz | 整函数/正定椭圆 Dirichlet |
| 等距群 | $\operatorname{PSL}_2(\mathbb R)$ | $\operatorname{PGL}_2(\mathbb C)$（对角） | 未定（$\mathrm{Isom}(g)$） |

**一句话**：三个模型是同一个代数骨架的三种不同实现（实、复化、Hermitian）；
**曲率符号、零轨迹类型、边界问题类型**三者一起翻转。

---

## 6. 与 note 50、Paper II、Paper III 的接口

- **note 50**：本篇实现 WP1（C1 模型）与 WP4（RH 边界），并推进 WP5（C2）。
  note 50 的 Layer A/B/C 与 C1/C2 区分在这里得到具体模型。
- **Paper II**：C1 的定理 3.3 是 Paper II `thm:C0-poisson-dirichlet` 的复分析
  读法，函数类更窄；C2 的定理 4.3 是新的 Hermitian 模型，不是 Paper II 的模型。
- **Paper III**：C1 的 $q=0$ 除子与奇异延拓是 Paper III 的复化入口；C2 的高阶
  零点（命题 4.4(2)）是另一种奇异入口。两者都不是 Paper II 的 puncture。
- **pcrg-paper**：C1/C2 的区分对应 `bivaluation-02` 的代数复化/Hermitian 版本；
  本篇不重述字典，只把模型具体化。

---

## 7. 开放问题

1. **内禀 RH**：对角线 $D=\{w=\bar w\}$ 上的 RH 问题、Cauchy--Fantappiè 核、
   指标升级为 $\operatorname{Pic}(D)$ 的除子类。`OPEN`。
2. **矩阵 RH 的 AES 可实现性**：哪些边界跳矩阵来自 AES 的赋值/坐标变换？
   Birkhoff 分解是否总存在？`OPEN`。
3. **C2 完备模型的 Dirichlet/Liouville**：有界调和函数是否常数？DtN 显式核？
   `OPEN`。
4. **完备 Hermitian AES 的分类**：除 $a(z)=z$ 外还有哪些完备模型？曲率
   符号/总曲率的限制？`OPEN`。
5. **C2 的谱理论**：$-\Delta_g$ 在完备模型上的谱、Friedrichs 实现、热核。
   `OPEN`。
6. **C1 复长度与 C2 度量的关系**：$\ell$ 是 $\mathbb H^3$ 的复长度，不是
   C1/C2 的距离；是否存在一个把 $\ell$ 读成 C2 度量的"谱"或"平移"的公式？
   `OPEN`。
7. **p-adic/树方向**：note 50 §6.5 的提案；本篇未展开。`OPEN`。

---

## 附录 A：witness 输出

运行
```
python3 51-complexified-model-and-rh-witness.py
```
全部通过。摘录：

```
A. C1 complexified basic model
  PASS  A1  (grad a)^2 = mu^2 + lambda^2 a^2
  PASS  A2  Delta_g a = 2 lambda^2 a
  PASS  A4  [X_u,X_v] = lambda X_u
  PASS  A5  Delta_g = X_u^2 + X_v^2 + lambda X_v
  PASS  A6  q^2 = -4 mu^2 w wbar/(w-wbar)^2
  PASS  A7  diagonal PGL_2(C) action preserves g
  PASS  A8  curvature K = -lambda^2
B. C2 Hermitian basic model
  PASS  B1  Hermitian eikonal e^{-2rho} = mu^2 + lambda^2 r^2
  PASS  B2  K = 2 lambda^2 mu^2/(mu^2+lambda^2 r^2)
  PASS  B3  length 0->R = asinh(lambda R/mu)/lambda
  PASS  B4  length -> oo as R -> oo (completeness)
  PASS  B6  total curvature = 2 pi
C. Riemann--Hilbert identities
  PASS  C1  Poisson kernel = Cauchy jump
  PASS  C2  H D has symbol |k|
  PASS  C3  index of G=e^{i k theta} is k
```

## 附录 B：与 Paper II 标签的对应

| 本篇 | Paper II 标签 |
|---|---|
| §1.2 基本模型 | `prop:hyperbolic-analytic-normalization` |
| §3.2 Dirichlet = RH | `thm:C0-poisson-dirichlet`（复分析读法） |
| §3.3 Poisson 核 | `lem:poisson-kernel-transport` |
| §3.3 DtN/能量 | §7 的 DtN 与能量结果 |
| §4.2 C2 调和性 | 无直接对应（C2 新定义） |
| §4.4 C2 基本模型 | 无直接对应（C2 新模型） |
