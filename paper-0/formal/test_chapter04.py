"""Chapter 4 scope, guards, source pins and retained execution boundaries (CC0)."""

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


class Chapter04BoundaryTests(unittest.TestCase):
    def test_current_source_correspondence_audits_and_scope_are_exact(self):
        mapping = read("chapter04-map.json")
        declared = set()
        for module in mapping["modules"]:
            text = (HERE / module["file"]).read_text()
            names = re.findall(r"^theorem (\w+)", text, re.M)
            self.assertEqual(names, module["lean_audit_names"])
            self.assertEqual(names, re.findall(r"^#print axioms " + re.escape(module["module"]) + r"\.(\w+)", text, re.M))
            self.assertEqual(set(names), set(module["expected_axioms"]))
            self.assertFalse(re.search(r"^\s*(?:axiom|constant)\s|\b(?:sorry|admit|native_decide)\b", text, re.M))
            self.assertTrue(all(set(a) <= {"propext", "Classical.choice", "Quot.sound"}
                                for a in module["expected_axioms"].values()))
            declared.update(module["module"] + "." + n for n in names)
        attached = set()
        for row in mapping["mapping"]:
            text = (ROOT / row.get("source", mapping["source"])).read_text()
            for label in row["source_labels"]:
                self.assertIn("\\label{" + label + "}", text)
            attached.update(row["formal"])
        self.assertEqual(attached, declared)
        self.assertEqual(len(declared), 57)
        self.assertIn("Full PGL/projective-line action and matrix-to-bijection identification", mapping["excluded"])
        self.assertIn("Intrinsic horocycle/ideal-boundary and differential tangency identification", mapping["excluded"])
        self.assertIn("enclosed disks", mapping["interpretation"])
        self.assertEqual(inventory.generate(), read("inventory.json"))

    def test_both_manuscript_sources_reject_drift_and_old_proof_library_contracts_stay_exact(self):
        mapping = read("chapter04-map.json")
        for source in [mapping["source"], *mapping["additional_sources"]]:
            original = inventory.digest
            with patch.object(inventory, "digest", side_effect=lambda p:
                              "changed" if p == ROOT / source else original(p)):
                with self.assertRaisesRegex(ValueError, "reviewed formal correspondence has source drift"):
                    inventory.generate()
        old = read("evidence/analysis-execution.json")
        with tarfile.open(HERE / "evidence" / old["archive"]["path"]) as stream:
            snapshots = {m.name: stream.extractfile(m).read() for m in stream.getmembers() if m.name.startswith("sources/")}
        for module in read("analysis-map.json")["modules"] + read("analysis-map.json")["core_imports"]:
            self.assertEqual(snapshots["sources/" + module["file"]], (HERE / module["file"]).read_bytes())
        for name in ("mathlib.lock.json", "contract-chapter03.json", "contract-analysis-v1.1.json",
                     "analysis_run.py", "chapter03_run.py", "run.py"):
            self.assertEqual(snapshots["sources/" + name], (HERE / name).read_bytes())
        contract = read("contract-chapter04.json")
        self.assertEqual(contract["bounds"], read("contract-analysis-v1.1.json")["bounds"])
        self.assertEqual(contract["expected_work"]["child_commands"], 8)
        self.assertEqual(len(contract["negative_controls"]), 4)
        for control in contract["negative_controls"]:
            self.assertTrue((HERE / control["file"]).is_file())
            self.assertGreaterEqual(len(control["expected_fragments"]), 2)

    def test_deferred_chapter03_obligations_and_pole_wording_limitation_remain_visible(self):
        obligations = read("chapter03-obligations.json")
        self.assertEqual(len(obligations["obligations"]), 6)
        source = (ROOT / "paper-0/sections/03-aes-and-motion.tex").read_text()
        for row in obligations["obligations"]:
            self.assertEqual(row["status"], "deferred-formal-prerequisites")
            self.assertTrue(row["difficulty"] and row["resume_when"])
            for label in row["source_labels"]:
                self.assertIn("\\label{" + label + "}", source)
        mapping = read("chapter04-map.json")
        self.assertEqual(mapping["source_audit"][0]["source_label"], "rem:p0-pole-forward")
        self.assertIn("first exit", mapping["source_audit"][0]["issue"])
        text = (HERE / "Chapter04Ripples.lean").read_text()
        self.assertIn("theorem output_translation_ripple", text)
        self.assertIn("theorem inversion_followed_by_translation_has_same_finite_pole", text)
        live = inventory.generate()
        for label in ("thm:p0-ripple-pencil-formula", "lem:p0-pole-covariance", "prop:p0-pole-rigidity"):
            self.assertEqual(next(c for c in live["claims"] if label in c["labels"])["formal_status"],
                             "component-map-supplied")
        for label in ("prop:p0-projective-trichotomy", "ex:p0-e1-model"):
            self.assertEqual(next(c for c in live["claims"] if label in c["labels"])["formal_status"],
                             "not-yet-formalized")


class Chapter04ReceiptTests(unittest.TestCase):
    def test_three_profiles_full_current_snapshot_audits_and_specific_controls_are_archived(self):
        record = read("evidence/chapter04-execution.json")
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
        for name, profile in record["profiles"].items():
            raw = files[profile["directory"] + "/result.json"]
            self.assertEqual(hashlib.sha256(raw).hexdigest(), profile["report_sha256"])
            result = json.loads(raw)
            self.assertEqual(result["status"], "Passed")
            contract = read(profile["contract"])
            self.assertEqual(len(result["calls"]), contract["expected_work"]["child_commands"])
            self.assertLess(result["wall_seconds"], contract["bounds"]["wall_seconds"])
            if name == "chapter04":
                self.assertEqual(result["new_lean_statements"], 57)
                for module in read("chapter04-map.json")["modules"]:
                    self.assertEqual(result["axioms"][module["module"]], module["expected_axioms"])
                for control in contract["negative_controls"]:
                    diagnostics = files[profile["directory"] + "/lean-negative-" + control["name"] + ".stdout"].decode()
                    self.assertEqual(diagnostics.count("error:"), 1)
                    self.assertIn("Type mismatch", diagnostics)
                    for fragment in control["expected_fragments"]:
                        self.assertIn(fragment, diagnostics)
            elif name == "analytic":
                self.assertEqual((result["core_lean_statements"], result["new_lean_statements"]), (192, 66))
            else:
                self.assertEqual(len(result["rows"]), 69)
                self.assertEqual(result["reference_steps"], 51137)
                for row in result["rows"]:
                    self.assertEqual(hashlib.sha256(files[profile["directory"] + "/" + row["name"] + ".run.adva"]).hexdigest(),
                                     row["report_sha256"])
        lock_raw = files["sources/machine.lock.json"]
        self.assertEqual(hashlib.sha256(lock_raw).hexdigest(), record["source_lock_sha256"])
        lock = json.loads(lock_raw)
        self.assertEqual(lock, read("machine.lock.json"))
        for name, digest in lock["formal_sources"].items():
            self.assertEqual(hashlib.sha256(files["sources/" + name]).hexdigest(), digest)
            self.assertEqual(files["sources/" + name], (HERE / name).read_bytes())
        for name, digest in read("inventory.json")["sources"].items():
            self.assertEqual(hashlib.sha256(files["manuscript/" + name]).hexdigest(), digest)
        self.assertEqual(record["total_lean_statements"], 315)


if __name__ == "__main__":
    unittest.main()
