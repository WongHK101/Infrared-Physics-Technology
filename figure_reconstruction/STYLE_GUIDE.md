# Figure and Table Conventions

Updated 2026-10-21.

- Editable figures use Times New Roman; plot math uses STIX to match the serif text.
- Chart axes use a common 10 pt base, 9 pt tick labels, and 8.5 pt legends before
  placement. Multi-panel chart titles use `(a)`, `(b)`, `(c)` and left alignment.
- Scene identifiers use `S01` through `S15`. Display conditions use Day, Night,
  Low-light, Grayscale, Pseudocolor, Wide, Zoom, and General.
- Canonical retained scenes are green circles; QA-filtered scenes are gray squares
  in statistical plots. The canonical operating point uses a red star.
- Photo galleries keep white-background, black vertical scene labels, tight equal
  gutters, native aspect ratios, and identical source crops. Their label colors do
  not encode status.
- RGB edges are cyan, infrared edges red, and overlap pale yellow; these image
  overlays are distinct from the statistical-plot palette.
- Each quantitative encoding needs a key. The Appendix B QA scatter includes both
  status and robust-rejection marker-size keys.
- Main and appendix figures share the same outputs; PNG previews do not replace
  the vector PDF/SVG master. No experimental quantity or captured-image pixel is
  changed for appearance.
- Both manuscript languages load `layout_settings.tex`: consistent table body
  size, 1.15 row spacing, booktabs rules, and top-aligned float pages.
- Compact seven/eight-column tables keep 3 pt cell padding; other tables use 4 pt.
  All manuscript tables occupy the text width. Captions remain external to artwork.
- Appendix equations are numbered by appendix section in both languages.
