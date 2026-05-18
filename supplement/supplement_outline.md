# Supplementary Material Outline

Working title:

Supplementary Material for UAV-TAlign-12K: Scene-Level Reliability Evaluation for Cross-FOV UAV Infrared-Visible Image Alignment

## S1. Reliability Score Design

Report the non-trained, interpretable reliability score used for scene ranking and operating-profile visualization. The score combines accepted-frame support, severe outlier control, consensus stability, edge/gradient improvement, and geometry diagnostics. It supports risk-coverage analysis and threshold sweeps, while the canonical QA gate remains the retained-product decision rule.

Primary source:

- `tables/reliability_score_design.md`

## S2. Threshold Sensitivity

Report threshold sweeps around the strict canonical operating point. The section should emphasize the stability of the operating profile and the availability of conservative, balanced, and permissive reliability regimes.

Primary source:

- `tables/threshold_sensitivity.csv`

## S3. Per-Scene Reliability Details

Report scene-level accepted ratio, severe outlier ratio, robust reject ratio, delta edge/gradient diagnostics, reliability score, and canonical QA status.

Primary source:

- `tables/per_scene_reliability_table.csv`

## S4. Condition Reliability Profile

Summarize reliability diagnostics by light condition, thermal rendering, view type, and scene family where available. Report both scene-level macro summaries and pair-level micro support when possible.

Primary source:

- `tables/condition_reliability_profile.csv`

## S5. RIFT2 Parameter Sanity Check

Document the light-vs-strong resize-aware RIFT2 sanity check. The strong setting increases matches, inliers, coverage, and median reprojection quality at higher runtime, and is therefore used for the 12K RIFT2 baseline.

Primary source:

- `tables/rift2_light_vs_strong_sanity.csv`

## S6. Manifest Integrity Summary

Document the official evaluation split and manifest hash. Use paper-facing wording around integrity-checked evaluation pairs.

Primary sources:

- `tables/manifest_integrity_summary.csv`
- `../submission_materials/release_metadata_bundle/`

## S7. Additional Qualitative Examples

Reserve space for additional retained and QA-filtered examples across day, night, lowlight, grayscale, pseudocolor, wide, and zoom scenes.

Primary source:

- `figures/qualitative_examples_placeholder.md`

## S8. Classical Keypoint Completeness

Reserve a table for SIFT/AKAZE 12K full results after the background run completes and GPT decides whether the results should enter the main manuscript or supplementary material.

Primary source:

- `tables/sift_akaze_placeholder.md`
