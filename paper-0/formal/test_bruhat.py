"""Source-bound PGL conjugacy, Bruhat cells and execution evidence (CC0)."""

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
SUCCESSORS = {"inventory.py", "inventory.json", "test_projective.py", "test_pgl.py",
              "test_affine_generation.py", "test_arithmetic.py"}


def read(name):
    return json.loads((HERE / name).read_text())


class BruhatBoundaryTests(unittest.TestCase):
    def test_exact_audits_and_new_equation_are_source_bound(self):
        mapping = read("bruhat-map.json")
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
        self.assertEqual(sum(len(m["lean_audit_names"]) for m in mapping["imports"]), 159)
        source = (ROOT / mapping["source"]).read_text()
        for row in mapping["mapping"]:
            for label in row["source_labels"]:
                self.assertIn("\\label{" + label + "}", source)
        live = inventory.generate()
        self.assertEqual(live, read("inventory.json"))
        self.assertEqual(len(live["claims"]), 102)
        self.assertGreaterEqual(sum(c["formal_status"] == "component-map-supplied" for c in live["claims"]), 32)
        self.assertTrue({"eq:p0-apollonius-pencil", "eq:p0-prefix-matrices", "eq:p0-affine-stabilizer",
                         "eq:p0-projective-factorization", "eq:p0-bruhat"} <=
                        {e["label"] for e in live["equation_components"]})
        original = inventory.digest
        with patch.object(inventory, "digest", side_effect=lambda p:
                          "changed" if p == ROOT / mapping["source"] else original(p)):
            with self.assertRaisesRegex(ValueError, "reviewed formal correspondence has source drift"):
                inventory.generate()

    def test_old_proofs_receivers_and_bounds_are_preserved(self):
        old = read("evidence/arithmetic-execution.json")
        with tarfile.open(HERE / "evidence" / old["archive"]["path"]) as stream:
            files = {m.name: stream.extractfile(m).read() for m in stream.getmembers() if m.name.startswith("sources/")}
        lock = json.loads(files["sources/machine.lock.json"])
        changed = {n for n in lock["formal_sources"] if files["sources/" + n] != (HERE / n).read_bytes()}
        self.assertEqual(changed, {'test_arithmetic.py', 'test_pgl.py', 'inventory.py', 'inventory.json', 'test_projective.py', 'test_affine_generation.py', 'test_apollonius.py'})
        self.assertEqual(len(json.loads(files["sources/inventory.json"])["equation_components"]), 4)
        contract = read("contract-bruhat.json")
        self.assertEqual(contract["bounds"], read("contract-arithmetic.json")["bounds"])
        self.assertEqual(contract["expected_work"]["child_commands"], 14)
        self.assertEqual(len(contract["negative_controls"]), 4)
        for control in contract["negative_controls"]:
            self.assertTrue((HERE / control["file"]).is_file())
            self.assertGreaterEqual(len(control["expected_fragments"]), 2)

    def test_stabilizers_pole_fibers_cells_and_domain_guards_are_distinct(self):
        text = (HERE / "ProjectiveBruhat.lean").read_text()
        for phrase in ("def pointStabilizer", "def stabilizerConjugacy", "def finiteAffineEquiv",
                       "theorem finite_stabilizer_iff", "theorem finite_pole_fiber",
                       "theorem finite_stabilizer_excludes_own_pole", "theorem finite_pole_fiber_not_subgroup",
                       "theorem bruhat_cover", "theorem bruhat_disjoint", "theorem bigCell_matrix_iff",
                       "theorem bigCell_iff_finite_pole", "(hz : z ≠ q)"):
            self.assertIn(phrase, text)
        self.assertIn("Topology, manifold structure or dimensions of Bruhat cells", read("bruhat-map.json")["excluded"])
        self.assertEqual(len(read("chapter03-obligations.json")["obligations"]), 6)


class BruhatReceiptTests(unittest.TestCase):
    def test_nine_successful_profiles_current_sources_and_exact_controls_are_archived(self):
        record = read("evidence/bruhat-execution.json")
        self.assertEqual(record["status"], "Passed")
        archive = HERE / "evidence" / record["archive"]["path"]
        self.assertEqual(hashlib.sha256(archive.read_bytes()).hexdigest(), record["archive"]["sha256"])
        with tarfile.open(archive) as stream:
            members = stream.getmembers()
            self.assertEqual(len(members), record["archive"]["members"])
            self.assertLess(sum(m.size for m in members), 64 * 1024 * 1024)
            self.assertTrue(all(m.isfile() and not Path(m.name).is_absolute() and ".." not in Path(m.name).parts for m in members))
            files = {m.name: stream.extractfile(m).read() for m in members}
        self.assertEqual(set(record["profiles"]), {"native", "analytic", "chapter04", "apollonius", "projective", "pgl",
                                                  "affine_generation", "arithmetic", "bruhat"})
        for name, profile in record["profiles"].items():
            raw = files[profile["directory"] + "/result.json"]
            self.assertEqual(hashlib.sha256(raw).hexdigest(), profile["report_sha256"])
            result = json.loads(raw)
            contract = read(profile["contract"])
            self.assertEqual(result["status"], "Passed")
            self.assertEqual(len(result["calls"]), contract["expected_work"]["child_commands"])
            self.assertLess(result["wall_seconds"], contract["bounds"]["wall_seconds"])
            snapshot = profile["source_snapshot"]
            source_pin = result.get("source_lock_sha256", result.get("machine_lock_sha256"))
            raw_lock = files[snapshot + "/machine.lock.json"]
            self.assertEqual(source_pin, hashlib.sha256(raw_lock).hexdigest())
            for filename, digest in json.loads(raw_lock)["formal_sources"].items():
                self.assertEqual(hashlib.sha256(files[snapshot + "/" + filename]).hexdigest(), digest)
            if name == "bruhat":
                self.assertEqual((result["import_lean_statements"], result["new_lean_statements"]), (159, 35))
                for module in read("bruhat-map.json")["modules"]:
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
            # The fixed-point continuation separately pins current navigation
            # and this historical receipt regression.
            if name not in {'test_arithmetic.py', 'test_bruhat.py', 'test_pgl.py', 'test_fixed_points.py', 'inventory.py', 'inventory.json', 'test_projective.py', 'test_affine_generation.py', 'test_apollonius.py'}:
                self.assertEqual(files["sources/" + name], (HERE / name).read_bytes())
        for name, digest in read("inventory.json")["sources"].items():
            self.assertEqual(hashlib.sha256(files["manuscript/" + name]).hexdigest(), digest)
        original_lock = json.loads(files["execution-snapshot-v1/machine.lock.json"])
        changed = {name for name in original_lock["formal_sources"]
                   if files["execution-snapshot-v1/" + name] != (HERE / name).read_bytes()}
        self.assertEqual(changed, {'test_arithmetic.py', 'test_bruhat.py', 'test_pgl.py', 'bruhat-map.json', 'contract-bruhat.json', 'inventory.py', 'inventory.json', 'test_projective.py', 'test_affine_generation.py', 'test_apollonius.py'})
        original_map = json.loads(files["execution-snapshot-v1/bruhat-map.json"])
        self.assertEqual(original_map["modules"], read("bruhat-map.json")["modules"])
        self.assertEqual(original_map["imports"], read("bruhat-map.json")["imports"])
        original = json.loads(files["bruhat-01/result.json"])
        self.assertEqual(original["status"], "Passed")
        self.assertEqual(hashlib.sha256(files["bruhat-01/result.json"]).hexdigest(),
                         record["terminology_successor"]["original_report_sha256"])
        self.assertEqual(record["total_lean_statements"], 574)


if __name__ == "__main__":
    unittest.main()
