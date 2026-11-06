"""Prompts de vídeo (Seedance 2.5, Higgsfield) para ALEGRINHA NA TAMPINHA, na espinha COMPLETA da CINEORO.

Ordem dos blocos: CONTRACT · REFERENCES · WHO IS WHO · SCENE & SOUL · ABSOLUTE LOCKS · TIMELINE · ACTING · CAMERA ·
GEOMETRY · PHYSICS & MATERIAL · LIGHT · FILM LOOK · SOUND · WORLD · NEGATIVE · ORDER.
Os blocos repetidos do mundo são colados idênticos em cada prompt (cada geração é uma ilha: o motor não tem memória).
Regra do diretor: nunca "lid"/"cap"/"tampa": sempre FOIL, uma lâmina de alumínio maleável.
PROMPTS[k] = (título, segundos da geração, texto); segundos = soma dos planos. Prompts em inglês.
"""


def _join(*blocks):
    return "\n\n".join(b.strip() for b in blocks if b)


# ===========================================================================
# MUNDO LIVE (captação)
# ===========================================================================
LIVE_LOOK = (
    "LOOK (KEY — reproduce this exact photographic character): 35mm color negative look. Organic grain, fine to "
    "medium, alive in the shadows and midtones. Soft highlight roll-off with gentle warm halation blooming around windows, "
    "sunlit patches and bright skin edges; highlights creamy and warm, never pure white. Blacks slightly lifted and never "
    "crushed, shadows holding detail with a faint cool teal-green cast. Vintage spherical glass character: moderate "
    "micro-contrast, slight softness toward the frame edges, a gentle natural vignette darkening the corners, subtle "
    "chromatic fringing on high-contrast edges. Colour comes from the place itself — the real materials, surfaces and light "
    "of each location — never a grade laid over it; skin golden and natural with visible pores and texture. Photoreal live-action footage, 16:9, real-time 24fps cadence with natural motion blur. NOT a render, NOT HDR, NOT the glossy AI look.\n"
    "NO LENS FLARES: no flares, no light streaks, no floating bokeh orbs; the warm halation stays soft and contained around "
    "bright edges."
)

LIVE_SCOPE = (
    "REFERENCE SCOPE: image references supply identity, wardrobe, objects and architecture ONLY — their light, grade and "
    "surfaces are replaced by what is written below."
)

PREVIZ_SCOPE = (
    "CAMERA MOVE ONLY: copy just the path, framing, distance and speed of its camera. Take NOTHING else from it — not its hands, "
    "objects, shapes, colours, surfaces, lighting, textures or the timing of the hand action; those come only from the text "
    "and the image references. The footage must look like real live-action, never like the previz."
)
CREQUI_CAM = "[video reference] CRÉQUI PREVIZ — {shot}. " + PREVIZ_SCOPE
FOIL_CAM = "[video reference] FOIL PREVIZ — {shot}. " + PREVIZ_SCOPE

LIVE_WORLD = (
    "WORLD — the Brazilian summer kitchen of @loc_cozinha, with its tiles, fridge, window and furniture exactly as the "
    "reference shows them and nothing added. NO legible writing anywhere (any magnet, note or label is unreadable colour), NO "
    "other brand, NO other people."
)

LIVE_LIGHT = (
    "LIGHT — NATURAL LIGHT ONLY, a summer afternoon (KEY): warm daylight from the window side at FRAME-LEFT (~3800 K), with "
    "patches of sun on the green tile wall and on the frame-left side of his face; the fridge's cool light (~5000 K) only "
    "while its door is open. Highlights roll off warm, shadows hold detail. The lit side never flips."
)

LIVE_NEG_SPINE = (
    "smoke, vapour, steam, cartoon or clay hands, oversized hands, stiff robotic motion, glassy stare, frozen pupils, warped hands, extra fingers, a second person, speech or lip-sync, "
    "readable text, invented logos, stiff foil, subtitles, handheld shake, CGI-gloss look, cartoon look, wrong aspect "
    "ratio."
)

MACRO_NEG = "fisheye, circular black border, round lens mask, black corners, curved straight lines, "

MUSIC_BAN = (
    "AUDIO: only the sounds listed here, with quiet room tone between them; nothing else is heard — NO music. NO voice-over."
)

# Lente macro com sonda (24 mm tipo Laowa Probe): o visual, dito uma vez; o movimento vem de cada plano e do previz
MACRO_LENS = (
    "MACRO PROBE LENS (KEY): a 24 mm probe macro, about 74° horizontal: the object at the tip is huge and crisp on a thin "
    "plane of focus, nearby things pass soft in the foreground, the room falls away into soft colour; wide perspective with "
    "straight lines. A full, clean 16:9 frame edge to edge — NO fisheye, NO circular black border."
)

HANDS = "his hands are real human hands with natural proportions, skin and fluid motion; "

DOOR_ITEMS = (
    "the inside of the open door shows the usual Brazilian fridge-door items, all plain and unlabeled: a carton of eggs, a "
    "water bottle, a juice jug, a jar of preserves, butter in a dish"
)

KITCHEN_GEOMETRY = (
    "he faces the camera, so his RIGHT hand is on the frame-left side (the counter, the sunlit side) and his LEFT hand on the "
    "frame-right side (the fridge); the camera never crosses to the far side of the fridge"
)


def live_contract(secs, shots, extra=""):
    return (
        "CONTRACT — Live-action photoreal raw camera footage with production sound only, 16:9, %d seconds total, %s, real-time "
        "motion. Deadpan, played completely straight. No dialogue (a voice-over is added in post)%s. NO music, NO "
        "subtitles, NO on-screen text." % (secs, shots, extra)
    )


def who_man(role, never="NEVER speaks, NEVER removes his glasses"):
    return (
        "WHO IS WHO — @man-portoalegre (round black glasses, dark curly hair, short beard, sage-green check short-sleeve shirt "
        "over a white T-shirt, thin silver bracelet on his LEFT wrist — 100% matches its reference) — the MAN: " + role + "; "
        + never + ". He is alone; nobody else appears, not even as a reflection."
    )


def acting_man(task, moments, detail, nots, direction="treat the small thing as sacred."):
    # forma enxuta (comédia seca): direção, tarefa em uma linha, momento a momento, olhos, NOT
    return (
        "ACTING — @man-portoalegre (deadpan, played completely straight; the work happens in the eyes)\n"
        "DIRECTION: " + direction + "\n"
        "TASK: " + task + "\n"
        "MOMENT TO MOMENT: " + moments + "\n"
        "EYES: alive in every hold — they search and settle, blinks a moment late; involuntary detail: " + detail + "\n"
        "NOT: " + nots
    )


TRAY_TEXT = (
    "a tray of exactly SIX pink ribbed yogurt cups joined in one block, each sealed with FOIL — a thin, soft aluminum sheet "
    "printed green that bends and crinkles, never stiff."
)
PAIR_TEXT = (
    "exactly TWO pink ribbed yogurt cups joined side by side by a thin plastic break line, each sealed with soft green-printed "
    "FOIL."
)
FOIL_TEXT = (
    "a thin, soft aluminum sheet, SQUARE with small rounded corners like the square rim of the cup, printed green on the "
    "outside; its inner face is bare SILVER covered edge to edge with a generous, creamy layer of pink yogurt stuck to it, "
    "about 3–4 mm thick, only a thin silver line at the edges — plenty, but true to one small cup, never a heap. It bends and "
    "crinkles, never stiff; NO tab, NO writing."
)

LIVE_WORLD = (
    "WORLD — the Brazilian summer kitchen of @loc_cozinha exactly as the reference shows it: the green tile wall with sun at "
    "FRAME-LEFT, the stainless fridge at FRAME-RIGHT, the counter in front of him. NO legible writing, NO other brand."
)

LIVE_SCOPE = (
    "REFERENCE SCOPE: references supply identity, wardrobe, objects and architecture ONLY — their light, grade and "
    "surfaces are replaced by what is written below."
)

# Planos compartilhados entre os takes separados e a 1d (texto idêntico)
FRIDGE_SHOT = (
    "MCU, 84°, locked off INSIDE the fridge on the middle shelf, 0.7 m from the doorway, looking out; right in front of the "
    "lens on the shelf sits ONE PAIR of two joined yogurt cups, the only yogurt there. At the first frame the door is CLOSED "
    "and the frame is dark. [0–1s] He pulls the door open toward frame-left: the fridge light comes on and his face appears "
    "in the doorway; " + DOOR_ITEMS + ". [1–2s] Eyes on the pair just beside the lens, a slow smile. [2–4s] His right hand "
    "reaches in, covers the lens for a moment, grips the pair across BOTH cups and pulls it out: the two joined cups, foil up, "
    "the break line between them, clearly visible in his hand as they leave the fridge. [4–5s] His left hand swings the door "
    "shut toward the lens and the frame goes dark."
)
SNAP_SHOT = (
    "extreme close-up with the macro probe, in front of him and above his hands (" + HANDS.rstrip("; ") + "): the pair is "
    "held LOW, at the height of his belly, well below his face. Each hand grips one cup in a C — fingers wrapped around the "
    "side and under the cup, the THUMB flat on top of that cup's foil. The probe starts 3 cm above the two foils and the two "
    "thumbs and makes ONE steady pull-back with a slight rise through the whole shot, revealing the pair at belly height and "
    "his shirt soft behind. Gently and smoothly, without force, moving ONLY his wrists — forearms, elbows and shoulders stay still — he closes the pair like closing a book: the joint between the cups RISES "
    "into a ridge while the two cup BOTTOMS swing toward each other underneath (an upside-down V; the foils tilt outward, away "
    "from each other); at {snap} the break line gives with a crisp, bright crack — the créqui — and he lowers the two cups "
    "apart, level, one in each hand."
)
NOSTALGIA_SHOT = (
    "TIGHT CLOSE-UP, 29°, only 0.5 m from his face, the camera diagonal — about 35° toward his right side — and 20 cm ABOVE "
    "his eye line looking down: a three-quarter, slightly high angle. His face fills the frame from chin to hairline; his "
    "hands are below frame; the tile wall soft behind, no ceiling. A moment after the crack he nods slightly, a few small up-and-down nods of quiet approval, with a light smile; then he glances down toward the sink at frame-left, where his right hand, below frame, sets the other cup down. He never looks upward and never into the lens."
)
FOIL_SHOT = (
    "extreme close-up with the macro probe beside his right hand (" + HANDS.rstrip("; ") + "): the back of that hand large and "
    "soft in the foreground at frame-left, its fingertip under the near edge of the foil; the cup held in his left hand at "
    "chest height at frame-right; the tile wall soft behind. ONE gentle, continuous push-in: the fingertip lifts the near edge "
    "and the foil hinges up on its far edge like a little door opening toward the lens, rising almost upright, its "
    "yogurt-coated silver side turned to the camera, the open cup and its pink yogurt below; then it comes free of the rim in "
    "his fingers."
)
LICK_SHOT = (
    "MCU, 47°, 0.8 m away, the camera diagonal — about 35° toward his right side — and 15 cm above his eye line: a "
    "three-quarter, slightly high angle, locked off. The open cup in his left hand at chest height; the foil, now pulled off, in "
    "his right hand. Casually, the way anyone cleans a yogurt lid, he brings the foil to his mouth and licks the yogurt off its "
    "silver side in one quick, matter-of-fact lick, eyes OPEN and looking at the foil the whole time. At {freeze} the image "
    "FREEZES mid-lick — foil at his mouth, eyes open on the foil — and stays frozen, like a photograph, to the end."
)

# ===========================================================================
# 1a — POV da geladeira (4 s)
# ===========================================================================
P_1A = _join(
    live_contract(5, "ONE locked-off shot"),
    "REFERENCES — each reference has ONE job:\n"
    "@man-portoalegre — IDENTITY of the man. 100% matches.\n"
    "@loc_cozinha — WORLD: the kitchen.\n"
    "@prop_pote-morango — OBJECT ONLY: the reference shows ONE cup; in this shot he takes TWO of them joined side by side "
    "as one pack.\n" + LIVE_SCOPE,
    who_man("opens the fridge, reaches in, takes a pair of joined yogurts and shuts the door; he never looks into the lens"),
    "SCENE & SOUL — SCENE: a summer afternoon in a Brazilian kitchen, seen from inside the fridge. He opens the door, takes a "
    "pair of joined yogurt cups and shuts the door. Already in progress.\n"
    "THE SOUL OF THE SCENE (play it, never explain it): the most important small ritual of his day, and nobody knows.\n"
    "THE PAIR — " + PAIR_TEXT,
    "ABSOLUTE LOCKS — break one and the take is WRONG, regenerate:\n"
    "1. He takes a PAIR: TWO cups joined side by side, both in his hand — WRONG if a single cup, a tray or another count.\n"
    "2. The pair is clearly visible as it leaves the fridge.\n"
    "3. The camera is LOCKED OFF inside the fridge; he never looks into the lens.\n"
    "4. The door starts CLOSED and he opens it on camera; it shuts toward the lens at the end and the frame goes dark.",
    "TIMELINE — ONE shot, already in progress:\n"
    "SHOT 1 (0–5s) — " + FRIDGE_SHOT + " Hard end on the dark frame.",
    acting_man(
        "collect the day's reward, keeping the pleasure under control. Tactic: savour — a moment slower than needed, so the "
        "moment lasts.",
        "— [0–1s] he opens the door, eyes already searching — [1–2s] eyes settle on the pair, the smile arrives late — [2–4s] the "
        "hand goes in and comes out with the pair, eyes following it — [4–5s] a satisfied glance as the door closes.",
        "his eyes narrow slightly against the fridge light.",
        "mugging, laughing, looking into the lens, presenting the pair.",
    ),
    "CAMERA — authored, designed camera: locked off, STAYS PUT, 84°; level horizon. NOT: handheld shake, push-in, zoom.",
    "GEOMETRY — the camera sits where the pair was, 0.7 m from his face; the door swings from frame-left.",
    "PHYSICS & MATERIAL — the door swings with weight and seals with a soft thump; the pair is cold and light. OVER-REAL: a "
    "light film of condensation on the cups, the weave of his shirt, stubble and pores. If any surface looks smooth, plastic "
    "or rendered — WRONG.",
    LIVE_LIGHT, LIVE_LOOK,
    "SOUND — the door seal letting go as it opens; the fridge hum; the foil's faint crinkle; the seal's soft thump at the end. " + MUSIC_BAN,
    LIVE_WORLD,
    "NEGATIVE: a single cup, one cup alone, a tray, the door already open at the first frame, the product hidden as it leaves, any camera movement, " + LIVE_NEG_SPINE,
    "[ORDER: 1 locked-off shot, 5s — inside the fridge: the door opens, his hand covers the lens, pulls out the pair, clearly "
    "seen, and the door shuts to dark. Invariants: TWO joined cups, never one; the door opens on camera; never into the lens; locked off. Look: 35mm negative. NO text.]",
)

# ===========================================================================
# 1b — O créqui (5 s)
# ===========================================================================
P_1B = _join(
    live_contract(5, "2 shots with 1 hard cut at 3s"),
    "REFERENCES — each reference has ONE job:\n"
    "@man-portoalegre — IDENTITY of the man. 100% matches.\n"
    "@loc_cozinha — WORLD: the kitchen.\n"
    "@prop_pote-morango — OBJECT ONLY: one yogurt cup; here two of them are joined.\n" + LIVE_SCOPE,
    who_man("splits a pair of joined yogurts with a crisp snap and keeps one cup"),
    "SCENE & SOUL — SCENE: the same kitchen, moments later. He holds the pair of joined cups he just took from the "
    "fridge and splits it with a crisp snap. Already in progress.\n"
    "THE SOUL OF THE SCENE (play it, never explain it): the snap is the sound he came for, and it takes him back to "
    "childhood.\n"
    "THE PAIR — " + PAIR_TEXT,
    "ABSOLUTE LOCKS — break one and the take is WRONG, regenerate:\n"
    "1. Two joined cups before the snap, exactly two after.\n"
    "2. THE FOLD: a C-grip, thumb flat on each cup's foil, the pair at BELLY height; gently, like closing a book, the joint RISES and the cup BOTTOMS swing together — WRONG if the joint dips, if he twists or pulls it apart, or holds it at face height.\n"
    "3. His LEFT hand keeps one cup; his RIGHT hand sets the other on the counter.\n"
    "4. Shot 2 is a THREE-QUARTER, slight HIGH angle (no ceiling in frame); he nods slightly with a light smile, then glances down toward the sink; never upward, never into the lens.",
    "TIMELINE — 2 shots, 1 hard cut:\n"
    "SHOT 1 (0–3s) — " + SNAP_SHOT.format(snap="2s") + " HARD CUT.\n"
    "SHOT 2 (3–5s) — " + NOSTALGIA_SHOT + " Hard end.",
    acting_man(
        "get the snap clean and take it in without showing how much it matters. Tactic: savour — straight in, no hesitation, "
        "then a few small nods of approval.",
        "— [0–2s] hands only — [2s] the crack — [3–4s] a few small nods of quiet approval, a light smile — [4–5s] he glances down toward the sink as he sets the other cup down.",
        "his shoulders drop a millimetre at the crack.",
        "sitcom delight, mugging, looking into the lens, looking down at the cup, a pause before the snap.",
    ),
    "CAMERA — Shot 1: the macro probe TRAVELS in one steady pull-back. Shot 2: locked off, STAYS PUT, 29°.\n" + MACRO_LENS,
    "GEOMETRY — " + KITCHEN_GEOMETRY + ".",
    "PHYSICS & MATERIAL — the break line resists, then gives all at once with a sharp snap, no splinters, both cups intact and "
    "sealed; the counter takes the cup with a small knock. OVER-REAL: the ridge where the break line parted, foil creases, "
    "condensation, fine hairs on his thumbs. If any surface looks smooth, plastic or rendered — WRONG.",
    LIVE_LIGHT, LIVE_LOOK,
    "SOUND — the créqui, a short, crisp, bright plastic snap, the most important sound of the scene; the foil's crinkle; a light knock on "
    "the counter; his breath. " + MUSIC_BAN,
    LIVE_WORLD,
    "NEGATIVE: " + MACRO_NEG + "moving arms or elbows during the fold, a wide or medium shot instead of the close-up, a previz or clay look, doll-like hands, the joint dipping down, a pair twisted or pulled apart, three cups, a pause before the snap, a low "
    "angle with the ceiling in frame, " + LIVE_NEG_SPINE,
    "[ORDER: 2 shots, 1 hard cut, 5s — (1, 0–3s) macro pull-back from the thumbs, the gentle book-like fold, the snap at 2s; "
    "(2, 3–5s) three-quarter slight high angle, small approving nods, light smile, a glance down to the sink. Invariants: two cups separated; left hand "
    "keeps one; full 16:9 frame. Look: 35mm negative. NO text.]",
)

# ===========================================================================
# 1c — O foil e a lambida (6 s)
# ===========================================================================
P_1C = _join(
    live_contract(6, "2 shots with 1 hard cut at 2s"),
    "REFERENCES — each reference has ONE job:\n"
    "@man-portoalegre — IDENTITY of the man. 100% matches.\n"
    "@loc_cozinha — WORLD: the kitchen.\n"
    "@prop_pote-morango — OBJECT ONLY: the yogurt cup and its green foil.\n" + LIVE_SCOPE,
    who_man("opens the cup in his left hand and licks the yogurt off the foil"),
    "SCENE & SOUL — SCENE: the same kitchen. He opens the cup he kept; the foil comes away with yogurt on it and he licks it, "
    "and the image freezes. Already in progress.\n"
    "THE SOUL OF THE SCENE (play it, never explain it): opening the cup is serious business; licking the foil is pure habit, done without thinking.\n"
    "THE FOIL — " + FOIL_TEXT,
    "ABSOLUTE LOCKS — break one and the take is WRONG, regenerate:\n"
    "1. Cup in his LEFT hand, foil in his RIGHT; the FINGERTIP lifts the foil — no nail, no tab — and pulls it off.\n"
    "2. The silver side comes away with a generous 3–4 mm layer of pink yogurt and faces the lens as it opens — WRONG if clean or heaped.\n"
    "3. NO text or message on the foil.\n"
    "4. The last second is a TOTAL FREEZE mid-lick.",
    "TIMELINE — 2 shots, 1 hard cut:\n"
    "SHOT 1 (0–2s) — " + FOIL_SHOT + " HARD CUT.\n"
    "SHOT 2 (2–6s) — " + LICK_SHOT.format(freeze="5s"),
    acting_man(
        "clean the yogurt off the foil, the way anyone does. Tactic: none — he licks it casually, out of habit, without emotion.",
        "— [0–2s] hands only — [2–3s] a plain look at the foil — [3–4s] he lifts the foil — [4–5s] a quick lick, eyes "
        "open on the foil — [5–6s] frozen.",
        "none.",
        "mugging, a sensual or slow lick, closed eyes, pleasure or savouring, looking into the lens, any movement after the freeze.",
    ),
    "CAMERA — Shot 1: the macro probe TRAVELS in one gentle push-in. Shot 2: locked off, STAYS PUT, 47°.\n" + MACRO_LENS,
    "GEOMETRY — " + KITCHEN_GEOMETRY + "; in shot 2 the lens is 35° toward his right side, so the foil hand is nearer.",
    "PHYSICS & MATERIAL — the foil lifts at one edge and comes away without tearing; the yogurt coat is thick, creamy and "
    "clinging and does not drip; each lick wipes a clean silver stripe and leaves a slight smear at his lip. OVER-REAL: "
    "creamy yogurt on bare silver, foil creases, the ring where the foil sealed the rim, pores. If any surface looks smooth, "
    "plastic or rendered — WRONG.",
    LIVE_LIGHT, LIVE_LOOK,
    "SOUND — the foil's soft crinkle; a small wet lick; his breath; near silence at the freeze. " + MUSIC_BAN,
    LIVE_WORLD,
    "NEGATIVE: " + MACRO_NEG + "moving arms or elbows during the fold, a wide or medium shot instead of the close-up, a previz or clay look, doll-like hands, a sensual or slow lick, closed eyes, pleasure on his face, savouring, tongue play, a round foil, a round cup, a thin smear of yogurt, a fingertip pinch grip, the pair held at face height, a fingernail or pull tab, a clean silver side, a heap of yogurt, a message on the foil, any movement after the "
    "freeze, " + LIVE_NEG_SPINE,
    "[ORDER: 2 shots, 1 hard cut, 6s — (1, 0–2s) macro beside his hand, push-in, the foil opens like a little door, yogurt "
    "side to the lens; (2, 2–6s) three-quarter slight high angle, the lick, FREEZE from 5s. Invariants: cup left, foil right; "
    "a real layer of yogurt; fingertip; no text. Look: 35mm negative. NO text.]",
)

# ===========================================================================
# 1bc — Créqui + foil + lambida numa geração só (11 s), substitui 1b e 1c
# ===========================================================================
P_1BC = _join(
    live_contract(11, "4 shots with 3 hard cuts at 3s, 5s and 7s"),
    "REFERENCES — each reference has ONE job:\n"
    "@man-portoalegre — IDENTITY of the man. 100% matches.\n"
    "@loc_cozinha — WORLD: the kitchen.\n"
    "@prop_pote-morango — OBJECT ONLY: the yogurt cup and its green foil; in shot 1 two of them are joined.\n"
    + CREQUI_CAM.format(shot="for shot 1") + "\n" + FOIL_CAM.format(shot="for shot 3") + "\n" + LIVE_SCOPE,
    who_man("splits the pair he just took from the fridge with a crisp snap, keeps one cup, opens it and licks the foil; he "
            "never looks into the lens"),
    "SCENE & SOUL — SCENE: the same summer kitchen, right after he took a pair of joined cups from the fridge. In four shots: "
    "the snap; one cup kept; the foil; the lick; the image freezes. Already in progress.\n"
    "THE SOUL OF THE SCENE (play it, never explain it): the snap takes him back to childhood; then licking the foil is pure "
    "habit, done without thinking.\n"
    "THE PAIR — " + PAIR_TEXT + " THE FOIL (shots 3–4): " + FOIL_TEXT,
    "ABSOLUTE LOCKS — break one and the take is WRONG, regenerate:\n"
    "1. Two joined cups before the snap, exactly two after; NO tray. THE FOLD: C-grip, thumb flat on each foil, at belly height; gently, like closing a book, the joint RISES and the cup BOTTOMS swing together — WRONG if the joint dips.\n"
    "2. C-GRIP at belly height for the fold, wrists only; his LEFT hand keeps the same cup to the lick; his RIGHT fingertip lifts the foil and pulls it off. Real human hands.\n"
    "3. The silver side comes away with a generous 3–4 mm layer of yogurt — never clean, never a heap; no text on the foil.\n"
    "4. Shot 2 is a TIGHT three-quarter CLOSE-UP (face fills the frame) and shot 4 a three-quarter MCU, both slight HIGH angles from the same side, 35° toward his right; daylight from "
    "FRAME-LEFT; macro frames are full 16:9, no circular border.\n"
    "5. The last second is a TOTAL FREEZE mid-lick.",
    "TIMELINE — 4 shots, 3 hard cuts:\n"
    "SHOT 1 (0–3s) — " + SNAP_SHOT.format(snap="2s") + " HARD CUT.\n"
    "SHOT 2 (3–5s) — " + NOSTALGIA_SHOT + " HARD CUT.\n"
    "SHOT 3 (5–7s) — " + FOIL_SHOT + " HARD CUT.\n"
    "SHOT 4 (7–11s) — " + LICK_SHOT.format(freeze="10s"),
    acting_man(
        "take in the snap without showing how much it matters, then get every bit of yogurt off the foil. Tactic: savour — no "
        "hesitation at the snap, let the sound carry him away, then the lick is casual, a habit. ",
        "— [0–2s] hands only, the crack at 2s — [3–4s] a few small nods of quiet approval, a light smile — [4–5s] he glances down toward the sink as he sets the other cup down — [5–7s] hands only — [7–8s] a plain "
        "look at the foil — [8–9s] he lifts the foil — [9–10s] a quick lick, eyes open on the foil — [10–11s] frozen.",
        "his shoulders drop a millimetre at the crack; none.",
        "sitcom delight, mugging, looking up, big nods, looking into the lens, a pause before the snap, a sensual or slow lick, closed eyes, "
        "savouring, any movement after the freeze.",
    ),
    "CAMERA — Shot 1: one steady macro pull-back. Shots 2 and 4: locked off, STAY PUT, 29° and 47°. Shot 3: one gentle macro "
    "push-in. Natural, fluid camera moves, never mechanical.\n" + MACRO_LENS,
    "GEOMETRY — " + KITCHEN_GEOMETRY + "; in shots 2 and 4 the lens is 35° toward his right side, so the right hand is nearer.",
    "PHYSICS & MATERIAL — the break line resists, then gives all at once with a sharp snap, no splinters, both cups sealed; the "
    "counter takes the cup with a small knock; the foil lifts without tearing; the yogurt layer is creamy and clinging and "
    "does not drip; each lick wipes a clean silver stripe and leaves a slight smear at his lip. OVER-REAL: condensation on the "
    "cups, the ridge where the break line parted, foil creases, yogurt on bare silver, pores. If any surface looks smooth, "
    "plastic or rendered — WRONG.",
    LIVE_LIGHT, LIVE_LOOK,
    "SOUND — the créqui at 2s, a short, crisp, bright plastic snap, the most important sound of the scene; a light knock on the counter; "
    "the foil's crinkle; a small wet lick; his breath; near silence at the freeze. " + MUSIC_BAN,
    LIVE_WORLD,
    "NEGATIVE: " + MACRO_NEG + "moving arms or elbows during the fold, a wide or medium shot instead of the close-up, a previz or clay look, doll-like hands, a sensual or slow lick, closed eyes, pleasure on his face, savouring, tongue play, a round foil, a round cup, a thin smear of yogurt, the pair held at face height, a tray, the joint dipping down, a pair twisted or pulled apart, a pause before the snap, a low angle, a different cup in "
    "his left hand, a clean silver side, a heap of yogurt, any movement after the freeze, " + LIVE_NEG_SPINE,
    "[ORDER: 4 shots, 3 hard cuts, 11s — (1, 0–3s) macro pull-back, the gentle book-like fold at 2s; (2, 3–5s) tight three-quarter close-up, small approving nods, light smile, a glance down to the sink; (3, 5–7s) macro push-in, the foil opens like a little door; (4, 7–11s) the "
    "same three-quarter side, the lick, FREEZE from 10s. Invariants: two cups separated; the same cup in the left hand; a real layer of "
    "yogurt; real hands; daylight frame-left. Look: 35mm negative. NO text.]",
)

# ===========================================================================
# 1d — Cena 1 inteira (1a + 1b + 1c) numa geração só (15 s)
# ===========================================================================
P_1D = _join(
    live_contract(16, "5 shots with 4 hard cuts at 5s, 8s, 10s and 12s"),
    "REFERENCES — each reference has ONE job:\n"
    "@man-portoalegre — IDENTITY of the man. 100% matches.\n"
    "@loc_cozinha — WORLD: the kitchen.\n"
    "@prop_pote-morango — OBJECT ONLY: the yogurt cup and its green foil; it shows ONE cup, but in shots 1–2 he holds TWO joined side by side.\n"
    + CREQUI_CAM.format(shot="for shot 2") + "\n" + FOIL_CAM.format(shot="for shot 4") + "\n" + LIVE_SCOPE,
    who_man("takes a pair of joined yogurts from the fridge, splits it with a crisp snap, keeps one cup, opens it and licks "
            "the foil; he never looks into the lens"),
    "SCENE & SOUL — SCENE: one uninterrupted ritual in a summer kitchen, in five shots: the pair from the fridge; the snap; "
    "one cup kept; the foil; the lick; the image freezes. Already in progress.\n"
    "THE SOUL OF THE SCENE (play it, never explain it): the most important small ritual of his day, and nobody knows; the "
    "snap takes him back to childhood.\n"
    "THE PAIR — " + PAIR_TEXT + " THE FOIL (shots 4–5): " + FOIL_TEXT,
    "ABSOLUTE LOCKS — break one and the take is WRONG, regenerate:\n"
    "1. A PAIR of TWO joined cups (shots 1–2), never a single cup; two separate cups after the snap. The fridge door opens on camera.\n"
    "2. THE FOLD: C-grip, thumb flat on each foil, at belly height; gently, like closing a book, the joint RISES and the cup BOTTOMS swing together — WRONG if the joint dips.\n"
    "3. C-GRIP at belly height for the fold, wrists only; the LEFT hand keeps the cup; the RIGHT fingertip lifts the foil and pulls it off, with a generous 3–4 mm layer of yogurt. Real human hands.\n"
    "4. Shot 3 is a TIGHT three-quarter CLOSE-UP (face fills the frame) and shot 5 a three-quarter MCU, both slight HIGH angles; daylight from FRAME-LEFT; macro frames are full 16:9, no "
    "circular border.\n"
    "5. The last second is a TOTAL FREEZE mid-lick.",
    "TIMELINE — 5 shots, 4 hard cuts:\n"
    "SHOT 1 (0–5s) — " + FRIDGE_SHOT + " HARD CUT.\n"
    "SHOT 2 (5–8s) — " + SNAP_SHOT.format(snap="7s") + " HARD CUT.\n"
    "SHOT 3 (8–10s) — " + NOSTALGIA_SHOT + " HARD CUT.\n"
    "SHOT 4 (10–12s) — " + FOIL_SHOT + " HARD CUT.\n"
    "SHOT 5 (12–16s) — " + LICK_SHOT.format(freeze="15s"),
    acting_man(
        "the whole ritual, from the fridge to the last lick, keeping the pleasure small. Tactic: savour — a moment slower "
        "at the fridge, no hesitation at the snap, the lick casual, a habit.",
        "— [0–5s] he opens the door, the smile arrives late, eyes follow the pair out — [5–8s] hands only, "
        "the crack at 7s — [8–9s] a few small nods of quiet approval, a light smile — [9–10s] he glances down toward the sink as he sets the other cup down — [10–12s] hands only — [12–15s] a plain look at "
        "the foil, a quick casual lick, eyes open — [15–16s] frozen.",
        "his eyes narrow slightly against the fridge light; his shoulders drop a millimetre at the crack.",
        "mugging, laughing, looking into the lens, a pause before the snap, a sensual or slow lick, closed eyes, savouring, any movement after the freeze.",
    ),
    "CAMERA — shots 1, 3 and 5 locked off, STAY PUT, at 84°, 29° and 47°; shot 2: one steady macro pull-back; shot 4: one "
    "gentle macro push-in. Natural, fluid camera moves, never mechanical.\n" + MACRO_LENS,
    "GEOMETRY — " + KITCHEN_GEOMETRY + "; in shots 3 and 5 the lens is 35° toward his right side.",
    "PHYSICS & MATERIAL — the break line resists, then gives all at once with a sharp snap, no splinters; the foil lifts "
    "without tearing; the yogurt layer is creamy and clinging; each lick wipes a clean silver stripe. OVER-REAL: condensation "
    "on the cups, the ridge where the break line parted, foil creases, yogurt on bare silver, the weave of his shirt, pores. "
    "If any surface looks smooth, plastic or rendered — WRONG.",
    LIVE_LIGHT, LIVE_LOOK,
    "SOUND — the fridge hum; the door's soft thump; the créqui at 7s, a short, crisp, bright plastic snap; the foil's crinkle; "
    "a small wet lick; near silence at the freeze. " + MUSIC_BAN,
    LIVE_WORLD,
    "NEGATIVE: " + MACRO_NEG + "moving arms or elbows during the fold, a wide or medium shot instead of the close-up, a previz or clay look, doll-like hands, a sensual or slow lick, closed eyes, pleasure on his face, savouring, tongue play, a round foil, a round cup, a thin smear of yogurt, the pair held at face height, a tray, the joint dipping down, a pair twisted or pulled apart, a pause before the snap, a low angle, a clean silver "
    "side, a heap of yogurt, any movement after the freeze, " + LIVE_NEG_SPINE,
    "[ORDER: 5 shots, 4 hard cuts, 16s — (1, 0–5s) inside the fridge, the door opens, he takes the pair, the door shuts; (2, 5–8s) macro pull-back, the gentle book-like fold at 7s; (3, 8–10s) tight three-quarter close-up, small approving nods; (4, 10–12s) macro push-in, "
    "the foil opens like a little door; (5, 12–16s) three-quarter, the lick, FREEZE from 15s. Invariants: TWO joined cups, never one; "
    "the fold; cup left, foil right; a real layer of yogurt; real hands; daylight frame-left. Look: 35mm negative. NO text.]",
)

# ===========================================================================
# 2a — Mergulho (4 s)
# ===========================================================================
P_2A = _join(
    "CONTRACT — Live-action photoreal raw camera footage with production sound only, 16:9, 4 seconds total, ONE continuous take, time-freeze: everything in "
    "the scene is motionless like a photograph and ONLY the camera moves. Deadpan, played straight. No dialogue. NO music, "
    "NO score, NO subtitles, NO on-screen text.",
    "REFERENCES — each reference has ONE job:\n"
    "[first frame] KEYFRAME: the take STARTS from this exact frame (the man mid-lick, the foil at his mouth, the open cup in his left hand) and the world stays frozen in it; light, grade and skin continue the keyframe exactly.\n"
    "@prop_pote-morango — OBJECT ONLY: the open cup and its yogurt.",
    "WHO IS WHO — @man-portoalegre is the frozen man in the keyframe; he NEVER moves in this take; nobody else exists.",
    "SCENE & SOUL — SCENE: the instant after the lick. Time stops. The camera, a slim probe lens, slides forward and down in one "
    "arc toward the open cup in his left hand and dives into the pink yogurt.\n"
    "THE SOUL OF THE SCENE (play it, never explain it): a held breath, then a plunge. The world waits politely.",
    "ABSOLUTE LOCKS — break one and the take is WRONG, regenerate:\n"
    "1. NOTHING MOVES except the camera: no blink, no breath, no yogurt ripple — WRONG if he moves.\n"
    "2. ONE smooth arc, no cuts.\n"
    "3. THE LAST FRAME is a uniform strawberry-cream pink filling the whole frame, with no cup, rim, highlight or edge — WRONG if "
    "any object remains.\n"
    "4. Light and grade stay exactly those of the keyframe.",
    "TIMELINE — ONE continuous take, no cuts, already in progress at the first frame:\n"
    "PART 1 (0–1s) — MCU 47°, the frozen frame, the camera 0.8 m from him and diagonal, about 35° toward his right side, 15 cm "
    "above his eye line; the camera begins to drift forward.\n"
    "PART 2 (1–3s) — the camera arcs forward and down past his chest, 20 cm above his thumb, toward the open cup in his left hand; the rim grows in the lower right of the frame and the yogurt surface, glossy with one frozen swirl, fills the "
    "lens.\n"
    "PART 3 (3–4s) — the lens dives through the surface; the frame fills with soft, uniform strawberry-cream pink. Hard end on the "
    "uniform pink.",
    "ACTING — none: he is a frozen photograph. NOT: a blink, a breath, any micro-movement, a changing expression.",
    "CAMERA — an impossible camera, a slim probe lens gliding on a curve, TRAVELS in one smooth move, no zoom. OPTICS: 47° at the "
    "start narrowing to a macro close-focus at the end; the picture stays a full 16:9 rectangle. FOCUS: on his face at first, "
    "then on the rim, then the surface. HORIZON: level at the start. NOT: handheld shake, orbit, whip, cuts, slow motion, "
    "fisheye, circular black frame.",
    "GEOMETRY — the cup is in his LEFT hand at chest height, at the lower right of the frame; the camera starts 0.8 m from his "
    "face, diagonal, and ends inside the yogurt; the path is one curve down and to the right of the frame, passing 20 cm above "
    "his thumb.",
    "PHYSICS & MATERIAL — everything is frozen: the yogurt holds its swirl, the glasses hold their reflection, the light is "
    "unchanged; only the camera's own travel is real, smooth and weighted. OVER-REAL: the frozen glossy swirl, a faint pink "
    "smear on his lip, fine foil creases. If any surface looks clean, smooth, plastic, CGI or rendered — WRONG.",
    "LIGHT — continues the keyframe exactly: warm natural summer daylight from FRAME-LEFT, patches of sun on the green tile "
    "wall; inside the yogurt the light becomes soft, creamy and pink. The lit sides never flip.",
    LIVE_LOOK,
    "SOUND — sound drops almost to silence; a soft airy whoosh at 3s as the lens dives. " + MUSIC_BAN,
    LIVE_WORLD,
    "NEGATIVE: any movement in the man, blinking, breathing, yogurt ripple, smoke or mist, cuts, a visible cup or rim at the end, "
    "readable text, music, score, subtitles, handheld shake, wrong aspect ratio.",
    "[ORDER: 1 continuous take, 4s, time-freeze, camera only — (0–1s) the frozen frame; (1–3s) the arc to the cup; (3–4s) the dive "
    "into uniform pink. Invariants: nothing moves but the camera; one arc; last frame uniform pink; light of the keyframe. Look: "
    "35mm negative. NO text.]",
)

# ===========================================================================
# 7a — A vitória (6 s)
# ===========================================================================
P_7A = _join(
    live_contract(6, "ONE continuous take", "; a wordless laugh is allowed, no words and no exclamations"),
    "REFERENCES — each reference has ONE job:\n"
    "[first frame] KEYFRAME: the take STARTS from this exact frame (the man mid-lick, the foil at his mouth, the open cup in his left hand) and comes alive from it; light, grade and skin continue the keyframe exactly.\n"
    "@man-portoalegre — IDENTITY of the man. 100% matches.\n"
    "@loc_cozinha — WORLD: the kitchen.\n"
    "@prop_pote-morango — OBJECT ONLY: the cup and its green foil.\n" + LIVE_SCOPE,
    who_man("finishes the lick, checks the foil, discovers he has won and celebrates",
            never="NEVER says a word (a wordless laugh is allowed), NEVER removes his glasses, NEVER shows a second person"),
    "SCENE & SOUL — SCENE: the freeze releases. He finishes the lick, checks the foil for leftover yogurt, sees that he has won "
    "and is instantly, completely happy, with no pause. He celebrates by raising the foil with his arm.\n"
    "THE SOUL OF THE SCENE (play it, never explain it): luck lands on a man who was only here for a snack, and he takes it with "
    "his whole body.",
    "ABSOLUTE LOCKS — break one and the take is WRONG, regenerate:\n"
    "1. The open cup stays in his LEFT hand; the foil is in his RIGHT hand, soft and crinkly.\n"
    "2. NO PAUSE between seeing it and being happy — WRONG if there is a beat of stillness or doubt.\n"
    "3. NOTHING readable on the foil; no keychain and no other prop appears.\n"
    "4. The framing stays exactly that of the keyframe — WRONG if the camera moves.\n"
    "5. He is ALONE; wordless — WRONG if he says anything.",
    "TIMELINE — ONE continuous take, no cuts, already in progress at the first frame:\n"
    "PART 1 (0–1s) — the lick ends and the foil leaves his mouth.\n"
    "PART 2 (1–2s) — he looks at the foil in his right hand to check for leftover yogurt; its silver inner side, licked almost "
    "clean with a last faint pink smear at one corner, faces him, not the camera.\n"
    "PART 3 (2–3s) — he sees he has won: his face lights up at once.\n"
    "PART 4 (3–6s) — he celebrates, raising the foil high with his right arm, laughing without words. Hard "
    "end at the peak of the celebration.",
    acting_man(
        "own the win, now, in his whole body. Tactic: verify, then pure joy — a quick check that turns into joy with no pause.",
        "— [0–1s] the end of the quick lick, eyes open on the foil — [1–2s] eyes open and search the foil — [2–3s] the discovery: the eyes widen and "
        "the smile arrives instantly — [3–6s] the right arm goes up with the foil, he laughs without words.",
        "a sharp inhale at the discovery.",
        "a pause before the joy, speaking, shouting words, looking into the lens, a keychain.",
        direction="be as happy as a person can be, immediately.",
    ),
    "CAMERA — MCU, 47°, 0.8 m from him, the camera diagonal, about 35° toward his right side, 15 cm above his eye line looking "
    "down a little (a three-quarter, slightly high angle), locked off exactly as the keyframe; STAYS PUT.\nOPTICS: 47°, no lens drift.\nFOCUS: on his face; the foil sharp when it "
    "rises.\nHORIZON: level.\nNOT: handheld shake, push-in, orbit, zoom, slow motion.",
    "GEOMETRY — he is centre, turned a little away from the diagonal lens; the open cup in his LEFT hand at chest height; his "
    "RIGHT arm, the one nearer the lens, rises with the foil ending above the top of his head; the green tile wall with sun at "
    "frame-left and the stainless fridge at frame-right, soft behind him.",
    "PHYSICS & MATERIAL — the foil crinkles as the arm rises, catching the window light in soft glints; "
    "the cup in his left hand stays steady; his shoulders and torso carry the weight of the celebration with a small lift. "
    "Nothing floats, nothing loops. OVER-REAL: foil creases with moving glints, the weave of his shirt moving, skin pores, a trace "
    "of yogurt on his lip. If any surface looks clean, smooth, plastic, CGI or rendered — WRONG.",
    LIVE_LIGHT, LIVE_LOOK,
    "SOUND — DIEGETIC ONLY: the crinkle of the foil; a small wet lick; his breath; a wordless laugh. " + MUSIC_BAN,
    LIVE_WORLD,
    "NEGATIVE: a pause before the joy, words or shouts, a keychain or any other prop, readable text on the foil, the camera moving, "
    "the foil in the left hand, " + LIVE_NEG_SPINE,
    "[ORDER: 1 continuous take, 6s — (0–1s) the lick ends; (1–2s) he checks the foil; (2–3s) he sees he won, instantly happy; "
    "(3–6s) he raises the foil with his right arm, wordless laugh, hard end at the peak. Invariants: cup left hand, foil right "
    "hand; no pause; no text; the camera locked as the keyframe; alone. Look: 35mm negative, summer window light. NO text.]",
)

# ===========================================================================
# MUNDO TOON (fábrica)
# ===========================================================================
TOON_LOOK = (
    "LOOK (KEY — reproduce this exact look): premium 3D animation, a miniature designer-toy diorama. The WORLD and the "
    "CHARACTERS are matte soft-touch vinyl and painted resin with rounded bevels and no gloss. Palette: mostly monochromatic "
    "green (varied greens, a white floor and a white belt); the cows and the fruit keep their own colours, brand accents only "
    "in tiny details. Soft global illumination, gentle ambient occlusion in every crevice, short soft contact shadows, lifted "
    "pastel shadows with no hard black. Miniature-photography focus: a thin sharp plane with a soft falloff in front and behind. "
    "Clean image: NO film grain, NO noise, NO vignette, even exposure to all four corners, nothing from live action.\n"
    "FLARE/GLOW POLICY: NO LENS FLARES, no light streaks, no bokeh orbs; the only glow is the small warm halo of tiny bulbs on "
    "the machines, contained."
)

TOON_LIGHT = (
    "LIGHT — STYLIZED STUDIO LIGHT, soft and clear (KEY): one large soft key that travels with the camera, high at FRAME-LEFT "
    "(~5600 K); a pale sky-blue bounce from FRAME-RIGHT; small warm bulbs on the machines; the back wall half a stop darker. "
    "Shadows lifted pastel, never black. The lit side of every cow is FRAME-LEFT and never flips."
)

COW = (
    "THE ALEGRINHA — the matte vinyl cow of @char_vaca-vinil (100% matches): cream body, her RIGHT ear black (screen-left when "
    "she faces the camera), small horns, round dot eyes, a wide smile that can open to show a small red mouth, a pink belly "
    "patch, black flank patches, black gloves and hooves, a golden bell on a cord; NO keyring. NO EYEBROWS and no brow line, "
    "so she can never look angry. Outfits per hall from @char_alegrinha-looks: hairnet, boots and pale-green apron (hall 1); "
    "white lab coat (hall 2); over-ear headphones (hall 3); painter's smock and beret (hall 4)."
)

# Estilo de atuação pedido pelo diretor: engraçadinhas e desastradinhas (sem citar personagem de marca no prompt)
COW_STYLE = (
    "minion-style (KEY): the cows are cute, eager little workers, a bit clumsy: they rush, "
    "overcommit, wobble under things too big for them, nearly drop them, recover in a hurry and look very proud of themselves. "
    "Quick, bouncy reactions, big round happy smiles, open eyes; tiny mishaps that never break anything and never hurt anyone. "
    "Never angry, never bored, never blank."
)

# Escala: vacas pequenas num mundo grande (do blocking do diretor)
TOON_SCALE = (
    "SCALE (KEY — small cows in a big world): seen from far away, each cow fills only about ONE SIXTH of the frame height, "
    "with the tall hall rising above her: wall with portholes and high shelves of pink cups, at least three times her height. "
    "Everything she handles is oversized for her: a strawberry or an apple is as big as her head or bigger, a coconut half "
    "as wide as she is, the pulp funnel twice her height, the microphone stand taller than she is, each easel taller than its "
    "painter, each pink yogurt cup about half her height."
)

TOON_SCOPE = (
    "REFERENCE SCOPE: @char_vaca-vinil and @char_alegrinha-looks supply the cow, her proportions, colours and outfits ONLY — IGNORE "
    "their grey backdrops and lighting. @loc_fabrica supplies layout, materials, props and colours ONLY — it is an isometric "
    "overview, so IGNORE its camera angle and use the side-on camera written below."
)

TOON_WORLD = (
    "WORLD — a big green factory for small cows: one white belt runs FRAME-LEFT to FRAME-RIGHT through four halls divided by "
    "walls with arched openings; fruit rides it in hall 1, pink yogurt cups from hall 2 on. No humans. Signs and screens are "
    "blank: NO letters, NO numerals, NO logos."
)

TOON_SOUND_BASE = (
    "SOUND — SOFT FOLEY ONLY: the belt's soft rumble, padded footsteps of vinyl hooves, a soft clink of the golden bells, squeaky rubbery fruit, gentle machine puffs, small happy grunts of effort (no words). " + MUSIC_BAN
)

TOON_NEG_SPINE = (
    "eyebrows, frowning or angry faces, cows filling the frame, normal-size fruit, humans, speech or lip-sync, keyring, wrong "
    "number of cows, merged cows, swapped ear colours, 2D cel look, glossy plastic, hard black shadows, dirt, film grain, "
    "camera shake, readable text, logos, subtitles, wrong aspect ratio."
)


def toon_contract(secs, shots):
    return (
        "CONTRACT — 3D animated footage, miniature designer-toy diorama, 16:9, %d seconds total, %s, real-time animation at 24 fps "
        "with light squash and stretch. No speech, no lip-sync, no voice-over (a voice-over is added in post). NO music, NO subtitles, NO on-screen text of any kind: no letters, no numerals, no logos." % (secs, shots)
    )


TOON_CAMERA_TRAVEL = (
    "CAMERA — a VERY WIDE side-on travelling shot: a miniature rail far back from the line, planimetric (no yaw, roll or "
    "tilt), TRAVELS FRAME-LEFT to FRAME-RIGHT at a constant calm speed, never stopping, reversing or cutting. 70°, the lens "
    "at belt height about 12 cow-heights from the back wall, so each hall is seen whole — floor, belt, all its cows, its "
    "machines and its tall wall up to the ceiling — like a dollhouse cut open; the belt runs across the lower part of the "
    "frame; the dividing walls slide through the frame as dark wipes; focus deep enough to hold the whole hall; level horizon. "
    "Only the cow in the opening is close to the lens. NOT: close-ups, medium shots, cows filling the frame, handheld shake, "
    "drone, zoom, speed ramps."
)

_OPEN_A = (
    "PART 1 (0–2s) — the first frame is the approved last frame of the previous shot: the lens is covered in thick pink yogurt. "
    "A cow in a white hairnet, pressed right up against the camera — the ONLY close moment of the take (her face fills the lower half of the frame) — wipes the lens with a white cloth in exactly two quick, over-eager strokes: the first takes most of the yogurt, the second takes the very last of it, edges and corners included. From that moment the lens is SPOTLESS for the rest of the take — no pink tint, no smear, no streak, no drop at the edges. She hurries out "
    "of frame toward frame-left, nearly tripping, and the camera is already far back: the very wide factory appears behind her, the travelling already moving."
)
_OPEN_B = (
    "PART 1 (0–2s) — the first frame is the approved last frame of the previous shot: the lens is covered in thick pink yogurt. "
    "With nobody in front of the camera, the yogurt slides down the glass like a thick gel and runs off the bottom edge, leaving the lens COMPLETELY clean, no yogurt, smear or streak left; the wide factory appears from the top down and the travelling is already moving."
)


def _spine(opening, name):
    return _join(
        toon_contract(30, "ONE continuous take with no cuts, a very wide side-on travelling shot"),
        "REFERENCES — each reference has ONE job:\n"
        "[first frame] KEYFRAME: the take STARTS from this exact frame (the lens covered in pink yogurt).\n"
        "@char_vaca-vinil — IDENTITY of the cow.\n@char_alegrinha-looks — the cow's four outfits, one per hall.\n"
        "@loc_fabrica — WORLD: the factory's materials, props and colours.\n" + TOON_SCOPE,
        "WHO IS WHO — READ FIRST, ABSOLUTE:\n" + COW + "\n"
        "HALLS: hall 1 (fruit selection) three cows; hall 2 (pulp lab) three; hall 3 (sound studio) exactly TWO, one inside the "
        "glass booth and one outside at the audio desk; hall 4 (art studio) three. Each cow does ONE job, the one in the TIMELINE, "
        "and NEVER another.\n" +
        ("FACES: no cow looks into the lens (except the wiping cow in the opening, who looks at the glass); no cow speaks; no "
         "human exists.\nCONTACT: cows touch only fruit, tools and the cloth." if name == "A" else
         "FACES: no cow looks into the lens; no cow speaks; no human exists.\nCONTACT: cows touch only fruit and tools."),
        "SCENE & SOUL — SCENE: a long, very wide side-on travelling shot along a production line in a big green factory run by small "
        "cows: giant fruit is selected, pressed into pulp, packed with a crisp créqui, and finally yogurt is painted onto foil. "
        "Already in progress at the first frame.\n"
        "THE SOUL OF THE SCENE (play it, never explain it): the cows are tiny, the job is huge, and they love it; every little "
        "mishap is fixed in a hurry and celebrated.",
        "ABSOLUTE LOCKS — break one and the take is WRONG, regenerate:\n"
        "1. COW COUNTS: hall 1 three cows, hall 2 three, hall 3 exactly TWO, hall 4 three — WRONG if a count changes or two cows "
        "merge.\n"
        "2. VERY WIDE: after the opening, the camera stays far back, each hall seen whole, moving FRAME-LEFT to FRAME-RIGHT at a constant speed, never cutting, stopping or reversing; each cow fills only about one sixth of the frame height — WRONG if the framing tightens or a cow fills the frame.\n"
        "3. HAPPY FACES: NO eyebrows, NO frown on any cow; her RIGHT ear is the black one; NO keyring.\n"
        "4. EACH HALL KEEPS ITS OUTFIT: hairnet and apron, lab coat, headphones, painter's smock and beret.\n"
        "5. NO TEXT anywhere; after the opening the lens is SPOTLESS for the rest of the take — WRONG if any yogurt, smear or pink tint remains.",
        "TIMELINE — ONE continuous take, no cuts, already in progress at the first frame:\n" + opening + "\n"
        "PART 2 (2–7s) — HALL 1, fruit selection: giant strawberries, apples and coconut halves ride the belt in the foreground. "
        "Three small cows in hairnets, white boots and aprons stand at small round tables behind the belt. COW A hugs a "
        "strawberry bigger than her head, waddles it to the belt, wobbles, drops it on with a bounce and pats it proudly; COW B "
        "lifts an apple bigger than her head to inspect it, it slips, she juggles it twice, catches it with a relieved grin and "
        "sets it on the belt; COW C shoves a coconut half onto the belt with her whole body, nearly slips and throws a quick "
        "thumbs-up.\n"
        "PART 3 (7–14s) — HALL 2, pulp lab: a huge pulp funnel twice a cow's height, thick pink pulp running in glass tubes. "
        "EXACTLY THREE small cows in white lab coats, all three in frame together, each at her own station: COW A at the "
        "funnel on the left, COW B at the swatch strip in the centre, COW C at the console on the right. COW A, on tiptoe, "
        "tosses a strawberry up into the funnel; it drops in with a plop and she hops for joy; COW B holds a test tube up to a "
        "tall strip of pink swatches on the wall and nods so hard her bell clinks; COW C slaps a big green button with both "
        "gloves, then takes an empty pink yogurt cup from a stack beside the console and sets it on the belt with both gloves, "
        "proud. From here on pink cups ride the belt.\n"
        "PART 4 (14–21s) — HALL 3, sound studio: a tall wall of acoustic foam and a glass booth. Inside, standing on a little box "
        "at a microphone stand taller than she is, COW A holds ONE pack made of two small yogurt cups stuck together side by side, both gloves on the pack, and pulls the two cups apart with a crisp créqui, ending with one cup in each glove; she flinches at her own loud snap, ears flying, then grins. Outside the booth, COW B stands IN FRONT of a big "
        "toy-like audio desk, her back to it, wearing headphones and turned toward the booth and COW A; when she hears the "
        "snap she nods with approval and purses her lips in a satisfied pout as if mooing.\n"
        "PART 5 (21–30s) — HALL 4, art studio: easels taller than the painters, each with a big flat sheet of soft aluminum foil. "
        "Three small cows in painter's smocks and berets. COW A backs up to judge her work, bumps gently into the easel behind "
        "her, steadies it and tilts her head; COW B dips her brush so deep into a big pot of yogurt that her whole glove comes "
        "out pink, and shrugs happily; COW C, on tiptoe, paints one plain stroke of yogurt onto the foil, the tip of her red "
        "tongue poking out in concentration, no decoration. Hard end at 30s, wide, in the middle of the movement.",
        "ACTING — " + COW_STYLE + " Each cow plays exactly the task written for her in the TIMELINE, with total, eager "
        "commitment; the happiness shows in ears, bell and body. NOT: looking into the lens, mouths forming words, frowning, a "
        "blank face.",
        TOON_CAMERA_TRAVEL,
        "GEOMETRY — " + TOON_SCALE + " In each hall the cows stand about 2.5 cow-lengths apart, all of a hall's cows in frame "
        "together; the back wall rises to the top of the frame; the arched openings are about 3 cow-heights tall. Hall 3: the "
        "booth at the left of the hall, the audio desk at the right.",
        "PHYSICS & MATERIAL — vinyl bodies have weight and a light squash on every landing and every wobble; fruit is big, heavy "
        "for them and rubbery: the strawberry dents under a hug and recovers slowly, the apple bounces in her gloves, the coconut "
        "half drags; the pink pulp is thick and slow in the glass tubes; the cup is set on the belt by hand, never appearing by itself; yogurt is thick and "
        "glossy and clings to the brush and the glove; the foil is a thin soft sheet that flexes when brushed; " + ("the cloth in "
        "the opening is white and absorbent; " if name == "A" else "in the opening the yogurt on the lens is a thick gel that "
        "slides down the glass by itself and leaves it clean; ") + "the bells clink softly. Nothing floats, nothing "
        "loops. MATERIAL TRUTH of this world: matte vinyl with faint seam lines and soft fillets, a tiny glint on the golden bells, "
        "glossy pulp and yogurt, rubbery fruit with modelled seeds; pristine, never dirt.",
        TOON_LIGHT, TOON_LOOK, TOON_SOUND_BASE, TOON_WORLD,
        "NEGATIVE: only two cows in hall 2, a cup appearing by itself, yogurt left on the lens after the wipe, a single cup turning into two, a fourth cow in hall 3, a cut, a stop, the camera reversing, close framing, " + TOON_NEG_SPINE,
        "[ORDER: 1 continuous take, 30s, very wide side-on travelling left to right, small cows in a big world — (0–2s) opening on the "
        "yogurt-covered lens; (2–7s) hall 1, giant fruit; (7–14s) hall 2, three cows, the funnel, the button, a cup set on the belt by hand; "
        "(14–21s) hall 3, the snap and the créqui, the pout; (21–30s) hall 4, the bump, the pink glove, the stroke. Invariants: "
        "cow counts 3-3-2-3; very wide, each hall seen whole, cows a sixth of the frame height; constant direction and speed, no cuts; no eyebrows, no "
        "frowns, black right ear, no keyring; outfit per hall; no text. Look: matte vinyl, mostly monochromatic green, clean. "
        "NO text.]",
    )


P_3A_A = _spine(_OPEN_A, "A")
P_3A_B = _spine(_OPEN_B, "B")


def _insert(label, seconds, who, scene_soul, locks, shots, acting, geometry, physics, order, extra_neg=""):
    return _join(
        toon_contract(seconds, label + ", backstage handheld camera"),
        "REFERENCES — each reference has ONE job:\n@char_vaca-vinil — IDENTITY of the cow.\n@char_alegrinha-looks — the cow's outfit "
        "for this hall.\n@loc_fabrica — WORLD: the hall's materials, props and colours.\n" + TOON_SCOPE,
        "WHO IS WHO — READ FIRST, ABSOLUTE:\n" + COW + "\n" + who,
        scene_soul,
        "ABSOLUTE LOCKS — break one and the take is WRONG, regenerate:\n" + locks,
        "TIMELINE — hard cuts only at the specified seconds; the camera adds no cuts of its own:\n" + shots,
        "ACTING — " + COW_STYLE + " " + acting.replace("ACTING — ", "", 1),
        "CAMERA — BACKSTAGE HANDHELD (KEY): as if a behind-the-scenes crew were filming the factory at work — a small handheld "
        "camera held at cow height by an operator standing among the machines, with a gentle, natural sway, small breathing "
        "reframes and the occasional quick correction to keep the action in frame, never shaky or chaotic; still WIDE, the whole "
        "setting around the cow in frame, never a close-up or a medium shot; shot sizes and angles as stated per shot; level "
        "horizon on average unless a shot says top-down. NOT: a locked-off tripod look, a smooth rail or gimbal glide, drone, "
        "whip pan, zoom, close-ups.",
        "GEOMETRY — " + TOON_SCALE + " " + geometry,
        physics,
        TOON_LIGHT, TOON_LOOK, TOON_SOUND_BASE, TOON_WORLD,
        "NEGATIVE: " + extra_neg + TOON_NEG_SPINE.replace("camera shake, ", ""),
        order,
    )


_INS_LOCKS_TAIL = (
    "3. HAPPY FACES: NO eyebrows, NO frown; her RIGHT ear is the black one; NO keyring.\n4. NO text anywhere.\n"
    "5. Lit side FRAME-LEFT."
)

# Inserts padronizados (v1.22): 2 planos de 4 s em todos os setores
#  plano 1 = ISOMÉTRICO (o ângulo do insert de frutas aprovado) com a ação geral do setor
#  plano 2 = CHÃO, BASTIDOR, câmera na mão, um objeto gigante desfocado na frente e um detalhe da ação
ISO_CAMERA = (
    "SHOT 1 — ISOMETRIC (KEY, identical in all four factory inserts): a high three-quarter view looking down at about 45° onto "
    "the hall from far away with a long lens (about 30°), so lines stay nearly parallel like an isometric diorama; the white "
    "belt runs diagonally from the upper left to the lower right of the frame and everything on it travels from LEFT to "
    "RIGHT, toward the lower right; the whole hall and all its cows are in frame, "
    "small, each cow about one sixth of the frame height; the camera is locked off with only a very slow, steady drift."
)
GROUND_CAMERA = (
    "SHOT 2 — GROUND-LEVEL BACKSTAGE (KEY, identical in all four factory inserts): a small handheld camera resting almost on "
    "the floor at belt height, as if a behind-the-scenes crew were filming, with a gentle natural sway; a giant object huge "
    "and soft out of focus in the near foreground, and behind it, sharp, one small cow doing one detail of the work, the hall "
    "rising tall around her; the belt, when in frame, moves from LEFT to RIGHT; 47°."
)
INSERT_LOOK_REF = (
    "[image reference] INSERT LOOK — the approved isometric frame of the hall 1 insert: copy ONLY its camera angle, lens, "
    "light, palette and material look, so all four inserts match; IGNORE its content."
)


def _insert_iso(hall, who, soul, locks, iso_action, ground_action, acting, physics, order_iso, order_ground, extra_neg=""):
    return _join(
        toon_contract(8, "2 shots with 1 hard cut at 4s: an isometric overview, then a ground-level backstage shot"),
        "REFERENCES — each reference has ONE job:\n" + INSERT_LOOK_REF + "\n@char_vaca-vinil — IDENTITY of the cow.\n"
        "@char_alegrinha-looks — the cow's outfit for this hall.\n@loc_fabrica — WORLD: the materials, props and colours of THIS "
        "hall only; it shows the whole factory, so IGNORE every other hall in it and its camera angle.\n" + TOON_SCOPE,
        "WHO IS WHO — READ FIRST, ABSOLUTE:\n" + COW + "\n" + who,
        "SCENE & SOUL — SCENE: " + hall + ", seen first from above as an isometric overview, then from the floor like a "
        "backstage shot. Already in progress.\nTHE SOUL OF THE SCENE (play it, never explain it): " + soul,
        "ABSOLUTE LOCKS — break one and the take is WRONG, regenerate:\n" + locks + "\n"
        "LOOK LOCK: the same isometric angle, light, palette and vinyl look as the other factory inserts.\n"
        "ONLY THIS HALL: no other sector appears anywhere in frame; the belt moves LEFT to RIGHT — WRONG otherwise.",
        "TIMELINE — 2 shots, 1 hard cut:\nSHOT 1 (0–4s) — isometric overview: " + iso_action + " HARD CUT.\n"
        "SHOT 2 (4–8s) — ground-level backstage: " + ground_action + " Hard end.",
        "ACTING — " + COW_STYLE + " " + acting,
        "CAMERA — " + ISO_CAMERA + "\n" + GROUND_CAMERA + "\nNOT: close-ups of faces, a low or eye-level angle in shot 1, a "
        "high angle in shot 2, drone, whip pan, zoom.",
        "GEOMETRY — " + TOON_SCALE,
        physics,
        TOON_LIGHT, TOON_LOOK, TOON_SOUND_BASE,
        "WORLD — ONLY " + hall + " is seen, closed in by its own walls: NO other hall, NO arched opening looking into a "
        "neighbouring hall, NO machines, props or outfits from another sector. The belt runs LEFT to RIGHT. No humans. Signs "
        "and screens are blank: NO letters, NO numerals, NO logos.",
        "NEGATIVE: another hall or sector in view, an opening into a neighbouring hall, the belt moving right to left, "
        + extra_neg + TOON_NEG_SPINE.replace("camera shake, ", ""),
        "[ORDER: 2 shots, 1 hard cut, 8s — (1, 0–4s) isometric overview: " + order_iso + "; (2, 4–8s) ground-level backstage: "
        + order_ground + ". Invariants: only this hall, belt left to right; the same isometric angle and look as the other inserts; cows small; no eyebrows, no "
        "frowns; black right ear; no text.]",
    )


_TAIL = "HAPPY FACES: NO eyebrows, NO frown; her RIGHT ear is the black one; NO keyring. NO text anywhere."

P_3B = _insert_iso(
    "hall 1, fruit selection",
    "HALL 1 outfit: a white hairnet with the horns poking through, white rubber boots and a pale-green apron. Shot 1 shows "
    "the hall's THREE cows; shot 2 shows ONE.",
    "the fruit is enormous, the cows are tiny, and they are thrilled.",
    "1. Shot 1: exactly THREE small cows; shot 2: exactly ONE.\n2. Every fruit is bigger than a cow's head.\n3. " + _TAIL,
    "giant strawberries, apples and coconut halves ride the diagonal belt; one cow hugs a strawberry bigger than her head and "
    "waddles it onto the belt, one lifts an apple to inspect it, one shoves a coconut half along with her whole body.",
    "a giant strawberry soft in the near foreground; behind it one small cow in a hairnet and apron hugs another strawberry "
    "bigger than her head, inspects it, wobbles and nods proudly.",
    "Shot 1: three eager workers, one wobble. Shot 2: the proud nod; detail: her left ear flicks when she approves. NOT: "
    "looking into the lens, frowning, a blank face.",
    "PHYSICS & MATERIAL — the fruit is heavy for the cows and rubbery: it dents under a hug and recovers slowly; the belt moves "
    "steadily; the bells clink softly. Nothing floats, nothing loops. MATERIAL TRUTH: matte vinyl, modelled seeds, soft "
    "fillets; never dirt.",
    "giant fruit on the diagonal belt, three small cows at work",
    "a giant strawberry in front, one cow hugging another",
)

P_4B = _insert_iso(
    "hall 2, the pulp lab",
    "HALL 2 outfit: a white lab coat with a blank badge and white rubber boots. Shot 1 shows the hall's THREE cows; shot 2 "
    "shows ONE.",
    "science, taken far too seriously by someone far too small, and loved completely.",
    "1. Shot 1: exactly THREE small cows, each at her station (funnel, swatch strip, console); shot 2: exactly ONE.\n"
    "2. The cup is set on the belt by a cow's gloves, never appearing by itself.\n3. " + _TAIL,
    "a huge pulp funnel with thick pink pulp running through glass tubes; one cow on tiptoe tosses a strawberry into the "
    "funnel, one holds a test tube up to a tall strip of pink swatches, one presses a big green button and then sets an "
    "empty pink cup on the diagonal belt with both gloves.",
    "a pink yogurt cup on the belt huge in the near foreground while a nozzle fills it with thick pink pulp; behind the cup, "
    "small and sharp, a cow peeks over the rim, delighted.",
    "Shot 1: the tiptoe toss, the over-eager nod, the proud placing of the cup. Shot 2: the peek of pure delight. NOT: looking "
    "into the lens, frowning, a blank face.",
    "PHYSICS & MATERIAL — the pulp is thick and slow in the glass tubes and in the cup, which fills gradually (START empty, "
    "DURING rising pink, END full); the strawberry tumbles once and drops. Nothing floats, nothing loops. MATERIAL TRUTH: matte "
    "vinyl machines, glossy pulp, clear glass; never dirt.",
    "the funnel, the swatches, the button and the cup placed on the belt",
    "the nozzle fills the cup, a cow peeks",
    extra_neg="a cup appearing by itself, only two cows in shot 1, ",
)

P_5B = _insert_iso(
    "hall 3, the sound studio",
    "HALL 3: exactly TWO cows — COW A inside the glass acoustic booth, in plain cream vinyl, at a tall microphone; COW B "
    "outside the booth, standing in front of a big toy-like audio desk and facing the booth, wearing over-ear headphones.",
    "the créqui is the sweetest sound the engineer has ever heard.",
    "1. EXACTLY TWO cows in this hall.\n2. COW A starts with ONE pack of two cups stuck together side by side and pulls them apart into two — WRONG if she starts with a single cup or with two loose cups.\n3. " + _TAIL,
    "the glass booth with a tall wall of acoustic foam; inside, COW A on a little box holds ONE pack made of two small yogurt cups stuck together side by side, both gloves on the pack, and pulls the two cups apart with a crisp créqui, ending with one cup in each glove; outside, COW B stands in front of the audio desk, turned toward the booth, "
    "and nods with approval when she hears it.",
    "from the floor just outside the booth, a slider of the audio desk huge and soft in the near foreground; behind it, sharp, COW B in headphones watches the big volume meter on the desk; its needle jumps with the snap and she nods with approval, a small satisfied pout as if mooing; COW A is tiny behind the glass.",
    "COW A: total concentration, then a flinch at her own snap, then a grin. COW B: watches the volume meter, then nods with approval as the needle jumps. NOT: looking into the lens, mouths forming words, frowning, a blank face.",
    "PHYSICS & MATERIAL — the plastic break line gives with a sharp snap; the cups stay sealed; a meter's needle jumps; the "
    "glass booth shows soft reflections. Nothing floats, nothing loops. MATERIAL TRUTH: matte vinyl, clear glass, soft "
    "acoustic foam; never dirt.",
    "the booth, the two cups separated, the engineer's nod",
    "the engineer watching the volume meter and nodding",
    extra_neg="a third cow, a single cup turning into two, two loose cups from the start, ",
)

P_6B = _insert_iso(
    "hall 4, the art studio",
    "HALL 4 outfit: a cream painter's smock and a small beret between the horns. Shot 1 shows the hall's THREE cows; shot 2 "
    "shows ONE.",
    "they paint yogurt onto foil with the gravity of old masters and the coordination of toddlers.",
    "1. Shot 1: exactly THREE small cows, one per easel; shot 2: exactly ONE.\n2. The painting is PLAIN yogurt strokes — NO "
    "decoration, NO drawing, NO letters; every easel is taller than its painter.\n3. " + _TAIL,
    "three easels taller than the painters, each with a big square sheet of soft aluminum foil; one cow backs up to judge her "
    "work and bumps gently into the easel behind her, one dips her brush so deep into a big pot of yogurt that her glove comes "
    "out pink, one paints a plain stroke on tiptoe.",
    "from the floor just behind COW A, who has stepped back: her soft shoulder in the near foreground, and beyond it, sharp, "
    "her gloved fingers making a finger frame around the foil on her towering easel.",
    "Shot 1: the bump, the pink glove, the tiptoe stroke. Shot 2: the art critic's finger frame; detail: she tilts her head. "
    "NOT: looking into the lens, frowning, a blank face, decoration on the foil.",
    "PHYSICS & MATERIAL — the foil flexes slightly under the brush; the yogurt is thick and glossy and leaves a clean ridge; "
    "the brush lifts heavy with yogurt. Nothing floats, nothing loops. MATERIAL TRUTH: matte vinyl, glossy yogurt, soft foil; "
    "never dirt.",
    "three easels, the bump, the pink glove, the stroke",
    "over her shoulder from the floor, the finger frame",
    extra_neg="decoration or drawings on the foil, ",
)

# ===========================================================================
PROMPTS = {
    "1a": ("1a · POV da geladeira", 5, P_1A),
    "1b": ("1b · O créqui", 5, P_1B),
    "1c": ("1c · O foil e a lambida", 6, P_1C),
    "1bc": ("1bc · Créqui, foil e lambida", 11, P_1BC),
    "2a": ("2a · Mergulho", 4, P_2A),
    "3a-A": ("3a · Espinha, abertura A (a vaca limpa)", 30, P_3A_A),
    "3a-B": ("3a · Espinha, abertura B (a lente se limpa sozinha)", 30, P_3A_B),
    "3b": ("3b · Inserts do Setor 1", 8, P_3B),
    "4b": ("4b · Inserts do Setor 2", 8, P_4B),
    "5b": ("5b · Inserts do Setor 3", 8, P_5B),
    "6b": ("6b · Inserts do Setor 4", 8, P_6B),
    "7a": ("7a · A vitória", 6, P_7A),
}
# 1d é uma alternativa a 1a+1b+1c (mesmos 15 s); fica fora de BASE_KEYS e ALT_KEYS para não somar duas vezes.
PROMPTS["1d"] = ("1d · Cena 1 inteira (alternativa a 1a+1bc)", 16, P_1D)

# Plano base: 3a conta uma vez (abertura A); a B só entra se for testada.
BASE_KEYS = ["1a", "1bc", "2a", "3a-A", "3b", "4b", "5b", "6b", "7a"]
ALT_KEYS = ["3a-B"]

# Higgsfield (página oficial, verificada em 20/10/2026): 8 s = 128 (1080p), 56 (720p), 24 (480p).
# Por segundo (divisão minha): 16 e 3. O preço de finalizar um draft em 1080p não é publicado: assumo uma geração 1080p inteira.
CR_480 = 3
CR_1080 = 16
