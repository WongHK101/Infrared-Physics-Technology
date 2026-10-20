from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np
from PIL import Image
from skimage import color, feature, morphology, transform

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "_shared"))
ROOT = Path(__file__).resolve().parent
DATA = ROOT / "source_data"
ASSETS = ROOT / "source_assets"


def edge_overlay(rgb_path: Path, ir_path: Path, matrix: list[list[float]]) -> np.ndarray:
    rgb = np.asarray(Image.open(rgb_path).convert("RGB")) / 255.0
    ir = np.asarray(Image.open(ir_path).convert("RGB")) / 255.0
    target_scale = min(1.0, 1800.0 / max(rgb.shape[:2]))
    out_shape = (max(1, int(rgb.shape[0] * target_scale)), max(1, int(rgb.shape[1] * target_scale)))
    rgb_small = transform.resize(rgb, (*out_shape, 3), preserve_range=True, anti_aliasing=True)
    scale = np.array([[target_scale, 0, 0], [0, target_scale, 0], [0, 0, 1]], float)
    h_scaled = scale @ np.asarray(matrix, float)
    tform = transform.ProjectiveTransform(matrix=h_scaled)
    warped = transform.warp(ir, inverse_map=tform.inverse, output_shape=out_shape, preserve_range=True)
    rgb_edge = feature.canny(color.rgb2gray(rgb_small), sigma=1.25)
    ir_edge = feature.canny(color.rgb2gray(warped), sigma=1.10)
    rgb_edge = morphology.binary_dilation(rgb_edge, morphology.disk(2))
    ir_edge = morphology.binary_dilation(ir_edge, morphology.disk(2))
    both = rgb_edge & ir_edge
    gray = color.rgb2gray(rgb_small)
    canvas = np.repeat((0.05 + 0.28 * gray)[..., None], 3, axis=2)
    canvas[rgb_edge] = np.array([0.00, 0.82, 0.96])
    canvas[ir_edge] = np.array([0.98, 0.22, 0.16])
    canvas[both] = np.array([1.00, 0.96, 0.62])
    return canvas


def main() -> None:
    from editable_diagram import Diagram
    selected = json.loads((DATA / "selected_pair_homographies.json").read_text(encoding="utf-8"))
    methods = ["SIFT", "RIFT2", "LoFTR", "XoFTR", "RoMa", "raw MINIMA"]
    d = Diagram(1200, 685)
    tiles = ROOT / "outputs" / "tiles"
    tiles.mkdir(parents=True, exist_ok=True)
    for i, method in enumerate(methods):
        overlay = edge_overlay(
            ASSETS / "scene04_pair000020_rgb.jpg",
            ASSETS / "scene04_pair000020_infrared.jpg",
            selected["methods"][method],
        )
        tile = tiles / f"{method.replace(' ', '_')}_edges.png"
        Image.fromarray((overlay.clip(0, 1)*255).astype(np.uint8)).save(tile)
        x, y = 8 + (i % 3)*402, 10 + (i // 3)*315
        d.text(x, y, 388, 35, method, size=28, bold=True)
        d.photo(x, y+40, 388, 265, tile)
    for x, label, color in [(225, "RGB", "#00D1F5"),
                             (485, "Infrared", "#FA3829"),
                             (795, "Overlap", "#FFF59E")]:
        d.box(x, 649, 24, 18, fill=color, stroke="#67737C", rounded=False)
        d.text(x+35, 641, 180, 34, label, size=24, align="left")
    d.export(ROOT, "fig05_pairwise_evidence")


if __name__ == "__main__":
    main()
