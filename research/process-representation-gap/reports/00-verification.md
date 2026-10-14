# 00 — Verification, reproducibility, and one honest anomaly

Work-plan sections 7 and 11. Everything in this programme is replayable from
three pinned checkouts with one command, and this report states exactly what was
verified, on what, and what was observed that is not yet explained.

## 1. The single command

```bash
python3 research/process-representation-gap/tools/verify_all.py
```

It chains six stages and returns one exit code:

| stage | what it proves |
|---|---|
| `manifest` | all 6 pins and 30 files resolve, and the plan's expected values for the 10 682-byte Adva source agree |
| `freeze-contracts` | the digest ledger matches all 7 frozen contract files |
| `determinism` | every checker is byte-stable across repeated runs, across `python3` / `python3 -O`, and across a `PYTHONHASHSEED` sweep |
| `fixtures` | every extracted witness still matches the evidence it came from |
| `gap-classification` | every cited verdict still has the value the table declares |
| `interface-promotion` | every proposal's citations still verify, and none claims to be applied |

**Result on this machine: `all obligations held`, 13 checkers, 16 evidence
documents.**

## 2. What determinism means here, precisely

Three comparisons, all required:

1. **Repeated runs** in the same mode: byte-identical.
2. **`python3` versus `python3 -O`**: byte-identical. This is why there is no
   `assert` anywhere in the programme — CPython strips assertions under `-O`, so
   a checker that relied on them would silently stop checking while still
   exiting 0.
3. **`PYTHONHASHSEED` sweep** (0 and 1): byte-identical. CPython randomises
   string hashing per process, so a checker whose *output* depends on set or
   dict iteration order differs between processes while looking perfectly stable
   within one. Two runs are not enough to catch that class.

A fourth comparison is deliberately weaker, and the weakness is declared:
**fresh output versus the committed evidence** is compared with the
`environment` block removed. The interpreter version is provenance, not
mathematics, and requiring a particular CPython release would make the evidence
unauditable on any other machine. Within one machine the raw bytes are compared
too, and that result is recorded separately as `byte_identical_to_recorded`.

Derived artefacts — `fixtures/INDEX.json`, `evidence/gap-classification.json`,
`evidence/interface-promotion.json` — carry **no** environment block at all, so
they must reproduce **byte for byte** on any machine.

## 3. The anomaly, stated rather than hidden

During development the harness reported, once:

```
exp3_typed_hole_context_independent.py  identical_across_runs: false
                                        identical_across_modes: false
```

**It did not reproduce.** Immediately afterwards and in every subsequent run,
that checker is byte-stable across repeated runs, across both execution modes,
and across the seed sweep; `matches_recorded_evidence` is true.

What was done about it:

* the observation is recorded here rather than dismissed as noise;
* the assertion it tripped was **strengthened** — the seed sweep was added
  specifically because this class of defect is invisible to two consecutive
  runs;
* an independent probe ran all 13 checkers under `PYTHONHASHSEED` 0, 1 and 97
  and found all 13 stable;
* a second, unrelated environment observation was found and handled: the shell's
  `python3` resolved to **3.14.6** for the early runs and **3.13.5** for later
  ones, on the same machine, because `PATH` differed between invocations. That
  is precisely the machine-dependence the environment-tolerant comparison exists
  for, and no substantive byte changed when the interpreter changed.

**What is not claimed.** The transient is not explained. It is not asserted to
be spurious, and it is not asserted to be a real defect. If it recurs, the
harness now reports `DET-HASH-SEED-UNSTABLE` or `DET-RUN-FAILED` with the
failing seed, which is the information needed to localise it.

## 4. Independence, per experiment

Every experiment has a second checker sharing no semantic helper with the first
— only JSON serialisation, hashing and diagnostics. Two checkers calling the
same helper would be one checker.

| experiment | primary | independent route | agreement |
|---|---|---|---|
| exp1 | plant simulation + summary updater | explicit flux ledger, basis-image matrix route, Cayley–Hamilton | 163/163 fields |
| exp2 | fiber enumeration + abstract update | exact partition-refinement oracle from another repository, plus affine-map algebra | all 5 verdicts, both shortest witnesses |
| exp3 | graph builder, binding, graft receipts | direct substitution-and-evaluation interpreter, no graph ever built | 344 comparisons |
| exp4 | pair algebra `(b,k)*(c,l)` | exact 2×2 upper-triangular matrices over `Q`, BFS-with-dedup enumeration | 87 comparisons |
| exp5 | composite Artin image triples | one generator action at a time on the probe, never forming a composite; Cayley BFS | 43 688 evaluations |
| exp6 | multilinear box-hull separation, spanning-disk linking | closed-form normal equations with exact Lipschitz bounds, signed-crossing linking | 0 disagreements, 20 certificates re-derived |

Two independent routes found real defects — in themselves — during development,
and both are retained as negative controls:
`exp5-reversed-composition-route` (composing automorphisms in the wrong order
reverses the composite, and the routes disagree on the first word of length two)
and `exp2-reversed-composition-route`. That is the mechanism by which the
independence requirement does work rather than decorating.

## 5. Negative controls

105 controls across the programme. Each declares the **specific** diagnostic it
must raise, and the harness checks the code, not "some exception". Controls are
polarity-checked: a control body must *fail*, so its `require` must raise. Four
exp3 controls and four exp5 controls were fixed during development precisely
because they passed silently — a control that cannot fail proves nothing.

Failures observed and fixed during development, kept on the record:

* a mutated substitution table applied to *both* routes agreed trivially, so the
  control proved nothing; it was replaced by a single-route mutation;
* an enumeration-budget control contrasted a declared 5461 against an observed
  5461 and could never fire; it now mutates the alphabet;
* a sign-flip control had inverted polarity and passed on a real difference;
* an exp2 readout control encoded the wrong claim direction.

## 6. Environment requirements

Three sibling checkouts, each resolved from an environment variable:

| variable | default | used by |
|---|---|---|
| `AEG_PAPER_REPO` | `/Users/mingli/AEG/aeg-paper` | `tools/build_manifest.py` |
| `AEG_ADVA_REPO` | `/Users/mingli/Adva/adva` | `tools/build_manifest.py`, the Adva interface probe |
| `AEG_PROCESS_GEOMETRY_REPO` | `/Users/mingli/AEG/process-geometry` | `tools/build_manifest.py`, the independent routes of exp1 and exp2 |

A missing checkout is a **loud** failure with a coded diagnostic. Each external
file is re-hashed against its pinned digest at run time, so a sibling checkout
that has drifted cannot pass.

All three repositories are public, so the CI job needs no cross-repository
secret; it fetches each pinned commit with `git fetch --depth 1 origin <sha>`,
which was verified to resolve both Adva pins into one object store and to
support the tree-path and blob lookups the manifest uses.

## 7. Runtime budget, and a measurement lesson

Measured single-pass cost of the 13 checkers on this machine, under normal load:

| checker | seconds |
|---|---|
| `exp3_typed_hole_context` | 51.3 |
| `exp3_typed_hole_context_independent` | under 45 |
| `exp4_objectification_elevation` | 28.4 |
| `exp1_order_and_mixing_independent` | 25.2 |
| `exp6_knot_deformation_environment` | 1.2 |
| the other eight | under 0.5 each |

The determinism harness runs each checker three times, so a full
`verify_all.py` pass is roughly eight minutes of CPU on an idle machine. The CI
job is given 45 minutes to leave headroom on a shared runner, and an extra
seed sweep is available on demand via `--seeds` rather than being paid for on
every run.

**A measurement lesson, recorded because it nearly produced a wrong report.**
While several verification runs were in flight at once, one checker was
measured at **1036 seconds** and two later timing attempts exceeded ten
minutes. Both were contention artefacts: re-measured alone, the same checker
takes **51.3 seconds**, and a stack sample taken under load showed it running
normally rather than stuck. The same figure was briefly interpreted as a 35x
interpreter-dependent slowdown between CPython 3.13 and 3.14; it was not, and
the interpreter change (section 3) is the only environment difference that
actually occurred.

The lesson is not incidental to this programme: two of the numbers in the
transient investigation were wrong before they were right, and only an
independent re-measurement caught it. That is the same discipline the
experiments apply to their own claims.

## 8. What is *not* verified

* **Not** that the checkers are correct in the mathematical sense. They are
  exact and independently cross-checked; only review settles correctness.
* **Not** that the declared models are the right models. Each is declared, and
  each says what it is not.
* **Not** any unbounded claim. Every result carries its domain and budget.
* **Not** the frozen sibling repositories themselves — nothing in them was
  modified, and no claim is made about their state beyond the pinned commits.
