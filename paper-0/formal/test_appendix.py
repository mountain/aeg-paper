"""Check Appendix C's statement correspondence and finite receiving boundaries."""

import hashlib
import json
from pathlib import Path
import re
import tarfile
import unittest

import appendix_fixtures
from fixtures import polynomial
import inventory

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]


def read(name):
    return json.loads((HERE / name).read_text())


class AppendixTests(unittest.TestCase):
    def test_completed_induction_receipt_binds_exact_sources_controls_and_traces(self):
        record = read("evidence/appendix-c-execution.json")
        self.assertEqual(record["status"], "Passed")
        path = HERE / "evidence" / record["archive"]["path"]
        self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(), record["archive"]["sha256"])
        with tarfile.open(path) as stream:
            members = stream.getmembers()
            self.assertEqual(len(members), record["archive"]["members"])
            self.assertLess(sum(m.size for m in members), 32 * 1024 * 1024)
            self.assertTrue(all(m.isfile() and not Path(m.name).is_absolute() and ".." not in Path(m.name).parts for m in members))
            files = {m.name: stream.extractfile(m).read() for m in members}
        raw = files["run-02/result.json"]
        self.assertEqual(hashlib.sha256(raw).hexdigest(), record["report_sha256"])
        result = json.loads(raw)
        self.assertEqual(result["status"], "Passed")
        contract = json.loads(files["sources/" + result["contract"]])
        self.assertEqual(len(result["rows"]), contract["expected_work"]["native_calls"])
        self.assertEqual(len(result["calls"]), contract["expected_work"]["child_commands"])
        self.assertEqual(result["appendix_lean_theorems"], 24)
        self.assertEqual(result["appendix_axioms"], read("appendix-map.json")["expected_axioms"])
        self.assertIn("Type mismatch", files["run-02/lean-missing-ratio-guard.stdout"].decode())
        lock_raw = files["sources/machine.lock.json"]
        self.assertEqual(hashlib.sha256(lock_raw).hexdigest(), record["source_lock_sha256"])
        for name, digest in json.loads(lock_raw)["formal_sources"].items():
            self.assertEqual(hashlib.sha256(files["sources/" + name]).hexdigest(), digest)
            # The archive binds the inventory at execution time. Editorial
            # additions update live navigation without extending those proofs.
            # Proof sources still agree byte-for-byte with the frozen run.
            if name != "inventory.json":
                self.assertEqual(files["sources/" + name], (HERE / name).read_bytes())
        index = json.loads(files["sources/inventory.json"])
        for name, digest in index["sources"].items():
            self.assertEqual(hashlib.sha256(files["manuscript/" + name]).hexdigest(), digest)
        for row in result["rows"]:
            self.assertEqual(hashlib.sha256(files["run-02/" + row["name"] + ".run.adva"]).hexdigest(), row["report_sha256"])
        for call in result["calls"]:
            expected = 4294967296 if call["name"].startswith("lean") else 1073741824
            self.assertEqual(call["address_space_limit_bytes"], expected)

    def test_failed_exact_axiom_audit_is_retained_without_proof_or_budget_changes(self):
        record = read("evidence/appendix-c-attempt-1.json")
        self.assertEqual(record["status"], "Failed")
        self.assertFalse(record["whole_run_admitted"])
        self.assertFalse(record["missing_ratio_guard_control_reached"])
        path = HERE / "evidence" / record["archive"]["path"]
        self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(), record["archive"]["sha256"])
        with tarfile.open(path) as stream:
            members = stream.getmembers()
            self.assertTrue(all(m.isfile() and not Path(m.name).is_absolute() and ".." not in Path(m.name).parts for m in members))
            files = {m.name: stream.extractfile(m).read() for m in members}
        lock = json.loads(files["sources/machine.lock.json"])
        for name, digest in lock["formal_sources"].items():
            self.assertEqual(hashlib.sha256(files["sources/" + name]).hexdigest(), digest)
        old_map = json.loads(files["sources/appendix-map.json"])
        for name in ("scale_append", "scale_snoc"):
            self.assertEqual(old_map["expected_axioms"][name], [])
            old_map["expected_axioms"][name] = ["propext"]
        self.assertEqual(old_map, read("appendix-map.json"))
        for name in ("AppendixC.lean", "appendix-statement.json", "appendix-certificate.json", "checker.adva"):
            self.assertEqual(files["sources/" + name], (HERE / name).read_bytes())
        self.assertEqual(read("contract-appendix-c.json")["bounds"], read("contract-appendix-c-v1.1.json")["bounds"])

    def test_induction_mapping_has_exact_theorems_source_and_guard_boundary(self):
        mapping = read("appendix-map.json")
        source = ROOT / mapping["source"]
        self.assertEqual(hashlib.sha256(source.read_bytes()).hexdigest(), mapping["source_sha256"])
        lean = (HERE / "AppendixC.lean").read_text()
        actual = re.findall(r"^theorem (\w+)", lean, re.M)
        self.assertEqual(actual, mapping["lean_audit_names"])
        self.assertEqual(actual, re.findall(r"^#print axioms (\w+)", lean, re.M))
        self.assertEqual(set(actual), set(mapping["expected_axioms"]))
        self.assertFalse(re.search(r"^\s*(?:axiom|constant)\s|\b(?:sorry|admit|native_decide)\b", lean, re.M))
        covered = set()
        for row in mapping["mapping"]:
            covered.update(row["formal"])
            for label in row["source_labels"]:
                self.assertIn("\\label{" + label + "}", source.read_text())
            self.assertLessEqual(set(row["formal"]), set(actual))
            if "eq:appendix-alternating-acs-bridge" in row["source_labels"]:
                self.assertEqual(row["formal"], [])
        self.assertEqual(covered, set(actual))
        live = inventory.generate()
        self.assertEqual(live, read("inventory.json"))
        for label in ("def:appendix-alternating-expression", "prop:appendix-alternating-arithmetic-perturbation"):
            row = next(c for c in live["claims"] if label in c["labels"])
            self.assertEqual(row["formal_status"], "component-map-supplied")
        lock = read("machine.lock.json")["formal_sources"]
        for name in ("AppendixC.lean", "appendix_run.py", "appendix_fixtures.py", "appendix-map.json",
                     "appendix-statement.json", "appendix-certificate.json", "contract-appendix-c-v1.1.json",
                     "negative/MissingRatioGuard.lean"):
            self.assertIn(name, lock)

    def test_symbolic_step_and_wrong_order_remain_distinct_within_old_bounds(self):
        statement = read("appendix-statement.json")
        self.assertEqual(statement, appendix_fixtures.statement())
        certificate = read("appendix-certificate.json")
        self.assertEqual(certificate, appendix_fixtures.certificate())
        left, right = statement["goal"]["fields"]
        self.assertEqual(polynomial(left), polynomial(right))
        wrong_left, wrong_right = appendix_fixtures.wrong_goal()["fields"]
        self.assertNotEqual(polynomial(wrong_left), polynomial(wrong_right))
        previous, current = read("contract-v2.1.json"), read("contract-appendix-c-v1.1.json")
        self.assertEqual(previous["bounds"], current["bounds"])
        expected = current["expected_work"]
        self.assertEqual(expected["appendix_lean_theorems"], len(read("appendix-map.json")["lean_audit_names"]))
        self.assertLessEqual(expected["native_calls"], current["bounds"]["native_calls"])
        self.assertLessEqual(expected["child_commands"], current["bounds"]["child_commands"])
        self.assertLessEqual(len(certificate), current["bounds"]["proof_steps"])


if __name__ == "__main__":
    unittest.main()
