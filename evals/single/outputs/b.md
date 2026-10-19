# Cineoro, modo C (reparo) — "Pescador puxando a rede"

O prompt que você usou era de uma linha, de humor ("cinematic, dramatic lighting, emotional"). Não existe bloco para trocar. Por isso o prompt inteiro foi reconstruído na espinha do CINEORO e **substitui o antigo**. Não anexe frames do take que falhou como keyframe: eles carregam o olhar de boneca e a luz de estúdio para a nova geração.

## Diagnóstico

| Sintoma | Causa na redação antiga | Correção | Departamento |
|---|---|---|---|
| Saiu música | Nenhuma política de música. A palavra "emotional" chama a trilha padrão da engine. | Política "sem música" com sinônimos no CONTRACT, no SOUND, no NEGATIVE e no ORDER. Som diegético específico. | sound |
| Rosto com olhar de boneca | "emotional" é rótulo de emoção. Não há tarefa para os olhos e o rosto é o foco. | ACTING com tática (ler o peso da rede com as mãos e os olhos). Fisiologia dos olhos vivos. Olhar concreto na rede e na água, não na lente. Rosto em perfil, na sombra. | performance |
| Luz de estúdio | "dramatic lighting" não nomeia fonte, então a engine usa preenchimento plano e sem fonte. | Uma única fonte motivada (lampião no barco) com direção, Kelvin, alcance e o que fica escuro. Sem vinheta. Lado iluminado travado. | light |
| (provável) mexe como câmera de IA, rede sem peso | Ação como palavra ("pulls a net"), sem massa nem resistência. | PHYSICS com peso, resistência e estados graduais. Câmera como operador humano, que FICA NO LUGAR. | realism, camera |

## Cabeçalho

```
O QUE ACONTECE: Noite fechada, um pescador sozinho num barco aberto puxa uma rede mão sobre mão; a rede fica pesada, ele se apoia para vencer o peso, ela cede e um peixe prateado aparece no clarão do lampião.
O QUE É DITO: nada (sem diálogo, sem narração).
TEMPO: puxa em curso, ritmo de trabalho, 4s · a rede pesa, ele se escora, 4s · ela cede, o brilho do peixe, ele continua puxando, 4s = 12s
COMO TERMINA: corte seco no meio da puxada, o rosto nunca em close.
DIREÇÃO: (1) luz de um lampião só, de lado e atrás, para o rosto ser trabalho e sombra e não retrato iluminado; (2) o drama vem do peso da rede, não do rosto, então os olhos têm uma tarefa e o rosto fica em perfil; (3) silêncio de barco, sem trilha, porque a emoção já está na solidão e no esforço.
```

## Prompt

```
CONTRACT — Live-action photoreal film footage, 16:9, 12 seconds total, ONE continuous take, no cuts, quiet breathing handheld, real-time motion, no dialogue. NO music, NO score, NO subtitles, NO on-screen text.

SCENE — Deep night on open dark water. One man, alone in a small wooden fishing skiff, is already hauling a wet net in over the gunwale, hand over hand, in progress at the first frame. No other boat, no other person, no shore light.
THE SOUL OF THE SCENE (play it, never explain it): he has done this ten thousand times and reads the net through his palms; the whole night is in how heavy it is.

ABSOLUTE LOCKS — break one and the take is WRONG, regenerate:
1. He is ALONE in the boat and on the water. WRONG if a second person, boat or shore light appears.
2. The only key is one hanging lantern frame-LEFT behind him; it never moves sides. WRONG if the light looks like a studio, a softbox or a frontal fill.
3. His face is a dark profile turned toward the net (frame-RIGHT), eyes on the net and the water, never at the lens. WRONG if he faces the camera or the eyes look glassy.
4. The net is heavy: it comes in gradually, with resistance. WRONG if it floats, glides or comes in effortlessly.
5. No music of any kind.

TIMELINE — ONE continuous take, no cuts, already in progress at the first frame:
BEAT 1 (0–4s) — MS, 47°: he is mid-haul, standing amidships, right hand over left, pulling the wet net up over the right gunwale in dripping armfuls; it piles in a dark heap at his boots; water streams from the mesh back into the sea.
BEAT 2 (4–8s) — the net goes heavy: he stops, plants his left boot against a rib of the hull, leans back with his whole weight, the skiff heels a few degrees toward him; his jaw sets once.
BEAT 3 (8–12s) — the net gives, three or four arm-lengths arrive at once; a single silver fish flashes in the lantern light as it comes over the rail; he does not look up and keeps hauling. Hard end mid-pull.

ACTING — @FISHERMAN (fully invested in the tactic; the work happens in the eyes)
SCENE DIRECTION (shared, unspoken): keep the net coming without losing it.
EVENT: a man tests the night's catch by the weight in his hands.
MOTIVE: the catch is the night's wage.
GOAL: land the net before the weight turns it against him.
OBSTACLE: the wet net, the cold, the pitching hull.
TACTIC: read the net through his palms and forearms; eyes on the mesh and the black water at the rail, measuring how much is left to come.
MOMENT TO MOMENT: — [0–4s] steady hauling, eyes on the mesh checking each armful — [4–8s] the weight stops him: eyes drop to the water at the rail, he braces — [8–12s] the give, a quick check of the silver in the mesh, then back to the work.
LIVING EYES: pupils move with the task — mesh, water, the next armful; blinks uneven and a beat late; slight asymmetry. Involuntary detail: his jaw sets once at 5s. A small reflection of the lantern in the eye is fine; a frozen pupil is wrong.
NOT: looking into the lens, a sad or heroic face, a smile, crying, a posed stare.

CAMERA — handheld documentary, the operator standing in the skiff 2 m from him, at chest height, on the side of the boat away from the lantern (shadow side), about 70° off his axis. MOVEMENT: the camera STAYS PUT and breathes (a small tremor, a few degrees off level, a drift that arrives a beat late, the hull's roll felt in the frame); no travel, no push-in. OPTICS: MS, 47° — natural perspective, moderate depth, no lens drift. FOCUS: on his hands and the net, then holds as the fish appears. HORIZON: slightly rolling with the boat. NOT: gimbal glide, drone, dolly, zoom, orbit, slow motion, a close-up of the face.

GEOMETRY — the skiff about 5 m long, he stands amidships facing frame-RIGHT toward the right gunwale where the net comes in; the lantern hangs frame-LEFT on a short post 1.5 m behind and above him; camera 2 m away at chest height; beyond 3 m of water, darkness.

PHYSICS & MATERIAL — the wet net is HEAVY: it comes up in sagging armfuls, drips in strings, the mesh springs and tangles at the rail, knots catch on the gunwale and he frees them; the hull rocks and heels as he leans; water sheets off the mesh; breath fog thin in the cold. START: loose light armfuls. DURING: the weight builds and stops him. END: it gives and arrives faster. Nothing floats, nothing loops. OVER-REAL: tarred hemp-brown mesh with cork floats, salt crust and fish scales on the gunwale, cracked wet knuckles, wool sweater beaded with spray, scuffed oilskin, a worn dark patch on the gunwale where nets have been hauled for years. If any surface looks clean, smooth, plastic, CGI or rendered — WRONG.

LIGHT — MOTIVATED LIGHT ONLY, deep night, DIM & COLD (KEY): the only key is a small kerosene lantern hanging frame-LEFT behind him and above, ~2000 K, painting a warm rim on his back, the near shoulder and the edge of the cheek in profile and a restless warm flicker on the wet net; faint cold sea-and-sky ambience ~9000 K on the water. It reaches about 2 m and dies; the far side of his face and the water beyond fall into deep shadow. Exposed for the lit hands and net; shadows deep but breathing, never crushed; even exposure corner to corner, NO vignette. The lantern stays frame-left, off the camera's side, the whole take; the lit side never flips. NOT: studio light, softbox, flat even light, frontal beauty fill, daylight, moonlight blue wash, a second source, milky blacks.

FILM LOOK (KEY — reproduce this exact photographic character): real 35mm film, 500-speed stock, pushed one stop; lantern-amber against deep blue-black, muted, never teal-and-orange; highlights roll off with soft halation on the wet net; shadows deep but breathing; fine organic moving grain, most visible in the dark; real skin with pores and lines; spherical lens character, round soft bokeh. NOT a render, NOT HDR, NOT digital-clean. NO LENS FLARES: no flares, no light streaks, no floating bokeh orbs, no glow overlays; the lantern stays small and contained.

SOUND — DIEGETIC ONLY, dirty-real: water streaming off the mesh back into the sea; the wet hiss of rope-and-net dragging over wood; knots knocking the gunwale; the hull creaking and slapping small waves; his breath through the nose, a held breath at 5s and a release; the lantern's wick fluttering; the small flap of the fish on the boards at 10s. A beat of near-silence at 5s while he braces. NO music, NO score, NO BGM, NO instrumental, NO melody, NO synth, NO ambient pad, NO drone, NO hum, NO swell, NO chimes, NO voice-over, NO narration.

NEGATIVE: a second person, another boat, shore lights, him facing the camera, doll eyes, glassy stare, frozen pupils, sad or heroic face, smiling, effortless hauling, floating net, net gliding, clean new net, studio light, softbox, flat even light, beauty fill, daylight, moonlight wash, second light source, vignette, milky blacks, HDR glow, lens flare, CGI water, plastic skin, beauty retouching, gimbal, drone, dolly, zoom, orbit, slow motion, extra cuts, looping motion, music, score, BGM, pad, drone tone, subtitles, captions, on-screen text, warped hands, extra fingers, watermark, wrong aspect ratio.

[ORDER: ONE take, 12s, 16:9, quiet breathing handheld, camera STAYS PUT — (0–4s) mid-haul, wet net in armfuls over the right gunwale — (4–8s) the net goes heavy, he braces, the hull heels, his jaw sets — (8–12s) it gives, a silver fish flashes in the lantern, he keeps hauling — hard end mid-pull. Invariants: alone; one lantern frame-left, lit side never flips; face in dark profile, eyes on the net, never at the lens; the net is heavy, gradual; no music. Look: 35mm, lantern amber against blue-black, fine grain, no vignette. No dialogue. NO music, NO subtitles.]
```

## Cartão de geração

```
GENERATION CARD
Model: Seedance 2.5 · Task: text-to-video (sem referências)
Duration: 12s (= timeline) · Aspect: 16:9 · Resolution: draft 480p → final 1080p · Audio: on
Attach in this order: nenhum anexo
Notes: defaults assumidos sem perguntar: estilo realista observacional (você pediu "cinematic" sem estilo específico), plano médio a 47°, um take contínuo de 12 s, lampião como única fonte, sem diálogo, sem trilha, pescador sem identidade fixa (sem referência). Faça rascunho antes e confira, nessa ordem: (1) sem música; (2) o lampião sempre à esquerda e sem cara de estúdio; (3) olhos com movimento (olhando a rede, não à lente); (4) a rede pesada, vindo aos poucos.
```

## O que olhar no rascunho e plano B

1. Olhar, luz e música são os três sintomas originais. Confira nessa ordem.
2. Escada de fallback, do mais barato ao mais caro:
   - Só a música voltou: edição de áudio do take ("remove the background music; keep water, creaks and breath exactly as they are; picture unchanged").
   - Olhos ainda sem vida: regenerar mudando só o ACTING (esconder mais o rosto: capuz ou aba do boné, rosto de perfil mais fechado, ou foco só nas mãos).
   - Luz ainda de estúdio: regenerar mudando só o bloco LIGHT, deixando o lampião mais baixo e a escuridão além de 2 m mais defendida.
3. Se você quiser outra abordagem num momento-chave, ALTERNATIVE DIRECTION: a mesma cena em plano detalhe só das mãos e da rede (12°, rosto fora de quadro), sem nunca mostrar o rosto. É a saída mais segura contra o olhar de boneca.
