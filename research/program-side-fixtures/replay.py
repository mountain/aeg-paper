#!/usr/bin/env python3
"""Fail-closed replay; never rewrites frozen evidence or dependency pins."""
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

HERE = Path(__file__).resolve().parent
PAPER = HERE.parents[1]
ADVA = PAPER.parent / "adva"


def require(ok, message):
    if not ok:
        raise RuntimeError(message)


def run(argv, timeout=300, **kwargs):
    return subprocess.run(list(map(str, argv)), check=True, timeout=timeout, **kwargs)


def pins():
    sources = json.loads((HERE / "sources.json").read_text())
    for name, root in [("aeg-paper", PAPER), ("adva", ADVA)]:
        pin = sources[name]
        if name == "adva":
            head = subprocess.check_output(["git", "-C", str(root), "rev-parse", "HEAD"], text=True).strip()
            require(head == pin["revision"], "Adva HEAD differs from executable pin")
            # Reject tracked changes AND untracked files in both compiled crates.
            status = subprocess.check_output(["git", "-C", str(root), "status", "--porcelain", "--untracked-files=all", "--", "Cargo.toml", "Cargo.lock", "crates/adva-ir", "crates/adva-lisp"], text=True)
            require(not status, "Adva compiled dependency is dirty")
        for item in pin["files"]:
            raw = subprocess.check_output(["git", "-C", str(root), "show", f'{pin["revision"]}:{item["path"]}'])
            require(hashlib.sha256(raw).hexdigest() == item["sha256"] and len(raw) == item["bytes"], "source pin mismatch")
    return sources


def mutations(binary, native, temporary):
    original = json.loads(native.read_bytes())
    cases = []

    def add(name, change):
        ev = json.loads(json.dumps(original))
        change(ev)
        cases.append((name, ev))

    add("invented_schedule_count", lambda e: e["spine"]["orders"].__setitem__("schedule_count", 2))
    add("missing_schedule", lambda e: e["expanded"]["orders"]["linear_extensions"].pop())
    add("wrong_canonical_word", lambda e: e["spine"]["orders"]["canonical_schedule"].reverse())
    add("wrong_slot_receipt", lambda e: e["spine"]["mapping"][0].__setitem__("slot", 2))
    add("substituted_occurrence", lambda e: e["spine"]["artifact"]["result"]["nodes"][0]["inputs"][0]["lineage"].__setitem__(0, "occurrence:forged"))
    add("substituted_source", lambda e: e["spine"]["artifact"]["result"]["occurrences"][0].__setitem__("source", "source:forged"))
    for name, evidence in cases:
        path = temporary / f"{name}.json"
        path.write_text(json.dumps(evidence))
        proc = subprocess.run([str(binary), "receive", str(path)], capture_output=True, text=True, timeout=300)
        require(proc.returncode == 1 and proc.stderr.startswith("rejected:"), f"receiver accepted {name}")
    # The mathematical oracle is tested separately from the semantic receiver.
    for name, evidence in cases[:4]:
        path = temporary / f"{name}.json"
        for optimized in [[], ["-O"]]:
            proc = subprocess.run([sys.executable, *optimized, str(HERE / "verify.py"), str(path)], capture_output=True, timeout=300)
            require(proc.returncode != 0, f"oracle accepted {name}")
    return len(cases)


def main():
    pins()
    cargo = shutil.which("cargo")
    require(cargo is not None, "cargo is required (toolchain 1.94.0)")
    base = [cargo, "+1.94.0"]
    manifest = ["--manifest-path", HERE / "Cargo.toml"]
    run([*base, "fmt", *manifest, "--", "--check"])
    run([*base, "test", "--locked", *manifest], timeout=600)
    run([*base, "clippy", "--locked", *manifest, "--all-targets", "--", "-D", "warnings"], timeout=600)
    run([*base, "build", "--locked", *manifest], timeout=600)
    run([*base, "build", "--release", "--locked", *manifest], timeout=600)
    # An explicit target directory is allowed; otherwise Cargo uses this project.
    target = Path(os.environ.get("CARGO_TARGET_DIR", HERE / "target")).resolve()
    with tempfile.TemporaryDirectory(prefix="oq1007-") as name:
        temp = Path(name)
        for profile in ["debug", "release"]:
            binary = target / profile / "aeg-oq1007-native"
            path = temp / f"{profile}.json"
            with path.open("wb") as out:
                run([binary, "produce"], stdout=out)
            require(path.read_bytes() == (HERE / "evidence-native-v1.json").read_bytes(), f"{profile} native evidence drift")
            run([binary, "receive", path])
        for options in [[], ["-O"]]:
            proc = run([sys.executable, *options, HERE / "verify.py", temp / "debug.json"], capture_output=True)
            require(proc.stdout == (HERE / "evidence-oracle-v1.json").read_bytes(), "oracle evidence drift")
        count = mutations(target / "debug/aeg-oq1007-native", temp / "debug.json", temp)
        # The old tree-side calibration remains byte-identical.
        run([sys.executable, HERE.parent / "iota-carousel/verify_canonical_choice.py", temp / "193.json"], capture_output=True)
        require((temp / "193.json").read_bytes() == (HERE.parent / "iota-carousel/evidence-canonical-choice-v1.json").read_bytes(), "existing 193-tree evidence drift")
    print(f"PASS: pinned native debug/release replay; fresh reception; normal/optimized oracle; {count} saved-candidate refusals; existing 193-tree calibration")


if __name__ == "__main__":
    main()
