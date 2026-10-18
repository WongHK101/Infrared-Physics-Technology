# UAV-TAlign figure sources

The manuscript uses eleven main-text figures and four appendix figures. Stable
directory IDs are not the displayed LaTeX figure numbers.

Each directory contains its build.py, figure_contract.md, caption draft, frozen
source_data/source_assets as applicable, and SVG/PDF/PNG outputs. Figures 1--3,
5--7 use editable Draw.io compositions. Their text and diagram shapes remain
vector objects, and verified JPEG/PNG assets are embedded without resampling.
Figure 4 and the quantitative figures 8--11 are data-driven Matplotlib plots.

## Rebuild

Set DRAWIO_EXECUTABLE to your installed draw.io desktop executable, then run
python build_all.py in this directory. Python needs NumPy, pandas, Matplotlib,
Pillow and scikit-image. The script exports each figure and copies the PDF
versions, including the appendix plates, to the manuscript figures directory.

PNG exports are previews (4400 pixels wide for Draw.io, 600 dpi for Matplotlib).
The manuscript uses PDF; SVG and Draw.io are the editable handoff formats.
The old make_live_plan.py and auxiliary Draw.io panel files are historical;
build.py is the authoritative entry point for the October 18 revision.

## Evidence

The source assets are selected figure crops, not the full dataset. Builds do not
read or modify raw dataset directories, weights or experiment outputs. The
pairwise edge panels are deterministic renders of frozen matrices, not new
model inference.

STUDENT_ASSET_ADOPTION_ZH.md documents the 2026-10-18 student delivery and the
selective visual merge. The accompanying provenance JSON records original-file
hashes, 44 exact JPEG matches and six pixel-exact edge-panel checks. The student
originals remain unchanged outside this repository.

The canonical set, source CSVs, all numerical results, and the corrected
risk/validation/ablation definitions remain unchanged.
