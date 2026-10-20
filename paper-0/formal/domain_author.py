"""Author guarded rational comb evaluation in existing Adva instructions (CC0).

This is a separate bounded evaluator, not an extension of the equation kernel.
Every division guard examines the actual denominator before calculation.
"""

import json
from pathlib import Path

from author import Author, REGISTERS


def generated():
    a = Author()
    # Existing integer registers are reused as rational numerator/denominator
    # pairs. tag/arity are scratch; count/depth are the constant operand.
    num, den, cn, cd = "index", "other_index", "count", "depth"

    def rational(src, n, d):
        a.shape(src, 31, 2)
        for i, dst in [(0, n), (1, d)]:
            a.field(src, i, "leaf", 2)
            a.emit("tag", src="leaf", dst="tag")
            a.require("tag", -1, "noninteger rational")
            a.emit("as_integer", src="leaf", dst=dst)
        good = a.fresh()
        a.equal_constant(d, 0)
        a.branch(a.reject("invalid rational denominator"), good)
        a.mark(good)

    a.const("one", 1)
    a.emit("input", dst="input")
    a.shape("input", 30, 2)
    a.field("input", 0, "a", 2)
    a.field("input", 1, "proof", 2)
    rational("a", num, den)
    a.emit("tag", src="proof", dst="tag")
    a.require("tag", 32, "wrong tag")
    a.emit("length", src="proof", dst="length")
    a.member("length", range(17), "comb length bound")
    a.const("position", 0)
    a.mark("loop")
    a.emit("equal", left="position", right="length", dst="test")
    a.branch("finish", "step")
    a.mark("step")
    a.emit("field_dynamic", src="proof", index="position", dst="step")
    a.shape("step", 33, 3)
    for i, dst, allowed in [(0, "rule", range(4)), (1, "other_tag", (1, 2))]:
        a.field("step", i, "leaf", 3)
        a.emit("tag", src="leaf", dst="tag")
        a.require("tag", -1, "noninteger step label")
        a.emit("as_integer", src="leaf", dst=dst)
        a.member(dst, allowed, "unknown operation or slot")
    a.field("step", 2, "a", 3)
    rational("a", cn, cd)
    a.equal_constant("other_tag", 2)
    a.branch("swap", "dispatch")
    a.mark("swap")
    # Native Copy applies to integer registers too. Source values are retained
    # in the trace; no host operand swap or rational normalization is used.
    for x, y, t in [(num, cn, "tag"), (den, cd, "arity")]:
        a.copy(x, t)
        a.copy(y, x)
        a.copy(t, y)
    a.mark("dispatch")
    for value, label in [(0, "add"), (1, "subtract"), (2, "multiply"), (3, "divide")]:
        following = a.fresh()
        a.equal_constant("rule", value)
        a.branch(label, following)
        a.mark(following)
    a.jump(a.reject("unknown operation or slot"))
    for operation, label in [(0, "add"), (1, "subtract")]:
        a.mark(label)
        a.emit("multiply", left=num, right=cd, dst="tag")
        a.emit("multiply", left=cn, right=den, dst="arity")
        if operation == 1:
            a.const("constant", -1)
            a.emit("multiply", left="arity", right="constant", dst="arity")
        a.emit("add", left="tag", right="arity", dst=num)
        a.emit("multiply", left=den, right=cd, dst=den)
        a.jump("advance")
    a.mark("multiply")
    a.emit("multiply", left=num, right=cn, dst=num)
    a.emit("multiply", left=den, right=cd, dst=den)
    a.jump("advance")
    a.mark("divide")
    good = a.fresh()
    a.equal_constant(cn, 0)
    a.branch(a.reject("division by zero"), good)
    a.mark(good)
    a.emit("multiply", left=num, right=cd, dst=num)
    a.emit("multiply", left=den, right=cn, dst=den)
    a.mark("advance")
    a.emit("add", left="position", right="one", dst="position")
    a.jump("loop")
    a.mark("finish")
    a.emit("box_integer", src=num, dst="left")
    a.emit("box_integer", src=den, dst="right")
    a.node(31, ["left", "right"], "equation")
    a.emit("return", src="equation")
    for reason in sorted(a.rejections):
        a.mark(a.reject(reason))
        a.emit("reject", reason=reason)
    for instruction in a.code:
        for key in ("yes", "no", "target"):
            if key in instruction:
                instruction[key] = a.labels[instruction[key]]
    return {"schema": "adva.data-machine.program.research.v1",
            "name": "aeg-guarded-rational-comb-v1",
            "registers": [{"name": n, "kind": k} for n, k in REGISTERS], "code": a.code}


if __name__ == "__main__":
    p = generated()
    (Path(__file__).parent / "domain-checker.adva").write_text(json.dumps(p, indent=2) + "\n")
    print(json.dumps({"instructions": len(p["code"]), "registers": len(p["registers"])}))
