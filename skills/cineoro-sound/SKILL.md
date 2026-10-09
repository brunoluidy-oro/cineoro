---
name: cineoro-sound
description: Voice, dialogue and sound department of the CINEORO directing tree for Seedance 2.5 video prompts, where speech, lip-sync, effects and ambience are generated in the same pass as the picture. Writes the DIALOGUE and VOICE block (who speaks, on or off screen, language and accent, delivery as mouth and breath physics, timing in seconds), the per-character VOICE LOCK, audio-reference binding, and the SOUND block (specific diegetic sources, silence design, a music policy that actually holds). Use it whenever a shot has a spoken line, a voice that must stay identical across shots, a foreign or invented language, whispering, crying or screaming speech, an off-screen voice, or whenever a take came back with unwanted music, subtitles, wrong lips moving, an English accent on another language, robotic voice, echo or chimes. Triggers include "diálogo", "fala", "voz", "sotaque", "dublagem", "lip sync", "no music", "keep the same voice", "she whispers", "voice reference". Called by cineoro-director; also usable on its own.
---

# CINEORO · SOUND

Seedance 2.5 generates the voice, the lips, the effects and the room tone in the same pass as the
image. That makes sound a directing job inside the prompt: the engine will invent a score, a narrator,
subtitles, a generic voice and a clean digital room unless the prompt decides otherwise. Silence is
an instrument; the heaviest moments get more silence, not more sound.

You write the **DIALOGUE & VOICE** block, the **VOICE LOCK** per character, the **SOUND** block, and
hand the director the audio locks and negatives.

---

## Seven laws

1. **Only the scripted line is spoken.** Name the speaker, mark ON CAMERA or OFF-SCREEN, give the
   second it starts, name the language and accent. Every other mouth stays closed — say so. No ad-libs,
   no narration, no voice-over unless the film uses them.
2. **Delivery is mouth and breath physics, not a label.** "lips barely moving, almost no jaw, the
   words dissolving into the exhale" — never the word "whisper". "a swallow cuts the phrase in half,
   the last note goes wet and closes in the throat" — never "sadly".
3. **A voice is a written condition, decided once.** The VOICE LOCK is pasted verbatim into every
   shot the character speaks in; the scene's manner (whisper, scream, delirium) is layered on top,
   never replacing it. For hard continuity, bind an audio reference to that character only.
4. **The spelling steers the phonetics.** The engine reads the script of the line as a pronunciation
   instruction. Write each line in the native orthography of the language you want to hear
   (Portuguese with its accents, Spanish with its ñ). For an invented language, pick a script whose
   phonetics match the sound you want and never romanize it — Latin letters pull English phonetics in.
5. **Sound is specific and sourced** (diegetic in a realist film; heightened, comic or stylized design
   when the STYLE INTENT asks — still specific). List what the world sounds like, each with behaviour
   ("fine snow ticking on hide", "the rawhide creaking against the wood and the small snap as each
   knot seats"). The sound of hands working is part of believable behaviour.
6. **The music policy is explicit and repeated.** The engine adds music when not told. If the film has
   no score, ban it at the top and the end with the synonyms it slips through (music, score, BGM,
   instrumental, melody, synth, ambient pad, drone, swell, chimes). If it has one, describe it
   precisely — instrumentation, entry second, level under dialogue, build, stop. For a music video, the
   user's track is attached as an audio reference; lip-sync and movement are timed to its beats and
   no other music is allowed. See `references/soundscape.md` → "When the film has music".
7. **No text on screen.** Subtitles appear when tone tags are attached to single words or dialogue words
   are repeated. Keep one emotion note per line, never per word, and state "no subtitles, no
   captions, no on-screen text — the words exist only as sound".

---

## DIALOGUE & VOICE — template

```
DIALOGUE — only these lines are spoken, each by the named character; ON CAMERA lines are lip-synced,
mouth movements match the sound exactly; NO dubbing, NO voice-over, NO narration, NO subtitles, NO
on-screen text — the words exist only as sound. Every mouth not speaking stays closed.
[2–5s] @NAME (on camera, [language + accent], [delivery as physics]): "[line]"
[9–11s] @NAME2 (OFF-SCREEN, from frame-left, [muffled through the wall]): "[line]" — the voice belongs
to nobody in frame; no visible mouth forms these words.
VOICE LOCK — @NAME: [verbatim profile]. These voice identities are fixed and identical across all
shots of the film.
[If an audio reference is attached:] @NAME's lines keep exactly the voice of [audio tag] — same
timbre, never re-voiced; [audio tag] is used for this voice ONLY; all other sound is generated fresh.
```

Official Seedance 2.5 notation also works and can be mixed in: dialogue in `{}` or quotes, sound
effects in `<>`, music in `()`, with "Character's line (emotion): content" and the language named
before any non-Chinese line. Pick one convention per project and keep it.

## VOICE LOCK — template (one per character, lives in the project bible)

```
VOICE LOCK — @NAME: [age/sex impression], [trained or untrained], [register: chest/head], [texture:
rasp, breath, crack], [volume habit], [rhythm: fast and flat when working / slower with him],
[how it breaks: in the breath, never a sob aloud], [how it screams: ugly, hoarse, shapeless], [accent].
Never [the two wrong voices this character must not get].
```

Write the voice so that a stranger could cast it. Two voices in one scene must differ on at least
two axes (register, texture, tempo).

## SOUND — template

```
SOUND — DIEGETIC ONLY, dirty-real location sound: [5–10 specific sources in order of prominence,
each with behaviour]. [Silence design: where sound drops away and for how long]. [Off-screen sound
cues that drive the action, with seconds]. NO music, NO score, NO BGM, NO instrumental, NO melody,
NO ambient pad, NO drone, NO swell, NO chimes, NO metallic ringing, NO reverb or echo unless the
space has it, NO clean digital sheen.
```

---

## Speech problems and the order of fixes

1. **The engine smeared a sound or a cluster** → regenerate the same shot, same line, with a
   *different description of the delivery* (slower, more breath, louder on the stressed syllable).
2. Still smeared → simplify the spelling of the critical word toward what the engine can produce,
   keeping meaning and sound.
3. **Lip-sync drifts late in a long line** → shorten the line, split it across two beats, prefer
   medium close-ups, keep lines out of the last 1–2 seconds of the generation.
4. **Wrong mouth moving** → OFF-SCREEN label + "no visible mouth forms these words" + the listener's
   mouth-shut lock in LOCKS and NEGATIVE.
5. **Voice changed between generations** → paste the identical VOICE LOCK; attach a 5–10 s clean
   audio reference of that voice, bound to that character only, and describe the voice in words too.
6. **Default language took over** (another language or accent appeared) → name the language and the
   accent in the line label *and* in the CONTRACT; never mix languages inside one line.

Language and script strategy, invented languages, accents, multi-speaker binding, screams, crying,
laughter, singing and humming: **`references/voice-and-language.md`**.
Soundscape library by world, silence design, rhythmic sounds that must not become music, and audio
artifacts: **`references/soundscape.md`**.

---

## Hand-off to the director

Return to `cineoro-director`:
- the **DIALOGUE & VOICE** block (lines with seconds, ON/OFF labels, voice locks, audio binding);
- the **SOUND** block;
- audio **locks** ("only @A speaks — one word, twice", "her mouth stays shut the entire scene");
- the audio part of the **NEGATIVE** (music synonyms, subtitles, wrong speaker, re-dubbed voice,
  English accent) and the music ban for the **CONTRACT** line.

## Checklist

- Is every line labelled with speaker, ON/OFF, seconds, language/accent and delivery physics?
- Is every non-speaking mouth locked shut?
- Is each speaking character's VOICE LOCK pasted verbatim (and any audio reference bound to one voice)?
- Is each line written in the orthography of the language you want to hear, never romanized?
- Is the SOUND list specific, diegetic and full of the sounds the hands make?
- Is the music ban written with synonyms at the top and at the end?
- Is there one emotion note per line (none per word), and a no-subtitles clause?
- Are lines kept out of the last 1–2 seconds of the generation?
