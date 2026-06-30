# UAV-TAlign 结果摘要（协作者写作版，2026-06-28）

这份摘要的目标不是替代正式证据包，而是给协作者一个可以直接理解和转述的当前结果主线。所有数字都应回到本地证据文件复核后再进入论文正文。

## 1. 当前整体结论

截至目前，`UAV-TAlign` 的 benchmark 主链路已经闭环：

- `UAV-TAlign-12K` 官方评测集固定为 `6037` 对图像、`15` 个 scene；
- 主实验 formal run 已完成；
- `uav_talign_full` 的 scene-level 结果与 protocol closure 已完成；
- 原始 `LoFTR` OOM 问题已通过单独的 memory-aware 正式重跑补齐；
- benchmark 当前已经具备“可支撑写作”的主结果证据层。

换句话说，我们现在的主要矛盾不再是“benchmark 有没有跑通”，而是：

- 如何把现有已验收证据组织成稳定的主表、结果段和补充材料；
- 是否还要继续补 `RIFT2`、ablation、multi-seed 这三块证据。

## 2. Pairwise baseline 主结果

当前可直接引用的 pairwise baseline 结果如下：

| Method | H available | 比例 | 说明 |
|---|---:|---:|---|
| `sift_ransac` | `5257 / 6037` | `87.08%` | 原始 formal run，可用 |
| `akaze_ransac` | `5692 / 6037` | `94.29%` | 原始 formal run，可用 |
| `loftr_outdoor` | `5984 / 6037` | `99.12%` | 来自单独 accepted retry，不可再引用原始 OOM 包 |
| `roma_outdoor` | `6037 / 6037` | `100.00%` | 原始 formal run，可用 |
| `xoftr_official` | `5989 / 6037` | `99.20%` | 原始 formal run，可用 |
| `raw_minima` | `6037 / 6037` | `100.00%` | 原始 formal run，可用 |

其中，`LoFTR` 需要特别注意：

- 原始 `2026-06-26` formal run 中的 `LoFTR` 是全量 OOM 失败包；
- 当前论文可用的 `LoFTR` 结果必须来自：
  `formal_run_evidence_20260626/loftr_retry_20260628/`

## 3. UAV-TAlign 主方法结果

`uav_talign_full` 当前最重要的 scene-level 结果是：

- `15 / 15` scenes 有 scene homography
- `9 / 15` scenes 通过 strict canonical QA gate
- retention rate 为 `60.00%`
- retained scene ids 为：
  `01,04,05,06,07,08,10,12,14`

对应 canonical operating point 的关键量：

- pair coverage micro：`74.44%`
- accepted-attempted ratio micro：`64.71%`
- mean severe-outlier ratio：`0.009259`
- mean robust reject ratio：`0.113163`
- mean delta edge F1：`0.134312`
- mean delta grad NCC：`0.130337`

这组结果支撑的主线很明确：

- 我们的方法不是“所有 scene 都过”，而是在严格 scene-level gate 下仍然保留了 `9 / 15`；
- 保留结果具备明显条件区分性，因此 benchmark 不只是一个 pairwise 匹配任务，而是一个真正有 scene-level 难度分层的 UAV 双模态对齐任务；
- 这也反过来支持了数据集设计和 benchmark 设计的合理性。

## 4. 条件分解可以怎么讲

当前最稳定、最容易写进论文主线的条件分解是 `light_condition`：

- `day`: `5 / 7 = 71.43%`
- `night`: `3 / 5 = 60.00%`
- `lowlight`: `1 / 3 = 33.33%`

这个结果可以支撑以下叙事：

1. 白天条件下 scene-level QA gate 最稳定。
2. 夜间条件下仍然保留了较强的可用性，不是完全崩掉。
3. 低照是最困难场景，这个结论符合实际，也说明 benchmark 不是“容易数据集”。

## 5. 现在已经适合协作者写的内容

目前已经适合协作者开始写的部分：

1. benchmark 主结果表
2. `uav_talign_full` 的主结果段
3. `light_condition` 的条件分解段
4. protocol closure 对应的 supplement 表和 risk-coverage 相关描述

## 6. 现在还不建议定稿的部分

当前仍不建议直接定稿的部分：

1. `RIFT2`，因为还没有冻结成当前统一证据包的一部分
2. ablation wave，因为证据包还未冻结
3. multi-seed supplement，因为证据包还未冻结

## 7. 推荐下一步

最推荐的下一步不是直接改正文，而是：

1. 先用 `benchmark_master_summary_20260628.*` 和 `benchmark_table_figure_source_map_20260628.md` 统一口径；
2. 再决定 `RIFT2` 是否保留；
3. 然后冻结 ablation 和 multi-seed；
4. 最后再统一进入论文正文和补充材料写作。
