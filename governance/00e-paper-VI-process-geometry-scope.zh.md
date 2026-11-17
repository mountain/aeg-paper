# 权威范围：Paper VI — 过程几何（Process Geometry）

**状态：** 权威范围规范（新论文，不是 Papers 0–V 的修正案）
**版本：** 1.0
**日期：** 2026-11-01
**适用于：** `paper-6/`；以及 `README.md` 与 `01-paper-series-architecture.md` 中描述
Paper V 之后系列的表格行。那些文件对 Papers 0–IV 权威（`00c` 对 Paper V 权威），故本文件
在其被扩展之前支配 Paper VI。
**优先性：** 在 §2 所列领地内，本文件优先于研究笔记。它不取代 `00`、`00a`、`00b`、`00c`
或 `01` 关于 Papers 0–V 的任何陈述，且它不授予 Paper VI 重定义其对象的权利。

---

## 1. 为什么存在第七篇论文

Papers 0–V 从语法到几何、分析、奇异性、凝聚与三元特征发展算术表达式几何。其中每一篇都
把*运算序列*视为原始历史：Paper I 把其历史限制为顺序树，Paper V 的载体是那条线的端点，
而非程序理论。

当前研究产生了第二个 Papers 0–V 都不拥有的原生形式体系：

* **过程几何**（`mountain/process-geometry`、`docs/MATHEMATICAL_CORE.md`、
  `docs/THEORY_MAP.md`）：一个过程优先的库，其原生对象是带有序孔、保留构造历史与三种
  耦合读法（构造、因果、前沿）的开放有限带型程序，连同呈现、商与对象化。
* **carousel/iota 主线**（`notes/analysis-and-calculus/26`–`40`、
  `research/iota-carousel/`、`research/donaghey-orbits/`）：元一 iota 载体、平面螺旋模
  `C^4 = S`、carousel 对应，以及任意平面二叉树的规范求值顺序。
* **过程表示缺口**实验（`research/process-representation-gap/`），在固定源修订版比较已声明
  过程表示与任务充分呈现。

统一观察是：元一 iota 在槽位上诱导一个序，故算术表达式的脊柱与左/右梳序是开放程序上过程
序的特殊情形。本论文的计划是陈述该一般理论，并精确化与算术表达式几何的等价。

因此 Paper VI 是一个**新槽位**，不是修正案：它导入 Papers I 与 V 的对象与过程语料，并
拥有两者都不声称的一般理论。

## 2. Paper VI 拥有什么

Paper VI 可以把以下定义并发展为它自己的主要理论。

### 2.1 原生程序过程

* 开放有限程序：带有序孔、显式源与 occurrence 身份、显式复制与丢弃、保留构造历史的
  带型表达式 DAG；
* 三种读法 K（构造与替换）、C（因果发展）、F（切割与前沿），以及「它们是一个过程的读法」
  这一陈述；
* 作为构造序线性扩张的求值调度，而非序本身；
* 切片、切割联结，以及外部切片在调度选择下的不变性。

### 2.2 元一载体与求值顺序

* 元一原则：iota 载体作用于一个槽位，因此诱导一个槽位序，由此恢复脊柱与左/右梳序；
* 平面二叉树及其角落序、依赖偏序与线性扩张；
* 规范求值顺序：对角落序最小化逆序数的唯一线性扩张（左优先后序），带任意树的证明与
  有限校准；
* 该序与标记历史、镜像/反演、Donaghey 型树变换的关系，仅作为有界陈述。

### 2.3 carousel 对应

* carousel 的类级四循环与其二阶计数影子；
* iota 复单位 `J`、三个面向对立关系平面，以及从 Paper V 导入的手性符号定律；
* 平面螺旋模 `V = V_class ⊗ V_index`，带 `C^4 = S`，其作为有限校准的地位，以及切割
  Laplacian 不承载指标的阻碍；
* 对应及其限度：强形式「carousel = J」被反驳，幸存的对应恰按已确立的强度陈述。

### 2.4 算术–过程字典与等价

* 算术表达式对象（表达式树、标记脊柱历史、算子、charge）与过程对象（程序体、调度、读法、
  前沿）之间的带型字典；
* 字典所支持的等价陈述，每条带其论断状态：已证明、条件证明、计算验证示例、结构性提案或
  开放；
* 等价的精确范围：哪些 AEG 陈述被恢复为顺序（单脊柱）特殊情形，哪些过程陈述尚无 AEG 对应。

## 3. Paper VI 不得发展什么

* Papers 0–V 的奠基对象：算术表达式空间、运动、余循环、接触结构、射影语义、零几何、
  双曲函数论、凝聚、三元特征或孔径；
* 超出为其登记状态证明等价的论断；
* 把过程几何的工程语料当作数学：Rust 内核、CLI、包、fixture 与 API 承诺是被引用的来源，
  不是定理；
* 由对应导出的一般复杂度、困难性或可判定性论断；
* 把 Pushkarev–Byzov、Donaghey 或任何其他外部结果提升到其经典状态之上；
* 重定义 Paper I 的顺序历史或 Paper V 的载体；本论文通过引用导入它们。

## 4. 与早先论文的关系

依赖是单向的：

```text
Paper 0 (expression-space and charge vocabulary) --+
Paper I (marked spinal histories, mirror/reversal) --+--> Paper VI
Paper V (six-state carrier, iota, chirality sign law) -+    (program processes, evaluation order,
                                                              carousel correspondence, equivalence)
```

Paper VI 可以通过引用 Paper I 陈述顺序情形的结果、引用 Paper V 陈述载体、引用 Paper 0
陈述表达式空间与 charge 词汇。它不得在其范围内证明新论断，也不得被用作 Papers 0–V 任何
已证明节点的依赖。

## 5. 来源语料与状态

被接纳的来源，按优先顺序：

1. 本范围文件与治理记录；
2. `paper-6/` 本身；
3. AEG 研究笔记 `notes/analysis-and-calculus/26`–`40`（Donaghey、镜像/反演、PPCT 格、
   carousel 与 iota、规范选择）；
4. `research/iota-carousel/` 与 `research/donaghey-orbits/` 的证据与验证器；
5. `research/process-representation-gap/` 的报告与提案，按其固定修订版；
6. 过程几何的 `docs/MATHEMATICAL_CORE.md`、`docs/THEORY_MAP.md` 与
   `docs/RESEARCH_STATUS.md`，按已声明修订版；
7. `00c` 接纳的 Adva 研究笔记（0001–0127），以及（仅过程材料）按哈希引用的更晚笔记；
8. 外部经典来源：Donaghey (1980)、Pushkarev–Byzov (2014)，以及标准序/格参考文献。

笔记与固定 checkout 是证据，不是权威。陈述只有带状态标签才能进入手稿，且每个导入的外部
定理保留其经典归属。

## 6. 论断状态与诚实要求

Paper VI 使用 `governance/05c-paper-VI-status-register.md` 的词汇：`PROVED`、
`PROVED WITH STATED HYPOTHESES`、`COMPUTATIONALLY VERIFIED EXAMPLE`、
`STRUCTURAL PROPOSAL`、`CONJECTURE`、`OPEN PROBLEM`，以及导入来源标签
`IMPORTED CLASSICAL` 与 `IMPORTED TECHNICAL`。

* 有限校准绝不提升为定理。
* 非规范对应按非规范陈述。
* 等价按当前支持的强度陈述；其开放方向列为开放问题，而非推论。
* 每个导入的过程几何陈述命名其修订版；漂移是边界，不是许可。

## 7. 交付物与验收

Paper VI 是 `paper-6/aeg-paper-6.tex` 处的手稿，由 `./build.sh 6` 构建，含：

* 引言与计划；
* 原生过程载体与元一原则；
* 求值顺序与规范序定理；
* carousel 对应与螺旋载体；
* 算术–过程字典与等价陈述；
* 一个列出开放问题及其依赖的边界节；
* 一个参考文献与一个论断台账。

草稿可以把各节陈述为计划而非已证明理论，前提是每条论断带其状态。作为可审查手稿被接受
要求：没有开放问题被呈现为已解决，且每个有限论断命名其验证器。
