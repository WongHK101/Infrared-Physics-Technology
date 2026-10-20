"""Correct the student Draw.io framework without replacing its visual layout."""
from pathlib import Path
import hashlib
import re
import shutil
import sys
import xml.etree.ElementTree as ET

from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "_shared"))
from editable_diagram import Diagram

ROOT = Path(__file__).resolve().parent
BASE_SHA256 = "33368e43a36445ab8f2505db8abf62eeacb71ef38558368dc711d1b7bb25e475"
P = "XzELz4YX8JGQN3SIv_NI-"
Q = "4mSE56h2CbKbttdPeRyT-"


def main():
    base = ROOT / "source_assets/student_framework_original.drawio"
    assert hashlib.sha256(base.read_bytes()).hexdigest() == BASE_SHA256
    d = Diagram(1610, 1060)
    d.doc = ET.parse(base).getroot()
    d.root = d.doc.find(".//mxGraphModel/root")
    d.sequence = 10000
    cells = {c.get("id"): c for c in d.root.findall("mxCell")}

    def geometry(key, **values):
        g = cells[key].find("mxGeometry")
        for name, value in values.items():
            g.set(name, str(value))

    def label(key, text, size=23):
        c = cells[key]
        c.set("value", text)
        c.set("style", c.get("style", "") +
              f";fontFamily=Times New Roman;fontSize={size};fontColor=#17252D;")

    def remove(key):
        d.root.remove(cells[key])

    def display_asset(path):
        # Small workflow panels retain >1000 effective dpi; full sources stay intact.
        target = ROOT / "outputs/display_assets" / path.name
        target.parent.mkdir(parents=True, exist_ok=True)
        with Image.open(path) as img:
            if max(img.size) <= 1600:
                shutil.copy2(path, target)
            else:
                img = img.convert("RGB")
                img.thumbnail((1600, 1600), Image.Resampling.LANCZOS)
                img.save(target, quality=96, subsampling=0, optimize=True)
        return target

    def photo(key, path):
        g = cells[key].find("mxGeometry")
        box = [float(g.get(n, "0")) for n in ("x", "y", "width", "height")]
        remove(key)
        d.photo(*box, display_asset(ROOT / "source_assets" / path))

    # Preserve the student's panels, hierarchy, arrows and parameter-space drawing.
    for c in cells.values():
        c.set("style", re.sub(r"light-dark\((#[0-9A-Fa-f]+),[^)]+\)", r"\1",
                              c.get("style", "")))

    # Keep the approved S02/000009 example and native-resolution image assets.
    rgb = ROOT / "source_assets/scene02_pair000009_rgb_selected_crop.jpg"
    ir = ROOT / "source_assets/scene02_pair000009_infrared_selected_crop.jpg"
    photo(Q+"2", rgb.name)
    photo(Q+"3", ir.name)
    remove(Q+"1")
    d.photo(280, 268, 135, 110, display_asset(rgb))
    d.photo(424, 268, 135, 110, display_asset(ir))
    label(P+"15", "MINIMA (RoMa)")
    for key, pair in [(Q+"6", "000001"), (Q+"8", "000005"), (Q+"7", "000009")]:
        photo(key, f"scene02_pair{pair}_rgb.jpg")
    label(P+"23", "I<sub>N</sub>")
    g = cells[P+"212"].find("mxGeometry")
    points = g.findall("mxPoint")
    points[0].set("as", "targetPoint")
    points[1].set("as", "sourcePoint")

    label(P+"175", "Frame quality weights", 24)
    geometry(P+"175", x=1004, y=716, width=225, height=42)
    label(P+"173", "{H<sub>i</sub>, q<sub>i</sub>}", 30)
    label(P+"162", "Candidate<br/>homographies", 23)
    geometry(P+"162", x=590, y=709, width=145, height=50)
    label(P+"214", "Kept", 20)
    label(P+"216", "Consensus", 20)
    geometry(P+"216", x=80, width=150)
    label(P+"217", "Rejected", 20)
    geometry(P+"217", x=80, width=150)
    label(P+"196", r"$$\bar{\mathbf{h}}_S=\frac{\sum_{i\in\mathcal C_S} q_i\mathbf{h}_i}{\sum_{i\in\mathcal C_S}q_i}$$", 23)
    geometry(P+"196", x=5, y=35, width=215, height=75)
    geometry(P+"198", x=0, width=220)
    label(P+"199", "Weighted<br/>consensus", 24)
    geometry(P+"199", x=15, width=190)
    label(P+"181", "H&#772;<sub>S</sub>", 43)

    # Grid highlights illustrate spatial support, not measured support maps.
    remove(Q+"23")
    for x, img, broad in [(1248.55, rgb, False), (1412.55, ir, True)]:
        d.photo(x, 540, 157, 126, display_asset(img))
        for k in range(1, 4):
            d.line([(x+k*157/4, 548), (x+k*157/4, 658)], color="#FFFFFF", arrow=False)
            d.line([(x, 548+k*110/4), (x+157, 548+k*110/4)], color="#FFFFFF", arrow=False)
        if broad:
            d.cell(x+39, 548, 78, 110, style="fillColor=#37A56D;fillOpacity=25;strokeColor=none;")
        else:
            d.cell(x+39, 575, 39, 55, style="fillColor=#37A56D;fillOpacity=25;strokeColor=none;")
    label(P+"168", "Sparse support", 23)
    geometry(P+"168", x=1243, y=685, width=165, height=60)
    label(P+"167", "Broad support", 23)
    geometry(P+"167", x=1413, y=685, width=165, height=60)

    photo(Q+"30", "scene02_pair000009_after_scene_homography_overlay_crop.jpg")
    photo(Q+"29", "scene02_pair000009_edge_overlay_crop.jpg")
    label(P+"189", "Warped overlay", 23)
    geometry(P+"189", x=295, y=1008, width=290, height=30)
    label(P+"190", "Edge agreement", 23)
    label(P+"188", "Scene transform", 23)
    geometry(P+"188", x=30, y=987, width=205, height=40)

    # Canonical retention and score ranking branch independently from diagnostics.
    label(P+"184", "QA", 43)
    label(P+"191", "Scene diagnostics", 23)
    geometry(P+"191", x=1016, y=1006, width=220, height=30)
    label(P+"185", "Canonical gate<br/>y<sub>S</sub>", 27)
    geometry(P+"185", x=1290, y=815, width=260, height=95)
    d.box(1290, 945, 260, 95, fill="#E2EDF1", stroke="#4A9985")
    d.text(1300, 952, 240, 80, "Score ranking<br/>R(S)", size=27)
    remove(P+"208")
    d.line([(1218, 909), (1250, 909), (1250, 862), (1282, 862)], color="#159FB3")
    d.line([(1250, 909), (1250, 992), (1282, 992)], color="#159FB3")
    d.export(ROOT, "fig03_scene_framework")


if __name__ == "__main__":
    main()
