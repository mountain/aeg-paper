# Baseline — pinned sources, reproduction, and the PR-16 witness

Generated from `evidence/manifest.json` by `tools/build_manifest.py`. Every
hash below was read from a Git **object store**, never from a working tree, so
a locally reformatted or re-encoded copy cannot stand in for the pinned bytes.
The builder exits non-zero if any pin is missing; it never falls back to `main`.

## 1. Pins

| repository | label | commit |
|---|---|---|
| `mountain/aeg-paper` | PR-16 review head | `3b90a423fafc2a838269855c8c68286449c61c4c` |
| `mountain/aeg-paper` | PR-16 base | `dd7b93e5eda57343e1ff05ed954883db310eda1d` |
| `mountain/aeg-paper` | merge main | `735695cbc7ce512a1cd5e188577613eda4b3083c` |
| `mountain/adva` | PR-16 reproduction | `cce73004c2b4fbfb87d9ba1ccc66820423273cf6` |
| `mountain/adva` | new-experiment candidate | `1b9bd090b2c4710916b6a0ccca0ad88fb7d323bd` |
| `mountain/process-geometry` | baseline | `c47c96fa79123c677172278be59d67ca1cc891b1` |

All six pins resolve locally. The isolated worktree for this work sits at the
merge commit `735695cb…`, so the PR-16 witness document and its fixtures are
present as committed.

## 2. Plan expected values, re-derived

Work-plan section 2.1 fixes three values for
`programs/bootstrap-0/first-trace-arithmetic.adva` and requires them to be
checked against the **raw Git blob bytes**, not a newline-normalised or
re-encoded copy.

| quantity | plan expectation | observed | agrees |
|---|---|---|---|
| byte length | 10 682 | 10 682 | yes |
| Git blob | `de247cd071f714e14a91b0e54a9bab77b0de43e9` | `de247cd071f714e14a91b0e54a9bab77b0de43e9` | yes |
| SHA-256 | `637c2d05663fcee780156d93f4f9e19f829418213a4948c91113141b64d3a579` | same | yes |

Independently, the same bytes appear inside the aeg-paper fixture
`paper-4/scripts/fixtures/opposite-features/adva-0114.json`, whose SHA-256 is
also `637c2d05…`. So the transport bytes are identical on both sides of the
cross-repository witness.

## 3. The 30 pinned files

### `mountain/adva` (5 files, at `1b9bd090…`)

| sha256 | bytes | git blob | path |
|---|---|---|---|
| `edbc7da2c771` | 14 318 | `faaa17bb513b` | `docs/PROGRAM_PROCESS_CORE.md` |
| `06a236fde470` | 29 903 | `d7ab72b2d9d5` | `docs/TECHNICAL_REPORT_PROGRAM_PROCESS_CORE.md` |
| `ffa6ff6729fb` | 17 255 | `b5e44e805c42` | `docs/research/0233-periodic-programs-before-floquet-observations.md` |
| `9d377f2f5a4f` | 4 045 | `f175b123d659` | `docs/research/0114-three-sided-trace-arithmetic-calibration.md` |
| `637c2d05663f` | 10 682 | `de247cd071f7` | `programs/bootstrap-0/first-trace-arithmetic.adva` |

### `mountain/aeg-paper` (12 files, at `735695cb…`)

| sha256 | bytes | git blob | path |
|---|---|---|---|
| `f53de804f439` | 19 777 | `7b212abd1337` | `AGENTS.md` |
| `bdd983477e51` | 9 256 | `4bcc9f2eb374` | `README.md` |
| `75c5a24dcfc6` | 97 980 | `5f93799557a3` | `governance/05-mathematical-status.md` |
| `487c40648c25` | 96 326 | `884ac913c65d` | `governance/08-open-questions.md` |
| `d75a90c1d95d` | 9 266 | `abb01561d0b3` | `governance/opposite-feature-witness-2026-10-09.md` |
| `379475ec7e4e` | 9 302 | `27e348f8333a` | `paper-4/README.md` |
| `c39d66c42140` | 22 676 | `6229d09f089d` | `paper-4/sections/05b-ported-aes-programs.tex` |
| `63f8423b439f` | 9 343 | `115aaf6a6ef3` | `paper-4/sections/05-contextual-residuals.tex` |
| `fb1b23327ff9` | 7 386 | `47648a5ad9d2` | `paper-4/scripts/verify-opposite-features.py` |
| `8a9a97e457ab` | 43 506 | `6f0a486336df` | `paper-4/scripts/verify-ported-aes.py` |
| `637c2d05663f` | 10 682 | `de247cd071f7` | `paper-4/scripts/fixtures/opposite-features/adva-0114.json` |
| `62c9e9505085` | 25 001 | `d9adca9ce839` | `paper-4/scripts/fixtures/opposite-features/evidence.json` |

### `mountain/process-geometry` (13 files, at `c47c96fa…`)

| sha256 | bytes | git blob | path |
|---|---|---|---|
| `341fc288e4dc` | 22 124 | `95a9ff375c40` | `README.md` |
| `b172fd58da06` | 23 045 | `e0e96fe53c17` | `docs/RESEARCH_STATUS.md` |
| `0bd0207bdf54` | 41 363 | `16ac11f52e6a` | `docs/ENGINEERING_ARCHITECTURE.md` |
| `ff063d2f8c7d` | 17 319 | `22323f2e3b3c` | `docs/RESEARCH_PROGRAM.md` |
| `a0b965621a6d` | 52 461 | `e0bc0a81f32a` | `docs/MATHEMATICAL_CORE.md` |
| `ad364fcda718` | 8 829 | `4cc9ad42b997` | `docs/00-process-presentation-v0.1.md` |
| `b0100dba1423` | 9 224 | `5c7f8d7b7b1f` | `docs/06-addition-multiplication-function-theory.md` |
| `f50600f58ff5` | 16 056 | `bbc02aab3c92` | `docs/51-aeg-addition-multiplication-rank-transition.md` |
| `ab1a46d8da91` | 11 306 | `2ddd71f74934` | `docs/50-aeg-translation-objectification-rank-lowering.md` |
| `02b8c8279330` | 19 235 | `f745e6d22ab5` | `docs/44-objectification-semantic-compression-and-rank-lowering.md` |
| `93e9dc4651f4` | 1 359 | `0d1f1895744f` | `src/process_geometry/process/history.py` |
| `1b2bf6a4510f` | 12 181 | `a381c47822ba` | `src/process_geometry/experimental/finite_task_quotient.py` |
| `e59c8a1b0ba2` | 5 600 | `12e457428041` | `src/process_geometry/signature.py` |

The last three are used as *executable* pins: experiment 1 loads `ProcessWord`
from `process/history.py`, and experiment 2's independent route loads
`minimize_finite_task_process` from `finite_task_quotient.py`. Each checker
re-hashes its pinned file at run time and raises a coded diagnostic on drift,
so a cross-repository dependency cannot change underneath the evidence.

## 4. Reproduction of the PR-16 witness

Run inside the worktree, at `735695cb…`:

```bash
python3 paper-4/scripts/verify-opposite-features.py > /tmp/opposite.json
cmp /tmp/opposite.json paper-4/scripts/fixtures/opposite-features/evidence.json
python3 -O paper-4/scripts/verify-opposite-features.py > /tmp/opposite-O.json
cmp /tmp/opposite.json /tmp/opposite-O.json
```

Result: **the emitted bytes are identical to the frozen fixture**, and identical
under `-O`. The witness reproduces bit-exact from the pinned commit.

The witness's own claims, as registered in `governance/05-mathematical-status.md`:

| id | status | statement |
|---|---|---|
| `PIV-S8` | `COMPUTATIONALLY VERIFIED EXAMPLE` | the pinned Adva 0114 adapter retains source, events, residual and policy; four Q snapshot producers fill a strict finite body yielding `(3,1,2)` on both paths; the packet observation separates equal scalar outputs |
| `PIV-S9` | `PROVED WITH STATED HYPOTHESES` | on the two frozen records with the declared 0114 projection policy, equal `(T,S)` and unequal `C` exclude any function `C = chi_C(T,S)` |
| `PIV-F2` | `OPEN PROBLEM` | `chi_T` and `chi_S` have only two-record sample consistency; faithful AES gate motions, spectral operator closure, truth-fiber and cyclic update semantics remain open |

## 5. What this baseline does *not* establish, and the one correction recorded

Two attributions had to be fixed before any experiment could cite them:

1. **The three-scalar body `y1 = c+v`, `y2 = f−h`, `y3 = 3h/f` is a declared
   adapter, not an Adva output.** It is defined in the aeg-paper PR-16 script
   `paper-4/scripts/verify-opposite-features.py`. It is **not** the output of
   Adva research 0114, whose own coordinates are time, space and construction.
   Experiment 2's probe `experiments/adva_continuation_interface.py` verifies
   this attribution directly: the body occurs **zero** times in the pinned Adva
   tree.
2. **`PR-16` is an aeg-paper identifier, not an Adva one.** The literal string
   does not occur anywhere in the pinned Adva tree. The Adva-side referents of
   the two records are `docs/research/0114-…`, ADR 0023/0024, and
   `programs/bootstrap-0/first-trace-arithmetic.adva`.

Neither correction weakens PR-16. Both sharpen what it may be cited for, which
is what the work plan asks of a frozen baseline.

## 6. Blockers

None. `tools/build_manifest.py` exits 0 with `blockers: []`.
