from __future__ import annotations

from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Rectangle
from PIL import Image


COLORS = {
    "ink": "#1F2933",
    "muted": "#66737F",
    "grid": "#D9E0E6",
    "panel": "#F5F7F8",
    "visible": "#2F6B9A",
    "visible_light": "#D9EAF4",
    "infrared": "#D77A2B",
    "infrared_light": "#F8E5D1",
    "confidence": "#2F8F6B",
    "confidence_light": "#D9EEE6",
    "filtered": "#8A949C",
    "filtered_light": "#E8ECEF",
    "canonical": "#A83A3A",
    "accent": "#D4A72C",
    "purple": "#6F5A8A",
}


def configure_style() -> None:
    mpl.rcParams.update(
        {
            "font.family": "sans-serif",
            "font.sans-serif": ["Arial", "Helvetica", "DejaVu Sans", "sans-serif"],
            "font.size": 7.0,
            "axes.titlesize": 8.0,
            "axes.labelsize": 7.0,
            "xtick.labelsize": 6.4,
            "ytick.labelsize": 6.4,
            "legend.fontsize": 6.4,
            "axes.edgecolor": COLORS["ink"],
            "axes.labelcolor": COLORS["ink"],
            "xtick.color": COLORS["ink"],
            "ytick.color": COLORS["ink"],
            "text.color": COLORS["ink"],
            "axes.spines.right": False,
            "axes.spines.top": False,
            "axes.linewidth": 0.7,
            "svg.fonttype": "none",
            "pdf.fonttype": 42,
            "savefig.facecolor": "white",
            "figure.facecolor": "white",
        }
    )


def mm(value: float) -> float:
    return value / 25.4


def save_bundle(fig: plt.Figure, output_dir: Path, stem: str) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_dir / f"{stem}.svg", bbox_inches="tight", pad_inches=0.03)
    fig.savefig(output_dir / f"{stem}.pdf", bbox_inches="tight", pad_inches=0.03)
    fig.savefig(
        output_dir / f"{stem}.png",
        dpi=300,
        bbox_inches="tight",
        pad_inches=0.03,
    )


def panel_label(ax, label: str, x: float = -0.04, y: float = 1.04) -> None:
    ax.text(
        x,
        y,
        label,
        transform=ax.transAxes,
        fontsize=8.5,
        fontweight="bold",
        va="bottom",
        ha="left",
        color=COLORS["ink"],
        clip_on=False,
    )


def image_panel(ax, path: Path, title: str | None = None) -> None:
    image = Image.open(path).convert("RGB")
    ax.imshow(image)
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(True)
        spine.set_linewidth(0.45)
        spine.set_edgecolor("#C8D0D6")
    if title:
        ax.set_title(title, pad=2.0, fontsize=6.6, fontweight="semibold")


def placeholder(ax, title: str, note: str) -> None:
    ax.set_facecolor("white")
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    for spine in ax.spines.values():
        spine.set_visible(False)
    rect = Rectangle(
        (0.03, 0.06),
        0.94,
        0.86,
        facecolor="#FAFBFC",
        edgecolor=COLORS["filtered"],
        linewidth=1.0,
        linestyle=(0, (4, 3)),
    )
    ax.add_patch(rect)
    ax.text(0.5, 0.58, title, ha="center", va="center", fontweight="bold")
    ax.text(
        0.5,
        0.39,
        note,
        ha="center",
        va="center",
        fontsize=6.2,
        color=COLORS["muted"],
        wrap=True,
    )


def rounded_box(
    ax,
    xy: tuple[float, float],
    width: float,
    height: float,
    text: str,
    facecolor: str,
    edgecolor: str,
    fontsize: float = 6.8,
    fontweight: str = "semibold",
    radius: float = 0.025,
) -> FancyBboxPatch:
    box = FancyBboxPatch(
        xy,
        width,
        height,
        boxstyle=f"round,pad=0.012,rounding_size={radius}",
        facecolor=facecolor,
        edgecolor=edgecolor,
        linewidth=0.8,
    )
    ax.add_patch(box)
    ax.text(
        xy[0] + width / 2,
        xy[1] + height / 2,
        text,
        ha="center",
        va="center",
        fontsize=fontsize,
        fontweight=fontweight,
        color=COLORS["ink"],
    )
    return box


def arrow(
    ax,
    start: tuple[float, float],
    end: tuple[float, float],
    color: str | None = None,
    connectionstyle: str = "arc3",
) -> None:
    ax.add_patch(
        FancyArrowPatch(
            start,
            end,
            arrowstyle="-|>",
            mutation_scale=8,
            linewidth=0.9,
            color=color or COLORS["muted"],
            connectionstyle=connectionstyle,
        )
    )


def soften_axes(ax, grid_axis: str = "y") -> None:
    ax.grid(axis=grid_axis, color=COLORS["grid"], linewidth=0.55, alpha=0.85)
    ax.set_axisbelow(True)

