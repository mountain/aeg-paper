# Scott 拓扑与 Lawson 拓扑

## 从信息序到单侧拓扑，再到双侧（Hausdorff）拓扑

### Research Note v0.2

**2026-10-31**（v0.2：追加 §8–§12，闭合 OQ-091/092/093 与泛函层残余）

---

## 0. 位置与目标

这份笔记是一页**可引用的参考词汇**，解释 domain theory（域论）里的两个拓扑：Scott 拓扑与 Lawson 拓扑。它服务于 AEG 后期那条"基于序拓扑的分析学"路线，承接 `08-reflection-on-measurement-systems.md` 里已经出现的两个问题意识：

- "metric、neighborhood、relative scale、error、path cost **可能都是导出的**"（§16）；
- "completed reading object 何时是 \(\mathbb R\)"（§22.3），即有限读数 + 精度加细如何生成完备对象。

这两个问题在域论里正好有现成、严格的答案：**从逼近序（信息序）出发，先得到 Scott 拓扑（单侧、从下累积），再与对偶侧合成 Lawson 拓扑（双侧、Hausdorff）**。本文只做词汇与对应关系的澄清，不引入新的定理。

**地位约定**：所有域论事实标 `CLASSICAL`（取自 Scott [1]、Gierz–Hofmann–Keimel–Lawson–Mislove–Scott《A Compendium of Continuous Lattices》[2]，以及 Warner [3]）。所有把域论结构对应到 AEG 的语句标 `structural proposal` 或 `conjecture`，**不得**当作已证结论。对照表只是研究地图，不是理论等价性的断言。

---

## 1. 前置：信息序、定向集、dcpo、way-below

域论的基本态度：元素间的序 \(x\sqsubseteq y\) 不是"大小"，而是 **\(y\) 的信息量不少于 \(x\)**（\(y\) 是 \(x\) 的延拓 / 加细 / 更完整版本）。`CLASSICAL`

- **定向集 (directed set)**：非空子集 \(D\)，任意有限个元素在 \(D\) 内有共同上界。直觉：一族"越来越完整"的逼近，趋向一个极限。
- **dcpo**（directed-complete partial order）：每个定向集都有最小上界 \(\bigsqcup D\)。
- **紧致元 (compact element)**：\(k\) 满足 \(k\sqsubseteq \bigsqcup D \Longrightarrow \exists d\in D,\ k\sqsubseteq d\)。直觉：一旦极限对象包含 \(k\) 的信息，**某个有限阶段**就已包含它——所以 \(k\) 是"有限 / 可计算"的对象。domain theory 里 compact = finite。
- **way-below（\(x\ll y\)）**：对任意定向集 \(D\)，若 \(y\sqsubseteq \bigsqcup D\)，则存在 \(d\in D\) 使 \(x\sqsubseteq d\)。读作"**\(x\) 是 \(y\) 的一个有限逼近**"。`CLASSICAL`

  （Warner [3, Def 2.9] 的等价写法：\(x\ll y \Longleftrightarrow y\in\operatorname{int}(\uparrow\!x)\)，其中 \(\uparrow\!x=\{z:x\sqsubseteq z\}\)，内部取 Scott 拓扑。二者在连续格上一致。）

- **连续格 / 连续 domain**：每个元素 \(x=\bigsqcup\{z:z\ll x\}\)，即每个元素都是它所有有限逼近的定向并。这是"一切皆可由有限信息逼近"的正式说法。`CLASSICAL`

---

## 2. Scott 拓扑 \(\sigma(L)\)

**定义**（[1,2,3, Def 2.4]）：\(O\subseteq L\) 是 Scott 开集 ⟺

1. \(O\) 是上集：\(x\in O\) 且 \(x\sqsubseteq y \Longrightarrow y\in O\)；
2. \(O\) 对定向并不可达：对任意定向集 \(D\)，若 \(\bigsqcup D\in O\)，则 \(D\cap O\neq\varnothing\)（极限在 \(O\) 里，就必有一个有限阶段已经在 \(O\) 里）。`CLASSICAL`

**直觉（一句话）**：Scott 开集是**"可有限观测的性质"**。一个性质若在有限阶段永远观测不到、只在极限处突然出现，它就不是 Scott 开集。

**核心定理（拓扑 ↔ 序）**：对 dcpo，\(f:L\to L'\) Scott 连续 **当且仅当** \(f\) 单调且保定向并：

\[
f\Big(\bigsqcup D\Big)=\bigsqcup f(D)\qquad(\text{对所有定向集 }D).
\]

`CLASSICAL`。这是域论里最重要的一句话："连续"不是"邻近点映到邻近点"，而是"**极限的信息 = 各有限阶段信息的极限**"。

**性质**：Scott 拓扑总是 T0（连续 domain 上还 sober），但**一般非 T1、非 Hausdorff**。连续 domain 上，集合 \(\mathord{\Uparrow} x=\{y:x\ll y\}\) 构成 Scott 拓扑的一个基。`CLASSICAL`

**两个例子**（[3]）：

- \(L=[0,1]\)（通常序）：Scott 开集 = \(\varnothing\)、\([0,1]\)、以及所有 \((a,1]\)（\(0\le a<1\)）。这就是**右半开区间（下极限）拓扑**。于是 \(f:X\to[0,1]\) Scott 连续 ⟺ \(\{x:f(x)>a\}\) 总开 ⟺ **\(f\) 下半连续 (lsc)**。此处 \(x\ll y\iff x<y\)（外加底元 \(0\ll 0\)）。
- \(L=\mathcal P(S)\)（包含序）：定向并 = 并集。紧致元 = **有限子集**；\(A\ll B\iff A\) 有限且 \(A\subseteq B\)。Scott 开集由 \(\uparrow\! F=\{B:F\subseteq B\}\)（\(F\) 有限）生成。

---

## 3. 为什么 Scott 是"单侧"的

Scott 拓扑只编码"**从下面逼近**"（下方向、前向、累积）。它刻意"看不见"上方向：一个被定向族从下逼近的点 \(y\)，Scott 拓扑无法把它和它的逼近区分开（所以非 T1）。这是设计目的而非缺陷——它只关心"有限信息能确定什么"，不关心"从上往下"的极限。`CLASSICAL`

要得到对称的、Hausdorff 的拓扑，必须补上另一侧。

---

## 4. 下拓扑 (lower topology) \(\omega(L)\)

**定义**：以主滤子 \(\uparrow\! x=\{y:x\sqsubseteq y\}\) 作为**闭集**的子基生成；等价地，以 \(L\setminus\uparrow\! x=\{y:x\nsqsubseteq y\}\) 作为开子基。它是 \(L\) 的对偶序 \(L^{\mathrm{op}}\) 上的 Scott 拓扑，编码"**从上面逼近**"（上方向、后向）。`CLASSICAL`

---

## 5. Lawson 拓扑 \(\lambda(L)\)

**定义**：Scott 拓扑与下拓扑的**公共加细（join）**：

\[
\lambda(L)=\text{由 }\{U:U\text{ 是 Scott 开}\}\cup\{L\setminus\uparrow\! x:x\in L\}\text{ 生成的拓扑}.
\]

（连续 domain 上等价写法：以 \(\{\mathord{\Uparrow} x\}\cup\{L\setminus\uparrow\! x\}\) 为子基。）它也被称为 Scott 拓扑的 **patch 拓扑**——补上"从上看的补集"，让每个点同时由"它包含什么、它不含什么"两侧确定。`CLASSICAL`

**性质**（[2]）：

- 对任意 dcpo，Lawson 拓扑**总是 Hausdorff**；
- 对**连续格**（以及更一般的 Lawson 紧 domain），Lawson 拓扑是**紧 Hausdorff**；
- 在连续格上它使 \(\ll\) 成为闭关系，即"有限逼近"这层结构在 Lawson 拓扑下是干净的。

**两个例子（最能看清它干了什么）**：

- \(L=[0,1]\)：Scott 侧给 \((a,1]\)，下拓扑侧给 \([0,b)\)（因 \(\uparrow\! x=[x,1]\)，其补为 \([0,x)\)）。两者相交 \((a,1]\cap[0,b)=(a,b)\)，生成所有开区间——**Lawson 拓扑 = 通常的欧氏拓扑**。
- \(L=\mathcal P(S)\)：Scott 子基 \(\uparrow\!\{s\}=\{A:s\in A\}\)，下拓扑子基 \(\mathcal P(S)\setminus\uparrow\!\{s\}=\{A:s\notin A\}\)。这恰是 \(\mathcal P(S)\cong\{0,1\}^{S}\) 的**乘积拓扑**（逐点收敛）。当 \(S\) 可数无穷时，就是 **Cantor 空间**（紧 Hausdorff 可度量）。

---

## 6. 与 AEG 的对照表

这是研究地图，不是理论等价性的断言。`structural proposal`（整表），其中"对偶侧 ⟷ backward adjoint"一条另标 `conjecture`。（2026-10-31 修订：§9 给出精确机制——加法 ⟷ way-below 逼近、乘法 ⟷ Scott 自同构、下拓扑/后向 ⟷ 互反对合；§6 的"下拓扑 ⟷ 乘法"措辞已按 §9 更正。）

| 拓扑 | 直觉 | \([0,1]\) 上 | 对 AEG 的候选对应 |
|---|---|---|---|
| Scott \(\sigma\) | 有限信息、从下逼近、可有限观测 | 右半开 \((a,1]\) | 单侧、前向、累积、加法侧、下半连续、`ev` 保定向并 |
| 下拓扑 \(\omega\) | 从上逼近（对偶 Scott） | \([0,b)\) | 单侧、后向、乘法 / 尺度侧 |
| Lawson \(\lambda=\sigma\vee\omega\) | 两侧同时确定，对称、Hausdorff | 欧氏拓扑 | 双面合成、恢复经典（接触 / 空间）几何 |

三条具体对应（逐条标地位）：

1. **way-below ⟷ "概念 = 过程的压缩，过程 = 概念的展开"** — `structural proposal`。\(x\ll y\) 是"\(x\) 是 \(y\) 的有限逼近"；\(\mathcal P(S)\) 里"有限子集 = 紧致元"几乎逐字对应 AEG 里"有限表达式树 / 有限运算历史 = 可计算对象"的地位。AEG 缺的严格版本就是："有限历史"在数学上是什么——候选答案是"紧致元 / way-below 元"。

2. **Scott 连续 = 保定向并 ⟷ "求值 ev 的极限判据"** — `structural proposal`。候选定义：**求值 ev 连续 ⟺ 极限过程的语义值 = 其有限历史逼近的定向并（下极限）**。这是 `08` §22.3 所问"completed reading object 何时是 \(\mathbb R\)"的一个可能答案形状。

3. **"补上对偶侧 = 从 Scott 升到 Lawson" ⟷ `02-mixed-affine-integration` 的 backward adjoint multiplier** — `conjecture`。Warner [3] 只用 Scott（单侧、无对合），天然对应 AEG 的前向 / 累积 / 加法一侧；`02` 里那个从未来端点往回传的 backward adjoint multiplier（\(p(b)=1\) 由未来向现在传播）是"下拓扑 / 对偶 Scott"一侧；两者合成（Scott \(\vee\) 下拓扑 = Lawson）才是完整、Hausdorff 的经典几何。**"补上 Warner 故意丢掉的对合"在拓扑语言里就是"从 Scott 升到 Lawson"**。这条目前是猜测，需与 `02` 的 backward adjoint 逐项对表后才可升级。

---

## 7. 地位标注与开放问题

**开放问题**（`open problem`，留待后续）：

1. AEG 的历史对象是表达式树 / rewrite 图 / DAG，**并不自动是 dcpo**。要落地必须先显式定义信息序（最自然候选：\(h\sqsubseteq h'\iff h'\) 是 \(h\) 的加细 / 延拓）并验证定向完备性。
2. "Scott ⟷ 加法侧、下拓扑 ⟷ 乘法 / 尺度侧"目前只是直觉映射，需要给出从 add/scale 过程到值格序的具体函子后才算成立。
3. 若对照表成立，AEG 的 add×multiply、forward×backward 双面结构应与 Scott/Lawson 双面结构对表；尚未证明。

（推进状态 2026-10-31：问题 1 → §8（脊髓历史部分解决，分支历史仍开放）；问题 2 → §9（已解决并修订 §6）；问题 3 → §10（已解决）；泛函层残余 → §11。）

---

## 8. 推进：信息序与 ideal completion（OQ-091 部分结论）

**2026-10-31**。本节把 §7 的开放问题 1 推进到 AEG 的固定历史类上——Paper I 的**标记脊髓历史**（`def:marked-spinal-history`，见 `paper-1/sections/02-sequential-histories.tex`）——给出信息序、验证 ideal completion 给出 dcpo，并判定求值是否保定向并。地位标注沿用 §0 约定。

### 8.1 信息序 = 时序前缀序

一个（自由）标记脊髓历史是有限时序词

\[
\gamma=(g_1,\ldots,g_n),\qquad g_i=C_{\omega_i,c_i}^{(\varepsilon_i)},\ \varepsilon_i\in\{1,2\}.
\]

`eq:chronological-history-concatenation` 定义时序拼接 \(\gamma\delta=(g_1,\ldots,g_m,h_1,\ldots,h_n)\)（\(\gamma\) 先、\(\delta\) 后）。定义

\[
\gamma\sqsubseteq\gamma' \iff \gamma'=\gamma\delta\ \text{对某个}\ \delta,
\]

即"\(\gamma\) 是 \(\gamma'\) 的一个有限前缀（更早的截断）"。`REFORMULATION`：这不是外加的序，而是 AEG 自己的时序拼接结构。按 §2 的"信息保留 / 遗忘"层级，更长历史保留严格更多的过程数据，所以"前缀 = 信息更少 = 有限逼近"是忠实的，不引入任何新数据。

（有界历史 \((x_0;\gamma)\) 的序取词部分的同一前缀序；初始累加器 \(x_0\) 固定，不影响序。）

### 8.2 定向完备性：ideal completion 就是"有限 ∪ 无限历史"

记历史字母表 \(\Gamma=\{C_{\omega,c}^{(\varepsilon)}\}\)，有限历史集 \(H=\Gamma^{*}\)（自由幺半群）。前缀序下：

- **定向集 = 链**：前缀序中两词有共同上界 ⟺ 一个是另一个的前缀；故定向集恰是一条前缀链，等于某个（有限或无限）词的全体有限前缀。`CLASSICAL`
- **ideal completion** \(\operatorname{Idl}(H)\cong\Gamma^{\infty}=\Gamma^{*}\cup\Gamma^{\omega}\)，即有限词与可数无限词全体，按前缀序。紧致元恰为有限词（主理想 \(\downarrow\gamma\)）；每个无限词 \(\gamma_{\infty}=(g_1,g_2,\ldots)\) 是它有限前缀的定向并：

\[
\gamma_{\infty}=\bigsqcup_{n\ge0}(g_1,\ldots,g_n).
\]

`CLASSICAL`（理想完备定理；这是标准的"无穷历史 / 流"domain 构造）。于是

\[
\boxed{
\text{有限历史}\ \subset\ \text{有限} \cup \text{无限历史}\ \cong\ \operatorname{Idl}(H),
\qquad
\text{有限} = \text{紧致} = \text{可计算逼近}.
}
\]

`REFORMULATION`：这给 AEG 的"概念 = 过程的压缩，过程 = 概念的展开"补上严格收敛语义——**极限历史 = 有限历史逼近的定向并**。

### 8.3 求值是否保定向并：自由 dcpo 泛性质给出精确判据

自由 dcpo 泛性质（`CLASSICAL`）：对任意 dcpo \(D\) 与单调映射 \(f:H\to D\)，存在唯一 Scott 连续扩张

\[
\hat f(\gamma_{\infty})=\bigsqcup_{n\ge0} f(g_1,\ldots,g_n),
\]

且反过来 Scott 连续的 \(\hat f\) 在 \(H\) 上的限制必单调。**因此求值 \(\operatorname{ev}_x\) 可 Scott 连续扩张到全部（有限 + 无限）历史 ⟺ \(\operatorname{ev}_x\) 单调。**

对普通算术求值 \(\operatorname{ev}_x(\gamma)=g_n\circ\cdots\circ g_1(x)\)（`eq:ordinary-history-evaluation`），结论是**否定的**，障碍有两处（`computationally verified example` + 观察，不是一般定理）：

1. **值域不是 dcpo**：域 \(K\)（如 \(\mathbb R\)）带通常序没有无界定向集的并，不是 dcpo；需取完备化（如 \(\mathbb R\cup\{+\infty\}\)）或连续格（如 \([0,1]\)，正是 Warner 的取值格）。
2. **\(\operatorname{ev}_x\) 偏且不单调**：第二槽除法 \(c/z\) 使求值偏；且 \(x\mapsto1/x\) 在 \((0,\infty)\) 反序，\(x\mapsto x^{2}\) 在 \(\mathbb R\) 不单调。故普通求值不满足自由 dcpo 定理的单调前提。

因此：**普通算术求值不是序连续的；要使其 Scott 连续，必须（a）把值域换成连续格 / 下半连续格，且（b）限制在求值单调的单侧 sector 上**。这正是 §6 把"下半连续 ⟷ 单侧累积"列为核心对应的原因，也是 projective continuation（`paper-1/sections/03-projective-affine.tex`）所要解决的偏性问题的序论表述。`structural proposal`

### 8.4 本节结论与仍开放的部分

**已解决**（对标记脊髓历史）：信息序（= 时序前缀序）、定向完备（= ideal completion ≅ 有限 ∪ 无限历史，有限 = 紧致）、求值可 Scott 连续的精确判据（⟺ 单调）。

**仍开放**（`open problem`）：

1. 分支历史（非脊髓，`thm:sequential-tree-classification` 之外）的信息序与定向完备；候选序是依赖偏序 / 子树加细，不是前缀序。
2. 把判据落实：在某个具体 sector（如下半连续 / 单调 sector）与具体值格（如 \([0,1]\)）上构造单调的 \(\operatorname{ev}_x\)，得到可 Scott 连续的求值扩张。
3. 与 projective continuation 对表：普通求值的偏性（除法零点）在 projective 完备化后是否恢复为某 dcpo 上的 Scott 连续映射。

---

## 9. 推进：加 / 乘两侧的序论安放（OQ-092）

**2026-10-31**。本节把 §6 的对照表落实为精确命题，并**修订**其中一处不精确：乘法本身是保序的，不是反序的；承载"Scott vs 下拓扑"对偶的是**互反对合**（reciprocal involution），而不是乘法本身。

### 9.1 具体映射：值格 \([0,\infty]\) 与两类生成元

取连续格 \(L=[0,\infty]\)（非负扩张实数，通常序；Warner 值格 \([0,1]\) 的等价版本）。把 AEG 的两个生成方向嵌入 \(L\) 的 Scott 连续自映射幺半群：

\[
T_s(a)=a+s\quad(s\ge0),\qquad D_k(a)=ka\quad(k>0).
\]

`REFORMULATION`：这正是 Paper 0 的 add/scale 过程在值格上的作用——加法对应 \(D_u=\partial_u+\mu\partial_a\) 的平移，乘法对应 \(D_v=\partial_v+\lambda a\partial_a\) 的伸缩（正乘性 sector）。

### 9.2 精确不对称：加法 = way-below 逼近，乘法 = Scott 自同构

`CLASSICAL`（domain theory），实例化到 AEG 生成元（`REFORMULATION`）：

1. **\(T_s\) 是 Scott 连续嵌入但不是自同构**：\(T_s\) 保定向并（\(\sup_i(a_i+s)=\sup_i a_i+s\)），但像 \([s,\infty]\subsetneq[0,\infty]\)，非满。且加法**正是 way-below 的见证**：

\[
a\ll b \iff a<b \iff \exists s>0:\ T_s(a)=a+s\le b,
\]

（底元 \(0\) 紧致，\(0\ll0\) 是唯一例外）。即**加法过程 = Scott 拓扑的"有限逼近"原始结构**。

2. **\(D_k\) 是 Scott 自同构（序自同构）**：\(D_k\) 双射、保序、逆 \(D_{1/k}\)，故是序自同构，从而是 Scott 拓扑的自同胚。即**乘法过程 = Scott 拓扑的"尺度对称"原始结构**，在 \(\log\) 坐标下化为平移。

### 9.3 对偶侧由互反对合承载（不是乘法本身）

`CLASSICAL`：设 \(\neg:[0,\infty]\to[0,\infty]\) 为互反 \(\neg(a)=1/a\)（在 \((0,\infty)\) 上），\(\neg(0)=\infty,\ \neg(\infty)=0\)。它是**反序双射**，即序同构 \([0,\infty]\to[0,\infty]^{\mathrm{op}}\)，故是

\[
\neg:(L,\sigma)\xrightarrow{\ \cong\ }(L,\omega)
\]

的 Scott / 下拓扑同胚，且共轭乘法为逆：

\[
\neg\circ D_k\circ\neg = D_{1/k}.
\]

`computationally verified example`（平凡计算）。所以"前向 ↔ 后向"在乘性侧由 \(\neg\) 精确实现：前向尺度 \(e^{M}\) 与后向乘子 \(e^{-M}=1/e^{M}\) 正是 \(\neg D_{e^M}\neg\) 的一对。

`REFORMULATION`：\(\neg\) 就是 Warner 明确丢弃的 order-reversing involution（"No involution is required"）。§6 的"补上对合 = 从 Scott 升到 Lawson"现在有精确形式：**补上 \(\neg\) 就得到下拓扑 \(\omega=\neg_*\sigma\)，从而得到 Lawson \(\lambda=\sigma\vee\omega\)**。

### 9.4 结论与对 §6 的修订

**结论**（`structural proposal`，其中 9.2 / 9.3 的 domain 事实为 `CLASSICAL`）：
- 加法 ⟷ Scott（way-below / 逼近，前向累积）——由 9.2(1) 精确成立。
- 乘法 ⟷ Scott 自同构（尺度对称）——由 9.2(2) 精确成立。
- 下拓扑 / 后向 ⟷ 互反对合 \(\neg\)（reciprocal）——由 9.3 精确成立；\(\neg\) 把前向尺度共轭为后向乘子。

**对 §6 的修订**：§6 表里"下拓扑 ⟷ 乘法 / 尺度侧"的措辞不精确——乘法本身保序（Scott 连续），不是反序；真正的对偶载体是互反 \(\neg\)。§6 已加修订指针，与本节一致。

**仍开放**（`open problem`，并入 OQ-093）：把 \(\neg\) 与 `02-mixed-affine-integration.tex` 的 backward adjoint（\(p(b)=1\) 由未来向现在传播）逐项对表，确认 \(e^{-M}\) 就是该 backward 乘子。本节只做到电荷层面 \(e^{M}\leftrightarrow e^{-M}\)，尚未落到混合积分的算子方程。

---

## 10. 推进：Lawson = backward-adjoint 补全（OQ-093）

**2026-10-31**。本节把 `02-mixed-affine-integration.tex` 的 backward adjoint 与 §9 的互反对合 \(\neg\) 逐项对表，证明"从 Scott 升到 Lawson"正是"补上 backward adjoint 一侧"。

### 10.1 两个乘子

`02` 的绝对时间形式（`eq:transport`、`eq:adjoint-equation`）里，乘性电荷

\[
M(t)=\int_a^t v(s)\,\mathrm ds,
\]

给出**前向（过去）尺度** \(K(t)=e^{M(t)}\)（`eq:acs-path` 的直接路径权重），而**后向伴随乘子**（`prop:adjoint`）

\[
p(t)=\exp\!\left(\int_t^b v(s)\,\mathrm ds\right),\qquad p(b)=1,
\]

解 `-p'(t)=v(t)p(t)`，由未来端点向现在传播。

### 10.2 后向伴随 = 互反（\(\neg\)）像

直接计算（`computationally verified example`）：

\[
p(t)=e^{M(b)-M(t)}=e^{M(b)}\cdot e^{-M(t)}=e^{M(b)}\cdot\neg\bigl(K(t)\bigr),
\qquad
\neg(a)=\frac1a.
\]

所以**后向伴随乘子是前向尺度的互反（\(\neg\)）像，乘以归一化常数 \(K(b)=e^{M(b)}\)**；该常数正是终端条件 \(p(b)=1\) 钉住的参考尺度。

### 10.3 Scott ∨ lower = Lawson = 欧氏

由 §9.3，\(\neg\) 是反序同胚 \((L,\sigma)\to(L,\omega)\)，且 \(\omega=\neg_*\sigma\)。于是：

- **前向尺度 \(K\) 携带 Scott（下）侧信息**：\(K(t)>a\iff M(t)>\log a\)，是"从下超过阈值"（下半连续）观测；
- **后向伴随 \(p=\neg(K)\)（模常数）携带下拓扑（上）侧信息**：\(p(t)>a\iff M(t)<M(b)-\log a\)，是"从上低于阈值"观测；
- **两者之并 = \(\sigma\vee\omega\) = Lawson = 欧氏拓扑**（`CLASSICAL`，\([0,\infty]\) / 对数坐标 \([-\infty,+\infty]\) 上 Lawson 即通常拓扑）。

因此：**"backward-adjoint 补全" = 把 \(\neg(K)\) 加回 \(K\) = 从 Scott 升到 Lawson = 由非 Hausdorff 恢复到欧氏 / Hausdorff**。这正是 OQ-093 的题面。`REFORMULATION`（对应关系逐项精确），其中拓扑事实为 `CLASSICAL`。

### 10.4 结论与残余

**结论**：§6 的"补上对合 = 从 Scott 升到 Lawson"现在有精确的算子对应——对合是互反 \(\neg\)，backward adjoint \(p\) 是 \(\neg(K)\) 模常数，两侧之并恢复欧氏拓扑。

**残余**（`open problem` 备注，不阻塞本节结论）：加法源 \(u\) 通过 way-below（§9.2）进入，并经配对 \(\int p\,u\)（`eq:adjoint-pairing`）与后向侧相乘；"混合积分泛函 \(\mathfrak M\) 在 Lawson 拓扑下的连续性"这一**泛函层**陈述尚未表述，暂记为后续项。

---

## 11. 泛函层：混合积分是双侧配对（§10.4 残余的收尾）

**2026-10-31**。把 §10.4 的残余项精确化并回答。

### 11.1 残余项的精确重述

§10.4 问"混合积分泛函 \(\mathfrak M[u;v]\) 在 Lawson 拓扑下是否连续"。这需要先精确化：\(\mathfrak M\) 有两个自变量，分别生活在两个不同的单侧空间里——加法源 \(u\)（前向、way-below / Scott 侧，§9.2）与乘性密度 \(v\)（后向、\(\neg\)-对偶 / 下拓扑侧，§9.3、§10.2）。所以"Lawson 连续性"应读作：**\(\mathfrak M\) 对其两个自变量分别在各自单侧拓扑下连续，且其值由两侧配对决定**。

### 11.2 分别 Scott 连续（可证）

`CLASSICAL`（单调收敛定理 + 线性泛函），实例化到 AEG（`REFORMULATION`）。对非负密度 \(u,v\ge0\)：

1. **对 \(v\)（乘性 / 后向侧）Scott 连续**：固定 \(u\ge0\)，映射
\[
v\ \mapsto\ \mathfrak M[u;v]=\int_a^b u(x)e^{\int_x^b v}\,\mathrm dx
\]
单调（\(v\le v'\implies e^{\int_x^b v}\le e^{\int_x^b v'}\)）且保定向并（单调收敛），故 Scott 连续。
2. **对 \(u\)（加法 / 前向侧）Scott 连续**：固定 \(v\ge0\)，核 \(p=e^{\int_x^b v}\ge0\)，\(\mathfrak M[u;v]=\int_a^b u\,p\,\mathrm dx\) 是带非负核的线性泛函，单调且保定向并，故 Scott 连续。

### 11.3 双侧配对 = Lawson 的泛函形式

\(\mathfrak M=\int_a^b u\,p\) 是前向源 \(u\) 与后向场 \(p=K(b)\cdot\neg(K)\) 的**对偶配对**（`eq:adjoint-pairing`、`eq:mixed-as-adjoint-pairing`）。因此：

- \(u\) 单独只给 Scott / 下侧信息（加法、前向、way-below）；
- \(p\) 单独只给下拓扑 / 上侧信息（\(\neg\) 像、后向）；
- 二者各自的单侧空间都非 Hausdorff，**只有配对 \(\int u\,p\) 才恢复完整（双侧）值**——这正是 §10 的"Scott ∨ lower = Lawson"在泛函层的表达。`structural proposal`（对应关系），其中 11.2 的连续性为 `CLASSICAL`。

### 11.4 闭合

至此，笔记 09 的整条线闭合：Warner 引入（§0–§5）→ 历史 dcpo（§8，OQ-091）→ 加 / 乘序论安放（§9，OQ-092）→ backward-adjoint = \(\neg\)，Lawson = 欧氏（§10，OQ-093）→ 泛函层双侧配对（§11）。§7 的三个开放问题与 §10.4 的残余项均已推进到相应小节。

---

## 12. 收尾总结

**这条线的最终结论**（一条可回填 AEG 研究地图的闭合链）：

1. **信息序**：标记脊髓历史按时序前缀序 \(\gamma\sqsubseteq\gamma\delta\) 成 dcpo（ideal completion = 有限 ∪ 无限历史，有限 = 紧致）——§8。
2. **值格**：在连续格 \([0,\infty]\)（或 \([0,1]\)）上，加法 = way-below（逼近）、乘法 = Scott 自同构（尺度）、互反 \(\neg\) = 承载 Scott / 下拓扑对偶的反序对合——§9。
3. **backward adjoint**：`02` 的后向乘子 \(p=\neg(K)\) 模常数，两侧之并 = Lawson = 欧氏 / Hausdorff——§10。
4. **泛函层**：混合积分 \(\int u\,p\) 是前向源与后向场的对偶配对，分别 Scott 连续——§11。

一句话：**Warner 丢掉的 order-reversing involution，正是 AEG `02` 里 backward adjoint 的拓扑化身；补上它（Scott → Lawson）就是补上"从未来往回传"的那一侧，从而恢复完整的（Hausdorff）分析学。** `structural proposal`（整条链的定位），各环节的 domain 事实均为 `CLASSICAL`。

仍开放（移交，不属本笔记主线）：分支历史的 dcpo（§8.4，OQ-091 残余）。

---

**参考**（[3] 为本次引入来源）：

1. D. Scott, *Continuous lattices*, Proc. 1971 Dalhousie Conference, LNM 274, Springer (1972).
2. G. Gierz, K.H. Hofmann, K. Keimel, J.D. Lawson, M. Mislove, D.S. Scott, *A Compendium of Continuous Lattices*, Springer (1980).
3. M.W. Warner, *Fuzzy topology with respect to continuous lattices*, Fuzzy Sets and Systems 35 (1990) 85–91.
