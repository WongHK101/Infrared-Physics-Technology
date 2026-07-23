# UAV-TAlign figure reconstruction

This directory contains the reproducible source package for the nine redesigned
main-text figure groups. Each figure has an independent directory with:

- `build.py`: rendering or validated-export entry point;
- `drawio_source/`: editable Draw.io source for schematic panels where applicable;
- `figure_contract.md`: claim, evidence hierarchy, panel map, and review risks;
- `source_data/`: frozen, figure-local CSV/JSON inputs;
- `source_assets/`: selected public-safe image crops or visual inputs;
- `outputs/`: SVG, PDF, and 600-dpi PNG exports; raster panels are embedded
  at 600 dpi in the vector containers.

Figures 1, 2, and 4 are hybrid compositions: Draw.io supplies the editable
schematic panels, while Python renders the data-bound plots and verified
RGB/infrared imagery. Figure 3 is a fully editable Draw.io schematic. Figures
5--9 remain Python-rendered because their primary evidence is image- or
data-bound rather than diagrammatic.

Run the Python/hybrid assembly and verify the Draw.io-managed export with:

```powershell
python build_all.py
```

Refresh verified qualitative assets from the read-only dataset and frozen
scene-result record with `prepare_highres_assets.py` before rebuilding when the
case shortlist changes.

The scripts never write to the raw dataset or experiment-output directories.
Missing visual evidence is represented by an explicitly labelled wireframe;
no synthetic result or fabricated image is used.
