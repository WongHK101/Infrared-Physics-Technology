# Paper-Ready Benchmark Tables Draft (2026-06-28)

This file is a paper-facing table draft layer generated from the currently
accepted local evidence. It is still outside the manuscript body, but it is
closer to the final presentation style than the raw benchmark master summary.

## Table A. Pairwise Baseline Comparison on UAV-TAlign-12K

All methods are evaluated on the official `6037`-pair manifest-filtered split.
`LoFTR` is sourced from the accepted standalone retry package rather than the
original failed formal package.

| Method | H avail. (%) | Mean inlier ratio | Mean coverage | Median reproj. error | Runtime / pair (s) |
|---|---:|---:|---:|---:|---:|
| SIFT | `87.08` | `0.242` | `0.627` | `0.000` | `4.421` |
| AKAZE | `94.29` | `0.160` | `0.730` | `0.105` | `1.103` |
| LoFTR | `99.12` | `0.074` | `0.895` | `0.823` | `0.169` |
| RoMa | `100.00` | `0.328` | `0.997` | `1.741` | `0.929` |
| XoFTR | `99.20` | `0.089` | `0.949` | `1.732` | `0.647` |
| raw MINIMA | `100.00` | `0.319` | `1.000` | `1.773` | `1.346` |

Local evidence sources:

- main accepted package:
  `submission_materials/formal_run_evidence_20260626/main_outputs/main_experiment_summary.json`
- accepted `LoFTR` retry:
  `submission_materials/formal_run_evidence_20260626/loftr_retry_20260628/main_outputs/main_experiment_summary.json`

## Table B. Scene-Level Canonical Result of UAV-TAlign

| Method | Scene homographies | Retained scenes | Retention (%) | Pair coverage (%) | Accepted-attempted ratio (%) |
|---|---:|---:|---:|---:|---:|
| UAV-TAlign | `15 / 15` | `9 / 15` | `60.00` | `74.44` | `64.71` |

Retained scene ids:

- `01,04,05,06,07,08,10,12,14`

Additional canonical-operating-point diagnostics:

- mean severe-outlier ratio: `0.009`
- mean robust reject ratio: `0.113`
- mean delta edge F1: `0.134`
- mean delta grad NCC: `0.130`

Local evidence source:

- `submission_materials/formal_run_evidence_20260626/protocol_closure/canonical_operating_point.csv`

## Table C. Light-Condition Breakdown

| Light condition | Retained scenes | Retention (%) |
|---|---:|---:|
| Day | `5 / 7` | `71.43` |
| Night | `3 / 5` | `60.00` |
| Low-light | `1 / 3` | `33.33` |

Local evidence source:

- `submission_materials/formal_run_evidence_20260626/protocol_closure/condition_reliability_profile.csv`

## Presentation Notes

- If we later decide to restore `RIFT2` into the benchmark main table, it should
  be inserted into Table A only after a local accepted evidence pack is frozen.
- The current draft intentionally separates pairwise baseline evidence from the
  scene-level canonical result, because they correspond to different benchmark
  tracks.
- The current draft is suitable for direct manuscript adaptation, but the exact
  wording and decimal precision can still be adjusted when we move into the
  paper body.
