from __future__ import annotations

import json
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from PIL import Image
from skimage import color, feature, transform

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "_shared"))
from figure_style import (  # noqa: E402
    COLORS,
    configure_style,
    mm,
    panel_label,
    placeholder,
    save_bundle,
    soften_axes,
)


ROOT = Path(__file__).resolve().parent
DATA = ROOT / "source_data"
ASSETS = ROOT / "source_assets"


def edge_overlay(rgb_path: Path, ir_path: Path, matrix: list[list[float]]) -> np.ndarray:
    rgb = np.asarray(Image.open(rgb_path).convert("RGB")) / 255.0
    ir = np.asarray(Image.open(ir_path).convert("RGB")) / 255.0
    target_scale = min(1.0, 1000.0 / max(rgb.shape[:2]))
    out_shape = (max(1, int(rgb.shape[0] * target_scale)), max(1, int(rgb.shape[1] * target_scale)))
    rgb_small = transform.resize(rgb, (*out_shape, 3), preserve_range=True, anti_aliasing=True)
    scale = np.array([[target_scale, 0, 0], [0, target_scale, 0], [0, 0, 1]], float)
    h_scaled = scale @ np.asarray(matrix, float)
    tform = transform.ProjectiveTransform(matrix=h_scaled)
    warped = transform.warp(ir, inverse_map=tform.inverse, output_shape=out_shape, preserve_range=True)
    rgb_edge = feature.canny(color.rgb2gray(rgb_small), sigma=1.35)
    ir_edge = feature.canny(color.rgb2gray(warped), sigma=1.15)
    canvas = np.ones((*out_shape, 3), float)
    canvas[rgb_edge] = np.array([0.05, 0.65, 0.78])
    canvas[ir_edge] = np.array([0.88, 0.20, 0.18])
    both = rgb_edge & ir_edge
    canvas[both] = np.array([0.18, 0.18, 0.18])
    return canvas


def main() -> None:
    configure_style()
    metrics = pd.read_csv(DATA / "pairwise_methods.csv")
    selected = json.loads((DATA / "selected_pair_homographies.json").read_text(encoding="utf-8"))
    fig = plt.figure(figsize=(mm(183), mm(105)))
    gs = fig.add_gridspec(2, 1, height_ratios=[0.88, 1.12], hspace=0.35)

    ax_a = fig.add_subplot(gs[0])
    panel_label(ax_a, "a", x=-0.015, y=1.02)
    y = np.arange(len(metrics))[::-1]
    availability = metrics["h_available_pct"].to_numpy() / 100.0
    coverage = metrics["mean_coverage"].to_numpy()
    for yi, a, c in zip(y, availability, coverage):
        ax_a.plot([c, a], [yi, yi], color=COLORS["grid"], lw=2.1, zorder=1)
    ax_a.scatter(coverage, y, s=35, color=COLORS["visible"], label="Mean coverage", zorder=3)
    ax_a.scatter(availability, y, s=42, facecolor="white", edgecolor=COLORS["confidence"], linewidth=1.3, label="H availability", zorder=4)
    ax_a.set_yticks(y, metrics["method"])
    ax_a.set_xlim(0.30, 1.025)
    ax_a.set_xlabel("Fraction of evaluated pairs / normalized spatial support")
    ax_a.set_title("Availability and coverage are complementary", fontweight="semibold", pad=4)
    soften_axes(ax_a, "x")
    ax_a.legend(loc="lower right", ncol=2)

    bottom = gs[1].subgridspec(1, 6, wspace=0.05)
    methods = ["SIFT", "RIFT2", "LoFTR", "XoFTR", "RoMa", "raw MINIMA"]
    rgb_path = ASSETS / "scene04_pair000020_rgb.jpg"
    ir_path = ASSETS / "scene04_pair000020_infrared.jpg"
    for idx, method in enumerate(methods):
        ax = fig.add_subplot(bottom[0, idx])
        if idx == 0:
            panel_label(ax, "b", x=-0.10, y=1.03)
        matrix = selected["methods"].get(method)
        if matrix is None:
            placeholder(ax, "RIFT2 overlay", "Insert frozen strong-run\nper-pair homography")
        else:
            overlay = edge_overlay(rgb_path, ir_path, matrix)
            ax.imshow(overlay)
            ax.set_xticks([])
            ax.set_yticks([])
            for spine in ax.spines.values():
                spine.set_visible(True)
                spine.set_color("#C8D0D6")
                spine.set_linewidth(0.45)
        ax.set_title(method, fontsize=6.5, fontweight="semibold", pad=2)
    fig.text(0.50, 0.015, "Fixed S04 pair · cyan: RGB edges · red: infrared edges · dark overlap: edge agreement", ha="center", fontsize=6.2, color=COLORS["muted"])

    save_bundle(fig, ROOT / "outputs", "fig05_pairwise_evidence")
    plt.close(fig)


if __name__ == "__main__":
    main()

