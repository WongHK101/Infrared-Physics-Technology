from __future__ import annotations

import json
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

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
DRAWIO_LOGIC = ROOT / "drawio_source" / "fig04_matched_control_logic.png"


def load_scene(scene: str) -> dict:
    return json.loads((DATA / f"scene{scene}_result.json").read_text(encoding="utf-8"))


def main() -> None:
    configure_style()
    s01 = load_scene("01")
    s02 = load_scene("02")
    b1, b2 = s01["band_payload"], s02["band_payload"]

    fig = plt.figure(figsize=(mm(183), mm(105)))
    gs = fig.add_gridspec(
        2,
        3,
        width_ratios=[1.18, 1.1, 0.92],
        height_ratios=[1, 0.78],
        wspace=0.32,
        hspace=0.28,
    )

    ax_a = fig.add_subplot(gs[0, 0])
    panel_label(ax_a, "a", x=-0.10)
    for scene, payload, offset, color, label in [
        ("S01", b1, -0.10, COLORS["confidence"], "S01 high-confidence"),
        ("S02", b2, 0.10, COLORS["filtered"], "S02 QA-filtered"),
    ]:
        rows = payload["homography_stability"]["per_homography"]
        dist = np.array([r["param_distance_to_median"] for r in rows], float)
        keep = np.array([r["robust_keep"] for r in rows], bool)
        x = np.arange(1, len(rows) + 1) + offset
        ax_a.scatter(x[keep], dist[keep], s=23, color=color, label=label, edgecolor="white", linewidth=0.35, zorder=3)
        ax_a.scatter(x[~keep], dist[~keep], s=30, color=COLORS["canonical"], marker="x", linewidth=1.0, zorder=4)
    ax_a.set_yscale("symlog", linthresh=1)
    ax_a.set_xlabel("Selected hypothesis index")
    ax_a.set_ylabel("Distance to median hypothesis")
    ax_a.set_title("Robust hypothesis support", fontweight="semibold", pad=4)
    soften_axes(ax_a)
    ax_a.legend(loc="upper left")
    ax_a.text(0.98, 0.03, "× robust rejection", transform=ax_a.transAxes, ha="right", color=COLORS["canonical"], fontsize=5.8)

    ax_b = fig.add_subplot(gs[0, 1])
    panel_label(ax_b, "b", x=-0.10)
    for payload, color, marker, label in [
        (b1, COLORS["confidence"], "o", "S01"),
        (b2, COLORS["filtered"], "s", "S02"),
    ]:
        frames = payload["per_frame"]
        edge = np.array([f["delta_edge_f1"] for f in frames])
        grad = np.array([f["delta_grad_ncc"] for f in frames])
        severe = np.array([f.get("severe_misalignment", False) for f in frames])
        ax_b.scatter(edge[~severe], grad[~severe], s=25, color=color, marker=marker, alpha=0.88, label=label, edgecolor="white", linewidth=0.35)
        ax_b.scatter(edge[severe], grad[severe], s=48, facecolor="white", edgecolor=COLORS["canonical"], marker="X", linewidth=1.0)
    ax_b.axhline(0, color=COLORS["grid"], lw=0.8)
    ax_b.axvline(0, color=COLORS["grid"], lw=0.8)
    ax_b.set_xlabel("Change in edge F1")
    ax_b.set_ylabel("Change in gradient NCC")
    ax_b.set_title("Frame-level QA response", fontweight="semibold", pad=4)
    ax_b.legend(loc="upper left")
    ax_b.text(0.98, 0.03, "X severe relative outlier", transform=ax_b.transAxes, ha="right", color=COLORS["canonical"], fontsize=5.8)

    ax_c = fig.add_subplot(gs[0, 2])
    panel_label(ax_c, "c", x=-0.10)
    labels = ["Accepted\nratio", "Robust\nreject", "Severe\noutlier"]
    values1 = [b1["qa_decision_inputs"]["accepted_ratio"], b1["qa_decision_inputs"]["robust_reject_ratio"], b1["qa_decision_inputs"]["severe_outlier_ratio"]]
    values2 = [b2["qa_decision_inputs"]["accepted_ratio"], b2["qa_decision_inputs"]["robust_reject_ratio"], b2["qa_decision_inputs"]["severe_outlier_ratio"]]
    x = np.arange(3)
    ax_c.bar(x - 0.18, values1, 0.34, color=COLORS["confidence"], label="S01")
    ax_c.bar(x + 0.18, values2, 0.34, color=COLORS["filtered"], label="S02")
    references = [0.80, 0.25, 0.10]
    ax_c.scatter(x, references, marker="_", s=145, linewidth=1.35, color=COLORS["canonical"], zorder=5, label="QA reference")
    ax_c.set_xticks(x, labels)
    ax_c.set_ylim(0, 1.06)
    ax_c.set_ylabel("Ratio")
    ax_c.set_title("QA decision evidence", fontweight="semibold", pad=4)
    soften_axes(ax_c)
    ax_c.legend(loc="upper right")

    ax_d = fig.add_subplot(gs[1, :])
    ax_d.imshow(plt.imread(DRAWIO_LOGIC))
    ax_d.axis("off")

    save_bundle(fig, ROOT / "outputs", "fig04_consensus_qa")
    plt.close(fig)


if __name__ == "__main__":
    main()
