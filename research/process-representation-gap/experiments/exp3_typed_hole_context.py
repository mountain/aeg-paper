#!/usr/bin/env python3
"""Experiment 3 -- typed hole filling and context.

Contract: research/process-representation-gap/contracts/exp3-typed-hole-context.v1.json

The question the work plan asks (section 6, 实验三) is whether two open processes
that give the same output under one filling may be replaced by each other in
another legal context.  The answer computed here is NO on the declared finite
domain, with explicit witnesses: value equality at the frozen initial filling is
never sufficient for contextual substitutability.

The governing interface is Paper IV section 05b, "Ported AES programs": strict
finite arithmetic networks with ordered typed boundaries, explicit copy and
strict discard, immutable source and occurrence identity, and certified
simultaneous substitution carrying a graft receipt.  This file implements that
interface.  It is NOT native Adva execution, NOT a faithful AES motion, and it
makes no geometric claim about a carrier.

Every obligation is a ``gapkit.require`` with a stable ``EXP3-`` code.  No
``assert`` is used anywhere, so the checker behaves identically under
``python3 -O``.  Exact arithmetic only: ints and ``fractions.Fraction``.

Run:

    python3 research/process-representation-gap/experiments/exp3_typed_hole_context.py
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
EVIDENCE = ROOT / "evidence" / "exp3-typed-hole-context.json"

SCHEMA = "aeg.process-representation-gap.exp3.v1"

# --------------------------------------------------------------------------
# declared interface
# --------------------------------------------------------------------------

TYPE_Q = "Q"
TYPE_CARRIER = "CarrierID"

ARITY = {
    "const_Q": (0, 1),
    "const_carrier": (0, 1),
    "add": (2, 1),
    "sub": (2, 1),
    "mul": (2, 1),
    "div": (2, 1),
    "copy": (1, 2),
    "discard": (1, 0),
    "transport": (1, 1),
    "route": (1, 1),
}

HOLES = ("h1", "h2", "h3", "h4")
NHOLES = 4
LITERALS = (-1, 0, 1, 2)
OPS = ("add", "sub", "mul", "div")
MAX_BINARY_GATES = 2
DECLARED_COUNTS = {"0": 8, "1": 256, "2": 16384}

DECLARED_REJECTIONS = ("EXP3-PROVENANCE-MISWIRE",)
# Declared primitive domain predicates.  In observation mode a failure is the
# declared UNDEFINED outcome; in strict execution mode it raises its own code.
DOMAIN_PREDICATE_CODES = ("EXP3-STRICT-DIVISION-BY-ZERO",)

EXTERNAL_INPUT = "@input"
EXTERNAL_OUTPUT = "@output"

# Receipt layout for a graft: ("graft", body receipt, producer receipts,
# binding records, declared output boundary, producer region prefixes).
RECEIPT_BODY = 1
RECEIPT_PRODUCERS = 2
RECEIPT_RECORDS = 3
RECEIPT_BOUNDARY = 4
RECEIPT_REGIONS = 5


class _Undefined:
    """The declared undefined outcome: a value, not an exception."""

    __slots__ = ()

    def __repr__(self) -> str:
        return "UNDEFINED"


UNDEFINED = _Undefined()


def carrier(label: str) -> tuple:
    return ("carrier", label)


def render_value(value) -> str:
    if value is UNDEFINED:
        return "UNDEFINED"
    if isinstance(value, Fraction):
        return qtext(value)
    if isinstance(value, tuple) and len(value) == 2 and value[0] == "carrier":
        return "carrier:" + value[1]
    raise Diagnostic("EXP3-UNKNOWN-VALUE", repr(value))


# --------------------------------------------------------------------------
# the declared body grammar
# --------------------------------------------------------------------------

def expressions(max_gates: int = MAX_BINARY_GATES):
    """All expression trees with 0..max_gates binary gates, in a fixed order.

    Leaves are the four holes and the four declared literals, so the size-s
    class has Catalan(s) * 4^s * 8^(s+1) members: 8, 256, 16384.  The
    enumeration is total and deterministic; nothing is sampled.
    """
    leaves = [("var", i) for i in range(1, NHOLES + 1)] + [("const", c) for c in LITERALS]
    by_size = {0: leaves}
    for size in range(1, max_gates + 1):
        layer = []
        for left in range(size):
            right = size - 1 - left
            for op in OPS:
                for first in by_size[left]:
                    for second in by_size[right]:
                        layer.append((op, first, second))
        by_size[size] = layer
    return by_size


def render_expression(expr) -> str:
    kind = expr[0]
    if kind == "var":
        return "h%d" % expr[1]
    if kind == "const":
        return "const(%d)" % expr[1]
    return "%s(%s,%s)" % (expr[0], render_expression(expr[1]), render_expression(expr[2]))


def binary_gate_count(expr) -> int:
    if expr[0] in ("var", "const"):
        return 0
    return 1 + binary_gate_count(expr[1]) + binary_gate_count(expr[2])


def hole_occurrences(expr) -> list:
    counts = [0] * NHOLES
    stack = [expr]
    while stack:
        node = stack.pop()
        kind = node[0]
        if kind == "var":
            counts[node[1] - 1] += 1
        elif kind != "const":
            stack.append(node[1])
            stack.append(node[2])
    return counts


def expression_literals(expr) -> list:
    out = []
    stack = [expr]
    while stack:
        node = stack.pop()
        kind = node[0]
        if kind == "const":
            out.append(node[1])
        elif kind != "var":
            stack.append(node[1])
            stack.append(node[2])
    return sorted(out)


def expression_operators(expr) -> list:
    out = []
    stack = [expr]
    while stack:
        node = stack.pop()
        kind = node[0]
        if kind in ("var", "const"):
            continue
        out.append(kind)
        stack.append(node[1])
        stack.append(node[2])
    return sorted(out)


# --------------------------------------------------------------------------
# strict finite networks (Paper IV, Definition def:strict-finite-network)
# --------------------------------------------------------------------------

# Wire    = (id, type, source, occurrence)
# Gate    = (id, op, inputs, outputs, source, occurrence, parameter)
# Network = (wires, gates, inputs, outputs, receipt)

def wire_record(wire) -> dict:
    return {"id": wire[0], "type": wire[1], "source": wire[2], "occurrence": wire[3]}


def gate_record(gate) -> dict:
    parameter = gate[6]
    if isinstance(parameter, Fraction):
        rendered = qtext(parameter)
    elif parameter is None:
        rendered = None
    else:
        rendered = str(parameter)
    return {
        "id": gate[0],
        "op": gate[1],
        "inputs": list(gate[2]),
        "outputs": list(gate[3]),
        "source": gate[4],
        "occurrence": gate[5],
        "parameter": rendered,
    }


class Builder:
    """Builds a strict finite network with typed wires and source records."""

    def __init__(self, instance: str, template=None) -> None:
        self.instance = instance
        self.template = template or instance
        self.wires = {}
        self.gates = {}
        self.inputs = []

    def wire(self, label: str, wire_type: str, source: str) -> str:
        wid = "%s/w/%s" % (self.instance, label)
        require(wid not in self.wires, "EXP3-DUPLICATE-WIRE",
                "wire %r declared twice in instance %r" % (wid, self.instance))
        self.wires[wid] = (wid, wire_type, source, "%s/occ/%s" % (self.instance, label))
        return wid

    def input(self, label: str, wire_type: str = TYPE_Q) -> str:
        wid = self.wire(label, wire_type, "%s/src/%s" % (self.template, label))
        self.inputs.append(wid)
        return wid

    def gate(self, label: str, op: str, inputs=(), parameter=None,
             output_type: str = TYPE_Q, output_source=None) -> tuple:
        require(op in ARITY, "EXP3-UNKNOWN-PRIMITIVE", repr(op))
        source = "%s/gsrc/%s" % (self.template, label)
        if output_source is None:
            output_source = source
        outs = tuple(
            self.wire("%s:%d" % (label, slot), output_type, output_source)
            for slot in range(ARITY[op][1])
        )
        gid = "%s/g/%s" % (self.instance, label)
        require(gid not in self.gates, "EXP3-DUPLICATE-GATE",
                "gate %r declared twice in instance %r" % (gid, self.instance))
        self.gates[gid] = (gid, op, tuple(inputs), outs, source,
                           "%s/ev/%s" % (self.instance, label), parameter)
        return outs

    def finish(self, outputs, receipt=None) -> tuple:
        return (dict(self.wires), dict(self.gates), tuple(self.inputs), tuple(outputs),
                receipt if receipt is not None else ("network", self.instance))


def _fanout(builder: Builder, stem: str, wire: str, uses: int) -> list:
    """Exactly ``uses`` occurrence-distinct consumers of one produced wire.

    ``uses - 1`` explicit copy gates are inserted, so no produced wire is ever
    implicitly shared; every copy output is consumed.
    """
    if uses == 1:
        return [wire]
    produced = []
    current = wire
    for index in range(uses - 1):
        outs = builder.gate("%s_copy%d" % (stem, index), "copy", (current,))
        produced.append(outs[0])
        current = outs[1]
    produced.append(current)
    return produced


def build_body(expr, instance: str = "b") -> tuple:
    """The declared open body: holes h1..h4 in order, one output y of type Q.

    An unused hole is consumed by an explicit strict discard; a hole consumed
    k times receives k occurrence-distinct wires through an explicit copy chain.
    """
    counts = hole_occurrences(expr)
    builder = Builder(instance)
    holes = [builder.input(name) for name in HOLES]
    available = {}
    for index in range(NHOLES):
        if counts[index] == 0:
            available[index] = []
        else:
            available[index] = _fanout(builder, "copy%d" % (index + 1), holes[index], counts[index])
    used = [0] * NHOLES
    counter = [0]

    def emit(node):
        kind = node[0]
        if kind == "var":
            slot = node[1] - 1
            wire = available[slot][used[slot]]
            used[slot] += 1
            return wire
        if kind == "const":
            counter[0] += 1
            return builder.gate("k%d" % counter[0], "const_Q", (),
                                parameter=Fraction(node[1]))[0]
        label = "g%d" % counter[0]
        counter[0] += 1
        first = emit(node[1])
        second = emit(node[2])
        return builder.gate(label, kind, (first, second))[0]

    root = emit(expr)
    for index in range(NHOLES):
        if counts[index] == 0:
            builder.gate("discard%d" % (index + 1), "discard", (holes[index],))
    return builder.finish([root], receipt=("body", render_expression(expr)))


# --------------------------------------------------------------------------
# declared producers (closed networks, each with a source record)
# --------------------------------------------------------------------------

PRODUCER_EXPRESSIONS = {
    "q1": ("add", ("const", 1), ("const", 1)),
    "q2": ("add", ("const", 3), ("const", 4)),
    "q3": ("div", ("const", 6), ("const", 2)),
    "q4": ("sub", ("const", 9), ("const", 4)),
    "q5": ("add", ("const", 2), ("const", 2)),
    "u0": ("div", ("const", 1), ("const", 0)),
}
CARRIER_PRODUCERS = {"pc_L": "L", "pc_M": "M"}
PRODUCER_ORDER = ("q1", "q2", "q3", "q4", "q5", "u0")


def admit_producer(record) -> None:
    """A numerical input is admitted only as an explicit constant producer with
    its source record; a bare value is refused (Paper IV section 5.3)."""
    require(isinstance(record, dict), "EXP3-RAW-VALUE-INPUT",
            "producer record must be a declared record, got %s" % (type(record).__name__,))
    require(bool(record.get("source")), "EXP3-RAW-VALUE-INPUT",
            "producer %r carries no source record: a bare value is not an admitted input"
            % (record.get("name"),))


def _build_from_expression(tree, builder: Builder, counter):
    kind = tree[0]
    if kind == "const":
        counter[0] += 1
        return builder.gate("k%d" % counter[0], "const_Q", (),
                            parameter=Fraction(tree[1]))[0]
    label = "g%d" % counter[0]
    counter[0] += 1
    first = _build_from_expression(tree[1], builder, counter)
    second = _build_from_expression(tree[2], builder, counter)
    return builder.gate(label, kind, (first, second))[0]


def build_producer(name: str, instance: str) -> tuple:
    """A closed producer network: declared constant sources, one output."""
    if name in CARRIER_PRODUCERS:
        builder = Builder(instance)
        label = CARRIER_PRODUCERS[name]
        wire = builder.gate("carrier", "const_carrier", (), parameter=label,
                            output_type=TYPE_CARRIER)[0]
        return builder.finish([wire], receipt=("producer", name, "carrier", label))
    require(name in PRODUCER_EXPRESSIONS, "EXP3-UNKNOWN-PRODUCER", repr(name))
    builder = Builder(instance)
    out = _build_from_expression(PRODUCER_EXPRESSIONS[name], builder, [0])
    return builder.finish([out], receipt=("producer", name, "Q"))


def build_constant_producer(value, instance: str) -> tuple:
    builder = Builder(instance)
    wire = builder.gate("k1", "const_Q", (), parameter=Fraction(value))[0]
    return builder.finish([wire], receipt=("producer", "constant", qtext(Fraction(value))))


PRODUCER_CACHE = {}


def producer_template(name: str) -> tuple:
    if name not in PRODUCER_CACHE:
        PRODUCER_CACHE[name] = build_producer(name, "template/%s" % name)
    return PRODUCER_CACHE[name]


def rename_network(network, prefix: str) -> tuple:
    """Administrative renaming: occurrences and administrative names are
    refreshed per named instance, source identities are transported unchanged
    (Paper IV section 5.2)."""
    wires, gates, inputs, outputs, receipt = network
    new_wires = {}
    for key, wire in wires.items():
        new_wires[prefix + key] = (prefix + wire[0], wire[1], wire[2], prefix + wire[3])
    new_gates = {}
    for key, gate in gates.items():
        # Occurrences are fresh for the named instance; sources are transported
        # unchanged, so template reuse is never confused with implicit sharing.
        new_gates[prefix + key] = (
            prefix + gate[0], gate[1],
            tuple(prefix + w for w in gate[2]),
            tuple(prefix + w for w in gate[3]),
            gate[4], prefix + gate[5], gate[6],
        )
    return (new_wires, new_gates, tuple(prefix + w for w in inputs),
            tuple(prefix + w for w in outputs), receipt)


# --------------------------------------------------------------------------
# certified simultaneous substitution (Paper IV, Construction constr:certified-substitution)
# --------------------------------------------------------------------------

def certified_substitution(body, producers, binding,
                           body_prefix: str = "body/", validate_inputs: bool = True) -> tuple:
    """Substitute producer output occurrences into selected body holes.

    ``binding`` is an ordered tuple of (producer index, output slot, hole slot).
    Types and positions are preserved, every supplied output is used once and
    every selected hole is filled once.  A numerical input enters only through
    an explicit producer network carrying a source record.
    """
    if validate_inputs:
        validate(body)
        for producer in producers:
            validate(producer)
    supplied = set()
    holes = set()
    records = []
    for entry in binding:
        require(len(entry) == 3, "EXP3-BINDING-MALFORMED", repr(entry))
        pindex, slot, hole = entry
        require(0 <= pindex < len(producers), "EXP3-BINDING-POSITION",
                "producer index %r out of range" % (pindex,))
        require(0 <= slot < len(producers[pindex][3]), "EXP3-BINDING-POSITION",
                "output slot %r out of range" % (slot,))
        require(0 <= hole < len(body[2]), "EXP3-BINDING-POSITION",
                "hole slot %r out of range" % (hole,))
        require((pindex, slot) not in supplied, "EXP3-DUPLICATE-BINDING",
                "producer output occurrence %r bound twice" % ((pindex, slot),))
        require(hole not in holes, "EXP3-DUPLICATE-BINDING",
                "body hole %r bound twice" % (hole,))
        producer_wire = producers[pindex][0][producers[pindex][3][slot]]
        body_wire = body[0][body[2][hole]]
        require(producer_wire[1] == body_wire[1], "EXP3-TYPE-MISMATCH",
                "graft boundary: producer output carries type %s, body hole %r carries type %s"
                % (producer_wire[1], body_wire[0], body_wire[1]))
        supplied.add((pindex, slot))
        holes.add(hole)
        records.append({
            "producer": pindex,
            "output_slot": slot,
            "hole": hole,
            "producer_source": producer_wire[2],
            "producer_occurrence": producer_wire[3],
            "hole_source": body_wire[2],
            "hole_occurrence": body_wire[3],
        })
    expected = {(index, slot)
                for index, producer in enumerate(producers)
                for slot in range(len(producer[3]))}
    require(supplied == expected, "EXP3-UNUSED-PRODUCER-OUTPUT",
            "producer output occurrences %r were neither bound nor explicitly discarded"
            % (sorted(expected - supplied),))

    prefixes = tuple("arg%d/" % index for index in range(len(producers)))
    renamed_body = rename_network(body, body_prefix)
    renamed_producers = [rename_network(producer, prefixes[index])
                         for index, producer in enumerate(producers)]
    substitution = {renamed_body[2][hole]: renamed_producers[pindex][3][slot]
                    for pindex, slot, hole in binding}

    wires = {key: value for key, value in renamed_body[0].items()
             if key not in substitution}
    gates = {}
    for key, gate in renamed_body[1].items():
        gates[key] = (gate[0], gate[1], tuple(substitution.get(w, w) for w in gate[2]),
                      gate[3], gate[4], gate[5], gate[6])
    for renamed in renamed_producers:
        wires.update(renamed[0])
        gates.update(renamed[1])

    inputs = tuple(w for renamed in renamed_producers for w in renamed[2]) + \
        tuple(w for hole, w in enumerate(renamed_body[2]) if hole not in holes)
    outputs = tuple(substitution.get(w, w) for w in renamed_body[3])
    receipt = ("graft", body[4], tuple(p[4] for p in producers), tuple(records),
               outputs, prefixes)
    network = (wires, gates, inputs, outputs, receipt)
    validate(network)
    return network


# --------------------------------------------------------------------------
# validation: one declared check order, one code per failure
# --------------------------------------------------------------------------

def boundary_inventory(network):
    """Exact producer and consumer endpoints, including the ordered boundaries."""
    wires, gates, inputs, outputs, receipt = network
    producers, consumers = {}, {}

    def put(target, wid, endpoint, kind):
        require(wid in wires, "EXP3-UNKNOWN-WIRE", "unknown %s wire %r" % (kind, wid))
        if wid in target:
            # Declared precedence: a discard that consumes a wire the declared
            # output boundary requires is an illegal discard, not generic
            # implicit sharing.
            if kind == "consumer" and target[wid][0] == EXTERNAL_OUTPUT:
                raise Diagnostic(
                    "EXP3-ILLEGAL-DISCARD",
                    "wire %r is required by the declared output boundary and cannot be discarded"
                    % (wid,))
            raise Diagnostic("EXP3-IMPLICIT-SHARING",
                             "wire %r must have exactly one %s, already %r"
                             % (wid, kind, target[wid]))
        target[wid] = endpoint

    for slot, wid in enumerate(inputs):
        put(producers, wid, (EXTERNAL_INPUT, slot), "producer")
    for slot, wid in enumerate(outputs):
        put(consumers, wid, (EXTERNAL_OUTPUT, slot), "consumer")
    for gid, gate in sorted(gates.items()):
        for slot, wid in enumerate(gate[2]):
            put(consumers, wid, (gid, slot), "consumer")
        for slot, wid in enumerate(gate[3]):
            put(producers, wid, (gid, slot), "producer")
    for wid in wires:
        require(wid in producers, "EXP3-MISSING-PRODUCER", "wire %r has no producer" % (wid,))
        require(wid in consumers, "EXP3-MISSING-CONSUMER", "wire %r has no consumer" % (wid,))
    return producers, consumers


def gate_type_rule(gate):
    """(expected input types, expected output types, parameter kind)."""
    op = gate[1]
    if op == "const_Q":
        return (), (TYPE_Q,), "rational"
    if op == "const_carrier":
        return (), (TYPE_CARRIER,), "label"
    if op in ("add", "sub", "mul", "div"):
        return (TYPE_Q, TYPE_Q), (TYPE_Q,), None
    if op == "copy":
        return None, None, None
    if op == "discard":
        return None, (), None
    if op == "transport":
        return (TYPE_CARRIER,), (TYPE_CARRIER,), None
    if op == "route":
        return (TYPE_CARRIER,), (TYPE_CARRIER,), "label"
    raise Diagnostic("EXP3-UNKNOWN-PRIMITIVE", repr(op))


def validate(network) -> None:
    wires, gates, inputs, outputs, receipt = network
    for key, wire in wires.items():
        require(key == wire[0], "EXP3-ADMIN-NAME-MISMATCH", repr(key))
    for key, gate in gates.items():
        require(key == gate[0], "EXP3-ADMIN-NAME-MISMATCH", repr(key))
        require(gate[1] in ARITY, "EXP3-UNKNOWN-PRIMITIVE", repr(gate[1]))
        require((len(gate[2]), len(gate[3])) == ARITY[gate[1]], "EXP3-ARITY-MISMATCH",
                "gate %r has arity %r, declared %r"
                % (gate[0], (len(gate[2]), len(gate[3])), ARITY[gate[1]]))
        for wid in gate[2] + gate[3]:
            require(wid in wires, "EXP3-UNKNOWN-WIRE", "%r not in %r" % (wid, gate[0]))
    for wire in wires.values():
        require(bool(wire[2]), "EXP3-MISSING-SOURCE", repr(wire))
        require(bool(wire[3]), "EXP3-MISSING-OCCURRENCE", repr(wire))
    occurrences = [wire[3] for wire in wires.values()]
    require(len(set(occurrences)) == len(occurrences), "EXP3-DUPLICATE-OCCURRENCE",
            "wire occurrences must be distinct")
    gate_occurrences = [gate[5] for gate in gates.values()]
    require(len(set(gate_occurrences)) == len(gate_occurrences), "EXP3-DUPLICATE-OCCURRENCE",
            "gate occurrences must be distinct")

    for gate in gates.values():
        expected_inputs, expected_outputs, parameter_kind = gate_type_rule(gate)
        if expected_inputs is not None:
            actual = tuple(wires[w][1] for w in gate[2])
            require(actual == expected_inputs, "EXP3-TYPE-MISMATCH",
                    "gate %r expects inputs %r, wires carry %r"
                    % (gate[0], list(expected_inputs), list(actual)))
        if gate[1] == "copy":
            source_type = wires[gate[2][0]][1]
            actual = tuple(wires[w][1] for w in gate[3])
            require(actual == (source_type, source_type), "EXP3-TYPE-MISMATCH",
                    "copy gate %r must transport its input type unchanged" % (gate[0],))
        elif expected_outputs is not None:
            actual = tuple(wires[w][1] for w in gate[3])
            require(actual == expected_outputs, "EXP3-TYPE-MISMATCH",
                    "gate %r expects outputs %r, wires carry %r"
                    % (gate[0], list(expected_outputs), list(actual)))
        parameter = gate[6]
        if parameter_kind == "rational":
            require(isinstance(parameter, Fraction), "EXP3-PARAMETER-CONTRACT",
                    "const_Q gate %r needs an exact rational parameter" % (gate[0],))
        elif parameter_kind == "label":
            require(isinstance(parameter, str), "EXP3-PARAMETER-CONTRACT",
                    "gate %r needs a declared label parameter" % (gate[0],))
        else:
            require(parameter is None, "EXP3-PARAMETER-CONTRACT",
                    "gate %r carries an undeclared parameter" % (gate[0],))

    boundary_inventory(network)

    # The graft receipt declares the assembled output boundary; a network that
    # silently drops a promised output is refused.
    if isinstance(receipt, tuple) and receipt and receipt[0] == "graft":
        require(tuple(receipt[RECEIPT_BOUNDARY]) == tuple(outputs), "EXP3-ILLEGAL-DISCARD",
                "the graft receipt declares output boundary %r but the assembled network "
                "exposes %r" % (list(receipt[RECEIPT_BOUNDARY]), list(outputs)))

    # Acyclicity is the last declared check, so that a locally acyclic pair of
    # pieces cross-wired into a cycle is reported by its own code.
    topological_order(network)


def dependency_graph(network):
    """Gate dependencies through producer endpoints; raises on an unknown wire."""
    wires, gates, inputs, outputs, receipt = network
    producers, _ = boundary_inventory(network)
    dependencies = {}
    for gid, gate in gates.items():
        deps = set()
        for wid in gate[2]:
            endpoint = producers[wid]
            if endpoint[0] != EXTERNAL_INPUT:
                deps.add(endpoint[0])
        dependencies[gid] = deps
    return dependencies


def topological_order(network) -> tuple:
    """Deterministic topological order; an empty ready set is a global cycle."""
    _, gates, _, _, _ = network
    dependencies = dependency_graph(network)
    done = set()
    order = []
    remaining = set(gates)
    while remaining:
        ready = sorted(gid for gid in remaining if dependencies[gid] <= done)
        require(ready, "EXP3-GLOBAL-CYCLE",
                "no gate is ready: the assembled global graph contains an operation cycle")
        order.extend(ready)
        done.update(ready)
        remaining -= set(ready)
    return tuple(order)


def check_event_order(network, order) -> None:
    """The declared event order contract.

    An event order must (i) visit every primitive gate occurrence exactly once,
    (ii) be topological for the assembled graph, and (iii) follow the graft
    receipt's declared call order, in which every producer-region event precedes
    every body-region event.  Rule (iii) is a declared HISTORY obligation: the
    numerical result is schedule independent, but the ordered trace is not, so
    rejecting this order separates historical from numerical equality.
    """
    _, gates, _, _, receipt = network
    order = tuple(order)
    require(sorted(order) == sorted(gates), "EXP3-EVENT-ORDER-MISMATCH",
            "the event order must visit every primitive occurrence exactly once")
    dependencies = dependency_graph(network)
    done = set()
    for gid in order:
        require(dependencies[gid] <= done, "EXP3-EVENT-ORDER-MISMATCH",
                "gate %r is scheduled before its producers" % (gid,))
        done.add(gid)
    if isinstance(receipt, tuple) and receipt and receipt[0] == "graft":
        regions = receipt[RECEIPT_REGIONS]
        seen_body = False
        for gid in order:
            if gid.startswith("body/"):
                seen_body = True
            elif any(gid.startswith(prefix) for prefix in regions):
                if seen_body:
                    raise Diagnostic(
                        "EXP3-EVENT-ORDER-MISMATCH",
                        "producer-region event %r is scheduled after a body-region event" % (gid,))
            else:
                raise Diagnostic("EXP3-EVENT-ORDER-MISMATCH",
                                 "event %r belongs to no declared region" % (gid,))


# --------------------------------------------------------------------------
# evaluation: domain mode (total) and strict mode (coded failure)
# --------------------------------------------------------------------------

def _apply(gate, values):
    op = gate[1]
    if op == "const_Q":
        return [gate[6]]
    if op == "const_carrier":
        return [carrier(gate[6])]
    if op == "copy":
        return [values[0], values[0]]
    if op == "discard":
        return []
    if op == "transport":
        return [values[0]]
    if op == "route":
        require(values[0] is not UNDEFINED and values[0][1] == gate[6],
                "EXP3-PROVENANCE-MISWIRE",
                "handoff %r declares expectation %r but carries %r"
                % (gate[0], gate[6], render_value(values[0])))
        return [values[0]]
    if op == "add":
        return [values[0] + values[1]]
    if op == "sub":
        return [values[0] - values[1]]
    if op == "mul":
        return [values[0] * values[1]]
    if op == "div":
        require(values[1] != 0, "EXP3-STRICT-DIVISION-BY-ZERO",
                "gate %r divides by the exact rational 0" % (gate[0],))
        return [values[0] / values[1]]
    raise Diagnostic("EXP3-UNKNOWN-PRIMITIVE", repr(op))


def _run(network, values, strict: bool, cost=None):
    wires, gates, inputs, outputs, receipt = network
    require(len(values) == len(inputs), "EXP3-INPUT-ARITY",
            "boundary arity mismatch: %d values for %d inputs" % (len(values), len(inputs)))
    environment = dict(zip(inputs, values))
    for gid in topological_order(network):
        gate = gates[gid]
        args = [environment[w] for w in gate[2]]
        if any(isinstance(arg, _Undefined) for arg in args):
            # Strictness: no primitive observes an undefined operand, and a
            # strict discard likewise requires its producer to be defined.
            for wid in gate[3]:
                environment[wid] = UNDEFINED
            if cost is not None:
                cost.step(1)
            continue
        if strict:
            produced = _apply(gate, args)
        else:
            try:
                produced = _apply(gate, args)
            except Diagnostic as exc:
                if exc.code in DOMAIN_PREDICATE_CODES:
                    # Observation mode is total: a failing primitive domain
                    # predicate is the declared UNDEFINED outcome, exactly as
                    # Paper IV's strict numerical domain D_P is defined.
                    return ("UNDEFINED",)
                if exc.code in DECLARED_REJECTIONS:
                    return ("REJECTED", exc.code, exc.detail)
                raise
        for wid, value in zip(gate[3], produced):
            environment[wid] = value
        if cost is not None:
            cost.step(1)
    result = []
    for wid in outputs:
        value = environment.get(wid, UNDEFINED)
        if isinstance(value, _Undefined):
            return ("UNDEFINED",)
        result.append(render_value(value))
    return ("DEFINED", tuple(result))


def observe_scalar(network, values=(), cost=None):
    """The declared observation O_scalar; total on the declared domain."""
    return _run(network, values, strict=False, cost=cost)


def strict_execute(network, values=()):
    """Strict execution: raises the coded diagnostic of the first failing gate."""
    return _run(network, values, strict=True)


def constant_source_ancestry(network):
    """Per-wire set of declared constant-source labels, from the producer DAG.

    Copy transports the original source; substitution transports it unchanged;
    an external input contributes nothing.
    """
    wires, gates, inputs, outputs, receipt = network
    ancestry = {}
    for gid in topological_order(network):
        gate = gates[gid]
        if gate[1] in ("const_Q", "const_carrier"):
            origins = {gate[4]}
        else:
            origins = set()
            for wid in gate[2]:
                origins |= ancestry.get(wid, set())
        for wid in gate[3]:
            ancestry[wid] = set(origins)
    return ancestry


def observe_exact(network, values=(), cost=None):
    """The declared observation O_exact: the exact-semantics upper bound."""
    base = observe_scalar(network, values, cost=cost)
    if base[0] != "DEFINED":
        return base
    ancestry = constant_source_ancestry(network)
    outputs = tuple(network[3])
    wires = network[0]
    gates = network[1]
    return ("DEFINED", base[1],
            tuple(wires[w][1] for w in outputs),
            tuple(tuple(sorted(ancestry.get(w, set()))) for w in outputs),
            tuple(sorted((gate[4], gate[5], gate[1]) for gate in gates.values())))


def check_boundary_order(network, permutation) -> None:
    """A boundary may be reordered only through a declared typed permutation."""
    wires, gates, inputs, outputs, receipt = network
    permutation = tuple(permutation)
    require(sorted(permutation) == list(range(len(outputs))),
            "EXP3-BOUNDARY-ORDER-MISMATCH",
            "a reordered boundary requires a declared permutation of the output slots")
    reordered = tuple(outputs[index] for index in permutation)
    require(reordered == tuple(outputs), "EXP3-BOUNDARY-ORDER-MISMATCH",
            "output boundary %r reordered to %r without a declared typed permutation"
            % (list(outputs), list(reordered)))


# --------------------------------------------------------------------------
# declared fillings and closed composites
# --------------------------------------------------------------------------

FILLING_ORDER = ("beta0", "beta1", "beta2", "beta3", "beta4", "beta5", "beta_undef")
FILLING_PRODUCERS = {
    "beta0": ("q1", "q2", "q3", "q4"),
    "beta1": ("q1", "q2", "q3", "q5"),
    "beta2": ("q1", "q1", "q3", "q4"),
    "beta3": ("q5", "q2", "q3", "q4"),
    "beta4": ("q1", "q2", "q5", "q4"),
    "beta5": ("q1", "q5", "q3", "q4"),
    "beta_undef": ("q1", "q2", "q3", "u0"),
}
FILLING_VALUES = {
    "beta0": (Fraction(2), Fraction(7), Fraction(3), Fraction(5)),
    "beta1": (Fraction(2), Fraction(7), Fraction(3), Fraction(4)),
    "beta2": (Fraction(2), Fraction(2), Fraction(3), Fraction(5)),
    "beta3": (Fraction(4), Fraction(7), Fraction(3), Fraction(5)),
    "beta4": (Fraction(2), Fraction(7), Fraction(4), Fraction(5)),
    "beta5": (Fraction(2), Fraction(4), Fraction(3), Fraction(5)),
    "beta_undef": (Fraction(2), Fraction(7), Fraction(3), UNDEFINED),
}
FULL_BINDING = tuple((index, 0, index) for index in range(NHOLES))


def filling_values(filling: str) -> tuple:
    return FILLING_VALUES[filling]


def close_body(body, filling: str, validate_inputs: bool = True) -> tuple:
    """Certify the simultaneous substitution of one declared filling."""
    producers = [producer_template(name) for name in FILLING_PRODUCERS[filling]]
    return certified_substitution(body, producers, FULL_BINDING,
                                  validate_inputs=validate_inputs)


def close_with_values(body, values) -> tuple:
    """Certify a substitution by explicit constant producers (used by the
    declared error battery, never by the exhaustive search)."""
    producers = [build_constant_producer(value, "arg%d/const" % index)
                 for index, value in enumerate(values)]
    return certified_substitution(body, producers, FULL_BINDING)


def direct_composite_observation(body, filling):
    """The direct route to the same composite observation (Paper IV Theorem 5.5).

    The declared composite domain is
        D = { producer tuple is in D_Q } intersected with { body defined on the
        substituted values },
    exactly as Paper IV Equation (5.2) states.  Because strict discard requires
    its own input producer to be defined, an undefined producer makes the
    composite UNDEFINED even when the consuming body only discards the hole.
    """
    values = filling_values(filling)
    for value in values:
        if isinstance(value, _Undefined):
            return ("UNDEFINED",)
    return observe_scalar(body, values)


def body_behaviour(body, cost=None):
    """The declared F-behaviour vector plus the Paper IV compatibility check."""
    vector = []
    compatible = True
    for filling in FILLING_ORDER:
        composite = close_body(body, filling, validate_inputs=False)
        closed = observe_scalar(composite, cost=cost)
        direct = direct_composite_observation(body, filling)
        # Paper IV Theorem thm:ported-substitution-evaluation, instantiated.
        if closed != direct:
            compatible = False
        vector.append(closed)
        if cost is not None:
            cost.step(1)
            cost.observe(1)
    return tuple(vector), compatible


# --------------------------------------------------------------------------
# declared tiers
# --------------------------------------------------------------------------

GRID_FIELDS = ("dom_profile", "literals", "op_count", "operators", "support", "use_counts")


def field_value(expr, name: str, vector):
    if name == "support":
        return [index + 1 for index, count in enumerate(hole_occurrences(expr)) if count]
    if name == "use_counts":
        return list(hole_occurrences(expr))
    if name == "literals":
        return expression_literals(expr)
    if name == "operators":
        return expression_operators(expr)
    if name == "op_count":
        return [binary_gate_count(expr)]
    if name == "dom_profile":
        return ["U" if entry[0] == "UNDEFINED" else "D" for entry in vector]
    raise Diagnostic("EXP3-UNKNOWN-FIELD", repr(name))


def payload(expr, vector, fields) -> dict:
    return {
        "initial": list(vector[0]),
        "fields": {name: field_value(expr, name, vector) for name in fields},
    }


def candidate_names():
    """All 2^6 - 1 = 63 non-empty subsets of the declared field set."""
    names = []
    for size in range(1, len(GRID_FIELDS) + 1):
        for subset in combinations(GRID_FIELDS, size):
            names.append(subset)
    return names


RANKING_RULE = ("minimal by (total binary gate count of the pair, canonical encoding of the "
                "first body, canonical encoding of the second body)")


def encode_pair(expr_a, expr_b) -> tuple:
    first, second = render_expression(expr_a), render_expression(expr_b)
    if second < first:
        first, second = second, first
    return (binary_gate_count(expr_a) + binary_gate_count(expr_b), first, second)


# --------------------------------------------------------------------------
# the exhaustive context search on the declared budget
# --------------------------------------------------------------------------

def make_witness(first, second) -> dict:
    separating = None
    for index, filling in enumerate(FILLING_ORDER):
        left = first["vector"][index]
        right = second["vector"][index]
        if left != right:
            separating = {
                "filling": filling,
                "fills": list(FILLING_PRODUCERS[filling]),
                "filling_values": [render_value(value) for value in filling_values(filling)],
                "observation_left": list(left),
                "observation_right": list(right),
            }
            break
    return {
        "bodies": [first["encoding"], second["encoding"]],
        "binary_gates": [first["size"], second["size"]],
        "observation_at_beta0": list(first["vector"][0]),
        "separating_filling": separating,
        "behaviour_left": [list(entry) for entry in first["vector"]],
        "behaviour_right": [list(entry) for entry in second["vector"]],
        "fillings": list(FILLING_ORDER),
    }


def exhaustive_search(cost=None):
    by_size = expressions()
    records = []
    incompatible = []
    for size in range(MAX_BINARY_GATES + 1):
        for expr in by_size[size]:
            body = build_body(expr)
            if cost is not None:
                cost.step(1)
            vector, compatible = body_behaviour(body, cost=cost)
            if not compatible:
                incompatible.append(render_expression(expr))
            records.append({"expr": expr, "size": size, "vector": vector,
                            "encoding": render_expression(expr)})
    require(not incompatible, "EXP3-SUBSTITUTION-EVALUATION-MISMATCH",
            "certified substitution disagreed with direct body evaluation on %r"
            % (incompatible[:5],))

    def groups(keyfn):
        buckets = {}
        for record in records:
            buckets.setdefault(keyfn(record), []).append(record)
        return buckets

    initial = lambda record: (record["vector"][0],)
    base_buckets = groups(initial)
    base_insufficient = []
    for key, members in sorted(base_buckets.items(), key=lambda kv: str(kv[0])):
        if len({record["vector"] for record in members}) > 1:
            base_insufficient.append(members)

    def minimal_witness(members):
        best = None
        ordered = sorted(members, key=lambda r: (r["size"], r["encoding"]))
        for first, second in combinations(ordered, 2):
            if first["vector"] == second["vector"]:
                continue
            rank = encode_pair(first["expr"], second["expr"])
            if best is None or rank < best[0]:
                best = (rank, first, second)
        return best

    base_witness = None
    for members in base_insufficient:
        found = minimal_witness(members)
        if found is None:
            continue
        if base_witness is None or found[0] < base_witness[0]:
            base_witness = found

    grid = {}
    for subset in candidate_names():
        def keyfn(record, subset=subset):
            return (record["vector"][0],
                    tuple(tuple(field_value(record["expr"], name, record["vector"]))
                          for name in subset))
        buckets = groups(keyfn)
        bad = [members for members in buckets.values()
               if len({record["vector"] for record in members}) > 1]
        entry = {
            "fields": list(subset),
            "key": "+".join(subset),
            "classes_on_domain": len(buckets),
            "insufficient_fibres": len(bad),
            "sufficient": not bad,
            "witness": None,
        }
        if bad:
            best = None
            for members in bad:
                found = minimal_witness(members)
                if found is None:
                    continue
                if best is None or found[0] < best[0]:
                    best = found
            if best is not None:
                entry["witness"] = make_witness(best[1], best[2])
        grid[entry["key"]] = entry

    # Positive control: two distinct bodies that agree on every declared
    # filling.  Without it, every literal difference would look like a gap.
    positive = None
    for members in groups(lambda record: record["vector"]).values():
        if len(members) < 2:
            continue
        ordered = sorted(members, key=lambda r: (r["size"], r["encoding"]))
        for first, second in combinations(ordered, 2):
            rank = encode_pair(first["expr"], second["expr"])
            if positive is None or rank < positive[0]:
                positive = (rank, first, second)

    return {
        "by_size": {str(size): len(by_size[size]) for size in range(MAX_BINARY_GATES + 1)},
        "domain_size": len(records),
        "records": records,
        "base_classes": len(base_buckets),
        "base_insufficient_fibres": len(base_insufficient),
        "base_witness": base_witness,
        "grid": grid,
        "positive_control": positive,
        "compatibility_checked": len(records) * len(FILLING_ORDER),
    }


# --------------------------------------------------------------------------
# the frozen Paper IV scalar snapshot: an EXISTING BOUNDED EXAMPLE
# --------------------------------------------------------------------------

def build_paper4_snapshot_body() -> tuple:
    """y1 = x1+x2, y2 = x3*x4, y3 = (x1+x3)/(x2-x4), with explicit copies."""
    builder = Builder("piv")
    holes = [builder.input("x%d" % index) for index in range(1, 5)]
    copies = [_fanout(builder, "copy%d" % index, hole, 2)
              for index, hole in enumerate(holes, 1)]
    y1 = builder.gate("y1", "add", (copies[0][0], copies[1][0]))[0]
    y2 = builder.gate("y2", "mul", (copies[2][0], copies[3][0]))[0]
    numerator = builder.gate("numerator", "add", (copies[0][1], copies[2][1]))[0]
    denominator = builder.gate("denominator", "sub", (copies[1][1], copies[3][1]))[0]
    y3 = builder.gate("y3", "div", (numerator, denominator))[0]
    return builder.finish([y1, y2, y3], receipt=("paper4-snapshot",))


def build_readout_body() -> tuple:
    """A readout-shaped body y3 = 3h/f, used only for the declared f = 0 instance."""
    builder = Builder("readout")
    c = builder.input("c")
    v = builder.input("v")
    f = builder.input("f")
    h = builder.input("h")
    f1, f2 = _fanout(builder, "copy_f", f, 2)
    h1, h2 = _fanout(builder, "copy_h", h, 2)
    y1 = builder.gate("incidence", "add", (c, v))[0]
    y2 = builder.gate("frame_gap", "sub", (f1, h1))[0]
    three = builder.gate("port_arity", "const_Q", (), parameter=Fraction(3))[0]
    ports = builder.gate("ports", "mul", (three, h2))[0]
    y3 = builder.gate("ports_per_frame", "div", (ports, f2))[0]
    return builder.finish([y1, y2, y3], receipt=("readout",))


def close_body_paper4(body) -> tuple:
    producers = [producer_template(name) for name in ("q1", "q2", "q3", "q4")]
    return certified_substitution(body, producers, FULL_BINDING)


def paper4_snapshot_layer():
    body = build_paper4_snapshot_body()
    validate(body)
    alone = observe_scalar(body, (Fraction(2), Fraction(7), Fraction(3), Fraction(5)))
    composite = close_body_paper4(body)
    via_graft = observe_scalar(composite, ())
    exact = observe_exact(composite, ())
    require(alone == ("DEFINED", ("9", "15", "5/2")), "EXP3-PAPER4-SNAPSHOT-MISMATCH",
            "the four-input body evaluated alone gave %r" % (list(alone),))
    require(via_graft == ("DEFINED", ("9", "15", "5/2")), "EXP3-PAPER4-SNAPSHOT-MISMATCH",
            "the certified composite gave %r" % (list(via_graft),))
    require(exact == via_graft or exact[1] == via_graft[1], "EXP3-PAPER4-SNAPSHOT-MISMATCH",
            "O_scalar and O_exact disagree numerically")
    constants = [gate for gate in composite[1].values() if gate[1] == "const_Q"]
    copies = [gate for gate in composite[1].values() if gate[1] == "copy"]
    require(len(constants) == 8, "EXP3-PAPER4-SNAPSHOT-MISMATCH",
            "expected eight constant sources, found %d" % (len(constants),))
    require(len({gate[4] for gate in constants}) == 8, "EXP3-PAPER4-SNAPSHOT-MISMATCH",
            "the eight constant sources must be distinct")
    require(len(copies) == 4, "EXP3-PAPER4-SNAPSHOT-MISMATCH",
            "expected four explicit copy gates, found %d" % (len(copies),))
    return {
        "status": ("EXISTING BOUNDED EXAMPLE reproduced here for compatibility; NOT new, NOT "
                   "native Adva execution, and NOT a faithful AES motion"),
        "provenance": "paper-4/sections/05b-ported-aes-programs.tex, Example ex:ported-four-puncture",
        "producers": {
            "q1": {"expression": "1 + 1", "value": "2"},
            "q2": {"expression": "3 + 4", "value": "7"},
            "q3": {"expression": "6 / 2", "value": "3"},
            "q4": {"expression": "9 - 4", "value": "5"},
        },
        "body": "y1 = x1 + x2; y2 = x3 * x4; y3 = (x1 + x3) / (x2 - x4)",
        "output_via_graft": list(via_graft[1]),
        "output_body_alone": list(alone[1]),
        "agrees": via_graft == alone,
        "primitive_gate_count": len(composite[1]),
        "constant_source_count": len(constants),
        "distinct_constant_sources": len({gate[4] for gate in constants}),
        "copy_gate_count": len(copies),
        "output_constant_ancestry_sizes": [len(entry) for entry in exact[3]],
        "strict_domain_note": "the composite is defined exactly when x2 - x4 is not 0",
    }


# --------------------------------------------------------------------------
# the declared carrier / provenance layer
# --------------------------------------------------------------------------

def build_carrier_body(name: str) -> tuple:
    builder = Builder("carrier-%s" % name)
    hole = builder.input("k1", TYPE_CARRIER)
    hole_source = builder.wires[hole][2]
    if name == "cb_pass":
        out = builder.gate("handoff", "transport", (hole,),
                           output_type=TYPE_CARRIER, output_source=hole_source)[0]
    elif name == "cb_fresh_L":
        builder.gate("drop", "discard", (hole,))
        out = builder.gate("fresh", "const_carrier", (), parameter="L",
                           output_type=TYPE_CARRIER)[0]
    elif name == "cb_fresh_M":
        builder.gate("drop", "discard", (hole,))
        out = builder.gate("fresh", "const_carrier", (), parameter="M",
                           output_type=TYPE_CARRIER)[0]
    elif name == "cb_route_L":
        out = builder.gate("handoff", "route", (hole,), parameter="L",
                           output_type=TYPE_CARRIER, output_source=hole_source)[0]
    else:
        raise Diagnostic("EXP3-UNKNOWN-CARRIER-BODY", repr(name))
    return builder.finish([out], receipt=("carrier-body", name))


CARRIER_BODIES = ("cb_pass", "cb_fresh_L", "cb_fresh_M", "cb_route_L")
CARRIER_FILLINGS = {"gamma_L": "pc_L", "gamma_M": "pc_M"}


def close_carrier_body(body, filling: str) -> tuple:
    producer = producer_template(CARRIER_FILLINGS[filling])
    return certified_substitution(body, [producer], ((0, 0, 0),))


def _exact_render(exact):
    if exact[0] != "DEFINED":
        return list(exact)
    return {"status": exact[0],
            "values": list(exact[1]),
            "output_types": list(exact[2]),
            "output_constant_ancestry": [list(entry) for entry in exact[3]],
            "gate_inventory": [list(entry) for entry in exact[4]]}


def carrier_layer():
    entries = {}
    for name in CARRIER_BODIES:
        body = build_carrier_body(name)
        validate(body)
        row = {}
        for filling in ("gamma_L", "gamma_M"):
            composite = close_carrier_body(body, filling)
            row[filling] = {
                "observation": list(observe_scalar(composite, ())),
                "exact": _exact_render(observe_exact(composite, ())),
            }
        entries[name] = row
    return entries


def carrier_witnesses(layer):
    """The declared provenance witnesses, read off the carrier layer."""
    value_pair = {
        "bodies": ["cb_pass", "cb_fresh_L"],
        "same_under": "gamma_L",
        "observation_under_gamma_L": layer["cb_pass"]["gamma_L"]["observation"],
        "observation_under_gamma_M": {
            "cb_pass": layer["cb_pass"]["gamma_M"]["observation"],
            "cb_fresh_L": layer["cb_fresh_L"]["gamma_M"]["observation"],
        },
        "kind": "same carrier label under one legal filling, different labels under another",
    }
    legality_pair = {
        "bodies": ["cb_pass", "cb_route_L"],
        "same_under": "gamma_L",
        "observation_under_gamma_L": layer["cb_pass"]["gamma_L"]["observation"],
        "observation_under_gamma_M": {
            "cb_pass": layer["cb_pass"]["gamma_M"]["observation"],
            "cb_route_L": layer["cb_route_L"]["gamma_M"]["observation"],
        },
        "kind": "carrier value under one legal filling, declared rejection under another",
    }
    return {"carrier_value_witness": value_pair, "carrier_legality_witness": legality_pair}


# --------------------------------------------------------------------------
# the frozen hand table, tied to the contract
# --------------------------------------------------------------------------

def verify_hand_table(contract_document, paper4):
    """Re-derive every hand-computed value declared in the frozen contract."""
    table = contract_document["independent_check"]["hand_computed_witnesses"]
    observed = {}
    observed["producer_values"] = {
        name: observe_scalar(producer_template(name), ())[1][0]
        if observe_scalar(producer_template(name), ())[0] == "DEFINED" else "UNDEFINED"
        for name in PRODUCER_ORDER
    }
    observed["beta0_values_of_holes"] = [
        render_value(value) for value in filling_values("beta0")
    ]
    observed["beta0_value_of_h1"] = observe_scalar(close_body(build_body(("var", 1)), "beta0"), ())[1][0]
    observed["beta0_value_of_const(2)"] = observe_scalar(close_body(build_body(("const", 2)), "beta0"), ())[1][0]
    observed["beta3_value_of_h1"] = observe_scalar(close_body(build_body(("var", 1)), "beta3"), ())[1][0]
    observed["beta3_value_of_q5"] = observe_scalar(producer_template("q5"), ())[1][0]
    observed["paper4_snapshot_output"] = list(paper4["output_via_graft"])
    for key, expected in sorted(table.items()):
        require(key in observed, "EXP3-HAND-TABLE-MISMATCH",
                "the frozen contract declares %r, which this checker does not derive" % (key,))
        require(observed[key] == expected, "EXP3-HAND-TABLE-MISMATCH",
                "%s: observed %r, the frozen contract declares %r"
                % (key, observed[key], expected))
    return observed


# --------------------------------------------------------------------------
# negative controls
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


def check_contract_digest(raw: bytes, expected: str) -> str:
    observed = gapkit.sha256_bytes(raw)
    require(observed == expected, "EXP-CONTRACT-DRIFT",
            "%s: frozen %r != actual %r" % (CONTRACT.name, expected, observed))
    return observed


def negative_controls(contract_raw: bytes, contract_sha: str, search):
    controls = []
    body = build_body(("add", ("var", 1), ("var", 2)))
    producers = [producer_template(name) for name in ("q1", "q2", "q3", "q4")]

    # 1. The frozen contract must not drift.
    controls.append({
        "id": "contract-drift",
        "expected": "EXP-CONTRACT-DRIFT",
        "observed": gapkit.reject(
            lambda: check_contract_digest(contract_raw + b"\n", contract_sha),
            "EXP-CONTRACT-DRIFT"),
    })

    # 2. Type mismatch at the graft boundary.
    def type_mismatch():
        bad = list(producers)
        wires, gates, inputs, outputs, receipt = bad[0]
        wire = wires[outputs[0]]
        wires = dict(wires)
        wires[wire[0]] = (wire[0], TYPE_CARRIER, wire[2], wire[3])
        bad[0] = (wires, gates, inputs, outputs, receipt)
        certified_substitution(body, bad, FULL_BINDING)
    controls.append({
        "id": "graft-boundary-type-mismatch",
        "expected": "EXP3-TYPE-MISMATCH",
        "observed": gapkit.reject(type_mismatch, "EXP3-TYPE-MISMATCH"),
    })

    # 3a. Strict division by zero: the Paper IV body's denominator x2 - x4.
    def denominator_zero():
        strict_execute(build_paper4_snapshot_body(),
                       (Fraction(2), Fraction(5), Fraction(3), Fraction(5)))
    controls.append({
        "id": "strict-division-by-zero-paper4-denominator",
        "expected": "EXP3-STRICT-DIVISION-BY-ZERO",
        "observed": gapkit.reject(denominator_zero, "EXP3-STRICT-DIVISION-BY-ZERO"),
    })

    # 3b. Strict division by zero: the readout-shaped body at f = 0.
    def frames_zero():
        composite = close_with_values(build_readout_body(),
                                      (Fraction(2), Fraction(1), Fraction(0), Fraction(2)))
        strict_execute(composite, ())
    controls.append({
        "id": "strict-division-by-zero-frames-zero",
        "expected": "EXP3-STRICT-DIVISION-BY-ZERO",
        "observed": gapkit.reject(frames_zero, "EXP3-STRICT-DIVISION-BY-ZERO"),
    })

    # 4. Provenance miswiring: a handoff carrying the wrong carrier label.
    # Observation mode must report the declared REJECTED outcome; strict
    # execution must raise the same declared code.
    def provenance_miswire():
        composite = close_carrier_body(build_carrier_body("cb_route_L"), "gamma_M")
        observed = observe_scalar(composite, ())
        require(observed[0] == "REJECTED" and observed[1] == "EXP3-PROVENANCE-MISWIRE",
                "EXP3-CONTROL-SETUP",
                "observation mode reported %r instead of the declared rejection" % (observed,))
        strict_execute(composite, ())
    controls.append({
        "id": "provenance-miswire",
        "expected": "EXP3-PROVENANCE-MISWIRE",
        "observed": gapkit.reject(provenance_miswire, "EXP3-PROVENANCE-MISWIRE"),
    })

    # 5a. Event order mismatch: not topological.
    def order_not_topological():
        composite = close_body_paper4(build_paper4_snapshot_body())
        check_event_order(composite, tuple(reversed(topological_order(composite))))
    controls.append({
        "id": "event-order-not-topological",
        "expected": "EXP3-EVENT-ORDER-MISMATCH",
        "observed": gapkit.reject(order_not_topological, "EXP3-EVENT-ORDER-MISMATCH"),
    })

    # 5b. Event order mismatch: topological, but a producer-region event is
    # scheduled after a body-region event, violating the declared call order.
    def order_producer_after_body():
        composite = close_body(build_body(("add", ("const", 1), ("var", 1))), "beta0")
        _, gates, _, _, _ = composite
        dependencies = dependency_graph(composite)
        done = set()
        order = []
        remaining = set(gates)
        while remaining:
            ready = [gid for gid in remaining if dependencies[gid] <= done]
            ready.sort(key=lambda gid: (0 if gid.startswith("body/") else 1, gid))
            order.append(ready[0])
            done.add(ready[0])
            remaining.discard(ready[0])
        check_event_order(composite, tuple(order))
    controls.append({
        "id": "event-order-producer-after-body",
        "expected": "EXP3-EVENT-ORDER-MISMATCH",
        "observed": gapkit.reject(order_producer_after_body, "EXP3-EVENT-ORDER-MISMATCH"),
    })

    # 6. Implicit sharing: a second consumer without an explicit copy gate.
    def implicit_sharing():
        composite = close_body(build_body(("add", ("var", 1), ("var", 1))), "beta0")
        wires, gates, inputs, outputs, receipt = composite
        target = None
        for gate in gates.values():
            if gate[1] == "copy" and gate[0].startswith("body/"):
                target = gate[3][0]
                break
        require(target is not None, "EXP3-CONTROL-SETUP", "no body copy gate found")
        gates = dict(gates)
        extra = "body/g/undeclared-extra"
        gates[extra] = (extra, "discard", (target,), (), "body/gsrc/undeclared-extra",
                        "body/ev/undeclared-extra", None)
        validate((wires, gates, inputs, outputs, receipt))
    controls.append({
        "id": "implicit-sharing",
        "expected": "EXP3-IMPLICIT-SHARING",
        "observed": gapkit.reject(implicit_sharing, "EXP3-IMPLICIT-SHARING"),
    })

    # 7. Illegal discard: a declared body output consumed by a discard.
    def illegal_discard():
        composite = close_body_paper4(build_paper4_snapshot_body())
        wires, gates, inputs, outputs, receipt = composite
        dropped = outputs[0]
        outputs = tuple(outputs[1:])
        gates = dict(gates)
        extra = "body/piv/g/drop-output"
        gates[extra] = (extra, "discard", (dropped,), (), "body/piv/gsrc/drop-output",
                        "body/piv/ev/drop-output", None)
        validate((wires, gates, inputs, outputs, receipt))
    controls.append({
        "id": "illegal-discard",
        "expected": "EXP3-ILLEGAL-DISCARD",
        "observed": gapkit.reject(illegal_discard, "EXP3-ILLEGAL-DISCARD"),
    })

    # 8. A cycle formed by cross-wiring two locally acyclic pieces.
    def cross_wired_cycle():
        wires = {}
        gates = {}
        for name in ("a", "b", "da", "db"):
            wires[name] = (name, TYPE_Q, "cycle/source/%s" % name, "cycle/wire/%s" % name)
        gates["copy-A"] = ("copy-A", "copy", ("b",), ("a", "da"), "cycle/source/CA",
                           "cycle/event/CA", None)
        gates["discard-A"] = ("discard-A", "discard", ("da",), (), "cycle/source/DA",
                              "cycle/event/DA", None)
        gates["copy-B"] = ("copy-B", "copy", ("a",), ("b", "db"), "cycle/source/CB",
                           "cycle/event/CB", None)
        gates["discard-B"] = ("discard-B", "discard", ("db",), (), "cycle/source/DB",
                              "cycle/event/DB", None)
        piece_a = ({key: wires[key] for key in ("b", "a", "da")},
                   {key: gates[key] for key in ("copy-A", "discard-A")},
                   ("b",), ("a",), ("piece", "A"))
        piece_b = ({key: wires[key] for key in ("a", "b", "db")},
                   {key: gates[key] for key in ("copy-B", "discard-B")},
                   ("a",), ("b",), ("piece", "B"))
        require(observe_scalar(piece_a, (Fraction(3),)) == ("DEFINED", ("3",)),
                "EXP3-CONTROL-SETUP", "piece A must be locally acyclic and defined")
        require(observe_scalar(piece_b, (Fraction(3),)) == ("DEFINED", ("3",)),
                "EXP3-CONTROL-SETUP", "piece B must be locally acyclic and defined")
        validate((wires, gates, (), (), ("assembly", "cross-wired")))
    controls.append({
        "id": "cross-wired-cycle",
        "expected": "EXP3-GLOBAL-CYCLE",
        "observed": gapkit.reject(cross_wired_cycle, "EXP3-GLOBAL-CYCLE"),
    })

    # 9. Unused producer output.
    def unused_producer_output():
        certified_substitution(body, producers, ((0, 0, 0), (1, 0, 1), (2, 0, 2)))
    controls.append({
        "id": "unused-producer-output",
        "expected": "EXP3-UNUSED-PRODUCER-OUTPUT",
        "observed": gapkit.reject(unused_producer_output, "EXP3-UNUSED-PRODUCER-OUTPUT"),
    })

    # 10. Duplicate binding.
    def duplicate_binding():
        certified_substitution(body, producers,
                               ((0, 0, 0), (1, 0, 0), (2, 0, 2), (3, 0, 3)))
    controls.append({
        "id": "duplicate-binding",
        "expected": "EXP3-DUPLICATE-BINDING",
        "observed": gapkit.reject(duplicate_binding, "EXP3-DUPLICATE-BINDING"),
    })

    # 11. Boundary order mismatch.
    def boundary_order_mismatch():
        composite = close_body_paper4(build_paper4_snapshot_body())
        check_boundary_order(composite, (2, 0, 1))
    controls.append({
        "id": "boundary-order-mismatch",
        "expected": "EXP3-BOUNDARY-ORDER-MISMATCH",
        "observed": gapkit.reject(boundary_order_mismatch, "EXP3-BOUNDARY-ORDER-MISMATCH"),
    })

    # 12. A bare numerical value is not an admitted input.
    controls.append({
        "id": "raw-value-input",
        "expected": "EXP3-RAW-VALUE-INPUT",
        "observed": gapkit.reject(lambda: admit_producer({"name": "bare-2", "value": "2"}),
                                  "EXP3-RAW-VALUE-INPUT"),
    })

    # 13. Value equality at beta0 is not substitutability.
    def value_equality_claim():
        witness = search["base_witness"]
        require(witness is not None, "EXP3-CONTROL-SETUP",
                "the declared budget produced no beta0 collision witness")
        separation = make_witness(witness[1], witness[2])["separating_filling"]
        require(False, "EXP3-VALUE-EQUALITY-INSUFFICIENT",
                "pi0 is not sufficient on the declared domain: %s and %s agree at beta0 and "
                "separate under %s"
                % (witness[1]["encoding"], witness[2]["encoding"], separation["filling"]))
    controls.append({
        "id": "value-equality-substitutability-claim",
        "expected": "EXP3-VALUE-EQUALITY-INSUFFICIENT",
        "observed": gapkit.reject(value_equality_claim, "EXP3-VALUE-EQUALITY-INSUFFICIENT"),
    })

    # 14. Sufficiency claim for the existing summary, refuted by the search.
    def sufficiency_claim():
        require(search["base_insufficient_fibres"] == 0,
                "EXP3-SUFFICIENCY-CLAIM-REFUTED",
                "pi0 has %d fibres on the declared domain that the declared filling family "
                "separates" % (search["base_insufficient_fibres"],))
    controls.append({
        "id": "initial-summary-sufficiency-claim",
        "expected": "EXP3-SUFFICIENCY-CLAIM-REFUTED",
        "observed": gapkit.reject(sufficiency_claim, "EXP3-SUFFICIENCY-CLAIM-REFUTED"),
    })

    # 15. Enumerated count mismatch.
    def enumerated_count_mismatch():
        # The mutation is one declared datum: the frozen count for the
        # one-binary-gate class is changed by one.
        declared = DECLARED_COUNTS["1"] - 1
        observed = search["by_size"]["1"]
        require(observed == declared, "EXP3-ENUMERATION-MISMATCH",
                "bodies with one binary gate: %d, declared %d" % (observed, declared))
    controls.append({
        "id": "enumerated-count-mismatch",
        "expected": "EXP3-ENUMERATION-MISMATCH",
        "observed": gapkit.reject(enumerated_count_mismatch, "EXP3-ENUMERATION-MISMATCH"),
    })

    # 16. Route disagreement must be detected: one observed value of the
    # secondary table is replaced by a neighbouring value before the comparison.
    def route_disagreement():
        composite = close_body(build_body(("add", ("var", 1), ("var", 2))), "beta0")
        primary = observe_scalar(composite, ())
        secondary = list(primary[1])
        secondary[-1] = "neighbour"
        require(tuple(secondary) == primary[1], "EXP3-ROUTE-DISAGREEMENT",
                "the primary route reports %r and the secondary route reports %r after the "
                "declared mutation" % (list(primary[1]), secondary))
    controls.append({
        "id": "primary-independent-disagreement",
        "expected": "EXP3-ROUTE-DISAGREEMENT",
        "observed": gapkit.reject(route_disagreement, "EXP3-ROUTE-DISAGREEMENT"),
    })
    return controls


# --------------------------------------------------------------------------
# rejected contexts, each with a reason
# --------------------------------------------------------------------------

def rejected_contexts():
    return [
        {"id": "carrier-producer-into-rational-hole",
         "context": "fill a Q hole with the CarrierID producer pc_L",
         "reason": "the graft boundary preserves types and positions; an opaque label is not a rational",
         "code": "EXP3-TYPE-MISMATCH"},
        {"id": "rational-producer-into-carrier-hole",
         "context": "fill the CarrierID hole k1 with a Q producer",
         "reason": "the graft boundary preserves types and positions",
         "code": "EXP3-TYPE-MISMATCH"},
        {"id": "partial-closure-claimed-closed",
         "context": "claim a closed composite while one hole is unbound",
         "reason": "unselected holes remain on the open frontier; the external order is producer inputs in argument order followed by the unfilled body inputs",
         "code": "EXP3-UNUSED-PRODUCER-OUTPUT"},
        {"id": "one-instance-used-twice-without-fresh-renaming",
         "context": "identify two uses of one producer occurrence instead of creating a fresh instance",
         "reason": "repeated use of a template first creates separate named instances whose occurrences are fresh; the declared renaming does exactly that, any other identification does not",
         "code": "EXP3-DUPLICATE-OCCURRENCE"},
        {"id": "unused-producer-output",
         "context": "leave a supplied producer output unconsumed",
         "reason": "every supplied output is used once; an unused output requires an explicit discard",
         "code": "EXP3-UNUSED-PRODUCER-OUTPUT"},
        {"id": "duplicate-binding",
         "context": "bind one hole twice, or one producer output occurrence twice",
         "reason": "the binding is injective on producer output occurrences and on selected holes",
         "code": "EXP3-DUPLICATE-BINDING"},
        {"id": "reordered-boundary-without-permutation",
         "context": "present an assembled boundary in a different order with no declared typed permutation",
         "reason": "sequential partial filling can induce a different order from simultaneous filling; comparison then requires a declared typed boundary permutation",
         "code": "EXP3-BOUNDARY-ORDER-MISMATCH"},
        {"id": "discard-a-declared-output",
         "context": "consume a declared body output with a discard",
         "reason": "a graft is accepted only when its boundary inventory is complete",
         "code": "EXP3-ILLEGAL-DISCARD"},
        {"id": "cross-wired-cycle",
         "context": "assemble two locally acyclic pieces by cross-wiring",
         "reason": "local acyclicity does not imply global acyclicity",
         "code": "EXP3-GLOBAL-CYCLE"},
        {"id": "bare-numerical-input",
         "context": "supply a number as a bare value rather than through an explicit constant producer",
         "reason": "a numerical input is admitted by an explicit constant producer with its source record, not by erasing the producing process",
         "code": "EXP3-RAW-VALUE-INPUT"},
        {"id": "wrong-carrier-handoff",
         "context": "hand a carrier labelled M to an interface declaring its expectation to be L",
         "reason": "the declared handoff route contract requires carrier identity at the seam",
         "code": "EXP3-PROVENANCE-MISWIRE"},
        {"id": "producer-after-body-event-order",
         "context": "schedule a producer-region event after a body-region event",
         "reason": "the graft receipt declares the call order producer-then-body; this is a HISTORY obligation because the numerical result is schedule independent",
         "code": "EXP3-EVENT-ORDER-MISMATCH"},
        {"id": "identify-bodies-by-one-filling",
         "context": "replace one open body by another because they agree under the initial filling",
         "reason": "value equality at one filling is not contextual equality; the declared search exhibits legal fillings that separate such pairs",
         "code": "EXP3-VALUE-EQUALITY-INSUFFICIENT"},
    ]


# --------------------------------------------------------------------------
# cost per tier
# --------------------------------------------------------------------------

def cost_report(search):
    domain = search["records"]
    report = {}

    cost = gapkit.Cost()
    sizes = []
    for record in domain:
        body_payload = payload(record["expr"], record["vector"], ())
        cost.store(body_payload)
        cost.step(1)
        cost.observe(1)
        sizes.append(len(gapkit.canonical(body_payload).encode("utf-8")))
    cost.verify(len(domain) * len(FILLING_ORDER))
    report["pi0"] = {
        "tier": "existing-summary",
        "cost": cost.as_record(),
        "mean_storage_bytes_per_body": qtext(Fraction(cost.storage_bytes, len(domain))),
        "max_storage_bytes_per_body": max(sizes),
    }

    grid_costs = {}
    for subset in candidate_names():
        subset_cost = gapkit.Cost()
        subset_sizes = []
        for record in domain:
            body_payload = payload(record["expr"], record["vector"], subset)
            subset_cost.store(body_payload)
            subset_cost.step(1)
            subset_cost.observe(1)
            subset_sizes.append(len(gapkit.canonical(body_payload).encode("utf-8")))
        subset_cost.verify(len(domain) * len(FILLING_ORDER))
        grid_costs["+".join(subset)] = {
            "cost": subset_cost.as_record(),
            "mean_storage_bytes_per_body": qtext(Fraction(subset_cost.storage_bytes, len(domain))),
            "max_storage_bytes_per_body": max(subset_sizes),
        }
    report["grid"] = grid_costs

    full_cost = gapkit.Cost()
    full_sizes = []
    for record in domain:
        full_payload = payload(record["expr"], record["vector"], GRID_FIELDS)
        full_cost.store(full_payload)
        full_cost.step(len(FILLING_ORDER))
        full_cost.observe(len(FILLING_ORDER))
        full_sizes.append(len(gapkit.canonical(full_payload).encode("utf-8")))
    full_cost.verify(len(domain) * len(FILLING_ORDER))
    report["pi_F"] = {
        "tier": "bounded-enhancement",
        "cost": full_cost.as_record(),
        "mean_storage_bytes_per_body": qtext(Fraction(full_cost.storage_bytes, len(domain))),
        "max_storage_bytes_per_body": max(full_sizes),
    }

    hist_cost = gapkit.Cost()
    hist_sizes = []
    for record in domain:
        body = build_body(record["expr"])
        hist_payload = {
            "wires": [wire_record(wire) for wire in body[0].values()],
            "gates": [gate_record(gate) for gate in body[1].values()],
            "receipt": list(body[4]),
        }
        hist_cost.store(hist_payload)
        hist_cost.step(len(body[1]))
        hist_cost.observe(1)
        hist_sizes.append(len(gapkit.canonical(hist_payload).encode("utf-8")))
    hist_cost.verify(len(domain) * len(FILLING_ORDER))
    report["hist"] = {
        "tier": "full-history-upper-bound",
        "cost": hist_cost.as_record(),
        "mean_storage_bytes_per_body": qtext(Fraction(hist_cost.storage_bytes, len(domain))),
        "max_storage_bytes_per_body": max(hist_sizes),
    }
    return report


def select_cheapest_sufficient(search, costs):
    """The plan's section 9 selection rule, applied to the declared grid."""
    candidates = []
    for key, entry in sorted(search["grid"].items()):
        if not entry["sufficient"]:
            continue
        cost = costs["grid"][key]["cost"]
        candidates.append((cost["structural_size"], cost["storage_bytes"], key))
    candidates.sort()
    if candidates:
        best = candidates[0]
        return {"key": best[2], "structural_size": best[0], "storage_bytes": best[1],
                "source": "declared grid"}
    full = costs["pi_F"]["cost"]
    return {"key": "pi_F", "structural_size": full["structural_size"],
            "storage_bytes": full["storage_bytes"],
            "source": "declared maximal bounded candidate",
            "note": ("no candidate in the declared 63-candidate grid is sufficient on the "
                     "declared domain, so the declared maximal bounded candidate is the "
                     "cheapest sufficient one found; this is not a minimal repair in any "
                     "proved sense")}


# --------------------------------------------------------------------------
# main
# --------------------------------------------------------------------------

def run():
    require(CONTRACT.exists(), "EXP3-CONTRACT-MISSING", str(CONTRACT))
    contract_raw = CONTRACT.read_bytes()
    frozen = read_frozen()
    require(CONTRACT.name in frozen, "EXP-CONTRACT-DRIFT",
            "%s is absent from the frozen digest ledger" % (CONTRACT.name,))
    contract_sha = check_contract_digest(contract_raw, frozen[CONTRACT.name])
    contract_document = json.loads(contract_raw.decode("utf-8"))

    by_size = expressions()
    for size in range(MAX_BINARY_GATES + 1):
        require(len(by_size[size]) == DECLARED_COUNTS[str(size)], "EXP3-ENUMERATION-MISMATCH",
                "bodies with %d binary gates: %d, declared %d"
                % (size, len(by_size[size]), DECLARED_COUNTS[str(size)]))

    search_cost = gapkit.Cost()
    search = exhaustive_search(cost=search_cost)

    witnesses = {}
    if search["base_witness"] is not None:
        witnesses["initial_filling_collision"] = make_witness(search["base_witness"][1],
                                                              search["base_witness"][2])
    if search["positive_control"] is not None:
        _, first, second = search["positive_control"]
        witnesses["positive_control"] = {
            "kind": "distinct literal bodies, declared-filling equivalent",
            "bodies": [first["encoding"], second["encoding"]],
            "binary_gates": [first["size"], second["size"]],
            "shared_behaviour": [list(entry) for entry in first["vector"]],
            "fillings": list(FILLING_ORDER),
            "note": ("the two bodies differ literally yet agree on every declared filling; this "
                     "is an equivalence, not a gap, and an enhancement that separated them "
                     "would be over-refined for the declared task"),
        }

    layer = carrier_layer()
    carrier = carrier_witnesses(layer)
    require(carrier["carrier_value_witness"]["observation_under_gamma_L"][0] == "DEFINED",
            "EXP3-CARRIER-CONTROL", "the declared carrier value witness must be defined")
    require(carrier["carrier_value_witness"]["observation_under_gamma_M"]["cb_pass"] !=
            carrier["carrier_value_witness"]["observation_under_gamma_M"]["cb_fresh_L"],
            "EXP3-CARRIER-CONTROL", "the declared carrier value witness must separate")
    require(carrier["carrier_legality_witness"]["observation_under_gamma_M"]["cb_pass"][0] ==
            "DEFINED", "EXP3-CARRIER-CONTROL", "cb_pass must stay defined under gamma_M")
    require(carrier["carrier_legality_witness"]["observation_under_gamma_M"]["cb_route_L"][0] ==
            "REJECTED", "EXP3-CARRIER-CONTROL", "the declared carrier legality witness must reject")

    paper4 = paper4_snapshot_layer()
    hand_table = verify_hand_table(contract_document, paper4)
    costs = cost_report(search)
    selection = select_cheapest_sufficient(search, costs)
    controls = negative_controls(contract_raw, contract_sha, search)

    sufficient = sorted(key for key, entry in search["grid"].items() if entry["sufficient"])
    grid_summary = {}
    for key, entry in sorted(search["grid"].items()):
        grid_summary[key] = {
            "fields": entry["fields"],
            "classes_on_domain": entry["classes_on_domain"],
            "insufficient_fibres": entry["insufficient_fibres"],
            "sufficient": entry["sufficient"],
            "witness": entry["witness"],
            }
    insufficient_witnesses = [key for key, entry in search["grid"].items()
                              if entry["witness"] is not None]

    record = {
        "schema": SCHEMA,
        "contract": {
            "path": str(CONTRACT.relative_to(ROOT.parent.parent)),
            "sha256": contract_sha,
        },
        "environment": gapkit.environ(),
        "model": {
            "interface": ("strict finite arithmetic networks with ordered typed boundaries, "
                          "explicit copy, strict discard, immutable source and occurrence "
                          "identity, and certified simultaneous substitution carrying a graft "
                          "receipt (Paper IV section 05b)"),
            "native_status": ("declared instance of the Paper IV ported-AES program interface; "
                              "NOT native Adva execution and NOT a faithful AES motion"),
            "types": [TYPE_Q, TYPE_CARRIER],
            "primitives": {op: list(ARITY[op]) for op in sorted(ARITY)},
            "evaluator_modes": [
                "observation mode: total, returns DEFINED / UNDEFINED / REJECTED",
                "strict execution mode: raises the coded diagnostic of the first failing gate",
            ],
            "substitution_evaluation_compatibility": (
                "checked for every body in the declared budget under every declared filling: "
                "the certified composite's observation equals the body's observation on the "
                "filling values, instantiating Paper IV Theorem thm:ported-substitution-evaluation"),
        },
        "domain": {
            "body_budget": {"by_binary_gates": search["by_size"], "total": search["domain_size"]},
            "hole_interface": "(h1..h4 : Q) -> (y : Q)",
            "literals": list(LITERALS),
            "operators": list(OPS),
            "filling_family": list(FILLING_ORDER),
            "filling_producers": {name: list(FILLING_PRODUCERS[name]) for name in FILLING_ORDER},
            "filling_values": {name: [render_value(value) for value in filling_values(name)]
                               for name in FILLING_ORDER},
            "carrier_bodies": list(CARRIER_BODIES),
            "carrier_fillings": sorted(CARRIER_FILLINGS),
        },
        "task": {
            "observation": ("O_scalar of the certified composite for every filling in the "
                            "declared family, with UNDEFINED and REJECTED as declared outcomes"),
            "upper_bound_observation": ("O_exact: O_scalar plus output types, constant-source "
                                        "ancestry and the gate inventory"),
            "adaptive": False,
        },
        "context_search": {
            "ranking_rule": RANKING_RULE,
            "domain_size": search["domain_size"],
            "compatibility_checks": search["compatibility_checked"],
            "initial_summary_classes": search["base_classes"],
            "initial_summary_insufficient_fibres": search["base_insufficient_fibres"],
            "declared_filling_equivalence_classes": len(
                {item["vector"] for item in search["records"]}),
            "grid_candidates": len(search["grid"]),
            "grid_candidates_insufficient": len(insufficient_witnesses),
            "grid_sufficient_candidates": sufficient,
            "grid": grid_summary,
        },
        "hand_table_check": hand_table,
        "witnesses": witnesses,
        "carrier_layer": layer,
        "carrier_witnesses": carrier,
        "paper4_snapshot": paper4,
        "cost": {"search": search_cost.as_record(), "tiers": costs},
        "selection": selection,
        "numerical_versus_contextual_equality": {
            "numerical_equality": ("two open bodies agree on O_scalar at the frozen initial "
                                   "filling beta0"),
            "contextual_equality": ("two open bodies agree on O_scalar for every filling in the "
                                    "declared family F, with UNDEFINED and REJECTED included"),
            "distinction": ("numerical equality at beta0 does not imply contextual equality: the "
                            "witnesses exhibit legal re-fillings that separate pairs which are "
                            "numerically equal at beta0, and the positive control exhibits pairs "
                            "that differ literally yet are contextually equal"),
        },
        "rejected_contexts": rejected_contexts(),
        "negative_controls": controls,
        "scope_boundary": {
            "proved": [
                "For every declared filling the certified composite's domain is the intersection "
                "of the producer domain with the body domain, exactly as Paper IV Equation (5.2) "
                "states; this is checked on the declared budget by the primary route and "
                "re-derived by the independent route.",
            ],
            "computationally_verified_example": [
                "No body summary in the declared 63-candidate grid is sufficient on the declared "
                "budget of 16648 bodies under the declared filling family of size 7.",
                "The declared maximal bounded candidate pi_F is sufficient and closed-update on "
                "the same domain.",
                "The Paper IV four-input three-output scalar snapshot reproduces exactly "
                "(9, 15, 5/2) through certified substitution.",
            ],
            "bounded_domain_compatible": [
                "Every sufficiency statement is restricted to the declared body budget and the "
                "declared filling family; no statement is made about bodies with three or more "
                "binary gates, about fillings outside F, or about carriers outside the declared "
                "finite label set.",
            ],
            "structurally_proposed": [
                "The declared carrier-expectation contract for handoffs is an abstraction of the "
                "handoff route discipline present in the pinned PR-16 record; it is a structural "
                "proposal for this interface and not a reimplementation of Adva.",
            ],
            "not_claimed": [
                "No claim that value equality is never sufficient in general, or for any richer "
                "interface.",
                "No claim that the declared filling family is complete, or that behaviour on F "
                "determines behaviour on any other filling.",
                "No claim about native Adva execution, AES motion realization, or geometry.",
                "No spectral, operator, matrix or complexity claim.",
            ],
        },
    }
    return record


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", default=None)
    args = parser.parse_args()
    record = run()
    text = gapkit.canonical(record)
    if args.out:
        Path(args.out).write_text(text, encoding="utf-8")
        written = gapkit.sha256_bytes(text.encode("utf-8"))
        sys.stderr.write("exp3 written to %s sha256=%s\n" % (args.out, written))
    else:
        sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
