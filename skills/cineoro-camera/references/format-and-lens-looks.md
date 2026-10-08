# Format and lens looks — paste-ready blocks

A project's lens look is decided once (in the project bible, `cineoro-bible`) and pasted verbatim into
every prompt. Never rewrite it per shot — consistency across a film comes from identical text.

**How a look block works:** an optional format anchor (a name the engine has seen a lot of) +
the observable outcomes that actually control the image + a short "NOT" tail naming the digital
default it must not fall back to.

**Dosing words** (put one in front of the effects): subtle · gentle · moderate · strong · maximum.

**Artifact caveat (observed in production):** if the engine starts throwing banding, strange
artifacts or ghosting, remove "gate weave" and "chromatic aberration" together, keep grain moderate,
and add "NO digital artifacts, NO compression trails, NO ghosting streaks". The rest of the block
survives.

---

## A · Hard anamorphic, large format (epic, cold, monumental)

```
HARD ANAMORPHIC LOOK (KEY): true 65mm ANAMORPHIC — [21:9] aspect ratio, strong squeeze, oval
elliptical bokeh, horizontally stretched highlights, gentle barrel edge stretch (geometric only, no
edge darkening), shallow cinemascope focus, anamorphic focus breathing; heavy organic film grain,
halation, slight softness — NOT over-sharpened, NOT digital-clean, NOT a crisp AI look.
```

## B · Spherical large format (intimate, natural, modern arthouse)

```
LENS LOOK (KEY): large-format spherical lens character — round bokeh, very shallow focus with a
gentle falloff, natural perspective, soft wide-open rendering at the edges; fine organic grain,
soft highlight roll-off — NOT over-sharpened, NOT digital-clean.
```

## C · 16mm documentary (raw, urgent, intimate)

```
LENS LOOK (KEY): 16mm documentary film character — visible coarse grain, slightly soft lenses,
modest depth of field, highlights that bloom, occasional focus search; colour slightly muted and
warm in the shadows — NOT clean digital, NOT sharp 4K.
```

## D · Vintage spherical (period, warm, memory)

```
LENS LOOK (KEY): vintage spherical prime character — low contrast wide open, soft glowing
highlights, swirly out-of-focus background, mild warm flare veil only from in-frame practicals, fine
grain — NOT modern clinical sharpness.
```

## E · Clean modern digital cinema (commercial, crisp but not AI)

```
LENS LOOK (KEY): modern cinema-camera image — natural sharpness without edge enhancement, gentle
highlight roll-off, rich shadow detail, very fine grain/noise, realistic skin texture with pores —
NOT over-sharpened, NOT HDR, NOT the glossy AI look.
```

## F · Vertical social / phone-real (UGC, found footage)

```
CAPTURE LOOK (KEY): handheld phone footage — 9:16, small-sensor deep focus, auto-exposure breathing,
slight rolling-shutter wobble on fast moves, mild compression, natural mixed white balance — NOT
cinematic shallow focus, NOT colour-graded.
```

---

## Writing a new look block

1. Pick the anchor only if it helps (a format the engine knows).
2. List **4–8 outcomes** a viewer could point at in the frame.
3. Add a **NOT** tail with the 2–4 digital defaults the look must avoid.
4. Test it on 2–3 different scene types before locking it in the bible.
5. Lock it: the block goes into the project bible as a verbatim template, and every prompt pastes it.

## Naming a reference film or cinematographer

Production prompts have used a reference title + cinematographer as a look anchor ("a night still
out of [film] ([director] / [DP])"). Treat it the same way as a format name: optional, never alone,
always followed by the observable description. Do not chain several names — the averages blur. If
the platform or brand context makes names undesirable, drop the name and keep the outcomes; the
outcomes carry the control.
