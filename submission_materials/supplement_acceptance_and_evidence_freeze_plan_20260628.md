# 补充实验验收与证据冻结计划（2026-06-28）

这份文档服务于当前 `P3-A ~ P5` 三大区中的“补充实验”和“证据筛选”两条线。
它不进入论文正文，主要用于本地验收、证据冻结和协作者移交。

## 1. 目标

当前补充实验只覆盖两块：

- cumulative ablation wave
- multi-seed sensitivity supplement

当前验收目标不是立刻写正文，而是先把下面三件事闭环：

1. 远端输出目录真实存在且可复核；
2. 每个 stage / seed 有完整 `main_experiment_summary.json` 与 `uav_talign_full` 结果文件；
3. 本地形成可追溯的 frozen evidence bundle、摘要表和简短解释说明。

## 2. 当前运行口径

补充实验统一使用：

- 数据集：`UAV-TAlign-1K`
- 方法：`uav_talign_full`
- 设备：`cuda:0`
- scene 子集：`01,02,03,04,07,08,13,14`

ablation wave 当前包含四个 stage：

1. `A1_candidate_only`
2. `A2_candidate_plus_aggregation`
3. `A3_candidate_plus_aggregation_plus_qa`
4. `S1_random_selection_seed0`

multi-seed 当前包含：

1. `seed1`
2. `seed2`
3. `seed3`

## 3. 远端验收清单

### 3.1 Ablation

每个 ablation stage 必须检查：

- `main_experiment_summary.json`
- `experiment_config.json`
- `uav_talign_full/results.jsonl`
- `uav_talign_full/scene_results.jsonl`

需要抽取的核心字段：

- `status_counts`
- `qa_status_counts`
- `canonical_scene_pass_count`
- `accepted_frames_summary`
- `runtime_sec_summary`

### 3.2 Multi-seed

每个 seed 必须检查：

- `main_experiment_summary.json`
- `experiment_config.json`
- `uav_talign_full/results.jsonl`
- `uav_talign_full/scene_results.jsonl`

需要抽取的核心字段：

- retained scenes / 8
- accepted ratio
- QA status counts
- seed-to-seed spread

## 4. 本地冻结结构

补充实验一旦验收通过，本地建议冻结为：

- `submission_materials/supplement_run_evidence_<date>/ablation/`
- `submission_materials/supplement_run_evidence_<date>/multiseed/`

每个子目录至少包含：

- 远端 launcher summary
- launcher log
- `main_experiment_summary.json`
- `results.jsonl`
- `scene_results.jsonl`
- `sha256_manifest.txt`
- `acceptance_notes.md`

## 5. 预期产出

补充实验完成后，本地至少应补齐三类文件：

1. ablation summary 表
2. multi-seed summary 表
3. 一页中文验收说明

这些文件优先服务于：

- benchmark 设计闭环检查
- 协作者写结果段落
- 后续补正文前的统一口径

## 6. 当前状态

截至 `2026-06-29`，主 benchmark 证据已基本闭环，但补充实验证据仍处于：

- `running / pending acceptance`

补充说明：

- `2026-06-28` 的早期 supplement bundle 多次失败，主要原因是：
  1. 轻量 `1K` 子集 scene 名与原始 `12K` scene 名不一致；
  2. Windows worker 将 Python `stderr` warning 误判为失败。
- 这两个问题都已经修复。
- 当前正式重发根目录为：
  `G:\UAV-TAlign\UAV-TAlign\outputs\ipt_p3p5_supplement_bundle_20260629_133127`
- `debug_ab1_20260629` 已经提供了 `A1_candidate_only` 的中间可运行性证据，
  证明方法主链路在远端 `UAV-TAlign-1K` 上可以实际执行。

因此在补充实验正式验收前，以下内容仍保持 pending：

- ablation table 最终冻结
- multi-seed sensitivity table 最终冻结
- 进入正文的补充结果段
