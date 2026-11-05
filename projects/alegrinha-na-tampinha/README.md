# Alegrinha na Tampinha (título de trabalho)

Filme de 60″ para o iogurte **Laticínios Porto Alegre** (bandeja de 540 g, 6 potes de 90 g) e a promoção dos chaveiros Alegrinha. Produzido no Seedance 2.5 com a skill CINEORO.

**Status:** decupagem v0. Prompts ainda **não** escritos, a pedido. Abra `shotlist.html` para a decupagem completa (direções, planta da fábrica, assets, gerações, pós, perguntas).

## Estrutura do filme

| Cena | Mundo | Geração | No filme |
|---|---|---|---|
| 1 | captação | 1a · 14 s · 3 planos | 0″–14″ |
| 2 | captação | 2a · 4 s (3 s usados) | 14″–17″ |
| 3 | animação | 3a, 3b (7 s cada, 1 take), 3c (7 s, 3 planos), 3d (8 s, 2 planos) | 17″–46″ |
| 4 | captação | 4a · 6 s | 46″–52″ |
| 5 | pós | assinatura, cartela, chaveiros | 52″–60″ |

Os tempos são nominais; os setores (7–8 s) dependem da locução real.

## Decisões padrão (mudam se você responder diferente)

- Plano 1 = POV do produto (câmera dentro da geladeira); alternativa: primeira pessoa.
- Sabor-herói: Morango. Formato 16:9, 60″.
- Fábrica: mundo em massa fosca (tvN) + Alegrinhas de pelúcia de pelo curto (mesmo material do chaveiro). Direções A/B/C comparadas no HTML.
- Faixa lateral contínua, uma esteira, quatro portões em arco, três vacas por setor, luz principal viajando com a câmera no lado esquerdo.
- Todo texto (letterings, logo, mensagem da tampa, assinatura) em pós. Locução, trilha e SFX em pós.
- Sem blockout 3D por enquanto; gatilho para fazê-lo descrito no HTML.

## Assets que bloqueiam o primeiro draft (P0)

1. Foto do pote avulso + tampa (real).
2. Placas da cozinha e da geladeira (esperam o style ref da captação).
3. Model sheet 3D da Alegrinha (sem argola nem corrente).
4. Fábrica: planta, panorama-mestre e uma placa por setor.

## Arquivos

- `shotlist.src.html`: fonte editável.
- `shotlist.html`: página final (gerada por `python3 build.py`, miniaturas embutidas).
- `thumbs/`: miniaturas dos assets recebidos (os originais não estão no repositório).
- `build.py`: gerador.

## Fora do roteiro

O character ref da mãe (`char_mom`) foi enviado, mas o filme de 60″ só tem o homem. Não usado.
