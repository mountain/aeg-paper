# Paper I Mathematical Decisions and Closure Records

**Status:** Active Paper I decision record  
**Date:** 2026-08-06  
**Baseline:** `134e70a74ed010024afa7439bd3931402731423a`  
**Applies to:** the active `aeg-paper.tex` manuscript only

This file records the conservative choices required to turn the Paper I status
register into a coherent manuscript.  It does not change the scope of Papers II–IV.

## C-0001 — Chronological composition and projective action

- **Issues:** OQ-002, OQ-003.
- **History convention:** a history `γ=(g_1,…,g_n)` applies `g_1` first and `g_n`
  last, so `ν_x(γ)=g_n∘⋯∘g_1(x)`.
- **Concatenation:** `γδ` means first `γ`, then `δ`.
- **Matrix action:** a class of
  \(\begin{psmallmatrix}A&B\\C&D\end{psmallmatrix}\) acts on column homogeneous
  coordinates and sends \(z\) to \((Az+B)/(Cz+D)\).
- **Matrix order:** \(\rho(\gamma\delta)=\rho(\delta)\rho(\gamma)\).
- **Checks:** addition followed by scaling; the `C≠0` Möbius decomposition; the ACS
  elementary rectangle; the contact commutator rectangle.
- **Proof locations:** Appendix A and Sections 3, 4, 8, and 9.

## D-0001 — Regular arithmetic expression space

- **Issue:** OQ-001.
- **Canonical primitive data:** an oriented Riemannian surface \((M,g)\), a smooth
  assignment \(a\), and constants \(\mu\ne0\), \(\lambda\in\mathbb R\), satisfying
  \[
  |\nabla a|_g^2=\mu^2+\lambda^2a^2.
  \]
- **Derived data:** the orientation and eikonal identity determine a unique oriented
  orthonormal arithmetic frame \((X_u,X_v)\) with
  \(X_ua=\mu\) and \(X_va=\lambda a\).
- **Equivalence:** a surface supplied with such a frame satisfies the eikonal identity;
  the converse is proved by an explicit rotation of the normalized gradient frame.
- **Boundary convention:** all regular-zero conclusions refer to the interior unless a
  separate boundary hypothesis is stated.
- **Proof location:** Definition `def:regular-aes` and the frame-equivalence proposition
  in Section 5.

## P-0001 — Field scope of bilateral generation

- **Issue:** OQ-004.
- **Decision:** the generation theorem is stated over every field \(K\), including
  characteristic two.
- **Hypotheses:** elementary contexts entering `PGL_2(K)` are non-degenerate;
  \(AD-BC\ne0\); in the non-affine decomposition \(C\ne0\).
- **Reason:** the explicit formula with Weyl inversion remains valid when \(-1=1\);
  the sign is absorbed by the field arithmetic and the determinant remains nonzero.
- **Proof location:** Theorem `thm:bilateral-pgl2-generation` in Section 3 and the
  explicit check in Appendix A.

## D-0002 — Affine syntactic sector

- **Issue:** OQ-005.
- **Decision:** the *elementary affine sublanguage* consists of non-degenerate
  elementary one-hole contexts that individually fix \(\infty\).  Its projective image
  is the affine Borel subgroup because it contains all translations and nonzero
  scalings.
- **Qualification:** this syntactic language is not asserted to equal the full preimage
  \(\rho^{-1}(B_\infty)\); words containing inversions can simplify to affine
  operators.
- **Proof location:** the elementary-context table and Corollary
  `cor:affine-borel-sector` in Section 3.

## D-0003 — Primary meaning of arithmetic torsion

- **Issue:** OQ-007.
- **Primary definition:** for two scale-compatible positive add--scale histories,
  arithmetic torsion is their relative target-frame translation defect, independent
  of the initial value.
- **Derived cases:** elementary affine torsion is the two-step example; a
  charge-compatible pair admits the exact ACS boundary/area representation; closed
  commutator holonomy is the source-normalized relative translation; horizontal
  curvature is the common infinitesimal density.
- **Terminology warning:** none of these is the torsion tensor of an affine connection.
- **Proof locations:** `def:relative-torsion`, `thm:torsion-stokes`, and the synthesis
  proposition in Sections 8 and 9.

## C-0002 — ACS direct-path orientation and weight

- **Issue:** OQ-008.
- **Path coordinates:** \((A,M)\), with addition horizontal and log scaling vertical.
- **Evaluation convention:**
  \[
  \nu_x(\gamma)=e^{M_\gamma}
  \left(x+\int_{C_\gamma}e^{-M}\,dA\right).
  \]
- **Pair orientation:** for \(\tau(\gamma,\delta)=\nu_x(\gamma)-\nu_x(\delta)\), use
  the one-chain \(C_\gamma-C_\delta\).
- **Plane orientation:** \(dA\wedge dM\).
- **Weighted form:** if the common scale is \(M_*\),
  \(\eta_*=e^{M_*-M}dA\), so
  \(d\eta_*=e^{M_*-M}dA\wedge dM\).
- **Sign check:** addition by \(\mu h\) followed by scaling by \(e^{\lambda k}\), minus
  the reversed order, is \(\mu h(e^{\lambda k}-1)>0\) when all parameters are positive.
- **Proof location:** Section 8 and Appendix D.

## D-0004 — Compatibility levels for relative torsion

- **Issue:** OQ-009.
- **Domain:** both histories are words in the positive real translation and
  log-scaling generators used to define their ACS charge paths.
- **Scale-compatible:** \(M_\gamma=M_\delta\).  This is sufficient for the endpoint
  difference to be independent of the seed.
- **Charge-compatible:** \((A_\gamma,M_\gamma)=(A_\delta,M_\delta)\).  This is stronger
  and makes \(C_\gamma-C_\delta\) a closed ACS chain to which the weighted Stokes
  formula applies directly.
- **Decision:** the two conditions remain distinct and have separate propositions.

## D-0005 — Singular arithmetic expression space

- **Issue:** OQ-010.
- **Definition:** a singular AES has a closed nowhere-dense singular set \(S\); its
  nonempty dense regular locus \(M\setminus S\) is a regular AES; and every point of
  \(S\) is locally essential, meaning that the metric and assignment do not jointly
  extend there to a local regular AES.  Weaker extension or asymptotic behavior near
  \(S\) must be stated for each model.
- **Discipline:** the label “singular” does not validate an arbitrary failed example;
  regular-locus equations and local singular behavior must still be verified.
- **Proof/test location:** Definition `def:singular-aes` and the radial disc example in
  Section 7.

## P-0002 — Isolated-zero radial model

- **Issue:** OQ-011.
- **Decision:** on the Poincaré disc, the metric extends smoothly through the center,
  while
  \[
  a(r)=\frac{\mu}{\lambda}\frac{2r}{1-r^2}
  \]
  is continuous but not differentiable at \(r=0\) as a Cartesian function.
- **Classification:** if the center is included, it is an assignment singularity and a
  singular zero; if the center is deleted, the punctured regular model has no zero.
- **Proof location:** Section 7 and Appendix C.

## D-0006 — Model names

- **Issue:** OQ-012.
- **Decision:** Paper I uses descriptive names: *basic regular hyperbolic model* and
  *isolated-zero singular model*.  Historical `E_0/E_1` names are not used as
  canonical indices because no invariant indexing principle has been fixed.

### Model registry

| Formula | Domain | Zero set | Singular set | Historical name | Paper I name |
|---|---|---|---|---|---|
| \(a=-x/y\), \(g=y^{-2}(dx^2/\mu^2+dy^2/\lambda^2)\) | \(y>0\) | \(x=0\) | empty | often \(\mathfrak E_0\), earlier README also used \(\mathfrak E_1\) | basic regular hyperbolic model |
| \(a=(\mu/\lambda)2r/(1-r^2)\), Poincaré metric | unit disc | center only after continuous extension | \(\{0\}\) | often \(\mathfrak E_1\) | isolated-zero singular model |

## P-0003 — Geometric normalization closures

- **Issues:** OQ-013, OQ-014, OQ-015.
- **Invariant metric:** derived from the affine group law and a normalized
  left-invariant generator frame; no uniqueness beyond that normalization is claimed.
- **Curvature:** \(K=-\lambda^2\), by explicit reduction to a constant multiple of the
  standard upper-half-plane metric.
- **Laplacian:** with \(\Delta=\operatorname{div}\nabla\),
  \(\Delta_g a=2\lambda^2a\); no \(\mu\)-factor remains.
- **Proof locations:** Section 6 and Appendix C.

## P-0004 — Grid, zero-family, and notation closures

- **OQ-016:** arithmetic grid flows are proved assignment-compatible; they are not
  called isometries.  Pullback calculations record the failure in general.
- **OQ-017:** the optional Baumslag–Solitar relation is stated only for the explicit
  assignment-compatible maps and checked as a map identity.
- **OQ-018:** the zero theorem is stated for a boundaryless surface or interior zeros.
- **OQ-020:** spatial regularity of a family implies both a smooth total zero set and
  that its projection to the parameter interval is a submersion; the tangent-space
  correction is written explicitly.
- **OQ-021:** no uncertified multi-zero example is included in Paper I.
- **OQ-022:** local/global comparison is a layered synthesis proposition, not a claim
  that all finite quantities are identical.
- **OQ-023:** \(\mathbb H^2\) denotes the upper half-plane and
  \(\mathcal D=\ker\alpha\) the horizontal distribution.
- **OQ-024:** \(\lambda\) is a fixed intensity and \(M\) accumulated logarithmic scale.
- **OQ-025:** new material uses “horizontal covariant differential” and \(\delta_H\).

## Repository and release decisions

- **OQ-059:** mathematical restructuring remains at the root `aeg-paper.tex` path;
  large path renaming is deferred.
- **OQ-060:** one shared bibliography is retained during migration.
- **OQ-064:** the root README and manuscript explicitly distinguish the prior Zenodo
  DOI from the active restructured manuscript.
- **OQ-065:** the root build is stabilized first; multi-paper build selection is
  deferred until Papers II–IV have canonical entry points.

## Status-promotion rule for this task

A result previously marked `STANDARD CONSEQUENCE REQUIRING AN IN-PAPER PROOF` is
promoted only if its final statement and proof occur in the active manuscript and an
independent mathematical review records no blocking defect.  The companion closure
report lists those promotions after review; this decision file alone does not promote
a theorem.
