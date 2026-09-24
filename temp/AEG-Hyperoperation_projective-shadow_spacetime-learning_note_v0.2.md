# AEG / Hyperoperation：历史商、时空复杂度与 Projective Shadow
## Research checkpoint v0.1 — 2026-08-19

> 本笔记记录从“万有覆叠作为动力学分析工具”转向“由万有覆叠与相对过程几何反向设计学习机制”之后的一轮推导。
>
> 当前核心线索：
>
> \[
> \text{History Quotient}
> \to
> \text{Spacetime-Optimal Materialization}
> \to
> \text{Rank Raising}
> \to
> \text{Process-Metric Compression}
> \to
> \text{Finite Lie Shadow + Residual}.
> \]

---

## 1. Spacetime-Optimal History Quotient Principle

给定历史空间 \(\mathcal H\) 与任务 \(Q\)，一种状态表示是历史的商：

\[
R:\mathcal H\to Z.
\]

历史 \(h_1,h_2\) 若对所有允许的未来 continuation 都不可区分，则可定义 task-equivalence：

\[
h_1\sim_Q h_2.
\]

最粗的 future-sufficient state 为：

\[
Z_Q=\mathcal H/\sim_Q.
\]

但 semantic minimality 不等于 computational optimality。一个状态若压缩过度，可能在每次更新或查询时付出很高的 reconstruction cost。

因此 admissible state representation 还必须满足 recursive closure：

\[
q(h\cdot a)=F(q(h),a).
\]

当前工作原则：

\[
R^*
=
\arg\min_{R\text{ sufficient, recursive}}
V_{\mathrm{ST}}(R),
\]

其中第一版可取：

\[
V_{\mathrm{ST}}\approx T_R S_R,
\]

更一般可取：

\[
V_{\mathrm{ST}}=\int S_R(t)\,dt.
\]

若 \(T=T(S)\)，最小化 \(TS\) 的边际条件是：

\[
\frac{d\log T}{d\log S}=-1.
\]

它表达的不是数值上的 \(T=S\)，而是空间边际代价与时间边际收益相平衡。

---

## 2. Benchmark I：Four-Sheet Wrapped Process

离散圆周：

\[
X_N=\mathbb Z/N\mathbb Z,
\qquad N=16.
\]

离散万有覆叠：

\[
\widetilde X=\mathbb Z.
\]

真实 predictive state：

\[
z_t=\ell_t\bmod 64,
\]

普通 observation：

\[
x_t=\ell_t\bmod 16.
\]

真实 sheet residue：

\[
r_t=\left\lfloor\frac{\ell_t}{16}\right\rfloor\bmod4.
\]

未来输出分布依赖 \(r_t\)，因此普通 \(X_N\) 商掉了 future-relevant history。

### 已验证的结构

1. \(X_N\) 不是 predictive sufficient。
2. 四重覆盖 \(\mathbb Z/64\mathbb Z\) recursively sufficient。
3. 在非退化 output kernel 下，四重覆盖是最粗 exact predictive cover。
4. subgroup search 可从候选 \(m\) 中恢复 \(m_*=4\)。
5. 不预知 \(m\) 的 future-distinguishability + congruence partition refinement 可从较大的 workspace 中恢复 64 个 predictive states。

因此：

\[
\boxed{
\text{future distinguishability}
+
\text{recursive congruence}
\Rightarrow
\text{history quotient discovery}.
}
\]

---

## 3. Benchmark II：Lifted Random-Access Memory

在已经找到正确 predictive state \(z_t\) 之后，考虑长度 \(H\) 的历史随机访问。

保存 \(k\) 个均匀 checkpoints：

\[
S(k)=1+k,
\]

最坏 replay time：

\[
T(k)=1+\left\lceil\frac Hk\right\rceil.
\]

连续近似：

\[
C_{\mathrm{ST}}(k)
=
(1+k)\left(1+\frac Hk\right)
=
H+1+k+\frac Hk.
\]

由 AM-GM：

\[
C_{\mathrm{ST}}
\ge
(\sqrt H+1)^2,
\]

最优：

\[
\boxed{k^*=\sqrt H.}
\]

所以在 checkpoint model 中：

\[
S\sim\sqrt H,
\qquad
T\sim\sqrt H.
\]

### 非均匀 query distribution

若历史位置 \(\tau\) 的访问概率密度为 \(p(\tau)\)，checkpoint density 为 \(\rho(\tau)\)，则 expected replay 的连续近似为：

\[
E[T_{\mathrm{replay}}]
\approx
\frac12\int\frac{p(\tau)}{\rho(\tau)}\,d\tau,
\]

约束：

\[
\int\rho(\tau)\,d\tau=k.
\]

变分给：

\[
\boxed{
\rho^*(\tau)\propto\sqrt{p(\tau)}.
}
\]

这是当前得到的第一条 memory allocation law。

---

## 4. Benchmark III：Rank Raising 与 process-metric compression

取 primitive：

\[
A:x\mapsto x+1.
\]

只允许 \(A\) 时：

\[
|A^n|=n.
\]

加入尺度过程：

\[
M_b:x\mapsto bx,
\]

则：

\[
M_b A M_b^{-1}=A^b.
\]

因此：

\[
A^n
\]

可以按 base-\(b\) 递归编译成长度：

\[
O(\log n)
\]

的 process word。

这说明：

\[
\boxed{
\text{增加 representation primitive}
\Rightarrow
\text{改变 process-space word metric}.
}
\]

时间复杂度可以定义为：

\[
T_\Sigma(g)=d_\Sigma(e,g),
\]

其中 \(\Sigma\) 是当前 primitive library。

因此 representation learning 可被理解为：

\[
\boxed{
\text{learning a process metric in which useful computations become short}.
}
\]

---

## 5. Continuous rank-raising operator

设连续 process vector field 为 \(X\)，ruler \(A\) 满足：

\[
X(A)=1.
\]

定义：

\[
\boxed{
\mathcal R(X,A)
=
(Y,B)
=
(AX,\log A).
}
\]

则：

\[
[X,Y]
=
[X,AX]
=
X(A)X
=
X,
\]

且：

\[
Y(B)
=
AX(\log A)
=
1.
\]

因此：

\[
\boxed{
(X,A)
\mapsto
(AX,\log A)
}
\]

构成一个显式 rank-raising recursion。

从：

\[
X_0=\partial_x,
\qquad
A_0=x
\]

开始：

\[
X_1=x\partial_x,
\qquad
A_1=\log x,
\]

\[
X_2=x\log x\,\partial_x,
\qquad
A_2=\log\log x,
\]

\[
X_3=x\log x\log\log x\,\partial_x,
\quad\ldots
\]

并且始终：

\[
[X_r,X_{r+1}]=X_r.
\]

这给 rank raising 一个计算解释：

\[
\boxed{
\text{rank raising}
=
\text{fast-forward operator construction}.
}
\]

---

## 6. Exact tower 的 Lie closure 很快变成无限维

前三个 exact generators：

\[
X_0=\partial_x,
\qquad
X_1=x\partial_x,
\qquad
X_2=x\log x\,\partial_x.
\]

虽然：

\[
[X_0,X_1]=X_0,
\qquad
[X_1,X_2]=X_1,
\]

但：

\[
[X_0,X_2]
=
(\log x+1)\partial_x,
\]

继续：

\[
\operatorname{ad}_{X_0}^{m}X_2
=
(-1)^{m-2}(m-2)!
x^{-(m-1)}\partial_x,
\qquad m\ge2.
\]

因此 exact process algebra 已经产生无穷多个线性独立方向。

结论：

\[
\boxed{
\text{exact Hyperoperation process algebra}
\neq
\text{一个小的有限维 Lie algebra}.
}
\]

有限维 Lie model 必须理解为 shadow / normal form，而不是完整 closure。

---

## 7. 相邻三 rank 的统一正常形

对任意相邻三阶：

\[
(X_r,X_{r+1},X_{r+2}),
\]

取中间 ruler 坐标：

\[
u=A_{r+1}.
\]

因为：

\[
X_{r+1}(u)=1,
\]

所以：

\[
X_{r+1}=\partial_u.
\]

又因为：

\[
X_{r+2}=A_{r+1}X_{r+1},
\]

得到：

\[
X_{r+2}=u\partial_u.
\]

同时：

\[
A_r=e^u,
\]

而：

\[
X_r(A_r)=1,
\]

所以：

\[
X_r=e^{-u}\partial_u.
\]

因此所有相邻三 rank 都具有统一 exact normal form：

\[
\boxed{
X_r=e^{-u}\partial_u,
\qquad
X_{r+1}=\partial_u,
\qquad
X_{r+2}=u\partial_u.
}
\]

---

## 8. 二阶 osculating shadow 自动生成 \(\mathfrak{sl}_2\)

在自然基点：

\[
u=0
\iff
A_r=1
\]

附近：

\[
e^{-u}
=
1-u+\frac12u^2+O(u^3).
\]

于是：

\[
j^2X_r
=
\left(1-u+\frac12u^2\right)\partial_u.
\]

定义二阶 residual mode：

\[
K_r
=
2\left(
j^2X_r
-
j^2X_{r+1}
+
j^2X_{r+2}
\right).
\]

得到：

\[
\boxed{
K_r=u^2\partial_u.
}
\]

所以：

\[
E=\partial_u,
\qquad
H=u\partial_u,
\qquad
F=u^2\partial_u
\]

满足：

\[
[E,H]=E,
\]

\[
[H,F]=F,
\]

\[
[E,F]=2H.
\]

因此：

\[
\boxed{
\text{every adjacent three-rank window}
\Rightarrow
\mathfrak{sl}_2
\text{ 2-jet shadow}.
}
\]

这给此前：

\[
012\rightsquigarrow\widetilde{SL_2\mathbb R}
\]

一个更自然的来源：不是手工选取 projective modes，而是相邻 ruler scaffold 的二阶 osculating geometry。

---

## 9. 为什么二阶恰好特殊？

考虑多项式 vector fields：

\[
\mathcal V_d
=
\operatorname{span}
\{
\partial_u,
u\partial_u,
\ldots,
u^d\partial_u
\}.
\]

有：

\[
[u^i\partial_u,u^j\partial_u]
=
(j-i)u^{i+j-1}\partial_u.
\]

因此：

- \(d=0\)：translation，闭合；
- \(d=1\)：affine，闭合；
- \(d=2\)：projective / \(\mathfrak{sl}_2\)，闭合；
- \(d\ge3\)：一般不闭合，例如
  \[
  [u^2\partial_u,u^d\partial_u]
  =
  (d-2)u^{d+1}\partial_u.
  \]

所以在这一自然的 polynomial-osculating hierarchy 中：

\[
\boxed{
d=2
}
\]

是最后一个有限维闭合层级。

这给 \(\mathfrak{sl}_2\) 作为 finite Lie shadow 一个明确的 maximality 理由。

---

## 10. Projective shadow 不是 exact Lie quotient

需要特别谨慎：

\[
j^2
\]

一般不是从完整 vector-field Lie algebra 到 \(\mathfrak{sl}_2\) 的 Lie algebra homomorphism。

因此正确术语应是：

\[
\boxed{
\text{osculating projective shadow}
}
\]

而不是简单“Lie quotient”。

完整理论需要保存 shadow 之外的 residual。

---

## 11. Schwarzian：shadow 之外的自然 residual

对局部 ruler transition：

\[
f:u\mapsto v,
\]

定义 Schwarzian：

\[
\boxed{
\mathcal S(f)
=
\frac{f'''}{f'}
-
\frac32
\left(\frac{f''}{f'}\right)^2.
}
\]

Möbius transformation 的 Schwarzian 为零。

对任意局部 diffeomorphism \(f\)，在基点存在唯一 Möbius map \(M\) 与 \(f\) 具有相同 2-jet。

因为：

\[
\mathcal S(M)=0,
\]

三阶 mismatch 满足：

\[
\boxed{
f'''(p)-M'''(p)
=
f'(p)\,\mathcal S(f)(p).
}
\]

因此：

\[
f(u)-M(u)
=
\frac{f'(p)\mathcal S(f)(p)}{6}(u-p)^3
+
O((u-p)^4).
\]

所以 Schwarzian 正是 projective shadow 之后第一个 residual。

更强地，给定：

\[
q(u)=\mathcal S(f)(u)
\]

和 2-jet normalization，可通过二阶线性 ODE 重建 \(f\)（等价地，\(f\) 是相应两个独立解之比）。

因此一维 ruler transition 可以概念性拆成：

\[
\boxed{
\text{exact transition}
=
\text{finite }PSL_2\text{ shadow}
+
\text{Schwarzian function}.
}
\]

这可能是“Lie shadow + arithmetic residual”在一维的第一版严格形式。

---

## 12. Hyperoperation rank step 是 constant-Schwarzian transition

相邻 rulers 满足：

\[
u_{r+1}=\log u_r,
\]

反向：

\[
u_r=e^{u_{r+1}}.
\]

计算：

\[
\boxed{
\mathcal S(e^v)=-\frac12,
}
\]

以及：

\[
\boxed{
\mathcal S(\log u)=\frac1{2u^2}.
}
\]

因此在新的 rank coordinate 中，每一次 rank raising 都具有相同的 normalized projective residual：

\[
\boxed{
q_{\rm rank}=-\frac12.
}
\]

这意味着 Hyperoperation tower 可暂时理解成：

\[
\boxed{
\text{a repeated constant-Schwarzian extension of projective shadows}.
}
\]

这一表述目前是工作假说，需要进一步检查 normalization、domain、branch 与 higher-dimensional generalization。

---

## 13. Constant Schwarzian 的三种符号 normal forms

归一化后：

\[
\mathcal S(f)=0
\]

对应 Möbius / projective branch；

\[
\mathcal S(f)=-\frac{a^2}{2}
\]

对应：

\[
f\sim e^{au};
\]

\[
\mathcal S(f)=+\frac{a^2}{2}
\]

对应：

\[
f\sim \tan\frac{au}{2}.
\]

这给出：

\[
\boxed{
0,\quad -, \quad +
}
\]

三种最简单 projective residual 类型。

它与此前 AEG 中反复出现的 flat / hyperbolic / spherical 三支有明显形式相似性，但当前只应作为待验证线索。

---

## 14. 相邻 projective shadows 的 rank atlas

令：

\[
u_r=A_r.
\]

每一个 \(u_r\) ruler coordinate 给出一个 local projective shadow：

\[
\mathfrak p_r
\simeq
\mathfrak{sl}_2.
\]

相邻坐标：

\[
u_{r+1}=\log u_r.
\]

并且：

\[
u_r\partial_{u_r}
=
\partial_{u_{r+1}}.
\]

即：

\[
\boxed{
\text{rank }r\text{ 的 dilation}
=
\text{rank }r+1\text{ 的 translation}.
}
\]

这可能是 rank raising 最简洁的几何表达。

因此高 rank 信息也许不应被压进一个越来越大的有限维 Lie algebra，而应表示为：

\[
\boxed{
\text{a chain / groupoid of finite projective shadows}
+
\text{rank-transition cocycles}.
}
\]

---

## 15. 一个新的 learning / compilation architecture

当前可以提出四层表示：

### Layer A — Semantic Quotient

寻找：

\[
\mathcal H\to Z_Q.
\]

决定“什么历史不能丢”。

### Layer B — Materialization

决定哪些 \(Z_Q\)-states 值得保存：

\[
\min ST.
\]

### Layer C — Rank Raising

对高成本重复过程学习 ruler：

\[
XA=1
\]

并构造：

\[
(X,A)\mapsto(AX,\log A).
\]

决定“什么长过程值得变成新 primitive”。

### Layer D — Shadow / Residual Factorization

对 ruler transition \(f\)：

1. 提取 osculating \(PSL_2\) shadow；
2. 计算 / 学习 Schwarzian residual \(q=\mathcal S(f)\)；
3. 若 \(q\approx0\)，使用 pure projective primitive；
4. 若 \(q\) 近常数，objectify 为 simple rank transition；
5. 若 \(q\) 是低复杂函数，保存 compact residual model；
6. 若 \(q\) 很复杂，再决定增加 rank、保存 history 或使用 learned residual。

这形成一个 self-growing process language：

\[
\boxed{
\text{history}
\to
\text{quotient}
\to
\text{memory}
\to
\text{ruler}
\to
\text{rank}
\to
\text{projective shadow + residual}.
}
\]

---

## 16. 当前关键修正

### 修正 A

不能再把：

\[
012\to\mathfrak{sl}_2
\]

解释为 exact Hyperoperation generator closure。

更准确的是：

\[
\boxed{
012
\to
\text{2-jet projective shadow}
\simeq
\mathfrak{sl}_2.
}
\]

### 修正 B

高 rank 不应期待继续产生一个小的 finite-dimensional global Lie algebra。

更可能的结构是：

\[
\boxed{
\text{ranked exact scaffold}
+
\text{overlapping finite Lie shadows}
+
\text{transition residuals/cocycles}.
}
\]

### 修正 C

“universal cover”仍然重要，但它描述的是 finite Lie shadow 的 canonical global model，而不是完整 arithmetic process geometry。

这与“Lie universal cover 只是 coarse standard shadow”的既有判断一致。

---

## 17. 下一轮优先问题

### P1. Projective-shadow theorem

严格表述并证明：

> 任意按
> \[
> (X,A)\mapsto(AX,\log A)
> \]
> 生成的相邻三-rank window，在中间 ruler coordinate 的自然基点上都有 canonical \(\mathfrak{sl}_2\) second-order osculating shadow。

### P2. Schwarzian completeness

严格整理：

\[
\text{2-jet projective shadow}
+
\mathcal S(f)
\]

在何种局部条件下完整决定 ruler transition。

### P3. Rank cocycle

研究：

\[
\mathcal S(u_r\circ u_{r+1}^{-1})=-\frac12
\]

是否可作为 rank-raising 的 intrinsic characterization，以及 normalization / branch freedom。

### P4. Spacetime model selection

定义候选：

\[
\text{exact},
\quad
\text{affine shadow},
\quad
\text{projective shadow},
\quad
\text{projective + residual},
\quad
\text{next-rank objectification}
\]

的统一 representation cost 与 execution cost。

### P5. First nonlinear learner

从 black-box dynamics 学：

1. ruler；
2. local projective shadow；
3. Schwarzian residual；
4. 自动判断 residual 是否为 constant-Schwarzian；
5. 若是，自动生长 rank primitive。

---

## 18. 当前一句话总结

\[
\boxed{
\text{有限 Lie 几何可能不是完整 Hyperoperation tower 的容器，}
}
\]

而更像是：

\[
\boxed{
\text{每个 rank window 的标准低阶 shadow；}
}
\]

完整结构则由：

\[
\boxed{
\text{ranked projective shadows}
+
\text{Schwarzian transition data}
}
\]

粘合起来。

如果这一方向成立，那么“万有覆叠标准型”和“学习新 representation”之间的接口会变得非常具体：

\[
\boxed{
\widetilde{SL_2}
\text{ 提供 finite standard processor，}
\qquad
\text{Schwarzian 提供不可被该 processor 商掉的过程残差。}
}
\]

而 spacetime-optimal learner 决定：何时只使用 shadow，何时保留 residual，何时继续升 rank。


---

# Addendum v0.2：Schwarzian-controlled \(SL_2\) lift 与深度分解

## 19. 重要措辞修正：当前构造首先是 ruler-dilation tower

递推：

\[
(X,A)\mapsto(AX,\log A)
\]

严格给出的，是“把 \(A\)-坐标中的 translation 提升为 dilation”的连续动力学：

\[
X=\partial_A,
\qquad
Y=A\partial_A=\partial_{\log A}.
\]

其 flow 满足：

\[
\Phi_Y^t(x)
=
A^{-1}(e^tA(x)).
\]

从：

\[
\partial_x
\to
x\partial_x
\to
x\log x\,\partial_x
\to\cdots
\]

得到的是一个 canonical ruler-dilation tower。

它与：

\[
+\to\times\to\exp\to\text{tetration}\to\cdots
\]

具有明确的 ruler / inverse-ruler 联系，但目前**不能未经额外证明就把二者在每一 rank 上完全等同**。

因此后续应区分：

- classical Hyperoperation objectification；
- continuous ruler-dilation rank raising；
- 二者之间需要建立的 normalization / typing / iteration correspondence。

---

## 20. Schwarzian residual 可以提升成一个受控 \(SL_2\) 系统

给定：

\[
q(u)=\mathcal S(f)(u),
\]

考虑：

\[
y''+\frac12q(u)y=0.
\]

令：

\[
\Psi=
\begin{pmatrix}
y\\y'
\end{pmatrix}.
\]

则：

\[
\Psi'
=
B_q(u)\Psi,
\qquad
B_q(u)
=
\begin{pmatrix}
0&1\\
-\frac12q(u)&0
\end{pmatrix}.
\]

因为：

\[
\operatorname{tr}B_q=0,
\]

所以：

\[
B_q(u)\in\mathfrak{sl}_2.
\]

基本解矩阵可取：

\[
G(u)\in SL_2.
\]

若 \(y_1,y_2\) 是两个线性独立解，则：

\[
f=\frac{y_1}{y_2}
\]

具有：

\[
\mathcal S(f)=q.
\]

改变解基只会对 \(f\) 做 Möbius 变换。

因此：

\[
\boxed{
\text{arbitrary 1D ruler transition}
\longleftrightarrow
\text{scalar control field }q(u)
\text{ driving an }\mathfrak{sl}_2\text{ system}
}
\]

（局部、模 projective gauge）。

这比“finite shadow + arbitrary infinite-dimensional correction”更强：

\[
\boxed{
\text{processor remains }SL_2,
\qquad
\text{infinite-dimensional information moves into }q(u).
}
\]

这给 universal-cover programme 一个新的解释方向：

\[
\boxed{
\widetilde{SL_2}
\text{ 可以充当标准 processor，}
\quad
q(u)\text{ 充当 process-history control field。}
}
\]

---

## 21. Hyperoperation rank step 是 constant-control \(SL_2\) system

对：

\[
f(u)=e^{au},
\]

有：

\[
\mathcal S(f)
=
-\frac{a^2}{2}.
\]

于是：

\[
B_q
=
\begin{pmatrix}
0&1\\
a^2/4&0
\end{pmatrix}
\]

是常矩阵。

所以 exponential rank transition 并不是仅仅“近似具有一个 \(SL_2\) shadow”，而是可以通过一个 **constant \(SL_2\) linear system** 精确生成其 projective developing map。

类似地：

### Parabolic

\[
q=0
\]

对应线性 / Möbius型：

\[
f\sim u.
\]

### Hyperbolic

\[
q=-\frac{a^2}{2}<0
\]

对应：

\[
f\sim e^{au}.
\]

### Elliptic

\[
q=+\frac{a^2}{2}>0
\]

对应：

\[
f\sim\tan\frac{au}{2}.
\]

因此 constant Schwarzian 的符号三分直接对应 constant \(\mathfrak{sl}_2\) generator 的三种基本类型。

这与此前 AEG 中的 flat / hyperbolic / spherical 三支存在明显结构呼应，但该对应仍需单独严格化，不能先当成同一结论。

---

## 22. Projective shadow 在 map level 是 osculating Möbius / Padé 型逼近

例如：

\[
f(v)=e^v.
\]

在 \(v=0\) 处，唯一与 \(f\) 匹配 value、first derivative、second derivative 的 Möbius map 是：

\[
\boxed{
M(v)
=
\frac{1+v/2}{1-v/2}.
}
\]

它满足：

\[
M(v)
=
1+v+\frac12v^2+\frac14v^3+\cdots,
\]

而：

\[
e^v
=
1+v+\frac12v^2+\frac16v^3+\cdots.
\]

因此二阶完全匹配。

其逆：

\[
M^{-1}(u)
=
\frac{2(u-1)}{u+1}
\]

在 \(u=1\) 处给出 \(\log u\) 的二阶 projective shadow。

这说明：

\[
\boxed{
\text{Lie-algebra 2-jet shadow}
}
\]

在 group / transition level 对应一个 canonical osculating Möbius transformation。

---

## 23. 深度 = Schwarzian cocycle 的因子化

Schwarzian 满足组合律：

\[
\boxed{
\mathcal S(f\circ g)
=
(\mathcal S(f)\circ g)(g')^2
+
\mathcal S(g).
}
\]

设：

\[
F_k=f_k\circ\cdots\circ f_1,
\qquad
F_0=\mathrm{id}.
\]

则：

\[
\boxed{
\mathcal S(F_k)
=
\sum_{i=1}^k
\left(
\mathcal S(f_i)\circ F_{i-1}
\right)
(F_{i-1}')^2.
}
\]

所以一个复杂 transition 的 projective residual 可以被因子化成多层简单 residual 的 transported sum。

### 对 repeated exponential

令：

\[
F_{k+1}=\exp\circ F_k.
\]

因为每一层：

\[
\mathcal S(\exp)=-\frac12,
\]

得到：

\[
\boxed{
\mathcal S(F_k)
=
-\frac12
\sum_{j=0}^{k-1}
(F_j')^2.
}
\]

例如：

\[
\mathcal S(e^u)
=
-\frac12,
\]

\[
\mathcal S(e^{e^u})
=
-\frac12
-
\frac12e^{2u},
\]

而再升一层会出现：

\[
-\frac12e^{2u+2e^u}
\]

等更复杂项。

因此：

\[
\boxed{
\text{flattened high-rank transition}
}
\]

会拥有迅速复杂化的 Schwarzian field，而：

\[
\boxed{
\text{ranked/deep representation}
}
\]

只需反复使用同一个简单的：

\[
q=-\frac12
\]

layer primitive。

这给“depth 为什么降低 representation complexity”一个非常具体的 projective-cocycle 解释。

---

## 24. 新的 learning problem：Projective Residual Factorization

给定 black-box transition \(f\) 或轨迹数据：

### Step 1 — learn ruler coordinates

使 primitive flow 尽量满足：

\[
XA=1.
\]

### Step 2 — estimate Schwarzian field

\[
q(u)=\mathcal S(f)(u).
\]

### Step 3 — model selection

比较：

- \(q=0\)：pure projective；
- \(q\approx\text{constant}\)：simple rank primitive；
- \(q\approx\) piecewise constant：少量 controlled-\(SL_2\) segments；
- \(q\) 可被多层 cocycle factorization 简化：grow depth；
- \(q\) 高复杂：保留 learned residual / history。

### Step 4 — spacetime objective

可用：

\[
\mathcal J
=
L_{\mathrm{task}}
+
\lambda C_R
+
\mu C_T
+
\nu C_S.
\]

其中：

\[
C_R
\]

不只计算参数量，还计算 residual field \(q\) 的描述复杂度。

于是 learner 可以因为：

\[
\boxed{
\text{factorization lowers residual description cost}
}
\]

而主动增加 rank / depth。

---

## 25. 新的核心工作假说

当前可以提出一个比“有限 Lie shadow”更精确的工作假说：

> **一维 ranked process geometry 可以局部表示为一个序列的 projective \(SL_2\) processors；完整的非-projective information 由 ruler transitions 的 Schwarzian control fields 携带。Hyperoperation/ruler-dilation rank step 的特殊性在于其相邻 transition 具有常 Schwarzian，因此能够由固定的 constant-\(SL_2\) primitive 表示。高 rank 的复杂性主要不表现为需要越来越大的有限维 Lie algebra，而表现为这些简单 projective processors 的 cocycle composition。**

形式上：

\[
\boxed{
\text{Exact ranked process geometry}
\approx
\left(
\widetilde{SL_2}\text{ local processors},
\;
q_r(u)\text{ transition controls},
\;
\text{rank gluing}
\right).
}
\]

这是当前最值得继续验证的结构。

---

## 26. 下一步实验优先级更新

### E1. Constant-Schwarzian discovery

生成未知 Möbius gauge 下的：

\[
q=0,\quad
q<0,\quad
q>0
\]

三类 black-box transitions，让 learner：

1. 恢复 ruler；
2. 估计 Schwarzian；
3. 自动识别 branch；
4. 构造对应 constant-\(SL_2\) primitive。

### E2. Variable-\(q\) segmentation

给定缓慢变化的 \(q(u)\)，学习 piecewise-constant \(SL_2\) control，优化：

\[
\text{segment count}
\times
\text{execution / approximation cost}.
\]

### E3. Depth discovery

生成：

\[
f=\exp^{\circ k}
\]

但不给 \(k\)，让 learner 比较：

- flat residual model；
- repeated constant-Schwarzian factorization。

检查 spacetime / representation objective 是否自动恢复 depth \(k\)。

### E4. Noncommutative extension

把 scalar projective connection 的思想与此前：

\[
E,F,[E,F]
\]

的 endogenous-ruler learner 合并，进入多 primitive / noncommutative process groupoid。

---

## 27. v0.2 阶段性结论

这一轮最重要的变化是：

旧图景：

\[
\text{finite Lie shadow}
+
\text{mysterious infinite residual}.
\]

新图景：

\[
\boxed{
\text{finite }SL_2\text{ processor}
+
\text{scalar Schwarzian control field}.
}
\]

而 Hyperoperation 相邻 rank step进一步简化为：

\[
\boxed{
\text{constant Schwarzian}
\Longleftrightarrow
\text{constant }SL_2\text{ control}.
}
\]

这使“万有覆叠标准型”“rank raising”“representation complexity”和“深度学习的层级分解”第一次有了同一个具体数学接口。
