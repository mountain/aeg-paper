#!/usr/bin/env python3
"""Fresh-process reception of serialized evidence and adversarial saved packets."""
from copy import deepcopy
from pathlib import Path
import json
import subprocess
import sys
import tempfile

from receive import demand, digest, load_json
from verify_v2 import mutations

HERE = Path(__file__).resolve().parent


def invoke(path, expected=None):
    tool = 'receive.py' if expected is not None else 'verify_v2.py'
    args = [sys.executable, *(['-O'] if sys.flags.optimize else []), str(HERE / tool), '--receive', str(path)]
    if expected is not None:
        args += ['--expected', expected]
    return subprocess.run(args, text=True, capture_output=True, timeout=30)


def main():
    saved = load_json(HERE / 'evidence-v2.json')
    with tempfile.TemporaryDirectory(prefix='oq096-v2-') as directory:
        path = Path(directory) / 'candidate.json'

        def check(obj, reason=None, expected=None):
            path.write_text(json.dumps(obj, sort_keys=True) + '\n')
            result = invoke(path, expected)
            if reason:
                demand(result.returncode == 1 and 'REJECTED: ' + reason + '\n' == result.stderr,
                       'subprocess:unexpected-refusal:' + str(reason) + ':' + result.stderr)
            else:
                demand(result.returncode == 0, 'subprocess:reception:' + result.stderr)
            return result

        for key, candidate in zip(('A', 'B', 'C', 'A-copy', 'different-value'), saved['candidates']):
            received = check(candidate, expected=key)
            demand(json.loads(received.stdout) == saved['results']['accepted'][key], 'subprocess:observations')
        check(saved)
        for _, reason, altered in mutations(saved['candidates']):
            check(altered, reason, 'A')
        # Rehash outer candidates, so semantic failures cannot hide behind checksums.
        altered = deepcopy(saved)
        altered['candidates'][0] = mutations(saved['candidates'])[0][2]
        altered['candidates_sha256'] = digest(altered['candidates'])
        check(altered, 'source:binding')
        altered = deepcopy(saved)
        altered['candidates'][0] = deepcopy(saved['candidates'][1])
        altered['candidates_sha256'] = digest(altered['candidates'])
        check(altered, 'instance:binding')
        altered = deepcopy(saved)
        altered['results']['numeric_equivalence_classes'] = [['A'], ['B'], ['C'], ['A-copy'], ['different-value']]
        check(altered, 'evidence:results')
        altered = deepcopy(saved)
        altered['candidates'].reverse()
        altered['candidates_sha256'] = digest(altered['candidates'])
        check(altered, 'instance:binding')
        path.write_text('{"schema":"x","schema":"y"}\n')
        result = invoke(path, 'A')
        demand(result.returncode == 1 and result.stderr == 'REJECTED: json:duplicate-key\n', 'json:duplicate-accepted')
    print('PASS: 5 fresh receipts, saved evidence, 20 packet mutations, 4 evidence mutations, duplicate-key refusal')


if __name__ == '__main__':
    main()
