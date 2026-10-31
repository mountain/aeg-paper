# 命题骨架：Contact 曲率 = 最小分支 DAG 的序缺陷

## 经 Scott/Lawson 函子把 `O({A,M})` 的谱与 `dα` 接起来

### Research Note v0.1

**2026-10-31**（v0.1：把 `15` 的 Birkhoff 下集格、`12`/`13` 的 Scott/Lawson 函子、与 `paper-0` §9 的 contact 曲率，接成一条命题的骨架。核心判断：`O({A,M})` 本身是**平的**（菱形），曲率 `μλ` 是函子 `Φ` 对两个不可比方向作**非交换实现**的代价）

---

## 0. 目标与结论

前一轮讨论提出猜想："Contact 结构 = 体计算的 DAG 语言"。本笔记把它落成一条**精确命题**的骨架：最小分支 DAG `{A,M}`（加 ⊥ 乘）经 Scott/Lawson 函子求值，其**序缺陷**的无穷小密度恰为 contact 曲率 `μλ`。

**结论预告**（四点）：

1. **[Birkhoff]** `O({A,M})` = 菱形（`B₂`），`Stone(O({A,M})) = {A,M}`（下集格与反链互 Stone 对偶）。
2. **[序缺陷]** 两条极大链（线索）`(A,M)`、`(M,A)` 的求值差 = `T_open = μh(e^{λk}−1)`（`paper-0` `eq:exact-open-contact-defect`）。
3. **[无穷小]** `T_open` 的密度 = `μλ` = `[D_u,D_v]` 系数（`paper-0` `thm:contact-curvature`）。
4. **[精化]** DAG `{A,M}` 本身是**平的**；曲率 `μλ` 来自函子 `Φ` 对 `A`（加）与 `M`（乘）的**非交换实现**——加乘在电荷层交换、在值层不交换。

---

## 1. 精确命题（定理陈述）

**Theorem（Contact 曲率 = 最小分支 DAG 的序缺陷）.** 设

- `P = {A, M}` 为二元素反链（加 `A` 与乘 `M` 不可比），`O(P)` 为其下集格（菱形 `B₂`），两条极大链 `γ₁ = (A,M)`、`γ₂ = (M,A)`；
- `Φ` 为 Scott/Lawson 函子（`12`/`13`），把生成元 `A = T_{μh}`（加性，电荷 `μh`）与 `M = D_{e^{λk}}`（乘性，电荷 `λk`）实现为水平场 `D_u`、`D_v`（`paper-0` `eq:horizontal-arithmetic-fields`）。

则：

1. **(Birkhoff 谱)** `Stone(O(P)) = P = {A,M}`：下集格是反链上的自由分配格，其 Stone 对偶（join-不可约元 / 素滤子）恰恢复两个方向 `A, M`。
2. **(序缺陷)** 两线索在赋值 `a` 上的求值差
\[
\nu_a(\gamma_1)-\nu_a(\gamma_2)
 = T_{\mathrm{open}}(h,k)
 = \mu h(e^{\lambda k}-1),
\]
与 `a` 无关。
3. **(无穷小 = 曲率)** 缺陷密度等于 contact 曲率：
\[
\lim_{h,k\to0}\frac{T_{\mathrm{open}}(h,k)}{hk}=\mu\lambda,
\qquad
[D_u,D_v]=\mu\lambda\,\partial_a.
\]
4. **(合成)** 故最小分支 DAG `{A,M}` 经 `Φ` 求值，其序缺陷密度 = contact 曲率 `μλ` = `dα` 的系数（`dα = −μλ\,Q^*(dvol_{g})`）。

---

## 2. 引理分解

### 2.1 引理 A（DAG 侧，`CLASSICAL`）

`O({A,M}) = {∅, {A}, {M}, {A,M}}` 是菱形（`B₂`）；两条极大链 = 两个线性扩展 `(A,M)`、`(M,A)`；`Stone(O({A,M})) = {A,M}`。

**证明**：`B₂` 的 join-不可约元为 `{A}, {M}`，构成反链 `{A,M}`（Birkhoff 表示定理：`O` 与 `Stone` 在有限分配格 ↔ 有限偏序间互逆）。∎

### 2.2 引理 B（函子侧，`REFORMULATION` + `12`/`13`）

函子 `Φ` 的生成元识别：`T_s`（加）= way-below 见证（`09` §9.2）、`D_k`（乘）= Scott 自同构（`09` §9.2）；在 contact 实现下 `T_{μh} ↔ Φ_u^h`（加性流 `a ↦ a+μh`）、`D_{e^{λk}} ↔ Φ_v^k`（乘性流 `a ↦ e^{λk}a`）。

**证明**：这是 `paper-0` `eq:additive-horizontal-flow`/`eq:multiplicative-horizontal-flow` 与 `09` §9 的生成元对应逐项核对（`12` §2、`13` §1）。∎

### 2.3 引理 C（求值侧，`proved in paper-0`）

\[
\nu_a(A,M)=e^{\lambda k}(a+\mu h),\qquad
\nu_a(M,A)=e^{\lambda k}a+\mu h,
\qquad
T_{\mathrm{open}}=\mu h(e^{\lambda k}-1).
\]

**证明**：`paper-0` `eq:exact-open-contact-defect`（先加后乘 vs 先乘后加）。∎

### 2.4 引理 D（几何侧，`proved in paper-0`）

`[D_u,D_v]=\mu\lambda\partial_a`；`α∧dα = μλ\,du∧da∧dv`；`dα = −λ\,da∧dv = −μλ\,Q^*(dvol_{g})`。

**证明**：`paper-0` `thm:contact-curvature`、`prop:contact-form`、`prop:p0-contact-quotient`(5)。∎

### 2.5 引理 E（合成，`proved in paper-0`）

`T_open` 与 `T_closed` 有共同无穷小密度 `μλ`（`paper-0` `prop:torsion-curvature-synthesis`）。∎

---

## 3. 主定理的拼合（逐条映射）

主定理的四条由 §2 拼合：

- 第 1 条 = 引理 A（`CLASSICAL`）。
- 第 2 条 = 引理 B（`Φ` 把 `A,M` 实现为 `T_{μh}, D_{e^{λk}}`）+ 引理 C（求值）。
- 第 3 条 = 引理 E（密度 `μλ`）+ 引理 D（`μλ = [D_u,D_v]` 系数）。
- 第 4 条 = 引理 D 的 `dα = −μλ\,Q^*(dvol)` 与第 3 条的密度相等。

**拼合的实质**：把 `paper-0` §9 里"tearing 的密度 = 曲率"这句话，改写成"**最小分支 DAG `{A,M}` 的序缺陷密度 = 曲率**"。前者是 `paper-0` 已证的（`prop:torsion-curvature-synthesis`）；后者是新的**读法**——把"开缺陷 `T_open`"识别为"两条线索（两个线性扩展）的求值差"，即 DAG 语言里的"分支缺陷"。

**地位**：第 1–3 条全为 `CLASSICAL`/`proved in paper-0`；第 4 条的"合成"是 `REFORMULATION`（把已证的缺陷—曲率等式，读回 DAG 语言），不是新定理。**这是 OQ-094 全线的收束点**：`09`–`16` 的域论/函子工具，正是把这条 `paper-0` 已有的等式**放回它的域论发源地**（下集格 `O(P)` 的谱）。

---

## 4. 精化：DAG 平、曲率来自函子的非交换代价

这是对"Contact = DAG 语言"猜想的**关键修正**：

- **`O({A,M})` 是平的**：菱形 `B₂` 是自由分配格，无任何序论曲率；两条线索的"分叉"只是组合事实。
- **曲率 `μλ` 不在 DAG 里，而在函子 `Φ` 的实现里**：加 `T_s` 与乘 `D_k` 在**电荷层**交换（`A+` 与 `M` 是 ACS 的两个交换坐标），但在**值层**不交换（`e^{λk}(a+μh) ≠ e^{λk}a+μh`）。曲率是"把平的 DAG 通过非交换流实现到值空间"所付的代价。

**等价表述（更贴近你的谱语言）**：`Stone(O({A,M})) = {A,M}` 的谱拓扑是**离散**的（两个方向无黏连）；曲率 `μλ` 是尝试把这两个离散方向**连续地、非交换地**提升到 `(u,v,a)` 态空间时出现的**障碍类**——它是实现的谱不变量，不是 DAG 的谱不变量。

---

## 5. 谱的落点

| 层 | 对象 | 曲率 |
|---|---|---|
| DAG（体，组合）| `{A,M}` 反链，`O(P)=B₂` 菱形 | **0**（平）|
| 谱（Stone 对偶）| `{A,M}` 两点离散空间（Scott 拓扑）| **0**（离散）|
| 实现（contact，几何）| `(u,v,a)` 态空间 + 水平分布 | **μλ**（`[D_u,D_v]`）|

即：**曲率出现在"谱 → 几何实现"这一步**，不在"体 → 谱"这一步。这精确回答了"Contact 是不是体计算的 DAG 语言"：**是，但只在"体经谱再经函子实现为几何"这一整条链上；DAG 与谱本身是平的，Contact 的曲率是最后一步非交换实现的代价。**

---

## 6. 地位总表

| 命题 | 地位 |
|---|---|
| §2.1 引理 A（`O({A,M})` 菱形、Stone 对偶）| `CLASSICAL`（Birkhoff 表示定理）|
| §2.2 引理 B（`Φ` 的生成元识别）| `REFORMULATION`（`09` §9 + `paper-0` 流 + `12`/`13`）|
| §2.3–2.5 引理 C/D/E | `proved in paper-0`（`eq:exact-open-contact-defect`、`thm:contact-curvature`、`prop:torsion-curvature-synthesis`）|
| §1 主定理（缺陷密度 = 曲率 = DAG 序缺陷）| `proved`（`18` 引理 1–3 补齐函子层缺口后升级）|
| §4 精化（DAG 平、曲率来自非交换实现）| `structural proposal`（精确化猜想）|
| §5 谱落点表 | `structural proposal` |

---

## 7. 收尾与下一步

命题骨架成立：**最小分支 DAG 的序缺陷 = contact 曲率 `μλ`**，且"体 → 谱"平、"谱 → 几何实现"曲。这既是 OQ-094 全线的收束，也是把 `paper-0` §9 的 contact 结构放回 DAG/域论发源地的第一步。

**要升级为"可引用的定理"还差一步**：引理 B 的 `Φ` 目前只在**生成元层**逐项核对（`T_s ↔ D_u`、`D_k ↔ D_v`）。要把它升级为**函子层**的交换图——即"下集格 `O(P)` 的谱空间上的 Scott 拓扑，经 `Φ` 与 contact 的水平分布 `ker α` 交换"——需要补一个从"有限 DAG 求值"到"连续流"的极限/光滑化函子，且要处理 `h,k → 0` 时 `Φ_u^h, Φ_v^k` 的无穷小生成与 `D_u, D_v` 的对应。

**已解决（2026-10-31，`18-limit-smoothing-functor.md`）**：该缺口由三条引理闭合——(1) 生成元 `T_s`、`D_k` 是 `D_u`、`D_v` 的**精确指数流**；(2) 词 = 流的复合（函子性，反同态）；(3) DAG 序缺陷的无穷小二阶系数 = 流交换子 = Lie 括号 `[D_u,D_v](a) = μλ`（`CLASSICAL` 流交换子 + `paper-0` 已证的 `prop:torsion-curvature-synthesis`）。故 `17` 的主命题由此升级为**定理**：Contact 曲率 `μλ` = 最小分支 DAG 的序缺陷密度。残余为高阶括号（多反链边）与全 DAG 的 Lie 实现（`18` §8）。

**参考**（沿用）：

1. `paper-0/sections/09-contact-of-tearing.tex`（`eq:exact-open-contact-defect`、`thm:contact-curvature`、`prop:torsion-curvature-synthesis`、`prop:p0-contact-quotient`）。
2. `notes/analysis-and-calculus/09-order-topology-scott-lawson.md` §9、`12-galois-connection-oq094a.md`、`13-functorial-language-oq094a.md`、`15-branching-history-dcpo.md`。
3. G. Birkhoff, *Lattice Theory*, AMS (1967)（下集格 / 有限分配格表示）。
