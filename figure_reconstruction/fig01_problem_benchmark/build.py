from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec, GridSpecFromSubplotSpec

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "_shared"))
from figure_style import (  # noqa: E402
    configure_style,
    image_panel,
    mm,
    panel_label,
    save_bundle,
)


ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / "source_assets"
DRAWIO_PANEL = ROOT / "drawio_source" / "fig01_acquisition_panel.png"


def find(scene: str, suffix: str) -> Path:
    matches = sorted(ASSETS.glob(f"{scene}_*_{suffix}.jpg"))
    if not matches:
        raise FileNotFoundError(f"Missing asset: {scene} * {suffix}")
    return matches[0]


def main() -> None:
    configure_style()
    fig = plt.figure(figsize=(mm(183), mm(105)))
    outer = GridSpec(
        3,
        3,
        figure=fig,
        width_ratios=[0.90, 1, 1],
        height_ratios=[1, 1, 1],
        wspace=0.10,
        hspace=0.10,
    )

    ax_a = fig.add_subplot(outer[:, 0])
    panel_label(ax_a, "a", x=-0.02, y=1.01)
    ax_a.imshow(plt.imread(DRAWIO_PANEL))
    ax_a.axis("off")

    examples = [
        ("scene01", "S01  day · gray · wide"),
        ("scene04", "S04  night · gray · zoom"),
        ("scene05", "S05  night · pseudocolor"),
        ("scene10", "S10  day · pseudocolor"),
        ("scene13", "S13  low-light · pseudocolor"),
        ("scene14", "S14  low-light · tower"),
    ]
    for idx, (scene, title) in enumerate(examples):
        row, col = divmod(idx, 2)
        sub = GridSpecFromSubplotSpec(
            2,
            2,
            subplot_spec=outer[row, col + 1],
            height_ratios=[0.15, 0.85],
            hspace=0.02,
            wspace=0.03,
        )
        label_ax = fig.add_subplot(sub[0, :])
        label_ax.axis("off")
        label_ax.text(0.5, 0.45, title, ha="center", va="center", fontsize=6.5, fontweight="semibold")
        rgb_ax = fig.add_subplot(sub[1, 0])
        ir_ax = fig.add_subplot(sub[1, 1])
        image_panel(rgb_ax, find(scene, "rgb_selected_crop"), "RGB" if idx == 0 else None)
        image_panel(ir_ax, find(scene, "infrared_selected_crop"), "Infrared" if idx == 0 else None)
        if idx == 0:
            panel_label(label_ax, "b", x=-0.05, y=1.0)

    save_bundle(fig, ROOT / "outputs", "fig01_problem_benchmark")
    plt.close(fig)


if __name__ == "__main__":
    main()
