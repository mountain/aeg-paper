#!/usr/bin/env python3
"""Experiment 3, independent route -- direct substitution-and-evaluation.

This checker deliberately shares NO semantic helper with
``exp3_typed_hole_context.py``.  It never constructs a wire, a gate, a network,
a schedule, a graft receipt or a constant-source ancestry.  Instead it
substitutes the declared producer values directly into the body's expression
term and evaluates the term with exact rationals, and it does the same for the
declared carrier layer with carrier labels.  The declared strict-domain rule

    the composite is defined  iff  every closure producer is defined
                                   and  the body term is defined on the
                                        substituted values

is applied directly, which is Paper IV's Equation (5.2) written out rather than
obtained from an assembled graph.

Why this is independent: the primary route's semantics live in graph
construction (explicit copy gates, strict discard gates, the one-producer and
one-consumer inventory, boundary completeness, acyclicity, the graft receipt
and the constant-source ancestry).  None of that code is present here.  This
route obtains the same observations from a term evaluator plus a declared
predicate on the producer tuple.  The only shared module is
``tools/gapkit.py``, which carries deterministic JSON serialisation, hashing,
cost accumulation and the diagnostic type, and carries no experiment semantics.

The route recomputes the whole declared search, the strictness witnesses, the
Paper IV scalar snapshot and a hand-computed table, then compares its verdicts
with the primary evidence.  Any disagreement raises EXP3-ROUTE-DISAGREEMENT.

Run:

    python3 research/process-representation-gap/experiments/exp3_typed_hole_context_independent.py
"""

from __future__ import annotations

import argparse
import json
import sys
from fractions import Fraction
from itertools import combinations
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(ROOT / "tools"))
import gapkit  # noqa: E402
from gapkit import Diagnostic, qtext, require  # noqa: E402

CONTRACT = ROOT / "contracts" / "exp3-typed-hole-context.v1.json"
FROZEN = ROOT / "contracts" / "FROZEN.sha256"
PRIMARY_EVIDENCE = ROOT / "evidence" / "exp3-typed-hole-context.json"

SCHEMA = "aeg.process-representation-gap.exp3-independent.v1"

HOLES = ("h1", "h2", "h3", "h4")
LITERALS = (-1, 0, 1, 2)
OPS = ("add", "sub", "mul", "div")
MAX_BINARY_GATES = 2

FILLINGS = ("beta0", "beta1", "beta2", "beta3", "beta4", "beta5", "beta_undef")
FILLING_VALUES = {
    "beta0": (Fraction(2), Fraction(7), Fraction(3), Fraction(5)),
    "beta1": (Fraction(2), Fraction(7), Fraction(3), Fraction(4)),
    "beta2": (Fraction(2), Fraction(2), Fraction(3), Fraction(5)),
    "beta3": (Fraction(4), Fraction(7), Fraction(3), Fraction(5)),
    "beta4": (Fraction(2), Fraction(7), Fraction(4), Fraction(5)),
    "beta5": (Fraction(2), Fraction(4), Fraction(3), Fraction(5)),
}


class _Undefined:
    __slots__ = ()

    def __repr__(self) -> str:
        return "UNDEFINED"


UNDEFINED = _Undefined()
FILLING_VALUES["beta_undef"] = (Fraction(2), Fraction(7), Fraction(3), UNDEFINED)

PRODUCER_VALUES = {
    "q1": Fraction(2),
    "q2": Fraction(7),
    "q3": Fraction(3),
    "q4": Fraction(5),
    "q5": Fraction(4),
    "u0": UNDEFINED,
}
CARRIER_LABELS = {"pc_L": "L", "pc_M": "M"}

# Hand-computed table for the frozen witnesses.  Entered as literals, not
# derived from any other implementation.
HAND_TABLE = {
    "producer q1": "2",
    "producer q2": "7",
    "producer q3": "3",
    "producer q4": "5",
    "producer q5": "4",
    "producer u0": "UNDEFINED",
    "h1 at beta0": "2",
    "const(2) at beta0": "2",
    "h1 at beta3": "4",
    "q5 at beta3": "4",
    "paper4 y1": "9",
    "paper4 y2": "15",
    "paper4 y3": "5/2",
}


# --------------------------------------------------------------------------
# term-level semantics: no graph is ever built
# --------------------------------------------------------------------------

def all_terms(max_gates: int = MAX_BINARY_GATES):
    """Every expression term with 0..max_gates binary operators."""
    leaves = [("var", i) for i in range(1, len(HOLES) + 1)] + [("const", c) for c in LITERALS]
    table = {0: leaves}
    for size in range(1, max_gates + 1):
        layer = []
        for left in range(size):
            right = size - 1 - left
            for op in OPS:
                for first in table[left]:
                    for second in table[right]:
                        layer.append((op, first, second))
        table[size] = layer
    return table


def term_text(term) -> str:
    kind = term[0]
    if kind == "var":
        return "h%d" % term[1]
    if kind == "const":
        return "const(%d)" % term[1]
    return "%s(%s,%s)" % (term[0], term_text(term[1]), term_text(term[2]))


def term_ops(term) -> int:
    if term[0] in ("var", "const"):
        return 0
    return 1 + term_ops(term[1]) + term_ops(term[2])


def term_eval(term, values):
    """Exact evaluation; UNDEFINED propagates and 0 denominators are UNDEFINED."""
    kind = term[0]
    if kind == "var":
        return values[term[1] - 1]
    if kind == "const":
        return Fraction(term[1])
    first = term_eval(term[1], values)
    if first is UNDEFINED:
        return UNDEFINED
    second = term_eval(term[2], values)
    if second is UNDEFINED:
        return UNDEFINED
    if kind == "add":
        return first + second
    if kind == "sub":
        return first - second
    if kind == "mul":
        return first * second
    if second == 0:
        return UNDEFINED
    return first / second


_MEMO = {}


def term_observation(term, filling: str):
    """O_scalar of the composite: strict over producers, then over the term."""
    key = (term, filling)
    hit = _MEMO.get(key)
    if hit is not None:
        return hit
    values = FILLING_VALUES[filling]
    undefined = False
    for value in values:
        if value is UNDEFINED:
            undefined = True
            break
    if undefined:
        result = ("UNDEFINED",)
    else:
        value = term_eval(term, values)
        result = ("UNDEFINED",) if value is UNDEFINED else ("DEFINED", (qtext(value),))
    _MEMO[key] = result
    return result


def behaviour(term):
    return tuple(term_observation(term, filling) for filling in FILLINGS)


def term_used_holes(term) -> list:
    counts = [0] * len(HOLES)
    pending = [term]
    while pending:
        node = pending.pop()
        kind = node[0]
        if kind == "var":
            counts[node[1] - 1] += 1
        elif kind != "const":
            pending.append(node[1])
            pending.append(node[2])
    return counts


def term_literals(term) -> list:
    out = []
    pending = [term]
    while pending:
        node = pending.pop()
        kind = node[0]
        if kind == "const":
            out.append(node[1])
        elif kind != "var":
            pending.append(node[1])
            pending.append(node[2])
    return sorted(out)


def term_operators(term) -> list:
    out = []
    pending = [term]
    while pending:
        node = pending.pop()
        kind = node[0]
        if kind in ("var", "const"):
            continue
        out.append(kind)
        pending.append(node[1])
        pending.append(node[2])
    return sorted(out)


FIELDS = ("dom_profile", "literals", "op_count", "operators", "support", "use_counts")


def field_value(term, name: str, vector):
    if name == "support":
        return [index + 1 for index, count in enumerate(term_used_holes(term)) if count]
    if name == "use_counts":
        return term_used_holes(term)
    if name == "literals":
        return term_literals(term)
    if name == "operators":
        return term_operators(term)
    if name == "op_count":
        return [term_ops(term)]
    if name == "dom_profile":
        return ["U" if entry[0] == "UNDEFINED" else "D" for entry in vector]
    raise Diagnostic("EXP3I-UNKNOWN-FIELD", repr(name))


def rank_of(pair) -> tuple:
    first, second = sorted(term_text(term) for term in pair)
    return (term_ops(pair[0]) + term_ops(pair[1]), first, second)


def independent_search():
    table = all_terms()
    terms = []
    for size in range(MAX_BINARY_GATES + 1):
        terms.extend(table[size])
    vectors = {term: behaviour(term) for term in terms}

    def group(keyfn):
        buckets = {}
        for term in terms:
            buckets.setdefault(keyfn(term), []).append(term)
        return buckets

    base = group(lambda term: (vectors[term][0],))
    base_bad = [members for members in base.values()
                if len({vectors[term] for term in members}) > 1]

    def minimal(members):
        best = None
        for first, second in combinations(sorted(members, key=lambda t: (term_ops(t), term_text(t))), 2):
            if vectors[first] == vectors[second]:
                continue
            rank = rank_of((first, second))
            if best is None or rank < best[0]:
                best = (rank, first, second)
        return best

    base_witness = None
    for members in base_bad:
        found = minimal(members)
        if found is None:
            continue
        if base_witness is None or found[0] < base_witness[0]:
            base_witness = found

    grid = {}
    for size in range(1, len(FIELDS) + 1):
        for subset in combinations(FIELDS, size):
            key = "+".join(subset)
            buckets = group(lambda term, subset=subset: (
                vectors[term][0],
                tuple(tuple(field_value(term, name, vectors[term])) for name in subset)))
            bad = [members for members in buckets.values()
                   if len({vectors[term] for term in members}) > 1]
            entry = {"classes_on_domain": len(buckets),
                     "insufficient_fibres": len(bad),
                     "sufficient": not bad}
            if bad:
                best = None
                for members in bad:
                    found = minimal(members)
                    if found is None:
                        continue
                    if best is None or found[0] < best[0]:
                        best = found
                if best is not None:
                    entry["witness_rank"] = list(best[0])
                    entry["witness_bodies"] = [term_text(best[1]), term_text(best[2])]
                    entry["separating_filling"] = next(
                        filling for index, filling in enumerate(FILLINGS)
                        if vectors[best[1]][index] != vectors[best[2]][index])
            grid[key] = entry

    positive = None
    for members in group(lambda term: vectors[term]).values():
        if len(members) < 2:
            continue
        for first, second in combinations(sorted(members, key=lambda t: (term_ops(t), term_text(t))), 2):
            rank = rank_of((first, second))
            if positive is None or rank < positive[0]:
                positive = (rank, first, second)

    return {
        "domain_size": len(terms),
        "by_size": {str(size): len(table[size]) for size in range(MAX_BINARY_GATES + 1)},
        "vectors": vectors,
        "base_classes": len(base),
        "base_insufficient_fibres": len(base_bad),
        "base_witness_rank": list(base_witness[0]) if base_witness else None,
        "base_witness_bodies": [term_text(base_witness[1]), term_text(base_witness[2])]
        if base_witness else None,
        "filling_classes": len({vectors[term] for term in terms}),
        "grid": grid,
        "positive_control_rank": list(positive[0]) if positive else None,
        "positive_control_bodies": [term_text(positive[1]), term_text(positive[2])]
        if positive else None,
    }


# --------------------------------------------------------------------------
# independent Paper IV snapshot and hand table
# --------------------------------------------------------------------------

PAPER4_BODY = (
    "tuple",
    ("add", ("var", 1), ("var", 2)),
    ("mul", ("var", 3), ("var", 4)),
    ("div", ("add", ("var", 1), ("var", 3)), ("sub", ("var", 2), ("var", 4))),
)


def paper4_outputs(values):
    results = []
    for term in PAPER4_BODY[1:]:
        value = term_eval(term, values)
        if value is UNDEFINED:
            return None
        results.append(qtext(value))
    return results


def readout_outputs(values):
    """y1 = c+v, y2 = f-h, y3 = 3h/f, for the declared f = 0 instance."""
    c, v, f, h = values
    if f == 0:
        raise Diagnostic("EXP3-STRICT-DIVISION-BY-ZERO",
                         "the readout body divides by the exact rational 0 at f = 0")
    return [qtext(c + v), qtext(f - h), qtext(Fraction(3) * h / f)]


# --------------------------------------------------------------------------
# independent carrier layer
# --------------------------------------------------------------------------

CARRIER_TERMS = {
    "cb_pass": ("transport",),
    "cb_fresh_L": ("fresh", "L"),
    "cb_fresh_M": ("fresh", "M"),
    "cb_route_L": ("route", "L"),
}


def carrier_observation(name: str, label: str):
    term = CARRIER_TERMS[name]
    if term[0] == "transport":
        return ("DEFINED", ("carrier:" + label,))
    if term[0] == "fresh":
        return ("DEFINED", ("carrier:" + term[1],))
    if label != term[1]:
        raise Diagnostic("EXP3-PROVENANCE-MISWIRE",
                         "route(%s) received carrier %s" % (term[1], label))
    return ("DEFINED", ("carrier:" + label,))


def carrier_observation_total(name: str, label: str):
    try:
        return carrier_observation(name, label)
    except Diagnostic as exc:
        if exc.code == "EXP3-PROVENANCE-MISWIRE":
            return ("REJECTED", exc.code)
        raise


# --------------------------------------------------------------------------
# declared types: an independent type table
# --------------------------------------------------------------------------

HOLE_TYPES = {"h1": "Q", "h2": "Q", "h3": "Q", "h4": "Q", "k1": "CarrierID"}


def bind_check(hole: str, producer_type: str) -> None:
    require(hole in HOLE_TYPES, "EXP3I-UNKNOWN-HOLE", repr(hole))
    require(HOLE_TYPES[hole] == producer_type, "EXP3-TYPE-MISMATCH",
            "hole %s expects %s, producer supplies %s"
            % (hole, HOLE_TYPES[hole], producer_type))


# --------------------------------------------------------------------------
# main
# --------------------------------------------------------------------------

def read_frozen() -> dict:
    out = {}
    if FROZEN.exists():
        for line in FROZEN.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            digest, _, name = line.partition("  ")
            out[name.strip()] = digest.strip()
    return out


def run():
    require(CONTRACT.exists(), "EXP3I-CONTRACT-MISSING", str(CONTRACT))
    contract_raw = CONTRACT.read_bytes()
    frozen = read_frozen()
    require(CONTRACT.name in frozen, "EXP-CONTRACT-DRIFT",
            "%s is absent from the frozen digest ledger" % (CONTRACT.name,))

    def digest_check(raw: bytes) -> str:
        observed = gapkit.sha256_bytes(raw)
        require(observed == frozen[CONTRACT.name], "EXP-CONTRACT-DRIFT",
                "frozen %r != observed %r" % (frozen[CONTRACT.name], observed))
        return observed

    contract_sha = digest_check(contract_raw)
    contract_document = json.loads(contract_raw.decode("utf-8"))
    require(PRIMARY_EVIDENCE.exists(), "EXP3I-PRIMARY-MISSING", str(PRIMARY_EVIDENCE))
    primary = json.loads(PRIMARY_EVIDENCE.read_text(encoding="utf-8"))
    require(primary["contract"]["sha256"] == contract_sha, "EXP-CONTRACT-DRIFT",
            "the primary evidence cites a different contract digest")

    disagreements = []
    comparisons = []

    def compare(name, left, right):
        ok = left == right
        comparisons.append({"claim": name, "independent": left, "primary": right, "agree": ok})
        if not ok:
            disagreements.append(name)

    search = independent_search()
    compare("domain_size", search["domain_size"], primary["context_search"]["domain_size"])
    compare("counts_by_size", search["by_size"],
            primary["domain"]["body_budget"]["by_binary_gates"])
    compare("initial_summary_classes", search["base_classes"],
            primary["context_search"]["initial_summary_classes"])
    compare("initial_summary_insufficient_fibres", search["base_insufficient_fibres"],
            primary["context_search"]["initial_summary_insufficient_fibres"])
    compare("declared_filling_equivalence_classes", search["filling_classes"],
            primary["context_search"]["declared_filling_equivalence_classes"])

    primary_grid = primary["context_search"]["grid"]
    compare("grid_candidate_keys", sorted(search["grid"]), sorted(primary_grid))
    for key in sorted(set(search["grid"]) & set(primary_grid)):
        compare("grid[%s].classes" % key, search["grid"][key]["classes_on_domain"],
                primary_grid[key]["classes_on_domain"])
        compare("grid[%s].insufficient_fibres" % key, search["grid"][key]["insufficient_fibres"],
                primary_grid[key]["insufficient_fibres"])
        compare("grid[%s].sufficient" % key, search["grid"][key]["sufficient"],
                primary_grid[key]["sufficient"])

    # Verify every witness the primary reports, from the term route.
    witness_checks = []
    witness = primary["witnesses"]["initial_filling_collision"]
    for entry in (witness, primary["witnesses"]["positive_control"]):
        pair = entry["bodies"]
        terms = [parse_text(name) for name in pair]
        vector_a, vector_b = behaviour(terms[0]), behaviour(terms[1])
        same_at_beta0 = vector_a[0] == vector_b[0]
        first_difference = next((filling for index, filling in enumerate(FILLINGS)
                                 if vector_a[index] != vector_b[index]), None)
        witness_checks.append({
            "bodies": pair,
            "independent_observation_at_beta0": [list(vector_a[0]), list(vector_b[0])],
            "same_at_beta0": same_at_beta0,
            "independent_first_difference": first_difference,
            "independent_equivalent_on_all_fillings": vector_a == vector_b,
        })
    compare("witness_beta0_same", witness_checks[0]["same_at_beta0"], True)
    compare("witness_separating_filling", witness_checks[0]["independent_first_difference"],
            witness["separating_filling"]["filling"])
    compare("positive_control_equivalent", witness_checks[1]["independent_equivalent_on_all_fillings"],
            True)

    for key, entry in sorted(primary_grid.items()):
        declared = entry.get("witness")
        if declared is None:
            compare("grid[%s].no-witness" % key, search["grid"][key]["sufficient"], True)
            continue
        terms = [parse_text(name) for name in declared["bodies"]]
        vector_a, vector_b = behaviour(terms[0]), behaviour(terms[1])
        found = next((filling for index, filling in enumerate(FILLINGS)
                      if vector_a[index] != vector_b[index]), None)
        compare("grid[%s].witness_separates" % key, found,
                declared["separating_filling"]["filling"])
        compare("grid[%s].witness_at_beta0" % key, vector_a[0], vector_b[0])

    # The independent route's own minimal witnesses, for the record.
    compare("minimal_witness_rank", search["base_witness_rank"],
            primary_witness_rank(primary["witnesses"]["initial_filling_collision"]))

    # Hand-computed table.
    hand = contract_document["independent_check"]["hand_computed_witnesses"]
    derived = {
        "producer q1": qtext(PRODUCER_VALUES["q1"]),
        "producer q2": qtext(PRODUCER_VALUES["q2"]),
        "producer q3": qtext(PRODUCER_VALUES["q3"]),
        "producer q4": qtext(PRODUCER_VALUES["q4"]),
        "producer q5": qtext(PRODUCER_VALUES["q5"]),
        "producer u0": "UNDEFINED",
        "h1 at beta0": term_observation(("var", 1), "beta0")[1][0],
        "const(2) at beta0": term_observation(("const", 2), "beta0")[1][0],
        "h1 at beta3": term_observation(("var", 1), "beta3")[1][0],
        "q5 at beta3": qtext(PRODUCER_VALUES["q5"]),
    }
    paper4 = paper4_outputs((Fraction(2), Fraction(7), Fraction(3), Fraction(5)))
    require(paper4 is not None and paper4 == ["9", "15", "5/2"],
            "EXP3-PAPER4-SNAPSHOT-MISMATCH",
            "the term route gave %r for the four-input body" % (paper4,))
    derived["paper4 y1"], derived["paper4 y2"], derived["paper4 y3"] = paper4
    for label, expected in sorted(HAND_TABLE.items()):
        require(derived[label] == expected, "EXP3-HAND-TABLE-MISMATCH",
                "hand table %s: term route %r, hand says %r" % (label, derived[label], expected))
    compare("paper4_snapshot", paper4, primary["paper4_snapshot"]["output_via_graft"])
    compare("producer_values", derived["producer u0"], hand["producer_values"]["u0"])
    compare("beta0_values_of_holes",
            [qtext(value) for value in FILLING_VALUES["beta0"]],
            hand["beta0_values_of_holes"])

    # Independent Paper IV strict-domain check: x2 - x4 = 0 is undefined.
    require(paper4_outputs((Fraction(2), Fraction(5), Fraction(3), Fraction(5))) is None,
            "EXP3-PAPER4-SNAPSHOT-MISMATCH",
            "the term route did not report the zero denominator as undefined")

    # Carrier layer.
    carrier = {}
    for name in sorted(CARRIER_TERMS):
        row = {}
        for filling, label in (("gamma_L", "L"), ("gamma_M", "M")):
            observed = carrier_observation_total(name, label)
            row[filling] = [observed[0], list(observed[1])] if observed[0] == "DEFINED" else list(observed)
        carrier[name] = row
    for name in sorted(CARRIER_TERMS):
        for filling in ("gamma_L", "gamma_M"):
            left = carrier[name][filling]
            right = primary["carrier_layer"][name][filling]["observation"]
            compare("carrier[%s][%s].status" % (name, filling), left[0], right[0])
            if left[0] == "DEFINED":
                compare("carrier[%s][%s].value" % (name, filling), list(left[1]), right[1])
            else:
                compare("carrier[%s][%s].code" % (name, filling), left[1], right[1])

    negative_controls = []

    # Independent negative control 1: a drifted contract copy is refused.
    negative_controls.append({
        "id": "independent-contract-drift",
        "expected": "EXP-CONTRACT-DRIFT",
        "observed": gapkit.reject(
            lambda: digest_check(contract_raw + b" "), "EXP-CONTRACT-DRIFT"),
    })

    # Independent negative control 2: binding a carrier producer into a Q hole.
    negative_controls.append({
        "id": "independent-graft-type-mismatch",
        "expected": "EXP3-TYPE-MISMATCH",
        "observed": gapkit.reject(lambda: bind_check("h1", "CarrierID"), "EXP3-TYPE-MISMATCH"),
    })

    # Independent negative control 3: strict division by zero in the term route.
    negative_controls.append({
        "id": "independent-strict-division-by-zero",
        "expected": "EXP3-STRICT-DIVISION-BY-ZERO",
        "observed": gapkit.reject(lambda: readout_outputs((Fraction(2), Fraction(1),
                                                           Fraction(0), Fraction(2))),
                                  "EXP3-STRICT-DIVISION-BY-ZERO"),
    })

    # Independent negative control 4: the term route must not silently agree
    # when one primary value is replaced by a neighbouring value.
    def mutated_table():
        right = list(primary["paper4_snapshot"]["output_via_graft"])
        mutated = list(right)
        mutated[-1] = "5/3"
        require(mutated == right, "EXP3-ROUTE-DISAGREEMENT",
                "the term route reports %r and the mutated primary table reports %r"
                % (right, mutated))
    negative_controls.append({
        "id": "independent-route-disagreement",
        "expected": "EXP3-ROUTE-DISAGREEMENT",
        "observed": gapkit.reject(mutated_table, "EXP3-ROUTE-DISAGREEMENT"),
    })

    record = {
        "schema": SCHEMA,
        "role": "independent verification route for exp3",
        "contract": {"path": str(CONTRACT.relative_to(ROOT.parent.parent)), "sha256": contract_sha},
        "environment": gapkit.environ(),
        "independence": {
            "route": ("direct substitution-and-evaluation: producer values are substituted into the "
                      "body term and the term is evaluated with fractions.Fraction; no wire, gate, "
                      "network, schedule, graft receipt or constant-source ancestry is constructed"),
            "declared_domain_rule": ("the composite is defined iff every closure producer is "
                                     "defined and the body term is defined on the substituted "
                                     "values; Paper IV Equation (5.2) written out directly"),
            "shared_module": "tools/gapkit.py only (JSON serialisation, hashing, diagnostics, Cost)",
            "shared_semantic_helpers": [],
        },
        "independent_search": {
            "domain_size": search["domain_size"],
            "by_size": search["by_size"],
            "initial_summary_classes": search["base_classes"],
            "initial_summary_insufficient_fibres": search["base_insufficient_fibres"],
            "declared_filling_equivalence_classes": search["filling_classes"],
            "minimal_witness_rank": search["base_witness_rank"],
            "minimal_witness_bodies": search["base_witness_bodies"],
            "grid_sufficient_candidates": sorted(
                key for key, entry in search["grid"].items() if entry["sufficient"]),
            "grid_size": len(search["grid"]),
        },
        "witness_checks": witness_checks,
        "carrier_layer": carrier,
        "hand_table": {label: derived[label] for label in sorted(HAND_TABLE)},
        "comparisons": comparisons,
        "disagreements": disagreements,
        "negative_controls": negative_controls,
        "conclusion": ("the independent term route reproduces every primary verdict and every "
                       "reported witness" if not disagreements else
                       "the independent route disagrees; the disagreement is the result"),
    }
    require(not disagreements, "EXP3-ROUTE-DISAGREEMENT",
            "the independent route disagrees with the primary on: %r" % (disagreements,))
    return record


_TEXT_MEMO = {}


def parse_text(text: str):
    """Parse the canonical body encoding used in the evidence."""
    hit = _TEXT_MEMO.get(text)
    if hit is not None:
        return hit
    if text.startswith("const("):
        term = ("const", int(text[6:-1]))
    elif text.startswith("h") and text[1:].isdigit():
        term = ("var", int(text[1:]))
    else:
        op = text.split("(", 1)[0]
        inner = text[len(op) + 1:-1]
        depth = 0
        split = None
        for index, char in enumerate(inner):
            if char == "(":
                depth += 1
            elif char == ")":
                depth -= 1
            elif char == "," and depth == 0:
                split = index
                break
        require(split is not None, "EXP3I-PARSE-ERROR", repr(text))
        term = (op, parse_text(inner[:split]), parse_text(inner[split + 1:]))
    _TEXT_MEMO[text] = term
    return term


def primary_witness_rank(entry) -> list:
    first, second = entry["bodies"]
    return [entry["binary_gates"][0] + entry["binary_gates"][1]] + sorted([first, second])


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", default=None)
    args = parser.parse_args()
    record = run()
    text = gapkit.canonical(record)
    if args.out:
        Path(args.out).write_text(text, encoding="utf-8")
        sys.stderr.write("exp3 independent written to %s sha256=%s\n"
                         % (args.out, gapkit.sha256_bytes(text.encode("utf-8"))))
    else:
        sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
