"""Editable diagrams with native-resolution photographs and vector labels."""
from __future__ import annotations

import base64
import os
from pathlib import Path
import shutil
import subprocess
import xml.etree.ElementTree as ET

from PIL import Image

INK = "#223645"
BLUE = "#315F82"
GREEN = "#2F8063"
ORANGE = "#B76A2A"
GRAY = "#7A8790"


class Diagram:
    def __init__(self, width: int, height: int):
        self.doc = ET.Element("mxfile", host="app.diagrams.net", compressed="false")
        page = ET.SubElement(self.doc, "diagram", id="publication", name="Publication")
        model = ET.SubElement(page, "mxGraphModel", page="0", math="0",
                              background="#FFFFFF", pageWidth=str(width),
                              pageHeight=str(height))
        self.root = ET.SubElement(model, "root")
        ET.SubElement(self.root, "mxCell", id="0")
        ET.SubElement(self.root, "mxCell", id="1", parent="0")
        self.sequence = 2

    def cell(self, x, y, w, h, value="", style=""):
        node = ET.SubElement(
            self.root, "mxCell", id=str(self.sequence), value=value,
            style=style, vertex="1", parent="1",
        )
        self.sequence += 1
        ET.SubElement(node, "mxGeometry", x=str(x), y=str(y),
                      width=str(w), height=str(h), **{"as": "geometry"})
        return node

    def box(self, x, y, w, h, fill="#F4F7FA", stroke="#BDCBD4", rounded=True):
        return self.cell(x, y, w, h, style=(
            f"rounded={int(rounded)};arcSize=12;whiteSpace=wrap;html=1;"
            f"fillColor={fill};strokeColor={stroke};strokeWidth=1.4;"
        ))

    def text(self, x, y, w, h, value, size=24, color=INK, align="center", bold=False):
        return self.cell(x, y, w, h, value, (
            "text;html=1;whiteSpace=wrap;overflow=visible;rounded=0;"
            "fillColor=none;strokeColor=none;verticalAlign=middle;"
            f"fontFamily=Times New Roman;fontSize={size};fontColor={color};"
            f"align={align};fontStyle={int(bold)};spacing=0;"
        ))

    def photo(self, x, y, w, h, path: Path):
        # Embed original bytes and preserve aspect ratio; never enlarge a thumbnail.
        with Image.open(path) as img:
            iw, ih = img.size
            mime = "jpeg" if img.format == "JPEG" else "png"
        scale = min(w / iw, h / ih)
        dw, dh = iw * scale, ih * scale
        encoded = base64.b64encode(path.read_bytes()).decode("ascii")
        self.cell(x + (w-dw)/2, y + (h-dh)/2, dw, dh, style=(
            "shape=image;verticalLabelPosition=bottom;verticalAlign=top;"
            "imageAspect=1;aspect=fixed;html=1;"
            f"image=data:image/{mime},{encoded};"
        ))

    def ellipse(self, x, y, w, h, fill, stroke="none", dashed=False):
        self.cell(x, y, w, h, style=(
            f"ellipse;fillColor={fill};strokeColor={stroke};"
            f"strokeWidth=1.5;dashed={int(dashed)};"
        ))

    def line(self, points, color=INK, arrow=True, dashed=False):
        edge = ET.SubElement(self.root, "mxCell", id=str(self.sequence),
                             edge="1", parent="1", style=(
            "edgeStyle=none;html=1;rounded=0;strokeWidth=2;"
            f"strokeColor={color};endArrow={'block' if arrow else 'none'};"
            f"endFill=1;dashed={int(dashed)};"
        ))
        self.sequence += 1
        geo = ET.SubElement(edge, "mxGeometry", relative="1", **{"as": "geometry"})
        for key, point in [("sourcePoint", points[0]), ("targetPoint", points[-1])]:
            ET.SubElement(geo, "mxPoint", x=str(point[0]), y=str(point[1]),
                          **{"as": key})
        if len(points) > 2:
            middle = ET.SubElement(geo, "Array", **{"as": "points"})
            for x, y in points[1:-1]:
                ET.SubElement(middle, "mxPoint", x=str(x), y=str(y))

    def export(self, root: Path, stem: str):
        source = root / "drawio_source" / f"{stem}.drawio"
        source.parent.mkdir(parents=True, exist_ok=True)
        ET.ElementTree(self.doc).write(source, encoding="utf-8", xml_declaration=True)
        exe = os.environ.get("DRAWIO_EXECUTABLE") or shutil.which("drawio")
        if not exe:
            raise RuntimeError("Set DRAWIO_EXECUTABLE to the installed draw.io executable.")
        out = root / "outputs"
        out.mkdir(exist_ok=True)
        for fmt in ("pdf", "svg", "png"):
            args = [exe, "--export", "--format", fmt, "--crop", "--border", "5",
                    "--output", str(out / f"{stem}.{fmt}"), str(source)]
            if fmt == "png":
                args[1:1] = ["--width", "4400"]
            flags = subprocess.CREATE_NO_WINDOW if os.name == "nt" else 0
            subprocess.run(args, check=True, creationflags=flags, timeout=240)


def find_asset(folder: Path, scene: str, suffix: str) -> Path:
    matches = sorted(folder.glob(f"{scene}_*_{suffix}.jpg"))
    if len(matches) != 1:
        raise ValueError(f"Expected one asset for {scene}/{suffix}, got {len(matches)}")
    return matches[0]


def overlay_gallery(root: Path, stem: str, rows):
    """Three comparable, uncropped panels per row; scene labels stay horizontal."""
    d = Diagram(1200, 55 + 320 * len(rows))
    for col, text in enumerate(["Size-matched reference", "Scene homography", "Edge agreement"]):
        d.text(8 + col * 402, 0, 388, 35, text, size=26, bold=True)
    suffixes = ["before_resize_overlay_crop", "after_scene_homography_overlay_crop",
                "edge_overlay_crop"]
    for row, (scene, label, retained) in enumerate(rows):
        y = 45 + 320 * row
        d.box(8, y, 1192, 34, fill="#EEF4F2" if retained else "#F0F2F4", stroke="none")
        d.text(20, y, 1170, 34, label, size=24,
               color=GREEN if retained else INK, align="left", bold=True)
        for col, suffix in enumerate(suffixes):
            d.photo(8 + col * 402, y + 40, 388, 271.6,
                    find_asset(root / "source_assets", scene, suffix))
    d.export(root, stem)
