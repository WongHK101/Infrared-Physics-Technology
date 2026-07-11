# LoFTR Retry Evidence (2026-06-28)

This sub-bundle stores the accepted `LoFTR-only` retry evidence that was
generated after the original formal run exposed a full CUDA OOM collapse for
`loftr_outdoor`.

## Provenance

- Execution host: isolated Windows workstation with an NVIDIA RTX 4090
- Remote code root: `G:\UAV-TAlign\UAV-TAlign`
- Remote retry output root:
  `G:\UAV-TAlign\UAV-TAlign\outputs\ipt_p0c_12k_loftr_retry_20260626_140300`
- Retry launch audit:
  `G:\UAV-TAlign\_audit\loftr_retry_launch_20260626_140003`
- Official manifest canonical SHA256:
  `a092f7ad00c6e02ead3bd39de5c246001f1d4bebbc4105ba715ef37bbb202c6c`

## Acceptance Status

- Launcher summary recorded `exit_code=0`.
- Validator recorded `ok=true`.
- Runtime stderr files are empty.
- The raw `loftr_outdoor/results.jsonl` copied here is complete:
  `6037` lines, SHA256
  `4acd4a145919754df41ee3c292b5fd92d35c647cc461a1fc1e5c9b5cd91f2387`.

## Execution Profile

The accepted retry used the memory-safe LoFTR profile that we fixed into the
benchmark launcher and validator flow:

- `methods = loftr_outdoor`
- `device = cuda:0`
- `loftr_match_max_dim = 1200`
- `loftr_use_amp = true`
- `seed = 0`
- `resume = false`

## Accepted Result Snapshot

- `6037 / 6037` records processed
- `5984` `ok`
- `13` `fit_failed`
- `35` `insufficient_matches`
- `5` `no_matches`
- `0` `error`
- `homography_available_count = 5984`
- `H availability = 99.1221%`

Main metric summaries from `main_experiment_summary.json`:

- mean inlier ratio: `0.07376900876141765`
- mean coverage: `0.8951258903428856`
- median reprojection error: `0.8226231932640076`
- mean runtime / pair: `0.1688754416783756`

## Folder Map

- `main_outputs/`
  Retry experiment summary, launcher summary, validator output, and the copied
  complete `loftr_outdoor` JSONL.
- `remote_audit/`
  Local acceptance note and SHA256 manifest for the copied retry evidence.

## Primary Files

- `main_outputs/main_experiment_summary.json`
- `main_outputs/validate_stdout.json`
- `main_outputs/launcher_summary.txt`
- `main_outputs/loftr_outdoor_results.jsonl`
