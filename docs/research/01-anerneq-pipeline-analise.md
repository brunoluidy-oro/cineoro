# Análise do pipeline ANERNEQ (Higgsfield · Seedance 2.5)

Fonte: os 5 links de geração enviados (projeto "ANERNEQ — full film", Higgsfield Original Series), a página do projeto (`/original-series/anerneq/full-film`, seção *Project brief*) e o arquivo `ANERNEQ_SKILL_v6_EN.md`.
Método: os metadados e o prompt final de cada geração foram lidos pela API pública do Higgsfield (`fnf/folder-items/{id}`). Os vídeos foram baixados, e os cortes, detectados com ffmpeg (`select='gt(scene,0.25)'`). A partir deles, foram montados contact sheets de 1 quadro por segundo.

> O que vale para a skill nova é a **metodologia**. Personagens, idioma (conlang em cirílico), figurino, cultura e roteiro do ANERNEQ foram descartados, conforme pedido.

---

## 1. Metadados das 5 gerações

| # | Data (UTC) | Modelo (`job_set_type`) | Duração pedida | Shots/cortes no prompt | Cortes detectados no vídeo | Referências anexadas | Tamanho do prompt |
|---|---|---|---|---|---|---|---|
| 4 | 2026-08-20 | `seedance_2_5` | 20 s | 1 take, 0 cortes (~14 s) | nenhum | 5 imagens + 1 element (personagem) | 19.261 caracteres |
| 5 | 2026-08-27 | `seedance_2_5` | 30 s | 5 shots, 4 cortes (~26 s) | 5,9 · 11,5 · 16,7 · 20,2 s | 7 imagens + 1 vídeo + 1 element | 7.078 |
| 3 | 2026-09-05 | `seedance_2_5` | 30 s | 6 beats, 5 jump cuts (~21 s) | 3,5 · 6,9 · 10,0 · 18,9 · 28,8 s | 2 elements (personagem + ambiente) | 7.816 |
| 1 | 2026-09-08 | `seedance_2_5` | 21 s | 4 shots, 3 cortes | 4,7 · 10,2 · 14,6 s | 3 imagens + 1 element | 9.126 |
| 2 | 2026-09-10 | `seedance_2_5` | 22 s | 5 shots, 4 cortes | 2,9 · 6,4 · 10,4 · 12,1 s* | 2 imagens (keyframes) + 1 áudio + 3 elements | 13.804 |

\* No #2, o detector também marca como corte o empurrão (movimento brusco). A sequência de planos bate com o prompt.

Parâmetros comuns às 5 gerações: `resolution: 1080p`, `aspect_ratio: 21:9`, `generate_audio: true`, `multi_shots: false`, `multi_shot_mode: custom`, `multi_prompt: []`, `speedramp: auto`, `bitrate_mode: high`, `draft: false`, `prompt_language: en`.
Arquivo entregue: HEVC 2206×946, 24 fps, áudio AAC 32 kHz estéreo.

**Achados técnicos (observados, não documentados oficialmente):**
1. **Multi-shot só por texto.** Todos os vídeos com cortes foram gerados com `multi_shots: false`. Os cortes saíram da linguagem do prompt (`SHOT 1 (~5s) … HARD CUT`, `BEAT 1 (0:00-0:04) … JUMP CUT`), e a ordem e o conteúdo dos planos foram respeitados.
2. **Duração da geração ≠ duração do roteiro, e o modelo estica o final.** No #3 o prompt somava ~21 s, mas a geração foi de 30 s: os beats 4–5 se alongaram (o beat 5 ficou com ~10 s em vez de 4). No #5 (~26 s pedidos, 30 s gerados), o shot 5 virou ~10 s. **Regra derivada:** a duração do job deve ser igual à soma dos tempos do prompt.
3. **Gerações de 20 a 30 s em um único job** foram usadas em produção.
4. **Prompts longos foram aceitos** (até ~19 mil caracteres) e o resultado continuou seguindo as instruções.
5. **Sintaxe das referências no texto salvo:** `<<<uuid-do-element>>>` para Elements (personagem/ambiente salvos), `<<<image_1>>>`, `<<<audio_1>>>` para uploads avulsos. Tags em texto livre (`@NARTY`, `@DOG`) também aparecem, ao lado de imagens anexadas sem marcação explícita.

---

## 2. Como o prompt evoluiu: da v6 (20 blocos) ao formato final

A ordem cronológica mostra a metodologia amadurecendo:

**20/08 (#4): ainda a estrutura de 20 blocos da skill v6**, com três acréscimos:
- `FILM LOCK (KEY — reproduce this exact photographic character)`: uma descrição fotoquímica detalhada da cena (exposição *mid-key*, "NOT underexposed", sombras levantadas e quentes, imagem em duas temperaturas teal × ocre, halation, grão, **"NO vignette, NO edge falloff"**).
- `REFERENCE SCOPE (KEY)`: "as referências fornecem rostos, figurino, físico, mãos, cão e trenó **APENAS**; IGNORE fundo, chão, céu, clima, direção de luz, exposição e grade".
- Recapitulações entre colchetes no fim: `[TOTAL RUNTIME …]` e `[GEOMETRY ANCHOR …]`, que repetem a cena inteira em forma comprimida.

**27/08 (#5): forma mais enxuta**, com os blocos FILM LOOK → LIGHT LOCK → WORLD → CAST → MULTISHOT (5 shots com segundos) → VOICES → AUDIO → CAMERA → **KEEP THE LOGIC — AND THE RESTRAINT** → FILM LOOK REPRISE → NEGATIVE.
- Nova trava de luz entre cortes: "the residual glow LOW on ONE FIXED SIDE of the horizon, same in every shot; the campfire the warm key on the faces, same side, same intensity in every shot".
- O look é repetido no fim ("FILM LOOK REPRISE").
- Referências: rosto, turnaround de figurino, props em fundo neutro, plate de locação, **3 frames de um take anterior** e **o take anterior inteiro como vídeo de referência**. É o ciclo de refação.

**05/09 (#3): estrutura "travas primeiro".**
- REFERENCE USAGE → OFF-SCREEN VOICE → **AXIS & BODY CONTINUITY LOCK** → **CLEAN FRAMES RULE** → CAMERA → SHOT com BEATs em timecode → LIGHT → FILM LOOK → SOUND → WORLD → NEGATIVE → **[ORDER: …]**.
- Cada trava traz a consequência: "WRONG if her head switches sides between cuts … — regenerate".

**08/09 (#1): regras absolutas numeradas e "alma da cena".**
- REFERENCE USAGE → **WHO GURENAV IS (the soul of the scene — play it, never explain it)** → DIALOGUE → **ABSOLUTE RULES 1–7** ("break one and the take is WRONG, regenerate") → SHOT 1…4 → LIGHT → FILM LOOK → SOUND → WORLD → NEGATIVE → [ORDER].

**10/09 (#2): síntese final.**
- REFERENCE USAGE com **keyframe por shot** ("shot 1 STARTS from this exact frame … and comes alive from it"; "shots 3, 4, 5 CONTINUE this exact look … with no keyframe") e **áudio de referência para a voz de um único personagem**.
- Em seguida vêm: WHO IS WHO — READ FIRST, ABSOLUTE → travas nomeadas (NOBODY HOLDS…, POPULATED BACKGROUND LOCK, VILLAGER FACE LOCK, AXIS & LIGHT, SPEAR AIM LOCK) → STYLE PREFIX (agora um **resumo da linha do tempo** com segundos) → Style → THE SHOT → SPOKEN LINES → CAMERA → LIVING FACE/EYES → CHARACTER ACTING → HYPER-REAL CAPTURE → PHYSICS → AUDIO → [TOTAL RUNTIME recap] → NEGATIVE.

**Padrão final:** identidade e regras no topo (primazia), linha do tempo no meio, look e som depois, negativos e recapitulação no fim (recência). As invariantes críticas aparecem em **3 a 4 lugares**: trava, texto do shot, NEGATIVE e recap.

---

## 3. Catálogo de técnicas (genéricas) com evidência

| Técnica | Evidência (trecho) | Para que serve |
|---|---|---|
| Mapa de papéis das referências | "<<<image_1>>> — KEYFRAME FOR SHOT 1 … <<<audio_1>>> — VOICE REFERENCE FOR RINTYN ONLY" | Cada referência tem **uma** função. Evita o modelo misturar look, identidade e cenário. |
| Escopo da referência | "IGNORE their backdrops, ground, horizon, sky, weather, lighting direction, exposure and colour grade" | Impede que o fundo ou a luz da foto de referência contaminem o plano. |
| Keyframe por shot dentro de um multi-shot | "shot 2 STARTS from this exact frame … comes alive from it" | Fixa composição e textura de pele nos shots-chave; os demais "continuam o look". |
| WHO IS WHO com "nunca" | "the ATTACKER: STANDS … NEVER kneels, sits, falls … owns the LEFT side of the frame" | Papéis, lado do quadro e proibições por personagem. Combate troca de identidade. |
| Anticlone | "Omryn's face exists ONCE … no clones, no duplicates" | Rosto do protagonista vazando para a multidão. |
| Trava de contato | "NOBODY HOLDS TYNE (ABSOLUTE) … The only touch on Tyne in the whole scene is Rintyn's single arm in shot 4" | Contato físico inventado pelo modelo. |
| Fundo povoado | "in EVERY shot … the background carries PEOPLE … NEVER an empty street" | Fundo vazio após um corte. |
| Eixo e corpo entre jump cuts | "head toward frame-RIGHT … this orientation NEVER flips … camera stays on ONE side of her body axis" | Personagem trocando de lado entre cortes. |
| Lado iluminado fixo | "lit sides never flip"; "glow LOW on ONE FIXED SIDE of the horizon, same in every shot" | Continuidade de luz entre cortes. |
| Objeto preso à mão | "THE TORCH STAYS IN HIS RIGHT HAND in every shot; the LEFT hand breaks and feeds" | Troca de mão entre cortes. |
| Mira e altura de objeto | "point toward the kneeling girl at her SHOULDER-BLADE height, clearly below her head; it never touches anyone" | Objeto perigoso na altura errada. |
| Regra de quadros limpos | "every beat is ONE clear, deliberate, readable composition … NO accidental crops through a face" | Enquadramentos "moles" típicos de IA. |
| Câmera viva sempre | "NOT ONE SECOND static, locked or stabilized, never a glide" | O padrão do modelo é estabilizar. |
| Começar em andamento | "ONE UNINTERRUPTED TAKE, ALREADY IN PROGRESS AT THE FIRST FRAME" | Evita abertura vazia ou "pose inicial". |
| Final cortado no meio da ação | "Hard end mid-burn" / "Hard end mid-rise" / "End mid-beat" | Evita o modelo "resolver", congelar ou repetir o movimento no final. |
| Voz fora de quadro | "The voice belongs to NOBODY in frame; TYNE'S MOUTH STAYS SHUT … WRONG if her lips move" | Lip-sync aplicado à pessoa errada. |
| Áudio de referência para voz | "his lines keep exactly this voice … all other sound is generated fresh" | Voz idêntica entre gerações. |
| Alma da cena | "WHO GURENAV IS (the soul of the scene — play it, never explain it)" | Dá ao modelo a lógica interna que gera o comportamento. |
| Tática em vez de emoção | "her tactic — MAKE HIM PHYSICALLY IMPOSSIBLE TO LOSE … the tie is rigging, the walk is transit" | Atuação viva sem rótulo de emoção. |
| Mecânica em vez de palavra | "frozen rawhide is stiff and springs back; each knot has to be forced and seats suddenly" | Comportamento crível nas mãos. |
| Over-real material | "OVER-real: the dark greasy frozen rawhide with old knots and ice in its twists…" | Textura específica impede o aspecto "limpo". |
| Exposição sem vinheta | "Even exposure, NO vignette"; "Shadows deep but BREATHING — never crushed" | O modelo escurece cantos e esmaga pretos quando se pede "escuro". |
| Som sujo e diegético | "dirty-real location sound … no metallic ringing, no chimes, no clean digital sheen" | O modelo tende a adicionar "brilhos" musicais. |
| Tambor não é música | "diegetic, slow, spaced — NOT music, NOT a rhythm pattern" | Som percussivo vira trilha. |
| Recap no fim | "[ORDER: FOUR shots, THREE hard cuts, ~21s …]" | Reforço por recência da ordem e das invariantes. |
| Referência nomeada de filme | "a NIGHT still out of The Revenant (Iñárritu / Lubezki)" | Âncora de look, **sempre** acompanhada da descrição observável. |

---

## 4. O que os vídeos mostram

- **#1 (4 shots):** cortes em 4,7 / 10,2 / 14,6 s, perto dos 5/10/15 s pedidos. A tocha fica na mão direita nos 4 shots, o rosto é sempre visível e o shot 4 é externo, como pedido.
- **#2 (5 shots, keyframes):** o shot 1 nasce exatamente do keyframe 1 e o shot 2 do keyframe 2. Os shots 3–5 mantêm grade e textura sem keyframe. O empurrão para fora do quadro pela direita e a queda com a multidão ao fundo saem como descritos.
- **#3 (jump cuts, 30 s para ~21 s de roteiro):** a orientação do corpo se mantém (cabeça à direita, olhar à esquerda) em todos os cortes. O beat 5 (memória/quase-sorriso) se esticou por ~10 s, efeito do excesso de duração.
- **#4 (take único):** nenhum corte, o take segue a ação mecânica (nós → caminhada → laço), com foreground desfocado "passando".
- **#5 (alternância ele/ela):** a faca fica plana na garganta, sem sangue. O tropeço e a mão no pulso aparecem, e o gesto final (nariz na bochecha) acontece. O shot 5 se esticou.

---

## 5. Contradições entre as fontes, e como a skill nova resolve

| Tema | Skill v6 (ANERNEQ) | cinedance | Prática final (5 prompts) | Decisão na skill nova |
|---|---|---|---|---|
| Negativos | Bloco NEGATIVE longo + biblioteca por tipo de cena | "Positive only"; negativos só locais, sem bloco | NEGATIVE longo e **específico do plano** + travas positivas | **Positivo primeiro, negativo como cerca.** Cada falha prevista vira uma trava positiva + um item no NEGATIVE. Nunca nomear (nem negando) um estilo que você não quer contaminando (ex.: estilo do mapa de staging). |
| Repetição | "Repita o que importa em todos os blocos" | "Diga cada coisa uma vez" | Invariantes em 3–4 lugares | **Repita as poucas críticas (≤5), diga o resto uma vez.** |
| Nomes de equipamento/diretor | "65mm anamorphic", "Vision3 500T" | Proíbe nomes de lente, câmera e diretor; usa FOV em graus | Usa "The Revenant (Iñárritu / Lubezki)" + descrição | **FOV em graus controla o enquadramento; nome de formato ou filme só como âncora de textura, sempre com os resultados observáveis.** |
| Abertura do prompt | STYLE PREFIX no topo | Abre em SCENE CONTEXT, sem prefixo | Abre em REFERENCE USAGE / WHO IS WHO | **Abre com contrato (1 linha) → referências → elenco → cena → travas.** O look vai para o meio e o recap para o fim. |
| Rosto | LIVING FACE/EYES descreve pupilas, piscadas, assimetria | "Sem coreografia facial; dê uma tarefa aos olhos" | Os dois juntos | **Duas camadas:** a TAREFA (causa) e a FISIOLOGIA VIVA (sacadas, piscar irregular, assimetria, um detalhe involuntário). Nunca coreografar a *emoção*. |
| Tamanho do prompt | "Prompt mais curto = menos slop" | "Densidade só onde importa" | 7–19 mil caracteres | **Subtrair sujeitos e adjetivos, não especificação.** Texto de controle fica, decoração sai. |
| Duração | ~9 s no exemplo | 15 s por prompt | 14–30 s por job | **Duração do job = soma exata dos tempos do prompt**, dentro do limite do modelo. |
| Luz | "Underexposed, low-key" fixo | Luz como prioridade, Kelvin | Mid-key quando necessário, "no vignette", sombras que respiram | **Escuro ≠ subexposto.** Descrever a fonte e a queda de luz; travar exposição uniforme sem vinheta. |

---

## 6. O que é do ANERNEQ e foi descartado

Personagens e elenco, a conlang e o dicionário, a fonética do cirílico (fica só o **princípio** "escreva a fala na grafia cuja fonética você quer"), figurino e props específicos (fica o princípio "objeto com função"), o roteiro e as falas, a cultura chukchi composta, a paleta "grafite + âmbar + aurora esmeralda" (fica o método de uma paleta funcional com uma única exceção de cor), as regras sobre "ossos de baleia" (fica o método de **não nomear o objeto e descrever a geometria**) e o formato 21:9 como obrigação (vira uma escolha de projeto).
