#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Read-only diagnosis of the drift between paper-0/formal/inventory.json and the
current Paper 0 manuscript tree.

It does NOT write inventory.json and does not touch the manuscript.  It calls the
repository's own generator (paper-0/formal/inventory.py), aligns the live result
with the committed manifest, and blames the source files with git.

Run from anywhere:
    python3 research/formal-inventory-drift/diagnose.py
Exit code 0 when the manifest already matches, 1 when it has drifted.
"""
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
FORMAL = ROOT / "paper-0/formal"
sys.path.insert(0, str(FORMAL))
import inventory  # noqa: E402


def key(claim):
    return (claim["source"], tuple(claim["labels"]), claim["environment"])


def main():
    committed = json.loads((FORMAL / "inventory.json").read_text())
    live = inventory.generate()
    old = {key(c): c for c in committed["claims"]}
    new = {key(c): c for c in live["claims"]}
    added = sorted((new[k] for k in new.keys() - old.keys()), key=lambda c: (c["source"], c["line"]))
    removed = sorted((old[k] for k in old.keys() - new.keys()), key=lambda c: (c["source"], c["line"]))
    changed = [{"labels": list(k[1]), "source": k[0], "old_line": old[k]["line"], "new_line": new[k]["line"]}
               for k in old.keys() & new.keys() if old[k] != new[k]]
    digest_drift = sorted(p for p, d in committed.get("sources", {}).items()
                          if d != live["sources"].get(p))

    print("committed claims %d | live claims %d | added %d | removed %d | field-changed %d"
          % (len(committed["claims"]), len(live["claims"]), len(added), len(removed), len(changed)))
    print("committed source digests %d | live %d | drifted %d"
          % (len(committed.get("sources", {})), len(live["sources"]), len(digest_drift)))
    for row in added:
        print("  + %s:%d  %s  %s  %s" % (row["source"], row["line"], row["environment"],
                                         ",".join(row["labels"])[:44], (row["title"] or "")[:40]))
    for row in removed:
        print("  - %s:%d  %s  %s" % (row["source"], row["line"], row["environment"],
                                     ",".join(row["labels"])[:44]))
    for row in changed:
        print("  ~ %s  %s  line %d -> %d" % (row["source"], row["labels"], row["old_line"], row["new_line"]))
    for path in digest_drift:
        print("  digest %s differs" % path)

    touched = sorted({r["source"] for r in added + removed} | {c["source"] for c in changed} | set(digest_drift))
    print("\nsources involved: %d" % len(touched))
    for source in touched:
        log = subprocess.run(["git", "-C", str(ROOT), "log", "--oneline", "--", source],
                             capture_output=True, text=True).stdout.strip().splitlines()
        print("  %s" % source)
        for line in log[:3]:
            print("      %s" % line)
    return 0 if not (added or removed or changed or digest_drift) else 1


if __name__ == "__main__":
    sys.exit(main())
