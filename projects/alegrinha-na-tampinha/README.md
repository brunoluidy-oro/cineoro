# Alegrinha na Tampinha (título de trabalho)

Filme de 60″ para o iogurte **Laticínios Porto Alegre** (bandeja de 540 g, 6 potes de 90 g) e a promoção dos chaveiros Alegrinha. Seedance 2.5 com a skill CINEORO.

**Status:** decupagem v0.6. Os prompts de **vídeo** ainda não foram escritos, a pedido. Abra `shotlist.html` para tudo.

## Decisões do diretor

- **Formato 16:9.**
- **Tom cômico** em todo o filme (takes, timing, direção). Sem gags específicos.
- **Captação:** cozinha brasileira de verão, luz natural, macro com lente probe. Look da Codemig (negativo colorido 35 mm), bloco travado no HTML, ajustado para 16:9. **Só na captação.**
- **Plano 1:** POV da geladeira. A câmera começa dentro dela, o homem abre a porta e pega um produto que ainda não vemos.
- **Fábrica:** tudo fosco, **toda em tons de verde da marca** (#8cc647, #69b58f, #2d9577, #46a84f, colunas #006536, branco). Sem look da captação: limpa, sem grão.
- **Travelling horizontal contínuo** o tempo todo, insinuando uma linha de produção. Sem portões. Encadeado por extensão (Extend); se falhar, o corte se esconde atrás de uma coluna. Inserts (de cima, close, macro) entram por cima como cutaways.
- **Vacas** sempre felizes por estarem trabalhando, com o sorriso variando; nunca tristes, bravas ou neutras.
- Cena 1c: sem a tampa que descola com resistência e sem o fio de iogurte.

## O que já temos

Roteiro de 60″ decupado em 8 cenas e 13 gerações (mais 1 opcional) · homem · vaca fosca (model sheet, 3 vistas) · 3 bandejas inteiras · 4 chaveiros · pote real (Element `prop_pote-morango-real`).

## O que falta

**Você gera as imagens**
1. Cozinha de verão: 2–3 placas (cozinha, interior da geladeira, balcão), no look da Codemig.
2. Fábrica: panorama-mestre dos 4 setores e uma placa por setor, em vinil fosco e tons de verde.
3. Alegrinha completa: close do rosto, mãos, 4 figurinos (Seletora, Cientista, Som, Pintora) e folha de expressões felizes.
4. Toons: bandeja, pote e kit de props (prompts da bandeja e do pote em `assets-prompts.md`).

**Pós (pode vir depois)**: logo vetorial, tipografia dos letterings, arte da mensagem da tampa, layout da cartela, locução, SFX do “créqui”, trilha.

**Eu faço**: os prompts de vídeo, depois que as imagens 1–3 estiverem prontas.

Perguntas pequenas, com padrão já adotado, estão no HTML (seção Perguntas).

## Estrutura do filme

| Cena | Mundo | Gerações | No filme |
|---|---|---|---|
| 1 | captação | 1a POV da geladeira (6 s) · 1b o créqui (5 s) · 1c tampa e lambida (6 s) | 0″–14″ |
| 2 | captação | 2a mergulho no iogurte (4 s, 3 usados) | 14″–17″ |
| 3–6 | animação | espinha contínua (3a 7 s → 4a 7 s → 5a 7 s → 6a 8 s) + inserts 3b, 4b, 5b, 6b (8 s cada) | 17″–46″ |
| 7 | captação | 7a a vitória (6 s) · 7b macro da tampa (4 s, opcional) | 46″–52″ |
| 8 | pós | assinatura, cartela, chaveiros | 52″–60″ |

Tempos nominais: os setores dependem da locução real.

## Arquivos

- `shotlist.src.html`: fonte editável da página.
- `shotlist.html`: página final (gerada).
- `assets_prompts.py`: prompts de imagem (fonte). `assets-prompts.md`: os mesmos, em texto puro (gerado).
- `build.py`: gerador. Rode `python3 build.py` nesta pasta.
- `thumbs/`: miniaturas dos assets recebidos (os originais não estão no repositório).

## Fora do roteiro

O character ref da mãe (`char_mom`) foi enviado, mas o filme de 60″ só tem o homem. Não usado.
