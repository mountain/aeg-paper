# Paper 0 来源与论断审计

**状态：** 审计记录  
**日期：** 2026-08-09  
**规范入口：** `paper-0/aeg-paper-0.tex`

## 1. 目的

Paper 0 被引入以把最早的基于路径的 AEG 阐述与后来的双边/射影完成置于一个初级前奏中。它不
改变 Paper I 的标记历史定义。

## 2. 溯源

所用来源族是：

| 材料 | 历史来源 | Paper 0 处理 |
|---|---|---|
| 右/左展开示例 | 归档遗留根手稿，Basic Concepts | 修复约定与平行递归定义 |
| 路径记号与有界/自由路径 | 归档遗留根手稿 | 重新推导为年代纯梳求值 |
| `E_0` 网格与赋值 `a=-x/y` | 归档遗留根手稿与规范 Paper I 双曲模型 | 简明已证明初级模型 |
| 反演下弯曲网格 | 归档遗留注 | 扩展为 ripple 铅笔定理 |
| 单孔双边截面与矩阵表 | `notes/projective-condensation/01-bilateral-projective-condensation.tex` 与 Paper I | 以初级自包含形式保留 |
| 仿射不动点闭包 | 遗留 Paper I 附录与射影凝聚笔记 | 与吸引与算子身份分离 |
| 倒数作为几何级数闭包 | 射影凝聚/PAL 笔记 | 用有限、解析与形式收敛假设重写 |
| 连分数递推 | 双边射影笔记与标准矩阵演算 | 带显式普通域警告重新推导 |
| 极点/无穷与仿射规范 | 射影凝聚笔记 | 限制为初级射影坐标断言 |

`mountain/pcrg-paper` 仓库被列为可能的比较来源，但本次编辑期间无法通过连接的仓库索引获取。
因此未导入任何无支持的 PCRG 断言。

## 3. Paper 0 中的新推导

以下表述对规范系列是新的，并在 Paper 0 中证明：

1. 显式年代纯梳递归对 `L_k` 与 `R_k`；
2. 该索引约定下的对偶运算命题；
3. 路径/条件拉回区分；
4. `F^{-1}(Im w=t)` 的 ripple 铅笔线/圆公式及其在 `F^{-1}(infinity)` 处的相切；
5. 一个前缀矩阵的四读法定理：点、极点、不动点与 ripple 铅笔；
6. `1/(1-r)` 的极点、`s -> 1+rs` 的有限不动点消失与无穷处抛物不动点之间的显式联系；
7. 分离 Paper 0 与 Paper I 的拥有权/接口陈述。

## 4. 论断台账

| 论断 | 状态 |
|---|---|
| 显式定义纯梳的唯一内部序 | proved |
| 通过 `omega^op` 的梳对偶 | proved |
| `E_0` 赋值/eikonal 恒等式 | proved |
| 网格移动的算术相容性 | proved |
| horocycle 拉回线/圆公式 | 对实正行列式 Möbius 映射 proved |
| Apollonius 零–极水平集公式 | 在显示的零/极坐标有限处 proved |
| 几何级数有限公式 | proved |
| 几何级数解析极限 | 在 `|r|<1` 下 proved |
| 形式级数恒等式 | 在 `K[[r]]` 中 proved |
| 仿射迭代与收敛 | 带所述假设 proved |
| 倒数不动点方程与局部乘子测试 | proved |
| `PGL_2(K)` 生成 | proved |
| ripple 铅笔内在的射影 AES | open |
| 无穷算术表达式的一般收敛理论 | open |
| 由 ripple 数据导出的历史商不变量 | open |

## 5. 规范源闭包

```text
paper-0/aeg-paper-0.tex
paper-0/sections/01-introduction.tex
paper-0/sections/02-two-combs.tex
paper-0/sections/03-paths.tex
paper-0/sections/04-ripple-pencils.tex
paper-0/sections/05-reciprocals-fixed-points.tex
paper-0/sections/06-projective-unification.tex
paper-0/sections/07-interface.tex
paper-0/appendices/app-A-calculations.tex
```

构建使用 `bibliography/aeg-paper.bib`。无归档源被 TeX input 包含。

## 6. Paper I 迁移边界

以阐述所有权移动：

- 初级纯左/右梳比较；
- 基本网格的路径几何；
- 作为弯曲/ripple 网格的反演；
- 倒数–极点–无穷与初级不动点讨论；
- 初级矩阵综合。

保留在 Paper I：

- 标记脊柱历史术语与定义；
- 内在顺序树分类；
- 混合手性与反演/逆区分；
- 定理级射影历史求值与 Hecke 接口；
- 仿射流、完整双曲定理、零刚性、torsion 与接触几何。

Paper I 为逻辑自包含重复一些矩阵陈述；这是刻意的接口重复，而非分歧拥有权。
