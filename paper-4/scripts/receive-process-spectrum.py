#!/usr/bin/env python3
"""Independent finite receiver; imports no producer functions.

Contracts are trusted test inputs, not inferred from emitted values. Source IDs
are synthetic declared ancestry, not cryptographic/native Adva authorization.
Authored by Codex (OpenAI), research direction Mingli Yuan.
"""
import copy
import itertools
import json
import sys


def check(ok, message):
    if not ok:
        raise ValueError(message)


def receive(receipt, budget, limit, shared=True, swap=False):
    check(type(budget) is int and budget >= 0, 'budget')
    check(limit is None or type(limit) is int and limit >= 0, 'limit')
    count = budget if limit is None else min(budget, limit)
    expected_events = []
    # Closed-form event checks, no execution of the producer's transition code.
    for i in range(count):
        expected_events.append({
            'event': 'e%d' % i, 'transition': 'tick', 'iteration': i,
            'predecessors': [] if i == 0 else ['e%d' % (i-1)],
            'value': i+1, 'occurrences': ['e%d:left' % i, 'e%d:right' % i],
            'sources': ['s0', 's0' if shared else 's1'],
            'outputs': {'evidence' if swap else 'history': list(range(i+1)),
                        'result': i+1,
                        'history' if swap else 'evidence': {'checked_steps': i+1}}})
    attempts = [{'before': i, 'enabled': True, 'after': i+1} for i in range(count)]
    if limit is not None and budget > limit:
        attempts.append({'before': limit, 'enabled': False, 'after': limit})
    enabled = limit is None or count < limit
    expected = dict(contract=dict(stop_after=limit, shared=shared, swap=swap),
                    observation_budget=budget, events=expected_events,
                    attempts=attempts, state=count, future_tick_enabled=enabled,
                    observation_status='truncated' if enabled else 'complete')
    # Canonical JSON comparison also rejects bool-as-int and unexpected fields.
    check(json.dumps(receipt, sort_keys=True) == json.dumps(expected, sort_keys=True),
          'receipt contract/history/source/role/guard mismatch')


def math_audit(data):
    # Enumerate all 3^3 orientations (absent/forward/reverse) directly, retain
    # only transitive relations. This avoids producer closure and dedup code.
    vertices = ('a', 'b', 'c')
    pairs = list(itertools.combinations(vertices, 2))
    relations = []
    for choices in itertools.product((0, 1, -1), repeat=3):
        r = {(v, v) for v in vertices}
        for (x, y), direction in zip(pairs, choices):
            if direction:
                r.add((x, y) if direction == 1 else (y, x))
        if all((x, z) in r for x, y in r for w, z in r if y == w):
            relations.append(r)
    check(len(relations) == data['labelled_posets_checked'] == 19, 'poset census')
    for r in relations:
        opens = [frozenset(u) for size in range(4)
                 for u in itertools.combinations(vertices, size)
                 if all(y not in u or x in u for x, y in r)]
        recovered = {(x, y) for x in vertices for y in vertices
                     if not any(y in u and x not in u for u in opens)}
        # In a finite lattice, a nonzero element is join-irreducible iff it
        # has exactly one lower cover; differs from producer pairwise joins.
        ji = []
        for u in opens:
            covers = [v for v in opens if v < u and
                      not any(v < w < u for w in opens)]
            if u and len(covers) == 1:
                ji.append(u)
        principal = {y: frozenset(x for x in vertices if (x, y) in r) for y in vertices}
        check(recovered == r and set(ji) == set(principal.values()), 'reconstruction')
        check(all(((x, y) in r) == (principal[x] <= principal[y])
                  for x in vertices for y in vertices), 'abstract JI order')
    for m, strict, expected_count in zip(data['models'],
            [set([('a','b'),('b','c'),('a','c')]),
             set([('b','a'),('b','c')]), set([('c','b'),('b','a'),('c','a')])], [4,5,4]):
        r = strict | {(v,v) for v in vertices}
        check(set(map(tuple,m['order'])) == r, 'marked order')
        opens = {frozenset(u) for size in range(4) for u in itertools.combinations(vertices,size)
                 if all(y not in u or x in u for x,y in r)}
        check(set(map(frozenset,m['opens'])) == opens and len(opens) == expected_count, 'opens')
        check(set(map(frozenset,m['join_irreducibles'])) ==
              {frozenset(x for x in vertices if (x,y) in r) for y in vertices}, 'model JI')
        covers = {(x,y) for x,y in strict if not any((x,z) in strict and (z,y) in strict for z in vertices)}
        check(set(map(tuple,m['edges'])) == covers, 'cover edges')
        lap = [[sum((x,z) in covers or (z,x) in covers for z in vertices) if x == y
                else -int((x,y) in covers or (y,x) in covers) for y in vertices] for x in vertices]
        check(lap == m['laplacian'], 'Laplacian')
        # Exact 3x3 determinant by six-term formula. Three distinct roots plus
        # monic degree three determine the characteristic polynomial exactly.
        for t in (0,1,3):
            a,b,c = [[t*int(i==j)-lap[i][j] for j in range(3)] for i in range(3)]
            det = a[0]*(b[1]*c[2]-b[2]*c[1])-a[1]*(b[0]*c[2]-b[2]*c[0])+a[2]*(b[0]*c[1]-b[1]*c[0])
            check(det == 0, 'exact spectral root')
        check(m['characteristic'] == [1,-4,3,0], 'polynomial')
        check(m['adjacency_characteristic'] == [1,0,0,0], 'DAG nilpotence')
        check(m['ideal_size_polynomial'] == [sum(len(u)==k for u in opens) for k in range(4)], 'rank counts')


def main():
    data = json.load(open(sys.argv[1], encoding='utf-8'))
    math_audit(data)
    killed = []
    for row, n in zip(data['anytime'], (0,1,2,3,6)):
        check(row['horizon'] == n and row['open_count'] == n+1, 'horizon')
        for key, budget, limit in [('loop',n+1,None),('stopped',n+1,n),
                                  ('loop_prefix',n,None),('stopped_prefix',n,n)]:
            receive(row[key], budget, limit)
        receive(row['independent_sources'], n+1, None, shared=False)
        receive(row['swapped_roles'], n+1, None, swap=True)
        check(row['loop']['events'][:n] == row['stopped']['events'] == row['events'], 'prefix')
        check(row['future_tick_enabled_in_loop'] is True and
              row['future_tick_enabled_in_stopped'] is False, 'derived enabling')
        # Full run cannot be inferred from event count alone: the loop prefix
        # and stopped complete run have equal observations, different contracts.
        mutant = copy.deepcopy(row['loop'])
        mutant['contract']['stop_after'] = n
        check(mutant['events'][:n] == row['events'], 'weak test survival')
        mutations = [('guard-removed-weak-test-survivor', mutant, n+1, n)]
        for field, value in [('future_tick_enabled',True), ('observation_status','truncated'),
                             ('state',n+1), ('attempts',row['loop']['attempts'])]:
            bad = copy.deepcopy(row['stopped']); bad[field] = value
            mutations.append((field,bad,n+1,n))
        if n:
            for label in ('source','role','history','occurrence','predecessor','result','evidence','event-deletion'):
                bad = copy.deepcopy(row['stopped']); event = bad['events'][-1]
                if label == 'source': event['sources'][1] = 's1'
                elif label == 'role': event['outputs']['history'],event['outputs']['evidence'] = event['outputs']['evidence'],event['outputs']['history']
                elif label == 'history': event['outputs']['history'] = []
                elif label == 'occurrence': event['occurrences'][1] = event['occurrences'][0]
                elif label == 'predecessor': event['predecessors'] = ['foreign']
                elif label == 'result': event['outputs']['result'] += 1
                elif label == 'evidence': event['outputs']['evidence']['checked_steps'] += 1
                else: bad['events'].pop()
                mutations.append((label,bad,n+1,n))
        bad = copy.deepcopy(row['loop_prefix']); bad['observation_status'] = 'complete'
        mutations.append(('truncated-as-complete',bad,n,None))
        for label,bad,budget,limit in mutations:
            try: receive(bad,budget,limit)
            except ValueError: killed.append([n,label])
            else: raise ValueError('mutation survived: '+label)
    check(len(data['anytime']) == 5, 'row coverage')
    print(json.dumps(dict(schema='aeg.process-spectrum.receiver.v1',
                          labelled_posets_checked=19, receipts_checked=30,
                          rejected_mutations=killed),indent=2,sort_keys=True))


if __name__ == '__main__':
    main()
