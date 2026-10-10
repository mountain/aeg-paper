#!/usr/bin/env python3
"""One command that re-verifies the whole programme.

Work-plan section 11 requires every piece of evidence to be replayable.  This
entry point chains the reproducibility tools so an independent reviewer has a
single command and a single exit code:

1. rebuild the pinned-source manifest (nonzero on any pin or expected value);
2. re-run every experiment under ``python3`` and ``python3 -O`` and compare
   with the recorded evidence;
3. rebuild the frozen-contract digest ledger;
4. regenerate the extracted fixtures;
5. rebuild the cross-experiment gap classification.

Order matters: the ledger is refreshed before the gap table, because the gap
table refuses to cite a contract whose digest is not frozen.

Run:

    python3 research/process-representation-gap/tools/verify_all.py
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
REPO = ROOT.parent.parent
sys.path.insert(0, str(HERE))
import gapkit  # noqa: E402

STEPS = [
    ("manifest", ["tools/build_manifest.py", "--out", "evidence/manifest.json"]),
    ("freeze-contracts", ["tools/freeze_contracts.py"]),
    ("determinism", ["tools/check_determinism.py"]),
    ("fixtures", ["tools/build_fixtures.py", "--out", "fixtures/INDEX.json"]),
    ("gap-classification", ["tools/build_gap_classification.py",
                            "--out", "evidence/gap-classification.json"]),
]


def run_step(name, argv):
    """Run one tool with ``research/process-representation-gap`` as the cwd.

    The tools emit relative paths, so the cwd must be the research directory,
    not the repository root; otherwise ``--out evidence/...`` resolves against
    the wrong tree.
    """
    command = [sys.executable, str(ROOT / argv[0])] + argv[1:]
    proc = subprocess.run(command, capture_output=True, check=False, cwd=str(ROOT))
    return {
        "step": name,
        "exit_code": proc.returncode,
        "stderr_tail": proc.stderr.decode("utf-8", "replace").strip().splitlines()[-3:],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--only", default=None)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    steps = STEPS if not args.only else [s for s in STEPS if s[0] == args.only]
    results = [run_step(name, argv) for name, argv in steps]
    failed = [r["step"] for r in results if r["exit_code"] != 0]
    report = {
        "schema": gapkit.SCHEMA + ".verify-all",
        "environment": gapkit.environ(),
        "steps": results,
        "failed": failed,
        "verdict": "all obligations held" if not failed else "failed: " + ", ".join(failed),
    }
    text = gapkit.canonical(report)
    sys.stdout.write(text)
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
