# Ablation Summary (2026-06-29)

Accepted local evidence root:

- `submission_materials/supplement_run_evidence_20260629/ablation/`

Remote source:

- `G:\UAV-TAlign\UAV-TAlign\outputs\ipt_p3p5_supplement_bundle_20260629_133127`

Evaluation scope:

- subset: `UAV-TAlign-1K`
- scenes: `01,02,03,04,07,08,13,14`
- method: `uav_talign_full`

## Summary Table

| Stage | Canonical pass | QA pass | Accepted frames mean | Accepted frames range | Attempted frames mean | Runtime mean (s) |
|---|---:|---:|---:|---:|---:|---:|
| `A1_candidate_only` | `8 / 8` | `5 / 8` | `13.625` | `8 - 34` | `17.75` | `121.517` |
| `A2_candidate_plus_aggregation` | `8 / 8` | `5 / 8` | `13.625` | `8 - 34` | `17.75` | `30.606` |
| `A3_candidate_plus_aggregation_plus_qa` | `5 / 8` | `5 / 8` | `26.000` | `7 - 49` | `31.375` | `50.690` |
| `S1_random_selection_seed0` | `5 / 8` | `6 / 8` | `26.625` | `7 - 49` | `31.500` | `50.750` |

## Acceptance Notes

- All 4 accepted stages have complete local evidence:
  `config + summary + logs + results + scene_results + 8 scene_result.json`.
- `A1` and `A2` preserve all 8 scenes at the canonical-pass level, but their
  accepted-frame statistics are much lower than the later gated pipeline.
- `A3` is the first stage that reflects the stricter QA-aware operating style.
- `S1_seed0` is kept in both `ablation/` and `multiseed/` views:
  it acts as the ablation endpoint and also the random-sensitivity baseline.
