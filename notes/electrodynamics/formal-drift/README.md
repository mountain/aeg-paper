# formal-drift（工作区草稿）

AEG 侧的正式报告已落在仓库内：
`~/AEG/aeg-paper/research/formal-inventory-drift/`（`README.md` + `diagnose.py` + `drift-summary.json`）。

本目录只保留最初的诊断脚本副本与摘要，供工作区离线查阅：

- `diagnose_inventory_drift.py`：第一版（指向 `~/AEG` 的只读诊断）
- `drift-summary.json`：摘要（95→102、+7、4 处行号平移、9/22 摘要变化）

**结论一句话**：`paper-0/formal/inventory.json` 自 `99f15bc`（2026-10-29）起落后于正文树，
因为那次提交在 `03-aes-and-motion.tex` 插入了 6 个命题 + 1 条 remark 却没有重新生成清单；
该检查两天没被发现，是因为 `paper0-formal.yml` 原本只在 PR 且路径命中 `paper-0/formal/**` 时运行。
**未修**（重新生成会改写验证产物），当前是红但安全（不在 required checks 中）。
