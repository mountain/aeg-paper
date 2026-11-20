# 021 — 平环上的火烧波前：$C_t$、自交计数 = Gauss 圆问题、Gauss 词与扭/解电影

> **文档性质**：算术表达式几何（AEG）研究笔记（021：把"火烧法"波前的**扭转模式**在平环 $\mathbb T^2$ 上做成精确对象、可证公式与可重放脚本）
> **前置依赖**：笔记十八《凯莱模型上的赋值、对偶、加乘分解与 Eikonal 填充》（[018-cayley-assignment-duality-eikonal.md](018-cayley-assignment-duality-eikonal.md)，其中 §6–7 把 Eikonal 方程与"中轴 / Voronoi 脊 / cut locus"定位为火烧法的正确形式）、笔记十九《SC 方共形双曲模型》（[019_sc_square_eikonal.md](019_sc_square_eikonal.md)，径向 Eikonal 填充 = 覆叠里的标准圆）
> **日期**：2026-11-20
> **备注**：本笔记对应脚本 `047-fire-front-twist.py`；所有陈述标状态（`PROVED` / `COMPUTATIONALLY VERIFIED EXAMPLE` / `STRUCTURAL PROPOSAL`）。

---

## 一、对象：覆叠里的圆，商面上的扭转

设 $M=\mathbb T^2=\mathbb R^2/\mathbb Z^2$（单位方平环），基点 $p=0$，万有覆叠 $\widetilde M=\mathbb R^2$，deck 群 $\Gamma=\mathbb Z^2$。火烧法从 $\tilde p=0$ 出发，$t$ 时刻的波前在覆叠里是标准圆

$$\Sigma_t=\{x\in\mathbb R^2:\|x\|=t\},$$

商面上则是**距离圆**

$$C_t=\pi(\Sigma_t)=\big\{\big(t\cos\theta\bmod 1,\ t\sin\theta\bmod 1\big):\theta\in[0,2\pi)\big\}.$$

- $t<\tfrac12$ 时 $C_t$ 是光滑嵌入圆（$\mathrm{inj}(0)=\tfrac12$，半个 systole）；
- $t=\tfrac12$ 时首次自切（self-tangency）；
- $t>\tfrac12$ 后成为带横截自交的浸入圆。

"覆叠里是正圆、商面上一次次扭起又解开"就是 $C_t$ 随 $t$ 的**带参数电影**（`047` 输出 `047-fire-front-twist.gif`，120 帧，$t\in[0.05,2.5]$）。

## 二、自交 = 弦位移是格向量；事件时刻 = 半格长（`PROVED`）

$C_t$ 在 $q$ 处自交，当且仅当圆上有两个不同点 $x,x'$ 满足 $x'\equiv x \pmod{\mathbb Z^2}$，即 $x'-x=v\in\mathbb Z^2\setminus\{0\}$。半径为 $t$ 的圆存在位移为 $v$ 的弦当且仅当 $\|v\|<2t$。因此：

1. 每个 crossing 都由一个非零格向量 $v=(m,n)$ 标注；
2. 它在**事件时刻**出生

$$t=\frac{\|v\|}{2}=\frac12\sqrt{m^2+n^2};$$

3. 事件时刻 = 半格长 = 基点 $(M,p)$ 的**测地回环长度谱**的一半（$M=\mathbb T^2$ 时格长 $\sqrt{m^2+n^2}$，systole $=1$，故首个事件 $t=\tfrac12$）。

对每个**无向**格向量 $\{v,-v\}$，$t>\|v\|/2$ 时恰有**两条平行弦**（两个中点 $\pm\sqrt{t^2-\|v\|^2/4}\cdot\hat v^\perp$），$t=\|v\|/2$ 时合并为一条直径自切。故每越过一个事件，$N(t)$ 跳增 $2\times(\text{该长度上的无向格向量数})$。

**核对**（`COMPUTATIONALLY VERIFIED EXAMPLE`，脚本自检 `len(crossings_at(t)) == N_exact(t)` 全过）：$N(0.49)=0\to N(0.51)=4$（事件 $t=\tfrac12$，$+4$）；$N(0.70)=4\to N(0.71)=8$（$t=\tfrac{\sqrt2}{2}$，$+4$）；$N(0.99)=8\to N(1.01)=12$（$t=1$，$+4$）。

## 三、主结果：$N(t)=r_2(2t)-1$（`PROVED`）

因为每个 crossing 一一对应一个非零格向量 $v$（$\|v\|<2t$），所以自交计数就是

$$N(t)=\#\{v\in\mathbb Z^2\setminus\{0\}:\|v\|<2t\}=r_2(2t)-1,$$

其中 $r_2(R)$ 是**Gauss 圆问题**计数函数。故 $N(t)\sim 4\pi t^2$（面积论证，首项精确）。数值（脚本打印）：$N(2)=44$、$N(3)=108$，与 $4\pi t^2$（$t=3$ 时 $\approx 113.1$）首项吻合。

**结论（可证）**：单位平环上"扩散圆扭转的自交计数"**就是** Gauss 圆问题；每个 crossing 由格向量 $v$ 标注，出生时刻 $t=\|v\|/2$。这是"扭转模式 = 按时间扫出基点长度谱"在零曲率下的最干净裸露。

## 四、Gauss 词（`COMPUTATIONALLY VERIFIED EXAMPLE`）

沿 $C_t$（按 $\theta$ 递增）穿过各 crossing 的**循环序**是其 Gauss 词。脚本对 $t=0.60,0.78,1.10$ 输出：

| $t$ | $N(t)$ | Gauss 词（循环，标号各出现两次） |
|---|---|---|
| 0.60 | 4 | `2 1 0 2 3 0 1 3` |
| 0.78 | 8 | `7 1 4 6 2 4 0 3 6 0 5 7 3 5 1 2` |
| 1.10 | 12 | `4 10 1 6 3 4 8 2 6 0 10 8 5 11 0 7 2 5 9 3 7 1 11 9` |

每个标号恰好出现两次（合法 Gauss code，对应 $C_t$ 是一条浸入圆的横截自交）。Gauss 词编码了"这些格向量的角序如何交错"，是比 $N(t)$ 更细的不变量。

## 五、扭/解的锐化与接口

1. **$N(t)$ 单调阶梯（`PROVED`）**：$N(t)=r_2(2t)-1$ 只增不减——闭曲面上 $C_t$ 不会"解回"简单圆，全局复杂度单调上升；阶梯只在 $t=\|v\|/2$ 处跳。
2. **"解开"是局部 perestroika（`STRUCTURAL PROPOSAL`）**：每次事件处前沿做一次 A/D 型重连（自切 $\to$ 两横截交点），局部图片在下一事件前又"顺滑"下来。这是波前突变（Arnold perestroika）在平环上的显式实例。
3. **cut locus 一致（`PROVED`）**：$0$ 在 $\mathbb T^2$ 上的 cut locus 是 $\{x=\tfrac12\}\cup\{y=\tfrac12\}$（首个自切处），与 018 §7 的"中轴 / Voronoi 脊"一致。
4. **与 paper-3 writhe 的接口（`STRUCTURAL PROPOSAL`）**：$C_t$ 提升到单位切丛 $ST\,\mathbb T^2\simeq\mathbb T^3$ 的接触结构里是 Legendrian 曲线，其 self-linking（Thurston–Bennequin）＝ 扭数的严格版本；可接 paper-3 §08 的 $w:B_n\to\mathbb Z$ 与 Markov 障碍。**尚未在平环上计算**，留作下一步。

## 六、状态汇总

| 结果 | 状态 |
|---|---|
| 自交 ⟺ 弦位移为非零格向量；事件时刻 $t=\|v\|/2$ | `PROVED` |
| $N(t)=r_2(2t)-1$，$N(t)\sim 4\pi t^2$ | `PROVED` |
| 每无向格向量贡献两条弦；每事件跳增 $2\times$（无向向量数）| `PROVED` |
| $N(0.49)=0,0.51=4,0.71=8,1.01=12,2=44,3=108$ | `COMPUTATIONALLY VERIFIED EXAMPLE` |
| Gauss 词（$t=0.60,0.78,1.10$）| `COMPUTATIONALLY VERIFIED EXAMPLE` |
| 平环 cut locus $=\{x=\tfrac12\}\cup\{y=\tfrac12\}$ | `PROVED` |
| "解开"=A/D 型 perestroika；Legendrian/self-linking 接口 | `STRUCTURAL PROPOSAL` |

## 附：脚本索引

`047-fire-front-twist.py` 输出：`047-fire-front-twist-t0_35/0_60/0_78/1_10.png`（覆叠圆 vs 商面折叠，四张快照）、`047-fire-front-twist-nt.png`（$N(t)$ 阶梯 + 事件标注）、`047-fire-front-twist.gif`（120 帧电影）。事件表、Gauss 词、$N(t)$ 采样均由脚本打印（本笔记 §二–§四直接引用）。
