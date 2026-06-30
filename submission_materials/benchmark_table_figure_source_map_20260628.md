# Benchmark Table / Figure Source Map (2026-06-28)

This note maps the benchmark-facing tables and figures to the current accepted
local evidence files. It is intended to prevent later confusion when numbers are
moved into the paper or supplement.

## Main Benchmark Table

Recommended local source:

- `submission_materials/benchmark_master_summary_20260628.csv`

Underlying evidence:

- pairwise methods except `LoFTR`:
  `submission_materials/formal_run_evidence_20260626/main_outputs/main_experiment_summary.json`
- accepted `LoFTR`:
  `submission_materials/formal_run_evidence_20260626/loftr_retry_20260628/main_outputs/main_experiment_summary.json`

Important rule:

- Do not source `LoFTR` numbers from the original failed
  `formal_run_evidence_20260626/main_outputs/loftr_outdoor_results.jsonl`.

## Scene-Level Main Result Table

Recommended local source:

- `submission_materials/benchmark_master_summary_20260628.md`

Underlying evidence:

- `submission_materials/formal_run_evidence_20260626/protocol_closure/canonical_operating_point.csv`
- `submission_materials/formal_run_evidence_20260626/main_outputs/main_experiment_summary.json`

## Light-Condition Breakdown Table

Underlying evidence:

- `submission_materials/formal_run_evidence_20260626/protocol_closure/condition_reliability_profile.csv`

Rows to use:

- `group_by = light_condition`
- `group = day`
- `group = night`
- `group = lowlight`

## Risk-Coverage Figure

Underlying evidence:

- `submission_materials/formal_run_evidence_20260626/protocol_closure/risk_coverage.csv`
- current preview figure:
  `submission_materials/formal_run_evidence_20260626/protocol_closure/risk_coverage_curve.png`

## Threshold Sensitivity Figure / Supplement Table

Underlying evidence:

- `submission_materials/formal_run_evidence_20260626/protocol_closure/threshold_sensitivity.csv`
- current preview figure:
  `submission_materials/formal_run_evidence_20260626/protocol_closure/threshold_sensitivity.png`

## Per-Scene Reliability Supplement Table

Underlying evidence:

- `submission_materials/formal_run_evidence_20260626/protocol_closure/per_scene_reliability_table.csv`

## Condition Reliability Supplement Table

Underlying evidence:

- `submission_materials/formal_run_evidence_20260626/protocol_closure/condition_reliability_profile.csv`

## Ablation Summary Table

Recommended local source:

- `submission_materials/supplement_run_evidence_20260629/ablation/ablation_summary_20260629.md`

Underlying evidence:

- `submission_materials/supplement_run_evidence_20260629/ablation/prcv_ablation_A1_candidate_only/main_experiment_summary.json`
- `submission_materials/supplement_run_evidence_20260629/ablation/prcv_ablation_A2_candidate_plus_aggregation/main_experiment_summary.json`
- `submission_materials/supplement_run_evidence_20260629/ablation/prcv_ablation_A3_candidate_plus_aggregation_plus_qa/main_experiment_summary.json`
- `submission_materials/supplement_run_evidence_20260629/ablation/prcv_ablation_S1_random_selection_seed0/main_experiment_summary.json`

## Multi-Seed Sensitivity Table

Recommended local source:

- `submission_materials/supplement_run_evidence_20260629/multiseed/multiseed_summary_20260629.md`

Underlying evidence:

- `submission_materials/supplement_run_evidence_20260629/multiseed/prcv_ablation_S1_random_selection_seed0/main_experiment_summary.json`
- `submission_materials/supplement_run_evidence_20260629/multiseed/prcv_ablation_S1_random_selection_seed1/main_experiment_summary.json`
- `submission_materials/supplement_run_evidence_20260629/multiseed/prcv_ablation_S1_random_selection_seed2/main_experiment_summary.json`
- `submission_materials/supplement_run_evidence_20260629/multiseed/prcv_ablation_S1_random_selection_seed3/main_experiment_summary.json`

## Remaining Unmapped Or Not Yet Frozen

- `RIFT2` full 12K benchmark evidence

This remaining item should not yet be treated as fully paper-safe until its
local frozen evidence pack is created and added to this mapping note.
