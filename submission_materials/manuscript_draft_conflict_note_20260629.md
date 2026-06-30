# Manuscript Draft Conflict Note (2026-06-29)

This note records the main conflicts between the current manuscript draft and
the accepted local evidence layer. It is a writing-protection note only.

## 1. Why This Note Exists

The current manuscript draft already contains many strong sentences and a
mostly correct paper structure. However, some numbers were written before the
latest evidence freeze and should not be copied forward blindly.

This note highlights the major conflicts that matter most for the next writing
pass.

## 2. Main Conflicts

### Conflict A: `LoFTR` row in the main benchmark table

Current draft location:

- `sections/06_results.tex`, table row for `Kornia LoFTR outdoor`

Draft value:

- `6009/6037`, `99.54`

Accepted writing-safe value:

- `5984/6037`, `99.12`

Reason:

- the draft row reflects an outdated pre-freeze result
- the accepted value must come from the standalone retry evidence pack

### Conflict B: `RIFT2` in abstract, highlights, and main results

Current draft locations:

- `paper.tex` abstract
- `paper.tex` highlights
- `sections/06_results.tex`

Current risk:

- the draft presents `RIFT2` as if it were already frozen in the same accepted
  evidence structure as the other benchmark rows

Current project rule:

- `RIFT2` is still deferred unless we explicitly freeze a formal local accepted
  evidence pack

### Conflict C: scene-level main table accepted-frame row

Current draft location:

- `sections/06_results.tex`, `tab:scene_level_main`

Draft value:

- `2473/3847`, `64.3`

Accepted writing-safe scene-level values:

- retained scenes: `9/15`
- retention rate: `60.00%`
- pair coverage micro: `74.44%`
- accepted-attempted ratio micro: `64.71%`

Risk:

- the current accepted-frame row in the draft is not aligned with the accepted
  protocol-closure writing layer

### Conflict D: random-selection spread

Current draft location:

- `sections/06_results.tex`, cumulative ablation paragraph

Draft wording:

- `4/8 to 7/8`

Accepted writing-safe wording:

- `5/8 to 7/8`

Reason:

- the accepted local supplement freeze now fixes the current frozen spread

### Conflict E: ablation table values

Current draft location:

- `sections/06_results.tex`, `tab:ablation_main`

Current risk:

- the table uses a paper-facing proxy summary that has not yet been updated to
  the newly frozen supplement numbers

Writing rule:

- rebuild or restate this table from:
  `supplement_run_evidence_20260629/ablation/ablation_summary_20260629.md`

## 3. What Is Still Safe To Reuse

The following manuscript-level ideas remain structurally good and do not need a
conceptual rewrite:

- the abstract framing from pairwise evidence to scene-level retention
- the dataset chapter structure
- the result-section ordering
- the reliability-coverage discussion logic
- the high-level cumulative ablation narrative

So the next writing pass should mostly be treated as:

- number alignment
- evidence-source alignment
- selective wording cleanup

not as a full paper rewrite.

## 4. Writing Rule for the Next Pass

Before editing any manuscript body table or result sentence, first map it to:

- `benchmark_master_summary_20260628.*`
- `benchmark_table_figure_source_map_20260628.md`
- `supplement_run_status_note_20260629.md`
- `supplement_run_evidence_20260629/ablation/ablation_summary_20260629.md`
- `supplement_run_evidence_20260629/multiseed/multiseed_summary_20260629.md`

If a sentence cannot be traced to one of these accepted local sources, it should
be treated as draft-only and revalidated before use.
