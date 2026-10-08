---
name: cineoro-light
description: Light, exposure and film-look department of the CINEORO directing tree for Seedance 2.5 video prompts. Writes the LIGHT block (motivated sources, direction, side, falloff, exposure priority, Kelvin, continuity of the lit side across cuts), the FILM LOOK lock (capture medium, grain, halation, roll-off, colour as material plus light plus role, no vignette) and the NO LENS FLARES fence. Use it whenever a prompt needs lighting or a consistent look, whenever a take came back flat, over-bright, front-lit, with milky or crushed blacks, a dark vignette, a teal-and-orange grade, invented daylight, lens flares, HDR glow or a look that changes between shots, and whenever the user asks how to light a scene or keep colour consistent across a film. Triggers include "iluminação", "luz natural", "fotografia do filme", "grade", "color", "the image is too bright", "flat light", "keep the color consistent", "night scene by firelight", "film look". Called by cineoro-director; also usable on its own.
---

# CINEORO · LIGHT

The engine's default is to flood a scene with even, flattering, bright light and to clean it until it
glows. Every believable image starts by taking that away. Light here is **a priority constraint, not
decoration**: a source that exists in the world, a direction, a side of the face it reaches, a
distance at which it dies, and a decision about what stays dark.

You write the **LIGHT** block, the **FILM LOOK** lock (with `cineoro-camera` for the lens part) and
the **NO LENS FLARES** fence, and you hand the director the light locks that must survive every cut.

---

## Six laws

1. **Every light has a source that could exist in this world.** Name it (a campfire, a stone lamp, a
   window, a sodium street lamp, the sky after sunset), its **direction**, its **height**, its
   **side** relative to the camera, and its **colour temperature** in Kelvin. If nothing in the world
   could emit it, it doesn't exist.
2. **Say what stays dark.** Exposure is a decision: "exposed for the flame-lit faces; everything beyond
   a metre falls into shadow". The engine fills any darkness you don't defend.
3. **Dark is not underexposed.** Asking for "dark, underexposed, low-key" makes the engine crush
   blacks and darken the frame corners. Write the darkness as *falloff from a source* and lock the
   exposure: "shadows deep but breathing, never crushed; even exposure corner to corner, NO
   vignette".
4. **The lit side never flips.** Across cuts and across generations, the key stays on the same side
   of the faces and the same side of the frame. State it per shot when a scene has cuts.
5. **Colour is material + light + role, never a list.** Not "she wears red" but "the crimson scarf
   catching the cold spill from the corridor". A film's palette is functional: a permanent state and
   a rare exception that means something.
6. **The look is a lock, pasted verbatim.** One FILM LOOK block per project (or per sequence), never
   rewritten per shot. Flares get their own fence, because folded into anything else the engine keeps
   adding them.

---

## The LIGHT block — template

```
LIGHT — [NATURAL / MOTIVATED] LIGHT ONLY, [time of day], [two mood words] (KEY):
SOURCE: the only key is [source], [direction] at [height], [Kelvin]; [secondary: sky ambience /
snow bounce / practical in the background], [Kelvin].
REACH: it lights [the underside of their faces / her left cheek and the knot] and dies within
[distance]; [what it never reaches].
EXPOSURE: exposed for [what]; [what falls into shadow]; shadows deep but breathing, never crushed;
highlights roll off softly; even exposure corner to corner, NO vignette.
CONTINUITY: [the source stays frame-left, off-screen, in every shot; the warm side of every face is
the camera-facing side; lit sides never flip].
NOT: [bright light, studio light, flat even light, beauty fill, daylight (if night), a second source,
milky blacks, crushed muddy blacks, HDR glow].
```

## The FILM LOOK lock — template

```
FILM LOOK (KEY — reproduce this exact photographic character): [capture: real 35mm/65mm film,
500-speed tungsten stock pushed one stop / modern cinema camera]; [key: low-key / mid-key];
[colour: two temperatures — cool desaturated X in the shadows and sky against warm Y in skin, wood,
fur; muted and filmic, never teal-and-orange, never saturated]; [contrast: highlights roll off and
bloom with halation; shadows deep but breathing]; [grain: heavy organic MOVING grain, most visible
in the shadows/sky]; [softness: softer than digital]; [frame: even exposure to all four corners, NO
vignette, NO edge falloff]. MEGA-REAL — NOT a render, NOT 3D, NOT AI-CGI, NOT digital-clean, NOT HDR.
[+ the lens-look paragraph from cineoro-camera]

NO LENS FLARES: no flares, no light streaks, no floating bokeh orbs, no glow overlays; every light
source stays small and contained within itself.
```

Paste-ready looks for common worlds (night by fire, polar/blue dusk, overcast day, harsh sun,
interior by window, urban night, candle/oil lamp, moonlight, mixed practicals):
**`references/film-locks.md`**.

---

## Decisions to make before writing

- **Key level:** low-key (fire, night, interiors by one practical) or mid-key (dusk, overcast,
  daylight exteriors). Mid-key needs "NOT underexposed, NO crushed blacks" stated, or the engine
  drifts dark and murky when you also ask for mood.
- **Exposure priority:** for the faces, for the sky, for the practical. One choice.
- **Camera side vs light:** shooting into the light (contre-jour, rim-lit silhouettes) or with the
  light (frontal, flatter). For drama, the camera usually sits on the **shadow side**.
- **Kelvin per scene,** fixed within the scene: 1800–2000 K fire/candle · 2700–3200 K tungsten ·
  4000 K mixed · 5600 K daylight · 7000–9000 K shade/blue hour · 10000 K+ polar night ambience.
- **The palette's role:** what colour is the permanent state of the film, and what is the rare
  exception (warmth that only exists where people made it; one colour that appears once).

Contre-jour locks, the flat-light rescue, colour continuity across a film, artifact cleanup and
reference-scope rules: **`references/light-control.md`**.

---

## Light in multi-shot generations

Production prompts kept a single generation's light consistent across 4–6 cuts with three moves:
1. **One fixed source, one fixed side** — "the big fire behind and beside the camera, never in frame;
   warm live flicker on the camera-facing side of every face".
2. **Named exceptions per shot** — "when she falls frame-right in shot 5, the warm glow reaches her
   from off-screen FRAME-RIGHT onto her LEFT cheek".
3. **Keyframe inheritance** — when a shot starts from a keyframe image, write "light continues the
   keyframe exactly"; shots without a keyframe "continue this exact grade, light and skin texture".

## Hand-off to the director

Return to `cineoro-director`:
- the **LIGHT** block and the **FILM LOOK** lock (verbatim from the bible when one exists);
- the light **locks** for the LOCKS block ("lit sides never flip", "no source in frame",
  "nothing burns inside — no glow, no embers");
- the light **negatives** for this scene type.

## Checklist

- Is every source physically present in the world, with direction, height, side and Kelvin?
- Is it stated what the light reaches, where it dies, and what stays dark?
- Is darkness written as falloff, with "breathing shadows" and "NO vignette", not as "underexposed"?
- Is the lit side locked across every cut?
- Is colour tied to material + light + role, not listed?
- Is the FILM LOOK pasted verbatim from the bible (or written once and flagged for the bible)?
- Is NO LENS FLARES its own fence?
- If references are attached, is their lighting excluded unless the reference is this shot's keyframe?
