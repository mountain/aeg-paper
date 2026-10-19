"""Executable acceptance for R1--R4 repairs; no claim of human review."""
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
from fractions import Fraction as Q
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(ROOT/'experiments'), str(ROOT/'tools'), str(ROOT/'reviews')]
import exp6_knot_deformation_environment as p
import exp6_knot_deformation_environment_independent as s
import gapkit
import check_determinism as det
from verify_inventory import validate_inventory
from independent_review_2026_10_14 import braid_review, timing_review

def need(ok, detail):
    gapkit.require(ok, 'REPAIR-REGRESSION', detail)

def reject(fn, code):
    return gapkit.reject(fn, code)['code']

def geometric_controls():
    a=((0,0,0),(1,0,0),(0,1,0))
    cases = [
        ('rigid-triangle',a,tuple((x+2,y+3,z-1) for x,y,z in a),'valid'),
        ('collapse-half',a,tuple((-x,-y,z) for x,y,z in a),'not-certified'),
        ('collapse-third',a,tuple((-2*x,-2*y,z) for x,y,z in a),'not-certified'),
        ('nontranslation-expansion',a,tuple((2*x,2*y,z) for x,y,z in a),'not-certified'),
        ('adjacent-overlap',((0,0,0),(2,0,0),(1,0,0)),None,'invalid'),
        ('edge-collapse',((0,0,0),(0,0,0),(1,1,0)),None,'invalid'),
        ('two-nodes',((0,0,0),(1,0,0)),None,'invalid'),
        ('crossed-square',((0,0,0),(2,2,0),(0,2,0),(2,0,0)),None,'invalid')]
    out=[]
    for name,start,end,expected in cases:
        end = start if end is None else end
        m=p.motion(name,len(start),[0,1],[start,end])
        f={'nodes':len(start),'closed':True,'bps':(Q(0),Q(1)),'positions':m['positions']}
        left=p.check_self_embedding(m)[0]
        right=s.self_embedded_verdict(f)['verdict']
        need(left == expected and right == expected, f'{name}: {left}/{right} expected {expected}')
        out.append({'case':name,'primary':left,'secondary':right})
    return out

def contract_controls():
    results={}
    with tempfile.TemporaryDirectory() as td:
        root=Path(td)/'research/process-representation-gap'
        shutil.copytree(ROOT,root,ignore=shutil.ignore_patterns('__pycache__'))
        repo=Path(os.environ.get('AEG_PAPER_REPO',ROOT.parent.parent))
        name='exp1-order-and-mixing.v1.json'
        path=root/'contracts'/name
        original=path.read_bytes(); ledger=root/'contracts/FROZEN.sha256'; old_ledger=ledger.read_bytes()
        path.write_bytes(original+b'\n')
        proc=subprocess.run([sys.executable,str(root/'tools/freeze_contracts.py')],capture_output=True)
        need(proc.returncode != 0 and b'EXP-CONTRACT-DRIFT' in proc.stderr,'old-version freeze must fail')
        need(ledger.read_bytes()==old_ledger,'failed freeze must not write ledger')
        results['old-version-mutation']='EXP-CONTRACT-DRIFT'
        results['mutated-contract']=reject(lambda:validate_inventory(root,repo=repo),'EXP-CONTRACT-DRIFT')
        ledger.write_bytes(old_ledger.replace(hashlib.sha256(original).hexdigest().encode(),
                          hashlib.sha256(path.read_bytes()).hexdigest().encode()))
        results['mutated-contract-and-ledger']=reject(lambda:validate_inventory(root,repo=repo),
                                                      'REPLAY-HISTORICAL-CONTRACT-DRIFT')
        path.write_bytes(original);ledger.write_bytes(old_ledger)
        ledger.write_bytes(old_ledger.replace(hashlib.sha256(original).hexdigest().encode(),b'0'*64))
        results['ledger-only-mutation']=reject(lambda:validate_inventory(root,repo=repo),'EXP-CONTRACT-DRIFT')
        ledger.write_bytes(old_ledger)
        evidence=root/'evidence/exp5-braid-nonarithmetic.json';raw=evidence.read_bytes();evidence.unlink()
        results['deleted-evidence']=reject(lambda:validate_inventory(root,repo=repo),'REPLAY-INVENTORY-MISMATCH')
        evidence.write_bytes(raw)
        rawpath=root/'evidence/exp5-braid-words.raw.json'
        doc=json.loads(rawpath.read_bytes());doc['rows'][0]['permutation']=[2,1,0]
        rawpath.write_text(gapkit.canonical(doc))
        # Exercise actual raw regeneration, not merely a comparison to HEAD.
        old_root=det.ROOT
        try:
            det.ROOT=root
            results['mutated-raw-row']=reject(lambda:det.run(root/'experiments/exp5_braid_nonarithmetic.py',False,0),
                                             'DET-RAW-DIFFERS')
        finally:
            det.ROOT=old_root
    return results

def main():
    geometry=geometric_controls()
    current=json.loads((ROOT/'evidence/exp6-knot-deformation-environment.json').read_text())
    need('not certified' in current['gates']['C_process_faithful']['verdict'],'gate C must remain syntactic')
    need('trefoil' in current['environments']['thickened-surface']['not_strict_embedding'],'torus correction missing')
    need('standard unknotted' in current['environments']['strict-torus']['ambient_embedding'],'torus framing missing')
    d,_=p.r2_insert(p.diagram((1,-1,2,-2),(1,-1)),1,3)
    odd=[]
    for label in (1,2,3,4):
        where=[i for i,x in enumerate(d['word']) if abs(x)==label]
        if (where[1]-where[0]-1)%2: odd.append(label)
    need(odd == [3,4],'historical R2 counterexample must remain visible')
    result={'schema':'aeg.exp6-repair-acceptance.v1','geometry':geometry,
            'r2':{'odd_labels':odd,'interpretation':'abstract signed-word calculus only'},
            'integrity_controls':contract_controls(),'braid':braid_review(),'timing':timing_review(),
            'verdict':'bounded repair obligations held; general embedding and planar moves remain open'}
    print(gapkit.canonical(result),end='')

if __name__=='__main__':
    main()
