# CODEMIG · VT 60" — gerações (prompts CINEORO completos).
# Cada prompt é uma ilha: monta a espinha inteira e cola os templates de templates.py.

import templates as T

ANCH = {
    "JOVEM": "25, lean, sun-weathered brown skin, short dark curly hair, light stubble, a thin scar through the left eyebrow, faded rust-red cotton work shirt with the sleeves rolled to the forearm, khaki canvas trousers, dusty brown leather work boots",
    "ALUNO": "10, slim Black boy, short tight curls, round face, a small gap between his front teeth, plain white school T-shirt with no emblem",
    "PROFESSORA": "40, white woman, medium build, shoulder-length dark brown hair tied low, light freckles, dusty-rose cotton blouse with the sleeves pushed up, a chalk smudge on the right sleeve",
    "HOMEM_EV": "40, mixed-race brown man, stocky, short black hair greying at the temples, trimmed beard, untucked light-grey linen shirt, wedding ring on the left hand",
    "OPERARIO": "30, Black man, broad shoulders, short beard, white hard hat with no logo, clear safety glasses, orange ear muffs around his neck, dark grey flame-retardant coverall with reflective strips, leather gloves",
    "PESQUISADORA": "30, Black woman, slim, natural hair in a tight bun, small gold stud earrings, buttoned white lab coat, purple nitrile gloves, clear safety glasses",
    "DONO": "60, white man, heavyset, sun-reddened skin, thick white moustache, balding with white hair at the sides, brown-and-cream checked short-sleeved shirt, canvas apron, a small old burn mark on the back of his left hand",
    "AGRICULTORA": "40, mixed-race brown woman, strong build, sun lines at the eyes, long black hair in a single braid, wide-brim straw hat pushed back off the forehead, long-sleeved khaki field shirt, jeans, leather boots",
    "FUNCIONARIO": "30, mixed-race brown man, medium build, short black hair, a moustache, white hard hat with chin strap and no logo, clear safety glasses, orange high-visibility reflective vest over a long-sleeved grey work shirt, leather gloves, ear plugs on a cord around his neck, fine ore dust on everything",
    "MOTORISTA": "40, Black man, solid build, close-cropped greying hair, round face, pale grey short-sleeved uniform shirt with no insignia, a steel wristwatch on the left wrist",
    "ESTUDANTE": "15, mixed-race brown teenage boy, thin and tall for his age, short hair faded at the sides, a faint teenage moustache, charcoal-grey hoodie over a white T-shirt, black jeans, worn white sneakers, dark backpack",
    "ENFERMEIRA": "30, mixed-race brown woman, medium build, dark hair in a low bun, a small mole above the upper lip, white scrubs, a stethoscope around her neck",
}

SCOPE_ID = ("REFERENCE SCOPE: character references supply face, build, hands and wardrobe ONLY — "
            "IGNORE their grey backdrop, studio lighting, exposure and colour grade.")

DLG = ("DIALOGUE — only these lines are spoken, each by the named character; ON CAMERA lines are "
       "lip-synced, mouth movements match the sound exactly; NO dubbing, NO voice-over, NO "
       "narration, NO subtitles — the words exist only as sound. Every mouth not speaking stays "
       "closed.")

EYES = ("pupils move with the task — search, settle, drift, settle again; blinks uneven and a beat "
        "late; brows, cheeks and mouth work independently, slight asymmetry.")

DIRECT = ("SCENE DIRECTION (shared, unspoken): tell a fellow mineiro, eye to eye, something you are "
          "proud of — the lens is that person.")

LOCKS_HEAD = "ABSOLUTE LOCKS — break one and the take is WRONG, regenerate:"


def contract(seconds, takes, camera, dialogue=True, extra=""):
    lang = T.LANG if dialogue else "no dialogue — no one speaks"
    return (f"CONTRACT — Live-action photoreal film footage, 16:9, {seconds} seconds total, {takes}, "
            f"{camera}, real-time motion{extra}, {lang}. NO music, NO score. {T.TEXT_POLICY}.")


def card(task, dur, attach, notes):
    lines = [
        "GENERATION CARD",
        f"Modelo: Seedance 2.5 (Higgsfield) · Tarefa: {task}",
        f"Duração: {dur}s (= timeline) · Aspecto: 16:9 · Resolução: draft 480p → final 1080p · Áudio: on",
        "Anexar nesta ordem:",
    ]
    lines += [f"  {i}) {a}" for i, a in enumerate(attach, 1)]
    lines.append(f"Notas: {notes}")
    return "\n".join(lines)


def join(*blocks):
    return "\n\n".join(b.strip() for b in blocks if b)


# ---------------------------------------------------------------- T01
T01 = join(
    contract(8, "ONE continuous take, no cuts", "an authored composed frame with ONE slow deliberate dolly move"),
    f"""REFERENCES — each reference has ONE job:
@JOVEM — IDENTITY of @JOVEM: face, hair, build, hands and wardrobe. 100% matches.
@PICO — WORLD: the summit — exposed grey rock with ochre lichen, patches of red earth, low dry grass, the layered sea of hills beyond; the world for the whole take.
{SCOPE_ID} @PICO supplies geography and materials ONLY — its light is replaced by the LIGHT block.""",
    f"""WHO IS WHO — READ FIRST, ABSOLUTE:
@JOVEM ({ANCH['JOVEM']}) — the PROTAGONIST: stands, looks, turns, speaks once; NEVER walks, NEVER raises his arms, NEVER smiles broadly; owns the frame-LEFT third.
FACES: his face exists once; nobody else in the frame.""",
    """SCENE — Late afternoon on a rock summit in Minas Gerais. @JOVEM is already standing near the edge with his back to the camera, looking over a sea of hills that runs in layers to the horizon; the wind moves the grass.
THE SOUL OF THE SCENE (play it, never explain it): he climbed up here to confirm something he already knows about where he comes from — and then he tells you, one local to another, not as a speech.""",
    f"""{LOCKS_HEAD}
1. ONE continuous take with ONE slow forward dolly move, no cuts — WRONG if the camera cuts, orbits or rises like a drone.
2. @JOVEM is in frame from the first frame, at the frame-LEFT third, standing still on the rock — WRONG if the first frame is empty or he walks.
3. After the turn his eyes find the lens and stay there, alive — WRONG if the stare is glassy or he looks past the camera.
4. The sun stays frame-LEFT and lights the frame-LEFT side of his face — WRONG if the light flips or comes from the front.
5. Only @JOVEM speaks, one line, in Brazilian Portuguese — NO music.""",
    """TIMELINE — ONE continuous take, no cuts, already in progress at the first frame:
BEAT 1 (0–3s) — WS from behind, 47°, camera at chest height 6 m behind him, already dollying forward, slow and steady: @JOVEM at the frame-LEFT third, back to camera, weight on his right leg, eyes travelling the horizon from frame-left to frame-right like someone checking an inheritance; the hills fill the right two-thirds of the frame in layers fading into haze.
BEAT 2 (3–4s) — he turns toward the camera over his left shoulder, head first and then the shoulders, unhurried, his boots re-planting on the rock; the dolly keeps coming.
BEAT 3 (4–7s) — the dolly arrives at a medium shot, waist up, @JOVEM still at the frame-LEFT third with the sea of hills behind him to frame-right; at 4–7s he speaks to the lens.
BEAT 4 (7–8s) — the dolly settles to a stop; he holds your eyes, mouth closed, waiting to see if it reached you. Hard end on the held look.""",
    f"""{DLG}
[4–7s] @JOVEM (on camera, Brazilian Portuguese, light Minas Gerais interior accent, low and close, not projected, a small breath before the last word): "Em Minas, terra não é só terra."
{T.voice_lock('JOVEM')}""",
    f"""ACTING — @JOVEM (fully invested in the tactic; the work happens in the eyes)
{DIRECT}
EVENT: a man shares what this ground means before anyone has asked.
MOTIVE: he grew up on this earth and has heard it treated as only dirt.
GOAL: that you see what he sees.
OBSTACLE: the moment it sounds like a speech, it is lost.
TACTIC: check the horizon like an inheritance, then turn and test you — say it plainly and watch whether it lands.
MOMENT TO MOMENT: — [0–3s] eyes travel the hills, settle on one far ridge, move on — [3–4s] the turn: his eyes reach the lens a beat after his head — [4–7s] the line to you, his eyes checking both of yours — [7–8s] he waits for your answer.
LIVING EYES: {EYES} Involuntary detail: the wind lifts his collar and he does not fix it. The low sun puts a small live point in his frame-left eye; a frozen pupil is wrong.
NOT: a heroic pose, open arms, a broad smile, a nod to the camera, narrating, squinting into the sun.""",
    """CAMERA — authored composition: a dolly on a short track laid over the rock, lens at chest height (1.4 m); the track runs parallel to his line of sight, offset 1.5 m to his right, so he holds the frame-LEFT third; it starts 6 m from him and ends 2.5 m from him.
MOVEMENT: the camera TRAVELS forward in one slow, constant dolly move from 0s to 7s, then settles; no other movement, no handheld shake.
OPTICS: 47° for the whole take; natural perspective; no zoom, no lens drift.
FOCUS: on @JOVEM throughout; the hills slightly soft but readable.
HORIZON: level.
COMPOSITION: off-centre — he holds the frame-LEFT third, the hills the right two-thirds; his eyes on the upper-third line after the turn.
NOT: drone, aerial, crane rise, orbit, zoom, gimbal float, handheld shake, centred symmetrical framing.""",
    """GEOMETRY — the rock edge runs left to right across the lower frame; @JOVEM stands 1 m back from it, facing the valley at the start and the camera after the turn; the camera at 1.4 m height on the track, offset 1.5 m to his right; the nearest ridge about 2 km away, the farthest dissolving into haze.""",
    """PHYSICS & MATERIAL — the wind blows steadily from frame-left, combing the dry grass in waves and pressing his shirt against his back; his weight shifts on the uneven rock and his boots grind grit when he turns; small puffs of red dust lift off the earth and drift right. Nothing floats, nothing loops. OVER-REAL: ochre lichen on the grey rock, red laterite earth packed in the cracks, dry seed heads of capim grass, a dried sweat line on his collar, dust on his boots, sun-cracked lips. If any surface looks clean, smooth, plastic, CGI or rendered — WRONG.""",
    T.LIGHT_EXT,
    T.FILM_LOOK,
    f"""SOUND — LOCATION SOUND ONLY: wind across the open summit, steady, one gust at 2s; dry grass hissing; his boots grinding grit on the turn; a hawk's call far off at 1s; his breath before the line; after the line, only the wind. {T.MUSIC_POLICY}""",
    T.WORLD,
    f"""NEGATIVE: empty first frame, @JOVEM walking, raised arms, broad smile, squinting, a second person, drone shot, aerial, orbit, crane rise, zoom, centred composition, sun disc in frame, sunbeams, light from the front, {T.NEG_SPINE}.""",
    """[ORDER: ONE continuous take, 8s, one slow forward dolly from WS to MS — (0–3s) his back to camera at the frame-LEFT third, eyes on the hills — (3–4s) he turns over his left shoulder — (4–7s) his line to the lens — (7–8s) the dolly settles, he holds your eyes. Invariants: one take, one dolly move; first frame occupied; eyes alive on the lens; sun frame-LEFT. Look: large-format spherical, mid-key, red-ochre earth, fine grain, no vignette. Only @JOVEM speaks, one line, Brazilian Portuguese. NO music. NO subtitles, NO text.]""",
)

# ---------------------------------------------------------------- T02-B1
T02B1 = join(
    contract(5, "ONE continuous take, no cuts", "an impossible camera that tilts down and then travels straight down through the ground, photographed like a real camera descending a freshly cut excavation wall", dialogue=False),
    f"""REFERENCES — each reference has ONE job:
@JOVEM — OBJECT ONLY: his dusty brown leather work boots and the hems of his khaki canvas trousers — nothing else of him appears.
@PICO — WORLD for the first second only: the red earth and dry grass of the summit floor.
{SCOPE_ID} @PICO supplies ground materials ONLY — its light is replaced by the LIGHT block.""",
    """WHO IS WHO — READ FIRST, ABSOLUTE:
@JOVEM — seen ONLY as his two boots planted on the red earth during 0–1s; his face, hands and body NEVER appear. Nobody else exists in this take.""",
    """SCENE — On the summit, the camera looks down at @JOVEM's boots on the red earth and then dives into the ground: grass roots, soil, rock layers and finally a dark seam of iron ore.
THE SOUL OF THE SCENE (play it, never explain it): what is under his feet is the beginning of everything that follows — earth becoming ore.""",
    f"""{LOCKS_HEAD}
1. ONE continuous downward movement, no cuts — WRONG if it cuts, reverses or rises.
2. The descent looks photographed, not animated: real soil, real rock, real roots — WRONG if it looks like a CGI render or a game cutaway.
3. The take ENDS on a frame almost completely filled with dark banded ore, the camera still descending — WRONG if it ends on anything else or on black.
4. NO people besides the two boots in the first second — NO music.""",
    """TIMELINE — ONE continuous take, no cuts, already in progress at the first frame:
BEAT 1 (0–1s) — CU, 47°, the camera already tilting down from knee height onto @JOVEM's two boots planted on red earth with dry grass, frame-centre-left; the tilt completes and the lens points straight down.
BEAT 2 (1–2s) — the camera travels straight down past the boots and into the ground: the surface passes the lens and becomes a vertical wall of earth sliding upward through the frame, grass roots hanging in it.
BEAT 3 (2–4s) — the descent accelerates: red laterite soil, then mottled saprolite in ochre and cream, then fractured grey rock pass upward; small stones and crumbs fall with the movement.
BEAT 4 (4–5s) — a seam of dark banded iron ore fills the frame — steel-grey hematite layers with metallic glints between thin ochre bands — the camera still descending. Hard end mid-descent.""",
    """CAMERA — an impossible camera with a real body: it behaves like a camera lowered down a vertical excavation wall on a cable, close to the wall (about 40 cm), slight sway and a tremor from the cable.
MOVEMENT: the camera TRAVELS — a tilt down (0–1s) and then a straight vertical descent that accelerates (1–4s) and keeps its speed to the end; one continuous movement.
OPTICS: 47°, no lens drift; the wall surface sharp, the depth beyond falling into shadow.
FOCUS: on the wall surface passing the lens.
NOT: a CGI fly-through, a game-style cross-section, a zoom, a cut, a reversal, a rise, a spin.""",
    """PHYSICS & MATERIAL — gravity is real: loose crumbs and pebbles fall past the lens at the same speed as the descent, never float; roots hang and sway with the passing air; the soil is damp and compact in the deeper layers, dry and crumbling near the surface; the ore is heavy, dense, glinting where fresh fractures catch the light. Nothing floats, nothing loops. OVER-REAL: dry capim roots with earth clinging to them, the brick-red of laterite with black manganese specks, cream-and-ochre mottling of saprolite, rough fracture faces of grey rock, thin metallic hematite bands in the ore. If any surface looks clean, smooth, plastic, CGI or rendered — WRONG.""",
    """LIGHT — MOTIVATED LIGHT ONLY, late afternoon above ground (KEY):
START (0–1s): the low sun ~4300 K from frame-LEFT on the boots and the red earth.
DURING (1–4s): underground, the only light is the daylight falling in from the opening above and from frame-LEFT; it weakens with depth — each layer is a little darker and cooler than the one before.
END (4–5s): the ore is lit only by that last faint top light; the hematite bands catch it in small metallic glints; the frame is dark but readable, never black.
EXPOSURE: exposed for the wall surface in whatever light exists each second; NO invented lamp underground; shadows soft and readable; NO vignette.
NOT: a headlamp, a glowing underground light, magical glow, a bright evenly lit cross-section, sunbeams.""",
    T.FILM_LOOK,
    f"""SOUND — the wind of the summit for the first second, then cut off as the ground closes over; the dry rustle of grass; soil scraping and crumbling past; small stones ticking; a deep low rumble of rock pressure growing with depth; a faint metallic resonance as the ore passes. {T.MUSIC_POLICY}""",
    f"""NEGATIVE: @JOVEM's face, his hands, a second person, a CGI cross-section, game graphics, glowing ore, gold, lava, crystals, gems, magical light, a headlamp, black frame at the end, a cut, the camera rising, a spin, floating particles, {T.NEG_SPINE}.""",
    """[ORDER: ONE continuous take, 5s, impossible camera descending a real excavation wall — (0–1s) tilt down onto his boots on red earth — (1–2s) into the ground, roots — (2–4s) laterite, saprolite, grey rock pass upward, accelerating — (4–5s) dark banded iron ore fills the frame, still descending; hard end. Invariants: one movement; photographed, not CGI; ends on the ore; only his boots. Look: large-format spherical, red-ochre earth, fine grain, no vignette. No dialogue. NO music. NO subtitles, NO text.]""",
)

# ---------------------------------------------------------------- T02-B2 + T03
_CLASS_WHO = f"""WHO IS WHO — READ FIRST, ABSOLUTE:
@ALUNO ({ANCH['ALUNO']}) — the STUDENT: sits at his desk, answers, listens; NEVER stands, NEVER speaks after his line; owns the frame-LEFT half.
@PROFESSORA ({ANCH['PROFESSORA']}) — the TEACHER: steps into frame from frame-RIGHT and stands beside his desk, speaks once; NEVER sits, NEVER touches the student; owns the frame-RIGHT half.
FACES: each face exists once; the 6–8 classmates in the soft background are distinct children, silent, mouths closed, none with @ALUNO's face; no twins, no clones.
CONTACT: the only touch is @PROFESSORA's right hand resting on the back of @ALUNO's chair; nobody touches anyone."""

_CLASS_ACTING = f"""ACTING — @ALUNO (fully invested in the tactic; the work happens in the eyes)
{DIRECT}
EVENT: a child gives the answer and the teacher turns it into the lesson.
MOTIVE: he just answered in class and wants to have got it right.
GOAL: to be right.
OBSTACLE: maybe it was a silly answer.
TACTIC: answer short and search your eyes for the "right?".
LIVING EYES: {EYES} Involuntary detail: he presses his lips together right after the line. A frozen pupil is wrong.
NOT: a cute pose, a big grin, a child-actor performance.

ACTING — @PROFESSORA (fully invested in the tactic; the work happens in the eyes)
{DIRECT}
MOTIVE: she wants to turn his answer into the lesson for everyone.
GOAL: that the idea sticks.
OBSTACLE: a lesson that sounds like a lecture gets lost.
TACTIC: validate him with one look, then turn to you as to the whole class and check that it landed.
LIVING EYES: {EYES} Involuntary detail: a small nod to herself after the line. A frozen pupil is wrong.
NOT: lecturing, pointing a finger, a broad smile, patting the student.

ACTING — classmates (background): follow the exchange with their eyes; NOT looking at the lens, NOT speaking."""

_CLASS_CAMERA = """CAMERA — authored: an impossible camera that, once inside the room, becomes a crane arriving and settling.
MOVEMENT: the camera TRAVELS down through the dark ore, between the steel roof trusses and through the gap in the ceiling lining, fast and continuous, decelerating as it descends into the room; it lands softly at @ALUNO's eye height and from then on STAYS PUT — a locked frame with only a faint settle.
OPTICS: 47° during the descent; 29° MCU from the landing; no zoom.
FOCUS: on the surfaces passing during the descent; on @ALUNO's eyes after the landing; on @PROFESSORA's eyes when she speaks; @ALUNO stays in focus beside her.
HORIZON: level after the landing.
COMPOSITION: off-centre two-shot after she enters — @ALUNO in the frame-LEFT half, @PROFESSORA in the frame-RIGHT half, both eyelines on the upper-third line; the classroom soft behind.
NOT: a cut, a CGI fly-through, a drone, an orbit, handheld shake after the landing, centred symmetrical framing."""

_CLASS_GEOM = """GEOMETRY — windows along the frame-LEFT wall; @ALUNO seated at a second-row desk facing the camera; @PROFESSORA standing 60 cm to his right (frame-RIGHT); the camera at 1.1 m height, 1.8 m in front of his desk after the landing; classmates 1.5–5 m behind them, soft."""

_CLASS_PHYS = """PHYSICS & MATERIAL — during the descent, dust motes stream past the steel; the steel trusses are heavy, riveted and painted, flaking; the ceiling lining has a gap the camera passes cleanly; in the room, chairs creak when weight shifts, a pencil rolls a few centimetres on a desk, her hand presses the chair back slightly. Nothing floats, nothing loops. OVER-REAL: rust blooming through grey paint on the trusses, worn formica desks with pen marks, chalk dust on her sleeve, sun-faded curtains, scuffed floor tiles. If any surface looks clean, smooth, plastic, CGI or rendered — WRONG."""

_CLASS_LIGHT_START = """START (0–2s): the dark banded ore lit only by faint top light, hematite glints.
DURING (2–4s): thin blades of daylight from gaps in the roof tiles cross the steel trusses from frame-LEFT; between them, shadow.
END (4s on): inside the classroom — the key is daylight through the windows on frame-LEFT, ~5600 K, soft and directional, on the frame-LEFT side of both faces; the classroom behind about one stop darker, readable, never black."""

T02B2 = join(
    contract(12, "ONE continuous take, no cuts", "an authored impossible camera that travels from inside the earth through a steel roof into a classroom and lands", extra=" (fast travel during the descent, everything after the landing in real time)"),
    f"""REFERENCES — each reference has ONE job:
@ALUNO — IDENTITY of @ALUNO: face, hair, build, hands and wardrobe. 100% matches.
@PROFESSORA — IDENTITY of @PROFESSORA: face, hair, build, hands and wardrobe. 100% matches.
{SCOPE_ID}""",
    _CLASS_WHO,
    """SCENE — A state school classroom in Minas Gerais on a weekday afternoon; a lesson is already happening. The camera arrives from inside the earth, through the steel of the roof, and lands on a student who is about to answer.
THE SOUL OF THE SCENE (play it, never explain it): the boy's short answer is the thesis of the whole film, and the teacher knows it — she makes it the lesson.""",
    f"""{LOCKS_HEAD}
1. ONE continuous take from the ore to the classroom, no cuts — WRONG if it cuts.
2. Once landed, the camera stays put; the speech happens only after the landing, in real time — WRONG if anyone speaks while the camera is travelling.
3. @ALUNO frame-LEFT seated, @PROFESSORA frame-RIGHT standing, in that order — WRONG if they swap sides or she sits.
4. @ALUNO speaks only "É futuro."; @PROFESSORA speaks only "Minério não é só minério."; every other mouth is closed — WRONG if the lines swap mouths or a classmate speaks.
5. Daylight from frame-LEFT — NO music.""",
    """TIMELINE — ONE continuous take, no cuts, already in progress at the first frame:
BEAT 1 (0–2s) — the frame is filled with dark banded iron ore, the camera already descending; the ore gives way to darkness and out of it heavy steel roof trusses rise past the lens.
BEAT 2 (2–4s) — the camera threads between two steel trusses, passes through a gap in the ceiling lining and enters the classroom from above, decelerating.
BEAT 3 (4–6s) — it descends to a boy's eye height and lands softly in an MCU, 29°, of @ALUNO seated at his desk in the frame-LEFT half, already looking at the lens; it settles and STAYS PUT.
BEAT 4 (6–7s) — @ALUNO answers to the lens.
BEAT 5 (7–8s) — @PROFESSORA steps into the frame-RIGHT half from frame-right and rests her right hand on the back of his chair; her eyes go to him once.
BEAT 6 (8–10s) — she turns her eyes to the lens and speaks, as to the whole class.
BEAT 7 (10–12s) — both hold; her eyes check you; his flick to her and back to you. Hard end on the held look.""",
    f"""{DLG}
[6–7s] @ALUNO (on camera, Brazilian Portuguese, Belo Horizonte accent, quick and a little unsure, rising slightly at the end): "É futuro."
[8–10s] @PROFESSORA (on camera, Brazilian Portuguese, Belo Horizonte accent, warm teacher's tone, each word placed, completing his thought): "Minério não é só minério."
{T.voice_lock('ALUNO')}
{T.voice_lock('PROFESSORA')}""",
    _CLASS_ACTING,
    _CLASS_CAMERA,
    _CLASS_GEOM,
    _CLASS_PHYS,
    f"""LIGHT — MOTIVATED LIGHT ONLY, afternoon (KEY):
{_CLASS_LIGHT_START}
EXPOSURE: exposed for whatever the camera is passing each second, then for skin; shadows soft and readable; even exposure, NO vignette.
CONTINUITY: once inside, the window light stays frame-LEFT; lit sides never flip.
NOT: flat ceiling-panel light, frontal fill, a glowing underground light, sunbeam shafts, beauty light.""",
    T.FILM_LOOK,
    f"""SOUND — a deep rock rumble at the start; a metallic hum as the steel passes; the dry tick of the roof tiles; then the classroom: low murmur that stops as the boy answers, a chair creak, a pencil rolling, a bus passing outside far off, children's voices from the yard, distant. After her line, the room is quiet for two seconds. {T.MUSIC_POLICY}""",
    T.WORLD,
    f"""NEGATIVE: speech during the descent, swapped sides, @PROFESSORA sitting, lines in the wrong mouth, a classmate speaking, readable writing on the chalkboard, a school emblem, a cut, a CGI fly-through, glowing ore, handheld shake after the landing, {T.NEG_SPINE}.""",
    """[ORDER: ONE continuous take, 12s — (0–2s) dark ore, then steel trusses rise past — (2–4s) between the trusses, through the ceiling — (4–6s) lands on @ALUNO, MCU 29°, frame-LEFT, and stays put — (6–7s) "É futuro." — (7–8s) @PROFESSORA enters frame-RIGHT, hand on his chair — (8–10s) "Minério não é só minério." to the lens — (10–12s) both hold. Invariants: one take; speech only after the landing; he left seated, she right standing; one line each, other mouths closed. Look: large-format spherical, mid-key, red-ochre and steel, fine grain, no vignette. Brazilian Portuguese. NO music. NO subtitles, NO text.]""",
)

# ---------------------------------------------------------------- T02-B3 (alternativa inteiriça)
T02B3 = join(
    contract(17, "ONE continuous take, no cuts", "an authored impossible camera that goes from a man's boots on a summit down through the earth, through a steel roof and into a classroom, and lands", extra=" (fast travel during the descent, everything after the landing in real time)"),
    f"""REFERENCES — each reference has ONE job:
@JOVEM — OBJECT ONLY: his dusty brown leather work boots and trouser hems — nothing else of him appears.
@ALUNO — IDENTITY of @ALUNO: face, hair, build, hands and wardrobe. 100% matches.
@PROFESSORA — IDENTITY of @PROFESSORA: face, hair, build, hands and wardrobe. 100% matches.
{SCOPE_ID}""",
    _CLASS_WHO + "\n@JOVEM — seen ONLY as his two boots on the red earth during 0–1s; his face and body NEVER appear.",
    """SCENE — From a man's boots on a summit, the camera dives through the earth — roots, soil, rock, iron ore — then through the steel of a school roof, and lands on a student who is about to answer.
THE SOUL OF THE SCENE (play it, never explain it): earth, ore, steel, school — one chain; the boy's short answer is the thesis of the film and the teacher makes it the lesson.""",
    f"""{LOCKS_HEAD}
1. ONE continuous take from the boots to the classroom, no cuts — WRONG if it cuts.
2. The descent looks photographed, not animated — WRONG if it looks like a CGI cross-section.
3. Speech only after the landing, in real time; @ALUNO frame-LEFT seated, @PROFESSORA frame-RIGHT standing — WRONG if anyone speaks while travelling or they swap sides.
4. @ALUNO speaks only "É futuro."; @PROFESSORA only "Minério não é só minério."; every other mouth closed.
5. NO music.""",
    """TIMELINE — ONE continuous take, no cuts, already in progress at the first frame:
BEAT 1 (0–1s) — CU, 47°, the camera tilting down onto @JOVEM's boots planted on red earth in low sun from frame-left.
BEAT 2 (1–4s) — straight down into the ground: roots, red laterite, mottled saprolite, grey rock pass upward, accelerating; crumbs fall with the movement.
BEAT 3 (4–6s) — dark banded iron ore fills the frame; out of its darkness heavy steel roof trusses rise past the lens.
BEAT 4 (6–8s) — between two trusses, through the gap in the ceiling lining, into the classroom from above, decelerating.
BEAT 5 (8–10s) — lands softly in an MCU, 29°, of @ALUNO seated in the frame-LEFT half, already looking at the lens; STAYS PUT.
BEAT 6 (10–11s) — @ALUNO answers to the lens.
BEAT 7 (11–12s) — @PROFESSORA steps into the frame-RIGHT half and rests her right hand on the back of his chair; her eyes go to him once.
BEAT 8 (12–15s) — she turns to the lens and speaks, as to the whole class.
BEAT 9 (15–17s) — both hold; her eyes check you. Hard end on the held look.""",
    f"""{DLG}
[10–11s] @ALUNO (on camera, Brazilian Portuguese, Belo Horizonte accent, quick and a little unsure, rising slightly at the end): "É futuro."
[12–15s] @PROFESSORA (on camera, Brazilian Portuguese, Belo Horizonte accent, warm teacher's tone, each word placed, completing his thought): "Minério não é só minério."
{T.voice_lock('ALUNO')}
{T.voice_lock('PROFESSORA')}""",
    _CLASS_ACTING,
    _CLASS_CAMERA.replace("down through the dark ore", "down from the boots, through the earth and the dark ore"),
    _CLASS_GEOM,
    _CLASS_PHYS.replace("PHYSICS & MATERIAL — during the descent,", "PHYSICS & MATERIAL — in the earth, crumbs and pebbles fall past the lens at the speed of the descent, roots sway; at the roof,"),
    f"""LIGHT — MOTIVATED LIGHT ONLY, afternoon (KEY):
START (0–1s): the low sun ~4300 K from frame-LEFT on the boots and the red earth.
DURING (1–6s): underground, only the daylight falling in from above, weaker and cooler with depth; the ore lit by a faint top light, hematite glints; then thin blades of daylight from gaps in the roof tiles cross the steel from frame-LEFT.
END (8s on): inside the classroom — the key is daylight through the windows on frame-LEFT, ~5600 K, soft and directional, on the frame-LEFT side of both faces; the room behind one stop darker, readable.
EXPOSURE: exposed for whatever the camera passes, then for skin; NO invented lamp; shadows soft and readable; NO vignette.
NOT: headlamp, glowing underground light, flat ceiling-panel light, frontal fill, sunbeam shafts.""",
    T.FILM_LOOK,
    f"""SOUND — summit wind cut off as the ground closes; soil scraping, stones ticking, a deep rock rumble; a metallic hum at the steel; the tick of roof tiles; then the classroom murmur that stops as he answers, a chair creak, children in the yard far off; after her line, two seconds of quiet room. {T.MUSIC_POLICY}""",
    T.WORLD,
    f"""NEGATIVE: @JOVEM's face or body, speech during the descent, swapped sides, @PROFESSORA sitting, lines in the wrong mouth, a classmate speaking, readable chalkboard writing, school emblem, a cut, a CGI cross-section, glowing ore, gems, lava, handheld shake after the landing, {T.NEG_SPINE}.""",
    """[ORDER: ONE continuous take, 17s — (0–1s) tilt onto his boots — (1–4s) down through roots, soil, rock — (4–6s) iron ore, steel trusses rise — (6–8s) through the ceiling — (8–10s) lands on @ALUNO, MCU 29°, frame-LEFT, stays put — (10–11s) "É futuro." — (11–12s) @PROFESSORA enters frame-RIGHT — (12–15s) "Minério não é só minério." — (15–17s) both hold. Invariants: one take; photographed descent; speech only after landing, he left, she right; one line each. Look: large-format spherical, mid-key, red-ochre and steel, fine grain, no vignette. Brazilian Portuguese. NO music. NO subtitles, NO text.]""",
)


# ---------------------------------------------------------------- Revezamento
def rev_locks(tag, line):
    return f"""{LOCKS_HEAD}
1. The camera TRAVELS frame-left to frame-right at one constant walking pace from the first frame to the last — WRONG if it stops, reverses, pushes in or glides like a gimbal.
2. @{tag} is in frame from the first frame, already working — WRONG if the frame starts empty.
3. When @{tag} speaks, the eyes are on the lens and alive — WRONG if the stare is glassy.
4. Only @{tag} speaks, only "{line}" — every other mouth closed.
5. Light from frame-LEFT — NO music."""


T04 = join(
    contract(6, "ONE continuous take, no cuts", "observed handheld with the camera travelling sideways from frame-left to frame-right at a constant pace"),
    f"""REFERENCES — each reference has ONE job:
@HOMEM_EV — IDENTITY of @HOMEM_EV: face, hair, build, hands and wardrobe. 100% matches.
{SCOPE_ID}""",
    f"""WHO IS WHO — READ FIRST, ABSOLUTE:
@HOMEM_EV ({ANCH['HOMEM_EV']}) — the CAR OWNER: plugs in the charger, speaks once; NEVER poses with the car, NEVER points at it, NEVER walks out of frame.
FACES: his face exists once; any passer-by far in the background is a distinct soft figure.
CONTACT: nobody touches him.""",
    """SCENE — Late afternoon in an open-air parking lot in a Minas Gerais city; @HOMEM_EV is already at a public charging post beside his compact electric car, connector in hand.
THE SOUL OF THE SCENE (play it, never explain it): he did the maths before switching cars and is quietly proud of it — he half-suspects you think it is a luxury and disarms that without a fuss.""",
    rev_locks("HOMEM_EV", "É a possibilidade de um mundo mais verde,"),
    """TIMELINE — ONE continuous take, no cuts, already in progress at the first frame:
BEAT 1 (0–2s) — MS, 63°, the camera already travelling left to right: @HOMEM_EV at the right third, connector in his right hand, guiding it into the car's charging port at hip height; the first push meets resistance, he lines it up and presses again until the latch clicks.
BEAT 2 (2–5s) — still with his hand on the connector, he turns his head toward the lens with a sidelong look and speaks; he drifts toward the centre as the camera passes.
BEAT 3 (5–6s) — he lets go of the connector and checks the cable hangs right, eyes back on the car; the camera still travelling. Hard end mid-movement.""",
    f"""{DLG}
[2–5s] @HOMEM_EV (on camera, Brazilian Portuguese, Belo Horizonte accent, relaxed and conversational, a half-smile in the breath): "É a possibilidade de um mundo mais verde,"
{T.voice_lock('HOMEM_EV')}""",
    f"""ACTING — @HOMEM_EV (fully invested in the tactic; the work happens in the eyes)
{DIRECT}
MOTIVE: he did the maths and it paid off.
GOAL: that you don't take him for someone showing off.
OBSTACLE: an electric car still reads as a luxury.
TACTIC: keep doing the ordinary task and say it sideways, casually, checking from the corner of his eye whether you think it's luxury.
LIVING EYES: {EYES} Involuntary detail: he blows a short breath through his nose when the latch clicks. A frozen pupil is wrong.
NOT: a salesman smile, showing the car off, a thumbs-up, posing, a speech.""",
    T.rev_camera("2.5 m", "MS"),
    """PHYSICS & MATERIAL — the connector is heavy, its thick cable stiff and coiling, dragging on the ground; the port flap springs open; the latch seats with a click only on the second push. Nothing floats, nothing loops. OVER-REAL: road dust on the car's lower doors, a scuffed rubber cable sheath, a scratched charging post with no brand and a dark blank screen, painted parking lines worn grey, a dry leaf against the kerb, his fingertips pressing white on the grip. If any surface looks clean, smooth, plastic, CGI or rendered — WRONG.""",
    T.LIGHT_EXT,
    T.FILM_LOOK,
    f"""SOUND — LOCATION SOUND ONLY: city traffic two streets away, steady; the cable dragging on asphalt; the port flap; the latch click at 1.5s; a short electronic beep from the charger (one tone, not a melody); his footfall; a car door closing far off. {T.MUSIC_POLICY}""",
    T.WORLD,
    f"""NEGATIVE: car brand badge, readable charger screen, logos, a salesman smile, thumbs-up, posing beside the car, the camera stopping, push-in, gimbal glide, a second speaker, {T.NEG_SPINE}.""",
    """[ORDER: ONE continuous take, 6s, handheld travelling left to right at constant pace — (0–2s) he seats the connector, latch clicks on the second push — (2–5s) sidelong to the lens, his line — (5–6s) back to the cable, camera still travelling. Invariants: constant lateral travel; occupied first frame; living eyes on the lens; only his one line. Look: large-format spherical, mid-key, red-ochre earth, fine grain, no vignette. Brazilian Portuguese. NO music. NO subtitles, NO text.]""",
)

T05 = join(
    contract(6, "ONE continuous take, no cuts", "observed handheld with the camera travelling sideways from frame-left to frame-right at a constant pace"),
    f"""REFERENCES — each reference has ONE job:
@OPERARIO — IDENTITY of @OPERARIO: face, build, hands, wardrobe and safety equipment. 100% matches.
{SCOPE_ID}""",
    f"""WHO IS WHO — READ FIRST, ABSOLUTE:
@OPERARIO ({ANCH['OPERARIO']}) — the STEELWORKER: watches the line, speaks once; NEVER removes his helmet or glasses, NEVER poses, NEVER walks out of frame.
FACES: his face exists once; the two workers far in the background are distinct soft figures, mouths closed.
CONTACT: nobody touches anyone.""",
    """SCENE — Inside a working steel mill in Minas Gerais in the afternoon; behind @OPERARIO a line of hot-rolled steel coils moves on rollers; he is already at his post watching it.
THE SOUL OF THE SCENE (play it, never explain it): he has seen this plant change from the inside and wants someone from outside to see it too.""",
    rev_locks("OPERARIO", "de uma indústria mais eficiente,"),
    """TIMELINE — ONE continuous take, no cuts, already in progress at the first frame:
BEAT 1 (0–2s) — MS, 63°, the camera already travelling left to right: @OPERARIO at the right third, eyes on the steel coil rolling past behind him; he raises a gloved hand and signals once to someone off-screen frame-right.
BEAT 2 (2–4s) — his eyes come from the line to the lens and he speaks, a little louder over the hall.
BEAT 3 (4–6s) — his eyes go back to the line, checking it, then flick once to the lens to see if you saw; the camera still travelling. Hard end mid-movement.""",
    f"""{DLG}
[2–4s] @OPERARIO (on camera, Brazilian Portuguese, light Minas Gerais interior accent, pushed slightly louder over the machines, plain and certain): "de uma indústria mais eficiente,"
{T.voice_lock('OPERARIO')}""",
    f"""ACTING — @OPERARIO (fully invested in the tactic; the work happens in the eyes)
{DIRECT}
MOTIVE: he saw the plant change and nobody outside knows.
GOAL: that you see what works here.
OBSTACLE: the line needs his eyes — he can't stop watching it.
TACTIC: show you with his eyes — the line, then you — and check you looked.
LIVING EYES: {EYES} Involuntary detail: he squints once against the heat shimmer. The clear safety glasses show a soft reflection of the hall; a frozen pupil behind them is wrong.
NOT: removing the glasses, a proud pose, a speech, a smile at the camera, folded arms.""",
    T.rev_camera("2.5 m", "MS"),
    """PHYSICS & MATERIAL — the steel coil is enormous and heavy, rolling slowly on the rollers with a deep grind; heat shimmer rises off it and bends the air behind him; his coverall is stiff and creased; dust and scale drift in the light. Nothing floats, nothing loops. OVER-REAL: blue-black mill scale on the hot steel, oil-dark concrete floor, scratches and dents on his helmet, sweat at his temple under the helmet band, worn leather of his gloves, yellow safety rails with paint chipped to the metal. If any surface looks clean, smooth, plastic, CGI or rendered — WRONG.""",
    T.light_int("tall dusty side windows of the mill hall",
                "the faint orange glow of hot steel far in the background frame-right ~1800 K, never on his face.",
                "the daylight lights the frame-LEFT side of his face and the edge of his helmet; the frame-RIGHT side in soft shade; the hall falls off into dim depth behind him."),
    T.FILM_LOOK,
    f"""SOUND — LOCATION SOUND ONLY: the deep grinding roll of the coil on the rollers; a constant industrial hum; a hydraulic hiss at 1s; an overhead crane's warning beep far off (single repeated tone, not a melody); a metal clank at 4s; his voice over it. {T.MUSIC_POLICY}""",
    T.WORLD,
    f"""NEGATIVE: helmet off, glasses off, company logo on the helmet or coverall, sparks fountain, molten-metal spectacle, fire, the camera stopping, push-in, gimbal glide, a second speaker, {T.NEG_SPINE}.""",
    """[ORDER: ONE continuous take, 6s, handheld travelling left to right at constant pace — (0–2s) eyes on the coil, a hand signal — (2–4s) to the lens, his line over the noise — (4–6s) back to the line, a flick to you. Invariants: constant lateral travel; full safety equipment on; living eyes; only his one line. Look: large-format spherical, mid-key, red-ochre and steel, fine grain, no vignette. Brazilian Portuguese. NO music. NO subtitles, NO text.]""",
)

T06 = join(
    contract(5, "ONE continuous take, no cuts", "observed handheld with the camera travelling sideways from frame-left to frame-right at a constant pace"),
    f"""REFERENCES — each reference has ONE job:
@PESQUISADORA — IDENTITY of @PESQUISADORA: face, hair, build, hands, wardrobe and safety equipment. 100% matches.
{SCOPE_ID}""",
    f"""WHO IS WHO — READ FIRST, ABSOLUTE:
@PESQUISADORA ({ANCH['PESQUISADORA']}) — the RESEARCHER: works at the bench, speaks once; NEVER stops the experiment, NEVER removes gloves or glasses, NEVER walks out of frame.
FACES: her face exists once; one colleague far in the background is a distinct soft figure, mouth closed.
CONTACT: nobody touches anyone.""",
    """SCENE — Afternoon in a pharmaceutical research laboratory in Minas Gerais; @PESQUISADORA is already pipetting samples into a well plate at her bench.
THE SOUL OF THE SCENE (play it, never explain it): almost nobody ever asks what she does — she gives you exactly one phrase and goes back to work.""",
    rev_locks("PESQUISADORA", "de novas tecnologias,"),
    """TIMELINE — ONE continuous take, no cuts, already in progress at the first frame:
BEAT 1 (0–2s) — MS, 63°, the camera already travelling left to right: @PESQUISADORA at the right third, a pipette in her right hand, dispensing into a row of wells, eyes on the tip; she ejects the tip into a waste container.
BEAT 2 (2–4s) — she lifts her eyes from the plate to the lens for the length of the phrase only, and speaks.
BEAT 3 (4–5s) — her eyes return to the plate and she loads a fresh tip; the camera still travelling. Hard end mid-movement.""",
    f"""{DLG}
[2–4s] @PESQUISADORA (on camera, Brazilian Portuguese, Belo Horizonte accent, quiet, quick and exact, the voice of someone mid-task): "de novas tecnologias,"
{T.voice_lock('PESQUISADORA')}""",
    f"""ACTING — @PESQUISADORA (fully invested in the tactic; the work happens in the eyes)
{DIRECT}
MOTIVE: nobody ever asks what she does.
GOAL: that you get it in one phrase.
OBSTACLE: the samples can't wait.
TACTIC: borrow two seconds from the experiment, check that you followed, give the time back.
LIVING EYES: {EYES} Involuntary detail: she pushes her glasses up with the back of her wrist. A frozen pupil is wrong.
NOT: smiling for the camera, holding up a test tube, posing, a speech, stopping the work.""",
    T.rev_camera("2 m", "MS"),
    """PHYSICS & MATERIAL — the pipette plunger resists her thumb and springs back; liquid draws up and dispenses in small clear drops; the used tip pops off into the bin; the nitrile gloves wrinkle at the knuckles. Nothing floats, nothing loops. OVER-REAL: a hand-written strip of tape on a rack with unreadable marks, a scratched bench surface, a tiny droplet on the glove, condensation on a sample tube, a worn pipette grip, a faint crease line on the lab coat. If any surface looks clean, smooth, plastic, CGI or rendered — WRONG.""",
    T.light_int("a wide lab window",
                "the white work light under the shelf above the bench ~5000 K as a low secondary on the plate and her hands, never flattening her face.",
                "the daylight lights the frame-LEFT side of her face; the frame-RIGHT side in soft shade; the lab behind falls off a stop, readable."),
    T.FILM_LOOK,
    f"""SOUND — LOCATION SOUND ONLY: the fume hood's steady airflow; the pipette's soft click and the tip popping into the bin; glass tapping glass; a centrifuge winding down far off; her breath. {T.MUSIC_POLICY}""",
    T.WORLD,
    f"""NEGATIVE: glowing liquids, coloured smoke, sci-fi lab, holograms, readable labels, logos, gloves off, glasses off, holding up a tube to the camera, the camera stopping, push-in, gimbal glide, a second speaker, {T.NEG_SPINE}.""",
    """[ORDER: ONE continuous take, 5s, handheld travelling left to right at constant pace — (0–2s) pipetting, tip ejected — (2–4s) eyes up to the lens, her phrase — (4–5s) back to the plate, new tip. Invariants: constant lateral travel; occupied first frame; living eyes; only her one line. Look: large-format spherical, mid-key, fine grain, no vignette. Brazilian Portuguese. NO music. NO subtitles, NO text.]""",
)

T07 = join(
    contract(6, "ONE continuous take, no cuts", "observed handheld with the camera travelling sideways from frame-left to frame-right at a constant pace"),
    f"""REFERENCES — each reference has ONE job:
@DONO — IDENTITY of @DONO: face, hair, build, hands and wardrobe. 100% matches.
{SCOPE_ID}""",
    f"""WHO IS WHO — READ FIRST, ABSOLUTE:
@DONO ({ANCH['DONO']}) — the OWNER: stands at the table, serves, speaks once; NEVER sits, NEVER walks out of frame.
CUSTOMER (unreferenced: a woman about 35, seen from behind and in partial profile, dark hair, olive cardigan) — seated at the table in the frame-LEFT foreground, soft; NEVER speaks, mouth closed, NEVER looks at the lens.
FACES: each face exists once; no twins, no clones.
CONTACT: nobody touches anyone; the plate passes from his hands to the table, never into her hands.""",
    """SCENE — Lunchtime in a small healthy-food restaurant in an interior town of Minas Gerais; @DONO is already setting a full plate in front of a regular customer.
THE SOUL OF THE SCENE (play it, never explain it): he has watched the town change across decades of counter, and this restaurant is his proof — he lets you in on it like an old regular.""",
    rev_locks("DONO", "de uma economia mais sustentável."),
    """TIMELINE — ONE continuous take, no cuts, already in progress at the first frame:
BEAT 1 (0–2s) — MS, 63°, the camera already travelling left to right: @DONO at the right third, standing at the table, setting down a heavy ceramic plate of rice, beans, greens and grilled vegetables in front of the CUSTOMER, who sits soft in the frame-LEFT foreground.
BEAT 2 (2–3s) — he watches her take the first look at the plate, waiting for her verdict.
BEAT 3 (3–5s) — he turns his eyes to the lens with a complicit look, like to an old regular, and speaks.
BEAT 4 (5–6s) — his eyes go back to her; he wipes his hands on the apron; the camera still travelling. Hard end mid-movement.""",
    f"""{DLG}
[3–5s] @DONO (on camera, Brazilian Portuguese, light Minas Gerais interior accent, deep and unhurried, a complicit warmth, the last word landing low): "de uma economia mais sustentável."
{T.voice_lock('DONO')}""",
    f"""ACTING — @DONO (fully invested in the tactic; the work happens in the eyes)
{DIRECT}
MOTIVE: decades behind this counter, and the restaurant is the proof that things changed.
GOAL: to bring you into the joke and the pride.
OBSTACLE: the customer is right there — the plate comes first.
TACTIC: serve without hurry, then include you like an old regular with a sideways look.
LIVING EYES: {EYES} Involuntary detail: his moustache lifts on one side before the line. A frozen pupil is wrong.
NOT: a waiter's bow, presenting the plate to the camera, a big laugh, a thumbs-up, a speech.

ACTING — CUSTOMER: TACTIC check the plate and trust him; eyes on the food, then up to him; involuntary detail: she pulls the napkin closer; NOT speaking, NOT looking at the lens.""",
    T.rev_camera("2.2 m", "MS"),
    """PHYSICS & MATERIAL — the ceramic plate is heavy and touches down with a dull knock; steam rises off the beans and bends in the air from the window; the apron is stiff canvas with old stains; the chair scrapes when she settles. Nothing floats, nothing loops. OVER-REAL: a chipped enamel jug on the table, a worn wooden tabletop polished by elbows, faded checked oilcloth on the next table, a small old burn mark on the back of his left hand, flour or stain marks on the apron, a handwritten menu board in the background with unreadable chalk. If any surface looks clean, smooth, plastic, CGI or rendered — WRONG.""",
    T.light_int("the street window of the restaurant",
                "a warm pendant bulb over the counter in the background ~2800 K, small, never on the faces.",
                "the daylight lights the frame-LEFT side of his face and the steam over the plate; the frame-RIGHT side in soft shade; the back of the room falls off a stop, readable."),
    T.FILM_LOOK,
    f"""SOUND — LOCATION SOUND ONLY: the plate's dull knock on wood; cutlery on plates at other tables; a low murmur of other diners with no words standing out; a pan sizzling in the kitchen off-screen; the street through the open door; the chair scrape. {T.MUSIC_POLICY}""",
    T.WORLD,
    f"""NEGATIVE: the customer speaking, the customer looking at the lens, the plate handed into her hands, presenting the plate to the camera, a waiter's bow, readable menu, logos, the camera stopping, push-in, gimbal glide, {T.NEG_SPINE}.""",
    """[ORDER: ONE continuous take, 6s, handheld travelling left to right at constant pace — (0–2s) he sets the plate before the customer — (2–3s) he waits for her look — (3–5s) to the lens, complicit, his line — (5–6s) back to her, hands on the apron. Invariants: constant lateral travel; occupied first frame; living eyes; only his one line, the customer silent. Look: large-format spherical, mid-key, red-ochre earth, fine grain, no vignette. Brazilian Portuguese. NO music. NO subtitles, NO text.]""",
)

T08 = join(
    contract(11, "ONE continuous take, no cuts", "observed handheld walk-and-talk: the camera travels sideways from frame-left to frame-right with her and stops when she stops"),
    f"""REFERENCES — each reference has ONE job:
@AGRICULTORA — IDENTITY of @AGRICULTORA: face, hair, build, hands and wardrobe. 100% matches.
{SCOPE_ID}""",
    f"""WHO IS WHO — READ FIRST, ABSOLUTE:
@AGRICULTORA ({ANCH['AGRICULTORA']}) — the FARMER: walks the soybean rows, checks the plants, speaks two lines, stops; NEVER poses, NEVER takes the hat off, NEVER walks toward the camera.
FACES: her face exists once; nobody else in frame.
CONTACT: only her right hand brushing the tops of the plants.""",
    """SCENE — Late afternoon in a soybean field in the interior of Minas Gerais; @AGRICULTORA is already walking along a row, her right hand brushing the tops of the knee-high plants, checking the pods.
THE SOUL OF THE SCENE (play it, never explain it): she talks about what is hers — the land she looks after — and walks you through it; on "mais raro" she stops judging the plants and looks for you.""",
    f"""{LOCKS_HEAD}
1. The camera TRAVELS frame-left to frame-right with her at her walking pace from the first frame until 8s, then STAYS PUT when she stops — WRONG if it stops early, reverses, pushes in or glides like a gimbal.
2. @AGRICULTORA walks frame-left to frame-right and stops at 8s — WRONG if she walks toward or away from the camera.
3. Her eyes are alive: on the plants, then on the lens; at 8s they find the lens and stay — WRONG if glassy or hidden by the hat brim.
4. Only @AGRICULTORA speaks, only these two lines.
5. Sun from frame-LEFT — NO music.""",
    """TIMELINE — ONE continuous take, no cuts, already in progress at the first frame:
BEAT 1 (0–1s) — MS, 63°, the camera already travelling left to right beside her: @AGRICULTORA walking left to right at the left-centre of the frame, right hand brushing the plants, eyes on the pods.
BEAT 2 (1–5s) — still walking, she turns her head to the lens and speaks the first line, eyes moving between you and the plants.
BEAT 3 (5–6s) — a breath; she bends a stem to look at a pod and lets it spring back.
BEAT 4 (6–8s) — walking, she starts the second line to the lens.
BEAT 5 (8–10s) — on "mais raro" she stops walking, turns her body toward the lens and stops judging the plants; the camera stops with her and STAYS PUT; she finishes the line.
BEAT 6 (10–11s) — she holds your eyes, waiting. Hard end on the held look.""",
    f"""{DLG}
[1–5s] @AGRICULTORA (on camera, Brazilian Portuguese, light Minas Gerais interior accent, steady, a walking breath under the words): "Enquanto o mundo olha para o nióbio e as terras raras de Minas,"
[6–10s] @AGRICULTORA (on camera, Brazilian Portuguese, light Minas Gerais interior accent, slowing, the last words given straight to you): "Minas olha para o que há de mais raro na nossa terra:"
{T.voice_lock('AGRICULTORA')}""",
    f"""ACTING — @AGRICULTORA (fully invested in the tactic; the work happens in the eyes)
{DIRECT}
EVENT: a woman walking her field turns the talk from what is under the ground to who is on it.
MOTIVE: she looks after this land and knows what it is worth.
GOAL: to bring you along to the point.
OBSTACLE: the world only talks about what's under the ground.
TACTIC: walk you through the field like a neighbour, judging the plants as she goes — then stop and look for you.
MOMENT TO MOMENT: — [0–5s] eyes split between the pods and you — [5–6s] she checks one pod — [6–8s] back to you, still walking — [8–10s] she stops; her eyes leave the plants for good and search both of yours — [10–11s] she waits.
LIVING EYES: {EYES} Involuntary detail: she breathes out through her nose when she stops. The hat brim is pushed back so the sun reaches her eyes; a frozen pupil is wrong.
NOT: a speech, a proud pose, arms spread over the field, a broad smile, taking the hat off.""",
    """CAMERA — observed handheld: the operator crab-walks sideways at her walking pace (about 0.8 m per second) from frame-LEFT to frame-RIGHT along the next row, lens at shoulder height (1.5 m), 2.5 m from her, on the shadow side of her face.
MOVEMENT: the camera TRAVELS frame-left to frame-right with her from the first frame until 8s, with human footfall bounce; at 8s it stops with her and STAYS PUT, breathing, to the end. One movement, then stillness.
OPTICS: MS at 63°, natural perspective; no lens drift inside the take.
FOCUS: on her eyes; the field behind soft but readable.
HORIZON: level.
COMPOSITION: off-centre; she holds the left-centre while walking; when she stops she is just left of centre with the field running to the horizon frame-right; her eyes on the upper-third line.
NOT: gimbal glide, drone, aerial, orbit, push-in, zoom, the camera stopping before 8s, the camera reversing, centred symmetrical framing.""",
    """GEOMETRY — the soybean rows run left to right across the frame; @AGRICULTORA walks along one row, the camera along the parallel row 2.5 m away on her right-hand side; the plants knee-high; the field runs flat to a line of trees about 400 m away; the sun low on frame-LEFT.""",
    """PHYSICS & MATERIAL — the plants are springy: her hand bends the tops and they whip back behind her; the pod she checks resists, bends and springs back; her boots press into the soft red soil between rows and lift dust; her braid swings with each step and settles when she stops. Nothing floats, nothing loops. OVER-REAL: fine hairs on the green soybean pods, a few yellowing leaves with holes, red soil caked on her boots, sun lines at her eyes, a frayed edge on the straw brim, a sweat patch on the back of her shirt. If any surface looks clean, smooth, plastic, CGI or rendered — WRONG.""",
    T.LIGHT_EXT,
    T.FILM_LOOK,
    f"""SOUND — LOCATION SOUND ONLY: the leaves brushing her hand and her trousers in a steady rhythm; her boots on soft soil; wind over the field; a quero-quero bird calling twice far off; insects in the late afternoon; when she stops, the brushing stops and only wind and insects remain. {T.MUSIC_POLICY}""",
    T.WORLD,
    f"""NEGATIVE: walking toward the camera, the camera stopping early, the camera reversing, arms spread over the field, hat off, eyes hidden in the hat's shadow, a tractor in the foreground, drone shot, a second person, {T.NEG_SPINE}.""",
    """[ORDER: ONE continuous take, 11s, handheld walk-and-talk travelling left to right, then still — (0–1s) she walks, hand on the plants — (1–5s) first line to the lens, walking — (5–6s) checks a pod — (6–8s) second line begins — (8–10s) she stops on "mais raro", the camera stops with her, she finishes the line — (10–11s) she holds your eyes. Invariants: lateral travel until 8s then still; she walks left to right; living eyes on the lens; only her two lines; sun frame-LEFT. Look: large-format spherical, mid-key, red-ochre earth, fine grain, no vignette. Brazilian Portuguese. NO music. NO subtitles, NO text.]""",
)

# ---------------------------------------------------------------- T09
T09 = join(
    contract(14, "ONE continuous take, no cuts", "an authored locked frame on a tripod whose only movement is one focus rack"),
    f"""REFERENCES — each reference has ONE job:
@FUNCIONARIO — IDENTITY of @FUNCIONARIO: face, build, hands, wardrobe and safety equipment. 100% matches.
@MINA — WORLD: the open-pit niobium mine — terraced benches of ochre and brown earth, haul roads, a stockpile of ore; the world for the whole take.
{SCOPE_ID} @MINA supplies geography and materials ONLY — its light is replaced by the LIGHT block.""",
    f"""WHO IS WHO — READ FIRST, ABSOLUTE:
@FUNCIONARIO ({ANCH['FUNCIONARIO']}) — the MINE WORKER: stands still, speaks, looks down once, looks back up; NEVER removes any safety equipment, NEVER walks, NEVER gestures toward the mine.
FACES: his face exists once; the haul trucks far in the background have no visible drivers.
CONTACT: nobody touches anyone.""",
    """SCENE — Late afternoon at the edge of an open-pit niobium mine in the interior of Minas Gerais. The frame opens on the ore; only then does the man behind it come into focus — he is already looking at you.
THE SOUL OF THE SCENE (play it, never explain it): the world comes here for the ore and nobody asks about him; he waits, without hurry, for the moment you understand that the rare thing is him.""",
    f"""{LOCKS_HEAD}
1. ONE continuous take, the camera LOCKED; the only movement is the focus rack from the ore to his face at 1–2s — WRONG if the camera moves or cuts.
2. Full mining safety equipment on at all times: hard hat with chin strap, safety glasses, high-visibility vest, gloves — WRONG if any piece is missing, unbuckled or carries a logo.
3. His eyes are alive and on the lens, except one look down at the ore at 4–5s and the rise back at 7–8s, landing on the upper-third line at about 45% of the frame width — WRONG if glassy or landing elsewhere.
4. Only @FUNCIONARIO speaks, only these lines, with the pause after "a nossa gente."
5. Sun from frame-LEFT — NO music.""",
    """TIMELINE — ONE continuous take, no cuts, already in progress at the first frame:
BEAT 1 (0–1s) — the frame opens with the rough edge of an ore stockpile sharp in the frame-RIGHT lower foreground, 0.8 m from the lens; @FUNCIONARIO stands 1.6 m from the lens, just left of centre, soft, already looking at the lens.
BEAT 2 (1–2s) — the focus racks from the ore to his face; the ore goes soft.
BEAT 3 (2–4s) — he speaks the first line, plain and low.
BEAT 4 (4–5s) — the pause: his eyes drop to the ore in the frame-RIGHT foreground.
BEAT 5 (5–9s) — he starts the second line with his eyes still on the ore; on "construir novos caminhos" (7–8s) his eyes rise and land on the lens.
BEAT 6 (9–12s) — he finishes the sentence to the lens, small pauses between "nasce", "vive" and "trabalha".
BEAT 7 (12–14s) — he holds your eyes, mouth closed, checking that it landed. Hard end on the held look.""",
    f"""{DLG}
[2–4s] @FUNCIONARIO (on camera, Brazilian Portuguese, light Minas Gerais interior accent, low, plain, unhurried): "a nossa gente."
[5–12s] @FUNCIONARIO (on camera, Brazilian Portuguese, light Minas Gerais interior accent, calm and weighted, a breath at each comma): "Afinal, o que cresce aqui também deve construir novos caminhos para quem nasce, vive e trabalha aqui."
{T.voice_lock('FUNCIONARIO')}""",
    f"""ACTING — @FUNCIONARIO (fully invested in the tactic; the work happens in the eyes)
{DIRECT}
EVENT: where you expected the ore to be the star, a person appears.
MOTIVE: the world comes for the ore and never asks about him.
GOAL: that you see who is standing here.
OBSTACLE: he is not used to being the subject.
TACTIC: hold your gaze without hurry and wait for it to land; look at the ore once as if to say "that's not it", then come back to you.
MOMENT TO MOMENT: — [0–4s] steady on you, the first line plain — [4–5s] eyes to the ore — [5–8s] the thought builds, eyes still on the ore — [7–8s] eyes rise and land on you — [8–14s] he checks both of your eyes and waits for the penny to drop.
LIVING EYES: {EYES} Involuntary detail: he swallows once after "a nossa gente.". The clear safety glasses show a soft reflection of the sky; a frozen pupil behind them is wrong.
NOT: a heroic pose, a proud smile, gesturing at the mine, a speech, raising his voice.""",
    T.MATCH_FRAME + """

CAMERA — authored: a locked tripod at his eye height (1.65 m), 1.6 m from his face, frontal; the ore stockpile edge 0.8 m from the lens in the frame-RIGHT lower foreground.
MOVEMENT: the camera STAYS PUT for the whole take — no drift, no push, no shake.
OPTICS: MCU at 29°; no zoom, no lens drift.
FOCUS: starts on the ore in the foreground, his face soft; racks once to his face at 1–2s and stays on his eyes to the end.
HORIZON: level; the far benches of the pit soft behind him.
COMPOSITION: off-centre — his face just left of centre, the soft ore at frame-right bottom, the pit's terraced benches soft beyond.
NOT: handheld, push-in, zoom, dolly, drone, orbit, a second focus rack, centred symmetrical framing.""",
    """PHYSICS & MATERIAL — the ore lumps are dense and heavy, sharp-edged, dull brown with darker grains; fine dust lifts off the pit in the wind and drifts slowly right; the vest is stiff and scuffed; his breath moves the dust on his upper lip. Nothing floats, nothing loops. OVER-REAL: fine ore dust settled in the creases of his vest and gloves and in his moustache, scratches on the helmet, the chin strap's worn buckle, a red-brown film on his boots, sweat at the temple under the helmet band, terraced bench walls with drill marks in the background. If any surface looks clean, smooth, plastic, CGI or rendered — WRONG.""",
    T.LIGHT_EXT,
    T.FILM_LOOK,
    f"""SOUND — LOCATION SOUND ONLY: wind over the open pit; a haul truck's diesel engine labouring far off, steady; a reversing alarm far away (single repeated tone, not a melody); gravel shifting on the stockpile; his breath before each line; after his last word, only wind and the distant truck. {T.MUSIC_POLICY}""",
    T.WORLD + " Mining safety equipment is complete and correct; nobody in the pit without it.",
    f"""NEGATIVE: missing helmet, unbuckled chin strap, no glasses, no vest, logos on the equipment, company name on trucks, gesturing at the mine, a second focus rack, camera movement, handheld shake, a cut, eyes landing off the upper third, a second speaker, glowing ore, gold, {T.NEG_SPINE}.""",
    """[ORDER: ONE continuous take, 14s, locked tripod, one focus rack — (0–1s) ore sharp frame-right, he is soft — (1–2s) rack to his face — (2–4s) "a nossa gente." — (4–5s) eyes to the ore — (5–9s) second line begins, eyes rise to the lens at 7–8s — (9–12s) the sentence finished to you — (12–14s) he holds. Invariants: locked frame, one rack; full safety equipment; living eyes landing at the upper third, 45% width; only his lines. Look: large-format spherical, mid-key, red-ochre earth, fine grain, no vignette. Brazilian Portuguese. NO music. NO subtitles, NO text.]""",
)


# ---------------------------------------------------------------- T10 / T11 (match, sem fala)
def match_locks(subject, mouth_note):
    return f"""{LOCKS_HEAD}
1. The camera is LOCKED in the MATCH FRAME for the whole take — WRONG if it moves, pushes or cuts.
2. {subject}'s eyes rise and land on the lens at 2–3s, on the upper-third line at about 45% of the frame width, and stay there alive — WRONG if they land elsewhere or turn glassy.
3. NO dialogue: {mouth_note} — WRONG if any mouth forms words.
4. Light from frame-LEFT — NO music."""


T10 = join(
    contract(5, "ONE continuous take, no cuts", "an authored locked frame on a tripod", dialogue=False),
    """WHO IS WHO — READ FIRST, ABSOLUTE:
MOTHER (unreferenced: a woman about 28, mixed-race brown skin, dark hair loosely tied, tired soft eyes, a plain oatmeal cotton T-shirt) — holds her newborn, looks down, then up; NEVER speaks, NEVER smiles broadly, NEVER moves out of the MATCH FRAME.
NEWBORN — a real newborn of a few days, small and correctly proportioned, wrapped in a pale cotton blanket, most of the face covered by the blanket and her hand; only the forehead, a closed eye and a cheek show.
FACES: each face exists once; nobody else in the room.
CONTACT: only her hands on the baby: left arm under the body, right hand cupping the back of the head, thumb moving on the blanket.""",
    """SCENE — A bedroom in a modest house in Minas Gerais, afternoon; the MOTHER sits on the edge of the bed holding her newborn, already watching its breathing.
THE SOUL OF THE SCENE (play it, never explain it): she is memorising the face of someone who just arrived — and then she looks up at you, as if you had come in to meet him.""",
    match_locks("the MOTHER", "her mouth stays closed, the baby makes only small breathing sounds"),
    """TIMELINE — ONE continuous take, no cuts, already in progress at the first frame:
BEAT 1 (0–2s) — the MATCH FRAME: the MOTHER in MCU, face just left of centre, eyes down on the baby in her arms at the bottom of frame; her thumb moves on the blanket; she checks the breathing.
BEAT 2 (2–3s) — her eyes rise from the baby and land on the lens.
BEAT 3 (3–5s) — she holds your eyes, quiet, the baby's breathing under her hand. Hard end on the held look.""",
    """ACTING — MOTHER (fully invested in the tactic; the work happens in the eyes)
EVENT: a new life, and she lets you see it.
MOTIVE: everything is new and fragile.
GOAL: to keep him calm and to remember this.
OBSTACLE: tiredness pulling at her.
TACTIC: watch his breathing, memorise the face, then look up and include you — the eyes say "look who arrived".
LIVING EYES: """ + EYES + """ Involuntary detail: a slow tired blink before she looks up. A frozen pupil is wrong.
NOT: speaking, a broad smile, crying, rocking theatrically, presenting the baby to the camera.""",
    T.MATCH_FRAME + """

CAMERA — authored: a locked tripod at her seated eye height (1.1 m), 1.6 m from her face, frontal.
MOVEMENT: the camera STAYS PUT — no drift, no push, no shake.
OPTICS: MCU at 29°; no zoom, no lens drift.
FOCUS: on her eyes; the baby's blanket slightly soft at the bottom edge; the room soft behind.
HORIZON: level.
NOT: handheld, push-in, zoom, tilt down to the baby, orbit, centred symmetrical framing.""",
    """PHYSICS & MATERIAL — the baby is light but limp and warm, the weight sinking into the crook of her arm; the blanket's cotton has soft pilling and folds; a tiny movement of the baby's chest under her hand; her shoulders slightly rounded with fatigue. Nothing floats, nothing loops. OVER-REAL: faint dark circles under her eyes, a few loose hairs across her forehead, the worn softness of the T-shirt neckline, pilling on the blanket, a crease mark from a pillow on her cheek, the baby's flaky newborn skin at the forehead. If any surface looks clean, smooth, plastic, CGI or rendered — WRONG.""",
    T.light_int("a bedroom window with a thin curtain",
                "no other source.",
                "the daylight lights the frame-LEFT side of her face and the blanket; the frame-RIGHT side in soft shade; the room behind falls off a stop, readable."),
    T.FILM_LOOK,
    f"""SOUND — LOCATION SOUND ONLY: quiet room tone; the baby's small breathing and one tiny newborn sigh; her thumb on the cotton; a neighbour's radio far away with no recognisable music — only a murmur of voices; a motorbike passing in the street outside. {T.MUSIC_POLICY}""",
    T.WORLD,
    f"""NEGATIVE: the mother speaking, any mouth forming words, a doll-like baby, wrong newborn proportions, an adult-faced baby, the baby's full face, presenting the baby to the camera, crying, a broad smile, camera movement, tilt down, a cut, eyes landing off the upper third, {T.NEG_SPINE}.""",
    """[ORDER: ONE continuous take, 5s, locked MATCH FRAME, MCU 29° — (0–2s) eyes down on the baby, thumb on the blanket — (2–3s) eyes rise and land on the lens at the upper third, 45% width — (3–5s) she holds your eyes. Invariants: locked frame; eyes landing on the mark; no dialogue; baby partly covered, correct proportions. Look: large-format spherical, mid-key, fine grain, no vignette. NO music. NO subtitles, NO text.]""",
)

T11 = join(
    contract(5, "ONE continuous take, no cuts", "an authored locked frame on a tripod", dialogue=False),
    """WHO IS WHO — READ FIRST, ABSOLUTE:
FAN (unreferenced: a young woman about 20, dark skin, short natural hair, small hoop earrings, a plain terracotta-red T-shirt with no print) — watches the play, then looks up to the lens; NEVER speaks, NEVER shouts, NEVER cheers with her arms up, NEVER moves out of the MATCH FRAME.
CROWD — the stands behind her: dozens of distinct people, soft, out of focus, colours indistinct and mixed; nobody with her face; no twins, no clones.
CONTACT: nobody touches her.""",
    """SCENE — A late-afternoon match at a large concrete football stadium in Belo Horizonte; the FAN is in the stands, already following a long ball, holding her breath.
THE SOUL OF THE SCENE (play it, never explain it): for one second she is deciding whether it will be a goal — and as the ball rises her eyes rise with it and find you.""",
    match_locks("the FAN", "her mouth stays closed; the crowd is only a roar with no words standing out"),
    """TIMELINE — ONE continuous take, no cuts, already in progress at the first frame:
BEAT 1 (0–2s) — the MATCH FRAME: the FAN in MCU, face just left of centre, eyes down-right on the pitch below, lips pressed, breath held; the crowd soft behind her.
BEAT 2 (2–3s) — a long ball goes up; her eyes and chin rise with it and land on the lens.
BEAT 3 (3–5s) — she holds your eyes, breath still held, the crowd's roar swelling behind. Hard end on the held look.""",
    """ACTING — FAN (fully invested in the tactic; the work happens in the eyes)
EVENT: a whole stadium holds its breath and she lets you into it.
MOTIVE: this is her Sunday ritual.
GOAL: to know whether it will be a goal.
OBSTACLE: it's not decided yet.
TACTIC: follow the play, deciding — then share the held breath with you.
LIVING EYES: """ + EYES + """ Involuntary detail: she bites the inside of her lip as the ball goes up. The low sun puts a small live point in her frame-left eye; a frozen pupil is wrong.
NOT: cheering, shouting, arms up, face paint, a scarf, a team jersey, a broad smile.

ACTING — CROWD (background): one organism following one ball; soft, nobody looking at the lens.""",
    T.MATCH_FRAME + """

CAMERA — authored: a locked tripod in the stands at her seated eye height (1.1 m), 1.6 m from her face, frontal.
MOVEMENT: the camera STAYS PUT — no drift, no push, no shake.
OPTICS: MCU at 29°; no zoom, no lens drift.
FOCUS: on her eyes; the crowd behind deeply soft, faces unreadable.
HORIZON: level.
NOT: handheld, push-in, zoom, a pan to the pitch, crowd wide shot, orbit, centred symmetrical framing.""",
    """PHYSICS & MATERIAL — the stands vibrate faintly with the crowd; a breath of wind moves her T-shirt; the people behind rise slightly as the ball goes up, soft shapes lifting. Nothing floats, nothing loops. OVER-REAL: the weathered grey concrete of the stand, a faded plastic seat edge, a few beads of sweat at her hairline, a small chip in the paint of her hoop earring, the cotton texture of the T-shirt. If any surface looks clean, smooth, plastic, CGI or rendered — WRONG.""",
    T.LIGHT_EXT,
    T.FILM_LOOK,
    f"""SOUND — LOCATION SOUND ONLY: the stadium's crowd noise, a dense wordless roar; the thud of the ball kicked far below at 2s; the crowd's rising intake "uhh" as the ball goes up, swelling to the end; a whistle far off. NO chanting songs, NO drums, NO brass band, NO stadium anthem. {T.MUSIC_POLICY}""",
    T.WORLD + " Wardrobe and crowd carry NO football club colour combinations (black-and-white, blue-and-white, green-and-white), NO yellow-and-green national colours, NO flags, NO scarves, NO jerseys.",
    f"""NEGATIVE: the fan speaking or shouting, any mouth forming words, cheering arms, team jersey, scarf, flag, face paint, black-and-white, blue-and-white, green-and-white, yellow-and-green, readable faces in the crowd, chanting, drums, camera movement, a cut, eyes landing off the upper third, {T.NEG_SPINE}.""",
    """[ORDER: ONE continuous take, 5s, locked MATCH FRAME, MCU 29° — (0–2s) eyes down on the play, breath held — (2–3s) the ball goes up, her eyes rise and land on the lens at the upper third, 45% width — (3–5s) she holds your eyes as the roar swells. Invariants: locked frame; eyes landing on the mark; no dialogue; neutral wardrobe, no club colours. Look: large-format spherical, mid-key, fine grain, no vignette. NO music, NO chants, NO drums. NO subtitles, NO text.]""",
)

# ---------------------------------------------------------------- T12 + T13
T12 = join(
    contract(15, "2 shots with 1 hard cut at 4s", "shot 1 observed from inside the bus, shot 2 an authored locked frame rigged to the dashboard; cuts only at the specified point, the camera adds no cuts of its own"),
    f"""REFERENCES — each reference has ONE job:
@MOTORISTA — IDENTITY of @MOTORISTA: face, hair, build, hands and wardrobe. 100% matches.
@ESTUDANTE — IDENTITY of @ESTUDANTE: face, hair, build, hands and wardrobe. 100% matches.
@ONIBUS_INT — WORLD: the inside of a city bus — driver's cab, folding front door, steps, seats, handrails; the world for both shots.
{SCOPE_ID} @ONIBUS_INT supplies the space and materials ONLY — its light is replaced by the LIGHT block.""",
    f"""WHO IS WHO — READ FIRST, ABSOLUTE:
@MOTORISTA ({ANCH['MOTORISTA']}) — the BUS DRIVER: sits at the wheel on the bus's left side, opens and closes the door, drives, speaks once in shot 2; NEVER stands, NEVER lets go of the wheel for more than a second; owns the frame-LEFT half in shot 1.
@ESTUDANTE ({ANCH['ESTUDANTE']}) — the STUDENT: climbs in through the front door, greets with a raised hand, walks past into the bus; NEVER speaks, mouth closed; enters at frame-RIGHT in shot 1.
FACES: each face exists once; the 3–4 seated passengers are distinct soft adults, mouths closed; no twins, no clones.
CONTACT: nobody touches anyone; the greeting is a raised hand and a nod.""",
    """SCENE — Late afternoon on a city bus in Minas Gerais; the bus has just stopped and the front door is already folding open for a teenage student with a backpack.
THE SOUL OF THE SCENE (play it, never explain it): every day he takes people to where the opportunities are; this boy is one of them — he knows him — and he tells you the route like a man explaining it, hands on the wheel.""",
    f"""{LOCKS_HEAD}
1. Exactly 2 shots with 1 hard cut at 4s — WRONG if there are extra cuts.
2. @ESTUDANTE never speaks; only @MOTORISTA speaks, one line, in shot 2 — WRONG if the student's mouth forms words.
3. In shot 2 @MOTORISTA's eyes rise and land on the lens at 5–6s on the upper-third line at about 45% of the frame width, and stay alive — WRONG if glassy or landing elsewhere.
4. His hands stay on the wheel while he speaks; the bus moves forward from 6s — WRONG if the bus stays parked or he lets go.
5. Daylight from frame-LEFT — NO music.""",
    """TIMELINE — 2 shots, 1 hard cut; cuts only at the specified point, the camera adds no cuts of its own:
SHOT 1 (0–4s) — MS, 47°, observed handheld from the first row of seats, looking forward: @MOTORISTA at the wheel in the frame-LEFT half, his right hand on the door control; the folding door in the frame-RIGHT half is already opening with a pneumatic hiss; @ESTUDANTE climbs the steps, backpack on one shoulder, raises a hand; @MOTORISTA nods, eyes following the boy's feet on the steps. HARD CUT.
SHOT 2 (4–15s) — the MATCH FRAME, MCU, 29°, locked on a rig on the dashboard facing @MOTORISTA: his eyes follow the boy passing behind him into the bus (4–5s); his eyes rise and land on the lens (5–6s); the door folds shut and he releases the brake — the bus begins to roll and the street slides past the windows behind him (6s); at 7–12s he speaks to the lens, one quick glance to the road at the comma; at 12–15s his eyes go back to the road, then once more to you. Hard end mid-drive.""",
    f"""{DLG}
[7–12s] @MOTORISTA (on camera, Brazilian Portuguese, Belo Horizonte accent, plain and patient, like explaining a route, a glance to the road at the comma): "Se Minas tem o que o futuro procura, esse futuro também precisa chegar até os mineiros."
{T.voice_lock('MOTORISTA')}""",
    f"""ACTING — @MOTORISTA (fully invested in the tactic; the work happens in the eyes)
{DIRECT}
EVENT: the driver who carries people to opportunity says where the road has to go.
MOTIVE: every day he drives people to where the opportunity is.
GOAL: that you understand the route.
OBSTACLE: the road needs his eyes.
TACTIC: explain it like a route — hands on the wheel, eyes splitting between the road and you, checking you followed.
MOMENT TO MOMENT: — [0–4s] door, nod to the boy he knows — [4–5s] eyes follow the boy past — [5–6s] eyes rise to you — [7–12s] the line, a glance at the road at the comma — [12–15s] road, then you once more.
LIVING EYES: {EYES} Involuntary detail: his thumb taps the wheel once before the line. A frozen pupil is wrong.
NOT: a speech, letting go of the wheel, turning his body to the camera, a big smile, pointing.

ACTING — @ESTUDANTE: TACTIC greet fast without missing the time; eyes check that the driver remembered him; involuntary detail: he hitches the backpack strap; NOT speaking, NOT looking at the lens.

ACTING — passengers (background): eyes on the window, tired; NOT looking at the lens, NOT speaking.""",
    T.MATCH_FRAME + """

CAMERA — shot 1: observed handheld, the operator seated in the first row on the door side, 1.8 m behind and right of the driver, lens at seated eye height (1.2 m); STAYS PUT and breathes. Shot 2: authored — the MATCH FRAME on a rig fixed to the dashboard right of the wheel, locked to the bus; the bus moves, the camera moves with it; no shake beyond the bus's own vibration.
OPTICS: shot 1 at 47°; shot 2 at 29°; no lens drift inside a shot.
FOCUS: shot 1 on the door and the boy, then the driver's face; shot 2 on the driver's eyes, the bus interior soft behind.
HORIZON: level, with the bus's gentle sway.
NOT: gimbal float, a third shot, a cut-in to the boy, zoom, orbit, an exterior view, centred symmetrical framing.""",
    """GEOMETRY — driver's seat on the bus's left side, folding door on the right; shot 1: driver frame-LEFT, door frame-RIGHT; shot 2: his face just left of centre, the aisle soft behind, the street sliding past the side windows frame-RIGHT once the bus moves.""",
    """PHYSICS & MATERIAL — the folding door swings open on its pneumatic arm with a hiss and a thump; the bus dips slightly as the boy climbs; the backpack swings on one strap; when the brake releases the bus lurches gently forward and everybody sways; the wheel is large and turns under his palms. Nothing floats, nothing loops. OVER-REAL: worn rubber on the steps, a handrail polished by hands, a cracked vinyl seat taped with grey tape, dust on the dashboard, the wheel's worn grip. If any surface looks clean, smooth, plastic, CGI or rendered — WRONG.""",
    T.light_int("the bus's front and door-side windows",
                "no other source inside the bus.",
                "the daylight lights the frame-LEFT side of the faces; the frame-RIGHT side in soft shade; once the bus moves, the light flickers gently as shadows of trees and poles pass."),
    T.FILM_LOOK,
    f"""SOUND — LOCATION SOUND ONLY: the diesel engine idling, then pulling away; the door's pneumatic hiss and thump; footsteps on the steps; the boy's backpack zip jingling; the brake release; tyres on the street, traffic outside, a horn far off; the bell cord ding once (a single tone, not a melody); the engine's hum under his voice. {T.MUSIC_POLICY}""",
    T.WORLD,
    f"""NEGATIVE: the student speaking, a third shot, extra cuts, the driver standing, hands off the wheel while speaking, a parked bus in shot 2, company livery, route number, readable signs, logos, eyes landing off the upper third, gimbal float, {T.NEG_SPINE}.""",
    """[ORDER: 2 shots, 1 hard cut at 4s, 15s — (1, 0–4s) from the first row: door opens, @ESTUDANTE climbs and raises a hand, @MOTORISTA nods — (2, 4–15s) MATCH FRAME on the dashboard: eyes follow the boy, rise and land on the lens at 5–6s, the bus pulls away, his line at 7–12s with a glance at the road, then road and you. Invariants: one cut only; the student silent; eyes landing on the upper third at 45% width; hands on the wheel, bus moving. Look: large-format spherical, mid-key, fine grain, no vignette. Brazilian Portuguese. NO music. NO subtitles, NO text.]""",
)

# ---------------------------------------------------------------- T14
T14 = join(
    contract(7, "ONE continuous take, no cuts", "observed handheld that stays put and breathes"),
    f"""REFERENCES — each reference has ONE job:
@ESTUDANTE — IDENTITY of @ESTUDANTE: face, hair, build, hands and wardrobe — the same clothes as on the bus. 100% matches.
{SCOPE_ID}""",
    f"""WHO IS WHO — READ FIRST, ABSOLUTE:
@ESTUDANTE ({ANCH['ESTUDANTE']}) — the STUDENT: finishes wiring a terminal, turns, speaks once; NEVER smiles broadly, NEVER takes off the hoodie; owns the frame just left of centre.
FACES: his face exists once; two classmates far behind at other benches are distinct soft figures, mouths closed.
CONTACT: nobody touches anyone.""",
    """SCENE — Afternoon in the workshop room of a free technical course for young people in Minas Gerais; @ESTUDANTE is already at an electrical training panel, tightening the last terminal of a circuit with a screwdriver.
THE SOUL OF THE SCENE (play it, never explain it): at 15 he wants to be taken seriously — he finishes the connection with his own hands and then says it straight to you.""",
    f"""{LOCKS_HEAD}
1. The camera STAYS PUT and breathes — WRONG if it travels or pushes in.
2. @ESTUDANTE wears exactly the bus wardrobe: charcoal-grey hoodie, white T-shirt, black jeans — WRONG if anything changes.
3. His eyes are alive and steady on the lens while he speaks — WRONG if glassy.
4. Only @ESTUDANTE speaks, only this line; "Codemig" said as one word — NO music.
5. Daylight from frame-LEFT; no readable text or logo anywhere in the room.""",
    """TIMELINE — ONE continuous take, no cuts, already in progress at the first frame:
BEAT 1 (0–2s) — MS, 47°: @ESTUDANTE at the training panel, frame just left of centre, turning a screwdriver on a terminal; the screw resists, then seats; he tugs the wire once to test it.
BEAT 2 (2–6s) — he turns his head and then his shoulders to the lens and speaks, a small pause at the ellipsis.
BEAT 3 (6–7s) — he holds your eyes, testing whether you believe him. Hard end on the held look.""",
    f"""{DLG}
[2–6s] @ESTUDANTE (on camera, Brazilian Portuguese, Belo Horizonte accent, earnest and steady, "Codemig" said as one word with the stress on the last syllable, a short pause at the ellipsis): "É para isso que a Codemig existe… para fazer essa conexão acontecer."
{T.voice_lock('ESTUDANTE')}""",
    f"""ACTING — @ESTUDANTE (fully invested in the tactic; the work happens in the eyes)
{DIRECT}
MOTIVE: at 15 he wants to be taken seriously.
GOAL: that you believe him.
OBSTACLE: he is fifteen.
TACTIC: finish the job properly in front of you, then hold your gaze and check you believe him.
LIVING EYES: {EYES} Involuntary detail: a quick swallow before he speaks. A frozen pupil is wrong.
NOT: a cheeky grin, a thumbs-up, a teenage slouch-pose, a speech, reading.""",
    """CAMERA — observed handheld, the operator standing 2 m from him at chest height (1.3 m), slightly on the shadow side of his face.
MOVEMENT: the camera STAYS PUT and breathes — a small human tremor, a drift a beat late; no travel.
OPTICS: MS at 47°; natural perspective; no lens drift.
FOCUS: on his hands at the terminal, then on his eyes when he turns.
HORIZON: level.
COMPOSITION: off-centre — his face just left of centre, the panel frame-left, the workshop soft frame-right.
NOT: gimbal glide, push-in, zoom, dolly, orbit, centred symmetrical framing.""",
    """PHYSICS & MATERIAL — the screw resists and then seats with a small snap; the copper wire is stiff and springs back when he tugs it; the screwdriver's handle is scuffed; the hoodie sleeves are pushed up and slide down once. Nothing floats, nothing loops. OVER-REAL: the training panel's scratched grey metal with unreadable worn labels, colour-coded wires with stripped copper ends, a small cut on his knuckle, dust on the window sill, worn white sneakers. If any surface looks clean, smooth, plastic, CGI or rendered — WRONG.""",
    T.light_int("the workshop windows",
                "a small work lamp on the bench ~4000 K, low and secondary, only on the panel.",
                "the daylight lights the frame-LEFT side of his face and the panel; the frame-RIGHT side in soft shade; the room behind falls off a stop, readable."),
    T.FILM_LOOK,
    f"""SOUND — LOCATION SOUND ONLY: the screwdriver's squeak and the small snap of the terminal; the wire's metallic flick; another student's soft tool noise at a far bench; an instructor's voice far off with no words standing out; a fan humming; the street far away. {T.MUSIC_POLICY}""",
    T.WORLD,
    f"""NEGATIVE: different wardrobe from the bus, programme logo, posters with text, readable labels, "Codemig" spelled out letter by letter, a cheeky grin, thumbs-up, camera travelling, push-in, {T.NEG_SPINE}.""",
    """[ORDER: ONE continuous take, 7s, breathing handheld that stays put — (0–2s) he seats the terminal and tests the wire — (2–6s) to the lens, his line with the pause — (6–7s) he holds your eyes. Invariants: camera stays put; the bus wardrobe; living eyes; only his line, "Codemig" as one word. Look: large-format spherical, mid-key, fine grain, no vignette. Brazilian Portuguese. NO music. NO subtitles, NO text.]""",
)

# ---------------------------------------------------------------- T15
T15 = join(
    contract(11, "ONE continuous take, no cuts", "observed handheld that stays put and breathes"),
    f"""REFERENCES — each reference has ONE job:
@ENFERMEIRA — IDENTITY of @ENFERMEIRA: face, hair, build, hands and wardrobe. 100% matches.
{SCOPE_ID}""",
    f"""WHO IS WHO — READ FIRST, ABSOLUTE:
@ENFERMEIRA ({ANCH['ENFERMEIRA']}) — the NURSE: takes the patient's blood pressure, speaks once; NEVER stops caring for the patient, NEVER turns her body to the camera; owns the frame-LEFT half.
PATIENT (unreferenced: a man about 70, white hair, thin, hospital gown, sitting up in the bed) — owns the frame-RIGHT half, partly turned away from the camera; NEVER speaks, mouth closed; watches her.
FACES: each face exists once; no other people in focus.
CONTACT: only her hands on the patient's left arm and the cuff; nobody else touches anyone.""",
    """SCENE — Afternoon in a public hospital ward in Minas Gerais; @ENFERMEIRA is already wrapping a blood-pressure cuff around the PATIENT's upper arm by the window.
THE SOUL OF THE SCENE (play it, never explain it): caring is her job and she does not stop caring to talk to you — her hands and attention stay on him; only at the end does she give you her eyes.""",
    f"""{LOCKS_HEAD}
1. Her hands stay on the patient and the cuff for the whole take — WRONG if she stops the task to talk.
2. Her eyes stay on the patient and the gauge until "também criem oportunidades" (about 7s), then come to the lens and stay alive — WRONG if she looks at the lens earlier or the stare is glassy.
3. Only @ENFERMEIRA speaks, one line; the patient's mouth stays closed.
4. @ENFERMEIRA frame-LEFT, PATIENT frame-RIGHT — WRONG if they swap.
5. Daylight from frame-LEFT — NO music.""",
    """TIMELINE — ONE continuous take, no cuts, already in progress at the first frame:
BEAT 1 (0–2s) — MS two-shot, 47°: @ENFERMEIRA frame-LEFT closes the velcro of the cuff around the PATIENT's upper arm frame-RIGHT, checks it is snug with two fingers, picks up the bulb.
BEAT 2 (2–7s) — she pumps the bulb with steady squeezes, eyes on the gauge and on his face, and starts her line while working.
BEAT 3 (7–9s) — she releases the valve slowly; her eyes come from the gauge to the lens for the end of the line.
BEAT 4 (9–11s) — her eyes go back to the gauge and the patient; she reads the number and nods to him. Hard end mid-task.""",
    f"""{DLG}
[2–9s] @ENFERMEIRA (on camera, Brazilian Portuguese, Belo Horizonte accent, low and calm, the bedside cadence of someone working, breathing with the pumping, the last phrase given to you): "Para fazer com que os recursos essenciais para a transição energética que o mundo precisa, também criem oportunidades para Minas."
{T.voice_lock('ENFERMEIRA')}""",
    f"""ACTING — @ENFERMEIRA (fully invested in the tactic; the work happens in the eyes)
{DIRECT}
EVENT: a nurse explains why she is here without leaving her patient.
MOTIVE: caring is the job, and the job is why it matters.
GOAL: that you understand why she is here.
OBSTACLE: the patient needs her attention now.
TACTIC: keep the hands and the eyes on him while talking; at the end, give you her eyes to check you got it.
MOMENT TO MOMENT: — [0–2s] cuff, two-finger check — [2–7s] pumping, eyes on the gauge and his face, the line flowing as she works — [7–9s] valve released, eyes to you — [9–11s] back to him.
LIVING EYES: {EYES} Involuntary detail: she wets her lips before the last phrase. A frozen pupil is wrong.
NOT: stopping the work, turning to the camera, a TV-presenter smile, a speech, a dramatic hospital scene.

ACTING — PATIENT: TACTIC follow the nurse and trust her; eyes on her face and the cuff; involuntary detail: his fingers curl when the cuff tightens; NOT speaking, NOT looking at the lens.""",
    """CAMERA — observed handheld, the operator standing 2.2 m from them at chest height (1.3 m), on the shadow side of her face.
MOVEMENT: the camera STAYS PUT and breathes — small human tremor, a drift a beat late; no travel.
OPTICS: MS two-shot at 47°; no lens drift.
FOCUS: on her eyes and hands; the patient slightly soft; the ward behind soft.
HORIZON: level.
COMPOSITION: off-centre — her face in the frame-LEFT half on the upper-third line, the patient frame-RIGHT partly turned away, the window light frame-left.
NOT: gimbal glide, push-in, zoom, dolly, orbit, a cut to the gauge, centred symmetrical framing.""",
    """GEOMETRY — the bed along the frame-RIGHT side, the patient sitting up at 60°, his left arm toward her; @ENFERMEIRA standing beside the bed at frame-LEFT, 40 cm from him; the window behind her on frame-LEFT; the camera 2.2 m away at the foot side of the bed.""",
    """PHYSICS & MATERIAL — the velcro rips and grips; the cuff inflates with each squeeze and presses into the thin skin of his arm; the gauge needle climbs and then falls with the slow hiss of the valve; her stethoscope swings slightly as she leans. Nothing floats, nothing loops. OVER-REAL: the worn grey cuff with frayed velcro, the scratched gauge face with unreadable numbers, the thin skin and veins of his arm, a faded hospital blanket, a dented metal bed rail, a small coffee stain on her scrub pocket. If any surface looks clean, smooth, plastic, CGI or rendered — WRONG.""",
    T.light_int("the ward window behind her",
                "no other source on the faces.",
                "the daylight lights the frame-LEFT side of her face and the patient's arm; the frame-RIGHT side of each face in soft shade; the ward behind falls off a stop, readable."),
    T.FILM_LOOK,
    f"""SOUND — LOCATION SOUND ONLY: the velcro rip; the rubber bulb squeezing; the valve's slow hiss; a monitor's soft beep in another bed (single repeated tone, not a melody); a trolley rolling in the corridor; the ward's low murmur with no words standing out. {T.MUSIC_POLICY}""",
    T.WORLD,
    f"""NEGATIVE: stopping the task, looking at the lens before 7s, turning her body to the camera, the patient speaking, swapped sides, a dramatic emergency, blood, readable numbers, hospital logo, camera travelling, push-in, {T.NEG_SPINE}.""",
    """[ORDER: ONE continuous take, 11s, breathing handheld that stays put — (0–2s) she closes the cuff and checks it — (2–7s) pumping, eyes on gauge and patient, her line flowing — (7–9s) valve released, eyes to the lens for the end of the line — (9–11s) back to him, reads the number, nods. Invariants: hands never leave the task; eyes to the lens only at 7s; she left, patient right; only her line. Look: large-format spherical, mid-key, fine grain, no vignette. Brazilian Portuguese. NO music. NO subtitles, NO text.]""",
)

# ---------------------------------------------------------------- T16
T16 = join(
    contract(12, "ONE continuous take, no cuts", "an authored locked frame on a tripod, tight close-up"),
    f"""REFERENCES — each reference has ONE job:
@JOVEM — IDENTITY of @JOVEM: face, skin texture, hair and wardrobe — use the close-up skin detail anchor. 100% matches.
@PICO — WORLD: the same summit as the opening; only its soft, layered hills appear behind him.
{SCOPE_ID} @PICO supplies the background landscape ONLY — its light is replaced by the LIGHT block.""",
    f"""WHO IS WHO — READ FIRST, ABSOLUTE:
@JOVEM ({ANCH['JOVEM']}) — the PROTAGONIST: holds still, speaks two sentences; NEVER moves his head out of the frame, NEVER smiles broadly; his face fills the frame just left of centre.
FACES: his face exists once; nobody else.""",
    """SCENE — The same summit at the same late-afternoon hour; @JOVEM, in a very tight close-up, is already looking at you; the sea of hills is a soft haze behind him.
THE SOUL OF THE SCENE (play it, never explain it): now he has decided. "O minério é nosso" claims it; "O futuro também" invites you in.""",
    f"""{LOCKS_HEAD}
1. ONE continuous take, the camera LOCKED in a very tight close-up — WRONG if it moves, cuts or widens.
2. His eyes stay on the lens and alive from start to finish, both eyes sharp — WRONG if glassy, watery or looking away.
3. Real skin in detail: pores, stubble, the scar through the left eyebrow — WRONG if smooth or retouched.
4. Only @JOVEM speaks, these two sentences, with a breath between them.
5. Sun from frame-LEFT — NO music.""",
    """TIMELINE — ONE continuous take, no cuts, already in progress at the first frame:
BEAT 1 (0–1s) — CU, 18°, locked: @JOVEM's face from the eyebrows to the chin, just left of centre, eyes already on the lens; a breath in.
BEAT 2 (1–6s) — he speaks the first sentence, steady, close, the weight on "nossa terra" both times.
BEAT 3 (6–7s) — a breath; his eyes check both of yours.
BEAT 4 (7–8s) — "O minério é nosso." — a claim, the jaw set.
BEAT 5 (8–10s) — a beat, then "O futuro também." — an offer, the face opening slightly.
BEAT 6 (10–12s) — he holds your eyes, looking for the "yes". Hard end on the held look.""",
    f"""{DLG}
[1–6s] @JOVEM (on camera, Brazilian Portuguese, light Minas Gerais interior accent, low and close, steady, the stress on "nossa terra" both times): "Para transformar a força que vem da nossa terra em mais desenvolvimento para a nossa terra."
[7–10s] @JOVEM (on camera, Brazilian Portuguese, light Minas Gerais interior accent, the first sentence set like a claim, a short beat, the second softer like an offer): "O minério é nosso. O futuro também."
{T.voice_lock('JOVEM')}""",
    f"""ACTING — @JOVEM (fully invested in the tactic; the work happens in the eyes)
{DIRECT}
EVENT: the man from the opening comes back having decided.
MOTIVE: everything he showed you comes down to this.
GOAL: your "yes".
OBSTACLE: a slogan would kill it.
TACTIC: look at you from close up and search both of your eyes for the yes; claim it, then invite you in.
MOMENT TO MOMENT: — [1–6s] steady, eyes moving between your two eyes — [6–7s] a check — [7–8s] he claims it, jaw set — [8–10s] he offers it, the face opening — [10–12s] he waits.
LIVING EYES: {EYES} Involuntary detail: a small tightening at the corner of his mouth after "nosso". The low sun puts a small live point in his frame-left eye; a frozen pupil is wrong.
NOT: a slogan delivery, a broad smile, a wink, a nod, tears, raising his voice.""",
    """CAMERA — authored: a locked tripod at his eye height (1.65 m), 1.3 m from his face, frontal.
MOVEMENT: the camera STAYS PUT for the whole take — no drift, no push, no shake.
OPTICS: CU at 18°, the face from eyebrows to chin; long-lens compression; no zoom, no lens drift.
FOCUS: on both eyes; the hills behind melted into soft layered haze.
HORIZON: level.
COMPOSITION: off-centre — his face just left of centre, the eyes on the upper-third line, the soft hills frame-right.
NOT: handheld, push-in, pull-back, zoom, dolly, drone, orbit, centred symmetrical framing.""",
    """PHYSICS & MATERIAL — the wind from frame-left moves a few hairs at his temple and the edge of his collar; his breath is visible only as the movement of his lips and nostrils; his skin catches the light unevenly. Nothing floats, nothing loops. OVER-REAL: pores and fine sun lines at the eyes, three-day stubble with a few grey hairs, the thin scar through the left eyebrow, sun-cracked lips, a small mole on the cheek, fine dust in the eyebrow hairs. If any surface looks clean, smooth, plastic, CGI or rendered — WRONG.""",
    T.LIGHT_EXT,
    T.FILM_LOOK,
    f"""SOUND — LOCATION SOUND ONLY: wind across the open summit, steady and quiet; dry grass hissing; his breath before each sentence; after "O futuro também.", only the wind. {T.MUSIC_POLICY}""",
    T.WORLD,
    f"""NEGATIVE: camera movement, a cut, widening the frame, smooth retouched skin, missing scar, watery eyes, tears, a broad smile, a wink, a nod, slogan delivery, looking away, {T.NEG_SPINE}.""",
    """[ORDER: ONE continuous take, 12s, locked tight CU 18° — (0–1s) eyes on the lens, a breath — (1–6s) the first sentence — (6–7s) a breath — (7–8s) "O minério é nosso." — (8–10s) "O futuro também." — (10–12s) he holds your eyes. Invariants: locked frame; living eyes on the lens; real skin with the scar; only his two sentences; sun frame-LEFT. Look: large-format spherical, mid-key, red-ochre earth, fine grain, no vignette. Brazilian Portuguese. NO music. NO subtitles, NO text.]""",
)
