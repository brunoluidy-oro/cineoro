# Character sheet — the standard template

This is THE template for every character sheet in the CINEORO tree. Always start from it. When the user
asks for anything different — a 3D character, a specific art style, an animal, a creature, extra
views, a different way of showing a feature (hands, tattoos, a costume detail, a profile), a different
aspect ratio — **keep the template and adapt it**; never replace it with a free-form prompt.

## Why it looks like this (production lesson, Oct 2026)

The previous template (three thin panels, "forehead to chin", neutral expression, flat even studio
light, a long NEGATIVE list) gave poor references: the face was small, the hair was cropped, the
expression was a mugshot, and the flat light erased skin and hair texture. The version below was
approved by the director on a real job and produced clean, usable sheets:
- **two panels**: the face gets half the frame; front and back share the other half;
- **the entire head in frame** — hair is identity;
- **a living expression drawn from the character's personality**, not a neutral stare;
- **cinematic but bright light**: enough direction to reveal pores and hair strands, yet the whole
  sheet stays light and clean — at most one side of the face slightly darker, never moody;
- **prose, not lists**, with a lens per panel (85mm face, 35mm full body) and no NEGATIVE block.

## The template (fill the brackets; keep every other line)

```
Cinematic character reference sheet, split-frame layout, photorealistic, two panels divided by a thin vertical line, [16:9].

Left panel — facial close-up: [a/an ORIGIN man/woman/boy/girl], [AGE] years old, the entire head fully inside the frame, nothing cropped. [SKIN: tone and texture]. [HAIR: length, colour, texture, grey strands, hairline]. [EYES and EYEBROWS]. [FACIAL HAIR or MAKEUP]. [EXPRESSION: one living expression drawn from the personality — "Warm, lively, slightly amused expression — the face of someone who …"]. [ACCESSORIES visible in the close-up]. [DISTINGUISHING MARKS that must stay consistent]. Real skin texture with pores, fine lines and natural imperfections, no retouching, not a model — an ordinary [person] from [PLACE]. Shot on 85mm portrait lens, shallow depth of field, soft cinematic key light from one side with gentle fill, the whole face bright and evenly readable — at most one side of the face slightly darker.

Right panel — full-body front and back views side by side: the same [person] shown twice within this panel — on the left, a full-body front view facing the camera; on the right, a full-body back view photographed from directly behind. In both, [he/she] stands in a neutral relaxed pose, arms resting at [his/her] sides with hands relaxed and fingers together, full height in frame head-to-toe, [BUILD]. Outfit: [GARMENTS with material, colour and fit], [FOOTWEAR], [the same ACCESSORIES]; no logos, no text. Both figures matched in framing, scale and lighting for consistency. Shot on 35mm lens, even full-length lighting.

Look: clean studio character sheet, plain solid light-grey background, consistent character across all views, soft diffused cinematic lighting, bright and clean overall exposure with no deep shadows, natural skin tones, fine detail of skin, hair and fabric, vertical divider line separating each view.
```

## Approved example (the one that set the standard)

```
Cinematic character reference sheet, split-frame layout, photorealistic, two panels divided by a thin vertical line.

Left panel — facial close-up: a Brazilian woman, 44 years old, the entire head fully inside the frame, nothing cropped. Warm light-brown skin, shoulder-length dark brown wavy hair with a few natural grey strands, expressive dark brown eyes with soft laugh lines, natural eyebrows, light everyday makeup. Warm, lively, slightly amused expression — the face of someone quick to comment and quick to laugh. A thin gold chain necklace with a small round pendant resting on the collarbone, small gold hoop earrings. Real skin texture with pores, fine lines and natural imperfections, no retouching, not a model — an ordinary woman from Minas Gerais. Shot on 85mm portrait lens, shallow depth of field, soft cinematic key light with gentle fill.

Right panel — full-body front and back views side by side: the same woman shown twice within this panel — on the left, a full-body front view facing the camera; on the right, a full-body back view photographed from directly behind. In both, she stands in a neutral relaxed pose, arms resting at her sides with hands relaxed and fingers together, full height in frame head-to-toe, average build. Outfit: dusty-rose linen button-up blouse with sleeves rolled to the forearms, dark blue straight-leg jeans, simple tan leather flat sandals, the same thin gold necklace and small gold hoop earrings; no logos, no text. Both figures matched in framing, scale and lighting for consistency. Shot on 35mm lens, even full-length lighting.

Look: clean studio character sheet, plain solid grey background, consistent character across all views, soft diffused cinematic lighting, natural skin tones, fine detail, vertical divider line separating each view.
```

## Rules for filling it

- **Prose, in this order:** who → skin → hair → eyes and brows → facial hair or makeup → expression
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
  character is a model or a star.
- **Accessories appear in both panels** ("the same thin gold necklace") so the full-body views
  confirm them.
- **Wardrobe is the base state** of the character, written exactly as the shot prompts describe it;
  other states (wet, wounded, uniform change) get their own sheet and tag (see `asset-pipeline.md`).
- **No NEGATIVE block by default.** "no logos, no text" lives inside the Outfit line. If a specific
  drift keeps recurring in tests (a cap appearing, the wrong colour), add one short positive sentence
  that fixes it ("bare head, no cap") rather than a list.
- If a reference image exists, it supplies identity; the text still restates the critical details.

## Adapting the template (keep its skeleton, change only what the request needs)

The skeleton that never changes: **the split-frame declaration · the close-up panel with the entire
head · the expression from personality · the realism line · the two matched full-body views · lens
per panel · bright soft cinematic light · plain light-grey background · the Look line.**

| Request | Adapt |
|---|---|
| **Stylized 3D / animation / art style** | Replace "photorealistic" and the realism line with the exact style ("stylized 3D render, Pixar-like proportions, not a photograph"); describe skin and materials in that medium's terms; drop "not a model". |
| **Extra views** (profile, ¾, hands, a tattoo, headgear) | State the count up front ("three panels: close-up, front and side, back") or swap a view ("on the right, a full-body left-profile view"); keep "matched in framing, scale and lighting". Hands get their own close-up panel when they act on screen. |
| **Non-human** (animal, creature, robot) | The close-up panel shows the head with the same "entire head, nothing cropped"; front/back become front/rear or side views as the anatomy demands; the expression line describes the creature's resting attitude. |
| **No face** (masked, helmeted) | The close-up shows the mask or helmet; the identity lock refers to it. |
| **Uniform with safety gear** | The headgear is part of "the entire head"; glasses stay clear so the eyes read. |
| **Different aspect ratio or layout** | Change only the ratio in the first line and the panel arrangement; keep both panels' content. |
| **Coloured or environment background requested** | Only if the user asks; keep it flat and identical across panels so it doesn't leak into later shots. |
| **Darker or coloured light requested** | Only on request, and identical across all views. |

Every adaptation is stated explicitly in the prompt — never leave the template's original wording in
place when it contradicts the request (e.g. "photorealistic" in a cartoon sheet).
