# 022 — 双曲火烧波前：三洞球面 $\mathbb H^2/\Gamma(2)$ 上 $N(t)$ = 轨道计数

> **文档性质**：算术表达式几何（AEG）研究笔记（022：把平环火烧波前（021）的方法搬到双曲模型；目标是把"事件时刻 = 半长度谱、自交计数 = 轨道计数"在双曲面上落地）
> **前置依赖**：笔记二十一《平环火烧波前》（[021-fire-front-twist-flat-torus.md](021-fire-front-twist-flat-torus.md)）；笔记十八 §6–7（Eikonal = 火烧法、Voronoi/中轴脊 = cut locus）
> **日期**：2026-11-20
> **备注**：本笔记对应脚本 `048-fire-front-twist-hyperbolic.py`；所有陈述标状态（`PROVED` / `COMPUTATIONALLY VERIFIED EXAMPLE` / `STRUCTURAL PROPOSAL` / `STANDARD CONSEQUENCE`）。

---

## 一、对象：三洞球面 $\mathbb H^2/\Gamma(2)$

取 $M=\mathbb H^2/\Gamma(2)$，其中 $\Gamma(2)$ 是 level-2 主同余子群

$$\Gamma(2)=\Big\{\begin{pmatrix}a&b\\ c&d\end{pmatrix}\in SL(2,\mathbb Z): a,d\text{ 奇},\ b,c\text{ 偶}\Big\}/\{\pm I\},$$

由两个抛物元**自由生成**（经典）：

$$A:z\mapsto z+2,\qquad B:z\mapsto \frac{z}{2z+1},$$

三个尖点为 $\{0,1,\infty\}$，商是**三洞球面**（cusped pair of pants，genus 0、3 个尖点，无挠）。基点 $\tilde p=i$。

波前 $\Sigma_t=\{x:d(\tilde p,x)=t\}$ 是双曲圆（上半平面里仍是欧氏圆，圆心 $i\cosh t$、半径 $\sinh t$）；商面上的距离圆 $C_t=\pi(\Sigma_t)$ 随 $t$ 扭转（脚本 `048` 输出 `048-fire-front-twist.gif`，70 帧，$t\in[0.15,1.7]$，左=覆叠 $\mathbb H$ 里圆与圆相撞，右=商面折叠）。

## 二、一般结论：事件时刻 = 半位移，$N(t)$ = 轨道计数（`PROVED`）

与平环完全同一论证（见 021 §2，把格向量换成 deck 元）：

1. $C_t$ 在 $q$ 自交 ⟺ 存在 $\gamma\neq e$ 使圆上两点 $x,\gamma x$ 均距 $\tilde p$ 为 $t$，即 $x\in\Sigma_t(\tilde p)\cap\Sigma_t(\gamma^{-1}\tilde p)$；
2. 这两个双曲圆相交当且仅当 $\|\gamma\|:=d(\tilde p,\gamma\tilde p)<2t$，所以每个 crossing 在**事件时刻** $t=\tfrac12\|\gamma\|$ 出生；
3. 每个**无向**类 $\{\gamma,\gamma^{-1}\}$ 贡献两个横截 crossing（两圆的**两个**交点），$t=\tfrac12\|\gamma\|$ 时合并为一个自切。

于是

$$N(t)=\#\{\gamma\in\Gamma(2)\setminus\{e\}:d(\tilde p,\gamma\tilde p)<2t\},$$

即**轨道计数函数**（orbital counting）——平环的 $N(t)=r_2(2t)-1$（Gauss 圆问题）在双曲面的推广：把 $\mathbb Z^2$ 的格长换成 $\Gamma(2)$ 的双曲位移。事件时刻 $=\tfrac12\times$ 基点 $(M,p)$ 的**测地回环长度谱**。

## 三、$\Gamma(2)$ 上的计算（`COMPUTATIONALLY VERIFIED EXAMPLE`）

生成元位移 $\|A\|=\|B\|=\operatorname{arcosh}3\approx1.7627$，故**首个事件** $t=\tfrac12\operatorname{arcosh}3\approx0.8814$（$+4$，两个无向类 $\{A\},\{B\}$ 各两条弦）。事件表（脚本打印，按 $\|\gamma\|$ 排序）：

| $t=\|\gamma\|/2$ | $\gamma$（无向类的代表） | $N(t)$ 跳增 |
|---|---|---|
| $0.8814$ | $A,\ B$ | $0\to4$ |
| $1.4436$ | $AA,\ BB,\ Ab,\ Ba$ | $4\to12$ |
| $1.7627$ | $AB,\ BA$ | $12\to16$ |
| $1.8184$ | $AAA,\ BBB,\ AbA,\ BaB$ | $16\to24$ |
| … | … | … |

采样：$N(0.5)=0$、$N(0.89)=4$、$N(1.5)=12$、$N(1.8)=16$、$N(2.1)=32$。脚本自检：`len(crossings_at(t))==N_exact(t)` 且每个 crossing 的两个原像 $\{z,\gamma z\}$ 都在 $\Sigma_t$ 上（$d(\tilde p,z)=d(\tilde p,\gamma z)=t$）——全过。

**枚举完备性（诚实声明）**：约化词枚举到深度 $12$（保留 $\|\gamma\|\le5.0$ 共 72 个词）；深度 $11$ vs $12$ 在 $\|\gamma\|<4.4$ 的谱上**STABLE**（40 个词一致）。但对**尖点群**，$A^k$ 的位移 $\sim2\log k$（抛物方向增长极慢），故朴素的"按词深度的完备性判据"不可用；严格完备需要 horoball 修正。本笔记把它列为 `STANDARD CONSEQUENCE` 之外的**未决点**，不冒充完整证明。

## 四、Gauss 词（`COMPUTATIONALLY VERIFIED EXAMPLE`）

| $t$ | $N(t)$ | Gauss 词（循环） |
|---|---|---|
| 0.95 | 4 | `1 1 0 3 2 2 3 0` |
| 1.25 | 4 | `1 1 0 3 2 2 3 0` |
| 1.60 | 12 | `5 1 1 5 4 10 11 0 3 11 10 7 6 2 2 6 7 9 8 3 0 8 9 4` |

（$t=0.95$ 与 $t=1.25$ 词相同：两次事件之间无新 crossing 诞生，Gauss 词在事件区间内不变；连续出现的 `1 1`、`2 2` 是刚在 $t=0.8814$ 出生的"年轻"crossing，两个角序点仍紧邻。）

## 五、增长：指数速率 = 临界指数 $\delta=1$（`STANDARD CONSEQUENCE` + `COMPUTATIONALLY VERIFIED`）

轨道计数（脚本打印）：$R=2\to4$、$R=3\to12$、$R=4\to24$、$R=4.4\to40$。比值 $\#/e^R\approx0.5$ 基本稳定，与有限面积带尖点 Fuchsian 群的轨道增长 $\#\{\gamma:\|\gamma\|\le R\}\sim C\,e^{\delta R}$（$\delta=1$）一致（Patterson/Margulis）。故 $N(t)\sim C\,e^{2t}$（$N(t)$ 的自变量是 $t$，增长指数 $\approx2\delta=2$）。对照平环的 $N(t)\sim4\pi t^2$：**平环多项式增长、双曲三洞球面指数增长**——这正是负曲率"扭转模式"以指数速度变复杂的定量体现。

## 六、SC 方 / $\{4,\infty\}$ 的接口（`STRUCTURAL PROPOSAL`，未实现）

SC 方 $\mathcal Q_e$ 的 deck 群 $\Gamma_4=\langle J,T\rangle\cong C_2*C_4$（笔记 019）**有挠**（2 阶、4 阶椭圆元 → 锥点）。此时：
- 无挠群上"crossing ↔ 无向 deck 元"的一一对应会因椭圆元（$\gamma^n=e$、锥点回环）而需要修正；
- 锥点处波前会产生 cusp/反射奇点（不再是纯横截自交）。

因此 SC 方需要先把椭圆元/锥点的贡献单独列出来，再套用 §2 的无挠骨架。**留作下一步**。

## 七、状态汇总

| 结果 | 状态 |
|---|---|
| 事件时刻 $t=\tfrac12\|\gamma\|$；每无向类两条弦 | `PROVED` |
| $N(t)=\#\{\gamma\neq e:\|\gamma\|<2t\}$ | `PROVED` |
| $\Gamma(2)=\langle A,B\rangle$ 自由、三尖点 $\{0,1,\infty\}$、商 = 三洞球面 | `STANDARD CONSEQUENCE` |
| 首事件 $t=0.8814$；$N(0.5)=0,1.5=12,1.8=16,2.1=32$ | `COMPUTATIONALLY VERIFIED EXAMPLE` |
| 枚举深度 11 vs 12 STABLE（$\|\gamma\|<4.4$）| `COMPUTATIONALLY VERIFIED EXAMPLE` |
| 尖点群严格完备需 horoball 修正 | `STRUCTURAL PROPOSAL`（未决点）|
| Gauss 词（$t=0.95,1.25,1.60$）| `COMPUTATIONALLY VERIFIED EXAMPLE` |
| $N(t)$ 指数增长、速率 $\approx2\delta=2$ | `STANDARD CONSEQUENCE` + `COMPUTATIONALLY VERIFIED` |
| SC 方 $\{4,\infty\}$ 需椭圆元/锥点修正 | `STRUCTURAL PROPOSAL` |

## 附：脚本索引

`048-fire-front-twist-hyperbolic.py` 输出：`048-fire-front-twist-t0_50/0_95/1_25/1_60.png`（覆叠 $\mathbb H$ vs 商面折叠，四张快照）、`048-fire-front-twist-nt.png`（$N(t)$ 阶梯 + 事件词标注）、`048-fire-front-twist.gif`（70 帧电影）。事件表、$N(t)$ 采样、Gauss 词、轨道增长、稳定性检查均由脚本打印（§三–§五直接引用）。
