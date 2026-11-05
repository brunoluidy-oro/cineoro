# Alegrinha na Tampinha (título de trabalho)

Filme de 60″ para o iogurte **Laticínios Porto Alegre** (bandeja de 540 g, 6 potes de 90 g) e a promoção dos chaveiros Alegrinha. Seedance 2.5 com a skill CINEORO.

**Status:** decupagem v0.5. Os prompts de **vídeo** ainda não foram escritos, a pedido. Abra `shotlist.html` para tudo.

## O que já temos

- Roteiro de 60″ decupado em 8 cenas e 13 gerações (mais 1 opcional).
- Homem (character sheet), vaca fosca (model sheet, 3 vistas), 3 bandejas inteiras, 4 chaveiros, **pote real** (Element `prop_pote-morango-real`).
- Look da captação: negativo colorido 35 mm, bloco travado (texto da Codemig) no HTML.
- Decisões: POV da geladeira no plano 1 · espinha lateral intercalada com inserts · tudo fosco · tom cômico, sem gags específicos.

## O que falta

**Você decide**
1. Formato: o look da Codemig é 21:9. O filme da Porto Alegre é 21:9 ou 16:9? (padrão: 16:9)
2. O look da Codemig vale só na captação, com a fábrica limpa e sem grão? (padrão: sim)
3. Rosto da vaca: sorriso fixo ou com reações? (padrão: fixo)

**Você gera as imagens**
1. Cozinha de verão: 2–3 placas (cozinha, interior da geladeira, balcão), no look da Codemig.
2. Fábrica: panorama-mestre dos 4 setores e uma placa por setor, em vinil fosco.
3. Alegrinha completa: close do rosto, mãos e 4 figurinos (Seletora, Cientista, Som, Pintora).
4. Toons: bandeja, pote e kit de props (prompts da bandeja e do pote em `assets-prompts.md`).

**Pós (pode vir depois)**: logo vetorial, tipografia dos letterings, arte da mensagem da tampa, layout da cartela, locução, SFX do “créqui”, trilha.

**Eu faço**: os prompts de vídeo, depois que as decisões e as imagens acima estiverem fechadas.

## Estrutura do filme

| Cena | Mundo | Gerações | No filme |
|---|---|---|---|
| 1 | captação | 1a POV da geladeira (6 s) · 1b o créqui (5 s) · 1c tampa e lambida (6 s) | 0″–14″ |
| 2 | captação | 2a mergulho no iogurte (4 s, 3 usados) | 14″–17″ |
| 3 | animação | Setor Sabores: 3a espinha (6 s) · 3b inserts (8 s) | 17″–24″ |
| 4 | animação | Setor Polpa: 4a · 4b | 24″–31″ |
| 5 | animação | Setor Créqui: 5a · 5b | 31″–38″ |
| 6 | animação | Setor Tampinha: 6a · 6b | 38″–46″ |
| 7 | captação | 7a a vitória (6 s) · 7b macro da tampa (4 s, opcional) | 46″–52″ |
| 8 | pós | assinatura, cartela, chaveiros | 52″–60″ |

Tempos nominais: os setores (7–8 s) dependem da locução real.

## Arquivos

- `shotlist.src.html`: fonte editável da página.
- `shotlist.html`: página final (gerada).
- `assets_prompts.py`: prompts de imagem (fonte). `assets-prompts.md`: os mesmos, em texto puro (gerado).
- `build.py`: gerador. Rode `python3 build.py` nesta pasta.
- `thumbs/`: miniaturas dos assets recebidos (os originais não estão no repositório).

## Fora do roteiro

O character ref da mãe (`char_mom`) foi enviado, mas o filme de 60″ só tem o homem. Não usado.
