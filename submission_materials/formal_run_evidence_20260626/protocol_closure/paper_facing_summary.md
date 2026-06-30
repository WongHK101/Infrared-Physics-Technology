# P0-D Protocol Closure Summary

## Run Provenance
- P0-C output root: `G:\UAV-TAlign\UAV-TAlign\outputs\ipt_p0c_12k_main`
- Official manifest: `G:\UAV-TAlign\UAV-TAlign\manifests\UAV-TAlign-12K_official_valid_evaluation_manifest.json`
- Manifest canonical SHA256: `a092f7ad00c6e02ead3bd39de5c246001f1d4bebbc4105ba715ef37bbb202c6c`
- Valid evaluation pairs: `6037`
- Git commit: `c55e39e49cda508bae68520f718894bb0c761cec`

## Main Findings
- UAV-TAlign produces scene-level homographies for `15/15` scenes and retains `9/15` scenes under the strict canonical QA-controlled operating point.
- The P0-D reliability score provides an interpretable ordering for coverage analysis without changing the canonical result.
- The canonical QA gate retains `01,04,05,06,07,08,10,12,14` with scene coverage `60.0%` and pair coverage `74.4%`.
- At 9 retained scenes by score ranking, scene coverage is `60.0%` and pair coverage is `72.4%`; the mean severe-outlier ratio is `0.009`.
- The score-ranked top-K operating points and the canonical retained-scene set are related but not identical; the score-ranked curve is used for operating-profile visualization, not as a replacement for the canonical QA gate.
- Risk-coverage and threshold-sensitivity curves should be used to present the operating trade-off rather than relaxing the canonical result.

## Named Operating Regimes
| Regime | Retained scenes | Scene coverage | Pair coverage | Mean severe outlier | Mean robust reject |
|---|---:|---:|---:|---:|---:|
| conservative | 3 | 20.0% | 29.2% | 0.000 | 0.093 |
| balanced | 8 | 53.3% | 64.7% | 0.000 | 0.124 |
| permissive | 13 | 86.7% | 96.1% | 0.032 | 0.140 |
| inclusive_profile | 15 | 100.0% | 100.0% | 0.044 | 0.149 |

## Artifacts
- `reliability_score_design.md`
- `per_scene_reliability_table.csv`
- `canonical_operating_point.csv`
- `risk_coverage.csv` and `risk_coverage_curve.pdf/png`
- `threshold_sensitivity.csv` and `threshold_sensitivity.pdf/png`
- `condition_reliability_profile.csv` and `condition_reliability_profile.pdf/png`

## Suggested Paper Wording
Under the strict canonical reliability gate, UAV-TAlign produces scene-level homographies for all 15 scenes and retains 9 scenes as high-confidence operating points. The risk-coverage curve is a score-ranked operating profile, with the canonical 9/15 point marked explicitly; it visualizes reliability--coverage trade-offs without replacing the canonical decision rule.
