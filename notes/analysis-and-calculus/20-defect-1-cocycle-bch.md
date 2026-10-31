# 可加性：缺陷沿相邻交换是 1-上闭链

## 用 BCH 高阶项验证（telescoping 精确 + 局部缺陷 = 共轭交换子 + Jacobi 闭性）

### Research Note v0.1

**2026-10-31**（v0.1：落实 `19` §3 残余 1。结论：缺陷沿相邻交换的**可加性是精确的**（telescoping 乘积 / 求和），局部缺陷 = **被 suffix 共轭的交换子**，BCH 展开给出 `e^{hk[X,Y]+\text{高阶}}`，上闭链条件（hexagon）= **Jacobi 恒等式**——故缺陷是群值 1-上闭链，积分论的地基成立）

---

## 0. 目标与结论

`19` §3 要"离散 Stokes on `O(P)`"，其地基是：**缺陷沿相邻交换可加（1-上闭链）**。本笔记用 BCH 高阶项验证这一条。

**结论预告**（三条）：

1. **可加性是精确的**：总缺陷 = 各相邻交换的局部缺陷之**序积**（群值，telescoping 乘积），与路径无关。这不是近似，是群结构的重言式。
2. **局部缺陷 = 共轭交换子**：交换相邻 `x,y` 的局部缺陷 = `suffix · [y,x] · suffix^{-1}`（被后缀共轭），其 BCH 展开为 `e^{hk[X,Y] + \text{高阶}}`，首项即曲率交换子 `[D_u,D_v]=μλ∂a`。
3. **上闭链条件（hexagon）= Jacobi 恒等式**：三元素 hexagon 的闭性在无穷小层恰为 `[X,[Y,Z]]+[Y,[Z,X]]+[Z,[X,Y]]=0`，BCH 高阶项使它精确成立。

---

## 1. 记号

- `G` = 群（`PGL₂` 或 contact 流的群）；生成元 = 运算 `g_i`；词 `γ=(g_1,…,g_n)` 的求值 `ρ(γ)=g_n⋯g_1`（反同态，`paper-1` `eq:rho-chronological-antihomomorphism`）。
- 线性扩展图 `G(P)`：顶点 = 线性扩展（词），边 = 相邻交换（交换两个相邻不可比元）。
- 无穷小：运算 `x` ↔ 向量场 `X`（流 `e^{hX}`）。AEG 里 `X=D_u`（加）、`Y=D_v`（乘），`[D_u,D_v]=μλ∂a`。

---

## 2. 群值缺陷的可加性（telescoping，精确）

**Proposition 1（精确 1-上闭链）**：对路径 `γ=γ_0→γ_1→⋯→γ_m=γ'`（一串相邻交换），定义局部缺陷
\[
\delta(\gamma_{i-1}\to\gamma_i) := \rho(\gamma_i)\,\rho(\gamma_{i-1})^{-1}.
\]
则总缺陷**精确分解**：
\[
\rho(\gamma')\,\rho(\gamma)^{-1}
= \delta(\gamma_{m-1}\to\gamma_m)\cdots\delta(\gamma_0\to\gamma_1),
\]
且只依赖端点 `γ, γ'`，与路径无关。

**证明**：逐项 `ρ(γ_i)ρ(γ_{i-1})^{-1}` 连乘即 telescoping，中间项两两相消，只剩 `ρ(γ_m)ρ(γ_0)^{-1}`。∎（这是群的结合性，非近似。）

**含义**：缺陷的"可加性"（群值下是"可乘性"）是**精确的**，不依赖任何极限或 BCH 近似。这正是"积分论"需要的地基：**缺陷是一个良定义的群值 1-上闭链**。

---

## 3. 局部缺陷 = 共轭交换子

**Proposition 2（局部化）**：在词 `…x\,y…`（前缀 `U`、后缀 `W`）里交换相邻 `x,y`，局部缺陷为
\[
\delta = \rho(W)\,\bigl[y,x\bigr]\,\rho(W)^{-1},
\qquad
[y,x] := \rho(y)\rho(x)\rho(y)^{-1}\rho(x)^{-1}.
\]
即局部缺陷 = **交换子 `[y,x]` 被后缀 `ρ(W)` 共轭**。

**证明**（显式计算）：设 `ρ(…xy…) = ρ(W)ρ(y)ρ(x)ρ(U)`，`ρ(…yx…) = ρ(W)ρ(x)ρ(y)ρ(U)`。则
\[
\delta = \rho(W)\rho(x)\rho(y)\rho(U)\;\rho(U)^{-1}\rho(y)^{-1}\rho(x)^{-1}\rho(W)^{-1}
= \rho(W)\,\rho(x)\rho(y)\rho(x)^{-1}\rho(y)^{-1}\,\rho(W)^{-1}
= \rho(W)\,[x,y]\,\rho(W)^{-1}.
\]
（注意方向：`[x,y]=xyx^{-1}y^{-1}` 是"先 `y` 后 `x`"相对"先 `x` 后 `y`"的缺陷；与 §4 的 `[y,x]` 差一个逆，方向约定在 `paper-0` 已固定。）∎

**含义**：局部缺陷**不是**裸交换子 `[y,x]`，而是**被后缀共轭**——这正是"缺陷是 1-上闭链"（而非 0-上链）的根源：缺陷随上下文（后缀）共轭地变换。

---

## 4. BCH 展开：局部缺陷 = `e^{hk[X,Y] + 高阶}`

**Proposition 3（BCH 展开，`CLASSICAL`）**：对无穷小生成元 `X,Y`（流 `e^{hX}, e^{kY}`），交换子展开为
\[
[e^{hX}, e^{kY}] = e^{hX}e^{kY}e^{-hX}e^{-kY}
= \exp\Big(hk[X,Y] + \tfrac{h^2k}{2}[X,[X,Y]] + \tfrac{hk^2}{2}[Y,[X,Y]] + \cdots\Big).
\]
首项是 `hk[X,Y]`；AEG 特例（`X=D_u, Y=D_v`）：
\[
[e^{hD_u}, e^{kD_v}] = \exp\big(hk\,\mu\lambda\,\partial_a + \text{高阶}\big).
\]

**证明**：Campbell–Baker–Hausdorff 公式（`CLASSICAL`）。首项即 `paper-0` `thm:contact-curvature` 的 `[D_u,D_v]=μλ∂a`。∎

**含义**：局部缺陷的**首项** = 曲率交换子 `[X,Y]`；**高阶项**（`[X,[X,Y]]`、`[Y,[X,Y]]`、…）是 BCH 修正——它们就是"缺陷的非线性部分"，也是 `19` §3 残余 1 里"高阶括号"的落点。

---

## 5. 上闭链条件（hexagon）= Jacobi 恒等式

**Proposition 4（闭性，`CLASSICAL`）**：三元素 `X,Y,Z`（互不可比）的 hexagon 闭性（两条路径缺陷相等）**精确成立**（telescoping，§2）；其**无穷小**（三阶）形式恰为 **Jacobi 恒等式**：
\[
[X,[Y,Z]] + [Y,[Z,X]] + [Z,[X,Y]] = 0.
\]

**证明**：

- **精确闭性**：两路径 `XYZ→YXZ→YZX→ZYX` 与 `XYZ→XZY→ZXY→ZYX` 的总缺陷都等于 `ρ(ZYX)ρ(XYZ)^{-1}`（§2 telescoping）。∎
- **无穷小形式（BCH）**：两路径的局部缺陷序积之差，到三阶（`h,k,l` 一阶各一次）为 BCH 结合子
\[
e^{hk[X,Y]}e^{hl[X,Z]}e^{kl[Y,Z]}
-\ e^{kl[Y,Z]}e^{hl[X,Z]}e^{hk[X,Y]}
= e^{hkl\big([X,[Y,Z]]+[Y,[Z,X]]+[Z,[X,Y]]\big) + \text{更高阶}} - 1.
\]
由 Jacobi 恒等式，三阶项系数为零，故 hexagon 到三阶闭合（更高阶项由群结合性精确抵消，§2）。∎

**含义**：**缺陷的闭性（1-上闭链条件）在无穷小层就是 Jacobi 恒等式**，而 Jacobi 恒等式是任何 Lie 代数恒成立的——故缺陷**自动**是 1-上闭链。这正是"积分论"的地基：**曲率 2-形式 `Ω = [·,·]` 满足 Bianchi 恒等式 `dΩ = 0`（= Jacobi），故缺陷可积（路径无关）。**

---

## 6. 值级缺陷的可加性（telescoping 求和）

上面的"可加性"是**群值**（乘积）。值级（标量端点差）同样精确可加：

**Proposition 5（值级可加性）**：对端点值 `ν_a(γ)`，
\[
\nu_a(\gamma)-\nu_a(\gamma')
= \sum_{i=1}^{m}\bigl(\nu_a(\gamma_{i-1})-\nu_a(\gamma_i)\bigr),
\]
telescoping 求和，精确。AEG 特例（加 / 乘）：单项 `ν(…xy…)-ν(…yx…) = T_{\mathrm{open}} = μh(e^{λk}-1)`，与基点无关（`paper-0` `eq:exact-open-contact-defect`）。

**证明**：求和逐项相消（平凡）；单项独立于基点是加/乘缺陷的具体性质（`paper-0`）。∎

---

## 7. 结论：缺陷是 1-上闭链，积分论地基成立

**Theorem（缺陷是群值 1-上闭链）**：射影求值的**序缺陷**（两线索之差）是线性扩展图 `G(P)` 上的**群值 1-上闭链**：

- **可加性（可乘性）**：精确（telescoping，§2）；
- **局部化**：局部缺陷 = 共轭交换子（§3）；
- **BCH 展开**：局部缺陷 = `e^{hk[X,Y]+\text{高阶}}`，首项 = 曲率（§4）；
- **闭性**：hexagon 条件 = Jacobi 恒等式（Bianchi），自动成立（§5）。

故 `19` §3 的"离散 Stokes on `O(P)`"地基成立：**缺陷可沿任意相邻交换路径积分（求和），且路径无关**——这就是 §5 合成图里"Stokes 积分"这一步在宏观 DAG 层的严格形式。

**地位**：§2/§6（telescoping）平凡精确；§3（共轭交换子）`REFORMULATION` + 显式核对；§4（BCH）`CLASSICAL`；§5（Jacobi 闭性）`CLASSICAL`；§7（1-上闭链总括）`proved`（由 §2–§5 拼合）。

---

## 8. 残余（移交）

1. **平方 / hexagon 之外的 2-胞腔**：线性扩展图的高维胞腔（多于三元素的交换关系）是否全部闭合——需说明 `G(P)` 的 2-胞腔恰为平方与 hexagon（标准 Coxeter / permutahedron 事实），其余胞腔由它们生成。`CLASSICAL` 但需写清。
2. **高阶括号的几何意义**：§4 的 `[X,[X,Y]]`、`[Y,[X,Y]]` 对应"多反链边的嵌套缺陷"——即 `18` §8 残余 1，需与 `15` 的下集格 `O(P)` 的高维胞腔对表。
3. **宏观 Stokes 的收尾**：把本笔记的"1-上闭链"与 `19` §2 的"全息 Stokes"合成，得任意 `P` 的缺陷 = `∫∫ μλ`（各菱形面积之和）。

---

**参考**（沿用）：

1. `paper-1/sections/03-projective-affine.tex`（`eq:rho-chronological-antihomomorphism`）。
2. `paper-0/sections/09-contact-of-tearing.tex`（`thm:contact-curvature`、`eq:exact-open-contact-defect`）。
3. `notes/analysis-and-calculus/18-limit-smoothing-functor.md`、`19-integration-and-bulk-boundary.md`。
4. 标准 Lie 理论：Campbell–Baker–Hausdorff 公式、Jacobi 恒等式、Bianchi 恒等式。
