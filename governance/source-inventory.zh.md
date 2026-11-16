# AEG 来源清单

**固定基线：** `134e70a74ed010024afa7439bd3931402731423a`  
**清单日期：** 2026-08-06  
**基线数量：** 207 个跟踪文件，含 107 个 `.tex` 源  
**Paper I 迁移后数量：** 123 个 `.tex` 源

**当前活跃源闭包：** Paper 0：17 个规范 `.tex` 文件（12 个节源、4 个附录、1 个入口）；
Paper I：9 个规范 `.tex` 文件；Paper II：13；Paper III：17；Paper IV：19

*2026-09-22 由迁移 M-0019 更新：Paper 0 吸收 Paper I 的几何章节与附录并增长为 12 节与 4
附录；Paper I 缩减为历史、射影、Hecke 与零层。*

本清单分类固定基线中的每个顶层路径族。族分类适用于命名目录下每个文件；例外显式列出。迁移
不删除或静默覆写任何遗留源。论断级溯源记录于 `migration-log.md`。

## 1. 规范与根级文件

| 路径 | 基线处理 | Paper I 处理 |
|---|---|---|
| `.dockerignore`, `.gitignore` | KEEP | 仓库卫生；未变 |
| `Dockerfile` | KEEP / VERIFY | 容器配方保留；任务环境 Docker 不可用 |
| `LICENSE` | KEEP | 未变 |
| `README.md` | REWRITE | 四论文入口与 DOI 区分 |
| `restructure/AGENTS.md` | KEEP / AUTHORITATIVE | 现整合为仓库范围根 `AGENTS.md` |
| `aeg-paper.tex` | REWRITE / CANONICALIZE | 由唯一活跃 Paper I 入口 `paper-1/aeg-paper-1.tex` 取代 |
| `aeg-paper-0.bib` | KEEP / CLEAN | 现为 `bibliography/aeg-paper.bib` 共享参考文献 |
| `aeg-paper.pdf` | REBUILD | 由规范产物 `paper-1/aeg-paper-1.pdf` 取代 |
| `build.sh` | STABILIZE | Papers I–IV 规范多论文构建 |
| `aeg-lemma.tex` | HOLD | 引用缺失的 13–17 节；无 Paper I 依赖 |

新规范源树恰为：

```text
paper-1/
  aeg-paper-1.tex
  sections/
    01-introduction.tex
    02-sequential-histories.tex
    03-projective-affine.tex
    04-affine-cocycles.tex
    05-affine-flow.tex
    06-hyperbolic-model.tex
    07-zero-geometry.tex
    08-acs-torsion.tex
    09-contact-curvature.tex
    10-conclusion.tex
  appendices/
    app-A-conventions.tex
    app-B-affine-cocycles.tex
    app-C-hyperbolic-calculations.tex
    app-D-acs-contact.tex
    app-E-equality-neutrality.tex
```

后续论文目的地记录 `paper-2/README.md`、`paper-3/README.md` 与 `paper-4/README.md` 相对于固定
基线是新的。Papers II–IV 此后已推进到规范活跃源闭包。Paper II 记录于第 6 节、Paper III 第 7
节、Paper IV 第 8 节。

## 2. 穷举基线族分类

| 基线族 | 文件 | 内容 | 状态 | 规范目的地 |
|---|--:|---|---|---|
| root | 11 | 元数据、Paper I 入口、参考文献、PDF、构建 | 混合，上文逐项 | Paper I / 仓库 |
| `sections/` | 13 | 遗留 `sec01.tex`–`sec12.tex` 源族 | ARCHIVAL | 与基线根手稿一起保留于 `archive/legacy-root-manuscript/`；审计部分在 `paper-1/sections/` 重新推导；分析 → II；管 → III；商 → IV |
| `restructure/` | 13 | 权威、范围、依赖、状态、编辑、验收、讨论 | KEEP / AUTHORITATIVE | 现 `governance/`；仓库治理控制面 |
| `revision-1/` | 13 | 备选八节 TeX 构建 | ARCHIVAL | 现 `archive/revision-1/`；无活跃定理权威 |
| `revision-2/` | 26 | 备选 TeX 构建、PDF、Lean 实验与报告 | ARCHIVAL / HOLD | 现 `archive/revision-2/`；形式化可单独审计 |
| `arxiv/` | 14 | 先前分发快照、样式、图、参考文献 | ARCHIVAL | 现 `archive/arxiv/`；DOI/版本溯源 |
| `paper4p/` | 2 | 短备选手稿与构建 | ARCHIVAL | 现 `archive/paper4p/`；无活跃定理权威 |
| `notes/` | 32 | 双边、解析、环、热、环、资源笔记 | HOLD / PARTIAL EXPORT | 审计代数 → I；分析 → II；奇异 → III；商/复杂度 → IV；现分类于 `notes/` 主题子目录 |
| `misc/` | 28 | 独立图/模型 TeX 与图像实验 | HOLD / ARCHIVAL | 现保留于 `images/sources/`；仅在公式与资产审计后复用——审计是 `figure-asset-audit.md` |
| `images/` | 26 | 21 PDF 与 5 PNG 渲染资产 | HOLD / SHARED ASSET ARCHIVE | 活跃 Paper I 构建无需任何；逐资产台账见 `figure-asset-audit.md` |
| `knots/` | 6 | 纽结/问题 TeX 加一个 PDF | EXPORTED / ARCHIVAL | 现保留于 `notes/knots-and-loops/`；Paper III 研究归档；无不变量断言 |
| `ideal_glass/` | 18 | 独立 PDF、TeX、Python 包、实验工具 | HOLD / INDEPENDENT | 现 `archive/ideal_glass/`；非 Paper I 依赖 |
| `plans/` | 2 | 历史原则与研究计划 | ARCHIVAL | 现 `archive/plans/`；活跃计划在 `governance/` |
| `styles/` | 2 | arXiv 与 quiver 样式 | ARCHIVAL | 现保留于 `archive/legacy-latex-styles/`；任何规范论文不加载 |
| `peddle/` | 1 | 独立 HTML 实验室 | HOLD / INDEPENDENT | 现 `archive/peddle/`；非 Paper I 依赖 |

固定基线无跟踪 `gpt/` 目录。规划文档中的 `gpt/` 引用因此被当作一般归档规则，而非缺失跟踪文件
的证据。

## 3. 扩展审计

| 扩展或类型 | 基线计数 | 处理 |
|---|--:|---|
| `.tex` | 107 | 1 个规范根入口、13 个遗留节、其余来源按上分类归档/HOLD |
| `.pdf` | 33 | 渲染/历史资产；根 PDF 从源重建 |
| `.png` | 7 | 历史/共享图像资产；活跃 Paper I 不加载 |
| `.md` | 19 | 仓库、重组、报告与形式化笔记 |
| `.py` | 11 | 独立 ideal-glass 实验；无 Paper I 构建依赖 |
| `.lean` | 6 | `revision-2` 下实验形式化；非 Paper I 证明权威 |
| `.sh` | 6 | 根与备选构建脚本；只有根 `build.sh` 规范 |
| `.sty` | 4 | 历史样式；活跃 Paper I 只用安装包 |
| `.bib` / `.bbl` | 2 / 1 | 基线根 `aeg-paper-0.bib` 加 arXiv 快照；共享参考文献现于 `bibliography/` |
| 其他仓库/配置文件 | 11 | 许可、忽略、Docker、HTML、JSON、TOML、文本、工具链，以及历史 ideal-glass 树中的一个 `.DS_Store` |

## 4. 活跃依赖闭包

活跃 `paper-1/aeg-paper-1.tex` 只包含 `paper-1/sections/` 与 `paper-1/appendices/` 下的 15 个
文件，随后是共享 `bibliography/aeg-paper.bib`。它不包含遗留 `sections/sec*.tex`、备选手稿、
外部图像或历史样式。这使 Paper I 构建依赖闭包显式，并防止后续论文材料经隐式 include 重新进入。

## 5. 保留规则

`ARCHIVAL`、`EXPORTED` 与 `HOLD` 意为「从规范 Paper I 构建排除」，而非「丢弃」。每个迁移陈述
在其记录的当前目的地仍可用，仅路径归档移动被记录，使溯源保持可恢复。

当前非规范研究材料布局是：

```text
images/
  sources/                         # 旧 misc/ 图与模型来源
archive/
  legacy-latex-styles/             # 旧 styles/ 第三方 TeX 样式
notes/
  analysis-and-calculus/
  computation-and-resources/
  foundations-and-geometry/
  knots-and-loops/                 # 含旧 knots/ 树
  projective-condensation/
  thermodynamics-and-renormalization/
```

此分类只改变路径。它不把任何笔记或图来源提升为定理权威，也不把任何文件加入规范论文构建闭包。

## 6. 规范 Paper II 源树

受控 Paper II 迁移恰好添加以下活跃源闭包：

```text
paper-2/
  aeg-paper-2.tex
  sections/
    01-introduction.tex
    02-analytic-data.tex
    03-surface-operators.tex
    04-contact-analysis.tex
    05-pullback-cylinder.tex
    05-hyperbolic-analysis.tex
    06-poisson-dirichlet.tex
    07-boundary-energy.tex
    08-conclusion.tex
  appendices/
    app-A-frame-calculations.tex
    app-B-contact-calculations.tex
    app-C-poisson-fourier.tex
```

Paper II 入口只输入这十二个节/附录文件与 `bibliography/aeg-paper.bib` 共享参考文献。它通过
引用与重述导入 Paper I 陈述，而非 TeX 包含。无遗留 `sections/sec*.tex`、归档、笔记、Paper III
或 Paper IV 源属于其构建依赖闭包。公式级溯源与论断处理记录于 `paper-II-source-audit.md` 与
`decisions-paper-II.md`。`05-pullback-cylinder.tex` 是闭包后添加，激活正则解析桥：平面调和 AES、
局部双全纯拉回、完备柱面 AES 及其酉/反演下降。其分支与临界轨迹被明确排除并传递给 Paper III。

## 7. Paper III 集成增补

当前 Paper III 源闭包是：

```text
paper-3/
  aeg-paper-3.tex
  sections/
    01-singular-aes.tex
    02-local-zero-models.tex
    03-multi-zero-constructions.tex
    04-arithmetic-zero-networks.tex
    04-parameter-discriminants.tex
    05-q4-geodesic-knots.tex
    05-polynomial-threaded-carriers.tex
    05-sextic-ll-laboratory.tex
    05-history-divisor-naturality.tex
    05-regular-tubes.tex
    06-singular-fibers.tex
    07-monodromy-and-braids.tex
    08-threading-and-knot-questions.tex
  appendices/
    app-A-regularity-and-properness.tex
    app-B-configuration-and-braid-background.tex
    app-C-affine-quandle-calculations.tex
```

入口只输入这十六个节/附录文件与 `bibliography/aeg-paper.bib` 共享参考文献。它通过引用接口导入
Papers I 与 II，而非 TeX 包含。无遗留 `sections/sec*.tex`、笔记、纽结文件、杂项图来源、归档手稿
或重组讨论属于活跃 Paper III TeX 依赖闭包。

历史源与 Git 历史审计记录于 `paper-III-source-audit.md`。其核心溯源发现是：在 249 个可达 commit
中无可验证的一般多重零构造、已定义一般 `E_k` 或显式历史 AEG `E_log` 构造。活跃手稿中的平行
多重零、对数覆盖、螺旋管、Morse、分支、辫实现与有限域构造因此是 `REDERIVED HERE`；遗留文件
仍为 `ARCHIVAL` 或 `HOLD`。

闭包后文件 `04-arithmetic-zero-networks.tex` 添加单独审计的算术–自守层。它含精确 (q=4)
Hecke–Hauptmodul 奇异 AES、符号特征下降，以及对提供首一一般平方自由多项式的标准相对除子分解。
三角群一致化与数论背景是引用外部输入；AEG 拉回与零网络公式是 `REDERIVED HERE`。无一般历史到
除子函子被加入证明闭包：该箭头仍是开放问题。此添加不改变 `E_k` 或 `E_log` 的否定历史发现。

随后 `05-q4-geodesic-knots.tex` 与 `05-history-divisor-naturality.tex` 添加形成符号覆盖/寄存器
扩展。第一个把同一符号特征覆盖与完备粗柱面等同，并在保留双曲 orbifold 与应用声明尖点填充后与
`S^3` 中 `T(2,4)` 的补等同；它还记录算子级周期轨道映射与被引用的零脊柱/模板编码。第二个证明
二次与四次提供寄存器模型、标记迹、极点余循环、坍缩核与 Frobenius 字典。Dehornoy 与
Dehornoy–Pinsky 提供经典测地流输入；AEG 覆盖识别与寄存器综合在活跃手稿中重新推导。两个文件
都不改变否定历史发现或关闭一般历史到素除子与纽结不变量问题。

后来的 `05-polynomial-threaded-carriers.tex` 添加是新推导，不是恢复的历史源。它证明提供族
`Im(z^2-t^m)=0` 带内在根线 `z^2=t^m`、其载体拓扑、判别式/框架/辫恒等式、q=4 标记环面特化与
对数正切加权锥。它还给出一个提供的四股中心扩张校准，同时留下无限制标记历史系数路径函子开放。
算术二次扭曲、径向载体与路径选择仍是显式论断边界。

随后 `05-sextic-ll-laboratory.tex` 添加是显式实验室，不是恢复的历史源，也不是多项式族的一般
理论。它从提供稀疏六次 `P_0(x)=x^6-x` 出发，计算其临界值五次、载体墙、六根线、亏格二双重
覆盖、混合辫正合序列与一个算术纤维。有限平展 Lyashko–Looijenga 覆盖、其次数、转置因式分解
计数、Birman–Hilden 提升、Picard–Lefschetz 与辛单值，以及算术 Galois/自同态判据是引用的经典
输入。正则 LL 纤维中的 `1296` 点是坐标归一化首一中心六次；自由残差 `mu_6` 源旋转有 `216` 个
轨道。两个数都不被断言计数非同构亏格二曲线。一个精确第二叶现在证明模像至少含两点：它与
(x^6-x) 有相同事件多项式，但在 (t=1) 有不同的亏格二 Igusa 读数。同一来源给出商覆盖谱多项式与
迹–范下降、规范平均/零和序列，以及带精确正下界的单值不变遗忘方差。它不断言沿任意开 LL 路径
恒常。沿两条显式切片铅笔不变比是 ((t-\beta)/t)^5，带平衡正则纤维除子 (5[\beta]-5[0])；这是
对数电荷，不是有限 Dirichlet 能量。完整 (216) 轨道普查、算术/周期比较、标记单值与 Hodge/Siegel
能量精细化，以及从无限制 AEG 历史到 LL 拉回或其 Hurwitz 群胚的每个函子仍开放。

显示对的精确证书在 TeX 闭包之外单独跟踪于
`paper-3/computations/ll-igusa-twin/verify-explicit-twin.py`，其调用与论断边界在相邻 `README.md`。
此可复现性产物不改变规范 Paper III TeX 输入计数。

此增补取代先前 Paper III 仅由范围/溯源 README 组成的清单陈述。它不改变上述固定 Paper I 基线
计数。

## 8. 规范 Paper IV 源树

当前 Paper IV 源闭包含 `paper-4/aeg-paper-4.tex`、`paper-4/sections/` 下十四个编号节文件与
`paper-4/appendices/` 下四个技术附录，共十九个规范 TeX 文件。它使用 `bibliography/aeg-paper.bib`
共享参考文献与独立有限验证脚本 `paper-4/scripts/verify-paper4.py`。

无遗留节、研究笔记、归档手稿或治理讨论是活跃 TeX 依赖。来源审计、数学决定、红队审查与闭包
边界记录于 `paper-IV-source-audit.md`、`decisions-paper-IV.md`、`paper-IV-red-team-report.md` 与
`paper-IV-closure-report.md`。
