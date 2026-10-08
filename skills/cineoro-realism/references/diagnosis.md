# Diagnosis — symptom → cause → fix → department

Use in repair mode. Look at the take (or the user's description), find the row, change **one block**,
and choose the cheapest regeneration path (edit seconds / keyframe / regenerate — see
`cineoro-assets/references/reference-usage.md`).

**Contents:** faces and acting · identity and casting · space and continuity · camera and lens ·
light and look · physics and behaviour · time and structure · sound and speech · text and artifacts

---

## Faces and acting

| Symptom | Cause | Fix | Dept |
|---|---|---|---|
| Glassy/dead eyes | no task; emotion adjectives; long hold on a face | ACTING tactic + LIVING EYES; shorten the hold; or hide eyes | performance |
| Glowing eyes | strong emotional wording | neutral words + "normal human eyes; no glowing eyes" | performance |
| Mask-like emotion, overacting | emotion labels, facial choreography | replace with tactic verbs; obstacle that is held | performance |
| Listener dead in the reaction | no task for the listener | full ACTING block for the listener | performance |
| Crying looks fake | "crying" as a label | tears physics + break in breath and swallow | performance, sound |
| Character "lucid" when absent | no absence markers | unfocused-but-alive eyes, gaze past the partner, slack mouth, late blinks; negative "lucid" | performance |

## Identity and casting

| Symptom | Cause | Fix | Dept |
|---|---|---|---|
| Face drifted/changed mid-clip | weak identity binding; too many refs | headshot + full-body; name bound to its ref each mention; key refs first | assets |
| Lead's face on extras / twins | no anti-clone; >4 referenced people | anti-clone lock; ≤4 referenced identities; darker crowd | space, assets |
| Two characters swapped features | similar characters in contact | differentiate; split clips; "never blend or swap features" | space |
| Porcelain/beauty skin | beauty words; no texture anchor | over-real skin list; keyframe skin lock; ban porcelain | realism |
| Wardrobe changed between shots | wardrobe not restated | wardrobe state in CAST + lock | assets |

## Space and continuity

| Symptom | Cause | Fix | Dept |
|---|---|---|---|
| Characters swapped sides after a cut | no side ownership/axis lock | WHO IS WHO sides; axis lock repeated in each shot; check the reference image's sides | space |
| Body orientation flipped (lying figure) | no orientation lock | "head frame-RIGHT, gaze frame-LEFT, never flips; rises from the same spot" | space |
| Prop changed hands | no hand lock | "stays in his RIGHT hand in every shot" + negative | space |
| Someone grabbed/held the wrong person | no contact map | CONTACT lock: who touches whom, nobody else | space |
| Empty background after a cut | no population lock | "in EVERY shot the background carries people" | space |
| First frame empty / posed start | no occupancy + no in-progress | first-frame occupancy + "already in progress" | space, director |
| Character far from landmark | vague spatial words | measurable distance + contact with landmark | space |

## Camera and lens

| Symptom | Cause | Fix | Dept |
|---|---|---|---|
| Gimbal/drone smoothness | default stabilization | operator body + NOT list | camera |
| Static when it should move | handheld ≠ travelling | TRAVELS sentence in CAMERA and in the shot line | camera |
| Moves when it should hold | movement words leaked | STAYS PUT sentence + "no pan, no push-in" | camera |
| Lens drifted | no FOV / mixed content | FOV per shot + outcome stack + anti-drift | camera |
| Zoom instead of push-in | "push in/zoom" wording | "rough human walk-in, footstep bounce" | camera |
| Centred symmetrical frame | no composition rule | screen positions + off-centre + negative | camera |
| Mushy framing | crowded beat | clean frames rule; fewer subjects | camera |

## Light and look

| Symptom | Cause | Fix | Dept |
|---|---|---|---|
| Flat, bright, even | no defended darkness | single source, falloff, exposure priority; shadow-side camera | light |
| Dark vignette / crushed blacks | "underexposed/dark" wording | falloff wording + "even exposure, NO vignette; breathing shadows" | light |
| Grey, milky blacks | over-soft film words | "blacks deep and soft, no milky blacks" | light |
| Lit side flipped between cuts | no light continuity lock | fixed source side per shot | light |
| Look changed between shots | look stated once | FILM LOOK lock early + reprise in ORDER | light |
| Lens flares / glow orbs | flare not fenced | NO LENS FLARES block | light |
| Reference's daylight leaked | no reference scope | REFERENCE SCOPE excluding light/grade | assets, light |

## Physics and behaviour

| Symptom | Cause | Fix | Dept |
|---|---|---|---|
| Floaty, weightless motion | no mass/effort | PHYSICS: weight, effort, resistance, settle | realism |
| Smooth elegant "AI" action (one perfect knot) | action as a word | five-part mechanics with failed attempts and tests | performance |
| Invented daily life (wrong tool use) | object without function | name the function; full process | performance, realism |
| Bright red/spurting blood | default gore | dark, viscous, wells, gravity, time — or implied | realism |
| Looping motion | idle tail | hard end mid-action; timeline exactly as long as the job | director |

## Time and structure

| Symptom | Cause | Fix | Dept |
|---|---|---|---|
| Last beat stretched and drags | job longer than the timeline | duration = sum of shot times | director |
| Missing beat / extra cuts | too much in one time range | fewer actions per range; whole-second ranges without gaps | story, director |
| Cuts not where asked | vague cut language | "SHOT N (a–bs) … HARD CUT"; "cuts only at the specified points" | director |
| Action reset after a cut | no continuation phrasing | "continues from the previous shot's action; nothing resets" | space |

## Sound and speech

| Symptom | Cause | Fix | Dept |
|---|---|---|---|
| Music/score/pad | ban stated once | ban with synonyms at top and end | sound |
| Subtitles/captions | tone tags per word; repeated words | one note per line; no-subtitles clause | sound |
| Wrong mouth moving | speaker not locked | ON/OFF labels; non-speaker mouth shut | sound |
| English accent on another language | romanized/ambiguous line | native orthography; language + accent named | sound |
| Smeared word | hard phonemes | different delivery description → simplify spelling | sound |
| Lip-sync drifts late | long line, line at the end | shorter lines; MCU; nothing in the last 1–2 s | sound |
| Voice changed between shots | lock missing | verbatim VOICE LOCK + audio reference | sound, assets |
| Bubbling/echo audio | water/echo words | remove them | sound |
| Chimes/metallic ringing | clean "magical" wording | "dirty-real location sound"; negative | sound |

## Text and artifacts

| Symptom | Cause | Fix | Dept |
|---|---|---|---|
| Garbled on-screen text | text requested | avoid; or spell letter by letter / supply as image | director |
| Banding, ghosting, compression trails | heavy film-artifact words | drop gate weave + chromatic aberration; moderate grain; ban trails | light |
| Fingerprint textures | oversized reference images | downscale refs to ~output resolution | assets |
| Staging-map style in the shot | graphic words in video prompt | remove graphic vocabulary; attach map last | space |
