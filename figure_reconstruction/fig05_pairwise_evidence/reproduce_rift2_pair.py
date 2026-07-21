"""Reproduce one RIFT2 homography for the qualitative comparison panel."""

from __future__ import annotations

import argparse
import json
import pathlib
import sys
import time

import cv2
import numpy as np


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--rift2-repo", type=pathlib.Path, required=True)
    parser.add_argument("--rgb", type=pathlib.Path, required=True)
    parser.add_argument("--infrared", type=pathlib.Path, required=True)
    parser.add_argument("--output", type=pathlib.Path, required=True)
    parser.add_argument("--max-dim", type=int, default=1200)
    parser.add_argument("--npt", type=int, default=2000)
    parser.add_argument("--patch-size", type=int, default=64)
    parser.add_argument("--lowes-ratio", type=float, default=0.95)
    parser.add_argument("--reproj-threshold", type=float, default=5.0)
    return parser.parse_args()


def resize_max(image: np.ndarray, max_dim: int) -> tuple[np.ndarray, float]:
    height, width = image.shape[:2]
    scale = min(1.0, float(max_dim) / float(max(height, width)))
    if scale < 1.0:
        image = cv2.resize(
            image,
            (round(width * scale), round(height * scale)),
            interpolation=cv2.INTER_AREA,
        )
    return image, scale


def normalized(matrix: np.ndarray) -> np.ndarray:
    return matrix / matrix[2, 2]


def main() -> None:
    args = parse_args()
    if args.output.exists():
        raise FileExistsError(f"Refusing to overwrite existing output: {args.output}")
    if not args.rgb.is_file() or not args.infrared.is_file():
        raise FileNotFoundError("RGB or infrared source image is missing")

    sys.path.insert(0, str(args.rift2_repo))
    from src.RIFT2 import RIFT2  # pylint: disable=import-outside-toplevel
    from src.matcher_functions import (  # pylint: disable=import-outside-toplevel
        match_keypoints_nn,
    )

    cv2.setRNGSeed(0)
    np.random.seed(0)
    rgb_original = cv2.imread(str(args.rgb), cv2.IMREAD_COLOR)
    infrared_original = cv2.imread(str(args.infrared), cv2.IMREAD_COLOR)
    if rgb_original is None or infrared_original is None:
        raise RuntimeError("decode_failed")

    rgb, scale_rgb = resize_max(rgb_original, args.max_dim)
    infrared, scale_infrared = resize_max(infrared_original, args.max_dim)
    model = RIFT2(npt=args.npt, patch_size=args.patch_size)

    started = time.perf_counter()
    kp_rgb, des_rgb, kp_infrared, des_infrared = model(rgb, infrared)
    points_rgb, points_infrared, matches = match_keypoints_nn(
        des_rgb,
        des_infrared,
        kp_rgb,
        kp_infrared,
        lowes_ratio=args.lowes_ratio,
        mutual=False,
    )
    if len(points_rgb) < 4:
        raise RuntimeError(f"insufficient_matches:{len(points_rgb)}")

    h_resized, mask = cv2.findHomography(
        points_rgb,
        points_infrared,
        cv2.USAC_MAGSAC,
        args.reproj_threshold,
    )
    if h_resized is None or mask is None:
        raise RuntimeError("homography_fit_failed")

    # RIFT2 estimates RGB-resized -> infrared-resized. Convert to both original
    # image coordinate directions so the figure can use infrared -> RGB.
    s_rgb = np.diag([scale_rgb, scale_rgb, 1.0])
    s_infrared = np.diag([scale_infrared, scale_infrared, 1.0])
    h_rgb_to_infrared = normalized(
        np.linalg.inv(s_infrared) @ h_resized @ s_rgb
    )
    h_infrared_to_rgb = normalized(np.linalg.inv(h_rgb_to_infrared))

    inlier_mask = mask.ravel().astype(bool)
    projected = cv2.perspectiveTransform(
        points_rgb[inlier_mask].reshape(-1, 1, 2), h_resized
    ).reshape(-1, 2)
    reprojection = np.linalg.norm(
        projected - points_infrared[inlier_mask], axis=1
    )

    record = {
        "method": "RIFT2 (Python, resize-aware)",
        "mapping_used_by_figure": "infrared_original_to_rgb_original",
        "rgb_source": "/".join(args.rgb.parts[-3:]),
        "infrared_source": "/".join(args.infrared.parts[-3:]),
        "rgb_shape": list(rgb_original.shape[:2]),
        "infrared_shape": list(infrared_original.shape[:2]),
        "config": {
            "max_dim": args.max_dim,
            "npt": args.npt,
            "patch_size": args.patch_size,
            "lowes_ratio": args.lowes_ratio,
            "mutual": False,
            "estimator": "USAC_MAGSAC",
            "reproj_threshold": args.reproj_threshold,
            "opencv_version": cv2.__version__,
        },
        "scale_rgb": scale_rgb,
        "scale_infrared": scale_infrared,
        "keypoints_rgb": len(kp_rgb),
        "keypoints_infrared": len(kp_infrared),
        "matches": len(matches),
        "inliers": int(inlier_mask.sum()),
        "inlier_ratio": float(inlier_mask.mean()),
        "mean_reprojection_resized_px": float(reprojection.mean()),
        "runtime_sec": time.perf_counter() - started,
        "homography_rgb_resized_to_infrared_resized": h_resized.tolist(),
        "homography_rgb_original_to_infrared_original": h_rgb_to_infrared.tolist(),
        "homography_infrared_original_to_rgb_original": h_infrared_to_rgb.tolist(),
    }
    args.output.parent.mkdir(parents=True, exist_ok=False)
    args.output.write_text(json.dumps(record, indent=2), encoding="utf-8")
    print(json.dumps(record, indent=2))


if __name__ == "__main__":
    main()
