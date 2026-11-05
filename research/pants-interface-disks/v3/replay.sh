#!/usr/bin/env bash
set -euo pipefail
here="$(cd "$(dirname "$0")" && pwd)"
task_tmp="$(mktemp -d)"
trap 'rm -rf "$task_tmp"' EXIT
node "$here/cli.mjs" generate > "$task_tmp/normal.json"
cmp "$task_tmp/normal.json" "$here/evidence-v3.json"
node --jitless "$here/cli.mjs" generate > "$task_tmp/jitless.json"
cmp "$task_tmp/normal.json" "$task_tmp/jitless.json"
node "$here/cli.mjs" check "$here/evidence-v3.json"
node "$here/cli.mjs" selftest
python3 "$here/oracle.py" > "$task_tmp/oracle.json"
python3 -O "$here/oracle.py" > "$task_tmp/oracle-optimized.json"
cmp "$task_tmp/oracle.json" "$task_tmp/oracle-optimized.json"
cat "$task_tmp/oracle.json"
