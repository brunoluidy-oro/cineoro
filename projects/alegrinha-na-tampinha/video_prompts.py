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
    "FILM LOOK (KEY — reproduce this exact photographic character): 35mm color negative film look. Organic grain, fine to "
    "medium, alive in the shadows and midtones. Soft highlight roll-off with gentle warm halation blooming around windows, "
    "sunlit patches and bright skin edges; highlights creamy and warm, never pure white. Blacks slightly lifted and never "
    "crushed, shadows holding detail with a faint cool teal-green cast. Vintage spherical glass character: moderate "
    "micro-contrast, slight softness toward the frame edges, a gentle natural vignette darkening the corners, subtle "
    "chromatic fringing on high-contrast edges. Colour comes from the place itself — the real materials, surfaces and light "
    "of each location — never a grade laid over it; skin golden and natural with visible pores and texture. Photoreal "
    "live-action cinema, 16:9, real-time 24fps cadence with natural motion blur. NOT a render, NOT HDR, NOT the glossy AI "
    "commercial look.\n"
    "NO LENS FLARES: no flares, no light streaks, no floating bokeh orbs; the warm halation stays soft and contained around "
    "bright edges."
)

LIVE_SCOPE = (
    "REFERENCE SCOPE: identity and object references supply faces, wardrobe, hands and objects ONLY — IGNORE their backdrops, "
    "lighting direction, exposure and colour grade. The kitchen reference supplies architecture and materials only; its camera "
    "angle and light are replaced by those written below."
)

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
    "readable text, invented logos, stiff foil, music, subtitles, handheld shake, CGI-gloss look, cartoon look, wrong aspect "
    "ratio."
)

MACRO_NEG = "fisheye, circular black border, round lens mask, black corners, curved straight lines, "

MUSIC_BAN = (
    "NO music of any kind (no score, soundtrack, BGM, jingle, beat or melody): raw production sound only. NO voice-over, NO "
    "subtitles."
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
        "motion. Dry comedy played completely straight. No dialogue (a voice-over is added in post)%s. NO music, NO "
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
        "ACTING — @man-portoalegre (dry comedy played completely straight; the work happens in the eyes)\n"
        "DIRECTION: " + direction + "\n"
        "TASK: " + task + "\n"
        "MOMENT TO MOMENT: " + moments + "\n"
        "EYES: alive in every hold — they search and settle, blinks a beat late; involuntary detail: " + detail + "\n"
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
    "a thin, soft aluminum sheet, printed green on the outside; its inner face is bare SILVER with a real, generous layer of "
    "pink yogurt stuck to it — about 2–3 mm thick, true to the size of one small cup, covering most of the silver with a thin "
    "clean edge — never a heap. It bends and crinkles, never stiff; NO tab, NO writing."
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
    "MCU, 84°, locked off INSIDE the fridge on the middle shelf, 0.7 m from the doorway, looking out. The door is already "
    "open; " + DOOR_ITEMS + ". His face is in the doorway, eyes on a point inside the fridge just beside the lens; a slow "
    "smile. At 1s his right hand reaches in and covers the lens for a moment, then pulls back out holding a PAIR of two "
    "joined yogurt cups, foil up, clearly visible as it leaves the fridge; at 3s his left hand swings the door shut toward "
    "the lens and the frame goes dark as it closes."
)
SNAP_SHOT = (
    "extreme close-up with the macro probe, in front of him and above his hands (" + HANDS.rstrip("; ") + "): it starts 3 cm above the two foils, his two "
    "thumbs lying flat on them, one per cup, and makes ONE steady pull-back with a slight rise through the whole shot, "
    "revealing the pair at chest height and his shirt soft behind. He is already folding the pair toward its centre: thumbs "
    "press the outer halves down, fingers push up under the joint, the cup bottoms swing toward each other (an upside-down "
    "V); at {snap} the break line snaps with a crisp, bright crack — the créqui — and he draws the two cups apart, level, one "
    "in each hand."
)
NOSTALGIA_SHOT = (
    "CU, 29°, 0.9 m away, the camera diagonal — about 35° toward his right side — and 25 cm ABOVE his eye line looking down: a "
    "three-quarter, slightly high angle, tile wall behind, no ceiling in frame. A half-beat after the crack his gaze lifts slightly upward toward the window light, faraway and nostalgic, a "
    "small half-smile, never into the lens. His LEFT hand keeps one cup at chest height; his RIGHT hand sets the other on the "
    "counter without looking."
)
FOIL_SHOT = (
    "extreme close-up with the macro probe beside his right hand (" + HANDS.rstrip("; ") + "): the back of that hand large and soft in the foreground at "
    "frame-left, its fingertip under the near edge of the foil; the cup held by the fingers of his left hand at frame-right; "
    "the tile wall soft behind. ONE gentle, continuous push-in: the fingertip lifts the near edge and the foil hinges up on its "
    "far edge like a little door opening toward the lens, rising almost upright, its yogurt-thick silver side turned to the "
    "camera, the open cup and its pink yogurt below."
)
LICK_SHOT = (
    "MCU, 47°, 0.8 m away, the camera diagonal — about 35° toward his right side — and 15 cm above his eye line: a "
    "three-quarter, slightly high angle, locked off. The open cup in his left hand at chest height; the foil in his right hand, "
    "nearer the lens, its yogurt side toward him, tilted so the pink catches the light. He looks at it with reverence, brings "
    "it to his mouth and licks the coat off in one slow sweep, a second beginning. At {freeze} the image FREEZES mid-lick — "
    "foil at his mouth, eyes half-closed — and stays frozen, like a photograph, to the end."
)

# ===========================================================================
# 1a — POV da geladeira (4 s)
# ===========================================================================
P_1A = _join(
    live_contract(4, "ONE locked-off shot"),
    "REFERENCES — each reference has ONE job:\n"
    "@man-portoalegre — IDENTITY of the man. 100% matches.\n"
    "@loc_cozinha — WORLD: the kitchen.\n"
    "@prop_pote-morango — OBJECT ONLY: one yogurt cup; here two of them are joined.\n" + LIVE_SCOPE,
    who_man("reaches into the fridge, takes a pair of joined yogurts and shuts the door; he never looks into the lens"),
    "SCENE & SOUL — SCENE: a summer afternoon in a Brazilian kitchen, seen from inside the fridge. He reaches in, takes a pair "
    "of joined yogurt cups and shuts the door. Already in progress.\n"
    "THE SOUL OF THE SCENE (play it, never explain it): the most important small ritual of his day, and nobody knows.\n"
    "THE PAIR — " + PAIR_TEXT,
    "ABSOLUTE LOCKS — break one and the take is WRONG, regenerate:\n"
    "1. He takes a PAIR of two joined cups — WRONG if a tray, a single cup or another count.\n"
    "2. The pair is clearly visible as it leaves the fridge.\n"
    "3. The camera is LOCKED OFF inside the fridge; he never looks into the lens.\n"
    "4. The door closes toward the lens and the frame ends dark.",
    "TIMELINE — ONE shot, already in progress:\n"
    "SHOT 1 (0–4s) — " + FRIDGE_SHOT + " Hard end on the dark frame.",
    acting_man(
        "collect the day's reward, keeping the pleasure under control. Tactic: savour — half a beat slower than needed, so the "
        "moment lasts.",
        "— [0–1s] eyes settle on the point inside the fridge, the smile arrives late — [1–3s] the hand goes in and comes out "
        "with the pair, eyes following it — [3–4s] a satisfied glance as the door closes.",
        "his eyes narrow slightly against the fridge light.",
        "mugging, laughing, looking into the lens, presenting the pair.",
    ),
    "CAMERA — authored, designed camera: locked off, STAYS PUT, 84°; level horizon. NOT: handheld shake, push-in, zoom.",
    "GEOMETRY — the camera sits where the pair was, 0.7 m from his face; the door swings from frame-left.",
    "PHYSICS & MATERIAL — the door swings with weight and seals with a soft thump; the pair is cold and light. OVER-REAL: a "
    "light film of condensation on the cups, the weave of his shirt, stubble and pores. If any surface looks smooth, plastic "
    "or rendered — WRONG.",
    LIVE_LIGHT, LIVE_LOOK,
    "SOUND — the fridge hum; the foil's faint crinkle; the door seal's soft thump at the end. " + MUSIC_BAN,
    LIVE_WORLD,
    "NEGATIVE: a tray, a single cup, the product hidden as it leaves, any camera movement, " + LIVE_NEG_SPINE,
    "[ORDER: 1 locked-off shot, 4s — inside the fridge: his hand covers the lens, pulls out the pair, clearly seen, and the "
    "door shuts to dark. Invariants: a pair of two joined cups; never into the lens; locked off. Look: 35mm negative. NO "
    "music. NO text.]",
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
    "2. THE FOLD: a thumb flat on each cup, the cup BOTTOMS swing toward each other, no pause — WRONG if twisted, pulled apart "
    "or pinched.\n"
    "3. His LEFT hand keeps one cup; his RIGHT hand sets the other on the counter.\n"
    "4. Shot 2 is a THREE-QUARTER, slight HIGH angle (no ceiling in frame); his gaze lifts slightly upward, never into the lens.",
    "TIMELINE — 2 shots, 1 hard cut:\n"
    "SHOT 1 (0–3s) — " + SNAP_SHOT.format(snap="2s") + " HARD CUT.\n"
    "SHOT 2 (3–5s) — " + NOSTALGIA_SHOT + " Hard end.",
    acting_man(
        "get the snap clean and take it in without showing how much it matters. Tactic: savour — straight in, no hesitation, "
        "then let the sound carry him somewhere else.",
        "— [0–2s] hands only — [2s] the crack — [3–4s] the gaze lifts slightly, faraway; one corner of the mouth moves once — "
        "[4–5s] the gaze stays up while his hand sets the cup down by feel.",
        "his shoulders drop a millimetre at the crack.",
        "sitcom delight, mugging, looking into the lens, looking down at the cup, a pause before the snap.",
    ),
    "CAMERA — Shot 1: the macro probe TRAVELS in one steady pull-back. Shot 2: locked off, STAYS PUT, 29°.\n" + MACRO_LENS,
    "GEOMETRY — " + KITCHEN_GEOMETRY + ".",
    "PHYSICS & MATERIAL — the break line resists, then gives all at once with a sharp snap, no splinters, both cups intact and "
    "sealed; the counter takes the cup with a small knock. OVER-REAL: the ridge where the break line parted, foil creases, "
    "condensation, fine hairs on his thumbs. If any surface looks smooth, plastic or rendered — WRONG.",
    LIVE_LIGHT, LIVE_LOOK,
    "SOUND — the créqui, a short, crisp, bright plastic snap, the hero sound of the film; the foil's crinkle; a light knock on "
    "the counter; his breath. " + MUSIC_BAN,
    LIVE_WORLD,
    "NEGATIVE: " + MACRO_NEG + "a pair twisted or pulled apart, three cups, a pause before the snap, a low "
    "angle with the ceiling in frame, " + LIVE_NEG_SPINE,
    "[ORDER: 2 shots, 1 hard cut, 5s — (1, 0–3s) macro pull-back from the thumbs, the fold toward the centre, the snap at 2s; "
    "(2, 3–5s) three-quarter slight high angle, gaze lifting, one cup kept, the other set down. Invariants: the fold; left hand "
    "keeps one; full 16:9 frame. Look: 35mm negative. NO music. NO text.]",
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
    "THE SOUL OF THE SCENE (play it, never explain it): the foil is a treasure and the lick is a ceremony.\n"
    "THE FOIL — " + FOIL_TEXT,
    "ABSOLUTE LOCKS — break one and the take is WRONG, regenerate:\n"
    "1. Cup in his LEFT hand, foil in his RIGHT; the FINGERTIP lifts the foil — no nail, no tab.\n"
    "2. The silver side comes away with a real 2–3 mm layer of pink yogurt and faces the lens as it opens — WRONG if clean or heaped.\n"
    "3. NO text or message on the foil.\n"
    "4. The last second is a TOTAL FREEZE mid-lick.",
    "TIMELINE — 2 shots, 1 hard cut:\n"
    "SHOT 1 (0–2s) — " + FOIL_SHOT + " HARD CUT.\n"
    "SHOT 2 (2–6s) — " + LICK_SHOT.format(freeze="5s"),
    acting_man(
        "get every bit of yogurt off the foil, against his hunger. Tactic: treat the foil like a treasure that could break.",
        "— [0–2s] hands only — [2–3s] a long look at the yogurt — [3–4s] he lifts it, a small inhale — [4–5s] the lick, eyes "
        "half-closed — [5–6s] frozen.",
        "a small inhale before the lick.",
        "mugging, looking into the lens, any movement after the freeze.",
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
    "NEGATIVE: " + MACRO_NEG + "a fingernail or pull tab, a clean silver side, a heap of yogurt, a message on the foil, any movement after the "
    "freeze, " + LIVE_NEG_SPINE,
    "[ORDER: 2 shots, 1 hard cut, 6s — (1, 0–2s) macro beside his hand, push-in, the foil opens like a little door, yogurt "
    "side to the lens; (2, 2–6s) three-quarter slight high angle, the lick, FREEZE from 5s. Invariants: cup left, foil right; "
    "a real layer of yogurt; fingertip; no text. Look: 35mm negative. NO music. NO text.]",
)

# ===========================================================================
# 1d — Cena 1 inteira (1a + 1b + 1c) numa geração só (15 s)
# ===========================================================================
P_1D = _join(
    live_contract(15, "5 shots with 4 hard cuts at 4s, 7s, 9s and 11s"),
    "REFERENCES — each reference has ONE job:\n"
    "@man-portoalegre — IDENTITY of the man. 100% matches.\n"
    "@loc_cozinha — WORLD: the kitchen.\n"
    "@prop_pote-morango — OBJECT ONLY: the yogurt cup and its green foil; in shots 1–2 two of them are joined.\n" + LIVE_SCOPE,
    who_man("takes a pair of joined yogurts from the fridge, splits it with a crisp snap, keeps one cup, opens it and licks "
            "the foil; he never looks into the lens"),
    "SCENE & SOUL — SCENE: one uninterrupted ritual in a summer kitchen, in five shots: the pair from the fridge; the snap; "
    "one cup kept; the foil; the lick; the image freezes. Already in progress.\n"
    "THE SOUL OF THE SCENE (play it, never explain it): the most important small ritual of his day, and nobody knows; the "
    "snap takes him back to childhood.\n"
    "THE PAIR — " + PAIR_TEXT + " THE FOIL (shots 4–5): " + FOIL_TEXT,
    "ABSOLUTE LOCKS — break one and the take is WRONG, regenerate:\n"
    "1. A PAIR of two joined cups (shots 1–2), two separate cups after the snap; NO tray anywhere.\n"
    "2. THE FOLD: a thumb flat on each cup, the cup BOTTOMS swing toward each other, no pause.\n"
    "3. LEFT hand keeps the cup, RIGHT hand sets the other down and lifts the foil with the FINGERTIP; the silver side comes "
    "away with a real 2–3 mm layer of yogurt, never a heap. Real human hands.\n"
    "4. Shots 3 and 5 are THREE-QUARTER, slight HIGH angles; daylight from FRAME-LEFT; macro frames are full 16:9, no "
    "circular border.\n"
    "5. The last second is a TOTAL FREEZE mid-lick.",
    "TIMELINE — 5 shots, 4 hard cuts:\n"
    "SHOT 1 (0–4s) — " + FRIDGE_SHOT + " HARD CUT.\n"
    "SHOT 2 (4–7s) — " + SNAP_SHOT.format(snap="6s") + " HARD CUT.\n"
    "SHOT 3 (7–9s) — " + NOSTALGIA_SHOT + " HARD CUT.\n"
    "SHOT 4 (9–11s) — " + FOIL_SHOT + " HARD CUT.\n"
    "SHOT 5 (11–15s) — " + LICK_SHOT.format(freeze="14s"),
    acting_man(
        "the whole ritual, from the fridge to the last lick, keeping the pleasure small. Tactic: savour — half a beat slower "
        "at the fridge, no hesitation at the snap, reverence at the foil.",
        "— [0–4s] eyes settle on the point in the fridge, the smile arrives late, eyes follow the pair out — [4–7s] hands only, "
        "the crack at 6s — [7–9s] the gaze lifts slightly, faraway, nostalgic — [9–11s] hands only — [11–14s] a long look at "
        "the yogurt, a small inhale, the lick — [14–15s] frozen.",
        "his eyes narrow slightly against the fridge light; his shoulders drop a millimetre at the crack.",
        "mugging, laughing, looking into the lens, a pause before the snap, any movement after the freeze.",
    ),
    "CAMERA — shots 1, 3 and 5 locked off, STAY PUT, at 84°, 29° and 47°; shot 2: one steady macro pull-back; shot 4: one "
    "gentle macro push-in. Natural, fluid camera moves, never mechanical.\n" + MACRO_LENS,
    "GEOMETRY — " + KITCHEN_GEOMETRY + "; in shots 3 and 5 the lens is 35° toward his right side.",
    "PHYSICS & MATERIAL — the break line resists, then gives all at once with a sharp snap, no splinters; the foil lifts "
    "without tearing; the yogurt layer is creamy and clinging; each lick wipes a clean silver stripe. OVER-REAL: condensation "
    "on the cups, the ridge where the break line parted, foil creases, yogurt on bare silver, the weave of his shirt, pores. "
    "If any surface looks smooth, plastic or rendered — WRONG.",
    LIVE_LIGHT, LIVE_LOOK,
    "SOUND — the fridge hum; the door's soft thump; the créqui at 6s, a short, crisp, bright plastic snap; the foil's crinkle; "
    "a small wet lick; near silence at the freeze. " + MUSIC_BAN,
    LIVE_WORLD,
    "NEGATIVE: " + MACRO_NEG + "a tray, a pair twisted or pulled apart, a pause before the snap, a low angle, a clean silver "
    "side, a heap of yogurt, any movement after the freeze, " + LIVE_NEG_SPINE,
    "[ORDER: 5 shots, 4 hard cuts, 15s — (1, 0–4s) inside the fridge, he takes the pair, the door shuts; (2, 4–7s) macro "
    "pull-back, the fold, the snap at 6s; (3, 7–9s) three-quarter high angle, the nostalgic gaze; (4, 9–11s) macro push-in, "
    "the foil opens like a little door; (5, 11–15s) three-quarter, the lick, FREEZE from 14s. Invariants: a pair, no tray; "
    "the fold; cup left, foil right; a real layer of yogurt; real hands; daylight frame-left. Look: 35mm negative. NO music. "
    "NO text.]",
)

# ===========================================================================
# 2a — Mergulho (4 s)
# ===========================================================================
P_2A = _join(
    "CONTRACT — Live-action photoreal raw camera footage with production sound only, 16:9, 4 seconds total, ONE continuous take, time-freeze: everything in "
    "the scene is motionless like a photograph and ONLY the camera moves. Dry comedy played straight. No dialogue. NO music, "
    "NO score, NO subtitles, NO on-screen text.",
    "REFERENCES — each reference has ONE job:\n"
    "[first frame] KEYFRAME: the take STARTS from this exact frame (the man mid-lick, the foil at his mouth, the open cup in his "
    "left hand) and the world stays frozen in it; light, grade and skin continue the keyframe exactly.\n"
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
    "BEAT 1 (0–1s) — MCU 47°, the frozen frame, the camera 0.8 m from him and diagonal, about 35° toward his right side, 15 cm "
    "above his eye line; the camera begins to drift forward.\n"
    "BEAT 2 (1–3s) — the camera arcs forward and down past his chest, 20 cm above his thumb, toward the open cup in his left "
    "hand; the rim grows in the lower right of the frame and the yogurt surface, glossy with one frozen swirl, fills the "
    "lens.\n"
    "BEAT 3 (3–4s) — the lens dives through the surface; the frame fills with soft, uniform strawberry-cream pink. Hard end on the "
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
    "35mm negative. NO music. NO text.]",
)

# ===========================================================================
# 7a — A vitória (6 s)
# ===========================================================================
P_7A = _join(
    live_contract(6, "ONE continuous take", "; a wordless laugh is allowed, no words and no exclamations"),
    "REFERENCES — each reference has ONE job:\n"
    "[first frame] KEYFRAME: the take STARTS from this exact frame (the man mid-lick, the foil at his mouth, the open cup in his "
    "left hand) and comes alive from it; light, grade and skin continue the keyframe exactly.\n"
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
    "BEAT 1 (0–1s) — the lick ends and the foil leaves his mouth.\n"
    "BEAT 2 (1–2s) — he looks at the foil in his right hand to check for leftover yogurt; its silver inner side, licked almost "
    "clean with a last faint pink smear at one corner, faces him, not the camera.\n"
    "BEAT 3 (2–3s) — he sees he has won: his face lights up at once.\n"
    "BEAT 4 (3–6s) — he celebrates, raising the foil high with his right arm, laughing without words. Hard "
    "end at the peak of the celebration.",
    acting_man(
        "own the win, now, in his whole body. Tactic: verify, then pure joy — a quick check that turns into joy with no pause.",
        "— [0–1s] the last sweep of the lick — [1–2s] eyes open and search the foil — [2–3s] the discovery: the eyes widen and "
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
    "hand; no pause; no text; the camera locked as the keyframe; alone. Look: 35mm negative, summer window light. NO music. NO "
    "text.]",
)

# ===========================================================================
# MUNDO TOON (fábrica)
# ===========================================================================
TOON_LOOK = (
    "FILM LOOK (KEY — reproduce this exact look): premium 3D animation, a miniature designer-toy diorama. The WORLD and the "
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
    "minion-style (KEY): the cows are cute, eager little workers in a family animated comedy, a bit clumsy: they rush, "
    "overcommit, wobble under things too big for them, nearly drop them, recover in a hurry and look very proud of themselves. "
    "Quick, bouncy reactions, big round happy smiles, open eyes; tiny mishaps that never break anything and never hurt anyone. "
    "Never angry, never bored, never blank."
)

# Escala: vacas pequenas num mundo grande (do blocking do diretor)
TOON_SCALE = (
    "SCALE (KEY — small cows in a big world): the cows are small; each fills only about a quarter of the frame height. Above "
    "them rises tall wall with portholes and high shelves of pink cups, at least twice their height. Everything they handle is "
    "oversized for them: a strawberry or an apple is as big as a cow's head or bigger, a coconut half is as wide as a cow, the "
    "pulp funnel is twice a cow's height, the microphone stand is taller than a cow, each easel is taller than its painter, "
    "each pink yogurt cup is about half a cow's height."
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
    "SOUND — SOFT CARTOON FOLEY ONLY: the belt's low hum, padded footsteps of vinyl hooves, the golden bells' soft ding (one "
    "note per weight shift), squeaky rubbery fruit, gentle machine puffs, small happy grunts of effort (no words). " + MUSIC_BAN
)

TOON_NEG_SPINE = (
    "eyebrows, frowning or angry faces, cows filling the frame, normal-size fruit, humans, speech or lip-sync, keyring, wrong "
    "number of cows, merged cows, swapped ear colours, 2D cel look, glossy plastic, hard black shadows, dirt, film grain, "
    "camera shake, readable text, logos, subtitles, music, wrong aspect ratio."
)


def toon_contract(secs, shots):
    return (
        "CONTRACT — 3D animated footage, miniature designer-toy diorama, 16:9, %d seconds total, %s, real-time animation at 24 fps "
        "with light squash and stretch. No speech, no lip-sync, no voice-over (a voice-over is added in post). ABSOLUTELY NO "
        "MUSIC, NO score, NO subtitles, NO on-screen text of any kind: no letters, no numerals, no logos." % (secs, shots)
    )


TOON_CAMERA_TRAVEL = (
    "CAMERA — a miniature rail just behind the near edge of the belt, planimetric (no yaw, roll or tilt), TRAVELS FRAME-LEFT "
    "to FRAME-RIGHT at a constant calm speed, about one cow-length per second, never stopping, reversing or cutting. WIDE, "
    "63°, the lens low at belt height: the belt big in the foreground across the bottom fifth of the frame, the cows about "
    "1.5 cow-lengths behind it, small, tall wall above them; the dividing walls pass close to the lens as dark wipes; focus on "
    "the cows; level horizon. NOT: close-ups, handheld shake, drone, zoom, speed ramps."
)

_OPEN_A = (
    "BEAT 1 (0–2s) — the first frame is the approved last frame of the previous shot: the lens is covered in thick pink yogurt. "
    "A cow in a white hairnet, VERY close to the camera (her face fills the lower half of the frame), wipes the lens with a "
    "white cloth in two quick, over-eager strokes; the yogurt goes onto the cloth and the glass is left clean. She hurries out "
    "of frame toward frame-left, nearly tripping, and the wide factory appears behind her, the travelling already moving."
)
_OPEN_B = (
    "BEAT 1 (0–2s) — the first frame is the approved last frame of the previous shot: the lens is covered in thick pink yogurt. "
    "With nobody in front of the camera, the yogurt slides down the glass like a thick gel and runs off the bottom edge, leaving "
    "a perfectly clean lens; the wide factory appears from the top down and the travelling is already moving."
)


def _spine(opening, name):
    return _join(
        toon_contract(30, "ONE continuous take with no cuts, a wide side-on travelling shot"),
        "REFERENCES — each reference has ONE job:\n"
        "[first frame] KEYFRAME: the take STARTS from this exact frame (the lens covered in pink yogurt).\n"
        "[video reference] BLOCKING — CAMERA AND SCALE ONLY: follow its camera path (side-on, left to right, constant speed), its "
        "wide framing with the lens low behind the belt, the belt in the foreground, and the size of the cows relative to the "
        "set and the props. IGNORE its untextured grey clay surfaces, its lighting and colours, and the cows' poses and faces.\n"
        "@char_vaca-vinil — IDENTITY of the cow.\n@char_alegrinha-looks — the cow's four outfits, one per hall.\n"
        "@loc_fabrica — WORLD: the factory's materials, props and colours.\n" + TOON_SCOPE,
        "WHO IS WHO — READ FIRST, ABSOLUTE:\n" + COW + "\n"
        "HALLS: hall 1 (fruit selection) three cows; hall 2 (pulp lab) three; hall 3 (sound studio) exactly TWO, one inside the "
        "glass booth and one outside at the audio desk; hall 4 (art studio) three. Each cow does ONE job, the one in the TIMELINE, "
        "and NEVER another.\n" +
        ("FACES: no cow looks into the lens (except the wiping cow in the opening, who looks at the glass); no cow speaks; no "
         "human exists.\nCONTACT: cows touch only fruit, tools and the cloth." if name == "A" else
         "FACES: no cow looks into the lens; no cow speaks; no human exists.\nCONTACT: cows touch only fruit and tools."),
        "SCENE & SOUL — SCENE: a long, wide side-on travelling shot along a production line in a big green factory run by small "
        "cows: giant fruit is selected, pressed into pulp, packed with a crisp créqui, and finally yogurt is painted onto foil. "
        "Already in progress at the first frame.\n"
        "THE SOUL OF THE SCENE (play it, never explain it): the cows are tiny, the job is huge, and they love it; every little "
        "mishap is fixed in a hurry and celebrated.",
        "ABSOLUTE LOCKS — break one and the take is WRONG, regenerate:\n"
        "1. COW COUNTS: hall 1 three cows, hall 2 three, hall 3 exactly TWO, hall 4 three — WRONG if a count changes or two cows "
        "merge.\n"
        "2. WIDE AND SMALL: the camera stays wide and low behind the belt and moves FRAME-LEFT to FRAME-RIGHT at a constant speed "
        "for all 30 seconds, never cutting, stopping or reversing; each cow fills only about a quarter of the frame height — "
        "WRONG if a cow fills the frame.\n"
        "3. HAPPY FACES: NO eyebrows, NO frown on any cow; her RIGHT ear is the black one; NO keyring.\n"
        "4. EACH HALL KEEPS ITS OUTFIT: hairnet and apron, lab coat, headphones, painter's smock and beret.\n"
        "5. NO TEXT of any kind anywhere.",
        "TIMELINE — ONE continuous take, no cuts, already in progress at the first frame:\n" + opening + "\n"
        "BEAT 2 (2–7s) — HALL 1, fruit selection: giant strawberries, apples and coconut halves ride the belt in the foreground. "
        "Three small cows in hairnets, white boots and aprons stand at small round tables behind the belt. COW A hugs a "
        "strawberry bigger than her head, waddles it to the belt, wobbles, drops it on with a bounce and pats it proudly; COW B "
        "lifts an apple bigger than her head to inspect it, it slips, she juggles it twice, catches it with a relieved grin and "
        "sets it on the belt; COW C shoves a coconut half onto the belt with her whole body, nearly slips and throws a quick "
        "thumbs-up.\n"
        "BEAT 3 (7–14s) — HALL 2, pulp lab: a huge pulp funnel twice a cow's height, thick pink pulp running in glass tubes. "
        "Three small cows in white lab coats. COW A, on tiptoe, tosses a strawberry up into the funnel; it drops in with a plop "
        "and she hops for joy; COW B holds a test tube up to a tall strip of pink swatches on the wall and nods so hard her bell "
        "rings; COW C slaps a big green button with both gloves, a pink yogurt cup pops out onto the belt, she startles, then "
        "claps. From here on pink cups ride the belt.\n"
        "BEAT 4 (14–21s) — HALL 3, sound studio: a tall wall of acoustic foam and a glass booth. Inside, standing on a little box "
        "at a microphone stand taller than she is, COW A holds a pair of joined yogurt cups with a gloved thumb flat on top of "
        "each cup and folds the pair toward its centre, the cup bottoms swinging toward each other underneath, until it snaps "
        "with a crisp créqui; she flinches at her own loud snap, ears flying, then grins. Outside the booth, COW B, only her head "
        "and headphones showing above a big cartoon audio desk, closes her eyes, purses her lips in a satisfied pout as if mooing "
        "and sways.\n"
        "BEAT 5 (21–30s) — HALL 4, art studio: easels taller than the painters, each with a big flat sheet of soft aluminum foil. "
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
        "half drags; the pink pulp is thick and slow in the glass tubes; the cup pops out with a small hop; yogurt is thick and "
        "glossy and clings to the brush and the glove; the foil is a thin soft sheet that flexes when brushed; " + ("the cloth in "
        "the opening is white and absorbent; " if name == "A" else "in the opening the yogurt on the lens is a thick gel that "
        "slides down the glass by itself and leaves it clean; ") + "the bells ding once per weight shift. Nothing floats, nothing "
        "loops. MATERIAL TRUTH of this world: matte vinyl with faint seam lines and soft fillets, a tiny glint on the golden bells, "
        "glossy pulp and yogurt, rubbery fruit with modelled seeds; pristine, never dirt.",
        TOON_LIGHT, TOON_LOOK, TOON_SOUND_BASE, TOON_WORLD,
        "NEGATIVE: a fourth cow in hall 3, a cut, a stop, the camera reversing, close framing, " + TOON_NEG_SPINE,
        "[ORDER: 1 continuous take, 30s, wide side-on travelling left to right, small cows in a big world — (0–2s) opening on the "
        "yogurt-covered lens; (2–7s) hall 1, giant fruit; (7–14s) hall 2, the funnel, the button, cups pop onto the belt; "
        "(14–21s) hall 3, the fold and the créqui, the pout; (21–30s) hall 4, the bump, the pink glove, the stroke. Invariants: "
        "cow counts 3-3-2-3; wide, cows a quarter of the frame height; constant direction and speed, no cuts; no eyebrows, no "
        "frowns, black right ear, no keyring; outfit per hall; no text. Look: matte vinyl, mostly monochromatic green, clean. "
        "ABSOLUTELY NO MUSIC. NO text.]",
    )


P_3A_A = _spine(_OPEN_A, "A")
P_3A_B = _spine(_OPEN_B, "B")


def _insert(label, seconds, who, scene_soul, locks, shots, acting, geometry, physics, order, extra_neg=""):
    return _join(
        toon_contract(seconds, label),
        "REFERENCES — each reference has ONE job:\n@char_vaca-vinil — IDENTITY of the cow.\n@char_alegrinha-looks — the cow's outfit "
        "for this hall.\n@loc_fabrica — WORLD: the hall's materials, props and colours.\n" + TOON_SCOPE,
        "WHO IS WHO — READ FIRST, ABSOLUTE:\n" + COW + "\n" + who,
        scene_soul,
        "ABSOLUTE LOCKS — break one and the take is WRONG, regenerate:\n" + locks,
        "TIMELINE — hard cuts only at the specified seconds; the camera adds no cuts of its own:\n" + shots,
        "ACTING — " + COW_STYLE + " " + acting.replace("ACTING — ", "", 1),
        "CAMERA — locked off in each shot, STAYS PUT; WIDE and LOW, never a close-up of a face: the cow is small in the frame and "
        "the oversized props and the tall set around her dominate; shot sizes and angles as stated per shot; no lens drift inside "
        "a shot; level horizon unless a shot says top-down. NOT: close-ups, a cow filling the frame, handheld shake, drone, orbit, "
        "whip pan, zoom.",
        "GEOMETRY — " + TOON_SCALE + " " + geometry,
        physics,
        TOON_LIGHT, TOON_LOOK, TOON_SOUND_BASE, TOON_WORLD,
        "NEGATIVE: " + extra_neg + TOON_NEG_SPINE,
        order,
    )


_INS_LOCKS_TAIL = (
    "3. HAPPY FACES: NO eyebrows, NO frown; her RIGHT ear is the black one; NO keyring.\n4. NO text anywhere.\n"
    "5. Lit side FRAME-LEFT."
)

P_3B = _insert(
    "2 shots with 1 hard cut at 4s", 8,
    "HALL 1 outfit: a white hairnet with the horns poking through, white rubber boots and a pale-green apron.",
    "SCENE & SOUL — SCENE: hall 1, fruit selection, seen from above and from belt level. Already in progress.\n"
    "THE SOUL OF THE SCENE (play it, never explain it): the fruit is enormous, the cows are tiny, and they are thrilled.",
    "1. SHOT 1 shows exactly TWO small cows; SHOT 2 shows EXACTLY ONE cow — WRONG if more cows appear.\n"
    "2. WIDE AND SMALL: every cow is small in frame and the fruit is bigger than her head — WRONG if a cow fills the frame.\n"
    + _INS_LOCKS_TAIL,
    "SHOT 1 (0–4s) — straight-down top view, 63°, wide: the white belt crosses the frame left to right carrying giant "
    "strawberries, apples and coconut halves; at the belt's edges two small cows in hairnets reach in with both arms; one "
    "tugs a strawberry bigger than herself off the belt and staggers back with it, the other leans in after a bruised apple.\n"
    "SHOT 2 (4–8s) — low wide angle at belt level, 47°: a giant strawberry soft in the foreground; behind it one small cow in a "
    "hairnet and apron hugs another strawberry bigger than her head, inspects it nose to seed, wobbles, and nods proudly. Hard "
    "end.",
    "ACTING — shot 1: two eager tuggers, one triumphant stagger. Shot 2: the cow inspects like a jeweller who can barely lift "
    "the jewel; detail: her left ear flicks when she approves; the smile wide. NOT: looking into the lens, frowning, eyebrows, "
    "a blank face.",
    "Shot 1: the belt crosses the frame at its vertical centre, the cows at its top and bottom edges, small. Shot 2: the "
    "foreground strawberry fills the lower left corner, soft; the cow stands 1.5 cow-lengths behind it at screen-centre-right, "
    "about a quarter of the frame height, tall wall above her.",
    "PHYSICS & MATERIAL — the strawberries are heavy for the cows and rubbery: they dent under a hug and recover slowly; the "
    "stagger has real weight; the bell swings and dings once per wobble. Nothing floats, nothing loops. MATERIAL TRUTH: matte "
    "vinyl, modelled seeds on the strawberry, soft fillets; never dirt.",
    "[ORDER: 2 shots, 1 hard cut, 8s — (1, 0–4s) top view, giant fruit, two small cows tugging; (2, 4–8s) low wide, one small "
    "cow hugging a giant strawberry. Invariants: cows small, fruit giant; no eyebrows, no frowns; black right ear; no text. "
    "ABSOLUTELY NO MUSIC.]",
)

P_4B = _insert(
    "3 shots with 2 hard cuts at 3s and 6s", 9,
    "HALL 2 outfit: a white lab coat with a blank badge and white rubber boots.",
    "SCENE & SOUL — SCENE: hall 2, the pulp lab, in three wide details. Already in progress.\n"
    "THE SOUL OF THE SCENE (play it, never explain it): science, taken far too seriously by someone far too small, and loved "
    "completely.",
    "1. EACH SHOT shows EXACTLY ONE small cow (in shot 3 she is in the background) — WRONG if more cows appear.\n"
    "2. WIDE AND SMALL: the funnel is twice her height, the swatch strip taller than her — WRONG if a cow fills the frame.\n"
    + _INS_LOCKS_TAIL,
    "SHOT 1 (0–3s) — low wide angle, 63°: the huge pulp funnel towers over a small cow; on tiptoe she tosses a strawberry up "
    "into it; it drops in with a plop and she hops for joy; thick pink pulp runs down the glass tubes.\n"
    "SHOT 2 (3–6s) — wide, 47°: a small cow in a lab coat in front of a strip of pink swatches taller than she is; she holds "
    "a test tube of pink pulp up against it, compares, and nods so hard her bell rings.\n"
    "SHOT 3 (6–9s) — low at belt level, 47°: a nozzle fills a pink cup on the belt with thick pink yogurt pulp; behind the "
    "cup, small, a cow peeks over the rim, delighted. Hard end.",
    "ACTING — shot 1: the tiptoe toss, the hop. Shot 2: the over-eager nod; detail: one ear tilts first. Shot 3: the peek of "
    "pure delight. NOT: looking into the lens, frowning, eyebrows, a blank face.",
    "Shot 1: the funnel at frame-centre rising out of the top of the frame, the cow small at its foot, frame-left. Shot 2: the "
    "cow at the screen-left third, the swatch strip rising behind her. Shot 3: the nozzle above the belt at frame-centre, the "
    "cup beneath it in the foreground, the cow 1.5 cow-lengths behind.",
    "PHYSICS & MATERIAL — the pulp is thick and slow, it coats the glass and gathers in the cup; the strawberry tumbles once "
    "and drops; the cup fills gradually (START empty, DURING rising pink, END full to the rim). Nothing floats, nothing loops. "
    "MATERIAL TRUTH: matte vinyl machines, glossy pulp, clear glass tubes; never dirt.",
    "[ORDER: 3 shots, 2 hard cuts, 9s — (1, 0–3s) the giant funnel, the tiptoe toss; (2, 3–6s) the tall swatch strip, the "
    "nod; (3, 6–9s) the nozzle fills the cup, the cow peeks. Invariants: one small cow per shot; giant props; no eyebrows, no "
    "frowns; black right ear; no text. ABSOLUTELY NO MUSIC.]",
)

P_5B = _insert(
    "2 shots with 1 hard cut at 4s", 8,
    "HALL 3: exactly TWO cows — COW A inside the glass acoustic booth, in plain cream vinyl, at the microphone; COW B outside the "
    "booth at the audio desk, wearing over-ear headphones. Each shot shows ONE of them.",
    "SCENE & SOUL — SCENE: hall 3, the sound studio, in two wide shots. Already in progress.\n"
    "THE SOUL OF THE SCENE (play it, never explain it): the créqui is music to the engineer's ears.",
    "1. EXACTLY TWO cows in this hall; each shot shows one — WRONG if a third appears.\n"
    "2. THE FOLD: TWO joined cups before the snap and TWO after; a gloved thumb flat on top of each cup, the cup bottoms "
    "swinging toward each other underneath — WRONG if she twists or pulls it apart. Both cows small in frame.\n"
    + _INS_LOCKS_TAIL,
    "SHOT 1 (0–4s) — wide, 47°, inside the glass acoustic booth: a tall wall of acoustic foam, a microphone with a round pop "
    "filter on a stand taller than the cow; small COW A stands on a little box in front of it, holds a pair of joined yogurt "
    "cups with a gloved thumb flat on top of each cup and folds the pair toward its centre, the cup bottoms swinging toward "
    "each other underneath, until the break line snaps with a crisp créqui; the needle on a meter jumps; she flinches at her "
    "own loud snap, ears flying, then grins.\n"
    "SHOT 2 (4–8s) — low, 47°, from behind the edge of a big cartoon audio desk with a few simple sliders, which fills the "
    "lower half of the frame: only COW B's head and headphones show above it; she listens, eyes closed, purses her lips in a "
    "small satisfied pout as if mooing and sways. Hard end.",
    "ACTING — COW A: total concentration, then the flinch at her own snap, then the grin. COW B: bliss; detail: a slow, dreamy sway. NOT: looking into the lens, mouths forming words, frowning, eyebrows, a blank face.",
    "Shot 1: the cow at screen-centre on her box, the microphone between her and frame-left, the foam wall rising behind her "
    "out of the top of the frame. Shot 2: the desk across the lower half, the cow's head at the screen-right third, the booth "
    "glass soft behind her at frame-left.",
    "PHYSICS & MATERIAL — the plastic break line resists, then gives with a sharp snap; no splinters; the cups stay sealed; the "
    "meter's needle jumps and settles with a small overshoot; the glass booth shows soft reflections. Nothing floats, nothing "
    "loops. MATERIAL TRUTH: matte vinyl, clear glass, soft acoustic foam; never dirt.",
    "[ORDER: 2 shots, 1 hard cut, 8s — (1, 0–4s) wide in the booth, the small cow folds the pair, the créqui, the flinch; "
    "(2, 4–8s) behind the big desk, the satisfied pout. Invariants: exactly two cows, small; the fold toward the centre; no "
    "eyebrows, no frowns; black right ear; no text. ABSOLUTELY NO MUSIC.]",
    extra_neg="a third cow, a pair that never separates, a pair twisted or pulled apart, three cups, ",
)

P_6B = _insert(
    "3 shots with 2 hard cuts at 3s and 6s", 9,
    "HALL 4 outfit: a cream painter's smock and a small beret between the horns. Three cows, one per easel; each shot shows one.",
    "SCENE & SOUL — SCENE: hall 4, the art studio, in three wide beats. Already in progress.\n"
    "THE SOUL OF THE SCENE (play it, never explain it): they paint yogurt onto foil with the gravity of old masters and the "
    "coordination of toddlers.",
    "1. THREE cows in this hall, one per easel; each shot shows one — WRONG if the count changes.\n"
    "2. The painting is PLAIN: simple yogurt strokes, NO decoration, NO drawing, NO letters; every easel is taller than its "
    "painter.\n" + _INS_LOCKS_TAIL,
    "SHOT 1 (0–3s) — low wide angle, 47°: an easel taller than the painter holds a big flat sheet of soft aluminum foil; small "
    "COW C, on tiptoe, brushes one plain stroke of yogurt onto it, the tip of her red tongue poking out in concentration.\n"
    "SHOT 2 (3–6s) — wide, 47°: a pot of yogurt as tall as her waist; COW B dips her brush in so deep that her whole glove comes "
    "out pink, looks at it, and shrugs happily.\n"
    "SHOT 3 (6–9s) — over-the-shoulder, 47°, from just behind COW A, who has stepped back to judge her work: she makes a finger "
    "frame with her gloved fingers around the foil on her towering easel. Hard end.",
    "ACTING — COW C: the tongue of concentration, the careful stroke. COW B: the pink glove, the happy shrug. COW A: the art "
    "critic's finger frame; detail: she tilts her head. NOT: looking into the lens, frowning, eyebrows, a blank face, "
    "decoration on the foil.",
    "Shots 1 and 2: the cow small at the screen-left third, the easel or the pot rising beside her; shot 3: the camera 0.5 "
    "cow-lengths behind and to the left of COW A's shoulder, her finger frame at frame-centre, the foil on the easel sharp "
    "inside it, the easel about 2 cow-lengths away and taller than her.",
    "PHYSICS & MATERIAL — the foil is a thin soft aluminum sheet that flexes slightly under the brush; the yogurt is thick and "
    "glossy, it drags and leaves a clean ridge; the brush dips and lifts heavy with yogurt; the pink glove drips once into the "
    "pot. Nothing floats, nothing loops. MATERIAL TRUTH: matte vinyl, glossy yogurt, soft foil; never dirt.",
    "[ORDER: 3 shots, 2 hard cuts, 9s — (1, 0–3s) the tall easel, the tiptoe stroke; (2, 3–6s) the big pot, the pink glove; "
    "(3, 6–9s) over the shoulder, the finger frame. Invariants: three cows, one per shot, small; plain, no decoration; no "
    "eyebrows, no frowns; black right ear; no text. ABSOLUTELY NO MUSIC.]",
    extra_neg="decoration or drawings on the foil, ",
)

# ===========================================================================
PROMPTS = {
    "1a": ("1a · POV da geladeira", 4, P_1A),
    "1b": ("1b · O créqui", 5, P_1B),
    "1c": ("1c · O foil e a lambida", 6, P_1C),
    "2a": ("2a · Mergulho", 4, P_2A),
    "3a-A": ("3a · Espinha, abertura A (a vaca limpa)", 30, P_3A_A),
    "3a-B": ("3a · Espinha, abertura B (a lente se limpa sozinha)", 30, P_3A_B),
    "3b": ("3b · Inserts do Setor 1", 8, P_3B),
    "4b": ("4b · Inserts do Setor 2", 9, P_4B),
    "5b": ("5b · Inserts do Setor 3", 8, P_5B),
    "6b": ("6b · Inserts do Setor 4", 9, P_6B),
    "7a": ("7a · A vitória", 6, P_7A),
}
# 1d é uma alternativa a 1a+1b+1c (mesmos 15 s); fica fora de BASE_KEYS e ALT_KEYS para não somar duas vezes.
PROMPTS["1d"] = ("1d · Cena 1 inteira (alternativa a 1a+1b+1c)", 15, P_1D)

# Plano base: 3a conta uma vez (abertura A); a B só entra se for testada.
BASE_KEYS = ["1a", "1b", "1c", "2a", "3a-A", "3b", "4b", "5b", "6b", "7a"]
ALT_KEYS = ["3a-B"]

# Higgsfield (página oficial, verificada em 20/10/2026): 8 s = 128 (1080p), 56 (720p), 24 (480p).
# Por segundo (divisão minha): 16 e 3. O preço de finalizar um draft em 1080p não é publicado: assumo uma geração 1080p inteira.
CR_480 = 3
CR_1080 = 16
