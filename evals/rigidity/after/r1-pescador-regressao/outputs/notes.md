# Notes — r1-pescador-regressao

## (1) Skill files read
- skills/cineoro-director/SKILL.md
- skills/cineoro-director/references/style-and-divergence.md (required at the start of every project)
- skills/cineoro-director/references/seedance-2.5.md (references and Higgsfield syntax matter here)
- skills/cineoro-director/references/prompt-spine.md
- skills/cineoro-director/references/worked-examples.md (once per session, for density)
- Department SKILL.md files: cineoro-story, cineoro-performance, cineoro-camera, cineoro-light, cineoro-sound, cineoro-space, cineoro-assets, cineoro-realism
- skills/cineoro-performance/references/acting-task.md (performance says to read it before any ACTING block)
- skills/cineoro-sound/references/voice-and-language.md (the scene has speech)
Not read: cineoro-bible (no project), the director's qa-and-repair, scene-types and shotlist-html, and the reference files for camera, light, space, assets, realism and story (budget).

## (2) Places the skill pushed me away from the user's request
- "bem cinematográfico": the realist fallback preset points to observed handheld, off-centre framing, no score and no flares. The user said "cinematográfico e real", which could also mean a polished, composed, dolly-type look or a score. I read "real" as the stated style and used the realist preset, but toned it down to a camera that mostly stays put. This is a judgement call the skill nudged.
- Music: the skill bans music by default. The user didn't ask for music and didn't rule it out either. "Cinematográfico" could suggest a score. I went with no music, as the skill's fallback.
- Jangada photo: the skill pushes "one job per reference" and downgrades the photo to OBJECT ONLY in the background, with its sky and light ignored. The user may have expected the photo to set the world or location too.
- Length: the skill sends you toward a 1,000–2,000-word prompt (this one is roughly 2,000), even though the official guidance it quotes is ≤1,000 words. The user asked for "o prompt", not a long control document.
- Delivery shape: the skill requires a header, the prompt and the card, all in a fixed format. It also forbids showing the reasoning, which means I had to pick the defaults silently.
- ALTERNATIVE DIRECTION line: added because the skill's divergence rule asks for it on key scenes. The user didn't ask for options.
- The skill hints at hiding faces and at "fewer sharp faces". I didn't do that in the main prompt, because the user supplied face photos, so the faces are meant to be seen. I offered it only as the alternative.

## (3) Rules broken on purpose
- The user's line repeats inside the prompt only in the DIALOGUE block. I kept it out of the ORDER recap (where the template's "Only @A speaks" summary might quote it) to follow the sound rule against repeating dialogue words. That is not a break, just a resolution in favour of the sound law over the template habit.
- The 10-year-old is in the referenced cast with a real-face photo. The skill warns some providers refuse real faces. I kept the user's references and only put the warning on the card, instead of replacing them with generated portraits.
- The STYLE INTENT block and the 2–3 directions for a "new project" were not output (Mode A, single scene). The intent was fixed internally, and only one ALTERNATIVE DIRECTION line was given.
- Prompt length is about 2,000 words, at the compression threshold. I didn't run the compression pass.
