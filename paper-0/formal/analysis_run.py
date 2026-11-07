"""Receive real analytic Chapter 3 proofs under a separate bounded profile (CC0).

The preceding native/coordinate profile remains unchanged and must also pass.
This profile rebuilds its five source imports and audits all new Mathlib proofs.
"""

import argparse
import os
from pathlib import Path
import re
import time

import analysis_dependencies
import inventory
from run import HERE, Run, read, require, save, sha


class AnalysisRun(Run):
    def __init__(self, args):
        super().__init__(args)
        self.contract = read(HERE / "contract-analysis-v1.1.json")
        self.bounds = self.contract["bounds"]

    def deadline(self):
        require(time.monotonic() - self.started < self.bounds["wall_seconds"], "analytic profile deadline exhausted")

    def compile(self, filename, namespace, names, axioms, path):
        command = "lean-" + Path(filename).stem
        self.command(command, ["/usr/bin/env", "LEAN_PATH=" + path, self.args.lean, "-j1", "-o",
                     self.output / (Path(filename).stem + ".olean"), HERE / filename], lean=True)
        output = (self.output / (command + ".stdout")).read_text()
        diagnostics = output + (self.output / (command + ".stderr")).read_text()
        require(not re.search(r"\b(?:warning|error):|sorryAx", diagnostics, re.I), "unclean analytic/import proof: " + filename)
        audits = re.findall("'" + re.escape(namespace) + r"\.(\w+)' (?:does not depend on any axioms|depends on axioms: \[([^\]]*)\])", output)
        actual = {name: sorted(x.strip() for x in raw.split(",") if x.strip()) for name, raw in audits}
        require([name for name, _ in audits] == names and actual == axioms, "exact analytic/import audit differs: " + filename)
        return actual

    def execute(self):
        lock = read(HERE / "machine.lock.json")
        for filename, expected in lock["formal_sources"].items():
            self.deadline()
            require(sha(HERE / filename) == expected, "analytic source drift: " + filename)
        require(inventory.generate() == read(HERE / "inventory.json"), "analytic manuscript/coverage inventory drift")
        dependency = analysis_dependencies.check(self.args.mathlib_root, self.deadline)
        self.command("lean-version", [self.args.lean, "--version"], lean=True)
        require("version 4.24.0," in (self.output / "lean-version.stdout").read_text(), "analytic Lean release mismatch")
        # Lake only reports the prepared dependency search path; cache fetch and
        # library compilation are preparation, never a receiving fallback.
        self.command("mathlib-path", ["/usr/bin/env", "--chdir=" + str(self.args.mathlib_root),
                     "PATH=" + str(self.args.lean.parent) + os.pathsep + os.environ["PATH"],
                     self.args.lean.parent / "lake", "env", "printenv", "LEAN_PATH"], lean=True)
        library_path = (self.output / "mathlib-path.stdout").read_text().strip()
        require(library_path and "\n" not in library_path, "invalid Mathlib library path")
        mapping = read(HERE / "analysis-map.json")
        core = {}
        for module in mapping["core_imports"]:
            core[module["module"]] = self.compile(module["file"], module["module"], module["lean_audit_names"],
                                                module["expected_axioms"], str(self.output))
        path = str(self.output) + os.pathsep + library_path
        actual = {}
        for module in mapping["modules"]:
            actual[module["module"]] = self.compile(module["file"], module["module"], module["lean_audit_names"],
                                                  module["expected_axioms"], path)
        controls = {}
        for control in self.contract["negative_controls"]:
            name = "lean-negative-" + control["name"]
            self.command(name, ["/usr/bin/env", "LEAN_PATH=" + path, self.args.lean, "-j1", HERE / control["file"]],
                         codes=(1,), lean=True)
            diagnostics = (self.output / (name + ".stdout")).read_text() + (self.output / (name + ".stderr")).read_text()
            require(diagnostics.count("error:") == 1 and "Type mismatch" in diagnostics and
                    all(part in diagnostics for part in control["expected_fragments"]),
                    "analytic negative control failed for an unrelated reason: " + control["name"])
            controls[control["name"]] = "Rejected with the expected specific type mismatch"
        require(len(self.calls) == self.contract["expected_work"]["child_commands"], "analytic child-command count differs")
        return {**dependency, "contract": "contract-analysis-v1.1.json", "contract_sha256": sha(HERE / "contract-analysis-v1.1.json"),
                "source_lock_sha256": sha(HERE / "machine.lock.json"), "analysis_map_sha256": sha(HERE / "analysis-map.json"),
                "lean_sha256": sha(self.args.lean), "new_lean_statements": sum(map(len, actual.values())),
                "core_lean_statements": sum(map(len, core.values())), "axioms": actual, "core_axioms": core,
                "negative_controls": controls,
                "scope": mapping["interpretation"], "preceding_native_profile": "chapter03_run.py must pass separately under its unchanged contract"}


def main():
    parser = argparse.ArgumentParser()
    for name in ("mathlib-root", "lean", "output"):
        parser.add_argument("--" + name, type=Path, required=True)
    args = parser.parse_args()
    for name in ("mathlib_root", "lean"):
        setattr(args, name, getattr(args, name).resolve())
    run = AnalysisRun(args)
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
            result.update(status="Failed", error="analytic shared deadline exhausted")
        used = sum(p.stat().st_size for p in run.output.rglob("*") if p.is_file())
        if used + 1048576 > run.bounds["artifact_bytes"]:
            result.update(status="Failed", error="analytic artifact capacity exhausted")
        save(run.output / "result.json", result)
        require(result["status"] == "Passed", "analytic profile did not pass")


if __name__ == "__main__":
    main()
