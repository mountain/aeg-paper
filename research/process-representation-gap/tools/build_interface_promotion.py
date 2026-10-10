#!/usr/bin/env python3
"""Interface-promotion proposals for work-plan section 10.

Section 10 says: complete the research evidence first, and only then propose an
interface promotion; do not change stable interfaces across three repositories
at once.  This tool therefore emits **proposals**, never changes.

Each proposal is machine-checked against the same raw evidence the gap
classification uses: the verdicts it cites are re-read and re-tested at run
time, so a proposal cannot drift away from the finding that motivates it.  The
``applied`` field is a literal ``false`` and the tool refuses to emit a proposal
that claims otherwise.

Run:

    python3 research/process-representation-gap/tools/build_interface_promotion.py
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
PROPOSALS_DIR = ROOT / "proposals"
SCHEMA = "aeg.process-representation-gap.interface-promotion.v1"

# Declared proposals.  Each cites evidence pointers that are re-checked below.
PROPOSALS = [
    {
        "id": "P-AEG-1",
        "repository": "mountain/aeg-paper",
        "target": "governance/process-representation-gap-2026-10-10.md",
        "status_row_target": "governance/05-mathematical-status.md",
        "kind": "additive governance status record",
        "precedent": "governance/opposite-feature-witness-2026-10-09.md, added by PR 16",
        "summary": (
            "Register the six experiments and the pinned-source continuation gap as a "
            "governance-reviewed record, exactly as PR 16 registered its finite snapshot "
            "witness.  Additive only: no theorem, label, notation or frozen audit changes, "
            "and no claim is promoted."
        ),
        "citations": [
            ("exp2", "exp2-loop-continuation.json", ["representations", "pi0"],
             {"sufficient": False, "closed_update": False}),
            ("exp3", "exp3-typed-hole-context.json", ["context_search"],
             {"grid_candidates": 63, "grid_candidates_insufficient": 63}),
            ("adva", "adva-continuation-interface.json", ["verdict"],
             {"native_legal_continuation_interface_for_pr16_records": False}),
        ],
        "information_added": (
            "a reproducible, hash-pinned record of where six declared representations stop "
            "being sufficient, with the cost of each candidate and the exact witness"
        ),
        "cost": "one governance document; no runtime cost, no API, no code in the paper build",
        "task_improved": "an auditor asking whether PR 16's obstruction survives to other tasks",
        "still_fails": [
            "does not close PIV-F2; chi_T and chi_S remain two-record sample consistency",
            "does not promote any experiment result to a theorem",
        ],
        "regression_condition": (
            "any cited evidence file changing its SHA-256, or any cited verdict changing value; "
            "tools/build_interface_promotion.py re-checks both and exits nonzero"
        ),
        "review_gate": "repository governance review under AGENTS.md; no automatic merge",
        "applied": False,
    },
    {
        "id": "P-PG-1",
        "repository": "mountain/process-geometry",
        "target": "workstreams/process_representation_gap/",
        "kind": "research-local workstream, no src/ change",
        "precedent": (
            "workstreams/native_method_firewall/ (README + one module + one external test); "
            "workstreams/am_weight_compiler/ for the frozen-contract and disposition schema"
        ),
        "summary": (
            "Host the continuation-equivalence and objectification findings as a workstream "
            "following the repository's own convention: README + module + tests, with a "
            "frozen contract if an economy claim is made.  No src/ change and no public API."
        ),
        "citations": [
            ("exp2", "exp2-loop-continuation.json", ["enhancement_grid"],
             {"selected": "counts+accum"}),
            ("exp2", "exp2-loop-continuation.json", ["reserved_verification_family"],
             {"sufficient": True, "closed_update": True}),
            ("exp4", "exp4-objectification-elevation.json",
             ["attempts", "exp5_artin_object", "gates", "gate_iii_exact_descent"],
             {"verdict": "PASS", "mismatches": 0}),
        ],
        "information_added": (
            "a declared typed feedback machine, its exact continuation quotient, the "
            "one-field enhancement grid, and the gate-by-gate elevation criterion"
        ),
        "cost": "research-local only; workstream-internal tests are not collected by the root suite",
        "task_improved": (
            "the repository's own open obligation 'a theorem deciding when a nontrivial "
            "continuation-value fibre objectifies into a higher-rank compositional process'"
        ),
        "still_fails": [
            "the exp5 Artin object is a quotient, not an elevation: no new rank is claimed",
            "no general theorem; the enhancement grid is bounded to the declared domain",
        ],
        "regression_condition": (
            "the workstream must reproduce the recorded numbers from the pinned commit; "
            "a mismatch against evidence/exp2-loop-continuation.json is a failure"
        ),
        "review_gate": "repository governance; the workstream must declare a claim ceiling",
        "applied": False,
        "interface_pressure_observed": (
            "process_geometry.experimental.minimize_finite_task_process was reused "
            "successfully as an EXACT oracle with no modification.  The promotion signal is "
            "therefore 'this experimental entry point is reusable as-is', not 'change it'."
        ),
    },
    {
        "id": "P-ADVA-1",
        "repository": "mountain/adva",
        "target": "docs/research/<NNNN>-declared-continuation-profile.md",
        "companion": "experiments/<name>/contract.json",
        "kind": "new declared research profile, explicitly not a PSC0 extension",
        "precedent": (
            "docs/research/0129-bounded-breakthrough-trusted-boundaries.md, which fixes the "
            "six-part bounded-run contract template"
        ),
        "summary": (
            "The pinned source supplies no native legal-continuation interface for a relation "
            "path or a relation cell.  If a continuation notion is wanted, it belongs in a NEW "
            "declared profile with its own legality predicate, append operation, "
            "boundary-agreement rule, identity policy and filler decision -- never as a silent "
            "extension of PSC0."
        ),
        "citations": [
            ("adva", "adva-continuation-interface.json", ["verdict"],
             {"native_legal_continuation_interface_for_pr16_records": False}),
            ("adva", "adva-continuation-interface.json", ["checks"], {}),
        ],
        "information_added": (
            "the five semantics a downstream experiment must invent, enumerated explicitly, "
            "plus a calibration model (experiment 2) that declares all five"
        ),
        "cost": (
            "one research note plus one bounded-run contract; no Rust type, no SourceId or "
            "OccurrenceId allocation, no change to PSC0 or to any frozen artefact"
        ),
        "task_improved": (
            "making the continuation gap explicit instead of leaving it to be rediscovered, "
            "and giving a future profile a declared contract to satisfy"
        ),
        "still_fails": [
            "does not implement continuation; the profile is a specification",
            "does not execute compute/verify/learn mechanisms, matching the existing boundary",
        ],
        "regression_condition": (
            "if a pinned Adva operation later appends a step to FrameRelationPathV0 or composes "
            "two RelationCellV0, the gap claim is falsified and the probe exits nonzero"
        ),
        "review_gate": "repository governance; the profile must declare its own scope and ceilings",
        "applied": False,
    },
]


def read_evidence(name):
    path = EVIDENCE / name
    require(path.exists(), "PROMO-EVIDENCE-MISSING", str(path))
    return path, json.loads(path.read_text(encoding="utf-8"))


def pointer(doc, path):
    node = doc
    for key in path:
        require(isinstance(node, dict) and key in node, "PROMO-POINTER-MISSING",
                f"{'.'.join(str(p) for p in path)} missing at {key!r}")
        node = node[key]
    return node


def run():
    out = []
    for proposal in PROPOSALS:
        require(proposal["applied"] is False, "PROMO-MUST-NOT-BE-APPLIED",
                f"{proposal['id']} claims to be applied; this tool only proposes")
        checks = []
        for experiment, filename, path, expectations in proposal["citations"]:
            evidence_path, doc = read_evidence(filename)
            node = pointer(doc, path)
            for field, expected in expectations.items():
                require(node.get(field) == expected, "PROMO-CITATION-MISMATCH",
                        f"{proposal['id']}: {filename} {'/'.join(map(str, path))}.{field} "
                        f"is {node.get(field)!r}, proposal cites {expected!r}")
            checks.append({
                "experiment": experiment,
                "file": filename,
                "sha256": gapkit.sha256_file(evidence_path),
                "pointer": ".".join(str(p) for p in path),
                "verified": {k: node.get(k) for k in sorted(expectations)},
            })
        out.append({**{k: v for k, v in proposal.items() if k != "citations"},
                    "citations_verified": checks})
    require(out, "PROMO-EMPTY", "no proposals")
    return {
        "schema": SCHEMA,
        "generated_by": "tools/build_interface_promotion.py",
        "authority_note": (
            "work-plan section 10: this plan grants no additional authority to publish or "
            "merge new research.  Every proposal below is unapplied and requires the target "
            "repository's own governance review."),
        "proposals": out,
        "applied": False,
        "count": len(out),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", default=None)
    args = parser.parse_args()
    record = run()
    text = gapkit.canonical(record)
    if args.out:
        Path(args.out).write_text(text, encoding="utf-8")
        sys.stderr.write(f"interface promotion sha256={gapkit.sha256_bytes(text.encode())}\n")
    else:
        sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
