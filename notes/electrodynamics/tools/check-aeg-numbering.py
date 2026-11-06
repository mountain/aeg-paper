#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""校验"我引用的 AEG 印刷号"是否与某个 PDF 的实际编号一致。

为什么需要这个工具：Paper I 的定理/命题/定义/注共用一个章计数器，
**任何一次插入都会让后面所有印刷号平移**。2026-11-01 一天之内已经发生了两次：
本仓库（electrodynamics/）插入两条 remark（Cor 10.13 -> 10.14），
以及尚未合并的 PR #21（branch paper-1/handle-surgery-annular-interfaces）
会把 capping 定理从 10.12 推到 10.19。逐条手改引用已经出过一次错。

做法（不依赖 LaTeX 宏包，只用 pdftotext）：
  1. 从 .tex 源里按类型抽取有序的 (label, 标题) 列表；
  2. 从 PDF 文本里按类型抽取有序的 (编号, 标题开头) 列表；
  3. 同类型按顺序配对 ⇒ label -> 印刷号（并用标题前缀做一致性核对）；
  4. 与我文档里引用的编号表比对，报出不匹配项。

用法:
  python3 check-aeg-numbering.py --pdf main.pdf --tex paper-1/sections/08-caps-and-interface-disks.tex
  python3 check-aeg-numbering.py --pdf a.pdf --tex a.tex --pdf b.pdf --tex b.tex   # 多组对照
"""
import argparse
import json
import re
import subprocess
import sys

TYPES = {"theorem": "Theorem", "proposition": "Proposition", "corollary": "Corollary",
         "definition": "Definition", "lemma": "Lemma", "remark": "Remark"}

# 本文档里实际引用过的编号（新增引用时在这里登记）
CITED = {
    "prop:local-pants-handlebody-genus": ("Proposition", "10.2"),
    "prop:pants-gluing-interface-disk": ("Proposition", "10.3"),
    "thm:hole-disk-complementarity": ("Theorem", "10.4"),
    "prop:seam-circle-holonomy": ("Proposition", "10.7"),
    "rem:analytic-thickening-declared": ("Remark", "10.8"),
    "prop:polynomial-interface-spectrum": ("Proposition", "10.9"),
    "rem:three-interface-layers": ("Remark", "10.10"),
    "def:interface-record-with-residual": ("Definition", "10.11"),
    "thm:constant-boundary-capping-obstruction": ("Theorem", "10.12"),
    "rem:capping-scope-mu-essential": ("Remark", "10.13"),
    "cor:capping-dichotomy": ("Corollary", "10.14"),
    "rem:capping-singular-branch-nonempty": ("Remark", "10.15"),
    "def:certified-cap-tuple": ("Definition", "10.16"),
}

BEGIN = re.compile(r"\\begin\{(" + "|".join(TYPES) + r")\}\s*(?:\[(.*?)\])?\s*\n?\s*\\label\{([^}]+)\}", re.S)
PDF_ITEM = re.compile(r"^(" + "|".join(TYPES.values()) + r")\s+(\d+\.\d+)\s*(?:\((.*)$|\.\s*(.*)$)", re.M)


def norm(text, length=24):
    """标题前缀归一化：去掉 LaTeX 与数学符号，只留 ASCII 字母数字。"""
    text = re.sub(r"\$[^$]*\$", " ", text or "")
    text = re.sub(r"\\[a-zA-Z]+", " ", text)
    return re.sub(r"[^0-9a-zA-Z]+", "", text)[:length].lower()


def labels_from_tex(path):
    source = open(path, encoding="utf-8", errors="replace").read()
    found = []
    for kind, title, label in BEGIN.findall(source):
        found.append((TYPES[kind], label, (title or "").strip()))
    return found


def numbers_from_pdf(path):
    text = subprocess.run(["pdftotext", path, "-"], capture_output=True, text=True).stdout
    found = []
    for match in PDF_ITEM.finditer(text):
        kind, number = match.group(1), match.group(2)
        title = match.group(3) or match.group(4) or ""
        # 跨行标题：取紧随其后的一行作为补充
        found.append((kind, number, title.strip()))
    return found


def build_map(tex_path, pdf_path):
    """先把 .tex 定位到某一章（用标题匹配），再在章内按类型+标题配对。"""
    ordered = labels_from_tex(tex_path)
    scanned = numbers_from_pdf(pdf_path)

    # 1) 用第一个带标题的 .tex 条目定位章号
    chapter = None
    for _, label, title in ordered:
        if not norm(title):
            continue
        target = norm(title)[:12]
        hits = [item for item in scanned if norm(item[2])[:12] == target]
        if hits:
            chapter = hits[0][1].split(".")[0]
            break
    if chapter is None:
        raise SystemExit("无法用标题把 %s 定位到某一章" % tex_path)

    # 2) 章内条目
    in_chapter = [item for item in scanned if item[1].split(".")[0] == chapter]
    mapping, mismatches = {}, []
    for kind in TYPES.values():
        left = [item for item in ordered if item[0] == kind]
        right = [item for item in in_chapter if item[0] == kind]
        if len(left) != len(right):
            mismatches.append("%s: tex 有 %d 条，该章 PDF 有 %d 条" % (kind, len(left), len(right)))
        used = set()
        untitled = []
        for _, label, title in left:
            target = norm(title)[:12] if norm(title) else ""
            match = None
            if target:
                for index, item in enumerate(right):
                    if index in used:
                        continue
                    if norm(item[2])[:12] == target:
                        match = index
                        break
            if match is None:
                untitled.append(label)
                continue
            used.add(match)
            mapping[label] = (kind, right[match][1])
        # 无标题条目：按剩余顺序补
        leftovers = [item for index, item in enumerate(right) if index not in used]
        for label, item in zip(untitled, leftovers):
            mapping[label] = (item[0], item[1])
            mismatches.append("%s: 无标题，按顺序配到 %s %s（请人工核对）"
                              % (label, item[0], item[1]))
    return mapping, mismatches, chapter


def compare(mapping, cited):
    diffs = []
    for label, (kind, expected) in sorted(cited.items()):
        actual = mapping.get(label)
        if actual is None:
            diffs.append((label, expected, "missing"))
        elif actual[1] != expected:
            diffs.append((label, expected, actual[1]))
    return diffs


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--pdf", action="append", required=True)
    parser.add_argument("--tex", action="append", required=True)
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--shift-table", action="store_true",
                        help="只打印 CITED 条目在各 PDF 之间的编号平移表（markdown）")
    args = parser.parse_args()
    if len(args.pdf) != len(args.tex):
        raise SystemExit("每份 PDF 需要配一份 teX")

    out = {}
    for tex_path, pdf_path in zip(args.tex, args.pdf):
        mapping, mismatches, chapter = build_map(tex_path, pdf_path)
        diffs = compare(mapping, CITED)
        out[pdf_path] = {"chapter": chapter, "labels": len(mapping),
                         "ref_parse_mismatches": mismatches, "cited_differences": diffs}
        if not args.json:
            print("=== %s （定位到第 %s 章）" % (pdf_path, chapter))
            for message in mismatches:
                print("   [解析] " + message)
            if diffs:
                print("   [引用不匹配] %d 处" % len(diffs))
                for label, expected, actual in diffs:
                    print("     %-45s 我引用 %-8s 实际 %s" % (label, expected, actual))
            else:
                print("   [引用] 全部一致 ✓")
    if args.shift_table:
        rows = []
        for label in CITED:
            cells = []
            for tex_path, pdf_path in zip(args.tex, args.pdf):
                mapping, _, _ = build_map(tex_path, pdf_path)
                found = mapping.get(label)
                cells.append(found[1] if found else "—")
            rows.append((label, cells))
        header = ["item (label)"] + [p.rsplit("/", 1)[-1] for p in args.pdf]
        print("| " + " | ".join(header) + " |")
        print("|" + "---|" * len(header))
        for label, cells in rows:
            print("| `%s` | %s |" % (label, " | ".join(cells)))
        shifted = [r for r in rows if len(set(r[1])) > 1]
        print("\n平移 %d / %d 条" % (len(shifted), len(rows)))
        return 0

    if args.json:
        print(json.dumps(out, ensure_ascii=False, indent=2))
    return 1 if any(v["cited_differences"] for v in out.values()) else 0


if __name__ == "__main__":
    sys.exit(main())
