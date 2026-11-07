"""Receive Chapter 3 coordinate algebra and the complete preceding checks (CC0)."""

import argparse
from fractions import Fraction
from pathlib import Path
import re
import time

import domain_fixtures
from evaluability_run import EvaluabilityRun
from run import HERE, read, require, save, sha


class Chapter03Run(EvaluabilityRun):
    def execute(self):
        # The predecessor validates its own expected counts before new work.
        # Its bounds equal the successor's: all work shares the original clock.
        previous = super().execute()
        self.contract = read(HERE / "contract-chapter03.json")
        require(self.bounds == self.contract["bounds"], "Chapter 3 changed the receiving bounds")
        cases = read(HERE / "chapter03-cases.json")
        for case in cases:
            report, _ = self.native(case["name"], domain_fixtures.encode(case), case["status"],
                                    program_name="domain-checker.adva")
            fields = report["state"]["phase"]["value"]["fields"]
            actual = Fraction(fields[0]["value"], fields[1]["value"])
            require(actual == domain_fixtures.oracle(case) == Fraction(*case["expected"]),
                    "Chapter 3 scalar path disagrees with independent goal/oracle")

        self.command("lean-chapter03", ["/usr/bin/env", "LEAN_PATH=" + str(self.output),
                     self.args.lean, "-j1", "-o", self.output / "Chapter03Coordinates.olean",
                     HERE / "Chapter03Coordinates.lean"], lean=True)
        output = (self.output / "lean-chapter03.stdout").read_text()
        diagnostics = output + (self.output / "lean-chapter03.stderr").read_text()
        require(not re.search(r"\b(?:warning|error):|sorryAx", diagnostics, re.I),
                "unclean Chapter 3 coordinate proof")
        audits = re.findall(r"'AEGPaper0\.Chapter03Coordinates\.(\w+)' (?:does not depend on any axioms|depends on axioms: \[([^\]]*)\])", output)
        mapping = read(HERE / "chapter03-map.json")
        actual = {name: sorted(x.strip() for x in raw.split(",") if x.strip()) for name, raw in audits}
        require([name for name, _ in audits] == mapping["lean_audit_names"], "Chapter 3 audit names/order differ")
        require(actual == mapping["expected_axioms"], "Chapter 3 exact global axiom audit differs")

        controls = [
            ("height", "Chapter03MissingHeight", "Type mismatch",
             ["p.snd ≠ 0 → assignment (translate s p) = assignment p + s", "translation_assignment s p"]),
            ("orientation", "Chapter03MissingOrientation", "Application type mismatch",
             ["OrthonormalOriented f", "canonical_frame_unique mu lambda a q hq f hf"]),
        ]
        for name, module, diagnostic, fragments in controls:
            command = "lean-chapter03-missing-" + name
            self.command(command, ["/usr/bin/env", "LEAN_PATH=" + str(self.output), self.args.lean,
                         "-j1", HERE / ("negative/" + module + ".lean")], codes=(1,), lean=True)
            negative = (self.output / (command + ".stdout")).read_text()
            negative += (self.output / (command + ".stderr")).read_text()
            require(negative.count("error:") == 1 and diagnostic in negative and
                    all(fragment in negative for fragment in fragments),
                    "Chapter 3 " + name + " control failed for an unrelated reason")
        expected = self.contract["expected_work"]
        require(len(self.rows) == expected["native_calls"] and len(self.calls) == expected["child_commands"],
                "Chapter 3 combined execution counts differ")
        return {**previous, "contract": "contract-chapter03.json",
                "contract_sha256": sha(HERE / "contract-chapter03.json"),
                "chapter03_map_sha256": sha(HERE / "chapter03-map.json"),
                "chapter03_lean_theorems": len(audits), "chapter03_axioms": actual,
                "chapter03_native_scalar_cases": len(cases),
                "chapter03_negative_controls": {name: "Rejected with the expected missing-hypothesis type mismatch"
                                                  for name, *_ in controls},
                "reference_steps": self.reference_budget.steps,
                "scope": "Chapter 3 pointwise coordinate field/order algebra, canonical frame linear algebra, symmetric bilinear positive coordinate metric, candidate gradient/covector metric-dual uniqueness and eikonal identity, positive-height arithmetic motions, finite paths and bridge to existing ordinary tree evaluation, prefix operators and conjugation. Native additions check scalar value words only. No smooth manifold, analytic derivative identification, curvature, completeness, Laplace/ODE/rectification or length theorem is formally certified."}


def main():
    parser = argparse.ArgumentParser()
    for name in ("machine-root", "binary", "lean", "output"):
        parser.add_argument("--" + name, type=Path, required=True)
    args = parser.parse_args()
    for name in ("machine_root", "binary", "lean"):
        setattr(args, name, getattr(args, name).absolute())
    run = Chapter03Run(args)
    result = {"status": "Failed", "calls": run.calls, "rows": run.rows}
    try:
        result.update(run.execute())
        result["status"] = "Passed"
    except Exception as error:
        result["error"] = f"{type(error).__name__}: {error}"
        raise
    finally:
        result["wall_seconds"] = time.monotonic() - run.started
        if result["wall_seconds"] > run.bounds["wall_seconds"]:
            result.update(status="Failed", error="shared deadline exhausted")
        used = sum(p.stat().st_size for p in run.output.rglob("*") if p.is_file())
        if used + 1048576 > run.bounds["artifact_bytes"]:
            result.update(status="Failed", error="final artifact capacity exhausted")
        save(run.output / "result.json", result)
        require(result["status"] == "Passed", "Chapter 3 coordinate reception did not pass")


if __name__ == "__main__":
    main()
