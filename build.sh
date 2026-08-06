#!/usr/bin/env bash
set -euo pipefail

root_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

build_paper() {
  local number="$1"
  local paper_dir="${root_dir}/paper-${number}"
  local main="aeg-paper-${number}"

  (
    cd "${paper_dir}"
    pdflatex -halt-on-error -file-line-error -interaction=nonstopmode "${main}.tex"
    bibtex "${main}"
    pdflatex -halt-on-error -file-line-error -interaction=nonstopmode "${main}.tex"
    pdflatex -halt-on-error -file-line-error -interaction=nonstopmode "${main}.tex"
    pdflatex -halt-on-error -file-line-error -interaction=nonstopmode "${main}.tex"
    test -s "${main}.pdf"
  )
}

case "${1:-all}" in
  1|2|3)
    build_paper "$1"
    ;;
  all)
    build_paper 1
    build_paper 2
    build_paper 3
    ;;
  *)
    echo "usage: $0 [1|2|3|all]" >&2
    exit 2
    ;;
esac
