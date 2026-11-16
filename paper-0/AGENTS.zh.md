# Paper 0 编辑说明

这些说明适用于 `paper-0/` 内部，补充仓库根 `AGENTS.md` 与权威修正案
`governance/00b-paper-0-geometric-foundation-amendment.md`。

## 范围

Paper 0 是系列**几何基础**。保持其聚焦于：

- 算术展开：显式操作数槽递归下左右展开梳、单孔截面，与作关联同一表达式不同展开重写的分配律；
- 算术表达式空间：正则 AES 公理、规范算术框架、作运动的四运算、模型 `E_0` 与 `E_1`、连续算术
  运动及其矫正；
- 对偶读法：极点、horocycle 拉回、ripple 几何（仅描述名）、倒数、无穷、不动点与矩阵综合；
- 交换化：仿射余循环、相对缺陷、ACS、torsion–Stokes 定理与撕裂（度量缺陷之名）；
- 撕裂的接触结构：接触形式、水平场、曲率、有限开与闭缺陷与标量水平微分；
- §10 结构提案与 §11 穿孔空间与计算见证，各按记录状态。

此处不作为主要理论发展：内在顺序树分类、作主要对象的混合手性标记历史、Hecke `q=4` 语言、正则
零刚性或奇异零分类、函数论、商塔或无穷表达式一般收敛理论。那些属 Papers I–IV。

## 左/右术语

根仓库警告非形式左/右术语含糊。Paper 0 仅可在 `conv:p0-left-right-convention` 递归约定下使用它：

```text
L_0[z] = z,    L_k[z] = omega_k(L_{k-1}[z], c_k)
R_0[z] = z,    R_k[z] = omega_k(c_k, R_{k-1}[z])
```

索引是年代的。左/右每次后使用必须可约化到此操作数槽约定。

## 论断纪律

- 普通算术域与射影延拓必须保持不同。
- 无穷展开在陈述形式或解析收敛前不是数。
- 代数不动点不必吸引。
- 射影极点不是可允许普通除零。
- `Ripple pencil` 与 `ripple geometry` 是标准 horocycle 拉回族的描述术语，非新射影几何声称。
- `Tearing` 是命名双历史缺陷的结构提案，其值是 `thm:torsion-stokes` 其密度是
  `thm:contact-curvature`；从不陈述为独立定理。
- 穿孔声明为正则结构奇异点，非度量中孔；穿孔 AES 是 Paper I 奇异 AES 有限点情形，且此处不尝试
  其分类。
- `Yuan2026AEGHoleRegister` 项仅以状态 `COMPUTATIONALLY VERIFIED EXAMPLE` 进入，且 §11 非断言是
  该节一部分。
- 模型标签遵循 `conv:p0-model-labels`：`E_0` 是基本正则双曲模型（一次等同于旧
  `E_{\mathrm{hyp}}`）、`E_1` 是单穿孔盘、`E_k` 仅描述。
- 每条实质新或移动结果必须出现在 `governance/05b-paper-0-status-register.md`。

## 构建

从仓库根构建 Paper 0：

```bash
./build.sh 0
```

报告完成前检查 PDF、未定义引用、重复标签、缺失引用与图溢出。`paper-0/`、`paper-1/` 或
`bibliography/` 下任何变更也需 `./build.sh 1`，因 CI 一起验证两日志。
