# Finite-type and ported AES integration

Date: 2026-10-09. Baseline: `968c5c29557e8f7d70fe8baea2733726b852507d`.
Status: integration and reproducibility record; mathematical statuses are
registered in `05b-paper-0-status-register.md` and `05-mathematical-status.md`.

## Purpose and provenance

This integration develops Mingli Yuan's 2026-10-09 research direction:
make punctured AES constructions reusable across contexts, then distinguish
geometric ends from program holes and ports so arbitrary finite input arity
can coexist with a declared three-output interface. The circle surgery,
three-ended organization, and opposite-process feature questions originate in
that research discussion. The candidate manuscript *Ported Arithmetic
Expression Spaces: Substitution, Execution, and Composition*, dated 9 October
2026, Version 0.1, was prepared in collaboration with Codex following that
programme.

The complete text of that eight-page manuscript and the mathematical
conclusions of the accompanying discussion were available for this
integration. Its original LaTeX/checker archive
`aes-ported-paper4-v0.1.zip` and the earlier
`aes-k4-compactification-v0.1.zip` were not available as readable bytes.
Consequently the canonical Paper IV text is a reviewed adaptation from the
readable PDF, not a byte-preserving source import. The two new repository
verification scripts are independent implementations. The historical reports
of **39** and **55** successful checks have **not** been rerun or independently
reproduced as the original suites. Recovering those two archives remains a
separate open provenance task. No uninspected original diagram is represented
as inspected or imported. No private conversation transcript is included here.

The working scope remains the existing series architecture: Paper 0 owns
geometric construction and collar descent; Paper I owns marked history syntax;
Paper IV owns the finite program/observation interface and its cost boundaries.
The integration does not claim a completed Adva-to-AES equivalence.

## Source-to-manuscript map

| Research conclusion or note | Canonical destination | Treatment |
|---|---|---|
| Visual boundary, cusp point filling, metric completion, marked boundary, unit tangent lift are distinct | Paper 0 §12.1 and Appendix E.4 | Explicit distinctions; no dimension increase from ordinary compactification |
| Product-sign Bolza curve after an independent metric sheet; genus alone does not identify it with glued pants | Appendix E.4 | Exact specialization and genus computation; pinned Process Geometry §2.6; semantic/conformal identification remains open |
| Genus-zero k-cusp compactification preserves k marked points and k−3 complex moduli | §12.1 | Carrier claim with punctured-disc ends, not arbitrary AES classification |
| Pants counts, FN reconstruction, pinched three-cusp components and plumbing | §12.3–12.4 | Counts derived; standard geometry cited; full AES germs separately required |
| Explicit z^(k−2) cover and exceptional harmonic four-puncture modulus | §12.4 | Direct cover verification; special family only |
| Three-circle gaps, dual ideal triangles, doubling to three cusps and recursive circles | Appendix E.1 | Elementary normalization proof; recursion is extra structure |
| Four initial triangular gaps then ternary recursion | Appendix E.1 | Corrected count 4·3^n; no uniform four-branch rule |
| Paper 0 common-point four circles are not the tangent-ring seed | Appendix E.2 | Incidence/angle obstruction, explicit t∈[1,√2] circle deformation; no AES deformation claimed |
| Four half-discs give two sheets; independent disc plus cuts gives a three-sheet model | Appendix E.3 | Declared cut transpositions, monodromy, w³ map and Euclidean cone angle; mere point gluing excluded |
| Every k≥1 admits a compactifiable punctured AES | §12.2 `thm:p0-arbitrary-k-punctures` | Direct proof; k−1 finite critical points plus essential infinity |
| General cut/reconstruct theorem with exact end data | §12.3 `prop:p0-aes-collar-descent` | Full smooth collars, marked orientation, equal signed parameters and Hausdorff quotient |
| Complete regular AES cannot use a three-cusp complete metric | §12.4 warning | Imports Paper I splitting theorem with all global hypotheses |
| k4 model, two pants cuts, fixed finite end values | §12.2–12.3 | Explicit rational data and direct collar reconstruction |
| An assignment-identity word can move the surface state | §12.5 | New independent analytic certificate at (0,1), residue (−3/4,0), plus exact finite regression checks |
| Puncture, computational hole and anchored port are distinct | Paper IV §6.1 | Structural definition; k, input arity and output arity independent |
| Programs fill holes before numerical evaluation; source, occurrence, copies and call records survive | §6.2–6.3 | Finite typed substitution, explicit resource discipline; `Subst` avoids existing rewrite-area `Fill` |
| Exact partial-domain substitution/evaluation compatibility | §6.4 | Strict deterministic finite DAG theorem; discarded invalid work still invalid |
| Numeric equality, network isomorphism and literal graft receipts differ | §6.3–6.4 | Boundary permutation and renaming explicit; receipts and schedules not collapsed |
| Joint geometric and computational assembly | §6.5 | Full seam/interface records, globally acyclic event graph and added packet allocation; no gate-motion theorem |
| Opposite-process features may be richer than scalar eigenvalues | §6.6 and open obligations | Domain, policy, provenance and residue retained; spectrum requires a declared endomorphism |
| Feature observation sufficiency vs closed online state | §6.6 | Contextual-refinement iff and stronger right-congruence iff; counterexample included |
| Four input producers, three outputs (9,15,5/2), two geometric cuts | §6.7 | Exact scalar experiment; not identification with Adva native three output roles |
| Three-side cyclic dependence requires snapshot/update/fixed-point semantics | §6.8 | Open; no feedback solution inferred from finite acyclic theorem |
| Actual opposite-edge witnesses and faithful multi-input AES motions | Paper IV open programme and status ledger | Remain open, matching the pinned Adva 0114 boundary |

The session's specialized Kleinian realization of an Apollonian limit set is
retained as background motivation only, not imported as an AES claim. It is
not needed for any proof here, and the three-dimensional Kleinian model is
outside the current planar/AES construction. Likewise the original numerical
cross-seam trajectories and original conjugation checks are not claimed
reproduced without their unavailable source/evidence files. The manuscript
instead proves full-collar local-flow compatibility and provides a new exact
motion-residue certificate.

## Directly necessary repair of an existing claim

The September 29 review already records that the printed unrestricted
`thm:p0-punctures-are-critical` is false. Its proof created a replacement metric
and treated it as an extension of the original metric. The integration repairs
only this directly relevant puncture foundation:

- require the original metric to be conformal near each puncture to a smooth
  positive-definite extending background metric;
- use the eikonal identity to prove that the prescribed conformal factor is
  exactly the extension formula;
- restrict the dependent count corollary and explanatory prose to that class;
- retain the anisotropic counterexample and the general inclusion Crit(a)⊆S;
- prove arbitrary-k existence directly, treating infinity by divergence rather
  than as a critical point of a nonexistent smooth extension.

The original review, evidence record, and dated governance history are intact.
The false equality for a prescribed AES is not confused with a refutation of
every possible existential statement about other functions on its surface.
No other historical witness is silently reclassified.

## Sources verified for this integration

- Wolpert, *Geometry of the Weil–Petersson completion of Teichmüller space*,
  Surveys in Differential Geometry 8 (2003), §§2–3; pants/FN/plumbing/cusps.
- Graham–Lagarias–Mallows–Wilks–Yan, *Apollonian Circle Packings: Geometry and
  Group Theory I*, DCG 34 (2005); recursive construction and Möbius action.
- Hatcher, *Algebraic Topology* (2002), §1.3; covering classification.
- Process Geometry `c47c96fa79123c677172278be59d67ca1cc891b1`,
  `docs/MATHEMATICAL_CORE.md` §2.6; exact Bolza provenance.
- Adva `cce73004c2b4fbfb87d9ba1ccc66820423273cf6`,
  `docs/TECHNICAL_REPORT_PROGRAM_PROCESS_CORE.md` §§1.2–1.3 and research notes
  0109 and 0114; program substitution, outer/inner arity, unresolved opposite
  characteristics. These are pinned research claims, not present-day promises.

The shared bibliography contains the actual cited sources; private source URLs
and ephemeral download locations are not publication references.

## Reproduction

From the repository root:

```sh
python3 paper-0/scripts/verify-compactification.py
python3 paper-4/scripts/verify-paper4.py
python3 paper-4/scripts/verify-ported-aes.py > /tmp/ported-aes.json
cmp /tmp/ported-aes.json paper-4/scripts/fixtures/ported-aes/integration-evidence.json
python3 -O paper-4/scripts/verify-ported-aes.py > /tmp/ported-aes-optimized.json
cmp /tmp/ported-aes.json /tmp/ported-aes-optimized.json
./build.sh 0
./build.sh 1
./build.sh 4
```

The verification scripts use the Python standard library and exact rational
arithmetic. The updated CI runs these checks and builds Papers 0, I and IV,
then rejects unresolved references, citations and duplicate labels. Finite
checks are regression evidence alongside the in-paper proofs, not universal
verification of arbitrary surfaces or programs.

Local results and final artifact sizes are recorded below after validation.

## Local validation results

- New Paper 0 exact finite suite: 139 checks passed; normal and `python -O`
  evidence byte-identical. This covers finite family samples, signed/zero
  generator cases, counts, two puncture partitions, first-jet frame/bracket
  values, the residue certificate, circle incidence and sheet monodromy.
- Existing Paper IV suite: all 7 groups passed.
- New Paper IV suite: all 14 substantive groups passed; normal, optimized and
  checked-in JSON evidence byte-identical. This includes strict failure,
  explicit sharing/discard, source/occurrence collisions, boundary permutations,
  receipt distinctions, feature obstructions, two detached seam-packet
  reassemblies and exact rational collar samples.
- Canonical builds: Papers 0, I and IV each produced a PDF. Paper 0: 90 pages,
  823,784 bytes. Paper IV: 54 pages, 587,514 bytes. Paper I was rebuilt for
  cross-bibliography validation; its untouched checked-in PDF was retained.
- Static active-source closure: Paper 0 has 19 files/243 labels; Paper I has
  10 files/67 labels; Paper IV has 20 files/105 labels. No missing references,
  duplicate labels, or missing citation keys in those closures. No missing
  figures, undefined control sequences or missing-glyph warnings in final logs.
- Paper IV's final log has no warnings. Paper 0 retains one pre-existing
  11.13pt overfull box in unchanged `10-beyond-linear.tex`. Paper I retains
  two pre-existing overfull boxes in its unchanged text. No newly inserted
  compactification, ported-program or appendix passage reports an overfull box.
- The container's preinstalled TeX tree lacked format/font-map databases. Local
  temporary format/font-map reconstruction from its already-installed TeX
  distribution enabled the canonical build script; no manuscript workaround
  or system-wide setting change was used. CI installs the standard TeX packages.
- Independent mathematical review checked the repaired theorem, new geometric
  proofs, finite-program proofs, exact residue and explicit remaining gaps.
  Visual inspection covered the new Paper IV chapter/ledger and 23 Paper 0
  pages: 1–4, 6, 57–61, 66–74 and 87–90. No new clipping, overlap, missing
  glyph or equation-layout defect was found. Existing literal emphasis
  asterisks and the interface-table page break remain minor editorial issues.

## Remaining work

Recover the two original archives for byte-preserving research provenance and
rerun their original suites. Thereafter the next mathematical task is a
specific opposite-edge feature witness and a certified multi-input AES gate
realization with domains and history residue retained. This integration does
not claim either has been constructed.
