# 积分与体-表面对应（草案）

## 全息 Stokes：体平、曲率是表面 holonomy，积分是桥梁

### Research Note v0.1（草案）

**2026-10-31**（v0.1 草案：把"积分理论"与"体-表面对应"合成一条。核心：**体（有限 DAG / 紧致元）是平的；曲率 `μλ` 住在表面（理想边界 / 极限）上，作为 holonomy；积分（Stokes）是体与表面之间的桥梁**）

---

## 0. 目标与一句话结论

前几轮讨论确立了三件独立的事，本笔记把它们合为一条：

1. **Contact 曲率 = 最小分支 DAG 的序缺陷**（`17`/`18`）。
2. **"发生在极限处" = 体的理想边界 = 边缘表面**（Scott 排除、Alexandrov 拍平的那层）。
3. **从无穷小到宏观的桥梁 = 积分理论**（尚未彰显的那条线索）。

**一句话结论（全息式）**：

\[
\boxed{\ \text{体（有限 DAG，紧致元）是平的；曲率 }\mu\lambda\text{ 住在表面（理想边界）上作为 holonomy；积分（Stokes）把体的平性转成表面的曲率。}\ }
\]

---

## 1. 三个对象的精确对应

| 概念 | 精确对象 | 出处 |
|---|---|---|
| **体（bulk）** | 有限计算 DAG = 紧致元 = 下集格 `O(P)` | `15` §3（`Idl(FinDAG)`，紧致 = 有限）|
| **表面（surface）** | 理想边界 = 无限历史 `Γ^ω` = 极大元（"极限处"）| `09` §8、`15` §3（`γ_∞ = ⊔γ_n`）|
| **积分（integration）** | Stokes：`∫_体 dα = ∫_表面 α`（缺陷 = 边界 holonomy）| `paper-0` §8/§9（`thm:torsion-stokes`、`thm:legendre-dual-tearing`）|

**维度轴 + 完备轴**（前一轮已定）：

- **维度轴**：线索（链 = 1 维）围成 DAG（分支 = 2 维+）——下集格 `O(P)` 的 1-骨架。
- **完备轴**：有限体（紧致）的边缘 = 无限极限（理想边界）——ideal completion 的边界。

本笔记的"体-表面"取**完备轴**：体 = 有限，表面 = 无限极限。

---

## 2. 主定理（全息 Stokes，最小情形，`proved in paper-0`）

**Theorem（全息 Stokes）.** 对最小分支 DAG `{A,M}`：

1. **体是平的（组合意义）**：`O({A,M})` 是菱形 `B₂`（自由分配格），无序论曲率（`17` §4）。
2. **体的求值产生曲率，但曲率是恰当的（exact）**：contact 曲率形式
\[
d\alpha = -\lambda\,da\wedge dv = d(-\lambda a\,dv),
\]
非零但**恰当**（是 `-\lambda a\,dv` 的微分）。
3. **缺陷是边界 holonomy（Stokes）**：对以两线索为界的 2-胞腔 `Σ`（电荷矩形 `[0,h]×[0,k]`），
\[
T = \int_{\Sigma} d\alpha = \int_{\partial\Sigma}(-\lambda a\,dv),
\]
即缺陷 = 闭回路（四步时序历史 `A_h,M_k,A_{-h},M_{-k}`）上的 holonomy（`paper-0` `thm:legendre-dual-tearing`）。

**证明**：`dα = d(−λa dv)` 恰当（`paper-0` `prop:contact-form` 的 `dα = −λ da∧dv`）；Stokes 给 `∫_Σ dα = ∫_{∂Σ}(−λa dv)`；`paper-0` `thm:legendre-dual-tearing` 已证该边界积分 = Reeb 漂移 / 序缺陷，密度 `μλ`。∎

**全息内容（本笔记的新读法）**：

- 体（`Σ` 内部）携带**恰当的**曲率形式 `dα`（`dα ≠ 0` 但 `dα = dβ`），故其积分**只依赖边界**；
- 表面（`∂Σ` = 闭回路 = 两线索之差）是缺陷**住**的地方（holonomy）；
- 积分（Stokes）是桥梁：**把体的"恰当曲率"转成表面的"holonomy"**。

即：**体的非交换性（`dα ≠ 0`）由表面的 holonomy 记录**——这是"体-表面"对应的精确全息形式。

---

## 3. 离散 Stokes on `O(P)`（推广到任意分支，`open problem`）

最小情形只处理一个反链 `{A,M}`。宏观推广是把 Stokes 从"单个菱形"提升到"整个下集格 `O(P)`"：

**目标定理（离散 Stokes on `O(P)`，待证）**：设 `P` 为任意分支依赖偏序，`G(P)` 为线性扩展图（顶点 = 线性扩展 = 线索，边 = 相邻交换 = 菱形）。定义曲率 2-形式 `ω`：每个菱形（不可比对 `{x,y}` 经函子 `F` 实现为 `D_u,D_v`）上取 `ω = μλ`。则

\[
\nu_a(\gamma) - \nu_a(\gamma') = \int_{\Sigma_{\gamma,\gamma'}} \omega,
\]

对任意以 `γ, γ'` 为界的 2-链 `Σ`。`P = {A,M}` 时退化为 §2 的 `thm:torsion-stokes`。

**三个必须验证的点**（`open problem`）：

1. **可加性（1-上闭链）**：缺陷沿一串相邻交换可加——这等价于 `ω` 是线性扩展图上的**闭 2-形式**（否则"积分"不定义）。这是核心，需用 BCH 高阶项（`18` §8 残余 1）或直接计算验证。
2. **恰当性 ⟺ 边界量**：`dα` 的恰当性（§2.2）在宏观对应"缺陷只依赖两线索、不依赖中间 2-链"——这是"缺陷是 holonomy 型量"的宏观版本。
3. **与 `15` 的谱对接**：`O(P)` 的 Scott/Lawson 拓扑（`15` §6）应是这个离散 Stokes 复合体的**谱空间**（"谱 = 积分论的对象空间"）。

---

## 4. 表面 = 极限 = Scott 保留的那层

把 §2 的"表面 = 边界"与 Alexandrov/Scott 的"极限"接起来：

- **Scott 拓扑把无限历史保持为真极限**（从下逼近），故**表面（理想边界）在 Scott 下是真边界**；
- **Alexandrov 把无限历史拍平成孤立点**，故**表面被物化进体**，体-表面对应被抹平。

因此：**体-表面对应（体平、曲率住表面）只在 Scott 拓扑下成立；Alexandrov 拓扑抹平了表面，也抹平了"曲率是 holonomy"这一全息结构。**

这正是前面几轮"为什么谱要落在 Scott 而非 Alexandrov"的深层理由：**只有 Scott 拓扑保留表面（极限）作为曲率 holonomy 的居所。**

---

## 5. 一张图（合成）

\[
\begin{array}{c@{\quad}c@{\quad}c}
\text{体（有限 DAG，紧致元，平）}
&\xrightarrow{\ \text{理想完备}\ }&
\text{表面（无限历史 = 极限 = 理想边界）}\\
\Big\downarrow \text{求值（函子 }F,\ \text{非交换）} && \Big\downarrow \text{holonomy}\\
\text{curvature } d\alpha \ (\text{恰当，}d\alpha = d(-\lambda a\,dv))
&\xrightarrow{\ \text{Stokes 积分}\ }&
\text{缺陷 } \mu\lambda\ (\text{序缺陷 = 曲率密度})
\end{array}
\]

四格读法：

- **左上 → 右上**（理想完备）：体 → 表面（维度完备轴）。
- **左上 → 左下**（求值函子 `F`）：体（平）→ 曲率（恰当）。
- **左下 → 右下**（Stokes 积分）：曲率（体）→ 缺陷（表面 holonomy）。
- **右上 → 右下**（holonomy）：表面（极限）→ 缺陷（曲率住表面）。

**这张图是"积分 + 体-表面"的完整草案**：积分（Stokes）把体的恰当曲率搬到表面的 holonomy，体-表面由理想完备与 holonomy 两侧同时定义。

---

## 6. 地位总表与残余

| 命题 | 地位 |
|---|---|
| §1 三对象对应（体 = 紧致元，表面 = 理想边界）| `REFORMULATION`（`09` §8、`15` §3）+ `structural proposal`（"体-表面"命名）|
| §2 主定理（全息 Stokes，最小情形）| `proved in paper-0`（`thm:torsion-stokes`、`thm:legendre-dual-tearing`、`prop:contact-form`）|
| §2 全息读法（体平、曲率住表面）| `structural proposal`（新读法）|
| §3 离散 Stokes on `O(P)`（宏观推广）| `open problem`（三点待验：可加性 / 恰当性 / 谱对接）|
| §4 表面 = 极限 = Scott 保留 | `structural proposal`（衔接 Alexandrov/Scott）|
| §5 合成图 | `structural proposal` |

**残余（移交，`open problem`）**：

1. §3 的可加性（缺陷沿相邻交换是 1-上闭链）——这是"积分论"能否成立的核心，落在 `18` §8 残余 1（高阶括号）。
2. §3 的谱对接——`O(P)` 的 Scott 拓扑作为离散 Stokes 复合体的谱空间。
3. 宏观"体-表面"的严格化——把 §5 的图从最小 `{A,M}` 推广到任意 `P`，需要 §3 的三点先闭合。

---

**参考**（沿用）：

1. `paper-0/sections/09-contact-of-tearing.tex`（`prop:contact-form`、`thm:legendre-dual-tearing`、`thm:torsion-stokes`）。
2. `notes/analysis-and-calculus/09-order-topology-scott-lawson.md` §8、`15-branching-history-dcpo.md`、`17-contact-curvature-as-dag-defect.md`、`18-limit-smoothing-functor.md`。
3. G. Birkhoff, *Lattice Theory*, AMS (1967)。
