from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
FIGURES = [
    "fig01_problem_benchmark",
    "fig02_benchmark_protocol",
    "fig03_scene_framework",
    "fig04_consensus_qa",
    "fig05_pairwise_evidence",
    "fig06_scene_products",
    "fig07_reliability_selection",
    "fig08_operating_profile",
    "fig09_validation_attribution",
]


def main() -> None:
    failures: list[str] = []
    for name in FIGURES:
        print(f"[build] {name}", flush=True)
        result = subprocess.run(
            [sys.executable, "build.py"], cwd=ROOT / name, check=False
        )
        if result.returncode:
            failures.append(name)
        else:
            source = ROOT / name / "outputs" / f"{name}.pdf"
            destination = ROOT.parent / "figures" / f"{name}.pdf"
            shutil.copy2(source, destination)
    if failures:
        raise SystemExit(f"Figure builds failed: {', '.join(failures)}")


if __name__ == "__main__":
    main()
