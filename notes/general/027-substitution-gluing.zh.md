# 027 — 代入 = 拼接：火烧法作为复合的接口

> **文档性质**：算术表达式几何（AEG）研究笔记（027：一条结构提案——火烧法把算术程序的**代入**变成带孔 AEG 曲面的**拼接**）
> **日期**：2026-11-20
> **状态**：地基事实 `PROVED`；对应关系本身是 `STRUCTURAL PROPOSAL` 加三个 `OPEN PROBLEM`；无新计算。

---

## 一、地基：火烧法是 AES 的求值，不是类比

笔记 [018 §6](018-cayley-assignment-duality-eikonal.md) 已记录 Eikonal 方程
$$|\nabla a|^2=\mu^2+\lambda^2 a^2$$
是 regular-AES 公理，即**火烧法是 AES 的几何形式**。于是到达时间（波前 $C_t$）**就是**值，$C_t$ 扫过曲面的轨迹**就是**有序求值历史。没有需要"额外附加"的东西：火烧法就是计算本身。

## 二、三层对应

| 算术 / 计算 | 几何（火烧法） |
|---|---|
| 表达式（带输入槽） | 带孔（=尖点）AEG 曲面 |
| **代入**（复合，把子式塞进槽） | **沿尖点拼接** |
| 有序求值历史 | 波前 $C_t$ 扫过曲面 |
| 值（终点） | node / 波前到达之处 |

"代入 = 拼接" 之所以成立，正是 [algebra/01 §2](../algebra/01-finite-layer-exponential-polynomials.md) 的复合/回拉结构——$\operatorname{ev}(D_*\gamma,\varphi)=\operatorname{ev}(\gamma,D^*\varphi)$、$(E\circ D)^*=D^*\circ E^*$——的几何读法：一张曲面的孔里流出的波前，就是另一张曲面槽里流进的输入。代入就是要求**波前在拼接处连续**。

## 三、接口数据（火烧法贡献的东西）

021–026 恰好算出了拼接处必须匹配的局部数据：

1. **cut locus = 拼接缝**（[018 §7](018-cayley-assignment-duality-eikonal.md)、[021](021-fire-front-twist-flat-torus.md)）：火烧法基本域的墙就是火与其 deck 副本的相撞轨迹（Voronoi/中轴脊）。相撞点就是未来的"槽位"。
2. **半/全时钟**（[026](026-firefront-trichotomy.md)）：crossing 在 $t=\|\gamma\|/2$ 诞生（两股火相切），波前在 $t=\|\gamma\|$ 抵达 deck 像 $\gamma p$。子式的**全位移到达**就是父式槽位的**输入时刻**。
3. **方向圆**（[023](023-gauss-word-alignment.md)）：crossing 的渐近方向是垂直平分线的边界端点——拼接时须对齐的相位/角度。

## 四、提案

> **结构提案（代入 = 拼接）。** 沿尖点拼接的两张带孔 AEG 曲面，对应由代入复合的两个算术程序，当且仅当它们在拼接尖点处的**波前到达结构匹配**：到达时刻（半/全位移）、方向（平分线端点）、相撞图样（cut locus）。这个匹配就是代入规则的几何化——子式的输出流 = 父式槽位的输入流。

## 五、开放问题

1. **精确匹配条件。** 尖点处波前沿 horocycle 逼近；两侧 horocycle 流要怎样对齐（Fenchel–Nielsen twist 参数的带尖点版）才构成合法代入，尚未写出精确方程。
2. **谱的分解。** 拼接后曲面的长度谱、$N(t)$、cut locus 如何从两张分量的对应量**组合**出来？这是代入规则在谱数据层面的形式；若形式干净，它就是"代入的算术"。
3. **尖点 vs 有限边界。** 021–026 的机器建在**尖点**三洞球面 $\Gamma(2)$ 上；有限长边界的裤子需要先把半/全时钟与 cut locus 搬到有限边界长，才能得到完整的 Fenchel–Nielsen 图景。

## 六、状态

| 结果 | 状态 |
|---|---|
| 火烧法 = Eikonal = AES 公理 | `PROVED`（[018 §6](018-cayley-assignment-duality-eikonal.md)） |
| 代入 = 拼接，作为复合的几何形式 | `STRUCTURAL PROPOSAL` |
| cut locus / 半全时钟 / 方向圆作为接口数据 | `PROVED`（021–026） |
| 尖点匹配的精确条件 | `OPEN PROBLEM` |
| 拼接曲面的谱分解 | `OPEN PROBLEM` |
| 有限边界裤子的移植 | `OPEN PROBLEM` |
