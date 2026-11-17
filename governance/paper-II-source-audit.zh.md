# Paper II 来源与定理审计

**论文：** *Arithmetic Expression Geometry II: Hyperbolic Real Function Theory*

**审计基线：** `61ff60d`

**审计日期：** 2026-08-06

**状态：** 对数学审查手稿已闭包

本文件记录 Paper II 写作任务的受控范围。它从属于 `AGENTS.md`、
`00-authoritative-scope.md` 与 `01-paper-series-architecture.md`，但是对下列文件、定理节点与
验证的任务特定权威。

## 1. 范围

任务是创建 Paper II 的第一份完整数学审查手稿。论文导入 Paper I 中证明的正则 AES、基本双曲
模型与接触状态空间接口。它添加解析数据、区分二维曲面全纯性与三维接触 CR 分析、固定算子域
与度量、在基本双曲 AES 上证明 Poisson–Dirichlet 定理，并构造显式赋值依赖解族。

任务不尝试一般谱分解、任意 AES 上的 Green 函数理论、奇异零分析、管拓扑或计算复杂度推论。

## 2. 允许改变的文件

- `paper-2/**`；
- `build.sh`（用于加法多论文构建接口）；
- `README.md`（用于活跃手稿与构建文档）；
- `bibliography/aeg-paper.bib`（用于 Paper II 实际引用的参考文献）；
- `governance/paper-II-source-audit.md`；
- `governance/decisions-paper-II.md`；
- `governance/paper-II-closure-report.md`；
- `governance/audit-report.md`；
- `governance/05-mathematical-status.md`；
- `governance/07-acceptance-checklist.md`；
- `governance/08-open-questions.md`；
- `governance/migration-log.md` 与 `governance/source-inventory.md`。

## 3. 禁止改变的文件

- `paper-1/` 下的数学源与生成 PDF；
- 遗留 `sections/sec*.tex` 源；
- `archive/`、`notes/`、`notes/knots-and-loops/` 与 `images/sources/` 下的文件；
- Paper III 与 Paper IV 数学源。

遗留源仍是溯源记录。规范 Paper II 陈述被重新推导，而非原地静默编辑。

## 4. 来源审计

| 来源 | 可复用内容 | 所需处理 |
|---|---|---|
| `sections/sec07.tex` | 水平导数；自然单位；三角计算 | 只通过导入保留 Paper I 曲率；重新推导解析算子并把可计算族移到 Paper II 附录 |
| `sections/sec08.tex` | 形式 Cauchy–Riemann 系统、共形性、因式分解、显式对数场 | 分离曲面全纯性与接触 CR；固定度量、度量、域、分支与符号假设 |
| `sections/sec09.tex` | 解析研究接口 | 用已证明 Paper II 结果与有界前沿替换计划语言 |
| `sections/sec11.tex` | 扩展接触、因式分解、对数与有限族计算 | 审计公式；只在规范 Paper II 证明或附录中复用 |
| `archive/revision-1/sections/sec06-analytic.tex` 与修订 2 对应 | 紧凑形式算子包 | 仅溯源；无独立定理权威 |
| `notes/analysis-and-calculus/01-horizontal-analysis-program.tex` | 因式分解与变分算子的区分 | 通过显式伴随与双曲模型计算解决该区分 |
| Paper I 第 5、6、9 节 | 正则 AES、规范框架、双曲度量、接触分布与括号 | 导入已证明接口；定义被丰富而非改变 |

审计发现遗留解析表述中的四个阻塞缺陷：

1. 正则 AES 的二维复分析与三维接触状态空间的 CR 分析未被范畴式分离；
2. 原始平方和被称为 Laplacian，却没有其散度漂移或声明度量；
3. affine–Appell 族被称为基，却没有环境完备化或生成定理；
4. 尚无边界、核、谱或延拓定理被证明。

Paper II 通过定义与精确计算解决前三者。它通过 Poisson 核及其 Dirichlet-to-Neumann 能量恒等式
在基本双曲 AES 上解决第四个。

## 5. 范围内的定理节点

以下依赖顺序对本次任务固定。

```text
P2-D1  analytic regular AES and arithmetic frame
  |
  +--> P2-T1  frame adjoints, energy form, and Laplace--Beltrami operator
  |       |
  |       +--> P2-T2  intrinsic CR factorization and holomorphic => harmonic
  |
  +--> P2-D2  normalized contact analytic structure
          |
          +--> P2-T3  contact adjoints, Friedrichs realization, bracket generation
          +--> P2-T4  contact-CR factorization and logarithmic CR field
          +--> P2-T5  finite filtered affine--Appell modules

Paper I basic hyperbolic model
  |
  +--> P2-T6  arithmetic-frame operator equals the hyperbolic Laplacian
          |
          +--> P2-T7  Poisson kernel and C_0 Dirichlet theorem
          +--> P2-T8  Dirichlet-to-Neumann multiplier and energy identity
          +--> P2-T9  explicit assignment-dependent holomorphic families
```

术语 `harmonic` 保留给命名算子。曲面调和性指 `\Delta_g F=0`；接触变分调和性指
`\Delta_{\mathcal C}F=0`；接触 CR 因式分解产生一个单独命名的扭曲方程。

## 6. 授权的论断状态变更

- 形式框架与因式分解恒等式在完整论文内计算后可成为 `PROVED`；
- 修正后的对数接触 CR 场在其分支域固定后可成为 `PROVED WITH STATED HYPOTHESES`；
- affine–Appell 材料只作为有限滤过模可成为 `PROVED`，而非 Hilbert 或 Schauder 基；
- Poisson、Dirichlet-to-Neumann 与显式解族结果在其证明包含后可成为
  `PROVED WITH STATED HYPOTHESES`；
- 不授权一般自伴性、谱完备性、Green 核或延拓断言。

## 7. 所需验证

1. [x] 独立构建 Paper I 与 Paper II；
2. [x] 确认两个预期 PDF 非空；
3. [x] 运行 BibTeX 并检查未定义引用与引用；
4. [x] 检查重复标签与缺失资产；
5. [x] 独立验证 P2-T1–P2-T9 中每个公式；
6. [x] 渲染每个 Paper II 页面并检查标题、方程、图、分页与参考文献；
7. [x] 执行独立数学与范围审查；
8. [x] 记录剩余局限而非提升它们。

## 8. 预期输出

- `paper-2/aeg-paper-2.tex`；
- 规范 `paper-2/sections/` 与 `paper-2/appendices/` 源；
- `paper-2/aeg-paper-2.pdf`；
- 一个 Paper II 决定记录与闭包报告；
- 更新的仓库构建与溯源记录。

所有预期输出现已存在。精确产物元数据、静态检查、渲染审查、独立审查处置与剩余发布动作记录
于 `paper-II-closure-report.md`。迁移 M-0003 与状态变更 S-0006 闭包本手稿的溯源与论断状态台账。
