# UAV-TAlign 正式补充实验说明（2026-06-26）

## 1. 这份证据包是什么

这份目录记录的是本次 `UAV-TAlign-12K` 正式长跑完成后的关键证据整理结果。

它的定位不是“原始实验根目录备份”，而是：

- 保留远端原始结果不动；
- 把论文写作真正需要的主实验 summary、关键 JSONL、协议闭环 CSV/PNG 拉回本机；
- 固定一份中文说明，方便后续协作者直接据此写主文、补充材料和回复说明。

远端原始证据位置：

- 主实验输出：
  `G:\UAV-TAlign\UAV-TAlign\outputs\ipt_p0c_12k_main`
- 协议闭环输出：
  `G:\UAV-TAlign\UAV-TAlign\outputs\ipt_p0d_protocol_closure`
- 验收审计目录：
  `G:\UAV-TAlign\_audit\p2d_acceptance_20260626_111420`

---

## 2. 本次正式运行口径

- 执行主机：独立 Windows RTX 4090 工作站
- 代码仓库：
  `G:\UAV-TAlign\UAV-TAlign`
- 代码提交：
  `c55e39e49cda508bae68520f718894bb0c761cec`
- 实验环境前缀：
  `G:\UAV-TAlign\uav_talign_envs\uav-talign-e10a8be-py310`
- 官方评测 manifest canonical SHA256：
  `a092f7ad00c6e02ead3bd39de5c246001f1d4bebbc4105ba715ef37bbb202c6c`
- 正式评测 pair 数：
  `6037`
- 正式评测 scene 数：
  `15`

主实验 launcher 记录为：

- `exit_code = 0`
- 自动 validator 记录为：
  `ok = true`

因此从“流程级验收”角度，这次正式长跑已经完成。

---

## 3. 当前可以直接用于论文的证据

## 3.1 Pairwise baseline 结果

以下结果可以作为本轮正式运行的有效证据：

| Method | H available | 比例 | 备注 |
|---|---:|---:|---|
| `sift_ransac` | `5257 / 6037` | `87.08%` | 可用 |
| `akaze_ransac` | `5692 / 6037` | `94.29%` | 可用 |
| `roma_outdoor` | `6037 / 6037` | `100.00%` | 可用 |
| `xoftr_official` | `5989 / 6037` | `99.20%` | 可用 |
| `raw_minima` | `6037 / 6037` | `100.00%` | 可用 |

## 3.2 UAV-TAlign 主方法结果

`uav_talign_full` 本轮正式结果为：

- `15 / 15` scenes 有 scene-level homography
- `9 / 15` scenes 通过 strict canonical QA gate
- 状态分布：
  - `pass = 8`
  - `pass_with_warning = 1`
  - `canonical_fail = 6`
- canonical retained scene ids：
  `01, 04, 05, 06, 07, 08, 10, 12, 14`

canonical operating point 对应的关键量：

- scene coverage：
  `60.0%`
- pair coverage micro：
  `74.44%`
- mean reliability score：
  `75.94`
- mean severe-outlier ratio：
  `0.0093`
- mean robust reject ratio：
  `0.1132`
- mean delta edge F1：
  `0.1343`
- mean delta grad NCC：
  `0.1303`
- accepted/attempted micro：
  `64.71%`

## 3.3 条件分解结果

按 `light_condition` 统计的 canonical retained 结果：

- `day`:
  `5 / 7 = 71.4%`
- `night`:
  `3 / 5 = 60.0%`
- `lowlight`:
  `1 / 3 = 33.3%`

这三组结果已经和我们希望在论文中强调的主线一致：

- 白天最稳定；
- 夜间仍有较强保留能力；
- 低照场景最难，但仍有可通过 scene；
- UAV 视角下的 scene-level gate 是有区分性的，而不是“全部过”或“全部不过”。

---

## 4. LoFTR 补充进展与 caveat

## 4.1 原始正式包中的 LoFTR 失败记录仍需保留

`loftr_outdoor` 在本次正式长跑中：

- `6037 / 6037` 全部为 `error`
- 错误类型统一为：
  `OutOfMemoryError`

因此：

- 这次正式 run 的 LoFTR 结果不能直接作为论文终稿主表证据；
- 如果主文必须保留 LoFTR 正式对比，需要后续单独做一次 memory-aware 重跑；
- 当前原始正式包里，LoFTR 只能作为“本轮正式 run 失败记录”，不能作为性能结果引用。

## 4.2 LoFTR 已完成补充重跑并通过验收

后续我们已经单独完成 `LoFTR-only` memory-aware 正式重跑，证据位置为：

- `loftr_retry_20260628/`

该补充包的正式验收结论为：

- launcher `exit_code = 0`
- validator `ok = true`
- `6037 / 6037` 记录完整
- `5984` 条 `homography_available = true`
- `0` 条 `error`
- 运行口径固定为：
  - `loftr_match_max_dim = 1200`
  - `loftr_use_amp = true`

因此现在论文可引用的 LoFTR 结果应当来自：

- `loftr_retry_20260628/main_outputs/`

而不是原始 `main_outputs/loftr_outdoor_results.jsonl` 那份 OOM 失败记录。

## 4.3 自动 validator 的历史盲点与当前状态

本轮 `check_prcv_main_outputs.py` 自动校验通过，原因是它目前主要检查：

- 文件存在性
- 行数完整性
- manifest / scene count / pair count

它没有进一步判定：

- 某个 baseline 是否出现 `6037/6037 all-error`

这是“原始正式包”的历史问题。现在这个盲点已经补上，新的 validator 已增加：

- `all-error` baseline 拒绝规则
- `homography_available_count = 0` 拒绝规则

因此当前 benchmark 级结论应当写成：

- `原始正式包结构验收通过`
- `LoFTR 原始包语义失败，但失败记录已保留`
- `LoFTR 补充重跑验收通过`
- `当前 benchmark 主链路语义闭环成立`

---

## 5. Protocol closure 的额外说明

协议闭环脚本第一次在实验前缀环境里失败，不是因为主实验结果坏掉，而是因为：

- `G:\UAV-TAlign\uav_talign_envs\uav-talign-e10a8be-py310`
  缺少 `pandas`

随后我们使用远端基础 Python：

- `D:\anaconda\python.exe`

对同一份 `ipt_p0c_12k_main` 输出做了只读后处理，成功生成：

- `canonical_operating_point.csv`
- `per_scene_reliability_table.csv`
- `threshold_sensitivity.csv`
- `condition_reliability_profile.csv`
- `risk_coverage.csv`
- `paper_facing_summary.md`
- 对应 PNG 图

这一步没有修改主实验原始结果，只是修复了后处理环境与字段兼容问题。

---

## 6. 这份目录里最值得直接引用的文件

如果接下来要写论文或给协作者分工，建议优先看这些文件：

### 主实验证据

- `main_outputs/main_experiment_summary.json`
- `main_outputs/validate_stdout.json`
- `main_outputs/uav_talign_full_results.jsonl`

### 场景级协议证据

- `protocol_closure/paper_facing_summary.md`
- `protocol_closure/canonical_operating_point.csv`
- `protocol_closure/per_scene_reliability_table.csv`
- `protocol_closure/condition_reliability_profile.csv`
- `protocol_closure/risk_coverage.csv`

### 审计与回溯

- `remote_audit/acceptance_notes.md`
- `remote_audit/sha256_manifest.txt`

---

## 7. 现在可以怎么用这批证据

当前这批结果已经足够支撑：

1. 写 `UAV-TAlign full` 的正式 scene-level 主线结果；
2. 写 `SIFT / AKAZE / RoMa / XoFTR / raw MINIMA` 的正式 baseline 结果；
3. 写 supplement 里的：
   - per-scene reliability table
   - condition reliability profile
   - threshold sensitivity
   - risk-coverage curve

当前还不建议直接定稿的部分主要变成：

1. `RIFT2` 若仍要保留，则需要补足正式证据；
2. ablation / multiseed 若要进入最终补充材料，需要继续冻结证据包；
3. 论文正文里的总表与图注尚未统一改写。

---

## 8. 下一步建议

建议后续按这个顺序推进：

1. 用本目录里的 `UAV-TAlign full + 五个原始可用 baseline + LoFTR 补充包` 写 benchmark 主线；
2. 单独决定是否现在补 `RIFT2` 正式证据；
3. 如果需要，我下一步可以继续：
   - 把这批关键数字整理进 paper tables 草稿；
   - 生成论文正文可直接引用的中英文结果摘要；
   - 继续整理 ablation / multiseed / RIFT2 的证据闭环。
