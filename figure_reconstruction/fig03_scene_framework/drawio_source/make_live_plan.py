from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent

INK = "#172A3A"
MUTED = "#607181"
LINE = "#526776"
BLUE = "#2F6B9A"
BLUE_FILL = "#EAF3F9"
TEAL = "#27856C"
TEAL_FILL = "#E8F5F0"
ORANGE = "#D9792B"
ORANGE_FILL = "#FFF2E7"
PURPLE = "#6C5A9A"
PURPLE_FILL = "#F1EEF8"
RED = "#C74848"
RED_FILL = "#FCEBEC"
SLATE_FILL = "#F3F6F8"
WHITE = "#FFFFFF"


def shape(
    cell_id: str,
    label: str,
    x: int,
    y: int,
    width: int,
    height: int,
    *,
    fill: str = WHITE,
    stroke: str = LINE,
    font_size: int = 16,
    font_color: str = INK,
    bold: bool = False,
    rounded: bool = True,
    align: str = "center",
    extra: str = "",
) -> dict:
    style = (
        f"rounded={1 if rounded else 0};whiteSpace=wrap;html=1;"
        f"arcSize=14;fillColor={fill};strokeColor={stroke};strokeWidth=2;"
        f"fontColor={font_color};fontFamily=Helvetica;fontSize={font_size};"
        f"fontStyle={1 if bold else 0};align={align};verticalAlign=middle;"
        "spacing=8;shadow=0;"
        f"{extra}"
    )
    return {
        "type": "shape",
        "id": cell_id,
        "label": label,
        "shape": "rounded" if rounded else "rectangle",
        "x": x,
        "y": y,
        "width": width,
        "height": height,
        "style": style,
    }


def text(
    cell_id: str,
    label: str,
    x: int,
    y: int,
    width: int,
    height: int,
    *,
    font_size: int = 16,
    color: str = INK,
    bold: bool = False,
    align: str = "left",
) -> dict:
    return shape(
        cell_id,
        label,
        x,
        y,
        width,
        height,
        fill="none",
        stroke="none",
        font_size=font_size,
        font_color=color,
        bold=bold,
        rounded=False,
        align=align,
        extra="strokeWidth=0;fillOpacity=0;",
    )


def ellipse(
    cell_id: str,
    label: str,
    x: int,
    y: int,
    width: int,
    height: int,
    *,
    fill: str,
    stroke: str,
) -> dict:
    return {
        "type": "shape",
        "id": cell_id,
        "label": label,
        "shape": "ellipse",
        "x": x,
        "y": y,
        "width": width,
        "height": height,
        "style": (
            f"ellipse;whiteSpace=wrap;html=1;fillColor={fill};strokeColor={stroke};"
            f"strokeWidth=2;fontColor={INK};fontFamily=Helvetica;fontSize=14;"
            "fontStyle=2;align=center;verticalAlign=middle;"
        ),
    }


def edge(
    edge_id: str,
    source: str,
    target: str,
    *,
    color: str = LINE,
    dashed: bool = False,
    label: str = "",
    exit_x: float | None = None,
    exit_y: float | None = None,
    entry_x: float | None = None,
    entry_y: float | None = None,
    waypoints: list[dict[str, float]] | None = None,
) -> dict:
    result = {
        "type": "edge",
        "id": edge_id,
        "source": source,
        "target": target,
        "label": label,
        "style": (
            "edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;"
            f"strokeColor={color};strokeWidth=2;endArrow=block;endFill=1;"
            f"dashed={1 if dashed else 0};fontFamily=Helvetica;fontSize=13;"
            f"fontColor={MUTED};labelBackgroundColor=#FFFFFF;"
        ),
    }
    if exit_x is not None:
        result["exit_x"] = exit_x
    if exit_y is not None:
        result["exit_y"] = exit_y
    if entry_x is not None:
        result["entry_x"] = entry_x
    if entry_y is not None:
        result["entry_y"] = entry_y
    if waypoints:
        result["waypoints"] = waypoints
    return result


stage_one = [
    text("title", "UAV-TAlign: scene-level infrared-visible alignment", 50, 20, 1500, 40, font_size=25, bold=True),
    text("subtitle", "From synchronized pairwise evidence to reliability-controlled scene products", 50, 56, 1500, 28, font_size=15, color=MUTED),
    shape("band_pairwise", "", 45, 100, 1510, 250, fill="#F8FAFC", stroke="#D5DEE5", rounded=True, extra="strokeWidth=1;"),
    text("panel_a", "a", 58, 108, 30, 28, font_size=20, bold=True),
    text("pairwise_band_title", "PAIRWISE EVIDENCE CONSTRUCTION", 95, 110, 520, 28, font_size=15, color=BLUE, bold=True),
    shape("input_group", "<b>Synchronized scene</b><br><font color='#607181'>N RGB-infrared pairs</font>", 90, 170, 190, 110, fill=WHITE, stroke=LINE, font_size=16, bold=False),
    shape("rgb_chip", "<b>RGB</b><br><font color='#607181'>visible FOV</font>", 112, 295, 70, 40, fill=BLUE_FILL, stroke=BLUE, font_size=12, bold=False),
    shape("ir_chip", "<b>IR</b><br><font color='#607181'>thermal FOV</font>", 188, 295, 70, 40, fill=ORANGE_FILL, stroke=ORANGE, font_size=12, bold=False),
    shape("pairwise", "<b>Cross-modal pairwise evidence</b><br><br><font color='#2F6B9A'><i>H</i><sub>i</sub></font><br><font color='#607181'>matches + robust geometry</font>", 330, 150, 245, 150, fill=BLUE_FILL, stroke=BLUE, font_size=16),
    shape("schedule", "<b>Progressive scene sampling</b><br><br><font color='#6C5A9A'>12 → 24 → …</font><br><font color='#607181'>even coverage + adaptive expansion</font>", 620, 150, 245, 150, fill=PURPLE_FILL, stroke=PURPLE, font_size=16),
    shape("confidence", "<b>Geometry-calibrated confidence</b><br><br><font color='#526776'><i>q</i><sub>i</sub> = f(η, c, ε)</font><br><font color='#607181'>inliers + support + residual</font>", 910, 150, 245, 150, fill=SLATE_FILL, stroke=LINE, font_size=16),
    shape("qa_probes", "<b>Cross-modal QA probes</b><br><br><font color='#D9792B'>ΔEdge · ΔGrad · outliers</font><br><font color='#607181'>appearance + stability diagnostics</font>", 1200, 150, 275, 150, fill=ORANGE_FILL, stroke=ORANGE, font_size=16),
    edge("e_input_pairwise", "input_group", "pairwise", color=BLUE),
    edge("e_pairwise_schedule", "pairwise", "schedule"),
    edge("e_schedule_confidence", "schedule", "confidence"),
    edge("e_confidence_qa", "confidence", "qa_probes"),
]

stage_two = [
    shape("band_consensus", "", 45, 380, 920, 410, fill="#FAFCFB", stroke="#D5E5DE", rounded=True, extra="strokeWidth=1;"),
    text("panel_b", "b", 58, 388, 30, 28, font_size=20, bold=True),
    text("consensus_band_title", "ROBUST SCENE CONSENSUS", 95, 390, 430, 28, font_size=15, color=TEAL, bold=True),
    shape("hypothesis_frame", "<b>Frame hypotheses</b>", 90, 440, 465, 145, fill=WHITE, stroke="#C9D5DD", font_size=15, align="left", extra="verticalAlign=top;spacingTop=10;"),
    ellipse("h1", "H₁", 120, 495, 52, 34, fill=TEAL_FILL, stroke=TEAL),
    ellipse("h2", "H₂", 182, 495, 52, 34, fill=TEAL_FILL, stroke=TEAL),
    ellipse("h3", "H₃", 244, 495, 52, 34, fill=TEAL_FILL, stroke=TEAL),
    ellipse("h4", "×", 306, 495, 52, 34, fill=RED_FILL, stroke=RED),
    ellipse("h5", "H₅", 368, 495, 52, 34, fill=TEAL_FILL, stroke=TEAL),
    ellipse("h6", "H₆", 430, 495, 52, 34, fill=TEAL_FILL, stroke=TEAL),
    text("mad_rule", "<i>d</i><sub>i</sub> ≤ median(<i>d</i>) + 2.5 MAD(<i>d</i>)", 130, 548, 360, 25, font_size=13, color=MUTED, align="center"),
    shape("consensus", "<b>Median/MAD consensus</b><br><br><font color='#27856C'>support-aware filtering</font><br><font color='#607181'>quality-weighted aggregation</font>", 585, 440, 235, 145, fill=TEAL_FILL, stroke=TEAL, font_size=16),
    shape("scene_transform", "<b>Scene transform</b><br><font color='#27856C'><i>H̃</i><sub>S</sub></font>", 835, 472, 120, 82, fill=WHITE, stroke=TEAL, font_size=15),
    edge("e_pairwise_hypotheses", "pairwise", "hypothesis_frame", color=BLUE, exit_x=0.5, exit_y=1.0, entry_x=0.5, entry_y=0.0),
    edge("e_hypotheses_consensus", "hypothesis_frame", "consensus", color=TEAL),
    edge("e_consensus_transform", "consensus", "scene_transform", color=TEAL, exit_x=1.0, exit_y=0.5, entry_x=0.0, entry_y=0.5),
]

stage_three = [
    shape("band_decision", "", 990, 380, 565, 430, fill="#FAFBFC", stroke="#D9E0E5", rounded=True, extra="strokeWidth=1;"),
    text("panel_c", "c", 1004, 388, 30, 28, font_size=20, bold=True),
    text("decision_band_title", "RELIABILITY CONTROL", 1040, 390, 350, 28, font_size=15, color=ORANGE, bold=True),
    shape("canonical_gate", "<b>Canonical QA gate</b><br><font color='#607181'>fixed product decision</font>", 1140, 440, 230, 90, fill=ORANGE_FILL, stroke=ORANGE, font_size=16),
    shape("product", "<b>High-confidence scene product</b><br><font color='#27856C'>retained alignment</font>", 1260, 570, 240, 85, fill=TEAL_FILL, stroke=TEAL, font_size=16),
    shape("filtered", "<b>QA-filtered scene</b><br><font color='#607181'>diagnostic output retained</font>", 1000, 570, 210, 85, fill=SLATE_FILL, stroke=LINE, font_size=15),
    shape("ranking", "<b>Interpretable reliability score</b><br><font color='#2F6B9A'><i>R</i>(S)</font>", 1000, 690, 240, 75, fill=BLUE_FILL, stroke=BLUE, font_size=15),
    shape("operating_profile", "<b>Risk–coverage profile</b><br><font color='#607181'>ordered operating points</font>", 1270, 690, 230, 75, fill=WHITE, stroke=BLUE, font_size=15),
    edge("e_transform_gate", "scene_transform", "canonical_gate", color=ORANGE),
    edge("e_gate_product", "canonical_gate", "product", color=TEAL, exit_x=0.7, exit_y=1.0, entry_x=0.5, entry_y=0.0),
    edge(
        "e_gate_filtered",
        "canonical_gate",
        "filtered",
        color=LINE,
        dashed=True,
        exit_x=0.3,
        exit_y=1.0,
        entry_x=0.5,
        entry_y=0.0,
    ),
    edge("e_transform_ranking", "scene_transform", "ranking", color=BLUE, dashed=True),
    edge("e_ranking_profile", "ranking", "operating_profile", color=BLUE),
    edge(
        "e_qa_gate",
        "qa_probes",
        "canonical_gate",
        color=ORANGE,
        exit_x=0.5,
        exit_y=1.0,
        entry_x=0.5,
        entry_y=0.0,
    ),
    text("decision_note", "The canonical gate defines products; R(S) only orders operating points.", 1005, 775, 535, 30, font_size=13, color=MUTED, align="center"),
]

plan = {
    "report": "drawio_live_report.json",
    "calls": [
        {
            "name": "drawio_live_launch",
            "arguments": {
                "file_path": "${PLAN_DIR}/blank_canvas.drawio",
                "port": 9343,
                "step_delay_ms": 350,
                "maximize": True,
                "include_screenshot": False,
            },
            "timeout_ms": 120000,
        },
        {
            "name": "drawio_live_clear",
            "arguments": {"confirm": True},
            "timeout_ms": 30000,
        },
        {
            "name": "drawio_live_draw_sequence",
            "arguments": {
                "operations": stage_one,
                "step_delay_ms": 350,
                "screenshot_after": True,
            },
            "screenshot": "stage_01_pairwise.png",
            "timeout_ms": 180000,
        },
        {
            "name": "drawio_live_draw_sequence",
            "arguments": {
                "operations": stage_two,
                "step_delay_ms": 350,
                "screenshot_after": True,
            },
            "screenshot": "stage_02_consensus.png",
            "timeout_ms": 180000,
        },
        {
            "name": "drawio_live_draw_sequence",
            "arguments": {
                "operations": stage_three + [{"type": "fit"}],
                "step_delay_ms": 350,
                "screenshot_after": True,
            },
            "screenshot": "stage_03_final.png",
            "timeout_ms": 180000,
        },
        {
            "name": "drawio_live_inspect",
            "arguments": {"max_cells": 200},
            "timeout_ms": 30000,
        },
        {
            "name": "drawio_live_save_snapshot",
            "arguments": {
                "output_path": "${PLAN_DIR}/fig03_scene_framework.drawio",
                "page_name": "UAV-TAlign scene framework",
                "overwrite": True,
            },
            "timeout_ms": 30000,
        },
    ],
}

(ROOT / "live_plan.json").write_text(json.dumps(plan, indent=2), encoding="utf-8")
