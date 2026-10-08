---
name: "project-[slug]"
description: "Project skill (bible) for [TITLE], a [runtime] [format] in [aspect ratio], generated with Seedance 2.5. Use whenever writing or revising a video prompt, shot, scene, voice line or asset for [TITLE] — including any request mentioning [CHARACTER 1], [CHARACTER 2], [LOCATION 1], [LOCATION 2] or [a key object]. Holds the verbatim look templates, the @TAG registry, cast and voice locks, props with their functions, world rules, project negatives and anti-AI-tell rules, reference prompts, the script and the director's statement. Always used together with cineoro-director."
---

# [TITLE] — PROJECT SKILL

*[Title meaning / epigraph, if any.]*

[One paragraph: what the film is — runtime, aspect ratio, how it is made (every frame generated?),
how speech works (characters speak on camera in [language]? no dubbing?), the one technical promise
that matters most.]

## How to use this skill

When asked for a shot or a scene, in order:
1. **Plain-language header first** — what happens, what is said, how long each beat runs, how it
   ends. Four lines. If the shot can't be written there, it isn't designed yet.
2. **Write the prompt in the CINEORO spine** (`cineoro-director`), pasting this file's templates
   **verbatim** (§1.3) and tags (§1.2).
3. **Check it** against the anti-AI-tell rules (`cineoro-realism` + §2 here) and add this project's
   negatives (§5).

Language rule: **the prompt is in English; spoken lines stay in [language/script] and are never
translated or romanized inside the prompt.**

## The tools

[Model/platform and settings] — all video and speech. **Claude + this skill + cineoro-director** —
every prompt. [Previz tool] — geometry, blocking, the numbers for GEOMETRY. [Image model] — assets.

## The point of the project

[The believability target: what the audience must believe — usually behaviour: how people use
things, move, speak. Everything in this file serves it.]

---

# 1 · THE PROMPT

## 1.1 Spine and always-on blocks

The CINEORO spine (CONTRACT → REFERENCES → CAST → SCENE & SOUL → LOCKS → TIMELINE → DIALOGUE →
ACTING → CAMERA → GEOMETRY → PHYSICS & MATERIAL → LIGHT → FILM LOOK → SOUND → WORLD → NEGATIVE →
ORDER). In this project these conditional blocks are **always on**: [e.g. WORLD, DIALOGUE].

**Every prompt is an island.** Light, optics, wardrobe, props, voice and geometry are re-specified
from scratch in every shot. "Same as the previous shot" is an instruction to something with no
*before*.

## 1.2 Naming — the @TAG registry

```
[@CHAR1] [@CHAR2] [@ANIMAL]
[@PROP1] [@PROP2] [@PROP3]
[@LOC1_NIGHT] [@LOC1_DAWN] [@LOC2]
```
One element, one name — identical in the asset, the prompt and the table. A change of state gets a
**new tag** (`[@CHAR1_WET]`), never an overwrite. Full registry: `references/asset-registry.md`.

## 1.3 Verbatim templates — paste, never rewrite

**CONTRACT line pattern:**
```
Live-action photoreal film, [aspect], [N]s, [N] shots / [N] cuts, [camera language], [real-time],
dialogue as spoken audio in [language], NO music, NO subtitles.
```

**FILM LOOK:**
```
[frozen block]
```

**LENS LOOK:**
```
[frozen block]
```

**LIGHT — base for [world/time 1]:**
```
[frozen block]
```

**LIGHT — base for [world/time 2]:**
```
[frozen block]
```

**NO LENS FLARES:**
```
No lens flares, no light streaks, no floating bokeh orbs, no glow overlays. Every light source stays
small and contained within itself.
```

**WORLD:**
```
WORLD: [place, period] — [materials that exist]; NO [what doesn't exist]. [Daily-life rule].
```

**Standing NEGATIVE spine for this project:**
```
[the CINEORO spine adapted: remove what this film wants, add the world's anachronisms]
```

*Artifact note: if the engine produces banding or ghosting, remove "gate weave" and "chromatic
aberration" together and keep grain moderate.*

## 1.4 Props master list

- **[@PROP]** — [material, geometry, wear]. Function: [what it is for, who uses it, how]. [Carries
  more than itself? — lock harder.]
- …

---

# 2 · PROJECT ANTI-AI-TELL RULES

> Realism is what you subtract, not what you add.

[Rules learned on this project, each with the failure it prevents and the date it was added. Start
with the world-specific ones; the general catalogue lives in `cineoro-realism`.]

1. …

---

# 3 · VOICES AND PRONUNCIATION

[Language, accent, script rule. Pronunciation notes for hard sounds.]

```
VOICE LOCK — [@CHAR1]:
[verbatim profile]

VOICE LOCK — [@CHAR2]:
[verbatim profile]
```
Audio references: [@CHAR1_VOICE] = [file], bound to [@CHAR1] only.

---

# 4 · REFERENCE PROMPTS

## 4.1 The model prompt

[One complete prompt in the CINEORO spine for the film's most typical scene, with every verbatim
template pasted.]

## 4.2 Scene types for this film

Adapt the model prompt by changing [the blocks that change]:
**A · [type]** — [what changes]. Negative: […].
**B · [type]** — …

---

# 5 · NEGATIVE LIBRARY — PROJECT ADDITIONS

**[Scene type / object]:** […]
**[The object the engine keeps misdrawing]:** don't name it — describe the geometry: [...]. Scale:
[...]. Negative: [...].

---

# 6 · STRUCTURE AND SCRIPT

## Blocks / acts
[Each with its event.]

## Motifs and rhymes
[The gesture first and last; the line that changes meaning; the loop; the colour used once.]

## Dialogue
[Lines in the original language, with translation in italics for the director only — never pasted
into prompts.] Full script: `references/script.md`.

---

# 7 · CAST

**[@CHAR1] ([name]), [age].** [Look, build, marks, wardrobe and its state]. Hands: [size, marks,
condition — two characters' hands that touch must never look alike]. Temperament: [...]. Super-
objective: [...]. Never: [...].

---

# 8 · ACTING NOTES FOR THIS FILM

**The principle:** the actor is invested in a TACTIC in service of a GOAL and never plays an emotion
(`cineoro-performance`).
[Per character: how their state is played as concrete tactics; contrast pairs and the essential axis.]

---

# 9 · LANGUAGE   *(only if invented)*

[Sound design of the language; script choice and why; the rule "one word, one meaning, no synonyms";
dictionary and grammar in `references/language.md`; the lines that carry the film.]

---

# 10 · DIRECTOR'S STATEMENT

**The idea.** […] Pitch anchor: "[…]".
**Visual language — functional, not stylistic.** [Each choice → the story mechanism it serves.]
**Camera.** [When low angle, when canted, when still, when it walks.]
**Editing.** [Observed vs authored; where the film switches.]
**Light and colour.** [Permanent state, man-made exception, the colour used once.]
**Sound.** [Score policy; what replaces music; silence as an instrument.]
**Daily life.** [Processes shown in full; objects with function; movement as mechanics.]
**The motif.** […]

---

# 11 · PRODUCTION NOTES

**Assets.** [Status table: built / to build. Face anchors generated once; states via masks.]
**Runtime.** [Ceiling; what compresses; what is never cut.]
**Generation settings.** [Model · resolution · aspect · audio on · duration = timeline sum · draft
first for blocking.]
**Order of work on a shot.** Event and tactic → geometry (previz) → prompt in the spine → draft →
check → fix the one block that failed → final.
