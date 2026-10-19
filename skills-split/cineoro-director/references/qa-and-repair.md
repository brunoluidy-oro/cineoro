# QA and repair

**Contents:** pre-generation QA (the prompt) · post-generation QA (the take) · repair protocol (Mode C)
· regeneration paths · the repair deliverable · learning loop

---

## Pre-generation QA — the prompt

**Structure**
- CONTRACT opens; ORDER closes (multi-beat); spine order respected; no unused blocks.
- Total seconds = sum of ranges = generation duration (4–30 s); whole seconds, contiguous.
- No scene numbers, no prior-scene leakage, no "as before"; English prompt, lines in their language.

**References and cast**
- Each attachment has one job + SCOPE; upload order = order of first appearance.
- No tag for anything absent from this shot; no stale tags.
- WHO IS WHO with sides, NEVER lists, contact map, anti-clone; ≤4 referenced people.

**Time**
- First frame occupied, action in progress; hard end mid-action.
- One action per range; no overstuffed ranges; lines out of the last 1–2 seconds.

**Performance**
- ACTING for every face (listeners too); tactic verbs; living eyes + one involuntary detail; no emotion
  labels.

**Camera, space, light**
- FOV in degrees per shot; camera body and movement stated; composition as chosen in the STYLE INTENT.
- Measurable distances; axis side; prop hands; orientation across cuts.
- Every source defined (natural or stylized), reach, exposure, NO vignette; lit side locked; flare/glow policy stated.

**Style fidelity (contradiction check)**
- Does anything in LOCKS, NEGATIVE, fences or look phrases forbid what the STYLE INTENT asks for?
- Is any realist-preset default present without a reason from this brief?
- Would the prompt look the same for a different scene? Then it is a template, not a direction.

**Sound**
- Lines labelled (speaker, ON/OFF, seconds, language/accent, delivery); others' mouths shut.
- Music ban with synonyms at top and end; no-subtitles clause; one emotion note per line.

**Realism**
- Physics with resistance; OVER-REAL specific; NEGATIVE shot-specific first; ≤5 critical invariants
  repeated in four places.

## Post-generation QA — the take

Watch it three times: once for the story (does the event land, does the ending hold?), once for
the people (eyes, hands, mouths, identity), once for the frame (sides, light, look, cuts, sound).
Check:
1. Cuts at the right seconds; no extra cuts; no stretched final beat.
2. Identity stable; no clones; wardrobe states right.
3. Sides, axis, prop hands, contact as locked.
4. Eyes alive; no glowing or glassy eyes; listeners doing something.
5. Physics: weight, resistance, no floating, no loop at the end.
6. Light: source side stable, no vignette, no flat fill, no flares.
7. Sound: right speaker, right language/accent, no music, no subtitles, no chimes.
8. Look consistent across the cuts.

## Repair protocol (Mode C)

**First, what kind of prompt failed?**
- **A CINEORO prompt** (it has the spine blocks) → follow steps 1–6 below: change one block, keep the
  rest identical.
- **A one-line or mood prompt** ("a woman lights a campfire, cinematic, dramatic lighting, 4k") → there
  is no block to change. Map each symptom to the words (or the missing instruction) that caused it,
  then **rebuild the whole prompt in the spine** and deliver it like Mode A (header + prompt + card),
  preceded by the diagnosis table. Say plainly that the rebuild replaces the old prompt. Don't attach
  frames of the failed take as keyframes — they carry the failure (dead eyes, wrong light) into the
  new generation.
- **Someone else's structured prompt** (another template) → keep its working parts, move them into the
  spine, and fix the failing parts; note what you moved.

1. **Name the symptom** precisely (which shot, which second, what is wrong).
2. **Find the cause** in `cineoro-realism/references/diagnosis.md`; identify the **one block** (or the
   one lock) responsible.
3. **Choose the cheapest path** (below).
4. **Change only that block** (plus its repetitions in LOCKS/NEGATIVE/ORDER if it is a critical
   invariant). Keep everything else byte-identical so the next take isolates the fix.
5. **Draft first**, check the fixed thing, then finalize.
6. **Log the lesson** in the project bible (§2 anti-AI-tell rules) if it is likely to recur.

## Regeneration paths, cheapest first

| Problem scope | Path |
|---|---|
| Audio only (music, a wrong sound) | audio edit of the take ("remove the background music; keep everything else") |
| 1–3 seconds wrong, rest good | timestamped edit of the take ("from 4 to 6 seconds … leave the rest unchanged") |
| Take good but too short / ends early | extend forward |
| One shot of a multi-shot wrong | regenerate the generation with the fixed block; attach frames of the good shots as keyframes |
| Performance wrong, composition right | regenerate with a keyframe from the take + the fixed ACTING block |
| Speech smeared | regenerate same line with a new delivery description → then simplified spelling |
| Systemic (axis, clones, light, look) | fix the block, repeat the invariant in four places, regenerate (draft first) |

## The repair deliverable

For a one-line/mood prompt: a diagnosis table (symptom · cause in the old wording · fix ·
department), then the full Mode A deliverable, then "what to check in the draft" and the fallback
ladder (audio edit → first-frame keyframe → ACTING-only regenerate). For a CINEORO prompt:

```
DIAGNOSIS: [symptom] → [cause] ([department]).
PATH: [edit / extend / keyframe regenerate / regenerate].
[Edit instruction, if editing — exact wording.]
CHANGED BLOCKS: [only the changed blocks/lines, ready to paste]
CHECK IN THE DRAFT: [what to look at first]
```

## Learning loop

Every repaired failure that could recur becomes:
- a project anti-AI-tell rule (symptom + fix + date) in the bible;
- a NEGATIVE item for that scene type;
- if structural, a new lock in the relevant reference prompt.
The bible grows from failures; that is how a long project stops repeating them.
