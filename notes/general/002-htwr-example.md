# HTWR 核上的精确时空帕累托边界：部分分式重构、催化虫洞与不确定性原理

> **文档性质**：算术表达式几何（AEG）研究笔记（之二：展示定理与严格上下界推导）
> **前置依赖**：笔记一《双曲热带波前-残差核（HTWR Core）》公理 I–IV
> **日期**：2026-11-13
> **备注**：本笔记中的反例审计、上下界严格证明与催化虫洞构造，形成于与 **Google Gemini（Carbon 版本）** 的协作核查与推演。

---

## 一、 模型定标与测试靶点

选取 $\sqrt{2}$ 的 Pell 有理收敛子序列 $\{x_n\}_{n \ge 1}$ 作为标准试验场。定义整数对 $(P_n, Q_n)$ 满足 $(1 + \sqrt{2})^n = P_n + Q_n\sqrt{2}$，记 $x_n := \frac{P_n}{Q_n} \in \mathbb{P}^1(\mathbb{Q})$（其平移态 $u_n := x_n + 1 = \frac{Q_{n+1}}{Q_n}$ 满足纯连分数不动点递推 $u_{n+1} = 2 + \frac{1}{u_n}$）。

1. **双曲管径标定**：记银比 $\lambda := 1 + \sqrt{2}$，单步双曲深度增量 $h_0 := \ln \lambda \approx 0.8814$。因 $\gcd(P_n, Q_n) = 1$ 且 $P_n = \frac{1}{2}[\lambda^n + (1-\sqrt{2})^n] > Q_n > 0$，第 $n$ 阶状态的信息高度（双曲径向深度）精确满足：

$$I(x_n) = \ln P_n = n h_0 - \ln 2 + o(1)$$



对目标态 $x_N$（$N \gg 1$），记终点固有深度为 $I_* := I(x_N) = N h_0 - \ln 2 + o(1)$。
2. **局部作用量定标**：取公理 II 中归一化门斜率 $\alpha_g = \alpha > 0$，底噪量子 $\epsilon_0 > 0$（满足 $\epsilon_0 \ll \alpha h_0$）：
* 一元 Möbius 测地门 $\gamma \in \mathrm{PSL}(2, \mathbb{Z})$（由 $z \mapsto z \pm 1,\ z \mapsto -1/z$ 生成）及扇出奇点 $\Delta$：$c(z) = \epsilon_0 + \alpha I(z)$；
* 二元散射门 $\star \in \{+, -, \times, \div\}$：$c(z_1, z_2) = \epsilon_0 + \alpha\big(I(z_1) + I(z_2)\big)$。



该序列同时容许两条正交的生成几何：

* **零亏格双曲测地流（$g=0$）**：经平移 $u_n = x_n + 1$ 沿 $T(u) = 2 + 1/u$ 串行推进 $N-1$ 步，全程仅维持单根导线（$m=1$），总作用量为二次阶：

$$\mathcal{A}_{\text{CF}}(x_N) = \sum_{n=1}^{N-1} 3\alpha I(u_n) + O(N\epsilon_0) = \frac{3\alpha}{2 h_0} I_*^2 + O(\alpha I_*)$$


* **高亏格牛顿切线折叠（$g \ge 1$）**：精确满足单导线二倍跳变恒等式 $x_{2n} = \frac{x_n^2 + 2}{2 x_n}$，仅需 $\Theta(\log N)$ 层环柄即可跨越至终点。

---

## 二、 分配律破缺与“$\frac{3}{2}I_*$ 假性壁垒”的消解

在考察牛顿倍增步 $x_n \mapsto x_{2n}$（设输入深度 $L := I(x_n) \approx \frac{1}{2} I_*$）时，后缀上下文空间 $\mathcal{K}_1$ 中的**分配律/部分分式对称性破缺**直接决定了空间峰值与虫洞损耗：

1. **未拆解有理分式上下文 $k_{\text{naive}}(\square) = \frac{\square^2 + 2}{2\square}$**：
* 需两次 $\Delta$ 扇出产生三导线截面 $(\square, \square, \square)$，左两路相乘坠入深度 $2L$ 的平方深渊 $\frac{P_n^2}{Q_n^2}$，同时右路挂起深度为 $L$ 的分母 $2x_n$。
* 在除法门合拢前，双管截面 $(P_n^2 + 2Q_n^2)/Q_n^2$ 与 $2P_n/Q_n$ 的瞬时总通量膨胀至 **$3L \approx \frac{3}{2} I_*$**，随后经除法门约去公因子 $Q_n$（约分虫洞）坍缩回输出深度 $2L = I_*$，单轮消耗作用量 $13\alpha L$，累计作用量 $13\alpha I_*$。


2. **部分分式（Heron）重构上下文 $k_{\text{Heron}}(\square) = \frac{1}{2}\left(\square + \frac{2}{\square}\right)$**：
* 语义上 $k_{\text{Heron}} = k_{\text{naive}}$，但由于将射影极点 $\{0, \infty\} \subset \mathbb{P}^1(\mathbb{Q})$ 在有理数域上拆分为两个一度分支，仅需**一次** $\Delta$ 扇出。
* 在最后一轮倍增（$n = N/2 \to N$）中，截面 $[2]$ 上并置的两根导线为 $x_{N/2} = \frac{P_{N/2}}{Q_{N/2}}$ 与 $\frac{2}{x_{N/2}} = \frac{2 Q_{N/2}}{P_{N/2}}$（因 $P_m$ 恒为奇数，二者既约）。其瞬时总通量为：

$$\Sigma_{\text{Heron}} = \ln P_{N/2} + \ln(2 Q_{N/2}) = \left(\frac{N}{2}h_0 - \ln 2\right) + \left(\frac{N}{2}h_0 - \frac{1}{2}\ln 2\right) + o(1) = I_* - \frac{1}{2}\ln 2 < I_*$$


* 两分支经加法门直接通分合成 $\frac{P_{N/2}^2 + 2Q_{N/2}^2}{P_{N/2} Q_{N/2}}$（**零公因子约分浪费**），单轮消耗作用量降至 $7\alpha L$，累计总作用量压缩至 **$7\alpha I_* + O(\epsilon_0 \log N)$**。



> **实例校验（$N=8$）**：$x_4 = \frac{17}{12}$，$x_8 = \frac{577}{408}$，终点深度 $I(x_8) = \ln 577 \approx 6.3578$。在 $x_4 \mapsto x_8$ 的 Heron 环柄内部，最宽截面为 $(\frac{17}{12}, \frac{24}{17})$，瞬时总通量 $\ln 17 + \ln 24 = \ln 408 \approx 6.0113 < \ln 577$。

**几何结论**：代数上等价的两个非线性上下文在 HTWR 核中具有严格不等的世界面度量（$\Sigma_{\text{naive}} = \frac{3}{2}I_* > \Sigma_{\text{Heron}} = I_*$）。在无附加通道约束下，总通量上限 $\Sigma_{\max} = I_*$ 已足以容纳 Heron 倍增链，不产生二次时间退化。

---

## 三、 切割界面的正交分解：纵向波前深度 vs 横向催化通量

上述分析揭示了总通量 $\Sigma(\mathbf{u})$ 的掩蔽效应：由于主载体导线在终点必须达到深度 $I_*$，在早期浅层（$L \ll I_*$）开启的环柄全部躲在终点肥管投下的“空间阴影”内。要分离“问题固有的纵向目标深度”与“非线性分岔占用的横向工作空间”，必须对任意切割截面 $\mathbf{u} = (u_1, \dots, u_m) \in X^m$ 的空间通量做正交分解：

$$\Sigma(\mathbf{u}) = \underbrace{\Phi(\mathbf{u})}_{\text{纵向主波前深度}} + \underbrace{\Sigma_{\text{aux}}(\mathbf{u})}_{\text{横向催化/纠缠通量}}$$

其中：

* **纵向主波前深度** $\Phi(\mathbf{u}) := \max_{1 \le j \le m} I(u_j)$：度量当前截面中最深导线向双曲边界尖点推进的距离（从 $0$ 演化至 $I_*$ 的状态坐标）；
* **横向催化通量（Transverse Catalytic Flux）** $\Sigma_{\text{aux}}(\mathbf{u}) := \Sigma(\mathbf{u}) - \Phi(\mathbf{u}) = \sum_{j \neq j_{\max}} I(u_j)$：度量除主载体导线外，由扇出奇点 $\Delta$ 派生并同时挂起在截面上的**辅助纠缠管径总和**。
* 纯树单线测地流（$m=1,\ g=0$）恒有 $\Sigma_{\text{aux}} \equiv 0$；
* Heron 全倍增链在末轮合拢前需要 $\Sigma_{\text{aux}} = I(x_{N/2}) = \frac{1}{2} I_* + O(1)$。



以横向催化配额 $\Sigma_{\text{aux}} \le \sigma_{\max}$ 作为空间约束变量，HTWR 核上的普适时空权衡律随即完整显现。

---

## 四、 普适时空不确定性下界定理（对任意目标与任意 DAG 成立）

### 定理 1（HTWR 时空作用量-催化通量不确定性原理）

设目标态 $y^* \in \mathbb{P}^1(\mathbb{Q})$ 的信息高度为 $I_* = I(y^*) > \ln 2$。对于 HTWR 核中**任意**制备 $y^*$ 的非线性弦图网络 $h \in \mathrm{Hom}([0], [1])$，若其存在叶状切片序列（拓扑求值序）使得每一空间截面 $\mathcal{C}_t$ 的横向催化通量满足 $\Sigma_{\text{aux}}(\mathcal{C}_t) \le \sigma_{\max}$（$\sigma_{\max} \ge 0$），则 $h$ 的总作用量满足无条件刚性下界：

$$\mathcal{A}(h) \ge \frac{\alpha (I_* - \ln 2)^2}{2(\sigma_{\max} + \ln 2)}$$

#### 严格证明

将弦图 $h$ 按拓扑序分解为 $M$ 个单生成元切片 $g_1, g_2, \dots, g_M$，由于共享子图已显式表示为 $\Delta$ 生成元，每个门在序列中恰好出现一次，$\mathcal{A}(h) = \sum_{t=1}^M c_{g_t}$。记截面 $\mathcal{C}_t$ 上的纵向主深度为 $\Phi_t := \Phi(\mathcal{C}_t)$，初态 $\Phi_0 = 0$，终态 $\Phi_M = I_*$。考察单步增量 $\Delta \Phi_t := \Phi_t - \Phi_{t-1} > 0$ 的一切可能生成元 $g_t$：

1. **常数注入、擦除 $\epsilon$ 与扇出 $\Delta$**：均不产生超越原截面最大高度的新状态（对 $\Delta(u) \mapsto (u,u)$，最大值不变，仅将副本计入 $\Sigma_{\text{aux}}$），故 $\Delta \Phi_t \le 0$。
2. **一元 Möbius 生成元 $\gamma \in \{z \mapsto -1/z,\ z \mapsto z \pm 1\}$**：求逆严格保持高度 $I(-1/z) = I(z)$；加减 $1$ 满足 $\max(\vert{}p \pm q\vert{}, \vert{}q\vert{}) \le 2\max(\vert{}p\vert{}, \vert{}q\vert{})$，故 $I(z \pm 1) \le I(z) + \ln 2$。若 $\Delta \Phi_t > 0$，则必有 $\Phi_t = I(z \pm 1) \le I(z) + \ln 2$，从而：

$$\Delta \Phi_t \le \ln 2 \le \sigma_{\max} + \ln 2, \qquad c_{g_t}(z) \ge \alpha I(z) \ge \alpha(\Phi_t - \ln 2)$$


3. **二元散射生成元 $\star \in \{+, -, \times, \div\}$**：设输入导线为 $u_1, u_2 \in \mathcal{C}_{t-1}$ 且 $I(u_1) \ge I(u_2)$。由于 $u_1, u_2$ 在截面 $\mathcal{C}_{t-1}$ 中占据两个独立槽位，无论全局最大导线是否落在 $u_1$ 上，较细导线 $u_2$ 必然计入横向催化通量，即：

$$I(u_2) \le \Sigma_{\text{aux}}(\mathcal{C}_{t-1}) \le \sigma_{\max}$$



由对数 Weil 高度的三角不等式（乘除满足 $I(u_1 \star u_2) \le I(u_1) + I(u_2)$，加减满足 $I(u_1 \pm u_2) \le I(u_1) + I(u_2) + \ln 2$），输出态 $u_{\text{out}} = u_1 \star u_2$ 满足 $I(u_{\text{out}}) \le I(u_1) + I(u_2) + \ln 2$。若 $\Delta \Phi_t > 0$，则 $\Phi_t = I(u_{\text{out}})$ 且 $\Phi_{t-1} \ge I(u_1)$，立得两条核心不等式：

$$\Delta \Phi_t \le I(u_{\text{out}}) - I(u_1) \le I(u_2) + \ln 2 \le \sigma_{\max} + \ln 2$$


$$c_{g_t}(u_1, u_2) \ge \alpha\big(I(u_1) + I(u_2)\big) \ge \alpha\big(I(u_{\text{out}}) - \ln 2\big) = \alpha(\Phi_t - \ln 2)$$



抽取序列 $\{\Phi_t\}_{t=0}^M$ 中刷新历史最高纪录的严格递增子序列 $0 = \hat{\Phi}_0 < \hat{\Phi}_1 < \dots < \hat{\Phi}_R = I_*$，记步长 $\delta_r := \hat{\Phi}_r - \hat{\Phi}_{r-1} \in (0,\ \sigma_{\max} + \ln 2]$。利用 $\frac{\delta_r}{\sigma_{\max} + \ln 2} \le 1$ 及右端点黎曼和单调性，对所有满足 $\hat{\Phi}_r > \ln 2$ 的纪录步求和：

$$\mathcal{A}(h) \ge \sum_{\hat{\Phi}_r > \ln 2} \alpha(\hat{\Phi}_r - \ln 2) \ge \frac{\alpha}{\sigma_{\max} + \ln 2} \sum_{\hat{\Phi}_r > \ln 2} (\hat{\Phi}_r - \ln 2)\,\delta_r \ge \frac{\alpha}{\sigma_{\max} + \ln 2} \int_{\ln 2}^{I_*} (x - \ln 2)\,dx = \frac{\alpha(I_* - \ln 2)^2}{2(\sigma_{\max} + \ln 2)}$$

证毕。 $\square$

---

## 五、 催化虫洞大步跨越与紧致帕累托边界定理

定理 1 给出了双曲反比下界 $\Omega(I_*^2 / \sigma_{\max})$。下面针对 Pell 收敛子 $x_N$（对**任意整数 $N \ge 1$**，无需假设 $N = 2^K$），构造一个精妙的“线性主管道 + 常驻催化剂虫洞”网络，证明该下界在整个区间 $\sigma_{\max} \in [0, \frac{1}{2}I_*]$ 上是**紧致的（Tight up to a constant）**！

### 核心构造：主导线零扇出的催化步进恒等式

若在深度 $L \gg \sigma_{\max}$ 处直接对主导线 $x_n$ 做 $\Delta$ 扇出，横向通量将瞬间飙升至 $L > \sigma_{\max}$ 而违规。为绕开此禁令，利用 $(1+\sqrt{2})^{n+k} = (P_n + Q_n\sqrt{2})(P_k + Q_k\sqrt{2})$ 及 Pell 恒等式 $P_k^2 - 2Q_k^2 = (-1)^k$，将跨度为 $k$ 的跳变映射改写为关于主变量 $x_n$ 的**一度分式线性（Möbius）分解式**：

$$x_{n+k} = \frac{x_n x_k + 2}{x_n + x_k} = x_k + \frac{2 - x_k^2}{x_n + x_k} = x_k + \frac{(-1)^{k+1} / Q_k^2}{x_n + x_k}$$

**几何奇迹**：在该表达式中，重负荷主变量 $x_n$ **仅出现一次（严格线性穿行，零 $\Delta$ 扇出！）**！给定催化步长参数 $k \ge 1$（对应催化基元深度 $s := I(x_k) \approx k h_0$），只需在横向常驻一对轻量级催化剂导线 $(x_k,\ c_k)$，其中 $c_k := 2 - x_k^2 = \frac{(-1)^{k+1}}{Q_k^2}$（深度 $I(c_k) = 2\ln Q_k \approx 2s$）：

1. **余数前置消除整除锯齿**：对任意 $N$，作带余除法 $N = M k + r$（$0 \le r < k$）。在起点先用 Heron 倍增链制备初始主态 $z^{(0)} = x_r$（若 $r=0$ 则从 $x_k$ 起步减一轮）以及催化剂对 $(x_k, c_k)$。因 $r < k$，制备过程峰值通量不超过 $3s$，消耗作用量仅为 $O(\alpha s)$。
2. **即时扇出（Just-in-Time）四门虫洞跨越**：在第 $j$ 轮大步跨越（$z = x_{r+jk} \mapsto x_{r+(j+1)k}$，主深度 $L_j \approx (r+jk)h_0$）中，按序执行：
* 从催化剂 $x_k$ 扇出一份副本并与 $z$ 相加：$z_1 = z + x_k = \frac{Q_{r+(j+1)k}}{Q_{r+jk} Q_k}$（主深度升至 $L_j + s$，瞬时横向通量 $4s$）；
* 主导线求逆：$z_2 = 1 / z_1$（主深度 $L_j + s$，横向通量 $3s$）；
* 从催化剂 $c_k$ 扇出一份副本并与 $z_2$ 相乘：$z_3 = z_2 \cdot c_k = \frac{(-1)^{k+1} Q_{r+jk}}{Q_k Q_{r+(j+1)k}}$（自动约去一重 $Q_k$，主深度 $L_j + 2s$，**全局峰值横向通量为 $s + 2s + 2s = 5s$**）；
* 从催化剂 $x_k$ 扇出一份副本并与 $z_3$ 相加：$z_{\text{next}} = z_3 + x_k = \frac{Q_k P_{r+(j+1)k}}{Q_k Q_{r+(j+1)k}} = x_{r+(j+1)k}$（触发约分虫洞消去剩余因子 $Q_k$，主深度精准回落至 $L_{j+1} = L_j + s$！）。



> **算术实例验证（$n=3 \to 5,\ k=2$）**：主态 $x_3 = \frac{7}{5}$，催化剂 $x_2 = \frac{3}{2},\ c_2 = 2 - \frac{9}{4} = -\frac{1}{4}$。四步演化依次为：$z_1 = \frac{7}{5} + \frac{3}{2} = \frac{29}{10} \longrightarrow z_2 = \frac{10}{29} \longrightarrow z_3 = \frac{10}{29}\times\left(-\frac{1}{4}\right) = -\frac{5}{58} \longrightarrow z_4 = -\frac{5}{58} + \frac{3}{2} = \frac{82}{58} = \frac{41}{29} = x_5$，两轮 $Q_2 = 2$ 的虫洞约分严丝合缝。

单轮跨越总计消耗作用量 $\Delta \mathcal{A}_j = \alpha(4 L_j + 12s) + O(\epsilon_0)$，全程横向通量严格受控于 $5s$。令 $s = \frac{1}{5}\sigma_{\max}$（即取步长 $k = \lfloor \frac{\sigma_{\max}}{5 h_0} \rfloor$），对 $M \approx \frac{I_*}{s} = \frac{5 I_*}{\sigma_{\max}}$ 轮求和：

$$\mathcal{A}_{\text{BSGS}}(\sigma_{\max}) = \sum_{j=0}^{M-1} 4\alpha (j s) + O(\alpha M s) = 2\alpha s M^2 + O(\alpha I_*) = \frac{10\alpha I_*^2}{\sigma_{\max}} + O(\alpha I_*)$$

结合定理 1 的普适下界与 $\sigma_{\max} \ge \frac{1}{2}I_*$ 处的 Heron 全倍增饱和态，即得完整的帕累托边界定理：

---

### 定理 2（二次收敛子的双曲时空帕累托边界定理）

在 HTWR 核公理 I–IV 下，制备第 $N$ 阶 Pell 收敛子 $x_N$（固有深度 $I_* = N \ln(1+\sqrt{2}) - \ln 2 + o(1)$）在横向催化通量配额 $\Sigma_{\text{aux}} \le \sigma_{\max}$ 下的最小可达作用量 $\mathcal{A}^*(\sigma_{\max})$ 呈现双相结构，且在全定义域上精确锁定数量级：

1. **催化虫洞反比权衡相（$0 \le \sigma_{\max} < \frac{1}{2} I_*$）**：

$$\frac{\alpha (I_* - \ln 2)^2}{2(\sigma_{\max} + \ln 2)} \;\le\; \mathcal{A}^*(\sigma_{\max}) \;\le\; \begin{cases} \dfrac{3\alpha}{2 h_0} I_*^2 + O(\alpha I_*), & 0 \le \sigma_{\max} < 5 h_0 \\ \dfrac{10\alpha I_*^2}{\sigma_{\max}} + O(\alpha I_*), & 5 h_0 \le \sigma_{\max} < \dfrac{1}{2} I_* \end{cases}$$



在此区间内，系统遵守严格的**双曲时空守恒律** $\mathcal{A}^*(\sigma_{\max}) \cdot (\sigma_{\max} + \ln 2) = \Theta(\alpha I_*^2)$；边际空间影子价格（接触热力学广义压强）满足幂律发散 $-\frac{\partial \mathcal{A}^*}{\partial \sigma_{\max}} \asymp \frac{\alpha I_*^2}{\sigma_{\max}^2}$。
2. **全凝聚线性饱和相（$\sigma_{\max} \ge \frac{1}{2} I_*$）**：
当横向催化配额跨过临界点 $\sigma_c = \frac{1}{2} I_* - \frac{1}{2}\ln 2$ 时，Heron 部分分式环柄链解锁，二次障碍彻底消失，作用量坍缩并锁定于线性基态：

$$\alpha (I_* - \ln 2) \;\le\; \mathcal{A}^*(\sigma_{\max}) \;\le\; 7\alpha I_* + O(\epsilon_0 \log I_*)$$



---

## 六、 三种核心几何机制总结对照

| 演化机制 / 空间配额区 | 代表电路与拓扑亏格 | 横向催化通量 $\Sigma_{\text{aux}}$ | 峰值总通量 $\Sigma_{\text{total}}$ | 纵向总作用量 $\mathcal{A}$ | 双曲几何物理图景 |
| --- | --- | --- | --- | --- | --- |
| **纯测地流基态**<br>

<br>($\sigma_{\max} = 0$) | 连分数迭代 $2 + 1/u$<br>

<br>($g = 0$，零扇出单管) | $0$ | $I_*$ | $\dfrac{3\alpha}{2 h_0} I_*^2 \asymp \Theta(N^2)$ | 紧贴双曲测地线匀速挪动 $N$ 步的零曲率喇叭管 |
| **催化虫洞跨越态**<br>

<br>($5h_0 \le \sigma_{\max} < \frac{1}{2}I_*$) | 常驻 $(x_k, c_k)$ 四门步进<br>

<br>($g = \Theta(I_*/\sigma_{\max})$) | $\le \sigma_{\max}$ | $I_* + O(\sigma_{\max})$ | $\Theta\!\left(\dfrac{\alpha I_*^2}{\sigma_{\max}}\right)$ | 主导线零扇出穿行，借横向催化小环柄与 $Q_k$ 约分虫洞做等距大步跳跃 |
| **Heron 全凝聚基态**<br>

<br>($\sigma_{\max} \ge \frac{1}{2}I_*$) | 部分分式倍增 $\frac{1}{2}(x + \frac{2}{x})$<br>

<br>($g = \lceil \log_2 N \rceil$) | $\dfrac{1}{2} I_*$ | $I_*$ | $7\alpha I_* \asymp \Theta(N)$ | 极点有理劈裂消除冗余膨胀，$\log_2 N$ 次无损倍增直达尖点 |
| **未拆解牛顿次优态**<br>

<br>*(反例参照)* | 原始分式 $\frac{x^2+2}{2x}$<br>

<br>($g = 2\lceil \log_2 N \rceil$) | $I_*$ | $\dfrac{3}{2} I_*$ | $13\alpha I_* \asymp \Theta(N)$ | 因未拆解部分分式导致分子过度潜入深渊，再经 $Q_n$ 约分虫洞回吐虚胖通量 |