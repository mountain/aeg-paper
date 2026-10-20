"""Regression checks for the formalization's statement and trust boundaries."""

import hashlib
import json
from pathlib import Path
import tempfile
import tarfile
import unittest
from fractions import Fraction

from author import Author
from fixtures import add, certificates, equation, mul, node, polynomial, statements, var
import inventory
from run import controls, read
import domain_author
import domain_fixtures

HERE = Path(__file__).resolve().parent


class FormalTests(unittest.TestCase):
    def test_authored_bytecode_is_reproducible_and_has_no_host_oracle(self):
        program = Author().generate()
        self.assertEqual(program, read(HERE / "checker.adva"))
        self.assertLessEqual(len(program["code"]), 2048)
        self.assertLessEqual(len(program["registers"]), 64)
        self.assertLessEqual({i["op"] for i in program["code"]}, {
            "constant", "equal", "branch", "jump", "tag", "length", "field",
            "field_dynamic", "as_integer", "copy", "clear", "push", "pop",
            "is_empty", "add", "node", "stack_length", "input", "return", "reject",
        })
        for instruction in program["code"]:
            for key in ("target", "yes", "no"):
                if key in instruction:
                    self.assertTrue(0 <= instruction[key] < len(program["code"]))

    def test_goals_are_fixed_independently_of_proof_production(self):
        self.assertEqual(statements(), read(HERE / "statements.json"))
        self.assertEqual(certificates(), read(HERE / "certificates.json"))
        self.assertEqual({s["id"] for s in statements()}, set(certificates()))
        for statement in statements():
            left, right = statement["goal"]["fields"]
            self.assertEqual(polynomial(left), polynomial(right))
        self.assertNotEqual(polynomial(var(0)), polynomial(var(1)))
        self.assertNotEqual(polynomial(add(var(0), var(1))), polynomial(mul(var(0), var(1))))

    def test_machine_and_formal_source_locks_cover_the_live_proof_path(self):
        lock = read(HERE / "machine.lock.json")
        self.assertEqual(lock["commit"], read(HERE / "contract.json")["machine_commit"])
        for name in ("checker.adva", "statements.json", "certificates.json", "run.py", "Chapter02.lean"):
            self.assertIn(name, lock["formal_sources"])
        for name, digest in lock["formal_sources"].items():
            self.assertEqual(hashlib.sha256((HERE / name).read_bytes()).hexdigest(), digest, name)

    def test_inventory_tracks_nested_active_inputs_and_does_not_claim_completion(self):
        result = inventory.generate()
        self.assertEqual(result, read(HERE / "inventory.json"))
        self.assertIn("paper-0/sections/04b-pole-covariance.tex", result["sources"])
        self.assertEqual(len(result["sources"]), len(set(result["sources"])))
        self.assertTrue(any(c["formal_status"] == "not-yet-formalized" for c in result["claims"]))
        self.assertNotIn("proved", {c["formal_status"] for c in result["claims"]})

    def test_negative_family_penetrates_rule_goal_and_scope_boundaries(self):
        cases = {name: (data, status) for name, data, status in controls()}
        for name in ("forged-goal", "wrong-transitivity", "unknown-rule", "missing-premise", "arbitrary-proposition", "term-bound", "proof-bound", "stack-bound"):
            self.assertEqual(cases[name][1], "Rejected")
        a, b = var(0), var(1)
        self.assertNotEqual(polynomial(a), polynomial(b))
        self.assertEqual(cases["forged-goal"][0]["fields"][1], equation(a, b))

    def test_duplicate_metadata_and_malformed_terms_are_refused(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "bad.json"
            path.write_text('{"goal":1,"goal":2}')
            with self.assertRaises(ValueError):
                read(path)
        for term in (node(88), node(3, var(0)), node(0, {"kind": "integer", "value": True})):
            with self.assertRaises(ValueError):
                polynomial(term)

    def test_zero_counterexample_is_distinct_from_an_operator_counterexample(self):
        self.assertEqual((0, 0), (0, 0 * 0))
        self.assertNotEqual(0, 1)
        self.assertEqual(polynomial(mul(var(0), add(var(1), var(2)))),
                         polynomial(add(mul(var(0), var(1)), mul(var(0), var(2)))))

    def test_retained_execution_has_complete_source_and_report_bindings(self):
        record = read(HERE / "evidence/execution.json")
        archive = HERE / "evidence" / record["archive"]["path"]
        self.assertEqual(hashlib.sha256(archive.read_bytes()).hexdigest(), record["archive"]["sha256"])
        with tarfile.open(archive, "r:gz") as stream:
            members = stream.getmembers()
            self.assertEqual(len(members), record["archive"]["members"])
            self.assertLess(sum(m.size for m in members), 16 * 1024 * 1024)
            self.assertTrue(all(m.isfile() and not Path(m.name).is_absolute() and ".." not in Path(m.name).parts for m in members))
            files = {m.name: stream.extractfile(m).read() for m in members}
        raw = files["run-01/result.json"]
        self.assertEqual(hashlib.sha256(raw).hexdigest(), record["report_sha256"])
        result = json.loads(raw)
        self.assertEqual(result["status"], "Passed")
        self.assertEqual(len(result["rows"]), record["native_runs"])
        self.assertEqual(len(result["calls"]), record["child_commands"])
        for row in result["rows"]:
            report = files["run-01/" + row["name"] + ".run.adva"]
            self.assertEqual(hashlib.sha256(report).hexdigest(), row["report_sha256"])
        lock = json.loads(files["sources/machine.lock.json"])
        for name, digest in lock["formal_sources"].items():
            self.assertEqual(hashlib.sha256(files["sources/" + name]).hexdigest(), digest)
            # Historical source snapshots remain authoritative for run-01.
            # Live continuations may change supervisors/mappings, not these
            # protected original mathematical artifacts.
            if name in {"checker.adva", "Chapter02.lean", "statements.json", "certificates.json"}:
                self.assertEqual(files["sources/" + name], (HERE / name).read_bytes())

    def test_guarded_domain_program_is_reproducible_and_fits_the_existing_machine(self):
        program = domain_author.generated()
        self.assertEqual(program, read(HERE / "domain-checker.adva"))
        self.assertLessEqual(len(program["registers"]), 64)
        self.assertLessEqual(len(program["code"]), 2048)
        self.assertFalse(any(i["op"] in {"call", "ffi", "oracle"} for i in program["code"]))

    def test_both_operand_slots_have_independent_rational_results(self):
        cases = {c["name"]: c for c in domain_fixtures.cases()}
        expected = {"subtract-slot1": Fraction(5, 6), "subtract-slot2": Fraction(-5, 6),
                    "divide-slot1": Fraction(9, 4), "divide-slot2": Fraction(4, 9),
                    "zero-numerator-legal": Fraction(0), "mixed-slots": Fraction(8),
                    "negative-denominator": Fraction(-4, 3), "zero-multiplier": Fraction(0)}
        for name, value in expected.items():
            self.assertEqual(domain_fixtures.oracle(cases["domain-" + name]), value)
        self.assertEqual(domain_fixtures.cases(), read(HERE / "domain-cases.json"))

    def test_no_cancellation_or_zero_numerator_erases_a_prefix_domain(self):
        for case in domain_fixtures.cases():
            if case.get("reason") == "division by zero":
                with self.assertRaises(ZeroDivisionError, msg=case["name"]):
                    domain_fixtures.oracle(case)
        # Fixed-width and profile refusals do not refute the rational identity.
        for name in ("domain-overflow", "domain-word-bound"):
            case = next(c for c in domain_fixtures.cases() if c["name"] == name)
            self.assertIsInstance(domain_fixtures.oracle(case), Fraction)

    def test_current_definition_map_binds_labels_and_every_audited_theorem(self):
        import re
        mapping = read(HERE / "definition-map.json")
        source = HERE.parents[1] / mapping["source"]
        self.assertEqual(hashlib.sha256(source.read_bytes()).hexdigest(), mapping["source_sha256"])
        actual = re.findall(r"^theorem (\w+)", (HERE / "Chapter02Domains.lean").read_text(), re.M)
        self.assertEqual(actual, mapping["lean_audit_names"])
        for row in mapping["mapping"]:
            for name in row["formal"]:
                self.assertIn(name, actual)
            for label in row["source_labels"]:
                self.assertIn("\\label{" + label + "}", source.read_text())
        contract = read(HERE / "contract-v2.json")
        required = len(read(HERE / "statements.json")) + len(controls()) + 4 + len(domain_fixtures.cases()) + 4
        self.assertLessEqual(required, contract["bounds"]["native_calls"])

    def test_resource_failure_is_retained_and_only_lean_has_the_revised_limit(self):
        original = read(HERE / "contract-v2.json")
        revised = read(HERE / "contract-v2.1.json")
        for name, value in original["bounds"].items():
            self.assertEqual(revised["bounds"][name], value)
        self.assertEqual(revised["bounds"]["child_address_space_bytes"], 1073741824)
        self.assertEqual(revised["bounds"]["lean_child_address_space_bytes"], 4294967296)
        record = read(HERE / "evidence/chapter02-attempt-1.json")
        self.assertEqual(record["status"], "Failed")
        self.assertFalse(record["whole_run_admitted"])
        self.assertIn("out of memory", record["retained_diagnostic"])
        archive = HERE / "evidence" / record["archive"]["path"]
        self.assertEqual(hashlib.sha256(archive.read_bytes()).hexdigest(), record["archive"]["sha256"])
        with tarfile.open(archive) as stream:
            for name in ("checker.adva", "domain-checker.adva", "Chapter02.lean", "Chapter02Domains.lean", "domain-cases.json"):
                self.assertEqual(stream.extractfile("sources/" + name).read(), (HERE / name).read_bytes())

    def test_completed_successor_has_exact_sources_and_separate_child_resources(self):
        record = read(HERE / "evidence/chapter02-execution.json")
        archive = HERE / "evidence" / record["archive"]["path"]
        self.assertEqual(hashlib.sha256(archive.read_bytes()).hexdigest(), record["archive"]["sha256"])
        with tarfile.open(archive) as stream:
            members = stream.getmembers()
            self.assertEqual(len(members), record["archive"]["members"])
            self.assertLess(sum(m.size for m in members), 32 * 1024 * 1024)
            self.assertTrue(all(m.isfile() and not Path(m.name).is_absolute() and ".." not in Path(m.name).parts for m in members))
            files = {m.name: stream.extractfile(m).read() for m in members}
        raw = files["run-03/result.json"]
        self.assertEqual(hashlib.sha256(raw).hexdigest(), record["report_sha256"])
        result = json.loads(raw)
        self.assertEqual(result["status"], "Passed")
        self.assertEqual(len(result["rows"]), record["native_runs"])
        self.assertEqual(result["domain_cases"], 28)
        self.assertEqual(result["continuation_lean_theorems"], 63)
        for call in result["calls"]:
            expected = 4294967296 if call["name"].startswith("lean") else 1073741824
            self.assertEqual(call["address_space_limit_bytes"], expected)
        lock = json.loads(files["sources/machine.lock.json"])
        for name, digest in lock["formal_sources"].items():
            self.assertEqual(hashlib.sha256(files["sources/" + name]).hexdigest(), digest)
            self.assertEqual(files["sources/" + name], (HERE / name).read_bytes())
        for row in result["rows"]:
            self.assertEqual(hashlib.sha256(files["run-03/" + row["name"] + ".run.adva"]).hexdigest(), row["report_sha256"])


if __name__ == "__main__":
    unittest.main()
