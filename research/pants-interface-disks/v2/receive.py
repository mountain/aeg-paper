#!/usr/bin/env python3
"""Source-bound reception and two explicitly scoped observers for OQ-096 V2.
Does not import or invoke produce.py. Same model author, not independent review.
"""
from fractions import Fraction
from pathlib import Path
import argparse
import hashlib
import json

CONTRACT_SHA256 = '4eff959a029b79bd5b9ca2f62ceddb6faf9b708c2955db5bb0700333b3fa0e2c'
PORTS = ('Q:x:in', 'Q:y:in', 'Q:z:out', 'P:z:in', 'P:t:in', 'P:w:out')


class Rejected(ValueError):
    pass


def demand(ok, reason):
    if not ok:
        raise Rejected(reason)


def canonical(obj):
    return json.dumps(obj, sort_keys=True, separators=(',', ':')).encode()


def digest(obj):
    return hashlib.sha256(canonical(obj)).hexdigest()


def fields(obj, names, reason):
    demand(type(obj) is dict and set(obj) == set(names.split()), reason)


def strict_pairs(pairs):
    result = {}
    for key, value in pairs:
        demand(key not in result, 'json:duplicate-key')
        result[key] = value
    return result


def load_json(path):
    data = Path(path).read_bytes()
    demand(len(data) <= 1_000_000, 'json:byte-limit')
    try:
        return json.loads(data, object_pairs_hook=strict_pairs)
    except (json.JSONDecodeError, UnicodeDecodeError) as exc:
        raise Rejected('json:syntax') from exc


def load_contract():
    path = Path(__file__).with_name('contract.json')
    demand(hashlib.sha256(path.read_bytes()).hexdigest() == CONTRACT_SHA256, 'contract:pin')
    c = load_json(path)
    for name, expected in c['v1_files'].items():
        demand(hashlib.sha256((path.parent.parent / name).read_bytes()).hexdigest() == expected,
               'v1:changed:' + name)
    return c


def rational(value):
    demand(type(value) is str and 0 < len(value) <= 80, 'number:type-or-size')
    try:
        result = Fraction(value)
    except (ValueError, ZeroDivisionError) as exc:
        raise Rejected('number:invalid') from exc
    demand(str(result) == value, 'number:not-canonical')
    return result


def numeric_observation(z, contract):
    """Only the scalar interface and fixed consumer; no access to residuals."""
    value = rational(z)
    return {'interface': str(value),
            'output': str(value * rational(contract['consumer']['parameter_value']))}


def receive(packet, expected_key, contract):
    """expected_key comes from the caller's frozen manifest, never the packet."""
    instances = {i['key']: i for i in contract['instances']}
    demand(expected_key in instances, 'instance:unknown-expected')
    expected = instances[expected_key]
    fields(packet, 'schema instance scope consumer binding numeric residual residual_sha256', 'packet:fields')
    demand(packet['schema'] == 'oq096-receipt-v2', 'packet:schema')
    demand(packet['instance'] == expected_key and packet['scope'] == expected['scope'], 'instance:binding')
    demand(packet['consumer'] == contract['consumer'], 'consumer:context')
    residual = packet['residual']
    fields(residual, 'inputs occurrences events', 'residual:missing-or-fields')
    demand(packet['residual_sha256'] == digest(residual), 'residual:digest')
    ids = residual['occurrences']
    fields(ids, ' '.join(PORTS), 'identity:inventory')
    demand(all(type(v) is str for v in ids.values()), 'identity:type')
    demand(len(set(ids.values())) == len(PORTS), 'identity:collapsed')
    demand(all(ids[p] == expected['scope'] + '/' + p for p in PORTS), 'identity:scope-or-role')
    binding = packet['binding']
    fields(binding, 'producer output_slot wire consumer input_slot type output_occurrence input_occurrence', 'binding:fields')
    demand(type(binding['input_slot']) is int and type(binding['output_slot']) is int, 'binding:slot-type')
    demand(binding['input_slot'] == 0 and binding['output_slot'] == 0, 'binding:slot')
    wanted = dict(contract['binding'])
    wanted.update(producer=expected['scope'] + '/plus#1', consumer=expected['scope'] + '/times#1',
                  output_occurrence=ids['Q:z:out'], input_occurrence=ids['P:z:in'])
    demand(binding == wanted, 'binding:incidence')
    leaves = residual['inputs']
    demand(type(leaves) is list and len(leaves) == 2, 'inputs:inventory')
    environment = {'t': rational(contract['consumer']['parameter_value'])}
    normalized_inputs = []
    for index, wire in enumerate(('x', 'y')):
        leaf = leaves[index]
        fields(leaf, 'wire source record occurrence', 'input:fields')
        demand(leaf['wire'] == wire and leaf['occurrence'] == ids['Q:' + wire + ':in'], 'input:slot')
        source = leaf['source']
        demand(type(source) is str and source in contract['source_registry'], 'source:unknown')
        # First check immutable content, then which known source this request permits.
        demand(leaf['record'] == contract['source_registry'][source], 'source:record')
        demand(source == expected['inputs'][wire], 'source:binding')
        environment[wire] = rational(leaf['record']['value'])
        normalized_inputs.append({'wire': wire, 'source': source, 'record': leaf['record']})
    events = residual['events']
    demand(type(events) is list and len(events) == 2, 'history:inventory')
    normalized_events = []
    for index, (local, spec) in enumerate((('plus#1', contract['producer']), ('times#1', contract['consumer']))):
        event = events[index]
        fields(event, 'id source op inputs output input_values output_value', 'event:fields')
        demand(event['id'] == expected['scope'] + '/' + local, 'event:identity')
        demand(event['source'] == spec['source'], 'event:source')
        demand(event['op'] == spec['op'] and event['inputs'] == spec['input_wires']
               and event['output'] == spec['output_wire'], 'event:shape-or-slot')
        demand(all(w in environment for w in event['inputs']), 'event:dependency')
        demand(event['output'] not in environment, 'event:multiple-producers')
        operands = [environment[w] for w in event['inputs']]
        demand(event['input_values'] == list(map(str, operands)), 'history:input-values')
        if event['op'] == 'add':
            computed = sum(operands, Fraction(0))
        elif event['op'] == 'mul':
            computed = Fraction(1)
            for operand in operands:
                computed *= operand
        else:
            raise Rejected('event:unsupported')
        demand(rational(event['output_value']) == computed, 'history:output-value')
        environment[event['output']] = computed
        normalized_events.append({k: v for k, v in event.items() if k != 'id'})
    numeric = numeric_observation(str(environment['z']), contract)
    fields(packet['numeric'], 'interface output', 'numeric:fields')
    demand(packet['numeric'] == numeric and str(environment['w']) == numeric['output'], 'numeric:replay')
    # Fresh occurrence spellings are diagnostic, not discriminating observations.
    source = {'numeric': numeric, 'inputs': normalized_inputs,
              'events': normalized_events, 'consumer': contract['consumer'],
              'parameter_record': contract['source_registry'][contract['consumer']['parameter_source']]}
    return {'numeric_observation': numeric, 'source_observation': source,
            'recovered_producer': {'op': 'add', 'ordered_inputs': normalized_inputs, 'value': str(environment['z'])},
            'distinct_interface_occurrences': [binding['output_occurrence'], binding['input_occurrence']],
            'replayed_events': len(events)}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--receive', type=Path, required=True)
    parser.add_argument('--expected', required=True)
    args = parser.parse_args()
    try:
        result = receive(load_json(args.receive), args.expected, load_contract())
        print(json.dumps(result, sort_keys=True, indent=2))
    except Rejected as exc:
        parser.exit(1, 'REJECTED: ' + str(exc) + '\n')
