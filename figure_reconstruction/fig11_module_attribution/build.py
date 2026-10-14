from pathlib import Path
import sys
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "_shared"))
from figure_style import COLORS, save_bundle, soften_axes
from compact_chart_style import configure

ROOT = Path(__file__).resolve().parent


def main():
    configure()
    ablation = pd.read_csv(ROOT / "source_data/ablation_proxy_summary.csv")
    seeds = pd.read_csv(ROOT / "source_data/multiseed_summary.csv")
    fig, axes = plt.subplots(1, 2, figsize=(7.2, 2.85))
    fig.subplots_adjust(left=.09, right=.98, bottom=.25, top=.87, wspace=.36)
    ax = axes[0]
    x = np.arange(len(ablation))
    ax.plot(x, ablation.mean_delta_edge_f1, "o-", color=COLORS["visible"], lw=1.6, label="Edge-F1 gain")
    ax.plot(x, ablation.mean_delta_grad_ncc, "s-", color=COLORS["infrared"], lw=1.6, label="Gradient-NCC gain")
    ax.set_xticks(x, ["Pairwise\nevidence", "+ Robust\nconsensus", "+ QA\nverification"])
    ax.set(xlim=(-.15, 2.15), ylim=(0, .18), ylabel="Mean improvement", title="(a) Cumulative modules")
    ax.legend(loc="lower right", frameon=False)
    ax = axes[1]
    ax.vlines(seeds.seed, 0, seeds.canonical_pass_count, color=COLORS["grid"], lw=3)
    ax.scatter(seeds.seed, seeds.canonical_pass_count, color=COLORS["visible"], s=44, zorder=3)
    ax.axhline(5, ls="--", color=COLORS["canonical"], lw=1.2, label="Deterministic-even: 5/8")
    for seed, count in zip(seeds.seed, seeds.canonical_pass_count):
        ax.annotate(f"{count}/8", (seed, count), xytext=(0, 7), textcoords="offset points",
                    ha="center", fontsize=10)
    ax.set_xticks(seeds.seed)
    ax.set(xlim=(-.4, 3.4), ylim=(0, 8.6), xlabel="Random-selection seed",
           ylabel="Retained scenes (out of 8)", title="(b) Selection sensitivity")
    ax.legend(loc="lower center", frameon=False)
    for ax in axes:
        soften_axes(ax)
    save_bundle(fig, ROOT / "outputs", "fig11_module_attribution")
    plt.close(fig)


if __name__ == "__main__":
    main()
