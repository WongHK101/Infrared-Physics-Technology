from pathlib import Path
import sys
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "_shared"))
from figure_style import COLORS, save_bundle, soften_axes
from compact_chart_style import configure

ROOT = Path(__file__).resolve().parent


def main():
    configure()
    curve = pd.read_csv(ROOT / "source_data/risk_coverage.csv")
    canonical = pd.read_csv(ROOT / "source_data/canonical_operating_point.csv").iloc[0]
    fig, axes = plt.subplots(1, 2, figsize=(7.2, 2.85))
    fig.subplots_adjust(left=.09, right=.98, bottom=.23, top=.88, wspace=.38)
    ax = axes[0]
    ax.plot(curve.scene_coverage, curve.mean_severe_outlier_ratio,
            "o-", color=COLORS["visible"], lw=1.5, ms=4, label="Score-ranked set")
    ax.scatter(canonical.scene_coverage, canonical.mean_severe_outlier_ratio,
               marker="*", s=150, color=COLORS["canonical"], zorder=5, label="Canonical gate")
    for count, name, offset in [(3, "Conservative", (0, 11)), (8, "Balanced", (-26, 34)),
                                (13, "Permissive", (-48, 10)), (15, "Inclusive", (-39, 10))]:
        row = curve.loc[curve.retained_scene_count == count].iloc[0]
        ax.annotate(name, (row.scene_coverage, row.mean_severe_outlier_ratio),
                    xytext=offset, textcoords="offset points", fontsize=8)
    ax.set(xlabel="Scene coverage", ylabel="Mean severe-outlier ratio", xlim=(0, 1.05),
           ylim=(-.003, .075), title="(a) Reliability and coverage")
    ax.legend(loc="upper left", frameon=False)
    ax = axes[1]
    ax.plot(curve.pair_coverage_micro, curve.accepted_attempted_ratio_micro,
            "s-", color=COLORS["infrared"], lw=1.5, ms=4)
    ax.scatter(canonical.pair_coverage_micro, canonical.accepted_attempted_ratio_micro,
               marker="*", s=150, color=COLORS["canonical"], zorder=5)
    ax.annotate("Canonical: 74.4% pairs\n64.7% accepted support",
                (canonical.pair_coverage_micro, canonical.accepted_attempted_ratio_micro),
                xytext=(.27, .25), textcoords="axes fraction", fontsize=9,
                color=COLORS["canonical"],
                arrowprops={"arrowstyle": "-", "color": COLORS["canonical"], "lw": .8})
    ax.set(xlabel="Pair coverage", ylabel="Accepted / attempted frames", xlim=(0, 1.05),
           ylim=(0, 1.05), title="(b) Evidence support")
    for ax in axes:
        ax.xaxis.set_major_formatter(PercentFormatter(1))
        ax.yaxis.set_major_formatter(PercentFormatter(1))
        soften_axes(ax)
    save_bundle(fig, ROOT / "outputs", "fig08_operating_profile")
    plt.close(fig)


if __name__ == "__main__":
    main()
