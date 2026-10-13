# Asset pipeline — building references that hold

**Contents:** the asset registry · character in two passes · state variants with masks · props ·
locations · voices · image-generation prompt templates · QA for assets

---

## The asset registry (one table per project, kept in the bible)

| Tag | Type | Image file(s) | Text descriptor (minimal) | Critical details to restate | State of |
|---|---|---|---|---|---|
| `@MARIA` | character | maria_face_v1, maria_look_v1 | 34, lean, sun-lined face, short grey-streaked hair | scar through left eyebrow; wedding ring on right hand | — |
| `@MARIA_WET` | character state | maria_face_v1 + wet mask | same + soaked hair, darkened shirt | same | `@MARIA` |
| `@KNIFE` | prop | knife_v1 | short worn blade, pale bone handle, leather sheath on the belt | sheath on her LEFT hip | — |
| `@KITCHEN_DAWN` | location | kitchen_plate_v1/v2 | rural kitchen, wood stove, tin roof, one window frame-right | — | — |

Text descriptor format: `age + build/role + current state + 2–3 unique visible features +
action-critical details (+ voice, if the character speaks)`.

## Character in two passes

1. **Pass one — the character sheet.** The standard template (`character-sheet.md`): a split frame
   with the facial close-up (entire head) on one half and the full-body front and back views on the
   other, on a plain light-grey background. After generation the director blurs or removes the heads in
   the full-body views, so the close-up is the only face. Its close-up panel IS the face anchor: the face is born
   here once, and every other asset is checked against it.
2. **Pass two (optional) — a standalone face close-up**, only when a shot needs more skin detail than
   the sheet gives. Generate it with the approved sheet attached as the identity reference (Face
   anchor template below).
3. **Hands** if they matter (they usually do): a close-up of the hands with their marks, size and
   condition — two characters' hands must never look alike if they touch on screen.

## State variants with masks

The base portrait never runs through a model again. Frost, dirt, blood, a wound, wet hair, frostbite:
inpaint them around the base with masks, region by region. The base stays the same pixels, so identity
and skin texture survive. Each state gets a new tag.

## Props

Photograph-like stills on a neutral ground (grey seamless, snow, cloth): one object, its real scale
cue (a hand, a ruler-like reference in the descriptor), its material and wear. For objects the engine
misreads, **don't name the object in the prompt — describe the geometry** ("a single long smooth shaft
sweeping up out of the snow in a shallow arc, thickest at the base, tapering to a narrow tip, no knob,
no joint, three to five metres tall"). The word can pull a cartoon version of the object.

## Locations

Plates carry **architecture, materials, clutter and atmosphere** — not the lens. The lens look is
written in the prompt (on 2.5 the anamorphic character held from the prompt alone in production). Make
2–3 plates per location (wide, a reverse, a detail) in the same light state; a new light state (dawn vs
night) is a new location tag.

## Voices

A 5–10 s clean line per speaking character (from an approved take, or a cast recording you have rights
to), no music, no overlap. Tag it `@NAME_VOICE`.

---

## Image-generation prompt templates (for the image model of your choice)

**Face anchor**
```
Single close-up portrait photograph, one frame, no panels and no divider line, of the same [person]
as the attached character sheet (its face close-up supplies identity only): [descriptor], the entire
head fully inside the frame, nothing cropped, eyes to camera, [a mild expression from the personality — "the face of someone who…"],
real skin texture with pores, fine lines, asymmetry and marks [list], no retouching, not a model —
an ordinary [person] from [place], shot on 85mm portrait lens, soft cinematic key light from one
side with gentle fill, bright and clean overall — at most one side of the face slightly darker,
plain solid light-grey background, photoreal, not a render.
```

**Character sheet (close-up + full-body front and back)** — always use the standard template in
`character-sheet.md`, adapted to the request (3D, art style, creature, other views). Never write a
free-form turnaround prompt.

**Prop**
```
Photograph of [object geometry and materials, wear, age], alone on [neutral ground], true scale
[cue], soft overhead light, sharp detail, no hands, no text, no background objects, photoreal.
```

**Location plate**
```
Wide photograph of [place], [time and light state], [architecture, materials, clutter that tells how
people live here], [weather/atmosphere], no people, eye-level, [aspect ratio], documentary realism,
not a render.
```

**Keyframe still**
```
Film still: [composition with screen positions], [characters by tag, matching their references],
[action frozen mid-moment], [light as in the LIGHT block], [look as in the FILM LOOK], [aspect].
```

## QA for assets

- Face: entire head in frame; real texture, asymmetry, readable at small size, no beauty smoothing;
  bright enough to read every feature — at most one side slightly darker.
- Character sheet: two panels, the close-up filling its half with the entire head and hair in frame;
  the whole sheet bright and clean, at most one side of the face slightly darker, no dark or moody
  panel; pores and hair strands visible; same face in all views; expression alive but mild; wardrobe
  and accessories readable in the full-body views; materials believable; no text or logos; nothing out
  of period by accident.
- Props: scale clear; no extra objects; geometry unambiguous.
- Plates: no people; light state matches the scene's; no lens effects baked in unless intended.
- Every asset logged in the registry with its tag before the first shot.
