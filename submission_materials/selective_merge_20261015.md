# Student Revision Integration

The LaTeX manuscript at revision `d19e7fc` remains the base. The student Word
document is preserved separately, unchanged, as a comparison source.

## Incorporated

- Explicit distinction between synchronized capture and geometric registration.
- Clear track and deployment definitions, including the RIFT2 fitting profile.
- Less crowded, separate plots for operating profiles, conditions, validation,
  and module attribution, using the original numerical sources.

## Corrected

- Exact normalized scene score and fixed frame weighting formula.
- QA reference, severe-outlier definition, representative probes, support threshold,
  canonical paths, and the distinction between adaptive stopping and final retention.
- Pairwise aggregation denominators, pixel units, and the 1.39-pixel scene-mean statistic.
- Group-mean scope of perturbation trends, and ablation output/retention semantics.
- RIFT2 method/software citations and selected bibliography metadata.
- English/Chinese mirrors, highlights, automated references, and editable equations.

No experimental results, raw imagery, canonical decisions, or algorithm code were changed.
The original student's duplicate scene tables, raster equations, swapped consensus
legend, and score-to-retention shortcut were not imported.

## Verification

- English PDF: 34 preprint pages including references and protocol appendix; Chinese review PDF: 24 pages.
- Both builds complete without LaTeX errors, undefined citations/references, or overfull boxes.
  Existing empty-page-field BibTeX warnings remain on seven proceedings entries; they are not missing citations.
- Rendered both PDFs and inspected the revised tables, equations, and figures.
- English/Chinese citation keys, cross-references, and figure inputs match.
- The 15 archived scores reproduce to floating-point precision (maximum absolute difference below 2e-14).
- Recomputed the leave-frame-out statistic: median of scene means = 1.38790725318 pixels.
- New plot CSV copies are byte-identical to their archived source files.
- Abstract: 177 whitespace-delimited words. Four standalone highlights: 70, 70, 72, and 74 characters.
- Student Word SHA256 remains `293755adc8980d2248c346cab25c90ee4f30eb5e24ab25638939a7372aa6fac9`.

## Author Checks Before Submission

- Supply the actual dataset/reviewer-access URL or DOI; no link was invented.
- Confirm author list, affiliations, corresponding author, funding, conflicts, and CRediT roles.
- Review the AI-assistance declaration against actual use, including applicable tool/version
  information and final author responsibility; the manuscript contains a factual scope statement.
- Obtain the requested student figure sources listed in
  `figure_reconstruction/STUDENT_FIGURE_HANDOFF_ZH.md` before replacing their designs.
- The protocol definitions are compiled as Appendix A. The remaining `supplement/`
  directory is a source-material collection, not yet a standalone submission PDF.

## Bibliographic Verification Sources

- MAGSAC/MAGSAC++: official CVF proceedings entries.
- RIFT2: https://arxiv.org/abs/2303.00319
- RIFT2 implementation: https://github.com/canyagmur/RIFT2-multimodal-matching-rotation-python
- R2D2: official NeurIPS 2019 proceedings entry.
- S2DNet: official ECCV 2020 / ECVA entry.
- LasHeR: https://doi.org/10.1109/TIP.2021.3130533
- FLIR: original 2018 announcement cited in `references.bib`.
