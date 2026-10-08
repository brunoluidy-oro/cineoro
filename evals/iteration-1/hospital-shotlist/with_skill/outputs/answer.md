# Corredor da UTI · decupagem para Seedance 2.5 (21:9)

O shotlist em HTML está em `/home/user/cineoro/evals/iteration-1/hospital-shotlist/with_skill/outputs/shotlist.html`. Cada geração tem botões de copiar, a tabela de planos, o prompt completo e o card. Os mesmos prompts estão abaixo.

A cena virou **2 gerações, 51 s no total**: **1a** (26 s, 4 planos), a notícia, e **1b** (25 s, 3 planos), a visita. A virada ("Mas não acordou") fica inteira na 1a, num plano sustentado. A 1b termina em Ruiz, que é onde a cena assenta.

## Decisões que tomei

- **"Mas não acordou" sai em off, em cima do rosto da Clara.** A virada cai em quem escuta. O ombro do Ruiz fica no quadro para a voz ter de onde vir, e a boca dela fica travada como fechada.
- **Clara fica sentada até "Só cinco minutos"**, com o copo nas mãos o tempo todo. No corredor ninguém toca ninguém. O único toque da cena é ela segurando a mão do pai.
- **Ruiz não fiscaliza os cinco minutos.** Ele olha um instante a mais do que precisava e vai embora antes que ela o veja. A câmera não vai atrás dele.
- **O pai não reage em momento nenhum**: olhos fechados, a mão sem força. Esse é o maior risco da 1b, porque o motor adora um milagre.
- **Elenco e mundo**, que inventei e você pode trocar:
  - Clara de cardigã verde-musgo e cabelo preso numa piranha.
  - Ruiz de scrub azul-marinho, com as marcas vermelhas da máscara no rosto.
  - O pai com 78 anos e máscara de oxigênio.
  - Hospital público brasileiro, 3 da manhã, corredor com as luzes em modo noturno.
- **Fala**: português do Brasil com sotaque paulistano para os dois. Se o Ruiz for estrangeiro (o nome sugere isso), troque nos rótulos das falas e no VOICE LOCK por "Brazilian Portuguese with a light Rioplatense Spanish accent".
- **Luz e look**: a luz fria da UTI, entrando pela janelinha, é a luz principal e vem sempre do lado direito do quadro. Look de 35mm tungstênio sob fluorescente, lente esférica, sem vinheta, sem música e sem legendas.
- **Plataforma**: Seedance 2.5 em reference-to-video, com a sintaxe `@Image N` (BytePlus/fal). No Higgsfield, digite @ e escolha os uploads na mesma ordem. Primeiro um draft em 480p, depois o final em 1080p.

## Shotlist

| Ger. | Plano | Tempo | Enquadramento | O que acontece |
|---|---|---|---|---|
| 1a | 1 | 0–7s | Plano geral (master), 47° | Clara espera sentada; a porta abre; Ruiz sai tirando a máscara |
| 1a | 2 | 7–11s | Primeiro plano do Ruiz, 29°, de baixo | "Ele está estável." |
| 1a | 3 | 11–20s | Close da Clara por cima do ombro do Ruiz, 29° (a virada) | "Mas não acordou." (off), silêncio, "Posso entrar?" |
| 1a | 4 | 20–26s | Plano geral (master), 47° | "Só cinco minutos." Ela começa a levantar e o corte vem no meio do movimento |
| 1b | 1 | 0–7s | Plano geral (master, a partir do último frame da 1a), 47° | Copo na cadeira; ela entra sem tocar nele; a porta fecha |
| 1b | 2 | 7–15s | Plano médio pela janelinha, 29° | Ela segura a mão do pai e vigia as pálpebras dele; ele não reage |
| 1b | 3 | 15–25s | Primeiro plano do Ruiz na janelinha, 29° | Ele olha, solta o ar e vai embora pelo corredor; a câmera fica |

---

## Geração 1a · 26s · 4 planos · 21:9

```
O QUE ACONTECE: Clara espera sentada com o café já frio; a porta da UTI abre e o Dr. Ruiz sai tirando a máscara. Ele dá a notícia em duas frases; ela não pergunta o que a segunda deixou de fora — pede para entrar.
O QUE É DITO: RUIZ: "Ele está estável." / RUIZ (fora de quadro, sobre o rosto dela): "Mas não acordou." / CLARA: "Posso entrar?" / RUIZ: "Só cinco minutos."
TEMPO: espera, a porta abre, Ruiz sai — 7s · Ruiz, primeira frase — 4s · rosto da Clara: "Mas não acordou", o silêncio, a pergunta — 9s · plano geral: "Só cinco minutos", ela começa a levantar — 6s = 26s
COMO TERMINA: corte seco no meio do levantar dela, o copo na mão direita, Ruiz já virando para a porta.
```

```
CONTRACT — Live-action photoreal film footage, 21:9, 26 seconds total, 4 shots with 3 hard cuts at 7s, 11s and 20s, quiet breathing handheld, real-time motion, dialogue as spoken on-camera audio in Brazilian Portuguese with native São Paulo accents. NO music, NO score, NO subtitles, NO on-screen text.

REFERENCES — each reference has ONE job:
@Image 1 — IDENTITY of @CLARA: face, hair, hands, build, moss-green knit cardigan, grey T-shirt, jeans. 100% matches.
@Image 2 — IDENTITY of @RUIZ: face, grey stubble, hands, build, navy scrubs over a grey long-sleeve thermal, stethoscope. 100% matches.
@Image 3 — WORLD: the ICU corridor at night — walls, linked chairs, the ICU swing door with its small window, vinyl floor; architecture and materials for all four shots, not its light or lens.
REFERENCE SCOPE: @Image 1 and @Image 2 supply faces, hair, hands, build and wardrobe ONLY — IGNORE their backdrops, lighting direction, exposure and colour grade.

WHO IS WHO — READ FIRST, ABSOLUTE:
@CLARA (40, slim, olive skin, dark circles, dry lips, dark-brown hair in a loose claw clip with strands falling, no makeup; oversized moss-green cardigan, grey T-shirt, jeans, white sneakers) — the DAUGHTER: sits holding a paper cup of cold coffee in both hands, listens, asks one question, starts to rise at the very end; NEVER stands before 23s, NEVER cries, NEVER looks into the lens; owns the LEFT side of the frame.
@RUIZ (55, heavy-set, short grey hair, grey-white stubble, deep lines at the eyes; navy scrubs over a grey long-sleeve thermal, stethoscope; a pale-blue surgical mask on his face as he comes out, then crumpled in his LEFT hand) — the DOCTOR: comes out of the ICU, takes off the mask, gives the news, grants the visit; NEVER sits or crouches, NEVER smiles; owns the RIGHT side of the frame, in front of the ICU door.
FACES: each face exists once; nobody else in the corridor; no twins, no clones.
CONTACT: nobody touches anyone in this scene.

SCENE — 3 a.m., the corridor outside the ICU of a Brazilian public hospital. @CLARA has been waiting for hours on a row of linked steel chairs, a paper cup of coffee gone cold in her hands, her eyes on the ICU door. The door opens and the doctor comes out to her.
THE SOUL OF THE SCENE (play it, never explain it): neither of them will say the word "if". He tells her exactly what is true and not one word more; she hears what his second sentence leaves out and asks for the door instead of the answer — because the door is something he can give.

ABSOLUTE LOCKS — break one and the take is WRONG, regenerate:
1. @CLARA owns frame-LEFT, seated against the left wall; @RUIZ and the ICU door own frame-RIGHT; the camera stays on the south side of the CLARA–DOOR line in every shot. WRONG if they swap sides or the door appears frame-left.
2. @CLARA stays SEATED, the cup in both hands, until his last line; she starts to rise only at 23s. WRONG if she stands earlier or puts the cup down.
3. Only the four scripted lines; in shot 3 his second line is OFF-SCREEN and @CLARA's lips stay closed until her own question. WRONG if her mouth moves with his words.
4. Dry eyes and no touch — no tears, no hand on her shoulder, no hug. WRONG if anyone touches or cries.
5. No music of any kind, no subtitles.

TIMELINE — 4 shots, 3 hard cuts; cuts only at the specified points, the camera adds no cuts of its own:
SHOT 1 (0–7s) — THE MASTER: WS two-shot, 47°, camera at seated eye height (1.2 m), 4 m south of the CLARA–DOOR line, STAYS PUT: @CLARA is already seated frame-left, torso turned toward the ICU door on the right wall, the cup on her knee in both hands; at 0–3s she turns the cup a quarter-turn, eyes on the glowing door window frame-right. At 3s the latch clacks and the swing door opens; @RUIZ steps out already pulling the mask off with his LEFT hand; the door swings shut behind him on its closer and snaps into the latch at 6s; he stops 1.5 m from her, facing her; she draws the cup up against her chest. She stays seated. HARD CUT.
SHOT 2 (7–11s) — MCU @RUIZ, 29°, camera low beside her right shoulder, 1.6 m from him, tilted slightly up: @RUIZ in the frame-right third facing frame-left, the door window a soft cold rectangle behind his right shoulder; red mask lines on his nose and cheekbones; at 8–10s he speaks his first line. HARD CUT.
SHOT 3 (11–20s) — THE TURN, one sustained shot: CU @CLARA, 29°, over @RUIZ's LEFT shoulder — his dark soft shoulder fills the frame-right edge, his mouth never visible — camera at 1.4 m, 2 m from her, looking slightly down: @CLARA seated in the left-centre third, face up toward frame-right, the cup against her chest. At 11–13s his second line comes OFF-SCREEN; her lips stay closed; she holds absolutely still, thumbs pressing into the rim, eyes dry. At 13–16s, silence: her eyes go from his left eye to his right eye, down to the mask in his hand, back up; she swallows. At 16–18s she asks her question. At 18–20s she waits, eyes on his mouth. HARD CUT.
SHOT 4 (20–26s) — THE MASTER again, same position as shot 1: at 21–23s @RUIZ gives his answer; at 23–26s @CLARA is already rising — left hand pushing off the seat, the cup in her right hand, the chairs creaking — while @RUIZ half-turns to the door, his right hand rising to the push plate; no touch between them. Hard end mid-rise.

DIALOGUE — only these lines are spoken, each by the named character; on-camera lines lip-synced; NO dubbing, NO voice-over, NO subtitles — the words exist only as sound. Every mouth not speaking stays closed.
[8–10s] @RUIZ (on camera, Brazilian Portuguese, São Paulo accent, low and level, each word placed like a chart reading): "Ele está estável."
[11–13s] @RUIZ (OFF-SCREEN, his shoulder in the foreground; same voice, same flat register, no softening): "Mas não acordou." — no visible mouth forms these words; @CLARA's lips stay closed.
[16–18s] @CLARA (on camera, Brazilian Portuguese, São Paulo accent, quiet and quick, a short breath taken just before): "Posso entrar?"
[21–23s] @RUIZ (on camera, Brazilian Portuguese, São Paulo accent, flat and unhurried, a procedure stated): "Só cinco minutos."
VOICE LOCK — @RUIZ: man in his mid-fifties, low baritone, slightly hoarse at the end of a night shift, even and unhurried; never theatrical, never a soft therapist voice. VOICE LOCK — @CLARA: woman of forty, mid-low register, throat dry after hours of silence, quiet, quick once she speaks; any break lives in the breath, never in a sob; never girlish or breathy. These voice identities are fixed and identical across all shots.

ACTING — @CLARA (fully invested in the tactic; the work happens in the eyes)
SCENE DIRECTION (shared, unspoken): keep it to facts and procedure — nobody says "if" in this corridor.
EVENT: a vigil changes hands — what the doctor cannot promise, he replaces with the minutes he can give.
MOTIVE: if she asks the real question she will get the real answer, and she cannot take it here, alone, at three in the morning.
GOAL: get through that door to him.
OBSTACLE: his second sentence tells her more than it says; one more question and the rest comes out.
TACTIC: hold absolutely still, take his words as facts, then ask for the one thing within reach — the door — before he can add anything; her eyes search BOTH of his for the end of the sentence he isn't saying.
MOMENT TO MOMENT: — [3–7s] she reads his face before the mask is off — [11–13s] holds still, thumbs on the rim — [13–16s] his left eye, his right eye, the mask, back up; decides not to ask — [16–18s] the question, fast, to get past the one she didn't ask — [23–26s] already rising, eyes on the door.
LIVING EYES: pupils search, settle, drift, settle again; blinks uneven and a beat late; brows, cheeks and mouth work independently, slight asymmetry. Involuntary detail: the swallow at 14–15s she must finish before she can speak. The cold door light is a small live point in each eye; a FROZEN PUPIL is wrong. Eyes stay dry.
NOT: tears, a trembling chin, a hand over her mouth, pleading, grabbing his arm, standing early, looking into the lens.

ACTING — @RUIZ (fully invested in the tactic; the work happens in the eyes)
SCENE DIRECTION (shared, unspoken): keep it to facts and procedure.
EVENT: the same vigil changing hands.
MOTIVE: he will not lie to her, and he will not take her hope apart in a corridor at night — he has given this news too many times to do either.
GOAL: give her the facts exactly, then give her the visit.
OBSTACLE: what he knows and isn't saying — and her eyes hunting for it.
TACTIC: lay the facts down flat and in order, like reading a chart, and measure how much of each lands in her; never let his face add anything to the words.
MOMENT TO MOMENT: — [3–7s] eyes on her before the mask is off: the cold cup, how long she has waited — [8–10s] the first line laid down; checks it registers — [21–23s] the answer as procedure, already turning to open the door for her.
LIVING EYES: pupils move between her two eyes and the cup, settle, move again; blinks uneven; slight asymmetry. Involuntary detail: his jaw sets once at 10–11s. A small glint in each eye on his shadow side; a FROZEN PUPIL is wrong.
NOT: a comforting smile, grave head-shaking, a sigh before the news, crouching beside her, looking into the lens.

CAMERA — quiet breathing handheld; the operator always on the south side of the CLARA–DOOR line: seated height, 4 m back for the master (shots 1 and 4); low beside her for shot 2; standing behind his left shoulder for shot 3. MOVEMENT: STAYS PUT in every shot and breathes — small tremor, a drift that arrives a beat late; no travel. OPTICS: 47° in shots 1 and 4 — natural perspective, both walls readable, the corridor receding into dimness between the two figures; 29° in shots 2 and 3 — close through lens reach, background compressed into soft bokeh; no lens drift inside a shot. FOCUS: shot 1 on @CLARA, racking to @RUIZ as the door opens; shot 2 his eyes; shot 3 her eyes, his shoulder soft. HORIZON: level. COMPOSITION: off-centre, the figures on the thirds, the dark corridor between them; nothing readable beyond 6 m. NOT: gimbal glide, dolly, push-in, zoom, orbit, tripod lock, slow motion.

GEOMETRY — a corridor 2.6 m wide running away from the camera toward a nurses' station 15 m up; four linked steel-and-plastic chairs against the LEFT wall, @CLARA in the second from the camera; the ICU swing door on the RIGHT wall directly across from her, a small vertical window at head height; @RUIZ stops 1.5 m from her, his back to the door; one lit ceiling panel 3 m up the corridor beyond them. The camera stays on the south side of the CLARA–DOOR line in every shot.

PHYSICS & MATERIAL — the coffee is cold and untouched: no steam, a dull skin on the surface, a dried brown ring inside the cup, the paper rim crimped where her thumbs have pressed for hours; the swing door is heavy, slow on its closer, then the last centimetres snap into the latch; the mask's elastic tugs his ears forward before it comes free; the linked chairs flex and creak when she shifts; rising, her knees take the weight a half-beat late. Nothing floats, nothing loops. OVER-REAL: the crimped cup, red mask pressure lines on his skin, a sweat-darkened scrub collar, her chapped lips, scuffed grey vinyl with a dull sheen, greasy finger smudges on the push plate and the door window. If any surface looks clean, smooth, plastic, CGI or rendered — WRONG.

LIGHT — MOTIVATED LIGHT ONLY, night, COLD & QUIET (KEY): SOURCE: the key is the cold white light of the ICU (~5600 K) through the door's small window, from FRAME-RIGHT; while the door is open (3–6s) a wedge of it spills across the floor to her sneakers. The corridor is in night mode: panels near the camera OFF; one panel 3 m up the corridor on, ~4000 K with a faint green cast, a top-back rim on heads and shoulders; the nurses' station desk lamp far up the corridor (~2800 K) is a small warm glow that reaches nobody. REACH: the window light falls on @CLARA's face from frame-right and rims @RUIZ's right edge; his face toward her sits in soft shadow; beyond 6 m, grey-green dimness. EXPOSURE: exposed for the faces; shadows deep but breathing, never crushed; even exposure corner to corner, NO vignette. CONTINUITY: the cold light comes from frame-right in every shot; lit sides never flip. NOT: all ceiling lights on, flat even hospital light, frontal fill, a warm key.

FILM LOOK (KEY — reproduce this exact photographic character): real 35mm film, 500-speed tungsten stock under fluorescent light, softly printed, low-key; cold white and faint fluorescent green against warm skin and one small warm lamp far away, all muted, never teal-and-orange; highlights roll off with gentle halation; shadows deep but breathing; fine moving grain, most visible in the dim corridor; real skin with pores and lines; even exposure to all four corners, NO vignette. LENS LOOK: large-format spherical lens character — round soft bokeh, shallow focus with a gentle falloff, natural perspective, soft highlight roll-off — NOT over-sharpened, NOT digital-clean, NOT HDR, NOT a render, NOT AI-CGI.
NO LENS FLARES: no flares, no light streaks, no floating bokeh orbs, no glow overlays; every light source stays small and contained.

SOUND — DIEGETIC ONLY, dirty-real: the faint even hiss of the ceiling air vent; through the ICU door, muffled monitor beeps from several beds, irregular and out of step — NOT a rhythm, NOT music; at 3s the latch clack, the beeps and a ventilator's sigh rising while the door is open, the closer's hiss and the latch at 6s; the snap of the mask elastic; his clogs squeaking once on the vinyl; the cup crinkling under her thumbs at 12s; the chairs creaking at 23s; a short hard echo on footsteps only. After his second line, three seconds of only the vent and the far beeps. NO music, NO score, NO BGM, NO instrumental, NO melody, NO ambient pad, NO drone, NO swell, NO chimes.

WORLD — a Brazilian public hospital, today: pale institutional-green walls with a scuffed bumper rail, grey vinyl floor, linked steel-and-plastic waiting chairs, a heavy pale ICU swing door with a small window and a steel push plate, an alcohol-gel dispenser; NO readable signs, NO text on any surface, NO other people.

NEGATIVE: @CLARA standing before 23s, @CLARA putting the cup down, sides swapped, the door on frame-left, crossing the line, @CLARA's lips moving during his off-screen line, extra lines, ad-libs, tears, crying, a hand on her shoulder, a hug, any touch, @RUIZ smiling or crouching, steam from the cup, nurses or other people, readable signs, text, flat even hospital light, frontal fill, music, score, ambient pad, beeping that turns into music, subtitles, captions, centred symmetrical framing, glassy stare, frozen pupils, glowing eyes, plastic skin, beauty retouching, gimbal, zoom, push-in, slow motion, lens flare, HDR glow, vignette, crushed blacks, looping motion, warped hands, extra fingers, twins, clones, watermark, wrong aspect ratio.

[ORDER: 4 shots, 3 hard cuts, 26s, quiet breathing handheld — (1, 0–7s) master wide: @CLARA seated frame-left with the cold cup, the ICU door frame-right opens, @RUIZ steps out pulling off the mask and stops before her — (2, 7–11s) @RUIZ's MCU, his first line — (3, 11–20s) @CLARA's CU over his shoulder: his second line off-screen, her lips closed, the hold, the swallow, her question — (4, 20–26s) master: his answer, she starts to rise, he turns to the door — hard end mid-rise. Invariants: she frame-left, he and the door frame-right; she stays seated with the cup until 23s; her lips closed during his off-screen line; dry eyes, no touch. Look: 35mm tungsten under fluorescent, cold light from frame-right, fine grain, no vignette. Only @RUIZ and @CLARA speak — four lines, Brazilian Portuguese. NO music, NO subtitles.]
```

```
GENERATION CARD
Model: Seedance 2.5 · Task: reference-to-video
Duration: 26s (= timeline) · Aspect: 21:9 · Resolution: draft 480p → final 1080p (2206×946) · Audio: on
Attach in this order: 1) @CLARA — identity (rosto + corpo inteiro, cardigã verde-musgo)  2) @RUIZ — identity (rosto sem máscara + corpo inteiro, scrub azul-marinho)  3) corredor_uti_noite — world (plate do corredor vazio, sem pessoas)
Notes: Faça o draft 480p primeiro e confira duas coisas: a boca da Clara fechada em "Mas não acordou" (plano 3, 11–13s) e ela sentada até 23s. Se só a boca falhar, não regenere tudo — edite os segundos: "Edit Video 1: from 11 to 13 seconds, her lips stay closed; the voice comes from the man off-screen; leave the rest of Video 1 unchanged." Aprovado o take, exporte o ÚLTIMO FRAME: ele é a @Image 1 (keyframe) da geração 1b. Sintaxe @Image N = BytePlus/fal; no Higgsfield, digite @ e escolha os uploads nesta mesma ordem.
```

---

## Geração 1b · 25s · 3 planos · 21:9

```
O QUE ACONTECE: Clara deixa o copo na cadeira e entra; pela janelinha, ela segura a mão do pai, que não reage. Ruiz olha um instante a mais do que precisava e vai embora pelo corredor.
O QUE É DITO: nada.
TEMPO: copo na cadeira, ela entra, a porta fecha — 7s · pela janelinha: ela segura a mão do pai — 8s · Ruiz na janelinha, o respiro, ele vai embora — 10s = 25s
COMO TERMINA: corte seco no meio do passo de Ruiz, de costas, se afastando no corredor; a câmera não vai atrás.
```

```
CONTRACT — Live-action photoreal film footage, 21:9, 25 seconds total, 3 shots with 2 hard cuts at 7s and 15s, quiet breathing handheld, real-time motion, no dialogue — nobody speaks. NO music, NO score, NO subtitles, NO on-screen text.

REFERENCES — each reference has ONE job:
@Image 1 — KEYFRAME FOR SHOT 1: shot 1 STARTS from this exact frame (the corridor wide: @CLARA half-risen from the chairs frame-left, the paper cup in her right hand; @RUIZ frame-right turning to the ICU door) and comes alive from it.
@Image 2 — IDENTITY of @CLARA: face, hair, hands, build, moss-green knit cardigan, grey T-shirt, jeans. 100% matches.
@Image 3 — IDENTITY of @RUIZ: face, grey stubble, hands, build, navy scrubs over a grey long-sleeve thermal, stethoscope. 100% matches.
@Image 4 — IDENTITY of @PAI: face, grey hair, thin build, hands, hospital gown. 100% matches.
@Image 5 — WORLD: the ICU bay — bed, rails, monitor arm, IV pole, pale walls; the room seen through the door window in shot 2, not its light or lens.
REFERENCE SCOPE: @Image 2, @Image 3 and @Image 4 supply faces, hair, hands, build and wardrobe ONLY — IGNORE their backdrops, lighting direction, exposure and colour grade. Shot 1 inherits the keyframe's light, grade and skin texture; shots 2 and 3 continue that exact look.

WHO IS WHO — READ FIRST, ABSOLUTE:
@CLARA (40, slim, olive skin, dark circles, dark-brown hair in a loose claw clip, no makeup; oversized moss-green cardigan, grey T-shirt, jeans, white sneakers) — the DAUGHTER: sets the cup on the chair, goes into the ICU, holds her father's hand; NEVER speaks, NEVER cries aloud, NEVER looks toward the door window or the lens; frame-LEFT in the corridor until she crosses to the door.
@RUIZ (55, heavy-set, short grey hair, grey-white stubble, red mask lines on his nose and cheekbones; navy scrubs over a grey thermal, stethoscope; the crumpled pale-blue mask in his LEFT hand throughout) — the DOCTOR: holds the door for her, stays in the corridor, watches through the small window, leaves up the corridor AWAY from the camera; NEVER enters the room, NEVER walks toward the camera; owns frame-RIGHT, at the door.
@PAI (78, thin, grey hair flattened on the pillow, white stubble, faded hospital gown, a clear oxygen mask over nose and mouth, an IV cannula taped on the back of his hand, a pulse-oximeter clip on one finger) — the FATHER: lies unconscious on his back; NEVER opens his eyes, NEVER moves, NEVER grips back; seen only through the door window.
FACES: each face exists once; no nurse, no other patient, nobody else; no twins, no clones.
CONTACT: the only touch is @CLARA's two hands holding @PAI's hand in shot 2. In the corridor nobody touches anyone — she passes @RUIZ without contact.

SCENE — 3 a.m., the corridor outside the ICU of a Brazilian public hospital. The doctor has just granted @CLARA five minutes with her unconscious father; she is already rising from the steel chairs, the paper cup of cold coffee still in her hand.
THE SOUL OF THE SCENE (play it, never explain it): she goes in to be there in case he wakes. The doctor watches long enough to see her find the hand — and leaves before she can look up, so the minutes are hers, unwatched, and nobody has to say how many more there will be.

ABSOLUTE LOCKS — break one and the take is WRONG, regenerate:
1. @PAI never wakes: eyes closed in every frame, lids still, his hand limp dead weight; the only movement is the oxygen mask misting with each slow breath. WRONG if his eyes open, his lids flutter or his fingers move.
2. Shot 2 is seen ONLY THROUGH the small window of the ICU door, from the corridor — the dark window frame soft along the frame-left edge, glass between lens and room. WRONG if the camera is inside the ICU.
3. @RUIZ stays in the corridor; in shot 3 he walks AWAY from the camera up the corridor while the camera stays put. WRONG if he enters the room or walks toward the camera.
4. One touch only — @CLARA's hands around her father's hand. WRONG if anyone else touches, hugs or holds.
5. Nobody speaks, nothing is heard from inside the room, no music, no subtitles.

TIMELINE — 3 shots, 2 hard cuts; cuts only at the specified points, the camera adds no cuts of its own:
SHOT 1 (0–7s) — THE MASTER: WS, 47°, camera at seated eye height, 4 m south of the CHAIRS–DOOR line, STAYS PUT with one late pan: from the keyframe, @CLARA is half-risen frame-left; at 0–2s she straightens and sets the cup on the seat behind her without looking — cold coffee slops over the rim and runs down the paper; at 2–5s she crosses frame-left to frame-right in three steps while @RUIZ pushes the swing door open with his RIGHT palm flat on the push plate and stands against it, the mask in his LEFT hand; she goes through without touching him; at 5–7s he lets the door go — it swings shut on its closer and snaps into the latch; @RUIZ stays in the corridor, frame-right. HARD CUT.
SHOT 2 (7–15s) — THROUGH THE WINDOW: MS, 29°, camera in the corridor at 1.6 m, lens 50 cm from the glass of the door's small window, the dark window frame soft along the frame-left edge, a faint smudge on the glass; 3.5 m beyond, the bed runs across the frame, @PAI on his back, head on the pillow at frame-RIGHT, oxygen mask on, eyes closed; @CLARA already standing on the far side of the bed at his chest, looking DOWN at him. At 7–10s she slides both hands under his hand and lifts it, careful of the taped cannula; at 10–13s she holds it in both of hers at the edge of the mattress, her thumb crossing his knuckles once, eyes on his closed lids; at 13–15s she bends lower, her face 40 cm above his; his hand stays limp, his eyes stay closed; the mask mists and clears. HARD CUT.
SHOT 3 (15–25s) — THE LAST LOOK: MCU @RUIZ, 29°, camera in the corridor at 1.6 m, 3 m south of him, 1 m out from the right wall, STAYS PUT: @RUIZ at the ICU door in the frame-right third, in right profile, face to the small window, its cold light on his face from frame-right; the mask in his LEFT hand at his side; behind him, frame-left, the corridor recedes soft to the small warm glow of the nurses' station. At 15–20s he watches through the glass; at 20–21s a long breath out through the nose; at 21–25s he turns to his left, away from the window, and walks AWAY from the camera up the corridor, under the one lit ceiling panel, growing smaller; the camera does not follow. Hard end mid-stride, his back to the camera, 6 m away.

ACTING — @CLARA (fully invested in the tactic; the work happens in the eyes and the hands)
SCENE DIRECTION (shared, unspoken): use the minutes; don't let them become a goodbye.
EVENT: a vigil changes hands — she takes over the watch her father can't keep.
MOTIVE: if he wakes in these minutes, the first thing he feels must be her hand.
GOAL: get her warmth into his hand. OBSTACLE: the hand does not answer.
TACTIC: warm his hand and watch his closed lids for a flicker — lids, fingers, lids again.
MOMENT TO MOMENT: — [0–5s] the cup set down without a look, eyes on the door, past @RUIZ without looking at him — [7–13s] lifts and holds his hand, thumb across the knuckles once, eyes on his lids — [13–15s] bends lower, still watching the lids.
LIVING EYES: pupils move between his lids and his fingers, settle, move again; blinks uneven and late; slight asymmetry. Involuntary detail: her lips press together once when his hand stays limp. The bed lamp is a small live point in her eyes; a FROZEN PUPIL is wrong.
NOT: crying aloud, sobbing, collapsing onto the bed, kissing his face, talking to him, looking toward the window or into the lens.

ACTING — @RUIZ (fully invested in the tactic; the work happens in the eyes)
SCENE DIRECTION (shared, unspoken): let her have the minutes.
EVENT: a vigil changes hands — he hands the watch to her and steps out of it.
MOTIVE: he knows what a patient still not awake at this point usually means, and that these may be the minutes she keeps.
GOAL: see that she has found him, then leave her alone with him.
OBSTACLE: the part of him that wants to stay and keep watching over both of them.
TACTIC: check from outside like a doctor — her hands, the monitor above the bed, her hands again — and withdraw before she can look up and catch him watching.
MOMENT TO MOMENT: — [2–7s] holds the door, eyes on her as she passes, then on the closing door — [15–20s] at the window: hands, monitor, hands — a check that lasts a beat too long — [20–21s] the long breath out — [21–25s] turns and goes, without looking back.
LIVING EYES: pupils travel, settle, drift; blinks uneven and late; slight asymmetry. Involuntary detail: the long breath out through the nose at 20s. The window light is a small live point in his eye; a FROZEN PUPIL is wrong.
NOT: tears, a hand pressed to the glass, shaking his head, checking his watch, looking back, looking into the lens.

ACTING — @PAI: no task — he is unconscious. Eyes closed in every frame, lids still; the chest rises slowly under the gown; the oxygen mask mists faintly on each exhale; his hand is dead weight in hers. NOT: opening his eyes, fluttering lids, fingers moving, gripping back, turning his head.

CAMERA — quiet breathing handheld; the operator stays in the corridor for all three shots, on the south side of the CHAIRS–DOOR line. MOVEMENT: STAYS PUT in every shot and breathes — small tremor, a drift that arrives a beat late; in shot 1 one late pan with her to the door, then it settles; it never travels, never enters the room, never follows him. OPTICS: 47° in shot 1 — natural perspective, both walls readable; 29° in shots 2 and 3 — close through lens reach, background compressed into soft bokeh, his receding figure kept in the same long-lens space; no lens drift inside a shot. FOCUS: shot 1 on @CLARA; shot 2 on her hands and his face, the window frame soft; shot 3 on his eye, then on his back a beat late. HORIZON: level. NOT: the camera inside the ICU, the camera following him, gimbal glide, dolly, push-in, zoom, orbit, tripod lock, slow motion.

GEOMETRY — the corridor is 2.6 m wide and runs away from the camera toward a nurses' station 15 m up; linked chairs against the LEFT wall; the ICU swing door on the RIGHT wall across from them, its small window at 1.5–1.8 m. Inside, the bed stands 3.5 m beyond the door, long side facing it, the head of the bed at frame-right under the monitor arm; @CLARA on the far side of the bed at his chest. The camera stays on the south side of the CHAIRS–DOOR line in shots 1 and 3; in shot 2 it looks straight through the window.

PHYSICS & MATERIAL — the cup is full and cold, set down a little too fast: coffee slops over the crimped rim and a brown run crawls down the side; the swing door is heavy — his flat palm takes its weight, the closer pulls it back slowly and the last centimetres snap into the latch; @PAI's hand is dead weight — it sags between her fingers, his fingers curl loosely, the IV line across the back of it; the mattress dips under her forearms; his hand START limp on the sheet / DURING lifted and held, still limp / END still limp in hers — it never grips back. Nothing floats, nothing loops. OVER-REAL: the coffee run on the crimped cup, paper tape and a bruise around the cannula on his thin spotted hand, white stubble around the oxygen mask, worn plastic bed rails, the smudge on the door window, the red mask lines on @RUIZ's face. If any surface looks clean, smooth, plastic, CGI or rendered — WRONG.

LIGHT — MOTIVATED LIGHT ONLY, night, COLD & QUIET (KEY): SOURCE: in the corridor the key is the cold white light of the ICU (~5600 K) through the door's small window — and the doorway while it is open — from FRAME-RIGHT; night mode: panels near the camera OFF, one panel 3 m up the corridor on, ~4000 K, faint green, rimming heads; the nurses' station desk lamp far up the corridor (~2800 K) a small warm glow that reaches nobody. Inside the ICU (shot 2) the only key is the dimmed lamp above the head of the bed, frame-right, cold white ~5000 K, on his face, the pillow and her hands; the monitor soft and out of focus, a faint green spill on the rail; beyond the bed, blue-grey dimness. REACH: in shot 3 the window light lies on @RUIZ's face from frame-right; the far side of his face and the corridor behind him in soft shadow. EXPOSURE: exposed for the faces; shadows deep but breathing, never crushed; even exposure corner to corner, NO vignette. CONTINUITY: the key comes from frame-right in every shot; lit sides never flip. NOT: all ceiling lights on, flat even light, frontal fill, a warm key, reflections on the glass that hide the room.

FILM LOOK (KEY — reproduce this exact photographic character): real 35mm film, 500-speed tungsten stock under fluorescent light, softly printed, low-key; cold white and faint fluorescent green against warm skin and one small warm lamp far away, all muted, never teal-and-orange; highlights roll off with gentle halation; shadows deep but breathing; fine moving grain, most visible in the dim corridor; real skin with pores and lines; even exposure to all four corners, NO vignette. LENS LOOK: large-format spherical lens character — round soft bokeh, shallow focus with a gentle falloff, natural perspective, soft highlight roll-off — NOT over-sharpened, NOT digital-clean, NOT HDR, NOT a render, NOT AI-CGI.
NO LENS FLARES: no flares, no light streaks, no floating bokeh orbs, no glow overlays; every light source stays small and contained.

SOUND — DIEGETIC ONLY, dirty-real: the faint even hiss of the ceiling air vent; through the ICU door, muffled monitor beeps from several beds, irregular and out of step — NOT a rhythm, NOT music; at 1s the soft tap of the cup on the seat; her sneakers squeaking on the vinyl; the push plate thumping under his palm, the beeps and a ventilator's sigh rising while the door is open, the closer's hiss and the latch at 6s; in shot 2 nothing from inside the room but the muffled beeps — no voice; in shot 3 his clogs on the vinyl, receding with a short hard echo; after 23s only the vent and the far beeps. NO music, NO score, NO BGM, NO instrumental, NO melody, NO ambient pad, NO drone, NO swell, NO chimes.

WORLD — a Brazilian public hospital, today: pale institutional-green corridor walls with a scuffed bumper rail, grey vinyl floor, linked steel-and-plastic waiting chairs, a heavy pale ICU swing door with a small window and a steel push plate; the ICU bay: a bed with plastic rails, a monitor on an arm, an IV pole with bags, a pale curtain half drawn; NO readable signs, NO readable monitor numbers, NO text on any surface, NO other people.

NEGATIVE: @PAI opening his eyes, fluttering lids, fingers moving, gripping back, any sign of waking, the camera inside the ICU, shot 2 without the glass and window frame, @RUIZ entering the room, @RUIZ walking toward the camera, the camera following him, @RUIZ looking back, @CLARA looking at the window or into the lens, @CLARA speaking, a sob, collapsing over the bed, a hug, any touch in the corridor, a hand pressed on the glass, nurses, other patients, readable monitor numbers, readable text, sides swapped, the door on frame-left, flat even hospital light, music, score, ambient pad, beeping that turns into music, subtitles, captions, centred symmetrical framing, glassy stare, frozen pupils, glowing eyes, plastic skin, beauty retouching, gimbal, zoom, slow motion, lens flare, HDR glow, vignette, crushed blacks, looping motion, warped hands, extra fingers, twins, clones, watermark, wrong aspect ratio.

[ORDER: 3 shots, 2 hard cuts, 25s, quiet breathing handheld — (1, 0–7s) master wide from the keyframe: @CLARA sets the cold cup on the chair, crosses frame-left to frame-right, @RUIZ holds the swing door with his right palm, she goes in without touching him, the door closes — (2, 7–15s) through the small door window: she lifts her father's limp hand in both of hers and watches his closed lids; he does not respond — (3, 15–25s) @RUIZ's MCU at the window, cold light from frame-right, he watches a beat too long, breathes out, turns and walks away up the corridor while the camera stays — hard end mid-stride. Invariants: @PAI's eyes closed and hand limp; shot 2 only through the window; @RUIZ never enters and leaves away from the camera; one touch only; nobody speaks. Look: 35mm tungsten under fluorescent, cold light from frame-right, fine grain, no vignette. NO dialogue, NO music, NO subtitles.]
```

```
GENERATION CARD
Model: Seedance 2.5 · Task: reference-to-video (keyframe no plano 1)
Duration: 25s (= timeline) · Aspect: 21:9 · Resolution: draft 480p → final 1080p (2206×946) · Audio: on
Attach in this order: 1) último frame aprovado da 1a — keyframe do plano 1  2) @CLARA — identity  3) @RUIZ — identity  4) @PAI — identity (deitado, olhos fechados, máscara de oxigênio)  5) uti_leito_noite — world (o leito visto da porta, sem pessoas)
Notes: O risco nº 1 é o pai "acordar" no plano 2 (pálpebra tremendo, dedos apertando de volta) — é a primeira coisa a checar no draft; o nº 2 é Ruiz andando em direção à câmera no plano 3. Se a plataforma travar o aspecto em "adaptive" ao usar o keyframe como first frame, mande-o como imagem de referência comum — o texto já o amarra ao plano 1 e o frame da 1a já é 21:9. Sem o keyframe: apague a linha da @Image 1 e renumere as demais.
```

---

## Antes de gerar

As referências ainda não existem. São três identidades (@CLARA, @RUIZ, @PAI) e dois plates: o corredor vazio à noite e o leito da UTI visto da porta.

A ordem de produção é esta:
1. 1a em draft, depois 1a final.
2. Exporte o último frame da 1a.
3. Use esse frame como keyframe do plano 1 da 1b.
4. 1b em draft, depois 1b final.

Dá para rodar sem referências, como text-to-video: é só apagar o bloco REFERENCES. Nesse caso, o rosto da Clara e o do Ruiz vão mudar entre a 1a e a 1b.

Posso escrever os prompts de imagem desses cinco assets (rosto, corpo inteiro e os plates).
