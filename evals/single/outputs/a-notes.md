# Notes on the cineoro skill structure (test a)

## Files read (all inside /home/user/cineoro/skills/cineoro)
- SKILL.md
- references/style-and-divergence.md
- references/prompt-spine.md
- references/worked-examples.md
- references/seedance-2.5.md
- references/scene-types.md
- references/qa-and-repair.md
- departments/story/DEPARTMENT.md
- departments/performance/DEPARTMENT.md
- departments/camera/DEPARTMENT.md
- departments/light/DEPARTMENT.md
- departments/sound/DEPARTMENT.md
- departments/space/DEPARTMENT.md
- departments/assets/DEPARTMENT.md
- departments/realism/DEPARTMENT.md
- departments/performance/references/acting-task.md
- departments/sound/references/voice-and-language.md
- departments/assets/references/reference-usage.md
- departments/light/references/film-locks.md

Not read (not needed for this case): bible, shotlist-html, dramatic-read, coverage-and-editing, optics, operator-and-composition, format-and-lens-looks, soundscape, negative-library, anti-ai-tells, diagnosis, behaviour-mechanics, living-eyes-and-states, staging-map, previz-and-geometry, character-sheet, asset-pipeline, light-control, bible files.

## Broken paths
None found. Every path referenced in the files I read resolved (departments/<name>/DEPARTMENT.md, references/*.md). The glob listing matches what SKILL.md names.

## Confusion / friction
1. SKILL.md "Reading budget" says "read the SKILL.md of each department", but the files are DEPARTMENT.md. The routing paragraph above it clarifies this, so it is a stale wording only.
2. Department files still say "Return to `cineoro-director`" and refer to `cineoro-light`, `cineoro-space` etc.; SKILL.md explains the mapping, but it requires a mental translation on each hit.
3. acting-task.md says "carried over from the `cinedance` skill" and mentions `tig-scene-engine`; both are outside the tree (not needed).
4. The only worked example (Example 1) is almost the same scene as the user's task (grandmother, coffee strainer, "Leva a garrafa", Brazilian kitchen). Risk of copying it; style-and-divergence.md warns against inheriting. I changed shot structure, light (oil lamp, black window), grandson age, tactic of the boy, and had only one line. The task says "the user has photos of their faces only", which the example (with a world plate and wardrobe refs) doesn't cover; I described wardrobe in text and flagged it.
5. No guidance on a child in WHO IS WHO / real-face uploads beyond one line in seedance-2.5.md ("some providers refuse real faces"); I put that in the card notes.
6. The 15s line placement: voice-and-language says keep lines out of the last 1-2s; I put it at 10-12s. Fine.
7. Ambiguity: SKILL.md says ask only when the ambiguity changes the shot; the grandson's age/whether he speaks does change the shot, but the task said decide, so defaults are stated on the card.
8. The ALTERNATIVE DIRECTION line is required "for key scenes"; unclear if a plain 15s scene counts. I included one line in the header.
