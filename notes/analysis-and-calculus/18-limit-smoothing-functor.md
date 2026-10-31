# 极限/光滑化函子：离散 DAG 求值 → 连续流

## 把 `17` §7 的缺口写成引理（生成元 = 场的指数流，序缺陷 = Lie 括号）

### Research Note v0.1

**2026-10-31**（v0.1：完成 `17` §7 的"极限/光滑化函子"缺口。核心三条引理：生成元 `T_s`、`D_k` 是水平场 `D_u`、`D_v` 的**精确指数流**；词 = 流的复合（函子性）；DAG 的**序缺陷 = 流交换子 = Lie 括号 `[D_u,D_v]`**，二阶系数 = 曲率 `μλ`）

---

## 0. 目标与结论

`17` §7 留了一个缺口：引理 B 只在**生成元层**逐项核对（`T_s ↔ D_u`、`D_k ↔ D_v`），要升级为**函子层**的交换图，需补"离散 DAG 求值 → 连续流"的极限/光滑化函子。本笔记把它写成三条引理。

**结论预告**：离散到连续的对应是一个**李函子**（Lie functor）：

- 生成元 `T_s`（加）、`D_k`（乘）= 水平场 `D_u`、`D_v` 的**精确时间流**（无需极限，流是闭式）。
- 词 = 流的复合（函子性，反同态）。
- DAG `{A,M}` 的**序缺陷**（两线程差）= **流交换子**，其无穷小二阶系数 = **Lie 括号 `[D_u,D_v] = μλ∂a`**。

即："离散的分叉缺陷"与"连续的曲率"由标准 Lie 理论精确对接——这是把 `17` 的主命题从 `structural proposal` 升级为定理的最后一环。

---

## 1. 记号

- `C = ℝ³_{(u,v,a)}`，水平场 `D_u = ∂u + μ∂a`、`D_v = ∂v + λa∂a`（`paper-0` `eq:horizontal-arithmetic-fields`）。
- 它们的流（`paper-0` `eq:additive-horizontal-flow`、`eq:multiplicative-horizontal-flow`）：
\[
\Phi_u^h(u,v,a)=(u+h,\,v,\,a+\mu h),
\qquad
\Phi_v^k(u,v,a)=(u,\,v+k,\,e^{\lambda k}a).
\]
- 离散生成元：`A_h = T_{\mu h}`（加 `μh`）、`M_k = D_{e^{\lambda k}}`（乘 `e^{λk}`）。
- 自由幺半群 `Hist({A,M})` = `{A,M}` 上的词；DAG `{A,M}` 的两条线索（线性扩展）= `γ₁ = (A_h, M_k)`、`γ₂ = (M_k, A_h)`。

---

## 2. 引理 1：生成元 = 场的精确指数流（`CLASSICAL`，平凡核对）

**命题**：`A_h` 是 `D_u` 的时间-`h` 流在 `a` 纤维上的作用，`M_k` 是 `D_v` 的时间-`k` 流在 `a` 纤维上的作用：

\[
A_h(a) = \Phi_u^h(0,0,a)\big|_a = a+\mu h,
\qquad
M_k(a) = \Phi_v^k(0,0,a)\big|_a = e^{\lambda k}a.
\]

**证明**：直接代入流公式。注意**无需极限**——`a ↦ a+μh` 与 `a ↦ e^{λk}a` 本就是 `D_u, D_v` 的闭式流（对应的一参数群恰为平移与伸缩，`09` §9 已证 `T_s` 是 Scott 连续嵌入、`D_k` 是 Scott 自同构）。∎

**意义**：离散生成元到连续流的对应在生成元层是**精确**的（不是 `h→0` 的近似），因为加性与乘性流是闭式。极限只出现在**复合的非交换性**上（引理 3）。

---

## 3. 引理 2：词 = 流的复合（函子性，`REFORMULATION`）

**命题**：映射
\[
F:\ \operatorname{Hist}(\{A,M\}) \longrightarrow \{\text{contact 流的复合}\},
\qquad
F(A_h)=\Phi_u^h,\quad F(M_k)=\Phi_v^k,
\]
把时序拼接映到流复合（反同态）：

\[
F(\gamma\delta) = F(\delta)\circ F(\gamma),
\]

与 `paper-1` 的 `ρ(γδ)=ρ(δ)ρ(γ)`（`eq:rho-chronological-antihomomorphism`）同构。特别地，两条线索映到两个复合流：

\[
F(A_h,M_k)=\Phi_v^k\circ\Phi_u^h,\qquad
F(M_k,A_h)=\Phi_u^h\circ\Phi_v^k.
\]

**证明**：`F` 由生成元定义并按自由幺半群延拓；反同态是 `paper-1` `prop:projective-evaluation-chronology` 的流版本。∎

---

## 4. 引理 3：序缺陷 = 流交换子 = Lie 括号（`CLASSICAL` + 直接计算）

这是本笔记的**核心**。DAG 的两条线索在值层不交换，其缺陷的无穷小密度 = Lie 括号。

**命题**：

1. **(闭回路缺陷)** 四步时序历史 `(A_h, M_k, A_{-h}, M_{-k})` 的闭回路漂移
\[
T_{\mathrm{closed}}(h,k)=\mu h(1-e^{-\lambda k}),
\]
（`paper-0` `eq:exact-closed-contact-drift`），其二阶系数
\[
\frac{\partial^2}{\partial h\,\partial k}\Big|_{h=k=0} T_{\mathrm{closed}}(h,k)=\mu\lambda.
\]

2. **(Lie 括号)** 水平场的括号 `[D_u,D_v]=\mu\lambda\partial_a`（`paper-0` `thm:contact-curvature`），故其作用在赋值坐标上为
\[
[D_u,D_v](a)=\mu\lambda.
\]

3. **(对应)** 因此闭回路缺陷的二阶系数 = Lie 括号：
\[
\frac{\partial^2 T_{\mathrm{closed}}}{\partial h\partial k}\Big|_{0,0}
=[D_u,D_v](a)=\mu\lambda.
\]

**证明**：对 `T_closed = μh(1−e^{−λk})` 在 `k=0` 展开：`1−e^{−λk} = λk − λ²k²/2 + ⋯`，故 `T_closed = μλ·hk + O(hk²)`，二阶系数 `μλ`。另一方由 `paper-0` `thm:contact-curvature`，`[D_u,D_v](a) = μλ∂a(a) = μλ`。二者相等。∎

**一般事实（`CLASSICAL`）**：对任意光滑向量场 `X,Y`（流 `Φ_X^t, Φ_Y^s`）与光滑函数 `f`，
\[
\frac{\partial^2}{\partial t\partial s}\Big|_{0,0} f\Big(\Phi_X^{-t}\Phi_Y^{-s}\Phi_X^{t}\Phi_Y^{s}(p)\Big) = [X,Y](f)(p),
\]
即**流交换子的二阶系数 = Lie 括号**（Campbell–Baker–Hausdorff / 标准 Lie 理论）。引理 3 是它在 `X=D_u, Y=D_v, f=a` 的特例，且 `paper-0` 已给出直接数值核对（`prop:torsion-curvature-synthesis` 的 `T_open`/`T_closed` 共同密度 `μλ`）。

---

## 5. 光滑化 = Chen/BCH 级数（Lie 语言的精确形式）

引理 1–3 合起来给出"离散 → 连续"的完整光滑化：

- **生成元 → 场**：`A_h = e^{hX}`（`X=D_u`）、`M_k = e^{kY}`（`Y=D_v`）——引理 1。
- **词 → 流**：`F(γ) =` 指数流的复合 = **乘积积分**（product integral）——引理 2。
- **词的对数 → Lie 级数**：由 BCH 公式，
\[
\log\big(F(\gamma)\big)
 = \sum_i (\text{charge}_i\text{ 的场})
  + \tfrac12\sum_{i<j}[\text{场}_i,\text{场}_j]
  + \text{高阶括号},
\]
其**二阶项 = 一对对交换子 `[D_u,D_v]`**，系数正是 `μλ`。这是把词"光滑化"到 Lie 代数后，序缺陷显现为括号的地方。

**一句话**：离散 DAG 求值经"指数流 + BCH 对数"光滑化为 contact 结构的 Lie 代数，其中**序缺陷 = `[D_u,D_v] = μλ∂a`**，即曲率。这就是 §7 缺的"极限/光滑化函子"。

---

## 6. 完成 `17` §7 的交换图

把引理 1–3 装配，`17` §7 的缺口闭合为下列交换图：

\[
\begin{array}{ccc}
\text{DAG } \{A,M\},\ O(\{A,M\})=B_2,\ \text{两线索}
  & \xrightarrow{\ F\ } &
\text{contact 流的复合}\\[2pt]
\Big\downarrow {\text{序缺陷（两线索差）}} & & \Big\downarrow {\text{流交换子}}\\[2pt]
T_{\mathrm{open}}/T_{\mathrm{closed}}
  & \xrightarrow{\ \partial^2/\partial h\partial k\ } &
[D_u,D_v]=\mu\lambda\partial_a
\end{array}
\]

- 顶行 = 引理 2（函子性）。
- 右列 = 引理 1（生成元 = 指数流）。
- 底行 = 引理 3（序缺陷的二阶系数 = Lie 括号 = 曲率）。

这条交换图把 `17` 的主命题（"Contact 曲率 = 最小分支 DAG 的序缺陷"）从 `structural proposal` 升级为**定理**：DAG 侧、函子侧、几何侧的每个箭头现在都有引理支撑，唯一的"非平凡"一步（序缺陷 = 曲率）是 `paper-0` 已证的 `prop:torsion-curvature-synthesis` + 标准 Lie 括号事实。

---

## 7. 地位总表

| 命题 | 地位 |
|---|---|
| §2 引理 1（生成元 = 精确指数流）| `CLASSICAL`（一参数群 + `09` §9）+ 平凡核对 |
| §3 引理 2（词 = 流复合，反同态）| `REFORMULATION`（`paper-1` `eq:rho-chronological-antihomomorphism` 的流版本）|
| §4 引理 3（闭回路缺陷二阶系数 = `[D_u,D_v](a) = μλ`）| `CLASSICAL`（流交换子 = Lie 括号）+ `proved in paper-0`（`thm:contact-curvature`、`prop:torsion-curvature-synthesis`）|
| §5 光滑化 = Chen/BCH 级数 | `CLASSICAL`（BCH 公式）+ `REFORMULATION` |
| §6 交换图（完成 `17` §7）| `proved`（引理 1–3 拼合；核心非平凡步为 `paper-0` 已证）|

---

## 8. 收尾与下一步

"极限/光滑化函子"缺口闭合：**离散 DAG 求值经指数流 + BCH 对数光滑化为 contact Lie 代数，序缺陷 = `[D_u,D_v] = μλ`**。这使 `17` 的主命题升级为可引用定理：**Contact 曲率 `μλ` = 最小分支 DAG `{A,M}` 的序缺陷密度**。

**残余（`open problem`，不阻塞本节结论）**：

1. **高阶括号**：BCH 展开的高阶项（`[D_u,[D_u,D_v]]` 等）是否对应**更高阶的分叉缺陷**（多个反链边的嵌套）？这需要把 §5 从单个反链 `{A,M}` 推广到任意依赖偏序 `P`（`15` §3），并把 §4 的"二阶系数"推广为"`O(P)` 上的多线性缺陷形式"。
2. **全 DAG 的 Lie 实现**：引理 2 的函子 `F` 目前只在 `{A,M}` 两生成元上；推广到任意生成元集（任意多个不可比运算）需要"自由 Lie 代数 / 自由流群"的实现，即 `15` 的 DAG dcpo 到某个自由李代数的函子。

**参考**（沿用）：

1. `paper-0/sections/09-contact-of-tearing.tex`（`eq:horizontal-arithmetic-fields`、`eq:additive-horizontal-flow`、`eq:multiplicative-horizontal-flow`、`eq:exact-closed-contact-drift`、`thm:contact-curvature`、`prop:torsion-curvature-synthesis`）。
2. `paper-1/sections/03-projective-affine.tex`（`eq:rho-chronological-antihomomorphism`）。
3. `notes/analysis-and-calculus/15-branching-history-dcpo.md`、`17-contact-curvature-as-dag-defect.md`。
4. 标准 Lie 理论：流的交换子 = Lie 括号；Campbell–Baker–Hausdorff 公式。
