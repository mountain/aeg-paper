# Paper IV Source Audit

**Audit date:** 2026-08-07  
**Repository baseline:** `264b7edeade754b706b575929fbbe3c8df72b5c3`  
**Current manuscript:** `paper-4/aeg-paper-4.tex` and its explicit inputs  
**Status:** provenance and migration record

## 1. Purpose and authority

This audit records which repository materials and external mathematical sources
were used to construct Paper IV, which results were rederived in the active
manuscript, and which formulations were rejected or retained only as motivation.
It does not replace the authoritative restructuring documents.

The authority order used was:

1. the explicit Paper IV writing task;
2. `README.md`, `restructure/AGENTS.md`, and the authoritative restructuring
   files `00` through `08`;
3. the canonical Papers I--III;
4. Paper IV working discussions under `restructure/discussions/`;
5. historical notes and archived material;
6. external primary mathematical literature.

A working note or historical analogy is not proof authority. A claim is
canonical only when its hypotheses, statement, and proof occur in the active
Paper IV source or are imported by an exact citation.

## 2. Repository sources reviewed

### Canonical interfaces

- `paper-1/aeg-paper-1.tex` and
  `paper-1/appendices/app-E-equality-neutrality.tex`: history, operator,
  endpoint, charge, and torsion equality levels.
- `paper-2/aeg-paper-2.tex`: bounded analytic and representation interfaces.
- `paper-3/aeg-paper-3.tex` and its active README/decision records: finite
  forgetting, monodromy, and the claim boundary between supplied registers and
  history-natural constructions.
- `README.md`: the four-paper architecture and Paper IV scope.
- `restructure/00-authoritative-scope.md`: the requirement that state, metric,
  encoding, cost, and machine model be explicit before complexity claims.
- `restructure/06-editorial-rules.md`: claim-first exposition and separation of
  proved results, proposals, conjectures, and open problems.

### Paper IV working sources

- `notes/bilateral_projective_condensation.tex`: bivaluation/projector formulas,
  quotient towers, dual transport, and projective-condensation motivation.
- `restructure/discussions/history-residual-cut-resource-geometry.md`: the
  history--residual--cut framework, Horner, butterfly, OBDD, checkpointing,
  matrix-chain, and proof-obligation inventory.
- `restructure/discussions/three-branch-arithmetic-tubes-and-complexity.md`:
  cross-paper scope, rejection of unsupported curvature/hardness implications,
  and the distinction among representation, time, and space.

The active manuscript rederives every promoted theorem. The discussion files
are provenance and design sources, not cited proof substitutes.

## 3. External sources

The bibliography uses primary or standard sources for:

- Shannon entropy;
- Nerode residual equivalence;
- Newman's confluence lemma;
- coarse group growth;
- OBDD representation theory;
- radix fast Fourier transforms;
- reversible computation and checkpointing.

The external literature is used as calibration and historical placement. The
projective quotient, continuation-side, residual, finite-field, Horner, and
finite-network statements are proved directly in Paper IV.

## 4. Migration map

| Source material | Active Paper IV treatment | Status |
|---|---|---|
| bilateral rank-one matrix formula | rewritten as the bivaluation--projector theorem with a transversality hypothesis | REDERIVED HERE |
| `G/H`, `G/B_±`, frame and projector hierarchy | rewritten with right-coset and chronology conventions fixed | REDERIVED HERE |
| point/dual-point affine law | retained in Appendix A with chart and sign conventions stated | REDERIVED HERE |
| “forgotten frame information” intuition | converted into left/right continuation descent theorems | PROVED WITH STATED FUTURES |
| HRC contextual residue | totalized for partial domains and completed by an equivariant minimal-state theorem | REDERIVED HERE |
| residual logarithm as space | restricted to fixed-width/prefix-free state selection; operational claims moved to live configurations | CORRECTED AND PROVED |
| summed residual lower bound | named capacity--time and gated by snapshot charging | CORRECTED AND PROVED |
| completed/down-set workspace | rejected generally; retained only under no-recompute last-use retention | PARTIAL RESULT WITH COUNTERBOUNDARY |
| Horner fixed-weight example | generalized to fixed histograms and characteristic zero | PROVED |
| butterfly coset observation | retained as a local `GL_2/PGL_2` lemma with scalar warning | PROVED LOCALLY |
| NTT calibration | made finite and exact over `F_257` | PROVED IN FIXED MODEL |
| OBDD order example | supplied with residual-function lower-bound proof | PROVED IN FIXED MODEL |
| matrix-chain/checkpoint examples | supplied with exact elementary cost counts | PROVED IN FIXED MODELS |
| endpoint-difference holonomy | rejected by telescoping potential and pure-gauge propositions | PROVED OBSTRUCTION |
| noncommutativity/hyperbolicity implies hardness | excluded | UNSUPPORTED AND REJECTED |
| one scalar unifies representation/time/space | replaced by a model-relative Pareto vector framework | STRUCTURAL FRAMEWORK |

## 5. Negative and bounded findings

The reviewed sources do not supply:

- a completed multi-wire AEG category;
- a non-flat projective connection with a nontrivial loop residue;
- a machine-independent theorem identifying quotient-fiber entropy with
  workspace or runtime;
- an AEG-native fast-transform family with a proved asymptotic advantage;
- an approximate residual or rate--distortion theory;
- a robustness theorem across machine models.

These are retained as open problems. The audit does not claim an exhaustive
search of unreachable Git objects, uncommitted private notes, or external
repositories not supplied to the task.

## 6. Reproducibility

The finite projector, finite-field quotient, right-descent, Horner, OBDD, NTT,
matrix-chain, checkpoint, and fiber inequalities are independently checked by
`paper-4/scripts/verify-paper4.py`, which uses only the Python standard library.
The script is supplementary verification; the proofs remain in the manuscript.
