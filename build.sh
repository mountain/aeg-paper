#!/usr/bin/env bash
set -euo pipefail

main="aeg-paper"

pdflatex -halt-on-error -file-line-error -interaction=nonstopmode "${main}.tex"
bibtex "${main}"
pdflatex -halt-on-error -file-line-error -interaction=nonstopmode "${main}.tex"
pdflatex -halt-on-error -file-line-error -interaction=nonstopmode "${main}.tex"

test -s "${main}.pdf"
