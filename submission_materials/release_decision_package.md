# UAV-TAlign-12K Release Decision Package

This document prepares release options for user approval. It does not select a final hosting platform, license, DOI, or reviewer-access policy.

## Current Release State

- Dataset name: UAV-TAlign-12K.
- Candidate collection: 6,039 RGB-infrared pairs / 12,078 images.
- Official evaluation split: 6,037 integrity-checked RGB-infrared pairs / 12,074 images.
- Manifest SHA256: `a092f7ad00c6e02ead3bd39de5c246001f1d4bebbc4105ba715ef37bbb202c6c`.
- Dataset rights holder and attribution: Guangxi University.
- Dataset/content license: Creative Commons Attribution 4.0 International (CC BY 4.0).
- Original UAV-TAlign software license: Apache License 2.0.
- Vendored software: respective upstream licenses; the top-level license does not override them.
- Current release metadata bundle: `submission_materials/release_metadata_bundle/`.
- Current code repository state for release packaging: use the latest clean public code commit after user approval.

## Release Route Options

| Option | DOI support | Large-file suitability | Anonymous/reviewer access | Strengths | Risks / user decisions |
|---|---:|---:|---:|---|---|
| Zenodo dataset archive | Yes | Good for archived dataset releases; file-size policy should be checked at upload time | Secret links can share draft/restricted records | Strong citation workflow, DOI, versioned archival record | User must decide license, metadata, whether to publish immediately or use draft/restricted review access |
| OSF project / storage | Yes for public projects | Suitable for project organization; storage limits and add-ons should be checked | Private view-only links and anonymized links are supported | Good for reviewer-access workflows and structured project pages | User must confirm storage capacity, privacy/anonymization settings, and final license |
| Institutional repository | Usually yes | Often strong for large datasets | Depends on institution | Stable, policy-friendly, may support institutional review workflows | Requires institutional approval and may be slower |
| GitHub release + external dataset storage | GitHub itself does not provide dataset DOI by default | Good for code, manifests, lightweight metadata; not ideal as sole raw-image host | Anonymous code review can be handled separately | Simple for scripts, manifests, documentation, and versioned code | Raw image archive should usually live in DOI-capable or storage-oriented repository |
| Reviewer-access private link + public release after acceptance | Depends on backing platform | Depends on backing platform | Good when public DOI is not finalized before submission | Lets review proceed with verifiable artifacts while preserving final release timing | Must avoid author-identifying links if anonymous review is required; final public release plan must be credible |

## Recommended Practical Route For Review

1. Prepare public code, manifests, metadata, and evaluation scripts in the manuscript/code repository.
2. Prepare the raw-image archive in a DOI-capable repository or institutional storage.
3. Provide reviewer access through the selected platform if the final public DOI is not ready before submission.
4. Replace manuscript placeholders after the user selects the release platform, license, and access policy.

## Required Release Contents

- Raw UAV-TAlign-12K image dataset or controlled access instructions.
- Official valid evaluation manifest.
- Scene metadata.
- Integrity report and integrity summary.
- Excluded-pair list.
- Duplicate-hash diagnostics.
- Per-scene and per-condition statistics.
- Evaluation scripts.
- Environment file or reproducibility notes.
- Model-weight instructions; do not redistribute third-party weights unless licenses allow it.
- README with dataset structure, manifest hash, evaluation entry point, and citation instructions.
- CC BY 4.0 dataset/content notice and Apache-2.0 original-code notice.
- Code commit hash used for the journal-scale experiments and final public scripts.

## Data Availability Candidate Text

### Reviewer-access version

UAV-TAlign-12K, the official evaluation manifest, scene metadata, integrity report, and evaluation scripts have been prepared for public release. The official evaluation split contains 6,037 integrity-checked RGB-infrared pairs from a 6,039-pair UAV infrared-visible alignment collection. The dataset and code will be released through a public repository, and review access can be provided during peer review at [reviewer-access URL to be inserted]. The official manifest SHA256 is `a092f7ad00c6e02ead3bd39de5c246001f1d4bebbc4105ba715ef37bbb202c6c`.

### Public DOI / repository version

UAV-TAlign-12K is available at [repository/DOI to be inserted]. The official evaluation manifest, scene metadata, integrity report, and evaluation scripts are available at [code/repository URL to be inserted]. The official evaluation split contains 6,037 integrity-checked RGB-infrared pairs from a 6,039-pair UAV infrared-visible alignment collection. The official manifest SHA256 is `a092f7ad00c6e02ead3bd39de5c246001f1d4bebbc4105ba715ef37bbb202c6c`.

## Sources Checked

- Infrared Physics & Technology Guide for Authors: research data availability statement is required at submission.
- Zenodo help: link sharing can provide secret links for draft/restricted records.
- Zenodo FAQ: DOI can be reserved before publication.
- OSF support: private projects can be shared via view-only links, and DOI creation is available for public projects.

## User Decisions Still Required

- Final dataset hosting platform.
- Whether to provide reviewer-access before publication.
- Whether to publish a DOI before submission, reserve one, or release upon acceptance.
- Final author, affiliation, and corresponding-author information.
