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
            f"verticalAlign=middle;spacing=7;shadow=0;{extra}"
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


def edge(cell_id, source, target, color=LINE):
    return {
        "type": "edge",
        "id": cell_id,
        "source": source,
        "target": target,
        "style": (
            "edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;"
            f"strokeColor={color};strokeWidth=2;endArrow=block;endFill=1;"
        ),
    }


ops = [
    box("left_band", "", 20, 30, 690, 315, "#FAFBFC", "#D6E0E7", 14, False, "strokeWidth=1;"),
    text("panel_c", "c", 35, 42, 28, 24, 18, INK, True),
    text("left_title", "INTEGRITY-CHECKED OFFICIAL SPLIT", 75, 42, 420, 26, 15, BLUE, True),
    box("collection", "<b>Captured collection</b><br><font color='#D9792B' style='font-size:24px'>6,039 pairs</font>", 60, 110, 180, 100, ORANGE_FILL, ORANGE, 16),
    box("integrity", "<b>Integrity assurance</b><br><font color='#607181'>pairing · decode · content hash</font>", 285, 100, 205, 120, SLATE_FILL, LINE, 15),
    box("manifest", "<b>Versioned manifest</b><br><font color='#2F6B9A'>fixed IDs + SHA-256</font>", 525, 100, 160, 120, BLUE_FILL, BLUE, 14),
    box("official", "<b>Official split</b><br><font color='#27856C' style='font-size:24px'>6,037 pairs</font>", 525, 250, 160, 70, TEAL_FILL, TEAL, 15),
    edge("e_collection_integrity", "collection", "integrity", ORANGE),
    edge("e_integrity_manifest", "integrity", "manifest", BLUE),
    edge("e_manifest_official", "manifest", "official", TEAL),
    text("left_note", "One frozen manifest anchors every reported result.", 65, 278, 410, 28, 13, MUTED, False, "center"),
    box("right_band", "", 735, 30, 675, 315, "#FAFBFC", "#D6E0E7", 14, False, "strokeWidth=1;"),
    text("panel_d", "d", 750, 42, 28, 24, 18, INK, True),
    text("right_title", "THREE COMPLEMENTARY EVALUATION UNITS", 790, 42, 500, 26, 15, TEAL, True),
    box("track_pair", "<b>Pairwise evidence</b><br><font color='#607181'>unit: image pair</font><br><font color='#2F6B9A'>availability · support · coverage</font>", 785, 92, 560, 64, BLUE_FILL, BLUE, 14, False, "align=left;spacingLeft=18;"),
    box("track_scene", "<b>Scene products</b><br><font color='#607181'>unit: synchronized scene</font><br><font color='#27856C'>consensus · QA · canonical decision</font>", 785, 174, 560, 64, TEAL_FILL, TEAL, 14, False, "align=left;spacingLeft=18;"),
    box("track_profile", "<b>Operating profile</b><br><font color='#607181'>unit: selectable operating point</font><br><font color='#D9792B'>reliability ranking · coverage · condition</font>", 785, 256, 560, 64, ORANGE_FILL, ORANGE, 14, False, "align=left;spacingLeft=18;"),
    box("pair_tag", "PAIR", 1280, 105, 48, 38, "#FFFFFF", BLUE, 12, True),
    box("scene_tag", "SCENE", 1270, 187, 58, 38, "#FFFFFF", TEAL, 12, True),
    box("profile_tag", "PROFILE", 1260, 269, 68, 38, "#FFFFFF", ORANGE, 12, True),
    {"type": "fit"},
]

plan = {
    "report": "drawio_live_report.json",
    "calls": [
        {
            "name": "drawio_live_launch",
            "arguments": {
                "file_path": "${PLAN_DIR}/blank_canvas.drawio",
                "port": 9342,
                "step_delay_ms": 350,
                "maximize": True,
                "include_screenshot": False,
            },
            "timeout_ms": 120000,
        },
        {"name": "drawio_live_clear", "arguments": {"confirm": True}, "timeout_ms": 30000},
        {
            "name": "drawio_live_draw_sequence",
            "arguments": {"operations": ops[:11], "step_delay_ms": 350, "screenshot_after": True},
            "screenshot": "stage_01_integrity.png",
            "timeout_ms": 180000,
        },
        {
            "name": "drawio_live_draw_sequence",
            "arguments": {"operations": ops[11:], "step_delay_ms": 350, "screenshot_after": True},
            "screenshot": "stage_02_final.png",
            "timeout_ms": 180000,
        },
        {
            "name": "drawio_live_save_snapshot",
            "arguments": {
                "output_path": "${PLAN_DIR}/fig02_protocol_hierarchy.drawio",
                "page_name": "UAV-TAlign benchmark protocol",
                "overwrite": True,
            },
            "timeout_ms": 30000,
        },
    ],
}

(ROOT / "live_plan.json").write_text(json.dumps(plan, indent=2), encoding="utf-8")
