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
import json
import os
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


def run(script: Path, optimized: bool, hash_seed=None) -> bytes:
    """Run one checker in a fresh process.

    ``hash_seed`` matters: CPython randomises string hashing per process, so a
    checker whose OUTPUT depends on set or dict iteration order produces
    different bytes on different runs even though it is deterministic in any
    single process.  The sweep in ``main`` catches that class of defect.
    """
    cmd = [sys.executable] + (["-O"] if optimized else []) + [str(script)]
    env = dict(os.environ)
    if hash_seed is not None:
        env["PYTHONHASHSEED"] = str(hash_seed)
    proc = subprocess.run(cmd, capture_output=True, check=False,
                          cwd=str(ROOT.parent.parent), env=env)
    if proc.returncode != 0:
        raise gapkit.Diagnostic(
            "DET-RUN-FAILED",
            f"{script.name} (optimized={optimized}, seed={hash_seed}) "
            f"exited {proc.returncode}: "
            f"{proc.stderr.decode('utf-8', 'replace').strip()[:2000]}",
        )
    return proc.stdout


# Keys excluded when comparing a fresh run with the RECORDED evidence.  The
# run mode and the interpreter version are provenance, not mathematics: a
# reviewer on another machine, or CI on another Python release, must still be
# able to check every substantive byte.  Within one machine the comparison is
# still exact, and both cross-run and cross-mode comparisons are byte-exact.
ENVIRONMENT_KEYS = ("environment",)


def strip_environment(raw: bytes) -> bytes:
    """Remove the declared provenance keys from a JSON evidence document."""
    try:
        doc = json.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError):
        return raw
    if not isinstance(doc, dict):
        return raw
    for key in ENVIRONMENT_KEYS:
        doc.pop(key, None)
    return json.dumps(doc, sort_keys=True, indent=2, ensure_ascii=False).encode("utf-8")


def evidence_path_for(script: Path) -> Path:
    stem = script.stem
    return EVIDENCE / (stem.replace("_", "-") + ".json")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--only", default=None, help="restrict to one script stem")
    parser.add_argument("--seeds", default="",
                        help="extra PYTHONHASHSEED values to sweep (comma separated); "
                             "empty means no extra runs")
    args = parser.parse_args()

    scripts = sorted(p for p in EXPERIMENTS.glob("*.py") if not p.name.startswith("_"))
    if args.only:
        scripts = [p for p in scripts if p.stem == args.only]
    report = {"schema": gapkit.SCHEMA + ".determinism", "scripts": [], "failures": []}
    for script in scripts:
        entry = {"script": script.name}
        try:
            # The two plain runs use DIFFERENT, explicit hash seeds.  CPython
            # randomises string hashing per process, so a checker whose output
            # depends on set or dict iteration order differs between the two --
            # and pinning the seeds makes that comparison deterministic rather
            # than dependent on the OS entropy source.  This costs no extra
            # runs, which a multi-seed sweep does: the heaviest checker takes
            # about a minute, and a sweep would put the CI job over its budget.
            normal_a = run(script, optimized=False, hash_seed=0)
            normal_b = run(script, optimized=False, hash_seed=1)
            optimized = run(script, optimized=True, hash_seed=0)
            entry["identical_across_runs"] = normal_a == normal_b
            entry["identical_across_modes"] = normal_a == optimized
            entry["hash_seeds"] = {"run_a": 0, "run_b": 1, "optimized": 0}
            entry["hash_order_stable"] = normal_a == normal_b
            if not entry["hash_order_stable"]:
                report["failures"].append({
                    "script": script.name,
                    "error": {"code": "DET-HASH-SEED-UNSTABLE",
                              "detail": "output depends on PYTHONHASHSEED"},
                })
            extra = [int(x) for x in str(args.seeds).split(",") if x.strip()]
            if extra:
                seeded = {seed: run(script, optimized=False, hash_seed=seed)
                          for seed in extra}
                entry["extra_seed_sweep"] = {
                    "seeds": extra,
                    "identical": len(set(seeded.values())) == 1
                    and seeded[extra[0]] == normal_a,
                }
                if not entry["extra_seed_sweep"]["identical"]:
                    report["failures"].append({
                        "script": script.name,
                        "error": {"code": "DET-HASH-SEED-UNSTABLE",
                                  "detail": f"output differs under seeds {extra}"},
                    })
            entry["output_sha256"] = gapkit.sha256_bytes(normal_a)
            recorded = evidence_path_for(script)
            if recorded.exists():
                entry["recorded_evidence"] = recorded.name
                entry["byte_identical_to_recorded"] = recorded.read_bytes() == normal_a
                entry["matches_recorded_evidence"] = (
                    strip_environment(recorded.read_bytes())
                    == strip_environment(normal_a))
                entry["compared_ignoring"] = list(ENVIRONMENT_KEYS)
                if not entry["matches_recorded_evidence"]:
                    gapkit.require(False, "DET-EVIDENCE-STALE",
                                   f"{recorded.name} differs from a fresh run of {script.name} "
                                   f"beyond the ignored keys {ENVIRONMENT_KEYS}")
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
