# Figure Asset Audit

**File:** `governance/figure-asset-audit.md`
**Status:** Audit record (inventory and defect register for `images/` and
`images/sources/`; non-authoritative, does not revise scope, deletes nothing)
**Version:** 1.0
**Date:** 2026-11-11
**Prepared by:** DeepSeek Harness (AI coding agent), working under the
repository author's direction.  No mathematical status, scope statement, or
claim grade is changed by this audit.
**Depends on:**

* `AGENTS.md`
* `governance/source-inventory.md`
* `governance/06-editorial-rules.md`

**Applies to:** every rendered asset directly under `images/` and every source
under `images/sources/`, the directory that inherited the former `misc/`
family.

---

## 1. Provenance and population

| Location | Contents | Measured count | Recorded count |
|---|---|---:|---:|
| `images/` | rendered assets | 21 PDF + 5 PNG = 26 | 26 |
| `images/sources/` | former `misc/` sources | 27 `.tex` + 2 `.png` = 29 | 28 |

The `misc/` figure is one higher than the count recorded in
`source-inventory.md` section 2.  No file was added by this audit; the
discrepancy is recorded rather than reconciled, following the rule that
conflicting counts are logged and not silently adjusted.

`images/` and `images/sources/` are `HOLD / ARCHIVAL`.  Section 4 of
`source-inventory.md` already establishes that no canonical paper includes an
external image: the Paper 0 build closure is its 12 section files, 6 appendices,
and the shared bibliography.  Every figure currently printed in Paper 0 is
inline `tikzpicture` source.

## 2. Source-to-asset ledger

Sizes are the natural PDF box at 72 pt per inch, so they record the size at
which each asset would be placed if it were used without scaling.  Aspect ratio
is width over height.

| Source | Asset | Size (in) | Ratio | Note |
|---|---|---|---:|---|
| `01-grid-example-1.tex` | `01-grid-example-1.pdf` | 6.77 x 3.72 | 1.82 | rectilinear grid with assignment labels |
| `02-example-expression-syntax-tree.tex` | `02-....pdf` | 1.48 x 1.67 | 0.89 | the only portrait asset; small, harmless |
| `03-...-left-right.tex` | `03-....pdf` | 4.10 x 1.74 | 2.35 | string and tree, both combs |
| `04-...-combination.tex` | `04-....pdf` | 1.96 x 1.95 | 1.01 | mixed comb |
| `05-example-expression-embedding.tex` | `05-....pdf` | 6.77 x 4.06 | 1.67 | grid plus one embedded path |
| `06-example-canonical-form.tex` | `06-....pdf` | 6.77 x 4.56 | 1.49 | four histories, one endpoint |
| `07-grid-detail.tex` | `07-grid-detail.pdf` | 6.85 x 3.72 | 1.84 | grid with explicit assignment values |
| `08-grid-schema.tex` | `08-grid-schema.pdf` | 7.58 x 3.78 | 2.01 | exceeds the 6.5 in measure |
| `09-grid-schema-g1.tex` | `09-grid-schema-g1.pdf` | 7.58 x 3.78 | 2.01 | exceeds the 6.5 in measure |
| `10-gca.tex` | `10-gca.pdf` | 2.94 x 1.76 | 1.67 | small dependency diagram |
| `11-horocyclebased.tex` | `11-horocyclebased.pdf` | 3.34 x 3.16 | 1.06 | saturated red fill of the disc |
| `12-proofbymapping.tex` | `12-proofbymapping.pdf` | 7.01 x 3.16 | 2.22 | two panels, inherits the red fill |
| `13-tube1st.tex` | `13-tube1st.png` | 2120 x 955 px | 2.22 | rendered to raster, inherits the red fill |
| `14-apeirogon.tex` | `14-apeirogon.png` | 2400 x 1800 px | 1.33 | axes drawn over a raster figure |
| `17-area-formula.tex` | `17-area-formula.pdf` | 10.45 x 6.48 | 1.61 | exceeds the measure by a wide margin |
| `18-grid-example-2.tex` | `18-grid-example-2.pdf` | 6.77 x 3.72 | 1.82 | asset predates its source |
| `cayley-tree-4-border.tex` | `cayley-tree-4-border-2..5.pdf` | 0.85 to 3.61 square | 1.00 | one source, four assets |
| `cayley4.tex` | `cayley4.pdf` | 4.83 x 4.83 | 1.00 | Lindemayer tree |
| `knot_4_1.tex` | `knot_4_1.pdf` | 10.30 x 6.48 | 1.59 | exceeds the measure by a wide margin |

## 3. Defect register

### 3.1 `18-grid-example-2.pdf` does not correspond to its source

The source is dated 2025-12-06 and carries about thirty-five red numeric
labels; the asset is dated 2025-07-12.  Rendering the asset at 250 dpi confirms
that none of those labels is present.  The asset is a snapshot of an earlier
revision of the source, not a rendering of the current one.

**Treatment:** recorded, not rebuilt.  Rebuilding would replace an archival
artifact with something never distributed.  Any future use must reconstruct the
figure from the source rather than include this PDF.

### 3.2 Byte-identical duplicate sources

`01-grid-example-1.tex` and `15-domain2.tex` are identical
(`md5 2b86636918fd8f9aca1f23d3f7164826`).  Only `01` has an asset, so `15` is
dead weight but carries the name `domain2`, which records an intention the file
no longer expresses.

**Treatment:** both retained.  Deleting the duplicate would erase the name
`domain2`; it is cheaper to keep one redundant file than to lose that record.

### 3.3 Assets with no source

`cayley.pdf`, `jigsaw-riemann.png`, `sine2d.png`, `t4096.png`.

`cayley.pdf` is not the output of `cayley4.tex`, which produces `cayley4.pdf` at
a different size.  The three PNGs are montages or large renders with no
recorded generator.  None of them can be regenerated from this repository.

**Treatment:** retained as the only surviving record; marked not reproducible.

### 3.4 Sources with no asset

`08-uniformazation.tex`, `15-domain2.tex`, `16-localdomain.tex`,
`19-curl.tex`, `20-grid-example-3.tex`, `charts.tex`, `prism-torus.tex`,
`square-fractal.tex`.

That is eight of the twenty-seven sources.  A ninth source,
`cayley-tree-4-border.tex`, does have assets, but under names the source does
not contain: it hardcodes `\numsteps=2` while assets exist for `2..5`, so
three of its four renderings cannot be regenerated without editing the text of
the source.  The ledger in section 2 lists it once, under the assets it owns.

Two of the eight cannot compile as shipped and are not merely unrendered:

* `08-uniformazation.tex` contains an empty `tikzpicture` and produces nothing.
* `16-localdomain.tex` sizes its image with `\textwidth` inside a `standalone`
  document and references `ii2_symmetry.png`, which lives in `sources/`, not in
  `images/`; both choices assume a build directory the repository does not fix.

The remaining six are ordinary unrendered sources, useful only when a figure is
reconstructed from them rather than included.

### 3.5 Assets wider than the text measure

With `letterpaper` and `margin=1in` the measure is 6.5 in.  `17-area-formula`
(10.45 in) and `knot_4_1` (10.30 in) exceed it by more than half again;
`08-grid-schema` and `09-grid-schema-g1` (7.58 in) exceed it slightly.

Scaling `17` into the measure costs a factor of 0.62, which takes its red
labels from about 7 pt to about 4.3 pt.  This is the reason no asset of this
family can be included by `\includegraphics` without a redesign.

### 3.6 Saturated fills

`11`, `12`, `13`, and the two raster montages draw the disc as
`\draw[red,fill=red] ... circle[radius=4]`, a solid red disc that covers the
horocycle family and the point labels.  The fill is plausible as an intention to
mark the disc as a region; the saturation is not, and it does not survive
printing.

### 3.7 Duplicated grid body

The base grid of about 110 lines is copied verbatim into `05`, `06`, `07`,
`15`, and `20`, and the disc of `11` is copied into `12` and `13`.  A change to
the grid must be made in up to six places.

## 4. Status of the archive

Every item remains `HOLD / ARCHIVAL`.  Nothing in `images/` or
`images/sources/` may enter a canonical build closure.  The list below is
binding for future work.

| Use | Permitted |
|---|---|
| `\includegraphics` of an asset into a paper | no, without a recorded exception in this file |
| reconstruction of a figure in the paper's inline style, citing the source file | yes |
| deletion of a source or an asset | no, without an entry in `migration-log.md` |
| rebuild of an asset from its source | no, unless the asset is first preserved |

## 5. Reconstructions in Paper 0

Four figures in Paper 0 were reconstructed from this archive rather than
included.  Each carries a comment naming its source file.

| Paper 0 figure | Label | Derived from | Change made |
|---|---|---|---|
| Figure 4 | `fig:p0-halfplane-disc-dictionary` | `11`, `12` | light panel fill instead of a saturated disc; two families separated by colour and by panel captions |
| Figure 6 | `fig:p0-affine-vs-projective-cell` | `01`, `18` | reduced to the two curve families the Bruhat decomposition separates |
| Figure 8 | `fig:p0-same-charge-different-histories` | `06` | ACS coordinates instead of grid coordinates; the "infinite accumulation" path of the original is dropped, since Paper 0 develops no convergence theory for infinite expressions |
| Figure 10 | `fig:app-staircase-rectangles` | `17` | twenty-five columns reduced to the three orders that produce 1, 6, 21; the enclosed quantity labelled as a weighted area, not a cell count |

## 6. Open items

1. The `misc/` population count in `source-inventory.md` differs from the
   measured count by one (section 1).
2. `18-grid-example-2` has no faithful rendering (section 3.1).  A faithful one
   would have to be built and kept beside the current asset, not over it.
3. The three unrenderable PNG montages have no generator (section 3.3).  If
   they are to be used, they must be redrawn rather than cited.
