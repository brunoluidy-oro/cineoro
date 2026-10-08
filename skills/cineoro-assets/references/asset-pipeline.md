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

1. **Pass one — the face.** Generated once, always in close-up, neutral expression, soft directional
   light, real skin texture (pores, asymmetry, marks). This portrait is the anchor every other asset is
   checked against.
2. **Pass two — the look.** Full figure (front/side/back turnaround on a neutral grey ground),
   wardrobe materials and wear, silhouette, built to the locked face.
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
Close-up portrait photograph of [descriptor], neutral expression, eyes to camera, head and top of
shoulders, soft directional window light from frame-left, real skin texture with pores, fine lines,
asymmetry and marks [list], no makeup, no retouching, plain dark grey background, 85mm portrait
perspective, photoreal, not a render.
```

**Look / turnaround**
```
Full-body character turnaround of the same person as the reference portrait — front, side, back —
standing neutral, on a plain mid-grey seamless background, even soft light; wardrobe: [materials, wear,
fit, how it is fastened, what hangs from the belt and why]; photoreal documentary costume photography,
real fabric weight and dirt; same face exactly as the reference.
```

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

- Face: real texture, asymmetry, readable at small size, no beauty smoothing.
- Turnaround: same face; wardrobe readable; materials believable; nothing modern by accident.
- Props: scale clear; no extra objects; geometry unambiguous.
- Plates: no people; light state matches the scene's; no lens effects baked in unless intended.
- Every asset logged in the registry with its tag before the first shot.
