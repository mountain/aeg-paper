# Paper I — Foundations（基础）

**暂定标题：** *Arithmetic Expression Geometry I: Foundations*  
**副标题：** *Sequential Histories, Projective Semantics, and Zero Geometry*

**MSC 2020：** 20H10（主）；05C05、58K05；20G15、68Q42、53C21

Paper I 发展了 Paper 0 的几何所预设的那一层：过程的语法与算术词的射影语义。它包含：

1. 具有唯一合法内部求值顺序的有限二叉表达式树的分类，以及这些树的标记脊柱历史；
2. 操作数槽位手性，与时间反演、函数求逆保持区分；
3. 非退化双边历史的射影求值、`PGL_2(K)` 的生成、仿射/Borel 扇区，以及秩一 Bruhat 分解；
4. `Q(sqrt2)` 上的 `q=4` Hecke 子语言及其历史级关系；
5. 正则算术表达式空间的零理论：正则零轨迹、完备分裂定理及其 no-go 推论、奇异算术
   表达式空间的定义、一个已验证的孤立零模型，以及带 properness 警告的参数族零集引理。

本论文只从 Paper 0 导入恰好一个几何定义——正则 AES 及其规范算术框架——因为它的零定理
是用这些术语陈述的。本论文早期版本所发展的其余一切（算术表达式空间、运动、双曲与穿孔
模型、仿射余循环、累积交换空间、撕裂与接触结构）现在都在 Paper 0 的修正案
`governance/00b-paper-0-geometric-foundation-amendment.md` 下被证明，此处只引用而不重复。

## 2026-10-29 修订

两处审查发现已被处理。第一，生成定理 `thm:bilateral-pgl2-generation` 此前在本论文与
Paper 0 中用同一因式分解计算证明；按系列规则“每个结果一个规范来源”所选的删除路径，
其证明现在只保留在 Paper 0（其矩阵与射影统一一章），本论文保留历史级陈述、其三行推导、
仿射扇区推论 `cor:affine-borel-sector`（Paper 0 中没有），以及 `q=4` Hecke 子语言。
第二，属于 Paper 0 的记号已从附录中移除：附录 A 记号表中的累积尺度与余循环两行，以及
附录 B 中建立在累积交换空间与开/闭 torsion 对上的两个例子（它们已在 Paper 0 的交换化
与接触模型章节中证明，并在其附录 C、D 中计算）。附录 B 现在定义它所使用的两个步族
`A_p`、`M_q`，并仅作为记账记录它们的两个总量。摘要中报告的“ace”笔误在本版本的源与
构建 PDF 中均不存在；无需更正。

## 规范源闭包

```text
paper-1/
  aeg-paper-1.tex
  sections/
    00-paper-zero-interface.tex
    01-introduction.tex
    02-sequential-histories.tex
    03-projective-affine.tex
    04-regular-aes-interface.tex
    05-zero-geometry.tex
    06-conclusion.tex
  appendices/
    app-A-conventions.tex
    app-B-equality-neutrality.tex
```

## 论断边界

此处已证明（状态记录于 `governance/05-mathematical-status.md`）：

- 顺序树的四个等价刻画，以及标记树/历史对应；
- 镜像、时间反演与路径逆的区分；
- 射影求值与年代的相容性、`PGL_2(K)` 的生成（由 Paper 0 的生成定理推出），以及
  affine/Borel 定位；
- 由一个显式标记历史实现的四阶 Hecke 关系；
- 正则零轨迹及其局部刚性；对连通完备无边正则空间的完备正则分裂 `M = Z(a) x R`；
  空间正则族的淹没总零集；以及已验证的孤立零奇异模型。

开放问题列于结论一章；它们涉及 Hecke 历史纤维、奇异多重零模型、properness 升级、历史
复杂度，以及普通可允许性与射影非退化之间的关系。

从仓库根目录用 `./build.sh 1` 构建。
