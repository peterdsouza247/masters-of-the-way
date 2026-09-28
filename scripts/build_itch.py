#!/usr/bin/env python3
"""Create a reproducible itch.io HTML5 upload from the committed game."""

from __future__ import annotations

import argparse
from pathlib import Path
import re
import zipfile

ROOT = Path(__file__).resolve().parents[1]


def build(output: Path) -> Path:
    game = ROOT / "index.html"
    source = game.read_bytes()
    if not source.lstrip().lower().startswith(b"<!doctype html>"):
        raise ValueError("index.html is not an HTML document")
    # The upload must be self-contained. Links to documentation are fine, but
    # a runtime dependency on another host would fail inside the itch embed.
    text = source.decode("utf-8")
    if re.search(r'<(?:script|img|iframe)[^>]+src=["\'](?:https?:)?//', text, re.I):
        raise ValueError("External runtime asset found; bundle it locally first")
    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        entry = zipfile.ZipInfo("index.html", date_time=(2026, 1, 1, 0, 0, 0))
        entry.compress_type = zipfile.ZIP_DEFLATED
        entry.external_attr = 0o644 << 16
        archive.writestr(entry, source)
    with zipfile.ZipFile(output) as archive:
        assert archive.namelist() == ["index.html"]
        assert archive.read("index.html") == source
    return output


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, default=ROOT / "dist/masters-of-the-way-itch.zip")
    args = parser.parse_args()
    print(build(args.out))
