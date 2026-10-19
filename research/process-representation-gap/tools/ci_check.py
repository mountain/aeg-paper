#!/usr/bin/env python3
"""Read-only committed-evidence replay; green means bounded reproducibility."""
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
import gapkit
from verify_inventory import ROOT, inventory, validate_inventory

def strip_local_paths(raw):
    doc = json.loads(raw)
    doc.pop('environment', None)
    for entry in doc.get('repositories', {}).values():
        entry.pop('local_path', None)
    return gapkit.canonical(doc)

def replay():
    report = {'schema':'aeg.process-representation-gap.ci-check.v1.1', 'steps':[], 'failures':[]}
    try:
        validate_inventory(check_git=True)
        report['steps'].append({'step':'immutable-contracts-and-complete-inventory','exit_code':0})
        data = inventory()
        before = {str(p.relative_to(ROOT)):gapkit.sha256_file(p)
                  for p in ROOT.rglob('*') if p.is_file() and '__pycache__' not in p.parts}
        with tempfile.TemporaryDirectory(prefix='aeg-replay-') as td:
            work = Path(td)/'research/process-representation-gap'
            shutil.copytree(ROOT, work, ignore=shutil.ignore_patterns('__pycache__'))
            env = dict(os.environ)
            env['AEG_PAPER_REPO'] = str(ROOT.parent.parent)
            stages = [
                ('contracts-read-only',['tools/freeze_contracts.py','--check']),
                ('repair-regressions',['reviews/verify_repairs_2026_10_19.py']),
                ('repair-regressions-optimized',['-O','reviews/verify_repairs_2026_10_19.py']),
                ('manifest',['tools/build_manifest.py','--out','evidence/manifest.json']),
                ('determinism-and-raw-replay',['tools/check_determinism.py']),
                ('fixtures',['tools/build_fixtures.py','--out','fixtures/INDEX.json']),
                ('gap-classification',['tools/build_gap_classification.py','--out','evidence/gap-classification.json']),
                ('interface-promotion',['tools/build_interface_promotion.py','--out','evidence/interface-promotion.json'])]
            repair_output = None
            for name,args in stages:
                p = subprocess.run([sys.executable,*args],cwd=work,env=env,capture_output=True)
                step = {'step':name,'exit_code':p.returncode}
                if name == 'repair-regressions' and p.returncode == 0:
                    repair_output = p.stdout
                    gapkit.require(p.stdout == (ROOT/'reviews/2026-10-19-repair-results.json').read_bytes(),
                                   'REPLAY-REPAIR-EVIDENCE-DIFFERS')
                if name == 'repair-regressions-optimized' and p.returncode == 0:
                    gapkit.require(p.stdout == repair_output, 'REPLAY-REPAIR-MODE-DIFFERS')
                if p.returncode:
                    step['stdout_tail'] = p.stdout.decode(errors='replace')[-10000:]
                    step['stderr_tail'] = p.stderr.decode(errors='replace')[-5000:]
                    report['failures'].append(step)
                report['steps'].append(step)
                if p.returncode:
                    break
            exact = data['fixtures'] + ['contracts/FROZEN.sha256',
                    'evidence/gap-classification.json','evidence/interface-promotion.json']
            for path in exact:
                gapkit.require((work/path).read_bytes() == (ROOT/path).read_bytes(),
                               'REPLAY-DERIVED-DIFFERS',path)
            gapkit.require(strip_local_paths((work/'evidence/manifest.json').read_bytes()) ==
                           strip_local_paths((ROOT/'evidence/manifest.json').read_bytes()),
                           'REPLAY-MANIFEST-DIFFERS')
        after = {str(p.relative_to(ROOT)):gapkit.sha256_file(p)
                 for p in ROOT.rglob('*') if p.is_file() and '__pycache__' not in p.parts}
        gapkit.require(before == after,'REPLAY-NOT-READ-ONLY')
    except (gapkit.Diagnostic,OSError,ValueError) as exc:
        report['failures'].append({'error':str(exc)})
    report['verdict'] = 'bounded evidence reproduced; no claim promotion' if not report['failures'] else 'FAILED'
    return report

def main():
    report = replay()
    print(gapkit.canonical(report),end='')
    return int(bool(report['failures']))

if __name__ == '__main__':
    raise SystemExit(main())
