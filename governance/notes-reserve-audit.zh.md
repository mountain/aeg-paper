# 笔记储备审计

**文件：** `governance/notes-reserve-audit.md`
**状态：** 审计记录（`notes/` 的清单与状态登记；非权威，不修订范围）
**版本：** 1.1
**日期：** 2026-08-10；修正 2026-09-29、2026-10-31
**拟定：** DeepSeekHarness（AI 编码代理），在仓库作者指导下工作；所有数学等级遵循
`governance/05-mathematical-status.md` 的官方状态词汇，本审计不改变任何论断状态。
**依赖：**

* `AGENTS.md`
* `governance/00-authoritative-scope.md`
* `governance/05-mathematical-status.md`
* `governance/08-open-questions.md`

**适用于：** `notes/` 下每条笔记，连同冲突或修正陈述起源处的 `archive/` 归档材料交叉引用。

**修正案（2026-09-29）。** 版本 1.0 后向 `notes/foundations-and-geometry/` 添加了四条笔记，
故第 2 节不再覆盖 `notes/` 下每条笔记。`07`、`08`、`09`、`10` 行加入第 2.1 节，对应条目加入
第 4 节，一个新冲突 C-10 加入第 3 节。同进行的逐文件比较显示缺口更宽：本修正案前九条既有
笔记也从未被覆盖，`foundations-and-geometry/06` 是其一。`06` 现在第 2.1 节定级，其余九个在
新第 2.7 节记录为未定级且显式如此。修正案扩展覆盖；不修订版本 1.0 所赋任何等级、不提升任何
笔记、不改变任何论文断言。添加笔记本身是探索性记录，唯一实质后果——一条登记 Paper 0 断言按
打印被反驳——记录于 C-10 并带入其命名登记，非此处决定。

**修正案（2026-10-31）。** 2026-09-29 修正案后向 `notes/analysis-and-calculus/` 添加了一条
笔记：`09-order-topology-scott-lawson`。它先在第 2.7 节覆盖缺口清单记录为未定级（计数九→十），
同日读取并定级：第 2.2 节加一行、第 4 节 Tier C 加一点、第 2.7 节回到九。等级是
`STRUCTURAL PROPOSAL` + `REFORMULATION`——经典域论内容在笔记标 `CLASSICAL`，AEG 实例化（前缀序
信息序、加法 = way-below、乘法 = Scott 自同构、后向伴随 = 倒数、单独 Scott 连续）是正确重构，
整合的「缺失对合 = 后向伴随 = 序拓扑分析基础」读法是结构提案，非定理。三个同伴开放问题
（OQ-091–OQ-093）加入 `governance/08-open-questions.md`；OQ-092 与 OQ-093 解决，OQ-091 部分
解决（分支历史情形仍开放）。

**修正案（2026-10-31，第二次）。** 同日向 `notes/analysis-and-calculus/` 又添加十一条笔记，
延续 `09` 开启的主线并应用到 Paper I 主体与 Paper 0 接触结构：`10`–`20`。第 2.2 节为该主线加
一个合并行（十一条笔记一起定级，因它们形成一条连续论证），第 4 节 Tier C 加一个主线点，残差
登记为 OQ-094（094a–094d，在 `11`–`16` 解决）与 OQ-095（宏观 Stokes 与完整 DAG Lie 实现，开放）。
主线等级是 `STRUCTURAL PROPOSAL` + `REFORMULATION`（+ `CLASSICAL`），两个可证明子结果显式注明：
`14` 定理 1 的单调性阻碍（`WORKING-NOTE PROVED`）与计算验证（`D_{-1}=T_1¬T_{-1}¬T_1¬`、BCH
密度、端枚举）。本修正案不编辑论文源、不提升任何断言；合并处置记录于
`governance/scott-lawson-paper-1-integration-2026-10-31.md`。

**修正案（2026-11-11）。** 2026-11-10 向 `notes/analysis-and-calculus/` 又添加两条笔记：`52`
（Scott/Lawson 对 Adva 区间词汇）与 `53`（穿孔 AES 上的流与约化为 ODE），并在此对齐其 v0.2
修订（2026-11-11 合并到 `main`）。第 2.2 节各加一行。`52` 定级 `STRUCTURAL PROPOSAL` +
`REFORMULATION`（+ `CLASSICAL`）且仅登记（OQ-102）；其 `ZeroStatus`/`RootStatus`/`InvalidWitness`
词汇是候选 Paper I 零理论纪律笔记，非正文。`53` 定级 `PROVED WITH STATED HYPOTHESES` +
`STRUCTURAL PROPOSAL` + `OPEN PROBLEM`；其光滑流约化定理（R-A/R-B/R-C/R-D）以 `PROVED WITH
STATED HYPOTHESES` 提升进 Paper 0 §11（`prop:p0-reduction-descent`、`prop:p0-reduction-reverse`、
`cor:p0-reduction-section`、`prop:p0-reduction-transport`），其穿孔 AES 应用仍 `STRUCTURAL
PROPOSAL`（`subsec:p0-punctured-flow-proposal`），其七个问题登记为 OQ-101。根存在路由（管重放 +
Newton + 约化）仍是值层验证关注且不被提升。

**修正案（2026-11-14）。** 添加新主题目录 `notes/general/`（笔记 `001`–`005`），携带 HTWR
（双曲热带波前残差）核心。第 2 节得小节 2.9、第 4 节 Tier C 得一点。五条笔记定级 `STRUCTURAL
PROPOSAL`（其中各笔记陈述处有 `STANDARD CONSEQUENCE REQUIRING AN IN-PAPER PROOF` 与
`COMPUTATIONALLY VERIFIED EXAMPLE`）；无笔记被提升、无笔记被分配给论文。开放残差登记为 OQ-103
于 `governance/08-open-questions.md`。目录也加入 `notes/README.md`。

---

## 1. 目的与方法

五份规范手稿（Papers 0–IV）已纳入 `notes/` 材料的一个子集。本审计清点什么被纳入与什么未纳入，
用 `governance/05-mathematical-status.md` 官方状态词汇按证明完备性给未纳入储备定级，记录冲突
与过时而不静默调和，并推荐处置。它刻意**不**修改任何论文源、不提升任何断言、不修订权威范围。
下方任何项的提升需单独任务并按 `governance/05-mathematical-status.md` 第 4 节规定的集成审计。

下方使用的等级标签：

* `WORKING-NOTE PROVED` — 笔记本身内有完整证明；结果在论文标 `PROVED` 前需
  **INTEGRATION AUDIT**（陈述/证明匹配、约定、域与正则假设）。
* `COMPUTATIONALLY VERIFIED EXAMPLE` — 由可复现脚本对有限数据集检查；无一般定理。
* `STRUCTURAL PROPOSAL` — 连贯框架，无完备/唯一性定理。
* `OPEN PROGRAM` — 带声明通过/失败判据的研究计划。
* `EXPLORATORY` — 想法级材料，尚未是精确数学断言。
* `CORRECTED` — 含后来显示错误或不精确的陈述；修正在此记录。

---

## 2. 每条笔记的处置

### 2.1 `notes/foundations-and-geometry/`

| 文件 | 处置 | 等级 | 当前状态 / 目的地 |
| --- | --- | --- | --- |
| 01-cayley-hyperbolic-model | 未纳入 | STRUCTURAL PROPOSAL + 猜想 | 带分形边界的 Cayley 模型；「K=−2 几乎处处」断言是猜想的且未验证。见 OQ-078-A。 |
| 02-parameterized-evaluation-frameworks | 部分纳入 | STRUCTURAL PROPOSAL | 双管思想存活于 (A,M) charge 图景；代数全空间 `E_alg → B_eval` 与观测「ACS = 恒等参数纤维 (r=0,t=1)」不在任何论文。Paper IV 展望候选。 |
| 03-single-zero-diffusion-model | 已纳入 | （冲突） | 内容等于 Paper I §7 孤立零盘模型，**但倒置名 E₀/E₁**；见 C-1。 |
| 04-affine-torus-holonomy | 未纳入 | WORKING-NOTE PROVED | T² 上 4×4 分段映射、16 面 torsion 表、带共轭权重的离散 Stokes 律、四个算例环。Paper III（穿线/quandle 层）或 Paper IV（资源环）玩具校准候选。 |
| 05-process-groups-and-zariski-topology | 未纳入 | 初级部分 WORKING-NOTE PROVED；解释 STRUCTURAL | charge 同态下 ℤ 中理想的原像给 F₂ 正规子群与 Zariski 闭集格对应；初级且正确。「以 Spec ℤ 为截面的过程空间」读法是结构的。可选 Paper IV 展望。 |
| 06-hole-obstructions-ledger | 保留溯源副本 | COMPUTATIONALLY VERIFIED EXAMPLE + `EXPLORATORY` 读法 | 版本 1.0 后 2026-09-22 加入储备，故缺早先清单；2026-09-29 加入此处。探索登记 `temp/孔的不可避免性_v0.1.md` 加状态头的逐字副本，保留使 `paper-0/sections/11-holed-aes.tex` 的引用指向跟踪文件（那里引为 `Yuan2026AEGHoleRegister`）。六类计算阻碍及其脚本；「孔携带交换」句是章节动机且**不**由六个见证证明——Paper 0 §11.6 恰记录为非断言。不作依赖使用。 |
| 07-joint-quotient-acs-charge-aes-operator | 未纳入 | WORKING-NOTE PROVED | 2026-09-29 添加。ACS charge 端点与 AES 仿射算子的联合商 `G = ℝ_A × Aff⁺(1,ℝ)`；其中心与导出子群特征；两个读数是两个投影，核 `[G,G]` 与 `Z(G)`；对由纤维积 `G ≅ 𝔼² ×_ℝ ℍ²` 恢复群元；接触形式 `α = dB − dA − B dM` 有不可积水平分布（`[X,Y] = ∂_B`），故序缺陷是非可积性。**需集成审计**；`G` 非 Paper 0 对象且 Paper 0 拥有 ACS、AES 与接触结构。 |
| 08-isometric-realisations-thurston-geometries | 未纳入 | WORKING-NOTE PROVED（分类引为标准） | 2026-09-29 添加。无损实现 `ρ: G → Isom(X)` 带微分同胚轨道映射恰对 `ℍ²×ℝ` 与 `SL~₂(ℝ)` 存在；其余六模型由伴随谱论证（𝔼³、𝕊³、𝕊²×ℝ、Nil）、中心（ℍ³）与导出子代数维数（Sol）排除。Paper 0 §9 接触模型在 Reeb 单位扩张与反演 `I(A,M,B)=(−A,−M,−Be^{−M})` 后**是** `SL~₂(ℝ)` 几何（`I*α = ω = dA − e^{−M}dB`、`I*g_contact = F*g_SL`）的识别是可复用部分。**需集成审计**；八几何分类本身被引用，非重新推导。 |
| 09-automorphisms-dilation-and-obstructions | 未纳入 | WORKING-NOTE PROVED | 2026-09-29 添加。所有 Lie 自同构是 `F_{α,γ,δ,κ}(A,S,B) = (αA + γ log S, S, δB + κ(S−1))`、`αδ ≠ 0`；内者恰 `α=1, γ=0, δ>0`；`Φ_λ(A,S,B)=(λA,S,λB)` 实现平面相似，`D_λ T_g D_λ^{−1} = T_{Φ_λ(g)}`，对 `λ≠1` 为外；外层级 `Φ_2^n(Γ)` 平凡交而内者留 `ℤ×{0}`；`γ≠0` 被双重阻碍——`log` 非半代数，点稳定子论证禁止平面共轭。**需集成审计**。 |
| 10-punctures-are-critical-counterexample-record | 未纳入 | EVIDENCE RECORD（精确反驳；非提升候选） | 2026-09-29 添加。保留 `thm:p0-punctures-are-critical` 的验证反例使伴随审查有跟踪所指，与 `06-hole-obstructions-ledger.md` 同精神。模型是带光滑延拓赋值与 `S = {0} ≠ ∅ = Crit(ã)` 的穿孔 AES；缺口是证明构造新度量并称之为给定 `g` 的延拓。处置绑定 C-10；此记录本身不改论断状态。 |

### 2.2 `notes/analysis-and-calculus/`

| 文件 | 处置 | 等级 | 当前状态 / 目的地 |
| --- | --- | --- | --- |
| 01-horizontal-analysis-program | 已纳入 | program | 由 Paper II 实现：算子选择（因式分解对变分）、框架漂移 `Δ_g = X_u²+X_v²−c_vX_u+c_uX_v`、Appell 模、边界。 |
| 02-mixed-affine-integration | 未纳入 | WORKING-NOTE PROVED | 连续混合积分 `∫u·exp(∫_x^b v)`、传输/分裂/窗口导数恒等式、伴随配对、连续 ACS 三重恒等式。完整证明；**需集成审计**（哪篇论文、哪些约定）。 |
| 03-weighted-contact-calculus | 未纳入 | WORKING-NOTE PROVED | 分次协变微分 `∇^{(n)}f=δf−nf dM`、分次 Leibniz 律、规范矫正 `ã=e^{−M}a`、扭曲积 `⋆_M` 带导子 `D_M`、扭曲 Rota–Baxter 恒等式、对偶权线伴随几何、E₀/ACS 结构方程 `dω_A=ω_M∧ω_A`。完整证明；**需集成审计**。 |
| 09-order-topology-scott-lawson | 未纳入 | STRUCTURAL PROPOSAL + REFORMULATION | 参考词汇（Scott/Lawson/way-below/理想完备化，引 `CLASSICAL`）加对 AEG 标记脊柱历史的忠实实例化：信息序 = 年代前缀序，理想完备化 = 有限∪无穷历史（OQ-091，部分——分支情形开放）；加法 = way-below、乘法 = Scott 自同构、对偶 = 倒数对合（OQ-092，解决并修正 §6 措辞）；后向伴随 `p=¬(K)` 模常数，join = Lawson = Euclid（OQ-093）；混合积分单独 Scott 连续（函数配对）。整合的「缺失对合 = 后向伴随 = 序拓扑分析基础」读法是结构提案，非定理。 |
| 10–20（Scott–Lawson 主线） | 未纳入 | STRUCTURAL PROPOSAL + REFORMULATION（+ CLASSICAL）；两个已证明子结果 | 一条连续论证（2026-10-31）把 `09` 读回 Paper I 主体与 Paper 0 接触结构。`10` 生成元对应 `T_s=C_{+,s}^{(1)}`、`D_k=C_{×,k}^{(1)}`、`¬=C_{/,1}^{(2)}`；`11`–`13` OQ-094a（Scott ⟷ `Aff^+`、Lawson ⟷ `PGL₂`、「邻接 ¬」交换，**非** Galois 等价）；`14` OQ-094b（`ρ` 仅对平凡预序单调——**`WORKING-NOTE PROVED` 定理 1**——且唯一候选延拓是无穷矩阵积 = 连分数，Paper I 范围外）；`15` OQ-094c（分支历史 dcpo：信息序 = 下集嵌入，`Idl(FinDAG)` = 有限∪无穷 DAG，Birkhoff `O(P)`，前缀 = 链特化——`CLASSICAL` 理想完备化实例化）；`16` OQ-094d（Hecke 历史空间 = Cantor，`G₄≅C₂*C₄` 端 = Cantor，`H(√2)` 第一类极限集 = 圆；修正 `10` §4）；`17`–`18` 接触曲率 = 极小 DAG 序缺陷（生成元 = 精确流，序缺陷 = Lie 括号 `[D_u,D_v]=μλ∂a`，BCH）；`19` 全息 Stokes + 体边界（体平坦，缺陷 = 边界 holonomy——`STRUCTURAL PROPOSAL`）；`20` 缺陷是群值 1-余循环（telescoping 可加性，局部缺陷 = 共轭交换子，六边形 = Jacobi 恒等式——**`WORKING-NOTE PROVED`**，虽大体经典/平凡）。计算检查：`D_{-1}=T_1¬T_{-1}¬T_1¬`、BCH 密度 `μλ`、端枚举。整合的「接触 = 体积计算的 DAG 语言」与体边界（「全息」）读法是结构提案，非定理。残差：OQ-095（高阶括号、完整 DAG Lie 实现、宏观 Stokes、谱对接）。处置在 `governance/scott-lawson-paper-1-integration-2026-10-31.md`。 |
| 25-pants-interface-disks-and-substitution | 未纳入；新主线 | STRUCTURAL PROPOSAL + PROVED WITH STATED HYPOTHESES（工作笔记；需集成审计） | 指定装饰球–管加厚、曲面裤与内部界面盘；给有限拓扑证明、多项式替换/特征示例与常边界正则 AES 盘阻碍。规范 AEG 实现、一般装饰复合与原生 Seal 桥仍开放（OQ-096）。V1 现有已执行同作者有限证据：56 立方、336 四面体、局部链环、曲面/体填充区分、替换与十个负控制；一般 V2–V4 义务仍开放。不提升或重写笔记 15–24 或手稿断言。方向：苑明理；构造、证明与起草：Codex（OpenAI），2026-10-31。 |
| 21–24（级数论 + 跨项目对应） | 未纳入 | STRUCTURAL PROPOSAL + REFORMULATION（+ CLASSICAL）；一个计算验证示例 | `10`–`20` 主线的延续（2026-10-31）。`21` 级数论 = 自由 Lie 代数中的 Magnus 展开，带 arity-`k` ↔ (`k−1`)-胞腔对应（低阶 1–3 **`COMPUTATIONALLY VERIFIED EXAMPLE`** 经 `E₁₂,E₂₃,E₃₄` 幂零模型，系数 `hkl/3`；一般 arity-`k` 是 `OPEN`/`STRUCTURAL PROPOSAL`——OQ-095.1/095.2）与体边界三重约化；`22` 跨项目 Wu/Yang/Zhang ↔ AEG 半直/分配/缺陷对应（带 `[Adva]`/`[AEG]`/`[对应]` 标记骨架）；`23` 差替换 = 经 PBW 交换化 Magnus（`CLASSICAL` BCH/PBW + `structural proposal`）；`24` 非退化条件 = 缺陷 `μλ` 与弱非退化 = 逐层穿透（`structural proposal`，诚实注明 `lc=0` 非可逆对 `μλ=0` 可积）。残差：OQ-095（宏观 Stokes、完整 DAG Lie 实现、谱对接）。不提升论文断言。 |
| 26-donaghey-general-to-binary-tree | 未纳入；新主线 | STRUCTURAL PROPOSAL + CLASSICAL（结构对应；需集成审计） | 读 Donaghey 1980、Pushkarev–Byzov 2014 与 OEIS A014486；把一般树 ↔ 二叉树双射与 AEG 树层对齐。紧 `[对应]`：Donaghey σ（左/右转置）↔ AEG 镜像 `m`；θ（Dyck 反射）↔ 时间反演 `r`；φ（PPCT↔Dyck）↔ 上下码；右/左双射 ↔ `conv:p0-left-right-convention`（右/左梳）；四个 Catalan 族 ↔ 二元（顺序）对一般（分支）树。记录非交换差异：AEG 词级 `⟨m,r⟩ ≅ Z₂×Z₂`（Klein），而 Donaghey 树级 `⟨σ,θ⟩ ≅ Z₂*Z₂`（无限二面）带无限阶 `τ`（Pushkarev–Byzov Thm 6.4, Cor 6.3）。还记录 carousel 效应、fringing 定理、`O(n^{log₂3})` 轨道增长、PPCT 分配格断言。残差登记为 OQ-098（非交换扩展、PPCT 格对 `O(P)`、carousel/轨道对应、函子性）。不提升论文断言。 |
| 27-mirror-reversal-tree-layer | 未纳入；新主线 | STRUCTURAL PROPOSAL + CLASSICAL（结构对应；需集成审计） | 推进 OQ-098.1。确立 AEG 镜像 `m` 与反演 `r` 交换（`def:mirror-temporal-reversal`），故 `⟨m,r⟩ ≅ Z₂×Z₂`（Klein）；词 ↔ 梳双射（`prop:marked-tree-history-correspondence`）保持交换，故标记历史（单脊柱梳）层是 Klein——非交换 `Z₂*Z₂` **不**由把 AEG 现有运算传输到树获得。Donaghey `σ` 等于 `m`，但 `θ̃=φ⁻¹θφ`（Dyck 路径反射）非 AEG `r`（词反演）；`τ` 的无限阶与任意长轨道构造在分支树上（完全树 + fringing，Pushkarev–Byzov Cor 6.3），故非交换扩展属分支层（`O(P)`、线性扩张）。含 `n=2` 梳计算确认 `mr=rm`，与同伴有限验证 `research/donaghey-orbits/`（按 Pushkarev–Byzov Def. 2.1 实现 `τ`；复现 Donaghey `M_n(x)` 于 `n=1..10`；显示毛虫非 `τ` 不变且所有长度 `>6` 轨道是分支的）——`COMPUTATIONALLY VERIFIED EXAMPLE`、`n≤10`、非一般证明。平移残差：`θ̃` 自然性、`τ` 分支层提升、`τ` 梳上精确阶。不提升论文断言。 |
| 28-ppct-lattice-attribution | 未纳入；新主线 | STRUCTURAL PROPOSAL + CLASSICAL（格归属；需集成审计） | 推进 OQ-098.2。分离 PPCT 上两个候选格：(A) Tamari / 旋转格是格但**非分配**（`T_4`、`n=5` 见证、`research/ppct-lattice/`）；(B) 无穷二叉（立方）树的 Birkhoff 下集格分配，join-不可约元 = 顶点且大小 `N` 下集 `R(N)=Catalan(N)`。Pushkarev–Byzov 措辞「其不可约元按无穷立方树顶点排序的分配格」匹配 (B)，而「所有树的标准格排序」是 (A)；两者互斥，故来源措辞混淆。AEG `O(P)` 是有限依赖偏序上同一 Birkhoff 构造，故分配读法与 AEG 对齐但两者一般不合同。残差：`O(P)` 到 `T_∞` 上下集格的子格嵌入，与「标准格排序」的来源精确含义。不提升论文断言。 |
| 29-branching-layer-descent | 未纳入；新主线 | STRUCTURAL PROPOSAL + CLASSICAL + COMPUTATIONALLY VERIFIED EXAMPLE（n<=8；需集成审计） | 推进 OQ-098.1(b)，否定解决。AEG 依赖偏序（`def:internal-dependency-poset`）是内在骨架（后代序），遗忘平面左/右数据。Donaghey `τ` **不**尊重依赖偏序同构：同构依赖偏序的两棵树可映射到依赖偏序不同的树（显式 `n=4` 见证：3 链类成员映射到 3 链，另一个到「V」；每个骨架类对 `n≥5` 有非唯一 `τ` 像，验证 `n≤8`）。故 `τ` 不下降到 `P` 或 `O(P)`，双曲/长轨道行为严格是平面树现象，非偏序层。残差：非下降一般 `n` 证明；分支层是否有自身（非 τ）双曲结构；良定义下降所需精确平面数据。不提升论文断言。 |
| 30-donaghey-aeg-tree-layer-overview | 未纳入；综合 | STRUCTURAL PROPOSAL + CLASSICAL + COMPUTATIONALLY VERIFIED EXAMPLE（需集成审计） | 笔记 26–29 综合（OQ-098 线）。一句话：Donaghey/De Bruijn–Morselt 一般树 ↔ 二叉树变换精确匹配 AEG 树层（σ↔镜像 `m`、θ↔时间反演 `r`、φ↔上下码、R/L↔左/右梳），但其非交换 `Z₂*Z₂` / 双曲长轨道结构属平面树层，非梳层（098.1：AEG `m,r` 给 `Z₂×Z₂`/Klein；毛虫非 τ 不变，长轨道全分支，验证 `n≤10`）且不下降到依赖偏序 / `O(P)`（098.1(b)，验证 `n≤8`）。「PPCT 分配格」是无穷立方树的 Birkhoff 下集格，非 Tamari/旋转格（098.2）。残差：098.1(a) `θ̃` 自然性、098.2 子格嵌入 / 来源含义、098.1(b) 一般 `n` 与分支层自身动力学、098.3 carousel↔Hecke、098.4 函子性。不提升论文断言。 |
| 31-carousel-and-iota | 未纳入；新主线 | STRUCTURAL PROPOSAL + CLASSICAL + COMPUTATIONALLY VERIFIED EXAMPLE（猜想；需集成审计） | 调查用户猜测 carousel <-> iota。分离三个不同 iota：(A) 六态载体中 AEG 切割收缩（`c_i=ε_i+ι_i`、`Ω=TSR`、`Ω²=-1`、手性符号律偶保持/奇翻转）；(B) Adva **iota 框架** = 加倍切割坐标上复结构 `J²=-I`；(C) Adva **iota 组合子**（SKI 基；adva `0168` 排除其下辫/交换）。关键发现：AEG 六态载体与 Adva `0010` 手性载体 `W=(T⊕SR)⊕(S⊕RT)⊕(R⊕TS)` 是带 `J²=-I` 的同一 6 维空间（故 AEG iota = Adva iota 框架）。Carousel：类级核心是 4-环（`LL→RL→RN→LN`），计数影子是对合（阶 2，验证 `n≤7`，`research/donaghey-orbits/verify_carousel.py`）。猜想：carousel 4-环 = iota 复单位离散影子，指标 `k` 是单独平移；阶 2 对阶 4 不匹配开放。残差：类->载体映射、作用对齐、阶不匹配、fringing/exp 关系。不提升论文断言。 |
| 32-carousel-iota-alignment | 未纳入；新主线 | STRUCTURAL PROPOSAL + CLASSICAL + COMPUTATIONALLY VERIFIED EXAMPLE（反驳强形式；需集成审计） | 尝试笔记 31 §4 两项（类->载体映射；carousel = J？）。验证 `Ω²=-I`、`Ω⁴=I`、J 保持每个平面 `W_T,W_S,W_R`，每个平面四个带符号状态上 J 是单个 4-环（`research/iota-carousel/`）。强形式「六态上 carousel = J」被**反驳**：J 把正状态送到带符号状态（`SR↦-T`）、保持平面、carousel 有 5 类。carousel 类级 4-环 `LL→RL→RN→LN→LL` 可（非规范；3 平面 × 2 定向 = 6 候选）对齐到一个平面带符号状态上 J 的 4-环；但 `SR→LL` 条目与指标平移无 J 对应。故 carousel =（J 型旋转）+（平移）；平移的 iota 载体开放（候选：Laplacian `H` 或 `Λ¹↔Λ²` 分次）。不提升论文断言。 |
| 33-shift-research | 未纳入；新主线 | STRUCTURAL PROPOSAL + CLASSICAL + COMPUTATIONALLY VERIFIED EXAMPLE（否定结果；需集成审计） | 推进笔记 32 平移问题。iota 框架是**螺旋**：`[J,H]=0`、`J²=-I`、`A=-JH`、`A²=-H²`、`exp(tA)=cos(tH)-J sin(tH)`（旋转角 ∝ H 特征值）——验证。但 `H` **不能**携带 carousel 指标 `k`：切割图是依赖偏序的下集 Hasse 图（遗忘左/右），而 `k = #左叶` 是平面的；`n=4` 四棵树共享同一切割图谱却有 `k=3,2,1`（`research/iota-carousel/verify_shift.py`）。与笔记 29 同平面性阻碍。故平移需平面、无界载体（候选未确立）。不提升论文断言。 |
| 34-planar-carrier | 未纳入；新主线 | STRUCTURAL PROPOSAL + COMPUTATIONALLY VERIFIED EXAMPLE（构造；需集成审计） | 构造显式**螺旋模** `V = V_class ⊗ V_index`，`V_class=⟨LL,RL,RN,LN⟩`（平面：左/右 × 叶/非叶）与 `V_index=⟨e_k:k≥1⟩`（无界）。算子 `J:(c,k)↦(c+1,k)`（iota 复单位，Z/4）、`S:(c,k)↦(c,k+1)`（平移/高度）、carousel `C:(c,k)↦(c+1 mod 4, k+[c=LN])`。验证（全 True，`research/iota-carousel/verify_planar.py`）：`C⁴=S`（carousel 是**螺旋** / 射影 Z/4 = 平移的四次根）、`J⁴=id`、`[J,S]=0`、计数影子 `M²=id`（螺旋对计数不可见）。故平面载体存在；iota 供 `J`（旋转半），`S`（高度）独立。残差：从 AEG/Adva 导出 `S`；吸收 `SR`/环绕；词/历史 Z/4；角级 Thm 4.3。不提升论文断言。 |
| 35-derive-shift | 未纳入；新主线 | STRUCTURAL PROPOSAL + CLASSICAL + COMPUTATIONALLY VERIFIED EXAMPLE（部分导出；需集成审计） | 从 AEG 原生结构导出笔记 34 平移 `S`。carousel 指标 `k` 是**遍历位置**（Pushkarev–Byzov Thm 4.2）；AEG 标记历史的**年代指标**（`def:marked-spinal-history`、`eq:chronological-history-concatenation`）是自然无界位置 + 后继，故 `S` = 年代后继（追加一语境）。分层精度：**左梳**精确（DFS 左遍历 = 脊柱序 = 年代）；**右梳**差左/右翻转（DFS 先访离脊柱左叶）；**分支**层分道（DFS ≠ 线性扩张），与笔记 29 同缺口。验证 `research/iota-carousel/verify_traversal.py`。残差：分支层 `S`；直对半直 `V_class⊗V_index`；一般 `n`；切割基/时钟指标对词指标。不提升论文断言。 |
| 36-branching-layer-shift | 未纳入；新主线 | STRUCTURAL PROPOSAL + COMPUTATIONALLY VERIFIED EXAMPLE（导出；需集成审计） | 导出分支层 `S`。修正笔记 35：其「左遍历」是**先序**；年代/求值序是**后序**。验证：内部节点**左优先后序**是每个 PPCT（`n≤5`）依赖偏序的**线性扩张**，且对**左与右**梳都等于年代序 `[2,1,0]`；先序非线性扩张。故 `S` = 后序后继 = 「沿规范（左优先）脊柱历史前进」（`thm:birkhoff-downset-spinal`），平面（左优先）、无界、AEG 原生。残差：角序对求值序对齐（Thm 4.2）、左/右优先选择、一般 `n`、与笔记 29 下降阻碍关系。不提升论文断言。 |
| 37-corner-order-alignment | 未纳入；新主线 | STRUCTURAL PROPOSAL + CLASSICAL + COMPUTATIONALLY VERIFIED EXAMPLE（对齐；需集成审计） | 导出角序 ↔ 求值序对齐。Pushkarev–Byzov OCR 确认：「角」= **顶点**（SR/LL/RL/LN/RN 分类顶点），**左标准遍历是先序**。故 carousel `k` 是先序位置；求值序是后序。对齐（论文 Remark + 计算，`research/iota-carousel/verify_corner_order.py`）：**叶**——先序 = 后序（左到右前沿）；**非叶链**——反转；**跨不可比链**——选择（平衡树失败全局反转）。故 carousel `k` 的 `S` = **先序（角）后继**；笔记 36 的 `S` = 后序是求值序，叶相等、非叶反转。残差：规范跨链选择；一般 `n`；`S` 到螺旋；区分笔记 29 多值下降与角序非线性扩张缺口。不提升论文断言。 |
| 38-canonical-cross-chain-choice | 未纳入；新主线 | STRUCTURAL PROPOSAL + COMPUTATIONALLY VERIFIED EXAMPLE（规范化；需集成审计） | 规范笔记 37 跨链选择：定义规范线性扩张为**对角落序（先序）最小化逆序数（Kendall tau）**者。对 `n=4,5` 全部 PPCT 验证（`research/iota-carousel/verify_canonical_choice.py`）：极小者是**唯一**且等于**左优先后序**。故 `S`（笔记 36）非任意左优先选择而是最接近角序的唯一求值序；「选择」被解决。结构原因：先序与后序只在根位置不同，左优先序保留。残差：一般 `n` 证明；其他内在判据（叶序保持）给同一极小者；σ 等变；与笔记 29 形式分离。不提升论文断言。 |
| 39-canonical-choice-general-proof | 未纳入；新主线 | PROVED + COMPUTATIONALLY VERIFIED EXAMPLE（需集成审计） | 一般 `n` **归纳证明**：对角落序（先序）最小化逆序数的唯一线性扩张是左优先后序。关键步：对 `t = Node(a,b)` 任何线性扩张是 `M+[root]`，`M` 交错；根贡献常数 `m-1` 逆序；跨 `a`/`b` 逆序 `≥0` 且等号当且仅当 `M` 是块 `E_a+E_b`；归纳给 `Q(a)`、`Q(b)` 唯一。故 `Q(t)` 对每个 PPCT 是唯一极小者。计算扩到 `n ≤ 7`（193 树），一致。故笔记 38 规范化被证明，非仅验证。残差：其他内在判据（叶序保持）、σ 等变、与笔记 29 形式分离。不提升论文断言（研究笔记）。 |
| 40-carousel-iota-overview | 未纳入；综合 | STRUCTURAL PROPOSAL + CLASSICAL + PROVED（综合；需集成审计） | 笔记 31–39 综合（carousel ↔ iota 主线）。一句话：(i) **旋转半**——carousel 类级 4-环同构于 iota 复单位 `J`（`Ω=TSR`、`Ω²=-1`）作为 `C₄`，但仅非规范（`J` 保持平面且送正状态到带符号状态，故不解释 `SR→LL` 条目/指标）；(ii) **平移半**——`S` 是**角序（先序）后继**，在分支层实现为**左优先后序**，唯一规范化为与角序的**逆序极小者**（**一般 `n` 证明**，笔记 39）。载体：**平面螺旋模** `V=V_class⊗V_index` 带 `C⁴=S`（carousel = 射影 `Z/4`）。关键事实：AEG 六态载体 = Adva `0010` 手性载体；iota 框架是螺旋；`H` 不能携带指标（非平面）。残差：`θ̃` 内在定义、其他内在判据、σ 等变、与笔记 29 形式分离、fringing/轨道（098.3）、函子性（098.4）。不提升论文断言。 |
| 41-donaghey-iota-grand-overview | 未纳入；大综合 | STRUCTURAL PROPOSAL + CLASSICAL + PROVED（大综合；需集成审计） | 跨两个概览（笔记 30 与 40）对整条 26–40 线的大综合。一句话：笔记 26–40 沿两个正交主线研究一个对象（Donaghey tau）——树层主线（26–30：一般↔二元、R/L=左/右梳、sigma/theta/phi=镜像/反演/码、轨道、下降）与 carousel–iota 主线（31–40：tau 的 carousel = 旋转半 ↔ iota 复单位 J 加平移半 ↔ 角序后继 S）。由一个平面性阻碍统一（「左/右不可丢」出现三次——tau 不下降到 O(P)（笔记 29）、J 保持平面（笔记 32）、H 不确定指标（笔记 33））与一个已证明结论（平移的唯一逆序极小者规范化，笔记 39，一般 n）。载体：AEG 六态 = Adva iota 框架；极小平面载体 = 螺旋模 V=V_class⊗V_index、C^4=S。含 12 行映射、跨主线状态表与统一开放问题清单（098.1a、098.1b 残差、098.2 残差、098.3、098.4，加平面性阻碍必要性与 sigma 等变/其他判据）。不提升论文断言。**v0.3（2026-11-01）：扩到笔记 26–46，纳入 45（O(P) 是 Down(T_inf) 的格商，非子集子格；抽象嵌入开放）与 46（τ 无偏序级 trace——e、|O|、高度、不可比性全失败；不变量是平面 (k,l)）；平面性阻碍现有五次出现；映射现 17 行；开放问题表合并（098.1b：$n\le6$ 证据、一般 $n$ 开放；098.2：文本与商关系解决、抽象子格嵌入开放）。** |
| 42-fringing-hecke | 未纳入；新主线 | STRUCTURAL PROPOSAL + COMPUTATIONALLY VERIFIED EXAMPLE（部分对应；需集成审计；阶 4 对齐被笔记 47 取代：$J\sim R^2$，非 $J\sim C_4$） | 推进 OQ-098.3。分层答案。**结构对应成立**：两侧都是自由积作用本原周期轨道编码——AEG `Γ_4=C₂*C₄`（`eq:q4-sign-kernel-presentation`）带本原双曲类 ↔ 周期轨道（`prop:q4-hyperbolic-class-knot`）与零 dessin 作为编码脊柱（`thm:q4-zero-dessin-coding-spine`），对 Pushkarev–Byzov `⟨σ,θ⟩=Z₂*Z₂` 带 `τ`-轨道与角序编码。共享：自由积、本原、编码脊柱、周期轨道与阶 4 旋转（carousel `J`/`C⁴=S` ↔ Hecke `R²`，Hecke 生成元平方；笔记 47）。**增长率对应不成立**：fringing 的 `O(n^{log₂3})` 是轨道长度替换增长（验证 `Δ(Q(T))=3Δ(T)` 或 `(3/2)Δ(T)`，`research/iota-carousel/verify_fringing.py`），而 Hecke 侧是周期轨道计数（指数，熵 1）——不同量、不同率。残差：精确阶 4 同构/嵌入、码翻译、增长率配对、`Hist_4^{ph}` 对 τ 轨道类。不提升论文断言。 |
| 43-theta-tilde-intrinsic | 未纳入；新主线 | PROVED + COMPUTATIONALLY VERIFIED EXAMPLE（解决 098.1a；需集成审计） | 解决 OQ-098.1(a)。因 `τ = φ⁻¹θφσ` 且 `σ = m`，路径反射是 `θ̃ := φ⁻¹θφ = τ∘m`，经 `τ` 与 `m` 内在定义无需 Dyck 路径。证明：`θ̃² = id`（对合）与 `m∘θ̃ = τ⁻¹`；故 `⟨m,θ̃⟩ = ⟨m,τ⟩ ≅ Z₂*Z₂`（Donaghey Thm 6.4，`σ=m`）。验证 `n ≤ 6`（`research/iota-carousel/verify_theta.py`）：`θ̃²=id`、`m∘θ̃=τ⁻¹`、`θ̃` 轨道长度 ∈ {1,2}，`τ` / `m∘θ̃` 轨道长度相等。故 AEG 树层真携带 `Z₂*Z₂`（而词层只有 Klein `Z₂×Z₂`）；差异是 `θ̃ ≠ r`。残差：直接词级公式（τ 不保持梳）、更自然的「轮廓反射」描述、`θ̃ = r` 精确条件与 `⟨m,θ̃⟩` 几何实现。不提升论文断言。 |
| 44-functoriality-rl | 未纳入；新主线 | PROVED（无计数保持对象双射）+ COMPUTATIONALLY VERIFIED EXAMPLE；R/L 像未构造且其他对象函子仍开放（部分 098.4；需集成审计） | 推进 OQ-098.4。右/左双射是集合双射 `PPCT(n leaves) ↔ PPT(n-1 edges)`（Catalan c_{n-1}）。保持 AEG 序缺陷 / 线性扩张结构的函子性要求保持**运算偏序**，故至少**运算数**。计算（`research/iota-carousel/verify_functor.py`）：PPCT 侧总有 `n-1` 个二元内部节点；PPT 侧内部节点数范围 `{1,…,n-1}`（m=3 边分布 `{1:1,2:3,3:1}`）。n=4 多重集 `{3,3,3,3,3}` 对 `{1,2,2,2,3}`——**不同**，故无双射保持运算数，故无保持运算偏序 / 线性扩张 / 序缺陷。阻碍对保持运算偏序的任何对象双射**结构**；它不构造 Pushkarev–Byzov R/L 映射或测试特定像（「星 ↦ 3 运算树」注是预期行为，非计算事实）。其他对象（`O(P)`、`Hist_4`）函子仍开放。残差：R/L 映射本身此处不构造；其他对象（`O(P)`、`Hist_4`）函子；与笔记 29/33 关系。不提升论文断言。 |
| 45-downset-lattice-residual | 未纳入；新主线 | PROVED（商与非子集子格）+ COMPUTATIONALLY VERIFIED EXAMPLE + CLASSICAL；抽象子格嵌入仍开放（部分 098.2；需集成审计） | 处理 OQ-098.2 文本与商部分；抽象嵌入问题留开放。(i) **文本修正**：OCR 的 Pushkarev–Byzov §5 句读「not monotone with respect to the **standard lattice ordering of all trees**（**recall that the PPCTs form a distributive lattice whose irreducible elements are ordered as the vertices of the infinite cubic tree**）」——括号把「标准格排序」定义为分配（下集）格序，**非 Tamari**；这修正笔记 28「最可能 Tamari」读法（无论如何对象是 `Down(T_∞)`）。(ii) 精确关系：`O(P) = Down(P)` 是 `Down(T_∞)` 的**格商**——更精确地，含 `P` 的有限子树 `Q ⊂ T_∞` 的 `Down(Q)`——经限制 `ρ: S ↦ S ∩ P`，是**满射格同态**（保持 `∪`,`∩`）；它**非子集子格**（`Down(P) ⊄ Down(Q)`）；`O(P)` 是否作为某 `Down(Q)` 抽象子格嵌入仍开放。对四个小 `P` 验证非包含（`research/iota-carousel/verify_downset_quotient.py`）。还注明：分配格元素是 0/1/2 子有序二叉树（平面森林），非全 2 子 PPCT（经旋转识别）。残差：抽象子格嵌入；精确子集子格条件；「标准格排序」原始来源（Donaghey 1980 无「分配格」陈述）。不提升论文断言。 |
| 46-lifting-trace-planar | 未纳入；新主线 | COMPUTATIONALLY VERIFIED EXAMPLE（$n\le6$）+ CLASSICAL；一般 $n$ 无偏序不变量陈述开放（部分 098.1b；需集成审计） | 处理 098.1(b)「提升」残差（部分）：τ 是否在 `O(P)` 级留 trace？答案：**`n ≤ 6` 否**（有限证据，强于笔记 29）；一般 `n` 开放。即使粗偏序统计也不 τ 不变——对所有 `n ≤ 6`，`e(P)`（线性扩张）、`|O(P)|`（下集）、`height(P)`、`incomp(P)` 无一保持（见证 n=4：`N(L,N(N(L,L),L))` 有 `e=1`，其 τ 像 `N(N(L,L),N(L,L))` 有 `e=2`；链类 -> 分支）。真正不变量是**平面**角型 `(k,l)=(#LL,#RL)`，沿每轨道到交换保持（Pushkarev–Byzov Cor 4.5，验证）。检查范围内 τ trace 是平面的；`O(P)` 无。这是笔记 41 平面性阻碍第五次出现（τ 下降、J、H、R/L、现 τ 粗不变量）。残差：一般 `n` 无偏序不变量陈述；轨道级分布；笔记 45 商上多值 trace。不提升论文断言。 |
| 47-order4-alignment | 未纳入；新主线 | CLASSICAL + [对应] + PROVED（计算；精确阶 4 匹配；需集成审计） | 098.3 精确阶 4 对齐。carousel `J` 不直接与 Hecke `C₄` 生成元 `R` 对齐——`χ_J = λ²+1` 对 `χ_R = λ²-√2λ+1`，故不共轭。精确匹配是 **`J|_plane ~ R²`**：两者都是复结构（`(·)² = -I`、特征多项式 `λ²+1`、特征值 `±i`、线性阶 4 / 射影阶 2）；且 `R`（`R⁴ = -I`，SL₂ 阶 8 / PGL₂ 阶 4）是 carousel 复结构的**平方根**。故 carousel「阶 4 旋转」是 Hecke `C₄` 生成元的**平方**。sympy 验证（`research/iota-carousel/verify_order4.py`）：AEG 六态 `J` 来自 `Cl(3)`（Ω=TSR、Ω²=-1、三平面各 `[[0,-1],[1,0]]`），Hecke `R = J_h T = [[0,-1],[1,√2]]` 带 `R⁴=-I`、`R²` 带 `λ²+1`。残差：自然性（需 `W ≅ ℂ³` 与 H² 切平面共同空间）；三平面对一；Hecke `χ` 与 carousel `sgn` 是否同一符号特征；carousel 侧「J 的平方根」是什么。不提升论文断言。 |
| 52-scott-lawson-adva-interval-boundary | 未纳入；边界/纪律笔记 | STRUCTURAL PROPOSAL + REFORMULATION（+ CLASSICAL） | 2026-11-10 添加；v0.2 修订 2026-11-11。分离三层——有限有理表示、实区间完备化（连续 dcpo）与有效名称；有理有限区间**非** dcpo。记录常量生成元一致（`T_s, D_k, ¬`）与项级 `+,-,*,/` 依赖（`x-x`、`x/x`）；分离精确有限项 Scott 连续与固定网格舍入不连续；分离区间 Newton `RootExists` 与 `ExactZero`。不提升断言状态。仅登记（OQ-102）；`ZeroStatus`/`RootStatus`/`InvalidWitness` 词汇是候选 Paper I 零理论纪律笔记，非正文。 |
| 53-punctured-aes-flows-and-reduction | 部分纳入 | PROVED WITH STATED HYPOTHESES + STRUCTURAL PROPOSAL + OPEN PROBLEM | 2026-11-10 添加；v0.2 修订 2026-11-11。分离二维 AES 与动力学载体及奇维接触载体；记录三个完备化、无规范穿孔 holonomy、两个 Legendre 用法与带正速率与时间余循环的带型约化数据 `(N_reg,U_reg,B,X̃,Y,π,ν,τ,Σ,j,σ; optional G,R_g)`。光滑流约化定理（R-A 下降、R-B 逆提升/漂移、R-C 截面根、R-D 传输到基本模型）以 `PROVED WITH STATED HYPOTHESES` 提升到 Paper 0 §11（`prop:p0-reduction-descent`、`prop:p0-reduction-reverse`、`cor:p0-reduction-section`、`prop:p0-reduction-transport`），记录于 `governance/05b-paper-0-status-register.md`；穿孔 AES 应用仍 `STRUCTURAL PROPOSAL`；七个问题是 OQ-101。根存在路由（管重放 + Newton + 约化）仍是值层验证关注且不被提升。 |

### 2.3 `notes/computation-and-resources/`

| 文件 | 处置 | 等级 | 当前状态 / 目的地 |
| --- | --- | --- | --- |
| 01-binary-expression-complexity-program | 部分纳入 | STRUCTURAL PROPOSAL | 计划主题实现于 Paper IV 案例研究（Horner、OBDD、变换、检查点）。长度四 Catalan 成本计划本身仍开放。 |
| 02-path-loop-homology-toy-model | 部分纳入 | WORKING-NOTE PROVED（玩具） | T/D 世界、重写 2-胞腔、Thue–Morse 奇偶作为 H¹ 上链带 H₁(G)≅ℤ。哲学用于 Paper IV §8（重写纤维、telescope 阻碍）；Thue–Morse 校准示例本身未纳入。 |
| 03-turing-machine-resource-geometry | 部分纳入 | STRUCTURAL PROPOSAL + 定义 | 资源平面 (A,M)、ω=e^M dA、资源 torsion；Paper IV 选残差/状态路线。TM 特定 torsion 与其可证伪判据（分类可实现重排）仍开放；见 OQ-078-E。 |
| 04-resource-geometry-progress-memo | 部分纳入 | COMPUTATIONALLY VERIFIED EXAMPLE | Y-DAG 石子示例带 τ = 2e(e−1)；不同结束时间的「幽灵等待」闭包。算例未纳入；玩具之外闭包规则未测试。 |
| 05-computational-spacetime-geometry-program | 未纳入 | OPEN PROGRAM | PD₃ 计划带三个里程碑与显式通过/失败判据；里程碑 1（环面阶段 T²×[a₋,a₊]、`[κ]=μλ[du∧dv]≠0`、PD 对偶类）良定义。见 OQ-078-F。 |
| 06-computational-spacetime-duality | 未纳入 | STRUCTURAL PROPOSAL | 「路线 B」2-群胚：路径作 1-态射、由 torsion 标记的交换方块作 2-态射，de Rham 配对作时空对偶桥。尚无连贯定理。 |

### 2.4 `notes/knots-and-loops/`

| 文件 | 处置 | 等级 | 当前状态 / 目的地 |
| --- | --- | --- | --- |
| 01-figure-eight-arithmetic-loop | 部分纳入 | WORKING-NOTE PROVED | 两网格上 4₁ 关系子，闭包 ⇔ Δ(t)=0；仿射词计算是 Paper III App C。 |
| 02-zero-taxonomy-and-arithmetic-loops | 部分纳入 | STRUCTURAL PROPOSAL | 六层零分类；Paper I App E 保留前四层。零偏序与分离问题仍开放。 |
| 03-figure-eight-aeg-summary | 未纳入 | EXPLORATORY / 被取代 | H³ 上 `E_{4_1}`、「fire-burning」、λ=φ² 调参、π₁↔路径 / H₁↔ACS 字典。被 Papers I–III 的 q=4 Hecke 路线取代；归档。 |
| 04-figure-eight-hnn-arithmetization | 部分纳入 | 推导 WORKING-NOTE PROVED | HNN 算术化强制 t 是 Alexander 根（u↦+1、v↦+φ、t↦·φ⁻²）；笔记自身批判（标量加法不能表示 F₂）正确且预示 Paper III 坍缩定理。 |
| 05-figure-eight-modulo-arithmetization | 未纳入 | **CORRECTED** | 「稠密奇点」断言错误：商 R²/(ℤ(1,0)+ℤ(0,φ)) 是紧 Hausdorff 环面；稠密只属其一维投影（Kronecker）。见 C-8。 |
| 06-fox-calculus-and-alexander-modules | 部分纳入 | WORKING-NOTE PROVED | 仿射余循环 `D(uv)=D(u)+φ(u)D(v)` 作为 Fox-Leibniz 规则；交换子与 BS(1,2) Alexander 计算；Alexander 层定位是 Paper III §8。 |
| 07-figure-eight-arithmetic-interpretation | 部分纳入 | COMPUTATIONALLY VERIFIED EXAMPLE | SageMath/snappy 数据集：关系子闭包对到 11 交叉纽结清单恢复 Δ(t)=0。呈现与映射依赖；非定理。 |
| 08-small-knot-group-embeddings | 未纳入 | WORKING-NOTE PROVED（计算） | 三参数群 G 带 aᵐbⁿ 正规形；三叶/五叶嵌入带 Δ 因子。数据集候选；仅嵌入级断言。 |
| 09-knot-torsion-and-cyclotomic-fields | 未纳入 | COMPUTATIONALLY VERIFIED EXAMPLE | 经验因式分解 τ = σΔ(t)(t^K−1)/t^k、割圆因子、随机洗牌控制。数据集，非定理；见 OQ-078-G。 |
| 10-arithmetic-knot-geometry-zh | 部分纳入 | COMPUTATIONALLY VERIFIED EXAMPLE | 同数据集早期中文陈述。 |
| 11, 12（呈现问题，zh） | 未纳入 | EXPLORATORY | 喂笔记 01–09 的呈现选择问题。 |
| 13-knot-torsion-results | 未纳入 | COMPUTATIONALLY VERIFIED EXAMPLE | 4₁、6₂、6₃、7₆ 完整表。数据集。 |

### 2.5 `notes/projective-condensation/`

| 文件 | 处置 | 等级 | 当前状态 / 目的地 |
| --- | --- | --- | --- |
| 01-bilateral-projective-condensation | 已纳入 | — | Paper I §2–3（顺序分类、PGL₂ 生成）与 Paper IV §1–4（双赋值、商塔、框架 torsor、有限域计数、telescope 阻碍）直接来源。其 §10 接触比较猜想（AEG 水平分布对 PSL₂(R) 单位切接触结构）仍 CONJECTURE；见 OQ-078-H。 |
| 02-projective-geometric-frameworks | 未纳入 | EXPLORATORY | 2025 年 5 月射影对双曲定位讨论；被已纳入笔记 01 取代。 |
| 03-canonical-forms-and-condensation | 部分纳入 | STRUCTURAL PROPOSAL | 凝聚作商成为 Paper IV 代数凝聚；BS(1,1) 网格讨论喂 Paper 0。「计算能量/质量诱导曲率」隐喻仍未纳入且归档。 |

### 2.6 `notes/thermodynamics-and-renormalization/`

| 文件 | 处置 | 等级 | 当前状态 / 目的地 |
| --- | --- | --- | --- |
| 01-physical-evolution-landscapes | 未纳入 | EXPLORATORY | 概念备忘录（丰富性、相似/流行、凝聚）。 |
| 02-aeg-flow-and-renormalization-en | 未纳入 | EXPLORATORY | 双时间尺度读法（加法=动力学时间、乘法=演化时间/尺度）；解释性。 |
| 03, 04（zh） | 未纳入 | EXPLORATORY | RG 讨论与迭代示例；历史。 |
| 05-aeg-thermodynamics | 未纳入 | 核心 WORKING-NOTE PROVED | 显式接触同胚 Φ:(u,v,a)↦(S,V;U,T,p)=(v,−u;a,λa,μ) 拉回热力学形式；AEG 变量中 Maxwell 关系；相容性注（常数 (λ,μ) 与非平凡基本方程 U(S,V) 不相容）；Massieu 表示；可解族。独立对应笔记强候选；**需集成审计**。 |
| 06-algorithmic-thermodynamics | 未纳入 | PARTIALLY PROVED | 经线性成本 W=A+αM 首达路径的 Baez–Stay 桥；前缀自由首达论证被证明；完整 Gibbs/配分对应开放。 |
| 07-contact-algorithmic-thermodynamics | 未纳入 | WORKING-NOTE PROVED（固定 N 扇区） | 到 Baez–Stay 接触形式固定 N 切片的接触同胚。候选笔记。 |
| 08-keraia-aeg-correspondence | 未纳入 | EXPLORATORY | Keraia 机器字典（n₀,n₁ ↔ 加法/乘法 charge）。 |
| 09-keraia-aeg-mapping-correction | 未纳入 | CORRECTED（作为批判） | 记录原型可视化器两个真实错误：把独立可观测量 E,V 坍缩为一个静态量，混淆硬件成本与热力学共轭变量。保持附着于 06–08 任何未来使用。 |

### 2.7 覆盖缺口（2026-09-29 记录）

本审计「适用于」行声称覆盖 `notes/` 下每条笔记。2026-09-29 第 2 节对工作树的逐文件比较发现
**版本 1.0 从未覆盖的九条笔记**且 2026-09-29 修正案不定级，因定级需读取它们而此处未读：

* `notes/analysis-and-calculus/` — `04-hyperoperation`、`05-hyperoperation-calculus`、
  `06-process-concept-representation`、`07-reflection-on-coordinates`、
  `08-reflection-on-measurement-systems`；
* `notes/knots-and-loops/` — `11-figure-eight-presentation-problem-zh`、
  `12-knot-presentation-questions-zh`；
* `notes/thermodynamics-and-renormalization/` — `03-aeg-flow-and-renormalization-zh`、
  `04-renormalization-iteration-examples-zh`。

八个主题目录中两个完全覆盖；四个不。此处不断言这些文件内容。直到单独授权任务读取并定级，
本审计覆盖 `notes/` 下**除九个外**全部，上述「适用于」行应带该限定读。添加笔记时应重跑同检查。

### 2.8 归档交叉引用（各一行）

* `archive/revision-2/aristotle/` — 遗留论文陈述的 Lean 4/Mathlib 形式化（37 定理、零 `sorry`）。
  机器检查，但与当前论文版本不匹配；任何引用需遗留→当前陈述映射。
* `archive/ideal_glass/` — 把 AEG 接触/ACS 应用到理想玻璃协议的 Python 原型 + 中文工作笔记；通篇
  声明近似；探索性。
* `archive/peddle/` — 交互式石子游戏资源实验室（HTML）；视觉，未数学审计。

### 2.9 `notes/general/`（2026-11-14 添加；追加于 2.8 后避免 2.7/2.8 重编号）

| 文件 | 处置 | 等级 | 当前状态 / 目的地 |
| --- | --- | --- | --- |
| 001-htwr-core | 未纳入；新主线 | STRUCTURAL PROPOSAL | HTWR（双曲热带波前残差）核心：公理 I–IV 陈述 `P¹(Q)` + 对数 Weil 高度双曲校准、带 fanout Δ / erasure ε 作为成本生成元的装配世界面语法、热带波前/Bellman 传输与 Bellman–Galois 残差对偶。公理提案；无存在/唯一/不变定理。Paper IV（资源/复杂度层）展望候选，未分配。 |
| 002-htwr-example | 未纳入；新主线 | STRUCTURAL PROPOSAL（+ 恒等式的 STANDARD CONSEQUENCE） | 定理 1（时空不确定下界）与定理 2（Pell 收敛子两相 Pareto 边界）**条件于**公理 I–IV 证明；催化虫洞 Möbius 大步与 naive 对 Heron fanout 比较是核心机制。范/Newton 恒等式经典。不提升论文断言。 |
| 003-htwr-core.tex | 未纳入；001 编译伴侣 | STRUCTURAL PROPOSAL（同 001） | 001 的 LaTeX 渲染；非独立断言。 |
| 004-test-sequences | 未纳入；新主线 | STRUCTURAL PROPOSAL + COMPUTATIONALLY VERIFIED EXAMPLE（+ STANDARD CONSEQUENCE） | Pell/Fibonacci 统一到金属均值族（Cassini、Newton 加倍、Möbius 大步全验证）；Sylvester（双指数、无虫洞、naive = 最优）；Recamán（无结构、负参考）。为论文符号表记录记号冲突（Pell 数对伴 Pell）。 |
| 005-fanout-wrapping | 未纳入；新主线 | STRUCTURAL PROPOSAL + COMPUTATIONALLY VERIFIED EXAMPLE（+ STANDARD CONSEQUENCE） | Level-C 见证：在精确有理区间算术（`005-fanout-wrapping-witness.py`）复现 Pell 加倍映射 naive 与 Heron 形式包裹同一中心（577/408）但宽度 `W_true < W_heron < W_naive`，包裹过量随 fanout 计数单调且精确首阶比 577/288。由 `aeglib/python/examples/level_c_fanout_wrapping.py` 在 aeglib 0.0.2 `ArbBall`（VdP C11 区间类型）重放（宽比 ≈ 2.002）。「fanout 成本 = 包裹」对应（区间宽 ↔ 信息高度）是 STRUCTURAL PROPOSAL；残差 OQ-103。 |
| 006-split-tube-htwr | 未纳入；新主线 | PROVED WITH STATED HYPOTHESES（块三角性）+ STANDARD CONSEQUENCE（半径不等式）+ STRUCTURAL PROPOSAL（HTWR 读法）+ COMPUTATIONALLY VERIFIED EXAMPLE（轨道采样） | OQ-103.4：把 VdP C11 split-tube 形式化为 HTWR「主线（phase/action）+ fanout 辅助（变分 phi）」分解；证明（定义性，`006-split-tube-witness.py`）phase/action RHS 不读 phi，故 `r_phase <= r_unsplit`。诚实发现：收敛 C11 轨道上变分 RHS 不持续主导，故逐项包裹约化弱（<= ~9%）；其决定性价值在打靶期间（docs/17 §11）。把 OQ-103.4 推进到「形式化 + 弱约化确认」。 |
| 007-pan-encke-farey | 未纳入；新主线 | PROVED WITH STATED HYPOTHESES（共振阶梯）+ COMPUTATIONALLY VERIFIED EXAMPLE（边缘重合、重叠）+ STRUCTURAL PROPOSAL（Farey/Ford + HTWR 深度） | Pan/Encke 缝边缘波 AEG 应用：Lindblad 共振阶梯 `x=m/(m±1)` 是共转 `x=1` 的 Farey 邻域；aeglib `ArbBall` 认证共振半径（`pan_encke_resonance_ladder.py`，m=551 → a_P+161.6 km 于 Encke 外缘）与开缝判据（`pan_encke_gap_criterion.py`，Hill 半径 19.05 km、共振重叠 m≈475、缝≈8.5 R_H）。Farey/Ford 与 HTWR 深度读法是 STRUCTURAL PROPOSAL。残差（边缘波波长/振幅、密度波色散）：OQ-104。 |
| 008-encke-density-wave | 未纳入；新主线 | PROVED WITH STATED HYPOTHESES（色散闭式）+ STANDARD CONSEQUENCE（lambda_0）+ COMPUTATIONALLY VERIFIED EXAMPLE（波长曲线 + 图像测量） | OQ-104.1：闭式解紧绕密度波色散 `(ω−mΩ)²=κ²−2πGΣ|k|+c²k²`；径向波长 `λ₀=c²/(GΣ)≈0.75 km` 在共振处并向外递减（环绕），匹配观测「波长平滑变化」签名（Tiscareno et al. 2005）。图像测量（PIA08257、见证 `008-encke-edge-wave-image.py`）：边缘波方位波长 `λ_θ≈260–320 km`、径向振幅 `A≈0.65 km`、`m≈2600–3200`——清空缝内共振，确认边缘波是捕获边缘模，非自由 `m=551` 密度波。残差 D4 → 边缘模色散（OQ-104.3）。 |
| 009-encke-edge-mode-wkb | 未纳入；新主线 | PROVED WITH STATED HYPOTHESES（转向点）+ STANDARD CONSEQUENCE（m>=551 无模）+ COMPUTATIONALLY VERIFIED EXAMPLE（evanescent 衰减） | OQ-104.3（负闭包）：测试冷自引力 WKB 边缘模（`008-encke-edge-mode-wkb.py`）。转向点 `r_L=a_P((m+1)/m)^{2/3}` 仅对 `m<551` 在边缘外；对 `m≥551`（测得 `m≈2800`）共振在清空缝内且边缘远离共振（evanescent 衰减长 ≈0.5 m）。故观测边缘波非冷 WKB 边缘模；OQ-104.3 重围为压力约束边缘模或 Pan 近场畸变。 |
| 010-encke-scalloped-edge-tidal | 未纳入；新主线 | PROVED WITH STATED HYPOTHESES（受迫偏心率）+ COMPUTATIONALLY VERIFIED EXAMPLE（匹配图像） | Pan/Encke 线最终闭包：观测边缘波是线性区 `d≈8.5 R_H` 中 Pan 的**静态潮汐畸变**（受迫本轮）。受迫偏心率 `e_f=(M_P/M_S)(a_P/d)²≈5.9e-6`、径向振幅 `GM_P/(κ²d²)≈0.785 km`（观测 0.65 km）、方位 FWHM ≈249 km（观测 ~300 km）。见证 `010-encke-scalloped-edge-tidal.py`。残差（次签名：「变化平滑」/增-减/无阻尼）需完整动力学。 |

---

## 3. 冲突与过时登记

在此记录，不调和。任何未来工作优先级顺序仍是 `AGENTS.md` → 权威治理 → 当前论文源。

| ID | 冲突 | 证据 | 当前权威解决 |
| --- | --- | --- | --- |
| C-1 | E₀/E₁ 命名倒置 | `notes/foundations-and-geometry/03` 把孤立零盘命名 E₀、零线上半平面命名 E₁；遗留与当前论文用相反分配 | Paper I §6–7 与系列记号表；`governance/01` §17（E₀ = 基本双曲模型；E₁ 仅在奇异状态后固定） |
| C-2 | 「threadlike」= 每左子是叶 | 遗留 `sec02-00`；纽结笔记用 | Paper I §2 内在脊柱分类（Definition 2.x，顺序树） |
| C-3 | 经反路径 ACS 求值 `ν_x(γ)=e^{M}x+∫_{C̄γ}e^M dA` | 遗留 `sec05` | Paper I §8 直接路径公式 `ν_x(γ)=e^{M_γ}(x+∫_{C_γ}e^{−M}dA)` |
| C-4 | μ=λ=1 声称 Laplace 特征值 −2 | `archive/paper4p` 摘要 | 直接计算与 Paper I §6/App C：`Δa=2a`（梯度散度约定） |
| C-5 | δ 定义在坐标函数并由 Leibniz 扩展 | 遗留 `sec07` | Paper I §9：δ_H 限制为标量场；不声称分次复形 |
| C-6 | torsion 只对时间反演定义 | 遗留 `sec05` | Paper I §8：任意尺度/charge 相容对的相对 torsion |
| C-7 | 管结构提议在 Paper I 内 | `archive/paper4p` | Paper III 拥有管；Paper I 只保留正则总零集引理 |
| C-8 | 格 ℤ(1,0)+ℤ(0,φ) 的「稠密奇点」 | `notes/knots-and-loops/05` | 错误：商是紧 Hausdorff 环面；稠密只是一维投影性质。笔记标 CORRECTED。 |
| C-9 | 接触 CR / 扭曲调和 / Appell 基作为 Paper I 内容 | 遗留 `sec06`、`sec08` | Paper II 拥有全部；Paper I 只保留接触形式与水平括号。 |
| C-10 | `thm:p0-punctures-are-critical` 按打印为假 | `notes/foundations-and-geometry/10` 与根审查 `AEG-Paper-0-review-2026-09-29-thm-punctures-are-critical-v0.1.md`；反例符号验证 | **UNRESOLVED——记录，不调和。** 打印陈述只假设 `a` 光滑延拓；证明第一步构造 `g~ = |dã|²_{g₀} g₀ / (μ²+λ²ã²)`，满足 eikonal 恒等式但*非*给定 `g` 的延拓，而 `def:p0-punctured-aes` 条件 (ii) 要求延拓 `g` 本身。`cor:p0-puncture-count` 继承缺口。反向包含 `Crit(ã) ⊆ S` 与 `thm:p0-four-circle-model` 不受影响。修正于 `governance/05b-paper-0-status-register.md` 与 `governance/08-open-questions.md`（OQ-082）；论文源**不**被本审计编辑。 |

---

## 4. 未纳入储备，按就绪层

### Tier A — 工作笔记已证明，提升候选

任何论文条目前需集成审计（陈述/证明、约定、域数据）；本审计不提升任何。

1. `analysis-and-calculus/02` — 混合加乘积分。
2. `analysis-and-calculus/03` — 分次 δ 演算、扭曲积、Rota–Baxter、对偶权线几何。
3. `thermodynamics-and-renormalization/05` — AEG↔热力学接触同胚与 Maxwell 传输（加相容性阻碍注）。
4. `thermodynamics-and-renormalization/07` — 固定 N 算法热力学接触同胚。
5. `foundations-and-geometry/04` — 仿射环面 holonomy 玩具模型。
6. `foundations-and-geometry/05`（初级部分）— charge 同态对 ℤ 中理想与正规子群格。
7. `knots-and-loops/06` — Fox 演算 ↔ 仿射余循环（已部分在 Paper III §8；BS(1,2) 计算额外）。
8. `knots-and-loops/08` — 三参数群中小纽结嵌入。
9. `foundations-and-geometry/07` — ACS charge 与 AES 仿射算子联合商（2026-09-29 添加）。
10. `foundations-and-geometry/08` — Thurston 几何等距实现，含 Paper 0 §9 接触模型与 `SL~₂(ℝ)` 几何等同（2026-09-29 添加）。
11. `foundations-and-geometry/09` — 联合群自同构、扩张与 `γ≠0` 两阻碍（2026-09-29 添加）。

### Tier B — 计算验证数据集

作为数据保留；任何一般断言需呈现/映射依赖分析与证明。

* `knots-and-loops/07`、`09`、`10`、`13` — 关系子→Alexander 闭包与 torsion 因式分解表（SageMath/snappy）。
* `computation-and-resources/04` — Y-DAG 石子 torsion 与鬼等待闭包（算例）。
* `archive/aristotle` — 遗留陈述 Lean 验证（版本不匹配警告，C-set 见上）。

### Tier C — 结构提案与开放计划

* `analysis-and-calculus/25` — 新裤/界面盘/替换主线（2026-10-31），OQ-096。指定有限模型内提供短条件证明，含常边界正则 AES 封顶阻碍。其语义/几何识别与原生 Seal 桥仍开放；整体非手稿提升候选。

* `analysis-and-calculus/09` — Scott/Lawson 参考词汇加忠实 AEG 实例化（前缀序信息序、加法 = way-below、后向伴随 = 倒数、Lawson = Euclid）。整合的「序拓扑分析」读法是结构提案；分支历史 dcpo 仍开放（OQ-091）。
* `analysis-and-calculus/10`–`20` — Scott–Lawson 主线（2026-10-31 添加）：把 `09` 读入 Paper I 主体与 Paper 0 接触结构。可证明核心（OQ-094a–d 解决；接触曲率 `μλ` = 极小 DAG 序缺陷；缺陷是 1-余循环）组装 `CLASSICAL` 域/Lie 论与 `proved in paper-0/paper-1` 事实；整合的「接触 = 体积计算的 DAG 语言」与体边界（「全息」）读法是结构提案。残差：OQ-095（高阶括号、完整 DAG Lie 实现、宏观 Stokes、谱对接）。整体非提升候选；任何论文条目需 `05-mathematical-status.md` §4 集成审计。
* `computation-and-resources/05`、`06` — PD₃ 计划与路线 B 2-群胚。里程碑 1 带通过/失败判据良定义，应显式尝试或退役。
* `computation-and-resources/03` — 图灵机资源 torsion；阻塞问题是可实现内存增量重排分类（笔记自身可证伪判据）。
* `foundations-and-geometry/01` — Cayley 模型；K=−2 a.e. 曲率断言是开放猜想。
* `thermodynamics-and-renormalization/06`、`08` — 算法热力学桥；带 `09` 修正。
* `projective-condensation/01` §10 — PSL₂(R)/单位切丛对 AEG 水平分布的接触比较猜想。
* `general/001`–`005` — HTWR（双曲热带波前残差）主线（2026-11-14 添加）：`P¹(Q)` 上算术求值的资源/复杂度读法带对数 Weil 高度校准、时空不确定下界与 Pell/Fibonacci 收敛子两相 Pareto 边界（全条件于公理 I–IV），与 naive 对 Heron fanout 差被复现为精确有理区间包裹差的 Level-C 见证。残差：OQ-103。整体非提升候选；任何论文条目需 `05-mathematical-status.md` §4 集成审计。

### Tier D — 探索、被取代或修正

保留于 `notes/` 作为溯源；不作依赖使用：

* `foundations-and-geometry/02`（E_alg 丛，ACS 作纤维观测是唯一可挽救思想）、`thermodynamics-and-renormalization/01`–`04`、`knots-and-loops/03`（E_{4_1}、λ=φ²）、`05`（修正）、`11`、`12`、`projective-condensation/02`。

### Tier E — 证据记录（2026-09-29 添加）

保留使审查有跟踪所指；非提升候选且非依赖：

* `foundations-and-geometry/10` — `thm:p0-punctures-are-critical` 反例记录。其处置绑定 C-10。与根审查一起是 `governance/05b-paper-0-status-register.md` 与 `governance/08-open-questions.md` 修正背后的证据；其本身非状态记录。

---

## 5. 推荐处置

每项需单独授权任务；本审计不执行其中任何。

1. **混合演算技术笔记**（Tier A 1–2）：整合为一个自包含笔记或 Paper II 附录扩展；对照 Paper II 标量 δ_H 与 Paper I 接触形式审计框架约定。
2. **热力学对应笔记**（Tier A 3–4）：独立对应笔记或未来系列成员；任何论文放置前审计单位/归一化并决定目的地。
3. **环面玩具校准**（Tier A 5）：Paper III（穿线层）或 Paper IV（资源环）可选附录。
4. **纽结数据集**（Tier B）：与脚本保留于 `notes/`；只有 4₁ 实例当前用于 Paper III。一般「关系子闭包 ⇒ Alexander 多项式」定理**不**被数据授权且需呈现/映射依赖证明。
5. **PD₃ 里程碑 1**（Tier C）：在 `T²_{u,v}×[a₋,a₊]` 上尝试 `[κ]=μλ[du∧dv]≠0` 与显式 PD 对偶类，或记录为何退役。这是整个储备最便宜的具体步骤。
6. **TM 资源 torsion**（Tier C）：在投入更多不变量前解决或收窄可实现重排分类。
7. **Cayley 模型**（Tier C）：经分段线性共形因子分布曲率验证或证伪 K=−2 a.e. 断言。
8. **归档形式化**（Tier B）：若任何处引用，先发布遗留→当前陈述映射。
9. **联合商笔记**（Tier A 9–11，2026-09-29 添加）：任何论文放置前决定 `07`–`09` 目的地。`07` 与 `09` 是围绕 `G` 的新组织对象且不得归于 Paper 0；`08` 含一项看似直接可复用——Reeb 单位扩张与反演后 Paper 0 §9 接触模型与 `SL~₂(ℝ)` 几何的等同——该单命题可独立审计，与其余无关。
10. **C-10 反例**（Tier E，2026-09-29 添加）：决定是在共形延拓假设下重述 `thm:p0-punctures-are-critical`、加宽 `def:p0-punctured-aes` 排除反例类，还是收窄断言。本审计不编辑论文源；C-10 保持开放直到授权任务关闭。
11. **关闭覆盖缺口**（§2.7，2026-09-29 添加）：读取并定级本审计从未覆盖的九条笔记，使其「适用于」行为真。这是记账，非数学，是此处最便宜项。

---

## 6. 登记的新开放问题

以下由本审计加入 `governance/08-open-questions.md`：

* OQ-078 — 笔记储备：提升候选及其集成审计。
* OQ-079 — 笔记储备：冲突与修正台账（C-1 … C-10）。
* OQ-080 — 笔记储备：带通过/失败判据的开放计划（PD₃ 里程碑 1、TM 可实现重排、Cayley K=−2、算法热力学桥、接触比较猜想）。

全部优先级 P3（研究；不阻塞 Papers 0–IV）。

2026-09-29 修正案登记**无新开放问题**。C-10 属现有 Paper 0 项，通过修正 OQ-082 而非开平行
问题带入 `governance/08-open-questions.md`；OQ-079 台账范围相应更新为 C-1 … C-10。

---

## 7. 本审计刻意不做什么

* 它**不**编辑任何论文源、附录或参考文献。
* 它**不**提升任何笔记超出其记录等级。
* 它**不**把任何未纳入材料分配给论文；上述处置仅是推荐。
* 它**不**删除或重命名任何笔记，含被修正者（`knots-and-loops/05`），其保留且修正记录于 C-8。
* 它**不**解决第 3 节冲突；它们保持记录并由现有优先级顺序支配直到授权任务关闭。
* 它是**带日期快照**。版本 1.0 覆盖 2026-08-10 存在笔记；2026-09-29 修正案扩到其后添加四笔记。
  任何后来添加笔记须同法追加，否则本文件不再覆盖其「适用于」行所声称。
