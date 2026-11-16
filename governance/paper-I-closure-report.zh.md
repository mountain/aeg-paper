# Paper I 闭包报告

**手稿：** *Arithmetic Expression Geometry I: Foundations*  
**状态：** 数学审查手稿  
**闭包日期：** 2026-08-06  
**审计基线：** `134e70a74ed010024afa7439bd3931402731423a`

本报告记录 Paper I 重组任务的结果。它应与 `audit-report.md`、`source-inventory.md`、
`migration-log.md` 与 `decisions-paper-I.md` 一起阅读。下文「已闭包」指在论文实际打印的
假设下对数学审查手稿闭包。它不意味着 Papers II–IV、作者发布批准或 DOI 出版工作已完成。

**闭包后说明：** 第 8 节记录后来的算术–自守集成，第 9 节记录 M-0006 接口重建；第 1–7 节
保留原始 60 页闭包证据。

## 1. 验收结果

- **仓库基线：** 已闭包。固定基线、备选手稿树、历史笔记、图件、样式、构建脚本与参考文献
  被清点。未修改的基线构建失败与过期的跟踪 PDF 在构建脚本被改动前被记录。
- **结构迁移：** 已闭包。活跃入口包含十个基础节与五个附录，且只输入新的
  `paper-1/sections/` 与 `paper-1/appendices/` 树。未删除任何遗留源。
- **数学闭包：** Paper I 已闭包。每个命名基础定理与定义槽位带精确假设存在；定理类结果在
  活跃手稿或支持附录中有证明。
- **编辑闭包：** 数学审查已闭包。258 词摘要与结论已对照已证明正文结果检查；全部八个计划
  概念图作为可复现 TikZ 存在。
- **发布状态：** 尚未是作者批准的发布。任务环境中 Docker 不可用，作者仍须批准单位、日期、
  版本声明与较早 Zenodo DOI 的关系。

## 2. 基础定理清单

| 领域 | 稳定标签 | 活跃源 | 闭包 |
|---|---|---|---|
| 顺序分类与历史 | `thm:sequential-tree-classification`、`def:marked-spinal-history` | 第 2 节 | 已证明 / 已定义 |
| 射影求值与生成 | `def:projective-evaluation`、`thm:bilateral-pgl2-generation`、`cor:affine-borel-sector` | 第 3 节；附录 A | 已证明 / 已定义 |
| 仿射余循环与微分 | `prop:affine-cocycle-formulas`、`prop:target-affine-cocycle`、`prop:source-normalized-cocycle`、`prop:left-right-affine-differentials` | 第 4 节；附录 A–B | 已证明 |
| 连续仿射流与正则 AES | `def:regular-aes`、`thm:continuous-affine-flow` | 第 5 节 | 已证明 / 已定义 |
| 基本双曲模型 | `thm:basic-hyperbolic-aes`、`prop:laplace-eigenfunction` | 第 6 节；附录 C | 已证明 |
| 正则与奇异零点 | `thm:regular-zero-locus`、`def:singular-aes`、`prop:regular-total-zero-set` | 第 7 节；附录 C | 已证明 / 已定义 |
| ACS 与全局 torsion | `def:acs`、`def:relative-torsion`、`thm:torsion-stokes` | 第 8 节；附录 D | 对正加–尺度历史已证明 / 已定义 |
| 接触与水平曲率 | `prop:contact-form`、`thm:contact-curvature`、`prop:horizontal-differential-curvature` | 第 9 节；附录 D | 已证明 |

目标框架与源归一化余循环的依赖图别名附着于组合余循环命题。普通算术求值、射影求值、charge
求值、端点相等、镜像、时间反演与路径逆始终被区分。

## 3. 已闭包的数学决定

`08-open-questions.md` 的 Part XIV 台账闭包每个 Paper I P0 项与本手稿使用的章节阻塞 P1 项。
特别是：

1. 历史是年代词，列向量 Möbius 作用下 `rho(gamma delta)=rho(delta)rho(gamma)`；
2. 双边非退化语境在每个域上生成 `PGL_2(K)`，无穷稳定子是仿射 Borel 扇区；
3. 正则 AES 数据是带导出算术框架的内在 eikonal 数据；
4. 双曲模型由归一化左不变度量导出，无唯一性断言；
5. 正则零点与奇异零点被范畴式分开；
6. 相对 torsion 对尺度相容的正加–尺度历史定义，加权 Stokes 需要 charge 相容与定向
   `dA wedge dM`；
7. 有限目标框架开缺陷、源归一化闭漂移与其共同无穷小接触曲率在有限尺度不被等同。

## 4. 构建与静态验证

`build.sh` 编码的严格命令序列以 TeX Live 2023 执行：

```text
pdflatex -halt-on-error -file-line-error -interaction=nonstopmode aeg-paper-1.tex
bibtex aeg-paper-1
pdflatex -halt-on-error -file-line-error -interaction=nonstopmode aeg-paper-1.tex
pdflatex -halt-on-error -file-line-error -interaction=nonstopmode aeg-paper-1.tex
```

任务运行器在沙箱退出时物化对生成二进制的重复写入，故最终证据运行把相同四阶段作为独立
进程调用执行。这避免运行器特定的 overlay 竞争，且不改变仓库构建程序。

最终产物：

| 属性 | 值 |
|---|---:|
| PDF | `paper-1/aeg-paper-1.pdf` |
| 页数 | 60 |
| 页面尺寸 | US letter，612 x 792 pt |
| PDF 版本 | 1.5 |
| 文件大小 | 575,584 bytes |
| SHA-256 | `98a8a9a2f35cbb2252cfc9576d447ca427a27f95815deaab03d3e3c9f7c04911` |

静态与渲染检查：

- 166 个唯一活跃标签；无重复标签；
- 每个活跃 `ref`、`eqref` 与 `autoref` 目标存在；
- 每个引用键存在于当时根共享 `aeg-paper-0.bib`；
- 每个命名稳定定理/定义槽位存在；
- 8 个 figure 环境，全部内联 TikZ，无缺失资产；
- 最终日志无 LaTeX 或 BibTeX 警告、未定义引用、未定义引用、overfull box 或 underfull box；
- 活跃手稿无未解决 TODO/FIXME 标记；
- 全部 60 页以 Poppler 渲染；标题/摘要、目录、全部八页图、附录与参考文献被视觉检查剪切、
  碰撞与不可读标签。

任务环境中未安装 Docker。现有 `Dockerfile` 原样保留；容器验证仍是发布检查而非未报告的成功。

## 5. 独立审查记录

集成手稿接受了以下内容的独立只读审查：

- 代数章节与复合/矩阵约定；
- 流、度量、双曲、零轨迹与奇异模型计算；
- ACS 定向、加权 Stokes、有限缺陷与接触曲率；
- 全手稿数学一致性；
- Paper I 范围、摘要/结论可追溯性与后续论文边界；
- 渲染 PDF 布局与概念图。

那些审查的所有阻塞发现都被修复并重新检查。最终数学与范围审查报告零阻塞缺陷。

## 6. 为后续论文保留的范围

Paper I 不声称完整算术全纯函数理论、一般多重零或管分类、辫/纽结不变量、完整射影凝聚商塔
或计算下界。那些材料保留其溯源并分别分配给 Paper II、III、IV 范围记录。当前手稿只证明
那些后续计划所需的接口。

## 7. 剩余人工发布动作

在把本手稿称为公开发布候选之前，作者应：

1. 在干净 checkout 与保留的 Dockerfile 中构建提交的 commit；
2. 批准作者、单位、邮箱、日期与版本元数据；
3. 决定此前 Zenodo 记录是否及如何指向新版本；
4. 审查草稿 pull request 并授权非草稿发布状态。

## 8. 闭包后算术–自守修正案（2026-08-06）

本修正案记录一个后来的集成检查点，且不重写第 4 节 60 页产物证据，后者仍是原始闭包运行的
证据。活跃依赖形态仍是十节与五附录；未引入额外 Paper I 源文件。入口与第 1、3、7、10 节
现在使算术–自守导出显式。

| 扩展节点 | 活跃陈述 | 来源与状态 |
|---|---|---|
| P1-H1 / P1-H2 | 射影语境 `T_sqrt(2)` 与 `J=-1/z` 生成 `q=4` Hecke 算子子群，带精确射影四阶 | `prop:hecke-four-arithmetic-relation`，第 3 节；矩阵计算加被引用的标准群识别 |
| P1-Z9 | 每个连通、完备、无边正则 AES 微分同胚于 `Z(a) x R`；其赋值满射且其零集非空连通 | `thm:complete-regular-aes-splitting`，第 7 节；由矫正与完备单位梯度流证明 |

相等层级仍是定理边界的一部分：字面词、标记历史、诱导射影算子、Hecke 关系、胞腔稳定子
陪集与端点不被等同。穿过 `0` 或无穷的射影延拓不认证普通算术计算。分裂是光滑而非等距的，
且不适用于不完备度量或带边流形。因此它提供下游所需的精确全局 no-go 结果：分支 Hecke 零
网络不能是一个连通、完备、无边正则标量 AES 的零集，但它可在声明的奇异、不完备、边界或
更高秩机制后出现。

对 `sqrt(2)` 的特化、矩阵关系与分裂证明是活跃手稿内部结果。常规 Hecke 群识别与连分数背景
使用新引用的主要来源。Paper I 不声称 Hauptmodul、dessin、分支度量或历史到除子函子；那些是
下游接口。

最终统一仓库构建以以下当前证据产出修正后的 Paper I 产物：

| 属性 | 当前集成产物 |
|---|---:|
| 页数 | 63 |
| 文件大小 | 604,976 bytes |
| SHA-256 | `bbcb16fa720c26f837555ff2387ee7205884a8f07963c6f949e19cb636710fd5` |
| 活跃标签 | 177 unique |
| 引用键使用 | 6 unique |

最终日志无 LaTeX 或宏包警告、未定义引用或引用、overfull 或 underfull box、重复标签或致命
诊断。此表只取代活跃集成快照的产物元数据；上述原始 60 页闭包证据仍是历史记录。

## 9. M-0006 接口重建（2026-08-06）

Paper I 在 M-0006 中不接受新定理或源文件。第 10 节现在命名其 q=4 算子导出的已证明下游
用途：Paper III 从本原双曲算子类过渡到经典周期轨道纽结，同时保留标记历史、算子、共轭类与
纽结之间的区分。这不把 Paper I 变成纽结论论文，也不关闭历史到除子问题。

该接口编辑后的统一仓库构建产出：

| 属性 | M-0006 集成产物 |
|---|---:|
| 页数 | 63 |
| 文件大小 | 604,948 bytes |
| SHA-256 | `9144f603f9452f09ecaf9e9c32e15029b33992cf0837073580a9d3f7188de2d9` |
| 活跃标签 | 177 unique |
| 引用目标 | 88 unique，全部存在 |
| 引用键使用 | 6 unique，全部存在 |

规范日志与 BibTeX 日志无警告、未定义引用或引用、overfull 或 underfull box 或致命诊断。
三页改变的结论页被渲染并视觉检查，无布局缺陷。
