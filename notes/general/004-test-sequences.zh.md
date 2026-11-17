# 试验场序列选型与金属均值统一视角：Pell / Fibonacci / Sylvester / Recamán

> **文档性质**：算术表达式几何（AEG）研究笔记（之三：HTWR 核的试验场序列选型、结构对照与状态标注）
> **前置依赖**：笔记一《双曲热带波前-残差核（HTWR Core）》（[001-htwr-core.md](001-htwr-core.md)）、笔记二《精确时空帕累托边界》（[002-htwr-example.md](002-htwr-example.md)）及其编译版（[003-htwr-core.tex](003-htwr-core.tex)）
> **日期**：2026-11-13
> **备注**：本笔记整理 Pell、Fibonacci、Sylvester、Recamán 四个候选试验场在 HTWR 核下的定位，把 Pell 与 Fibonacci 统一到金属均值族；所有恒等式均为独立数值验证（见文内标注），HTWR 量级分析按笔记公理 I–IV 做结构平移并明确状态。

---

## 一、目的与范围

本笔记承接笔记一"核心几何推论与后续研究靶点"一节（[001-htwr-core.md](001-htwr-core.md) 第 121 行、[003-htwr-core.tex](003-htwr-core.tex) 第 504 行）提出的任务：

> 选取典型测试序列（如 $2^N-1$、Fibonacci 有理逼近序列或 Sylvester 数列），精确算出第一条非平凡的 $(\mathcal A,\Sigma)$ 帕累托曲线。

这里对候选序列做一次**结构定位**：哪些序列落入 Pell 的"二次无理数收敛子"谱系（其 HTWR 分析可整体平移），哪些落入别的谱系，哪些根本不承载可用的代数结构。$2^N-1$ 仅做标记，留待后续。本笔记**不修改**公理 I–IV，也不重述它们的证明；只做结构对照、恒等式验证与状态标注。

---

## 二、状态标签约定

本笔记遵循 [governance/05-mathematical-status.md](../../governance/05-mathematical-status.md) 的权威标签：

- `PROVED` / `PROVED WITH STATED HYPOTHESES`
- `STANDARD CONSEQUENCE REQUIRING AN IN-PAPER PROOF`
- `COMPUTATIONALLY VERIFIED EXAMPLE`
- `PARTIALLY PROVED`
- `STRUCTURAL PROPOSAL`
- `CONJECTURE` / `OPEN PROBLEM` / `UNSUPPORTED AND EXCLUDED`

一条原则（据 AGENTS.md）：HTWR 公理 I–IV 本身是**公理化提议**（`STRUCTURAL PROPOSAL`，见 [001-htwr-core.md](001-htwr-core.md) 标题与 [002-htwr-example.md](002-htwr-example.md) 备注），因此"在公理 I–IV 下证明的定理"是**条件性**结论——它们相对于公理成立，但不因此自动成为可发表的一般定理。本笔记对所有 HTWR 量级分析均标注 `STRUCTURAL PROPOSAL`，恒等式标注 `COMPUTATIONALLY VERIFIED EXAMPLE`（并注明哪些是经典标准事实）。

---

## 三、Pell 试验场（回顾摘要）

（完整推导见 [002-htwr-example.md](002-htwr-example.md)；此处仅列出作为对照锚点的要素。）

- **对象**：$(1+\sqrt2)^n=P_n+Q_n\sqrt2$，$x_n=P_n/Q_n\in\mathbb P^1(\mathbb Q)$，$x_n\to\sqrt2$。
  - $P_n=1,3,7,17,41,99,239,577,\dots$（伴 Pell / Pell–Lucas 半序列，OEIS A001333）
  - $Q_n=1,2,5,12,29,70,169,408,\dots$（**Pell 数**，OEIS A000129）
- **深度**：$I(x_n)=\ln P_n=n h_0-\ln2+o(1)$，$h_0=\ln(1+\sqrt2)\approx0.8814$。
- **三条结构要素**：
  1. **范数恒等式**：$P_k^2-2Q_k^2=(-1)^k$；
  2. **Newton 倍增**：$x_{2n}=\frac{x_n^2+2}{2x_n}$（对方程 $x^2-2=0$ 做 Newton 步）；
  3. **Möbius 大步（催化）**：$x_{n+k}=x_k+\dfrac{(-1)^{k+1}}{Q_k^2(x_n+x_k)}$（主变量 $x_n$ 只出现一次）。
- **结论**：定理 1（不确定性下界 $\mathcal A\ge\frac{\alpha(I_*-\ln2)^2}{2(\sigma_{\max}+\ln2)}$，对任意目标与 DAG）与定理 2（Pell 收敛子的双相帕累托边界）。

**状态**：范数恒等式与倍增恒等式为经典标准事实（`STANDARD CONSEQUENCE REQUIRING AN IN-PAPER PROOF`）；定理 1、2 在公理 I–IV 下证明（`STRUCTURAL PROPOSAL` 框架内的条件结论）。

---

## 四、Fibonacci：Pell 的同构孪生

### 4.1 对象与收敛子

取斐波那契数 $F_0=0,F_1=1,\ F_{n+1}=F_n+F_{n-1}$，记比值

$$
y_n:=\frac{F_{n+1}}{F_n}\in\mathbb P^1(\mathbb Q),\qquad y_n\to\varphi=\frac{1+\sqrt5}{2}=[1;\overline1].
$$

$y_n$ 是黄金比连分数 $[1;\overline1]$ 的收敛子：$1,\ 2,\ \frac32,\ \frac53,\ \frac85,\ \frac{13}{8},\ \frac{21}{13},\dots$，且**无需平移**地满足纯连分数不动点递推

$$
y_{n+1}=1+\frac1{y_n},
$$

因为 $\varphi=1+\frac1\varphi$。

### 4.2 与 Pell 的逐项结构对照

| 结构要素 | Pell（白银比，$m=2$） | Fibonacci（黄金比，$m=1$） |
| --- | --- | --- |
| 极限 / 比率 | $\sqrt2$，$\lambda=1+\sqrt2$ | $\varphi=\frac{1+\sqrt5}{2}$ |
| 单位群构造 | $(1+\sqrt2)^n=P_n+Q_n\sqrt2$ | $\varphi^n=\frac{L_n+F_n\sqrt5}{2}$（$L_n$ Lucas 数） |
| 收敛子 | $x_n=P_n/Q_n\to\sqrt2$ | $y_n=F_{n+1}/F_n\to\varphi$ |
| 连分数不动点 | $u_{n+1}=2+\frac1{u_n}$ | $y_{n+1}=1+\frac1{y_n}$ |
| 范数/单位恒等式 | $P_k^2-2Q_k^2=(-1)^k$ | **Cassini**：$F_{n+1}F_{n-1}-F_n^2=(-1)^n$ |
| 缺陷催化剂 | $c_k=2-x_k^2=\frac{(-1)^{k+1}}{Q_k^2}$ | $d_k=y_k^2-y_k-1=\frac{(-1)^k}{F_k^2}$ |
| Newton 倍增 | $x_{2n}=\frac{x_n^2+2}{2x_n}$（对 $x^2-2=0$） | $y_{2n}=\frac{y_n^2+1}{2y_n-1}$（对 $y^2-y-1=0$） |
| Möbius 大步 | $x_{n+k}=x_k+\frac{(-1)^{k+1}}{Q_k^2(x_n+x_k)}$ | $y_{n+k}=y_k+\frac{(-1)^{k+1}}{F_k(F_k y_n+F_{k-1})}$ |
| 单步深度增量 | $h_0=\ln(1+\sqrt2)\approx0.8814$ | $h_0=\ln\varphi\approx0.4812$ |

### 4.3 三条恒等式（数值验证）

以下恒等式对本笔记 $n,k\le 10$ 逐项验证成立：

1. **Cassini 恒等式**：$F_{n+1}F_{n-1}-F_n^2=(-1)^n$（$n=2,\dots,11$ 全部 OK）。等价地，Lucas 版 $L_n^2-5F_n^2=4(-1)^n$（$L_n=F_{n-1}+F_{n+1}$）。
2. **Newton 倍增**：$y_{2n}=\frac{y_n^2+1}{2y_n-1}$。这是对方程 $f(y)=y^2-y-1=0$（$\varphi$ 的极小多项式）做 Newton 步：$y-\frac{f(y)}{f'(y)}=\frac{y^2+1}{2y-1}$。与 Pell 的 $x_{2n}=\frac{x^2+2}{2x}$（对 $x^2-2=0$）完全对应。
3. **Möbius 大步（催化）**：由斐波那契矩阵 $M^k=\begin{pmatrix}F_{k+1}&F_k\\F_k&F_{k-1}\end{pmatrix}$（$\det M^k=(-1)^k$）作用于 $y_n$ 得
$$
y_{n+k}=\frac{F_{k+1}y_n+F_k}{F_k y_n+F_{k-1}}=y_k+\frac{(-1)^{k+1}}{F_k(F_k y_n+F_{k-1})}.
$$
**关键**：$y_n$ 在该表达式中**只出现一次**（Möbius 形式），这正是 Pell 催化虫洞"主导线零扇出"的斐波那契版。

**状态**：三条恒等式为经典标准事实（Cassini、Newton 迭代、斐波那契矩阵幂），本笔记数值验证有限项——`COMPUTATIONALLY VERIFIED EXAMPLE`，可升格为 `STANDARD CONSEQUENCE REQUIRING AN IN-PAPER PROOF`。

### 4.4 HTWR 平移（结构观察）

**深度标定**：$\gcd(F_n,F_{n+1})=1$ 且 $F_{n+1}>F_n$，故 $I(y_n)=\ln F_{n+1}=(n+1)\ln\varphi-\ln\sqrt5+o(1)$。目标态 $y_N$ 的固有深度 $I_*=I(y_N)=N\ln\varphi+O(1)$。

在此模型下，Pell 的三条结论**逐字平移**，只把 $h_0=\ln(1+\sqrt2)$ 换成 $h_0=\ln\varphi$：

1. **零亏格测地流**（$g=0$）：$y_{n+1}=1+\frac1{y_n}$ 单导线串行推进，$\mathcal A_{\mathrm{CF}}(y_N)=\Theta\bigl(\frac{I_*^2}{h_0}\bigr)=\Theta\bigl(\frac{I_*^2}{\ln\varphi}\bigr)$。
2. **催化虫洞**（$g\ge1$）：常驻催化剂 $(y_k,d_k)$，$d_k=y_k^2-y_k-1=(-1)^k/F_k^2$（深度 $2\ln F_k\approx2s$），每轮大步消耗 $\Theta(\alpha I_*)$ 级横向通量，累计 $\mathcal A_{\mathrm{BSGS}}(\sigma_{\max})=\Theta\bigl(\frac{\alpha I_*^2}{\sigma_{\max}}\bigr)$。
3. **帕累托边界**：$0\le\sigma_{\max}<\frac12I_*$ 反比权衡相、$\sigma_{\max}\ge\frac12I_*$ Heron 线性饱和相的结构不变，仅 $h_0$ 改变。

**平移为何严格**：定理 1 对**任意**目标态与 DAG 成立，不依赖 Pell；定理 2 的证明只用三要素——深度线性增长、范数恒等式（提供约分虫洞）、Möbius 大步（主变量单次出现）——Fibonacci 三者俱全。

**状态**：`STRUCTURAL PROPOSAL`（定理 2 的完整书面平移尚未写出；定理 1 直接适用）。

---

## 五、金属均值统一族

两者是同一族的前两个成员。金属均值（metallic means）

$$
\sigma_m=[m;\overline m]=\frac{m+\sqrt{m^2+4}}{2},\qquad \sigma_m=m+\frac1{\sigma_m},\qquad \sigma_m^2-m\sigma_m-1=0.
$$

- $m=1$：$\sigma_1=\varphi=[1;\overline1]$（黄金比）→ Fibonacci；
- $m=2$：$\sigma_2=1+\sqrt2=[2;\overline2]$（白银比）→ Pell；
- $m=3$：$\sigma_3=(3+\sqrt{13})/2=[3;\overline3]$（青铜比）→ 待分析。

统一地，$\sigma_m^n=\frac{A_n+B_n\sqrt{m^2+4}}{2}$ 满足 Pell 型方程

$$
A_n^2-(m^2+4)\,B_n^2=4(-1)^n,
$$

且收敛子递推为 $u_{n+1}=m+\frac1{u_n}$、单步深度增量 $h_0=\ln\sigma_m$。

- $m=1$：$A_n=L_n,\ B_n=F_n$，得 $L_n^2-5F_n^2=4(-1)^n$；
- $m=2$：$A_n=2P_n,\ B_n=Q_n$，得 $P_n^2-2Q_n^2=(-1)^n$。

**状态**：金属均值及其 Pell 型方程为经典标准数论——`STANDARD CONSEQUENCE REQUIRING AN IN-PAPER PROOF`。$m\ge3$ 的 HTWR 帕累托边界尚未写出：`OPEN PROBLEM`（结构上预期同构，但需逐项核对大步 Möbius 分解与约分虫洞的系数）。

**量差记录**：$\ln\varphi\approx0.4812$ 约为 $\ln(1+\sqrt2)\approx0.8814$ 的 $54.6\%$；到同一目标深度 $I_*$，Fibonacci 需约 $1.83$ 倍步数，二次壁垒常数 $\propto1/h_0$ 更大。$\varphi$ 是金属均值中最小者（连分数全为 $1$），故 Fibonacci 是该收敛子族的"最慢"基准成员。

---

## 六、Sylvester 试验场（另一谱系）

（OEIS [A000058](https://oeis.org/A000058)，Sylvester 常数 [A076393](https://oeis.org/A076393)。）

### 6.1 定义与恒等式

$$
s(0)=2,\qquad s(n+1)=s(n)^2-s(n)+1=s(n)\bigl(s(n)-1\bigr)+1.
$$

前几项：$2,3,7,43,1807,3263443,10650056950807,113423713055421844361000443,\dots$（位数 $1,1,1,2,4,7,14,27,53$，每步翻倍）。

三条精确恒等式（本笔记逐项验证）：

1. **乘积 = 差**：$s(n)-1=\prod_{k=0}^{n-1}s(k)$；
2. **埃及分数**：$\sum_{k=0}^{n}\frac1{s(k)}=1-\frac1{s(n+1)-1}\to1$；
3. **两两互素**：$\gcd(s(i),s(j))=1\ (i\neq j)$。

增长：$s(n)=\lfloor E^{2^{n+1}}+\frac12\rfloor$，$E\approx1.2640847353053011$（$\ln E\approx0.23434833$）；$\ln s(n+1)/\ln s(n)\to2$。

### 6.2 HTWR 分析（结构观察）

深度 $L_n=I(s(n))=\ln s(n)$ 满足 $L_{n+1}=2L_n+O(1)$（**每步翻倍**）。用一次 $\Delta$ 扇出 + 一次 $\times$ 平方 + 线性修正，单步作用量 $\approx4\alpha L_n$，累计

$$
\mathcal A(s(N))\approx4\alpha\sum_{n=0}^{N-1}L_n=\Theta(\alpha L_N)=\Theta(\alpha I_*),
$$

即**线性于输出深度**——不存在二次壁垒。峰值横向通量出现在末步：$\sigma_{\max}\approx L_{N-1}=\frac12I_*+O(1)$。代入定理 1 得下界 $\Omega(\alpha I_*)$，与上界在常数内吻合：Sylvester 的朴素电路**自动**饱和不确定性原理于"全凝聚线性相"。

**与 Pell/Fibonacci 的本质差别**：Sylvester 两两互素，**没有范数恒等式，也没有约分虫洞**可资利用；深度靠"反复平方"翻倍，而非靠单位群结构。它在 HTWR 中的角色是检验"反复平方制造指数位宽"这条 BSS 免费午餐漏洞是否被按管径收费（公理 I.3 + II.3）堵住——模型内自洽（线性下界与线性可达重合）。

动力学注记：$f(s)=s^2-s+1$ 在 $s=1$ 处有抛物不动点（$f(1)=1,\ f'(1)=1$），$s(0)=2$ 的轨道即整个序列；它是真二次映射，不属于 $\mathrm{PSL}(2,\mathbb Z)$ 测地流。

**状态**：三条恒等式 `COMPUTATIONALLY VERIFIED EXAMPLE`（也是经典标准事实）；HTWR 量级分析 `STRUCTURAL PROPOSAL`。开放问题（`OPEN PROBLEM`）：该序列"每项是否无平方因子"及原始素因子分布。

---

## 七、Recamán 序列：反例参照

（OEIS [A005132](https://oeis.org/A005132)。）

$$
a(0)=0,\qquad a(n)=\begin{cases}a(n{-}1)-n,& \text{若结果为正且此前未出现},\\ a(n{-}1)+n,& \text{否则（无论是否已出现）}.\end{cases}
$$

前 40 项：$0,1,3,6,2,7,13,20,12,21,11,22,10,23,9,24,8,25,43,62,42,63,41,18,42,17,43,16,44,15,45,14,46,79,113,78,114,77,39,78$。

**判定：不符合"Pell 序列"（以及金属均值族）的定义。** 逐点：

| 判据 | Pell / Fibonacci 收敛子 | Recamán | 吻合 |
| --- | --- | --- | --- |
| 元素类型 | 有理数，收敛到二次无理数 | 非负整数，无极限 | ✗ |
| 递推 | 二阶线性（$S_{n+1}=mS_n+S_{n-1}$） | 一阶自指贪心（需全史成员查询） | ✗ |
| 单调 / 收敛 | 交替逼近 $\sqrt2$ / $\varphi$ | 剧烈非单调、发散 | ✗ |
| 数论来源 | Pell 型方程（单位群） | 无 | ✗ |
| 增长 | 指数 | $\sim n\log n$（经验拟合） | ✗ |
| 单射 | 是 | 否（$42,43,78$ 等重复出现） | ✗ |

**状态**：`COMPUTATIONALLY VERIFIED EXAMPLE`（前 40 项与 OEIS 一致）+ `STRUCTURAL PROPOSAL`（"不承载可用的代数结构"这一否定性判断是观察，非定理）。Recamán 不能承袭笔记二的构造（无范数恒等式、无倍增、无 Möbius 大步），在试验场谱系中仅作"无结构贪心序列"的反例参照。

---

## 八、四序列定位总表

| 序列 | 谱系 | 深度增长 | 范数/单位恒等式 | 约分虫洞 | HTWR 二次壁垒 | 试验场角色 |
| --- | --- | --- | --- | --- | --- | --- |
| **Pell**（$m=2$，银比） | 金属均值收敛子 | 线性 $n\ln(1+\sqrt2)$ | $P^2-2Q^2=(-1)^k$ | 有 | 有，被虫洞打破 | 主试验场（定理 1/2） |
| **Fibonacci**（$m=1$，金比） | 金属均值收敛子 | 线性 $n\ln\varphi$ | $F_{n+1}F_{n-1}-F_n^2=(-1)^n$ | 有 | 有，结构同 Pell | 同族"最慢"基准 |
| **Sylvester** | 双重指数/两两互素 | **翻倍** $2^{n}\ln E$ | 无（互素） | 无 | **无，朴素即最优** | 反复平方免费午餐压力测试 |
| **Recamán** | 无结构贪心 | $\sim n\log n$ | 无 | 无 | 不适用 | 反例参照 |

---

## 九、记号冲突与需记录事项

据 AGENTS.md"不静默调和冲突"：

- 笔记把分母 $Q_n=1,2,5,12,29,\dots$ 记为"Pell 数"、分子 $P_n=1,3,7,17,\dots$ 记为伴序列；但 OEIS 标准术语中，$1,2,5,12,29,\dots$ 是 **A000129 Pell numbers**，$1,3,7,17,\dots$ 是 **A001333 companion Pell（Pell–Lucas）**。
- 建议后续在论文符号表显式声明，避免"Pell sequence"检索歧义。

---

## 十、数学状态总表

| 编号 | 结论 | 状态 | 备注 |
| --- | --- | --- | --- |
| F1 | Cassini 恒等式 $F_{n+1}F_{n-1}-F_n^2=(-1)^n$ | `COMPUTATIONALLY VERIFIED EXAMPLE` → `STANDARD CONSEQUENCE REQUIRING AN IN-PAPER PROOF` | 经典；本笔记 $n\le11$ 验证 |
| F2 | Newton 倍增 $y_{2n}=\frac{y_n^2+1}{2y_n-1}$ | 同上 | 经典 Newton 迭代 |
| F3 | Möbius 大步 $y_{n+k}=y_k+\frac{(-1)^{k+1}}{F_k(F_k y_n+F_{k-1})}$ | 同上 | 斐波那契矩阵 $M^k$ |
| F4 | Fibonacci 的定理 2 帕累托边界 | `STRUCTURAL PROPOSAL` | 由 Pell 定理 2 平移，书面证明待写 |
| M1 | 金属均值 $\sigma_m=[m;\overline m]$ 及 Pell 型方程 | `STANDARD CONSEQUENCE REQUIRING AN IN-PAPER PROOF` | 经典数论 |
| M2 | $m\ge3$ 的 HTWR 帕累托边界 | `OPEN PROBLEM` | 预期同构，待核对 |
| S1 | Sylvester 三条恒等式（乘积=差、埃及分数、互素） | `COMPUTATIONALLY VERIFIED EXAMPLE` → `STANDARD CONSEQUENCE REQUIRING AN IN-PAPER PROOF` | 经典；本笔记验证 |
| S2 | Sylvester 的 HTWR 线性可达 / 无二次壁垒 | `STRUCTURAL PROPOSAL` | 量级观察 |
| R1 | Recamán 不符合 Pell 定义 | `COMPUTATIONALLY VERIFIED EXAMPLE` + `STRUCTURAL PROPOSAL` | 否定性观察 |
| A0 | HTWR 公理 I–IV 框架 | `STRUCTURAL PROPOSAL` | 见笔记一、二备注 |

---

## 十一、后续研究靶点

1. **（开放）** $m\ge3$ 金属均值（青铜比等）的 HTWR 帕累托曲线——核对大步 Möbius 分解与约分虫洞系数是否逐项成立。
2. **（开放）** $2^N-1$（Mersenne）序列的 HTWR 分析——它属于"线性递推 + 反复平方可加速"的又一谱系，需单独定位。
3. **（开放）** 为 Sylvester 写出严格的第一条 $(\mathcal A,\Sigma)$ 帕累托曲线（若其"无约分虫洞"结构使曲线退化为单点/直线，需给出形式化陈述）。
4. **（编辑）** 将第九节的记号冲突登记进论文符号表或开放问题文件。
5. **（编辑）** 把本笔记 F1–F3、S1 的 `STANDARD CONSEQUENCE` 证明补入正文，使 Fibonacci/Sylvester 试验场具备可引用的恒等式依据。
