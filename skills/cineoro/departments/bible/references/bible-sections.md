# Bible sections — how to fill each one well

**Contents:** description · the point of the project · verbatim templates · registry · props ·
project anti-AI-tell rules · voices · reference prompts · scene types · negatives · structure ·
cast · acting notes · language · director's statement · production notes · versioning

---

## Description (frontmatter)

It is how the project skill gets loaded, so it must name the project, the main characters, the main
locations and a key object — the words the user will actually type. Keep it under 1024 characters,
no angle brackets.

## The point of the project

One paragraph naming the believability target. Good: "Not photorealism — that is solved. Believability:
the viewer believes behaviour — how a person holds a knife, makes fire, what hangs off the belt and
why." Bad: "A beautiful cinematic film with stunning visuals."

## Verbatim templates

- Freeze them only after testing on 2–3 different scene types.
- Each template is self-contained (no "as above").
- Mark the KEY blocks (look, light, lens) — those are the ones that hold a film together across
  hundreds of generations.
- When a template changes, bump the bible version and note which shots predate it.

## Registry

Tags in caps with `@`; states as suffixes (`@NAME_WET`); locations with light state
(`@KITCHEN_DAWN`, `@KITCHEN_NIGHT`); voices as `@NAME_VOICE`; staging maps and location plates
versioned (`_v1`, `_v2`). One element, one name.

## Props master list

For each prop: geometry, material, wear, **function** (what it is for, who uses it, how), where it
lives on the body or in the space. Mark the 2–3 objects that carry more than themselves (the
instrument of the climax, the object passed between characters) — they are locked harder and appear
in the CAST block whenever present. Include a **safe fallback** for an object that generates badly
(e.g. a simpler tool that reads the same).

## Project anti-AI-tell rules

Start empty and grow from failures: each rule = the symptom seen + the fix that worked + the date.
Typical world-specific entries: an object the engine misdraws (geometry method), a wardrobe item that
drifts, a material that comes out too clean, a gesture that keeps turning into something else (a
nose-to-cheek greeting turning into a kiss).

## Voices

VOICE LOCK per speaking character (`cineoro-sound` format), plus pronunciation notes and the script
rule for each language. Two voices in the same scene differ on at least two axes.

## Reference prompts

One complete prompt per main scene type, written in the spine with all templates pasted. A good
reference prompt covers ~90% of the shots of its type: you copy it and change the details instead of
writing from zero.

## Scene types

Name 4–8 types the film actually has (quiet warm, implied violence, altered state, crowd, sensitive
partly hidden, extreme wide with scale, physical process, chase…) and say which blocks change and
which negatives are added for each.

## Negatives

World anachronisms; the objects the engine misdraws (with the geometry method); scene-type sets that
differ from the CINEORO library.

## Structure

Acts/blocks with their events; the loop or motif system; which scenes never get cut; which compress.
Dialogue in the original language with translations for the director only.

## Cast

Per character: tag, name, age, look, build, marks, hands, wardrobe and its states, temperament,
super-objective, arc, what they never do, the voice tag. Hands deserve their own line.

## Acting notes

How each character's state is played as tactics (an "absent" character as competent actions in the
wrong world; a grieving one as holding still). Contrast pairs with the essential axis.

## Language (invented)

Sound design → script choice and why → pronunciation notes → "one word, one meaning, no synonyms" →
dictionary by semantic field → grammar (affixes, word order) → the few lines that carry the film.
Coin a word once; never vary it.

## Director's statement

Idea; pitch anchor; and each visual, sonic and editing choice written as **function**: "natural light
only, because the film is about a body surviving next to a mind coming apart; warmth exists only where
someone built it with their hands". If a rule can't name its function, it is decoration — cut it.

## Production notes

Asset status; runtime ceiling; generation settings (model, resolution, aspect, audio, duration =
timeline sum, draft first); the order of work on a shot.

## Versioning

Put `Bible v[N] — [date]` at the top. Log changes at the bottom. Never edit a template silently.
