# Reference usage and the iteration loop

**Contents:** syntax by platform · roles in detail · reference hierarchy · keyframes · the iteration
loop · draft → final · edit (timestamped) · extend and chain · previous take as reference · stale-tag
hygiene

---

## Syntax by platform

| Platform | How to cite an attachment in the prompt |
|---|---|
| BytePlus ModelArk (official) | `@Image 1`, `@Video 1`, `@Audio 1` — numbered by upload order (variants like "Image 1" are tolerated) |
| fal.ai | `@Image1`, `@Video1`, `@Audio1` |
| Replicate | `[Image1]`, `[Video1]`, `[Audio1]` |
| Higgsfield (web) | type `@` and pick the upload or the saved Element; production prompts were stored with tokens like `<<<image_1>>>`, `<<<audio_1>>>` and `<<<element-id>>>` |
| Dreamina / Jimeng | `@` mentions in the app |

Rules that hold everywhere: describe each mapping in words ("@Image 1 is the old fisherman — face,
hands, wardrobe"); don't write names on the images; upload in the order subjects first appear; in
edit/extend tasks write "Video 1", not "reference Video 1" (otherwise the task can be read as a
reference task).

Free-text tags (`@SLED`, `@DOG`) next to attached images are fine as handles; bind them once in
REFERENCES ("@SLED = Image 4, object only").

## Roles in detail

- **IDENTITY** — face, build, hands, marks, wardrobe. Headshot + full-body (or a multi-view sheet) per
  character. Restate critical details in words.
- **KEYFRAME FOR SHOT N** — an exact frame the shot starts from; followed strictly. Name what is in it
  (one line), so the text and image agree.
- **FIRST / LAST FRAME** — platform roles for the whole clip's start/end. Some providers don't allow
  combining them with other references; the workaround is to pass them as references and name them in
  the prompt ("Image 3 is the first frame, Image 5 is the last frame") — less strict.
- **WORLD** — location plate(s): architecture, materials, clutter, atmosphere. Not lens, not light
  unless it is the keyframe.
- **OBJECT ONLY** — props on neutral backgrounds: shape, scale, material, wear.
- **VOICE** — 5–10 s of clean speech; bound to one character; describe the voice in words too.
- **MOTION** — a video whose movement (action, expression, camera move) is copied; scope everything
  else out.
- **3D CLAY / PREVIZ** — official 2.5 role for motion and lighting from an untextured model; scope hard
  ("movement, blocking and light direction only") and attach after the photo references.
- **STORYBOARD** — up to 15 line-art panels as loose plot guidance.
- **STYLE** — a look reference; never let it override identity, blocking, optics or lighting.
- **PREVIOUS TAKE** — an earlier generation used as a video reference while correcting it (see below).

## Reference hierarchy

Identity references control face/body/costume. Location references control architecture, geography
and atmosphere. Prop references control shape, scale, state and contact. A style or location
reference never overrides identity, blocking, optics or lighting. If a reference image contradicts the
text (positions, sides), the image usually wins — fix the image.

## Keyframes

- One keyframe per key shot inside a multi-shot generation is enough; the others "continue this exact
  look, mise-en-scène and texture with no keyframe".
- Keyframes carry the grade and the **skin texture** — write "the skin stays exactly as in the
  keyframes: pored, weathered, alive — no porcelain, no beauty smoothing".
- Keyframes come from: approved frames of earlier takes; stills built in an image model; frames
  extracted at the exact moment of a previous take.
- "Comes alive from it": the shot starts on that frame and moves; it does not hold it frozen.

## The iteration loop

1. **Generate** (draft if available).
2. **Check** against the QA list (`cineoro-director/references/qa-and-repair.md`).
3. **Diagnose** the one block that failed (`cineoro-realism` has the symptom → cause → fix table).
4. **Choose the cheapest fix:**
   - wrong for 1–3 seconds → **edit** those seconds;
   - right but too short → **extend**;
   - composition right but performance wrong → regenerate with a **keyframe** from the take + the
     fixed ACTING block;
   - speech smeared → regenerate with a different delivery description;
   - systemic (wrong axis, clones, wrong light) → fix the block and regenerate.
5. **Change one block per retake** so you know what fixed it.
6. **Promote** approved frames to keyframes, clean lines to voice references, the take to the cut.

## Draft → final

`draft` renders a 480p preview; finalizing the same draft renders 1080p **without resending the prompt
or assets** (resending causes an error even with identical values; draft IDs expire after 7 days).
Use drafts to check blocking, timing and cuts before paying for 1080p.

## Timestamped edit

```
Edit Video 1: from 4 to 6 seconds, [the change: her right hand stays on the rope; the knife never
appears]; leave the rest of Video 1 unchanged — same framing, light, performance and sound.
```
Edits require the adaptive ratio and the model-chosen duration; input 4–30 s. Trigger words: edit,
add, insert, remove, delete, modify, replace, change to. A mismatch between the task type and the
wording raises an error.

## Extend and chain

- **Extend** forward or backward from a clip ("continue from the end of Video 1: …"), 4–30 s, repeatable
  (quality can degrade over many rounds).
- **Chain** generations with the last frame of one as the first frame of the next. If the join jumps,
  trim ~6 frames from the end of the first and ~1 from the start of the next.
- **Transition** generates the missing segment between two clips.

## Previous take as a reference

When a take is close, attach it as a video reference with a hard scope ("Video 1 is the previous take:
keep its framing, timing and light; change only [X]") and attach its best frames as keyframes for the
shots that must not move.

## Stale-tag hygiene

Never place a tag in a shot where that element is not present — the engine will force it into frame.
Never carry a tag from a previous shot. Version tags (`_v2`, `_v3`) and reference only the active one.
