# 014 — Pell 收敛子的整合主图：Ford 圆、{∞,4} 圆盘铺砌与催化虫洞的两次 ln Q_k 约分

> **文档性质**：算术表达式几何（AEG）研究笔记（014：Pell 试验场的整合可视化，与四门催化虫洞的两次 `ln Q_k` 约分推导）
> **前置依赖**：笔记一《双曲热带波前-残差核（HTWR Core）》公理 I–IV（[001-htwr-core.md](001-htwr-core.md)）、笔记二《精确时空帕累托边界》（[002-htwr-example.md](002-htwr-example.md)）、笔记四《试验场序列选型》（[004-test-sequences.md](004-test-sequences.md)）
> **日期**：2026-11-14
> **备注**：主图与全部数值由 [014-pell-master-figure.py](014-pell-master-figure.py) 生成（脚本末尾打印自检）；[011-wormhole-acceleration-witness.py](011-wormhole-acceleration-witness.py)、[012-pell-hyperbolic-viz.py](012-pell-hyperbolic-viz.py)、[013-pell-poincare-wormhole.py](013-pell-poincare-wormhole.py) 为开发轨迹，本笔记为其收敛点。

---

## 一、统一常数 k 与主图概述

本笔记围绕一个常数

$$k := 3 - 2\sqrt2 = (\sqrt2 - 1)^2 = \lambda^{-2} = \left|\frac{\mu}{\lambda}\right|,$$

其中 $\lambda = 1+\sqrt2$（银比）、$\mu = 1-\sqrt2$。这个 `k` 同时是：

1. Pell 闭式的收缩因子 $|\mu/\lambda|$；
2. 银比的逆平方 $\lambda^{-2}$；
3. `{∞,4}` 铺砌的基本常数（Math.SE 的 IFS 构造，见 [013](013-pell-poincare-wormhole.py) 的 `F_1..F_4`）；
4. 收敛速率 $|x_n - \sqrt2| = 2\sqrt2\, k^n\,(1+o(1))$。

主图 `014-pell-master-figure.png` 的六个面板：

| 面板 | 内容 | 角色 |
| --- | --- | --- |
| (a) | Ford 圆 + 高度 $I=\ln P_n$ | HTWR 公理 I 读法 |
| (b) | `{∞,4}` 铺砌（Poincaré 圆盘），尖点 $w(\pm(\sqrt2-1))$ | 几何骨架 |
| (c) | $Z[\sqrt2]$ 单位在 $P^2-2Q^2=\pm1$ 上 | 范数 = 约分虫洞的算术源头 |
| (d) | 误差 $=2\sqrt2\,k^n$ vs 线性深度 | 收敛律 |
| (e) | 催化虫洞深度剖面（$k=2$ 与 $k=8$） | 虫洞加速 |
| (f) | Sylvester 对照（无虫洞） | 负参照 |

---

## 二、面板 (e)：四门跨越与两次 `ln Q_k` 约分

设 $x_n = P_n/Q_n$，常驻催化剂 $x_k = P_k/Q_k$，并置 $c_k := 2 - x_k^2$。由 Pell 范数恒等式

$$P_k^2 - 2Q_k^2 = (-1)^k$$

立得催化剂的深度为

$$c_k = 2 - \frac{P_k^2}{Q_k^2} = \frac{2Q_k^2 - P_k^2}{Q_k^2} = \frac{(-1)^{k+1}}{Q_k^2}.$$

### 2.1 四门代数（精确）

1. **加法潜入** $z_1 = x_n + x_k = \dfrac{P_n Q_k + P_k Q_n}{Q_n Q_k} = \dfrac{Q_{n+k}}{Q_n Q_k}$（用加法公式 $Q_{n+k} = P_n Q_k + P_k Q_n$）；
2. **求逆** $z_2 = \dfrac{1}{z_1} = \dfrac{Q_n Q_k}{Q_{n+k}}$；
3. **乘催化剂** $z_3 = z_2 c_k = \dfrac{Q_n Q_k}{Q_{n+k}}\cdot\dfrac{(-1)^{k+1}}{Q_k^2} = \dfrac{(-1)^{k+1} Q_n}{Q_k\, Q_{n+k}}$；
4. **加催化剂收束** $z_4 = z_3 + x_k = \dfrac{(-1)^{k+1} Q_n}{Q_k Q_{n+k}} + \dfrac{P_k}{Q_k} = \dfrac{(-1)^{k+1} Q_n + P_k Q_{n+k}}{Q_k Q_{n+k}}$。

关键：重负荷主变量 $x_n$ 在分式线性形式 $x_{n+k} = x_k + (2 - x_k^2)/(x_n + x_k)$ 中**只出现一次**（主导线零扇出），因此四门即可跨越 $k$ 步。

### 2.2 虫洞 #1（门 3，约去一重 `Q_k`）

未约分时，$z_2$ 的分子携带一重 $Q_k$，而 $c_k$ 的分母携带 $Q_k^2$，乘积为

$$z_3^{\text{(未约分)}} = \frac{(-1)^{k+1} Q_n Q_k}{Q_{n+k} Q_k^2}.$$

约去分子与分母公共的一重 $Q_k$，得 $z_3 = (-1)^{k+1} Q_n/(Q_k Q_{n+k})$。信息高度 $I(p/q) = \ln\max(|p|,|q|)$ 由分母主导，故

$$I\big(z_3^{\text{(未约分)}}\big) = \ln\big(Q_{n+k} Q_k^2\big), \qquad I(z_3) = \ln\big(Q_{n+k} Q_k\big),$$

**省下的深度** $= \ln\big(Q_{n+k}Q_k^2\big) - \ln\big(Q_{n+k}Q_k\big) = \ln Q_k.$

### 2.3 虫洞 #2（门 4，Cassini 消去另一重 `Q_k`）

用 Pell 的 Cassini 恒等式

$$P_{n+k} Q_k - P_k Q_{n+k} = (-1)^{k+1} Q_n$$

把 $z_4$ 的分子改写为

$$(-1)^{k+1} Q_n + P_k Q_{n+k} = P_{n+k} Q_k,$$

于是

$$z_4 = \frac{P_{n+k} Q_k}{Q_k Q_{n+k}} = \frac{P_{n+k}}{Q_{n+k}} = x_{n+k},$$

第二重 $Q_k$ 约去。深度由分子主导（$P_{n+k} > Q_{n+k}$）：

$$I\big(z_4^{\text{(未约分)}}\big) = \ln\big(P_{n+k} Q_k\big), \qquad I(x_{n+k}) = \ln P_{n+k},$$

**省下的深度** $= \ln Q_k.$

### 2.4 结论与数值

四门跨越的两处约分各精确省下 $\ln Q_k$，**总计 $2\ln Q_k$**——这正是笔记二表格里「$Q_k$ 约分虫洞坍缩虚胖通量」的逐门算术版。数值（脚本自检）：

| 量 | $k=2$（$x_3\to x_5$） | $k=8$（$x_4\to x_{12}$） |
| --- | --- | --- |
| 深度路径 | $1.946 \to 3.367 \to 3.367 \to 4.060 \to 3.714$ | $2.833 \to 5.953 \to 5.953 \to 13.063 \to 9.883$ |
| 每次省 | $\ln Q_2 = \ln 2 \approx 0.693$ | $\ln Q_8 = \ln 408 \approx 6.011$ |
| 总省 | $2\ln 2 \approx 1.386$ | $2\ln 408 \approx 12.023$ |
| 门数 vs 连分数 | $4$ vs $6$（$1.5\times$） | $4$ vs $24$（$6\times$） |

> **附注（诚实边界）**：§2.2/§2.3 的「省 $\ln Q_k$」在「未约分 → 消去一重 $Q_k$」这一步上精确成立；进一步化到既约分式时可能额外附带 $\gcd(Q_n,\, Q_k Q_{n+k})$ 等 $O(1)$ 约分（不改变 $\ln Q_k$ 主项）。以 $k=8,\,n=4$ 的 $z_3$ 为例：未约分高度 $\ln(Q_{n+k}Q_k^2)=\ln(13860\cdot408^2)\approx21.558$；消去一重 $Q_k$ 后 $\ln(Q_{n+k}Q_k)=\ln(13860\cdot408)\approx15.547$（省 $6.011=\ln408$）；继续约去附带 $\gcd=12$ 得既约 $-1/471240$，深度 $13.063$。$z_4$ 因 $\gcd(P,Q)=1$ 无附带约分，恰好省 $\ln Q_k$。图中「幽灵点」按「约分后深度 $+\ln Q_k$」示意。

---

## 三、面板 (f)：Sylvester 无虫洞对照

Sylvester $s_{n+1} = s_n^2 - s_n + 1$ 的项两两互素，**没有范数恒等式**，因此不存在 $c_k = \pm 1/Q_k^2$ 型轻量催化剂，也就没有约分虫洞可资利用。其深度 $\ln s_n$ **每步翻倍**（$0.69 \to 1.10 \to 1.95 \to 3.76 \to 7.50 \to 15.00 \to 30.00$），与 Pell 的线性深度形成对照。结论（对应笔记四定位）：Sylvester 里「反复平方制造指数位宽」这条免费午餐被按管径收费堵住，**naive = optimal**。

---

## 四、状态标注

- 恒等式（Pell 范数、Cassini、Möbius 大步、四门跨越、收敛率 $2\sqrt2 k^n$、Sylvester 深度翻倍）均为经典标准事实，`COMPUTATIONALLY VERIFIED EXAMPLE`；
- 「高度 = 到 Ford 圆距离」「深度剖面 = 虫洞」是 HTWR 公理 I–II 的读法，`STRUCTURAL PROPOSAL`；
- 加速倍数（$4$ vs $24$ 门等）是 HTWR 代价模型（公理 II）下的读数，不是机器墙钟成本，也非独立计算下界。
