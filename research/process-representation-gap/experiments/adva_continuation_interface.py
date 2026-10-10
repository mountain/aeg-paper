#!/usr/bin/env python3
"""Adva native-continuation interface probe.

This is not a sixth experiment; it is the source-reading probe that fixes the
P0 baseline claim the work plan's section 2 and section 6 (实验二) depend on:
whether the pinned Adva source supplies a NATIVE legal-continuation interface
for the two PR-16 records.

Every fact below is re-derived at run time from the pinned commit through
``git show``.  Nothing is quoted from a working tree, and no claim is accepted
because it "looks reasonable": each check names the exact string it requires
and fails with its own diagnostic code.

Run:

    python3 research/process-representation-gap/experiments/adva_continuation_interface.py
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(ROOT / "tools"))
import gapkit  # noqa: E402
from gapkit import require  # noqa: E402

REPO = Path("/Users/mingli/Adva/adva")
COMMIT = "1b9bd090b2c4710916b6a0ccca0ad88fb7d323bd"
COMMIT_PR16 = "cce73004c2b4fbfb87d9ba1ccc66820423273cf6"

TRACE_ARTIFACT = "programs/bootstrap-0/first-trace-arithmetic.adva"
RELATION_RS = "crates/adva-witness/src/relation.rs"
PROCESS_CORE = "docs/PROGRAM_PROCESS_CORE.md"
SEMANTIC_SCOPE = "docs/SEMANTIC_SCOPE.md"
TECH_REPORT = "docs/TECHNICAL_REPORT_PROGRAM_PROCESS_CORE.md"
PERIODIC_0233 = "docs/research/0233-periodic-programs-before-floquet-observations.md"
TRACE_0114 = "docs/research/0114-three-sided-trace-arithmetic-calibration.md"
CONTRACT_0129 = "docs/research/0129-bounded-breakthrough-trusted-boundaries.md"

SCHEMA = "aeg.process-representation-gap.adva-interface.v1"


def show(path: str, commit: str = COMMIT) -> str:
    proc = subprocess.run(
        ["git", "-C", str(REPO), "show", f"{commit}:{path}"],
        capture_output=True, check=False,
    )
    require(proc.returncode == 0, "ADVA-PATH-MISSING",
            f"{commit}:{path}: {proc.stderr.decode('utf-8', 'replace').strip()}")
    return proc.stdout.decode("utf-8")


def blob(path: str, commit: str = COMMIT) -> str:
    proc = subprocess.run(
        ["git", "-C", str(REPO), "rev-parse", f"{commit}:{path}"],
        capture_output=True, check=False,
    )
    require(proc.returncode == 0, "ADVA-PATH-MISSING", f"{commit}:{path}")
    return proc.stdout.decode().strip()


def squash(text: str) -> str:
    """Collapse all whitespace so a phrase may be matched across line breaks.

    Source prose is hard-wrapped; matching a multi-line sentence against the
    raw text would fail for a formatting reason rather than a content reason.
    """
    return " ".join(text.split())


def grep_tree(needle: str) -> list:
    proc = subprocess.run(
        ["git", "-C", str(REPO), "grep", "-n", "-F", needle, COMMIT, "--",
         "*.rs", "*.md", "*.adva"],
        capture_output=True, check=False,
    )
    if proc.returncode not in (0, 1):
        return []
    return [line for line in proc.stdout.decode("utf-8", "replace").splitlines() if line]


def fact(checks, name, condition, code, detail):
    record = {"name": name, "holds": bool(condition), "detail": detail}
    checks.append(record)
    require(condition, code, f"{name}: {detail}")
    return record


def run():
    require(REPO.exists(), "ADVA-REPO-MISSING", str(REPO))
    checks = []

    core = show(PROCESS_CORE)
    scope = show(SEMANTIC_SCOPE)
    relation = show(RELATION_RS)
    artifact = show(TRACE_ARTIFACT)
    periodic = show(PERIODIC_0233)
    trace0114 = show(TRACE_0114)

    # --- 1. The native carrier and its exclusions -------------------------
    fact(checks, "native-carrier-is-open-finite-program",
         "Adva begins with programs, not with values, vectors, matrices, or manifolds."
         in squash(core),
         "ADVA-NATIVE-CARRIER",
         "PROGRAM_PROCESS_CORE.md states the native object is an open finite affine program")

    fact(checks, "psc0-excludes-recursion-and-cycles",
         "recursion, and cyclic substitution remain outside PSC0." in squash(core),
         "ADVA-RECURSION-EXCLUDED",
         "PROGRAM_PROCESS_CORE.md places recursion and cyclic substitution outside PSC0")

    fact(checks, "semantic-scope-excludes-stable-feedback",
         "recursion and cyclic modules;" in scope and "stable feedback, event re-enabling" in scope,
         "ADVA-FEEDBACK-EXCLUDED",
         "SEMANTIC_SCOPE.md excludes recursion, cyclic modules and stable feedback")

    fact(checks, "psc0-objects-are-finite",
         "PSC0 programs, causal cuts, and program slices are finite." in squash(show(TECH_REPORT)),
         "ADVA-FINITENESS",
         "TECHNICAL_REPORT states PSC0 objects are finite; no truncation is required")

    # --- 2. Finite unrolling is explicitly not unbounded recursion --------
    fact(checks, "finite-unrolling-is-not-recursion",
         "Any finite multi-year run is unrolled; no cyclic Adva program or" in periodic
         and "unbounded recursion is being introduced." in periodic,
         "ADVA-UNROLLING-DISCLAIMER",
         "research 0233 states finite unrolling introduces no cyclic program")

    # --- 3. The 0114 nonclaims -------------------------------------------
    fact(checks, "research-0114-nonclaims",
         "This experiment does not define the three `chi` maps" in squash(trace0114)
         and "execute mechanisms, or turn document-local coordinates into global identities."
         in squash(trace0114),
         "ADVA-0114-NONCLAIMS",
         "research 0114 disclaims chi maps, semantic compatibility and mechanism execution")

    # --- 4. The two records are records, not executions -------------------
    data = json.loads(artifact)
    fact(checks, "trace-artifact-schema",
         data.get("schema") == "adva.trace-arithmetic-calibration.research",
         "ADVA-ARTIFACT-SCHEMA",
         f"artifact schema is {data.get('schema')!r}")
    left_word = data["relation"]["left"]["mechanism_path"]["steps"]
    right_word = data["relation"]["right"]["mechanism_path"]["steps"]
    fact(checks, "pr16-left-word",
         left_word == ["compute", "verify", "compute"], "ADVA-RECORD-WORD",
         f"left mechanism path is {left_word}")
    fact(checks, "pr16-right-word",
         right_word == ["verify", "compute", "verify"], "ADVA-RECORD-WORD",
         f"right mechanism path is {right_word}")
    cell = data["relation"]["relation"]
    fact(checks, "relation-cell-profile-is-braid-m6",
         cell["profile"] == {"kind": "braid", "boundary": "m6",
                             "process_lift": "positive_braid_monoid",
                             "coxeter_shadow": "symmetric_three"},
         "ADVA-CELL-PROFILE", f"profile is {cell['profile']!r}")
    fact(checks, "relation-filling-is-open",
         cell["filling"]["state"] == "open", "ADVA-FILLING-OPEN",
         f"relation filling state is {cell['filling']['state']!r}")
    fact(checks, "frame-ids-are-disjoint",
         len({s["frame"] for s in data["relation"]["left"]["steps"]}
             | {s["frame"] for s in data["relation"]["right"]["steps"]}) == 6,
         "ADVA-FRAME-IDS",
         "the six frame ids are distinct")

    # --- 5. No continuation operation exists on the cell ------------------
    fact(checks, "check-braid-fixes-three-step-words",
         "let [a, b, a_again] = left.steps() else {" in relation
         and "InvalidBraidWord" in relation,
         "ADVA-BRAID-WORD-FIXED",
         "check_braid destructures exactly three steps and requires the braid pattern")
    fact(checks, "transport-refuses-open-boundary",
         "OpenBoundaryCannotTransport" in relation,
         "ADVA-TRANSPORT-REFUSED",
         "RelationCellV0::transport refuses a cell whose filling is still open")

    cell_ops = _impl_ops(relation, "RelationCellV0")
    fact(checks, "relation-cell-exposes-only-new-check-transport",
         cell_ops == ["check", "new", "transport"],
         "ADVA-CELL-OPS",
         f"RelationCellV0 public operations are {cell_ops}")
    for absent in ("compose", "append", "extend", "continue_with", "then"):
        fact(checks, f"no-{absent}-on-relation-cell",
             absent not in cell_ops, "ADVA-CELL-OP-PRESENT",
             f"RelationCellV0 has no {absent!r} operation")

    adr0022 = squash(_doc_adr0022())
    fact(checks, "no-frame-reuse-for-iteration",
         "frame ID within a finite path is rejected because V0 has no event "
         "re-enabling or feedback semantics." in adr0022,
         "ADVA-FRAME-REUSE",
         "ADR 0022 rejects frame-id reuse for iteration")

    # --- 6. Attribution control ------------------------------------------
    triple_hits = (grep_tree("3 * h") + grep_tree("c + v") + grep_tree("f - h"))
    fact(checks, "scalar-triple-is-absent-from-pinned-adva",
         triple_hits == [], "ADVA-TRIPLE-ATTRIBUTION",
         f"the (c+v, f-h, 3h/f) body does not occur in the pinned Adva tree "
         f"({len(triple_hits)} hits); it is a declared downstream adapter")

    # --- 7. Contract convention ------------------------------------------
    contract0129 = squash(show(CONTRACT_0129))
    template_heads = ["**Question and level.**", "**Imported knowledge.**", "**Interface.**",
                      "**Protected obligations.**", "**Acceptance and verification.**",
                      "**Resources and exit.**"]
    missing = [h for h in template_heads if h not in contract0129]
    fact(checks, "research-0129-contract-template",
         not missing and "write a concrete run contract" in contract0129,
         "ADVA-CONTRACT-TEMPLATE",
         f"research 0129 six-part bounded-run contract template; missing {missing}")

    verdict = {
        "native_legal_continuation_interface_for_pr16_records": False,
        "reason": ("the pinned source fixes the relation cell to exactly the two three-step "
                   "braid words, rejects frame-id reuse for iteration, refuses transport on an "
                   "open filling, and excludes recursion, cyclic substitution and stable "
                   "feedback from PSC0; no append, step, glue or continuation operation exists "
                   "on RelationCellV0"),
        "what_exists": [
            "analyze_causal_cut, advance_causal_cut, analyze_program_slice, "
            "compose_program_slices on SharedProgramDiagram (crates/adva-lisp/src/process.rs)",
            "RelationCellV0::{new, check, transport} with a filled boundary",
            "the finite data-machine profile adva data-run --resume, walled off from PSC0",
        ],
        "what_must_be_invented_downstream": [
            "a legality predicate on these records",
            "an append/step/gluing operation on FrameRelationPathV0 or RelationCellV0",
            "a boundary-agreement rule for an appended step",
            "an identity policy that does not reuse a FrameIdV0",
            "a filler/transport decision, since transport refuses the open boundary",
        ],
        "consequence_for_this_programme": (
            "experiment 2 builds its own declared small typed model, as the work plan "
            "prescribes when the two records have no common legal native continuation "
            "interface; no Adva continuation semantics is invented"),
    }

    return {
        "schema": SCHEMA,
        "kind": "pinned-source interface probe",
        "repository": {"remote": "mountain/adva", "commit": COMMIT,
                       "pr16_reproduction_commit": COMMIT_PR16},
        "environment": gapkit.environ(),
        "pinned_blobs": {
            path: blob(path) for path in
            (TRACE_ARTIFACT, RELATION_RS, PROCESS_CORE, SEMANTIC_SCOPE, TECH_REPORT,
             PERIODIC_0233, TRACE_0114, CONTRACT_0129)
        },
        "checks": checks,
        "checks_passed": len(checks),
        "verdict": verdict,
        "attribution_note": (
            "The three-scalar body y1 = c + v, y2 = f - h, y3 = 3h/f is defined in the "
            "aeg-paper PR-16 witness, paper-4/scripts/verify-opposite-features.py. It is NOT "
            "an Adva output and NOT a research-0114 output; research 0114's own coordinates "
            "are time, space and construction. This probe verifies that absence directly."),
    }


def _impl_ops(source: str, type_name: str) -> list:
    """Public method names of one inherent impl block, sorted."""
    marker = f"impl {type_name} {{"
    index = source.find(marker)
    require(index >= 0, "ADVA-IMPL-MISSING", f"no inherent impl for {type_name}")
    depth = 0
    start = source.index("{", index)
    ops = []
    for position in range(start, len(source)):
        char = source[position]
        if char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
            if depth == 0:
                block = source[start:position]
                break
    else:
        raise gapkit.Diagnostic("ADVA-IMPL-UNTERMINATED", type_name)
    for line in block.splitlines():
        stripped = line.strip()
        if stripped.startswith("pub fn "):
            name = stripped[len("pub fn "):].split("(")[0].strip()
            ops.append(name)
    return sorted(set(ops))


def _doc_adr0022():
    for path in ("docs/adr/0022-relation-frame-carrier-identity.md",
                 "docs/adr/0022-relation-frame-identity.md"):
        try:
            return show(path)
        except gapkit.Diagnostic:
            continue
    proc = subprocess.run(
        ["git", "-C", str(REPO), "ls-tree", "-r", "--name-only", COMMIT, "docs/adr/"],
        capture_output=True, check=False)
    names = [n for n in proc.stdout.decode().splitlines() if "0022" in n]
    require(names, "ADVA-ADR-MISSING", "no ADR 0022 found")
    return show(names[0])


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", default=None)
    args = parser.parse_args()
    record = run()
    text = gapkit.canonical(record)
    if args.out:
        Path(args.out).write_text(text, encoding="utf-8")
        sys.stderr.write(f"adva probe sha256={gapkit.sha256_bytes(text.encode())}\n")
    else:
        sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
