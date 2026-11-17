# Paper VI 状态登记

**文件：** `governance/05c-paper-VI-status-register.md`
**状态：** 对 Paper VI 权威
**版本：** 1.1
**日期：** 2026-11-01
**依赖：**

* `AGENTS.md`
* `governance/00e-paper-VI-process-geometry-scope.md`
* `governance/05-mathematical-status.md`（共享词汇；下文扩展）
* `paper-6/`

**适用于：** Paper VI 的数学与溯源论断。

**词汇。** Paper VI 使用 `05` 的标签（`PROVED`、`PROVED WITH STATED HYPOTHESES`、
`COMPUTATIONALLY VERIFIED EXAMPLE`、`STRUCTURAL PROPOSAL`、`CONJECTURE`、`OPEN PROBLEM`）
以及其导入来源与定义特有的标签：

* `IMPORTED CLASSICAL` — 一个带归属使用的外部定理。
* `IMPORTED TECHNICAL` — 一份同伴技术报告在已声明修订版的陈述，只按该报告所述可复现；
  不是本论文的定理，也不是 `CLASSICAL`。
* `DEFINITION` — 由论文固定的对象或构造，不是论断。
* `CONSTRUCTION` — 一个其恒等式被检查的显式构造。
* `CORRESPONDENCE` — 两个结构之间带引用证据的已陈述对齐；不是定理也不是等同。

---

## Paper VI 过程几何集成（2026-11-01）

规范源：`paper-6/`。范围：`governance/00e-paper-VI-process-geometry-scope.md`。开放问题：
`OQ-100`。本节登记新论文的论断状态。它不提升、削弱或重定义 Papers 0–V 的任何论断，且
那些论文的任何已证明节点都不得依赖它。

| ID | 状态 | 陈述与边界 |
|---|---|---|
| PVI-1 | `IMPORTED TECHNICAL` | 原生开放程序、三种读法 K/C/F 与精确切片定律从 Adva 技术报告 `docs/TECHNICAL_REPORT_PROGRAM_PROCESS_CORE.md`（`mountain/adva` commit `1b9bd090`）导入，并带 `mountain/process-geometry`（commit `c47c96fa`）的数学核心；两者都固定于 `research/process-representation-gap/reports/manifest-baseline.md`。导入不是新定理的证明，也不是 `CLASSICAL`。 |
| PVI-2 | `PROVED` | 命题 2.7（`prop:sequential-leaf`）：自由标记脊柱历史恰是带一个孔与链体的开放有限程序，直到已声明的槽位约定。有界历史把其初始标记 `x_0` 作为对应之外的一个额外数据保留。仅顺序；无分支论断。 |
| PVI-3 | `PROVED` | 定理 3.6（`thm:canonical-order`）：对每棵平面二叉树，左优先后序是对依赖序最小化对角落序逆序数的唯一线性扩张。证明：对树归纳，带父/块分解。 |
| PVI-4 | `COMPUTATIONALLY VERIFIED EXAMPLE` | 校准 3.9：由 `research/iota-carousel/verify_canonical_choice.py` 在全部 3–6 个内部顶点（等价 4–7 叶，193 棵树）的平面二叉树上检查规范序。是实现的证据，不是定理的证据。 |
| PVI-5 | `PROVED`（对应记录） | 命题 4.2：强形式「carousel 类-环 = J」为假；幸存的对应是非规范的（3 平面 × 2 定向），带索引平移的 `SR` 条目无 `J` 对应。平面/符号部分从 Paper V 导入；载体恒等式由 `research/iota-carousel/verify_omega.py` 重放，而六个平面/定向候选在对齐笔记中手工枚举，不由该脚本。负校准，不是正性论断。 |
| PVI-6 | `PROVED`（有限阻碍） | No-go 4.3：下集格 `O(P)` 的 Hasse 图的归一化 Laplacian 不能承载平面统计量 `k(t)` = 左叶数——即平移笔记与其验证器所计算的统计量；在四叶（三内部顶点）时，四棵树共享归一化谱 `(0, 0.1464, 0.5, 0.8536)` 却有不同 `k`。源的遍历指标是否在每棵树上等于 `k(t)` 是开放的（`OQ-100.2`）。平面性阻碍。 |
| PVI-7 | `COMPUTATIONALLY VERIFIED EXAMPLE` | 校准 4.6：关系 `C^4 = S`、`J_cl^4 = id`、`[J_cl,S] = 0`、`M^2 = id` 是定义的精确恒等式，并由 `research/iota-carousel/verify_planar.py` 在有限范围内重放，复现 `evidence-planar-v1.json`。`S` 是单侧平移，故 `C` 不可逆（半群作用）。`C` 与源 carousel 的等同是提案，不属于本行。双螺旋构造 `H_iota = diag(H,H)` 对其块形式为 `PROVED`，由 `verify_shift.py` 重放。 |
| PVI-8 | `STRUCTURAL PROPOSAL` | 元一原则（槽位序由载体诱导）与把 carousel 读作平面螺旋。带支持校准的命名机制；不是定理。 |
| PVI-9 | `PROVED` | 定理 5.2（`thm:sequential-recovery`）：字典的单脊柱片段是自由历史与链程序之间（直到槽位约定）的对象级等价（与单孔语境拼接相容的双射）。有界历史把初始标记保留在映射之外；分支情形被排除。 |
| PVI-10 | `CONJECTURE` | 猜想 5.3：从带平面调度结构的平面树到开放有限程序的自然一般赋值，在顺序片段上限制为 PVI-9。未证明；见 `OQ-100.1`。 |
| PVI-11 | `OPEN` | 字典行「单孔语境作为编译观测」与「charge 作为前沿数据」；三个完整程序侧验收测试（第一个受限示例是 PVI-12）；呈现与对象化范围（`OQ-100.7`、`OQ-100.8`）。 |
| PVI-12 | `COMPUTATIONALLY VERIFIED EXAMPLE` | `research/program-side-fixtures/`：一个固定三语境自由脊柱、槽位 `(1,2,1)`、用带已检查调用/嫁接签名数据的原生 `neg` 表示乘以 -1。在 `mountain/adva@87a1a6933bca3fdb5c176cbf612729e278d172f7`，一个调度与逆序数 3 与树一致。字面常量相反给出六个事件与十五个调度；遗忘常量是 15 对 1 的投影。原生重放、源绑定接收、独立组合 oracle 与拒绝控制均被存储。只测试声明的二语境签名；无一般赋值、无完整 193 树原生普查、无载体检查或定理提升。OQ-100.7 仍 OPEN。 |

**边界说明。** 本论文是草稿，其内容部分是计划。读者不得从 PVI-9 推断一般等价、从
PVI-7 推断一般载体论断、或从 PVI-5 推断规范 carousel 对应。
