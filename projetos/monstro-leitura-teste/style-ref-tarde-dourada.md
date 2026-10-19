# STYLE REF — TARDE DOURADA

Referência: filme "BIS — O nome já diz" (arquivo `YTDown.com_YouTube_Media_3CnLiR3Drmo_BIS-O-nome-ja_-diz_001_1080p.mp4`,
o mesmo link do briefing da Leitura). Uso: **somente estética** (luz, cor, textura, lente, câmera, decupagem).
Nada de produto, embalagem, logo, texto, elenco ou cenário do filme original é para copiar.

---

## 1. O que foi analisado e como

- **Arquivo:** 26,7 s, 1920×1080 (16:9, pixel quadrado, sem letterbox), 23,976 fps, H.264 a ~2 Mb/s, Rec.709.
- **Método:** (a) olhei a folha de contato a 1 fps e 6 quadros cheios (2,6 s · 3,9 s · 8,6 s · 10,4 s ·
  12,3 s · 19,2 s); (b) medi 43 quadros (0 a 21 s, sem o cartão final) com script: percentis de luma, saturação,
  matiz, tom das sombras/médios/altas, queda de luz nos cantos, paleta por k-means; (c) estimei o movimento
  global de câmera entre quadros consecutivos por correlação de fase; (d) detectei os cortes.
- **Limites (importante):** o arquivo é um H.264 de YouTube, então **grão fino não é mensurável** (a compressão
  apaga) e **temperatura de cor em Kelvin e distância focal são estimativas visuais**, não dados. O áudio
  **não foi analisado**. Os números abaixo descrevem o look já gradeado, não o negativo.

---

## 2. Resumo do estilo (em uma frase)

Sala de aula no fim de tarde: **sol baixo e dourado atravessando persianas**, pele quente e brilhante, pretos
fundos e levemente violeta, **azul-cobalto e rosa-magenta empoeirado** como acentos contra um miolo
âmbar/marrom, lente aberta e perto do rosto, foco raso com bokeh cremoso, câmera **travada** e planos
centrados, quase sempre de baixo para cima, na altura da carteira.

---

## 3. O que as medições mostram

| Item | Medição (43 quadros) | Leitura |
|---|---|---|
| Luma mediana | 63/255 (≈ 25%), variando de 28 a 91 por plano | imagem **densa e quente**, não high-key |
| Pretos / brancos | P1 ≈ 4 · P5 ≈ 11 · P95 ≈ 160 · P99 ≈ 188 | pretos fundos mas abertos; **brancos não estouram** (pico ≈ 74%), exceto janela e tubos fluorescentes |
| Tom das sombras (15% mais escuros) | RGB ≈ 16/12/18, R/B 0,93 | pretos **frios, levemente violeta** |
| Tom dos médios | RGB ≈ 80/62/60, R/B 1,33 | miolo **quente, marrom-âmbar** |
| Tom das altas (15% mais claros) | RGB ≈ 170/145/124, R/B 1,37 | altas **âmbar**, nunca branco puro |
| Saturação média (HSV) | 41% (36–52% por plano) | **moderada**; os acentos é que são saturados |
| Matiz dos pixels saturados | vermelho/laranja (pele, madeira, parede) 52% · âmbar 12% · **azul 15%** · magenta/rosa 14% · **verde < 0,5%** | paleta **sem verde** |
| Queda de luz nos cantos | cantos ≈ 79% do centro (muito varia com o conteúdo) | queda **natural**, sem vinheta aplicada visível |
| Câmera | 5 de 13 planos com deslocamento global zero; os outros com pans/empurrões lentos (≤ 2 px/quadro a 320 px) | **travada** ou deriva lenta; **não é câmera na mão tremida** |
| Decupagem | 13 planos em 21,3 s (≈ 1,6 s/plano) + packshot (3,6 s) + fecho (1,9 s) | cortes secos e rápidos |
| Obturador | borrão de movimento no braço que varre o quadro (8,6 s) | 24 p com obturador natural (180°) |

**Paleta medida (k-means, 10 grupos):** `#0f0b0e` 17% (preto violeta) · `#806658` 15% · `#4a332f` 14% · `#664c42` 14% ·
`#2f1e1c` 13% · `#9e806d` 11% · `#162036` 9% (azul-marinho profundo) · `#c3a88b` 4% · `#34445c` 4% · `#efede4` 1% (branco quente).
Em outras palavras: ~70% dos pixels são marrons-âmbar de tom e luminosidade variados, ~12% azul-marinho/cobalto,
~17% preto. O azul "elétrico" aparece só nos acentos (mural da sala, embalagem), não na média.

---

## 4. Luz (fotografia)

- **Chave:** sol baixo de fim de tarde (≈ 3200–3800 K, estimativa visual) entrando por **janela com persiana
  semiaberta**, do lado direito e um pouco atrás dos atores. Risca o ambiente, envolve a bochecha/orelha do lado
  da janela e desenha **aro dourado no cabelo**. A persiana brilha quente, com **halo suave (halation)**.
- **Contra-luz suave nos rostos:** pele com brilho (testa, nariz, lábio), subsurface quente na orelha e no nariz
  quando a luz vaza por trás, cílios e fios soltos acesos.
- **Preenchimento:** o rebote de parede bege e teto, quente (~4000 K), sombras **macias, sem borda dura**;
  relação chave:preenchimento aprox. 3:1 no rosto (estimativa).
- **Práticas:** tubos fluorescentes lineares no teto, secundários; aparecem como formas quase brancas nos planos
  em contra-picado. Eles **não dominam** o balanço de cor.
- **Exposição:** na pele. Médios densos, altas com rolloff suave, pretos profundos mas não esmagados.
- **Direção:** a luz vem sempre do mesmo lado do ambiente (direita/fundo); o lado iluminado não troca entre planos.

## 5. Cor

- **Miolo âmbar/marrom-umber** (parede, madeira, pele), **sombras violeta-frias**, **azul-cobalto/marinho** como
  contracor dominante (mural, piso, uniformes, embalagem) e **rosa-magenta empoeirado** como terceiro acento
  (camiseta). **Amarelo-mostarda** aparece uma vez (moletom) como respiro quente.
- **Verde ausente.** Qualquer verde na cena quebra a paleta.
- Saturação moderada no todo; saturação alta só nos acentos pequenos. Pele sempre quente e natural, nunca
  alaranjada de grade "teal-and-orange".

## 6. Textura

- Captura **digital limpa com maciez filmica**: sem nitidez artificial, sem grão pesado (não confirmável no
  arquivo), halo suave nas altas luzes.
- **Pele real** (poros, brilho oleoso leve, fios soltos), **tecidos com trama visível** (malhas listradas,
  camiseta lavada), **objetos usados** (carteiras de laminado riscado, cadernos de espiral, caneta, pulseiras
  de miçangas), mural de cortiça/azul com papéis e post-its borrados. Mundo vivido, não catálogo.
- **Bokeh redondo e cremoso** (lente esférica), com **oclusores em primeiro plano** (cabelo, ombro, carteira)
  borrados nas bordas do quadro.

## 7. Lente e câmera

- **Formato:** 16:9 esférico, sem anamórfico, 24 p, obturador natural.
- **Lentes:** de normais a abertas **coladas no rosto** (≈ 24–35 mm equivalente em S35, estimativa), com leve
  esticamento de perspectiva em close (nariz, testa), profundidade de campo **rasa** (aprox. T1.8–2.8).
- **Câmera:** **travada** ou com deriva/empurrão lento; sem handheld nervoso. Alturas: **na altura da carteira,
  olhando para cima** (teto com tubos à vista), **top-down 90°** na mesa, **POV debaixo da carteira**,
  frontal centrado olhando para a lente nos closes de virada.
- **Composição:** rostos centrados ou em terço inferior, muito pé-direito e parede acima da cabeça; **uma faixa
  horizontal azul (mural) atrás das cabeças** como bloco de cor; fundo cheio de gente borrada.
- **Ritmo:** cortes secos de 1–2 s; planos de "gag" (rosto frontal olhando para a lente) mais longos (≈ 3,5 s).

## 8. Inventário de planos da referência (para escolher o que se aplica)

| # | Tempo | Plano | Câmera | Luz / lente |
|---|---|---|---|---|
| 1 | 0,0–1,8 | ECU mãos abrindo o bombom | deriva leve | foco raso, fundo quente + azul borrado |
| 2 | 1,8–3,4 | MCU menina, olhos fechados | deriva lenta | sol da persiana de lado, pele dourada |
| 3 | 3,4–4,8 | CU menino, olhar para fora | pan lento | lente aberta colada, bokeh de turma |
| 4 | 4,8–6,2 | menina espia atrás do ombro | travada | oclusor em primeiro plano borrado |
| 5 | 6,2–7,5 | CU perfil do menino | travada | — |
| 6 | 7,5–9,7 | WIDE contra-picado, braço varre o quadro | travada | tubos no quadro, persiana brilhando, borrão de movimento |
| 7 | 9,7–11,6 | over-the-shoulder duplo | travada | cabeça em primeiro plano borrada, fundo suave |
| 8 | 11,6–13,2 | top-down da mesa | travada | luz rasante na madeira, notebook, caneta |
| 9 | 13,2–14,4 | POV baixo, mão com o bombom | mão em movimento | pés em primeiro plano borrados |
| 10 | 14,4–15,2 | CU frontal abrindo o doce | travada | — |
| 11 | 15,2–16,9 | CU frontal | travada | — |
| 12 | 16,9–17,7 | CU frontal da menina olhando para a lente | travada | olhar direto, gag |
| 13 | 17,7–21,3 | frontal médio, doce na boca | travada | mural azul em faixa atrás |
| — | 21,3–24,8 | packshot em azul chapado | — | cartão final |
| — | 24,8–26,7 | pé pisa no bombom (fecho) | baixa | — |

---

## 9. Blocos prontos para colar (inglês — é o que o Seedance recebe)

**STYLE INTENT**
```
MEDIUM: live-action photoreal commercial.
REGISTER: authored-composed comedy commercial, youth / school world.
CAMERA LANGUAGE: locked-off, composed frames; slow drifts only; frontal centred close-ups, low desk-height angles,
  occasional top-down.
LIGHT LOGIC: low late-afternoon sun through half-closed blinds as the motivated key; warm bounce fill; fluorescent
  tubes as secondary practicals.
COLOUR & TEXTURE: amber-umber core, cool violet-black shadows, cobalt-blue and dusty magenta accents, NO green;
  clean digital with soft halation, no heavy grain; soft bloom on windows and tubes allowed, no lens flares.
MOTION: real-time 24p with a natural 180-degree shutter.
REALIST PRESET RULES SWITCHED OFF: handheld, grain, muted palette, off-centre framing, chiaroscuro darkness,
  "no glow".
```

**LIGHT (base)**
```
LIGHT — MOTIVATED LIGHT ONLY, late-afternoon interior, WARM & DENSE (KEY): SOURCE: the only key is low sun, amber
~3200–3800 K, coming through half-closed venetian blinds from a large window at frame-right, slightly behind the
subjects, about 20° above the horizon; it wraps the right cheek, ear and hair edge with a golden rim, and the blinds
glow hot and soft with a gentle halation. FILL: the warm bounce of beige walls and ceiling (~4000 K), about three
times dimmer than the key on the face, soft shadows with no hard edges. PRACTICALS: linear fluorescent ceiling tubes,
cool-white, secondary, never the dominant colour. REACH: the sun reaches the window-side of every face and dies
across the room; the far wall stays warm and soft. EXPOSURE: exposed for the skin; dense midtones (median luminance
about a quarter of full range), highlights roll off softly with the peak around three quarters except for the window
and tubes, blacks deep but open with a faint cool-violet tint; natural falloff, NO vignette overlay. CONTINUITY: the
window stays frame-right in every frame, lit sides never flip, the light never changes during the take. NOT: flat
even light, cold daylight, hard-edged shadows, overexposed skin, crushed muddy blacks, a second sun.
```

**FILM LOOK (lock)**
```
FILM LOOK (KEY — reproduce this exact photographic character): modern digital cinema capture at 24 fps with a
natural 180° shutter, graded for a warm, dense commercial look: amber-umber midtones and highlights, cool violet-black
shadows, saturated cobalt-blue and dusty magenta-pink accents against them, NO green anywhere in the palette;
moderate overall saturation with skin kept warm and natural; soft S-curve contrast, highlights rolling off with gentle
halation on windows and lamps, blacks deep but open; clean image with a filmic softness, no heavy grain, no sharpening
halos; real skin with pores, a light sheen on forehead and nose, flyaway hair catching the backlight. Lens: spherical,
round soft creamy bokeh, shallow depth of field, normal-to-wide focal length used close to faces for a slight
perspective stretch; soft out-of-focus foreground occluders (hair, shoulders, desks) at the frame edges.
MEGA-REAL, NOT a render, NOT HDR, NOT teal-and-orange.
SOFT BLOOM on the window and tube lights only; NO lens flares, no streaks, no floating bokeh orbs.
```

**CAMERA & LENS (outcomes)**
```
LENS LOOK: spherical normal-to-wide lens working close to faces (a slight stretch of nose and forehead in close-ups),
shallow depth of field with round creamy bokeh, focus peaked on the eyes, a blurred crowd or shelves behind, soft
foreground hair, shoulders or furniture as occluders; 16:9, 24p, natural motion blur on fast arms and hands.
CAMERA LANGUAGE: locked-off and composed — a tripod or dolly head, no hand-held shake, no gimbal glide; moves, when
they exist, are slow drifts or a single decisive pull. Angles: frontal and centred for the gag close-ups, low desk-height
looking up (ceiling visible) for wides, top-down for the table.
```

**COLOUR / PRODUCTION DESIGN**
```
PALETTE — core: amber, umber, tan and warm brown (walls, wood, skin); counter-colour: deep cobalt and navy blue
(a pin-board or feature wall as a horizontal colour band behind the heads, uniforms, floor); accent: dusty magenta-pink
(one garment); rare warm accent: mustard yellow. Shadows: violet-black. Highlights: warm off-white, never pure white.
NO green. Everything lived-in: scuffed laminate, spiral notebooks, beaded bracelets, washed cotton, striped knits,
pinned papers blurred on a blue board.
```

**NEGATIVE (style spine)**
```
teal-and-orange grade, green cast, neon saturation, cold blue daylight, flat even light, overexposed or blown skin,
crushed muddy blacks, HDR look, beauty retouching, plastic skin, heavy film grain, hand-held shaky camera, gimbal glide,
vignette overlay, lens flares, anamorphic streaks, hard-edged shadows, clean showroom set.
```

---

## 10. O que transferir e o que NÃO transferir

- **Transferir:** luz de sol baixo por persiana (lado direito/fundo), preenchimento quente por rebote, pretos
  violeta, médios âmbar densos, acentos azul-cobalto + rosa empoeirado, **zero verde**, bokeh redondo, lente
  perto do rosto, câmera travada, closes frontais centrados, faixa azul atrás da cabeça, texturas de mundo usado.
- **Não transferir:** o produto, a embalagem e o logo do filme original, o cartão final em azul, o texto na
  tela, a sala de aula e os atores. Não anexe quadros com rosto/logo como referência de imagem; se anexar, use só
  os quadros de luz/cor e escreva o escopo "IGNORE faces, text, products; take light, colour and lens only".
- **Quadros do vídeo mais úteis como referência de luz/cor** (se a plataforma aceitar): 2,6 s (luz de persiana na
  pele), 8,6 s (contra-picado com tubos e persiana brilhando), 12,3 s (top-down, cor e textura da madeira),
  19,2 s (CU frontal centrado, lente e bokeh).
- **Diferença deliberada:** o original corta a ~1,6 s por plano; o filme da Leitura é um plano contínuo de 30 s.
  O estilo é de **imagem**, não de ritmo de montagem.

---

## 11. Como esse style ref entrou no filme da Leitura

Aplicado ao prompt `prompt-seedance-filme-30s-v1-pai.md` (revisão 3): LIGHT (janela de loja com persiana à
direita, luz constante), FILM LOOK, lente 63° colada no rosto, câmera travada em dolly (o recuo de ~1 s vira uma
puxada seca de trilho), paleta sem verde (avental do livreiro passou de verde para mostarda; camiseta do filho
de amarela para rosa-empoeirado; pai de carvão para azul-marinho lavado), faixa azul-cobalto atrás do pai e
NEGATIVE de estilo. Para voltar ao visual anterior (high-key limpo, câmera na mão), reverta o commit
"Apply TARDE DOURADA style ref" ou peça a versão alternativa.
