from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "_shared"))
from figure_style import (  # noqa: E402
    COLORS,
    arrow,
    configure_style,
    image_panel,
    mm,
    panel_label,
    rounded_box,
    save_bundle,
)


ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / "source_assets"


def only(pattern: str) -> Path:
    matches = list(ASSETS.glob(pattern))
    if len(matches) != 1:
        raise FileNotFoundError(f"Expected one asset for {pattern}, found {len(matches)}")
    return matches[0]


def stage_box(
    ax,
    x: float,
    title: str,
    symbol: str,
    detail: str,
    facecolor: str,
    edgecolor: str,
) -> None:
    rounded_box(ax, (x, 0.55), 0.132, 0.31, "", facecolor, edgecolor)
    ax.text(
        x + 0.066,
        0.795,
        title,
        ha="center",
        va="center",
        fontsize=6.3,
        fontweight="bold",
    )
    ax.text(
        x + 0.066,
        0.705,
        symbol,
        ha="center",
        va="center",
        fontsize=7.2,
        fontweight="semibold",
        color=edgecolor,
    )
    ax.text(
        x + 0.066,
        0.615,
        detail,
        ha="center",
        va="center",
        fontsize=5.55,
        color=COLORS["muted"],
        linespacing=1.2,
    )


def main() -> None:
    configure_style()
    fig = plt.figure(figsize=(mm(183), mm(103)))
    ax = fig.add_axes([0.018, 0.055, 0.965, 0.90])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    panel_label(ax, "a", x=-0.008, y=1.01)

    ax.text(
        0.004,
        0.965,
        "Synchronized UAV scene evidence",
        ha="left",
        va="center",
        fontsize=7.0,
        fontweight="bold",
    )
    rgb_ax = ax.inset_axes([0.002, 0.705, 0.105, 0.135])
    ir_ax = ax.inset_axes([0.002, 0.535, 0.105, 0.135])
    image_panel(rgb_ax, only("*rgb_selected_crop.jpg"), "RGB")
    image_panel(ir_ax, only("*infrared_selected_crop.jpg"), "Infrared")
    ax.text(
        0.054,
        0.495,
        r"$S=\{(I_i^R,I_i^T)\}_{i=1}^{N}$",
        ha="center",
        va="center",
        fontsize=6.2,
        color=COLORS["muted"],
    )

    stages = [
        (
            0.145,
            "Pairwise evidence",
            r"$H_i$",
            "MINIMA--RoMa\nmatches + geometry",
            COLORS["visible_light"],
            COLORS["visible"],
        ),
        (
            0.305,
            "Progressive schedule",
            r"$12\!\rightarrow\!24\!\rightarrow\!\cdots$",
            "even coverage\nadaptive expansion",
            "#EEF1F6",
            COLORS["purple"],
        ),
        (
            0.465,
            "Frame reliability",
            r"$q_i$",
            "inlier + coverage\nresidual + support",
            "#F2F5F7",
            COLORS["muted"],
        ),
        (
            0.625,
            "Robust consensus",
            r"$\bar{H}_{S}$",
            "median / MAD filter\nquality weighting",
            COLORS["confidence_light"],
            COLORS["confidence"],
        ),
        (
            0.785,
            "Cross-modal QA",
            r"$\Delta E,\Delta G,O_S,J_S$",
            "edge + gradient\nstability + outliers",
            COLORS["infrared_light"],
            COLORS["infrared"],
        ),
    ]
    for stage in stages:
        stage_box(ax, *stage)
    arrow(ax, (0.108, 0.705), (0.143, 0.705))
    for start in [0.277, 0.437, 0.597, 0.757]:
        arrow(ax, (start, 0.705), (start + 0.026, 0.705))

    panel_label(ax, "b", x=-0.008, y=0.43)
    ax.text(
        0.004,
        0.405,
        "Evidence consolidation and product decision",
        ha="left",
        va="center",
        fontsize=7.0,
        fontweight="bold",
    )
    ax.add_patch(
        Rectangle(
            (0.145, 0.105),
            0.42,
            0.29,
            facecolor="#FAFBFC",
            edgecolor=COLORS["grid"],
            linewidth=0.8,
        )
    )
    ax.text(0.164, 0.355, "Frame hypotheses", fontsize=6.3, fontweight="bold")
    hypothesis_x = [0.19, 0.26, 0.33, 0.40, 0.47, 0.53]
    for i, x in enumerate(hypothesis_x):
        accepted = i not in {3}
        ax.add_patch(
            Circle(
                (x, 0.265),
                0.022,
                facecolor=COLORS["confidence_light"] if accepted else "white",
                edgecolor=COLORS["confidence"] if accepted else COLORS["canonical"],
                linewidth=1.0,
            )
        )
        ax.text(
            x,
            0.265,
            rf"$H_{{{i+1}}}$" if accepted else r"$\times$",
            ha="center",
            va="center",
            fontsize=5.7,
            color=COLORS["ink"] if accepted else COLORS["canonical"],
        )
    ax.plot([0.19, 0.53], [0.19, 0.19], color=COLORS["grid"], linewidth=1.0)
    ax.text(
        0.36,
        0.145,
        r"$\mathcal{C}_{S}:\ d_i\leq \mathrm{median}(d)+2.5\,\mathrm{MAD}(d)$",
        ha="center",
        va="center",
        fontsize=6.0,
        color=COLORS["muted"],
    )

    rounded_box(
        ax,
        (0.61, 0.245),
        0.20,
        0.145,
        "Canonical gate\n$y_S$",
        COLORS["confidence_light"],
        COLORS["confidence"],
        fontsize=6.5,
    )
    rounded_box(
        ax,
        (0.61, 0.075),
        0.20,
        0.125,
        "Reliability ordering\n$R(S)$",
        COLORS["filtered_light"],
        COLORS["filtered"],
        fontsize=6.4,
    )
    arrow(ax, (0.565, 0.265), (0.608, 0.315), color=COLORS["confidence"])
    arrow(ax, (0.565, 0.205), (0.608, 0.137), color=COLORS["filtered"])
    ax.text(
        0.71,
        0.222,
        "fixed product decision",
        ha="center",
        va="center",
        fontsize=5.5,
        color=COLORS["confidence"],
    )
    ax.text(
        0.71,
        0.050,
        "coverage-aware operating profile",
        ha="center",
        va="center",
        fontsize=5.5,
        color=COLORS["filtered"],
    )

    product_ax = ax.inset_axes([0.855, 0.145, 0.14, 0.225])
    image_panel(
        product_ax,
        only("*after_scene_homography_overlay_crop.jpg"),
        "High-confidence scene product",
    )
    arrow(ax, (0.812, 0.315), (0.852, 0.265), color=COLORS["confidence"])
    ax.text(
        0.922,
        0.095,
        r"$y_S$ defines products; $R(S)$ ranks operating points",
        ha="center",
        va="center",
        fontsize=5.5,
        color=COLORS["muted"],
    )

    save_bundle(fig, ROOT / "outputs", "fig03_scene_framework")
    plt.close(fig)


if __name__ == "__main__":
    main()
