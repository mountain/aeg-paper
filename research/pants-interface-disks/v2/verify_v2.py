#!/usr/bin/env python3
"""Deterministic replay, quotients and rejection controls for the frozen V2 contract."""
from copy import deepcopy
from pathlib import Path
import argparse
import hashlib
import json

from produce import build
from receive import (Rejected, canonical, demand, digest, fields, load_contract,
                     load_json, numeric_observation, receive)

HERE = Path(__file__).resolve().parent
FILES = ('contract.json', 'produce.py', 'receive.py', 'verify_v2.py', 'test_reception.py')


def mutations(candidates):
    """Adversarial edits; recompute residual hashes to test semantic guards."""
    by_key = {p['instance']: p for p in candidates}
    a = by_key['A']
    cases = []

    def add(name, reason, edit, rehash=True):
        packet = deepcopy(a)
        edit(packet)
        if rehash:
            packet['residual_sha256'] = digest(packet['residual'])
        cases.append((name, reason, packet))

    add('same-value-source-substitution', 'source:binding',
        lambda p: p['residual']['inputs'][0].update(source='C:x', record=deepcopy(by_key['C']['residual']['inputs'][0]['record'])))
    add('source-record-rewrite', 'source:record',
        lambda p: p['residual']['inputs'][0]['record'].update(origin='forged-origin'))
    add('unknown-source', 'source:unknown', lambda p: p['residual']['inputs'][0].update(source='foreign:x'))
    add('gate-source-substitution', 'event:source', lambda p: p['residual']['events'][0].update(source='foreign:add'))
    add('collapse-interface-identities', 'identity:collapsed',
        lambda p: p['residual']['occurrences'].update({'P:z:in': p['residual']['occurrences']['Q:z:out']}))
    add('alias-interface-binding', 'binding:incidence', lambda p: p['binding'].update(input_occurrence=p['binding']['output_occurrence']))
    add('wrong-consumer-slot', 'binding:slot', lambda p: p['binding'].update(input_slot=1))
    add('wrong-producer-slot', 'binding:slot', lambda p: p['binding'].update(output_slot=1))
    add('boolean-slot', 'binding:slot-type', lambda p: p['binding'].update(input_slot=False))
    add('commutative-producer-slot-swap', 'event:shape-or-slot', lambda p: p['residual']['events'][0].update(inputs=['y', 'x']))
    add('missing-residual', 'residual:missing-or-fields', lambda p: p.update(residual=None))
    add('erase-producer-event', 'history:inventory', lambda p: p['residual']['events'].pop(0))
    add('unrecorded-constant-replacement', 'event:shape-or-slot', lambda p: p['residual']['events'][0].update(op='constant', inputs=[]))
    add('forged-history-value', 'history:output-value', lambda p: p['residual']['events'][0].update(output_value='6'))
    add('missing-input-source', 'input:fields', lambda p: p['residual']['inputs'][0].pop('source'))
    add('input-slot-swap', 'input:slot', lambda p: p['residual']['inputs'].reverse())
    add('stale-residual-digest', 'residual:digest', lambda p: p['residual'].update(events=[]), rehash=False)
    add('changed-consumer-parameter', 'consumer:context', lambda p: p['consumer'].update(parameter_value='5'))
    add('forged-numeric-output', 'numeric:replay', lambda p: p['numeric'].update(output='21'))
    cases.append(('whole-valid-foreign-receipt', 'instance:binding', deepcopy(by_key['B'])))
    return cases


def partition(keys, observations):
    groups = {}
    for key, observation in zip(keys, observations):
        groups.setdefault(canonical(observation), []).append(key)
    return list(groups.values())


def analyze(candidates, contract):
    keys = [i['key'] for i in contract['instances']]
    demand(type(candidates) is list and len(candidates) == len(keys), 'candidates:inventory')
    # Do not take expected identity from the untrusted candidates.
    accepted = [receive(packet, key, contract) for key, packet in zip(keys, candidates)]
    all_ids = [v for p in candidates for v in p['residual']['occurrences'].values()]
    event_ids = [e['id'] for p in candidates for e in p['residual']['events']]
    demand(len(set(all_ids)) == len(all_ids), 'identity:cross-instance-port-reuse')
    demand(len(set(event_ids)) == len(event_ids), 'identity:cross-instance-event-reuse')
    numeric = [r['numeric_observation'] for r in accepted]
    source = [r['source_observation'] for r in accepted]
    nclasses, sclasses = partition(keys, numeric), partition(keys, source)
    # Acceptance targets are frozen before execution, not inferred from report labels.
    demand(numeric[0] == numeric[1] == numeric[2] == numeric[3], 'target:numeric-equality')
    demand(source[0] != source[1] and source[0] != source[2], 'target:source-separation')
    demand(source[0] == source[3], 'target:alpha-invariant-reuse')
    demand(numeric[0] != numeric[4], 'target:numeric-nonconstant')
    demand([v['record']['value'] for v in source[0]['inputs']] ==
           [v['record']['value'] for v in source[2]['inputs']], 'target:equal-operand-control')
    for i in range(len(keys)):
        demand(source[i]['numeric'] == numeric[i], 'target:projection')
        for j in range(len(keys)):
            demand(source[i] != source[j] or numeric[i] == numeric[j], 'target:partition-refinement')
    negatives = []
    for name, expected_reason, altered in mutations(candidates):
        # Most malformed receipts keep exactly the same claimed numeric packet.
        try:
            receive(altered, 'A', contract)
        except Rejected as exc:
            demand(str(exc) == expected_reason, 'negative:wrong-reason:' + name + ':' + str(exc))
            negatives.append({'name': name, 'status': 'rejected', 'reason': str(exc),
                              'numeric_claim_unchanged': altered['numeric'] == candidates[0]['numeric']})
        else:
            raise Rejected('negative:accepted:' + name)
    erased = deepcopy(candidates[0]['numeric'])
    demand(numeric_observation(erased['interface'], contract) == erased, 'erasure:numeric')
    try:
        receive(erased, 'A', contract)
    except Rejected as exc:
        demand(str(exc) == 'packet:fields', 'erasure:wrong-reason')
    else:
        raise Rejected('erasure:source-recovered-without-residual')
    return {'accepted': dict(zip(keys, accepted)),
            'numeric_equivalence_classes': nclasses, 'source_equivalence_classes': sclasses,
            'source_partition_refines_numeric': True,
            'occurrence_inventory': {'port_occurrences': len(all_ids), 'event_occurrences': len(event_ids), 'all_fresh': True},
            'erasure_control': {'numeric_only_succeeds': True, 'source_reopening': 'rejected:packet:fields',
                                'interpretation': 'retained residuals are additional data, not recovered from the numeric quotient'},
            'negative_controls': negatives}


def file_pins():
    return {name: hashlib.sha256((HERE / name).read_bytes()).hexdigest() for name in FILES}


def run():
    contract = load_contract()
    candidates = [build(contract, i) for i in contract['instances']]
    return {'schema': 'oq096-equal-value-evidence-v2',
            'status': 'computationally-verified-example',
            'baseline_aeg': contract['baseline_aeg'], 'files_sha256': file_pins(),
            'candidates_sha256': digest(candidates), 'candidates': candidates,
            'results': analyze(candidates, contract), 'limits': contract['limits']}


def receive_evidence(saved):
    fields(saved, 'schema status baseline_aeg files_sha256 candidates_sha256 candidates results limits', 'evidence:fields')
    contract = load_contract()
    demand(saved['schema'] == 'oq096-equal-value-evidence-v2', 'evidence:schema')
    demand(saved['status'] == 'computationally-verified-example', 'evidence:status')
    demand(saved['baseline_aeg'] == contract['baseline_aeg'] and saved['limits'] == contract['limits'], 'evidence:scope')
    demand(saved['files_sha256'] == file_pins(), 'evidence:source-files')
    demand(saved['candidates_sha256'] == digest(saved['candidates']), 'evidence:candidate-digest')
    results = analyze(saved['candidates'], contract)
    demand(canonical(results) == canonical(saved['results']), 'evidence:results')
    return {'status': 'saved-v2-evidence-received', 'candidates_sha256': saved['candidates_sha256'],
            'receipts': len(saved['candidates']), 'negative_controls': len(results['negative_controls'])}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--receive', type=Path)
    args = parser.parse_args()
    try:
        output = receive_evidence(load_json(args.receive)) if args.receive else run()
        print(json.dumps(output, sort_keys=True, indent=2))
    except Rejected as exc:
        parser.exit(1, 'REJECTED: ' + str(exc) + '\n')
