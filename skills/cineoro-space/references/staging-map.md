# Staging map — position reference as character disposition

Read when the user attaches a frame and asks for a staging reference, or when characters keep jumping
seats and swapping places between shot sizes. Output: a diagram-generation prompt (for an image model)
plus a connector block to paste into the video prompt's references. Origin: the `cinedance`
blocking-map method; kept intact because it works.

**Contents:** what it is · three-layer anti-bleed · two-step workflow · step-1 template · step-2
connector · tag naming · rules · known failures · QA · extensions · storyboards in 2.5

---

## What it is

A deliberately schematic, colour-coded OUTLINE drawing fed to the video model alongside the real
location and character references. It tells the model WHO IS WHERE — nothing else. It carries maximum
geometry with minimum style mass, because style bleed from the map into the shot is the method's
known enemy.

## The three-layer anti-bleed architecture

1. **IMAGE:** figures are thin muted-colour OUTLINES, no fills, no colour blocks. The grid is faint —
   an authoring tool, not a signal to the model.
2. **TEXT:** the connector is written in POSITIVE form. Models are weak at negation — "no flat
   illustration, no vector shapes, no grid" still injects *flat, vector, grid* and primes the very
   style being banned. The connector never names the map's graphic style; it only asserts where style
   DOES come from. Graphic vocabulary exists only in the diagram GENERATION prompt, which never
   touches the video context.
3. **STRUCTURE:** the staging reference is attached LAST, after location and character references,
   so the photo references dominate the style vote.

## Workflow — two steps, in order

**STEP 1 — the user uploads a frame → deliver the diagram prompt.** The source image is attached to
the diagram generation as a COMPOSITION-ONLY guide (framing, angle, crop, positions, poses, scale);
its photographic look must not be copied; nothing may be added; cropped bodies must not be completed.
Translate every character's position, pose, facing and anchoring geometry into explicit text as well.
Deliver together: (1) the diagram prompt; (2) the tags — `@staging_[PROJECT]_[scene]_[version]` for
the result and `@loc_[PROJECT]_[name]_[scene]_[version]` for the source frame; (3) a one-line colour
key ("BLUE = the captive soldier, centre-foreground"). Don't move to step 2 until asked.

**STEP 2 — when asked, deliver the connector block**, where the user binds each letter to their
character tag. Letters exist ONLY in the prompt text; the map carries only colours.

## STEP 1 template — the diagram prompt

```
[Attached image] — use the attached image ONLY as the compositional guide: copy its exact framing,
camera angle, crop, and the positions, poses and scale of every person — but do NOT copy its
photographic look: no photo textures, no realistic lighting, no realistic faces, no colours from the
image. Do NOT add anything that is not in the attached image. Do NOT complete cropped bodies — if a
body part is cut off by the frame edge in the image, cut it off in the drawing. The OUTPUT is a flat
schematic:
Flat minimalist technical LINE DRAWING, a staging plan for a film scene — an obviously schematic,
non-photographic drawing on a white background with a very faint, thin, light-grey graph-paper grid.
Figures are clean THIN OUTLINES in muted colours — NO fills, NO solid colour blocks, NO shading, NO
texture, NO realism, NO text, NO letters, NO labels anywhere.
Front view matching the attached image's framing exactly: [N] outline figures.
[Per figure: POSITION IN FRAME — a MUTED-COLOUR outline figure, what is visible (full body / head and
shoulders / torso and arms), pose exactly as in the image, facing direction, any signature prop as a
simple outlined shape and exactly where it sits relative to the body.]
[Anchoring furniture/architecture as thin-outline shapes and where — or "open background".]
[Background extras as tiny faint grey silhouettes, exact area — or omit.]
Nothing else — no ground line, no extra props, no extra figures. Simple, readable, diagrammatic.
[Image-model parameters if your tool uses them, e.g. aspect ratio matching the source frame, a raw
style, low stylization; exclusion list: photorealism, photo texture, realistic lighting, realistic
faces, shading, solid colour fills, colour blocks, text, letters, labels, typography]
```

Notes: one muted, maximally distinct hue per figure (muted blue, orange, yellow, purple, red, green).
Check every time: cropped bodies described as cropped and forbidden from completion; head angle and
gaze spelled out; prop height pinned to anatomy ("across the throat, under the chin — not the
chest"); nothing added that isn't in the frame.

## STEP 2 template — the connector (paste into the video prompt's REFERENCES)

POSITIVE FORM ONLY. Never name the map's graphic style in the video prompt — not even as a negation.
One paste: the LOCKS paragraph is part of the connector.

```
@staging_[PROJECT]_[scene]_[version] — POSITION REFERENCE ONLY
Use this reference solely to read where each figure is placed, its pose, and its facing direction
inside @loc_[PROJECT]_[name]_[scene]_[version]. Every visual quality of the shot — style, light,
colour grade, faces, wardrobe, environment, props — comes exclusively from
@loc_[PROJECT]_[name]_[scene]_[version] and the character references. The shot is a fully photoreal
live-action frame.

LETTER LEGEND (letters exist only in this prompt; they do not appear on the reference)
@A = the BLUE figure on the staging reference = [character tag] → [spot, pose, facing].
@B = the ORANGE figure on the staging reference = [character tag] → [spot, pose, facing].

RENDER RULE: place the real, photoreal characters (from their own references) into the real location
at the positions this reference defines, and take nothing else from it.

LOCKS: All style, light and texture come exclusively from the location and character references;
the staging reference defines positions only. The colours on the staging reference identify WHO IS
WHO on that reference only — wardrobe and grading come from the character and location references.
Everyone stays in their staging-locked position until their scripted action.
```

ATTACHMENT ORDER: location and character references FIRST, staging reference LAST.

## Tag naming

`@loc_[PROJECT]_[name]_[scene]_[version]` and `@staging_[PROJECT]_[scene]_[version]`; PROJECT in
caps; bump `_v2`, `_v3` on every retake; reference only the active version per shot.

## Rules

- Letters live in prompt-space, colours live in image-space. No typography on the map.
- One muted, maximally distinct colour per figure; outlines, never fills.
- Front view from the CAMERA's side, never top-down — video models think in frames, not floor plans.
- Pose is geometry, crop is geometry.
- The grid is for the author; never mention it in the connector.
- Never trade signal for stealth: reduce style mass (outlines, muted colour, faint grid), never the
  contrast of the figures.
- Small drawing inaccuracies are fine — the legend text overrides them.

## Known failures

- **Style bleed** — fix at all three layers (image, text, structure). If bleed persists in a
  moving-character shot, keep movement language plain and physical ("real, live-action gestures"),
  never "come alive"; last resort, drop the map from that shot.
- **Colour → wardrobe bleed** (blue figure → blue tunic) — outlines, muted palette, legend routing
  identity to the character tag, wardrobe routed to character references.
- **Invented content** (completed crops, added helmets) — guard lines + per-figure crop description +
  put the invented item in the image model's exclusion list.
- **Prop at the wrong height** — pin to anatomy with a positive AND a contrast.
- **Stale staging tags** — reference only the active version.

## QA

On the diagram: thin outlines only; no text; crops stay cropped; props at the right anatomical place;
poses and framing match the frame. On the video: fully photoreal; no white/grid artifacts; no map
colours in wardrobe; no letters; every character in the mapped position until their scripted action.

## Extensions

- **Trajectory maps** — a dashed muted line per path (bullet, thrown object), bound in the legend with
  START, PATH, END and TRIGGER beat.
- **Camera path maps** — arrows, declared "arrows = camera path only".
- **Movement maps** — a dashed line for a character's cross, with start, end mark and the beat.

## Storyboards in Seedance 2.5

The official 2.5 guide accepts **multi-panel storyboards** (up to 15 panels, line art recommended) as
loose plot guidance. Use them for sequence order, not for exact positions; for exact positions use the
staging map or a keyframe.
