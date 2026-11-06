#!/usr/bin/env python3
"""Gera shotlist.html, assets-prompts.md e video-prompts.md.

- shotlist.src.html (+ video_prompts.py, + thumbs/ se houver placeholders) -> shotlist.html
- assets_prompts.py -> assets-prompts.md
- video_prompts.py  -> video-prompts.md

Uso (dentro desta pasta):  python3 build.py
Placeholders na página:  {{PROMPT:1a}}  {{PROMPTS:3b,4b,5b,6b}}  {{CREDITS}}  {{IMG:nome}}  {{ASSET_PROMPTS}}
"""
import base64
import html
import pathlib
import re
import runpy

ROOT = pathlib.Path(__file__).resolve().parent
ap = runpy.run_path(str(ROOT / "assets_prompts.py"))
vp = runpy.run_path(str(ROOT / "video_prompts.py"))
OBJECTS = ap["OBJECTS"]
PROMPTS, BASE_KEYS, ALT_KEYS = vp["PROMPTS"], vp["BASE_KEYS"], vp["ALT_KEYS"]
CR_480, CR_1080 = vp["CR_480"], vp["CR_1080"]


def n(x: float) -> str:
    return f"{int(x + 0.5):,}".replace(",", ".")


# ----------------------------------------------------------------------------- prompts de vídeo
def prompt_box(key: str) -> str:
    title, secs, text = PROMPTS[key]
    pid = "pv-" + key
    words = len(text.split())
    return (
        f'<details class="pbox"><summary>{html.escape(title)} <span class="meta">{secs} s · {words} palavras</span></summary>'
        f'<div class="pbar"><span>Copie e cole no Seedance 2.5</span>'
        f'<button class="copy" type="button" data-target="{pid}">Copiar prompt</button></div>'
        f'<pre class="prompt" id="{pid}">{html.escape(text)}</pre></details>'
    )


def credits_html() -> str:
    rows, tot_s = [], 0
    for k in BASE_KEYS:
        title, secs, _ = PROMPTS[k]
        tot_s += secs
        rows.append((title, secs))
    draft, final = tot_s * CR_480, tot_s * CR_1080
    base = draft + final
    alt_s = sum(PROMPTS[k][1] for k in ALT_KEYS)
    out = ['<div class="scroll-x"><table class="credits"><thead><tr><th>Geração</th><th class="num">Segundos</th>'
           '<th class="num">Draft 480p</th><th class="num">Final 1080p</th><th class="num">Ciclo</th></tr></thead><tbody>']
    for title, secs in rows:
        out.append(f'<tr><td>{html.escape(title)}</td><td class="num">{secs}</td><td class="num">{n(secs * CR_480)}</td>'
                   f'<td class="num">{n(secs * CR_1080)}</td><td class="num">{n(secs * (CR_480 + CR_1080))}</td></tr>')
    out.append(f'<tr class="tot"><td><b>Total</b></td><td class="num"><b>{tot_s}</b></td><td class="num"><b>{n(draft)}</b></td>'
               f'<td class="num"><b>{n(final)}</b></td><td class="num"><b>{n(base)}</b></td></tr></tbody></table></div>')

    def scen(total_s):
        d, f = total_s * CR_480, total_s * CR_1080
        b = d + f
        return b, b + 0.5 * b, b + 0.5 * d
    b1, full1, draft1 = scen(tot_s)
    b2, full2, draft2 = scen(tot_s + alt_s)
    out.append('<div class="scroll-x"><table class="credits"><thead><tr><th>Cenário</th><th class="num">Créditos</th></tr></thead><tbody>')
    out.append(f'<tr><td>Sem nenhuma refação</td><td class="num">{n(b1)}</td></tr>')
    out.append(f'<tr><td><b>50% dos takes com 1 refação completa</b> (refaz o draft e o 1080p)</td><td class="num"><b>{n(full1)}</b></td></tr>')
    out.append(f'<tr><td>50% dos takes com 1 refação pega ainda no draft (só o 480p se repete)</td><td class="num">{n(draft1)}</td></tr>')
    out.append(f'<tr><td>Testando também a abertura B do 3a (+{alt_s} s), refação completa</td><td class="num">{n(full2)}</td></tr>')
    out.append(f'<tr><td>Testando também a abertura B do 3a, refação só no draft</td><td class="num">{n(draft2)}</td></tr>')
    out.append('</tbody></table></div>')
    out.append('<ul class="small-notes">'
               f'<li><b>Preço usado:</b> a página oficial da Higgsfield (verificada em 20/10/2026) diz que um clipe de 8 s custa 128 créditos em 1080p, 56 em 720p e 24 em 480p. Por segundo, isso dá {CR_1080} no 1080p e {CR_480} no 480p (divisão minha).</li>'
               '<li><b>O que eu assumi:</b> finalizar um draft em 1080p custa uma geração 1080p inteira. Esse preço não é publicado. Outra página da própria Higgsfield cita 72 créditos para 8 s em 1080p (9 por segundo); se for esse o preço real, o total cai bastante. Confira o preço no botão Gerar antes do primeiro lote.</li>'
               f'<li><b>Refação:</b> contei 50% dos segundos, não 50% dos takes. Se a espinha de 30 s (3a) precisar ser refeita, são +{n(30 * (CR_480 + CR_1080))} créditos de uma vez.</li>'
               '<li>Os Elements são imagens e eu não contei custo extra por referência. O plano Plus inclui 1.000 créditos por mês; não sei qual é o seu plano.</li>'
               '</ul>')
    return "\n".join(out)


def video_prompts_md() -> str:
    lines = ["# Prompts de vídeo (Seedance 2.5)", "", "Gerado por `build.py` a partir de `video_prompts.py`. Edite lá, não aqui.", ""]
    for k, (title, secs, text) in PROMPTS.items():
        lines += [f"## {title} ({secs} s)", "", "```", text, "```", ""]
    return "\n".join(lines)


# ----------------------------------------------------------------------------- prompts de imagem
def asset_prompts_html() -> str:
    out = []
    for obj in OBJECTS:
        kind = "captação" if obj["kind"] == "real" else "animação"
        tcls = "t-live" if obj["kind"] == "real" else "t-toon"
        out.append(f'<details><summary>{html.escape(obj["title"])} <span class="tag {tcls}">{kind}</span> <code>{obj["tag"]}</code></summary><div>')
        out.append(f'<p><b>Anexar:</b> {html.escape(obj["attach"])}</p>')
        out.append(f'<p style="color:var(--muted)">{html.escape(obj["note"])}</p>')
        for i, (label, prompt) in enumerate(obj["prompts"]):
            pid = f'p-{obj["id"]}-{i}'
            out.append(
                f'<div class="pview"><div class="pbar"><span>Visão: {html.escape(label)}</span>'
                f'<button class="copy" type="button" data-target="{pid}">Copiar prompt</button></div>'
                f'<pre class="prompt" id="{pid}">{html.escape(prompt)}</pre></div>'
            )
        out.append("</div></details>")
    return "\n".join(out)


def asset_prompts_md() -> str:
    lines = [
        "# Prompts de assets (GPT): pote real e objetos toon",
        "",
        "Gerado por `build.py` a partir de `assets_prompts.py`. Edite lá, não aqui.",
        "",
        "Como usar: uma imagem por vez; anexe o que a nota pede; depois de aprovada, anexe a imagem aprovada nas seguintes.",
        "",
    ]
    for obj in OBJECTS:
        lines += [f"## {obj['title']} (`{obj['tag']}`)", "", f"**Anexar:** {obj['attach']}", "", f"> {obj['note']}", ""]
        for label, prompt in obj["prompts"]:
            lines += [f"### Visão: {label}", "", "```", prompt, "```", ""]
    return "\n".join(lines)


def inline_img(match: re.Match) -> str:
    data = (ROOT / "thumbs" / f"{match.group(1)}.jpg").read_bytes()
    return "data:image/jpeg;base64," + base64.b64encode(data).decode("ascii")


src = (ROOT / "shotlist.src.html").read_text(encoding="utf-8")
out = src.replace("{{ASSET_PROMPTS}}", asset_prompts_html())
out = re.sub(r"\{\{PROMPTS:([^}]+)\}\}", lambda m: "".join(prompt_box(k.strip()) for k in m.group(1).split(",")), out)
out = re.sub(r"\{\{PROMPT:([^}]+)\}\}", lambda m: prompt_box(m.group(1).strip()), out)
out = out.replace("{{CREDITS}}", credits_html())
out = re.sub(r"\{\{IMG:([a-z0-9-]+)\}\}", inline_img, out)
(ROOT / "shotlist.html").write_text(out, encoding="utf-8")
(ROOT / "assets-prompts.md").write_text(asset_prompts_md(), encoding="utf-8")
(ROOT / "video-prompts.md").write_text(video_prompts_md(), encoding="utf-8")
left = re.findall(r"\{\{[^}]+\}\}", out)
print(f"shotlist.html: {len(out) / 1024:.0f} KB · placeholders restantes: {left}")
