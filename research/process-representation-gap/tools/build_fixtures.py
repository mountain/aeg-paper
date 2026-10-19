#!/usr/bin/env python3
"""Extract the minimal witnesses into ``fixtures/`` with their provenance.

Work-plan section 10 asks for ``fixtures/`` to hold "minimal positive and
negative witnesses together with fixed source references", and section 7
requires raw data to be machine-readable and traceable.

Fixtures are therefore EXTRACTED, never retyped.  Each fixture records the
evidence file it came from, that file's SHA-256, and the exact JSON pointer, so
a reviewer can walk from the fixture back to the run that produced it.  A
missing pointer is a failure, not an omission.

Run:

    python3 research/process-representation-gap/tools/build_fixtures.py
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))
import gapkit  # noqa: E402
from gapkit import require  # noqa: E402

EVIDENCE = ROOT / "evidence"
FIXTURES = ROOT / "fixtures"
SCHEMA = "aeg.process-representation-gap.fixture.v1"

# Declared extraction table: fixture name -> (evidence file, JSON pointer).
# Adding a witness means adding a row here, so a fixture can never appear
# without a source.
DECLARED = [
    ("exp2-order-gap", "exp2-loop-continuation.json", ["witnesses", "order_gap"]),
    ("exp2-legality-gap", "exp2-loop-continuation.json", ["witnesses", "legality_gap"]),
    ("exp2-positive-control", "exp2-loop-continuation.json", ["witnesses", "positive_control"]),
    ("exp2-pr16-continuation-gap", "exp2-loop-continuation.json",
     ["pr16_native_continuation_gap"]),
    ("exp1-mixing-gap", "exp1-order-and-mixing.json", ["witnesses", "gap"]),
    ("exp1-positive-control", "exp1-order-and-mixing.json", ["witnesses", "positive_control"]),
    ("exp1-spectral", "exp1-order-and-mixing.json", ["witnesses", "spectral"]),
    ("exp4-baseline-gate-i", "exp4-objectification-elevation.json",
     ["baseline_control", "gates", "gate_i_task_sufficiency_pi_out", "minimal_witness"]),
    ("exp4-elevation-verdict", "exp4-objectification-elevation.json",
     ["baseline_control", "verdict"]),
    ("exp6-witness2-environment", "exp6-knot-deformation-environment.json",
     ["environments", "witness-2-environment-changes-equivalence"]),
    ("exp6-gate-b-refutation", "exp6-knot-deformation-environment.json",
     ["gates", "B_state_faithful"]),
    ("exp6-gate-d", "exp6-knot-deformation-environment.json", ["gates", "D_completeness"]),
    ("exp3-initial-filling-collision", "exp3-typed-hole-context.json",
     ["witnesses", "initial_filling_collision"]),
    ("exp3-positive-control", "exp3-typed-hole-context.json",
     ["witnesses", "positive_control"]),
    ("exp3-paper4-snapshot", "exp3-typed-hole-context.json", ["paper4_snapshot"]),
    ("adva-continuation-verdict", "adva-continuation-interface.json", ["verdict"]),
]


def pointer(doc, path):
    node = doc
    for key in path:
        require(isinstance(node, dict) and key in node, "FIXTURE-POINTER-MISSING",
                f"{'/'.join(path)} missing at {key!r}")
        node = node[key]
    return node


def dynamic_rows():
    """Rows whose shape is a repeated list, resolved at run time."""
    rows = []
    _, braid = read("exp5-braid-nonarithmetic.json")
    for witness in braid["witnesses"]:
        rows.append((f"exp5-{witness['id'].split('-')[0].lower()}",
                     "exp5-braid-nonarithmetic.json", ["witnesses", witness["id"]]))
    return rows


def read(name):
    path = EVIDENCE / name
    require(path.exists(), "FIXTURE-EVIDENCE-MISSING", str(path))
    return path, json.loads(path.read_text(encoding="utf-8"))


def run():
    FIXTURES.mkdir(exist_ok=True)
    rows = DECLARED + dynamic_rows()
    index = []
    for name, filename, path in rows:
        evidence_path, doc = read(filename)
        if path[0] == "witnesses" and len(path) == 2 and isinstance(doc.get("witnesses"), list):
            node = next((w for w in doc["witnesses"] if w.get("id") == path[1]), None)
            require(node is not None, "FIXTURE-POINTER-MISSING", f"{filename}:{path}")
        else:
            node = pointer(doc, path)
        record = {
            "schema": SCHEMA,
            "fixture": name,
            "source": {
                "evidence_file": filename,
                "sha256": gapkit.sha256_file(evidence_path),
                "pointer": ".".join(path),
            },
            "payload": node,
        }
        text = gapkit.canonical(record)
        (FIXTURES / f"{name}.json").write_text(text, encoding="utf-8")
        index.append({"fixture": name, "source": record["source"],
                      "sha256": gapkit.sha256_bytes(text.encode("utf-8"))})

    index_record = {
        "schema": SCHEMA + ".index",
        "generated_by": "tools/build_fixtures.py",
        "note": ("fixtures are extracted from evidence, never retyped; the source block "
                 "lets a reviewer walk from a fixture back to the run that produced it"),
        "fixtures": index,
    }
    (FIXTURES / "INDEX.json").write_text(gapkit.canonical(index_record), encoding="utf-8")
    return index_record


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", default=None)
    args = parser.parse_args()
    record = run()
    text = gapkit.canonical(record)
    if args.out:
        Path(args.out).write_text(text, encoding="utf-8")
    else:
        sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
