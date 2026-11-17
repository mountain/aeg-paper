# 最小对向过程特征快照实验

日期：2026-10-09。作者方向：苑明理；实现与分析由 Codex 准备。基线：aeg-paper
`dd7b93e5eda57343e1ff05ed954883db310eda1d`。状态：独立有限实验与数学边界记录。无现有冻结
证据或手稿定理被改变。

## 来源与权威

固定来源仓库：`mountain/adva`，commit `cce73004c2b4fbfb87d9ba1ccc66820423273cf6`。
来源路径：`docs/research/0114-three-sided-trace-arithmetic-calibration.md` 与
`programs/bootstrap-0/first-trace-arithmetic.adva`。后者的获取 UTF-8 字节被复制到
`paper-4/scripts/fixtures/opposite-features/adva-0114.json`。SHA-256：
`637c2d05663fcee780156d93f4f9e19f829418213a4948c91113141b64d3a579`。Git blob：
`de247cd071f714e14a91b0e54a9bab77b0de43e9`。来源的 BLAKE3 文档/见证/trace 引用作为不透明
坐标保留；此 checker 不重算那些上游摘要协议或重跑 Rust 生产者。SHA-256 检查传输字节，而非
外部真理。不从该固定记录推断任何当前 Adva main 断言。

支配的 Paper IV 条件是 PIV-S1/S2/S3/S5/S6 与 `paper-4/sections/05b-ported-aes-programs.tex`。
这是附着于该有限接口的快照适配器，不是 Adva 机制的实现或忠实 AES 门运动的构造。

## 接口：可观测、形式、谱

| 种类 | 候选 | 含义与限度 |
|---|---|---|
| 直接记录观测 | 带框架 ID、机制、标签输入/输出与路由交接的有序事件 | 对照冻结投影记录重算；事件是记录，不是独立见证执行 |
| 直接投影 | T=(frames,handoffs,transferred ports)，S=(labelled start,end)，C=(compute,verify,learn,length,alternations) | 政策固定坐标序与字面载体标签；载体 ID 不是数值赋值 |
| 来源包 | 仓库、完整 commit、路径、字节哈希、来源摘要、侧、trace 引用 | 与值并列保留；无全局身份或外部认证断言 |
| 形式候选 | 交换单项式 compute^c verify^v 与比指数 (-1,+1) | 不是谱；右/左=verify/compute 是符号的，不恒等于 1 |
| 谱候选 | 未实例化 | 需要指定的自同态、闭输入/输出对象、算子域、标记与残差；未提供此算子 |

快照政策 `snapshot-v1` 保留字面事件、载体标签、完整来源包与左减右残差。信任政策是固定仓库
证据，无外部真理认证。来源真理纤维与语义填充子仍开放。丢弃来源包会改变观测政策，且不被
数值相等许可。

## 精确有限计算

宿主提取独立检查事件词一致、唯一框架、边界载体、有序交接覆盖、路由与载体连续。它推导
T、S、C 并对照持久投影与残差检查。它不执行 `compute`、`verify` 或 `learn`。

对每侧，四个不同的 Q 值生产者程序暴露 (c,v,f,h)=(compute count,verify count,frame count,
handoff count)。这些是来源包的带型*标量适配器*，不是整个事件记录的投射。其不可变源字段
标识固定侧与适配器字段；输出包络保留完整包。标量生产者是常量快照程序。其提取是独立宿主
计算，不是事件 trace 的算术实现。

有限体有 f 与 h 的显式复制门，并读取：

    y1 = c + v
    y2 = f - h
    y3 = (3*h)/f

系数 3 是单独声明的路由元数常量。提取器检查每个交接的三个路由端口。左输入是 (2,1,3,2)，
右输入 (1,2,3,2)。两个输出都恰为 (3,1,2)。四个孔与三个标量输出可使用 Paper IV 已声明的
四端载体/锚定接口；输入元数独立于端数。此处不要求或检查新 collar 或运动断言。

所有生产者输出被绑定一次，类型匹配 Q，复制显式，所有源与生产者 occurrence 在嫁接回执中
存活，组装事件图无环。体的精确定义域是 f != 0；其生产者是全的。替换与单独求值的输出一致，
两个不同合法调度亦一致。每个门被严格执行。输出观测显式为标量三元组或三元组**连同**其
来源/事件包。这些是不同的观测。三个标量输出不是 Adva 的原生 history/result/evidence 角色。

## 负控制与特征充分性

1. 两条冻结路径给出相等三元组但不同的有序机制词、事件、框架 occurrence 与 trace 引用。包
   感知观测按实际词区分它们，独立于哈希。
2. 合成词 `compute verify compute verify` 与 `verify compute verify compute` 共享关联、长度与
   交替 (2,2,4,3)，但序不同。这些是新构造控制，不是额外冻结过程执行。
3. CarrierID 型生产者不能馈入 Q 算术门。
4. f=0 导致严格除法失败；它不被射影延拓。
5. 不改变源词/投影而改变事件机制被拒绝。fixture 字节哈希单独拒绝改变的传输字节。

仅对双记录快照域与恒等延拓，标量三元组对标量观测充分。它对历史感知观测不充分：其纤维含
两条历史，其观测词不同。这直接展示 PIV-S5 中的核阻碍。丰富包在这两条记录上单射，故对此
快照观测充分。不提供延拓作用或更新实现；PIV-S6 与三侧反馈仍未测试。保留所有历史使快照
分离容易，而非压缩跨侧重构。

## 跨侧结论

**有限投影阻碍（带所述假设证明）。** 设 D 含这两条记录路径，T,S,C 恰有上述坐标政策。无
函数 chi_C 在 (T,S)(D) 上对每个 d 满足 C(d)=chi_C(T(d),S(d))。

证明：两条记录都有 T=(3,2,6) 与 S=(0,1,2,15,16,17)，而 C 分别是 (2,1,0,3,2) 与
(1,2,0,3,2)。同一输入上的函数不能返回两个不同输出。残差 (+1,-1,0,0,0) 是精确的。这排除
chi_C 的此*投影*定义，而非每个丰富时间/空间特征或未来理论。把字面历史加到 T 或 S 会改变
问题且不证明原方程。

对 T=chi_T(S,C) 与 S=chi_S(C,T)，两条记录间输入对不同。两行查找可能但提供不了独立推导的
跨侧见证、未见实例泛化或重构律。两个关系都不被提升。所需后续条件：定义可允许过程域与
特征余域、提议提取律、冻结未见实例测试与来源/观测保留。对 chi_C，用独立论证的信息丰富
(T,S) 或限制域使碰撞消失。任何限制必须排除或显式商掉其中一条记录，带观测下降论证。

形式比 verify/compute 不恒等于一；把两个权重特化为相等非零数会隐藏它。经 M6 下降仍需
holonomy/目标代数见证。不由此推出谱、共同真理坐标、不动点或 AES/Adva 等价。

## 复现与审查决定

    python3 paper-4/scripts/verify-opposite-features.py > /tmp/opposite.json
    cmp /tmp/opposite.json paper-4/scripts/fixtures/opposite-features/evidence.json
    python3 -O paper-4/scripts/verify-opposite-features.py > /tmp/opposite-O.json
    cmp /tmp/opposite.json /tmp/opposite-O.json
    python3 paper-4/scripts/verify-ported-aes.py > /tmp/ported.json
    cmp /tmp/ported.json paper-4/scripts/fixtures/ported-aes/integration-evidence.json
    python3 paper-4/scripts/verify-paper4.py

所有命令本地通过；现有 Paper IV 套件通过全部七个验证组。CI 添加普通/优化重放与精确证据
比较。无 LaTeX 源变更：源编辑规则不要求 PDF 构建，且不声称本地产出新 PDF。现有全论文构建
留在 CI。无定理、标签、记号或材料被移动；无旧断言被加强。冻结上游与集成证据保持未变。
有限检查无警告发出。

一个窄后继 PR 由可重放外部源适配器与精确有限不可能证书所保证。状态登记记录两者而不关闭
PIV-F2。下一个有用任务是在更广声明过程域上独立定义的跨侧特征律，以历史作为负控制保留；
手稿提升可随该审查进行。
