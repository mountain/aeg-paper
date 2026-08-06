#!/usr/bin/env bash
set -euo pipefail

root_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
paper_dir="${root_dir}/paper-1"
main="aeg-paper-1"

(
  cd "${paper_dir}"
  pdflatex -halt-on-error -file-line-error -interaction=nonstopmode "${main}.tex"
  bibtex "${main}"
  pdflatex -halt-on-error -file-line-error -interaction=nonstopmode "${main}.tex"
  pdflatex -halt-on-error -file-line-error -interaction=nonstopmode "${main}.tex"

  test -s "${main}.pdf"
)
