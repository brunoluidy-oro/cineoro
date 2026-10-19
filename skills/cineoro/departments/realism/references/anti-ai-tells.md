# Anti-AI-tell catalogue — causes, fixes, examples

The full list behind the short catalogue in SKILL.md. Grouped by where the tell shows.

**Contents:** eyes and faces · frame density · engine weak spots · physics · frame and repetition ·
time (start/end/duration) · sound and text · implied action · the "every block" rule

---

## Eyes and faces

- **Glassy eyes are a frozen pupil, not a highlight.** A reflection of fire or stars is good. Fix with
  movement and cause: a task for the eyes, pupils that search and settle, uneven blinks, brows/cheeks/
  mouth working independently, slight asymmetry.
- **Mad eyes are ACTIVE** — darting and rolling, or wide with visible sclera and a tremor; never a fixed
  doll stare. Clinical markers that read: dilated pupils, sclera, broken breathing, indistinct
  muttering, sweat, shifting micro-expression.
- **Glowing eyes** (officially documented) come from strong emotional wording ("fanatical", "possessed")
  — use neutral words and "normal human eyes; no glowing eyes".
- **Hide the eyes** where the risk is highest (goggles, hood shadow, smoke, silhouette) and play the
  mouth, the jaw and the breath.
- **Skin from keyframes** — when a keyframe has real weathered skin, write "the skin stays exactly as
  in the keyframes: pored, weathered, chapped, alive — no porcelain, no doll face, no beauty smoothing".
- **Two faces close together** — "both faces stay individually readable and never blend or swap
  features".

## Frame density

- Fewer subjects, darker background, fewer sharp faces. "Everything beyond two metres falls into
  darkness."
- Crowds: background in darkness and out of focus; about a metre apart; at most six prop-bearers;
  never clustered; nobody looking at the lens.
- The engine defaults to a centred, evenly lit frame: state the composition (symmetrical or
  off-centre) and the background treatment you chose.
- **Clean frames:** one clear readable composition per beat; no accidental crops through faces.

## Engine weak spots

- **i2v vs t2v:** for a new angle, drop the anchor image and go text + identity references; for a wide
  derived from a close reference, build the wide still first, then animate.
- **Repeat a good shot:** describe the exact angle, light and composition, and reuse its frame as a
  keyframe.
- **Two similar people fighting or embracing:** two clips and a cut, radically different characters,
  or an explicit pose from the first frame; WHO IS WHO mandatory.
- **More than four referenced people:** unstable; reduce, group, darken the rest.
- **Long continuous action:** the hardest thing for the engine. Jump cuts and short shots route around
  it — the gap is a device, not a patch.
- **Words that pull stock objects:** describe geometry instead of naming (negative-library.md).

## Physics

- **Material resists before it gives.** Then gives suddenly.
- **Death is gradual** if intended; freezing, soaking, burning, bleeding take time.
- **Blood** is dark, near-black, viscous; it wells and travels with gravity over time; never bright red;
  on the lens "a real dark droplet, NOT a CGI overlay".
- **Tears** swell, run and freeze.
- **Weight:** heavy things are lifted with effort, set down with a thud; the body counter-leans.
- **Cloth, fur, hair** have weight and settle after moving; wind moves them in one direction.
- **Particles** (snow, dust, smoke, embers) move with the wind and exist in foreground, midground and
  background.
- **Nothing floats, nothing loops.**

## Frame and repetition

- **Camera travels vs stays put** — say which.
- **Distance, darkness and scale** are repeated in every block at once, plus a matching negative. One
  mention is lost.
- **A hidden face** needs "FACE NOT SHOWN, hand / body part only" in every block that could reveal it.
- **A pull-back** is an operator walking backwards, shaking.
- **Artifacts:** remove "gate weave" and "chromatic aberration" together, keep grain moderate, add "NO
  digital artifacts, NO compression trails, NO ghosting streaks".

## Time — start, end, duration

- **Already in progress at the first frame.** The engine's empty or posed opening is a tell.
- **Hard end mid-action** ("hard end mid-rise", "end mid-beat"). The engine otherwise resolves,
  freezes or loops the last second.
- **Generation length = the timeline's sum.** A generation longer than the written timeline stretches
  the last beats into slow, empty seconds (observed: a ~21 s timeline in a 30 s job stretched its fifth
  beat to ~10 s).
- **Gradual and partial states:** START / DURING / END, with negatives in both directions (not
  instantly, not never).

## Sound and text

- Music sneaks in → ban with synonyms at top and end.
- Subtitles appear → no per-word tone tags, no repeated dialogue words, explicit no-subtitles clause.
- Clean digital room tone → "dirty-real location sound", name the sources.

## Implied action (violence, death, intimacy)

- **Off frame:** the hand enters, the movement begins, then the frame ends or the camera holds the face
  and the reaction while the hand leaves past the bottom edge.
- "One short press, NO blood, NO gore" for a killing that must stay implied.
- **Sensitive moment, action partly hidden:** "FACE NOT SHOWN" or "ACTION BELOW FRAME" in every block;
  negative: camera tilting down, reframing to reveal.

## The "every block" rule

What the engine must not lose — distance, darkness, scale, a hidden face, an absent person — is
stated in COMPOSITION/GEOMETRY, in the SHOT text, in CAMERA, in LIGHT where relevant, and fenced in
the NEGATIVE. Say it once and the engine loses it; say it in four blocks and it holds. Use this only
for the critical few (≤5), or the prompt drowns.
