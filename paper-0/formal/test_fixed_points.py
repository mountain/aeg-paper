"""Fixed loci, invariant eigenlines and conjugation receipts (CC0)."""

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


class FixedPointsBoundaryTests(unittest.TestCase):
    def test_fixed_point_eigenline_dictionary_is_exactly_audited_and_source_mapped(self):
        mapping = read("fixed-points-map.json")
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
        self.assertEqual(len(names), 33)
        self.assertEqual(names, {n for row in mapping["mapping"] for n in row["formal"]})
        self.assertEqual(sum(len(m["lean_audit_names"]) for m in mapping["imports"]), 194)
        source = (ROOT / mapping["source"]).read_text()
        for row in mapping["mapping"]:
            for label in row["source_labels"]:
                self.assertIn("\\label{" + label + "}", source)
        live = inventory.generate()
        self.assertEqual(live, read("inventory.json"))
        self.assertEqual(len(live["claims"]), 102)
        self.assertEqual(sum(c["formal_status"] == "component-map-supplied" for c in live["claims"]), 32)
        self.assertTrue({"eq:p0-apollonius-pencil", "eq:p0-prefix-matrices", "eq:p0-affine-stabilizer", "eq:p0-projective-factorization", "eq:p0-bruhat"} <= {e["label"] for e in live["equation_components"]})
        claim = next(c for c in live["claims"] if "thm:p0-four-matrix-readings" in c["labels"])
        self.assertTrue(any(n.startswith("AEGPaper0.ProjectiveFixedPoints.") for n in claim["lean_components"]))
        original = inventory.digest
        with patch.object(inventory, "digest", side_effect=lambda p:
                          "changed" if p == ROOT / mapping["source"] else original(p)):
            with self.assertRaisesRegex(ValueError, "reviewed formal correspondence has source drift"):
                inventory.generate()

    def test_old_proof_goals_library_receivers_and_numeric_bounds_remain_exact(self):
        old = read("evidence/bruhat-execution.json")
        with tarfile.open(HERE / "evidence" / old["archive"]["path"]) as stream:
            files = {m.name: stream.extractfile(m).read() for m in stream.getmembers() if m.name.startswith("sources/")}
        old_lock = json.loads(files["sources/machine.lock.json"])
        changed = {n for n in old_lock["formal_sources"] if files["sources/" + n] != (HERE / n).read_bytes()}
        self.assertEqual(changed, {"inventory.py", "inventory.json", "test_bruhat.py"})
        contract = read("contract-fixed-points.json")
        self.assertEqual(contract["bounds"], read("contract-bruhat.json")["bounds"])
        self.assertEqual(contract["expected_work"]["child_commands"], 15)
        self.assertEqual(len(contract["negative_controls"]), 4)
        for control in contract["negative_controls"]:
            self.assertTrue((HERE / control["file"]).is_file())
            self.assertGreaterEqual(len(control["expected_fragments"]), 2)

    def test_actual_invariant_spans_quotient_lines_and_nonclaims_are_explicit(self):
        text = (HERE / "ProjectiveFixedPoints.lean").read_text()
        for phrase in ("Vec K →ₗ[K] Vec K", "Submodule.span K {v}", "def lineAction : PGL2 K →*",
                       "def eigenlineFixedEquiv", "def fixedPointConjugacy", "theorem fixedSet_conjugate",
                       "theorem finite_fixed_eigenvalue_nonzero", "theorem eigenvalue_unique",
                       "theorem inversion_no_rational_fixed_point",
                       "theorem representative_eigenvalues_are_not_intrinsic"):
            self.assertIn(phrase, text)
        self.assertIn("Analytic attraction, repulsion, stability, convergence or infinite-expression evaluation",
                      read("fixed-points-map.json")["excluded"])
        self.assertEqual(len(read("chapter03-obligations.json")["obligations"]), 6)


class FixedPointsReceiptTests(unittest.TestCase):
    def test_ten_profiles_current_sources_and_specific_rejections_are_archived(self):
        record = read("evidence/fixed-points-execution.json")
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
        self.assertEqual(set(record["profiles"]), {"native", "analytic", "chapter04", "apollonius", "projective", "pgl", "affine_generation", "arithmetic", "bruhat", "fixed_points"})
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
            if name == "fixed_points":
                self.assertEqual((result["import_lean_statements"], result["new_lean_statements"]), (194, 33))
                for module in read("fixed-points-map.json")["modules"]:
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
        self.assertEqual(record["total_lean_statements"], 607)


if __name__ == "__main__":
    unittest.main()
