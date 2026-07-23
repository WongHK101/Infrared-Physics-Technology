from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.gridspec import GridSpec

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "_shared"))
from figure_style import (  # noqa: E402
    COLORS,
    configure_style,
    mm,
    panel_label,
    save_bundle,
    soften_axes,
)


ROOT = Path(__file__).resolve().parent
DATA = ROOT / "source_data"
DRAWIO_PROTOCOL = ROOT / "drawio_source" / "fig02_protocol_hierarchy.png"


def main() -> None:
    configure_style()
    scenes = pd.read_csv(DATA / "UAV-TAlign-12K_per_scene_valid_counts.csv")
    scenes["scene_label"] = scenes["scene_id"].map(lambda x: f"S{int(x):02d}")
    light_colors = {
        "day": COLORS["visible"],
        "night": COLORS["purple"],
        "lowlight": COLORS["infrared"],
    }

    fig = plt.figure(figsize=(mm(183), mm(105)))
    gs = GridSpec(2, 2, figure=fig, width_ratios=[1.25, 1], height_ratios=[1, 0.78], wspace=0.23, hspace=0.34)

    ax_a = fig.add_subplot(gs[0, 0])
    panel_label(ax_a, "a")
    order = scenes.sort_values("valid_pair_count", ascending=True)
    colors = [light_colors[v] for v in order["light_condition"]]
    ax_a.barh(order["scene_label"], order["valid_pair_count"], color=colors, height=0.65)
    ax_a.set_xlabel("Integrity-checked RGB-infrared pairs")
    ax_a.set_ylabel("Scene")
    soften_axes(ax_a, "x")
    for y, value in enumerate(order["valid_pair_count"]):
        ax_a.text(value + 22, y, f"{value:,}", va="center", fontsize=5.8)
    for label, color in light_colors.items():
        ax_a.scatter([], [], color=color, s=18, label=label.capitalize())
    ax_a.legend(loc="lower right", ncol=3, handletextpad=0.35, columnspacing=0.8)
    ax_a.set_xlim(0, order["valid_pair_count"].max() * 1.15)

    ax_b = fig.add_subplot(gs[0, 1])
    panel_label(ax_b, "b")
    categories = ["Day", "Night", "Low-light", "Gray", "Pseudo", "Wide", "Zoom", "General"]
    matrix = np.zeros((len(scenes), len(categories)))
    for i, row in scenes.reset_index(drop=True).iterrows():
        mapping = {
            "Day": row.light_condition == "day",
            "Night": row.light_condition == "night",
            "Low-light": row.light_condition == "lowlight",
            "Gray": row.thermal_rendering == "grayscale",
            "Pseudo": row.thermal_rendering == "pseudocolor",
            "Wide": row.view_type == "wide",
            "Zoom": row.view_type == "zoom",
            "General": row.view_type not in {"wide", "zoom"},
        }
        matrix[i] = [mapping[c] for c in categories]
    ax_b.imshow(matrix, aspect="auto", cmap=plt.matplotlib.colors.ListedColormap(["#F5F7F8", COLORS["confidence"]]), vmin=0, vmax=1)
    ax_b.set_xticks(range(len(categories)), categories, rotation=38, ha="right")
    ax_b.set_yticks(range(len(scenes)), [f"S{int(x):02d}" for x in scenes.scene_id])
    ax_b.tick_params(length=0)
    ax_b.set_title("Condition coverage", pad=4, fontweight="semibold")
    for x in [2.5, 4.5]:
        ax_b.axvline(x, color="white", lw=2.0)
    for spine in ax_b.spines.values():
        spine.set_visible(False)

    ax_cd = fig.add_subplot(gs[1, :])
    ax_cd.imshow(plt.imread(DRAWIO_PROTOCOL))
    ax_cd.axis("off")

    save_bundle(fig, ROOT / "outputs", "fig02_benchmark_protocol")
    plt.close(fig)


if __name__ == "__main__":
    main()
