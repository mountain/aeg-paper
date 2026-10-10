#!/usr/bin/env python3
"""Freeze the source baseline for the process-representation-gap programme.

The work plan (section 3) requires a frozen baseline manifest: repository,
exact commit, source path, Git blob, SHA-256, environment and commands.  This
script reads the *Git object store* of each pinned repository, never a working
tree copy, so a locally reformatted or re-encoded file cannot substitute for
the pinned bytes.

It refuses to proceed if a pinned commit is missing, and it never falls back to
``main``.  A missing pin is a blocker to report, not a value to invent.

Run:

    python3 research/process-representation-gap/tools/build_manifest.py \
        --out research/process-representation-gap/evidence/manifest.json
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import gapkit  # noqa: E402

REPOS = {
    "aeg-paper": {
        "remote": "mountain/aeg-paper",
        "path_env": "AEG_PAPER_REPO",
        "pins": {
            "pr16_review_head": "3b90a423fafc2a838269855c8c68286449c61c4c",
            "pr16_base": "dd7b93e5eda57343e1ff05ed954883db310eda1d",
            "merge_main": "735695cbc7ce512a1cd5e188577613eda4b3083c",
        },
        "files": [
            "AGENTS.md",
            "README.md",
            "governance/05-mathematical-status.md",
            "governance/08-open-questions.md",
            "governance/opposite-feature-witness-2026-10-09.md",
            "paper-4/README.md",
            "paper-4/sections/05b-ported-aes-programs.tex",
            "paper-4/sections/05-contextual-residuals.tex",
            "paper-4/scripts/verify-opposite-features.py",
            "paper-4/scripts/verify-ported-aes.py",
            "paper-4/scripts/fixtures/opposite-features/adva-0114.json",
            "paper-4/scripts/fixtures/opposite-features/evidence.json",
        ],
        "file_commit": "735695cbc7ce512a1cd5e188577613eda4b3083c",
    },
    "adva": {
        "remote": "mountain/adva",
        "path_env": "AEG_ADVA_REPO",
        "pins": {
            "pr16_reproduction": "cce73004c2b4fbfb87d9ba1ccc66820423273cf6",
            "new_experiment_candidate": "1b9bd090b2c4710916b6a0ccca0ad88fb7d323bd",
        },
        "files": [
            "docs/PROGRAM_PROCESS_CORE.md",
            "docs/TECHNICAL_REPORT_PROGRAM_PROCESS_CORE.md",
            "docs/research/0233-periodic-programs-before-floquet-observations.md",
            "docs/research/0114-three-sided-trace-arithmetic-calibration.md",
            "programs/bootstrap-0/first-trace-arithmetic.adva",
        ],
        "file_commit": "1b9bd090b2c4710916b6a0ccca0ad88fb7d323bd",
    },
    "process-geometry": {
        "remote": "mountain/process-geometry",
        "path_env": "AEG_PROCESS_GEOMETRY_REPO",
        "pins": {
            "baseline": "c47c96fa79123c677172278be59d67ca1cc891b1",
        },
        "files": [
            "README.md",
            "docs/RESEARCH_STATUS.md",
            "docs/ENGINEERING_ARCHITECTURE.md",
            "docs/RESEARCH_PROGRAM.md",
            "docs/MATHEMATICAL_CORE.md",
            "docs/00-process-presentation-v0.1.md",
            "docs/06-addition-multiplication-function-theory.md",
            "docs/51-aeg-addition-multiplication-rank-transition.md",
            "docs/50-aeg-translation-objectification-rank-lowering.md",
            "docs/44-objectification-semantic-compression-and-rank-lowering.md",
            "src/process_geometry/process/history.py",
            "src/process_geometry/experimental/finite_task_quotient.py",
            "src/process_geometry/signature.py",
        ],
        "file_commit": "c47c96fa79123c677172278be59d67ca1cc891b1",
    },
}

# The plan states these expected values.  They are re-derived here and the
# comparison is recorded; a mismatch is a blocker, never a silent update.
EXPECTED = {
    ("adva", "programs/bootstrap-0/first-trace-arithmetic.adva"): {
        "size": 10682,
        "git_blob": "de247cd071f714e14a91b0e54a9bab77b0de43e9",
        "sha256": "637c2d05663fcee780156d93f4f9e19f829418213a4948c91113141b64d3a579",
    },
}


def git(repo_path: str, *args: str) -> bytes:
    proc = subprocess.run(
        ["git", "-C", repo_path, *args],
        capture_output=True,
        check=False,
    )
    if proc.returncode != 0:
        raise gapkit.Diagnostic(
            "MANIFEST-GIT-FAILED",
            f"git {' '.join(args)} in {repo_path}: "
            f"{proc.stderr.decode('utf-8', 'replace').strip()}",
        )
    return proc.stdout


def pin_record(repo_path: str, commit: str) -> dict:
    raw = git(repo_path, "rev-parse", f"{commit}^{{commit}}").decode().strip()
    gapkit.require(raw == commit, "MANIFEST-PIN-MISMATCH", f"{commit} -> {raw}")
    return {"commit": commit, "resolved": raw, "available": True}


def file_record(repo_path: str, commit: str, path: str) -> dict:
    blob = git(repo_path, "rev-parse", f"{commit}:{path}").decode().strip()
    payload = git(repo_path, "cat-file", "blob", blob)
    return {
        "path": path,
        "available": True,
        "git_blob": blob,
        "size_bytes": len(payload),
        "sha256": gapkit.sha256_bytes(payload),
    }


def build() -> dict:
    record = {
        "schema": gapkit.SCHEMA,
        "kind": "source-baseline-manifest",
        "generated_by": "tools/build_manifest.py",
        "environment": gapkit.environ(),
        "repositories": {},
        "plan_expected_value_checks": [],
        "blockers": [],
    }
    for name, spec in sorted(REPOS.items()):
        repo_path = str(gapkit.sibling_repo(spec["path_env"]))
        entry = {"remote": spec["remote"], "local_path": repo_path, "pins": {}, "files": []}
        for label, commit in sorted(spec["pins"].items()):
            try:
                entry["pins"][label] = pin_record(repo_path, commit)
            except gapkit.Diagnostic as exc:
                entry["pins"][label] = {"commit": commit, "available": False, "error": exc.as_record()}
                record["blockers"].append(f"{name}:{label}:{commit}")
        file_commit = spec["file_commit"]
        for path in spec["files"]:
            try:
                rec = file_record(repo_path, file_commit, path)
            except gapkit.Diagnostic as exc:
                rec = {"path": path, "available": False, "error": exc.as_record()}
            entry["files"].append(rec)
            expected = EXPECTED.get((name, path))
            if expected is not None:
                observed = {
                    "size": rec.get("size_bytes"),
                    "git_blob": rec.get("git_blob"),
                    "sha256": rec.get("sha256"),
                }
                check = {
                    "repository": name,
                    "path": path,
                    "expected": expected,
                    "observed": observed,
                    "agrees": all(observed.get(k) == v for k, v in expected.items()),
                }
                record["plan_expected_value_checks"].append(check)
        record["repositories"][name] = entry
    for check in record["plan_expected_value_checks"]:
        if not check["agrees"]:
            record["blockers"].append(
                f"expected-value-mismatch:{check['repository']}:{check['path']}"
            )
    return record


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", default=None)
    args = parser.parse_args()
    record = build()
    text = gapkit.emit(record, args.out)
    if args.out is None:
        sys.stdout.write(text)
    else:
        for blocker in record["blockers"]:
            sys.stderr.write(f"BLOCKER {blocker}\n")
    return 1 if record["blockers"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
