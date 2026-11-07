"""Affine stabilizer and quotient-generation scope, guards and receipts (CC0)."""

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


class AffineGenerationBoundaryTests(unittest.TestCase):
    def test_standard_affine_and_actual_quotient_generation_are_exactly_audited_and_mapped(self):
        mapping = read("affine-generation-map.json")
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
        self.assertEqual(len(names), 39)
        self.assertEqual(names, {n for row in mapping["mapping"] for n in row["formal"]})
        self.assertEqual(sum(len(m["lean_audit_names"]) for m in mapping["imports"]), 120)
        source = (ROOT / mapping["source"]).read_text()
        for row in mapping["mapping"]:
            for label in row["source_labels"]:
                self.assertIn("\\label{" + label + "}", source)
        live = inventory.generate()
        self.assertEqual(live, read("inventory.json"))
        self.assertEqual(len(live["claims"]), 102)
        self.assertEqual(sum(c["formal_status"] == "component-map-supplied" for c in live["claims"]), 32)
        self.assertTrue({"eq:p0-apollonius-pencil", "eq:p0-prefix-matrices", "eq:p0-affine-stabilizer", "eq:p0-projective-factorization"} <= {e["label"] for e in live["equation_components"]})
        equation = next(e for e in live["equation_components"] if e["label"] == "eq:p0-affine-stabilizer")
        self.assertTrue(any(n.startswith("AEGPaper0.AffineStabilizer.") for n in equation["lean_components"]))
        original = inventory.digest
        with patch.object(inventory, "digest", side_effect=lambda p:
                          "changed" if p == ROOT / mapping["source"] else original(p)):
            with self.assertRaisesRegex(ValueError, "reviewed formal correspondence has source drift"):
                inventory.generate()

    def test_old_proof_goals_library_receivers_and_numeric_bounds_remain_exact(self):
        old = read("evidence/pgl-execution.json")
        with tarfile.open(HERE / "evidence" / old["archive"]["path"]) as stream:
            files = {m.name: stream.extractfile(m).read() for m in stream.getmembers() if m.name.startswith("sources/")}
        old_lock = json.loads(files["sources/machine.lock.json"])
        changed = {n for n in old_lock["formal_sources"] if files["sources/" + n] != (HERE / n).read_bytes()}
        self.assertEqual(changed, {"inventory.py", "inventory.json", "test_pgl.py", "test_projective.py"})
        contract = read("contract-affine-generation.json")
        self.assertEqual(contract["bounds"], read("contract-pgl.json")["bounds"])
        self.assertEqual(contract["expected_work"]["child_commands"], 13)
        self.assertEqual(len(contract["negative_controls"]), 4)
        for control in contract["negative_controls"]:
            self.assertTrue((HERE / control["file"]).is_file())
            self.assertGreaterEqual(len(control["expected_fragments"]), 2)

    def test_interfaces_normal_forms_order_and_proper_generator_family_are_explicit(self):
        affine = (HERE / "AffineStabilizer.lean").read_text()
        self.assertIn("K ≃ᵃ[K] K", affine)
        self.assertIn("def infinityStabilizer : Subgroup (PGL2 K)", affine)
        self.assertIn("def affineStabilizerEquiv : Aff K ≃*", affine)
        self.assertIn("MulEquiv.ofBijective", affine)
        for name in ("normalized_class_unique", "normalizedAffine_inverse_apply", "affine_parameter_composition",
                     "zero_slope_impossible", "inversion_not_in_affine_stabilizer", "affine_composition_order_matters"):
            self.assertIn("theorem " + name, affine)
        generation = (HERE / "ProjectiveGeneration.lean").read_text()
        for name in ("quotient_affine_factorization", "quotient_nonaffine_factorization", "elementary_generators_generate"):
            self.assertIn("theorem " + name, generation)
        self.assertIn("Subgroup.closure (elementaryGenerators (K := K)) = ⊤", generation)
        self.assertIn("dilationClass (u : Kˣ)", generation)
        self.assertIn("Arithmetic grammar/history evaluation dictionary into the generated quotient group",
                      read("affine-generation-map.json")["excluded"])
        self.assertEqual(len(read("chapter03-obligations.json")["obligations"]), 6)


class AffineGenerationReceiptTests(unittest.TestCase):
    def test_seven_profiles_current_sources_and_specific_rejections_are_archived(self):
        record = read("evidence/affine-generation-execution.json")
        self.assertEqual(record["status"], "Passed")
        archive = HERE / "evidence" / record["archive"]["path"]
        self.assertEqual(hashlib.sha256(archive.read_bytes()).hexdigest(), record["archive"]["sha256"])
        with tarfile.open(archive) as stream:
            members = stream.getmembers()
            self.assertEqual(len(members), record["archive"]["members"])
            self.assertLess(sum(m.size for m in members), 64 * 1024 * 1024)
            self.assertTrue(all(m.isfile() and not Path(m.name).is_absolute() and
                                ".." not in Path(m.name).parts for m in members))
            files = {m.name: stream.extractfile(m).read() for m in members}
        self.assertEqual(set(record["profiles"]), {"native", "analytic", "chapter04", "apollonius", "projective", "pgl", "affine_generation"})
        for name, profile in record["profiles"].items():
            raw = files[profile["directory"] + "/result.json"]
            self.assertEqual(hashlib.sha256(raw).hexdigest(), profile["report_sha256"])
            result = json.loads(raw)
            self.assertEqual(result["status"], "Passed")
            contract = read(profile["contract"])
            self.assertEqual(len(result["calls"]), contract["expected_work"]["child_commands"])
            self.assertLess(result["wall_seconds"], contract["bounds"]["wall_seconds"])
            if name == "affine_generation":
                self.assertEqual((result["import_lean_statements"], result["new_lean_statements"]), (120, 39))
                for module in read("affine-generation-map.json")["modules"]:
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
        self.assertEqual(len(json.loads(files["sources/inventory.json"])["equation_components"]), 4)
        raw = files["sources/machine.lock.json"]
        self.assertEqual(hashlib.sha256(raw).hexdigest(), record["source_lock_sha256"])
        lock = json.loads(raw)
        for name, digest in lock["formal_sources"].items():
            self.assertEqual(hashlib.sha256(files["sources/" + name]).hexdigest(), digest)
            # Current arithmetic continuation separately pins these successors.
            if name not in {"inventory.py", "inventory.json", "test_affine_generation.py", "test_pgl.py", "test_projective.py"}:
                self.assertEqual(files["sources/" + name], (HERE / name).read_bytes())
        for name, digest in read("inventory.json")["sources"].items():
            self.assertEqual(hashlib.sha256(files["manuscript/" + name]).hexdigest(), digest)
        self.assertEqual(record["total_lean_statements"], 504)


if __name__ == "__main__":
    unittest.main()
