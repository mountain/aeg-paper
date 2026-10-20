"""Author a bounded equality kernel in existing Adva v1 instructions.

Original CC0 contribution by Codex (OpenAI). No host proof callback is emitted.
"""

import json
from pathlib import Path

REGISTERS = [(x, "stack") for x in ("proof_stack", "walk", "compare_left", "compare_right")]
REGISTERS += [(x, "data") for x in (
    "input", "proof", "goal", "step", "a", "b", "c", "left", "right",
    "u", "v", "temporary", "t0", "t1", "t2", "equation", "term", "other", "leaf",
)]
REGISTERS += [(x, "integer") for x in (
    "length", "position", "rule", "tag", "other_tag", "arity", "index", "other_index",
    "count", "constant", "one", "depth",
)]
REGISTERS += [("test", "boolean")]
R = {name: i for i, (name, _) in enumerate(REGISTERS)}


class Author:
    def __init__(self):
        self.code, self.labels, self.rejections = [], {}, set()
        self.serial = 0

    def fresh(self, prefix="label"):
        self.serial += 1
        return f"{prefix}_{self.serial}"

    def mark(self, name):
        if name in self.labels:
            raise ValueError("duplicate label")
        self.labels[name] = len(self.code)

    def emit(self, op, **fields):
        for key in ("src", "dst", "left", "right", "stack", "condition", "index"):
            if isinstance(fields.get(key), str):
                fields[key] = R[fields[key]]
        if "fields" in fields:
            fields["fields"] = [R[x] for x in fields["fields"]]
        self.code.append({"op": op, **fields})

    def const(self, register, value):
        self.emit("constant", dst=register, value=value)

    def jump(self, label):
        self.emit("jump", target=label)

    def branch(self, yes, no):
        self.emit("branch", condition="test", yes=yes, no=no)

    def reject(self, reason):
        self.rejections.add(reason)
        return "reject_" + reason.replace(" ", "_")

    def equal_constant(self, register, value):
        self.const("constant", value)
        self.emit("equal", left=register, right="constant", dst="test")

    def require(self, register, value, reason):
        good = self.fresh()
        self.equal_constant(register, value)
        self.branch(good, self.reject(reason))
        self.mark(good)

    def member(self, register, values, reason):
        good = self.fresh()
        for value in values:
            following = self.fresh()
            self.equal_constant(register, value)
            self.branch(good, following)
            self.mark(following)
        self.jump(self.reject(reason))
        self.mark(good)

    def arity(self, register, length):
        self.emit("length", src=register, dst="arity")
        self.require("arity", length, "wrong arity")

    def shape(self, register, tag, length):
        self.emit("tag", src=register, dst="tag")
        self.require("tag", tag, "wrong tag")
        self.arity(register, length)

    def field(self, src, index, dst, arity):
        self.emit("field", src=src, index=index, dst=dst, arity=arity)

    def node(self, tag, fields, dst):
        self.emit("node", tag=tag, fields=fields, dst=dst)

    def copy(self, src, dst):
        self.emit("copy", src=src, dst=dst)

    def pop_equation(self, left, right):
        self.emit("pop", stack="proof_stack", dst="equation")
        self.field("equation", 0, left, 2)
        self.field("equation", 1, right, 2)

    def validate(self, root):
        """Validate every term node, with a per-expression bound of 63."""
        loop, done, body, variable, zero, one, binary = [self.fresh() for _ in range(7)]
        self.emit("clear", stack="walk")
        self.emit("push", stack="walk", src=root)
        self.const("count", 0)
        self.mark(loop)
        self.emit("is_empty", stack="walk", dst="test")
        self.branch(done, body)
        self.mark(body)
        room = self.fresh()
        self.equal_constant("count", 63)
        self.branch(self.reject("term bound"), room)
        self.mark(room)
        self.emit("add", left="count", right="one", dst="count")
        self.emit("pop", stack="walk", dst="term")
        self.emit("tag", src="term", dst="tag")
        for tag, label in [(0, variable), (1, zero), (2, one), (3, binary), (4, binary)]:
            following = self.fresh()
            self.equal_constant("tag", tag)
            self.branch(label, following)
            self.mark(following)
        self.jump(self.reject("unknown term"))
        self.mark(variable)
        self.arity("term", 1)
        self.field("term", 0, "leaf", 1)
        self.emit("tag", src="leaf", dst="tag")
        self.require("tag", -1, "noninteger variable")
        self.emit("as_integer", src="leaf", dst="index")
        self.member("index", range(8), "unknown variable")
        self.jump(loop)
        self.mark(zero)
        self.arity("term", 0)
        self.jump(loop)
        self.mark(one)
        self.arity("term", 0)
        self.jump(loop)
        self.mark(binary)
        self.arity("term", 2)
        for index in range(2):
            self.field("term", index, "leaf", 2)
            self.emit("push", stack="walk", src="leaf")
        self.jump(loop)
        self.mark(done)

    def compare(self, left, right):
        """Tree equality consists only of explicit tag and integer comparisons."""
        loop, body, done, variable, binary = [self.fresh() for _ in range(5)]
        self.emit("clear", stack="compare_left")
        self.emit("clear", stack="compare_right")
        self.emit("push", stack="compare_left", src=left)
        self.emit("push", stack="compare_right", src=right)
        self.mark(loop)
        self.emit("is_empty", stack="compare_left", dst="test")
        self.branch(done, body)
        self.mark(body)
        self.emit("pop", stack="compare_left", dst="term")
        self.emit("pop", stack="compare_right", dst="other")
        self.emit("tag", src="term", dst="tag")
        self.emit("tag", src="other", dst="other_tag")
        self.emit("equal", left="tag", right="other_tag", dst="test")
        same = self.fresh()
        self.branch(same, self.reject("equation mismatch"))
        self.mark(same)
        for tag, label in [(0, variable), (1, loop), (2, loop), (3, binary), (4, binary)]:
            following = self.fresh()
            self.equal_constant("tag", tag)
            self.branch(label, following)
            self.mark(following)
        self.jump(self.reject("unknown term"))
        self.mark(variable)
        self.field("term", 0, "leaf", 1)
        self.emit("as_integer", src="leaf", dst="index")
        self.field("other", 0, "leaf", 1)
        self.emit("as_integer", src="leaf", dst="other_index")
        self.emit("equal", left="index", right="other_index", dst="test")
        self.branch(loop, self.reject("equation mismatch"))
        self.mark(binary)
        for index in range(2):
            self.field("term", index, "leaf", 2)
            self.emit("push", stack="compare_left", src="leaf")
            self.field("other", index, "leaf", 2)
            self.emit("push", stack="compare_right", src="leaf")
        self.jump(loop)
        self.mark(done)
        self.emit("is_empty", stack="compare_right", dst="test")
        good = self.fresh()
        self.branch(good, self.reject("equation mismatch"))
        self.mark(good)

    def generate(self):
        self.const("one", 1)
        self.emit("clear", stack="proof_stack")
        self.emit("input", dst="input")
        self.shape("input", 20, 2)
        self.field("input", 0, "proof", 2)
        self.field("input", 1, "goal", 2)
        self.emit("tag", src="proof", dst="tag")
        self.require("tag", 21, "wrong tag")
        self.emit("length", src="proof", dst="length")
        self.member("length", range(65), "proof bound")
        self.shape("goal", 22, 2)
        self.field("goal", 0, "left", 2)
        self.field("goal", 1, "right", 2)
        self.validate("left")
        self.validate("right")
        self.const("position", 0)
        self.mark("step_loop")
        self.emit("equal", left="position", right="length", dst="test")
        self.branch("finish", "read_step")
        self.mark("read_step")
        self.emit("field_dynamic", src="proof", index="position", dst="step")
        self.emit("tag", src="step", dst="rule")
        for rule in [0, 1, 2, 3, 4, *range(10, 18)]:
            following = self.fresh()
            self.equal_constant("rule", rule)
            self.branch(f"rule_{rule}", following)
            self.mark(following)
        self.jump(self.reject("unknown rule"))
        self.mark("rule_0")
        self.arity("step", 1)
        self.field("step", 0, "left", 1)
        self.copy("left", "right")
        self.jump("push_equation")
        self.mark("rule_1")
        self.arity("step", 0)
        self.pop_equation("right", "left")
        self.jump("push_equation")
        self.mark("rule_2")
        self.arity("step", 0)
        self.pop_equation("u", "v")
        self.pop_equation("left", "right")
        self.compare("right", "u")
        self.copy("v", "right")
        self.jump("push_equation")
        for rule, tag in [(3, 3), (4, 4)]:
            self.mark(f"rule_{rule}")
            self.arity("step", 0)
            self.pop_equation("u", "v")
            self.pop_equation("left", "right")
            self.node(tag, ["left", "u"], "left")
            self.node(tag, ["right", "v"], "right")
            self.jump("push_equation")
        for rule in range(10, 18):
            self.mark(f"rule_{rule}")
            arity = 3 if rule in (10, 13, 16) else 2 if rule in (11, 14) else 1
            self.arity("step", arity)
            for index, register in enumerate(["a", "b", "c"][:arity]):
                self.field("step", index, register, arity)
            if rule in (10, 13):
                tag = 3 if rule == 10 else 4
                self.node(tag, ["a", "b"], "t0")
                self.node(tag, ["t0", "c"], "left")
                self.node(tag, ["b", "c"], "t0")
                self.node(tag, ["a", "t0"], "right")
            elif rule in (11, 14):
                tag = 3 if rule == 11 else 4
                self.node(tag, ["a", "b"], "left")
                self.node(tag, ["b", "a"], "right")
            elif rule in (12, 15, 17):
                self.node(2 if rule == 15 else 1, [], "t0")
                self.node(3 if rule == 12 else 4, ["a", "t0"], "left")
                self.copy("t0" if rule == 17 else "a", "right")
            else:
                self.node(3, ["b", "c"], "t0")
                self.node(4, ["a", "t0"], "left")
                self.node(4, ["a", "b"], "t0")
                self.node(4, ["a", "c"], "t1")
                self.node(3, ["t0", "t1"], "right")
            self.jump("push_equation")
        self.mark("push_equation")
        self.validate("left")
        self.validate("right")
        self.emit("stack_length", stack="proof_stack", dst="depth")
        room = self.fresh()
        self.equal_constant("depth", 32)
        self.branch(self.reject("proof stack bound"), room)
        self.mark(room)
        self.node(22, ["left", "right"], "equation")
        self.emit("push", stack="proof_stack", src="equation")
        self.emit("add", left="position", right="one", dst="position")
        self.jump("step_loop")
        self.mark("finish")
        self.emit("stack_length", stack="proof_stack", dst="depth")
        self.require("depth", 1, "non singleton proof")
        self.pop_equation("left", "right")
        self.field("goal", 0, "u", 2)
        self.field("goal", 1, "v", 2)
        self.compare("left", "u")
        self.compare("right", "v")
        self.node(22, ["left", "right"], "equation")
        self.emit("return", src="equation")
        for reason in sorted(self.rejections):
            self.mark(self.reject(reason))
            self.emit("reject", reason=reason)
        for instruction in self.code:
            for key in ("yes", "no", "target"):
                if key in instruction:
                    instruction[key] = self.labels[instruction[key]]
        return {"schema": "adva.data-machine.program.research.v1",
                "name": "aeg-commutative-semiring-equality-v1",
                "registers": [{"name": name, "kind": kind} for name, kind in REGISTERS],
                "code": self.code}


if __name__ == "__main__":
    root = Path(__file__).resolve().parent
    program = Author().generate()
    (root / "checker.adva").write_text(json.dumps(program, indent=2) + "\n")
    print(json.dumps({"registers": len(REGISTERS), "instructions": len(program["code"])}))
