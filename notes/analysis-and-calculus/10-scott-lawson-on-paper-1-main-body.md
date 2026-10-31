# Scott–Lawson 拓扑与 Paper I 主体部分

## 从 09 的词汇表下放到历史层与射影语义层

### Research Note v0.1

**2026-10-31**（v0.1：承接 `09-order-topology-scott-lawson.md` 的闭合链，把该拓扑框架落到 `paper-1` 的 §2–§3 主体上）

---

## 0. 位置与目标

`09` 已闭合一条线：信息序（§8）→ 值格上加 / 乘 / 互反的序论安放（§9）→ backward adjoint = ¬（§10）→ 泛函层配对（§11）。但那条线主要工作在**值格 `[0,∞]` 与分析层**（`02-mixed-affine-integration`）。本笔记把 `09` 的词汇表**下放到 Paper I 主体**——即 `paper-1/sections/02-sequential-histories.tex`（历史层）与 `paper-1/sections/03-projective-affine.tex`（射影语义层）——回答：在这套拓扑下，Paper I 的主体部分可以怎样更严密、更深入地研究。

**地位约定**沿用 `09` §0：所有 domain 事实标 `CLASSICAL`（Scott [1]、Gierz–Hofmann–Keimel–Lawson–Mislove–Scott [2]、Warner [3]）；把 domain 结构对应到 AEG / Paper I 的语句标 `structural proposal` 或 `conjecture`，不得当作已证结论。本笔记是研究地图，不是理论等价性的断言。

---

## 1. 关键观察：09 的三个生成元就是 Paper I 的三个初等 context

这是本笔记的支点，是一个**语法层面**的精确对应（`REFORMULATION`，不是类比）。`09` §9.1 在值格 `[0,∞]` 上引入

\[
T_s(a)=a+s\ (s\ge0),\qquad D_k(a)=ka\ (k>0),\qquad \neg(a)=\frac1a .
\]

对照 `paper-1` §3 的初等 context 表（`03-projective-affine.tex`，`eq:elementary-one-hole-contexts` 与矩阵表）：

| `09` 生成元 | Paper I 初等 context | 说明 |
|---|---|---|
| `T_s(a)=a+s` | `C_{+,s}^{(1)}[z]=z+s` | 加法平移，第一槽 |
| `D_k(a)=ka` | `C_{×,k}^{(1)}[z]=C_{×,k}^{(2)}[z]=kz` | 非零乘性伸缩 |
| `¬(a)=1/a` | `C_{/,1}^{(2)}[z]=1/z` | 第二槽除法，`c=1` |

即 `09` 的"加法 = way-below 见证、乘法 = Scott 自同构、互反 = 反序对合"这三个生成元，**逐字就是 Paper I 的三个初等 context**（加法、乘法、第二槽除法）。`09` 的拓扑结构因此不是外加在 AEG 之上的类比，而是直接长在 Paper I 的历史语言上。这是本笔记与 `09` 前文的关键差异：`09` §9–§11 把生成元作用在**值格**上，本笔记把它们读回**历史语言本身**。

（注意：`J(z)=-1/z=D_{-1}\circ\neg=\neg\circ D_{-1}` 与 `¬(z)=1/z` 只差一个 affine-sector 内的反射 `D_{-1}`；二者"补上对偶侧"的角色在 `B_∞` 陪集层面等价，见 §3。）

---

## 2. 主对应：Scott 侧 ⟷ affine sector，补上 ¬ ⟷ 补上 J，Lawson ⟷ PGL₂

`paper-1` §3 已经证明（代数层面）：

- affine / Borel sector `B_∞ = Stab(∞) = {z ↦ az+b} = ⟨T_b, D_a⟩`（`cor:affine-borel-sector`）——由平移与伸缩生成。
- 单个射影步 `J(z)=-1/z` 离开第一 Bruhat 胞腔；`PGL_2 = B_∞ ⊔ B_∞ J B_∞`（Bruhat 分解），且 `⟨T_s, D_q, J⟩ = PGL_2`（`thm:bilateral-pgl2-generation`，证明在 Paper 0）。

`09` 已经证明（domain 层面，`CLASSICAL`）：

- 加法 `T_s` = way-below 见证（`a ≪ b ⟺ a < b ⟺ ∃s>0: a+s ≤ b`，底元 `0` 唯一例外）→ Scott 拓扑的"从下逼近"原语（`09` §9.2(1)）。
- 乘法 `D_k` = Scott 自同构（尺度对称）（`09` §9.2(2)）。
- 互反 `¬` = 反序对合，`(L,σ) → (L,ω)` 同胚，`ω = ¬_*σ`（`09` §9.3）。
- Scott ∨ lower = Lawson = 欧氏 / Hausdorff（`09` §10.3）。

把两组事实并置（`structural proposal`，其中两组事实各自为已证 / `CLASSICAL`）：

\[
\boxed{
  \underbrace{\langle T_s, D_k\rangle = B_\infty}_{\text{affine sector}}
  \longleftrightarrow \text{Scott 侧（way-below 逼近 + 尺度自同构）}
}
\]

\[
\boxed{
  \underbrace{\neg = C_{/,1}^{(2)}}_{\text{第二槽除法（= 补上对偶侧，}\sigma\to\omega\text{）}}
  \qquad\Longrightarrow\qquad
  \underbrace{\langle T_s, D_k, \neg\rangle = \operatorname{PGL}_2}_{\text{全体射影变换}}
  \longleftrightarrow \sigma\vee\omega = \lambda = \text{Lawson（Hausdorff）}.
}
\]

一句话（`structural proposal`）：**Paper I 的"affine sector → PGL₂"二分，正是 `09` 的"Scott → Lawson"二分在群层面的化身**；"补上第二槽除法 `J/¬`" = "补上 Warner 丢掉的对合" = "从单侧（非 Hausdorff）升到双侧（Hausdorff）" = "从 `B_∞` 越到第二个 Bruhat 胞腔"。

这条对应给 Paper I §3 的代数二分补上序拓扑读法，是本笔记的核心结论。

**修订指针（2026-10-31，v0.3 校正）**：上面 `⟨T_s, D_k, ¬⟩ = PGL₂` 在**群生成**意义下正确（`D_{-1} = T_1¬T_{-1}¬T_1¬`，故 `⟨Aff^+,¬⟩ = PGL₂`）。需细化的是第一框：`T_s(s≥0), D_k(k>0)` 的**半群**闭包是 `Aff^+ = {ka+s : k>0, s≥0}`，其**群**闭包是 `B_∞^+ = {ka+s : k>0, s∈ℝ}`（`B_∞` 的单位分量），二者都**不含**反射 `D_{-1}`；全 `B_∞ = B_∞^+ ⊔ D_{-1}B_∞^+` 需要 `D_{-1}`，而 `D_{-1}` 借道 `¬`（引理 F）。故"Scott 侧"的载体应写 `Aff^+`（半群，=`B_∞ ∩ Stab([0,∞])`），且 `B_∞` 的反射已是对偶数据。详见 `11-oq094a-proof-skeleton.md` §6。

---

## 3. 需要诚实标注的三处域差别

对应是**生成元 / 群元素层面**的，但三个"空间"必须分清，不可混淆（`warning`）：

1. **值格 `[0,∞]` ≠ 累加器域 `P^1(K)`**。`09` 的 `T_s, D_k, ¬` 是 `[0,∞]` 上的自映射（值 / 电荷 / 尺度的大小）；Paper I 的 context 是 `P^1(K)` 上的群元素（累加器变量 `z` 的域）。对应成立是因为**同一批映射**既是 `[0,∞] ⊂ P^1` 的自映射、又是 `PGL_2` 的元素；但 `09` 的"反序""way-below"只在 `[0,∞]`（正半线）上有意义。

2. **`D_k` (k>0) 只对应正分量 `Aff^+`，不是整个 `B_∞`**。Paper I 的 `B_∞` 允许 `k<0`（反射 `D_{-1}`）；`09` 刻意取 `k>0` 以保持 `[0,∞]` 自映射。所以 `09` 的"单侧"结构 = Paper I 的**正分量** `Aff^+(1,ℝ) = {z ↦ az+b : a>0}`（`03` §"The positive real component"），而非全 affine sector。全 `B_∞` 已含一个反序元素 `D_{-1}`（`z ↦ -z` 在 ℝ 上反序）。

3. **`¬` 的反序只在每个连通半线上**。`z ↦ 1/z` 在 `(0,∞)` 与 `(-∞,0)` 上分别反序，但在 `0` 处有极点；它不是 `P^1` 上的全局序自同构。`09` 取 `[0,∞]` 恰好规避这一点。`J=-1/z` 与 `¬` 差一个 `D_{-1}`，二者"补上对偶侧"的角色在 `B_∞` 陪集层面一致（`B_∞ J = B_∞ ¬`）。

这三处差别不削弱主对应，但决定了主对应**只能逐条对表**（§9 的开放问题 1），不能一步到位断言 `B_∞ ≅` 某个 Scott 空间。

---

## 4. 历史层的拓扑：前缀 dcpo 的 Lawson = 乘积 / 康托 / Baire 拓扑

`09` §8 已给出：标记脊髓历史 `Γ^*`（自由幺半群）按前缀序 `γ ⊑ γδ` 成偏序，ideal completion `Idl(Γ^*) ≅ Γ^∞ = Γ^* ∪ Γ^ω`，紧致元 = 有限词。本笔记补充其**拓扑**内容（`REFORMULATION`，domain 事实为 `CLASSICAL`）：

- **Scott 基** = `{↑γ : γ ∈ Γ^* 有限}`，即"前缀 `γ` 已发生"这个有限信息可观测量（`↑γ = {δ : γ ⊑ δ}`）。
- **Lawson = Scott ∨ lower** = 由 `{↑γ} ∪ {Γ^∞ \ ↑γ}` 生成 = 所有柱集 = **词上的乘积拓扑**。

具体地（`CLASSICAL`，经典 `Σ^∞` 例子实例化）：

- `Γ` 有限（如 Hecke 字母表 `{t_+, t_-, j}`，3 个字母）→ `Γ^ω` = **Cantor 空间**，`Γ^∞` = Cantor 空间 + 有限词作为（孤立）紧致元；
- `Γ` 可数无穷 → `Γ^ω` = **Baire 空间**；
- `Γ` 不可数（`K = ℝ` 时全 context 集）→ 超出经典 `Σ^∞` 的可数约定，需另行说明（`open problem`）。

**对 Paper I 的含义**：`def:marked-spinal-history` 的历史空间在 Lawson 拓扑下是一个干净、Hausdorff、且（有限字母表时）紧的对象；"有限历史 = 紧致元 = 可计算逼近"因此有了拓扑实现。而 Hecke 子语言 `Hist_4`（3 个生成元，`03` §"A distinguished arithmetic sublanguage"）的历史空间正是 **Cantor 空间**。

**措辞更正（2026-10-31）**：上一版此处写"`G_4` 作用在其边界（Cantor 集）上"**不精确**。`G_4 = H(√2)` 是第一类 Fuchsian 格，极限集 = 整个圆周 `P^1(ℝ)`（非 Cantor 集）；Cantor 集是**端空间**（因 `G_4 ≅ C₂*C₄` 殆自由）。历史 Cantor 空间编码的是**端空间**，不是极限集。详见 `16-hecke-history-boundary.md` §3–§4。

---

## 5. 射影求值 ρ 与 Scott 连续性的边界（精确的负结果）

这是 `09` §8.4 开放问题 3（"与 projective continuation 对表"）的精确回答（`structural proposal`，其中自由 dcpo 泛性质为 `CLASSICAL`）。

- 前缀序下 `γ ⊑ γδ`，但 `ρ(γδ) = ρ(δ)ρ(γ)`（`eq:rho-chronological-antihomomorphism`）：`ρ(γδ)` 是 `ρ(γ)` 被 `ρ(δ)` **左乘**，不是 `ρ(γ)` 的"上界"。
- 值对象 `PGL_2` 是群，不带信息序 / dcpo 结构；因此在给定一个 `PGL_2`（或其子集）上的偏序之前，"ρ 是否 Scott 连续"**不是良定义的问题**。可归约到值格的方向（把 `ρ(γ)` 读成 `[0,∞]` 值可观测量，如尺度 `K=e^M`）恰好回到 `09` §9–§11，而不是一个直接的 ρ 连续性。
- 更本质地：无限历史 `γ_∞ = ⊔_n γ_n` 的"射影值" `ρ(γ_∞)` 是无限矩阵乘积 `⋯ M_n ⋯ M_1`，其收敛正是**连分数 / 无限乘积收敛**问题——即 `AGENTS.md` 与 Paper 0 scope 明确排除的"infinite arithmetic expressions 的一般收敛理论"，属于 Paper II / III。

所以 Scott 拓扑给出一个**精确的负边界**："射影算子的 Scott 连续性" = "无限算术表达式的收敛性" = 越出 Paper I 主体范围。这为 Paper I 的 scope 边界（§3 只做有限词、把收敛留给下游）提供了一个序拓扑理由，而不是随意的范围截断。

---

## 6. 分支历史：OQ-091 的残余，及 Birkhoff 对偶的入口

`paper-1` §2 的 `thm:sequential-tree-classification` 把"内部依赖偏序 = 链"与"唯一合法求值序"等价；分支树（`fig:sequential-branching-dependency`）的依赖偏序 `P = I(T)` 不是链，有多个合法求值序（多个线性扩展）。`09` §8.4 开放问题 1 正是这个分支情形的 dcpo。本笔记给出候选方向（`open problem`，全部不得提前断言）：

- **信息序候选**：子-DAG / 子树加细，即"`h` 是 `h'` 的一个子计算"；不是词前缀序。
- **定向完备候选**：有限子-DAG 按包含序的 ideal completion = 全体（含无穷）DAG；紧致元 = 有限 DAG。
- **结构提示**：分支树的一个"合法求值序" = 依赖偏序 `P` 的一个线性扩展 = 一条脊髓历史。`P` 的全体下集格 `O(P)`（自由分配格）及其 ideal completion 是经典 Birkhoff 对偶 / 序结构的领地；Scott 拓扑应落在 `O(P)`（或线性扩展空间）上，而非单条词上。

这会把 Paper I §2 的分类从"链 vs 分支"的二分，深化为"单条脊髓历史 = `P` 的线性扩展；分支树的完整空间 = `O(P)` 上的 Scott 拓扑"。

---

## 7. 边界：泛函层属于 Paper 0，不属于 Paper I 主体

`09` §11 的混合积分 `𝔐 = ∫ u·p` 双侧配对，作用于 `02-mixed-affine-integration` 的分析对象（加法源 `u`、乘性密度 `v`、backward adjoint `p`），属于 Paper 0 的几何 / 分析层，不是 Paper I 主体（§2 历史层 + §3 射影语义层）的对象。因此 `09` §11 的结论不回填 Paper I 主体；Paper I 主体可回填的是本笔记 §1–§6（生成元对应、主对应、历史拓扑、ρ 负结果、分支 dcpo）。

---

## 8. 研究计划（按可证性排序）

| # | 命题 | 地位 | 可否立即证 |
|---|---|---|---|
| 1 | 生成元对应（§1）| `REFORMULATION` | 是（语法核对）|
| 2 | 历史 Lawson = 乘积 / 康托 / Baire（§4，`Γ` 可数）| `CLASSICAL` 实例化 | 是 |
| 3 | ρ 的 Scott 连续性不成立 / 不良定义（§5）| 自由 dcpo + 观察 | 是（负结果，短证明）|
| 4 | 主对应 Scott ⟷ affine、Lawson ⟷ PGL₂（§2）| `structural proposal` | 部分（生成元与 Bruhat 已证；拓扑读法是提议）|
| 5 | Hecke 历史空间 = Cantor + `G_4` 边界作用（§4 末）| `structural proposal` | 历史空间部分是 `CLASSICAL`；与 `G_4` 边界作用的对应需对表 |
| 6 | 分支历史 dcpo（§6）| `open problem` | 否（需显式构造）|
| 7 | 不可数字母表 `Γ` 的 `Σ^∞` 推广（§4）| `open problem` | 否 |

---

## 9. 开放问题清单（移交 08 寄存器）

1. **OQ-094a**：主对应"Scott ⟷ affine sector、Lawson ⟷ PGL₂"能否从 `structural proposal` 升级为定理？需要把 `[0,∞]` 值格的 Scott / Lawson 结构、与 `B_∞` / `PGL_2` 的群结构，用显式函子对表（含 §3 的三处域差别）。
2. **OQ-094b**：ρ 的 Scott 连续性边界（§5）：写出"无限矩阵乘积收敛 ⟷ 越界"的干净陈述与边界刻画。
3. **OQ-094c**：分支历史的 dcpo（§6）：子-DAG 加细序的定向完备、紧致元、Scott 拓扑在 `O(P)` 上的落点。
4. **OQ-094d**：Hecke 历史空间（Cantor）与 `G_4` 边界作用的对应，能否给出 `rem:hecke-history-operator-coset` 的历史层拓扑实现。
5. （OQ-091 已有，沿用）单调 sector + 值格 dcpo 的具体实例化；与射影 continuation 的调和。

---

## 10. 收尾

一句话：**`09` 的拓扑框架逐字长在 Paper I 的历史语言上（`T_s, D_k, ¬` 就是 `C_{+,s}^{(1)}, C_{×,k}^{(1)}, C_{/,1}^{(2)}`）；"Scott → Lawson" 在 Paper I 主体里就是 "affine sector → PGL₂"；而 ρ 的 Scott 连续性边界精确刻画了 Paper I 与"无限算术表达式收敛理论"（Paper II / III）的分界。**

仍开放（移交）：主对应的函子化升级、分支 dcpo、Hecke 边界作用。

---

**参考**（沿用 `09`）：

1. D. Scott, *Continuous lattices*, Proc. 1971 Dalhousie Conference, LNM 274, Springer (1972).
2. G. Gierz, K.H. Hofmann, K. Keimel, J.D. Lawson, M. Mislove, D.S. Scott, *A Compendium of Continuous Lattices*, Springer (1980).
3. M.W. Warner, *Fuzzy topology with respect to continuous lattices*, Fuzzy Sets and Systems 35 (1990) 85–91.
