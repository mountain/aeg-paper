# 07 – 关系记忆误差、门控边界与 Scott 连续概率运输

**Status:** research note，2026-11-11。
本篇继续 [note 06](06-typed-probability-transport-and-relation-memory.md)：
把“能否遗忘”推进为误差界，把有限矩阵连续性推进为一个明确的
Scott 连续紧不确定集构造，并核查模型中真正参与选概率的状态。
一般命题附证明；模型结果分为固定源码检查和冻结数据认证。
未重跑训练，未建立完整表达式空间的概率语义。

有限输入、例子的边界和验证运算均用有理数。与
[note 03](03-quadrilateral-neighborhoods-and-scott-continuity.md)
相同，实数只承担通常的极限完成语义；没有引入无穷小。
softmax 的指数通过有理上下界认证，而不是假定它具有有理值。

## 1. 核对模型以后，需要区分的三种接口

### 1.1 Sector-Prob 已有一个聚合接口，但不是下降定理

固定 mountain/einsteins-blackboard 提交
32558fe87ac3bb85d93beca9b2be6d56cf74ca09。
其分析脚本 [analyze_quality_structure.py](https://github.com/mountain/einsteins-blackboard/blob/32558fe87ac3bb85d93beca9b2be6d56cf74ca09/scritps/analyze_quality_structure.py)
的 load_sector_prob 读取源扇区×深度类型×目标基底的概率张量。
analyze_second_order 并非直接把 12×8 矩阵自乘，而是：

1. 对深度类型取平均，为每个源扇区指定一个占优基底 q(s)；
2. 按 q(s) 把扇区分组；
3. 在每组内均匀平均“向上”或“向下”的目标基底分布，得到 8×8 表。

因此上一轮提出的接口问题已有一个候选答案，需要检验其含义。
设 $E_b=\{s:q(s)=b\}$，在非空组上定义

$$
R_{bs}=\frac{\mathbf1_{s\in E_b}}{|E_b|},\qquad
\bar\pi^\uparrow_{sj}
=\tfrac12(\pi_{s,0,j}+\pi_{s,1,j}).
$$

脚本计算的表就是 $T^\uparrow=R\bar\pi^\uparrow$。
没有扇区落入的基底对应零行，不能把该行当作概率分布。
此表可描述“先按组均匀重新选一个源扇区，再作一步分支选择”。
但真实历史给出的条件源分布未必均匀；目标基底也不是完整目标坐标。
所以它本身不证明真实多步过程具有这个 Markov 核。
必须另行指定目标状态怎样进入下一步，并检验 note 06 的下降条件。

本次没有取得该历史脚本所用的完整训练权重并重跑它；
上述是对固定源码的解释，不是对历史 12×8 模型的性能复核。

### 1.2 dirac-belt 的两代模型：门控看源表示，运动输出赋值

固定 mountain/dirac-belt 提交
7eb633bde849e66feeb4b22c765780abee72936a。
在 [SectionExact](https://github.com/mountain/dirac-belt/blob/7eb633bde849e66feeb4b22c765780abee72936a/code/section_exact.py)
与 [PoleSectionExact](https://github.com/mountain/dirac-belt/blob/7eb633bde849e66feeb4b22c765780abee72936a/code/pole_section_exact.py)
中，概念表示都有

$$
x_i=\rho_i\,d_i,\qquad a_i=x_i e^{\alpha_i}.
$$

| 项目 | SectionExact | PoleSectionExact |
|---|---|---|
| 分支运动 | $(a+\mu_j)e^{\alpha_j}$ | $q_j+m_j(a-q_j)$ |
| 概率选择 | 源方向的扇区＋源半径的深度格 | 同左 |
| 运动输出 | 预测赋值 a′ | 预测赋值 a′ |
| 当前概率入口 | 已登记源概念的索引 | 已登记源概念的索引 |

两份源码的 _bin_index 都对方向角和半径作整数分格。
深度分格还使用全体概念的最大半径，故模型快照或该归一化参数也是合同的一部分。
channel_distribution 读取该格的 logits，再在通道上作 softmax。

这些接口没有仅凭任意预测 a′ 唯一指定下一步源概念、表示深度 α′ 或概率格。
若要迭代这种“先选概率、再作分支运动”的模型，须选择一种提升：
保留完整表示、回到已登记概念、给出新的上下文状态，或明确规定 α′。
这些选择可能产生不同的关系过程。

一个有理见证是

$$
(x,t)=(1,2),\ (2,1),\qquad a=xt=2,
$$

其中 t 代替正尺度 $e^\alpha$。
若两个半径格分别取通道概率 (3/4,1/4)、(1/4,3/4)，
并取值域分支 $F_0(a)=a,\ F_1(a)=a+1$，
同一个赋值 a 就对应两种不同的下一步概率律，TV 距离为 1/2。
这是允许参数的反例，不声称训练快照中已经出现这两个恰好等值的概念。

### 1.3 能量读出、通道分布与目标概念分布

上述 affine_mixture_dist 计算

$$
-\log\sum_j\pi_j(i)
\exp\left(-\frac{\|F_j(a_i)-a_t\|^2}{2\sigma^2}\right).
$$

它是给候选尾概念 t 的混合能量；在通道 j 上归一化，
并不等于已经对所有尾概念 t 归一化的转移概率。
若增加目标词表上的归一化，还应记录候选集合、温度和归一化规则。
以下理论会明确指定所运输的概率律，不把这些读出混为一谈。

## 2. 连续分支为什么还不够

### 2.1 硬门控的有理反例

**Status: proved / computationally verified example.**
考虑两个固定输出 0、1，记 $\nu_p=(1-p)\delta_0+p\delta_1$，并定义

$$
\kappa(z)=
\begin{cases}
\nu_{1/4},&z<0,\\
\nu_{3/4},&z\ge0.
\end{cases}
\tag{2.1}
$$

两条输出分支都是常值连续映射，门控仍造成 TV=1/2 的跳跃。
对有理边界的区间套 $I_n=[-1/n,1/n]$，有

$$
\bigcap_n I_n=\{0\},\qquad
\bigcap_n\kappa[I_n]=\{\nu_{1/4},\nu_{3/4}\}
\ne\kappa[\{0\}]=\{\nu_{3/4}\}.
\tag{2.2}
$$

在以反包含为序的紧不确定集上，(I_n) 是有向族，
(2.2) 表明精确图像运输不保持其上确界，因而不是 Scott 连续的。
这里只需要一个跨门控边界的有理区间套。

把两侧极限都补到边界可以得到另一种集合值语义；
那会改变边界点的对象，不能称为原来单值核已经连续。

### 2.2 连续混合的充分条件，以及该用哪种概率拓扑

**Status: proved with stated hypotheses.**
设 X、Y 为度量空间，有限个分支 $F_j:X\to Y$ 和概率权重
$\pi_j:X\to[0,1]$ 连续，且 $\sum_j\pi_j=1$。
定义

$$
\kappa(z)=\sum_j\pi_j(z)\delta_{F_j(z)}.
\tag{2.3}
$$

则 κ 对概率测度的弱拓扑连续。证明：对每个有界连续 f，

$$
\int f\,d\kappa(z)=\sum_j\pi_j(z)f(F_j(z))
$$

为连续函数。这是有限分支的弱 Feller 论证；相关标准框架见 [S2]。
此处不借用任何平稳测度存在或唯一性结论。

不能把弱连续性换成 TV 连续性：
$\delta_{1/n}$ 弱收敛到 $\delta_0$，但 TV 恒为 1。
有限通道标签的概率变化可用 TV；连续移动的输出位置需要另外的拓扑或距离。

若分支共同满足 Lipschitz 常数 L，且对所有 z，
$\operatorname{diam}\{F_j(z)\}\le D$，则

$$
W_1(\kappa(z),\kappa(z'))
\le L\,d(z,z')+
D\,\operatorname{TV}(\pi(z),\pi(z')).
\tag{2.4}
$$

**证明。** 先保持权重 π(z)，把每个原子从 F_j(z) 移到 F_j(z′)，
代价不超过 Ld。再在固定位置 F_j(z′) 上匹配两组权重的共同部分；
剩余质量为 TV，移动距离至多 D。两个运输计划复合给出上界。□

### 2.3 一个保持有理运算的连续门控

令 $c(z)=\max(-1,\min(1,z))$，取

$$
\pi_1(z)=\tfrac12+\tfrac14c(z),\qquad
\pi_0(z)=1-\pi_1(z).
$$

有限输入、端点和分段线性插值全部可用有理数计算。
对 F₀(z)=z、F₁(z)=z+1，L=D=1，
$\operatorname{TV}(\pi(z),\pi(z'))\le|z-z'|/4$，所以 κ 的 W₁ Lipschitz 常数
不超过 5/4。验证脚本还在 [-1,1] 的有理网格上直接积分 CDF，
核对 $W_1=5|z-z'|/4$。

如果采用扇区方向的周期插值，首尾扇区必须相容。
改变门控是一种候选模型修订，本次没有修改或重新训练 dirac-belt。
连续门控也不会自动解决第 1 节的表示提升与历史遗忘问题。
另一条路线是保留格身份，把它视为不同分支层，再明确边界粘合规则；
这改变了拓扑合同，不能当作原坐标拓扑中的自动连续化。

## 3. 正面结果：紧不确定集上的 Scott 连续运输

### 3.1 命题

**Status: proved with stated hypotheses.**
对 Hausdorff 空间 X，记 $\mathcal K(X)$ 为非空紧子集，
序为 $A\sqsubseteq B\iff A\supseteq B$。
它是 dcpo：非空有向族的上确界是交集。

若 $f:X\to Y$ 连续且 Y 也是 Hausdorff，则

$$
\widehat f:\mathcal K(X)\longrightarrow\mathcal K(Y),
\qquad A\longmapsto f[A]
\tag{3.1}
$$

Scott 连续。

**证明。** 对反包含有向族 $(A_i)$，选定 A₀，
限制到包含于 A₀ 的共尾子族。该子族为 A₀ 内的非空紧闭集，
有有限交性质，故交非空紧；它就是反包含序的上确界。

连续图像非空紧，且 (3.1) 单调。
显然 $f[\cap_iA_i]\subseteq\cap_if[A_i]$。
若 $y\in\cap_if[A_i]$，则各
$A_i\cap f^{-1}(\{y\})$ 非空。
在上述共尾子族上，它们是 A₀ 内具有有限交性质的闭集，
因而有共同点 x；于是 x∈∩A_i 且 f(x)=y。
得到

$$
f[\bigcap_iA_i]=\bigcap_if[A_i].
$$

故 $\widehat f$ 保持有向上确界，Scott 连续。□

### 3.2 应用于概率关系，而不先丢掉参数相关性

在第 2.2 节的条件下，取 f=κ，Y 改为带弱拓扑的概率测度空间。
可得

$$
\widehat\kappa(A)=
\left\{\sum_j\pi_j(z)\delta_{F_j(z)}:z\in A\right\}
\tag{3.2}
$$

是 Scott 连续的紧不确定集运输。
这里得到的是“一组可能的完整概率律”，不是先给 A 选一个先验后混合成一条律。
同一个 z 同时决定所有权重、输出及所携带的关系记忆。
把各权重区间、输出区间独立相乘，会丢掉这项共享关系，不能直接代替 (3.2)。

若每一步都在明确的完整状态上使用连续有限分支核，
有限次条件复合仍是这种形式：路径权重是沿该路径的条件权重乘积，
输出是分支映射的复合。因此每个固定有限词都有上述 Scott 连续提升。
共享记忆必须作为状态运输，不能在每一步无声明地重新初始化。

有理边界四边形可用 $(\xi,y)$ 盒表示，有限记忆可作为附加离散坐标，
在指定紧窗口内应用本命题。输入的完成对象允许非有理极限，
而有限边界、算术分支和证明证书仍可计算。

**边界。** 本节的目标是概率律空间的紧不确定集 dcpo，
并非连续 valuation 的通常点序，也未证明其 Scott 拓扑等于值格 Lawson 拓扑。
它没有建立任意表达式历史的全局识别、tube 粘合或无限词收敛。
一般有效紧集的精确图像是否有可操作的有限表示，还需要表示理论；
本篇的有理分段线性算例有显式表示。

## 4. 不完全保留记忆时，误差如何增长？

### 4.1 从精确下降到单步缺陷

设 Ω、S 非空有限，q:Ω→S 满射，C 为其 0–1 观察矩阵。
P 为完整状态上的行随机矩阵。
选一个行随机提升 R:S→Ω，使 RC=I，即只在对应观察纤维内分配质量。
定义重新初始化后得到的核

$$
K=RPC.
$$

它总是一个合法概率核，但未必是对所有历史成立的精确下降。
令

$$
\varepsilon=\max_{\omega}
\operatorname{TV}\big((PC)_{\omega\bullet},K_{q(\omega)\bullet}\big),
\qquad
\Delta=\max_{q(\omega)=q(\omega')}
\operatorname{TV}\big((PC)_{\omega\bullet},(PC)_{\omega'\bullet}\big).
\tag{4.1}
$$

由于 K 的每行是同一纤维内各 PC 行的凸组合，
$\varepsilon\le\Delta$。
对任意完整分布 u，三角不等式又给出

$$
\operatorname{TV}(uPC,(uC)K)\le\varepsilon.
\tag{4.2}
$$

这些是有限有理数据上的精确可计算量。
对确定性 P 和硬标签 q，各 PC 行都是点质量，所以 Δ 只能为 0 或 1；
此时“很接近的几何状态”不能仅靠 TV 得到小缺陷。
要量化这种接近，须换观察、引入概率核，或使用与几何相容的距离。

### 4.2 命题：多步误差界

**Status: proved with stated hypotheses.**
定义 Dobrushin 系数

$$
\tau(K)=\max_{i,j}\operatorname{TV}(K_{i\bullet},K_{j\bullet})\le1.
$$

它满足
$\operatorname{TV}(pK,p'K)\le\tau(K)\operatorname{TV}(p,p')$。
一个初等证明是把 p−p′ 的正负部分分别归一化为概率向量；
两个像都是 K 各行的凸组合，其距离不超过行集合的直径。
标准背景及锥上的推广见 [S1]。

设完整过程 $u_{n+1}=u_nP$，近似观察过程
$\bar p_{n+1}=\bar p_nK$，初始 $\bar p_0=u_0C$。
则 $E_n=\operatorname{TV}(u_nC,\bar p_n)$ 满足

$$
E_{n+1}\le\varepsilon+\tau E_n,\qquad
E_n\le
\begin{cases}
\varepsilon(1-\tau^n)/(1-\tau),&\tau<1,\\
n\varepsilon,&\tau=1.
\end{cases}
\tag{4.3}
$$

**证明。** 在两分布之间插入 $(u_nC)K$；
(4.2) 控制第一段，收缩系数控制第二段，随后归纳。□

对随操作变化的 P_t、R_t、K_t，同一证明给出

$$
E_n\le\sum_{t=0}^{n-1}\varepsilon_t
\prod_{j=t+1}^{n-1}\tau(K_j).
\tag{4.4}
$$

统一的质量尺度因子在归一化后消去；
若要比较绝对质量，另须保留总质量及尺度运输误差。

### 4.3 闭合关系也有误差预算

若完整操作词 w 满足 $P_w=I$，其观察词 K_w 的每行距离对应点质量
不超过 (4.4) 的预算 B_w。证明是对每个观察标签任选一个完整原像作初态。
若 $P_w=P_v$，则两条观察词满足

$$
\max_i\operatorname{TV}((K_w)_{i\bullet},(K_v)_{i\bullet})
\le B_w+B_v.
\tag{4.5}
$$

这适用于已经指定的完整过程和观察。
若只知道两个几何端点相同，而完整历史算子不相同，
不能以 (4.5) 判定它们应当具有相同的语义分布。

## 5. 一个进一步的限制：强遗忘与近似逆之间的张力

**Status: proved with stated hypotheses.**
设 K、L 为同一有限集上的概率核，标签数至少为 2。
若

$$
\eta=\max_i\operatorname{TV}((KL)_{i\bullet},e_i),
$$

则

$$
\tau(K)\tau(L)\ge1-2\eta.
\tag{5.1}
$$

**证明。** 任取 i≠j，两次三角不等式给出
$\operatorname{TV}((KL)_i,(KL)_j)\ge1-2\eta$；
另一方面，收缩系数满足
$\tau(KL)\le\tau(K)\tau(L)$。□

特别地，若要求较准确的逐状态逆，τ(K) 不能很小。
例如 η≤1/20 时，τ(K)≥9/10。
较强收缩有助于抑制 (4.3) 的累计误差，却会损失逆操作所需的可区分性。
因此“可以忘掉很多细节”与“可以准确恢复每个来源”是两项不同要求。
此结论是 note 06 随机逆限制的定量版本，不是详细平衡不可逆定理。

## 6. 固定导出数据的门控跳变认证

### 6.1 数据与读取范围

**Status: computationally verified example，带有理区间证书。**
本次读取 dirac-belt 固定提交中的
[pal/atlas.json](https://github.com/mountain/dirac-belt/blob/7eb633bde849e66feeb4b22c765780abee72936a/pal/atlas.json)
及
[pal/gating_logits.npy](https://github.com/mountain/dirac-belt/blob/7eb633bde849e66feeb4b22c765780abee72936a/pal/gating_logits.npy)。
元数据给出 8 扇区、4 深度格、32 通道；
数组为 32×32 的 binary32 logits，
Git blob 为 71e4d35e28be599d521f4c1d1ea431e3f05561e8。
这是 PAL 的一份导出数据，不是历史 Sector-Prob 的 12×4×8 模型。

按源码使用行号 sector×4+depth，在每行作 softmax。
认证对象是以已保存 binary32 logits 为精确输入的**数学 softmax**，
不包含 PyTorch 执行时的浮点舍入误差，也不是对另存的 pi.npy 逐位认证。
对相邻扇区（包括首尾接缝）以及相邻深度格比较通道分布：

| 比较 | 对数 | 已证正跳变的对数 | 最大值的有理包围区间 |
|---|---:|---:|---|
| 相邻扇区，同深度格 | 32 | 32 | [0.9632340078247685, 0.9632340078247686] |
| 相邻深度格，同扇区 | 24 | 24 | [0.9631621769719242, 0.9631621769719243] |

采用从 0 开始的指标，最大项分别在 (2,0)→(3,0) 和 (3,1)→(3,2)；
相应最大项也已通过区间分离认证为唯一最大。
表中有限小数都是有理端点，不是四舍五入值冒充严格界。

### 6.2 证书怎样避免浮点猜测

脚本先验证源字节的 Git blob，再把每个 binary32 数精确转成有理数。
为包围 softmax，减去各行最大 logit，把 $e^{-x}$、x≥0 用以下步骤认证：

1. 写 $x=2^mt$、0≤t≤1；
2. 以 24 阶 Taylor 部分和 S 包围 $e^t$，余项满足
   $$
   0\le e^t-S\le
   \frac{t^{25}/25!}{1-t/26};
   $$
3. 反复平方再取倒数，每步向外舍入到分母 $2^{96}$ 的有理格；
4. 用区间除法归一化，随后对总变差作区间运算。

这套检查不调用浮点指数，也不依赖 PyTorch 或 NumPy。
完整输出保存在
[gate-audit-20261111.json](../../research/aes-probability-transport/gate-audit-20261111.json)。

### 6.3 这个读数说明什么

它认证了冻结导出中相邻格的**通道标签分布**不同。
对把空间表示作为连续输入的硬门控扩展，这构成边界跳变的具体来源。
对固定有限概念索引赋离散拓扑时，任意函数本来就连续；
那不是这里讨论的参数邻域连续性。

它没有认证经过分支运动后输出概率律的同等跳变。
如果多个通道在所观察位置产生相同或很接近的输出，
遗忘通道身份后的弱距离可以很小，甚至为零。
它也没有测量预测准确率、语义错误或训练稳定性。

## 7. 有限重放与下一步

从仓库根目录执行：

~~~bash
python3 research/aes-probability-transport/verify_memory_and_gates.py
~~~

[脚本](../../research/aes-probability-transport/verify_memory_and_gates.py)
使用 Fraction 检查：

- 一个四状态模型的 ε=1/10、纤维直径 Δ=1/5、τ=1/2；
  4 个点初态各重放 12 步，均满足误差界；
- 9 个二标签近似逆算例；
- 289 对有理输入的 W₁ 计算；
- 等值不等门控、硬门控不保持区间套交、移动点质量不 TV 连续、
  未满足下降条件却声称零误差等反例。

若提供上述固定导出，可重放数据证书：

~~~bash
python3 research/aes-probability-transport/verify_memory_and_gates.py \
  --gate-logits /path/to/dirac-belt/pal/gating_logits.npy
~~~

后续应优先比较两种观察：保留关系通道身份，以及只保留赋值输出。
在固定输入窗口上，分别检查硬门控两侧的概率律是否有弱极限跳变；
同时明确预测 a′ 怎样成为下一步的完整状态。
这比从通道跳变直接推断语义断裂更有判别力。
是否改用连续门控，须依据这种比较以及任务目标判断。

本次已推进到：连续有限分支核的 Scott 紧集提升、记忆遗忘的有限误差预算、
近似逆与收缩的定量限制，以及一份真实导出数据的认证。
一般表达式空间、无限记忆、语义不对称来源和信息—几何面积统一仍开放。

## 8. 来源与归属

- **Human origin/direction:** 苑明理提出关系第一性、乘法跨层、
  可计算参数套、闭合关系、概率—尺度实践及 popularity / similarity 的方向判断。
- **AI contribution:** ChatGPT / Codex（OpenAI）于 2026-11-11
  核查固定源码，整理本篇证明与边界，编写有理验证及导出数据认证脚本。
- **AEG baseline:** note 06 使用 bad30f3190b5e82039a2a79a0141f18c609c8050；
  本篇承接 PR #36，不修改 paper 或治理状态登记。
- **Source audit:** 本篇第 1、6 节的链接固定到实际读取的提交。
  源码及数据只读；没有训练模型、修改模型仓库或把历史模型与 PAL 导出混同。
  源仓可能需要访问权限。
- **[S1]** Stéphane Gaubert and Zheng Qu,
  *Dobrushin's ergodicity coefficient for Markov operators on cones*，
  [作者提供的论文](https://www.cmap.polytechnique.fr/~gaubert/PAPERS/GaubertQuIEOTD14QuFinal.pdf)，
  §1，式 (1)–(2)。此处只用有限随机矩阵的标准收缩系数，
  不宣称本篇误差递推或紧集图像性质是新的通用概率论定理。
- **[S2]** Fetima Ladjimi and Marc Peigné,
  *Iterated function systems with place dependent probabilities and application
  to the Diaconis-Friedman's chain on [0,1]*，
  [arXiv:1707.07237](https://arxiv.org/abs/1707.07237)。
  作为依赖状态的分支概率与弱 Feller 框架参照；
  本篇所需有限和连续性已直接证明。
