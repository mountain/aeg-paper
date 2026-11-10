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
8. `aes/`

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
- [51 — The complexified basic model and Riemann–Hilbert boundary](analysis-and-calculus/51-complexified-model-and-rh.md):
  the C1 complexified hyperbolic model (PGL_2(C)-invariant metric, curvature
  $-\lambda^2$, real slice), the Riemann–Hilbert/Schwarz boundary theory
  (Poisson as a Cauchy jump, DtN as the Hilbert transform, the $C_0\cap L^1$
  theorem), and the C2 Hermitian companion (complete model with $a(z)=z$,
  positive curvature, total curvature $2\pi$, discrete zero locus).
  Companion witness: `analysis-and-calculus/51-complexified-model-and-rh-witness.py`.

## Order topology and interval vocabulary

- [52 — Scott/Lawson topologies and the compatibility boundary with Adva interval vocabulary](analysis-and-calculus/52-scott-lawson-adva-interval-boundary.md):
  separates the value-lattice Scott/lower/Lawson vocabulary from the interval
  domain's reverse-inclusion information order; records where constant
  generators `T_s, D_k, ¬` agree with endpoint interval operations, where
  term-level `+,-,*,/` lose sharpness/dependency, and why `ExactZero` is not a
  Scott open set. It also separates interval-Newton `RootExists` from
  `ExactZero`, and records the observed `contracted=true` but `delta_y ∌ 0`
  contradiction as `InvalidWitness`. Structural proposal with an explicit
  open-problem list; no claim status is promoted.

## Punctured AES flows and reduction

- [53 — Flows on punctured AES, three completions, and reduction to ODE](analysis-and-calculus/53-punctured-aes-flows-and-reduction.md):
  separates the punctured AES geometry from the extra flow data; records the
  three completions (topological/conformal, metric, arithmetic), the absence of
  canonical puncture holonomy, the optional `Mon_extra`, the Hamiltonian/
  Lagrangian joint reading as an added contact/Legendre structure, and a
  reduction datum `(π,τ,σ,U_reg)` for returning to an ODE. Root existence is
  routed through lift tube replay + Newton and then reduction; exact-zero stays
  in the value layer. Structural proposal with an explicit open-problem list.

## The elliptic AES programme

- [AES notes: the elliptic AES programme](aes/README.md): design notes for a
  genuine elliptic AES (positive curvature, compactification, analysis), using
  the Cayley–Klein real-form family as skeleton.
- [01 — Trichotomy audit and the Cayley–Klein skeleton](aes/01-trichotomy-audit-and-cayley-klein-skeleton.md):
  the five same-named trichotomies, the trace-versus-curvature distinction, and
  why the trace trichotomy collapses for positive curvature.
- [02 — The arithmetic side of the elliptic AES](aes/02-arithmetic-side-of-the-elliptic-aes.md):
  the three-layer syntax/value/realization split, the bounded spherical
  assignment, the critical/turning locus, and the range domain.
