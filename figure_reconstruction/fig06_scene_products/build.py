from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "_shared"))
from editable_diagram import overlay_gallery

ROOT = Path(__file__).resolve().parent


def main():
    rows = [
        ("scene10", "Day / pseudocolor"),
        ("scene04", "Night / grayscale / zoom"),
        ("scene14", "Low-light / pseudocolor"),
    ]
    overlay_gallery(ROOT, "fig06_scene_products", [
        (s, f"S{s[-2:]}   {label}", True)
        for s, label in rows
    ])
    overlay_gallery(ROOT, "fig06_additional_product", [
        ("scene07", "S07   Tower orbit", True),
    ])


if __name__ == "__main__":
    main()
