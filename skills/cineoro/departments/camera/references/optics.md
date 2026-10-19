# Optics — lens control library

Read when writing the OPTICS line, choosing lens character, building any multi-shot, or fixing a shot
that drifted lens. Origin: the `cinedance` optics library, extended for Seedance 2.5 production.

**Contents:** principle · decision tree · language bank per FOV · telephoto stack · wide stack ·
multi-shot consistency · anti-drift locks · named optical techniques · anti-patterns

---

## Principle

Seedance responds to observable lens **results**, not to camera metadata. Control with diagonal
field of view in degrees, physical camera distance in metres, and the visible optical outcome.
`85mm`, `f/1.4`, `ISO 800` and lens model names (Cooke, Master Prime, Helios, K35…) are ignored or
break complex moves when used as primary control. A **format** name ("65mm anamorphic") can anchor
texture when paired with outcome phrases — see `format-and-lens-looks.md`.

## Lens decision tree (choose silently from content)

**Face portrait**
- close intimate face with environment visible → 84° intimate wide
- medium portrait → 29° short telephoto
- tight emotional close-up → 18° classic telephoto
- distant hidden observation → 8° super-telephoto with foreground occlusion

**Environmental action**
- natural documentary action → 47° (or 63° walking with the subject)
- wide environmental action → 84°
- large-scale geography → 107°
- extreme immersion → 135° only if the whole beat is environmental

**Detail / macro**
- standard detail → 29° or 18°
- detail inside a wide environment → detail-on-wide (below)
- never mix macro detail with wide environmental action in one beat — split it with a cut

**Observation at distance** → 8° (sports, paparazzi, wildlife, surveillance), occlusion + haze.

## Language bank — paste into OPTICS

**47° standard normal**
```
47° diagonal field of view, standard normal lens character, camera 3 to 5 metres from the subject,
natural human-eye perspective. No obvious distortion, natural proportions, comfortable depth of
field, background readable but not exaggerated, grounded cinema framing.
```

**63° observational**
```
63° diagonal field of view, observational lens character, camera 1.5 to 2.5 metres from the
subject, walking with them. Environment readable around the subject, mild perspective expansion,
reportage feel, focus following the subject.
```

**84° classic wide / intimate wide**
```
84° diagonal field of view, classic wide-angle lens character, camera 1 to 1.5 metres from the
subject, slight low angle if needed. Strong but natural perspective expansion, foreground presence
larger and closer, environment visible to the frame edges, deep readable spatial context, straight
lines stay rectilinear, no fisheye curve.
```

**107° wide rectilinear**
```
107° diagonal field of view, wide rectilinear lens character, camera 0.5 to 0.8 metres from the
foreground subject. The immediate foreground looms large, the environment spreads to all frame
edges, deep edge-to-edge focus, straight lines remain straight, no circular vignette, no fisheye
bubble.
```

**29° short telephoto portrait**
```
29° diagonal field of view, short telephoto portrait lens character, camera 4 to 6 metres from the
subject. Close framing achieved through lens reach, not physical proximity. Subject razor-sharp,
background compressed closer behind, stable face proportions, background dissolving into soft bokeh.
```

**18° classic telephoto**
```
18° diagonal field of view, classic telephoto lens character, camera 6 to 8 metres from the subject.
Strong background compression, distant elements stacked close behind the subject, razor-thin focus
on the eyes, foreground and background melting into soft bokeh, the image feels observed from a
distance.
```

**8° super-telephoto observation**
```
8° diagonal field of view, super-telephoto observation lens character, camera 20 to 25 metres from
the subject. Extreme compression, background flattened into a soft colour wash, only the subject
sharp. Feels like distant documentary observation. Foreground occlusion: blurred foreground objects
occupy the lower 30 to 45 percent of the frame as oversized dark bokeh shapes.
```

## Telephoto outcome stack — include at least 4 in any tele shot

background blurred into a soft wash · razor focus on the subject · only the subject is sharp ·
creamy bokeh behind the subject · background compressed flat · subject pops against a dissolved
background · close framing through lens reach, not proximity · camera far from the subject in
physical space · atmospheric haze between camera and subject · foreground occlusion as soft dark
bokeh

## Wide-angle outcome stack — include at least 3 in any wide shot

foreground looms larger than natural · environment visible around the subject · deep edge-to-edge
focus · straight lines stay rectilinear · wide spatial context to the frame edges · camera
physically close to the subject · immersive close perspective · no telephoto compression

## Multi-shot lens consistency

- **Same lens across shots:** "LENS IS X° ACROSS ALL SHOTS." Open each shot with "LENS X°" and close
  with "X° maintained, no drift".
- **Mixed lens:** a shot earns its own lens only when the content type changes; hard cuts only
  between lens characters — no smooth FOV transitions inside a shot.
- **Extreme FOV (8°, 107°) — all four mechanisms or the sequence degrades after 2–3 beats:**
  1. one location reference across all beats; 2. FOV phrase at the start of each beat;
  3. FOV confirmation at the end of each beat; 4. colour via material + light, never as a list.

## Anti-drift locks (use only when the risk is real)

- **Telephoto:** "No part of this shot becomes wide-angle or normal-lens coverage. Wider framing is
  achieved by the camera being farther away with the same long-lens reach, not by switching lenses.
  The background stays compressed and dissolved in every frame."
- **Wide:** "No part of this shot becomes telephoto portrait coverage. The environment stays visible
  around the subject, the camera stays physically close, and the image keeps wide spatial expansion."
- **Normal:** "No extreme wide distortion, no telephoto compression; natural, human-eye neutral."

## Named optical techniques

- **Observation pattern (hidden camera)** — all three at once: foreground occlusion over 20–30% of the
  frame; atmospheric haze between camera and subject; distance vantage at 8°–12°. Change the
  occlusion type between beats, keep the vantage single.
- **Sports broadcast** — 8° + handheld 1–2 cm tremor + "anchored at distance, finding the action".
- **Detail-on-wide (snake cam)** — 84° + low angle right up against a small object; foreground object
  exaggerated, background receding.
- **Intimate wide** — 63–84° on a close face; surroundings readable without blur.
- **Compressed air column** at 8°–12° — "dust/snow suspended in the long compressed air between camera
  and subject", "heat shimmer compressed into a wall in front of the figure".
- **Low-angle tower** — 84° at ground level, the subject towering, sky or ceiling behind.

## Anti-patterns — never write these

"extreme / ultra / super wide-angle lens" · "wide shot" or "establishing shot" *as a lens
instruction* · "zoom out plus wide-angle" · "tight wide framing" · f-stop/ISO/brand as primary
control · compound camera movements in one shot · mixed content classes in one beat · negative-only
lens control
