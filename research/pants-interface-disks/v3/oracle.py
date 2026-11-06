#!/usr/bin/env python3
"""Direct finite certificate oracle. Imports no JavaScript producer/receiver.
Same model author, not independent human review or independently commissioned code.
"""
from fractions import Fraction
from pathlib import Path
from copy import deepcopy
import hashlib
import json
import sys

ROOT = Path(__file__).resolve().parent
CONTRACT_BLOB = '704655355b4ae69f9b11bd7dc7b7451e696de460'
PIN_FILES = ["SPEC.md","common.mjs","produce.mjs","receive.mjs","verify.mjs","io.mjs","cli.mjs","receive-cli.mjs","oracle.py"]

def require(ok, reason):
    if not ok:
        raise ValueError(reason)

def canonical(x):
    return json.dumps(x, sort_keys=True, separators=(',', ':'), ensure_ascii=False)

def same(a, b):
    return canonical(a) == canonical(b)

def pairs(items):
    out = {}
    for key, value in items:
        require(key not in out, 'json:duplicate-key')
        out[key] = value
    return out

def load(path):
    return json.loads(Path(path).read_text(), object_pairs_hook=pairs)

def blob(path):
    data = Path(path).read_bytes()
    return hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()

def context(key, c):
    for row in c['instances']:
        if row['key'] == key:
            return row
    parts = key.split(':')
    require(len(parts) == 3 and parts[0] == 'grid'
            and parts[1] in list('012345') and parts[2] in list('012345'), 'request:unknown')
    i, j = map(int, parts[1:])
    return {'key': key, 'scope': 'run-' + key.replace(':', '-'),
            'inputs': {'x': 'grid:' + c['grid'][i], 'y': 'grid:' + c['grid'][j]}}

def graph(key, c):
    r = context(key, c)
    def oid(local):
        return r['scope'] + '/' + local
    events, ports = [], []
    for b in c['blocks']:
        ins = [b['key'] + ':' + w + ':in' for w in b['inputs']]
        out = b['key'] + ':' + b['output'] + ':out'
        events.append(dict(key=b['key'], id=oid(b['event']), source=b['source'],
                           op=b['op'], inputs=ins, output=out, type='rational'))
        for i, p in enumerate(ins):
            ports.append(dict(role=p, id=oid(p), event=b['key'], direction='in', slot=i, type='rational'))
        ports.append(dict(role=out, id=oid(out), event=b['key'], direction='out', slot=0, type='rational'))
    assignments = dict(c['fixed_sources'], **{'Q:x:in': r['inputs']['x'], 'Q:y:in': r['inputs']['y']})
    leaves = [dict(port=p, source=s, record=c['source_registry'][s], occurrence=oid(p))
              for p, s in sorted(assignments.items())]
    bindings = [dict(e, from_id=oid(e['from']), to_id=oid(e['to']))
                for e in sorted(c['bindings'], key=lambda x: x['from'])]
    return dict(events=sorted(events, key=lambda e: e['key']),
                ports=sorted(ports, key=lambda p: p['role']), bindings=bindings, leaves=leaves,
                guards=[dict(event='R', denominator='R:w:in', nonzero=True)],
                boundary=dict(inputs=c['external_order'], outputs=c['output_order']))

def arithmetic_claims(g):
    values = {l['port']: Fraction(l['record']['value']) for l in g['leaves']}
    x, y, t, u = [values[p] for p in ['Q:x:in', 'Q:y:in', 'P:t:in', 'R:u:in']]
    z, w = x + y, (x + y) * t
    require(w != 0, 'domain:zero')
    v = u / w
    by_key = {e['key']: e for e in g['events']}
    trace = []
    for k, args, result in [('Q', [x, y], z), ('P', [z, t], w), ('R', [u, w], v)]:
        e = by_key[k]
        trace.append(dict(event=k, id=e['id'], source=e['source'], op=e['op'],
                          inputs=list(map(str, args)), output=str(result)))
    return dict(trace=trace, numeric=dict(z=str(z), w=str(w), v=str(v)))

def receive(p, key, c):
    r = context(key, c)
    require(set(p) == set('schema request scope graph trace numeric'.split()), 'oracle:packet-fields')
    require(p['schema'] == 'oq096-receipt-v3' and p['request'] == key
            and p['scope'] == r['scope'], 'oracle:request')
    # A direct reference normal form; no staged-composition implementation is reused.
    expected_graph = graph(key, c)
    require(same(p['graph'], expected_graph), 'oracle:graph')
    claims = arithmetic_claims(expected_graph)
    require(same(p['trace'], claims['trace']) and same(p['numeric'], claims['numeric']), 'oracle:arithmetic')
    return claims

def verdict(fn):
    try:
        fn()
    except ValueError as exc:
        return str(exc)
    return 'accepted'

def cyclic(g):
    owner = {p['role']: p['event'] for p in g['ports']}
    adjacency = {e['key']: [] for e in g['events']}
    for e in g['bindings']:
        adjacency[owner[e['from']]].append(owner[e['to']])
    visiting, visited = set(), set()
    def visit(k):
        if k in visiting:
            return True
        if k in visited:
            return False
        visiting.add(k)
        if any(visit(v) for v in adjacency[k]):
            return True
        visiting.remove(k)
        visited.add(k)
        return False
    return any(visit(k) for k in adjacency)

def check(e, c):
    keys = [r['key'] for r in c['instances']] + [f'grid:{i}:{j}' for i in range(6) for j in range(6)]
    require([r['request'] for r in e['cases']] == keys, 'oracle:case-order')
    good = zero = 0
    identities = set()
    for row, key in zip(e['cases'], keys):
        g = graph(key, c)
        for o in g['ports'] + g['events']:
            require(o['id'] not in identities, 'oracle:freshness')
            identities.add(o['id'])
        if verdict(lambda: arithmetic_claims(g)) == 'domain:zero':
            require(row['verdict'] == 'domain:zero' and same(row['left_graph'], g)
                    and same(row['right_graph'], g), 'oracle:domain')
            zero += 1
        else:
            require(row['verdict'] == 'accepted', 'oracle:verdict')
            receive(row['left'], key, c)
            receive(row['right'], key, c)
            require(same(row['left'], row['right']), 'oracle:bracket')
            good += 1
    require(good == 36 and zero == 5 and len(identities) == 492, 'oracle:counts')
    for n in e['negatives']:
        require(verdict(lambda: receive(n['packet'], n['expected'], c)) != 'accepted',
                'oracle:accepted-negative:' + n['name'])
    require(len(e['negatives']) == 32, 'oracle:negative-count')
    accepted = rejected = unchanged = 0
    for row in e['cases'][:5]:
        base = row['left']
        for sx in sorted(c['source_registry']):
            for sy in sorted(c['source_registry']):
                p = deepcopy(base)
                for port, source in [('Q:x:in', sx), ('Q:y:in', sy)]:
                    leaf = next(l for l in p['graph']['leaves'] if l['port'] == port)
                    leaf.update(source=source, record=c['source_registry'][source])
                numeric_ok = verdict(lambda: p.update(arithmetic_claims(p['graph']))) == 'accepted'
                if verdict(lambda: receive(p, row['request'], c)) == 'accepted':
                    accepted += 1
                else:
                    rejected += 1
                    if numeric_ok and same(p['numeric'], base['numeric']):
                        unchanged += 1
    audit = dict(attempted=accepted+rejected, accepted=accepted, rejected=rejected,
                 numeric_unchanged_rejected=unchanged)
    require(same(audit, e['summary']['source_audit']) and (accepted, rejected, unchanged) == (5,975,107),
            'oracle:source-audit')
    base = e['cases'][0]['left']
    edges = []
    for a in [p for p in base['graph']['ports'] if p['direction'] == 'out']:
        for b in [p for p in base['graph']['ports'] if p['direction'] == 'in']:
            p = deepcopy(base)
            p['graph']['bindings'].append(dict(
                **{'from': a['role'], 'to': b['role']}, output_slot=a['slot'], input_slot=b['slot'],
                type=a['type'], from_id=a['id'], to_id=b['id']))
            require(verdict(lambda: receive(p, 'A', c)) != 'accepted', 'oracle:extra-edge')
            edges.append((a['role'], b['role'], cyclic(p['graph'])))
    require(len(edges) == 18 and sum(x[2] for x in edges) == 12, 'oracle:edge-count')
    require([(r['from'], r['to'], r['topology']=='graph:feedback') for r in e['edge_audit']] == edges,
            'oracle:edge-report')
    witness = e['counterexample']
    require(same(witness['left']['numeric'], witness['right']['numeric'])
            and witness['left']['numeric'] == {'z':'5','w':'20','v':'1/20'}, 'oracle:lossy-numeric')
    for side, pair in [('left', ('Q:z:out','P:z:in')), ('right', ('P:w:out','R:w:in'))]:
        expected = [b for b in base['graph']['bindings'] if (b['from'], b['to']) == pair]
        require(same(witness[side]['ledger'], expected), 'oracle:lossy-seam')
    require(e['summary'] == dict(
        requests=41, accepted=36, domain_rejected=5, bracketed_constructions=82,
        distinct_occurrences=492, source_reuse_alpha_equal=True, source_audit=audit,
        negative_packets=32, extra_edges=18, cyclic_extra_edges=12), 'oracle:summary')
    # Independently test the declared alpha quotient, never normalize before reception.
    a, ac = deepcopy(e['cases'][0]['left']), deepcopy(e['cases'][3]['left'])
    for p in [a, ac]:
        for obj in p['graph']['events'] + p['graph']['ports']:
            del obj['id']
        for obj in p['graph']['leaves']:
            del obj['occurrence']
        for obj in p['graph']['bindings']:
            del obj['from_id']; del obj['to_id']
        for obj in p['trace']:
            del obj['id']
        del p['request']; del p['scope']
    require(same(a, ac), 'oracle:alpha')
    return e['summary']

def main():
    require(blob(ROOT/'contract.json') == CONTRACT_BLOB, 'contract:pin')
    c = load(ROOT/'contract.json')
    repo = ROOT.parents[2]
    for path, sha in c['frozen_files'].items():
        require(blob(repo/path) == sha, 'frozen:changed:' + path)
    pins = dict(contract_git_blob=CONTRACT_BLOB, implementation_git_blobs={p:blob(ROOT/p) for p in PIN_FILES})
    e = load(ROOT/'evidence-v3.json')
    require(same(e['pins'], pins), 'evidence:pins')
    if len(sys.argv) == 4 and sys.argv[1] == '--packet':
        receive(load(sys.argv[2]), sys.argv[3], c)
        summary = {'packet': 'accepted'}
    else:
        require(len(sys.argv) == 1, 'usage')
        summary = check(e, c)
    print(json.dumps({'oracle':'python-fraction-direct-normal-form', 'summary':summary}, sort_keys=True))

if __name__ == '__main__':
    main()
