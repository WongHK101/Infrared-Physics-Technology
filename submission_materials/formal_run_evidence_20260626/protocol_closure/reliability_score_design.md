# Reliability Score Design

This P0-D analysis uses an interpretable, non-trained scene reliability score.
It is designed for ranking, threshold sweep, and risk-coverage visualization,
not as a learned replacement for the canonical QA-controlled scene criterion.

## Inputs

The score uses scene-level quantities already produced by the UAV-TAlign QA
pipeline:

- accepted ratio among attempted frames;
- severe baseline-relative QA outlier ratio;
- robust consensus reject ratio;
- edge-overlap improvement after alignment;
- gradient-NCC improvement after alignment;
- a lightweight geometry diagnostic from inlier ratio, spatial coverage, and
  reprojection error.

## Normalization

- `accepted_score = clip(accepted_ratio, 0, 1)`.
- `outlier_score = 1 - clip(severe_outlier_ratio / 0.10, 0, 1)`.
- `robust_score = 1 - clip(robust_reject_ratio / 0.25, 0, 1)`.
- `edge_score = clip((delta_edge_f1 + 0.05) / 0.20, 0, 1)`.
- `grad_score = clip(delta_grad_ncc / 0.15, 0, 1)`.
- `geometry_score = 0.5 * clip(mean_inlier_ratio / 0.50, 0, 1)
  + 0.3 * clip(mean_coverage, 0, 1)
  + 0.2 * (1 - clip((mean_reproj_error - 1.5) / 1.0, 0, 1))`.

## Score

`reliability_score = 100 * (0.25 accepted_score + 0.25 outlier_score
+ 0.20 robust_score + 0.15 edge_score + 0.10 grad_score
+ 0.05 geometry_score)`.

The largest weights are assigned to retained evidence, QA outlier control, and
robust consensus behavior because these terms directly express the
scene-level reliability question. Edge/gradient gains provide image-domain
supporting evidence, while geometry statistics are retained as a low-weight
diagnostic rather than a single absolute quality ordering.

## Paper-facing usage

The strict canonical result remains the primary operating point. The score is
used to show the broader reliability--coverage profile and threshold
sensitivity of the same completed 12K first-wave run.
