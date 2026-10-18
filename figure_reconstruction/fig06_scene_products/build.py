from pathlib import Path
import json
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "_shared"))
from editable_diagram import overlay_gallery

ROOT = Path(__file__).resolve().parent


def main():
    manifest = json.loads((ROOT / "source_assets/asset_manifest.json").read_text("utf-8"))
    ids = {f"scene{r['scene_id']}": r["pair_id"] for r in manifest}
    rows = [
        ("scene10", "Day / pseudocolor"),
        ("scene04", "Night / grayscale / zoom"),
        ("scene14", "Low-light / pseudocolor"),
    ]
    overlay_gallery(ROOT, "fig06_scene_products", [
        (s, f"S{s[-2:]} / {ids[s]}   {label}   |   Canonically retained", True)
        for s, label in rows
    ])
    overlay_gallery(ROOT, "fig06_additional_product", [
        ("scene07", f"S07 / {ids['scene07']}   Day / grayscale / tower   |   Canonically retained", True),
    ])


if __name__ == "__main__":
    main()
