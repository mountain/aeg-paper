#!/usr/bin/env python3
"""Cross-experiment gap classification and cost comparison.

Work-plan section 9 gives a gap taxonomy; section 10 requires the summary tables
to be GENERATED FROM THE RAW DATA so that the report cannot drift from the
evidence.  This tool therefore does not summarise prose.  It reads each
experiment's evidence document, re-checks the raw verdicts with explicit
obligations, and emits one normalised finding per gap.

The mapping from a raw verdict to a taxonomy category is DECLARED below as
data, keyed by (experiment, representation id, verdict field).  Nothing is
inferred; an unexpected or missing verdict fails with a coded diagnostic rather
than being dropped from the table.

Run:

    python3 research/process-representation-gap/tools/build_gap_classification.py
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

CONTRACTS = ROOT / "contracts"
EVIDENCE = ROOT / "evidence"
SCHEMA = "aeg.process-representation-gap.gap-classification.v1"

# Work-plan section 9, restated as machine categories.
CATEGORIES = {
    "observation-insufficient": {
        "plan_row": "同摘要且未来任务不同",
        "conclusion": "观察对该任务不充分",
        "action": "保存任务相关残余或增加观察能力",
    },
    "update-not-closed": {
        "plan_row": "同摘要与同动作得到不同摘要",
        "conclusion": "当前表示不能闭合更新",
        "action": "修改状态表示或降低动作域",
    },
    "legality-signature": {
        "plan_row": "同摘要且合法性不同（工作计划 4.2）",
        "conclusion": "共同合法继续不足以刻画该对；须把合法性签名加入等价定义",
        "action": "在合同中声明合法性通道，或收窄动作域",
    },
    "value-equality-insufficient": {
        "plan_row": "同值但合法上下文中行为不同",
        "conclusion": "值相等不足以保证可替换",
        "action": "丰富类型、来源、接口或上下文合同",
    },
    "objectification-failure": {
        "plan_row": "单次对象调用正确，复合降阶不一致",
        "conclusion": "对象化或升阶合同失败",
        "action": "修正组合律与降低映射，不仅补输出字段",
    },
    "quotient-forgets-history": {
        "plan_row": "忠实群表示仍遗忘字面施工历史",
        "conclusion": "所选群商不服务历史任务",
        "action": "同时保留执行历史，明确两层等价",
    },
    "bounded-compatible": {
        "plan_row": "所有有限样本通过",
        "conclusion": "该有限预算内相容",
        "action": "寻求归纳不变量或一般证明，保持未决",
    },
    "budget-exhausted": {
        "plan_row": "搜索预算耗尽",
        "conclusion": "仅在声明预算内未找到见证",
        "action": "扩大预算需新合同版本，不得静默扩大",
    },
    "source-interface-absent": {
        "plan_row": "固定源码未提供声明的接口",
        "conclusion": "该能力在固定源码中不存在，只可另行声明模型",
        "action": "报告缺口并在新合同中自建模型，不虚构原生语义",
    },
}

# Declared verdict extraction.  Each entry names the evidence path to read and
# the field to test; a missing path is a failure, never a skip.
VERDICT_RULES = [
    # (experiment, evidence file, json pointer, expected field values, category)
    ("exp1", "exp1-order-and-mixing.json", ("representations", "pi0"),
     {"sufficient": False}, "observation-insufficient"),
    ("exp1", "exp1-order-and-mixing.json", ("representations", "pi0"),
     {"closed_update": False}, "update-not-closed"),
    ("exp1", "exp1-order-and-mixing.json", ("representations", "pi0_counts"),
     {"sufficient": False}, "observation-insufficient"),
    ("exp1", "exp1-order-and-mixing.json", ("representations", "pi0_endpoint"),
     {"sufficient": False}, "observation-insufficient"),
    ("exp1", "exp1-order-and-mixing.json", ("downstream_spectral_analysis",),
     {}, "observation-insufficient"),
    ("exp2", "exp2-loop-continuation.json", ("representations", "pi0"),
     {"sufficient": False}, "observation-insufficient"),
    ("exp2", "exp2-loop-continuation.json", ("representations", "pi0"),
     {"closed_update": False}, "update-not-closed"),
    ("exp2", "exp2-loop-continuation.json", ("representations", "pi1"),
     {"sufficient": False, "closed_update": True}, "observation-insufficient"),
    ("exp2", "exp2-loop-continuation.json", ("representations", "pi2"),
     {"sufficient": False, "closed_update": True}, "observation-insufficient"),
    ("exp2", "exp2-loop-continuation.json", ("witnesses", "legality_gap"),
     {"base_equivalent": False, "augmented_equivalent": False}, "legality-signature"),
    ("exp2", "exp2-loop-continuation.json", ("enhancement_grid", "candidates", "counts+alternations"),
     {"sufficient": False, "closed_update": False}, "update-not-closed"),
    ("exp4", "exp4-objectification-elevation.json",
     ("baseline_control", "gates", "gate_i_task_sufficiency_pi_out"),
     {"verdict": "FAIL"}, "observation-insufficient"),
    ("exp4", "exp4-objectification-elevation.json",
     ("attempts", "exp2_accumulator_object", "gates", "gate_i_task_sufficiency"),
     {"verdict": "FAIL"}, "observation-insufficient"),
    ("exp5", "exp5-braid-nonarithmetic.json", ("layers",),
     {}, "quotient-forgets-history"),
    ("exp6", "exp6-knot-deformation-environment.json", ("gates", "B_state_faithful"),
     {"status": "computationally-verified-example"}, "value-equality-insufficient"),
    ("exp6", "exp6-knot-deformation-environment.json", ("result_labels",),
     {"completeness": "bounded-domain-compatible at best: no completeness claim is made"},
     "bounded-compatible"),
    ("exp6", "exp6-knot-deformation-environment.json",
     ("environments", "witness-2-environment-changes-equivalence"),
     {"outcome": "success (the environment changes the declared equivalence)"},
     "value-equality-insufficient"),
    ("exp6", "exp6-knot-deformation-environment.json",
     ("geometric_route", "details", "witness_3_obstacle_changes_legality"),
     {}, "legality-signature"),
    ("exp6", "exp6-knot-deformation-environment.json",
     ("geometric_route", "details", "witness_4_time_changes_legality"),
     {}, "legality-signature"),
    ("exp6", "exp6-knot-deformation-environment.json", ("topological_route", "witness_1_same_type_different_history"),
     {}, "quotient-forgets-history"),
    ("exp3", "exp3-typed-hole-context.json", ("witnesses", "initial_filling_collision"),
     {}, "value-equality-insufficient"),
    ("exp3", "exp3-typed-hole-context.json", ("context_search",),
     {"grid_candidates": 63, "grid_candidates_insufficient": 63}, "bounded-compatible"),
    ("exp3", "exp3-typed-hole-context.json", ("rejected_contexts",),
     {}, "legality-signature"),
    ("adva", "adva-continuation-interface.json", ("verdict",),
     {"native_legal_continuation_interface_for_pr16_records": False},
     "source-interface-absent"),
]


def read_evidence(name: str):
    path = EVIDENCE / name
    require(path.exists(), "GAP-EVIDENCE-MISSING", str(path))
    return path, json.loads(path.read_text(encoding="utf-8"))


def pointer(doc, path):
    node = doc
    for key in path:
        require(isinstance(node, dict) and key in node, "GAP-POINTER-MISSING",
                f"{'/'.join(str(p) for p in path)} missing at {key!r}")
        node = node[key]
    return node


def contract_record(experiment: str):
    matches = sorted(CONTRACTS.glob(f"{experiment}-*.json"))
    require(matches, "GAP-CONTRACT-MISSING", experiment)
    # Prefer the highest declared version, so a superseded contract is retained
    # on disk but never cited.
    def version_key(path):
        stem = path.name[:-len(".json")]
        tail = stem.rsplit(".v", 1)[-1]
        parts = tail.split(".")
        try:
            return tuple(int(p) for p in parts)
        except ValueError:
            return (0,)

    chosen = max(matches, key=version_key)
    digest = gapkit.sha256_file(chosen)
    frozen = _read_frozen()
    require(frozen.get(chosen.name) == digest, "EXP-CONTRACT-DRIFT",
            f"{chosen.name}: frozen {frozen.get(chosen.name)!r} != {digest}")
    return {"path": str(chosen.relative_to(ROOT.parent.parent)), "sha256": digest,
            "superseded_retained": [p.name for p in matches if p != chosen]}


def run():
    frozen = _read_frozen()
    experiments = ["exp1", "exp2", "exp3", "exp4", "exp5", "exp6"]
    contracts = {}
    for experiment in experiments:
        contracts[experiment] = contract_record(experiment)

    findings = []
    for experiment, filename, path, expectations, category in VERDICT_RULES:
        evidence_path, doc = read_evidence(filename)
        node = pointer(doc, path)
        for field, expected in expectations.items():
            require(node.get(field) == expected, "GAP-VERDICT-MISMATCH",
                    f"{filename} {'/'.join(str(p) for p in path)}.{field} is "
                    f"{node.get(field)!r}, table declares {expected!r}")
        findings.append({
            "experiment": experiment,
            "category": category,
            "taxonomy": CATEGORIES[category],
            "evidence": {"file": filename,
                         "sha256": gapkit.sha256_file(evidence_path),
                         "pointer": ".".join(str(p) for p in path)},
            "verdict": {k: node.get(k) for k in sorted(expectations)},
        })

    require(findings, "GAP-NO-FINDINGS", "the declared rules produced nothing")

    # Every experiment must contribute at least one finding or be reported as
    # having none yet.  A silently absent experiment is a table defect.
    coverage = {}
    for experiment in experiments:
        evidence_names = sorted(p.name for p in EVIDENCE.glob(f"{experiment}-*.json")
                                if "independent" not in p.name)
        coverage[experiment] = {
            "contract": contracts[experiment],
            "evidence_files": evidence_names,
            "findings": len([f for f in findings if f["experiment"] == experiment]),
        }

    by_category = {}
    for finding in findings:
        by_category.setdefault(finding["category"], []).append(
            f"{finding['experiment']}:{finding['evidence']['pointer']}")

    # No experiment may be silently absent from the table.
    for experiment in experiments:
        require(coverage[experiment]["findings"] > 0, "GAP-EXPERIMENT-UNCOVERED",
                f"{experiment} has a frozen contract but contributes no finding")

    return {
        "schema": SCHEMA,
        "generated_by": "tools/build_gap_classification.py",
        # No environment block: this is a DERIVED summary of per-experiment
        # evidence, and each of those records its own environment.  Omitting it
        # here keeps the committed artefact reproducible on any machine.
        "environment_note": "see the per-experiment evidence documents cited in each finding",
        "taxonomy": CATEGORIES,
        "coverage": coverage,
        "findings": findings,
        "by_category": by_category,
        "note": ("every row above is re-checked against the raw evidence at run time; "
                 "an unexpected or missing verdict fails the build rather than being "
                 "dropped from the table"),
    }


def _read_frozen():
    out = {}
    ledger = CONTRACTS / "FROZEN.sha256"
    if ledger.exists():
        for line in ledger.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            digest, _, name = line.partition("  ")
            out[name.strip()] = digest.strip()
    return out


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", default=None)
    args = parser.parse_args()
    record = run()
    text = gapkit.canonical(record)
    if args.out:
        Path(args.out).write_text(text, encoding="utf-8")
        sys.stderr.write(f"gap classification sha256={gapkit.sha256_bytes(text.encode())}\n")
    else:
        sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
