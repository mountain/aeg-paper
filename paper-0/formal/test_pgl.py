"""Scalar faithfulness, standard GL quotient boundaries and evidence (CC0)."""

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


class PGLBoundaryTests(unittest.TestCase):
    def test_exact_scalar_and_standard_quotient_audits_have_source_maps(self):
        mapping = read("pgl-map.json")
        declared = set()
        for module in mapping["modules"]:
            text = (HERE / module["file"]).read_text()
            names = re.findall(r"^(?:@\[ext\] )?theorem (\w+)", text, re.M)
            self.assertEqual(names, module["lean_audit_names"])
            self.assertEqual(names, re.findall(r"^#print axioms " + re.escape(module["module"]) + r"\.(\w+)", text, re.M))
            self.assertEqual(set(names), set(module["expected_axioms"]))
            self.assertFalse(re.search(r"^\s*(?:axiom|constant)\s|\b(?:sorry|admit|native_decide)\b", text, re.M))
            self.assertTrue(all(set(a) <= {"propext", "Classical.choice", "Quot.sound"}
                                for a in module["expected_axioms"].values()))
            declared.update(module["module"] + "." + n for n in names)
        self.assertEqual(len(declared), 41)
        self.assertEqual(declared, {n for row in mapping["mapping"] for n in row["formal"]})
        source = (ROOT / mapping["source"]).read_text()
        for row in mapping["mapping"]:
            for label in row["source_labels"]:
                self.assertIn("\\label{" + label + "}", source)
        live = inventory.generate()
        self.assertEqual(live, read("inventory.json"))
        self.assertEqual(len(live["claims"]), 102)
        self.assertEqual(sum(c["formal_status"] == "component-map-supplied" for c in live["claims"]), 32)
        self.assertEqual(len(live["equation_components"]), 4)
        original = inventory.digest
        with patch.object(inventory, "digest", side_effect=lambda p:
                          "changed" if p == ROOT / mapping["source"] else original(p)):
            with self.assertRaisesRegex(ValueError, "reviewed formal correspondence has source drift"):
                inventory.generate()

    def test_old_proof_library_goals_receivers_and_numerical_bounds_remain_exact(self):
        old = read("evidence/projective-execution.json")
        with tarfile.open(HERE / "evidence" / old["archive"]["path"]) as stream:
            files = {m.name: stream.extractfile(m).read() for m in stream.getmembers() if m.name.startswith("sources/")}
        old_lock = json.loads(files["sources/machine.lock.json"])
        changed = {n for n in old_lock["formal_sources"] if files["sources/" + n] != (HERE / n).read_bytes()}
        self.assertEqual(changed, {"inventory.py", "inventory.json", "test_projective.py"})
        contract = read("contract-pgl.json")
        self.assertEqual(contract["bounds"], read("contract-projective.json")["bounds"])
        self.assertEqual(contract["expected_work"]["child_commands"], 9)
        self.assertEqual(len(contract["negative_controls"]), 4)
        for control in contract["negative_controls"]:
            self.assertTrue((HERE / control["file"]).is_file())
            self.assertGreaterEqual(len(control["expected_fragments"]), 2)

    def test_gl_scalar_kernel_quotient_and_equality_distinctions_are_explicit(self):
        scalar = (HERE / "ProjectiveFaithfulness.lean").read_text()
        for name in ("three_fixed_points_force_scalar", "equal_actions_iff_nonzero_scalar",
                     "literal_matrix_equality_is_stronger", "one_point_agreement_is_insufficient"):
            self.assertIn("theorem " + name, scalar)
        group = (HERE / "ProjectiveGeneralLinear.lean").read_text()
        self.assertIn("Matrix.GeneralLinearGroup (Fin 2) K", group)
        self.assertIn("carrier := {g | ∃ s : K, s ≠ 0", group)
        self.assertIn("theorem scalarSubgroup_matrix_membership", group)
        self.assertIn("def PGL2 (K : Type*) [Field K] := GL2 K ⧸", group)
        self.assertIn("theorem scalarSubgroup_eq_kernel", group)
        self.assertIn("theorem quotient_action_injective", group)
        self.assertIn("QuotientGroup.quotientKerEquivRange", group)
        self.assertIn("def coefficientEquiv", group)
        self.assertIn("Abstract affine-group isomorphism and an independently packaged quotient-level generator theorem",
                      read("pgl-map.json")["excluded"])
        self.assertEqual(len(read("chapter03-obligations.json")["obligations"]), 6)


class PGLReceiptTests(unittest.TestCase):
    def test_six_profiles_current_sources_and_specific_rejections_are_archived(self):
        record = read("evidence/pgl-execution.json")
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
        self.assertEqual(set(record["profiles"]), {"native", "analytic", "chapter04", "apollonius", "projective", "pgl"})
        for name, profile in record["profiles"].items():
            raw = files[profile["directory"] + "/result.json"]
            self.assertEqual(hashlib.sha256(raw).hexdigest(), profile["report_sha256"])
            result = json.loads(raw)
            self.assertEqual(result["status"], "Passed")
            contract = read(profile["contract"])
            self.assertEqual(len(result["calls"]), contract["expected_work"]["child_commands"])
            self.assertLess(result["wall_seconds"], contract["bounds"]["wall_seconds"])
            if name == "pgl":
                self.assertEqual((result["import_lean_statements"], result["new_lean_statements"]), (31, 41))
                for module in read("pgl-map.json")["modules"]:
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
        for name, digest in lock["formal_sources"].items():
            self.assertEqual(hashlib.sha256(files["sources/" + name]).hexdigest(), digest)
            # The affine/generation continuation separately pins current
            # navigation and this receipt test; the PGL snapshot stays exact.
            if name not in {"inventory.py", "inventory.json", "test_pgl.py"}:
                self.assertEqual(files["sources/" + name], (HERE / name).read_bytes())
        for name, digest in read("inventory.json")["sources"].items():
            self.assertEqual(hashlib.sha256(files["manuscript/" + name]).hexdigest(), digest)
        self.assertEqual(record["total_lean_statements"], 465)


if __name__ == "__main__":
    unittest.main()
