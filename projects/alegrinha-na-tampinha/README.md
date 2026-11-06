# Alegrinha na Tampinha (título de trabalho)

Filme de 60″ para o iogurte **Laticínios Porto Alegre** e a promoção dos chaveiros Alegrinha. Seedance 2.5 com a skill CINEORO.

**Status:** direção das cenas e prompts de vídeo prontos (v1.9). Abra `shotlist.html`: cada geração tem o seu prompt recolhido e, no fim, a previsão de créditos.

**v1.9:** 1a vira um plano só de 4 s (ele tira uma dupla da geladeira e fecha a porta; sem bandeja, sem o plano andando); 1d passa a 15 s; previz de quebra e tampa saem como referência de vídeo (o motor copiou o movimento robótico e as mãos de boneco); 1b plano 2 em três quartos; iogurte no foil em camada real de 2–3 mm.

**v1.3** (feedback do rascunho do 1d): itens sem rótulo na porta da geladeira; 1a/1d plano 2 é ele andando e saindo do quadro com a bandeja, geladeira fechada, sem olhar para a câmera; lente macro reescrita (24 mm tipo Laowa Probe, quadro 16:9 cheio, sem borda circular nem olho de peixe) com base em reviews do visual da lente; o créqui é uma dobra para dentro, um polegar sobre cada copo (também para a vaca da fábrica); momento nostálgico com olhar subindo de leve e câmera de fato em high angle; foil com mais iogurte colado e movimento contínuo para a frente seguindo a abertura; lambida mais perto, em três quartos, com congelamento no fim. O layout da cozinha agora segue o que o rascunho mostrou: sol e azulejo à esquerda, geladeira à direita, balcão à esquerda.

**v1.2:** novo prompt **1d** (1a + 1b + 1c numa geração só, 17 s, 6 planos, alternativa às três separadas). 1a agora é plano médio fixo com ele segurando a bandeja (sem plano fechado e recuo); 1b sem a pausa antes do créqui; 1c com o iogurte no lado prateado do foil, que ele lambe; sem fumaça nem vapor na geladeira e sem exageros. (O layout do balcão foi revisto na v1.3.)

**v1.1:** os prompts de vídeo foram refeitos na espinha completa da CINEORO (a v1.0 tinha uma versão comprimida sem atuação, quem é quem, geometria e física). Cada rosto do homem tem o bloco ACTING completo (evento, motivo, objetivo, obstáculo, tática, momento a momento, olhos vivos, NOT). As vacas pequenas na espinha de 30 s usam a forma curta. Tamanho: 900 a 2.000 palavras por prompt.

## Regras do filme

- 60″, 16:9. Comédia seca: o humor vem da atuação e do timing.
- Captação: cozinha de verão, luz natural, macro com sonda. Look da Codemig (negativo 35 mm), só na captação.
- Fábrica: vinil fosco, meio monocromática em verde, limpa. Alegrinhas sempre felizes trabalhando.
- Um travelling horizontal contínuo de 30 s (uma geração) atravessa os 4 setores; inserts de cima e closes entram por cima.
- Texto, locução, trilha e SFX na pós. O tempo se ajusta cortando.

## Regras que valem para todos os prompts

- **Foil, nunca “tampa”**: a vedação é uma lâmina de alumínio impressa em verde, macia e maleável. Sem aba, sem “PUXE” e sem mensagem escrita.
- A bandeja de 6 aparece só no 1a. Do 1b em diante é uma dupla de dois iogurtes unidos, separada da bandeja fora de quadro.
- Abertura do 3a ainda em aberto: A (a vaca limpa a lente) ou B (a lente se limpa sozinha). Os dois prompts existem.

## Elements (Higgsfield)

`@man-portoalegre` · `@loc_cozinha` · `@loc_fabrica` (panorama isométrico) · `@char_vaca-vinil` · `@char_alegrinha-looks` · `@prop_bandeja-morango` (só no 1a) · `@prop_pote-morango` · `@prop_pelucia-fabrica` / `-frutas` / `-morango`

No 1b ele já tem uma **dupla** (2 iogurtes unidos), separada da bandeja fora de quadro; o créqui separa a dupla em duas unidades.

Sem referência por enquanto (o motor deduz do texto; se falhar, criamos): a dupla, o interior da geladeira (POV do plano 1a) e a fábrica vista de lado.

## Estrutura

| Cena | Gerações | No filme |
|---|---|---|
| 1 | 1a POV da geladeira · 1b o créqui · 1c foil e lambida (ou 1d, as três juntas) | 0″–14″ |
| 2 | 2a mergulho no iogurte | 14″–17″ |
| 3–6 | 3a espinha (30 s) + inserts 3b, 4b, 5b, 6b | 17″–46″ |
| 7 | 7a a vitória | 46″–52″ |
| 8 | pós | 52″–60″ |

## Arquivos

- `shotlist.src.html` / `shotlist.html`: a página de direção das cenas (o `.html` é gerado por `python3 build.py`).
- `assets-prompts.md` (e `assets_prompts.py`): prompts de imagem já usados (pote real, bandeja e pote toon, looks e expressões da Alegrinha).
- `thumbs/`: miniaturas antigas dos assets (a página enxuta não usa mais).
- `video-prompts.md` (fonte: `video_prompts.py`): os prompts de vídeo, em inglês, e os preços de crédito da previsão.
