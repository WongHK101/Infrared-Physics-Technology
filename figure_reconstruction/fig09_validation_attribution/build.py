from pathlib import Path
import sys
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "_shared"))
from figure_style import COLORS, save_bundle, soften_axes
from compact_chart_style import configure

ROOT = Path(__file__).resolve().parent


def main():
    configure()
    leave = pd.read_csv(ROOT / "source_data/leave_frame_out_per_scene.csv")
    perturb = pd.read_csv(ROOT / "source_data/synthetic_perturbation_summary.csv")
    fig, axes = plt.subplots(1, 2, figsize=(7.2, 3.0))
    fig.subplots_adjust(left=.08, right=.98, bottom=.23, top=.85, wspace=.38)
    ax = axes[0]
    data = leave.sort_values("mean_leave_out_displacement_px", ascending=False)
    passed = data.canonical_scene_pass.astype(str).str.lower().eq("true")
    colors = np.where(passed, COLORS["confidence"], COLORS["filtered"])
    ax.bar(np.arange(15), data.mean_leave_out_displacement_px, color=colors, width=.7)
    median = leave.mean_leave_out_displacement_px.median()
    ax.axhline(median, ls="--", color=COLORS["canonical"], lw=1)
    ax.set_xticks(np.arange(15), [f"S{int(s):02d}" for s in data.scene_id], rotation=90)
    ax.set(xlabel="Scene ID", ylabel="Mean fold displacement (px)", ylim=(0, 10.4),
           title="(a) Consensus stability")
    ax.text(.97, .63, f"All-scene median: {median:.2f} px", transform=ax.transAxes,
            ha="right", color=COLORS["canonical"], fontsize=9)
    ax.legend(handles=[Patch(color=COLORS["confidence"], label="Retained"),
                       Patch(color=COLORS["filtered"], label="QA-filtered")],
              loc="upper right", frameon=False)
    ax = axes[1]
    for mode, color, marker in [("translation", COLORS["visible"], "o"),
                                ("rotation", COLORS["infrared"], "s"),
                                ("scale", COLORS["purple"], "^")]:
        data = perturb.loc[perturb["mode"] == mode].sort_values("severity_px")
        ax.plot(data.severity_px, data.mean_delta_joint_score,
                color=color, marker=marker, ms=4, lw=1.5, label=mode.capitalize())
    ax.set(xlabel="Nominal perturbation severity (px)", ylabel="Mean joint-score change",
           title="(b) Quality-signal sensitivity")
    ax.legend(loc="lower left", frameon=False)
    for ax in axes:
        soften_axes(ax)
    save_bundle(fig, ROOT / "outputs", "fig09_validation_attribution")
    plt.close(fig)


if __name__ == "__main__":
    main()
