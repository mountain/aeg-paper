# Paper III 来源审计

**审计日期：** 2026-08-06

**审计的仓库 HEAD：** 24c1df0dd1feb38b691a50a6c6dc7a6aa613248a

**审计的历史数量：** 本地 checkout 中所有 refs 可达的 249 个 commit

**当前手稿：** paper-3/aeg-paper-3.tex 及其显式节与附录输入

**文档状态：** 溯源审计与迁移控制记录；它不取代权威范围或数学状态文件

## 1. 目的与权威

本审计识别与 Arithmetic Expression Geometry III: Singular Zero Geometry and Tubes
相关的数学与历史来源。它记录什么可导入、什么必须重新推导、什么已被取代或拒绝、什么未找到。

本审计所用权威顺序是：

1. AGENTS.md 与显式任务；
2. governance/00-authoritative-scope.md 到 governance/08-open-questions.md；
3. 规范 Paper I 与 Paper II 手稿；
4. 当前 Paper III 手稿，对其在此证明的论断；
5. governance/discussions/ 下的工作讨论；
6. 遗留节、笔记、纽结计算、杂项文件、归档手稿与从 Git 恢复的已删除历史文件。

工作讨论、历史笔记、图或计算不是证明权威。一条论断只有在假设、陈述与证明出现在活跃手稿或由
显式引用从 Papers I 或 II 导入时才在 Paper III 规范。

状态 REDERIVED HERE 在本文件中有精确含义：当前 Paper III 手稿从所述数据给出新定义、构造、
计算或证明。结果可能由历史材料启发，但历史材料不用作证明权威。

## 2. 审计方法与否定历史发现

审计覆盖以下内容的当前内容与 Git 历史：

- paper-1/、paper-2/、paper-3/ 与遗留 sections/；
- notes/、notes/knots-and-loops/、images/sources/、images/ 与 archive/；
- governance/04-current-to-target-map.md、governance/05-mathematical-status.md、
  governance/08-open-questions.md 与两个 Paper III 工作讨论；
- 可达 Git 历史中可发现的已删除跟踪材料。

历史审计枚举本地 checkout 中 `git rev-list --all` 返回的全部 249 个 commit，并在其树中搜索
multi-zero、multiple zero、E_k、E_log、E_{\log}、logarithmic model、tube、singularity、
discriminant、braid、threading、knot、Alexander 与 Burau 的拼写与 TeX 变体。候选命中随后在
上下文中检查，而非仅因术语出现即计为构造。

### 否定发现

无可达 commit 含可验证一般多重零 AEG 构造、已定义一般对象 E_k 或显式 AEG 构造 E_{\log}。
特别是：

- notes/foundations-and-geometry/03-single-zero-diffusion-model.tex 题为「Second Kind AEG-S2」的旧版本与后来在 Paper I 中规范化的同一孤立零 Poincare 盘模型相同；不是多重零模型；
- 遗留 K2/K3 与管节在标签首次出现时为空或标 TODO；
- 后来重组文档作为迁移目标或开放计划重复名称，但不提供缺失公式；
- 2026 工作讨论中的对数叶解释是关于覆盖数据的结构提案，不是显式 AEG 赋值与度量。

这是关于本 checkout 中 249 个可达 commit 树的否定结果。它不排除未提交私有笔记、不可达 Git 对象
或未提供审计的外部仓库。若此类来源后来提供，必须按路径、不可变修订与公式级比较加入本审计。

因此当前 Paper III 手稿中每个显式多重零、对数与螺旋构造是 REDERIVED HERE。无一被呈现为关于
预先存在 E_k 或 E_{\log} 的恢复定理。

## 3. 规范导入接口

| 来源 | 精确位置 | 导入内容 | Paper III 处理 |
|---|---|---|---|
| paper-1/sections/07-zero-geometry.tex | 审计树 14–37 行 | 实赋值的正则零是光滑余一维子流形 | IMPORTED；无孤立、交叉、分支或诞生/死亡事件被称为正则 |
| 同上 | 39–49 行 | 正则内部零处孤立点、交叉、分支与端点的排除 | IMPORTED 作为局部阻碍 |
| 同上 | 101–135 行 | 奇异 AES 数据与正则/奇异零集分解 | IMPORTED；Paper III 中的附加 Whitney 分层是 REDERIVED HERE |
| 同上 | 141–246 行 | 已验证孤立零 Poincare 盘模型 | IMPORTED 作为单个局部示例，非普遍正规形 |
| 同上 | 248–299 行 | 空间横截下光滑总零关联与淹没参数投影 | IMPORTED 并以向量丛语言重新表达 |
| 同上 | 301–311 行 | 无 properness 全局乘积结论失败 | IMPORTED 作为长期警告 |
| 同上 | 313–316 行 | Paper I 无认证多重零模型 | PRESERVED；Paper III 提供新模型 |
| paper-2 活跃手稿 | 完备基本模型上的算术全纯坐标 | 普通全纯多项式根族可在 Paper II 坐标中解释 | 仅 IMPORTED 接口；Paper III 构造的辫族是 REDERIVED HERE |
| governance/00-authoritative-scope.md | 392–508 与 758–852 行 | 模型审计、族零集极限与纽结定理门禁 | AUTHORITATIVE 约束 |
| governance/01-paper-series-architecture.md | 1079–1123 与 1512–1527 行 | 规范记号与八部分 Paper III 序 | AUTHORITATIVE 结构 |
| governance/04-current-to-target-map.md | 1509–1653 行 | 重证多重零公式；区分七个零/管/纽结层；保持纽结断言 | AUTHORITATIVE 迁移规则 |
| governance/05-mathematical-status.md | 1410–1564 与 2210–2398 行 | 真淹没边界与开放判别式、单值、穿线与不变量问题 | AUTHORITATIVE，除下文修正的无支持 E_k 与 E_{\log} 溯源标签 |
| governance/08-open-questions.md | OQ-012、OQ-019–021、OQ-037–046 | 拒绝数值模型命名；要求 properness、嵌入移动点、避碰、环境同痕与 Markov 下降 | AUTHORITATIVE 开放问题边界 |

## 4. 历史管时间线

| 日期 | 不可变来源 | 历史内容 | 现处置 |
|---|---|---|---|
| 2023-01-03 | commit 4272d61aed28cfaedb66fca42b45395808f5ff25，aeg-paper.tex，历史 842–854 行 | 「第一类管结构：TODO」与后来保留为 images/13-tube1st.png 的图像 | MOTIVATION ONLY；无定义或证明 |
| 2023-11-09 文档日期；首次跟踪 2025-03-01 | blob f0edf2dc6d293a7ebca2d4b9b722be2b62e68679 于 gpt/2023-11-09_023605_Meeting_Minutes_Arithmetic_Expression_Geometry.tex，commit 97d5c2248e7bc14e1f64272e8285c79797f3cbac 引入 | K3 切片、轨迹 P(e^\lambda)、提议一致化与由同余坍缩零线 | HISTORICAL MOTIVATION；拓扑、同余、零关联关系与 properness 未定义 |
| 2025-04-30 | commit 61cba1358f305b956dfe92705883d87516499063；现 archive/paper4p/aeg.tex，593–632 行 | T 作为 AES 切片的不交并、基/纤维语言、提议截面与 a=-x/y 的常零线 x=0 | AMBIENT-FAMILY SOURCE；显式缺拓扑、可微结构与丛证明 |
| 2025-05-16 | commit bf8959d365194c0361b7e35ff9147c524795585c；notes/foundations-and-geometry/02-parameterized-evaluation-frameworks.tex | 区分 AES 流形的几何族与求值参数上的代数求值族 | RETAIN 概念区分；拒绝无支持维数与丛断言 |
| 2026-08 | governance/discussions/aeg-tube-braid-markov-invariants.md | 分离边界辫与奇异填充并发展 Markov 与仿射 no-go 计算 | WORKING DERIVATION；只在活跃手稿重证该计算处使用 |
| 2026-08 | governance/discussions/three-branch-arithmetic-tubes-and-complexity.md，1250–1296 行 | 记录未定位到一般 E_k、E_{\log}、内在线、辫提升或 Markov 归一化不变量来源 | AUDIT CORROBORATION |
| 2026-08-06 | 当前 paper-3/ 源闭包 | 提供显式平行、对数覆盖、螺旋、Morse、分支与辫模型 | REDERIVED HERE |

「管」的三个历史含义必须保持区分：

1. AES 空间的环境族 q:X→B；
2. 代数求值族 E_alg→B_eval；
3. 零关联 \(\pi:\mathcal Z\to B\)。

当前手稿当投影是满射真光滑淹没时把真零管保留给第三个对象，带边界存在时对应整齐边界条件。
环境族内轨迹如 P(e^\lambda) 不自动是零支或线。

## 5. 公式级历史来源映射

### 5.1 管、奇点与覆盖材料

| 历史来源 | 精确材料 | 有效残基 | 拒绝或缺失推断 |
|---|---|---|---|
| archive/paper4p/aeg.tex，593–632 行 | T=\(\bigsqcup_{\lambda>0}E_1^{(\lambda)}\)；P(e^\lambda)；a=-x/y 的零集 x=0 | 环境 AES 切片参数化集合与平凡零集控制示例 | 无提供的全空间拓扑、光滑结构、局部平凡化、properness、嵌入线数据或纽结信息 |
| notes/foundations-and-geometry/02-parameterized-evaluation-frameworks.tex，25–62 行 | 乘/加求值族；E_alg 与 E_geom 区分 | 代数求值与几何参数族的区分 | 无拓扑即称纤维「通常二维」或不交并为丛 |
| notes/knots-and-loops/03-figure-eight-aeg-summary.tex，23–38 行 | 用提升纤维与 eikonal 传播的提议八字外部模型 | 候选研究计划 | 光滑全局传播、等变、下降、割迹控制、完备性、properness 与全测地性未证明 |
| 同上，40–47 行 | 黄金比校准 | Alexander 根可激励乘子 | 若 AEG 乘子是 t=e^\lambda，相容参数是 \(\lambda=\log t\)，非 \(\lambda=t\) |
| notes/knots-and-loops/04-figure-eight-hnn-arithmetization.tex，23–83 行 | 线性系统 \(\mu_u/t=\mu_u+\mu_v\)、\(\mu_v/t=\mu_u+2\mu_v\)，行列式 \(t^2-3t+1\) | RETAIN 作为显式仿射呈现计算 | 它不给忠实纽结群几何 |
| 同上，94–117 行 | 平移生成元交换 | RETAIN 作为所述忠实性阻碍 | 任何更早嵌入语言被取代 |
| notes/knots-and-loops/05-figure-eight-modulo-arithmetization.tex，25–63 行 | (1,0) 与 (0,\varphi) 生成的格 | 该格是普通离散矩形格 | \(\mathbb R^2\) 中「稠密奇异环面」为假；稠密只在指定一维投影后发生 |
| notes/foundations-and-geometry/03-single-zero-diffusion-model.tex，23–99 行 | Poincare 盘中的一个孤立零 | 被已验证 Paper I 模型取代 | 非多重零构造且非 E_k 证据 |
| notes/knots-and-loops/01-figure-eight-arithmetic-loop.tex，159–281 行 | 弯曲网格交公式与赋值 \(-x/y=-R/c\) | 符号与域审计后 RETAIN 作为可视化计算 | 映射 w=-1/z 全纯且保向，与 285 行相反 |
| notes/knots-and-loops/02-zero-taxonomy-and-arithmetic-loops.tex，85–136 行 | 六层零分类与零签名 | 仅作为关系论词汇 RETAIN | 历史下标不规范计数孤立奇点 |
| images/13-tube1st.png 与 images/sources/13-tube1st.tex | 四切片管图；TeX 文件只生成图像一个分量 | HISTORICAL VISUAL | 图不证明光滑关联或同痕 |
| images/14-apeirogon.png 与 images/sources/14-apeirogon.tex | Apeirogon 图与稀疏轴叠加 | HISTORICAL VISUAL | 无公式把它连接到 AEG E_{\log} 构造 |

### 5.2 仿射、Alexander 与纽结材料

| 历史来源 | 精确材料 | 现处理 |
|---|---|---|
| notes/knots-and-loops/06-fox-calculus-and-alexander-modules.tex，34–70 行 | Fox 系数 \(1-y\sim-\lambda\) 与 \(\pm\mu\lambda\) 的一阶比较 | RETAIN 作为类比，非同构 |
| 同上，72–102 行 | BS(1,2) Fox 因子 \(1-2t\) | RETAIN 计算；无下降即拒绝「内在不变量」 |
| 同上，104–170 行 | 八字位移 \(D(r)=-\Delta\) 与余循环律 \(D(uv)=D(u)+\phi(u)D(v)\) | 约定审计后 RETAIN；不断言非平凡上同调 |
| notes/knots-and-loops/01-figure-eight-arithmetic-loop.tex，98–150 行 | 显式网格点与选定位移消失时的闭包 | RETAIN 作为自由词计算 |
| notes/knots-and-loops/07-figure-eight-arithmetic-interpretation.tex，8–59 行 | 八字呈现与给 \(x-(t^2-3t+1)\) 的仿射词 | 只在生成元赋值在关系子轨迹下降的限定下 RETAIN |
| 同上，66–83 行 | 声称 Sage/SnapPy 检查到十一交叉 | HOLD 直到提供脚本、版本、呈现与不可变外部修订 |
| notes/knots-and-loops/08-small-knot-group-embeddings.tex | 三参数群律与声称纽结群嵌入 | REJECT 嵌入断言；所述指数解释不由显示的闭群律表示 |
| notes/knots-and-loops/09-knot-torsion-and-cyclotomic-fields.tex，110–165 行 | 条件 Alexander 因式分解与显式 6_2/6_3 计算 | RETAIN 作为呈现计算；因式分解是条件的，非新不变量 |
| notes/knots-and-loops/13-knot-torsion-results.tex，8–228 行 | 不同呈现与循环关系子下 4_1、6_2、6_3、7_6 的原始数据 | 主要 RETAIN 作为原始 torsion 依赖呈现、基点、符号与归一化的否定证据 |
| notes/knots-and-loops/10-arithmetic-knot-geometry-zh.tex，162–229 行 | 同表的润色重述 | 无独立证明权威；「内在」与「忠实」断言被拒绝 |
| images/sources/knot_4_1.tex，20–131 行 | images/knot_4_1.pdf 的可复现算术网格图 | 约定审查后 RETAIN 作为图来源 |

## 6. E_k 与 E_{\log} 溯源修正

以下仓库陈述必须被读作被本审计取代：

- paper-3/README.md 曾把多重零、E_k 与 E_log 笔记描述为好像提供迁移构造；
- governance/05-mathematical-status.md 把 E_k 描述为部分证明、E_{\log} 为部分显式构造；
- 一些工作讨论来源映射把对数或管几何归于 notes/computation-and-resources/03-turing-machine-resource-geometry.tex。

修正状态是：

| 历史标签 | 正确溯源状态 | 允许当前使用 |
|---|---|---|
| E_k | OPEN HISTORICAL NAME；NO CERTIFIED GENERAL MODEL FOUND | 不作定理定义分类使用。用「parallel k-zero model」等描述名。 |
| E_{\log} | DISCUSSION-LEVEL COVER/WINDING INTUITION；NO EXPLICIT HISTORICAL AEG MODEL FOUND | 只在提供新赋值、度量、域、覆盖群与零集审计时使用。 |
| tube of the first kind / K3 tube | HISTORICAL AMBIENT-FAMILY PROGRAM | 作为动机引用，非零管定理。 |
| `03-turing-machine-resource-geometry.tex` tube source | INCORRECT SOURCE ATTRIBUTION | `notes/computation-and-resources/03-turing-machine-resource-geometry.tex` 属于 Paper IV 资源/计算计划。 |

当前 Paper III 对数模型因此被称为对数零提升，而非 E_{\log}。其缺失原点对显示赋值与度量可去，
故它是覆盖域模型而非本质奇异脊柱。

## 7. 当前 Paper III 构造台账

下表分离导入与当前手稿证明的构造。每行标 REDERIVED HERE 者必须从活跃证明审查；上述历史文件
仅是动机或比较。

| 活跃来源 | 构造或结果 | 溯源状态 | 主要局限 |
|---|---|---|---|
| sections/01-singular-aes.tex，定义「Stratified singular AES」 | 添加局部有限 Whitney 分层作为控制数据 | REDERIVED HERE 自 Paper I 奇异 AES 接口 | 分层不声称规范 |
| 同上，定义「Zero-object hierarchy」 | 分离总零集、光滑关联、真管、嵌入管、线、辫闭包与纽结不变量 | REDERIVED HERE 自权威重组区分 | 层级中无箭头自动 |
| sections/02-local-zero-models.tex，「Cylindrical propagation」 | 显式乘积圆零模型 | REDERIVED HERE | 控制示例，非分类 |
| 同上，定理「Conformal realization」与推论 | \(g_a=\lvert da\rvert_h^2(\mu^2+\lambda^2a^2)^{-1}h\) 实现每个淹没，并在临界集外实现临界函数 | REDERIVED HERE | 完备性与刚性不蕴含 |
| sections/03-multi-zero-constructions.tex，定理「Parallel multi-zero model」 | \(a_h=e^xh(y)\) 带显式共形度量；对 k 简单根多项式恰 k 分量 | REDERIVED HERE；非迁移 E_k | 无唯一性、规范分类、齐性或完备性 |
| 同上，定理「Logarithmic zero lift」 | \(\mathbb C^\times\) 上 \(a_\times=Y\) 的拉回；零线 y=k\pi 与覆盖作用 k→k+2 | REDERIVED HERE；非迁移 E_{\log} | 楼下两个覆盖轨道；省略原点无本质奇点 |
| sections/04-parameter-discriminants.tex，参数化零截面定理 | 垂直横截与关联淹没的向量丛版本 | REDERIVED HERE 自 Paper I 接口与标准横截 | 全局拓扑仍需 properness 与边界控制 |
| 同上，结构判别式与非真逃逸示例 | 分离临界、边界、度量/域与逃逸机制 | REDERIVED HERE | 一般 Whitney 分层 AEG 判别式仍开放 |
| sections/05-regular-tubes.tex，定理「Proper real-zero tube」 | 圆上真零管有紧一维纤维与环面分量 | REDERIVED HERE 用真淹没定理与曲面分类 | 要求 properness、无边与光滑全局垂直定向 |
| 同上，定理「Helical zero-tube theorem」与推论 | 显式紧螺旋族；分量传输、覆盖平移与环面链环边界迹 | REDERIVED HERE | 选定边界迹是额外数据且非新纽结不变量 |
| sections/06-singular-fibers.tex，命题「AEG Morse bifurcations」 | 带共形实现奇异度量的定号与不定 Morse 族 | REDERIVED HERE | 示例，非普遍 AEG 正规形 |
| 同上，命题「Simple polynomial discriminant normal form」 | 简单横截多项式判别式点局部约化为 \(w^2=\tau\) | REDERIVED HERE 用经典全纯正规形论证 | 局部分支数据不决定全局填充或闭包 |
| sections/07-monodromy-and-braids.tex，有限根定理 | 平方自由首一多项式族定义有限真根覆盖与辫单值 | REDERIVED HERE 自经典构型空间事实 | 适用于复辅助场，非自动实秩一赋值 |
| 同上，定理「AEG realization of every braid」 | 用 Paper II 全纯坐标把选定几何辫实现为多项式根 | REDERIVED HERE | 普遍性不是纽结不变量且不提供算术历史的自然辫 |
| 同上，定理「Logarithmic root transport and gauge」 | 记录提升依赖覆盖整数与规范不变循环和 | REDERIVED HERE | 单个叶标签规范依赖；根须避开零 |
| sections/08-threading-and-knot-questions.tex，定义「Finite zero thread」 | 使线选择显式附加数据 | REDERIVED HERE | 内在性要求自然性定理 |
| 同上，命题「Stateless additive collapse」 | Abel 加法辫数据穿过 writhe 分解并在两个稳定化下坍缩 | REDERIVED HERE 自工作计算 | 适用于无状态加法目标 |
| 同上，命题「Ordinary exactness」 | 固定乘子仿射 torsion 是 Alexander-quandle 余边界 | REDERIVED HERE 自直接 Aff 计算 | 它不能提供普通余循环增强 |
| 同上，定理「Finite-field resonant affine class」与「Planar state-sum collapse」 | 证明共振扭曲类非零，再证明其平面经典链环状态和约化为染色计数 | REDERIVED HERE | 非零上同调单独不给超越 Alexander 基线的信息 |
| 同上，变乘子异常 | 计算 \(\mathfrak A_\kappa=((q-r)(r-1)/(qr))\kappa(x,y)\) | REDERIVED HERE 自直接代数 | 无连贯与状态数据非零缺陷不是 associator 或不变量 |
| 同上，历史八字词 | 重算词 abbbaBAAB 并得 \(-\Delta_{4_1}(t)\) | RETAINED AND REDERIVED HERE | 它是一般 t 的自由词阻碍，非通用纽结群不变量 |

appendices/app-A-regularity-and-properness.tex、appendices/app-B-configuration-and-braid-background.tex 与 appendices/app-C-affine-quandle-calculations.tex 中的支持计算是活跃证明闭包的一部分。它们不是遗留笔记的转包含。

## 8. 保留的断言与计算

以下历史材料在所述审计后可保持可见：

1. Paper I 正则零、奇异 AES、族关联与孤立盘结果，以其原始假设导入。
2. notes/foundations-and-geometry/02-parameterized-evaluation-frameworks.tex 中环境几何族与代数求值族的区分。
3. 平凡历史零族 x=0 作为说明参数化图不证明非平凡管拓扑的控制。
4. 线性 HNN/Aff 系统及其 Alexander 因子 \(t^2-3t+1\)，连同同一笔记平移像非忠实的证明。
5. Fox 一阶类比与仿射余循环律，除非独立证明不断言新上同调类。
6. 八字、6_2、6_3、7_6 计算，在记录呈现、词序、作用约定、初值、归一化与循环基点后。
7. 原始纽结表作为呈现无关原始 torsion 的反例。
8. Markov、Alexander-quandle、精确性、共振与变乘子计算，仅在活跃手稿重证处。
9. 历史图作为标注示意图，绝不作为存在、properness、同痕或不变性证据。

## 9. 拒绝、取代或严格条件断言

以下断言无新证明不得恢复：

1. 模型索引规范计数零、奇点或拓扑类型。
2. 正则内部零可孤立、交叉、分支或诞生/死亡。
3. 拓扑只在 da=0 处改变；非真逃逸、边界事件、域变化、度量退化与射影极点也必须控制。
4. 切片的不交并自动是光滑族或纤维丛。
5. 光滑总零集或淹没关联自动是全局管。
6. 无声明拓扑、闭包或连续参数化的求值像 S_{r,t}「通常二维」。
7. 提升八字纤维自动是三维泛覆盖中嵌入全测地双曲平面。
8. 无转换 t=e^\lambda 即把 AEG 加法参数与 Alexander 乘子等同。
9. (1,0) 与 (0,\varphi) 生成的格在平面中稠密。
10. 全纯 Mobius 映射 w=-1/z 反转定向。
11. 选定自由词 Aff 计算自动定义呈现纽结群的表示。
12. notes/knots-and-loops/08-small-knot-group-embeddings.tex 中三参数构造嵌入纽结群。
13. 原始仿射 torsion 独立于呈现、基点、循环关系子或归一化。
14. 标量交叉和仅因 Markov 稳定化前非零即新。
15. 固定乘子 Aff 共轭无附加状态即含超越 Alexander quandle 的纽结不变量。
16. 更强辫表示自动给更强纽结不变量。
17. 非平 Reidemeister-III 缺陷自动是 associator 或填充无关曲面 holonomy。
18. 可数多个对数叶本身实现任意纽结。
19. 管加任意选定线自动给同痕不变量。
20. 局部分支模型 w²=\tau 决定全局辫因式分解或填充的纽结类型。

## 10. 保留纽结计算的可复现要求

在历史计算作为数据而非动机引用前，其记录必须含：

- 群或幺半群呈现与精确关系词；
- 左或右作用与乘/复合序；
- 生成元与逆约定；
- 初始点或状态；
- 仿射乘子与对数参数约定；
- 循环基点与所用共轭；
- 分母与单位归一化；
- 脚本路径、软件版本、不可变仓库修订与预期输出。

当前声称 SageMath/SnapPy 计算延伸到十一交叉不满足此要求，因为脚本不在本仓库。它仍 HOLD。

## 11. 审计暴露的参考文献缺口

共享参考文献必须以精确版本或论文支持：

- Ehresmann 真淹没定理与实际使用的边界/整齐版本；
- Whitney 分层、Thom 同痕与局部奇异/判别式正规形；
- Artin 辫、Fadell–Neuwirth 构型空间与标准辫参考如 Birman；
- Alexander 闭辫定理与 Markov 闭包定理；
- Fox 演算、Burau 表示与精确 Alexander 比较；
- Rudolph 代数函数/辫曲面的结果，带所述准正性假设；
- Markov 迹、Jones/Turaev 构造、quandle 与扭曲 quandle 上同调；
- 若讨论更强辫表示，Lawrence、Bigelow、Krammer 与 Kohno；
- 八字纽结外部及其纤维/双曲结构的标准来源；
- SageMath 与 SnapPy，计算断言加精确版本与脚本修订。

governance/discussions/aeg-tube-braid-markov-invariants.md 末尾非正式列出的参考文献是参考文献
种子，尚未是已验证参考文献。

## 12. 已知溯源映射修正

1. governance/discussions/aeg-tube-braid-markov-invariants.md 中把管或对数几何归于
   notes/computation-and-resources/03-turing-machine-resource-geometry.tex 的引用不正确。
2. 历史短手稿路径是 archive/paper4p/aeg.tex，非活跃 paper4p/aeg.tex 源。
3. governance/discussions/three-branch-arithmetic-tubes-and-complexity.md 来源表中的重复 README
   路径描述不同文档，不应被当作两个独立来源。
4. 遗留 sections/sec09.tex 含关系与奇点展望，非管定理。
5. 当前 paper-3/ 文件是活跃手稿闭包。governance/source-inventory.md 中 Paper III 只是 README
   目的地记录的更早陈述被那里追加的集成增补取代。

## 13. 迁移规则

迁移非破坏：

- 所有遗留笔记、图、纽结计算与归档手稿原地保留；
- 无历史公式仅因复制到润色行文即被提升；
- 导入的 Paper I 与 II 结果保留其假设与引用；
- Paper III 新证明的构造在本审计中标记 REDERIVED HERE；
- E_k 与 E_{\log} 仍是历史名称而非规范分类符号；
- 穿线、Markov 下降与超越 Alexander/Burau 的分离保持开放，除非活跃手稿提供每个所需独立性
  证明。

本审计是 Paper III 集成记录的溯源权威。单个论断的数学真值状态由
governance/05-mathematical-status.md 按上述显式否定溯源发现与活跃手稿证明修正后支配。

## 14. 审计后算术–自守增补

2026-08-06 算术–自守集成不改变对 `E_k` 或 `E_log` 的否定历史发现。其溯源相反分裂为三个显式层。

### 内部 AEG 来源

Paper I 双边射影语义已提供算术语境

```text
T_s(z) = z+s,
J(z)   = -1/z.
```

特化 `s=sqrt(2)`、其四阶矩阵关系与完备正则 AES 分裂定理是活跃 Paper I 中新集成证明。

### 外部标准输入

(q=4) Hecke 群的定义与几何、Rosen 连分数与归一化三角群 Hauptmodul 使用新加入共享参考文献的
主要来源。这些来源确立群/一致化输入；它们不含 AEG 拉回度量或声称的 AEG 历史函子。

### 活跃系列中重新推导

以下公式与结论是 `REDERIVED HERE`：

- Paper II 中平面与柱面正则 AES 目标；
- 局部双全纯轨迹上的函子式拉回；
- Paper III 中本质临界点、(2m) 支零芽与 (2\pi m) 锥完备化；
- 归一化 (q=4) Hauptmodul 的平方根与 Cayley 实化；
- 所得 AEG 零图与 (\beta^{-1}([0,1])) 的相等；
- 符号特征下降边界；
- 从算术素相对除子到几何叶的 AEG 层级。

一般历史到相对除子映射是 `STRUCTURAL PROPOSAL`，不是恢复定理，也不是历史管对话的推论。

## 15. 符号覆盖纽结与寄存器增补

文件 `sections/05-q4-geodesic-knots.tex` 与 `sections/05-history-divisor-naturality.tex` 是
2026-08-06 推导。无历史仓库来源陈述其定理。

透镜空间紧化、中位环面斜率、尖点环绕公式与周期轨道模板是来自 Dehornoy 与 Dehornoy–Pinsky
的外部经典输入。活跃 Paper III 重新推导并审计其 (p,q)=(2,4) 特化、指标二周边格与所得
`S^3 minus T(2,4)` 覆盖。AEG 零 dessin 与经典编码图之间的相等用已声明 Hauptmodul 归一化加被
引用图定义。它不是恢复的 `E_log` 管或新测地流模板定理。

二次与四次寄存器方程、标记迹、极点余循环、算子坍缩计算与 Frobenius 字典是 `REDERIVED HERE`。
Hartshorne、SGA 1 与 Neukirch 提供标准代数几何与算术背景。带型寄存器是新提供输入；历史扫描
未发现把这些覆盖规范归于 AEG 历史的来源。因此一般自然性函子与从它下降的任何纽结装饰保留其
开放状态。

## 16. 多项式穿线载体增补

文件 `sections/05-polynomial-threaded-carriers.tex` 是新的 2026-08-06 推导。历史仓库扫描未发现
族 `Im(z^2-t^m)=0`、其载体拓扑或那里证明的水平恒等式的来源。以下断言因此从其显示方程
`REDERIVED HERE`：

- 载体的光滑性、整齐性、四个边界分量、`2m` 个 Morse 鞍点、Euler 特征 `-2m` 与亏格 `m-1`；
- 奇异 AES 切片度量与 `4 pi` 锥完备化；
- 内在根线、辫 `sigma_1^m` 与闭包 `T(2,m)`；
- 判别式阶与周期、辫指数、负载体框架与负半 Euler 特征的相等；
- 由标记覆盖格、覆盖作用与尖点斜率给出 q=4 周边二项式；
- 加权对数正切锥及其算术二次扭曲边界；
- 提供的四股辫中心扩张拉回、其积分关系特征与其 LHS transgression/归一化周期。

构型空间、Garside、环面链环、群上同调与加权射影背景是标准的；手稿要么引用它要么包含所需
计算。无历史来源使径向载体、分裂算术下降或四根系数路径规范。那些选择不被提升为一般 AEG
历史函子，新关系特征不与 Paper I 仿射 torsion 等同，二股与四股环面链环不互相等同。
