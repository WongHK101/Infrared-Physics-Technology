# Condition profile figure

Three related panels compare illumination, thermal rendering, and view type.
Use `source_data/condition_reliability_profile.csv` unchanged. Filled circles
encode scene-level retention; open squares encode the ratio of summed accepted
and attempted frames. Counts annotate retained/total scenes, not pair counts.
The same scenes recur across attributes, so the panels are not independent samples.
`build.py` produces editable-text SVG, vector PDF, and 600-dpi PNG. No image
assets or new experimental runs are required.
