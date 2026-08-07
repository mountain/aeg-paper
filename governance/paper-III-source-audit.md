# Paper III Source Audit

**Audit date:** 2026-08-06

**Repository HEAD audited:** 24c1df0dd1feb38b691a50a6c6dc7a6aa613248a

**Historical population audited:** 249 commits reachable from all refs in the local
checkout

**Current manuscript:** paper-3/aeg-paper-3.tex and its explicit section and
appendix inputs

**Document status:** provenance audit and migration control record; it does not
replace the authoritative scope or mathematical-status files

## 1. Purpose and authority

This audit identifies the mathematical and historical sources relevant to
Arithmetic Expression Geometry III: Singular Zero Geometry and Tubes.  It records
what can be imported, what must be rederived, what has been superseded or rejected,
and what was not found.

The authority order used in this audit is:

1. AGENTS.md and the explicit task;
2. governance/00-authoritative-scope.md through
   governance/08-open-questions.md;
3. the canonical Paper I and Paper II manuscripts;
4. the current Paper III manuscript, for claims proved there;
5. working discussions under governance/discussions/;
6. legacy sections, notes, knot calculations, miscellaneous files, archived
   manuscripts, and deleted historical files recovered from Git.

A working discussion, historical note, picture, or computation is not proof
authority.  A claim is canonical in Paper III only when its hypotheses, statement,
and proof occur in the active manuscript or are imported from Papers I or II by an
explicit citation.

The status REDERIVED HERE has a precise meaning in this document: the current
Paper III manuscript gives a new definition, construction, computation, or proof
from stated data.  The result may have been motivated by historical material, but
the historical material is not used as proof authority.

## 2. Audit method and negative historical finding

The audit covered the current contents and Git history of:

- paper-1/, paper-2/, paper-3/, and legacy sections/;
- notes/, notes/knots-and-loops/, images/sources/, images/, and archive/;
- governance/04-current-to-target-map.md,
  governance/05-mathematical-status.md,
  governance/08-open-questions.md, and both Paper III working discussions;
- deleted tracked material discoverable in the reachable Git history.

The history audit enumerated all 249 commits returned by git rev-list --all in the
local checkout and searched their trees for spelling and TeX variants of
multi-zero, multiple zero, E_k, E_log, E_{\log}, logarithmic model, tube,
singularity, discriminant, braid, threading, knot, Alexander, and Burau.  Candidate
hits were then inspected in context rather than counted as constructions merely
because a term occurred.

### Negative finding

No reachable commit contains a verifiable general multi-zero AEG construction, a
defined general object E_k, or an explicit AEG construction E_{\log}.  In
particular:

- the old version of notes/foundations-and-geometry/03-single-zero-diffusion-model.tex titled “Second Kind AEG-S2” is the same
  one-isolated-zero Poincare-disc model later made canonical in Paper I; it is not a
  multi-zero model;
- the legacy K2/K3 and tube sections were empty or marked TODO when the labels first
  appeared;
- later restructuring documents repeat the names as migration targets or open
  programs, but do not supply missing formulas;
- the logarithmic-sheet interpretation in the 2026 working discussion is a
  structural proposal about covering data, not an explicit AEG assignment and
  metric.

This is a negative result about the 249 reachable commit trees in this checkout.  It
does not exclude an uncommitted private note, an unreachable Git object, or an
external repository not supplied for the audit.  If such a source is later
provided, it must be added to this audit by path, immutable revision, and
formula-level comparison.

Consequently, every explicit multi-zero, logarithmic, and helical construction in
the current Paper III manuscript is REDERIVED HERE.  None is presented as a
recovered theorem about a pre-existing E_k or E_{\log}.

## 3. Canonical imported interfaces

| Source | Exact locus | Imported content | Paper III treatment |
|---|---|---|---|
| paper-1/sections/07-zero-geometry.tex | lines 14–37 in the audited tree | A regular zero of a real assignment is a smooth codimension-one submanifold | IMPORTED; no isolated, crossing, branching, or birth/death event is called regular |
| same | lines 39–49 | Exclusion of isolated points, crosses, branches, and endpoints at regular interior zeros | IMPORTED as the local obstruction |
| same | lines 101–135 | Singular AES data and the decomposition into regular and singular zero sets | IMPORTED; the additional Whitney stratification in Paper III is REDERIVED HERE |
| same | lines 141–246 | Verified isolated-zero Poincare-disc model | IMPORTED as a single local example, not as a universal normal form |
| same | lines 248–299 | Smooth total zero incidence and submersive parameter projection under spatial transversality | IMPORTED and re-expressed in vector-bundle language |
| same | lines 301–311 | Failure of global product conclusions without properness | IMPORTED as a standing warning |
| same | lines 313–316 | No certified multi-zero model in Paper I | PRESERVED; Paper III supplies new models |
| paper-2 active manuscript | arithmetic-holomorphic coordinate on the complete basic model | Ordinary holomorphic polynomial root families can be interpreted in the Paper II coordinate | IMPORTED interface only; the braid family constructed in Paper III is REDERIVED HERE |
| governance/00-authoritative-scope.md | lines 392–508 and 758–852 | Model audit, family-zero-set limits, and the knot-theorem gate | AUTHORITATIVE constraint |
| governance/01-paper-series-architecture.md | lines 1079–1123 and 1512–1527 | Canonical notation and the eight-part Paper III order | AUTHORITATIVE structure |
| governance/04-current-to-target-map.md | lines 1509–1653 | Reprove multi-zero formulas; distinguish seven zero/tube/knot levels; hold knot claims | AUTHORITATIVE migration rule |
| governance/05-mathematical-status.md | lines 1410–1564 and 2210–2398 | Proper-submersion boundary and open discriminant, monodromy, threading, and invariant questions | AUTHORITATIVE except for the unsupported E_k and E_{\log} provenance labels corrected below |
| governance/08-open-questions.md | OQ-012, OQ-019–021, OQ-037–046 | Reject numerical model naming; require properness, embedded moving points, collision avoidance, ambient isotopy, and Markov descent | AUTHORITATIVE open-problem boundary |

## 4. Historical tube timeline

| Date | Immutable source | Historical content | Present disposition |
|---|---|---|---|
| 2023-01-03 | commit 4272d61aed28cfaedb66fca42b45395808f5ff25, aeg-paper.tex, historical lines 842–854 | “tube structure of the first kind: TODO” and the image later retained as images/13-tube1st.png | MOTIVATION ONLY; no definition or proof |
| 2023-11-09 document date; first tracked 2025-03-01 | blob f0edf2dc6d293a7ebca2d4b9b722be2b62e68679 at gpt/2023-11-09_023605_Meeting_Minutes_Arithmetic_Expression_Geometry.tex, introduced in commit 97d5c2248e7bc14e1f64272e8285c79797f3cbac | K3 slices, a trajectory P(e^\lambda), a proposed uniformization, and collapse of zero lines by a congruence | HISTORICAL MOTIVATION; topology, congruence, zero-incidence relation, and properness are undefined |
| 2025-04-30 | commit 61cba1358f305b956dfe92705883d87516499063; now archive/paper4p/aeg.tex, lines 593–632 | T as a disjoint union of AES slices, base/fiber language, proposed sections, and the constant zero line x=0 for a=-x/y | AMBIENT-FAMILY SOURCE; explicitly lacks topology, differentiable structure, and bundle proof |
| 2025-05-16 | commit bf8959d365194c0361b7e35ff9147c524795585c; notes/foundations-and-geometry/02-parameterized-evaluation-frameworks.tex | Distinguishes a geometric family of AES manifolds from an algebraic evaluation family over evaluation parameters | RETAIN conceptual distinction; reject unsupported dimension and bundle assertions |
| 2026-08 | governance/discussions/aeg-tube-braid-markov-invariants.md | Separates boundary braids from singular fillings and develops Markov and affine no-go calculations | WORKING DERIVATION; used only where the active manuscript re-proves the calculation |
| 2026-08 | governance/discussions/three-branch-arithmetic-tubes-and-complexity.md, lines 1250–1296 | Records that no general E_k, E_{\log}, intrinsic thread, braid lift, or Markov-normalized invariant source was located | AUDIT CORROBORATION |
| 2026-08-06 | current paper-3/ source closure | Supplies explicit parallel, logarithmic-cover, helical, Morse, branch, and braid models | REDERIVED HERE |

Three historical meanings of “tube” must remain distinct:

1. an ambient family of AES spaces q:X→B;
2. an algebraic evaluation family E_alg→B_eval;
3. the zero incidence \(\pi:\mathcal Z\to B\).

The current manuscript reserves proper zero tube for the third object when the
projection is a surjective proper smooth submersion, with the corresponding neat
boundary conditions when boundaries are present.  A trajectory such as P(e^\lambda)
inside an ambient family is not automatically a zero branch or thread.

## 5. Formula-level historical source map

### 5.1 Tube, singularity, and covering material

| Historical source | Exact material | Valid residue | Rejected or missing inference |
|---|---|---|---|
| archive/paper4p/aeg.tex, lines 593–632 | T=\(\bigsqcup_{\lambda>0}E_1^{(\lambda)}\); P(e^\lambda); zero set x=0 for a=-x/y | A parameterized collection of ambient AES slices and a trivial zero-set control example | No supplied total-space topology, smooth structure, local trivialization, properness, embedded-thread datum, or knot information |
| notes/foundations-and-geometry/02-parameterized-evaluation-frameworks.tex, lines 25–62 | Multiplicative/additive evaluation families; E_alg and E_geom distinction | The distinction between algebraic evaluation and geometric parameter families | Calling the fibers “typically two-dimensional” or the disjoint union a bundle without a topology |
| notes/knots-and-loops/03-figure-eight-aeg-summary.tex, lines 23–38 | Proposed figure-eight-exterior model using a lifted fiber and eikonal propagation | A candidate research program | Smooth global propagation, equivariance, descent, cut-locus control, completeness, properness, and total-geodesicity are not proved |
| notes/knots-and-loops/03-figure-eight-aeg-summary.tex, lines 40–47 | Golden-ratio calibration | The Alexander root may motivate a multiplier | If the AEG multiplier is t=e^\lambda, the compatible parameter is \(\lambda=\log t\), not \(\lambda=t\) |
| notes/knots-and-loops/04-figure-eight-hnn-arithmetization.tex, lines 23–83 | Linear system \(\mu_u/t=\mu_u+\mu_v\), \(\mu_v/t=\mu_u+2\mu_v\), determinant \(t^2-3t+1\) | RETAIN as an explicit affine presentation calculation | It does not give a faithful knot-group geometry |
| notes/knots-and-loops/04-figure-eight-hnn-arithmetization.tex, lines 94–117 | Translation generators commute | RETAIN as the stated obstruction to faithfulness | Any earlier embedding language is superseded |
| notes/knots-and-loops/05-figure-eight-modulo-arithmetization.tex, lines 25–63 | Lattice generated by (1,0) and (0,\varphi) | The lattice is an ordinary discrete rectangular lattice | “Dense singular torus” is false in \(\mathbb R^2\); density occurs only after a specified one-dimensional projection |
| notes/foundations-and-geometry/03-single-zero-diffusion-model.tex, lines 23–99 | One isolated zero in the Poincare disc | Superseded by the verified Paper I model | Not a multi-zero construction and not evidence for E_k |
| notes/knots-and-loops/01-figure-eight-arithmetic-loop.tex, lines 159–281 | Curved-grid intersection formula and assignment \(-x/y=-R/c\) | RETAIN after a sign and domain audit as a visualization calculation | The map w=-1/z is holomorphic and orientation preserving, contrary to line 285 |
| notes/knots-and-loops/02-zero-taxonomy-and-arithmetic-loops.tex, lines 85–136 | Six-layer zero taxonomy and a zero signature | RETAIN only as relation-theory vocabulary | Historical subscripts do not canonically count isolated singularities |
| images/13-tube1st.png and images/sources/13-tube1st.tex | Four-slice tube picture; the TeX file generates only one component of the image | HISTORICAL VISUAL | The picture proves neither smooth incidence nor isotopy |
| images/14-apeirogon.png and images/sources/14-apeirogon.tex | Apeirogon picture and sparse axis overlay | HISTORICAL VISUAL | No formula links it to an AEG E_{\log} construction |

### 5.2 Affine, Alexander, and knot material

| Historical source | Exact material | Present treatment |
|---|---|---|
| notes/knots-and-loops/06-fox-calculus-and-alexander-modules.tex, lines 34–70 | Fox coefficient \(1-y\sim-\lambda\) and the first-order comparison with \(\pm\mu\lambda\) | RETAIN as an analogy, not an isomorphism |
| same, lines 72–102 | BS(1,2) Fox factor \(1-2t\) | RETAIN the computation; reject “intrinsic invariant” without descent |
| same, lines 104–170 | Figure-eight displacement \(D(r)=-\Delta\) and cocycle law \(D(uv)=D(u)+\phi(u)D(v)\) | RETAIN after convention audit; nontrivial cohomology is not inferred |
| notes/knots-and-loops/01-figure-eight-arithmetic-loop.tex, lines 98–150 | Explicit grid points and closure when the selected displacement vanishes | RETAIN as a free-word calculation |
| notes/knots-and-loops/07-figure-eight-arithmetic-interpretation.tex, lines 8–59 | Figure-eight presentation and the affine word yielding \(x-(t^2-3t+1)\) | RETAIN only with the qualification that the generator assignment descends to the knot group on the relator locus |
| notes/knots-and-loops/07-figure-eight-arithmetic-interpretation.tex, lines 66–83 | Claimed Sage/SnapPy checks through eleven crossings | HOLD until scripts, versions, presentations, and an immutable external revision are supplied |
| notes/knots-and-loops/08-small-knot-group-embeddings.tex | Three-parameter group law and claimed knot-group embeddings | REJECT embedding claims; the stated exponentiation interpretation is not represented by the displayed closed group law |
| notes/knots-and-loops/09-knot-torsion-and-cyclotomic-fields.tex, lines 110–165 | Conditional Alexander factorization and explicit 6_2/6_3 calculations | RETAIN as presentation calculations; the factorization is conditional, not a new invariant |
| notes/knots-and-loops/13-knot-torsion-results.tex, lines 8–228 | Raw data for 4_1, 6_2, 6_3, and 7_6 under different presentations and cyclic relators | RETAIN primarily as negative evidence that raw torsion depends on presentation, basepoint, sign, and normalization |
| notes/knots-and-loops/10-arithmetic-knot-geometry-zh.tex, lines 162–229 | Polished restatement of the same tables | No independent proof authority; “intrinsic” and “faithful” claims are rejected |
| images/sources/knot_4_1.tex, lines 20–131 | Reproducible arithmetic-grid drawing for images/knot_4_1.pdf | RETAIN as a figure source after convention review |

## 6. E_k and E_{\log} provenance correction

The following repository statements must be read as superseded by this audit:

- paper-3/README.md formerly described multi-zero, E_k, and E_log notes as though
  they supplied migrated constructions;
- governance/05-mathematical-status.md described E_k as partially proved and
  E_{\log} as a partial explicit construction;
- some working-discussion source maps attributed logarithmic or tube geometry to
  notes/computation-and-resources/03-turing-machine-resource-geometry.tex.

The corrected statuses are:

| Historical label | Correct provenance status | Allowed current use |
|---|---|---|
| E_k | OPEN HISTORICAL NAME; NO CERTIFIED GENERAL MODEL FOUND | Do not use as a theorem-defined classification.  Use descriptive names such as “parallel k-zero model.” |
| E_{\log} | DISCUSSION-LEVEL COVER/WINDING INTUITION; NO EXPLICIT HISTORICAL AEG MODEL FOUND | Use only when a new assignment, metric, domain, deck group, and zero-set audit are supplied. |
| tube of the first kind / K3 tube | HISTORICAL AMBIENT-FAMILY PROGRAM | Cite as motivation, not as a zero-tube theorem. |
| `03-turing-machine-resource-geometry.tex` tube source | INCORRECT SOURCE ATTRIBUTION | `notes/computation-and-resources/03-turing-machine-resource-geometry.tex` belongs to the Paper IV resource/computation program. |

The current Paper III logarithmic model is therefore called the logarithmic zero
lift, not E_{\log}.  Its missing origin is removable for the displayed assignment
and metric, so it is a covering-domain model rather than an essential singular
spine.

## 7. Current Paper III construction ledger

The following table separates imports from constructions proved in the current
manuscript.  Every row marked REDERIVED HERE must be reviewed from the active proof;
the historical files listed above are motivation or comparison only.

| Active source | Construction or result | Provenance status | Principal limitation |
|---|---|---|---|
| sections/01-singular-aes.tex, Definition “Stratified singular AES” | Adds a locally finite Whitney stratification as control data | REDERIVED HERE from the Paper I singular-AES interface | The stratification is not claimed canonical |
| same, Definition “Zero-object hierarchy” | Separates total zero set, smooth incidence, proper tube, embedded tube, thread, braid closure, and knot invariant | REDERIVED HERE from the authoritative restructuring distinctions | No arrow in the hierarchy is automatic |
| sections/02-local-zero-models.tex, “Cylindrical propagation” | Explicit product-circle zero model | REDERIVED HERE | A control example, not a classification |
| same, Theorem “Conformal realization” and corollary | \(g_a=\lvert da\rvert_h^2(\mu^2+\lambda^2a^2)^{-1}h\) realizes every submersion, and realizes critical functions off their critical set | REDERIVED HERE | Completeness and rigidity are not implied |
| sections/03-multi-zero-constructions.tex, Theorem “Parallel multi-zero model” | \(a_h=e^xh(y)\) with an explicit conformal metric; exactly k components for a polynomial with k simple roots | REDERIVED HERE; not migrated E_k | No uniqueness, canonical classification, homogeneity, or completeness |
| same, Theorem “Logarithmic zero lift” | Pullback of \(a_\times=Y\) on \(\mathbb C^\times\); zero lines y=k\pi and deck action k→k+2 | REDERIVED HERE; not migrated E_{\log} | Two deck orbits downstairs; no essential singularity at the omitted origin |
| sections/04-parameter-discriminants.tex, parameterized zero-section theorem | Vector-bundle version of vertical transversality and incidence submersion | REDERIVED HERE from the Paper I interface and standard transversality | Global topology still needs properness and boundary control |
| same, structural discriminant and nonproper escape example | Separates critical, boundary, metric/domain, and escape mechanisms | REDERIVED HERE | A general Whitney-stratified AEG discriminant remains open |
| sections/05-regular-tubes.tex, Theorem “Proper real-zero tube” | Proper real zero tubes over the circle have compact one-manifold fibers and torus components | REDERIVED HERE using the proper-submersion theorem and surface classification | Requires properness, boundarylessness, and a smooth global vertical orientation |
| same, Theorem “Helical zero-tube theorem” and corollary | Explicit compact helical family; component transport, deck shift, and torus-link boundary traces | REDERIVED HERE | The selected boundary trace is extra data and is not a new knot invariant |
| sections/06-singular-fibers.tex, Proposition “AEG Morse bifurcations” | Definite and indefinite Morse families with conformally realized singular metrics | REDERIVED HERE | Examples, not universal AEG normal forms |
| same, Proposition “Simple polynomial discriminant normal form” | Local reduction to \(w^2=\tau\) at a simple transverse polynomial discriminant point | REDERIVED HERE using a classical holomorphic normal-form argument | Local branch data do not determine a global filling or closure |
| sections/07-monodromy-and-braids.tex, finite-root theorem | Square-free monic polynomial families define finite proper root coverings and braid monodromy | REDERIVED HERE from classical configuration-space facts | Applies to complex auxiliary fields, not automatically to real rank-one assignments |
| same, Theorem “AEG realization of every braid” | Uses the Paper II holomorphic coordinate to realize a chosen geometric braid as polynomial roots | REDERIVED HERE | Universality is not a knot invariant and does not provide a natural braid from arithmetic history |
| same, Theorem “Logarithmic root transport and gauge” | Records lift-dependent deck integers and gauge-invariant cycle sums | REDERIVED HERE | Individual sheet labels are gauge dependent; roots must avoid zero |
| sections/08-threading-and-knot-questions.tex, Definition “Finite zero thread” | Makes thread selection explicit additional data | REDERIVED HERE | Intrinsicness requires a naturality theorem |
| same, Proposition “Stateless additive collapse” | Abelian additive braid data factor through writhe and collapse under both stabilizations | REDERIVED HERE from a working calculation | Applies to stateless additive targets |
| same, Proposition “Ordinary exactness” | Fixed-multiplier affine torsion is an Alexander-quandle coboundary | REDERIVED HERE from direct Aff calculations | It cannot furnish an ordinary cocycle enhancement |
| same, Theorems “Finite-field resonant affine class” and “Planar state-sum collapse” | Proves a resonant twisted class is nonzero, then proves its planar classical-link state sum reduces to coloring count | REDERIVED HERE | Nonzero cohomology alone does not give information beyond the Alexander baseline |
| same, variable-multiplier anomaly | Computes \(\mathfrak A_\kappa=((q-r)(r-1)/(qr))\kappa(x,y)\) | REDERIVED HERE from direct algebra | A nonzero defect is not an associator or invariant without coherence and state data |
| same, historical figure-eight word | Recomputes the word abbbaBAAB and obtains \(-\Delta_{4_1}(t)\) | RETAINED AND REDERIVED HERE | It is a free-word obstruction at generic t, not a generic knot-group invariant |

Supporting calculations in appendices/app-A-regularity-and-properness.tex,
appendices/app-B-configuration-and-braid-background.tex, and
appendices/app-C-affine-quandle-calculations.tex are part of the active proof
closure.  They are not transclusions of the legacy notes.

## 8. Retained claims and calculations

The following historical material may remain visible after the stated audit:

1. The Paper I regular-zero, singular-AES, family-incidence, and isolated-disc
   results, imported with their original hypotheses.
2. The distinction in notes/foundations-and-geometry/02-parameterized-evaluation-frameworks.tex between ambient geometric families and
   algebraic evaluation families.
3. The trivial historical zero family x=0 as a control illustrating that a
   parameterized picture does not prove nontrivial tube topology.
4. The linear HNN/Aff system and its Alexander factor \(t^2-3t+1\), together with
   the same note's proof that the translation image is nonfaithful.
5. The Fox first-order analogy and affine cocycle law, with no assertion of a new
   cohomology class unless independently proved.
6. The figure-eight, 6_2, 6_3, and 7_6 computations after recording presentation,
   word order, action convention, initial value, normalization, and cyclic
   basepoint.
7. The raw knot tables as counterexamples to presentation-independent raw torsion.
8. The Markov, Alexander-quandle, exactness, resonance, and variable-multiplier
   calculations only where they are re-proved in the active manuscript.
9. Historical figures as labeled schematics, never as evidence for existence,
   properness, isotopy, or invariance.

## 9. Rejected, superseded, or strictly conditional claims

The following claims must not be restored without a new proof:

1. Model indices canonically count zeros, singularities, or topological type.
2. A regular interior zero may be isolated, crossing, branching, or born/die.
3. Topology changes only where da=0; nonproper escape, boundary events, domain
   changes, metric degeneration, and projective poles must also be controlled.
4. A disjoint union of slices is automatically a smooth family or fiber bundle.
5. A smooth total zero set or submersive incidence is automatically a global tube.
6. The evaluation images S_{r,t} are “typically two-dimensional” without a
   declared topology, closure, or continuous parameterization.
7. A lifted figure-eight fiber is automatically an embedded totally geodesic
   hyperbolic plane in the three-dimensional universal cover.
8. The AEG additive parameter may be identified with an Alexander multiplier
   without the conversion t=e^\lambda.
9. The lattice generated by (1,0) and (0,\varphi) is dense in the plane.
10. The holomorphic Mobius map w=-1/z reverses orientation.
11. A selected free-word Aff computation automatically defines a representation
    of the presented knot group.
12. The three-parameter constructions in notes/knots-and-loops/08-small-knot-group-embeddings.tex embed the knot group.
13. Raw affine torsion is independent of presentation, basepoint, cyclic relator,
    or normalization.
14. A scalar crossing sum is new merely because it is nonzero before Markov
    stabilization.
15. Fixed-multiplier Aff conjugation contains a knot invariant beyond the Alexander
    quandle without additional state.
16. A stronger braid representation automatically gives a stronger knot invariant.
17. A nonflat Reidemeister-III defect is automatically an associator or
    filling-independent surface holonomy.
18. Countably many logarithmic sheets by themselves realize arbitrary knots.
19. A tube plus an arbitrarily selected thread automatically gives an isotopy
    invariant.
20. A local branch model w²=\tau determines the global braid factorization or knot
    type of a filling.

## 10. Reproducibility requirements for retained knot computations

Before a historical computation is cited as data rather than motivation, its record
must include:

- the group or monoid presentation and exact relator word;
- left or right action and multiplication/composition order;
- generator and inverse conventions;
- initial point or state;
- affine multiplier and logarithmic-parameter convention;
- cyclic basepoint and any conjugation used;
- denominator and unit normalization;
- script path, software version, immutable repository revision, and expected
  output.

The current claim that SageMath/SnapPy computations extend through eleven crossings
does not satisfy this requirement because the scripts are not present in this
repository.  It remains HOLD.

## 11. Bibliographic gaps exposed by the audit

The shared bibliography must support, with exact editions or papers:

- Ehresmann's proper-submersion theorem and the boundary/neat version actually
  used;
- Whitney stratification, Thom isotopy, and local singularity/discriminant normal
  forms;
- Artin braids, Fadell–Neuwirth configuration spaces, and a standard braid
  reference such as Birman;
- Alexander's closed-braid theorem and Markov's closure theorem;
- Fox calculus, the Burau representation, and the precise Alexander comparison;
- Rudolph's algebraic-function/braided-surface results with the quasipositivity
  hypotheses stated;
- Markov traces, Jones/Turaev constructions, quandles, and twisted quandle
  cohomology;
- Lawrence, Bigelow, Krammer, and Kohno if stronger braid representations are
  discussed;
- a standard source for the figure-eight knot exterior and its fibered/hyperbolic
  structure;
- SageMath and SnapPy, plus exact versions and script revisions for computational
  claims.

The references listed informally near the end of
governance/discussions/aeg-tube-braid-markov-invariants.md are a bibliography
seed, not yet a verified bibliography.

## 12. Known provenance-map corrections

1. References in governance/discussions/aeg-tube-braid-markov-invariants.md that
   assign tube or logarithmic geometry to notes/computation-and-resources/03-turing-machine-resource-geometry.tex are incorrect.
2. The historical short-manuscript path is archive/paper4p/aeg.tex, not an active
   paper4p/aeg.tex source.
3. Duplicate README paths in the source table of
   governance/discussions/three-branch-arithmetic-tubes-and-complexity.md describe
   different documents and should not be treated as two independent sources.
4. Legacy sections/sec09.tex contains relation and singularity outlook, not a
   tube theorem.
5. The current paper-3/ files are an active manuscript closure.  The earlier
   statement in governance/source-inventory.md that Paper III was only a README
   destination record is superseded by the integration addendum appended there.

## 13. Migration rule

The migration is non-destructive:

- all legacy notes, figures, knot calculations, and archived manuscripts remain in
  place;
- no historical formula is promoted solely by copying it into polished prose;
- imported Paper I and II results retain their hypotheses and citations;
- constructions newly proved in Paper III are labeled REDERIVED HERE in this audit;
- E_k and E_{\log} remain historical names rather than canonical classification
  symbols;
- threading, Markov descent, and separation beyond Alexander/Burau remain open
  unless the active manuscript supplies every required independence proof.

This audit is the provenance authority for the Paper III integration record.  The
mathematical truth status of individual claims remains governed by
governance/05-mathematical-status.md as corrected by the explicit negative
provenance finding above and by proofs in the active manuscript.

## 14. Post-audit arithmetic--automorphic addendum

The 2026-08-06 arithmetic--automorphic integration does not change the negative
historical finding for `E_k` or `E_log`.  Its provenance is instead split into three
explicit layers.

### Internal AEG source

Paper I's bilateral projective semantics already supplies the arithmetic contexts

```text
T_s(z) = z+s,
J(z)   = -1/z.
```

The specialization `s=sqrt(2)`, its order-four matrix relation, and the complete
regular-AES splitting theorem are newly integrated proofs in the active Paper I.

### External standard input

The definition and geometry of the (q=4) Hecke group, Rosen continued fractions,
and the normalized triangle-group Hauptmodul use the primary sources newly added to
the shared bibliography.  These sources establish the group/uniformization input;
they do not contain the AEG pullback metric or the claimed AEG history functor.

### Rederived in the active series

The following formulas and conclusions are `REDERIVED HERE`:

- the planar and cylindrical regular AES targets in Paper II;
- functorial pullback on the local-biholomorphism locus;
- essential critical points, (2m)-prong zero germs, and (2\pi m) cone
  completions in Paper III;
- the square-root and Cayley realification of the normalized (q=4) Hauptmodul;
- the equality of the resulting AEG zero graph with
  (\beta^{-1}([0,1]));
- the sign-character descent boundary;
- the AEG hierarchy from arithmetic prime relative divisors to geometric sheets.

The general history-to-relative-divisor map is a `STRUCTURAL PROPOSAL`, not a
recovered theorem and not a consequence of the historical tube conversations.

## 15. Sign-cover knot and register addendum

The files `sections/05-q4-geodesic-knots.tex` and
`sections/05-history-divisor-naturality.tex` are 2026-08-06 derivations.  No
historical repository source states their theorems.

The lens-space compactification, median-torus slopes, cusp-linking formula, and
periodic-orbit template are external classical inputs from Dehornoy and
Dehornoy--Pinsky.  The active Paper III rederives and audits their (p,q)=(2,4)
specialization, the index-two peripheral lattice, and the resulting
`S^3 minus T(2,4)` cover.  The equality between the AEG zero dessin and the
classical coding graph uses the already declared Hauptmodul normalization plus
the cited graph definition.  It is not a recovered `E_log` tube or a new
geodesic-flow template theorem.

The quadratic and quartic register equations, tagged trace, pole cocycle,
operator-collapse calculation, and Frobenius dictionaries are `REDERIVED HERE`.
Hartshorne, SGA 1, and Neukirch supply standard algebraic-geometry and arithmetic
background.  The typed registers are newly supplied inputs; the historical scan
found no source assigning these covers canonically to AEG histories.  Consequently
the general naturality functor and any knot decoration descended from it retain
their open status.

## 16. Polynomial threaded-carrier addendum

The file `sections/05-polynomial-threaded-carriers.tex` is a new 2026-08-06
derivation.  The historical repository scan found no source for the family
`Im(z^2-t^m)=0`, its carrier topology, or the horizontal identity proved there.
The following claims are therefore `REDERIVED HERE` from their displayed
equations:

- smoothness, neatness, four boundary components, `2m` Morse saddles, Euler
  characteristic `-2m`, and genus `m-1` of the carrier;
- the singular-AES slice metric and `4 pi` cone completion;
- the intrinsic root thread, braid `sigma_1^m`, and closure `T(2,m)`;
- equality of discriminant order and period, braid exponent, negative carrier
  framing, and negative half Euler characteristic;
- the q=4 peripheral binomial from the marked cover lattice, deck action, and
  cusp slope;
- the weighted logarithmic-tangent cone and its arithmetic quadratic-twist
  boundary;
- the supplied four-strand pullback of the braid-center extension, its integral
  relation character, and its LHS transgression/normalized period.

The configuration-space, Garside, torus-link, group-cohomology, and
weighted-projective background is standard; the manuscript either cites it or
includes the needed calculation.  No historical source makes the radial carrier,
the split arithmetic descent, or the four-root coefficient paths canonical.
Those choices are not promoted to a general AEG history functor, the new relation
character is not identified with Paper I affine torsion, and the two- and
four-strand torus links are not identified with one another.
