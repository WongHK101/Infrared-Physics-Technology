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


def condition_panel(ax, data, group_by, title, panel) -> None:
    panel_label(ax, panel)
    sub = data[data["group_by"] == group_by].copy()
    labels = sub["group"].str.replace("lowlight", "low-light").str.capitalize()
    y = np.arange(len(sub))[::-1]
    retention = sub["canonical_scene_retention_macro"].to_numpy()
    support = sub["accepted_attempted_ratio_micro"].to_numpy()
    for yi, r, s in zip(y, retention, support):
        ax.plot([r, s], [yi, yi], color=COLORS["grid"], lw=2.0)
    ax.scatter(retention, y, s=37, color=COLORS["confidence"], label="Scene retention")
    ax.scatter(support, y, s=42, facecolor="white", edgecolor=COLORS["infrared"], linewidth=1.2, label="Accepted support")
    ax.set_yticks(y, labels)
    ax.set_xlim(0, 1.04)
    ax.set_xlabel("Ratio")
    ax.set_title(title, fontweight="semibold", pad=4)
    soften_axes(ax, "x")
    for yi, count, total in zip(y, sub["canonical_retained_scene_count"], sub["scene_count"]):
        ax.text(1.03, yi, f"{int(count)}/{int(total)}", ha="right", va="center", fontsize=5.6, color=COLORS["muted"])


def main() -> None:
    configure_style()
    curve = pd.read_csv(DATA / "risk_coverage.csv")
    canonical = pd.read_csv(DATA / "canonical_operating_point.csv").iloc[0]
    condition = pd.read_csv(DATA / "condition_reliability_profile.csv")

    fig = plt.figure(figsize=(mm(183), mm(108)))
    gs = fig.add_gridspec(2, 2, wspace=0.30, hspace=0.38)

    ax_a = fig.add_subplot(gs[0, 0])
    panel_label(ax_a, "a")
    x = curve["scene_coverage"]
    y = curve["mean_severe_outlier_ratio"]
    ax_a.plot(x, y, color=COLORS["visible"], lw=1.7, marker="o", ms=3.2, label="Score-ranked profile")
    ax_a.scatter([canonical.scene_coverage], [canonical.mean_severe_outlier_ratio], s=100, marker="*", color=COLORS["canonical"], edgecolor="white", linewidth=0.6, zorder=5, label="Canonical QA gate")
    for count, name in [(3, "conservative"), (8, "balanced"), (13, "permissive"), (15, "inclusive")]:
        row = curve[curve["retained_scene_count"] == count].iloc[0]
        ax_a.annotate(name, (row.scene_coverage, row.mean_severe_outlier_ratio), xytext=(2, 5), textcoords="offset points", fontsize=5.5, color=COLORS["muted"])
    ax_a.set_xlabel("Scene coverage")
    ax_a.set_ylabel("Mean severe-outlier ratio")
    ax_a.set_xlim(0, 1.03)
    ax_a.set_ylim(-0.003, max(0.05, y.max() * 1.25))
    ax_a.set_title("Score-ranked reliability profile", fontweight="semibold", pad=4)
    soften_axes(ax_a)
    ax_a.legend(loc="upper left")

    ax_b = fig.add_subplot(gs[0, 1])
    panel_label(ax_b, "b")
    ax_b.plot(curve["pair_coverage_micro"], curve["accepted_attempted_ratio_micro"], color=COLORS["infrared"], lw=1.7, marker="o", ms=3.2)
    ax_b.scatter([canonical.pair_coverage_micro], [canonical.accepted_attempted_ratio_micro], s=100, marker="*", color=COLORS["canonical"], edgecolor="white", linewidth=0.6, zorder=5)
    ax_b.annotate("canonical\n74.4% pairs", (canonical.pair_coverage_micro, canonical.accepted_attempted_ratio_micro), xytext=(7, -2), textcoords="offset points", fontsize=5.8, color=COLORS["canonical"], va="center")
    ax_b.set_xlabel("Pair coverage")
    ax_b.set_ylabel("Accepted / attempted frame support")
    ax_b.set_xlim(0, 1.03)
    ax_b.set_ylim(0, 1.03)
    ax_b.set_title("Evidence support across operating points", fontweight="semibold", pad=4)
    soften_axes(ax_b)

    ax_c = fig.add_subplot(gs[1, 0])
    condition_panel(ax_c, condition, "light_condition", "Illumination profile", "c")
    ax_c.text(0.02, 0.96, "●  Scene retention", transform=ax_c.transAxes, color=COLORS["confidence"], fontsize=5.8, va="top")
    ax_c.text(0.02, 0.86, "○  Accepted support", transform=ax_c.transAxes, color=COLORS["infrared"], fontsize=5.8, va="top")

    ax_d = fig.add_subplot(gs[1, 1])
    panel_label(ax_d, "d")
    rendering = condition[condition["group_by"] == "thermal_rendering"].copy()
    view = condition[condition["group_by"] == "view_type"].copy()
    combined = pd.concat([rendering.assign(section="Rendering"), view.assign(section="View")], ignore_index=True)
    labels = combined["group"].str.capitalize().str.replace("Pseudocolor", "Pseudocolor")
    yv = np.arange(len(combined))[::-1]
    retention = combined["canonical_scene_retention_macro"].to_numpy()
    support = combined["accepted_attempted_ratio_micro"].to_numpy()
    for yi, r, s in zip(yv, retention, support):
        ax_d.plot([r, s], [yi, yi], color=COLORS["grid"], lw=2.0)
    ax_d.scatter(retention, yv, s=37, color=COLORS["confidence"])
    ax_d.scatter(support, yv, s=42, facecolor="white", edgecolor=COLORS["infrared"], linewidth=1.2)
    ax_d.set_yticks(yv, labels)
    ax_d.set_xlim(0, 1.04)
    ax_d.set_xlabel("Ratio")
    ax_d.set_title("Rendering and view profiles", fontweight="semibold", pad=4)
    soften_axes(ax_d, "x")
    split_y = len(view) - 0.5
    ax_d.axhline(split_y, color=COLORS["grid"], lw=0.9)
    ax_d.text(1.03, yv[0] + 0.35, "Rendering", ha="right", fontsize=5.5, color=COLORS["muted"])
    ax_d.text(1.03, split_y - 0.35, "View", ha="right", fontsize=5.5, color=COLORS["muted"])

    save_bundle(fig, ROOT / "outputs", "fig08_operating_profile")
    plt.close(fig)


if __name__ == "__main__":
    main()
