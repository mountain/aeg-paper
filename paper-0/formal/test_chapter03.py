"""Chapter 3 source correspondence and algebra/geometry trust boundaries (CC0)."""

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


class Chapter03BoundaryTests(unittest.TestCase):
    def test_source_map_matches_exact_audits_and_keeps_unproved_geometry_explicit(self):
        mapping = read("chapter03-map.json")
        source = ROOT / mapping["source"]
        self.assertEqual(hashlib.sha256(source.read_bytes()).hexdigest(), mapping["source_sha256"])
        lean = (HERE / "Chapter03Coordinates.lean").read_text()
        names = re.findall(r"^theorem (\w+)", lean, re.M)
        self.assertEqual(names, mapping["lean_audit_names"])
        self.assertEqual(names, re.findall(r"^#print axioms (\w+)", lean, re.M))
        self.assertEqual(set(names), set(mapping["expected_axioms"]))
        self.assertEqual(len(names), 61)
        self.assertFalse(re.search(r"^\s*(?:axiom|constant)\s|\b(?:sorry|admit|native_decide)\b", lean, re.M))
        self.assertNotIn("import Mathlib", lean)
        attached = set()
        for row in mapping["mapping"]:
            for label in row["source_labels"]:
                self.assertIn("\\label{" + label + "}", source.read_text())
            attached.update(row["formal"])
        self.assertEqual(attached, set(names))
        for name in ("analytic differential and Jacobian identification", "Gaussian curvature and metric completeness",
                     "Laplace eigenfunction", "full regular-AES smooth manifold definition"):
            self.assertIn(name, mapping["excluded"])
        self.assertIn("candidate coordinate covector", lean)
        self.assertIn("(h : ∀ v, metric mu lambda p w v = assignmentCovector p v)", lean)
        self.assertIn("point_path_tree_bridge", names)
        live = inventory.generate()
        self.assertEqual(live, read("inventory.json"))
        for label in ("prop:canonical-arithmetic-frame", "prop:invariant-affine-metric",
                      "thm:basic-hyperbolic-aes", "prop:p0-grid-assignment-action", "ex:p0-four-step-path"):
            row = next(c for c in live["claims"] if label in c["labels"])
            self.assertEqual(row["formal_status"], "component-map-supplied")
        # The real-analysis successor now maps the smooth coordinate model,
        # Laplace and flow components separately. Length/trace and E1 remain
        # outside both continuations.
        for label in ("prop:p0-projective-trichotomy", "ex:p0-e1-model"):
            row = next(c for c in live["claims"] if label in c["labels"])
            self.assertEqual(row["formal_status"], "not-yet-formalized")

    def test_source_drift_is_rejected_and_both_guard_controls_are_specific(self):
        mapping = read("chapter03-map.json")
        original = inventory.digest
        with patch.object(inventory, "digest", side_effect=lambda p:
                          "changed" if p == ROOT / mapping["source"] else original(p)):
            with self.assertRaisesRegex(ValueError, "reviewed formal correspondence has source drift"):
                inventory.generate()
        height = (HERE / "negative/Chapter03MissingHeight.lean").read_text()
        orientation = (HERE / "negative/Chapter03MissingOrientation.lean").read_text()
        self.assertIn("exact translation_assignment s p", height)
        self.assertNotIn("p.2 ≠ 0", height)
        self.assertIn("hq f hf hu hv", orientation)
        self.assertNotIn("det f.u f.v = 1", orientation)
        self.assertEqual(read("contract-evaluability.json")["bounds"], read("contract-chapter03.json")["bounds"])

    def test_scalar_cases_use_independent_values_and_distinguish_composition_order(self):
        cases = read("chapter03-cases.json")
        self.assertEqual(len(cases), 3)
        values = []
        for case in cases:
            value = domain_fixtures.oracle(case)
            self.assertEqual(value, Fraction(*case["expected"]))
            values.append(value)
        self.assertEqual(values, [Fraction(3), Fraction(4), Fraction(20)])
        self.assertNotEqual(values[1], values[2])
        self.assertEqual(read("contract-chapter03.json")["expected_work"]["native_calls"], 66 + len(cases))


class Chapter03ReceiptTests(unittest.TestCase):
    def test_completed_receipt_binds_current_sources_replays_audits_and_negative_controls(self):
        record = read("evidence/chapter03-execution.json")
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
        expected = read("contract-chapter03.json")["expected_work"]
        self.assertEqual(len(result["rows"]), expected["native_calls"])
        self.assertEqual(len(result["calls"]), expected["child_commands"])
        self.assertEqual(result["chapter03_lean_theorems"], 61)
        self.assertEqual(result["chapter03_axioms"], read("chapter03-map.json")["expected_axioms"])
        lock_raw = files["sources/machine.lock.json"]
        self.assertEqual(hashlib.sha256(lock_raw).hexdigest(), record["source_lock_sha256"])
        lock = json.loads(lock_raw)
        for name, digest in lock["formal_sources"].items():
            self.assertEqual(hashlib.sha256(files["sources/" + name]).hexdigest(), digest)
            # Keep original execution sources exact; live navigation and this
            # navigation/receipt regression have separately pinned successors.
            if name not in {"inventory.json", "inventory.py", "test_chapter03.py"}:
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
        for control, phrase in (("height", "p.snd ≠ 0 →"), ("orientation", "OrthonormalOriented f")):
            output = files["run-01/lean-chapter03-missing-" + control + ".stdout"].decode()
            self.assertEqual(output.count("error:"), 1)
            self.assertIn(phrase, output)
        self.assertNotIn("sorryAx", files["run-01/lean-chapter03.stdout"].decode())


if __name__ == "__main__":
    unittest.main()
