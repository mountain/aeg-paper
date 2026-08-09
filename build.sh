#!/usr/bin/env bash
set -euo pipefail

root_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

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

build_paper() {
  local number="$1"
  local paper_dir="${root_dir}/paper-${number}"
  local main="aeg-paper-${number}"
  local bibtex_cmd
  bibtex_cmd="$(resolve_bibtex)"

  if [[ ! -f "${paper_dir}/${main}.tex" ]]; then
    echo "missing canonical source: ${paper_dir}/${main}.tex" >&2
    return 1
  fi

  (
    cd "${paper_dir}"
    pdflatex -halt-on-error -file-line-error -interaction=nonstopmode "${main}.tex"
    "${bibtex_cmd}" "${main}"
    pdflatex -halt-on-error -file-line-error -interaction=nonstopmode "${main}.tex"
    pdflatex -halt-on-error -file-line-error -interaction=nonstopmode "${main}.tex"
    pdflatex -halt-on-error -file-line-error -interaction=nonstopmode "${main}.tex"
    test -s "${main}.pdf"
  )
}

case "${1:-all}" in
  0|1|2|3|4)
    build_paper "$1"
    ;;
  all)
    build_paper 0
    build_paper 1
    build_paper 2
    build_paper 3
    build_paper 4
    ;;
  *)
    echo "usage: $0 [0|1|2|3|4|all]" >&2
    exit 2
    ;;
esac
