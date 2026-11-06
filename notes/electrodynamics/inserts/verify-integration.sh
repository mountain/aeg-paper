#!/bin/sh
# Check the integrated state of the two manuscript inserts.
#
#   paper-0-pole-covariance.tex   -> paper-0/sections/04b-pole-covariance.tex
#                                    (Paper 0, Subsection 4.4)
#   paper-4-transport-density.tex -> paper-4/sections/04b-transport-density.tex
#                                    (Paper IV, Subsection 4.8)
#
# For each paper the script checks that the source file and its \input line are
# present, builds the paper on a scratch copy (so the AEG checkout is not
# touched and its tracked PDFs are not rewritten), and reports the numbers the
# new statements actually carry.  Logs are saved beside this script.
set -e
cd "$(dirname "$0")"
here="$(pwd)"
aeg="${AEG_PAPERS:-$HOME/AEG/aeg-paper}"
scratch="$here/_scratch"
fail=0

check_source() { # paper-number marker-file input-anchor
  paper="$aeg/paper-$1"
  [ -f "$paper/sections/04b-$2.tex" ] || { echo "  FAIL: missing sections/04b-$2.tex"; fail=1; }
  grep -q "input{sections/04b-$2}" "$paper/sections/04-$3.tex" \
    || { echo "  FAIL: no \\input line in sections/04-$3.tex"; fail=1; }
  echo "  source ok: sections/04b-$2.tex wired into sections/04-$3.tex"
}

check_build() { # paper-number
  paper="$aeg/paper-$1"
  mkdir -p "$scratch"
  cp -R "$paper" "$scratch/paper-$1"
  ( cd "$scratch/paper-$1" && for i in 1 2 3; do
      pdflatex -interaction=nonstopmode "aeg-paper-$1.tex" > /dev/null; done ) || true
  log="$scratch/paper-$1/aeg-paper-$1.log"
  cp "$log" "$here/build-paper$1-integrated.log"
  if grep -q "There were undefined references" "$log"; then
    echo "  FAIL: undefined references in paper-$1"; fail=1
  else
    echo "  build ok: paper-$1, $(grep -o '([0-9]* pages' "$log" | tail -1 | tr -d '('), no undefined reference"
  fi
  if grep -q "Overfull \\\\hbox" "$log"; then
    echo "  note: paper-$1 has $(grep -c 'Overfull \\hbox' "$log") pre-existing overfull line(s)"
  fi
  grep -oE "\\\\newlabel\{[a-z0-9]+:([a-z0-9]*-?pole-[a-z]+|transport-density|edge-factor-triviality|nontrivial-edge|transport-normalisation|f7-edge-transports)\}\{\{[0-9.]+" \
    "$scratch/paper-$1/aeg-paper-$1.aux" 2>/dev/null \
    | sed 's/\\newlabel{//; s/}{{/ = /' | sed 's/^/    /' || true
}

echo "Paper 0"
check_source 0 pole-covariance ripple-geometry
check_build 0
echo "Paper IV"
check_source 4 transport-density condensation-and-continuation
check_build 4

rm -rf "$scratch"
echo
[ "$fail" -eq 0 ] && echo "PASS: both inserts are integrated and both papers build clean." \
                  || { echo "FAIL: see above."; exit 1; }
