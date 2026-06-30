# 补充实验验收状态说明（2026-06-29）

这份说明记录 `P3-C / P3-D` 补充实验从远端重发、到本地验收冻结的完整状态。
它是本地审计说明，不进入论文正文。

## 1. 当前结论

截至 `2026-06-29`，补充实验已经完成远端运行并通过本地验收：

1. 远端补充 bundle 已正常结束，`exit_code=0`；
2. 7 个阶段均具备完整的 summary / config / results / scene-level 产物；
3. 关键证据已冻结到本地 `submission_materials/supplement_run_evidence_20260629/`；
4. 当前补充实验已经从 `running / pending acceptance` 转为：
   `accepted / locally frozen`

远端 accepted bundle：

- `G:\UAV-TAlign\UAV-TAlign\outputs\ipt_p3p5_supplement_bundle_20260629_133127`

本地 freeze root：

- `submission_materials/supplement_run_evidence_20260629/`

## 2. 远端完成状态

`launcher_summary.txt` 已确认：

- `launched_at=2026-06-29 13:31:27`
- `worker_started_at=2026-06-29 13:31:27`
- `worker_finished_at=2026-06-29 14:30:01`
- `exit_code=0`

已完成阶段：

- `A1_candidate_only`
- `A2_candidate_plus_aggregation`
- `A3_candidate_plus_aggregation_plus_qa`
- `S1_random_selection_seed0`
- `S1_random_selection_seed1`
- `S1_random_selection_seed2`
- `S1_random_selection_seed3`

## 3. 本地验收结果

### 3.1 完整性检查

本地已逐阶段验收以下核心文件：

- `experiment_config.json`
- `main_experiment_summary.json`
- `_stage_stdout.txt`
- `_stage_stderr.txt`
- `uav_talign_full_scene_metrics_detailed.jsonl`
- `uav_talign_full/results.json`
- `uav_talign_full/results.jsonl`
- `uav_talign_full/scene_results.jsonl`
- 每个阶段 8 个 `scene_result.json`

验收结果：

- `ablation`：4 个阶段全部完整
- `multiseed`：4 个 seed 全部完整

### 3.2 冻结结构

当前本地已冻结：

- `submission_materials/supplement_run_evidence_20260629/ablation/`
- `submission_materials/supplement_run_evidence_20260629/multiseed/`
- `submission_materials/supplement_run_evidence_20260629/remote_audit/`

并已生成：

- `ablation/sha256_manifest.txt`
- `multiseed/sha256_manifest.txt`
- `remote_audit/sha256_manifest.txt`

## 4. 当前补充实验核心结果

### 4.1 Ablation

在当前 `1K` 子集、8 个 scene 的口径下：

- `A1_candidate_only`：`8/8` canonical pass，接受帧均值 `13.625`
- `A2_candidate_plus_aggregation`：`8/8` canonical pass，接受帧均值 `13.625`
- `A3_candidate_plus_aggregation_plus_qa`：`5/8` canonical pass，接受帧均值 `26.0`
- `S1_random_selection_seed0`：`5/8` canonical pass，接受帧均值 `26.625`

这个结果说明：

- `A1/A2` 在 canonical scene pass 上更宽松，但接受帧量明显偏低；
- 引入 `A3` 后，scene-level gate 明显变严格，但保留帧统计更接近正式方法使用形态；
- `seed0` 与 `A3` 的量级接近，适合作为后续随机敏感性分析的基线。

### 4.2 Multi-seed

当前 4 个 seed 的 canonical pass 数为：

- `seed0`：`5/8`
- `seed1`：`5/8`
- `seed2`：`7/8`
- `seed3`：`5/8`

对应接受帧均值：

- `seed0`：`26.625`
- `seed1`：`26.75`
- `seed2`：`26.625`
- `seed3`：`28.125`

这个结果说明：

- 当前随机敏感性存在，但总体不呈现完全失稳；
- `seed2` 明显优于其余 seed，是当前需要重点解释的波动点；
- `accepted_frames_mean` 的波动较小，说明随机性主要反映在 strict scene pass 上。

## 5. 当前写作状态

补充实验现在可以进入“写作支持”层，但仍建议保持两条规则：

1. 先用本地 frozen evidence 和摘要表支撑写作；
2. 在论文正文落笔前，再决定补充实验最终采用哪种叙事粒度和表格呈现方式。

当前状态更新为：

- `ablation wave`：**accepted / locally frozen**
- `multi-seed supplement`：**accepted / locally frozen**

## 6. 下一步

下一步优先级建议为：

1. 统一 benchmark 主线与补充实验主线的叙事口径；
2. 决定 ablation 表和 multi-seed 表在正文还是补充材料呈现；
3. 把当前 frozen evidence 映射进 benchmark source map 和 paper checklist；
4. 再进入协作者论文写作阶段。
