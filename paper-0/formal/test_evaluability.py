"""Chapter 2 correspondence, guard and recorded-evidence boundaries (CC0)."""

from fractions import Fraction
import hashlib
import json
from pathlib import Path
import re
import tarfile
import unittest
from unittest.mock import patch

import domain_fixtures
import inventory

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]


def read(name):
    return json.loads((HERE / name).read_text())


class EvaluabilityBoundaryTests(unittest.TestCase):
    def test_map_has_exact_declarations_axioms_sources_and_coverage_boundaries(self):
        mapping = read("evaluability-map.json")
        lean = (HERE / "Chapter02Evaluability.lean").read_text()
        names = re.findall(r"^theorem (\w+)", lean, re.M)
        self.assertEqual(names, mapping["lean_audit_names"])
        self.assertEqual(names, re.findall(r"^#print axioms (\w+)", lean, re.M))
        self.assertEqual(set(names), set(mapping["expected_axioms"]))
        self.assertFalse(re.search(r"^\s*(?:axiom|constant)\s|\b(?:sorry|admit|native_decide)\b", lean, re.M))
        self.assertTrue(all(set(a) <= {"propext", "Classical.choice", "Quot.sound"}
                            for a in mapping["expected_axioms"].values()))
        sources = {mapping["source"]: mapping["source_sha256"], **mapping["additional_sources"]}
        for source, digest in sources.items():
            self.assertEqual(hashlib.sha256((ROOT / source).read_bytes()).hexdigest(), digest)
        attached = set()
        for row in mapping["mapping"]:
            source = ROOT / row.get("source", mapping["source"])
            for label in row["source_labels"]:
                self.assertIn("\\label{" + label + "}", source.read_text())
            attached.update(row["formal"])
        self.assertEqual(attached, set(names))
        self.assertIn("Richardson external undecidability theorem", mapping["excluded"])
        live = inventory.generate()
        self.assertEqual(live, read("inventory.json"))
        for label in ("def:p0-evaluable-expression", "ex:p0-cancelled-reciprocal-domain"):
            claim = next(c for c in live["claims"] if label in c["labels"])
            self.assertEqual(claim["formal_status"], "component-map-supplied")
        for claim in live["claims"]:
            # These claims remain outside both the Chapter 2 and the new
            # Chapter 3 coordinate continuation. Mapped coordinate components
            # elsewhere in Chapter 3 do not imply whole-chapter completion.
            if set(claim["labels"]) & {"rem:p0-length-two-coordinates", "ex:p0-e1-model"}:
                self.assertEqual(claim["formal_status"], "not-yet-formalized")

    def test_source_drift_in_either_reviewed_chapter_file_fails_closed(self):
        original = inventory.digest
        mapping = read("evaluability-map.json")
        for source in (mapping["source"], *mapping["additional_sources"]):
            with self.subTest(source=source), patch.object(
                    inventory, "digest", side_effect=lambda p: "changed" if p == ROOT / source else original(p)):
                with self.assertRaisesRegex(ValueError, "reviewed formal correspondence has source drift"):
                    inventory.generate()

    def test_cancelled_reciprocal_keeps_its_actual_guard_and_old_profile(self):
        cases = read("evaluability-cases.json")
        self.assertEqual(len(cases), 3)
        for case in cases:
            self.assertEqual(case["word"], [[3, 2, [1, 1]], [3, 2, [1, 1]]])
            if case["status"] == "Returned":
                self.assertEqual(domain_fixtures.oracle(case), Fraction(*case["initial"]))
            else:
                self.assertEqual(case["reason"], "division by zero")
                with self.assertRaises(ZeroDivisionError):
                    domain_fixtures.oracle(case)
        previous = read("contract-appendix-c-v1.1.json")
        current = read("contract-evaluability.json")
        old_bounds, new_bounds = previous["bounds"].copy(), current["bounds"].copy()
        self.assertEqual(old_bounds.pop("native_calls"), 64)
        self.assertEqual(new_bounds.pop("native_calls"), 72)
        self.assertEqual(old_bounds, new_bounds)
        self.assertEqual(current["expected_work"]["native_calls"], 63 + len(cases))
        self.assertEqual(current["expected_work"]["evaluability_lean_theorems"],
                         len(read("evaluability-map.json")["lean_audit_names"]))
        negative = (HERE / "negative/CancelledReciprocalTotal.lean").read_text()
        self.assertIn("exact (cancelled_reciprocal_domain s input).mpr", negative)
        self.assertNotIn("input ≠ s.zero", negative)


class EvaluabilityReceiptTests(unittest.TestCase):
    def test_completed_receipt_binds_snapshot_traces_audits_and_expected_guard_failure(self):
        record = read("evidence/evaluability-execution.json")
        self.assertEqual(record["status"], "Passed")
        archive = HERE / "evidence" / record["archive"]["path"]
        self.assertEqual(hashlib.sha256(archive.read_bytes()).hexdigest(), record["archive"]["sha256"])
        with tarfile.open(archive) as stream:
            members = stream.getmembers()
            self.assertEqual(len(members), record["archive"]["members"])
            self.assertLess(sum(m.size for m in members), 32 * 1024 * 1024)
            self.assertTrue(all(m.isfile() and not Path(m.name).is_absolute() and
                                ".." not in Path(m.name).parts for m in members))
            files = {m.name: stream.extractfile(m).read() for m in members}
        raw = files["run-01/result.json"]
        self.assertEqual(hashlib.sha256(raw).hexdigest(), record["report_sha256"])
        result = json.loads(raw)
        self.assertEqual(result["status"], "Passed")
        contract = json.loads(files["sources/contract-evaluability.json"])
        self.assertEqual(len(result["rows"]), contract["expected_work"]["native_calls"])
        self.assertEqual(len(result["calls"]), contract["expected_work"]["child_commands"])
        self.assertEqual(result["evaluability_axioms"], read("evaluability-map.json")["expected_axioms"])
        self.assertEqual(result["evaluability_lean_theorems"], 36)
        self.assertEqual(hashlib.sha256(files["sources/machine.lock.json"]).hexdigest(),
                         record["source_lock_sha256"])
        lock = json.loads(files["sources/machine.lock.json"])
        for name, digest in lock["formal_sources"].items():
            self.assertEqual(hashlib.sha256(files["sources/" + name]).hexdigest(), digest)
            # The next coordinate continuation extends live navigation and
            # this navigation/receipt regression. Frozen proofs and receivers
            # still match; every old file retains its archived digest above.
            if name not in {"inventory.json", "inventory.py", "test_evaluability.py"}:
                self.assertEqual(files["sources/" + name], (HERE / name).read_bytes())
        index = json.loads(files["sources/inventory.json"])
        for source, digest in index["sources"].items():
            self.assertEqual(hashlib.sha256(files["manuscript/" + source]).hexdigest(), digest)
        for row in result["rows"]:
            self.assertEqual(hashlib.sha256(files["run-01/" + row["name"] + ".run.adva"]).hexdigest(),
                             row["report_sha256"])
        for call in result["calls"]:
            self.assertEqual(call["address_space_limit_bytes"],
                             4294967296 if call["name"].startswith("lean") else 1073741824)
        negative = files["run-01/lean-cancelled-total.stdout"].decode()
        self.assertEqual(negative.count("error:"), 1)
        self.assertIn("input ≠ s.zero → Domain s (cancelledReciprocal s) input", negative)
        self.assertNotIn("sorryAx", files["run-01/lean-evaluability.stdout"].decode())


if __name__ == "__main__":
    unittest.main()
