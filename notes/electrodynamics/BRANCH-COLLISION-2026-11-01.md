# 撞车报告：PR #21 × 本会话这一轮（V2–V7 + `capping-scope`）

**日期**：2026-11-01 ｜ **状态**：分析完成；**未擅自改动 PR #21 或 main**
**触发**：`git fetch` 时看到两个远端分支，工作区 §2 记过一次"邻座重复劳动"的教训，故先对撞再决定是否继续。

---

## 0 一句话

> **PR #21 不是"重复劳动"，是真正相邻的两块工作**——但它（a）**改写了 capping 推论的 (3)**，
> （b）会把我刚推的两条 remark 的印刷号再平移一次。合并顺序必须先定，否则我七份文档里的
> 引用会第二次失效。（我已经把校验工具准备好，见 §6。）

---

## 1 两个远端分支的现状

| 分支 | 领先 main | 落后 main | PR | 判定 |
|---|---|---|---|---|
| `research/oq096-pants-interface-disks` | 0 | 19 | **#20 已合并** | 其内容即 main 里的 `research/pants-interface-disks/`（我 V2 的对照基线）⇒ **无撞车** |
| `paper-1/handle-surgery-annular-interfaces` | **1**（`fc61fbc`） | **12** | **#21 开着** | **真撞车**，见 §2–§5 |

`fc61fbc` = "Paper I: tunnel handles, pierced caps and annular Stokes balance"（Mingli Yuan，2026-10-31 21:02），
+791/−13 行，13 个文件。

---

## 2 文件级撞车

**双方都改 `paper-1/sections/08-caps-and-interface-disks.tex`：**

| 谁 | 改动 | 插入位置 |
|---|---|---|
| PR #21 `fc61fbc` | **+185 行**（两个新子节：钻隧道加把手；双 pants 与环状接口）+ 6 条编号条目 | 第 169 行附近（在 **capping 节之前**） |
| 我的 `495c9ad` | **+39 行**（两条 remark） | capping 定理证明之后、推论之后 |

⇒ **文本冲突风险低**（插入点不同），但两者都占同一个章计数器 ⇒ **编号必然平移**。

---

## 3 编号平移表（`tools/check-aeg-numbering.py` 实测，非估算）

| 条目 | main 现在 | PR #21 分支实测 | 合并后（含我的两条） |
|---|---|---|---|
| Prop polynomial interface spectrum | 10.9 | **10.17** | 10.17 |
| Def interface record | 10.11 | **10.18** | 10.18 |
| **Theorem capping obstruction** | **10.12** | **10.19** | 10.19 |
| **Remark μ≠0 充分非必要**（我的） | **10.13** | *missing*（该分支没有） | **≈10.20** |
| **Cor capping dichotomy** | **10.14** | **10.20** | **≈10.21** |
| **Remark 奇异支非空**（我的） | **10.15** | *missing* | **≈10.22** |
| Def certified cap tuple | 10.16 | **10.21** | ≈10.23 |

> 工具对 main 的输出是 **"引用全部一致 ✓"**；对 PR #21 分支报 **8 处平移**。
> 我这边的引用已登记在 `tools/check-aeg-numbering.py` 的 `CITED` 表里，合并后改表即可一次性回灌。

---

## 4 语义级撞车（**比编号更值得看**）

### 4.1 PR #21 **改写了 capping 推论的 (3)**

原文（main 现状）：

> (3) To glue across a seam $C_e$ in the regular category **the boundary assignment
> $a|_{C_e}$ must be nonconstant** and both sides must satisfy the two-sided smooth collar contract…

PR #21 改成：

> (3) … both sides must satisfy the two-sided smooth collar contract… **Nonconstant
> $a|_{C_e}$ is necessary if a compact regular AES disk is also to fill that seam.
> The disk obstruction alone imposes no such conclusion on gluing annular collars
> without a disk filling.**

**这是一处实质性的弱化/限定**：把"必须非常数"从无条件改成"仅在圆盘填充时才必需"。
它不在我原来的 grep（按 `\label` 与标题名找）里，所以差点漏掉——**教训：diff 要看正文，不能只看标签名。**

### 4.2 另外两处对已有条目的修改

- **Prop 10.7（seam-circle holonomy）加了假设**：原文直接写 $\oint\beta$；PR #21 加了
  "assume that the declared data $a,v$ extend smoothly to a neighborhood of $D_e$
  and that $\lambda$ is constant"。即把原来隐含的条件**显式化**。
- `paper-1/aeg-paper-1.tex` 与 provenance 增加了一条 Codex 的贡献登记（tunnel/pierced-cap/double-pants 那批）。

### 4.3 与我的两条 remark 的关系

| | PR #21 | 我的两条 remark |
|---|---|---|
| 层 | **拓扑手术**：钻隧道 ⇒ 亏格 +1、$\chi-2$、端口数不变；穿孔 cap 变环带；环状 Stokes 平衡 | **解析范围**：$\mu\ne0$ 充分非必要；显式圆锥奇异 cap |
| 是否动 Thm 10.12 | **不动**（我逐 hunk 核过） | 不动 |
| 是否动 Cor | **动 (3)**（见 4.1） | 不动，但我的 Remark 10.15 就贴在它后面 |

**判定：不重复，互补，但有一处需要协调。**

1. **术语风险**：他们的 "pierced cap"（穿孔 ⇒ 环带）与我的 "singular cap"（内部一个圆锥奇异点）
   在中文语境里都可能是"破了的帽子"，读者会混。合并后应在两边各加一句区分
   （他们那句 `rem:drilled-body-meridian` 已在讨论"哪个圆还有 cap"，正好是同一条线索的落点）。
2. **逻辑上是同一个分层的两侧**：他们的 Prop 说**拓扑**上可以换掉填充关系（$\chi-2$、环带）；
   我的 Remark 说**解析**上常值边界只能靠奇点实现。合起来正好是我在 V6 里那句
   "代数/拓扑层无障碍、障碍在解析层"的**双向证据**——值得合并后写一句交叉引用。
3. **4.1 的改写会波及我的措辞**：我的 Remark 10.15 说 "Corollary(2) 的那一支非空"，
   而 (2) 未被改；但读者会顺着 (3) 的新措辞理解 "cap"。合并后应确认我的
   Remark 10.15 中 "cap" 始终指**圆盘填充**（它确实如此），必要时加半句。

---

## 5 工具与 CI

| | PR #21 | 我 |
|---|---|---|
| checker | `research/pants-interface-disks/verify_handles.py` + `evidence-handles.json`（拓扑手术的有限标定） | `research/capping-scope/verify_capping.py` + `evidence-capping.json`（解析范围） |
| CI | 改 `.github/workflows/paper0-build.yml`（+10 行） | 新增 `.github/workflows/capping-scope.yml`（路径过滤 `research/capping-scope/**`） |
| 覆盖 | 两者互不覆盖 | 同 |

`gh run list` 显示 `fc61fbc` 曾在 13:02 跑过两条 workflow 并 success——但那是 **12 个提交之前**的树，
**不覆盖**我 00:03 推的两条 remark。我的 `capping-scope` 工作流在 `553704f` 上成功（16 s，跨机器回放通过）。

---

## 6 建议的整合顺序

1. **PR #21 先 rebase/merge main**（我的两条 remark 已在 main）。让它自己解决 4.1 的措辞与编号；
2. 合并后用 `tools/check-aeg-numbering.py` **一次性**重新导出编号表（工具已就绪）；
3. 按新表回灌我这七份文档（`pants-v2…v7`、`pant-vs-feynman-01.md`、两份 README）与 AEG research 的引用；
4. 合并后重跑 `./build.sh 1` 与 `paper0-build.yml`（PR 触发）；
5. 在两边各加一句 "pierced cap ≠ singular cap" 的区分与跨层交叉引用（§4.3 第 1、2 条）——
   **草稿已备好**：`~/AEG/aeg-paper/research/capping-scope/CROSSREF-DRAFT.tex`，
   三个块（A 给我们的 remark、B 给他们的 remark、C 现在就能用），
   每块的 `\ref` 目标归属已核（A 只依赖 PR #21 的 label，B 只依赖 main 的 label，C 两边都有）。

**我这一侧不需要动任何代码**：`CITED` 表是唯一的单点，改它即可。

---

## 7 边界（这份报告**没有**做的事）

1. **没有**改 PR #21、没有动它的分支、没有在它上面 force-push。
2. **没有**替作者决定 4.1 那处改写的对错——那是 PR #21 作者的事，我只报告它与我的 remark 相邻。
3. 编号表里"合并后"一列是**推断**（把两个插入叠加），实测值要等真正合并后用工具再跑一遍。
4. **没有**逐条比对 PR #21 的 `verify_handles.py` 与我的 `verify_capping.py` 的检查项
   （两者一个查拓扑手术、一个查解析范围，粗看互不覆盖；未逐行核）。
5. 未审 PR #21 的 $\chi(S')=\chi(S)-2$ 与 $\deg$ 论证本身——那属于它的评审范围，不是我的。
