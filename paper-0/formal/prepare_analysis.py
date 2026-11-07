"""Prepare the pinned external mathematical library; not a proof run (CC0)."""

import argparse
import json
import os
from pathlib import Path
import subprocess

from analysis_dependencies import HERE, check, head, sha


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mathlib-root", type=Path, required=True)
    parser.add_argument("--lean-bin", type=Path, required=True)
    args = parser.parse_args()
    root, lean_bin = args.mathlib_root.resolve(), args.lean_bin.resolve()
    lock = json.loads((HERE / "mathlib.lock.json").read_text())
    if not (root / ".git").exists():
        if root.exists() and any(root.iterdir()):
            raise ValueError("Mathlib destination must be new or the pinned checkout")
        root.mkdir(parents=True, exist_ok=True)
        subprocess.run(["git", "init", str(root)], check=True)
        subprocess.run(["git", "-C", str(root), "fetch", "--depth=1", lock["repository"], lock["commit"]], check=True)
        subprocess.run(["git", "-C", str(root), "checkout", "--detach", "FETCH_HEAD"], check=True)
    if head(root) != lock["commit"]:
        raise ValueError("existing Mathlib destination has a different revision")
    for name in ("lakefile.lean", "lake-manifest.json", "lean-toolchain"):
        if sha(root / name) != lock["sources"][name]:
            raise ValueError("Mathlib configuration drift: " + name)
    version = subprocess.check_output([str(lean_bin / "lean"), "--version"], text=True)
    if "version " + lock["lean_version"] + "," not in version:
        raise ValueError("Lean release mismatch")
    env = os.environ.copy()
    env["PATH"] = str(lean_bin) + os.pathsep + env["PATH"]
    subprocess.run([str(lean_bin / "lake"), "exe", "cache", "get", *lock["cache_roots"]],
                   cwd=root, env=env, check=True)
    print(json.dumps(check(root), indent=2))


if __name__ == "__main__":
    main()
