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
    "SOURCE: warm daylight from the window side at FRAME-LEFT (~3800 K), with patches of sun on the green tile wall and on the "
    "frame-left side of his face; the open fridge's cool white light (~5000 K) from the fridge side at FRAME-RIGHT, only while "
    "the door is open in shot 1.\n"
    "EXPOSURE: exposed for his face and the foil; highlights roll off warm, shadows hold detail; the film look's gentle "
    "vignette and nothing more.\n"
    "CONTINUITY: warm daylight from frame-left in every shot; the lit sides never flip.\n"
    "NOT: flat even light, studio fill, a third source, neon, night, glow, haze."
)

LIVE_NEG_SPINE = (
    "smoke, vapour, mist, fog, steam, glassy stare, frozen pupils, doll eyes, warped hands, extra fingers, duplicated people, "
    "twins, a second person, speech or lip-sync, voice-over, readable text, invented logos, stiff or rigid foil, music, score, "
    "subtitles, handheld shake, gimbal wobble, drone, canted horizon, CGI-gloss look, HDR glow, cartoon look, wrong aspect "
    "ratio."
)

# Negativo extra para os planos de macro com sonda (o motor leu "84° / perspectiva exagerada" como olho de peixe)
MACRO_NEG = (
    "fisheye, circular black border, round lens mask, porthole vignette, black corners, barrel distortion, curved straight "
    "lines, "
)

MUSIC_BAN = (
    "ABSOLUTELY NO MUSIC of any kind: NO score, NO soundtrack, NO background music, NO BGM, NO jingle, NO beat, NO rhythm "
    "track, NO instrumental, NO melody, NO ambient pad, NO drone, NO chimes, NO musical stings. The audio is raw production "
    "sound only, like an unedited set recording. NO voice-over, NO narration, NO subtitles."
)

# Lente macro com sonda: Laowa 24mm f/14 2x Probe (24 mm, ~85° na diagonal = ~74° na horizontal em 16:9, ponta de 20 mm,
# foco a 2 cm, f/14 = foco profundo). Escrita como imagem retangular cheia, sem máscara circular.
MACRO_LENS = (
    "MACRO PROBE LENS (KEY — the look of a 24 mm probe/snorkel macro, as in a peek through flower stems or a mail slot): the "
    "lens tip sits down inside the scene at the level of the object, grazing along its surfaces. The nearest things are huge, "
    "soft and layered across the foreground like out-of-focus petals or a doorway frame, the subject is crisp on a thin plane "
    "of focus seen past or through them, and the room behind falls away into soft colour. Strong wide-angle perspective, lines "
    "converging toward the subject but straight, never bent. The camera moves in ONE continuous, fluid move, never slow motion, "
    "and nearby things sweep across the frame edges as soft blur: a tiny camera in a big world. Natural contrasty light with warm highlights glowing on shiny surfaces. The picture is a full, clean 16:9 "
    "rectangle edge to edge: NO fisheye bulge, NO circular black frame, NO round lens mask."
)

# Itens de porta de geladeira brasileira, sem rótulos
DOOR_ITEMS = (
    "the inside of the open door, at frame-left, shows its shelves with the usual Brazilian fridge-door items, all plain: a "
    "carton of eggs, a water bottle, a juice jug, a jar of preserves, a stick of butter in a dish — NO labels, NO brands, "
    "NO text on any of them"
)

# O que o motor mostra da cozinha real (@loc_cozinha) segundo o rascunho de 06/11/2026
KITCHEN_GEOMETRY = (
    "the green tile wall at FRAME-LEFT with patches of sun on it; the stainless fridge at FRAME-RIGHT behind him; the counter "
    "in front of him at lower frame-left; a dish rack and a window beyond the fridge, as in @loc_cozinha"
)


def live_contract(secs, shots, extra=""):
    return (
        "CONTRACT — Live-action photoreal raw camera footage with production sound only, 16:9, %d seconds total, %s, real-time motion. Dry comedy played "
        "completely straight. No dialogue and no voice-over (a voice-over is added in post)%s. ABSOLUTELY NO MUSIC, NO score, "
        "NO subtitles, NO on-screen text." % (secs, shots, extra)
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
    "face bare SILVER aluminum with a thick, generous layer of pink yogurt stuck to it, covering most of the silver in creamy, "
    "uneven smears with soft peaks and only a thin clean silver edge showing. It bends and crinkles, never stiff. There is NO "
    "tab and NO writing to read."
)
# O créqui: dobrar a dupla em direção ao centro, um polegar sobre cada copo
FOLD_TEXT = (
    "a thumb lying flat on the foil of each cup and his fingers under the cups, he folds the pair toward its centre: the "
    "thumbs press the outer halves down while the fingers push up under the joint, so the joint rises into a ridge and the "
    "two cup bottoms swing toward each other underneath, an upside-down V"
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
    who_man("opens the fridge and takes the tray, then takes a few steps with it; in shot 1 he looks at a fixed point inside the "
            "fridge, just beside the lens, and NEVER into the lens; in shot 2 he never looks at the camera"),
    "SCENE & SOUL — SCENE: a summer afternoon in a Brazilian kitchen with natural window light. He opens the fridge, takes a "
    "yogurt tray, shuts the door and walks a few casual steps with it, staying in frame. Already in progress at the first frame.\n"
    "THE SOUL OF THE SCENE (play it, never explain it): this is the most important small ritual of his day and nobody knows "
    "about it. He is absolutely serious, like a man collecting a trophy, and he never lets it be funny.",
    "THE TRAY — " + TRAY_TEXT,
    "ABSOLUTE LOCKS — break one and the take is WRONG, regenerate:\n"
    "1. THE TRAY is one block of exactly six joined cups with soft foil — WRONG if it is a pair, a single cup, stiff foil or "
    "any other count.\n"
    "2. In shot 2 the tray hangs in his RIGHT hand at hip height, carried level and normally by its edge, like groceries — "
    "WRONG if he holds it up, shows it to the camera or changes hands.\n"
    "3. Both shots are LOCKED OFF — WRONG if the camera moves, and WRONG if he looks into the lens.\n"
    "4. In shot 2 the fridge door is CLOSED; THE LIT SIDES NEVER FLIP: daylight from FRAME-LEFT, the fridge at FRAME-RIGHT.\n"
    "5. He is ALONE and SILENT — WRONG if a second person, speech or lip-sync appears.",
    "TIMELINE — 2 shots, 1 hard cut; cuts only at the specified points, the camera adds no cuts of its own:\n"
    "SHOT 1 (0–3s) — MCU, 84°, locked off INSIDE the fridge on the middle shelf, lens at shelf height, 0.7 m from the doorway, "
    "looking out. The fridge door is already opening, its edge sliding out past frame-left; " + DOOR_ITEMS + ". His face "
    "appears in the doorway, eyes fixed on a point inside the fridge just beside the lens; a slow smile arrives; at 2s his right "
    "hand rises from below frame and reaches in, fingers opening, until the hand fills the lens, so we do not see what he "
    "takes. HARD CUT.\n"
    "SHOT 2 (3–6s) — MS, 47°, locked off at chest height, 1.6 m from him. The fridge door is closed. He is already walking away "
    "from the fridge toward frame-left at an easy, casual pace, eyes ahead and never on the camera, the tray hanging from his "
    "right hand at hip height, level, the green foil on top and not turned to the lens. He takes a few unhurried steps along the "
    "counter and stays in frame the whole time. Hard end mid-stride, still in frame.",
    acting_man(
        "a man collects his small daily reward from the fridge and carries it off.",
        "it is the best part of his day, and it is only his.",
        "take it and carry it off, undisturbed.",
        "his own pleasure, which he must keep under control so it never shows too much.",
        "savour — he moves a half-beat slower than needed so the moment lasts, and lets the eyes carry it.",
        "— [0–1.5s] eyes settle on the point inside the fridge — [1.5–3s] the smile arrives late; the hand goes in before the "
        "smile is finished — [3–4.5s] he walks easily, eyes ahead, a faint private satisfaction — [4.5–6s] he keeps walking a few "
        "steps, still in frame, without looking back.",
        "his eyes narrow slightly against the fridge light.",
        "mugging, laughing, sitcom delight, looking into the lens, talking, presenting the tray.",
    ),
    "CAMERA — authored, designed camera, smooth. Both shots are locked off and STAY PUT: no movement at all.\n"
    "OPTICS: shot 1 at 84°, shot 2 at 47°; natural perspective, round bokeh; no lens drift inside a shot.\n"
    "FOCUS: shot 1 on his eyes with the shelf edge soft in the foreground; shot 2 on him as he walks.\n"
    "HORIZON: level.\n"
    "NOT: handheld shake, gimbal wobble, whip, orbit, push-in, pull-back, zoom, drone, canted horizon, slow motion.",
    "GEOMETRY — shot 2: " + KITCHEN_GEOMETRY + "; he starts at centre and walks to frame-left, away from the fridge, so the "
    "tray hangs from the hand on the camera-near side of his body. In shot 1 the camera sits where the tray was, 0.7 m from "
    "his face. The camera stays on the same side of the man–fridge line.",
    "PHYSICS & MATERIAL — the fridge door swings with weight and stops against its seal; the tray has the weight of six full "
    "cups and swings very slightly with his stride; the foil crinkles softly. Nothing floats, nothing loops. OVER-REAL: a "
    "light film of condensation on the cups, faint fold lines in the foil, the weave of his shirt, stubble and skin pores. If "
    "any surface looks clean, smooth, plastic, CGI or rendered — WRONG.",
    LIVE_LIGHT, LIVE_LOOK,
    "SOUND — DIEGETIC ONLY: the low hum of the fridge compressor; the soft thup of the door seal letting go in the first "
    "second; the faint crinkle of the foil; his footsteps and breath. " + MUSIC_BAN,
    LIVE_WORLD,
    "NEGATIVE: a pair or a single cup instead of the tray, him leaving the frame, the fridge door open in shot 2, the tray held up to the camera or "
    "with the green foil facing the lens, smoke or vapour from the fridge, any camera movement, him looking into the lens, the "
    "tray in his left hand, " + LIVE_NEG_SPINE,
    "[ORDER: 2 shots, 1 hard cut, 6s, both locked off — (1, 0–3s) from inside the fridge, door items visible, he smiles and his "
    "right hand covers the lens; (2, 3–6s) medium shot, fridge closed, he takes a few casual steps, staying in frame, with the "
    "tray hanging in his right hand, never looking at the camera. Invariants: one tray of six with soft foil; right hand, "
    "carried normally; daylight frame-left, fridge frame-right; alone and silent; never into the lens. Look: 35mm negative, "
    "summer window light. NO music. NO text.]",
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
    "THE SOUL OF THE SCENE (play it, never explain it): the snap is the sound he came for, and it takes him back to something "
    "long ago. He takes it in like a first bite and lets almost nothing show.",
    "THE PAIR — " + PAIR_TEXT,
    "ABSOLUTE LOCKS — break one and the take is WRONG, regenerate:\n"
    "1. NO TRAY anywhere in frame — WRONG if a tray appears.\n"
    "2. THE FOLD: a thumb flat on top of each cup, the pair folds toward its centre with the cup BOTTOMS swinging toward each other underneath, no pause — WRONG if he twists it, "
    "pulls it apart or pinches it from the sides.\n"
    "3. TWO joined cups before the snap and exactly TWO separate cups after; ONE cup stays in his LEFT hand and his RIGHT hand "
    "sets the other on the counter at lower frame-left.\n"
    "4. In shot 2 the camera is ABOVE his eye line looking down (no ceiling in frame) and his gaze lifts slightly UPWARD, "
    "never into the lens.\n"
    "5. He is ALONE and SILENT; the créqui is the only sound that matters.",
    "TIMELINE — 2 shots, 1 hard cut; cuts only at the specified points:\n"
    "SHOT 1 (0–3s) — extreme close-up with the probe macro lens described in CAMERA, from in front of him and above his "
    "hands: the first frame is 3 cm above the two foils, looking down at his two thumbs, one lying flat on the foil of each "
    "cup. ONE continuous, steady pull-back with a slight rise, no pause, through the whole shot, revealing the pair at chest "
    "height, his fingers under the cups and his shirt soft behind. His hands hold the pair: " + FOLD_TEXT + ". He is already "
    "folding, with no pause; at 2s the break line snaps with a crisp, bright crack (the créqui) and he draws the two cups "
    "apart, level, one in each hand, a small gap of air between them. HARD CUT.\n"
    "SHOT 2 (3–5s) — CU, 29°, the camera 25 cm ABOVE his eye line looking down at him (a slight high angle: his face with the "
    "tile wall behind, no ceiling in frame), 0.9 m from him. A half-beat after the crack his gaze lifts slightly upward and "
    "drifts toward the window light at frame-left, a faraway, nostalgic look with a small half-smile, never into the lens. One "
    "cup stays in his LEFT hand at chest height; his RIGHT hand sets the other on the counter at lower frame-left with a light "
    "knock, without looking at it. Hard end.",
    acting_man(
        "a man hears the exact sound he was waiting for, and it takes him back.",
        "the créqui is the reason this ritual exists; it sounds like his childhood.",
        "get the snap clean and take it in without anyone seeing how much it matters.",
        "his own emotion, which wants to show on the crack and which he keeps small.",
        "savour — no hesitation before the snap: he goes straight in, then lets the sound carry him somewhere else; the eyes do it.",
        "— [0–2s] the fold builds without a stop (macro, hands only) — [2s] the crack — [3–4s] his gaze lifts slightly upward "
        "and drifts toward the light, faraway, one corner of the mouth moves once — [4–5s] the gaze stays up while his right "
        "hand sets the cup down by feel.",
        "his shoulders drop a millimetre at the crack.",
        "sitcom delight, mugging, speaking, looking into the lens, looking down at the cup, a pause before the snap.",
    ),
    "CAMERA — Shot 1: the macro probe TRAVELS in one continuous, steady pull-back from the thumbs. Shot 2: locked off, STAYS PUT, "
    "slight high angle.\n"
    + MACRO_LENS + " Shot 2 is 29°; no lens drift inside a shot.\n"
    "FOCUS: shot 1 a thin plane of focus on the break line, the foreground thumbs and the kitchen softly out of focus; shot 2 on his eyes.\nHORIZON: level.\n"
    "NOT: handheld shake, orbit, zoom, drone, slow motion, fisheye, circular frame.",
    "GEOMETRY — " + KITCHEN_GEOMETRY + "; he stands at centre, torso square to the camera in shot 2, so his right hand is "
    "toward frame-left (the counter, the sunlit side) and his left hand toward frame-right (the fridge side). In shot 1 the "
    "pair is held at chest height, tilted toward the probe. The camera stays on the same side of him as in the previous shot.",
    "PHYSICS & MATERIAL — the plastic break line resists first, then gives all at once with a sharp snap; no splinters and no "
    "loose bits; both cups stay intact and sealed; the foil on each cup flexes and crinkles; a light film of condensation on the "
    "cups; the counter surface takes the cup with a small knock. Nothing floats, nothing loops. OVER-REAL: the thin ridge left "
    "where the break line parted, foil creases, fine hairs on his thumbs, the texture of the counter surface. If any surface "
    "looks clean, smooth, plastic, CGI or rendered — WRONG.",
    LIVE_LIGHT, LIVE_LOOK,
    "SOUND — DIEGETIC ONLY: the créqui, a short, crisp, bright plastic snap, loud and clean, the hero sound of the film; the soft "
    "crinkle of the foil; a light knock as the cup meets the counter; his breath. " + MUSIC_BAN,
    LIVE_WORLD,
    "NEGATIVE: " + MACRO_NEG + "a tray in frame, a pair twisted or pulled apart or pinched from the sides, a pair that never "
    "separates, three cups, a pause before the snap, the cup in the wrong hand, a low angle with the ceiling in frame, him "
    "looking into the lens, " + LIVE_NEG_SPINE,
    "[ORDER: 2 shots, 1 hard cut, 5s — (1, 0–3s) probe macro along the break line, thumbs on top of each cup folding the pair "
    "inward, no pause, the snap at 2s; (2, 3–5s) slight high angle, gaze lifting slightly upward, nostalgic, one cup in his left "
    "hand, the other set on the counter. Invariants: no tray; fold inward with a thumb on each cup; two joined, then two apart; "
    "left hand keeps one; full 16:9 frame, no fisheye; alone and silent. Look: 35mm negative, summer window light. NO music. "
    "NO text.]",
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
    "thick with yogurt on its silver side, and he licks it off. At the end the whole image freezes. Already in progress.\n"
    "THE SOUL OF THE SCENE (play it, never explain it): the foil is a treasure and the lick is a ceremony. He does it with "
    "complete reverence and complete seriousness.",
    "THE FOIL — " + FOIL_TEXT,
    "ABSOLUTE LOCKS — break one and the take is WRONG, regenerate:\n"
    "1. The cup is in his LEFT hand, the foil in his RIGHT hand.\n"
    "2. THE FOIL COMES AWAY WITH ITS SILVER SIDE THICKLY COATED IN PINK YOGURT, and that coat is what he licks — WRONG if the "
    "silver side comes away clean or only lightly smeared.\n"
    "3. THE FINGERTIP (the tip of the last phalanx of his right hand) lifts the foil's edge — WRONG if a fingernail, a tab or "
    "a tool is used; and shot 1 is ONE continuous forward move that follows the foil as it opens.\n"
    "4. NO readable text and NO message anywhere on the foil.\n"
    "5. THE LAST SECOND IS A TOTAL FREEZE: mid-lick, foil at his mouth, nothing moves until the clip ends; he is ALONE and "
    "SILENT.",
    "TIMELINE — 2 shots, 1 hard cut; cuts only at the specified points:\n"
    "SHOT 1 (0–2s) — extreme close-up with the probe macro lens described in CAMERA, from beside his face: his cheek and nose "
    "huge and soft in the foreground at one side of the frame, the lens looking past them at the cup he holds in his left "
    "hand close in front of his face, the green tile wall soft behind. ONE gentle, continuous push-in toward the cup, slightly "
    "downward, no pause: the fingertip of his right hand lifts the near edge of the foil and the foil hinges up on its far "
    "edge like a little door opening toward the lens, rising almost upright, so its bare silver underside, thickly coated "
    "with pink yogurt, turns to face the camera while the open cup and its pink yogurt surface appear below. HARD CUT.\n"
    "SHOT 2 (2–6s) — MCU, 47°, closer than before: 0.8 m from him, the camera diagonal to him, about 35° off his front toward "
    "his right side (the foil-hand side), 15 cm above his eye line looking down a little: a three-quarter, slightly high "
    "angle, locked off. The open cup in his left hand at chest height, the pink yogurt visible; the foil in his right hand, "
    "nearer the lens, its yogurt-coated silver side toward him and tilted so the pink coat catches the light. He looks at it "
    "with reverence, brings it to his mouth and licks the coat off with one slow sweep, a second sweep beginning. At 5s the "
    "image FREEZES mid-lick — foil at his mouth, eyes half-closed, cup in his left hand — and stays frozen, like a photograph, "
    "to the end of the clip.",
    acting_man(
        "a man opens his reward and gives the foil the honour it deserves.",
        "the lick is the first taste and he refuses to rush it.",
        "get every bit of yogurt off the foil.",
        "his hunger, which pushes him to hurry against his need for ceremony.",
        "treat the foil like a treasure — he handles it as if it could break, which it cannot.",
        "— [0–2s] eyes on the fingertip (macro, hands only) — [2–3s] eyes on the yogurt-coated silver, a long look — [3–4s] he "
        "lifts it, a small inhale — [4–5s] the lick: eyes close halfway — [5–6s] frozen mid-lick, nothing moves.",
        "a small inhale before the lick.",
        "mugging, speaking, looking into the lens, a fingernail or a tab, a message on the foil, a clean foil, any movement "
        "after the freeze.",
    ),
    "CAMERA — Shot 1: the macro probe TRAVELS in one gentle, continuous push-in toward the opening foil. Shot 2: locked "
    "off, STAYS PUT, three-quarter slightly high angle.\n"
    + MACRO_LENS + " Shot 2 is 47°; no lens drift inside a shot.\n"
    "FOCUS: shot 1 a thin plane of focus on the foil, the cup rim in the foreground and the kitchen softly out of focus; shot 2 on the foil and his lips, eyes just softer.\n"
    "HORIZON: level.\nNOT: handheld shake, orbit, zoom, drone, slow motion, fisheye, circular frame.",
    "GEOMETRY — in shot 2 " + KITCHEN_GEOMETRY + "; he faces the original camera position, so the lens, 35° to his right, "
    "sees his right cheek and the foil hand nearer; the open cup in his LEFT hand toward frame-right, the foil in his RIGHT "
    "hand rising to his mouth. The camera stays on the same side as in the previous shots.",
    "PHYSICS & MATERIAL — the foil lifts at one corner, bends, crinkles and comes away without tearing; the yogurt coat on its "
    "silver side is thick, creamy and clinging, with soft peaks, and does not drip; each lick wipes a clean silver stripe "
    "through the pink and leaves a slight smear at the corner of his lip; the yogurt in the cup is smooth and holds a soft "
    "swirl. Nothing floats, nothing loops. OVER-REAL: the creamy yogurt coat on bare silver, fine foil creases, the faint ring "
    "where the foil sealed the rim, skin pores, a trace of yogurt on his lip. If any surface looks clean, smooth, plastic, CGI "
    "or rendered — WRONG.",
    LIVE_LIGHT, LIVE_LOOK,
    "SOUND — DIEGETIC ONLY: the soft crinkle of the foil; a small wet lick; his breath; the room tone far behind; at the freeze "
    "the sound drops to near silence. " + MUSIC_BAN,
    LIVE_WORLD,
    "NEGATIVE: " + MACRO_NEG + "a fingernail, a pull tab, a message or any readable text on the foil, a clean or thinly smeared "
    "silver side, a cut inside shot 1, a straight-on or low angle in shot 2, any movement after the freeze, the cup in the "
    "right hand, " + LIVE_NEG_SPINE,
    "[ORDER: 2 shots, 1 hard cut, 6s — (1, 0–2s) one continuous forward macro move following the foil as the fingertip lifts "
    "it, the silver side thick with yogurt; (2, 2–6s) closer, three-quarter, slightly high angle, he licks the foil, FREEZE "
    "mid-lick from 5s to the end. Invariants: cup left hand, foil right hand; thick yogurt on the silver side; fingertip "
    "only; no tab, no text; full 16:9 frame, no fisheye; alone and silent. Look: 35mm negative, summer window light. NO "
    "music. NO text.]",
)

# ===========================================================================
# 1d — Cena 1 inteira (1a + 1b + 1c) numa geração só (17 s)
# ===========================================================================
P_1D = _join(
    live_contract(17, "6 shots with 5 hard cuts at 3s, 6s, 9s, 11s and 13s, locked-off cameras and two slow macro moves"),
    "REFERENCES — each reference has ONE job:\n"
    "@man-portoalegre — IDENTITY of the man. 100% matches.\n"
    "@loc_cozinha — WORLD: the kitchen's architecture and materials.\n"
    "@prop_bandeja-morango — OBJECT ONLY, shots 1–2: the six-cup tray and its green foil.\n"
    "@prop_pote-morango — OBJECT ONLY, shots 3–6: the yogurt cup and its green foil.\n" + LIVE_SCOPE,
    "WHO IS WHO — READ FIRST, ABSOLUTE:\n"
    "@man-portoalegre (round black glasses, dark curly hair, short beard, sage-green check short-sleeve shirt over a white "
    "T-shirt, thin silver bracelet on his LEFT wrist) — the MAN: takes the tray and walks a few steps with it, folds a pair to a crisp "
    "snap, keeps one cup, opens it and licks the yogurt off the foil; NEVER speaks, NEVER removes his glasses, NEVER looks into "
    "the lens (in shot 1 he looks at a point inside the fridge beside it). He is alone.",
    "SCENE — one uninterrupted ritual in a summer kitchen, in six shots: he takes a yogurt tray from the fridge and walks a "
    "few steps with it; a pair is broken off it off-camera between shots 2 and 3; he folds the pair to a crisp snap, keeps one cup, sets "
    "the other down, opens the cup and licks the foil, and the image freezes. Already in progress.\n"
    "THE SOUL OF THE SCENE (play it, never explain it): the most important small ritual of his day, and nobody knows. The snap "
    "takes him back; the foil is a treasure, the lick a ceremony. He is absolutely serious and never lets it be funny.",
    "THE PACK — shots 1–2: a tray of exactly SIX pink ribbed yogurt cups joined in one block; shot 3: a pair, exactly TWO "
    "joined by a thin plastic break line; shots 4–6: two separate cups. Every cup is sealed with FOIL: a thin, soft, flexible "
    "aluminum sheet, its outer face printed green (white shield logo, a strawberry), its inner face bare SILVER aluminum "
    "thickly covered with pink yogurt in creamy smears with soft peaks, only a thin clean silver edge showing. It bends and "
    "crinkles, never stiff; NO tab, NO writing.",
    "ABSOLUTE LOCKS — break one and the take is WRONG, regenerate:\n"
    "1. PACK: tray of six (shots 1–2), pair (shot 3), two separate cups (shots 4–6); NO tray in frame from shot 3. In shot 2 "
    "the fridge is CLOSED and the tray hangs normally in his RIGHT hand, never shown to the camera.\n"
    "2. THE FOLD: a thumb flat on top of each cup, the pair folds toward its centre with the cup BOTTOMS swinging toward each other underneath, no pause — WRONG if twisted, pulled "
    "apart or pinched. After the snap ONE cup stays in his LEFT hand and his RIGHT hand sets the other down; in shots 5–6 the "
    "cup is in his LEFT hand and the foil in his RIGHT.\n"
    "3. THE FOIL is lifted by the FINGERTIP in ONE continuous forward move and comes away with its SILVER SIDE THICKLY COATED "
    "IN PINK YOGURT, which he licks — WRONG with a nail, tab, clean silver or text.\n"
    "4. LIT SIDES NEVER FLIP: daylight FRAME-LEFT, fridge FRAME-RIGHT; every macro frame is a full 16:9 rectangle, NO circular "
    "black border; in shot 4 the camera is ABOVE his eye line.\n"
    "5. ALONE and SILENT; the last second is a TOTAL FREEZE mid-lick, foil at his mouth.",
    "TIMELINE — 6 shots, 5 hard cuts; cuts only at the specified points, the camera adds no cuts of its own:\n"
    "SHOT 1 (0–3s) — MCU, 84°, locked off INSIDE the fridge on the middle shelf, 0.7 m from the doorway. The door is already "
    "opening past frame-left; " + DOOR_ITEMS + ". His face appears, eyes on a point inside the fridge beside the lens; a slow "
    "smile arrives; at 2s his right hand reaches in and fills the lens. HARD CUT.\n"
    "SHOT 2 (3–6s) — MS, 47°, locked off at chest height, 1.6 m away. The fridge door is closed. He is already walking away from "
    "it toward frame-left at an easy, casual pace, eyes ahead, never on the camera, the tray hanging from his right hand at "
    "hip height, level, the foil on top and not turned to the lens; he takes a few unhurried steps and stays in frame. HARD CUT.\n"
    "SHOT 3 (6–9s) — extreme close-up with the probe macro lens described in CAMERA, from in front of him and above his "
    "hands: the first frame is 3 cm above the two foils, looking down at his two thumbs, one lying flat on the foil of each "
    "cup. ONE continuous, steady pull-back with a slight rise, no pause, through the whole shot, revealing the pair (broken off the tray off-camera) at chest "
    "height, his fingers under the cups and his shirt soft behind. His hands hold the pair: " + FOLD_TEXT + ". He is already "
    "folding, with no pause; at 8s the break line snaps with a crisp, bright crack (the créqui) and he draws the two cups "
    "apart, level, one in each hand, a small gap of air between them. HARD CUT.\n"
    "SHOT 4 (9–11s) — CU, 29°, the camera 25 cm ABOVE his eye line looking down at him (a slight high angle, tile wall behind, no "
    "ceiling in frame), 0.9 m away. A half-beat after the crack his gaze lifts slightly upward toward the daylight at "
    "frame-left, a faraway, nostalgic look with a small half-smile, never into the lens. One cup stays in his LEFT hand at "
    "chest height; his RIGHT hand sets the other on the counter at lower frame-left, without looking. HARD CUT.\n"
    "SHOT 5 (11–13s) — extreme close-up with the probe macro lens described in CAMERA, from beside his face: his cheek and nose "
    "huge and soft in the foreground at one side of the frame, the lens looking past them at the cup he holds in his left "
    "hand close in front of his face, the green tile wall soft behind. ONE gentle, continuous push-in toward the cup, slightly "
    "downward, no pause: the fingertip of his right hand lifts the near edge of the foil and the foil hinges up on its far "
    "edge like a little door opening toward the lens, rising almost upright, so its bare silver underside, thickly coated "
    "with pink yogurt, turns to face the camera while the open cup and its pink yogurt surface appear below. HARD CUT.\n"
    "SHOT 6 (13–17s) — MCU, 47°, 0.8 m away, the camera diagonal, about 35° off his front toward his right side (the foil-hand "
    "side), 15 cm above his eye line looking down a little: a three-quarter, slightly high angle, locked off. The open cup in "
    "his left hand at chest height; the foil in his right hand, nearer the lens, its yogurt-coated silver side toward him, "
    "tilted so the pink catches the light. He looks at it with reverence, brings it to his mouth and licks the coat off in one "
    "slow sweep, a second beginning. At 16s the image FREEZES mid-lick — foil at his mouth, eyes half-closed — and stays "
    "frozen, like a photograph, to the end of the clip.",
    acting_man(
        "a man performs his small daily ritual, from the fridge to the last lick.",
        "it is the best part of his day, and only his; the snap sounds like his childhood.",
        "take it, get the snap clean, get every bit of yogurt off the foil.",
        "his own pleasure, which wants to show and which he keeps small.",
        "savour — a half-beat slower at the fridge, no hesitation at the snap, reverence at the foil; the eyes carry everything.",
        "— [0–1.5s] eyes settle on the point in the fridge — [1.5–3s] the smile arrives late; the hand goes in before it is "
        "finished — [3–6s] he walks a few easy steps, eyes ahead, a faint private satisfaction — [6–8s] the fold builds without a "
        "stop (hands only) — [8s] the crack — [9–11s] his gaze lifts slightly upward toward the light, faraway; one corner of "
        "the mouth moves once; the gaze stays up while his hand sets the cup down by feel — [11–13s] hands only — [13–14s] eyes "
        "on the yogurt-coated silver, a long look — [14–15s] he lifts it, a small inhale — [15–16s] the lick: eyes close "
        "halfway — [16–17s] frozen.",
        "his eyes narrow slightly against the fridge light at the start; his shoulders drop a millimetre at the crack.",
        "mugging, laughing, sitcom delight, looking into the lens, talking, presenting the tray, a pause before the snap, any "
        "movement after the freeze.",
    ),
    "CAMERA — authored, designed camera. Shots 1, 2, 4 and 6 are locked off and STAY PUT, at 84°, 47°, 29° and 47°. Shot 3: "
    "the macro probe TRAVELS in one continuous, steady pull-back from the thumbs. Shot 5: the macro probe TRAVELS in one gentle, continuous push-in toward the opening foil.\n"
    + MACRO_LENS + "\nFOCUS: his eyes or the object of each shot; in the macro shots sharp at the tip, the kitchen softly out of "
    "focus behind. HORIZON: level.\n"
    "NOT: handheld shake, gimbal wobble, whip, orbit, zoom, drone, slow motion, fisheye, circular frame.",
    "GEOMETRY — " + KITCHEN_GEOMETRY + "; he stands at centre, torso square to the camera, so his right hand is toward "
    "frame-left (the counter, the sunlit side) and his left hand toward frame-right (the fridge side). The camera stays on the "
    "same side of the man–fridge line in every shot.",
    "PHYSICS & MATERIAL — the break line resists, then gives all at once with a sharp snap, no splinters; the foil lifts at one "
    "corner, bends and crinkles without tearing; the yogurt coat on the silver is thick, creamy and clinging, and does not "
    "drip; each lick wipes a clean silver stripe and leaves a slight smear at his lip. Nothing floats, nothing loops. "
    "OVER-REAL: a light film of condensation on the cups, the ridge where the break line parted, fine foil creases, creamy "
    "yogurt on bare silver, the weave of his shirt, stubble and skin pores. If any surface looks clean, smooth, plastic, CGI or "
    "rendered — WRONG.",
    LIVE_LIGHT, LIVE_LOOK,
    "SOUND — DIEGETIC ONLY: the fridge hum; the door seal's soft thup; his footsteps; the foil's crinkle; the créqui at 8s, a "
    "short, crisp, bright plastic snap, the hero sound of the film; a small wet lick; his breath; near silence at the freeze. "
    + MUSIC_BAN,
    LIVE_WORLD,
    "NEGATIVE: " + MACRO_NEG + "a tray after shot 2, him leaving the frame in shot 2, the fridge open in shot 2, the tray held up to the camera, a pair twisted "
    "or pulled apart, a pause before the snap, a low angle in shot 4, a clean silver side, any movement after the freeze, "
    "hands swapped, " + LIVE_NEG_SPINE,
    "[ORDER: 6 shots, 5 hard cuts, 17s — (1, 0–3s) inside the fridge, door items visible; (2, 3–6s) medium shot, fridge closed, "
    "he takes a few casual steps, staying in frame, with the tray hanging in his right hand; (3, 6–9s) probe macro, thumbs folding the pair inward, no "
    "pause, snap at 8s; (4, 9–11s) slight high angle, gaze lifted; (5, 11–13s) one continuous forward macro move, the foil "
    "comes away thick with yogurt; (6, 13–17s) closer, three-quarter, he licks the foil, FREEZE from 16s. Invariants: tray "
    "only in shots 1–2; right hand tray and foil, left hand cup; fingertip only; no text; full 16:9 macro frames, no fisheye; "
    "daylight frame-left, fridge frame-right; alone and silent. Look: 35mm negative, summer window light. NO music. NO text.]",
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
    "solid black (it sits on SCREEN-LEFT when she faces the camera) and her LEFT ear cream, small horns, small round black dot "
    "eyes, a wide happy smile line that can open to show a small red mouth, a pink belly patch, black patches on the flanks, "
    "black glove hands, black hooves, a thin cord with a golden bell; NO keyring, NO chain. HER FACE HAS NO EYEBROWS and NO brow "
    "line: only the dot eyes, the smile and the nostrils, so she can never look angry; she never frowns, scowls or squints in "
    "anger. She is always happy to be working. "
    "@char_alegrinha-looks shows the four outfits, one per hall: hairnet, white boots and pale-green apron (hall 1); white lab "
    "coat with a blank badge and white boots (hall 2); over-ear headphones (hall 3); cream painter's smock and a small beret "
    "between the horns (hall 4)."
)

# Estilo de atuação pedido pelo diretor: engraçadinhas e desastradinhas (sem citar personagem de marca no prompt)
COW_STYLE = (
    "ACTING STYLE (KEY): the cows are cute, eager little workers in a family animated comedy, a bit clumsy: they rush, "
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
    "WORLD — a tiny factory for tiny cows: steps, rails, doors and valves are sized for hooves and glove hands, but the machines, "
    "fruit and cups are big for them; nothing is made for humans and no human exists here. One continuous white belt runs "
    "FRAME-LEFT to FRAME-RIGHT through four connected halls divided by walls with arched openings that the belt passes through. "
    "Fruit rides the belt in hall 1; from hall 2 on, pink yogurt cups ride it. All signs, screens, badges and crates are blank "
    "or carry only abstract icons: NO letters, NO numerals, NO logos."
)

TOON_SOUND_BASE = (
    "SOUND — SOFT CARTOON FOLEY ONLY: the belt's low hum, padded footsteps of vinyl hooves, the golden bells' soft ding (one "
    "note per weight shift), squeaky rubbery fruit, gentle machine puffs, small happy grunts of effort (no words). " + MUSIC_BAN
)

TOON_NEG_SPINE = (
    "eyebrows, brow lines, frowning, angry or scowling faces, squinting, giant cows filling the frame, tiny props, normal-size "
    "fruit, photoreal humans, live-action footage, any human hand, speech or lip-sync, cow mouths forming words, keyring or "
    "chain on any cow, wrong number of cows, merged or fused cows, extra legs, extra horns, swapped ear colours, ink outlines, "
    "2D cel look, glossy candy plastic, chrome, hard black shadows, grunge, dirt, film grain, vignette, camera shake, drone, "
    "canted horizon, readable text, letters, numerals, logos, watermark, subtitles, captions, music, score, soundtrack, wrong "
    "aspect ratio."
)


def toon_contract(secs, shots):
    return (
        "CONTRACT — 3D animated footage, miniature designer-toy diorama, 16:9, %d seconds total, %s, real-time animation at 24 fps "
        "with light squash and stretch. No speech, no lip-sync, no voice-over (a voice-over is added in post). ABSOLUTELY NO "
        "MUSIC, NO score, NO subtitles, NO on-screen text of any kind: no letters, no numerals, no logos." % (secs, shots)
    )


TOON_CAMERA_TRAVEL = (
    "CAMERA — a miniature rail running just behind the near edge of the production belt, perfectly planimetric (the lens axis "
    "stays perpendicular to the back wall; no yaw, no roll, no tilt).\n"
    "MOVEMENT: the camera TRAVELS FRAME-LEFT to FRAME-RIGHT at a constant calm speed of about one cow-length per second, never "
    "stops, never reverses, never cuts. One movement only.\n"
    "OPTICS: WIDE, 63°, the lens low at belt height and close to the belt, so the belt is big in the immediate foreground across "
    "the bottom fifth of the frame, its rollers and rivets sliding past; the cows stand about 1.5 cow-lengths behind it, small, "
    "with tall wall above them; the dividing walls pass close to the lens as dark vertical wipes; a thin plane of sharp focus "
    "on the cows; no lens drift.\n"
    "HORIZON: level.\n"
    "NOT: close-ups, cows filling the frame, handheld shake, drone, orbit, push-in zoom, canted horizon, whip pan, reversing, "
    "speed ramps."
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
        COW_STYLE + "\n"
        "ACTING — wide shot, every cow about a quarter of the frame height: one line of task each, played with total, eager "
        "commitment; the happiness shows in ears, head, bell and body, the smile always wide.\n"
        "HALL 1: A — proud of a strawberry she can barely carry (the wobble, then the pat); B — panics for a second, saves the "
        "apple, beams; C — all-in shove, the near-slip, the thumbs-up.\n"
        "HALL 2: A — the tiptoe toss and the hop; B — the over-eager nod and the bell; C — the button, the startle, the clap.\n"
        "HALL 3: A — total concentration, then the flinch at her own snap, then the grin; B — bliss, the pout of a satisfied moo, "
        "the sway.\n"
        "HALL 4: A — the critic's step back and the bump; B — the pink glove and the shrug; C — the tongue of concentration.\n"
        "NOT: looking into the lens, mouths forming words, frowning, eyebrows, sadness, a blank face.",
        TOON_CAMERA_TRAVEL,
        "GEOMETRY — " + TOON_SCALE + " The belt crosses the immediate foreground across the bottom fifth of the frame; in each "
        "hall the cows stand about 1.5 cow-lengths behind it and about 2.5 cow-lengths apart, so all of a hall's cows are in "
        "frame together, small; the back wall is about 6 cow-heights behind the belt and rises to the top of the frame; the "
        "arched openings between halls are about 3 cow-heights tall and the belt runs through them. Hall 3: the booth at "
        "frame-left of the hall, the audio desk at frame-right. Hall 4: the three easels in a row, COW A one cow-length behind "
        "the line.",
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
        COW_STYLE + "\n" + acting,
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
    "ACTING — COW A: total concentration, then the flinch at her own snap, then the grin. COW B: bliss; detail: the sway lands "
    "on the beat of nothing. NOT: looking into the lens, mouths forming words, frowning, eyebrows, a blank face.",
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
