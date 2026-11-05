# Alegrinha na Tampinha (título de trabalho)

Filme de 60″ para o iogurte **Laticínios Porto Alegre** (bandeja de 540 g, 6 potes de 90 g) e a promoção dos chaveiros Alegrinha. Seedance 2.5 com a skill CINEORO.

**Status:** decupagem v0.2. Os prompts de **vídeo** ainda não foram escritos, a pedido. Os prompts de **imagem** dos sheets de produto (GPT) estão prontos em `assets-prompts.md`. Abra `shotlist.html` para tudo o mais.

## Decisões do diretor

- Tom cômico em todo o filme (takes, timing, direção): comédia seca, com seriedade como motor.
- Plano 1 é o POV da geladeira: a câmera começa dentro dela, o homem abre a porta e pega um produto que ainda não vemos.
- Captação: cozinha brasileira de verão, muita luz natural, closes de macro com lente probe (referência: Laowa 24 mm f/14 2x) sobre bandeja, tampa e o pote que se parte. Textura a basear no filme da Codemig (**pendente**: preciso de quadros ou descrição).
- Fábrica: tudo fosco (vinil macio, como a model sheet da vaca). Travelling lateral como take-base ("espinha"), intercalado com inserts (de cima, close, macro).

## Estrutura do filme

| Cena | Mundo | Gerações | No filme |
|---|---|---|---|
| 1 | captação | 1a POV da geladeira e revelação (6 s) · 1b o créqui (5 s) · 1c tampa e lambida (6 s) | 0″–14″ |
| 2 | captação | 2a mergulho no iogurte (4 s, 3 usados) | 14″–17″ |
| 3 | animação | Setor Sabores: 3a espinha (6 s) · 3b inserts (8 s) | 17″–24″ |
| 4 | animação | Setor Polpa: 4a · 4b | 24″–31″ |
| 5 | animação | Setor Créqui: 5a · 5b | 31″–38″ |
| 6 | animação | Setor Tampinha: 6a · 6b | 38″–46″ |
| 7 | captação | 7a a vitória (6 s) · 7b macro da tampa (4 s, opcional) | 46″–52″ |
| 8 | pós | assinatura, cartela, chaveiros | 52″–60″ |

13 gerações, mais 1 opcional. Tempos nominais: os setores (7–8 s) dependem da locução real.

## Bloqueia o primeiro draft (P0)

1. Foto do pote avulso + tampa (real).
2. Cozinha de verão (placas) e os quadros da Codemig.
3. Fábrica: planta, panorama-mestre e uma placa por setor.

A model sheet da Alegrinha (vinil fosco, 3 vistas) já chegou. Falta close do rosto, mãos, figurinos e folha de reações.

## Arquivos

- `shotlist.src.html`: fonte editável da página.
- `shotlist.html`: página final (gerada).
- `assets_prompts.py`: prompts de imagem dos produtos (fonte).
- `assets-prompts.md`: os mesmos prompts em texto puro (gerado).
- `build.py`: gerador. Rode `python3 build.py` nesta pasta.
- `thumbs/`: miniaturas dos assets recebidos (os originais não estão no repositório).

## Fora do roteiro

O character ref da mãe (`char_mom`) foi enviado, mas o filme de 60″ só tem o homem. Não usado.
