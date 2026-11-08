"""Apollonius source, equation navigation, guards and full receipts (CC0)."""

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


class ApolloniusBoundaryTests(unittest.TestCase):
    def test_exact_audits_correspond_to_the_numbered_equation_without_inventing_environments(self):
        mapping = read("apollonius-map.json")
        module, = mapping["modules"]
        text = (HERE / module["file"]).read_text()
        names = re.findall(r"^theorem (\w+)", text, re.M)
        self.assertEqual(names, module["lean_audit_names"])
        self.assertEqual(names, re.findall(r"^#print axioms " + re.escape(module["module"]) + r"\.(\w+)", text, re.M))
        self.assertEqual(len(names), 39)
        self.assertEqual(set(names), set(module["expected_axioms"]))
        self.assertFalse(re.search(r"^\s*(?:axiom|constant)\s|\b(?:sorry|admit|native_decide)\b", text, re.M))
        self.assertTrue(all(set(a) <= {"propext", "Classical.choice", "Quot.sound"}
                            for a in module["expected_axioms"].values()))
        attached = {n for row in mapping["mapping"] for n in row["formal"]}
        self.assertEqual(attached, {module["module"] + "." + n for n in names})
        live = inventory.generate()
        self.assertEqual(live, read("inventory.json"))
        self.assertEqual(len(live["claims"]), 102)
        # The projective successor maps two existing Section 6 environments;
        # the Apollonius equation itself still invents no environment.
        self.assertGreaterEqual(sum(c["formal_status"] == "component-map-supplied" for c in live["claims"]), 32)
        equation = next(e for e in live["equation_components"] if e["label"] == "eq:p0-apollonius-pencil")
        self.assertEqual(equation["label"], "eq:p0-apollonius-pencil")
        self.assertEqual(set(equation["lean_components"]), attached)
        self.assertIn("\\begin{equation}", (ROOT / equation["source"]).read_text().splitlines()[equation["line"] - 1])
        original = inventory.digest
        with patch.object(inventory, "digest", side_effect=lambda p:
                          "changed" if p == ROOT / mapping["source"] else original(p)):
            with self.assertRaisesRegex(ValueError, "reviewed formal correspondence has source drift"):
                inventory.generate()

    def test_old_proofs_library_goals_contracts_and_receivers_remain_exact(self):
        previous = read("evidence/chapter04-execution.json")
        with tarfile.open(HERE / "evidence" / previous["archive"]["path"]) as stream:
            files = {m.name: stream.extractfile(m).read() for m in stream.getmembers() if m.name.startswith("sources/")}
        old = json.loads(files["sources/machine.lock.json"])
        changed = {n for n in old["formal_sources"] if files["sources/" + n] != (HERE / n).read_bytes()}
        self.assertEqual(changed, {"inventory.py", "inventory.json", "test_chapter04.py"})
        contract = read("contract-apollonius.json")
        self.assertEqual(contract["bounds"], read("contract-chapter04.json")["bounds"])
        self.assertEqual(contract["expected_work"]["child_commands"], 8)
        self.assertEqual(len(contract["negative_controls"]), 4)
        for control in contract["negative_controls"]:
            self.assertTrue((HERE / control["file"]).is_file())
            self.assertGreaterEqual(len(control["expected_fragments"]), 2)
        self.assertEqual(read("apollonius-map.json")["imports"], [read("chapter04-map.json")["modules"][0]])

    def test_guard_counterexamples_and_proper_circle_scope_are_retained(self):
        mapping = read("apollonius-map.json")
        text = (HERE / "Chapter04Apollonius.lean").read_text()
        for name in ("unguarded_zero_level_at_pole_fails", "negative_unit_weight_is_not_bisector",
                     "equal_foci_unit_locus", "zero_level_singleton", "upper_zero_level_empty",
                     "negative_level_empty", "positive_level_upper_nonempty"):
            self.assertIn("theorem " + name, text)
        self.assertIn("Metric.sphere", text)
        self.assertIn("dist z (q : ℂ) = dist z (p : ℂ)", text)
        self.assertIn("proper-circle", mapping["source_audit"][0]["issue"])
        self.assertIn("r=0", mapping["source_audit"][0]["issue"])
        self.assertIn("Full PGL/projective-line action and matrix-to-bijection identification", mapping["excluded"])
        self.assertEqual(len(read("chapter03-obligations.json")["obligations"]), 6)


class ApolloniusReceiptTests(unittest.TestCase):
    def test_four_profiles_current_sources_and_expected_rejections_are_archived(self):
        record = read("evidence/apollonius-execution.json")
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
        self.assertEqual(set(record["profiles"]), {"native", "analytic", "chapter04", "apollonius"})
        for name, profile in record["profiles"].items():
            raw = files[profile["directory"] + "/result.json"]
            self.assertEqual(hashlib.sha256(raw).hexdigest(), profile["report_sha256"])
            result = json.loads(raw)
            self.assertEqual(result["status"], "Passed")
            contract = read(profile["contract"])
            self.assertEqual(len(result["calls"]), contract["expected_work"]["child_commands"])
            self.assertLess(result["wall_seconds"], contract["bounds"]["wall_seconds"])
            if name == "apollonius":
                self.assertEqual((result["import_lean_statements"], result["new_lean_statements"]), (36, 39))
                module, = read("apollonius-map.json")["modules"]
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
        raw = files["sources/machine.lock.json"]
        self.assertEqual(hashlib.sha256(raw).hexdigest(), record["source_lock_sha256"])
        lock = json.loads(raw)
        for name, digest in lock["formal_sources"].items():
            self.assertEqual(hashlib.sha256(files["sources/" + name]).hexdigest(), digest)
            # Preserve the completed Apollonius execution snapshot. Current
            # navigation and this receipt test have separately pinned successors.
            if name not in {'test_arithmetic.py', 'test_bruhat.py', 'test_pgl.py', 'test_fixed_points.py', 'inventory.py', 'inventory.json', 'test_projective.py', 'test_affine_generation.py', 'test_apollonius.py'}:
                self.assertEqual(files["sources/" + name], (HERE / name).read_bytes())
        for name, digest in read("inventory.json")["sources"].items():
            self.assertEqual(hashlib.sha256(files["manuscript/" + name]).hexdigest(), digest)
        self.assertEqual(record["total_lean_statements"], 354)


if __name__ == "__main__":
    unittest.main()
