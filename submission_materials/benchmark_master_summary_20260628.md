# Benchmark Master Summary (2026-06-28)

This note merges the currently accepted benchmark-facing results across the
original formal 12K package, the accepted `LoFTR` retry, and the accepted
protocol-closure outputs. It is the current local source of truth for
benchmark-facing numbers before manuscript-body edits.

## 1. Pairwise Baselines

| Method | Evidence source | H available | H % | Mean inlier ratio | Mean coverage | Median reproj | Mean runtime / pair (s) |
|---|---|---:|---:|---:|---:|---:|---:|
| `sift_ransac` | original formal run | `5257 / 6037` | `87.08%` | `0.242457` | `0.627112` | `0.000376` | `4.420841` |
| `akaze_ransac` | original formal run | `5692 / 6037` | `94.29%` | `0.159959` | `0.730288` | `0.104917` | `1.102855` |
| `loftr_outdoor` | accepted retry | `5984 / 6037` | `99.12%` | `0.073769` | `0.895126` | `0.822623` | `0.168875` |
| `roma_outdoor` | original formal run | `6037 / 6037` | `100.00%` | `0.327633` | `0.997112` | `1.740945` | `0.928936` |
| `xoftr_official` | original formal run | `5989 / 6037` | `99.20%` | `0.089057` | `0.949395` | `1.732160` | `0.646835` |
| `raw_minima` | original formal run | `6037 / 6037` | `100.00%` | `0.319165` | `0.999627` | `1.773367` | `1.345901` |

Important note:

- The original `2026-06-26` formal package contains a failed `LoFTR` run with
  full OOM collapse.
- The accepted benchmark-facing `LoFTR` result must therefore be sourced from:
  `formal_run_evidence_20260626/loftr_retry_20260628/main_outputs/main_experiment_summary.json`

## 2. Scene-Level Canonical Result

Accepted scene-level benchmark result:

- method: `uav_talign_full`
- scene homographies available: `15 / 15`
- canonical retained scenes: `9 / 15`
- retention rate: `60.00%`
- retained scene ids:
  `01,04,05,06,07,08,10,12,14`
- pair coverage micro: `74.44%`
- accepted-attempted ratio micro: `64.71%`
- mean severe-outlier ratio: `0.009259`
- mean robust reject ratio: `0.113163`
- mean delta edge F1: `0.134312`
- mean delta grad NCC: `0.130337`

## 3. Light-Condition Breakdown

| Condition | Retained scenes | Retention |
|---|---:|---:|
| `day` | `5 / 7` | `71.43%` |
| `night` | `3 / 5` | `60.00%` |
| `lowlight` | `1 / 3` | `33.33%` |

## 4. Source Files

- machine-readable summary:
  `submission_materials/benchmark_master_summary_20260628.csv`
- original pairwise + scene summaries:
  `submission_materials/formal_run_evidence_20260626/main_outputs/main_experiment_summary.json`
- accepted LoFTR retry:
  `submission_materials/formal_run_evidence_20260626/loftr_retry_20260628/main_outputs/main_experiment_summary.json`
- canonical scene-level operating point:
  `submission_materials/formal_run_evidence_20260626/protocol_closure/canonical_operating_point.csv`
- condition breakdown:
  `submission_materials/formal_run_evidence_20260626/protocol_closure/condition_reliability_profile.csv`
