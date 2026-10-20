from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "_shared"))
from editable_diagram import Diagram, find_asset

ROOT = Path(__file__).resolve().parent


def main():
    d = Diagram(1200, 830)
    scenes = [
        ("scene01", "S01  Day / grayscale / wide"),
        ("scene04", "S04  Night / grayscale / zoom"),
        ("scene05", "S05  Night / pseudocolor"),
        ("scene10", "S10  Day / pseudocolor"),
        ("scene13", "S13  Low-light / pseudocolor"),
        ("scene14", "S14  Low-light / pseudocolor"),
    ]
    for i, (scene, label) in enumerate(scenes):
        x, y = 8 + (i % 2) * 604, (i // 2) * 280
        d.box(x, y, 580, 34, fill="#EDF1F6", stroke="none")
        d.text(x, y, 580, 34, label, size=25, bold=True)
        for j, (suffix, name) in enumerate([
            ("rgb_selected_crop", "RGB"),
            ("infrared_selected_crop", "Infrared"),
        ]):
            d.text(x + j * 294, y + 36, 286, 26, name, size=23)
            d.photo(x + j * 294, y + 66, 286, 200.2,
                    find_asset(ROOT / "source_assets", scene, suffix))
    d.export(ROOT, "fig01_problem_benchmark")


if __name__ == "__main__":
    main()
