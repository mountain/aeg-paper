# 历史商—时空复杂度—Projective Shadow：快速测试与阶段冻结
## Research Note v0.3 — 2026-08-19

> 目的：在另起研究线索之前，用一组低代价测试检查当前最关键的结构猜想，区分“已经相当稳的结论”“获得数值支持的工作假说”和“仍不应过度解释的部分”。
>
> 本轮不追求 benchmark 性能，而追求：
>
> \[
> \text{结构正确性}
> \;+\;
> \text{反例敏感性}
> \;+\;
> \text{可继续实验性}.
> \]

---

# 1. 当前研究线的最小骨架

截至本轮，学习机制方面形成四层结构：

\[
\boxed{
\begin{array}{c}
\textbf{I. History Quotient}\\
\text{什么历史差异不能丢？}\\
\downarrow\\
\text{future-sufficient state}
\\[3mm]
\textbf{II. Materialization}\\
\text{哪些历史状态值得保存？}\\
\downarrow\\
\text{space--time optimal memory}
\\[3mm]
\textbf{III. Rank Raising}\\
\text{哪些长过程值得对象化为新 primitive？}\\
\downarrow\\
\text{shorter process metric}
\\[3mm]
\textbf{IV. Projective Shadow + Residual}\\
\text{有限 Lie 标准型保存什么？剩余信息在哪里？}\\
\downarrow\\
SL_2\text{ processor} + \text{Schwarzian control field}.
\end{array}
}
\]

前三阶段已有 toy benchmark：

1. **Four-Sheet Wrapped Process**：从 future distinguishability 自动恢复正确历史商；
2. **Lifted Random-Access Memory**：checkpoint model 中得到
   \[
   k^*=\sqrt H;
   \]
3. **Rank-Raising Compiler**：加入尺度过程后，把重复过程的 word length 从
   \[
   \Theta(n)
   \]
   压缩到
   \[
   \Theta(\log n).
   \]

当前最值得检查的是第四层：

\[
\boxed{
\text{exact ranked process geometry}
\stackrel{?}{\longrightarrow}
\text{finite projective processor}
+
\text{compact residual}.
}
\]

---

# 2. 测试 A：Schwarzian 三支与 Möbius gauge

## A.1 解析恒等式

定义：

\[
\mathcal S(f)
=
\frac{f'''}{f'}
-
\frac32
\left(\frac{f''}{f'}\right)^2.
\]

符号计算确认：

\[
\mathcal S(u)=0,
\]

\[
\mathcal S(e^{au})=-\frac{a^2}{2},
\]

\[
\mathcal S\left(\tan\frac{au}{2}\right)=+\frac{a^2}{2},
\]

\[
\mathcal S(\log u)=\frac1{2u^2}.
\]

因此 constant Schwarzian 的三种最简单符号类型为：

\[
\boxed{
q=0,\quad q<0,\quad q>0.
}
\]

分别对应 projective/parabolic、exponential/hyperbolic、trigonometric/elliptic 型 normal form。

## A.2 Möbius gauge

对任意 Möbius map \(M\)：

\[
\mathcal S(M\circ f)=\mathcal S(f).
\]

符号测试在 exponential 与 tangent 两支上精确成立。

因此 Schwarzian 确实不会把 projective gauge 误当作 residual。

---

# 3. 测试 B：black-box 三支识别

## 设置

在区间：

\[
u\in[-0.5,0.5]
\]

生成三类 transition：

\[
f_0(u)=u,
\]

\[
f_-(u)=e^{0.8u},
\]

\[
f_+(u)=\tan(0.3u).
\]

其理论 Schwarzian 分别为：

\[
0,\quad -0.32,\quad +0.18.
\]

每次实验：

1. 随机生成一个安全的 Möbius post-gauge；
2. 只观察 gauge 后的函数采样；
3. 加入标准差 \(10^{-7}\) 的函数值噪声；
4. 用 Chebyshev 平滑拟合；
5. 从一、二、三阶导数估计 Schwarzian；
6. 只按照 Schwarzian 平均值的符号分类。

共进行：

\[
50\times3=150
\]

个测试实例。

## 结果

\[
\boxed{
150/150
}
\]

分类正确。

各类 Schwarzian 均值的平均绝对误差：

| branch | theoretical \(q\) | mean absolute error |
|---|---:|---:|
| parabolic | \(0\) | \(4.1\times10^{-5}\) |
| hyperbolic | \(-0.32\) | \(6.0\times10^{-5}\) |
| elliptic | \(+0.18\) | \(1.8\times10^{-4}\) |

结论：

\[
\boxed{
\text{projective gauge}
+
\text{Schwarzian sign}
}
\]

在这个低噪声 toy regime 中是稳定可识别的。

### 同时暴露的问题

Schwarzian 需要三阶导数。

即使函数值噪声只有：

\[
10^{-7},
\]

局部 \(q(u)\) 的波动已经达到：

\[
10^{-3}
\]

量级。

因此未来真实 learner 不应直接 finite-difference 三阶导数，而应使用：

- smoothing spline；
- regularized neural differential representation；
- ODE-constrained estimation；
- weak-form / integral estimation。

---

# 4. 测试 C：osculating Möbius 与三阶 residual

对：

\[
f(u)=e^u
\]

在 \(u=0\) 处匹配 value、first derivative、second derivative 的唯一 Möbius map 为：

\[
\boxed{
M(u)=\frac{1+u/2}{1-u/2}.
}
\]

展开：

\[
e^u
=
1+u+\frac12u^2+\frac16u^3+\cdots,
\]

\[
M(u)
=
1+u+\frac12u^2+\frac14u^3+\cdots.
\]

因此：

\[
e^u-M(u)
=
-\frac1{12}u^3+O(u^4).
\]

数值检查：

\[
\frac{e^u-M(u)}{u^3}
\longrightarrow
-0.083333\ldots
=
-\frac1{12}.
\]

例如：

| \(u\) | ratio |
|---:|---:|
| 0.01 | -0.08417 |
| 0.005 | -0.08375 |
| 0.002 | -0.08350 |

而 Schwarzian 公式给：

\[
\frac{f'(0)\mathcal S(f)(0)}{6}
=
\frac{-1/2}{6}
=
-\frac1{12}.
\]

因此：

\[
\boxed{
\text{2-jet projective shadow}
+
\text{Schwarzian cubic residual}
}
\]

在最基本的 exponential rank transition 上得到精确数值验证。

---

# 5. 测试 D：variable-\(q\) 的 controlled-\(SL_2\) 重建

选取非平凡 variable residual：

\[
q(u)
=
0.15+0.05\sin(1.3u),
\qquad
u\in[-1,1].
\]

构造：

\[
y''+\frac12q(u)y=0
\]

的两组独立解，并令：

\[
f(u)=\frac{y_1(u)}{y_2(u)}.
\]

理论上：

\[
\mathcal S(f)=q.
\]

## D.1 从 black-box \(f\) 恢复 \(q\)

对 \(f\) 的 801 个采样点进行 Chebyshev 平滑，并从导数估计 Schwarzian。

无额外噪声时：

\[
\mathrm{RMSE}(q_{\mathrm{est}},q)
\approx
1.0\times10^{-8},
\]

最大误差：

\[
7.2\times10^{-8}.
\]

## D.2 从估计出的 \(q\) 再重建 transition

把 \(q_{\mathrm{est}}\) 重新代入：

\[
\Psi'
=
\begin{pmatrix}
0&1\\
-q_{\mathrm{est}}/2&0
\end{pmatrix}
\Psi.
\]

使用相同 projective normalization 后恢复：

\[
f_{\mathrm{rec}}.
\]

得到：

\[
\max|f_{\mathrm{rec}}-f|
\approx
4.9\times10^{-8}.
\]

因此 toy setting 中形成了完整闭环：

\[
\boxed{
f
\to
q=\mathcal S(f)
\to
SL_2\text{ controlled system}
\to
f.
}
\]

## D.3 Möbius gauge + 噪声

再对 \(f\) 做随机 Möbius post-gauge，并加入：

\[
10^{-8}
\]

函数值噪声。

20 个随机实例中：

\[
\operatorname{median RMSE}(q)
\approx
2.1\times10^{-5},
\]

最差：

\[
3.4\times10^{-5}.
\]

这支持：

\[
\boxed{
\text{finite }SL_2\text{ processor}
+
\text{scalar }q(u)\text{ control}
}
\]

作为一维 transition 的可操作表示，而不仅是形式比喻。

---

# 6. 测试 E：深度是否真的在因子化 residual？

考虑 repeated exponential：

\[
F_k
=
\exp^{\circ k}.
\]

每一层 primitive 都有：

\[
q_{\mathrm{layer}}=-\frac12.
\]

但 flatten 后：

\[
q_k=\mathcal S(F_k)
\]

通过 Schwarzian cocycle 累积：

\[
\mathcal S(f\circ g)
=
(\mathcal S(f)\circ g)(g')^2
+
\mathcal S(g).
\]

在：

\[
u\in[-0.5,0.3]
\]

上，计算 \(k=1,2,3,4\) 的 flattened \(q_k\)。

用 Chebyshev polynomial 直接逼近 flattened \(q_k\)，要求 relative sup error：

\[
10^{-6}.
\]

结果：

| depth \(k\) | \(\max|q_k|\) | required degree |
|---:|---:|---:|
| 1 | 0.50 | 0 |
| 2 | 1.41 | 6 |
| 3 | 14.96 | 10 |
| 4 | \(3.04\times10^4\) | 16 |

而 layered representation 始终重复同一个：

\[
q=-\frac12
\]

primitive，只增加 depth counter。

因此这个快速实验支持：

\[
\boxed{
\text{flattening makes residual representation rapidly more complex;}
}
\]

\[
\boxed{
\text{depth factorizes that complexity into repeated simple controls.}
}
\]

### 但这里必须保留限定

Chebyshev degree 只是一个 **representation-complexity proxy**。

这并没有证明：

- 深度 representation 在所有编码模型中最优；
- flattened representation 必须有上述复杂度；
- neural network 中会获得同样数量级优势。

所以当前只能记作：

\[
\boxed{
\text{positive structural evidence, not a complexity theorem}.
}
\]

---

# 7. 这轮测试支持什么？

## 7.1 支持得比较强

### (a) Projective shadow / Schwarzian residual 分解

一维 transition 中：

\[
\boxed{
\text{Möbius/projective data}
+
\mathcal S(f)
}
\]

是一个非常自然且实际可计算的分解。

### (b) Schwarzian 是 gauge-independent residual

Möbius post-gauge 不改变 \(q\)。

### (c) Variable residual 仍可由固定 \(SL_2\) processor 执行

\[
q(u)
\]

并不要求扩大 processor 的 Lie dimension：

\[
B_q(u)\in\mathfrak{sl}_2
\]

始终成立。

### (d) Constant Schwarzian 是特殊的低复杂 rank transition

\[
q=0,\quad q<0,\quad q>0
\]

三类都能稳定识别。

---

# 8. 支持但仍需谨慎的部分

## 8.1 “深度 = residual factorization”

快速测试明显支持这一方向，但还没有正式 MDL / circuit complexity theorem。

下一步若重启此线，应定义真正的：

\[
C_R(q)
\]

而不是使用 polynomial degree 代理。

## 8.2 与 AEG flat / hyperbolic / spherical 三支的关系

Schwarzian 的：

\[
0,-,+
\]

三分与此前几何三支非常诱人，但现在只能说：

\[
\boxed{
\text{formal structural resemblance}.
}
\]

还没有证明它们是同一个分类。

## 8.3 Hyperoperation tower 的身份

目前严格得到的是 continuous ruler-dilation tower：

\[
(X,A)
\mapsto
(AX,\log A).
\]

不能把：

\[
x\log x\,\partial_x
\]

未经额外论证直接等同于 classical tetration rank。

这里仍缺：

\[
\boxed{
\text{classical Hyperoperation objectification}
\leftrightarrow
\text{continuous ruler-dilation tower}
}
\]

的正式桥梁。

---

# 9. 当前已经相当明确的学习框架

如果以后重启这条研究线，最值得继续的不是普通 neural architecture search，而是一个：

\[
\boxed{
\textbf{Self-Growing Process Representation Learner}.
}
\]

其循环可以写成：

1. 从 history 中寻找 future-sufficient quotient；
2. 根据访问分布决定 materialization；
3. 对高成本 process 学 ruler；
4. 若现有 relative geometry 中已有 scaling direction，则直接 objectify；
5. 否则构造 rank-raised process；
6. 提取 local projective shadow；
7. 估计 Schwarzian residual；
8. 比较：
   - pure projective；
   - constant-\(q\) primitive；
   - segmented \(q\)；
   - layered factorization；
   - generic residual model；
9. 按：
   \[
   C_R+C_T+C_S
   \]
   决定是否扩展 process language。

核心目标不再只是：

\[
\min L_{\mathrm{prediction}},
\]

而是：

\[
\boxed{
\min
\left(
L_{\mathrm{task}}
+
\lambda_R C_R
+
\lambda_T C_T
+
\lambda_S C_S
\right).
}
\]

---

# 10. 阶段冻结结论

本轮快速测试没有发现当前主线中的直接反例。

更准确地说：

### 已经站稳的局部结构

\[
\boxed{
\text{history quotient}
\to
\text{predictive state}
}
\]

\[
\boxed{
\text{materialization}
\to
\text{space/time trade-off}
}
\]

\[
\boxed{
\text{rank raising}
\to
\text{process-metric compression}
}
\]

以及一维：

\[
\boxed{
\text{projective shadow}
+
\text{Schwarzian control field}.
}
\]

### 当前最有潜力的新统一表达

\[
\boxed{
\textbf{标准 Lie 几何是 processor；
历史与非标准结构进入 control/residual；
学习的任务是在任务损失约束下寻找使 representation、space 和 time 联合代价最小的 quotient、processor 与 residual factorization。}
}
\]

### 还没有解决的核心问题

1. 一般历史商如何在连续、高维、非平稳系统中算法化；
2. 如何定义与机器模型无关或至少可审计的 \(C_R\)；
3. continuous ruler-dilation rank 与 classical Hyperoperation rank 的严格关系；
4. 一维 Schwarzian 结构如何推广到高维 / noncommutative process geometry；
5. Arithmetic Universal-Cover Conjecture 本身仍是远强于现有实验的猜想；
6. toy compression 是否会转化成真正学习任务中的 sample / time / memory advantage，尚未验证。

---

# 11. 建议的未来恢复点

如果以后重新开启这条线，推荐直接从以下任务恢复：

> **给定一个未知的一维 black-box process family，学习 ruler coordinate 与 Schwarzian control field；在 constant-\(q\)、piecewise-\(q\)、layered-\(q\)、generic residual 四种 representation 之间，用显式 \(C_R+C_T+C_S\) 目标进行模型选择，并测试是否自动恢复隐藏的 compositional depth。**

这个任务足够小，可以直接做数值实验；同时又完整连接：

\[
\text{AEG relative geometry}
\leftrightarrow
\text{Lie shadow}
\leftrightarrow
\text{history residual}
\leftrightarrow
\text{learning}
\leftrightarrow
\text{complexity}.
\]

---

## 最终状态

这一研究线现在适合暂时冻结为：

\[
\boxed{
\textbf{promising, internally coherent, experimentally sanity-checked, but still pre-theorem / pre-application.}
}
\]

它已经有足够清楚的下一恢复点，因此可以安全切换到新的实际任务，而不必继续在当前 toy framework 上追加低边际收益实验。
