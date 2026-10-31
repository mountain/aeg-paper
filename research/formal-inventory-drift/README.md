# Formal inventory drift: `paper-0/formal/inventory.json` is stale

日期：2026-11-01。状态：**DIAGNOSIS ONLY**（只读诊断，未修）。
**方向**：苑明理要求推进"过期清单"的调查。**诊断与文字**：DeepSeek Harness agent
（deepseek-v4-flash-vision-exp）。构造与接收同一作者，无独立复核。

**本次没有做的事情（重要）**：没有重新生成 `inventory.json`，没有改动
`paper-0/` 下任何源文件。理由见 §4。

---

## 1 现象

CI 检查 `symbolic-derivations`（`paper-0/formal/test_appendix.py`）在 main 上是**红的**：

```
FAIL: test_induction_mapping_has_exact_theorems_source_and_guard_boundary
    self.assertEqual(live, read("inventory.json"))
AssertionError: {'sch[251 chars]x': 'b3c07d732a70aa20e099be79323af7dcdcba7fada…
            != {'sch[251 chars]x': '9c7ace714160fd91f1815aa1b954e9f2f0c2a3c70…
Diff is 52715 characters long.
```

该测试把 `paper-0/formal/inventory.py` **现场生成**的清单与**已提交**的
`inventory.json` 逐字段比较。它失败 ⇒ 提交的清单落后于正文树。

---

## 2 实测差异（`diagnose.py`，只读）

| 量 | 已提交 | 现场生成 |
|---|---|---|
| 定理类环境条目 | **95** | **102** |
| 跟踪的源文件 | 22 | 22 |
| 源文件摘要不一致 | — | **9 / 22** |

- **新增 7 条**（全部在 `paper-0/sections/03-aes-and-motion.tex`）：
  `prop:p0-dilation-length`、`prop:p0-length-multiplicative-charge`、
  `prop:p0-length-losses`、`prop:p0-relative-defect-length-zero`、
  `prop:p0-projective-trichotomy`、`prop:p0-affine-two-layers`、
  `rem:p0-length-two-coordinates`（自述 "structural proposal"）；
- **删除 0 条**；
- **行号平移 4 条**（上面 7 条插在它们之前）：
  `thm:continuous-affine-flow` 656→916、`conv:p0-model-labels` 737→997、
  `ex:p0-e0-model` 753→1013、`ex:p0-e1-model` 763→1023；
- **9 个源文件的 sha256 变了**：`aeg-paper-0.tex`、`01-introduction`、
  `03-aes-and-motion`、`04-ripple-geometry`、`08-acs-tearing`、
  `09-contact-of-tearing`、`10-beyond-linear`、`11-holed-aes`、`12-interface`。

---

## 3 根因（追责到提交）

| 事实 | 内容 |
|---|---|
| 清单最后写入 | `5512938`（2026-10-21 04:59 UTC）"Add Taylor and Conway background…" |
| 其后动过正文的提交 | `99f15bc`（2026-10-29 18:51 +0800）"paper-0: conservative front matter, MSC, provenance, typography"（11 文件，+461/−112）与 `3b92867`（bibliography 文件名） |
| 关键漏项 | `99f15bc` 在 `03-aes-and-motion.tex` 里插入了一整块"长度 / 乘性荷 / 三分法"内容（6 命题 + 1 remark），**没有重新生成 `inventory.json`**，也没更新 `paper-0/formal/README.md` |
| 文档仍在用旧数 | `paper-0/formal/README.md` 写着 "The current live inventory has **22 source files and 95 theorem-like environments**" —— 与已提交的旧清单一致，与当前正文（102）不一致 |

**为什么两天没被发现**：`paper0-formal.yml` 原先只在 `pull_request` 且路径命中
`paper-0/formal/**` 时运行。`gh run list --workflow=paper0-formal.yml` 显示**历史上只有一次运行**
——就是 2026-11-01 我为规则集加的"每个分支都跑"那一次（`0e4978b`，失败）。
也就是说：**这个检查的红色是被 CI 规则工作暴露出来的，不是被它造成的。**
（当日 6 个提交碰 `paper-0/formal` 的文件数为 0，已核。）

---

## 4 建议的修法（**未执行**）

顺序很重要：

1. **先审那 7 条新条目**（尤其 6 个 proposition 是否应当正式化、`rem:p0-length-two-coordinates`
   自述为 structural proposal 是否要进清单）。这是内容决定，不是清单问题。
2. **再重新生成**：`python paper-0/formal/inventory.py`（该文件的 `__main__` 就是写回
   `inventory.json`）。生成器会自动把尚无 Lean/证书的条目记为 `not-yet-formalized`，
   所以重新生成**不会**把未形式化的东西伪装成已形式化 —— 这是它可接受的前提。
3. **同步更新** `paper-0/formal/README.md` 的 "95 → 102"（以及它前一行的历史 checkpoint 数字不要动）。
4. **然后**把 `paper0-formal.yml` 的 `push: branches: ["**"]` 加回来，并把
   `symbolic-derivations` 加进 `all-branches-ci` 规则集的 required checks。

**为什么我不直接执行第 2 步**：重新生成会改写一份**验证产物**，
并把 7 条**未经审阅**的正文条目一次性烘焙进清单。这属于"让证据去配合当前状态"，
按 `AGENTS.md`（"do not conceal mathematical gaps"、"Safe default when uncertain: propose the
minimum viable change"）应留给作者决定。当前状态是可以安全停住的：
`symbolic-derivations` **不在** required checks 里，所以它是红的但不锁任何分支。

---

## 5 本诊断**没有**做的事

1. **没有**判断那 7 条新命题的数学正确性（那是评审，不是清单问题）。
2. **没有**逐条分类 9 个源文件摘要变化的内容（可能全是排版/front matter，也可能是实质改动；
   要分类必须逐 diff 读 `99f15bc` 的 461/112 行）。
3. **没有**改动 `inventory.json`、`paper-0/**`、`paper0-formal.yml`。
4. **没有**核 `paper-0/formal/README.md` 里其它数字（如 "20 files and 91 environments at the
   first checkpoint"）是否仍然自洽。

---

## 6 复跑

```sh
python3 research/formal-inventory-drift/diagnose.py
# 退出码 0 = 清单与正文一致；1 = 有漂移
```

脚本只读：调用仓库自己的 `paper-0/formal/inventory.py` 生成 live 清单，
与 `inventory.json` 对齐比较，并用 `git log` 追责到源文件。
