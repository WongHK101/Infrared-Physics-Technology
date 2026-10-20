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
    fig, ax = plt.subplots(figsize=(7.2, 3.5))
    fig.subplots_adjust(left=.10, right=.97, bottom=.17, top=.75)
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
               6:(-20,20), 7:(-5,8), 8:(-12,8), 9:(-8,16), 10:(-12,8),
               11:(-12,16), 12:(8,16), 13:(-32,-22), 14:(-12,23), 15:(-12,16)}
    for r in data.itertuples():
        ax.annotate(f"S{int(r.scene_id):02d}", (r.accepted_ratio, r.severe_outlier_ratio),
                    xytext=offsets[int(r.scene_id)], textcoords="offset points",
                    fontsize=8, arrowprops={"arrowstyle":"-", "color":"#A4ADB4",
                                          "lw":.5, "shrinkA":2, "shrinkB":4})
    ax.axhline(.10, color=COLORS["canonical"], ls="--", lw=.8)
    ax.text(.99, .121, "Outlier reference",
            ha="right", fontsize=8, color=COLORS["canonical"])
    ax.set(xlim=(-.02, 1.055), ylim=(-.025, .205),
           xlabel="Accepted-frame ratio", ylabel="Severe relative-outlier ratio")
    _, status_labels = ax.get_legend_handles_labels()
    # Separate status keys from the quantitative marker-size encoding.
    status_handles = [plt.Line2D([], [], marker=marker, color=color, ls="none", ms=6)
                      for color, marker in [(COLORS["filtered"], "s"),
                                             (COLORS["confidence"], "o")]]
    fig.legend(status_handles, status_labels, loc="upper center",
               bbox_to_anchor=(.52, 1.0), ncol=2)
    size_handles = [ax.scatter([], [], s=45+300*value, c=COLORS["muted"],
                               edgecolor="white", linewidth=.5)
                    for value in (0, .25, .50)]
    fig.legend(size_handles, ["0", "0.25", "0.50"], title="Robust-rejection ratio",
               title_fontsize=8.5, loc="upper center", bbox_to_anchor=(.52, .93),
               ncol=3)
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

