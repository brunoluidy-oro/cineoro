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
    "LIGHT — NATURAL LIGHT ONLY, a summer afternoon, bright and warm (KEY):\n"
    "SOURCE: warm daylight through the kitchen window at FRAME-RIGHT (~3800 K), falling on the frame-right side of his face, "
    "the counter and the green tiles; the open fridge's cool white light (~5000 K) from FRAME-LEFT on the frame-left side of "
    "his face and chest.\n"
    "REACH: the fridge light dies within 1.5 m of the fridge; the window light fills the room softly.\n"
    "EXPOSURE: exposed for his face and the foil; highlights roll off warm, shadows hold detail; the film look's gentle "
    "vignette and nothing more.\n"
    "CONTINUITY: cool on the frame-left side of his face and warm on the frame-right side in every shot; the lit sides never "
    "flip.\n"
    "NOT: flat even light, studio fill, a third source, neon, night, glow, haze."
)

LIVE_NEG_SPINE = (
    "smoke, vapour, mist, fog, steam, glassy stare, frozen pupils, doll eyes, warped hands, extra fingers, duplicated people, "
    "twins, a second person, speech or lip-sync, voice-over, readable text, invented logos, stiff or rigid foil, music, score, "
    "subtitles, handheld shake, gimbal wobble, drone, canted horizon, CGI-gloss look, HDR glow, cartoon look, wrong aspect "
    "ratio."
)

MUSIC_BAN = (
    "NO music, NO score, NO BGM, NO instrumental, NO melody, NO ambient pad, NO drone, NO chimes, NO voice-over, NO "
    "narration, NO subtitles."
)


def live_contract(secs, shots, extra=""):
    return (
        "CONTRACT — Live-action photoreal commercial footage, 16:9, %d seconds total, %s, real-time motion. Dry comedy played "
        "completely straight. No dialogue and no voice-over (a voice-over is added in post)%s. NO music, NO score, NO subtitles, "
        "NO on-screen text." % (secs, shots, extra)
    )


def who_man(role, never="NEVER speaks, NEVER removes his glasses, NEVER shows a second person"):
    return (
        "WHO IS WHO — READ FIRST, ABSOLUTE:\n"
        "@man-portoalegre (round black glasses, dark curly hair, short beard, sage-green check short-sleeve shirt over a white "
        "T-shirt, thin silver bracelet on his LEFT wrist — 100% matches its reference) — the MAN: " + role + "; " + never + ".\n"
        "FACES: his face exists once; nobody else is in the apartment, no figure in the window, no reflection of anyone else.\n"
        "CONTACT: the only touches in the scene are his own hands on the objects named below."
    )


def acting_man(event, motive, goal, obstacle, tactic, moments, detail, nots, direction="treat the small thing as sacred."):
    return (
        "ACTING — @man-portoalegre (fully invested in the tactic; the work happens in the eyes)\n"
        "SCENE DIRECTION (shared, unspoken): " + direction + "\n"
        "EVENT: " + event + "\nMOTIVE: " + motive + "\nGOAL: " + goal + "\nOBSTACLE: " + obstacle + "\nTACTIC: " + tactic + "\n"
        "MOMENT TO MOMENT: " + moments + "\n"
        "LIVING EYES: pupils move with the task, search, settle, drift, settle again; blinks uneven and a beat late; brows and "
        "cheeks work independently, slight asymmetry. Involuntary detail: " + detail + " A soft window reflection in the glasses "
        "is fine; a frozen pupil or a glare mask over the eyes is wrong.\n"
        "NOT: " + nots
    )


# Descrições de objeto compartilhadas (idênticas em todos os prompts de captação)
TRAY_TEXT = (
    "a multipack tray of exactly SIX pink ribbed yogurt cups joined in one block, sealed with FOIL: a thin, soft, flexible "
    "aluminum sheet printed in green with a white shield logo and a strawberry, that bends and crinkles and is never stiff."
)
PAIR_TEXT = (
    "exactly TWO pink ribbed yogurt cups joined side by side by a thin plastic break line, each sealed with FOIL: a thin, soft, "
    "flexible aluminum sheet printed in green that bends and crinkles, never stiff."
)
FOIL_TEXT = (
    "a thin, soft, flexible aluminum sheet: its outer face printed in green with a white shield logo and a strawberry, its inner "
    "face plain bare SILVER aluminum coated with a thick layer of pink yogurt that clings to it. It bends and crinkles, never "
    "stiff. There is NO tab and NO writing to read."
)

# ===========================================================================
# 1a — POV da geladeira (6 s)
# ===========================================================================
P_1A = _join(
    live_contract(6, "2 shots with 1 hard cut at 3s, both locked off"),
    "REFERENCES — each reference has ONE job:\n"
    "@man-portoalegre — IDENTITY of the man: face, glasses, hair, beard, hands, build, wardrobe, bracelet. 100% matches.\n"
    "@loc_cozinha — WORLD: the kitchen's architecture and materials, for both shots.\n"
    "@prop_bandeja-morango — OBJECT ONLY: the six-cup yogurt tray, its shape, scale, colours and green foil.\n" + LIVE_SCOPE,
    who_man("opens the fridge and takes the tray; in shot 1 he looks at a fixed point inside the fridge, just beside the "
            "lens, and NEVER into the lens"),
    "SCENE & SOUL — SCENE: a summer afternoon in a Brazilian kitchen with natural window light. He opens the fridge, takes a "
    "yogurt tray and stands holding it. Already in progress at the first frame.\n"
    "THE SOUL OF THE SCENE (play it, never explain it): this is the most important small ritual of his day and nobody knows "
    "about it. He is absolutely serious, like a man collecting a trophy, and he never lets it be funny.",
    "THE TRAY — " + TRAY_TEXT,
    "ABSOLUTE LOCKS — break one and the take is WRONG, regenerate:\n"
    "1. THE TRAY is one block of exactly six joined cups with soft foil — WRONG if it is a pair, a single cup, stiff foil or "
    "any other count.\n"
    "2. FROM SECOND 3 the tray is in his RIGHT hand — WRONG if it changes hands.\n"
    "3. Both shots are LOCKED OFF — WRONG if the camera moves, and WRONG if he looks into the lens.\n"
    "4. THE LIT SIDES NEVER FLIP: window light from FRAME-RIGHT, fridge light from FRAME-LEFT; the fridge stays at frame-left in "
    "shot 2.\n"
    "5. He is ALONE and SILENT — WRONG if a second person, speech or lip-sync appears.",
    "TIMELINE — 2 shots, 1 hard cut; cuts only at the specified points, the camera adds no cuts of its own:\n"
    "SHOT 1 (0–3s) — MCU, 84°, locked off INSIDE the fridge on the middle shelf, lens at shelf height, 0.7 m from the doorway, "
    "looking out. The fridge door is already opening, its edge sliding out past frame-left. His face appears in the doorway, "
    "eyes fixed on a point inside the fridge just beside the lens; a slow smile arrives; at 2s his right hand rises from below "
    "frame and reaches in, fingers opening, until the hand fills the lens, so we do not see what he takes. HARD CUT.\n"
    "SHOT 2 (3–6s) — MS, 47°, locked off at chest height, 1.6 m from him: he stands 0.5 m in front of the open fridge (fridge "
    "and counter at frame-left, window light from frame-right), holding the tray in his right hand at chest height, foil up and "
    "tilted toward the lens so the green foil reads, his left hand loose at his side. He looks at the tray, deadpan. Hard end.",
    acting_man(
        "a man collects his small daily reward from the fridge.",
        "it is the best part of his day, and it is only his.",
        "take it and stand there with it, undisturbed.",
        "his own pleasure, which he must keep under control so it never shows too much.",
        "savour — he moves a half-beat slower than needed so the moment lasts, and lets the eyes carry it.",
        "— [0–1.5s] eyes settle on the point inside the fridge — [1.5–3s] the smile arrives late; the hand goes in before the "
        "smile is finished — [3–4.5s] he stands holding the tray, eyes on the tray — [4.5–6s] eyes lift a little, composed and "
        "content.",
        "his eyes narrow slightly against the fridge light.",
        "mugging, laughing, sitcom delight, looking into the lens, talking.",
    ),
    "CAMERA — authored commercial camera, smooth and designed. Both shots are locked off and STAY PUT: no movement at all.\n"
    "OPTICS: shot 1 at 84°, shot 2 at 47°; natural perspective, round bokeh; no lens drift inside a shot.\n"
    "FOCUS: shot 1 on his eyes with the shelf edge soft in the foreground; shot 2 on his face and the tray together.\n"
    "HORIZON: level.\n"
    "NOT: handheld shake, gimbal wobble, whip, orbit, push-in, pull-back, zoom, drone, canted horizon, slow motion.",
    "GEOMETRY — the fridge is tall, at FRAME-LEFT in shot 2, its door open toward the camera and frame-left; the counter is "
    "beside the fridge, also at frame-left, within reach of his right hand; he stands 0.5 m in front of the fridge at centre-left, "
    "torso square to the camera, so his right hand is the one nearest the fridge; the window is behind and to the right of the "
    "camera. In shot 1 the camera sits where the tray was, 0.7 m from his face; in shot 2 it stands 1.6 m from him. The camera "
    "stays on the same side of the man–fridge line.",
    "PHYSICS & MATERIAL — the fridge door swings with weight and stops against its seal; the tray has the weight of six full "
    "cups and flexes slightly in his hand; the foil crinkles softly where his thumb presses. Nothing floats, nothing loops. "
    "OVER-REAL: a light film of condensation on the cups, faint fold lines in the foil, the weave of his shirt, stubble and skin "
    "pores. If any surface looks clean, smooth, plastic, CGI or rendered — WRONG.",
    LIVE_LIGHT, LIVE_LOOK,
    "SOUND — DIEGETIC ONLY: the low hum of the fridge compressor; the soft thup of the door seal letting go in the first "
    "second; the faint crinkle of the foil; his breath. " + MUSIC_BAN,
    LIVE_WORLD,
    "NEGATIVE: a pair or a single cup instead of the tray, smoke or vapour from the fridge, any camera movement, him looking "
    "into the lens, the tray in his left hand, " + LIVE_NEG_SPINE,
    "[ORDER: 2 shots, 1 hard cut, 6s, both locked off — (1, 0–3s) from inside the fridge, he smiles and his right hand covers "
    "the lens; (2, 3–6s) medium shot, the tray in his right hand. Invariants: one tray of six with soft foil; right hand; "
    "fridge and counter frame-left, window frame-right; alone and silent; never into the lens. Look: "
    "35mm negative, summer window light. NO music. NO text.]",
)

# ===========================================================================
# 1b — O créqui (5 s)
# ===========================================================================
P_1B = _join(
    live_contract(5, "2 shots with 1 hard cut at 3s"),
    "REFERENCES — each reference has ONE job:\n"
    "@man-portoalegre — IDENTITY of the man. 100% matches.\n"
    "@loc_cozinha — WORLD: the kitchen, for both shots.\n"
    "@prop_pote-morango — OBJECT ONLY: one yogurt cup, its shape, colour and green foil; the pack in this shot is two of them "
    "joined.\n" + LIVE_SCOPE,
    who_man("holds a pair of joined yogurts, splits it with a crisp snap and keeps one cup"),
    "SCENE & SOUL — SCENE: the same kitchen and light, a moment after the previous shot. He already holds a pair of two joined "
    "cups, broken off the tray before this shot, off-camera. He splits the pair with a crisp snap. Already in progress.\n"
    "THE SOUL OF THE SCENE (play it, never explain it): the snap is the sound he came for. He takes it in like a first bite and "
    "lets almost nothing show.",
    "THE PAIR — " + PAIR_TEXT,
    "ABSOLUTE LOCKS — break one and the take is WRONG, regenerate:\n"
    "1. NO TRAY anywhere in frame — WRONG if a tray appears.\n"
    "2. TWO joined cups before the snap and exactly TWO separate cups after — WRONG if it stays joined or becomes three.\n"
    "3. After the snap ONE cup stays in his LEFT hand and his RIGHT hand sets the other on the counter at FRAME-LEFT, beside "
    "the fridge.\n"
    "4. The foil stays on both cups, soft and flexible.\n"
    "5. He is ALONE and SILENT; the créqui is the only sound that matters.",
    "TIMELINE — 2 shots, 1 hard cut; cuts only at the specified points:\n"
    "SHOT 1 (0–3s) — extreme close-up with a slim probe macro lens, about 84° of exaggerated perspective, the front element 2 cm "
    "from the pair, gliding slowly along the break line between the two cups (about 5 cm per second). His left hand holds one "
    "cup and his right hand holds the other by the fingertips, one on each side of the line. From the first frame his fingers "
    "are already bending the pair against the break line, with no pause: the line tightens without stopping and at 2s it snaps "
    "with a crisp, bright crack (the créqui): two separate cups, one in each hand. HARD CUT.\n"
    "SHOT 2 (3–5s) — CU, 29°, the camera about 20 cm above his eye line looking down a little (a slight high angle), 0.9 m from "
    "him: eyes half-closed, a contained pleasure. One cup stays in his LEFT hand at chest height; his RIGHT hand sets the other "
    "on the counter at frame-left with a light knock. Hard end.",
    acting_man(
        "a man hears the exact sound he was waiting for.",
        "the créqui is the reason this ritual exists.",
        "get the snap clean and take it in without anyone seeing how much it matters.",
        "his own delight, which wants to show on the crack and which he keeps small.",
        "savour — no hesitation before the snap: he goes straight in, then absorbs it like a bite, and lets the eyes carry it.",
        "— [0–2s] the bend builds without a stop (macro, hands only) — [2s] the crack: his eyes close halfway — [3–4s] one corner "
        "of the mouth moves once — [4–5s] eyes open slowly and follow the cup to the counter.",
        "his shoulders drop a millimetre at the crack.",
        "sitcom delight, mugging, speaking, looking into the lens, a pause before the snap.",
    ),
    "CAMERA — Shot 1: a macro probe TRAVELS slowly along the break line, one movement only. Shot 2: locked off, STAYS PUT, slight "
    "high angle.\n"
    "OPTICS: shot 1 about 84° with exaggerated perspective, nearest things huge, far things small; shot 2 29°; no lens drift "
    "inside a shot.\n"
    "FOCUS: shot 1 on the break line; shot 2 on his eyes.\nHORIZON: level.\n"
    "NOT: handheld shake, orbit, zoom, drone, slow motion.",
    "GEOMETRY — he stands at centre in the kitchen, torso square to the camera in shot 2, so his right hand is toward frame-left; "
    "the counter is beside the fridge at FRAME-LEFT, 0.6 m from his right hand, both out of frame or soft; the window light "
    "comes from frame-right. In shot 1 the pair is held at chest height, tilted toward the probe. The camera stays on the same "
    "side of him as in the previous shot.",
    "PHYSICS & MATERIAL — the plastic break line resists first, then gives all at once with a sharp snap; no splinters and no "
    "loose bits; both cups stay intact and sealed; the foil on each cup flexes and crinkles; a light film of condensation on the "
    "cups; the counter surface takes the cup with a small knock. Nothing floats, nothing loops. OVER-REAL: the thin ridge left "
    "where the break line parted, foil creases, fine hairs on his fingers, the texture of the counter surface. If any surface "
    "looks clean, smooth, plastic, CGI or rendered — WRONG.",
    LIVE_LIGHT, LIVE_LOOK,
    "SOUND — DIEGETIC ONLY: the créqui, a short, crisp, bright plastic snap, loud and clean, the hero sound of the film; the soft "
    "crinkle of the foil; a light knock as the cup meets the counter; his breath; the fridge hum far behind. " + MUSIC_BAN,
    LIVE_WORLD,
    "NEGATIVE: a tray in frame, a pair that never separates, three cups, a pause before the snap, the cup in the wrong hand, "
    "him looking into the lens, " + LIVE_NEG_SPINE,
    "[ORDER: 2 shots, 1 hard cut, 5s — (1, 0–3s) probe macro along the break line, no pause, the snap at 2s; (2, 3–5s) slight "
    "high angle, one cup in his left hand, the other set on the counter. Invariants: no tray; two joined, then two apart; left "
    "hand keeps one; soft foil; alone and silent. Look: 35mm negative, summer window light. NO music. NO text.]",
)

# ===========================================================================
# 1c — O foil e a lambida (6 s)
# ===========================================================================
P_1C = _join(
    live_contract(6, "2 shots with 1 hard cut at 2s"),
    "REFERENCES — each reference has ONE job:\n"
    "@man-portoalegre — IDENTITY of the man. 100% matches.\n"
    "@loc_cozinha — WORLD: the kitchen, for both shots.\n"
    "@prop_pote-morango — OBJECT ONLY: the yogurt cup and its green foil, shape, colour and print.\n" + LIVE_SCOPE,
    who_man("opens the cup in his left hand and licks the yogurt off the foil"),
    "SCENE & SOUL — SCENE: the same kitchen and light. He opens the single cup he kept in his left hand: the foil comes away "
    "with a coat of yogurt on its silver side, and he licks it off. Already in progress.\n"
    "THE SOUL OF THE SCENE (play it, never explain it): the foil is a treasure and the lick is a ceremony. He does it with "
    "complete reverence and complete seriousness.",
    "THE FOIL — " + FOIL_TEXT,
    "ABSOLUTE LOCKS — break one and the take is WRONG, regenerate:\n"
    "1. The cup is in his LEFT hand, the foil in his RIGHT hand.\n"
    "2. THE FOIL COMES AWAY WITH ITS SILVER SIDE COATED IN PINK YOGURT, and that coat is what he licks — WRONG if the silver "
    "side comes away clean.\n"
    "3. THE FINGERTIP (the tip of the last phalanx of his right hand) lifts the foil's edge — WRONG if a fingernail, a tab or "
    "a tool is used.\n"
    "4. NO readable text and NO message anywhere on the foil.\n"
    "5. The hard end falls MID-LICK, foil at his mouth, eyes visible, frame clean (it becomes the freeze frame); he is ALONE "
    "and SILENT.",
    "TIMELINE — 2 shots, 1 hard cut; cuts only at the specified points:\n"
    "SHOT 1 (0–2s) — extreme close-up with a slim probe macro lens, about 84°, the front element 2 cm from the edge of the cup "
    "in his left hand: the fingertip of his right hand lifts the edge of the foil and the soft foil comes away from the rim as "
    "a thin crinkled sheet, its silver inner side coated with a thick layer of pink yogurt. HARD CUT.\n"
    "SHOT 2 (2–6s) — MCU, 47°, the camera about 20 cm above his eye line looking down a little (a slight high angle), 1.2 m "
    "from him, locked off. The open cup in his left hand at chest height, the pink yogurt visible; the foil in his right hand, "
    "its yogurt-coated silver side toward him and tilted so the pink coat catches the light. He looks at it with reverence, "
    "brings it to his mouth and licks the coat off with one slow sweep, a second sweep beginning. Hard end mid-lick: foil at "
    "his mouth, eyes half-closed, cup in his left hand at chest height.",
    acting_man(
        "a man opens his reward and gives the foil the honour it deserves.",
        "the lick is the first taste and he refuses to rush it.",
        "get every bit of yogurt off the foil.",
        "his hunger, which pushes him to hurry against his need for ceremony.",
        "treat the foil like a treasure — he handles it as if it could break, which it cannot.",
        "— [0–2s] eyes on the fingertip (macro, hands only) — [2–3s] eyes on the yogurt-coated silver, a long look — [3–4s] he "
        "lifts it, a small inhale — [4–6s] the lick: eyes close halfway.",
        "a small inhale before the lick.",
        "mugging, speaking, looking into the lens, a fingernail or a tab, a message on the foil, a clean foil.",
    ),
    "CAMERA — Shot 1: macro probe, STAYS PUT. Shot 2: locked off, STAYS PUT, slight high angle.\n"
    "OPTICS: shot 1 about 84° with exaggerated perspective; shot 2 47°; no lens drift inside a shot.\n"
    "FOCUS: shot 1 on the foil's edge; shot 2 on the foil and his lips, eyes just softer.\nHORIZON: level.\n"
    "NOT: handheld shake, orbit, zoom, drone, slow motion.",
    "GEOMETRY — in shot 2 he is centre, torso square to the camera; the open cup in his LEFT hand at chest height, toward "
    "frame-right of his body line; the foil in his RIGHT hand, toward frame-left, rising to his mouth; the fridge and the "
    "counter at frame-left, soft behind him; window light from frame-right. The camera stays on the same side as in the "
    "previous shots.",
    "PHYSICS & MATERIAL — the foil lifts at one corner, bends, crinkles and comes away without tearing; the yogurt coat on its "
    "silver side is thick, glossy and clinging, it does not drip; each lick wipes a clean silver stripe through the pink and "
    "leaves a slight smear at the corner of his lip; the yogurt in the cup is smooth and holds a soft swirl. Nothing floats, "
    "nothing loops. OVER-REAL: the glossy yogurt coat on bare silver, fine foil creases, the faint ring where the foil sealed "
    "the rim, skin pores, a trace of yogurt on his lip. If any surface looks clean, smooth, plastic, CGI or rendered — WRONG.",
    LIVE_LIGHT, LIVE_LOOK,
    "SOUND — DIEGETIC ONLY: the soft crinkle of the foil; a small wet lick; his breath; the fridge hum far behind. " + MUSIC_BAN,
    LIVE_WORLD,
    "NEGATIVE: a fingernail, a pull tab, a message or any readable text on the foil, a clean silver side with no yogurt, the cup "
    "in the right hand, " + LIVE_NEG_SPINE,
    "[ORDER: 2 shots, 1 hard cut, 6s — (1, 0–2s) macro: the fingertip lifts the foil's edge, the silver side comes away coated "
    "in yogurt; (2, 2–6s) slight high angle, he licks the coat off the foil, hard end mid-lick. Invariants: cup left hand, "
    "foil right hand; yogurt on the silver side; fingertip only; no tab, no text; alone and silent. Look: 35mm negative, "
    "summer window light. NO music. NO text.]",
)

# ===========================================================================
# 1d — Cena 1 inteira (1a + 1b + 1c) numa geração só (17 s)
# ===========================================================================
P_1D = _join(
    live_contract(17, "6 shots with 5 hard cuts at 3s, 6s, 9s, 11s and 13s, locked-off cameras and one slow macro glide"),
    "REFERENCES — each reference has ONE job:\n"
    "@man-portoalegre — IDENTITY of the man. 100% matches.\n"
    "@loc_cozinha — WORLD: the kitchen's architecture and materials, for all shots.\n"
    "@prop_bandeja-morango — OBJECT ONLY, shots 1–2: the six-cup tray, its shape, scale, colours and green foil.\n"
    "@prop_pote-morango — OBJECT ONLY, shots 3–6: the yogurt cup and its green foil.\n" + LIVE_SCOPE,
    "WHO IS WHO — READ FIRST, ABSOLUTE:\n"
    "@man-portoalegre (round black glasses, dark curly hair, short beard, sage-green check short-sleeve shirt over a white "
    "T-shirt, thin silver bracelet on his LEFT wrist) — the MAN: takes the tray from the fridge, splits a pair with a crisp "
    "snap, keeps one cup, opens it and licks the yogurt off the foil; NEVER speaks, NEVER removes his glasses, NEVER looks into "
    "the lens (in shot 1 he looks at a point inside the fridge beside it). He is alone; his face exists once.",
    "SCENE — one uninterrupted ritual in a summer kitchen with natural window light, in six shots: he takes a yogurt tray from "
    "the fridge; a pair is broken off it off-camera between shots 2 and 3; he splits the pair with a crisp snap, keeps one "
    "cup, sets the other on the counter, opens the cup and licks the yogurt off the foil. Already in progress.\n"
    "THE SOUL OF THE SCENE (play it, never explain it): the most important small ritual of his day, and nobody knows. The snap "
    "is the sound he came for, the foil a treasure, the lick a ceremony. He is absolutely serious and never lets it be funny.",
    "THE PACK — shots 1–2: a tray of exactly SIX pink ribbed yogurt cups joined in one block; shot 3: a pair, exactly TWO "
    "joined by a thin plastic break line; shots 4–6: two separate cups. Every cup is sealed with FOIL: a thin, soft, flexible "
    "aluminum sheet, its outer face printed green (white shield logo, a strawberry), its inner face bare SILVER aluminum "
    "coated with a thick layer of pink yogurt. It bends and crinkles, never stiff; NO tab, NO writing.",
    "ABSOLUTE LOCKS — break one and the take is WRONG, regenerate:\n"
    "1. PACK PROGRESSION: tray of six (shots 1–2), pair (shot 3), two separate cups (shots 4–6); NO tray in frame from shot 3 — "
    "WRONG if a count changes or a tray returns.\n"
    "2. HANDS: the tray is in his RIGHT hand; after the snap ONE cup stays in his LEFT hand and his RIGHT hand sets the other "
    "on the counter; in shots 5–6 the cup is in his LEFT hand and the foil in his RIGHT.\n"
    "3. THE FOIL is lifted by the FINGERTIP (tip of the last phalanx) and comes away with its SILVER SIDE COATED IN PINK "
    "YOGURT, which he licks — WRONG with a nail, tab or tool, a clean silver side, or any text or message on it.\n"
    "4. THE LIT SIDES NEVER FLIP: window light from FRAME-RIGHT, fridge and counter at FRAME-LEFT, in every shot.\n"
    "5. ALONE and SILENT; the hard end falls MID-LICK, foil at his mouth, frame clean.",
    "TIMELINE — 6 shots, 5 hard cuts; cuts only at the specified points, the camera adds no cuts of its own:\n"
    "SHOT 1 (0–3s) — MCU, 84°, locked off INSIDE the fridge on the middle shelf, 0.7 m from the doorway. The door is already "
    "opening past frame-left. His face appears, eyes on a point inside the fridge beside the lens; a slow smile arrives; at 2s "
    "his right hand reaches in and fills the lens, so we do not see what he takes. HARD CUT.\n"
    "SHOT 2 (3–6s) — MS, 47°, locked off at chest height, 1.6 m from him: he stands 0.5 m in front of the open fridge holding "
    "the tray in his right hand at chest height, foil up and tilted toward the lens, his left hand loose. He looks at the tray, "
    "deadpan. HARD CUT.\n"
    "SHOT 3 (6–9s) — extreme close-up, slim probe macro lens, 84° with exaggerated perspective, the front element 2 cm from a "
    "pair of joined cups, gliding slowly along the break line (about 5 cm per second). His left hand holds one cup and his "
    "right hand the other, by the fingertips. From the first frame his fingers are already bending the pair, with no pause: "
    "the line tightens without stopping and at 8s it snaps with a crisp, bright crack (the créqui): two cups. HARD CUT.\n"
    "SHOT 4 (9–11s) — CU, 29°, the camera 20 cm above his eye line looking down a little (a slight high angle), 0.9 m from him: "
    "eyes half-closed, a contained pleasure. One cup stays in his LEFT hand at chest height; his RIGHT hand sets the other on "
    "the counter at frame-left with a light knock. HARD CUT.\n"
    "SHOT 5 (11–13s) — extreme close-up, macro probe, 84°, the front element 2 cm from the rim of the cup in his left hand: "
    "the fingertip of his right hand lifts the foil's edge and the soft foil comes away as a thin crinkled sheet, its silver "
    "inner side coated with thick pink yogurt. HARD CUT.\n"
    "SHOT 6 (13–17s) — MCU, 47°, slight high angle (20 cm above his eye line), 1.2 m from him, locked off. The open cup in his "
    "left hand at chest height, the pink yogurt visible; the foil in his right hand, its yogurt-coated silver side toward him, "
    "tilted so the pink catches the light. He looks at it with reverence, brings it to his mouth and licks the coat off in "
    "one slow sweep, a second beginning. Hard end mid-lick: foil at his mouth, eyes half-closed, cup in his left hand.",
    acting_man(
        "a man performs his small daily ritual, from the fridge to the last lick.",
        "it is the best part of his day, and only his.",
        "take it, get the snap clean, get every bit of yogurt off the foil.",
        "his own pleasure, which wants to show and which he keeps small.",
        "savour — a half-beat slower at the fridge, no hesitation at the snap, reverence at the foil; the eyes carry everything.",
        "— [0–1.5s] eyes settle on the point in the fridge — [1.5–3s] the smile arrives late; the hand goes in before it is "
        "finished — [3–6s] holding the tray, eyes on it, then lifting a little, composed — [6–8s] the bend builds without a stop "
        "(hands only) — [8s] the crack: eyes close halfway — [9–11s] one corner of the mouth moves once; eyes open slowly and "
        "follow the cup to the counter — [11–13s] hands only — [13–14s] eyes on the yogurt-coated silver, a long look — "
        "[14–15s] he lifts it, a small inhale — [15–17s] the lick: eyes close halfway.",
        "his eyes narrow slightly against the fridge light at the start; his shoulders drop a millimetre at the crack.",
        "mugging, laughing, sitcom delight, looking into the lens, talking, a pause before the snap.",
    ),
    "CAMERA — authored commercial camera. Shots 1, 2, 4 and 6 are locked off and STAY PUT. Shot 3: the macro probe TRAVELS "
    "slowly along the break line, one movement only. Shot 5: the macro probe STAYS PUT.\n"
    "OPTICS: as stated per shot; no lens drift inside a shot.\n"
    "FOCUS: on his eyes or on the object each shot is about.\nHORIZON: level.\n"
    "NOT: handheld shake, gimbal wobble, whip, orbit, push-in, zoom, drone, slow motion.",
    "GEOMETRY — fridge and counter at FRAME-LEFT, window light from frame-right; he stands torso square to the camera, so his "
    "right hand is the one nearest the fridge and counter. The camera stays on the same side of the man–fridge line in every "
    "shot.",
    "PHYSICS & MATERIAL — the break line resists, then gives all at once with a sharp snap, no splinters; the foil lifts at one "
    "corner, bends and crinkles without tearing; the yogurt coat on the silver is thick, glossy and clinging, and does not drip; "
    "each lick wipes a clean silver stripe and leaves a slight smear at the corner of his lip. Nothing floats, nothing loops. "
    "OVER-REAL: a light film of condensation on the cups, the ridge where the break line parted, fine foil creases, glossy "
    "yogurt on bare silver, the weave of his shirt, stubble and skin pores. If any surface looks clean, smooth, plastic, CGI or "
    "rendered — WRONG.",
    LIVE_LIGHT, LIVE_LOOK,
    "SOUND — DIEGETIC ONLY: the fridge compressor hum; the soft thup of the door seal in the first second; the crinkle of the "
    "foil; the créqui at 8s, a short, crisp, bright plastic snap, the hero sound of the film; a light knock of the cup on the "
    "counter; a small wet lick; his breath. " + MUSIC_BAN,
    LIVE_WORLD,
    "NEGATIVE: a tray after shot 2, a pair that never separates, three cups, a pause before the snap, a clean silver side, a "
    "message on the foil, hands swapped, " + LIVE_NEG_SPINE,
    "[ORDER: 6 shots, 5 hard cuts, 17s — (1, 0–3s) inside the fridge; (2, 3–6s) medium shot, tray in his right hand; (3, 6–9s) "
    "probe macro, no pause, snap at 8s; (4, 9–11s) slight high angle, one cup set on the counter; (5, 11–13s) macro, the "
    "fingertip lifts the foil, silver side coated in yogurt; (6, 13–17s) he licks the foil, hard end mid-lick. Invariants: tray "
    "only in shots 1–2; tray and foil in the right hand, cup in the left; fingertip only; no text; fridge and counter "
    "frame-left, window frame-right; alone and silent. Look: 35mm negative, summer window light. NO music. NO text.]",
)

# ===========================================================================
# 2a — Mergulho (4 s)
# ===========================================================================
P_2A = _join(
    "CONTRACT — Live-action photoreal commercial footage, 16:9, 4 seconds total, ONE continuous take, time-freeze: everything in "
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
    "BEAT 1 (0–1s) — MCU 47°, the frozen frame; the camera begins to drift forward.\n"
    "BEAT 2 (1–3s) — the camera arcs forward and down past his chest, 20 cm above his thumb, toward the open cup in his left "
    "hand; the rim grows in the lower right of the frame and the yogurt surface, glossy with one frozen swirl, fills the "
    "lens.\n"
    "BEAT 3 (3–4s) — the lens dives through the surface; the frame fills with soft, uniform strawberry-cream pink. Hard end on the "
    "uniform pink.",
    "ACTING — none: he is a frozen photograph. NOT: a blink, a breath, any micro-movement, a changing expression.",
    "CAMERA — an impossible camera, a slim probe lens gliding on a curve, TRAVELS in one smooth move, no zoom. OPTICS: 47° at the "
    "start narrowing to a macro close-focus at the end. FOCUS: on his face at first, then on the rim, then the surface. HORIZON: "
    "level at the start. NOT: handheld shake, orbit, whip, cuts, slow motion.",
    "GEOMETRY — the cup is in his LEFT hand at chest height, at the lower right of the frame; the camera starts 1.2 m from his "
    "face and ends inside the yogurt; the path is one curve down and to the right of the frame, passing 20 cm above his thumb.",
    "PHYSICS & MATERIAL — everything is frozen: the yogurt holds its swirl, the glasses hold their reflection, the light is "
    "unchanged; only the camera's own travel is real, smooth and weighted. OVER-REAL: the frozen glossy swirl, a faint pink "
    "smear on his lip, fine foil creases. If any surface looks clean, smooth, plastic, CGI or rendered — WRONG.",
    "LIGHT — continues the keyframe exactly: warm natural summer window light from FRAME-RIGHT, cool fridge light from FRAME-LEFT; "
    "inside the yogurt the light becomes soft, creamy and pink. The lit sides never flip.",
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
        "a man discovers that luck has found him.",
        "he never wins anything and it is exactly the day he did the ritual properly.",
        "own the win, now, in his whole body.",
        "nothing holds him back: the obstacle is that the joy is bigger than the kitchen.",
        "verify, then pure joy — a quick check that turns into joy with no pause between the two.",
        "— [0–1s] the last sweep of the lick, eyes half-closed — [1–2s] eyes snap open and search the foil — [2–3s] the "
        "discovery: the eyes widen and the smile arrives instantly — [3–6s] the right arm goes up with the foil, the body follows, "
        "he laughs without words.",
        "a sharp inhale at the discovery.",
        "a pause before the joy, speaking, shouting words, looking into the lens, a keychain.",
        direction="be as happy as a person can be, immediately.",
    ),
    "CAMERA — MCU, 47°, the camera about 20 cm above his eye line looking down a little (a slight high angle), 1.2 m from him, "
    "locked off exactly as the keyframe; STAYS PUT.\nOPTICS: 47°, no lens drift.\nFOCUS: on his face; the foil sharp when it "
    "rises.\nHORIZON: level.\nNOT: handheld shake, push-in, orbit, zoom, slow motion.",
    "GEOMETRY — he is centre, torso square to the camera; the open cup in his LEFT hand at chest height; his RIGHT arm rises on "
    "the frame-left side, the foil ending above the top of his head; the fridge and the counter at frame-left, "
    "soft behind him.",
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
    "LIGHT — STYLIZED STUDIO ILLUMINATION, soft and clear (KEY):\n"
    "SOURCE: one large soft key box that travels WITH the camera, high at FRAME-LEFT and slightly in front (~5600 K); a pale "
    "sky-blue bounce from FRAME-RIGHT, low (~7500 K); small warm bulbs (~2800 K) on the machines.\n"
    "REACH: the key lights the whole front plane evenly from the left; the back wall falls half a stop darker and a step "
    "cooler.\n"
    "EXPOSURE: exposed for the cows and the fruit on the belt; shadows are lifted pastel, never black; even exposure corner to "
    "corner.\n"
    "CONTINUITY: the lit side of every cow is FRAME-LEFT in every shot; it never flips as the camera moves.\n"
    "NOT: hard sun, black shadows, a second key, moody low-key, flat fog."
)

COW = (
    "THE ALEGRINHA — the matte vinyl dairy cow of @char_vaca-vinil (100% matches its reference): cream-white body, her RIGHT ear "
    "solid black (it sits on SCREEN-LEFT when she faces the camera) and her LEFT ear cream, small horns, small black dot eyes, a "
    "thin smile line that can widen to show a small red mouth, a pink belly patch, black patches on the flanks, black glove "
    "hands, black hooves, a thin cord with a golden bell; NO keyring, NO chain. She is always happy to be working: the smile "
    "varies in size, never sad, angry or blank. "
    "@char_alegrinha-looks shows the four outfits, one per hall: hairnet, white boots and pale-green apron (hall 1); white lab "
    "coat with a blank badge and white boots (hall 2); over-ear headphones (hall 3); cream painter's smock and a small beret "
    "between the horns (hall 4)."
)

TOON_SCOPE = (
    "REFERENCE SCOPE: @char_vaca-vinil and @char_alegrinha-looks supply the cow, her proportions, colours and outfits ONLY — IGNORE "
    "their grey backdrops and lighting. @loc_fabrica supplies layout, materials, props and colours ONLY — it is an isometric "
    "overview, so IGNORE its camera angle and use the side-on camera written below."
)

TOON_WORLD = (
    "WORLD — a tiny factory built to the scale of tiny cows: every step, rail, door and valve is sized for hooves and glove hands; "
    "nothing is made for humans and no human exists here. One continuous white belt runs FRAME-LEFT to FRAME-RIGHT through four "
    "connected halls divided by walls with arched openings that the belt passes through. All signs, screens, badges and crates "
    "are blank or carry only abstract icons: NO letters, NO numerals, NO logos."
)

TOON_SOUND_BASE = (
    "SOUND — SOFT CARTOON FOLEY ONLY: the belt's low hum, padded footsteps of vinyl hooves, the golden bells' soft ding (one "
    "note per weight shift), squeaky rubbery fruit, gentle machine puffs. " + MUSIC_BAN
)

TOON_NEG_SPINE = (
    "photoreal humans, live-action footage, any human hand, speech or lip-sync, cow mouths forming words, keyring or chain on any "
    "cow, wrong number of cows, merged or fused cows, extra legs, extra horns, swapped ear colours, ink outlines, 2D cel look, "
    "glossy candy plastic, chrome, hard black shadows, grunge, dirt, film grain, vignette, camera shake, drone, canted horizon, "
    "readable text, letters, numerals, logos, watermark, subtitles, captions, music, score, wrong aspect ratio."
)


def toon_contract(secs, shots):
    return (
        "CONTRACT — 3D animated footage, miniature designer-toy diorama, 16:9, %d seconds total, %s, real-time animation at 24 fps "
        "with light squash and stretch. No speech, no lip-sync, no voice-over (a voice-over is added in post). NO music, NO "
        "score, NO subtitles, NO on-screen text of any kind: no letters, no numerals, no logos." % (secs, shots)
    )


TOON_CAMERA_TRAVEL = (
    "CAMERA — a miniature-diorama rail parallel to the production belt, perfectly planimetric (the lens axis stays perpendicular "
    "to the back wall; no yaw, no roll, no tilt).\n"
    "MOVEMENT: the camera TRAVELS FRAME-LEFT to FRAME-RIGHT at a constant calm speed of about one cow-length per second, never "
    "stops, never reverses, never cuts. One movement only.\n"
    "OPTICS: 47°, lens at 1 cow-height above the floor, 8 cow-heights from the back wall, the belt in the lower third of the "
    "frame at all times; a thin plane of sharp focus riding on the cows; no lens drift.\n"
    "HORIZON: level.\n"
    "NOT: handheld shake, drone, orbit, push-in zoom, canted horizon, whip pan, reversing, speed ramps."
)

_OPEN_A = (
    "BEAT 1 (0–2s) — the first frame is the approved last frame of the previous shot: the lens is covered in thick pink yogurt. "
    "A cow in a white hairnet, VERY close to the camera (her face fills the lower half of the frame), wipes the lens with a "
    "white cloth in two quick strokes; the yogurt goes onto the cloth and the glass is left clean. She steps out of frame "
    "toward frame-left; the factory appears behind her and the travelling is already moving."
)
_OPEN_B = (
    "BEAT 1 (0–2s) — the first frame is the approved last frame of the previous shot: the lens is covered in thick pink yogurt. "
    "With nobody in front of the camera, the yogurt slides down the glass like a thick gel and runs off the bottom edge, leaving "
    "a perfectly clean lens; the factory appears from the top down and the travelling is already moving."
)


def _spine(opening, name):
    return _join(
        toon_contract(30, "ONE continuous take with no cuts, a side-on travelling shot"),
        "REFERENCES — each reference has ONE job:\n"
        "[first frame] KEYFRAME: the take STARTS from this exact frame (the lens covered in pink yogurt).\n"
        "@char_vaca-vinil — IDENTITY of the cow.\n@char_alegrinha-looks — the cow's four outfits, one per hall.\n"
        "@loc_fabrica — WORLD: the factory's layout, materials and props.\n" + TOON_SCOPE,
        "WHO IS WHO — READ FIRST, ABSOLUTE:\n" + COW + "\n"
        "HALLS: hall 1 (fruit selection) three cows; hall 2 (pulp lab) three; hall 3 (sound studio) exactly TWO, one inside the "
        "glass booth and one outside at the audio desk; hall 4 (art studio) three. Each cow does ONE job, the one in the TIMELINE, "
        "and NEVER another.\n" +
        ("FACES: no cow looks into the lens (except the wiping cow in the opening, who looks at the glass); no cow speaks; no "
         "human exists.\nCONTACT: cows touch only fruit, tools and the cloth." if name == "A" else
         "FACES: no cow looks into the lens; no cow speaks; no human exists.\nCONTACT: cows touch only fruit and tools."),
        "SCENE & SOUL — SCENE: a long side-on travelling shot along a production line in a tiny green factory: fruit is selected, "
        "pressed into pulp, packed with a crisp créqui, and finally yogurt is painted onto foil. Already in progress at the first "
        "frame.\n"
        "THE SOUL OF THE SCENE (play it, never explain it): every cow takes her job as seriously as an Olympic athlete, a surgeon, "
        "an orchestra and an art critic, and she is delighted to do it.",
        "ABSOLUTE LOCKS — break one and the take is WRONG, regenerate:\n"
        "1. COW COUNTS: hall 1 three cows, hall 2 three, hall 3 exactly TWO, hall 4 three — WRONG if a count changes or two cows "
        "merge.\n"
        "2. THE CAMERA moves FRAME-LEFT to FRAME-RIGHT at a constant speed for all 30 seconds and NEVER cuts, stops or reverses; the "
        "belt stays in the lower third.\n"
        "3. HER RIGHT EAR IS THE BLACK ONE and there is NO keyring on any cow.\n"
        "4. EACH HALL KEEPS ITS OUTFIT: hairnet and apron, lab coat, headphones, painter's smock and beret.\n"
        "5. NO TEXT of any kind anywhere.",
        "TIMELINE — ONE continuous take, no cuts, already in progress at the first frame:\n" + opening + "\n"
        "BEAT 2 (2–7s) — HALL 1, fruit selection: three cows in hairnets, white boots and aprons, one at each of three small round "
        "tables behind the belt. COW A (left) turns a big strawberry in her gloves to inspect it and sets it on the belt; COW B "
        "(centre) holds up a bruised apple, judges it solemnly and drops it in a bin at the foot of her table; COW C (right) "
        "carries half a coconut onto the belt, leaning back for the weight.\n"
        "BEAT 3 (7–14s) — HALL 2, pulp lab: three cows in white lab coats. COW A throws a strawberry into the funnel of a pulp "
        "press; COW B holds a test tube against a strip of pink swatches to compare the colour; COW C presses a green button on a "
        "console and gives a thumbs-up. Thick pink pulp runs through glass tubes.\n"
        "BEAT 4 (14–21s) — HALL 3, sound studio: a glass acoustic booth holds the microphone; inside, COW A holds a pair of joined "
        "yogurt cups and snaps them in two with a crisp créqui, and the needle of a meter jumps. Outside the booth, COW B in "
        "over-ear headphones operates a cartoon audio desk, listening, her lips pursed in a satisfied pout as if mooing.\n"
        "BEAT 5 (21–30s) — HALL 4, art studio: three cows in painter's smocks and berets, each with a large flat sheet of soft "
        "aluminum foil on a small easel. COW A steps back to judge her work; COW B dips a brush into yogurt; COW C brushes yogurt "
        "onto the foil, plain, with no decoration. Hard end at 30s, wide, in the middle of the movement.",
        "ACTING — wide shot, every cow under 10% of the frame: one line of task each, played with total commitment; the work is "
        "the performance and the happiness shows in ears, head, bell and body, the smile varying in size.\n"
        "HALL 1: A inspects her strawberry like a jeweller (left ear flicks once when she approves); B judges the bruised apple "
        "like a magistrate and lets it drop into the bin (bell dings); C hauls the heavy coconut half onto the belt, leaning "
        "back with the weight.\n"
        "HALL 2: A feeds the press with a pitcher's wind-up and watches the strawberry fall; B squints, comparing tube and "
        "swatches (one ear tilts); C presses the green button with authority and her thumbs-up lasts half a second too long.\n"
        "HALL 3: A snaps the pair with total concentration (ears jump at the crack); B listens with closed eyes, then opens them "
        "on the meter with the pout of a satisfied moo.\n"
        "HALL 4: A steps back and judges like an art critic, head tilted; B loads her brush with care (bell sways); C paints one "
        "plain, confident stroke after another (tail tip curls).\n"
        "NOT: looking into the lens, mouths forming words, sadness, a blank face.",
        TOON_CAMERA_TRAVEL,
        "GEOMETRY — in each hall the cows stand behind the belt, about 2.5 cow-lengths apart, so all of a hall's cows are in frame "
        "together; the back wall is 8 cow-heights behind the belt; the arched openings between halls are about 1.6 cow-heights tall "
        "and the belt runs through them. Hall 3: the booth at frame-left of the hall, the audio desk at frame-right. Hall 4: the "
        "three easels in a row, COW A one cow-length behind the line.",
        "PHYSICS & MATERIAL — vinyl bodies have weight and a light squash on every landing; fruit is rubbery: the strawberry dents "
        "under a glove grip and recovers slowly, the apple bounces once in the bin, the coconut half is heavy and makes her lean "
        "back; the pink pulp is thick and slow in the glass tubes; yogurt is thick and glossy and clings to the brush; the foil is "
        "a thin soft sheet that flexes when brushed; " + ("the cloth in the opening is white and absorbent; " if name == "A" else
        "in the opening the yogurt on the lens is a thick gel that slides down the glass by itself and leaves it clean; ") +
        "the bells ding once per weight shift. Nothing floats, nothing loops. MATERIAL TRUTH of this world: matte vinyl with faint seam lines and soft "
        "fillets, a tiny glint on the golden bells, glossy pulp and yogurt, rubbery fruit with modelled seeds; pristine, never "
        "dirt.",
        TOON_LIGHT, TOON_LOOK, TOON_SOUND_BASE, TOON_WORLD,
        "NEGATIVE: a fourth cow in hall 3, a cut, a stop, the camera reversing, " + TOON_NEG_SPINE,
        "[ORDER: 1 continuous take, 30s, side-on travelling left to right — (0–2s) opening on the yogurt-covered lens; (2–7s) hall "
        "1; (7–14s) hall 2; (14–21s) hall 3; (21–30s) hall 4. Invariants: cow counts 3-3-2-3; constant direction and speed, no "
        "cuts; black right ear, no keyring; outfit per hall; no text. Look: matte vinyl, mostly monochromatic green, clean. NO "
        "music. NO text.]",
    )


P_3A_A = _spine(_OPEN_A, "A")
P_3A_B = _spine(_OPEN_B, "B")


def _insert(label, seconds, who, scene_soul, locks, shots, acting, geometry, physics, order, extra_neg=""):
    return _join(
        toon_contract(seconds, label),
        "REFERENCES — each reference has ONE job:\n@char_vaca-vinil — IDENTITY of the cow.\n@char_alegrinha-looks — the cow's outfit "
        "for this hall.\n@loc_fabrica — WORLD: the hall's layout, materials and props.\n" + TOON_SCOPE,
        "WHO IS WHO — READ FIRST, ABSOLUTE:\n" + COW + "\n" + who,
        scene_soul,
        "ABSOLUTE LOCKS — break one and the take is WRONG, regenerate:\n" + locks,
        "TIMELINE — hard cuts only at the specified seconds; the camera adds no cuts of its own:\n" + shots,
        acting,
        "CAMERA — locked off in each shot, STAYS PUT; the shot sizes and angles are stated per shot; no lens drift inside a shot; "
        "level horizon unless a shot says top-down. NOT: handheld shake, drone, orbit, whip pan, zoom.",
        geometry,
        physics,
        TOON_LIGHT, TOON_LOOK, TOON_SOUND_BASE, TOON_WORLD,
        "NEGATIVE: " + extra_neg + TOON_NEG_SPINE,
        order,
    )


P_3B = _insert(
    "2 shots with 1 hard cut at 4s", 8,
    "HALL 1 outfit: a white hairnet with the horns poking through, white rubber boots and a pale-green apron.",
    "SCENE & SOUL — SCENE: hall 1, fruit selection, seen from above and then up close. Already in progress.\n"
    "THE SOUL OF THE SCENE (play it, never explain it): each fruit is a small treasure and each cow its gatekeeper.",
    "1. SHOT 1 shows only gloves, fruit and the belt; SHOT 2 shows EXACTLY ONE cow — WRONG if more cows appear.\n"
    "2. The belt runs FRAME-LEFT to FRAME-RIGHT on screen in both shots, including the top view.\n"
    "3. Her RIGHT ear is the black one; NO keyring.\n4. NO text anywhere.\n5. Lit side FRAME-LEFT.",
    "SHOT 1 (0–4s) — straight-down top view, 63°: the white belt crosses the frame left to right with strawberries, apples and "
    "coconut halves riding on it, and black gloves pick them one by one; a bruised apple is lifted off the line.\n"
    "SHOT 2 (4–8s) — CU, 29°, side-on: a cow in a white hairnet and pale-green apron turns a big strawberry in her gloves to "
    "inspect it, her golden bell swinging, her happy face intent on the fruit. Hard end.",
    "ACTING — the cow in shot 2: TACTIC inspect like a jeweller; eyes on the fruit; detail: her left ear flicks once; the smile "
    "is wide and soft. The gloves in shot 1: quick, careful, never rough. NOT: looking into the lens, a blank face, sadness.",
    "GEOMETRY — shot 1: the belt crosses the frame at its vertical centre, 1.0 cow wide, with fruit spaced about one cow-length "
    "apart; shot 2: the cow centred at screen-left third, the strawberry at chest height held in both gloves.",
    "PHYSICS & MATERIAL — the strawberry is rubbery and dents under the glove grip, then recovers slowly; the apple lifts clean "
    "off the belt; the bell swings and dings once per turn. Nothing floats, nothing loops. MATERIAL TRUTH: matte vinyl, modelled "
    "seeds on the strawberry, soft fillets; never dirt.",
    "[ORDER: 2 shots, 1 hard cut, 8s — (1, 0–4s) top view of the belt and gloves; (2, 4–8s) CU of the strawberry inspection. "
    "Invariants: one cow in shot 2; belt left to right; black right ear; no text. NO music.]",
)

P_4B = _insert(
    "3 shots with 2 hard cuts at 3s and 6s", 9,
    "HALL 2 outfit: a white lab coat with a blank badge and white rubber boots.",
    "SCENE & SOUL — SCENE: hall 2, the pulp lab, in three details. Already in progress.\n"
    "THE SOUL OF THE SCENE (play it, never explain it): science, taken far too seriously and loved completely.",
    "1. SHOT 1 shows only the press and the tubes; SHOT 2 shows EXACTLY ONE cow; SHOT 3 shows only the nozzle and the pot — WRONG if "
    "more cows appear.\n2. The belt runs FRAME-LEFT to FRAME-RIGHT on screen in every shot.\n"
    "3. Her RIGHT ear is the black one; NO keyring.\n4. NO text anywhere.\n5. Lit side FRAME-LEFT.",
    "SHOT 1 (0–3s) — high angle, 63°: strawberries drop down the funnel of the pulp press and thick pink pulp runs through the "
    "glass tubes.\n"
    "SHOT 2 (3–6s) — CU, 29°, side-on: a cow in a white lab coat holds a test tube of pink pulp against a strip of pink swatches, "
    "her happy face intent.\n"
    "SHOT 3 (6–9s) — CU, 29°, side-on: a nozzle injects thick pink yogurt pulp into a small pot on the belt, filling it. Hard end.",
    "ACTING — the cow in shot 2: TACTIC compare, squinting; eyes alternating between the tube and the swatches; detail: one ear "
    "tilts; the smile is small and focused. NOT: looking into the lens, a blank face, sadness.",
    "GEOMETRY — shot 1: the funnel at the top centre, tubes running to frame-right; shot 2: the cow at screen-left third, the "
    "strip of swatches in her left glove, the tube in her right; shot 3: the nozzle above the belt at frame-centre, the pot "
    "beneath it.",
    "PHYSICS & MATERIAL — the pulp is thick and slow, it coats the glass and gathers in the pot; the strawberries tumble once and "
    "drop; the pot fills gradually (START empty, DURING rising pink, END full to the rim). Nothing floats, nothing loops. "
    "MATERIAL TRUTH: matte vinyl machines, glossy pulp, clear glass tubes; never dirt.",
    "[ORDER: 3 shots, 2 hard cuts, 9s — (1, 0–3s) press and tubes; (2, 3–6s) tube against swatches; (3, 6–9s) nozzle fills the "
    "pot. Invariants: one cow in shot 2; belt left to right; black right ear; no text. NO music.]",
)

P_5B = _insert(
    "2 shots with 1 hard cut at 4s", 8,
    "HALL 3: exactly TWO cows — COW A inside the glass acoustic booth, in plain cream vinyl, at the microphone; COW B outside the "
    "booth at the audio desk, wearing over-ear headphones. Each shot shows ONE of them.",
    "SCENE & SOUL — SCENE: hall 3, the sound studio, in two close-ups. Already in progress.\n"
    "THE SOUL OF THE SCENE (play it, never explain it): the créqui is music to the engineer's ears.",
    "1. EXACTLY TWO cows in this hall; each shot shows one — WRONG if a third appears.\n"
    "2. The pair of cups is TWO joined cups before the snap and TWO separate cups after.\n"
    "3. Her RIGHT ear is the black one; NO keyring.\n4. NO text anywhere; the audio desk is cartoon with a few simple sliders.\n"
    "5. Lit side FRAME-LEFT.",
    "SHOT 1 (0–4s) — CU, 29°, side-on, inside the glass acoustic booth: in front of a microphone with a round pop filter, COW A "
    "bends a pair of joined yogurt cups against their break line and snaps them apart with a crisp créqui; the needle on a meter "
    "jumps.\n"
    "SHOT 2 (4–8s) — CU, 29°, outside the booth: COW B in over-ear headphones at a cartoon audio desk with a few simple sliders "
    "listens, then makes a small satisfied pout with her lips as if mooing, her eyes closing happily. Hard end.",
    "ACTING — COW A: TACTIC snap the pair with total concentration; eyes on the cups; detail: her ears jump at the crack. COW B: "
    "TACTIC analyse the sound; eyes closed, then opening on the meter; detail: the pout of a satisfied moo. NOT: looking into "
    "the lens, mouths forming words, a blank face.",
    "GEOMETRY — shot 1: COW A at screen-centre, the microphone and pop filter between her and the camera's left, the glass wall "
    "behind her; shot 2: COW B at screen-right third, the desk's sliders in the lower third, the booth glass out of focus behind "
    "her at frame-left.",
    "PHYSICS & MATERIAL — the plastic break line resists, then gives with a sharp snap; no splinters; the cups stay sealed; the "
    "meter's needle jumps and settles with a small overshoot; the glass booth shows soft reflections. Nothing floats, nothing "
    "loops. MATERIAL TRUTH: matte vinyl, clear glass, soft acoustic foam; never dirt.",
    "[ORDER: 2 shots, 1 hard cut, 8s — (1, 0–4s) the cow in the booth snaps the pair; (2, 4–8s) the cow at the desk pouts like a "
    "satisfied moo. Invariants: exactly two cows; two cups then two; black right ear; no text. NO music.]",
    extra_neg="a third cow, a pair that never separates, three cups, ",
)

P_6B = _insert(
    "3 shots with 2 hard cuts at 3s and 6s", 9,
    "HALL 4 outfit: a cream painter's smock and a small beret between the horns. Three cows, one per easel; each shot shows one.",
    "SCENE & SOUL — SCENE: hall 4, the art studio, in three beats. Already in progress.\n"
    "THE SOUL OF THE SCENE (play it, never explain it): they paint yogurt onto foil with the gravity of old masters.",
    "1. THREE cows in this hall, one per easel; each shot shows one — WRONG if the count changes.\n"
    "2. The painting is PLAIN: simple yogurt strokes, NO decoration, NO drawing, NO letters.\n"
    "3. Her RIGHT ear is the black one; NO keyring.\n4. NO text anywhere.\n5. Lit side FRAME-LEFT.",
    "SHOT 1 (0–3s) — CU, 29°, side-on: COW C brushes yogurt onto a flat sheet of soft aluminum foil on her easel, simple "
    "strokes, no decoration.\n"
    "SHOT 2 (3–6s) — CU, 29°, side-on: COW B dips her brush into a cup of yogurt.\n"
    "SHOT 3 (6–9s) — over-the-shoulder, 47°, from just behind COW A, who has stepped back to judge her work: she makes a finger "
    "frame with her gloved fingers around the foil on the easel. Hard end.",
    "ACTING — COW C: TACTIC paint one plain, confident stroke after another; eyes on the foil; detail: the tip of her tail curls. "
    "COW B: TACTIC load the brush with care; eyes on the brush; detail: her bell sways. COW A: TACTIC judge like an art critic; "
    "eyes on the framed foil; detail: she tilts her head. NOT: looking into the lens, a blank face, decoration on the foil.",
    "GEOMETRY — shots 1 and 2: the cow at screen-centre, her easel at frame-right of her; shot 3: the camera 0.5 cow-lengths "
    "behind and to the left of COW A's shoulder, her finger frame at frame-centre, the foil on the easel sharp inside it, the "
    "easel about 2 cow-lengths away.",
    "PHYSICS & MATERIAL — the foil is a thin soft aluminum sheet that flexes slightly under the brush; the yogurt is thick and "
    "glossy, it drags and leaves a clean ridge; the brush dips and lifts with a thin string of yogurt; the gloves hold the "
    "brush firmly. Nothing floats, nothing loops. MATERIAL TRUTH: matte vinyl, glossy yogurt, soft foil; never dirt.",
    "[ORDER: 3 shots, 2 hard cuts, 9s — (1, 0–3s) brushing yogurt on the foil; (2, 3–6s) dipping the brush; (3, 6–9s) over the "
    "shoulder, finger frame. Invariants: three cows, one per shot; plain, no decoration; black right ear; no text. NO music.]",
    extra_neg="decoration or drawings on the foil, ",
)

# ===========================================================================
PROMPTS = {
    "1a": ("1a · POV da geladeira", 6, P_1A),
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
# 1d é uma alternativa a 1a+1b+1c (mesmos 17 s); fica fora de BASE_KEYS e ALT_KEYS para não somar duas vezes.
PROMPTS["1d"] = ("1d · Cena 1 inteira (alternativa a 1a+1b+1c)", 17, P_1D)

# Plano base: 3a conta uma vez (abertura A); a B só entra se for testada.
BASE_KEYS = ["1a", "1b", "1c", "2a", "3a-A", "3b", "4b", "5b", "6b", "7a"]
ALT_KEYS = ["3a-B"]

# Higgsfield (página oficial, verificada em 20/10/2026): 8 s = 128 (1080p), 56 (720p), 24 (480p).
# Por segundo (divisão minha): 16 e 3. O preço de finalizar um draft em 1080p não é publicado: assumo uma geração 1080p inteira.
CR_480 = 3
CR_1080 = 16
