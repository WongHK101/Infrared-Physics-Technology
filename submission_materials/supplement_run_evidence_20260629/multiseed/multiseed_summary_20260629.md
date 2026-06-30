# Multi-Seed Summary (2026-06-29)

Accepted local evidence root:

- `submission_materials/supplement_run_evidence_20260629/multiseed/`

Remote source:

- `G:\UAV-TAlign\UAV-TAlign\outputs\ipt_p3p5_supplement_bundle_20260629_133127`

Evaluation scope:

- subset: `UAV-TAlign-1K`
- scenes: `01,02,03,04,07,08,13,14`
- method: `uav_talign_full`
- seeds: `0,1,2,3`

## Summary Table

| Seed | Canonical pass | QA pass | Accepted frames mean | Accepted frames range | Attempted frames mean | Runtime mean (s) |
|---|---:|---:|---:|---:|---:|---:|
| `seed0` | `5 / 8` | `6 / 8` | `26.625` | `7 - 49` | `31.500` | `50.750` |
| `seed1` | `5 / 8` | `5 / 8` | `26.750` | `8 - 49` | `32.000` | `51.210` |
| `seed2` | `7 / 8` | `7 / 8` | `26.625` | `8 - 49` | `31.750` | `51.344` |
| `seed3` | `5 / 8` | `5 / 8` | `28.125` | `8 - 49` | `33.500` | `53.627` |

## Acceptance Notes

- All 4 accepted seeds have complete local evidence:
  `config + summary + logs + results + scene_results + 8 scene_result.json`.
- The main spread appears in strict scene retention, not in accepted-frame mean.
- `seed2` is the strongest current seed under the strict canonical criterion.
- The accepted-frame mean is relatively stable across seeds, which suggests the
  random variation is concentrated near the pass/fail boundary.
