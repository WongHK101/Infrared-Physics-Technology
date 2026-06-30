# Ablation / Multi-Seed Output Audit (2026-06-28, updated 2026-06-29)

This note records the final audit state for the supplementary ablation and
multi-seed outputs after the accepted rerun and local evidence freeze.

## 1. Final Accepted Remote Bundle

Accepted remote bundle:

- `G:\UAV-TAlign\UAV-TAlign\outputs\ipt_p3p5_supplement_bundle_20260629_133127`

Accepted remote launcher status:

- `worker_started_at=2026-06-29 13:31:27`
- `worker_finished_at=2026-06-29 14:30:01`
- `exit_code=0`

## 2. Final Local Freeze Result

Accepted local freeze root:

- `submission_materials/supplement_run_evidence_20260629/`

Frozen subdirectories:

- `submission_materials/supplement_run_evidence_20260629/ablation/`
- `submission_materials/supplement_run_evidence_20260629/multiseed/`
- `submission_materials/supplement_run_evidence_20260629/remote_audit/`

## 3. Completeness Audit

The following accepted stages were frozen locally:

- ablation:
  `A1_candidate_only`, `A2_candidate_plus_aggregation`,
  `A3_candidate_plus_aggregation_plus_qa`, `S1_random_selection_seed0`
- multi-seed:
  `seed0`, `seed1`, `seed2`, `seed3`

For every accepted stage / seed, the local freeze now contains:

- `experiment_config.json`
- `main_experiment_summary.json`
- `_stage_stdout.txt`
- `_stage_stderr.txt`
- `uav_talign_full_scene_metrics_detailed.jsonl`
- `uav_talign_full/results.json`
- `uav_talign_full/results.jsonl`
- `uav_talign_full/scene_results.jsonl`
- 8 per-scene `scene_result.json`

Integrity manifests were also generated:

- `ablation/sha256_manifest.txt`
- `multiseed/sha256_manifest.txt`
- `remote_audit/sha256_manifest.txt`

## 4. Final Conclusion

The two previously pending supplement items should now be treated as:

- **ablation wave: evidence frozen**
- **multi-seed supplement: evidence frozen**

So the former state:

- **evidence not yet frozen**

is no longer current.

## 5. Writing-Phase Implication

These supplement outputs are now suitable to support:

1. local collaborator handoff
2. benchmark design closure checks
3. later manuscript tables or supplement notes

They still remain outside the paper body until we explicitly decide the final
presentation format.
