#!/usr/bin/env python3
"""Gera shotlist.html a partir de shotlist.src.html, embutindo as miniaturas de thumbs/ como data URI.

Uso (dentro desta pasta):  python3 build.py
Edite o .src.html e rode de novo; o shotlist.html é sempre regenerado.
"""
import base64
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent
src = (ROOT / "shotlist.src.html").read_text(encoding="utf-8")


def inline(match: re.Match) -> str:
    name = match.group(1)
    data = (ROOT / "thumbs" / f"{name}.jpg").read_bytes()
    return "data:image/jpeg;base64," + base64.b64encode(data).decode("ascii")


out = re.sub(r"\{\{IMG:([a-z0-9-]+)\}\}", inline, src)
(ROOT / "shotlist.html").write_text(out, encoding="utf-8")
print(f"shotlist.html: {len(out) / 1024:.0f} KB")
