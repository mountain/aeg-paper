# OQ-099 candidate: the *scope* of the constant-boundary capping obstruction

日期：2026-10-31。状态：**SCOPE ANALYSIS（v2）+ COMPUTATIONALLY VERIFIED EXAMPLE**。
各命题状态逐条标注（`AGENTS.md` 的 status-label 约定）。**修订记录见 §7：v1 有一条错误已撤回。**

**方向**：苑明理。**构造、检查器与文字**：DeepSeek Harness agent（deepseek-v4-flash-vision-exp）。
**构造与接收同一作者，不构成独立实现或人工复核。**

**阅读基线**：AEG `3b82ed8`。本目录**不改动** `paper-1/` 下任何文件；结论以"建议稿动作"给出。

---

## 1 问题

Paper I 的常值边界封盖阻碍（`thm:constant-boundary-capping-obstruction`，印为 Thm 10.12）：

> 设 $D$ 紧光滑圆盘、$g$ 光滑黎曼度规、$a\in C^\infty(D)$、$\mu\ne0$、$\lambda\in\mathbb R$。
> 不存在数据 $(g,a)$ 使 $\lvert da\rvert_g^2=\mu^2+\lambda^2a^2$ 于 $\operatorname{int}D$、且 $a\vert_{\partial D}=c$（常数）。

推论（`cor:capping-dichotomy`，10.14（2026-11-01 前为 10.13））第 (2) 条：要在几何上封盖一条水平圆，
**必须**允许一个内部临界点或非 $C^1$/度规奇点。

同仓库另有孔–盘互补（`thm:hole-disk-complementarity`，10.4）：同一个缝圆在**体内可填充**。

两个问题：

- **Q1（范围）**：Thm 10.12 的假设里哪一条**是紧的**？去掉会怎样？
- **Q2（推论空性）**：Cor 10.14(2) 的"允许奇点即可"是**真的非空**，还是只是没被排除？

---

## 2 结论

### A1 — 已证的阻碍只用到 $\mu\ne0$〔`proved with stated hypotheses`〕

证明的三步只用 $\lvert da\rvert_g^2=\mu^2+\lambda^2a^2\ge\mu^2>0$（当 $\mu\ne0$）⇒ $\operatorname{int}D$ 上 $da\ne0$；
再由"常值边界 + 非常值 ⇒ 内部极值"矛盾。
⇒ **已证的这条是充分条件，且与 $g$、$\lambda$ 无关。**

### A2 — 退化情形**有**光滑封盖〔`proved`〕

| 情形 | 显式解 | 恒等式 |
|---|---|---|
| $\mu=0$ 且 $\lambda=0$ | $a\equiv c$ | $\lvert da\rvert^2=0=\mu^2+\lambda^2a^2$ ✓ |
| $\mu=0$ 且 $c=0$ | $a\equiv 0$ | 同上 ✓ |

⇒ Thm 10.12 的结论**不能**外推到整个 $\mu=0$ 平面；退化点恰是 $\mu=0$ 且 $\lambda c=0$。

### A3 — $\mu=0,\ \lambda\ne0,\ c\ne0$ **也**被阻碍，但机制不同〔`partially proved`〕

在 $\{a\ne0\}$ 上令 $u=\log\lvert a\rvert/\lvert\lambda\rvert$，则 $\lvert du\rvert=1$
（因为 $du=da/(\lambda a)$，与 $\lvert da\rvert=\lvert\lambda\rvert\lvert a\rvert$ 等价 —— 已符号核对）。
于是两条：

1. $\lvert du\rvert=1$ 的水平集是**等距集**；$u$ 在 $\partial D$ 上为常数 ⇒ 圆是 $u$ 的水平集
   ⇒ 近旁 $u=k\mp d_g(\cdot,\partial D)$ ⇒ 在内部**割迹/中轴**上 $u$ 不光滑（紧区域中非空）；
2. 光滑的 $a$ **不能**在内部某点为零：若 $a\sim r^m$（$m\ge1$），则
   $\lvert da\rvert/\lvert a\rvert\sim m/(\lvert\lambda\rvert r)\to\infty$，与 $\lvert da\rvert=\lvert\lambda\rvert\lvert a\rvert$ 矛盾
   （已符号核对，极限为 $\infty$）。

⇒ **$\mu\ne0$ 是充分而非必要**。

### A4 — 尖锐条件

$$\boxed{\text{光滑封盖存在}\iff \mu=0\ \text{且}\ \lambda c=0}$$

（$\Leftarrow$：A2；$\Rightarrow$：$\mu\ne0$ 用 A1，$\mu=0,\lambda\ne0,c\ne0$ 用 A3。）

### A5 — $\mu\ne0$ 时**显式**存在一个奇异封盖〔`proved`，$+$ `computationally verified example`〕

$$a(r)=\frac{\mu}{\lambda}\sinh\big(\lambda(r+C)\big)
\ \Longrightarrow\ (a')^2=\mu^2\cosh^2\big(\lambda(r+C)\big)=\mu^2+\lambda^2a^2$$

方程在**穿孔圆盘**上逐点成立（符号恒等式）；$C$ 由 $a(1)=c$ 定。圆心处

$$a(r)=A+B\,r+O(r^2),\quad A=\frac{\mu}{\lambda}\sinh(\lambda C),\ B=\mu\cosh(\lambda C)\ne0,$$

沿 $+x$ 与 $-x$ 的单侧展开为 $A\pm Bx$，**相差 $2B\ne0$** ⇒ $C^0$ 但非 $C^1$。
**奇点恰好是一个内部点，圆锥型。**

⇒ Cor 10.14(2) 的那一支**非空**（不只是"允许"）。
数值实例 $\mu=\lambda=1,c=2$：$a(1)=2.000000000000$，PDE 相对残差 $1.8\times10^{-16}$。

### A6 — 奇点可搬到任意内点〔`proved`〕

对保持 $\partial D$ 逐点的微分同胚 $\varphi$，$\big(a\circ\varphi^{-1},(\varphi^{-1})^*g\big)$
满足同一方程、边界值不变、奇点移到 $\varphi(p_0)$（拉回度规的定义）。
⇒ Thm 10.12 是关于**正则类**的陈述，不是关于某个特殊圆心的陈述。

### A7 — 拓扑那半边已在本仓库〔`standard consequence requiring an in-paper proof`〕

`research/pants-interface-disks/`（OQ-096 V1）已用精确模 2 秩验证
$\lvert C\rvert\ne0\in H_1(S;\mathbb F_2)$（秩 $110\to111$）而 $C=\partial D$ 在体内成立。
⇒ 拓扑可填充（10.4）与解析可填充（10.12）是两件事；**A5 补上中间一档：带一个允许奇点的可填充性。**

---

## 3 判定

| 问题 | 判定 |
|---|---|
| Q1：Thm 10.12 的假设是否紧 | **不紧**：$\mu\ne0$ 充分而非必要；尖锐条件是 $\mu=0\wedge\lambda c=0$（A2+A3） |
| Q2：Cor 10.14(2) 是否非空 | **非空且可构造**（A5），奇点位置可任意指定（A6） |

---

## 4 建议的正文动作（**未应用**）

- **选项 1（最小）**：在 Thm 10.12 后加一条 remark：$\mu\ne0$ 充分而非必要，尖锐条件是 $\mu=0\wedge\lambda c=0$；
- **选项 2（更强）**：把 iff 条件单独写成一条 proposition，引用 A3 的两条标准事实，Thm 10.12 保留为简短的充分陈述；
- 在 Cor 10.14 后加 remark 给出 A5 那一族，使第 (2) 支"已知非空"；
- **不改** Thm 10.12 的假设清单，**不改** Cor 10.14 的措辞。

---

## 5 已执行的检查

`verify_capping.py`（`sympy` + 标准库）：

| 编号 | 检查 | 结果 |
|---|---|---|
| A1 | $\mu^2+\lambda^2a^2\ge\mu^2$ 的符号恒等式 | ✓ |
| A2 | 两个退化族的恒等式 | ✓ |
| A3 | $du\cdot(\lambda a)=da$ 恒等式；圆的等距水平集含 $r$ 的奇次幂 | ✓ / ✓ |
| A3b | 内部零点的 $\lvert da\rvert/\lvert a\rvert\to\infty$ | $+\infty$ |
| A5 | $\sinh$ 族的方程恒等式；$C$ 由 $a(1)=c$ 解出 | ✓ |
| A5b | 单侧展开差 $2B$ | ✓ |
| A5c | $\mu=\lambda=1,c=2$，6 个半径上的 PDE 残差 | $\le2\times10^{-16}$ |
| A6/A7 | 陈述 + 引用（非计算） | — |

证据：`evidence-capping.json`。复跑：

```sh
python3 verify_capping.py --check
python3 verify_capping.py > evidence-capping.json
```

---

## 6 边界

1. **没有重证** Thm 10.12，也没有修改它。
2. **A3 是机制，不是完整证明**：它依赖两条标准事实（$\lvert du\rvert=1$ ⇒ 水平集是等距集；
   紧区域中闭曲线的距离函数在非空的内部集合上不光滑）。本目录只核了它的**代数步骤**。
3. A2、A5 在**平坦度规**上构造；定理本身对任意光滑 $g$ 陈述。只有**阻碍**那一步是度规无关的。
4. 只考察圆锥型奇点；Cor 10.14(2) 的另一半（内部临界点）**未构造**。
5. 未讨论 $\mu,\lambda$ 与 AES 数据（加性/乘性荷）的归一化关系 —— 这里把它们当作方程参数。
6. 与 `notes/analysis-and-calculus/25-*` 的相关表述**未逐条对照**。
7. 未加 CI workflow（若需要，可仿 `pants-interface-disks.yml` 另开一张）。

---

## 6.5 同时交付：`PROPOSED-REMARK.tex`

按论文风格写好的**草稿**（两条 remark：`rem:capping-scope-mu-essential` 与
`rem:capping-singular-branch-nonempty`），**未应用到正文**。
插入位置写在文件头部注释里（Thm 10.12 之后 / Cor 10.14 之后）。
是否采用、以及如何与 `governance/03-theorem-dependency-graph.md` 对齐，由作者决定。

---

## 7 修订记录（不覆盖，保留）

**v1（同日，已撤回）**：曾断言"$\mu=0$ 时对每个常数 $c$ 都可**光滑**封盖"，用的族是平坦圆盘上的
$a(r)=c\,e^{\lambda(r-1)}$。**这是错的**：该族作为 $r$ 的函数解析，但作为 $(x,y)$ 的函数**不是** $C^\infty$
——它在 $r=\sqrt{x^2+y^2}$ 处含奇次幂。

**v2（本文件）**：改为 A2/A3 的二分：退化情形（$\mu=0\wedge\lambda c=0$）才有光滑封盖；
$\mu=0,\lambda\ne0,c\ne0$ 仍然被阻碍（A3 的等距机制）。尖锐条件变为 A4 的 iff。

教训记在这里：**"在 $r$ 上解析"不等于"在 $(x,y)$ 上光滑"**；本目录所有径向构造都必须过这一关。
