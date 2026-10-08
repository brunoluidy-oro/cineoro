# CINEORO: árvore de direção para Seedance 2.5

Um conjunto de **10 skills do Claude** para dirigir e escrever prompts de vídeo no **Seedance 2.5** (Higgsfield, Dreamina, BytePlus, fal, Replicate). O objetivo é que o resultado pareça live-action crível, não "vídeo de IA".

A árvore une três fontes:
- a skill **cinedance** (arquitetura de prompt, óptica em graus, tarefa de atuação, leitura dramática, mapa de staging, shotlist);
- a skill-projeto e o pipeline final do **ANERNEQ** (verossimilhança, anti-IA, voice locks, templates congelados, referências por papel, multi-shot de 20–30 s);
- a **documentação oficial do Seedance 2.5**, pesquisada com fontes.

## A árvore

```
cineoro-director        RAIZ: recebe o pedido, chama os departamentos, monta o prompt, QA, card de geração
├── cineoro-story       dramaturgia e decupagem (quantas gerações, quantos planos, onde cortar)
├── cineoro-performance atuação: tarefa em vez de emoção, olhos vivos, corpo como mecânica
├── cineoro-camera      câmera e óptica: FOV em graus, operador, composição, looks de lente
├── cineoro-light       luz e look: fontes motivadas, exposição, film locks, cor
├── cineoro-sound       voz e som: falas, sotaque, voice lock, voz off, som diegético, sem música
├── cineoro-space       espaço e continuidade: WHO IS WHO, geometria, eixo, multidão, previz
├── cineoro-assets      referências: papéis, keyframes, assets, draft/edição/extensão
├── cineoro-realism     verossimilhança: anti-IA, física, negativos, diagnóstico de takes
└── cineoro-bible       gera a skill-projeto (a "bíblia" do filme, no formato ANERNEQ)
```

O **diretor** é a porta de entrada: você pede uma cena e ele aciona os departamentos.
Cada departamento também funciona sozinho. Exemplos: "o olhar ficou de vidro" aciona atuação; "saiu música no fundo" aciona som.
O diretor tem um "mínimo" de cada departamento embutido, então funciona mesmo que você instale só ele. Mas o resultado é melhor com a árvore completa.

## O que você recebe em cada pedido

1. **Header em linguagem simples** (4 linhas: o que acontece, o que é dito, tempos, como termina).
2. **O prompt**, em inglês e na ordem da espinha CINEORO. As falas ficam no idioma original, por exemplo português com sotaque nomeado.
3. **Card de geração**: duração (igual à soma dos tempos), aspecto, resolução, áudio, e quais referências subir, em que ordem e com que papel.

Outros modos: **shotlist HTML** para roteiros, **reparo** de take que falhou (diagnóstico + bloco corrigido + caminho mais barato), **bíblia de projeto** e **prompts de assets**.

## Instalação

Os pacotes prontos estão em [`dist/`](dist/), um `.skill` por skill (o arquivo é um `.zip`).

- **claude.ai / app do Claude:** envie cada arquivo `.skill` na área de Skills das configurações. Instale pelo menos `cineoro-director`; o ideal é instalar as 10.
- **Claude Code:** copie as pastas de [`skills/`](skills/) para `~/.claude/skills/` (ou para `.claude/skills/` do projeto).

> **Conflito com a cinedance:** as duas disparam com "prompt de Seedance". Se mantiver as duas ativas, peça explicitamente "usa o cineoro" ou desative a cinedance. A CINEORO cobre tudo o que ela fazia.

## Como pedir

- "Monta o prompt dessa cena pro Seedance 2.5: …"
- "Decupa esse roteiro em prompts e me dá o shotlist."
- "Esse take saiu com cara de IA: [descrição/prompt]. Conserta."
- "Vou começar um curta novo: cria a bíblia do projeto."
- "Faz os prompts de referência do personagem (rosto e turnaround)."

## Pesquisa e decisões

- [`docs/research/01-anerneq-pipeline-analise.md`](docs/research/01-anerneq-pipeline-analise.md): análise dos 5 prompts finais do ANERNEQ e dos vídeos gerados (cortes, durações, referências), além das contradições entre as fontes e como foram resolvidas.
- [`docs/research/02-seedance-2.5-tecnico.md`](docs/research/02-seedance-2.5-tecnico.md): brief técnico do Seedance 2.5 com fontes, separando o que é oficial, o que foi relatado e o que não foi verificado.
- [`docs/research/03-comparacao-cinedance-anerneq-cineoro.md`](docs/research/03-comparacao-cinedance-anerneq-cineoro.md): o que cada skill faz e o que a árvore herdou.
- [`docs/arquitetura.md`](docs/arquitetura.md): a espinha do prompt, os donos de cada bloco e os modos.
- [`evals/`](evals/): testes da árvore contra a cinedance em 3 pedidos reais.

## Idioma

As skills estão em **inglês**, porque os prompts do Seedance precisam sair em inglês e as duas skills de origem também eram em inglês. Elas reconhecem pedidos em português e mantêm as falas no idioma pedido.
