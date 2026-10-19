#!/usr/bin/env python3
"""Exact finite calibration; synthetic models, not native Adva execution.

Authored by Codex (OpenAI), under Mingli Yuan's research direction.
No assertions: normal and optimized runs enforce identical checks.
"""
import itertools
import json


def require(condition, message):
    if not condition:
        raise ValueError(message)


def order(vertices, edges):
    require(len(set(vertices)) == len(vertices), 'duplicate event')
    require(all(x in vertices and y in vertices for x, y in edges), 'endpoint')
    require(all(x != y for x, y in edges), 'self-loop')
    reach = {(v, v) for v in vertices} | set(edges)
    for k in vertices:
        reach |= {(i, j) for i in vertices for j in vertices
                  if (i, k) in reach and (k, j) in reach}
    require(not any(x != y and (y, x) in reach for x, y in reach), 'cycle')
    return reach


def ideals(vertices, reach):
    return [frozenset(v for i, v in enumerate(vertices) if mask >> i & 1)
            for mask in range(1 << len(vertices))
            if all(not (mask >> vertices.index(y) & 1) or
                   (mask >> vertices.index(x) & 1) for x, y in reach)]


def reconstruct(vertices, opens):
    return {(x, y) for x in vertices for y in vertices
            if all(y not in u or x in u for u in opens)}


def join_irreducibles(opens):
    # Independent lattice-only algorithm: no original vertices/order used.
    return [u for u in opens if u and not any(
        a < u and b < u and a | b == u for a in opens for b in opens)]


def determinant(matrix):
    n = len(matrix)
    total = 0
    for p in itertools.permutations(range(n)):
        term = (-1) ** sum(p[i] > p[j] for i in range(n) for j in range(i+1, n))
        for i in range(n):
            term *= matrix[i][p[i]]
        total += term
    return total


def characteristic(matrix):
    # For these 3x3 matrices coefficient formulas use principal minors.
    require(len(matrix) == 3, 'three-event characteristic only')
    trace = sum(matrix[i][i] for i in range(3))
    minors = sum(matrix[i][i]*matrix[j][j]-matrix[i][j]*matrix[j][i]
                 for i in range(3) for j in range(i+1, 3))
    return [1, -trace, minors, -determinant(matrix)]


def frontier(u, wires):
    return [w for w in wires if (w['producer'] == 'input' or w['producer'] in u)
            and (w['consumer'] == 'output' or w['consumer'] not in u)]


def packet(producer, consumer, occurrence, source, slot=0, role='internal'):
    return dict(producer=producer, consumer=consumer, occurrence=occurrence,
                source=source, type='Q', slot=slot, role=role)


def model(name, edges):
    vertices = ['a', 'b', 'c']
    reach = order(vertices, edges)
    opens = ideals(vertices, reach)
    require(reconstruct(vertices, opens) == reach, 'topology reconstruction')
    jis = join_irreducibles(opens)
    principal = {v: frozenset(x for x in vertices if (x, v) in reach) for v in vertices}
    require(set(jis) == set(principal.values()), 'lattice reconstruction')
    require(all(((x, y) in reach) == (principal[x] <= principal[y])
                for x in vertices for y in vertices), 'JI order')
    adj = [[int((x, y) in edges) for y in vertices] for x in vertices]
    und = [[int((x, y) in edges or (y, x) in edges) for y in vertices] for x in vertices]
    lap = [[sum(und[i]) if i == j else -und[i][j] for j in range(3)] for i in range(3)]
    wires = [packet(x, y, 'edge-'+str(i), 'event:'+x) for i, (x,y) in enumerate(edges)]
    for v in vertices:
        if not any(y == v for x,y in edges):
            wires.append(packet('input', v, 'input-'+v, 'external:'+v))
        if not any(x == v for x,y in edges):
            wires.append(packet(v, 'output', 'output-'+v, 'event:'+v, role='result'))
    recovered = {w['occurrence'] for u in opens for w in frontier(u,wires)}
    require(recovered == {w['occurrence'] for w in wires}, 'all wires visible')
    return dict(name=name, edges=edges, order=sorted(reach), laplacian=lap,
                characteristic=characteristic(lap), adjacency_characteristic=characteristic(adj),
                opens=[sorted(u) for u in opens], join_irreducibles=[sorted(u) for u in jis],
                ideal_size_polynomial=[sum(len(u) == k for u in opens) for k in range(4)],
                boundaries=[dict(open=sorted(u), wires=frontier(u, wires)) for u in opens])


def exhaustive():
    vertices = ['a','b','c']
    possible = [(x,y) for x in vertices for y in vertices if x != y]
    unique = set()
    for mask in range(64):
        edges = [e for i,e in enumerate(possible) if mask >> i & 1]
        try:
            reach = order(vertices, edges)
        except ValueError:
            continue
        unique.add(tuple(sorted(reach)))
    for pairs in unique:
        reach = set(pairs)
        opens = ideals(vertices, reach)
        require(reconstruct(vertices, opens) == reach, 'exhaustive reconstruction')
        require(set(join_irreducibles(opens)) == {
            frozenset(x for x in vertices if (x,y) in reach) for y in vertices}, 'JI census')
    require(len(unique) == 19, 'labelled poset census')
    return len(unique)


def run(steps, shared=True, swap=False, stop_after=None):
    # Minimal one-control-location self-loop: x <- x+1; emit after each step.
    # Two immutable input sites s0,s1 have equal Q values. Copy ancestry is
    # shared s0/s0 versus independent s0/s1; this does not change scalar state.
    x = 0
    events = []
    for k in range(steps):
        if stop_after is not None and k >= stop_after:
            break
        x += 1
        events.append(dict(event='e'+str(k), transition='tick', iteration=k,
                           predecessors=[] if k == 0 else ['e'+str(k-1)], value=x,
                           occurrences=['e'+str(k)+':left','e'+str(k)+':right'],
                           sources=['s0','s0' if shared else 's1'],
                           outputs={'history' if not swap else 'evidence': list(range(k+1)),
                                    'result':x,
                                    'evidence' if not swap else 'history':{'checked_steps':k+1}}))
    return events


def guarded_run(budget, limit, shared=True, swap=False, ignore_guard=False):
    """Separate machine: finite control, unbounded counter; halt at x == limit.

    budget bounds observation, not execution semantics. A refused tick emits no
    event. ignore_guard is used only by the executable mutation control.
    """
    x, events, attempts = 0, [], []
    while len(attempts) < budget:
        enabled = ignore_guard or limit is None or x < limit
        attempts.append(dict(before=x, enabled=enabled,
                             after=x + 1 if enabled else x))
        if not enabled:
            break
        k = x
        x += 1
        events.append(dict(event=f'e{k}', transition='tick', iteration=k,
                           predecessors=[] if k == 0 else [f'e{k-1}'], value=x,
                           occurrences=[f'e{k}:left', f'e{k}:right'],
                           sources=['s0', 's0' if shared else 's1'],
                           outputs={'history' if not swap else 'evidence': list(range(x)),
                                    'result': x,
                                    'evidence' if not swap else 'history': {'checked_steps': x}}))
    enabled = ignore_guard or limit is None or x < limit
    return dict(contract=dict(stop_after=limit, shared=shared, swap=swap),
                observation_budget=budget, events=events, attempts=attempts,
                state=x, future_tick_enabled=enabled,
                observation_status='truncated' if enabled else 'complete')


def cyclic():
    rows = []
    for n in [0,1,2,3,6]:
        ev = run(n)
        vertices = [e['event'] for e in ev]
        edges = [(vertices[k-1],vertices[k]) for k in range(1,n)]
        reach = order(vertices, edges)
        require(len(ideals(vertices,reach)) == n+1, 'prefix chain opens')
        require(run(n+1)[:n] == ev, 'prefix compatibility')
        loop = guarded_run(n+1, None)
        stopped = guarded_run(n+1, n)
        require(loop['events'][:n] == stopped['events'] == ev, 'common prefix')
        require(loop['attempts'][-1] == dict(before=n, enabled=True, after=n+1), 'legal continuation')
        require(stopped['attempts'][-1] == dict(before=n, enabled=False, after=n), 'guard refusal')
        # Removing the guard survives the old prefix-only assertion, but must
        # fail the new extension criterion, including the zero-event horizon.
        mutant = guarded_run(n+1, n, ignore_guard=True)
        require(mutant['events'][:n] == ev, 'mutant survives weak test')
        require(mutant['events'] != stopped['events'], 'guard mutant killed')
        if n:
            require(run(n,shared=False) != ev, 'source collision control')
            require(run(n,swap=True) != ev, 'role collision control')
            require([e['value'] for e in run(n,shared=False)] == [e['value'] for e in ev], 'value policy')
        rows.append(dict(horizon=n, events=ev, open_count=n+1,
                         future_tick_enabled_in_loop=loop['future_tick_enabled'],
                         future_tick_enabled_in_stopped=stopped['future_tick_enabled'],
                         loop=loop, stopped=stopped,
                         stopped_prefix=guarded_run(n, n),
                         loop_prefix=guarded_run(n, None),
                         independent_sources=guarded_run(n+1, None, shared=False),
                         swapped_roles=guarded_run(n+1, None, swap=True)))
    require(run(1)[-1]['transition'] == run(3)[-1]['transition'], 'control identity')
    require(run(1)[-1]['outputs'] != run(3)[-1]['outputs'], 'control loses history/result')
    rejected = False
    try:
        order(['tick'], [('tick','tick')])
    except ValueError:
        rejected = True
    require(rejected, 'cyclic control cannot be treated as event poset')
    return rows


def main():
    chain = model('chain', [('a','b'),('b','c')])
    fork = model('fork', [('b','a'),('b','c')])
    require(chain['laplacian'] == fork['laplacian'], 'same undirected operator')
    require(chain['characteristic'] == [1,-4,3,0], 'exact lambda(lambda-1)(lambda-3)')
    require(chain['adjacency_characteristic'] == fork['adjacency_characteristic'] == [1,0,0,0], 'directed nilpotent spectrum')
    require([len(chain['opens']),len(fork['opens'])] == [4,5], 'open census')
    require(chain['ideal_size_polynomial'] == [1,1,1,1] and
            fork['ideal_size_polynomial'] == [1,1,2,1], 'rank polynomial')
    # Count-only invariants fail on a chain and its labelled reverse.
    reverse = model('reverse', [('c','b'),('b','a')])
    require(len(reverse['opens']) == len(chain['opens']) and reverse['order'] != chain['order'], 'count-only collision')
    # Same event order, types, values, occurrences; different source sharing.
    cut = frozenset(['b'])
    shared = [packet('b','a','left','s0'),packet('b','c','right','s0')]
    independent = [packet('b','a','left','s0'),packet('b','c','right','s1')]
    require(frontier(cut,shared) != frontier(cut,independent), 'frontier sharing')
    require([{k:v for k,v in w.items() if k != 'source'} for w in shared] ==
            [{k:v for k,v in w.items() if k != 'source'} for w in independent], 'source-only control')
    print(json.dumps(dict(schema='aeg.process-spectrum.v1', models=[chain,fork,reverse],
                          labelled_posets_checked=exhaustive(),
                          source_control=dict(open=['b'],shared=shared,independent=independent),
                          anytime=cyclic()), indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
