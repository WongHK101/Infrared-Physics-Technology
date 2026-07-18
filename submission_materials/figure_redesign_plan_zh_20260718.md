# UAV-TAlign-12K 主文图件重构方案

日期：2026-07-18

## 1. 审查结论

当前手稿的主要视觉差距不在于单纯少了若干图号，而在于视觉证据链尚未完整展开。现有 25 页手稿包含 4 张主图，第一张图直到数据集章节才出现，且结果部分没有展示任何成对基线对比、场景级对齐前后效果或可靠性筛选案例。四篇参考论文共同采用了更完整的视觉叙事：先用首屏图建立问题，再用结构图解释方法，随后用中间表示、定量曲线和大幅定性结果逐层闭合证据。

本文建议从 4 个主图组升级为 9 个主图组。9 个图组对应约 0.36 个图组/页，接近 RoMa 和 SelectiveNet 的视觉密度，低于 TWMM 的高密度图像型写法，适合当前 25 页期刊稿。重点不是增加装饰，而是让每个核心结论至少获得一张直接、可独立阅读的视觉证据。

## 2. 四篇参考论文的图件策略

| 论文 | 页数 | 编号图 | 表格 | 图件组织方式 | 本文应借鉴的核心做法 |
|---|---:|---:|---:|---|---|
| Gao et al., TGRS 2025, UAVMatch | 14 | 12 | 6 | 第 1 页展示传感器与跨视场问题；随后依次给出数据生成、网络总览、模块结构、定量曲线和整页算法对比 | 首图建立任务张力；方法图拆成总览与模块；定性结果采用统一网格和局部放大 |
| Edstedt et al., CVPR 2024, RoMa | 11 | 4 | 8 | 第 1 页以困难案例作为 hero figure；第 2 页立即给出方法图；后续两图解释局部可定位性和损失梯度 | 图数不必很多，但首图必须展示能力，方法图必须突出相对已有方案的新设计 |
| Geifman and El-Yaniv, ICML 2019, SelectiveNet | 9 | 3 | 6 | 一张架构图、一张风险-覆盖率曲线、一张表征可视化，曲线直接服务核心理论命题 | 可靠性曲线必须简单、单义，并把 coverage 与 risk 的运行含义讲清楚 |
| Meng et al., ISPRS JPRS 2022, TWMM | 26 | 18 | 8 | 问题差异、形变、匹配机制、采集设备、中间相似度图、模块消融和连续多页定性结果逐层展开 | 用真实中间表示解释方法，而非只画流程框；结果区需要大幅 before/after、棋盘格和局部放大 |
| UAV-TAlign 当前稿 | 25 | 4 | 6 | 数据样例、单行方法流程、单一 illumination 柱图和默认风格风险曲线 | 缺少首屏 hero、机制图、基线视觉证据、场景级定性结果和验证可视化 |

## 3. 当前图件资产审查

| 当前资产 | 审查结果 | 新方案中的位置 |
|---|---|---|
| `figures/fig_dataset_examples.pdf` | 真实样例清晰，但仅 4 对图像，尺度偏小，不能独立建立 benchmark 规模与跨视场难度 | 作为新 Fig. 1 的样例源，不再原样使用 |
| `figures/fig_method_pipeline.pdf` | 流程完整，但横向五框在版面中字号过小，也没有真实输入、场景假设分布和最终产品 | 重绘为新 Fig. 3 的两层结构 |
| `figures/fig_condition_reliability_profile.pdf` | 仅展示 illumination，默认柱图信息密度低 | 与 rendering、view profile 合并为新 Fig. 8 |
| `figures/fig_risk_coverage_curve.pdf` | 数值有效，但多条不同量纲曲线共用双轴，canonical 点与 score-ranked 曲线的关系不够直观 | 拆解并重绘为新 Fig. 8 的核心 panel |
| `figures/fig_benchmark_protocol_image2.png` | 已具备三轨评测概念，但微型文字过多、图标化较重 | 简化为新 Fig. 2 的协议主框架 |
| `figures/fig_scene_reliability_principle_image2.png` | 当前最有价值的未入稿机制素材，已覆盖假设分布、共识、QA 和 retain-vs-rank | 作为新 Fig. 4 的结构基础，替换为真实数据驱动的中间表示 |
| `figures/fig_proxy_reliability.pdf` | 15 场景散点能直观解释 QA 信号 | 作为新 Fig. 7 的定量 panel |
| `figures/fig_ablation_sensitivity.pdf` | 消融与多 seed 信息完整，但仍是独立默认绘图风格 | 与重采样、扰动验证统一为新 Fig. 9 |
| `figures/fig_uav_talign_overview_image2.png` | 叙事结构好，但在论文宽度下文字过密 | 作为 Fig. 3 和 Fig. 4 的节点来源，不作为最终图 |
| `figures/fig_uav_talign_architecture_image2.png` | 模块最完整，但视觉层级过多，缩放后难以阅读 | 仅作内部结构参考 |
| `figures/framwork.pdf` | 与当前方法流程重复 | 退役，不再进入主文或补充材料 |

## 4. 新的主文视觉叙事链

读者应按以下顺序仅通过图件就能理解全文：

1. 看见跨视场、跨分辨率、跨光照红外-可见光对齐问题，以及 UAV-TAlign-12K 的真实规模。
2. 理解 official manifest、三层评测单元和场景级可靠性协议如何组织 benchmark。
3. 理解 UAV-TAlign 如何把成对证据转换为场景变换。
4. 看见多帧假设为何需要质量加权、鲁棒共识和跨模态验证。
5. 看见传统、红外专用与现代匹配器在统一评测下提供何种证据。
6. 直接检查高置信场景产品的对齐前后效果。
7. 理解 canonical gate 如何在匹配证据充分时区分可交付场景产品。
8. 理解可靠性与覆盖率的连续运行空间，以及不同采集条件下的表现结构。
9. 通过重采样、受控扰动和累加式消融验证各模块作用。

## 5. 九张主文图的逐图设计

### Fig. 1. Cross-FOV UAV infrared-visible alignment at a glance

**插入位置：** Introduction 第一页或第二页，首次定义问题后。

**核心结论：** UAV-TAlign-12K 覆盖真实 H30T 同步采集下的跨视场、跨分辨率、跨光照红外-可见光场景，对齐任务的最终单位是可交付的场景变换，而非孤立的匹配点。

**建议版式：** 全宽 hero figure，三层结构。

- (a) M350 + H30T 同步采集示意：同一时刻 RGB 与 infrared 产品、不同分辨率和视场范围。
- (b) 6 组代表性原始图像对：day/night/lowlight、grayscale/pseudocolor、wide/zoom/general。
- (c) 一个代表场景的 raw pair、未对齐叠加、对齐后叠加和场景产品图标。
- (d) 紧凑 dataset card：15 scenes、6,039 candidate pairs、6,037 integrity-checked evaluation pairs。

**推荐样例：** S01 day-gray-wide、S04 night-gray-zoom、S05 night-pseudo、S06 day-pseudo、S13 lowlight-pseudo-road、S14 lowlight-pseudo-tower。

**可用素材：** 当前 dataset examples、release metadata、selected RGB/infrared crops、before/after overlay。

**参考范式：** RoMa Fig. 1 的首屏能力展示；UAVMatch Fig. 1 的传感器问题定义；TWMM Fig. 1 的跨模态差异可视化。

### Fig. 2. Benchmark organization and multi-level evaluation protocol

**插入位置：** Dataset and Protocol，数据组织说明之后。

**核心结论：** benchmark 由固定 manifest 驱动，并在 pairwise evidence、scene-level product、reliability-coverage profile 三个互补层级上评测。

**建议版式：** 2 x 2 多面板。

- (a) 15-scene atlas 或场景条带，按 scene family 分组。
- (b) 每场景 pair count 与 illumination/rendering/view 标签矩阵。
- (c) integrity flow：6,039 candidate pairs -> 6,037 evaluation pairs，并标出 manifest hash 图标。
- (d) 三轨评测流程：pairwise evidence -> scene product -> operating profile。

**可用素材：** release metadata bundle、per-scene/per-condition CSV、`fig_benchmark_protocol_image2.png`。

**参考范式：** UAVMatch Fig. 2-3 的数据构建流程，但本文突出真实采集、固定 manifest 与多层评测，而非合成变换生成。

### Fig. 3. UAV-TAlign scene-level alignment framework

**插入位置：** Method 开头，问题定义之后。

**核心结论：** UAV-TAlign 是完整的场景级证据整合框架，而非单次 matcher 后处理。

**建议版式：** 上层为主流水线，下层为三个关键模块的放大框。

- 主流水线：scene frame pool -> progressive evidence scheduling -> pairwise homographies -> geometry-calibrated weighting -> robust consensus -> cross-modal verification -> high-confidence scene product。
- 模块 A：候选证据的渐进式调度和覆盖。
- 模块 B：单应性参数空间中的质量加权与鲁棒聚合。
- 模块 C：canonical gate 与 continuous reliability ranking 的并行输出。

**设计要求：** 真实 RGB/infrared 缩略图只在入口和输出出现；每个模块最多 2 行文字；最终印刷尺寸下正文标签不小于 8 pt。

**可用素材：** `fig_method_pipeline.pdf`、`fig_uav_talign_overview_image2.png`、`fig_uav_talign_architecture_image2.png`。

**参考范式：** RoMa Fig. 2 的单页贡献图。使用统一绿色强调本文新增模块，灰色表示通用 matcher/backbone。

### Fig. 4. From heterogeneous frame hypotheses to a reliable scene transform

**插入位置：** Robust Scene Consensus 与 Cross-Modal Verification 两小节之间或之后。

**核心结论：** 鲁棒共识与 QA 验证将分散、异质的 frame-level hypotheses 转换为稳定场景变换，并显式抑制偏离共识的证据。

**建议版式：** 四个连续 panel，至少两个 panel 使用真实场景数据。

- (a) 同一场景 12 个 frame-level homography 对应的角点位移或参数分布。
- (b) 质量权重编码：点大小表示 support，颜色表示 cross-modal quality。
- (c) median/MAD 筛选前后，显示 dispersion 收缩和 consensus cluster。
- (d) canonical gate 与 score ranking 的双输出关系，明确二者服务不同运行接口。

**可用素材：** per-scene hypotheses、scene summaries、`fig_scene_reliability_principle_image2.png`。

**参考范式：** TWMM Fig. 3-4 和 Fig. 10-13 对中间表示的逐步可视化。该图是证明方法创新不只是包装 matcher 的关键图。

### Fig. 5. Pairwise evidence across matcher families

**插入位置：** Results 的 Pairwise Baseline Comparison 小节。

**核心结论：** 传统关键点、红外专用方法和现代稠密/学习型匹配器提供不同形态的几何证据；availability、spatial support、fit residual 和 runtime 必须联合解读。

**建议版式：** 上半部分为指标概览，下半部分为固定样例的视觉对比。

- (a) 七种方法的 homography availability 与 mean coverage 点图，不使用综合排名。
- (b) 两个固定困难样例的 checkerboard 或 cyan-red overlay，对比 SIFT、RIFT2、LoFTR、XoFTR、RoMa 和 raw MINIMA。
- (c) 每个方法旁仅标注 availability/coverage，不在图中强调单一 best。

**样例选择：** 固定一个 night grayscale case 和一个 lowlight pseudocolor case；所有方法使用完全相同的 pair 和 crop。

**可用素材：** frozen 6,037-pair JSONL 中的 homography 与 metrics、local dataset images。RIFT2 per-pair homography 需要从 4090 strong-run output 补拷，不需要重新运行实验。

**参考范式：** UAVMatch Fig. 10-11 的统一方法网格；TWMM Fig. 15 的同图像、多方法、局部放大对比。

### Fig. 6. High-confidence scene alignment products across operating conditions

**插入位置：** Scene-Level Performance 小节，canonical table 之后。

**核心结论：** UAV-TAlign 在 day、night、lowlight 和 pseudocolor 条件下都能输出可检查的高置信场景变换。

**建议版式：** 4 行 x 5 列，整页或接近整页宽度。

- 行：S01 day-gray-wide、S04 night-gray-zoom、S06 day-pseudo-general、S14 lowlight-pseudo-general。
- 列：RGB、infrared、before overlay、after overlay、edge/checkerboard + zoom inset。
- 每行统一 crop，使用相同 overlay convention；局部放大框位置在 RGB、infrared 和 overlay 中保持一致。

**可用素材：** drawing-ready package 已有 S01、S04、S06、S14 的 RGB、infrared、before、after 和 edge crops。

**参考范式：** TWMM Fig. 16 的多场景全页定性展示；UAVMatch Fig. 12 的 raw/warped/fused 列结构。

### Fig. 7. Reliability-controlled scene product selection

**插入位置：** Scene-Level Performance 与 Reliability-Coverage 小节之间。

**核心结论：** canonical decision 根据场景级证据一致性选择高置信产品，即使 pairwise homography 本身普遍可用，也能识别 QA-relative outlier patterns。

**建议版式：** 左侧 matched controls，右侧全场景诊断图。

- (a) S01 wide retained vs S02 zoom filtered：同一场景族、同一 illumination/rendering，展示 after overlay 和 QA signature。
- (b) S04 zoom retained vs S03 wide filtered：夜间 matched control。
- (c) 15-scene accepted-frame ratio vs severe-outlier ratio 散点，canonical product 用绿色，QA-filtered scene 用中性灰/琥珀色。
- (d) 每个 control 旁显示 accepted ratio、severe outlier、robust reject ratio 三个微型指标，不堆叠全部 warning code。

**可用素材：** S01/S02/S03/S04 selected crops、`fig_proxy_reliability.pdf`、per-scene reliability CSV。

**参考范式：** SelectiveNet 对 accept/reject 的直接可视化逻辑；RoMa Fig. 1 的案例先行表达。

### Fig. 8. Reliability-coverage operating profile and condition structure

**插入位置：** Reliability-Coverage Operating Profile 小节。

**核心结论：** 固定 score ranking 暴露连续的 reliability-coverage operating space；canonical gate 在该空间中定义一个独立、严格的交付点。

**建议版式：** 2 x 2 panel。

- (a) 主图：x 轴 scene coverage，y 轴 mean severe-outlier ratio，单条 risk curve。
- (b) pair coverage 与 accepted support 随 scene coverage 的变化，使用同一横轴但独立 panel，不使用双 y 轴。
- (c) illumination profile：day/night/lowlight 的 scene-product coverage 和 accepted ratio。
- (d) thermal rendering 与 view type 的 compact dot plot。

**固定标注：** canonical star = 9/15 scenes、60.0% scene coverage、74.4% pair coverage。图注必须说明 star 对应 canonical product set，不等于 score-ranked top-9 set。

**可用素材：** risk coverage CSV、condition reliability profile CSV、current risk/condition plots。

**参考范式：** SelectiveNet Fig. 2 的单义 risk-coverage 曲线；避免当前多量纲曲线叠在同一双轴图上的视觉负担。

### Fig. 9. Independent validation and module attribution

**插入位置：** Controlled Validation 与 Ablation 两小节，可合并成一个视觉结果小节。

**核心结论：** 场景共识在重采样下保持稳定，联合质量信号对受控扰动单调响应，主要模块贡献由累加式消融和多 seed 结果共同支持。

**建议版式：** 2 x 2 panel。

- (a) Leave-frame-out：75 次 recomputation 的 drift distribution，标注 median 1.39 px、mean 2.26 px。
- (b) Translation/rotation/scale 扰动强度与 joint-score change 曲线，三类扰动分开显示。
- (c) Cumulative modules：pairwise evidence -> robust consensus -> cross-modal verification，显示 dispersion、severe outlier 和 proxy improvement。
- (d) Random selection multi-seed：固定 8-scene subset 上 5/8 至 7/8 的波动，并标记 deterministic operating policy。

**可用素材：** composite validation JSON、ablation summary、multiseed summary、`fig_ablation_sensitivity.pdf`。

**参考范式：** UAVMatch Fig. 8-9 的模块与敏感性曲线，但本文按 scene-level diagnostics 组织，不复制其训练网络式消融叙事。

## 6. 主文表格与图件重新分工

建议主文保留三张核心表：

1. 数据资源定位表。
2. 七种 pairwise baseline 的完整定量表。
3. Canonical scene-level operating point 表。

当前 condition table、controlled validation table 和 cumulative ablation table 的完整数值移入补充材料。主文用 Fig. 8 和 Fig. 9 承担趋势解释，在正文中保留最关键数值。这样可以在不增加重复信息的前提下显著提升视觉证据密度。

## 7. 补充材料图件建议

| 编号 | 内容 | 作用 |
|---|---|---|
| Fig. S1 | 15-scene complete atlas | 展示完整数据覆盖和 scene family |
| Fig. S2 | 七种 matcher 在 3-4 个固定样例上的完整视觉网格 | 补充主文 Fig. 5 的方法子集 |
| Fig. S3 | 15-scene reliability heatmap | 展示 accepted ratio、outlier、reject ratio、dispersion、edge/grad signals |
| Fig. S4 | Threshold sensitivity | 展示 conservative/balanced/permissive operating regimes |
| Fig. S5 | Reliability score component decomposition | 明确非训练 score 的构成和排序用途 |
| Fig. S6 | RIFT2 light vs strong sanity check | 支撑最终 resize-aware strong setting |
| Fig. S7 | SIFT/AKAZE status and per-condition completeness | 补齐 classical keypoint context |
| Fig. S8 | Additional high-confidence and QA-filtered examples | 扩展不同场景、渲染和照明条件 |
| Fig. S9 | Candidate selection multi-seed stability | 完整呈现 deterministic 与 random policy 的稳定性证据 |

## 8. 统一视觉规范

- 主文图优先使用全宽版式；最终双栏宽度下文字不小于 8 pt。
- 流程与统计图输出矢量 PDF/SVG；影像合成图保留 600 dpi TIFF/PNG 和可编辑源文件。
- 固定颜色语义：RGB/visible 为蓝色，infrared 为橙色，高置信产品为绿色，QA-filtered scene 为中性灰或琥珀色，canonical point 为深红色星形。
- 所有 overlay 统一采用 cyan-red 或 checkerboard convention，图注解释一次后全文复用。
- 不使用默认 Matplotlib 配色、双 y 轴堆叠、3D 柱图、渐变背景或装饰性图标墙。
- 不把 complementary diagnostics 合成为单一视觉排名。
- 所有 qualitative comparison 使用固定 pair、固定 crop、固定缩放和固定方法顺序。
- 不使用生成式 AI 制作数据样例或对齐结果；所有影像必须来自真实数据和冻结输出。
- pseudocolor thermal 保留 H30T 原始 palette，不重新着色。

## 9. 执行优先级与素材闭环

### P0：不新增实验即可完成

- Fig. 1 benchmark hero。
- Fig. 2 benchmark protocol。
- Fig. 3 framework overview。
- Fig. 4 consensus and verification mechanism。
- Fig. 6 high-confidence qualitative products。
- Fig. 7 reliability-controlled selection。
- Fig. 8 operating profile。
- Fig. 9 validation and ablation。

### P1：只需补拷冻结结果，不需重新实验

- Fig. 5 的 RIFT2 per-pair homography/visual output 从 4090 strong-run output 拷回。
- 其他 baseline 可直接使用 6,037-pair frozen JSONL 中的 homography 生成统一 checkerboard/overlay。

### P2：图件完成后的手稿集成

- 按 Fig. 1-9 顺序重排英文手稿的 figure references 和 Results 小节。
- 将 condition/validation/ablation 详细表迁入 supplement。
- 同步修改中文审阅稿并重新生成 `paper_zh.pdf`。
- 最终逐页检查图中文字、裁切、缩放、引用顺序和中英文图注一致性。

## 10. 最终裁决

当前手稿不应继续以 4 张低密度图作为投稿版本。建议正式冻结为 9 个主文图组和 9 个补充图组，其中主文 Fig. 1、Fig. 4、Fig. 5、Fig. 6、Fig. 8 是提升稿件说服力的五张关键图。该方案不改变算法结论，也不要求新增大规模实验；它主要把已经存在的数据、冻结输出和验证结果组织成与高水平 benchmark/method 论文相匹配的视觉证据链。
