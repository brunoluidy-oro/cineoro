## CABRESTO — O sonho de Seu Damião (12s)

Aviso rápido antes do prompt. A bíblia proíbe quase tudo o que essa cena pede: câmera lenta, cor saturada, verde fora do juazeiro, nuvens, outra pessoa em quadro, música e, de nome, a sanfona. Segui o seu pedido. O sonho entra como a **única exceção declarada do filme**, e ela só funciona se ficar fechada nesta geração. Por isso o prompt suspende, só aqui, os templates FILM LOOK, LIGHT, WORLD e a espinha de negativos nos pontos que entram em choque com a cena. O resto continua valendo: textura de 35mm, NO LENS FLARES, nenhuma legenda, o mundo de 1958 e Damião sem nenhum sinal de cegueira. No sonho ele enxerga.

Defaults que assumi (mude o que quiser):
- **Onde fica:** a noite do dia 2, entre G15 ("Zé?" / "Tô aqui, pai.") e G16 ("Bebe tu. Eu num tô com sede."). Proposta de numeração: **G15b**. Ela soma 12s ao corte e ainda cabe no teto de 8:00.
- **Damião no sonho:** usa o estado `@DAMIAO_POUSO` (sem chapéu e sem gibão, de camisa). Assim o rosto aparece sem a sombra da aba: no sonho não há nada a esconder. Os olhos são normais, escuros e sem névoa nenhuma.
- **A esposa:** ganha a tag nova **`@ESPOSA`**, que ainda não está no registro e precisa entrar na bíblia (§1.2 e §7). Como não tem asset, vai só por texto. Ela não fala e ninguém toca ninguém.
- **Sanfona:** uma sanfona só, tocando uma melodia lenta, muito baixa e distante, sem zabumba, triângulo ou qualquer outro instrumento. A chuva fica sempre mais alta que a música.
- **Câmera lenta:** a geração inteira em câmera lenta (cerca de 4×). A chuva, o cabelo e o vestido em câmera lenta é que separam o sonho do resto do filme.
- **O fim:** corte seco no sorriso dela, no meio de um passo que ela dá na direção dele. Ela não chega até ele.

**Cabeçalho**
```
O QUE ACONTECE: No sonho, a chuva chega ao sertão. Gotas grossas caem em câmera lenta sobre a terra
rachada, que escurece, e o verde brota intenso na caatinga. Seu Damião, sem chapéu e encharcado,
ergue o rosto para a chuva e baixa o olhar: a falecida esposa está de vestido branco no meio da
chuva, a seis metros, sorrindo para ele.
O QUE SE DIZ: nada. Só a chuva e uma sanfona bem baixinha, ao longe.
TEMPO: a chuva na terra rachada — 5s · Damião e a esposa — 7s = 12s
COMO TERMINA: corte seco no sorriso dela, no meio de um passo que ela dá na direção dele.
```

**Prompt**
```
CONTRACT — Live-action photoreal film footage, 21:9, 12 seconds total, 2 shots with 1 hard cut at 5s,
the WHOLE generation in SLOW MOTION (filmed at high frame rate, played back about 4x slower — every
raindrop, splash, strand of hair and fold of cloth moves slowly and heavily), handheld, no dialogue.
This is a DREAM inside a realist film: the image stays real film footage, only the colour, the
rain and the time are changed. Music: ONLY one faint, distant solo accordion melody, very quiet,
under the rain. NO other instrument, NO subtitles, NO on-screen text.

REFERENCES — each reference has ONE job:
@DAMIAO_POUSO — IDENTITY of @DAMIAO_POUSO: face, hands, build, faded cotton shirt, hat off. 100%
matches.
REFERENCE SCOPE: the identity reference supplies face, body and wardrobe ONLY — IGNORE its
backdrop, night, firelight, exposure and colour grade.

WHO IS WHO — READ FIRST, ABSOLUTE:
@DAMIAO_POUSO (66, lean, deep sun-cut lines, white stubble, thin grey moustache; hat off, white
hair flattened by it, leather jacket off, faded cotton shirt; tip of the right index finger missing
— 100% matches its reference) — the OLD COWHAND, here soaked by rain: hair plastered to his skull,
shirt dark and clinging; stands still; owns the LEFT side of the frame; his eyes are ordinary dark
brown eyes, clear, wet, NO haze; NEVER cries, NEVER walks to her, NEVER reaches out, NEVER looks
into the lens.
@ESPOSA (his late wife, early sixties, small and straight-backed, dark skin lined by sun, grey hair
pulled back in a low bun coming loose in the rain; a plain long white cotton dress, home-sewn, wet
and heavy, clinging at the shoulders and hem, dusty-red mud splashed on the hem; barefoot) — owns
the RIGHT side of the frame, about 6 m from him; NEVER speaks, NEVER floats, NEVER glows, NEVER
looks into the lens.
FACES: exactly TWO people; each face exists once; no other people, no twins, no clones; NO cattle,
NO horse in this dream.
CONTACT: nobody touches anyone.

SCENE — A dream of the old cowhand during the great drought of 1958: the rain finally comes to the
sertão. Heavy drops fall in slow motion on cracked ochre earth; the grey thorn scrub has turned an
intense, impossible green; in the middle of the rain stands his late wife in a white dress, smiling
at him.
THE SOUL OF THE SCENE (play it, never explain it): for one moment everything he has lost is given
back at once — the rain, the green, her, and his own sight. He doesn't move, because moving might
end it.

ABSOLUTE LOCKS — break one and the take is WRONG, regenerate:
1. SLOW MOTION throughout, real and heavy — WRONG if anything moves at normal speed or floats
   weightless.
2. The colour is SATURATED and the green is INTENSE, but it stays photographed film, not a painting
   — WRONG if it looks like CGI, a fantasy render or a glowing fairy tale.
3. @ESPOSA is a solid, wet, real woman standing on the ground — WRONG if she glows, is
   translucent, floats, has a halo or a light behind her.
4. @DAMIAO_POUSO stands still with clear, ordinary eyes; he does not cry — WRONG if tears, a white or
   milky eye, or a reaching hand.
5. Only one faint, distant solo accordion, always quieter than the rain — WRONG if any other
   instrument, a full song, a choir or loud music.

TIMELINE — 2 shots, 1 hard cut at 5s; the camera adds no cuts of its own:
SHOT 1 (0–5s) — CU of the ground, 47°, camera handheld at knee height looking down at 40°, STAYS
PUT and breathes; in SLOW MOTION: the rain already falling, fat drops striking cracked ochre earth
plates; each drop throws a small crown of dust and water, the dry crust darkens in spreading
blotches, water runs into the cracks and fills them; at the top of the frame a tuft of new bright
green leaves on a grey thorn branch, beaded with water. HARD CUT.
SHOT 2 (5–12s) — WS, 63°, camera handheld at chest height 3 m behind and to the right of
@DAMIAO_POUSO, over his right shoulder, STAYS PUT and breathes; in SLOW MOTION: @DAMIAO_POUSO in the
frame-LEFT foreground, three-quarter back, face tipped up into the rain, water running off his
brow; he lowers his face; 6 m beyond him, frame-RIGHT, @ESPOSA standing in the rain among intense
green scrub, the wet white dress heavy on her, smiling at him; at 10–12s she takes one slow step
toward him, mud lifting off her bare heel. Hard end mid-step, on her smile.

ACTING — @DAMIAO_POUSO (fully invested in the tactic; the work happens in the eyes)
SCENE DIRECTION (shared, unspoken): stay inside the dream as long as it lasts.
EVENT: the dream gives everything back at once — and the film knows it can't last.
MOTIVE: forty years of rain prayed for, a wife buried; this is all of it.
GOAL: keep her there. OBSTACLE: any movement might wake him.
TACTIC: hold still; take her in with the eyes — her face, her dress, her face again — the way he
once checked the sky for rain.
MOMENT TO MOMENT: — [5–8s] face up, eyes closed against the drops, mouth slightly open, drinking the
air — [8–10s] the face comes down, the eyes open and find her at once, cleanly, no delay — [10–12s]
his eyes go from her face to her feet and back as she steps; he does not move.
LIVING EYES: wet lashes, rain forcing uneven blinks, saccades between her face and her step;
involuntary detail: his chest lifts once in a long held breath. Clear, focused eyes; a frozen pupil
or a glassy stare is wrong.
NOT: crying, a trembling chin, reaching out, walking toward her, a smile breaking wide, looking into
the lens.

ACTING — @ESPOSA: TACTIC welcome him without a word, the way she once met him back from a drive;
eyes on his face, steady, a small private smile, crow's feet deepening; involuntary detail: she
blinks rain off her lashes and the smile stays; NOT a beatific saint's smile, NOT ghostly, NOT
beckoning with a hand, NOT looking into the lens.

CAMERA — handheld, the operator on foot, a real body in the rain: drops strike near the lens edge,
no droplets on the lens. MOVEMENT: both shots STAY PUT and breathe, slow-motion tremor; one movement
only. OPTICS: shot 1 CU 47° — shallow focus, the drops sharp, background soft; shot 2 WS 63° —
natural perspective, deep enough to hold both, falloff on the far scrub; no lens drift inside a
shot. FOCUS: shot 1 on the impact point; shot 2 starts on the back of his head, racks once to her
face at 9s. HORIZON: level within 2°. Composition off-centre: he on the left third, she on the
right. NOT: dolly, zoom, orbit, drone, crane, a push into her face, dream blur, soft-focus filter.

GEOMETRY — flat ground of cracked earth among low thorn scrub; @DAMIAO_POUSO frame-LEFT, 3 m from
the camera; @ESPOSA frame-RIGHT, 6 m beyond him, facing him and the camera's direction; the camera
behind his right shoulder, never between them, never crossing to her side.

PHYSICS & MATERIAL — rain heavy and vertical, fat drops in slow motion stretching and breaking on
impact; dry earth first resists — drops bead and roll on the dust — then darkens, softens and
drinks; water threads into the cracks; his wet shirt clings and drips; her cotton dress is HEAVY
with water, hangs and sways slowly, never billows; loose hair strands stick to her temples; mud on
her heel. Nothing floats, nothing loops, nothing glows. OVER-REAL: dust craters punched by each
drop, the crust breaking into mud at the edges of the plates, water beading on grey thorns,
rain-soaked cotton showing the weave, his sun-cut wrinkles running with water, his missing
fingertip on the right hand at his side. If any surface looks clean, smooth, plastic, CGI or
rendered — WRONG.

LIGHT — NATURAL LIGHT ONLY, dream rain, SOFT & SATURATED (KEY): the only light is a low, heavy
rain-cloud sky, ~6500 K, soft, from above and slightly frame-right; no sun. It wraps every face
gently, the far side of faces in soft shade; the rain catches it as fine bright lines. Exposed for
the faces; mid-key, NOT underexposed, NO crushed blacks; shadows soft but breathing; even exposure
to all four corners, NO vignette. The light stays from above and frame-right in both shots; lit
sides never flip. NOT: sunbeams, god rays, a backlight or halo behind @ESPOSA, a glow around her,
golden light, flat grey murk.

FILM LOOK (KEY — the dream variant of this film's look): real 35mm colour negative, 250-speed stock,
the same grain and texture as the rest of the film — but in this dream the colour is SATURATED: the
earth darkening to a deep wet red-ochre, the new leaves an intense pure green, the dress a clean
warm white, skin rich and wet. Highlights roll off with gentle halation; moderate organic MOVING
grain; softer than digital; real skin with pores and sun damage; even exposure to all four
corners, NO vignette. Saturated by the film stock and the wet world, never by a filter — NOT
teal-and-orange, NOT a fantasy grade, NOT neon, NOT HDR, NOT a render, NOT CGI.
LENS LOOK (KEY): 2.39:1 spherical 35mm lens character — round soft bokeh, natural perspective,
shallow focus with a gentle falloff in the close-ups, mild focus breathing; no anamorphic oval
bokeh, no streaks — NOT over-sharpened, NOT a crisp AI look.
NO LENS FLARES: no flares, no light streaks, no floating bokeh orbs, no glow overlays, no sun disc in
frame; every light source stays small and contained within itself.

SOUND — slowed-down, deep rain: a dense heavy roar of rain, each big drop landing as a low thud on
the dry earth in shot 1, then hiss and drip; water running in the cracks; one far roll of thunder at
3s. Under it, from far away and very quiet, ONE solo accordion plays a slow, simple melody of a
few notes — like a memory, always quieter than the rain, no rhythm section. Nobody speaks; no
breath sounds louder than the rain. NO other instrument: NO zabumba, NO triangle, NO drums, NO
guitar, NO viola, NO fiddle, NO strings, NO choir, NO singing, NO ambient pad, NO synth, NO swell,
NO chimes.

WORLD — the sertão of Paraíba, Brazil, 1958, in a dream: cracked ochre earth, thorn scrub
(jurema, catingueira) and mandacaru suddenly leafing out green; everything is earth, cotton,
leather, wood. NO plastic, NO synthetic fabric, NO zippers, NO jeans, NO watch, NO glasses, NO
roads, NO power lines, NO buildings, NO fences, NO other people, NO cattle, NO horse, NO dogs.

NEGATIVE: normal-speed motion, floaty weightless motion, @ESPOSA glowing, translucent, ghostly,
floating, a halo or backlight behind her, a wedding veil, a modern white dress, @ESPOSA speaking or
beckoning, @DAMIAO_POUSO crying, tears, reaching out, walking to her, white or milky eyes, hazy
eyes, a hat, a third person, cattle, a horse, a fantasy painting look, dream blur, soft-focus
filter, sparkles, light particles, rainbow, sunbeams, god rays, raindrops on the lens, a full
band, loud music, any instrument other than one faint accordion; centred symmetrical framing, flat
even light, beauty light, milky blacks, crushed blacks, vignette, teal-and-orange, HDR, lens flare,
sun disc in frame, plastic skin, waxy skin, beauty retouching, clean faces, doll face, glassy
stare, frozen pupils, glowing eyes, zombie eyes, looking into the lens, twins, clones, extra
people, warped hands, extra fingers, looping motion, gimbal, drone, aerial, crane, zoom,
over-sharpened, CGI, 3D render, subtitles, captions, on-screen text, watermark, logo, zabumba,
triangle, viola, guitar, fiddle, fife, choir, ambient pad, drone tone, swell, chimes, wrong aspect
ratio.

[ORDER: 2 shots, 1 hard cut at 5s, 12s, all in SLOW MOTION, handheld, staying put — (1, 0–5s) CU:
fat drops strike cracked earth, it darkens and drinks, new green leaves beaded with water — (2,
5–12s) WS over his right shoulder: @DAMIAO_POUSO frame-left, soaked, face up then down, eyes clear;
@ESPOSA frame-right 6 m away in a wet white dress among intense green, solid and real, smiling; she
takes one slow step — hard end mid-step on her smile. Invariants: real heavy slow motion; saturated
but filmed, never CGI; she is solid, no glow; he stands still, clear eyes, no tears; only one faint
distant accordion under the rain. Look: 35mm grain, saturated dream colour, no vignette, no flares.
Nobody speaks. NO subtitles.]
```

**Cartão de geração**
```
GENERATION CARD
Model: Seedance 2.5 (Higgsfield seedance_2_5) · Task: reference-to-video (omni-reference)
Duration: 12s (= timeline) · Aspect: 21:9 · Resolution: draft 480p → final 1080p (2206×946) ·
Audio: on · bitrate: high
Attach in this order: 1) DAMIAO_POUSO (Element: rosto + camisa, sem chapéu) — identidade.
@ESPOSA vai só por texto (sem asset). Se for reaparecer, gere o rosto dela uma vez, em close, e
registre como Element ESPOSA.
Notes: faça o draft primeiro. O risco maior é a esposa virar "fantasma" (brilho, contraluz,
transparência); se acontecer, repita a lock 3 dentro do SHOT 2. Depois vem a música: se entrar
uma banda ou a sanfona encobrir a chuva, baixe para "barely audible" ou gere sem música e ponha
a sanfona na montagem, que é o caminho mais seguro. Confira também que a câmera lenta vale para os
12s e que o olho do Damião sai limpo. Para a bíblia: acrescentar @ESPOSA ao registro e ao elenco,
o L5 SONHO e o look de sonho como exceção única, e corrigir em §10 que o verde não aparece "uma
vez" nem há "nada de sanfona" — agora as duas regras têm exceção no sonho.
```
