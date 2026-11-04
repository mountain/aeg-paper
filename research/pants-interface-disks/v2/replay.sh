#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/../../.."
result_dir="$(mktemp -d)"
trap 'rm -rf "$result_dir"' EXIT
python3 research/pants-interface-disks/verify_v1.py > "$result_dir/v1.json"
cmp "$result_dir/v1.json" research/pants-interface-disks/evidence-v1.json
python3 -O research/pants-interface-disks/verify_v1.py > "$result_dir/v1-opt.json"
cmp "$result_dir/v1.json" "$result_dir/v1-opt.json"
python3 research/pants-interface-disks/verify_v1.py --receive research/pants-interface-disks/evidence-v1.json
python3 research/pants-interface-disks/v2/verify_v2.py > "$result_dir/v2.json"
cmp "$result_dir/v2.json" research/pants-interface-disks/v2/evidence-v2.json
python3 -O research/pants-interface-disks/v2/verify_v2.py > "$result_dir/v2-opt.json"
cmp "$result_dir/v2.json" "$result_dir/v2-opt.json"
python3 research/pants-interface-disks/v2/verify_v2.py --receive research/pants-interface-disks/v2/evidence-v2.json
python3 research/pants-interface-disks/v2/test_reception.py
python3 -O research/pants-interface-disks/v2/test_reception.py
python3 research/pants-interface-disks/v2/review_2026_11_05.py > "$result_dir/review.json"
python3 -O research/pants-interface-disks/v2/review_2026_11_05.py > "$result_dir/review-opt.json"
cmp "$result_dir/review.json" "$result_dir/review-opt.json"
cat "$result_dir/review.json"
