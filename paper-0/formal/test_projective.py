"""Concrete projective quotient/action, scope, guards and evidence (CC0)."""

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


class ProjectiveBoundaryTests(unittest.TestCase):
    def test_homogeneous_and_actual_chart_statements_are_exactly_mapped_and_audited(self):
        mapping = read("projective-map.json")
        all_names = set()
        for module in mapping["modules"]:
            text = (HERE / module["file"]).read_text()
            names = re.findall(r"^theorem (\w+)", text, re.M)
            self.assertEqual(names, module["lean_audit_names"])
            self.assertEqual(names, re.findall(r"^#print axioms " + re.escape(module["module"]) + r"\.(\w+)", text, re.M))
            self.assertEqual(set(names), set(module["expected_axioms"]))
            self.assertFalse(re.search(r"^\s*(?:axiom|constant)\s|\b(?:sorry|admit|native_decide)\b", text, re.M))
            self.assertTrue(all(set(a) <= {"propext", "Classical.choice", "Quot.sound"}
                                for a in module["expected_axioms"].values()))
            all_names.update(module["module"] + "." + n for n in names)
        attached = set()
        for row in mapping["mapping"]:
            text = (ROOT / row.get("source", mapping["source"])).read_text()
            for label in row["source_labels"]:
                self.assertIn("\\label{" + label + "}", text)
            attached.update(row["formal"])
        self.assertEqual(attached, all_names)
        self.assertEqual(len(all_names), 70)
        self.assertEqual(sum(len(m["lean_audit_names"]) for m in mapping["imports"]), 57)
        live = inventory.generate()
        self.assertEqual(live, read("inventory.json"))
        self.assertEqual(len(live["claims"]), 102)
        self.assertGreaterEqual(sum(c["formal_status"] == "component-map-supplied" for c in live["claims"]), 32)
        self.assertTrue({"eq:p0-apollonius-pencil", "eq:p0-prefix-matrices", "eq:p0-affine-stabilizer", "eq:p0-projective-factorization"} <= {e["label"] for e in live["equation_components"]})
        for label in ("thm:p0-four-matrix-readings", "thm:p0-pgl2-generation"):
            self.assertEqual(next(c for c in live["claims"] if label in c["labels"])["formal_status"],
                             "component-map-supplied")

    def test_all_three_source_guards_and_preceding_proof_bytes_remain_exact(self):
        mapping = read("projective-map.json")
        for source in [mapping["source"], *mapping["additional_sources"]]:
            original = inventory.digest
            with patch.object(inventory, "digest", side_effect=lambda p:
                              "changed" if p == ROOT / source else original(p)):
                with self.assertRaisesRegex(ValueError, "reviewed formal correspondence has source drift"):
                    inventory.generate()
        old = read("evidence/apollonius-execution.json")
        with tarfile.open(HERE / "evidence" / old["archive"]["path"]) as stream:
            files = {m.name: stream.extractfile(m).read() for m in stream.getmembers() if m.name.startswith("sources/")}
        old_lock = json.loads(files["sources/machine.lock.json"])
        changed = {n for n in old_lock["formal_sources"] if files["sources/" + n] != (HERE / n).read_bytes()}
        self.assertEqual(changed, {'inventory.py', 'test_apollonius.py', 'inventory.json'})
        contract = read("contract-projective.json")
        self.assertEqual(contract["bounds"], read("contract-apollonius.json")["bounds"])
        self.assertEqual(contract["expected_work"]["child_commands"], 11)
        self.assertEqual(len(contract["negative_controls"]), 4)
        for control in contract["negative_controls"]:
            self.assertTrue((HERE / control["file"]).is_file())
            self.assertGreaterEqual(len(control["expected_fragments"]), 2)

    def test_quotient_inverse_chart_bridges_and_active_guard_counterexamples_are_present(self):
        line = (HERE / "ProjectiveLine.lean").read_text()
        self.assertIn("def lineSetoid", line)
        self.assertIn("def chartEquiv : Quotient", line)
        self.assertIn("theorem quotient_eq_iff_nonzero_scalar", line)
        self.assertIn("theorem quotient_action_representative", line)
        self.assertIn("left_inv := fun x => action_adjugate_left", line)
        self.assertIn("theorem zero_scalar_changes_action", line)
        bridge = (HERE / "Chapter04ProjectiveBridge.lean").read_text()
        self.assertIn("theorem singular_composition_counterexample", bridge)
        self.assertIn("theorem nonaffine_action_factorization", bridge)
        self.assertIn("theorem concrete_history_prefix_rigidity", bridge)
        complex_chart = (HERE / "Chapter04ComplexProjective.lean").read_text()
        self.assertIn("theorem real_complex_chart_compatibility", complex_chart)
        self.assertIn("theorem complex_ripple_chart_membership", complex_chart)
        self.assertIn("Isomorphism with an external PGL/Projectivization group API and faithfulness of its scalar quotient",
                      read("projective-map.json")["excluded"])
        self.assertEqual(len(read("chapter03-obligations.json")["obligations"]), 6)


class ProjectiveReceiptTests(unittest.TestCase):
    def test_five_profiles_current_sources_and_specific_rejections_are_archived(self):
        record = read("evidence/projective-execution.json")
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
        self.assertEqual(set(record["profiles"]), {"native", "analytic", "chapter04", "apollonius", "projective"})
        for name, profile in record["profiles"].items():
            raw = files[profile["directory"] + "/result.json"]
            self.assertEqual(hashlib.sha256(raw).hexdigest(), profile["report_sha256"])
            result = json.loads(raw)
            self.assertEqual(result["status"], "Passed")
            contract = read(profile["contract"])
            self.assertEqual(len(result["calls"]), contract["expected_work"]["child_commands"])
            self.assertLess(result["wall_seconds"], contract["bounds"]["wall_seconds"])
            if name == "projective":
                self.assertEqual((result["import_lean_statements"], result["new_lean_statements"]), (57, 70))
                for module in read("projective-map.json")["modules"]:
                    self.assertEqual(result["axioms"][module["module"]], module["expected_axioms"])
                for control in contract["negative_controls"]:
                    diagnostics = files[profile["directory"] + "/lean-negative-" + control["name"] + ".stdout"].decode()
                    self.assertEqual(diagnostics.count("error:"), 1)
                    self.assertIn("Type mismatch", diagnostics)
                    for fragment in control["expected_fragments"]:
                        self.assertIn(fragment, diagnostics)
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
            # The PGL successor pins current navigation and this receipt test
            # separately; the completed projective snapshot stays historical.
            if name not in {'test_arithmetic.py', 'test_bruhat.py', 'test_pgl.py', 'test_fixed_points.py', 'inventory.py', 'inventory.json', 'test_projective.py', 'test_affine_generation.py', 'test_apollonius.py'}:
                self.assertEqual(files["sources/" + name], (HERE / name).read_bytes())
        for name, digest in read("inventory.json")["sources"].items():
            self.assertEqual(hashlib.sha256(files["manuscript/" + name]).hexdigest(), digest)
        self.assertEqual(record["total_lean_statements"], 424)


if __name__ == "__main__":
    unittest.main()
