#!/usr/bin/env python3
"""CI gate: prove the committed evidence is reproducible on any machine.

``tools/verify_all.py`` already re-runs every experiment and rebuilds every
derived artefact.  What this gate adds is the comparison against what is
*committed*, which is what makes the evidence auditable rather than merely
self-consistent:

1. run ``verify_all.py`` and require exit 0;
2. every ``evidence/*.json`` produced by an experiment must match the committed
   file **modulo the declared provenance keys**;
3. every derived artefact (``fixtures/``, ``evidence/gap-classification.json``)
   must match the committed file **byte for byte**.

The provenance keys excluded in step 2 are the interpreter version and the run
mode.  They are provenance, not mathematics: a reviewer on another machine, or
CI on another Python release, must still be able to check every substantive
byte.  Within one machine the comparison is exact, and the determinism harness
separately requires both repeated runs and ``python3`` versus ``python3 -O`` to
be byte-identical.

Run:

    python3 research/process-representation-gap/tools/ci_check.py
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
REPO = ROOT.parent.parent
sys.path.insert(0, str(HERE))
import gapkit  # noqa: E402
from check_determinism import ENVIRONMENT_KEYS, strip_environment  # noqa: E402

# Derived artefacts must reproduce exactly, so they must not carry
# machine-dependent provenance.
EXACT_ARTIFACTS = [
    "fixtures/INDEX.json",
    "evidence/gap-classification.json",
    "evidence/interface-promotion.json",
]

# Evidence documents that are inherently machine-dependent, with the keys that
# legitimately differ.  Everything else in them is still compared.
TOLERANT_ARTIFACTS = {
    "evidence/manifest.json": ("environment", "repositories.*.local_path"),
}


def relative_evidence_paths():
    out = []
    for path in sorted((ROOT / "evidence").glob("*.json")):
        rel = str(path.relative_to(ROOT))
        if rel in TOLERANT_ARTIFACTS:
            continue
        if rel in EXACT_ARTIFACTS:
            continue
        out.append(rel)
    return out


def strip_local_paths(raw: bytes) -> bytes:
    """Drop the resolved sibling-checkout paths from the manifest."""
    try:
        doc = json.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError):
        return raw
    if not isinstance(doc, dict):
        return raw
    doc.pop("environment", None)
    for entry in doc.get("repositories", {}).values():
        if isinstance(entry, dict):
            entry.pop("local_path", None)
    return json.dumps(doc, sort_keys=True, indent=2, ensure_ascii=False).encode("utf-8")


def run_verify_all():
    command = [sys.executable, str(HERE / "verify_all.py")]
    proc = subprocess.run(command, capture_output=True, check=False, cwd=str(ROOT))
    return {
        "step": "verify_all",
        "exit_code": proc.returncode,
        "stderr_tail": proc.stderr.decode("utf-8", "replace").strip().splitlines()[-3:],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--skip-verify-all", action="store_true")
    args = parser.parse_args()

    report = {"schema": gapkit.SCHEMA + ".ci-check", "steps": [], "failures": []}

    if not args.skip_verify_all:
        step = run_verify_all()
        report["steps"].append(step)
        if step["exit_code"] != 0:
            report["failures"].append({"artifact": "verify_all", "reason": "nonzero exit"})

    # Step 2: experiment evidence, modulo provenance.
    compared = []
    for rel in relative_evidence_paths():
        committed = (REPO / "research" / "process-representation-gap" / rel)
        if not committed.exists():
            report["failures"].append({"artifact": rel, "reason": "missing"})
            continue
        fresh = committed.read_bytes()
        # The evidence on disk has just been rewritten by verify_all; what we
        # compare is the committed blob against it.
        blob = subprocess.run(
            ["git", "-C", str(REPO), "show", f"HEAD:{committed.relative_to(REPO)}"],
            capture_output=True, check=False)
        if blob.returncode != 0:
            compared.append({"artifact": rel, "status": "not-committed-yet"})
            continue
        ok = strip_environment(blob.stdout) == strip_environment(fresh)
        compared.append({"artifact": rel, "status": "match" if ok else "DIFFERS",
                         "compared_ignoring": list(ENVIRONMENT_KEYS)})
        if not ok:
            report["failures"].append({
                "artifact": rel,
                "reason": "regenerated evidence differs from the committed evidence "
                          "beyond the ignored provenance keys",
            })

    # Step 3: derived artefacts, byte for byte.
    exact = []
    for rel in EXACT_ARTIFACTS:
        path = REPO / "research" / "process-representation-gap" / rel
        blob = subprocess.run(
            ["git", "-C", str(REPO), "show", f"HEAD:{path.relative_to(REPO)}"],
            capture_output=True, check=False)
        if blob.returncode != 0:
            exact.append({"artifact": rel, "status": "not-committed-yet"})
            continue
        ok = blob.stdout == path.read_bytes()
        exact.append({"artifact": rel, "status": "match" if ok else "DIFFERS"})
        if not ok:
            report["failures"].append({"artifact": rel, "reason": "not byte-reproducible"})

    # Manifest, modulo environment and the resolved checkout paths.
    manifest_rel = "evidence/manifest.json"
    path = REPO / "research" / "process-representation-gap" / manifest_rel
    blob = subprocess.run(
        ["git", "-C", str(REPO), "show", f"HEAD:{path.relative_to(REPO)}"],
        capture_output=True, check=False)
    if blob.returncode == 0:
        ok = strip_local_paths(blob.stdout) == strip_local_paths(path.read_bytes())
        report["steps"].append({"step": "manifest", "status": "match" if ok else "DIFFERS"})
        if not ok:
            report["failures"].append({
                "artifact": manifest_rel,
                "reason": "pins or expected values changed beyond environment and local_path"})

    report["evidence_compared"] = compared
    report["derived_artifacts"] = exact
    report["failures_count"] = len(report["failures"])
    report["verdict"] = ("committed evidence is reproducible on this machine"
                         if not report["failures"] else "NOT reproducible")
    sys.stdout.write(gapkit.canonical(report))
    return 1 if report["failures"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
