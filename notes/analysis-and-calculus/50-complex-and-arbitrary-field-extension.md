# Paper II 的复域与任意域扩充：分层、定理命运与路线图

**状态**：研究/设计笔记（research-and-design note）。它不是任何论文的源文件，
不进入 `governance/` 的状态登记，也不改变 Paper II 现有任何定理、命题、计算或
开放问题的状态。文中的新陈述按仓库的状态标签逐条标注；证明只写到笔记所需的
程度，正式论文中的证明必须另写。

**日期**：2026-11-07

**阅读对象**：`aeg-paper/paper-0`、`aeg-paper/paper-1`、`aeg-paper/paper-2`、
`aeg-paper/notes/analysis-and-calculus/01--03`、`48`、`49`；
`pcrg-paper/references/developing/08`、`09`、`10`；
`pcrg-paper/references/bivaluation-02.md`；
`pcrg-paper/notes/2026-06-17-*finite-field*`。

**配套脚本**：`50-complex-arbitrary-field-witness.py`（本目录；全部检查通过）。

---

## 0. 一句话结论

Paper II 的结论不是一个关于 $\mathbb R$ 的整体，而是一座三层建筑：

1. **Layer A（代数骨架）**：算术框架、eikonal 的二次型形式、结构函数、括号约束、
   Laplace 公式、raw/exact 因子分解、"arithmetic holomorphic $\Rightarrow$
   harmonic"、曲率公式。它们只用加法、乘法、除法、微分和 $i^2=-1$，因此在任意
   特征 $\ne 2$ 的域上成立，不需要测度、共轭、正性或序。
2. **Layer B（复分析中层）**：把 Layer A 的系数域取成 $\mathbb C$ 后得到的
   **全纯复化**（C1），以及在其上再加 Hermitian 结构得到的 **Hermitian 复化**
   （C2）。C1 给 Cauchy 核、Riemann--Hilbert 问题、Hilbert 变换；C2 给 $L^2$、
   Poisson 核、谱理论。
3. **Layer C（实分析顶层）**：序、正性、极大值原理、完备性、理想边界、调和测度、
   $L^2$ 谱、实三分与实长度。Paper II 现在住在这里。

所以"复域扩充"不是把 $\mathbb R$ 全局换成 $\mathbb C$，而是**把三层分开，把
每一层推到它真正的边界**。而 `pcrg-paper` 的双赋值理论（`bivaluation-02`）正是
Layer A 的一次独立发现：它的
"任意域代数骨架 $\to$ 复代数化 $\to$ Hermitian/概率版本"
与本文的 Layer A $\to$ C1 $\to$ C2 是同一分层。

一句话的版本：

> **Paper II 的实分析结论 = 一个可在任意域上写下的代数骨架 + 一个复分析中层 +
> 一个实分析顶层。复域扩充的任务是认领这个骨架，并决定中层要 C1 还是 C2。**

---

## 1. 三种"复化"与一种"域扩张"

先把可能的读法列清楚。它们在文献里都叫"complexification"，但数学上不同，
不能混用。

### 1.1 C1：代数/全纯复化（推荐的主线）

把 $(M,g,a;\mu,\lambda)$ 整体复化：

- $M$ 是复曲面（复维 $2$，即实维 $4$）；
- $g$ 是**全纯对称双线性型**（不是 Hermitian 型），非退化；
- $a\in\mathcal O(M)$ 全纯，$\mu\in\mathbb C^\times$，$\lambda\in\mathbb C$；
- eikonal 写成复双线性形式
  $$
  (\nabla a)^2:=\sum_{i,j}g^{ij}\partial_i a\,\partial_j a
  =\mu^2+\lambda^2a^2 .
  $$

这是对 Paper II 方程的字面域扩张：每个公式都保持，只是不再有共轭、绝对值、
正性与序。实理论是它的一个**实形式**（real form）：一个共轭 $\sigma$ 使
$\sigma^*g=\bar g$、$\sigma^*a=\bar a$，实轨迹 $M^\sigma$ 就是原来的 AES。

C1 的自然分析不是 $L^2$ 分析，而是复分析：Cauchy 核、留数、
Riemann--Hilbert 问题、全纯延拓。它的"正则性"由 $q^2:=\mu^2+\lambda^2a^2\ne0$
和一个 $q$ 的平方根分支控制；$q=0$ 是新的**极除子**（polar divisor），在实理论里
不可能出现（因为 $\mu\ne0$ 时 $q^2>0$）。

### 1.2 C2：Hermitian 复化（$L^2$/谱版本）

$M$ 是复曲线（复维 $1$），$g$ 是**正定 Hermitian 度量**，$a:M\to\mathbb C$ 全纯。
此时 $|\nabla a|_g^2\ge0$ 是实数，未 Hermitian 化的 eikonal
$$
|\nabla a|_g^2=\mu^2+\lambda^2a^2
$$
会强迫 $a$ 为常数（见 §5.1 的 no-go）。要得到非平凡理论，必须把 eikonal
**Hermitian 化**：
$$
|\nabla a|_g^2=\mu^2+\lambda^2|a|^2 .
$$
这条路线保留正性、测度、$L^2$、Poisson 核与谱理论，代价是 eikonal 不再是
Paper II 的那一条。它对应双赋值的 Hermitian 版本 $I_H=1+a\bar c$（`bivaluation-02`
§26；自对偶 $c=a$ 时给出 $1+|a|^2$），而不是代数版本 $I=1+ab$。

### 1.3 C3：值复化（$a:M\to\mathbb C$，$g$ 仍为实 Riemann 度量）

$M$ 实二维，$g$ 正定，$a=u+iv$。eikonal 分裂成实方程组
$$
|\nabla u|^2-|\nabla v|^2=\mu^2+\lambda^2(u^2-v^2),
\qquad
\langle\nabla u,\nabla v\rangle=\lambda^2uv .
$$
这是两个方程对两个未知函数；主象征行列式为
$2|(\nabla u+i\nabla v)\cdot\xi|^2=2|(\nabla a)\cdot\xi|^2$，故在
$\xi\perp\nabla a$ 时退化。它刚性、不是"任意全纯函数"意义上的函数论；
它更像一个复 eikonal 的 PDE 课题，而不是 Paper II 的函数论。**不推荐作为
主线**，但可以作为"复相位 eikonal"的独立问题。

一个先要记住的 no-go：**不能只把 $\mu,\lambda$ 复化而让 $a$ 仍取实值、$g$ 仍
正定**。因为 $|\nabla a|^2\ge0$ 是实数，而 $\mu^2+\lambda^2a^2$ 一般不是实数；
若 $a$ 的取值含一个区间且 $\mu,\lambda$ 有非零虚部，方程无解。要么 $a$ 复化
（C3），要么 $g$ 复化（C1），要么 Hermitian 化（C2）。

### 1.4 K：任意域上的代数骨架

不假设度量、拓扑、序、共轭。取一个域 $K$（$\operatorname{char}K\ne2$），
一个交换 $K$-代数 $A$，$a\in A$，两个导子 $X_u,X_v\in\operatorname{Der}_K(A)$，
$\mu\in K^\times$，$\lambda\in K$，满足
$$
X_u a=\mu,\qquad X_v a=\lambda a,\qquad
[X_u,X_v]=c_uX_u+c_vX_v\quad(c_u,c_v\in A).
$$
如果再给一个对称双线性型 $g$ 使 $g(X_i,X_j)=\delta_{ij}$，就得到度量版本；
$q^2:=\mu^2+\lambda^2a^2$ 是单位时称**正则**。这是 Layer A 的定义，见 §3。

### 1.5 一张选择表

| | C1 全纯复化 | C2 Hermitian 复化 | C3 值复化 | K 任意域 |
|---|---|---|---|---|
| 载体 | 复曲面 | 复曲线 | 实曲面 | 交换 $K$-代数 |
| $g$ | 全纯双线性 | Hermitian 正定 | 实正定 | 对称双线性（可选） |
| $a$ | 全纯 | 全纯 | $M\to\mathbb C$ | $a\in A$ |
| eikonal | $(\nabla a)^2=q^2$ | $\lVert\nabla a\rVert^2=\mu^2+\lambda^2\lVert a\rVert^2$ | 分裂成 2 个实方程 | 二次型恒等式 |
| 共轭 | 无 | 有 | 有 | 无 |
| 正性/序 | 无 | 有 | 有 | 无 |
| 测度/$L^2$ | 无 | 有 | 有 | 无 |
| 自然分析 | Cauchy/Riemann--Hilbert | Poisson/谱 | 非线性椭圆系统 | 无（代数） |
| 三分 | 只剩 split/parabolic | 依所选实形式 | 实三分 | $\Delta$ 的平方类 |
| 长度 | 复长度 $\log\kappa$ | 依所选实形式 | 实长度 | 离散/赋值 |

---

## 2. Paper II 的三层建筑

### 2.1 Layer A：代数骨架

下列结果只用到"两个导子 + 一个赋值 + 一个括号关系"，因此可以逐字搬到任意
特征 $\ne2$、含 $i$ 的域上。它们是 Paper II 的**代数核心**：

- 框架的导数法则 $X_u a=\mu$、$X_v a=\lambda a$
  （Paper 0, `prop:canonical-arithmetic-frame`）；
- 结构函数与约束
  $$
  [X_u,X_v]=c_uX_u+c_vX_v,\qquad
  \mu c_u+\lambda a c_v=\mu\lambda
  $$
  （Paper II, eq. `eq:surface-structure-assignment-constraint`）；
- 散度与形式伴随（`prop:surface-frame-divergence`）——散度公式
  $\operatorname{div}_g X_u=-c_v$、$\operatorname{div}_g X_v=c_u$（相对由 $g$
  决定的体积形式）是代数的；**形式伴随**需要内积/测度，属于 Layer B/C；
- 框架 Laplace 公式
  $$
  \Delta_g=X_u^2+X_v^2-c_vX_u+c_uX_v
  $$
  （`prop:surface-frame-laplacian`）——作为**微分表达式**是代数的；
- raw 因子分解
  $$
  4\partial_{\!AEG}\bar\partial_{\!AEG}
  =X_u^2+X_v^2+i[X_u,X_v],\qquad
  4\bar\partial_{\!AEG}\partial_{\!AEG}
  =X_u^2+X_v^2-i[X_u,X_v]
  $$
  （`prop:surface-raw-factorization`）；
- exact drift 因子分解
  $$
  4\partial\bar\partial=\Delta_g+2(c_v+ic_u)\bar\partial,\qquad
  4\bar\partial\partial=\Delta_g+2(c_v-ic_u)\partial
  $$
  （`prop:surface-exact-drift-factorizations`）；
- 形式伴随因子分解
  $$
  4\bar\partial^*\bar\partial=-\Delta_g
  $$
  （`thm:surface-adjoint-factorization`）——这里的 $*$ 在实理论中是
  $L^2(d\mathrm{vol}_g)$ 的形式伴随；在代数层，它是一个**由恒等式定义的
  代数算子** $\bar\partial^T=-\partial+\tfrac12(c_v+ic_u)$，见定理 3.2 与注 3.2；
- "全纯 $\Rightarrow$ 调和"
  （`thm:surface-holomorphic-implies-harmonic`）；
- 曲率公式 $K=\lambda^2(\mu^2-\lambda^2a^2)/(\mu^2+\lambda^2a^2)$
  （`prop:planar-harmonic-aes`）作为代数恒等式；
- 结构常数在基本模型中的值 $c_u=\lambda$、$c_v=0$，以及
  $\Delta_g=X_u^2+X_v^2+\lambda X_v$。

**关键观察**：Paper II 的证明里，`thm:surface-adjoint-factorization` 的
计算其实没有用到共轭、测度或正性；它只用了
$4\partial\bar\partial=X_u^2+X_v^2+i[X_u,X_v]$ 和
$\bar\partial^*=-\partial+\tfrac12(c_v+ic_u)$。后者的"伴随"身份是实的，
但恒等式本身是代数的。因此**该定理的代数内容可以逐字搬到任意域**，见 §3.2。

### 2.2 Layer B：复分析中层

Layer B 有两支：

- **C1**：Cauchy 核 = Poisson 核的跳跃；Schwarz 积分；Riemann--Hilbert 问题；
  Dirichlet-to-Neumann 映射 = Hilbert 变换 $\mathcal N=|D|=HD$；
  能量 = $H^{1/2}$ 二次型。见 §4.6。
- **C2**：Poisson 核、$L^2$、Friedrichs 实现、谱、极大值原理、
  Dirichlet 唯一性类。见 §5。

C1 与 C2 的关系不是"一个更一般，一个更特殊"，而是**同一个代数骨架的两种
不同复化**：C1 是复化本身（不取共轭），C2 是加共轭与正性的 Hermitian 版本。
双赋值的 $b=a$（代数自对偶）与 $b=\bar a$（Hermitian 对偶）正是这两个版本。

### 2.3 Layer C：实分析顶层

Paper II 现有的下列结果真正用到 $\mathbb R$ 的序、正性、完备性或测度：

- $|\nabla a|^2=\mu^2+\lambda^2a^2$ 的**正性**，$q>0$，$E_a=\nabla a/q$；
- $q^2>0$ 保证 $\nabla a\ne0$，从而水平集是光滑曲线、零轨迹正则
  （Paper I 的 `thm:regular-zero-locus`）；
- 定向正交框架的唯一性（正性 + 定向）；
- Riemann 体积 $d\mathrm{vol}_g$、散度、形式伴随、Dirichlet 能量；
- Friedrichs 实现、Hörmander 次椭圆性、$L^2$ 谱；
- 极大值原理、Poisson 核的正性与总质量 $1$、$C_0$ Dirichlet 唯一性类；
- 理想边界、调和测度、完备性、曲率符号 $K=-\lambda^2<0$；
- 实三分（双曲/抛物/椭圆）与实长度 $2\operatorname{arccosh}(|\tau|/2)$。

这些在 C1 里大多**没有对应物**；在 C2 里有一部分保留（Poisson、$L^2$、谱、
极大值原理），但 eikonal 已被 Hermitian 化，且三分只剩相对实结构才有意义。

### 2.4 定理逐条命运表

图例：✓ = 逐字成立；≈ = 需要修改/换定义；✗ = 不成立或没有意义；
— = 不适用。

| Paper II 结果 | C1 全纯 | C2 Hermitian | K 任意域 |
|---|---|---|---|
| 正则 AES 定义 | ✓（$g$ 复双线性，$q\ne0$） | ≈（$g$ Hermitian，eikonal 取模） | ≈（代数定义） |
| 规范框架 | ≈（需 $J$；$q$ 只是局部记号） | ≈（需 $J$，正性给 $q>0$） | ≈（需 $J$；$q^2$ 不一定是平方） |
| 结构函数/约束 | ✓ | ✓ | ✓ |
| 散度（相对体积形式） | ≈（需选体积形式） | ✓ | ≈（需选体积形式） |
| 形式伴随（$L^2$） | ✗（无测度） | ✓ | ✗（只有代数算子） |
| 框架 Laplace 公式 | ✓（微分表达式） | ✓ | ✓ |
| raw 因子分解 | ✓ | ✓ | ✓ |
| exact drift 因子分解 | ✓ | ✓ | ✓ |
| 伴随因子分解 $4\bar\partial^*\bar\partial=-\Delta$ | ≈（代数算子，非伴随） | ✓ | ≈（代数算子，非伴随） |
| 全纯 $\Rightarrow$ 调和 | ✓（代数） | ✓（$L^2$ 局部） | ✓（代数） |
| $U(1)$ 规范协变 | ≈（$\mathbb C^\times$ 规范） | ✓（$U(1)$） | ≈（$K^\times$/范数一） |
| Dirichlet 能量/Friedrichs | ✗ | ✓ | ✗ |
| 平面基/曲率公式 | ≈（需实结构的全纯替代） | ✓ | ✓（代数恒等式） |
| 全纯拉回 | ✓（局部双全纯） | ✓ | ≈（代数拉回） |
| 柱面 AES/自守下降 | ≈（$\log\lVert W\rVert$ 需复化） | ✓ | ≈（代数版本） |
| 基本双曲模型 | ✓（复化模型，§4.2） | ≈（不同实形式） | ≈（代数基本模型，例 3.1/3.2） |
| Poisson 核 | ≈（Cauchy 核的跳跃） | ✓ | ✗ |
| $C_0$ Dirichlet 定理 | ≈（Riemann--Hilbert/Schwarz） | ✓（需类） | ✗ |
| DtN $=\lVert D\rVert$ | ≈（$=HD$，Hilbert 变换） | ✓ | ✗ |
| 能量 $=H^{1/2}$ | ✓（复系数） | ✓ | ✗ |
| 显式族（$\arctan$、正频率） | ≈（$\arctan\rightsquigarrow\log$） | ✓ | ≈（代数/有限域版本） |
| 接触分支：非整分/括号 | ✓ | ✓ | ✓ |
| 接触分支：Friedrichs/Hörmander | ≈（括号条件 ✓；次椭圆性需实结构） | ✓ | ✗ |
| 接触分支：CR 因子分解 | ✓ | ✓ | ✓ |
| 接触分支：对数首次积分 | ≈（多值 $\mathrm{Log}$，见 §4.8） | ✓ | ≈（代数对数） |
| 仿射--Appell 模 | ≈（需指数/形式幂级数） | ✓ | ≈（形式版本） |

这张表是本文的核心。它说明：**Paper II 的大部分"框架性"内容其实属于
Layer A，而不是 $\mathbb R$ 的专利；真正属于 $\mathbb R$ 的是"分析"那一半。**

---

## 3. Layer A：任意域上的代数 AES

### 3.1 定义

**定义 3.1（代数 AES）**。设 $K$ 是域，$\operatorname{char}K\ne2$。
一个 $K$ 上的**代数 AES** 是数据 $(A,a;X_u,X_v;\mu,\lambda)$：

- $A$ 是交换 $K$-代数；
- $a\in A$；
- $X_u,X_v\in\operatorname{Der}_K(A)$；
- $\mu\in K^\times$，$\lambda\in K$；

满足
$$
X_u a=\mu,\qquad X_v a=\lambda a,
$$
且存在 $c_u,c_v\in A$ 使
$$
[X_u,X_v]=c_uX_u+c_vX_v .
$$
若再给一个对称 $A$-双线性型 $g$ 使 $g(X_i,X_j)=\delta_{ij}$，称**度量版本**；
若 $q^2:=\mu^2+\lambda^2a^2$ 是 $A$ 的单位，称**正则**。

**例 3.1（最简代数模型，非度量版本）**。$A=K[a]$，$X_u=\mu\,\partial_a$，
$X_v=\lambda a\,\partial_a$。则 $X_u a=\mu$，$X_v a=\lambda a$，
$[X_u,X_v]=\lambda X_u$，所以 $c_u=\lambda$，$c_v=0$，
$q^2=\mu^2+\lambda^2a^2$。**注意**：这不是度量版本。两个导子在 $K(a)$ 上
线性相关（$X_v=(\lambda a/\mu)X_u$），不能同时正交归一；它只是代数 AES 的
最简例子。

**例 3.2（度量版本：Paper 0 基本模型的代数骨架）**。取
$A=K[x,y,y^{-1}]$，$a=-x/y$，
$$
X_u=-\mu y\,\partial_x,\qquad X_v=-\lambda y\,\partial_y,
$$
$$
g=\frac1{y^2}\left(\frac{dx^2}{\mu^2}+\frac{dy^2}{\lambda^2}\right).
$$
则 $X_u a=\mu$、$X_v a=\lambda a$、$[X_u,X_v]=\lambda X_u$，
且 $g(X_i,X_j)=\delta_{ij}$、$g^{-1}(da,da)=\mu^2+\lambda^2a^2$。这里
$X_u,X_v$ 线性无关，是真正的 2 维框架；$q^2=(x^2+y^2)/y^2$（在
$\mu=\lambda=1$ 时）一般不是 $K[x,y,y^{-1}]$ 中的平方，但框架仍然存在。
这正说明 $q$ 只是写单位梯度的方便记号，不是框架存在的前提。

**注 3.1**。在 Paper 0 的原定义里，$g$ 是 Riemann 度量、$a$ 是实函数、
$q>0$、框架由正性与定向唯一确定。在代数定义里，$g$ 只是对称双线性型，
$q^2$ 可能不是平方，$q$-公式可能只在二次扩张上存在；框架本身在 $J$ 存在且
$X_u,X_v$ 线性无关时可以存在（例 3.2）。**这些"缺失"不是缺陷，而是 Layer A
的准确边界。**

### 3.2 定理 A：Paper II 的代数内容

**定理 3.2（代数 Paper II）**。设 $(A,a;X_u,X_v;\mu,\lambda)$ 是 $K$ 上的
代数 AES，$i\in K$（或把一切基扩张到 $K[i]$）。令
$$
\partial=\frac12(X_u-iX_v),\qquad
\bar\partial=\frac12(X_u+iX_v),
$$
$$
\Delta:=X_u^2+X_v^2-c_vX_u+c_uX_v,\qquad
\bar\partial^T:=-\partial+\frac12(c_v+ic_u),\qquad
\partial^T:=-\bar\partial+\frac12(c_v-ic_u).
$$
则作为由 $X_u,X_v$ 生成的 $A$-微分算子环中的元素：

1. $[X_u,X_v]a=\mu\lambda$，且 $\mu c_u+\lambda a c_v=\mu\lambda$；
2. $4\partial\bar\partial=X_u^2+X_v^2+i[X_u,X_v]$，
   $4\bar\partial\partial=X_u^2+X_v^2-i[X_u,X_v]$；
3. $4\bar\partial^T\bar\partial=-\Delta$，且 $4\partial^T\partial=-\Delta$；
4. 若 $\bar\partial F=0$，则 $\Delta F=0$；
5. 若 $g$ 是对称双线性型、$X_u,X_v$ 线性无关（故有对偶余框架
   $\eta^u,\eta^v$），且 $g(X_i,X_j)=\delta_{ij}$，则
   $g^{-1}(da,da)=\mu^2+\lambda^2a^2$（这里 $g^{-1}$ 是 $\Omega^1$ 上的
   对偶度量；下文简写为 $g(da,da)$ 时同义）。

**证明**。1 是把括号作用于 $a$：$[X_u,X_v]a=X_u(\lambda a)-X_v(\mu)=\mu\lambda$；
再与 $c_uX_u+c_vX_v$ 作用于 $a$ 比较。2 是直接展开
$(X_u\mp iX_v)(X_u\pm iX_v)$。3 是
$$
4\bar\partial^T\bar\partial
=-4\partial\bar\partial+2(c_v+ic_u)\bar\partial
=-S-i[X_u,X_v]+(c_v+ic_u)(X_u+iX_v)
=-S+c_vX_u-c_uX_v=-\Delta,
$$
其中 $S=X_u^2+X_v^2$；展开时系数 $c_u,c_v$ 始终写在导子左边，不需要把它们
移过导子，因此没有 $X_u(c_v)$、$X_v(c_u)$ 之类的项。4 由 3 立即得到。
5 是框架正交归一的定义：
$da=\mu\eta^u+\lambda a\eta^v$，故
$g^{-1}(da,da)=\mu^2+\lambda^2a^2$。

**状态**：`PROVED WITH STATED HYPOTHESES`（$\operatorname{char}K\ne2$，$i\in K$
或 $K[i]$）。计算已由 `50-complex-arbitrary-field-witness.py` 的 B1--B3 检查
（B1 用中心结构函数，B2/B3 用一个 $c_v\ne0$ 的具体非坐标框架）。

**注 3.2（"伴随"到底是什么）**。在实理论里，$\bar\partial^*$ 是
$L^2(d\mathrm{vol}_g)$ 的形式伴随；在代数层，$\bar\partial^T$ 是**由恒等式 3
定义的算子**，不声称它是某个内积的伴随。两者在 $\mathbb R$ 上一致，是因为
散度项恰好给出 $\tfrac12(c_v+ic_u)$。不要把 $\bar\partial^T$ 误读为 Hilbert
伴随：后者需要测度和共轭，属于 Layer B。

### 3.3 框架的存在性与唯一性

Paper 0 的框架公式
$$
X_u=\frac{\mu}{q}E_a-\frac{\lambda a}{q}JE_a,\qquad
X_v=\frac{\lambda a}{q}E_a+\frac{\mu}{q}JE_a
$$
用到三样东西：$J$（$J^2=-1$ 的复结构）、$E_a=\nabla a/q$（单位梯度），以及把
$\nabla a$ 归一化的 $q$。在 $\mathbb R$ 上，$J$ 由定向唯一确定，$q>0$ 由正性
唯一确定；在 $K$ 上，$J$ 是额外选择，而 $q$ 只是写公式的方便记号。

**命题 3.3（框架的存在性与唯一性）**。在代数 AES 上：

1. 框架（当它存在时）由 $(g,a,J)$ 与导数法则唯一确定。$q$ 不是框架的一部分：
   $q\mapsto -q$ 同时使 $E_a=\nabla a/q$ 变号，公式给出的 $(X_u,X_v)$ 不变。
2. 公式中的 $q$ 需要 $q^2=\mu^2+\lambda^2a^2$ 在所考虑的环中是平方。若它不是
   平方，公式只存在于二次扩张
   $A[q]/(q^2-(\mu^2+\lambda^2a^2))$ 上，或存在于 $q^2$ 为平方的局部化上。
   **框架本身可以存在而不需要 $q\in A$**：例如例 3.2 的度量基本模型，
   $X_u,X_v$ 与 $g$ 都存在，而 $q^2=(x^2+y^2)/y^2$ 一般不是
   $K[x,y,y^{-1}]$ 中的平方。
3. 真正的额外选择是 $J$（$J^2=-1$，且与 $g$ 相容）：在 $\mathbb R$ 上由定向
   唯一确定；在 $\mathbb C$ 上是复结构的一部分；在 $K$ 上可能不存在，或只在
   二次扩张上存在。$q=0$ 不是框架的极除子，而是 $q$-公式（即单位梯度 $E_a$）
   的极除子；框架作为环境空间上的导子可以在 $q=0$ 处继续存在（如 §4.3 的
   $w=0$），尽管该点不在正则轨迹 $M$ 内。

**状态**：`PROVED`（1--3 是初等的）。1 的唯一性草图：满足 eikonal 的框架必是
$(E_a,JE_a)$ 的旋转，旋转角由 $\cos\theta=\mu/q$、$\sin\theta=-\lambda a/q$
在 $J$ 固定时唯一确定。**措辞修正**：Paper 0 所谓"规范"框架，
在 Layer A 里应读作"给定 $J$ 后规范；$q$ 是局部表达式"；"规范"的强度随域而
变化。这是正式论文里应明确写出的一点。

### 3.4 eikonal 作为自入射：$q^2=\mu^2I(\alpha,\alpha)$

令
$$
\alpha:=\frac{\lambda a}{\mu}.
$$
则
$$
q^2=\mu^2(1+\alpha^2)=\mu^2 I(\alpha,\alpha),
\qquad
I(\alpha,\beta):=1+\alpha\beta .
$$
$I$ 正是双赋值理论的入射标量（`bivaluation-02` §24.2）。于是：

- $q^2=0$（$q$-公式/单位梯度的极除子）$\iff$ $\alpha^2=-1$ $\iff$
  $\alpha=\pm i$（在含 $i$ 的域中）；在 $K$ 中存在解 $\iff$ $-1$ 是 $K$ 的平方。
- $\mathbb R$：无解（$q^2>0$），单位梯度无处不在（框架本身也处处存在）；
- $\mathbb C$：$\alpha=\pm i$，两个极除子（框架本身仍可继续存在）；
- $\mathbb F_q$（$q$ 奇）：有解 $\iff q\equiv1\pmod4$。已对 $q=3,5,7,11,13$
  验证（witness C 部分）。

**状态**：`PROVED`（初等）+ `COMPUTATIONALLY VERIFIED EXAMPLE`（有限域）。
这个观察把"单位梯度何时失效"从一个分析问题变成了一个**算术问题**：退化除子
的存在性由 $-1$ 的平方类决定。注意区分：$q=0$ 是**正规化**（单位梯度）的极
除子，不一定是框架的极除子（见命题 3.3(3) 与 §4.3）。

### 3.5 三分：$\Delta$ 的平方类与不动点的 Galois 作用

**定理 3.4（任意域三分）**。设 $K$ 是特征 $\ne2$ 的域，
$M\in\operatorname{PGL}_2(K)$，取任意提升
$\widetilde M=\left(\begin{smallmatrix}A&B\\C&D\end{smallmatrix}\right)$，令
$$
\tau:=\frac{\operatorname{tr}(\widetilde M)^2}{\det\widetilde M}\in K .
$$
则 $M$ 在 $\mathbb P^1(\bar K)$ 上的不动点由二次方程
$$
Cz^2+(D-A)z-B=0
$$
给出（$C=0$ 时按线性方程与 $\infty$ 处理），其判别式为
$$
\operatorname{disc}=\operatorname{tr}^2-4\det=\det\cdot(\tau-4).
$$
令 $[\cdot]\in K^\times/(K^\times)^2$ 记平方类（$[0]:=0$）。则：

1. $[\tau-4]=0$：抛物；一个 $K$-有理重不动点；不动点除子就是入射除子。
2. $[\tau-4]=[\det]$：分裂；两个不同的 $K$-有理不动点。
3. 其它：非分裂；没有 $K$-有理不动点；两个不动点在二次扩张
   $K(\sqrt{\det(\tau-4)})$ 上共轭。

**证明**。不动点方程由 $z(Cz+D)=Az+B$ 得到；判别式计算是直接的。
$K$-有理根的个数由判别式的平方类决定；$\det$ 的平方类在 $\widetilde M$ 的
标量伸缩下不变，所以三种情形由 $\operatorname{PGL}_2(K)$-共轭类的两个不变量
$[\det]$ 与 $[\tau-4]$ 决定。$\square$

**状态**：`STANDARD CONSEQUENCE REQUIRING AN IN-PAPER PROOF`。$\mathbb R$ 情形
就是 Paper 0 的 `prop:p0-projective-trichotomy`（双曲/抛物/椭圆）；$\mathbb F_q$
情形由 `pcrg-paper` 的 `10-the-trichotomy-and-what-changes-over-fq` 用 Legendre
符号表述并穷尽验证；本文的 witness C 部分对
$q=3,5,7,11,13$ 验证了"判别式平方类 $\leftrightarrow$ 有理不动点数"的对应，
无不符。

**长度**。同一个乘子 $\kappa$（特征值比，确定到 $\kappa\leftrightarrow\kappa^{-1}$）
在不同域上有不同类型的读出：

| 域 | 长度/不变量 | 类型 |
|---|---|---|
| $\mathbb R$（分裂） | $\ell=2\operatorname{arccosh}(\lvert\tau\rvert/2)=\bigl\lvert\log\lvert\kappa\rvert\bigr\rvert$ | 连续 |
| $\mathbb C$ | $\ell=\log\kappa\pmod{2\pi i}$ | 复连续 |
| $\mathbb F_q$ | $\operatorname{ord}(\kappa)\mid q-1$ | 离散 |
| 赋值域 $(K,v)$ | $-v(\kappa)$ | 离散/整数 |
| 一般域 | 只有 $\kappa$ 的共轭类 | 无长度 |

这正是 `pcrg-paper` note 10 的中心句："三分从来不是阻碍；变的是不变量的类型——
连续的长度对离散的除数。"

### 3.6 与 pcrg 双赋值的字典

双赋值理论（`bivaluation-02`）的核心对象是
$$
V_K=K^2,\quad V_K^\vee,\quad
[v]\in\mathbb P^1(K),\quad [\varphi]\in\mathbb P^1(K)^\vee,
$$
$$
a(v)=-\frac XY,\qquad b(\varphi)=-\frac RS,\qquad
I(a,b)=1+ab=\varphi(v).
$$
这与 Paper 0 的基本模型赋值 $a=-x/y$ 是同一个公式。字典如下：

| AES | 双赋值 | 备注 |
|---|---|---|
| 赋值 $a_{\mathrm{AES}}=-x/y$ | 点侧赋值 $a=-X/Y$ | 同一个公式 |
| 归一化 $\alpha=\lambda a_{\mathrm{AES}}/\mu=-X/y$ | 点侧赋值 $a$ | $\alpha$ 是双赋值坐标 |
| eikonal $q^2=\mu^2+\lambda^2a^2$ | $\mu^2 I(\alpha,\alpha)$ | 自入射 |
| $q$-正规化的极除子 $q=0$ | 入射除子 $I(\alpha,\alpha)=0$ | $\alpha=\pm i$ |
| Hermitian eikonal $\mu^2+\lambda^2\lVert a\rVert^2$ | $\mu^2 I_H(\alpha,\bar\alpha)$，$I_H=1+\lVert\alpha\rVert^2$ | $b=\bar a$ |
| 框架 $(X_u,X_v)$ | 对偶对 $(v,\varphi)$ 的度量读法 | 需度量与 $J$；不是逐字同一 |
| 不动点对 $(q_+,q_-)$ | 像方向/核方向 | $q_+=[v]$，$q_-=\ker\varphi$ |
| 抛物 $q_+=q_-$ | 入射除子 | $\Delta=0$ |
| 分裂/非分裂 | 两个 $K$-点 / 共轭对 | Galois 作用 |
| 秩一凝聚 $\Pi=v\otimes\varphi/\varphi(v)$ | 双赋值凝聚子 | $\varphi(v)\ne0$ 即正则 |
| 投影运动 | $\operatorname{PGL}_2(K)$ | 同一个群 |

**状态**：`STRUCTURAL PROPOSAL`（字典本身）。它的每一行都有独立依据
（Paper 0 的矩阵读法、`bivaluation-02` 的定义、本文 §3.4--3.5 的计算），
但"字典是一个函子"没有任何证明，不应这样陈述。

**关键区分**（`bivaluation-02` §26 的核心）：代数对偶的 $b$ 与 Hermitian
共轭的 $\bar a$ 不是一回事。AES 的实 eikonal 用的是 $b=a$（代数自对偶），
Hermitian 版本用的是 $b=\bar a$。在 $\mathbb R$ 上两者重合，在 $\mathbb C$ 上
分道扬镳——这正是 C1 与 C2 的分水岭。

### 3.7 任意域上什么没有了

保留下来的：框架、eikonal（二次型）、括号约束、Laplace 公式、因子分解、
全纯 $\Rightarrow$ 调和、射影运动、三分、代数零轨迹、曲率作为代数函数。

没有了的：积分、测度、$L^2$、Poisson 核、Dirichlet 问题、谱、极大值原理、
完备性、曲率符号、收敛、连续长度。

**有限域的额外警告**（`pcrg-paper` 09/10）：

- 容量 = 载体维数，冗余 = $q+1$；扩域买不到连续容量（09）；
- $\operatorname{PSL}_2(\mathbb F_q)$ 只有 $(q+5)/2$ 个共轭类，装不下一个连续统，
  所以连续长度不是"技术困难"，是"位置不够"（10）；
- 抛物层是 torsor 层：$\ell=0$ 不是空层，而是"不变量消失、全部内容交给选择"的
  那一层（09）；
- 有限域上没有吸引收敛：$\operatorname{PGL}_2(\mathbb F_q)$ 是有限群，
  轨道最终周期化；"不动点存在"不等于"吸引不动点存在"（2026-06-17 有限域笔记）。

这些是 Layer A 的"失败图册"，不是 Layer C 的奇点。**不要把它们当成 Paper III
的解析奇点。**

---

## 4. C1：全纯复化

### 4.1 定义

**定义 4.1（全纯 AES）**。设 $M$ 是复曲面，$g$ 是全纯对称双线性型（非退化），
$a\in\mathcal O(M)$，$\mu\in\mathbb C^\times$，$\lambda\in\mathbb C$，满足
$$
(\nabla a)^2=\mu^2+\lambda^2a^2,
\qquad
q^2:=\mu^2+\lambda^2a^2\in\mathcal O(M)^\times,
$$
并假定 $q$ 的一个全纯平方根存在、选定它，且存在一个复结构 $J$（$J^2=-1$，
$g(JX,JY)=g(X,Y)$，$g(X,JX)=0$）。称 $(M,g,a;\mu,\lambda;q,J)$ 为**全纯 AES**。

**定义 4.2（实形式）**。一个共轭 $\sigma:M\to M$ 使
$\sigma^*g=\bar g$、$\sigma^*a=\bar a$、$\sigma^*q=\bar q$，
且实轨迹 $M^\sigma$ 是 Paper 0 意义下的正则 AES，称 $(M,g,a)$ 的一个实形式。

Paper II 的实理论就是 C1 的一个实形式；C1 是它的全纯延拓。

### 4.2 复化基本模型

取
$$
M=\{(w,\bar w)\in\mathbb C^2:\ w\ne\bar w,\ w\bar w\ne0\},
$$
$$
g=-\frac{4}{\lambda^2}\frac{dw\,d\bar w}{(w-\bar w)^2},
\qquad
a=-\frac{i\mu}{\lambda}\frac{w+\bar w}{w-\bar w}.
$$
这里 $dw\,d\bar w$ 是对称双线性积，**不是** Hermitian $(1,1)$-形式。
**注意**：$(w,\bar w)$ 是两个独立的复坐标；直到取实形式（第 7 条）时才令
$\bar w$ 为 $w$ 的复共轭。

**命题 4.3**。在上述数据下：

1. $(\nabla a)^2=\mu^2+\lambda^2a^2$；
2. $\Delta_g a=2\lambda^2a$；
3. 框架 $X_u=-\lambda y(\partial_w+\partial_{\bar w})$、
   $X_v=-i\lambda y(\partial_w-\partial_{\bar w})$ 满足
   $X_u a=\mu$、$X_v a=\lambda a$、$[X_u,X_v]=\lambda X_u$；
4. $\Delta_g=X_u^2+X_v^2+\lambda X_v$；
5. $\bar\partial_{\!AEG}=\tfrac12(X_u+iX_v)=-\lambda y\,\partial_{\bar w}$，
   所以 arithmetic holomorphic 场就是 $F(w)$；
6. $q^2=-\dfrac{4\mu^2w\bar w}{(w-\bar w)^2}$；
7. 实形式：取 $w=X+iy$、$\bar w=X-iy$（即 $\bar w$ 是 $w$ 的复共轭），
   $y>0$，则给出 Paper II 的基本模型：$X=\operatorname{Re}w$，
   $a=-(\mu/\lambda)X/y$，$g=\lambda^{-2}(dX^2+dy^2)/y^2$。

**证明**。1--6 是直接计算，已由 witness 的 A1--A10 检查；7 是把
$w=X+iy$、$\bar w=X-iy$ 代入。

**状态**：`PROVED`（显式计算）+ `COMPUTATIONALLY VERIFIED EXAMPLE`。

**几何读法**。$(w,\bar w)$ 是 $\mathbb P^1\times\mathbb P^1$ 上的两个独立点，
$w=\bar w$ 是对角线（理想边界），$w\bar w=0$ 是坐标轴（$q$-公式/单位梯度的
极除子）。$a$ 是 $(w,\bar w,0,\infty)$ 的交叉比型坐标；在实形式下它退化为
$a=-(\mu/\lambda)X/y$。$\operatorname{PGL}_2(\mathbb C)$ 对角作用保持 $g$。

### 4.3 $q$-正规化的极除子与零轨迹

$q^2=0$ 的轨迹是 $w\bar w=0$，即 $w=0$ 或 $\bar w=0$。在实形式下
$w\bar w=|w|^2=0$ 只发生在 $w=0$，而 $w=0$ 在对角线上（$y=0$），
不在 $\mathbb H^2$ 内。所以**实模型没有 $q$-正规化的极除子，复模型有两个**。

在正则轨迹 $M$ 内，按定义 $q\ne0$，于是 $(\nabla a)^2=q^2\ne0$，故
$\nabla a\ne0$：水平集与零除子都是光滑的，这一点与实理论相同。

复化特有的新现象出现在被排除的除子 $q=0$ 上（若考虑奇异延拓）：此处
$\nabla a$ 可以非零但是**迷向的**（null）。在 $w=0$ 处
$\partial_{\bar w}a=0$、$\partial_w a\ne0$，故 $(\nabla a)^2=0$ 而
$\nabla a\ne0$。于是水平集在 $q=0$ 处是特征的（characteristic）。**注意**：零除子本身在 $\nabla a=0$ 处才奇异；$q=0$ 且
$\nabla a\ne0$ 时零除子仍可以是光滑复曲线，只是法向迷向。若要把正则理论
延拓过 $q=0$（奇异 AES），这种"非零但迷向的梯度"是实理论里不可能出现的新
现象：$\mathbb R$ 上 $q^2>0$ 保证 $\nabla a\ne0$ 且非迷向；$\mathbb C$ 上
"$\nabla a\ne0$"与"$q\ne0$"是两件事。

**推论 4.4**。为了做分析（水平集非特征、$E_a$ 有定义），全纯 AES 的正则定义
**应**要求 $q\ne0$（即 $q^2$ 是单位）；仅要求 $\nabla a\ne0$ 不够，因为
$q=0$ 处可以 $\nabla a\ne0$ 但迷向。框架本身可以在 $q=0$ 处继续存在
（命题 3.3(3)），所以"框架存在"与"正则"是两个不同的条件。这是 C1 与 Paper 0
定义的关键差异，应在正式论文里明确指出。

### 4.4 全纯 $\Rightarrow$ 调和（代数版本）

C1 的定理就是 §3.2 的定理取 $K=\mathbb C$、$A=\mathcal O(M)$。特别地：

- $4\bar\partial^T\bar\partial=-\Delta$；若 $\bar\partial F=0$，则 $\Delta F=0$；
- 这里 $\bar\partial^T$ 是由恒等式定义的代数算子，不是 $L^2$ 伴随；所以定理
  不需要测度、不需要共轭、不需要正性；
- 实理论中的 `thm:surface-holomorphic-implies-harmonic` 因此有一条**纯代数的
  证明路线**，它与原来的形式伴随证明并列，且更适合推广到 $K$。

**状态**：`PROVED`（同 §3.2）。

### 4.5 复长度与三分的塌缩

**命题 4.5**。设 $M\in\operatorname{PGL}_2(\mathbb C)$，提升
$\widetilde M$ 的特征值为 $\lambda_1,\lambda_2$，令 $\kappa=\lambda_1/\lambda_2$。
则：

1. 非恒等 $M$ 在 $\mathbb P^1(\mathbb C)$ 上总有两个不动点（计重数）；只有
   **分裂**（$\kappa\ne1$）与**抛物**（$\kappa=1$）两类，"非分裂"不存在。
2. 复长度
   $$
   \ell=\log\kappa\pmod{2\pi i,\ \kappa\leftrightarrow\kappa^{-1}},
   \qquad
   \frac{\tau}{2}=\cosh\frac{\ell}{2},
   \qquad
   \ell=2\operatorname{arccosh}\frac{\tau}{2}.
   $$
   $|\operatorname{Re}\ell|$（取 $\operatorname{Re}\ell\ge0$ 的分支）是 $M$
   在 $\mathbb H^3$ 上的平移长度，$\operatorname{Im}\ell$ 是绕轴的旋转角。
3. 实三分是 $\operatorname{Gal}(\mathbb C/\mathbb R)$ 对不动点对的作用：
   两个实不动点 = 双曲/分裂；一个实重不动点 = 抛物；共轭对 = 相对实结构的
   椭圆（即实形式的非分裂类）。所以相对实结构的"椭圆"不是 $\mathbb C$ 上的
   开类，而是 $|\kappa|=1$（即 $\operatorname{Re}\ell=0$）的余维一轨迹。

**状态**：`STANDARD CONSEQUENCE`（1、2 是标准双曲几何；3 是 Galois 读法，
`STRUCTURAL PROPOSAL` 的强度）。witness D2--D3 检查了
$\tau/2=\cosh(\ell/2)$ 与 $\ell=2\operatorname{arccosh}(\tau/2)$。

**注意**：复长度是 $M$ 作为 $\mathbb H^3$ 等距变换的长度，**不是**复化
$\mathbb H^2$（复曲面）上的长度。不要把 C1 的复化模型与 $\mathbb H^3$ 混为一谈。

### 4.6 边界：Cauchy/Poisson，Riemann--Hilbert，DtN = Hilbert

**命题 4.6**。在基本模型上：

1. Poisson 核是 Cauchy 核的跳跃：
   $$
   P_y(X-t)=\frac1\pi\frac{y}{(X-t)^2+y^2}
   =\frac{1}{2\pi i}\left(\frac{1}{t-w}-\frac{1}{t-\bar w}\right),
   \qquad w=X+iy .
   $$
2. 对 $f\in C_0(\mathbb R)\cap L^1(\mathbb R)$（或 Schwartz），Schwarz 积分
   $$
   F(w)=\frac{1}{\pi i}\int_{\mathbb R}\frac{f(t)}{t-w}\,dt
   $$
   在 $\mathbb H^2$ 内全纯，$\operatorname{Re}F$ 是 $f$ 的 Poisson 积分，
   $\operatorname{Im}F$ 是共轭调和函数，边界值为 $f+iHf$（$H$ 为 Hilbert
   变换；符号依 $H$ 的约定），且 $F(\infty)=0$。
3. Dirichlet-to-Neumann 映射是 Hilbert 变换与切向导数的复合：
   $$
   \mathcal N=|D_X|=H_XD_X=D_XH_X,
   $$
   在 $x$ 坐标中 $\mathcal N=|D_x|=(\lambda/\mu)|D_X|$。
4. 能量恒等式仍是 $H^{1/2}$ 二次型（相差一个常数因子）：
   $$
   \int_{\mathbb R}|k|\,|\hat f(k)|^2\,dk
   =\int_{\mathbb H^2}|\nabla U|^2\,dX\,dy,
   \qquad U=\operatorname{Re}F .
   $$

**状态**：1 是初等恒等式（witness D1）；2--4 是标准复分析/调和分析，
需要把函数类与 $\infty$ 处行为写清楚。**注意**：对一般的 $f\in C_0$ 但不
$L^1$，Schwarz 积分在 $\infty$ 处不一定趋于 $0$；Paper II 的实 Poisson 定理
（`thm:C0-poisson-dirichlet`）比全纯版本更强。正式论文里必须把类写成
$C_0\cap L^1$ 或 Schwartz，或者把 $\infty$ 处的条件单独陈述。

**读法**：C1 把 Paper II 的"C0 Dirichlet 定理"换成了
"Riemann--Hilbert/Schwarz 问题"；把 $|D|$ 换成了 Hilbert 变换 $H$；
把极大值原理换成了 Schwarz 反射/Liouville。这不是"更强的定理"，而是
**同一个边界算子的复分析读法**。

### 4.7 C1 里什么失败了

- 正性：$q^2$ 可以非实、可正可负；在奇异延拓中还可以为零；没有 $q>0$；
- 极大值原理：没有序，没有"有界 $\Rightarrow$ 唯一"；
- $L^2$：没有实测度；$\int F\bar G$ 需要共轭；
- 谱：没有自伴算子，只有 D-模/全纯族；
- $C_0$ 唯一性类：需要重新陈述（见 4.6 的注意）；
- Poisson 核：正性与总质量 $1$ 只在 Cauchy 核的**跳跃**（实结构）中出现；
  单独的 Cauchy 核不是正核；
- 实三分与实长度：只剩 split/parabolic 与复长度；
- 曲率符号：$K$ 是复函数，没有"负曲率"的比较几何；
- 完备性/理想边界：复化模型的"边界"是对角线，不是实理想边界；
- "非分裂"类：$\mathbb C$ 上不存在。

保留下来的是：框架、eikonal、括号、Laplace、因子分解、全纯 $\Rightarrow$ 调和、
曲率公式、拉回、Cauchy/Riemann--Hilbert/Hilbert。

### 4.8 接触分支的复化

把 $\mathcal C=\mathbb C^3_{(u,v,a)}$、$\alpha=da-\mu\,du-\lambda a\,dv$、
$D_u=\partial_u+\mu\partial_a$、$D_v=\partial_v+\lambda a\partial_a$ 复化。
则：

- $\alpha\wedge d\alpha=-\mu\lambda\,du\wedge dv\wedge da$（非零，若 $\mu\lambda\ne0$），
  复接触结构成立；
- $[D_u,D_v]=\mu\lambda\partial_a$，非整分性保持；
- CR 算子 $\bar L=\tfrac12(D_u+iD_v)$ 的因子分解
  $4L\bar L=Q_{\mathcal C}+i\mu\lambda\partial_a$ 是代数恒等式；
- 首次积分
  $$
  z=u+iv,\qquad
  \zeta=u+\frac{i}{\lambda}\operatorname{Log}(\mu+i\lambda a)
  $$
  在复化后是多值的：环绕 $a=i\mu/\lambda$ 的闭路使
  $\zeta\mapsto\zeta-2\pi/\lambda$，故
  $e^{\rho z+\sigma\zeta}$ 单值 $\iff\sigma\in i\lambda\mathbb Z$。
  这是复化带来的"量子化"现象；在实理论里 $\mu+i\lambda a$ 永不为零，
  不会出现。
- Friedrichs/Hörmander/$L^2$ 属于 C2/实层，不在 C1。

**状态**：因子分解与括号 `PROVED`；多值性与格点的观察是
`COMPUTATIONALLY/ELEMENTARILY VERIFIED`（直接计算），但"单值化格点"是否应成为
正式定义的一部分是 `OPEN`。

---

## 5. C2：Hermitian 复化与 no-go

### 5.1 未 Hermitian 化的 eikonal 只有常值解

**命题 5.1（no-go）**。设 $M$ 是连通复曲线，$g$ 是 Hermitian 正定度量，
$a:M\to\mathbb C$ 全纯，$\mu,\lambda\in\mathbb R$，$\mu\ne0$，$\lambda\ne0$。
若未 Hermitian 化的 eikonal
$$
|\nabla a|_g^2=\mu^2+\lambda^2a^2
$$
成立（左边是 Hermitian 范数平方，实 $\ge0$），则 $a$ 是常数。

**证明**。左边实 $\ge0$，故右边实 $\ge0$；$\mu^2$ 实，故 $\lambda^2a^2$ 实，
即 $a^2$ 实值。于是 $a(M)\subset\mathbb R\cup i\mathbb R$。$a$ 全纯且 $M$ 连通，
开映射定理迫使 $a$ 为常数。$\square$

**状态**：`PROVED`（初等）。**例外**：$\lambda=0$ 时方程是 $|\nabla a|^2=\mu^2$，
有非平凡全纯解（例如 $\mathbb C$ 上 $a=\mu z$，或 $\mathbb C^\times$ 上
$a=\mu\log z$ 配上适当的度量），所以 no-go 的 $\lambda\ne0$ 假设不可省。

**意义**：这条 no-go 说明"把 $a$ 复化、度量仍 Hermitian"不是 Paper II 的
复化；它只会得到常值。要保留函数论，必须 Hermitian 化 eikonal（5.2），
或走 C1（放弃正性）。这也从另一个角度解释了双赋值为什么要区分
$b=a$ 与 $b=\bar a$。

### 5.2 Hermitian 化 eikonal

**定义 5.2（Hermitian AES）**。设 $M$ 是复曲线，$g=e^{2\rho}|dz|^2$ 是
Hermitian 度量，$a\in\mathcal O(M)$，满足
$$
|\nabla a|_g^2=\mu^2+\lambda^2|a|^2 .
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
**状态**：`DEFINITION/PROPOSAL`。这不是 Paper II 的 eikonal，而是一个新的
Hermitian 理论；它的"相位"$\arg a$ 是新的自由度，它的"模长"进入 eikonal。
它是否与双赋值的 $I_H=1+|a|^2$ 一致，取决于归一化；这是 `OPEN`。

**例 5.3**。$M=\mathbb C$，$a=e^z$。则
$|a'|^2=|a|^2$，
$\rho=\tfrac12\log(|a|^2/(\mu^2+\lambda^2|a|^2))$，
度量 $g=e^{2\rho}|dz|^2$ 是 Hermitian 正定的；$a$ 全纯、非平凡。
**状态**：`COMPUTATIONALLY VERIFIED EXAMPLE`（可直接代入验证；
正式论文应补完备性/曲率的讨论）。

### 5.3 C2 保留了什么

- 正性、测度、$L^2$、Friedrichs 实现；
- 谱理论（在度量完备/有界几何等额外假设下）；
- 极大值原理（对 $\operatorname{Re}F$、$\operatorname{Im}F$ 的实调和性）；
- Poisson 核（若度量是双曲型的）；
- 但 eikonal 已 Hermitian 化，三分只剩相对实结构才有意义。

### 5.4 C2 的开放问题

1. Hermitian AES 的局部/整体存在性、唯一性、完备性；
2. 度量由 $a$ 反解后，曲率与 $a$ 的关系；
3. $\arg a$ 作为"相位连接"的几何意义；
4. Hermitian AES 的 Poisson/Dirichlet 理论；
5. 与双赋值 Hermitian 入射 $I_H=1+|a|^2$ 的精确对应；
6. Hermitian AES 的"全纯 $\Rightarrow$ 调和"是否仍由某个因子分解给出。

---

## 6. 与 pcrg-paper 任意域理论的接口

### 6.1 同一分层的两次发现

`bivaluation-02` 明确写：
$$
\text{任意域代数骨架}
\longrightarrow
\text{复射影版本}
\longrightarrow
\text{Hermitian/概率版本}.
$$
本文的分层是：
$$
\text{Layer A（任意域）}
\longrightarrow
\text{C1（复代数化）}
\longrightarrow
\text{C2（Hermitian/正性）}.
$$
两者是同一件事：C1 不带共轭，C2 带共轭与正性。`bivaluation-02` §25 特意强调
$\mathrm{alg}$ 上标："这只是代数复化，还没有引入 Hermitian 内积、共轭或概率
解释"——这正是 C1 与 C2 的分界。

### 6.2 capacity / trichotomy / torsor

- **capacity**（09）：容量 = 载体维数，冗余 = $q+1$；这是 Layer A 的"信息容量"
  陈述，不是分析。
- **trichotomy**（10）：$\operatorname{tr}^2-4\det$ 的三分在 $\mathbb R$ 上是
  初等的，在 $\mathbb F_q$ 上由 Legendre 承载；变的是不变量类型（连续长度
  $\to$ 除数）。这与本文 §3.5 完全一致。
- **torsor**（09）：$\ell=0$ 是 torsor 层；抛物共轭类不带连续不变量，
  全部内容交给选择。这与本文 §3.5 的"长度只在分裂层有定义"一致。
- **no attraction**（2026-06-17 有限域笔记）：有限域上轨道周期化，
  "不动点存在"$\ne$"吸引不动点存在"。这是 Layer A 的"动力学"读法，
  不是 Layer C 的"收敛"。

### 6.3 failure atlas vs 解析奇点

`pcrg-paper` 的 failure atlas 分层（chart escape、nonsplit 不可见极点、
no-condensation-as-limit、incidence divisor 退化）是 **Layer A 的失败图册**：
它们是"没有足够结构（拓扑/范数/序）时的代数/射影现象"。

Paper III 的解析奇点是 **Layer C 的失败图册**：critical point、branch point、
puncture、非 proper 的零轨迹。

两者不应混淆：
- chart escape 不是解析奇点，换图就消失；
- nonsplit 不可见极点不是"无极点"，是"极点在扩域中"；
- no-attraction 不是"不收敛"，是"没有拓扑/度量可谈收敛"。

### 6.4 不应混淆的术语

| 左 | 右 | 区别 |
|---|---|---|
| $b$（代数对偶余赋值） | $\bar a$（Hermitian 共轭） | 代数 vs 反全纯 |
| C1（无共轭） | C2（有共轭） | 复代数化 vs Hermitian |
| $q$-正规化的极除子 $q=0$ | 解析奇点 | 单位梯度失效 vs 函数/轨迹奇异 |
| chart escape | 无对象 | 换图 vs 真缺失 |
| 长度 $\ell$ | 乘子 $\kappa$ | 需要序/赋值 vs 代数不变量 |
| 复化 $\mathbb H^2$ | $\mathbb H^3$ | 复曲面 vs 双曲三维空间 |
| 抛物层 torsor | 空层 | 选择就是内容 vs 没有内容 |

### 6.5 赋值域与树：p-adic 方向

任意域没有分析；但**赋值域**有。对非阿基米德（non-Archimedean）局部域 $K$
（例如 $\mathbb Q_p$、$\mathbb F_q((t))$），$\operatorname{PGL}_2(K)$ 作用在
$(q+1)$-正则的 Bruhat--Tits 树 $T$ 上，边界是 $\mathbb P^1(K)$。这是
$\mathbb H^2$ 的非阿基米德对应物：

- 树上的调和函数、Poisson 核、Poisson 变换是标准理论（Cartier；
  Figà-Talamanca--Nebbia）；
- 球函数是 Hecke 算子的特征函数，特征值 $q^s+q^{1-s}$；
- "DtN" 的对应物是 Hecke/Taibleson 算子，符号是 $|\xi|_K^s$。

AES 的翻译：赋值 $a$ 应是树上的函数，eikonal 应是离散梯度关系（例如
$a=\sinh(\lambda s)$，$s$ 为到某顶点的距离）；这是 `STRUCTURAL PROPOSAL`，
不是定理。外部 p-adic 分析是标准的，AEG 的翻译尚未证明。**不要**把树的
Poisson 理论直接称为 AEG 定理。

从更远看，阿基米德与非阿基米德两种局部域可以在 adele 环上统一
（Tate 的框架）；这对 AEG 是一个开放的结构性方向，不是本文的结论。

---

## 7. 与 Paper III 的接口：复化后的零轨迹

Paper II 的零轨迹在实理论里是 $1$ 维曲线；在 C1 里它是复曲线/除子。
这带来三个新对象：

1. **零除子** $Z(a)=\{a=0\}$ 是复曲线。在正则轨迹 $M$ 内 $q\ne0$，故
   $\nabla a\ne0$，零除子光滑；它的奇点（若把理论延拓到奇异轨迹）来自
   $\nabla a=0$（$a$ 的临界点）。$q=0$（迷向梯度）不是正则零除子的奇点，
   而是延拓边界上的特征点；此时零除子仍可以是光滑复曲线，只是法向迷向。
   这是复化特有的现象，在实理论里不存在。
2. **临界值/奇异纤维**：$a$ 作为全纯函数，其临界值处的纤维是奇异的；
   局部理论是 Milnor 纤维化、消失圈、单值群。这是 Paper III 的
   "branched pullback / 零网络 / tube" 的复分析对应物。
3. **Picard--Lefschetz 方向**：族 $a_t=a-t$ 的消失圈与 braid 单值，
   是 Paper III 的"tube topology / braid" 的复化候选。**状态**：
   `STRUCTURAL PROPOSAL` / `OPEN`；不要在正式论文里直接声称。

**一个具体的连接**：Paper III 的 `q=4` Hecke--Hauptmodul 构造本身就是复代数/
复解析的；Paper II 的 C1 层正好补上它的"正则复分析"半边。这不是新理论，
而是把 Paper II 的实分析接口换成复分析接口。

---

## 8. 建议的论文架构与工作包

### 8.1 四种选项

**选项 A：原地扩充 Paper II**。加两节"Complexification"与"Arbitrary-field
algebraic core"。优点：函数论集中。缺点：Paper II 的标题、scope、
claim boundary 都是"Hyperbolic Real Function Theory"；任意域部分没有分析，
放进函数论论文会失衡；需要改 scope。**不推荐作为第一步。**

**选项 B：新论文（Paper VII）**。标题候选：
*Arithmetic Expression Geometry VII: Complexification and Arbitrary-Field
Arithmetic Expression Spaces*，副标题 *Holomorphic Function Theory, Algebraic
Skeletons, and the Bivaluation Interface*。优点：scope 干净；可以同时承接
Paper II 的实理论、Paper III 的复奇点、pcrg 的双赋值；可以把三层讲清楚。
缺点：需要 `governance/00f` scope 文件与新目录；系列已到 Paper VI（共 7 篇）。

**选项 C：Paper II, Part II**。作为 Paper II 的续篇，共享引言。优点：
治理扰动小；明确是续作。缺点："Paper II"变成两部；读者需要同时读两部。

**选项 D：先写笔记**。本笔记 + 一个复化基本模型的计算笔记 + 一个双赋值字典
笔记；成熟后再决定 B 或 C。**推荐作为现在这一步**，与仓库"notes 先行"的
文化一致。

### 8.2 推荐

短期：选项 D。把本笔记作为设计文档；补两个计算笔记：
(a) 复化基本模型的完整计算与 Riemann--Hilbert 边界理论；
(b) 双赋值字典的逐条验证（含有限域）。
**进展**：(a) 已写成 [51 — 复化基本模型与 Riemann–Hilbert 边界](51-complexified-model-and-rh.md)，
包含 C1 模型、RH 边界与 C2 Hermitian 伴随模型；WP1/WP4 已落地，WP5 推进。
(b) 仍待写。
中期：选项 B（新论文），因为"任意域"与"复化"都不是 Paper II 的标题所能容纳的，
而且它们与 Paper III 的复奇点有实质接口。若作者更看重连续性，选 C。

### 8.3 工作包

| 包 | 内容 | 状态目标 |
|---|---|---|
| WP1 | 全纯 AES 定义、正则轨迹、复化基本模型、$q$-正规化的极除子 | `PROVED`（note 51） |
| WP2 | 代数 AES 定义、定理 3.2、框架存在性/唯一性 | `PROVED WITH STATED HYPOTHESES` |
| WP3 | 任意域三分、长度类型表、双赋值字典 | `STANDARD` + `PROPOSAL` |
| WP4 | C1 边界：Cauchy/Poisson、Riemann--Hilbert、DtN=Hilbert | `STANDARD CONSEQUENCE`（note 51，需写类） |
| WP5 | C2：no-go、Hermitian eikonal、例、L²/谱问题 | `PROVED`（no-go + C2 基本模型，note 51）+ `OPEN`（谱/边界） |
| WP6 | 局部域/树：Bruhat--Tits、Poisson、Hecke/Taibleson | `STRUCTURAL PROPOSAL`（外部标准结果待导入） |
| WP7 | 复奇点接口：零除子、临界值、Picard--Lefschetz | `OPEN` |
| WP8 | 有限域验证套件（witness C）与有限 Fourier/特征标 | `COMPUTATIONALLY VERIFIED` |

### 8.4 风险与非声明

必须避免的说法：

- "在任意域上做分析"——只有代数骨架；分析需要赋值/拓扑/实结构。
- "复化就是 Paper II 的 C0 定理的推广"——C1 的边界问题是
  Riemann--Hilbert，不是同一个唯一性类。
- "复化 $\mathbb H^2$ 就是 $\mathbb H^3$"——前者是复曲面，后者是双曲三维空间；
  复长度属于后者。
- "框架在任意域上规范"——只在给定 $J$ 后规范；$q$ 只是局部表达式，框架本身
  可以不需要 $q$（命题 3.3）。
- "p-adic 树上的 Poisson 理论是 AEG 定理"——它是标准外部理论，AEG 的翻译
  尚未证明。
- "有限域上的 failure atlas 就是 Paper III 的奇点"——前者是代数/射影现象，
  后者是解析现象。
- "Hermitian eikonal 就是 Paper II 的 eikonal"——它是另一个 eikonal；未
  Hermitian 化的版本只有常值解（命题 5.1）。

---

## 9. 结论

Paper II 的真正内容是三层，而不是一个关于 $\mathbb R$ 的定理集合：

- **Layer A** 是可以在任意特征 $\ne2$、含 $i$ 的域上写下的代数骨架；
  它的核心恒等式 $4\bar\partial^T\bar\partial=-\Delta$ 不需要测度、共轭或正性。
  这一层与 `pcrg-paper` 的双赋值理论是同一件事的两次发现。
- **Layer B** 是复分析中层，有两条路：C1（全纯、Cauchy/Riemann--Hilbert、
  Hilbert 变换）与 C2（Hermitian、$L^2$/谱）。C1 是字面的域扩张，C2 是
  保留正性的 Hermitian 版本；未 Hermitian 化的 C2 eikonal 只有常值解。
- **Layer C** 是实分析顶层：序、正性、极大值原理、完备性、理想边界、
  谱、实三分与实长度。Paper II 现在住在这里，而它的许多"框架性"结论
  其实属于 Layer A。

所以"Paper II 的复域扩充"最准确的表述是：

> **把 Paper II 的三层显式化：在任意域上认领代数骨架，在 $\mathbb C$ 上发展
> C1 的全纯边界理论，在 Hermitian 结构上发展 C2 的 $L^2$/谱理论，并把 Paper II
> 的实理论作为 C1 的一个实形式保留下来（它同时给 C2 提供正性/共轭结构）。**

下一步最值得做的三件事：

1. 把定理 3.2 写成正式论文的"代数 Paper II"，并在 Paper II 的证明旁边加一条
   纯代数证明路线（不改变原定理的状态）。
2. ~~把复化基本模型与 Riemann--Hilbert 边界理论写成计算笔记~~ **已完成**：
   [note 51](51-complexified-model-and-rh.md) 确认了 $|D|=HD$、$H^{1/2}$ 能量、
   $C_0\cap L^1$ 类，并给出 C2 的完备基本模型。
3. 把双赋值字典写成逐条验证的笔记（含有限域），决定它是否足以支撑
   "任意域 AES"的正式定义。

---

## 附录 A：witness 脚本输出（节选）

运行
```
python3 50-complex-arbitrary-field-witness.py
```
全部通过。摘录：

```
A. Complexified basic model over C
  PASS  A1  (grad a)^2 = mu^2 + lambda^2 a^2  (complex bilinear)
  PASS  A2  Delta_g a = 2 lambda^2 a
  PASS  A3  [X_u, X_v] = lambda X_u
  PASS  A4  Delta_g = X_u^2 + X_v^2 + lambda X_v
  PASS  A7  mu^2 + lambda^2 a^2 = -4 mu^2 w wbar/(w-wbar)^2
  PASS  A10 (X_u + i X_v)/2 = -lambda y d_wbar
B. Algebraic Paper II identity (Weyl algebra, no conjugation)
  PASS  B1  4 dbar^T dbar = -Delta (central structure functions)
  PASS  B2  concrete frame: 4 dbar^T dbar = -Delta
C. Finite-field trichotomy for PGL_2(F_q)
  PASS  C q= 3: |PGL_2|=   24  split=   6 parabolic=  9 nonsplit=   9  mismatches=0
  PASS  C q= 5: |PGL_2|=  120  split=  45 parabolic= 25 nonsplit=  50  mismatches=0
  PASS  C q= 7: |PGL_2|=  336  split= 140 parabolic= 49 nonsplit= 147  mismatches=0
  PASS  C q=11: |PGL_2|= 1320  split= 594 parabolic=121 nonsplit= 605  mismatches=0
  PASS  C q=13: |PGL_2|= 2184  split=1001 parabolic=169 nonsplit=1014  mismatches=0
D. Cauchy/Poisson and complex length
  PASS  D1  Poisson kernel = Cauchy jump
```

有限域的"$-1$ 是平方 $\iff q\equiv1\pmod4$"也逐项打印：$q=5,13$ 为真，
$q=3,7,11$ 为假。

## 附录 B：与 Paper II 标签的对应

| 本文 | Paper II 标签 |
|---|---|
| §2.1 框架/约束 | `prop:canonical-arithmetic-frame`、eq. `eq:surface-structure-assignment-constraint` |
| §2.1 Laplace | `prop:surface-frame-laplacian` |
| §2.1 raw/exact 分解 | `prop:surface-raw-factorization`、`prop:surface-exact-drift-factorizations` |
| §2.1/§4.4 伴随因子分解 | `thm:surface-adjoint-factorization` |
| §2.1/§4.4 全纯 $\Rightarrow$ 调和 | `thm:surface-holomorphic-implies-harmonic` |
| §2.4 平面基/曲率 | `prop:planar-harmonic-aes` |
| §2.4 全纯拉回 | `thm:planar-holomorphic-pullback` |
| §2.4 柱面/自守 | `prop:cylindrical-aes`、`prop:cylinder-automorphic-descent` |
| §4.2 基本模型 | `prop:hyperbolic-analytic-normalization` |
| §4.6 Poisson/Dirichlet | `lem:poisson-kernel-transport`、`thm:C0-poisson-dirichlet` |
| §4.8 接触 | `prop:contact-raw-cr-factorization`、`prop:contact-adjoint-cr-factorization`、`prop:contact-logarithmic-first-integrals` |
| §3.5 实三分 | `prop:p0-projective-trichotomy`（Paper 0） |
