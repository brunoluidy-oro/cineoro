# Arquitetura da árvore CINEORO

## Por que uma árvore e não uma skill só

O ANERNEQ resolveu **um filme**: uma skill-projeto com tudo dentro (look, vozes, props, roteiro, idioma).
A cinedance resolve **a ferramenta**: arquitetura de prompt, óptica, atuação, staging, shotlist.
A skill nova precisa fazer as duas coisas e ir além, e isso não cabe num único arquivo legível. Por isso ela segue a lógica de um set de filmagem: **um diretor que decide e monta o prompt, e departamentos que respondem por uma área cada**.

- Cada departamento pode ser chamado sozinho (ex.: "conserta os olhos mortos deste prompt" → atuação).
- O diretor tem um **resumo mínimo de cada departamento**, então funciona mesmo que um departamento não esteja instalado.
- Os departamentos não montam o prompt final: entregam **blocos** e **travas** ao diretor.

```
cineoro-director        RAIZ: intake, roteamento, montagem do prompt, card de geração, QA, modos
├── cineoro-story       dramaturgia e decupagem: leitura dramática, cobertura, cortes, orçamento de segundos
├── cineoro-performance atuação: tarefa (ladder), olhos vivos, comportamento, estados alterados, choro
├── cineoro-camera      câmera e óptica: FOV, operador, movimento, composição, formato/anamórfico
├── cineoro-light       luz e look: fontes motivadas, exposição, film lock, cor, flares e artefatos
├── cineoro-sound       voz e som: falas, voice lock, idioma/fonética, voz off, ambiente, silêncio
├── cineoro-space       espaço e continuidade: geometria em números, previz, staging map, eixo, multidão
├── cineoro-assets      referências: assets, papéis das referências, keyframes, ciclo de refação
├── cineoro-realism     verossimilhança: anti-IA, física, mecânica, biblioteca de negativos, diagnóstico
└── cineoro-bible       bíblia do projeto: gera a skill-projeto (como a ANERNEQ) para cada filme
```

## A espinha do prompt (ordem dos blocos)

| # | Bloco | Dono | Obrigatório? |
|---|---|---|---|
| 0 | CONTRACT (formato, duração, nº de shots/cortes, câmera, som) | director | sempre |
| 1 | REFERENCES (cada asset → um papel + escopo) | assets | se houver referência |
| 2 | CAST — WHO IS WHO | space + assets | se houver pessoa/animal |
| 3 | SCENE & SOUL | story + performance | sempre |
| 4 | ABSOLUTE LOCKS (3–7, "WRONG if … — regenerate") | director (coletadas) | sempre |
| 5 | TIMELINE (shots/beats com segundos e tipo de corte) | story + camera + performance | sempre |
| 6 | DIALOGUE & VOICE | sound | se houver voz |
| 7 | ACTING (tarefa + olhos vivos por personagem) | performance | se houver rosto |
| 8 | CAMERA (operador, óptica, foco, horizonte) | camera | sempre |
| 9 | GEOMETRY (posições, distâncias, alturas, eixo, lado iluminado) | space | se houver blocking |
| 10 | PHYSICS & MATERIAL (mecânica, resistência, over-real) | realism | sempre |
| 11 | LIGHT (fonte, direção, lado, exposição) | light | sempre |
| 12 | FILM LOOK (+ NO LENS FLARES) | light + camera | sempre |
| 13 | SOUND (lista diegética, política de música) | sound | sempre |
| 14 | WORLD (época, lugar, cultura material, o que não existe) | bible / story | se o mundo for específico |
| 15 | NEGATIVE (espinha fixa + tipo de cena + falhas deste plano) | realism | sempre |
| 16 | ORDER (recap comprimido da linha do tempo + invariantes) | director | sempre que houver mais de um beat |

**Primazia e recência:** identidade e regras no topo, recap no fim. As invariantes críticas (até 5) aparecem em LOCKS, no texto do shot, no NEGATIVE e no ORDER.

## Fluxo do diretor

1. **Intake** — o que chegou: uma ideia, uma cena, um roteiro, um take que falhou ou um projeto novo?
2. **Header em linguagem simples** (4 linhas, para o diretor humano): o que acontece, o que é dito, quanto dura cada beat, como termina.
3. **Departamentos** — story decide a cobertura; os demais entregam blocos e travas.
4. **Montagem na espinha** + repetição das invariantes críticas.
5. **QA** (checklist) + **card de geração** (duração = soma dos tempos, aspecto, resolução, áudio, ordem e papel das referências).

## Modos

- **A · Prompt único** (padrão): uma geração, de 1 take até multi-shot dentro do mesmo job.
- **B · Shotlist HTML**: roteiro/sequência → cenas → gerações, com copiar e marcar.
- **C · Reparo**: take que falhou → diagnóstico → corrigir **um** bloco → refazer.
- **D · Projeto novo**: chama `cineoro-bible` e gera a skill-projeto (look, vozes, assets, nomes, mundo).
- **E · Assets**: prompts de imagem para rosto, turnaround, props e plates de locação (via `cineoro-assets`).
