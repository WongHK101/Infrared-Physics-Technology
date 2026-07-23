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
RED = "#C74848"
RED_FILL = "#FCEBEC"
SLATE_FILL = "#F3F6F8"


def box(cell_id, label, x, y, width, height, fill, stroke, font_size=15, bold=False, extra=""):
    return {
        "type": "shape",
        "id": cell_id,
        "label": label,
        "shape": "rounded",
        "x": x,
        "y": y,
        "width": width,
        "height": height,
        "style": (
            f"rounded=1;arcSize=14;whiteSpace=wrap;html=1;fillColor={fill};"
            f"strokeColor={stroke};strokeWidth=2;fontColor={INK};fontFamily=Helvetica;"
            f"fontSize={font_size};fontStyle={1 if bold else 0};align=center;"
            f"verticalAlign=middle;spacing=6;shadow=0;{extra}"
        ),
    }


def text(cell_id, label, x, y, width, height, font_size=15, color=INK, bold=False, align="left"):
    return {
        "type": "shape",
        "id": cell_id,
        "label": label,
        "shape": "text",
        "x": x,
        "y": y,
        "width": width,
        "height": height,
        "style": (
            "text;html=1;strokeColor=none;fillColor=none;fillOpacity=0;"
            f"fontColor={color};fontFamily=Helvetica;fontSize={font_size};"
            f"fontStyle={1 if bold else 0};align={align};verticalAlign=middle;"
        ),
    }


def edge(
    cell_id,
    source,
    target,
    color=LINE,
    dashed=False,
    *,
    exit_x=None,
    exit_y=None,
    entry_x=None,
    entry_y=None,
    waypoints=None,
):
    operation = {
        "type": "edge",
        "id": cell_id,
        "source": source,
        "target": target,
        "style": (
            "edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;"
            f"strokeColor={color};strokeWidth=2;dashed={1 if dashed else 0};"
            "endArrow=block;endFill=1;"
        ),
    }
    if exit_x is not None:
        operation["exit_x"] = exit_x
        operation["exit_y"] = exit_y
    if entry_x is not None:
        operation["entry_x"] = entry_x
        operation["entry_y"] = entry_y
    if waypoints:
        operation["waypoints"] = waypoints
    return operation


ops = [
    box("panel", "", 20, 20, 1380, 360, "#FAFBFC", "#D6E0E7", 14, False, "strokeWidth=1;"),
    text("panel_d", "d", 38, 32, 30, 26, 19, INK, True),
    text("title", "MATCHED-CONTROL DECISION LOGIC", 78, 32, 520, 28, 15, BLUE, True),
    box("shared_support", "<b>Matched pairwise support</b><br><font color='#2F6B9A'>S01 and S02: 49/50 frames accepted</font>", 65, 120, 250, 100, BLUE_FILL, BLUE, 15),
    text("lane_retained", "RETAINED PRODUCT", 365, 72, 250, 24, 13, TEAL, True),
    box("s01_evidence", "<b>S01</b><br><font color='#27856C'>0 severe outliers</font><br><font color='#607181'>0.0% robust rejection</font>", 365, 105, 210, 90, TEAL_FILL, TEAL, 14),
    box("s01_consensus", "<b>Stable consensus</b><br><font color='#607181'>supported scene transform</font>", 625, 105, 210, 90, TEAL_FILL, TEAL, 14),
    box("s01_gate", "<b>Canonical gate</b><br><font color='#27856C'>retain</font>", 885, 105, 170, 90, "#FFFFFF", TEAL, 14),
    box("s01_product", "<b>High-confidence<br>scene product</b>", 1105, 105, 225, 90, TEAL_FILL, TEAL, 15),
    text("lane_filtered", "QA-FILTERED PRODUCT", 365, 205, 250, 24, 13, RED, True),
    box("s02_evidence", "<b>S02</b><br><font color='#C74848'>QA-relative outliers</font><br><font color='#607181'>consensus rejection</font>", 365, 235, 210, 82, RED_FILL, RED, 14),
    box("s02_consensus", "<b>Unstable evidence</b><br><font color='#607181'>high outlier burden</font>", 625, 235, 210, 82, SLATE_FILL, LINE, 14),
    box("s02_gate", "<b>Canonical gate</b><br><font color='#C74848'>filter</font>", 885, 235, 170, 82, "#FFFFFF", RED, 14),
    box("s02_product", "<b>QA-filtered scene</b><br><font color='#607181'>diagnostics retained</font>", 1105, 235, 225, 82, SLATE_FILL, LINE, 14),
    edge("e_shared_s01", "shared_support", "s01_evidence", TEAL),
    edge(
        "e_shared_s02",
        "shared_support",
        "s02_evidence",
        RED,
        True,
        exit_x=1,
        exit_y=0.85,
        entry_x=0,
        entry_y=0.5,
        waypoints=[{"x": 340, "y": 205}, {"x": 340, "y": 276}],
    ),
    edge("e_s01_consensus", "s01_evidence", "s01_consensus", TEAL),
    edge("e_s01_gate", "s01_consensus", "s01_gate", TEAL),
    edge("e_s01_product", "s01_gate", "s01_product", TEAL),
    edge("e_s02_consensus", "s02_evidence", "s02_consensus", LINE, True),
    edge("e_s02_gate", "s02_consensus", "s02_gate", RED, True),
    edge("e_s02_product", "s02_gate", "s02_product", LINE, True),
    text("insight", "Equivalent accepted-frame support does not imply an equivalent scene product.", 355, 338, 975, 24, 13, MUTED, False, "center"),
    {"type": "fit"},
]

plan = {
    "report": "drawio_live_report.json",
    "calls": [
        {
            "name": "drawio_live_launch",
            "arguments": {
                "file_path": "${PLAN_DIR}/blank_canvas.drawio",
                "port": 9344,
                "step_delay_ms": 350,
                "maximize": True,
                "include_screenshot": False,
            },
            "timeout_ms": 120000,
        },
        {"name": "drawio_live_clear", "arguments": {"confirm": True}, "timeout_ms": 30000},
        {
            "name": "drawio_live_draw_sequence",
            "arguments": {"operations": ops[:14], "step_delay_ms": 350, "screenshot_after": True},
            "screenshot": "stage_01_structure.png",
            "timeout_ms": 180000,
        },
        {
            "name": "drawio_live_draw_sequence",
            "arguments": {"operations": ops[14:], "step_delay_ms": 350, "screenshot_after": True},
            "screenshot": "stage_02_final.png",
            "timeout_ms": 180000,
        },
        {
            "name": "drawio_live_save_snapshot",
            "arguments": {
                "output_path": "${PLAN_DIR}/fig04_matched_control_logic.drawio",
                "page_name": "UAV-TAlign matched-control logic",
                "overwrite": True,
            },
            "timeout_ms": 30000,
        },
    ],
}

(ROOT / "live_plan.json").write_text(json.dumps(plan, indent=2), encoding="utf-8")
