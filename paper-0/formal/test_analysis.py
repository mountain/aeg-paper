"""Real-analysis source, library and recorded-reception boundaries (CC0)."""

import hashlib
import json
from pathlib import Path
import re
import tarfile
import tempfile
import unittest
from unittest.mock import patch

import analysis_dependencies
import inventory

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]


def read(name):
    return json.loads((HERE / name).read_text())


class AnalysisBoundaryTests(unittest.TestCase):
    def test_every_analytic_statement_has_a_source_map_exact_audit_and_explicit_remaining_scope(self):
        mapping = read("analysis-map.json")
        source = ROOT / mapping["source"]
        self.assertEqual(hashlib.sha256(source.read_bytes()).hexdigest(), mapping["source_sha256"])
        names = set()
        for module in mapping["modules"]:
            lean = (HERE / module["file"]).read_text()
            declared = re.findall(r"^theorem (\w+)", lean, re.M)
            self.assertEqual(declared, module["lean_audit_names"])
            self.assertEqual(declared, re.findall(r"^#print axioms (\w+)", lean, re.M))
            self.assertEqual(set(declared), set(module["expected_axioms"]))
            self.assertFalse(re.search(r"^\s*(?:axiom|constant)\s|\b(?:sorry|admit|native_decide)\b", lean, re.M))
            self.assertTrue(all(set(a) <= {"propext", "Classical.choice", "Quot.sound"}
                                for a in module["expected_axioms"].values()))
            names.update(module["module"] + "." + name for name in declared)
        attached = set()
        for row in mapping["mapping"]:
            for label in row["source_labels"]:
                self.assertIn("\\label{" + label + "}", source.read_text())
            attached.update(row["formal"])
        self.assertEqual(attached, names)
        self.assertEqual(len(names), 66)
        self.assertEqual(sum(len(m["lean_audit_names"]) for m in mapping["core_imports"]), 192)
        self.assertIn("Gaussian curvature and metric completeness", mapping["excluded"])
        self.assertIn("intrinsic bundle Laplacian identification", mapping["excluded"])
        live = inventory.generate()
        self.assertEqual(live, read("inventory.json"))
        for label in ("def:regular-aes", "prop:laplace-eigenfunction", "thm:continuous-affine-flow"):
            self.assertEqual(next(c for c in live["claims"] if label in c["labels"])["formal_status"],
                             "component-map-supplied")

    def test_library_fingerprints_refuse_changed_sources_objects_and_dependency_revisions(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / ".git").mkdir(); (root / ".git/HEAD").write_text("a" * 40)
            (root / "source.lean").write_text("valid source")
            (root / "object.olean").write_bytes(b"fixed object")
            lock = {"commit": "a" * 40, "packages": {},
                    "sources": {"source.lean": analysis_dependencies.sha(root / "source.lean")},
                    "compiled_library": {"object.olean": analysis_dependencies.sha(root / "object.olean")}}
            (root / "mathlib.lock.json").write_text(json.dumps(lock))
            with patch.object(analysis_dependencies, "HERE", root):
                self.assertEqual(analysis_dependencies.check(root)["mathlib_source_files"], 1)
                for name, message in (("source.lean", "sources drift"), ("object.olean", "compiled_library drift")):
                    before = (root / name).read_bytes(); (root / name).write_bytes(b"changed")
                    with self.assertRaisesRegex(ValueError, message): analysis_dependencies.check(root)
                    (root / name).write_bytes(before)
                (root / ".git/HEAD").write_text("b" * 40)
                with self.assertRaisesRegex(ValueError, "revision mismatch"): analysis_dependencies.check(root)

    def test_guard_controls_and_separate_receiving_profiles_keep_their_declared_boundaries(self):
        contract = read("contract-analysis-v1.1.json")
        self.assertEqual(len(contract["negative_controls"]), 4)
        for control in contract["negative_controls"]:
            self.assertTrue((HERE / control["file"]).is_file())
            self.assertTrue(control["expected_fragments"])
        legacy = read("contract-chapter03.json")["bounds"]
        self.assertEqual(legacy["wall_seconds"], 300)
        self.assertEqual(legacy["lean_child_address_space_bytes"], 4294967296)
        self.assertEqual(contract["bounds"]["wall_seconds"], 300)
        self.assertEqual(contract["bounds"]["lean_child_address_space_bytes"], 8589934592)
        self.assertEqual(contract["expected_work"]["child_commands"], 16)
        lock = read("mathlib.lock.json")
        self.assertEqual(lock["commit"], "f897ebcf72cd16f89ab4577d0c826cd14afaafc7")
        self.assertEqual(lock["lean_version"], "4.24.0")
        self.assertTrue(lock["sources"] and lock["compiled_library"])

    def test_failed_lake_classification_and_its_exact_receiving_correction_are_retained(self):
        record = read("evidence/analysis-attempt-1.json")
        self.assertEqual(record["status"], "Failed")
        self.assertFalse(record["whole_run_admitted"])
        self.assertFalse(record["analytic_proofs_reached"])
        self.assertEqual(record["native_profile_status"], "Passed")
        archive = HERE / "evidence" / record["archive"]["path"]
        self.assertEqual(hashlib.sha256(archive.read_bytes()).hexdigest(), record["archive"]["sha256"])
        with tarfile.open(archive) as stream:
            members = stream.getmembers()
            self.assertTrue(all(m.isfile() and not Path(m.name).is_absolute() and
                                ".." not in Path(m.name).parts for m in members))
            files = {m.name: stream.extractfile(m).read() for m in members}
        self.assertIn("out of memory", files["analysis-01/mathlib-path.stderr"].decode())
        failed = json.loads(files["analysis-01/result.json"])
        self.assertEqual(failed["calls"][-1]["name"], "mathlib-path")
        self.assertEqual(failed["calls"][-1]["address_space_limit_bytes"], 1073741824)
        old = files["sources/analysis_run.py"].decode()
        corrected = old.replace('"contract-analysis.json"', '"contract-analysis-v1.1.json"').replace(
            'self.args.lean.parent / "lake", "env", "printenv", "LEAN_PATH"])',
            'self.args.lean.parent / "lake", "env", "printenv", "LEAN_PATH"], lean=True)')
        self.assertEqual(corrected, (HERE / "analysis_run.py").read_text())
        self.assertEqual(read("contract-analysis.json")["bounds"], read("contract-analysis-v1.1.json")["bounds"])
        for module in read("analysis-map.json")["modules"]:
            self.assertEqual(files["sources/" + module["file"]], (HERE / module["file"]).read_bytes())
        self.assertEqual(files["sources/mathlib.lock.json"], (HERE / "mathlib.lock.json").read_bytes())


class AnalysisReceiptTests(unittest.TestCase):
    def test_both_received_profiles_sources_imports_library_pins_and_controls_are_archived(self):
        record = read("evidence/analysis-execution.json")
        self.assertEqual(record["status"], "Passed")
        path = HERE / "evidence" / record["archive"]["path"]
        self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(), record["archive"]["sha256"])
        with tarfile.open(path) as stream:
            members = stream.getmembers()
            self.assertEqual(len(members), record["archive"]["members"])
            self.assertLess(sum(m.size for m in members), 64 * 1024 * 1024)
            self.assertTrue(all(m.isfile() and not Path(m.name).is_absolute() and
                                ".." not in Path(m.name).parts for m in members))
            files = {m.name: stream.extractfile(m).read() for m in members}
        analytic = json.loads(files["analysis-02/result.json"])
        legacy = json.loads(files["native-02/result.json"])
        for key, result, name in (("analytic_report_sha256", analytic, "analysis-02"),
                                  ("native_report_sha256", legacy, "native-02")):
            self.assertEqual(result["status"], "Passed")
            self.assertEqual(hashlib.sha256(files[name + "/result.json"]).hexdigest(), record[key])
        self.assertEqual(analytic["new_lean_statements"], 66)
        self.assertEqual(analytic["core_lean_statements"], 192)
        self.assertEqual(len(analytic["calls"]), 16)
        self.assertTrue(all(c["address_space_limit_bytes"] == 8589934592 for c in analytic["calls"]))
        self.assertEqual(len(legacy["rows"]), 69)
        self.assertEqual(len(legacy["calls"]), 148)
        lock = json.loads(files["sources/machine.lock.json"])
        for name, digest in lock["formal_sources"].items():
            self.assertEqual(hashlib.sha256(files["sources/" + name]).hexdigest(), digest)
            self.assertEqual(files["sources/" + name], (HERE / name).read_bytes())
        for name, digest in json.loads(files["sources/inventory.json"])["sources"].items():
            self.assertEqual(hashlib.sha256(files["manuscript/" + name]).hexdigest(), digest)
        for row in legacy["rows"]:
            self.assertEqual(hashlib.sha256(files["native-02/" + row["name"] + ".run.adva"]).hexdigest(), row["report_sha256"])
        for module in read("analysis-map.json")["modules"]:
            self.assertEqual(analytic["axioms"][module["module"]], module["expected_axioms"])
        self.assertEqual(set(analytic["negative_controls"]), {"height", "laplacian-sign", "initial-value", "intensity"})
        self.assertEqual(analytic["mathlib_lock_sha256"], hashlib.sha256(files["sources/mathlib.lock.json"]).hexdigest())


if __name__ == "__main__":
    unittest.main()
