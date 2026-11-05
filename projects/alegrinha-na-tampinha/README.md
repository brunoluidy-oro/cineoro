# Alegrinha na Tampinha (título de trabalho)

Filme de 60″ para o iogurte **Laticínios Porto Alegre** (bandeja de 540 g, 6 potes de 90 g) e a promoção dos chaveiros Alegrinha. Seedance 2.5 com a skill CINEORO.

**Status:** decupagem v0.8. Os prompts de **vídeo** ainda não foram escritos, a pedido. Abra `shotlist.html` para tudo.

## Decisões do diretor

- **Formato 16:9.** Sabor-herói **Morango**.
- **Tom cômico** vindo do feeling e da atuação, não de piadas físicas. Sem gags específicos.
- **Captação:** cozinha brasileira de verão, luz natural, macro com lente probe. Look da Codemig (negativo colorido 35 mm), bloco travado no HTML, ajustado para 16:9. **Só na captação.**
- **Plano 1:** POV da geladeira. A câmera começa dentro dela, o homem abre a porta e pega um produto que ainda não vemos.
- **Créqui** é destacar o copo da bandeja (nesses multipacks, normalmente dobrando o copo contra uma linha de quebra; não há fonte sobre esta bandeja, então vale gravar um pote real).
- **Fábrica:** tudo fosco e **meio monocromática em verde**. Limpa, sem grão. Acentos da marca podem aparecer em detalhes.
- **Espinha:** um travelling horizontal contínuo de 30 s, **uma geração só**, insinuando uma linha de produção. Sem cortes entre os setores; as paredes com abertura em arco do panorama são atravessadas pela câmera. Inserts (de cima, close, macro) entram por cima como cutaways.
- **Vacas** sempre felizes por estarem trabalhando, com o sorriso variando. O vermelho do chaveiro é a boca dela, não uma coleira.
- **Cena 7:** ele só comemora; nenhum chaveiro aparece. O tempo se ajusta na pós, cortando.

## O que já temos

Roteiro de 60″ decupado em 8 cenas e 10 gerações (mais 1 opcional) · homem · vaca fosca (model sheet, 3 vistas) · 3 bandejas inteiras · 4 chaveiros · pote real (Element `prop_pote-morango-real`) · cozinha (Element `loc_cozinha`) · panorama isométrico da fábrica.

## O que falta

**Você gera as imagens**
1. **Alegrinha:** painel com os 4 looks lado a lado (Seletora, Cientista, Som, Pintora) e painel de expressões felizes. Prompts curtos em `assets-prompts.md`.
2. **Interior da geladeira**, visto de dentro, olhando para fora (o POV do plano 1).
3. **Fábrica vista de lado**, na altura da esteira, de frente para os setores (o ângulo do travelling). O panorama atual é isométrico.
4. Toons: bandeja e pote (prompts em `assets-prompts.md`).

**Pós (pode vir depois)**: logo vetorial, tipografia dos letterings, arte da mensagem da tampa, layout da cartela, locução, SFX do “créqui”, trilha.

**Eu faço**: os prompts de vídeo, depois que as imagens 1–3 estiverem prontas.

**Em aberto**: só a geração opcional 7b (macro da mensagem na tampa).

## Estrutura do filme

| Cena | Mundo | Gerações | No filme |
|---|---|---|---|
| 1 | captação | 1a POV da geladeira (6 s) · 1b o créqui (5 s) · 1c tampa e lambida (6 s) | 0″–14″ |
| 2 | captação | 2a mergulho no iogurte (4 s, 3 usados) | 14″–17″ |
| 3–6 | animação | **3a espinha completa (30 s)** + inserts 3b, 4b, 5b, 6b (8 s cada) | 17″–46″ |
| 7 | captação | 7a a vitória (6 s) · 7b macro da tampa (4 s, opcional) | 46″–52″ |
| 8 | pós | assinatura, cartela, chaveiros | 52″–60″ |

Tempos nominais: você ajusta cortando na pós.

## Arquivos

- `shotlist.src.html`: fonte editável da página.
- `shotlist.html`: página final (gerada).
- `assets_prompts.py`: prompts de imagem (fonte). `assets-prompts.md`: os mesmos, em texto puro (gerado).
- `build.py`: gerador. Rode `python3 build.py` nesta pasta.
- `thumbs/`: miniaturas dos assets recebidos (os originais não estão no repositório).
