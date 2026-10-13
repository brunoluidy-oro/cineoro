# CODEMIG · VT 60" — templates congelados v1 (a testar).
# Todo prompt do shotlist cola estes blocos literalmente. Mudou aqui, muda em todos.

ACCENT_INTERIOR = (
    "light Minas Gerais interior accent: the R at the end of a syllable is a light retroflex "
    "'caipira' R, present but soft, never exaggerated, never a caricature; unhurried, slightly "
    "sing-song mineiro melody; word endings softened, every word still clear"
)
ACCENT_BH = (
    "Belo Horizonte accent: the R at the end of a syllable is a soft aspirated breath, almost an "
    "'h'; open, friendly urban mineiro melody; every word clear"
)

VOICE = {
    "JOVEM": "young man, 25, warm untrained baritone in the chest, a little grain, speaks low and "
             "close without projecting; " + ACCENT_INTERIOR + ". Never an announcer voice, never a "
             "radio voice, never a speech.",
    "ALUNO": "boy of 10, clear high child's voice, quick, a little breathy with eagerness; "
             + ACCENT_BH + ". Never an adult dubbing a child, never a cartoon voice.",
    "PROFESSORA": "woman, 40, mid register, a teacher's trained projection used gently, warm and "
                  "precise, each word placed; " + ACCENT_BH + ". Never stern, never an announcer.",
    "HOMEM_EV": "man, 40, relaxed baritone, conversational, a half-smile in the breath; "
                + ACCENT_BH + ". Never a salesman, never an announcer.",
    "OPERARIO": "man, 30, mid-low voice, a little hoarse from talking over machines, short "
                "phrases pushed slightly louder than normal; " + ACCENT_INTERIOR
                + ". Never an announcer.",
    "PESQUISADORA": "woman, 30, light mid voice, quick and exact, quiet, the voice of someone "
                    "mid-task; " + ACCENT_BH + ". Never breathy, never a TV presenter.",
    "DONO": "man, 60, deep, slow, slightly rough, the easy voice of a man who has talked across "
            "a counter for decades; " + ACCENT_INTERIOR + ". Never a caricature of a country man.",
    "AGRICULTORA": "woman, 40, mid-low, dry and steady, a walking breath under the words; "
                   + ACCENT_INTERIOR + ". Never an announcer, never a caricature.",
    "FUNCIONARIO": "man, 30, low, calm, unhurried, weighted pauses between phrases, chest voice; "
                   + ACCENT_INTERIOR + ". Never a dramatic narrator, never a movie-trailer voice.",
    "MOTORISTA": "man, 40, plain mid baritone, patient, the cadence of someone explaining a route; "
                 + ACCENT_BH + ". Never an announcer.",
    "ESTUDANTE": "teenage boy, 15, voice recently changed, light baritone that thins on the "
                 "stressed syllables, earnest; " + ACCENT_BH + ". Never a child's voice, never an "
                 "adult's.",
    "ENFERMEIRA": "woman, 30, soft mid voice, calm bedside cadence, low volume, every word clear; "
                  + ACCENT_BH + ". Never breathy, never a presenter.",
}


def voice_lock(tag):
    return (f"VOICE LOCK — @{tag}: {VOICE[tag]} This voice identity is fixed and identical in "
            "every generation of the film.")


TEXT_POLICY = ("NO subtitles, NO captions, NO on-screen text, NO logos, NO brand names on any "
               "surface")

MUSIC_POLICY = ("NO music, NO score, NO BGM, NO instrumental, NO melody, NO jingle, NO ambient pad, "
                "NO drone, NO swell, NO chimes — the soundtrack is added in post; this generation "
                "carries only location sound and the scripted voice.")

LANG = ("dialogue as spoken on-camera audio in Brazilian Portuguese with light Minas Gerais "
        "accents")

FILM_LOOK = """FILM LOOK (KEY — reproduce this exact photographic character): modern large-format cinema camera with spherical lenses; MID-KEY natural image — NOT underexposed, NOT dark, NO crushed blacks; colour muted and true: the red-ochre of Minas earth (soil, ore, brick, rust) is the warm constant of the film, greens and sky slightly desaturated, skin natural and varied, never teal-and-orange, never saturated; highlights roll off gently with subtle halation; shadows soft and readable; very fine organic grain; natural sharpness without edge enhancement; real skin with pores, marks and asymmetry; round soft bokeh; even exposure to all four corners, NO vignette. NOT a render, NOT HDR, NOT the glossy AI commercial look.
NO LENS FLARES: no flares, no light streaks, no sun stars, no floating bokeh orbs, no glow overlays; every light source stays small and contained."""

LIGHT_EXT = """LIGHT — NATURAL LIGHT ONLY, late afternoon, LOW & CLEAR (KEY):
SOURCE: the low sun ~4300 K from frame-LEFT, about 25° above the horizon and slightly in front of the subject; the open sky ~7000 K as the soft fill on the other side.
REACH: the sun lights the frame-LEFT side of every face and lays a warm edge along hair, shoulders and the crests of the terrain; the frame-RIGHT side of each face sits in soft open shade, readable.
EXPOSURE: exposed for skin; the sky holds tone, never blown white; shadows soft and readable; even exposure corner to corner, NO vignette.
CONTINUITY: the sun stays frame-LEFT for the whole generation; lit sides never flip.
NOT: golden-hour postcard glow, orange sky, sunbeams, sun disc in frame, reflector fill, flat overcast, midday top light."""


def light_int(window, practicals, reach):
    """Base interior: the fixed lines are verbatim; only the scene's source and reach change."""
    return f"""LIGHT — MOTIVATED LIGHT ONLY, daytime interior (KEY):
SOURCE: the key is daylight through {window} on frame-LEFT, ~5600 K, soft and directional; {practicals}
REACH: {reach}
EXPOSURE: exposed for skin; the room behind about one stop darker, readable, never black; shadows soft and readable; even exposure corner to corner, NO vignette.
CONTINUITY: the daylight stays frame-LEFT for the whole generation; lit sides never flip.
NOT: flat ceiling-panel light, frontal fill, beauty light, a blown-out window flooding the frame, green fluorescent cast."""


WORLD = """WORLD — Minas Gerais, Brazil, today: real places as they are used every day; materials and objects worn by use and with a function; uniforms, vehicles, machines and signage carry NO brand names, NO logos, NO company or government insignia and NO readable text (logos are added in post)."""

NEG_SPINE = ("glassy stare, frozen pupils, doll eyes, dead stare into the lens, warped hands, extra "
             "fingers, duplicated characters, twins, clones, looping motion, garbled text, readable "
             "signage, logos, brand names, watermark, subtitles, captions, music, score, jingle, "
             "beauty retouching, porcelain or waxy skin, glossy AI commercial look, HDR glow, lens "
             "flare, vignette, crushed blacks, golden-hour postcard, teal-and-orange grade, wrong "
             "aspect ratio")

# Câmera do revezamento (P1): travelling lateral constante, esquerda → direita.
def rev_camera(distance, size):
    return f"""CAMERA — observed handheld: the operator crab-walks sideways at an even slow walking pace (about 0.5 m per second) from frame-LEFT to frame-RIGHT, lens at shoulder height (1.5 m), {distance} from the subject, on the shadow side of the face.
MOVEMENT: the camera TRAVELS frame-left to frame-right at that same constant pace from the first frame to the last — it never stops, never reverses, never pushes in; small human footfall bounce, a late correction now and then.
OPTICS: {size} at 63°, natural perspective; no lens drift inside the take.
FOCUS: on the speaker's eyes; the background slides past, soft but readable.
HORIZON: level.
COMPOSITION: off-centre; the subject drifts from the right third toward the left third as the camera passes; the eyes stay on the upper-third line.
NOT: gimbal glide, dolly-smooth slide, drone, orbit, push-in, zoom, whip pan, the camera stopping, the camera reversing, centred symmetrical framing."""


# Quadro do match cut (P2): o levantar do olhar cai no mesmo ponto da tela.
MATCH_FRAME = """MATCH FRAME (KEY — identical in every shot of the match series): MCU at 29°, camera locked on a tripod or a fixed rig at the subject's eye height, 1.6 m from the face, frontal to the face; the face sits just left of centre; when the eyes rise and reach the lens they land on the upper-third line at about 45% of the frame width; the background soft at least 4 m behind."""
