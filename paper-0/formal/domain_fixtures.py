"""Fixed guarded-comb cases and an independent unbounded rational oracle (CC0)."""

from fractions import Fraction
import json
from pathlib import Path

from fixtures import integer, node


def encode(case):
    def rational(pair):
        return node(31, *(integer(x) for x in pair))
    return node(30, rational(case["initial"]), node(32, *(
        node(33, integer(op), integer(slot), rational(value))
        for op, slot, value in case["word"])))


def oracle(case):
    """No fixed-width arithmetic; guards use the actual denominator operand."""
    value = Fraction(*case["initial"])
    for op, slot, constant in case["word"]:
        other = Fraction(*constant)
        if op not in range(4) or slot not in (1, 2):
            raise ValueError("unknown operation or slot")
        left, right = (value, other) if slot == 1 else (other, value)
        if op == 0:
            value = left + right
        elif op == 1:
            value = left - right
        elif op == 2:
            value = left * right
        else:
            if right == 0:
                raise ZeroDivisionError("division by zero")
            value = left / right
    return value


def cases():
    result = [{"name": "domain-empty", "initial": [3, 2], "word": [], "status": "Returned"}]
    for op, name in enumerate(("add", "subtract", "multiply", "divide")):
        for slot in (1, 2):
            result.append({"name": f"domain-{name}-slot{slot}", "initial": [3, 2],
                           "word": [[op, slot, [2, 3]]], "status": "Returned"})
    def put(name, initial, word, reason=None):
        row = {"name": name, "initial": initial, "word": word,
               "status": "Rejected" if reason else "Returned"}
        if reason:
            row["reason"] = reason
        result.append(row)
    put("domain-left-zero-denominator", [1, 1], [[3, 1, [0, 1]]], "division by zero")
    put("domain-right-zero-denominator", [0, 1], [[3, 2, [1, 1]]], "division by zero")
    put("domain-zero-numerator-legal", [2, 1], [[3, 2, [0, 1]]])
    put("domain-zero-numerator-illegal", [0, 1], [[3, 2, [0, 1]]], "division by zero")
    put("domain-intermediate-zero", [1, 1], [[1, 1, [1, 1]], [3, 2, [1, 1]]], "division by zero")
    put("domain-cancelled-pole", [0, 1], [[3, 2, [1, 1]], [2, 1, [0, 1]]], "division by zero")
    put("domain-left-pole-before-zero", [1, 1], [[3, 1, [0, 1]], [2, 1, [0, 1]]], "division by zero")
    put("domain-mixed-slots", [2, 1], [[0, 1, [3, 1]], [3, 2, [10, 1]], [2, 1, [4, 1]]])
    put("domain-zero-divided-nonzero", [0, 1], [[3, 1, [2, 1]]])
    put("domain-zero-multiplier", [3, 1], [[2, 1, [0, 1]]])
    put("domain-negative-denominator", [3, -2], [[3, 2, [2, 1]]])
    put("domain-unknown-operation", [1, 1], [[4, 1, [1, 1]]], "unknown operation or slot")
    put("domain-unknown-slot", [1, 1], [[0, 3, [1, 1]]], "unknown operation or slot")
    put("domain-invalid-initial", [1, 0], [], "invalid rational denominator")
    put("domain-invalid-constant", [1, 1], [[0, 1, [1, 0]]], "invalid rational denominator")
    put("domain-word-bound", [1, 1], [[0, 1, [0, 1]]] * 17, "comb length bound")
    put("domain-overflow", [2**63 - 1, 1], [[2, 1, [2, 1]]], "integer overflow")
    put("domain-unit-marked-first", [2, 1], [[0, 1, [1, 1]], [2, 1, [1, 1]]])
    put("domain-unit-marked-second", [2, 1], [[2, 1, [1, 1]], [0, 1, [1, 1]]])
    return result


if __name__ == "__main__":
    (Path(__file__).parent / "domain-cases.json").write_text(json.dumps(cases(), indent=2) + "\n")
