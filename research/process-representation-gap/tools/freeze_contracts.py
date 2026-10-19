#!/usr/bin/env python3
"""Register new contract versions without altering any existing digest.

Merge-preserving and idempotent: existing entries are kept, and entries for the
new contract files currently present are added; changed old versions fail.  That keeps concurrent
authoring of different contracts from dropping another experiment's entry.

Run:

    python3 research/process-representation-gap/tools/freeze_contracts.py
"""

from __future__ import annotations

import sys
import argparse
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))
import gapkit  # noqa: E402

CONTRACTS = ROOT / "contracts"
LEDGER = CONTRACTS / "FROZEN.sha256"

HEADER = [
    "# Frozen contract digest ledger.",
    "# Format: <sha256>  <filename>",
    "# A contract change must add a NEW version file and update this ledger in the",
    "# same commit; a mismatch makes every citing experiment raise EXP-CONTRACT-DRIFT.",
]


def read_ledger():
    entries = {}
    order = []
    if LEDGER.exists():
        for line in LEDGER.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            digest, _, name = line.partition("  ")
            name = name.strip()
            gapkit.require(name and name not in entries and len(digest) == 64,
                           "FREEZE-LEDGER-MALFORMED", line)
            if name not in entries:
                order.append(name)
            if name:
                entries[name] = digest.strip()
    return entries, order


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="read-only verification")
    args = parser.parse_args()
    entries, order = read_ledger()
    present = sorted(p.name for p in CONTRACTS.glob("*.json"))
    gapkit.require(set(entries) <= set(present), "FREEZE-CONTRACT-MISSING")
    for name in present:
        actual = gapkit.sha256_file(CONTRACTS / name)
        if name in entries:
            gapkit.require(entries[name] == actual, "EXP-CONTRACT-DRIFT", name)
        else:
            gapkit.require(not args.check, "FREEZE-UNREGISTERED", name)
            entries[name] = actual
        if name not in order:
            order.append(name)
    lines = list(HEADER)
    for name in sorted(order):
        if name in entries:
            lines.append(f"{entries[name]}  {name}")
    if not args.check:
        LEDGER.write_text("\n".join(lines) + "\n", encoding="utf-8")
    sys.stderr.write(f"froze {len(present)} contract(s); ledger has {len(entries)} entries\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
