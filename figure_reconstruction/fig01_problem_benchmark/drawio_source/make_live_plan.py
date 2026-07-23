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
SLATE_FILL = "#F3F6F8"


def shape(cell_id, label, shape_name, x, y, width, height, style):
    return {
        "type": "shape",
        "id": cell_id,
        "label": label,
        "shape": shape_name,
        "x": x,
        "y": y,
        "width": width,
        "height": height,
        "style": style,
    }


def box(cell_id, label, x, y, width, height, fill, stroke, font_size=16, bold=False, extra=""):
    return shape(
        cell_id,
        label,
        "rounded",
        x,
        y,
        width,
        height,
        (
            f"rounded=1;arcSize=14;whiteSpace=wrap;html=1;fillColor={fill};"
            f"strokeColor={stroke};strokeWidth=2;fontColor={INK};fontFamily=Helvetica;"
            f"fontSize={font_size};fontStyle={1 if bold else 0};align=center;"
            f"verticalAlign=middle;spacing=6;shadow=0;{extra}"
        ),
    )


def text(cell_id, label, x, y, width, height, font_size=16, color=INK, bold=False, align="center"):
    return shape(
        cell_id,
        label,
        "text",
        x,
        y,
        width,
        height,
        (
            "text;html=1;strokeColor=none;fillColor=none;fillOpacity=0;"
            f"fontColor={color};fontFamily=Helvetica;fontSize={font_size};"
            f"fontStyle={1 if bold else 0};align={align};verticalAlign=middle;"
        ),
    )


def edge(cell_id, source, target, color=LINE, width=2, dashed=False, end_arrow="none"):
    return {
        "type": "edge",
        "id": cell_id,
        "source": source,
        "target": target,
        "style": (
            "edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;"
            f"strokeColor={color};strokeWidth={width};dashed={1 if dashed else 0};"
            f"endArrow={end_arrow};endFill=1;"
        ),
    }


ops = [
    text("title", "SYNCHRONIZED UAV INFRARED–VISIBLE CAPTURE", 20, 10, 470, 34, 18, BLUE, True),
    text("subtitle", "DJI M350 platform · H30T multi-sensor payload", 20, 43, 470, 25, 14, MUTED),
    box("panel", "", 15, 78, 480, 610, "#FBFCFD", "#D4DEE5", 14, False, "strokeWidth=1;"),
    shape("rotor_fl", "", "ellipse", 55, 105, 82, 32, f"ellipse;fillColor=#FFFFFF;strokeColor={LINE};strokeWidth=3;"),
    shape("rotor_fr", "", "ellipse", 373, 105, 82, 32, f"ellipse;fillColor=#FFFFFF;strokeColor={LINE};strokeWidth=3;"),
    shape("rotor_rl", "", "ellipse", 55, 202, 82, 32, f"ellipse;fillColor=#FFFFFF;strokeColor={LINE};strokeWidth=3;"),
    shape("rotor_rr", "", "ellipse", 373, 202, 82, 32, f"ellipse;fillColor=#FFFFFF;strokeColor={LINE};strokeWidth=3;"),
    box("drone_body", "<b>M350</b>", 205, 142, 100, 58, SLATE_FILL, LINE, 18, True),
    box("payload", "<b>H30T</b><br><font color='#607181'>synchronized payload</font>", 195, 220, 120, 62, "#FFFFFF", LINE, 15),
    edge("arm_fl", "drone_body", "rotor_fl", LINE, 3),
    edge("arm_fr", "drone_body", "rotor_fr", LINE, 3),
    edge("arm_rl", "drone_body", "rotor_rl", LINE, 3),
    edge("arm_rr", "drone_body", "rotor_rr", LINE, 3),
    edge("body_payload", "drone_body", "payload", LINE, 3),
    shape(
        "rgb_fov",
        "",
        "triangle",
        135,
        300,
        120,
        145,
        f"triangle;direction=north;fillColor={BLUE_FILL};fillOpacity=70;strokeColor={BLUE};strokeWidth=2;",
    ),
    shape(
        "ir_fov",
        "",
        "triangle",
        255,
        300,
        120,
        145,
        f"triangle;direction=north;fillColor={ORANGE_FILL};fillOpacity=70;strokeColor={ORANGE};strokeWidth=2;",
    ),
    text("rgb_label", "<b>RGB</b><br>visible field of view", 118, 445, 150, 38, 14, BLUE),
    text("ir_label", "<b>Infrared</b><br>thermal field of view", 248, 445, 150, 38, 14, ORANGE),
    box("sync_badge", "<b>hardware-synchronized pair</b>", 132, 492, 250, 42, TEAL_FILL, TEAL, 14),
    box("stats", "", 45, 548, 420, 104, "#FFFFFF", "#C9D5DD", 14, False, "strokeWidth=1;"),
    text("n_scenes", "<b><font color='#2F6B9A' style='font-size:26px'>15</font></b><br><font color='#607181'>scenes</font>", 55, 562, 110, 70, 15),
    text("n_collection", "<b><font color='#D9792B' style='font-size:26px'>6,039</font></b><br><font color='#607181'>candidate pairs</font>", 175, 562, 130, 70, 15),
    text("n_eval", "<b><font color='#27856C' style='font-size:26px'>6,037</font></b><br><font color='#607181'>evaluation pairs</font>", 315, 562, 130, 70, 15),
    text("footer", "Native onboard imagery · fixed integrity-checked manifest", 50, 660, 410, 24, 13, MUTED),
    {"type": "fit"},
]

plan = {
    "report": "drawio_live_report.json",
    "calls": [
        {
            "name": "drawio_live_launch",
            "arguments": {
                "file_path": "${PLAN_DIR}/blank_canvas.drawio",
                "port": 9341,
                "step_delay_ms": 350,
                "maximize": True,
                "include_screenshot": False,
            },
            "timeout_ms": 120000,
        },
        {"name": "drawio_live_clear", "arguments": {"confirm": True}, "timeout_ms": 30000},
        {
            "name": "drawio_live_draw_sequence",
            "arguments": {"operations": ops[:18], "step_delay_ms": 350, "screenshot_after": True},
            "screenshot": "stage_01_capture.png",
            "timeout_ms": 180000,
        },
        {
            "name": "drawio_live_draw_sequence",
            "arguments": {"operations": ops[18:], "step_delay_ms": 350, "screenshot_after": True},
            "screenshot": "stage_02_final.png",
            "timeout_ms": 180000,
        },
        {
            "name": "drawio_live_inspect",
            "arguments": {"max_cells": 100},
            "timeout_ms": 30000,
        },
        {
            "name": "drawio_live_save_snapshot",
            "arguments": {
                "output_path": "${PLAN_DIR}/fig01_acquisition_panel.drawio",
                "page_name": "UAV-TAlign acquisition panel",
                "overwrite": True,
            },
            "timeout_ms": 30000,
        },
    ],
}

(ROOT / "live_plan.json").write_text(json.dumps(plan, indent=2), encoding="utf-8")
