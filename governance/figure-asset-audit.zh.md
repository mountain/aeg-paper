# 图资产审计

**文件：** `governance/figure-asset-audit.md`
**状态：** 审计记录（`images/` 与 `images/sources/` 的清单与缺陷登记；非权威，不修订范围，不
删除任何内容）
**版本：** 1.0
**日期：** 2026-11-11
**拟定：** DeepSeek Harness（AI 编码代理），在仓库作者指导下工作。本审计不改变任何数学状态、
范围陈述或论断等级。
**依赖：**

* `AGENTS.md`
* `governance/source-inventory.md`
* `governance/06-editorial-rules.md`

**适用于：** `images/` 下每个渲染资产与 `images/sources/` 下每个来源——该目录继承了旧 `misc/`
族。

---

## 1. 溯源与数量

| 位置 | 内容 | 实测计数 | 记录计数 |
|---|---|---:|---:|
| `images/` | 渲染资产 | 21 PDF + 5 PNG = 26 | 26 |
| `images/sources/` | 旧 `misc/` 来源 | 27 `.tex` + 2 `.png` = 29 | 28 |

`misc/` 图比 `source-inventory.md` 第 2 节记录的计数高一个。本审计未添加文件；差异被记录而非
调和，遵循「冲突计数被记录而非静默调整」的规则。

`images/` 与 `images/sources/` 是 `HOLD / ARCHIVAL`。`source-inventory.md` 第 4 节已确立无规范
论文包含外部图像：Paper 0 构建闭包是其 12 个节文件、6 个附录与共享参考文献。Paper 0 当前
打印的每个图都是内联 `tikzpicture` 源。

## 2. 来源到资产台账

尺寸是 72 pt/英寸的自然 PDF box，故记录每个资产若不缩放放置时的尺寸。纵横比是宽除以高。

| 来源 | 资产 | 尺寸 (in) | 比 | 注 |
|---|---|---:|---|
| `01-grid-example-1.tex` | `01-grid-example-1.pdf` | 6.77 x 3.72 | 1.82 | 带赋值标签的直线网格 |
| `02-example-expression-syntax-tree.tex` | `02-....pdf` | 1.48 x 1.67 | 0.89 | 唯一竖版资产；小、无害 |
| `03-...-left-right.tex` | `03-....pdf` | 4.10 x 1.74 | 2.35 | 串与树，两个梳 |
| `04-...-combination.tex` | `04-....pdf` | 1.96 x 1.95 | 1.01 | 混合梳 |
| `05-example-expression-embedding.tex` | `05-....pdf` | 6.77 x 4.06 | 1.67 | 网格加一条嵌入路径 |
| `06-example-canonical-form.tex` | `06-....pdf` | 6.77 x 4.56 | 1.49 | 四条历史、一个端点 |
| `07-grid-detail.tex` | `07-grid-detail.pdf` | 6.85 x 3.72 | 1.84 | 带显式赋值值的网格 |
| `08-grid-schema.tex` | `08-grid-schema.pdf` | 7.58 x 3.78 | 2.01 | 超过 6.5 in 版心 |
| `09-grid-schema-g1.tex` | `09-grid-schema-g1.pdf` | 7.58 x 3.78 | 2.01 | 超过 6.5 in 版心 |
| `10-gca.tex` | `10-gca.pdf` | 2.94 x 1.76 | 1.67 | 小依赖图 |
| `11-horocyclebased.tex` | `11-horocyclebased.pdf` | 3.34 x 3.16 | 1.06 | 盘的饱和红填充 |
| `12-proofbymapping.tex` | `12-proofbymapping.pdf` | 7.01 x 3.16 | 2.22 | 两面板，继承红填充 |
| `13-tube1st.tex` | `13-tube1st.png` | 2120 x 955 px | 2.22 | 渲染为栅格，继承红填充 |
| `14-apeirogon.tex` | `14-apeirogon.png` | 2400 x 1800 px | 1.33 | 栅格图上绘轴 |
| `17-area-formula.tex` | `17-area-formula.pdf` | 10.45 x 6.48 | 1.61 | 大幅超过版心 |
| `18-grid-example-2.tex` | `18-grid-example-2.pdf` | 6.77 x 3.72 | 1.82 | 资产早于其来源 |
| `cayley-tree-4-border.tex` | `cayley-tree-4-border-2..5.pdf` | 0.85 到 3.61 方形 | 1.00 | 一个来源、四个资产 |
| `cayley4.tex` | `cayley4.pdf` | 4.83 x 4.83 | 1.00 | Lindemayer 树 |
| `knot_4_1.tex` | `knot_4_1.pdf` | 10.30 x 6.48 | 1.59 | 大幅超过版心 |

## 3. 缺陷登记

### 3.1 `18-grid-example-2.pdf` 与其来源不对应

来源日期 2025-12-06，带约三十五个红色数值标签；资产日期 2025-07-12。以 250 dpi 渲染资产
确认这些标签无一个存在。资产是来源早期修订的快照，不是当前渲染。

**处理：** 记录，不重建。重建会用从未分发的东西替换归档产物。任何未来使用必须从来源重构
图，而非包含此 PDF。

### 3.2 字节相同重复来源

`01-grid-example-1.tex` 与 `15-domain2.tex` 相同（`md5 2b86636918fd8f9aca1f23d3f7164826`）。
只有 `01` 有资产，故 `15` 是死重，但带名称 `domain2`，记录文件不再表达的一个意图。

**处理：** 两者保留。删除重复会擦除名称 `domain2`；保留一个冗余文件比失去该记录更便宜。

### 3.3 无来源的资产

`cayley.pdf`、`jigsaw-riemann.png`、`sine2d.png`、`t4096.png`。

`cayley.pdf` 不是 `cayley4.tex` 的输出，后者以不同尺寸产出 `cayley4.pdf`。三个 PNG 是蒙太奇
或大渲染，无记录生成器。它们都不能从此仓库重新生成。

**处理：** 作为唯一幸存记录保留；标记为不可复现。

### 3.4 无资产的来源

`08-uniformazation.tex`、`15-domain2.tex`、`16-localdomain.tex`、`19-curl.tex`、
`20-grid-example-3.tex`、`charts.tex`、`prism-torus.tex`、`square-fractal.tex`。

那是二十七个来源中的八个。第九个来源 `cayley-tree-4-border.tex` 确有资产，但名称来源不含：
它硬编码 `\numsteps=2`，而 `2..5` 有资产，故其四个渲染中的三个无法在不编辑来源文本的情况下
重新生成。第 2 节台账在它拥有的资产下把它列一次。

八个中的两个按交付无法编译，不仅是未渲染：

* `08-uniformazation.tex` 含空 `tikzpicture`，不产出任何东西。
* `16-localdomain.tex` 在 `standalone` 文档中用 `\textwidth` 调整图像，并引用
  `ii2_symmetry.png`（位于 `sources/`，非 `images/`）；两个选择都假设仓库未固定的构建目录。

其余六个是普通未渲染来源，只在从它们重构图时有用于，而非包含。

### 3.5 宽于正文版心的资产

`letterpaper` 与 `margin=1in` 下版心是 6.5 in。`17-area-formula`（10.45 in）与 `knot_4_1`
（10.30 in）超过它一半以上；`08-grid-schema` 与 `09-grid-schema-g1`（7.58 in）略超。

把 `17` 缩进版心花 0.62 因子，使其红标签从约 7 pt 到约 4.3 pt。这是此族无资产能被
`\includegraphics` 包含而不重设计的原因。

### 3.6 饱和填充

`11`、`12`、`13` 与两个栅格蒙太奇把盘画为 `\draw[red,fill=red] ... circle[radius=4]`，一个
覆盖 horocycle 族与点标签的实心红盘。填充作为标记盘为区域的意图是合理的；饱和不是，且
不能存活打印。

### 3.7 重复网格体

约 110 行的基础网格被逐字复制到 `05`、`06`、`07`、`15`、`20`，`11` 的盘被复制到 `12`、`13`。
网格变更必须最多在六处进行。

## 4. 归档状态

每个条目保持 `HOLD / ARCHIVAL`。`images/` 或 `images/sources/` 中任何内容不得进入规范构建
闭包。以下清单对未来工作有约束力。

| 使用 | 允许 |
|---|---|
| 把资产 `\includegraphics` 进论文 | 否，除非本文件有记录例外 |
| 引用来源文件、按论文内联风格重构图 | 是 |
| 删除来源或资产 | 否，除非 `migration-log.md` 有条目 |
| 从来源重建资产 | 否，除非资产先被保留 |

## 5. Paper 0 中的重构

Paper 0 中的四个图由此归档重构而非包含。每个带命名其来源文件的注释。

| Paper 0 图 | 标签 | 派生自 | 所做变更 |
|---|---|---|---|
| Figure 4 | `fig:p0-halfplane-disc-dictionary` | `11`, `12` | 轻面板填充替代饱和盘；两族按颜色与面板标题分开 |
| Figure 6 | `fig:p0-affine-vs-projective-cell` | `01`, `18` | 缩减到 Bruhat 分解所分离的两曲线族 |
| Figure 8 | `fig:p0-same-charge-different-histories` | `06` | ACS 坐标替代网格坐标；原始「无穷累积」路径被弃，因 Paper 0 不发展无穷表达式收敛理论 |
| Figure 10 | `fig:app-staircase-rectangles` | `17` | 二十五列缩减到产生 1、6、21 的三个阶；围量标注为加权面积而非胞腔计数 |

## 6. 开放项

1. `source-inventory.md` 中 `misc/` 数量计数与实测计数差一（第 1 节）。
2. `18-grid-example-2` 无忠实渲染（第 3.1 节）。忠实者必须建在当前资产旁保留，而非覆盖它。
3. 三个不可渲染 PNG 蒙太奇无生成器（第 3.3 节）。若要使用，必须重绘而非引用。
