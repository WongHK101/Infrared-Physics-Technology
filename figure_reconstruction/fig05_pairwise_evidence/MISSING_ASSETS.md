# Missing visual source

The quantitative RIFT2 row is frozen and included in `pairwise_methods.csv`.
The qualitative RIFT2 cell intentionally remains a wireframe because the strong-run
per-pair homography for `S04 / 000020` has not yet been copied into this local package.

Required replacement:

- one 3 x 3 infrared-to-RGB homography matrix from the accepted RIFT2 strong run;
- add it under `methods.RIFT2` in `source_data/selected_pair_homographies.json`;
- rerun `build.py`.

No experiment rerun is required.

