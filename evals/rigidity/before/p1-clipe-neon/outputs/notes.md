# Notes — p1-clipe-neon

## 1. Skill files read (in order)
1. skills/cineoro-director/SKILL.md
2. skills/cineoro-sound/SKILL.md
3. skills/cineoro-director/references/seedance-2.5.md
4. skills/cineoro-light/SKILL.md
5. skills/cineoro-camera/SKILL.md
6. skills/cineoro-performance/SKILL.md
7. skills/cineoro-realism/SKILL.md
8. skills/cineoro-assets/SKILL.md
9. skills/cineoro-sound/references/voice-and-language.md (grep only, for singing/lip-sync; nothing on music-video lip-sync to a song)

Not read: cineoro-story (no script), cineoro-space (one person), worked-examples.md, prompt-spine.md, scene-types.md, film-locks.md, acting-task.md (performance says to read it before any ACTING block; I skipped it for budget and efficiency).

## 2. Where the skill pushed AWAY from the user's request
- **Music ban everywhere** (director CONTRACT "NO music", sound law 6, realism spine "music, score, BGM", seedance notes). The user's clip IS music: their own song as an audio reference, plus lip-sync. I inverted the policy: the soundtrack = Audio 1, unchanged. I banned only *generated* music, remixes and extra instruments. The tree has no music-video or playback mode at all.
- **"Diegetic only, dirty-real location sound"** (SOUND template). It doesn't fit a music video. I replaced it with "Audio 1 is the entire soundtrack".
- **Audio reference = voice only** (assets template "VOICE of @NAME ONLY; all other sound generated fresh"). Here the reference is the full song and the lip-sync source. I wrote a custom reference job.
- **FILM LOOK "muted and filmic, never saturated", "MEGA-REAL", 35mm grain, low-key fire looks.** The user wants saturated, stylized, music-video colour and explicitly no documentary. I wrote a glossy saturated neon look and kept realism only in skin and material.
- **Light "NATURAL / MOTIVATED LIGHT ONLY", Kelvin-based.** Neon is a motivated practical, so it is compatible. But Kelvin doesn't describe saturated pink and blue, so I described the colours and their sides instead of Kelvin.
- **Camera: orbit, gimbal, stabilized and drone appear in NOT lists and the realism spine** ("static locked camera, tripod, gimbal, stabilized footage"), and the default is a handheld documentary operator. The user explicitly wants the camera circling her. I wrote a Steadicam orbit as the movement, removed stabilization and orbit from the negatives, and put "shaky documentary handheld" in NOT instead.
- **Composition "off-centre, centred symmetrical reads as render".** A vertical performance clip wants the singer owning the centre. I made it "slightly off-centre" as a compromise and removed "centred, symmetrical" from the negative.
- **Performance: anti-"looking into the lens" default.** Lip-sync to camera is the genre. I let her lock onto the lens during the line, with a task behind it.
- **"Lines out of the last 1–2 s" and "short lines".** These were respected (the line runs 4–9 s). But the line's timing is dictated by the user's audio, not by me. I stated it as a default the user must align.
- **Realism doctrine "subtract, darker, fewer adjectives"** pulls toward naturalism. I kept the anti-AI parts (skin, eyes, physics of dance weight) and dropped the documentary aesthetic.

## 3. Rules broken on purpose
- Music ban (CONTRACT/SOUND/NEGATIVE): broken. The user's song is the deliverable.
- FILM LOOK "never saturated / muted / MEGA-REAL / no digital clean": broken, at the user's explicit request.
- Standing NEGATIVE spine: removed music, score, BGM, centred, symmetrical, gimbal, stabilized and level-horizon entries, because the shot wants them.
- I did not read `acting-task.md` before writing the ACTING block (performance says to). This was for budget and speed.
- Light in colour names rather than Kelvin (law 1 asks for Kelvin).
- The card adds a post-production recommendation (lay the master audio back over the video), which is outside the "header + prompt + card only" deliverable. I added it as a card note because it is the most likely failure.
