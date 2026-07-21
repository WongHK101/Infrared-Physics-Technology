from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.pyplot as plt

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "_shared"))
from figure_style import (  # noqa: E402
    COLORS,
    arrow,
    configure_style,
    image_panel,
    mm,
    panel_label,
    rounded_box,
    save_bundle,
)


ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / "source_assets"


def only(pattern: str) -> Path:
    matches = list(ASSETS.glob(pattern))
    if len(matches) != 1:
        raise FileNotFoundError(f"Expected one asset for {pattern}, found {len(matches)}")
    return matches[0]


def main() -> None:
    configure_style()
    fig = plt.figure(figsize=(mm(183), mm(92)))
    ax = fig.add_axes([0.02, 0.06, 0.96, 0.88])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    panel_label(ax, "a", x=-0.01, y=1.01)

    rgb_ax = ax.inset_axes([0.00, 0.57, 0.105, 0.31])
    ir_ax = ax.inset_axes([0.00, 0.18, 0.105, 0.31])
    image_panel(rgb_ax, only("*rgb_selected_crop.jpg"), "RGB")
    image_panel(ir_ax, only("*infrared_selected_crop.jpg"), "Infrared")
    ax.text(0.052, 0.94, "Synchronized scene pairs", ha="center", fontsize=6.8, fontweight="bold")

    boxes = [
        (0.15, "Pairwise evidence", "matches · H · residuals", COLORS["visible_light"], COLORS["visible"]),
        (0.34, "Evidence selection", "quality · coverage · diversity", "#EEF1F6", COLORS["purple"]),
        (0.53, "Robust consensus", "weighted median · MAD filtering", COLORS["confidence_light"], COLORS["confidence"]),
        (0.72, "QA verification", "stability · edge · gradient", COLORS["infrared_light"], COLORS["infrared"]),
    ]
    for x, title, subtitle, fc, ec in boxes:
        rounded_box(ax, (x, 0.55), 0.15, 0.29, "", fc, ec)
        ax.text(x + 0.075, 0.735, title, ha="center", va="center", fontweight="bold", fontsize=6.6)
        ax.text(x + 0.075, 0.635, subtitle, ha="center", va="center", color=COLORS["muted"], fontsize=5.7, wrap=True)
    for start, end in [(0.106, 0.15), (0.30, 0.34), (0.49, 0.53), (0.68, 0.72)]:
        arrow(ax, (start, 0.695), (end, 0.695))

    out_ax = ax.inset_axes([0.89, 0.55, 0.105, 0.29])
    image_panel(out_ax, only("*after_scene_homography_overlay_crop.jpg"), "Scene product")
    arrow(ax, (0.87, 0.695), (0.89, 0.695), color=COLORS["confidence"])

    ax.plot([0.225, 0.795], [0.43, 0.43], color=COLORS["grid"], lw=0.9)
    for x in [0.225, 0.415, 0.605, 0.795]:
        ax.plot([x, x], [0.43, 0.51], color=COLORS["grid"], lw=0.8)
    ax.text(0.15, 0.43, "Pair level", ha="right", va="center", color=COLORS["muted"], fontweight="semibold")
    ax.text(0.15, 0.28, "Scene level", ha="right", va="center", color=COLORS["muted"], fontweight="semibold")

    rounded_box(ax, (0.23, 0.17), 0.25, 0.20, "Canonical gate\nhigh-confidence product", COLORS["confidence_light"], COLORS["confidence"], fontsize=6.5)
    rounded_box(ax, (0.56, 0.17), 0.25, 0.20, "Interpretable score\noperating-profile ranking", COLORS["filtered_light"], COLORS["filtered"], fontsize=6.5)
    arrow(ax, (0.795, 0.55), (0.355, 0.38), color=COLORS["confidence"], connectionstyle="arc3,rad=0.16")
    arrow(ax, (0.795, 0.55), (0.685, 0.38), color=COLORS["filtered"], connectionstyle="arc3,rad=-0.12")
    ax.text(0.52, 0.08, "Fixed product decision", ha="right", fontsize=5.9, color=COLORS["confidence"])
    ax.text(0.54, 0.08, "≠", ha="center", fontsize=8, fontweight="bold", color=COLORS["canonical"])
    ax.text(0.56, 0.08, "score-ranked top-K set", ha="left", fontsize=5.9, color=COLORS["filtered"])

    save_bundle(fig, ROOT / "outputs", "fig03_scene_framework")
    plt.close(fig)


if __name__ == "__main__":
    main()

