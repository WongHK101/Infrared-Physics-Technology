# 中文审阅稿同步约定

## 文件

- 英文投稿主文件：`paper.tex`
- 英文章节：`sections/*.tex`
- 中文审阅主文件：`paper_zh.tex`
- 中文章节：`sections_zh/*_zh.tex`
- 中文审阅 PDF：`paper_zh.pdf`
- 编译命令：`powershell -ExecutionPolicy Bypass -File build_zh.ps1`

## 同步规则

英文稿是实验事实、数值、公式、表格和引用的唯一来源。每次修改英文稿后，应同步更新对应的
中文章节，再重新编译 `paper_zh.pdf`。中文稿可调整句序以便阅读，但不得修改结论强度、实验
数字、公式符号、表格数据、图号或引用键。

| 英文文件 | 中文镜像 |
|---|---|
| `paper.tex` | `paper_zh.tex` |
| `sections/01_introduction.tex` | `sections_zh/01_introduction_zh.tex` |
| `sections/02_related_work.tex` | `sections_zh/02_related_work_zh.tex` |
| `sections/03_dataset_protocol.tex` | `sections_zh/03_dataset_protocol_zh.tex` |
| `sections/04_method.tex` | `sections_zh/04_method_zh.tex` |
| `sections/05_experimental_setup.tex` | `sections_zh/05_experimental_setup_zh.tex` |
| `sections/06_results.tex` | `sections_zh/06_results_zh.tex` |
| `sections/07_discussion.tex` | `sections_zh/07_discussion_zh.tex` |
| `sections/08_conclusion.tex` | `sections_zh/08_conclusion_zh.tex` |

## 固定术语

| English | 中文 |
|---|---|
| infrared-visible alignment | 红外-可见光对齐 |
| RGB-infrared pair | RGB-红外图像对 |
| pairwise homography evidence | 成对单应性证据 |
| scene transform | 场景变换 |
| high-confidence scene product | 高置信场景产品 |
| canonical operating point | 规范运行点 |
| cross-modal scene verification | 跨模态场景验证 |
| reliability--coverage profile | 可靠性--覆盖率曲线 |
