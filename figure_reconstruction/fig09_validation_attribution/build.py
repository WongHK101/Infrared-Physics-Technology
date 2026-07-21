from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "_shared"))
from figure_style import COLORS, configure_style, mm, panel_label, save_bundle, soften_axes  # noqa: E402


ROOT = Path(__file__).resolve().parent
DATA = ROOT / "source_data"


def main() -> None:
    configure_style()
    leave = pd.read_csv(DATA / "leave_frame_out_per_scene.csv")
    perturb = pd.read_csv(DATA / "synthetic_perturbation_summary.csv")
    ablation = pd.read_csv(DATA / "ablation_proxy_summary.csv")
    seeds = pd.read_csv(DATA / "multiseed_summary.csv")

    fig = plt.figure(figsize=(mm(183), mm(108)))
    gs = fig.add_gridspec(2, 2, wspace=0.31, hspace=0.39)

    ax_a = fig.add_subplot(gs[0, 0])
    panel_label(ax_a, "a", x=-0.09)
    order = leave.sort_values("mean_leave_out_displacement_px")
    y = np.arange(len(order))
    passed = order["canonical_scene_pass"].astype(str).str.lower().eq("true")
    colors = np.where(passed, COLORS["confidence"], COLORS["filtered"])
    ax_a.hlines(y, 0, order["mean_leave_out_displacement_px"], color=COLORS["grid"], lw=1.4)
    ax_a.scatter(order["mean_leave_out_displacement_px"], y, color=colors, s=25, zorder=3)
    ax_a.axvline(order["mean_leave_out_displacement_px"].median(), color=COLORS["canonical"], lw=1.0, ls=(0, (3, 2)))
    ax_a.set_yticks(y, [f"S{int(x):02d}" for x in order.scene_id])
    ax_a.set_xlabel("Mean leave-frame-out displacement (px)")
    ax_a.set_title("Leave-frame-out consensus · 75 folds", fontweight="semibold", pad=4)
    soften_axes(ax_a, "x")
    ax_a.text(order["mean_leave_out_displacement_px"].median(), len(order) - 0.2, " median 1.39 px", color=COLORS["canonical"], fontsize=5.7, va="top")

    ax_b = fig.add_subplot(gs[0, 1])
    panel_label(ax_b, "b", x=-0.09)
    mode_colors = {"translation": COLORS["visible"], "rotation": COLORS["infrared"], "scale": COLORS["purple"]}
    for mode, sub in perturb.groupby("mode"):
        ax_b.plot(sub["severity_px"], sub["mean_delta_joint_score"], marker="o", ms=3.6, lw=1.5, label=mode.capitalize(), color=mode_colors.get(mode, COLORS["muted"]))
    ax_b.axhline(0, color=COLORS["grid"], lw=0.8)
    ax_b.set_xlabel("Perturbation severity")
    ax_b.set_ylabel("Change in joint QA score")
    ax_b.set_title("Controlled perturbation · 675 trials", fontweight="semibold", pad=4)
    soften_axes(ax_b)
    ax_b.legend(loc="lower left")

    ax_c = fig.add_subplot(gs[1, 0])
    panel_label(ax_c, "c", x=-0.09)
    stage_labels = ["Pairwise\nevidence", "Robust\nconsensus", "QA-aware\nverification"]
    x = np.arange(len(ablation))
    ax_c.plot(x, ablation["mean_delta_edge_f1"], marker="o", color=COLORS["visible"], label="Edge gain")
    ax_c.plot(x, ablation["mean_delta_grad_ncc"], marker="s", color=COLORS["infrared"], label="Gradient-NCC gain")
    ax_c.plot(x, ablation["mean_severe_outlier_ratio"], marker="D", color=COLORS["canonical"], label="Severe-outlier ratio")
    ax_c.set_xticks(x, stage_labels)
    ax_c.set_ylim(0, 0.17)
    ax_c.set_ylabel("Ratio / metric change")
    ax_c.set_title("Cumulative modules · 8-scene subset", fontweight="semibold", pad=4)
    soften_axes(ax_c)
    ax_c.legend(loc="lower right")
    ax_c.annotate("dispersion\n151.2 → 52.5 px", xy=(1, ablation.loc[1, "mean_delta_edge_f1"]), xytext=(0.42, 0.158), textcoords="data", fontsize=5.6, color=COLORS["confidence"], arrowprops={"arrowstyle": "->", "lw": 0.7, "color": COLORS["confidence"]})

    ax_d = fig.add_subplot(gs[1, 1])
    panel_label(ax_d, "d", x=-0.09)
    bars = ax_d.bar(seeds["seed"].astype(str), seeds["canonical_pass_count"], color=[COLORS["filtered"], COLORS["filtered"], COLORS["confidence"], COLORS["filtered"]], width=0.62)
    ax_d.set_ylim(0, 8.5)
    ax_d.set_xlabel("Random-selection seed")
    ax_d.set_ylabel("Canonical products / 8 scenes")
    ax_d.set_title("Random-selection sensitivity · 8 scenes", fontweight="semibold", pad=4)
    soften_axes(ax_d)
    for bar, value, frames in zip(bars, seeds["canonical_pass_count"], seeds["accepted_frames_mean"]):
        ax_d.text(
            bar.get_x() + bar.get_width() / 2,
            value + 0.18,
            f"{int(value)}/8\n{frames:.1f} frames",
            ha="center",
            fontsize=5.8,
            fontweight="semibold",
            linespacing=1.05,
        )

    save_bundle(fig, ROOT / "outputs", "fig09_validation_attribution")
    plt.close(fig)


if __name__ == "__main__":
    main()
