"""Refresh figure-local captions from the authoritative English LaTeX."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent


def balanced(text, start):
    depth = 1
    for pos in range(start, len(text)):
        if text[pos] == "{":
            depth += 1
        elif text[pos] == "}":
            depth -= 1
            if depth == 0:
                return text[start:pos]
    raise ValueError("Unbalanced caption")


for section in sorted((ROOT.parent / "sections").glob("*.tex")):
    text = section.read_text(encoding="utf-8")
    for block in re.findall(r"\\begin\{figure\}.*?\\end\{figure\}", text, re.S):
        assets = list(re.finditer(r"\{figures/(fig\d+_[^}]+)\.pdf\}", block))
        # An appendix float may contain two independently numbered figures.
        for i, asset in enumerate(assets):
            end = assets[i+1].start() if i+1 < len(assets) else len(block)
            segment = block[asset.end():end]
            stem = asset.group(1)
            directory = next(ROOT.glob(stem[:5]+"_*"))
            start = segment.index(r"\caption{") + len(r"\caption{")
            caption = balanced(segment, start)
            name = "caption_draft.txt" if directory.name == stem else f"{stem}_caption.txt"
            (directory / name).write_text(caption.strip()+"\n", encoding="utf-8")
