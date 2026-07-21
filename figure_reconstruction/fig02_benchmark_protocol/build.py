from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.gridspec import GridSpec
from matplotlib.patches import Rectangle

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "_shared"))
from figure_style import (  # noqa: E402
    COLORS,
    arrow,
    configure_style,
    mm,
    panel_label,
    rounded_box,
    save_bundle,
    soften_axes,
)


ROOT = Path(__file__).resolve().parent
DATA = ROOT / "source_data"


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

    ax_c = fig.add_subplot(gs[1, 0])
    panel_label(ax_c, "c")
    ax_c.axis("off")
    rounded_box(ax_c, (0.02, 0.26), 0.25, 0.50, "Collection\n6,039 pairs", COLORS["visible_light"], COLORS["visible"])
    rounded_box(ax_c, (0.38, 0.26), 0.24, 0.50, "Integrity gate\ndecode · pairing · hash", "#F5F7F8", COLORS["muted"], fontsize=6.3)
    rounded_box(ax_c, (0.73, 0.26), 0.25, 0.50, "Official split\n6,037 pairs", COLORS["confidence_light"], COLORS["confidence"])
    arrow(ax_c, (0.28, 0.51), (0.37, 0.51))
    arrow(ax_c, (0.63, 0.51), (0.72, 0.51))
    ax_c.text(0.50, 0.12, "Frozen, versioned evaluation manifest", ha="center", color=COLORS["muted"], fontsize=6.1)

    ax_d = fig.add_subplot(gs[1, 1])
    panel_label(ax_d, "d")
    ax_d.axis("off")
    tracks = [
        (0.68, "Pairwise evidence", "availability · support · coverage", COLORS["visible_light"], COLORS["visible"]),
        (0.38, "Scene products", "consensus · QA · canonical decision", COLORS["confidence_light"], COLORS["confidence"]),
        (0.08, "Operating profile", "score ranking · coverage · condition", COLORS["infrared_light"], COLORS["infrared"]),
    ]
    for y, title, subtitle, fc, ec in tracks:
        rounded_box(ax_d, (0.04, y), 0.92, 0.22, "", fc, ec)
        ax_d.text(0.09, y + 0.14, title, fontweight="bold", fontsize=7.0, va="center")
        ax_d.text(0.09, y + 0.07, subtitle, fontsize=6.1, color=COLORS["muted"], va="center")
        ax_d.add_patch(Rectangle((0.84, y + 0.065), 0.07, 0.09, fc="white", ec=ec, lw=0.8))

    save_bundle(fig, ROOT / "outputs", "fig02_benchmark_protocol")
    plt.close(fig)


if __name__ == "__main__":
    main()
