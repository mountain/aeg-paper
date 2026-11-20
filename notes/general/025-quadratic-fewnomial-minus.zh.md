# 025 — 单位圆上的二次 fewnomial：node 在 $c-a$

> **文档性质**：算术表达式几何（AEG）研究笔记（025：给出 [021](021-fire-front-twist-flat-torus.md)/[024](024-cusp-birth-fewnomial-firefront.md) 背后的一般法则，并套到新例 $P_\epsilon(V)=V^2-\epsilon V-1$）
> **日期**：2026-11-20
> **备注**：对应脚本 `052-quadratic-fewnomial-minus.py`；状态见下。

---

## 一、$f(V)=aV^2+bV+c$ 在 $|V|=1$ 上的一般法则

自交 $f(V)=f(W)$（$V\neq W$）分解为

$$f(V)-f(W)=(V-W)\bigl(a(V+W)+b\bigr),$$

故 crossing 是**弦和**条件 $V+W=-b/a$，可解当且仅当 $|b/a|\le2$（在 $|b/a|=2$ 处作为尖点诞生，此时 $V=W$）。在 crossing 处 $V+\overline V=-b/a$，于是

$$f(V)=aV^2-a(V+\overline V)V+c=-a|V|^2+c=c-a.$$

因此（`PROVED`，三行）：

1. **node 位置** $=c-a$，**与 $b$ 无关**；
2. **诞生**在 $|b/a|=2$（$b$ 唯一介入之处）；
3. **根乘积** $=c/a$（$f(V)=0$ 的根）。

三个系数各司其职：$b/a$ = 诞生阈值、$c/a$ = 零点结构、$c-a$ = node 处的值。

## 二、新例 $P_\epsilon(V)=V^2-\epsilon V-1$

这里 $a=1$、$b=-\epsilon$、$c=-1$，故 node 恒在 $c-a=-2$，诞生于 $|\epsilon|=2$，根满足 $r_+r_-=-1$。相图（参 [algebra/01 §3](../algebra/01-finite-layer-exponential-polynomials.md)）：

| $\epsilon$ | $|V|=1$ 在 $P_\epsilon$ 下的像 |
|---|---|
| $0$ | $e^{2it}-1$：圆心 $-1$、半径 $1$ 的圆，走两遍 |
| $0<\epsilon<2$ | $-2$ 处一个横截 node |
| $\epsilon=2$ | $-2$ 处尖点 |
| $\epsilon>2$ | 光滑简单闭曲线 |

具体地 $P_\epsilon(e^{it})=e^{it}(2i\sin t-\epsilon)$；node 的原像是 $V=e^{\pm it}$（$2\cos t=\epsilon$）。根 $r_\pm=\frac{\epsilon\pm\sqrt{\epsilon^2+4}}{2}$，实、$r_+r_-=-1$（反互易）；$\epsilon=1$ 时是黄金比 $\varphi$ 与 $-1/\varphi$；$\epsilon=2$ 时是 $1\pm\sqrt2$。

## 三、与 $+1$ 族对照，及恒等式

| | $Q_\epsilon=V^2+\epsilon V+1$（[024](024-cusp-birth-fewnomial-firefront.md)） | $P_\epsilon=V^2-\epsilon V-1$（本例） |
|---|---|---|
| 弦和条件 | $V+W=-\epsilon$ | $V+W=+\epsilon$ |
| node | $0=c-a$ | $-2=c-a$ |
| 根 $r_+r_-$ | $+1$（共轭，$\epsilon<2$ 时在单位圆上） | $-1$（反互易，恒实） |
| node vs 零点 | node 是零点（在 $0$） | node 不是零点（在 $-2$） |

两族由精确恒等式联系：

$$P_\epsilon(V)+2=V^2-\epsilon V+1=Q_{-\epsilon}(V).$$

所以 $P_\epsilon$ 的 node 是 $Q_{-\epsilon}$ 零点集**平移 $-2$ 的像**：一族的自交轨迹，是符号翻转族的（平移后的）零点轨迹。

## 四、回到火烧波前

两族共享 [024](024-cusp-birth-fewnomial-firefront.md) 的诞生机制：弦和 $V+W=-b/a$ 在 $|b/a|=2$ 达到直径，与火烧波前弦差 $u-v=v/t$ 在 $t=|v|/2$ 达到直径对偶（平行四边形律 $|u-v|^2+|u+v|^2=4$）。本例新增的是**值层面**内容：node 位置 $c-a$ 与根乘积 $c/a$ 在单参数族下固定，只有诞生阈值 $b/a$ 在变——把"曲线在哪儿自交/打零点"（值）与"crossing 何时诞生"（历史/尺度）分开，这正是 AEG 值/历史区分的意义（`STRUCTURAL PROPOSAL`）。

## 五、状态

| 结果 | 状态 |
|---|---|
| $f(V)-f(W)=(V-W)(a(V+W)+b)$；node 在 $c-a$；诞生于 $\|b/a\|=2$；根乘积 $c/a$ | `PROVED` |
| $P_\epsilon$ 相图；node 在 $-2$；根乘积 $-1$ | `PROVED` |
| $P_\epsilon+2=Q_{-\epsilon}$ | `PROVED` |
| node/根 = 值层面，诞生 = 历史层面 | `STRUCTURAL PROPOSAL` |
| 图 `052-quadratic-fewnomial-minus.png` | `COMPUTATIONALLY VERIFIED EXAMPLE` |

## 附：脚本索引

`052-quadratic-fewnomial-minus.py` 打印一般法则与 $P_\epsilon$ 表，并输出 `052-quadratic-fewnomial-minus.png`（$\epsilon=0,1,2,2.5$ 时的 $P_\epsilon(e^{it})$）。
