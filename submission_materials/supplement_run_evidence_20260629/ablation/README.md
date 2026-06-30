# Ablation Evidence Freeze

This directory contains the accepted local freeze of the rerun ablation wave
from the remote supplement bundle.

Accepted stages:

- `prcv_ablation_A1_candidate_only`
- `prcv_ablation_A2_candidate_plus_aggregation`
- `prcv_ablation_A3_candidate_plus_aggregation_plus_qa`
- `prcv_ablation_S1_random_selection_seed0`

For each stage, the frozen local evidence includes:

- `experiment_config.json`
- `main_experiment_summary.json`
- `_stage_stdout.txt`
- `_stage_stderr.txt`
- `uav_talign_full_scene_metrics_detailed.jsonl`
- `uav_talign_full/results.json`
- `uav_talign_full/results.jsonl`
- `uav_talign_full/scene_results.jsonl`
- 8 per-scene `scene_result.json` files

Integrity note:

- `sha256_manifest.txt` records the local digest list for the frozen files

Writing note:

- Use the local summary note and table in this directory as the paper-facing
  starting point, not the raw logs.
