---
name: cineoro-assets
description: References and assets department of the CINEORO directing tree for Seedance 2.5. Builds reference assets (face anchor, turnaround, props on neutral ground, location plates, voice clips) under one @TAG convention, writes the REFERENCES block giving each attached image, video or audio exactly one job (identity, keyframe for shot N, world, object only, voice, motion, previous take) plus a scope of what to ignore, and runs the iteration loop - keyframes from approved takes, draft then final, timestamped edits, extensions. Use it whenever a prompt attaches references; when identity drifted, a face swapped, a reference's background or light leaked in, or a take needs fixing without regenerating everything; and when the user asks how to make character sheets, Elements, keyframes or reference images for Seedance or Higgsfield. Triggers - "referência", "character sheet", "keyframe", "@image", "identity drift", "refazer o take", "extend", "edit video". Called by cineoro-director; also usable alone.
---

# CINEORO · ASSETS

An asset is a pair: **text + image** (or text + audio). The image is what the engine anchors identity
to; the text is what tells it how to use the image and what to take from it. Nothing is shot until
every character, location and important object is named, built and locked.

You write the **REFERENCES** block (and its SCOPE), the minimal identity anchors used in **CAST**, the
**generation card's attachment list**, and you run the **iteration loop** after a take comes back.

---

## Seven laws

1. **Assets first.** No shot until every character, location and prop that matters has a tag, an
   image and a text descriptor.
2. **One element, one name.** The same `@TAG` in the asset library, in the prompt and in the shot
   table. A change of state gets a **new tag** (`@MARIA_WET`, `@MARIA_BLOODIED`), never an overwrite.
3. **The face is generated once, in close-up, and never regenerated.** The base portrait never runs
   through a model again; every state (dirt, frost, a wound) is built around it with masks, so the
   identity and its skin texture survive every version. The look (full figure, wardrobe) is built to
   the locked face.
4. **Every reference has exactly one job,** stated in the REFERENCES block: identity, keyframe for
   shot N, world, object only, voice, motion, or previous take. A reference without a stated job
   leaks everything it contains.
5. **Scope what a reference must NOT give.** Identity and object references bring their own
   background, light and grade; say they supply faces/wardrobe/objects only and that their backdrop,
   sky, weather, lighting direction, exposure and colour are ignored.
6. **Text keeps the image honest.** Keep the character text minimal (long appearance text fights the
   image), but state in words the critical details the engine may drop (a tattoo, a logo, a colour,
   a missing finger, which hand holds what).
7. **Approved output becomes the next input.** Frames from approved takes become keyframes and look
   anchors; clean lines become voice references; approved clips become extension sources.

---

## REFERENCES — template

```
REFERENCES (Seedance 2.5) — each reference has ONE job:
[ref] — IDENTITY of @NAME: face, [tattoos/marks], hands, build, wardrobe ([state]). 100% matches.
[ref] — KEYFRAME FOR SHOT 1: shot 1 STARTS from this exact frame ([one-line description of it]) and
comes alive from it.
[ref] — KEYFRAME FOR SHOT 3: …
[ref] — WORLD: [location]'s architecture, materials and clutter — the world for shots [N–M].
[ref] — OBJECT ONLY: [the prop] — shape, scale, material, wear. Ignore its background.
[ref] — VOICE of @NAME ONLY: [3-word description of the voice]; all other sound generated fresh.
[ref] — MOTION ONLY: [the movement/camera move] — nothing else is taken from it.
REFERENCE SCOPE: identity and object references supply faces, wardrobe, build, hands and objects
ONLY — IGNORE their backdrops, ground, sky, weather, lighting direction, exposure and colour grade.
Shots that start from a keyframe inherit its light, grade and skin texture; shots [N–M] continue
that exact look with no keyframe.
```

`[ref]` is the platform's token for that attachment. Syntax differs by platform:
**`references/reference-usage.md`** (BytePlus `@Image 1`, fal `@Image1`, Replicate `[Image1]`,
Higgsfield `@` mentions of uploads and Elements). Use one convention per project.

Official 2.5 phrasing for keyframe chains also works: "Use Images 2 to 4 in order as keyframes."

---

## Limits and stability (Seedance 2.5)

- Up to 30 images, 10 videos, 10 audio clips (videos and audio each ≤30 s in total), 50 references
  overall. Using fewer, better references is more stable than filling the limits.
- **Referenced subjects:** 1–8 from images is the stable range (9–12 less so); for people, **more than
  four referenced identities in one generation is unstable**.
- **Upload order = order of first appearance**, and bind the name to its reference every time it is
  mentioned.
- Multi-view character sheets (turnarounds) are supported as references in 2.5.
- Downscale reference images to roughly the output resolution — oversized references can print
  fingerprint-like textures.
- Some providers block uploads of real human faces; build characters from generated or authorized
  portraits.

---

## Which generation mode (decision)

| Situation | Mode |
|---|---|
| New angle on a known character, no matching still | text + identity references (no keyframe) |
| A specific composition must be hit | keyframe (approved still) as the shot's start frame |
| A wide derived from a close reference | build the wide still first, then animate it |
| Repeating a good shot one-to-one | keyframe from that take + the same angle, light and composition described in words |
| Two seconds of a good take are wrong | timestamped **edit** of that take, rest unchanged |
| The take is good but ends too early | **extend** forward from it |
| Testing blocking/timing cheaply | **draft** (480p) → finalize the same draft to 1080p |

**Character sheets** always use the standard template in **`references/character-sheet.md`**,
adapted (never replaced) for 3D, art styles, creatures or other views.

Full iteration loop, chaining, edit/extend wording and the draft workflow:
**`references/reference-usage.md`**. How to build each asset (face anchor, turnaround, props,
location plates, state variants, voice clips) with ready image prompts:
**`references/asset-pipeline.md`**.

---

## Hand-off to the director

Return to `cineoro-director`:
- the **REFERENCES** block with SCOPE;
- one-line **identity anchors** per character for CAST (age, build, 2–3 unique features, wardrobe
  state, "100% matches its reference");
- the **attachment list** for the generation card, in upload order, each with its role;
- the next **iteration step** when a take is being repaired (edit / extend / keyframe / regenerate).

## Checklist

- Every attached file has one job in REFERENCES, and the SCOPE excludes what it must not give?
- Every `@TAG` used is present in this shot; no stale tags from other shots?
- Upload order matches order of first appearance?
- ≤4 referenced people; critical details restated in words?
- Keyframes bound to the shot they start; non-keyframed shots told to continue the look?
- State changes use new tags, base faces untouched?
