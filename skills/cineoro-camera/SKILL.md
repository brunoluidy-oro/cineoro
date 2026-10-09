---
name: cineoro-camera
description: Camera and optics department of the CINEORO directing tree for Seedance 2.5 video prompts. Decides shot size, field of view in degrees, lens character (including anamorphic and large-format looks), camera height, side, distance, operator behaviour (handheld physics, travels vs stays put, push-ins, pull-backs, whips), focus behaviour, horizon, composition and per-shot camera specs inside multi-shot timelines. Use it whenever a prompt needs a CAMERA block or per-shot framing, whenever a take came back with lens drift, gimbal-smooth or drone-like motion, a static locked frame, centred symmetrical composition, mushy framing, a flipped axis or the wrong shot size, and whenever the user asks how to frame, move or lens a shot. Triggers include "camera block", "enquadramento", "lente", "plano fechado", "câmera na mão", "push-in", "anamorphic", "FOV", "the lens keeps drifting", "too smooth". Called by cineoro-director; also usable on its own.
---

# CINEORO · CAMERA

The camera is a person with a body, standing somewhere specific, holding a lens with a specific
character. The engine's instinct is the opposite — a weightless, stabilized, centred, mid-focal
"AI camera". This department replaces that instinct with an operator.

You write the **CAMERA** block, the camera half of every shot in the **TIMELINE** (size, angle,
lens, movement), and — with `cineoro-light` — the optical half of the **FILM LOOK**.

---

## Five laws

1. **Two levers define "how it is shot": shot size and field of view.** Write FOV in degrees from the
   fixed steps (table below), never a vague "wide". Millimetres, f-stops and lens brands are not
   control — at most a texture anchor (law 5).
2. **The camera either TRAVELS or STAYS PUT — say which, explicitly.** The engine conflates "handheld"
   with "moving". "The camera DOES NOT TRAVEL — it stays in one place and breathes" and "the camera
   WALKS WITH HIM at shoulder height" are different shots. One movement per shot; no compound moves.
3. **A defined camera body, not a floating eye** — a human operator, a dolly, a crane, a locked
   tripod, a drone, or an impossible camera (through a keyhole, inside a mouth) are all valid; the
   engine's default is a weightless drift, so state which one and how it moves. Height (at ice level, hip height, eye level, above
   the head), distance (in metres), side (which side of the axis, shadow side or light side), angle
   to the subject's axis (degrees). Handheld is described as a body: breath, weight shifts, late
   corrections, footfalls landing in the frame.
4. **Composition is a decision, not a default.** The engine centres and evenly fills the frame
   unless told otherwise. Choose — rigorous symmetry (authored, comic, ritual), off-centre asymmetry
   (observed), extreme negative space, frontal tableau — and state screen positions and the focal
   point. One clear focal point and intentional edges in any style.
5. **Lens look = outcomes, optionally anchored by a format name.** "true 65mm anamorphic" may anchor
   texture, but the control comes from the observable outcomes next to it: oval bokeh, horizontal
   squeeze, edge stretch, shallow cinemascope focus, breathing. A name alone does nothing reliable.

---

## Shot size × FOV — the anchor tables

| Abbr | Meaning | In frame |
|---|---|---|
| ECU | Extreme close-up | a detail: eyes, a knot, a hand |
| CU | Close-up | full face / one element large |
| MCU | Medium close-up | head and shoulders |
| MS | Medium shot | to the waist |
| WS | Wide shot | full figure + surroundings |
| EWS | Extreme wide | scale, location, people small |

| FOV | ≈ mm (S35) | Character | Use |
|---|---|---|---|
| 107° | 14–16 | wide rectilinear | huge spaces, foreground looming |
| 84° | 20–24 | classic wide / intimate wide | close face + environment, immersion, low angles |
| 63° | 28–35 | observational | reportage, walking with a subject |
| 47° | 40–50 | neutral human | grounded medium coverage |
| 29° | 75–85 | short tele portrait | dialogue singles, isolation |
| 18° | 100–135 | classic tele | tight emotional CU, compression |
| 12° | 180–200 | tele detail | hands/objects from a distance |
| 8° | 300–400 | super-tele observation | hidden camera, wildlife, far figure in a vast space |

Use only these steps. In a multi-shot, set FOV per shot and add "no lens drift inside the shot".
Decision tree, paste-ready lens language, outcome stacks and anti-drift locks:
**`references/optics.md`**.

---

## The CAMERA block — template

```
CAMERA — [HANDHELD documentary / shoulder-mounted / locked-off tripod / slow dolly], the operator
[kneeling at ice level / walking beside him at shoulder height / standing 4 m away behind a post],
[distance] from [subject], on the [shadow / light] side of the axis, [N]° off the subject's eyeline.
MOVEMENT: the camera [STAYS PUT and breathes: small human tremor, a few degrees off level, a drift
that arrives a beat late] / [TRAVELS: walks with her from the back of the sled to the front at her
pace, every footfall landing in the frame]. One movement only.
OPTICS: [shot size] at [FOV]° — [3–4 observable outcome phrases]; no lens drift inside the shot.
FOCUS: [on what]; [hunts ONCE as … / racks from … to … on the line "…" / breathes].
HORIZON: [level — calm scene] / [canted ~4° and wandering — loss of control].
NOT: [the 3–6 camera behaviours this shot invites: gimbal glide, push-in, zoom, orbit, drone,
tripod-locked, slow motion, a reframe that reveals the hidden action].
```

Per-shot line inside the TIMELINE (the director assembles it):

```
SHOT 2 (5.0–10.0s) — MS three-quarter, 47°, camera WALKING WITH him at shoulder height, arcing
slowly to his left, jolting with each step; focus riding his face. HARD CUT.
```

---

## Operator behaviour library (short)

- **Breathing handheld (stays put):** operator breath, micro-settling, weight shift, a late
  correction; "the camera DOES NOT TRAVEL". Best for faces and intimate moments.
- **Walking handheld (travels):** footfall bounce, framing a beat behind the subject, foreground
  smearing past in motion blur. Best for transit, process, following.
- **Rough walk-in (push-in, human):** "a rough human walk-in from the medium down into her close-up,
  trembling, imperfect, footstep bounce" — never "dolly in" or "zoom", which the engine renders as a
  mechanical glide.
- **Pull-back:** a real operator walking backwards, shaking the whole way, nearly losing the frame
  once. Use sparingly.
- **Low angle:** camera *on the ground*, the figure towering over the lens. Negative: eye-level,
  chest height, floating, drone.
- **High angle:** operator above, looking down at a kneeling/fallen figure; the ground fills the
  background.
- **Madness / panic:** the camera shakes and jumps but **stays put** — no orbit, no circling.
- **Whip:** subject A settled ≥0.3 s → whip ≥0.8 s with motion blur → subject B settled. Faster
  renders as a hard cut.
- **Observation:** 8–12°, operator far away, foreground occlusion over 20–30% of the frame, haze
  between camera and subject.

Full library, including slow-motion rules, POV, vehicle and multi-shot camera continuity:
**`references/operator-and-composition.md`**.

---

## Composition — tools, not a dogma

- **Observed realist toolkit:** off-centre placement, asymmetry, a background in darkness beyond a
  stated distance, chiaroscuro, a tilted horizon only when the scene loses control.
- **Authored/formal toolkit:** centred symmetry, frontal tableaux, level horizons, planimetric staging,
  locked frames, matched cuts.
- **Spectacle toolkit:** scale against people, crane and aerial reveals, orbit and speed ramps when the
  genre wants them.
  Pick from the STYLE INTENT; mixing toolkits inside one shot is the usual cause of mush.
- **Clean frames rule:** every shot is one clear, deliberate, readable composition — one focal
  point, intentional edges, no accidental crop through a face, no mushy half-framing. Foreground blur
  only as one soft shape at a frame edge.
- **Layering:** state foreground / midground / background, each with what is in it and how sharp it is.
- **Scale:** in wide formats (21:9), people are small in an enormous space; in vertical (9:16) the
  subject owns the frame and the background is texture.
- **Axis:** the camera stays on one side of the action axis across all cuts unless a cross is
  designed and stated (lock it with `cineoro-space`).

---

## Format and lens look

The lens look is written in the prompt, in its own block, verbatim every time for a project. On
Seedance 2.5 the anamorphic character was held from the prompt itself, shot after shot, without
baking it into the location plates (observed in production). Paste-ready format blocks (anamorphic,
spherical large-format, 16 mm documentary, vintage, clean modern digital) and dosing words:
**`references/format-and-lens-looks.md`**.

---

## Hand-off to the director

Return to `cineoro-director`:
- the **CAMERA** block;
- the camera line for each **SHOT** of the TIMELINE (size, FOV, position, movement, focus, cut type);
- the optical paragraph for **FILM LOOK** (with `cineoro-light`);
- **locks** (e.g. "the camera stays on her left side of the axis in every shot", "NOT ONE SECOND
  static or stabilized") and camera **negatives**.

## Checklist

- Shot size and FOV (from the table) stated for every shot?
- TRAVELS vs STAYS PUT stated explicitly, one movement per shot?
- Operator height, distance, side and angle written physically?
- Focus behaviour stated (what, when it moves)?
- Horizon choice justified by the scene's state of control?
- Composition chosen from the STYLE INTENT, screen positions stated, one focal point, background treatment stated?
- Lens look written as outcomes (with an optional format anchor), not as gear alone?
- Multi-shot: FOV and position per shot, same side of the axis, "no lens drift inside the shot"?
