---
name: "project-sertao"
description: "Project skill (bible) for CABRESTO (working title), an 8-minute live-action short in 21:9 (2.39) generated entirely with Seedance 2.5 on Higgsfield. Sertão of Paraíba, 1958, the great drought: the old cowhand Seu Damião and his teenage son Zé drive the last six head of cattle three days to an açude that may be dry, while the father hides that he is going blind. Use whenever writing or revising a video prompt, shot, scene, voice line or asset for this film, including any request mentioning Damião, Zé, the horse Tição, the cow Estrela, the cabresto, the chocalho, the cabaça, the binga, the caatinga, the lajedo, the rio seco, the cacimba, the juazeiro, the pouso, the açude, vaqueiro, aboio or o curta do sertão. Holds the verbatim look templates, the @TAG registry, cast and voice locks, props with their functions, world rules, project negatives and anti-AI-tell rules, reference prompts, the script and the director's statement. Always used together with cineoro-director."
---

# CABRESTO — PROJECT SKILL

**Bible v1 — 2026-10-09** · status: *a testar* (ver §11 — os templates congelam na v1.1, depois do
teste em três tipos de cena).

*Cabresto: a corda de couro cru com que se amarra e se puxa um cavalo. No começo do filme o pai o
coloca no escuro, de cor; no fim o filho o usa para levar o pai.*

Curta de ~8 minutos, 21:9 (2.39), **todo quadro gerado** no Seedance 2.5 pelo Higgsfield, com voz,
efeitos e ambiente gerados no mesmo passe. Os personagens falam em cena, em português do sertão da
Paraíba, poucas falas; não há dublagem nem narração. A promessa técnica que importa mais: **a cegueira
de Seu Damião nunca é "atuada" pela máquina** — ela só existe no comportamento (a mão que fecha no ar,
o olhar que chega atrasado e pousa um palmo ao lado) até o último fim de tarde, quando o sol baixo entra
por baixo da aba do chapéu.

## Como usar esta skill

Para qualquer plano, cena ou geração deste filme, nesta ordem:
1. **Cabeçalho em linguagem simples primeiro** — o que acontece, o que se diz, quanto dura cada beat,
   como termina. Quatro linhas. Se não cabe ali, o plano ainda não está desenhado.
2. **Escreva o prompt no spine CINEORO** (`cineoro-director`), colando os templates desta skill
   **verbatim** (§1.3) e usando só as tags do registro (§1.2). A geração está mapeada em
   `references/script.md` (G01–G23): comece pela linha dela.
3. **Parta do prompt de referência do tipo de cena** (§4 e `references/reference-prompts.md`) — copie e
   troque os detalhes; não escreva do zero.
4. **Confira** contra as regras anti-IA do projeto (§2) e acrescente os negativos do projeto (§5).

Regra de idioma: **o prompt é em inglês; as falas ficam em português nordestino, na ortografia
nativa, nunca traduzidas nem romanizadas dentro do prompt.** Cabeçalho e cartão de geração em
português.

Tamanho: os templates fixos somam ~750 palavras. Os três prompts de referência já passaram pelo passe
de compressão e ficam em **~2.700 (20–25 s) a ~3.000 palavras (30 s, dois rostos falando)** — acima da
faixa usual de 1.000–2.000 do `cineoro-director`, no teto do que segurou em produção no Higgsfield
(~3.000). Inserts e escalas usam a variante mínima (~1.000). Se um prompt passar de ~3.000, rode de
novo o passe de compressão — mas **nunca** encurte um template: corte no texto do plano.

## As ferramentas

**Higgsfield · Seedance 2.5** (`seedance_2_5`) — todo vídeo e toda fala; t2v ou omni-reference;
21:9; draft 480p → final 1080p (2206×946); áudio ligado; `bitrate_mode` high. **Claude + esta skill +
cineoro-director** — todo prompt. **Previz** (Blender, opcional) — só se a geometria do lajedo ou do
açude der problema. **Modelo de imagem** à escolha — assets (`references/asset-registry.md`).

## O ponto do projeto

Não é fotorrealismo — isso a máquina já resolve. É **crença no comportamento**: o espectador tem de
acreditar em como um vaqueiro velho põe um cabresto sem luz, como um menino cava uma cacimba no leito
seco, como se raciona água numa cabaça, como seis cabeças de gado magro seguem um chocalho, como um
homem que não quer ser cego monta, procura, disfarça. E tem de acreditar no mundo: a caatinga cinza de
1958, sem plástico, sem moto, sem forró. Tudo neste arquivo serve a isso.

---

# 1 · O PROMPT

## 1.1 Spine e blocos sempre ligados

O spine CINEORO (CONTRACT → REFERENCES → WHO IS WHO → SCENE & SOUL → LOCKS → TIMELINE → DIALOGUE →
ACTING → CAMERA → GEOMETRY → PHYSICS & MATERIAL → LIGHT → FILM LOOK + LENS LOOK + NO LENS FLARES →
SOUND → WORLD → NEGATIVE → ORDER). Neste filme ficam **sempre ligados**: **WHO IS WHO** (há sempre
animais — a contagem de seis vive ali), **GEOMETRY** (a formação da coluna, §1.3), **WORLD** e
**SOUND** com o chocalho. DIALOGUE e VOICE LOCK só quando há fala; nesse caso o VOICE LOCK é colado
inteiro.

**Todo prompt é uma ilha.** Luz, ótica, figurino, arreio, contagem do gado, voz e geometria são
reespecificados em todo prompt. "Igual ao plano anterior" é uma instrução para algo que não tem
*antes*.

## 1.2 Nomes — o registro @TAG

```
PERSONAGENS  @DAMIAO  @DAMIAO_POUSO  @DAMIAO_D3  @ZE
ANIMAIS      @TICAO  @ESTRELA  @GADO
OBJETOS      @CABRESTO  @CHOCALHO  @CABACA  @BINGA  @FUMO  @PEIXEIRA  @VARA  @MATULAO  @COURO
LUGARES      @CURRAL_MADRUGADA  @CAATINGA_DIA  @CAATINGA_TARDE  @RIO_SECO_DIA  @JUAZEIRO_DIA
             @POUSO1_NOITE  @POUSO2_NOITE  @LAJEDO_TARDE  @ACUDE_TARDE
VOZES        @DAMIAO_VOICE  @DAMIAO_ABOIO  @ZE_VOICE
```
Um elemento, um nome — idêntico no asset, no prompt, na tabela e no nome do Element no Higgsfield
(salve o Element como `DAMIAO`, `ZE`, `TICAO`, `ESTRELA`, sem @; no prompt, mencione com @). Mudança de
estado = **tag nova** (`@DAMIAO_D3`), nunca sobrescrever. Nunca ponha no prompt uma tag de algo que não
está no plano — a máquina força o elemento a aparecer. Registro completo, descritores e prompts de
imagem: `references/asset-registry.md`.

## 1.3 Templates verbatim — colar, nunca reescrever

Só mudam os campos marcados `{ASSIM}`, escolhendo uma das opções escritas. **Único ajuste permitido
dentro de um template:** trocar `@DAMIAO` pela tag do estado em uso (`@DAMIAO_D3` no dia 3,
`@DAMIAO_POUSO` à noite — o L4 já vem com ela). Todo o resto é colado letra por letra. Os blocos
marcados **KEY** são os que seguram o filme de pé através de centenas de gerações.

**CONTRACT — padrão da linha:**
```
CONTRACT — Live-action photoreal film footage, 21:9, {N} seconds total, {N shots with N hard cuts at
Ns, Ns / ONE continuous take, no cuts}, observational handheld at walking height, documentary,
real-time motion, {dialogue as spoken on-camera audio in Brazilian Portuguese with native rural
Paraíba sertão (nordestino) accents / no dialogue}. NO music, NO score, NO subtitles, NO on-screen
text.
```

**FILM LOOK (KEY):**
```
FILM LOOK (KEY — reproduce this exact photographic character): real 35mm colour negative, 250-speed
daylight stock, printed down — MID-KEY by day, NOT underexposed, NO crushed blacks; LOW-KEY by night,
only what the fire reaches. The palette of drought: bleached bone-white earth, ash-grey branches, ochre
dust, sun-darkened leather and skin; the sky white-hot and colourless near the sun, never saturated,
never cloudy; at night fire-amber skin against blue-black. Muted and dry — never teal-and-orange, never
a yellow or sepia tint. Highlights roll off into white with gentle halation; shadows dense but
detailed, lifted by ground bounce; moderate organic MOVING grain, most visible in the sky and under the
hat brims; softer than digital; real skin with pores, sun damage and dust in the creases; even
exposure to all four corners, NO vignette. NOT a render, NOT CGI, NOT digital-clean, NOT HDR.
```

**LENS LOOK (KEY):**
```
LENS LOOK (KEY): 2.39:1 spherical 35mm lens character — round soft bokeh, natural perspective, deep
focus in the wides with the far scrub dissolving into heat shimmer, shallow focus with a gentle
falloff in the close-ups, mild focus breathing; no anamorphic oval bokeh, no streaks — NOT
over-sharpened, NOT a crisp AI look.
```

**NO LENS FLARES:**
```
NO LENS FLARES: no flares, no light streaks, no floating bokeh orbs, no glow overlays, no sun disc in
frame; every light source stays small and contained within itself.
```

**LIGHT — L1 MADRUGADA** (G01–G03):
```
LIGHT — NATURAL LIGHT ONLY, pre-dawn, COLD & DIM (KEY): the only light is the pale band of sky low on
frame-LEFT before sunrise, ~9000 K, soft and shadowless; NO lamp, NO fire, NO moon. Shapes read as
silhouettes against it; faces and hands dim but readable on the sky side, the far side blue-black.
Low mid-key, exposed for the sky side of faces and hands; shadows deep but breathing, never crushed;
even exposure, NO vignette. The sky band stays frame-left in every shot; lit sides never flip. NOT:
sun disc, orange or pink sunrise, golden light, stars, moon, lantern, flat light, day-for-night blue
wash.
```

**LIGHT — L2 DIA (sol duro)** (manhã e meio-dia dos três dias):
```
LIGHT — NATURAL LIGHT ONLY, drought day, HARD & WHITE (KEY): the only key is the hard sun, ~5600 K,
{MIDDAY: high, nearly overhead, slightly in front of the camera / MORNING: low-to-mid, behind the
travellers on frame-left}; the pale ground and rock bounce warm light into every shadow. Short hard
shadows; the hat brims throw dense shade over the eyes down to the cheekbones — eyes readable only
inside that shade, by the bounce; heat shimmer beyond 30 m. Exposed for sunlit skin and leather; the
sky near the sun rolls off to white, never a flat blown block; shadows dense but detailed, never
crushed, never milky; even exposure, NO vignette. The sun keeps its side in every shot and never
enters the frame; lit sides never flip. NOT: golden hour, beauty light, overcast softness, clouds,
saturated blue sky, sunbeams, fill-reflector look, HDR.
```

**LIGHT — L3 SOL BAIXO** (só o fim de tarde do dia 3, G19–G23 — a luz que entrega):
```
LIGHT — NATURAL LIGHT ONLY, late afternoon of drought, LOW & RAKING (KEY): the only key is the low
sun, ~3800 K, about 10° above the horizon on frame-RIGHT, ahead of the travellers, always outside the
frame; warm bounce from the pale ground; the sky on frame-left a pale dusty blue-grey. The sun comes in
UNDER the hat brims: faces turned toward frame-right are lit full, eyes included; everything turned
away gets a warm rim; long shadows stretch toward frame-left. Exposed for the faces turned into the
sun; their far side in soft warm shade, readable; shadows deep but breathing; even exposure, NO
vignette. The sun stays low on frame-right in every shot; lit sides never flip. NOT: sun disc in
frame, sunset postcard, orange-pink sky, golden glow on everything, sunbeams, flat light.
```

**LIGHT — L4 FOGO** (os dois pousos, G08, G09, G15):
```
LIGHT — MOTIVATED LIGHT ONLY, moonless night, DIM & WARM-ON-COLD (KEY): the only key is a small fire
of dry branches on bare ground, knee-high flames, ~1900 K, between the two men, low in frame or just
below the bottom edge; a faint cold sky glow ~10000 K only on the tops of the scrub. The fire paints a
restless warm flicker on the fire-facing side of faces and hands and dies within three metres; beyond
it, blue-black; the sky deep blue-black with no visible detail. Exposed for the fire-lit faces; their
far side in deep shadow; shadows breathing, never crushed; even exposure, NO vignette. @DAMIAO_POUSO
always frame-LEFT of the fire, @ZE always frame-RIGHT; the lit side of each face never flips. NOT:
daylight, moonlight, a lantern, a second warm source, flat light, beauty fill, star field, Milky Way,
milky blacks, orange light filling the frame.
```

**GEOMETRY — as três formações da coluna** (a formação diz quem guia; ver §10):
```
GEOMETRY — FORMATION A (the father leads): the column moves frame-LEFT → frame-RIGHT on a pale stony
trail 1.5 m wide: @DAMIAO on @TICAO at the head (frame-right); @ESTRELA 3 m behind the horse; the
other five head in a loose single file 1–2 m apart behind her; @ZE on foot 4 m behind the last head
(frame-left), stick in his RIGHT hand. Camera on the near side of the trail, 2–8 m from the column, at
@ZE's eye height (1.5 m) unless a shot says otherwise — looking up about 15° at the mounted father
(his eyes at 2.3 m). Beyond 40 m, heat shimmer. The camera never crosses to the far side of the trail.
```
```
GEOMETRY — FORMATION B (the son leads the herd): the column moves frame-LEFT → frame-RIGHT on a pale
stony trail 1.5 m wide: @ZE on foot at the head (frame-right), stick in his RIGHT hand; @ESTRELA 2 m
behind him; the other five head in a loose single file 1–2 m apart behind her; @DAMIAO on @TICAO at
the tail, 4 m behind the last head (frame-left). Camera on the near side of the trail, 2–8 m from the
column, at @ZE's eye height (1.5 m) unless a shot says otherwise. Beyond 40 m, heat shimmer. The camera
never crosses to the far side of the trail.
```
```
GEOMETRY — FORMATION C (the son leads the father): the column moves frame-LEFT → frame-RIGHT: @ZE on
foot at the head (frame-right), one step ahead of @TICAO's head on the camera side of the horse, the
lead rope of @CABRESTO in his LEFT hand 40 cm below the horse's jaw, the slack coiled in his RIGHT;
@DAMIAO mounted, reins knotted on the horse's neck, both hands on the saddle front; @ESTRELA 3 m behind
the horse; the other five in a loose file behind her. Camera on the near side of the trail at
@DAMIAO's eye height (about 2.2 m, the operator on raised ground or rock) unless a shot says otherwise.
The camera never crosses to the far side of the trail.
```

**WORLD:**
```
WORLD — the sertão of Paraíba, Brazil, 1958, the great drought: grey leafless thorn scrub (jurema,
catingueira), mandacaru and xique-xique cacti, cracked ochre earth, granite outcrops, dry white-sand
riverbeds; the juazeiro is the only green tree; everything is leather, rawhide, cotton, straw, gourd,
clay, wood or hand-forged iron. NO plastic, NO synthetic fabric, NO rubber, NO zippers, NO jeans, NO
watch, NO glasses, NO firearms, NO motor vehicles, NO roads, NO power lines, NO wind turbines, NO water
tanks, NO wire fences, NO other people, NO dogs, NO goats. Water is rationed from gourds; the cattle
are driven by voice and the lead cow's bell, never by a whip.
```

**Espinha NEGATIVE do projeto** (vai no fim de todo NEGATIVE, depois das falhas do plano e do tipo de
cena; tire só o que o plano realmente quer; os anacronismos já estão cercados no WORLD e não se
repetem aqui):
```
centred symmetrical framing, flat even light, beauty light, milky blacks, crushed blacks, vignette,
golden-hour postcard, saturated blue sky, clouds, teal-and-orange, yellow or sepia tint, HDR, lens
flare, sun disc in frame, plastic skin, waxy skin, beauty retouching, clean faces, clean new leather,
clean clothing, doll face, glassy stare, frozen pupils, glowing eyes, white or opaque eyes, zombie
eyes, looking into the lens, cowboy hat, Stetson, cangaceiro half-moon hat, metal stars, cartridge
belts, humped zebu cattle, dairy cattle, fat glossy cattle, more than six cattle, duplicated cattle,
twins, clones, extra people, warped hands, extra fingers, extra legs or hooves, floaty motion, looping
motion, tripod-locked camera, gimbal, stabilized footage, drone, aerial, crane, zoom, slow motion,
over-sharpened, CGI, 3D render, subtitles, captions, on-screen text, watermark, logo, music, score,
BGM, instrumental, melody, accordion, zabumba, triangle, viola, guitar, fiddle, fife, choir, ambient
pad, drone tone, swell, chimes, wrong aspect ratio
```

*Nota de artefato: se a máquina devolver banding ou ghosting, não acrescente "gate weave" nem
"chromatic aberration" ao look; mantenha o grão moderado e some "NO digital artifacts, NO compression
trails, NO ghosting streaks".*

## 1.4 Lista mestre de objetos

Os três objetos que carregam mais do que eles mesmos — **travados com mais força** e descritos em
WHO IS WHO sempre que estão em quadro — são **@CABRESTO, @CHOCALHO e @CABACA**.

- **@CABRESTO** ★ — cabresto de couro cru trançado, castanho-claro acinzentado de suor e idade, trança
  chata de ~1,5 cm: focinheira, tira atrás das orelhas, nó feito à mão sob o queixo com uma argola de
  couro torcido; da argola sai uma corda de couro cru em trança redonda, grossa como um dedo, 3 m,
  enrolada em quatro voltas e amarrada na frente da sela. Vai **por baixo do freio**, sempre no
  @TICAO. Função: amarrar o cavalo à noite e puxá-lo a pé. O pai o coloca de cor, no escuro (G01); o
  filho leva o pai por ele (G20–G23). Nunca de náilon, nunca um cabresto de corda americano.
  *Fallback:* se a trança derivar, "a rough twisted rawhide rope halter".
- **@CHOCALHO** ★ — chocalho de ferro batido, ferrugem e preto, trapezoidal, ~15 cm, aberto embaixo,
  badalo de ferro, pendurado numa coleira de couro cru sob o pescoço da @ESTRELA. Som: um *toc* oco e
  surdo a cada passo, nunca um *plim*. Função: o gado segue o chocalho — e o pai se guia por ele. É a
  bússola do filme; o som está em toda cena de dia. *Fallback:* se vier sino suíço, "a flat dark iron
  box-bell, like a small rusted can".
- **@CABACA** ★ — cabaça seca de ~30 cm, castanho-clara com pátina escura, rolha de sabugo de milho,
  cordão de fibra no gargalo amarrado à frente da sela, lado direito (lado da câmera). A ração de água.
  **Paga três vezes:** G06 (a mão fecha no ar, Zé não vê), G16 (o pai recusa), G19 (Zé vê).
- **@BINGA** — isqueiro de pederneira: fuzil de aço do tamanho da palma, lasca de pedra cinza, pavio de
  algodão num canudo de chifre; riscado para baixo, solta faísca, o pavio pega uma **brasa** (não
  chama). No bolso da camisa do Damião. Função: acender o cigarro de palha (G08). Nunca isqueiro
  moderno, nunca fósforo.
- **@FUMO** — fumo de rolo escuro e palhas de milho num saquinho de pano; cortado com a peixeira contra
  o polegar, esfarelado na palma, enrolado na palha, lambido, torcido.
- **@PEIXEIRA** — faca de lâmina longa e fina, cabo de madeira gasto, bainha de couro enfiada no cinto
  nas costas, cabo para a direita. Corta fumo, corda, carne-de-sol.
- **@VARA** — vara de tanger do Zé: galho de jurema descascado, 1,5 m, grosso como um polegar,
  cinza-claro, um nó perto da ponta; sempre na mão DIREITA dele; toca o flanco, nunca bate.
- **@MATULAO** — saco de algodão com farinha, rapadura e carne-de-sol, amarrado atrás da sela.
- **@COURO** — couro de boi seco, pelo para cima, a cama do Zé no chão.
- Parte do figurino/arreio (não têm tag própria; vêm com @DAMIAO e @TICAO): o chapéu de couro, o gibão,
  as perneiras, a sela vaqueira com estribos de ferro. Geometria do chapéu em §2, regra 5.

---

# 2 · REGRAS ANTI-IA DO PROJETO

> Realismo é o que se subtrai, não o que se acrescenta.

Regras v1 são **preventivas** (previstas pela leitura, ainda não observadas em take). Cada falha real
vira regra nova, com o sintoma, a correção que funcionou e a data. O catálogo geral está em
`cineoro-realism`.

1. **Nunca escreva "blind", "cataract" nem "cego" no prompt** (2026-10-09, preventiva). A palavra puxa
   olho branco de terror ou um "cego de filme" tateando. Descreva a geometria, só quando o olho aparece
   (G19): `in the centre of both pupils a faint milky grey haze, like breath on glass; the dark brown
   irises clear around it`. Negativo: `white or opaque eyes, zombie eyes, glowing eyes, blank stare`.
2. **A cegueira nunca é atuada** (2026-10-09). Damião nunca tateia, nunca abana a mão diante do rosto,
   nunca fica de olhar fixo. Ele age como quem vê: vira a cabeça para o som, o olhar chega um tempo
   atrasado e pousa **um palmo ao lado** do alvo, a mão erra por um palmo e acha no segundo toque.
   Colar: `his eyes keep moving toward sounds, arrive a beat late and settle a palm's width beside the
   target; he never gropes, never waves a hand in front of his face, never stares blankly`.
3. **Seis cabeças, contadas** (2026-10-09). A máquina multiplica gado. Toda geração com a coluna diz
   `exactly SIX head of cattle … SIX, never more` em WHO IS WHO, nas LOCKS, no NEGATIVE (`more than six
   cattle, duplicated cattle`) e no ORDER.
4. **Gado magro, mas vivo** (2026-10-09). Nem gado gordo de exposição, nem carcaça ambulante de horror:
   `ribs and hip bones showing, alive and walking`. Raça: gado pequeno do sertão (pé-duro), chifres
   médios; nunca zebu branco de cupim, nunca holandês malhado.
5. **O chapéu de couro tem geometria** (2026-10-09). Nos assets e, se derivar, no prompt: `a stiff hat
   of brown cured leather, low rounded crown with stitched seams, short stiff brim flat at the front
   and slightly turned up at the sides and back, a thin leather chin strap`. Negativo: `cowboy hat,
   Stetson, cangaceiro half-moon hat, metal stars`.
6. **O aboio não pode virar música** (2026-10-09). A máquina transforma canto em canção com
   acompanhamento — e "Nordeste" puxa forró. O aboio é uma **fala** com segundos, escrita como física da
   voz (§3), e o NEGATIVE leva `accordion, zabumba, triangle, viola, guitar, fiddle, fife, choir`.
7. **Céu de seca é branco e sem nuvem** (2026-10-09). Nunca céu azul saturado com nuvens de
   cartão-postal.
8. **Nada limpo** (2026-10-09). Poeira nas rugas e na barba, linhas de sal secas na camisa do Zé, couro
   arranhado de branco pelos espinhos, lábios rachados no dia 3. Couro novo, roupa limpa = errado.
9. **Mãos de montaria travadas** (2026-10-09). Damião segura as rédeas na mão ESQUERDA; a direita é a
   livre — a que procura, a que erra, a que pega a cabaça (e é a que tem a ponta do indicador faltando).
   Zé leva a @VARA na DIREITA; no fim, a corda do cabresto na ESQUERDA.
10. **Sem ponto de vista do cego** (2026-10-09). Nunca um plano subjetivo com a visão embaçada do pai,
    nunca desfoque "de catarata". O filme é observado de fora, do lado do Zé.
11. **Chocalho é ferro, não sino** (2026-10-09). Som surdo e oco; nunca tilintar, nunca "chimes".
12. **Calor visível só ao longe** (2026-10-09). Tremor de calor a partir de 30 m; nunca distorção
    digital passando sobre rostos.

---

# 3 · VOZES E PRONÚNCIA

Português do Brasil, **sotaque rural do sertão da Paraíba**, 1958. Dizer a variedade e a região no
CONTRACT **e** em cada fala. Ortografia nativa com acentos; a gramática rural vai escrita ("Dois dia",
"os urubu", "num" por "não", "tu" com verbo na 3ª pessoa: "Vai tu na frente"), mas **não** se
reescreve foneticamente cada "r" caído — o rótulo de sotaque faz isso. Falas curtas, nunca nos
últimos 1–2 s da geração. Uma nota de emoção por fala, nunca por palavra. Nunca repetir as palavras do
diálogo em outro bloco do prompt (convida legenda).

Notas de pronúncia: "num" — nasal e curto, quase "nũ"; "Esse sol…" — o "l" final quase "u"; "urubu"
com acento no último "bu"; "Tô", "Tá" fechados.

```
VOICE LOCK — @DAMIAO: man in his late sixties, untrained, low chest voice, dry and rasping from sun
and tobacco, short of breath; few words, slow, flat certainty, the last syllable dropped into the
exhale; never raised except in the herding call; never sentimental, never trembling; native rural
Paraíba sertão accent, open nasal vowels. Never a radio voice, never a theatrical old-man quaver.

VOICE LOCK — @ZE: 15-year-old boy mid voice-change, untrained, light and uneven — it cracks upward on
stressed syllables; quick and quiet with his father, word endings half-swallowed, a little hoarse
from dust; the same rural Paraíba sertão accent as his father. Never a child's piping voice, never a
settled adult baritone.

HERDING CALL — @DAMIAO: a long wordless herding call from the chest, open vowels "Êêê boi… êêê… ôôô…",
one phrase per breath, rising, held, falling away, rough, cracking slightly at the top; outdoors, dry,
no reverb; sung by the man on camera, mouth open on the vowels — NOT music, NO instruments, NO
accompaniment.

HERDING CALL — @ZE: the same call, thinner — it starts too high, breaks in the middle, stops,
restarts lower and holds; mouth open on the vowels — NOT music, NO instruments.
```
Nos estados (`@DAMIAO_POUSO`, `@DAMIAO_D3`) o VOICE LOCK é o mesmo texto, só com o rótulo da tag do
estado — a voz não muda com o estado. As duas vozes diferem em três eixos: registro (peito grave ×
muda instável), textura (rouca e seca × leve e falhando), andamento (lento × rápido e engolido).

Referências de áudio: ainda não existem. Do primeiro take aprovado com fala de cada um, cortar 5–10 s
limpos → `@DAMIAO_VOICE`, `@ZE_VOICE`; do primeiro aboio aprovado → `@DAMIAO_ABOIO`. Cada uma ligada a
**um** personagem só ("its only job is this voice; all other sound is generated fresh"). Máximo 30 s
de áudio por geração.

---

# 4 · PROMPTS DE REFERÊNCIA

## 4.1 O prompt-modelo — travessia de dia (G05, "O galho")

O tipo mais comum do filme: a coluna andando sob sol duro, uma falha do pai disfarçada. ~90% das
gerações de travessia começam de uma cópia deste.

**Cabeçalho**
```
O QUE ACONTECE: Meio-dia do primeiro dia. Seu Damião, à frente da coluna, entra a cavalo num galho de
jurema sem se abaixar; os espinhos raspam o gibão e jogam o chapéu para trás; a mão dele erra o galho,
acha no segundo toque, afasta; ele puxa a aba mais para baixo. Zé, lá atrás, levanta os olhos pelo
barulho e volta ao gado.
O QUE SE DIZ: DAMIÃO (resmungado): "Esse sol…"
TEMPO: a coluna andando — 7s · o galho — 7s · Zé e a novilha — 6s = 20s
COMO TERMINA: corte seco no meio de um passo do Zé, a vara acabando de tocar a novilha.
```

**Prompt**
```
CONTRACT — Live-action photoreal film footage, 21:9, 20 seconds total, 3 shots with 2 hard cuts at
7s and 14s, observational handheld at walking height, documentary, real-time motion, dialogue as
spoken on-camera audio in Brazilian Portuguese with native rural Paraíba sertão (nordestino) accents.
NO music, NO score, NO subtitles, NO on-screen text.

REFERENCES — each reference has ONE job:
@DAMIAO — IDENTITY of @DAMIAO: face, hands, build, leather hat, jacket and leggings. 100% matches.
@ZE — IDENTITY of @ZE: face, build, straw hat, patched shirt. 100% matches.
@TICAO — IDENTITY of the horse @TICAO with saddle, bridle and @CABRESTO. 100% matches.
@ESTRELA — IDENTITY of the lead cow @ESTRELA with @CHOCALHO. 100% matches.
@CAATINGA_DIA — WORLD: thorn scrub, stony trail, cracked ground — the world for all three shots.
REFERENCE SCOPE: identity references supply faces, bodies, coats, wardrobe, tack and objects ONLY —
IGNORE their backdrops, ground, sky, lighting direction, exposure and colour grade.

WHO IS WHO — READ FIRST, ABSOLUTE:
@DAMIAO (66, lean, deep sun-cut lines, white stubble, thin grey moustache; stiff brown leather hat
with a chin strap, scuffed leather jacket and leggings; tip of the right index finger missing — 100%
matches its reference) — the OLD COWHAND: rides @TICAO at the head of the column, reins in his LEFT
hand, right hand free; NEVER dismounts, NEVER gropes, NEVER looks into the lens; owns the RIGHT side
of the frame.
@ZE (15, thin, tall for his age, faint first moustache, peeling sun-burned nose; frayed straw hat,
oversized patched cotton shirt, sandals — 100% matches its reference) — the SON: walks at the tail of
the column, stick in his RIGHT hand; NEVER rides, NEVER speaks in this generation, NEVER looks into
the lens; owns the LEFT side of the frame.
ANIMALS: exactly SIX head of cattle — @ESTRELA (old red-brown cow, white star on the forehead, rusted
iron bell on a rawhide collar) first, then five more small thin sertão cattle, each a different dull
coat — dun, brindle, black, cream, red — ribs and hip bones showing, alive and walking; SIX, never
more. @TICAO (small old dark-bay horse, nearly black, grey around the eyes, ribs showing, pale scar on
the right shoulder, unshod; braided rawhide halter under the bridle, its lead rope coiled at the
saddle front).
FACES: each face exists once; no other people; no twins, no clones, no duplicated cattle.
CONTACT: nobody touches anyone in this generation.

SCENE — Midday on the first day of a three-day cattle drive across the drought-struck sertão, 1958:
the column is already moving through grey thorn scrub — the old cowhand on horseback at the head, his
last six head behind him, his son on foot at the tail.
THE SOUL OF THE SCENE (play it, never explain it): the old man can no longer see the branches; he
rides as he has for fifty years and covers every miss before anyone sees it. The boy is too busy
being a good cowhand to look at his father long enough to notice.

ABSOLUTE LOCKS — break one and the take is WRONG, regenerate:
1. Exactly SIX head of cattle in every shot where the column is seen — WRONG if more than six or a
   herd appears.
2. The column moves frame-LEFT → frame-RIGHT in every shot; @DAMIAO at the head (frame-right), @ZE at
   the tail (frame-left) — WRONG if anyone moves the other way or they swap ends.
3. @DAMIAO's eyes stay inside the shade of his hat brim and keep moving toward sounds; he never
   gropes, never stares blankly, never waves a hand before his face — WRONG if he plays a blind man.
4. Reins in @DAMIAO's LEFT hand; only his RIGHT hand finds the branch — WRONG if the hands swap.
5. No music of any kind — the only voice is his two muttered words.

TIMELINE — 3 shots, 2 hard cuts; cuts only at the specified points, the camera adds no cuts of its
own:
SHOT 1 (0–7s) — WS, 63°, camera WALKING 5 m behind @ZE on the near side, at his eye height: @ZE
already walking in the frame-left foreground, three-quarter back, stick in his RIGHT hand; ahead of
him, left to right, the SIX head in a loose single file, the red heifer last, @ESTRELA first, her
bell swinging; at the head, frame-right, @DAMIAO on @TICAO at a walk, small, his eyes in the brim's
shade. Every footfall of the operator lands in the frame. HARD CUT.
SHOT 2 (7–14s) — MS @DAMIAO from below, 47°, camera at hip height 3 m from @TICAO's right shoulder,
looking up 15°, STAYS PUT and breathes as the horse walks in from frame-left: a low branch of dry
thorny jurema crosses the trail at chest height; @DAMIAO rides into it without ducking — the thorns
drag across the leather jacket with a dry scrape and knock the hat back onto its chin strap; @TICAO
stops by himself; @DAMIAO's RIGHT hand comes up a beat late, closes on air a hand's width below the
branch, finds it by touch on the second try and bends it away over his head; the reins stay in his
LEFT hand; he pulls the brim down lower over his eyes; at 11–13s he mutters. HARD CUT.
SHOT 3 (14–20s) — MCU @ZE, 29°, camera WALKING beside him on the near side, 2 m away, half a step
ahead, at his eye height: his eyes come up toward frame-right — his father's back — for one beat,
then drop to the cattle; the red heifer lags; he taps her flank twice with the stick in his RIGHT
hand; she trots one step. Hard end mid-step.

DIALOGUE — only this line is spoken; ON CAMERA, lip-synced; NO dubbing, NO voice-over, NO narration,
NO subtitles, NO on-screen text — the words exist only as sound. Every other mouth stays closed.
[11–13s] @DAMIAO (on camera, Brazilian Portuguese, rural Paraíba sertão accent, muttered to himself,
lips barely parting, the last syllable dropped into the exhale): "Esse sol…"
VOICE LOCK — @DAMIAO: man in his late sixties, untrained, low chest voice, dry and rasping from sun
and tobacco, short of breath; few words, slow, flat certainty, the last syllable dropped into the
exhale; never raised except in the herding call; never sentimental, never trembling; native rural
Paraíba sertão accent, open nasal vowels. Never a radio voice, never a theatrical old-man quaver.
This voice identity is fixed and identical across all shots of the film.

ACTING — @DAMIAO (fully invested in the tactic; the work happens in the eyes)
SCENE DIRECTION (shared, unspoken): an ordinary day of driving cattle — the father leads, the son
follows.
EVENT: the father's first miss on the road, covered before anyone sees it.
MOTIVE: if the boy knows, the boy takes the front — and a cowhand who is led is no longer a cowhand.
GOAL: get the column through the scrub without stopping.
OBSTACLE: he can't see the branch; every miss makes a sound the boy might hear.
TACTIC: ride by memory and by the horse; deal with the branch by hand as if it were routine; give the
miss a reason — the sun.
MOMENT TO MOMENT: — [7–9s] riding easy, head tilted back toward the bell behind him, checking by ear
that the herd follows — [9–10s] the scrape: his body takes it without surprise — [10–11s] the hand
misses, then finds — [11–13s] the mutter, to nobody — [13–14s] the brim pulled lower.
LIVING EYES: under the brim his eyes keep moving toward sounds, arrive a beat late, settle a palm's
width beside the thing; uneven late blinks; narrowed against the glare; involuntary detail: his jaw
sets once after the miss. A frozen pupil or a fixed glassy stare is wrong.
NOT: groping, a blank stare, eyes rolled up, a hand waving before his face, a startled jump, a pained
face, looking into the lens.

ACTING — @ZE
SCENE DIRECTION (shared, unspoken): an ordinary day of driving cattle.
MOTIVE: he wants his father to see him work like a cowhand. GOAL: keep the six together and moving.
OBSTACLE: the heat, tired legs, a heifer that keeps lagging.
TACTIC: drive the stragglers with small exact taps, stealing looks at his father's back for approval.
MOMENT TO MOMENT: — [0–7s] eyes on the hindquarters ahead, counting the six — [14–16s] the scrape
pulls his eyes to his father's back for one beat — [16–20s] back to the heifer; the tap.
LIVING EYES: busy counting; quick saccades; uneven blinks against the dust; involuntary detail: he
wipes the sweat off his upper lip with the back of his left wrist.
NOT: worry, frowning at his father, calling out, smiling, looking into the lens.

CAMERA — observational handheld at walking height, documentary; the operator on foot on the near side
of the trail, 2–5 m from the subjects. MOVEMENT: shot 1 TRAVELS behind @ZE at his pace; shot 2 STAYS
PUT at hip height and breathes while the horse walks in; shot 3 TRAVELS beside @ZE. One movement per
shot. OPTICS: per shot; no lens drift inside a shot. FOCUS: shot 1 on @ZE, breathing out to the
column; shot 2 on @DAMIAO's right hand and the brim; shot 3 on @ZE's eyes. HORIZON: level within 2° —
an ordinary day. NOT: gimbal glide, drone, crane, dolly, zoom, orbit, slow motion, a push into
@DAMIAO's eyes.

GEOMETRY — FORMATION A (the father leads): the column moves frame-LEFT → frame-RIGHT on a pale stony
trail 1.5 m wide: @DAMIAO on @TICAO at the head (frame-right); @ESTRELA 3 m behind the horse; the
other five head in a loose single file 1–2 m apart behind her; @ZE on foot 4 m behind the last head
(frame-left), stick in his RIGHT hand. Camera on the near side of the trail, 2–8 m from the column, at
@ZE's eye height (1.5 m) unless a shot says otherwise — looking up about 15° at the mounted father
(his eyes at 2.3 m). Beyond 40 m, heat shimmer. The camera never crosses to the far side of the trail.

PHYSICS & MATERIAL — the horse's head bobs with each step, unshod hooves clack and slide on loose
stones, the rider's weight sways with the walk; the branch resists, bends and springs back, dry bark
scraping leather; the hat hangs a moment on its strap before he pulls it forward; dust lifts from
every hoof and drifts low in the hot wind; the cattle walk heavily, heads low, hips rocking, skin
sliding over the hip bones; the iron bell swings and knocks dull. Nothing floats, nothing loops.
OVER-REAL: the leather jacket scratched white by thorns and cracked at the elbows; dust in his neck
creases and white stubble; dried salt lines on the boy's shirt; grey thorns with tiny hooked spines;
sweat darkening the horse's coat under the saddle; cracked earth plates at the trail's edge. If any
surface looks clean, smooth, plastic, CGI or rendered — WRONG.

LIGHT — NATURAL LIGHT ONLY, drought day, HARD & WHITE (KEY): the only key is the hard sun, ~5600 K,
high, nearly overhead, slightly in front of the camera; the pale ground and rock bounce warm light
into every shadow. Short hard shadows; the hat brims throw dense shade over the eyes down to the
cheekbones — eyes readable only inside that shade, by the bounce; heat shimmer beyond 30 m. Exposed
for sunlit skin and leather; the sky near the sun rolls off to white, never a flat blown block;
shadows dense but detailed, never crushed, never milky; even exposure, NO vignette. The sun keeps its
side in every shot and never enters the frame; lit sides never flip. NOT: golden hour, beauty light,
overcast softness, clouds, saturated blue sky, sunbeams, fill-reflector look, HDR.

FILM LOOK (KEY — reproduce this exact photographic character): real 35mm colour negative, 250-speed
daylight stock, printed down — MID-KEY by day, NOT underexposed, NO crushed blacks; LOW-KEY by night,
only what the fire reaches. The palette of drought: bleached bone-white earth, ash-grey branches, ochre
dust, sun-darkened leather and skin; the sky white-hot and colourless near the sun, never saturated,
never cloudy; at night fire-amber skin against blue-black. Muted and dry — never teal-and-orange, never
a yellow or sepia tint. Highlights roll off into white with gentle halation; shadows dense but
detailed, lifted by ground bounce; moderate organic MOVING grain, most visible in the sky and under the
hat brims; softer than digital; real skin with pores, sun damage and dust in the creases; even
exposure to all four corners, NO vignette. NOT a render, NOT CGI, NOT digital-clean, NOT HDR.
LENS LOOK (KEY): 2.39:1 spherical 35mm lens character — round soft bokeh, natural perspective, deep
focus in the wides with the far scrub dissolving into heat shimmer, shallow focus with a gentle
falloff in the close-ups, mild focus breathing; no anamorphic oval bokeh, no streaks — NOT
over-sharpened, NOT a crisp AI look.
NO LENS FLARES: no flares, no light streaks, no floating bokeh orbs, no glow overlays, no sun disc in
frame; every light source stays small and contained within itself.

SOUND — DIEGETIC ONLY, dirty-real location sound: cicadas in the scrub, a high dry shrill rising and
falling in waves; the iron bell's dull hollow knock with each of @ESTRELA's steps; unshod hooves on
loose stones; saddle leather creaking; the dry scrape of thorns across leather at 9s and the whip of
the branch springing back at 12s; the cattle's heavy breathing and one hoarse low moo; sandals in the
dust; two taps of the stick on hide at 17s; hot wind in dry branches. After the mutter, only cicadas
and the bell for two seconds. NO music, NO score, NO BGM, NO instrumental, NO melody, NO ambient pad,
NO drone, NO swell, NO chimes, NO reverb.

WORLD — the sertão of Paraíba, Brazil, 1958, the great drought: grey leafless thorn scrub (jurema,
catingueira), mandacaru and xique-xique cacti, cracked ochre earth, granite outcrops, dry white-sand
riverbeds; the juazeiro is the only green tree; everything is leather, rawhide, cotton, straw, gourd,
clay, wood or hand-forged iron. NO plastic, NO synthetic fabric, NO rubber, NO zippers, NO jeans, NO
watch, NO glasses, NO firearms, NO motor vehicles, NO roads, NO power lines, NO wind turbines, NO water
tanks, NO wire fences, NO other people, NO dogs, NO goats. Water is rationed from gourds; the cattle
are driven by voice and the lead cow's bell, never by a whip.

NEGATIVE: a herd, cattle walking frame-right to frame-left, father and son swapping ends, @DAMIAO
ducking smoothly, groping, a blank stare, his eyes in direct sun, the hat flying off, reins in his
right hand, @ZE speaking, @ZE riding, @ZE beating the heifer, green leaves on the scrub, a blown-out
white sky block, CGI dust; centred symmetrical framing, flat even light, beauty light, milky blacks,
crushed blacks, vignette, golden-hour postcard, saturated blue sky, clouds, teal-and-orange, yellow or
sepia tint, HDR, lens flare, sun disc in frame, plastic skin, waxy skin, beauty retouching, clean
faces, clean new leather, clean clothing, doll face, glassy stare, frozen pupils, glowing eyes, white
or opaque eyes, zombie eyes, looking into the lens, cowboy hat, Stetson, cangaceiro half-moon hat,
metal stars, cartridge belts, humped zebu cattle, dairy cattle, fat glossy cattle, more than six
cattle, duplicated cattle, twins, clones, extra people, warped hands, extra fingers, extra legs or
hooves, floaty motion, looping motion, tripod-locked camera, gimbal, stabilized footage, drone,
aerial, crane, zoom, slow motion, over-sharpened, CGI, 3D render, subtitles, captions, on-screen text,
watermark, logo, music, score, BGM, instrumental, melody, accordion, zabumba, triangle, viola, guitar,
fiddle, fife, choir, ambient pad, drone tone, swell, chimes, wrong aspect ratio.

[ORDER: 3 shots, 2 hard cuts, 20s, observational handheld at walking height — (1, 0–7s) behind @ZE:
the SIX head in single file moving frame-left → frame-right, @DAMIAO on @TICAO at the head frame-right
— (2, 7–14s) from below: he rides into the thorny branch without ducking, the hat knocked back, his
right hand misses then finds the branch, brim pulled lower, the mutter — (3, 14–20s) @ZE's MCU: one
look at his father's back, then the stick taps the lagging heifer — hard end mid-step. Invariants:
exactly six cattle; column frame-left → frame-right, father at the head, son at the tail; his eyes in
the brim's shade, no blind-man acting; reins in his left hand, the right hand finds the branch. Look:
35mm, hard white drought sun, bleached palette, moving grain, no vignette. Only @DAMIAO speaks — two
words, Brazilian Portuguese. NO music, NO subtitles.]
```

**Cartão de geração**
```
GENERATION CARD
Model: Seedance 2.5 (Higgsfield seedance_2_5) · Task: reference-to-video (omni-reference)
Duration: 20s (= timeline) · Aspect: 21:9 · Resolution: draft 480p → final 1080p (2206×946) ·
Audio: on · bitrate: high
Attach in this order: 1) DAMIAO (Element: rosto + look) — identidade · 2) ZE (Element) — identidade ·
3) TICAO (Element, com sela e cabresto) — identidade · 4) ESTRELA (Element, com chocalho) — identidade ·
5) caatinga_dia_v1 — mundo
Notes: no draft, conferir a contagem de seis no plano 1 (risco maior), a mão direita no galho e que
Damião não "faz cego". Se o rebanho multiplicar, regenerar com a lock 1 repetida dentro do SHOT 1.
```

## 4.2 Tipos de cena deste filme

Dois outros prompts completos, prontos para copiar: **pouso noturno (G08)** e **o olho / a prova
(G19)** — em `references/reference-prompts.md`. Para os demais, adapte o modelo trocando os blocos
indicados:

**A · Travessia de dia** (G04, G05, G06, G12, G16, G18, G20, G21) — é o 4.1. Trocar: formação
(A até G11, B de G12 a G18, C de G20 em diante), variante MORNING/MIDDAY do L2 (L3 a partir de G19),
a falha do pai e a tarefa do Zé. Negativos: os do 4.1.

**B · Escala** (G03, G07, G13, G17, G22) — variante mínima do spine (CONTRACT · SCENE · TIMELINE de um
plano · CAMERA · LIGHT · FILM LOOK + LENS LOOK + NO LENS FLARES · SOUND · WORLD · NEGATIVE), mais WHO IS
WHO curto com a contagem. Câmera: EWS a 8° de 150–300 m, o operador na mão sobre uma pedra, tremor de
calor entre câmera e coluna; ou 107° baixo, câmera no chão com o rastro da trilha saindo do primeiro
plano. Lock repetido em todos os blocos: `the figures occupy less than a tenth of the frame height`.
Negativos: `medium shot, the camera walking closer, drone, aerial, crane, a herd, green landscape`.

**C · Processo** (G01 cabresto no escuro, G10 cacimba, G11 o gado bebe; parte de G08) — BEATS com
segundos, cada passo com resistência, erro, nova tentativa, resultado e teste; foco nas mãos; nada
aparece do nada. G01: focinheira passada, tira por trás das orelhas, o nó sob o queixo apertado com
dois puxões, o teste com um tranco, o freio por cima, a corda enrolada em quatro voltas e amarrada na
sela — tudo sem olhar para as mãos, os olhos no escuro à frente. G10: Zé cava com as mãos e uma cuia o
leito de areia branca, 60 cm, a areia úmida escurecendo, a água minando turva devagar no fundo, ele
espera, enche a cuia. Negativos: `effortless, one perfect smooth action, objects appearing, a skip to
the result, clear clean water, modern tools`.

**D · Pouso noturno** (G08, G09, G15) — prompt completo em `references/reference-prompts.md`. L4 FOGO;
@DAMIAO_POUSO sem chapéu e sem gibão; Damião sempre à esquerda do fogo, Zé à direita. Negativos da
noite: `daylight, moon, star field, lantern, orange light filling the frame, CGI flames, looping
fire`. À noite os olhos do Damião são normais — escuros, molhados, refletindo o fogo; **nenhuma névoa
aparece à noite**.

**E · O olho** (G19; em grau menor G14) — prompt completo em `references/reference-prompts.md`. É o
único lugar do filme em que a névoa da catarata aparece e o único em que o sol entra sob a aba. Em G14
(juazeiro, sombra verde) ele ergue o rosto para o céu e a aba sobe, mas a sombra ainda esconde o olho;
o que se vê é o olhar pousando no pedaço errado do céu.

**F · A pé e a cavalo** (G12, G16, G20, G23 — o diálogo deste filme) — dois-planos e singles com
diferença de altura. Linhas de olhar: quem está à frente (frame-right) olha para trás e para cima
(frame-left); o olhar do Damião para o Zé sempre pousa um palmo ao lado do rosto dele. **Até G19 a
câmera fica na altura do Zé** (olha o pai de baixo); **depois de G19 a câmera fica na altura do
Damião** (§10). Negativos: `eyelines crossing, both speaking at once, the listener's mouth moving`.

**G · Animal** (inserts: o chocalho da Estrela, as orelhas do Tição, o gado na cacimba) — câmera na
altura do animal; a tarefa do animal é concreta (Estrela segue para onde o chocalho sempre levou;
Tição escolhe onde pisar e tem sempre uma orelha virada para trás, para o cavaleiro). Escrever
orelhas, narinas, peso e rabo — nunca expressão humana. Negativos: `glowing animal, cartoon animal,
stuffed toy, plastic fur, groomed show animal, animal looking into the lens`.

---

# 5 · BIBLIOTECA DE NEGATIVOS — ACRÉSCIMOS DO PROJETO

Some ao NEGATIVE do plano o conjunto do tipo de cena; a espinha (§1.3) vem sempre por último.

**Dia de seca (todo exterior de dia):** golden-hour postcard, saturated blue sky, clouds, green
vegetation (except the juazeiro), sun disc in frame, sunbeams, god rays, yellow or sepia tint, heat
distortion over faces.

**Noite de pouso:** daylight, moon, star field, Milky Way, lantern, torch, second warm source, orange
light filling the frame, CGI flames, looping fire, sparks as particles.

**Gado e cavalo:** more than six cattle, a herd, humped zebu cattle, black-and-white dairy cattle, fat
glossy cattle, emaciated cattle collapsing, cattle looking into the lens, groomed show horse, shod
horse, western saddle, a second horse, a donkey.

**Figurino:** cowboy hat, Stetson, cangaceiro half-moon hat, metal stars, studs, cartridge belts,
bandana, rubber boots, sneakers, printed T-shirts, clean new leather.

**Música (o mundo puxa forró):** accordion, zabumba, triangle, viola, guitar, fiddle, fife, choir,
singing with accompaniment, humming score, ambient pad, swell.

**O olho do pai — não nomeie, descreva a geometria:** nunca "blind", "cataract", "cego". Descrição:
`in the centre of both pupils a faint milky grey haze, like breath on glass; the dark brown irises
clear around it`. Escala: o tamanho da pupila, nada além. Negativo: `white or opaque eyes, zombie
eyes, glowing eyes, the whole eye clouded white, eyes rolled back, blank stare, blue contact-lens
eyes`.

**O cabresto — geometria, não nome:** `braided rawhide halter, pale tan-grey, flat braid 1.5 cm wide,
noseband and a strap behind the ears, a hand-tied knot under the jaw with a twisted rawhide ring, a
3 m round-braided rawhide lead rope as thick as a finger, coiled in four loops and tied to the saddle
front, worn under the bridle`. Negativo: `nylon halter, coloured rope, western rope halter, metal
buckles, leather show halter`.

**O chocalho:** `a hammered iron bell, rust-brown and black, trapezoid, 15 cm tall, open at the bottom,
hanging from a rawhide collar`. Negativo: `Swiss cowbell, brass bell, shiny bell, ringing, chimes`.

**A binga:** `a palm-size steel striker struck down across a grey flint; sparks; a cotton wick in a
short horn tube catching a coin-sized orange ember, no flame`. Negativo: `modern lighter, Zippo,
match, a flame from the lighter`.

**A parede do açude (G23):** `a long straight ridge of packed grey-brown earth across the low ground
ahead, about 6 m high, far too straight to be natural`; o que está atrás dela nunca é visto. Negativo:
`visible water, a lake, a reflection of the sky, concrete dam, spillway gates, buildings`.

---

# 6 · ESTRUTURA E ROTEIRO

Roteiro completo, geração por geração (G01–G23, estado de entrada e de saída, falas com segundos
aproximados): `references/script.md`.

## Blocos

1. **A PARTIDA** (dia 1, madrugada → manhã · G01–G04 · ~75 s) — no escuro, o pai põe o cabresto de cor;
   a porteira abre sobre o curral vazio; seis cabeças saem; o aboio do pai.
2. **DIA 1** (G05–G09 · ~85 s) — as primeiras falhas, disfarçadas: o galho, a cabaça que a mão erra;
   no pouso, a binga que passa ao lado do cigarro — o Zé, de costas, só ouve.
3. **DIA 2** (G10–G15 · ~110 s) — a cacimba no rio seco; "Vai tu na frente" — o pai passa a frente ao
   filho com uma desculpa; o juazeiro e os urubus ("Tô vendo"); de noite, no escuro, todos são cegos.
4. **DIA 3 — A PROVA** (G16–G19 · ~85 s) — o pai dá a sua água; no lajedo a vaca desgarra e o pai não
   vê — escuta; **a cabaça pela terceira vez: Zé vê** (a virada).
5. **O CABRESTO** (G20–G23 · ~90 s) — o filho desamarra a corda e leva o pai; o aboio do filho, falhando;
   a parede do açude; "Tem água, Zé?" — "Tem, pai."

Teto: **8:00** = ~7:25 gerados + ~35 s de título e créditos montados na edição (nunca gerar texto).
Nunca se cortam: G01, G10, G19, G20. Comprimem primeiro: as escalas (B) e G04, G11, G21.

## Motivos e rimas

- **O cabresto, primeiro e último gesto:** as mãos do pai no escuro (G01) → a mão do filho na corda
  (G20). Mesma corda, mesma trança, mesmo nó.
- **O aboio:** a voz do pai abre a viagem (G03); a voz do filho, falhando, fecha (G21). O gado segue as
  duas.
- **A cabaça, paga três vezes:** G06 (a mão fecha no ar, ninguém vê), G16 (o pai recusa: evita a mão),
  G19 (Zé vê, e põe a cabaça na mão do pai).
- **"Esse sol…"** — a desculpa do pai, dita uma vez (G05); depois, o sol é que o entrega (G19).
- **A mentira que muda de boca:** "Tô vendo" (o pai, G14) → "Tem, pai." (o filho, G23).
- **O verde usado uma vez:** a copa do juazeiro (G14).
- **O chocalho:** a bússola. Some só em G19 — as cigarras param, o chocalho para (a vaca parada), fica a
  respiração do cavalo.

## Diálogo (proposta — o argumento não trazia falas; ajustar à vontade)

| G | Quem | Fala |
|---|---|---|
| G02 | DAMIÃO | "Abre a porteira, Zé." |
| G05 | DAMIÃO | "Esse sol…" |
| G08 | ZÉ / DAMIÃO | "Pai, quanto falta?" / "Dois dia. Se Deus quiser." |
| G12 | DAMIÃO | "Vai tu na frente. Tá na hora de aprender." |
| G14 | ZÉ / DAMIÃO | "Olha os urubu, pai." / "Tô vendo." |
| G15 | DAMIÃO / ZÉ | "Zé?" / "Tô aqui, pai." |
| G16 | DAMIÃO | "Bebe tu. Eu num tô com sede." |
| G19 | DAMIÃO / ZÉ | "Que foi, Zé?" / "A água, pai." |
| G20 | ZÉ / DAMIÃO | "Deixa que eu levo, pai. O caminho aqui é ruim." / "É ruim mesmo." |
| G23 | DAMIÃO / ZÉ | "Tem água, Zé?" / "Tem, pai." |

Mais os dois aboios (G03 Damião, G21 Zé). Ninguém nunca diz "cego", "vista" ou "olho".

---

# 7 · ELENCO

**@DAMIAO (Seu Damião), 66.** Vaqueiro a vida inteira; as seis cabeças são o que sobrou do gado de
"sorte" juntado em quarenta anos (uma cria em cada quatro). Magro, de ossos compridos, rugas fundas de
sol, barba branca por fazer, bigode ralo grisalho, pele escura queimada; olhos castanho-escuros. Chapéu
de couro com barbicacho, gibão marrom arranhado de branco, perneiras, camisa de algodão desbotada
abotoada até o pescoço, alpercatas de couro com espora de ferro, peixeira atravessada no cinto.
**Mãos:** grandes, nodosas, cor de couro, unhas grossas rachadas, cicatrizes brancas de espinho no
dorso, **falta a ponta do indicador direito** (corda, há muitos anos); mãos que sabem tudo de cor.
Temperamento: poucas palavras, ordens curtas, nunca se queixa. **Superobjetivo:** levar o gado vivo até
a água e entregar ao filho um rebanho, não uma dívida — sem deixar de ser o vaqueiro que guia.
**Nunca:** tateia, abana a mão diante do rosto, esfrega os olhos na frente do filho, pede ajuda, diz
que não enxerga, chora.
Estados: `@DAMIAO` (dias 1–2, encourado) · `@DAMIAO_POUSO` (noite: sem chapéu — cabelo branco
achatado com a marca do chapéu, sem gibão, camisa) · `@DAMIAO_D3` (dia 3: poeira grossa, lábios
rachados, a névoa nas pupilas — construída por máscara sobre o rosto-base, nunca regerada).
*Âncoras (colar em WHO IS WHO):*
`@DAMIAO (66, lean, deep sun-cut lines, white stubble, thin grey moustache; stiff brown leather hat
with a chin strap, scuffed leather jacket and leggings; tip of the right index finger missing — 100%
matches its reference)`
`@DAMIAO_POUSO (66, lean, deep sun-cut lines, white stubble, thin grey moustache; hat off, white hair
flattened by it, leather jacket off, faded cotton shirt; tip of the right index finger missing — 100%
matches its reference)`
`@DAMIAO_D3 (66, lean, sun-cut lines caked with dust, three-day white stubble, cracked lips; stiff
brown leather hat with a chin strap, scuffed leather jacket and leggings; tip of the right index
finger missing — 100% matches its reference)`

**@ZE (Zé), 15.** O caçula. Magro, alto para a idade, os punhos saindo das mangas, buço começando,
cabelo preto cortado em casa e torto, nariz queimado descascando, olhos escuros. Chapéu de palha de
carnaúba esfiapado, rasgado na frente da aba; camisa de algodão remendada grande demais (era do pai);
calça arregaçada na canela; alpercatas. **Nenhuma peça de couro de vaqueiro** — ainda não é vaqueiro, e
no fim continua sem o gibão: vira vaqueiro sem a roupa. **Mãos:** compridas, finas, jovens, poeirentas,
unhas roídas, uma bolha nova na palma direita da vara — nunca parecidas com as do pai (elas se tocam em
G19 e G20). Temperamento: calado com o pai, mandão com o gado, quer ser visto trabalhando.
**Superobjetivo:** ser tomado por vaqueiro pelo pai — ganhar a frente. **Nunca:** chora, abraça o pai,
diz em voz alta o que viu, demonstra pena, olha para a lente, abana a mão diante do rosto do pai para
testar.
*Âncora:* `@ZE (15, thin, tall for his age, faint first moustache, peeling sun-burned nose; frayed
straw hat, oversized patched cotton shirt, sandals — 100% matches its reference)`

**@TICAO (Tição), cavalo.** Pequeno (~1,40 m na cernelha), velho, castanho-escuro quase preto, pelos
brancos em volta dos olhos e do focinho, costelas aparecendo, cicatriz clara antiga no ombro direito
(lado da câmera), sem ferradura, crina curta e falhada. Sela vaqueira gasta, estribos de ferro, freio, e
o @CABRESTO por baixo. **Tarefa:** o cavalo soube primeiro — há meses escolhe o caminho pelo velho;
segue o chocalho, desvia do que machuca, para sozinho antes do obstáculo. Uma orelha sempre virada
para trás, para o cavaleiro.
*Âncora:* `@TICAO (small old dark-bay horse, nearly black, grey around the eyes, ribs showing, pale
scar on the right shoulder, unshod; braided rawhide halter under the bridle, its lead rope coiled at
the saddle front)`

**@ESTRELA, vaca-guia.** Velha, vermelho-castanha, gado pé-duro, chifres médios curvados para cima,
estrela branca irregular na testa, ancas e costelas aparecendo, @CHOCALHO na coleira de couro cru.
**Tarefa:** ir para onde o chocalho sempre levou; as outras cinco vão atrás dela.
*Âncora:* `@ESTRELA (old red-brown cow, white star on the forehead, rusted iron bell on a rawhide
collar)`

**@GADO, as outras cinco.** Sem referência individual; cada uma com uma pelagem: boi baio de chifre
longo, vaca rajada, garrote preto, vaca creme, novilha vermelha (a que se atrasa).
*Âncora:* `five more small thin sertão cattle, each a different dull coat — dun, brindle, black, cream,
red — ribs and hip bones showing, alive and walking`

---

# 8 · NOTAS DE ATUAÇÃO PARA ESTE FILME

**O princípio:** o ator está investido numa TÁTICA a serviço de um OBJETIVO e nunca atua uma emoção
(`cineoro-performance`). Ninguém neste filme "sofre": todos trabalham.

**A direção comum do filme inteiro (não dita):** *fazer desta uma viagem normal — o pai é o vaqueiro, o
filho é o menino.* Depois de G19 a direção continua a mesma, e é isso que dói: o filho passa a
sustentar a mentira do pai.

**Damião — a cegueira jogada como competência.** Ele nunca joga "cego"; joga *vaqueiro que vê*, com
canais físicos concretos: (1) **o ouvido** — orienta a cabeça pelo chocalho, pelos cascos, pela
respiração do Zé; (2) **a mão** — confere tudo pelo tato como quem confere por hábito (a corda, a
cabaça, o nó); (3) **o cavalo** — deixa o Tição escolher a linha e parar sozinho; (4) **as desculpas** —
o sol, "tá na hora de aprender", "num tô com sede"; (5) **a aba** — puxa o chapéu para baixo sempre
que erra. Os olhos têm trabalho: *escutar com os olhos* — vão para o som, chegam um tempo atrasados,
pousam um palmo ao lado, e então se apertam como contra o sol. Detalhe involuntário preferido: o
maxilar que trava uma vez depois de cada erro.

**Zé — de provar a proteger.** Até G19: tática de *provar-se* — trabalha demais o gado, rouba olhares
para as costas do pai procurando aprovação (nunca para o rosto). Em G19: *saber sem perguntar* —
segura a cabaça e espera, olhando de um olho do pai para o outro. Depois de G19: *proteger o disfarce*
— arranja o mundo para o pai não precisar enxergar (inventa que o caminho é ruim, pega a corda como
quem faz um favor pequeno). Detalhe involuntário preferido: o engolir em seco.

**Par de contraste — o eixo essencial é *quem guia*.** Damião: **conhece o caminho (+) / não enxerga
(−)**. Zé: **enxerga (+) / não conhece o caminho (−)**. Os dois empurram a mesma direção ("viagem
normal"); o contraste vaza pelos olhos — o pai olha para sons, o filho olha para o pai. No fim os
dois sinais se juntam numa só coluna: os olhos do filho, a memória do pai.

**O que nunca:** lágrimas (de ninguém, o filme todo), abraço, "o senhor tá cego?", o teste da mão
abanando diante do rosto, música subindo, o pai confessando.

---

# 9 · LÍNGUA

Não se aplica — não há língua inventada. Regras do português nordestino em §3.

---

# 10 · DECLARAÇÃO DO DIRETOR

**A ideia.** Um homem que guiou a vida inteira aprende a ser guiado, e um menino aprende a guiar
guardando o segredo do pai. Âncora de pitch: *"Quem guia quem."*

**Luz e cor.** O sol é o antagonista: o filme é sobre perder a vista, então a luz é dura e branca e o
céu de seca é sem cor. **A sombra da aba do chapéu é o esconderijo do pai** — por isso, de dia, os
olhos dos dois vivem na sombra da aba. **Só no último fim de tarde o sol desce abaixo da aba e acende
os olhos dele: é a luz que o entrega.** Por isso nenhuma cena dos dias 1 e 2 acontece com sol baixo. O
calor (cor quente) só existe no fogo, à noite — e à noite pai e filho são igualmente cegos, por isso a
noite não denuncia nada. O verde aparece uma vez, no juazeiro (sombra = vida).

**Câmera.** É o Zé: anda na altura de um menino a pé, sempre do mesmo lado da trilha, e aprende o que
ele aprende. **Até G19 olhamos o pai montado de baixo para cima (~15°) — o menino olha o pai; G19 é a
última contra-plongée e o primeiro olho visto. Depois, a câmera encontra o Damião na altura dele.**
Nunca um plano subjetivo da visão do pai. Horizonte nivelado — é um mundo sob controle; inclina-se só
no lajedo, quando a vaca desgarra (G18). No 21:9, as escalas mostram gente pequena em terra enorme: o
tamanho da viagem é dito pelas escalas, não pelo diálogo. Lente esférica, não anamórfica: o sol está
perto do quadro o filme inteiro e a anamórfica convida riscos de flare horizontais; o filme é sobre
olhos, não espetáculo.

**Direção de tela.** A viagem anda sempre da esquerda para a direita do quadro (para o oeste, para o
açude). **Quem guia ocupa o lado direito do quadro** — o pai no dia 1, o filho a partir de G12, o filho
puxando o pai a partir de G20. A troca de lado é a história. Por consequência o sol tem lugar certo: de
manhã atrás deles (quadro-esquerda), ao meio-dia alto, no fim da tarde à frente (quadro-direita, na
cara deles).

**Montagem.** Observada (cortes secos, saltos de tempo, a câmera reposicionada a cada corte, sempre do
mesmo lado) para a viagem e os processos; **autoral** — quadros compostos e segurados — nas três
viradas: a cabaça I (G06), a prova (G19), o cabresto (G20). Nunca cortar para longe da virada; o valor
muda no rosto do Zé.

**Som.** Sem trilha. **O chocalho é a bússola do filme**: o pai o segue, o espectador aprende a
segui-lo. O aboio é a única melodia do filme e é uma voz. Silêncio como instrumento: em G19 as
cigarras param e o chocalho para; fica a respiração do cavalo. Nada de sanfona — o Nordeste do filme é
o de 1958, não o do cartão-postal.

**Cotidiano.** Processos mostrados inteiros: o cabresto posto no escuro, a cacimba cavada na areia, o
cigarro de palha enrolado e aceso com binga, a água racionada na cabaça, o gibão que existe para
atravessar espinho. Cada objeto tem função; nenhum aparece porque é bonito.

**Mundo — composto, não reconstrução.** O sertão do filme é uma composição de paisagens da Paraíba
(Cariri e Sertão) na seca de 1958; o "açude do Jatobá" é fictício. O cotidiano tem de estar certo
mesmo assim: indumentária de vaqueiro, aboio, cacimba, binga, fumo de rolo, cabaça, chocalho, pé-duro.
(Âncora só para humanos: a luz branca sem filtro de *Vidas Secas*. **Nunca** citar o filme no prompt —
puxaria preto-e-branco.)

**Nota de leitura (não é reescrita):** catarata não avança em três dias. No filme ela já estava
madura; o que a viagem tira do pai são as muletas — o caminho de casa decorado, a luz conhecida, a
rotina. É isso que "ir ficando cego" significa na tela.

---

# 11 · NOTAS DE PRODUÇÃO

**Assets** (registro e prompts de imagem em `references/asset-registry.md`):

| Asset | Status |
|---|---|
| DAMIAO rosto-base, look encourado, mãos; DAMIAO_POUSO look; DAMIAO_D3 (máscaras: poeira, lábios, névoa) | a construir |
| ZE rosto-base, look, mãos | a construir |
| TICAO (turnaround com sela, freio e cabresto; cabeça em close) | a construir |
| ESTRELA (lado + cabeça com estrela e chocalho); GADO (as cinco, opcional) | a construir |
| CABRESTO, CHOCALHO, CABACA, BINGA, FUMO, PEIXEIRA, VARA, MATULAO, COURO (fundo neutro) | a construir |
| Placas: CURRAL_MADRUGADA, CAATINGA_DIA, CAATINGA_TARDE, RIO_SECO_DIA, JUAZEIRO_DIA, POUSO1_NOITE, POUSO2_NOITE, LAJEDO_TARDE, ACUDE_TARDE | a construir |
| Vozes: DAMIAO_VOICE, ZE_VOICE, DAMIAO_ABOIO | do primeiro take aprovado |

Rostos gerados uma vez, em close, nunca regerados; estados por máscara. Referências reduzidas a ~1080p
antes do upload. Pessoas referenciadas por geração: no máximo 2 (bem abaixo do limite de 4); sujeitos
referenciados por geração: no máximo 6.

**Duração.** Teto 8:00. Ver §6.

**Configuração de geração.** Seedance 2.5 · Higgsfield `seedance_2_5` · omni-reference (t2v para
escalas sem rosto) · 21:9 · draft 480p → final 1080p (2206×946) · áudio ligado · bitrate high ·
**duração = soma dos ranges da timeline** · draft sempre primeiro em geração com mais de um plano.

**Teste antes de congelar (v1 → v1.1).** Antes de produzir, gerar em draft os três prompts de
referência — G05 (dia), G08 (noite), G19 (o olho) — e conferir: o look segura nos três? o céu sai
branco sem nuvem? a contagem de seis? a névoa no olho sai sutil (nem invisível, nem branca)? o aboio
sai sem instrumento (testar G03 também)? Ajustar os templates uma vez, subir para **v1.1**, e daí em
diante não tocar.

**Ordem de trabalho num plano.** Evento e tática → geometria (formação; previz se preciso) → prompt no
spine com os templates colados → draft → conferir → consertar o único bloco que falhou (ou editar os
segundos errados do take) → final. Frames de takes aprovados viram keyframes; falas limpas viram
referência de voz.

**Ordem de geração sugerida.** Por luz e lugar, não por roteiro: noite (G08, G09, G15) → madrugada
(G01–G03) → dia (o resto dos dias 1–2) → dia 3 (G16–G18) → sol baixo (G19–G23, por último, quando os
assets do D3 e as vozes já existirem).

---

## Registro de versões

- **v1 — 2026-10-09** — bíblia criada a partir do argumento do usuário. Defaults assumidos: título
  provisório, nomes do cavalo/vaca/açude, falas propostas, final com o açude fora de quadro. Templates
  ainda não testados.
