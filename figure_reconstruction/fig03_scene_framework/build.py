from pathlib import Path
import sys

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "_shared"))
from editable_diagram import Diagram, find_asset, BLUE, GREEN, ORANGE

ROOT = Path(__file__).resolve().parent


def main():
    d = Diagram(1200, 925)
    for y, h, fill, title, color in [
        (0, 285, "#EFF5FA", "(a) Progressive pairwise evidence", BLUE),
        (300, 275, "#FCF5EB", "(b) Robust scene consensus", ORANGE),
        (590, 325, "#EFF6F2", "(c) Cross-modal verification and operating profile", GREEN),
    ]:
        d.box(5, y, 1190, h, fill=fill, stroke="#CAD5DC")
        d.text(24, y+12, 1150, 38, title, size=29, color=color, align="left", bold=True)

    for x, suffix, title in [(25, "rgb_selected_crop", "RGB"),
                              (237, "infrared_selected_crop", "Infrared")]:
        d.photo(x, 60, 200, 140, find_asset(ROOT / "source_assets", "scene02", suffix))
        d.text(x, 201, 200, 30, title, size=24)
    d.text(25, 237, 412, 32, "Example input: S02 / 000009", size=22)
    d.line([(450, 132), (505, 132)], color=BLUE)
    d.box(510, 76, 245, 110, fill="#DDEAF5", stroke=BLUE)
    d.text(520, 84, 225, 94, "MINIMA / RoMa<br/>correspondences<br/>+ robust fitting", size=25)
    d.line([(756, 132), (810, 132)], color=BLUE)
    d.box(815, 76, 350, 110, fill="#FFFFFF", stroke=BLUE)
    d.text(825, 83, 330, 95,
           "Frame homography H<sub>i</sub><br/>Geometry-informed weight q<sub>i</sub><br/>r<sub>i</sub>, c<sub>i</sub>, e<sub>i</sub>, m<sub>i</sub>, n<sub>i</sub>",
           size=25)
    d.text(520, 216, 645, 54,
           "Evenly spaced evidence; progressive expansion<br/>All pairs for N &#8804; 300; staged expansion otherwise",
           size=23)

    d.box(25, 390, 170, 108, fill="#FFFFFF", stroke=ORANGE)
    d.text(35, 399, 150, 90, "Accepted<br/>H<sub>i</sub>, q<sub>i</sub>", size=28)
    d.line([(195, 445), (250, 445)], color=ORANGE)
    d.text(255, 350, 295, 32, "Median / MAD filtering", size=25, bold=True)
    d.ellipse(297, 393, 210, 116, fill="none", stroke=ORANGE, dashed=True)
    # Explicitly a schematic, not measured frame hypotheses.
    rng = np.random.default_rng(17)
    for x, y in rng.normal((400, 448), (29, 15), (26, 2)):
        d.ellipse(float(x)-4, float(y)-4, 8, 8, fill="#55A7AC")
    for x, y in [(275, 403), (530, 405), (540, 491)]:
        d.text(x-10, y-10, 20, 20, "&#215;", size=29, color="#A43E3E", bold=True)
    d.text(376, 427, 38, 38, "&#9733;", size=37, color=ORANGE)
    d.text(255, 530, 320, 28, "Parameter-space schematic", size=20)
    d.line([(560, 445), (605, 445)], color=ORANGE)
    d.box(610, 386, 330, 120, fill="#FFFFFF", stroke=ORANGE)
    d.text(622, 393, 306, 43, "Quality-weighted aggregation", size=25, bold=True)
    d.text(622, 444, 306, 48,
           "h&#772;<sub>S</sub> = &#8721;<sub>i&#8712;C<sub>S</sub></sub> q<sub>i</sub>h<sub>i</sub> / &#8721;<sub>i&#8712;C<sub>S</sub></sub> q<sub>i</sub>",
           size=25)
    d.line([(940, 445), (1000, 445)], color=ORANGE)
    d.box(1005, 402, 160, 87, fill="#F5E8D5", stroke=ORANGE)
    d.text(1012, 410, 146, 70, "Scene<br/>H&#772;<sub>S</sub>", size=29)
    d.text(610, 529, 555, 28,
           "&#9679; Kept hypothesis    &#215; Rejected    &#9733; Consensus", size=22)
    d.box(25, 685, 150, 108, fill="#FFFFFF", stroke=GREEN)
    d.text(33, 694, 134, 90, "Scene<br/>H&#772;<sub>S</sub>", size=29)
    d.line([(175, 739), (225, 739)], color=GREEN)
    d.box(230, 664, 405, 154, fill="#FFFFFF", stroke=GREEN)
    d.text(242, 672, 381, 133,
           "Representative QA probes<br/>Edge / gradient improvement<br/>Relative outliers + frame support<br/>Geometry + consensus diagnostics",
           size=25)
    d.line([(635, 739), (703, 739), (703, 686), (763, 686)], color=GREEN)
    d.line([(635, 739), (703, 739), (703, 836), (763, 836)], color=ORANGE)
    d.box(770, 638, 395, 110, fill="#DBEEE3", stroke=GREEN)
    d.text(783, 645, 369, 96,
           "Fixed canonical gate<br/>Support AND (L<sub>S</sub> OR W<sub>S</sub>)<br/>Retained / QA-filtered product", size=24)
    d.box(770, 782, 395, 110, fill="#FBF0E5", stroke=ORANGE)
    d.text(783, 789, 369, 96,
           "Reliability score R(S)<br/>Diagnostic ranking<br/>Reliability-coverage operating profile", size=24)
    d.text(25, 850, 610, 40,
           "Canonical selection and score ranking are separate outputs.", size=22)
    d.export(ROOT, "fig03_scene_framework")


if __name__ == "__main__":
    main()
