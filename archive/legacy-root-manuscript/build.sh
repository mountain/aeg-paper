#!/usr/bin/env bash
set -euo pipefail

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
main="aeg-paper"

resolve_bibtex() {
  if command -v bibtex >/dev/null 2>&1; then
    command -v bibtex
  elif command -v bibtex.original >/dev/null 2>&1; then
    command -v bibtex.original
  else
    echo "bibtex executable not found" >&2
    return 127
  fi
}

bibtex_cmd="$(resolve_bibtex)"

cd "${script_dir}"
pdflatex -halt-on-error -file-line-error -interaction=nonstopmode "${main}.tex"
"${bibtex_cmd}" "${main}"
pdflatex -halt-on-error -file-line-error -interaction=nonstopmode "${main}.tex"
pdflatex -halt-on-error -file-line-error -interaction=nonstopmode "${main}.tex"
test -s "${main}.pdf"

echo "built ${script_dir}/${main}.pdf"
