# 024 — 尖点诞生：fewnomial 的弦和 vs 火烧波前的弦差

> **文档性质**：算术表达式几何（AEG）研究笔记（024：把有限层指数多项式 [notes/algebra/01](../algebra/01-finite-layer-exponential-polynomials.md) §3 与火烧波前 [021](021-fire-front-twist-flat-torus.md) 之间的单句联系写下来）
> **日期**：2026-11-20
> **备注**：对应脚本 `051-fewnomial-firefront-comparison.py`；状态见下。

---

## 一、两个弦条件

单位圆上取 $u=e^{i\theta_1}$、$v=e^{i\theta_2}$。

**(a) fewnomial。** 对 $P_\epsilon(V)=V^2+\epsilon V+1$，
$$P_\epsilon(V)-P_\epsilon(W)=(V-W)(V+W+\epsilon),$$
故自交（$V\neq W$）恰是**弦和**条件
$$V+W=-\epsilon.$$
可解当且仅当 $|\epsilon|\le2$（因 $|V+W|\le2$）。相图：$\epsilon=0$ 同一圆走两遍；$0<\epsilon<2$ 原点一个横截 node；$\epsilon=2$ 尖点；$\epsilon>2$ 光滑简单闭曲线（`PROVED`，[algebra/01 §3](../algebra/01-finite-layer-exponential-polynomials.md)）。

**(b) 火烧波前（平环）。** $C_t(\theta)=(t\cos\theta,\,t\sin\theta)\bmod 1$。标注为 $v\in\mathbb Z^2\setminus\{0\}$ 的 crossing 满足 $t(u-v)=v$，即**弦差**条件
$$u-v=\frac{v}{t},$$
可解当且仅当 $t\ge|v|/2$（因 $|u-v|\le2$）。$t=|v|/2$ 时两分支相切（诞生），$t>|v|/2$ 横截（`PROVED`，[021](021-fire-front-twist-flat-torus.md)）。

## 二、互补性：平行四边形律

对单位圆上两点，
$$|u-v|^2+|u+v|^2=2(|u|^2+|v|^2)=4.$$
于是两个诞生条件是**互补的直径**：

- 火烧波前诞生在 $t=|v|/2$ ⟺ $|u-v|=2$ ⟺ $u=-v$（**对径**）；
- fewnomial 诞生在 $|\epsilon|=2$ ⟺ $|u+v|=2$ ⟺ $u=v$（**重合**）。

两者是同一种 $A_2$（尖点）perestroika，一次经弦**差**、一次经弦**和**读出。这就是 [021 §5](021-fire-front-twist-flat-torus.md)"解开=局部重连"的解析形式。

## 三、字典

| | fewnomial $P_\epsilon$ | 火烧波前 $C_t$ |
|---|---|---|
| 参数圆 | $|V|=1$ | $T_p\,\mathbb T^2$ 里的 $S^1$ |
| 谱（频率） | 有限指数集 $\{0,1,2\}$ | 格 $\mathbb Z^2$（长度谱） |
| 两点条件 | 弦**和** $V+W=-\epsilon$ | 弦**差** $u-v=v/t$ |
| 尺度参数 | 系数比 $\epsilon$ | 半径 $t$ |
| 诞生 | $|\epsilon|=2$（重合） | $t=|v|/2$（对径） |
| 计数 | 1 个 node（有限） | $N(t)=r_2(2t)-1$（无穷） |

所以 fewnomial 是火烧波前的**有限谱截断**：把指数集 $\{0,1,2\}$ 换成完整格 $\mathbb Z^2$，就从"一个系数控制的一个 node"过渡到"长度谱控制的 Gauss 圆计数"。两个逆问题（"自交模式能否决定谱数据"）于是成为有限 vs 无穷频率下的同一个问题（`STRUCTURAL PROPOSAL`；参 [023](023-gauss-word-alignment.md) 的标记/未标记讨论）。

## 四、状态

| 结果 | 状态 |
|---|---|
| fewnomial 自交 ⟺ $V+W=-\epsilon$；相图 | `PROVED` |
| 火烧波前 crossing ⟺ $t(u-v)=v$；诞生于 $t=|v|/2$ | `PROVED` |
| 平行四边形律 $|u-v|^2+|u+v|^2=4$；对径/重合对偶 | `PROVED` |
| fewnomial = 火烧波前的有限谱截断 | `STRUCTURAL PROPOSAL` |
| 图 `051-fewnomial-firefront-comparison.png` | `COMPUTATIONALLY VERIFIED EXAMPLE` |

## 附：脚本索引

`051-fewnomial-firefront-comparison.py` 输出 `051-fewnomial-firefront-comparison.png`：上排 $P_\epsilon(e^{it})$（$\epsilon=2.5,2.0,1.2$）；下排折叠距离圆 $C_t$（$t=0.4,0.5,0.6$）。
