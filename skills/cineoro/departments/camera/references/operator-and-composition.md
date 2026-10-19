# Operator behaviour and composition

Read for any shot where the camera moves, any multi-shot, any shot where framing failed last time,
or any scene whose meaning lives in how the camera behaves.

**Contents:** camera as a point of view · movement library · speed (real-time vs slow-motion) ·
multi-shot camera continuity · composition grammar · aspect-ratio grammar · failure → fix

---

## The camera's point of view is a directing decision

Decide who the camera *is* before writing it:
- **The observer walking alongside** (documentary): handheld, late, unstaged, jump cuts. Strips out
  stagedness and routes around the engine's hardest limit — long continuous action.
- **The author** (composed): designed frames, stillness, deliberate moves; used at the key moments of
  a film so they feel different from the observed coverage around them.
- **The character** (POV): the camera's height, breath and gaze are the character's.
Mixing them deliberately is a strong design: documentary coverage for daily life, a switch to a
composed, authored form for the turning points.

## Movement library

| Move | Write it as | Engine default to block |
|---|---|---|
| Breathing static | "stays in one place and breathes: small tremor, a few degrees off level, a drift that arrives a beat late" | tripod lock, perfect level |
| Walk-with | "walks beside him at shoulder height, never behind; footfall bounce; framing a beat late" | gimbal glide, back-of-head following |
| Lead | "walks backwards in front of her, 2 m ahead, her face toward the lens" | drone pull |
| Arc | "arcs slowly around him by about 40° while he works, jolting with each step" | perfect orbit, 360° circling |
| Rough push-in | "rough human walk-in from medium to close-up, trembling, footstep bounce" | dolly-in, zoom |
| Pull-back | "the operator walks backwards, shaking the whole way, nearly losing the frame once" | crane/drone reveal |
| Crouch drift | "drifts down with his crouch, settling at knee height" | elevator move |
| Whip | "settled ≥0.3 s → fast whip with motion blur ≥0.8 s → settled ≥0.3 s" | hard cut instead of a whip |
| Jolt | "a hard JOLT with the shove, the frame whipping half a beat after her" | no reaction to impact |
| Low tower | "camera on the ground, lens tilted up, the figure towering" | chest-height camera |
| Snow-level / floor-level | "lens at the level of the snow, the crust filling the lower third" | eye level |
| Vehicle | "mounted on the side of the vehicle at door height, road vibration, wind buffeting" | smooth tracking |

Rules:
- **One movement per shot.** If the beat needs two (walk-with then push-in), split it with a cut or
  state the order and the moment of change ("then, on the line '…', the operator steps in").
- **Motion is caused.** The camera reacts to events (jolts on impact, flinches on a gunshot, holds a
  startled micro-pause on a loud sound).
- **Handheld intensity is dosed:** subtle / gentle / moderate / strong. Over-dosed shake reads as
  digital jitter.
- **Blocking the engine's smoothing:** when handheld is the language, lock it — "NOT ONE SECOND
  static, locked or stabilized, never a glide; NOT a gimbal, NOT a drone, NOT a slider".

## Speed — real-time and slow motion

- Default: "real-time motion".
- Each shot runs at **one speed from start to finish**; mix speeds only across hard cuts. A speed ramp
  inside one shot breaks the motion model.
- Slow motion must be motivated (impact, memory, sensory overload) and stated with what it reveals
  ("water droplets suspended", "snow bursting in slow arcs").
- Platform speed-ramp settings exist on some front-ends; when the scene must be real-time, say so in
  the prompt as well.

## Multi-shot camera continuity

For each shot inside a single generation give: duration (seconds), shot size + FOV, camera position
(height, side, distance), movement, focus, and the cut type into the next. Across the shots hold:
the side of the axis, the lit side of the faces, the screen direction of movement, gaze targets.
Typical rhythm for 20–30 s generations: 3–6 shots of 3–7 s; a key shot (the reversal) gets the longest
duration and a single movement.

## Composition grammar

- **Thirds and weight:** the subject in a third, the look-room on the side of the gaze; negative space
  on the side the danger or the absent person is.
- The engine's default is centred, evenly lit, background readable. Whatever composition you choose —
  off-centre chiaroscuro (observed) or rigorous symmetry (authored, comic, ritual) — state it, so the
  default doesn't win.
- **Foreground:** one soft shape at a frame edge (a shoulder, a post, a fur ruff) adds depth and
  realism; a frame-filling blur is mush.
- **Background:** state a distance beyond which everything falls into darkness or softness ("nothing
  readable beyond two metres").
- **Faces:** never crop through the eyes or the mouth by accident; extreme close-ups crop on purpose
  (brow to collar so the mouth reads).
- **Headroom and horizon:** horizon out of frame for intimate low angles; a horizon line high for
  burden, low for exposure.
- **Clean frames rule** (paste when shots came back mushy): "every beat is ONE clear, deliberate,
  readable composition — one focal point, intentional edges. NO mushy half-framings, NO accidental
  crops through a face, NO confused staging."

## Aspect-ratio grammar

- **21:9 / 2.39:1** — people small in vast space; two-shots can hold both faces at the thirds;
  singles leave large negative space; ideal for landscape-as-pressure films.
- **16:9** — neutral cinema/TV.
- **9:16 vertical** — one subject owns the frame; stack foreground/background vertically; avoid wide
  two-shots; camera closer, wider FOV (63–84°) to keep the environment.
- **1:1 / 4:5** — portrait-like, centred compositions become acceptable.
Always state the aspect ratio in the CONTRACT line and keep it in the negative ("wrong aspect ratio,
square frame, vertical frame" for a scope film).

## Failure → fix

| Symptom | Fix |
|---|---|
| Lens drifted toward a middle focal length | FOV per shot + outcome stack + anti-drift lock |
| Smooth gimbal/drone look | operator body language + explicit NOT list + "never a glide" |
| Camera static when it should move (or vice versa) | TRAVELS / STAYS PUT sentence, repeated in the shot line |
| Push-in became a zoom | "rough human walk-in", footstep bounce, "no zoom" |
| Centred, symmetrical frame | off-centre placement with screen positions + "asymmetric" + negative "centred, symmetrical" |
| Mushy framing, crops through faces | clean frames rule |
| Wrong side of the axis after a cut | axis lock with `cineoro-space`; camera side stated in every shot |
| Hidden action revealed by a reframe | "the camera never tilts down; ACTION BELOW FRAME" in every block |
