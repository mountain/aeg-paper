# 020 — Add/multiply lines, graph potential, boundary-value satisfiability, and the cusped 4-gon on the Cayley model

> **Document nature**: research notes on Arithmetic Expression Geometry (AEG) (020: the Cayley model of the F₂/T₄ tree — "frame correction → node potential → boundary-value satisfiability → graph colouring → E₁-like square → cusped 4-gon").
> **Prerequisites**: Note XVII, *Cayley model and the conformal-hyperbolic unification* ([017-cayley-model-conformal-hyperbolic.md](017-cayley-model-conformal-hyperbolic.md)); Note XVIII, *Assignment, duality, add-multiply, Eikonal on the Cayley model* ([018-cayley-assignment-duality-eikonal.md](018-cayley-assignment-duality-eikonal.md)); Note XIX, *The Schwarz–Christoffel square* ([019_sc_square_eikonal.md](019_sc_square_eikonal.md)); `paper-0/sections/03-aes-and-motion.tex` (`prop:canonical-arithmetic-frame`).
> **Date**: 2026-11-15
> **Remark**: this note consolidates 041–046; the "level lines = add lines" claim of `040` is corrected by `041`.

---

## 1. Correction: add lines = horizontal, multiply lines = vertical (041)

In `paper-0`'s `prop:canonical-arithmetic-frame`, `J` is the **`g`-orthogonal rotation** (not the Euclidean 90°). Substituting

$$X_u=\frac{\mu}{q}E_a-\frac{\lambda a}{q}JE_a,\quad X_v=\frac{\lambda a}{q}E_a+\frac{\mu}{q}JE_a$$

with `q=√(μ²+λ²a²)` gives **`X_u=(−μy,0)` (horizontal), `X_v=(0,−λy)` (vertical)** (sympy-verified).

- **add lines** = horizontal `y=const` (along which `a=−x/y` varies linearly);
- **multiply lines** = vertical `x=const` (along which `a` scales as `1/y`);
- **add ⊥ multiply = 90°** (independent of `a`).

**The `040` error**: I had called the level lines (rays) "add lines". The level line `y=kx` (`k=−1/a`) makes with the add line (horizontal) the angle

$$\angle(\text{level},\text{add})=\arctan(1/|a|),$$

which **varies continuously with `a`** (90° at `a=0`, hugging the multiply line; 0° as `|a|→∞`, hugging the add line). This is the reviewer's "the angle depends on `a`".

## 2. Graph potential: node values (042)

**Setup**: tree nodes (4-valent branch points, `∇a` undefined) are singularities, edges are regular (carry the Eikonal flow), the origin is completed with `a=0`.

Along an edge `da/ds=±√(μ²+λ²a²)`, so `β(v)−β(u)=±λℓ_e` (`β=arcsinh(λa/μ)`). **The tree is acyclic ⟹ no cycle obstruction ⟹ a solution exists**:

$$\boxed{a(\text{node})=\frac{\mu}{\lambda}\sinh\big(\lambda\,d(\text{node})\big)},\quad d=\text{$g$-path-length from the root}.$$

Numerics (`μ=1,λ=2`, `g=(dx²+dy²)/L²`): root edge `g`-length `3ln2≈2.079`, node values `0→≈16→≈1023`; `da/ds=√(μ²+λ²a²)` matches to `1e-15`.

## 3. Boundary-value satisfiability criterion (043)

The strict 1D flow condition (the edge must be a characteristic):

$$\boxed{\ell_e=\frac{\big|\operatorname{arcsinh}(\lambda a_v/\mu)-\operatorname{arcsinh}(\lambda a_u/\mu)\big|}{\lambda}}$$

local = global (acyclic tree). Test (`μ=1,λ=2`):

| edge | `g`-length | required (odd ints) | result |
|---|---|---|---|
| **E₀** `ε₄→Jε₄` (`a:1→−1`) | 1.6227 | 1.4436 | **slack +0.179** (edge not characteristic) |
| **Cayley** (`a:0→1`) | 3ln2=2.0794 | 0.7218 | **+1.358** mismatch |
| **Cayley** (`a:1→3`) | 2.0794 | 0.5241 | **+1.555** mismatch |

**Two readings**: (2D Eikonal, no edge-length constraint) E₀ realizes the odd integers (`a=−x/y`), Cayley does not (its Eikonal solution gives `≈16,1023`); (1D flow) neither is strict — E₀ has slack, Cayley is worse; the only strict solution is `a=(μ/λ)sinh(λd)`.

## 4. Graph-potential colouring (044)

Nodes coloured by `a=(μ/λ)sinh(λd)` (log scale), edges by the flow rate `√(μ²+λ²a²)`; the right panel colours by the `g`-distance `d`. 53 nodes, `a:0→6.5×10⁴`, `d:0→6.24`.

## 5. The E₁-like blue square (045)

Blue lines (dual `{4,∞}` perpendicular bisectors) bound closed squares (root square `[−4,4]²`). With **`a=0` on the blue boundary + Eikonal inside**:

$$a_{\text{centre}}=\frac{\mu}{\lambda}\sinh(\lambda\cdot\text{inradius}),\quad \text{inradius}=\int\frac{dx}{L}.$$

Self-similarity gives **`inradius=ln2` for every square**, hence

$$a_{\text{centre}}=\tfrac12\sinh(2\ln2)=\boxed{\tfrac{15}{16}}\quad(\text{all squares}).$$

**Key distinction**: the source-free fill is constant `15/16`; **the differing number is the centre "source strength" `a(node)`** (`0,16,1023,…`, the potential). So "E₁ + centre puncture source" is right, but the "pole value" is the **source strength**.

**± symmetry**: `sinh` is odd, so `a(d)` and `−a(d)` both solve the flow (`0→−16→−1023` is a valid mirror). **Inversion**: `1/a` is **not** an Eikonal solution — `|∇(1/a)|²=λ²b²+μ²b⁴` (quartic dual); only the value **rotation** `a→e^{iθ}a` is a symmetry.

## 6. The cusped 4-gon (046)

The 4 corners of a blue square = the dual `{4,∞}` vertices = the primal `{∞,4}` face centres = the **parabolic cusps `Q√2 ∪ {∞}`**. Making the 4 corners singular changes three things:

1. **Geometry**: `E₁` (one-puncture disc) → **cusped 4-gon** (4 parabolic vertices; `a=0` on the sides, `a=∞` at the corners — a mixed boundary condition);
2. **Potential**: node graph → **node + cusp bipartite graph** (the cusps carry "cusp potentials" / pole residues);
3. **Value function**: one puncture → **4 cusps + centre source** composite profile (the constant `15/16` is replaced by a cusp-dominated profile).

## 7. Status summary

| result | status | verification |
|---|---|---|
| `X_u=(−μy,0)`, `X_v=(0,−λy)`, add ⊥ multiply | `PROVED` | sympy vs `prop:canonical-arithmetic-frame` |
| level-vs-add angle `arctan(1/|a|)` | `COMPUTATIONALLY VERIFIED` | numeric |
| `a(node)=(μ/λ)sinh(λd)`, acyclic consistency | `PROVED` | analytic + `1e-15` |
| criterion `ℓ_e=|β(Δa)|/λ` | `PROVED` | analytic + numeric |
| odd integers unrealizable in Cayley; 2D-realizable in E₀ with 1D slack | `PROVED` | exact numerics |
| graph colouring (potential / flow) | `COMPUTATIONALLY VERIFIED` | `044` |
| blue square `inradius=ln2`, source-free centre `15/16` | `PROVED` | numeric |
| inversion `1/a` not an Eikonal solution (quartic dual) | `PROVED` (refuted) | numeric |
| "E₁ + centre source strength = potential" | `STRUCTURAL PROPOSAL` | geometry exact, arithmetic open |
| 4 corners = cusps, upgrade to cusped 4-gon | `STRUCTURAL PROPOSAL` (corner=cusp exact) | `016/017` + `046` |

## 八、从 HTWR 回到 tube：研究来路、差距与暂缓记录（2026-11-15）

**性质与基线。** 本节是研究动机、未解接口与阶段性取舍的记录，状态为 OPEN PROBLEM / STRUCTURAL PROPOSAL；不新增存在性定理。基线为本仓库提交 [1be194f](https://github.com/mountain/aeg-paper/commit/1be194fb85efb426388d54c47dcda00f1df823c2)。研究动机与历史解释由苑明理于 2026-11-15 补充；来源核对、难度评估与本节整理由 OpenAI ChatGPT（Codex）协助完成。

**长期动机。** 希望构造一个真正非平凡的 AES 切片族：切片具有多条有结构的零线，不能仅把基本模型 $E_0$ 换坐标；同一算术历史随参数变化形成穿线，其赋值由多项式描述。随后利用求根、因式分解、消元等计算，分析切片本身或明确声明的零线关系商空间。完成标准包括一次具体的“代数计算给出几何信息”，而不止画出零网络或写出端点多项式。

[2025-05-16 的讨论记录](../foundations-and-geometry/02-parameterized-evaluation-frameworks.tex)已提出 multiplicative tube：固定加法、改变乘数 $u$，固定抽象字 $\gamma$ 给出 $P_\gamma(x_0,u)$；并记录了苑明理对基本模型过于刚性、可变量分离的质疑，以及寻找“几何化条件”的目标。该旧稿的自动纤维丛、维数等表述只作历史材料，不在本节恢复为定理。[旧 Cayley 构造](../foundations-and-geometry/01-cayley-hyperbolic-model.tex)则探索自由群树、递归方格和边界深度度量。

按苑明理本次说明，近期 HTWR 的 Pell 试验场重新激活了这一长期问题：$\mathbb Q[\sqrt2]$ 在旧 tube 方案中的作用，使研究从虫洞约分细节转向非平凡切片及穿线。最近的[笔记 014](014-pell-master-figure.md)、[015](015-pell-hecke-belyi-thread.md)、[016](016-c2c4-tearing-belyi-f7.md)把 Pell、Hecke 零网络、自由积骨架与多项式联系起来，017–020 进一步尝试 Cayley 度量、赋值与面内填充。这是研究线索的重新接续，尚非各模型已统一的证明。

**已有部件与仍缺的接口。**

| 层次 | 已有内容 | 尚缺内容 |
|---|---|---|
| 多零线切片 | Paper III 的平行多零线模型和 Hecke 四价零网络 | 选定一个适合原生加乘路径、参数变化和所需零关系的共同模型 |
| 参数求值 | 固定字给出 $p_\gamma(u)$；允许除以 $u$ 时一般为 Laurent 多项式 | 将字实现为实际切片中的路径，并控制定义域、奇点与接缝 |
| Cayley 填充 | 离散轨道赋值、图距离势和面内填充候选 | 证明所选数据来自同一 $(M_u,g_u,a_u)$；图上相容不自动给出二维解 |
| 多项式的几何收益 | Paper III 已有给定 $P(z,t)$ 的 carrier/root-thread 模型 | 固定字的参数多项式与该类额外给定多项式之间的自然联系；以及对指定零关系的有效判别 |

所需的核心相容式可写成
$$
s_\gamma(u)\in M_u,\qquad a_u(s_\gamma(u))=p_\gamma(u),
$$
其中 $s_\gamma(u)$ 必须是声明的几何加乘运动得到的端点。不同历史可以有相同端点多项式；因此必须分别规定“历史相同”“赋值相同”“属于同一零分支”和“零关系商中相同”，并证明拟使用的多项式数据在目标商上是否良定义、能区分什么。

两项边界应保留在重启记录中。第一，在 $\mu\ne0$ 的非退化情形，正则性只禁止局部零线交叉与分支，并不禁止多个连通分量；[Paper III 的平行多零线定理](../../paper-3/sections/03-multi-zero-constructions.tex)已经给出正则例子。第二，本笔记第三节的长度等式要求边是特征线；其失配不能单独证明二维 Eikonal 填充不存在。对正参数 $\mu,\lambda$，二维解沿一般边只推出
$$
\left|\Delta\operatorname{arsinh}(\lambda a/\mu)\right|\leq\lambda\ell_e.
$$
所以该节将特征边检验扩展为二维“不可能”的表述仍需修订，不能用作放弃此路线的数学依据。当前缺的是兼容构造，不是已经证明无解。

**难度判断与暂缓范围。** 初步评估为高难度、工期不可可靠估计的数学构造任务。标量计算和局部核对容易完成，但没有依据承诺在一次短时研究中得到满足上述动机的完整例子。一个精心选择的特例可能绕开一般理论；本判断不要求先解决全部历史自然性或全部 AES 分类，也不声称不存在简单突破。鉴于当前时间预算有限，本轮停在历史与差距记录，不继续扩展填充图或泛化实验。相关未解接口见 [OQ-072–077](../../governance/08-open-questions.md)，尤其是参数族的 properness、历史到除子的映射和切片—tube 自然性；本节不改变这些问题的治理状态。

**重启入口。** 先给出一个明确候选族 $(M_u,g_u,a_u)$ 及其运动规则，在共同定义域上核对 AES 方程和声明的奇集，再选一项零关系问题。可保留银比探针：从零依次执行 $+1,\times u,-1,-1,\times u,-1$，得到
$$
p_\gamma(u)=u^2-2u-1,\qquad p_\gamma(1+\sqrt2)=0.
$$
这个恒等式仅是选定参数的算术见证。未来应进一步确定实际端点所在的零分支或商类，并展示多项式计算提供的几何判别；只出现两个不同的零值点仍不够，因为它们可能在 $E_0$ 的同一条零线上。若使用严格的 proper zero tube 概念，还须另核对正则性、投影及 properness，不能由“有一族切片”自动推出。

## Appendix: script index

`041` add/multiply correction · `042` node values · `043` satisfiability · `044` potential colouring · `045` E₁ square · `046` cusped 4-gon.
