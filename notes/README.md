# Research notes

The notes are grouped by subject and ordered independently inside each subject
directory. Source filenames use:

```text
NN-descriptive-topic-slug.tex
```

`NN` is a two-digit reading/order code within that directory. It is not a
mathematical-status, authority, chronology, or paper-allocation code. Rendered PDFs
and local compilation companions use the same basename as their source. A local
`references.bib` remains unnumbered because it is a shared support file rather than a
note.

The subject directories are:

1. `analysis-and-calculus/`
2. `computation-and-resources/`
3. `foundations-and-geometry/`
4. `knots-and-loops/`
5. `projective-condensation/`
6. `thermodynamics-and-renormalization/`
7. `electrodynamics/`

`electrodynamics/` is an archived working directory rather than a numbered note:
it holds a rendered manuscript on a contact-geometric reading of classical
electrodynamics, the two subsections that were inserted into Papers 0 and IV, the
five Chinese source notes of that working dialogue, and a strand of Paper I
capping and interface-disk calculations.  Its `NN-` filename convention does not apply here;
its register of contents and its known staleness are recorded in
`electrodynamics/SNAPSHOT.md`.

These files remain historical or exploratory research material unless a governance
record explicitly assigns a stronger status. Filename order does not promote a note
to theorem authority.

## Finite-field differences and harmonic analysis

- [48 — Finite trigonometry over F7](analysis-and-calculus/48-finite-field-trigonometry.tex):
  conics, angle groups, ripple pencils, and finite-field Fourier analysis.
- [49 — Conic motions, arithmetic histories, and three finite calculi](analysis-and-calculus/49-conic-histories-and-finite-calculi.tex):
  an explicit elliptic history, ordinary/projective domains, and the Fourier/Jordan
  comparison of nonsplit, split, and unipotent motions.
- [Resources, build instructions, provenance, and mathematical status](analysis-and-calculus/finite-field-calculi/README.md).

These two notes were migrated from `mountain/math-notes` at `7ece143` on
2026-11-06. AEG is their maintenance home; incorporation into Paper I and an
elliptic AES definition remain research tasks.

## Complex and arbitrary-field extensions

- [50 — Paper II: complex and arbitrary-field extensions](analysis-and-calculus/50-complex-and-arbitrary-field-extension.md):
  a three-layer reading of Paper II (algebraic skeleton over any field, C1
  holomorphic complexification, C2 Hermitian complexification, the real layer),
  the arbitrary-field trichotomy, the bivaluation dictionary, and a roadmap.
  Design note; it changes no paper source and no mathematical-status register.
  Companion witness: `analysis-and-calculus/50-complex-arbitrary-field-witness.py`.
