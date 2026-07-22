# Figure reconstruction QA report

Date: 2026-07-22

## Build and export

- Backend: Python / Matplotlib only.
- Nine figure directories build successfully through `build_all.py`.
- Every figure exports one editable-text SVG, one single-page selectable-text PDF,
  and one 600-dpi PNG preview. Raster panels embedded in SVG/PDF are rendered at
  600 dpi rather than Matplotlib's 100-dpi default.
- All PNG previews are wider than 1,500 pixels.
- Python syntax compilation passes for all drawing scripts.

## Data and image integrity

- Quantitative panels use figure-local copies of frozen CSV/JSON evidence.
- Main-split values follow the current manuscript evidence freeze, including LoFTR
  `5984/6037`, the canonical `9/15` product set, `74.4%` pair coverage, and
  `1491/2304 (64.7%)` accepted/attempted support.
- The 82 selected JPEG source assets contain no EXIF metadata. Figure-local
  qualitative crops are at least 1280 x 896 pixels; RGB-space overlays are
  generally 2800 x 1960 pixels.
- No raw dataset file or experiment output is modified by the build scripts.
- No account name, server address, credential, or absolute local path is present in
  the tracked figure scripts and text/data manifests.

## Visual review

- A 3 x 3 review sheet is available as `figure_contact_sheet.png`.
- Panel letters, titles, axes, condition labels, and image crops were reviewed at
  original PNG resolution after the second layout pass.
- Color semantics remain consistent: RGB/visible blue, infrared orange,
  high-confidence green, QA-filtered gray, and canonical decision red.
- Quantitative panels avoid dual y-axes and do not convert complementary diagnostics
  into a single absolute method ranking.
- The nine-figure sequence was reviewed against the four local high-quality reference
  papers. It now provides comparable evidence density: benchmark overview, protocol,
  algorithm mechanism, qualitative products, operating profile, and controlled validation.
- Fig. 3 was rebuilt from a generic flowchart into an explicit algorithmic schematic with
  progressive scheduling, frame reliability, median/MAD consensus, cross-modal QA, and
  separate canonical/ranking branches. Its visual example is the requested S02/000009
  pair and is presented as an aligned scene candidate before the two decision branches.
- S06 is not used as a qualitative case. It remains only where all-scene quantitative
  evidence is shown, preserving the complete 15-scene analysis.
- Fig. 5 uses a dark image-plate background with thicker cyan/red edge traces and a light
  agreement cue, so method-specific alignment evidence remains legible at print size.

## Resolved source item

- Fig. 5 contains the reproduced RIFT2 fixed-pair overlay. The single-pair record
  matches the frozen strong configuration and is retained with the figure source data;
  no full benchmark rerun was performed.
- No figure has an active placeholder or unresolved source dependency.
