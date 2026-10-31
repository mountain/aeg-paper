# Paper I 详细写作计划：序拓扑、DAG 分析学三支柱与孔—盖精细几何

**文档标识：** `paper-1-detailed-writing-plan.md`  
**状态：** 详细写作计划与章节级技术规范（基于 2026-10-31 最新研究进展整合）  
**基准版本：** `aeg-paper` 归档提交 `5be8059bc8678c4611a8f61c3b4ccd568c6d7009`  
**核心依据：**
* `notes/analysis-and-calculus/01`–`25`（重点涵盖 `02`–`03` 混合积分与分次接触微积分、`09`–`16` Scott–Lawson 序拓扑与分支历史 dcpo、`17`–`24` DAG 微分/积分/级数理论及跨项目对偶、`25` Pants/接口圆盘/代数代换与常值封盖障碍）
* `governance/00-authoritative-scope.md`、`governance/00b-paper-0-geometric-foundation-amendment.md`、`governance/02-paper-I-outline.md`、`governance/decisions-paper-I.md`、`governance/scott-lawson-paper-1-integration-2026-10-31.md`、`governance/notes-reserve-audit.md`、`governance/08-open-questions.md`（OQ-091–OQ-096）
* `paper-1/aeg-paper-1.tex` 及 `paper-1/sections/00`–`06`、`paper-0/sections/08`–`12`、`paper-4/sections/05b-ported-aes-programs.tex`、`research/pants-interface-disks/README.md`

## 1. 背景评估与总体架构设计

### 1.1 `notes/analysis-and-calculus` 近期更新的核心脉络

在 `notes/analysis-and-calculus/` 的近期推进（尤其是 `02`–`03` 及 2026-10-31 集中完成的 `09`–`25`）中，算术表达式几何（AEG）完成了从“单脊顺序词 + 局部接触几何”向**“分支 DAG 域论（Scott–Lawson 序拓扑）+ 分析学微积分三支柱（微分、积分、级数）+ 孔与盖的体-表精细几何”**的系统升级。其核心突破可概括为四条闭合或半闭合主线：

1. **序拓扑与历史层/射影层地基（Notes `09`–`16`，OQ-091–OQ-094）**：
   * Paper I 的三个初等单孔上下文 $T_s = C_{+,s}^{(1)}$、$D_k = C_{\times,k}^{(1)}$、$\neg = C_{/,1}^{(2)}$ 在连续格 $L=[0,\infty]$ 上精确对应 Scott 拓扑的 way-below（$\ll$）逼近见证、Scott 尺度自同构与反转序对合 $\neg:(L,\sigma)\xrightarrow{\sim}(L,\omega)$。
   * 代数侧从正仿射半群 $\operatorname{Aff}^+ = C(L,\sigma)\cap B_\infty$ 到全射影群 $\operatorname{PGL}_2(\mathbb{R}) = \langle\operatorname{Aff}^+,\neg\rangle$ 的扩张，与拓扑侧从单侧 Scott 拓扑 $\sigma$ 到双侧 Hausdorff Lawson 拓扑 $\lambda = \sigma\vee\neg_*\sigma$ 的扩张，在“生成数据 + 补 $\neg$”层构成自然同构交换方阵 $\Phi(\sigma\vee\neg_*\sigma)=\langle\Phi(\sigma),\neg\rangle$（同时严格证明其非全范畴 Galois 等价，并澄清全仿射群 $B_\infty$ 中的反射 $D_{-1}=T_1\neg T_{-1}\neg T_1\neg$ 已借道对偶算子 $\neg$）。
   * 顺序历史的前缀序 $\gamma\sqsubseteq\gamma\delta$ 推广为任意分支计算 DAG 依赖偏序集 $P=(I(T),\preccurlyeq_T)$ 的**下集（序理想）嵌入序** $P\sqsubseteq Q$；其理想完备 $\operatorname{Idl}(\mathrm{FinDAG},\sqsubseteq)$ 给出有限与（前驱有限化）无限计算 DAG 的 dcpo，固定有限 DAG $P$ 的偏求值构成有限分配格 $\mathcal{O}(P)$（Birkhoff 对偶），而极大链 = 线性扩展 = 标记脊髓历史。
   * 射影算子映射 $\rho:\Gamma^*\to\operatorname{PGL}_2(K)$ 因前缀追加与左乘反同态 $\rho(\gamma\delta)=\rho(\delta)\rho(\gamma)$ 的结构冲突，仅对平凡预序单调，无非退化 Scott 连续扩张；Lawson 乘积拓扑下的唯一候选极限为无限矩阵乘积 = 广义连分数 $[a_0;a_1,\dots]$，从而为 Paper I 的有限历史边界提供了严格的序拓扑与解析判据。同时更正了 $q=4$ Hecke 子语言的边界刻画：历史 Cantor 空间 $\Gamma_4^\omega\cong 3^\omega$ 编码的是殆自由群 $G_4\cong C_2*C_4$ 的组合**端空间（space of ends）**，而非第一类 Fuchsian 格 $H(\sqrt{2})$ 的几何**极限集** $\mathbb{P}^1(\mathbb{R})$。

2. **分析学三支柱：微分、积分与级数理论（Notes `01`–`03`, `17`–`24`，OQ-095）**：
   * **微分（Differentiation）**：通过极限/光滑化李函子 $F$，生成元 $A_h, M_k$ 实现为水平向量场 $D_u = \partial_u+\mu\partial_a$、$D_v = \partial_v+\lambda a\partial_a$ 的精确闭式指数流 $\Phi_u^h,\Phi_v^k$；最小分支 DAG $\{A,M\}$（组合平坦菱形 $B_2$）在值空间非交换实现下的开缺陷 $T_{\mathrm{open}}=\mu h(e^{\lambda k}-1)$ 与闭回路漂移 $T_{\mathrm{closed}}=\mu h(1-e^{-\lambda k})$ 的二阶混合导数密度恰为李括号 $[D_u,D_v]=\mu\lambda\partial_a$ 与接触曲率 $\mathcal{R}_H(F)=\mu\lambda(\partial_a F)\,du\wedge dv$。配合权 $n$ 分次水平协变微分 $\nabla^{(n)}f = \delta_H f - nf\,dM$（满足 $\nabla^{(1)}a = dA$ 与分次 Leibniz 法则），构成完整的水平微分学。
   * **积分（Integration）**：在一维层，连续混合仿射积分 $\mathfrak{M}_a^b[u;v]=\int_a^b u(x)\exp(\int_x^b v(s)\,ds)\,dx$ 统一了非齐次仿射输运解、反向 ACS 线积分 $\int_{C^{\mathrm{rev}}}e^M dA$、右端点滑窗 Volterra 卷积（含窗口导数 $\mathcal{A}'(w)=u(0)K(w)+\int_0^w u'(x)K(w-x)\,dx$）、扭曲 Rota–Baxter 积分 $I_M=e^M\circ J\circ e^{-M}$ 以及前向加性源 $u$（Scott 侧）与后向伴随余向量 $p(t)=e^{M(b)}\neg(K(t))$（下拓扑 $\omega$ 侧，$\nabla^{(-1)}p=0$）的 Lawson 双侧配对。在二维与高维 DAG 层，线性扩展图 $G(P)$ 上的交换缺陷构成精确 telescoping 群值 1-上闭链（全局赋值之余边界），局部相邻交换缺陷为后缀共轭交换子 $\rho(W)[x,y]\rho(W)^{-1}$，三元反链 hexagon 闭性对应无穷小 Jacobi 恒等式（离散 Bianchi 恒等式 $d\Omega=0$）；在体-表面层，体（有限 DAG / 紧致元）携带恰当曲率形式 $d\alpha = d(-\lambda a\,dv)$，经全息 Stokes 定理 $\int_\Sigma d\alpha = \int_{\partial\Sigma}(-\lambda a\,dv)$ 转化为理想边界表面（Scott 拓扑保留的真极限）上的 holonomy。
   * **级数（Series）**：历史词求值的对数 $\Omega(\gamma)=\log(e^{X_n}\cdots e^{X_1})$ 在自由李代数 $\operatorname{Lie}(X_1,\dots,X_n)$ 中展开为 Magnus 级数；其 **arity-$k$ 互异生成元嵌套括号**对应下集格 $\mathcal{O}(P)$ 的 **$k$ 元反链（$(k-1)$ 维胞腔）**（1 阶=电荷/0-胞腔，2 阶=$[X_i,X_j]$/1-胞腔菱形，3 阶=$[X_i,[X_j,X_k]]$/2-胞腔三元反链，已由 `sympy` 在三阶幂零李代数核验系数 $hkl/3$），而重复下标括号对应单流非线性修正。由于二维接触分布仅有 $\{D_u,D_v\}$ 两个方向，其互异元数止于 $\mathrm{arity}\le 2$；**唯有在一般分支 DAG 上，级数理论才能展开至全元数（$\mathrm{arity}\le n$）**。进一步地，体上的满级数投影到表面时经历三重全息简化：**降次**（2-形式 $d\alpha\to$ 1-形式势 $-\lambda a\,dv$）、**上闭链约化**（内部胞腔相消 $\to$ 边界闭类）与**规范形**（非规范 Magnus 展开 $\to$ 表面连分数规范形）。在 PBW 定理 $\operatorname{gr}(U(\operatorname{Lie}(\mathfrak{g})))\cong S(\mathfrak{g})$ 下，令缺陷 $\mu\lambda=0$（阿贝尔化）即退化为杨路差分代换的累积和与单项式展开。

3. **几何一侧对“孔（Holes）”与“盖（Caps）”的精细刻画（Note `25`、Paper 0 §§11–12、Paper I §5、Paper IV §5b，OQ-096）**：
   * **孔的五重严格区分**：语法单孔上下文槽位 $C_{\omega,c}^{(\varepsilon)}[z]$ $\neq$ 严格有限网络端口/输入孔（含 `discard(1/0)` 严格定义域）$\neq$ 装饰球-管厚化体侧表面 $S_G$ 上的拓扑孔口/接缝圆周 $C_e$ $\neq$ 几何本质穿孔 $S$（细分为赋值非 $C^1$ 型如 $\mathfrak{E}_1$ 与共形背景度量退化/临界点型 $S=\operatorname{Crit}(\widetilde{a})$ 如四圆八分支模型 $(xy)^2=0$）$\neq$ 四类不同边界（计算前沿、几何边界 $\partial H_G$、Stokes 积分链边界 $\partial\Sigma$、理想完备极限边界 $\Gamma^\omega$）。
   * **孔—盘（表面—体）互补定理（命题 A/B 及 V1 有限胞腔核验）**：“**表面给孔以意义，体给盘以意义**”。在球-管厚化体 $H_G$（柄数 $g(H_G)=\beta_1(|G|)$，侧表面欧拉示性数 $\chi(S_G)=2-2\beta_1(|G|)-b$）中，两个三端口 gate 的 pair of pants $P_1, P_2$ 沿内部管道截面 $D_e = D^2\times\{1/2\}$ 拼接时，边缘圆周 $C_e=\partial D_e$ 在四孔侧表面 $S_G = P_1\cup_C P_2$ 上是不可填的同调非平凡类（$[C_e]\neq 0\in H_1(S_G;\mathbb{F}_2)$，V1 模 2 边界矩阵秩 $110\to 111$），而在三维体 $H_G$ 内由接口圆盘 $D_e$ 精确填充（$i_*[C_e]=0\in H_1(H_G;\mathbb{F}_2)$）。沿 $D_e$ 切开计算体时，同一体内圆盘暴露为两侧方向相反的**盖子（Caps）**。
   * **接口圆盘状态、代数代换、常值封盖障碍与四重封合判据（命题 C）**：接口圆盘 $D_e$ 承载代数代换（多项式模型下对应字符评价谱值 $\chi_c(z)=c\in\operatorname{Spec}\mathbb{Q}[z]$ 与商环张量积 $B_+\otimes_{\mathbb{Q}[z]}B_\times$），并保留五元组 $(D_e,C_e;\sigma_e,r_e,\beta_e)$ 以区分数值状态 $\sigma_e$ 与生产过程残余 $r_e$ 及全态切向位移残余（`prop:p0-k4-motion-residue`）。**命题 C（常值边界圆盘无正则 AES 封盖定理）**严格证明：当 $\mu\neq 0$ 时，紧致光滑圆盘上不存在满足 $|da|_g^2=\mu^2+\lambda^2 a^2$ 且边界赋值为常值 $a|_{\partial D}=c$ 的正则 AES 数据。因此，端口数值标签 $\sigma_e=c$ 绝不能直接视为常值边界正则 AES 补片；必须严格区分**接口代换绑定**、**拓扑补盘/共形填点**、**正则 AES 双侧领口下降（`def:p0-collar-contract`）/奇异封盖**与 **Adva `Seal` 见证封合**。

### 1.2 针对 `paper-1` 的两种结构整合路径（架构决策建议）

由于 `governance/00b-paper-0-geometric-foundation-amendment.md` 确立了“单一权威源（one canonical source per result）”原则（将基础流、ACS 与接触曲率置于 `Paper 0`），而本次需求明确要求**为 `paper-1` 建立涵盖微分、积分、级数理论与盖、孔精细刻画的详细写作计划**，我们在制定章节级计划时提供两种兼容方案：

| 维度 | 方案 A：扩充型 `Paper I`（严守 `00b` 跨卷引用纪律，推荐作为默认平滑演进路线） | 方案 B：重构合卷型 `Paper I`（将 `02`–`03` 及 `09`–`25` 全面内化为独立正文定理） |
| :--- | :--- | :--- |
| **核心定位** | *AEG I: Foundations — Sequential and Branching Histories, Order-Topological Calculus, and Hole–Cap Geometry* | *AEG I: Foundations of History Calculus and Hole–Cap Geometry* |
| **与 `Paper 0` 关系** | 保持 `Paper 0` 对基础接触形式 $\alpha$、水平场 $D_u,D_v$、ACS 面积公式与四圆穿孔模型的所有权；`Paper I` 通过 `00-paper-zero-interface.tex` 显式导入基础定义，在正文开发**建立在历史/DAG 与端口层上的新理论**（Scott–Lawson 拓扑、李函子、混合积分双侧配对、1-上闭链、Magnus 级数、球-管厚化与孔—盖障碍定理） | 将 `Paper 0` §§8–9、§§11–12 的核心引理回迁或自包含重述于 `Paper I` 的分析与几何章节中，使 `Paper I` 成为不依赖 `Paper 0` 后半部即可独立阅读的完整奠基长文 |
| **与 `Paper II/IV` 边界** | 不触碰 `Paper II` 的二阶椭圆/扭曲调和算子 $\mathcal{H}_{\mathrm{tw}},\mathcal{L}_{\mathrm{var}}$ 与 Poisson 核；引用 `Paper IV` §5b 的严格有限网络代换定理而将球-管厚化、孔—盘互补与命题 C 放在 `Paper I` 几何侧 | 同左，但将 `notes/analysis-and-calculus/02`–`03` 的一维混合积分与分次 $\nabla^{(n)}$ 完整并入 `Paper I` 分析学章节 |
| **治理合规性** | 仅需登记局部集成审计（Integration Audit，见 `05-mathematical-status.md` §4），无需推翻 `00b` 修正案 | 需按 `00-authoritative-scope.md` §27 发起正式范围修正（`00d-paper-I-calculus-and-capping-amendment.md`） |

> **写作计划组织方式**：下文第 2 至第 5 章按**完整九章结构（含接口导言与四个附录）**展开详细写作计划。在每一章中，我们同时标明“**直接写入 `Paper I` 正文的定理/定义槽位**”与“**自 `Paper 0` / `Paper IV` 导入的接口声明**”，使该计划既能按**方案 A** 直接施工，也能按**方案 B** 展开为自包含长文。

## 2. 升级版 `Paper I` 总体章节结构与依赖图

### 2.1 目标章节序列（Target Section Sequence）

```text
Section 0. Interface: Imported Geometric Primitives from Paper 0
Section 1. Introduction: From Process Histories to Order-Topological Calculus and Hole–Cap Geometry
Section 2. Sequential and Branching Arithmetic Histories: Spine Classification, Down-Set DCPOs, and Birkhoff Duality
Section 3. Bilateral Projective Semantics, the Affine Sector, and the Scott–Lawson Topological Correspondence
Section 4. Analytical Pillar I — Differential Theory: The Smoothing Lie Functor, Minimal DAG Defects, and Graded Horizontal Calculus
Section 5. Analytical Pillar II — Integral Theory: Mixed Affine Integration, Dual Adjoint Pairing, 1-Cocycles, and Holographic Stokes
Section 6. Analytical Pillar III — Series Theory: Free Lie Algebra Magnus Expansion, Arity–Cell Correspondence, and Abelianization
Section 7. Geometric Characterization I — Taxonomy of Holes, Essential Punctures, and Regular Zero Rigidity
Section 8. Geometric Characterization II — Theory of Caps: Ball-and-Tube Thickening, Hole–Disk Complementarity, Capping Obstructions, and Certified Sealing
Section 9. Conclusions, Claim-Status Ledger, and Downstream Research Interfaces
Appendix A. Chronological Composition, Matrix Actions, and Orientation Conventions
Appendix B. Equality, Neutrality, and Residual Separation Examples
Appendix C. Symbolic and Computational Verifications for the Magnus Series (Up to Order 3) and PBW Abelianization
Appendix D. Finite Cellulation and Mod-2 Homology Verification Protocol for Pants Gluing and Interface Disks (V1–V4)
```

### 2.2 核心逻辑依赖图（Theorem Dependency Architecture）

| 层级 | 模块名称 | 核心输入依赖 | 产出的核心定义与定理槽位 | 下游供给目标 |
| :--- | :--- | :--- | :--- | :--- |
| **Layer 1: 历史与域论层** | §2 顺序与分支历史 | 二元表达式树 $T$、内部依赖偏序 $I(T)$ | `thm:sequential-tree-classification`、`prop:marked-tree-history-correspondence`、`thm:branching-dag-dcpo`（$\operatorname{Idl}(\mathrm{FinDAG})$）、`thm:birkhoff-downset-spinal`（$\mathcal{O}(P)$ 极大链 = 脊髓历史） | §3 拓扑对应、§4–§6 DAG 微积分、§8 下集前沿切割 |
| **Layer 2: 射影与序拓扑层** | §3 射影语义与 Scott–Lawson | §2 标记历史、`Paper 0` 生成定理 | `thm:bilateral-pgl2-generation`、`cor:affine-borel-sector`、`thm:scott-lawson-functorial-square`（$\operatorname{Aff}^+\leftrightarrow\sigma$, $\operatorname{PGL}_2\leftrightarrow\lambda$）、`thm:rho-monotonicity-obstruction`（连分数边界）、`prop:hecke-ends-vs-limit-set` | §4 流实现、§5 双侧伴随配对、§6 表面规范形 |
| **Layer 3A: 分析学—微分** | §4 微分理论 | §2 最小反链 $\{A,M\}$、§3 $\operatorname{Aff}^+$、`Paper 0` 接触形式 $\alpha$ | `lem:generators-exact-flows`、`thm:dag-defect-equals-curvature`（$[D_u,D_v]=\mu\lambda\partial_a$）、`def:graded-horizontal-differential`（$\nabla^{(n)}$）、`prop:graded-leibniz-and-gauge` | §5 积分论、§6 级数 2 阶项、`Paper II` 调和分析 |
| **Layer 3B: 分析学—积分** | §5 积分理论 | §3 对偶对合 $\neg$、§4 $\nabla^{(n)}$ 与流交换子、`Paper 0` ACS | `prop:mixed-integral-equivalences`、`thm:lawson-dual-adjoint-pairing`（$p=e^{M(b)}\neg(K)$）、`thm:defect-group-1-cocycle`（共轭交换子与 Jacobi 闭性）、`thm:holographic-stokes-minimal` | §6 级数体-表面降次与约化、OQ-095.3 宏观 Stokes |
| **Layer 3C: 分析学—级数** | §6 级数理论 | §2 下集格 $\mathcal{O}(P)$、§4–§5 李括号与 1-上闭链 | `def:history-magnus-series`、`prop:arity-cell-correspondence-low-order`（arity-$k \leftrightarrow (k-1)$-胞腔）、`prop:bulk-boundary-series-reduction`、`thm:pbw-abelianization-difference-substitution` | `Paper IV` 复杂度与消元界面、OQ-095.1/095.2 |
| **Layer 4A: 几何侧—孔** | §7 孔与穿孔零点几何 | `Paper 0` 正则/穿孔 AES 接口、§2 单孔上下文 | `def:fivefold-hole-taxonomy`、`thm:regular-zero-locus`、`thm:complete-regular-aes-splitting`、`def:singular-aes`、`prop:isolated-zero-singular-model` vs `thm:p0-punctures-are-critical` 对照 | §8 封盖障碍定理、`Paper III` 奇异管与纽结 |
| **Layer 4B: 几何侧—盖** | §8 盖与接口圆盘几何 | §2/§7、Note `25`、`Paper 0` §12、`Paper IV` §5b | `prop:local-pants-handlebody-genus`（命题 A）、`prop:pants-gluing-interface-disk`（命题 B）、`thm:hole-disk-complementarity`、`thm:constant-boundary-capping-obstruction`（命题 C）、`def:certified-cap-tuple` | `Paper IV` 端口程序与 Adva `Seal` 形式验证 |

## 3. 逐章详细写作计划（Sections 0–9 & Appendices）

### Section 0. Interface: Imported Geometric Primitives from Paper 0
* **目标文件**：更新 `paper-1/sections/00-paper-zero-interface.tex`（原 §4 `04-regular-aes-interface.tex` 合并至此或保留为独立短节，统一管理跨卷导入）。
* **核心写作内容**：
  1. **五卷分工声明**：明确 `Paper 0` 提供单累加器几何运动、基本双曲模型 $\mathfrak{E}_0$、单穿孔模型 $\mathfrak{E}_1$、四圆穿孔模型、累积交换空间（ACS）及接触流形 $(\mathcal{C},\alpha)$；`Paper I` 在此之上建立（a）顺序与分支历史的语法与序拓扑，（b）双侧射影算子语义，（c）历史与 DAG 上的微积分三支柱（微分、积分、级数），以及（d）正则/奇异零点几何与“孔—盖（Hole–Cap）”的精细几何刻画。
  2. **显式导入清单（保持原标签不变）**：
     * 正则 AES 定义 `def:regular-aes`（程函方程 $|\nabla a|_g^2 = \mu^2+\lambda^2 a^2, \mu\neq 0$）与典范算术标架 `prop:canonical-arithmetic-frame`（$X_u a=\mu, X_v a=\lambda a, [X_u,X_v]a=\mu\lambda$）。
     * 算术接触模型 $\mathcal{C}=\mathbb{R}^3_{(u,v,a)}$、接触 1-形式 $\alpha = da - \mu\,du - \lambda a\,dv$（`eq:arithmetic-contact-form`）、水平向量场 $D_u = \partial_u+\mu\partial_a, D_v = \partial_v+\lambda a\partial_a$（`eq:horizontal-arithmetic-fields`）及接触曲率括号 $[D_u,D_v]=\mu\lambda\partial_a$（`thm:contact-curvature`）。
     * 累积交换空间 $\mathcal{A}=\mathbb{R}^2_{(A,M)}$、直接路径求值公式 `prop:acs-evaluation` 与加权扭率—Stokes 定理 `thm:torsion-stokes`。
     * 穿孔 AES 定义 `def:p0-punctured-aes` 与双侧领口契约 `def:p0-collar-contract`。

### Section 1. Introduction: From Process Histories to Order-Topological Calculus and Hole–Cap Geometry
* **目标文件**：扩写 `paper-1/sections/01-introduction.tex`。
* **小节规划与核心论点**：
  * **1.1 过程先于结果（Process before Result）的扩展层级**：在原有图 `fig:process-result-structure` 基础上，将过程层级扩展为：
    $$\text{分支/顺序语法树 } T \longrightarrow \text{依赖偏序 } P \text{ 与下集格 } \mathcal{O}(P) \longrightarrow \text{标记脊髓历史 } \gamma \text{（极大链）} \longrightarrow \begin{cases} \text{射影/仿射算子 } \rho(\gamma) \longrightarrow \text{端点值 } \nu_x(\gamma) \\ \text{自由李代数 Magnus 级数 } \Omega(\gamma) \\ \text{ACS 电荷阴影 } (A_\gamma,M_\gamma) \end{cases}$$
  * **1.2 为什么需要序拓扑与分支 DAG**：解释单脊树（Sequential Tree）拥有唯一合法求值序，而一般分支树的多个合法求值序恰为下集分配格 $\mathcal{O}(P)$ 的极大链；引入 Scott 拓扑（从下有限逼近，加法 way-below）与 Lawson 拓扑（双侧 Hausdorff，补入互反对合 $\neg$）如何将代数上的“仿射 Borel 扇区 $\subset \operatorname{PGL}_2$”转化为拓扑上的“单侧 $\to$ 双侧”完备化。
  * **1.3 分析学的微积分三支柱（微分、积分、级数）**：概述如何通过极限/光滑化李函子连接离散 DAG 求值与连续接触流：微分度量最小分支菱形 $\{A,M\}$ 的无穷小非交换缺陷（曲率 $\mu\lambda$ 与分次微分 $\nabla^{(n)}$），积分通过 1-上闭链与全息 Stokes 将平直体的恰当形式转化为理想边界表面的 holonomy（以及一维混合积分的前向-后向双侧伴随配对），级数则通过自由李代数 Magnus 展开将 $\mathrm{arity}\text{-}k$ 嵌套括号定位于 $\mathcal{O}(P)$ 的 $(k-1)$ 维反链胞腔。
  * **1.4 几何一侧对“孔”与“盖”的精细刻画**：阐明为何单靠正则 AES（满足全局分裂 $M\cong Z(a)\times\mathbb{R}$）无法承载多零点分支网络与常值端口封盖（命题 C），从而必须严格区分五种“孔”与四种“封合（盖）”，建立“表面给孔以意义，体给盘以意义”的球-管厚化与孔—盘互补模型。
  * **1.5 贡献总结与范围边界（Claim Discipline）**：明确列出已证明定理（`PROVED` / `WORKING-NOTE PROVED`）、计算验证实例（`COMPUTATIONALLY VERIFIED EXAMPLE`）、结构性提议（`STRUCTURAL PROPOSAL`）及开放问题（OQ-095, OQ-096）。

### Section 2. Sequential and Branching Arithmetic Histories: Spine Classification, Down-Set DCPOs, and Birkhoff Duality
* **目标文件**：扩写 `paper-1/sections/02-sequential-histories.tex`，融合 `notes/analysis-and-calculus/09` §8 与 `15-branching-history-dcpo.md`。
* **小节与定理槽位设计**：
  * **2.1–2.5 保留并加固现有顺序历史核心（Keep & Preserve）**：
    * `def:arithmetic-expression-tree`、`def:internal-dependency-poset`（$(I(T),\preccurlyeq_T)$）、`lem:unique-linear-extension`。
    * **Theorem 2.1 (`thm:sequential-tree-classification`)**：四等价刻画（唯一线性扩展 $\iff I(T)$ 为链 $\iff$ 每个内部节点至多一个内部子节点 $\iff$ 单脊结构）。
    * `def:marked-spinal-history`（单孔上下文 $C_{\omega,c}^{(1)}[z]=\omega(z,c), C_{\omega,c}^{(2)}[z]=\omega(c,z)$、手性词 $\varepsilon(\gamma)$）、**Proposition 2.2 (`prop:marked-tree-history-correspondence`)**（标记平面顺序树 $\leftrightarrow$ 有界标记脊髓历史双射）。
    * 时序拼接 $\gamma\delta$、普通算术求值 $\nu_x(\gamma)$、平面镜像 $m\gamma$ vs 时间反转 $r\gamma$ vs 路径逆 $\gamma^{-1}$（`def:mirror-temporal-reversal`, `def:path-inverse`）及六层相等性层级。
  * **2.6 新增：顺序历史的前缀信息序与理想完备（源自 `09` §8，OQ-091）**：
    * **Definition 2.3 (`def:prefix-information-order`)**：在自由标记脊髓历史幺半群 $H=\Gamma^*$ 上定义时序前缀序 $\gamma\sqsubseteq\gamma' \iff \exists\delta\in\Gamma^*,\ \gamma'=\gamma\delta$。
    * **Proposition 2.4 (`prop:spinal-ideal-completion`)**：$(H,\sqsubseteq)$ 的理想完备 $\operatorname{Idl}(H)\cong \Gamma^{\le\omega}=\Gamma^*\cup\Gamma^\omega$ 构成 dcpo；紧致元恰为有限历史 $\Gamma^*$，每个无限历史 $\gamma_\infty=(g_1,g_2,\dots)=\bigsqcup_{n\ge 0}(g_1,\dots,g_n)$ 是其有限前缀的定向并。
  * **2.7 新增：分支计算 DAG 的下集信息序与 dcpo（源自 `15` §§1–4，OQ-094c）**：
    * **Definition 2.5 (`def:downset-information-order`)**：对有限计算 DAG（带运算/常量/槽位装饰的有限依赖偏序集）$P, Q \in \mathrm{FinDAG}$，定义信息序 $P\sqsubseteq Q$ 当且仅当 $P$ 是 $Q$ 的保持装饰的**下集（序理想，order ideal）**，即 $\forall x\in P, y\in Q,\ y\le_Q x \implies y\in P$（语义：“$P$ 是 $Q$ 的一个已完成的子计算”）。
    * **Theorem 2.6 (`thm:branching-dag-dcpo`)**：$\operatorname{Idl}(\mathrm{FinDAG},\sqsubseteq)$ 同构于全体“每个节点仅有有限多个前驱”的（有限或无限）计算 DAG 构成的 dcpo；紧致元恰为有限计算 DAG，且无穷前驱“扫帚型”DAG 被自然排除。当 $P$ 限制为链（顺序树）时，下集序退化为 §2.6 的时序前缀序。
  * **2.8 新增：固定分支树的偏求值格 $\mathcal{O}(P)$ 与 Birkhoff 对偶（源自 `15` §§5–6）**：
    * **Theorem 2.7 (`thm:birkhoff-downset-spinal`)**：对任意固定有限依赖偏序集 $P=I(T)$：
      1. 其全体下集按包含序构成有限分配格 $\mathcal{O}(P)$（偏求值状态格），且由 Birkhoff 表示定理有 $\operatorname{Stone}(\mathcal{O}(P))\cong P$（join-不可约元恢复原偏序集 $P$）；
      2. $P$ 的合法内部求值序（线性扩展）与 $\mathcal{O}(P)$ 中从 $\varnothing$ 到 $P$ 的**极大链** $\varnothing = D_0\subset D_1\subset\cdots\subset D_{|P|}=P$ 一一对应；
      3. 在选定初始累加器与槽位标记后，每条极大链唯一编码一条标记脊髓历史。因此，顺序树对应 $\mathcal{O}(P)$ 为单链的退化情形，而分支树的完整求值空间由分配格 $\mathcal{O}(P)$ 及其极大链族刻画。

### Section 3. Bilateral Projective Semantics, the Affine Sector, and the Scott–Lawson Topological Correspondence
* **目标文件**：扩写 `paper-1/sections/03-projective-affine.tex`，融合 `notes/analysis-and-calculus/09` §9、`10`–`14` 及 `16`。
* **小节与定理槽位设计**：
  * **3.1–3.6 保留现有双侧射影语义与仿射/Hecke 骨架（Keep & Preserve）**：
    * 初等单孔上下文矩阵表、普通可容许域与射影延拓的严格区分（`warn:projective-not-ordinary`）。
    * 射影求值反同态 $\rho(\gamma\delta)=\rho(\delta)\rho(\gamma)$（`prop:projective-evaluation-chronology`）、双侧生成定理 $\rho(\operatorname{Hist}^{\mathrm{nd}}_K)=\operatorname{PGL}_2(K)$（`thm:bilateral-pgl2-generation`）、仿射/Borel 扇区 $\rho(\operatorname{Hist}^{\mathrm{aff}}_K)=B_\infty\cong\operatorname{Aff}(1,K)$（`cor:affine-borel-sector`）、正实分量 $\operatorname{Aff}^+(1,\mathbb{R})$、秩一 Bruhat 分解 $\operatorname{PGL}_2(K)=B_\infty\sqcup B_\infty J B_\infty$ 及无穷小 Riccati 展望 $\dot{z}=\beta+\alpha z+\kappa z^2$。
  * **3.7 新增：值格 $L=[0,\infty]$ 上初等上下文的 Scott–Lawson 序拓扑刻画（源自 `09` §9、`10` §1、`11` §§1–3，OQ-092 & OQ-094a）**：
    * **Proposition 3.1 (`prop:generator-domain-roles`)**：在配备通常序的连续格 $L=[0,\infty]\subset\mathbb{P}^1(\mathbb{R})$ 上，Paper I 的三个初等上下文具有如下精确序拓扑角色：
      1. **加法平移 $T_s = C_{+,s}^{(1)}$（$s\ge 0$）**：是 Scott 连续嵌入（保定向并但 $s>0$ 时非满射），且恰为 way-below 关系 $\ll$ 的见证（对 $a>0$，$a\ll b \iff a<b \iff \exists s>0,\ T_s(a)=a+s\le b$），其前向轨道生成 Scott 拓扑 $\sigma(L)$ 的基 $\{\Uparrow a = (a,\infty]\}$；
      2. **正乘法伸缩 $D_k = C_{\times,k}^{(1)}$（$k>0$）**：是 $(L,\le)$ 的序自同构，从而是 $(L,\sigma)$ 的 Scott 自同胚；
      3. **第二槽除法（互反）$\neg = C_{/,1}^{(2)}: a\mapsto 1/a$（$0\leftrightarrow\infty$）**：是反序对合，给出从 Scott 拓扑到下拓扑（lower topology）的同胚 $\neg:(L,\sigma)\xrightarrow{\sim}(L,\omega)$，$\omega=\neg_*\sigma$，且满足 $\neg\circ D_k\circ\neg = D_{1/k}$；
      4. **Lawson 双侧合成**：$\lambda(L) = \sigma(L)\vee\omega(L) = \sigma(L)\vee\neg_*\sigma(L)$ 恰为 $[0,\infty]$ 上的紧 Hausdorff 欧氏拓扑。
  * **3.8 新增：四层仿射-射影层级与 Galois/函子交换方阵（源自 `11`–`13`，OQ-094a）**：
    * **Lemma 3.2 (`lem:four-level-affine-hierarchy`)**：在 $K=\mathbb{R}$ 上严格区分四个代数层级：
      $$\operatorname{Aff}^+ := \{a\mapsto ka+s : k>0, s\ge 0\} = B_\infty\cap\operatorname{Stab}([0,\infty]), \qquad \langle\operatorname{Aff}^+\rangle = B_\infty^+ = \{ka+s : k>0, s\in\mathbb{R}\},$$
      $$B_\infty = B_\infty^+\sqcup D_{-1}B_\infty^+, \qquad \operatorname{PGL}_2(\mathbb{R}) = \langle\operatorname{Aff}^+,\neg\rangle,$$
      其中负尺度反射 $D_{-1}(z)=-z$ 不属于 $\langle\operatorname{Aff}^+\rangle$，但满足显式六步分解
      $$D_{-1} = T_1\circ\neg\circ T_{-1}\circ\neg\circ T_1\circ\neg \in \langle\operatorname{Aff}^+,\neg\rangle.$$
      因此全仿射群 $B_\infty$ 已包含借道第二槽除法 $\neg$ 的对偶反射数据，纯单侧 Scott 载体为正仿射半群 $\operatorname{Aff}^+$。
    * **Theorem 3.3 (`thm:scott-lawson-functorial-square`)**：在反调 Galois 连接 $C\dashv\operatorname{Top}$ 下，考察三个射影限制函子 $A(\tau)=C(L,\tau)\cap B_\infty$、$E(\tau)=C(L,\tau)\cap\operatorname{PGL}_2(\mathbb{R})$ 与 $H(\tau)=\operatorname{Homeo}(L,\tau)\cap\operatorname{PGL}_2(\mathbb{R})$：
      1. **自同胚层**：$H(\sigma)=\{D_k:k>0\}$，$H(\lambda)=\operatorname{Stab}([0,\infty])=\langle H(\sigma),\neg\rangle\subsetneq\operatorname{PGL}_2(\mathbb{R})$（因 $T_s$ 非满射，自同胚层无法抵达全射影群）；
      2. **自映射生成层**：$A(\sigma)=\operatorname{Aff}^+$，在生成集 $S_0=\{T_s(s\ge 0), D_k(k>0)\}$ 上，“拓扑侧补 $\neg$（取 patch 拓扑 $\tau\mapsto\tau\vee\neg_*\tau$）”与“群侧补 $\neg$（取群闭包 $S\mapsto\langle S,\neg\rangle$）”构成交换方阵，满足自然性恒等式：
         $$\Phi(\sigma\vee\neg_*\sigma) = \langle\Phi(\sigma),\neg\rangle = \operatorname{PGL}_2(\mathbb{R}), \qquad \Phi(\sigma)=A(\sigma)=\operatorname{Aff}^+;$$
      3. **非全范畴 Galois 等价的严格边界**：证明不存在单一函子 $\operatorname{Top}(L)\to\operatorname{Sub}(\operatorname{PGL}_2(\mathbb{R}))$ 在 $\sigma,\lambda$ 上单射且同时取值为 $(\operatorname{Aff}^+,\operatorname{PGL}_2)$，因为 $A(\sigma)=A(\lambda)=\operatorname{Aff}^+$（坍缩）、$H(\lambda)\subsetneq\operatorname{PGL}_2$（过小）、而 $E(\sigma)\ni \neg T_s\neg$（过大，已含非仿射 Möbius 映射 $a/(1+sa)$）。
  * **3.9 新增：射影求值 $\rho$ 的 Scott 连续性负定理与 Hecke 端空间/极限集辨析（源自 `14`、`16`，OQ-094b & OQ-094d）**：
    * **Theorem 3.4 (`thm:rho-monotonicity-obstruction`)**：设 $\le$ 为 $\operatorname{PGL}_2(K)$ 上的任意偏序。若 $\rho:(\Gamma^*,\sqsubseteq)\to(\operatorname{PGL}_2(K),\le)$ 单调，则 $\le$ 必为平凡预序（$\forall x,y,\ x\le y$）；故 $\rho$ 不存在取值于非平凡 dcpo 的 Scott 连续扩张。在历史 dcpo $\Gamma^{\le\omega}$ 的 Lawson（乘积）拓扑下，$\rho$ 的唯一候选极限扩张为无限矩阵乘积 $\hat{\rho}(\gamma_\infty)=\lim_{n\to\infty}[M_n\cdots M_1]$，其在周期交替历史 $\gamma_i=(\neg,T_{a_i})$ 下恰为广义连分数 $[a_n;a_{n-1},\dots,a_0]$ 的收敛性——从序拓扑角度严格锁定了 Paper I 限制于有限历史词的范围边界。
    * **Proposition 3.5 (`prop:hecke-ends-vs-limit-set`)**：对 $q=4$ Hecke 子语言 $\operatorname{Hist}_4$（字母表 $\Gamma_4=\{\mathsf{t}_+,\mathsf{t}_-,\mathsf{j}\}$）：
      1. 完备历史空间 $\Gamma_4^{\le\omega}$ 在 Lawson 拓扑下紧 Hausdorff，其无限历史边界 $\Gamma_4^\omega\cong 3^\omega$ 为标准 Cantor 空间；
      2. 射影算子群 $G_4 = \langle T,J\mid J^2=(JT)^4=1\rangle \cong C_2 * C_4$ 是殆自由群，其组合**端空间** $\operatorname{Ends}(G_4)$（Bass–Serre 树边界）为 Cantor 集，由 $\Gamma_4^\omega$ 中不含禁止词 $\{JJ,(JT)^4,(TJ)^4\}$ 的有限型子位移（SFT）约化词编码；
      3. 作为 Fuchsian 群，$G_4 = H(\sqrt{2})$（参数 $\lambda_4=\sqrt{2}\le 2$）是有限余体积的**第一类** Fuchsian 格，其几何**极限集** $\Lambda(G_4)=\mathbb{P}^1(\mathbb{R})$ 是整个实射影圆周而非 Cantor 集。严格区分“历史 Cantor 空间 $\to$ 组合端空间 $\operatorname{Ends}(G_4)$”与下游 Paper II/III 的“第一类极限集 $\mathbb{P}^1(\mathbb{R})$”。

### Section 4. Analytical Pillar I — Differential Theory: The Smoothing Lie Functor, Minimal DAG Defects, and Graded Horizontal Calculus
* **目标文件**：新建 `paper-1/sections/04-differential-theory.tex`，融合 `notes/analysis-and-calculus/17`、`18` 及 `01`、`03` 的一阶微分部分。
* **小节与定理槽位设计**：
  * **4.1 离散生成元到连续水平流的极限/光滑化李函子（源自 `18` §§1–3）**：
    * **Lemma 4.1 (`lem:generators-exact-flows`)**：在接触状态空间 $\mathcal{C}=\mathbb{R}^3_{(u,v,a)}$ 上，加性生成元 $A_h = T_{\mu h}$ 与正乘性生成元 $M_k = D_{e^{\lambda k}}$ 恰为水平向量场 $D_u = \partial_u+\mu\partial_a$ 与 $D_v = \partial_v+\lambda a\partial_a$ 的时间 $h$ 与时间 $k$ **精确闭式指数流**在赋值纤维 $a$ 上的作用：
      $$A_h(a) = \left.\Phi_u^h(0,0,a)\right|_a = a+\mu h, \qquad M_k(a) = \left.\Phi_v^k(0,0,a)\right|_a = e^{\lambda k}a.$$
    * **Lemma 4.2 (`lem:word-flow-antihomomorphism`)**：映射 $F:\operatorname{Hist}(\{A,M\})\to\operatorname{Diff}(\mathcal{C})$，$F(A_h)=\Phi_u^h, F(M_k)=\Phi_v^k$ 将时序拼接反同态地映为流复合 $F(\gamma\delta)=F(\delta)\circ F(\gamma)$。
  * **4.2 最小分支 DAG $\{A,M\}$ 的序缺陷与接触曲率定理（源自 `17` §§1–5、`18` §§4–6）**：
    * **Theorem 4.3 (`thm:dag-defect-equals-curvature`)**：设 $P=\{A,M\}$ 为二元素反链（加与乘不可比），其下集格 $\mathcal{O}(P)=B_2=\{\varnothing,\{A\},\{M\},\{A,M\}\}$ 为四元自由分配菱形格，Stone 谱 $\operatorname{Stone}(\mathcal{O}(P))=\{A,M\}$，两条极大链对应脊髓历史 $\gamma_1=(A_h,M_k)$ 与 $\gamma_2=(M_k,A_h)$。则：
      1. **开缺陷与闭回路漂移**：$\nu_a(\gamma_1)-\nu_a(\gamma_2) = T_{\mathrm{open}}(h,k) = \mu h(e^{\lambda k}-1)$，四步闭回路 $(A_h,M_k,A_{-h},M_{-k})$ 的垂直漂移为 $T_{\mathrm{closed}}(h,k) = \mu h(1-e^{-\lambda k}) = e^{-\lambda k}T_{\mathrm{open}}(h,k)$；
      2. **无穷小二阶导数 = 李括号 = 接触曲率**：
         $$\left.\frac{\partial^2 T_{\mathrm{open}}}{\partial h\,\partial k}\right|_{0,0} = \left.\frac{\partial^2 T_{\mathrm{closed}}}{\partial h\,\partial k}\right|_{0,0} = [D\_u,D\_v](https://www.google.com/search?q=a) = \mu\lambda, \qquad [D_u,D_v] = \mu\lambda\,\partial_a;$$
      3. **谱与实现的分离（Structural Refinement）**：组合体 $\mathcal{O}(\{A,M\})$ 与 Stone 谱本身曲率为 $0$（平坦）；曲率 $\mu\lambda$ 产生于将两个在电荷层交换的方向提升到值空间作非交换流实现的一步（半直积重标定律 $D_k\circ T_s = T_{ks}\circ D_k$ 与朴素换序 $T_s\circ D_k$ 之差）。
  * **4.3 分次水平协变微分 $\nabla^{(n)}$ 与扭曲导数（源自 `01` §2、`03` §§2–4）**：
    * 导入标量水平微分 $\delta_H F = dF - (\partial_a F)\alpha = (D_u F)\,du + (D_v F)\,dv$ 及其反对称二阶曲率算子 $\mathcal{R}_H(F) = (D_u D_v F - D_v D_u F)\,du\wedge dv = \mu\lambda(\partial_a F)\,du\wedge dv$（`Paper 0` §9.5）。
    * **Definition 4.4 (`def:graded-horizontal-differential`)**：在自然算术单位 $dA=\mu\,du, dM=\lambda\,dv$ 下，对整数权 $n\in\mathbb{Z}$ 的截面 $f$，定义**权 $n$ 水平协变微分**：
      $$\nabla^{(n)}f := \delta_H f - n f\,dM.$$
    * **Proposition 4.5 (`prop:graded-leibniz-and-gauge`)**：
      1. 赋值函数 $a$ 为权 $1$ 对象，满足基本传播律 $\nabla^{(1)}a = \delta_H a - a\,dM = dA$；
      2. **分次 Leibniz 法则**：对权 $m$ 的 $f$ 与权 $n$ 的 $g$，有
         $$\nabla^{(m+n)}(fg) = \bigl(\nabla^{(m)}f\bigr)g + f\bigl(\nabla^{(n)}g\bigr);$$
      3. **规范展平（Gauge Rectification）与扭曲乘积**：令 $\widetilde{a} := e^{-M}a$（权 $0$），则 $\delta_H\widetilde{a} = e^{-M}dA$；在单参数曲线上定义扭曲乘积 $(F\star_M G)(t) := e^{-M(t)}F(t)G(t)$ 与扭曲导数 $D_M := \frac{d}{dt} - M'(t) = e^M\circ\frac{d}{dt}\circ e^{-M}$，则 $D_M$ 是关于 $\star_M$ 的严格导子：$D_M(F\star_M G) = (D_M F)\star_M G + F\star_M(D_M G)$。

### Section 5. Analytical Pillar II — Integral Theory: Mixed Affine Integration, Dual Adjoint Pairing, 1-Cocycles, and Holographic Stokes
* **目标文件**：新建 `paper-1/sections/05-integral-theory.tex`，融合 `notes/analysis-and-calculus/02`、`03`、`09` §§10–11、`19` 及 `20`。
* **小节与定理槽位设计**：
  * **5.1 一维连续混合仿射积分及其四重恒等式（源自 `02` §§1–4、`03` §§2–4）**：
    * **Definition 5.1 (`def:mixed-affine-integral`)**：对 $[a,b]$ 上的可积密度 $u,v\in L^1([a,b])$，定义绝对时间参数化下的**连续混合加-乘积分**：
      $$\mathfrak{M}_a^b[u;v] := \int_a^b u(x)\exp\!\left(\int_x^b v(s)\,ds\right)dx,$$
      以及右端点滑窗参数化下的单侧 Volterra 卷积形式 $\mathcal{A}(w) := \int_0^w u(x)K(w-x)\,dx$，其中 $K(r)=\exp(\int_0^r v(y)\,dy)$。
    * **Proposition 5.2 (`prop:mixed-integral-equivalences`)**：
      1. **仿射输运与分裂律**：$\mathfrak{M}_a^b[u;v]$ 是非齐次仿射输运方程 $w'(t)=v(t)w(t)+u(t)$ 的非齐次传播项（$w(b)=e^{\int_a^b v}w(a)+\mathfrak{M}_a^b[u;v]$），满足 $\mathfrak{M}_a^c[u;v] = e^{\int_b^c v}\mathfrak{M}_a^b[u;v] + \mathfrak{M}_b^c[u;v]$ 及右端点导数 $\frac{d}{db}\mathfrak{M}_a^b[u;v] = u(b)+v(b)\mathfrak{M}_a^b[u;v]$；
      2. **滑窗导数与分部积分对偶**：当 $u\in C^1([0,w]), v\in C([0,w])$ 时，窗口增长触发加法轮廓导数 $u'$：
         $$\mathcal{A}'(w) = u(0)K(w) + \int_0^w u'(x)K(w-x)\,dx = u(w) + \int_0^w u(x)v(w-x)K(w-x)\,dx;$$
      3. **反向 ACS 线积分**：在累积交换空间 $\mathcal{A}$ 上，$\mathfrak{M}_a^b[u;v] = \int_{C^{\mathrm{rev}}}\eta$（其中 $\eta=e^M dA$，$C^{\mathrm{rev}}$ 为反向密度生成的连续 ACS 路径）；
      4. **规范共轭与扭曲 Rota–Baxter 恒等式**：混合积分算子 $(I_M f)(t)=e^{M(t)}\int_{t_0}^t e^{-M(s)}f(s)\,ds = (e^M\circ J\circ e^{-M})f$ 关于扭曲乘积 $\star_M$ 满足扭曲 Rota–Baxter 恒等式：
         $$I_M(f)\star_M I_M(g) = I_M\bigl(I_M(f)\star_M g + f\star_M I_M(g)\bigr).$$
  * **5.2 对偶权线丛、后向伴随乘子与 Lawson 双侧泛函配对（源自 `02` §5、`03` §5、`09` §§10–11，OQ-093）**：
    * **Theorem 5.3 (`thm:lawson-dual-adjoint-pairing`)**：
      1. **对偶联络**：在权 $-1$ 对偶线丛 $L^{-1}$ 上定义 $\nabla^{(-1)}p := \delta_H p + p\,dM$，则标量配对满足 $\delta_H(pa) = (\nabla^{(-1)}p)a + p(\nabla^{(1)}a)$；当 $p$ 满足齐次后向平行移动方程 $\nabla^{(-1)}p = 0$（即 $-p'(t)=v(t)p(t),\ p(b)=1$）时，$\delta_H(pa) = p\,dA$，故 $\mathfrak{M}_a^b[u;v] = \int_a^b p(t)u(t)\,dt$；
      2. **后向伴随 = 互反对合像**：前向尺度 $K(t)=e^{M(t)}$ 与后向伴随乘子 $p(t)=\exp(\int_t^b v(s)\,ds)$ 满足精确反序对合关系：
         $$p(t) = e^{M(b)-M(t)} = K(b)\cdot\neg\bigl(K(t)\bigr), \qquad \neg(a)=\frac{1}{a};$$
      3. **双侧 Scott 连续性与 Lawson 泛函完备**：前向尺度 $K$ 编码 Scott（从下逼近）拓扑 $\sigma$，后向伴随 $p$ 编码下拓扑 $\omega=\neg_*\sigma$；对非负密度 $u,v\ge 0$，泛函 $\mathfrak{M}[u;v]$ 对 $u$ 与对 $v$ 分别单调且保定向并（分别 Scott 连续），而双侧配对 $\int_a^b u(t)p(t)\,dt$ 恰为 $\lambda=\sigma\vee\omega$ 在泛函层的实现。
  * **5.3 线性扩展图 $G(P)$ 上的群值 1-上闭链与 Jacobi 闭性（源自 `20` §§1–7，配合 `25` §7 边界澄清）**：
    * **Theorem 5.4 (`thm:defect-group-1-cocycle`)**：设 $P$ 为有限依赖偏序集，$G(P)$ 为其线性扩展图（顶点为线性扩展/脊髓历史 $\gamma$，有向边 $e:\gamma\to\gamma'$ 为相邻不可比元素 $x,y$ 的一次换序）。则：
      1. **精确可乘/可加性（Telescoping）**：定义有向边上的群值局部缺陷 $\delta(\gamma\to\gamma') := \rho(\gamma')\rho(\gamma)^{-1}$（及标量值局部缺陷 $\Delta_a(\gamma\to\gamma'):=\nu_a(\gamma)-\nu_a(\gamma')$）。对 $G(P)$ 上任意路径 $\gamma_0\to\gamma_1\to\cdots\to\gamma_m$，总缺陷精确分解为
         $$\rho(\gamma_m)\rho(\gamma_0)^{-1} = \delta(\gamma_{m-1}\to\gamma_m)\cdots\delta(\gamma_0\to\gamma_1), \qquad \nu_a(\gamma_0)-\nu_a(\gamma_m)=\sum_{i=1}^m \Delta_a(\gamma_{i-1}\to\gamma_i),$$
         只依赖端点而与路径无关（注：如 `note 25` §7 所澄清，在未加规范限制的全局顶点赋值下，它是全局 0-上链 $\rho(\gamma)$ 的群值余边界，故自动闭合）；
      2. **局部缺陷的后缀共轭结构**：在历史词 $\gamma = UxyW$（$U$ 先执行、$W$ 后执行）中交换相邻不可比元 $x,y$ 至 $\gamma'=UyxW$，局部群值缺陷不是裸交换子，而是**被后缀 $\rho(W)$ 共轭的交换子**：
         $$\delta(UxyW\to UyxW) = \rho(W)\,\bigl[\rho(x),\rho(y)\bigr]\,\rho(W)^{-1}, \qquad [g,h]:=ghg^{-1}h^{-1};$$
      3. **BCH 展开与三元 Hexagon 的 Jacobi 闭性**：当生成元对应无穷小向量场 $e^{hX}, e^{kY}, e^{lZ}$ 时，$[e^{hX},e^{kY}]=\exp(hk[X,Y]+\frac{h^2k}{2}[X,[X,Y]]+\frac{hk^2}{2}[Y,[X,Y]]+\cdots)$；三元反链 $\{X,Y,Z\}$ 生成的六边形（permutahedron 2-胞腔）两条三步交换路径的无穷小三阶差恰由 **Jacobi 恒等式** $[X,[Y,Z]]+[Y,[Z,X]]+[Z,[X,Y]]=0$（离散 Bianchi 恒等式 $d\Omega=0$）消去。
  * **5.4 全息 Stokes 定理与体-表面积分读法（源自 `19` §§1–5）**：
    * **Proposition 5.5 (`prop:holographic-stokes-minimal`)**：在最小分支 DAG $\{A,M\}$ 的接触实现中，体（电荷矩形 $\Sigma=[0,h]\times[0,k]$）上的曲率 2-形式 $d\alpha = -\lambda\,da\wedge dv = d(-\lambda a\,dv)$ 非零但**恰当（exact）**；由 Stokes 定理，体的曲率积分化归为边界闭回路 $\partial\Sigma$ 上的势 1-形式线积分（holonomy）：
      $$T = \int_\Sigma d\alpha = \oint_{\partial\Sigma}(-\lambda a\,dv).$$
    * **Remark 5.6 (`rem:scott-preserves-ideal-surface`，标记为 `STRUCTURAL PROPOSAL`）**：在完备化轴上，有限 DAG（紧致元）构成平坦的“体（bulk）”，无限历史 $\Gamma^\omega$ 构成“理想表面（surface）”。Scott 拓扑将无限历史保留为真极限（使曲率作为表面 holonomy 存在），而 Alexandrov 拓扑将无限历史物化为孤立点从而抹平体-表面区分。同时登记任意偏序集 $P$ 上的宏观离散 Stokes 积分与谱对接为开放问题 **OQ-095.3 / OQ-095.4**。

### Section 6. Analytical Pillar III — Series Theory: Free Lie Algebra Magnus Expansion, Arity–Cell Correspondence, and Abelianization
* **目标文件**：新建 `paper-1/sections/06-series-theory.tex`，融合 `notes/analysis-and-calculus/21`、`22`、`23` 及 `24`。
* **小节与定理槽位设计**：
  * **6.1 算术历史的 Magnus 级数与自由李代数空间（源自 `21` §§1–2）**：
    * **Definition 6.1 (`def:history-magnus-series`)**：对由无穷小生成元 $X_1,\dots,X_n$ 构成的时序历史词 $\gamma=(e^{X_1},\dots,e^{X_n})$，其求值算子 $\rho(\gamma)=e^{X_n}\cdots e^{X_1}$ 的形式对数定义为自由李代数 $\operatorname{Lie}(X_1,\dots,X_n)$（完备化）中的 **Magnus 级数**：
      $$\Omega(\gamma) = \log\bigl(e^{X_n}\cdots e^{X_1}\bigr) = \underbrace{\sum_{i=1}^n X_i}_{\Omega_1\text{（1 阶：阿贝尔电荷）}} + \underbrace{\frac{1}{2}\sum_{1\le i<j\le n}[X_j,X_i]}_{\Omega_2\text{（2 阶：交换子/曲率）}} + \underbrace{\frac{1}{12}\sum_{i,j,k}\bigl(2[X_i,[X_j,X_k]]+\cdots\bigr)}_{\Omega_3\text{（3 阶：嵌套括号）}} + \cdots$$
  * **6.2 “元数（Arity）$\leftrightarrow$ 胞腔（Cell）”对应与高维 DAG 完备性（源自 `21` §§3–5，OQ-095.1 & OQ-095.2）**：
    * **Proposition 6.2 (`prop:arity-cell-correspondence-low-order`，低阶已核验 + 一般阶 `STRUCTURAL PROPOSAL`）**：将 Magnus 级数 $\Omega(\gamma)$ 的李括号项按所含**互异生成元的个数（元数 $\mathrm{arity}=k$）**与**重复生成元自嵌套**分解：
      1. **低阶精确对应（1–3 阶）**：
         * $\mathrm{arity}=1$（生成元 $X_i$）$\longleftrightarrow$ $\mathcal{O}(P)$ 的 0-胞腔（单点 / 标量电荷）；
         * $\mathrm{arity}=2$（互异交换子 $[X_i,X_j]$）$\longleftrightarrow$ $\mathcal{O}(P)$ 的 1-胞腔（二元反链菱形 $B_2$，系数即接触曲率 $\mu\lambda$）；
         * $\mathrm{arity}=3$（三元互异嵌套括号 $[X,[Y,Z]], [Y,[Z,X]]$）$\longleftrightarrow$ $\mathcal{O}(P)$ 的 2-胞腔（三元反链立方体 $B_3$；在阶 3 自由幂零李代数矩阵模型 $X=E_{12}, Y=E_{23}, Z=E_{34}$ 下，已由符号计算核验 $\log(e^{hX}e^{kY}e^{lZ})$ 的 $E_{14}$ 项系数恰为 $\frac{1}{3}hkl\,[X,[Y,Z]]$）；
         * 重复下标项（如 $[X,[X,Y]]$，系数 $\frac{1}{2}h^2k$）不对应新反链胞腔，而是单个流 $e^{hX}$ 非线性性的高阶自修正；
      2. **为什么级数理论只能在完整 DAG 上完备**：二维接触分布 $\mathcal{D}=\operatorname{span}\{D_u,D_v\}$ 仅有 2 个生成方向，其自由李代数 $\operatorname{Lie}(D_u,D_v)$ 中互异生成元元数恒满足 $\mathrm{arity}\le 2$（一切 3 阶以上括号均为重复下标自嵌套）；唯有在具有 $n$ 个互不可比运算的一般分支 DAG $P$ 上，$\operatorname{Lie}(X_1,\dots,X_n)$ 才具备 $\mathrm{arity}=3,\dots,n$ 的互异高阶括号，完整编码 $\mathcal{O}(P)$ 的高维胞腔缺陷。
      3. **开放问题边界（OQ-095.1 / OQ-095.2）**：一般阶 $\mathrm{arity}\text{-}k$ 定位定理（证明 $\mathrm{arity}\text{-}k$ 互异项仅由 $k$ 元反链缺陷贡献）及全 DAG 李实现函子 $F:\mathrm{FinDAG}\to\operatorname{Lie}(g_1,\dots,g_n)$ 明确列为开放问题。
  * **6.3 级数的三重体-表面全息简化（源自 `21` §6）**：
    * **Proposition 6.3 (`prop:bulk-boundary-series-reduction`)**：体上的 Magnus 级数向表面（边界）投影时发生三重结构简化：
      1. **微分形式降次（Degree Descent）**：体上的 2-形式曲率载体 $d\alpha$（对应 $\mathrm{arity}=2$ 括号）在表面降为一阶势 1-形式 $-\lambda a\,dv$（Stokes 积分降一阶）；
      2. **上闭链约化（Cocycle Reduction）**：由 Theorem 5.4 的 1-上闭链闭性，体内部相邻胞腔的高阶展开项在沿闭合边界求缺陷时成对抵消，表面只保留上同调闭类；
      3. **规范形约化（Canonical Form）**：体上的 Magnus 级数依赖生成元排列与 Hall/Lyndon 基选择（非规范），而在理想边界 $\Gamma^\omega$ 上求值化为无限 Möbius 乘积 = **连分数展开**（具有唯一部分商序列的规范形）。
  * **6.4 PBW 阿贝尔化、差分代换与非退化条件的代数-分析对偶（源自 `22`–`24`）**：
    * **Theorem 6.4 (`thm:pbw-abelianization-difference-substitution`)**：记自由李代数 $\mathfrak{L}=\operatorname{Lie}(X_1,\dots,X_n)$，其泛包络代数 $U(\mathfrak{L})\cong T(X_1,\dots,X_n)$ 的滤过相关分次代数为对称代数 $\operatorname{gr}(U(\mathfrak{L}))\cong S(X_1,\dots,X_n)$（PBW 定理）。当令所有李括号为零（阿贝尔化，即 AEG 中接触曲率/缺陷 $\mu\lambda=0$）时：
      1. 李字基（Hall/Lyndon 基）退化为交换单项式基 $d_1^{\alpha_1}\cdots d_n^{\alpha_n}$；
      2. 非交换 Magnus 级数 $\log(e^{X_1}\cdots e^{X_j})$ 退化为阿贝尔累积和 $x_j = d_1+\cdots+d_j$——这在代数结构上精确同构于杨路（Yang Lu）不等式机器证明中的**差分代换与单项式展开**（在全 $n!$ 线性扩展锥上检验系数非负性 vs 在非交换层提取 Magnus 缺陷系数）。
    * **Remark 6.5 (`rem:wu-zhang-nondegeneracy-correspondence`，标记为 `STRUCTURAL PROPOSAL`）**：总结跨项目结构对表（`22`, `24`）：吴文俊消元法的伪除法（以乘代除，将奇点推至初式 $\operatorname{lc}\neq 0$ 的非退化边界）与张景中面积法的弱非退化改进，在结构上对应 AEG 用半直积分配律重标定 $D_k\circ T_s = T_{ks}\circ D_k$（无缺陷）替代朴素换序 $T_s\circ D_k$（有缺陷 $\mu\lambda$），同时诚实声明两者的退化机制不同（$\operatorname{lc}=0$ 为乘法不可逆 vs $\mu\lambda=0$ 为水平分布可积）、数学载体不同（多项式环 vs 仿射流）。

### Section 7. Geometric Characterization I — Taxonomy of Holes, Essential Punctures, and Regular Zero Rigidity
* **目标文件**：重构并扩充原 `paper-1/sections/05-zero-geometry.tex` 为 `07-holes-and-zero-geometry.tex`，融合 `notes/analysis-and-calculus/25` §§1.3, 3.3、`notes/foundations-and-geometry/06-hole-obstructions-ledger.md` 及 `paper-0/sections/11-holed-aes.tex`。
* **小节与定理槽位设计**：
  * **7.1 “孔（Holes）”的五重严格分类谱系与四类边界（源自 `25` §1.3、`Paper 0` §11.6、`Paper IV` §5b）**：
    * **Definition 7.1 (`def:fivefold-hole-taxonomy`)**：在 AEG 体系中严格区分以下五类不可混同的“孔”对象：
      1. **语法单孔（Syntactic One-Hole Placeholder）**：一维上下文 $C_{\omega,c}^{(\varepsilon)}[z]$ 中的形式占位符 $z$；
      2. **计算端口孔（Computational Port / Wire Hole）**：严格有限有向无环网络 $P:A\rightsquigarrow B$ 中等待代换绑定 $\operatorname{Subst}_\beta(P;\boldsymbol{q})$ 的有序带类型输入/输出出现（occurrence），受 `discard(1/0)` 等严格偏定义域约束；
      3. **拓扑表面孔口与接缝圆周（Topological Surface Hole / Seam Circle）**：三维厚化柄体 $H_G$ 的外露侧表面 $S_G = \partial H_G\setminus\bigcup_{D\in E_G}\operatorname{int}(D)$ 上删去外部端口圆盘留下的边界圈，或沿内部管道切开时暴露的接缝圆周 $C_e=\partial D_e$；
      4. **几何本质穿孔与奇异集（Essential Geometric Puncture / Singular Set）**：流形 $\overline{M}$ 上使正则 AES 数据 $(g,a;\mu,\lambda)$ 无法局部光滑非退化延拓的闭无处稠密子集 $S\subset\overline{M}$；
      5. **组合交互孔（Combinatorial Interaction Site）**：多分量耦合系统中承载双向交换与标架/相位单值群扭转的通道位置（如 `Paper 0` §11.5 六项计算见证中的 $K_3$ 边与 $\mathbb{Z}_3\times\mathbb{Z}_4\cong\mathbb{Z}_{12}$ 相位扭转）。
    * **Convention 7.2 (`conv:four-boundaries-distinction`)**：严格区分四种“边界”：（a）**计算前沿（Computational Frontier）**：依赖偏序下集 $U\in\mathcal{O}(P)$ 与未完成事件之间切开的内部有向 wires 集合；（b）**几何边界（Geometric Boundary）**：厚化体边界 $\partial H_G = S_G\cup\bigcup_{D\in E_G}D$；（c）**积分链边界（Integration Boundary）**：Stokes 公式 $\int_\Sigma d\alpha = \int_{\partial\Sigma}\beta$ 中的定向 1-链 $\partial\Sigma$；（d）**完备化极限边界（Completion Boundary）**：理想完备 $\operatorname{Idl}(\mathrm{FinDAG})$ 中的无限历史 $\Gamma^\omega$。
  * **7.2 正则 AES 的零点轨迹刚性与完全分裂禁戒定理（保留原 §5.1–§5.2，`PROVED`）**：
    * **Theorem 7.3 (`thm:regular-zero-locus`)** 与 **Corollary 7.4 (`cor:regular-zero-rigidity`)**：因 $|\nabla a|_g^2 = \mu^2+\lambda^2 a^2\ge\mu^2>0$，正则 AES 内部零点集 $Z(a)=a^{-1}(0)$ 是光滑嵌入余维 1 子流形，局部无孤立点、无交叉点、无分支点、无端点。
    * **Theorem 7.5 (`thm:complete-regular-aes-splitting`)**：若正则 AES $(M,g,a;\mu,\lambda)$ 连通、无边界且黎曼完备，则单位梯度流整流变换 $r=\mathcal{R}\circ a = \int_0^a (\mu^2+\lambda^2 s^2)^{-1/2}ds$ 给出全局微分同胚 $F:Z(a)\times\mathbb{R}\xrightarrow{\sim} M$；故 $Z(a)$ 非空连通、$M$ 非紧，**在连通完备无边界正则标量 AES 范畴内严格禁戒多连通分支零集或四价 Hecke 分支零网（Global No-Go Theorem）**。
  * **7.3 奇异 AES 定义与两类本质穿孔机制的精细刻画（扩充原 §5.3–§5.4，对接 `Paper 0` §§11–12）**：
    * 保留 **Definition 7.6 (`def:singular-aes`)**（闭无处稠密奇异集 $S$、正则轨迹 $M\setminus S$、局部本质性）与正则/奇异零点分解 $Z_{\mathrm{reg}}(a), Z_{\mathrm{sing}}(a)$。
    * **Theorem 7.7 (`thm:two-essential-puncture-mechanisms`)**：对比并精细刻画两类已验证的本质穿孔（孔）机制：
      1. **第一类：度量光滑延拓而赋值非 $C^1$ 的孤立零点穿孔（`prop:isolated-zero-singular-model`，模型 $\mathfrak{E}_1$）**：单位圆盘 $\mathbb{D}$ 配备完备 Poincaré 度量 $g_{\mathbb{D}}=\frac{4}{\lambda^2(1-\rho^2)^2}(d\xi^2+d\eta^2)$ 与径向赋值 $a_{\mathbb{D}}=\frac{2\mu}{\lambda}\frac{\rho}{1-\rho^2}$；度量在原点光滑非退化延拓，但 $a_{\mathbb{D}}$ 在原点仅连续而非 $C^1$（方向导数双侧极限为 $\pm 2\mu/\lambda$），故 $S=\{0\}$ 本质，$Z_{\mathrm{reg}}=\varnothing, Z_{\mathrm{sing}}=\{0\}$，且穿孔圆盘 $\mathbb{D}\setminus\{0\}$ 度量不完备（穿孔在有限距离处）。
      2. **第二类：赋值光滑延拓而共形背景度量退化的临界穿孔（导入并对接 `Paper 0` `thm:p0-punctures-are-critical`, `thm:p0-four-circle-model`, `thm:p0-arbitrary-k-punctures`）**：当 $a$ 光滑延拓为 $\overline{M}$ 上的 $\widetilde{a}$，且 $g$ 在 $U\setminus S$ 上共形于 $\overline{M}$ 上的光滑非退化背景度量 $g_0$ 时，本质穿孔集精确由临界点集决定：
         $$S = \operatorname{Crit}(\widetilde{a}) = \{p\in\overline{M} : d\widetilde{a}(p)=0\}, \qquad g = \frac{|d\widetilde{a}|_{g_0}^2}{\mu^2+\lambda^2\widetilde{a}^2}\,g_0.$$
         （同时注明 `notes/foundations-and-geometry/10` C-10 的反例警示：若无“延拓共形背景 $g_0$”假设，仅靠 $a$ 光滑延拓只能推出 $\operatorname{Crit}(\widetilde{a})\subseteq S$，如 $a=x, g=dx^2+(x^2+y^2)^{-1}dy^2$ 在原点 $da\neq 0$ 但度量奇异）。在四圆多项式 $P=S_2^4-4\rho^2 S_2^3+16\rho^4 x^2y^2$ 模型中，原点处切锥为重数 2 的坐标轴并 $(xy)^2=0$，零点轨迹呈 4 圆 8 分支交汇于穿孔，共形因子以 $O(|x|^{10})$ 退化使穿孔处于有限距离。
  * **7.4 光滑参数族的总零点集与适定性（Properness）边界（保留原 §5.5，`prop:regular-total-zero-set` & `rem:zero-family-properness`）**：空间正则假设 $d_p a_t\neq 0$ 保证总零点集 $\mathcal{Z}=A^{-1}(0)\subset M\times I$ 为光滑超曲面且投影 $\pi:\mathcal{Z}\to I$ 为淹没（submersion），但唯有附加**适定性（properness）**假设才能升级为局部平凡零点管（zero tube）。

### Section 8. Geometric Characterization II — Theory of Caps: Ball-and-Tube Thickening, Hole–Disk Complementarity, Capping Obstructions, and Certified Sealing
* **目标文件**：新建 `paper-1/sections/08-caps-and-interface-disks.tex`，全面整合 `notes/analysis-and-calculus/25-pants-interface-disks-and-substitution.md`、`research/pants-interface-disks/`（V1）、`paper-0/sections/12-compactification.tex` 及 `paper-4/sections/05b-ported-aes-programs.tex`（OQ-096）。
* **小节与定理槽位设计**：
  * **8.1 带装饰 DAG 的三维球-管厚化模型与局部 Pants 分解（源自 `25` §2）**：
    * **Definition 8.1 (`def:decorated-ball-tube-thickening`)**：对有限严格有向无环网络 $G$（保留有序带类型外部输入/输出、每个 gate 的有序槽位与偏函数、不可变 source、独立 occurrence、显式 copy/discard 及绑定记录），构造指定三维厚化体 $H_G$：为每个 gate $v$ 选定向三维球 $B_v$ 及边界上互不相交的参数化端口圆盘；为每条内部 wire $e$ 选管道 $T_e = D^2\times[0,1]$ 按定向相容贴合；外露端口圆盘族记为 $E_G$，观察侧表面定义为
      $$S_G := \partial H_G \setminus \bigcup_{D\in E_G}\operatorname{int}(D).$$
    * **Proposition 8.2 (`prop:local-pants-handlebody-genus`，Note 25 命题 A，`PROVED WITH STATED HYPOTHESES`）**：
      1. 总端口数为 3 的 gate（如二元运算 `2->1` 或显式复制 `1->2`），其球面删去三个开端口圆盘后同胚于 **pair of pants**（三孔球面，$\chi=-1, b=3$）；总端口数为 2 对应圆柱，为 1 对应圆盘；
      2. 对连通网络 $G$（底层无向多重图为 $|G|$，保留重数），$H_G$ 是三维柄体（handlebody），其亏格（柄数）与侧表面欧拉示性数满足精确公式（无隐藏柄条件）：
         $$g(H_G) = \beta_1(|G|), \qquad \chi(S_G) = 2 - 2\beta_1(|G|) - b,$$
         其中 $b=|E_G|$ 为外部端口总数（校准例：两二元节点串接 $\beta_1=0,b=4\implies \chi=-2$；一次 copy 经两分支再合并 $\beta_1=1,b=2\implies \chi=-2$）。
  * **8.2 内部接口圆盘、Pants 拼接与“孔—盘（表面—体）互补定理”（源自 `25` §3 & §8.1 V1）**：
    * **Proposition 8.3 (`prop:pants-gluing-interface-disk`，Note 25 命题 B，`PROVED WITH STATED HYPOTHESES`）**：设两个三端口 gate 球 $B_1,B_2$ 沿一条内部管道 $T_e$ 连接，取中部截面圆盘 $D_e = D^2\times\{1/2\}$ 及其边缘圆周 $C_e = \partial D_e\subset S_G$。沿 $D_e$ 切开并将半管道吸收进两侧 collar 后，两体仍为三维球，外露侧表面分别为 pants $P_1, P_2$；重新拼接在体与侧表面上分别表示为：
      $$H_G \cong B_1 \cup_{D_e} B_2 \cong B^3, \qquad S_G \cong P_1 \cup_{C_e} P_2, \qquad \partial D_e = C_e.$$
    * **Theorem 8.4 (`thm:hole-disk-complementarity`，孔—盘互补与盖子的第一层几何意义）**：在两个三端口节点拼接的四孔侧表面 $S_G$ 与三维柄体 $H_G$ 中，共享圆周 $C_e$ 与截面圆盘 $D_e$ 满足严格互补关系：
      1. **表面不可填性（孔）**：在侧表面 $S_G$ 中，$C_e$ 两侧均为含外部孔口的 pants，故 $C_e$ 不在 $S_G$ 内围出圆盘，且在模 2 同调中非平凡：
         $$[C_e] \neq 0 \in H_1(S_G;\mathbb{F}_2);$$
      2. **体内可填性（盘/盖）**：在包含映射 $i:S_G\hookrightarrow H_G$ 下，$C_e$ 由体内显式接口圆盘 $D_e\subset H_G$ 填充（$\partial D_e = C_e$），故
         $$i_*[C_e] = 0 \in H_1(H_G;\mathbb{F}_2);$$
      3. **切开暴露为盖子**：当沿 $D_e$ 切开计算体 $H_G$ 时，单一内部接口圆盘 $D_e$ 分裂为生产侧输出端与消费侧输入端上带有相反边界定向的两个圆盘副本 $D_e^+, D_e^-$，各自作为封住两侧 pants 开口的**盖子（Caps）**。这精确落实了“**表面给孔以意义，体给盘以意义；两者由带方向的共同边缘 $C_e=\partial D_e$ 联系**”（已在 V1 的 56 立方体、336 四面体有限胞腔复形上完全核验：侧表面边界矩阵秩 $110$，加入 $C_e$ 后秩升为 $111$）。
    * **Remark 8.5 (`rem:downset-frontier-disks`)**：将 §2.8 的下集格 $\mathcal{O}(P)$ 与本节连接：对依赖偏序 $P$ 的任一下集 $U\in\mathcal{O}(P)$，切开所有从 $U$ 指向 $P\setminus U$ 的内部管道 $T_e$，即得到一组代表当前计算前沿（computational frontier）的接口圆盘族 $\{D_e\}_{e\in\partial^+ U}$。
  * **8.3 接口状态、代数代换、谱值与过程残余保留（源自 `25` §4、`Paper IV` §5b、`Paper 0` §12.5）**：
    * 导入 `Paper IV` 严格有限网络代换相容性定理 `thm:ported-substitution-evaluation`（$D_{P\circ Q}=\{(x,z):x\in D_Q, (\operatorname{Eval}(Q)(x),z)\in D_P\}$，$\operatorname{Eval}(P\circ Q)(x,z)=\operatorname{Eval}(P)(\operatorname{Eval}(Q)(x),z)$）。
    * **Proposition 8.6 (`prop:polynomial-interface-spectrum`)**：在有理多项式片段（如 $Q_+:z=x+y$ 与 $P_\times:w=zt$ 沿接口圆盘 $D_z$ 拼接为 $w=(x+y)t$）中，接口可观测量代数 $A_z=\mathbb{Q}[z]$ 上的代换诱导代数同态 $s^*:A_z\to\mathbb{Q}[x,y],\ z\mapsto x+y$；给定输入 $(r,s)$，评价特征标满足 $\chi_{r,s}\circ s^* = \chi_{r+s}$，接口圆盘上的“谱值”定义为评价字符值 $\chi_c(z)=c$（对应 $\operatorname{Spec}\mathbb{Q}[z]$ 的有理点 $(z-c)$），而关系拼接对应商环张量积（概形纤维积）：
      $$\mathbb{Q}[x,y,z]/(z-x-y)\ \otimes_{\mathbb{Q}[z]}\ \mathbb{Q}[z,t,w]/(w-zt) \;\cong\; \mathbb{Q}[x,y,t,w]/(w-(x+y)t).$$
      （同时声明：$\operatorname{Spec} A_z$ 是状态参数空间，不等同于几何圆周 $C_z$ 或 $\mathcal{O}(P)$ 的 Stone 序谱）。
    * **Definition 8.7 (`def:interface-record-with-residual`)**：为防止数值相等抹杀过程历史（如 $2+3=5$ 与 $1+4=5$ 在接口圆盘上具有相同数值 $\sigma_e=5$ 但来源与历史不同，或 `Paper 0` `prop:p0-k4-motion-residue` 中四步词 $W_{s,t}=M_{-t}\circ A_{-e^t s}\circ M_t\circ A_s$ 保持赋值 $a\circ W_{s,t}=a$ 却在 $p=(0,1)$ 产生非零切向水平集位移 $\partial_s\partial_t W_{s,t}(p)|_{0,0}=([X_u,X_v]-X_u)(p)=(-3/4,0)\neq 0$），接口圆盘记录必须定义为五元组：
      $$\mathcal{I}_e = (D_e, C_e;\ \sigma_e,\ r_e,\ \beta_e),$$
      其中 $\sigma_e$ 为声明观察层下的接口状态，$r_e$ 为可重开恢复的生产过程残余（及切向几何残余），$\beta_e$ 为端口绑定凭证。
  * **8.4 正则 AES 封盖的直接障碍定理与四重封合判据（源自 `25` §§5–6、`Paper 0` §12.3）**：
    * **Theorem 8.8 (`thm:constant-boundary-capping-obstruction`，Note 25 命题 C，`PROVED WITH STATED HYPOTHESES`）**：设 $D$ 为紧致光滑二维圆盘，$g$ 为 $D$ 上的光滑黎曼度量，$a\in C^\infty(D,\mathbb{R})$，且 $\mu\neq 0, \lambda\in\mathbb{R}$。则**不存在**在 $\operatorname{int}(D)$ 上满足正则 AES 程函方程 $|da|_g^2 = \mu^2+\lambda^2 a^2$ 且在边界 $\partial D$ 上取常数值 $a|_{\partial D}=c$ 的光滑数据 $(g,a)$。
      * *证明核心*：因 $\mu^2+\lambda^2 a^2\ge\mu^2>0$，内部处处 $da\neq 0$；若 $a$ 非常数，紧圆盘 $D$ 上必在内部取得全局极大或极小值，该处 $da=0$，矛盾；若 $a$ 为常数，内部处处 $da=0$，亦矛盾。$\square$
    * **Corollary 8.9 (`cor:capping-dichotomy`)**：
      1. 带有数值标签 $\sigma_e=c$ 的体内接口圆盘 $D_e$ **绝不能**被直接实现为边界赋值为常值 $a|_{C_e}=c$ 的紧致正则 AES 圆盘补片；
      2. 若要在几何上封住一条等值圈 $a|_{\partial D}=c$，必须允许内部出现赋值临界点/非 $C^1$ 奇点（即进入 §7.3 的奇异/穿孔 AES 范畴，如 $\mathfrak{E}_1$ 或临界点模型）或度量退化；
      3. 若要在正则 AES 范畴内跨接缝 $C_e$ 拼接，边界上的赋值 $a|_{C_e}$ 必须非常值，且两侧必须满足完整的双侧光滑领口契约（`Paper 0` `def:p0-collar-contract` / `prop:p0-aes-collar-descent`：$\phi_e^* g_2 = g_1,\ a_2\circ\phi_e = a_1$）。
    * **Definition 8.10 (`def:certified-cap-tuple` & 四重封合严格分离）**：将候选“可认证盖子（Certified Cap）”形式化为六元组
      $$\mathcal{C} = (D, C, \sigma, r, w; \mathcal{Q}),$$
      其中 $w$ 为针对明确闭合义务的验证证书，$\mathcal{Q}$ 为声明的观察范围；并建立四重封合判据对照表，严禁将（i）**计算端口代换绑定**、（ii）**三维体拓扑补盘 $\partial D=C$ / 共形填点**、（iii）**正则 AES 领口下降 / 本质奇点消去**与（iv）**Adva `WitnessProofV0::Seal { body }` 见证封合**（检验加性残余 $A=0$、乘性残余 $M=1$ 并保留非零定义域义务）混为一谈。

### Section 9. Conclusions, Claim-Status Ledger, and Downstream Research Interfaces
* **目标文件**：扩写 `paper-1/sections/06-conclusion.tex` 为 `09-conclusion.tex`。
* **核心内容**：
  1. **更新后的全卷逻辑脊柱总结图**：串联“顺序/分支语法 $\to$ 下集格 $\mathcal{O}(P)$ 与 Scott–Lawson 拓扑 $\to$ 微分/积分/级数三支柱 $\to$ 孔的五重分类与盖的互补/障碍定理”。
  2. **权威数学状态台账（Claim-Status Register）**：严格按 `governance/05-mathematical-status.md` 标注每项结果的等级（见第 4 节总表）。
  3. **下游论文接口与开放问题清单（OQ-095 & OQ-096）**：
     * 移交 `Paper II`：水平度量、算术全纯性、扭曲调和算子 $\mathcal{H}_{\mathrm{tw}} = \Delta_H + i\mu\lambda\partial_a$ vs 变分算子 $\mathcal{L}_{\mathrm{var}} = -(D_u^2+D_v^2+\lambda D_v)$、Appell 模与双曲理想边界 Poisson–Dirichlet 定理（`notes/analysis-and-calculus/01`）。
     * 移交 `Paper III`：多零点奇异管、参数判别式、Hecke 主模 dessin 与周期轨道纽结。
     * 移交 `Paper IV`：双赋值、射影凝聚商塔、特征因子化与在线残差复杂度。
     * 移交未来阶提升理论（`notes/analysis-and-calculus/04`–`08`）：Hyperoperation 线性化塔（Rank $\ge 3$ 临界指数模型、迭代对数、Witt 代数、Schwarzian 导数与 transseries）及测量体系内生坐标。

### Appendices A–D（附录规划）
* **Appendix A (`app-A-conventions.tex`)**：保留时序拼接 $\gamma\delta$、左乘列向量 Möbius 作用、反同态 $\rho(\gamma\delta)=\rho(\delta)\rho(\gamma)$、ACS 直接路径与反向路径定向约定，并补充值格 $L=[0,\infty]$ 上 $T_s, D_k, \neg$ 的矩阵与序作用核对表（含 $D_{-1}=T_1\neg T_{-1}\neg T_1\neg$ 的逐步验证）。
* **Appendix B (`app-B-equality-neutrality.tex`)**：保留六层相等性分离实例，并补充同值不同生产过程（$2+3$ vs $1+4$）在纯数值观察与来源观察下的分离实例（对应 OQ-096 V2）。
* **Appendix C (`app-C-magnus-sympy-verification.tex`，新增）**：记录 `notes/analysis-and-calculus/21` §4 的阶 3 幂零李代数矩阵模型（$X=E_{12}, Y=E_{23}, Z=E_{34}\in\mathfrak{n}_4$）下 $\log(e^{hX}e^{kY}e^{lZ})$ 的符号展开完整推导，展示 1 阶电荷项 $(h,k,l)$、2 阶菱形项 $(\frac{1}{2}hk,\frac{1}{2}kl)$、重复自嵌套项与 3 阶三元反链项 $\frac{1}{3}hkl[X,[Y,Z]]$，以及 PBW 阿贝尔化向差分代换累积和的退化核对。
* **Appendix D (`app-D-pants-cellulation-verification.tex`，新增）**：记录 `notes/analysis-and-calculus/25` §8 与 `research/pants-interface-disks/` 的 V1–V4 验证规程与 V1 精确数值结果（两个实体盒 $[0,3]^3, [5,8]\times[0,3]^2$ 与连接管 $[3,5]\times[1,2]^2$，56 个立方体、336 个四面体、132 个顶点 link 检查、侧表面 $(V,E,F)=(116,228,110),\ \chi=-2$、模 2 边界矩阵秩 $110\to 111$ 证明 $[C]\neq 0\in H_1(S;\mathbb{F}_2)$ 而 $C=\partial D$ 在 $H$ 中成立，以及 10 项负对照拒绝清单）。

## 4. 新增与扩充命题的数学状态与来源对表（Integration Audit Matrix）

根据 `AGENTS.md` 与 `governance/05-mathematical-status.md` 的严格纪律，任何从 `notes/analysis-and-calculus/` 进入 `paper-1` 的命题必须保持诚实的状态标签，严禁将结构性提议（`STRUCTURAL PROPOSAL`）或单个有限计算实例（`COMPUTATIONALLY VERIFIED EXAMPLE`）夸大为一般定理：

| 章节位置 | 命题/对象名称 | 原始笔记来源 | 当前数学状态（Grade） | 进入 `Paper I` 的集成审计要求（Integration Audit） |
| :--- | :--- | :--- | :--- | :--- |
| **§2.6** | 顺序历史前缀序与理想完备 $\operatorname{Idl}(\Gamma^*)\cong\Gamma^{\le\omega}$ | `09` §8 | `CLASSICAL` + `REFORMULATION` | 对齐 `def:marked-spinal-history` 的有界与自由历史记号 |
| **§2.7–2.8** | 分支 DAG 下集序 dcpo $\operatorname{Idl}(\mathrm{FinDAG})$ 与 Birkhoff 下集格 $\mathcal{O}(P)$ | `15` §§1–6 | `CLASSICAL` + `WORKING-NOTE PROVED` | 补齐运算标签、常量与槽位装饰在下集嵌入 $P\sqsubseteq Q$ 下的保持声明（`15` §7 残余 1） |
| **§3.7–3.8** | 生成元域论角色、四层仿射层级与交换方阵 $\Phi(\sigma\vee\neg_*\sigma)=\langle\Phi(\sigma),\neg\rangle$ | `09` §9, `10`–`13` | `WORKING-NOTE PROVED`（核心）+ `STRUCTURAL PROPOSAL`（读法） | 严格写明载体为半群 $\operatorname{Aff}^+$ 而非全 $B_\infty$，并写入非全 Galois 等价的三条反例证明 |
| **§3.9** | $\rho$ 单调性阻碍定理（Thm 3.4）与连分数收敛边界 | `14` §§2–4 | `WORKING-NOTE PROVED` + `CLASSICAL` | 直接收录完整四行群论证明与 $\gamma_i=(\neg,T_{a_i})$ 连分数显式核对 |
| **§3.9** | Hecke 历史 Cantor 空间编码端空间 $\operatorname{Ends}(G_4)$ vs 第一类极限集 $\mathbb{P}^1(\mathbb{R})$ | `16` §§1–4 | `CLASSICAL` + `REFORMULATION` | 修正早期“Cantor 极限集”不精确措辞，明确区分象征端边界与几何极限集 |
| **§4.1–4.2** | 极限/光滑化李函子与“接触曲率 $\mu\lambda =$ 最小 DAG $\{A,M\}$ 序缺陷密度” | `17`, `18` | `WORKING-NOTE PROVED`（拼合 `Paper 0` 已证定理与经典李括号） | 明确标注“组合体 $\mathcal{O}(\{A,M\})$ 平坦、曲率来自非交换实现”为精确化阐释 |
| **§4.3** | 权 $n$ 分次水平协变微分 $\nabla^{(n)}f=\delta_H f-nf\,dM$ 与扭曲导子 $D_M$ | `03` §§3–4 | `WORKING-NOTE PROVED` | 统一自然算术单位 $dA=\mu\,du, dM=\lambda\,dv$ 与 `Paper 0` §9 的 $\delta_H$ 记号 |
| **§5.1–5.2** | 连续混合仿射积分 $\mathfrak{M}_a^b[u;v]$、扭曲 Rota–Baxter 与后向伴随 Lawson 双侧配对 | `02`, `03` §5, `09` §§10–11 | `WORKING-NOTE PROVED` | 明确区分绝对时间参数化与右端点滑窗参数化，核对 $p(t)=K(b)\neg(K(t))$ 终端归一化 |
| **§5.3–5.4** | $G(P)$ 上群值 1-上闭链、后缀共轭交换子、Hexagon Jacobi 闭性与全息 Stokes | `19`, `20`, `25` §7 | `WORKING-NOTE PROVED`（1-上闭链与最小 Stokes）+ `STRUCTURAL PROPOSAL`（全息读法） | 必须纳入 `25` §7 的边界说明：全局顶点赋值下 $\delta(\gamma,\gamma')=\rho(\gamma')\rho(\gamma)^{-1}$ 是群值余边界；任意 $P$ 的宏观 Stokes 标为 `OPEN PROBLEM`（OQ-095.3） |
| **§6.1–6.3** | 自由李代数 Magnus 级数、“$\mathrm{arity}\text{-}k \leftrightarrow (k-1)$-胞腔”对应与体-表面简化 | `21` §§1–6 | 低阶 `COMPUTATIONALLY VERIFIED EXAMPLE` + 一般阶 `STRUCTURAL PROPOSAL` / `OPEN PROBLEM` | 1–3 阶写入正文与 Appendix C；$\mathrm{arity}\ge 3$ 的一般定位定理严格标为猜想与 OQ-095.1 |
| **§6.4** | PBW 阿贝尔化 = 杨路差分代换；吴初式/张弱非退化 $\leftrightarrow$ 缺陷 $\mu\lambda$ | `22`, `23`, `24` | `CLASSICAL`（PBW/BCH）+ `STRUCTURAL PROPOSAL`（跨项目对应） | 诚实注明退化机制不同（不可逆 vs 可积）与数学载体不同（多项式环 vs 仿射流） |
| **§7.1–7.4** | 五重孔分类、正则零点刚性、全局分裂禁戒定理、两类本质穿孔机制对照 | `Paper I` §5, `Paper 0` §§11–12, `25` §1.3 | `PROVED`（正则零点/分裂/$\mathfrak{E}_1$/四圆模型） | 明确纳入 `thm:p0-punctures-are-critical` 的“延拓共形背景 $g_0$”前提及 C-10 反例说明 |
| **§8.1–8.3** | 指定球-管厚化（命题 A）、Pants 圆盘拼接（命题 B）、孔—盘互补与 V1 核验 | `25` §§2–4, §8.1 | 有限模型下 `PROVED WITH STATED HYPOTHESES` + V1 `COMPUTATIONALLY VERIFIED EXAMPLE` | 声明球-管厚化是指定的最小规则而非运算元数唯一决定的内在几何；V2–V4 标为未运行/开放 |
| **§8.4** | 常值边界圆盘无正则 AES 封盖定理（命题 C）与四重封合判据 | `25` §§5–6 | `PROVED WITH STATED HYPOTHESES`（命题 C）+ `STRUCTURAL PROPOSAL`（可认证盖子 $\mathcal{C}$） | 严格区分端口数值标签 $\sigma_e=c$ 与常值几何边界赋值 $a|_{C_e}=c$；不得宣称已建立原生 Adva `Seal` 等价桥 |

## 5. 分阶段执行与验证路线图（Execution & Verification Roadmap）

为确保写作与形式化验证同步推进，建议按以下四个阶段实施：

### 阶段一：治理登记与接口锁定（Governance & Interface Lock）
1. **更新笔记储备审计表**：在 `governance/notes-reserve-audit.md` §2.2 中补齐 `21`–`24` 的分级记录（当前 `09`、`10`–`20` 与 `25` 已登记，`04`–`08` 及 `21`–`24` 待补齐审计行），并在 `governance/08-open-questions.md` 中确认 OQ-095（095.1–095.4）与 OQ-096（096.1–096.4）的交叉引用。
2. **选定整合方案（方案 A 或方案 B）**：更新 `governance/02-paper-I-outline.md` 至 Version 2.0，固定上述九章四附录的标签命名规范（Labeling Convention）。
3. **升级 `00-paper-zero-interface.tex`**：将 `Paper 0` 的接触结构、ACS 积分与穿孔/领口契约标签一次性对齐，确保跨卷引用零断链。

### 阶段二：历史层、序拓扑与分析学三支柱撰写（Sections 2–6 & Appendix C）
1. **扩写 §2 与 §3**：在 `02-sequential-histories.tex` 末尾增补 §2.6–§2.8（前缀序、分支 DAG 下集 dcpo、Birkhoff 分配格 $\mathcal{O}(P)$）；在 `03-projective-affine.tex` 增补 §3.7–§3.9（Scott–Lawson 对应、四层仿射层级、交换方阵、$\rho$ 单调性阻碍定理与 Hecke 端空间/极限集修正）。
2. **撰写 §4（微分理论）**：新建 `04-differential-theory.tex`，完成李函子引理、最小分支 DAG $\{A,M\}$ 序缺陷密度 = 接触曲率 $\mu\lambda$ 定理，以及 `03-weighted-contact-calculus.tex` 的权 $n$ 分次协变微分 $\nabla^{(n)}$ 与规范展平。
3. **撰写 §5（积分理论）**：新建 `05-integral-theory.tex`，整合 `02-mixed-affine-integration.tex` 的五重等价命题、对偶权线丛 $\nabla^{(-1)}p=0$ 与 Lawson 双侧伴随配对定理、线性扩展图 $G(P)$ 上的群值 1-上闭链与 Hexagon Jacobi 闭性，以及最小菱形的全息 Stokes 定理。
4. **撰写 §6（级数理论）与 Appendix C**：新建 `06-series-theory.tex` 与 `appendices/app-C-magnus-sympy-verification.tex`，写入自由李代数 Magnus 展开、“$\mathrm{arity}\text{-}k \leftrightarrow (k-1)$-胞腔”低阶定理与高阶猜想、体-表面三重简化机制，以及 PBW 阿贝尔化与杨路差分代换的同构定理。

### 阶段三：孔与盖的精细几何撰写及 V2–V4 实验推进（Sections 7–8 & Appendix D）
1. **重构 §7（孔与零点几何）**：在保留原 §5 全部定理与证明的基础上，增补 §7.1“孔的五重分类谱系与四类边界”及 §7.3“两类本质穿孔机制（赋值非 $C^1$ 型 vs 共形背景度量临界退化型）的精确对照”。
2. **撰写 §8（盖与接口圆盘理论）与 Appendix D**：新建 `08-caps-and-interface-disks.tex` 与 `appendices/app-D-pants-cellulation-verification.tex`，完整写入球-管厚化命题 A、Pants 圆盘拼接命题 B、孔—盘互补定理（含 V1 有限胞腔模 2 同调数据）、多项式接口谱模型、五元组接口残余记录，以及**常值边界圆盘无正则 AES 封盖定理（命题 C）**与四重封合判据。
3. **推进 OQ-096 的 V2–V4 验证脚本（在 `research/pants-interface-disks/` 下扩展）**：
   * **V2（同值不同生产者与残余重开）**：构造 `2+3` 与 `1+4` 接入同一消费端 `w=zt` 的双实例有限复形，验证纯数值观察层下接口均输出 `5`，而在来源观察层下保留的残余 $r_e$ 与 occurrence 凭证严格可分。
   * **V3（三块组合结合律与非法反馈拒绝）**：验证三个兼容 pants 块的两种括号化具有显式装饰同构与相同严格定义域，并自动拒绝含 `discard(1/0)`、类型错配或交叉成环的非法拼接。
   * **V4（AES Collar 与原生 `Seal` 映射接口）**：构造非恒定边界赋值的显式双侧光滑 collar 拼接实例（与命题 C 形成正反对照），并编写与 `WitnessProofV0::Seal { body }`（$A=0, M=1$）的证据保持接口检查器。

### 阶段四：全卷统稿、红队审查与构建闭环（Section 1, Section 9 & Build Audit）
1. **重写 §1（引言）与 §9（结论）**：同步摘要、关键词、导言图与结论逻辑脊柱，确保不出现任何违反 `AGENTS.md` §6 的越界声明。
2. **执行编译与引用检查**：在仓库根目录运行 `./build.sh 1`，检查所有新增 `Theorem`、`Proposition`、`Lemma`、`Definition`、`Remark`、`Warning` 标签及跨卷 `Paper 0` / `Paper IV` 引用无未定义警告（undefined references）。
3. **独立红队数学审查（Red-Team Claim Audit）**：逐条核查 `governance/07-acceptance-checklist.md`，完成从 `WORKING-NOTE PROVED` 到论文正文 `PROVED` 的正式状态晋升登记。
