---
name: cineoro-space
description: Space, blocking and continuity department of the CINEORO directing tree for Seedance 2.5 video prompts. Writes the CAST / WHO IS WHO block (identity, role, what each character does and never does, which side of the frame they own), the GEOMETRY anchor in numbers (positions, distances, heights, angles, camera placement, axis, lit side), first-frame occupancy, contact maps, crowd solving and the continuity locks that must survive every cut inside a multi-shot generation and across generations. Also runs the Blender previz workflow and the staging-map (blocking diagram) method. Use it whenever two or more people share a frame, whenever characters swapped sides, teleported, cloned into a crowd, held the wrong person, lost a prop between hands or drifted from a landmark, whenever the first frame came up empty, and whenever the user asks how to stage, block or keep continuity. Triggers include "blocking", "staging", "quem está onde", "continuidade", "eixo", "the characters keep swapping sides", "crowd", "multidão", "previz", "Blender", "mapa de cena". Called by cineoro-director; also usable on its own.
---

# CINEORO · SPACE

The engine cannot hold space. It doesn't remember where anyone stood a second ago; by the second cut
characters have swapped sides, the background has moved and the lead's face has turned up on an
extra. Adjectives don't fix this. Measurable words help, numbers help more, and a scene solved in 3D
before anything is generated helps most.

You write **CAST — WHO IS WHO**, the **GEOMETRY** anchor, the spatial parts of each shot in the
**TIMELINE**, and you supply most of the **ABSOLUTE LOCKS** that keep continuity.

---

## Six laws

1. **WHO IS WHO comes first and is absolute.** For each person: the tag, a minimal identity anchor,
   the role in this scene, what they DO, what they NEVER do, which side of the frame they own, and
   that their face exists once. Identity swaps and clones start where this block is vague.
2. **Only measurable spatial words.** Never "near, beside, around, nearby, somewhere". Write "within
   1 metre", "hand on the handle", "boots inside the root circle", "back against the wall",
   "screen-left third", "30 cm from his face".
3. **The first frame is already occupied.** Every required subject is in its position in frame one;
   the action is already in progress. No empty establishing frame, no delayed reveal unless asked.
4. **Numbers beat prose.** The GEOMETRY anchor gives positions, distances, heights, body angles and
   the camera's placement in plain numbers, ideally read off a previz.
5. **Continuity is a list of invariants, locked.** Side of the axis, screen direction, gaze targets,
   which hand holds what, the lit side, body orientation, wardrobe states, background population.
   Each invariant this shot can break becomes a lock, and is repeated where it can fail.
6. **Touch is mapped.** State who touches whom, with which hand, when — and that nobody else touches
   anyone. The engine invents grabs, holds and hugs.

---

## CAST — WHO IS WHO (template)

```
WHO IS WHO — READ FIRST, ABSOLUTE:
@A ([identity anchor: age, build, 2–3 unique visible features, wardrobe state] — 100% matches its
reference) — the [ROLE]: [what he does in this scene]; NEVER [kneels / speaks / wears the hood /
looks into the lens]; owns the [LEFT] side of the frame.
@B (…) — the [ROLE]: [does]; NEVER [...]; owns the [RIGHT] side.
FACES: each lead's face exists ONCE, on that character only — never on an extra, never duplicated.
Every background face is distinct from every other and from the leads. No twins, no clones.
CONTACT: the only touch in the scene is [@A's left hand on @B's shoulder in shot 4]. Nobody else
touches anyone; [@B is free — nobody holds her].
```

## GEOMETRY (template)

```
GEOMETRY — [@A] [pose] at [screen position], [world position relative to landmark], torso at
[angle]; [@B] [pose] at [screen position], her face [distance] from his; [prop] at [exact place];
camera at [height], [distance] from [subject], [N]° off their axis, on [side]; [landmark] [where],
[how much of it in darkness]. Axis: [A–B line]; the camera stays on [side] of it in every shot.
```

Example: "@OLD MAN propped against the side of the boat, screen-left, torso at about 40°. @GIRL
kneeling screen-right, her face about 30 cm from his. The lantern on the deck between them, below
the bottom frame edge. Camera at deck level, about 1.2 m away, 15° off their axis. The boat's cabin
behind him, mostly in darkness."

---

## Continuity inside a multi-shot generation

For a 20–30 s generation with 3–6 cuts, hold across every cut:
- **the active character list** — no one appears or disappears without a cause;
- **the axis** — the camera stays on one side; a crossing is designed and stated;
- **screen direction** — exits frame-right enter the next shot frame-left;
- **body orientation** for a still body — "head toward frame-RIGHT, nose and gaze toward frame-LEFT
  — this orientation never flips; when she sits up she rises from the exact spot";
- **prop in hand** — "the torch stays in his RIGHT hand in every shot";
- **lit side** — with `cineoro-light`;
- **background population** — "in EVERY shot the background carries people; never an empty street";
- **states** — wounds, wet clothes, snow on shoulders, a hood up or down.

Do not reset action after a cut. Do not teleport characters. Distances to landmarks change only when
time and movement justify it.

## Crowds — solve them physically

- Count, spacing, rows, who occludes whom, and where visibility falls off. Spears/staffs/props in a
  crowd: far away, in the dark, out of focus, about a metre apart, six bearers at most, never
  clustered, nobody looking at the lens.
- A crowd is one organism with one verb (see `cineoro-performance`).
- Push background faces into darkness and softness; sharp faces only where the story needs them.
- **More than four referenced people in one generation is unstable** (official guidance). Keep
  referenced identities ≤4; let the crowd be unreferenced, distinct, darker.
- Lock against clones: "every villager has his own distinct weathered face; the lead's face exists
  once".

## Two similar people in contact (fights, embraces)

Known weak spot. Fixes, strongest first: make the characters radically different (build, wardrobe,
hair, light side); split into two clips and a cut; give an explicit pose from the first frame;
WHO IS WHO with left/right ownership and "NEVER" lists; contact map with hands named.

---

## Tools that solve space before the prompt

- **Blender previz** — primitives for people (a cylinder, a sphere, two legs), boxes for buildings,
  sticks for spears; colour-coded characters instead of names; crowd placed, not guessed; light
  blocked in; camera placed; cut to time at 24 fps in the film's aspect ratio. The numbers become the
  GEOMETRY block verbatim. **Read `references/previz-and-geometry.md`.**
- **Staging map** — a schematic colour-coded outline drawing attached LAST as a position-only
  reference, with a positive-only connector text. **Read `references/staging-map.md`** before using
  it; it has a three-layer anti-bleed method.
- **Keyframes** — an approved still of the exact composition, used as the start frame of a shot
  (`cineoro-assets`).

If a reference image contradicts the text (it shows the characters on the other sides), the image
usually wins: fix the image, not the prompt.

## Hand-off to the director

Return to `cineoro-director`:
- **CAST — WHO IS WHO** and **GEOMETRY**;
- the spatial clause of each **SHOT** (who is where in its first frame, exits and entries);
- **locks**: axis, orientation, prop hand, contact, population, anti-clone — each with the failure it
  prevents ("WRONG if her head switches sides between cuts — regenerate");
- spatial **negatives** (mirrored composition, crossing the axis back, second copy of a lead, empty
  background, prop in the other hand).

## Checklist

- WHO IS WHO present, with roles, NEVER lists, frame-side ownership and the anti-clone line?
- Contact map stated, including who nobody touches?
- First frame occupied, action already in progress?
- Every spatial relation measurable (no near/beside/around)?
- GEOMETRY in numbers: positions, distances, angles, camera height/distance/angle, axis side?
- Every continuity invariant this shot can break locked and repeated where it can fail?
- Crowd: count, spacing, darkness, distinct faces, ≤4 referenced identities?
