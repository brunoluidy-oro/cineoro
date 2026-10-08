# Notes: fogueira-reparo (with_skill)

## Skill files read, in order
1. skills/cineoro-director/SKILL.md
2. skills/cineoro-director/references/qa-and-repair.md (Mode C)
3. skills/cineoro-director/references/seedance-2.5.md
4. skills/cineoro-realism/SKILL.md
5. skills/cineoro-realism/references/diagnosis.md
6. skills/cineoro-director/references/prompt-spine.md
7. skills/cineoro-director/references/scene-types.md (type G, physical process)
8. skills/cineoro-director/references/worked-examples.md (includes example 3, a repair)
9. skills/cineoro-performance/SKILL.md
10. skills/cineoro-light/SKILL.md
11. skills/cineoro-sound/SKILL.md
12. skills/cineoro-story/SKILL.md
13. skills/cineoro-camera/SKILL.md
14. skills/cineoro-space/SKILL.md
15. skills/cineoro-assets/SKILL.md
16. skills/cineoro-performance/references/acting-task.md
17. skills/cineoro-performance/references/behaviour-mechanics.md
18. skills/cineoro-performance/references/living-eyes-and-states.md
19. skills/cineoro-light/references/film-locks.md
20. skills/cineoro-light/references/light-control.md
21. skills/cineoro-sound/references/soundscape.md
22. skills/cineoro-realism/references/negative-library.md
23. skills/cineoro-assets/references/reference-usage.md
24. skills/cineoro-camera/references/format-and-lens-looks.md
25. skills/cineoro-camera/references/optics.md
26. skills/cineoro-camera/references/operator-and-composition.md
27. skills/cineoro-realism/references/anti-ai-tells.md

Not read on purpose: cineoro-bible (single generation, no project), space previz/staging-map (one
person, no blocking problem), sound voice-and-language (no speech), assets asset-pipeline (no assets
built), director shotlist-html (not Mode B). I did not open eval_metadata.json.

## Defaults decided (stated in the answer)
16:9; 15 s in one continuous take (4 beats: 3/4/4/4); MS at 47°, breathing handheld that stays put;
"pederneira" read as a ferrocerium rod with a steel scraper (rod in the left hand, scraper in the right);
no dialogue; text-to-video with no references; before ignition the only light is weak moonlight from
behind plus the spark flashes. The five critical invariants repeated in LOCKS, shot text, NEGATIVE and
ORDER: no flame or glow before 6 s, world light only, eyes on the task, which hand holds which tool,
no music.

## Friction found in the skill tree (for the next iteration)
- **Missing story references.** `cineoro-story/references/` is empty. SKILL.md points to
  `dramatic-read.md` and `coverage-and-editing.md`, but neither file exists.
- **Mode C assumes a CINEORO prompt.** The protocol says "change only that block, keep everything else
  byte-identical". That doesn't fit when the failed prompt is a one-line mood prompt with no blocks.
  Nothing says to deliver a full spine prompt plus a generation card in that case. I did it anyway
  and said so in the answer. Suggested fix: add a "repair of a non-CINEORO prompt" row to
  qa-and-repair.md.
- **No guidance for light that changes during a take.** In this shot the source does not exist at
  frame 1 and grows during the take (dark → sparks → ember → flame). film-locks.md only covers fixed
  sources. Suggested fix: add an entry for "light that grows" with START/DURING/END exposure, plus a
  lock that the frame brightens only as the source grows.
- **Prompt is long.** It came out at about 1,850 words (about 10.8k characters). That is above the
  600–1,200 target but under the ~3,000-word production ceiling. The extra text is locks, process
  mechanics and light states.
- **"Pederneira" is ambiguous** (ferro rod vs flint-and-steel). Worth a line in behaviour-mechanics.md
  with both processes.
