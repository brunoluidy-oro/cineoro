# Skill files read, in order

1. skills/cineoro-director/SKILL.md
2. skills/cineoro-director/references/prompt-spine.md
3. skills/cineoro-director/references/seedance-2.5.md
4. skills/cineoro-director/references/scene-types.md
5. skills/cineoro-director/references/worked-examples.md
6. skills/cineoro-director/references/qa-and-repair.md
7. skills/cineoro-story/SKILL.md
8. skills/cineoro-performance/SKILL.md
9. skills/cineoro-camera/SKILL.md
10. skills/cineoro-light/SKILL.md
11. skills/cineoro-sound/SKILL.md
12. skills/cineoro-space/SKILL.md
13. skills/cineoro-assets/SKILL.md
14. skills/cineoro-realism/SKILL.md
15. skills/cineoro-story/references/dramatic-read.md
16. skills/cineoro-story/references/coverage-and-editing.md
17. skills/cineoro-performance/references/acting-task.md
18. skills/cineoro-performance/references/behaviour-mechanics.md
19. skills/cineoro-performance/references/living-eyes-and-states.md
20. skills/cineoro-camera/references/optics.md
21. skills/cineoro-camera/references/format-and-lens-looks.md
22. skills/cineoro-camera/references/operator-and-composition.md
23. skills/cineoro-light/references/film-locks.md
24. skills/cineoro-light/references/light-control.md
25. skills/cineoro-sound/references/voice-and-language.md
26. skills/cineoro-sound/references/soundscape.md
27. skills/cineoro-assets/references/reference-usage.md
28. skills/cineoro-assets/references/asset-pipeline.md
29. skills/cineoro-realism/references/negative-library.md
30. skills/cineoro-realism/references/anti-ai-tells.md

Files 2–6 and 7–14 were read in parallel batches; the order inside each batch is the order the calls
were issued.

## Not read (and why)

- skills/cineoro-bible/*: one generation with no project bible and no multi-shot project, so Step 0
  doesn't route to it.
- skills/cineoro-director/references/shotlist-html.md: that file is for Mode B (shotlist), and this
  task is Mode A.
- skills/cineoro-space/references/previz-and-geometry.md and staging-map.md: no Blender previz or
  staging map was used, so GEOMETRY was written directly.
- skills/cineoro-realism/references/diagnosis.md: that file is for Mode C (repair), and nothing here
  needed repairing.

## Mode and decisions

- Mode A (single prompt), scene types A (quiet intimate) + G (physical process). Calibrated against
  worked example 1.
- 4 shots, 23 s, 16:9, Higgsfield reference-to-video. Upload order: grandfather, grandson, jangada.
