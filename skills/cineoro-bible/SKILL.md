---
name: cineoro-bible
description: Project-bible builder of the CINEORO directing tree for Seedance 2.5 films, series, ads and music videos. Interviews the user (or reads the treatment, script and references) and generates a dedicated PROJECT SKILL - the film's bible - with look templates pasted verbatim into every prompt, the @TAG registry, cast sheets with voice locks, props with their functions, world rules, project anti-AI-tell rules and negatives, reference prompts by scene type, the script in its original language, an optional invented-language dictionary, and the director's statement as functional rules. Use it whenever the user starts a new film or series, says "new project", "bíblia do filme", "skill do projeto", "lock the style for the whole film", "create a project skill like ANERNEQ", or when prompts for one project keep drifting in look, voice or naming. Works with cineoro-director, which uses the project skill as its source of verbatim templates.
---

# CINEORO · BIBLE

A film made of generated shots holds together only if every prompt carries the same words for the
same things. The engine has no memory; the bible is the memory. This department builds a **project
skill** — a file the director loads for every shot of that project — so that look, light, voices,
names, props and world are pasted verbatim instead of re-invented.

The structure comes from a production that carried a 20-minute photoreal AI short through hundreds of
generations: one playbook holding the prompt structure, the reusable templates, the props list, the
voice profiles, the language, the script, the negative library, the acting method and the director's
statement.

---

## When the bible is needed

- A film, series, campaign or music video with more than ~5 generations.
- Recurring characters, voices or locations.
- A look that must stay identical across shots and sessions.
- An invented language, a period world, or a culture whose daily life must be right.

For a one-off shot, skip the bible; the director writes the look inline.

---

## Reading list for this mode

A bible touches every department, so read only this list (not every department reference):
`assets/project-skill-template.md`, `references/bible-sections.md`, `references/interview.md`, then
`cineoro-director/references/prompt-spine.md` and `worked-examples.md`,
`cineoro-light/references/film-locks.md`, `cineoro-camera/references/format-and-lens-looks.md`,
`cineoro-sound/references/voice-and-language.md` (if there is speech),
`cineoro-performance/references/acting-task.md`, `cineoro-realism/references/negative-library.md`,
and `cineoro-assets/references/asset-pipeline.md` (the registry format and asset image prompts).

## Procedure

1. **Gather** — read whatever the user has (logline, treatment, script, mood references, asset images).
   Ask only for what is missing and decisive; offer defaults for the rest. Use the interview in
   `references/interview.md`, in the user's language. **If the user gives only a logline**, you will
   have to propose beats, lines and endings: mark every invented element as a *director's proposal*
   (in the script header, the dialogue table and the reply) so the user can accept or rewrite it — the
   user's own material is never changed.
2. **Decide the functional rules** — the director's statement turned into rules (light system,
   camera language, editing grammar, sound policy, palette with its one exception, motifs). Every rule
   must say *what story mechanism it serves*.
3. **Lock the verbatim templates** — CONTRACT line pattern, FILM LOOK, base LIGHT block(s), LENS LOOK,
   NO LENS FLARES, standing NEGATIVE spine for this world, WORLD block. Pull starting points from
   `cineoro-light` and `cineoro-camera`, adapt once, then freeze. **Template budget:** the always-on
   templates together stay under ~600 words, and no item is fenced in two templates (an anachronism
   banned in WORLD is not repeated in the NEGATIVE spine). Every word in a template is paid in every
   prompt of the film — a bloated bible pushes every shot past 2,500 words.
4. **Register the assets** — every character, location, prop, state and voice with one `@TAG`
   (registry format in `cineoro-assets/references/asset-pipeline.md`). On Higgsfield, name each saved
   Element exactly as its tag without the `@`, so the picker and the prompt agree.
5. **Cast sheets** — per character: tag, age, look, hands, temperament, super-objective, what they never
   do, VOICE LOCK (`cineoro-sound` format).
6. **World and daily life** — what exists, what doesn't, how things are made and used; props master list
   with function; the objects that carry more than themselves (locked harder).
7. **Reference prompts** — one complete model prompt in SKILL.md §4.1, plus complete prompts for the
   2–3 other main scene types in `references/reference-prompts.md`, all in the CINEORO spine (use the
   spine's CONTRACT form), so most shots start from a copy.
8. **Write the project skill** from `assets/project-skill-template.md`, filling every section; long
   material (full script, dictionary, extra reference prompts, registry) goes into the project skill's
   own `references/`. Paste blocks are always English; the human-facing prose (statement, acting
   notes, structure, production notes) is written in the user's language.
9. **Mark it v1 — to test.** Templates freeze only after drafts of 2–3 scene types (list them in §11 as
   the test plan); after the test, issue v1.1 and freeze.
10. **Validate and package** — run the checklist below; then zip the folder as `project-[slug].skill`
    (a zip of the folder; if the skill-creator packager is available use it) so the user can install it.

Detailed guidance per section, with examples of good and bad entries: `references/bible-sections.md`.

---

## Output

```
project-[slug]/
├── SKILL.md                  ← from assets/project-skill-template.md
└── references/
    ├── script.md             ← generations with entry/exit states and lines in the original language
    ├── asset-registry.md     ← the full @TAG table + image prompts for each asset
    ├── reference-prompts.md  ← complete prompts for the other main scene types
    └── language.md           ← dictionary + grammar (only if an invented language)
```

The project skill's `name` is `project-[slug]` (kebab-case). Its description names the project, the main
characters and locations, and says it is used with `cineoro-director` for every prompt of the project.

## Rules for a good bible

- **Verbatim means verbatim.** Templates are never paraphrased per shot. Change them only by issuing a
  new version of the bible.
- **One word, one meaning.** No synonyms in names, tags, templates or an invented language.
- **Function over style.** Every visual, sonic and cultural rule names the story mechanism it serves.
- **Composite, not reconstruction** — when a world draws on a real culture, say whether it is a
  reconstruction or a composite, and keep its daily life correct either way.
- **The bible grows.** New lessons from failed takes become project anti-AI-tell rules and negatives,
  with the date.

## Hand-off

Give the user the project skill (packaged), a one-paragraph summary of the locked decisions, and the
list of assets still to build. From then on, `cineoro-director` loads the project skill first for
every shot of that project.

## Checklist

- Every template that must be pasted verbatim is present and complete?
- Every character, location, prop, state and voice has one `@TAG` in the registry?
- Every speaking character has a VOICE LOCK; every language rule is stated?
- The light/palette system, camera language and editing grammar each name their story function?
- At least one complete reference prompt in the CINEORO spine?
- Project-specific negatives and anti-AI-tell rules recorded?
- Description of the project skill names the project, characters and locations so it triggers?
