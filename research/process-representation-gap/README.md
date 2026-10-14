# Process representation gap

Execution of the work plan `AEG-process-representation-work-plan.md` (version
1.1, 2026-10-10) against the three pinned repositories.

This directory asks a single question in six settings: **where does a declared
representation of a process stop being sufficient for a declared task, and what
is the cheapest honest repair?**

The research starts from native process languages. Linear operators, spectra,
scalars and matrices are *optional downstream representations*, never the
definition of the native object.

## Reading order

1. `reports/00-gap-classification.md` — the cross-experiment result, the cost
   table, and the gap taxonomy. Start here for conclusions.
2. `reports/00-minimal-repair.md` — what to change, ordered by evidence.
3. `reports/00-verification.md` — what was verified, how, and one anomaly that
   is on the record rather than explained away.
4. `reports/00-interface-promotion.md` and `proposals/` — the section 10
   promotion proposals. **None is applied.**
5. `reports/manifest-baseline.md` — the frozen source baseline.
6. The six per-experiment reports in `reports/`.
7. `contracts/` — the frozen contracts, one per experiment, with the digest
   ledger `contracts/FROZEN.sha256`.
8. `evidence/` — machine-readable evidence, one document per run.

## What is here

```text
contracts/    frozen experiment contracts + FROZEN.sha256 digest ledger
fixtures/     minimal witnesses extracted from the evidence, with provenance
experiments/  exact checkers, primary and independent, plus source probes
evidence/     canonical JSON evidence and raw per-record tables
proposals/    unapplied interface-promotion drafts for the sibling repositories
reports/      per-experiment and cross-experiment results
tools/        the shared harness and the reproducibility tooling
```

The suggested structure of work-plan section 10 is followed, adapted to this
repository: `fixtures/` holds material **extracted** from `evidence/` by
`tools/build_fixtures.py` rather than retyped, `proposals/` was added because
section 10 requires promotion to be *proposed* and this branch must not change
the sibling repositories, and the plan's "实验" numbering is preserved in every
filename.

## Baseline

Frozen by `tools/build_manifest.py`, which reads Git **object stores** and never
a working tree, so a locally reformatted or re-encoded file cannot substitute
for the pinned bytes. It refuses to fall back to `main`.

| repository | pinned commit | role |
|---|---|---|
| `mountain/aeg-paper` | PR 16 head `3b90a423…`, base `dd7b93e5…`, merge `735695cb…` | governance-reviewed mathematical status and cross-repository witnesses |
| `mountain/adva` | `cce73004…` (PR 16 reproduction), `1b9bd090…` (new-experiment candidate) | implementation tied to the native program core |
| `mountain/process-geometry` | `c47c96fa…` | non-arithmetic process, continuation equivalence, objectification |

30 files are pinned with Git blob and SHA-256. The work plan's expected values
for `programs/bootstrap-0/first-trace-arithmetic.adva` are re-derived and
compared: 10 682 bytes, blob `de247cd0…`, SHA-256 `637c2d05…` — all agree.

## Reproducing everything

Three sibling checkouts are required, and each is resolved from an environment
variable so the programme is not tied to one machine:

| variable | default | used by |
|---|---|---|
| `AEG_PAPER_REPO` | `/Users/mingli/AEG/aeg-paper` | `tools/build_manifest.py` |
| `AEG_ADVA_REPO` | `/Users/mingli/Adva/adva` | `tools/build_manifest.py`, `experiments/adva_continuation_interface.py` |
| `AEG_PROCESS_GEOMETRY_REPO` | `/Users/mingli/AEG/process-geometry` | `tools/build_manifest.py`, the independent routes of exp1 and exp2 |

A missing checkout is a **loud** failure with a coded diagnostic. The programme
never silently skips a cross-repository check, because a skipped check is not a
check. Each external file is re-hashed against its pinned digest at run time, so
a sibling checkout that has drifted cannot pass.

```bash
# 1. Rebuild the pinned-source manifest; nonzero exit means a blocker.
python3 research/process-representation-gap/tools/build_manifest.py \
    --out research/process-representation-gap/evidence/manifest.json

# 2. Re-run every experiment and compare with the recorded evidence.
#    Checks repeated runs, python3 vs python3 -O, and bytes on disk.
python3 research/process-representation-gap/tools/check_determinism.py

# 3. Re-run one experiment and print its evidence.
python3 research/process-representation-gap/experiments/exp2_loop_continuation.py

# 4. Run an independent verification route on its own.
python3 research/process-representation-gap/experiments/exp2_loop_continuation_independent.py

# 5. The CI gate: additionally compare the committed evidence with a fresh run.
python3 research/process-representation-gap/tools/ci_check.py
```

## Continuous integration

`.github/workflows/research-process-representation-gap.yml` runs on any pull
request or push touching this directory. It checks out `aeg-paper` with full
history, fetches the two pinned sibling commits with a depth-1 fetch into a
temporary object store, points the `AEG_*_REPO` variables at them, and runs
`tools/ci_check.py`, which:

* runs the full six-stage chain and requires exit 0;
* requires every experiment's fresh output to match the **committed** evidence,
  modulo the declared provenance keys;
* requires `fixtures/INDEX.json`, `evidence/gap-classification.json` and
  `evidence/interface-promotion.json` to match the committed bytes exactly.

All three repositories are public, so no cross-repository secret is needed. A
missing or drifted checkout fails the job; it is never skipped, because a
skipped check is not a check.

Exit code 0 means every obligation held. A failure raises a diagnostic with a
stable machine-readable code; the code is the contract, and negative controls
name the exact code they expect.

## Rules this programme enforces on itself

* **Exact arithmetic only.** Integers, `fractions.Fraction`, strings, tuples.
  No float carries a witness, a comparison, or a cost.
* **No `assert`.** CPython strips assertions under `-O`, so a checker that
  relies on them silently stops checking. Every obligation raises a coded
  diagnostic instead.
* **Contracts freeze before implementation.** A contract is frozen by a digest
  in `contracts/FROZEN.sha256`; a changed requirement becomes a **new version
  file** with the old results retained. `exp2-loop-continuation.v1.json` is kept
  beside the current `v1.1.json` for exactly this reason.
* **Independence is structural.** Each experiment has a second checker that
  shares no semantic helper with the first — only JSON serialisation. Two
  checkers calling the same helper are one checker.
* **Determinism is checked, not asserted.** Byte-identical across repeated runs,
  across `python3` / `python3 -O`, and across `PYTHONHASHSEED` values. The seed
  sweep is not decoration: CPython randomises string hashing per process, so a
  checker whose output depends on set or dict iteration order varies between
  processes while looking stable within one running process.
* **One transient failure is on the record.** During development the harness
  once reported `identical_across_runs: false` for
  `exp3_typed_hole_context_independent.py`. It did not reproduce, and every
  checker is currently stable across repeated runs, both execution modes and
  the seed sweep. Rather than declare it spurious, the assertion it tripped was
  strengthened to a seed sweep so that a defect of that class cannot hide
  again. See `reports/00-verification.md`.
* **Claims carry their domain.** Every result is labelled proved /
  proved-with-stated-hypotheses / computationally-verified-example /
  structural-proposal / bounded-domain-compatible / budget-exhausted / unknown /
  open, and a finite enumeration is never upgraded into a general theorem.

## Status vocabulary

| label | meaning in this directory |
|---|---|
| proved | a general argument is written down, with its hypotheses |
| computationally verified example | an exact finite computation, reproducible from the evidence |
| bounded-domain compatible | no counterexample inside the declared budget; **not** a theorem |
| budget exhausted | the declared search bound was reached; the conclusion is restricted to it |
| unknown | the declared model cannot decide it |
| open | carried forward, with the exact missing hypothesis |

## One thing this programme does *not* do

It does not modify the pinned repositories, does not promote any claim into the
AEG manuscripts, and does not change any frozen audit, theorem, label or
notation. Work-plan section 10 requires research evidence first and interface
promotion only afterwards, through the repositories' own governance. Every
consequence for another repository is written down in
`reports/00-minimal-repair.md` as a *proposal with its regression condition*,
not as an applied change.
