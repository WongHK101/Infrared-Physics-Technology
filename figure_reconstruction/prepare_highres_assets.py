"""Prepare verified high-resolution qualitative assets for manuscript figures.

The dataset and frozen experiment record are read-only inputs. This script only
writes to figure-local ``source_assets`` directories.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
from PIL import Image, ImageOps
from skimage import color, feature, morphology, transform


ROOT = Path(__file__).resolve().parent
ASPECT = 10.0 / 7.0
MAX_RGB_WIDTH = 2800

FIGURE_CASES = {
    "fig01_problem_benchmark": [
        ("01", "000009"),
        ("04", "000020"),
        ("05", "000650"),
        ("07", "000050"),
        ("10", "000100"),
        ("13", "000200"),
        ("14", "000300"),
    ],
    "fig03_scene_framework": [("02", "000009")],
    "fig06_scene_products": [
        ("04", "000020"),
        ("07", "000050"),
        ("10", "000100"),
        ("14", "000300"),
    ],
    "fig07_reliability_selection": [
        ("01", "000009"),
        ("02", "000009"),
        ("03", "000020"),
        ("04", "000020"),
    ],
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset-root", type=Path, required=True)
    parser.add_argument("--scene-results", type=Path, required=True)
    return parser.parse_args()


def load_scene_records(path: Path) -> dict[str, dict]:
    records: dict[str, dict] = {}
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            if line.strip():
                record = json.loads(line)
                records[str(record["scene_id"]).zfill(2)] = record
    return records


def find_scene(dataset_root: Path, scene_id: str) -> Path:
    matches = sorted(dataset_root.glob(f"{scene_id}_*"))
    if len(matches) != 1:
        raise FileNotFoundError(
            f"Expected one dataset scene for {scene_id}, found {len(matches)}"
        )
    return matches[0]


def crop_to_aspect(image: np.ndarray, aspect: float = ASPECT) -> np.ndarray:
    height, width = image.shape[:2]
    current = width / height
    if current > aspect:
        crop_width = round(height * aspect)
        x0 = (width - crop_width) // 2
        return image[:, x0 : x0 + crop_width]
    crop_height = round(width / aspect)
    y0 = (height - crop_height) // 2
    return image[y0 : y0 + crop_height, :]


def resize_rgb_working(image: np.ndarray) -> tuple[np.ndarray, float]:
    height, width = image.shape[:2]
    scale = min(1.0, MAX_RGB_WIDTH / float(width))
    if scale == 1.0:
        return image, scale
    resized = Image.fromarray(image).resize(
        (round(width * scale), round(height * scale)), Image.Resampling.LANCZOS
    )
    return np.asarray(resized), scale


def thermal_display(image: np.ndarray, rendering: str) -> np.ndarray:
    if rendering == "grayscale":
        gray = ImageOps.autocontrast(Image.fromarray(image).convert("L"))
        return np.asarray(gray.convert("RGB"))
    return image


def red_cyan_overlay(rgb: np.ndarray, thermal: np.ndarray) -> np.ndarray:
    rgb_gray = (255 * color.rgb2gray(rgb)).astype(np.uint8)
    thermal_gray = (255 * color.rgb2gray(thermal)).astype(np.uint8)
    # RGB composition: infrared evidence is red; RGB evidence is cyan.
    return np.stack((thermal_gray, rgb_gray, rgb_gray), axis=2)


def high_contrast_edge_overlay(rgb: np.ndarray, thermal: np.ndarray) -> np.ndarray:
    rgb_gray = color.rgb2gray(rgb)
    thermal_gray = color.rgb2gray(thermal)
    rgb_edge = feature.canny(rgb_gray, sigma=1.15)
    thermal_edge = feature.canny(thermal_gray, sigma=1.05)
    rgb_edge = morphology.binary_dilation(rgb_edge, morphology.disk(2))
    thermal_edge = morphology.binary_dilation(thermal_edge, morphology.disk(2))
    agreement = rgb_edge & thermal_edge

    background_gray = np.clip(rgb_gray * 0.28 + 0.055, 0, 1)
    background = np.repeat(background_gray[..., None], 3, axis=2)
    background[rgb_edge] = (0.08, 0.84, 0.94)
    background[thermal_edge] = (0.96, 0.18, 0.14)
    background[agreement] = (1.0, 0.96, 0.62)
    return (255 * background).astype(np.uint8)


def save_jpeg(path: Path, image: np.ndarray) -> tuple[int, int]:
    path.parent.mkdir(parents=True, exist_ok=True)
    Image.fromarray(image).save(path, quality=96, subsampling=0, optimize=True)
    return image.shape[1], image.shape[0]


def prepare_case(
    dataset_root: Path,
    record: dict,
    pair_id: str,
    output_dir: Path,
) -> dict:
    scene_id = str(record["scene_id"]).zfill(2)
    scene_dir = find_scene(dataset_root, scene_id)
    rgb_path = scene_dir / "rgb" / f"{pair_id}.jpg"
    thermal_path = scene_dir / "thermal" / f"{pair_id}.jpg"
    rgb_original = np.asarray(Image.open(rgb_path).convert("RGB"))
    thermal_original = np.asarray(Image.open(thermal_path).convert("RGB"))

    rgb_working, scale = resize_rgb_working(rgb_original)
    rendering = str(record.get("thermal_rendering", "grayscale"))
    thermal_visible = thermal_display(thermal_original, rendering)
    h_thermal_to_rgb = np.asarray(record["homography"], dtype=np.float64)
    scaled_h = np.diag([scale, scale, 1.0]) @ h_thermal_to_rgb

    target_size = (rgb_working.shape[1], rgb_working.shape[0])
    output_shape = (target_size[1], target_size[0])
    thermal_resized = transform.resize(
        thermal_visible,
        (*output_shape, 3),
        preserve_range=True,
        anti_aliasing=True,
    ).astype(np.uint8)
    projective = transform.ProjectiveTransform(matrix=scaled_h)
    thermal_warped = transform.warp(
        thermal_visible,
        inverse_map=projective.inverse,
        output_shape=output_shape,
        preserve_range=True,
    ).astype(np.uint8)

    assets = {
        "rgb_selected_crop": crop_to_aspect(rgb_working),
        "infrared_selected_crop": crop_to_aspect(thermal_visible),
        "before_resize_overlay_crop": crop_to_aspect(
            red_cyan_overlay(rgb_working, thermal_resized)
        ),
        "after_scene_homography_overlay_crop": crop_to_aspect(
            red_cyan_overlay(rgb_working, thermal_warped)
        ),
        "edge_overlay_crop": crop_to_aspect(
            high_contrast_edge_overlay(rgb_working, thermal_warped)
        ),
    }
    prefix = f"scene{scene_id}_pair{pair_id}"
    dimensions = {}
    for suffix, image in assets.items():
        dimensions[suffix] = save_jpeg(output_dir / f"{prefix}_{suffix}.jpg", image)

    return {
        "scene_id": scene_id,
        "scene_name": scene_dir.name,
        "pair_id": pair_id,
        "rgb_source": f"{scene_dir.name}/rgb/{pair_id}.jpg",
        "infrared_source": f"{scene_dir.name}/thermal/{pair_id}.jpg",
        "rgb_original_size": [rgb_original.shape[1], rgb_original.shape[0]],
        "infrared_original_size": [
            thermal_original.shape[1],
            thermal_original.shape[0],
        ],
        "working_scale": scale,
        "asset_dimensions": dimensions,
        "canonical_scene_pass": bool(record.get("canonical_scene_pass")),
        "qa_status": record.get("qa_status"),
    }


def main() -> None:
    args = parse_args()
    dataset_root = args.dataset_root.resolve()
    scene_results = args.scene_results.resolve()
    if not dataset_root.is_dir() or not scene_results.is_file():
        raise FileNotFoundError("Dataset root or frozen scene-result file is missing")

    records = load_scene_records(scene_results)
    for figure_name, cases in FIGURE_CASES.items():
        output_dir = (ROOT / figure_name / "source_assets").resolve()
        if ROOT.resolve() not in output_dir.parents:
            raise RuntimeError(f"Unsafe output directory: {output_dir}")
        output_dir.mkdir(parents=True, exist_ok=True)
        for stale in output_dir.glob("scene*_*.jpg"):
            stale.unlink()
        manifest = [
            prepare_case(dataset_root, records[scene_id], pair_id, output_dir)
            for scene_id, pair_id in cases
        ]
        (output_dir / "asset_manifest.json").write_text(
            json.dumps(manifest, indent=2), encoding="utf-8"
        )
        print(f"[assets] {figure_name}: {len(manifest)} verified cases")


if __name__ == "__main__":
    main()
