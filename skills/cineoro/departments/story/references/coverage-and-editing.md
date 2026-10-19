# Coverage and editing — from scene to generations

**Contents:** budgeting a scene into generations · shot patterns inside a generation · cut types ·
hand-offs between generations · motifs and rhymes · runtime planning · the director's statement as
function

---

## Budgeting a scene into generations

1. Run the dramatic read; mark tactic switches (T1, T2…), the reversal (R) and the value shift (V).
2. Group beats into generations of **4–30 s**, each a mini-sequence that ends on a natural cut point:
   - a generation never splits R;
   - a generation may hold one or two tactic switches;
   - the last generation of the scene contains V and holds on it.
3. For each generation write: purpose, duration, shot count, first-frame state, last-frame state.
4. Prefer more, shorter generations for complex physical action; fewer, longer ones for pressure held
   on faces.

Example (a 70-second scene): G1 (0–22 s, 4 shots: setup → T1) · G2 (22–44 s, 3 shots: T2 escalates) ·
G3 (44–70 s, 2 shots: R held 14 s on her face → V on his reaction, hard end).

## Shot patterns inside a generation

- **Alternating singles** (him / her / him / her, no wide): pressure dialogues, pursuit. Each shot
  states its own size and side; the last shot can bring both faces together.
- **Process in jump cuts:** 4–6 beats of the same action from different positions, same side of the
  axis, small time-skips.
- **One take with internal beats:** BEAT ranges inside a continuous shot ("0–4s… 4–9s…") to place
  events and lines without cuts.
- **Wide → push:** a wide establishing the space already in action, then a rough walk-in to the face for
  the reversal.
- **Insert pattern:** a 2–3 s detail (hands, object) between two faces; it must carry information, not
  decoration.

## Cut types

`HARD CUT` (default) · `JUMP CUT` (same subject, time-skip, new position, same axis side) · `SMASH CUT`
(abrupt contrast) · `MATCH CUT` (shape or motion rhymes) · `INSERT CUT` · `REVERSE CUT` · `WHIP` (needs
settle time on both ends). Fades and dissolves only on explicit request. State "cuts only at the
specified points; the camera adds no cuts of its own" whenever you specify cuts; state "ONE continuous
take, no cuts" when there are none.

## Hand-offs between generations

The engine has no memory, so continuity between generations is designed:
- write the **end state** of generation N in detail (positions, prop hands, wardrobe states, light,
  emotional state) and make it the **first-frame state** of N+1;
- chain with the last frame of N as the keyframe/first frame of N+1 when exact continuity matters
  (`cineoro-assets`);
- for emotional continuity only: "Prior audio context only, not visual content: '[line]'".

## Motifs and rhymes (planned here, executed as locks)

- **One gesture, first and last** — a physical action that opens and closes the film; lock its exact
  mechanics both times.
- **A line that changes meaning** — the same words in a new mouth or new situation; never change one
  word.
- **A loop** — the film opens and closes on the same image or creature, with the meaning inverted.
- **A paid-three-times structure** — the same exchange made three times, explained once.
- **A colour or light exception** used once (with `cineoro-light`).
- **A sound motif** (breath, a drum, a lullaby) that returns at the turns (with `cineoro-sound`).

## Runtime planning

- Set a hard ceiling for the film. Decide what compresses into short inserts (transit, routine) and
  what is never cut (the processes that buy belief, the turning points).
- Count generations × seconds early; the ceiling is a directing tool, not an afterthought.

## The director's statement as function

Every visual choice serves the story's mechanism, not a style:
- *A body surviving next to a mind coming apart* → natural light only, people small in vast space,
  a live handheld operator walking with them.
- *Cold is the permanent state, warmth is man-made* → palette and light system.
- *Low angle when the world presses down; canted horizon only when control is lost.*
- *Documentary cuts for life, an authored form at the turns.*
Write the statement once in the project bible (`cineoro-bible`); this department applies it per scene.
