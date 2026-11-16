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

build_app() {
  local app_dir="${root_dir}/applications/pan-encke"
  local en="aeg-app-pan-encke"
  local zh="aeg-app-pan-encke-zh"
  local bibtex_cmd
  bibtex_cmd="$(resolve_bibtex)"

  if [[ ! -f "${app_dir}/${en}.tex" ]]; then
    echo "missing application source: ${app_dir}/${en}.tex" >&2
    return 1
  fi

  # English (pdflatex)
  (
    cd "${app_dir}"
    pdflatex -halt-on-error -file-line-error -interaction=nonstopmode "${en}.tex"
    "${bibtex_cmd}" "${en}"
    pdflatex -halt-on-error -file-line-error -interaction=nonstopmode "${en}.tex"
    pdflatex -halt-on-error -file-line-error -interaction=nonstopmode "${en}.tex"
    pdflatex -halt-on-error -file-line-error -interaction=nonstopmode "${en}.tex"
    test -s "${en}.pdf"
  )

  # Chinese (xelatex + ctex)
  (
    cd "${app_dir}"
    xelatex -halt-on-error -file-line-error -interaction=nonstopmode "${zh}.tex"
    "${bibtex_cmd}" "${zh}"
    xelatex -halt-on-error -file-line-error -interaction=nonstopmode "${zh}.tex"
    xelatex -halt-on-error -file-line-error -interaction=nonstopmode "${zh}.tex"
    xelatex -halt-on-error -file-line-error -interaction=nonstopmode "${zh}.tex"
    test -s "${zh}.pdf"
  )
}

case "${1:-all}" in
  0|1|2|3|4|5|6)
    build_paper "$1"
    ;;
  app)
    build_app
    ;;
  all)
    build_paper 0
    build_paper 1
    build_paper 2
    build_paper 3
    build_paper 4
    build_paper 5
    build_paper 6
    build_app
    ;;
  *)
    echo "usage: $0 [0|1|2|3|4|5|6|app|all]" >&2
    exit 2
    ;;
esac
