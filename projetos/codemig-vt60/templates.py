# CODEMIG · VT 60" — templates congelados v2 (a testar).
# Todo prompt do shotlist cola estes blocos literalmente. Mudou aqui, muda em todos.

ASPECT = "21:9"  # formato do filme (decidido); as character sheets ficam 16:9 (assets.py)

ACCENT_INTERIOR = "light Minas Gerais interior accent with a soft 'caipira' R, never a caricature"
ACCENT_BH = "Belo Horizonte accent with a soft aspirated R"

VOICE = {
    "JOVEM": "young Brazilian man, 25, warm baritone; " + ACCENT_INTERIOR,
    "ALUNO": "Brazilian boy, 10, clear bright child's voice; " + ACCENT_BH,
    "PROFESSORA": "Brazilian woman, the voice of the attached audio reference — its timbre, accent and manner (direct, clear, a little brisk)",
    "HOMEM_EV": "Brazilian man, 40, relaxed baritone; " + ACCENT_BH,
    "OPERARIO": "Brazilian man, 40, mid-low voice, slightly raised over the machines; " + ACCENT_INTERIOR,
    "PESQUISADORA": "Brazilian woman, 30, light quick mid voice; " + ACCENT_BH,
    "DONO": "Brazilian man, 60, deep easy voice; " + ACCENT_INTERIOR,
    "AGRICULTORA": "Brazilian woman, 40, steady mid-low voice; " + ACCENT_INTERIOR,
    "FUNCIONARIO": "Brazilian man, 30, low calm chest voice; " + ACCENT_INTERIOR,
    "MOTORISTA": "Brazilian man, 52, plain friendly baritone; " + ACCENT_BH,
    "ESTUDANTE": "Brazilian teenage boy, 15, light new baritone; " + ACCENT_BH,
    "ENFERMEIRA": "Brazilian woman, 42, soft calm mid voice; " + ACCENT_BH,
}


def voice_lock(tag):
    return f"VOICE LOCK — @{tag}: {VOICE[tag]}. Identical in every generation of the film."


TEXT_POLICY = ("NO subtitles, NO captions, NO on-screen text, NO logos, NO brand names on any "
               "surface")

MUSIC_POLICY = ("NO music, NO score, NO BGM, NO instrumental, NO melody, NO jingle, NO ambient pad, "
                "NO drone, NO swell, NO chimes — the soundtrack is added in post; this generation "
                "carries only location sound and the scripted voice.")

LANG = ("dialogue as spoken on-camera audio in Brazilian Portuguese with light Minas Gerais "
        "accents")

# Style ref do cliente (35mm color negative), sem o parágrafo de cor e sem "tactile surfaces":
# a cor vem do ambiente de cada cena.
FILM_LOOK = f"""FILM LOOK (KEY — reproduce this exact photographic character): 35mm color negative film look. Organic grain, fine to medium, alive in the shadows and midtones. Soft highlight roll-off with gentle warm halation blooming around windows, sunlit patches and bright skin edges; highlights creamy and warm, never pure white. Blacks slightly lifted and never crushed, shadows holding detail with a faint cool teal-green cast. Vintage spherical glass character: moderate micro-contrast, slight softness toward the frame edges, a gentle natural vignette darkening the corners, subtle chromatic fringing on high-contrast edges. Colour comes from the place itself — the real materials, surfaces and light of each location — never a grade laid over it; skin golden and natural with visible pores and texture. Photoreal live-action cinema, {ASPECT}, real-time 24fps cadence with natural motion blur. NOT a render, NOT HDR, NOT the glossy AI commercial look.
NO LENS FLARES: no flares, no light streaks, no sun stars, no floating bokeh orbs; the warm halation stays a soft bloom around the highlights."""

LIGHT_EXT = """LIGHT — NATURAL LIGHT ONLY, late afternoon (KEY): one dominant motivated natural source with real falloff and soft-edged shadows.
SOURCE: the low sun ~4300 K from frame-LEFT, about 25° above the horizon and slightly in front of the subject; the open sky as the soft fill on the other side.
REACH: the sun lights the frame-LEFT side of every face and lays a warm edge on hair and shoulders; the frame-RIGHT side of each face sits in soft open shade, readable.
EXPOSURE: exposed for skin; highlights creamy and warm, the sky holding tone; blacks slightly lifted; corners allowed to fall into shade.
CONTINUITY: the sun stays frame-LEFT in every shot; lit sides never flip.
NOT: orange postcard sky, sunbeams, sun disc in frame, reflector fill, flat overcast, midday top light."""


# Variante diurna (a pedido, T08): manhã clara, sol alto — sem cara de entardecer.
LIGHT_EXT_DAY = """LIGHT — NATURAL LIGHT ONLY, bright mid-morning (KEY): one dominant motivated natural source with real falloff and soft-edged shadows.
SOURCE: the sun ~5600 K from frame-LEFT, about 50° above the horizon, softened by a thin high veil of cloud; the blue sky with a few white clouds as the fill on the other side; the green leaves bounce a soft fill up under any hat brim.
REACH: the sun lights the frame-LEFT side of every face and shoulder with a clean, neutral-warm edge; the frame-RIGHT side of each face sits in soft open shade, readable; shadows short and soft.
EXPOSURE: exposed for skin; highlights creamy, the sky holding its blue; blacks slightly lifted; corners allowed to fall into shade.
CONTINUITY: the sun stays frame-LEFT in every shot; lit sides never flip.
NOT: golden hour, orange or pink sky, long shadows, sunset glow, a low sun, sunbeams, sun disc in frame, reflector fill, flat overcast, harsh noon top light that buries the eyes in hat shadow."""

# Contraluz do T09-B, SÓ no plano 1 (ele de costas). O plano 2 usa a mesma luz do T09-A (LIGHT_EXT).
LIGHT_EXT_BACK = """SHOT 1 — NATURAL BACKLIGHT, low late afternoon (this shot only): the low sun ~3800 K, about 8° above the horizon, directly behind the machine and the man and straight toward the lens; it rims his hard hat, shoulders and vest with a warm edge, glows in the drifting dust and stretches his shadow toward us; the sun itself half-hidden behind the machine's silhouette, only its glow and the flare showing — never a clipped white disc, never a sunburst."""

# FILM LOOK com UM flare, só no plano 1 do T09-B (a pedido). O resto do filme segue sem flares.
FILM_LOOK_FLARE = FILM_LOOK.split("NO LENS FLARES:")[0] + """LENS FLARE — SHOT 1 ONLY (a deliberate exception): the low sun behind the machine throws ONE soft warm flare across the lower half of the frame — a gentle veil, a faint horizontal streak, a few soft ghost circles — subtle, never a hard star. In shot 2 and everywhere else: no flares, no light streaks, no floating bokeh orbs; the warm halation stays a soft bloom around the highlights."""


# Luz artificial de interior (T15, a pedido): corredor de hospital moderno, claro, sem cara de lâmpada verde.
LIGHT_ARTIFICIAL = """LIGHT — MOTIVATED ARTIFICIAL LIGHT ONLY, bright modern interior (KEY): one dominant motivated source with real falloff and soft-edged shadows.
SOURCE: the long linear LED strips of the corridor ceiling, ~4200 K neutral-warm, soft-edged, the nearest strip above and slightly in front of her on frame-LEFT; soft bounce from the pale walls and the polished floor.
REACH: the ceiling light shapes her face softly with a gentle falloff toward frame-RIGHT, never flat; the pale walls and floor open the shadows; the corridor stays bright and falls off about one stop toward its far end.
EXPOSURE: exposed for skin; highlights creamy; blacks slightly lifted; the whites of the scrubs holding texture, never blown.
CONTINUITY: the key stays above-front on frame-LEFT in every shot; lit sides never flip.
NOT: green fluorescent cast, flat hard top light with dark eye sockets, a blue clinical tint, a dim or grim corridor, a blown-out window."""


def light_int(window, practicals, reach):
    """Base interior: the fixed lines are verbatim; only the scene's source and reach change."""
    return f"""LIGHT — MOTIVATED LIGHT ONLY, daytime interior (KEY): one dominant motivated natural source with real falloff and soft-edged shadows.
SOURCE: daylight through {window} on frame-LEFT, ~5600 K, soft and directional; {practicals}
REACH: {reach}
EXPOSURE: exposed for skin; highlights creamy and warm; blacks slightly lifted; the room behind about one stop darker; corners allowed to fall into shade.
CONTINUITY: the daylight stays frame-LEFT in every shot; lit sides never flip.
NOT: flat ceiling-panel light as the key, frontal fill, beauty light, a blown-out window flooding the frame, green fluorescent cast."""


WORLD = """WORLD — Minas Gerais, Brazil, today: a modern Brazilian state moving forward — contemporary architecture, new and well-kept public spaces, current equipment and technology, Brazilian people and Brazilian everyday details; nothing rustic, run-down, poor-looking, old-fashioned or colonial. Uniforms, vehicles, machines and signage carry NO brand names, NO logos, NO insignia and NO readable text (logos are added in post); screens are off or show only abstract shapes."""

NEG_SPINE = ("glassy stare, frozen pupils, doll eyes, dead stare into the lens, solemn faces, "
             "warped hands, extra fingers, duplicated characters, twins, clones, looping motion, "
             "locked-off tripod shot, static camera, gimbal glide, garbled text, readable signage, "
             "logos, brand names, watermark, subtitles, captions, music, score, jingle, rustic, "
             "run-down, colonial architecture, decay, grime, peeling paint, poverty, beauty "
             "retouching, porcelain or waxy skin, glossy AI commercial look, HDR glow, lens flare, "
             "crushed blacks, wrong aspect ratio")

SHARED_ACTING = ("SCENE DIRECTION (shared, unspoken): tell a friend some good news about your state — "
                 "happy and proud of what you are saying, a real smile that comes and goes; the lens "
                 "is that friend.")

EYES = "pupils search, settle and drift; blinks uneven; slight asymmetry."

# Câmera do revezamento (P1): travelling lateral constante, esquerda → direita, em TODOS os planos.
REV_CAMERA = """CAMERA — handheld in EVERY shot: the operator crab-walks sideways at an even slow walking pace from frame-LEFT to frame-RIGHT in every shot — the close-up inserts and the line shot alike — with human footfall bounce and late small corrections; the camera never stops, never reverses, never pushes in.
OPTICS: as stated per shot; no lens drift inside a shot.
FOCUS: on the hands and objects in the inserts; on the speaker's eyes in the line shot; backgrounds slide past soft.
HORIZON: level.
NOT: tripod, locked-off frame, gimbal glide, dolly-smooth slide, drone, orbit, push-in, zoom, the camera stopping or reversing."""


def handheld(extra=""):
    return f"""CAMERA — handheld in EVERY shot, an operator with a body: breathing, small weight shifts, late corrections; never locked, never still — in the close-ups it drifts and follows the hands, in the line shot it drifts slowly around the speaker.{extra}
OPTICS: as stated per shot; no lens drift inside a shot.
FOCUS: on the action in the close-ups; on the speaker's eyes in the line shot.
HORIZON: level.
NOT: tripod, locked-off frame, gimbal glide, dolly, drone, zoom."""


# Quadro do T09-A (nióbio): o close do pedido anterior, só para esse take.
NIOBIUM_FRAME = """NIOBIUM FRAME (KEY): CU at 29°, handheld held close and breathing at the subject's eye height, 1.2 m from the face, frontal; the face just left of centre; when the eyes reach the lens they land on the upper-third line at about 45% of the frame width; the background soft."""

# Quadro do match cut v2 (P2): MCU centralizado, reto pra câmera, mesma distância, dolly-out lento.
MATCH_FRAME = """MATCH FRAME (KEY — identical in every shot of the match series): medium close-up (head and shoulders) at 47°, the camera at the subject's eye height about 1.3 m from the face, straight to camera and frontal; the face dead centre, the eyes on the upper-third line looking into the lens; the background soft. Every shot of the series carries the same slow DOLLY-OUT (the camera moving back, no zoom)."""


def dolly_out(secs):
    """Dolly-out lento: só a câmera recua; a lente fica fixa (sem zoom). O quadro abre de MCU para médio."""
    end = round(1.3 + 0.25 * secs, 1)
    return f"""CAMERA — the DOLLY-OUT, slow, about {secs}s: the camera glides straight back along the lens axis, from about 1.3 m to about {end} m from the face at an even pace, the lens fixed at 47° — NO zoom, NO lens movement — so the framing opens gently from a medium close-up toward a medium shot, the face staying dead centre and the background growing wider behind it. A faint handheld breath rides on the move; the move never stops or reverses.
FOCUS: on the eyes throughout. HORIZON: level.
NOT: a zoom, a vertigo or dolly-zoom effect, a push-in, a locked frame, a handheld shake, an orbit, a gimbal glide, a drone."""


# NEGATIVE para os takes com dolly-out: a espinha sem a proibição do deslize suave.
NEG_DOLLY = NEG_SPINE.replace("gimbal glide, ", "")
