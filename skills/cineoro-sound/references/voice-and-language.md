# Voice and language

**Contents:** supported languages · the script-steers-phonetics rule · Portuguese and other natural
languages · invented languages · accents · multi-speaker binding · audio references · voice states
(whisper, failing speech, crying, screaming, laughter, singing, humming) · line writing for the engine

---

## Supported languages (Seedance 2.5, official)

Chinese, English, Spanish, Indonesian, Malay, Thai, Arabic, **Portuguese**, Vietnamese, Japanese,
Korean. Other languages can come out — production has generated convincing speech in an invented
language written in Cyrillic — but expect more retakes and use the fix ladder in SKILL.md.

## The script-steers-phonetics rule

The engine reads the characters of the line as a pronunciation instruction.
- A line in Latin script is read with English phonetics unless the language is named and the
  orthography is clearly another language's (accents, ç, ã, ñ).
- Partial romanization is the worst case: it drags the whole line toward English rhythm.
- The prompt itself stays in English; only the spoken line is in its own language and script, never
  translated, transliterated or glossed inside the prompt.

## Portuguese (and other natural languages)

```
[3–6s] @MARIA (on camera, Brazilian Portuguese, native accent from [region], quiet, low in her chest,
the last word swallowed): "Eu volto antes do almoço."
```
- Name **the variety and the region** (Brazilian Portuguese, carioca / nordestino / paulistano;
  European Portuguese) — accents are part of casting.
- Write the line with full orthography (acentos, cedilha, til). Avoid abbreviations ("vc", "tá" is
  fine if that is how it is said — write the spoken form).
- Do not translate the line in the prompt; a translation next to it invites subtitles or a second
  reading.
- Same rules apply to Spanish (variety + region), Japanese (kana/kanji, not romaji), Arabic (Arabic
  script, name the dialect), Korean (Hangul).

## Invented languages (conlangs)

Method proven in production:
1. **Design the sound first** (e.g. guttural, throaty uvular stops, glottal stops, hard back vowels,
   consonant clusters) and choose a **script whose letters the engine pronounces that way** (for that
   case, Cyrillic).
2. **One word, one meaning, no synonyms.** A word is coined once and used everywhere without
   variants, or the language falls apart on screen.
3. **Never romanize, never translate inside the prompt.**
4. **Pronunciation notes** go in the VOICE block once ("ӄ — a deep uvular stop at the very back of
   the throat; hard flat ы/э; clusters not softened").
5. **When the engine can't say it:** regenerate with a different delivery description first; then
   simplify the spelling of the problem word toward what the engine can produce, keeping meaning and
   sound.
6. The dictionary and grammar live in the project bible (`cineoro-bible`), never in a shot prompt.

## Accents

An accent is a voice attribute in the VOICE LOCK and in the line label. If the engine drifts to a
default (often English or Mandarin), name the language and accent in the CONTRACT line as well:
"all speech in Brazilian Portuguese with native accents".

## Multi-speaker binding

- One label per line; never two speakers in one sentence of the prompt.
- Bind each audio reference to exactly one character: "Audio 1 is @RINTYN's voice ONLY".
- Official mapping pattern: "Images 1–2 are Character 1 and correspond to Audio 1; Images 3–4 are
  Character 2 and correspond to Audio 2".
- In an exchange, mark the listener's mouth as closed during the other's line.

## Audio references for voices

- 5–10 s of clean speech per voice is the recommended clip length; total audio per generation is
  limited (30 s across all audio references).
- Describe the voice in words too ("the low, thick, warm voice of Audio 1") — the description helps
  matching.
- State the scope: "its only job is this voice; all other sound is generated fresh as raw location
  sound".
- A good take of a character can be the source of the next audio reference — cut a clean 5–10 s
  piece of an approved line.

## Voice states — write the physics

| State | Write | Avoid |
|---|---|---|
| Whisper | "lips barely moving, almost no jaw, voiced only on the tail of the exhale" | "whispers" |
| Failing / dying speech | "barely voiced, no projection, words dissolving into breath, the same syllables repeating" | "weak voice" |
| Speaking while crying | "the break happens in the breath; a swallow cuts the phrase; a note goes wet and closes in the throat; sniffling between words" | "sobbing", "crying voice" |
| Child-like voice from an adult | "the voice drops into a tiny, sniffling child's register for one word" | "baby voice" |
| Scream | "ugly, hoarse, shapeless, cracking and running out of air, thrown from the belly" | "cinematic scream", "wail" |
| Command | "flat, certain, unhurried, brief, chest-deep" | "authoritative" |
| Laughter | "soft wheezing laugh, hitching, restarting, never stopping" / "a small broken laugh, soft and wrong" | "maniacal laugh", "villain laugh" |
| Singing / humming | "a wordless lullaby, mmm… mm-mmm… hmm, breaking off mid-phrase" | "beautiful song" |
| Muffled / through a wall | "muffled by the hide wall and the wind, far, the high frequencies gone" | "distant voice" |

## Writing lines for the engine

- **Short lines.** Long lines drift out of sync; split them across beats.
- **Seconds per line** (whole seconds), with room before and after; nothing in the last 1–2 seconds.
- **Repetition is a choice**: if a word repeats, write it each time with its own delivery; never
  repeat dialogue words elsewhere in the prompt (it invites subtitles).
- **One emotion note per line**, in the label — not attached to individual words.
- **Non-verbal vocal events** (a gasp, a short wrenched cry, a held breath at the drum) are written
  as lines with seconds, so the engine places them.
