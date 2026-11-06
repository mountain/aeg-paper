#!/bin/sh
# Build the formal manuscript.  Requires xelatex (for the Chinese reading
# guides) and texlive with ctex, tikz, tcolorbox, longtable, booktabs.
set -e
cd "$(dirname "$0")"
for i in 1 2 3; do
  xelatex -interaction=nonstopmode aeg-electrodynamics.tex > /dev/null
done
echo "built: $(pwd)/aeg-electrodynamics.pdf"
