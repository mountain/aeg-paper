# 020 — 凯莱模型上的加乘线、图的势、边值可满足性与尖点 4 边形

> **文档性质**：算术表达式几何（AEG）研究笔记（020：`F₂`/`T₄` 凯莱模型上的「加乘框架订正 → 节点势 → 边值可满足性 → 图着色 → E₁ 型蓝方框 → 尖点 4 边形」）
> **前置依赖**：笔记十七《Cayley 共形双曲统一》（[017-cayley-model-conformal-hyperbolic.md](017-cayley-model-conformal-hyperbolic.md)）、笔记十八《凯莱模型赋值/对偶/Eikonal》（[018-cayley-assignment-duality-eikonal.md](018-cayley-assignment-duality-eikonal.md)）、笔记十九《SC 方盘》（[019_sc_square_eikonal.md](019_sc_square_eikonal.md)）、`paper-0/sections/03-aes-and-motion.tex`（`prop:canonical-arithmetic-frame`）
> **日期**：2026-11-15
> **备注**：本笔记整合 041–046；`040` 的「等值线=加线」结论已由 `041` 订正。

---

## 一、订正：加线 = 水平线，乘线 = 竖直线（041）

`paper-0` 的 `prop:canonical-arithmetic-frame` 中，`J` 是 **`g`-正交旋转**（不是欧氏 90°）。代回

$$X_u=\frac{\mu}{q}E_a-\frac{\lambda a}{q}JE_a,\quad X_v=\frac{\lambda a}{q}E_a+\frac{\mu}{q}JE_a$$

（`q=√(μ²+λ²a²)`）得 **`X_u=(−μy,0)`（水平）、`X_v=(0,−λy)`（竖直）**（sympy 严格核验）。

- **加线** = 水平线 `y=const`（沿它 `a=−x/y` 线性变化）；
- **乘线** = 竖直线 `x=const`（沿它 `a` 按 `1/y` 伸缩）；
- **加 ⊥ 乘 = 90°**（与 `a` 无关）。

**`040` 的错误**：曾把「等值线（射线）」当作加线。等值线 `y=kx`（`k=−1/a`）与加线（水平）的夹角是

$$\angle(\text{level},\text{add})=\arctan(1/|a|),$$

**随 `a` 连续变化**（`a=0` 时 90° 贴乘线；`|a|→∞` 时 0° 贴加线）。这正是评审所指的「夹角和 `a` 值有关」。

## 二、图的势：节点值（042）

**设置**：树节点（4 价分支点，`∇a` 未定义）为奇点，边正则（承载 Eikonal 流），原点补 `a=0`。

沿边 `da/ds=±√(μ²+λ²a²)`，两端满足 `β(v)−β(u)=±λℓ_e`（`β=arcsinh(λa/μ)`）。**树无环 ⟹ 无环绕障碍 ⟹ 解存在**：

$$\boxed{a(\text{node})=\frac{\mu}{\lambda}\sinh\big(\lambda\,d(\text{node})\big)},\quad d=\text{从原点的 }g\text{-路径长}.$$

数值（`μ=1,λ=2`，`g=(dx²+dy²)/L²`）：根边 `g`-长 = `3ln2≈2.079`，节点值 `0→≈16→≈1023`；沿边 `da/ds=√(μ²+λ²a²)` 逐点差 `1e-15`。

## 三、边值可满足性判据（043）

「给定节点值求边值」的**严格 1D 流条件**（边须为特征线）：

$$\boxed{\ell_e=\frac{\big|\operatorname{arcsinh}(\lambda a_v/\mu)-\operatorname{arcsinh}(\lambda a_u/\mu)\big|}{\lambda}}$$

局部即全局（树无环）。检验（`μ=1,λ=2`）：

| 边 | `g`-长 | 奇整数要求 | 结果 |
|---|---|---|---|
| **E₀** `ε₄→Jε₄`（`a:1→−1`）| 1.6227 | 1.4436 | **slack +0.179**（边非特征线）|
| **Cayley**（`a:0→1`）| 3ln2=2.0794 | 0.7218 | **+1.358** 不符 |
| **Cayley**（`a:1→3`）| 2.0794 | 0.5241 | **+1.555** 不符 |

**两读法区分**：
- **2D Eikonal**（`|∇a|=√(…)`，无边长约束）：E₀ 下奇整数**可实现**（`a=−x/y` 全局解）；Cayley 下**不可实现**（Cayley 的 Eikonal 解给 `≈16,1023`）。
- **1D 流**（边为特征线）：两者**都不严格成立**（E₀ 有 slack，Cayley 差更大），唯一严格解是 `a=(μ/λ)sinh(λd)`。

## 四、图的势着色（044）

节点按 `a=(μ/λ)sinh(λd)`（对数色）、边按流速 `√(μ²+λ²a²)` 着色；右图按 `g`-距离 `d` 着色。53 节点，`a:0→6.5×10⁴`，`d:0→6.24`。

## 五、E₁ 型蓝方框（045）

蓝线（对偶 `{4,∞}` 垂直平分线）围成闭合方框（根方框 `[−4,4]²`）。**蓝边界 `a=0` + 内部 Eikonal**：

$$a_{\text{centre}}=\frac{\mu}{\lambda}\sinh(\lambda\cdot\text{inradius}),\quad \text{inradius}=\int\frac{dx}{L}.$$

自相似使 **每个方框 `inradius=ln2`**，故

$$a_{\text{centre}}=\tfrac12\sinh(2\ln2)=\boxed{\tfrac{15}{16}}\quad(\text{所有方框相同}).$$

**关键区分**：无源填充中心恒为 `15/16`；**各不相同的数是中心「源强度」`a(node)`**（`0,16,1023,…`，即势）。所以「E₁ 型 + 中心 puncture 源」正确，但「极点值」应理解为**源强度**。

**± 对称**：`sinh` 奇，`a(d)` 与 `−a(d)` 都满足流方程（`0→−16→−1023` 是合法镜像）。
**逆值对称**：`1/a` **不是** Eikonal 解——`|∇(1/a)|²=λ²b²+μ²b⁴`（四次对偶），仅**值旋转** `a→e^{iθ}a` 是真正的对称。

## 六、尖点 4 边形（046）

蓝方框 4 顶点 = 对偶 `{4,∞}` 顶点 = 原始 `{∞,4}` 面心 = **抛物线尖点 `Q√2 ∪ {∞}`**。把 4 顶点设为奇点，三处形态皆变：

1. **几何**：`E₁`（单 puncture 圆盘）→ **尖点 4 边形**（4 抛物顶点，边上 `a=0`、角上 `a=∞`，混合边界条件）；
2. **势**：节点图 → **节点 + 尖点二部图**（尖点带「尖点势」/极点留数）；
3. **值函数**：单 puncture → **4 尖点 + 中心源** 的复合剖面（恒定 `15/16` 被尖点主导剖面取代）。

## 七、状态汇总

| 结果 | 状态 | 验证 |
|---|---|---|
| `X_u=(−μy,0)`、`X_v=(0,−λy)`，加⊥乘 | `PROVED` | sympy 对 `prop:canonical-arithmetic-frame` |
| 等值线与加线夹角 `arctan(1/|a|)` | `COMPUTATIONALLY VERIFIED` | 数值 |
| `a(node)=(μ/λ)sinh(λd)`，树无环一致 | `PROVED` | 解析 + `1e-15` |
| 可满足性判据 `ℓ_e=|β(Δa)|/λ` | `PROVED` | 解析 + 数值 |
| 奇整数在 Cayley 下不可满足；E₀ 下 2D 可实现但有 1D slack | `PROVED` | 精确数值 |
| 图着色（势/流速） | `COMPUTATIONALLY VERIFIED` | `044` |
| 蓝方框 `inradius=ln2`、无源中心 `15/16` | `PROVED` | 数值 `ln2`/`15/16` |
| 逆值 `1/a` 非 Eikonal 解（四次对偶）| `PROVED`（否证）| 数值 |
| 「E₁ 型 + 中心源强度=势」 | `STRUCTURAL PROPOSAL` | 几何精确，算术语义待定 |
| 4 顶点=尖点、升级为尖点 4 边形 | `STRUCTURAL PROPOSAL`（顶点=尖点为精确对偶）| `016/017` + `046` |

## 附：脚本索引

`041` 加/乘订正 · `042` 节点值 · `043` 可满足性 · `044` 势着色 · `045` E₁ 方框 · `046` 尖点 4 边形。
