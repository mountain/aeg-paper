"""Receive Appendix C induction together with the unchanged native regression (CC0)."""

import argparse
from pathlib import Path
import re
import time

import appendix_fixtures
from fixtures import input_data, polynomial
from run import HERE, Run, read, require, save, sha


class AppendixRun(Run):
    def __init__(self, args):
        super().__init__(args)
        self.contract = read(HERE / "contract-appendix-c-v1.1.json")
        self.bounds = self.contract["bounds"]

    def command(self, name, argv, codes=(0,), *, lean=False):
        if name == "lean-domains":
            # The same old proof now also emits the import artifact needed by
            # Appendix C. The original supervisor and proof bytes are retained.
            argv = [*argv, "-o", self.output / "Chapter02Domains.olean"]
        return super().command(name, argv, codes, lean=lean)

    def execute(self):
        previous = super().execute()
        statement = read(HERE / "appendix-statement.json")
        certificate = read(HERE / "appendix-certificate.json")
        require(statement == appendix_fixtures.statement(), "appendix statement drift")
        require(certificate == appendix_fixtures.certificate(), "appendix certificate drift")
        left, right = statement["goal"]["fields"]
        require(polynomial(left) == polynomial(right), "appendix polynomial oracle disagrees")
        self.native(statement["id"], input_data(certificate, statement["goal"]), "Returned")
        wrong = appendix_fixtures.wrong_goal()
        require(polynomial(wrong["fields"][0]) != polynomial(wrong["fields"][1]),
                "chronological negative goal is no longer distinct")
        self.native("appendix-wrong-pair-order", input_data(certificate, wrong), "Rejected")

        self.command("lean-appendix", ["/usr/bin/env", "LEAN_PATH=" + str(self.output),
                     self.args.lean, "-j1", "-o", self.output / "AppendixC.olean",
                     HERE / "AppendixC.lean"], lean=True)
        output = (self.output / "lean-appendix.stdout").read_text()
        diagnostics = output + (self.output / "lean-appendix.stderr").read_text()
        require(not re.search(r"\b(?:warning|error):|sorryAx", diagnostics, re.I), "unclean Appendix C proof")
        audits = re.findall(r"'AEGPaper0\.AppendixC\.(\w+)' (?:does not depend on any axioms|depends on axioms: \[([^\]]*)\])", output)
        mapping = read(HERE / "appendix-map.json")
        actual = {name: sorted(x.strip() for x in raw.split(",") if x.strip()) for name, raw in audits}
        require(len(audits) == len(mapping["lean_audit_names"]) and
                [name for name, _ in audits] == mapping["lean_audit_names"], "Appendix C audit names/order differ")
        require(actual == mapping["expected_axioms"], "Appendix C global axiom audit differs")

        self.command("lean-missing-ratio-guard", ["/usr/bin/env", "LEAN_PATH=" + str(self.output),
                     self.args.lean, "-j1", HERE / "negative/MissingRatioGuard.lean"], codes=(1,), lean=True)
        negative = (self.output / "lean-missing-ratio-guard.stdout").read_text()
        negative += (self.output / "lean-missing-ratio-guard.stderr").read_text()
        require(negative.count("error:") == 1 and "Type mismatch" in negative and
                "perturbation_ratio s word x y" in negative and "y ≠ x →" in negative,
                "missing-guard control failed for an unrelated reason")
        return {**previous, "contract": "contract-appendix-c-v1.1.json",
                "contract_sha256": sha(HERE / "contract-appendix-c-v1.1.json"),
                "appendix_map_sha256": sha(HERE / "appendix-map.json"),
                "appendix_native_certificates": 1, "appendix_native_negative_controls": 1,
                "appendix_lean_theorems": len(audits), "appendix_axioms": actual,
                "missing_ratio_guard": "Rejected by Lean with the expected missing-hypothesis type mismatch",
                "reference_steps": self.reference_budget.steps,
                "scope": "Universal finite-list expansion, perturbation, prefix and guarded-ratio proofs in Lean; one Adva symbolic induction-step certificate and wrong-order rejection. The old native regression is retained. No Adva induction kernel or formal ACS/RG/real-analysis result is claimed."}


def main():
    parser = argparse.ArgumentParser()
    for name in ("machine-root", "binary", "lean", "output"):
        parser.add_argument("--" + name, type=Path, required=True)
    args = parser.parse_args()
    for name in ("machine_root", "binary", "lean"):
        setattr(args, name, getattr(args, name).absolute())
    run = AppendixRun(args)
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
        require(result["status"] == "Passed", "Appendix C finite reception did not pass")


if __name__ == "__main__":
    main()
