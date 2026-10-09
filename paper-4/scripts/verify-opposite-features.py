#!/usr/bin/env python3
"""Finite snapshot adapter, not Adva mechanism execution or AES motion."""
import importlib.util
import sys
import json
import hashlib
from pathlib import Path
from collections import Counter
from copy import deepcopy
from dataclasses import replace

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('ported', HERE / 'verify-ported-aes.py')
p = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = p
spec.loader.exec_module(p)
require = p.require
COMMIT = 'cce73004c2b4fbfb87d9ba1ccc66820423273cf6'
SHA256 = '637c2d05663fcee780156d93f4f9e19f829418213a4948c91113141b64d3a579'
POLICY = 'snapshot-v1:literal-events+labelled-carriers;no-mechanism-execution'

def extract(data, side):
    raw, saved = data['relation'][side], data[side]
    events = raw['steps']
    word = [e['mechanism'] for e in events]
    require(word == raw['mechanism_path']['steps'], 'raw word disagreement')
    require(len({e['frame'] for e in events}) == len(events), 'duplicate frame')
    require(raw['start'] == events[0]['input'] and raw['end'] == events[-1]['output'], 'boundary disagreement')
    require(len(raw['handoffs']) == len(events)-1, 'handoff coverage')
    route = {'history_to':'subject', 'result_to':'method', 'evidence_to':'object'}
    for a,b,h in zip(events, events[1:], raw['handoffs']):
        require((h['from'], h['to'], h['route']) == (a['frame'], b['frame'], route), 'handoff contract')
        require(tuple(a['output'][k] for k in ('history','result','evidence')) == tuple(b['input'][k] for k in ('subject','method','object')), 'handoff carrier mismatch')
    count = Counter(word)
    T = (len(events), len(raw['handoffs']), 3*len(raw['handoffs']))
    S = tuple(raw['start'][k] for k in ('subject','method','object')) + tuple(raw['end'][k] for k in ('history','result','evidence'))
    C = tuple(count[k] for k in ('compute','verify','learn')) + (len(word), sum(a!=b for a,b in zip(word,word[1:])))
    require(T == tuple(saved['time'].values()), 'stored T disagreement')
    require(S == tuple(saved['space']['start'].values())+tuple(saved['space']['end'].values()), 'stored S disagreement')
    require(C == tuple(saved['construction']['incidence'][k] for k in ('compute','verify','learn'))+(saved['construction']['step_count'],saved['construction']['alternations']), 'stored C disagreement')
    require(word == saved['construction']['ordered_word'], 'stored word disagreement')
    return dict(side=side, policy=POLICY, repository='mountain/adva', commit=COMMIT,
                path='programs/bootstrap-0/first-trace-arithmetic.adva', transport_sha256=SHA256,
                source_witness_digest=data['source_witness_digest'], source_document_digest=data['source_document_digest'],
                trace_digest=saved['trace_digest'], events=events, handoffs=raw['handoffs'], T=T, S=S, C=C,
                word=word, residual=data['additive_residual'], trust='pinned repository record; not external truth authentication')

def run(packet):
    # Host extraction is separate from the arithmetic DAG: these are Q-valued
    # adapters, NOT casts of labelled carrier IDs or implementations of compute.
    b=p.Builder('body/'+packet['side'])
    c,v,f,h=[b.input(x) for x in ('compute','verify','frames','handoffs')]
    f1,f2=b.gate('copy-f','copy',(f,)); h1,h2=b.gate('copy-h','copy',(h,))
    y1,=b.gate('incidence','add',(c,v)); y2,=b.gate('frame-gap','sub',(f1,h1))
    three,=b.gate('port-arity','const',parameter=3)
    ports,=b.gate('ports','mul',(three,h2)); y3,=b.gate('ports-per-frame','div',(ports,f2))
    body=b.finish((y1,y2,y3))
    values=(packet['C'][0],packet['C'][1],packet['T'][0],packet['T'][1])
    qs=[]
    for i,value in enumerate(values):
        # Each extraction source points to its exact packet and adapter field.
        source=f"adva@{COMMIT}/{packet['side']}/adapter/{i}"
        q=p.Builder(f"{packet['side']}/q{i}",source)
        w,=q.gate('snapshot','const',parameter=value)
        qs.append(q.finish((w,)))
    n=p.substitute(body,qs,tuple((i,0,i) for i in range(4)))
    out,trace=p.evaluate(n)
    require(out == p.evaluate(body,values)[0], 'substitution/evaluation mismatch')
    require(out == p.evaluate(n,order=p.schedule(n,reverse=True))[0], 'schedule disagreement')
    occurrences={g.occurrence for g in n.gates.values()}
    require(all(g.occurrence in occurrences for q in qs for g in q.gates.values()), 'lost producer occurrence')
    # Type guard at the actual graft boundary.
    bad=deepcopy(qs); w=bad[0].outputs[0]
    bad[0].wires[w]=replace(bad[0].wires[w],type='CarrierID')
    p.reject(lambda:p.substitute(body,bad,tuple((i,0,i) for i in range(4))), 'type mismatch')
    p.reject(lambda:p.evaluate(body,(2,1,0,2)), 'division by zero')
    return dict(scalars=list(map(str,out)), packet=packet, receipt=n.receipt, execution=trace,
                wires=[p.wire_record(w) for w in n.wires.values()], gates=[p.gate_record(g) for g in n.gates.values()])

def main():
    raw=(HERE/'fixtures/opposite-features/adva-0114.json').read_bytes()
    require(hashlib.sha256(raw).hexdigest()==SHA256,'frozen transport bytes changed')
    data=json.loads(raw)
    a,b=[extract(data,s) for s in ('left','right')]
    require(a['T']==b['T'] and a['S']==b['S'] and a['C']!=b['C'],'chi_C collision missing')
    for key,stored in [('T',tuple(data['additive_residual']['time'].values())),('S',tuple(data['additive_residual']['space']['start']+data['additive_residual']['space']['end'])),('C',tuple(data['additive_residual']['construction'].values()))]:
        require(tuple(x-y for x,y in zip(a[key],b[key]))==stored,'residual mismatch')
    tampered=deepcopy(data)
    tampered['relation']['left']['steps'][0]['mechanism']='verify'
    try:
        extract(tampered,'left')
    except AssertionError:
        pass
    else:
        raise AssertionError('inconsistent event record accepted')
    runs=[run(x) for x in (a,b)]
    require(runs[0]['scalars']==runs[1]['scalars']==['3','1','2'],'scalar control')
    require(runs[0]['packet']['word']!=runs[1]['packet']['word'],'history observation failed')
    # Stronger synthetic control: identical incidence/length/alternations.
    words=[['compute','verify','compute','verify'],['verify','compute','verify','compute']]
    shadow=lambda w:(w.count('compute'),w.count('verify'),len(w),sum(x!=y for x,y in zip(w,w[1:])))
    require(shadow(words[0])==shadow(words[1]) and words[0]!=words[1],'order collision')
    # Formal commutative weights: ratio exponent (compute,verify) = (-1,+1).
    exponent=tuple(b['C'][i]-a['C'][i] for i in (0,1))
    require(exponent==(-1,1),'formal holonomy')
    print(json.dumps(dict(schema='aeg.opposite-feature-snapshot.v1',runs=runs,
        controls={'inconsistent_event_rejected':True,'scalar_history_collision':True,'synthetic_words':words,'synthetic_shadow':shadow(words[0]),'binding_type_rejected':True,'zero_frames_rejected':True,'schedule_independence':True,'formal_ratio_exponents':exponent},
        chi={'C_from_T_S':'impossible on this two-record domain for declared projections','T_from_S_C':'sample-consistent only; no general witness','S_from_C_T':'sample-consistent only; no general witness'},
        spectral='not defined: no endomorphism/domain/closure supplied', truth_fiber=data['truth_fiber']),sort_keys=True,indent=2))

if __name__=='__main__':
    main()
