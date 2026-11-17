# Paper IV 来源审计

**审计日期：** 2026-08-07  
**仓库基线：** `264b7edeade754b706b575929fbbe3c8df72b5c3`  
**当前手稿：** `paper-4/aeg-paper-4.tex` 及其显式输入  
**状态：** 溯源与迁移记录

## 1. 目的与权威

本审计记录哪些仓库材料与外部数学来源被用于构造 Paper IV、哪些结果在活跃手稿中被重新推导，
以及哪些表述被拒绝或仅作为动机保留。它不取代权威重组文档。

所用权威顺序是：

1. 显式 Paper IV 写作任务；
2. `README.md`、`AGENTS.md` 与权威重组文件 `00` 到 `08`；
3. 规范 Papers I–III；
4. `governance/discussions/` 下的 Paper IV 工作讨论；
5. 历史笔记与归档材料；
6. 外部主要数学文献。

工作笔记或历史类比不是证明权威。一条论断只有当其假设、陈述与证明出现在活跃 Paper IV 源中
或由精确引用导入时才是规范的。

## 2. 审查的仓库来源

### 规范接口

- `paper-1/aeg-paper-1.tex` 与 `paper-1/appendices/app-E-equality-neutrality.tex`：历史、算子、
  端点、charge 与 torsion 相等层级。
- `paper-2/aeg-paper-2.tex`：有界解析与表示接口。
- `paper-3/aeg-paper-3.tex` 及其活跃 README/决定记录：有限遗忘、单值与提供寄存器对历史自然
  构造之间的论断边界。
- `README.md`：四论文架构与 Paper IV 范围。
- `governance/00-authoritative-scope.md`：复杂度断言前状态、度量、编码、成本与机器模型必须
  显式的要求。
- `governance/06-editorial-rules.md`：论断优先阐述与已证明结果、提案、猜想与开放问题的分离。

### Paper IV 工作来源

- `notes/projective-condensation/01-bilateral-projective-condensation.tex`：双赋值/投影子公式、
  商塔、对偶传输与射影凝聚动机。
- `governance/discussions/history-residual-cut-resource-geometry.md`：历史–残差–切割框架、
  Horner、butterfly、OBDD、检查点、矩阵链与证明义务清单。
- `governance/discussions/three-branch-arithmetic-tubes-and-complexity.md`：跨论文范围、无支持
  曲率/困难性蕴含的拒绝，以及表示、时间与空间的区分。

活跃手稿重新推导每个被提升的定理。讨论文件是溯源与设计来源，不是被引用的证明替代。

## 3. 外部来源

参考文献对以下内容使用主要或标准来源：

- Shannon 熵；
- Nerode 残差等价；
- Newman 汇合引理；
- 粗群增长；
- OBDD 表示理论；
- 基数快速 Fourier 变换；
- 可逆计算与检查点。

外部文献被用作校准与历史定位。射影商、延拓侧、残差、有限域、Horner 与有限网络陈述在
Paper IV 中直接证明。

## 4. 迁移映射

| 来源材料 | 活跃 Paper IV 处理 | 状态 |
|---|---|---|
| 双边秩一矩阵公式 | 改写为带横截假设的双赋值–投影子定理 | REDERIVED HERE |
| `G/H`、`G/B_±`、框架与投影子层级 | 用固定的右陪集与年代约定改写 | REDERIVED HERE |
| 点/对偶点仿射律 | 在附录 A 中保留，带所述图表与符号约定 | REDERIVED HERE |
| 「被遗忘框架信息」直觉 | 转换为左/右延拓下降定理 | PROVED WITH STATED FUTURES |
| HRC 语境残差 | 对部分域全化，并由等变极小状态定理完成 | REDERIVED HERE |
| 残差对数作为空间 | 限制为定宽/前缀自由状态选择；操作断言移到活配置 | CORRECTED AND PROVED |
| 求和残差下界 | 命名为 capacity–time 并由快照计费门控 | CORRECTED AND PROVED |
| 完成/下集工作空间 | 一般拒绝；仅在无重算最后使用保留下保留 | PARTIAL RESULT WITH COUNTERBOUNDARY |
| Horner 定权示例 | 推广到固定直方图与特征零 | PROVED |
| butterfly 陪集观测 | 作为局部 `GL_2/PGL_2` 引理保留，带标量警告 | PROVED LOCALLY |
| NTT 校准 | 在 `F_257` 上有限且精确 | PROVED IN FIXED MODEL |
| OBDD 序示例 | 提供残差函数下界证明 | PROVED IN FIXED MODEL |
| 矩阵链/检查点示例 | 提供精确初级成本计数 | PROVED IN FIXED MODELS |
| 端点差 holonomy | 由 telescoping 势与纯规范命题拒绝 | PROVED OBSTRUCTION |
| 非交换性/双曲性蕴含困难性 | 排除 | UNSUPPORTED AND REJECTED |
| 一个标量统一表示/时间/空间 | 替换为模型相对 Pareto 向量框架 | STRUCTURAL FRAMEWORK |

## 5. 否定与有界发现

审查来源不提供：

- 完整多线 AEG 范畴；
- 带非平凡环残差的非平坦射影联络；
- 把商纤维熵与工作空间或运行时间等同的机器无关定理；
- 带已证明渐近优势的 AEG 原生快速变换族；
- 近似残差或率失真理论；
- 跨机器模型的稳健性定理。

这些保留为开放问题。审计不声称对不可达 Git 对象、未提交私有笔记或未提供给任务的外部仓库
的穷举搜索。

## 6. 可复现性

有限投影子、有限域商、右下降、Horner、OBDD、NTT、矩阵链、检查点与纤维不等式由
`paper-4/scripts/verify-paper4.py` 独立检查，它只使用 Python 标准库。该脚本是补充验证；证明
留在手稿中。
