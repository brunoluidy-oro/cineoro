"""Prompts de vídeo (Seedance 2.5, Higgsfield) para ALEGRINHA NA TAMPINHA, formato compacto CINEORO.

Os blocos repetidos são colados idênticos em cada prompt do seu mundo (cada geração é uma ilha: o motor
não tem memória). Regra do diretor: nunca "lid"/"cap"/"tampa": sempre FOIL, uma lâmina de alumínio maleável.
Os prompts são em inglês. PROMPTS[k] = (título, segundos da geração, texto); segundos = soma dos planos.
"""

# ---------------------------------------------------------------------------
# Blocos do mundo LIVE (captação)
# ---------------------------------------------------------------------------
LIVE_LOOK = (
    "FILM LOOK (KEY — reproduce this exact photographic character): 35mm color negative film look. Organic grain, fine to "
    "medium, alive in the shadows and midtones. Soft highlight roll-off with gentle warm halation blooming around windows, "
    "sunlit patches and bright skin edges; highlights creamy and warm, never pure white. Blacks slightly lifted and never "
    "crushed, shadows holding detail with a faint cool teal-green cast. Vintage spherical glass character: moderate "
    "micro-contrast, slight softness toward the frame edges, a gentle natural vignette darkening the corners, subtle "
    "chromatic fringing on high-contrast edges. Colour comes from the place itself — the real materials, surfaces and light "
    "of each location — never a grade laid over it; skin golden and natural with visible pores and texture. Photoreal "
    "live-action cinema, 16:9, real-time 24fps cadence with natural motion blur. NOT a render, NOT HDR, NOT the glossy AI "
    "commercial look."
)

MAN = (
    "@man-portoalegre (round black glasses, dark curly hair, short beard, sage-green check short-sleeve shirt over a white "
    "T-shirt, thin silver bracelet on his LEFT wrist), the only person in frame"
)
PACK = (
    "The pack is exactly TWO pink ribbed yogurt cups joined side by side by a break line, each sealed with FOIL: a thin, soft, "
    "flexible aluminum sheet printed in green that bends and crinkles, never stiff (@prop_pote-morango shows one cup)."
)
LIVE_LIGHT = (
    "LIGHT — warm natural summer window light from FRAME-RIGHT; the open fridge's cool light from FRAME-LEFT on his face. The "
    "lit sides never flip."
)
LIVE_NEG = (
    "NEGATIVE: glassy stare, warped hands, extra fingers, a second person, speech, voice-over, readable text, stiff foil, "
    "music, subtitles, handheld shake, CGI gloss, wrong aspect ratio."
)
LIVE_CONTRACT = (
    "CONTRACT — Live-action photoreal commercial footage, 16:9, %d seconds, %s. Dry comedy played straight. No dialogue, no "
    "voice-over. NO music, NO score, NO subtitles, NO on-screen text."
)

# ---------------------------------------------------------------------------
# Blocos do mundo TOON (fábrica)
# ---------------------------------------------------------------------------
TOON_LOOK = (
    "LOOK — premium 3D animation, a miniature designer-toy diorama: matte soft-touch vinyl world and characters, rounded "
    "bevels, no gloss; mostly monochromatic green with a white floor and belt; the cows and the fruit keep their own colours. "
    "Soft global illumination, lifted pastel shadows, a thin plane of sharp focus. Clean image: NO grain, NO vignette, NO lens "
    "flares."
)
TOON_LIGHT = "LIGHT — one big soft key travelling with the camera at FRAME-LEFT. The lit side never flips."
COW = (
    "COW — the matte vinyl cow of @char_vaca-vinil: cream body, her RIGHT ear black (screen-left when she faces the camera) and "
    "her left ear cream, small horns, dot eyes, a thin smile that can widen to show a small red mouth, pink belly patch, black "
    "flank patches, black glove hands and hooves, a golden bell on a cord, NO keyring. Always happy to be working, never sad "
    "or blank. Outfits per hall in @char_alegrinha-looks."
)
TOON_WORLD = (
    "WORLD — a tiny factory for tiny cows: one white belt running FRAME-LEFT to FRAME-RIGHT through four halls divided by walls "
    "with arched openings. @loc_fabrica gives layout and materials (ignore its isometric angle). NO text, letters or numerals "
    "anywhere."
)
TOON_SOUND = "SOUND — soft cartoon foley (belt hum, footsteps, bell dings, squeaky fruit). NO music, NO voice."
TOON_NEG = (
    "NEGATIVE: photoreal humans, human hands, speech, keyring, wrong cow count, merged cows, swapped ear colours, glossy "
    "plastic, hard shadows, film grain, camera shake, any text, music, wrong aspect ratio."
)
TOON_CONTRACT = (
    "CONTRACT — 3D animated footage, miniature designer-toy diorama, 16:9, %d seconds, %s. No speech, no lip-sync. NO music, "
    "NO subtitles, NO on-screen text."
)
TOON_CAMERA_TRAVEL = (
    "CAMERA — a side-on rail travelling parallel to the belt, 47°, lens at 1 cow-height, the belt in the lower third, moving "
    "FRAME-LEFT to FRAME-RIGHT at a constant calm speed (about one cow-length per second), no stops, no cuts."
)


def _join(*blocks):
    return "\n\n".join(b.strip() for b in blocks if b)


# ---------------------------------------------------------------------------
# CAPTAÇÃO
# ---------------------------------------------------------------------------
P_1A = _join(
    LIVE_CONTRACT % (6, "2 shots, 1 hard cut at 3s"),
    "REFERENCES — " + MAN + ". @loc_cozinha: the kitchen (ignore its camera angle).",
    "SCENE — Summer afternoon in a Brazilian kitchen. He opens the fridge, takes a pack of yogurt and steps into the light "
    "holding it, serious as a man in a ritual. Already in progress.",
    PACK,
    "LOCKS — 1. Exactly two joined cups with soft foil; WRONG if a tray of six or a rigid cover. 2. From second 3 the pack is "
    "in his RIGHT hand. 3. In shot 1 the camera is the fridge: he never looks into the lens, only at a point inside the fridge "
    "beside it. 4. Fridge at FRAME-LEFT in shot 2.",
    "TIMELINE —\n"
    "SHOT 1 (0–3s) — MCU, 84°, locked off inside the fridge at shelf height, 0.7 m from the doorway. The door is already "
    "swinging open, cool light on the lens. His face appears, eyes on a fixed point inside the fridge, a slow smile; at 2s his "
    "right hand reaches in and covers the lens, so we do not see what he takes. HARD CUT.\n"
    "SHOT 2 (3–6s) — starts CU, 29°, tight on the pack leaving the fridge in his right hand; the camera pulls straight back 1.2 "
    "m, smooth, to MS 47°, revealing him at the open fridge, pack at chest height, deadpan. Hard end.",
    "CAMERA — shot 1 stays put; shot 2 travels back in one smooth move. Level horizon. NOT: handheld shake, orbit, zoom.",
    LIVE_LIGHT, LIVE_LOOK,
    "SOUND — fridge hum, the door seal's soft thup, the crinkle of the foil. NO music, NO voice.",
    LIVE_NEG,
)

P_1B = _join(
    LIVE_CONTRACT % (5, "2 shots, 1 hard cut at 3s"),
    "REFERENCES — " + MAN + ". @loc_cozinha: the kitchen.",
    "SCENE — The same kitchen and light. He splits the two-cup pack with a crisp snap. Already in progress.",
    PACK,
    "LOCKS — 1. Two joined cups before the snap, exactly two separate cups after; WRONG if it stays joined or becomes three. "
    "2. After the snap one cup in his LEFT hand, the other set on the counter at FRAME-RIGHT. 3. Foil stays on, soft.",
    "TIMELINE —\n"
    "SHOT 1 (0–3s) — extreme close-up, slim probe macro lens, about 84° of exaggerated perspective, 2 cm from the pack, gliding "
    "slowly along the break line between the cups. Two fingertips pinch the cups. A short beat of stillness. At 2s he bends the "
    "pack against the break line and it snaps with a crisp, bright crack (the créqui): two separate cups. HARD CUT.\n"
    "SHOT 2 (3–5s) — CU, 29°, camera slightly above his eye line looking down a little (slight high angle): eyes half-closed, a "
    "contained pleasure, a tiny shiver. He keeps one cup in his left hand and sets the other on the counter. Hard end.",
    "CAMERA — shot 1 glides along the break line; shot 2 stays put. NOT: handheld shake, orbit, zoom.",
    LIVE_LIGHT, LIVE_LOOK,
    "SOUND — the créqui, a short crisp plastic snap, the hero sound; the foil's crinkle. NO music, NO voice.",
    LIVE_NEG,
)

P_1C = _join(
    LIVE_CONTRACT % (6, "2 shots, 1 hard cut at 2s"),
    "REFERENCES — " + MAN + ". @loc_cozinha: the kitchen. @prop_pote-morango: the cup with its green foil.",
    "SCENE — The same kitchen and light. He opens the single cup in his left hand and licks the yogurt off the foil. Already in "
    "progress.",
    "FOIL — a thin, soft, flexible aluminum sheet printed in green with a white shield logo and a strawberry; its inner side "
    "carries a film of pink yogurt. It bends and crinkles, never stiff. NO tab, NO writing to read.",
    "LOCKS — 1. Cup in his LEFT hand, foil in his RIGHT hand. 2. The fingertip (the tip of the last phalanx) lifts the foil's "
    "edge and the foil comes away. 3. No readable text, no message.",
    "TIMELINE —\n"
    "SHOT 1 (0–2s) — extreme close-up, slim probe macro lens, about 84°, 2 cm from the cup's edge: the fingertip of his right "
    "hand lifts the edge of the foil and it comes away. HARD CUT.\n"
    "SHOT 2 (2–6s) — MCU, 47°, camera slightly above his eye line looking down a little (slight high angle), locked off. He "
    "looks at the foil with reverence, brings it to his mouth and licks the yogurt off its inside. Hard end mid-lick, foil at "
    "his mouth, eyes half-closed, open cup in his left hand at chest height: this frame becomes the freeze frame.",
    "CAMERA — both shots stay put. NOT: handheld shake, orbit, zoom.",
    LIVE_LIGHT, LIVE_LOOK,
    "SOUND — the foil's crinkle, a small wet lick, his breath. NO music, NO voice.",
    LIVE_NEG,
)

P_2A = _join(
    "CONTRACT — Live-action photoreal commercial footage, 16:9, 4 seconds, ONE continuous take, time-freeze: everything in the "
    "scene is motionless like a photograph and ONLY the camera moves. NO music, NO subtitles, NO on-screen text.",
    "REFERENCES — [first frame] KEYFRAME: the take STARTS from this exact frame (the man mid-lick, the foil at his mouth, the "
    "open cup in his left hand); light, grade and skin continue it exactly. @prop_pote-morango: the open cup.",
    "SCENE — The instant after the lick. Time stops. The camera, a slim probe lens, slides forward and down in one arc toward "
    "the cup and dives into the pink yogurt.",
    "LOCKS — 1. Nothing moves except the camera; WRONG if he blinks or breathes. 2. One smooth arc, no cuts. 3. The last frame "
    "is a uniform strawberry-cream pink filling the frame, with no cup, rim, highlight or edge.",
    "TIMELINE —\n"
    "BEAT 1 (0–1s) — MCU 47°, the frozen frame; the camera starts to drift forward.\n"
    "BEAT 2 (1–3s) — the camera arcs forward and down past his chest, 20 cm above his thumb, toward the open cup; the rim grows "
    "and the yogurt fills the frame.\n"
    "BEAT 3 (3–4s) — the lens dives through the surface; the frame fills with soft, uniform strawberry-cream pink. Hard end.",
    "CAMERA — an impossible camera on a curve, one smooth move, no zoom. NOT: handheld shake, cut.",
    LIVE_LOOK,
    "SOUND — near silence, a soft airy whoosh at 3s. NO music, NO voice.",
    "NEGATIVE: any movement in the man, blinking, yogurt ripple, cuts, readable text, music, handheld shake, wrong aspect ratio.",
)

P_7A = _join(
    LIVE_CONTRACT % (6, "ONE continuous take") + " A wordless laugh is allowed, no words.",
    "REFERENCES — [first frame] KEYFRAME: the take STARTS from this exact frame (the man mid-lick, the foil at his mouth, the "
    "open cup in his left hand); light, grade and skin continue it exactly. " + MAN + ". @loc_cozinha: the kitchen.",
    "SCENE — The freeze releases. He finishes the lick, checks the foil for leftover yogurt, sees that he has won and is "
    "instantly happy, with no pause. He celebrates by raising the foil with his arm.",
    "LOCKS — 1. The cup stays in his LEFT hand; the foil in his RIGHT hand, soft and crinkly. 2. NO pause between seeing it and "
    "being happy. 3. Nothing readable on the foil; no keychain, no other prop. 4. He is alone.",
    "TIMELINE — ONE continuous take:\n"
    "BEAT 1 (0–1s) — the lick ends, the foil leaves his mouth.\n"
    "BEAT 2 (1–2s) — he looks at the foil in his right hand to check for leftover yogurt; its inner side faces him, not the "
    "camera.\n"
    "BEAT 3 (2–3s) — he sees he has won and lights up at once.\n"
    "BEAT 4 (3–6s) — he celebrates, raising the foil high with his right arm, shaking it with joy, laughing without words. Hard "
    "end at the peak.",
    "CAMERA — MCU 47°, slightly above his eye line looking down a little (slight high angle), locked off exactly as the keyframe. "
    "NOT: handheld shake, push-in, orbit.",
    LIVE_LIGHT, LIVE_LOOK,
    "SOUND — the foil's crinkle, a small lick, his breath, a wordless laugh. NO music, NO speech.",
    LIVE_NEG,
)

# ---------------------------------------------------------------------------
# FÁBRICA
# ---------------------------------------------------------------------------
_OPEN_A = (
    "BEAT 1 (0–2s) — the first frame is the approved last frame of the previous shot: the lens is covered in thick pink "
    "yogurt. A cow in a hairnet, VERY close to the camera, wipes the lens with a white cloth in two quick strokes; the yogurt "
    "goes onto the cloth and the glass is clean. She steps out of frame; the factory appears and the travelling is already "
    "moving."
)
_OPEN_B = (
    "BEAT 1 (0–2s) — the first frame is the approved last frame of the previous shot: the lens is covered in thick pink "
    "yogurt. With nobody in front of the camera, the yogurt slides down the glass like a thick gel and runs off the bottom "
    "edge, leaving a perfectly clean lens; the factory appears from the top down and the travelling is already moving."
)


def _spine(opening):
    return _join(
        TOON_CONTRACT % (30, "ONE continuous take, no cuts, a side-on travelling shot"),
        "REFERENCES — [first frame] KEYFRAME: the take STARTS from this exact frame. @loc_fabrica, @char_alegrinha-looks, "
        "@char_vaca-vinil.",
        COW, TOON_WORLD,
        "LOCKS — 1. Cow counts: hall 1 three, hall 2 three, hall 3 exactly TWO, hall 4 three. 2. The camera moves FRAME-LEFT to "
        "FRAME-RIGHT at a constant speed for all 30s and never cuts. 3. Right ear black, no keyring. 4. Each hall keeps its "
        "outfit. 5. No text anywhere.",
        "TIMELINE — ONE continuous take, no cuts:\n" + opening + "\n"
        "BEAT 2 (2–7s) — hall 1, fruit selection: three cows in hairnets, white boots and aprons, one at each of three small "
        "round tables behind the belt. The left cow turns a big strawberry in her gloves and sets it on the belt; the middle cow "
        "holds up a bruised apple, judges it solemnly and drops it in a bin; the right cow carries half a coconut onto the belt, "
        "leaning back for the weight.\n"
        "BEAT 3 (7–14s) — hall 2, pulp lab: three cows in white lab coats. One throws a strawberry into the funnel of a pulp "
        "press; another holds a test tube against a strip of pink swatches; the third presses a green button on a console and "
        "gives a thumbs-up. Pink pulp runs through glass tubes.\n"
        "BEAT 4 (14–21s) — hall 3, sound studio: inside a glass acoustic booth with a microphone, a cow holds a pair of joined "
        "yogurt cups and snaps them in two with a crisp créqui; the needle of a meter jumps. Outside, a cow in headphones "
        "operates a cartoon audio desk, listening, lips pursed in a satisfied pout.\n"
        "BEAT 5 (21–30s) — hall 4, art studio: three cows in painter's smocks and berets, each with a large flat sheet of soft "
        "aluminum foil on a small easel. One steps back to judge her work, one dips a brush into yogurt, one brushes yogurt onto "
        "the foil, plain, no decoration. Hard end at 30s, wide, mid-movement.",
        TOON_CAMERA_TRAVEL,
        TOON_LIGHT, TOON_LOOK, TOON_SOUND, TOON_NEG,
        "[ORDER: 1 take, 30s, side-on travelling left to right — (0–2s) opening on the yogurt-covered lens; (2–7s) hall 1; "
        "(7–14s) hall 2; (14–21s) hall 3; (21–30s) hall 4. Cows 3-3-2-3; constant direction; no text. NO music.]",
    )


P_3A_A = _spine(_OPEN_A)
P_3A_B = _spine(_OPEN_B)


def _insert(label, seconds, shots, locks, order):
    return _join(
        TOON_CONTRACT % (seconds, label),
        "REFERENCES — @loc_fabrica, @char_alegrinha-looks, @char_vaca-vinil.",
        COW, TOON_WORLD,
        "LOCKS — " + locks + " The belt runs FRAME-LEFT to FRAME-RIGHT on screen in every shot. Right ear black, no keyring. No "
        "text anywhere.",
        "TIMELINE — hard cuts only at the specified seconds:\n" + shots,
        TOON_LIGHT, TOON_LOOK, TOON_SOUND, TOON_NEG,
        order,
    )


P_3B = _insert(
    "2 shots with 1 hard cut at 4s", 8,
    "SHOT 1 (0–4s) — straight-down top view, 63°, locked off: the white belt crossing the frame left to right with strawberries, "
    "apples and coconut halves, and black gloves picking them one by one; a bruised apple is lifted off the line.\n"
    "SHOT 2 (4–8s) — CU, 29°, side-on, locked off: a cow in a white hairnet and pale-green apron turns a big strawberry in her "
    "gloves to inspect it, the golden bell swinging, her happy face intent on the fruit. Hard end.",
    "Shot 1 shows only gloves, fruit and belt; shot 2 exactly one cow.",
    "[ORDER: 2 shots, 8s — (0–4s) top view of the belt and gloves; (4–8s) CU of the strawberry inspection. One cow in shot 2. NO "
    "music.]",
)
P_4B = _insert(
    "3 shots with 2 hard cuts at 3s and 6s", 9,
    "SHOT 1 (0–3s) — high angle, 63°, locked off: strawberries drop down the funnel of the pulp press and thick pink pulp runs "
    "through the glass tubes.\n"
    "SHOT 2 (3–6s) — CU, 29°, side-on: a cow in a white lab coat holds a test tube of pink pulp against a strip of pink swatches, "
    "her happy face intent.\n"
    "SHOT 3 (6–9s) — CU, 29°, side-on: a nozzle injects thick pink yogurt pulp into a small pot on the belt, filling it. Hard end.",
    "Shot 1 shows only the press and tubes; shot 2 exactly one cow; shot 3 only the nozzle and the pot.",
    "[ORDER: 3 shots, 9s — (0–3s) press and tubes; (3–6s) test tube against swatches; (6–9s) nozzle fills the pot. NO music.]",
)
P_5B = _insert(
    "2 shots with 1 hard cut at 4s", 8,
    "SHOT 1 (0–4s) — CU, 29°, side-on, inside the glass acoustic booth: in front of a microphone with a round pop filter, a cow "
    "bends a pair of joined yogurt cups against their break line and snaps them apart with a crisp créqui; the needle on a meter "
    "jumps.\n"
    "SHOT 2 (4–8s) — CU, 29°, outside the booth: a cow in over-ear headphones at a cartoon audio desk with a few simple sliders "
    "listens, then makes a small satisfied pout as if mooing, her eyes closing happily. Hard end.",
    "Exactly two cows in this hall: one in the booth, one at the desk; each shot shows one.",
    "[ORDER: 2 shots, 8s — (0–4s) the cow in the booth snaps the pair; (4–8s) the cow at the desk pouts like a satisfied moo. "
    "NO music.]",
)
P_6B = _insert(
    "3 shots with 2 hard cuts at 3s and 6s", 9,
    "SHOT 1 (0–3s) — CU, 29°, side-on: a cow in a painter's smock and beret brushes yogurt onto a flat sheet of soft aluminum "
    "foil on her easel, simple strokes, no decoration.\n"
    "SHOT 2 (3–6s) — CU, 29°, side-on: another cow dips her brush into a cup of yogurt.\n"
    "SHOT 3 (6–9s) — over-the-shoulder, 47°, from just behind the cow who stepped back to judge her work: she makes a finger "
    "frame with her gloved fingers around the foil on the easel. Hard end.",
    "Three cows in this hall, one per easel; each shot shows one.",
    "[ORDER: 3 shots, 9s — (0–3s) brushing yogurt on the foil; (3–6s) dipping the brush; (6–9s) over the shoulder, finger frame. "
    "Plain, no decoration. NO music.]",
)

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

# Plano base: 3a conta uma vez (abertura A); a B só entra se for testada.
BASE_KEYS = ["1a", "1b", "1c", "2a", "3a-A", "3b", "4b", "5b", "6b", "7a"]
ALT_KEYS = ["3a-B"]

# Higgsfield (página oficial, verificada em 20/10/2026): 8 s = 128 (1080p), 56 (720p), 24 (480p).
# Por segundo (divisão minha): 16 e 3. O preço de finalizar um draft em 1080p não é publicado: assumo uma geração 1080p inteira.
CR_480 = 3
CR_1080 = 16
