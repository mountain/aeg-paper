"""Third review route. Exit 1 means the reviewed head has merge blockers.

This records counterexamples, not replacement frozen experimental evidence.
Run from any cwd with Python or Python -O; no external repositories required.
"""
import hashlib
import itertools
import json
import subprocess
import sys
import tempfile
from fractions import Fraction as Q
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'experiments'))
import exp6_knot_deformation_environment as primary
import exp6_knot_deformation_environment_independent as secondary

def need(ok, detail):
    if not ok:
        raise RuntimeError(detail)

def reduce_word(w):
    s = []
    for x in w:
        if s and s[-1] == -x:
            s.pop()
        else:
            s.append(x)
    return tuple(s)

def generator(w, a):
    # Derive inverse substitutions independently from the positive action.
    i = abs(a)
    image = {1: (1,), 2: (2,), 3: (3,)}
    if a > 0:
        image[i], image[i+1] = (i, i+1, -i), (i,)
    else:
        image[i], image[i+1] = (i+1,), (-(i+1), i, i+1)
    out = []
    for x in w:
        v = image[abs(x)]
        out.extend(v if x > 0 else tuple(-z for z in reversed(v)))
    return reduce_word(out)

def action(w, probe):
    for a in reversed(w):
        probe = generator(probe, a)
    return probe

def braid_review():
    words = [w for n in range(7) for w in itertools.product((1,2,-1,-2), repeat=n)]
    actions = {tuple(action(w, (i,)) for i in (1,2,3)) for w in words}
    # Abelianisation gives the same permutation convention without importing it.
    permutations = set()
    for a in actions:
        p = tuple(tuple(sum((1 if x>0 else -1) for x in v if abs(x)==i)
                        for i in (1,2,3)) for v in a)
        permutations.add(p)
    product = {action(w, (1,2,3)) for w in words}
    probe = {action(w, (1,2,3,-1,-2,-3)) for w in words}
    counts = [len(words),len({reduce_word(w) for w in words}),len(actions),len(permutations)]
    rows=json.loads((ROOT/'evidence/exp5-braid-words.raw.json').read_text())['rows']
    names={'s1':1,'s2':2,'S1':-1,'S2':-2}
    spell={1:'x',2:'y',3:'z',-1:'x^-1',-2:'y^-1',-3:'z^-1'}
    need(len(rows)==len(words),'raw braid row count')
    seen=set()
    for row in rows:
        w=tuple(names[x] for x in row['word']);seen.add(w)
        images=tuple(action(w,(i,)) for i in (1,2,3))
        need([''.join(spell[x] for x in v) or '1' for v in images]==row['artin'],'raw Artin images')
        permutation=[]
        for v in images:
            exps=[sum((1 if x>0 else -1) for x in v if abs(x)==i) for i in (1,2,3)]
            need(sorted(exps)==[0,0,1],'abelianised generator image')
            permutation.append(exps.index(1))
        need(permutation==row['permutation'],'raw permutation')
    need(seen==set(words),'raw enumeration coverage')
    need(counts == [5461,1457,577,6], 'braid layer counts')
    need(len(product)==1 and len(probe)==577, 'braid probe counts')
    for i in (1,2):
        for j in (1,2,3):
            need(action((i,-i),(j,))==(j,), 'inverse')
            need(action((-i,i),(j,))==(j,), 'inverse')
    need(tuple(action((1,2,1),(i,)) for i in (1,2,3)) ==
         tuple(action((2,1,2),(i,)) for i in (1,2,3)), 'braid relation')
    return {'counts':counts,'raw_rows_independently_compared':len(rows),'product_probe_classes':len(product),
            'selected_probe_classes':len(probe),'W2_permutation':[2,1,0],
            'scope':'words of length at most six; Artin faithfulness is a cited theorem'}

def timing_review():
    # Literal square and timetable, not either experiment's fixture builder.
    nodes = ((0,0,0),(2,0,0),(2,2,0),(0,2,0))
    breaks = tuple(map(Q,('0','1/4','3/8','1/2','5/8','1')))
    zs = (Q(10),Q(10),Q(0),Q(0),Q(10),Q(10))
    def z(t):
        for k in range(5):
            if breaks[k]<=t<=breaks[k+1]:
                return zs[k]+(zs[k+1]-zs[k])*(t-breaks[k])/(breaks[k+1]-breaks[k])
        raise RuntimeError('time outside timetable')
    raw = json.loads((ROOT/'evidence/exp6-knot-deformation-environment.raw.json').read_text())
    certs = raw['certificates']['w4-P1']
    coverage = {e:[] for e in range(4)}
    margins = []
    for c in certs:
        a,b = map(Q,c['time']);e=c['edge'];verts=[]
        for t in (a,b):
            for v in (nodes[e],nodes[(e+1)%4]):
                verts.append([Q(v[0])+8*t-1,Q(v[1]),Q(v[2])-z(t)])
        need(sorted(verts)==sorted([[Q(x) for x in v] for v in c['vertices']]), 'certificate corners')
        need(c['method']=='coordinate-hull-separation','unexpected certificate method')
        vals=[v[c['axis']] for v in verts];lo,hi=min(vals),max(vals)
        need(lo>Q(1,4) or hi<-Q(1,4),'separation inequality')
        bound=min(abs(lo),abs(hi));need(bound==Q(c['bound']),'stored bound')
        margins.append(bound-Q(1,4));coverage[e].append((a,b))
    for intervals in coverage.values():
        intervals.sort();need(intervals[0][0]==0 and intervals[-1][1]==1,'coverage endpoints')
        need(all(a[1]==b[0] for a,b in zip(intervals,intervals[1:])),'coverage gap')
    need(len(certs)==20 and min(margins)==Q(3,4),'clearance margin')
    # In [1/4,3/8], nearest square point is its left bottom corner.
    # d^2=(8t-1)^2+(30-80t)^2; minimiser is rational.
    t=Q(301,808);d2=(8*t-1)**2+(30-80*t)**2
    need(d2==Q(40400,10201),'analytic distance')
    # P2 waits: at 3/8 its bottom edge contains (1,0,0), ball centre too.
    need(z(Q(3,8))==0,'P2 collision')
    return {'certificates_recomputed':20,'coverage':'all four edges over [0,1]',
            'certified_margin':'3/4','analytic_minimum_squared_distance':str(d2),
            'minimiser':str(t),'P2_collision_time':'3/8',
            'self_embedding_argument':'both paths are rigid translations of a fixed simple square'}

def blockers():
    a=((0,0,0),(1,0,0),(0,1,0));b=((0,0,0),(-1,0,0),(0,-1,0))
    m=primary.motion('review-triangle-collapse',3,[0,1],[a,b])
    p=primary.check_self_embedding(m)[0]
    f={'nodes':3,'closed':True,'bps':(Q(0),Q(1)),'positions':m['positions']}
    s=secondary.self_embedded_verdict(f)['verdict']
    midpoint=primary.is_embedded_at(m,Q(1,2))[0]
    out,_=primary.r2_insert(primary.diagram((),()),0,0)
    w=out['word'];odd=[]
    for label in (1,2):
        at=[k for k,x in enumerate(w) if abs(x)==label]
        if (at[1]-at[0]-1)%2: odd.append(label)
    actual,_=primary.r2_insert(primary.diagram((1,-1,2,-2),(1,-1)),1,3)
    actual_odd=[]
    for label in (1,2,3,4):
        at=[k for k,x in enumerate(actual['word']) if abs(x)==label]
        if (at[1]-at[0]-1)%2: actual_odd.append(label)
    # Isolated copy: demonstrate re-freezing silently accepts an existing-file mutation.
    with tempfile.TemporaryDirectory() as td:
        r=Path(td);(r/'tools').mkdir();(r/'contracts').mkdir()
        for name in ('freeze_contracts.py','gapkit.py'):
            (r/'tools'/name).write_bytes((ROOT/'tools'/name).read_bytes())
        name='example.v1.json';original=b'{"frozen":true}\n'
        (r/'contracts'/name).write_bytes(original)
        old=hashlib.sha256(original).hexdigest()
        (r/'contracts/FROZEN.sha256').write_text(old+'  '+name+'\n')
        changed=b'{"frozen":true,"changed":true}\n';(r/'contracts'/name).write_bytes(changed)
        proc=subprocess.run([sys.executable,str(r/'tools/freeze_contracts.py')],capture_output=True)
        refreshed=hashlib.sha256(changed).hexdigest() in (r/'contracts/FROZEN.sha256').read_text()
    return {'self_embedding_false_acceptance':{'primary':p,'independent':s,
                'actual_midpoint_embedded':midpoint,'blocker':p=='valid' and s=='valid' and not midpoint},
            'R2_nonplanar_Gauss_record':{'word':list(w),'odd_intervening_labels':odd,
                'committed_fixture_word':list(actual['word']),
                'committed_fixture_odd_labels':actual_odd,
                'blocker':bool(odd)},
            'freeze_existing_contract_mutation':{'exit':proc.returncode,'digest_refreshed':refreshed,
                'blocker':proc.returncode==0 and refreshed}}

if __name__=='__main__':
    findings=blockers()
    report={'reviewed_head':'5e4a620ce3a3214159e38b6344a0ae2dd98aa343',
            'braid':braid_review(),'timing':timing_review(),'findings':findings}
    report['merge_ready']=not any(v['blocker'] for v in findings.values())
    print(json.dumps(report,sort_keys=True,indent=2))
    raise SystemExit(0 if report['merge_ready'] else 1)
