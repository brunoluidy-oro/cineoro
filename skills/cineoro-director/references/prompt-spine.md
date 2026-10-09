# The CINEORO prompt spine — full templates and assembly rules

Every Seedance 2.5 prompt in this tree is assembled in this order. Blocks marked *conditional* are
dropped when the shot doesn't need them; nothing is added that the shot doesn't use.

**Contents:** assembly rules · 0 CONTRACT · 1 REFERENCES · 2 WHO IS WHO · 3 SCENE & SOUL · 4 ABSOLUTE
LOCKS · 5 TIMELINE · 6 DIALOGUE & VOICE · 7 ACTING · 8 CAMERA · 9 GEOMETRY · 10 PHYSICS & MATERIAL ·
11 LIGHT · 12 FILM LOOK · 13 SOUND · 14 WORLD · 15 NEGATIVE · 16 ORDER · single-take variant ·
compression pass · minimal variant

---

## Assembly rules

1. **English prompt; spoken lines in their own language and script.**
2. **Block labels in CAPS** at the start of each block; one blank line between blocks.
3. **Tags:** use the project's `@TAGS` (or the platform's reference tokens) consistently; never a tag
   for something not in this shot.
4. **No scene numbers, no script headings, no "as before".** A prior line matters only as "Prior audio
   context only, not visual content: '…'".
5. **The critical few (≤5)** appear in LOCKS, in the shot text where they can fail, in NEGATIVE and in
   ORDER. Music and subtitle bans appear in CONTRACT and in ORDER/NEGATIVE.
6. **Project templates are pasted verbatim** within their scope — a declared bible EXCEPTION replaces them for its scenes (FILM LOOK, LENS LOOK, LIGHT base, flare policy, WORLD,
   NEGATIVE spine, VOICE LOCKS).
7. **Whole-second ranges**, contiguous; total = the generation's duration.
8. **Descriptive style lives in its home block** (light in LIGHT, lens in CAMERA/FILM LOOK, skin in
   PHYSICS & MATERIAL); the CONTRACT carries only format.

---

## 0 · CONTRACT (always)

```
CONTRACT — [MEDIUM: live-action photoreal / stylized live-action / stop-motion / 2D or 3D animation]
footage, [aspect ratio], [N] seconds total, [N] shots with [N] hard cuts at [s, s, s] / ONE continuous
take, [camera language from the STYLE INTENT], [motion: real-time / slow motion in shot N / stepped
animation], dialogue as spoken on-camera audio in [language + accent] / no dialogue / lip-sync to the
song in [audio ref]. [MUSIC POLICY: NO music, NO score / score: … / the user's track only]. [TEXT
POLICY: NO subtitles, NO on-screen text / the title card "…" spelled exactly].
```

## 1 · REFERENCES (conditional — any attachment)

From `cineoro-assets`. Each attachment → one job; then the SCOPE line.
```
REFERENCES — each reference has ONE job:
[ref] — IDENTITY of @A: … 100% matches.
[ref] — KEYFRAME FOR SHOT 1: shot 1 STARTS from this exact frame ([what it shows]) and comes alive
from it.
[ref] — WORLD for shots 2–4: architecture, materials, clutter.
[ref] — OBJECT ONLY: …
[ref] — VOICE of @B ONLY.
REFERENCE SCOPE: identity and object references supply faces, wardrobe, build, hands and objects
ONLY — IGNORE their backdrops, ground, sky, weather, lighting direction, exposure and colour grade.
```

## 2 · WHO IS WHO (conditional — people or animals)

From `cineoro-space`.
```
WHO IS WHO — READ FIRST, ABSOLUTE:
@A ([age, build, 2–3 unique features, wardrobe state]) — the [ROLE]: [does]; NEVER [...]; owns the
[LEFT] side of the frame.
@B (…) — the [ROLE]: [does]; NEVER [...]; owns the [RIGHT] side.
FACES: each lead's face exists once; every background face distinct; no twins, no clones.
CONTACT: the only touch is [...]; nobody else touches anyone.
```

## 3 · SCENE & SOUL (always)

From `cineoro-story` + `cineoro-performance`.
```
SCENE — [1–3 sentences: what happens, where, when, who; already in progress].
THE SOUL OF THE SCENE (play it, never explain it): [the inner logic that produces the behaviour].
```

## 4 · ABSOLUTE LOCKS (always)

Collected from all departments' risks; 3–7 items; the critical few start here.
```
ABSOLUTE LOCKS — break one and the take is WRONG, regenerate:
1. [invariant, stated positively] — WRONG if [the failure].
2. …
```
Typical: side of frame / axis; prop in hand; who is touched; body orientation across cuts; face always
visible (or never shown); background populated; mouth shut for non-speakers; tempo as chosen; camera
state as chosen (moving / locked); source visibility (in or out of frame); composition as chosen
(symmetrical / off-centre).

## 5 · TIMELINE (always)

Multi-shot:
```
TIMELINE — [N] shots, [N] hard cuts; cuts only at the specified points, the camera adds no cuts of
its own:
SHOT 1 (0–5s) — [size], [FOV]°, [camera position + movement]: [action already in progress, as
mechanics]; [line at second N]. HARD CUT.
SHOT 2 (5–10s) — …. HARD CUT.
SHOT 3 (10–21s) — …. Hard end mid-[action].
```
Single take with beats (jump cuts optional):
```
TIMELINE — ONE continuous take, no cuts, already in progress at the first frame:
BEAT 1 (0–4s) — …
BEAT 2 (4–9s) — …
BEAT 3 (9–14s) — … Hard end mid-[action].
```

## 6 · DIALOGUE & VOICE (conditional — speech)

From `cineoro-sound`.
```
DIALOGUE — only these lines are spoken, each by the named character; ON CAMERA lines lip-synced;
NO dubbing, NO voice-over, NO subtitles — the words exist only as sound. Every mouth not speaking
stays closed.
[2–5s] @A (on camera, [language + accent], [delivery physics]): "[line]"
[11–13s] @B (OFF-SCREEN, [where]): "[line]" — no visible mouth forms these words.
VOICE LOCK — @A: [verbatim]. These voice identities are fixed and identical across all shots.
```

## 7 · ACTING (conditional — faces)

From `cineoro-performance`; one block per face, listeners included.
```
ACTING — @A (fully invested in the tactic; the work happens in the eyes)
SCENE DIRECTION (shared, unspoken): …
EVENT: … · MOTIVE: … · GOAL: … · OBSTACLE: … · TACTIC: …
MOMENT TO MOMENT: — [0–5s] … — [5–10s] … — [break, if any]
LIVING EYES: pupils search, settle, drift; uneven late blinks; asymmetry; involuntary detail: [one].
A reflection of [source] is fine; a frozen pupil is wrong.
NOT: […]
```

## 8 · CAMERA (always)

From `cineoro-camera`.
```
CAMERA — [rig/style], the operator [position], [distance], on the [shadow] side of the axis.
MOVEMENT: the camera [STAYS PUT and breathes / TRAVELS …]; one movement per shot.
OPTICS: [default FOV]° unless a shot states otherwise; [outcomes]; no lens drift inside a shot.
FOCUS: … · HORIZON: …
NOT: [the rigs/moves that contradict THIS camera language — e.g. handheld film: gimbal glide, drone; locked/symmetrical film: shake, drift, canted horizon]
```

## 9 · GEOMETRY (conditional — blocking matters)

From `cineoro-space`.
```
GEOMETRY — @A [pose] at [screen pos], [world pos], torso [angle]; @B […], [distance] from @A;
[prop] at [place]; camera at [height], [distance], [angle] off the axis, on [side]; [landmark];
beyond [distance], darkness. The camera stays on [side] of the A–B axis in every shot.
```

## 10 · PHYSICS & MATERIAL (always)

From `cineoro-realism`.
```
PHYSICS & MATERIAL — [mass/effort]; [resistance → sudden give]; [contact]; [cloth/hair/fur weight];
[particles with wind]; [fluids]; [START / DURING / END for gradual states]. Nothing floats, nothing
loops. OVER-REAL: [5–8 textures]. If any surface looks clean, smooth, plastic, CGI or rendered — WRONG.
```

## 11 · LIGHT (always)

From `cineoro-light` (or the bible's base, verbatim, plus this scene's specifics).
```
LIGHT — [MOTIVATED] LIGHT ONLY, [time], [two words] (KEY): SOURCE … · REACH … · EXPOSURE … (shadows
deep but breathing, even exposure, NO vignette) · CONTINUITY … · NOT …
```

## 12 · FILM LOOK + flare/glow policy (always)

From the bible (verbatim) or `cineoro-light` + `cineoro-camera`.
```
FILM LOOK (KEY — reproduce this exact photographic character): [capture, key, colour, contrast,
grain, softness, frame]. [Lens look paragraph.]
[FLARE/GLOW POLICY — realist default:] NO LENS FLARES: no flares, no light streaks, no floating bokeh orbs, no glow overlays; every light
source stays small and contained.
```

## 13 · SOUND (always)

From `cineoro-sound`.
```
SOUND — [sources in order, with behaviour]; [silence]; [cues with seconds]. [MUSIC POLICY, one of:]
· no score: NO music, NO score, NO BGM, NO instrumental, NO melody, NO ambient pad, NO drone, NO chimes.
· score: [instrumentation, entry second, level under dialogue, how it grows, where it stops].
· the user's track: the song in [audio ref] is the only music; lip-sync and movement land on its
  beats [list the beats/seconds]; no other music.
```

## 14 · WORLD (conditional — specific period/place)

```
WORLD — [place, period]: [materials and objects that exist]; NO [what doesn't]. [Daily-life rule].
```

## 15 · NEGATIVE (always)

From `cineoro-realism`: this shot's failures first, then the scene-type set, then the spine (bible
version if any), minus anything the shot wants.
```
NEGATIVE: [shot-specific failures], [scene-type set], [standing spine].
```

## 16 · ORDER (recap; whenever there is more than one beat)

```
[ORDER: [N] shots, [N] hard cuts, [N]s, [camera language] — (1, 0–5s) …; (2, 5–10s) …; (3, 10–21s)
… hard end mid-[…]. Invariants: [the critical few, one phrase each]. Look: [5–8 words of the FILM
LOOK]. Only [@A] speaks — [N] lines. [Music policy]. [Text policy].]
```

---

## Single-take variant

For a one-shot generation, TIMELINE uses BEATS, CONTRACT says "ONE continuous take, no cuts", ORDER
recaps the beats. Add to LOCKS: "ONE continuous take — WRONG if the camera cuts".

## Compression pass (when a prompt passes ~2,000 words)

Cut in this order and stop as soon as it fits:
1. Decorative adjectives and anything a reference already shows (wardrobe detail on a referenced
   face, architecture on a world plate).
2. NEGATIVE items that the spine and the locks already cover twice; keep the shot-specific ones.
3. ACTING for faces under ~10% of the frame → the short form.
4. GEOMETRY duplicated in the TIMELINE shot lines → keep the numbers in one place.
5. PHYSICS & MATERIAL → keep resistance, gradual states and the OVER-REAL list; drop generic weather.
Never cut: the critical-few repetitions, the music and text policy (whatever it is), the ORDER recap, the voice locks,
the lit-side lock.

## Minimal variant (insert, b-roll, quick test)

CONTRACT · SCENE · TIMELINE (one shot) · CAMERA · LIGHT · FILM LOOK + flare policy · SOUND ·
NEGATIVE. Even a 5-second insert keeps the light source, the camera physics and the look — that is
what lets it cut against the rest of the film.
