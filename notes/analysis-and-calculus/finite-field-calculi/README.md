# Finite-field differences and harmonic analysis

This directory supports two research notes, maintained here after migration
from [mountain/math-notes](https://github.com/mountain/math-notes):

| Original path | Canonical AEG source | Resources |
| --- | --- | --- |
| `finite-trig/finite-trig.tex` | [48-finite-field-trigonometry.tex](../48-finite-field-trigonometry.tex) | [finite-trig/](finite-trig/README.md) |
| `conic-dynamics/conic-dynamics.tex` | [49-conic-histories-and-finite-calculi.tex](../49-conic-histories-and-finite-calculi.tex) | [conic-dynamics/](conic-dynamics/README.md) |

## Provenance and adaptation

- Source revision: `7ece14321b145fd7fa93e83342d432d355944b63` (2026-11-06).
- Destination baseline: AEG `1d8633ac6e9e5fedfcba58e8a25065cf4cd32090`.
- Imported the complete articles, all twelve figure sources and their PDF/PNG
  companions, both exact verification scripts, and the detailed resource READMEs.
  The original CC0 text is retained as [SOURCE-LICENSE-CC0.txt](SOURCE-LICENSE-CC0.txt).
- Adaptations: numbered article names, figure paths, mutual PDF links, portable
  AEG references, build paths, and migration metadata. Authors, citations,
  theorem labels, proofs, and mathematical hypotheses are preserved.
- The verifiers and figure sources are unchanged. Article PDFs are rebuilt
  under their numbered names. The original paths in math-notes retain only
  migration pointers; source history remains available at the pinned revision.
- These are canonical **research notes**, not additions to a paper manuscript
  or changes to an authoritative theorem status. The older checkout
  `/home/ubuntu/aeg-paper` is outside this migration.

## Mathematical status and AEG interface

The organizing sequence is a marked arithmetic history, its projective motion
`g`, pullback `T_g f = f composed with g`, the difference `Delta_g = T_g - I`,
and Fourier or Jordan analysis. Selecting a conic alone does not select a
difference: retain the affine chart, base point, one-step generator, coefficient
field, and the generator's arithmetic history.

| Material | Status retained on migration | Hypotheses / limits |
| --- | --- | --- |
| Finite trigonometry, angle and ripple geometry, Fourier identities in note 48 | proved with stated hypotheses within the note | The concrete circle is over F7; finite-field and complex characters have different coefficient fields. Finite geometry supplies no limiting real analysis. |
| Quotient-torus/norm-one comparison in note 49 | proved with stated hypotheses | Characteristic different from two, with -1 nonsquare. Projectivizing norm-one multiplication directly doubles the angle and reduces the eight-step action to order four. |
| Four-context history `(+2, reciprocal, times 2, +2)` and its ordinary domains | proved with stated hypotheses; computationally verified example | Over F7, `R(t)=(t+3)/(1-3t)` has an eight-cycle. `W^8` is projectively the identity with empty ordinary domain; the empty word has full ordinary domain. |
| Six-, seven-, and eight-cycle difference comparison | proved with stated hypotheses; finite examples computationally verified | On each moving orbit in characteristic 7, `im Delta = ker sum`. Orbit lengths 6 and 8 are invertible and allow unique zero-sum primitives; length 7 gives a nilpotent Jordan block and no shift-equivariant linear primitive choice. |
| Real projective Riccati flow and compactness obstruction | proved with stated hypotheses | The one-dimensional projective flow is not a two-dimensional AES. A smooth real assignment on a nonempty compact manifold without boundary cannot satisfy `|grad a|^2 = mu^2 + lambda^2 a^2` everywhere for real `mu != 0`. Finite computation does not prove these statements. |
| Addition of the history/domain example to Paper I | structural proposal | Requires separate manuscript review. Paper 0 owns the geometric foundation under the September 22 amendment. |
| General odd-q comparison; histories within one operator class; elliptic AES | open problem | A translation over Fq has order p, not necessarily q. An elliptic AES must specify changed assignment/domain/equation/regularity data. |

Here “elliptic” refers to nonsplit projective motion. Elliptic curves, PDE
ellipticity, and curvature sign are separate notions. No proof, hypothesis, or
claim status was strengthened by this migration. The exact checks supplement
the written proofs; they do not establish arbitrary-field generalizations.

## Build and verify

From the AEG repository root:

```bash
./notes/analysis-and-calculus/finite-field-calculi/build.sh
```

This runs both original Python verifiers, builds all figures, runs three
LaTeX passes for each note, checks references/citations/labels/assets and layout
warnings, and writes the two numbered PDFs beside their sources. Requirements:
Python 3 (standard library only), `pdflatex`, `rg`, and `pdftoppm`.
The root paper build does not include these standalone notes.

For checks without LaTeX:

```bash
python3 notes/analysis-and-calculus/finite-field-calculi/finite-trig/verify.py
python3 notes/analysis-and-calculus/finite-field-calculi/conic-dynamics/verify.py
```

For one article, run its resource subdirectory's `build.sh`.
Next: review the four-context history and its domain contrast as a candidate
Paper I example before extending the elliptic AES programme.
