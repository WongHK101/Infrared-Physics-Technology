# Resolved visual source

The qualitative RIFT2 cell now uses a reproduced 3 x 3 infrared-to-RGB
homography for `S04 / 000020` under the frozen strong configuration. The complete
single-pair record is stored in
`source_data/rift2_scene04_pair000020_reproduction.json`, and the reusable command
implementation is `reproduce_rift2_pair.py`.

The reproduction used `max_dim=1200`, `npt=2000`, `patch_size=64`, Lowe ratio
`0.95`, and `USAC_MAGSAC`, matching the accepted 12K strong run. No full benchmark
rerun was performed.
