# Notes — hospital-shotlist (old_skill)

## Skill files read
- `cinedance/SKILL.md`
- `cinedance/reference/dramatic-read.md`: scripted input, used to decide coverage
- `cinedance/reference/acting-task.md`: required whenever a face is on camera
- `cinedance/reference/shotlist-html.md`: MODE B container and HTML template
- `cinedance/reference/optics.md`: multishot, OPTICS blocks, 12°/18°/29°/47° language
- `cinedance/reference/locks.md`: multi-character staging, gaze and orientation, lighting priority
- `cinedance/reference/protocols.md`: checked for named techniques (none used beyond optics)

## Not read
- `cinedance/reference/blocking-map.md`: not needed because the user attached no frame and asked for no staging map.
- Nothing under `/home/user/cineoro/skills`. No other skill was read.

## Outputs
- `shotlist.html`: MODE B shotlist. One scene with prompts 1a–1e, each 15s, with copy buttons and a localStorage checkbox.
- `answer.md`: the full chat reply, with the shot table and all five prompts.
- Assembled from per-prompt source files with a small build script, so the HTML and answer.md carry identical prompt text.
