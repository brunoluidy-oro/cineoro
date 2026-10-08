Decupei a cena em **5 prompts de 15s (1a–1e)**, todos em 21:9. O shotlist editável está em `/home/user/cineoro/evals/iteration-1/hospital-shotlist/old_skill/outputs/shotlist.html`: a caixa de seleção salva o progresso sozinha e cada prompt tem botão de copiar.

**Referências.** Como você não definiu tags, usei a ordem de carregamento das imagens, que muda conforme quem está em quadro:
- **1a, 1b e 1c:** `@image1` = Clara, `@image2` = Dr. Ruiz.
- **1d:** `@image1` = Clara. O pai vai só descrito em texto. Se tiver referência dele, me manda que eu incluo como `@image2`.
- **1e:** `@image1` = Dr. Ruiz. Carregue só a imagem dele.

Deixe o formato em 21:9 também na interface. O prompt já pede, mas quem decide é a configuração.

## Shotlist — INT. HOSPITAL — CORREDOR DA UTI — NOITE

| Prompt | Tempo | Plano · lente | O que acontece |
|---|---|---|---|
| 1a | 0–3,5s | PLANO DETALHE (ECU) · 12° | O café frio nas mãos de Clara — sem vapor, marca seca na borda. |
| 1a | 3,5–15s | PLANO GERAL (WS) · 47° · fixo | A espera. A porta abre, Ruiz sai tirando a máscara, Clara se levanta. Silêncio, um metro entre os dois. |
| 1b | 0–3,5s | PLANO PRÓXIMO (MCU) · 29° · sobre o ombro de Clara | Ruiz: “Ele está estável.” |
| 1b | 3,5–15s | PRIMEIRÍSSIMO PLANO (CU) · 18° · contraplano | “Mas não acordou.” cai no rosto de Clara; ela segura 7s; “Posso entrar?” |
| 1c | 0–6s | PLANO PRÓXIMO (MCU) · 29° · sobre o ombro de Clara | Ruiz: “Só cinco minutos.” Ela assente; ele sai do caminho. |
| 1c | 6–15s | PLANO GERAL (WS) · 47° · fixo | Clara deixa o copo na cadeira e entra. A porta fecha. Ruiz fica sozinho diante dela. |
| 1d | 0–15s | PLANO ÚNICO pela janelinha · 47° · travelling in lento | Quadro dentro do quadro: Clara contorna a cama, senta e segura a mão do pai. A câmera não entra no quarto. |
| 1e | 0–8,5s | PRIMEIRÍSSIMO PLANO (CU) · 18° · perfil | Ruiz na janelinha: monitor, mãos, monitor, mãos — e os olhos ficam nas mãos. |
| 1e | 8,5–15s | PLANO GERAL (WS) · 47° · fixo | Ele vai embora pelo corredor. Ficam a janelinha acesa e o copo frio na cadeira. |

A câmera nunca entra no quarto. O pai só aparece pela janelinha, do ponto de vista do corredor.

## Prompts completos

### Prompt 1a · 15s · refs: @image1 Clara · @image2 Ruiz

```
SCENE CONTEXT
Night, a hospital ICU corridor. CLARA, 40, sits alone on a plastic chair directly opposite the ICU door, holding a paper cup of coffee that went cold hours ago. The door swings open and DR. RUIZ, 55, steps out pulling off his surgical mask; Clara stands, and the two face each other across one meter of corridor before a word is spoken.

ACTIVE REFERENCES
@image1 — CLARA: woman, 40, hours without sleep, hair loosely tied back, dark navy wool coat unbuttoned over a grey knit sweater; holds a white paper coffee cup with a brown cardboard sleeve and no lid in both hands. 100% matches the reference.
@image2 — DR. RUIZ: man, 55, ICU physician at the end of a night shift, teal scrubs, light-blue disposable surgical mask with elastic ear loops covering nose and mouth as he steps out. 100% matches the reference.

LOCATION MAP
Corridor 2.4 meters wide, pale grey vinyl floor with a soft sheen, pale green-grey walls. Screen-left wall: the ICU door — a heavy pale-grey swing door 1.2 meters wide that opens both ways, hinged on its edge deeper in the corridor, with one small square vision panel of clear glass, 30 × 30 centimeters, at eye height 1.5 meters from the floor; the panel glows warm amber from the lamp in the room behind it. Screen-right wall: a row of four grey molded-plastic chairs on a steel beam, backs against the wall, directly opposite the door, 2.4 meters across from it. Ceiling: rectangular fluorescent panels every 3 meters; night mode keeps every second panel dark, so the corridor recedes in alternating pools of cool light and dim gaps toward a dark far end 25 meters away, where a small green emergency light glows. The camera stands in the corridor 4 meters short of the door–chair line, looking down the corridor's length. The corridor is otherwise empty.

FIRST FRAME / BLOCKING
Frame one: Clara's two hands wrapped around the paper cup, resting on her left knee — hands and cup fill the frame.
From 3.5s: Clara sits on the chair directly facing the door, in the screen-right third of frame, body and face in profile toward screen-left, eyes locked on the door's vision panel, cup held in both hands on her lap. The door is closed, screen-left midground, 2.4 meters across from her. Ruiz steps out of the door at 6.5s and stops 1 meter in front of Clara, screen-left of her, body facing screen-right, eyes on her. From then on: Clara screen-right facing screen-left, Ruiz screen-left facing screen-right, the door with its amber panel directly behind Ruiz. Composition: wide 21:9 frame, the two figures at center, the corridor's receding pools of light filling the depth behind them.

FORMAT MODE
Timed multishot, two shots. Cuts only at the specified point, the camera does not cut on its own.
0.0s to 3.5s — INSERT: the cold coffee in Clara's hands.
3.5s HARD CUT
3.5s to 15.0s — one continuous wide shot: the wait, the door, Ruiz, Clara standing.

OPTICS
Shot 1 (0.0–3.5s): ECU, 12° diagonal field of view, tele-detail lens character, camera 2 meters from the cup, close framing through lens reach; razor-thin focus on the coffee surface and the rim, her fingers falling softly out of focus, background dissolved into a dark green-grey wash. 12° held, no drift mid-segment.
Shot 2 (3.5–15.0s): WS, 47° diagonal field of view, standard normal lens character, camera 4 meters from the door–chair line, natural human-eye perspective, zero obvious distortion, natural body proportions, both walls and the corridor depth readable, comfortable depth of field with the far corridor gently soft. 47° held, no drift mid-segment; no extreme wide distortion, no telephoto compression.

CAMERA
Shot 1: locked off at knee height, looking down into the cup at 30°.
Shot 2: tripod-locked at seated eye height, 1.2 meters, on the corridor's center line, looking down its length; the frame holds perfectly still for the whole shot — the stillness is the wait. Focus holds on the Clara–door plane. Tonal character: wide latitude, the amber panel's highlight rolling off softly, deep shadows keeping their detail.

ACTION
0.0–3.5s: the coffee surface lies flat, matte and still, cold, no steam rising; a dry brown ring line marks the inside of the cup 1 centimeter above the liquid; Clara's right thumb slides slowly along the rim once and stops.
3.5–6.5s: Clara sits motionless facing the door, cup on her lap; at 5.5s a shadow passes behind the vision panel, dimming the amber glow for half a second.
6.5–8.0s: the door swings open into the corridor, its leaf opening behind Ruiz on the side away from the camera; Ruiz steps out at 3 km/h, already hooking both index fingers under the mask's ear loops.
8.0–9.5s: Ruiz lifts the loops off both ears and draws the mask down off his face; Clara rises from the chair in one movement, the cup held level in both hands at waist height.
9.0–11.0s: behind Ruiz the door swings shut on its closer and latches; the amber panel settles behind his head.
9.5–11.0s: Ruiz crosses 1.4 meters and stops 1 meter in front of Clara, folding the mask once and closing it in his right fist.
11.0–15.0s: they stand facing each other in silence, one meter apart.

ACTING TASK — CLARA (she is fully invested in her tactic; the work happens in her eyes):
SCENE DIRECTION (shared, unspoken): keep it to what can be done right now — facts, permission, minutes; nobody puts the open question into words.
MOTIVE (her fuel): she wants to walk into that room steady — her father should feel a calm hand, not a frightened one.
GOAL: get to his side the moment the door allows it.
OBSTACLE: the news she hasn't heard yet; if the fear reaches her face out here, she arrives at the bed in pieces.
TACTIC: she watches the door like a sentry, then reads the doctor's face for the verdict before he can say it.
Moment to moment:
— the wait — her eyes hold the vision panel; the shadow crosses the glass and her eyes sharpen on it, measuring whether it is coming toward the door.
— the door opens — her eyes go straight to Ruiz's eyes, then to his mouth as the mask comes down, hunting there for the verdict first.
— the silence — she checks both his eyes, one then the other, and holds them, waiting.
(Safety: gaze always engaged in the task — never a frozen, glassy, unfocused stare; natural blink cadence, she blinks now and then to moisten her eyes.)

ACTING TASK — DR. RUIZ (he is fully invested in his tactic; the work happens in his eyes):
SCENE DIRECTION (shared, unspoken): keep it to what can be done right now — facts, permission, minutes; nobody puts the open question into words.
MOTIVE (his fuel): thirty years of night shifts taught him that exact words are the only kindness that holds; a promise he cannot keep costs the family more later.
GOAL: give her the true facts with no promise and no verdict, and keep the unit's rule.
OBSTACLE: her eyes — if she finds worry in his face she will ask the one question he cannot answer.
TACTIC: he finds her before he reaches her and measures what she can carry, keeping his own face as level as a chart.
Moment to moment:
— stepping out — his eyes find Clara at once and take her in: the cup, the coat, the way she rises.
— the mask comes down — he holds her eyes steadily, giving her nothing to read yet.
— the silence — he checks both her eyes, choosing his first word.
(Safety: gaze always engaged in the task — never a frozen, glassy, unfocused stare; natural blink cadence, he blinks now and then to moisten his eyes.)

PERFORMANCE
Clara: real skin with fine pores, soft grey shadow under the eyes from a sleepless night, dry lips, no makeup sheen; small amber catch-lights from the vision panel in her eyes. Ruiz: end-of-shift stubble shadow; once the mask is off, faint red pressure lines from its edge across the bridge of his nose and his cheeks, and behind his ears from the loops. Slow, visible breathing in both.

PHYSICS
The paper cup is light; the cold coffee tilts with it as Clara stands and settles level without spilling. Her wool coat swings and settles a beat after she rises. The door has real mass and closer resistance: it decelerates, swings shut and latches with a small bounce. Ruiz walks heel to toe on soft-soled clogs, weight transferring and settling as he stops. The elastic loops stretch and release.

LIGHTING
Priority lock. The ceiling panel directly above the door–chair line is dark; the nearest lit panel hangs 2 meters deeper in the corridor, beyond the two of them, throwing cool 4000K top-back light that rims hair and shoulders. The faces are keyed only by the soft warm glow of the vision panel from screen-left (a 3200K tungsten lamp inside the room) and a low bounce off the pale floor; camera-facing sides fall into soft shadow. White balance fixed at 4000K, so the corridor reads cool green-grey and the vision panel is the only warm amber surface in frame — the color of the room where her father lies. Exposure set for the amber panel and the rims; faces low-key with detail held in the shadows; no flat front light.

WARDROBE
Clara: dark navy wool coat, unbuttoned, creased from hours in the chair, over a grey knit sweater; dark trousers. Ruiz: teal short-sleeved scrubs, slightly rumpled; light-blue disposable mask until he removes it.

AUDIO
Low hum of the fluorescent ballasts; a muffled monitor beep behind the door at 70 per minute; the door's latch click and the hiss of its closer; soft footsteps on vinyl; the faint snap of the elastic loops. No dialogue — both mouths stay closed. No music.

STYLE
Photoreal, quiet observational hospital drama, restrained contrast with deep detailed shadows, natural skin tones, fine film grain, real-time motion.

OUTPUT SETTINGS
21:9 widescreen frame (2.33:1), composition built for the full width; 15 seconds; real-time 24 fps in both shots.

POSITIVE LOCKS
— Frame one already shows Clara's hands and the cup; from 3.5s Clara is in frame, seated, eyes on the door.
— Exactly two people appear: Clara and Ruiz; the corridor stays otherwise empty.
— Clara stays screen-right facing screen-left; Ruiz stays screen-left facing screen-right, the door behind him.
— The cup stays in both of Clara's hands for the whole clip; the folded mask stays in Ruiz's right fist once removed.
— The vision panel glows warm amber in every frame of shot 2.
— Silence throughout: no spoken words, no subtitles, no music.
— Cuts only at 3.5s; the camera does not cut on its own.
```

### Prompt 1b · 15s · refs: @image1 Clara · @image2 Ruiz

```
SCENE CONTEXT
Night, a hospital ICU corridor. DR. RUIZ, 55, just out of the ICU with his removed mask folded in his fist, stands one meter in front of CLARA, 40, who holds a cold paper cup of coffee in both hands. He gives her the news about her father in two short lines — stable, but not awake — and she answers with one question. Ruiz stands with his back to the ICU door; Clara stands with her back to the row of waiting chairs.

ACTIVE REFERENCES
@image1 — CLARA: woman, 40, hours without sleep, hair loosely tied back, dark navy wool coat unbuttoned over a grey knit sweater; holds a white paper coffee cup with a brown cardboard sleeve and no lid in both hands at waist height; voice low, tired, steady alto, Brazilian Portuguese. 100% matches the reference.
@image2 — DR. RUIZ: man, 55, ICU physician at the end of a night shift, teal scrubs, a light-blue surgical mask folded in his right fist, faint red pressure lines from the mask across his nose and cheeks; voice low, even, unhurried baritone, Brazilian Portuguese. 100% matches the reference.

LOCATION MAP
Corridor 2.4 meters wide, pale grey vinyl floor, pale green-grey walls. On Ruiz's side: the closed ICU door — heavy, pale grey, 1.2 meters wide, with one small square clear-glass vision panel, 30 × 30 centimeters, at eye height, glowing warm amber from the lamp in the room behind it. On Clara's side: a row of four grey molded-plastic chairs on a steel beam, backs against the wall. Ceiling fluorescent panels every 3 meters, every second one dark for night mode; the corridor recedes into alternating pools of cool light. Both camera positions stand down the corridor's length on the same side of the Clara–Ruiz eye line.

FIRST FRAME / BLOCKING
Ruiz stands 0.6 meters in front of the closed door, body facing screen-right, eyes on Clara. Clara stands 0.8 meters in front of the chairs, body facing screen-left, eyes on Ruiz. One meter between them.
Frame one (over Clara's shoulder onto Ruiz): Clara's left shoulder and the back of her head as a soft dark shape in the screen-right foreground; Ruiz in 3/4 view, screen-left of center, sharp; the amber vision panel glowing in the door behind his shoulder.
From 3.5s (reverse, over Ruiz's shoulder onto Clara): Ruiz's right shoulder as a soft dark shape at the screen-left edge; Clara in 3/4 front view, screen-right of center, face filling the frame's height from chin to hairline plus a little air; the grey chairs and wall dissolved behind her.

FORMAT MODE
Timed multishot, two shots. Cuts only at the specified point, the camera does not cut on its own.
0.0s to 3.5s — over-the-shoulder on Ruiz: he gives the first line.
3.5s REVERSE CUT
3.5s to 15.0s — over-the-shoulder close-up on Clara: his second line lands on her face, she holds, she asks.

OPTICS
Shot 1 (0.0–3.5s): MCU on Ruiz, 29° diagonal field of view, short telephoto portrait lens character, camera 4 meters away; close framing achieved through lens reach, not proximity; Ruiz razor-sharp, Clara's shoulder a soft dark shape, the door and corridor compressed close behind him into creamy bokeh with the amber panel a warm blur. 29° held, no drift mid-segment.
Shot 2 (3.5–15.0s): CU on Clara, 18° diagonal field of view, classic telephoto lens character, camera 3.5 meters away down the corridor; strong background compression, razor-thin focus on her eyes, Ruiz's shoulder melting into dark soft bokeh at frame-left, the chairs and wall dissolved into a soft green-grey wash behind her; the image feels observed from a short distance. 18° held, no drift mid-segment. No part of this shot becomes wide-angle or normal-lens coverage.

CAMERA
Both shots at standing eye height, 1.6 meters, both from the same side of the eye line, down the corridor's length. Shot 1: locked, with the faint organic settle of an operator's slow breathing. Shot 2: locked on Clara for the full 11.5 seconds with the same faint organic settle; the frame holds her and waits with her. Focus stays on the near eye of whoever faces camera. Tonal character: wide latitude, warm highlights rolling off softly, shadows holding detail.

ACTION
0.0–0.5s: Ruiz holds Clara's eyes.
0.5–2.0s: Ruiz says: "Ele está estável."
2.0–3.5s: he holds her eyes; in the foreground Clara's shoulder drops 1 centimeter as her breath goes out.
3.5s REVERSE CUT to Clara.
3.8–5.3s: Ruiz, his soft shoulder in the foreground, says: "Mas não acordou." Clara's lips stay closed while he speaks.
5.3–12.3s: Clara stands still and holds, the cup in both hands at waist height below frame; the only movement is her breathing and her eyes.
12.3–13.6s: Clara says: "Posso entrar?"
13.6–15.0s: she waits for the answer, eyes on Ruiz, lips closed.

ACTING TASK — CLARA (she is fully invested in her tactic; the work happens in her eyes):
SCENE DIRECTION (shared, unspoken): keep it to what can be done right now — facts, permission, minutes; nobody puts the open question into words.
MOTIVE (her fuel): she wants to walk into that room steady — her father should feel a calm hand, not a frightened one.
GOAL: get to his side, now, before anything else can be said.
OBSTACLE: "não acordou" presses behind every second; one question about it and she would be asking for a verdict she cannot carry into the room.
TACTIC: she reads Ruiz for what he is not saying while asking only for the practical thing — her eyes check both of his for a hidden worse answer, go to the amber panel over his shoulder, measuring the distance to her father, and come back to him for permission.
Moment to moment:
— "Ele está estável." — she takes the word in, checking his eyes: is that all of it?
— "Mas não acordou." — her eyes stay on his, searching one eye then the other for the part he hasn't said.
— the silence — she finds nothing more there; her eyes go to the amber panel behind him, measure it, and come back to him.
— "Posso entrar?" — she asks him straight, eyes holding his for the yes.
(Safety: gaze always engaged in the task — never a frozen, glassy, unfocused stare; natural blink cadence, she blinks now and then to moisten her eyes.)

ACTING TASK — DR. RUIZ (he is fully invested in his tactic; the work happens in his eyes):
SCENE DIRECTION (shared, unspoken): keep it to what can be done right now — facts, permission, minutes; nobody puts the open question into words.
MOTIVE (his fuel): thirty years of night shifts taught him that exact words are the only kindness that holds; a promise he cannot keep costs the family more later.
GOAL: give her the true facts with no promise and no verdict.
OBSTACLE: her eyes — if she finds worry in his face she will ask the one question he cannot answer.
TACTIC: he places each fact and checks both her eyes to see it land and whether the next question is coming, his own face as level as a chart.
Moment to moment:
— "Ele está estável." — he places it, then watches her take it, one eye then the other.
— "Mas não acordou." — he gives the second fact at the same weight as the first, holding her eyes so she can see he is hiding nothing worse.
— the silence — he waits for the question he cannot answer, ready to meet it.
— "Posso entrar?" — he registers that it is the question he can answer.
(Safety: gaze always engaged in the task — never a frozen, glassy, unfocused stare; natural blink cadence, he blinks now and then to moisten his eyes.)

PERFORMANCE
Clara's close-up: pore-level skin, soft grey shadow under the eyes, dry lips, no makeup sheen; a faint capillary flush rising at the rims of her eyes after the second line while her eyes stay clear and dry; small amber catch-lights from the vision panel in both eyes; visible slow breath at the nostrils. Ruiz: stubble shadow, the red mask lines across nose and cheeks, steady breathing.

PHYSICS
Bodies stay planted, weight settled on both feet; every small shift has mass. Clara's coat hangs with real wool weight and lifts slightly with each breath. Her breath after "Ele está estável" visibly leaves her shoulders.

LIGHTING
Priority lock. The vision panel behind Ruiz is a soft warm amber source (3200K tungsten lamp inside the room) at head height: it rims the back of his head and shoulder in warm light and falls on Clara's face from screen-left as her soft key. The nearest lit ceiling panel hangs 2 meters deeper in the corridor beyond them, throwing cool 4000K top-back light over both heads. Ruiz's face is lit by soft cool top light only, low-key. White balance fixed at 4000K: cool green-grey corridor, warm amber only where the room's light reaches. Exposure set for Clara's lit eye; the rest falls into soft shadow; no flat front light.

WARDROBE
Clara: dark navy wool coat, unbuttoned, creased, over a grey knit sweater. Ruiz: teal short-sleeved scrubs, slightly rumpled.

AUDIO
Only the three scripted lines, in Brazilian Portuguese, spoken in this order: Ruiz "Ele está estável." — Ruiz "Mas não acordou." — Clara "Posso entrar?" Under them: the low hum of the fluorescent ballasts and a muffled monitor beep behind the door at 70 per minute. No other words, no music.

STYLE
Photoreal, quiet observational hospital drama, restrained contrast with deep detailed shadows, natural skin tones, fine film grain, real-time motion.

OUTPUT SETTINGS
21:9 widescreen frame (2.33:1), composition built for the full width; 15 seconds; real-time 24 fps in both shots.

POSITIVE LOCKS
— Frame one already shows Ruiz sharp and Clara's shoulder in the foreground.
— Exactly two people: Clara and Ruiz; the corridor stays otherwise empty.
— Screen direction holds across the cut: Ruiz always faces screen-right, Clara always faces screen-left.
— Lips move only for the scripted lines; the listener's mouth stays closed; no subtitles.
— Cup in both of Clara's hands; folded mask in Ruiz's right fist.
— Clara's eyes stay dry in this clip.
— Cut only at 3.5s; the camera does not cut on its own.
```

### Prompt 1c · 15s · refs: @image1 Clara · @image2 Ruiz

```
SCENE CONTEXT
Night, a hospital ICU corridor. DR. RUIZ, 55, stands with his back to the closed ICU door, one meter in front of CLARA, 40, who has just asked to see her father; he grants her five minutes and steps out of her path. Clara leaves her cold paper cup of coffee on the chair behind her and goes in through the ICU door, which swings shut behind her, leaving Ruiz alone in the corridor at the door.
Prior audio context only, not visual content: "Posso entrar?"

ACTIVE REFERENCES
@image1 — CLARA: woman, 40, hours without sleep, hair loosely tied back, dark navy wool coat unbuttoned over a grey knit sweater; holds a white paper coffee cup with a brown cardboard sleeve and no lid in both hands until she sets it down. 100% matches the reference.
@image2 — DR. RUIZ: man, 55, ICU physician at the end of a night shift, teal scrubs, a light-blue surgical mask folded in his right fist, faint red pressure lines from the mask across his nose and cheeks; voice low, even, unhurried baritone, Brazilian Portuguese. 100% matches the reference.

LOCATION MAP
Corridor 2.4 meters wide, pale grey vinyl floor with a soft sheen, pale green-grey walls. Screen-left wall: the ICU door — a heavy pale-grey swing door 1.2 meters wide that opens both ways, with one small square clear-glass vision panel, 30 × 30 centimeters, at eye height 1.5 meters from the floor, glowing warm amber from the lamp in the room behind it. Screen-right wall: a row of four grey molded-plastic chairs on a steel beam, backs against the wall, directly opposite the door, 2.4 meters across. Ceiling fluorescent panels every 3 meters, every second one dark for night mode; the corridor recedes in alternating pools of cool light toward a dark far end where a small green emergency light glows. The corridor is otherwise empty.

FIRST FRAME / BLOCKING
Ruiz stands 0.6 meters in front of the closed door, body facing screen-right, eyes on Clara. Clara stands 0.8 meters in front of the chairs, body facing screen-left, eyes on Ruiz. One meter between them.
Frame one (over Clara's shoulder onto Ruiz): Clara's left shoulder and the back of her head as a soft dark shape in the screen-right foreground; Ruiz in 3/4 view, screen-left of center, sharp; the amber vision panel glowing in the door behind his shoulder.
From 6.0s (wide down the corridor): the door screen-left, the chairs screen-right, Clara and Ruiz between them at the center of frame, the corridor depth behind them.

FORMAT MODE
Timed multishot, two shots. Cuts only at the specified point, the camera does not cut on its own.
0.0s to 6.0s — over-the-shoulder on Ruiz: the five minutes, and he clears her path.
6.0s HARD CUT
6.0s to 15.0s — one continuous wide shot: Clara sets the cup down and goes in; the door closes; Ruiz remains.

OPTICS
Shot 1 (0.0–6.0s): MCU on Ruiz, 29° diagonal field of view, short telephoto portrait lens character, camera 4 meters away; close framing through lens reach; Ruiz razor-sharp, Clara's shoulder a soft dark shape, the door compressed close behind him into creamy bokeh with the amber panel a warm blur. 29° held, no drift mid-segment.
Shot 2 (6.0–15.0s): WS, 47° diagonal field of view, standard normal lens character, camera 4 meters from the door–chair line, natural human-eye perspective, zero obvious distortion, both walls and the corridor depth readable, comfortable depth of field. 47° held, no drift mid-segment; no extreme wide distortion, no telephoto compression.

CAMERA
Shot 1: standing eye height, 1.6 meters, down the corridor's length behind Clara's left shoulder; locked, with the faint organic settle of an operator's slow breathing.
Shot 2: tripod-locked at 1.4 meters on the corridor's center line, looking down its length, on the same side of the action as shot 1; the frame holds still while Clara crosses it. Focus on the door–chair plane. Tonal character: wide latitude, the amber highlight rolling off softly, shadows holding detail.

ACTION
0.0–1.0s: Ruiz holds Clara's eyes.
1.0–2.4s: Ruiz says: "Só cinco minutos."
2.4–3.6s: he holds her eyes until she gives one small nod — the back of her head dips once in the foreground.
3.6–5.0s: Ruiz takes one step to his left, deeper into the corridor, opening the path between Clara and the door; his eyes stay on her.
5.0–6.0s: Clara's foreground shoulder turns toward the chairs.
6.0s HARD CUT to the wide.
6.0–7.5s: Clara turns, bends and sets the paper cup on the seat of the chair behind her, the one directly opposite the door; she lets go of it.
7.5–9.5s: she straightens, turns and crosses 2 meters to the door at 3 km/h, passing 0.7 meters in front of Ruiz.
9.5–10.5s: she pushes the door open with her right palm and walks through into the room.
10.5–12.5s: the door swings shut on its closer and latches; the amber vision panel glows again in the closed door.
12.5–15.0s: Ruiz stands alone, 0.7 meters from the door's far edge, body turned to face the door, eyes on the closed door; the paper cup sits alone on the chair seat, screen-right.

ACTING TASK — CLARA (she is fully invested in her tactic; the work happens in her eyes):
SCENE DIRECTION (shared, unspoken): keep it to what can be done right now — facts, permission, minutes; nobody puts the open question into words.
MOTIVE (her fuel): she wants to walk into that room steady — her father should feel a calm hand, not a frightened one.
GOAL: be at his side for every one of the five minutes.
OBSTACLE: the clock he just gave her and the fear behind it; any pause out here spends the minutes.
TACTIC: she takes the yes and moves — every look is aimed at the door.
Moment to moment:
— "Só cinco minutos." — she takes both the gift and the limit, checks his eyes once to be sure, and nods.
— the cup — she glances down only to find the seat, sets the cup there and leaves it without a second look.
— the door — her eyes fix on the amber vision panel as she crosses; she passes Ruiz with one short look at his eyes — thanks, no words — and goes in.
(Safety: gaze always engaged in the task — never a frozen, glassy, unfocused stare; natural blink cadence, she blinks now and then to moisten her eyes.)

ACTING TASK — DR. RUIZ (he is fully invested in his tactic; the work happens in his eyes):
SCENE DIRECTION (shared, unspoken): keep it to what can be done right now — facts, permission, minutes; nobody puts the open question into words.
MOTIVE (his fuel): thirty years of night shifts taught him that exact words are the only kindness that holds; the rule is part of the care.
GOAL: give her the time and the limit in one breath, and see her in safely.
OBSTACLE: her gratitude — one soft look back from him and the limit stops sounding like a rule.
TACTIC: he gives the gift and the limit together and holds her eyes until he sees she has both, then clears the way and watches her go.
Moment to moment:
— "Só cinco minutos." — he holds her eyes after the line, checking that she has the number.
— the nod — he registers it and steps aside, eyes still on her.
— Clara passes — his eyes follow her to the door and through it.
— the door shuts — his eyes stay on the closed door, on the amber panel, measuring what he cannot follow from here.
(Safety: gaze always engaged in the task — never a frozen, glassy, unfocused stare; natural blink cadence, he blinks now and then to moisten his eyes.)

PERFORMANCE
Ruiz in shot 1: stubble shadow, the red mask lines across his nose and cheeks, amber catch-light from the panel at the edge of his eye, steady breathing. Both: real skin texture, no makeup sheen, no CG gloss.

PHYSICS
The paper cup is light; as it touches the plastic seat the cold coffee slops gently against the inner wall and settles. Clara's wool coat swings with her turn and settles a beat later. Her palm compresses against the door; the door has real mass and closer resistance, opens under her push, then decelerates, swings shut and latches with a small bounce. Footsteps heel to toe on vinyl, weight transferring through each step.

LIGHTING
Priority lock. The ceiling panel directly above the door–chair line is dark; the nearest lit panel hangs 2 meters deeper in the corridor, beyond the two of them, throwing cool 4000K top-back light that rims hair and shoulders. Faces are keyed only by the soft warm glow of the vision panel (a 3200K tungsten lamp inside the room) and a low bounce off the pale floor. As the door opens, a brief wedge of warm amber light from the room falls across the corridor floor and closes again with the door. White balance fixed at 4000K: cool green-grey corridor, the amber panel the only warm surface. Exposure set for the amber panel and the rims; faces low-key with detail in the shadows; no flat front light.

WARDROBE
Clara: dark navy wool coat, unbuttoned, creased, over a grey knit sweater; dark trousers. Ruiz: teal short-sleeved scrubs, slightly rumpled.

AUDIO
Only one scripted line, in Brazilian Portuguese: Ruiz "Só cinco minutos." Then: the soft tap of the paper cup on the plastic seat, footsteps on vinyl, the push of the door, the hiss of its closer and the latch click; the low hum of the fluorescent ballasts; a monitor beep that grows louder while the door is open and muffles again when it closes. No other words, no music.

STYLE
Photoreal, quiet observational hospital drama, restrained contrast with deep detailed shadows, natural skin tones, fine film grain, real-time motion.

OUTPUT SETTINGS
21:9 widescreen frame (2.33:1), composition built for the full width; 15 seconds; real-time 24 fps in both shots.

POSITIVE LOCKS
— Frame one already shows Ruiz sharp and Clara's shoulder in the foreground.
— Exactly two people in the corridor: Clara and Ruiz; the room behind the door stays unseen.
— Screen direction holds: the door is screen-left, the chairs screen-right; Ruiz faces screen-right until he turns to the door.
— The cup leaves Clara's hands only at 6.0–7.5s and stays on the chair seat for the rest of the clip; the folded mask stays in Ruiz's right fist.
— Lips move only for "Só cinco minutos."; Clara's mouth stays closed; no subtitles.
— Cut only at 6.0s; the camera does not cut on its own.
```

### Prompt 1d · 15s · refs: @image1 Clara · pai só em texto

```
SCENE CONTEXT
Night. Seen from a dark hospital corridor through the small square glass panel of a closed ICU door: inside the dim ICU room, CLARA, 40, walks to her unconscious father's bedside, sits, and takes his hand. The camera stays on the corridor side of the closed door for the whole shot.

ACTIVE REFERENCES
@image1 — CLARA: woman, 40, hours without sleep, hair loosely tied back, dark navy wool coat unbuttoned over a grey knit sweater; her hands are empty. 100% matches the reference.
Her FATHER (text only, no reference image): a thin man in his seventies, grey hair, lying on his back in the ICU bed, eyes closed, a clear oxygen nasal cannula, a pale hospital gown, a white blanket folded at mid-chest, a taped IV line in the crook of his right arm.

LOCATION MAP
Corridor side (foreground): the closed ICU door, heavy and pale grey, fills the frame, lit only by a dim cool spill from the corridor ceiling behind the camera. In it, one small square vision panel of clear glass, 30 × 30 centimeters, at eye height 1.5 meters from the floor, framed by a thin steel bead.
Room side (seen only through the glass): an ICU room 4 meters deep. The bed runs left to right across the view, 3.5 meters beyond the door, head at screen-left, foot at screen-right. A patient monitor on a wall arm above the head of the bed, screen-left, its screen glowing green with a steady waveform. An IV pole at the head of the bed. An over-bed lamp at its low setting pools warm amber light on the pillow, the blanket and the bedside. One chair on the far side of the bed, facing the door. The rest of the room falls into deep shadow.

FIRST FRAME / BLOCKING
Frame one: the dark door fills the 21:9 frame; the glowing vision panel sits at frame center, about a quarter of the frame's width. Through it, the father already lies in the bed, and Clara is already inside the room, 1.5 meters in from the door, walking away from camera toward the foot of the bed, screen-right, her back to the glass.
By 4.0s: Clara on the far side of the bed, facing the door and the camera, the bed between her and the glass. She takes the hand nearest her — her father's left hand, lying on the blanket. Her gaze stays on his face; his face is turned up, in profile to camera, eyes closed.
Composition: frame within a frame — the warm square of the room inside the cool dark door, the joined hands at the lower center of the square.

FORMAT MODE
One continuous shot, the camera does not cut on its own.

OPTICS
47° diagonal field of view, standard normal lens character, held for the whole shot, no drift. The view grows only by camera travel, never by zoom: the panel starts as a small bright square in the dark door and ends filling almost the whole frame width. Natural human-eye perspective, zero distortion. Focus set through the glass on the bedside, 4 meters beyond it; the steel bead of the panel and the glass surface stay softly out of focus.

CAMERA
Standing eye height, 1.6 meters, square-on to the door, starting 1.5 meters from the glass. A slow, steady physical push-in toward the panel at 0.25 km/h over the full 15 seconds, ending 0.4 meters from the glass — the movement of someone leaning in to look. Smooth, with a faint organic human settle. Tonal character: wide latitude, the lamp-lit pool holding detail, the door falling toward deep shadow.

ACTION
0.0–4.0s: Clara walks past the foot of the bed and along its far side to the chair, her eyes on her father's face.
4.0–6.0s: she sits on the front edge of the chair, coat still on, leaning toward the bed.
6.0–8.0s: she lifts his left hand off the blanket into both of hers and lowers their hands to the blanket's edge.
8.0–15.0s: she holds it. At 9.0s she squeezes once. At 11.0s her right thumb strokes slowly across his knuckles once. She leans 10 centimeters closer and stays, holding. Her father lies still, eyes closed, chest rising and falling slowly.

ACTING TASK — CLARA (she is fully invested in her tactic; the work happens in her eyes):
SCENE DIRECTION (shared, unspoken): keep it to what can be done right now — facts, permission, minutes; nobody puts the open question into words.
MOTIVE (her fuel): she wants him to feel a steady hand, not a frightened one — in case he can feel anything.
GOAL: reach him — get some answer from him inside the five minutes.
OBSTACLE: his stillness; every second without a reply pushes the question she refused to ask in the corridor.
TACTIC: she talks to him with her hands instead of words — a squeeze, then her eyes check his eyelids and his fingers for any answer; she checks the monitor once to confirm "stable" with her own eyes, then goes straight back to his face, keeping her own face calm for him.
Moment to moment:
— walking to the chair — her eyes find his face first and stay on it.
— sitting — she sits without taking her eyes off him.
— taking his hand — her eyes go to his eyelids: does he feel it?
— the squeeze — her eyes drop to his fingers, waiting for a squeeze back; none comes; her eyes return to his face.
— a look up at the monitor — the steady green line — and straight back to him.
— the thumb across his knuckles — her eyes on his eyelids again; she leans in and stays, still asking.
(Safety: gaze always engaged in the task — never a frozen, glassy, unfocused stare; natural blink cadence, she blinks now and then to moisten her eyes.)

ACTING TASK — FATHER (unconscious; he is in the scene as the one being held; eyes closed for the whole shot):
SCENE DIRECTION (shared, unspoken): keep it to what can be done right now — facts, permission, minutes; nobody puts the open question into words.
PRESENCE: his body holds the line the doctor called stable — slow, even breathing at 14 breaths per minute, chest rising under the blanket; his left hand lies open and slack in hers, fingers loosely curled; eyelids closed and smooth, face at rest.
(Safety: eyes stay gently closed and relaxed throughout; natural breathing rhythm; face soft and alive, never waxen.)

PERFORMANCE
Clara: real skin texture in the warm lamp light, amber catch-light of the lamp in her eyes, a soft green tint from the monitor on her cheek, visible breath. Father: thin skin on the back of his hand with visible veins, a faint pallor warmed by the lamp, the cannula tubing resting across his cheeks, slow breath at the nostrils.

PHYSICS
His hand has real dead weight: when she lifts it, the fingers droop with gravity and the wrist bends. The blanket compresses under their joined hands. The chair takes her weight as she sits; her coat folds and settles over the chair edge. The oxygen tubing moves slightly with his breathing.

LIGHTING
Priority lock. Inside the room: the over-bed lamp is the key, a warm 3200K tungsten pool from above the head of the bed, screen-left, lighting the pillow, his face in profile, the blanket and the joined hands; Clara's face takes the lamp's spill from screen-left and a faint green edge from the monitor; the room's corners fall to black. Corridor side: the door surface is dim, lit only by cool 4000K spill from behind the camera, falling toward near-black at the frame edges. A small cool reflection of a ceiling panel sits in the upper corner of the glass. White balance fixed at 4000K, so the room reads warm amber against the cool dark door. Exposure set for the lamp-lit bedside; the door is allowed to go low-key.

WARDROBE
Clara: dark navy wool coat, unbuttoned, creased, over a grey knit sweater. Father: pale hospital gown, white blanket.

AUDIO
Heard through the closed door, muffled: the monitor beep steady at 70 per minute, the soft hiss of the oxygen. Close to the camera: the low hum of the corridor's fluorescent ballasts. No dialogue — Clara's lips stay still. No music.

STYLE
Photoreal, quiet observational hospital drama, restrained contrast with deep detailed shadows, natural skin tones, fine film grain, real-time motion.

OUTPUT SETTINGS
21:9 widescreen frame (2.33:1), composition built for the full width; 15 seconds; real-time 24 fps.

POSITIVE LOCKS
— Frame one already shows the glowing panel with the father in bed and Clara inside the room.
— Exactly two people, both inside the room: Clara and her father. No one else in the room, in the corridor, or reflected in the glass.
— The camera stays on the corridor side of the closed door; the room is seen only through the glass panel for the entire shot.
— The father's eyes stay closed and his body stays still except for breathing.
— Clara holds his left hand from 8.0s to the end; her hands stay on his.
— 47° throughout; the push-in is camera travel, not zoom.
— One continuous shot; the camera does not cut on its own; no subtitles.
```

### Prompt 1e · 15s · refs: @image1 Ruiz (carregar só a dele)

```
SCENE CONTEXT
Night, a hospital ICU corridor. DR. RUIZ, 55, stands alone at the closed ICU door, looking through its small glass panel into the room where a patient's daughter holds her unconscious father's hand. He watches a moment longer than his job needs, then steps back and walks away down the corridor, leaving the glowing door and a forgotten paper cup of cold coffee on the chair opposite it.

ACTIVE REFERENCES
@image1 — DR. RUIZ: man, 55, ICU physician at the end of a night shift, teal scrubs, a light-blue surgical mask folded in his right fist, faint red pressure lines from the mask across his nose and cheeks. 100% matches the reference.

LOCATION MAP
Corridor 2.4 meters wide, pale grey vinyl floor with a soft sheen, pale green-grey walls. Screen-left wall: the closed ICU door — heavy, pale grey, 1.2 meters wide — with one small square clear-glass vision panel, 30 × 30 centimeters, at eye height 1.5 meters from the floor, glowing warm amber from the lamp in the room behind it. Screen-right wall: a row of four grey molded-plastic chairs on a steel beam, directly opposite the door; on the seat of the chair facing the door sits a white paper coffee cup with a brown cardboard sleeve, no lid, two-thirds full. Ceiling fluorescent panels every 3 meters, every second one dark for night mode; the corridor recedes in alternating pools of cool light and dim gaps toward a dark far end 25 meters away where a small green emergency light glows. The corridor is otherwise empty.

FIRST FRAME / BLOCKING
Frame one: Ruiz stands squarely at the door, his face 30 centimeters from the vision panel, body and face turned to screen-left toward the glass, in clean profile. The door runs along the screen-left edge of frame, seen almost edge-on: the panel's warm light spills out across his face, and the room inside stays out of view from this angle. Behind him, toward screen-right and in depth, the corridor's pools of light are compressed into soft bokeh.
From 8.5s (wide): the door with its glowing amber panel screen-left midground; Ruiz half a step back from it; the chair row along the screen-right foreground with the paper cup on the seat directly opposite the door; the corridor's depth at the center of frame.

FORMAT MODE
Timed multishot, two shots. Cuts only at the specified point, the camera does not cut on its own.
0.0s to 8.5s — profile close-up of Ruiz at the glass.
8.5s HARD CUT
8.5s to 15.0s — one continuous wide shot down the corridor: he leaves.

OPTICS
Shot 1 (0.0–8.5s): CU, 18° diagonal field of view, classic telephoto lens character, camera 3 meters away along the door-side wall; close framing achieved through lens reach; razor-thin focus on his near eye; only Ruiz is sharp; the corridor behind him compressed flat into a creamy bokeh wash of cool light pools; the image feels observed from a distance. 18° held, no drift mid-segment. No part of this shot becomes wide-angle or normal-lens coverage.
Shot 2 (8.5–15.0s): WS, 47° diagonal field of view, standard normal lens character, natural human-eye perspective, zero obvious distortion; the paper cup soft in the lower-right foreground, focus on the door and the corridor's depth. 47° held, no drift mid-segment.

CAMERA
Shot 1: eye height, 1.7 meters, standing 3 meters short of Ruiz along the door-side wall, looking deeper down the corridor at his profile; locked, with the faint organic settle of an operator's slow breathing.
Shot 2: tripod-locked low, at 1.0 meter, against the chair-side wall 2 meters short of the door–chair line, angled across and down the corridor so the door, the cup and the corridor's depth are all in frame; it holds perfectly still while he walks away. Tonal character: wide latitude, the amber highlight rolling off softly, shadows holding detail.

ACTION
0.0–6.0s: Ruiz looks through the glass, head still; only his eyes travel, lifting to the monitor above the bed and lowering to the bedside in turn (see ACTING TASK).
6.0–7.5s: his eyes settle low and stay; he holds his breath.
7.5–8.5s: he lets the breath out slowly through his nose, lowers his eyes and takes half a step back from the door.
8.5s HARD CUT to the wide.
8.5–10.0s: Ruiz stands half a step back from the door, the amber panel glowing at his head height; he turns to his right, away from the camera, toward the deep end of the corridor.
10.0–15.0s: he walks away down the corridor at 4 km/h, his back to the camera, through a pool of cool light and into the dim gap beyond, about 5.5 meters deeper by 15.0s. The camera holds still; the glowing door panel and the cup on the chair stay in frame as he recedes.

ACTING TASK — DR. RUIZ (he is fully invested in his tactic; the work happens in his eyes):
SCENE DIRECTION (shared, unspoken): keep it to what can be done right now — facts, permission, minutes; nobody puts the open question into words.
MOTIVE (his fuel): thirty years of nights like this one; his exactness is how he stays useful — and the scar over how much these rooms used to cost him.
GOAL: check his patient once more from the corridor, and go — the procedure, done right.
OBSTACLE: the joined hands behind the glass — the closeness his precision has kept out for thirty years; one look too long and the doctor gives way to the man.
TACTIC: he watches like a doctor: reads the monitor through the glass, then the hands, then the monitor again — every return to the monitor keeps him a doctor.
Moment to moment:
— his eyes read the monitor — the line is steady — then lower to the joined hands on the blanket.
— back up to the monitor, checking the numbers again.
— down to the hands.
— the break: on the next pass his eyes stay on the hands and the monitor gets no more looks; he holds them there and holds his breath.
— he lets the breath go, lowers his eyes, and steps back — back to the corridor, back to the job.
(Safety: gaze always engaged in the task — never a frozen, glassy, unfocused stare; natural blink cadence, he blinks now and then to moisten his eyes.)

PERFORMANCE
Shot 1: pore-level skin, end-of-shift stubble, the red mask lines across the bridge of his nose and his cheeks, the warm amber light catching the wet surface of his near eye as a small catch-light, slow breath visible at the nostril, the exhale visible in the slight drop of his shoulders.

PHYSICS
His half step back transfers weight from the front foot to the back foot and settles. Walking away: heel contact, weight transfer, hip shift, toe push-off on soft-soled clogs; the loose scrubs move a beat behind each stride; the folded mask stays closed in his right fist, arm swinging with real weight. The cup on the seat stays still, the cold coffee's surface flat.

LIGHTING
Priority lock. Shot 1: the vision panel's warm amber spill (a 3200K tungsten lamp inside the room) is the only key, from screen-left, falling across the front of his face — forehead, nose, the near eye — while the rest of his face falls off into shadow; cool 4000K top-back light from the lit ceiling panel deeper in the corridor rims his hair and shoulders. Shot 2: the amber panel is the warmest point in frame; the lit ceiling panels lay cool pools on the floor; Ruiz turns into a dark shape as he crosses each pool and gap. White balance fixed at 4000K. Exposure set for the amber on his eye in shot 1 and for the panel and light pools in shot 2; no flat front light.

WARDROBE
Ruiz: teal short-sleeved scrubs, slightly rumpled; the light-blue mask folded in his right fist.

AUDIO
The low hum of the fluorescent ballasts; the monitor beep muffled behind the door at 70 per minute; his slow exhale through the nose; soft footsteps on vinyl receding down the corridor. No dialogue — his mouth stays closed. No music.

STYLE
Photoreal, quiet observational hospital drama, restrained contrast with deep detailed shadows, natural skin tones, fine film grain, real-time motion.

OUTPUT SETTINGS
21:9 widescreen frame (2.33:1), composition built for the full width; 15 seconds; real-time 24 fps in both shots.

POSITIVE LOCKS
— Frame one already shows Ruiz in profile at the glass, face lit amber.
— Exactly one person in frame: Ruiz. The corridor stays empty; the room's interior stays out of view.
— Ruiz faces screen-left at the door, then turns and walks away from the camera into the depth of the corridor.
— The paper cup stays on the chair seat; the folded mask stays in his right fist.
— The vision panel glows warm amber in every frame.
— Silence: no spoken words, no subtitles, no music.
— Cut only at 8.5s; the camera does not cut on its own.
```

Se quiser mudar alguma coisa (mais um inserto, a cena dividida de outro jeito, outro figurino), me diz que eu atualizo o HTML.
