# Character sheet — the standard template

This is THE template for every character sheet in the CINEORO tree. Always start from it. When the user
asks for anything different — a 3D character, a specific art style, an animal, a creature, extra
views, a different way of showing a feature (hands, tattoos, a costume detail, a profile), a different
aspect ratio — **keep the template and adapt it**; never replace it with a free-form prompt.

## The template (fill the brackets; keep every other line)

```
Create a character sheet, three panels side by side, 16:9, same person, same scale, same ground line, same color grade:

- LEFT: large CLOSE-UP portrait, tightly framed from forehead to chin with a little of the shoulders, sharp focus, looking directly at camera with a neutral steady expression, showing the face, [FACIAL HAIR / HEAD ACCESSORIES] and skin details exactly.
- MIDDLE: full-body FRONT view WITH the head fully visible, from the top of the head down to the feet, both feet fully in frame. Standing straight, arms relaxed straight down at the sides, hands visible, body squared to camera, looking directly at camera with a neutral expression.
- RIGHT: full-body BACK view, same pose, WITH the head visible from behind, from the top of the head down to the heels, showing [BACK DETAILS OF THE WARDROBE: seams, closures, straps, prints, hair from behind].

CHARACTER: [ETHNICITY/ORIGIN IF RELEVANT], roughly [AGE]. BUILD: [height impression, proportions, shoulders, posture]. SKIN: [tone, texture, exposure marks, sun or weather effects]. FACE: [face shape, cheekbones, eyes and gaze, eyebrows, nose, lips, forehead and expression lines]. HAIR AND FACIAL HAIR: [length, color, texture, hairline, density and pattern of beard or stubble]. DISTINGUISHING MARKS: [scars, moles, wrinkles, only what must stay consistent]. HANDS: [size, texture, condition, nails].

WARDROBE, keep EXACTLY as described, identical in all panels:
- [ITEM 1: material, color, fit, wear and tear]
- [ITEM 2]
- [ITEM 3]
- [FOOTWEAR]
- [ACCESSORIES: only what is essential]

All three panels show the same person at identical scale, same color grade. Both full-body figures stand with the full body in frame, head to feet, arms straight down, no posing. The face in the close-up is identical to the face in the full-body panels.

Neutral flat medium-gray seamless studio background (not the colored background of any reference). Soft even studio lighting, consistent across all three views, no harsh shadows, no colored light. Preserve every material precisely: [LIST OF KEY TEXTURES], all worn and distressed with real use.

[STYLE: photorealistic live-action / stylized 3D render, not photograph, not realistic]. Ultra-detailed material rendering, [SKIN AND MATERIAL DETAILS]. High resolution, tack-sharp focus on the subject, deep depth of field on the full-body panels, shallow depth of field only on the close-up.

NO text, NO labels, NO captions, NO watermarks, NO logos, NO extra props, NO background environment. Clean character sheet only.

--- NEGATIVE ---
 changed outfit, action pose, [DESVIOS DE FIGURINO ESPECÍFICOS], smooth plastic skin, mannequin, extra limbs, warped seams, oversaturation, blur, watermark, text, logo
```

## Rules for filling it

- Fill **every** bracket; delete only a bracket that truly has nothing (then delete its label too).
- Only what must stay consistent across the film goes in DISTINGUISHING MARKS.
- WARDROBE items are the costume of the **base state**; other states (wet, wounded, dirty) are
  separate sheets or masked variants with a new tag (see `asset-pipeline.md`).
- The NEGATIVE's first slot lists the wardrobe drifts this costume is likely to suffer (wrong
  colour, missing strap, modern zipper, swapped boots…).
- If a reference image exists, it supplies identity; the text still restates the critical details.

## Adapting the template (keep its skeleton, change only what the request needs)

The skeleton that never changes: **panel layout declared up front · same subject / scale / ground
line / grade · the identity lock ("the face in the close-up is identical…") · neutral background ·
even consistent light · material preservation · STYLE line · clean-sheet line · NEGATIVE.**

| Request | Adapt |
|---|---|
| **Stylized 3D / animation / art style** | STYLE line → the exact style ("stylized 3D render, Pixar-like proportions, not photograph, not realistic" / "hand-painted 2D cel style" / "claymation with fingerprints"); SKIN AND MATERIAL DETAILS in that medium's terms; in NEGATIVE replace "smooth plastic skin" with the style's failure (e.g. "photoreal skin, off-model proportions, inconsistent line weight"); drop "worn and distressed" if the style is clean. |
| **Different presentation** (profile, ¾, hands, a tattoo, headgear detail, extra views) | Keep three panels if possible and swap the panel content ("LEFT: … close-up of the hands, palms and backs"), or add panels and state the count up front ("four panels side by side: close-up, front, side profile, back"). Keep the same-scale / same-ground-line clauses for every full-body panel. |
| **Non-human** (animal, creature, robot) | CHARACTER block → species/design, proportions, surface (fur, scales, metal), anatomy that must stay consistent; FRONT/BACK views become front/rear or side views as the anatomy demands; "arms straight down" becomes the creature's neutral stance. |
| **No face** (masked, helmeted) | LEFT panel shows the mask/helmet close-up; identity lock refers to it. |
| **Different aspect ratio or layout** | Change "16:9" and "side by side" only; keep the panel order logic. |
| **Coloured or environment background requested** | Allowed only if the user asks; keep it flat and identical across panels so it doesn't leak into later shots. |
| **Light other than even studio** | Only on request; keep it identical across the three views. |

Every adaptation is stated explicitly in the prompt — never leave the template's original wording in
place when it contradicts the request (e.g. "photorealistic" in a cartoon sheet).
