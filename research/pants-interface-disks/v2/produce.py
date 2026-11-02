#!/usr/bin/env python3
"""Construct the declared five finite V2 receipts; not used by the receiver.
Codex (OpenAI), under Mingli Yuan's research direction, 2026-11-02.
"""
from fractions import Fraction
from pathlib import Path
import hashlib
import json
import sys


def digest(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def build(contract, instance):
    scope = instance['scope']
    ids = {p: scope + '/' + p for p in
           ['Q:x:in', 'Q:y:in', 'Q:z:out', 'P:z:in', 'P:t:in', 'P:w:out']}
    inputs = []
    for wire in ['x', 'y']:
        source = instance['inputs'][wire]
        inputs.append({'wire': wire, 'source': source,
                       'record': contract['source_registry'][source],
                       'occurrence': ids['Q:' + wire + ':in']})
    x, y = [Fraction(item['record']['value']) for item in inputs]
    z = x + y
    t = Fraction(contract['consumer']['parameter_value'])
    w = z * t
    residual = {'inputs': inputs, 'occurrences': ids, 'events': [
        {'id': scope + '/plus#1', 'source': 'Q:add', 'op': 'add',
         'inputs': ['x', 'y'], 'output': 'z',
         'input_values': [str(x), str(y)], 'output_value': str(z)},
        {'id': scope + '/times#1', 'source': 'P:mul', 'op': 'mul',
         'inputs': ['z', 't'], 'output': 'w',
         'input_values': [str(z), str(t)], 'output_value': str(w)}]}
    binding = dict(contract['binding'])
    binding['producer'] = scope + '/plus#1'
    binding['consumer'] = scope + '/times#1'
    binding['output_occurrence'] = ids['Q:z:out']
    binding['input_occurrence'] = ids['P:z:in']
    return {'schema': 'oq096-receipt-v2', 'instance': instance['key'],
            'scope': scope, 'consumer': contract['consumer'], 'binding': binding,
            'numeric': {'interface': str(z), 'output': str(w)},
            'residual': residual, 'residual_sha256': digest(residual)}


if __name__ == '__main__':
    if len(sys.argv) != 1:
        raise SystemExit('usage: produce.py')
    contract = json.loads(Path(__file__).with_name('contract.json').read_text())
    print(json.dumps([build(contract, i) for i in contract['instances']], sort_keys=True, indent=2))
