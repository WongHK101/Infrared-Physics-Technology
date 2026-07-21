from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "_shared"))
from figure_style import COLORS, configure_style, image_panel, mm, panel_label, save_bundle, soften_axes  # noqa: E402


ROOT = Path(__file__).resolve().parent
DATA = ROOT / "source_data"
ASSETS = ROOT / "source_assets"


def find(scene: str, suffix: str) -> Path:
    matches = sorted(ASSETS.glob(f"{scene}_*_{suffix}.jpg"))
    if not matches:
        raise FileNotFoundError(f"Missing asset: {scene} * {suffix}")
    return matches[0]


def add_control_group(fig, spec, scenes, panel, title) -> None:
    sub = spec.subgridspec(2, 3, wspace=0.035, hspace=0.13)
    columns = [
        ("before_resize_overlay_crop", "Before"),
        ("after_scene_homography_overlay_crop", "Scene product"),
        ("edge_overlay_crop", "Edge agreement"),
    ]
    for row, (scene, label, is_pass) in enumerate(scenes):
        for col, (suffix, col_title) in enumerate(columns):
            ax = fig.add_subplot(sub[row, col])
            image_panel(ax, find(scene, suffix), col_title if row == 0 else None)
            if row == 0 and col == 0:
                panel_label(ax, panel, x=-0.16, y=1.08)
                ax.text(0.0, 1.28, title, transform=ax.transAxes, fontsize=7.0, fontweight="bold", ha="left")
            if col == 0:
                ax.text(
                    -0.04,
                    0.50,
                    label,
                    transform=ax.transAxes,
                    rotation=90,
                    ha="right",
                    va="center",
                    fontsize=6.1,
                    fontweight="semibold",
                    color=COLORS["confidence"] if is_pass else COLORS["filtered"],
                )


def main() -> None:
    configure_style()
    fig = plt.figure(figsize=(mm(183), mm(116)))
    gs = fig.add_gridspec(2, 2, height_ratios=[1.18, 0.82], wspace=0.15, hspace=0.36)
    add_control_group(
        fig,
        gs[0, 0],
        [("scene01", "S01 · retained", True), ("scene02", "S02 · filtered", False)],
        "a",
        "Day wide/zoom control",
    )
    add_control_group(
        fig,
        gs[0, 1],
        [("scene04", "S04 · retained", True), ("scene03", "S03 · filtered", False)],
        "b",
        "Night zoom/wide control",
    )

    ax_c = fig.add_subplot(gs[1, :])
    panel_label(ax_c, "c", x=-0.015, y=1.02)
    data = pd.read_csv(DATA / "per_scene_reliability_table.csv")
    passed = data["canonical_scene_pass"].astype(str).str.lower().eq("true")
    sizes = 35 + 210 * data["robust_reject_ratio"].clip(0, 0.5)
    ax_c.scatter(
        data.loc[~passed, "accepted_ratio"],
        data.loc[~passed, "severe_outlier_ratio"],
        s=sizes[~passed],
        color=COLORS["filtered"],
        alpha=0.80,
        label="QA-filtered",
        edgecolor="white",
        linewidth=0.5,
    )
    ax_c.scatter(
        data.loc[passed, "accepted_ratio"],
        data.loc[passed, "severe_outlier_ratio"],
        s=sizes[passed],
        color=COLORS["confidence"],
        alpha=0.90,
        label="High-confidence product",
        edgecolor="white",
        linewidth=0.5,
    )
    for _, row in data.iterrows():
        ax_c.text(row.accepted_ratio + 0.012, row.severe_outlier_ratio + 0.003, f"S{int(row.scene_id):02d}", fontsize=5.5, color=COLORS["ink"])
    ax_c.axhline(0.10, color=COLORS["canonical"], ls=(0, (3, 2)), lw=0.85)
    ax_c.set_xlabel("Accepted-frame ratio")
    ax_c.set_ylabel("Severe relative-outlier ratio")
    ax_c.set_xlim(-0.02, 1.08)
    ax_c.set_ylim(-0.01, max(0.20, data["severe_outlier_ratio"].max() * 1.22))
    ax_c.set_title("All-scene QA evidence", fontweight="semibold", pad=4)
    soften_axes(ax_c)
    ax_c.legend(loc="upper left", ncol=2)
    ax_c.text(1.075, 0.103, "reference", ha="right", va="bottom", color=COLORS["canonical"], fontsize=5.5)

    save_bundle(fig, ROOT / "outputs", "fig07_reliability_selection")
    plt.close(fig)


if __name__ == "__main__":
    main()

