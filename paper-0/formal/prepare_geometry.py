"""Build the declared geometric supplement from pinned sources (CC0).

Preparation is separate from bounded proof reception. The existing prepared
Mathlib source/cache lock is checked first and remains unchanged.
"""

import argparse
import json
import os
from pathlib import Path
import subprocess

import analysis_dependencies
import geometry_dependencies

HERE = Path(__file__).resolve().parent


def main():
    parser = argparse.ArgumentParser()
    for name in ("mathlib-root", "lean", "output"):
        parser.add_argument("--" + name, type=Path, required=True)
    args = parser.parse_args()
    root, lean, output = (p.resolve() for p in (args.mathlib_root, args.lean, args.output))
    analysis_dependencies.check(root)
    lock = json.loads((HERE / "geometry-library.lock.json").read_text())
    output.mkdir(parents=True, exist_ok=False)
    old = json.loads((HERE / "mathlib.lock.json").read_text())
    # Lean chooses a package root before resolving a full module name. An
    # overlay must therefore expose every old Mathlib module, not just new ones.
    prefix = ".lake/build/lib/lean/"
    for name in old["compiled_library"]:
        if name.startswith(prefix + "Mathlib/"):
            target = output / name[len(prefix):]
            target.parent.mkdir(parents=True, exist_ok=True)
            target.symlink_to(root / name)
    env = dict(os.environ, PATH=str(lean.parent) + os.pathsep + os.environ["PATH"])
    raw = subprocess.check_output([str(lean.parent / "lake"), "env", "printenv", "LEAN_PATH"],
                                  cwd=root, env=env, text=True).strip()
    if not raw or "\n" in raw:
        raise ValueError("invalid prepared Lean search path")
    paths = [str(Path(p) if Path(p).is_absolute() else root / p) for p in raw.split(os.pathsep)]
    env["LEAN_PATH"] = os.pathsep.join([str(output), *paths])
    for module in lock["modules"]:
        if analysis_dependencies.sha(root / module["source"]) != module["source_sha256"]:
            raise ValueError("geometry source drift before compilation")
        target = output / module["olean"]
        if target.exists():
            raise ValueError("supplement would overwrite an old pinned module")
        target.parent.mkdir(parents=True, exist_ok=True)
        subprocess.run([str(lean), "-j1", "-o", str(target), module["source"]],
                       cwd=root, env=env, check=True, timeout=120)
        if analysis_dependencies.sha(target) != module["olean_sha256"]:
            raise ValueError("source-built geometry hash mismatch: " + module["module"])
        print("Received", module["module"], flush=True)
    geometry_dependencies.check(root, output)
    analysis_dependencies.check(root)


if __name__ == "__main__":
    main()
