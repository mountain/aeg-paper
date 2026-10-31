# Donaghey / De Bruijn–Morselt 变换：一般树 ↔ 二叉树，与 AEG 树层的对应

## 右/左双射 = 左右梳；σ/θ/φ 分解 = 镜像/反演/词编码

### Research Note v0.1

**2026-10-31**（v0.1：读 Donaghey 1980、Pushkarev–Byzov 2014、OEIS A014486 图表。结论：(1) **右/左双射 = AEG 左右梳**，精确；(2) **σ/θ/φ 分解 = AEG 镜像/反演/词编码的显式组合学模型**，精确；(3) **Donaghey 的 σ、θ 生成自由积 `Z₂*Z₂`（无限二面体）、复合 τ 无限阶，而 AEG 词层的镜像+反演生成 `Z₂×Z₂`（Klein）——这是真实的非交换差异，登记为 OQ-098 核心**）

---

## 0. 材料与目标

**材料**（`temp/`，用户 2026-10-31 新增）：

- **Donaghey 1980**：R. Donaghey, "Automorphisms on Catalan Trees and Bracketings", *J. Combin. Theory Ser. B* **29** (1980), 75–90。
- **Pushkarev–Byzov 2014**：I. A. Pushkarev & V. A. Byzov, "Donaghey's Transformation: An Elementary Approach", *J. Math. Sci.* **196** (2) (2014), 199–215（译自 Зап. научн. сем. ПОМИ **411** (2013), 148–177）。
- **图表**：OEIS A014486 插图（Antti Karttunen, 2011），Catalan 结构对应表。

**目标**：把"一般树 → 二叉树"变换（R/L 双射、σ/θ/φ 分解、carousel、fringing、轨道结构）精确对接到 AEG 的树层（顺序/分支两类树、镜像/反演/路径逆、左右梳、Birkhoff 分配格），并登记残余开放问题。

---

## 1. `[Donaghey 1980]` 四族 Catalan 与 R/L 双射

四个 Catalan 族（皆 $c_n$ 计数，`CLASSICAL`）：

- **g.b.** general bracketings（一般括号化，$n$ 对括号，可 $k$-叉）；
- **b.b.** binary bracketings（二叉括号化，非结合 $(n{+}1)$ 项和，含一对外括号）；
- **p.t.** plane trees（平面树，$n$ 边）；
- **t.p.t.** trivalent plane trees（三叉平面树）。

外加两族：**z.t.** zigzag trees（t.p.t. 去叶保留左右斜）、**+.b.b.**（b.b. 删项留 `+`）。

自然对应（§I）：`+.b.b. ↔ z.t.`（`+` ↔ 顶点，嵌套括号 ↔ 祖先关系）；`(g.b.) ↔ p.t.`（每对括号 ↔ 顶点，即 De Bruijn–Morselt 的 **up-down code**，也即 Dyck 词）。

**两镜像映射 R、L**（Definition 1）：$g.b.\to +.b.b.$，
- **R**：把每个**右括号**换成 `+`，再唯一地补右括号；
- **L**：把每个**左括号**换成 `+`，再唯一地补左括号。

递归结构（Property 1）：

$$
(g_1)(g_2)\cdots(g_m)\ \xrightarrow{R}\ (b_1+(b_2+(\cdots+(b_m+)\cdots))),
\qquad
\xrightarrow{L}\ ((((\cdots+b_1)+b_2)\cdots)+b_m).
$$

**即 R = 右梳、L = 左梳**。复合得到四个自同构：$M_G=L^{-1}R$（g.b.）、$M_B=RL^{-1}$（+.b.b.）、$M_P=L^{-1}R$（p.t.）、$M_Z=RL^{-1}$（z.t.）。关键：$M_P$ **"把串行结构变成并行结构，反之亦然"**；$M_Z$ **"把左斜边变成右斜边"**。

**Motzkin 族（§V）**：primitive 元素 = 无 `((g))`、无 `)( )(` 者；$p_n=m_{n-2}+m_{n-1}$（Motzkin 数）；**Y-branching p.t.**（度 $\le3$）↔ Family A（无 `(g)(g)(g)`），**branch-reduced p.t.** ↔ Family G（无 `((g))`）；$M_P$ 把 Y-branching ↔ branch-reduced 双射。

---

## 2. `[Pushkarev–Byzov 2014]` 三定义、σ/θ/φ、轨道结构

**PPCT** = plane planted cubic tree（三叉平面树，根有一子，内部顶点二子）。

### 2.1 三个等价定义（Theorem 2.1）

- **(2.1) 归纳式**：右分解 $T=[T_0(\alpha_0),\dots,T_{n-1}(\alpha_{n-1}),\alpha_n]$ → 递归变换各子树 → 左分解 $T'=(\alpha_0,T_0'(\alpha_1),\dots,T_{n-1}'(\alpha_n))$。
- **(2.2) 双射复合**：$T\to T^R$（**右双射**：PPCT→PPT）$\to T'$（**左双射逆**：PPT→PPCT）。
- **(2.3) §3 核心**：$T'=\varphi^{-1}\circ\theta\circ\varphi\circ\sigma\,(T)$，其中
  - **σ = transposition**：左右儿子互换（手性翻转）；
  - **θ = reflection**：Dyck 路径反向（"going backwards along a path"）；
  - **φ = PPCT ↔ 正 Dyck 路径**（$2(n{-}1)$ 步）的标准双射（up-down code）。

### 2.2 右/左双射 = "顶点 ↔ 路径"

右双射把 PPT 的每个顶点映成 PPCT 的**右路径**；左双射映成**左路径**；逆映射把"路径"还原为"顶点"。即：**一般树（PPT）的每个顶点，在二叉树上展开成一条左/右梳**。这是"一般树 → 二叉树"的精确内容。

### 2.3 §3–§4：Dyck 路径与三角剖分、carousel

- σ 在 Dyck 路径上：零层顶点把每个 Dyck 路径切成**不可约子路径**；σ 交换它们（Fig 7/8，regular/special 两 case）。
- 三角剖分上：右/左后代序列的计数器 = **caterpillars**（所有三角形共享顶点于割线之右/左）；**"把每条 caterpillar 的割线顺时针移动一位"**——即 **carousel effect**。
- **Theorem 4.1/4.3（细分 carousel）**：PPCT 的角分五类 SR、LL、RL、RN、LN（另加根角），变换让它们循环搬运：
  SR → 第 1 个 LL；第 $k$ 个 LL → 第 $k$ 个 RL；第 $k$ 个 RL（非末）→ 第 $k$ 个 RN；末 RL → SR；第 $k$ 个 RN → 第 $k$ 个 LN；第 $k$ 个 LN → 第 $(k{+}1)$ 个 LL。
- **Corollary 4.4**：$(k,l,m,n)(T')=(n+1,\ k,\ l-1,\ m)$；**Corollary 4.5（交替不变量）**：若 $T_1\equiv T_2$ 则 $(k,l)$ 或 $(l,k)$ 相同——轨道落在 $T(k,m)\cup T(m,k)$。

### 2.4 §5–§6：双曲性、germ、fringing、轨道

- **双曲性**：变换对"所有树的标准格序"**非单调**；germ（边的分割）在迭代中移动/坍缩（Theorem 5.1），且**不能构造"温顺"理论**。
- **PPCT 形成分配格**（不可约元按无限三叉树排序）——原文断言，待核实（见 §7）。
- **Fringing（Definition 6.1）**：对每个叶加左右二子，得 $Q(T)$；$Q$ 是 fringing。
- **Theorem 6.1**：$\Delta(T)$ 奇 ⟹ $\Delta(Q(T))=3\Delta(T)$；偶 ⟹ $=\tfrac32\Delta(T)$。
- **Theorem 6.2**：三次变换后，内部边 ↔ regular fringes ↔ singular fringes 循环。
- **Corollary 6.3**：存在轨道长 $O(n^{\log_2 3})$ 的无限族——**双曲/分形增长**（Pushkarev 称"fractal rotation"）。
- **Corollary 6.5**：$n=2^k m$（$m$ 奇）时 $T(n)$ 轨道数 $\ge d_k^{(m)}$。
- **Theorem 6.4**：σ、θ 生成**自由积 `Z₂*Z₂`**（无限二面体）；"在所有树上，Donaghey 变换作为自由循环群作用"。

### 2.5 §7：经验数据

多项式 $M_n(x)$（$x^i$ 系数 = 长度 $i$ 的轨道数）：$M_1=x,\ M_2=x,\ M_3=x^2,\ M_4=x^2+x^3,\ M_5=x^2+2x^6,\ M_6=2x^2+3x^3+x^5+4x^6,\dots$（前十个 Donaghey 已给；$M_6$ 原式缺 $x^{18}$ 系印刷错误）。

---

## 3. `[OEIS A014486 图表]` Catalan 罗塞塔

一行逐列：A014486 项 / A063171 项 → **Dyck 山形（配括号化）** → 非交叉弦图 → **平面一般树（Łukasiewicz 词，A079436）** → 非交叉分划 → Murasaki 图 → **平面二叉树（内嵌 zigzag 树）** → 三角剖分。

即：一般树 ↔ 二叉树 ↔ Dyck 路径 ↔ 三角剖分 ↔ 弦图 均在同一表内逐行对应——R/L 双射的可视化完整版。

---

## 4. `[对应]` 与 AEG 树层的精确对齐

| Donaghey/PB | AEG | 状态 |
|---|---|---|
| **σ**（左右儿子互换） | 镜像 $m$：$m(C_{\omega,c}^{(\varepsilon)})=C_{\omega,c}^{(3-\varepsilon)}$（`def:mirror-temporal-reversal`）| 精确一致 |
| **θ**（Dyck 路径反向） | 时间反演 $r$：$r\gamma=(g_n,\dots,g_1)$（`def:mirror-temporal-reversal`）| 精确一致 |
| **φ**（PPCT↔Dyck） | 历史=词编码（up-down code）| 精确一致 |
| **τ = φ⁻¹θφσ** | Donaghey 变换 | 结构对应（**不是** AEG 的 $mr$，见 §6）|
| **右/左双射（顶点↔右/左路径）** | 左/右梳 `conv:p0-left-right-convention` | 精确一致 |
| **四族 Catalan** | 二叉树（顺序）vs 一般树（分支） | 精确一致 |
| **primitive / Motzkin 族** | 与单脊/归约子集的关系 | **open** |
| **carousel / fringing / 轨道增长** | 与 Hecke 周期轨道/"fractal rotation" 的关系 | **open** |
| **PPCT 分配格** | AEG 的 Birkhoff 分配格 $\mathcal O(P)$ | **需核实**（见 §7）|

`[对应]`（`structural proposal`，非定理；前三行是精确结构对应，后三行登记为 open/待核实）。

---

## 5. `[对应]` 区分：全局双射 vs 逐树线性扩张

- **Donaghey/De Bruijn–Morselt**：**全族双射**——"{一般树 $n$ 边} ↔ {二叉树 $n$ 内部点}"，两侧都 $c_n$ 计数。
- **AEG**：**逐树关系**——一棵分支树 → 依赖偏序 $P$ → 线性扩张 = 脊历史（`thm:sequential-tree-classification`、`thm:birkhoff-downset-spinal`）；顺序（链）情形唯一，一般情形是一个**集合**（每个线性扩张一棵二叉树）。

两者**不同但互补**：Donaghey 是全族保计数的规范双射，AEG 是逐棵树的求值序结构。用 Donaghey 的右双射可以把"分支树"送成"二叉树家族中的一个代表"，但 AEG 关心的是"一棵分支树的全部线性扩张"，这是 Donaghey 双射不直接给出的。

---

## 6. `[对应]` 关键的非交换差异：`Z₂×Z₂` vs `Z₂*Z₂`

这是本笔记最重要的发现，也是 OQ-098 的核心。

- **AEG（词层）**：$m,r$ 都是对合；且**交换**（`def:mirror-temporal-reversal` 后：$m(r\gamma)=r(m\gamma)$）。故 $\langle m,r\rangle\cong \mathbb Z_2\times\mathbb Z_2$（Klein 四元群），$mr$ 阶为 2。
- **Donaghey（树层）**：σ、θ（经 φ 共轭到树上）**不交换**；Theorem 6.4 证 $\langle\sigma,\theta\rangle\cong \mathbb Z_2*\mathbb Z_2$（无限二面体），$\tau=\varphi^{-1}\theta\varphi\sigma$ 无限阶（Corollary 6.3：存在任意长轨道）。

**为什么不同**：AEG 的"反演"$r$ 是**词反向**（简单序列反转）；Donaghey 的"反射"θ 经 φ 落到树上得 $\tilde\theta:=\varphi^{-1}\theta\varphi$，它**不是**词反向，而是"Dyck 路径反向诱导的树结构重排"。词层的 $m,r$ 交换；树层的 $\sigma,\tilde\theta$ 不交换——这正是"双曲性/任意长轨道"的来源。

**结论**：Donaghey 的复合 $\tau$ 是 AEG "镜像+反演"复合的**非交换、无限阶版本**；AEG 目前只在词层拥有交换（Klein）版本，树层是否出现非交换（无限二面体）版本 = **OQ-098.1**。

`[对应]`（`structural proposal`；群论部分——Klein vs 无限二面体——是精确事实，但"树层是否出现该结构"是 open）。

---

## 7. 地位总表与残余

| 命题 | 地位 |
|---|---|
| §1 四族、R/L、$M_P$/$M_Z$ | `CLASSICAL`（Donaghey 1980）|
| §2 三定义、右/左双射、Theorem 4.1/4.3/6.1/6.2 | `CLASSICAL`（Pushkarev–Byzov 2014）|
| §2 Theorem 6.4（`Z₂*Z₂`）、Corollary 6.3/6.5 | `CLASSICAL` |
| §3 A014486 罗塞塔 | `CLASSICAL`（OEIS 图表，参考性）|
| §4 σ/θ/φ、R/L 与 AEG 的精确对应 | `[对应]` `structural proposal` |
| §5 全局双射 vs 逐树线性扩张 | `[对应]` 区分（非同一）|
| §6 `Z₂×Z₂` vs `Z₂*Z₂` 差异 | `[对应]` 群论事实精确，树层结构 open |

**残余（`open`，登记 OQ-098）**：

1. **非交换扩展（098.1）**：AEG 的镜像+反演在**树层**是否生成 `Z₂*Z₂`（无限二面体）而非词层的 `Z₂×Z₂`？若成立，"路径逆"与"路径反向诱导的树重排"为何在树层不再交换，就给出 AEG 的"双曲性/长轨道"结构。
2. **PPCT 分配格 vs $\mathcal O(P)$（098.2）**：原文断言 PPCT 形成分配格、不可约元按无限三叉树排序；这是 Tamari 型格还是别的格？与 AEG 的 Birkhoff 分配格 $\mathcal O(P)$ 是否同构/嵌入？
3. **carousel / fringing / 轨道增长（098.3）**：carousel（SR/LL/RL/RN/LN 循环搬运）、fringing（$\Delta$ 三倍）、$O(n^{\log_23})$ 轨道增长，是否对应 AEG 的 Hecke 周期轨道 / "fractal rotation"？需要 AEG 的轨道/周期结构才能对接。
4. **右/左双射的函子性（098.4）**：R/L 是否给"分支层 → 顺序层"的函子，且尊重 AEG 的序缺陷/线性扩张结构？（目前只是集合双射，未见函子性。）

---

## 8. 参考

- Donaghey 1980：`temp/1-s2.0-0095895680900453-main.pdf`；`J. Combin. Theory Ser. B` **29** (1980), 75–90。
- Pushkarev–Byzov 2014：`temp/Pushkarev-Byzov2014_Article_DonagheySTransformationAnEleme.pdf`；`J. Math. Sci.` **196**(2) (2014), 199–215。
- 图表：`temp/a014486.pdf`（OEIS A014486，Antti Karttunen 2011）。
- De Bruijn–Morselt 1967（up-down code，经 Donaghey 1980 引用）。
- AEG 侧：`paper-0/sections/03-aes-and-motion.tex`（`conv:p0-left-right-convention`）；`paper-1/sections/02-sequential-histories.tex`（`def:mirror-temporal-reversal`、`def:path-inverse`、`thm:sequential-tree-classification`、`thm:birkhoff-downset-spinal`）。
