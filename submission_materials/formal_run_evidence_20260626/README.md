# Formal Run Evidence Bundle (2026-06-26)

This bundle stores the key evidence pulled back from the remote Windows 4090
host after the formal `UAV-TAlign-12K` run completed.

## Provenance

- Remote host: `ssh Administrator@100.103.212.54`
- Remote code root: `G:\UAV-TAlign\UAV-TAlign`
- Remote raw-output root: `G:\UAV-TAlign\UAV-TAlign\outputs\ipt_p0c_12k_main`
- Remote protocol-closure root:
  `G:\UAV-TAlign\UAV-TAlign\outputs\ipt_p0d_protocol_closure`
- Remote acceptance audit:
  `G:\UAV-TAlign\_audit\p2d_acceptance_20260626_111420`
- Git commit:
  `c55e39e49cda508bae68520f718894bb0c761cec`
- Official manifest canonical SHA256:
  `a092f7ad00c6e02ead3bd39de5c246001f1d4bebbc4105ba715ef37bbb202c6c`

## Acceptance Status

- Main experiment launcher finished with `exit_code=0`.
- Main output validator reported `ok=true`.
- Protocol-closure postprocessing was regenerated successfully.
- `loftr_outdoor` has since been repaired by an accepted standalone retry
  evidence bundle under `loftr_retry_20260628/`.
- Raw evidence remains on the remote host; this folder only contains key
  manuscript-facing artifacts and acceptance records.

## Important Update

The original `2026-06-26` main package still records the failed LoFTR attempt:

- `6037/6037` records are `error`
- the dominant error type is `OutOfMemoryError`

That failed package is intentionally preserved as raw evidence. The accepted
LoFTR replacement evidence now lives in:

- `loftr_retry_20260628/`

Therefore the full benchmark evidence should now be interpreted as:

- original accepted methods:
  `sift_ransac`, `akaze_ransac`, `roma_outdoor`, `xoftr_official`,
  `raw_minima`, `uav_talign_full`
- accepted LoFTR replacement:
  `loftr_retry_20260628/main_outputs/loftr_outdoor_results.jsonl`

## Folder Map

- `main_outputs/`
  Main experiment summary, validator output, and selected method result JSONL
  files copied from the remote run.
- `protocol_closure/`
  Scene-level protocol evidence used for supplement tables and risk-coverage
  style figures.
- `loftr_retry_20260628/`
  Accepted standalone LoFTR retry evidence generated with the memory-safe
  execution profile.
- `remote_audit/`
  Acceptance notes and the SHA256 manifest copied from the remote audit folder.

## Primary Files to Read First

- `main_outputs/main_experiment_summary.json`
- `main_outputs/validate_stdout.json`
- `loftr_retry_20260628/main_outputs/main_experiment_summary.json`
- `loftr_retry_20260628/main_outputs/validate_stdout.json`
- `protocol_closure/paper_facing_summary.md`
- `protocol_closure/canonical_operating_point.csv`
- `protocol_closure/per_scene_reliability_table.csv`
- `remote_audit/sha256_manifest.txt`

## Companion Note

See `supplement_run_note_zh.md` for the Chinese collaboration note that
summarizes the run, the accepted evidence, and the remaining caveats for paper
writing.
