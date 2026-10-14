from pathlib import Path
import sys
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "_shared"))
from figure_style import COLORS, save_bundle, soften_axes
from compact_chart_style import configure

ROOT = Path(__file__).resolve().parent


def main():
    configure()
    data = pd.read_csv(ROOT / "source_data/condition_reliability_profile.csv")
    fig, axes = plt.subplots(1, 3, figsize=(7.2, 2.95))
    fig.subplots_adjust(left=.09, right=.985, bottom=.22, top=.76, wspace=.64)
    groups = [("light_condition", ["day", "night", "lowlight"], "(a) Illumination"),
              ("thermal_rendering", ["grayscale", "pseudocolor"], "(b) Rendering"),
              ("view_type", ["wide", "zoom", "general"], "(c) View")]
    names = {"lowlight": "Low-light", "pseudocolor": "Pseudo-\ncolor"}
    for ax, (key, order, title) in zip(axes, groups):
        sub = data.loc[data.group_by == key].set_index("group").loc[order]
        y = np.arange(len(sub))[::-1]
        r = sub.canonical_scene_retention_macro.to_numpy()
        s = sub.accepted_attempted_ratio_micro.to_numpy()
        for yi, ri, si in zip(y, r, s):
            ax.plot([ri, si], [yi, yi], lw=2, color=COLORS["grid"])
        ax.scatter(r, y, color=COLORS["confidence"], marker="o", s=38, label="Scene retention", zorder=3)
        ax.scatter(s, y, edgecolors=COLORS["infrared"], facecolors="white", marker="s", s=38,
                   lw=1.2, label="Accepted / attempted frames", zorder=3)
        for yi, ri, count, total in zip(y, r, sub.canonical_retained_scene_count, sub.scene_count):
            ax.annotate(f"{int(count)}/{int(total)}", (ri, yi), xytext=(0, 8),
                        textcoords="offset points", ha="center", fontsize=8.5,
                        color=COLORS["confidence"])
        ax.set_yticks(y, [names.get(x, x.capitalize()) for x in order])
        ax.set(xlim=(0, 1.05), ylim=(-.6, len(sub)-.3), xlabel="Ratio", title=title)
        ax.set_xticks([0, .5, 1])
        ax.xaxis.set_major_formatter(PercentFormatter(1))
        soften_axes(ax, "x")
    handles, labels = axes[0].get_legend_handles_labels()
    fig.legend(handles, labels, loc="upper center", ncol=2, frameon=False, bbox_to_anchor=(.54, 1.0))
    save_bundle(fig, ROOT / "outputs", "fig10_condition_profile")
    plt.close(fig)


if __name__ == "__main__":
    main()
