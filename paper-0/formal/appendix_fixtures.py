"""Independent fixed induction-step goal and untrusted proof production (CC0)."""

import json
from pathlib import Path

from fixtures import add, equation, mul, node, var


def statement():
    q, x, delta, mu = [var(i) for i in range(4)]
    return {
        "id": "p0-appendix-c-perturbation-step",
        "source": "paper-0/appendices/app-C-affine-cocycles.tex",
        "label": "prop:appendix-alternating-arithmetic-perturbation",
        "lean": "perturbation_step",
        "coverage": "Symbolic semiring induction step only; unbounded list induction is checked separately by Lean.",
        "goal": equation(add(mul(q, add(x, delta)), mu), add(add(mul(q, x), mu), mul(q, delta))),
    }


def certificate():
    q, x, delta, mu = [var(i) for i in range(4)]
    qx, qd = mul(q, x), mul(q, delta)
    return [node(16, q, x, delta), node(0, mu), node(3),
            node(10, qx, qd, mu), node(2),
            node(0, qx), node(11, qd, mu), node(3), node(2),
            node(10, qx, mu, qd), node(1), node(2)]


def wrong_goal():
    q, x, delta, mu = [var(i) for i in range(4)]
    return equation(add(mul(q, add(x, delta)), mu), add(mul(q, add(x, mu)), delta))


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    for name, value in (("appendix-statement.json", statement()), ("appendix-certificate.json", certificate())):
        (here / name).write_text(json.dumps(value, indent=2) + "\n")
