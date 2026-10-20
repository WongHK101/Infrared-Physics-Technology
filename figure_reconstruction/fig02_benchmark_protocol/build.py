from pathlib import Path
import sys

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "_shared"))
from editable_diagram import Diagram, BLUE, GREEN, ORANGE
from compact_chart_style import configure
from figure_style import COLORS, save_bundle, soften_axes

ROOT = Path(__file__).resolve().parent


def dataset_details():
    configure()
    scenes = pd.read_csv(ROOT / "source_data/UAV-TAlign-12K_per_scene_valid_counts.csv")
    fig, (ax, bx) = plt.subplots(1, 2, figsize=(7.2, 4.1),
                               gridspec_kw={"width_ratios": [1.25, 1], "wspace": .30})
    order = scenes.sort_values("valid_pair_count")
    colors = {"day": COLORS["visible"], "night": COLORS["purple"],
              "lowlight": COLORS["infrared"]}
    ax.barh([f"S{x:02d}" for x in order.scene_id], order.valid_pair_count,
            color=[colors[x] for x in order.light_condition], height=.67)
    for y, n in enumerate(order.valid_pair_count):
        ax.text(n + 15, y, f"{n:,}", va="center", fontsize=8)
    ax.set_xlim(0, order.valid_pair_count.max()*1.15)
    ax.set_xlabel("Integrity-checked pairs")
    ax.set_title("(a) Pair count per scene", loc="left")
    soften_axes(ax, "x")
    for condition, color in colors.items():
        name = {"day": "Day", "night": "Night", "lowlight": "Low-light"}[condition]
        ax.scatter([], [], color=color, s=20, label=name)
    ax.legend(loc="lower right", frameon=False)
    fields = [("light_condition", "day"), ("light_condition", "night"),
              ("light_condition", "lowlight"), ("thermal_rendering", "grayscale"),
              ("thermal_rendering", "pseudocolor"), ("view_type", "wide"),
              ("view_type", "zoom"), ("view_type", "general")]
    matrix = np.column_stack([scenes[field].eq(value) for field, value in fields])
    bx.imshow(matrix, aspect="auto",
              cmap=plt.matplotlib.colors.ListedColormap(["#F3F5F6", COLORS["confidence"]]))
    bx.set_yticks(range(15), [f"S{x:02d}" for x in scenes.scene_id])
    bx.set_xticks(range(8), ["Day", "Night", "Low-light", "Grayscale", "Pseudocolor",
                             "Wide", "Zoom", "General"], rotation=60, ha="right")
    bx.tick_params(length=0)
    bx.set_title("(b) Acquisition attributes", loc="left")
    for x in (2.5, 4.5):
        bx.axvline(x, color="white", lw=2)
    save_bundle(fig, ROOT / "outputs", "fig02_dataset_details")
    plt.close(fig)


def main():
    d = Diagram(1200, 435)
    tracks = [
        (0, BLUE, "#EEF5FB", "(a) Pairwise evidence",
         "RGB-infrared pair<br/>(I<sub>i</sub><sup>R</sup>, I<sub>i</sub><sup>T</sup>)",
         "Homography H<sub>i</sub>", "Availability<br/>Spatial support",
         "Match + fit", "Summarize"),
        (145, GREEN, "#EEF6F0", "(b) Scene products",
         "Scene evidence<br/>{H<sub>i</sub>, q<sub>i</sub>}",
         "Scene consensus H&#772;<sub>S</sub>",
         "Canonical status y<sub>S</sub>",
         "Aggregate", "Fixed QA gate"),
        (290, ORANGE, "#FCF3EB", "(c) Operating profile",
         "Scene diagnostics", "Reliability score R(S)",
         "Reliability-coverage",
         "Fixed score", "Rank / top-K"),
    ]
    for y, color, fill, title, left, middle, right, link1, link2 in tracks:
        d.text(10, y, 900, 35, title, size=29, color=color, align="left", bold=True)
        for x, w, text in [(10, 250, left), (470, 265, middle), (925, 265, right)]:
            d.box(x, y+53, w, 80, fill=fill, stroke=color, rounded=False)
            d.text(x+8, y+58, w-16, 70, text, size=25)
        d.line([(260, y+93), (470, y+93)], color=color)
        d.line([(735, y+93), (925, y+93)], color=color)
        d.text(267, y+46, 196, 35, link1, size=23)
        d.text(737, y+46, 185, 35, link2, size=23)
    d.export(ROOT, "fig02_benchmark_protocol")
    dataset_details()


if __name__ == "__main__":
    main()
