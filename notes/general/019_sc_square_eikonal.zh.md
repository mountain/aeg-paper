# 019 — 正方形 $\mathcal{Q}_e = [-e, e]^2$ 上的 Schwarz–Christoffel「天圆地方」共形双曲模型、`{∞,4}` 嵌入与光滑正交程函填充

**日期**：2026-11-15

**关联前序笔记与脚本**：[016-c2c4-tearing-belyi-f7.md](https://www.google.com/search?q=https%3A%2F%2Fgithub.com%2Fmountain%2Faeg-paper%2Fblob%2Fmain%2Fnotes%2Fgeneral%2F016-c2c4-tearing-belyi-f7.md)、[017-cayley-model-conformal-hyperbolic.md](https://github.com/mountain/aeg-paper/blob/main/notes/general/017-cayley-model-conformal-hyperbolic.md)、[018-cayley-assignment-duality-eikonal.md](https://github.com/mountain/aeg-paper/blob/main/notes/general/018-cayley-assignment-duality-eikonal.md) · 伴随脚本 `039-sc-square-eikonal.py`

## 一、问题起源：从凯莱分形方框 $D_\infty$ 到「天圆地方」正方形 $\mathcal{Q}_e = [-e, e]^2$

在 [017 号笔记](https://github.com/mountain/aeg-paper/blob/main/notes/general/017-cayley-model-conformal-hyperbolic.md)与 [018 号笔记](https://github.com/mountain/aeg-paper/blob/main/notes/general/018-cayley-assignment-duality-eikonal.md)中，$F_2$ 四叉树 $T_4$ 被欧氏递归嵌入为 $L^1$ 菱形并集 $D_\infty$，并赋予分片线性 Manhattan 深度度量 $g = (dx^2+dy^2)/L^2$（光滑片上 $K=-2$）。将 [035-gradient-cayley.py](https://github.com/mountain/aeg-paper/blob/main/notes/general/035-gradient-cayley.py) 旋转 $45^\circ$ 后，四条主树干沿对角线 $Y = \pm X$ 收敛于同一个轴对齐外包正方形的四顶点，而中心梯度流呈现同心圆与径向射线的正交结构。

直接用欧氏同心圆或 [038-eikonal-cayley.py](https://github.com/mountain/aeg-paper/blob/main/notes/general/038-eikonal-cayley.py) 的分片 $L^1$ 距离构造全局程函（Eikonal）填充会遇到两重障碍：

1. **分形峡湾与中轴激波脊**：欧氏自相似并集 $D_\infty$ 在横纵轴方向存在可数多个自相似凹陷峡湾，且 $L^1$ 深度在中轴脊线上梯度跳变；此外原 `030/038` 使用 $L_{\mathrm{bug}} = \min_i \big\vert{}\Vert{}p-c_i\Vert{}_1 - R_i\big\vert{}$ 会将内部母方格边框误判为零深度裂缝。

2. **圆对称波前与正方形理想边界的不相容**：纯欧氏圆 $\rho = \text{const}$ 无法与外包正方形 $\partial\mathcal{Q}_e$ 的 $D_4$ 边界条件对齐。

复分析中的 **Gauss 双纽线椭圆积分（Schwarz–Christoffel 圆盘-正方形共形映射）** 唯一地解决了这一几何张力：它在中心无穷小邻域保持四阶各向同性的圆波前，向外平滑过渡为超椭圆（squircle）并严丝合缝贴合 $\partial\mathcal{Q}_e = \partial[-e, e]^2$，在开正方形 $(-e, e)^2$ 上给出**实解析、常负曲率** $K=-1$**、零激波奇点**的双曲模型与正交程函填充。

## 二、Gauss 双纽线映射 $\mathcal{S}: \mathbb{D}_w \xrightarrow{\sim} \mathcal{Q}_e$ 与四类特征点锁相

设规范正方形为 $\mathcal{Q}_e := [-e, e]^2 \subset \mathbb{C}_Z$（$Z = X + iY$，$e = \exp(1)$）。定义从 Poincaré 单位圆盘 $\mathbb{D}_w = \{\vert{}w\vert{} < 1\}$ 到 $\mathcal{Q}_e$ 的双纽线 Schwarz–Christoffel 全纯双射：

$$
Z = \mathcal{S}(w) := \frac{e}{K_+} \int_0^w \frac{d\zeta}{\sqrt{1 + \zeta^4}}, \qquad K_+ := \int_0^1 \frac{dt}{\sqrt{1 + t^4}} = \frac{\Gamma(1/4)^2}{8\sqrt{\pi}} = \frac{\varpi}{2\sqrt{2}} \approx 0.927037338650686,
$$


其中 $\varpi = 2\int_0^1 (1-t^4)^{-1/2}dt \approx 2.62205755429212$ 为 Gauss 双纽线常数，对角积分满足 $\int_0^1 (1-t^4)^{-1/2}dt = \sqrt{2}\,K_+ \approx 1.31102877714606$。

将标准 Hecke 上半平面 $\mathbb{H}^2_\tau$（$\Gamma_4 = \langle J, T \rangle \cong C_2 * C_4$，$\varepsilon_4 = \frac{-1+i}{\sqrt{2}}$）经以 $\varepsilon_4$ 为中心的 Cayley 变换

$$
w(\tau) = \frac{\tau - \varepsilon_4}{\tau - \overline{\varepsilon}_4}
$$


复合上 $\mathcal{S}$，得到精确的**拓扑-几何锁相**（`PROVED`）：

* **中心四阶椭圆点**：$\tau = \varepsilon_4 \mapsto w = 0 \mapsto Z = (0, 0)$。由于 $\mathcal{S}(w) = \frac{e}{K_+}\big(w - \frac{w^5}{10} + \frac{3 w^9}{72} - \cdots\big)$ 缺失 $w^2, w^3, w^4$ 项，中心邻域具有 $O(\vert{}w\vert{}^5)$ 超高阶圆度。

* **四边中点 = 中心理想四边形** $\{4,\infty\}$ **的四个基本抛物尖点**：
  

  $$
  \tau \in \left\{\infty,\ 0,\ -\frac{1}{\sqrt{2}},\ -\sqrt{2}\right\} \longmapsto w \in \{+1,\ -i,\ -1,\ +i\} \longmapsto Z \in \{(+e,0),\ (0,-e),\ (-e,0),\ (0,+e)\}.
  $$

  
  特别地，实虚轴线段 $[-e, e]_X$ 与 $[-e, e]_Y$ 在度量 $g_{\mathrm{SC}}$ 下**严格为完备双曲测地线**。

* **正方形四角 = 四条主对角双曲 Pell 轴的理想端点**：
  第一代邻点 $J(\varepsilon_4) = \frac{1+i}{\sqrt{2}}$ 映为 $w = \frac{1-i}{2} = \frac{1}{\sqrt{2}}e^{-i\pi/4}$，故从原点出发的四条 $\{\infty,4\}$ 主枝天然沿 $\pm 45^\circ, \pm 135^\circ$ 射出；直行双曲 Pell 元素 $L = TJT$ 的不动点 $\tau = \pm 1$ 及 $U(\pm 1)$ 映为 $w = e^{\pm i\pi/4}, e^{\pm 3\pi i/4}$，经 $\mathcal{S}$ **精确落入正方形四角** $(\pm e, \pm e)$，且两条欧氏对角线 $Y = \pm X$ 自身即为严格双曲测地线。

## 三、共形深度 $f_{\mathrm{SC}}$ 与曲率引理的 Wirtinger 解析证明

将单位圆盘双曲度量 $g_{\mathbb{D}} = \frac{4\vert{}dw\vert{}^2}{(1-\vert{}w\vert{}^2)^2}$ 沿 $w = \mathcal{S}^{-1}(Z)$ 推前至 $(-e, e)^2$，因 $w'(Z) = \frac{K_+}{e}\sqrt{1+w^4}$，写成 [017 号笔记](https://github.com/mountain/aeg-paper/blob/main/notes/general/017-cayley-model-conformal-hyperbolic.md)的共形深度标准型：

$$
g_{\mathrm{SC}} = \frac{dX^2 + dY^2}{f_{\mathrm{SC}}(X, Y)^2}, \qquad f_{\mathrm{SC}}(X, Y) := \frac{e}{2 K_+} \frac{1 - \vert{}w(Z)\vert{}^2}{\big\vert{}1 + w(Z)^4\big\vert{}^{1/2}}.
$$

* **边界一阶渐近**：在四条开边 $\vert{}X\vert{} \to e^-$（$\vert{}Y\vert{} < e$）或 $\vert{}Y\vert{} \to e^-$（$\vert{}X\vert{} < e$）附近，$e - \vert{}X\vert{} \simeq \vert{}\mathcal{S}'(w)\vert{}(1-\vert{}w\vert{})$，故 $f_{\mathrm{SC}}(X,Y) \simeq \mathrm{dist}_{\mathrm{Eucl}}\big((X,Y), \partial\mathcal{Q}_e\big)$ 斜率恒为 $1$，与上半平面 $f = y$ 完全平行。

* **常曲率** $K = -1$ **的四行 Wirtinger 恒等证明**（`PROVED`）：记 $c = \frac{e}{2K_+}$，$A = 1 - \vert{}w\vert{}^2$，$g(w) = (1+w^4)^{-1/4}$ 及对数导数 $\eta = \frac{g'(w)}{g(w)} = -\frac{w^3}{1+w^4}$，则 $f_{\mathrm{SC}} = c A \vert{}g\vert{}^2$ 且 $4 c^2 \vert{}g\vert{}^4 \vert{}w'(Z)\vert{}^2 \equiv 1$。由 Wirtinger 算子 $\vert{}\nabla f\vert{}^2 = 4\vert{}w'\vert{}^2 \vert{}\partial_w f\vert{}^2$ 与 $\Delta f = 4\vert{}w'\vert{}^2 \partial_w\partial_{\bar w} f$：
  

  $$
  \vert{}\nabla f_{\mathrm{SC}}\vert{}^2 = \vert{}-\bar w + A\eta\vert{}^2 = \vert{}w\vert{}^2 - 2A\operatorname{Re}(w\eta) + A^2\vert{}\eta\vert{}^2,
  $$

  $$
  f_{\mathrm{SC}}\,\Delta f_{\mathrm{SC}} = A\big(-1 - 2\operatorname{Re}(w\eta) + A\vert{}\eta\vert{}^2\big).
  $$

  
  两式相减，所有含四次分歧因子 $\eta$ 的非线性项逐项抵消：
  

  $$
  K = f_{\mathrm{SC}}\,\Delta f_{\mathrm{SC}} - \vert{}\nabla f_{\mathrm{SC}}\vert{}^2 = -A - \vert{}w\vert{}^2 = -(1 - \vert{}w\vert{}^2) - \vert{}w\vert{}^2 \equiv -1.
  $$

  
  （注：若取重标度 $\tilde f_{\mathrm{SC}} = \sqrt{2}\,f_{\mathrm{SC}}$，则 $K \equiv -2$，直接对齐凯莱分形模型 $D_\infty$ 的归一化。）

由此可将 [017 号笔记](https://github.com/mountain/aeg-paper/blob/main/notes/general/017-cayley-model-conformal-hyperbolic.md)第四节的三模型对比表扩充为**四种** $\{\infty,4\}$ **典范实现**：

| 模型 | 定义域 | 共形深度 $f$ | $\Delta f$ | $\Vert{}\nabla f\Vert{}^2$ | $K = f\Delta f - \Vert{}\nabla f\Vert{}^2$ | 奇点与边界特征 | 
| ----- | ----- | ----- | ----- | ----- | ----- | ----- | 
| **Poincaré** $\mathbb{H}^2$ | $\{y > 0\}$ | $y$ | $0$ | $1$ | $-1$ | 无界实轴 $\mathbb{R}\cup\{\infty\}$，光滑 | 
| **Cayley** $D_\infty$ | 分形方格并集 | $L_{\mathrm{true}}$（$L^1$ 深度） | $0$（片内） | $2$（片内） | $-2$（片内） | 含轴向峡湾与可数树/咽喉脊奇点 | 
| **SC 方盘** $\mathcal{Q}_e$ | $[-e, e]^2$ | $\frac{e(1-\Vert{}w\Vert{}^2)}{2K_+\Vert{}1+w^4\Vert{}^{1/2}}$ | $\neq 0$（实解析） | 实解析 | $-1$（全域恒等） | 紧致正方形四边，**零内部激波、无峡湾** | 
| **Hecke** $W$-平面 | $\mathbb{C}_W^\times$（分支） | $\Vert{}W\Vert{} = e^s$ | $1/\Vert{}W\Vert{}$ | $1$ | $0$（平坦整流） | $\varepsilon_4$ 处 $4\pi$ 锥角鞍点，拉直零集 | 

## 四、`[-e, e]²` 上的两族光滑正交程函填充

在度量 $g_{\mathrm{SC}}$ 下，正则 AES 的内蕴程函方程（[018 号笔记](https://github.com/mountain/aeg-paper/blob/main/notes/general/018-cayley-assignment-duality-eikonal.md)第六节）写作：

$$
\vert{}\nabla_{g_{\mathrm{SC}}} a\vert{}_{g_{\mathrm{SC}}}^2 = f_{\mathrm{SC}}(X, Y)^2 \left[\left(\frac{\partial a}{\partial X}\right)^2 + \left(\frac{\partial a}{\partial Y}\right)^2\right] = \mu^2 + \lambda^2 a^2.
$$

脚本 `039-sc-square-eikonal.py` 构造并在机器精度（残差 $\le 3\times 10^{-15}$）下验证了两族零激波正交程函填充：

1. **「天圆地方」径向波前填充（原点源** $\varepsilon_4 \to \partial\mathcal{Q}_e$**）**：
   取从中心 $\varepsilon_4$ 出发的双曲距离 $s_{\mathrm{rad}}(Z) = 2\operatorname{artanh}\vert{}w(Z)\vert{} = \ln\frac{1+\vert{}w(Z)\vert{}}{1-\vert{}w(Z)\vert{}}$，令
   

   $$
   a_{\mathrm{rad}}(X, Y) = \frac{\mu}{\lambda}\sinh\big(\lambda s_{\mathrm{rad}}(X, Y)\big).
   $$

   
   在 $\mathcal{Q}_e \setminus \{(0,0)\}$ 上严格满足程函方程：内圈等值线为围绕星号原点的欧氏同心圆，向外平滑过渡为超椭圆波前并渐近贴合正方形四边 $\partial[-e,e]^2$；正交梯度流线为 $\arg w(Z) = \text{const}$（其中八条对称射线 $X=0, Y=0, Y=\pm X$ 为严格直线段）。

2. **全局无奇点尖点轴向填充（**$E_0$ **共形推前）**：
   以连接左右基本尖点 $(-e, 0)$ 与 $(+e, 0)$ 的水平测地线 $Y=0$ 为零集，取到该测地线的有向双曲距离：
   

   $$
   s_\perp(Z) = \operatorname{arsinh}\left(\frac{2\operatorname{Im} w(Z)}{1 - \vert{}w(Z)\vert{}^2}\right), \qquad a_\perp(X, Y) = \frac{\mu}{\lambda}\sinh\big(\lambda s_\perp(Z)\big).
   $$

   
   由于 $\vert{}\nabla_w s_\perp\vert{} = \frac{2}{1-\vert{}w\vert{}^2}$，该解在**包含原点** $(0,0)$ **在内的整个开正方形** $(-e, e)^2$ **上处处实解析且零奇点**，与连接上下边界 $Y = \mp e$ 的等距正交轨线构成全局光滑正交网格。

## 五、附：欧氏分形模型 `030/038` 的上包络穿透深度 $L_{\mathrm{true}}$ 对照

若在 $[-e, e]^2$（旋正缩尺 $e/16$）内保留欧氏 $L^\infty$ 方框并集 $D_N = \bigcup_i Q_i$，定义到外部补集的**上包络穿透深度**（非精确距离，见下）：

$$
L_{\mathrm{true}}(X, Y) = \frac{16}{e} \max_i \Big(h_i - \max\big(\vert{}X - c_{X,i}\vert{},\ \vert{}Y - c_{Y,i}\vert{}\big)\Big)_+.
$$


这消除了 [038-eikonal-cayley.py](https://github.com/mountain/aeg-paper/blob/main/notes/general/038-eikonal-cayley.py) 中 $\min_i \vert{}d_i - R_i\vert{}$ 造成的内部伪零线裂缝与外部无界溢出，清晰显示分片线性模型的奇点集恰好由 $T_4$ 对角树骨架与父子方格咽喉截线组成（`039` 面板 d）。

**但需注明：$L_{\mathrm{true}}$ 是 L∞ 穿透深度，一般不等于到补集的精确距离。** 具体地：

- **星形 / 穿透假设（等式条件）**：$L_{\mathrm{true}}$ 精确等于到 $\partial D_N$ 的 $L^1$ 距离，当且仅当「最深的方框恰是最外层的方框」——即每条从根出发的 $L^\infty$ 射线只穿出并集一次（$L^\infty$ 正交凸 / 方向星形）。凯莱树并集在**主轴与主对角方向**满足该条件（数值对拍一致）。
- **一般情形为下界**：在峡湾与父子咽喉附近，并集延伸到更深方框之外，穿透深度 < 最近出口距离，故 $L_{\mathrm{true}}$ 只是**下界**。随机数值对拍（`039` 补充检验）给出偏差可达 $\sim0.85$（凯莱并集）与 $\sim1.5$（任意并集）。
- **修正与真值**：$L_{\mathrm{true}}$ 的**实际价值**是消除内部伪零线（与 `038` 的 $\min_i\vert d_i-R_i\vert$ 不同，它在内部缝合线取父方框的正穿透，只在外部补集归零）。若需精确到补集距离，应以**棋盘距离变换（CDT）** 或对 $L_{\mathrm{true}}$ 的补集距离变换为对拍真值；`L_true` 仅作快速下界与可视化。


## 六、状态汇总

| 命题 / 构造 | 状态 | 验证方式 | 
| ----- | ----- | ----- | 
| $\mathcal{S}: \mathbb{D}_w \xrightarrow{\sim} [-e, e]^2$ 将四尖点映至四边中点、四 Pell 轴映至四角 | **PROVED** | 解析恒等 + `039` 精度 $10^{-15}$ | 
| 共形深度 $f_{\mathrm{SC}}$ 满足 $K = f_{\mathrm{SC}}\Delta f_{\mathrm{SC}} - \Vert{}\nabla f_{\mathrm{SC}}\Vert{}^2 \equiv -1$ | **PROVED** | Wirtinger 四行恒等证明 + `039` 验证 | 
| 径向超椭圆填充 $a_{\mathrm{rad}}$ 与全局无奇点填充 $a_\perp$ 精确满足内蕴程函方程 | **PROVED** | 解析链式法则 + `039` 残差 $< 10^{-14}$ | 
| $L_{\mathrm{true}} = \max_i (R_i - d_i)_+$：修正 `038` 内部伪零线；**在星形/穿透假设下**等于到外部补集的 $L^1$ 距离，一般情形为下界 | **PROVED under star-shaped hypothesis** | 解析 + `039` 面板 (d) + 主轴对拍；任意并集偏差 $\sim1.5$，精确值须 CDT 对拍 | 
| 将 $\mathcal{Q}_e$ 上的圆-方极坐标流直接解释为连续算术加乘重整化坐标 | **STRUCTURAL PROPOSAL** | 几何精确，算术语义待与 Paper II/IV 耦合 | 
