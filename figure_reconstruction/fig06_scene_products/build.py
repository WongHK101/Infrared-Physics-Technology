from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.pyplot as plt

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "_shared"))
from figure_style import COLORS, configure_style, image_panel, mm, panel_label, save_bundle  # noqa: E402


ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / "source_assets"


def find(scene: str, suffix: str) -> Path:
    matches = sorted(ASSETS.glob(f"{scene}_*_{suffix}.jpg"))
    if not matches:
        raise FileNotFoundError(f"Missing asset: {scene} * {suffix}")
    return matches[0]


def main() -> None:
    configure_style()
    fig = plt.figure(figsize=(mm(183), mm(122)))
    gs = fig.add_gridspec(4, 5, wspace=0.035, hspace=0.14)
    scenes = [
        ("scene07", "S07 · day · gray · tower"),
        ("scene04", "S04 · night · gray · zoom"),
        ("scene10", "S10 · day · pseudocolor"),
        ("scene14", "S14 · low-light · pseudocolor"),
    ]
    columns = [
        ("rgb_selected_crop", "RGB"),
        ("infrared_selected_crop", "Infrared"),
        ("before_resize_overlay_crop", "Before"),
        ("after_scene_homography_overlay_crop", "Scene product"),
        ("edge_overlay_crop", "Edge agreement"),
    ]
    for row, (scene, scene_label) in enumerate(scenes):
        for col, (suffix, title) in enumerate(columns):
            ax = fig.add_subplot(gs[row, col])
            image_panel(ax, find(scene, suffix), title if row == 0 else None)
            if col == 0:
                ax.text(
                    -0.04,
                    0.5,
                    scene_label,
                    transform=ax.transAxes,
                    ha="right",
                    va="center",
                    rotation=90,
                    fontsize=6.2,
                    fontweight="semibold",
                    color=COLORS["ink"],
                )
            if row == 0 and col == 0:
                panel_label(ax, "a", x=-0.18, y=1.08)
    fig.text(0.995, 0.015, "All rows: canonical high-confidence scene products", ha="right", fontsize=5.8, color=COLORS["confidence"])
    save_bundle(fig, ROOT / "outputs", "fig06_scene_products")
    plt.close(fig)


if __name__ == "__main__":
    main()
