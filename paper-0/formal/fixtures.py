"""Explicit symbolic theorem statements and untrusted proof production (CC0)."""

import json
from pathlib import Path


def integer(value):
    return {"kind": "integer", "value": value}


def node(tag, *fields):
    return {"kind": "node", "tag": tag, "fields": list(fields)}


def var(index):
    return node(0, integer(index))


def add(a, b):
    return node(3, a, b)


def mul(a, b):
    return node(4, a, b)


def equation(a, b):
    return node(22, a, b)


def input_data(proof, goal):
    return node(20, node(21, *proof), goal)


def statements():
    """Reviewable targets; never inferred by running the proof producer."""
    a, b, c, d, e, z = [var(i) for i in range(6)]
    return [
        {"id": "p0-addition-opposition", "source": "paper-0/sections/02-expansion.tex",
         "label": "prop:p0-comb-opposition", "coverage": "addition one-hole component",
         "lean": "addition_opposition", "goal": equation(add(a, b), add(b, a))},
        {"id": "p0-multiplication-opposition", "source": "paper-0/sections/02-expansion.tex",
         "label": "prop:p0-comb-opposition", "coverage": "multiplication one-hole component",
         "lean": "multiplication_opposition", "goal": equation(mul(a, b), mul(b, a))},
        {"id": "p0-distributive-operator", "source": "paper-0/sections/02-expansion.tex",
         "label": "prop:p0-distributive-operator-identity",
         "coverage": "operator equality k*(z+p)=k*z+k*p only; excludes marked-data coincidence clause",
         "lean": "distributive_operator", "goal": equation(mul(c, add(z, b)), add(mul(c, z), mul(c, b)))},
        {"id": "p0-right-distributivity", "source": "paper-0/sections/02-expansion.tex",
         "label": "prop:p0-distributive-operator-identity",
         "coverage": "supporting derived semiring lemma, not a separately numbered manuscript theorem",
         "lean": "right_distributivity", "goal": equation(mul(add(a, b), c), add(mul(a, c), mul(b, c)))},
        {"id": "p0-affine-composition-polynomial", "source": "paper-0/sections/07-affine-cocycles.tex",
         "label": "prop:chronological-affine-cocycle-law",
         "coverage": "pointwise polynomial component d*(a*z+b)+e=(d*a)*z+(d*b+e); excludes inverse/normalized coordinate laws",
         "lean": "affine_composition", "goal": equation(add(mul(d, add(mul(a, z), b)), e),
                                                            add(mul(mul(d, a), z), add(mul(d, b), e)))},
    ]


def certificates():
    a, b, c, d, e, z = [var(i) for i in range(6)]
    return {
        "p0-addition-opposition": [node(11, a, b)],
        "p0-multiplication-opposition": [node(14, a, b)],
        "p0-distributive-operator": [node(16, c, z, b)],
        "p0-right-distributivity": [node(14, add(a, b), c), node(16, c, a, b), node(2),
                                    node(14, c, a), node(14, c, b), node(3), node(2)],
        "p0-affine-composition-polynomial": [
            node(16, d, mul(a, z), b), node(0, e), node(3),
            node(13, d, a, z), node(1), node(0, mul(d, b)), node(3),
            node(0, e), node(3), node(2),
            node(10, mul(mul(d, a), z), mul(d, b), e), node(2),
        ],
    }


def polynomial(term):
    """Independent sparse N[X] oracle: all-variable coefficient comparison."""
    if not isinstance(term, dict) or set(term) != {"kind", "tag", "fields"}:
        raise ValueError("bad symbolic term")
    if term["kind"] != "node" or type(term["tag"]) is not int:
        raise ValueError("bad constructor")
    tag, fields = term["tag"], term["fields"]
    if tag == 0 and len(fields) == 1:
        value = fields[0]
        if set(value) != {"kind", "value"} or value["kind"] != "integer" or type(value["value"]) is not int or not 0 <= value["value"] < 8:
            raise ValueError("bad variable")
        return {(value["value"],): 1}
    if tag in (1, 2) and not fields:
        return {} if tag == 1 else {(): 1}
    if tag not in (3, 4) or len(fields) != 2:
        raise ValueError("bad arithmetic term")
    left, right = map(polynomial, fields)
    result = dict(left) if tag == 3 else {}
    if tag == 3:
        for monomial, coefficient in right.items():
            result[monomial] = result.get(monomial, 0) + coefficient
    else:
        for x, cx in left.items():
            for y, cy in right.items():
                product = tuple(sorted(x + y))
                result[product] = result.get(product, 0) + cx * cy
    return result


if __name__ == "__main__":
    root = Path(__file__).resolve().parent
    for filename, value in [("statements.json", statements()), ("certificates.json", certificates())]:
        (root / filename).write_text(json.dumps(value, indent=2) + "\n")
