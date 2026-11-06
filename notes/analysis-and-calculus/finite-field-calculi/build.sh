#!/usr/bin/env bash
set -euo pipefail
resource_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
"$resource_dir/finite-trig/build.sh"
"$resource_dir/conic-dynamics/build.sh"
