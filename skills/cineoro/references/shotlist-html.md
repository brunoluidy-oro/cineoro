# MODE B — the HTML shotlist

Read before producing or revising a shotlist. Every prompt inside follows the CINEORO spine and carries
its full block stack; this file covers only the container, the generation plan and the revision loop.

**Contents:** what you produce · planning generations · revisions · HTML template · scene block pattern

---

## What you produce

One self-contained HTML file (save it to the environment's outputs folder — e.g.
`/mnt/user-data/outputs/shotlist.html` on claude.ai — or the working directory) with:
1. **Title bar** — project name (from the script or the bible), model and format line.
2. **Scenes**, numbered, each with a checkbox, a one-line description, and one or more **generation
   blocks**. Each generation block shows: label (`3a · 22s · 5 shots`), the plain-language header,
   the copy-ready prompt (`<pre>`), and the generation card (`<pre>`).
3. A short "how to use" note.

Generations of a scene are labelled `3a`, `3b`, `3c`. Each is a full standalone prompt with its own
complete stack; continuity between them is carried by the hand-off states (`cineoro-story`).

## Planning generations

1. Silent dramatic read per scene (`cineoro-story`) — never written into the HTML.
2. Budget each scene into generations of 4–30 s: never split the reversal; tactic switches are cut
   points; the last generation of the scene holds the value shift.
3. Duration of each generation = the sum of its shot ranges (no dead air: the engine stretches the end
   of a too-long job).
4. A heavy line earns its own shot; a held silence is a shot; the listener at the reversal is a shot.
5. Write each generation's end state and make it the next generation's first-frame state.

## Revisions

When the user asks for a change (rewrite 4, add an insert, split 6, change wardrobe), regenerate the
same HTML with the change applied. Keep scene numbers stable — checkbox state persists in the browser
by scene number.

## HTML template

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{{PROJECT_TITLE}} — Shotlist</title>
<style>
  :root { --bg:#0e0e10; --panel:#17171a; --panel-2:#1d1d21; --border:#2a2a30; --text:#e8e8ea;
          --dim:#9a9aa2; --accent:#d4a259; --done:#4ade80; }
  * { box-sizing: border-box; }
  body { margin:0; background:var(--bg); color:var(--text); line-height:1.5;
         font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",system-ui,sans-serif;
         padding:32px 16px 80px; }
  .container { max-width:980px; margin:0 auto; }
  h1 { font-size:28px; font-weight:600; margin:0 0 4px; letter-spacing:-0.02em; }
  .subtitle { color:var(--dim); font-size:14px; margin-bottom:24px; }
  .howto { background:var(--panel); border:1px solid var(--border); border-radius:8px;
           padding:14px 18px; font-size:13px; color:var(--dim); margin-bottom:24px; }
  .scene { background:var(--panel); border:1px solid var(--border); border-radius:10px;
           padding:20px 22px; margin-bottom:18px; }
  .scene-header { display:flex; align-items:flex-start; gap:12px; margin-bottom:10px; }
  .scene-header input { width:20px; height:20px; margin-top:2px; accent-color:var(--done);
                        cursor:pointer; flex-shrink:0; }
  .scene-num { font-size:18px; font-weight:700; color:var(--accent); min-width:48px; }
  .scene-desc { font-size:15px; flex:1; }
  .scene.done .scene-desc { text-decoration:line-through; color:var(--dim); }
  .gen { background:var(--panel-2); border:1px solid var(--border); border-radius:6px;
         margin-top:12px; overflow:hidden; }
  .gen-label { display:flex; justify-content:space-between; align-items:center; gap:8px;
               padding:8px 14px; border-bottom:1px solid var(--border); font-size:12px;
               color:var(--dim); text-transform:uppercase; letter-spacing:0.05em; }
  .copy-btn { background:transparent; color:var(--accent); border:1px solid var(--border);
              border-radius:4px; padding:4px 10px; font-size:11px; cursor:pointer;
              text-transform:uppercase; letter-spacing:0.05em; font-family:inherit; }
  .copy-btn:hover { border-color:var(--accent); }
  .copy-btn.copied { color:var(--done); border-color:var(--done); }
  .header-lines { padding:10px 14px; font-size:13px; color:var(--dim); white-space:pre-wrap;
                  border-bottom:1px solid var(--border); }
  pre { margin:0; padding:14px 16px; font-family:"SF Mono",Menlo,Consolas,monospace;
        font-size:12.5px; white-space:pre-wrap; word-break:break-word; }
  pre.card { color:var(--dim); border-top:1px solid var(--border); }
</style>
</head>
<body>
<div class="container">
  <h1>{{PROJECT_TITLE}}</h1>
  <div class="subtitle">Shotlist · Seedance 2.5 · {{FORMAT_LINE}}</div>
  <div class="howto">Tick scenes as you finish them — progress saves in this browser. Copy a prompt
  with its button; the card below it lists duration, aspect and the references to attach, in order.
  Ask Claude for revisions and this file is regenerated.</div>
  {{SCENES_HTML}}
</div>
<script>
  document.querySelectorAll('.scene input[type="checkbox"]').forEach(cb => {
    const key = 'shotlist-scene-' + cb.dataset.scene + '-done';
    try { if (localStorage.getItem(key) === '1') { cb.checked = true; cb.closest('.scene').classList.add('done'); } } catch (e) {}
    cb.addEventListener('change', () => {
      try { localStorage.setItem(key, cb.checked ? '1' : '0'); } catch (e) {}
      cb.closest('.scene').classList.toggle('done', cb.checked);
    });
  });
  document.querySelectorAll('.copy-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      const target = btn.closest('.gen').querySelector(btn.dataset.target);
      navigator.clipboard.writeText(target.textContent).then(() => {
        btn.classList.add('copied'); const t = btn.textContent; btn.textContent = 'Copied';
        setTimeout(() => { btn.classList.remove('copied'); btn.textContent = t; }, 1500);
      });
    });
  });
</script>
</body>
</html>
```

## Scene block pattern

```html
<div class="scene">
  <div class="scene-header">
    <input type="checkbox" data-scene="3">
    <div class="scene-num">3.</div>
    <div class="scene-desc">Nadia tries to take the boat out; Oskar blocks the gangway.</div>
  </div>
  <div class="gen">
    <div class="gen-label">
      <span>Generation 3a · 24s · 5 shots · 21:9</span>
      <span>
        <button class="copy-btn" data-target="pre.prompt">Copy prompt</button>
        <button class="copy-btn" data-target="pre.card">Copy card</button>
      </span>
    </div>
    <div class="header-lines">WHAT HAPPENS: …
WHAT IS SAID: …
TIMING: … = 24s
HOW IT ENDS: …</div>
    <pre class="prompt">[FULL PROMPT — the complete CINEORO spine]</pre>
    <pre class="card">GENERATION CARD …</pre>
  </div>
</div>
```

One checkbox per scene; the user ticks it when all of its generations are done. Escape `<`, `>` and
`&` inside `<pre>` (e.g. official SFX notation in angle brackets) so the HTML stays valid.
