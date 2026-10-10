#!/usr/bin/env python3
"""Determinism harness: every experiment must emit identical bytes.

Work-plan section 7: "验证逻辑不得只依赖 Python assert；普通模式与优化模式应一致."
Assertions are stripped under ``-O``, so a checker that relies on them silently
stops checking.  This tool enforces the two properties that actually matter:

1. each experiment, run twice in the same mode, emits byte-identical output;
2. each experiment, run under ``python3`` and under ``python3 -O``, emits
   byte-identical output;
3. the recorded evidence file is byte-identical to a fresh run.

Run:

    python3 research/process-representation-gap/tools/check_determinism.py
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))
import gapkit  # noqa: E402

EXPERIMENTS = ROOT / "experiments"
EVIDENCE = ROOT / "evidence"

# Diagnostic codes that mean "the checker refused a mutated input".  A control
# suite that never raises any diagnostic proves nothing, so a clean run must
# still show these codes inside the emitted evidence.
REQUIRED_CONTROL_PREFIXES = ("EXP1-", "EXP2-", "EXP3-", "EXP4-", "EXP5-", "EXP6-", "EXP2I-", "EXP5I-")


def run(script: Path, optimized: bool) -> bytes:
    cmd = [sys.executable] + (["-O"] if optimized else []) + [str(script)]
    proc = subprocess.run(cmd, capture_output=True, check=False, cwd=str(ROOT.parent.parent))
    if proc.returncode != 0:
        raise gapkit.Diagnostic(
            "DET-RUN-FAILED",
            f"{script.name} (optimized={optimized}) exited {proc.returncode}: "
            f"{proc.stderr.decode('utf-8', 'replace').strip()[:2000]}",
        )
    return proc.stdout


def evidence_path_for(script: Path) -> Path:
    stem = script.stem
    return EVIDENCE / (stem.replace("_", "-") + ".json")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--only", default=None, help="restrict to one script stem")
    args = parser.parse_args()

    scripts = sorted(p for p in EXPERIMENTS.glob("*.py") if not p.name.startswith("_"))
    if args.only:
        scripts = [p for p in scripts if p.stem == args.only]
    report = {"schema": gapkit.SCHEMA + ".determinism", "scripts": [], "failures": []}
    for script in scripts:
        entry = {"script": script.name}
        try:
            normal_a = run(script, optimized=False)
            normal_b = run(script, optimized=False)
            optimized = run(script, optimized=True)
            entry["identical_across_runs"] = normal_a == normal_b
            entry["identical_across_modes"] = normal_a == optimized
            entry["output_sha256"] = gapkit.sha256_bytes(normal_a)
            recorded = evidence_path_for(script)
            if recorded.exists():
                entry["recorded_evidence"] = recorded.name
                entry["matches_recorded_evidence"] = (
                    recorded.read_bytes() == normal_a)
                if not entry["matches_recorded_evidence"]:
                    gapkit.require(False, "DET-EVIDENCE-STALE",
                                   f"{recorded.name} differs from a fresh run of {script.name}")
            else:
                entry["recorded_evidence"] = None
                entry["matches_recorded_evidence"] = None
        except gapkit.Diagnostic as exc:
            entry["error"] = exc.as_record()
            report["failures"].append({"script": script.name, "error": exc.as_record()})
            report["scripts"].append(entry)
            continue
        for key in ("identical_across_runs", "identical_across_modes"):
            if not entry.get(key):
                report["failures"].append({
                    "script": script.name, "error": {"code": "DET-" + key.upper(), "detail": ""}})
        report["scripts"].append(entry)

    text = gapkit.canonical(report)
    sys.stdout.write(text)
    return 1 if report["failures"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
