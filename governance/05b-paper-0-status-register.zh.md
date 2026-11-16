# Paper 0 数学状态登记

**状态：** 仅对 Paper 0 权威的登记
**版本：** 1.2
**日期：** 2026-09-22；修正 2026-09-29、2026-11-08
**适用于：** `paper-0/aeg-paper-0.tex` 及其 `sections/` 与 `appendices/`
**同伴：** `05-mathematical-status.md`（适用于 Papers I–IV）

**修正案（2026-11-08）。** 第 2 节获得 §3 的正规形小节（`subsec:p0-normal-form`）：叶曲率
恒等式、正则 AES 正规形、其实现与软性推论，均带论文内证明。第 4 节获得 §9 的加权 charge 注
（`rem:p0-weighted-charges`），记录 `rem:p0-curvature-invariance` 中已存在的不变性讨论与分解
有限缺陷的坐标形式；它不加新不变性断言。正规形在结构假设下陈述，使 Paper I 的
`thm:complete-regular-aes-splitting` 保持乘积分解的规范陈述；不改或重复 Paper I 陈述。叶曲率
恒等式的机器交叉检查（SymPy，基本模型）记录于
`governance/discussions/smooth-and-differential-topology-layer.md`；非独立人工审查。

**修正案（2026-09-29）。** 独立验证的反例显示 `thm:p0-punctures-are-critical` **按打印为假**：
其证明第一步构造满足 eikonal 恒等式的度量并把它当作给定 `g` 的延拓，而 `def:p0-punctured-aes`
的条件 (ii) 要求延拓 `g` 本身。`cor:p0-puncture-count` 继承缺口，`rem:p0-puncture-hypothesis`
第二子句被反驳。第 6 节受影响行在下方修正；第 7 节相应修正。证据：根审查
`AEG-Paper-0-review-2026-09-29-thm-punctures-are-critical-v0.1.md` 与保留记录
`notes/foundations-and-geometry/10`；`governance/notes-reserve-audit.md` 台账条目 C-10。
**本修正案不编辑论文源**；打印定理因此仍带缺陷假设，修正案记录该事实而非修复。可修复形式在
下方注列陈述。`thm:p0-four-circle-model`、`prop:p0-tearing-puncture-independent`、
`prop:p0-surface-does-not-close` 与 `prop:p0-no-puncture-holonomy` 不受影响。

本登记由 `00b-paper-0-geometric-foundation-amendment.md` §1.7 创建。它逐字使用
`00-authoritative-scope.md` §23 的九个状态标签并继承 `05-mathematical-status.md` §4 的解释
规则。被移动结果保留其在 Paper I 中的状态；被移动不提升任何结果。

标签：`PROVED`；`PROVED WITH STATED HYPOTHESES`；`STANDARD CONSEQUENCE REQUIRING AN IN-PAPER
PROOF`；`COMPUTATIONALLY VERIFIED EXAMPLE`；`PARTIALLY PROVED`；`STRUCTURAL PROPOSAL`；
`CONJECTURE`；`OPEN PROBLEM`；`UNSUPPORTED AND EXCLUDED`。

## 1. 展开与语法（Paper 0 §2）

| 节点 | 状态 | 注 |
|---|---|---|
| 纯梳唯一内部序（`prop:p0-combs-unique-order`） | `PROVED` | 当前形式对应用平面树与独立定义的子交错 trace 关系；纯梳 trace 恰是年代输入标签。仍弱于 Paper I 分类。 |
| 梳对偶（`prop:p0-comb-opposition`） | `PROVED` | 语法由镜像/槽交换联系；值与域由对偶部分关系联系。交换律等同解释算子，非平面树。 |
| 仿射/射影断裂（`cor:p0-affine-projective-break`） | `PROVED WITH STATED HYPOTHESES`（2026-10-20 澄清） | 仿射自映射允许零乘子；仿射群成员要求非零乘子。只有非零分子倒数映射有可逆射影延拓。所有普通除法保留其实际分母守卫。 |
| 分配展开恒等式（`prop:p0-distributive-operator-identity`） | `PROVED`（2026-10-20 修正） | 算子恒等式未变。完整运算标签词对所有参数不同；其标量投影恰在 `(0,0)` 或 `(1,1)` 重合。OQ-090 由修正源与单独 Lean 陈述解决。见第 10 节。 |
| 分配 charge 传输（`ex:p0-distributive-charge-transport`） | `PROVED` | 算例；用 `prop:acs-evaluation` |
| 减法与除法的展开边界（`rem:p0-expansion-boundary`） | `PROVED WITH STATED HYPOTHESES`（2026-10-20 澄清） | `kc/z` 即使 `kc=0` 保留原 `z!=0` 域；只有 `kc!=0` 给非仿射可逆射影映射。零乘子/减法情形仍是仿射自映射，群断言限制为非零乘子。 |
| 输入处可求值（`def:p0-evaluable-expression`） | `PROVED` | 定义性：输入属于普通递归域，含每个中间分母守卫。恢复早期可求值表达式术语而不把载体限制为有理数。 |
| 约简倒数与继承域（`ex:p0-cancelled-reciprocal-domain`） | `PROVED WITH STATED HYPOTHESES` | 域上 `1/(1/z)` 有域 `K minus {0}` 并在那里返回 `z`。恒等式有更大域 `K`；两个射影倒数相反在 `P^1(K)` 上复合。普通排除不断言是 AES 奇点。示例含初等计算。 |
| 有效有理求值（`subsec:p0-evaluation-effectivity`） | `PROVED WITH STATED HYPOTHESES` | 有限四运算树、标准整数分数数据与无界精确整数算术；结构递归返回有理值或检测除零。不声称所有量化有理算术或有界实现。 |
| Richardson 限定（`subsec:p0-evaluation-effectivity`） | `PROVED WITH STATED HYPOTHESES` | 引用 Richardson（1968）外部结果，引言与 §2：指定富函数语言、负值存在与允许绝对值的零恒等。不导入任意域或闭常量语言不可判定结论。 |
| 与 Adva 有限构造观点的联系 | `STRUCTURAL PROPOSAL` | 由固定 Adva 报告支持的方法论解释；作者回顾动机与其来源历史单独记录于 `discussions/evaluable-expressions-and-effective-presentations.md`。非新等价定理或完整语义可判定断言。 |

## 2. 算术表达式空间与运动（Paper 0 §3）

| 节点 | 状态 | 注 |
|---|---|---|
| 正则 AES 定义（`def:regular-aes`） | `PROVED` | 定义，从 Paper I §5 移动 |
| 规范算术框架（`prop:canonical-arithmetic-frame`） | `PROVED` | 从 Paper I §5 移动，含证明 |
| 不变仿射度量（`prop:invariant-affine-metric`） | `PROVED` | 从 Paper I §6 移动 |
| 基本双曲 AES（`thm:basic-hyperbolic-aes`）、`K=-\lambda^2` | `PROVED` | 从 Paper I §6 移动 |
| Laplace 特征函数 `\Delta a=2\lambda^2a`（`prop:laplace-eigenfunction`） | `PROVED` | 从 Paper I §6 移动 |
| 赋值相容移动（`prop:p0-grid-assignment-action`） | `PROVED` | 现有 Paper 0 结果 |
| Baumslag–Solitar 型关系（`eq:p0-bs-relation`） | `PROVED` | 初级；现引用 `BaumslagSolitar1962NonHopfian` |
| 连续仿射流（`thm:continuous-affine-flow`） | `PROVED` | 从 Paper I §5 移动 |
| 矫正 `|\nabla r|=|\lambda|`（`eq:rectified-eikonal`） | `PROVED` | 从 Paper I §5 移动 |
| 无穷小序缺陷（`eq:infinitesimal-order-defect`） | `PROVED` | 精确恒等式加渐近形式 |
| 模型标签 `E_0`、`E_1`、`E_k`（`conv:p0-model-labels`） | `STRUCTURAL PROPOSAL` | 仅命名约定；无按 `k` 分类 |
| 单穿孔盘模型（`ex:p0-e1-model`） | `PROVED WITH STATED HYPOTHESES` | 验证是 Paper I §5 `prop:isolated-zero-singular-model`；度量延拓，赋值不 |
| 正扩张平移长度（`prop:p0-dilation-length`） | `STANDARD CONSEQUENCE REQUIRING AN IN-PAPER PROOF` | 2026-10-24 添加；论文内证明提供（沿不变测地线 `iR_{>0}` 积分 `dt/t`）；无需外部引用 |
| 仿射运动长度是其乘法 charge 到符号（`prop:p0-length-multiplicative-charge`） | `PROVED` | 2026-10-24 添加；由平移 `z -> z - z*` 共轭到 `D_Phi` 加 `thm:p0-descent`(3)。对 `Phi = 1` 作为长度 0 抛物情形成立 |
| 长度非同态且对历史非单射（`prop:p0-length-losses`） | `PROVED` | 2026-10-24 添加；(1) 核包含自 `thm:p0-descent`(4)，(2) 重述该条，(3) 显式对 `M_q M_{-q}` 非可加 |
| 尺度相容相对缺陷不改长度（`prop:p0-relative-defect-length-zero`） | `PROVED` | 2026-10-24 添加；乘子 1、迹 2，故长度 0 抛物，自 `prop:relative-affine-defect-coordinates` 加 `prop:p0-length-multiplicative-charge`。记录为 `xi_n` 或 `(xi_gamma-xi_delta)/Phi` 都不能是 Fenchel–Nielsen 扭曲的原因：长度 `ell` holonomy 有迹 `2cosh(ell/2) > 2`，无重标改变共轭型 |
| 射影运动迹分类与长度（`prop:p0-projective-trichotomy`） | `STANDARD CONSEQUENCE REQUIRING AN IN-PAPER PROOF` | 2026-10-24 添加；论文内证明提供（特征值 `lambda, lambda^-1`，故 `tau^2-4` 符号决定双曲/抛物/椭圆；共轭到 `diag(e^{l/2},e^{-l/2})` 给 `ell = 2 arccosh(|tau|/2)`；对照仿射切片 `prop:p0-length-multiplicative-charge` 检查）。收窄 3.6 节边界项 (1) 从「任意射影运动」到「一般域 `K`」 |
| 仿射共轭分类两层（`prop:p0-affine-two-layers`） | `PROVED` | 2026-10-24 添加；`D_Phi T_c D_Phi^{-1} = T_(Phi c)` 直接计算，故平移层类无连续不变量且是扩张下的 torsor，扩张类由其乘子决定。记录为长度零判定是层切换而非缺陷的原因 |
| 一个历史的两坐标（`rem:p0-length-two-coordinates`） | `STRUCTURAL PROPOSAL` | 2026-10-24 添加；读 `prop:affine-cocycle-formulas` 的 `(log Phi_n, xi_n)` 为下降与非下降侧。不加定理；不把任何几何坐标与加法侧等同；不声称 Fenchel–Nielsen |
| 正规形距离坐标 `t(a)` 与 `|\nabla t|=1`（`eq:p0-normal-form-t`、`eq:p0-normal-form-unit-gradient`） | `PROVED` | 2026-11-08 添加；`t` 在 `lambda != 0` 时是 `r/\lambda` 到 `mu` 符号（论文只陈述梯度模一致 `|\nabla r| = |\lambda|`），`lambda = 0` 时 `t = a/\|\mu\|`。标准单位梯度重参数化；与 §12 矫正赋值同一 `t` |
| 算术水平集曲率（`prop:p0-leaf-curvature`） | `PROVED` | 2026-11-08 添加；论文内证明提供（散度规则加 eikonal 恒等式）。符号约定 `k_g := -div(grad t)` 声明于 `eq:p0-normal-form-curvature-definition`；基本模型符号验证（叶曲率 `-lambda^2 a/q`，叶上恒定） |
| 正则 AES 正规形（`prop:p0-normal-form`） | `PROVED WITH STATED HYPOTHESES` | 2026-11-08 添加；假设结构陈述（每点位于 `grad t` 的极大轨道上且恰遇 `Z(a)` 一次），非完备性，使 Paper I 的 `thm:complete-regular-aes-splitting` 保持乘积分解的规范陈述（`rem:p0-normal-form-hypotheses`）。结论：轨道是正规测地线，`|t|` 是到 `Z(a)` 的距离，水平集平行，Fermi 形式 `dt^2 + J^2 ds^2` 带 `J_t = -k_g J`、`J_tt = -K J`，且 `a = (\|\mu\|/\|\lambda\|) sinh(\|\lambda\| t)` |
| 正规形假设何时成立（`rem:p0-normal-form-hypotheses`） | `PROVED WITH STATED HYPOTHESES` | 2026-11-08 添加；完备流足够（单位速，`dt/dsigma = 1`）；由 Hopf–Rinow 在 `E_0` 与完备无边曲面上任何正则 AES 成立。仅 eikonal 充分性的反例：带 `a = mu(r-r_0)`（有界坐标范围）的开 Euclid 环面 |
| 正规形实现（`prop:p0-normal-form-realization`） | `PROVED` | 2026-11-08 添加；每个带 `|\nabla t| = 1` 的正规坐标数据 `(gamma, t, g)` 给 `a = A(t)` 与 `Z(a) = gamma` 的正则 AES。无需完备性 |
| 正则范畴软性（`cor:p0-normal-form-softness`） | `PROVED` | 2026-11-08 添加；`g = dt^2 + J^2 ds^2` 中 `J` 是任意正光滑函数，故正则公理只约束赋值并留横截几何自由。因此无仅按曲面拓扑或光滑结构的正则 AES 分类。否定结果；不分类任何东西 |

## 3. 对偶读法与射影统一（Paper 0 §§4–6）

| 节点 | 状态 | 注 |
|---|---|---|
| ripple 铅笔定义（`def:p0-ripple-pencil`） | `PROVED` | 定义 |
| 线到圆过渡（`thm:p0-ripple-pencil-formula`） | `PROVED` | 现有 Paper 0 结果 |
| 协变–反变对偶（`prop:p0-path-ripple-duality`） | `PROVED` | 定义性 |
| 有限与无限几何展开（`prop:p0-finite-geometric-expansion`） | `PROVED WITH STATED HYPOTHESES` | 无穷值仅在所述收敛假设下 |
| 算术不动点（`prop:p0-reciprocal-fixed-points`） | `PROVED` | 代数不动点不断言吸引 |
| 一矩阵四读法（`thm:p0-four-matrix-readings`） | `PROVED` | |
| 初级射影生成（`thm:p0-pgl2-generation`） | `PROVED` | |
| 名称 `ripple geometry` | `STRUCTURAL PROPOSAL` | 对偶读法的描述名；`subsec:p0-ripple-status` 陈述边界 |

## 4. 交换化、撕裂、接触（Paper 0 §§7–9）

| 节点 | 状态 | 注 |
|---|---|---|
| 仿射余循环公式（`prop:affine-cocycle-formulas`） | `PROVED` | 从 Paper I §4 移动 |
| 相对仿射缺陷（`def:relative-affine-defect`） | `PROVED` | 从 Paper I §4 移动 |
| ACS 定义与 charge 路径（`def:acs`） | `PROVED` | 从 Paper I §8 移动 |
| 历史群（`conv:p0-history-group`） | `STANDARD CONSEQUENCE REQUIRING AN IN-PAPER PROOF` | 固定商的约定：两个加法步群的自由积；2026-09-22 添加 |
| charge 端点与求值是同态（`prop:p0-history-homomorphisms`） | `PROVED` | 2026-09-22 添加 |
| ACS 端点是历史群的交换化（`prop:p0-acs-is-abelianization`） | `PROVED` | 2026-09-22 添加；用标准事实 `(F*H)_ab = F_ab + H_ab` |
| 只有乘法 charge 下降到运动（`thm:p0-descent`） | `PROVED` | 2026-09-22 添加；求值核中的显式传输元 `M_q A_p M_{-q} A_{-e^{-q}p}`，带加法 charge `p(1-e^{-q})`；回答审查 R5 对带验证下降历史幺半群的要求 |
| 直接 ACS 求值（`prop:acs-evaluation`） | `PROVED` | 从 Paper I §8 移动 |
| 相对 torsion（`def:relative-torsion`） | `PROVED` | 从 Paper I §8 移动 |
| 加权 torsion–Stokes 定理（`thm:torsion-stokes`） | `PROVED` | 从 Paper I §8 移动 |
| 撕裂（`def:p0-tearing`） | `STRUCTURAL PROPOSAL` | 双历史缺陷的名称；标量缺陷对尺度相容对定义，仅在 charge 相容下等于加权 ACS 面积（`thm:torsion-stokes`） |
| 接触非退化（`prop:contact-form`） | `PROVED` | 从 Paper I §9 移动 |
| 接触曲率 `[D_u,D_v]=\mu\lambda\partial_a`（`thm:contact-curvature`） | `PROVED` | 从 Paper I §9 移动；重题「指定水平联络的曲率」，带注 `mu*lambda` 非接触同构不变量且非 `K=-lambda^2` |
| 基本模型是接触模型的 Reeb 商（`prop:p0-contact-quotient`） | `PROVED` | 2026-09-22 添加；仅对基本模型五个精确关系带证明；2026-09-22 审查提议并在此独立验证 |
| 有限/无穷小综合（`prop:torsion-curvature-synthesis`） | `PROVED` | 从 Paper I §9 移动 |
| 水平分布曲率形式（`prop:p0-curvature-form`） | `PROVED` | 2026-09-22（晚）添加：括号缺陷在分布上定义规范 2-形式，由 `(D, pi)` 决定且独立于 `alpha` 归一化；其在 `h`-正交框架上值是 `mu*lambda`，`h -> rho^2 h` 下重标律 `rho^{-2}` |
| 曲率标量不变群（`rem:p0-curvature-invariance`） | `PROVED`（解释性注） | 解决 OI-6：`mu*lambda` 非接触不变量，但它是声明框架与水平度量的不变量，且在数据 AES 侧是无图表达式 `da([X_u,X_v])` |
| 加权 charge 与缺陷泛函（`rem:p0-weighted-charges`） | `PROVED`（解释性注） | 2026-11-08 添加；单位选择 `U = mu u`、`V = lambda v` 给 `alpha = da - dU - a dV` 与 `D_u = mu D_U`、`D_v = lambda D_V`，故 `mu*lambda` 是两个归一化之积且 `d(alpha) = -da ^ dV` 是不变形式；有限缺陷变为 `T_open = Delta U (exp(Delta V) - 1)` 与 `T_closed = exp(-Delta V) T_open`；ACS 坐标 `(A,M)` 是同一加权 charge 平面。`rem:p0-curvature-invariance` 的坐标形式；无新不变性断言 |

## 5. 超越线性语言（Paper 0 §10）

| 节点 | 状态 | 注 |
|---|---|---|
| 算术生成元不闭（`prop:p0-arithmetic-generators`） | `PROVED` | 初等计算；由 `ad_A^n(P)` 证明，2026-09-22 修订；行文结论收窄为有限维 Lie 群闭包 |
| charge 端点可观测量看不到撕裂（`prop:p0-characters-cannot-see-tearing`） | `PROVED` | 对 charge 端点任意函数重述；明确不是关于非 Abel 线性表示 |
| 过程几何词汇与下降纪律 | `STRUCTURAL PROPOSAL` | 作为语言导入；不声称 AES 定理 |
| 满足 `eq:p0-bs-relation` 与括号律的精确校准 | `COMPUTATIONALLY VERIFIED EXAMPLE` | `Yuan2026ProcessGeometry` 的研究本地校准，带该仓库自身成熟度标签 |

## 6. 有孔空间（Paper 0 §11）

| 节点 | 状态 | 注 |
|---|---|---|
| 正则 AES 梯度不消失（`lem:p0-gradient-nonvanishing`） | `PROVED` | `|\nabla a|^2 = \mu^2+\lambda^2a^2 \ge \mu^2 > 0`；蕴含每个水平集是光滑曲线；Paper I 正则零定理是零水平情形 |
| 穿孔恰是赋值临界点（`thm:p0-punctures-are-critical`） | **按打印 `UNSUPPORTED AND EXCLUDED`**（2026-09-29 修正）；修复形式 `PROVED WITH STATED HYPOTHESES` | 2026-09-22（晚）作为 `PROVED` 添加，假设：赋值光滑延拓到环境曲面。**按打印被反驳**：验证反例有光滑延拓赋值、`S = {0}` 与 `Crit(atilde) = emptyset`。缺口在证明第一步——模板度量 `g~ = |d atilde|^2_{g_0} g_0 / (mu^2 + lambda^2 atilde^2)` 满足 eikonal 恒等式但不是给定 `g` 的延拓。反向包含 `Crit(atilde) subseteq S` 仍证明。**修复形式：** 若额外 `g` 在每个穿孔附近共形于光滑非退化延拓的度量，则结论成立；那时 eikonal 恒等式强制 `g` 是模板度量。待论文修正；见 C-10 |
| 假设是活跃的（`rem:p0-puncture-hypothesis`） | `PARTIALLY PROVED`（2026-09-29 修正） | Paper I 盘模型不满足假设（其赋值在穿孔非 `C^1`），故那里规范开放——那半成立。闭子句「第二类穿孔集规范」被**反驳**：反例是那类（赋值光滑、度量不可延拓）带 `S = {0}` 非被迫，且同模型平移到任何内部点。注所画两物种区分仍正确且是修复定理所需 |
| 穿孔数等于临界点数（`cor:p0-puncture-count`） | **`UNSUPPORTED AND EXCLUDED`**（2026-09-29 修正） | 继承上述缺口；它由定理「立即」导出。计数相等与「当且仅当」子句在反例（一穿孔、零临界点，在带无临界点光滑函数的盘上）都失败 |
| 撕裂看不到穿孔（`prop:p0-tearing-puncture-independent`） | `PROVED` | 2026-09-22（第四修订）添加：`tau` 是两词函数，故穿孔、改变模型或改变实现都不变；解决 OI-2 前半 |
| 曲面从不闭合比较（`prop:p0-surface-does-not-close`） | `PROVED` | 矩形两排序终止于赋值相差 `mu*h*(e^{lambda k}-1) != 0` 的点，故两流路径不围出 `M` 区域；ACS 比较因此在每个 AES 规范，非避孔权宜 |
| 穿孔周围无规范 holonomy（`prop:p0-no-puncture-holonomy`） | `PROVED` | 水平集叶层可积故平坦；弯曲联络需附加数据（接触模型，其中 `omega` 相对 charge 投影规范）；规范穿孔模型赋值单值，故无单值 |
| 穿孔处零集芽与度量（`prop:p0-puncture-local-picture`） | `PROVED` | 半径低于 `rho` 的圆与零轨迹恰交八点带变号；八扇区、四正四负（沿轴尖点）；`g` 共形于 Euclid 度量带消失因子，故共形类延拓而度量不 |
| 穿孔 AES 定义（`def:p0-punctured-aes`） | `PROVED` | 定义；2026-09-22 修订为先给环境曲面与有限集，使非空穿孔集存在；Paper I 奇异 AES 的有限点特化 |
| 四极限圆切锥（`prop:p0-puncture-tangent-cone`） | `PROVED` | 精确代数恒等式，论文内验证 |
| 带四圆零轨迹的显式穿孔 AES（`thm:p0-four-circle-model`） | `PROVED` | 2026-09-22 添加：eikonal 恒等式强制的模板度量、精确临界集（故半径 `< \rho` 穿孔盘上 `\nabla P \neq 0`）、零轨迹、原点不可延拓与有限距离穿孔不完备；回答审查 R7 构造要求。**不受 2026-09-29 修正影响**，但注意原因：这里 `d atilde(0) = 0`，故定理证明缺陷支不被进入且此模型未测试它 |
| 六个计算见证 | `COMPUTATIONALLY VERIFIED EXAMPLE` | 每个带论文内陈述模型处计数依赖它；登记非权威 |
| 观察者见证 | `PROVED`（界），登记数字**未复现** | 残差函数、其精确零与停止界 `|theta-pi/2| < 5eps/8 + O(eps^2)` 被证明；登记轮计数依赖未固定更新步且不引用 |
| 见证作为 AES 阻碍的读法 | `UNSUPPORTED AND EXCLUDED` | 在 `subsec:p0-holed-nonclaims` 列为非断言 |
| 把 $\mathbb Z_3$ 单值与任何 $\mathbb Z_4$ 扭曲等同 | `UNSUPPORTED AND EXCLUDED` | 在登记记录为未证明；此处不复现 |
| 把四圆模型推广到 `k` 穿孔或运动生成赋值 | `OPEN PROBLEM` | `op:p0-four-circle`；`k` 穿孔半被 `cor:p0-puncture-count` 重塑为带 `k` 临界点的函数问题，但该推论现在被排除（见上），故重塑撤回且问题回到更早形式 |
| 在赋值不延拓模型中跨穿孔撕裂比较 | `OPEN PROBLEM` | 对光滑延拓赋值由 `prop:p0-tearing-puncture-independent`、`prop:p0-surface-does-not-close`、`prop:p0-no-puncture-holonomy` 解决；非延拓情形是 OQ-088 |
| 赋值**不**光滑延拓时规范穿孔 | `OPEN PROBLEM` | Paper I 盘模型是开放情形（OQ-088）。**2026-09-29 修正：** 光滑延拓情形也*未*解决——见本表定理行，按打印被反驳。存活的分界线非「赋值延拓」而是「度量在每个穿孔附近共形于延拓者」；OQ-088 框架相应修正 |
| 返回约化为周期轨道（`prop:p0-reduction-descent`） | `PROVED WITH STATED HYPOTHESES` | 2026-11-11 添加；来源 `notes/analysis-and-calculus/53-punctured-aes-flows-and-reduction.md` §5.2。光滑流陈述：下降恒等式 $D\pi\,\widetilde X=\nu\,Y\circ\pi$、正速率 $\nu>0$、全轨道合法性、$Y(p)\neq0$ 与 $\pi(\Phi_S z)=\pi(z)$（严格或相对返回）蕴含经 $p=\pi z$ 的 $\dot b=Y(b)$ 的非平凡周期解，周期 $T=\tau(S,z)>0$。不断言穿孔 AES 满足这些假设 |
| 逆提升与漂移（`prop:p0-reduction-reverse`） | `PROVED WITH STATED HYPOTHESES` | 2026-11-11 添加；来源笔记 53 §5.3。主 $G$-丛加全轨道假设给唯一相对返回漂移 $g$；等变给 $\Phi_{kS}(z_0)=z_0\cdot g^k$，严格恰在 $g^k=e$ |
| 截面根是周期轨道（`cor:p0-reduction-section`） | `PROVED WITH STATED HYPOTHESES` | 2026-11-11 添加；来源笔记 53 §5.4。`prop:p0-reduction-descent` 假设下横截截面商不动点 $F_{\mathrm{quot}}=0$ 是周期轨道 |
| 传输到基本模型（`prop:p0-reduction-transport`） | `PROVED WITH STATED HYPOTHESES` | 2026-11-11 添加；来源笔记 53 §5.8（R-D）。$\Psi(x,y)=(-ye^{-x},e^{-x})$ 是到上半平面的全局微分同胚，按原时间传输任何 $C^1$ 平面向量场；有限周期轨道像远离 $\eta=0$ |
| 在穿孔 AES 上实现载体、端数据与区间接收器（`subsec:p0-punctured-flow-proposal`） | `STRUCTURAL PROPOSAL` | 2026-11-11 添加，2026-11-11 对齐笔记 53 v0.2。流声明在与二维 AES 分开的动力学载体 $N_{\mathrm{reg}}$ 上；接触形式活在奇维载体上；三个完备化保持区分；两个 Legendre 用法不混淆。非断言（无规范穿孔单值、2D AES 非 3D 接触载体、van der Pol 非 Hamilton、含零区间非根存在、底空间周期不必严格提升）是小节一部分 |
| 端数据/端管；极小端数据；载体假设；Hamilton–Lagrange 退化；约化假设锐化；覆盖/联络语义；AES 原生实现 | `OPEN PROBLEM` | `subsec:p0-punctured-flow-proposal` 的七个流/约化问题（`op:p0-punctured-flow-end-data` 与六个无标签项），登记为 OQ-101；Q5 与 Q7 由 `prop:p0-reduction-descent`/`prop:p0-reduction-transport` 部分解决 |

## 7. 开放计划

`OPEN PROBLEM`：
ripple 几何的内在射影 AES；商稳定 path/ripple 不变量；非延拓赋值穿孔规范；穿孔处 ripple
结构；多线语义；无穷算术表达式一般理论；取代 §10 两阻碍的正非线性描述。

**2026-09-29 修正。** 穿孔规范现在在**两**物种都开放，非仅非延拓赋值。原始双包含证明通过的
充分假设记录于上 `thm:p0-punctures-are-critical` 行；是否也必要、赋值不延拓时什么扮演临界集
角色，两者都开放（OQ-082 修正；OQ-088）。

## 8. 有限型紧化修正案（2026-10-09）

本当前修正案取代第 6 节受影响*活跃手稿*状态而不重写带日期 9 月 29 日证据或审查。原始无限制
临界集陈述仍被反驳；规范源现在打印下方显式受限版本。

| 节点 | 当前状态 | 活跃假设与边界 |
|---|---|---|
| `thm:p0-punctures-are-critical` | `PROVED WITH STATED HYPOTHESES` | 赋值光滑延拓，且每个穿孔附近**给定**度量共形于光滑正延拓的背景度量。Eikonal 然后强制模板因子，故构造延拓真与给定度量一致。 |
| `cor:p0-puncture-count` | `PROVED WITH STATED HYPOTHESES` | 穿孔/临界计数相等仅在前类；逆由带有限临界集赋值构造度量。不声称无限制存在分类。 |
| `rem:p0-puncture-hypothesis`、`rem:p0-multi-puncture` | `PROVED WITH STATED HYPOTHESES` | 各向异性反例包含；无共形背景只有 Crit(a) ⊆ S 成立。 |
| `def:p0-finite-type-carrier`、`def:p0-collar-contract` | `STRUCTURAL PROPOSAL` | 声明载体/端与完整光滑 collar 数据定义；无规范接缝选择。 |
| `prop:p0-conformal-end-filling` | `PROVED WITH STATED HYPOTHESES` | 有限拓扑型加穿孔盘共形端，仅共形点填充。 |
| `thm:p0-arbitrary-k-punctures` | `PROVED WITH STATED HYPOTHESES` | 每个 k≥1；k−1 个不同实临界点加本质无穷，μ≠0，实 λ；存在，非任意模分类。 |
| `eq:p0-pants-counts` | `PROVED WITH STATED HYPOTHESES` | 带 2γ−2+k>0 的连通定向有限型；引用标准分解存在；计数由 Euler 特征与端关联证明。 |
| `prop:p0-aes-collar-descent` | `PROVED WITH STATED HYPOTHESES` | 完整 collar 芽、逆/余循环律、Hausdorff 光滑商、一致定向与相等符号 μ,λ。框架与有限横流相容；穿孔处无解析延拓。 |
| `warn:p0-hyperbolic-auxiliary` | `PROVED WITH STATED HYPOTHESES` | 从 Paper I 导入完备分裂阻碍，带连通性、完备性、无边与单值赋值。 |
| 三尖点覆盖与退化段落 | `PROVED WITH STATED HYPOTHESES` | 幂映射覆盖是特殊共形族；FN/管道描述带标记与局部坐标选择的辅助双曲/共形几何。不断言 AES 相容退化。 |
| `prop:p0-k4-motion-residue` | `PROVED WITH STATED HYPOTHESES` | 显式 k4 模型中 (0,1) 附近局部流；精确标量恒等式与非零混合态位移 (−3/4,0)。新解析证书，非不可用原始数值套件的重跑。 |
| `prop:p0-apollonian-gap-equivalence` | `PROVED WITH STATED HYPOTHESES` | 非退化选定三角间隙、三个不同切、匹配循环标记；递归圆由唯一性。四个初始间隙仍三元递归。 |
| `prop:p0-four-circle-deformation` | `PROVED` | 仅关联阻碍与显式圆族；非 AES 形变。 |
| `prop:p0-three-sheet-cover` | `PROVED WITH STATED HYPOTHESES` | 独立基叶、显式切割置换、拉回复结构；锥角 6π 属 Euclid 拉回长度度量。 |
| Bolza 与双裤比较 | `PROVED WITH STATED HYPOTHESES` | 精确指定代数特化与亏格计数；仅亏格无共形或过程等价。 |
| `paper-0/scripts/verify-compactification.py` 中新精确有限检查 | `COMPUTATIONALLY VERIFIED EXAMPLE` | 显式公式回归证据，非一般定理证明或原始 39 检查归档。 |
| 任意共形模、AES 相容管道、忠实算术圆手术 | `OPEN PROBLEM` | 每计数一模型存在与辅助双曲相容不解决这些。 |

「产生*某个*可紧化多穿孔示例是开放」的旧陈述被 `thm:p0-arbitrary-k-punctures` 取代。规定穿孔
位置、规定零构型、运动生成赋值与分类仍开放。原始无限制「当且仅当」推论失去其证明；反例直接
反驳给定 AES 的相等，而非该环境曲面上每个可能存在性重构。

## 9. 形式化推导检查点（2026-10-20）

`paper-0/formal/` 中原始 CC0 实现开始当前手稿的单独逐章形式化。其清单是定理类环境的导航，
非本状态登记的替代。五个符号代数**分量**有 Adva 编写交换半环相等 checker 的显式证明证书与
单独 Lean 陈述。梳文法有两个额外 Lean 陈述；其与手稿的对应仍是显式审查工作。几何、分析、
射影域、归一化逆坐标与全章覆盖不被此检查点提升。

`prop:p0-distributive-operator-identity` 的算子部分对所有域参数有效。打印的「年代常量对
`(p,k)` 与 `(k,k*p)` 恰在 `p=k=1` 重合」断言在 `p=k=0` 失败，命题无限制参数声明允许之。若
相反意指完整标记词，运算标签也存活：两运算序列即使 `p=k=1` 也不同。手稿与证明保留待 OQ-090
的精确修正。其全命题状态因此是 `PARTIALLY PROVED`；认证算子方程不被此发现削弱。

由 Codex（OpenAI）编写。形式检查与源映射单独记录；不断言独立人工审查或全论文正确性。

## 10. 第 2 章定义/域延续（2026-10-20）

此后继取代第 9 节待定标记数据修正，同时保留该检查点与其归档验证字节。OQ-090 解决：源现在
区分完整标记历史与其年代标量投影并含零与单位情形。零情形作为算术语法接纳，不把其乘子当
可逆。群/延续断言显式保留其非零假设，含退化 `c=0` 倒数情形。

`paper-0/formal/definition-map.json` 把修正源绑定到新 `Chapter02Domains.lean` 模块。语法、先子
后父调度、普通部分求值、八个单孔截面域、非零仿射映射可逆性与标记/标量相等是单独定义与结论。
齐次倒数坐标与无穷行为覆盖；不声称 `PGL_2` 的完整形式商构造。charge 示例中实指数/ACS 事实保留
手稿/第 8 章证明依赖。

单独 `domain-checker.adva` 执行有界有理梳及其实际除法守卫。其有限回归是该程序声明执行的证据，
非关于所有域的普遍定理，也非未变多项式相等核的扩展。后继契约、映射、定理审计与证据索引陈述
精确覆盖。

## 11. 可求值与有效呈现（2026-10-20）

§2 新最后小节恢复 2022 年 12 月可求值表达式概念与 2023 年 1 月基础问题，带固定历史引用与从
判定困难到无法在实数上定义表达式推断的显式修正。语法、部分语义、有效求值与语义判定问题保持
分开。有理起点是有效呈现，非声称有理载体上通常拓扑离散。

定义与倒数示例登记于上。无现有定理被加强或移动，无额外几何奇异断言引入。历史来源未变。较长
讨论与作者回顾 Adva 联系保留于 `discussions/evaluable-expressions-and-effective-presentations.md`。

原始形式源 `02-expansion.tex`、证明程序与 Lean 模块未变。活跃覆盖清单含添加源并标记其新定义/
示例 `not-yet-formalized`。归档执行记录继续绑定自身手稿与清单快照；此行文添加不扩展其五个 Adva
证书或 71 个 Lean 陈述范围。当前清单是导航，非新执行证明记录。

此编辑延续验证：全部 14 个现有形式回归测试通过；`./build.sh 0` 产出 95 页 PDF、`./build.sh 1`
产出 32 页。两个最终日志无未定义引用、缺失引用、重复标签或缺失资产。PDF 页 13–14 的添加小节
视觉检查且不引入 overfull box。现有警告保留：Paper 0 §10 有一个 11.13 pt overfull 段落、Paper I
两个 overfull box、Paper 0 hyperref 数学书签警告。Paper I 重建 PDF 保留于外部工程记录；其跟踪
PDF 未变。无材料移到另一论文或归档。下一步形式化可把新可求值定义与倒数示例显式连接到现有守卫
求值定理；此添加不声称一般实语言判定过程。

## 12. 交替表达式与算术扰动（2026-10-20）

附录 C 在其一般仿射计算前恢复早期交替表达式呈现。完整算术推导存在于 2023 年 2 月草稿；2025
年 5 月 scale/RG 笔记显式指其扰动公式。来源时间线与作者回顾 ACS/RG 联系记录于
`discussions/alternating-expressions-perturbation-acs-rg.md`。

| 节点 | 状态 | 假设与边界 |
|---|---|---|
| `def:appendix-alternating-expression` | `PROVED` | 域上有限年代槽 (1) 先乘后加词定义；每乘子非零以保留周围仿射群约定。对仍是不同运算事件。 |
| `prop:appendix-alternating-arithmetic-perturbation` | `PROVED WITH STATED HYPOTHESES` | 域上有限分配展开与精确差传播，两输入同一历史。比额外要求不同初值。含显式算术归纳，无极限或小性假设。 |
| 恒等填充到交替形式 | `PROVED WITH STATED HYPOTHESES` | 只加法与非零缩放的词；填充保留诱导算子，非字面树或完整标记历史。不声称任意分支/倒数表达式的唯一正规形或转换。 |
| `eq:appendix-alternating-acs-bridge` | `PROVED WITH STATED HYPOTHESES` | 正实乘子、年代先乘后加对与现有 ACS 定义。直接边积分给源归一化平移；末端尺度恢复值。初值增益与加法事件后缀增益不同。 |
| 尺度归一化与历史 RG 读法 | `STRUCTURAL PROPOSAL` | 归档 2025 年 5 月笔记与作者回忆确立研究动机。初等恒等式不证明特定阻塞/重标 RG 变换、极限理论、物理等同或复杂度定理。 |

此添加使初始累加器与非零差商条件显式，同时留下原始归档不变。旧一般前缀扰动公式保留其标签
现指初级推导而非重复其证明。一般仿射余循环与 ACS 陈述不被加强或移动。此编辑检查点清单标记
添加定义/命题 `not-yet-formalized`；第 13 节记录其后续形式延续。先前 Adva 与 Lean 执行归档保留
其原范围。

验证：清单更新后全部 14 个现有形式回归测试通过。两个所需构建通过：Paper 0 97 页、Paper I 32
页。最终日志无未定义引用、缺失引用、重复标签或缺失资产。恢复附录页 85、87 视觉检查；无新
overfull box。第 11 节记录的现有布局/书签警告保留。Paper I 跟踪 PDF 在其单独构建后保留。

算例精确有理检查给初值增益 6、加法事件后缀增益 3 与 1、源归一化平移 7/6；直接递推与归一化
ACS 读数一致。这些检查支持示例，非普遍形式证明。无研究材料被移动或删除。下一步形式化可把
有限递推归纳连接到现有仿射代数基础设施；一般 RG 构造仍在此附录之外。

## 13. 附录 C 有限归纳延续（2026-10-20）

`paper-0/formal/AppendixC.lean` 提供 24 个显式审计陈述，手稿对应声明于 `appendix-map.json`。
当前清单标记恢复的交替表达式定义与算术扰动命题 `component-map-supplied`。此导航标签非声称整个
附录被形式证明。

完整有限标量展开与扰动命题由 `expanded_evaluation`、`contribution_at`、`exact_difference`、
`prefix_difference`、`perturbation_ratio` 与 `guarded_ratio` 表示。贡献按严格后缀积独立索引。
`evaluate_snoc` 识别年代递推；`events_correspondence` 与 `tree_correspondence` 把每个双事件对连接
到现有普通词/树求值。非零乘子与其非零累积尺度单独记录。多项式归纳只需显式交换半环律；差与商
用现有域律参数。商额外要求不同初值；`diagonal_ratio_undefined` 证明相等输入不容许此普通除法，
尽管域结构有全逆运算。

新陈述中十九个，含主要展开、扰动与比定理，不用全局公理。两个积助手与事件计数用 `propext`；两个
列表/树对应用 `propext` 与 `Quot.sound`。精确名称与公理清单被检查而非从成功编译推断。一个新 Adva
半环证书检查符号扰动步，带改目标拒绝与独立重放。它不引入原生普遍归纳。

首次组合调用在 `formal/evidence/appendix-c-attempt-1.json` 及其完整归档保留为 `Failed`。精确公理
映射曾为 `scale_append` 与 `scale_snoc` 漏 `propext`；接收在 63 个原生运行与正 Lean 模块后停在该
不匹配，在缺失守卫控制之前。`contract-appendix-c-v1.1.json` 声明只修正那两个预期条目后的后继，
带未变证明/程序/目标/情形字节与资源界。首次尝试的 184.11 秒是额外成本且不重新标记为成功。

当前执行回执单独记录为 `formal/evidence/appendix-c-execution.json`。恒等填充、实指数、ACS 积分与
RG 解释不被此延续提升。无现有数学陈述被加强或移动。下一步可在导入解析积分前形式化源归一化及其
与离散 ACS 权重相容。

记录的后继是 `Passed`：63 个原生运行、131 个子命令、49,581 个独立接收指令过渡与全部 24 个新
Lean 审计，连同未变 71 个先前陈述。省略比假设以预期类型不匹配拒绝。成功运行花 182.03 秒；全部
63 个原生报告/回执与正附录 C 审计与失败调用字节相同，其额外成本单独记录。十八个回归测试通过，
含源、trace 与失败保留检查。所需 Paper 0/Paper I 构建在 97/32 页通过，无未定义引用、缺失引用、
重复标签或缺失资产。先前记录布局/书签警告保留，无新溢出；跟踪 Paper I PDF 在其构建后保留。此
形式延续无材料被移动或删除。

## 14. 切割与表达式基础（2026-10-21）

附录 F（`app:p0-cuts-foundations`）是为下一算术表达式形式理论请求的背景与研究方向附录。它不把
Paper 0 扩展为一般收敛或复杂度理论。

| 节点 | 状态 | 注 |
|---|---|---|
| Bauer–Taylor 切割与可观测谓词（`subsec:p0-taylor-cuts`） | `PROVED WITH STATED HYPOTHESES` | 外部背景，引用 Bauer–Taylor（2009）第 2、6 节与 Taylor（2006）第 2、5–6 节。有居、圆、不相交、定位有理谓词描述实数；广义切割带区间信息。不推断布尔比较过程。 |
| Conway 选项、简单性与有限树边界（`subsec:p0-conway-cuts`、`subsec:p0-cut-representation-boundaries`） | `PROVED WITH STATED HYPOTHESES` | Conway（1976）第 0–2 章外部背景，Ehrlich（2011）更大域与层级。有限原始选项树给二进有理；扩签名中有限名称不必有有限切割展开。 |
| 不同载体中的有理观测（`subsec:p0-cut-representation-boundaries`） | `PROVED WITH STATED HYPOTHESES` | 行文初级比较：嵌入无理实数与该实数加正无穷小有相同严格有理比较。无理假设本质；在有理目标，与该有理比较区分它们。 |
| Adva through 先例（`subsec:p0-cut-formal-programme`） | `COMPUTATIONALLY VERIFIED EXAMPLE` | 报告固定研究笔记 0075 与其声明有限范围。关系可部分或多值；完整程序切片仍在。不导入 ASD、Conway 值选择或稳定原生 through 运算。 |
| 逐选项缩放对值选择（`subsec:p0-cut-formal-programme`） | `PROVED WITH STATED HYPOTHESES` | 显示有限反例在附录计算并追溯到固定 Adva 笔记 0021。不挑战 Conway 乘法：缩放选项是不同运算。 |
| 提议形式表达式计划（`subsec:p0-cut-formal-programme`） | `STRUCTURAL PROPOSAL` | 单独语法与守卫、精确指称构造器、带依赖与保留余数的观测、不同相等/精细化/相容判定。其一般规则、可靠性、有效性与资源保证仍开放。 |

无现有结果被加强、移除或迁移。附录背景不被现有 Adva/Lean 证书覆盖。只有当前导航清单与其活跃
源锁摘要刷新；冻结陈述、源映射、归档锁与执行回执保留。附录 C 回归现在区分其归档清单与活跃
导航，同时保留所有归档摘要与证明源检查。此添加的阐述与组织由 Codex（OpenAI）应作者请求。

验证：`./build.sh 0` 与 `./build.sh 1` 产出 100 与 32 页 PDF。两个最终日志无未定义引用、缺失
引用、重复标签或缺失资产。现有布局警告保留于 Paper 0 第 10 节与 Paper I 更旧材料，现有 Paper 0
hyperref 数学书签警告；附录 F 不引入溢出。十八个形式回归测试用现有验证环境通过。初始系统
Python 调用缺 `blake3`；配置环境提供固定依赖。其另一发现是历史/活跃清单比较，按上述修正而不改
归档字节。仅验证 Paper I PDF 保留于仓库外；其先前跟踪产物保留。下一步是尝试一般演算前指定小的
守卫表达式签名并分开指称、观测与 through 相容判定。

## 15. 平坦极限与复二次秩（2026-11-07）

此修复解决第 3 节 horocyclic 坐标与旧第 12.6 节「无重标能产 Euclid 平面」断言的冲突。它还撤回
「复化后全部三个绝对型坍缩」的断言。无材料迁移。

| 节点 | 状态 | 注 |
|---|---|---|
| 光滑尖平坦极限（`prop:p0-flat-limit`） | `PROVED WITH STATED HYPOTHESES` | 固定 `mu>0`、`lambda` 经正值降为零、由 `(u,v) -> (u,exp(lambda v))` 拉回。度量、赋值与规范框架在紧集上 `C^infinity` 收敛。极限是完备 Euclid 正则 AES。不声称正 lambda 全局均匀收敛或平坦。 |
| 复二次秩（`prop:p0-complex-conic-rank`） | `PROVED` | 秩在 R 到 C 标量扩张、可逆合同与非零缩放下不变。复对称形式按秩分类；只有非奇异实/虚区分消失。 |
