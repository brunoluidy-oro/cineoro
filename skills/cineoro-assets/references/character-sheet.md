# Character sheet — the standard template

This is THE template for every character sheet in the CINEORO tree. Always start from it. When the user
asks for anything different — a 3D character, a specific art style, an animal, a creature, extra
views, a different way of showing a feature (hands, tattoos, a costume detail, a profile), a different
aspect ratio — **keep the template and adapt it**; never replace it with a free-form prompt.

## Why it looks like this (production lesson, Oct 2026)

The previous template (three thin panels, "forehead to chin", neutral expression, flat even studio
light, a long NEGATIVE list) gave poor references: the face was small, the hair was cropped, the
expression was a mugshot, and the flat light erased skin and hair texture. The version below is
built from the director's approved example (see "Approved example" below) plus the note that came
with it — the whole scene stays bright, at most one side of the face a little darker:
- **two panels**: the face gets half the frame; front and back share the other half;
- **the entire head in frame** — hair is identity;
- **a living expression drawn from the character's personality**, not a neutral stare;
- **cinematic but bright light**: enough direction to reveal pores and hair strands, yet the whole
  sheet stays light and clean — at most one side of the face slightly darker, never moody;
- **prose, not lists**, with a lens per panel (85mm face, 35mm full body) and no NEGATIVE block.

## The template (fill the brackets; keep every other line)

```
Cinematic character reference sheet, split-frame layout, photorealistic, two panels divided by a thin vertical line, 16:9.

Left panel — facial close-up: [a/an ORIGIN man/woman/boy/girl], [AGE] years old, the entire head fully inside the frame, nothing cropped. [SKIN: tone and texture]. [HAIR: length, colour, texture, grey strands, hairline]. [FACE SHAPE, NOSE and LIPS]. [EYES and EYEBROWS]. [FACIAL HAIR or MAKEUP]. [EXPRESSION: one living expression drawn from the personality — "Warm, lively, slightly amused expression — the face of someone who …"]. [ACCESSORIES visible in the close-up]. [FACE and NECK MARKS that must stay consistent]. Real skin texture with pores, fine lines and natural imperfections, no retouching, not a model — an ordinary [person] from [PLACE]. Shot on 85mm portrait lens, shallow depth of field, soft cinematic key light from one side with gentle fill so pores and hair strands read — at most one side of the face slightly darker.

Right panel — full-body front and back views side by side: the same [person] shown twice within this panel — on the left, a full-body front view facing the camera; on the right, a full-body back view photographed from directly behind. In both, [he/she] stands in a neutral relaxed pose, arms resting at [his/her] sides with hands relaxed and fingers together, full height in frame head-to-toe, [BUILD]. Outfit: [GARMENTS with material, colour and fit], [FOOTWEAR], [the same ACCESSORIES]; no logos, no text. Both figures matched in framing, scale and lighting for consistency. Shot on 35mm lens, even full-length lighting.

Look: clean studio character sheet, plain solid light-grey background, consistent character across all views, soft diffused cinematic lighting, whites holding texture, natural skin tones, fine detail of skin, hair and fabric, vertical divider line separating each view.
```

## Approved example (the one that set the standard)

```
Cinematic character reference sheet, split-frame layout, photorealistic, two panels divided by a thin vertical line.

Left panel — facial close-up: a Brazilian woman, 44 years old, the entire head fully inside the frame, nothing cropped. Warm light-brown skin, shoulder-length dark brown wavy hair with a few natural grey strands, expressive dark brown eyes with soft laugh lines, natural eyebrows, light everyday makeup. Warm, lively, slightly amused expression — the face of someone quick to comment and quick to laugh. A thin gold chain necklace with a small round pendant resting on the collarbone, small gold hoop earrings. Real skin texture with pores, fine lines and natural imperfections, no retouching, not a model — an ordinary woman from Minas Gerais. Shot on 85mm portrait lens, shallow depth of field, soft cinematic key light with gentle fill.

Right panel — full-body front and back views side by side: the same woman shown twice within this panel — on the left, a full-body front view facing the camera; on the right, a full-body back view photographed from directly behind. In both, she stands in a neutral relaxed pose, arms resting at her sides with hands relaxed and fingers together, full height in frame head-to-toe, average build. Outfit: dusty-rose linen button-up blouse with sleeves rolled to the forearms, dark blue straight-leg jeans, simple tan leather flat sandals, the same thin gold necklace and small gold hoop earrings; no logos, no text. Both figures matched in framing, scale and lighting for consistency. Shot on 35mm lens, even full-length lighting.

Look: clean studio character sheet, plain solid grey background, consistent character across all views, soft diffused cinematic lighting, natural skin tones, fine detail, vertical divider line separating each view.
```

Use the template's light wording, not the example's: the example came with the director's note that
the whole scene must stay bright, so the template adds the bright-face clause, the light-grey
background and "bright and clean overall exposure with no deep shadows".

## Rules for filling it

- **Post-production step (always, by the director): the heads in the full-body views are blurred
  or removed after generation**, so the only face in the sheet is the left close-up and the video
  model never has two faces to choose from. Headless full-body panels in a delivered sheet are
  intentional — never flag them as a defect, and in shot prompts the sheet's identity comes from the
  close-up while the full-body views supply build, wardrobe and gear.

- **Prose, in this order:** who → skin → hair → face shape, nose and lips → eyes and brows → facial
  hair or makeup → expression
  → accessories → marks → the realism line → lens and light. Keep the whole prompt around 250–400
  words; long lists fight the image.
- **The expression comes from the personality.** One sentence: the expression plus "the face of
  someone who…". Keep it mild and readable (a hint of a smile, amused eyes, a calm steady look) — a
  big laugh or an open mouth distorts the identity the sheet must lock. Match the film's register: a
  warm institutional film gets warm faces; a thriller can get a guarded one.
- **The entire head is always in the close-up**, hair and any headgear included. Never "forehead to
  chin".
- **Light: bright first, texture second.** The key has a side so pores, fine lines and hair strands
  read, but the sheet stays light and clean; at most one side of the face slightly darker. Never
  "dark", "moody", "low-key" or "dramatic" in a character sheet — the film's look belongs to the shot
  prompts, not to the reference.
- **The realism line stays:** "Real skin texture with pores, fine lines and natural imperfections, no
  retouching, not a model — an ordinary [person] from [place]." Drop "not a model" only when the
  character is a model or a star. For a child or teenager drop "fine lines", which ages young faces:
  "Real child's skin texture with fine pores and natural imperfections, no retouching, not a child
  model" (a teenager: "Real teenage skin texture with pores and natural imperfections, no retouching,
  not a model").
- **Accessories:** those visible in the close-up (earrings, necklace, glasses, headgear) are
  repeated in the Outfit line as "the same …" so the full-body views confirm them. Those the close-up
  cannot show (a watch, a ring, gloves) are written once in the Outfit line, without "the same".
  Small hand or body marks (a scar on a finger) go in the Hands asset (`asset-pipeline.md`), not in the
  sheet.
- **Face structure is identity.** Always state face shape, nose and lips; two characters of similar
  age and origin must differ there, or the model returns look-alike faces.
- **Wardrobe is the base state** of the character, written exactly as the shot prompts describe it;
  other states (wet, wounded, uniform change) get their own sheet and tag (see `asset-pipeline.md`).
- **No NEGATIVE block by default.** "no logos, no text" lives inside the Outfit line. If a specific
  drift keeps recurring in tests (a cap appearing, the wrong colour), add one short positive sentence
  that fixes it ("bare head, no cap") rather than a list.
- If an approved face image already exists, attach it and add after the first sentence: "The face in
  every view is exactly the face in the attached reference image." The text still restates the
  critical details.

## Adapting the template (keep its skeleton, change only what the request needs)

The skeleton that never changes: **the split-frame declaration · the close-up panel with the entire
head · the expression from personality · the realism line · the two matched full-body views · lens
per panel · bright soft cinematic light · plain light-grey background · the Look line.**

| Request | Adapt |
|---|---|
| **Stylized 3D / animation / art style** | Replace "photorealistic" and the realism line with the exact style ("stylized 3D render, Pixar-like proportions, not a photograph"); describe skin and materials in that medium's terms; drop "not a model". |
| **Extra views** (profile, ¾, headgear) | Keep the two panels so the face keeps half the frame. Add the view inside the right panel ("the same woman shown three times within this panel — on the left a full-body front view, in the middle a full-body left-profile view, on the right a full-body back view") or swap one view ("on the right, a full-body left-profile view"); keep "matched in framing, scale and lighting". Hands, a tattoo or a ring go in a separate close-up asset (`asset-pipeline.md`, Hands), not in the sheet. If the user explicitly asks for them in the sheet, put them inside the right panel or in place of the back view, never as a third panel. |
| **Non-human** (animal, creature, robot) | The close-up panel shows the head with the same "entire head, nothing cropped"; front/back become front/rear or side views as the anatomy demands; the expression line describes the creature's resting attitude. |
| **No face** (masked, helmeted) | The close-up shows the entire mask or helmet, nothing cropped; describe it in the same words in the close-up and in the Outfit line, and write "the same masked [person]" in the right panel. |
| **Uniform with safety gear** | The headgear is part of "the entire head"; glasses stay clear so the eyes read. |
| **Different aspect ratio or layout** | The sheet stays 16:9 whatever the film's ratio; change it only on explicit request. For a vertical sheet, stack the panels: "two panels stacked, divided by a thin horizontal line", "Top panel" / "Bottom panel", and "horizontal divider line" in the Look line. |
| **White or pale-grey wardrobe, or white hair** | Use a plain solid medium-grey background so the silhouette, fabric folds and hair edges separate; everything else unchanged. |
| **Coloured or environment background requested** | Only if the user asks; keep it flat and identical across panels so it doesn't leak into later shots. |
| **Darker or coloured light requested** | Only on request, and identical across all views. |

Every adaptation is stated explicitly in the prompt — never leave the template's original wording in
place when it contradicts the request (e.g. "photorealistic" in a cartoon sheet).
