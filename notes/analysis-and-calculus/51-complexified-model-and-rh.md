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

**配套脚本**：`51-complexified-model-and-rh-witness.py`（本目录；检查数与覆盖边界见附录 A）。

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
   是实模型的复化；$g$ 在共同定义域内满足对角 Möbius 拉回不变性，并在全局环境 $N$ 上有群作用；
   实切片 $w=X+iy$（$y>0$）逐字回到 Paper II 的基本模型。
   $q^2=0$ 的除子是 $w\bar w=0$，在 $w=0$ 处 $\nabla a\ne0$ 但迷向——这是实理论
   不可能出现的新现象，出现在 $N_{\mathrm{aff}}$ 的延拓中；此处 $g$ 仍正则非退化，
   失效的是 $1/q$ 正规化。

2. **C1 实切片的 Dirichlet 问题有 Riemann–Hilbert 读法**。
   Poisson 核是 Cauchy 核的跳跃；带反射约束的 Dirichlet 问题可写成跳系数 $G=-1$ 的
   Riemann–Hilbert 问题；Schwarz 积分给出全纯解；DtN 是 Hilbert 变换
   $|D|=HD$；能量仍是 $H^{1/2}$。在实值 $C_0\cap L^1$ 类上给出 Dirichlet/Schwarz 定理，
   但全纯函数的无穷远极限只在非切向趋近下断言。矩阵跳与"内禀复边界"（对角线
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
   真正的函数论，在适当区域上的 Dirichlet 问题属正定椭圆理论，也可作复分析读法。

**三种基本模型的对照**（详见 §5）：

| | 实基本模型 | C1 复化 | C2 Hermitian |
|---|---|---|---|
| 曲率 | $-\lambda^2<0$ | $-\lambda^2$（全纯） | $>0$，趋向 $0$ |
| 零轨迹 | 测地线 $X=0$ | 复曲线 $w+\bar w=0$ | 单点 $\{0\}$ |
| 完备性 | 完备 | 无正定距离 | 完备 |
| 边界理论 | Poisson/Dirichlet | Riemann–Hilbert/Schwarz | Dirichlet/Poisson |
| 总曲率 | $-\infty$（无限面积） | — | $2\pi$ |

---

## 1. C1：复化基本模型

### 1.1 定义

**定义 1.1（复化基本模型）**。固定 $\mu\in\mathbb C^\times$、$\lambda\in\mathbb C^\times$
（本篇只处理 $\lambda\ne0$；$\lambda=0$ 时本坐标公式未定义，平坦极限需另选参数坐标）。
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
$q^2$ 是 $M$ 上处处非零的全纯函数，但不预设全局平方根。若
$U\subset M$ 是单连通开集，可取 $s^2=w\bar w$ 的全纯分支，并令
$q=2i\mu s/(w-\bar w)$。或者在非分歧双覆盖
$$
\widetilde M=\{(w,\bar w,s):(w,\bar w)\in M,\ s^2=w\bar w\}
\longrightarrow M
$$
上取此全局 $q$。覆盖变换 $s\mapsto-s$ 也改变 $q$ 的符号；含 $q$ 的
正规化框架只能在所选分支或覆盖上使用。$g,a,q^2,X_u,X_v$ 本身均在 $M$ 上定义。

这里用的框架旋转是复线性张量 $J\partial_X=\partial_y$、
$J\partial_y=-\partial_X$，即 $J\partial_w=i\partial_w$、
$J\partial_{\bar w}=-i\partial_{\bar w}$。它是实二维旋转的复化，**不是**
复曲面底层实四维流形的标准复结构。称局部数据
$(U,g,a;\mu,\lambda;q,J)$（或双覆盖上的相应数据）为带 $q$ 的复化基本模型。

**注 1.1（分支障碍，`PROVED`）**。在闭路
$w=\varepsilon e^{it}$、$\bar w=2$（$0<\varepsilon<2$，$0\le t\le2\pi$）上，
$w\bar w$ 绕 $0$ 一圈，而 $(w-\bar w)^2$ 绕数为 $0$，所以 $q^2$ 的绕数为 $1$。
若存在全局非零全纯 $q$，其平方沿任何闭路的绕数应为偶数，矛盾。
$M$ 排除 $w=\bar w$ 与 $w\bar w=0$；后者是 $q^2$ 的零除子，
也是 $1/q$ 正规化的障碍。在 $M$ 上 $(\nabla a)^2=q^2\ne0$，故 $a$ 是浸没。

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
   所以对全纯函数 $F\in\mathcal O(M)$，arithmetic holomorphic 条件局部等价于只依赖 $w$；
6. $q^2=-\dfrac{4\mu^2w\bar w}{(w-\bar w)^2}$；
7. 曲率 $K=-\lambda^2$（全纯）。

**证明**。写 $y=(w-\bar w)/(2i)$、$X=(w+\bar w)/2$，则
$g=(dX^2+dy^2)/(\lambda^2y^2)$、$a=-\mu X/(\lambda y)$。
因此 $a_X=-\mu/(\lambda y)$、$a_y=\mu X/(\lambda y^2)$，
$g^{-1}(da,da)=\mu^2(1+X^2/y^2)=\mu^2+\lambda^2a^2$。
二维共形 Laplace 算子是 $\lambda^2y^2(\partial_X^2+\partial_y^2)$，
代入 $a$ 得第 2 项。框架为 $X_u=-\lambda y\partial_X$、
$X_v=-\lambda y\partial_y$，求导直接给出第 3--5 项；
$X^2+y^2=w\bar w$ 给出第 6 项。这些是解析恒等式，不依赖计算脚本作为证明。
7 用局部对数的共形曲率公式：
写成 $g=e^{2\rho}dw\,d\bar w$，其中
$$
e^{2\rho}=-\frac{4}{\lambda^2(w-\bar w)^2},
\qquad
\rho=\tfrac12\log e^{2\rho},
$$
则 $K=-4e^{-2\rho}\partial_w\partial_{\bar w}\rho=-\lambda^2$；
witness A8 检查。$\square$

**注 1.2（实切片）**。$\mu,\lambda$ 此处取实非零。取 $w=X+iy$、$\bar w=X-iy$（$X,y\in\mathbb R$，
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
$\mathbb H^2$ 是复曲面 $M$ 的一个实子流形（实切片），它是反全纯对合 $(w,\bar w)\mapsto(\overline{\bar w},\overline w)$
的不动点集的上半平面连通分支，而非整个不动点集。**状态**：`PROVED`（显式计算）。

### 1.3 对角 $\operatorname{PGL}_2(\mathbb C)$ 不变性

**定理 1.2（共同定义域与全局环境，`PROVED WITH STATED HYPOTHESES`）**。
令
$$
N=(\mathbb P^1\times\mathbb P^1)\setminus D,\qquad D=\{w=\bar w\},
\qquad M\subset N.
$$
$g$ 唯一延拓为 $N$ 上非退化全纯双线性度量，对角
$\operatorname{PGL}_2(\mathbb C)$ 在 $N$ 上有全局等距作用。
对于 $T(z)=(Az+B)/(Cz+D_0)$，在 $M$ 上只断言局部拉回等式
$T^*g=g$，定义域是
$$
U_T=M\cap T^{-1}(M)
=\{(w,\bar w)\in M:(Cw+D_0)(C\bar w+D_0)(Aw+B)(A\bar w+B)\ne0\}.
$$
这里 $T:U_T\to U_{T^{-1}}$ 是双全纯映射；不能称之为整个 $M$ 的群作用。

**证明**。记 $\Delta=AD_0-BC\ne0$，在仿射共同定义域上
$$
dT(w)=\frac{\Delta\,dw}{(Cw+D_0)^2},\qquad
T(w)-T(\bar w)=\frac{\Delta(w-\bar w)}{(Cw+D_0)(C\bar w+D_0)},
$$
故 $dT(w)dT(\bar w)/(T(w)-T(\bar w))^2=dw\,d\bar w/(w-\bar w)^2$。
在 $w=\infty$ 的图中取 $u=1/w$，保持 $v=\bar w$，则
$$
g=\frac4{\lambda^2}\frac{du\,dv}{(1-uv)^2}.
$$
它在 $u=0$ 正则且非退化；交换两因子处理另一无穷远图。
两坐标同时为无穷远的点在 $D$ 中，已经排除。公式在重叠上相容，
所以给出 $N$ 上全局度量。Möbius 变换保持两点相异，因此在 $N$ 上是全局作用，
拉回恒等式由仿射稠密开集延拓到 $N$。
反例：平移 $T(z)=z-1$ 将 $(1,2)\in M$ 送到 $(0,1)\notin M$；
$T(z)=1/(z-1)$ 则把其第一坐标送到无穷远。$\square$

实参数下，实矩阵的正行列式射影类（即 $\operatorname{PSL}_2(\mathbb R)$）
保持上半平面实切片；一般复矩阵并不保持此切片。

**注 1.3**。这里“复化 $\mathbb H^2$”指度量公式及 $N$ 上的复群作用，
不是带指定 $a,q$ 的 $M$ 上全局群作用。它不是 $\mathbb H^3$：后者是实三维
Riemannian 流形，不是 Hermitian 复流形；其保定向等距群为
$\operatorname{PSL}_2(\mathbb C)$。本篇 $g$ 是复双线性，不定义正定距离。

**注 1.4（赋值不不变）**。$a$ 在 $\operatorname{PGL}_2(\mathbb C)$ 下不是
不变的，一般也不是仅依赖原赋值 $a$ 的线性分式函数。沿用定理 1.2 的
$T(z)=(Az+B)/(Cz+D_0)$ 与 $\Delta=AD_0-BC$，在共同定义域上直接计算给出
$$
a'=-\frac{i\mu}{\lambda}\,
\frac{2AC\,w\bar w+(AD_0+BC)(w+\bar w)+2BD_0}
{\Delta(w-\bar w)},
$$
一般不能只由原赋值 $a$ 决定（$q^2$ 本身也是 $a$ 的函数，不能作额外坐标）。
例如 $(w,\bar w)=(1,2),(2,4)$ 有相同的 $a$，但同时平移 $+1$ 后
$(w+\bar w)/(w-\bar w)$ 分别为 $-5,-4$。所以 $a$ 不是等距不变量；这与实模型中 $a=-(\mu/\lambda)X/y$ 在 $\operatorname{PSL}_2(\mathbb R)$
下按非线性方式变换是一致的。**状态**：`PROVED`（直接计算；不用于后续定理）。

### 1.4 $q=0$ 除子与迷向梯度

**命题 1.3**。在仿射延拓 $N_{\mathrm{aff}}=\{w\ne\bar w\}\subset N$ 上（不包括对角线）：

1. $q^2=0\iff w\bar w=0\iff w=0$ 或 $\bar w=0$；
2. 在 $w=0$（$\bar w\ne0$）处，$\partial_{\bar w}a=0$、$\partial_w a\ne0$，
   故 $\nabla a\ne0$ 但 $(\nabla a)^2=0$；
3. 在 $w=0$ 处框架 $X_u,X_v$ 与 $g$ 仍可延拓，但 $q$-正规化（单位梯度
   $E_a=\nabla a/q$）失效；
4. 零轨迹 $Z(a)=\{w+\bar w=0\}$ 是 $M$ 内的光滑复曲线，且
   $Z(a)\cap\{q=0\}=\varnothing$（在 $M$ 内 $q\ne0$）。

**证明**。1 由 $q^2=-4\mu^2w\bar w/(w-\bar w)^2$ 得到。2 由
$a=-(i\mu/\lambda)(w+\bar w)/(w-\bar w)$ 直接求导：在 $w=0$ 处
$$
\partial_w a=\frac{2i\mu}{\lambda\bar w}\ne0,\qquad
\partial_{\bar w}a=0 .
$$
3 是代入 $y=(w-\bar w)/(2i)$ 后 $X_u,X_v,g$ 的表达式在 $w=0$ 处有定义。
4 由 $w+\bar w=0$ 与 $w\bar w=y^2\ne0$（$y\ne0$）得到；
$\operatorname{Re}w=0$ 只能用在实切片，不能描述复曲面的全纯除子。$\square$

**状态**：`PROVED`（初等）。

**意义**。在 $M$ 内，C1 与实理论一样是"正则"的：$\nabla a\ne0$、零轨迹光滑。
新现象在 $M$ 的补集 $q=0$：梯度可以非零但迷向，水平集成为特征的。这正是
note 50 §4.3 的观察，也是接 Paper III 奇异延拓的入口。**不要把 $q=0$ 说成零轨迹的奇点**：本模型的 $a=0$ 与 $q^2=0$ 根本不相交。
$w=0$ 上是非零赋值 $a=i\mu/\lambda$ 的光滑特征水平集。

---

## 2. 全纯场与复长度

### 2.1 arithmetic holomorphic 场

**命题 2.1**。在复化基本模型上：

1. 预先要求 $F\in\mathcal O(M)$。则 $\bar\partial_{\!AEG}F=0$ 当且仅当
   $F=f\circ\pi_1$，其中 $f\in\mathcal O(\mathbb C^*)$、$\pi_1(w,\bar w)=w$。
   在一般开子域或 $q$ 双覆盖上仅断言局部表示，除非另证纤维连通与下降；
2. 对角 $\operatorname{PGL}_2(\mathbb C)$ 作用把 $F(w)$ 送到
   $F\bigl((Aw+B)/(Cw+D_0)\bigr)$，在 $U_T$ 上仍是满足该方程的全纯场；这是局部层的稳定性，而非 $\mathcal O(M)$ 的全局作用；
3. 全纯场自动 $\Delta_g$-调和（命题 1.1(4) 与 note 50 定理 3.2 的代数因子
   分解，或直接 $\Delta_g=4\lambda^2y^2\partial_w\partial_{\bar w}$）。

**证明**。1 局部由 $\bar\partial_{\!AEG}=-\lambda y\partial_{\bar w}$ 得到；
对固定 $w\ne0$，纤维 $\mathbb C\setminus\{0,w\}$ 连通，故 $F$ 沿纤维常值。
局部全纯截面保证下降的 $f$ 全纯。若不先要求 $F\in\mathcal O(M)$，
此一个复方向方程不能推出底层实四维上的全纯性。2 是链式法则。3 是
$\Delta_g=4\lambda^2y^2\partial_w\partial_{\bar w}$ 与
$\partial_{\bar w}F=0$。$\square$

**状态**：`PROVED`。

### 2.2 复长度

**命题 2.2**。设 $M\in\operatorname{PGL}_2(\mathbb C)$，提升
$\widetilde M$ 的特征值为 $\lambda_1,\lambda_2$，令 $\kappa=\lambda_1/\lambda_2$。
则：

1. 非恒等 $M$ 在 $\mathbb P^1(\mathbb C)$ 上总有两个不动点（计重数）；
   按特征值是否相异分为分裂（$\kappa\ne1$）与抛物（$\kappa=1$）两种类型，
   不是说只有两个共轭类；分裂元仍有特征值比参数。
2. 复长度
   $$
   \ell=\log\kappa\pmod{2\pi i,\ \kappa\leftrightarrow\kappa^{-1}},
   \qquad
   \tau^2=4\cosh^2\frac{\ell}{2},\qquad
   \tau=\operatorname{tr}\widehat M,\quad \widehat M\in\operatorname{SL}_2(\mathbb C).
   $$
   $\widehat M$ 的两个选择相差负号，所以只有 $\tau^2$ 是射影不变量；
   $\tau/2=\cosh(\ell/2)$ 须同时选相容的提升与对数分支。
3. 对分裂元，$|\operatorname{Re}\ell|$（取 $\operatorname{Re}\ell\ge0$ 的分支）是 $M$
   作为 $\mathbb H^3$ 等距变换的平移长度，$\operatorname{Im}\ell$ 是旋转角。

**状态**：`STANDARD CONSEQUENCE`（标准双曲几何；见 note 50 §4.5；本脚本无对应数值见证）。**警告**：$\ell$ 不是复化模型 $M$ 上的"距离"——$g$ 是复双线性，
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

一般标量 RH 问题形如 $F_+=GF_-+g$。指标是沿指定闭轮廓的
$\operatorname{wind}(G,0)$，但存在性、唯一性与核维数还依赖函数空间、
无穷远规范化及正负侧的约定。本笔记不援引未说明这些条件的指标计数定理。
若在一点紧化实轴上取常系数 $G=-1$，其指标为 $0$；这不满足
某些教材采用的 $G(\infty)=1$ 规范化，不能直接混用该规范化下的定理。
下文只用带反射约束的初等关系。一般指标理论在此是 `STRUCTURAL PROPOSAL`。

### 3.2 Dirichlet 问题是 $G=-1$ 的 RH 问题

**命题 3.1**。设 $f:\mathbb R\to\mathbb R$，并只考虑自身及其全局调和共轭都在每个有限边界点连续的实调和解 $U$。
在这个受限解类中，Dirichlet 问题
$$
\Delta U=0\ \text{在}\ \mathbb H^2,\qquad U|_{\mathbb R}=f
$$
等价于 RH 问题
$$
F_+(x)+F_-(x)=2f(x),\qquad x\in\mathbb R,
$$
其中 $F$ 在 $\mathbb H^2$ 全纯，$\operatorname{Re}F=U$，$F_-(z)=\overline{F(\bar z)}$ 是它在
下半平面的反射。等价地
$$
F_+=(-1)F_-+2f,
$$
即 $G=-1$、$g=2f$；$G=-1$ 的指标为 $0$。

**证明**。上半平面单连通，故每个实调和 $U$ 有全局调和共轭，唯一到常数。
若 $U=\operatorname{Re}F$，则 $F_-=\overline{F_+}$，故
$F_++F_-=2\operatorname{Re}F_+=2f$。反之，若 $F_++F_-=2f$，取
$U=\operatorname{Re}F$，则 $U$ 在 $\mathbb H^2$ 调和且边界值为 $f$。
$G=-1$ 的绕数为 $0$。$\square$

**状态**：`PROVED WITH STATED HYPOTHESES`。反射约束不可省：
$F_+=ic,F_-= -ic$（$c$ 为任意复常数）总满足零跳和，但若 $c$ 非实则不满足
反射关系，$\operatorname{Re}F_+$ 也不必有零边界值。唯一性另需 §3.4 的解类。

### 3.3 Poisson 核、Schwarz 积分与 DtN

**命题 3.2**。在 $\mathbb H^2=\{w=X+iy:y>0\}$ 上：

1. Poisson 核是 Cauchy 核的跳跃：
   $$
   P_y(X-t)=\frac1\pi\frac{y}{(X-t)^2+y^2}
   =\frac{1}{2\pi i}\left(\frac1{t-w}-\frac1{t-\bar w}\right).
   $$
2. 对实值 $f\in C_0(\mathbb R)\cap L^1(\mathbb R)$（或实 Schwartz），Schwarz 积分
   $$
   F(w)=\frac1{\pi i}\int_{\mathbb R}\frac{f(t)}{t-w}\,dt
   $$
   在 $\mathbb H^2$ 全纯，$\operatorname{Re}F$ 是 $f$ 的 Poisson 积分，
   $\operatorname{Im}F$ 是共轭调和函数；仅当非切向趋于无穷远时保证 $F\to0$。
   若 $f$ 还是局部 $C^{0,\alpha}$（$0<\alpha<1$）Hölder
   连续（或 Schwartz），则 $F$ 连续到每个有限边界点，边界值为 $f+iHf$，
   $Hf(X)=\pi^{-1}\operatorname{pv}\int f(t)/(X-t)\,dt$。
3. 对实 Schwartz 数据，取 $D_X=\partial_X$，共形紧化的欧氏外法向
   DtN（不是未正规化的双曲单位法向）是 Hilbert 变换与切向导数的复合：
   $$
   \mathcal N=|D_X|=H_XD_X=D_XH_X;
   $$
   在实参数与 $X=(\lambda/\mu)x$ 的坐标传输下
   $|D_x|=|\lambda/\mu|\,|D_X|$；正参数时才可去绝对值。
4. 对实 Schwartz 数据，用单位化 Fourier 变换
   $\hat f(k)=(2\pi)^{-1/2}\int e^{-ikX}f(X)\,dX$，有精确恒等式：
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
2 在紧子集上可在积分号下求导，因为 $|t-w|\ge\operatorname{Im}w>0$。
取实部得 Poisson 积分；在 $\operatorname{Im}w\ge\varepsilon|w|$ 的区域，
$|F(w)|\le\|f\|_1/(\pi\operatorname{Im}w)\to0$。
有限边界点的 Hölder 假设使减去 $f(X)$ 后的奇异积分局部可积，给出 Plemelj 边界值。
不能把 $1/(t-w)\sim-1/w$ 在整个积分范围与任意趋近方向上一致使用。3 由 Cauchy--Riemann：$\partial_yU=-\partial_XV$，故
$-\partial_yU=\partial_XV=\partial_X(Hf)=HD_Xf=|D_X|f$；$H$ 与 $D$ 交换。
4 是 $U$ 的 Fourier 乘子 $(ik,-|k|)e^{-|k|y}$ 的 $L^2$ 积分。$\square$

**状态**：`PROVED WITH STATED HYPOTHESES`（有限边界 Plemelj 公式为标准结果）。
能量对应齐次 $\dot H^{1/2}$ 半范数；本处数据另有 $L^2$，故可归入非齐次 $H^{1/2}$。
不声称所有 $C_0\cap L^1$ 数据都有有限能量或连续的共轭边界值。

**反例（$C_0\cap L^1$ 不保证全纯边界连续，`PROVED`）**。
取非负连续紧支撑 $f$，在 $0<t<e^{-2}$ 时令
$f(t)=1/\log(1/t)$，在 $t\le0$ 时令 $f(t)=0$，并在右端连续截断。
则 $f(0)=0$，但
$$
\operatorname{Im}F(iy)=-\frac1\pi\int_0^\infty
\frac{t f(t)}{t^2+y^2}\,dt\longrightarrow-\infty\quad(y\downarrow0),
$$
因为单调收敛后的积分含 $\int_0^{e^{-2}}dt/[t\log(1/t)]=\infty$。
所以实部的连续性不能转移给 $F$。还可选上述 $f$ 支撑在 $[0,1/2]$，令
$h(t)=\sum_{n\ge1}2^{-n}f(t-n)$。不交支撑保证 $h\in C_0\cap L^1$。
在每个 $n$ 附近，除第 $n$ 项外其余 Cauchy 积分一致有界（距离至少 $1/2$）；
第 $n$ 项的虚部随 $y\downarrow0$ 趋于 $-\infty$。因此可选 $0<y_n<1/n$，
使 $\operatorname{Im}F_h(n+iy_n)<-n$。这给出 $|w_n|\to\infty$ 却
$F_h(w_n)\not\to0$ 的明确构造，否定原来的无条件 $F(\infty)=0$ 声明。

### 3.4 $C_0\cap L^1$ 类的 C1 Dirichlet/Schwarz 定理

**定理 3.3**。对每个实值 $f\in C_0(\mathbb R)\cap L^1(\mathbb R)$，令 $F$ 为
命题 3.2(2) 的 Schwarz 积分，$U=\operatorname{Re}F$。则：

1. $F\in\mathcal O(\mathbb H^2)$；$U$ 是 $\Delta$-调和，连续到
   $\overline{\mathbb H^2}^{\,\mathrm{conf}}$，且 $U|_{\mathbb R}=f$、
   $U(\infty)=0$；
2. $U$ 是 $C^2(\mathbb H^2)\cap C(\overline{\mathbb H^2}^{\,\mathrm{conf}})$ 中
   唯一满足这些边界条件的有界调和函数；
3. 在 $\operatorname{Re}F$ 满足第 2 项解类的全纯函数中，$F$ 唯一到虚常数。
   选定 Schwarz 积分使 $F(iy)\to0$（$y\to\infty$），从而固定该常数；
4. 若 $f$ 还是局部 $C^{0,\alpha}$（$0<\alpha<1$）或 Schwartz，则 $F$ 连续到有限边界，边界值为
   $f+iHf$；对 Schwartz 数据，DtN 与能量由命题 3.2(3)(4) 给出。

**证明**。1 的全纯性与 $U$ 的调和性是命题 3.2；$U$ 的连续性与边界值是经典
Poisson 定理（Paper II 的 `thm:C0-poisson-dirichlet` 的实部分）；$U(\infty)=0$ 实际只需 $f\in C_0$：先一致逼近为支撑于 $[-R,R]$ 的函数，
Poisson 卷积在 $L^\infty$ 中为压缩；对紧支撑部分，$y\to\infty$ 时用
$P_y\le1/(\pi y)$，$|X|\to\infty$ 时用
$y/((X-t)^2+y^2)\le1/(2|X-t|)$，得紧化无穷远处一致趋零。2 是极大值原理：两个解之差是有界调和、边界值为 $0$，故为
$0$。3 是两个全纯解之差为全纯、实部为 $0$，故为纯虚常数。4 是 Plemelj 公式
（Hölder 数据）与命题 3.2(3)(4)。$\square$

**状态**：`STANDARD CONSEQUENCE REQUIRING AN IN-PAPER PROOF`（若进正式论文）。
它与 Paper II 的 `thm:C0-poisson-dirichlet` 是同一实定理的复分析读法；区别是
这里的函数类更窄（$C_0\cap L^1$，以保证未减项的 Schwarz 积分绝对收敛），
且唯一性用极大值原理而非 RH 指标。

**与 Paper II 的关系**。Paper II 的定理对 $f\in C_0$（不要求 $L^1$）给出
实 Poisson 解；本处用 $L^1$ 定义 Schwarz 积分并控制其非切向无穷远极限。不能据此声称
一般数据的全纯解连续到整个紧化边界。所以
**Paper II 的实定理更强，C1 的全纯定理更结构化**：它把解写成 Cauchy 积分，
把 DtN 写成 Hilbert 变换，把边界问题写成 $G=-1$ 的 RH 问题。

### 3.5 矩阵 RH 与内禀复边界（提案）

**矩阵 RH 问题（`STRUCTURAL PROPOSAL`）**。给定跳矩阵后还需指定轮廓、
函数空间、无穷远规范化，以及是否要求解可逆；否则 $F_\pm=0$ 就是
$F_+=GF_-$ 的平凡解。规范化可逆矩阵问题通常涉及 Birkhoff 分解与部分指标，
不能仅由行列式绕数决定，也不能不加条件地等同于 Toeplitz 算子可逆。
本篇不使用此类存在性结论。

**AES 翻译（`STRUCTURAL PROPOSAL`）**。把 $G$ 读成"边界散射数据"：$f$ 是
赋值在边界上的值，$G$ 是赋值坐标变换的跳跃。标量指标 $\kappa$ 是"绕数
障碍"；矩阵情形是"分解障碍"。**没有证明**：AES 的边界数据是否总给出
Birkhoff 可分解的 $G$；这是 `OPEN`。

**内禀复边界（`OPEN`）**。C1 模型的"边界"是对角线
$$
D=\{w=\bar w\}\subset\mathbb P^1\times\mathbb P^1 .
$$
实理想边界 $\mathbb P^1(\mathbb R)$ 是 $D$ 的实轨迹，$\mathbb R$ 只是仿射部分。更内禀的 RH 问题应提在 $D$ 上：
求 $M$ 上的全纯场，使其跨越 $D$ 的跳跃满足给定的矩阵条件；Cauchy 核应是
复曲面上的 Cauchy--Fantappiè 核；指标应升级为 $D$ 上的除子类/线丛类
（$\operatorname{Pic}(D)$ 的元素）。但 $D\simeq\mathbb P^1$，其 Picard 群本身
由次数同构于 $\mathbb Z$；这不是已经建立的新指标。复余维一的 $D$ 也没有
实轮廓那样天然的“正负两侧”，必须先定义邻域、覆盖和过渡数据。**这是提案，不是定理**；
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
| 本篇讨论的推广 | 未展开 | 矩阵 RH / 指标 / Birkhoff 分解（提案） |

---

## 4. C2：Hermitian 伴随模型

### 4.1 定义

**定义 4.1（Hermitian AES）**。设 $M$ 是连通复曲线，
$g=e^{2\rho}|dz|^2$ 是 Hermitian 正定度量，$a\in\mathcal O(M)$，满足
$$
|\nabla a|_g^2=\mu^2+\lambda^2|a|^2,
\qquad \mu\in\mathbb R^\times,\ \lambda\in\mathbb R .
$$
本篇约定 $|\nabla a|_g^2:=\tfrac12(|\nabla\operatorname{Re}a|_g^2+
|\nabla\operatorname{Im}a|_g^2)$；对全纯 $a$，这等于单个实分量的梯度平方，
而不是两个分量梯度平方之和。于是局部坐标中
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
上述不只是径向曲线的长度：令 $L(R)=\lambda^{-1}\operatorname{arcsinh}(\lambda R/\mu)$，
任何分段光滑曲线 $\gamma$ 都有
$|d(L(|\gamma|))/dt|\le|\dot\gamma|_g$，所以从 $0$ 到半径 $R$ 的任何路径
长度至少为 $L(R)$，径向路径取等号。闭度量球因而包含于欧氏紧圆盘，
度量在每个紧圆盘上与欧氏度量等价，故闭度量球紧；Hopf--Rinow 给出完备性。4：
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

**有界区域的陈述（`STANDARD CONSEQUENCE WITH STATED HYPOTHESES`）**。
设 $\Omega\Subset M$ 是有界 $C^{2,\alpha}$ 区域，度量系数在
$\overline\Omega$ 上 $C^{1,\alpha}$ 且有正的上下界，则 $\Delta_g$ 一致椭圆。
在此处的共形二维情形，$\Delta_gU=0$ 等价于 $\Delta_0U=0$，
对 $C^{2,\alpha}$ 边界数据有唯一 $C^{2,\alpha}(\overline\Omega)$ 调和解。
正定性本身不保证非紧区域上的全局一致椭圆性，也不保证任意无界区域的唯一性。

C1 在实切片的 Dirichlet/Schwarz 读法与 C2 的二维椭圆理论并不互斥。
C1 在复曲面上的一个方向算子 $\partial_{\bar w}$ 不是整个实四维的椭圆系统，
而实切片上的通常 Cauchy--Riemann 系统是椭圆的；两者不可混称“CR 非椭圆”。

**基本模型的 Liouville 性质（`PROVED`）**。在 $M=\mathbb C$、
$g=|dz|^2/(\mu^2+\lambda^2|z|^2)$ 上，$\Delta_gU=0$ 等价于欧氏调和。
若实值 $U$ 有界，因 $\mathbb C$ 单连通，可写 $U=\operatorname{Re}F$，$F$ 整。
$e^F$ 是有界整函数，Liouville 定理使其常数，故 $F'=0$、$U$ 常数。
复值有界调和函数逐分量应用此论证。因此此问题不再标为开放。
DtN 则须先指定有边界的区域和法向规范化；一点紧化的 $\infty$ 不是自动
带有经典 DtN 算子的光滑边界。

### 4.6 C2 的零轨迹与 puncture

**命题 4.4**。设 $M$ 连通复曲线，$a$ 是非恒定全纯函数。则 $Z(a)$ 是离散
闭集。本命题按定义 4.1 的公式考察候选度量；在真正的正定 Hermitian AES 上
该公式迫使 $a'\ne0$，故只能出现单零点。允许退化的延拓中，在 $Z(a)$ 的每个点 $p$，若 $a$ 的零点阶为 $m$，则局部
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
   $\int_0|z|^{m-1}d|z|$ 有限，故删去该点的穿孔邻域有有限长度逃逸路径，不能在该端完备；
   若保留该点则度量退化，不再是正定 Hermitian AES；
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
| 已展示的等距作用（不作全等距群分类） | $\operatorname{PSL}_2(\mathbb R)$ | $\operatorname{PGL}_2(\mathbb C)$ 在 $N$ 上（$M$ 上仅共同定义域） | 未定（$\mathrm{Isom}(g)$） |

**一句话**：三个模型是同一个代数骨架的三种不同实现（实、复化、Hermitian）；
**曲率与零轨迹类型**不同；边界问题的比较须保留实切片、区域与函数空间条件。

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
3. **C2 的区域 DtN**：基本模型有界调和函数为常数已在 §4.5 证明；
   指定区域和法向后研究 DtN 显式核，仍为 `OPEN`。
4. **完备 Hermitian AES 的分类**：除 $a(z)=z$ 外还有哪些完备模型？曲率
   符号/总曲率的限制？`OPEN`。
5. **C2 的谱理论**：$-\Delta_g$ 在完备模型上的谱、Friedrichs 实现、热核。
   `OPEN`。
6. **C1 复长度与 C2 度量的关系**：$\ell$ 是 $\mathbb H^3$ 的复长度，不是
   C1/C2 的距离；是否存在一个把 $\ell$ 读成 C2 度量的"谱"或"平移"的公式？
   `OPEN`。
7. **p-adic/树方向**：note 50 §6.5 的提案；本篇未展开。`OPEN`。

---

## 附录 A：witness 检查范围

运行（普通模式与优化模式均须执行）：
```
python3 notes/analysis-and-calculus/51-complexified-model-and-rh-witness.py
python3 -O notes/analysis-and-calculus/51-complexified-model-and-rh-witness.py
```

本次普通模式与 `-O` 均为 **35/35** 通过（A: 11、B: 7、C: 3、E: 14）。
脚本显式统计全部检查，失败时非零退出，不使用会被 `-O` 删除的 `assert`。
A/B/C 检查局部代数恒等式与径向积分；E 检查共同定义域反例、无穷远图度量、
平方根覆盖关系和闭路绕数的具体见证、复零集以及 Fourier 能量积分。
这些不是全局定理的自动证明：群作用的图粘合、平方根单值化障碍、下降所需纤维连通、
完备性、Plemelj 边界极限、RH 适定性与 Liouville 性质依赖正文论证或明确引用。
脚本不覆盖一般矩阵 RH、内禀复边界、一般参数域的全局分支或任意数据的无穷远行为。

## 附录 B：与 Paper II 标签的对应

| 本篇 | Paper II 标签 |
|---|---|
| §1.2 基本模型 | `prop:hyperbolic-analytic-normalization` |
| §3.2 Dirichlet = RH | `thm:C0-poisson-dirichlet`（复分析读法） |
| §3.3 Poisson 核 | `lem:poisson-kernel-transport` |
| §3.3 DtN/能量 | §7 的 DtN 与能量结果 |
| §4.2 C2 调和性 | 无直接对应（C2 新定义） |
| §4.4 C2 基本模型 | 无直接对应（C2 新模型） |
