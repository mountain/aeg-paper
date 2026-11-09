# Paper III intensity revision audit

**Date:** 2026-11-09. **Status:** repository revision under review, not a preprint release.

**Base repository:** `mountain/aeg-paper`.
**Verified main commit:** `db06fd057513f94f8da5bdcaf3122b244ab235d6`.
**Scope:** Paper III Sections 9.1 and 9.5, their governance records, and focused
regressions. This audit is subordinate to the repository scope and claim register.

## Mathematical outcome

1. **P3-L11 is restricted to the data actually fixed.** Fixed assignment gives a
   product zero incidence. Fixed metric only gives the same carrier if one also
   fixes the rectified signed coordinate. On the Euclidean plane,
   `a=(mu/lambda)sinh(lambda(x-b(mu,lambda)))` satisfies the eikonal identity
   while its zero line moves with an arbitrary smooth `b`. The unit-rescaling
   identity remains valid; frame directions are unchanged, while the vectors
   scale by `s^{-1}`.
2. **P3-L12 no longer identifies induced and ambient distances.** The zero-curve
   pullback tensor is independent of lambda. Ambient paths need not remain in
   the zero set. On the product cylinder, antipodal zero points have ambient
   distance tending to zero although their intrinsic distance remains `pi/mu`.
3. **The corrected compact limit is a point.** For compact connected smooth M
   with boundary and dA nowhere zero, the conformal metrics have diameter tending
   to zero. The proof uses finite nets with nonzero interior centers, transverse
   interior paths, and dominated convergence. It does not assume globally
   available gradient trajectories or assert a general quantitative rate.
4. **The distance formula has the correct direction.** The rectified assignment
   has unit gradient, giving a universal lower bound. Equality holds when its
   normalized gradient path reaches zero inside the domain. A disk example
   shows strictness even when the zero curve meets the boundary transversely.
5. **Area is controlled by both one-sided densities.** If the coarea density
   satisfies `I(c)=I_+ + O(c)` and `I(c)=I_- + O(|c|)` near zero, the leading
   coefficient is `pi(I_++I_-)/(2 mu lambda)`. The old coefficient is recovered
   for two matching sides. For `[0,1] x S^1`, `A=t`, `mu=1`, area is exactly
   `2 pi arctan(lambda)/lambda`, with leading term `pi^2/lambda`, not twice that.
6. **The assignment does not descend with the metric.** Its oscillation remains
   positive, so no constant on the GH singleton uniformly approximates A.
   Restricting A to its zero set is a different operation.

The moving-line, cylinder-shortcut, disk-access and one-sided-area examples are
retained in the main paper, rather than only in an external errata note.

## Assumptions made explicit

- Compactness and connectedness for the qualitative point-collapse theorem.
- Positive fixed mu; lambda tends to positive infinity.
- Smooth zero-curve portions for the induced tensor, without claiming a global
  stratification of arbitrary boundary zero sets.
- Gradient trajectories staying inside M for the exact distance upper estimate.
- Independent one-sided Lipschitz coarea-density assumptions for the area rate.
- Compactness is not replaced by bounded range. Removing critical points in an
  ambient family does not preserve the compact theorem automatically.

## Files changed

- `paper-3/sections/04-parameter-discriminants.tex`: corrected statements,
  proofs, boundary conditions and counterexamples; semantic labels preserved.
- `paper-3/scripts/verify-intensity-collapse.py`: 21 symbolic/geometric witnesses.
- `.github/workflows/paper3-intensity.yml`: focused witness and Paper III build gate.
- `paper-3/README.md`: corrected scope and test instructions.
- `governance/05-mathematical-status.md`: mark S-0010 historical and add S-0011.
- `governance/03-theorem-dependency-graph.md`: correct implications and exclusions.
- `governance/decisions-paper-III.md`: D3-28 records the revision boundary.
- `governance/discussions/aeg-intensity-plane-and-tube-collapse.md`: prominent
  supersession warning; the old discussion is preserved as historical evidence.
- This audit record.

No material was moved to another paper or deleted from the historical record.
Paper 0 is not edited. No dependent theorem was found to use P3-L11 or P3-L12.

## Validation

- All 34 materialized baseline text files were verified against their canonical
  Git blob SHA values at the fixed base commit.
- `python paper-3/scripts/verify-intensity-collapse.py`: PASS, 21 checks.
- Optimized-Python replay: PASS, byte-identical output. Checks do not depend on
  Python's removable `assert` statements.
- Existing `paper-3/computations/ll-igusa-twin/verify-explicit-twin.py`: PASS.
- Independent AI mathematical cross-check: no blocking issue found; the
  transverse-path and assignment-oscillation wording was tightened afterward.
  This is not independent human review or author acceptance.
- `bash build.sh 3`: PASS. The build environment's initially unconfigured TeX
  format and font maps were generated only in temporary writable directories;
  no source dependency or system installation was changed.
- Full manuscript PDF produced and revised pages visually checked. Detailed final
  PDF: 86 pages, 877703 bytes, SHA-256
  `ec693ee5fd5e5360720202a5d3b39d96091cacecfc2bdc6e8fa9cde1718f97fc`.
  Final LaTeX and BibTeX logs have no important warnings, undefined references
  or citations, duplicate labels, missing characters, or overfull/underfull boxes.
  Revised pages 57--63 were visually checked without layout issues.
- `git diff --check`: PASS. New workflow YAML parses; remote Actions execution
  is tracked in the pull request separately from these local results.

The finite tests guard explicit examples and identities. They do not substitute
for the in-paper general compactness and coarea proofs. Other papers and the
repository-wide CI suite were not rebuilt.

## Unresolved boundaries and next review

No general collapse rate is claimed. Noncompact families, rates under additional
boundary geometry, and decorated metric limits require separate analysis. The
second basic-model metric family remains distinct and has no new GH assertion.

Repository publication and merge were subsequently authorized by the author.
The revision follows the repository pull-request rules; this authorization is
not an independent mathematical review or formal PR approval. Exact remote
checks and merge status are recorded by GitHub, separately from this local audit.
No preprint release or deployment is claimed.
