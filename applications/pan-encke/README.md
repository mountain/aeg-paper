# Pan and the Encke Gap Edge Waves — an Application Example

This directory holds a self-contained application example of the **HTWR
(Hyperbolic Tropical Wavefront–Residual)** framework: a two-layer account of the
scalloped ("wavy") edges of Saturn's Encke gap, shaped by the shepherd moon Pan.

## The paper (bilingual)

| language | LaTeX source | built PDF | readable Markdown |
| --- | --- | --- | --- |
| English | `aeg-app-pan-encke.tex` | `aeg-app-pan-encke.pdf` | `pan-encke-paper.en.md` |
| Chinese | `aeg-app-pan-encke-zh.tex` | `aeg-app-pan-encke-zh.pdf` | `pan-encke-paper.zh.md` |

Shared bibliography: `aeg-app-pan-encke.bib`.

## The two-layer result (summary)

1. **Arithmetic layer (the HTWR contribution).** Pan's Lindblad resonance ladder
   `x = m/(m±1)` is the **Farey neighbourhood of corotation** (`x = 1`), realized
   as **Ford circles piling up on the hyperbolic upper half-plane** — a concrete
   physical instance of the rational-approximation structure at the core of the
   HTWR framework. The `m = 551` resonance sits at the Encke outer edge; the
   gap is opened by **Chirikov resonance overlap** (`gap ≈ 8.5 R_H`).
   Status: `STRUCTURAL PROPOSAL` (reading) + elementary celestial mechanics.

2. **Dynamical layer (standard celestial mechanics).** The observed edge wave is
   neither a propagating density wave nor a (cold or pressure) edge mode, but
   Pan's **static tidal distortion** (a forced epicycle), with amplitude
   `GM_P/(κ²d²) ≈ 0.79 km` and azimuthal scale ≈ 250 km — matching the values
   extracted from the public-domain Cassini image PIA08257 (≈ 0.65 km, ≈ 300 km).
   Status: `PROVED WITH STATED HYPOTHESES` + `COMPUTATIONALLY VERIFIED EXAMPLE`.

The two layers are **complementary, not the same phenomenon**: the arithmetic
skeleton explains *where the gap is*; the tidal distortion explains *why its edge
is scalloped*.

## Companion notes

The derivation is documented in the note series
`aeg-paper/notes/general/`:

- `007-pan-encke-farey` — the Farey/Ford resonance ladder and gap opening.
- `008-encke-density-wave` — the tight-winding density-wave dispersion.
- `009-encke-edge-mode-wkb` — the edge-mode elimination (cold + pressure).
- `010-encke-scalloped-edge-tidal` — the static tidal distortion (resolution).

Governance: the open items are registered as **OQ-104** in
`governance/08-open-questions.md`; the note-level status is in
`governance/notes-reserve-audit.md` §2.9.

## Build

From the repository root:

```bash
./build.sh app        # builds the English (pdflatex) and Chinese (xelatex+ctex) PDFs
./build.sh all        # builds papers 0–6 plus this application
```

Requirements: `pdflatex`, `bibtex`, `xelatex` (with `ctex` for the Chinese
version).

## Provenance

Research direction, object choice, and physical statements: **Mingli Yuan**
(corresponding author and sole holder of scientific responsibility).
Derivations, exact computations, image extraction, and LaTeX preparation were
assisted by **DeepSeek Harness** (an AI research agent), credited as assistance,
not authorship.  NASA images are public domain.
