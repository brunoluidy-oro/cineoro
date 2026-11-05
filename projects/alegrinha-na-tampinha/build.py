#!/usr/bin/env python3
"""Gera shotlist.html e assets-prompts.md.

- shotlist.src.html  + thumbs/*.jpg + assets_prompts.py  ->  shotlist.html
- assets_prompts.py                                      ->  assets-prompts.md

Uso (dentro desta pasta):  python3 build.py
Edite o .src.html ou o assets_prompts.py e rode de novo; os arquivos gerados são sempre regenerados.
"""
import base64
import html
import pathlib
import re
import runpy

ROOT = pathlib.Path(__file__).resolve().parent
ap = runpy.run_path(str(ROOT / "assets_prompts.py"))
OBJECTS, assemble = ap["OBJECTS"], ap["assemble"]


def asset_prompts_html() -> str:
    out = []
    for obj in OBJECTS:
        kind = "captação" if obj["kind"] == "real" else "animação"
        tcls = "t-live" if obj["kind"] == "real" else "t-toon"
        out.append(f'<details><summary>{html.escape(obj["title"])} <span class="tag {tcls}">{kind}</span> <code>{obj["tag"]}</code></summary><div>')
        out.append(f'<p><b>Anexar:</b> {html.escape(obj["attach"])}</p>')
        out.append(f'<p style="color:var(--muted)">{html.escape(obj["note"])}</p>')
        for i, (label, view) in enumerate(obj["views"]):
            pid = f'p-{obj["id"]}-{i}'
            out.append(
                f'<div class="pview"><div class="pbar"><span>Visão: {html.escape(label)}</span>'
                f'<button class="copy" type="button" data-target="{pid}">Copiar prompt</button></div>'
                f'<pre class="prompt" id="{pid}">{html.escape(assemble(obj, view))}</pre></div>'
            )
        out.append("</div></details>")
    return "\n".join(out)


def asset_prompts_md() -> str:
    lines = [
        "# Prompts de assets (GPT): sheets de produto, uma visão por imagem",
        "",
        "Gerado por `build.py` a partir de `assets_prompts.py`. Edite lá, não aqui.",
        "",
        "Como usar: uma imagem por vez, formato horizontal; gere primeiro a visão 3/4 de cada objeto; "
        "depois de aprovada, anexe-a como referência nas outras visões e mantenha o MASTER igual.",
        "",
    ]
    for obj in OBJECTS:
        lines += [f"## {obj['title']} (`{obj['tag']}`)", "", f"**Anexar:** {obj['attach']}", "", f"> {obj['note']}", ""]
        for label, view in obj["views"]:
            lines += [f"### Visão: {label}", "", "```", assemble(obj, view), "```", ""]
    return "\n".join(lines)


def inline_img(match: re.Match) -> str:
    data = (ROOT / "thumbs" / f"{match.group(1)}.jpg").read_bytes()
    return "data:image/jpeg;base64," + base64.b64encode(data).decode("ascii")


src = (ROOT / "shotlist.src.html").read_text(encoding="utf-8")
out = src.replace("{{ASSET_PROMPTS}}", asset_prompts_html())
out = re.sub(r"\{\{IMG:([a-z0-9-]+)\}\}", inline_img, out)
(ROOT / "shotlist.html").write_text(out, encoding="utf-8")
(ROOT / "assets-prompts.md").write_text(asset_prompts_md(), encoding="utf-8")
print(f"shotlist.html: {len(out) / 1024:.0f} KB · assets-prompts.md: {sum(len(o['views']) for o in OBJECTS)} prompts")
