# Paper Table / Figure Checklist (2026-06-28)

This checklist is for the current local evidence state. It does not mean the
paper body has been updated; it only marks whether the corresponding evidence is
already paper-safe, partially ready, or still blocked.

## Main Paper

| Item | Status | Current source | Notes |
|---|---|---|---|
| Pairwise benchmark main table | Ready | `benchmark_master_summary_20260628.csv` | `LoFTR` must come from retry package |
| `uav_talign_full` scene-level main table | Ready | `benchmark_master_summary_20260628.md` + `protocol_closure/canonical_operating_point.csv` | Canonical retained scenes fixed |
| Light-condition breakdown table | Ready | `protocol_closure/condition_reliability_profile.csv` | `day / night / lowlight` rows fixed |
| Risk-coverage figure | Ready | `protocol_closure/risk_coverage.csv` | Current PNG exists; can be redrawn later if needed |
| Threshold sensitivity figure / supplement table | Ready | `protocol_closure/threshold_sensitivity.csv` | Current PNG exists |
| Method narrative paragraph | Ready for drafting | `collaborator_result_brief_zh_20260628.md` | Can support collaborator writing |

## Supplement

| Item | Status | Current source | Notes |
|---|---|---|---|
| Per-scene reliability table | Ready | `protocol_closure/per_scene_reliability_table.csv` | Accepted |
| Condition reliability table | Ready | `protocol_closure/condition_reliability_profile.csv` | Accepted |
| Reliability-score design note | Ready | `protocol_closure/reliability_score_design.md` | Accepted |
| Protocol summary note | Ready | `protocol_closure/paper_facing_summary.md` | Accepted |
| LoFTR accepted retry evidence | Ready | `formal_run_evidence_20260626/loftr_retry_20260628/` | Use this instead of failed original package |
| Ablation summary table | Ready | `supplement_run_evidence_20260629/ablation/ablation_summary_20260629.md` | 4 accepted stages locally frozen |
| Multi-seed sensitivity table | Ready | `supplement_run_evidence_20260629/multiseed/multiseed_summary_20260629.md` | 4 accepted seeds locally frozen |

## Still Pending Or Blocked

| Item | Status | Why not ready | What is needed |
|---|---|---|---|
| `RIFT2` benchmark row | Pending decision | Not frozen in current accepted evidence structure | Keep/remove decision, then formal evidence if kept |
| Final merged paper tables | Pending | We have evidence, but not yet the final paper-facing formatted tables | Build final paper-ready table set |

## Current Writing Rule

Use the following local files as the primary writing layer:

- `submission_materials/benchmark_master_summary_20260628.csv`
- `submission_materials/benchmark_master_summary_20260628.md`
- `submission_materials/benchmark_table_figure_source_map_20260628.md`
- `submission_materials/collaborator_result_brief_zh_20260628.md`

Do not use the original failed LoFTR JSONL as a benchmark source.
