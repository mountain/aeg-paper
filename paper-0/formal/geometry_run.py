"""Receive the geometry continuation under a separate fixed profile (CC0)."""

import argparse
import os
from pathlib import Path
import time

import analysis_dependencies
import geometry_dependencies
from analysis_run import AnalysisRun
import inventory
from run import HERE, read, require, save, sha


class GeometryRun(AnalysisRun):
    def __init__(self, args):
        super().__init__(args)
        self.contract = read(HERE / "contract-geometry.json")
        self.bounds = self.contract["bounds"]

    def execute(self):
        lock = read(HERE / "machine.lock.json")
        for filename, expected in lock["formal_sources"].items():
            self.deadline()
            require(sha(HERE / filename) == expected, "geometry source drift: " + filename)
        require(inventory.generate() == read(HERE / "inventory.json"), "geometry inventory drift")
        dependency = analysis_dependencies.check(self.args.mathlib_root, self.deadline)
        dependency.update(geometry_dependencies.check(self.args.mathlib_root, self.args.geometry_root, self.deadline))
        self.command("lean-version", [self.args.lean, "--version"], lean=True)
        require("version 4.24.0," in (self.output / "lean-version.stdout").read_text(), "Lean release mismatch")
        self.command("mathlib-path", ["/usr/bin/env", "--chdir=" + str(self.args.mathlib_root),
                     "PATH=" + str(self.args.lean.parent) + os.pathsep + os.environ["PATH"],
                     self.args.lean.parent / "lake", "env", "printenv", "LEAN_PATH"], lean=True)
        library_path = (self.output / "mathlib-path.stdout").read_text().strip()
        require(library_path and "\n" not in library_path, "invalid Mathlib library path")
        path = str(self.output) + os.pathsep + str(self.args.geometry_root) + os.pathsep + library_path
        mapping = read(HERE / "geometry-map.json")
        imported = {}
        for module in mapping["imports"]:
            imported[module["module"]] = self.compile(module["file"], module["module"],
                module["lean_audit_names"], module["expected_axioms"], path)
        audits = {}
        for module in mapping["modules"]:
            audits[module["module"]] = self.compile(module["file"], module["module"],
                module["lean_audit_names"], module["expected_axioms"], path)
        controls = {}
        for control in self.contract["negative_controls"]:
            name = "lean-negative-" + control["name"]
            self.command(name, ["/usr/bin/env", "LEAN_PATH=" + path, self.args.lean, "-j1", HERE / control["file"]],
                         codes=(1,), lean=True)
            diagnostics = (self.output / (name + ".stdout")).read_text() + (self.output / (name + ".stderr")).read_text()
            require(diagnostics.count("error:") == 1 and "Type mismatch" in diagnostics and
                    all(part in diagnostics for part in control["expected_fragments"]),
                    "geometry control failed for an unrelated reason: " + control["name"])
            controls[control["name"]] = "Rejected with the expected specific type mismatch"
        require(len(self.calls) == self.contract["expected_work"]["child_commands"], "geometry command count differs")
        require(sum(map(len, audits.values())) == self.contract["expected_work"]["new_lean_statements"],
                "geometry audit count differs")
        require(sum(map(len, imported.values())) == self.contract["expected_work"]["import_lean_statements"],
                "geometry import audit count differs")
        return {**dependency, "contract": "contract-geometry.json", "contract_sha256": sha(HERE / "contract-geometry.json"),
                "source_lock_sha256": sha(HERE / "machine.lock.json"), "geometry_map_sha256": sha(HERE / "geometry-map.json"),
                "lean_sha256": sha(self.args.lean), "new_lean_statements": sum(map(len, audits.values())),
                "import_axioms": imported, "import_lean_statements": sum(map(len, imported.values())),
                "axioms": audits, "negative_controls": controls, "scope": mapping["interpretation"],
                "preceding_profiles": "chapter03_run.py, analysis_run.py, chapter04_run.py, apollonius_run.py, projective_run.py, pgl_run.py, affine_generation_run.py, arithmetic_run.py, bruhat_run.py, fixed_points_run.py and cardinality_run.py and normalization_run.py must pass separately under unchanged contracts"}


def main():
    parser = argparse.ArgumentParser()
    for name in ("mathlib-root", "geometry-root", "lean", "output"):
        parser.add_argument("--" + name, type=Path, required=True)
    args = parser.parse_args()
    for name in ("mathlib_root", "geometry_root", "lean"):
        setattr(args, name, getattr(args, name).resolve())
    run = GeometryRun(args)
    result = {"status": "Failed", "calls": run.calls}
    try:
        result.update(run.execute())
        result["status"] = "Passed"
    except Exception as error:
        result["error"] = f"{type(error).__name__}: {error}"
        raise
    finally:
        result["wall_seconds"] = time.monotonic() - run.started
        if result["wall_seconds"] > run.bounds["wall_seconds"]:
            result.update(status="Failed", error="geometry shared deadline exhausted")
        used = sum(p.stat().st_size for p in run.output.rglob("*") if p.is_file())
        if used + 1048576 > run.bounds["artifact_bytes"]:
            result.update(status="Failed", error="geometry artifact capacity exhausted")
        save(run.output / "result.json", result)
        require(result["status"] == "Passed", "geometry profile did not pass")


if __name__ == "__main__":
    main()
