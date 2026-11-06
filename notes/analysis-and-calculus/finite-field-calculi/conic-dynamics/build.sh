#!/usr/bin/env bash
set -euo pipefail
resource_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
note_dir="$(cd "$resource_dir/../.." && pwd)"
python3 "$resource_dir/verify.py"
main="49-conic-histories-and-finite-calculi"
cd "$note_dir"
for pass in 1 2 3; do
  if ! pdflatex -halt-on-error -file-line-error -interaction=nonstopmode "$main.tex" >"$main.build.log"; then
    tail -40 "$main.build.log" >&2
    exit 1
  fi
done
test -s "$main.pdf"
if rg -n 'Undefined control sequence|LaTeX Error|undefined references|Citation .* undefined|Reference .* undefined|multiply defined|not found|Overfull \\hbox|Overfull \\vbox|LaTeX Warning|Package .* Warning' "$main.log"; then
  echo "Build requires attention; see $main.log" >&2
  exit 1
fi
echo "Built $main.pdf; no reference, citation, label, asset, or layout warnings."
