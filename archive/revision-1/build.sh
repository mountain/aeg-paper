#!/usr/bin/env bash
set -euo pipefail

export TEXINPUTS=".:..:"
export BIBINPUTS=".:..:"
export BSTINPUTS=".:..:"

pdflatex main
if grep -q '\\citation' main.aux; then
  bibtex main
fi
pdflatex main
pdflatex main
