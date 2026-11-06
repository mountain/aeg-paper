#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""只读诊断：paper-0/formal/inventory.json 与当前正文树不一致的原因。

不修改 ~/AEG 的任何文件；不重新生成清单（那是"改证据让测试变绿"，需作者决定）。
做法：调用 AEG 自己的 inventory.generate() 得到 live 版本，与已提交版本逐条对齐，
报出新增 / 删除 / 字段变化的条目及其所在源文件行号，再把涉及的源文件交给 git 追责。
"""
import json
import subprocess
import sys
from pathlib import Path

AEG = Path.home() / "AEG/aeg-paper"
FORMAL = AEG / "paper-0/formal"
sys.path.insert(0, str(FORMAL))
import inventory  # noqa: E402  （AEG 自己的生成器）


def key(claim):
    return (claim["source"], tuple(claim["labels"]), claim["environment"])


def main():
    committed = json.loads((FORMAL / "inventory.json").read_text())
    live = inventory.generate()
    old = {key(c): c for c in committed["claims"]}
    new = {key(c): c for c in live["claims"]}

    added = [new[k] for k in new.keys() - old.keys()]
    removed = [old[k] for k in old.keys() - new.keys()]
    changed = []
    for k in old.keys() & new.keys():
        if old[k] != new[k]:
            fields = [f for f in old[k] if old[k][f] != new[k].get(f)]
            changed.append({"key": k, "fields": fields, "old_line": old[k]["line"],
                            "new_line": new[k]["line"]})

    print("已提交条目 %d，当前生成 %d" % (len(committed["claims"]), len(live["claims"])))
    print("新增 %d 条、删除 %d 条、字段变化 %d 条" % (len(added), len(removed), len(changed)))

    for label, rows in (("新增", added), ("删除", removed)):
        if rows:
            print("\n%s（前 12 条）：" % label)
            for r in sorted(rows, key=lambda x: (x["source"], x["line"]))[:12]:
                print("   %s:%d  %s  %s  %s" % (r["source"], r["line"], r["environment"],
                                                ",".join(r["labels"])[:40], (r["title"] or "")[:36]))
    if changed:
        print("\n字段变化（前 12 条）：")
        for c in changed[:12]:
            print("   %s  %s  行 %s -> %s" % (c["key"][0], c["key"][1], c["old_line"], c["new_line"]))

    # 追责：这些源文件在 5512938 之后被谁改过
    touched = sorted({r["source"] for r in added + removed} |
                     {c["key"][0] for c in changed})
    print("\n涉及源文件 %d 个；其后改动过它们的提交：" % len(touched))
    for src in touched[:8]:
        log = subprocess.run(["git", "-C", str(AEG), "log", "--oneline", "5512938..HEAD", "--", src],
                             capture_output=True, text=True).stdout.strip()
        print("   %s" % src)
        for line in (log.splitlines() or ["   （5512938..HEAD 内无改动）"]):
            print("      " + line)

    # 用于报告的紧凑摘要
    summary = {"committed_claims": len(committed["claims"]), "live_claims": len(live["claims"]),
               "added": len(added), "removed": len(removed), "changed": len(changed),
               "touched_sources": touched}
    Path("drift-summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
