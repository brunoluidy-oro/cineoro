# cinedance × ANERNEQ × CINEORO: o que cada uma faz e o que a árvore nova herdou

## Em uma frase

- **cinedance** é uma *skill de ferramenta*: ensina a escrever bons prompts de Seedance 2.0 para qualquer cena (arquitetura de blocos, óptica em graus, tarefa de atuação, leitura dramática, mapa de staging, shotlist HTML).
- **ANERNEQ** é uma *skill de projeto*: a bíblia de um filme específico (20 blocos fixos, templates colados palavra por palavra, vozes, props, idioma, roteiro, 26 lições anti-IA, declaração do diretor).
- **CINEORO** é uma *árvore de direção*: um diretor que orquestra nove departamentos. Ela reúne o rigor de ferramenta da cinedance, a doutrina de verossimilhança do ANERNEQ e as práticas do pipeline final de produção no Seedance 2.5. Também consegue **gerar a bíblia de projeto** para qualquer filme novo.

## Matriz de diferenças

| Aspecto | cinedance | ANERNEQ v6 (+ prompts finais) | CINEORO |
|---|---|---|---|
| Escopo | genérico | um filme | genérico + gerador de bíblias por projeto |
| Modelo-alvo | Seedance 2.0 (15 s) | Seedance 2.5 (prompts finais de 14–30 s) | Seedance 2.5 (4–30 s), com ficha técnica com fontes |
| Estrutura do prompt | ~17 blocos opcionais, abre em SCENE CONTEXT, sem prefixo de estilo | 20 blocos fixos com STYLE PREFIX no topo; no fim, REFERENCE USAGE → regras → shots → look → [ORDER] | **Espinha de 17 blocos**: CONTRACT → REFERENCES → WHO IS WHO → SCENE & SOUL → LOCKS → TIMELINE → … → NEGATIVE → ORDER |
| Estilo | distribuído pelos blocos e adaptado a cada cena | templates fixos colados palavra por palavra | distribuído pelos blocos, mas **congelado na bíblia** e colado palavra por palavra dentro do projeto |
| Negativos | só positivos, travas locais | espinha fixa + biblioteca por cena + específicos do plano | **positivo primeiro, negativo como cerca**: específicos → tipo de cena → espinha |
| Repetição | diga uma vez | repita em todo bloco | **repita só o crítico (≤5) em 4 lugares** |
| Óptica | FOV em graus, árvore de lentes, anti-drift | bloco anamórfico fixo | FOV em graus + bloco de formato como âncora de textura com resultados observáveis |
| Atuação | ACTING TASK (ladder do Tigran), sem coreografia facial | CHARACTER ACTING + LIVING FACE/EYES (fisiologia) | **duas camadas**: tarefa (causa) + olhos vivos (fisiologia), nunca coreografar a emoção |
| Corpo e ação | ambiente físico | "mecânica, nunca palavra", processos completos | biblioteca de mecânica (5 partes: estado, resistência, tentativas, resultado, teste) |
| Espaço | mapa de staging (anti-bleed), palavras mensuráveis | GEOMETRY ANCHOR vindo do Blender | os dois + WHO IS WHO com "NUNCA", lado do quadro, anticlone, mapa de contato |
| Continuidade | travas de multishot | eixo e corpo entre jump cuts; luz fixa por lado | travas de eixo, orientação, mão do objeto, lado iluminado e população; hand-off entre gerações |
| Luz | prioridade, Kelvin, contre-jour | só natural, low-key fixo | fontes motivadas + **"escuro ≠ subexposto"** (sem vinheta, sombras que respiram) + film locks por mundo |
| Som | só a fala do roteiro | voice locks, fala em cirílico, sem música | voice lock, **a grafia guia a fonética** (PT-BR com sotaque), voz off com boca fechada, música banida com sinônimos, silêncio |
| Referências | @tag + hierarquia | REFERENCE USAGE, keyframe por shot, áudio de voz, escopo | **mapa de papéis** (identidade/keyframe/mundo/objeto/voz/movimento/take anterior) + SCOPE + sintaxe por plataforma |
| Iteração | — | refazer o mesmo plano com outra descrição de fala; take anterior como referência | ciclo completo: **draft → final, edição por timestamp, extensão, keyframes de takes aprovados** |
| Dramaturgia | leitura dramática → cobertura (15 s) | declaração do diretor, motivos, loop | leitura dramática → **orçamento por gerações de 4–30 s**, gramática de montagem, motivos |
| Saída | prompt único ou shotlist HTML | prompt de 20 blocos | header de 4 linhas + prompt + **card de geração** (duração = soma, ordem e papel das referências); HTML; reparo |
| Diagnóstico | lista de riscos antes de escrever | 26 lições | riscos antes de escrever + **tabela sintoma → causa → correção → departamento** |
| Projeto | — | é o projeto | `cineoro-bible` gera a skill-projeto (template no formato ANERNEQ) |

## O que é totalmente novo na CINEORO (não estava em nenhuma das duas)

1. **Ficha técnica do Seedance 2.5 com fontes**: limites, referências, idiomas (português incluído), timestamps em segundos inteiros, draft/edit/extend, ausência de campo negativo e de parâmetro multi-shot.
2. **Regra "duração = soma da linha do tempo"**, derivada da análise dos vídeos (o motor estica o final quando sobra tempo).
3. **Card de geração** padronizado em todo prompt.
4. **Caminhos de reparo baratos** (editar segundos, remover música por edição, estender) antes de regenerar.
5. **Tipos de cena para publicidade e vertical/UGC**, além dos tipos cinematográficos.
6. **Mínimo de cada departamento dentro do diretor**, para a árvore funcionar mesmo se só o diretor estiver instalado.
7. **Gerador de bíblia de projeto**, com entrevista, template e critérios de qualidade.
