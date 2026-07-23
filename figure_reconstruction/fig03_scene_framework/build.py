from __future__ import annotations

import os
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parent
DRAWIO_SOURCE = ROOT / "drawio_source" / "fig03_scene_framework.drawio"
OUTPUTS = ROOT / "outputs"
EXPECTED_OUTPUTS = [
    OUTPUTS / "fig03_scene_framework.svg",
    OUTPUTS / "fig03_scene_framework.pdf",
    OUTPUTS / "fig03_scene_framework.png",
]


def main() -> None:
    drawio_executable = os.environ.get("DRAWIO_EXECUTABLE")
    if drawio_executable:
        subprocess.run(
            [
                drawio_executable,
                "--export",
                "--format",
                "pdf",
                "--crop",
                "--border",
                "15",
                "--embed-diagram",
                "--output",
                str(EXPECTED_OUTPUTS[1]),
                str(DRAWIO_SOURCE),
            ],
            check=True,
        )

    missing = [path for path in [DRAWIO_SOURCE, *EXPECTED_OUTPUTS] if not path.exists()]
    if missing:
        formatted = "\n".join(f"- {path}" for path in missing)
        raise FileNotFoundError(
            "The Draw.io-managed framework figure is incomplete:\n"
            f"{formatted}\n"
            "Regenerate it from drawio_source/make_live_plan.py and export_plan.json."
        )
    print("Fig. 3 uses the validated Draw.io source and cropped vector export.")


if __name__ == "__main__":
    main()
