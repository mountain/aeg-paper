# Arithmetic Expression Geometry II — Hyperbolic Real Function Theory（双曲实函数理论）

本目录包含一份处于数学审查中的草稿手稿：

> **Arithmetic Expression Geometry II: Hyperbolic Real Function Theory**
> *Horizontal Operators, Boundary Problems, and Arithmetic Holomorphicity*

规范源文件与生成产物是 [`aeg-paper-2.tex`](aeg-paper-2.tex) 与 `aeg-paper-2.pdf`。

## 草稿状态

这里的 **draft** 描述的是编辑与出版成熟度：概念组织、行文、图件以及正文–图件的整合仍在
开发中。它不是 `governance/` 中的数学论断状态标签，也不改变任何单个结果的状态。

## 主要结果

- 规范算术框架下对测度敏感的 Laplace–Beltrami 公式；
- 精确的曲面 Cauchy–Riemann 因式分解与全纯到调和的蕴含；
- 平面调和 AES 的局部双全纯拉回定理，带显式曲率定律；
- 一个完备平坦柱面 AES，其拉回的零集为 `W^{-1}(S^1)`，连同正则自守下降判据；
- 一个独立的 contact-CR 归一化、变分次 Laplacian 与 Friedrichs 实现；
- 完备基本双曲 AES 上的 Poisson 核与良定理想边界 `C_0` Dirichlet 问题；
- 一个精确的边界能量恒等式与 Dirichlet-to-Neumann 乘子；
- 显式的、依赖于赋值的全纯、调和与 contact-CR 族。

从仓库根目录用以下命令构建本手稿：

```bash
./build.sh 2
```

## 从 Paper 0 导入

- 正则 AES 定义与算术框架；
- 基本双曲模型；
- 算术接触模型、水平提升与括号曲率。

## 迁移的源文件族

- 遗留的 `sections/sec08.tex`；
- `sections/sec07.tex`、`sec09.tex` 与 `sec11.tex` 中的分析部分；
- `../archive/revision-1/`、`../archive/revision-2/` 与 `notes/` 下的相应材料。

## 状态边界

本手稿在基本双曲模型上证明了 Poisson–Dirichlet 定理与一个精确的边界能量恒等式。
它不声称一般的 Green 核、谱完备性、接触边界表示，或跨越奇异 AES 点的延拓。
拉回构造的临界点、极点与代数分支点留给 Paper III。二维正则 AES 复理论与三维
contact-CR 理论被严格分开。
