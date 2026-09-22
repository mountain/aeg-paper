# Paper 0 Mathematical Status Register

**Status:** Authoritative register for Paper 0 only
**Version:** 1.0
**Date:** 2026-09-22
**Applies to:** `paper-0/aeg-paper-0.tex` and its `sections/` and `appendices/`
**Companion:** `05-mathematical-status.md` (which applies to Papers I--IV)

This register is created by
`00b-paper-0-geometric-foundation-amendment.md` §1.7.  It uses the nine status
labels of `00-authoritative-scope.md` §23 verbatim and inherits the
interpretation rules of `05-mathematical-status.md` §4.  Moved results keep the
status they held in Paper I; no moved result is promoted by the move.

Labels: `PROVED`; `PROVED WITH STATED HYPOTHESES`; `STANDARD CONSEQUENCE
REQUIRING AN IN-PAPER PROOF`; `COMPUTATIONALLY VERIFIED EXAMPLE`; `PARTIALLY
PROVED`; `STRUCTURAL PROPOSAL`; `CONJECTURE`; `OPEN PROBLEM`; `UNSUPPORTED AND
EXCLUDED`.

## 1. Expansion and syntax (Paper 0 §2)

| Node | Status | Note |
|---|---|---|
| unique internal order for pure combs (`prop:p0-combs-unique-order`) | `PROVED` | elementary; weaker than Paper I's classification |
| comb opposition (`prop:p0-comb-opposition`) | `PROVED` | combinatorial |
| affine/projective break (`cor:p0-affine-projective-break`) | `PROVED` | conditional on $c\ne0$ |
| distributive expansion identity (`prop:p0-distributive-operator-identity`) | `PROVED` | ring identity, proved in-paper |
| distributive charge transport (`ex:p0-distributive-charge-transport`) | `PROVED` | worked example; uses `prop:acs-evaluation` |
| expansion boundary for subtraction and division (`rem:p0-expansion-boundary`) | `PROVED` | identity plus the observation that $kc/z$ is not affine |

## 2. Arithmetic expression spaces and motion (Paper 0 §3)

| Node | Status | Note |
|---|---|---|
| regular AES definition (`def:regular-aes`) | `PROVED` | definition, moved from Paper I §5 |
| canonical arithmetic frame (`prop:canonical-arithmetic-frame`) | `PROVED` | moved from Paper I §5, proof included |
| invariant affine metric (`prop:invariant-affine-metric`) | `PROVED` | moved from Paper I §6 |
| basic hyperbolic AES (`thm:basic-hyperbolic-aes`), `K=-\lambda^2` | `PROVED` | moved from Paper I §6 |
| Laplace eigenfunction `\Delta a=2\lambda^2a` (`prop:laplace-eigenfunction`) | `PROVED` | moved from Paper I §6 |
| assignment-compatible moves (`prop:p0-grid-assignment-action`) | `PROVED` | existing Paper 0 result |
| Baumslag--Solitar-type relation (`eq:p0-bs-relation`) | `PROVED` | elementary; now cited to `BaumslagSolitar1962NonHopfian` |
| continuous affine flow (`thm:continuous-affine-flow`) | `PROVED` | moved from Paper I §5 |
| rectification `|\nabla r|=|\lambda|` (`eq:rectified-eikonal`) | `PROVED` | moved from Paper I §5 |
| infinitesimal order defect (`eq:infinitesimal-order-defect`) | `PROVED` | exact identity plus asymptotic form |
| model labels `E_0`, `E_1`, `E_k` (`conv:p0-model-labels`) | `STRUCTURAL PROPOSAL` | naming convention only; no classification by `k` |
| one-puncture disc model (`ex:p0-e1-model`) | `PROVED WITH STATED HYPOTHESES` | the verification is Paper I §5 `prop:isolated-zero-singular-model`; the metric extends, the assignment does not |

## 3. Dual reading and projective unification (Paper 0 §§4--6)

| Node | Status | Note |
|---|---|---|
| ripple pencil definition (`def:p0-ripple-pencil`) | `PROVED` | definition |
| line-to-circle transition (`thm:p0-ripple-pencil-formula`) | `PROVED` | existing Paper 0 result |
| covariant--contravariant duality (`prop:p0-path-ripple-duality`) | `PROVED` | definitional |
| finite and infinite geometric expansions (`prop:p0-finite-geometric-expansion`) | `PROVED WITH STATED HYPOTHESES` | infinite values only under stated convergence hypotheses |
| arithmetic fixed points (`prop:p0-reciprocal-fixed-points`) | `PROVED` | algebraic fixed point is not asserted attracting |
| one matrix, four readings (`thm:p0-four-matrix-readings`) | `PROVED` | |
| elementary projective generation (`thm:p0-pgl2-generation`) | `PROVED` | |
| the name `ripple geometry` | `STRUCTURAL PROPOSAL` | descriptive name for the dual reading; `subsec:p0-ripple-status` states the boundary |

## 4. Commutativization, tearing, contact (Paper 0 §§7--9)

| Node | Status | Note |
|---|---|---|
| affine cocycle formulas (`prop:affine-cocycle-formulas`) | `PROVED` | moved from Paper I §4 |
| relative affine defect (`def:relative-affine-defect`) | `PROVED` | moved from Paper I §4 |
| ACS definition and charge path (`def:acs`) | `PROVED` | moved from Paper I §8 |
| direct ACS evaluation (`prop:acs-evaluation`) | `PROVED` | moved from Paper I §8 |
| relative torsion (`def:relative-torsion`) | `PROVED` | moved from Paper I §8 |
| weighted torsion--Stokes theorem (`thm:torsion-stokes`) | `PROVED` | moved from Paper I §8 |
| tearing (`def:p0-tearing`) | `STRUCTURAL PROPOSAL` | the name for the two-history defect; the scalar defect is defined for scale-compatible pairs, and equals the weighted ACS area only under charge-compatibility (`thm:torsion-stokes`) |
| contact nondegeneracy (`prop:contact-form`) | `PROVED` | moved from Paper I §9 |
| contact curvature `[D_u,D_v]=\mu\lambda\partial_a` (`thm:contact-curvature`) | `PROVED` | moved from Paper I §9; retitled "Curvature of the specified horizontal connection", with a remark that `mu*lambda` is not a contact-isomorphism invariant and is not `K=-lambda^2` |
| the basic model is the Reeb quotient of the contact model (`prop:p0-contact-quotient`) | `PROVED` | added 2026-09-22; five exact relations with proofs, for the basic model only; proposed in the 2026-09-22 review and verified independently here |
| finite/infinitesimal synthesis (`prop:torsion-curvature-synthesis`) | `PROVED` | moved from Paper I §9 |

## 5. Beyond linear language (Paper 0 §10)

| Node | Status | Note |
|---|---|---|
| arithmetic generators do not close (`prop:p0-arithmetic-generators`) | `PROVED` | elementary computation; proof by `ad_A^n(P)`, revised 2026-09-22; the prose conclusion is narrowed to finite-dimensional Lie-group closure |
| observables of the charge endpoint cannot see tearing (`prop:p0-characters-cannot-see-tearing`) | `PROVED` | restated for arbitrary functions of the charge endpoint; explicitly not a statement about non-abelian linear representations |
| process-geometry vocabulary and lowering discipline | `STRUCTURAL PROPOSAL` | imported as a language; no theorem about AES is claimed |
| exact calibrations meeting `eq:p0-bs-relation` and the bracket law | `COMPUTATIONALLY VERIFIED EXAMPLE` | research-local calibrations of `Yuan2026ProcessGeometry`, carrying that repository's own maturity labels |

## 6. Holed spaces (Paper 0 §11)

| Node | Status | Note |
|---|---|---|
| punctured AES definition (`def:p0-punctured-aes`) | `PROVED` | definition; revised 2026-09-22 to give an ambient surface and a finite set first, so that nonempty puncture sets exist; finite-point specialization of Paper I's singular AES |
| tangent cone of the four limiting circles (`prop:p0-puncture-tangent-cone`) | `PROVED` | exact algebraic identity, verified in-paper; **no AES data are attached to the configuration**, and the origin is not asserted to be a puncture |
| six computed witnesses | `COMPUTATIONALLY VERIFIED EXAMPLE` | each with the model stated in-paper where the count depends on it; the register is non-authoritative |
| observer witness | `PROVED` (bound), register numbers **not reproduced** | the residual functions, their exact zero, and the halting bound `|theta-pi/2| < 5eps/8 + O(eps^2)` are proved; the register's round counts depend on an unfixed update step and are not quoted |
| the reading of the witnesses as an obstruction of AES | `UNSUPPORTED AND EXCLUDED` | listed in `subsec:p0-holed-nonclaims` as a non-claim |
| the identification of the $\mathbb Z_3$ monodromy with any $\mathbb Z_4$ twist | `UNSUPPORTED AND EXCLUDED` | recorded in the register as unproved; not reproduced here |
| attaching AES data to the four-circle configuration | `OPEN PROBLEM` | `op:p0-four-circle`; required before any puncture claim may be based on that configuration |
| comparison of tearing across a puncture | `OPEN PROBLEM` | `op:p0-canonical-punctures` |
| canonical choice of punctures | `OPEN PROBLEM` | `subsec:p0-holed-open`; OQ-082 |

## 7. Open programmes

`OPEN PROBLEM`:
intrinsic projective AES for ripple geometry; quotient-stable path/ripple
invariants; canonical choice of punctures; ripple structure at a puncture;
multi-wire semantics; general theory of infinite arithmetic expressions; a
positive non-linear description replacing the two obstructions of §10.
