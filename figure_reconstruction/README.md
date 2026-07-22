# UAV-TAlign figure reconstruction

This directory contains the reproducible source package for the nine redesigned
main-text figure groups. Each figure has an independent directory with:

- `build.py`: Python-only rendering entry point;
- `figure_contract.md`: claim, evidence hierarchy, panel map, and review risks;
- `source_data/`: frozen, figure-local CSV/JSON inputs;
- `source_assets/`: selected public-safe image crops or visual inputs;
- `outputs/`: SVG, PDF, and 600-dpi PNG exports; raster panels are embedded
  at 600 dpi in the vector containers.

Run all figures with:

```powershell
python build_all.py
```

Refresh verified qualitative assets from the read-only dataset and frozen
scene-result record with `prepare_highres_assets.py` before rebuilding when the
case shortlist changes.

The scripts never write to the raw dataset or experiment-output directories.
Missing visual evidence is represented by an explicitly labelled wireframe;
no synthetic result or fabricated image is used.
