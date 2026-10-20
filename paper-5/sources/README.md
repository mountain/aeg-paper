# Sources for Paper V

This directory carries the provenance of Paper V: the material from which its
mathematical content was extracted, recorded so that a reader can audit the
absorption decisions rather than take them on trust.

**Governing scope:** [`governance/00c-paper-V-triadic-aperture-scope.md`](../../governance/00c-paper-V-triadic-aperture-scope.md)

## `survey/`

Ten batch digests (`G01.md`–`G10.md`) covering the 133 files of the research
corpus `adva/docs/research`, notes `0001`–`0127` — every note numbered before
`0128`.  The corpus totals 65,102 lines; it was partitioned into contiguous
batches of at most roughly 3,800 lines each and digested on 2026-10-20.

Each digest records, for its batch:

* **Coverage** — one line per file: the note title, the note's own `Status:`
  line, and a sentence naming the mathematical core, or the words
  "engineering-only" where that is the honest verdict.
* **Mathematical objects** — definitions, with the source note number.
* **Results** — kind, faithful shortened status, statement, and whether the
  engineering dependency is `none`, `partial`, or `essential`.
* **Threads** — the recurring theoretical through-lines.
* **Engineering-only material** — what was excluded and what it depended on.
* **Cross-links** — where the batch builds on, corrects, or feeds another thread.

## How this directory was used

Two rules governed the extraction, and both are visible in the digests:

1. **Mathematics in, engineering out.**  Checked-program harnesses, test suites,
   Rust/Python authority splits, work-package phases, document formats, ledgers,
   CI gates, and "not a stable API" governance boilerplate were excluded; only
   mathematical content was carried forward.
2. **Statuses inherited, not upgraded.**  A note's own `Status:` line bounds what
   Paper V may claim.  Where a note says "bounded calibration", the paper does not
   say "theorem".

Every result in the paper is mapped back to its source note, with its inherited
status, in
[`paper-5/appendices/app-D-claim-ledger.tex`](../appendices/app-D-claim-ledger.tex).
That appendix also lists the mathematical clusters deliberately left to a
subsequent paper, and the fifteen files that are predominantly engineering.

These digests are research instruments, not claims.  They are not authoritative
for any mathematical statement; the paper and its claim ledger are.
