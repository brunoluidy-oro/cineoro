# Alegrinha na Tampinha (título de trabalho)

Filme de 60″ para o iogurte **Laticínios Porto Alegre** e a promoção dos chaveiros Alegrinha. Seedance 2.5 com a skill CINEORO.

**Status:** direção das cenas v0.9, aguardando o OK do diretor. Os prompts de vídeo saem depois do OK. Abra `shotlist.html`.

## Regras do filme

- 60″, 16:9. Comédia seca: o humor vem da atuação e do timing.
- Captação: cozinha de verão, luz natural, macro com sonda. Look da Codemig (negativo 35 mm), só na captação.
- Fábrica: vinil fosco, meio monocromática em verde, limpa. Alegrinhas sempre felizes trabalhando.
- Um travelling horizontal contínuo de 30 s (uma geração) atravessa os 4 setores; inserts de cima e closes entram por cima.
- Texto, locução, trilha e SFX na pós. O tempo se ajusta cortando.

## Elements (Higgsfield)

`@man-portoalegre` · `@loc_cozinha` · `@loc_fabrica` (panorama isométrico) · `@char_vaca-vinil` · `@char_alegrinha-looks` · `@prop_bandeja-morango` (não entra nos takes de captação) · `@prop_pote-morango` · `@prop_pelucia-fabrica` / `-frutas` / `-morango`

A embalagem em cena é uma **dupla** (2 iogurtes unidos) que o créqui separa em duas unidades; a bandeja de 6 não aparece na captação.

Sem referência por enquanto (o motor deduz do texto; se falhar, criamos): a dupla, o interior da geladeira (POV do plano 1a) e a fábrica vista de lado.

## Estrutura

| Cena | Gerações | No filme |
|---|---|---|
| 1 | 1a POV da geladeira · 1b o créqui · 1c tampa e lambida | 0″–14″ |
| 2 | 2a mergulho no iogurte | 14″–17″ |
| 3–6 | 3a espinha (30 s) + inserts 3b, 4b, 5b, 6b | 17″–46″ |
| 7 | 7a a vitória (+ 7b opcional) | 46″–52″ |
| 8 | pós | 52″–60″ |

## Arquivos

- `shotlist.src.html` / `shotlist.html`: a página de direção das cenas (o `.html` é gerado por `python3 build.py`).
- `assets-prompts.md` (e `assets_prompts.py`): prompts de imagem já usados (pote real, bandeja e pote toon, looks e expressões da Alegrinha).
- `thumbs/`: miniaturas antigas dos assets (a página enxuta não usa mais).
