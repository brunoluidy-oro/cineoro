# CODEMIG · VT 60" — gerações v2 (prompts CINEORO completos).
# Cada prompt é uma ilha: monta a espinha inteira e cola os templates de templates.py.
# Gramática v2: câmera na mão sempre; subações em close; a fala no plano mais aberto, entre cortes.

import templates as T

ANCH = {
    "JOVEM": "25, Brazilian, mixed-race light-brown skin, lean, short black curly hair, ears that stick out slightly, light patchy stubble, a small mole on his left cheek, rust-red cotton overshirt open over a white T-shirt, black slim jeans, brown leather hiking boots with black toe caps, charcoal-grey backpack",
    "ALUNO": "10, Black Brazilian boy, slim, dark brown skin, short tight black curls, soft oval face, large dark brown eyes with long lashes, sage-green school T-shirt with no emblem, black shorts, black strapped sport sandals",
    "PROFESSORA": "40, white Brazilian woman, medium build, dark brown hair centre-parted in a low bun with loose strands framing the face, dense freckles across the nose and cheeks, mauve satin blouse with a band collar tucked into charcoal-grey straight-leg trousers, brown flats, a silver wristwatch on the left wrist",
    "HOMEM_EV": "34, mixed-race Brazilian businessman, light olive-tan skin, fit, short black hair swept up and back with tapered sides, thick dark eyebrows, short full dark beard and moustache, slim dark navy suit, light-blue dress shirt open at the collar with no tie, silver steel watch on the left wrist, gold ring, brown leather lace-up shoes",
    "OPERARIO": "40, mixed-race (pardo) Brazilian man, heavyset and broad-shouldered, round full face with freckled cheeks, close-shaved head, short full black beard flecked with grey, white hard hat with no logo, clear wraparound safety glasses, orange ear muffs around his neck, dark charcoal-grey flame-retardant coverall with silver reflective strips over the shoulders, chest, forearms and shins, grey knit work gloves, black leather safety boots",
    "PESQUISADORA": "30, Black Brazilian woman, deep brown skin, slim, black natural hair pulled up into a high twisted bun, high cheekbones, broad nose, full lips, small gold stud earrings, long buttoned white lab coat, black wide-leg trousers, purple nitrile gloves, clear safety glasses with a black brow bar and black arms",
    "DONO": "60, white Brazilian man, solid build, broad deeply lined face with age spots, large nose and ears, grey-hazel eyes, thick bushy white-grey moustache covering the upper lip, short white hair thinning on top, cream short-sleeved camp-collar shirt with a chest pocket, very dark navy knee-length waist apron, dark grey trousers, tan leather loafers",
    "AGRICULTORA": "40, mixed-race Brazilian woman, slim, warm brown skin, long face with high cheekbones and fine lines, long black hair in a single thick braid worn over her left shoulder, tan felt wide-brim hat with brown leather trim sitting just above the eyebrows, sage-green long-sleeved button-up shirt with two flap chest pockets worn untucked, dark indigo jeans, dark brown lace-up leather work boots, tortoiseshell sunglasses hooked on the shirt front",
    "FUNCIONARIO": "30, mixed-race Brazilian man, medium build, medium brown skin, short black hair, thick straight eyebrows, broad nose, full lips, clean-shaven with a faint stubble shadow, glossy white hard hat with black chin strap fastened and no logo, clear wraparound safety glasses, orange high-visibility vest with grey reflective strips over a long-sleeved dark charcoal collared work shirt worn untucked, black cargo work trousers, grey padded work gloves, black lace-up work boots",
    "MAE": "29, Brazilian woman, warm light-brown skin with a golden undertone and freckles across the nose and cheeks, slim, long chestnut-brown hair with caramel highlights in loose waves swept over one shoulder from a deep side part, almond-shaped dark brown eyes, small straight nose, soft full lips, a round textured gold stud earring, a thin gold necklace with a tiny pendant, ivory fine-rib long-sleeved knit top with a scoop neck and the sleeves pushed up, high-waisted sage-green linen wide-leg cropped trousers, ivory canvas slip-on shoes",
    "TORCEDORA": "22, Black Brazilian woman, deep brown skin with a warm glow, athletic, hair slicked straight back with glossy laid edges and a deep side part into a sleek low bun at the nape, forehead and ears fully visible, thick defined eyebrows, broad nose with a tiny gold nose stud, full lips with a berry gloss, large gold hoop earrings, a washed-terracotta velour football jersey with a cream polo collar with red stripes and cream cuffs and a plain chest with no emblem, tucked into high-waisted dark chocolate-brown wide-leg jeans, sand-coloured sneakers, a small olive-tan crossbody pouch on a chain",
    "MOTORISTA": "52, Black Brazilian man, medium-brown skin, heavy-set with a round belly, close-cropped salt-and-pepper hair, round full-cheeked face, broad nose, clean-shaven, pale grey short-sleeved open-collar uniform shirt with two flap chest pockets and nothing written on it, worn untucked, dark navy trousers, black loafers, a steel wristwatch on the left wrist",
    "ESTUDANTE": "15, mixed-race Brazilian teenage boy, light olive-tan skin, thin and tall for his age, short black hair cropped close all over, ears slightly sticking out, a faint teenage moustache and light chin stubble, dark charcoal (almost black) pullover hoodie with a kangaroo pocket, a white T-shirt hem showing below it, black skinny jeans, white canvas low-top sneakers",
    "ENFERMEIRA": "42, mixed-race Brazilian woman, medium-brown skin, slim-to-medium build, black hair centre-parted and slicked back into a low bun, a small mole on the forehead just above the brow line, white short-sleeved scrub tunic with a notched mandarin collar, a chest pocket holding a small plain ID badge with nothing written and two hip pockets, a black stethoscope around her neck, white straight scrub trousers, white flat shoes",
}

SCOPE_ID = ("REFERENCE SCOPE: character references supply face, hair, build, hands and wardrobe (with any safety equipment) ONLY — "
            "IGNORE their grey backdrop, studio lighting, exposure and colour grade.")

DLG = ("DIALOGUE — only these lines are spoken, each by the named character, lip-synced; NO "
       "dubbing, NO voice-over, NO narration, NO subtitles — the words exist only as sound. Every "
       "mouth not speaking stays closed.")

LOCKS_HEAD = "ABSOLUTE LOCKS — break one and the take is WRONG, regenerate:"
REAL = "Nothing floats, nothing loops. If any surface looks plastic, CGI or rendered — WRONG."


def contract(seconds, takes, camera, dialogue=True, extra=""):
    lang = T.LANG if dialogue else "no dialogue — no one speaks"
    return (f"CONTRACT — Live-action photoreal film footage, {T.ASPECT}, {seconds} seconds total, "
            f"{takes}, {camera}, real-time motion{extra}, {lang}. NO music, NO score. "
            f"{T.TEXT_POLICY}.")


def line(a, b, tag, text):
    return f'[{a}–{b}s] @{tag} (on camera, Brazilian Portuguese): "{text}"'


def dialogue(*lines_and_tags):
    lines = [x for x in lines_and_tags if x.startswith("[")]
    tags = [x for x in lines_and_tags if not x.startswith("[")]
    return "\n".join([DLG] + lines + [T.voice_lock(t) for t in tags])


def acting(tag, motive, tactic, eyes_job, involuntary, extra_not=""):
    nots = "a solemn or serious face, a speech, a stiff advertising grin"
    if extra_not:
        nots += ", " + extra_not
    return f"""ACTING — @{tag} (fully invested in the tactic; the work happens in the eyes)
{T.SHARED_ACTING}
MOTIVE: {motive}
TACTIC: {tactic}
EYES: {eyes_job} {T.EYES} Involuntary detail: {involuntary}. A frozen pupil is wrong.
NOT: {nots}."""


def card(task, dur, attach, notes):
    lines = [
        "GENERATION CARD",
        f"Modelo: Seedance 2.5 (Higgsfield) · Tarefa: {task}",
        f"Duração: {dur}s (= timeline) · Aspecto: {T.ASPECT} · Resolução: draft 480p → final 1080p · Áudio: on",
        "Anexar nesta ordem:",
    ]
    lines += [f"  {i}) {a}" for i, a in enumerate(attach, 1)]
    lines.append(f"Notas: {notes}")
    return "\n".join(lines)


def join(*blocks):
    return "\n\n".join(b.strip() for b in blocks if b)


def timeline(n, cuts, shots):
    head = (f"TIMELINE — {n} shots, {len(cuts)} hard cuts; cuts only at the specified points, the "
            "camera adds no cuts of its own:") if n > 1 else \
        "TIMELINE — ONE continuous take, no cuts, already in progress at the first frame:"
    return head + "\n" + "\n".join(shots)


def cut_list(cuts):
    return ", ".join(f"{c}s" for c in cuts)


# ---------------------------------------------------------------- T01-A (aberto, centralizado, ele vira de frente)
T01A = join(
    contract(5, "ONE continuous take, no cuts", "handheld, drifting slowly, wide and centred", dialogue=False),
    f"""REFERENCES — each reference has ONE job:
@JOVEM — IDENTITY of @JOVEM: face, hair, build, hands, wardrobe and backpack. 100% matches.
{SCOPE_ID}""",
    f"""WHO IS WHO — READ FIRST, ABSOLUTE:
@JOVEM ({ANCH['JOVEM']}) — the PROTAGONIST: looks at the hills, turns all the way round to face the camera; NEVER speaks in this take, NEVER walks away, NEVER raises his arms; stands on the vertical centre line of the frame.
FACES: his face exists once; nobody else in the frame.""",
    """SCENE — Late afternoon on a mountain summit in Minas Gerais, Brazil. @JOVEM is already standing near the edge with his back to the camera, centred in a wide frame, looking over a sea of green hills that runs in layers to the horizon on both sides of him.
THE SOUL OF THE SCENE (play it, never explain it): he loves where he comes from and is about to tell you why.""",
    f"""{LOCKS_HEAD}
1. ONE continuous handheld take, no cuts — WRONG if it cuts or the camera is locked.
2. WIDE and CENTRED the whole take: @JOVEM on the vertical centre line, his entire body from head to boots inside the frame, standing about 16 m from the lens, filling only about a fifth of the frame height, with a band of rock ground visible in the lower frame in front of him — WRONG if the shot is a medium shot, over-the-shoulder, cropped at the body, he sits off-centre, or the ground is not visible.
3. The turn is QUICK and COMPLETE: he spins round in about one second (2–3s), and from 3s his body and shoulders are square to the camera and his eyes on the lens, held until the end — WRONG if the turn is slow, stops half-way, or ends at three-quarter or in profile.
4. NO dialogue — his mouth stays closed — WRONG if he speaks.
5. Sun from frame-LEFT — NO music.""",
    timeline(1, [], [
        "BEAT 1 (0–2s) — EWS, 84°, handheld from 16 m behind him with the lens low, about 60 cm above the rock, drifting slowly, a band of lichen-covered rock ground in the lower frame: @JOVEM centred, back to camera, his backpack on both shoulders, boots on the rock, the layered hills and a wide sky around him; his eyes travel the horizon.",
        "BEAT 2 (2–3s) — a quick, lively turn: he spins all the way round in about one second, boots re-planting on the rock, and lands square to the camera, smiling, eyes on the lens.",
        "BEAT 3 (3–5s) — he holds, square to the camera, centred, smile and eyes on the lens, the backpack straps on both shoulders. Hard end on the held look.",
    ]),
    """ACTING — @JOVEM: TACTIC take in the view he loves, then turn to share it with you; eyes on the far ridges, then on the lens; involuntary detail: the wind lifts his collar; NOT a heroic pose, open arms, a solemn face.""",
    T.handheld() + """
COMPOSITION (the one deliberate symmetrical frame of the film): a very wide, low frame — @JOVEM small on the vertical centre line with his entire body in frame, rock ground across the lower frame, the hills falling away evenly on both sides, the horizon on the upper third, sky above.""",
    """GEOMETRY — the camera 16 m from @JOVEM, lens about 60 cm above the rock; he stands 1 m back from the rock edge on the centre line; hills 2–10 km beyond on both sides, the farthest dissolving into haze.""",
    """PHYSICS & MATERIAL — the wind from frame-left combs the grass and moves his overshirt; his boots shift on the rock when he turns; the backpack sways with the turn. """ + REAL + """ MATERIAL TRUTH: lichen on the grey rock, the weave of his overshirt, the backpack's fabric and straps.""",
    T.LIGHT_EXT,
    T.FILM_LOOK,
    f"""SOUND — LOCATION SOUND ONLY: strong wind across the open summit, steady with gusts (it carries into the next shot); dry grass hissing; his boots on grit as he turns; a hawk far off. {T.MUSIC_POLICY}""",
    T.WORLD,
    f"""NEGATIVE: a slow turn, a half-finished turn, speaking, a cut, over-the-shoulder framing, a medium shot, a cropped body, a camera at chest or eye height, no ground in frame, a close or tight framing, a figure off-centre, a half-finished turn, a three-quarter or profile ending, a dolly or drone move, a second person, raised arms, sun disc in frame, {T.NEG_SPINE}.""",
    """[ORDER: ONE handheld take, 5s, extra-wide, low camera, centred, 21:9 — (0–2s) his back to camera on the centre line, small, entire body in frame, rock ground in the lower frame, the hills on both sides — (2–3s) a quick one-second turn all the way round to face the camera, smiling — (3–5s) he holds square to the camera, eyes on the lens; hard end. Invariants: extra-wide, low lens with ground visible, centred, entire body in frame; the turn is quick (about one second) and complete; no dialogue; sun frame-LEFT. Look: 35mm color negative, warm halation, lifted blacks, organic grain. NO music. NO subtitles, NO text.]""",
)

# ---------------------------------------------------------------- T01-B (bloqueio 3D: close → descida → sala), duas versões
def t01b(short):
    total = 9 if short else 18
    L = dict(j="0–3", a="5–6", p="6–8", nospeech="3–5") if short else dict(j="0–3", a="12–13", p="13–15", nospeech="3–12")
    ramp = (" SPEED RAMP: the descent leaves the man at once, peaks through earth, ore and beams with heavy motion blur, and decelerates smoothly into the landing; about 1.5 s of screen time.") if short else ""
    b1 = "BEAT 1 (0–3s) — CU, 47°, handheld, frontal and centred: @JOVEM already facing the lens, shoulders square, mid-smile, exactly as at the last frame of the previous wide take (the edit cuts on that look); he speaks at once, the line fills the 3 s, and the instant it ends the camera sinks."
    landing = "lands at a seated child's eye height on a medium shot of @ALUNO at his desk in the centre of the frame."
    if short:
        beats = [b1,
            "BEAT 2 (3–5s) — the descent, level and facing forward, as a speed ramp: down his chest, hands, legs and boots on the lichen rock, into the earth in cross-section (roots, red soil, rock, a seam of iron ore), out through steel roof beams, past a white ceiling fan ON and spinning fast, into the bright classroom; it decelerates and " + landing,
            "BEAT 3 (5–6s) — handheld settles; @ALUNO answers, looking toward the front of the room; mid-line @PROFESSORA enters from frame-RIGHT, crouching beside his desk, and the camera makes a slight handheld pan right to frame her.",
            "BEAT 4 (6–8s) — @PROFESSORA, crouched, face turned toward him, speaks to HIM in a correcting teacher's tone; @ALUNO looks at her.",
            "BEAT 5 (8–9s) — @ALUNO keeps looking at her, nods in agreement and smiles. Hard end on the smile."]
        order_t = "(0–3s) @JOVEM's line, then the camera sinks at once — (3–5s) speed-ramp descent: body, earth, ore, beams, spinning fan, lands on @ALUNO — (5–6s) \"É futuro.\", @PROFESSORA crouches in from frame-RIGHT — (6–8s) \"Minério não é só minério.\" to him — (8–9s) he nods, smiles"
    else:
        beats = [b1,
            "BEAT 2 (3–5s) — the camera sinks straight down, level and facing forward: his chest, overshirt, hands, legs and boots on the lichen rock slide up past the lens.",
            "BEAT 3 (5–8s) — below the ground line: the earth in cross-section — roots, red soil, rock sliding upward — then a dark seam of banded iron ore with metallic glints.",
            "BEAT 4 (8–10s) — out of the ore, steel roof beams rise past the lens; the camera passes between them and down through the gridded classroom ceiling beside a white ceiling fan that is ON, blades spinning fast.",
            "BEAT 5 (10–12s) — down into the bright classroom, decelerating, desks with seated students rising into view; it " + landing,
            "BEAT 6 (12–13s) — handheld settles; @ALUNO answers, looking toward the front of the room; mid-line @PROFESSORA enters from frame-RIGHT, crouching beside his desk, and the camera makes a slight handheld pan right to frame her.",
            "BEAT 7 (13–15s) — @PROFESSORA, crouched, face turned toward him, speaks to HIM in a correcting teacher's tone; @ALUNO looks at her.",
            "BEAT 8 (15–18s) — @ALUNO keeps looking at her, nods in agreement and smiles; the two hold. Hard end on the smile."]
        order_t = "(0–3s) @JOVEM's line, then the camera sinks at once — (3–5s) down his body — (5–8s) earth and ore — (8–10s) beams, classroom ceiling, spinning fan — (10–12s) lands on @ALUNO — (12–13s) \"É futuro.\", @PROFESSORA crouches in from frame-RIGHT — (13–15s) \"Minério não é só minério.\" to him — (15–18s) he nods, smiles"
    return join(
        contract(total, "ONE continuous take, no cuts", "one continuous level vertical descent that follows the attached 3D blocking video, handheld" + (", with a speed ramp in the descent" if short else ""), extra=" (speech only when the camera is not travelling)"),
        f"""REFERENCES — each reference has ONE job:
@JOVEM — IDENTITY of @JOVEM: face, hair, build, hands, wardrobe, backpack. 100% matches.
@PICO_FRAME — PLACE AND WARDROBE STATE of the summit: lichen rock, green hills, sky, low warm sun from frame-left, and how his rust-red open overshirt, white T-shirt, black jeans, boots and backpack sit on him. It is the last frame of the previous shot; beat 1 is the same place and clothes seen close.
@ALUNO — IDENTITY of @ALUNO: face, hair, build, hands, wardrobe. 100% matches.
@PROFESSORA — IDENTITY of @PROFESSORA: face, hair, build, hands, wardrobe. 100% matches.
@Video1 — MOTION ONLY: the camera path, framing and timing of this 3D blocking (close-up, level descent through body, ground, ore and beams, past the fan, landing on the seated boy, slight pan right as the teacher crouches in). Take NOTHING else: ignore its flat colours, low-poly shapes and every word in it.
{SCOPE_ID} @PICO_FRAME supplies place, light and wardrobe ONLY — not its wide framing, not his pose, not a start frame, nothing of his face (his face comes from the @JOVEM sheet).""",
        f"""WHO IS WHO — READ FIRST, ABSOLUTE:
@JOVEM ({ANCH['JOVEM']}) — the PROTAGONIST on the summit: one line in close-up, then the camera leaves him.
@ALUNO ({ANCH['ALUNO']}) — the STUDENT: seated at his desk, centre of frame, facing the front of the room where the whiteboard is (behind the camera, never in frame); an open notebook, pencil case and textbook on his desk; answers, then looks at the teacher and agrees with a smile; NEVER stands.
@PROFESSORA ({ANCH['PROFESSORA']}) — the TEACHER: enters from frame-RIGHT crouching beside his desk, three-quarter view from behind-side, face turned toward HIM; speaks to him, never to the lens; her hand rests on the edge of his desk; NEVER sits.
CLASSMATES: about ten students, each at his own desk in rows, same light-green school T-shirt, each desk with notebook, pencil case and textbook, all facing the front; distinct faces; silent; soft.
FACES: each face exists once; no twins, no clones.""",
        """SCENE — Late afternoon on a mountain summit in Minas Gerais, Brazil, @JOVEM in close-up, looking at you. When he has spoken, the camera sinks straight down through the ground he stands on — earth, iron ore, the steel of a roof — into a bright, recently built Brazilian public school classroom, where a student answers and his teacher crouches in beside him.
THE SOUL OF THE SCENE (play it, never explain it): earth, ore, steel, school — one chain, one movement; the man who loves the land hands the film to the boy who is its future.""",
        f"""{LOCKS_HEAD}
1. ONE continuous take, ONE level vertical descent following @Video1 — WRONG if it cuts, tilts down or flies like a drone.
2. The camera starts sinking the INSTANT @JOVEM finishes his line — WRONG if he holds after it or the camera sinks before it ends.
3. No speech while the camera travels ({L['nospeech']}s): lines only at {L['j']}s (@JOVEM), {L['a']}s (@ALUNO), {L['p']}s (@PROFESSORA), each in the right mouth.
4. NO sound effects of any kind — WRONG if any rumble, whoosh, hum, scraping or stones are heard.
5. The ceiling fan is ON and visibly spinning — WRONG if still.
6. @ALUNO centred; @PROFESSORA enters from frame-RIGHT, crouched, mid-line, speaks to HIM not the lens; he looks at her, nods, smiles — WRONG if she enters from the left or looks at the lens.
7. NO whiteboard or blackboard in frame, none behind the boy; handheld; light from frame-LEFT — NO music.""",
        timeline(1, [], beats),
        dialogue(f'[{L["j"]}s] @JOVEM (on camera, Brazilian Portuguese, speaking up over the wind): "Em Minas, terra não é só terra."',
                 f'[{L["a"]}s] @ALUNO (on camera, Brazilian Portuguese): "É futuro."',
                 f'[{L["p"]}s] @PROFESSORA (on camera, Brazilian Portuguese, in the tone of a teacher gently correcting, speaking to the boy): "Minério não é só minério."',
                 "JOVEM", "ALUNO", "PROFESSORA"),
        """ACTING — happy and proud of what they say; pupils search, settle and drift; a frozen pupil is wrong.
@JOVEM: TACTIC say it like good news to a friend; eyes on yours; NOT a heroic pose, a solemn face.
@ALUNO: TACTIC answer simply, then turn to the teacher, take her correction with a nod and a smile; NOT a cute pose, a child-actor performance.
@PROFESSORA: TACTIC correct and complete his answer kindly, crouched to his level, eyes on him; NOT lecturing, pointing a finger, looking at the lens.
Classmates: follow the exchange, silent, NOT looking at the lens.""",
        """CAMERA — follows @Video1's path and timing, handheld (small human sway, late corrections, never a mechanical glide); level and facing forward the whole descent, never tilting.""" + ramp + """ After landing it stays handheld and makes one slight pan right to frame @PROFESSORA as she enters.
OPTICS: 47° throughout; no zoom, no lens drift. FOCUS: @JOVEM's eyes in beat 1; whatever passes the lens in the descent; then the faces of the exchange.
NOT: a cut, a tilt down, a drone, a CGI fly-through, a zoom, a locked tripod frame.""",
        """GEOMETRY — classroom: windows along the frame-LEFT wall; the whiteboard is on the front wall behind the camera, out of frame; @ALUNO at a second-row desk, centre of frame, 1.6 m from the lens; desks with seated students to both sides, soft; @PROFESSORA crouching at frame-RIGHT, 50 cm from his desk.""",
        """PHYSICS & MATERIAL — strong wind tugs at his collar and hair; in the descent soil and stones fall past the lens at the speed of the movement, roots sway, the ore glints; the white ceiling fan spins fast, blades motion-blurred. """ + REAL + """ MATERIAL TRUTH: the weave of his overshirt, roots with soil, banded hematite, matte steel, new laminate desks with notebooks and textbooks.""",
        """LIGHT — MOTIVATED, one dominant natural source per place with real falloff and soft-edged shadows.
SUMMIT: low sun ~4300 K from frame-LEFT. THE GROUND: as if sliced open in that same soft daylight — readable, never black, no invented lamp. CLASSROOM: window daylight from frame-LEFT ~5600 K; the room a stop darker; corners allowed to fall into shade.
NOT: a headlamp, glowing underground light, flat ceiling-panel key, frontal fill.""",
        T.FILM_LOOK,
        f"""SOUND — NO SOUND EFFECTS ANYWHERE: nothing designed or synthetic during the descent — no rumble, whoosh, scraping, stones, metallic hum, riser or impact. Only: strong wind across the open summit under his line ({L['j']}s), steady with gusts, dropping to near silence as the camera sinks below the ground line; then, from the landing, the quiet natural room tone of a classroom — the soft whir of the spinning fan, a faint student murmur that drops during the lines. {T.MUSIC_POLICY}""",
        T.WORLD,
        f"""NEGATIVE: sound effects, rumble, whoosh, text or labels from the blocking video, low-poly shapes, a cut, a tilt down, speech during the descent, a classmate speaking, the teacher entering from the left or looking at the lens, a stopped fan, a whiteboard or blackboard in frame or behind the boy, an empty classroom, a CGI cross-section, glowing ore, a black frame, {T.NEG_SPINE}.""",
        f"""[ORDER: ONE continuous take, {total}s, following @Video1, handheld{', speed-ramp descent' if short else ''} — {order_t}. Invariants: one level descent; sinks the instant his line ends; no speech while travelling; NO sound effects; fan ON; teacher enters from frame-RIGHT; no whiteboard in frame. Look: 35mm color negative, warm halation, lifted blacks, organic grain. Brazilian Portuguese. NO music. NO subtitles, NO text.]""",
    )


T01B_LONG = t01b(False)
T01B_SHORT = t01b(True)

# ---------------------------------------------------------------- Revezamento
def rev_locks(n, cuts, tag, text, extra=""):
    return f"""{LOCKS_HEAD}
1. Exactly {n} shots with hard cuts at {cut_list(cuts)} — WRONG if there are extra cuts.
2. In EVERY shot the handheld camera travels sideways from frame-left to frame-right at the same steady pace — WRONG if it stops, reverses, pushes in or glides.
3. The close-ups show hands and objects only; @{tag} speaks only in the medium-wide shot, eyes alive on the lens — WRONG if glassy.
4. Only @{tag} speaks, only "{text}" — every other mouth closed.{extra}
5. Light from frame-LEFT — NO music."""


T04 = join(
    contract(10, "4 shots with 3 hard cuts at 3s, 5s and 8s", "handheld travelling sideways from frame-left to frame-right in every shot"),
    f"""REFERENCES — each reference has ONE job:
@HOMEM_EV — IDENTITY of @HOMEM_EV: face, hair, build, hands and wardrobe. 100% matches.
{SCOPE_ID}""",
    f"""WHO IS WHO — READ FIRST, ABSOLUTE:
@HOMEM_EV ({ANCH['HOMEM_EV']}) — the CAR OWNER: plugs in the charger, speaks once, pats the car; NEVER poses beside the car, NEVER walks out of frame before shot 4.
FACES: his face exists once; passers-by far behind are distinct soft Brazilian figures.
CONTACT: nobody touches him.""",
    """SCENE — Late afternoon at the charging bays of a modern office building's open-air parking lot in Belo Horizonte, Brazil; flowering ipê trees along the edge. @HOMEM_EV is already plugging his compact electric car in.
THE SOUL OF THE SCENE (play it, never explain it): he did the maths, switched to electric and loves it — he tells you like someone who found a great deal.""",
    rev_locks(4, [3, 5, 8], "HOMEM_EV", "É a possibilidade de um mundo mais verde,"),
    timeline(4, [3, 5, 8], [
        "SHOT 1 (0–3s) — ECU, 47°, lens 40 cm from the car: his hand guides the charging connector into the car's port; the first push meets resistance, he lines it up and pushes again until it seats with a click. HARD CUT.",
        "SHOT 2 (3–5s) — CU, 47°: the light ring around the charging port glows on; his hand lets go of the connector and the thick cable settles. HARD CUT.",
        "SHOT 3 (5–8s) — MWS (from the knees up, the car and the trees around him), 63°: @HOMEM_EV standing by the car at the right third, turns to the lens and speaks at 5–8s, a pleased half-smile; he drifts toward the centre as the camera passes. HARD CUT.",
        "SHOT 4 (8–10s) — CU, 47°: his hand pats the car roof twice, satisfied, and he steps off frame-right. Hard end mid-step.",
    ]),
    dialogue(line(5, 8, "HOMEM_EV", "É a possibilidade de um mundo mais verde,"), "HOMEM_EV"),
    acting("HOMEM_EV", "he made a smart choice and it paid off.",
           "share it casually, with the pleasure of someone who found a good deal — check from the corner of his eye that you're convinced.",
           "on the connector, then a sidelong look to the lens.",
           "he blows a short pleased breath through his nose", "a salesman pitch, a thumbs-up"),
    T.REV_CAMERA,
    """PHYSICS & MATERIAL — the connector is heavy, its thick cable stiff and coiling; the port flap springs open; the connector seats only on the second push; ipê blossoms drift in the light wind. """ + REAL + """ MATERIAL TRUTH: the satin paint of the car, a fingerprint on the port cover, the rubber cable sheath, the brushed-steel charging post with a dark blank screen, fresh painted parking lines, pink ipê petals on the asphalt.""",
    T.LIGHT_EXT,
    T.FILM_LOOK,
    f"""SOUND — LOCATION SOUND ONLY: city traffic two streets away; the cable dragging; the port flap; the latch click at 2s; a soft single beep from the charger; his footstep; birds in the ipê trees. {T.MUSIC_POLICY}""",
    T.WORLD,
    f"""NEGATIVE: car badge, readable charger screen, posing beside the car, a thumbs-up, speaking in the close-ups, the camera stopping, push-in, extra cuts, {T.NEG_SPINE}.""",
    """[ORDER: 4 shots, 3 hard cuts at 3s, 5s and 8s, 10s, handheld travelling left to right in every shot — (1, 0–3s) ECU: the connector seats on the second push — (2, 3–5s) CU: the port light glows on, his hand lets go — (3, 5–8s) medium-wide: he turns to the lens and says his line, pleased — (4, 8–10s) CU: he pats the roof twice and steps off. Invariants: constant lateral travel; hands only in the close-ups; living eyes on the lens; only his one line. Look: 35mm color negative, warm halation, lifted blacks, organic grain. Brazilian Portuguese. NO music. NO subtitles, NO text.]""",
)

T05 = join(
    contract(9, "4 shots with 3 hard cuts at 3s, 5s and 7s", "handheld travelling sideways from frame-left to frame-right in every shot"),
    f"""REFERENCES — each reference has ONE job:
@OPERARIO — IDENTITY of @OPERARIO: face, build, hands, wardrobe and safety equipment. 100% matches.
{SCOPE_ID}""",
    f"""WHO IS WHO — READ FIRST, ABSOLUTE:
@OPERARIO ({ANCH['OPERARIO']}) — the STEELWORKER: runs the line from the console, speaks once; NEVER removes helmet or glasses, NEVER walks out of frame.
FACES: his face exists once; two colleagues far behind are distinct soft figures, mouths closed.
CONTACT: nobody touches anyone.""",
    """SCENE — Afternoon inside a modern, automated steel rolling mill in Minas Gerais, Brazil: clean painted floor lanes, a glowing steel slab moving through the rollers. @OPERARIO is already at his console beside the line.
THE SOUL OF THE SCENE (play it, never explain it): he has watched this plant become one of the most efficient anywhere and is proud to show it off.""",
    rev_locks(4, [3, 5, 7], "OPERARIO", "de uma indústria mais eficiente,",
              "\n4b. Full safety equipment on in every shot: hard hat, glasses, gloves."),
    timeline(4, [3, 5, 7], [
        "SHOT 1 (0–3s) — CU, 47°: a red-hot steel slab glides through the rolling-mill rollers, steam hissing off it where water sprays. HARD CUT.",
        "SHOT 2 (3–5s) — CU, 47°: his gloved hand pushes a joystick forward on a modern control console; the console lights are on, the screens show only abstract shapes. HARD CUT.",
        "SHOT 3 (5–7s) — MWS (from the knees up, the line glowing behind him), 63°: @OPERARIO at the console at the right third, turns to the lens and speaks at 5–7s, a proud grin, then glances back to the line. HARD CUT.",
        "SHOT 4 (7–9s) — CU, 47°: a finished steel coil, still warm, rolls smoothly into its place on the conveyor. Hard end mid-roll.",
    ]),
    dialogue(line(5, 7, "OPERARIO", "de uma indústria mais eficiente,"), "OPERARIO"),
    acting("OPERARIO", "he has seen the plant transform and wants people outside to see it.",
           "show it off — the line, then you — checking that you are impressed.",
           "from the line to the lens and back.",
           "he nods once at the line, satisfied", "removing the glasses, folded arms"),
    T.REV_CAMERA,
    """PHYSICS & MATERIAL — the slab is enormous and heavy, moving steadily on the rollers; heat shimmer bends the air above it; water spray flashes to steam; the coil is dense and rolls with weight, settling into the cradle. """ + REAL + """ MATERIAL TRUTH: blue-black mill scale on the hot steel, the glowing orange core, brushed steel of the console, the matte plastic of the joystick, the weave of the flame-retardant coverall, painted yellow safety lanes on a clean floor.""",
    T.light_int("tall windows along the mill hall",
                "the orange glow of the hot steel as a strong secondary on the line, never the key on his face.",
                "the daylight lights the frame-LEFT side of his face and the helmet; the hot steel adds a warm edge on the line side; the hall falls off into depth."),
    T.FILM_LOOK,
    f"""SOUND — LOCATION SOUND ONLY: the deep roll of steel on the rollers; water spray hissing to steam; a steady industrial hum; the joystick's click; a crane's warning tone far off (single repeated tone, not a melody); his voice over it. {T.MUSIC_POLICY}""",
    T.WORLD,
    f"""NEGATIVE: helmet off, glasses off, logos on helmet or coverall, a dirty old factory, sparks fountain, explosion, readable screens, speaking in the close-ups, the camera stopping, extra cuts, {T.NEG_SPINE}.""",
    """[ORDER: 4 shots, 3 hard cuts at 3s, 5s and 7s, 9s, handheld travelling left to right in every shot — (1, 0–3s) CU: the red-hot slab through the rollers — (2, 3–5s) CU: his gloved hand on the joystick — (3, 5–7s) medium-wide: he turns to the lens and says his line, proud — (4, 7–9s) CU: the finished coil rolls into place. Invariants: constant lateral travel; full safety equipment; living eyes; only his one line. Look: 35mm color negative, warm halation, lifted blacks, organic grain. Brazilian Portuguese. NO music. NO subtitles, NO text.]""",
)

T06 = join(
    contract(9, "4 shots with 3 hard cuts at 3s, 5s and 7s", "handheld travelling sideways from frame-left to frame-right in every shot"),
    f"""REFERENCES — each reference has ONE job:
@PESQUISADORA — IDENTITY of @PESQUISADORA: face, hair, build, hands, wardrobe and safety equipment. 100% matches.
{SCOPE_ID}""",
    f"""WHO IS WHO — READ FIRST, ABSOLUTE:
@PESQUISADORA ({ANCH['PESQUISADORA']}) — the RESEARCHER: works at the bench, speaks once; NEVER removes gloves or glasses, NEVER walks out of frame.
FACES: her face exists once; one colleague far behind is a distinct soft figure, mouth closed.
CONTACT: nobody touches anyone.""",
    """SCENE — Afternoon in a modern pharmaceutical research laboratory in Minas Gerais, Brazil, glass walls and white benches. @PESQUISADORA is already preparing a solution.
THE SOUL OF THE SCENE (play it, never explain it): she loves what she does and almost nobody asks — she gives you one bright phrase between two steps of the experiment.""",
    rev_locks(4, [3, 5, 7], "PESQUISADORA", "de novas tecnologias,"),
    timeline(4, [3, 5, 7], [
        "SHOT 1 (0–3s) — ECU, 47°, lens 30 cm from the glass: a clear solution spins in a vortex in a glass beaker on a magnetic stirrer; a pipette tip releases a drop of blue reagent that blooms and is pulled into the swirl. HARD CUT.",
        "SHOT 2 (3–5s) — CU, 47°: her gloved hand slides a rack of sample tubes into a modern automated analyser; its arm moves over the tubes. HARD CUT.",
        "SHOT 3 (5–7s) — MWS (from the knees up, the bright lab around her), 63°: @PESQUISADORA at the bench at the right third, lifts her eyes to the lens and speaks at 5–7s with a quick smile, then looks back at the beaker. HARD CUT.",
        "SHOT 4 (7–9s) — CU, 47°: she holds a small vial up to the window light and checks its clarity, pleased. Hard end mid-gesture.",
    ]),
    dialogue(line(5, 7, "PESQUISADORA", "de novas tecnologias,"), "PESQUISADORA"),
    acting("PESQUISADORA", "she loves her work and rarely gets to talk about it.",
           "borrow two seconds from the experiment to share it, light and quick, then go back.",
           "from the beaker to the lens and back.",
           "she pushes her glasses up with the back of her wrist", "holding a test tube up to the camera"),
    T.REV_CAMERA,
    """PHYSICS & MATERIAL — the liquid spins with a real vortex and a dimple at the centre; the reagent drop falls, blooms in tendrils and is drawn into the swirl; the tube rack clicks into place; the gloves wrinkle at the knuckles. """ + REAL + """ MATERIAL TRUTH: graduation marks on the borosilicate glass (unreadable), condensation on a cold tube, the satin white of the bench, the nitrile texture of the gloves, the cotton twill of the lab coat.""",
    T.light_int("the lab's tall glass windows",
                "a soft under-shelf work light ~5000 K on the bench only.",
                "the daylight lights the frame-LEFT side of her face and makes the glass glow; the lab behind falls off a stop."),
    T.FILM_LOOK,
    f"""SOUND — LOCATION SOUND ONLY: the stirrer's soft whirr and the liquid swirling; the pipette click; the analyser's motor; glass touching glass; the hood's airflow. {T.MUSIC_POLICY}""",
    T.WORLD,
    f"""NEGATIVE: glowing liquids, coloured smoke, sci-fi holograms, readable labels or screens, gloves off, speaking in the close-ups, the camera stopping, extra cuts, {T.NEG_SPINE}.""",
    """[ORDER: 4 shots, 3 hard cuts at 3s, 5s and 7s, 9s, handheld travelling left to right in every shot — (1, 0–3s) ECU: the vortex in the beaker, a blue drop blooms into it — (2, 3–5s) CU: the tube rack into the analyser — (3, 5–7s) medium-wide: she looks up and says her line with a quick smile — (4, 7–9s) CU: she checks a vial against the window. Invariants: constant lateral travel; hands only in the close-ups; living eyes; only her one line. Look: 35mm color negative, warm halation, lifted blacks, organic grain. Brazilian Portuguese. NO music. NO subtitles, NO text.]""",
)

T07 = join(
    contract(7, "2 shots with 1 hard cut at 3s", "handheld; shot 1 strictly top-down at 90° and not travelling, shot 2 travelling sideways from frame-left to frame-right"),
    f"""REFERENCES — each reference has ONE job:
@DONO — IDENTITY of @DONO: face, hair, build, hands and wardrobe. 100% matches.
{SCOPE_ID}""",
    f"""WHO IS WHO — READ FIRST, ABSOLUTE:
@DONO ({ANCH['DONO']}) — the OWNER: finishes the plate with a squeeze bottle, then speaks once, already looking at the lens, flicking a towel onto his shoulder; NEVER sits, NEVER walks out of frame.
KITCHEN STAFF: three or four cooks working in the industrial kitchen behind him, distinct Brazilian men and women in plain white cook's jackets and dark aprons with no logos, soft and busy, silent, mouths closed.
FACES: each face exists once; no twins, no clones.
CONTACT: nobody touches anyone.""",
    """SCENE — Lunchtime in the professional kitchen of a healthy-food restaurant in Belo Horizonte, Brazil — an industrial kitchen, stainless steel everywhere, practical and busy, nothing fancy; the pass window opens onto a sunlit dining room. @DONO is already finishing a salad plate on the stainless-steel pass counter.
THE SOUL OF THE SCENE (play it, never explain it): he has run restaurants in this city for decades and this one is his pride — he lets you in on it like an old friend.""",
    f"""{LOCKS_HEAD}
1. Exactly 2 shots with 1 hard cut at 3s — WRONG if there are extra cuts.
2. Shot 1 is ABSOLUTELY TOP-DOWN: a pure overhead flat-lay, the lens pointing exactly straight down at the counter, 90° to its surface — the round plate reads as a perfect circle and the counter fills the whole frame; NO horizon, NO wall, NO front edge of the counter, NO side of anything visible — WRONG if the view is angled, three-quarter, from the side or from the front.
3. Shot 1: the camera does NOT travel — it stays put with only a faint handheld breath. Shot 2: the handheld camera travels sideways from frame-left to frame-right at one steady pace — WRONG if shot 1 travels, or shot 2 stops, reverses, pushes in or glides.
4. Shot 1 shows only the plate, the steel counter and his hand with the squeeze bottle, no face; in shot 2 he is ALREADY looking at the lens in the first frame and speaks only there, eyes alive.
5. Only @DONO speaks, only "de uma economia mais sustentável." — the cooks never speak.
6. In shot 2 he flicks the towel onto his shoulder WHILE he speaks, without turning away from the lens, and the industrial stainless-steel kitchen with working cooks fills the background — WRONG if the background is empty or looks like a fancy dining room.
7. Light from frame-LEFT — NO music.""",
    timeline(2, [3], [
        "SHOT 1 (0–3s) — OVERHEAD FLAT-LAY, 47°: the camera is exactly perpendicular to the counter, lens pointing straight down (zenithal, no tilt, no perspective angle), held directly above and staying put; the plate is a perfect circle and the steel counter fills the whole frame, no horizon and no walls visible: a plain white round plate of salad — fresh greens, grilled vegetables, cherry tomatoes, seeds — on a brushed stainless-steel pass counter; beside the plate, a silver service bell, chef's tools (tongs, a spoon, a pepper mill) and paper order tickets; @DONO's hand squeezes a plastic squeeze bottle that draws a thin line of DARK green herb oil over the salad, the oil beading on the leaves. HARD CUT.",
        "SHOT 2 (3–7s) — MWS (from the knees up, the industrial kitchen behind him — stainless-steel prep tables, a range under an exhaust hood, steel shelving with pans and plastic containers), 63°: @DONO at the right third, ALREADY looking at the lens from the first frame, the cooks working at the range and the steel prep tables behind him, soft; he speaks at 3–6s at an easy, unhurried pace with a complicit smile and flicks a clean white kitchen towel onto his left shoulder while he speaks; at 6–7s he holds the smile. Hard end.",
    ]),
    dialogue(line(3, 6, "DONO", "de uma economia mais sustentável."), "DONO"),
    acting("DONO", "decades in this city's kitchens, and this place is his pride.",
           "let you in on it with a complicit look, like to an old friend, while he flicks the towel onto his shoulder.",
           "on the lens from the first frame of shot 2.",
           "his moustache lifts on one side before he speaks", "a waiter's bow, presenting the plate to the camera"),
    """CAMERA — handheld in both shots.
SHOT 1: held directly above the counter, the lens exactly vertical and looking straight down at 90° — no tilt, no angle — and it STAYS PUT: only a faint handheld breath, no travel.
SHOT 2: the operator crab-walks sideways at an even slow walking pace from frame-LEFT to frame-RIGHT, lens at shoulder height, small footfall bounce; never stops, never reverses, never pushes in.
OPTICS: as stated per shot; no lens drift. FOCUS: on the plate in shot 1; on his eyes in shot 2, the kitchen soft behind. HORIZON: level in shot 2.
NOT: shot 1 travelling, shot 1 tilted or angled, a tripod or locked-off frame in shot 2, gimbal glide, drone, push-in, zoom.""",
    """PHYSICS & MATERIAL — the squeeze bottle gives with a small hiss and draws a thin line of oil that beads on the leaves; the towel flicks through the air and lands on his shoulder; pans move and steam rises from the range behind him. """ + REAL + """ MATERIAL TRUTH: glossy dark green herb oil, flakes of sea salt, the glaze of a plain white ceramic plate, brushed stainless steel with soft reflections on the counter, prep tables, shelving and exhaust hood, a silver service bell, order tickets in paper, plastic kitchen containers, the cotton of the towel.""",
    T.light_int("the pass window that opens onto the sunlit dining room",
                "bright white overhead kitchen lights as an even secondary on the steel behind, small, never on his face.",
                "the daylight lights the frame-LEFT side of his face and the plate; the kitchen behind falls off a stop."),
    T.FILM_LOOK,
    f"""SOUND — LOCATION SOUND ONLY: the squeeze bottle's soft hiss; a service bell's single ding far off; the plate on the steel; pans sizzling and steel utensils and containers in the kitchen; the exhaust hood's steady hum; the cooks' murmur with no words standing out; the towel's soft flick. {T.MUSIC_POLICY}""",
    T.WORLD,
    f"""NEGATIVE: a customer, a face in shot 1, an angled, three-quarter, side or front view in shot 1, a horizon, walls or the counter's front edge in shot 1, a travelling or moving camera in shot 1, bright or golden oil, him turning toward the lens in shot 2, an empty kitchen, cooks speaking, an elegant dining room, light wood, plants, pendant lights, a fancy, upscale, rustic or home-style kitchen, readable menu, logos on the uniforms, a locked-off or stopped camera in shot 2, push-in, extra cuts, {T.NEG_SPINE.replace("locked-off tripod shot, static camera, ", "")}.""",
    """[ORDER: 2 shots, 1 hard cut at 3s, 7s, handheld — (1, 0–3s) strictly top-down 90° flat-lay on the steel counter, camera staying put: dark green herb oil from a squeeze bottle over the salad — (2, 3–7s) medium-wide, travelling: already looking at the lens, the industrial stainless-steel kitchen behind him, he says his line and flicks the towel onto his shoulder. Invariants: shot 1 exactly top-down at 90° (never angled or from the side), static, no face; shot 2 lateral travel; he looks at the lens from the first frame; towel toss during the line; busy industrial steel kitchen behind, nothing fancy. Look: 35mm color negative, warm halation, lifted blacks, organic grain. Brazilian Portuguese. NO music. NO subtitles, NO text.]""",
)

T08 = join(
    contract(10, "2 shots with 1 hard cut at 2s", "handheld travelling sideways from frame-left to frame-right in both shots while backing up, arcing around her like a slow orbit as she walks forward"),
    f"""REFERENCES — each reference has ONE job:
@AGRICULTORA — IDENTITY of @AGRICULTORA: face, hair, build, hands and wardrobe. 100% matches.
{SCOPE_ID}""",
    f"""WHO IS WHO — READ FIRST, ABSOLUTE:
@AGRICULTORA ({ANCH['AGRICULTORA']}) — the FARMER: walks FORWARD along her soybean row, head and body facing her line of walk, checks the plants with her hand, speaks; her eyes find the lens; NEVER walks sideways, NEVER walks away from the camera, NEVER stops walking.
FACES: her face exists once; nobody else in frame.
CONTACT: only her hands on the plants.""",
    """SCENE — Bright mid-morning in a large, modern soybean farm in the Triângulo Mineiro, Minas Gerais, Brazil: vivid green rows running straight away to the horizon, a centre-pivot irrigation arm far off, a blue sky with a few white clouds. @AGRICULTORA is already walking forward along a row, her open hand passing over the tops of the plants.
THE SOUL OF THE SCENE (play it, never explain it): this is her land and she runs it with pride; she comes walking toward you, delighted to get to the point.""",
    f"""{LOCKS_HEAD}
1. Exactly 2 shots with 1 hard cut at 2s — WRONG if there are extra cuts.
2. She walks FORWARD along her row for the whole take, her head and body facing her line of walk and only her eyes finding the lens — WRONG if she walks sideways, walks away, or turns her head sideways to look at the camera (the camera moves around her, she does not turn).
3. In EVERY shot the handheld camera travels sideways from frame-LEFT to frame-RIGHT at one steady pace while backing up at her walking pace, so it keeps its distance and ARCS around her like a slow orbit — about 25° off her line of walk on one side at the start to about 25° on the other by the end — WRONG if it stops, reverses, pushes in, pulls back, or swings round to her side or her back.
4. The close-up shows her hand and the plants only; she speaks only in the medium-wide shot, her eyes alive on the lens and readable under the hat brim — WRONG if glassy or hidden in shadow.
5. Only @AGRICULTORA speaks, only "Enquanto o mundo olha para o nióbiu e as terras raras de Minas, Minas olha para o que há de mais raro na nossa terra:" — the word "nióbiu" is said nee-OH-byoo with a clear B, never "niório" — every other mouth closed.
6. Bright mid-morning light from frame-LEFT, NOT golden hour — NO music.""",
    timeline(2, [2], [
        "SHOT 1 (0–2s) — CU, 47°, the lens at plant-top height about 0.8 m from her hand, sliding sideways from frame-LEFT to frame-RIGHT and backing up at her pace: her open hand sweeps forward over the tops of the soybean plants, the leaves brushing her palm and springing back; her body soft behind the hand, walking forward. HARD CUT.",
        "SHOT 2 (2–10s) — MWS (from the knees up, the rows behind her, the pivot far off), 63°, the camera about 3.5 m from her, arcing from frame-LEFT to frame-RIGHT around her while backing up at her pace: @AGRICULTORA walks forward along her row, centred, her head on her line of walk, her eyes finding the lens; she speaks at 2–9s, eyes mostly on you with a quick glance down at the plants now and then, smiling more as she goes; at 9–10s she keeps walking with a warm smile, eyes on you. Hard end mid-step.",
    ]),
    dialogue(line(2, 9, "AGRICULTORA", "Enquanto o mundo olha para o nióbiu e as terras raras de Minas, Minas olha para o que há de mais raro na nossa terra:"), "AGRICULTORA").replace(
        "\nVOICE LOCK",
        "\nPRONUNCIATION — \"nióbiu\" is Brazilian Portuguese for niobium, said nee-OH-byoo: three syllables, stress on the OH, a clear B before the final \"byoo\" — NEVER \"niório\", never \"niobrio\". Say it once, clearly, inside the sentence.\nVOICE LOCK"),
    acting("AGRICULTORA", "she runs this land and knows what it is worth.",
           "come toward you like a proud host and get to the point with a smile.",
           "on the lens, with a quick glance down at the plants now and then; steady on you toward the end of the line.",
           "she breathes a short laugh through her nose", "arms spread over the field, turning her head sideways to look at the camera"),
    """CAMERA — handheld in EVERY shot, an operator with a body: the operator crab-walks sideways at an even slow pace from frame-LEFT to frame-RIGHT while also backing up at her walking pace, so the camera keeps its distance and ARCS around her like a slow orbit — about 25° off her line of walk on one side at the start, about 25° on the other by the end — with human footfall bounce and late small corrections; the camera never stops, never reverses, never pushes in or pulls back; she stays centred in the frame.
SHOT 1: CU, the lens at plant-top height about 0.8 m from her hand. SHOT 2: lens at chest height, about 3.5 m from her.
OPTICS: as stated per shot; no lens drift inside a shot.
FOCUS: on her hand in shot 1; on her eyes in shot 2, the field sliding soft behind her.
HORIZON: level.
NOT: tripod, locked-off frame, gimbal glide, dolly-smooth slide, drone, a wide orbit round to her side or back, push-in, pull-back, zoom, the camera stopping or reversing.""",
    """GEOMETRY — the soybean rows run straight away from the camera to the horizon; @AGRICULTORA walks forward along one row on the centre line; the camera arcs across the rows from her front-left to her front-right, 0.8 m from her hand in shot 1 and 3.5 m from her in shot 2; the plants knee-high; the centre-pivot arm about 300 m away, small, sliding across behind her; the sun high on frame-LEFT.""",
    """PHYSICS & MATERIAL — the plants are springy: her hand bends the tops and they whip back behind her; her boots press into the soft soil between rows; her braid swings with each step. """ + REAL + """ MATERIAL TRUTH: glossy healthy leaves, the light cotton of her sage-green shirt, the felt of her hat brim, the spray of the irrigation catching the sun far off.""",
    T.LIGHT_EXT_DAY,
    T.FILM_LOOK,
    f"""SOUND — LOCATION SOUND ONLY: leaves brushing her hand and trousers in a steady rhythm; her boots on soft soil; wind over the field; a quero-quero bird calling far off; the faint hiss of the irrigation pivot. {T.MUSIC_POLICY}""",
    T.WORLD,
    f"""NEGATIVE: mispronouncing "nióbiu" (as "niório" or any other word), walking sideways, walking away from the camera, her head turned sideways to the lens, a camera that stays on one straight line, a camera that swings round to her side or back, stopping, the camera stopping or reversing, push-in, pull-back, golden hour, a low orange sun, a sunset sky, long shadows, eyes hidden in the hat shadow, arms spread, a straw hat, a poor old farm, an old tractor, speaking in the close-ups, drone shot, extra cuts, {T.NEG_SPINE}.""",
    """[ORDER: 2 shots, 1 hard cut at 2s, 10s, handheld travelling sideways from frame-left to frame-right in both shots while backing up, arcing around her like a slow orbit — (1, 0–2s) CU: her hand sweeping forward over the plants — (2, 2–10s) medium-wide: she walks forward and says her line, eyes on you, smiling, still walking; hard end mid-step. Invariants: she walks forward, head on her line of walk, never sideways; constant lateral travel left to right with the distance held, a slow arc about 25° each side of her line of walk; bright mid-morning light from frame-LEFT, not golden hour; eyes readable under the hat brim; living eyes; only her line. Look: 35mm color negative, warm halation, lifted blacks, organic grain. Brazilian Portuguese. NO music. NO subtitles, NO text.]""",
)

# ---------------------------------------------------------------- T09
T09 = join(
    contract(6, "ONE continuous take, no cuts", "handheld, close and breathing; one focus rack from the niobium to his eyes"),
    f"""REFERENCES — each reference has ONE job:
@FUNCIONARIO — IDENTITY of @FUNCIONARIO: face, build, hands, wardrobe and safety equipment. 100% matches.
{SCOPE_ID}""",
    f"""WHO IS WHO — READ FIRST, ABSOLUTE:
@FUNCIONARIO ({ANCH['FUNCIONARIO']}) — the MINE WORKER: holds a chunk of niobium up in front of his face, lowers it, says one short phrase and smiles; NEVER removes any safety equipment, NEVER walks away.
FACES: his face exists once; nobody else in the frame; the haul trucks far behind have no visible drivers.
CONTACT: only his gloved hand on the niobium.""",
    """SCENE — Late afternoon at the edge of a modern open-pit niobium mine in Araxá, Minas Gerais, Brazil: orderly terraced benches, big modern haul trucks far below, all soft behind him. @FUNCIONARIO is already holding a chunk of raw niobium in his gloved hand, right in front of his face.
THE SOUL OF THE SCENE (play it, never explain it): someone else began the sentence and he gets the last word — the rarest thing in Minas is its people, and he is one of them; he says it like the happy punchline of a story he is proud of.""",
    f"""{LOCKS_HEAD}
1. ONE continuous handheld take in the NIOBIUM FRAME, no cuts — WRONG if it cuts, pushes in or is locked.
2. 0–3s: the niobium chunk, held in his gloved hand, covers most of his face and is SHARP in the foreground; his face behind it is OUT OF FOCUS and barely shows — only the edge of the white hard hat, the clear glasses and one eye peeking at the lens — WRONG if his face is clearly visible before the niobium moves.
3. At 3s he lowers the niobium straight down and out of the bottom of the frame, and the face it reveals is ALREADY smiling, eyes on the lens, on the upper-third line at about 45% of the frame width, alive; the focus racks to his eyes in the same motion — WRONG if the niobium rises, sweeps across his face or stays in frame, if the smile starts after the reveal, or if the eyes are glassy or land elsewhere.
4. The first word of "a nossa gente." starts WITH the lowering at 3s and lands by 5s, as the conclusion of a longer sentence — resolved and proud, smiling, never solemn; his mouth is closed at 0–3s and 5–6s — WRONG if there is a silent beat between the reveal and the first word, or if he says any other word.
5. Full mining safety equipment on: hard hat with chin strap fastened, glasses, high-visibility vest, gloves — WRONG if any piece is missing or carries a logo.
6. Sun from frame-LEFT — NO music.""",
    timeline(1, [], [
        "BEAT 1 (0–3s) — the NIOBIUM FRAME, CU: a chunk of raw niobium — rough, faceted, silvery-grey metal with sharp crystalline edges that glint in the sun — held in his gloved fingers at arm's length toward the lens, right in front of his face, SHARP, filling about half the frame height and covering most of his face; his face behind it soft and barely showing: the edge of the white hard hat, the clear glasses, one eye peeking at the lens beside the chunk, already creased with a smile; the chunk turns a few degrees in his fingers and its facets glint.",
        "BEAT 2 (3–5s) — a small playful reveal: he lowers the niobium straight down and out of the bottom of the frame, and the face it uncovers is already smiling, eyes on the lens; the focus racks from the niobium to his eyes in the same motion, and he delivers the line as he lowers it, the phrase landing like the end of a sentence: resolved and proud, light, not solemn.",
        "BEAT 3 (5–6s) — he holds the smile, eyes on the lens, mouth closed. Hard end on the held look.",
    ]),
    dialogue(line(3, 5, "FUNCIONARIO", "a nossa gente.").replace(
        "(on camera, Brazilian Portuguese)",
        "(on camera, Brazilian Portuguese; the closing words of a longer sentence — a resolved, falling close, proud and smiling, never solemn)"), "FUNCIONARIO"),
    acting("FUNCIONARIO", "someone else just opened a sentence and he has the answer — the thing he is proudest of.",
           "show you the rare metal like a prize, then lower it with the answer already on his lips — the smile is on his face the moment it is revealed — and tell you the real treasure is the people, and he is one of them.",
           "peeking at the lens past the niobium; on the lens, steady and warm, from the moment it clears.",
           "his chin lifts a hair as the niobium comes down",
           "a heroic pose, gesturing at the mine, holding the niobium up to the camera after the line"),
    T.NIOBIUM_FRAME + "\nIn this take the eyes are already on the lens beside the niobium; they land fully on that mark when the niobium clears.",
    T.handheld() + "\nFOCUS PULL: at 0–3s the focus is on the niobium and his face is soft; from 3s, as the niobium leaves the frame, the focus racks smoothly to his eyes and stays on them.",
    """PHYSICS & MATERIAL — the niobium is dense, cold and heavy for its size, sharp-edged; his padded glove presses into it and it swings slightly with its weight as he lowers it; dust lifts off the pit in the wind and drifts right; the vest is stiff. """ + REAL + """ MATERIAL TRUTH: the rough crystalline silvery-grey facets of the niobium with a dull-bright metallic sheen and fine dust in the crevices (not a smooth ingot, not a mirror), the clean grey padded fabric of the glove, the glossy white helmet shell, the black elastic chin strap under his jaw, reflective tape on the vest, clear glasses without glare over the eyes.""",
    T.LIGHT_EXT,
    T.FILM_LOOK,
    f"""SOUND — LOCATION SOUND ONLY: wind over the open pit; a haul truck's diesel engine far off; a reversing alarm far away (single repeated tone, not a melody); the glove's fabric against the metal; after his line, only wind and the distant truck. {T.MUSIC_POLICY}""",
    T.WORLD + " Mining safety equipment is complete and correct; nobody in the pit without it.",
    f"""NEGATIVE: his face clearly visible before the niobium moves, the niobium staying in front of his face after 3s, the niobium raised or swept sideways across his face, a smooth polished ingot, a mirror ball, glowing metal, gold, a smile that starts after the reveal, a silent beat between the reveal and the first word, any word beyond "a nossa gente.", a solemn, serious or heroic face, dirty or grimy hands, missing helmet, unfastened chin strap, no glasses, no vest, logos on equipment or trucks, eyes landing off the upper third, a cut, a push-in, {T.NEG_SPINE}.""",
    """[ORDER: ONE handheld take, 6s, NIOBIUM FRAME close-up — (0–3s) a chunk of silvery faceted niobium in his gloved hand in front of his face, sharp, his face soft and barely showing behind it — (3–5s) he lowers it straight down out of frame; the face it reveals is already smiling, eyes on the lens at the upper third, 45% width, the focus racks to his eyes, and he says only "a nossa gente." as he lowers it, resolved and proud — (5–6s) he holds the smile, mouth closed; hard end. Invariants: full safety equipment; only that phrase, starting with the lowering; the smile is there at the reveal; the niobium leaves downward and out of frame; eyes landing on the mark; handheld. Look: 35mm color negative, warm halation, lifted blacks, organic grain. Brazilian Portuguese. NO music. NO subtitles, NO text.]""",
)


# ---------------------------------------------------------------- T09-B (cava: plano baixo + MCU com dolly-out)
T09B = join(
    contract(10, "2 shots with 1 hard cut at 3s", "handheld at ground level in shot 1, a slow dolly-out in shot 2"),
    f"""REFERENCES — each reference has ONE job:
@FUNCIONARIO — IDENTITY of @FUNCIONARIO: face, build, hands, wardrobe and safety equipment. 100% matches.
{SCOPE_ID}""",
    f"""WHO IS WHO — READ FIRST, ABSOLUTE:
@FUNCIONARIO ({ANCH['FUNCIONARIO']}) — the MINE WORKER: in shot 1 he walks away from the camera, seen from behind, toward the machine, speaking; in shot 2 he faces the lens in front of that same machine and speaks; NEVER removes any safety equipment.
FACES: his face exists once and shows only in shot 2; nobody else; the machine has no visible operator.""",
    """SCENE — Late afternoon on the floor of a modern open-pit niobium mine in Araxá, Minas Gerais, Brazil: orderly terraced benches rising on all sides, a wide flat of pale crushed ore, and far ahead one mid-sized modern hydraulic excavator, about 3.5 m tall — off-white and grey steel with a safety-orange stripe, no logos — small against the benches around it. @FUNCIONARIO is already walking away from the camera toward it.
THE SOUL OF THE SCENE (play it, never explain it): he walks into the work he is proudest of, then turns and tells you what it is all for — like good news to a friend.""",
    f"""{LOCKS_HEAD}
1. Exactly 2 shots with 1 hard cut at 3s — WRONG if there are extra cuts.
2. SHOT 1 is WIDE, the lens EXTREMELY LOW, a few centimetres off the ground: @FUNCIONARIO small in the middle distance, seen only from BEHIND, walking away toward the small machine far ahead, the low sun right behind it with ONE soft warm lens flare — WRONG if the lens is above knee height, his face shows, the machine is close, or there is a second flare.
3. SHOT 2 is the MATCH FRAME: medium close-up, face dead centre, straight into the lens, in front of the same machine; the camera moves slowly BACK (a dolly-out, no zoom), the framing opening toward a medium shot — WRONG if the lens zooms, the face drifts off centre or looks away, or a flare appears.
4. He speaks ONLY two lines, same voice and delivery: "Afinal, o que cresce aqui:" at 0–2s in shot 1 (mouth unseen) and "também deve construir novos caminhos para quem nasce, vive e trabalha aqui." at 3–9s in shot 2, a brief beat of silence after "nasce," and after "vive," — WRONG if he says anything else.
5. Full mining safety equipment in both shots: hard hat with chin strap, glasses, high-visibility vest, gloves, no logos.
6. Only shot 1 is backlit; shot 2 has the light of the previous take (low sun from frame-LEFT) — NO music.""",
    timeline(2, [3], [
        "SHOT 1 (0–3s) — WIDE, 84°, handheld, the lens a few centimetres above the ground, drifting slowly forward behind him: pale crushed-ore floor across the lower third, pebbles soft in the foreground; @FUNCIONARIO small in the middle distance, walking away at an easy pace toward a mid-sized off-white excavator far ahead, saying his first line as he goes, the terraced benches rising on both sides; the low sun right behind the machine, one soft flare blooming across the lower frame, his long shadow stretching toward us. HARD CUT.",
        "SHOT 2 (3–10s) — the MATCH FRAME, MCU, 47° lens fixed: @FUNCIONARIO dead centre, facing the lens in front of the same excavator, soft behind him; he speaks at 3–9s with a proud, easy smile, a brief beat of silence after 'nasce,' and after 'vive,', while the slow dolly-out runs the whole shot — the camera backs away, the frame opens toward a medium shot, the machine and the pit growing behind him, his face staying dead centre; at 9–10s he holds the smile. Hard end.",
    ]),
    dialogue(
        line(0, 2, "FUNCIONARIO", "Afinal, o que cresce aqui:").replace(
            "(on camera, Brazilian Portuguese)",
            "(on camera but seen from behind, walking away, Brazilian Portuguese; the same voice and delivery as his other lines — warm, resolved, proud, never solemn)"),
        line(3, 9, "FUNCIONARIO", "também deve construir novos caminhos para quem nasce, vive e trabalha aqui.").replace(
            "(on camera, Brazilian Portuguese)",
            "(on camera, Brazilian Portuguese; the same voice and delivery — warm, resolved, proud, never solemn)"),
        "FUNCIONARIO").replace("\nVOICE LOCK", "\nPACING — in the second line, a brief beat of silence (about half a second) after \"nasce,\" and after \"vive,\".\nVOICE LOCK"),
    acting("FUNCIONARIO", "he has just walked into the work he is proudest of.",
           "say what it is all for, like good news to a friend — easy, certain, smiling.",
           "in shot 2 straight into the lens, steady and warm.",
           "his chin lifts a hair as he starts",
           "a heroic pose, gesturing at the machine"),
    """CAMERA — SHOT 1: handheld, an operator with a body: the lens a few centimetres above the ground in a WIDE frame, drifting slowly forward behind him with human breath and late small corrections; never locked, no drone, no crane. FOCUS: on him and the machine, the foreground pebbles soft. HORIZON: level.
SHOT 2: the dolly-out below.""",
    T.dolly_out(7),
    T.MATCH_FRAME,
    """GEOMETRY — in shot 1 the camera sits on the ground about 40 m behind @FUNCIONARIO, the excavator about 150 m ahead of him, the sun low directly behind it; in shot 2 the camera starts 1.3 m from his face at eye height, the excavator about 12 m behind him, the sun low on frame-LEFT.""",
    """PHYSICS & MATERIAL — his boots crunch on the crushed ore and lift thin puffs of dust that catch the sun; the excavator is mid-sized and still. """ + REAL + """ MATERIAL TRUTH: pale crushed ore with fine dust, the glossy white helmet shell, the black chin strap, reflective tape on the vest, clear glasses without glare, the off-white painted steel of the excavator.""",
    "LIGHT — TWO SETUPS under the same low late-afternoon sun; only shot 1 is backlit.\n" + T.LIGHT_EXT_BACK + "\nSHOT 2 — the same light as the previous take: " + T.LIGHT_EXT.replace("LIGHT — ", "", 1).replace("CONTINUITY: the sun stays frame-LEFT in every shot; lit sides never flip.", "CONTINUITY: in shot 2 the sun stays frame-LEFT and the lit side never flips; shot 1 is the only backlit shot."),
    T.FILM_LOOK_FLARE,
    f"""SOUND — LOCATION SOUND ONLY under his voice: his boots on crushed stone (shot 1); wind over the open pit; the excavator's low idle hum; a reversing alarm far away (single repeated tone, not a melody). {T.MUSIC_POLICY}""",
    T.WORLD + " Mining safety equipment is complete and correct; nobody in the pit without it.",
    f"""NEGATIVE: a camera above knee height in shot 1, his face in shot 1, a close machine in shot 1, an oversized or giant machine, a second flare, a flare in shot 2, a zoom or vertigo effect, a push-in, the face drifting off centre, him looking away in shot 2, words beyond his two lines, gesturing at the machine, logos, missing helmet, extra cuts, {T.NEG_DOLLY.replace("lens flare, ", "")}.""",
    """[ORDER: 2 shots, 1 hard cut at 3s, 10s — (1, 0–3s) WIDE, lens a few centimetres above the ground, handheld: @FUNCIONARIO small, from behind, walking away toward a mid-sized excavator, saying "Afinal, o que cresce aqui:" at 0–2s, the low sun right behind the machine, ONE soft flare — (2, 3–10s) MATCH FRAME medium close-up, face dead centre, straight into the lens, slow dolly-out (no zoom), he says "também deve construir novos caminhos para quem nasce, vive e trabalha aqui." at 3–9s, a beat of silence after "nasce," and after "vive,". Invariants: shot 1 extremely low, backlit, back to camera; shot 2 centred, frontal, the light of the previous take; full safety equipment; a flare only in shot 1. Look: 35mm color negative, warm halation, lifted blacks, organic grain. Brazilian Portuguese. NO music. NO subtitles, NO text.]""",
)

# ---------------------------------------------------------------- T10 / T11 (match, sem fala)
def match_locks(subject, mouth_note, eyes="straight into the lens, the eyes alive"):
    return f"""{LOCKS_HEAD}
1. ONE take in the MATCH FRAME with the slow dolly-out (the camera moving back, no zoom), no cuts — WRONG if it cuts, if the camera is locked, or if the lens zooms or the camera pushes in.
2. {subject}'s face stays dead centre and frontal, {eyes}, while the framing opens from a medium close-up toward a medium shot — WRONG if the face drifts off centre or turns away, or the eyes go glassy.
3. NO dialogue: {mouth_note} — WRONG if any mouth forms words.
4. Light from frame-LEFT — NO music."""


T10 = join(
    contract(4, "ONE continuous take, no cuts", "a slow dolly-out from a medium close-up", dialogue=False),
    f"""REFERENCES — each reference has ONE job:
@MAE — IDENTITY of @MAE: face, hair, build, hands and wardrobe. 100% matches.
{SCOPE_ID}""",
    f"""WHO IS WHO — READ FIRST, ABSOLUTE:
@MAE ({ANCH['MAE']}) — the MOTHER: holds her newborn in her arms and smiles into the lens; NEVER speaks.
NEWBORN — a real newborn of a few days, small and correctly proportioned, wrapped in a pale cotton blanket and held in her arms at the bottom edge of the frame, most of the face covered by the blanket; only a forehead, a closed eye and a cheek show.
FACES: each face exists once; nobody else in the room.
CONTACT: only her hands on the baby.""",
    """SCENE — A bright bedroom in a modern apartment in Belo Horizonte, Brazil, afternoon; @MAE stands by the window holding her newborn in her arms, looking at you.
THE SOUL OF THE SCENE (play it, never explain it): someone new just arrived — she looks at you, radiant, as if you had come in to meet him.""",
    match_locks("@MAE", "her mouth stays closed in a smile, the baby makes only small breathing sounds"),
    timeline(1, [], [
        "BEAT 1 (0–4s) — the MATCH FRAME, MCU: @MAE's face dead centre, eyes on the lens, a warm radiant smile, the swaddled newborn held in her arms at the bottom edge of the frame; the slow dolly-out runs the whole take, the bedroom opening wider behind her; she keeps her eyes on you and the smile. Hard end on the held look.",
    ]),
    acting("MAE", "everything is new and she is happy.",
           "smile at you with the baby in her arms — \"look who arrived\".",
           "on the lens throughout.",
           "a slow happy blink",
           "speaking, crying, rocking theatrically, presenting the baby to the camera"),
    T.dolly_out(4),
    T.MATCH_FRAME,
    """PHYSICS & MATERIAL — the baby is light, warm and limp, sinking into the crook of her arm; the blanket's cotton folds; a tiny movement of the baby's chest under her hand. """ + REAL + """ MATERIAL TRUTH: the fine rib of her ivory knit, a few loose strands of hair across her cheek, the baby's delicate newborn skin, the sheer curtain glowing behind her.""",
    T.light_int("the bedroom window with a sheer curtain",
                "no other source.",
                "the daylight lights the frame-LEFT side of her face and the blanket; the room behind falls off a stop."),
    T.FILM_LOOK,
    f"""SOUND — LOCATION SOUND ONLY: quiet room tone; the baby's small breathing and one tiny sigh; the knit's soft rustle; the city far below the window. {T.MUSIC_POLICY}""",
    T.WORLD,
    f"""NEGATIVE: the mother speaking, any mouth forming words, a doll-like baby, wrong newborn proportions, the baby's full face, presenting the baby to the camera, crying, a cut, the face drifting off centre, a zoom, a generic or plain-looking woman, {T.NEG_DOLLY}.""",
    """[ORDER: ONE take, 4s, MATCH FRAME medium close-up with a slow dolly-out — @MAE's face dead centre, eyes on the lens, a warm radiant smile, the swaddled newborn held in her arms at the bottom edge, the room opening wider behind her as the camera backs away; hard end on the held look. Invariants: face centred throughout, the camera backing away with no zoom; no dialogue; baby partly covered, correct proportions. Look: 35mm color negative, warm halation, lifted blacks, organic grain. NO music. NO subtitles, NO text.]""",
)

T11 = join(
    contract(4, "ONE continuous take, no cuts", "a slow dolly-out from a medium close-up", dialogue=False),
    f"""REFERENCES — each reference has ONE job:
@TORCEDORA — IDENTITY of @TORCEDORA: face, hair, build, hands and wardrobe, EXCEPT the small emblem on the jersey chest, which must NOT appear: the chest of her jersey is plain. 100% matches otherwise.
{SCOPE_ID}""",
    f"""WHO IS WHO — READ FIRST, ABSOLUTE:
@TORCEDORA ({ANCH['TORCEDORA']}) — the FAN: sits in a grandstand watching the match with bright, excited attention, her eyes on the pitch just beside the lens; NEVER speaks, NEVER shouts, NEVER looks straight into the lens.
CROWD — many other fans seated and standing all around her, left, right and behind: distinct people, soft and out of focus, in everyday clothes of mixed colours, all watching the match and excited too; nobody with her face; no twins, no clones.
CONTACT: nobody touches her.""",
    """SCENE — A late-afternoon football match: @TORCEDORA sits in the grandstand of a stadium with many fans all around her, watching the match.
THE SOUL OF THE SCENE (play it, never explain it): this is the best part of her week — she is hooked on the game, lit up and happy, natural and never overplayed.""",
    match_locks("@TORCEDORA", "her lips may part in a small excited breath but form no words; the crowd is only a roar with no words standing out",
                eyes="her eyes bright on the match just beside the lens, close to the camera but never into it"),
    timeline(1, [], [
        "BEAT 1 (0–4s) — the MATCH FRAME, MCU: @TORCEDORA's face dead centre and frontal, her eyes bright and locked on the play just beside the lens, lit up with excitement — a small excited breath, a smile that comes and goes and widens as the play builds — the fans around her soft and excited too; the slow dolly-out runs the whole take, the crowd opening wider around her. Hard end.",
    ]),
    acting("TORCEDORA", "this is her Sunday ritual and she is hooked.",
           "follow the play with bright, happy attention, like a friend in the next seat who is thrilled to be there.",
           "bright on the match, just beside the lens, never into it.",
           "a small excited breath as the play builds",
           "blasé, flat or calm, exaggerated or frantic reactions, shouting, arms up, face paint, a scarf, a club crest or sponsor on her jersey, looking straight into the lens"),
    T.dolly_out(4),
    T.MATCH_FRAME + "\nIn this take her face is frontal and dead centre as in the frame above, but her eyes are on the match, just beside the lens, not into it.",
    """PHYSICS & MATERIAL — the stand vibrates faintly with the crowd; wind moves the hem of her jersey; the fans around her rise and settle, lean and gasp, soft shapes. """ + REAL + """ MATERIAL TRUTH: the velour of her terracotta football jersey with its cream polo collar and cuffs and a plain chest, her smooth slicked-back hair, a bead of sweat at the hairline, the glint of her gold hoops.""",
    T.LIGHT_EXT,
    T.FILM_LOOK,
    f"""SOUND — LOCATION SOUND ONLY: a dense wordless crowd roar swelling, soft gasps and "oh" sounds around her; a whistle far off. NO chanting songs, NO drums, NO brass band, NO anthem. {T.MUSIC_POLICY}""",
    T.WORLD + " Wardrobe and crowd carry NO football club colour combinations (black-and-white, blue-and-white, green-and-white), NO yellow-and-green, NO flags, NO scarves; her football jersey is generic and fictional — a plain chest, no crest, no sponsor, no number, no text — and nobody in the crowd wears a club shirt.",
    f"""NEGATIVE: a blasé, bored, flat or neutral expression, exaggerated or frantic reactions, the fan speaking or shouting, any mouth forming words, her looking straight into the lens, cheering arms, an emblem or crest on her jersey chest, a sponsor logo, a shirt number or text on her jersey, a recognisable club's kit, loose or voluminous hair, scarf, flag, face paint, black-and-white, blue-and-white, green-and-white, yellow-and-green, readable faces in the crowd, chanting, drums, a cut, the face drifting off centre, a zoom, a generic or plain-looking woman, {T.NEG_DOLLY}.""",
    """[ORDER: ONE take, 4s, MATCH FRAME medium close-up with a slow dolly-out — @TORCEDORA's face dead centre and frontal, her eyes bright on the match just beside the lens, lit up, a smile that comes and goes and widens, many excited fans all around her, the crowd opening wider as the camera backs away; hard end. Invariants: face centred throughout, the camera backing away with no zoom; eyes just beside the lens, never into it; lively and happy, never blasé and never overplayed; no dialogue; a generic jersey with a plain chest, no club colours. Look: 35mm color negative, warm halation, lifted blacks, organic grain. NO music, NO chants, NO drums. NO subtitles, NO text.]""",
)

# ---------------------------------------------------------------- T12 (só o motorista: match + fala, ônibus parado)
T12 = join(
    contract(10, "2 shots with 1 hard cut at 3s", "a slow dolly-out in shot 1, handheld in shot 2, inside a stopped bus"),
    f"""REFERENCES — each reference has ONE job:
@MOTORISTA — IDENTITY of @MOTORISTA: face, hair, build, hands and wardrobe. 100% matches.
@ONIBUS_INT — PLACE of the bus: the layout, the yellow handrails, the seats, the windows, the floor, the door. 100% matches the place.
@ONIBUS_CAB — PLACE of the driver's cab: the seat, the steering wheel, the dash, the fare validator, the mirror, the yellow handrail, the steps. 100% matches the cab.
{SCOPE_ID} For @ONIBUS_INT and @ONIBUS_CAB: IGNORE any people, any text, stickers, signs or logos (even on the steering wheel), the light, the exposure and the colour grade, raindrops on the glass, and whatever is seen outside the windows.""",
    f"""WHO IS WHO — READ FIRST, ABSOLUTE:
@MOTORISTA ({ANCH['MOTORISTA']}) — the BUS DRIVER: at the wheel on the bus's left side, smiles at you in shot 1, speaks once in shot 2; the bus is STOPPED; NEVER stands, NEVER opens the door.
FACES: each face exists once; two or three seated passengers far back are distinct soft Brazilian adults, mouths closed; nobody boards, no student, nobody else near the door; no twins, no clones.
CONTACT: nobody touches anyone.""",
    """SCENE — Late afternoon inside a clean, well-kept Brazilian city bus in Belo Horizonte, STOPPED at a stop with the engine idling — yellow handrails, blue patterned seats, a grey rubber floor, a folding glass door shut, the cab as in @ONIBUS_CAB. @MOTORISTA sits at the wheel looking at you.
THE SOUL OF THE SCENE (play it, never explain it): every day he drives people to where the opportunities are; he is proud of where this route goes — he tells you the route with a smile.""",
    f"""{LOCKS_HEAD}
1. Exactly 2 shots with 1 hard cut at 3s; shot 1 is the dolly-out, shot 2 is handheld — WRONG if extra cuts.
2. SHOT 1 is the MATCH FRAME: medium close-up of @MOTORISTA, face dead centre, straight into the lens with a warm smile for the whole 3 s, the camera moving slowly BACK (a dolly-out, no zoom) so the framing opens toward a medium shot — WRONG if the lens zooms, the face drifts off centre, he looks away or down, or the door opens.
3. The bus is STOPPED in both shots: nothing slides past the windows, no motion blur, the glass door stays shut, nobody boards, no student appears — WRONG if the bus moves or anyone else shows up.
4. SHOT 2 is a medium shot, waist-up, from the first row of seats behind and to the right of him: he turns to the lens and speaks at 3–9s, a hand on the wheel — WRONG if he stands or the bus moves.
5. Only @MOTORISTA speaks, only this line — every other mouth closed. Daylight from frame-LEFT — NO music.""",
    timeline(2, [3], [
        "SHOT 1 (0–3s) — the MATCH FRAME, MCU of @MOTORISTA at the wheel, face dead centre, straight into the lens with a warm smile, the stopped bus soft behind him — the windshield, the aisle and the shut glass door on frame-LEFT — opening wider as the slow dolly-out runs the whole shot. HARD CUT.",
        "SHOT 2 (3–10s) — MS (waist-up: the driver at the wheel, the windshield and the stopped avenue soft behind him), 40°, handheld from the first row of seats behind and to the right of him: @MOTORISTA, one hand on the wheel, turns to the lens and speaks at 3–9s, glancing at the windshield and back, smiling; at 9–10s he holds the smile. Hard end.",
    ]),
    dialogue(line(3, 9, "MOTORISTA", "Se Minas tem o que o futuro procura, esse futuro também precisa chegar até os mineiros."), "MOTORISTA"),
    acting("MOTORISTA", "every day he takes people to where the opportunities are.",
           "greet you with a smile, then explain the route like one he loves — a hand on the wheel, eyes splitting between the windshield and you, checking you followed.",
           "on the lens in shot 1; in shot 2 between the windshield and the lens.",
           "his thumb taps the wheel once", "standing up, turning his whole body to the camera"),
    T.dolly_out(3) + """
SHOT 2: handheld, an operator with a body — breathing, small weight shifts, late corrections, never locked, drifting slowly around the driver. HORIZON: level.""",
    T.MATCH_FRAME,
    """GEOMETRY — driver's seat on the bus's left side, glass folding door on the right (frame-LEFT in shot 1, where the camera faces him from the windshield side), the cab exactly as in @ONIBUS_CAB (black fabric seat, black steering wheel with a plain hub, dash of rocker switches, fare validator on its post, flat rectangular mirror, yellow handrail by the seat); in shot 2 the camera in the first row behind and right of the driver, the windshield ahead.""",
    """PHYSICS & MATERIAL — the bus is still, the engine idling with a faint vibration; his thumb taps the wheel; light shifts softly on the glass. """ + REAL + """ MATERIAL TRUTH: the glass of the door, the grey rubber floor with its yellow edge line, yellow-painted handrails with grey clamp brackets, grey seat shells with blue patterned cushions, the cotton of his pale grey shirt.""",
    T.light_int("the bus's windshield and door-side windows",
                "no other source inside the bus.",
                "the daylight lights the frame-LEFT side of his face; the bus behind falls off a stop."),
    T.FILM_LOOK,
    f"""SOUND — LOCATION SOUND ONLY: the engine idling; a quiet stopped avenue outside, a distant horn; the fabric of his shirt as he turns; his voice. {T.MUSIC_POLICY}""",
    T.WORLD,
    f"""NEGATIVE: the door opening, a student or any boarding passenger, a moving bus, motion blur outside, rain or raindrops on the windows, a logo on the steering wheel, chrome or satin-steel handrails, a European or American bus interior, an all-grey interior, readable stickers or fare signs, him standing, the face drifting off centre or a zoom in shot 1, a generic or plain-looking man, extra cuts, {T.NEG_DOLLY}.""",
    """[ORDER: 2 shots, 1 hard cut at 3s, 10s — (1, 0–3s) MATCH FRAME medium close-up of the driver, face dead centre, smiling into the lens, slow dolly-out (no zoom) — (2, 3–10s) medium shot, waist-up, from the first row behind and right of him, the bus STOPPED: he turns to the lens and says his line at 3–9s, smiling. Invariants: Brazilian city-bus look (yellow handrails, blue patterned seats, grey rubber floor); the bus stopped, the door shut, no student; shot 1 face centred, camera backing away with no zoom; he speaks only in shot 2. Look: 35mm color negative, warm halation, lifted blacks, organic grain. Brazilian Portuguese. NO music. NO subtitles, NO text.]""",
)

# ---------------------------------------------------------------- T14
T14 = join(
    contract(6, "2 shots with 1 hard cut at 5s", "handheld in every shot"),
    f"""REFERENCES — each reference has ONE job:
@ESTUDANTE — IDENTITY of @ESTUDANTE: face, hair, build, hands and wardrobe exactly as on the sheet. 100% matches.
{SCOPE_ID}""",
    f"""WHO IS WHO — READ FIRST, ABSOLUTE:
@ESTUDANTE ({ANCH['ESTUDANTE']}) — the STUDENT: already facing the lens in the very first frame, a tablet low in one hand, ONE classmate beside him, speaks once to the lens, bumps fists with her; NEVER takes off the hoodie; NEVER looks or acts like a teacher.
CLASSMATE (unreferenced: a Brazilian girl of 15, braids, a grey T-shirt, jeans, sneakers) — the only person beside him, grinning at the robot; NEVER speaks.
OTHER STUDENTS — three or four teenagers of 15–16 in casual everyday clothes far behind at their own benches, each busy with something else (one soldering, one typing on a laptop whose screen faces away, two assembling a small chassis), soft, not looking at the lens or at the robot; NO uniforms, NO lab coats, NO adults; NEVER speak.
ROBOT — a small amateur robot about 20 cm tall that the students built themselves, on the bench just behind his shoulder: grey and white 3D-printed parts, visible servo motors, a bare microcontroller board with jumper wires, a few zip ties, a taped battery pack, a little crooked, hand-assembled, two small LED eyes; NOT a toy, NOT a polished product; no logos; it waves one arm side to side WITHOUT STOPPING for the whole take, in complete silence.
FACES: each face exists once.
CONTACT: the only touch is the fist bump in shot 2.""",
    """SCENE — Afternoon in the robotics workshop of a free technical course for teenagers in Belo Horizonte, Brazil — a bright, serious, organised room: neutral grey metal shelving with matte grey and black equipment cases and tidy cable reels, a 3D printer, a soldering station, closed laptops, long benches. @ESTUDANTE stands at a bench with his classmate, a tablet in his hand, the robot they built waving behind him.
THE SOUL OF THE SCENE (play it, never explain it): he and his friends built a robot that really works and he is thrilled — he tells you what this place is for, like one of the gang.""",
    f"""{LOCKS_HEAD}
1. Exactly 2 shots, 1 hard cut at 5s; handheld in every shot.
2. The tablet's SCREEN is NEVER visible: held low at his side with its back to the lens — WRONG if any screen, interface or screen glow is shown.
3. He is ALREADY facing the lens in the first frame (no turning) and speaks at 0–5s, eyes alive; the name Codemig is said exactly Cô-dê-mí-gui, with no R sound in it — WRONG if he turns first, if glassy, or if the name comes out as anything else; only he speaks.
4. @ESTUDANTE wears exactly his sheet wardrobe: dark charcoal (almost black) hoodie, white T-shirt hem showing below it, black skinny jeans — WRONG if anything changes.
5. ONE classmate beside him; everyone else is far behind, busy with their own work and not watching; all teenagers in casual clothes — WRONG if a crowd watches the robot or the lens, or any adult, uniform or teacher-like posture appears.
6. The robot is small, amateur and student-built, waves without stopping and makes NO sound at all — WRONG if it stops, whirs or beeps, or looks like a store-bought toy.
7. Neutral, matte, professional shelving and cases — WRONG if any box looks like a toy, colourful or cartoonish. Daylight from frame-LEFT; no readable text or logo — NO music.""",
    timeline(2, [5], [
        "SHOT 1 (0–5s) — MS (waist-up, the workshop soft around him), 40°: @ESTUDANTE at a long bench, already facing the lens, the tablet held low in one hand with its back to us, the amateur robot on the bench behind his shoulder waving its arm side to side without stopping, the CLASSMATE beside him grinning at it, the other students far behind busy at their own benches; he speaks at 0–5s, grinning with pride. HARD CUT.",
        "SHOT 2 (5–6s) — CU, 35°: he and the CLASSMATE bump fists, quick and happy, the robot still waving soft behind them. Hard end mid-bump.",
    ]),
    dialogue(line(0, 5, "ESTUDANTE", "É para isso que a Cô-dê-mí-gui existe… para fazer essa conexão acontecer."), "ESTUDANTE").replace(
        "\nVOICE LOCK",
        "\nPRONUNCIATION — the name is said Cô-dê-mí-gui: four even syllables, a closed ô and a closed ê, the stress on mí, and a last syllable that is just \"gui\" (a hard G and an i); there is NO R sound anywhere in the name — NEVER \"Codemigri\", \"Codemiji\" or \"Codemaig\"; said once, clearly, inside the sentence.\nVOICE LOCK"),
    acting("ESTUDANTE", "he and his friends built a robot that works.",
           "tell you, thrilled, what this place is for — check that you believe him, like a friend, not a teacher.",
           "on the lens throughout.",
           "a quick swallow, then the grin breaks", "a teacher's or presenter's posture, a cheeky smirk, a teenage pose, turning toward the camera"),
    "ACTING — CLASSMATE: TACTIC watch the robot, delighted, like a friend; eyes on the robot, then on him; NOT speaking, NOT looking at the lens.\nACTING — OTHER STUDENTS (background): absorbed in their own work; NOT looking at the lens, NOT speaking.",
    T.handheld(),
    """PHYSICS & MATERIAL — the robot's single arm swings side to side on its servo, a little stiff and uneven, a little endearing, without a sound; the tablet is a thin slab with a matte case; the fist bump lands with a soft knock. """ + REAL + """ MATERIAL TRUTH: the matte-grey case of the tablet, the slightly uneven grey and white 3D-printed parts of the robot with visible screws, jumper wires, zip ties and a taped battery pack, the matte cotton knit of his hoodie, neutral matte grey metal shelving, dark grey and black equipment cases, coiled cables, a 3D printer and a soldering station, the everyday cotton T-shirts and hoodies of the students.""",
    T.light_int("the workshop's big windows",
                "the robot's two small LED eyes as tiny practicals.",
                "the daylight lights the frame-LEFT side of his face and the bench; the room behind falls off a stop."),
    T.FILM_LOOK,
    f"""SOUND — LOCATION SOUND ONLY: a fan humming; students working and chatting low at far benches, no words standing out; the fist bump. The robot makes NO sound. {T.MUSIC_POLICY}""",
    T.WORLD,
    f"""NEGATIVE: a visible tablet screen or any screen content, mispronouncing the name (Codemigri, Codemiji, Codemaig), a robot motor whirr, servo noise or beeps, a robot that stops waving, a large, polished, store-bought or toy robot, toy-like boxes, colourful storage boxes, cartoon packaging, a children's playroom look, a crowd watching the robot, an adult, a teacher, uniforms, lab coats, a classroom lesson posture, him turning to the lens, different wardrobe from the sheet, programme logo, posters with text, readable labels, extra cuts, {T.NEG_SPINE}.""",
    """[ORDER: 2 shots, 1 hard cut at 5s, 6s, handheld — (1, 0–5s) medium shot, waist-up: already facing the lens, the tablet low at his side with its back to us, the little amateur robot waving without stopping behind his shoulder, one classmate beside him, the others busy far behind; he says his line at 0–5s, proud, the name said Cô-dê-mí-gui with no R in it — (2, 5–6s) CU: a quick fist bump, the robot still waving behind. Invariants: no tablet screen ever visible; he faces the lens from the first frame; one classmate beside him, the rest busy and far away, all teenage and casual, no adults, no teacher look; a small amateur student-built robot that waves silently the whole time; neutral matte professional shelving, nothing toy-like; the sheet wardrobe; living eyes; handheld. Look: 35mm color negative, warm halation, lifted blacks, organic grain. Brazilian Portuguese. NO music. NO subtitles, NO text.]""",
)

# ---------------------------------------------------------------- T15
T15 = join(
    contract(8, "ONE continuous take, no cuts", "handheld, the camera backing up ahead of her as she walks and talks, round a 90-degree corner"),
    f"""REFERENCES — each reference has ONE job:
@ENFERMEIRA — IDENTITY of @ENFERMEIRA: face, hair, build, hands and wardrobe. 100% matches.
{SCOPE_ID}""",
    f"""WHO IS WHO — READ FIRST, ABSOLUTE:
@ENFERMEIRA ({ANCH['ENFERMEIRA']}) — the NURSE: already walking down the hospital corridor toward us and already speaking in the first frame, lifts a chart folder from the wall holder in passing, rounds a 90-degree corner of the corridor with the camera and keeps walking, speaking the whole time; NEVER stops, NEVER cares for a sick person on camera.
FACES: her face exists once; nobody else in the frame.
CONTACT: nobody touches anyone.""",
    """SCENE — Afternoon in a modern, recently built Brazilian hospital, in a long, bright corridor: smooth pale-grey and white walls with a warm wood-veneer band at hip height, a light polished-vinyl floor with a soft sheen, closed wood-veneer doors with narrow glass panels, wall-mounted chart holders beside the doors, a long line of recessed linear LED ceiling lights, and ahead a true 90-degree corner where the corridor turns, nothing on the walls readable. @ENFERMEIRA is already walking down it.
THE SOUL OF THE SCENE (play it, never explain it): caring is her job and she is proud of it — she tells you on the move, like a friend walking you down her ward, brisk and bright, and gives you a warm look at the end.""",
    f"""{LOCKS_HEAD}
1. ONE continuous handheld take, no cuts, and she never stops walking — WRONG if it cuts or she stops.
2. The scene is ALREADY in progress at the first frame: she is walking in the corridor and already speaking — WRONG if she enters from a room, starts late or begins still.
3. MEDIUM SHOT (waist-up), 40°, for the whole take, the lens backing up ahead of her at her walking pace and keeping the same distance — WRONG if the camera is ever static, goes wide or goes close.
4. In the MIDDLE of the take the corridor turns a true 90° corner: the camera, still backing up, swings round the corner and she turns with it, the walls sliding past and the new corridor opening behind her, without a break in her stride or her speech — WRONG if there is no real corner or the camera cuts or loses her.
5. She speaks the whole sentence in one brisk, upbeat flow, no silent gap and no drawn-out words, finishing at about 7s; she takes the chart folder from the wall holder IN MOTION in the first seconds, without breaking stride or speech — WRONG if she is slow, pauses or turns to the wall.
6. No room interior, bed or sick person is ever shown; the corridor is bright, modern and clean, lit by artificial ceiling light only — NO music.""",
    timeline(1, [], [
        "BEAT 1 (0–3s) — MS (waist-up), 40°, handheld, the lens backing up ahead of her down the long straight corridor: @ENFERMEIRA is already walking toward us and already speaking, eyes on the lens, a bright easy smile; in passing her free hand lifts a slim grey chart folder from the holder on the wall beside her and tucks it against her chest without breaking stride or speech, a quick glance down at it and back to the lens.",
        "BEAT 2 (3–6s) — the corner: the corridor turns a true 90 degrees to frame-LEFT; the camera, still backing up ahead of her, swings round the corner and she follows, turning with it, the walls sliding past and the new corridor opening behind her; she keeps walking and speaking the whole way, eyes on the lens.",
        "BEAT 3 (6–8s) — the new corridor runs straight; she walks on toward us with the chart against her chest, finishes her sentence at about 7s and gives you a warm look, still walking. Hard end mid-step.",
    ]),
    dialogue(
        line(0, 7, "ENFERMEIRA", "Para fazer com que os recursos essenciais para a transição energética que o mundo precisa, também criem oportunidades para Minas.").replace(
            "(on camera, Brazilian Portuguese)",
            "(on camera, Brazilian Portuguese; from the very first frame, a brisk, upbeat pace with no drawn-out words)"),
        "ENFERMEIRA"),
    acting("ENFERMEIRA", "caring is her job and she is proud of it.",
           "tell you on the move like a friend walking you down her ward — brisk, bright, no drag — and give you a warm look to check you understood why she is here.",
           "on the lens, with a quick glance at the chart when she takes it.",
           "she wets her lips and smiles", "stopping, turning her body to the camera, a dramatic hospital scene, a slow drawl"),
    """CAMERA — handheld, an operator with a body: breathing, small weight shifts, late corrections; never locked, never static. The operator walks BACKWARD ahead of her at her walking pace and keeps the same distance, and in the middle of the take swings round a true 90-degree corner of the corridor with her, still backing up.
OPTICS: 40° throughout. FOCUS: on her eyes; the corridor soft behind. HORIZON: level.
NOT: tripod, locked-off frame, gimbal glide, drone, push-in, zoom, the camera stopping, a cut at the corner.""",
    """GEOMETRY — the corridor runs straight away from the camera for about 8 m, with the chart holder on the wall at frame-RIGHT, her left hand taking the folder; then a true 90-degree corner to frame-LEFT; after it a second straight stretch; the lens 2.5 m ahead of her throughout.""",
    """PHYSICS & MATERIAL — the folder slides out of its holder with a small scrape; her soft rubber soles squeak faintly on the vinyl; the chart's paper sheets shift under her arm; her scrub tunic swings a little as she turns the corner. """ + REAL + """ MATERIAL TRUTH: the satin wood veneer, the polished pale vinyl with soft reflections of the ceiling lights, the matte painted walls, the crisp cotton of her white scrubs, the slim grey chart folder with unreadable paper.""",
    T.LIGHT_ARTIFICIAL.replace("CONTINUITY: the key stays above-front on frame-LEFT in every shot; lit sides never flip.",
                               "CONTINUITY: the key is the corridor's continuous ceiling strips, above and in front of her through the whole take, also round the corner; the light never changes character."),
    T.FILM_LOOK,
    f"""SOUND — LOCATION SOUND ONLY under her voice: her footsteps on the vinyl; the folder's paper; a ventilation hum; a trolley rolling far down the corridor; the ward's low murmur with no words standing out. {T.MUSIC_POLICY}""",
    T.WORLD,
    f"""NEGATIVE: a cut, a static camera, her stopping, entering from a room, a door closing behind her, a slow or drawling delivery, a silent gap in her speech, a late start, a corner that is only a soft curve, the inside of a room, a bed, a sick or dying person, blood, an IV drip, green fluorescent light, a dim or grim corridor, an old run-down hospital, daylight windows, readable signs or chart text, hospital logos, turning her body to the camera, other people in focus, {T.NEG_SPINE}.""",
    """[ORDER: ONE handheld take, 8s, medium shot waist-up, the camera backing up ahead of her — (0–3s) the scene already in progress: she is walking down the straight corridor and already speaking, her free hand lifts the chart folder from the wall holder in passing — (3–6s) a true 90-degree corner: the camera swings round it still backing up and she turns with it, no break in stride or speech — (6–8s) the new corridor, she finishes at about 7s with a warm look; hard end mid-step. Invariants: no cuts, she never stops, the camera never static; she is in motion and speaking from the first frame in a brisk, upbeat flow; a real 90-degree corner mid-take; modern, bright, clean corridor with artificial light only; no room interior or sick person shown. Look: 35mm color negative, warm halation, lifted blacks, organic grain. Brazilian Portuguese. NO music. NO subtitles, NO text.]""",
)

# ---------------------------------------------------------------- T16
T16 = join(
    contract(11, "ONE continuous take, no cuts", "handheld, close and breathing, tight close-up"),
    f"""REFERENCES — each reference has ONE job:
@JOVEM — IDENTITY of @JOVEM: face, skin texture, hair and wardrobe 100% matches.
{SCOPE_ID}""",
    f"""WHO IS WHO — READ FIRST, ABSOLUTE:
@JOVEM ({ANCH['JOVEM']}) — the PROTAGONIST: speaks his last words to you; his face fills the frame just left of centre.
FACES: his face exists once; nobody else.""",
    """SCENE — The same summit in Minas Gerais, Brazil, at the same late-afternoon hour; @JOVEM, in a very tight close-up, is already looking at you; the sea of hills is a soft haze behind him.
THE SOUL OF THE SCENE (play it, never explain it): he has shown you everything and he is happy and sure — "O minério é nosso" is pride, "O futuro também" is an invitation.""",
    f"""{LOCKS_HEAD}
1. ONE handheld take in a very tight close-up — WRONG if it cuts, widens or is locked.
2. His eyes stay on the lens and alive from start to finish — WRONG if glassy or looking away.
3. Real skin in detail: pores, stubble, the small mole on his left cheek (frame-right as he faces the lens) — WRONG if smooth or retouched.
4. Only @JOVEM speaks, only this text.
5. Sun from frame-LEFT — NO music.""",
    timeline(1, [], [
        "BEAT 1 (0–1s) — CU, 18°, handheld 1.3 m from his face, breathing: his face from the eyebrows to the chin, just left of centre, eyes already on the lens.",
        "BEAT 2 (1–9s) — he speaks to the lens, proud and warm, the smile growing.",
        "BEAT 3 (9–11s) — he holds your eyes with an open smile. Hard end on the held look.",
    ]),
    dialogue(line(1, 9, "JOVEM", "Para transformar a força que vem da nossa terra em mais desenvolvimento para a nossa terra. O minério é nosso. O futuro também."), "JOVEM"),
    acting("JOVEM", "everything he showed you comes down to this, and he is proud of it.",
           "look at you from close up, share it with pride and invite you in — look for your yes.",
           "on the lens throughout, moving between your two eyes.",
           "a small laugh of breath at the end", "a slogan delivery, a wink, tears"),
    T.handheld(),
    """PHYSICS & MATERIAL — the wind from frame-left moves a few hairs at his temple and the edge of his collar; his breath moves his lips and nostrils; his skin catches the light unevenly. """ + REAL + """ MATERIAL TRUTH: pores and fine lines at the eyes, stubble with individual hairs, the weave of his overshirt collar.""",
    T.LIGHT_EXT,
    T.FILM_LOOK,
    f"""SOUND — LOCATION SOUND ONLY: wind across the open summit, steady and quiet; dry grass hissing; his breath; after his last word, only the wind. {T.MUSIC_POLICY}""",
    T.WORLD,
    f"""NEGATIVE: a cut, widening the frame, smooth retouched skin,  watery eyes, tears, a wink, slogan delivery, looking away, {T.NEG_SPINE}.""",
    """[ORDER: ONE handheld take, 11s, tight CU 18° — (0–1s) eyes on the lens — (1–9s) his words to you, proud and warm — (9–11s) he holds your eyes, smiling. Invariants: handheld, tight close-up; living eyes on the lens; real skin; only his words; sun frame-LEFT. Look: 35mm color negative, warm halation, lifted blacks, organic grain. Brazilian Portuguese. NO music. NO subtitles, NO text.]""",
)
