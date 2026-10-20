# UAV-TAlign-12K Data Release Plan

## Recommended Landing Route

Primary release route:

- Public dataset archive: Zenodo, OSF, institutional repository, or equivalent DOI-capable repository.
- Public code and manifest repository: GitHub or anonymous review repository, then final public repository after acceptance.
- Reviewer access: private or anonymous-access link to the dataset archive during peer review if the public DOI is not finalized before submission.

## Minimum Release Contents

The release should include:

- UAV-TAlign-12K image archive or access instructions.
- Official valid evaluation manifest.
- Scene metadata.
- Integrity report and integrity summary.
- Excluded-pair list for the official evaluation split.
- Duplicate-hash diagnostics.
- Per-scene and per-condition valid-pair counts.
- Evaluation scripts and environment notes.
- README with dataset structure, naming policy, and citation instructions.
- License file or terms-of-use statement.
- Code commit hash used for the journal-scale experiments.
- Manifest SHA256 for reproducible evaluation.

## Current Official Evaluation Split

- Joint dataset owners: Nanning Normal University and Guangxi University.
- Approved data license: CC BY 4.0. Original project software: Apache-2.0.
- No dataset DOI or functioning reviewer-access link is recorded as of 2026-10-21.

- Candidate collection: 6,039 RGB-infrared pairs / 12,078 images.
- Official evaluation split: 6,037 integrity-checked RGB-infrared pairs / 12,074 images.
- Excluded pairs: 2 integrity-excluded pairs from scene 13.
- Manifest SHA256: `a092f7ad00c6e02ead3bd39de5c246001f1d4bebbc4105ba715ef37bbb202c6c`.

## Submission Text Policy

Before repository or DOI is finalized, use:

Use the factual current-state draft in `data_availability_statement.txt`. Do not state that review access is available until a functioning link or an editorial-system dataset attachment has been established.

After repository or DOI is finalized, replace with:

Use the public-release candidate in `data_availability_statement.txt`, with the real tested URLs. The supplementary code/evaluation ZIP is an offline access option, not a substitute for access to the full image archive.

## Open Decisions

- Select final hosting route for the image archive.
- Decide whether peer-review access uses an anonymous repository, private DOI draft, OSF private link, or institutional file sharing.
- Retain the confirmed joint attribution and approved layered licenses.
- Replace placeholders in `data_availability_statement.txt` before final submission.
