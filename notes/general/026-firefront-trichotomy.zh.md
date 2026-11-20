# 026 — 火烧波前的三分法：诞生（半）、值（平分线）、根（全）

> **文档性质**：算术表达式几何（AEG）研究笔记（026：把 [025](025-quadratic-fewnomial-minus.md) 的 fewnomial 三分法翻译到双曲火烧波前）
> **日期**：2026-11-20
> **备注**：对应插图 `053-half-full-firefront.png`；状态见下。

---

## 一、字典

[025](025-quadratic-fewnomial-minus.md) 的 fewnomial 法则把 $f(V)=aV^2+bV+c$（$|V|=1$）三个系数分成三个角色。在双曲火烧波前 $M=\mathbb H^2/\Gamma$（无挠，基点 $p$）上，三个角色有精确对应：

| 角色 | fewnomial（025） | 火烧波前（双曲） |
|---|---|---|
| **诞生**（历史/尺度） | $\|b/a\|=2$ | $t=\|\gamma\|/2$（crossing 诞生） |
| **node / 值** | node 在 $c-a$（**定点**） | crossing 在**固定测地线** $B_\gamma=\{d(p,z)=d(\gamma^{-1}p,z)\}$ 上 |
| **根 / 零点** | 根乘积 $c/a$ | 波前在 $t=\|\gamma\|$ 穿过 $\gamma p$ |

其中 $\|\gamma\|=d(p,\gamma p)$ 是位移（基点长度谱的条目）。

**两个结构性变化**值得精确写出（`PROVED` / `STANDARD CONSEQUENCE`）：

1. **定点 → 固定测地线。** fewnomial 的参数是系数 $b$，node 是**点** $c-a$，不随 $b$ 动。火烧波前的参数是半径 $t$，变 $t$ 把 crossing 沿垂直平分线 $B_\gamma$ 扫动，于是值层面不变量是整条测地线 $B_\gamma$（等价地其边界端点 $(\xi_1,\xi_2)$，即 [023](023-gauss-word-alignment.md) 的"方向"）。

2. **半 vs 全。** crossing 诞生于位移的**一半**（$t=\|\gamma\|/2$，两球 $\Sigma_t(p),\Sigma_t(\gamma^{-1}p)$ 在中点相切），波前在**整**位移（$t=\|\gamma\|$）穿过 deck 像 $\gamma p$。两个特殊时刻成对：
   $$\text{诞生}=\tfrac12\|\gamma\|,\qquad \text{根}=\|\gamma\|.$$
   等价地，自交计数是**双倍时刻的根计数**：
   $$N(t)=\#\{\gamma:\|\gamma\|<2t\}=\#\{\text{到时刻 }2t\text{ 已到达的 }\gamma p\}.$$

## 二、具体例子 $\gamma=A$（抛物 $z\mapsto z+2$）

取 $p=i$；$A p=2+i$、$A^{-1}p=-2+i$，$\|A\|=\operatorname{arcosh}3=2\operatorname{arsinh}1\approx1.7627$。平分线 $B_A$ 是竖直测地线 $x=-1$（端点 $(-1,\infty)$，见 [023](023-gauss-word-alignment.md)）。

- **诞生**在 $t=\|A\|/2=\operatorname{arsinh}1\approx0.8814$：两个双曲圆 $\Sigma_t(p)$（圆心 $i\sqrt2$、半径 $1$）与 $\Sigma_t(A^{-1}p)$（圆心 $-2+i\sqrt2$、半径 $1$）在中点 $-1+i\sqrt2\in B_A$ 相切。
- **根**在 $t=\|A\|=\operatorname{arcosh}3\approx1.7627$：$\Sigma_t(p)$（圆心 $3i$、半径 $2\sqrt2$）穿过 $A p=2+i$。

插图：`053-half-full-firefront.png`。

## 三、状态

| 结果 | 状态 |
|---|---|
| 诞生于 $t=\|\gamma\|/2$（参 022） | `PROVED` |
| crossing 在固定测地平分线 $B_\gamma$ 上（参 023） | `PROVED` |
| 波前在 $t=\|\gamma\|$ 穿过 $\gamma p$ | `PROVED`（按 $C_t$ 定义） |
| 半/全配对；$N(t)=$ 双倍时刻的根计数 | `PROVED` |
| 定点 → 固定测地线的升级；值/历史分离 | `STRUCTURAL PROPOSAL` |
| 图 `053-half-full-firefront.png` | `COMPUTATIONALLY VERIFIED EXAMPLE` |

## 附：脚本索引

`053-half-full-firefront.png` 由本笔记会话内联脚本生成（可由 $\|A\|=2\operatorname{arsinh}1$、平分线 $x=-1$ 复现）。
