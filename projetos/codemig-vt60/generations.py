# CODEMIG · VT 60" — gerações v2 (prompts CINEORO completos).
# Cada prompt é uma ilha: monta a espinha inteira e cola os templates de templates.py.
# Gramática v2: câmera na mão sempre; subações em close; a fala no plano mais aberto, entre cortes.

import templates as T

ANCH = {
    "JOVEM": "25, Brazilian, mixed-race light-brown skin, lean, short black curly hair, ears that stick out slightly, light patchy stubble, a small mole on his left cheek, rust-red cotton overshirt open over a white T-shirt, black slim jeans, brown leather hiking boots with black toe caps, charcoal-grey backpack",
    "ALUNO": "10, Black Brazilian boy, slim, dark brown skin, short tight black curls, soft oval face, large dark brown eyes with long lashes, sage-green school T-shirt with no emblem, black shorts, black strapped sport sandals",
    "PROFESSORA": "40, white Brazilian woman, medium build, dark brown hair centre-parted in a low bun with loose strands framing the face, dense freckles across the nose and cheeks, mauve satin blouse with a band collar tucked into charcoal-grey straight-leg trousers, brown flats, a silver wristwatch on the left wrist",
    "HOMEM_EV": "34, mixed-race Brazilian man, light olive-tan skin, fit, short black hair swept up and back with tapered sides, thick dark eyebrows, short full dark beard and moustache, plain red short-sleeved cotton piqué polo shirt with a ribbed collar and a two-button placket, worn untucked, no logo and no text on it, mid-blue straight-leg jeans, tan smooth-leather lace-up sapatênis (casual sneaker-shoes) with white rubber soles, silver steel watch on the left wrist, gold ring",
    "OPERARIO": "40, mixed-race (pardo) Brazilian man, heavyset and broad-shouldered, round full face with freckled cheeks, close-shaved head, short full black beard flecked with grey, white hard hat with no logo, clear wraparound safety glasses, orange ear muffs around his neck, dark charcoal-grey flame-retardant coverall with silver reflective strips over the shoulders, chest, forearms and shins, grey knit work gloves, black leather safety boots",
    "DONO": "60, white Brazilian man, solid build, broad deeply lined face with age spots, large nose and ears, grey-hazel eyes, thick bushy white-grey moustache covering the upper lip, short white hair thinning on top, cream short-sleeved camp-collar shirt with a chest pocket, very dark navy knee-length waist apron, dark grey trousers, tan leather loafers",
    "AGRICULTORA": "40, mixed-race Brazilian woman, slim, warm brown skin, long face with high cheekbones and fine lines, long black hair in a single thick braid worn over her left shoulder, tan felt wide-brim hat with brown leather trim sitting just above the eyebrows, sage-green long-sleeved button-up shirt with two flap chest pockets worn untucked, dark indigo jeans, dark brown lace-up leather work boots, tortoiseshell sunglasses hooked on the shirt front",
    "FUNCIONARIO": "30, mixed-race Brazilian man, medium build, medium brown skin, short black hair, thick straight eyebrows, broad nose, full lips, clean-shaven with a faint stubble shadow, glossy white hard hat with black chin strap fastened and no logo, clear wraparound safety glasses, orange high-visibility vest with grey reflective strips over a long-sleeved dark charcoal collared work shirt worn untucked, black cargo work trousers, grey padded work gloves, black lace-up work boots",
    "LOJISTA": "46, mixed-race (parda) Brazilian woman, medium height, soft average build, warm medium-brown skin with a golden undertone and fine laugh lines, round-oval face with soft full cheeks, small rounded nose, full lips, a tiny mole above the right corner of the upper lip, short natural curly dark-brown hair cut to the chin with silver strands at the temples, slim oval glasses with thin burgundy metal frames, small silver hoop earrings, plain muted teal cotton button-up dress shirt (a simple camisa social) with a regular soft collar, plain tonal buttons closed up to the second button, no chest pocket, long sleeves rolled to the forearms, worn untucked, straight dark-charcoal trousers, simple closed black leather flats, slim steel watch on the left wrist",
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


PACE = ("PACING — each line in ONE brisk, continuous flow (about 3 words a second): only a breath between "
        "phrases, no pause, no held beat, no trailing off; the first word lands as the window opens.")


def dialogue(*lines_and_tags, pace=PACE):
    lines = [x for x in lines_and_tags if x.startswith("[")]
    tags = [x for x in lines_and_tags if not x.startswith("[")]
    return "\n".join([DLG] + lines + ([pace] if pace else []) + [T.voice_lock(t) for t in tags])


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
    L = dict(j="0–2", a="5–6", p="6–9", nospeech="3–5") if short else dict(j="0–2", a="12–13", p="13–16", nospeech="3–12")
    ramp = (" SPEED RAMP: the descent leaves the man at once, peaks through stone, ore and beams with heavy motion blur, and decelerates smoothly into the landing; about 1.5 s of screen time.") if short else ""
    b1 = "BEAT 1 (0–3s) — CU, 47°, handheld, frontal and centred: @JOVEM already facing the lens, shoulders square, mid-smile, as in the last frame of the previous wide take; he speaks at once, in one flowing breath, the line done by about 2 s; he holds the mid-smile until 3 s and the camera sinks."
    landing = "lands at a seated child's eye height on a medium shot of @ALUNO at his desk in the centre of the frame."
    if short:
        beats = [b1,
            "BEAT 2 (3–5s) — the descent, level and facing forward, as a speed ramp: down his body and boots, through a thin crust of topsoil in a flash (plain brown soil, a few fine pale grass roots, small and quiet), then down through layered grey stone and a broad seam of banded iron ore with metallic glints, the body of the descent, out through steel roof beams, past a white ceiling fan ON and spinning fast, into the bright classroom; it decelerates and " + landing,
            "BEAT 3 (5–6s) — handheld settles on the happy classroom; @ALUNO answers, looking toward the front; mid-line @PROFESSORA enters from frame-RIGHT, crouching beside his desk, and the camera pans slightly right to frame her.",
            "BEAT 4 (6–9s) — @PROFESSORA, crouched, face turned toward him, speaks to HIM in the voice and teacher's manner of @Audio1 with ONE quick glance to the lens mid-line; @ALUNO looks at her and, as she finishes, nods and smiles, the happy classmates around them. Hard end on the smile."]
        order_t = "(0–3s) @JOVEM's line (done by 2s), a held smile, the camera sinks at 3s — (3–5s) speed-ramp descent to @ALUNO — (5–6s) \"É futuro.\", @PROFESSORA crouches in from frame-RIGHT — (6–9s) her line to him with one glance to the lens, he nods and smiles"
    else:
        beats = [b1,
            "BEAT 2 (3–5s) — the camera sinks straight down, level and facing forward: his chest, overshirt, hands, legs and boots on the lichen rock slide up past the lens.",
            "BEAT 3 (5–8s) — below the ground line: a thin crust of topsoil for a flash (plain brown soil, a few fine pale grass roots, small and quiet), then layered grey stone sliding upward and a broad dark seam of banded iron ore with metallic glints, which fill most of these seconds.",
            "BEAT 4 (8–10s) — out of the ore, steel roof beams rise past the lens; the camera passes between them and down through the gridded classroom ceiling beside a white ceiling fan that is ON, blades spinning fast.",
            "BEAT 5 (10–12s) — down into the bright classroom, decelerating, desks with seated students rising into view and, behind the boy, the bright back wall with its cabinet, bookshelf and drawings; it " + landing,
            "BEAT 6 (12–13s) — handheld settles; @ALUNO answers, looking toward the front; mid-line @PROFESSORA enters from frame-RIGHT, crouching beside his desk, and the camera pans slightly right to frame her.",
            "BEAT 7 (13–16s) — @PROFESSORA, crouched, face turned toward him, speaks to HIM in the voice and teacher's manner of @Audio1 with ONE quick glance to the lens mid-line; @ALUNO looks at her.",
            "BEAT 8 (16–18s) — @ALUNO nods and smiles, the happy classmates around them; the two hold. Hard end on the smile."]
        order_t = "(0–3s) @JOVEM's line (done by 2s), a held smile, the camera sinks at 3s — (3–5s) down his body — (5–8s) a flash of topsoil, then stone and ore — (8–10s) beams, ceiling, fan — (10–12s) lands on @ALUNO — (12–13s) \"É futuro.\", @PROFESSORA crouches in — (13–16s) her line to him with one glance to the lens — (16–18s) he nods, smiles"
    return join(
        contract(total, "ONE continuous take, no cuts", "one continuous level vertical descent that follows the attached 3D blocking video, handheld" + (", with a speed ramp in the descent" if short else ""), extra=" (speech only when the camera is not travelling)"),
        f"""REFERENCES — each reference has ONE job:
@JOVEM — IDENTITY of @JOVEM: face, hair, build, hands, wardrobe, backpack. 100% matches.
@PICO_FRAME — PLACE AND WARDROBE STATE of the summit: lichen rock, green hills, sky, low warm sun from frame-left, and how his rust-red open overshirt, white T-shirt, black jeans, boots and backpack sit on him; beat 1 is the same place and clothes seen close.
@ALUNO — IDENTITY of @ALUNO: face, hair, build, hands, wardrobe. 100% matches.
@PROFESSORA — IDENTITY of @PROFESSORA: face, hair, build, hands, wardrobe. 100% matches.
@Audio1 — VOICE of @PROFESSORA: the timbre, accent and teacher's manner of this recording, in which a teacher says "E minério não é só minério, viu?" — the very line she says here. 100% matches her voice and manner. Take nothing else from it.
@Video1 — MOTION ONLY: the camera path, framing and timing of this 3D blocking (close-up, level descent, landing on the seated boy, slight pan right as the teacher crouches in). Take NOTHING else: ignore its flat colours, low-poly shapes, its brown sticks (they stand for roots, which here are tiny) and every word in it.
{SCOPE_ID} @Audio1 supplies her voice ONLY. @PICO_FRAME supplies place, light and wardrobe ONLY — not its framing, not his pose, not a start frame, nothing of his face.""",
        f"""WHO IS WHO — READ FIRST, ABSOLUTE:
@JOVEM ({ANCH['JOVEM']}) — the PROTAGONIST on the summit: one line in close-up, then the camera leaves him.
@ALUNO ({ANCH['ALUNO']}) — the STUDENT: seated at his desk, centre of frame, facing the front of the room (the whiteboard is behind the camera, never in frame); notebook and pencil case on his desk; answers, then looks at the teacher and agrees with a smile; NEVER stands.
@PROFESSORA ({ANCH['PROFESSORA']}) — the TEACHER: enters from frame-RIGHT crouching beside his desk, three-quarter view from behind-side, face turned toward HIM; speaks to him, her eyes on him, with ONE quick glance to the lens mid-line and back; NEVER sits.
CLASSMATES: about ten students at their own desks in rows, same light-green school T-shirt, all facing the front; distinct faces; HAPPY — smiling, relaxed, bright-eyed, one nudging another, a couple laughing without a sound; silent; soft.
FACES: each face exists once; no twins, no clones.""",
        """SCENE — Late afternoon on a mountain summit in Minas Gerais, Brazil, @JOVEM in close-up, looking at you. When he has spoken, the camera sinks straight down through the ground — a thin crust of soil, then stone and iron ore, then the steel of a roof — into a bright, recently built Brazilian public school classroom, warm and lived-in. A student answers and his teacher crouches in beside him.
THE SOUL OF THE SCENE (play it, never explain it): earth, ore, steel, school — one chain, one movement; the man who loves the land hands the film to the boy who is its future.""",
        f"""{LOCKS_HEAD}
1. ONE continuous take, ONE level vertical descent following @Video1, through only a flash of plain soil with tiny grass roots and then mostly stone and iron ore — WRONG if it cuts, tilts down, flies like a drone, shows big or glowing roots or lingers on the soil.
2. The camera starts sinking at 3s, right after @JOVEM finishes his line (done by 2s) and holds the smile a beat — WRONG if it sinks before his line ends or he speaks while it sinks.
3. No speech while the camera travels ({L['nospeech']}s): lines only at {L['j']}s (@JOVEM), {L['a']}s (@ALUNO), {L['p']}s (@PROFESSORA), each in the right mouth.
4. NO sound effects of any kind, and the ceiling fan is ON and visibly spinning — WRONG if any rumble, whoosh or hum is heard or the fan is still.
5. @ALUNO centred; @PROFESSORA enters from frame-RIGHT, crouched, mid-line, speaks to HIM with ONE quick glance to the lens; he looks at her, nods, smiles — WRONG if she enters from the left, speaks to the lens or stares at it.
6. NO whiteboard behind the boy; his back wall holds a cabinet, a bookshelf and children's drawings; the classmates are HAPPY — WRONG if the wall is bare; handheld; light from frame-LEFT — NO music.""",
        timeline(1, [], beats),
        dialogue(f'[{L["j"]}s] @JOVEM (on camera, Brazilian Portuguese, speaking up over the wind, in one flowing breath with no pause after "Em Minas,"): "Em Minas, terra não é só terra."',
                 f'[{L["a"]}s] @ALUNO (on camera, Brazilian Portuguese): "É futuro."',
                 f'[{L["p"]}s] @PROFESSORA (on camera, Brazilian Portuguese, in the voice and the teacher-like manner of @Audio1, said kindly with a warm face, speaking to the boy; the whole line, from the "E" to the "viu?"): "E minério não é só minério, viu?"',
                 "JOVEM", "ALUNO", "PROFESSORA", pace=None).replace(T.voice_lock("PROFESSORA"), "VOICE LOCK — @PROFESSORA: the voice and teacher's manner of @Audio1. Identical in every generation of the film."),
        """ACTING — happy and proud of what they say; pupils search, settle and drift; a frozen pupil is wrong.
@JOVEM: TACTIC say it like good news to a friend; eyes on yours; NOT a heroic pose, a solemn face.
@ALUNO: TACTIC answer simply, then turn to the teacher, take her correction with a nod and a smile; NOT a cute pose.
@PROFESSORA: TACTIC complete his answer kindly, crouched to his level, eyes on him, with ONE quick glance to the lens mid-line as if sharing it with you; NOT lecturing, pointing, staring at the lens.
Classmates: happy, relaxed, silent; NOT looking at the lens.""",
        """CAMERA — follows @Video1's path and timing, handheld (small human sway, never a mechanical glide); level and facing forward the whole descent, never tilting.""" + ramp + """ After landing it stays handheld and makes one slight pan right to frame @PROFESSORA as she enters.
OPTICS: 47° throughout; no zoom. FOCUS: @JOVEM's eyes in beat 1; whatever passes the lens in the descent; then the faces of the exchange.
NOT: a cut, a tilt down, a drone, a CGI fly-through, a zoom, a locked tripod frame.""",
        """GEOMETRY — classroom: windows along the frame-LEFT wall; the whiteboard is on the front wall behind the camera, out of frame; @ALUNO at a second-row desk, centre of frame, 1.6 m from the lens; desks with seated students to both sides, soft; @PROFESSORA crouching at frame-RIGHT, 50 cm from his desk; back wall behind the boy: a light-wood cabinet at frame-LEFT, a bookshelf of colourful books at frame-RIGHT, rows of children's drawings (suns, trees, houses, a rocket, no writing) pinned between.""",
        """PHYSICS & MATERIAL — strong wind tugs at his collar and hair; in the descent a little loose soil and small stones fall past the lens, a few fine grass roots sway, the ore glints; the white ceiling fan spins fast, blades motion-blurred. """ + REAL + """ MATERIAL TRUTH: the weave of his overshirt, plain brown topsoil with fine pale grass roots, layered grey stone, banded hematite, matte steel, new laminate desks, the light wood of the cabinet, book spines (nothing legible), crayon drawings on paper.""",
        """LIGHT — MOTIVATED, one dominant natural source per place with real falloff and soft-edged shadows.
SUMMIT: low sun ~4300 K from frame-LEFT. THE GROUND: as if sliced open in that same soft daylight — readable, never black, no invented lamp, no orange or red glow. CLASSROOM: window daylight from frame-LEFT ~5600 K; the room a stop darker; corners allowed to fall into shade.
NOT: a headlamp, glowing underground light, glowing roots, lava-like colour, flat ceiling-panel key, frontal fill.""",
        T.FILM_LOOK,
        f"""SOUND — NO SOUND EFFECTS ANYWHERE: nothing designed or synthetic during the descent — no rumble, whoosh, scraping, stones, hum, riser or impact. Only: strong wind across the summit under his line ({L['j']}s), dropping to near silence as the camera sinks below the ground; then, from the landing, the quiet room tone of a classroom — the soft whir of the spinning fan, a faint happy student murmur that drops during the lines. {T.MUSIC_POLICY}""",
        T.WORLD,
        f"""NEGATIVE: sound effects, rumble, whoosh, text from the blocking video, low-poly shapes, a cut, a tilt down, speech during the descent, a classmate speaking, the teacher entering from the left or staring at the lens, a stopped fan, a whiteboard in frame or behind the boy, a bare or sober back wall, sad or bored classmates, readable writing on drawings or book spines, cutting the teacher's line short (dropping the "E" or the "viu?"), big, thick or glowing roots, lava-like orange or red glow in the ground, a soil layer as long as the stone, a CGI cross-section, glowing ore, a black frame, {T.NEG_SPINE}.""",
        f"""[ORDER: ONE continuous take, {total}s, following @Video1, handheld{', speed-ramp descent' if short else ''} — {order_t}. Invariants: one level descent; only a flash of plain soil with tiny grass roots, then mostly stone and ore; sinks at 3s, right after his line; no speech while travelling; NO sound effects; fan ON; teacher from frame-RIGHT in the voice of @Audio1, the whole line "E minério não é só minério, viu?", one glance to the lens; happy classmates; cabinet, bookshelf, drawings. Look: 35mm color negative, warm halation, lifted blacks, organic grain. Brazilian Portuguese. NO music. NO subtitles, NO text.]""",
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
    """REFERENCES — each reference has ONE job:
@HOMEM_EV — IDENTITY of @HOMEM_EV: face, hair, beard, build and hands. 100% matches. His CLOTHES do not come from the reference: he wears the red polo, jeans and sapatênis written below — IGNORE any suit, dress shirt, tie or shoes shown in it.
@CARRO_EV (only if attached) — OBJECT: the car and the charging post exactly as shown, plugged together by the short cable; IGNORE its background, light and framing.
@image 1 (only if attached) — LANDSCAPE: the mountain ridge behind the city, its shape and colours only: a long, continuous, gently undulating ridge, olive-green and brown with reddish earth scars; IGNORE its buildings, sky, clouds, light and framing.
REFERENCE SCOPE: the character reference supplies face, hair, beard, build and hands ONLY — IGNORE its clothes, its grey backdrop, studio lighting, exposure and colour grade.""",
    f"""WHO IS WHO — READ FIRST, ABSOLUTE:
@HOMEM_EV ({ANCH['HOMEM_EV']}) — the CAR OWNER: plugs in the charger, speaks once, pats the car; NEVER poses beside the car, NEVER walks out of frame before shot 4; his clothes are casual and identical in every shot — red polo, jeans, sapatênis — never a suit, never a dress shirt.
THE CHARGER — a slim brushed-steel public charging post (a totem about 1.5 m tall, a dark blank screen, a thin green status light, a cable holster) stands right beside the car's charge port; its own short cable runs from it to the port in one gentle arc, fixed at both ends, never loose, coiled or trailing on the ground.
FACES: his face exists once; passers-by far behind are distinct soft Brazilian figures.
CONTACT: nobody touches him.""",
    """SCENE — Late afternoon in a wide open-air car park of a modern building in Belo Horizonte, Brazil: white-lined parking bays on clean asphalt with concrete wheel stops and lamp posts, two or three other cars far back, a few flowering pink ipê trees along the far edge at mid-distance. The car park sits on a rise, so beyond the ipês the city spreads out below and behind — tall modern towers mixed with a few low, restored historic buildings in colonial style (whitewashed façades, red-tile roofs, tall shuttered windows) — and far behind it, across the whole width of the horizon, the Serra do Curral: a long, continuous, wall-like ridge with a gently undulating, almost level crest, olive-green and warm brown slopes with a few reddish earth scars, softened only a little by the evening haze, its foothills dotted with the city's buildings (never a single peak, a cliff or a sheer rock face). In the foreground, the green charging bay with a white plug pictogram (no letters) and the slim steel charging post right beside the car. @HOMEM_EV, in a red polo, jeans and sapatênis, is already plugging his small dark-grey compact electric hatchback (no badges) into it.
THE SOUL OF THE SCENE (play it, never explain it): he did the maths, switched to electric and loves it — he tells you like someone who found a great deal.""",
    rev_locks(4, [3, 5, 8], "HOMEM_EV", "É a possibilidade de um mundo mais verde,").replace(
        "speaks only in the medium-wide shot", "speaks only in the wide shot").replace(
        "5. Light from frame-LEFT — NO music.",
        "5. WARDROBE, identical in every shot: a plain RED polo, mid-blue jeans and tan sapatênis — WRONG if he wears a suit, a jacket, a dress shirt, a tie or any other clothes, even if the reference shows them.\n"
        "6. THE CHARGER is clearly a charging point in the wide shot: the steel totem stands right beside the car's charge port and the car is plugged into it by a short cable in one gentle arc, fixed at both ends — WRONG if there is no post, or the cable goes nowhere, has a free end, or lies, coils or trails on the ground.\n"
        "7. BACKGROUND in the wide shot: a real open-air car park (painted bays, wheel stops, lamp posts, other cars far back), the ipê trees at mid-distance, the Belo Horizonte skyline behind them (tall modern towers mixed with a few low, restored colonial-style buildings) and, behind it, the Serra do Curral as a long, even, gently undulating green-and-brown ridge — WRONG if the lot is empty or looks like a viewpoint, the city is missing, hidden, blurred or generic, the mountain is a lone peak, a mesa or a cliff, or any church, bell tower or steeple appears.\n"
        "8. Light from frame-LEFT — NO music."),
    timeline(4, [3, 5, 8], [
        "SHOT 1 (0–3s) — ECU, 47°, lens 40 cm from the car: his hand — the red sleeve of his polo, the steel watch and the gold ring in frame — guides the charging connector into the car's port, the thick cable leading out of frame toward the charging post; the first push meets resistance, he lines it up and pushes again until it seats with a click. HARD CUT.",
        "SHOT 2 (3–5s) — CU, 47°: the light ring around the charging port glows on; his hand lets go of the connector and the thick cable settles into one gentle arc running to the brushed-steel charging post soft beside it, its other end fixed in the post. HARD CUT.",
        "SHOT 3 (5–8s) — WS (his whole body from head to shoes, the car and the charging post beside him), 63°, the camera about 4.5 m away at chest-to-eye height, deep focus: the car plugged into the post by its short cable, @HOMEM_EV just right of the post at the right third in his red polo, jeans and sapatênis, turns to the lens and speaks at 5–8s, a pleased half-smile, drifting toward the centre as the camera passes; behind them the painted bays and a few far cars, the ipê trees, the Belo Horizonte skyline and the long ridge of the Serra do Curral, readable. HARD CUT.",
        "SHOT 4 (8–10s) — CU, 47°: his hand pats the car roof twice, satisfied, the red sleeve and the steel watch in frame, the ipê blossoms and the city soft behind, and he steps off frame-right. Hard end mid-step.",
    ]),
    dialogue(line(5, 8, "HOMEM_EV", "É a possibilidade de um mundo mais verde,"), "HOMEM_EV"),
    acting("HOMEM_EV", "he made a smart choice and it paid off.",
           "share it casually, with the pleasure of someone who found a good deal — check from the corner of his eye that you're convinced.",
           "on the connector, then a sidelong look to the lens.",
           "he blows a short pleased breath through his nose", "a salesman pitch, a thumbs-up"),
    T.REV_CAMERA.replace("backgrounds slide past soft.", "backgrounds slide past soft in the inserts; in the wide shot the depth of field is deep — the post, the car park and the city behind him stay readable, only gently soft, NO creamy bokeh."),
    """GEOMETRY — the car sits in its green charging bay, nose to frame-left, its charge port on the rear flank facing the camera; the charging post stands about 1.2 m from that flank, beside the port, its short cable running from the holster to the port in one gentle arc; in shot 3 @HOMEM_EV stands just right of the post, at the right third, and the camera looks across the car park toward its open side: other bays and cars far back, the ipê trees about 15 m behind along the edge, the city 500 m to 1 km beyond across the whole width of the frame, and behind it the Serra do Curral as a long, even ridge whose crest rises only a little above the tallest towers, the skyline and the ridge in the upper third; the sun low on frame-LEFT.""",
    """PHYSICS & MATERIAL — the connector is heavy, its thick cable stiff and springy, held in one short gentle arc between the post and the port; the port flap springs open; the connector seats only on the second push; ipê blossoms drift in the light wind; the polo moves with his breath. """ + REAL + """ MATERIAL TRUTH: the satin paint of the car, the rubber cable sheath, the slim brushed-steel charging post with a dark blank screen, a thin green status light and a cable holster, white parking lines on clean asphalt, concrete wheel stops, pink ipê petals on the asphalt, the cotton piqué of the red polo, the denim of the jeans, the tan leather and white rubber soles of the sapatênis.""",
    T.LIGHT_EXT,
    T.FILM_LOOK,
    f"""SOUND — LOCATION SOUND ONLY: the city's distant traffic from below the rise; the cable's rubber on the steel; the port flap; the latch click at 2s; a soft single beep from the charging post; his footstep; birds in the ipê trees. {T.MUSIC_POLICY}""",
    T.WORLD_BH,
    f"""NEGATIVE: no charging post, a cable going nowhere, a loose, coiled or trailing cable, a cable lying on the ground, a cable with a free end, a car with no post beside it, an empty or deserted lot, a hilltop viewpoint instead of a car park, a suit, a jacket, a dress shirt, a tie, formal clothes, a logo or text on the polo, the city missing or hidden behind the trees, a blurred or blank background, a lone peak, a pointed or dome-shaped mountain, a mesa, a cliff or sheer rock face, a dramatic granite or alpine mountain, a generic, European or American skyline, a skyline of only new towers, car badge, readable charger screen, posing beside the car, a thumbs-up, speaking in the close-ups, the camera stopping, push-in, extra cuts, {T.NEG_BH}.""",
    """[ORDER: 4 shots, 3 hard cuts at 3s, 5s and 8s, 10s, handheld travelling left to right in every shot — (1, 0–3s) ECU: the connector seats on the second push, its cable leading to the charging post — (2, 3–5s) CU: the port light glows on, his hand lets go, the cable settles in one gentle arc to the steel post — (3, 5–8s) wide shot, his whole body, deep focus: the car plugged into the steel charging totem beside it by a short cable fixed at both ends, in an open-air car park with painted bays; in his red polo, jeans and sapatênis he turns to the lens and says his line, pleased, the ipê trees at mid-distance and the Belo Horizonte skyline behind him (tall modern towers, low restored colonial-style buildings, and behind them the Serra do Curral as a long, even, gently undulating green-and-brown ridge — no peaks, no cliffs, no churches) — (4, 8–10s) CU: he pats the roof twice and steps off. Invariants: constant lateral travel; hands only in the close-ups; living eyes on the lens; only his one line; the same casual clothes, never a suit; a clear charging post, the cable connected at both ends, never loose on the ground; a real car park; the city and the long ridge readable. Look: 35mm color negative, warm halation, lifted blacks, organic grain. Brazilian Portuguese. NO music. NO subtitles, NO text.]""",
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
    dialogue(line(3, 6, "DONO", "de uma economia mais sustentável."), "DONO", pace=None),
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

# ---------------------------------------------------------------- T08 (mina: o funcionário abre a frase, em dois planos)
T08 = join(
    contract(9, "2 shots with 1 hard cut at 4s", "handheld; shot 1 travels sideways while backing up, arcing around him like a slow orbit; shot 2 a close, breathing frame"),
    f"""REFERENCES — each reference has ONE job:
@FUNCIONARIO — IDENTITY of @FUNCIONARIO: face, build, hands, wardrobe and safety equipment. 100% matches.
{SCOPE_ID}""",
    f"""WHO IS WHO — READ FIRST, ABSOLUTE:
@FUNCIONARIO ({ANCH['FUNCIONARIO']}) — the MINE WORKER: in shot 1 he walks FORWARD along the floor of the pit, head and body facing his line of walk, speaking, his eyes finding the lens; in shot 2 he stands at the edge of the pit and speaks to the lens, nothing in his hands; NEVER removes any safety equipment, NEVER walks sideways, NEVER walks away from the camera.
FACES: his face exists once; nobody else in frame; the haul trucks far off have no visible drivers.
CONTACT: nobody touches anyone.""",
    """SCENE — Late afternoon in a modern open-pit niobium mine in Araxá, Minas Gerais, Brazil: orderly terraced benches, big modern haul trucks far off, all in clean low sunlight. Shot 1 is at the bottom of the pit, @FUNCIONARIO already walking forward along its flat floor; shot 2 is at the edge of the pit, the benches and trucks soft far below him.
THE SOUL OF THE SCENE (play it, never explain it): this is his work and he is proud of it; he sets up a punchline — what the whole world looks at, and what Minas looks at instead — with the smile of someone about to hand over the answer.""",
    f"""{LOCKS_HEAD}
1. Exactly 2 shots with 1 hard cut at 4s — WRONG if there are extra cuts.
2. SHOT 1: he walks FORWARD along the floor of the pit, head and body facing his line of walk, only his eyes finding the lens; the handheld camera travels sideways from frame-LEFT to frame-RIGHT while backing up at his pace, ARCING around him like a slow orbit — about 15° off his line of walk on one side at the start to about 15° on the other by the end — WRONG if he walks sideways or away, turns his head to the lens, or the camera stops, reverses, pushes in, pulls back or swings round to his side or back.
3. SHOT 2 is the CLOSE FRAME at the edge of the pit, in the same low sun: his face fully visible, his eyes alive on the lens, his hands out of frame and nothing held — WRONG if he holds or shows any object (no niobium, no stone, no tool), if he looks away, or if the camera travels or zooms.
4. ONE sentence split by the cut: "Enquanto o mundo olha para o nióbiu e as terras raras de Minas" at 0–4s, ending mid-sentence on a continuing tone, and "Minas olha para o que há de mais raro na nossa terra:" at 4–7s, starting the instant the cut lands, the last words OPEN and expectant — the same voice and energy, no gap; "nióbiu" is said nee-OH-byoo, never "niório" — WRONG if he says any other word, pauses at the cut or ends like a verdict.
5. Full mining safety equipment in both shots: hard hat with chin strap fastened, glasses, high-visibility vest, gloves, no logos.
6. Late-afternoon light from frame-LEFT in both shots — NO music.""",
    timeline(2, [4], [
        "SHOT 1 (0–4s) — MWS (from the knees up, the pit around him), 63°, handheld, the camera about 3.5 m from him, travelling sideways from frame-LEFT to frame-RIGHT while backing up at his pace and arcing around him like a slow orbit: @FUNCIONARIO walks forward along the flat floor at the bottom of the pit, centred, his eyes finding the lens; he is already speaking the first part of his sentence in one brisk flow, smiling, and it ends mid-sentence on a continuing tone; the benches rise behind him, dust lifting at his boots. HARD CUT.",
        "SHOT 2 (4–9s) — CU, 29°, handheld, close and breathing, the CLOSE FRAME at the edge of the pit: @FUNCIONARIO faces the lens in the same low sun, head and shoulders, the terraced benches and the haul trucks far below soft behind him, nothing in his hands; his face fully visible, eyes on the lens, already speaking as the cut lands: the second part of the sentence at 4–7s in one brisk flow, the last words open and expectant; at 7–9s he holds the expectant smile, mouth closed. Hard end.",
    ]),
    dialogue(
        line(0, 4, "FUNCIONARIO", "Enquanto o mundo olha para o nióbiu e as terras raras de Minas").replace(
            "(on camera, Brazilian Portuguese)",
            "(on camera, Brazilian Portuguese; the first part of a sentence that continues after the cut — a proud, smiling flow ending on a continuing, lifted tone)"),
        line(4, 7, "FUNCIONARIO", "Minas olha para o que há de mais raro na nossa terra:").replace(
            "(on camera, Brazilian Portuguese)",
            "(on camera, Brazilian Portuguese; the second part, starting the instant the cut lands, same voice and energy — proud and smiling, the last words open and expectant, never a verdict)"),
        "FUNCIONARIO",
        pace="PACING — ONE sentence split by the cut at 4s: each part in ONE brisk flow (about 3 words a second), only a breath between phrases; the second part starts the instant the cut lands, no gap, same voice, pitch and energy; no pause, no held beat."
        ).replace(
        "\nVOICE LOCK",
        "\nPRONUNCIATION — \"nióbiu\" is Brazilian Portuguese for niobium, said nee-OH-byoo: three syllables, stress on the OH, a clear B before the final \"byoo\" — NEVER \"niório\", never \"niobrio\". Say it once, clearly, inside the sentence.\nVOICE LOCK", 1),
    acting("FUNCIONARIO", "he works in the place the whole world is staring at, and he knows what is rarer than any metal.",
           "set up the punchline with a smile — first what the world looks at, then what Minas looks at — and leave the last word hanging.",
           "on the lens in both shots; steady on you through the last words.",
           "his chin lifts a hair as he gets to \"Minas olha\"", "arms spread over the pit, a heroic pose, a solemn or conclusive ending"),
    """CAMERA — handheld in BOTH shots, an operator with a body. SHOT 1: crab-walking sideways at an even slow pace from frame-LEFT to frame-RIGHT while backing up at his walking pace, keeping the distance and ARCING around him like a slow orbit, about 15° each side of his line of walk, with footfall bounce and late small corrections; never stops or reverses; lens at chest height, 3.5 m from him, 63°. SHOT 2: close and breathing, holding its place with a human breath, no lateral travel, 29°, eye height, 1.2 m from his face, the face just left of centre.
FOCUS: his eyes in both shots, the pit soft behind him in shot 2. HORIZON: level.
NOT: tripod, gimbal glide, drone, push-in, pull-back, zoom, the shot-1 camera stopping or reversing, any travel or zoom in shot 2.""",
    T.CLOSE_FRAME,
    """GEOMETRY — shot 1: the pit floor is flat, wide and pale; he walks forward along the centre line; the camera arcs across his path from his front-left to his front-right, 3.5 m away; the benches rise behind him, the trucks small and far; the sun low on frame-LEFT. Shot 2: he stands at the edge of the pit, the camera 1.2 m from his face at eye height, the benches and trucks far below, soft; the sun low on frame-LEFT.""",
    """PHYSICS & MATERIAL — dust lifts at his boots and drifts right (shot 1); the wind moves a little dust off the pit edge (shot 2); the vest is stiff. """ + REAL + """ MATERIAL TRUTH: pale crushed ore with fine dust, the glossy white helmet shell, the black elastic chin strap under his jaw, reflective tape on the vest, clear glasses without glare, grey padded gloves.""",
    T.LIGHT_EXT,
    T.FILM_LOOK,
    f"""SOUND — LOCATION SOUND ONLY: his boots on crushed stone in a steady rhythm (shot 1); wind over the open pit; a haul truck's diesel engine far off; a reversing alarm far away (single repeated tone, not a melody). {T.MUSIC_POLICY}""",
    T.WORLD + " Mining safety equipment is complete and correct; nobody in the pit without it.",
    f"""NEGATIVE: mispronouncing "nióbiu" (as "niório" or any other word), walking sideways or away from the camera, his head turned sideways to the lens, a shot-1 camera that stays on one straight line or swings round to his side or back, any niobium, stone, tool or other object in his hands or in the frame, a pause or gap at the cut, a different voice or mood across the cut, a solemn, conclusive or verdict-like ending, any word beyond his sentence, a heroic pose, arms spread, dirty hands, missing helmet, unfastened chin strap, no glasses, no vest, logos on equipment or trucks, travel or zoom in shot 2, extra cuts, {T.NEG_SPINE}.""",
    """[ORDER: 2 shots, 1 hard cut at 4s, 9s — (1, 0–4s) MWS, handheld, travelling sideways left to right while backing up, arcing around him like a slow orbit: he walks forward along the floor of the pit and says "Enquanto o mundo olha para o nióbiu e as terras raras de Minas", ending mid-sentence on a continuing tone — (2, 4–9s) CU, handheld and breathing, the CLOSE FRAME at the edge of the pit, the same low sun, nothing in his hands, face fully visible; he says "Minas olha para o que há de mais raro na nossa terra:" at 4–7s, the last words open and expectant, then holds the expectant smile. Invariants: one sentence split by the cut, same voice and energy, no gap; shot 1 forward with the slow arc; shot 2 close, no travel, nothing held; full safety equipment; "nióbiu" said nee-OH-byoo; late-afternoon light from frame-LEFT. Look: 35mm color negative, warm halation, lifted blacks, organic grain. Brazilian Portuguese. NO music. NO subtitles, NO text.]""",
)


T08_V2 = join(
    contract(9, "TWO SEPARATE shots joined by ONE hard cut at 4s, never one continuous take", "handheld; shot 1 a wide shot of his whole body, orbiting him on the pit floor; shot 2 a close-up, breathing frame in another place"),
    f"""REFERENCES — each reference has ONE job:
@FUNCIONARIO — IDENTITY of @FUNCIONARIO: face, build, hands, wardrobe and safety equipment. 100% matches.
{SCOPE_ID}""",
    f"""WHO IS WHO — READ FIRST, ABSOLUTE:
@FUNCIONARIO ({ANCH['FUNCIONARIO']}) — the MINE WORKER: in shot 1 he walks FORWARD along the floor of the pit, head and body facing his line of walk, speaking, his eyes finding the lens; in shot 2, in another place at the rim of the pit, his face is close at the left of the frame and he raises a SMALL lump of niobium in his gloved left hand into the empty space on the right, speaking to the lens; NEVER removes any safety equipment, NEVER walks sideways, NEVER walks away from the camera.
FACES: his face exists once; nobody else in frame; the haul trucks far off have no visible drivers.
CONTACT: only his gloved hand on the niobium.""",
    """SCENE — Late afternoon in a modern open-pit niobium mine in Araxá, Minas Gerais, Brazil: orderly terraced benches, big modern haul trucks far off, all in clean low sunlight. TWO DIFFERENT PLACES: shot 1 at the bottom of the pit, @FUNCIONARIO already walking forward along its flat floor, the benches rising behind him like walls; shot 2 at the rim of the pit, high above the floor, a close-up of him on the left of the frame, the open pit and the tiny trucks soft far below on the right.
THE SOUL OF THE SCENE (play it, never explain it): this is his work and he is proud of it; he sets up a punchline — what the whole world looks at, and what Minas looks at instead — with the smile of someone about to hand over the answer.""",
    f"""{LOCKS_HEAD}
1. TWO SEPARATE shots with ONE hard picture cut at 4s, from a wide shot on the pit floor to a close-up at the rim of the pit — a NEW camera in a NEW place — WRONG if it plays as ONE continuous take, if shot 2 is on the pit floor, if anything carries from shot 1 into shot 2 (camera move, zoom, dissolve, morph), or if there are extra cuts.
2. SHOT 1 is a WIDE shot: his WHOLE body, head to boots, in frame from the first frame to the last, the camera about 5 m from him at his chest-to-eye height; he walks FORWARD along the pit floor, only his eyes finding the lens; the handheld camera travels sideways from frame-LEFT to frame-RIGHT while backing up at his pace, ORBITING him about 15° each side, his face always in frame — WRONG if the shot is tight, crops his head or feet, starts on his boots or tilts up from them, he walks sideways or away or turns his head to the lens, or the camera stops, reverses, pushes in or swings to his side or back.
3. SHOT 2 is the CLOSE FRAME at the rim of the pit, in the same low sun: his face on the LEFT third, fully visible, eyes alive on the lens; his gloved hand raises a SMALL lump of niobium — about 8 cm, lime-sized, smaller than his fist and about half as wide as his face — into the empty space on the right, to eye height, as sharp as his face — WRONG if the niobium is bigger than his fist or covers his mouth or eyes, if he looks away, or if the camera travels or zooms.
4. ONE sentence split by the cut — the VOICE flows across it, the PICTURE does not: part 1 (0–4s) ends mid-sentence on a continuing tone, part 2 (4–7s) starts the instant the cut lands, the last words OPEN and expectant — the same voice and energy, no gap; "nióbiu" is said nee-OH-byoo — WRONG if he says any other word, pauses at the cut or ends like a verdict.
5. Full mining safety equipment in both shots: hard hat with chin strap fastened, glasses, high-visibility vest, gloves, no logos. Late-afternoon light from frame-LEFT in both shots — NO music.""",
    timeline(2, [4], [
        "SHOT 1 (0–4s) — WS, his whole body head to boots, 63°, handheld, at his chest-to-eye height about 5 m from him, travelling sideways from frame-LEFT to frame-RIGHT while backing up at his pace and orbiting him: @FUNCIONARIO walks forward along the flat pit floor, centred, his whole body in frame the whole time, his eyes finding the lens; already speaking the first part of his sentence in one brisk flow, smiling, ending mid-sentence on a continuing tone; the benches rise behind him, dust lifting at his boots. HARD CUT at 4.0s to a NEW camera in ANOTHER place.",
        "SHOT 2 (4–9s) — NEW SETUP at the RIM of the pit, high above the floor: CU, 29°, handheld, close and breathing, holding its place, the CLOSE FRAME. @FUNCIONARIO at the left of the frame, his face on the left third, facing the lens in the same low sun, the pit far below, soft; already speaking as the cut lands, within the first second he raises a SMALL lump of raw niobium — rough, faceted, silvery-grey, lime-sized — in his gloved left hand, up from below the frame into the empty space on the right to eye height, and holds it there, steady, as sharp as his face; the second part of the sentence at 4–7s in one brisk flow, the last words open and expectant; at 7–9s he holds the expectant smile, the niobium still raised, mouth closed. Hard end.",
    ]).replace("TIMELINE — 2 shots, 1 hard cuts; cuts only", "TIMELINE — 2 SEPARATE shots, 1 hard cut at 4s, never one continuous take; cuts only"),
    dialogue(
        line(0, 4, "FUNCIONARIO", "Enquanto o mundo olha para o nióbiu e as terras raras de Minas").replace(
            "(on camera, Brazilian Portuguese)",
            "(on camera, Brazilian Portuguese; the first part of a sentence that continues after the cut — a proud, smiling flow ending on a continuing, lifted tone)"),
        line(4, 7, "FUNCIONARIO", "Minas olha para o que há de mais raro na nossa terra:").replace(
            "(on camera, Brazilian Portuguese)",
            "(on camera, Brazilian Portuguese; the second part, starting the instant the cut lands, same voice and energy — proud and smiling, the last words open and expectant, never a verdict)"),
        "FUNCIONARIO",
        pace="PACING — ONE sentence split by the cut at 4s: each part in ONE brisk flow (about 3 words a second), only a breath between phrases; the second part starts the instant the cut lands, no gap, same voice, pitch and energy; no pause, no held beat."
        ).replace(
        "\nVOICE LOCK",
        "\nPRONUNCIATION — \"nióbiu\" is Brazilian Portuguese for niobium, said nee-OH-byoo: three syllables, stress on the OH, a clear B before the final \"byoo\" — NEVER \"niório\", never \"niobrio\". Say it once, clearly, inside the sentence.\nVOICE LOCK", 1),
    acting("FUNCIONARIO", "he works in the place the whole world is staring at, and he knows what is rarer than any metal.",
           "set up the punchline with a smile — first what the world looks at (the metal he lifts), then what Minas looks at — and leave the last word hanging.",
           "on the lens in both shots, with one quick glance at the niobium at most as he lifts it; steady on you through the last words.",
           "his chin lifts a hair as the niobium rises", "arms spread over the pit, a heroic pose, a solemn or conclusive ending"),
    """CAMERA — handheld in BOTH shots, an operator with a body, but TWO separate setups. SHOT 1: crab-walking sideways at an even slow pace from frame-LEFT to frame-RIGHT while backing up at his walking pace, ORBITING him about 15° each side of his line of walk, with footfall bounce and late small corrections; never stops or reverses; lens at his chest-to-eye height, about 5 m from him, 63°, his whole body in frame. SHOT 2: a new setup, close and breathing, holding its place, no lateral travel, 29°, eye height, 1.2 m from his face, his face on the left third. FOCUS: shot 1 deep, him and the pit readable; shot 2 his eyes, the niobium as sharp as his face. HORIZON: level.
NOT: tripod, gimbal glide, drone, push-in, pull-back, zoom, one continuous take, a tight or chest-up shot 1, a wide shot 2, any travel or zoom in shot 2.""",
    T.CLOSE_FRAME_LEFT,
    """GEOMETRY — shot 1: the camera 5 m from him at chest-to-eye height, orbiting from his front-left to his front-right while he walks the flat pit floor; the benches rise behind him; the sun low on frame-LEFT. Shot 2, another place: he stands at the rim of the pit, the camera 1.2 m from his face, his face on the left third (eyes at about 28% of the frame width), the lime-sized niobium (about a tenth of the frame width) at about 70% of the width at eye height, the pit far below, soft; the sun low on frame-LEFT.""",
    """PHYSICS & MATERIAL — dust lifts at his boots (shot 1); the niobium is a small, dense lump, sharp-edged: his padded glove closes round it and it turns a few degrees, its facets glinting; the vest is stiff. """ + REAL + """ MATERIAL TRUTH: rough crystalline silvery-grey facets with a dull-bright metallic sheen and fine dust in the crevices (not a smooth ingot, not a mirror, not a boulder), glossy white helmet shell, black chin strap, reflective tape, clear glasses without glare, grey padded gloves.""",
    T.LIGHT_EXT,
    T.FILM_LOOK,
    f"""SOUND — LOCATION SOUND ONLY: his boots on crushed stone in a steady rhythm (shot 1); wind over the open pit; a haul truck's diesel engine far off; a reversing alarm far away (single repeated tone, not a melody); the glove's fabric against the metal (shot 2). {T.MUSIC_POLICY}""",
    T.WORLD + " Mining safety equipment is complete and correct; nobody in the pit without it.",
    f"""NEGATIVE: one continuous take, a camera move, zoom, dissolve or morph from shot 1 into shot 2, shot 2 on the pit floor, a tight or chest-up shot 1, a wide or full-body shot 2, a frame that starts at his feet or tilts up from his boots, walking sideways or away, an oversized niobium, a boulder, a niobium bigger than his fist, the niobium over his mouth or eyes, a smooth polished ingot, a mirror ball, glowing metal, gold, any niobium in shot 1, mispronouncing "nióbiu" (as "niório"), a pause or gap at the cut, a different voice or mood across the cut, a solemn or verdict-like ending, any word beyond his sentence, a heroic pose, missing helmet, unfastened chin strap, no glasses, no vest, travel or zoom in shot 2, extra cuts, {T.NEG_SPINE}.""",
    """[ORDER: TWO SEPARATE shots, 1 hard cut at 4s, 9s, never one continuous take — (1, 0–4s) on the pit floor: WS, his whole body head to boots in frame, camera about 5 m away at chest-to-eye height, handheld, travelling sideways left to right while backing up, orbiting him: he walks forward and says "Enquanto o mundo olha para o nióbiu e as terras raras de Minas", ending mid-sentence — HARD CUT to a new camera in another place — (2, 4–9s) at the rim of the pit, high above the floor: CU, handheld and breathing, same low sun, his face on the left third, his gloved hand raising a SMALL lime-sized lump of niobium (smaller than his fist) into the empty space on the right to eye height; he says "Minas olha para o que há de mais raro na nossa terra:" at 4–7s, the last words open and expectant, then holds the smile. Invariants: the cut is a picture cut from wide to close; one sentence, same voice and energy, no gap; shot 1 wide, whole body in frame, orbiting; shot 2 close, no travel, niobium small and never over mouth or eyes; full safety equipment; late-afternoon light from frame-LEFT. Look: 35mm color negative, warm halation, lifted blacks, organic grain. Brazilian Portuguese. NO music. NO subtitles, NO text.]""",
)


# ---------------------------------------------------------------- T08-C (plano 2 novo: a lojista diz a segunda metade da frase, na lojinha de artesanato; foto @image 1 do usuário)
T08C = join(
    contract(5, "ONE continuous take, no cuts", "handheld, a wide shot travelling slowly sideways from frame-left to frame-right"),
    f"""REFERENCES — each reference has ONE job:
@LOJISTA — IDENTITY of @LOJISTA: face, hair, glasses, build, hands and wardrobe. 100% matches.
@image 1 — PLACE: the building — a two-storey colonial-style corner building, white walls with deep-blue trim, an arcade of arched blue-framed openings under a dark wrought-iron balcony, a deep-blue pilaster at the corner, a white wall with a horizontal blue band and a large blue arched door at street level, a dark eave and a red clay-tile roof. 100% matches the building. The shop interior is not in the photo: it is described below.
REFERENCE SCOPE: the character reference supplies face, hair, build, hands and wardrobe ONLY — IGNORE its grey backdrop, studio lighting, exposure and colour grade. For @image 1: IGNORE the man walking, the parked car, the palm tree, the lamp posts and signs, the street, the sky, the harsh midday light and the vertical framing.""",
    f"""WHO IS WHO — READ FIRST, ABSOLUTE:
@LOJISTA ({ANCH['LOJISTA']}) — the SHOP OWNER: stands on the pavement in front of her own craft shop, facing the lens, and speaks once; NEVER walks away, NEVER goes into the shop, NEVER holds an object up to the camera.
THE SHOP — the ground floor of the building in @image 1 is her craft shop: its large blue arched door beside her stands OPEN and the interior shows through it — wooden shelves of ceramics, woven baskets, handwoven textiles and small carved wooden figures, a wooden counter, a few warm lamps, nobody inside; against the wall by the door, a low wooden stand with clay pots and two baskets; no sign with letters anywhere.
FACES: her face exists once; nobody else in frame.
CONTACT: only her hand resting on the stand.""",
    """SCENE — Late afternoon on a quiet street in a Minas Gerais town: the restored colonial-style building of @image 1 — white walls, deep-blue trim, arched blue-framed openings, a dark wrought-iron balcony upstairs, a red clay-tile roof — is a craft shop on its ground floor. @LOJISTA stands on the pavement in front of the open door, already looking at you, one hand on the display stand.
THE SOUL OF THE SCENE (play it, never explain it): a man at a mine just started a sentence and she picks it up — she lives from what Minas hands make and knows what is rarest here; she carries it on with a warm smile and leaves the last word hanging.""",
    f"""{LOCKS_HEAD}
1. ONE continuous handheld WIDE take, no cuts — WRONG if it cuts, if the shot is tight or a close-up, or if the lens zooms or the camera pushes in.
2. The handheld camera travels slowly sideways from frame-LEFT to frame-RIGHT the whole time (about one metre in total), never stopping or reversing, while @LOJISTA stays where she stands, her whole body in frame — WRONG if the camera stops, reverses, glides or orbits, or if she walks away or into the shop.
3. The building is the one in @image 1 and it is a SHOP: its large blue arched door beside her is OPEN and the craft shop's interior is visible through it, the blue-trimmed white walls, the arched openings and, along the top of the frame, the iron balcony and the red-tile eave filling the background — WRONG if the door is closed, the interior is not visible, the building is different, or there is any readable sign, text or logo.
4. Only @LOJISTA speaks, only "Minas olha para o que há de mais raro na nossa terra:" — every other mouth closed; nobody else in frame — WRONG if she says any other word or ends like a verdict.
5. Her eyes are alive on the lens and readable behind her glasses — WRONG if the glasses glare or hide them, or if she turns her head sideways to the lens.
6. Late-afternoon light from frame-LEFT — NO music, NO radio.""",
    timeline(1, [], [
        "BEAT 1 (0–5s) — WS, 70°, handheld, about 6 m from her at chest-to-eye height, the camera pitched up a few degrees, travelling slowly sideways from frame-LEFT to frame-RIGHT: @LOJISTA stands on the pavement about 1.5 m in front of the shop, at the right third, her whole body in frame, one hand resting on the edge of the low display stand, already looking into the lens; the large blue arched door beside her stands open and the warm craft shop interior shows through it; behind her the white wall with its deep-blue trim, the corner pilaster, the arched openings and, along the top of the frame, a corner of the iron balcony and the red-tile eave; she speaks at 0–3s, the first word within the first third of a second, bright and warm, the last words open and expectant; as the camera passes she drifts toward the centre of the frame and the interior slides behind her; at 3–5s she holds the expectant smile, mouth closed. Hard end.",
    ]),
    dialogue(
        line(0, 3, "LOJISTA", "Minas olha para o que há de mais raro na nossa terra:").replace(
            "(on camera, Brazilian Portuguese)",
            "(on camera, Brazilian Portuguese; the second half of a sentence a man began a moment ago — she picks it up at once, warm, proud and smiling, the last words open, lifted and expectant, never a verdict)"),
        "LOJISTA"),
    acting("LOJISTA", "she lives from what Minas hands make, and she knows what is rarest here — she is about to hand you the answer.",
           "pick up the sentence a man just began and carry it on with a smile — first what Minas looks at, then leave the last word hanging, like passing you the ball.",
           "on the lens, bright and warm, clear behind her glasses.",
           "her fingertips tap once on the edge of the stand",
           "a salesperson's pitch, pointing at her wares, holding an object up to the camera, a heroic pose, a solemn or conclusive ending"),
    """CAMERA — handheld, an operator with a body: crab-walking sideways at a slow, even pace from frame-LEFT to frame-RIGHT (about one metre over the whole shot) with footfall bounce and late small corrections; never stops, never reverses, never pushes in. Lens 70°, about 6 m from her at chest-to-eye height, pitched up a few degrees so the top of the frame catches the iron balcony and the red-tile eave. DEEP focus: the facade, the open door and the shop's interior stay readable, NO creamy bokeh. HORIZON: level.
NOT: tripod, locked-off frame, gimbal glide, dolly-smooth slide, drone, orbit, push-in, zoom, a close-up, the camera stopping or reversing.""",
    """GEOMETRY — the camera looks at the building's corner from across the street: on one side the arcade of arched blue-framed openings with the iron balcony above, on the other the white wall with its blue band and the large blue arched door, standing open, the shop interior inside it; @LOJISTA stands on the pavement about 1.5 m in front of that wall, at the right third at the start, drifting toward the centre as the camera passes, the low display stand against the wall to her left, by the door; the sun low on frame-LEFT, raking along the white walls.""",
    """PHYSICS & MATERIAL — the clay pots and baskets are light and handmade; the lime-washed walls show a faint texture; the blue paint is satin on old timber; her shirt moves with her breath; a faint breeze stirs a hanging textile inside. """ + REAL + """ MATERIAL TRUTH: white lime-washed plaster, deep-blue painted frames and door, red clay roof tiles, a dark wrought-iron balcony, honey-coloured wooden shelves, terracotta and glazed ceramics, woven straw baskets, handwoven cotton textiles, the cotton of her teal shirt, her slim glasses with clear lenses.""",
    T.LIGHT_EXT + "\nSHOP INTERIOR: a few warm lamps glow softly through the open door, small and secondary, never lighting her face.",
    T.FILM_LOOK,
    f"""SOUND — LOCATION SOUND ONLY: the quiet street of a small Minas town — a far-off motorbike, a bird, a faint wind; the soft clack of a clay pot on the stand; her voice. NO radio, NO music from the shop. {T.MUSIC_POLICY}""",
    T.WORLD_HIST,
    f"""NEGATIVE: a closed shop door, no interior visible, an empty or dark interior, a different building, a church, a bell tower, a steeple, a readable sign or shop name, text or logos on any surface, customers or any other person in frame, a man walking in the street, a parked car, harsh midday light, a blown-out sky, her walking away or into the shop, her head turned sideways to the lens, holding an object up to the camera, a salesperson's pitch, glare on her glasses hiding her eyes, a close-up, a push-in, a zoom, a cut, a solemn or verdict-like ending, any word beyond her sentence, decayed walls, {T.NEG_BH}.""",
    """[ORDER: ONE take, 5s, handheld WIDE shot travelling slowly left to right, never stopping — @LOJISTA stands on the pavement in front of her craft shop, at the right third, whole body in frame, one hand on the low display stand, looking into the lens; the large blue arched door beside her is open and the warm shop interior (ceramics, baskets, textiles) shows through it; behind her the white wall with deep-blue trim, the arched openings and, at the top edge, the iron balcony and the red-tile eave of the building in @image 1; she says "Minas olha para o que há de mais raro na nossa terra:" at 0–3s, bright and warm, the first word at once, the last words open and expectant, then holds the smile until 5s. Invariants: one wide take, no cuts, no close-up; the building of @image 1 as a shop, the door open, the interior visible; no readable sign or text; no church; nobody else in frame; her eyes readable behind the glasses; late-afternoon light from frame-LEFT. Look: 35mm color negative, warm halation, lifted blacks, organic grain. Brazilian Portuguese. NO music. NO subtitles, NO text.]""",
)

# ---------------------------------------------------------------- T09 (plantação, um take só: andando + drone + match com dolly-out)
T09 = join(
    contract(10, "3 shots with 2 hard cuts at 2s and 4s", "handheld orbit in shot 1, a high drone orbit in shot 2, a slow dolly-out in shot 3"),
    f"""REFERENCES — each reference has ONE job:
@AGRICULTORA — IDENTITY of @AGRICULTORA: face, hair, build, hands and wardrobe. 100% matches.
{SCOPE_ID}""",
    f"""WHO IS WHO — READ FIRST, ABSOLUTE:
@AGRICULTORA ({ANCH['AGRICULTORA']}) — the FARMER: walks through her soybean field with no destination, her hand brushing the tops of the plants; in shot 1 she walks FORWARD toward the camera; in shot 2 she is small, seen from far above, walking on; in shot 3 she faces the lens; she speaks in all three; NEVER walks sideways, NEVER stops walking in shots 1 and 2.
FACES: her face exists once; nobody else; no machine or vehicle anywhere in frame.""",
    """SCENE — Bright mid-morning on a large, modern soybean farm in the Triângulo Mineiro, Minas Gerais, Brazil: vivid green rows to the horizon, a blue sky with a few white clouds, a centre-pivot irrigation arm far off. @AGRICULTORA is already walking forward along a row, smiling, her open hand passing over the tops of the plants.
THE SOUL OF THE SCENE (play it, never explain it): someone just left a sentence hanging — "the rarest thing in our land:" — and she is the answer; she walks her field with nowhere else to be, delighted, telling you what it is all for like happy news she can't wait to share.""",
    f"""{LOCKS_HEAD}
1. Exactly 3 shots, 2 hard cuts, at 2s and at 4s — WRONG if there are extra cuts.
2. SHOT 1: she walks FORWARD, head and body facing her line of walk, only her eyes finding the lens; the handheld camera, at her EYE HEIGHT or a hair above (never below her eyes), travels sideways from frame-LEFT to frame-RIGHT while backing up at her pace, arcing about 15° each side — WRONG if she walks sideways or away or turns her head to the lens, or the camera is low, stops, reverses or swings to her side or back.
3. SHOT 2: an AERIAL WIDE from a smooth drone-mounted camera about 36 m above the field and 35 m from her on a DIAGONAL (about 45° off her line of walk), ORBITING her slowly and steadily, she small and centred, walking — WRONG if the drone is low (under 30 m), straight behind her, static, shaky, or her face is large.
4. NO drone sound (no rotor or propeller buzz, no motor whine, no helicopter thrum) in any shot; the aerial shot sounds like the open field.
5. SHOT 3 is the MATCH FRAME, a hair closer than the series: face dead centre, straight into the lens, the camera at her eye height or a hair above (never below), the rows and horizon behind her READABLE and only gently soft; the camera moves slowly BACK (a dolly-out, no zoom) — WRONG if the camera is low, the background melts into a blur, the lens zooms or the face drifts off centre.
6. Three lines only, ONE continuing speech in one bright, buoyant, proud voice with a Minas Gerais accent ("gente" said GEN-tchi), each starting the instant its shot begins, only a breath at each cut and two very short breaths in the last line, after "nasce," and after "vive," — WRONG if she says anything else, pauses elsewhere, or sounds calm, soft or slow.
7. Her eyes are alive and readable under the hat brim in shots 1 and 3. Bright mid-morning light, the sun high, NOT golden hour, NO flares — NO music.""",
    timeline(3, [2, 4], [
        "SHOT 1 (0–2s) — MWS (from the knees up, the rows readable behind her), 63°, handheld, the camera at her eye height (a hair above, never below her eyes), about 3.5 m from her, already arcing from frame-LEFT to frame-RIGHT around her while backing up at her pace: @AGRICULTORA is already walking forward, centred, smiling, her open hand sweeping over the tops of the plants; her eyes find the lens and she says her first line at once, the first word within the first third of a second, then keeps walking and smiling until the cut. HARD CUT.",
        "SHOT 2 (2–4s) — AERIAL WIDE (WS), 70°, a smooth, stable DRONE-mounted camera about 36 m above the field and 35 m from her on a diagonal, tilted about 45° down, orbiting her slowly and steadily (about 25° of arc over the shot) and keeping her small and centred: @AGRICULTORA walks on along her row, saying her next line as she goes, her voice close and clear; the rows sweep across the frame in long diagonals. HARD CUT.",
        "SHOT 3 (4–10s) — the MATCH FRAME, a hair closer, MCU, 47° fixed, the camera at her eye height or a hair above: @AGRICULTORA dead centre, already facing the lens at the cut, the rows and horizon readable behind her; she speaks at 4–8s, bright and proud, a smile in her voice, one brisk flow with a very short breath only after 'nasce,' and after 'vive,', while the slow dolly-out runs the whole shot and the frame opens toward a medium shot; at 8–10s she holds the smile. Hard end.",
    ]),
    dialogue(
        line(0, 2, "AGRICULTORA", "a nossa gente.").replace(
            "(on camera, Brazilian Portuguese)",
            "(on camera, Brazilian Portuguese with a Minas Gerais accent, \"gente\" said GEN-tchi; bright, buoyant and proud, a smile in the voice, never calm, soft or solemn)"),
        line(2, 4, "AGRICULTORA", "Afinal, o que cresce aqui:").replace(
            "(on camera, Brazilian Portuguese)",
            "(on camera but seen from far above, walking, Brazilian Portuguese; her voice close, clear and dry, not distant; the same bright, buoyant delivery)"),
        line(4, 8, "AGRICULTORA", "também deve construir novos caminhos para quem nasce, vive e trabalha aqui.").replace(
            "(on camera, Brazilian Portuguese)",
            "(on camera, Brazilian Portuguese; the same bright, buoyant, proud delivery, each phrase lifting a little — never calm, soft, measured or solemn)"),
        "AGRICULTORA",
        pace="PACING — the three lines are ONE continuing speech by the same woman, in ONE brisk, bright flow (about 3 words a second or faster): the same voice, accent and energy in all three shots, only a breath at each cut, no pause, no held beat; in the last line two very short beats of silence (a quarter of a second each) after \"nasce,\" and after \"vive,\" and no other pause."),
    acting("AGRICULTORA", "someone just opened a sentence and she has the answer — the thing she is proudest of, and the land she walks every day.",
           "give the answer like the happy punchline of a story, then tell what it is all for — brisk, bright and buoyant, a smile in the voice from the first word, each phrase lifting a little.",
           "on the lens in shots 1 and 3, bright and warm, readable under the hat brim.",
           "she breathes a short laugh through her nose",
           "arms spread over the field, turning her head sideways to look at the camera, a calm, soft, measured or solemn delivery, a heroic pose"),
    """CAMERA — SHOT 1: handheld, an operator with a body: crab-walking sideways at an even slow pace from frame-LEFT to frame-RIGHT while backing up at her walking pace, arcing about 15° each side of her line of walk, with footfall bounce and late small corrections; never stops or reverses; the lens at her EYE HEIGHT or a hair above, 3.5 m away, 63°. Deep focus: the rows, the pivot and the horizon stay readable, NO creamy bokeh.
SHOT 2: a smooth, stable drone-mounted camera, 70°, deep focus; the drone, its shadow and its sound never exist. SHOT 3: the dolly-out below.
NOT: a low camera in shots 1 and 3, a low, fast or static drone, a zoom.""",
    T.dolly_out(6, start=1.2).replace("CAMERA — the DOLLY-OUT", "CAMERA — SHOT 3, the DOLLY-OUT").replace("FOCUS: on the eyes throughout.", "FOCUS: on the eyes throughout, with a deep depth of field — the rows and the horizon behind her stay readable, NO creamy bokeh.").replace("NOT: a zoom, a vertigo or dolly-zoom effect, a push-in, a locked frame, a handheld shake, an orbit, a gimbal glide, a drone.", "NOT (shot 3): a zoom, a vertigo or dolly-zoom effect, a push-in, a locked frame, a handheld shake."),
    T.MATCH_FRAME.replace("KEY — identical in every shot of the match series", "KEY — a hair closer than the rest of the series").replace("about 1.3 m", "about 1.2 m").replace("the background soft", "the background readable and only gently soft"),
    """GEOMETRY — shot 1: the camera 3.5 m from her at her eye height, arcing from her front-left to her front-right; the pivot about 300 m away, small. Shot 2: the drone 36 m up and 35 m from her on a diagonal, looking down 45°. Shot 3: the camera starts 1.2 m from her face at eye height or a hair above, the field behind her. The sun high on frame-LEFT in shots 1 and 3.""",
    """PHYSICS & MATERIAL — the plants are springy: her hand bends the tops and they whip back; her boots press into the soft soil; her braid swings with each step; from the air the leaves ripple in the wind. """ + REAL + """ MATERIAL TRUTH: glossy healthy leaves, dark moist soil, the light cotton of her sage-green shirt, the felt of her hat brim.""",
    T.LIGHT_EXT_DAY.replace("CONTINUITY: the sun stays frame-LEFT in every shot; lit sides never flip.", "CONTINUITY: in shots 1 and 3 the sun stays frame-LEFT and the lit side never flips; in the aerial shot 2 the orbit may change the angle, the same high bright sun, no flare."),
    T.FILM_LOOK,
    f"""SOUND — LOCATION SOUND ONLY under her voice: leaves brushing her hand and trousers (shot 1); wind over the field and the soft rustle of the soybean leaves; a quero-quero bird far off; the faint hiss of the irrigation pivot. NO DRONE SOUND in the aerial shot — no rotor or propeller buzz, no motor whine, no helicopter thrum: it sounds exactly like the open field. {T.MUSIC_POLICY.replace('NO drone, ', 'NO sustained tone, ')}""",
    T.WORLD,
    f"""NEGATIVE: drone noise, rotor or propeller buzz, motor whine, helicopter thrum, a low, fast, static or shaky drone, a drone straight behind her, a low camera in shots 1 and 3, a blurred background, creamy bokeh, her face large in shot 2, any machine or vehicle in frame, a flare, golden hour, a low orange sun, a zoom or push-in, the face off centre, her looking away in shot 3, eyes hidden in the hat shadow, walking sideways or away in shot 1, a calm, soft, slow or measured delivery, a Northeastern accent, any word beyond her three lines, a pause between the lines, extra cuts, {T.NEG_DOLLY.replace("gimbal glide, ", "")}.""",
    """[ORDER: 3 shots, 2 hard cuts at 2s and 4s, 10s — (1, 0–2s) MWS, handheld, camera at her eye height, arcing around her as she walks forward through her soybean field, smiling, hand brushing the plants: "a nossa gente." at once — (2, 2–4s) AERIAL WIDE, a smooth drone 36 m up and 35 m away on a diagonal, orbiting her slowly, she small and centred, walking: "Afinal, o que cresce aqui:" — (3, 4–10s) MATCH FRAME, a hair closer, camera at her eye height or a hair above, face dead centre, rows and horizon readable, slow dolly-out (no zoom): "também deve construir novos caminhos para quem nasce, vive e trabalha aqui." at 4–8s, then the smile held. Invariants: ONE continuing speech in the same voice, Minas Gerais accent ("gente" GEN-tchi) and bright, buoyant energy; NO drone sound; no machine; the camera never low in shots 1 and 3; the background readable; bright mid-morning light, no flares. Look: 35mm color negative, warm halation, lifted blacks, organic grain. Brazilian Portuguese. NO music. NO subtitles, NO text.]""",
)

# ---------------------------------------------------------------- T10 / T11 (match, sem fala)
def match_locks(subject, mouth_note, eyes="straight into the lens, the eyes alive"):
    return f"""{LOCKS_HEAD}
1. ONE take in the MATCH FRAME with the slow dolly-out (the camera moving back, no zoom), no cuts — WRONG if it cuts, if the camera is locked, or if the lens zooms or the camera pushes in.
2. {subject}'s face stays dead centre and frontal, {eyes}, while the framing opens from a medium close-up toward a medium shot — WRONG if the face drifts off centre or turns away, or the eyes go glassy.
3. NO dialogue: {mouth_note} — WRONG if any mouth forms words.
4. Light from frame-LEFT — NO music."""


def add_lock(locks, text):
    """Insert one extra lock before the closing light lock of a match-series take."""
    tail = "4. Light from frame-LEFT — NO music."
    assert tail in locks
    return locks.replace(tail, text + "\n5. Light from frame-LEFT — NO music.")


T10 = join(
    contract(4, "ONE continuous take, no cuts", "a slow dolly-out from a medium close-up", dialogue=False),
    f"""REFERENCES — each reference has ONE job:
@MAE — IDENTITY of @MAE: face, hair, build, hands and wardrobe. 100% matches. Her SKIN in the footage is real skin (see PHYSICS & MATERIAL): any retouched, smoothed or glowing finish in the reference does NOT carry over.
{SCOPE_ID.replace("exposure and colour grade.", "exposure, colour grade and skin finish.")}""",
    f"""WHO IS WHO — READ FIRST, ABSOLUTE:
@MAE ({ANCH['MAE']}) — the MOTHER: holds her newborn in her arms and looks into the lens, the smile breaking through her closed lips; NEVER speaks.
NEWBORN — a real newborn of a few days, small and correctly proportioned, wrapped in a pale cotton blanket and held in her arms at the bottom edge of the frame, most of the face covered by the blanket; only a flushed, slightly blotchy forehead with fine downy hair, a closed swollen eyelid and a cheek show.
FACES: each face exists once; nobody else in the room.
CONTACT: only her hands on the baby.""",
    """SCENE — A bedroom in a modern apartment in Belo Horizonte, Brazil, afternoon, lived-in like a real home with a newborn: the window on frame-LEFT, the slept-in bed behind her on frame-RIGHT with the duvet pushed back, a nursing pillow and a creased muslin cloth on it, a glass of water on the bedside table; @MAE stands by the window holding her newborn in her arms, looking at you.
THE SOUL OF THE SCENE (play it, never explain it): someone new just arrived — she looks at you with the happiness of a mother who has hardly slept, as if you had come in to meet him; a caught moment, never a posed portrait.""",
    add_lock(match_locks("@MAE", "her mouth stays closed in a smile, the baby makes only small breathing sounds"),
             "4. REAL: her skin is real skin (visible pores, freckles, fine downy hairs, a natural shine), her smile a little uneven, the room lived-in — WRONG if her skin looks smooth, glowing or retouched, her smile is a frozen symmetrical grin, or the room looks like a showroom."),
    timeline(1, [], [
        "BEAT 1 (0–4s) — the MATCH FRAME, MCU: @MAE's face dead centre, eyes on the lens, the smile already in progress at the first frame — a little uneven, breaking through her closed lips and widening slightly as the take runs — the swaddled newborn held in her arms at the bottom edge of the frame, his chest rising and falling under her hand; she shifts her weight once and the blanket moves with her; one slow blink and one small quick one; the slow dolly-out runs the whole take, the lived-in bedroom opening wider behind her. Hard end mid-breath, the smile still alive.",
    ]),
    acting("MAE", "everything is new and she is happy — she has hardly stopped looking at him since he arrived.",
           "introduce him to you without a word and without waking him — she is bursting with it and holding it in, so the smile leaks through her lips; her eyes check that you see how perfect he is.",
           "on the lens throughout, reading you.",
           "a short breath of a laugh through her nose",
           "speaking, crying, rocking theatrically, presenting the baby to the camera, a frozen or perfectly symmetrical smile, a posed stock-photo mother"),
    T.dolly_out(4),
    T.MATCH_FRAME,
    """PHYSICS & MATERIAL — the baby is light, warm and limp, sinking into the crook of her arm; the blanket's cotton folds and shifts with her breathing; a tiny movement of the baby's chest under her hand; her weight settles from one foot to the other. Nothing floats, nothing loops. If any surface looks clean, smooth, plastic, CGI or rendered — WRONG.
OVER-REAL — HER SKIN: visible pores on the nose and cheeks, freckles of different sizes, fine downy hair along her temples and jaw catching the window light, a faint natural shine on the forehead and nose bridge, slightly dry lips with a small crease, a faint tired shadow under the eyes, no visible makeup, a smile a little asymmetric, a few flyaway hairs and a loose strand across her cheek. THE BABY: flushed, slightly blotchy newborn skin, fine downy hair, a swollen translucent eyelid. THE ROOM: the fine rib of her ivory knit, the creased muslin, the plain white curtain's uneven folds, the slept-in duvet, a few small scuffs on the painted wall.""",
    T.light_int("the bedroom window with a plain, slightly creased white curtain",
                "no other source.",
                "the daylight lights the frame-LEFT side of her face with a visible gradient across the cheek, a small soft window-shaped reflection in each eye and the soft shadow of her nose on the frame-RIGHT cheek; the frame-RIGHT side of her face and the room behind fall into soft shade, the wall brighter near the window and darker away from it; the daylight reads cool-neutral on her skin and the shade side takes a warm bounce from the walls, both muted.")
     .replace("highlights creamy and warm", "skin highlights keep their texture, never a glow")
     .replace("beauty light,", "beauty light, a glow on the skin,"),
    T.FILM_LOOK.replace("gentle warm halation blooming around windows, sunlit patches and bright skin edges; highlights creamy and warm, never pure white",
                        "a faint warm halation around the window only, none on the skin; skin highlights keep their texture, never creamy or glowing, never pure white"),
    f"""SOUND — LOCATION SOUND ONLY: quiet room tone; the baby's small breathing and one tiny sigh; her own quiet breath through her nose; the knit's soft rustle; the city far below the window. {T.MUSIC_POLICY}""",
    T.WORLD,
    f"""NEGATIVE: the mother speaking, any mouth forming words, a doll-like baby, wrong newborn proportions, the baby's full face, presenting the baby to the camera, crying, a cut, the face drifting off centre, a zoom, a generic or plain-looking woman, a frozen or perfectly symmetrical smile, a posed stock-photo portrait, smooth or airbrushed skin, a glowing or luminous skin finish, visible makeup, glamour or beauty lighting, salon-styled hair, perfect teeth, glowing eyes, a showroom-clean bedroom, a staged catalogue nursery, {T.NEG_DOLLY}.""",
    """[ORDER: ONE take, 4s, MATCH FRAME medium close-up with a slow dolly-out — @MAE's face dead centre, eyes on the lens, a smile already in progress and a little uneven, breaking through her closed lips, the swaddled newborn held in her arms at the bottom edge, the lived-in bedroom opening wider behind her as the camera backs away; hard end mid-breath. Invariants: face centred throughout, the camera backing away with no zoom; no dialogue; baby partly covered, correct proportions; REAL skin with pores, freckles, fine hairs and a natural shine, never smooth, glowing or retouched; a lived-in room, not a showroom. Look: 35mm color negative, halation at the window only, lifted blacks, organic grain. NO music. NO subtitles, NO text.]""",
)

T11 = join(
    contract(4, "ONE continuous take, no cuts", "a slow dolly-out from a medium close-up", dialogue=False),
    f"""REFERENCES — each reference has ONE job:
@TORCEDORA — IDENTITY of @TORCEDORA: face, hair, build, hands and wardrobe, EXCEPT the small emblem on the jersey chest, which must NOT appear: the chest of her jersey is plain. 100% matches otherwise.
{SCOPE_ID}""",
    f"""WHO IS WHO — READ FIRST, ABSOLUTE:
@TORCEDORA ({ANCH['TORCEDORA']}) — the FAN: sits in a grandstand watching the match with bright, excited attention, her eyes on the pitch just beside the lens; NEVER speaks, NEVER shouts, NEVER looks straight into the lens.
CROWD — the stand around her is full and every fan is a DIFFERENT person — a different age, sex, skin tone, hair and build; none has her face and none repeats another — all watching the match and excited too, none looking at the lens, all in plain generic football shirts (see SHIRTS). Seat by seat:
NEIGHBOUR on frame-LEFT, shoulder to shoulder with her: a Brazilian man of about 50, light-brown (pardo) skin, heavy-set, short black hair flecked with grey and a thick moustache, a hand on his forehead and his mouth open in a long "oh".
NEIGHBOUR on frame-RIGHT, shoulder to shoulder with her: a white Brazilian woman of about 62, fair freckled skin, short silver curls and thin-framed glasses, her hands pressed together at her chin, beaming.
BEHIND THEM, partly visible and a little softer: a young Black man of about 20 with a shaved head, standing, his hands on top of his head; a white man of about 38 with a short brown beard, leaning forward on his elbows; a girl of about 15 with light-brown skin and long straight black hair in a high ponytail, a hand over her mouth.
FURTHER BACK: soft figures, young and old, women and men, hair dark, grey, shaved, braided or curly — never two alike; the back rows react a beat after the front.
SHIRTS — every fan, hers included, wears a plain generic football shirt in ONE of three colourways and none outside them: TERRACOTTA (washed terracotta body, cream collar and cuffs, like hers) on about half of them, CREAM (cream body, terracotta collar and cuffs) on about a third, BRICK (deep brick-brown body, cream collar and cuffs) on the rest; every chest plain: no crest, no sponsor, no number, no text.
CONTACT: nobody touches her.""",
    """SCENE — A late-afternoon football match: @TORCEDORA sits in the grandstand of a stadium full of fans all around her in terracotta, cream and brick football shirts, watching the match.
THE SOUL OF THE SCENE (play it, never explain it): this is the best part of her week — she is hooked on the game, lit up and happy, natural and never overplayed.""",
    add_lock(match_locks("@TORCEDORA", "her lips may part in a small excited breath but form no words; the crowd is only a roar with no words standing out",
                         eyes="her eyes bright on the match just beside the lens, close to the camera but never into it"),
             "4. CROWD: every fan around her is a different person — a different age, sex, skin tone and hair, the two neighbours unlike each other and unlike her — and every one wears a plain generic football shirt in terracotta, cream or brick — WRONG if two fans look alike, anyone has her face, anyone wears everyday clothes or a colour outside the three, or any shirt shows a crest, sponsor, number or text."),
    timeline(1, [], [
        "BEAT 1 (0–4s) — the MATCH FRAME, MCU: @TORCEDORA's face dead centre and frontal, her eyes bright and locked on the play just beside the lens, lit up with excitement — a small excited breath, a smile that comes and goes and widens as the play builds — the heavy-set man on frame-LEFT, the silver-haired woman in glasses on frame-RIGHT and the fans behind them, each a different person in terracotta, cream and brick football shirts, a little softer than her and excited too; the slow dolly-out runs the whole take, the crowd opening wider around her. Hard end.",
    ]),
    acting("TORCEDORA", "this is her Sunday ritual and she is hooked.",
           "follow the play with bright, happy attention, like a friend in the next seat who is thrilled to be there.",
           "bright on the match, just beside the lens, never into it.",
           "a small excited breath as the play builds",
           "blasé, flat or calm, exaggerated or frantic reactions, shouting, arms up, face paint, a scarf, a club crest or sponsor on her jersey, looking straight into the lens"),
    T.dolly_out(4),
    T.MATCH_FRAME + "\nIn this take her face is frontal and dead centre as in the frame above, but her eyes are on the match, just beside the lens, not into it.",
    """PHYSICS & MATERIAL — the stand vibrates faintly with the crowd; wind moves the hem of her jersey; the fans around her rise and settle, lean and gasp, each in their own way, soft shapes. """ + REAL + """ MATERIAL TRUTH: the velour of her terracotta football jersey with its cream polo collar and cuffs and a plain chest, her smooth slicked-back hair, a bead of sweat at the hairline, the glint of her gold hoops; the polyester weave of the fans' plain football shirts, their cream collars, the creases across their chests.""",
    T.LIGHT_EXT,
    T.FILM_LOOK,
    f"""SOUND — LOCATION SOUND ONLY: a dense wordless crowd roar swelling, soft gasps and "oh" sounds around her; a whistle far off. NO chanting songs, NO drums, NO brass band, NO anthem. {T.MUSIC_POLICY}""",
    T.WORLD + " Wardrobe and crowd carry NO real football club colour combinations (black-and-white, blue-and-white, green-and-white, red-and-black), NO yellow-and-green, NO flags, NO scarves; every football shirt in the frame, hers included, is generic and fictional — a plain chest, no crest, no sponsor, no number, no text — and belongs to one short palette: terracotta, cream and brick, nothing else.",
    f"""NEGATIVE: a blasé, bored, flat or neutral expression, exaggerated or frantic reactions, the fan speaking or shouting, any mouth forming words, her looking straight into the lens, cheering arms, an emblem or crest on her jersey chest, a sponsor logo, a shirt number or text on her jersey, a recognisable real club's kit, a crest, sponsor, number or text on any shirt in the crowd, a shirt in any colour outside terracotta, cream and brick, fans in everyday clothes, neighbours who look alike or share the same hair, age or skin tone, a long-haired young woman on each side of her, a fan with her face, a flat crowd, fans looking into the lens, loose or voluminous hair on her, scarf, flag, face paint, black-and-white, blue-and-white, green-and-white, red-and-black, yellow-and-green, faces in the crowd sharper than hers, chanting, drums, a cut, the face drifting off centre, a zoom, a generic or plain-looking woman, {T.NEG_DOLLY}.""",
    """[ORDER: ONE take, 4s, MATCH FRAME medium close-up with a slow dolly-out — @TORCEDORA's face dead centre and frontal, her eyes bright on the match just beside the lens, lit up, a smile that comes and goes and widens, a full stand of excited fans all around her — a heavy-set man on frame-LEFT, a silver-haired woman in glasses on frame-RIGHT, a different face in every seat — all in plain generic football shirts in terracotta, cream and brick, the crowd opening wider as the camera backs away; hard end. Invariants: face centred throughout, the camera backing away with no zoom; eyes just beside the lens, never into it; lively and happy, never blasé and never overplayed; no dialogue; every fan a different person, the two neighbours unlike each other; every shirt a plain generic one in terracotta, cream or brick, no crest, sponsor, number or text, no real club colours. Look: 35mm color negative, warm halation, lifted blacks, organic grain. NO music, NO chants, NO drums. NO subtitles, NO text.]""",
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
4. SHOT 2 is a medium shot, waist-up, from the first row of seats behind and to the right of him: he is already turned to the lens at the cut and speaks at 3–8s, a hand on the wheel — WRONG if he stands, the bus moves or the first word waits more than a third of a second after the cut.
5. Only @MOTORISTA speaks, only this line, in ONE brisk flow with no pauses — every other mouth closed. Daylight from frame-LEFT — NO music.""",
    timeline(2, [3], [
        "SHOT 1 (0–3s) — the MATCH FRAME, MCU of @MOTORISTA at the wheel, face dead centre, straight into the lens with a warm smile, the stopped bus soft behind him — the windshield, the aisle and the shut glass door on frame-LEFT — opening wider as the slow dolly-out runs the whole shot. HARD CUT.",
        "SHOT 2 (3–10s) — MS (waist-up: the driver at the wheel, the windshield and the stopped avenue soft behind him), 40°, handheld from the first row of seats behind and to the right of him: @MOTORISTA, one hand on the wheel, already turned to the lens at the cut, starts the line at once and speaks at 3–8s in one brisk flow, glancing at the windshield and back, smiling; at 8–10s he holds the smile. Hard end.",
    ]),
    dialogue(line(3, 8, "MOTORISTA", "Se Minas tem o que o futuro procura, esse futuro também precisa chegar até os mineiros."), "MOTORISTA"),
    acting("MOTORISTA", "every day he takes people to where the opportunities are.",
           "greet you with a smile, then explain the route like one he loves, brisk and bright, no drag — a hand on the wheel, eyes splitting between the windshield and you, checking you followed.",
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
    """[ORDER: 2 shots, 1 hard cut at 3s, 10s — (1, 0–3s) MATCH FRAME medium close-up of the driver, face dead centre, smiling into the lens, slow dolly-out (no zoom) — (2, 3–10s) medium shot, waist-up, from the first row behind and right of him, the bus STOPPED: he is already turned to the lens and says his line at 3–8s in one brisk flow, smiling; he holds the smile at 8–10s. Invariants: Brazilian city-bus look (yellow handrails, blue patterned seats, grey rubber floor); the bus stopped, the door shut, no student; shot 1 face centred, camera backing away with no zoom; he speaks only in shot 2. Look: 35mm color negative, warm halation, lifted blacks, organic grain. Brazilian Portuguese. NO music. NO subtitles, NO text.]""",
)

# ---------------------------------------------------------------- T12-B (só o dolly do motorista, em 4s; substitui o plano 1 da T12)
T12B = join(
    contract(4, "ONE continuous take, no cuts", "a slow dolly-out from a medium close-up, inside a stopped bus", dialogue=False),
    f"""REFERENCES — each reference has ONE job:
@MOTORISTA — IDENTITY of @MOTORISTA: face, hair, build, hands and wardrobe. 100% matches.
@ONIBUS_INT — PLACE of the bus: the layout, the yellow handrails, the seats, the windows, the floor, the door. 100% matches the place.
{SCOPE_ID} For @ONIBUS_INT: IGNORE any people, any text, stickers, signs or logos, the light, the exposure and the colour grade, raindrops on the glass, and whatever is seen outside the windows.""",
    f"""WHO IS WHO — READ FIRST, ABSOLUTE:
@MOTORISTA ({ANCH['MOTORISTA']}) — the BUS DRIVER: sits at the wheel and smiles into the lens; NEVER speaks; the bus is STOPPED; NEVER stands, NEVER opens the door.
FACES: his face exists once; nobody else near him; two or three seated passengers far back are soft Brazilian adults with their mouths closed; nobody boards, no student; no twins, no clones.
CONTACT: nobody touches anyone.""",
    """SCENE — Late afternoon inside a clean, well-kept Brazilian city bus in Belo Horizonte, STOPPED at a stop with the engine idling — yellow handrails, blue patterned seats, a grey rubber floor, a folding glass door shut. @MOTORISTA sits at the wheel looking at you; the camera faces him from the windshield side, the aisle, the seats and the windows of the bus behind him.
THE SOUL OF THE SCENE (play it, never explain it): every day he drives people to where the opportunities are; he is proud of where this route goes — he looks at you with a smile, as if you had just stepped on.""",
    f"""{LOCKS_HEAD}
1. ONE take in the MATCH FRAME with the slow dolly-out (the camera moving back, no zoom), no cuts — WRONG if it cuts, if the camera is locked, or if the lens zooms or the camera pushes in.
2. The FIRST FRAME is a medium close-up, head and shoulders: his WHOLE head in frame with air above the hair (his head about half of the frame height, the top of his head at about 12% from the top edge, his chin at about 62%), his collar and the tops of his shoulders in the lower third — WRONG if the start is tighter (an extreme close-up, the face filling the frame, the forehead or hair cropped) or the camera starts closer than 1.3 m.
3. The camera stays at his EYE HEIGHT or a hair above, the 47° lens fixed, with DEEP focus: the yellow handrails, the blue seats and the windows behind him stay readable, only gently soft — WRONG if the camera is below his eyes or looks up at him, if the lens distorts his face (a wide-angle look, a big nose), or if the background melts into a blur.
4. His face stays dead centre and frontal, straight into the lens with a warm smile for the whole take, while the framing opens gently toward a medium shot — the move covers only about a metre in total, ending about 2.3 m away — WRONG if the face drifts off centre, he looks away or down, the move is fast or the framing ends wide.
5. NO dialogue: his mouth stays closed in a smile — WRONG if any mouth forms words. The bus is STOPPED: nothing slides past the windows, no motion blur, the glass door stays shut, nobody boards. Daylight from frame-LEFT — NO music.""",
    timeline(1, [], [
        "BEAT 1 (0–4s) — the MATCH FRAME, MCU: @MOTORISTA's face dead centre, his whole head in frame with air above the hair, the camera at his eye height or a hair above, his eyes straight into the lens, a warm smile for the whole take; the stopped bus behind him — the yellow handrails, the blue seats, the aisle and the windows, readable — opening wider as the slow, gentle dolly-out runs the whole take, ending as a medium shot with his face still dead centre. Hard end on the held smile.",
    ]).replace("TIMELINE — ONE continuous take, no cuts, already in progress at the first frame:", "TIMELINE — ONE continuous take, no cuts; the very first frame is already the MATCH FRAME (head and shoulders, 1.3 m):"),
    acting("MOTORISTA", "every day he takes people to where the opportunities are, and you have just stepped onto his bus.",
           "greet you with a warm, proud smile, like a friend glad to see you — easy and bright, nothing more.",
           "on the lens throughout.",
           "a slow happy blink",
           "speaking, a blank face, looking away or down, standing up"),
    T.dolly_out(4).replace("FOCUS: on the eyes throughout.", "FOCUS: on the eyes throughout, with a deep depth of field — the handrails, seats and windows behind him stay readable, NO creamy bokeh; the camera at his eye height or a hair above.").replace("the move never stops or reverses.", "the move is gentle, about 0.25 m a second, never closer than 1.3 m, never farther than 2.4 m, and never stops or reverses."),
    T.MATCH_FRAME.replace("the camera at the subject's eye height about 1.3 m", "the camera at the subject's eye height or a hair above (never below), about 1.3 m").replace("medium close-up (head and shoulders) at 47°", "medium close-up (his whole head with air above the hair, and his shoulders) at 47°").replace("the background soft", "the background readable and only gently soft"),
    """GEOMETRY — the driver's seat on the bus's left side; the camera faces him from the windshield side at his eye height or a hair above, starting 1.3 m from his face and backing along the same axis to about 2.3 m; behind him the aisle of the bus, the yellow handrails, the blue patterned seats and the windows, the glass folding door on frame-LEFT; the daylight from frame-LEFT.""",
    """PHYSICS & MATERIAL — the bus is still, the engine idling with a faint vibration; light shifts softly on the glass; his shirt moves with his breath. """ + REAL + """ MATERIAL TRUTH: the glass of the door, the grey rubber floor with its yellow edge line, yellow-painted handrails with grey clamp brackets, grey seat shells with blue patterned cushions, the cotton of his pale grey shirt.""",
    T.light_int("the bus's windshield and door-side windows",
                "no other source inside the bus.",
                "the daylight lights the frame-LEFT side of his face; the bus behind falls off a stop."),
    T.FILM_LOOK,
    f"""SOUND — LOCATION SOUND ONLY: the engine idling; a quiet stopped avenue outside, a distant horn; the fabric of his shirt. {T.MUSIC_POLICY}""",
    T.WORLD,
    f"""NEGATIVE: an extreme close-up, the face filling the frame, the forehead or hair cropped, a start closer than 1.3 m, a camera below his eyes or looking up at him, wide-angle distortion of the face, a big nose, a very blurred background, creamy bokeh, a fast move, the door opening, a student or any boarding passenger, a moving bus, motion blur outside, rain or raindrops on the windows, a logo on the steering wheel, chrome or satin-steel handrails, a European or American bus interior, an all-grey interior, readable stickers or fare signs, him standing, him speaking or any mouth forming words, the face drifting off centre, a zoom, a cut, a generic or plain-looking man, {T.NEG_DOLLY}.""",
    """[ORDER: ONE take, 4s, MATCH FRAME medium close-up with a slow dolly-out — @MOTORISTA's face dead centre, his whole head in frame with air above the hair at the start (never an extreme close-up), the camera at his eye height or a hair above, eyes straight into the lens, a warm smile; the stopped Brazilian city bus behind him (yellow handrails, blue patterned seats, windows) readable and only gently soft, opening wider as the camera backs away gently from 1.3 m to about 2.3 m, no zoom; hard end on the held smile. Invariants: the start is head and shoulders; the camera never below his eyes; deep focus, not a blur; face centred throughout; no dialogue; the bus stopped, the door shut, no student. Look: 35mm color negative, warm halation, lifted blacks, organic grain. NO music. NO subtitles, NO text.]""",
)

# ---------------------------------------------------------------- T14
T14 = join(
    contract(6, "ONE continuous take, no cuts", "handheld"),
    f"""REFERENCES — each reference has ONE job:
@ESTUDANTE — IDENTITY of @ESTUDANTE: face, hair, build, hands and wardrobe exactly as on the sheet. 100% matches.
{SCOPE_ID}""",
    f"""WHO IS WHO — READ FIRST, ABSOLUTE:
@ESTUDANTE ({ANCH['ESTUDANTE']}) — the STUDENT: alone in the foreground at a workshop bench, already facing the lens in the very first frame, a tablet low in one hand, speaks once to the lens; NEVER takes off the hoodie; NEVER looks or acts like a teacher.
OTHER STUDENTS — four or five teenagers of 15–16 in casual everyday clothes, far behind him at their own benches, each working on a DIFFERENT project of their own (one soldering, one typing on a laptop whose screen faces away, two assembling a small chassis, one measuring a part), soft, not looking at the lens or at the robot; nobody stands beside him; NO uniforms, NO lab coats, NO adults; NEVER speak.
ROBOT — a small amateur robot about 20 cm tall that the students built themselves, on the bench just behind his shoulder: grey and white 3D-printed parts, visible servo motors, a bare microcontroller board with jumper wires, a few zip ties, a little crooked, hand-assembled, two small LED eyes; NO batteries and NO battery pack anywhere on it; NOT a toy, NOT a polished product; no logos; it waves one arm side to side WITHOUT STOPPING for the whole take, in complete silence.
FACES: each face exists once.
CONTACT: nobody touches anyone.""",
    """SCENE — Afternoon in the robotics workshop of a free technical course for teenagers in Belo Horizonte, Brazil — a bright, organised room with the quiet buzz of kids making things: neutral grey metal shelving with matte grey and black equipment cases and tidy cable reels, a 3D printer, a soldering station, closed laptops, long benches. @ESTUDANTE stands alone at a bench in the foreground, a tablet in his hand, the robot they built waving behind him, the other students busy with their own projects far behind.
THE SOUL OF THE SCENE (play it, never explain it): he and his friends built a robot that really works and he is thrilled — he tells you what this place is for, like one of the gang.""",
    f"""{LOCKS_HEAD}
1. ONE continuous handheld take, no cuts.
2. The tablet's SCREEN is NEVER visible: held low at his side with its back to the lens — WRONG if any screen, interface or screen glow is shown.
3. He is ALREADY facing the lens in the first frame (no turning) and speaks at 0–5s, eyes alive; the name Codemig is said exactly Cô-dê-mí-gui — the first syllable with a CLOSED ô, never an open ó, and no R sound anywhere — WRONG if he turns first, if glassy, or if the name comes out as anything else; only he speaks.
4. DELIVERY: his voice is lively, bright and slightly excited — a smile in the voice, the pitch lifting on "isso", on the name and on "conexão" — WRONG if it is flat, dull, tired, mumbled or monotone, and equally WRONG if it is euphoric, shouted, giggly or a kids'-show host.
5. @ESTUDANTE wears exactly his sheet wardrobe: dark charcoal (almost black) hoodie, white T-shirt hem showing below it, black skinny jeans — WRONG if anything changes.
6. He stands ALONE in the foreground; every other student is far behind, busy with their own different project and not watching — WRONG if anyone stands beside him, a crowd watches the robot or the lens, or any adult, uniform or teacher-like posture appears.
7. The robot is small, amateur and student-built, with NO batteries, waves without stopping and makes NO sound — WRONG if it stops, whirs or beeps, shows batteries, or looks like a store-bought toy.
8. The room is BRIGHT and airy: daylight from frame-LEFT plus the ceiling lights on, no dark corners — WRONG if it is dim, murky or moody. Neutral matte professional shelving and cases, nothing toy-like; no readable text or logo — NO music.""",
    timeline(1, [], [
        "BEAT 1 (0–5s) — MS (waist-up, the bright workshop soft around him), 40°, handheld: @ESTUDANTE alone at a long bench, already facing the lens, the tablet held low in one hand with its back to us, the amateur robot on the bench behind his shoulder waving its arm side to side without stopping, the other students far behind each busy with their own project; he speaks at 0–5s, lively and bright, slightly excited, a smile in his voice, his eyebrows lifting on the key words and the grin breaking through on \"conexão\".",
        "BEAT 2 (5–6s) — he holds the proud grin, eyes on the lens, the robot still waving behind him. Hard end on the held look.",
    ]),
    dialogue(line(0, 5, "ESTUDANTE", "É para isso que a Cô-dê-mí-gui existe… para fazer essa conexão acontecer.").replace(
        "(on camera, Brazilian Portuguese)",
        "(on camera, Brazilian Portuguese; lively and bright, slightly excited — a teenager telling his friends about something that really works, a real smile in the voice, the pitch lifting and falling with energy; never flat, never euphoric)"),
        "ESTUDANTE",
        pace="PACING — ONE brisk, buoyant flow (about 5 syllables a second) with energy in it: the pitch lifts on \"isso\", peaks lightly on the name, lifts again on \"conexão\" and closes bright and sure on \"acontecer\"; the ellipsis is only a breath, never a drop in energy; the first word lands as the window opens, no pause, no trailing off, no mumbling.").replace(
        "\nVOICE LOCK",
        "\nPRONUNCIATION — the name is said Cô-dê-mí-gui: four even syllables; the FIRST syllable has a CLOSED, rounded ô, like the o in \"bolo\" and \"avô\", NEVER the open ó of \"avó\" or \"pó\"; the second has a closed ê; the stress falls on mí; the last syllable is just \"gui\" (a hard G and an i); there is NO R sound anywhere in the name — NEVER \"Có-dê-mí-gui\", \"Codemigri\", \"Codemiji\" or \"Codemaig\"; said once, clearly, inside the sentence.\nVOICE LOCK"),
    acting("ESTUDANTE", "he and his friends built a robot that works, and he can't help sharing it.",
           "tell you, lit up, what this place is for — brisk and bright with a lifting tone, a real smile breaking through, like a friend sharing something he is proud of, never a teacher or a presenter.",
           "on the lens throughout, bright and sure, his eyebrows lifting a hair on the key words.",
           "a quick happy breath in through the nose before the first word",
           "a flat, tired, bored or mumbled delivery, euphoria, shouting, giggling, a kids'-show host, a teacher's or presenter's posture, a cheeky smirk, a teenage pose, turning toward the camera"),
    "ACTING — OTHER STUDENTS (background): absorbed in their own different projects; NOT looking at the lens, NOT at the robot, NOT speaking.",
    T.handheld(),
    """PHYSICS & MATERIAL — the robot's single arm swings side to side on its servo, a little stiff and uneven, a little endearing, without a sound; the tablet is a thin slab with a matte case. """ + REAL + """ MATERIAL TRUTH: the matte-grey case of the tablet, the slightly uneven grey and white 3D-printed parts of the robot with visible screws, jumper wires and zip ties, the matte cotton knit of his hoodie, neutral matte grey metal shelving, dark grey and black equipment cases, coiled cables, a 3D printer and a soldering station, the everyday cotton T-shirts and hoodies of the students.""",
    """LIGHT — BRIGHT DAYLIGHT INTERIOR WITH THE ROOM LIGHTS ON (KEY): one dominant motivated source with soft-edged shadows, the whole room clearly lit.
SOURCE: daylight through the workshop's big windows on frame-LEFT, ~5600 K, soft and directional, with the ceiling's linear LED panels switched on at the same ~5600 K as an even, soft fill so no corner goes dark.
REACH: the daylight shapes the frame-LEFT side of his face and the bench; the ceiling light opens the shadows and keeps the room behind bright, only half a stop below the foreground.
EXPOSURE: exposed for skin; the room bright and airy; highlights creamy; blacks only slightly lifted; no murky, dim or underexposed areas.
CONTINUITY: the daylight stays frame-LEFT; the ceiling fill stays even and neutral, never competing with it.
NOT: a dim, moody or murky room, deep shadows in the corners, a green or blue fluorescent cast, flat top light as the key, a blown-out window.""",
    T.FILM_LOOK,
    f"""SOUND — LOCATION SOUND ONLY: a fan humming; students working and chatting low at far benches, no words standing out. The robot makes NO sound. {T.MUSIC_POLICY}""",
    T.WORLD,
    f"""NEGATIVE: a flat, dull, tired, monotone or mumbled delivery, euphoria, shouting, giggling, a kids'-show host voice, a visible tablet screen or any screen content, mispronouncing the name (Có-dê-mí-gui with an open ó, Codemigri, Codemiji, Codemaig), batteries or a battery pack on the robot, a robot motor whirr, servo noise or beeps, a robot that stops waving, a large, polished, store-bought or toy robot, a classmate beside him, a fist bump, a dim, dark, moody or murky room, toy-like boxes, colourful storage boxes, cartoon packaging, a children's playroom look, a crowd watching the robot, an adult, a teacher, uniforms, lab coats, a classroom lesson posture, him turning to the lens, different wardrobe from the sheet, programme logo, posters with text, readable labels, a cut, {T.NEG_SPINE}.""",
    """[ORDER: ONE handheld take, 6s, medium shot waist-up — he is alone in the foreground at the bench, already facing the lens, the tablet low at his side with its back to us, the little amateur robot (no batteries) waving silently without stopping behind his shoulder, the other students far behind busy with their own projects; he says his line at 0–5s, lively, bright and slightly excited (a smile in the voice, lifts on \"isso\", the name and \"conexão\"; never flat, never euphoric), the name said Cô-dê-mí-gui with a CLOSED ô and no R in it, then holds the grin to 6s; hard end. Invariants: a lively, slightly excited delivery, never flat and never euphoric; no tablet screen ever visible; he faces the lens from the first frame; nobody beside him; a small amateur student-built robot that waves silently the whole time; a BRIGHT room, daylight from frame-LEFT plus ceiling lights on; neutral matte professional shelving, nothing toy-like; the sheet wardrobe; living eyes; handheld. Look: 35mm color negative, warm halation, lifted blacks, organic grain. Brazilian Portuguese. NO music. NO subtitles, NO text.]""",
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
        "ENFERMEIRA", pace=None),
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
    contract(5, "ONE continuous take, no cuts", "handheld, close and breathing, a tight close-up whose opening framing follows the attached depth map"),
    f"""REFERENCES — each reference has ONE job:
@JOVEM — IDENTITY of @JOVEM: face, skin texture, hair and wardrobe. 100% matches.
@DEPTH_T16 — DEPTH MAP of the opening frame: a grey picture where WHITE is nearest to the lens and DARK is farthest. Its ONLY job is the opening GEOMETRY: the head dead centre, the crown of the curls near the top edge, both ears and the neck, the collar and both backpack straps filling the bottom, the hills falling away in layers behind him. It is a measurement, not a photograph.
{SCOPE_ID} For @DEPTH_T16: take the framing, the distances and the layering of near and far, and NOTHING else — its grey look, its flat white head and shoulders, its blank featureless face and its lack of colour must NEVER appear. The film is full colour; his face is a real, detailed face that comes from @JOVEM; the colour, light and landscape come from this text.""",
    f"""WHO IS WHO — READ FIRST, ABSOLUTE:
@JOVEM ({ANCH['JOVEM']}) — the PROTAGONIST: speaks his last words to you, close and warm; his face fills the frame dead centre.
FACES: his face exists once; nobody else.""",
    """SCENE — The same summit in Minas Gerais, Brazil, at the same late-afternoon hour: the layered green hills and flat-topped mesas fall away soft behind him under a pale, warm sky. @JOVEM, in a tight close-up, is already looking at you with a closed-mouth smile.
THE SOUL OF THE SCENE (play it, never explain it): he has shown you everything and he is happy, a little moved, and sure — "O minério é nosso" is pride, "o futuro também" is an invitation to say yes with him.""",
    f"""{LOCKS_HEAD}
1. ONE handheld take in a tight close-up — WRONG if it cuts, widens, pushes in or is locked.
2. The FIRST FRAME has the framing of @DEPTH_T16 — head dead centre, the crown of his curls near the top edge, both ears and the neck, the collar and both backpack straps at the bottom edge, the hills receding in layers behind him — but in FULL COLOUR, with a real detailed face, a closed-mouth smile and eyes on the lens — WRONG if the framing differs, if any frame is grey or looks like a depth map, or if his face is blank, flat or smooth.
3. His eyes stay on the lens and ALIVE from start to finish, travelling between your two eyes — WRONG if glassy, frozen or looking away.
4. The performance is warm and personal, a promise between friends — WRONG if it is a slogan, a speech, a stiff mask, a smirk, a wink or tears.
5. Real skin in detail: pores, light stubble, the small mole on his left cheek (frame-right as he faces the lens) — WRONG if smooth or retouched.
6. Only @JOVEM speaks, only this line, from 1s to 3s, in ONE brisk flowing delivery — WRONG if he pauses inside it for more than a breath at the comma, drags a word or stops for effect. Sun from frame-LEFT — NO music.""",
    timeline(1, [], [
        "BEAT 1 (0–1s) — CU, 31°, handheld 1.2 m from his face at eye height, breathing, framed EXACTLY as @DEPTH_T16: his head dead centre, the crown of his curls near the top edge, both ears and the neck visible, the collar and backpack straps at the bottom edge — in full colour, with a closed-mouth smile and eyes on the lens; a quiet breath in.",
        "BEAT 2 (1–3s) — he says the line in one bright, flowing breath, like good news he can't wait to share: the first half firm and quick, the second a bright invitation, the smile opening fully on \"o futuro também\".",
        "BEAT 3 (3–5s) — he holds your eyes with the open smile. Hard end on the held look.",
    ]),
    dialogue(line(1, 3, "JOVEM", "O minério é nosso, o futuro também."), "JOVEM",
             pace="PACING — ONE continuous flow of speech from 1s to 3s, about 6 syllables per second: bright, brisk, forward, with only a breath at the comma. NO pause, NO held beat, NO trailing off — the acting happens WHILE he speaks, never between the words."),
    """ACTING — @JOVEM (fully invested in the tactic; the work happens in the eyes and the face)
SCENE DIRECTION (shared, unspoken): tell a friend some good news about your state — happy and proud of what you are saying, a real smile that comes and goes; the lens is that friend.
EVENT: he has just shown you everything he loves about this place; this is the last thing he wants you to take with you.
MOTIVE: he is proud and a little moved, and he wants you to feel it too.
GOAL: to get your yes — to make you feel that this future is yours as well.
OBSTACLE: the lump in his throat, felt only in the eyes, never in the delivery — he keeps talking, brisk and warm, and it never becomes tears or a pause.
TACTIC: say it close, bright and quick, like good news you can't wait to share — certain and flowing, never a speech, never slow.
MOMENT TO MOMENT:
(0–1s) the closed-mouth smile, eyes steady on you, a quiet breath in; one corner of his mouth lifts a little more just before he speaks.
(1–3s) the line in one flowing breath: "O minério é nosso," — firm and quick, the chin lifts a hair, one small nod on "nosso"; a breath at the comma; "o futuro também." — the invitation: the brows lift, the eyes brighten, the smile opens fully and he leans a hair toward the lens, asking for your yes — all of it WHILE he speaks, never in a pause.
(3–5s) the held look: the smile at full, the eyes bright and a little glossy with joy (never tears), a short laugh of breath through the nose; he stays with you, never looks away.
EYES: on the lens throughout, travelling between your two eyes; pupils search, settle and drift; blinks uneven and never on the beat of the words; slight asymmetry; a real smile in which the eyes smile with the mouth.
NOT: a slow or deliberate delivery, pauses inside the line, a dramatic stop before "o futuro também", trailing off, a slogan or campaign-ad delivery, a speech, a stiff mask of a face, a frozen pupil, a smirk, a wink, tears, crying, over-acting.""",
    T.handheld(),
    """PHYSICS & MATERIAL — the wind from frame-left moves a few curls at his temple and the edge of his collar; his breath moves his lips and nostrils; the handheld breath makes the frame sway a few millimetres; his skin catches the light unevenly. """ + REAL + """ MATERIAL TRUTH: pores and fine lines at the eyes, light stubble with individual hairs, the weave of his rust-red overshirt collar, the straps of his backpack.""",
    T.LIGHT_EXT,
    T.FILM_LOOK,
    f"""SOUND — LOCATION SOUND ONLY: wind across the open summit, steady and quiet; dry grass hissing; his breath; after his last word, only the wind. {T.MUSIC_POLICY}""",
    T.WORLD,
    f"""NEGATIVE: a cut, widening the frame, a push-in, an opening frame whose framing differs from @DEPTH_T16, a grey or black-and-white frame, a depth-map look, a blank or featureless face, a white silhouette, smooth retouched skin, watery eyes, tears, a wink, a smirk, a slogan or ad delivery, a stiff expressionless face, looking away, pauses inside the line, a slow deliberate delivery, a dramatic stop before "o futuro também", {T.NEG_SPINE}.""",
    """[ORDER: ONE handheld take, 5s, tight CU 31°, opening framed EXACTLY like @DEPTH_T16, in full colour — (0–1s) head dead centre, closed-mouth smile, eyes on the lens — (1–3s) the line in one bright flowing breath, "O minério é nosso," firm and quick, "o futuro também." as an invitation, the smile opening fully — (3–5s) he holds your eyes with the open smile; hard end. Invariants: handheld, tight close-up; the depth-map framing, full colour; living eyes on the lens; ONE brisk flowing delivery, no pause beyond a breath at the comma; warm and personal, never a slogan; real skin; only his words; sun frame-LEFT. Look: 35mm color negative, warm halation, lifted blacks, organic grain. Brazilian Portuguese. NO music. NO subtitles, NO text.]""",
)


# ---------------------------------------------------------------- T16 · v1 (como estava, antes da rodada de atuação)
T16_V1 = join(
    contract(5, "ONE continuous take, no cuts", "handheld, close and breathing, tight close-up"),
    f"""REFERENCES — each reference has ONE job:
@JOVEM — IDENTITY of @JOVEM: face, skin texture, hair and wardrobe 100% matches.
{SCOPE_ID}""",
    f"""WHO IS WHO — READ FIRST, ABSOLUTE:
@JOVEM ({ANCH['JOVEM']}) — the PROTAGONIST: speaks his last words to you; his face fills the frame just left of centre.
FACES: his face exists once; nobody else.""",
    """SCENE — The same summit in Minas Gerais, Brazil, at the same late-afternoon hour; @JOVEM, in a very tight close-up, is already looking at you; the sea of hills is a soft haze behind him.
THE SOUL OF THE SCENE (play it, never explain it): he has shown you everything and he is happy and sure — "O minério é nosso" is pride, "o futuro também" is an invitation.""",
    f"""{LOCKS_HEAD}
1. ONE handheld take in a very tight close-up — WRONG if it cuts, widens or is locked.
2. His eyes stay on the lens and alive from start to finish — WRONG if glassy or looking away.
3. Real skin in detail: pores, stubble, the small mole on his left cheek (frame-right as he faces the lens) — WRONG if smooth or retouched.
4. Only @JOVEM speaks, only this text.
5. Sun from frame-LEFT — NO music.""",
    timeline(1, [], [
        "BEAT 1 (0–1s) — CU, 18°, handheld 1.3 m from his face, breathing: his face from the eyebrows to the chin, just left of centre, eyes already on the lens.",
        "BEAT 2 (1–3s) — he speaks to the lens, proud and warm, the smile growing.",
        "BEAT 3 (3–5s) — he holds your eyes with an open smile. Hard end on the held look.",
    ]),
    dialogue(line(1, 3, "JOVEM", "O minério é nosso, o futuro também."), "JOVEM"),
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
    """[ORDER: ONE handheld take, 5s, tight CU 18° — (0–1s) eyes on the lens — (1–3s) his words to you, proud and warm — (3–5s) he holds your eyes, smiling. Invariants: handheld, tight close-up; living eyes on the lens; real skin; only his words; sun frame-LEFT. Look: 35mm color negative, warm halation, lifted blacks, organic grain. Brazilian Portuguese. NO music. NO subtitles, NO text.]""",
)
