# 平坦极限与复化严格性修复

**状态：** 范围修复与验证报告，不是全系列证明审计。
**日期：** 2026-11-07。
**基础：** `mountain/aeg-paper` main，`f1fe625967292254b3a014cedefc5a8e884dc827`。远程 main
ref 在最终验证期间再次检查且未改变。在初始产物交付时，未执行任何 commit、push、pull request
或 merge。这是本地验证快照；后续发布与远程检查结果由 pull request 记录，不在此断言。

## 数学变更

1. **Paper 0 第 3 节：** 添加 `prop:p0-flat-limit`。对固定 `mu>0`，全局映射
   `(u,v) -> (u,exp(lambda v))` 把正 lambda 模型与公共平面上的度量
   `exp(-2 lambda v) du^2/mu^2 + dv^2` 等同。度量、赋值与规范框架在紧集上光滑收敛到完备平坦
   正则 AES。证明处理所有导数阶；不声称整个非紧平面上的均匀收敛。
2. **Paper 0 第 12.6 节：** 移除「无重标能给出 Euclid 平面」的错误断言。添加
   `prop:p0-complex-conic-rank`，证明 R 到 C 标量扩张与可逆合同下的秩保持。只有两个非退化实
   二次型在 C 上变得等价；退化形式保持分离。Euclid 绝对含线与圆点数据。球面紧化现在显式要求
   亏格零与选定圆代表，且不产生带非零加法强度的闭正则 AES。
3. **研究笔记 51：** 完整对角 PGL2(C) 度量作用属于 `(P1 x P1) minus diagonal`；受限仿射模型
   只在公共域上支持拉回恒等式。平移与极点给出受限模型全局保持的精确反例。平方根是局部的或
   定义在无分支双重覆盖上；绕数论证排除基上的全局平方根。
4. **相邻笔记 51 修正：** 区分复化框架旋转与环境复结构，修正复零除子，陈述全局下降的连通
   纤维论证，显式化迹/长度符号选择，并把 RH/Schwarz 边界断言限制为其实际迹与趋近假设。添加
   C2 完备性与归一化论证。一般矩阵与内在复边界 RH 仍是提案/开放问题。

独立只读数学审查检查了新证明与笔记 51 修复。它发现并解决闭与带边紧正则 AES 的区分，以及
RH 对应中缺失的共轭边界迹假设。无阻塞发现遗留。

## 文件与溯源

- 论文源：`paper-0/sections/03-aes-and-motion.tex`、
  `paper-0/sections/12-compactification.tex`。
- 研究笔记与见证：`notes/analysis-and-calculus/51-complexified-model-and-rh.md`
  与 `51-complexified-model-and-rh-witness.py`。
- 新回归：`paper-0/scripts/verify-model-limits.py`；新可选 CI workflow
  `.github/workflows/model-rigor.yml` 使用 SymPy 1.14.0。
- 状态/导航：`governance/05b-paper-0-status-register.md`、`paper-0/README.md`、
  `paper-0/formal/README.md`、`paper-0/formal/inventory.json`、
  `paper-0/formal/machine.lock.json` 与本报告。
- 生成的 Paper 0 PDF：105 页。Paper I 仅为验证重建；其跟踪 PDF 恢复到原始字节。

无研究材料被移动或移除。活跃形式化清单现在有 22 个源与 105 个定理类条目。两个新命题都
明确为 `not-yet-formalized`。基线已失败两个清单一致性单元测试；干净基线重放复现那些失败。
刷新活跃清单与其一个锁摘要修复导航漂移，而不改变归档手稿快照、证书、Lean 证明、契约或执行
回执。

## 验证

使用 Python 3.12.14、SymPy 1.14.0 与 blake3 1.0.9：

| 检查 | 结果 |
|---|---|
| 新模型极限/秩见证 | 32/32，普通与 `python -O`，输出相同 |
| 笔记 51 见证 | 35/35，普通与 `python -O`，输出相同 |
| 现有紧化检查 | 139/139，普通与 `python -O`，输出相同 |
| 形式化回归单元测试 | 18/18，普通与 `python -O` |
| Python 编译 | 两个变更/新见证脚本通过 |
| 空白/补丁检查 | `git diff --check` 通过；源补丁干净应用到基础快照 |
| Paper 0 构建 | `./build.sh 0`，产出 105 页 PDF |
| Paper I 构建 | `./build.sh 1`，产出 61 页 PDF |
| 最终 LaTeX 日志 | 无未定义引用、缺失引用/资产、重复标签或未定义控制 |
| PDF 检查 | 变更命题/表/注页 19、80、81 渲染并视觉检查 |

安装的 TeX 发行版缺生成格式/字体映射缓存。构建使用由安装的 TeX 源与字体映射组装的临时可写
TeX 缓存；未改变系统文件或仓库构建设置。Paper 0 保留两个既有 overfull box（6.42 与 11.13 pt）
与六个既有 hyperref 数学书签警告。被编辑表的早期 0.58 pt 溢出被移除；无新溢出遗留。Paper I
在未变源中有既有布局警告，且不作为布局干净的产物呈现。

## 边界与下一步

有限/符号见证不证明紧集收敛、全局拼贴/拓扑、完备性、解析边界极限或一般 RH 可解性。修复后
文本提供范围证明或显式陈述的标准结果；这些都不是新的 Adva/Lean 证书。外部原生 Adva/Lean
执行套件、无关的仓库范围 workflow 与远程 GitHub Actions 在此本地交付检查点尚未重跑。新 CI
workflow 提供给后续发布阶段。

有用的下一步是对光滑族与分支/下降陈述的单独形式化，或对笔记 50 与剩余提议 RH 扩展的专门
解析审计。此处不声称那些已完成。
