"""Explicit replay coverage and immutable historical contract guard."""
import hashlib
import json
import os
import subprocess
from pathlib import Path
import gapkit
ROOT = Path(__file__).resolve().parents[1]
PREFIX = 'research/process-representation-gap/'
BASELINE = '1556eaedaee0946b2e395320739234dc59ec846c'

def inventory(root=ROOT):
    return json.loads((root / 'tools/replay-inventory.json').read_text())

def blob(repo, ref, path):
    p = subprocess.run(['git', '-C', str(repo), 'show', f'{ref}:{PREFIX}{path}'], capture_output=True)
    gapkit.require(p.returncode == 0, 'REPLAY-PIN-MISSING', f'{ref}:{path}')
    return p.stdout

def ledger(raw):
    entries = {}
    for line in raw.decode().splitlines():
        if not line or line.startswith('#'):
            continue
        digest, name = line.split('  ')
        gapkit.require(name not in entries and len(digest) == 64, 'REPLAY-LEDGER-MALFORMED', line)
        entries[name] = digest
    return entries

def validate_inventory(root=ROOT, check_git=False, repo=None):
    root = Path(root)
    repo = Path(repo or os.environ.get('AEG_PAPER_REPO', ROOT.parent.parent))
    data = inventory(root)
    gapkit.require(data['historical_contract_commit'] == BASELINE, 'REPLAY-BASELINE-CHANGED')
    paths = ['contracts/FROZEN.sha256', 'tools/replay-inventory.json']
    for key, folder, suffix in (('scripts','experiments','.py'), ('contracts','contracts','.json'),
                                ('evidence','evidence','.json'), ('fixtures','fixtures','.json')):
        expected = data[key]
        actual = sorted(str(p.relative_to(root)) for p in (root / folder).glob('*' + suffix))
        gapkit.require(len(expected) == len(set(expected)) and sorted(expected) == actual,
                       'REPLAY-INVENTORY-MISMATCH', key)
        paths += expected
    current = ledger((root / 'contracts/FROZEN.sha256').read_bytes())
    gapkit.require(set(current) == {Path(x).name for x in data['contracts']}, 'REPLAY-LEDGER-COVERAGE')
    for name, digest in current.items():
        gapkit.require(hashlib.sha256((root/'contracts'/name).read_bytes()).hexdigest() == digest,
                       'EXP-CONTRACT-DRIFT', name)
    # Changing BOTH an old contract and the mutable ledger still fails.
    historical = ledger(blob(repo, BASELINE, 'contracts/FROZEN.sha256'))
    for name, digest in historical.items():
        gapkit.require(current.get(name) == digest, 'REPLAY-HISTORICAL-CONTRACT-DRIFT', name)
    if check_git:
        for path in paths:
            gapkit.require((root/path).read_bytes() == blob(repo, 'HEAD', path),
                           'REPLAY-WORKTREE-DRIFT', path)
    return paths

if __name__ == '__main__':
    validate_inventory()
    print('explicit inventory and historical contract pins verified')
