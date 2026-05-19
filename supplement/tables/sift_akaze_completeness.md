# SIFT/AKAZE 12K Classical-Keypoint Completeness

SIFT and AKAZE were evaluated on the same official UAV-TAlign-12K valid evaluation manifest used by the main 12K experiments. The run completed for all 6,037 evaluation pairs with an empty `run_stderr.log`.

## Pairwise Summary

| Method | OK / N | H Available | H Availability (%) | Mean Inlier Ratio | Mean Coverage | Median Reproj. | Runtime / Pair (s) |
|---|---:|---:|---:|---:|---:|---:|---:|
| SIFT + RANSAC | 5257/6037 | 5257/6037 | 87.08 | 0.242 | 0.627 | 0.000 | 9.008 |
| AKAZE + RANSAC | 5692/6037 | 5692/6037 | 94.29 | 0.160 | 0.730 | 0.105 | 1.511 |

## Status Counts

| Method | Status counts |
|---|---|
| SIFT + RANSAC | ok 5257; error 153; fit_failed 289; no_matches 93; insufficient_matches 245 |
| AKAZE + RANSAC | ok 5692; fit_failed 152; no_matches 92; insufficient_matches 101 |

## Notes

These results provide classical-keypoint context for the main pairwise baseline table. Detailed per-scene and condition summaries are provided in:

- `sift_akaze_per_scene_summary.csv`
- `sift_akaze_condition_summary.csv`

The reported metrics remain complementary diagnostics under a unified downstream estimator and should not be interpreted as a single absolute ordering of matcher quality.

Very low fitted reprojection error can occur on sparse inlier sets and should be interpreted
together with homography availability and spatial coverage. Error-status records are method-level
backend statuses captured by the unified evaluator; the overall run completed normally with an
empty `run_stderr.log`.
