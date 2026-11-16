# 权威修正案：Paper 0 前奏

**状态：** 权威修正案  
**版本：** 1.0  
**日期：** 2026-08-09  
**适用于：** AEG 论文系列架构与 Paper I 重组

本文件明确修正 `governance/00-authoritative-scope.md` 与
`governance/01-paper-series-architecture.md`。凡那些文件描述以 Paper I 开始的四论文系列
之处，本修正案优先并插入下文规定的初级 Paper 0。现有治理文件的其余所有范围限制仍有效。

## 1. 修订后的系列架构

活跃手稿系列是：

0. **Arithmetic Expression Geometry 0: Paths and Ripple Pencils**  
   *Left and Right Expansions, Reciprocals, and Projective Unification*
1. **Arithmetic Expression Geometry I: Foundations**
2. **Arithmetic Expression Geometry II: Hyperbolic Real Function Theory**
3. **Arithmetic Expression Geometry III: Singular Zero Geometry and Tubes**
4. **Arithmetic Expression Geometry IV: Projective Condensation and Computational Complexity**

依赖架构是

```text
Paper 0 -> Paper I -> Paper II
                   -> Paper III
                   -> Paper IV
```

Paper 0 是初级前奏。它不取代 Paper I 作为后续论文定理级基础的地位。

## 2. Paper 0 的角色

Paper 0 必须以自包含且初级的形式发展以下材料：

- 显式左展开与右展开梳约定；
- 两个纯梳的平行单孔求值；
- 第零类上半平面模型中的仿射点路径图景；
- 通过 Möbius 映射拉回 horocycle 得到的射影 ripple 铅笔图景；
- 算术倒数、分母极点、无穷远点、有限与无限倒数展开、迭代不动点；
- 初等算术截面的矩阵表示；
- 路径、极点、不动点与 ripple 铅笔的射影统一；
- 定位 `Aff(1,K) = Stab(infinity) < PGL_2(K)` 以及由平移、非零缩放与反演对 `PGL_2(K)`
  的初等生成。

Paper 0 可以使用历史记号 `E_0`，前提是它明确把该模型与 Paper I 的规范齐次双曲模型等同，
且不引入冲突的第二个定义。

## 3. Paper 0 的排除

Paper 0 不得作为主要理论发展：

- 超出纯梳证明的内在依赖偏序分类；
- 混合手性标记脊柱历史；
- Hecke `q=4` 历史语言；
- 仿射余循环与全局 torsion；
- 作为完整内在理论的连续仿射流；
- 正则零刚性或奇异零分类；
- 接触几何、水平演算或函数论；
- 射影双赋值、商塔或计算复杂度；
- 无穷算术表达式的一般收敛理论。

几何级数、连分数或迭代的收敛论断必须陈述其域、拓扑、普通域与吸引假设。

## 4. 转移后的 Paper I

Paper I 保留当前标记历史术语与形式体系。本修正案不授权标记历史重设计。

Paper I 仍是以下内容的规范拥有者：

- 内在顺序树分类；
- 标记平面顺序树与有界/自由标记脊柱历史；
- 操作数槽位手性、镜像、反演与路径逆；
- 年代历史的射影求值；
- `q=4` Hecke 子语言；
- 仿射余循环、连续流与正则 AES 定义；
- 完整齐次双曲模型与零集定理；
- ACS torsion、接触曲率与后续论文接口。

Paper I 可以为了逻辑自包含而重复简明初等矩阵公式与射影生成证明。Paper 0 是教学性
path/ripple 阐述与倒数–极点–无穷讨论的规范来源。

## 5. Paper 0 的论断状态

以下为 `proved with stated hypotheses`：

- 每个显式定义的纯梳有唯一内部求值顺序；
- 右梳与左梳之间的对偶运算对应；
- 非退化单孔算术截面的初等矩阵表；
- 第零类模型的上半平面赋值恒等式；
- 实保向 Möbius 映射下拉回 horocycle 的线/圆公式；
- 有限几何级数与连分数矩阵递推；
- 仿射与倒数不动点公式；
- `PGL_2(K)` 生成与秩一 Bruhat 定位。

术语 `point path` 与 `ripple pencil` 是描述性定义。它们不断言新的双曲或射影几何同构类。

以下仍是开放计划：

- ripple 几何内在的射影算术表达式空间；
- 商稳定 path/ripple 不变量；
- 多线 path/ripple 语义；
- 无穷算术表达式的一般理论。

## 6. 所需仓库变更

Paper 0 的规范入口是 `paper-0/aeg-paper-0.tex`。根构建脚本必须接受目标 `0`，仓库概览
必须在 Papers I–IV 之前列出 Paper 0。Paper I 必须包含一个简短接口陈述，识别被转移的初级
材料，而不改变其标记历史定义。
