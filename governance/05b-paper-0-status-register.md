# Paper 0 Mathematical Status Register

**Status:** Authoritative register for Paper 0 only
**Version:** 1.1
**Date:** 2026-09-22; amended 2026-09-29
**Applies to:** `paper-0/aeg-paper-0.tex` and its `sections/` and `appendices/`
**Companion:** `05-mathematical-status.md` (which applies to Papers I--IV)

**Amendment (2026-09-29).** An independently verified counterexample shows that
`thm:p0-punctures-are-critical` is **false as printed**: its proof's first step
constructs a metric satisfying the eikonal identity and treats it as an extension
of the given `g`, whereas condition (ii) of `def:p0-punctured-aes` requires
extending `g` itself. `cor:p0-puncture-count` inherits the gap, and the second
clause of `rem:p0-puncture-hypothesis` is refuted. The affected rows in section 6
are amended below; section 7 is amended accordingly. Evidence: the root review
`AEG-Paper-0-review-2026-09-29-thm-punctures-are-critical-v0.1.md` and the
retained record `notes/foundations-and-geometry/10`; ledger entry C-10 in
`governance/notes-reserve-audit.md`. **No paper source is edited by this
amendment**; the printed theorem therefore still carries the defective
hypothesis, and the amendment records that fact rather than repairing it. The
repairable form is stated in the note column below. `thm:p0-four-circle-model`,
`prop:p0-tearing-puncture-independent`, `prop:p0-surface-does-not-close` and
`prop:p0-no-puncture-holonomy` are not affected.

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
| unique internal order for pure combs (`prop:p0-combs-unique-order`) | `PROVED` | Current formal correspondence uses planar trees and an independently defined child-interleaving trace relation; pure-comb traces are exactly the chronological input labels. Still weaker than Paper I's classification. |
| comb opposition (`prop:p0-comb-opposition`) | `PROVED` | Syntax is related by mirror/slot exchange; values and domains by the opposite partial relation. Commutativity identifies interpreted operators, not planar trees. |
| affine/projective break (`cor:p0-affine-projective-break`) | `PROVED WITH STATED HYPOTHESES` (clarified 2026-10-20) | Affine self-maps allow zero multipliers; affine group membership requires a nonzero multiplier. Only nonzero-numerator reciprocal maps have the invertible projective continuation. All ordinary divisions keep their actual denominator guards. |
| distributive expansion identity (`prop:p0-distributive-operator-identity`) | `PROVED` (corrected 2026-10-20) | The operator identity is unchanged. Full operation-labelled words differ for all parameters; their scalar projections coincide exactly at `(0,0)` or `(1,1)`. OQ-090 is resolved by the amended source and separate Lean statements. See section 10. |
| distributive charge transport (`ex:p0-distributive-charge-transport`) | `PROVED` | worked example; uses `prop:acs-evaluation` |
| expansion boundary for subtraction and division (`rem:p0-expansion-boundary`) | `PROVED WITH STATED HYPOTHESES` (clarified 2026-10-20) | `kc/z` keeps the original `z!=0` domain even when `kc=0`; only `kc!=0` gives a non-affine invertible projective map. Zero multiplier/subtraction cases remain affine self-maps, with group claims restricted to nonzero multipliers. The subtraction expansion also has a Lean proof in the 2026-11-07 continuation. |
| evaluability at an input (`def:p0-evaluable-expression`) | `PROVED` | Definitional: an input belongs to the ordinary recursive domain, including every intermediate denominator guard. The 2026-11-07 Lean continuation connects this to functional tree semantics, a dependent value map, both comb folds, closed-input independence and exact effective evaluation under a supplied equality decision. |
| cancelled reciprocal and inherited domain (`ex:p0-cancelled-reciprocal-domain`) | `PROVED WITH STATED HYPOTHESES` | Over a field, `1/(1/z)` has domain `K minus {0}` and returns `z` there. The identity has the larger domain `K`; two projective reciprocals instead compose on `P^1(K)`. The ordinary exclusion is not asserted to be an AES singularity. These finite algebraic/domain statements, including the projective round trip in the existing point graph, have Lean proofs in the 2026-11-07 continuation. |
| effective rational evaluation (`subsec:p0-evaluation-effectivity`) | `PROVED WITH STATED HYPOTHESES` | Finite four-operation trees, valid exact rational data and unbounded integer arithmetic. The 2026-11-07 Lean continuation instantiates all field laws with standard `Rat` and proves structural evaluation sound, complete and terminating with a value or no ordinary evaluation. No claim about all quantified rational arithmetic, arbitrary real constants or bounded implementations. |
| Richardson qualification (`subsec:p0-evaluation-effectivity`) | `PROVED WITH STATED HYPOTHESES` | External result cited to Richardson (1968), introduction and §2: the specified rich function language, existence of negative values, and identity with zero after allowing absolute value. No arbitrary-field or closed-constant-language undecidability conclusion is imported. |
| connection to Adva's finite construction viewpoint | `STRUCTURAL PROPOSAL` | Methodological interpretation supported by the pinned Adva report; the author's retrospective motivation and its source history are recorded separately in `discussions/evaluable-expressions-and-effective-presentations.md`. Not a new equivalence theorem or a claim of complete semantic decidability. |

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
| translation length of a positive dilation (`prop:p0-dilation-length`) | `STANDARD CONSEQUENCE REQUIRING AN IN-PAPER PROOF` | added 2026-10-24; in-paper proof supplied (integrate `dt/t` along the invariant geodesic `iR_{>0}`); no external citation needed |
| length of an affine motion is its multiplicative charge up to sign (`prop:p0-length-multiplicative-charge`) | `PROVED` | added 2026-10-24; conjugation to `D_Phi` by the translation `z -> z - z*` plus `thm:p0-descent`(3). Holds for `Phi = 1` as the parabolic case with length 0 |
| length is not a homomorphism and not injective on histories (`prop:p0-length-losses`) | `PROVED` | added 2026-10-24; (1) kernel inclusion from `thm:p0-descent`(4), (2) restates that item, (3) non-additivity by the explicit pair `M_q M_{-q}` |
| scale-compatible relative defect changes no length (`prop:p0-relative-defect-length-zero`) | `PROVED` | added 2026-10-24; multiplier 1, trace 2, so parabolic of length 0, from `prop:relative-affine-defect-coordinates` plus `prop:p0-length-multiplicative-charge`. Recorded as the reason neither `xi_n` nor `(xi_gamma-xi_delta)/Phi` can be a Fenchel--Nielsen twist: a length-`ell` holonomy has trace `2cosh(ell/2) > 2`, and no rescaling changes a conjugacy type |
| trace classification and length of a projective motion (`prop:p0-projective-trichotomy`) | `STANDARD CONSEQUENCE REQUIRING AN IN-PAPER PROOF` | added 2026-10-24; in-paper proof supplied (eigenvalues `lambda, lambda^-1`, so the sign of `tau^2-4` decides hyperbolic / parabolic / elliptic; conjugation to `diag(e^{l/2},e^{-l/2})` gives `ell = 2 arccosh(|tau|/2)`; checked against `prop:p0-length-multiplicative-charge` on the affine slice). Narrows section 3.6's boundary item (1) from "any projective motion" to "a general field `K`" |
| two layers of the affine conjugacy classification (`prop:p0-affine-two-layers`) | `PROVED` | added 2026-10-24; `D_Phi T_c D_Phi^{-1} = T_(Phi c)` computed directly, so the translation layer's class carries no continuous invariant and is a torsor under the dilations, while a dilation's class is determined by its multiplier. Recorded as the reason the length-zero verdict is a layer switch rather than a defect |
| two coordinates of one history (`rem:p0-length-two-coordinates`) | `STRUCTURAL PROPOSAL` | added 2026-10-24; reads `(log Phi_n, xi_n)` of `prop:affine-cocycle-formulas` as the descending and non-descending sides. Adds no theorem; identifies no geometric coordinate with the additive side; makes no Fenchel--Nielsen claim |

## 3. Dual reading and projective unification (Paper 0 §§4--6)

| Node | Status | Note |
|---|---|---|
| ripple pencil definition (`def:p0-ripple-pencil`) | `PROVED` | definition |
| line-to-circle transition (`thm:p0-ripple-pencil-formula`) | `PROVED` | existing Paper 0 result |
| covariant--contravariant duality (`prop:p0-path-ripple-duality`) | `PROVED` | definitional |
| zero-pole Apollonius equation and circle/bisector cases (`eq:p0-apollonius-pencil` and surrounding prose) | `PROVED WITH STATED HYPOTHESES` | Added 2026-11-07: actual complex norm level, with nonzero `A,C`, nonzero determinant and the pole excluded. Proper circles require positive level and nonunit distance weight; the unit-weight case is the vertical metric bisector of distinct real foci. The zero level is a single real zero in the full complex domain and empty in the upper half-plane; negative levels are empty. These qualifications bound the source's circle wording explicitly. |
| the forward pole remark (`rem:p0-pole-forward`) | `PARTIALLY PROVED` (wording limitation recorded 2026-11-07) | The preceding lemma's per-step criterion is correct. A first exit from the affine sector does not force all later adjacent poles to differ: `J` followed by a translation has the same pole 0 and the same pencil. Read the different-pole premise only for a newly postcomposed non-affine step; the prospective quantitative transport is not certified here. Manuscript wording amendment remains separate. |
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
| the history group (`conv:p0-history-group`) | `STANDARD CONSEQUENCE REQUIRING AN IN-PAPER PROOF` | convention fixing the quotient: free product of the two additive step groups; added 2026-09-22 |
| charge endpoint and evaluation are homomorphisms (`prop:p0-history-homomorphisms`) | `PROVED` | added 2026-09-22 |
| the ACS endpoint is the abelianization of the history group (`prop:p0-acs-is-abelianization`) | `PROVED` | added 2026-09-22; uses the standard fact `(F*H)_ab = F_ab + H_ab` |
| only the multiplicative charge descends to the motion (`thm:p0-descent`) | `PROVED` | added 2026-09-22; explicit transport element `M_q A_p M_{-q} A_{-e^{-q}p}` in the kernel of the evaluation, with additive charge `p(1-e^{-q})`; answers the review's R5 request for a history monoid with verified descent |
| direct ACS evaluation (`prop:acs-evaluation`) | `PROVED` | moved from Paper I §8 |
| relative torsion (`def:relative-torsion`) | `PROVED` | moved from Paper I §8 |
| weighted torsion--Stokes theorem (`thm:torsion-stokes`) | `PROVED` | moved from Paper I §8 |
| tearing (`def:p0-tearing`) | `STRUCTURAL PROPOSAL` | the name for the two-history defect; the scalar defect is defined for scale-compatible pairs, and equals the weighted ACS area only under charge-compatibility (`thm:torsion-stokes`) |
| contact nondegeneracy (`prop:contact-form`) | `PROVED` | moved from Paper I §9 |
| contact curvature `[D_u,D_v]=\mu\lambda\partial_a` (`thm:contact-curvature`) | `PROVED` | moved from Paper I §9; retitled "Curvature of the specified horizontal connection", with a remark that `mu*lambda` is not a contact-isomorphism invariant and is not `K=-lambda^2` |
| the basic model is the Reeb quotient of the contact model (`prop:p0-contact-quotient`) | `PROVED` | added 2026-09-22; five exact relations with proofs, for the basic model only; proposed in the 2026-09-22 review and verified independently here |
| finite/infinitesimal synthesis (`prop:torsion-curvature-synthesis`) | `PROVED` | moved from Paper I §9 |
| the curvature form of the horizontal distribution (`prop:p0-curvature-form`) | `PROVED` | added 2026-09-22 (evening): the bracket defect defines a canonical 2-form on the distribution, determined by `(D, pi)` and independent of the normalization of `alpha`; its value on the `h`-orthonormal frame is `mu*lambda`, with the rescaling law `rho^{-2}` under `h -> rho^2 h` |
| the curvature scalar's invariance group (`rem:p0-curvature-invariance`) | `PROVED` (explanatory remark) | resolves OI-6: `mu*lambda` is not a contact invariant, but it is an invariant of the declared frame and horizontal metric, and on the AES side of the data it is the chart-free expression `da([X_u,X_v])` |

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
| the gradient never vanishes in a regular AES (`lem:p0-gradient-nonvanishing`) | `PROVED` | `|\nabla a|^2 = \mu^2+\lambda^2a^2 \ge \mu^2 > 0`; implies every level set is a smooth curve; Paper I's regular-zero theorem is the level-zero case |
| punctures are exactly the critical points of the assignment (`thm:p0-punctures-are-critical`) | **`UNSUPPORTED AND EXCLUDED` as printed** (amended 2026-09-29); the repaired form is `PROVED WITH STATED HYPOTHESES` | added 2026-09-22 (evening) as `PROVED`, hypothesis: the assignment extends smoothly to the ambient surface. **Refuted as printed**: a verified counterexample has a smoothly extending assignment, `S = {0}`, and `Crit(atilde) = emptyset`. The gap is in the proof's first step — the template metric `g~ = |d atilde|^2_{g_0} g_0 / (mu^2 + lambda^2 atilde^2)` satisfies the eikonal identity but is not an extension of the given `g`. The reverse inclusion `Crit(atilde) subseteq S` remains proved. **Repaired form:** the conclusion holds if in addition `g` is conformal, near each puncture, to a metric extending smoothly and non-degenerately; then the eikonal identity forces `g` to be the template metric. Awaiting a paper amendment; see C-10 |
| the hypothesis is active (`rem:p0-puncture-hypothesis`) | `PARTIALLY PROVED` (amended 2026-09-29) | the disc model of Paper I does not satisfy the hypothesis (its assignment is not `C^1` at the puncture), so canonicality there remains open — that half stands. The closing clause, "in the second kind the puncture set is canonical", is **refuted**: the counterexample is of that kind (assignment smooth, metric non-extendable) with `S = {0}` unforced, and the same model translates to any interior point. The distinction the remark draws between the two species remains correct and is what the repaired theorem needs |
| puncture count equals critical-point count (`cor:p0-puncture-count`) | **`UNSUPPORTED AND EXCLUDED`** (amended 2026-09-29) | inherits the gap above; it was derived "immediately" from the theorem. Both the equality of counts and the "iff" clause fail on the counterexample (one puncture, zero critical points, on a disc that carries a smooth function with no critical point) |
| the tearing does not see the puncture (`prop:p0-tearing-puncture-independent`) | `PROVED` | added 2026-09-22 (fourth revision): `tau` is a function of the two words, so puncturing, changing the model, or changing the realisation leaves it unchanged; resolves the first half of OI-2 |
| the surface never closes the comparison (`prop:p0-surface-does-not-close`) | `PROVED` | the two orderings of a rectangle end at points whose assignments differ by `mu*h*(e^{lambda k}-1) != 0`, so the two flow paths bound no region of `M`; the ACS comparison is therefore canonical in every AES, not a workaround for punctures |
| no canonical holonomy around a puncture (`prop:p0-no-puncture-holonomy`) | `PROVED` | the level-set foliation is integrable hence flat; a curved connection requires added data (the contact model, where `omega` is canonical relative to the charge projection); and in canonical-puncture models the assignment is single-valued, so there is no monodromy |
| the zero-set germ and the metric at the puncture (`prop:p0-puncture-local-picture`) | `PROVED` | a circle of radius below `rho` meets the zero locus in exactly eight points with sign changes; eight sectors, four positive and four negative (the cusps along the axes); `g` is conformal to the Euclidean metric with vanishing factor, so the conformal class extends although the metric does not |
| punctured AES definition (`def:p0-punctured-aes`) | `PROVED` | definition; revised 2026-09-22 to give an ambient surface and a finite set first, so that nonempty puncture sets exist; finite-point specialization of Paper I's singular AES |
| tangent cone of the four limiting circles (`prop:p0-puncture-tangent-cone`) | `PROVED` | exact algebraic identity, verified in-paper |
| an explicit punctured AES with the four-circle zero locus (`thm:p0-four-circle-model`) | `PROVED` | added 2026-09-22: the template metric forced by the eikonal identity, the exact critical set (so `\nabla P \neq 0` on a punctured disc of radius `< \rho`), the zero locus, non-extendability at the origin, and incompleteness with the puncture at finite distance; answers the review's R7 request for a construction. **Unaffected by the 2026-09-29 amendment**, but note why: here `d atilde(0) = 0`, so the defective branch of the theorem's proof is never entered and this model never tested it |
| six computed witnesses | `COMPUTATIONALLY VERIFIED EXAMPLE` | each with the model stated in-paper where the count depends on it; the register is non-authoritative |
| observer witness | `PROVED` (bound), register numbers **not reproduced** | the residual functions, their exact zero, and the halting bound `|theta-pi/2| < 5eps/8 + O(eps^2)` are proved; the register's round counts depend on an unfixed update step and are not quoted |
| the reading of the witnesses as an obstruction of AES | `UNSUPPORTED AND EXCLUDED` | listed in `subsec:p0-holed-nonclaims` as a non-claim |
| the identification of the $\mathbb Z_3$ monodromy with any $\mathbb Z_4$ twist | `UNSUPPORTED AND EXCLUDED` | recorded in the register as unproved; not reproduced here |
| generalizing the four-circle model to `k` punctures or to motion-generated assignments | `OPEN PROBLEM` | `op:p0-four-circle`; the `k`-puncture half was recast by `cor:p0-puncture-count` as a question about functions with `k` critical points, but that corollary is now excluded (see above), so the recasting is withdrawn and the question returns to its earlier form |
| comparison of tearing across a puncture in a model whose assignment does not extend | `OPEN PROBLEM` | settled for smoothly extending assignments by `prop:p0-tearing-puncture-independent`, `prop:p0-surface-does-not-close`, `prop:p0-no-puncture-holonomy`; the non-extending case is OQ-088 |
| canonical punctures when the assignment does **not** extend smoothly | `OPEN PROBLEM` | the disc model of Paper I is the open case (OQ-088). **Amended 2026-09-29:** the smoothly extending case is *not* settled either — see the theorem row in this table, refuted as printed. The dividing line that survives is not "assignment extends" but "the metric is conformal near each puncture to one that extends"; OQ-088's framing is amended accordingly |

## 7. Open programmes

`OPEN PROBLEM`:
intrinsic projective AES for ripple geometry; quotient-stable path/ripple
invariants; canonicality of punctures for non-extending assignments; ripple
structure at a puncture;
multi-wire semantics; general theory of infinite arithmetic expressions; a
positive non-linear description replacing the two obstructions of §10.

**Amended 2026-09-29.** Canonicality of punctures is now open in **both**
species, not only for non-extending assignments. The sufficient hypothesis under
which the original two-inclusion proof goes through is recorded in the
`thm:p0-punctures-are-critical` row above; whether it is also necessary, and what
plays the role of the critical set when the assignment does not extend, are both
open (OQ-082 amendment; OQ-088).

## 8. Finite-type compactification amendment (2026-10-09)

This current amendment supersedes the affected *active-manuscript* statuses in
section 6 without rewriting the dated September 29 evidence or review. The
original unrestricted critical-set statement remains refuted; the canonical
source now prints the explicitly restricted version below.

| Node | Current status | Active hypotheses and boundary |
|---|---|---|
| `thm:p0-punctures-are-critical` | `PROVED WITH STATED HYPOTHESES` | Assignment extends smoothly, and near each puncture the **given** metric is conformal to a background metric extending smoothly and positively across it. Eikonal then forces the template factor, so the constructed extension really agrees with the given metric. |
| `cor:p0-puncture-count` | `PROVED WITH STATED HYPOTHESES` | Equality of puncture/critical counts only in the preceding class; converse constructs a metric from an assignment with finite critical set. No unrestricted existential classification is claimed. |
| `rem:p0-puncture-hypothesis`, `rem:p0-multi-puncture` | `PROVED WITH STATED HYPOTHESES` | The anisotropic counterexample is included; without conformal background only Crit(a) ⊆ S follows. |
| `def:p0-finite-type-carrier`, `def:p0-collar-contract` | `STRUCTURAL PROPOSAL` | Definitions of declared carrier/end and full smooth collar data; no canonical seam choice. |
| `prop:p0-conformal-end-filling` | `PROVED WITH STATED HYPOTHESES` | Finite topological type plus punctured-disc conformal ends, and only conformal point filling. |
| `thm:p0-arbitrary-k-punctures` | `PROVED WITH STATED HYPOTHESES` | Every k≥1; k−1 distinct real critical points plus essential infinity, μ≠0, real λ; existence, not arbitrary-moduli classification. |
| `eq:p0-pants-counts` | `PROVED WITH STATED HYPOTHESES` | Connected oriented finite type with 2γ−2+k>0; standard decomposition existence cited; count proved by Euler characteristic and end incidence. |
| `prop:p0-aes-collar-descent` | `PROVED WITH STATED HYPOTHESES` | Full collar germs, inverse/cocycle laws, Hausdorff smooth quotient, consistent orientation and equal signed μ,λ. Frame and finite transverse-flow compatibility; no analytic extension at punctures. |
| `warn:p0-hyperbolic-auxiliary` | `PROVED WITH STATED HYPOTHESES` | Imported complete-splitting obstruction from Paper I, with connectedness, completeness, no boundary and single-valued assignment. |
| Three-cusp covering and degeneration paragraphs | `PROVED WITH STATED HYPOTHESES` | Power-map cover is a special conformal family; FN/plumbing describe auxiliary hyperbolic/conformal geometry with markings and local coordinate choices. No AES-compatible degeneration is asserted. |
| `prop:p0-k4-motion-residue` | `PROVED WITH STATED HYPOTHESES` | Local flows near (0,1) in explicit k4 model; exact scalar identity and nonzero mixed state displacement (−3/4,0). New analytic certificate, not a rerun of the unavailable original numerical suite. |
| `prop:p0-apollonian-gap-equivalence` | `PROVED WITH STATED HYPOTHESES` | Non-degenerate chosen triangular gaps, three distinct tangencies, matching cyclic marking; recursive circles by uniqueness. Four initial gaps still recurse ternarily. |
| `prop:p0-four-circle-deformation` | `PROVED` | Incidence obstruction and explicit circle family only; not an AES deformation. |
| `prop:p0-three-sheet-cover` | `PROVED WITH STATED HYPOTHESES` | Independent base sheet, explicit cut permutations, pulled-back complex structure; cone angle 6π pertains to the Euclidean pullback length metric. |
| Bolza and double-pants comparison | `PROVED WITH STATED HYPOTHESES` | Exact specified algebraic specialization and genus count; no conformal or process equivalence from genus alone. |
| New exact finite checks in `paper-0/scripts/verify-compactification.py` | `COMPUTATIONALLY VERIFIED EXAMPLE` | Regression evidence for the explicit formulas, not the proof of general theorems or the original 39-check archive. |
| Arbitrary conformal moduli, AES-compatible plumbing, faithful arithmetic circle surgery | `OPEN PROBLEM` | Existence of one model per count and auxiliary hyperbolic compatibility do not settle these. |

The old statement that producing *some* compactifiable multi-puncture example
is open is superseded by `thm:p0-arbitrary-k-punctures`. Prescribed puncture
positions, prescribed zero configurations, motion-generated assignments and
classification remain open. The original unrestricted “iff” corollary loses
its proof; the counterexample directly refutes the equality for a given AES,
not every possible existential reformulation on that ambient surface.

## 9. Formal derivation checkpoint (2026-10-20)

The original CC0 implementation in `paper-0/formal/` starts a separate
chapter-by-chapter formalization of the current manuscript. Its inventory is
navigation over theorem-like environments, not a replacement for this status
register. Five symbolic algebraic **components** have explicit proof
certificates for an Adva-written commutative-semiring equality checker and
separate Lean statements. The comb grammar has two additional Lean statements;
their correspondence with the manuscript remains explicit review work.
Geometry, analysis, projective domains, normalized inverse coordinates and
whole-chapter coverage are not promoted by this checkpoint.

The operator part of `prop:p0-distributive-operator-identity` is valid for all
field parameters. The printed claim that the chronological constant pairs
`(p,k)` and `(k,k*p)` coincide precisely at `p=k=1` fails at `p=k=0`, which
the proposition's unrestricted parameter declaration permits. If complete
marked words are intended instead, operation labels also survive: the two
operation sequences are different even at `p=k=1`. The manuscript and proof
are preserved pending the precise correction in OQ-090. Its whole-proposition
status is therefore `PARTIALLY PROVED`; the certified operator equation is
not weakened by this finding.

Authored by Codex (OpenAI). Formal checks and source mapping are separately
recorded; no independent human review or whole-paper correctness is asserted.

## 10. Chapter 2 definition/domain continuation (2026-10-20)

This successor supersedes section 9's pending marked-data correction, while
preserving that checkpoint and its archived verification bytes. OQ-090 is
resolved: the source now distinguishes full marked histories from their
chronological scalar projection and includes both zero and unit cases. The
zero case is admitted as arithmetic syntax, without treating its multiplier
as invertible. Group/continuation claims explicitly retain their nonzero
hypotheses, including the degenerate `c=0` reciprocal case.

`paper-0/formal/definition-map.json` binds the amended source to the new
`Chapter02Domains.lean` module. Syntax, child-before-parent schedules,
ordinary partial evaluation, domains of all eight one-hole sections,
invertibility of nonzero affine maps, and marked/scalar equalities are
separate definitions and conclusions. Homogeneous reciprocal coordinates
and infinity behavior are covered; a full formal quotient construction of
`PGL_2` is not claimed. Real exponential/ACS facts in the charge example
retain the manuscript/Chapter 8 proof dependency.

The separate `domain-checker.adva` executes bounded rational combs and their
actual division guards. Its finite regression is evidence of that program's
declared execution, not a universal theorem about all fields and not an
extension of the unchanged polynomial equality kernel. The successor
contract, mapping, theorem audit and evidence index state the exact coverage.

## 11. Evaluability and effective presentations (2026-10-20)

The new final subsection of §2 restores the December 2022 evaluable-expression
concept and the January 2023 foundational question, with pinned historical
citations and an explicit correction of the inference from decision difficulty
to inability to define expressions over the reals. Syntax, partial semantics,
effective evaluation and semantic decision problems remain separate. The
rational starting point is an effective presentation, not a claim that the
usual topology on the rational carrier is discrete.

The definition and reciprocal example are registered above. No existing
theorem is strengthened or moved, and no additional geometric singularity
claim is introduced. Historical sources remain unchanged. The longer
discussion and the author's retrospective connection to Adva are retained in
`discussions/evaluable-expressions-and-effective-presentations.md`.

The original formal source `02-expansion.tex`, proof programs and Lean modules
are unchanged. The live coverage inventory includes the added source and marks
its new definition/example `not-yet-formalized`. Archived execution records
continue to bind their own manuscript and inventory snapshots; this prose
addition does not extend the scope of their five Adva certificates or 71 Lean
statements. A current inventory is navigation, not a new executed proof record.

Validation of this editorial continuation: all 14 existing formal regression
tests pass; `./build.sh 0` produces the 95-page PDF and `./build.sh 1` produces
32 pages. Neither final log has undefined references, missing citations,
duplicate labels or missing assets. The added subsection on PDF pages 13--14
was visually checked and introduces no overfull box. Existing warnings remain:
Paper 0 §10 has one 11.13 pt overfull paragraph, Paper I has two overfull boxes,
and Paper 0 has hyperref math-in-bookmark warnings. Paper I's rebuilt PDF is
retained in the external engineering record; its tracked PDF is unchanged.
No material is moved to another paper or archive. A next formalization step
can connect the new evaluability definition and reciprocal example explicitly
to the existing guarded-evaluation theorems; no general real-language decision
procedure is claimed by this addition.

## 12. Alternating expressions and arithmetic perturbation (2026-10-20)

Appendix C restores the early alternating-expression presentation ahead of
its general affine calculations. The full arithmetic derivation is present in
the February 2023 draft; the May 2025 scale/RG note explicitly refers to its
perturbation formula. The source timeline and the author's retrospective
connection to ACS/RG are recorded in
`discussions/alternating-expressions-perturbation-acs-rg.md`.

| Node | Status | Hypotheses and boundary |
|---|---|---|
| `def:appendix-alternating-expression` | `PROVED` | Definition of a finite chronological slot-(1) scale-then-add word over a field; each multiplier is nonzero to retain the surrounding affine-group convention. Pairs remain distinct operation events. |
| `prop:appendix-alternating-arithmetic-perturbation` | `PROVED WITH STATED HYPOTHESES` | Finite distributive expansion and exact difference propagation over a field, with the same history for both inputs. The ratio additionally requires distinct initial values. An explicit arithmetic induction is included, with no limits or smallness assumptions. |
| identity padding to alternating form | `PROVED WITH STATED HYPOTHESES` | Only words of additions and nonzero scalings; padding retains the induced operator, not the literal tree or complete marked history. No unique normal form or conversion of arbitrary branching/reciprocal expressions is claimed. |
| `eq:appendix-alternating-acs-bridge` | `PROVED WITH STATED HYPOTHESES` | Positive real multipliers, chronological scale-then-add pairs and the existing ACS definition. Direct edge integration gives source-normalized translation; terminal scale restores the value. Initial-value gain and additive-event suffix gain are distinct. |
| scale normalization and the historical RG reading | `STRUCTURAL PROPOSAL` | The archived May 2025 note and the author's recollection establish the research motivation. No specific blocking/rescaling RG transformation, limiting theory, physical identification or complexity theorem is proved by the elementary identity. |

This addition makes the initial accumulator and nonzero difference-quotient
condition explicit, while leaving the original archives unchanged. The old
general prefix perturbation formula retains its label and now refers to the
elementary derivation instead of duplicating its proof. General affine cocycle
and ACS statements are not strengthened or moved. At this editorial checkpoint
the inventory marked the added definition/proposition `not-yet-formalized`;
section 13 records their subsequent formal continuation. Previous Adva and
Lean execution archives retain their original scope.

Validation: all 14 existing formal regression tests pass after the inventory
update. Both required builds pass: Paper 0 has 97 pages, Paper I has 32.
The final logs have no undefined references, missing citations, duplicate
labels or missing assets. Restored appendix pages 85 and 87 were visually
checked; no new overfull box appears. The existing layout/bookmark warnings
recorded in section 11 remain. Paper I's tracked PDF is preserved after its
separate build.

An exact rational check of the worked example gives initial-value gain 6,
additive-event suffix gains 3 and 1, and source-normalized translation 7/6;
the direct recurrence and normalized ACS reading agree. These checks support
the example, not a universal formal proof. No research material is moved or
deleted. A next formalization step can connect the finite recurrence induction
to the existing affine algebra infrastructure; a general RG construction
remains outside this appendix.

## 13. Appendix C finite-induction continuation (2026-10-20)

`paper-0/formal/AppendixC.lean` supplies 24 explicitly audited statements,
with the manuscript correspondence declared in `appendix-map.json`. The
current inventory marks the restored alternating-expression definition and
arithmetic perturbation proposition `component-map-supplied`. This navigation
label is not a claim that the entire appendix is formally proved.

The full finite scalar expansion and perturbation proposition is represented
by `expanded_evaluation`, `contribution_at`, `exact_difference`,
`prefix_difference`, `perturbation_ratio` and `guarded_ratio`. Contributions
are independently indexed by their strict suffix products. `evaluate_snoc`
identifies the chronological recurrence; `events_correspondence` and
`tree_correspondence` connect each two-event pair to the existing ordinary
word/tree evaluation. Nonzero multipliers and their nonzero accumulated
scale are recorded separately. Polynomial induction needs only the explicit
commutative-semiring laws; difference and quotient use the existing field-law
parameters. The quotient additionally requires distinct initial values;
`diagonal_ratio_undefined` proves that equal inputs do not admit this ordinary
division even though the field structure has a total inverse operation.

Nineteen of the new statements, including the primary expansion, perturbation
and ratio theorems, use no global axioms. The two product helpers and event
count use `propext`; two list/tree correspondences use `propext` and
`Quot.sound`. Exact name and axiom lists are checked rather than inferred from
successful compilation. One new Adva semiring certificate checks the symbolic
perturbation step, with changed-goal rejection and independent replay. It does
not introduce native universal induction.

The first combined invocation is retained as `Failed` in
`formal/evidence/appendix-c-attempt-1.json` and its complete archive. The exact
axiom map had omitted `propext` for `scale_append` and `scale_snoc`; reception
stopped at that mismatch after 63 native runs and the positive Lean module,
before the missing-guard control. `contract-appendix-c-v1.1.json` declares the
successor after correcting only those two expected entries, with unchanged
proof/program/goal/case bytes and resource bounds. The first attempt's
184.11 seconds are additional costs and are not relabelled as success.

The current execution receipt is recorded separately as
`formal/evidence/appendix-c-execution.json`. Identity padding, real
exponentials, ACS integration and the RG interpretation are not promoted by
this continuation. No existing mathematical statement is strengthened or
moved. A next step can formalize source normalization and its compatibility
with the discrete ACS weights before importing analytic integration.

The recorded successor is `Passed`: 63 native runs, 131 child commands,
49,581 independently received instruction transitions and all 24 new Lean
audits, alongside the unchanged 71 preceding statements. Omitting the ratio
hypothesis is rejected with the expected type mismatch. The successful run
took 182.03 seconds; all 63 native reports/receipts and the positive Appendix C
audit are byte-identical to the failed invocation, whose additional costs
remain separately recorded. Eighteen regression tests pass, including source,
trace and failure-preservation checks. The required Paper 0/Paper I builds pass
at 97/32 pages without undefined references, missing citations, duplicate
labels or missing assets. The previously recorded layout/bookmark warnings
remain, with no new overflow; the tracked Paper I PDF is preserved after its
build. No material is moved or deleted by this formal continuation.


## 14. Cuts and expression foundations (2026-10-21)

Appendix F (`app:p0-cuts-foundations`) is a background and research-direction
appendix requested for the next formal theory of arithmetic expressions.
It does not expand Paper 0 into a general convergence or complexity theory.

| Node | Status | Note |
|---|---|---|
| Bauer--Taylor cuts and observable predicates (`subsec:p0-taylor-cuts`) | `PROVED WITH STATED HYPOTHESES` | External background, cited to Bauer--Taylor (2009), Sections 2 and 6, and Taylor (2006), Sections 2 and 5--6. Inhabited, rounded, disjoint, located rational predicates describe reals; generalized cuts carry interval information. No Boolean comparison procedure is inferred. |
| Conway options, simplicity, and finite-tree boundary (`subsec:p0-conway-cuts`, `subsec:p0-cut-representation-boundaries`) | `PROVED WITH STATED HYPOTHESES` | External background from Conway (1976), Chapters 0--2, with Ehrlich (2011) for the larger field and hierarchy. Finite primitive option trees yield dyadics; finite names in an expanded signature need not have finite cut unfoldings. |
| Rational observations in different carriers (`subsec:p0-cut-representation-boundaries`) | `PROVED WITH STATED HYPOTHESES` | Elementary comparison supplied in prose: an embedded irrational real and that real plus a positive infinitesimal have the same strict rational comparisons. The irrationality hypothesis is essential; at a rational target, comparison with that rational distinguishes them. |
| Adva through precedent (`subsec:p0-cut-formal-programme`) | `COMPUTATIONALLY VERIFIED EXAMPLE` | Reports pinned research note 0075 and its declared finite scope. Relations may be partial or multivalued; the complete program slice remains. Does not import ASD, Conway value selection, or a stable native through operation. |
| Option-wise scaling versus value selection (`subsec:p0-cut-formal-programme`) | `PROVED WITH STATED HYPOTHESES` | The displayed finite counterexample is calculated in the appendix and traced to pinned Adva note 0021. It does not challenge Conway multiplication: scaling the options is a different operation. |
| Proposed formal expression programme (`subsec:p0-cut-formal-programme`) | `STRUCTURAL PROPOSAL` | Separate syntax and guards, exact denotation constructors, observations with dependencies and retained remainders, and distinct equality/refinement/compatibility judgments. Their general rules, soundness, effectiveness, and resource guarantees remain open. |

No existing result is strengthened, removed or relocated. The appendix's
background is not covered by the existing Adva/Lean certificates. Only the
current navigation inventory and its live source-lock digest are refreshed;
frozen statements, source maps, archived locks and execution receipts are
preserved. The Appendix C regression now distinguishes its archived inventory
from live navigation, while retaining all archived digest and proof-source
checks. Exposition and organization
for this addition are by Codex (OpenAI), at the author's request.

Validation: `./build.sh 0` and `./build.sh 1` produced PDFs of 100 and
32 pages. Both final logs contain no undefined references, missing citations,
duplicate labels or missing assets. Existing layout warnings remain in
Paper 0 section 10 and Paper I's older material, with existing Paper 0
hyperref math-bookmark warnings; Appendix F introduces no overflow. Eighteen
formal regression tests pass using the existing verification environment.
The initial system-Python invocation lacked `blake3`; the configured environment
supplied the pinned dependency. Its other finding was the historical/live
inventory comparison, corrected as described above without changing archived
bytes. The validation-only Paper I PDF is retained outside the repository;
its previously tracked artifact is preserved. The next task is to specify a
small guarded expression signature and separate denotation, observation and
through-compatibility judgments before attempting a general calculus.

## 15. Chapter 2 evaluability continuation (2026-11-07)

`paper-0/formal/Chapter02Evaluability.lean` supplies 36 audited statements for
the finite arithmetic content added in subsection
`subsec:p0-evaluation-effectivity`, with a separate source-bound
`evaluability-map.json`. The unchanged expansion source is additionally pinned
for prefix domains, condition pullbacks and the subtraction expansion. Old
proofs, native programs, statements, cases, contracts and all earlier execution
archives retain their bytes; this continuation does not rewrite history.

The semantic domain is existence of ordinary `TreeEval`. Tree evaluation is
functional and gives a dependent value map on that domain. Both combs agree
with the existing chronological partial folds; closed expressions have
input-independent evaluation. An arbitrary undefined prefix, or an undefined
child of any operation, cannot be made admissible by a later operation.
Inverse image of a condition through a concatenation equals the appropriately
nested inverse image; no inverse function is assumed. The previously missing
slot-(2) subtraction expansion is proved from the existing field-law
parameters, including zero scaling as an affine self-map.

The tree for `1/(1/z)` has exactly one hole and domain precisely `z!=0`, and
returns `z` there. Its partial graph differs from the identity at zero. The
existing projective reciprocal graph is functional, total in the sense of a
specified round trip, and two reciprocals return every point, including the
zero/infinity cases. This proves the example's finite algebraic and domain
clauses without constructing a full projective quotient or making ordinary
division by zero admissible.

The structurally recursive `compute` is sound and complete for arbitrary
finite trees when equality on the coefficient carrier is supplied as
decidable. `none` is equivalent to absence of an ordinary evaluation.
`rationalField` explicitly instantiates every `FieldData` law using the pinned
Lean standard `Rat` library, and the rational specialization terminates with
the correct value or arithmetic undefinedness. Valid rational constants have
nonzero representation denominators; parsing raw fractions is a separate
obligation. Kernel reductions cover branching expressions, an intermediate
zero denominator, zero numerators, undefinedness before multiplication by
zero, cancelled reciprocals and arithmetic beyond signed 64-bit range.
The semantic value's classical choice is separate from the executable
evaluator. Every theorem's exact global axiom set is disclosed, including
dependencies of standard rational lemmas; no new target axiom is introduced.

The missing-nonzero-input negative Lean module must reject for its expected
type mismatch after the positive module compiles. Three new bounded native
double-reciprocal cases retain the unchanged machine profile and rational
program, with positive/negative inputs and the excluded zero checked against
the independent `Fraction` oracle and both trace replay routes.
`contract-evaluability.json` declares the combined run before execution:
the 95 earlier Lean statements remain included, the native call capacity
increases from 64 to 72 for 66 expected executions, and all other limits are
unchanged. This capacity increase is declared new work, not a retry or a
conversion of bounded refusals into semantic results.

Live navigation is refreshed to 22 source files and 102 theorem-like
environments. The seven pre-existing Chapter 3 additions remain
`not-yet-formalized`; no claim-status decision is inferred from their inclusion.
The cancelled-reciprocal definition/example now have component maps. The
current totals are 12 component-mapped environments, one fragment-certified
environment and 89 not yet formalized, with no assertion that every mapped
environment is wholly covered. Archived inventories and their old generators
remain checked against their own snapshots. CI now invokes the successor and
restores push triggering; repository required-check settings are unchanged.

The real exponential/ACS charge example, the cited Richardson obstruction,
topology/cardinality background, complete `PGL_2` quotient, and general native
checker soundness are outside these new certificates. Their existing
mathematical or external-source status is neither strengthened nor weakened.
No manuscript statement or hypothesis is altered, and no material is moved.
The next geometric formalization task remains the definitions and explicit
prerequisites of Chapter 3.

Both required builds pass: Paper 0 has 103 pages and Paper I has 61 pages.
Final logs contain no undefined references, missing citations, duplicate
labels or missing assets. Existing overfull boxes remain (Paper 0: two,
maximum 11.13 pt; Paper I: eight, maximum 105.15 pt), along with existing
hyperref bookmark and Paper I underfull-box warnings. No TeX source was
changed; validation PDFs are retained externally and the tracked PDFs are
preserved.

The completed combined receipt is `formal/evidence/evaluability-execution.json`:
`Passed`, with 66 native runs, 139 child commands, 50,205 independently
received instruction transitions and all 131 Lean statement audits (95 old,
36 new). Both missing-hypothesis controls reject for the expected reasons.
The invocation took 200.89 seconds under the unchanged 300-second deadline.
Its separate archive retains complete source/manuscript snapshots, native
traces and replay receipts, Lean diagnostics and both build logs. All 22
regression tests pass, including the archive/source/trace bindings and
fail-closed checks for changes in either reviewed Chapter 2 source. These
counts include auxiliary lemmas and finite controls, not 131 newly covered
manuscript propositions.

## 16. Chapter 3 coordinate foundation (2026-11-07)

This is a component formalization of the current third chapter, not a
whole-chapter or smooth-Riemannian completion. The unchanged manuscript is
bound by `formal/chapter03-map.json` to the 61 audited statements of
`formal/Chapter03Coordinates.lean`. Existing manuscript statuses in section 2
are unchanged. The new algebraic components have the following status:

| Component | Status | Formal boundary |
| --- | --- | --- |
| canonical-frame coordinate construction, uniqueness and converse | `PROVED WITH STATED HYPOTHESES` | Oriented orthonormal coefficient plane, supplied `q!=0` and eikonal square; positivity proves any root nonzero. Existence/smoothness of a positive real root and gradient-adapted frame are not supplied. |
| basic model coordinate metric | `PROVED WITH STATED HYPOTHESES` | Symmetric bilinear positive definite form, signed orthonormal frame, orientation, affine coordinate invariance and scaling to standard metric. Field/order and nonzero-parameter/height hypotheses remain explicit. |
| candidate assignment covector and gradient | `PROVED WITH STATED HYPOTHESES` | Covector linearity, explicit metric-dual candidate, its uniqueness, nonzero value and coordinate eikonal identity. Identifying the displayed rational covector with an analytic differential remains open. |
| elementary coordinate motions | `PROVED WITH STATED HYPOTHESES` | Translation/scaling/reflection assignment actions, inverses and conjugation. Certified positive heights are preserved by positive scaling; zero scaling leaves the chart. No global action on an arbitrary punctured model is inferred. |
| finite affine point paths and prefixes | `PROVED WITH STATED HYPOTHESES` | Arbitrary nonzero-affine word lifts, prefix assignment values, unique affine coefficients, prefix recursion and actual ordinary expression-tree evaluation bridge. General nonzero multipliers use the punctured coordinate chart; upper-half-plane realizations need positive multipliers. |
| four-step path example | `COMPUTATIONALLY VERIFIED EXAMPLE` | Kernel reduction checks every displayed point/value prefix over exact rationals; universal path/tree results are checked separately. |
| two-layer conjugation and order defect | `PROVED WITH STATED HYPOTHESES` | Exact coordinate conjugation and polynomial order defect only. Full conjugacy/torsor classification, real exponentials, length and asymptotics retain their separate obligations. |

The algebraic interface uses Lean's standard `Lean.Grind.Field` and optional
linear-order/ordered-ring laws, with an explicit checked conversion to the
existing `FieldData` and equality with the preceding rational interpretation.
No AES conclusion is a field of the assumed structure. `grind` produces
kernel-checked proofs, with exact disclosed `propext`, `Classical.choice` and
`Quot.sound` dependencies. There is no target axiom or admitted proof.

The metric-dual proof closes a pointwise algebraic gap: the candidate gradient
is proved to pair with every vector as the candidate covector does, and any
other such gradient is proved equal to it. It does not assume the desired
eikonal norm as a model axiom. The analytic differential/Jacobian
identification, smooth metric/manifold construction and smooth-frame bridge
remain separate. Gaussian curvature/completeness, the Laplace eigenfunction,
ODE solutions, chain rule/rectification, hyperbolic translation length and
projective trace classification, and the punctured model are not promoted.

Historical `archive/revision-2/aristotle/RequestProject/AES.lean` is not imported.
Its older sign/frame conventions and `from_AES` identity corollaries are not a
proof of the present geometric definition. The current proof uses the signed
frame `(-mu*y,0),(0,-lambda*y)` and records its exact source correspondence.
The positive-height carrier is an algebraic chart, not a declared smooth
Riemannian surface. These distinctions preserve the manuscript's analytic
obligations instead of replacing them by assumed coordinate identities.

The tree bridge explicitly encodes each affine section as a multiplication
event followed by an addition event, including identity padding when needed.
It proves the value interpretation of that encoded tree, not literal equality
with an original four-operation tree or equality of their marked histories.
The four-step affine point example and the native four-operation scalar case
retain their respective finite words; equal values do not identify them.

Two negative Lean modules omit, respectively, nonzero chart height and frame
orientation. Reception requires their specific type mismatches after positive
compilation. A concrete rational reversed-orientation counterexample is also
checked. Three additional native runs check only the scalar four-step path
and the two conjugation orders, with fixed independent goals, a rational
oracle, native replay and the generic instruction receiver; no native
geometry or general checker soundness theorem is claimed.

`contract-chapter03.json` declares the complete successor before execution,
retaining the preceding 131 Lean statements and 66 native runs. All receiving
bounds are unchanged: 72 native calls, 160 child commands, a shared 300-second
deadline and the existing instruction, fuel and per-child limits. The expected
combined work is 69 native runs and 148 child commands, with 61 new Lean
audits. The original proofs, programs, goals, cases, runtime receivers,
contracts and success/failure archives remain unchanged. The predecessor's
navigation/receipt regression is updated only for separately pinned successor
navigation; the original test/generator/inventory snapshots retain their own
archived digest checks, and the successor tests bind the full current path.

Navigation still tracks 22 source files and 102 theorem-like environments:
20 have component maps, one has a fragment certificate and 81 are not yet
formalized. Eight Chapter 3 environments gain component maps with precise
coverage exclusions. The smooth regular-AES definition, Laplace theorem,
continuous-flow theorem, length/trichotomy results, structural two-coordinate
remark and punctured example remain unformalized. One conjugation component
does not promote the whole two-layer proposition. No manuscript claim or
hypothesis is changed, and no material is moved or deleted.

Both required manuscript builds pass at 103/61 pages. There are no undefined
references, missing citations, duplicate labels or missing assets. Existing
overfull boxes remain (Paper 0: two, maximum 11.13 pt; Paper I: eight, maximum
105.15 pt), with the existing bookmark/underfull warnings. TeX source and
tracked PDFs are unchanged; validation PDFs and full logs are retained.
CI invokes `chapter03_run.py` on the existing triggers; required-check settings
are unchanged. The next geometric task is the analytic differential and
Jacobian bridge needed to construct the smooth regular-AES model.

The completed receipt is `formal/evidence/chapter03-execution.json`: `Passed`,
with 69 native runs, 148 child commands, 51,137 independently received
instruction transitions and all 192 Lean audits (131 preceding, 61 new).
The new missing-height/orientation controls reject for exactly their expected
type mismatches; the earlier negative controls remain included. The complete
run took 177.71 seconds under the unchanged shared deadline. All 26 regression
tests pass, including exact current source/map/audit/native-trace bindings and
preservation of earlier success/failure archives. The separate execution
archive contains the captured 42 formal sources, 22 manuscript files, full
native reports/replay receipts, Lean diagnostics and both manuscript build
logs. Counts include supporting lemmas and finite controls, not 192 completed
manuscript propositions.

## 17. Chapter 3 real derivatives, smooth model and analytic laws (2026-11-07)

This successor discharges the candidate-differential/Jacobian obligations of
section 16 for the basic real global coordinate model and advances its
analytic laws. It does not mark the third chapter complete. The 66 new
statements are in `Chapter03Analysis.lean`, `Chapter03Flow.lean`,
`Chapter03Calculus.lean`, `Chapter03Rectification.lean` and
`Chapter03Dynamics.lean`; `formal/analysis-map.json` maps every statement to
the unchanged manuscript with exact disclosed global axiom sets.

| Component | Status | Hypotheses and boundary |
| --- | --- | --- |
| assignment differential, affine Jacobian and actual metric gradient | `PROVED WITH STATED HYPOTHESES` | Real Fréchet derivatives under the original nonzero-height guard; unique metric-dual gradient and actual signed frame derivatives. The former candidate formulas are independently derived from analytic differentiation. |
| smooth basic coordinate AES | `PROVED WITH STATED HYPOTHESES` | Open positive-height real domain, smooth assignment/continuous-bilinear tensor/gradient, positive definite metric and actual gradient/eikonal identity. The domain has a Mathlib smooth manifold structure of real dimension two. This constructs the model in one global chart; no arbitrary-manifold or boundary-chart equivalence and no new Riemannian distance/bundle instance is inferred. |
| Laplace eigenfunction | `PROVED WITH STATED HYPOTHESES` | Actual first/second partials, determinant and positive `sqrt(det g)` density, divergence-of-gradient coordinate operator and `Delta a=2 lambda^2 a`. Nonzero parameters/height and differentiability premises are explicit. Identification with an independent intrinsic bundle-Laplacian operator remains outside the certificate. |
| real square root and rectification | `PROVED WITH STATED HYPOTHESES` | The eikonal root is positive, nonzero and smooth for `mu!=0`. Actual `arsinh` differentiation gives the metric-dual rectified gradient with magnitude `|lambda|` on the nondegenerate basic model. The separate `lambda=0` unit rectifier `a/mu` is proved for a supplied `CoordinateRegularAES`. |
| signed-frame Lie bracket and curve propagation | `PROVED WITH STATED HYPOTHESES` | Actual derivatives give the bracket and assignment action `mu*lambda`; actual curve chain rule yields the angular equation, with the displayed angular tangent having unit metric norm. This is the real coordinate specialization. |
| constant-angle affine flow | `PROVED WITH STATED HYPOTHESES` | Global scalar ODE solution, zero/nonzero linear-coefficient branches, initial value, derivative, composition and uniqueness via an integrating factor. Globally defined coordinate curves with the required tangents follow it. General varying-angle existence/general-interval uniqueness and arbitrary-manifold flows are not silently imported. |

All geometric norms here use the constructed tensor. The positive real
intensities of the manuscript imply the explicit nonzero hypotheses in the
model construction and the positivity needed to identify its volume density.
The `lambda=0` fallback is separate from the hyperbolic metric formula, whose
`lambda` denominator must remain nonzero. Negative intensity/scale parameters
are not used to identify a positive-height model with the wrong component.

Mathlib `v4.24.0`, commit `f897ebcf72cd16f89ab4577d0c826cd14afaafc7`, is
pinned to the existing Lean 4.24.0. `formal/mathlib.lock.json` records its
manifest and dependency revisions, 7,600 source-file fingerprints and 3,175
compiled-library fingerprints. The compiler/standard library and cached
external mathematical library are declared trusted builds with integrity
checks; no authenticated compiler/cache provenance theorem is claimed. The
new proof audits admit only their exact disclosed `propext`,
`Classical.choice` and `Quot.sound` sets, with no target AEG axiom or admitted
proof. The model constructor proves its structure fields; it does not assume
the target differential or eigenfunction.

`contract-analysis.json` declares a separate analytic-only receiving profile
before execution: a 300-second shared deadline, 60-second child CPU,
120-second child wall time and 8 GiB Lean virtual-address limit. Engineering
measurements observed about 2.3 GiB resident memory, 18 seconds CPU and one
cold-import wall observation near 50 seconds. The preceding native/coordinate
profile keeps its unchanged 300-second deadline, bounds and 1/4 GiB child
split; both profiles must pass independently. Source fetching/cache preparation
is separate work and cannot serve as a verification fallback or fuel refill.

The analytic profile rebuilds the five unchanged core source modules and
exactly audits their 192 statements before checking the 66 new statements.
Four negative modules must reject for the specific missing-height,
wrong-Laplace-sign, missing-initial-value and missing-nonzero-intensity type
mismatches after positive compilation. Source/inventory/library fingerprints
are checked; no expected result is generated or rewritten by reception.
The original coordinate proofs, native programs/goals/cases and runtime
receivers remain unchanged. The historical navigation/test snapshots retain
their own archived digest bindings; current navigation has separate pins.

Navigation now has 23 component-mapped environments, one fragment-certified
environment and 78 not yet formalized, with the same 22 files and 102
theorem-like environments. The regular-AES definition, Laplace and flow
environments receive explicit component maps; none is promoted automatically
to a whole-environment formal proof. No manuscript claim, hypothesis or
mathematical status is strengthened, and no material is moved or deleted.

Gaussian curvature and completeness, hyperbolic translation length and trace
trichotomy, and punctured E1 remain formal obligations. Completeness must use
the Riemannian length metric, not the ambient/subspace Euclidean metric.
General manifold/boundary-chart and intrinsic bundle-operator equivalences
also retain their separate scope. These are the next geometric tasks.

The first analytic invocation is retained as `Failed` in
`formal/evidence/analysis-attempt-1.json` and its complete archive. It stopped
before any new proof module: the Lake environment-path query incorrectly used
the native 1 GiB address-space limit and emitted `INTERNAL PANIC: out of memory`.
Lake is itself a Lean process. The same query passed its engineering check
under the already declared 8 GiB Lean limit. The failed analytic invocation's
14.27 seconds and the independently completed native invocation's 196.51
seconds remain additional recorded work; neither is promoted to a completed
combined analytic verification. `contract-analysis-v1.1.json` declares a fresh
bounded successor with that receiving classification corrected. All proof,
library, goal and numerical receiving limits are unchanged. The regression
checks the exact source correction and retained failure. Both profiles are
rerun against the successor source snapshot.

The first completed combined receipt is `formal/evidence/analysis-execution-02.json`:
`Passed`. The native profile records 69 runs, 148 child commands and 51,137
independently received instruction transitions. The analytic profile records
16 child commands, the 192 unchanged source-import audits and all 66 new
analytic audits, for 258 distinct audited statements overall. Four analytic
negative controls reject for exactly their expected diagnostics. The profiles
took 255.02/186.44 seconds, each under its own 300-second deadline. All 31
regression tests pass, including the source/library/audit/native-trace/archive
bindings and exact failure-preserving receiving correction. All 69 native
reports are byte-identical across attempts; the first attempt's additional
costs remain recorded separately.

The complete successor archive retains 59 formal source files, 22 manuscript
files, both profile reports, all native traces/replay receipts, Lean audits,
negative diagnostics and both build logs. Library source and compiled-cache
fingerprints are retained instead of copying the external library into the
paper repository. Required builds produce 103/61-page PDFs with no undefined
references, missing citations/assets or duplicate labels. Existing overfull
boxes remain (Paper 0: two, maximum 11.13 pt; Paper I: eight, maximum 105.15 pt),
with the existing bookmark/underfull warnings. TeX source and tracked PDFs are
unchanged. CI now has separate native and `real-analysis` jobs; repository
required-check settings are unchanged.

The first remote analytic job at `4387911` failed before proof reception:
the preparation script created a fresh Git checkout without `origin`, and
the official Mathlib cache tool requires that remote to identify its cache
repository. `formal/evidence/analysis-ci-preparation-01.json` and the complete
job log preserve the failure; the separate symbolic/native job passed. The
preparation correction registers the same pinned repository as `origin`
before fetching its exact detached revision. Proofs, library pins, goals,
verification contracts and numerical bounds remain unchanged. The preceding
local successful receipt and its archive remain under
`formal/evidence/analysis-execution-02.json`; the current receipt binds a
fresh source snapshot including the preparation correction.

The current `formal/evidence/analysis-execution.json` and
`analysis-run-03.tar.gz` receive both fresh bounded invocations: the native
profile passes in 232.16 seconds, and the analytic profile in 143.57 seconds,
each within its unchanged 300-second deadline. All 69 native reports are
byte-identical to the preceding success; the analytic profile again audits
192 imported and 66 new statements, with all four negative controls rejecting
as required. All 31 regressions pass against the new full source/archive
bindings. Clean-checkout preparation matches all 7,600 source and 3,175
compiled-module fingerprints without changing the library lock. Both
manuscript builds again pass at 103/61 pages, with the same layout warnings;
tracked PDFs and TeX sources remain unchanged.

## 18. Deferred Chapter 3 obligations and easier Chapter 4 continuation (2026-11-07)

The user requested that difficult remaining Chapter 3 formal prerequisites be
recorded while easier Chapter 4 results advance first. The source-bound work
register is `formal/chapter03-obligations.json`. It records six known groups:
curvature, completeness for the correct Riemannian length metric, hyperbolic
length/trace, punctured E1, intrinsic/boundary/bundle interfaces and general
flows beyond constant coefficients. Each has source labels, a concrete missing
prerequisite and a resumption condition. Deferral does not change the existing
manuscript mathematical statuses or mean that those theorems are unprovable.

`formal/Chapter04Ripples.lean` and `formal/Chapter04Poles.lean` introduce 57
audited statements mapped in `formal/chapter04-map.json` to the unchanged
Chapter 4 and its nested pole-covariance source. There are 315 distinct audited
statements in the combined development; supporting lemmas are included in that
count. No complete-Chapter-4 status is assigned.

| Component | Status | Hypotheses and boundary |
| --- | --- | --- |
| complex Möbius imaginary part and upper-plane preservation | `PROVED WITH STATED HYPOTHESES` | Actual complex division with real coefficients. Positive determinant and positive input height imply a nonzero denominator and positive image height; ordinary partial arithmetic is not silently totalized. |
| horizontal-line / completed-square circle pullbacks | `PROVED WITH STATED HYPOTHESES` | Positive determinant, positive level and positive input height; the circle case additionally requires a nonzero lower-left entry. Positive radius, unique real-axis contact and circle height bounds are explicit. These are coordinate equations; intrinsic horocycle and differential tangency identifications remain separate. |
| nested circles and the inversion example | `PROVED WITH STATED HYPOTHESES` | Nesting is inclusion of the enclosed tangent disks as the level decreases. Distinct circle boundaries are disjoint level sets, not subsets of each other. The map `J=-1/z`, determinant, radius and circle equation are actual complex-coordinate results. |
| point/pullback duality | `PROVED` | Exact inverse-image membership and contravariant composition for arbitrary maps, with chronological order stated. |
| pole covariance and history rigidity | `PROVED WITH STATED HYPOTHESES` | Bijections of a pointed carrier; poles are actual inverse images of its infinity point. Per-step constancy, all-prefix rigidity and first exit follow without target axioms. A terminal pole alone does not detect all factors. The PGL representation and its matrix-to-bijection/affine-stabilizer identification are not yet supplied. |
| homogeneous real matrix pole column | `PROVED WITH STATED HYPOTHESES` | Nonzero determinant implies a nonzero `(-D,C)` column and, for `C!=0`, a finite denominator root with nonvanishing numerator. This is exact matrix algebra, not a completed projective-line quotient construction. |
| forward-remark limitation | `PARTIALLY PROVED` as printed | Actual posttranslation preserves determinant, finite pole and the entire complex ripple pencil. `J` then `T_s` disproves the reading that every later step changes poles after the first non-affine step. The correct individual-step criterion is retained; the prospective quantitative transport discussion is not certified. |

The previous Chapter 3 result is a real global-coordinate AES certificate; the
complex coordinate used here is the continuation chart specified by
`rem:p0-ripple-normalization`. No unproved isometry between all chart/metric
presentations is used. General PGL/ideal-boundary identification, absolute-value
Apollonius circles/perpendicular bisectors, intrinsic chart independence and
puncture-persistent ripple structures remain outside this continuation.

The existing Mathlib source/cache lock is unchanged: 7,600 source files and
3,175 compiled modules. The 57 new exact global axiom sets use only their
disclosed subsets of `propext`, `Classical.choice` and `Quot.sound`; there are no
target AEG axioms or admitted proofs. The original proofs, programs, goals,
contracts and runtime receivers retain their bytes. Current navigation and its
historical receipt regression have separately pinned successors; historical
archives and inventories remain bound to their original execution snapshots.

Live navigation now has 30 component-mapped environments, one fragment-certified
and 71 not yet formalized, within the same 22 manuscript sources and 102
theorem-like environments. A component map attached to the forward remark
records the scope limitation, not a proof of its unrestricted wording. The
corresponding status row in section 3 records that limitation explicitly.
No source text is silently rewritten and no research material is moved or lost.

`formal/contract-chapter04.json` declares eight child commands, two positive
modules, all 57 exact audits and four rejecting controls for determinant,
circle guards, affine-step hypothesis and composition order. Its numerical
bounds equal the existing analytic profile, including its separate 300-second
deadline and 8 GiB Lean virtual-address limit. The unchanged native and Chapter
3 analytic contracts remain separately required; fetching or another profile
cannot refill a proof run's budget. CI invokes the new profile separately after
Chapter 3 real analysis and uploads its evidence separately.

`formal/evidence/chapter04-execution.json` and its complete archive receive
all three profiles as `Passed`: native 174.33 seconds, analytic 136.43 seconds
and Chapter 4 58.91 seconds, each inside its own unchanged 300-second deadline.
The 69 native reports remain byte-identical to the preceding success. There
are 148 native child commands and 51,137 independently received instruction
transitions, 16 analytic child commands (192 core plus 66 analytic audits),
and eight Chapter 4 commands (57 exact audits and four expected specific
rejections). Import rechecks are not counted as new statements. All 35
regressions pass against the completed source/report/archive bindings; the
pre-receipt log retains its 34 passes and the then-absent receipt test rather
than relabelling that preparatory check as a completed verification.

The archive retains 70 formal source files plus the source lock, 22 manuscript
files, workflow, three reports, all native traces/replay receipts, Lean audits,
negative diagnostics and both build logs. Both builds pass at 103/61 pages
with no unresolved references/citations, duplicate labels or missing assets.
The existing overfull boxes (2/8, maximum 11.13/105.15 pt) and bookmark/underfull
warnings remain; tracked PDFs and TeX sources are unchanged. The next easier
step is the zero-pole Apollonius equations; full PGL and intrinsic geometric
identifications retain their separate prerequisites.

## 19. Apollonius norm levels, Euclidean circles and bisectors (2026-11-07)

`formal/Chapter04Apollonius.lean` advances the numbered equation
`eq:p0-apollonius-pencil` and its surrounding zero-pole prose with 39 new
audited statements. `formal/apollonius-map.json` pins their correspondence to
the unchanged Chapter 4 source. Its import is the unchanged 36-statement ripple
module, rebuilt and audited separately; import audits are not counted as new.
The combined development has 354 distinct audited statements, including
supporting lemmas. Chapter 4 is not marked complete.

| Component | Status | Hypotheses and boundary |
| --- | --- | --- |
| actual complex modulus factorization | `PROVED WITH STATED HYPOTHESES` | Nonzero `A,C` give numerator/denominator factors at real zero `q=-B/A` and pole `p=-D/C`. For input different from the pole, the norm level equals the weighted-distance equation with `k=r*abs(C/A)`. This uses actual complex norms, not a substituted polynomial observable. |
| entire guarded complex locus | `PROVED WITH STATED HYPOTHESES` | Nonzero determinant implies distinct foci and excludes the pole from the weighted locus. It identifies the full guarded norm-level set with that locus. The manuscript's positive determinant implies the nonzero assumption; positive height automatically excludes the real pole. |
| nonunit-weight circle | `PROVED WITH STATED HYPOTHESES` | Nonnegative `k` permits reversible squaring, and `k!=1` allows completing the square. The locus equals an actual Euclidean complex `Metric.sphere`, with derived center `(q-k^2*p)/(1-k^2)` and radius `abs(k)*abs(q-p)/abs(1-k^2)`. Positive `k` and distinct foci give positive radius and an upper-half-plane witness. |
| unit-weight bisector | `PROVED WITH STATED HYPOTHESES` | For distinct real foci, actual distance equality is exactly the vertical line `re z=(q+p)/2`. No full PGL representation or intrinsic hyperbolic-distance identification is used. |
| degenerate/negative parameters | `PROVED WITH STATED HYPOTHESES` | Zero level is the real zero singleton, empty in the upper half-plane. Negative levels are empty; negative weighted loci need distinct foci for this conclusion. Unit weight with equal foci gives the whole plane. Proper-circle wording requires positive level. |
| active guard witnesses | `PROVED WITH STATED HYPOTHESES` | Total complex division assigns zero at the pole, whereas the distinct-focus weighted locus excludes it. Negative unit weight is empty while unit weight is nonempty, although their squares agree. These are positive counterexamples to dropping the pole/sign/distinctness conditions. |

Circle and bisector identities refer to the full guarded complex plane. Their
upper-half-plane readings are intersections with the positive-height domain,
not an assertion that an entire Euclidean circle lies in the upper half-plane.
They use the continuation chart specified in the existing normalization remark.
The source's zero-level wording limitation is recorded explicitly rather than
silently certifying a nondegenerate circle there. No manuscript text, hypothesis
or ordinary arithmetic-domain rule is rewritten, and no material is moved.

Because the anchor is an equation and prose, live inventory now records one
separate `equation_components` entry with all 39 statements. The environment
counts remain 30 component-mapped, one fragment-certified and 71 not yet
formalized, among the same 102 environments and 22 manuscript sources. No
new theorem environment or whole-environment formal status is invented.

All exact new global axiom sets disclose only their actual subsets of
`propext`, `Classical.choice` and `Quot.sound`, without target AEG axioms or
admitted proofs. The same 7,600 source and 3,175 compiled-module Mathlib
fingerprints are reused unchanged, including the already pinned complex norm
module. Compiler/standard-library and cached-library trusted-build boundaries
are unchanged. Preceding proof, goal, program, runtime-receiver and contract
bytes remain exact; only navigation and its historical receipt test have
separately pinned successors. Historical execution archives are preserved.

`formal/contract-apollonius.json` declares an independent 300-second profile
with unchanged numerical Chapter 4 bounds: eight child commands, 36 import
audits, 39 new audits and four specific rejecting controls for missing pole,
nonnegative-weight, nonunit-weight and distinct-focus guards. All three
predecessor profiles remain independently required under their original
contracts. CI runs the additional profile separately and retains its own
artifact; profiles cannot refill one another's deadlines.

`formal/evidence/apollonius-execution.json` and its full archive retain all
four completed `Passed` profiles: native 174.35 seconds, Chapter 3 analysis
131.33 seconds, original Chapter 4 52.99 seconds and Apollonius 73.61 seconds,
each inside its own unchanged 300-second deadline. The original profiles
retain their exact counts (69 native runs, 148 commands, 51,137 independently
received instruction transitions; 192 core/66 analytic audits in 16 commands;
57 original Chapter 4 audits and four rejections in eight commands). The new
profile has 36 exact source-import audits, 39 new audits and four expected
specific rejections in eight commands. Import rechecks are not counted twice.
All 69 native reports are byte-identical to the preceding success.

The completed archive binds 79 formal sources plus their lock, 22 manuscript
sources, workflow, all four reports, native traces/replay receipts, Lean audits,
negative diagnostics and both build logs. All 39 regression tests pass against
the completed source/report/archive bindings, following 38 preparatory passes
and the then-absent receipt test, whose original diagnostic remains archived.
Both builds pass at 103/61 pages with no unresolved references/citations,
duplicate labels or missing assets. Existing overfull boxes (2/8, maximum
11.13/105.15 pt) and bookmark/underfull warnings remain; manuscript text and
tracked PDFs are unchanged. The next prerequisite is a concrete projective-line
action and its bridge to the already proved pointed-bijection pole laws.

## 20. Homogeneous projective action and concrete matrix pole bridge (2026-11-07)

The prerequisite left by sections 18--19 is discharged in a concrete algebraic
model. `formal/ProjectiveLine.lean`, `Chapter04ProjectiveBridge.lean` and
`Chapter04ComplexProjective.lean` add 70 exactly audited statements, bringing
the combined distinct count to 424 including supporting lemmas. Their map,
`formal/projective-map.json`, pins the current Section 6, the ripple source
and its nested pole subsection. No complete-chapter or external PGL API
certificate is inferred from these component maps.

| Component | Status | Hypotheses and boundary |
| --- | --- | --- |
| projective-line homogeneous quotient and chart | `PROVED WITH STATED HYPOTHESES` | Over any field, nonzero pairs modulo collinearity are equivalent to the explicit finite/infinity chart. Quotient equality is exactly multiplication by a nonzero scalar. This is an algebraic quotient, with no topology or smooth structure asserted. |
| actual nondegenerate matrix bijections | `PROVED WITH STATED HYPOTHESES` | Nonzero determinant preserves nonzero vectors; the adjugate yields both inverse laws after projection. The constructed `Equiv.Perm` supplies bijectivity instead of assuming the target action law. Quotient representatives transform by the actual linear matrix product. |
| finite/infinite point action and fixed points | `PROVED WITH STATED HYPOTHESES` | The finite denominator-zero branch maps to infinity; the image of infinity has its separate formula. The pole is uniquely `-D/C` for nonzero `C`, infinity exactly for `C=0`, and finite fixed points satisfy the displayed quadratic. Nonzero scalar multiples have equal actions. |
| concrete covariance and chronological prefix rigidity | `PROVED WITH STATED HYPOTHESES` | Matrix multiplication has the chronological action order. The existing abstract bijection lemmas give matrix-pole covariance, per-step constancy, all-prefix rigidity and first exit, with the affine hypothesis identified as the actual lower-left coefficient `C=0`. Every section matrix remains nondegenerate. |
| elementary matrix/action factorizations | `PROVED WITH STATED HYPOTHESES` | Translations, nonzero dilations and inversion act at finite points and infinity as specified. Affine and non-affine cases have their two-/four-factor forms up to explicit nonzero matrix scalars, and as equal total projective actions. Operational generation is certified; the external PGL quotient-group isomorphism and its faithfulness are separate obligations. |
| real/complex continuation chart and ripple bridge | `PROVED WITH STATED HYPOTHESES` | The real-to-complex point embedding commutes with the matrix action. A nonzero denominator identifies the finite complex action with the existing actual Möbius formula; positive determinant preserves the upper chart. Ripple membership is its actual output-condition pullback. Ordinary arithmetic domains remain distinct from projective continuation. |

The first two modules require only a field; no positivity, characteristic-zero
or real-order assumption is hidden in their algebraic statements. The last
module specializes real coefficients to the previously fixed complex chart.
Nonzero determinant, nonzero scalar and chronological-order hypotheses are
active: zero scaling changes the action, and a concrete singular-matrix
example breaks the unguarded composition law. Equality of projective actions
does not identify arithmetic histories, their markings or ordinary domains.

Two existing Section 6 environments now receive component maps, for 32 mapped
environments, one fragment-certified and 69 not yet formalized among the same
102 environments. Four equation anchors have separate maps across the same
22 manuscript sources. Source text and mathematical hypotheses are preserved;
no research material is moved. The previously recorded forward-pole wording
limitation is not erased by constructing the concrete bridge.

Exact new global axiom sets disclose only their actual subsets of `propext`,
`Classical.choice` and `Quot.sound`, with no target AEG axiom or admitted proof.
The same Mathlib/Lean source and cached-library fingerprints are reused without
change. Preceding proof, program, goal, runtime-receiver and receiving-contract
bytes retain their exact bindings. Navigation and its historical receipt test
have separately pinned successors; old execution archives remain preserved.

`formal/contract-projective.json` declares a separate 300-second receiving
profile with the unchanged numerical analytic bounds, including 8 GiB Lean
virtual address space. Eleven commands rebuild 57 unchanged import audits,
check 70 new audits and reject four controls for missing determinant/scalar/
affine guards or reversed pole order. All four predecessor profiles remain
independently required, with no budget refill across profiles. The new profile
has its own CI job and artifact. External PGL/Projectivization group API
identification, scalar-quotient faithfulness, abstract affine-group isomorphism,
and topological/intrinsic geometric interfaces remain separate obligations.

`formal/evidence/projective-execution.json` and its full archive receive all
five profiles as `Passed`: native 172.45 seconds, Chapter 3 analysis 128.75,
original Chapter 4 51.85, Apollonius 69.21 and projective 80.76 seconds. Each
is inside its own unchanged 300-second deadline. Predecessor counts remain
exact: 69 native runs, 148 child commands and 51,137 independently received
instruction transitions; 192 core/66 analytic audits in 16 commands; 57 original
Chapter 4 audits and four rejections in eight commands; 36 import/39 Apollonius
audits and four rejections in eight commands. The new profile has 57 import
audits, 70 new audits and four specific rejections in eleven commands. Import
rechecks are not counted as new statements. All 69 native reports are
byte-identical to the preceding success.

The archive binds 90 formal sources plus their lock, 22 manuscript sources,
workflow, five reports, native traces/replay receipts, Lean audits, negative
diagnostics and both build logs. All 43 regressions pass against the completed
bindings; the preparatory log retains its 42 passes and then-absent receipt
test rather than relabelling that stage as complete. Both builds pass at
103/61 pages with no unresolved references/citations, duplicate labels or
missing assets. Existing overfull boxes (2/8, maximum 11.13/105.15 pt) and
bookmark/underfull warnings remain; manuscript text and tracked PDFs are
unchanged. The next algebraic step is scalar-quotient faithfulness and the
external PGL/affine-group interfaces; the known Chapter 3 geometric obligations
remain in their separate work register.
