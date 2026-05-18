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

- Candidate collection: 6,039 RGB-infrared pairs / 12,078 images.
- Official evaluation split: 6,037 integrity-checked RGB-infrared pairs / 12,074 images.
- Excluded pairs: 2 integrity-excluded pairs from scene 13.
- Manifest SHA256: `a092f7ad00c6e02ead3bd39de5c246001f1d4bebbc4105ba715ef37bbb202c6c`.

## Submission Text Policy

Before repository or DOI is finalized, use:

> UAV-TAlign-12K, the official evaluation manifest, scene metadata, integrity report, and evaluation scripts have been prepared for public release. The official evaluation split contains 6,037 integrity-checked RGB-infrared pairs from a 6,039-pair UAV infrared-visible alignment collection. The dataset and code will be released through a public repository, and review access can be provided during peer review. The official manifest hash and metadata schema are provided to support reproducible evaluation.

After repository or DOI is finalized, replace with:

> UAV-TAlign-12K is available at [repository/DOI]. The official evaluation manifest, scene metadata, integrity report, and evaluation scripts are available at [code/repository URL]. The official evaluation split contains 6,037 integrity-checked RGB-infrared pairs from a 6,039-pair UAV infrared-visible alignment collection. The official manifest SHA256 is `a092f7ad00c6e02ead3bd39de5c246001f1d4bebbc4105ba715ef37bbb202c6c`.

## Open Decisions

- Select final hosting route for the image archive.
- Decide whether peer-review access uses an anonymous repository, private DOI draft, OSF private link, or institutional file sharing.
- Confirm dataset license or terms-of-use text.
- Replace placeholders in `data_availability_statement.txt` before final submission.
