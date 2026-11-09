"""Fixed-point normalization and finite affine-iteration receipts (CC0)."""

import hashlib
import json
from pathlib import Path
import re
import tarfile
import unittest
from unittest.mock import patch

import inventory

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]


def read(name):
    return json.loads((HERE / name).read_text())


class NormalizationBoundaryTests(unittest.TestCase):
    def test_normalization_and_pole_reading_are_exactly_audited_and_source_mapped(self):
        mapping = read("normalization-map.json")
        names = set()
        for module in mapping["modules"]:
            text = (HERE / module["file"]).read_text()
            declared = re.findall(r"^theorem (\w+)", text, re.M)
            self.assertEqual(declared, module["lean_audit_names"])
            self.assertEqual(declared, re.findall(r"^#print axioms " + re.escape(module["module"]) + r"\.(\w+)", text, re.M))
            self.assertEqual(set(declared), set(module["expected_axioms"]))
            self.assertFalse(re.search(r"^\s*(?:axiom|constant)\s|\b(?:sorry|admit|native_decide)\b", text, re.M))
            self.assertTrue(all(set(a) <= {"propext", "Classical.choice", "Quot.sound"}
                                for a in module["expected_axioms"].values()))
            names.update(module["module"] + "." + n for n in declared)
        self.assertEqual(len(names), 28)
        self.assertEqual(names, {n for row in mapping["mapping"] for n in row["formal"]})
        self.assertEqual(sum(len(m["lean_audit_names"]) for m in mapping["imports"]), 442)
        for row in mapping["mapping"]:
            source = (ROOT / row.get("source", mapping["source"])).read_text()
            for label in row["source_labels"]:
                self.assertIn("\\label{" + label + "}", source)
        live = inventory.generate()
        self.assertEqual(live, read("inventory.json"))
        self.assertEqual(len(live["claims"]), 102)
        self.assertEqual(sum(c["formal_status"] == "component-map-supplied" for c in live["claims"]), 35)
        self.assertTrue({"eq:p0-apollonius-pencil", "eq:p0-prefix-matrices", "eq:p0-affine-stabilizer", "eq:p0-projective-factorization", "eq:p0-bruhat", "eq:p0-affine-centered-form"} <= {e["label"] for e in live["equation_components"]})
        for label, prefix in [("rem:p0-ripple-normalization", "AEGPaper0.Chapter04Normalization."),
                              ("rem:p0-pole-bruhat", "AEGPaper0.Chapter04PoleReading.")]:
            claim = next(c for c in live["claims"] if label in c["labels"])
            self.assertTrue(any(n.startswith(prefix) for n in claim["lean_components"]))
        original = inventory.digest
        with patch.object(inventory, "digest", side_effect=lambda p:
                          "changed" if p == ROOT / mapping["source"] else original(p)):
            with self.assertRaisesRegex(ValueError, "reviewed formal correspondence has source drift"):
                inventory.generate()

    def test_old_proof_goals_library_receivers_and_numeric_bounds_remain_exact(self):
        old = read("evidence/cardinality-execution.json")
        with tarfile.open(HERE / "evidence" / old["archive"]["path"]) as stream:
            files = {m.name: stream.extractfile(m).read() for m in stream.getmembers() if m.name.startswith("sources/")}
        old_lock = json.loads(files["sources/machine.lock.json"])
        changed = {n for n in old_lock["formal_sources"] if files["sources/" + n] != (HERE / n).read_bytes()}
        self.assertEqual(changed, {"inventory.py", "inventory.json", "test_cardinality.py"})
        contract = read("contract-normalization.json")
        self.assertEqual(contract["bounds"], read("contract-cardinality.json")["bounds"])
        self.assertEqual(contract["expected_work"]["child_commands"], 23)
        self.assertEqual(len(contract["negative_controls"]), 4)
        for control in contract["negative_controls"]:
            self.assertTrue((HERE / control["file"]).is_file())
            self.assertGreaterEqual(len(control["expected_fragments"]), 2)

    def test_actual_derivatives_metric_scale_and_quotient_pole_are_explicit(self):
        norm = (HERE / "Chapter04Normalization.lean").read_text()
        pole = (HERE / "Chapter04PoleReading.lean").read_text()
        for name in ("normalize_hasFDerivAt", "normalize_fderiv", "metric_pullback", "tensor_pullback",
                     "normalized_metric_scale", "ripple_in_original_coordinates", "original_boundary_contact"):
            self.assertIn("theorem " + name, norm)
        for name in ("rightmost_translation_reads_pole", "rightmost_translation_unique",
                     "pole_invariant_under_affine_output", "same_pole_distinct_output"):
            self.assertIn("theorem " + name, pole)
        self.assertIn(" / lambda^2", norm)
        audit = read("normalization-map.json")["source_audit"][0]
        self.assertEqual(audit["status"], "partially proved as printed")
        self.assertIn("lambda^-2", audit["issue"])
        self.assertEqual(len(read("chapter03-obligations.json")["obligations"]), 6)


class NormalizationReceiptTests(unittest.TestCase):
    def test_twelve_profiles_current_sources_and_specific_rejections_are_archived(self):
        record = read("evidence/normalization-execution.json")
        self.assertEqual(record["status"], "Passed")
        archive = HERE / "evidence" / record["archive"]["path"]
        self.assertEqual(hashlib.sha256(archive.read_bytes()).hexdigest(), record["archive"]["sha256"])
        with tarfile.open(archive) as stream:
            members = stream.getmembers()
            self.assertEqual(len(members), record["archive"]["members"])
            self.assertLess(sum(m.size for m in members), 128 * 1024 * 1024)
            self.assertTrue(all(m.isfile() and not Path(m.name).is_absolute() and
                                ".." not in Path(m.name).parts for m in members))
            files = {m.name: stream.extractfile(m).read() for m in members}
        self.assertEqual(set(record["profiles"]), {"native", "analytic", "chapter04", "apollonius", "projective", "pgl", "affine_generation", "arithmetic", "bruhat", "fixed_points", "cardinality", "normalization"})
        for name, profile in record["profiles"].items():
            raw = files[profile["directory"] + "/result.json"]
            self.assertEqual(hashlib.sha256(raw).hexdigest(), profile["report_sha256"])
            result = json.loads(raw)
            self.assertEqual(result["status"], "Passed")
            self.assertEqual(result.get("source_lock_sha256", result.get("machine_lock_sha256")),
                             record["source_lock_sha256"])
            contract = read(profile["contract"])
            self.assertEqual(len(result["calls"]), contract["expected_work"]["child_commands"])
            self.assertLess(result["wall_seconds"], contract["bounds"]["wall_seconds"])
            if name == "normalization":
                self.assertEqual((result["import_lean_statements"], result["new_lean_statements"]), (442, 28))
                for module in read("normalization-map.json")["modules"]:
                    self.assertEqual(result["axioms"][module["module"]], module["expected_axioms"])
                for control in contract["negative_controls"]:
                    diagnostic = files[profile["directory"] + "/lean-negative-" + control["name"] + ".stdout"].decode()
                    self.assertEqual(diagnostic.count("error:"), 1)
                    self.assertIn("Type mismatch", diagnostic)
                    for fragment in control["expected_fragments"]:
                        self.assertIn(fragment, diagnostic)
            elif name == "native":
                self.assertEqual((len(result["rows"]), result["reference_steps"]), (69, 51137))
                for row in result["rows"]:
                    self.assertEqual(hashlib.sha256(files[profile["directory"] + "/" + row["name"] + ".run.adva"]).hexdigest(),
                                     row["report_sha256"])
        raw = files["sources/machine.lock.json"]
        self.assertEqual(hashlib.sha256(raw).hexdigest(), record["source_lock_sha256"])
        lock = json.loads(raw)
        self.assertEqual(lock, read("machine.lock.json"))
        for name, digest in lock["formal_sources"].items():
            self.assertEqual(hashlib.sha256(files["sources/" + name]).hexdigest(), digest)
            self.assertEqual(files["sources/" + name], (HERE / name).read_bytes())
        for name, digest in read("inventory.json")["sources"].items():
            self.assertEqual(hashlib.sha256(files["manuscript/" + name]).hexdigest(), digest)
        self.assertEqual(record["total_lean_statements"], 672)


if __name__ == "__main__":
    unittest.main()
