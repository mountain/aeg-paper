# 从算术 Tube 到纽结不变量：对数零面、编织曲面与 Markov 筛选

**File:** <code>restructure/discussions/aeg-tube-braid-markov-invariants.md</code>  
**Status:** Working research note  
**Version:** 1.0  
**Date:** 2026-08-05  
**Discussion period:** 2026-07-24—2026-08-05  
**Primary topic:** AEG Tube、对数零面、辫单值性与可能的纽结不变量  
**Primary paper interface:** Paper III — Arithmetic Expression Geometry III: Singular Zero Geometry and Tubes  
**Relevant theorem nodes:** A1, A4, T7, Z2, Z3, Z5, T8, Z6, T15, T16, T17；本笔记提出的候选节点尚未进入权威依赖图  
**Authority:** Subordinate to <code>restructure/00–08</code>; not itself authoritative

> This note condenses a research discussion into a reusable working document.
> It contains intermediate ideas, rejected formulations, and open questions.
> When it conflicts with the authoritative restructuring files, the latter prevail.

## 1. Executive summary

本讨论追问：算术表达式几何中的 Tube 如何容纳不同纽结，而 assignment、对数零面、算术扭率与接触连接能否进一步产生不由 Alexander–Burau 层决定的新不变量。

目前最强的结论不是“已经构造出新纽结不变量”，而是一条更清楚的分界线。

第一，Tube 中真正承载纽结复杂性的是有限多个 moving roots 或有限多截面的非交换 braid monodromy。\(E_{\log}\) 的可数零面应先理解为同一有限零结构在 logarithmic cover 中的 lifts；它们主要记录整数 deck winding，不能仅凭可数性产生一般辫群的非交换复杂性。

第二，真正嵌入的闭辫沿参数圆始终位于判别式补空间，边界上没有 root collision。四价重联应位于二维 filling 与判别式的横截事件中，局部模型为
\[
w^2=\tau,
\]
而不是一般 knot tube 的正则点。这把 regular tube、branched filling 与 boundary braid 分成了三个不同层次。

第三，经典拓扑骨架已有成熟前身：配置空间、闭辫、Rudolph 的 algebraic functions 与 braided surfaces、无限循环覆盖上的 Burau–Alexander 理论、Lawrence 多探针表示，以及 quandle cocycle 与 KZ–Kohno holonomy。AEG 的潜在新增量只能来自 assignment、nodal divisor、arithmetic connection、expression probes 与 branch-cell curvature 等装饰。

第四，讨论得到两个可直接证明的塌缩结果：无状态、交换值、对 braid 拼接可加的标量只看到 writhe；固定 multiplier 的 \(\operatorname{Aff}(1)\) 共轭子 quandle 是 Alexander quandle，raw affine torsion 在普通系数下是 coboundary。扭曲系数下存在一个尚未判定的共振窗口 \(T_{\mathrm{coef}}=t^{-1}\)。

因此真正的成败链条是
\[
\text{AEG 局部几何}
\longrightarrow
\text{braid action}
\longrightarrow
\text{Markov descent}
\longrightarrow
\text{Alexander/Burau 非塌缩}.
\]
Paper III 拥有这一发展。当前阻塞点是：尚无通过正、负 Markov stabilization 的 AEG closure construction，也尚无 knot-level separation theorem。

## 2. Starting intuition

初始直觉是：若一个 arithmetic tube 中出现可数多个零面，而一条表达式轨迹或 strand 穿过这些面，则交叉顺序、零面层号与算术扭率也许能编码纽结。其几何诱因来自三类图像：

1. \(E_{\log}\) 的无限层状零结构类似一组 pages；
2. moving roots 随圆参数闭合，形成缠绕的多截面；
3. order-4 局部图像似乎提供 crossing 或 reconnection 的基本单元。

预期收益是把 AEG 的“过程先于端值”原则推广到纽结：同样的终点或同样的交换化数据可能对应不同的有序历史，而 Tube 也许能记录这些差异，并给出比 Alexander polynomial 更精细的量。

这一初始图像隐含了若干当时未被证明的假设：

- 可数零面是 downstairs 中彼此独立的物理面；
- 四价点可以作为嵌入 Tube 的正则局部模型；
- 有一条穿线便足以记录一般 knot complexity；
- 零面穿越数或扭率和会自动在 Markov moves 下不变；
- 比 Burau 更强的 braid datum 会自动给出比 Alexander 更强的 knot invariant；
- contact structure 或 distinguished spine 可以在不作归一化的情况下被遗忘。

讨论的主要贡献恰恰是逐项拆开这些假设。战略直觉仍有价值：AEG 可能提供经典 braid skeleton 上的额外装饰。但“有装饰”与“有普通纽结不变量”之间还隔着局部一致性、gauge equivalence、Markov descent 和非塌缩四道检验。

## 3. Objects and notation

| Object | Meaning | Status | Paper owner | Notes |
|---|---|---|---|---|
| \(\mathfrak E=(M,g,a;\ldots)\) | arithmetic expression space，含 metric 与 assignment | STRUCTURAL PROPOSAL | Paper I / III interface | 具体子节点保留各自权威状态；regular 与 singular 必须分开 |
| \(E_k\), \(E_{\log}\) | 多零与对数零几何的候选模型 | STRUCTURAL PROPOSAL | Paper III | 一般分类仍为 OPEN PROBLEM；不得从单个例子推广 |
| \(\mathcal Z=a^{-1}(0)\) | arithmetic nodal set/divisor | PROVED WITH STATED HYPOTHESES / STRUCTURAL PROPOSAL | Paper I 提供 regular interface；Paper III 发展 singular theory | 前一标签限 regular zero theorem；后一标签用于 singular divisor framework |
| \(\mathcal P_n\) | 首一 \(n\) 次复多项式空间 | PROVED | Paper III | 标准背景定义；系数与无序 roots 等价 |
| \(\mathcal P_n^{\mathrm{sf}}\) | 判别式非零的 square-free 子空间 | PROVED | Paper III | 标准背景定义；基本群结论另需正文引用 |
| \(\Delta\) | discriminant locus \(\{\operatorname{Disc}=0\}\) | OPEN PROBLEM：标准定义已知，AEG 发展未完成 | Paper III | 与 \(E_k\) strata 的关系尚待建立 |
| \(\gamma:S^1\to\mathcal P_n^{\mathrm{sf}}\) | coefficient loop / moving-root loop | STANDARD CONSEQUENCE REQUIRING AN IN-PAPER PROOF | Paper III | roots 的轨迹给出 closed braid |
| \(\Gamma:D^2\to\mathcal P_n\) | \(\gamma\) 的二维 filling | STRUCTURAL PROPOSAL | Paper III | 是否满足 AEG 额外条件仍未知 |
| \(\widetilde F\), \(T\) | 无限循环或 logarithmic cover 及其 deck transformation | STRUCTURAL PROPOSAL | Paper III | 经典 cover 是背景；AEG 识别尚待证明，不应把 lifts 当成独立 downstairs sheets |
| \(K\) | 有限多根或多截面形成的 braid/link locus | STRUCTURAL PROPOSAL | Paper III | 与 singular spine 可为不同对象 |
| \(s\) | expression 或 polynomial probe section | STRUCTURAL PROPOSAL | Paper III | 单 probe 与 multi-probe 应分开 |
| \(\mathcal H\) | 跨 fibers 的 horizontal distribution/connection | STRUCTURAL PROPOSAL | Paper III，输入来自 Paper I | 需固定 gauge 与左右作用约定 |
| \(\Sigma\) | singular/branch locus | STRUCTURAL PROPOSAL | Paper III | filling 中的 simple branch points |
| \(\kappa\) | affine translation-order defect | PROVED WITH STATED HYPOTHESES | Paper I algebraic source；Paper III 测试其 knot use | 本文用 \(u,v\) 作 translation coordinates，避免与 assignment \(a\) 冲突 |
| \(T_{\mathrm{coef}}\) | twisted coefficient module 上的作用参数 | STRUCTURAL PROPOSAL | Paper III | 与 deck transformation \(T\) 不得混淆 |
| \(\mathcal D_{\mathrm{AEG}}(\beta)\) | AEG-decorated braid presentation datum | STRUCTURAL PROPOSAL | Paper III | 未过 Markov 检验前不用 \(\mathcal I\) 命名 |

一个暂定的数据包是
\[
\mathfrak T=
\bigl(
\pi:\mathcal X\to B,\,
g^V,\,
a,\,
\mathcal H,\,
\mathcal Z,\,
\Sigma,\,
K,\,
s
\bigr),
\]
其中 \(B=S^1\) 时描述边界 Tube，\(B=D^2\) 时描述 filling。忘掉
\[
(g^V,a,\mathcal H,\mathcal Z,s)
\]
后，只留下经典 braided mapping torus 或 braided surface 的骨架。此处是工作框架，不含存在性、唯一性或不变性断言。

## 4. Development of the argument

### 4.1 从局部 fiber 到全局 monodromy

假设 \(n\) 个 roots 在每个 fiber 内互异，并随 \(\theta\in S^1\) 连续运动。局部 fiber 可以完全相同，但绕 \(S^1\) 一周后的返回置换与完整路径不同。无序配置空间的基本群给出
\[
\pi_1(\operatorname{UConf}_n(\mathbb C))
\cong
B_n.
\]
因此不同 knot 的机制不是“换一套局部面”，而是选择不同的 finite multisection 与 braid monodromy。

**Status:** STANDARD CONSEQUENCE REQUIRING AN IN-PAPER PROOF。  
**Downstream implication:** Tube 的表示理论必须先有 finite moving-root layer；\(E_{\log}\) 不能代替 braid monodromy。

### 4.2 可数 logarithmic sheets 的正确角色

若 \(E_{\log}\) 来自对 angular/logarithmic coordinate 的提升，则整数标号的 sheets 由 deck transformation
\[
T:k\longmapsto k+1
\]
联系。downstairs 中它们是同一有限零结构的 lifts。单 probe 的净层号变化首先给出一个 \(\mathbb Z\)-值 winding history，这是交换化信息。

因此这里应区分两层数据，而不声称存在未经证明的直积：
\[
\text{threading data}
=
\underbrace{\text{finite strands 的非交换 braid history}}_{\text{knot complexity}}
+
\underbrace{\text{logarithmic lifts 的整数 deck history}}_{\text{winding shadow}}.
\]

**Status:** 第一部分为经典背景；其 AEG 解释为 STRUCTURAL PROPOSAL。  
**Correction:** “可数 sheets 本身产生任意 knot complexity”被排除。

### 4.3 边界 Tube 避开判别式

一个嵌入 closed braid 对应
\[
\gamma:S^1\longrightarrow\mathcal P_n^{\mathrm{sf}}.
\]
因为 \(\gamma\) 始终避开
\[
\Delta=\{\operatorname{Disc}=0\},
\]
边界参数上不会发生 root collision。若碰撞发生，所得对象已离开 embedded braid category。

**Status:** STANDARD CONSEQUENCE REQUIRING AN IN-PAPER PROOF。  
**Downstream implication:** regular boundary tube 与 singular reconnection 必须分节定义。

### 4.4 四价事件属于 filling

令
\[
\Gamma:D^2\longrightarrow\mathcal P_n,
\qquad
\Gamma|_{\partial D^2}=\gamma.
\]
圆盘内部可以横截判别式。简单交点的局部正规形为
\[
w^2=\tau.
\]
当 \(\tau\) 绕原点一周，两根作 half-twist；沿实方向穿过 \(\tau=0\) 时，实切片出现四价重联。故
\[
\begin{aligned}
S^1\text{-Tube}
&:\ \text{discriminant-free closed braid},\\
D^2\text{-filling}
&:\ \text{允许 simple branch points 的 braided surface},\\
\partial(D^2\text{-filling})
&:\ \text{原来的 closed braid}.
\end{aligned}
\]

**Status:** 局部正规形为经典事实；把 AEG order-4 图像放入 filling 是 STRUCTURAL PROPOSAL，需 Paper III 正式化。  
**Correction:** 四价点不是一般嵌入 knot tube 上的正则点。

### 4.5 经典边界与 AEG 的潜在新增量

moving algebraic roots、closed braids 与 braided surfaces 已由 Rudolph 等发展；无限循环覆盖上的 braid action 是 Burau–Alexander 机制；two-point configuration homology 导向 Lawrence–Krammer–Bigelow 表示；quandle cocycle 提供局部权重的 Reidemeister descent；KZ–Kohno 型 connection 提供有序 monodromy。

因此 AEG 的潜在原创性不在
\[
\text{roots move}\Longrightarrow\text{closed braid},
\]
而在额外数据
\[
(g^V,a,\mathcal H,\mathcal Z,s)
\]
是否自然、可计算、gauge-compatible，并在 Markov quotient 后仍有剩余信息。

**Status:** 历史定位为标准背景；新增装饰为 STRUCTURAL PROPOSAL。

### 4.6 Markov 筛选

设候选 crossing operators 给出
\[
\rho_n^{\mathrm{AEG}}:B_n\to A_n^\times,
\qquad
R_i=\rho_n^{\mathrm{AEG}}(\sigma_i).
\]
第一关是 braid relations：
\[
R_iR_{i+1}R_i=R_{i+1}R_iR_{i+1},
\qquad
R_iR_j=R_jR_i\quad (|i-j|\ge2).
\]
第二关是 closure descent。若采用 Markov trace \(\tau_n:A_n\to R\)，至少需要 cyclicity 和
\[
\tau_{n+1}\bigl(\iota_n(X)R_n^{\pm1}\bigr)
=
\kappa_\pm\tau_n(X).
\]
若归一化形式为
\[
I_n(\beta)=u^{w(\beta)}v^n\tau_n(\rho_n(\beta)),
\]
则须找到单位 \(u,v\) 满足
\[
uv\kappa_+=1,
\qquad
u^{-1}v\kappa_-=1.
\]
这不是自动成立的。

第三关是 knot-level comparison：即使 \(\rho^{\mathrm{AEG}}\) 检测到 Burau kernel element，取 closure functional 后新增信息仍可能消失。因此
\[
\rho^{\mathrm{AEG}}\text{ 比 Burau 强}
\centernot\Longrightarrow
I_{\mathrm{AEG}}\text{ 比 Alexander 强}.
\]

**Status:** 经典 Markov 机制为标准背景；AEG representation、trace 与非塌缩均为 OPEN PROBLEM。

### 4.7 第一塌缩：无状态可加标量

设 \(A\) 为交换群，且
\[
\Theta_n:B_n\to A
\]
是群同态。令 \(c_i=\Theta_n(\sigma_i)\)。对 braid relation 应用 \(\Theta_n\)：
\[
2c_i+c_{i+1}=c_i+2c_{i+1},
\]
故 \(c_i=c_{i+1}\)。存在唯一 \(c_n\in A\) 使
\[
\Theta_n(\beta)=w(\beta)c_n.
\]
若这族映射与 \(B_n\hookrightarrow B_{n+1}\) 相容，则 \(c_n\) 与 \(n\) 无关；若 \(\Theta\) 本身还要求在正、负 stabilization 下均不变，则 \(c=0\)。

**Status:** PROVED。  
**Boundary:** 该结论只排除无状态、交换值、对拼接直接可加的标量。它不排除 coloring state sums、operator-valued ordered products、twisted local systems 或 multi-probe constructions。

### 4.8 第二塌缩：固定 multiplier 的 affine torsion

在交换环 \(R\) 上写
\[
\operatorname{Aff}(1,R)=R^\times\ltimes R,
\qquad
(p,u)(q,v)=(pq,u+pv),
\]
并固定右共轭约定
\[
x\triangleright y=y^{-1}xy.
\]
直接计算：
\[
(p,u)\triangleright(q,v)
=
\left(p,q^{-1}\bigl(u+(p-1)v\bigr)\right).
\]
固定 \(t\in R^\times\) 后，
\[
X_t=\{(t,u):u\in R\}
\]
是共轭子 quandle，且
\[
u\triangleright v
=
t^{-1}u+(1-t^{-1})v.
\]
所以 \(X_t\) 是参数 \(t^{-1}\) 的 Alexander quandle。只有在域上且 \(t\neq1\) 等适当条件下，才能进一步称其为完整共轭类。

定义 translation-order defect
\[
\kappa((p,u),(q,v))
=
(1-q)u+(p-1)v.
\]
在 \(X_t\) 上，
\[
\kappa_t(u,v)=(t-1)(v-u).
\]
若普通 quandle coboundary 约定为
\[
df(u,v)=f(u\triangleright v)-f(u),
\qquad f(u)=u,
\]
则
\[
df(u,v)=\frac{t-1}{t}(v-u),
\qquad
\kappa_t=t\,df=d(tf).
\]
故 raw torsion 在平凡系数的普通 quandle cohomology 中表示零类。

**Status:** PROVED WITH STATED HYPOTHESES。  
**Consequence:** 固定 multiplier 的 single-probe、first-order scalar torsion 不会自行增加一个新的 quandle cohomology class；Alexander coloring count 本身仍可能非平凡。

### 4.9 扭曲系数的共振窗口

在 Carter–Elhamdadi–Saito 的一种约定下，twisted 2-cocycle 方程为
\[
\begin{aligned}
T_{\mathrm{coef}}\phi(x,y)+\phi(x\triangleright y,z)
={}&T_{\mathrm{coef}}\phi(x,z)
+(1-T_{\mathrm{coef}})\phi(y,z)\\
&+\phi(x\triangleright z,y\triangleright z),
\end{aligned}
\]
而 twisted coboundary 是
\[
\delta_T f(x,y)
=
f(x\triangleright y)
-
T_{\mathrm{coef}}f(x)
-
(1-T_{\mathrm{coef}})f(y).
\]
对 \(f(u)=u\)，
\[
\delta_Tf(u,v)
=
(T_{\mathrm{coef}}-t^{-1})(v-u).
\]
直接代入可验证 \(\kappa_t\) 对任意 \(T_{\mathrm{coef}}\) 都满足上述 twisted 2-cocycle 方程。若
\[
T_{\mathrm{coef}}-t^{-1}
\]
可逆，则
\[
\kappa_t
=
\frac{t-1}{T_{\mathrm{coef}}-t^{-1}}\delta_T f
\]
仍为 exact。共振值
\[
T_{\mathrm{coef}}=t^{-1}
\]
处，当前 exactness 证明失效，但这不等于已经证明其上同调类非零。

**Status:** cocycle 与非共振 exactness 为 PROVED WITH STATED HYPOTHESES；共振非平凡性为 OPEN PROBLEM。  
**Downstream implication:** 有限域搜索应优先检查共振及零因子情形，而非无目标枚举 twisting。

### 4.10 变化 multiplier 与 RIII anomaly

对
\[
x=(p,u),\quad y=(q,v),\quad z=(r,w),
\]
定义普通 quandle 2-cocycle defect
\[
\begin{aligned}
\mathfrak A_\kappa(x,y,z)
={}&
\kappa(x,y)+\kappa(x\triangleright y,z)\\
&-\kappa(x,z)-\kappa(x\triangleright z,y\triangleright z).
\end{aligned}
\]
代数化简得到
\[
\mathfrak A_\kappa(x,y,z)
=
\frac{(q-r)(r-1)}{qr}\,\kappa(x,y).
\]
它通常非零，但在 \(q=r\)、\(r=1\) 或 \(\kappa(x,y)=0\) 时消失。对普通单分支 knot 的 conjugation coloring，同一分支上的 meridians 互相共轭，multiplier 保持不变，故不能随意让每条 arc 取不同 multiplier。要使此 anomaly 有内容，需要多分支 link、biquandle/dynamical state、区域变量，或把 multiplier 解释为独立 probe/connection state。

**Status:** 公式为 PROVED WITH STATED HYPOTHESES；其 higher-cocycle 解释为 STRUCTURAL PROPOSAL。  
**Correction:** non-flatness 或 RIII defect 不会自动生成 associator。还必须给出 associator、pentagon/hexagon coherence，或满足相应 fake-flatness 与 filling-independence 的 2-connection。

## 5. Established results

### Result R-1: Scalar additive collapse

**Status:** PROVED  
**Statement:** 每个无状态、取值于交换群且对 braid 拼接可加的 \(\Theta_n:B_n\to A\) 都具有 \(\Theta_n(\beta)=w(\beta)c_n\) 的形式。若它本身在正、负 Markov stabilization 下不变，则它平凡。  
**Hypotheses:** \(n\ge2\)；\(A\) 为交换群；\(\Theta_n\) 为群同态；跨股数结论另需标准嵌入相容性。  
**Argument or proof location:** 本笔记 §4.7 的生成元短证明。  
**Repository source:** 本讨论的新可导出命题；现有 authoritative files 仅给出 knot invariant 的开放状态。  
**Relevant theorem nodes:** 与 A4、T17 有概念联系，但尚无权威节点。  
**Paper destination:** Paper III。  
**Remaining integration work:** 固定 Markov convention，并把命题写入 Paper III 的 no-go 小节。

### Result R-2: Fixed-multiplier affine subquandle

**Status:** PROVED WITH STATED HYPOTHESES  
**Statement:** 对右共轭 \(x\triangleright y=y^{-1}xy\)，固定 multiplier 子 quandle \(X_t\subset\operatorname{Aff}(1,R)\) 同构于参数 \(t^{-1}\) 的 Alexander quandle。  
**Hypotheses:** \(R\) 为交换环；\(t\in R^\times\)。称为完整共轭类还需额外条件，例如域上 \(t\neq1\)。  
**Argument or proof location:** 本笔记 §4.8 的直接群运算。  
**Repository source:** <code>knots/knots_01.tex</code>、<code>notes/note_11.tex</code> 提供 affine/knot 动机；精确子 quandle 限定来自本讨论审计。  
**Relevant theorem nodes:** A1, A4。  
**Paper destination:** Paper III，代数输入回引 Paper I。  
**Remaining integration work:** 与仓库全局左右共轭和 composition conventions 对齐。

### Result R-3: Raw affine torsion is ordinarily exact

**Status:** PROVED WITH STATED HYPOTHESES  
**Statement:** 在 \(X_t\) 上，\(\kappa_t(u,v)=(t-1)(v-u)=d(tf)\)，其中 \(f(u)=u\)。因此 raw torsion 在平凡系数的普通 quandle cohomology 中为 coboundary。  
**Hypotheses:** 同 R-2；采用 §4.8 的 coboundary 符号约定。  
**Argument or proof location:** 本笔记 §4.8。  
**Repository source:** <code>notes/note_11.tex</code> 中的相关强表述需要据此收缩；<code>knots/results.tex</code> 的计算不能替代上同调证明。  
**Relevant theorem nodes:** A4, T17。  
**Paper destination:** Paper III。  
**Remaining integration work:** 审计符号；明确“raw torsion 未增加新类”不等于 Alexander coloring count 平凡。

### Result R-4: Twisted cocycle and non-resonant exactness

**Status:** PROVED WITH STATED HYPOTHESES  
**Statement:** \(\kappa_t\) 满足所采用的 twisted 2-cocycle 方程；当 \(T_{\mathrm{coef}}-t^{-1}\) 可逆时，它仍为 twisted coboundary。  
**Hypotheses:** coefficient ring、module action 与右 quandle convention 如 §4.9；可逆性用于 exactness。  
**Argument or proof location:** 本笔记 §4.9 的代入计算。  
**Repository source:** 本讨论的新计算；需与 twisted quandle 文献的 conventions 核对。  
**Relevant theorem nodes:** 候选新节点。  
**Paper destination:** Paper III。  
**Remaining integration work:** 写出链复形，验证负 crossing、区域 Alexander numbering 与 gauge change。

### Result R-5: Variable-multiplier RIII defect

**Status:** PROVED WITH STATED HYPOTHESES  
**Statement:** 对 §4.10 的右共轭约定，
\[
\mathfrak A_\kappa(x,y,z)=
\frac{(q-r)(r-1)}{qr}\kappa(x,y).
\]
**Hypotheses:** multiplier \(p,q,r\) 为单位；采用普通 2-cocycle defect 与给定顺序。  
**Argument or proof location:** 本笔记 §4.10；完整展开应进入附录或计算笔记。  
**Repository source:** 本讨论的新代数计算。  
**Relevant theorem nodes:** A4, T17；候选 anomaly 节点。  
**Paper destination:** Paper III。  
**Remaining integration work:** 用 symbolic check 独立复核，并分别测试左共轭与镜像 convention。

### Result R-6: Boundary collision exclusion and filling local model

**Status:** STANDARD CONSEQUENCE REQUIRING AN IN-PAPER PROOF  
**Statement:** embedded root braid 的 boundary loop 位于 \(\mathcal P_n^{\mathrm{sf}}\)，故无碰撞；generic filling 与 discriminant 的 simple transverse intersection 局部为 \(w^2=\tau\)，其 monodromy 是 half-twist。  
**Hypotheses:** coefficient family 至少具有所需 smooth/holomorphic regularity；discriminant crossing 为简单横截；其余 roots 保持简单。  
**Argument or proof location:** 配置空间与 simple branched-cover 的标准局部论证。  
**Repository source:** <code>notes/note_02.tex</code>、<code>note_03.tex</code>、<code>note_13.tex</code> 的 Tube/branch 动机需迁移审计。  
**Relevant theorem nodes:** Z3, Z5, T8, Z6；候选 discriminant 节点。  
**Paper destination:** Paper III。  
**Remaining integration work:** 正式引用或写出局部正规形证明，并补 properness/compactness 条件。

### Result R-7: Figure-eight affine relator calculation

**Status:** COMPUTATIONALLY VERIFIED EXAMPLE  
**Statement:** 在 <code>knots/knots_01.tex</code> 的约定中，令 \(a:x\mapsto tx\)、\(b:x\mapsto x+1\)，词 \(abbbaBAAB\) 的 translation coordinate 为 \(-\Delta_{4_1}(t)\)。  
**Hypotheses:** 保留该文件的 word order、逆元、表示与 normalization convention。  
**Argument or proof location:** <code>knots/knots_01.tex</code> 的逐词 affine composition。  
**Repository source:** <code>knots/knots_01.tex</code>。  
**Relevant theorem nodes:** A1, A4。  
**Paper destination:** Paper III 的受限例子或档案计算。  
**Remaining integration work:** 明确它先是自由群 word calculation；只有在 relator image 为 identity 的参数 locus 上才下降到 knot group representation。不得把 generic \(t\) 的结果直接称为内在 knot invariant。

## 6. Structural proposals and conjectures

### 6.1 Structural proposals

#### SP-1: AEG-decorated braided mapping torus

提出 §3 的 \(\mathfrak T\) 数据包作为工作对象。还需定义 admissible morphisms、gauge changes、spine changes、boundary/filling compatibility 与 forgetful functor。验证它的定理应是：每个允许的局部 chart 能粘合成此类对象，且 gauge-equivalent presentations 给出同一适当类别的 decorated braid。若出现不可控 chart dependence 或无法定义 composition，则框架需弱化。目标为 Paper III。

#### SP-2: Presentation datum rather than invariant

在证明不变性前，候选数据统一写作
\[
\mathcal D_{\mathrm{AEG}}(\beta)
=
\left(
H_1(\widetilde F),
T,
\beta_*,
[\mathcal Z],
\operatorname{Hol},
I(s,\mathcal Z)
\right),
\]
不写作 \(\mathcal I_{\mathrm{AEG}}(K)\)。验证它需一个 gauge-equivalence theorem 和 AEG Markov theorem。若数据依赖 braid axis、sheet origin 或 presentation，则只能保留为 annular/framed datum。目标为 Paper III。

#### SP-3: Twisted branch-cell cocycle

尝试从 \(B_1\) branch chart 的 mixed curvature 与 counterterm 构造
\[
[\phi_{\mathrm{AEG}}]\in H_Q^2(X;M_\Phi).
\]
额外数据包括 crossing state space、module action、region numbering、orientation convention 与 gauge coboundaries。需要证明 normalized twisted cocycle equation、非平凡性及 closure invariance。若所有自然类均 exact，则该路线只提供重述。目标为 Paper III。

#### SP-4: Two-probe AEG local system

在 punctured disc \(F_n\) 的无序双点配置空间
\[
\operatorname{UConf}_2(F_n)
\]
上构造 braid-equivariant AEG local system。严格版本可能需要相对同调或 Borel–Moore homology，不应先验固定为朴素 \(H_2\)。验证定理包括局部系统等变性、有限生成性、gauge compatibility 与 Markov descent。若只恢复 Lawrence–Krammer–Bigelow 表示而没有 AEG-specific deformation，则原创性主张需收缩。目标为 Paper III。

#### SP-5: Higher anomaly route

把 \(\mathfrak A_\kappa\) 视为 associator 或 3-cocycle 的候选来源，而不是已经存在的高阶不变量。所需新增数据为 associator \(\Phi\)、pentagon、hexagon，或 coherent 2-connection 与 filling-independence。任一 coherence failure 都使普通 braid isotopy 依赖具体 homotopy。目标为 Paper III；若进入真正 higher-categorical formalism，可列为 Papers I–IV 之后的项目。

### 6.2 Conjectures

#### C-1: AEG linearization conjecture

**Status:** CONJECTURE  
存在一个明确定义且 Markov-compatible 的 AEG braid object，使其适当线性化或交换化恢复 Burau：
\[
\operatorname{Lin/Ab}(\rho^{\mathrm{AEG}})
\cong
\rho^{\mathrm{Bur}},
\]
同时线性化核中存在 closure 后不消失的信息。

已知特殊情形仅是“单 probe 与无限循环覆盖自然接近 Burau”的经典类比；尚无 AEG representation 或 closure functional。若所有自然 AEG decorations 经 Markov normalization 后因子化通过 Burau，则猜想失败。目标为 Paper III。

#### C-2: Resonant torsion nontriviality

**Status:** CONJECTURE  
在某些有限系数环、某些 \(t\in R^\times\) 及共振作用 \(T_{\mathrm{coef}}=t^{-1}\) 下，\(\kappa_t\) 定义非零 twisted quandle cohomology class，并产生非平凡的 diagram state sum。

当前只证明了共振处现有 exactness 证法失效，尚无非零类证据。因此该猜想应在最小有限例子计算后决定保留或降为开放问题。目标为 Paper III。

### 6.3 Open programs

#### OP-1: AEG–Alexander–Markov program

四个阶段依次为：

1. 每个 oriented link 的 classical braid skeleton 是否可提升为满足 AEG 条件的 Tube presentation；
2. 两个 presentations 的等价是否由 AEG braid isotopy、gauge equivalence 与适当 Markov moves 生成；
3. 是否存在 closure datum 在这些 moves 下下降；
4. 是否存在 Alexander/Burau 层相同而 AEG 值不同的 links。

任何前三步失败都阻止“ordinary knot invariant”的称呼；第四步失败则表示不变量可能只是已知层的重表达。

#### OP-2: Nonabelian configuration-space holonomy

研究
\[
\nabla_{\mathrm{AEG}}
=
d-\hbar\sum_{i<j}
\Omega_{ij}^{\mathrm{AEG}}\,d\log(z_i-z_j)
-\Theta_{\mathrm{AEG}}.
\]
严格 braid representation 需要 infinitesimal braid relations 及涉及 \(\Theta_{\mathrm{AEG}}\) 的 flatness 条件；projective flatness 还需 framing anomaly normalization；真正 non-flat 情形则必须升级到 coherent higher transport。目标为 Paper III 或后续工作。

## 7. Rejected or superseded formulations

### Rejected formulation X-1

**Earlier formulation:** 可数 \(E_{\log}\) sheets 自身足以制造任意 knot complexity。  
**Problem:** deck-layer count 首先是交换的 winding 数据；一般 braid complexity 来自有限 moving points 的非交换 monodromy。  
**Counterexample, contradiction, or missing hypothesis:** 不同 braid 可有同一总 deck shift。  
**Replacement formulation:** 把 logarithmic winding 与 finite-strand braid history 分层记录。  
**Files or passages still using the old form:** <code>notes/note_02.tex</code>、<code>note_03.tex</code>、<code>note_13.tex</code> 需审计。

### Rejected formulation X-2

**Earlier formulation:** order-4 结点是一般 embedded knot tube 的正则点。  
**Problem:** embedded root braid 的 boundary loop 位于判别式补空间。  
**Counterexample, contradiction, or missing hypothesis:** root collision 意味着离开 \(\mathcal P_n^{\mathrm{sf}}\)。  
**Replacement formulation:** 四价重联是 \(D^2\)-filling 横截判别式时的 branch event。  
**Files or passages still using the old form:** Tube 与 tiling 相关 notes 需逐段审计。

### Rejected formulation X-3

**Earlier formulation:** smooth total zero set 自动是全局平凡 Tube。  
**Problem:** smooth submersion 不提供全局 properness、compact fibers 或 Ehresmann triviality 的全部条件。  
**Counterexample, contradiction, or missing hypothesis:** authoritative Z6 已明确 properness warning。  
**Replacement formulation:** 区分 total zero set、smooth zero surface、locally trivial tube 与 embedded tube。  
**Files or passages still using the old form:** 以 <code>restructure/04-current-to-target-map.md</code> 和 Z6 为准审计历史 notes。

### Rejected formulation X-4

**Earlier formulation:** tube with thread 自动定义 knot invariant。  
**Problem:** 尚未证明 isotopy、gauge、spine change 或 Markov invariance。  
**Counterexample, contradiction, or missing hypothesis:** 同一 link 有不同 braid presentations；distinguished axis 可能保留 presentation data。  
**Replacement formulation:** 在下降前称 \(\mathcal D_{\mathrm{AEG}}(\beta)\) 为 presentation datum。  
**Files or passages still using the old form:** <code>knots/results.tex</code>、<code>knots/knots_03.tex</code> 与 Tube notes 需限定措辞。

### Rejected formulation X-5

**Earlier formulation:** 任意标量零面穿越和或 torsion sum 都可成为新 knot invariant。  
**Problem:** 无状态可加标量通过 \(B_n^{\mathrm{ab}}\cong\mathbb Z\) 因子化。  
**Counterexample, contradiction, or missing hypothesis:** §4.7 证明其只看到 writhe，双向 stabilization 甚至迫使其平凡。  
**Replacement formulation:** 保留状态、非交换有序积、twisted coefficients 或 multi-probe 数据。  
**Files or passages still using the old form:** 所有把 total crossing weight 直接称 invariant 的草稿需审计。

### Rejected formulation X-6

**Earlier formulation:** 整个 \(\operatorname{Aff}(1)\) conjugation quandle 是 Alexander quandle。  
**Problem:** 只有固定 multiplier 子 quandle \(X_t\) 具有该形式。  
**Counterexample, contradiction, or missing hypothesis:** 变化 multiplier 的共轭运算保留第一坐标但依赖另一元素的 multiplier。  
**Replacement formulation:** 明确写 \(X_t\subset\operatorname{Aff}(1,R)\)，并固定右共轭 convention。  
**Files or passages still using the old form:** <code>notes/note_11.tex</code> 及未来 knot notes。

### Rejected formulation X-7

**Earlier formulation:** raw affine torsion 本身给出非平凡 ordinary quandle cocycle invariant。  
**Problem:** \(\kappa_t=d(tf)\) 是 coboundary。  
**Counterexample, contradiction, or missing hypothesis:** §4.8 的显式 primitive。  
**Replacement formulation:** 普通系数下记录 collapse；twisted 共振非平凡性另行计算。  
**Files or passages still using the old form:** <code>notes/note_11.tex</code> 的“intrinsic topological invariant”等强表述需审计。

### Rejected formulation X-8

**Earlier formulation:** 让同一 knot 的各 arcs 有不同 multiplier 即可逃离 affine collapse。  
**Problem:** ordinary conjugation coloring 中 multiplier 是共轭不变量，同一 component 上恒定。  
**Counterexample, contradiction, or missing hypothesis:** meridian colors 沿 Reidemeister propagation 互相共轭。  
**Replacement formulation:** 使用 multi-component link、biquandle/dynamical state、region variables 或独立 probe state。  
**Files or passages still using the old form:** 尚无权威文件；未来草稿禁用。

### Rejected formulation X-9

**Earlier formulation:** 一个比 Burau faithful 的 braid representation 自动给出比 Alexander 更强的 knot invariant。  
**Problem:** closure functional 或 Markov trace 可能杀掉新增信息。  
**Counterexample, contradiction, or missing hypothesis:** braid-level kernel detection 与 knot-level separation 是不同命题。  
**Replacement formulation:** 分别证明 braid non-factorization、Markov descent 和 knot-pair separation。  
**Files or passages still using the old form:** two-probe 相关新稿需防止该跳步。

### Rejected formulation X-10

**Earlier formulation:** non-flat connection 或 RIII anomaly 自动产生 associator。  
**Problem:** 一般 non-flat parallel transport 首先导致 homotopy dependence；associator 还需 coherence。  
**Counterexample, contradiction, or missing hypothesis:** 缺少 pentagon、hexagon、fake-flatness 与 filling-independence。  
**Replacement formulation:** anomaly 仅是 higher cocycle 的候选输入。  
**Files or passages still using the old form:** <code>notes/loop_02.tex</code> 及 future holonomy drafts 需审计。

### Rejected formulation X-11

**Earlier formulation:** figure-eight relator 在 generic \(t\) 下必须映到 identity，故其 translation polynomial 已是 knot invariant。  
**Problem:** 计算首先定义在自由群 words 上；要下降到 knot group representation，需满足 relator image 为 identity。  
**Counterexample, contradiction, or missing hypothesis:** generic \(t\) 下 translation coordinate 为 \(-\Delta_{4_1}(t)\)，并不自动为零。  
**Replacement formulation:** 把它保留为 presentation-dependent word calculation，并明确有效 parameter locus 与 normalization。  
**Files or passages still using the old form:** <code>knots/knots_01.tex</code>、<code>knots/results.tex</code>。

## 8. Decision register

| ID | Decision | Status | Consequence | Paper/file affected |
|---|---|---|---|---|
| D-1 | knot complexity 归因于 finite-strand braid monodromy | adopted | \(E_{\log}\) 负责 deck history，不替代 braid | Paper III |
| D-2 | order-4 event 移入 \(D^2\)-filling | adopted | boundary Tube 与 branched surface 分层 | Paper III / Tube notes |
| D-3 | Markov quotient 作为 invariant 的必要筛子 | adopted | 下降前只称 presentation datum | Paper III / knot notes |
| D-4 | scalar additive 与 ordinary affine torsion collapse 写成 no-go 结果 | adopted | 缩小搜索空间 | Paper III |
| D-5 | twisted 搜索优先检查 \(T_{\mathrm{coef}}=t^{-1}\) | provisionally adopted | 首个有限计算有明确靶点 | Paper III |
| D-6 | two-probe 使用 Lawrence 型无序配置空间作为基准 | provisionally adopted | 需 AEG-specific local system | Paper III |
| D-7 | distinguished spine 的数据先称 annular/framed | adopted | 不提前声称 ordinary knot invariant | Paper III |
| D-8 | higher anomaly 仅作候选，不作已成 associator | adopted | 需 coherence theorem | Paper III / beyond |
| D-9 | Paper I 不发展 braids、Markov 或 knot invariant | adopted，来自 authoritative scope | 仅保留必要接口 | Paper I |
| D-10 | 共振 torsion 类非零 | unresolved | 需有限域 cohomology 计算 | Paper III |

### Adopted

- 区分 finite braid history 与 logarithmic deck history。
- 区分 boundary tube、branched filling 与 boundary closure。
- 区分 braid-level strength、Markov descent 与 knot-level strength。
- 在证明不变性前使用 \(\mathcal D_{\mathrm{AEG}}\) 而非 \(\mathcal I_{\mathrm{AEG}}\)。
- 把两个 collapse 结果作为下一稿的硬边界。

### Rejected

- countable sheets 自动产生任意 knot。
- raw scalar torsion 自动给出新 invariant。
- non-flatness 自动产生 associator。
- 更强 braid representation 自动意味着更强 knot invariant。

### Deferred

- 完整 AEG Tube category。
- two-probe homology 的严格版本。
- nonabelian \(\operatorname{PGL}_2\) holonomy。
- higher-categorical filling theory。

### Still open

- 共振 twisted torsion 是否非 exact。
- AEG local system 是否检测 Burau kernel。
- 是否存在双向 Markov normalization。
- 是否能区分 Alexander/Burau 层相同的 knots。

## 9. Mathematical dependency map

### 9.1 Imported nodes

\[
\begin{aligned}
\mathrm{A1}&:\ \text{affine composition law},\\
\mathrm{A4}&:\ \text{elementary arithmetic torsion},\\
\mathrm{T7}\Rightarrow\mathrm{Z2}&:\ \text{regular zero-locus rigidity},\\
\mathrm{Z3}\to\mathrm{Z5}\Rightarrow\mathrm{T8}\Rightarrow\mathrm{Z6}
&:\ \text{singular definition, families, total zero set, properness warning},\\
\mathrm{T15}\Rightarrow\mathrm{T16}\to\mathrm{T17}
&:\ \text{horizontal curvature and local-global torsion interface}.
\end{aligned}
\]

### 9.2 Modified or clarified nodes

- Z6 is strengthened editorially as a mandatory gate: smooth total zero set does not imply global tube triviality.
- A4/T17 are not knot-invariance nodes; their affine torsion formulas may feed candidate decorations only after separate descent.
- T15/T16 supply curvature language but do not imply a flat or coherent braid connection.
- Z3/Z5/T8 do not imply discriminant stratification, braided filling, or knot invariance.

### 9.3 New candidate nodes

\[
\begin{aligned}
\mathrm{CAND\text{-}B1}&:\ \text{boundary root braid from }\gamma:S^1\to\mathcal P_n^{\mathrm{sf}},\\
\mathrm{CAND\text{-}B2}&:\ \text{simple discriminant branch model }w^2=\tau,\\
\mathrm{CAND\text{-}N1}&:\ \text{scalar additive collapse},\\
\mathrm{CAND\text{-}N2}&:\ \text{fixed-multiplier affine torsion collapse},\\
\mathrm{CAND\text{-}N3}&:\ \text{twisted resonant cohomology computation},\\
\mathrm{CAND\text{-}M1}&:\ \text{AEG Markov descent theorem},\\
\mathrm{CAND\text{-}S1}&:\ \text{Alexander/Burau non-collapse theorem}.
\end{aligned}
\]
这些名称只供本笔记引用，不得视为已写入 <code>03-theorem-dependency-graph.md</code>。

### 9.4 Forbidden dependencies

\[
\begin{aligned}
\mathrm{T8}&\ -/\!\!\to\ \text{global tube triviality},\\
\mathrm{Z6}&\ -/\!\!\to\ \text{knot invariant},\\
\mathrm{A4}&\ -/\!\!\to\ \text{nontrivial quandle class},\\
\mathrm{T15/T16}&\ -/\!\!\to\ \text{flat braid connection},\\
\text{countable lifts}&\ -/\!\!\to\ \text{arbitrary braid complexity},\\
\text{Burau-kernel detection}&\ -/\!\!\to\ \text{knot-level separation},\\
\text{RIII defect}&\ -/\!\!\to\ \text{coherent associator}.
\end{aligned}
\]

## 10. Paper-series allocation

| Material | Destination | Status | Dependency | Re-entry condition |
|---|---|---|---|---|
| affine composition and torsion identities | Paper I | PROVED WITH STATED HYPOTHESES | A1, A4 | conventions audited |
| regular zero-locus and singular-AES interface | Paper I | STANDARD CONSEQUENCE REQUIRING AN IN-PAPER PROOF / STRUCTURAL PROPOSAL | T7, Z2, Z3 | retain hypotheses |
| minimal parameter-family/total-zero-set interface | Paper I | STANDARD CONSEQUENCE REQUIRING AN IN-PAPER PROOF | Z5, T8, Z6 | properness warning explicit |
| analytic kernels, boundary-value theory | Paper II | OPEN PROBLEM | Paper I analytic interface | no migration from this note |
| \(E_k\), \(E_{\log}\), discriminant strata | Paper III | STRUCTURAL PROPOSAL / OPEN PROBLEM | Z3, Z5 | definitions fixed |
| Tube, filling, monodromy, braids, threading | Paper III | STRUCTURAL PROPOSAL | T8, Z6 | topology and properness proved |
| Markov-normalized knot invariant | Paper III | OPEN PROBLEM | braid action + descent | isotopy and stabilization proof |
| beyond Alexander/Burau comparison | Paper III | OPEN PROBLEM | true closure invariant | explicit separation benchmark |
| projective condensation and complexity | Paper IV | OPEN PROBLEM | projective nodes | 本讨论不新增结论；按 Paper IV 权威节点另行处理 |
| coherent 2-holonomy / higher associator | Beyond Papers I–IV or late Paper III | STRUCTURAL PROPOSAL | explicit anomaly + coherence | pentagon/hexagon or 2-connection theorem |

### Paper I

Paper I 必须只提供：affine cocycle/torsion、contact/horizontal curvature，以及 regular/singular zero geometry 的最小接口。它必须保留 T7、Z2、Z3、Z5、T8、Z6 的既有状态与 hypotheses。braids、knots、Markov moves、\(E_{\log}\) 分类和新 knot invariant 不得成为 Paper I 主理论；最多在结尾给出指向 Paper III 的一句前向说明。

### Paper II

本讨论不向 Paper II 迁移 knot 内容。若未来 arithmetic holomorphic filling、Poisson/Green kernel 或 boundary regularity 成为构造输入，其分析理论由 Paper II 所有，但 braid/Markov 结论仍属于 Paper III。

### Paper III

Paper III 拥有 discriminant、\(E_k\)、\(E_{\log}\)、Tube、branched filling、monodromy、braids、threading、Markov descent 与 knot comparison。本文所有 proposal、conjecture、no-go theorem 和计算路线均应在 Paper III 内组织。

### Paper IV

本讨论不推出 projective condensation 或 complexity 结论。不得从 braid noncommutativity、negative curvature 或 knot complexity 跳到算法复杂度。

### Beyond Papers I–IV

若 RIII anomaly 需要真正的 bicategory、2-connection、surface holonomy 或 relation-level semantics，且无法在 Paper III 内自包含，则另立后续项目，不提前挤入当前四篇架构。

## 11. Repository source map

| Source file | Relevant material | Current status | Target destination | Required action |
|---|---|---|---|---|
| <code>restructure/00-authoritative-scope.md</code> | Paper III 拥有 Tube/knot | authoritative | 全系列 | 保持不改 |
| <code>restructure/03-theorem-dependency-graph.md</code> | A1, A4, T7, Z2, Z3, Z5, T8, Z6, T15–T17 | authoritative | 全系列 | 本任务不改；候选节点另候审批 |
| <code>restructure/04-current-to-target-map.md</code> | zero set 到 knot invariant 的七层区分 | authoritative | Paper III | 用作迁移门槛 |
| <code>restructure/05-mathematical-status.md</code> | items 74–81 及 R8/R9 exclusions | authoritative | Paper III | 保持状态词 |
| <code>restructure/08-open-questions.md</code> | OQ-037—OQ-046 | authoritative issue register | Paper III | 仅交叉引用，不在本任务修改 |
| <code>knots/knots_01.tex</code> | figure-eight word \(abbbaBAAB\)，translation \(-\Delta_{4_1}\) | COMPUTATIONALLY VERIFIED EXAMPLE | Paper III | 审计 descent 与 parameter locus |
| <code>knots/knots_03.tex</code> | reverse-word torsion 与 \(\Delta(t)(t^K-1)\) 型因子 | presentation-dependent computation | Paper III / archive | 保留计算，重写 invariant 语言 |
| <code>knots/results.tex</code> | knot/torsion 结果汇总 | mixed, requires audit | Paper III | 逐条重标 status |
| <code>notes/note_02.tex</code> | multi-zero/Tube 动机 | exploratory | Paper III | 抽取，保留 provenance |
| <code>notes/note_03.tex</code> | singular/tube extensions | exploratory | Paper III | 审计 regular/singular 边界 |
| <code>notes/note_11.tex</code> | torsion、Fox/cohomology 强解释 | overstated in places | Paper III / Paper I input | 保留公式，收缩 intrinsic invariant 主张 |
| <code>notes/note_13.tex</code> | logarithmic/tube 几何 | exploratory | Paper III | 对照 deck-cover 解释重写 |
| <code>notes/loop_02.tex</code> | loops、holonomy、relation-level 动机 | exploratory | Paper III / beyond | 不把 non-flatness 当 coherence |
| <code>paper4p/aeg.tex</code>、<code>sections/sec04.tex</code> | current foundational geometry | current paper source | Paper I | 不引入 knot 主理论 |

## 12. Proof obligations

### PO-1: AEG Tube 的严格定义与范畴

**Target statement:** 定义 \(\mathfrak T\) 的 admissible objects、morphisms、gauge equivalence、boundary 与 filling。  
**Known special cases:** 经典 braided mapping tori 和 braided surfaces。  
**Available argument:** §3 的数据包与 forgetful skeleton。  
**Missing step:** AEG fields 的 gluing、regularity 与 equivalence。  
**Required hypotheses:** fiber smoothness、assignment regularity、connection convention、properness。  
**Dependencies:** Z3, Z5, T8, Z6, T15。  
**Failure consequence:** 只能讨论例子，无法陈述 presentation theorem。  
**Recommended next action:** 写一份 definition comparison note，给出最小对象与三个例子。

### PO-2: Proper tube theorem

**Target statement:** 在明确 properness/compact-fiber 条件下，total zero set 在参数区间或圆上给出 locally trivial tube。  
**Known special cases:** Ehresmann 型标准结论。  
**Available argument:** T8 的 smooth total zero set 与 Z6 warning。  
**Missing step:** 精确 map、properness、boundary behavior。  
**Required hypotheses:** smooth submersion、properness，必要时 compactness。  
**Dependencies:** Z5, T8, Z6。  
**Failure consequence:** 无法从 smooth zero surface 进入 tube 层。  
**Recommended next action:** 把 Z6 写成带假设的 lemma/proposition。

### PO-3: Discriminant and local branch theorem

**Target statement:** AEG family 的 simple discriminant crossings 具有 \(w^2=\tau\) 正规形并诱导 half-twist。  
**Known special cases:** 一般复多项式族。  
**Available argument:** 标准判别式局部模型。  
**Missing step:** AEG regularity 与 chart compatibility。  
**Required hypotheses:** simple double root、横截性、其余 roots simple。  
**Dependencies:** Z3, Z5。  
**Failure consequence:** order-4 filling 解释仍只是类比。  
**Recommended next action:** 写出局部系数坐标证明并明确实/复切片。

### PO-4: Logarithmic-cover theorem

**Target statement:** 给定 \(E_{\log}\) 模型的 sheets 确由指定有限零结构的 deck lifts 组成，并刻画单 probe 的 winding。  
**Known special cases:** 标准无限循环覆盖。  
**Available argument:** angular coordinate lifting。  
**Missing step:** AEG assignment 与 completion 的严格定义。  
**Required hypotheses:** cover map、deck action、singular spine/domain exclusions。  
**Dependencies:** Z3；Paper III definitions。  
**Failure consequence:** “可数 sheets”仍可能含糊。  
**Recommended next action:** 对一个明确模型写 covering-space proposition。

### PO-5: Scalar collapse integration

**Target statement:** R-1 以全仓库 braid conventions 陈述。  
**Known special cases:** §4.7 已完整证明。  
**Available argument:** braid abelianization。  
**Missing step:** 与 stabilization normalization、orientation、multi-component wording对齐。  
**Required hypotheses:** 无状态交换群同态。  
**Dependencies:** 无 AEG 深层依赖。  
**Failure consequence:** 未来可能重复搜索已被排除的标量量。  
**Recommended next action:** 独立短注并加入测试例。

### PO-6: Affine collapse convention audit

**Target statement:** R-2、R-3 在固定 chronological composition 与 right/left conjugation convention 下成立。  
**Known special cases:** §4.8。  
**Available argument:** 直接计算。  
**Missing step:** 与 A1/A4 的 repository convention 全面对照。  
**Required hypotheses:** coefficient ring、单位 multiplier、符号约定。  
**Dependencies:** C0, A1, A4。  
**Failure consequence:** 参数 \(t\) 或符号可能倒置。  
**Recommended next action:** 用 symbolic algebra 同时生成左右 convention 表。

### PO-7: Resonant twisted cohomology

**Target statement:** 判定 \(T_{\mathrm{coef}}=t^{-1}\) 时 \([\kappa_t]\) 是否非零。  
**Known special cases:** 非共振且差可逆时 exact。  
**Available argument:** §4.9 给出 cocycle 与候选 primitive。  
**Missing step:** 计算具体 quandle chain complex/cohomology quotient。  
**Required hypotheses:** 有限环/域、module action、normalization 与 region convention。  
**Dependencies:** PO-6。  
**Failure consequence:** twisted route 可能再次 collapse。  
**Recommended next action:** 对小素数 \(p\) 枚举 \(t\in\mathbb F_p^\times\)，从 \(p=3,5,7\) 开始。

### PO-8: RIII anomaly verification and interpretation

**Target statement:** 独立验证 R-5，并判断是否能扩展为 normalized 3-cocycle。  
**Known special cases:** 显式 defect 公式；\(q=r\)、\(r=1\)、\(\kappa=0\) 时消失。  
**Available argument:** 手算代数。  
**Missing step:** symbolic regression、cocycle closure、component/region state model。  
**Required hypotheses:** right conjugation、单位 multiplier。  
**Dependencies:** A1, A4, PO-6。  
**Failure consequence:** higher route缺少可靠种子。  
**Recommended next action:** 建立 property-based finite-field tests。

### PO-9: Braid action from AEG data

**Target statement:** \(\rho_n^{\mathrm{AEG}}\) 满足 braid relations并跨 \(n\) 相容。  
**Known special cases:** Burau、Lawrence、KZ–Kohno classical models。  
**Available argument:** 仅有候选 local operators/holonomy。  
**Missing step:** Yang–Baxter 或 flatness/coherence proof。  
**Required hypotheses:** precise state space、connection/local system、gauge action。  
**Dependencies:** PO-1、PO-3、PO-7 或 two-probe construction。  
**Failure consequence:** 还不能称 braid invariant。  
**Recommended next action:** 先在 \(B_3\) 验证 \(\sigma_1\sigma_2\sigma_1=\sigma_2\sigma_1\sigma_2\)。

### PO-10: Two-probe homological definition

**Target statement:** 构造 braid-equivariant \(\mathcal L_{\mathrm{AEG}}\) 及相应的正确 homology theory。  
**Known special cases:** Lawrence–Krammer–Bigelow。  
**Available argument:** multi-probe 动机。  
**Missing step:** ordered/unordered、relative/Borel–Moore、cover 与 boundary conditions 的选择。  
**Required hypotheses:** finite-generation 与 equivariance。  
**Dependencies:** PO-1、PO-4。  
**Failure consequence:** two-probe 只是比喻或重现 classical LKB。  
**Recommended next action:** 先写 \(n=3,m=2\) 的 cellular model。

### PO-11: AEG Markov descent

**Target statement:** 构造在 conjugation 与指定 stabilization moves 下不变的 closure datum。  
**Known special cases:** Markov trace、quandle state sum、categorical trace。  
**Available argument:** §4.6 给出必要形式。  
**Missing step:** stabilization factors、单位 normalization、gauge/spine independence。  
**Required hypotheses:** 一族 \(\rho_n\)、代数嵌入、trace/state-sum compatibility。  
**Dependencies:** PO-9 或 PO-10。  
**Failure consequence:** 结果至多是 braid/annular invariant。  
**Recommended next action:** 在 \(\sigma_1^{\pm1}\) stabilization 上先算局部增量。

### PO-12: Ordinary versus transverse versus annular classification

**Target statement:** 精确说明候选量在哪组 moves 下不变。  
**Known special cases:** ordinary Markov 与 transverse positive Markov theorem。  
**Available argument:** classical criteria。  
**Missing step:** AEG spine、contact framing、negative stabilization 的行为。  
**Required hypotheses:** orientation 和 contact convention。  
**Dependencies:** PO-11。  
**Failure consequence:** invariant 类型被错误命名。  
**Recommended next action:** 制作 move-by-move audit table。

### PO-13: Burau-level and knot-level non-collapse

**Target statement:** 先检测显式 Burau kernel element，再给出 closure 后 Alexander/Burau 层相同而 AEG 值不同的 knots。  
**Known special cases:** \(B_5\) 中存在显式 Burau kernel element；相同 Alexander polynomial 的 knot pairs 已知。  
**Available argument:** benchmark strategy。  
**Missing step:** 已下降的 AEG invariant 与可重复计算。  
**Required hypotheses:** PO-11 完成。  
**Dependencies:** PO-9/10, PO-11。  
**Failure consequence:** 不能声称“beyond Alexander/Burau”。  
**Recommended next action:** 先做 braid-level kernel test，明确不把它当最终证明。

### PO-14: Higher coherence

**Target statement:** 若保留 anomaly，构造满足 pentagon/hexagon 或 2-connection coherence 的 higher transport，并证明 filling independence。  
**Known special cases:** flat KZ–Kohno 与既有 quasi-braided frameworks。  
**Available argument:** \(\mathfrak A_\kappa\) 候选。  
**Missing step:** 几乎全部 coherence 数据。  
**Required hypotheses:** 明确 2-category、associator、surface composition。  
**Dependencies:** PO-8、PO-9。  
**Failure consequence:** non-flat holonomy 只是 path/filling-dependent quantity。  
**Recommended next action:** 在 \(B_3/B_4\) 上先求最小 pentagon obstruction。

## 13. Definition decisions

### DD-1: Tube 的层级

**Competing formulations:** smooth total zero surface；locally trivial fibration；embedded tube；threaded tube。  
**Current evidence:** authoritative map 已明确七层区分，Z6 要求 properness。  
**Recommended default:** 只有满足明确 fibration/properness 条件时使用 tube；否则称 total zero set/surface。  
**Examples that must be tested:** trivial product family、nonproper submersion、simple discriminant crossing。  
**Affected theorem nodes:** Z5, T8, Z6。  
**Blocking level:** P1。

### DD-2: \(E_{\log}\) 的 downstairs 与 cover

**Competing formulations:** 可数独立零面；有限零结构的 logarithmic lifts。  
**Current evidence:** deck-cover 解释与 Burau/Alexander 接口更精确。  
**Recommended default:** 明确 cover map、deck group 与 singular spine，再谈 sheets。  
**Examples that must be tested:** 单 puncture、多个 punctures、completion 后 spine。  
**Affected theorem nodes:** 候选 Paper III nodes。  
**Blocking level:** P1。

### DD-3: Boundary Tube 与 filling

**Competing formulations:** order-4 点在 boundary；order-4 点在 \(D^2\)-filling。  
**Current evidence:** boundary loop 必须避开 discriminant。  
**Recommended default:** boundary 取 \(\mathcal P_n^{\mathrm{sf}}\)，branch events 只在 filling。  
**Examples that must be tested:** \(w^2-\tau\)、三根中两根碰撞、非横截碰撞。  
**Affected theorem nodes:** Z3, Z5；候选 discriminant nodes。  
**Blocking level:** P1。

### DD-4: Presentation datum 的命名

**Competing formulations:** \(\mathcal I_{\mathrm{AEG}}(K)\)；\(\mathcal D_{\mathrm{AEG}}(\beta)\)。  
**Current evidence:** Markov、gauge、spine invariance 未证。  
**Recommended default:** 使用 \(\mathcal D\) 与 braid presentation \(\beta\)。  
**Examples that must be tested:** conjugate braids、正负 stabilization、axis change。  
**Affected theorem nodes:** candidate M1/S1。  
**Blocking level:** P0 for any invariant claim。

### DD-5: Affine conjugation convention

**Competing formulations:** \(y^{-1}xy\)；\(yxy^{-1}\)。  
**Current evidence:** 两者给出 \(t^{-1}\) 与 \(t\) 的不同 Alexander 参数。  
**Recommended default:** 本路线暂用右共轭 \(y^{-1}xy\)，但最终服从 repository C0 convention audit。  
**Examples that must be tested:** generator、inverse crossing、mirror。  
**Affected theorem nodes:** C0, A1, A4。  
**Blocking level:** P1。

### DD-6: Twisted coefficient convention

**Competing formulations:** ordinary cocycle；twisted cocycle；deck action 与 dilation action 的不同识别。  
**Current evidence:** 普通公式不能直接用于 twisted state sum。  
**Recommended default:** 分别记 \(T\) 为 deck transformation、\(T_{\mathrm{coef}}\) 为 coefficient action；写出完整 chain differential。  
**Examples that must be tested:** \(T_{\mathrm{coef}}=1\)、\(t^{-1}\)、零因子。  
**Affected theorem nodes:** candidate N3/M1。  
**Blocking level:** P0 for twisted claims。

### DD-7: Probe 配置空间

**Competing formulations:** ordered \(\operatorname{Conf}_m\)；unordered \(\operatorname{UConf}_m\)；ordinary、relative 或 Borel–Moore homology。  
**Current evidence:** classical Lawrence construction 使用无序配置及适当 twisted homology。  
**Recommended default:** 不预先固定朴素 \(H_m\)；从 \(m=2,n=3\) 的 cellular model 比较选择。  
**Examples that must be tested:** \(m=1\) 恢复 Burau、\(m=2\) 恢复 classical specialization。  
**Affected theorem nodes:** candidate two-probe node。  
**Blocking level:** P2。

### DD-8: Invariant category

**Competing formulations:** ordinary knot；transverse/contact-framed knot；annular braid/solid-torus pattern。  
**Current evidence:** distinguished spine 与 positive-only stabilization 可能保留额外结构。  
**Recommended default:** 按实际不变 move 集合命名，不先承诺 ordinary。  
**Examples that must be tested:** negative stabilization、axis-preserving conjugation、spine change。  
**Affected theorem nodes:** candidate M1。  
**Blocking level:** P0 for naming。

### DD-9: Holonomy versus higher transport

**Competing formulations:** flat connection；projectively flat connection；non-flat 1-connection；coherent 2-connection。  
**Current evidence:** non-flatness 本身破坏 homotopy invariance。  
**Recommended default:** 先计算 curvature 与 RIII defect，再决定是否需要 higher structure。  
**Examples that must be tested:** \(B_3\) relation、central curvature、pentagon cell。  
**Affected theorem nodes:** T15, T16, T17；candidate higher node。  
**Blocking level:** P2。

## 14. Mathematical risks

| Risk | Severity | Affected claim | Detection method | Mitigation |
|---|---|---|---|---|
| 缺少 properness | High | smooth zero surface \(\Rightarrow\) tube | 检查 map 是否 proper、fibers 是否 compact | 以 Z6 为硬门槛 |
| regular/singular 混淆 | High | boundary braid 与 branch filling | 检查是否穿过 \(\Delta\) | 分开 \(S^1\) 与 \(D^2\) 定义 |
| cover/downstairs 混淆 | High | countable sheets | 写出 quotient 与 deck action | 只把净层号称 winding |
| composition-order/sign 错误 | High | affine quandle、torsion、RIII defect | 左右 convention 双算与 symbolic test | 锁定 C0 后迁移 |
| assignment \(a\) 与 translation \(a\) 冲突 | Medium | affine formulas | notation lint | translation 改用 \(u,v,w\) |
| 普通与 twisted coboundary 混淆 | High | resonant class | 写完整 chain differential | 区分 \(T\) 与 \(T_{\mathrm{coef}}\) |
| 共振“证法失效”误写成“非零” | High | C-2 | 直接算 cohomology quotient | 未算前保持 OPEN |
| braid-level 误写成 knot-level | Critical | beyond Burau claim | 分别做 kernel 与 closure tests | Markov descent 先于 knot comparison |
| spine/axis dependence 被遗忘 | High | ordinary knot invariant | negative stabilization 与 axis change | 准确命名 annular/transverse |
| metric/gauge dependence | High | holonomy 与 zero divisor weights | gauge-change calculation | 只保留 cohomology class 或证明 normalization |
| non-flatness 类比被当证明 | Critical | associator/higher invariant | pentagon、hexagon、fake-flatness tests | 无 coherence 不称 invariant |
| holomorphic filling 过度一般化 | High | all knots have AEG realization | 检查 quasipositivity restrictions | 区分 smooth 与 holomorphic category |
| 计算样例过度推广 | High | figure-eight/Alexander claims | 更换 presentation 与 Markov move | 标记 COMPUTATIONALLY VERIFIED EXAMPLE |
| projective category偷偷替代普通算术 | Medium | singularity removal | domain audit | 明确 poles 与 admissibility |
| 文献结果表述过强 | Medium | braided surfaces existence | 对照原定理 hypotheses | 使用精确措辞并给 primary citations |

## 15. Open questions

### OQ-037 — Discriminant locus

**Priority:** P3；**Blocks Paper I:** No。  
需要明确 AEG coefficient/assignment family 的 discriminant 定义、stratification 与 transversality。所需证据为可计算局部模型及与 Z3/Z5 的接口。目标 Paper III。对应 <code>restructure/08-open-questions.md</code> OQ-037。

### OQ-041 — Proper tube theorem

**Priority:** P3；**Blocks Paper I:** No，若 Z6 warning 保留。  
需要给出 total zero set 成为 locally trivial tube 的充分条件。目标 Paper III；对应 OQ-041。

### OQ-042 — Braid lift and monodromy

**Priority:** P3；**Blocks Paper I:** No。  
需要证明 AEG family 的 root/multisection monodromy 定义 braid，并处理 gauge 与 singular spine。目标 Paper III；对应 OQ-042。

### OQ-043 — Threading datum

**Priority:** P3；**Blocks Paper I:** No。  
需要定义 probe 与 nodal sheets 的交叉、顺序、接触阶及其 equivalence。目标 Paper III；对应 OQ-043。

### OQ-044 — Markov descent

**Priority:** P3；**Blocks Paper I:** No。  
需要确定 ordinary、transverse 或 annular move set，并证明 normalization。目标 Paper III；对应 OQ-044。

### OQ-045 — Beyond Alexander/Burau

**Priority:** P3；**Blocks Paper I:** No。  
需要一个已经下降的 invariant 以及相同 Alexander/Burau 层的 separation pair。目标 Paper III；对应 OQ-045。

### OQ-046 — Knot invariant status

**Priority:** P3；**Blocks Paper I:** No。  
当前保持 OPEN PROBLEM。只有 presentation、descent 与 invariance theorem 完成后才能更新。目标 Paper III；对应 OQ-046。

### Candidate new open question CQ-1 — Resonant twisted torsion

**Priority:** P2 research；**Blocks Paper I:** No。  
当 \(T_{\mathrm{coef}}=t^{-1}\) 或差为零因子时，\([\kappa_t]\) 是否非零？需要有限 quandle chain-complex calculation 与 state-sum test。目标 Paper III。**Candidate new open question; not yet added to <code>08-open-questions.md</code>.**

### Candidate new open question CQ-2 — Minimal AEG-specific two-probe deformation

**Priority:** P3；**Blocks Paper I:** No。  
什么是最小 \(\mathcal L_{\mathrm{AEG}}\)，使 two-probe representation 不只是 classical Lawrence specialization？需要 equivariance 与 deformation/non-isomorphism 证据。目标 Paper III。**Candidate new open question; not yet added to <code>08-open-questions.md</code>.**

### Candidate new open question CQ-3 — Spine independence versus transverse refinement

**Priority:** P3；**Blocks Paper I:** No。  
若 negative stabilization 不能归一化，所得量应解释为 transverse、framed 还是 annular invariant？需要 move audit 与 contact/spine change calculation。目标 Paper III。**Candidate new open question; not yet added to <code>08-open-questions.md</code>.**

## 16. Recommended next tasks

### Task 1: 共振 twisted cohomology 的有限计算

**Goal:** 判定小有限域上 \(T_{\mathrm{coef}}=t^{-1}\) 时 \(\kappa_t\) 是否为非零 class。  
**Allowed files:** 新建 Paper III computation note 与独立测试脚本；只读本笔记及 A1/A4 来源。  
**Forbidden files:** Paper I 正文、<code>restructure/00–08</code>。  
**Theorem nodes:** candidate N3。  
**Expected output:** \(p=3,5,7\) 的 normalized chain matrices、cocycle/coboundary ranks、\([\kappa_t]\) 判定和复现实验。  
**Validation:** 两种独立实现或 symbolic + exhaustive enumeration；明确 coefficient convention。  
**Blocking questions:** DD-5、DD-6。

### Task 2: Affine formulas 与 RIII defect 的 convention audit

**Goal:** 对左右共轭、word order、正负 crossing 生成一张完整公式表。  
**Allowed files:** 新 computation note；只读 <code>knots</code>、<code>notes/note_11.tex</code>、A1/A4。  
**Forbidden files:** 主 paper 与 authoritative register。  
**Theorem nodes:** A1, A4, candidate N2。  
**Expected output:** 手算、CAS verification 与 regression tests。  
**Validation:** 随机有限域 property tests。  
**Blocking questions:** repository C0。

### Task 3: Tube/filling 定义比较

**Goal:** 定义 boundary Tube、branched filling、threaded Tube 和 forgetful skeleton。  
**Allowed files:** 新 Paper III definition note。  
**Forbidden files:** Paper I 主文、authoritative graph。  
**Theorem nodes:** Z3, Z5, T8, Z6；candidate B1/B2。  
**Expected output:** 定义、morphism、gauge、三个正例与两个反例。  
**Validation:** \(w^2-\tau\) 与 nonproper family 测试。  
**Blocking questions:** DD-1—DD-4。

### Task 4: Figure-eight 与 reverse-word source audit

**Goal:** 区分自由群 word calculation、knot-group representation locus 与 presentation-dependent torsion。  
**Allowed files:** 新 audit note；只读 <code>knots/knots_01.tex</code>、<code>knots/knots_03.tex</code>、<code>knots/results.tex</code>。  
**Forbidden files:** 原始 notes，除非后续单独授权修改。  
**Theorem nodes:** A1, A4。  
**Expected output:** 假设表、符号表、可保留 example 与必须撤回的 invariant language。  
**Validation:** 独立重算 \(abbbaBAAB\) 与至少一个换 presentation 测试。  
**Blocking questions:** C0、normalization。

### Task 5: Two-probe 最小模型

**Goal:** 在 \(n=3,m=2\) 上构造 AEG-equivariant local system 候选。  
**Allowed files:** 新 Paper III research note 与实验代码。  
**Forbidden files:** Paper I、authoritative graph。  
**Theorem nodes:** candidate two-probe node。  
**Expected output:** ordered/unordered comparison、cover、homology choice、generator matrices。  
**Validation:** 关闭 AEG deformation 时恢复 classical specialization；检查 braid relation。  
**Blocking questions:** DD-2、DD-7。

### Task 6: Markov move audit harness

**Goal:** 对任一候选 \(\mathcal D_{\mathrm{AEG}}\) 自动检查 conjugation、正/负 stabilization 与 axis-preserving moves。  
**Allowed files:** Paper III test data 与脚本。  
**Forbidden files:** 在 descent 证明前不得改摘要声称 invariant。  
**Theorem nodes:** candidate M1。  
**Expected output:** move-by-move failure table与 normalization equations。  
**Validation:** unknot 的多个 braid presentations 与已知 classical invariant baseline。  
**Blocking questions:** DD-4、DD-8。

### Task 7: 非塌缩 benchmark

**Goal:** 在 Markov descent 完成后，按 braid-level 和 knot-level 两阶段测试。  
**Allowed files:** Paper III experiment note 与可复现数据。  
**Forbidden files:** 未完成 PO-11 时不得发布“beyond Alexander”结论。  
**Theorem nodes:** candidate S1。  
**Expected output:** 显式 Burau kernel test；随后选择相同 Alexander polynomial/module 的 knot pairs。  
**Validation:** 与 Jones/HOMFLY、quandle cocycle、twisted Alexander 等已知 invariants 比较。  
**Blocking questions:** PO-11。

推荐立即执行 Task 1。它范围小、可否证性强，并直接决定 twisted torsion 路线是否值得扩展。

## 17. Source trace

| Note section or claim | Discussion source | Related repository source |
|---|---|---|
| finite braid monodromy 与 logarithmic winding 分层 | 讨论中的“Tube 如何容纳不同纽结”与“穿线有两层” | <code>notes/note_02.tex</code>, <code>note_13.tex</code>, <code>restructure/04-current-to-target-map.md</code> |
| boundary/filling/order-4 correction | 讨论中的“order-4 分支应当出现在 Tube filling 中” | Z3, Z5, T8, Z6；Tube notes |
| classical originality boundary | 讨论中的“最接近的既有数学对象” | <code>restructure/00-authoritative-scope.md</code>, Paper III allocation |
| Markov sieve | 讨论中的“成败点应写成三次下降” | <code>restructure/05-mathematical-status.md</code> items 78–81 |
| scalar additive collapse | 讨论中的第一条 no-go 与后续红队修正 | 本讨论新证明 |
| affine subquandle/coboundary | 讨论中的第二条 no-go 与公式复核 | A1, A4；<code>notes/note_11.tex</code> |
| twisted resonance | 后续红队核查对普通/twisted coboundary 的修正 | 本讨论新计算；twisted quandle literature |
| variable multiplier anomaly | 讨论中的 RIII defect 与单分支限制 | 本讨论新计算 |
| two-probe route | 讨论中的 multi-probe 配置空间路线 | Paper III open program；Lawrence/Bigelow literature |
| figure-eight caveat | 讨论后的 repository source audit | <code>knots/knots_01.tex</code>, <code>knots/results.tex</code> |
| paper allocation | 讨论结论与 task-required restructuring audit | <code>restructure/00–08</code> |
| proof and definition registers | 本次讨论压缩 | 本笔记 §§12–16 |

### Primary literature used for positioning

- J. W. Alexander, “A Lemma on Systems of Knotted Curves,” 1923. [DOI](https://doi.org/10.1073/pnas.9.3.93)
- E. Artin, “Theorie der Zöpfe,” 1925. [DOI](https://doi.org/10.1007/BF02950718)
- A. A. Markoff, “Über die freie Äquivalenz geschlossener Zöpfe,” publication year 1936. [MathNet](https://www.mathnet.ru/eng/sm5359)
- E. Fadell and L. Neuwirth, “Configuration Spaces,” 1962. [DOI](https://doi.org/10.7146/math.scand.a-10517)
- Lee Rudolph, “Algebraic Functions and Closed Braids,” 1983. [DOI](https://doi.org/10.1016/0040-9383(83)90031-9)
- Lee Rudolph, “Braided Surfaces and Seifert Ribbons for Closed Braids,” 1983. [DOI](https://doi.org/10.1007/BF02564622)
- Werner Burau, “Über Zopfgruppen und gleichsinnig verdrillte Verkettungen,” 1936. [DOI](https://doi.org/10.1007/BF02940722)
- Vaughan F. R. Jones, “Hecke Algebra Representations of Braid Groups and Link Polynomials,” 1987. [DOI](https://doi.org/10.2307/1971403)
- Vladimir G. Turaev, “The Yang–Baxter Equation and Invariants of Links,” 1988. [DOI](https://doi.org/10.1007/BF01393746)
- J. S. Carter et al., “Quandle Cohomology and State-Sum Invariants of Knotted Curves and Surfaces,” 2003. [DOI](https://doi.org/10.1090/S0002-9947-03-03046-0)
- J. S. Carter, M. Elhamdadi, and M. Saito, “Twisted Quandle Homology Theory and Cocycle Knot Invariants,” 2002. [DOI](https://doi.org/10.2140/agt.2002.2.95)
- Ruth J. Lawrence, “Homological Representations of the Hecke Algebra,” 1990. [DOI](https://doi.org/10.1007/BF02097660)
- Stephen J. Bigelow, “The Burau Representation Is Not Faithful for \(n=5\),” 1999. [DOI](https://doi.org/10.2140/gt.1999.3.397)
- Stephen J. Bigelow, “Braid Groups Are Linear,” 2001. [DOI](https://doi.org/10.1090/S0894-0347-00-00361-1)
- Daan Krammer, “Braid Groups Are Linear,” 2002, pp. 131–156. [DOI](https://doi.org/10.2307/3062152)
- Toshitake Kohno, “Monodromy Representations of Braid Groups and Yang–Baxter Equations,” 1987. [DOI](https://doi.org/10.5802/aif.1114)
- S. Yu. Orevkov and V. V. Shevchishin, “Markov Theorem for Transversal Links,” 2003. [DOI](https://doi.org/10.1142/S0218216503002846)

Rudolph 的边界应准确表述为：无极点代数函数产生的 closed braids 恰为 quasipositive closed braids；其 braided-surface 结果不应无条件扩写为所有 \(B^4\) 内嵌曲面。

## 18. Final working position

目前已经理解：同一局部 Tube 容纳不同纽结的机制是 finite multisection 的 braid monodromy；\(E_{\log}\) 的可数 sheets 主要记录 logarithmic cover 中的整数 winding。嵌入 boundary braid 必须避开判别式，order-4 重联属于 \(D^2\)-filling 的 simple branch event，而非 boundary Tube 的正则点。

已经证明的新增边界有两条：无状态、交换值、拼接可加的 braid 标量只因子化到 writhe；固定 multiplier 的 affine 子 quandle 是 Alexander quandle，raw torsion 在普通系数下为 coboundary。另已证明它在所选 twisted convention 下仍是 cocycle，并在非共振可逆情形保持 exact。共振 \(T_{\mathrm{coef}}=t^{-1}\) 只留下一个开放窗口，尚未证明非平凡。

仍属 proposal 或 open problem 的，是 AEG-decorated Tube、two-probe local system、nonabelian holonomy、Markov-compatible closure 与 higher associator。尤其不能从更强的 braid representation 直接推出更强的 knot invariant，也不能把 spine-dependent 数据误称为普通 \(S^3\) knot invariant。

下一阻塞步骤是小有限域上的共振 twisted-cohomology 计算；若得到非零类，再构造完整 state sum 并逐项检验 Markov moves。若该路线再次塌缩，则转向 AEG-specific two-probe local system。后续发展明确属于 Paper III；Paper I 只保留 affine torsion、contact curvature 与 regular/singular zero geometry 的输入接口。
