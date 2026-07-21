from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec, GridSpecFromSubplotSpec
from matplotlib.patches import Circle, Polygon

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


def find(scene: str, suffix: str) -> Path:
    matches = sorted(ASSETS.glob(f"{scene}_*_{suffix}.jpg"))
    if not matches:
        raise FileNotFoundError(f"Missing asset: {scene} * {suffix}")
    return matches[0]


def draw_drone(ax) -> None:
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    ax.plot([0.28, 0.72], [0.82, 0.82], color=COLORS["ink"], lw=1.2)
    ax.plot([0.38, 0.23], [0.82, 0.92], color=COLORS["ink"], lw=1.0)
    ax.plot([0.62, 0.77], [0.82, 0.92], color=COLORS["ink"], lw=1.0)
    ax.plot([0.38, 0.23], [0.82, 0.72], color=COLORS["ink"], lw=1.0)
    ax.plot([0.62, 0.77], [0.82, 0.72], color=COLORS["ink"], lw=1.0)
    for x, y in [(0.20, 0.94), (0.80, 0.94), (0.20, 0.70), (0.80, 0.70)]:
        ax.add_patch(Circle((x, y), 0.075, fill=False, ec=COLORS["muted"], lw=0.8))
    ax.add_patch(
        Polygon(
            [[0.42, 0.87], [0.58, 0.87], [0.62, 0.77], [0.38, 0.77]],
            closed=True,
            fc="#E7ECEF",
            ec=COLORS["ink"],
            lw=0.8,
        )
    )
    rounded_box(
        ax,
        (0.39, 0.54),
        0.22,
        0.13,
        "H30T\npayload",
        "#FFFFFF",
        COLORS["ink"],
        fontsize=6.1,
    )
    ax.plot([0.50, 0.50], [0.77, 0.68], color=COLORS["ink"], lw=0.9)
    ax.add_patch(
        Polygon(
            [[0.43, 0.50], [0.16, 0.13], [0.47, 0.13]],
            closed=True,
            fc=COLORS["visible_light"],
            ec=COLORS["visible"],
            lw=0.8,
            alpha=0.9,
        )
    )
    ax.add_patch(
        Polygon(
            [[0.57, 0.50], [0.52, 0.13], [0.78, 0.13]],
            closed=True,
            fc=COLORS["infrared_light"],
            ec=COLORS["infrared"],
            lw=0.8,
            alpha=0.9,
        )
    )
    ax.text(0.21, 0.015, "RGB\nfield of view", ha="center", va="bottom", color=COLORS["visible"], fontsize=5.8)
    ax.text(0.76, 0.015, "Infrared\nfield of view", ha="center", va="bottom", color=COLORS["infrared"], fontsize=5.8)


def main() -> None:
    configure_style()
    fig = plt.figure(figsize=(mm(183), mm(98)))
    outer = GridSpec(
        2,
        4,
        figure=fig,
        width_ratios=[1.32, 1, 1, 1],
        height_ratios=[1, 1],
        wspace=0.12,
        hspace=0.18,
    )

    ax_a = fig.add_subplot(outer[:, 0])
    panel_label(ax_a, "a", x=-0.02, y=1.01)
    ax_a.axis("off")
    drone = ax_a.inset_axes([0.03, 0.49, 0.94, 0.48])
    draw_drone(drone)
    ax_a.text(
        0.50,
        0.455,
        "Synchronized onboard capture",
        transform=ax_a.transAxes,
        ha="center",
        va="center",
        fontsize=7.2,
        fontweight="bold",
    )
    card = ax_a.inset_axes([0.02, 0.19, 0.96, 0.23])
    card.axis("off")
    rounded_box(card, (0.02, 0.08), 0.96, 0.84, "", "#F5F7F8", "#D1D8DE")
    card.text(0.17, 0.68, "15", ha="center", fontsize=13, fontweight="bold", color=COLORS["visible"])
    card.text(0.17, 0.30, "scenes", ha="center", fontsize=5.8, color=COLORS["muted"])
    card.text(0.50, 0.68, "6,039", ha="center", fontsize=13, fontweight="bold", color=COLORS["infrared"])
    card.text(0.50, 0.30, "candidate\npairs", ha="center", va="center", fontsize=5.8, color=COLORS["muted"])
    card.text(0.83, 0.68, "6,037", ha="center", fontsize=13, fontweight="bold", color=COLORS["confidence"])
    card.text(0.83, 0.30, "evaluation\npairs", ha="center", va="center", fontsize=5.8, color=COLORS["muted"])
    before_ax = ax_a.inset_axes([0.02, 0.00, 0.46, 0.16])
    after_ax = ax_a.inset_axes([0.52, 0.00, 0.46, 0.16])
    image_panel(before_ax, find("scene01", "before_resize_overlay_crop"), "Before")
    image_panel(after_ax, find("scene01", "after_scene_homography_overlay_crop"), "Scene product")
    arrow(ax_a, (0.47, 0.075), (0.53, 0.075), color=COLORS["confidence"])

    examples = [
        ("scene01", "S01  day · gray · wide"),
        ("scene04", "S04  night · gray · zoom"),
        ("scene05", "S05  night · pseudocolor"),
        ("scene06", "S06  day · pseudocolor"),
        ("scene13", "S13  low-light · pseudocolor"),
        ("scene14", "S14  low-light · tower"),
    ]
    for idx, (scene, title) in enumerate(examples):
        row, col = divmod(idx, 3)
        sub = GridSpecFromSubplotSpec(
            2,
            2,
            subplot_spec=outer[row, col + 1],
            height_ratios=[0.13, 0.87],
            hspace=0.02,
            wspace=0.03,
        )
        label_ax = fig.add_subplot(sub[0, :])
        label_ax.axis("off")
        label_ax.text(0.5, 0.45, title, ha="center", va="center", fontsize=6.5, fontweight="semibold")
        rgb_ax = fig.add_subplot(sub[1, 0])
        ir_ax = fig.add_subplot(sub[1, 1])
        image_panel(rgb_ax, find(scene, "rgb_selected_crop"), "RGB" if idx == 0 else None)
        image_panel(ir_ax, find(scene, "infrared_selected_crop"), "Infrared" if idx == 0 else None)
        if idx == 0:
            panel_label(label_ax, "b", x=-0.05, y=1.0)

    save_bundle(fig, ROOT / "outputs", "fig01_problem_benchmark")
    plt.close(fig)


if __name__ == "__main__":
    main()
