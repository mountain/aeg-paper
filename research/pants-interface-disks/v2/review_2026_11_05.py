#!/usr/bin/env python3
"""Fresh-session model audit, not independent human review or a general proof.

Codex (OpenAI), requested by Mingli Yuan, 2026-11-05.
No producer, original mutation generator or partition helper is imported.
receive.py and the evidence CLI are the systems under test.
"""
from copy import deepcopy
from fractions import Fraction
from itertools import product
from pathlib import Path
import hashlib
import json
import subprocess
import sys
import tempfile

import receive as target

HERE = Path(__file__).resolve().parent
KEYS = ('A', 'B', 'C', 'A-copy', 'different-value')
EXPECTED_PAIRS = (('A:x', 'A:y'), ('B:x', 'B:y'), ('C:x', 'C:y'),
                  ('A:x', 'A:y'), ('A:x', 'B:y'))
EXPECTED_NUMERIC = ((5, 20), (5, 20), (5, 20), (5, 20), (6, 24))
V1_BLOBS = {
    'README.md': '880f34f3a074ebd7709b8266ebdd87f68086a4cb',
    'evidence-handles.json': '44f53051e5b01838b68ea3430226b94941afe109',
    'evidence-v1.json': 'c6eda244916e801ea880bf55a469ed8c2de54f66',
    'verify_handles.py': 'd8924c7a9a59963c24edbe02c08c4e8c86e7e260',
    'verify_v1.py': '10e455e60d4857d4ce84411390f8a0650c6c971a',
}


def check(condition, message):
    if not condition:
        raise RuntimeError(message)


def sha(value):
    raw = json.dumps(value, sort_keys=True, separators=(',', ':')).encode()
    return hashlib.sha256(raw).hexdigest()


def accept_or_reject(packet, key, contract, reason=None):
    try:
        result = target.receive(packet, key, contract)
    except target.Rejected as exc:
        check(reason is not None and str(exc) == reason, 'unexpected rejection: ' + str(exc))
        return None
    check(reason is None, 'unauthorized packet accepted: ' + key)
    return result


def retarget(packet, destination):
    """Rewrite ALL request/occurrence/event spellings; preserve source history."""
    result = deepcopy(packet)
    old, new = packet['scope'], destination['scope']

    def rename(value):
        if isinstance(value, dict):
            return {k: rename(v) for k, v in value.items()}
        if isinstance(value, list):
            return [rename(v) for v in value]
        if isinstance(value, str) and value.startswith(old + '/'):
            return new + value[len(old):]
        return value

    result = rename(result)
    result.update(instance=destination['instance'], scope=new)
    result['residual_sha256'] = sha(result['residual'])
    return result


def main():
    contract = target.load_contract()
    saved = json.loads((HERE / 'evidence-v2.json').read_text())
    packets = saved['candidates']
    check(tuple(p['instance'] for p in packets) == KEYS, 'fixture order')
    # Independent remote Git blob inventory, not merely the contract's pin check.
    direct_files = {p.name for p in HERE.parent.iterdir() if p.is_file()}
    check(direct_files == set(V1_BLOBS), 'V1 direct-file inventory')
    for name, expected in V1_BLOBS.items():
        raw = (HERE.parent / name).read_bytes()
        blob = b'blob ' + str(len(raw)).encode() + b'\0' + raw
        check(hashlib.sha1(blob).hexdigest() == expected, 'V1 blob: ' + name)

    observations = []
    for i, (key, packet) in enumerate(zip(KEYS, packets)):
        result = accept_or_reject(packet, key, contract)
        values = [Fraction(leaf['record']['value']) for leaf in packet['residual']['inputs']]
        z = values[0] + values[1]
        numeric = (z, 4 * z)
        check(numeric == EXPECTED_NUMERIC[i], 'independent rational evaluation')
        check(tuple(leaf['source'] for leaf in packet['residual']['inputs']) == EXPECTED_PAIRS[i],
              'independent source pair')
        check(result['numeric_observation'] == {'interface': str(z), 'output': str(4 * z)},
              'receiver numeric observation')
        observations.append(result)
    for i, j in product(range(5), repeat=2):
        check((observations[i]['numeric_observation'] == observations[j]['numeric_observation'])
              == (EXPECTED_NUMERIC[i] == EXPECTED_NUMERIC[j]), 'numeric equivalence matrix')
        check((observations[i]['source_observation'] == observations[j]['source_observation'])
              == (EXPECTED_PAIRS[i] == EXPECTED_PAIRS[j]), 'source equivalence matrix')
    all_ids = [v for p in packets for v in p['residual']['occurrences'].values()]
    all_ids += [e['id'] for p in packets for e in p['residual']['events']]
    check(len(all_ids) == len(set(all_ids)) == 40, 'fresh port and event inventory')
    check(set(packets[0]['residual']['occurrences'].values()).isdisjoint(
          packets[3]['residual']['occurrences'].values()), 'A-copy occurrence collision')
    # A/B differ even if source names, origin labels and execution IDs are erased.
    for field in ('inputs', 'events'):
        left, right = deepcopy(packets[0]['residual'][field]), deepcopy(packets[1]['residual'][field])
        def erase_labels(rows):
            for row in rows:
                for name in ('source', 'occurrence', 'id'):
                    row.pop(name, None)
                if 'record' in row:
                    row['record'].pop('origin', None)
            return rows
        check(erase_labels(left) != erase_labels(right), 'A/B distinction depends on labels')

    cross_rejected = relabeled_rejected = 0
    for i, j in product(range(5), repeat=2):
        accept_or_reject(packets[j], KEYS[i], contract, None if i == j else 'instance:binding')
        cross_rejected += i != j
        if i == j:
            continue
        rebound = retarget(packets[j], packets[i])
        same_sources = EXPECTED_PAIRS[i] == EXPECTED_PAIRS[j]
        accept_or_reject(rebound, KEYS[i], contract, None if same_sources else 'source:binding')
        if same_sources:
            check(rebound == packets[i], 'authorized alpha-renaming changes content')
        relabeled_rejected += not same_sources

    # Every registered ordered source pair in every expected context. Make the
    # arithmetic trace and both digest layers internally consistent before testing.
    rejected = equal_numeric_rejected = 0
    with tempfile.TemporaryDirectory(prefix='oq096-review-') as directory:
        path = Path(directory) / 'evidence.json'
        command = [sys.executable, *(['-O'] if sys.flags.optimize else []),
                   str(HERE / 'verify_v2.py'), '--receive', str(path)]
        for i, key in enumerate(KEYS):
            for sources in product(contract['source_registry'], repeat=2):
                packet = deepcopy(packets[i])
                for leaf, source in zip(packet['residual']['inputs'], sources):
                    leaf['source'] = source
                    leaf['record'] = deepcopy(contract['source_registry'][source])
                x, y = (Fraction(leaf['record']['value']) for leaf in packet['residual']['inputs'])
                z, w = x + y, (x + y) * 4
                packet['residual']['events'][0].update(input_values=[str(x), str(y)], output_value=str(z))
                packet['residual']['events'][1].update(input_values=[str(z), '4'], output_value=str(w))
                packet['numeric'] = {'interface': str(z), 'output': str(w)}
                packet['residual_sha256'] = sha(packet['residual'])
                legal = sources == EXPECTED_PAIRS[i]
                accept_or_reject(packet, key, contract, None if legal else 'source:binding')
                altered = deepcopy(saved)
                altered['candidates'][i] = packet
                altered['candidates_sha256'] = sha(altered['candidates'])
                path.write_text(json.dumps(altered))
                outcome = subprocess.run(command, capture_output=True, text=True, timeout=30)
                check(outcome.returncode == (0 if legal else 1), 'evidence CLI status')
                check(outcome.stderr == ('' if legal else 'REJECTED: source:binding\n'),
                      'evidence rejected for a reason other than source binding: ' + outcome.stderr)
                if not legal:
                    rejected += 1
                    equal_numeric_rejected += packet['numeric'] == packets[i]['numeric']
    check(rejected == 240, 'source-grid rejection count')
    print(json.dumps({
        'status': 'fresh-session-model-review-passed',
        'v1_direct_files_unchanged': 5,
        'independent_numeric_classes': [['A', 'B', 'C', 'A-copy'], ['different-value']],
        'independent_source_classes': [['A', 'A-copy'], ['B'], ['C'], ['different-value']],
        'original_cross_identity_rejections': cross_rejected,
        'fully_relabeled_source_rejections': relabeled_rejected,
        'authorized_exact_alpha_renamings': 2,
        'source_pair_cases': 245,
        'rehash_rejections_packet_and_fresh_evidence': rejected,
        'same_numeric_rehash_rejections': equal_numeric_rejected,
        'limit': 'fixed local registry; no external-origin authentication, general DAG proof, AES or native Seal',
    }, sort_keys=True, indent=2))


if __name__ == '__main__':
    main()
