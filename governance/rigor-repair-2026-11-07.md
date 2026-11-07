# Flat-limit and complexification rigor repair

**Status:** scoped repair and validation report, not a whole-series proof audit.
**Date:** 2026-11-07.
**Base:** `mountain/aeg-paper` main, `f1fe625967292254b3a014cedefc5a8e884dc827`.
The remote main ref was checked again during final validation and was unchanged.
At initial artifact delivery, no commit, push, pull request, or merge had been
performed. This is the local validation snapshot; subsequent publication and
remote check results are recorded by the pull request, not asserted here.

## Mathematical changes

1. **Paper 0, Section 3:** added `prop:p0-flat-limit`. For fixed `mu>0`, the
   global maps `(u,v) -> (u,exp(lambda v))` identify the positive-lambda models
   with metrics `exp(-2 lambda v) du^2/mu^2 + dv^2` on a common plane.
   Metric, assignment and canonical frame converge smoothly on compact sets
   to a complete flat regular AES. The proof handles all derivative orders;
   no uniform convergence on the entire noncompact plane is claimed.
2. **Paper 0, Section 12.6:** removed the incorrect claim that no rescaling
   can give the Euclidean plane. Added `prop:p0-complex-conic-rank`, proving
   rank preservation under R-to-C scalar extension and invertible congruence.
   Only the two nondegenerate real quadratic types become equivalent over C;
   degenerate forms stay separate. The Euclidean absolute includes line and
   circular-point data. Spherical compactification now explicitly requires
   genus zero and a chosen round representative, and does not produce a
   closed regular AES with nonzero additive intensity.
3. **Research note 51:** the full diagonal PGL2(C) metric action belongs on
   `(P1 x P1) minus diagonal`; the restricted affine model supports pullback
   identities only on common domains. A translation and a pole give exact
   counterexamples to global preservation of the restricted model. The
   square root is local or defined on the unramified double cover; a
   winding-number argument rules out a global square root on the base.
4. **Adjacent note 51 corrections:** distinguished the complexified frame
   rotation from the ambient complex structure, corrected the complex zero
   divisor, stated the connected-fiber argument for global descent, made
   trace/length sign choices explicit, and restricted RH/Schwarz boundary
   assertions to their actual trace and approach hypotheses. Added C2
   completeness and normalization arguments. General matrix and intrinsic
   complex-boundary RH remain proposals/open questions.

An independent, read-only mathematical review checked the new proofs and
note 51 repair. It caught and resolved the distinction between closed and
compact-with-boundary regular AESs, and a missing conjugate-boundary-trace
hypothesis in the RH correspondence. No blocking finding remained.

## Files and provenance

- Paper source: `paper-0/sections/03-aes-and-motion.tex`,
  `paper-0/sections/12-compactification.tex`.
- Research note and witness: `notes/analysis-and-calculus/51-complexified-model-and-rh.md`
  and `51-complexified-model-and-rh-witness.py`.
- New regression: `paper-0/scripts/verify-model-limits.py`; new optional CI
  workflow `.github/workflows/model-rigor.yml` uses SymPy 1.14.0.
- Status/navigation: `governance/05b-paper-0-status-register.md`,
  `paper-0/README.md`, `paper-0/formal/README.md`, `paper-0/formal/inventory.json`,
  `paper-0/formal/machine.lock.json`, and this report.
- Generated Paper 0 PDF: 105 pages. Paper I was rebuilt only for validation;
  its tracked PDF was restored to the original bytes.

No research material was moved or removed. The live formal inventory now has
22 sources and 105 theorem-like entries. Both new propositions are explicitly
`not-yet-formalized`. The baseline already failed two inventory-consistency
unit tests; a clean baseline replay reproduced those failures. Refreshing the
live inventory and its one lock digest repairs navigation drift without
changing archived manuscript snapshots, certificates, Lean proofs, contracts,
or execution receipts.

## Validation

Using Python 3.12.14, SymPy 1.14.0 and blake3 1.0.9:

| Check | Result |
|---|---|
| New model-limit/rank witness | 32/32, normal and `python -O`, identical output |
| Note 51 witness | 35/35, normal and `python -O`, identical output |
| Existing compactification checks | 139/139, normal and `python -O`, identical output |
| Formal regression unit tests | 18/18, normal and `python -O` |
| Python compilation | Both changed/new witness scripts passed |
| Whitespace/patch checks | `git diff --check` passed; source patch applied cleanly to the base snapshot |
| Paper 0 build | `./build.sh 0`, 105-page PDF produced |
| Paper I build | `./build.sh 1`, 61-page PDF produced |
| Final LaTeX logs | No undefined references, missing citations/assets, duplicate labels or undefined controls |
| PDF inspection | Changed proposition/table/remark pages 19, 80 and 81 rendered and visually checked |

The installed TeX distribution lacked generated format/font-map caches. The
build used temporary writable TeX caches assembled from the installed TeX
sources and font maps; no system files or repository build settings changed.
Paper 0 retains two pre-existing overfull boxes (6.42 and 11.13 pt) and six
existing hyperref math-bookmark warnings. The edited table's earlier 0.58 pt
overflow is removed; no new overflow remains. Paper I has existing layout
warnings in unchanged source and is not presented as a layout-clean artifact.

## Boundaries and next work

The finite/symbolic witnesses do not prove compact-set convergence, global
patching/topology, completeness, analytic boundary limits or general RH
solvability. The repaired text supplies scoped proofs or explicitly stated
standard results; none of this is a new Adva/Lean certificate. The external
native Adva/Lean execution suite, unrelated repository-wide workflows and
remote GitHub Actions had not been rerun at this local-delivery checkpoint.
The new CI workflow was supplied for the subsequent publication stage.

A useful next task is a separate formalization of the smooth-family and
branch/descent statements, or a dedicated analytic audit of note 50 and the
remaining proposed RH extensions. Those are not claimed complete here.
