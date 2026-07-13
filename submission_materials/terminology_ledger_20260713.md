# Terminology ledger

| Canonical term | Use | Replaced variants |
|---|---|---|
| infrared-visible alignment | Task and research area | RGB-thermal alignment, visible-thermal registration in general prose |
| RGB-infrared pair | Dataset sample unit | RGB-thermal pair, visible-infrared pair |
| UAV-TAlign-12K | Dataset and benchmark | 12K dataset, full collection |
| official evaluation split | Integrity-checked 6,037-pair split | valid manifest, formal split |
| UAV-TAlign reference framework | Proposed scene-scale procedure | full pipeline, benchmark baseline |
| pairwise homography evidence | Matcher-level output used by Track A | pairwise usability, matcher availability |
| scene transform | Scene-scale homography product in prose | retained homography, scene-level result |
| high-confidence scene product | Scene selected by the canonical decision | passed scene, successful scene |
| canonical operating point | Reported 9/15 product set and its coverage | strict gate, conservative gate |
| cross-modal scene verification | Final geometry and appearance-consistency stage | QA-aware verification, quality gate |
| reliability--coverage profile | Score-ranked Track C analysis | risk curve, retention sweep |
| RIFT2 (Python, resize-aware) | Fixed paper-facing baseline name | official RIFT2, RIFT2 strong |

Use `QA gate` only when defining the binary rule in the Method section. Use `RGB-infrared` for the
paired data unit and `infrared-visible` for the task, benchmark positioning, and alignment system.

