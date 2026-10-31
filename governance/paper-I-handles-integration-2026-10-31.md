# Paper I: handle surgery and annular-interface integration

Date: 2026-10-31 (Asia/Shanghai). Status: bounded manuscript integration audit;
not a whole-paper mathematical review or release approval.

## Baseline and authorization

Mingli Yuan requested checking the latest aeg-paper changes and adding the
discussion of drilling a body to add a surface handle to Paper I. The inspected
main baseline is `24ddba56242800b0a8ae837a2eb991d00502d00c`.
PR #20 is already merged as `5be8059bc8678c4611a8f61c3b4ccd568c6d7009`.
Subsequent combined-volume, cap, surface-holonomy and calculus-dictionary work
is present in that baseline, rather than being duplicated from the old branch.

The applicable scope is `00d-paper-I-calculus-and-capping-amendment.md`.
AGENTS.md's original narrow Paper I description is older, and expressly allows
an authoritative scope exception. The user's explicit Paper I instruction and
the existing amendment resolve that allocation. No new series-wide scope
change, paper migration or reordering is introduced.

## Integrated statements and dependencies

Canonical new text: `paper-1/sections/08-caps-and-interface-disks.tex`,
subsections 10.4 and 10.5 in this build. The abstract, introduction, conclusion,
acknowledgements and Appendix D are synchronized. Existing labels remain.

| Claim | Proof and explicit hypotheses | Status |
|---|---|---|
| Two mouths add a boundary handle | Compact oriented body; two proper tunnel ends in the same connected side surface, away from fixed external ports. Replace two disks by an annulus; use connectedness, orientability and Euler characteristic. Does not classify a knotted complement. | PI-H1, proved with stated hypotheses |
| Pierced disk loses its filling | Explicit product I times a disk, with a smaller concentric disk removed along the full interval. The remainder is a solid torus; annulus boundary is C-c; deformation retraction gives [C]=[c] nonzero in integral H_1. | PI-H2, proved with stated hypotheses |
| Double pants gluing gives a handle without feedback | Declared minimal ball-and-tube thickening; split and merge joined by two distinct forward wires. Euler count and E-V+1 agree. One versus two wires separates genus while preserving event reachability. | PI-H3, proved with stated hypotheses |
| Annular Stokes balance | Smooth declared one-form near the annulus; inner circle oriented as boundary of the removed disk, so boundary(A)=C-c. Ordinary Stokes gives the difference of periods. | PI-H4, proved with stated hypotheses |
| Product-tunnel computation | Three fixed cubical bodies with exact incidence/link, chain, homology and period checks. Same-author reuse of V1. | PI-H5, computationally verified example |
| Arithmetic annular interface | Two state carriers and compatibility relation, provenance and residuals still have to be specified; regular AES realization and native Seal remain open. | PI-H6, structural proposal / open problem |

The dependency chain is the existing decorated thickening and its genus
proposition -> surgery/product model -> double pants -> conditional annular
Stokes. No new proof depends on the higher-order Magnus interpretation, a
general DAG Stokes theorem, an ideal-completion boundary, or native Adva.

## Narrow corrections required by the integration

1. `prop:seam-circle-holonomy` now explicitly assumes smooth extension of
   the potential data to a neighborhood of the filling disk. Data only on the
   side surface do not supply a disk curvature integral.
2. `cor:capping-dichotomy` item 3 no longer infers nonconstant boundary
   assignment from collar gluing alone. Nonconstancy is necessary when a
   compact regular AES disk fills the seam; the disk extremum argument does
   not prohibit gluing annular collars without such a filling.
3. The introduction's universal-sounding surface-hole filling sentence is
   restricted to the two-pants model. The drilled example now explicitly
   separates a surface curve from its ability to bound in a chosen body.

No other analytical-pillar claims are audited or promoted by this change.
Homological vanishing is not claimed to certify embedded disk filling in
general. Nonzero topology is not claimed to force nonzero holonomy. The
closed angular one-form is an example for general forms, not a claimed global
arithmetic potential. The split--merge example gives 2x, making explicit that
handle insertion is not automatically a value-preserving program rewrite.

## Finite calibration and reproduction

The new `research/pants-interface-disks/verify_handles.py` imports unchanged
V1 helper code, Git blob `10e455e60d4857d4ce84411390f8a0650c6c971a`.
It constructs the 27-cube box, 26-cube blind indentation, and 24-cube tunnel.
All 64 vertex links in each body are checked. Boundary Euler characteristics
are 2, 2, 0; body first Betti numbers over F_2 are 0, 0, 1.
For the outer circle, the box has boundary/augmented rank 81/81 and the tunnel
80/81. The inner circle survives; an explicit radial rectangle fills a
meridian. Oriented chains give boundary(A)=C-c, and the form -y dz has periods
-9, -1 with annular curvature integral -8. Eight negative controls reject.

Executed locally:

```bash
python3 research/pants-interface-disks/verify_handles.py > /tmp/handles.json
cmp /tmp/handles.json research/pants-interface-disks/evidence-handles.json
python3 -O research/pants-interface-disks/verify_handles.py > /tmp/handles-O.json
cmp /tmp/handles.json /tmp/handles-O.json
bash build.sh 1
git diff --check
```

The manuscript-build workflow repeats the finite normal/optimized comparison.
The checked-in evidence binds both verifier and unchanged V1 helper digests.
The new test is a geometric calibration, not the previously planned V2
equal-value/distinct-producer experiment; the V1 evidence is unchanged.

## Build, static checks and visual inspection

- Unmodified baseline built locally: 55 pages.
- Updated Paper I built through the repository script: 59 pages, 752783 bytes.
- PDF SHA-256: `8a6a5b4f4bb3d248fba3bbac32abb0930e3cac2aa93a22e06f214991f02f1e2f`.
- Static source closure: 133 unique labels, zero duplicate labels, zero missing
  referenced labels/citation keys, and all input files present.
- Final LaTeX log: no undefined references/citations, undefined control
  sequences, duplicate labels or missing assets.
- Baseline and updated logs both have the same nine overfull-box widths and
  two hyperref PDF-string warnings in pre-existing text. No new warning was
  introduced. This is not a claim that the entire manuscript is warning-free.
- Rendered pages 2, 4, 8, 9, 44–49, 52, 57–58 were inspected. New text,
  equations and the calibration table have no clipping, overlap or missing
  glyphs. The pre-existing long scope-file path on page 9 remains overfull.
- Paper 0 and Paper IV were not changed or rebuilt locally; the existing
  remote integration workflow builds them alongside Paper I. Remote results
  belong to the submitted commit's workflow record, not to this local audit.

## Remaining work and provenance

OQ-096.5 asks for the actual two-boundary state relation and its compatibility
with a decorated surgery. The regular AES extension and native Seal bridge
remain open, as do OQ-096.1's general composition and OQ-096.2's residual
reopening experiment. No source is moved to another paper or archive.

Research direction and the drilling/handle question: Mingli Yuan.
Formalization, proofs, implementation, self-review and integration: Codex
(OpenAI). Existing DeepSeek assistance remains credited. These checks are
not independent human mathematical review or an independently authored
verification implementation.
