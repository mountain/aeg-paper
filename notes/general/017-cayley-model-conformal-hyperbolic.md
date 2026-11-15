# 017 — Cayley 模型与 `{∞,4}` 的共形双曲统一：`g = (dx²+dy²)/L²` 及三种实现

> **文档性质**：算术表达式几何（AEG）研究笔记（017：`F₂` 4 叉树的 Cayley 模型、其双曲度量 `g=(dx²+dy²)/L²`，以及 Poincaré / Cayley / Hecke 三种 `{∞,4}` 实现的共形统一）
> **前置依赖**：笔记十六《C₂*C₄ 范式》（[016-c2c4-tearing-belyi-f7.md](016-c2c4-tearing-belyi-f7.md)）、旧笔记《Cayley 模型》（[01-cayley-hyperbolic-model.tex](../../notes/foundations-and-geometry/01-cayley-hyperbolic-model.tex)）、TikZ 源（[cayley-tree-4-border.tex](../../images/sources/cayley-tree-4-border.tex)）
> **日期**：2026-11-15
> **备注**：本笔记把 2025-07 的「Cayley 模型」与 2025-11 的 `{∞,4}` 线程合流；复现脚本 [030-cayley-model-hyperbolic.py](030-cayley-model-hyperbolic.py)、证明脚本 [031-conformal-hyperbolic-proof.py](031-conformal-hyperbolic-proof.py)。

---

## 一、Cayley 树 4-border 构造 = `F₂` 4 叉树 = `T₄`

TikZ 源 `cayley-tree-4-border.tex` 的递归构造：每个节点一个**正方形（= L¹ 球 `|x|+|y|≤R`，半径 `R=2^step` 逐层减半）**，其两条对角线就是嵌入的 `F₂` 4 叉树；每节点在顶顶点分出 3 个孩子（转 `−90°, 0, +90°`），根有 4 支（`0°, 90°, 180°, −90°`）。边长三角以 `s_n = L_0/2^n` 递减，正方形并集的边界 `B_n` 在极限是**分形**。

**关键**：这棵树就是 `{∞,4}` 铺砌的 1-骨架 `T₄`（笔记 016 的 `C₂*C₄` 树）的**欧氏嵌入**。左图（`030`）复现了它：53 个方格、156 条边。

## 二、双曲度量 `g=(dx²+dy²)/L²` 与 `K=−2`

旧笔记 01 提议的度量（`030` 已算出并验证）：

$$g = \frac{dx^2+dy^2}{L^2},\qquad L(x,y)=\text{到 border 的 Manhattan 距离（深度）}.$$

`L` 分段线性（`L=±x±y+C`），故 `ΔL=0`、`|∇L|²=2`，曲率 `K=LΔL−|∇L|²=−2`（数值 `−2.000`）。于是 `g` 是常负曲率 `−2` 的双曲度量，**分形 border 在无穷内禀距离处**。

## 三、引理：调和深度 ⟹ 常负曲率（`031` 符号证明）

设 `g=(dx²+dy²)/f²`（`f>0`），则高斯曲率

$$K = f\,\Delta f - |\nabla f|^2.$$

**证明**：共形度量 `g=e^{2φ}(dx²+dy²)` 的曲率 `K=−e^{−2φ}Δφ`。取 `φ=−ln f`：`e^{−2φ}=f²`，`Δφ=−Δ(ln f)=−(fΔf−|∇f|²)/f²`，故 `K=fΔf−|∇f|²`。**推论**：若 `Δf=0`（`f` 调和）且 `|∇f|=c`（常速），则 `K=−c²`。∎

## 四、三种 `{∞,4}` 实现与深度对应

| 模型 | 深度 `f` | `Δf` | `|∇f|²` | `K` | 类型 |
|---|---|---|---|---|---|
| **Poincaré** `H²` | `f=y`（高度） | `0` | `1` | **−1** | 双曲 |
| **Cayley** `D∞` | `f=L`（Manhattan 深度） | `0`（分段） | `2` | **−2** | 双曲 |
| **Hecke** `W`-平面 | `f=\|W\|=e^s`（径向） | `1/\|W\|` | `1` | **0** | **平坦** |

**结论**：

1. **Poincaré ≅ Cayley**：同一个双曲平面，只差**位似** `g_C = ½ g_P`（`K=−2 = −1·2`）。Cayley 模型不是新空间，而是 `H²` 在「欧氏平面 + 共形因子 `1/L²`」下的另一模型。
2. **Hecke 平坦 `g₄=|dζ|²`（`K=0`）是 developing map**：它把零集拉直成 `s=0` 直线（整流），不是双曲模型本身。
3. **深度对应**：三个模型的「到边界距离」函数同一角色

$$y\ \sim\ L\ \sim\ e^s = |W|,$$

分别是各自模型里把边界拉到无穷的共形因子，仅曲率归一化不同（`1, 2, 0` ↔ `K=−1,−2,0`）。

一句话：

> **`{∞,4}` 的三种实现 = 同一个共形双曲结构：Poincaré 与 Cayley 是同一条双曲平面（差 homothety），Hecke 平坦度量是它的 developing/rectification；深度函数 `y ∼ L ∼ e^s` 是这个共形类的一个不变量。**

## 五、状态汇总

| 结果 | 状态 |
|---|---|
| `F₂` 4 叉树 = `T₄`（Cayley 树 4-border 的欧氏嵌入） | `PROVED`（构造 + `030` 复现）|
| 曲率恒等式 `K=fΔf−|∇f|²` | `PROVED`（标准，`031` 符号）|
| Poincaré `K=−1`、Cayley `K=−2`、Hecke `K=0` | `PROVED`（符号；Cayley 分段调和 + `030` 数值）|
| `g_C = ½ g_P`（homothety）| `PROVED` |
| Hecke 平坦 = developing map | `STRUCTURAL PROPOSAL`（`paper-3 thm:q4-hecke-zero-network` 的读法）|
| 深度对应 `y ∼ L ∼ e^s` 为共形不变量 | `STRUCTURAL PROPOSAL` |

## 附：脚本索引

`028` C₂*C₄ 树（零碰撞）· `029` a-公式 + 分布 · `030` Cayley 复现 + `K=−2` · `031` 共形双曲引理证明。
