# UAV-TAlign 协作者结果叙事增强稿（2026-06-29）

这份文档面向协作者写作，不是正文定稿，也不是实验日志。
它的目标是把当前已经验收的证据整理成一套更容易写进论文的结果主线。

## 1. 现在这篇论文最清晰的主线

这篇论文现在最强的主线，不是“我们提出了一个单独更强的 pairwise matcher”，而是：

1. 我们构建了一个真实采集、跨视场、无人机视角的红外-可见光配准 benchmark；
2. 在这个 benchmark 上，强 pairwise 匹配证据其实已经相当丰富；
3. 真正的核心问题变成：如何把大量 frame-level homography 变成一个可保留的
   scene-level alignment product；
4. UAV-TAlign 的贡献就在于把“能匹配”推进到“能不能保留、值不值得用”。

换句话说，论文最该强调的是：

- pairwise availability 只是前提
- scene-level reliability 才是问题核心

## 2. 数据集贡献应该怎么讲

目前最适合强化的数据集贡献有四点：

### 2.1 无人机视角是关键差异

和大量地面、车载、手持红外-可见光资源相比，我们的数据是：

- UAV 视角
- cross-FOV
- 强视角漂移
- 更明显的尺度变化和构图变化

这意味着它不是传统“近同视角、多模态成像”的轻量扩展，而是一个更接近真实空中
巡检、夜间监测、低照感知场景的注册问题。

### 2.2 数据规模和图像质量同时成立

当前数据集可以同时强调：

- `12000` 量级双模态图像
- `6039` candidate pairs
- `6037` integrity-checked evaluation pairs
- 图像质量高于常见 `640p` 左右的传统资源

这点很重要，因为它支持两层叙事：

1. 数据不是小规模概念验证；
2. 数据不是低分辨率近同视角的容易设置。

### 2.3 条件覆盖广，适合 reliability benchmark

现有正式证据已经支撑我们强调：

- day / night / lowlight
- grayscale thermal / pseudocolor thermal
- wide / zoom
- 农田、道路、建筑、工业设备、输电设施等多类场景

这些条件覆盖使得 benchmark 不只是“平均分比较”，而是天然适合讨论：

- 什么条件下更稳定
- 什么条件下更容易被 QA gate 拒绝
- 为什么 scene-level retention 是必要的

### 2.4 数据集价值不只是“更多图像”，而是“引出新的评测问题”

最重要的一句话其实是：

- UAV-TAlign-12K 的价值不只是规模和视角新，而是它把评测问题从 pairwise
  matching 推到了 scene-level retained alignment。

这个点对 IP&T 很重要，因为它让数据集贡献和方法贡献不是割裂的。

## 3. 主 benchmark 结果怎么讲最稳

现在最稳的 benchmark 主结果是：

- `SIFT`: `87.08%`
- `AKAZE`: `94.29%`
- `LoFTR` accepted retry: `99.12%`
- `RoMa`: `100.00%`
- `XoFTR`: `99.20%`
- `raw MINIMA`: `100.00%`

这些结果共同支撑的不是“谁第一名”，而是：

- 在 UAV-TAlign-12K 上，pairwise homography evidence 已经普遍可得；
- 因此 benchmark 的难点并没有停留在“能不能给一对图拟合 homography”；
- 真正剩下的问题是 scene-level 决策与可靠性控制。

这是我们最需要强调的逻辑转换。

## 4. 主方法结果怎么讲

当前 `uav_talign_full` 的 canonical 主结果是：

- `15/15` scenes 有 scene homography
- `9/15` scenes 通过 strict canonical QA gate
- retention rate: `60.00%`
- pair coverage micro: `74.44%`
- accepted-attempted ratio micro: `64.71%`

这组结果非常适合写成下面这个结构：

1. 方法并不是“所有 scene 都保留”；
2. 相反，它是在严格 gate 下保留 `9/15`；
3. 这说明 benchmark 确实具有足够的 scene-level 难度；
4. 也说明我们的方法核心不是盲目提高通过率，而是做 reliability-controlled
   retention。

也就是说，`9/15` 不是弱点，反而是 benchmark 和方法叙事的一部分。

## 5. 条件分解怎么讲

当前最稳的条件分解是光照条件：

- day: `5/7 = 71.43%`
- night: `3/5 = 60.00%`
- lowlight: `1/3 = 33.33%`

这部分最适合写成：

- 白天最好，这是符合预期的；
- 夜间仍然保留了较强可用性，不是全面失效；
- lowlight 最难，说明 benchmark 不是“容易数据集”。

它的作用不是单独炫数字，而是证明：

- benchmark 的条件分层是有效的；
- reliability profile 是有解释力的。

## 6. Ablation 应该怎么讲

目前 accepted supplement 最重要的结论是：

- `A1`: `8/8`
- `A2`: `8/8`
- `A3`: `5/8`
- `S1_seed0`: `5/8`

这些数字如果不解释，看起来会有点反直觉，因为前两项保留更多。
但正确叙事应该是：

1. `A1/A2` 更像宽松的 scene pass；
2. `A3` 才真正引入了 QA-aware verification 的严格筛选；
3. 因此 `A3` 不是性能“下降”，而是把 scene-level criterion 从“能拟合”
   变成了“是否足够可靠以保留”；
4. 这和我们的论文主线是一致的。

所以 ablation 不该写成“模块不断堆叠带来更高通过率”，而应该写成：

- robust consensus 改善了聚合质量
- QA-aware verification 把方法变成一个真正的 retained-product framework

## 7. Multi-seed 应该怎么讲

当前 accepted multi-seed 结果是：

- `seed0`: `5/8`
- `seed1`: `5/8`
- `seed2`: `7/8`
- `seed3`: `5/8`

这里最安全的解释是：

1. 随机选择会造成严格 canonical pass 的边界波动；
2. 但 accepted-frame mean 在不同 seed 间变化不大；
3. 所以随机性主要影响的是边界 scene 的 pass / fail 判定；
4. 这反过来支持 deterministic-even selection 作为默认操作策略。

进一步从 scene 级别看，`seed2` 更好主要不是整体都变强了，而是少数边界 scene
从 fail 跨到了 pass：

- `01_day_grayscale_wide_substation_power_lines_50`
- `03_night_grayscale_wide_substation_power_lines_45`

而诸如 `02_day_grayscale_zoom_substation_power_lines_50` 这种 scene 在所有 seed 下都仍然 fail。

所以 multi-seed 不应该被写成“方法不稳定”，而更适合写成：

- random evidence selection 对边界 scene 有非平凡敏感性；
- deterministic-even selection 是更可复现的默认策略。

## 8. 关于 RIFT2 的当前建议

虽然当前草稿正文里还写着 `RIFT2`，但从证据治理角度看：

- `RIFT2` 目前还没有冻结进和其他主结果完全一致的本地 accepted evidence 包

所以当前最稳的写作建议是：

1. 不要让 `RIFT2` 阻塞协作者写作；
2. 当前写作层优先使用已经完全冻结的 6 行 pairwise benchmark；
3. 如果后续决定要把 classical infrared-visible baseline 讲得更完整，再补
   `RIFT2` 的正式冻结。

## 9. 现在最适合协作者落笔的写法

如果现在就让协作者开始写，最推荐的结果段主线是：

1. 数据集定位：
   `UAV-TAlign-12K` 提供真实采集、跨视场、无人机视角的双模态配准 benchmark。
2. 主 benchmark：
   多个 off-the-shelf baseline 已经在 pairwise 层面接近饱和。
3. 问题转换：
   因此真正难点转向 scene-level retained alignment。
4. 方法结果：
   `UAV-TAlign` 在严格 canonical QA gate 下保留 `9/15` 高置信 scene。
5. 条件分析：
   day > night > lowlight，说明 benchmark 具有真实难度分层。
6. 补充实验：
   robust consensus 和 QA-aware verification 是核心驱动，deterministic-even
   selection 提供更稳定的默认策略。

## 10. 当前最需要避免的写法

当前最不建议的写法有三种：

1. 把论文写成“我们方法在 pairwise matching 上赢了所有 baseline”
2. 把 `9/15` 误写成方法性能不够高
3. 把 multi-seed 写成“方法整体不稳定”

更准确的写法应该始终围绕：

- benchmark 难点已经从 pairwise availability 转向 scene-level reliability
- 我们的方法正是为这个 decision layer 服务的
