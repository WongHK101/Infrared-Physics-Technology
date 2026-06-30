# Unified Benchmark Evidence and Writing Map (2026-06-29)

This note merges the currently accepted evidence into one writing-oriented map.
It is intentionally manuscript-adjacent, but it does not edit the manuscript
body. Its purpose is to prevent later mixing of:

- accepted benchmark evidence
- deferred benchmark rows
- outdated manuscript draft numbers
- newly accepted supplement evidence

## 1. Current Accepted Evidence Blocks

The current benchmark-support layer is composed of four accepted blocks:

1. Main formal 12K benchmark evidence
   - `submission_materials/formal_run_evidence_20260626/`
2. Accepted LoFTR retry evidence
   - `submission_materials/formal_run_evidence_20260626/loftr_retry_20260628/`
3. Protocol-closure evidence
   - `submission_materials/formal_run_evidence_20260626/protocol_closure/`
4. Supplement freeze evidence
   - `submission_materials/supplement_run_evidence_20260629/`

These four blocks are now sufficient to support:

- pairwise benchmark table writing
- scene-level main result writing
- reliability / risk-coverage writing
- ablation writing
- multi-seed sensitivity writing

## 2. One-Sentence Project Positioning

The manuscript should present UAV-TAlign-12K as a real captured, cross-FOV UAV
infrared-visible benchmark in which pairwise homography evidence is broadly
available, but the main operating question is whether scene-level transforms
should be retained under reliability control.

That positioning is already supported by the accepted evidence.

## 3. Writing-Safe Source of Truth

Use the following files as the writing-safe source of truth:

- pairwise + scene summary:
  `submission_materials/benchmark_master_summary_20260628.md`
- machine-readable writing layer:
  `submission_materials/benchmark_master_summary_20260628.csv`
- table / figure source map:
  `submission_materials/benchmark_table_figure_source_map_20260628.md`
- supplement acceptance note:
  `submission_materials/supplement_run_status_note_20260629.md`
- ablation summary:
  `submission_materials/supplement_run_evidence_20260629/ablation/ablation_summary_20260629.md`
- multi-seed summary:
  `submission_materials/supplement_run_evidence_20260629/multiseed/multiseed_summary_20260629.md`

## 4. Current Writing-Safe Main Numbers

### 4.1 Dataset and protocol

- candidate pairs: `6039`
- valid evaluation pairs: `6037`
- scenes: `15`
- official manifest hash anchored
- main benchmark unit: pairwise homography evidence
- complementary benchmark unit: scene-level retained alignment

### 4.2 Pairwise benchmark rows currently safe to write

Accepted pairwise rows already frozen in the local benchmark layer:

- `SIFT`: `5257/6037`, `87.08%`
- `AKAZE`: `5692/6037`, `94.29%`
- `LoFTR` accepted retry: `5984/6037`, `99.12%`
- `RoMa`: `6037/6037`, `100.00%`
- `XoFTR`: `5989/6037`, `99.20%`
- `raw MINIMA`: `6037/6037`, `100.00%`

### 4.3 Scene-level main result currently safe to write

- scene homographies available: `15/15`
- canonical retained scenes: `9/15`
- retention rate: `60.00%`
- pair coverage micro: `74.44%`
- accepted-attempted ratio micro: `64.71%`

### 4.4 Condition breakdown currently safe to write

- day: `5/7`, `71.43%`
- night: `3/5`, `60.00%`
- lowlight: `1/3`, `33.33%`

### 4.5 Supplement results currently safe to write

Ablation:

- `A1`: `8/8`
- `A2`: `8/8`
- `A3`: `5/8`
- `S1_seed0`: `5/8`

Multi-seed:

- `seed0`: `5/8`
- `seed1`: `5/8`
- `seed2`: `7/8`
- `seed3`: `5/8`

## 5. Important Non-Writing-Safe Item

`RIFT2` is the one major row that should currently be treated as:

- numerically known in draft materials
- not yet frozen in the same accepted local evidence structure

So the current writing rule is:

- do not let `RIFT2` block collaborator writing
- do not rely on `RIFT2` as a mandatory benchmark row until a formal local
  accepted evidence pack is frozen

## 6. Known Draft-vs-Evidence Conflicts

The current manuscript draft still contains several numbers or claims that do
not match the accepted local evidence layer.

### 6.1 `LoFTR` conflict

Draft currently shows:

- `6009/6037`, `99.54%`

Accepted local evidence shows:

- `5984/6037`, `99.12%`

Writing rule:

- use the accepted retry package only
- do not use the old manuscript draft row

### 6.2 `RIFT2` conflict

Draft currently treats `RIFT2` as already part of the paper-safe main table.

Project evidence status shows:

- `RIFT2` remains deferred unless we explicitly freeze a formal accepted local
  evidence pack

Writing rule:

- either remove `RIFT2` from the next writing pass
- or reopen `RIFT2` evidence freeze before final manuscript lock

### 6.3 Scene-level accepted-frame conflict

Draft main table currently shows:

- `2473/3847`, `64.3`

Accepted canonical evidence shows:

- pair coverage micro: `74.44%`
- accepted-attempted ratio micro: `64.71%`

Writing rule:

- if accepted frames are shown in the main table, they must be re-derived from
  the accepted protocol-closure source instead of copied from the old draft row

### 6.4 Multi-seed spread conflict

Draft currently states:

- random-selection spread is `4/8` to `7/8`

Accepted frozen supplement shows:

- current frozen spread is `5/8` to `7/8`

Writing rule:

- use `5/8` to `7/8` for the currently accepted supplement evidence

## 7. Recommended Writing Position on `seed2`

The safest interpretation of the accepted multi-seed evidence is:

- the random-selection supplement shows non-trivial scene-level sensitivity
- the main variation occurs in strict canonical scene pass, not in accepted
  frame mean
- `seed2` is better mainly because a small number of borderline scenes cross
  the QA-gated pass boundary

This means we should avoid overselling the seed result as a large-scale
instability of the method. It is better framed as:

- boundary sensitivity under random evidence selection
- support for deterministic-even selection as a reproducible default policy

## 8. Best Current Paper Narrative

The strongest current paper narrative is:

1. UAV-TAlign-12K broadens multimodal registration benchmarking from pairwise
   matching toward retained scene-level alignment.
2. Pairwise evidence is already broadly available with strong off-the-shelf
   baselines.
3. The main challenge therefore shifts to scene-level aggregation, reliability
   control, and acceptance policy.
4. The ablation and multi-seed results support that robust scene consensus and
   QA-aware verification are the primary drivers, while deterministic-even
   selection provides reproducible behavior.

## 9. Immediate Writing Guidance

For the next collaborator handoff, use this decision rule:

- write the paper around the accepted 6-row pairwise benchmark
- keep the accepted scene-level 9/15 canonical result as the core main-method
  result
- use the ablation and multi-seed supplement only to strengthen the method
  explanation
- treat `RIFT2` as optional until its evidence is frozen
