# Light control — locks, rescues, colour continuity

**Contents:** contre-jour locks · flat-light rescue · exposure failure modes · colour as material ·
palette as a system · continuity across a film · reference scope · flares and artifacts

---

## Contre-jour (backlight) locks

```
The subject stays between the camera and the brighter background. The camera stays on the shadow
side of the subject. Faces remain in deep shadow unless explicitly lit. Only rim light, edge light,
wet speculars, eye glints and environmental bounce reveal detail. No frontal key, no flat exposure,
no beauty fill.
```
If it still came back flat:
```
The entire shot is exposed for the backlight, not for the face. The face is allowed to fall into
shadow. The silhouette and rim contour carry the image.
```

## Flat-light rescue (the take came back evenly lit)

1. Remove every mood adjective that is not a source ("cinematic lighting", "dramatic lighting").
2. Name the single key, its side, its height, its distance-to-falloff.
3. Put the camera on the shadow side and say so in CAMERA and LIGHT.
4. Add the background's fate: "everything beyond two metres falls into darkness".
5. Add the negative trio: "flat even light, beauty fill, frontal key".

## Exposure failure modes (observed) and the fix

| Symptom | Cause | Fix |
|---|---|---|
| Dark vignette / corners falling off | "dark, underexposed, moody" words | "even exposure corner to corner, NO vignette, NO edge falloff"; describe darkness as falloff from a source |
| Crushed, muddy blacks | "low-key, crushed, deep black" | "shadows deep but BREATHING — never crushed"; for mid-key: "LIFTED shadows" |
| Milky, lifted, grey blacks | over-soft "film look" words | "blacks deep and soft, NO milky blacks" |
| Whole frame orange by firelight | warm source with no counter | add the cold ambient + "fire light dies within N metres" + "NO warm light on everything" |
| HDR glow, everything visible | engine default | "highlights roll off and clip gently; shadows hold detail but stay dark; NOT HDR" |
| Look changes between shots in one generation | look stated once at the end | FILM LOOK lock early-middle + a short "FILM LOOK REPRISE" in the recap |

## Colour as material + light + role

- ❌ "the woman wears red, the man wears blue" → ✅ "her crimson scarf catching the cold tungsten
  spill from the corridor; his navy coat swallowed by the dark".
- **Two-temperature images** read as photographic: a cool ambience against warm materials, both
  muted. Name both temperatures and what carries each.
- **The engine's grading traps:** teal-and-orange, saturated sunsets, neon purple. Name them in the
  negative when the world is near them.

## Palette as a system (decide once per film)

- **The permanent state** — e.g. graphite and deep blue: cold is the condition of the world.
- **The man-made exception** — warmth appears only where someone built it with their hands (fire,
  lamp, a lit window).
- **The single exception colour** — one colour used once (an aurora at the end, a red coat in one
  scene). Its rarity is its meaning.
Write the system into the project bible; each LIGHT block then only states which part of the system
this scene uses.

## Continuity across a film

- One FILM LOOK block per sequence, pasted verbatim.
- Same Kelvin per location and time of day across all its shots.
- Keyframes from approved takes carry the grade into new generations (see `cineoro-assets`).
- If colour drifts between generations, attach the last approved frame as a look reference with the
  scope "grade, palette, exposure and skin texture only — not composition".

## Reference scope (light)

Reference images carry their own lighting and will impose it. Unless a reference is the keyframe of
this shot, scope it out:
```
REFERENCE SCOPE: the references supply faces, wardrobe, build, hands and objects ONLY. IGNORE their
backdrops, ground, sky, weather, lighting direction, exposure and colour grade.
```

## Flares and artifacts

- **NO LENS FLARES** is its own short block: "no flares, no light streaks, no floating bokeh orbs, no
  glow overlays; every light source stays small and contained within itself". Folded into another
  block, it gets lost.
- Snow, rain or dust "stuck on the glass" appears when the camera is close to weather; forbid it
  unless wanted ("no snow stuck on the lens").
- **Artifact cleanup:** banding, ghosting or compression trails → remove "gate weave" and "chromatic
  aberration" together, keep grain moderate, add "NO digital artifacts, NO compression trails, NO
  ghosting streaks".
