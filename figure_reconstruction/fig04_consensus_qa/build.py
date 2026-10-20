from pathlib import Path
import json
import sys

import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "_shared"))
from compact_chart_style import configure
from figure_style import COLORS, save_bundle, soften_axes

ROOT = Path(__file__).resolve().parent


def main():
    configure()
    fig, (ax, bx) = plt.subplots(1, 2, figsize=(7.2, 3.5))
    fig.subplots_adjust(left=.09, right=.98, bottom=.19, top=.74, wspace=.38)
    series = [
        ("01", COLORS["confidence"], "o", -.10, "S01 retained"),
        ("02", COLORS["filtered"], "s", .10, "S02 QA-filtered"),
    ]
    for scene, color, marker, offset, label in series:
        result = json.loads((ROOT / f"source_data/scene{scene}_result.json").read_text("utf-8"))
        b = result["band_payload"]
        rows = b["homography_stability"]["per_homography"]
        dist = np.array([r["param_distance_to_median"] for r in rows])
        keep = np.array([r["robust_keep"] for r in rows])
        x = np.arange(1, len(rows)+1) + offset
        ax.scatter(x[keep], dist[keep], s=28, marker=marker, c=color, label=label,
                   edgecolor="white", linewidth=.4, zorder=3)
        ax.scatter(x[~keep], dist[~keep], s=30, marker="x", c=COLORS["canonical"], zorder=4)
        frames = b["per_frame"]
        edge = np.array([f["delta_edge_f1"] for f in frames])
        grad = np.array([f["delta_grad_ncc"] for f in frames])
        severe = np.array([f.get("severe_misalignment", False) for f in frames])
        bx.scatter(edge[~severe], grad[~severe], s=34, marker=marker, c=color,
                   edgecolor="white", linewidth=.4, label=label)
        bx.scatter(edge[severe], grad[severe], s=64, marker="X", facecolor="white",
                   edgecolor=COLORS["canonical"], linewidth=1.2)
    ax.set(yscale="symlog", xlabel="Accepted hypothesis index",
           ylabel="Parameter distance to median")
    ax.set_title("(a) Robust hypothesis support", loc="left")
    bx.set(xlabel="Change in edge F1", ylabel="Change in gradient NCC")
    bx.set_title("(b) Cross-modal QA response", loc="left")
    bx.axhline(0, c=COLORS["grid"], lw=.8)
    bx.axvline(0, c=COLORS["grid"], lw=.8)
    handles, labels = bx.get_legend_handles_labels()
    handles.append(Line2D([], [], color=COLORS["canonical"], marker="x", ls="none"))
    handles.append(Line2D([], [], color=COLORS["canonical"], marker="X", ls="none",
                          markerfacecolor="white"))
    fig.legend(handles, labels+["Robust rejection", "Severe relative outlier"],
               loc="upper center", ncol=2, bbox_to_anchor=(.54, 1.0))
    for a in (ax, bx):
        soften_axes(a)
    save_bundle(fig, ROOT / "outputs", "fig04_consensus_qa")
    plt.close(fig)


if __name__ == "__main__":
    main()
