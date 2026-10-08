---
name: cineoro-performance
description: Acting department of the CINEORO directing tree for Seedance 2.5 video prompts. Builds the ACTING block for every face on camera — the invested tactic (event, motive, goal, obstacle, tactic, moment-to-moment) plus the living-eyes physiology layer that kills glassy AI stares — and describes behaviour as body mechanics instead of poses. Use it whenever a prompt has a character, an animal or a crowd on camera, whenever a generated take came back with dead eyes, doll faces, melodrama, overacting, frozen listeners or fake crying, and whenever the user asks how a character should play a moment. Triggers include "acting task", "the eyes are dead", "olhar de vidro", "atuação", "como ele reage", "make her cry believably", "madness scene", "he looks like a doll". Called by cineoro-director; also use it on its own for performance questions.
---

# CINEORO · PERFORMANCE

The camera believes behaviour, not skin. Photoreal faces are already solved by the engine; a face
that is *doing something* is not. This department gives every person on camera real work, so the
emotion is produced by the work instead of being painted on.

You write the **ACTING** block (one per character with a face in frame), the performance side of
each beat in the **TIMELINE**, and you contribute the scene's **SOUL** line with `cineoro-story`.

---

## The four laws

1. **Nobody plays the emotion; everyone plays the direction.** "She is devastated" produces a mask.
   "She hums to keep him calm while her hands finish the knot" produces devastation in the viewer.
   The audience receives the feeling through the pressure of the obstacle, never from an adjective.
2. **The tactic is a verb aimed at someone or something.** Convince, calm, test, hide, measure,
   provoke, protect, stall. If you cannot point at whom the verb lands on, it is not a tactic.
3. **The eyes are where the tactic is visible.** Give the eyes a job — checking both of the
   partner's eyes for a sign of trust, stealing a look and snapping back, measuring the distance to
   the door. A mind visibly working is what reads as alive.
4. **Two layers, never confused.** The **TASK** is the cause (what the mind is doing). **LIVING
   EYES** is model safety (the involuntary physiology every living face has: saccades, uneven
   blinks, asymmetry). You may prescribe physiology. You never prescribe the *emotional*
   expression ("brows lift sadly", "lips tremble with fear") — that is playing the result, and the
   engine renders it as a mask.

---

## Procedure — run it in this order

0. **Read the whole scene first**, every line of every character. A task built from one line is
   wrong by construction.
1. **Name the scene's shared direction** — the one unspoken agreement all characters play toward
   ("make the goodbye painless", "keep it routine"). It is not the film's theme; characters never
   play the film's purposes.
2. **Name the event from the ending.** Read the last beat first; the scene is read backward through
   it. The event must contain every character, including silent or unconscious ones.
3. **Give each character a motive** — a different fuel pushing the same direction. This is what
   makes two performances distinct while the scene stays unified.
4. **Goal → obstacle → tactic** per character. The obstacle is what presses against the direction —
   usually the real feeling trying to surface. One crack and the scene collapses; that pressure is
   what the audience feels.
5. **Moment to moment**, keyed to the dialogue words *and to the seconds of the timeline*. Mark the
   point where a character's fuel runs out and the line breaks — if the script breaks it.
6. **Living eyes** for each face: one physiological liveness line + **one involuntary detail** that
   the tactic causes (a held breath, a late blink, a swallow that cuts a phrase, the jaw setting once).
7. **Behaviour as mechanics** — what the hands, weight and feet are doing, written as physics, not
   as a word (see `references/behaviour-mechanics.md`).
8. **Name the wrong performances** this shot invites (melodrama, crying aloud, looking into the
   lens, a lucid face where the character is absent) and hand them to the director as locks and
   negatives.

Full definitions, the contrast-pairing method and approved worked examples:
**read `references/acting-task.md` before writing any ACTING block.**

---

## The ACTING block — template

```
ACTING — @NAME (fully invested in the tactic; the work happens in the eyes)
SCENE DIRECTION (shared, unspoken): [one line]
EVENT: [what really happens to everyone here, named from the ending]
MOTIVE (his/her fuel): [why THIS person pushes that direction]
GOAL: [the personal fight inside the scene]
OBSTACLE: [what presses against the line; what one crack would cost]
TACTIC: [verb at the partner/object + the eye-work as action]
MOMENT TO MOMENT:
— [0.0–3.5s] "[line or action]" — [verb at the partner] + [what the eyes check]
— [3.5–7.0s] "[line or action]" — [verb] + [eye-work]
— [where the line breaks, if it breaks — and what holds after]
LIVING EYES: pupils move with the task — search, settle, drift, settle again; blink cadence
uneven and a beat late; brows, cheeks and mouth work independently, slight asymmetry. Involuntary
detail: [one, caused by the obstacle]. A reflection of [the scene's light source] in the eyes is
fine; a FROZEN PUPIL or fixed glassy stare is wrong.
NOT: [3–5 wrong performances specific to this beat]
```

Short form for a background character or a one-beat insert:

```
ACTING — @NAME: TACTIC [verb at target]; eyes [the job]; involuntary detail [one]; NOT [wrong
performance].
```

**Silent listeners get a full block.** Their task is real ("decide if he is lying", "protect the
mood", "wait for the moment to leave"). At the reversal, the value shift often lands on the
listener's face — that is the shot.

---

## Living eyes — the glassy-stare toolkit

The single most common AI tell is the dead eye. It is a **frozen pupil**, not a missing highlight.
Fixes, in order of strength:

1. **A task for the eyes** (law 3). Always first.
2. **Physiological liveness line** in the ACTING block (template above).
3. **Active states are active.** Madness, fear, fever: darting and rolling eyes, or wide with
   visible sclera and a tremor — never a fixed doll stare. Readable clinical markers: dilated pupils,
   visible sclera, broken breathing, indistinct muttering, sweat, micro-expressions that never
   settle.
4. **Hide the eyes where the risk is highest** and play the mouth, jaw and breath instead: goggles,
   a hood's shadow, a hat brim, smoke, backlight silhouette, a profile turned away, hands over the
   face. A face hidden on purpose must be stated in every block that could reveal it
   (see `cineoro-realism`).
5. **Gaze target is concrete and off-lens.** "eyes lock on her mouth", "past the camera into the
   dark frame-left" — never "looks into the distance", never into the lens unless the film breaks
   the fourth wall.

Never fix dead eyes with catchlights or lighting tricks; fix them with work.

---

## States that need body physics, not adjectives

| State | Write this (mechanics) | Never this |
|---|---|---|
| Holding back tears | breath catches, a swallow cuts the phrase, a note goes wet and closes in the throat, eyes over-blink | "she is about to cry" |
| Crying | tears swell at the lid, run along the nose, the nose runs; breath shudders on the inhale | "sobbing loudly", "crying beautifully" |
| Whisper / failing speech | lips barely moving, almost no jaw, words dissolving into breath on the exhale | the word "whisper" (hand delivery to `cineoro-sound`) |
| Exhaustion | movements a half-beat late, hands that miss and retry, weight sinking between steps | "tired" |
| Cold | stiff fingers that won't curl, breath fog torn by wind, shoulders up, talking through teeth | "freezing" |
| Pain | the body protects the injured side, a stop before each move, breath held then released through the nose | "in agony" |
| Madness / absence | concrete tactics of an absent person — the body keeps doing what a life taught it, correctly, in the wrong context | "acting crazy", "maniacal" |
| Shock | delayed reaction, the action continues automatically for a beat, the hands keep doing the last task | "shocked face" |
| Laughter | breath-driven, hitching, restarting, the body folds; under tension it is short and wrong | "laughs maniacally", "villain laugh" |
| Rage held | jaw grinding, words spat as stones, eyes avoiding the target half a beat | "furious face", "snarling" |

More states, animals, children and crowds: `references/living-eyes-and-states.md`.

---

## Behaviour, not poses

What the hands do decides whether the viewer believes the person. Every action a character performs
is written as **mechanics with resistance**: what the material does back, how many attempts it
takes, where the weight goes, what is tested after. Not "she ties him to the sled" but "she takes a
turn around the post, threads the end back, jerks the first knot down hard — the stiff strap springs
back — lays a second knot, hauls it tight with two pulls, tests it twice". Library of mechanics:
`references/behaviour-mechanics.md`.

---

## Contrast pairing (two-handers)

Build the pair on mirrored plus/minus: each character carries one + and one −, inverted against the
partner, and you name the **essential axis** the audience reads (e.g. care for the patient). Both
still push the same scene direction; the contrast leaks through the tactics and the eyes. Details
and an approved example: `references/acting-task.md`.

---

## Hand-off to the director

Return to `cineoro-director`:
- one **ACTING** block per face in frame (full or short form);
- the performance verbs for each beat of the **TIMELINE**, with seconds;
- the **SOUL** line (with `cineoro-story`): the inner logic of the scene in one or two sentences,
  "to be played, never explained";
- **locks** for the performance failures this shot invites (e.g. "she never looks at his face",
  "his mouth stays shut — the voice is off-screen") and the matching **negatives**.

## Checklist

- Is every tactic an active verb aimed at someone or something — not an adjective?
- Does every face in frame, including silent listeners and background faces that read, have work?
- Is there exactly one involuntary detail per face, caused by the obstacle?
- Does the obstacle explain why the face looks the way it will?
- Is the emotional expression left unprescribed, with only physiology and task written?
- Are the moment-to-moment beats keyed to the same seconds as the TIMELINE?
- Could a real actor play this from your text alone?
