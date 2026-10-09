# Style intent and divergence — how the tree stays open

The tree carries three kinds of rules. Confusing them is what makes prompts rigid: a stylistic habit
starts behaving like a law of physics. Read this at the start of every project, and whenever a brief
asks for something that sounds like it breaks a CINEORO rule.

## The three tiers

| Tier | What it is | Can a project override it? |
|---|---|---|
| **ENGINE LAW** | How Seedance 2.5 behaves, whatever the style: no memory between generations; duration = timeline (or the end stretches); whole-second contiguous ranges; >4 referenced people is unstable; one job per reference; the engine adds music, subtitles and a centred, evenly lit, mid-focal frame **unless told otherwise**; dead/glowing eyes, clones and warped hands are failure modes | No. These are facts about the tool. |
| **METHOD** | Directing craft that serves any style: an acting task instead of an emotion; write the visible; measurable space; every choice motivated by the scene; state the policy for anything the engine would otherwise decide (music, composition, light, motion) | No — but it is expressed in the project's own idiom (a clay puppet's "task" is still a task). |
| **STYLE** | Aesthetic choices: handheld vs locked vs crane; natural vs expressive light; score vs silence; photoreal vs stylized medium; grain vs clean; off-centre vs symmetrical; real-time vs slow motion; muted vs saturated; glow and flares or none | **Yes, always.** The brief and the bible decide. |

The **CINEORO REALIST preset** (natural motivated light, observed handheld, no score, film grain,
off-centre chiaroscuro, real-time, photoreal, no flares) is **one** style, inherited from the source
production. It is the fallback only when the user expresses no style — never a correction to a style
the user asked for.

Engine-law phrasing for style questions: the law is "**state a policy**", not "pick the realist one".
Music sneaks in → state the music policy (none / score described / the user's track). The engine
centres everything → state the composition (symmetrical or off-centre). The engine flattens light →
state the light (natural or neon gels or magic glow, with a source and a behaviour).

## Step 0.5 — the STYLE INTENT (before any department)

Read the brief (or the bible) and fix, in one block for yourself:

```
STYLE INTENT
MEDIUM: [live-action photoreal / stylized live-action / stop-motion / 2D / 3D animation / mixed]
REGISTER: [observed-realist / authored-composed / subjective-expressionist / genre spectacle /
           commercial-graphic / music video / social-phone / other]
CAMERA LANGUAGE: [handheld / locked / dolly-crane / impossible camera / phone] and why
LIGHT LOGIC: [natural motivated / stylized practicals (neon, gels) / magic or fantastical sources
             with defined behaviour / studio high-key]
SOUND/MUSIC POLICY: [no score (ban with synonyms) / score (described) / user's track as audio ref /
                    source music / heightened sound design]
COLOUR & TEXTURE: [muted / saturated / pastel / graphic; grain / clean; glow & flares allowed?]
MOTION: [real-time / slow motion where / stepped animation]
REALIST PRESET RULES SWITCHED OFF: [list — e.g. "no score", "no flares", "off-centre", "handheld"]
```

Then every department works **inside** this intent:
- the NEGATIVE never forbids something the intent requires (no "symmetrical" in a symmetrical film,
  no "glow" in a neon clip, no "cartoon" in an animation, no "music" when there is a score);
- the OVER-REAL list becomes **material truth of the chosen world** (clay fingerprints and armature
  wobble; pristine lacquer in a pastel tableau; scales and wet stone in a fantasy) — never grime
  pasted onto a pristine idiom;
- "believability" means **internal consistency of the world's rules**, not photorealism.

## Divergence — open before you close

Convergence (decide, lock, repeat) is what makes a film consistent. Divergence must come **first**,
or the first idea becomes the only idea.

1. **New project (Mode D):** before freezing anything, propose **2–3 directions** — genuinely
   different readings, not cosmetic variants. For each: one line of intent, camera language, light
   logic, sound policy, and what the audience feels differently. Example axes: observed vs authored vs
   subjective; restraint vs spectacle; inside the character's head vs outside watching. The user picks
   or mixes; the bible records the choice and the rejected options (they are useful later for
   deliberate breaks).
2. **Key scenes (the reversal, the opening, the ending):** after the prompt, add one line
   `ALTERNATIVE DIRECTION:` with a materially different approach (another POV, another time
   structure, another performance tactic) — cheap to read, easy to ask for.
3. **On request** ("me dá opções", "variações", "outra abordagem"): deliver 2–3 complete prompts that
   differ in directing decisions (camera POV, structure, tactic, light logic) — not in adjectives.
4. **Examples are calibration, not templates.** Worked examples and scene-type skeletons show density
   and order. Never inherit their camera, light, sound or palette choices — derive each from this
   scene's meaning. A useful test: *would this prompt look the same if the scene were different?* If
   yes, it is a template, not a direction.

## Every key choice has a reason

In the plain-language header, add one line: `DIRECTION: [the 2–3 choices that make this shot this
shot, and why]`. A choice that can't be justified from the scene or the project is a default — either
justify it or change it.

## Contradiction check (QA)

Before delivering, read the prompt against the STYLE INTENT: anything the intent asks for that a lock,
a NEGATIVE item, a fence (NO LENS FLARES) or a look phrase forbids is a contradiction — fix it. Typical
ones: "halation on the neon" vs "no glow"; "rigorous symmetry" vs over-real asymmetric defects; "slow
motion" vs a handheld breathing operator; "score swells" vs "NO music".
