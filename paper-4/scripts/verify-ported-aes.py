#!/usr/bin/env python3
"""New, independent finite checker for Paper IV's ported-AES insertion.

Standard library only; all numerical calculations use fractions.Fraction.
This is NOT the unavailable original ZIP checker or a recovery of its reported
55 checks. The graph fixtures and two event partitions below are newly authored
from the recovered eight-page draft, Version 0.1 (9 October 2026).

Run: python3 paper-4/scripts/verify-ported-aes.py
Optional: --evidence PATH writes the same deterministic JSON printed to stdout.
Checked evidence: python3 paper-4/scripts/verify-ported-aes.py --evidence
  paper-4/scripts/fixtures/ported-aes/integration-evidence.json

A check group counts one named mathematical/validation obligation, not every
assertion, sample, schedule, or rejected mutation. This finite experiment does
not prove the general substitution/descent theorems, smooth global gluing,
essentiality of ends, a gate-to-AES-motion bridge, or opposite-edge witnesses.
"""
from __future__ import annotations

import argparse
from collections import Counter
from copy import deepcopy
from dataclasses import dataclass, replace
from fractions import Fraction as F
from itertools import product
import json
from pathlib import Path
import random
import sys


class InvalidNetwork(ValueError):
    pass


class UndefinedArithmetic(ValueError):
    pass


def require(condition, message):
    # Do not use assert: verification must also work with python -O.
    if not condition:
        raise AssertionError(message)


def reject(call, fragment):
    try:
        call()
    except (InvalidNetwork, UndefinedArithmetic) as exc:
        require(fragment in str(exc), f"wrong rejection: {exc}; expected {fragment}")
        return str(exc)
    raise AssertionError(f"expected rejection containing {fragment!r}")


@dataclass(frozen=True)
class Wire:
    # Immutable syntactic source site, not a dynamically recomputed ancestry.
    # Constant ancestry is derived separately from the retained operation DAG.
    id: str
    type: str
    source: str
    occurrence: str


@dataclass(frozen=True)
class Gate:
    id: str
    op: str
    inputs: tuple[str, ...]
    outputs: tuple[str, ...]
    source: str
    occurrence: str
    parameter: F | None = None


@dataclass
class Network:
    wires: dict[str, Wire]
    gates: dict[str, Gate]
    inputs: tuple[str, ...]
    outputs: tuple[str, ...]
    receipt: tuple


ARITIES = {"const": (0, 1), "add": (2, 1), "sub": (2, 1),
           "mul": (2, 1), "div": (2, 1), "copy": (1, 2), "discard": (1, 0)}


def inventory(n):
    """Return exact producer/consumer endpoints, including ordered boundaries."""
    producers, consumers = {}, {}

    def put(target, wire, endpoint, kind):
        if wire not in n.wires:
            raise InvalidNetwork(f"unknown {kind} wire: {wire}")
        if wire in target:
            raise InvalidNetwork(f"wire must have one {kind}: {wire}")
        target[wire] = endpoint

    for slot, wire in enumerate(n.inputs):
        put(producers, wire, ("@input", slot), "producer")
    for slot, wire in enumerate(n.outputs):
        put(consumers, wire, ("@output", slot), "consumer")
    for gid, gate in sorted(n.gates.items()):
        for slot, wire in enumerate(gate.inputs):
            put(consumers, wire, (gid, slot), "consumer")
        for slot, wire in enumerate(gate.outputs):
            put(producers, wire, (gid, slot), "producer")
    if set(producers) != set(n.wires) or set(consumers) != set(n.wires):
        raise InvalidNetwork("incomplete boundary/wire inventory")
    return producers, consumers


def validate(n):
    if any(k != w.id for k, w in n.wires.items()):
        raise InvalidNetwork("wire administrative key mismatch")
    if any(k != g.id for k, g in n.gates.items()):
        raise InvalidNetwork("gate administrative key mismatch")
    for kind, records in (("wire", n.wires.values()), ("gate", n.gates.values())):
        records = list(records)
        if any(not r.source or not r.occurrence for r in records):
            raise InvalidNetwork(f"missing {kind} source or occurrence")
        if len({r.occurrence for r in records}) != len(records):
            raise InvalidNetwork(f"duplicate {kind} occurrence")
    for gate in n.gates.values():
        if gate.op not in ARITIES:
            raise InvalidNetwork(f"unknown primitive: {gate.op}")
        if (len(gate.inputs), len(gate.outputs)) != ARITIES[gate.op]:
            raise InvalidNetwork("ordered gate arity mismatch")
        if any(w not in n.wires for w in gate.inputs + gate.outputs):
            raise InvalidNetwork("unknown gate wire")
        if any(n.wires[w].type != "Q" for w in gate.inputs + gate.outputs):
            raise InvalidNetwork("gate type mismatch: rational primitive")
        if (gate.op == "const") != isinstance(gate.parameter, F):
            raise InvalidNetwork("constant parameter contract mismatch")
    producers, _ = inventory(n)
    dependencies = {
        gid: {producers[w][0] for w in g.inputs if producers[w][0] != "@input"}
        for gid, g in n.gates.items()
    }
    done = set()
    while len(done) < len(n.gates):
        ready = set(n.gates) - done
        ready = {g for g in ready if dependencies[g] <= done}
        if not ready:
            raise InvalidNetwork("global operation cycle")
        done.update(ready)
    return dependencies


def schedule(n, reverse=False, seed=None):
    deps = validate(n)
    done, order = set(), []
    rng = random.Random(seed)
    while len(done) != len(n.gates):
        ready = sorted(g for g in n.gates if g not in done and deps[g] <= done)
        g = rng.choice(ready) if seed is not None else ready[-1 if reverse else 0]
        done.add(g)
        order.append(g)
    return tuple(order)


def all_schedules(n):
    deps = validate(n)

    def visit(order, done):
        if len(done) == len(n.gates):
            yield tuple(order)
        for g in sorted(n.gates):
            if g not in done and deps[g] <= done:
                yield from visit(order + [g], done | {g})

    yield from visit([], set())


def evaluate(n, values=(), order=None):
    deps = validate(n)
    if len(values) != len(n.inputs):
        raise InvalidNetwork("input boundary arity mismatch")
    order = schedule(n) if order is None else tuple(order)
    if Counter(order) != Counter(n.gates.keys()):
        raise InvalidNetwork("schedule must visit every primitive exactly once")
    wire_values = dict(zip(n.inputs, map(F, values)))
    done, trace = set(), []
    for gid in order:
        if not deps[gid] <= done:
            raise InvalidNetwork("schedule is not topological")
        g = n.gates[gid]
        v = tuple(wire_values[w] for w in g.inputs)
        if g.op == "const":
            result = (g.parameter,)
        elif g.op == "copy":
            result = (v[0], v[0])
        elif g.op == "discard":
            result = ()  # Input read above remains strict.
        elif g.op == "div":
            if v[1] == 0:
                raise UndefinedArithmetic(f"division by zero at {g.occurrence}")
            result = (v[0] / v[1],)
        else:
            result = ({"add": lambda: v[0] + v[1],
                       "sub": lambda: v[0] - v[1],
                       "mul": lambda: v[0] * v[1]}[g.op](),)
        wire_values.update(zip(g.outputs, result))
        done.add(gid)
        trace.append(g.occurrence)
    return tuple(wire_values[w] for w in n.outputs), tuple(trace)


def outcome(n, values=()):
    try:
        return evaluate(n, values)[0]
    except UndefinedArithmetic:
        return None


class Builder:
    """Distinct instances have fresh occurrences but may retain template sources."""
    def __init__(self, instance, template=None):
        self.instance = instance
        self.template = template or instance
        self.wires, self.gates, self.inputs = {}, {}, []

    def wire(self, label, source):
        self.wires[label] = Wire(label, "Q", source, f"{self.instance}/wire/{label}")
        return label

    def input(self, label):
        w = self.wire(label, f"{self.template}/input/{label}")
        self.inputs.append(w)
        return w

    def gate(self, label, op, inputs=(), parameter=None):
        source = f"{self.template}/gate/{label}"
        # Copy transports the original source, creating two distinct occurrences.
        out_source = self.wires[inputs[0]].source if op == "copy" else source
        outputs = tuple(self.wire(f"{label}:{i}", out_source)
                        for i in range(ARITIES[op][1]))
        self.gates[label] = Gate(label, op, tuple(inputs), outputs, source,
                                 f"{self.instance}/gate/{label}",
                                 F(parameter) if parameter is not None else None)
        return outputs

    def finish(self, outputs):
        n = Network(self.wires, self.gates, tuple(self.inputs), tuple(outputs),
                    ("instance", self.instance, self.template))
        validate(n)
        return n


def rename(n, prefix):
    """Administrative renaming NEVER refreshes sources or occurrences."""
    return Network(
        {prefix + w.id: replace(w, id=prefix + w.id) for w in n.wires.values()},
        {prefix + g.id: replace(g, id=prefix + g.id,
                               inputs=tuple(prefix + w for w in g.inputs),
                               outputs=tuple(prefix + w for w in g.outputs))
         for g in n.gates.values()},
        tuple(prefix + w for w in n.inputs), tuple(prefix + w for w in n.outputs),
        n.receipt)


def substitute(body, producers, binding):
    """binding is an ordered tuple of (producer index, output slot, hole slot).

    Bound body-input segments are contracted. Their immutable boundary contracts
    remain in the receipt; primitive events and their sources are never deleted.
    Open frontier: producer inputs in argument order, then unfilled body inputs.
    """
    for n in [body] + list(producers):
        validate(n)
    expected = {(p, s) for p, q in enumerate(producers) for s in range(len(q.outputs))}
    supplied, holes = set(), set()
    records = []
    for p, s, h in binding:
        if (p, s) not in expected or not 0 <= h < len(body.inputs):
            raise InvalidNetwork("binding position out of range")
        if (p, s) in supplied or h in holes:
            raise InvalidNetwork("duplicate binding")
        supplied.add((p, s))
        holes.add(h)
        qw, bw = producers[p].wires[producers[p].outputs[s]], body.wires[body.inputs[h]]
        if qw.type != bw.type:
            raise InvalidNetwork("binding type mismatch")
        records.append((p, s, h, qw.source, qw.occurrence, bw.source, bw.occurrence))
    if supplied != expected:
        raise InvalidNetwork("unused producer output requires explicit discard")
    b = rename(body, "body/")
    qs = [rename(q, f"arg{p}/") for p, q in enumerate(producers)]
    substitutions = {b.inputs[h]: qs[p].outputs[s] for p, s, h in binding}
    wires = {w: data for w, data in b.wires.items() if w not in substitutions}
    gates = {gid: replace(g, inputs=tuple(substitutions.get(w, w) for w in g.inputs))
             for gid, g in b.gates.items()}
    for q in qs:
        wires.update(q.wires)
        gates.update(q.gates)
    n = Network(wires, gates,
                tuple(w for q in qs for w in q.inputs) +
                tuple(w for h, w in enumerate(b.inputs) if h not in holes),
                tuple(substitutions.get(w, w) for w in b.outputs),
                ("substitute", body.receipt, tuple(q.receipt for q in producers), tuple(records)))
    validate(n)
    return n


def operation_signature(n):
    """Occurrence-labelled graph normal form, forgetting only admin names/receipt."""
    validate(n)
    wocc = lambda w: n.wires[w].occurrence
    return (
        tuple(sorted((w.occurrence, w.source, w.type) for w in n.wires.values())),
        tuple(sorted((g.occurrence, g.source, g.op, g.parameter,
                      tuple(map(wocc, g.inputs)), tuple(map(wocc, g.outputs)))
                     for g in n.gates.values())),
        tuple(map(wocc, n.inputs)), tuple(map(wocc, n.outputs)))


def transport_certificate(left, right):
    require(operation_signature(left) == operation_signature(right),
            "no occurrence/source-preserving operation-graph isomorphism")
    rg = {g.occurrence: g.id for g in right.gates.values()}
    rw = {w.occurrence: w.id for w in right.wires.values()}
    return {"gates": {g.id: rg[g.occurrence] for g in left.gates.values()},
            "wires": {w.id: rw[w.occurrence] for w in left.wires.values()}}


def producer(instance, op, a, b, template=None):
    p = Builder(instance, template)
    a, = p.gate("a", "const", parameter=a)
    b, = p.gate("b", "const", parameter=b)
    out, = p.gate("operation", op, (a, b))
    return p.finish((out,))


def experiment():
    qs = [producer("q1", "add", 1, 1), producer("q2", "add", 3, 4),
          producer("q3", "div", 6, 2), producer("q4", "sub", 9, 4)]
    b = Builder("body")
    h = [b.input(f"h{i}") for i in range(1, 5)]
    x = [b.gate(f"copy{i}", "copy", (w,)) for i, w in enumerate(h, 1)]
    y1, = b.gate("y1", "add", (x[0][0], x[1][0]))
    y2, = b.gate("y2", "mul", (x[2][0], x[3][0]))
    num, = b.gate("numerator", "add", (x[0][1], x[2][1]))
    den, = b.gate("denominator", "sub", (x[1][1], x[3][1]))
    y3, = b.gate("y3", "div", (num, den))
    body = b.finish((y1, y2, y3))
    n = substitute(body, qs, tuple((i, 0, i) for i in range(4)))
    return qs, body, n


def wire_record(w):
    return {"id": w.id, "type": w.type, "source": w.source, "occurrence": w.occurrence}


def gate_record(g):
    return {"id": g.id, "op": g.op, "inputs": list(g.inputs), "outputs": list(g.outputs),
            "source": g.source, "occurrence": g.occurrence,
            "parameter": str(g.parameter) if g.parameter is not None else None}


def seams(n, regions):
    producers, consumers = inventory(n)
    out = []
    for wid in sorted(n.wires):
        p, c = producers[wid], consumers[wid]
        pr, cr = regions.get(p[0], p[0]), regions.get(c[0], c[0])
        if pr != cr:
            out.append({"wire": wire_record(n.wires[wid]), "from": [pr, *p], "to": [cr, *c]})
    return out


def package_regions(n, regions):
    """New packet format; no original recovered packet data is assumed."""
    if set(regions) != set(n.gates):
        raise InvalidNetwork("region gate inventory mismatch")
    boundary = seams(n, regions)
    packets = []
    for r in sorted(set(regions.values())):
        gates = [g for gid, g in sorted(n.gates.items()) if regions[gid] == r]
        ids = {w for g in gates for w in g.inputs + g.outputs}
        packets.append({"region": r, "gates": [gate_record(g) for g in gates],
                        "wires": [wire_record(n.wires[w]) for w in sorted(ids)],
                        "incoming": [s for s in boundary if s["to"][0] == r],
                        "outgoing": [s for s in boundary if s["from"][0] == r]})
    contract = {"regions": dict(sorted(regions.items())),
                "gate_manifest": {g.id: [g.source, g.occurrence, g.op,
                                          str(g.parameter) if g.parameter is not None else None]
                                  for g in n.gates.values()},
                "wire_ids": sorted(n.wires), "inputs": list(n.inputs),
                "outputs": list(n.outputs), "seams": boundary}
    # Prove the assembler consumes detached data, not the original Python object.
    return json.loads(json.dumps({"packets": packets, "contract": contract}, sort_keys=True))


def assemble(bundle):
    packets, contract = bundle["packets"], bundle["contract"]
    wires, gates, regions = {}, {}, {}
    packet_regions = [p["region"] for p in packets]
    if len(set(packet_regions)) != len(packet_regions):
        raise InvalidNetwork("duplicate packet region")
    for packet in packets:
        r = packet["region"]
        local_wires = set()
        for record in packet["wires"]:
            w = Wire(**record)
            if w.id in local_wires:
                raise InvalidNetwork("duplicate local wire inventory")
            local_wires.add(w.id)
            if w.id in wires and wires[w.id] != w:
                raise InvalidNetwork("seam wire metadata mismatch")
            wires[w.id] = w
        used = set()
        for record in packet["gates"]:
            g = Gate(**{**record, "inputs": tuple(record["inputs"]),
                        "outputs": tuple(record["outputs"]),
                        "parameter": F(record["parameter"]) if record["parameter"] is not None else None})
            if g.id in gates:
                raise InvalidNetwork("duplicate packet gate")
            gates[g.id], regions[g.id] = g, r
            used.update(g.inputs + g.outputs)
        if used != local_wires:
            raise InvalidNetwork("unaccounted local packet wire")
    if regions != contract["regions"] or sorted(wires) != contract["wire_ids"]:
        raise InvalidNetwork("incomplete assembly inventory")
    manifest = {g.id: [g.source, g.occurrence, g.op,
                       str(g.parameter) if g.parameter is not None else None]
                for g in gates.values()}
    if manifest != contract["gate_manifest"]:
        raise InvalidNetwork("assembly gate source/occurrence/parameter mismatch")
    n = Network(wires, gates, tuple(contract["inputs"]), tuple(contract["outputs"]),
                ("assembly", tuple(sorted(packet_regions))))
    expected = seams(n, regions)
    if expected != contract["seams"]:
        raise InvalidNetwork("ordered seam contract mismatch")
    for packet in packets:
        r = packet["region"]
        if (packet["incoming"] != [s for s in expected if s["to"][0] == r] or
                packet["outgoing"] != [s for s in expected if s["from"][0] == r]):
            raise InvalidNetwork("packet exposed frontier mismatch")
    validate(n)  # Local acyclicity alone is deliberately insufficient.
    return n


def positive_arithmetic():
    qs, body, n = experiment()
    require(tuple(evaluate(q)[0][0] for q in qs) == (F(2), F(7), F(3), F(5)), "producer values")
    require(evaluate(n)[0] == (F(9), F(15), F(5, 2)), "four-input output")
    require(evaluate(body, (2, 7, 3, 5))[0] == evaluate(n)[0], "substitution evaluation")
    constants = [g for g in n.gates.values() if g.op == "const"]
    require(len(constants) == len({g.source for g in constants}) == 8, "eight constant sources")
    copies = [g for g in n.gates.values() if g.op == "copy"]
    require(len(copies) == 4 and all(n.wires[g.outputs[0]].occurrence != n.wires[g.outputs[1]].occurrence
                                   for g in copies), "explicit distinct copy occurrences")
    ancestry = {}
    for gid in schedule(n):
        g = n.gates[gid]
        origins = {g.source} if g.op == "const" else set().union(*(ancestry[w] for w in g.inputs))
        for wire in g.outputs:
            ancestry[wire] = origins
    require(tuple(len(ancestry[w]) for w in n.outputs) == (4, 4, 8),
            "constant-source ancestry must survive copies and substitution")
    return {"output": ["9", "15", "5/2"], "primitive_gates": len(n.gates), "constant_sources": 8,
            "output_constant_ancestry_sizes": [4, 4, 8]}


def positive_identity_transport():
    qs, body, n = experiment()
    before = Counter((g.source, g.occurrence, g.op, g.parameter)
                     for p in [body] + qs for g in p.gates.values())
    after = Counter((g.source, g.occurrence, g.op, g.parameter) for g in n.gates.values())
    require(before == after, "substitution changed primitive identities")
    after_events = {g.occurrence: g for g in n.gates.values()}
    bound = {body.inputs[i]: qs[i].wires[qs[i].outputs[0]].occurrence for i in range(4)}
    for original in [body] + qs:
        for g in original.gates.values():
            transported = after_events[g.occurrence]
            expected_inputs = tuple(bound[w] if original is body and w in bound
                                    else original.wires[w].occurrence for w in g.inputs)
            require(tuple(n.wires[w].occurrence for w in transported.inputs) == expected_inputs,
                    "substitution changed an ordered primitive input slot")
            require(tuple(n.wires[w].occurrence for w in transported.outputs) ==
                    tuple(original.wires[w].occurrence for w in g.outputs),
                    "substitution changed an ordered primitive output slot")
    renamed = rename(n, "fresh/")
    cert = transport_certificate(n, renamed)
    require(len(cert["gates"]) == len(n.gates), "incomplete administrative transport")
    q1 = producer("instance-A", "add", 1, 1, "template")
    q2 = producer("instance-B", "add", 1, 1, "template")
    require({g.source for g in q1.gates.values()} == {g.source for g in q2.gates.values()}, "template sources")
    require({g.occurrence for g in q1.gates.values()}.isdisjoint(g.occurrence for g in q2.gates.values()),
            "template reuse must create fresh occurrences")
    return {"transported_gates": len(cert["gates"]), "transported_wires": len(cert["wires"])}


def negative_resource_binding():
    qs, body, n = experiment()
    bad = deepcopy(n)
    g = next(g for g in bad.gates.values() if g.op == "copy")
    bad.outputs += (g.inputs[0],)
    reject(lambda: validate(bad), "one consumer")
    binding = tuple((i, 0, i) for i in range(4))
    reject(lambda: substitute(body, qs, binding + ((0, 0, 0),)), "duplicate binding")
    reject(lambda: substitute(body, qs, binding[:-1]), "unused producer output")
    # A typed identity interface is valid at any type; plugging Bool into Q is not.
    w = Wire("b", "Bool", "boolean/source", "boolean/occurrence")
    boolean = Network({"b": w}, {}, ("b",), ("b",), ("boolean identity",))
    validate(boolean)
    reject(lambda: substitute(body, [boolean], ((0, 0, 0),)), "binding type mismatch")
    reject(lambda: substitute(body, [qs[0], qs[0]], ((0, 0, 0), (1, 0, 1))), "duplicate wire occurrence")
    return {"rejected": ["implicit sharing", "duplicate binding", "unused output",
                          "type mismatch", "reuse without fresh instance"]}


def positive_partial_frontier():
    b = Builder("partial-body")
    h0, h1 = b.input("h0"), b.input("h1")
    out, = b.gate("difference", "sub", (h0, h1))
    body = b.finish((out,))
    p = Builder("open-producer")
    u = p.input("u")
    one, = p.gate("one", "const", parameter=1)
    value, = p.gate("increment", "add", (u, one))
    q = p.finish((value,))
    n = substitute(body, [q], ((0, 0, 1),))
    require(tuple(n.wires[w].occurrence for w in n.inputs) ==
            ("open-producer/wire/u", "partial-body/wire/h0"), "partial frontier order")
    require(evaluate(n, (4, 10))[0] == (F(5),), "partial frontier evaluation")
    other = Builder("other-open-producer")
    v = other.input("v")
    two, = other.gate("two", "const", parameter=2)
    doubled, = other.gate("double", "mul", (v, two))
    other = other.finish((doubled,))
    simultaneous = substitute(body, [q, other], ((0, 0, 0), (1, 0, 1)))
    first = substitute(body, [q], ((0, 0, 0),))
    sequential = substitute(first, [other], ((0, 0, 1),))
    simultaneous_order = tuple(simultaneous.wires[w].occurrence for w in simultaneous.inputs)
    sequential_order = tuple(sequential.wires[w].occurrence for w in sequential.inputs)
    require(simultaneous_order == ("open-producer/wire/u", "other-open-producer/wire/v"),
            "simultaneous open frontier order")
    require(sequential_order == tuple(reversed(simultaneous_order)), "expected sequential frontier permutation")
    permutation = (1, 0)  # position i of normalized frontier takes sequential slot permutation[i].
    permuted = replace(sequential, inputs=tuple(sequential.inputs[i] for i in permutation))
    require(tuple(permuted.wires[w].type for w in permuted.inputs) ==
            tuple(simultaneous.wires[w].type for w in simultaneous.inputs), "typed boundary permutation")
    require(operation_signature(sequential) != operation_signature(simultaneous),
            "must not silently identify differently ordered boundaries")
    transport_certificate(permuted, simultaneous)
    require(evaluate(simultaneous, (3, 4))[0] == evaluate(sequential, (4, 3))[0] ==
            evaluate(permuted, (3, 4))[0] == (F(-4),), "explicit permuted open substitution evaluation")
    return {"frontier": ["producer.u", "unfilled-body.h0"], "sample_output": ["5"],
            "simultaneous_frontier": ["u", "v"], "sequential_frontier": ["v", "u"],
            "typed_normalization_permutation": list(permutation), "permuted_output": ["-4"]}


def positive_exact_domain():
    q = Builder("division-producer")
    u, v = q.input("u"), q.input("v")
    result, = q.gate("divide", "div", (u, v))
    q = q.finish((result,))
    p = Builder("division-body")
    h, z = p.input("h"), p.input("z")
    result, = p.gate("divide", "div", (h, z))
    p = p.finish((result,))
    n = substitute(p, [q], ((0, 0, 0),))
    legal = 0
    for u, v, z in product((-1, 0, 1), repeat=3):
        qv = outcome(q, (u, v))
        nested = None if qv is None else outcome(p, qv + (F(z),))
        flat = outcome(n, (u, v, z))
        require(flat == nested, "partial domain/evaluation compatibility")
        require((flat is not None) == (v != 0 and z != 0), "strict exact domain predicate")
        legal += flat is not None
    return {"rational_inputs": 27, "defined": legal, "undefined": 27 - legal,
            "domain": "v != 0 and z != 0 (on the tested grid)"}


def negative_strict_discard():
    q = producer("bad-division", "div", 1, 0)
    p = Builder("discard-body")
    h = p.input("h")
    p.gate("discard", "discard", (h,))
    good, = p.gate("visible", "const", parameter=7)
    p = p.finish((good,))
    n = substitute(p, [q], ((0, 0, 0),))
    reject(lambda: evaluate(n), "division by zero")
    reject(lambda: evaluate(n, order=schedule(n, reverse=True)), "division by zero")
    require(evaluate(p, (0,))[0] == (F(7),), "defined discard body")
    return {"discarded_producer": "1/0", "composite": "undefined", "body_alone": ["7"]}


def positive_schedule_independence():
    qs, _, n = experiment()
    orders = {schedule(n), schedule(n, reverse=True)}
    orders.update(schedule(n, seed=i) for i in range(16))
    traces = set()
    for order in orders:
        values, trace = evaluate(n, order=order)
        require(values == (F(9), F(15), F(5, 2)), "schedule-dependent arithmetic")
        traces.add(trace)
    # Exhaustive finite schedule check for two independent producer branches.
    a, b = rename(qs[0], "a/"), rename(qs[1], "b/")
    small = Network({**a.wires, **b.wires}, {**a.gates, **b.gates}, (), a.outputs + b.outputs, ("parallel",))
    exhaustive = list(all_schedules(small))
    require(len(exhaustive) == 80, "two three-event branches have 80 schedules")
    for order in exhaustive:
        require(evaluate(small, order=order)[0] == (F(2), F(7)), "small schedule output")
    require(len(traces) > 1, "operational traces were incorrectly identified")
    reject(lambda: evaluate(n, order=tuple(reversed(schedule(n)))), "not topological")
    return {"main_network_schedules_sampled": len(orders), "small_network_schedules_exhausted": len(exhaustive),
            "traces_distinct": True}


def positive_association_receipts():
    q = Builder("assoc-q")
    val, = q.gate("two", "const", parameter=2)
    q = q.finish((val,))
    p = Builder("assoc-p")
    h = p.input("h")
    c, = p.gate("three", "const", parameter=3)
    y, = p.gate("add", "add", (h, c))
    p = p.finish((y,))
    r = Builder("assoc-r")
    h = r.input("h")
    c, = r.gate("four", "const", parameter=4)
    y, = r.gate("multiply", "mul", (h, c))
    r = r.finish((y,))
    left = substitute(r, [substitute(p, [q], ((0, 0, 0),))], ((0, 0, 0),))
    right = substitute(substitute(r, [p], ((0, 0, 0),)), [q], ((0, 0, 0),))
    cert = transport_certificate(left, right)
    require(left.receipt != right.receipt, "literal call receipts collapsed")
    require(evaluate(left)[0] == evaluate(right)[0] == (F(20),), "associative scalar output")
    w = q.wires[q.outputs[0]]
    identity = Network({w.id: w}, {}, (w.id,), (w.id,), ("identity", w.source, w.occurrence))
    composed = substitute(identity, [q], ((0, 0, 0),))
    transport_certificate(composed, q)  # Left identity: Id o q.
    in_wire = p.wires[p.inputs[0]]
    input_identity = Network({in_wire.id: in_wire}, {}, (in_wire.id,), (in_wire.id,),
                             ("identity", in_wire.source, in_wire.occurrence))
    right_identity = substitute(p, [input_identity], ((0, 0, 0),))
    transport_certificate(right_identity, p)  # Right identity: p o Id.
    require(evaluate(right_identity, (5,))[0] == evaluate(p, (5,))[0] == (F(8),),
            "right identity numerical/interface law")
    return {"output": ["20"], "isomorphism_gate_pairs": sorted(cert["gates"].items()),
            "receipts_distinct": True, "left_identity_contract_preserved": True,
            "right_identity_contract_preserved": True}


def negative_endpoint_history_collapse():
    q = producer("sum-two", "add", 1, 1)
    b = Builder("literal-two")
    w, = b.gate("constant", "const", parameter=2)
    literal = b.finish((w,))
    require(evaluate(q)[0] == evaluate(literal)[0] == (F(2),), "equal endpoint controls")
    require(operation_signature(q) != operation_signature(literal), "endpoint collapsed graph")
    require(q.receipt != literal.receipt, "endpoint collapsed receipt")
    return {"same_output": ["2"], "gate_counts": [len(q.gates), len(literal.gates)], "histories_distinct": True}


def independent_partitions(n):
    # These partitions are newly declared event regions, NOT recovered original
    # geometric gate placements. The chapter attaches no gate motion to a point.
    out = []
    for selected in (("q1/", "q3/"), ("q2/", "q4/")):
        out.append({gid: ("inner" if g.occurrence.startswith(selected) or
                          g.occurrence in {"body/gate/copy1", "body/gate/copy3", "body/gate/numerator", "body/gate/y1"}
                          else "outer") for gid, g in n.gates.items()})
    return out


def positive_seam_reassembly():
    _, _, n = experiment()
    counts = []
    for regions in independent_partitions(n):
        bundle = package_regions(n, regions)
        restored = assemble(bundle)
        transport_certificate(n, restored)
        require(evaluate(restored)[0] == (F(9), F(15), F(5, 2)), "seam reassembly output")
        internal = [s for s in bundle["contract"]["seams"] if s["to"][0] != "@output"]
        directions = {(s["from"][0], s["to"][0]) for s in internal}
        require({("inner", "outer"), ("outer", "inner")} <= directions,
                "expected alternating coarse seam frontier")
        counts.append(len(internal))
    require(independent_partitions(n)[0] != independent_partitions(n)[1], "different partitions required")
    return {"independent_event_partitions": 2, "internal_seam_wire_counts": counts,
            "global_output": ["9", "15", "5/2"], "coarse_region_cycle_with_global_DAG": True}


def negative_seam_inventory():
    _, _, n = experiment()
    bundle = package_regions(n, independent_partitions(n)[0])
    missing = deepcopy(bundle)
    missing["contract"]["seams"].pop()
    reject(lambda: assemble(missing), "ordered seam contract mismatch")
    frontier = deepcopy(bundle)
    frontier["packets"][0]["incoming"].pop()
    reject(lambda: assemble(frontier), "packet exposed frontier mismatch")
    source = deepcopy(bundle)
    shared = set(w["id"] for w in source["packets"][0]["wires"]) & set(w["id"] for w in source["packets"][1]["wires"])
    wid = sorted(shared)[0]
    next(w for w in source["packets"][1]["wires"] if w["id"] == wid)["source"] += "/tampered"
    reject(lambda: assemble(source), "seam wire metadata mismatch")
    gate = deepcopy(bundle)
    gate["packets"][0]["gates"].pop()
    reject(lambda: assemble(gate), "unaccounted local packet wire")
    parameter = deepcopy(bundle)
    const = next(g for p in parameter["packets"] for g in p["gates"] if g["op"] == "const")
    const["parameter"] = str(F(const["parameter"]) + 1)
    reject(lambda: assemble(parameter), "assembly gate source/occurrence/parameter mismatch")
    return {"rejected": ["missing seam", "missing exposed frontier", "changed source",
                          "missing local gate", "changed gate parameter"]}


def negative_global_cycle():
    ws = {w: Wire(w, "Q", f"cycle/source/{w}", f"cycle/wire/{w}") for w in ("a", "b", "da", "db")}
    gs = {
        "copy-A": Gate("copy-A", "copy", ("b",), ("a", "da"), "source/A", "event/A"),
        "discard-A": Gate("discard-A", "discard", ("da",), (), "source/DA", "event/DA"),
        "copy-B": Gate("copy-B", "copy", ("a",), ("b", "db"), "source/B", "event/B"),
        "discard-B": Gate("discard-B", "discard", ("db",), (), "source/DB", "event/DB")}
    for region, inp, out, discard in (("A", "b", "a", "da"), ("B", "a", "b", "db")):
        local = Network({w: ws[w] for w in (inp, out, discard)},
                        {k: g for k, g in gs.items() if k.endswith(region)}, (inp,), (out,), ("piece", region))
        require(evaluate(local, (3,))[0] == (F(3),), "local piece must be acyclic/defined")
    global_n = Network(ws, gs, (), (), ("cyclic assembly",))
    regions = {gid: gid[-1] for gid in gs}
    bundle = package_regions(global_n, regions)
    reject(lambda: assemble(bundle), "global operation cycle")
    return {"locally_acyclic_pieces": 2, "global_cycle_rejected": True}


def positive_feature_observations_negative_update():
    states = (0, 1, 2)
    identity, f = (0, 1, 2), (0, 2, 2)
    monoid = (identity, f)
    chi, obs = (0, 0, 1), (0, 0, 0)
    require(tuple(f[f[x]] for x in states) == f, "continuation idempotence")
    for a, b in product(monoid, repeat=2):
        require(tuple(b[a[x]] for x in states) in monoid, "continuation monoid closure")
    factor = {}
    for k, continuation in enumerate(monoid):
        for x in states:
            feature = chi[x]
            observation = obs[continuation[x]]
            if (k, feature) in factor:
                require(factor[k, feature] == observation, "observation factorization")
            factor[k, feature] = observation
    require(chi[0] == chi[1] and chi[f[0]] != chi[f[1]], "missing online update obstruction")
    # A distinct absorbing illegal state prevents the legal/illegal distinction
    # from being silently lost under an over-coarse constant feature.
    total_action = (0, 2, 2)  # legal 0 stays legal; legal 1 becomes bottom=2.
    observation = ("ok", "ok", "invalid")
    require(total_action[2] == 2 and observation[total_action[0]] != observation[total_action[1]],
            "invalid outcome must distinguish futures")
    return {"finite_states": 3, "all_monoid_elements_checked": 2,
            "observation_descent": True, "online_update_exists": False,
            "obstruction": {"equal_feature_states": [0, 1], "updated_features": [0, 1]},
            "illegal_outcome_distinguished": True}


# Exact two-dimensional chart calculations. Matrices are row-major four-tuples.
def mm(a, b):
    return (a[0]*b[0]+a[1]*b[2], a[0]*b[1]+a[1]*b[3],
            a[2]*b[0]+a[3]*b[2], a[2]*b[1]+a[3]*b[3])


def mv(a, v):
    return (a[0]*v[0]+a[1]*v[1], a[2]*v[0]+a[3]*v[1])


def transpose(a):
    return (a[0], a[2], a[1], a[3])


def scale(c, v):
    return tuple(c*x for x in v)


def add(a, b):
    return tuple(x+y for x, y in zip(a, b))


def dot(a, b):
    return sum(x*y for x, y in zip(a, b))


def inverse_complex(z):
    d = dot(z, z)
    if d == 0:
        raise InvalidNetwork("reciprocal chart excludes zero")
    return (z[0]/d, -z[1]/d)


def reciprocal_jacobian(z):
    x, y = z
    d2 = (x*x+y*y)**2
    return ((y*y-x*x)/d2, -2*x*y/d2, 2*x*y/d2, (y*y-x*x)/d2)


def scalar_data(z):
    x, y = z
    a = x**4/F(4)-x*x/F(2)+y*y
    gradient = (x**3-x, 2*y)
    L, f = dot(gradient, gradient), 1+a*a
    if L == 0:
        raise InvalidNetwork("deleted critical point")
    return a, gradient, L/f, f


def chart_data(coordinate, center, radius, outer):
    base = inverse_complex(coordinate) if outer else coordinate
    z = (center + radius*base[0], radius*base[1])
    dz = scale(radius, reciprocal_jacobian(coordinate)) if outer else (radius, F(0), F(0), radius)
    a, gradient, conformal, f = scalar_data(z)
    metric = scale(conformal, mm(transpose(dz), dz))
    da = mv(transpose(dz), gradient)
    require(metric[1] == metric[2] == 0 and metric[0] == metric[3] > 0, "chart metric conformality")
    grad = scale(1/metric[0], da)
    rotate = (-grad[1], grad[0])
    xu = scale(1/f, add(grad, scale(-a, rotate)))
    xv = scale(1/f, add(scale(a, grad), rotate))
    require(dot(da, xu) == 1 and dot(da, xv) == a, "canonical frame signed derivatives")
    require(dot(xu, mv(metric, xu)) == dot(xv, mv(metric, xv)) == 1, "frame unit norm")
    require(dot(xu, mv(metric, xv)) == 0 and xu[0]*xv[1]-xu[1]*xv[0] > 0,
            "oriented orthonormal frame")
    require(dot(da, grad) == f, "AES identity at rational sample")
    return z, a, metric, da, xu, xv


def projective_point(v):
    first = next((x for x in v if x != 0), None)
    if first is None:
        raise InvalidNetwork("zero homogeneous point")
    return tuple(x/first for x in v)


def positive_reciprocal_collar_frame():
    samples = ((F(1), F(1,4)), (F(3,4), F(1,2)),
               (F(-1), F(1,3)), (F(4,5), F(-3,5)))
    centers, radius = (F(-1,2), F(1,2)), F(3,4)
    count = 0
    for center, xi in product(centers, samples):
        require(F(9,16) < dot(xi, xi) < F(25,16), "sample outside declared open collar")
        eta = inverse_complex(xi)
        require(inverse_complex(eta) == xi, "reciprocal inverse condition")
        inner = chart_data(xi, center, radius, False)
        outer = chart_data(eta, center, radius, True)
        jac = reciprocal_jacobian(xi)
        require(inner[:2] == outer[:2], "assignment overlap")
        require(mm(mm(transpose(jac), outer[2]), jac) == inner[2], "metric pullback")
        require(mv(transpose(jac), outer[3]) == inner[3], "assignment covector pullback")
        require(mv(jac, inner[4]) == outer[4] and mv(jac, inner[5]) == outer[5], "frame Jacobian transport")
        require(mm(reciprocal_jacobian(eta), jac) == (F(1), F(0), F(0), F(1)), "inverse Jacobians")
        # Sensitivity controls: metric mismatch and wrong tangent sign must fail.
        require(mm(mm(transpose(jac), scale(2, outer[2])), jac) != inner[2], "metric mutation unnoticed")
        require(mv(scale(-1, jac), inner[4]) != outer[4], "frame sign mutation unnoticed")
        count += 1
    for center in centers:
        xi_chart = (F(1), -center, F(0), radius)
        eta_chart = (F(0), radius, F(1), -center)
        xi_inverse = (radius, center, F(0), F(1))
        eta_inverse = (center, radius, F(1), F(0))
        for marked in ((F(-1), F(1)), (F(0), F(1)), (F(1), F(1)), (F(1), F(0))):
            xi = projective_point(mv(xi_chart, marked))
            eta = projective_point(mv(eta_chart, marked))
            require(projective_point((xi[1], xi[0])) == eta, "marked reciprocal chart transport")
            require(projective_point(mv(xi_inverse, xi)) == projective_point(marked), "inner marked inverse")
            require(projective_point(mv(eta_inverse, eta)) == projective_point(marked), "outer marked inverse")
        require(projective_point(mv(eta_chart, (F(1), F(0)))) == (F(0), F(1)),
                "infinite marked end must map to eta=0")
        # Coordinate transport only: no metric evaluation or regular extension
        # at a marked puncture is asserted.
    reject(lambda: inverse_complex((F(0), F(0))), "excludes zero")
    return {"cut_centers": ["-1/2", "1/2"], "cut_radius": "3/4",
            "xi_open_collar": "3/4 < |xi| < 5/4", "exact_rational_sample_points": count,
            "signed_parameters": {"mu": "1", "lambda": "1"},
            "metric_covector_frame_pullbacks": True,
            "marked_end_transports": 8, "infinite_end": "xi=infinity, eta=0 (exact homogeneous-coordinate check)",
            "negative_controls": ["doubled metric", "wrong Jacobian sign", "reciprocal at zero"]}


CHECKS = [
    ("positive_four_producer_rational_execution", positive_arithmetic),
    ("positive_substitution_source_occurrence_transport", positive_identity_transport),
    ("negative_implicit_sharing_binding_type_and_instance_controls", negative_resource_binding),
    ("positive_partial_substitution_frontier_order", positive_partial_frontier),
    ("positive_substitution_strict_partial_domain_grid", positive_exact_domain),
    ("negative_discard_does_not_erase_undefined_producer", negative_strict_discard),
    ("positive_topological_numerics_distinct_traces", positive_schedule_independence),
    ("positive_association_isomorphism_distinct_receipts", positive_association_receipts),
    ("negative_equal_scalar_does_not_identify_process", negative_endpoint_history_collapse),
    ("positive_two_independent_seam_packet_reassemblies", positive_seam_reassembly),
    ("negative_seam_frontier_inventory_and_source_controls", negative_seam_inventory),
    ("negative_locally_acyclic_pieces_form_global_cycle", negative_global_cycle),
    ("positive_observation_descent_negative_online_feature_update", positive_feature_observations_negative_update),
    ("positive_exact_reciprocal_collar_frame_samples_with_negative_controls", positive_reciprocal_collar_frame),
]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--evidence", type=Path, help="also write deterministic JSON evidence to this path")
    args = parser.parse_args()
    checks = []
    for name, check in CHECKS:
        try:
            checks.append({"name": name, "status": "pass", "evidence": check()})
        except Exception as exc:
            checks.append({"name": name, "status": "fail", "error": f"{type(exc).__name__}: {exc}"})
    summary = {
        "checker": "independently-authored-ported-aes-finite-checker-v1",
        "provenance": "New implementation from the recovered 2026-10-09 Version 0.1 PDF; original ZIP unavailable. Not the original reported 55 checks.",
        "arithmetic": "exact rational fractions; Python standard library only",
        "status": "pass" if all(c["status"] == "pass" for c in checks) else "fail",
        "groups_passed": sum(c["status"] == "pass" for c in checks),
        "groups_total": len(checks),
        "checks": checks,
        "limitations": [
            "Finite fixtures and declared sample domains are not proofs of the general theorems.",
            "The two event partitions and seam packets are independently authored, not recovered original packets or gate placements on a surface.",
            "Collar calculations are exact at eight declared rational sample points; no global smooth-gluing or essential-end theorem is claimed.",
            "No faithful AES realization of arithmetic/copy/discard gates or actual opposite-edge feature witness is implemented."
        ]
    }
    rendered = json.dumps(summary, indent=2, sort_keys=True) + "\n"
    if args.evidence:
        args.evidence.write_text(rendered, encoding="utf-8")
    sys.stdout.write(rendered)
    return 0 if summary["status"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
