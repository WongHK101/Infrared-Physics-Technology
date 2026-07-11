# Controlled Protocol Validation

This directory contains two read-only validations derived from the frozen UAV-TAlign-12K formal
outputs. Both were executed with code commit
`ce211c8ee675611ff33e1a8ffbea8ece5498bb44` and wrote to isolated output directories.

## Leave-frame-out consensus stability

- Scope: 15 scenes, 5 deterministic folds per scene, 75 recomputations.
- Each fold withholds approximately one fifth of accepted frame hypotheses.
- Scene-median displacement from the full-evidence consensus: 1.3879 px.
- Mean displacement across scenes: 2.2556 px.
- Raw artifacts: `ipt_leave_frame_out_20260710_192817/`.

## Synthetic QA perturbations

- Scope: 15 scenes, 45 representative frames, 675 controlled trials.
- Modes: translation, rotation, and scale.
- Nominal severities: 2, 5, 10, 20, and 40 px.
- The mean joint edge/gradient score decreases monotonically with severity within every mode.
- At the largest severity, mean joint-score changes are -0.0741, -0.0310, and -0.0251 for
  translation, rotation, and scale; degraded-trial fractions are 84.4%, 80.0%, and 73.3%.
- Raw artifacts: `ipt_synthetic_qa_20260710_193252/`.

The synthetic joint score is a controlled sensitivity diagnostic and is distinct from the fixed
canonical scene gate and the non-trained reliability ranking used for risk-coverage visualization.
