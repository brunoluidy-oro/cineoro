# Reparo: fogueira com pederneira (Seedance 2.5)

## Diagnóstico

O prompt antigo era uma frase de ação seguida de adjetivos, e cada falha do take vem de uma palavra que estava lá ou de uma instrução que faltava:

| Sintoma | Causa | Correção (departamento) |
|---|---|---|
| **Música de fundo** | Nada proibia música, e "cinematic" e "emotional" puxam trilha. | Música proibida com sinônimos no começo (CONTRACT) e no fim (SOUND, NEGATIVE, ORDER), mais uma lista de sons do mundo: o raspar do bastão, o sopro, o estalo dos gravetos (som). |
| **Fogueira já acesa no começo** | "lights a campfire" descreve a ação numa palavra só, então o motor pula direto pro resultado, e "campfire" já traz o fogo pronto. Não tinha linha do tempo nem estado gradual. | O processo inteiro em 4 BEATS com segundos (faísca que falha → brasa → sopro → chama → gravetos), o estado do fogo em START/DURING/END e a trava "nenhuma chama nem brilho antes de 6s", repetida em quatro lugares (story, realism). |
| **Luz de estúdio** | "dramatic lighting" não é uma fonte de luz. Antes de a fogueira existir não havia luz nenhuma no mundo, aí o motor inventou um refletor. | Luz motivada: lua fraca e fria atrás dela mais o clarão das faíscas, depois a brasa e a chama crescendo. O quadro só clareia porque o fogo cresce. Câmera do lado da sombra, com NOT studio, softbox e fill (light). |
| **Olhar vidrado de boneca** | "emotional" pede um rosto que interpreta emoção, "beautiful" pede pele de modelo, e sem nada pra fazer a pupila congela. | Tarefa no ACTING: ela convence o fogo a pegar, e os olhos seguem a faísca, a brasa e a fumaça. Mais a fisiologia dos olhos vivos e um detalhe involuntário: ela prende o fôlego no golpe forte e solta pelo nariz quando a brasa acende. Saíram as palavras de beleza (performance). |
| (extra) **"4k"** | O Seedance 2.5 não gera 4K (o máximo é 1080p). A palavra só empurra a imagem pro digital limpo. | Saiu do prompt. "clean 4K" entrou no NEGATIVE (light). |

## Caminho

**Regenerar do zero em text-to-video, com draft em 480p primeiro e depois finalizar o mesmo draft em 1080p.**
Só a música daria pra tirar com uma edição de áudio. Mas como a fogueira já aparece acesa no primeiro frame, o evento do plano não existe nesse take, e luz, tempo e atuação falharam juntos. É uma falha sistêmica, então editar não salva. Num reparo normal eu trocaria um bloco e manteria o resto idêntico. Aqui o prompt antigo não tinha blocos, então o bloco trocado é o prompt inteiro.

**Padrões que eu decidi:**
- 16:9, 15 s, um plano só sem cortes. Plano médio a 47°, câmera na mão parada, respirando, do outro lado do círculo de pedras.
- "Pederneira" = **bastão de ferrocério com raspador de aço**, que é a pederneira de camping de hoje. Bastão na mão esquerda, raspador na direita. Se a sua for a tradicional (pedra + fuzil de aço + pano carbonizado), só os trechos do bastão mudam e eu reescrevo.
- Ela não fala nada.
- Antes do fogo, as únicas luzes são a lua fraca atrás dela e as faíscas. Ela fica escura, mas dá pra ver.
- Sem referência. Se quiser uma atriz específica, anexe um retrato de rosto como IDENTITY. **Não** use frame do take ruim: ele traz junto o olhar de boneca e a luz de estúdio.

## Cabeçalho

```
O QUE ACONTECE: à noite, sozinha numa floresta, uma mulher de uns 30 anos tira faísca da pederneira até a isca
pegar, sopra a brasa até virar chama e põe o fogo nos gravetos.
O QUE SE FALA: nada.
TEMPO: dois golpes fracos, faíscas morrem — 3s · aperta a isca, golpe forte, uma brasa — 4s · ergue e sopra,
fumaça, chama aos 10s — 4s · põe nos gravetos, os finos pegam, ela estica a mão pro próximo — 4s = 15s
COMO TERMINA: corte seco no meio do gesto, a mão buscando mais um graveto, o fogo ainda pequeno.
```

## Prompt novo (todos os blocos; cole inteiro)

```
CONTRACT — Live-action photoreal film footage, 16:9, 15 seconds total, ONE continuous take with no cuts, quiet breathing handheld documentary, real-time motion, no dialogue. NO music, NO score, NO subtitles, NO on-screen text.

WHO IS WHO — READ FIRST, ABSOLUTE:
THE WOMAN (about 30, lean, dark hair in a loose low knot with strands falling forward, weathered skin, no makeup, chapped lips, faded olive canvas jacket with frayed cuffs) — the only person in the forest: she kneels at a ring of stones and lights a fire with a ferrocerium rod and a steel scraper; NEVER speaks, NEVER looks into the lens, NEVER stands; she owns the RIGHT half of the frame, the fire pit sits lower-left.
FACES: her face exists once; nobody else in frame, no figure among the trees.

SCENE — Night in a dense forest, fully dark. A woman alone kneels at a ring of stones: a nest of dry grass and bark shavings in the middle, a small teepee of pencil-thin dead twigs beside it. She is already striking sparks into the nest; the fire is not lit yet.
THE SOUL OF THE SCENE (play it, never explain it): she has done this many times and refuses to let it become an emergency — this is her only dry tinder, so every strike and every breath is measured.

ABSOLUTE LOCKS — break one and the take is WRONG, regenerate:
1. THE FIRE IS NOT LIT AT THE START: the first frame shows a cold, dark pit — no flame, no glow, no embers. Sparks only until 6s, a coin-sized ember from 6s, the first flame at 10s. WRONG if any flame or glow exists before 6s, or the fire appears whole.
2. ONLY THE WORLD'S LIGHT: before the ember, weak cold moonlight from behind her and the spark flashes; then the growing fire. WRONG if any lamp, softbox or fill lights her face — the frame brightens only because the fire grows.
3. HER EYES WORK: they follow the sparks, the ember, the smoke, the twigs. WRONG if she holds a fixed glassy stare or looks into the lens.
4. HANDS: rod in her LEFT hand, scraper in her RIGHT, until she sets them down at 7s; no lighter, no matches. WRONG if the tools swap hands.
5. NO MUSIC — only the forest and her work. WRONG if any music or tone plays.
6. ONE continuous take — WRONG if the camera cuts.

TIMELINE — ONE continuous take, no cuts, already in progress at the first frame:
BEAT 1 (0–3s) — MS, 47°, camera kneeling across the cold pit: mid-strike — the rod in her LEFT hand, tip planted in the nest, pulled back against the scraper held still in her RIGHT; a thin spray of sparks dies on the grass. Second strike at 2s: a wisp of smoke, gone. The pit stays dark, no flame; she is lit only by the cold moon edge and the spark flashes.
BEAT 2 (3–7s) — she packs the springy fibres tighter with two fingers, re-plants the rod, holds her breath and strikes hard at 5s: a dense white-orange shower bounces into the nest; at 6s one spot glows orange, a thread of white smoke rises; her eyes lock on it. Still no flame.
BEAT 3 (7–11s) — she lays rod and scraper on a stone, lifts the smouldering nest in cupped hands to 15 cm from her mouth and blows long and slow; the ember brightens with each breath; smoke thickens between her fingers, her eyes narrow, she turns aside for air, blows again; at 10s the nest bursts into a hand-sized flame in her palms.
BEAT 4 (11–15s) — she sets the burning nest into the base of the twig teepee and pulls her hands back from the heat; the thinnest twigs catch one by one, crackling; flames stay below 30 cm; her eyes check which twigs caught, her right hand reaches for one more twig from the pile by her knee. Hard end mid-reach.

ACTING — THE WOMAN (fully invested in the tactic; the work happens in the eyes)
SCENE DIRECTION (unspoken): keep it an ordinary evening chore.
EVENT: the fire takes — and she is already feeding it the next twig.
MOTIVE: alone, the dark complete beyond a few metres; hurrying would cost her the tinder.
GOAL: a flame in the kindling before this nest is used up.
OBSTACLE: the first sparks die, the nest's core is slightly damp, every failed strike tears fibres away.
TACTIC: coax the fire — aim each strike at the densest fibres, then feed the ember with her breath, measuring each breath against the smoke.
MOMENT TO MOMENT: — [0–3s] watches where the sparks die, changes the rod's angle — [3–7s] measures the fibres; on the hard strike, locks on the glowing spot — [7–11s] watches the ember answer each breath — [11–15s] checks which twigs caught, looks to the pile.
LIVING EYES: pupils jump to the sparks, settle, drift to the smoke, settle again; blinks uneven, a hard double blink when smoke reaches her eyes; brows, cheeks and mouth work independently, slight asymmetry. Involuntary detail: she holds her breath through the hard strike and lets it out through her nose when the ember glows. The flame reflects as a small live point in each eye — fine; a FROZEN PUPIL is wrong.
NOT: fixed stare into nothing, looking into the lens, smiling at the fire, a wistful face, posing.

CAMERA — quiet handheld documentary, the operator kneeling on the far side of the pit, lens 60 cm above the ground, 1.8 m from her, about 35° off her eyeline to her left.
MOVEMENT: the camera DOES NOT TRAVEL — it stays put and breathes, reframing a beat late as she lifts the nest and sets it down.
OPTICS: MS at 47° for the whole take — natural perspective, hands, nest and face in one frame, trunks behind her soft; no lens drift.
FOCUS: her hands and the nest; rides the nest up to her face at 7s and back down at 11s.
HORIZON: a degree or two off level, drifting.
NOT: gimbal, drone, tripod lock, push-in, zoom, orbit, slow motion.

GEOMETRY — she kneels at the far side of the pit, screen-right third, torso leaning over it at about 30°, face 50–60 cm above the nest; the 50 cm ring of stones in the lower-left third; spare twigs by her right knee; nearest trunk 2 m behind her; beyond 3 m, darkness.

PHYSICS & MATERIAL — the scraper bites the rod with a dry rasp; sparks fall with gravity and die in under a second; the nest is springy and pushes back against her fingers. FIRE — START (0–6s): no flame, no glow, sparks only. DURING (6–10s): one coin-sized ember that brightens with each breath and dulls between; smoke from a thin white thread to thick grey-white, pulled sideways by a faint draught. END (10–15s): the nest flares suddenly; thin twigs catch one by one, bark curling; the fire stays small. A loose strand of hair falls forward; she tilts her head to keep it from the flame. Nothing floats, nothing loops. OVER-REAL: grime in her knuckle creases and under her nails, a soot smudge on her right thumb, the rod scored bright where it has been struck, damp moss in the cracks of the stones, dry leaf litter under her knee, frayed cuffs. If any surface looks clean, smooth, plastic, CGI or rendered — WRONG.

LIGHT — MOTIVATED LIGHT ONLY, night, COLD, THEN FIRE (KEY):
SOURCE: before the fire, a weak cold moon ambience ~8000 K through the canopy, high behind her frame-right — a faint silver edge on her hair, right shoulder and the stones; each spark shower flashes on her hands and the underside of her face for a fraction of a second. From 6s the ember adds a tiny orange glow (~1800 K) on fingertips and chin; from 10s the small flame is the key, low and in front of her, ~1900 K, a restless flicker on the underside and camera-facing side of her face.
REACH: the firelight dies within 2–3 metres; beyond, cold blue-black forest.
EXPOSURE: exposed for her hands and face in whatever light exists each second — in the first 6 s she is dim but readable, never brightened by an invisible lamp. Shadows deep but breathing, never crushed; even exposure corner to corner, NO vignette.
CONTINUITY: moon behind her frame-right, fire low in the lower-left; lit sides never flip.
NOT: studio light, softbox, frontal key, beauty fill, headlamp, flashlight, lantern, bright moon, blue wash, god rays, flat even light, warm light before the fire exists, HDR glow.

FILM LOOK (KEY — reproduce this exact photographic character): real 35mm film, 500-speed tungsten stock pushed one stop; low-key; cold desaturated blue-grey forest against warm amber firelight on skin, fibres and stones, both muted, never teal-and-orange; sparks and flame bloom with gentle halation; fine moving grain, heavier in the dark; real skin with pores and fine lines. Spherical lens character, gentle focus falloff — NOT over-sharpened, NOT HDR, NOT digital-clean, NOT a render.
NO LENS FLARES: no flares, no light streaks, no floating bokeh orbs, no glow overlays; sparks and flame stay small and contained.

SOUND — DIEGETIC ONLY, dirty-real location sound: the dry metallic rasp of the scraper at about 1s and 2s, a harder one at 5s; sparks fizzing out in the grass; her held breath released through the nose at 6s; long controlled blowing, air hissing through the fibres; a soft whoosh as the nest flares at 10s; thin twigs crackling as they catch; her knee on dry leaves; leaves overhead in a light wind; sparse, irregular insects far off — not a rhythm; one night bird far away at about 4s. No voice, no humming. NO music, NO score, NO BGM, NO instrumental, NO melody, NO synth, NO ambient pad, NO drone, NO swell, NO chimes.

NEGATIVE: fire burning in the first frame, flames or embers before 6s, fire appearing full-size, bonfire, a flame on the first strike, lighter, matches, studio light, softbox, frontal fill, evenly lit face, beauty light, background music, score, humming tones, tools in the wrong hands, a second person, glassy stare, frozen pupils, doll eyes, doll face, looking into the lens, serene smile, porcelain skin, makeup, beauty retouching, daylight, flat even light, orange light filling the frame, uplight glow, lens flare, HDR glow, milky blacks, crushed blacks, vignette, CGI flames, CGI sparks, looping fire, centred symmetrical framing, plastic skin, clean new clothing, floaty motion, slow motion, cuts, subtitles, captions, on-screen text, watermark, gimbal, drone, over-sharpened, clean 4K, 3D render, warped hands, extra fingers, wrong aspect ratio.

[ORDER: ONE continuous take, 15s, breathing handheld, MS 47° — (0–3s) two weak strikes, sparks die, the pit stays dark — (3–7s) she packs the nest, holds her breath, hard strike, one spot glows — (7–11s) she lifts the nest and blows, smoke, the flame bursts at 10s — (11–15s) into the twigs, the thin twigs catch, she reaches for one more — hard end mid-reach. Invariants: no flame or glow before 6s, the fire grows from an ember; only moonlight, sparks and the growing fire light her; her eyes follow the sparks and smoke, never the lens; rod LEFT hand, scraper RIGHT. Look: 35mm, cold forest against warm fire, fine grain, no vignette. Nobody speaks. NO music, NO subtitles.]
```

## Generation card

```
GENERATION CARD
Model: Seedance 2.5 · Task: text-to-video
Duration: 15s (= timeline) · Aspect: 16:9 · Resolution: draft 480p → final 1080p (no 4K on 2.5) · Audio: on
Attach in this order: nothing (text only)
Notes: draft first. The risk most likely to fail is fire or glow before 6s and a frontal fill in the
first seconds. Check those two before paying for 1080p. On Higgsfield: seedance_2_5, bitrate_mode high
(same credits).
```

## O que conferir no draft (nesta ordem)

1. **Frame 1:** círculo de pedras frio e escuro, sem chama e sem brilho. A brasa só aparece por volta de 6s e a chama por volta de 10s.
2. **Luz nos primeiros 6s:** ela escura, só com a borda fria da lua e o clarão das faíscas. Se o rosto aparece iluminado de frente, a luz falhou.
3. **Olhos:** a pupila acompanha a faísca e a fumaça, as piscadas são irregulares e ela nunca olha pra lente.
4. **Som:** o raspar do bastão, o sopro e o estalo, sem nenhuma música.
5. **Mãos:** bastão na esquerda, raspador na direita.

Se tudo bater, finalize o **mesmo draft** em 1080p sem reenviar prompt nem arquivos.

## Se ainda falhar (do mais barato pro mais caro)

- **O take ficou bom, mas sobrou música** → edição de áudio desse take:
  `Edit Video 1: remove the background music from the whole clip; keep the scraper strikes, the blowing, the crackle, the forest sounds and every other sound exactly as they are; the picture stays unchanged.`
- **O fogo continua aparecendo cedo** → crie uma imagem parada do primeiro frame (ela ajoelhada diante do círculo de pedras frio, bastão e raspador na mão, sem fogo) e anexe como primeiro frame. A tarefa vira first-frame e o aspecto fica adaptativo, então gere a imagem já em 16:9. Cole este bloco logo depois do CONTRACT e não mexa no resto:
  `REFERENCES — @Image 1 — FIRST FRAME: the take STARTS from this exact frame (the woman kneeling at a cold, unlit ring of stones, rod in her left hand, scraper in her right, no fire anywhere) and comes alive from it.`
- **Fogo e luz certos, mas o olhar ainda vidrado** → regenere usando um frame bom do novo take como keyframe e mexa só no bloco ACTING. Se o olhar vidrado continuar, esconda mais os olhos: no BEAT 3, a fumaça passa entre a lente e o rosto e ela sopra de perfil. O trabalho fica na boca, no queixo e na respiração.
