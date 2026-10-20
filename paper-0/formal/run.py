"""Check fixed AEG statements using Adva, native replay, and independent oracles.

The host supplies no proof-checking callback to Adva. Original CC0 code by
Codex (OpenAI); local execution evidence is not independent human review.
"""

import argparse
from copy import deepcopy
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import resource
import subprocess
import time

import blake3

from fixtures import add, equation, input_data, integer, mul, node, polynomial, var
import domain_fixtures
import inventory

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]


def read(path):
    def pairs(items):
        result = {}
        for key, value in items:
            if key in result:
                raise ValueError("duplicate JSON key")
            result[key] = value
        return result
    return json.loads(path.read_text(), object_pairs_hook=pairs)


def save(path, obj):
    with path.open("x") as stream:
        json.dump(obj, stream, indent=2, allow_nan=False)
        stream.write("\n")


def require(condition, reason):
    if not condition:
        raise ValueError(reason)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def controls():
    a, b, c = var(0), var(1), var(2)
    cases = [
        ("reflexivity", [node(0, a)], equation(a, a), "Returned"),
        ("symmetry", [node(11, a, b), node(1)], equation(add(b, a), add(a, b)), "Returned"),
        ("add-zero", [node(12, a)], equation(add(a, node(1)), a), "Returned"),
        ("mul-one", [node(15, a)], equation(mul(a, node(2)), a), "Returned"),
        ("mul-zero", [node(17, a)], equation(mul(a, node(1)), node(1)), "Returned"),
        ("mul-congruence", [node(11, a, b), node(0, c), node(4)], equation(mul(add(a, b), c), mul(add(b, a), c)), "Returned"),
        ("forged-goal", [node(0, a)], equation(a, b), "Rejected"),
        ("wrong-transitivity", [node(0, a), node(0, b), node(2)], equation(a, b), "Rejected"),
        ("unknown-rule", [node(99, a)], equation(a, a), "Rejected"),
        ("missing-premise", [node(1)], equation(a, a), "Rejected"),
        ("leftover-premise", [node(0, a), node(0, a)], equation(a, a), "Rejected"),
        ("wrong-rule-arity", [node(16, a, b)], equation(a, a), "Rejected"),
        ("arbitrary-proposition", [node(200, a)], equation(a, b), "Rejected"),
        ("unknown-variable", [node(0, var(8))], equation(a, a), "Rejected"),
        ("noninteger-variable", [node(0, node(0, node(1)))], equation(a, a), "Rejected"),
        ("unknown-term", [node(0, node(88))], equation(a, a), "Rejected"),
        ("wrong-term-arity", [node(0, node(3, a))], equation(a, a), "Rejected"),
        ("stack-bound", [node(0, a)] * 33, equation(a, a), "Rejected"),
        ("proof-bound", [node(0, a)] * 65, equation(a, a), "Rejected"),
    ]
    big = a
    for _ in range(32):
        big = add(big, a)
    cases.append(("term-bound", [node(0, big)], equation(a, a), "Rejected"))
    return [(name, input_data(proof, goal), status) for name, proof, goal, status in cases]


class Run:
    def __init__(self, args):
        self.output = args.output.resolve()
        self.output.mkdir(parents=True, exist_ok=False)
        self.args = args
        self.contract = read(HERE / "contract-v2.1.json")
        self.bounds = self.contract["bounds"]
        self.started = time.monotonic()
        self.calls, self.rows = [], []
        self.program = read(HERE / "checker.adva")
        self.reference = None
        self.reference_budget = None

    def preflight(self):
        lock = read(HERE / "machine.lock.json")
        root = self.args.machine_root.resolve()
        head = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=root, text=True).strip()
        require(head == lock["commit"], "machine checkout revision mismatch")
        for relative, digest in lock["sources"].items():
            require(sha(root / relative) == digest, "machine source drift: " + relative)
        for relative, digest in lock["formal_sources"].items():
            require(sha(HERE / relative) == digest, "formal source drift: " + relative)
        require(read(HERE / "inventory.json") == inventory.generate(), "manuscript/coverage inventory drift")
        spec = importlib.util.spec_from_file_location("aeg_v1_reference", root / "experiments/bounded_self_compiler/reference.py")
        self.reference = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.reference)
        supervisor = self

        class BoundedBudget(self.reference.Budget):
            def tick(self):
                super().tick()
                if self.steps % 128 == 0:
                    require(time.monotonic() - supervisor.started < supervisor.bounds["wall_seconds"],
                            "independent receiving deadline exhausted")

        self.reference_budget = BoundedBudget(self.bounds["reference_steps"])
        digest = blake3.blake3(b"adva.data-machine.transition.v1\0")
        digest.update((root / "crates/adva-witness/src/data_machine_v1.rs").read_bytes())
        digest.update((root / "Cargo.lock").read_bytes())
        self.profile = digest.hexdigest()
        return {"machine_commit": head, "machine_profile": self.profile,
                "native_binary_sha256": sha(self.args.binary),
                "machine_lock_sha256": sha(HERE / "machine.lock.json")}

    def limits(self, lean=False):
        resource.setrlimit(resource.RLIMIT_CPU, (self.bounds["child_cpu_seconds"],) * 2)
        address_space = self.bounds["lean_child_address_space_bytes"] if lean else self.bounds["child_address_space_bytes"]
        resource.setrlimit(resource.RLIMIT_AS, (address_space,) * 2)
        resource.setrlimit(resource.RLIMIT_FSIZE, (self.bounds["child_file_bytes"],) * 2)

    def command(self, name, argv, codes=(0,), *, lean=False):
        remaining = self.bounds["wall_seconds"] - (time.monotonic() - self.started)
        require(remaining > 0, "shared deadline exhausted")
        require(len(self.calls) < self.bounds["child_commands"], "child command bound")
        used = sum(p.stat().st_size for p in self.output.rglob("*") if p.is_file())
        require(used + 3 * self.bounds["child_file_bytes"] + 1048576 <= self.bounds["artifact_bytes"], "artifact capacity")
        row = {"name": name, "argv": [str(x) for x in argv],
               "address_space_limit_bytes": self.bounds["lean_child_address_space_bytes"] if lean else self.bounds["child_address_space_bytes"]}
        self.calls.append(row)
        with (self.output / (name + ".stdout")).open("xb") as out, (self.output / (name + ".stderr")).open("xb") as err:
            result = subprocess.run(row["argv"], stdout=out, stderr=err,
                                    timeout=min(remaining, self.bounds["child_wall_seconds"]),
                                    preexec_fn=lambda: self.limits(lean), check=False)
        row["returncode"] = result.returncode
        require(result.returncode in codes, name + " failed; inspect retained diagnostics")
        return result.returncode

    def native(self, name, data, expected, *, fuel=200000, quantum=200000, resume=None,
               program_name="checker.adva"):
        require(len(self.rows) < self.bounds["native_calls"], "native call bound")
        ip, report_path = self.output / (name + ".input.json"), self.output / (name + ".run.adva")
        save(ip, data)
        require(program_name in ("checker.adva", "domain-checker.adva"), "unknown program profile")
        program = HERE / program_name
        program_object = self.program if program_name == "checker.adva" else read(program)
        command = [self.args.binary, "data-run-v1", program, "--input", ip,
                   "--fuel", str(fuel), "--quantum", str(quantum), "--output", report_path]
        if resume is not None:
            command += ["--resume", resume]
        self.command(name, command, codes=(0, 2))
        report = read(report_path)
        require(report["status"] == expected, name + ": unexpected outcome " + report["status"])
        state = self.reference.receive(report, program_object, data, fuel, self.profile, self.reference_budget)
        receipt_path = self.output / (name + ".receipt.adva")
        self.command(name + "-replay", [self.args.binary, "data-run-v1", program, "--input", ip,
                                      "--fuel", str(fuel), "--quantum", "0", "--check", report_path,
                                      "--output", receipt_path])
        receipt = read(receipt_path)
        require(receipt["state"] == state and receipt["verified_steps"] == state["spent"], "native replay mismatch")
        if expected == "Returned" and program_name == "checker.adva":
            require(report["state"]["phase"]["value"] == data["fields"][1], "returned equation differs from independent goal")
        self.rows.append({"name": name, "program": program_name, "status": report["status"], "phase": report["state"]["phase"],
                          "steps": state["spent"], "report_sha256": sha(report_path)})
        return report, report_path

    def domains(self):
        from fractions import Fraction
        cases = read(HERE / "domain-cases.json")
        require(cases == domain_fixtures.cases(), "domain fixture drift")
        for case in cases:
            mathematical = None
            error = None
            try:
                mathematical = domain_fixtures.oracle(case)
            except (ValueError, ZeroDivisionError) as exception:
                error = type(exception).__name__
            report, _ = self.native(case["name"], domain_fixtures.encode(case), case["status"],
                                    program_name="domain-checker.adva")
            phase = report["state"]["phase"]
            if case["status"] == "Returned":
                value = phase["value"]
                require(value["kind"] == "node" and value["tag"] == 31 and len(value["fields"]) == 2,
                        "invalid rational result shape")
                numerator, denominator = value["fields"]
                require(numerator["kind"] == denominator["kind"] == "integer", "noninteger rational result")
                require(denominator["value"] != 0, "returned zero rational denominator")
                require(mathematical is not None and Fraction(numerator["value"], denominator["value"]) == mathematical,
                        case["name"] + ": independent rational oracle differs")
            else:
                require(phase["reason"] == case["reason"], case["name"] + ": refusal reason differs")
                if case["reason"] in ("integer overflow", "comb length bound"):
                    require(mathematical is not None, "resource refusal was confused with an undefined arithmetic expression")
                else:
                    require(error is not None, "native domain refusal disagrees with independent mathematics")
            self.rows[-1]["rational_oracle"] = {"value": str(mathematical) if mathematical is not None else None,
                                                "error": error}
        sample = next(c for c in cases if c["name"] == "domain-mixed-slots")
        data = domain_fixtures.encode(sample)
        _, path = self.native("domain-prefix", data, "Suspended", quantum=17, program_name="domain-checker.adva")
        resumed, _ = self.native("domain-resumed", data, "Returned", resume=path, program_name="domain-checker.adva")
        whole = read(self.output / "domain-mixed-slots.run.adva")
        require(resumed["state"] == whole["state"] and resumed["trace"] == whole["trace"], "domain continuation changed execution")
        exhausted, path = self.native("domain-exhausted", data, "FuelExhausted", fuel=17, quantum=17,
                                      program_name="domain-checker.adva")
        again, _ = self.native("domain-still-exhausted", data, "FuelExhausted", fuel=17, quantum=17, resume=path,
                               program_name="domain-checker.adva")
        require(again["trace"] == exhausted["trace"], "domain continuation refilled fuel")
        first = read(self.output / "domain-unit-marked-first.run.adva")
        second = read(self.output / "domain-unit-marked-second.run.adva")
        require(first["state"]["phase"]["value"] == second["state"]["phase"]["value"], "unit words should agree in value")
        require(first["input"] != second["input"] and first["trace"] != second["trace"], "marked words were identified")
        return len(cases)

    def execute(self):
        provenance = self.preflight()
        statements = read(HERE / "statements.json")
        certificates = read(HERE / "certificates.json")
        require(set(certificates) == {s["id"] for s in statements}, "certificate/statement IDs differ")
        for statement in statements:
            left, right = statement["goal"]["fields"]
            require(polynomial(left) == polynomial(right), "independent polynomial oracle disagrees")
            self.native(statement["id"], input_data(certificates[statement["id"]], statement["goal"]), "Returned")
        for name, data, status in controls():
            self.native(name, data, status)
        # A valid rule may consume fuel without completing a proof. It is not false.
        sample = statements[-1]
        data = input_data(certificates[sample["id"]], sample["goal"])
        _, path = self.native("prefix", data, "Suspended", quantum=17)
        resumed, _ = self.native("resumed", data, "Returned", resume=path)
        whole = read(self.output / (sample["id"] + ".run.adva"))
        require(resumed["state"] == whole["state"] and resumed["trace"] == whole["trace"], "resume changed the derivation")
        exhausted, path = self.native("exhausted", data, "FuelExhausted", fuel=17, quantum=17)
        again, _ = self.native("still-exhausted", data, "FuelExhausted", fuel=17, quantum=17, resume=path)
        require(again["trace"] == exhausted["trace"], "continuation refilled fuel")
        domain_count = self.domains()
        self.command("lean-version", [self.args.lean, "--version"], lean=True)
        version = (self.output / "lean-version.stdout").read_text().strip()
        require("version 4.24.0," in version, "Lean release mismatch")
        self.command("lean", [self.args.lean, "-j1", "-o", self.output / "Chapter02.olean", HERE / "Chapter02.lean"], lean=True)
        log = (self.output / "lean.stdout").read_text()
        errors = (self.output / "lean.stderr").read_text()
        require("sorryAx" not in log + errors and "warning:" not in log + errors and "error:" not in log + errors, "unclean Lean verification")
        for statement in statements:
            require(f"'AEGPaper0.{statement['lean']}' does not depend on any axioms" in log,
                    "missing/unclean Lean audit for " + statement["id"])
        require("'AEGPaper0.comb_order_unique' depends on axioms: [propext]" in log,
                "comb-order axiom audit changed")
        expected = {s["lean"] for s in statements} | {"comb_opposition", "comb_order_unique", "zero_pair_counterexample"}
        audited = re.findall(r"'AEGPaper0\.(\w+)' (?:does not depend on any axioms|depends on axioms: \[[^\]]*\])", log)
        require(len(audited) == len(expected) and set(audited) == expected, "Lean audit labels differ")
        for name in expected - {"comb_order_unique"}:
            require(f"'AEGPaper0.{name}' does not depend on any axioms" in log, "unexpected Lean axioms")
        self.command("lean-domains", ["/usr/bin/env", "LEAN_PATH=" + str(self.output), self.args.lean,
                                      "-j1", HERE / "Chapter02Domains.lean"], lean=True)
        continuation = (self.output / "lean-domains.stdout").read_text()
        diagnostics = continuation + (self.output / "lean-domains.stderr").read_text()
        require(not re.search(r"\b(?:warning|error):", diagnostics, re.I), "unclean continuation proof")
        audits = re.findall(r"'AEGPaper0\.Chapter02\.(\w+)' (?:does not depend on any axioms|depends on axioms: \[([^\]]*)\])", continuation)
        definition_map = read(HERE / "definition-map.json")
        require(len(audits) == len(definition_map["lean_audit_names"]) and
                {name for name, _ in audits} == set(definition_map["lean_audit_names"]), "continuation audit labels differ")
        for name, raw in audits:
            axioms = {x.strip() for x in raw.split(",") if x.strip()}
            require(axioms <= {"propext", "Classical.choice", "Quot.sound"}, "unexpected continuation axiom: " + name)
        return {**provenance, "named_derivations": len(statements), "control_cases": len(controls()),
                "domain_cases": domain_count, "continuation_lean_theorems": len(audits),
                "continuation_axioms": {name: [x.strip() for x in raw.split(",") if x.strip()] for name, raw in audits},
                "reference_steps": self.reference_budget.steps,
                "lean_sha256": sha(self.args.lean.resolve()),
                "lean_version": (self.output / "lean-version.stdout").read_text().strip(),
                "scope": "Five unchanged Adva equational certificates; separate guarded rational finite cases; universal Lean syntax/domain/field/equality statements. No general Adva field-proof kernel, formal PGL quotient or full checker-soundness theorem is claimed.",
                "counterexample": {"source_label": "prop:p0-distributive-operator-identity",
                                   "p": 0, "k": 0, "pairs_equal": [0, 0] == [0, 0 * 0],
                                   "status": "retained historical counterexample; manuscript now distinguishes marked words and scalar projections and includes both zero and unit cases"}}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--machine-root", type=Path, required=True)
    parser.add_argument("--binary", type=Path, required=True)
    parser.add_argument("--lean", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    for name in ("machine_root", "binary", "lean"):
        setattr(args, name, getattr(args, name).absolute())
    run = Run(args)
    result = {"status": "Failed", "calls": run.calls, "rows": run.rows}
    try:
        result.update(run.execute())
        result["status"] = "Passed"
    except Exception as error:
        result["error"] = f"{type(error).__name__}: {error}"
        raise
    finally:
        result["wall_seconds"] = time.monotonic() - run.started
        # Reserve and check before publishing a self-reported success.
        if result["wall_seconds"] > run.bounds["wall_seconds"]:
            result["status"] = "Failed"
            result["error"] = "shared deadline exhausted"
        used = sum(p.stat().st_size for p in run.output.rglob("*") if p.is_file())
        if used + 1048576 > run.bounds["artifact_bytes"]:
            result["status"] = "Failed"
            result["error"] = "final artifact capacity exhausted"
        save(run.output / "result.json", result)
        require(result["status"] == "Passed", "finite run did not pass")


if __name__ == "__main__":
    main()
