from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
from PIL import Image


ROOT = Path(__file__).resolve().parent
FIGURES = [
    ("fig01_problem_benchmark", "Fig. 1  Problem + benchmark"),
    ("fig02_benchmark_protocol", "Fig. 2  Benchmark protocol"),
    ("fig03_scene_framework", "Fig. 3  Scene framework"),
    ("fig04_consensus_qa", "Fig. 4  Consensus + QA"),
    ("fig05_pairwise_evidence", "Fig. 5  Pairwise evidence"),
    ("fig06_scene_products", "Fig. 6  Scene products"),
    ("fig07_reliability_selection", "Fig. 7  Reliability selection"),
    ("fig08_operating_profile", "Fig. 8  Operating profile"),
    ("fig09_validation_attribution", "Fig. 9  Validation + attribution"),
]


def main() -> None:
    fig, axes = plt.subplots(3, 3, figsize=(16, 10), facecolor="#E8ECEF")
    for ax, (folder, title) in zip(axes.flat, FIGURES):
        path = ROOT / folder / "outputs" / f"{folder.replace('fig0', 'fig0')}.png"
        if not path.exists():
            candidates = list((ROOT / folder / "outputs").glob("*.png"))
            if not candidates:
                raise FileNotFoundError(folder)
            path = candidates[0]
        image = Image.open(path).convert("RGB")
        ax.imshow(image)
        ax.set_title(title, fontsize=11, fontweight="bold", pad=6)
        ax.axis("off")
    fig.tight_layout(pad=1.25)
    fig.savefig(ROOT / "figure_contact_sheet.png", dpi=180, bbox_inches="tight", facecolor=fig.get_facecolor())
    plt.close(fig)


if __name__ == "__main__":
    main()

