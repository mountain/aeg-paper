# 导出 S：shift = 时序后继（词/遍历位置），comb 层精确、分支层是缺口

## note 34 的"构造"→"导出"：S 接到 AEG 的时序结构

### Research Note v0.1 · 2026-11-01

**结论**：note 34 的 `V_index` 是构造的。本笔记把它**接到 AEG 原生结构**：carousel 的 index `k` 是**遍历位置**（Pushkarev–Byzov Thm 4.2），而 AEG 的 **marked history 时序位置**（词的第 i 个上下文，`def:marked-spinal-history`）是天然的"**unbounded 位置 + successor**"结构。取
$$
V_{\mathrm{index}} = \text{时序位置},\qquad S = \text{“前进一个时序位置”},
$$
即 **AEG 的时序后继（按一个上下文拼接，`eq:chronological-history-concatenation`）**。

**关键分层**：
- **comb（单脊）层：精确**——comb 的"左自然遍历" = 脊序 = 时序序，故 carousel 的"第 k 个"**就是**第 k 个时序位置，`S` 精确匹配。
- **分支层：是缺口**——一般树的"左自然遍历"是 **DFS**，而时序是**线性扩张**；二者不同，正与 note 29 的"平面/分支"障碍同源。**这是残余，不是已证。**

---

## 0. 目标

note 34 给出 `V = V_class ⊗ V_index`（`C⁴=S`），`V_index` 是构造的。要把 `S` **导出**自 AEG/Adva 已有对象。

---

## 1. `S` 的要求（note 33/34）

1. **unbounded**：无界整数分级；
2. **successor**：自然"下一位置"；
3. **独立于 `J`/`H`**（`H` 已排除，note 33）；
4. 与 `V_class` 张成螺旋：`C⁴=S`、`[J,S]=0`。

---

## 2. `k` = 遍历位置（Thm 4.2）

Pushkarev–Byzov **Thm 4.2**：left natural traversal = standard left traversal。carousel 的"第 k 个 LL/RL/RN/LN"是**遍历里的第 k 个位置**，`LL(k)→…→LN(k)→LL(k+1)` 是"遍历位置 + 类循环"。所以 `k` 是**位置/序**量，`S` = "**遍历前进一位**"。

---

## 3. AEG/Adva 的"位置/分级"候选

| 候选 | 所在 | unbounded | position | 备注 |
|---|---|---|---|---|
| **(A) marked history 时序位置** | AEG §2（`def:marked-spinal-history`；词 `(g_1,…,g_n)`）| 是（词长）| 是（第 i 个）| **AEG 原生，且 comb 上 = 脊序** |
| (B) iota frame ordered cut basis | Adva `frame.md`/`algebra.py`（`cuts=sorted(mask)`）| 是 | 是（排序位置）| 原生但 unplanar |
| (C) iota frame event clock | Adva `frame.md`（"event metadata"）| 是 | 是（clock 读数）| 原生但 unplanar |
| (D) Magnus arity | AEG §6（`prop:arity-cell-correspondence`）| 是 | 否（代数分级）| — |
| (E) `O(P)` rank | AEG §2（`thm:birkhoff-downset-spinal`）| 是 | 否（格秩）| unplanar |

---

## 4. 导出：`S` = 时序后继（AEG 拼接）

AEG §2 定义**时序拼接**（`eq:chronological-history-concatenation`）：
$$
\gamma\delta=(g_1,\dots,g_m,h_1,\dots,h_n),\qquad \gamma\text{ 先、}\delta\text{ 后}.
$$
把 $\delta$ 取为**单个上下文** $h$，得"**追加一个上下文**"——这就是自然的 **`S`（时序后继）**：词的位置 `i` 前进一位。

**取** `V_class` = 四角类（planar），`V_index` = 时序位置，$S$ = 追加一个上下文。则（沿用 note 34）：
$$
[J,S]=0,\qquad C^4=S,\qquad J^4=\mathrm{id}
$$
全部保持（`S` 只动 `V_index` 层，`J` 只动 `V_class` 类）。

**与 iota frame 的对应**：`V_index` 也可取 **(B)/(C)**——`frame.md` 明言 "clock readings are event metadata, not amplitude coordinates"，**正是 `V_index` 该有的样子**（独立于 `J`/`H`/`G`）。所以两条路都指向同一"位置/时钟"结构。

---

## 5. 精确性：左梳精确，其余回到"平面"缺口

**左梳（pure slot-1）层：`S` 精确 = 遍历前进。**
左梳的"左自然遍历"（DFS 先左）沿脊推进，恰是**脊序**；而 marked history 的时序也是脊序。故 carousel 的"第 k 个" = 第 k 个时序位置，`S = 时序后继` **就是**遍历前进。**精确。**
（计算验证：左梳 `N(N(N(L,L),L),L)` 的 DFS 先左沿脊；右梳 `N(L,N(L,N(L,L)))` 的 DFS 先访 `leaf-L`。脚本见 `research/iota-carousel/verify_traversal.py`。）

**右梳（pure slot-2）层：`S` ≠ 遍历前进（差的正是"左优先"）。**
右梳的脊在右子；DFS **先左**会先访问旁叶、再进脊，故遍历 ≠ 脊序 ≠ 时序。这里 `S` 仍存在（时序后继），但 carousel 的"遍历前进"与它**差一个左/右翻转**。

**一般层（含分支）：回到 note 29 的缺口。**
一般树的"左自然遍历"是 **DFS**，时序是**线性扩张**；二者不同。DFS 位置是**平面/结构**的，线性扩张是**偏序**的（`O(P)`）——与 **note 29**（`k` 是 planar、`O(P)` 是 unplanar）同源。

所以：
> **`S` = 时序后继是 AEG 原生的"位置/后继"结构；它与 carousel 的"遍历前进"在**左梳**层精确一致，在**右梳/一般**层相差一个左/右（平面）翻转，在**分支**层则分道。这个"平面翻转/分支"正是 note 29 的缺口，是 `open`。**

---

## 6. 地位与残余

| 命题 | 地位 |
|---|---|
| §2 `k` = 遍历位置（Thm 4.2）| `CLASSICAL`（Pushkarev–Byzov）|
| §3 (A) 时序位置是 AEG 原生的 unbounded+successor | `CLASSICAL`（`def:marked-spinal-history`、`eq:chronological-history-concatenation`）|
| §4 `S` = 时序后继；`C⁴=S`、`[J,S]=0` | `[对应]`（comb 上精确；见 §5）|
| §5 左梳：`S` 精确 = 遍历前进 | `[对应]` **精确**（DFS 先左沿脊 = 脊序 = 时序；计算验证）|
| §5 右梳：DFS 先访旁左叶 ≠ 脊序 | `[对应]` 精确差异（计算验证：右梳遍历先 `leaf-L`）|
| §5 分支层：DFS ≠ 线性扩张 | `[对应]` **缺口**（与 note 29 同源，open）|

**残余（`open`）**：
1. **分支层的 `S`**：carousel 的"遍历"（DFS）在分支层是平面/结构量；要把它接到时序，需要一个**平面版的时序**（例如"带左/右的线性扩张"），尚未建立。
2. **张量 vs 半直积**：`V_class`（planar Z/2）⊗ `V_index`（时序）——左/右与时序是否直接交换，还是需要半直积（"左/右翻转时序"）？
3. **一般 `n` 的严格证明**：`S` = 时序后继与 `C⁴=S` 的严格形式化。
4. **(B)/(C) 的对接**：cut basis / event clock 的 index 与词时序的 index 是否相等（`#cuts` vs `#contexts`）？

---

## 7. 参考

- AEG：`paper-1/sections/02-sequential-histories.tex`（`def:marked-spinal-history`、`eq:chronological-history-concatenation`、`thm:sequential-tree-classification`）。
- Adva：`knowledge/received/iota-frame-knowledge-2026-09-17-v1/materials/{frame.md,algebra.py}`（ordered cut basis、event clock）。
- carousel：Pushkarev–Byzov 2014 Thm 4.2 / 4.3 / Cor 4.4。
- 相关：note 29（平面缺口）、33（H 失败）、34（构造）；OQ-098.3。
