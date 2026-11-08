"""Arithmetic grammar, ordinary domains and projective-group receipts (CC0)."""

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


class ArithmeticBoundaryTests(unittest.TestCase):
    def test_arithmetic_dictionary_is_exactly_audited_and_source_mapped(self):
        mapping = read("arithmetic-map.json")
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
        self.assertEqual(len(names), 35)
        self.assertEqual(names, {n for row in mapping["mapping"] for n in row["formal"]})
        self.assertEqual(sum(len(m["lean_audit_names"]) for m in mapping["imports"]), 230)
        source = (ROOT / mapping["source"]).read_text()
        for row in mapping["mapping"]:
            for label in row["source_labels"]:
                self.assertIn("\\label{" + label + "}", source)
        live = inventory.generate()
        self.assertEqual(live, read("inventory.json"))
        self.assertEqual(len(live["claims"]), 102)
        self.assertGreaterEqual(sum(c["formal_status"] == "component-map-supplied" for c in live["claims"]), 32)
        self.assertTrue({"eq:p0-apollonius-pencil", "eq:p0-prefix-matrices", "eq:p0-affine-stabilizer", "eq:p0-projective-factorization"} <= {e["label"] for e in live["equation_components"]})
        equation = next(e for e in live["equation_components"] if e["label"] == "eq:p0-affine-stabilizer")
        self.assertTrue(any(n.startswith("AEGPaper0.ProjectiveArithmetic.") for n in equation["lean_components"]))
        original = inventory.digest
        with patch.object(inventory, "digest", side_effect=lambda p:
                          "changed" if p == ROOT / mapping["source"] else original(p)):
            with self.assertRaisesRegex(ValueError, "reviewed formal correspondence has source drift"):
                inventory.generate()

    def test_old_proof_goals_library_receivers_and_numeric_bounds_remain_exact(self):
        old = read("evidence/affine-generation-execution.json")
        with tarfile.open(HERE / "evidence" / old["archive"]["path"]) as stream:
            files = {m.name: stream.extractfile(m).read() for m in stream.getmembers() if m.name.startswith("sources/")}
        old_lock = json.loads(files["sources/machine.lock.json"])
        changed = {n for n in old_lock["formal_sources"] if files["sources/" + n] != (HERE / n).read_bytes()}
        self.assertEqual(changed, {'test_pgl.py', 'inventory.py', 'inventory.json', 'test_projective.py', 'test_affine_generation.py', 'test_apollonius.py'})
        contract = read("contract-arithmetic.json")
        self.assertEqual(contract["bounds"], read("contract-affine-generation.json")["bounds"])
        self.assertEqual(contract["expected_work"]["child_commands"], 16)
        self.assertEqual(len(contract["negative_controls"]), 4)
        for control in contract["negative_controls"]:
            self.assertTrue((HERE / control["file"]).is_file())
            self.assertGreaterEqual(len(control["expected_fragments"]), 2)

    def test_existing_syntax_domains_chronology_and_pure_slot_images_are_explicit(self):
        text = (HERE / "ProjectiveArithmetic.lean").read_text()
        self.assertIn("import Chapter02Domains", text)
        self.assertIn("def fieldData : FieldData K", text)
        self.assertIn("word.length ≤ 4", text)
        for name in ("section_nondegenerate_iff", "wordClass_append", "ordinary_iff_safe",
                     "left_tree_projective_match", "right_tree_projective_match",
                     "safe_iff_run_finite", "first_word_image_is_stabilizer",
                     "second_word_surjective", "group_equality_does_not_determine_domain",
                     "reciprocal_word_syntax_distinct", "zero_multiplication_ordinary"):
            self.assertIn("theorem " + name, text)
        self.assertEqual(len(read("chapter03-obligations.json")["obligations"]), 6)


class ArithmeticReceiptTests(unittest.TestCase):
    def test_eight_profiles_current_sources_and_specific_rejections_are_archived(self):
        record = read("evidence/arithmetic-execution.json")
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
        self.assertEqual(set(record["profiles"]), {"native", "analytic", "chapter04", "apollonius", "projective", "pgl", "affine_generation", "arithmetic"})
        for name, profile in record["profiles"].items():
            raw = files[profile["directory"] + "/result.json"]
            self.assertEqual(hashlib.sha256(raw).hexdigest(), profile["report_sha256"])
            result = json.loads(raw)
            self.assertEqual(result["status"], "Passed")
            contract = read(profile["contract"])
            self.assertEqual(len(result["calls"]), contract["expected_work"]["child_commands"])
            self.assertLess(result["wall_seconds"], contract["bounds"]["wall_seconds"])
            if name == "arithmetic":
                self.assertEqual((result["import_lean_statements"], result["new_lean_statements"]), (230, 35))
                for module in read("arithmetic-map.json")["modules"]:
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
            # Bruhat adds an equation; separately pinned navigation regressions
            # retain their original archived inventories and exact source hashes.
            if name not in {'test_arithmetic.py', 'test_bruhat.py', 'test_pgl.py', 'test_fixed_points.py', 'inventory.py', 'inventory.json', 'test_projective.py', 'test_affine_generation.py', 'test_apollonius.py'}:
                self.assertEqual(files["sources/" + name], (HERE / name).read_bytes())
        for name, digest in read("inventory.json")["sources"].items():
            self.assertEqual(hashlib.sha256(files["manuscript/" + name]).hexdigest(), digest)
        self.assertEqual(record["total_lean_statements"], 539)


if __name__ == "__main__":
    unittest.main()
