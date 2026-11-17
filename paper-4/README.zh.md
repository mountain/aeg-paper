# Arithmetic Expression Geometry IV

## Projective Condensation and Computational Complexity（射影凝聚与计算复杂度）

**副标题：** *From Histories and Quotients to Representation and Cost*

**规范源：** `aeg-paper-4.tex`  
**生成手稿：** `aeg-paper-4.pdf`  
**状态：** 处于数学审查中的草稿手稿<br>
**日期：** 2026-10-09

## 草稿状态

这里的 **draft** 描述的是编辑与出版成熟度：概念组织、行文、图件以及正文–图件的整合仍在
开发中。它不是 `governance/` 中的数学论断状态标签，也不改变任何单个结果的状态。

Paper IV 研究当一个算术历史被替换为一个算子、一个射影商状态或一个端点时被遗忘了什么，
并确定该被遗忘的信息何时能与一个精确在线状态或操作资源相关联。

中心链是

```text
marked history
  -> projective operator
  -> bivaluation / projective quotient
  -> contextual continuation residual
  -> operational realization.
```

这些箭头不被等同。本手稿分离四个层次：

1. 射影商纤维；
2. 未来相对语境残差；
3. 操作式活配置；
4. 相等语义实现的重写纤维。

## 主要已证明结果

- 正则双赋值是有序像–核对，且等价于 `K^2` 上的秩一幂等元。
- 对 `G = PGL_2(K)` 与有序对稳定子 `H`，双赋值空间是 `G/H`，而第三个射影点恢复一个
  `H`-torsor 框架。
- 在 `F_q` 上，商与纤维大小是显式的：`|G| = q(q^2-1)`、`|G/H| = q(q+1)`、`|H| = q-1`。
- 左延拓总是作用于 `G/H`。单个右更新 `k` 当且仅当 `k^{-1} H k` 含于 `H` 时下降；可逆右
  作用恰通过正规化子下降。
- 对带型接口、合法未来幺半群、部分域约定与观测，语境延拓等价给出规范的极小精确确定性
  在线状态。
- 有限残差空间给出定宽或前缀自由的极大状态下界。求和这些界给出定寄存器
  **capacity–time** 界，而非无条件的动态内存–时间定理。
- 带显式复制/丢弃的有限严格带型网络支持保源、保 occurrence 的替换与精确复合部分域。
  数值结合律包含域相等；图重结合是显式同构，而字面调用回执保持不同。
- 相容 AES collar 与完备计算接缝记录在组装全局事件图无环时一起下降。这构造一个附着的
  程序，而非其门作为 AES 运动的忠实实现。
- 特征观测因式分解等价于语境等价的精细化。在线特征更新额外要求右同余核；有效实现仍是
  独立的义务。
- 在允许擦除或重算的模型中，曾计算的节点集不决定工作空间。
- 精确纤维–像与条件熵不等式量化求值损失，而不把词增长变成运行时间下界。
- 加性势标签与纯规范群标签围绕每个重写环 telescoping，故它们单独不能定义非平凡
  holonomy。

## 精确校准

本手稿包含一个移植网络实验与四族计算校准：

- Ported AES：带四个输入程序与显式复制的固定四穿孔载体给出三个标量输出 `(9, 15, 5/2)`，
  保留源、occurrence、精确定义域与调用回执。这些是声明的标量投影，不是 Adva 的原生三
  输出角色。
- Horner histories：固定数字直方图有一个 ACS charge，但在特征零下有 multinomial 数量的
  不同仿射算子。
- OBDD equality：块序宽度至少 `2^n`，而交错序有常数宽度，尽管变量限制可交换。
- Butterfly 与 NTT 网络：局部 butterfly 是公共矩阵乘对角环面标签；完整变换需要多线线性
  语义、标量归一化与声明的成本模型。
- 矩阵链与检查点：相等的语义映射可以有不可比较的工作量、中间大小与活跃空间坐标。

## 论断边界

Paper IV **不**推断以下任何一条：

```text
noncommutativity -> negative curvature
negative curvature -> computational hardness
exponential group growth -> exponential runtime
large history fiber -> large shared representation
endpoint cost difference -> process holonomy
```

有限多线程序接口以所述假设建立。其实际算术/结构门作为 AES 运动的忠实实现、实际的对边
特征见证、非平坦射影传输、近似残差与机器稳健复杂度比较仍是开放计划。几何穿孔、计算孔
与输入/输出端口保持独立；绑定输入不改变载体赋值或端封。

## 源布局

```text
aeg-paper-4.tex
sections/01-introduction.tex
...
sections/05-contextual-residuals.tex
sections/05b-ported-aes-programs.tex
sections/06-operational-resource-geometry.tex
...
sections/14-conclusion.tex
appendices/app-A-projective-calculations.tex
appendices/app-B-residual-proofs.tex
appendices/app-C-network-counts.tex
appendices/app-D-claim-ledger.tex
../bibliography/aeg-paper.bib
scripts/verify-paper4.py
scripts/verify-ported-aes.py
scripts/fixtures/ported-aes/integration-evidence.json
```

## 构建

从仓库根目录：

```bash
./build.sh 4
```

或从本目录：

```bash
pdflatex -halt-on-error -file-line-error -interaction=nonstopmode aeg-paper-4.tex
bibtex aeg-paper-4
pdflatex -halt-on-error -file-line-error -interaction=nonstopmode aeg-paper-4.tex
pdflatex -halt-on-error -file-line-error -interaction=nonstopmode aeg-paper-4.tex
pdflatex -halt-on-error -file-line-error -interaction=nonstopmode aeg-paper-4.tex
```

用以下命令运行无依赖有限验证套件：

```bash
python scripts/verify-paper4.py
python scripts/verify-ported-aes.py
```

## 移植章节溯源与验证边界

移植章节改编自 2026-10-09 H² 紧化会话中产出的八页 `paper4-ported-aes-v0.1.pdf` 的完整
文本。它被置于语境残差之后、操作资源几何之前。`Subst` 表示程序替换；现有 `Fill` 记号仍
保留给重写填充面积。

候选会话报告了 55 个精确有限检查，但其原始 `aes-ported-paper4-v0.1.zip` 在集成期间无法
取回。新的 `verify-ported-aes.py` 是独立编写的集成 checker，不是恢复或重跑的原始套件。
其 14 个命名检查组覆盖：精确有理执行；源/occurrence 传输；一次性绑定、类型与实例控制；
部分前沿排序；严格部分域与丢弃；带不同 trace 的调度无关输出；带不同回执的复合同构；
相等值/不同过程控制；两个独立编写的接缝包重构及其负控制；由局部无环片段形成的全局环；
特征观测对在线更新；以及八个精确有理倒数图度量/余向量/框架样本。复合组检查恒等律与重
结合，前沿组检查其开放生产者顺序/同时比较所需的显式边界置换。checker 中的源标签是不可变
的语法位置；绑定后的值血统由生产者 DAG 与回执保留，而非通过覆写那些源字段。

被检查的确定性证据是 `scripts/fixtures/ported-aes/integration-evidence.json`。从本目录复现
并比较它，而不替换已检入的证据：

```bash
python scripts/verify-ported-aes.py > /tmp/ported-aes-evidence.json
cmp /tmp/ported-aes-evidence.json scripts/fixtures/ported-aes/integration-evidence.json
```

这些是独立的有限 fixture 与样本，不是恢复的原始包或门放置。它们补充论文内证明，且不
确立连续重叠恒等式、忠实的 AES 门运动实现或原生对边特征见证。

## 发布边界

PDF 是数学审查手稿。公开发布、作者元数据、DOI 分配与并入仓库发布线需要作者明确批准。

## 对向过程快照校准

独立的 `scripts/verify-opposite-features.py` 把固定的 Adva 0114 记录适配到现有带型有限
checker。复现、精确源坐标、有限 chi_C 阻碍与开放边界见
[见证记录](../governance/opposite-feature-witness-2026-10-09.md)。它保留完整事件/源包
与相等的标量三元组并列；它不执行 Adva 机制，也不证明它们的 AES 等价。

## 有限过程谱与循环前缀

[2026-10-10 校准](../governance/process-spectrum-calibration-2026-10-10.md) 比较精确覆盖
图谱、标记 Alexandrov 开集、抽象格与带型源前沿，然后对一个合成 anytime 循环对照其有限
展开进行测试。它保留 PR #16 的历史与边界。复现：

```bash
python3 paper-4/scripts/verify-process-spectrum.py > /tmp/process-spectrum.json
cmp /tmp/process-spectrum.json paper-4/scripts/fixtures/process-spectrum/evidence.json
python3 -O paper-4/scripts/verify-process-spectrum.py > /tmp/process-spectrum-O.json
cmp /tmp/process-spectrum.json /tmp/process-spectrum-O.json
```

独立 guard/receipt 审计（同一合成范围）：

```sh
python3 paper-4/scripts/receive-process-spectrum.py /tmp/process-spectrum.json > /tmp/process-receiver.json
cmp /tmp/process-receiver.json paper-4/scripts/fixtures/process-spectrum/receiver-evidence.json
```

接收方在不导入生成器的情况下检查显式停止尝试、完整对截断观测、源身份、角色与保留历史；
参见规范记录了解局限与变异结果。
