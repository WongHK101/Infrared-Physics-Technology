from pathlib import Path
import sys

import matplotlib.pyplot as plt
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "_shared"))
from editable_diagram import overlay_gallery
from compact_chart_style import configure
from figure_style import COLORS, save_bundle, soften_axes

ROOT = Path(__file__).resolve().parent


def qa_scatter():
    configure()
    data = pd.read_csv(ROOT / "source_data/per_scene_reliability_table.csv")
    fig, ax = plt.subplots(figsize=(8.3, 3.5))
    passed = data.canonical_scene_pass.astype(str).str.lower().eq("true")
    sizes = 45 + 300 * data.robust_reject_ratio.clip(0, .5)
    for mask, color, marker, label in [
        (~passed, COLORS["filtered"], "s", "QA-filtered"),
        (passed, COLORS["confidence"], "o", "Canonical retained"),
    ]:
        ax.scatter(data.loc[mask, "accepted_ratio"], data.loc[mask, "severe_outlier_ratio"],
                   s=sizes[mask], c=color, marker=marker, label=label,
                   edgecolor="white", linewidth=.5, zorder=3)
    offsets = {1:(7,7), 2:(7,7), 3:(-12,-20), 4:(-25,8), 5:(-10,8),
               6:(-20,20), 7:(-5,8), 8:(-12,8), 9:(-8,8), 10:(-12,8),
               11:(-12,8), 12:(8,10), 13:(-32,-22), 14:(-12,23), 15:(-12,8)}
    for r in data.itertuples():
        ax.annotate(f"S{int(r.scene_id):02d}", (r.accepted_ratio, r.severe_outlier_ratio),
                    xytext=offsets[int(r.scene_id)], textcoords="offset points",
                    fontsize=8, arrowprops={"arrowstyle":"-", "color":"#A4ADB4",
                                          "lw":.5, "shrinkA":2, "shrinkB":4})
    ax.axhline(.10, color=COLORS["canonical"], ls="--", lw=.8)
    ax.text(.99, .104, "Outlier reference",
            ha="right", fontsize=8, color=COLORS["canonical"])
    ax.set(xlim=(-.02, 1.055), ylim=(-.025, .205),
           xlabel="Accepted-frame ratio", ylabel="Severe relative-outlier ratio")
    ax.legend(frameon=False, loc="upper left", ncol=2)
    soften_axes(ax)
    save_bundle(fig, ROOT / "outputs", "fig07_qa_scatter")
    plt.close(fig)


def main():
    overlay_gallery(ROOT, "fig07_reliability_selection", [
        ("scene01", "S01 Wide<br/>Retained", True),
        ("scene02", "S02 Zoom<br/>Filtered", False),
    ])
    overlay_gallery(ROOT, "fig07_night_control", [
        ("scene04", "S04 Zoom<br/>Retained", True),
        ("scene03", "S03 Wide<br/>Filtered", False),
    ])
    qa_scatter()


if __name__ == "__main__":
    main()

