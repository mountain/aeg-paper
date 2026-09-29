# AEG Paper 0 数学评审：`thm:p0-punctures-are-critical` 的反例

**评审对象：** `paper-0/sections/11-holed-aes.tex`（及该定理在治理文件中的登记），仓库
`mountain/aeg-paper`，commit `d89ceb8f8090482317b750407f623c8dcfb37ea2`
（`git rev-parse HEAD` 实测；本地检出 `~/AEG/aeg-paper`）。

**评审者：** DeepSeek Harness Agent（`deepseek-v4-flash-vision-exp`）。**日期：** 2026-09-29。**版本：** v0.1。

**文件类别：** 外部评审 / 缺陷裁定（audit）。**本文不是权威规范、不是状态登记、不修改任何文件。**
凡与 `governance/` 冲突之处，以 `governance/` 为准；本文只提交证据与建议处置。

**评审范围：** `def:regular-aes`（`03-aes-and-motion.tex:40`）、`def:p0-punctured-aes`（`11:18`）、
`thm:p0-punctures-are-critical`（`11:144`）及其证明、`rem:p0-puncture-hypothesis`（`11:187`）、
`cor:p0-puncture-count`（`11:337`）、`thm:p0-four-circle-model`（`11:201`）证明中的相关步骤；
以及 `governance/05b-paper-0-status-register.md:97,99,103,113`、
`governance/08-open-questions.md:3108–3142`（OQ-082）与 `:3166–3200`（OQ-088）
中的相关条目。本次**没有**通读 Paper 0 其余章节，也没有复核 Papers I–IV。

---

## 1. 总体判断

建议：**采纳 R1–R3，改陈述并降状态；R4 作为现成的修复假设。**

反例成立。`thm:p0-punctures-are-critical` **如所陈述为假**；`cor:p0-puncture-count` 一并继承该缺陷；
`rem:p0-puncture-hypothesis` 中"第二类里穿孔集是 canonical 的"这句话被同一个反例推翻。

缺陷不在任何计算里。证明的 eikonal 计算完全正确；问题出在证明的第一步：
**它构造了一个新的度量，然后把它称为给定度量的延拓。**
`def:p0-punctured-aes` 的条件 (ii) 要求延拓的是 $g|_{U\cap M}$ 本身，而不是"某个满足 eikonal 的新度量"。

值得记下的是：本仓库自己已经在 `prop:p0-puncture-local-picture` 里记下了关键区分
（`governance/05b-paper-0-status-register.md:103`）："$g$ is conformal to the Euclidean metric
with conformal factor vanishing at the puncture, so the *conformal class* of $g$ extends across
the puncture although the metric does not"。**"共形类可延拓"与"度量可延拓"是两个命题**，
而定理的证明步骤看上去正是把前者当成了后者。

---

## 2. 反例（R1 的证据）

取

$$M=\mathbb D\setminus\{0\},\qquad \overline M=\mathbb D,\qquad S=\{0\},\qquad \mu=\lambda=1,$$

$$a(x,y)=x,\qquad g=\frac{dx^2}{1+x^2}+\frac{dy^2}{x^2+y^2}\quad\text{on }M .$$

**核对 A：$(M,g,a;1,1)$ 是 regular AES。**
`def:regular-aes` 要求 $M$ 为定向光滑曲面、$g$ 为光滑黎曼度量、$a\in C^\infty(M,\mathbb R)$、
$\mu\ne0$、$\lambda\in\mathbb R$，以及 $|\nabla a|_g^2=\mu^2+\lambda^2a^2$ 在 $M$ 上处处成立。
本题中 $g$ 在 $x^2+y^2>0$ 上光滑正定（$g_{xx}=\frac1{1+x^2}>0$，$g_{yy}=\frac1{x^2+y^2}>0$），
$g^{xx}=1+x^2$，$da=dx$，故

$$|\nabla a|_g^2=g^{xx}=1+x^2=\mu^2+\lambda^2a^2 .$$

条件 (i) 满足。✅

**核对 B：条件 (ii) 满足。**
$g_{yy}=\frac1{x^2+y^2}\to+\infty$ 当 $(x,y)\to0$。故 $g$ 没有**连续**延拓，更没有光滑延拓；
而条件 (ii) 要求不存在"$g|_{U\cap M}$ 与 $a|_{U\cap M}$ 到 $U$ 上光滑数据 $\tilde g,\tilde a$ 的延拓"。
$g$ 侧已经不可能，故 (ii) 成立。✅

**核对 C：赋值光滑延拓。** $a=x$ 显然延拓为 $\overline M$ 上的光滑函数 $\tilde a=x$。✅

**核对 D：临界集为空。** $d\tilde a=dx$ 在 $\mathbb R^2$ 上处处非零，故
$\{p\in\overline M:d\tilde a(p)=0\}=\varnothing$。✅

于是 $S=\{0\}\ne\varnothing=\operatorname{Crit}(\tilde a)$。
**定理的两条假设全部满足，结论不成立。**

---

## 3. 缺陷的确切位置（R1，建议 `ACCEPT`）

`paper-0/sections/11-holed-aes.tex:157–176`，$S\subseteq\{d\tilde a=0\}$ 那一半。逐字引用：

> For the inclusion $S\subseteq\{d\widetilde a=0\}$, let $p\in S$ and suppose
> $d\widetilde a(p)\ne0$. Choose a smooth background metric $g_0$ on a neighbourhood $U$ of $p$,
> possible because $\overline M$ is a smooth surface. … Define
> $\widetilde g=\frac{|d\widetilde a|_{g_0}^2}{\mu^2+\lambda^2\widetilde a^2}\,g_0$ on $U$.
> Then $\widetilde g$ is a smooth Riemannian metric on $U$, and
> $|d\widetilde a|^2_{\widetilde g}=\mu^2+\lambda^2\widetilde a^2$,
> so $(U,\widetilde g,\widetilde a;\mu,\lambda)$ is a regular AES **extending $(g,a)$ across $p$**.
> This contradicts condition (ii) of Definition …

前两句的 eikonal 计算正确：$\tilde g$ 配上 $\tilde a$ 确实是 regular AES。
**但"extending $(g,a)$"这一步没有任何论证。** $g_0$ 是任取的光滑背景度量，
而 $\tilde g$ 由 $g_0$ 与 $\tilde a$ 唯一决定；它与**给定的** $g$ 在 $U\cap M$ 上相等，
当且仅当 $g$ 在该邻域与 $g_0$ 共形。定义里没有这一条。

取最简单的 $g_0=dx^2+dy^2$，则 $\tilde g=\frac{dx^2+dy^2}{1+x^2}$，于是

$$\tilde g_{yy}=\frac1{1+x^2},\qquad g_{yy}=\frac1{x^2+y^2},\qquad
\frac{g_{yy}}{\tilde g_{yy}}=\frac{1+x^2}{x^2+y^2}\xrightarrow[(x,y)\to0]{}+\infty .$$

$\tilde g$ 在**任何**穿孔邻域上都不是 $g$ 的延拓，因此构造不出与条件 (ii) 的矛盾。

**同一缺陷被逐字写进了 OQ-082 的结案理由**（`governance/08-open-questions.md:3108`，理由在 `:3121–3128`）：

> `Mathematical justification:` `thm:p0-punctures-are-critical` proves both inclusions.
> If `p` is a puncture and `d a~(p) != 0`, then the template metric
> `g~ = |d a~|^2_{g_0} g_0 / (mu^2 + lambda^2 a~^2)`, built with any smooth background metric
> `g_0`, is a smooth non-degenerate metric on a neighbourhood of `p` satisfying the eikonal
> identity, **so the regular structure extends across `p`**, contradicting local essentiality.

---

## 4. `cor:p0-puncture-count` 一并失效（R2，建议 `ACCEPT`）

`11:337` 的推论从该定理"Immediate"，故继承缺陷。其第一句：

> the number of punctures equals the number of critical points of that extension in $\overline M$

被 §2 的反例直接否证（1 个穿孔，0 个临界点）。第二句

> a model of this kind with exactly $k$ punctures exists if and only if the ambient surface carries
> a smooth function with exactly $k$ critical points

中"only if"方向同样失效：$\overline M=\mathbb D$ 承载无临界点的光滑函数（$a=x$），
而该模型恰有 1 个穿孔。

---

## 5. `rem:p0-puncture-hypothesis` 的断言被推翻（R3，建议 `ACCEPT`）

`11:187–197`，逐字引用（`11:194–197`）：

> The two verified punctured models are therefore of different kinds: in the disc model the
> *assignment* fails at the puncture, while in the model below the assignment is smooth everywhere
> and the *metric* is what cannot be non-degenerately extended. **In the second kind the puncture
> set is canonical**; in the first, canonicality is still open.

§2 的反例**恰好属于第二类**：赋值 $a=x$ 在整个 $\overline M$ 上光滑，不可延拓的是度量，
而穿孔集不是 canonical 的。事实上同一模型平移即可：对**任意**内点 $p$，取以 $p$ 为心的圆盘、
$S=\{p\}$、$a=x-p_x$、$g=\frac{d(x-p_x)^2}{1+(x-p_x)^2}+\frac{d(y-p_y)^2}{(x-p_x)^2+(y-p_y)^2}$，
则同样是 regular AES、同样满足 (ii)、同样有 $\operatorname{Crit}(a)=\varnothing$（附录 A 第 9 组）。
**"度量不可延拓"这一物种里，穿孔位置一个都不被强制。** 故该 remark 后半句应撤回或改写为条件性陈述。

同一隐含假设也出现在 **OQ-088**（`:3166`，状态 `OPEN`）的"Why it matters"里：

> In the four-circle model the *metric* is what cannot be extended non-degenerately and
> the punctures are forced by the assignment; in the disc model the *assignment* is what fails,
> and the puncture set is still a stipulation.

前半句在四圆模型上为真，但它被写成该**物种**的一般刻画；§2 的反例正是同一物种中穿孔**不被强制**的模型。
建议 OQ-088 重述为：*赋值延拓而度量不延拓的模型中，穿孔是否被强制，取决于 $g$ 在穿孔附近是否与可延拓度量共形*——
共形的情形由修复后的定理覆盖，不共形的情形见 §2。

---

## 6. 活下来的部分与最小修复（R4，建议 `ACCEPT`）

**正向的一半仍然成立。** $\operatorname{Crit}(\tilde a)\subseteq S$ 的证明
（`11:180–186`）只用 eikonal 在 $M$ 的内点上取值，不涉及延拓，故不受影响：

> For the reverse inclusion, let $p\in\overline M$ with $d\widetilde a(p)=0$ and suppose $p\notin S$.
> Then $p\in M$ and the eikonal identity at $p$ reads $0=|da(p)|_g^2=\mu^2+\lambda^2a(p)^2\ge\mu^2>0$,
> a contradiction.

**充分修复条件。** 给定理加上：*在每个 $p\in S$ 的某个邻域上，$g$ 与一个可光滑非退化延拓到 $p$ 的
背景度量 $g_0$ 共形。* 此时 $g=e^{2\varphi}g_0$，eikonal 给出
$e^{-2\varphi}|d\tilde a|^2_{g_0}=\mu^2+\lambda^2\tilde a^2$，即

$$e^{2\varphi}=\frac{|d\tilde a|^2_{g_0}}{\mu^2+\lambda^2\tilde a^2},\qquad
\text{hence}\qquad g=\frac{|d\tilde a|^2_{g_0}}{\mu^2+\lambda^2\tilde a^2}\,g_0 .$$

右端在 $p$ 附近光滑、正定（因 $d\tilde a(p)\ne0$ 且 $g_0$ 非退化），于是 $g$ **确实**光滑非退化地
延拓过 $p$——证明的这一步此时才成立。

**这个假设不是临时补丁，而是本仓库已经记录在案的事实。**
`governance/05b-paper-0-status-register.md:103` 对 `prop:p0-puncture-local-picture` 已写明：
"$g$ is conformal to the Euclidean metric … so the *conformal class* of $g$ extends across the
puncture although the metric does not"。四圆模型正是满足该共形延拓假设、但因共形因子**在穿孔处趋于 0**
而使度量本身退化的情形。建议把这条已登记的区分提为定理的显式假设。

§2 的反例恰好逃开该假设：$g_{yy}/g_{xx}=\frac{1+x^2}{x^2+y^2}$ 在原点没有有限非零极限，
故 $g$ 在原点附近与任何可延拓度量都**不**共形。

---

## 7. `thm:p0-four-circle-model` 不受影响，但它从未测试到这条论证（R5，观察）

`11:201` 的四圆模型取 $a=P|_M$，$P=S_2^4-4\rho^2S_2^3+16\rho^4x^2y^2$。
$P$ 是多项式，故赋值光滑延拓；论文证明了 $\nabla P\ne0$ 在 $D_r\setminus\{0\}$ 上，
且 $\nabla P(0)=0$，故 $\operatorname{Crit}(P)\cap D_r=\{0\}=S$。
**结论在该模型上成立**，反例不触及它。本文复核了其证明的两处代数（见附录 A）：

- 梯度分解 $\partial_xP=8x\,f(y)$、$\partial_yP=8y\,f(x)$，
  $f(t)=S_2^2(S_2-3\rho^2)+4\rho^4t^2$，恒等成立；
- $f$ 在 $t^2$ 上严格递增（$\partial f/\partial(t^2)=4\rho^4>0$），联立零点给出
  $2u^2-3u+1=0$（$u=x^2/\rho^2$），即 $S_2=\rho^2$ 或 $2\rho^2$，均 $\ge r^2$，落在 $D_r$ 之外。

**但要点是：该模型中 $d\tilde a(0)=0$，所以缺陷所在的分支（$d\tilde a(p)\ne0$）根本没有被触发。**
这解释了缺陷为何能通过自审：当时唯一的构造函数性例子恰好在"安全"分支上。
建议在修订时补一个 $d\tilde a(p)\ne0$ 的穿孔模型作为对照——§2 的模型即可，但需注明它不满足
修复后的假设，因此是**反例**而非新例子。

---

## 8. 影响面与建议处置

| 位置 | 现状（2026-09-29 实测） | 建议 |
|---|---|---|
| `paper-0/sections/11-holed-aes.tex:144` `thm:p0-punctures-are-critical` | 陈述过强，证明有缺口 | 加共形延拓假设（§6），或改为条件性陈述 |
| 同文件 `:337` `cor:p0-puncture-count` | 继承缺陷 | 同步改写；"iff" 必须重述 |
| 同文件 `:187` `rem:p0-puncture-hypothesis` | "第二类 canonical" 被推翻 | 撤回或改为条件性 |
| `governance/05b-paper-0-status-register.md:97,99` | `PROVED` / `PROVED` | 降为 `NEEDS HYPOTHESIS`（或在改陈述后重证） |
| `governance/05b-paper-0-status-register.md:113` | "the smoothly extending case is settled by …" | 改为"settled only under the conformal-extension hypothesis" |
| `governance/08-open-questions.md:3108`（理由 `:3121–3128`）OQ-082 | `RESOLVED`，理由含该缺口 | 重开或收紧结案范围 |
| `governance/08-open-questions.md:3166` OQ-088 | `OPEN`；"Why it matters" 含上述隐含假设 | 按 §5 末尾重述问题 |
| `AEG-Paper-1-consolidation-plan-2026-09-24-v0.1.md:267` | 依赖该定理对齐 Paper I | 暂缓，待 Paper 0 结论稳定 |

除 `11-holed-aes.tex` 外，`paper-1`–`paper-4`、`prog`、`notes` 均无该标签引用
（`grep -rn "punctures-are-critical"` 实测），故影响面限于 Paper 0 §11 与上表三处治理文件。

**建议的处置次序：** 先定陈述（§6 的假设是否采纳），再改状态登记与 OQ-088，
最后才动 Paper I 的对齐计划。反过来做会把未定的结论传播到下游。

---

## 9. 复核方法与本评审自身的边界

**方法。** 全部结论用 `sympy` 符号代数**独立重推**，不依赖本文作者的任何采样：
不使用 Paper 0 的余项式或矩阵路线，直接由 `def:regular-aes` 与 `def:p0-punctured-aes` 的定义
逐条验证。脚本 `adjudicate_counterexample.py`，26 条断言全部通过；
另有 `independent_check.py`（38 条）覆盖同批札记中其余承载性代数。
两份脚本与本评审的完整复现记录见 `elementary-geometry-check/`（工作区内）。

**边界。** 本文只裁定该定理及其直接下游。以下**未**核查：
Paper 0 其余章节（尤其 §11 的六条 witnesses 与 `prop:p0-tearing-puncture-independent`、
`prop:p0-no-puncture-holonomy`）；`op:p0-four-circle` 的一般化；
Papers I–IV；以及 `11:669` `subsec:p0-holed-nonclaims` 所列举的非主张是否仍然完整。
本文不主张 §2 的反例是唯一的反例类，也不主张修复假设是必要的——它只被证明是充分的。

**本评审自身的错误记录。** 定位过程中本文作者先后产生 5 处自身错误并全部改正
（其中 1 处曾误报"REFUTED"）：sympy 把 `Symbol("u")` 与 `Symbol("u", positive=True)` 当作两个不同符号，
对不在表达式中的那个求导会**静默返回 0** 而不报错。列出此点是因为它与 §3 的缺陷同型：
**一个静默的常数返回来冒充了结论。** 任何复核若只看"没有报错"，都会漏掉这两者。

---

## 附录 A：机器复核要点（26 条断言，全部通过）

| 断言的实质内容 | 结果 |
|---|---|
| $|\nabla a|_g^2=1+x^2$ 且 $\mu^2+\lambda^2a^2=1+x^2$（eikonal 恒等） | ✅ |
| $g$ 在 $M$ 上光滑正定（$g_{xx}>0$ 处处，$g_{yy}>0$ 恰在 $M$ 上） | ✅ |
| $g_{yy}=\frac1{x^2+y^2}\to\infty$，故不存在连续延拓 | ✅ |
| $\tilde a=x$ 光滑延拓；$dx$ 处处非零，故 $\operatorname{Crit}(\tilde a)=\varnothing$ | ✅ |
| $S=\{0\}\ne\varnothing$：定理被反例否证 | ✅ |
| 模板度量 $\tilde g$ 确实满足 eikonal（证明该步的计算无误） | ✅ |
| 但 $\tilde g_{yy}=\frac1{1+x^2}\ne g_{yy}$，比值 $\to\infty$：**不是延拓** | ✅ |
| $\operatorname{Crit}(\tilde a)\subseteq S$ 仍成立 | ✅ |
| 共形假设下 eikonal **强制** $e^{2\varphi}=\frac{|d\tilde a|^2_{g_0}}{\mu^2+\lambda^2\tilde a^2}$ | ✅ |
| 反例逃开该假设：$g_{yy}/g_{xx}$ 在原点无有限非零极限 | ✅ |
| 四圆模型：梯度分解恒等；$f$ 严格递增；$2u^2-3u+1=0\Rightarrow S_2\in\{\rho^2,2\rho^2\}$；$\nabla P(0)=0$ | ✅ |
| **平移后的模型对任意内点 $p$ 同样成立**（仍是 regular AES、仍满足 (ii)、仍 $\operatorname{Crit}=\varnothing$） | ✅ |

## 附录 B：关键逐字引用与定位

| 内容 | 位置 |
|---|---|
| `def:regular-aes`（含 eikonal `eq:regular-aes-eikonal`） | `paper-0/sections/03-aes-and-motion.tex:40`，`:48` |
| `def:p0-punctured-aes`，条件 (ii) 全文 | `paper-0/sections/11-holed-aes.tex:18`（条件 (ii) 在 `:26–29`） |
| `thm:p0-punctures-are-critical` | `11-holed-aes.tex:144`；结论式 `:148` |
| 有缺陷的证明步骤 | `11-holed-aes.tex:157–176`；"extending $(g,a)$" 在 `:174` |
| 正向包含 $\operatorname{Crit}(\tilde a)\subseteq S$ | `11-holed-aes.tex:180–186` |
| `rem:p0-puncture-hypothesis`；"In the second kind … canonical" | `11-holed-aes.tex:187`；`:196` |
| `thm:p0-four-circle-model` | `11-holed-aes.tex:201` |
| `cor:p0-puncture-count` | `11-holed-aes.tex:337` |
| `prop:p0-puncture-local-picture`（共形类可延拓） | `11-holed-aes.tex:482`；登记见 `05b:103` |
| 状态登记：定理与推论 `PROVED` | `governance/05b-paper-0-status-register.md:97`，`:99` |
| OQ-088 结案理由（含同一缺口） | `governance/08-open-questions.md:3121–3128`；条目起于 `:3109` |
| Paper I 对齐计划对该定理的依赖 | `AEG-Paper-1-consolidation-plan-2026-09-24-v0.1.md:267`，`:281` |

---

**署名与授权边界。** 本评审由 DeepSeek Harness Agent 撰写。
账号使用不构成 Mingli Yuan 的署名、评审或背书；本评审不对任何结论主张权威性，
其数值与代数结论可由附录 A 的脚本独立重跑。
