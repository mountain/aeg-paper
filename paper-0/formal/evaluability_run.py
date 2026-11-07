"""Receive Chapter 2 evaluability with the complete preceding regression (CC0)."""

import argparse
from fractions import Fraction
from pathlib import Path
import re
import time

from appendix_run import AppendixRun
import domain_fixtures
from run import HERE, read, require, save, sha


class EvaluabilityRun(AppendixRun):
    def __init__(self, args):
        super().__init__(args)
        self.contract = read(HERE / "contract-evaluability.json")
        self.bounds = self.contract["bounds"]

    def execute(self):
        previous = super().execute()
        cases = read(HERE / "evaluability-cases.json")
        for case in cases:
            report, _ = self.native(case["name"], domain_fixtures.encode(case), case["status"],
                                    program_name="domain-checker.adva")
            phase = report["state"]["phase"]
            if case["status"] == "Returned":
                fields = phase["value"]["fields"]
                actual = Fraction(fields[0]["value"], fields[1]["value"])
                require(actual == domain_fixtures.oracle(case) == Fraction(*case["initial"]),
                        "cancelled reciprocal rational result differs")
            else:
                require(phase["reason"] == case["reason"] == "division by zero",
                        "cancelled reciprocal rejected for another reason")
                try:
                    domain_fixtures.oracle(case)
                except ZeroDivisionError:
                    pass
                else:
                    raise ValueError("cancelled reciprocal oracle erased the zero exclusion")

        self.command("lean-evaluability", ["/usr/bin/env", "LEAN_PATH=" + str(self.output),
                     self.args.lean, "-j1", "-o", self.output / "Chapter02Evaluability.olean",
                     HERE / "Chapter02Evaluability.lean"], lean=True)
        output = (self.output / "lean-evaluability.stdout").read_text()
        diagnostics = output + (self.output / "lean-evaluability.stderr").read_text()
        require(not re.search(r"\b(?:warning|error):|sorryAx", diagnostics, re.I),
                "unclean Chapter 2 evaluability proof")
        audits = re.findall(r"'AEGPaper0\.Chapter02Evaluability\.(\w+)' (?:does not depend on any axioms|depends on axioms: \[([^\]]*)\])", output)
        mapping = read(HERE / "evaluability-map.json")
        actual = {name: sorted(x.strip() for x in raw.split(",") if x.strip()) for name, raw in audits}
        require([name for name, _ in audits] == mapping["lean_audit_names"],
                "evaluability audit names/order differ")
        require(actual == mapping["expected_axioms"], "evaluability exact global axiom audit differs")

        self.command("lean-cancelled-total", ["/usr/bin/env", "LEAN_PATH=" + str(self.output),
                     self.args.lean, "-j1", HERE / "negative/CancelledReciprocalTotal.lean"],
                     codes=(1,), lean=True)
        negative = (self.output / "lean-cancelled-total.stdout").read_text()
        negative += (self.output / "lean-cancelled-total.stderr").read_text()
        require(negative.count("error:") == 1 and "Type mismatch" in negative and
                "input ≠ s.zero → Domain s (cancelledReciprocal s) input" in negative and
                "(cancelled_reciprocal_domain s input).mpr" in negative,
                "cancelled reciprocal control failed for an unrelated reason")
        expected = self.contract["expected_work"]
        require(len(self.rows) == expected["native_calls"] and
                len(self.calls) == expected["child_commands"], "combined execution counts differ")
        return {**previous, "contract": "contract-evaluability.json",
                "contract_sha256": sha(HERE / "contract-evaluability.json"),
                "evaluability_map_sha256": sha(HERE / "evaluability-map.json"),
                "evaluability_lean_theorems": len(audits), "evaluability_axioms": actual,
                "evaluability_native_cases": len(cases),
                "cancelled_total_control": "Rejected by Lean with the expected missing-nonzero-hypothesis type mismatch",
                "reference_steps": self.reference_budget.steps,
                "scope": "Chapter 2 arbitrary finite-tree evaluability and functional semantics, closed-input independence, exact effective evaluation under a supplied equality decision, concrete rational field interpretation and failure/completion dichotomy, cancelled reciprocal domains and projective round trip, prefix-domain and condition-pullback composition, and subtraction expansion. Previous 95 Lean statements and all native controls are retained. ACS integration, Richardson's external theorem, full PGL quotient and native checker soundness are outside this continuation."}


def main():
    parser = argparse.ArgumentParser()
    for name in ("machine-root", "binary", "lean", "output"):
        parser.add_argument("--" + name, type=Path, required=True)
    args = parser.parse_args()
    for name in ("machine_root", "binary", "lean"):
        setattr(args, name, getattr(args, name).absolute())
    run = EvaluabilityRun(args)
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
        require(result["status"] == "Passed", "Chapter 2 evaluability reception did not pass")


if __name__ == "__main__":
    main()
