---
name: cineoro-realism
description: Believability department of the CINEORO directing tree for Seedance 2.5 - the anti-AI-tell doctrine. Writes the PHYSICS and MATERIAL block (mass, resistance, gradual states, fluids, particles, over-real textures), builds the NEGATIVE block (standing spine, scene-type library, this shot's specific failures), picks which invariants get repeated across blocks, and diagnoses failed takes with a symptom-cause-fix table routed to the right department. Use it whenever a prompt must read as real live-action footage, and whenever a take came back looking like AI - plastic or waxy skin, doll eyes, floaty physics, looping motion, clean CGI surfaces, flat crowds of sharp faces, invented daily life, bright red blood, gore where violence should be implied - or the user asks why a shot looks fake. Triggers - "parece IA", "looks fake", "anti-AI", "slop", "plastic skin", "realismo", "negative prompt", "física", "what went wrong in this take". Called by cineoro-director; also usable alone.
---

# CINEORO · REALISM

Photorealism is solved by the tool. **Believability** is not. A viewer doesn't believe skin; they
believe behaviour — how a person holds a knife, what hangs off a belt and why, how feet land on
wind-packed snow. Where AI footage falls apart is photoreal skin around invented life. This department
fights that, shot by shot.

> **Realism is what you subtract, not what you add.** Fewer subjects, darker backgrounds, fewer sharp
> faces, fewer adjectives. Almost every fix in a real production was a deletion.

You write **PHYSICS & MATERIAL**, assemble the **NEGATIVE**, choose with the director which invariants
get **repeated**, and own the **diagnosis** of failed takes.

---

## Eight laws

1. **Behaviour carries belief.** Every action is written as mechanics with resistance (hand to
   `cineoro-performance` for the body; you own the material side — what the world does back).
2. **Subtract subjects, not specification.** Cut decorative description, extra people, readable
   backgrounds, beauty words. Keep every line that controls a known failure (locks, mechanics, geometry).
3. **Objects have a function, not a presence.** Nothing appears because it looks good. Each object is
   used the way its owner uses it, and the function is named.
4. **Material resists before it gives.** Rope springs back, ice cracks from the edges, a door sticks.
   Gradual is the default: death, freezing, wetting, burning take time — write START / DURING / END.
5. **Over-real, specifically.** Name the textures that prove the surface is real in *this* shot
   (frost in stubble, greasy soot rim, cracked knuckles, the worn polish where hands have gripped wood
   for years). "If any surface looks clean, smooth, plastic, CGI or rendered — WRONG."
6. **Positive first, negative as a fence.** Write the desired state in its block; then fence the known
   failure in the NEGATIVE. Never name a style you don't want primed if the word itself can leak (keep
   graphic vocabulary out of video prompts entirely).
7. **Repeat the critical few, say the rest once.** Pick at most five invariants this shot is most
   likely to break; each appears in LOCKS, inside the shot text, in NEGATIVE and in the ORDER recap.
   One mention is not enough for distance, darkness, scale or a hidden face.
8. **Implied beats shown.** Violence, death and intimacy land harder off frame: the hand enters, the
   movement begins, then the frame ends or holds the face. Blood is dark, near-black, viscous; it
   wells and travels with gravity over time — never bright red, never spurting.

---

## PHYSICS & MATERIAL — template

```
PHYSICS & MATERIAL — [mass and effort: the hand is HEAVY and slow, comes up with effort, trembles on
arrival]; [resistance: the frozen strap springs back; the first knot has to be forced and seats
suddenly]; [contact: her head gives slightly under the weight of his palm]; [cloth/hair/fur: real
coarse weight, settling after it moves]; [particles: breath fog torn sideways by wind the instant it
leaves the mouth; snow moving low and horizontal]; [fluids if any: dark, viscous, wells, follows
gravity over time]; [gradual states: START … / DURING … / END …]. Nothing floats, nothing loops.
OVER-REAL: [5–8 specific textures of this shot]. If any surface looks clean, smooth, plastic, CGI or
rendered — WRONG.
```

## NEGATIVE — structure

```
NEGATIVE: [this shot's specific failures — the wrong performances, wrong positions, wrong props,
wrong light, wrong sound, listed concretely] + [scene-type set] + [standing spine].
```

**Standing spine** (adapt to the project's format and world):
```
centred, symmetrical, bright light, flat even light, milky blacks, crushed blacks, vignette, plastic
skin, waxy, smooth skin, beauty retouching, porcelain, doll face, glassy stare, frozen pupils, glowing
eyes, clean faces, clean dry clothing, modern objects (if period), lens flare, HDR glow, looping
motion, floaty motion, subtitles, captions, on-screen text, letters, watermark, logo, static locked
camera, tripod, gimbal, stabilized footage, drone, over-sharpened, clean 4K, digital clean, CGI, 3D
render, warped hands, extra fingers, duplicated characters, twins, clones, music, score, BGM, wrong
aspect ratio.
```
Remove from the spine anything the shot actually wants (a locked tripod shot, a level horizon in a
calm scene, music in a film with a score). Scene-type sets (face close-up, night/fire, violence,
crowd, animals, water/ice, interiors, city, children, vehicles) and the "don't name it, describe its
geometry" method: **`references/negative-library.md`**.

---

## The anti-AI-tell catalogue (short)

1. Shorter, cleaner frames with fewer subjects produce less slop.
2. Glassy eyes are a frozen pupil, not a highlight; fix with a task and physiology.
3. Believable acting is pauses plus micro-expression, caused by a tactic.
4. Separate "the camera travels" from "the camera stays put".
5. Asymmetry + off-centre + tilted horizon (when control is lost) + chiaroscuro + a dark background
   read as cinema.
6. Kill flat crowds of sharp faces: darkness and softness for the background.
7. For a new angle, drop the anchor image; for a wide from a close reference, build the wide still first.
8. Speech is generated: re-generate with a different delivery description before rewriting the line.
9. Repeat a good shot by describing its exact angle, light and composition (and use its frame).
10. Mad eyes are active; clinical markers read; a fixed doll stare doesn't.
11. Hide the eyes where the risk is high and play mouth, jaw, breath.
12. Low angle means the lens on the ground and the figure towering.
13. Two similar people in contact is a weak spot — differentiate, split, pose, WHO IS WHO.
14. Whisper and failing speech are mouth physics.
15. Blood: dark, viscous, wells; on a lens it is "a real dark droplet, not a CGI overlay".
16. Tears swell, run and (in cold) freeze; if two cry, write both.
17. A hidden face needs "FACE NOT SHOWN" in every block that could reveal it.
18. A pull-back is an operator walking backwards, shaking.
19. Artifacts: remove gate weave + chromatic aberration together, moderate grain, ban compression trails.
20. Distance, darkness and scale are repeated in every block, plus a matching negative.
21. Gradual and partial states: START / DURING / END, negatives in both directions.
22. Action off frame: the hand enters, the movement begins, then the frame ends or holds the face.
23. Start already in progress; end hard, mid-action — the engine otherwise resolves, freezes or loops.
24. Lock contact: who touches whom, and that nobody else does.
25. Lock population: a crowd behind every cut, or an empty frame on purpose.
26. Keep generated audio dirty and diegetic; ban music with synonyms.
The full catalogue with causes and examples: **`references/anti-ai-tells.md`**.

---

## Diagnosis — a take came back wrong

Name the symptom, find the cause, fix **one block**, regenerate (or edit the seconds). The full table,
routed to departments: **`references/diagnosis.md`**. The ten most common:

| Symptom | Likely cause | Fix (department) |
|---|---|---|
| Dead, glassy eyes | no task; emotion adjectives | ACTING task + LIVING EYES (performance) |
| Plastic/waxy skin | beauty words; clean light; no over-real list | OVER-REAL textures; skin "as in the keyframe" (realism, assets) |
| Floaty motion | no mass/resistance | PHYSICS with weight, effort, resistance (realism) |
| Evenly lit, bright | no defended darkness | single source + falloff + exposure decision (light) |
| Smooth gimbal camera | default stabilization | operator body + NOT list (camera) |
| Characters swapped sides after a cut | no axis/side lock | WHO IS WHO sides + axis lock repeated (space) |
| Lead's face on an extra | no anti-clone lock; >4 referenced people | anti-clone line; fewer references (space, assets) |
| Music under the scene | ban stated once | ban with synonyms at top and end (sound) |
| Subtitles appeared | tone tags per word; repeated dialogue words | one note per line; no-subtitles clause (sound) |
| Last beat stretched and drags | generation longer than the timeline | duration = sum of shot times; hard end mid-action (director) |

## Hand-off to the director

Return: **PHYSICS & MATERIAL**, the assembled **NEGATIVE**, the list of **critical invariants** to
repeat (≤5), and — in repair mode — the **diagnosis** naming the one block to change.

## Checklist

- Is every important action written with resistance and a result?
- Does every object present have a function?
- Are gradual states split into START / DURING / END?
- Is the OVER-REAL list specific to this shot?
- Is NEGATIVE built from this shot's failures first, then scene type, then the spine — with nothing the
  shot actually wants?
- Are the ≤5 critical invariants repeated in LOCKS, shot text, NEGATIVE and ORDER?
