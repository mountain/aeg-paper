# Paper I 迁移日志

**基线：** `134e70a74ed010024afa7439bd3931402731423a`  
**规范活跃手稿：** `paper-1/aeg-paper-1.tex`、`paper-1/sections/` 与 `paper-1/appendices/`
**规则：** 遗留源保留直到人工审查；排除于活跃构建非删除。

## 迁移状态

- `CANONICAL`：重组 Paper I 的活跃源。
- `EXPORTED`：分配给后续论文且溯源记录的材料。
- `ARCHIVAL`：保留历史源，非活跃定理依赖。
- `HOLD`：复用前需单独审计的状态。

## 根与备选手稿

| 来源 | 状态 | 目的地 / 处理 | 论断处理 |
|---|---|---|---|
| `paper-1/aeg-paper-1.tex` | CANONICAL | 重写为十节 Paper I 入口 | 论断限于已证明基础结果 |
| `archive/legacy-root-manuscript/` | ARCHIVAL | 恢复的遗留 `aeg-paper.tex` 及其 `sections/sec01.tex`–`sec12.tex`；活跃构建中被 `paper-1/sections/` 取代 | 仅公式级审计后复用 |
| `../archive/revision-1/` | ARCHIVAL | 历史八节草稿 | 解析材料分配给 Paper II |
| `../archive/revision-2/` | ARCHIVAL | 历史八节与 Lean 支持草稿 | 非规范 Paper I 源 |
| `../archive/arxiv/` | ARCHIVAL | 较早分发快照 | DOI/发布溯源保留 |
| `../archive/paper4p/` | ARCHIVAL | 较早短手稿 | 管断言不导入 |
| `aeg-lemma.tex` | HOLD | 需单独源/证明审计 | 无 Paper I 依赖 |

## 遗留节处置

| 遗留源 | Paper I 目的地 | 导出或排除材料 |
|---|---|---|
| `sections/sec01.tex` | `01-introduction.tex` | 全纯计划 → Paper II |
| `sections/sec02-00.tex` | `02-sequential-histories.tex`；第 6 章示例 | 依赖定向的 threadlike 定义被取代 |
| `sections/sec02-01.tex` | 第 2 与 4 章；附录 E | 完整关系/中性理论 → Paper IV/HOLD |
| `sections/sec03.tex` | 第 4 与 5 章 | 解析算子解释 → Paper II |
| `sections/sec04.tex` | 第 6 与 7 章；附录 C | 管与一般模型层级 → Paper III |
| `sections/sec05.tex` | 第 8 章；附录 D | 凝聚解释 → Paper IV |
| `sections/sec06.tex` | 第 9 章；附录 D | 长标准接触计算缩减 |
| `sections/sec07.tex` | 仅基础处第 9 章 | Appell/函数论 → Paper II |
| `sections/sec08.tex` | 无活跃 Paper I 输入 | 整个解析发展 → Paper II |
| `sections/sec09.tex` | `10-conclusion.tex` | 接口在 Papers II–IV 间分割 |
| `sections/sec10.tex` | 附录 C 与 D | 历史模型编号移除 |
| `sections/sec11.tex` | 仅接触基础处附录 D | 全纯计算 → Paper II |
| `sections/sec12.tex` | 附录 E，极小示例 | 一般中性/关系 → Paper IV/HOLD |

## 工作笔记溯源

| 来源类 | 状态 | 规范目的地 |
|---|---|---|
| `notes/projective-condensation/01-bilateral-projective-condensation.tex` | EXPORTED/PARTIAL IMPORT | 顺序/射影/仿射证明 → Paper I 第 2–4 章；商与凝聚理论 → Paper IV |
| 分析、水平 CR、Appell 与算子笔记 | EXPORTED | Paper II |
| 多重零、`E_k`、`E_log`、奇异与管笔记 | EXPORTED | Paper III |
| `notes/knots-and-loops/` 与纽结相关 `images/sources/` | EXPORTED | Paper III 研究归档；尚无不变量断言 |
| `notes/thermodynamics-and-renormalization/rg_*` 与复杂度/资源笔记 | EXPORTED | Paper IV |
| 其余 `notes/`、`images/sources/` 与 `../archive/plans/` | HOLD/ARCHIVAL | 保留溯源；无自动定理权威 |

## 新规范源映射

| 目标 | 状态 | 主要论断 |
|---|---|---|
| `01-introduction.tex` | CANONICAL | 过程层级、贡献、范围 |
| `02-sequential-histories.tex` | CANONICAL | 顺序树分类；标记历史 |
| `03-projective-affine.tex` | CANONICAL | 双边射影语义；`PGL_2`；Borel 扇区 |
| `04-affine-cocycles.tex` | CANONICAL | 目标/源余循环；相对仿射缺陷 |
| `05-affine-flow.tex` | CANONICAL | Lie 流；正则 AES；eikonal/框架等价 |
| `06-hyperbolic-model.tex` | CANONICAL | 不变度量；完备齐次模型 |
| `07-zero-geometry.tex` | CANONICAL | 正则零定理；奇异 AES；参数族 |
| `08-acs-torsion.tex` | CANONICAL | 直接 ACS 求值；广义加权 Stokes |
| `09-contact-curvature.tex` | CANONICAL | 接触形式；有限缺陷；水平曲率 |
| `10-conclusion.tex` | CANONICAL | 已证明结论与 Papers II–IV 接口 |
| `appendices/app-A`–`app-E` | CANONICAL | 仅约定检查与支持计算 |

## 构建记录

| 阶段 | 结果 |
|---|---|
| 基线，固定 commit | 失败：缺 `stmaryrd.sty`；跟踪 PDF 过期 |
| 十节骨架 | 集成解析通过；所有目标输入存在 |
| 代数章节 | 集成构建与独立代数审查通过 |
| 几何章节 | 集成构建与独立几何审查通过 |
| ACS/接触章节 | 集成构建与独立符号/约定审查通过 |
| 最终本地构建 | 通过：60 页，干净 LaTeX/BibTeX 日志 |
| 渲染 PDF 审查 | 通过：全部页渲染；全部八图检查 |
| Docker 构建 | 未运行：当前环境 Docker 不可用 |

无遗留数学源被删除。Git 历史与保留路径在作者审查前保存每个被取代表述。

最终产物与全部闭包证据记录于 `paper-I-closure-report.md`。Paper II–IV 材料留在遗留树或其显式
目的地记录，且不通过活跃 Paper I 输入闭包导入。

## 迁移 M-0002

- 日期：2026-08-06
- 来源：`aeg-paper.tex`、`sections/foundations/` 与 `paper-II/`–`paper-IV/`
- 目的地：`paper-1/`–`paper-4/`
- 迁移状态：CANONICAL / EXPORTED
- 论断处理：无数学论断改变
- 受影响定理节点：无
- 记号变化：无
- 源中保留内容：遗留根 `sections/sec*.tex` 文件仍归档
- 源中移除内容：无；规范文件无数学编辑移动
- 构建结果：通过；`paper-1/aeg-paper-1.pdf` 产出（60 页）
- 审查者注：阿拉伯数字编号顶层目录现规范

## 命名约定 N-0001

- 源入口：`paper-k/aeg-paper-k.tex`
- 生成产物：`paper-k/aeg-paper-k.pdf`
- 当前实现：Papers I–III
- 保留未来名：`paper-4/aeg-paper-4.tex`；定理集稳定前不创建空手稿文件

## 迁移 M-0003

- **日期：** 2026-08-06
- **来源：** `sections/sec07.tex`、`sections/sec08.tex`、`sections/sec09.tex` 与
  `sections/sec11.tex` 的解析部分；对应 revision-1 与 revision-2 解析节；
  `notes/analysis-and-calculus/01-horizontal-analysis-program.tex`；Paper I 第 5、6、9 节的
  正则 AES、双曲模型与接触接口
- **目的地：** `paper-2/aeg-paper-2.tex`、`paper-2/sections/` 下八文件与
  `paper-2/appendices/` 下三文件
- **迁移状态：** CANONICAL / REDERIVED；遗留与备选源仍 ARCHIVAL 或 HOLD 且非活跃 TeX 依赖
- **论断处理：** 曲面与接触分析分离；原始平方和与度量选定变分 Laplacian 区分；形式、逐点与
  闭算子陈述获单独域；遗留 affine–Appell「基」修正为滤过 `C^infty(u,v)`-模；Poisson–Dirichlet
  与 Dirichlet-to-Neumann 定理在基本模型上新证明且经典溯源显式陈述
- **公式/源族目的地：** 一般曲面伴随与 CR 因式分解 → 第 2–3 节与附录 A；接触伴随、扭曲因式
  分解、对数场与 affine–Appell 计算 → 第 4 节与附录 B；双曲归一化、Poisson 核、边界唯一性、
  Fourier 能量与赋值依赖场 → 第 5–7 节与附录 C；局限与 Papers III–IV 边界 → 第 1 与 8 节
- **受影响定理节点：** P2-D1–P2-D2 与 P2-T1–P2-T9
- **记号变化：** `X_u,X_v` 保留给正则 AES 切框架；`D_u,D_v` 给接触提升；`Delta_g` 与 `Delta_C`
  命名变分算子；`Q_C` 命名原始接触平方和；接触 Appell 尺度是 `r=e^{lambda v}`，异于曲面 eikonal
  范 `q`
- **引用：** Paper I 溯源加 Ahlfors、H\"ormander 与 Caffarelli–Silvestre；无遗留源作外部证明权威
- **源中保留内容：** 每个遗留、修订与笔记文件未变供比较
- **源中移除内容：** 无
- **构建结果：** 本地通过；Paper II 产出干净 LaTeX 与 BibTeX 日志的 39 页 US-letter PDF；精确
  产物元数据与哈希记录于 `paper-II-closure-report.md`
- **审查者注：** 迹空间摘要收窄后独立跨支数学审查未发现阻塞公式或定理缺陷；范围审查确认
  Paper I → Paper II 依赖且无 Paper III/IV 泄漏

## 迁移 M-0004

- **日期：** 2026-08-06
- **来源：** Paper I 的奇异零与族接口；Paper II 的算术全纯坐标；`archive/paper4p/aeg.tex` 的
  历史管材料；`notes/foundations-and-geometry/02-parameterized-evaluation-frameworks.tex`、
  `notes/knots-and-loops/03-figure-eight-aeg-summary.tex`、`notes/knots-and-loops/04-figure-eight-hnn-arithmetization.tex`、`notes/knots-and-loops/05-figure-eight-modulo-arithmetization.tex`、
  `notes/foundations-and-geometry/03-single-zero-diffusion-model.tex`、`notes/knots-and-loops/06-fox-calculus-and-alexander-modules.tex`、`notes/knots-and-loops/01-figure-eight-arithmetic-loop.tex` 与
  `notes/knots-and-loops/02-zero-taxonomy-and-arithmetic-loops.tex` 的审计部分；
  `notes/knots-and-loops/` 与 `images/sources/knot_4_1.tex` 下纽结计算；两个从属 Paper III 讨论；
  与本地 checkout 所有 refs 可达的 249 个 commit
- **目的地：** `paper-3/aeg-paper-3.tex`、`paper-3/sections/` 下八文件、`paper-3/appendices/` 下
  三文件，与溯源审计 `governance/paper-III-source-audit.md`
- **迁移状态：** CANONICAL / REDERIVED HERE；遗留、归档、纽结、视觉与讨论源仍 ARCHIVAL、HOLD
  或 MOTIVATION 且非活跃 TeX 依赖
- **否定溯源发现：** 249 个可达 commit 树中无可验证一般多重零 AEG 构造、已定义一般 `E_k` 或
  显式历史 AEG `E_log` 构造；当前显式模型是新推导，非那些标签下的恢复定理
- **论断处理：** Paper I 的正则零、奇异 AES、关联与 properness 接口保留；环境族、零关联、真管、
  嵌入管、线、辫闭包与纽结不变量分离；拓扑改变含非真与边界机制；纽结断言停在显式 Markov 与
  选择独立门禁
- **新构造，全部 REDERIVED HERE：** 共形实现；柱面与平行多重零模型；对数零提升；结构判别式与
  非真逃逸；真实零管与螺旋管；定号与不定 Morse 族；简单分支模型；有限根与对数辫传输；Paper II
  坐标中每辫实现；有限零线；无状态标量、普通精确性、共振有限域、平面状态和与变乘子阻碍计算
- **保留历史计算：** HNN/Alexander 线性系统、选定 Fox 与仿射余循环公式、八字自由词计算与
  6_2/6_3/7_6 表，每个仅带 `paper-III-source-audit.md` 记录的局限与可复现字段
- **拒绝或持有断言：** 旧 `E_k` 指标的规范意义；`E_log` 的历史显式状态；光滑关联蕴含管；平面中
  无理格稠密；纽结群嵌入显示的解析仿射目标；呈现无关原始 torsion；从管、线、更强辫表示或
  非平缺陷自动不变
- **记号变化：** 旧 `E_k` 与 `E_log` 符号非规范模型名；描述名标识已证明构造；`tube` 保留给真零
  关联层；对数叶整数与规范不变循环和区分
- **源中保留内容：** 所有遗留节、笔记、纽结文件、图、归档手稿与工作讨论未变供比较
- **源中移除内容：** 无
- **构建结果：** 此仅溯源迁移条目不认证；构建与渲染产物证据属 Paper III 闭包报告
- **审查者注：** 活跃证明闭包排除每个历史笔记与讨论；任何未来 `E_k` 或 `E_log` 外部源须经不可变
  修订与公式级比较加入，溯源状态才可改变

## 迁移 M-0005

- **日期：** 2026-08-06
- **名称：** Papers I–III 跨算术–自守零网络集成
- **来源：** Paper I 的双边射影语境与正则 AES 方程；Paper II 的定向曲面复结构；Paper III 的奇异
  拉回、判别式、管与辫接口；新综合记录
  `governance/discussions/arithmetic-automorphic-zero-networks.md`；与引用的 Hecke 群、Rosen 连分数、
  三角群 Hauptmodul、相对除子与代数数论标准文献
- **活跃手稿目的地：** `paper-1/aeg-paper-1.tex` 与 Paper I 第 1、3、7、10 节；
  `paper-2/aeg-paper-2.tex`、Paper II 第 1、8 节与新 `paper-2/sections/05-pullback-cylinder.tex`；
  `paper-3/aeg-paper-3.tex`、Paper III 第 1–3 节、新 `paper-3/sections/04-arithmetic-zero-networks.tex`、
  现有参数、奇异纤维、辫与穿线节及附录 A；Paper II 与 III README 文件；根 `README.md`；与
  `bibliography/aeg-paper.bib`
- **治理目的地：** `00-authoritative-scope.md`、`01-paper-series-architecture.md`、
  `02-paper-I-outline.md`、`03-theorem-dependency-graph.md`、`05-mathematical-status.md`、
  `07-acceptance-checklist.md`、`08-open-questions.md`、三个论文决定记录、`paper-III-source-audit.md`、
  `source-inventory.md`、本迁移日志、三个闭包报告与 `governance/` 下新综合讨论
- **迁移状态：** CANONICAL / REDERIVED HERE / STANDARD EXTERNAL INPUT / OPEN FRONTIER。遗留笔记
  与讨论仍是溯源或动机且非活跃证明依赖。
- **Paper I 论断处理：** 算术语境 `T_sqrt(2)(z)=z+sqrt(2)` 与 `J(z)=-1/z` 射影求值；其矩阵关系
  把生成算子群与 `q=4` Hecke 三角群等同。字面词、标记历史、射影算子、稳定子陪集与端点保持区分。
  连通完备无边正则标量 AES 全局微分同胚于 `Z(a) x R`；这是光滑非 Riemannian 分裂且仅在那些精确
  假设下排除多分量或分支零网络。
- **Paper II 论断处理：** 旋转虚部平面目标是带打印曲率律的调和正则 AES；对数柱面是完备平坦正则
  AES；全纯局部双全纯把目标函子式拉回。临界点、代数分支点、柱面坐标零点或极点、退化度量与锥
  完备化在定理之外并传给 Paper III。解析拉回自然性不是历史到函数函子。
- **Paper III 论断处理：** 目标零线上全纯局部度 `m` 给局部本质 `2m` 支零与锥角 `2 pi m`。条件于
  引用归一化 `(2,4,infinity)` Hauptmodul，平方根/Cayley/柱面构造有零集 `beta^{-1}([0,1])`；四阶点
  是四价 `4 pi` 锥零、二阶点是双价边中点，赋值在符号特征核上或作为实符号线截面下降。相对除子
  定理仅在声明整环上提供首一一般平方自由多项式后适用。
- **算术边界：** 系数域因式分解、几何叶、解析单值与 Galois/Frobenius 数据是不同层。`q=4` 构造
  提供算子算术与自守一致化，非 `Z[sqrt(2)]` 中非唯一分解。从标记历史到算术相对零除子的一般函子
  仍开放。
- **受影响定理节点：** P1-H1、P1-H2、P1-Z9；P2-A1–P2-A3；P3-S1–P3-S4；P3-R1–P3-R3，其中 P3-S3
  是引用标准输入且 P3-R3 仍是开放结构提案
- **溯源：** AEG 矩阵、分裂、拉回、分支、Cayley、符号下降与零网络计算在活跃论文中证明或重新
  推导。Hecke 群与 Hauptmodul 几何与代数/算术背景是外部引用输入。一般 `E_k` 与显式 AEG `E_log` 的
  否定历史发现未变。
- **源中移除内容：** 无
- **统一构建结果：** `./build.sh all` 完成当前每论文四 LaTeX 遍序列（`pdflatex`、BibTeX 与三次解析
  `pdflatex`）。Papers I–III 含 63、44、43 页。最终大小、SHA-256 值、标签计数、引用计数与干净日志
  证据记录于 `audit-report.md` 第 9 节与三个闭包后修正案。

## 迁移 M-0006

- **日期：** 2026-08-06
- **名称：** q=4 符号覆盖纽结与有限寄存器除子自然性
- **来源：** 活跃 q=4 Hauptmodul/符号构造；Paper I 的年代射影求值与中性词 `omega_4`；引用的测地
  流、透镜空间、模板、有限平展与算术 Frobenius 文献；与双优先数学红队记录
- **活跃手稿目的地：** 新 `paper-3/sections/05-q4-geodesic-knots.tex` 与
  `paper-3/sections/05-history-divisor-naturality.tex`；Paper III 入口、摘要、引言、README 与 PDF；
  Paper I 与 II 结论接口；根 README；与共享参考文献
- **治理目的地：** `00-authoritative-scope.md`、`05-mathematical-status.md`、
  `07-acceptance-checklist.md`、`08-open-questions.md`、`decisions-paper-III.md`、
  `source-inventory.md`、本迁移日志、算术–自守综合讨论、审计报告与闭包修正案
- **迁移状态：** CANONICAL / REDERIVED HERE / CLASSICAL EXTERNAL INPUT / RESTRICTED NATURALITY
  MODEL / OPEN GENERAL FRONTIER
- **q=4 拓扑处理：** 符号核有签名 `(0;2;infinity,infinity)`；其完备粗 AEG 载体是 `C*`。保留双曲
  orbifold，其单位切丛由周边覆盖与斜率计算在声明填充下与 `S^3 minus T(2,4)` 等同。局部四支芽
  不与全局链环等同。
- **纽结处理：** 本原双曲算子类给经典测地流周期轨道纽结。循环词平移按算子共轭作用；路径逆给
  时间反演轨道；映射满射但坍缩标记历史纤维。零 dessin 是编码脊柱，非三维模板。不声称新同痕或
  Markov 不变量。
- **寄存器处理：** `u^2=t` 强制等变射影二次端点除子与显式 Frobenius。标记前缀迹与普通极点余循环
  在 `t=2` 与 `t=1/2` 区分 `omega_4` 与空历史。塔 `v^2=3`、`u^2=t+v` 强制带两个常几何分量的算术
  不可约四次，带显式判别式、单值与 Frobenius 循环型。
- **边界：** 两个寄存器是提供的带型输入。其末端端点数据穿过射影求值分解且不解决一般历史到素
  除子函子、因式分解历史问题或纽结装饰下降。
- **受影响定理节点：** P3-K1–P3-K4 与 P3-R3–P3-R5；OQ-072–OQ-074 按记录部分解决，OQ-075 仍开放，
  OQ-076 记录新标记历史纽结增强前沿
- **源中移除内容：** 无
- **统一构建结果：** `./build.sh all` 完成三手稿当前 `pdflatex`–BibTeX–三次 `pdflatex` 序列。
  Papers I–III 含 63、44、58 页。最终大小、SHA-256 值、标签、引用与引用计数、干净日志证据与
  视觉审计记录于 `audit-report.md` 第 10 节与 M-0006 闭包修正案。

## 迁移 M-0007

- **日期：** 2026-08-06
- **名称：** 切片间多项式关系与穿线载体
- **来源：** 用户指定管直觉；活跃 q=4 符号覆盖格与尖点斜率计算；提供族 `P_m(z,t)=z^2-t^m`；
  Paper III 现有奇异 AES、相对除子、有限根与辫接口；与独立载体、正合序列、q4 自然性与数学红队
  计算
- **活跃手稿目的地：** 新 `paper-3/sections/05-polynomial-threaded-carriers.tex`；Paper III 入口、
  摘要、引言、结论、README 与生成 PDF；根 README
- **治理目的地：** `00-authoritative-scope.md`、`05-mathematical-status.md`、
  `07-acceptance-checklist.md`、`08-open-questions.md`、`decisions-paper-III.md`、
  `source-inventory.md`、本迁移日志、审计报告与 Paper III 闭包修正案
- **迁移状态：** PROVED EXPLICIT HORIZONTAL MODEL / MARKED TORIC q=4 SPECIALIZATION / OPEN
  HISTORY-NATURAL LIFT
- **载体处理：** `Im(P_m)=0` 是带四个边界圆与 `2m` 个圆值 Morse 鞍点的紧连通整齐光滑关联；有亏格
  `m-1` 与奇异 AES 切片度量。不被称为真零管。
- **线处理：** `P_m=0` 是带辫 `sigma_1^m` 与闭包 `T(2,m)` 的嵌入有限根线。其算术素分量、几何
  分量与链环分量在此族一致，但嵌入辫保留整数 `m` 超出置换奇偶。
- **水平恒等式：** 判别式阶、对数周期、辫指数、载体框架周期与负半 Euler 特征一致。在 `m=4`，
  纯辫坐标与互相环绕数为二，尽管多项式分裂且其叶置换平凡。
- **q=4 处理：** 有序填充子午、指标二格、覆盖平移与尖点斜率导出双陪集环面除子 `u^2=t^4` 直到
  环面规范。紧化标记符号覆盖进一步恢复二项式作为其对数正切尖点截面并在加权 Hopf 圆丛中实现其
  链环。算术二次下降与到亏格三载体的径向延伸仍是单独声明选择。
- **扩展校准：** 提供四根 Garside 与旋转路径把辫中心扩张拉回到 q=4 单位切扩张；其共同全扭残差与
  归一化判别式周期被证明。诱导不变核特征有等于单位切 Euler 扩张类的 LHS transgression，但非
  Paper I 仿射 torsion 且尚无历史自然起源。
- **边界：** 纯辫正合序列非单位切中心扩张，不声称 Paper I torsion transgression，中性历史
  `omega_4` 仍是硬系数路径自然性测试。
- **受影响定理节点：** P3-H1–P3-H7；OQ-072 获标记周边细化；OQ-073 与 OQ-076 仍开放；OQ-077 记录
  混合切片–管自然性问题。
- **源中移除内容：** 无
- **统一构建结果：** Papers I–III 干净构建于 63、44、69 页。最终 Paper III 产物 704,239 字节、
  SHA-256 `f094bc5e70739fc0144fcefff78a877f03d420f39f2475be12aed6d938a9dd9e`；静态、数学与全页
  视觉审计在修复后报告无阻塞或重大发现。完整统一证据记录于 `audit-report.md` 与
  `paper-III-closure-report.md`。

## 迁移 M-0008

- **日期：** 2026-08-06
- **名称：** 六次 Lyashko–Looijenga 遗忘实验室
- **来源：** 提供的稀疏六次 `P_0(x)=x^6-x`；活跃多项式载体/线接口；经典 Lyashko–Looijenga、
  转置因式分解、Birman–Hilden、Picard–Lefschetz、辛单值与超椭圆算术文献；与独立根/临界值辫及
  论断边界红队
- **活跃手稿目的地：** 新 `paper-3/sections/05-sextic-ll-laboratory.tex`；Paper III 入口、引言/
  论断台账、结论、README 与生成 PDF；根 README
- **治理目的地：** `05-mathematical-status.md`、`07-acceptance-checklist.md`、
  `decisions-paper-III.md`、`source-inventory.md`、本迁移日志、审计报告与 Paper III 闭包修正案
- **迁移状态：** PROVED EXPLICIT SEXTIC LABORATORY / CLASSICAL LL AND GENUS-TWO INPUTS / OPEN
  LL–IGUSA TWIN TEST / OPEN AEG-HISTORY NATURALITY
- **事件多项式处理：** 对首一中心六次 `P`，`Q_P(t)=6^{-6} disc_x(P(x)-t)` 是临界值首一五次。
  正则 LL 映射是度 `6^4=1296` 的有限平展覆盖。这些是坐标归一化叶；自由残差源旋转 `mu_6` 给
  `216` 个轨道，非 `1296` 或 `216` 个两两非同构曲线。
- **显式铅笔处理：** `P_0=x^6-x` 有五个简单临界值与事件多项式 `Q_0=t^5+5^5/6^6`。绕那些值的
  子午提升为沿六顶点跨星的半扭，生成 `B_6`。关联实载体有鞍墙，其复零给内在六叶线，其双重分支
  覆盖给亏格二映射环面。实墙穿越、根碰撞与谱退化仍是不同层。
- **双辫处理：** 临界值传输经 LL `1296` 叶覆盖作用，而移动测试值给单独垂直 `F_5` 与六根辫。
  手稿用混合辫扩张及其 LL 拉回；不声称遗忘 LL 叶后的规范同态 `B_5 -> B_6`。
- **亏格二与算术处理：** 显示铅笔满射到亏格二映射类群且经引用经典提升与单值定理有完整辛单值。
  纤维 `y^2=x^6-x-1` 由引用经典判据有打印 `S_6` Galois 与几何自同态结论。共同有限目标
  `Sp_4(F_2) 同构 S_6` 不规范等同 Frobenius 元与拓扑环。
- **开放边界：** LL–Igusa 孪生测试未在一条 LL 纤维中确立两条非同构亏格二曲线。无无限制算术
  历史规范选择六次、LL 叶、混合辫路径或六根辫。不声称新纽结不变量或 Markov 下降。
- **受影响定理节点：** P3-L1–P3-L9；P3-H7 与 P3-R3 仍开放。
- **源中移除内容：** 无
- **规范构建结果：** `./build.sh 3` 产出干净 78 页、809,341 字节 PDF、SHA-256
  `d5bf667041dc6ce52189f840a5a691c4d8c6eed1126705911937a907fb74f816`。静态闭包 17 个 TeX 文件、
  322 唯一标签、157 解析引用目标与 30 解析引用键。全部 78 页渲染并视觉检查无阻塞布局缺陷。

## 迁移 M-0009

- **日期：** 2026-08-06
- **名称：** 显式几何 LL–Igusa 孪生与纤维式非因式分解
- **来源：** 稀疏偶系数六次 ansatz 中的精确消元；临界值缩放；二次 Igusa–Clebsch 不变量与二元
  六次判别式；与 Farb 及合作者近期工作的周围六次模比较
- **活跃手稿目的地：** Paper III 摘要、引言、六次 LL 实验室、结论、README 与根 README
- **治理目的地：** `00-authoritative-scope.md`、`01-paper-series-architecture.md`、
  `03-theorem-dependency-graph.md`、`05-mathematical-status.md`、`07-acceptance-checklist.md`、
  `decisions-paper-III.md`、`source-inventory.md`、本迁移日志、`audit-report.md` 与
  `paper-III-closure-report.md`
- **迁移状态：** EXPLICIT GEOMETRIC TWIN PROVED / 完整 216 轨道普查、算术周期比较、标记单值细化、
  Hodge/Siegel 能量与历史自然性 OPEN
- **精确对：** `(P_0=x^6-x)` 与显示的代数首一中心 `(P_1)` 有相同事件五次
  `(Q_0=t^5+5^5/6^6)` 且在相异残差源旋转轨道。
- **几何分离：** 在共同正则切片 `(t=1)`，两个六次有判别式 `(6^6+5^5)`，但其精确二次 Clebsch 值
  给相异绝对 Igusa–Clebsch 比。其亏格二曲线在 `(\mathbb C)` 上非同构，故切片模读数不穿过 LL 事件
  多项式因式分解。
- **计算溯源：** 同事件恒等式由打印精确 Sylvester 结式恒等式与缩放律证明；模分离是精确符号不变量
  比较。仓库脚本复现两计算且是验证证据而非证明替代。
- **有限叶下降：** 在 `(Q(1)\ne0)` 上，残差旋转商是度 `(216)` 有限平展覆盖。模叶可观测量有带
  下降迹、范与更高对称系数的范谱多项式。规范平均把常数与零和置换表示分开；其平方范是单值不变
  遗忘方差。显式孪生在 `(Q_0)` 供打印精确正下界。不断言沿任意开 LL 路径恒常。
- **移动切片电荷：** 对两条显式铅笔，`(\mathcal J_1/\mathcal J_0)=((t-\beta)/t)^5)`，`(0)` 与
  `(\beta)` 都正则，除子是 `(5[\beta]-5[0])`。其对数残差平衡，但这非有限 Dirichlet 能量。
- **Farb 边界：** 近期 Farb–Kisin–Wolfson、Farb–Wolfson、Farb–Looijenga 与刚性工作提供密切相关
  六次、构型空间、模、单值、算术与周期框架。它不提供此 LL 纤维对；Paper III 只声称显式上方
  纤维式非因式分解。
- **开放边界 / P3-L10：** 无全部 `(1296)` 叶或 `(216)` 旋转轨道的完整解决；不断言两数计数曲线；
  无对对的认证 Frobenius 或约化 Siegel 周期区分；无按标记局部 `(\operatorname{Sp}_4(\mathbb Z))`
  转置与 Hurwitz 作用分组后的结果；无 Hodge-或 Siegel-度量能量；无历史自然叶选择。
- **受影响定理节点：** P3-L9 从开放提升为已证明；P3-L10 引入为剩余有限普查与更深孪生问题。
- **源中移除内容：** 无
- **规范构建结果：** `./build.sh 3` 产出干净 83 页、859,662 字节 PDF、SHA-256
  `f9cf579734cbf2a5c70794470ba3af3b79c2fc1144926513f291b7a2462c858`。静态闭包 17 个规范 TeX
  文件、351 唯一标签、175 解析引用目标与 53 条目共享参考文献中 36 解析引用键。全部 83 页渲染
  并视觉检查无阻塞布局或字形缺陷。

## 迁移 M-0010

- 日期：2026-08-07
- 来源：根 `sections/sec01.tex`–`sections/sec12.tex` 与修订 `095ae4b28cb645ea43e18aa2560d227830cc3a14`
  的历史 `aeg-paper.tex`
- 目的地：`archive/legacy-root-manuscript/`
- 迁移状态：ARCHIVAL
- 论断处理：无数学论断改变；每个节源加归档溯源注释
- 源中移除内容：遗留根 `sections/` 路径；所有文件保留于目的地
- 构建结果：四份规范论文通过 `./build.sh`；归档包本身保留其历史仓库相对依赖路径且非独立构建包

## 迁移 M-0011

- 日期：2026-08-07
- 来源：`misc/`、`knots/` 与先前扁平 `notes/` 目录
- 目的地：图/模型源到 `images/sources/`；纽结源与相关环笔记到 `notes/knots-and-loops/`；其余笔记
  到 `source-inventory.md` 记录的五个其他主题子目录
- 迁移状态：ARCHIVAL RECLASSIFICATION
- 论断处理：无数学论断、状态、假设或构建闭包改变；跟踪渲染产物与本地编译伴侣随其源文档移动
- 引用处理：仓库对移动源路径的引用更新到当前目的地
- 源中移除内容：无；旧 `misc/` 与 `knots/` 目录名在全部内容保留于目的地后退役
- 构建结果：无规范 LaTeX 源或构建依赖改变；静态路径检查未发现对退役位置的剩余引用

## 迁移 M-0012

- 日期：2026-08-07
- 来源：顶层 `styles/`
- 目的地：`archive/legacy-latex-styles/`
- 迁移状态：ARCHIVAL
- 论断处理：无数学论断、状态、假设或规范构建闭包改变
- 引用处理：历史修订草稿、归档根手稿与热学笔记现引用两个归档样式路径
- 源中移除内容：无；两个第三方样式文件逐字节保留且空顶层目录退役
- 构建结果：规范论文不加载任一样式；静态路径检查未发现对退役顶层位置的剩余引用

## 迁移 M-0013

- 日期：2026-08-07
- 来源：根 `aeg-paper-0.bib`
- 目的地：`bibliography/aeg-paper.bib`
- 迁移状态：SHARED RESOURCE RELOCATION
- 论断处理：无数学论断、引用条目、假设或规范 TeX 成员改变；仅共享数据库路径改变
- 引用处理：四份规范论文与用共享数据库的历史手稿现引用其专用目录
- 源中移除内容：无；参考文献移动而不重写条目
- 构建结果：`./build.sh` 成功重建四份规范 PDF；每个 BibTeX 日志读 `../bibliography/aeg-paper.bib`，
  无未定义引用、未定义引用或重复标签

## 迁移 M-0014

- 日期：2026-08-07
- 来源：顶层 `restructure/`
- 目的地：顶层 `governance/`
- 迁移状态：GOVERNANCE CONTROL-PLANE RENAME
- 论断处理：无数学论断、状态、假设、源内容或规范构建闭包改变
- 引用处理：仓库指南、治理文档、论文 README、来源审计、讨论与本地工作区路径历史现用新名
- 源中移除内容：无；全部 30 文件带目录结构完整移动
- 构建结果：`./build.sh` 成功重建四份规范 PDF，无未定义引用、未定义引用或重复标签；唯一剩余
  `restructure/` 字符串是本迁移与 `source-inventory.md` 中的历史源路径记录

## 迁移 M-0015

- 日期：2026-08-07
- 来源：`governance/AGENTS.md` 与根发现指针 `AGENTS.md`
- 目的地：根 `AGENTS.md`
- 迁移状态：AUTHORITATIVE INSTRUCTION CONSOLIDATION
- 论断处理：无数学论断、状态、假设或规范构建闭包改变
- 引用处理：仓库 README、治理概览、来源清单、来源审计与讨论溯源现指向根指令文件
- 源中移除内容：仅被取代的根指针文本；完整权威指令内容保留于目的地
- 构建结果：权威内容在 `governance/` 路径迁移后匹配旧治理副本；所有 AGENTS 链接解析，`./build.sh`
  重建四份规范 PDF 无未定义引用、未定义引用或重复标签

## 迁移 M-0016

- 日期：2026-08-07
- 名称：显式手稿级草稿通知
- 目的地：根 README、现有逐论文 README 与四份规范手稿标题事项
- 迁移状态：EDITORIAL MATURITY DISCLOSURE
- 论断处理：无数学论断或治理状态改变；`draft` 明确是编辑、视觉、概念整合与出版成熟度描述而非
  论断状态标签
- 遗留比较：通知记录归档根手稿目前在阐述、图与正文–图整合上可能更精
- 构建结果：`./build.sh` 重建四份规范 PDF 无未定义引用、未定义引用或重复标签；每第一页渲染并
  检查确认通知在摘要前可见无剪切或重叠

## 迁移 M-0017

- 日期：2026-08-07
- 来源：`notes/` 下六个分类子目录
- 目的地：带归一化文件名的同主题目录
- 迁移状态：NOTE NAMING AND ORDER NORMALIZATION
- 命名规则：`NN-descriptive-topic-slug`，每个主题内独立两位阅读序；伴侣产物共享源 basename
- 论断处理：无笔记内容或数学状态提升；数字码明确非权威、年代或定理状态码
- 引用处理：治理记录与笔记到笔记引用更新为描述性文件名；旧名仅在显式标为历史溯源处存活
- 源中移除内容：无
- 构建结果：全部 39 个笔记源满足命名规则无逐目录重复码；27 个唯一仓库笔记路径引用与所有伴侣
  basename 解析；`./build.sh` 成功重建四份规范 PDF

## 迁移 M-0018

- 日期：2026-08-07
- 名称：最终仓库状态一致性审计
- 范围：根与治理概览、当前到目标映射、来源清单、带日期审计/闭包记录、开放问题登记与 Papers I
  与 II 中的 Paper I–III 接口段
- 迁移状态：DOCUMENTATION AND CROSS-PAPER CONSISTENCY RECONCILIATION
- 论断处理：无定理、假设、证明或数学论断状态改变；编辑 `draft`、数学审查闭包、历史审计快照与
  未解决研究计划保持区分
- 仓库处理：当前布局、四个规范源闭包、共享参考文献位置、多论文构建接口与已完成迁移同步；历史
  基线路径与带日期产物证据仍标为历史
- 卫生处理：`.DS_Store` 仓库范围忽略；现有本地副本既不跟踪也不删除
- 引用处理：Papers I 与 II 现引用现有 Paper II/III 手稿记录描述下游结果；所有 Markdown 链接、TeX
  输入、参考文献路径、引用键、标签与引用解析
- 构建结果：`./build.sh` 重建四份规范 PDF；最终日志无未定义引用、未定义引用、重复标签或缺失资产。
  Paper IV 七组有限验证套件也通过

## 迁移 M-0019

- **日期：** 2026-09-22
- **名称：** Paper 0 成为系列几何基础
- **权威：** `governance/00b-paper-0-geometric-foundation-amendment.md`（权威修正案 v1.0），取代
  `00a-paper-0-amendment.md` §§2–5 并重新分配那里所列 `00-authoritative-scope.md` §20 拥有权行
- **来源：** `paper-1/sections/04-affine-cocycles.tex`、`05-affine-flow.tex`、
  `06-hyperbolic-model.tex`、`08-acs-torsion.tex`、`09-contact-curvature.tex`、
  `paper-1/appendices/app-B-affine-cocycles.tex`、`app-C-hyperbolic-calculations.tex`、
  `app-D-acs-contact.tex` 与 `paper-1/appendices/app-A-conventions.tex` 的仿射群小节
- **目的地：** `paper-0/sections/07-affine-cocycles.tex`、`08-acs-tearing.tex`、
  `09-contact-of-tearing.tex`、`paper-0/appendices/app-B-hyperbolic-calculations.tex`、
  `app-C-affine-cocycles.tex`、`app-D-acs-contact.tex` 与合并 `paper-0/sections/03-aes-and-motion.tex`
- **迁移状态：** MOVE（几何章节与附录）、REWRITE（Paper 0 入口、引言、接口；Paper I 入口、引言、
  接口、结论）、KEEP（Paper I §§2、3、7；附录 A、E）
- **论断处理：** 无数学论断改变。每个移动标签、假设与状态保留；移动结果保留其在 Paper I 中的
  状态并进入新登记 `05b-paper-0-status-register.md`
- **加入 Paper 0 的新材料：** 分配展开节（`prop:p0-distributive-operator-identity`、
  `ex:p0-distributive-charge-transport`）、模型名约定 `conv:p0-model-labels`、撕裂定义
  （`def:p0-tearing`）、§10 两阻碍（`prop:p0-arithmetic-generators`、
  `prop:p0-characters-cannot-see-tearing`）、穿孔空间定义（`def:p0-punctured-aes`）、切锥命题
  （`prop:p0-puncture-tangent-cone`）与六个计算见证登记
- **记号变化：** Paper 0 采纳修正案 §7 对应表（`E_0` = 基本正则双曲模型，恰好与旧
  `E_{\mathrm{hyp}}` 等同一次；`E_1` = 单穿孔盘；`E_k` 仅描述性）。无其他记号重命名；`p0:` 标签
  前缀保留给既有 Paper 0 标签且移动标签保留原名
- **引用处理：** Papers II、III、IV 中移动对象的跨论文引用重新指向 Paper 0；新参考文献键
  `Yuan2026AEGPaperZero` 记录 Paper 0，`Yuan2026AEGFoundations` 现带修订 Paper I 副标题。
  `Wu2000MathematicsMechanization`、`Yuan2026ProcessGeometry` 与 `Yuan2026AEGHoleRegister` 添加，
  每个在文本引用
- **源中移除内容：** 无删除；被取代 Paper 0 节文件（`02-two-combs.tex`、`03-paths.tex`、
  `04-ripple-pencils.tex`、`07-interface.tex`）由同论文重写文件取代且 git 中可恢复
- **构建结果：** `./build.sh 0` 67 页、`./build.sh 1` 干净、`./build.sh 2`、`3`、`4` 重建；最终
  日志无未定义引用、未定义引用、重复标签或缺失资产
- **审查者注：** 孔/撕裂探索材料保留为跟踪笔记
  （`notes/foundations-and-geometry/06-hole-obstructions-ledger.md`）不提升其任何项；该登记两个
  精度缺陷记录于 Paper 0 §11 与 `08-open-questions.md` 而非静默修复

## 迁移 M-0020

- **日期：** 2026-09-22
- **名称：** Paper 0 响应外部审查的修订
- **权威：** 普通任务报告；无范围变化。M-0019 与 `00b-paper-0-geometric-foundation-amendment.md`
  固定的 Paper 0 范围未变
- **输入：** `AEG-Paper-0-review-2026-09-22-v0.1.md`（审查者：ChatGPT；审查产物 SHA-256
  `afeff197…f3f5e5b`、68 页）与 `AEG-Paper-0-review-2026-09-22-response-v0.1.md`
- **来源与目的地：** `paper-0/sections/02-expansion.tex`、`03-aes-and-motion.tex`、
  `04-ripple-geometry.tex`、`05-reciprocals-fixed-points.tex`、`06-projective-unification.tex`、
  `08-acs-tearing.tex`、`09-contact-of-tearing.tex`、`10-beyond-linear.tex`、`11-holed-aes.tex`、
  `12-interface.tex`、`aeg-paper-0.tex`、`paper-0/README.md` 与 `bibliography/aeg-paper.bib`
  （全部原地编辑）；`governance/05b-paper-0-status-register.md` 更新
- **迁移状态：** `REWRITE`（证明、定义与行文）与 `REPAIR`（两个空泛或误陈述定义）；无文件跨论文
  移动
- **论断处理：** 四个真实缺陷修复：穿孔空间定义（`def:p0-punctured-aes`）、
  `prop:p0-arithmetic-generators` 证明、极点图定向（`eq:p0-pole-coordinate`）与框架见证有向转移
  计数。一个过度陈述收窄：`prop:p0-arithmetic-generators` 结论现是有限维 Lie 群闭包边界，且
  `prop:p0-characters-cannot-see-tearing` 对任意 charge 端点可观测量重述。一个假设显式化：
  `def:p0-tearing` 现分离尺度相容与 charge 相容。一个解释性断言降级：四圆切锥不再耦合到穿孔，且
  §11.3 断言成为登记问题
- **新材料：** `prop:p0-contact-quotient`（基本模型是接触模型 Reeb 商，五关系带证明），审查中
  提议并在此独立验证；§3 部分运动 `Warning`；固定 Möbius 图 `Z = (lambda/mu)x + iy` 注；`mu*lambda`
  是什么与不是什么的注；以及 §§10–11 是研究报告而非稳定接口的陈述
- **记号变化：** 除极点图符号现为 `-1/(z-q)` 带所述理由外无
- **引用处理：** 添加 `Etnyre2001IntroductoryLectures`（接触几何）与
  `Khinchin1964ContinuedFractions`（标准连分数收敛）；两者文本引用。无条目移除
- **源中移除内容：** 无
- **构建结果：** `./build.sh 0` 产出干净最终日志的 74 页 PDF；无未定义引用、引用或重复标签
- **审查者注：** 审查每点在接受前检查；审查自身对 `prop:p0-arithmetic-generators` 的修正证明被
  采纳，其 Reeb 商命题被重新推导并采纳，其一项（校准轮计数）以移除不可复现数字而非重复解决

## 迁移 M-0021

- **日期：** 2026-09-22（当日第二次修订）
- **名称：** Paper 0 开放项 OI-4 与 OI-1 解决
- **权威：** 普通任务报告；无范围变化
- **来源与目的地：** `paper-0/sections/08-acs-tearing.tex` 与
  `paper-0/sections/11-holed-aes.tex`（原地编辑）；`paper-0/README.md`、
  `paper-0/sections/12-interface.tex`、`governance/05b-paper-0-status-register.md`、
  `governance/08-open-questions.md` 与 `governance/paper-0-closure-report.md` 更新
- **迁移状态：** `EXTEND`（现有章节内新结果）；无跨论文移动
- **论断处理：** 六个新节点，全部 `PROVED`（加一个约定）：`conv:p0-history-group`、
  `prop:p0-history-homomorphisms`、`prop:p0-acs-is-abelianization`、`thm:p0-descent`（§8）；
  `lem:p0-gradient-nonvanishing`、`thm:p0-four-circle-model`（§11）。两个开放问题解决且其正文保留：
  OQ-086（历史幺半群与 charge 下降）与 OQ-085（四圆构型的 AES 数据）。一个新开放问题开启：
  OQ-087（模型推广、`k` 穿孔、运动生成赋值）
- **数学内容：**
  OI-4 --- 历史群 `G = (R,+) * (R,+)` 固定，charge 端点等同为其交换化，求值是其按传输关系的商，
  下降问题不对称回答：乘法 charge 下降到运动，加法 charge 可证明不，由 `h(p,q) = M_q A_p M_{-q}
  A_{-e^{-q}p}` 带 `c(h) = (p(1-e^{-q}), 0)` 见证。
  OI-1 --- 四圆构型现是显式穿孔 AES 的零轨迹：赋值 `a = P`、eikonal 恒等式强制的度量
  `g = |grad a|^2 (dx^2+dy^2)/(mu^2 + lambda^2 a^2)`、精确临界集、零轨迹等于四圆、原点不可延拓、
  穿孔有限距离不完备
- **记号变化：** 无
- **引用处理：** 无
- **源中移除内容：** 无；「无 AES 数据附着于构型」的被取代陈述原地替换，OQ-085 与 OQ-086 被取代
  正文保留于那些问题内
- **构建结果：** `./build.sh 0` 产出干净最终日志的 78 页 PDF
- **审查者注：** 两构造写出前数值验证（并多项式精确临界集；传输元；轴长 `0 -> eps` 等于
  `4 eps^6` 如渐近预测）

## 迁移 M-0022

- **日期：** 2026-09-22（当日第三次修订）
- **名称：** Paper 0 开放项 OI-6 与 OI-3 解决
- **权威：** 普通任务报告；无范围变化
- **来源与目的地：** `paper-0/sections/09-contact-of-tearing.tex` 与
  `paper-0/sections/11-holed-aes.tex`（原地编辑）；`paper-0/README.md`、
  `governance/05b-paper-0-status-register.md`、`governance/08-open-questions.md` 与
  `governance/paper-0-closure-report.md` 更新
- **迁移状态：** `EXTEND`（现有章节内新结果）；无移动
- **论断处理：** 五个新节点，全部 `PROVED`：`prop:p0-curvature-form` 与
  `rem:p0-curvature-invariance`（§9）；`thm:p0-punctures-are-critical`、`rem:p0-puncture-hypothesis`
  与 `cor:p0-puncture-count`（§11）。OQ-082 对光滑延拓赋值解决且其非延拓情形重开为 OQ-088。
  `thm:p0-four-circle-model` 结束段修正：其穿孔集现证明为被迫而非规定
- **数学内容：**
  OI-6 --- 水平分布括号缺陷在分布上定义规范 2-形式 `omega`，由分布与 charge 投影决定且对 `alpha`
  归一化不敏感；其在 `h`-正交框架上的值是 `mu*lambda`，`h -> rho^2 h` 下重标律 `rho^{-2}`；数据
  AES 侧同一数字是无图表达式 `da([X_u,X_v])`。故 `mu*lambda` 非接触不变量，但也不是规范产物，论文
  现命名其精确不变群。
  OI-3 --- 对赋值光滑延拓到环境曲面的穿孔 AES，穿孔集恰是赋值临界集：规范、唯一且仅由 `a` 决定。
  Paper I 盘模型被排除因其赋值在穿孔非 `C^1`；该假设现显式且其情形重开为 OQ-088
- **记号变化：** 无
- **引用处理：** 无
- **源中移除内容：** 无；陈述四圆模型穿孔为规定的错误句被替换，OQ-082 被取代默认规则保留于该
  问题内
- **构建结果：** `./build.sh 0` 产出干净最终日志的 80 页 PDF
- **审查者注：** 并多项式临界半径写出规范化定理前数值重验（`0, rho, sqrt2 rho, sqrt3 rho`），因
  该定理假设恰区分那些赋值在穿孔临界的模型

## 迁移 M-0023

- **日期：** 2026-09-22（当日第四次修订）
- **名称：** Paper 0 开放项 OI-2 解决
- **权威：** 普通任务报告；无范围变化
- **来源与目的地：** `paper-0/sections/11-holed-aes.tex`（小节「跨穿孔撕裂」重写且其开放问题
  收窄）；`paper-0/README.md`、`governance/05b-paper-0-status-register.md`、
  `governance/08-open-questions.md` 与 `governance/paper-0-closure-report.md` 更新；
  `AEG-Paper-0-review-2026-09-22-response-v0.1.md` 获带日期状态节
- **迁移状态：** 一小节 `REWRITE`（此前不证明任何且登记两问题）加 `EXTEND`；无跨论文移动
- **论断处理：** 四个新节点，全部 `PROVED`：`prop:p0-tearing-puncture-independent`、
  `prop:p0-surface-does-not-close`、`prop:p0-no-puncture-holonomy`、
  `prop:p0-puncture-local-picture`。OQ-089 同修订开启并关闭且其解决记录，§11.6 第二开放问题收窄
  到赋值不延拓模型（OQ-088）
- **数学内容：**
  (a) `tau` 只依赖两词，故穿孔或改变实现不变；撕裂因此由 ACS 面积度量而非 holonomy。
  (b) *任何*正则 AES 中矩形两排序终止于赋值相差 `mu*h*(e^{lambda k}-1) != 0` 的点，故流路径不围
  出曲面区域；ACS 比较在每个模型（穿孔或否）规范。
  (c) 穿孔周围无规范 holonomy：水平集叶层可积（平坦），弯曲联络需附加数据，规范穿孔模型赋值单值
  故无单值。
  (d) 穿孔局部几何计算：小圆上八个变号零集支、八个交替符号扇区（负者是沿坐标轴尖点）、共形类
  延拓而度量不，穿孔在有限 `g` 距离
- **记号变化：** 无
- **引用处理：** 无
- **源中移除内容：** 前小节两个登记问题由答案替换；被取代文本 git 可恢复且其实质保留于 OQ-089
- **构建结果：** `./build.sh 0` 产出干净最终日志的 82 页 PDF
- **审查者注：** 八交叉与符号交替断言写出前数值验证；早草稿「零支仅触原点」陈述错误且由计算
  修正（沿轴尖点带负赋值）

---

## 迁移 M-0024

- **日期：** 2026-09-29
- **名称：** 外部审查 `thm:p0-punctures-are-critical` 后治理修正案；四笔记加入储备
- **权威：** 普通任务报告；无范围变化，**无论文源编辑**。此条目记录登记修正案，非手稿修订。
- **来源与目的地：** 新文件 `notes/foundations-and-geometry/07`、`08`、`09` 与 `10`（`.tex`）；仓库
  根新文件 `AEG-Paper-0-review-2026-09-29-thm-punctures-are-critical-v0.1.md`；
  `governance/notes-reserve-audit.md`（修正到版本 1.1）、`governance/05b-paper-0-status-register.md`
  （修正到版本 1.1）、`governance/08-open-questions.md`（OQ-082 与 OQ-088 修正）更新。`paper-0/**`
  **未变**。
- **迁移状态：** 储备与登记的 `EXTEND`；无跨论文移动，无断言提升。
- **论断处理：** 四笔记，全部未纳入且探索性，除 `10` 是 `EVIDENCE RECORD` 外全部定级
  `WORKING-NOTE PROVED`（`notes-reserve-audit.md` §2.1、§4 Tiers A 与 E）。一次状态**降级**：
  `thm:p0-punctures-are-critical` 与 `cor:p0-puncture-count` 从 `PROVED` 按打印移到
  `UNSUPPORTED AND EXCLUDED`，修复形式记录为 `PROVED WITH STATED HYPOTHESES`；
  `rem:p0-puncture-hypothesis` 移到 `PARTIALLY PROVED`。新台账条目 C-10。OQ-082 重开；OQ-088 修正。
  无新 OQ 开启。
- **数学内容：**
  (a) ACS charge 端点与 AES 仿射算子的联合商 `G = R_A x Aff^+(1,R)`、其特征中心与导出子群、其两
  投影与纤维积 `G = E^2 x_R H^2`，以及不可积性是序缺陷的接触形式 `alpha = dB - dA - B dM`（笔记 07）。
  (b) `G` 的无损实现恰在 `H^2 x R` 与 `SL~_2(R)` 存在；其余六 Thurston 模型排除；Paper 0 §9 接触
  模型在 Reeb 单位扩张与反演后是 `SL~_2(R)` 几何（笔记 08）。
  (c) `Aut(G) = F_{alpha,gamma,delta,kappa}`；扩张是外的；外层移除两个平移方向而内层不；`gamma != 0`
  由 `log` 非半代数与点稳定子论证阻碍（笔记 09）。
  (d) `thm:p0-punctures-are-critical` 验证反例：带光滑延拓赋值、`S = {0}`、`Crit(atilde) = emptyset`
  与不延拓度量的穿孔 AES。证明第一步构建新度量并当作给定 `g` 延拓；`def:p0-punctured-aes` 条件
  (ii) 要求延拓 `g` 本身。反向包含与 `thm:p0-four-circle-model` 不受影响（笔记 10、根审查）。
- **记号变化：** 无。
- **引用处理：** 无。
- **源中移除内容：** 无。`paper-0/**` 无删除；缺陷假设留在原地并在登记与 C-10 记录，使打印状态
  可恢复。
- **构建结果：** 四笔记 `pdflatex`（各三遍）编译，零警告零 overfull box：笔记 07 六页、笔记 08
  七页、笔记 09 五页、笔记 10 六页。笔记 10 嵌入验证脚本提取执行：14 断言通过。`./build.sh 0` 与
  `./build.sh 1` **未**运行且不受影响，因 `paper-0/`、`paper-1/` 或 `bibliography/` 下无文件改变；
  `paper0-build.yml` workflow 只对触及那些路径的 `pull_request` 触发且因此不为此变更运行。
- **审查者注：** 审查是外部的（DeepSeek Harness Agent）且降级凭独立重新推导与机器检查反例的力量
  记录，非凭审查者权威。笔记 07–09 每个恒等式经独立于产出它们的工作笔记的路径符号重证。
  **论文源刻意未修正**：是否在共形延拓假设下重述定理、加宽 `def:p0-punctured-aes` 或收窄断言留给
  作者，C-10 在该决定前保持开放。上构建结果行只记录实际执行；`build.sh` 此处未运行且此条目除陈述
  其不受影响外不断言它。

## H2 紧化与移植 AES 集成 — 2026-10-09

基线：`968c5c29557e8f7d70fe8baea2733726b852507d`。

- 带日期紧化研究结论 → Paper 0 规范节 `12-compactification.tex` 与附录 `app-E-circle-surgery.tex`，
  带独立论文内证明与显式几何/AES 边界。
- 可读候选手稿 *Ported Arithmetic Expression Spaces: Substitution, Execution, and Composition*，
  2026-10-09 v0.1 → Paper IV `05b-ported-aes-programs.tex`，在语境残差之后。适配现有记号、引用与
  论断台账；无原始对话复制。
- 9 月 29 日临界穿孔审查 → 活跃定理与依赖推论/注以共形背景假设的极小修正。原始审查与保留证据
  文件未变。
- 独立新回归脚本 → `paper-0/scripts/verify-compactification.py` 与
  `paper-4/scripts/verify-ported-aes.py`。原始 39/55 检查包不被表示为恢复或重跑。
- 无现有笔记、手稿节或归档产物被删除或移动。源覆盖、未解决产物恢复与验证在
  `h2-integration-2026-10-09.md`。

## Paper VI 过程几何摄入（2026-11-01）

- `notes/analysis-and-calculus/26`–`40`（Donaghey 变换、镜像/反演、PPCT 格、carousel 与 iota、
  规范选择）贡献 Paper VI 组合学；笔记原地且被引用，非移动。
- `research/iota-carousel/`（七个验证器与存储证据）与 `research/donaghey-orbits/` 供有限校准；其
  证据文件未变且由 CI 重放。
- `research/process-representation-gap/` 固定导入过程源：Adva 技术报告 `1b9bd090` 与 Process
  Geometry 数学核心 `c47c96fa`。两者在 `paper-6/aeg-paper-6.bib` 引用；无源文本复制进手稿。
- 新手稿是 `paper-6/`；其范围是 `governance/00e-paper-VI-process-geometry-scope.md` 且其论断登记
  于 `governance/05c-paper-VI-status-register.md`。Papers 0–V 无材料被本摄入删除、移动或提升。

## 有限域分析笔记摄入（2026-11-06）

**状态：** CANONICAL 研究笔记；无手稿集成或权威变化。来源：`mountain/math-notes` 于
`7ece14321b145fd7fa93e83342d432d355944b63`。目的地基线：AEG
`1d8633ac6e9e5fedfcba58e8a25065cf4cd32090`，checkout `/home/ubuntu/AEG/aeg-paper`。较旧
`/home/ubuntu/aeg-paper` 未动。

| 来源 | 目的地 |
| --- | --- |
| `finite-trig/finite-trig.tex` 与 PDF | `notes/analysis-and-calculus/48-finite-field-trigonometry.tex` 与重建 PDF |
| `conic-dynamics/conic-dynamics.tex` 与 PDF | `notes/analysis-and-calculus/49-conic-histories-and-finite-calculi.tex` 与重建 PDF |
| 两个 README、验证器、构建脚本与 `finite-trig/figures/` | `notes/analysis-and-calculus/finite-field-calculi/`，保留主题子目录 |
| 源 CC0 许可 | `notes/analysis-and-calculus/finite-field-calculi/SOURCE-LICENSE-CC0.txt` |

- 更新 `notes/README.md`、两篇文章互引用、图路径、可移植 Paper 0/I 引用与资源构建脚本；加联合
  构建入口与溯源/状态 README。原始作者归属、引用、标签、证明与数学假设保留。两个验证器与十二
  图源对源修订逐字节相同。
- 数学处理：迁移完整笔记而不加强断言。结果保留其所述假设；有限检查补充其证明。历史/域示例纳入
  Paper I 仍是结构提案。资源 README 与开放椭圆 AES 计划分开记录此状态；无主论文状态登记改变。
- 保留显式限制：普通算术异于射影求值；范一射影化加倍角；轨道长与系数特征控制本原归一化；非分裂
  运动不定义紧正则 AES。紧性阻碍的非空/紧/光滑/无边与实非零 mu 假设保留。
- 两个原始 math-notes 目录与其根 README 现指向 AEG。完整源历史在固定 commit 可恢复；有一个活跃
  维护之家。Octagons 留在 math-notes。无论文或归档改变。
- 验证：两个原始验证器通过（笔记 49：41 检查组）；全部十二图与两个编号 PDF 重建（29 与 9 页）。
  最终 LaTeX 日志无未定义引用/引用、重复标签、缺失资产或 overfull box。静态检查保留标签/引用/
  参考文献清单且解析每个内部引用与图。根 `build.sh` 只构建论文手稿；验证用独立笔记构建入口。
- 开放任务：一般奇 q 比较（平移有阶 p）、一个算子类内历史与普通域，与精确椭圆 AES 范畴。推荐
  下一步：在更广理论前审查四语境椭圆历史及其身份对域示例用于 Paper I。
- 发布顺序：先 commit 并 push AEG 目的地，再发布 math-notes 迁移指针，使其远程目标可用。
