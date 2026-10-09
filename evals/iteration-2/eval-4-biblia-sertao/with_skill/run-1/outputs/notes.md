# Notes — eval-4-biblia-sertao, with_skill, run-1

Mode chosen: **D · Project** (director → `cineoro-bible`). No questions asked; defaults stated in
the answer and in the bible's version log.

## Skill files read, in order

1. `skills/cineoro-director/SKILL.md`
2. `skills/cineoro-bible/SKILL.md`
3. `skills/cineoro-bible/assets/project-skill-template.md`
4. `skills/cineoro-bible/references/bible-sections.md`
5. `skills/cineoro-bible/references/interview.md`
6. `skills/cineoro-light/SKILL.md`
7. `skills/cineoro-camera/SKILL.md`
8. `skills/cineoro-sound/SKILL.md`
9. `skills/cineoro-assets/SKILL.md`
10. `skills/cineoro-performance/SKILL.md`
11. `skills/cineoro-story/SKILL.md`
12. `skills/cineoro-realism/SKILL.md`
13. `skills/cineoro-space/SKILL.md`
14. `skills/cineoro-director/references/prompt-spine.md` (reference prompts are written in the spine)
15. `skills/cineoro-director/references/seedance-2.5.md` (settings/platform matter for production notes)
16. `skills/cineoro-director/references/worked-examples.md` (once per session, density)
17. `skills/cineoro-light/references/film-locks.md` (bible step 3: pull light starting points)
18. `skills/cineoro-camera/references/format-and-lens-looks.md` (bible step 3: lens look)
19. `skills/cineoro-sound/references/voice-and-language.md` (speech in Portuguese)
20. `skills/cineoro-performance/references/acting-task.md` ("read before writing any ACTING block")
21. `skills/cineoro-realism/references/negative-library.md` (scene-type sets, geometry method)
22. `skills/cineoro-story/references/coverage-and-editing.md` (runtime, motifs, generation budgeting)
23. `skills/cineoro-director/references/scene-types.md` (the bible's scene types)
24. `skills/cineoro-sound/references/soundscape.md` (world soundscape, rhythmic sounds vs music)
25. Grep of `skills/cineoro-assets/references/` for "registry" → `asset-pipeline.md` (full read)
26. `skills/cineoro-assets/references/reference-usage.md` (first 40 lines — Higgsfield syntax)

Not read (not sent there for this case): space `previz-and-geometry.md`, `staging-map.md`; realism
`anti-ai-tells.md`, `diagnosis.md`; director `qa-and-repair.md`, `shotlist-html.md`; camera
`optics.md`, `operator-and-composition.md`; light `light-control.md`; performance
`behaviour-mechanics.md`, `living-eyes-and-states.md`; story `dramatic-read.md`.

## Output

- `project-sertao/SKILL.md` — the bible (template sections 0–11, verbatim blocks, model prompt G05).
- `project-sertao/references/script.md` — 23 generations with entry/exit states and lines.
- `project-sertao/references/asset-registry.md` — @TAG registry + image prompts for every asset.
- `project-sertao/references/reference-prompts.md` — complete prompts G08 (night) and G19 (reversal).
- Checked by script: every §1.3 template appears verbatim in all three complete prompts; every @TAG
  used anywhere is in the §1.2 registry; description 980 chars, no angle brackets.

## Friction found in the skill

1. **Reading budget doesn't scale to Mode D.** The rule is phrased per shot ("each department the
   shot touches"); a bible touches every department, so the budget sets no limit. I read 8 department
   SKILL.md files plus 12 references (~25k words). `cineoro-bible` could state its own Mode D reading
   list (film-locks, format-and-lens-looks, voice-and-language, acting-task, negative-library,
   asset-pipeline, prompt-spine, worked-examples).
2. **Registry format path missing.** Bible step 4 says "cineoro-assets registry format" but doesn't
   name the file. It lives in `cineoro-assets/references/asset-pipeline.md`, and I had to grep for it.
3. **How many complete reference prompts?** The procedure step 7 and bible-sections say "one complete
   prompt per main scene type". The template §4 has one model prompt plus adaptations, and the
   checklist says "at least one". The output tree has no slot for extra prompts. I wrote 3 complete
   prompts and added `references/reference-prompts.md`.
4. **CONTRACT mismatch.** The template's CONTRACT pattern ("…[N]s, [N] shots / [N] cuts … NO music,
   NO subtitles") differs from prompt-spine's (cut timings, NO score, NO on-screen text). I used the
   spine version.
5. **Template length vs the 2,000-word norm (biggest friction).** My first draft prompts came out at
   3,200–3,500 words. The always-on verbatim templates (FILM LOOK, LENS, LIGHT, WORLD, GEOMETRY,
   NEGATIVE spine, VOICE LOCKs) alone are ~750–850 words. The compression pass forbids touching
   templates, and the bible doesn't tell the author to budget template length. I tightened the
   templates themselves (fenced anachronisms only in WORLD, not again in the NEGATIVE spine). Even so,
   the multi-shot two-handers land at ~2,700–3,000 words: compliant with the "~3,000 held on
   Higgsfield" note, not with "usually 1,000–2,000". Suggest a bible rule: "always-on templates
   ≤ ~600 words combined; never fence the same item in two templates."
6. **Bible language for non-English users is unspecified.** The template is all English, and the
   paste blocks must be English. The human-facing prose (statement, acting notes, structure,
   production notes) has no rule. I wrote the prose in Portuguese and kept every paste block in
   English.
7. **Untested v1.** bible-sections says to freeze templates only after testing on 2–3 scene types,
   but the bible is built in one pass without generation access. I marked v1 "a testar", added a
   test plan (G05/G08/G19, plus G03 for the aboio) and a freeze at v1.1.
8. **Logline-only input.** Story says "never rewrite the user's material", but a bible needs a
   script. There's no guidance on how much to author (beats, lines, the açude outcome) when the user
   gives only a logline. I flagged everything not in the logline as a director proposal: in the
   script header, the dialogue table and the answer.
9. **Harsh sun entry is a stub.** film-locks "harsh midday sun" has 4 lines, without the
   REACH/EXPOSURE/CONTINUITY/NOT structure of the LIGHT template. There's no drought / white-sky
   world, and nothing on hat brims shading the eyes (a common need in period exteriors). I built it
   from the template.
10. **Journey continuity isn't covered.** Space and light don't cover continuity across generations
    of a travel film: the screen direction of the journey, the sun's side by time of day, and which
    side of the trail the camera owns. I added these as project rules, and "who leads owns
    frame-right" as a functional rule. It could be a general pattern in `cineoro-space`.
11. **Culturally coded sung calls vs the music ban.** voice-and-language mentions humming and singing
    briefly. Nothing covers a regional melodic call (aboio) where the engine is likely to add regional
    instruments. I added project negatives (accordion, zabumba, triangle, viola, fife…) and wrote the
    aboio as a HERDING CALL voice block.
12. **"Package the folder as a skill"** (bible step 9 / hand-off) gives no format or tool. I delivered
    the folder unpackaged.
13. **Higgsfield Element naming is undocumented.** reference-usage says prompts store
    `<<<element-id>>>` tokens, but nothing says whether Element names should match @TAGs. I specified
    "name the Element exactly as the tag without @". This is unverified.
14. **Interview defaults don't cover this case.** The defaults (16:9, spherical) don't address 21:9
    with harsh sun near frame. The camera skill points 21:9 monumental toward anamorphic. I chose
    spherical and gave the flare risk as the functional reason.
