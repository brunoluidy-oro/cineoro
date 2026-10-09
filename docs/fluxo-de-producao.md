# Fluxo de produção da árvore CINEORO

## A resposta curta

- **A árvore não depende da bíblia.** A bíblia é opcional: vale a pena quando o projeto tem muitas gerações, personagens recorrentes e um look que precisa durar o filme inteiro.
- **O produto final é sempre o prompt**, acompanhado do card de geração, ou um shotlist com vários prompts. A bíblia é a **memória do filme**: um documento intermediário que faz o prompt nº 80 sair com o mesmo look, a mesma voz e os mesmos nomes do prompt nº 1.
- **Sem bíblia**, o diretor decide o look e escreve tudo dentro do próprio prompt. Funciona bem para uma cena, um comercial ou poucas gerações.
- **Com bíblia**, ele cola os blocos fixos dela e decide só o que é específico daquela cena.

## Os modos de entrada

| Você chega com… | O diretor faz | Você recebe |
|---|---|---|
| uma ideia ou uma cena | Modo A: decide, consulta os departamentos e monta | 1 prompt (de 1 a 30 s, com vários planos se precisar) + card |
| um roteiro ou sequência | Modo B: leitura dramática → gerações → prompts | shotlist HTML com todos os prompts e cards |
| um take que deu errado | Modo C: diagnóstico → corrige um bloco → caminho mais barato | diagnóstico + bloco corrigido (ou prompt refeito) |
| um projeto novo (curta, série, campanha) | Modo D: entrevista → bíblia | a skill-projeto (bíblia) para instalar |
| pedido de rostos, cenários e objetos | Modo E: prompts de imagem para os assets | prompts de referência + registro de @TAGs |

## O fluxo completo de um filme (o seu caso: chegar com o roteiro)

```
ROTEIRO
   │
   ▼
1. DIRETOR LÊ ─────────── leitura dramática silenciosa (story): onde vira, onde assenta, quantas gerações.
   │                       Ele nunca reescreve o seu roteiro; se achar um problema, avisa numa linha.
   ▼
2. PROPOSTA DE DIREÇÃO ── antes de travar, abre caminhos: 2 ou 3 linhas de direção diferentes
   │                       (ex.: observacional, autoral/composta, subjetiva). Você escolhe ou mistura.
   ▼
3. BÍBLIA v1 ──────────── (Modo D) look, luz, lente, som, vozes, @TAGs, mundo, regras e EXCEÇÕES
   │                       declaradas (sonho, flashback, clipe, quebra de estilo). Marcada "a testar".
   ▼
4. ASSETS ─────────────── (Modo E) rostos-base, turnarounds, objetos, cenários, vozes.
   ▼
5. TESTE ──────────────── drafts em 480p de 2 ou 3 tipos de cena → ajustes → bíblia v1.1 travada.
   ▼
6. SHOTLIST ───────────── (Modo B) roteiro → cenas → gerações de até 30 s → um prompt completo por
   │                       geração, colando os blocos da bíblia e decidindo o resto cena a cena.
   ▼
7. GERAR E CONFERIR ───── draft → QA → final 1080p.
   │
   ├── deu errado num plano? → Modo C: corrige UM bloco, ou edita só os segundos ruins.
   │
   └── aprendeu algo que vale para o filme todo? → volta para a bíblia (v1.2) → refaz só os
       prompts afetados.
```

## Como funcionam as alterações

| Tipo de alteração | Onde muda | Efeito |
|---|---|---|
| Só um plano (o ator olhou para o lado errado, o nó não abriu) | só no prompt daquele plano, ou numa edição do take | nada mais muda |
| Uma cena que precisa quebrar o estilo (sonho, flashback, memória) | uma **exceção declarada** na bíblia, com escopo | só aquelas cenas usam o bloco da exceção |
| Uma decisão do filme inteiro (look, voz de um personagem, regra de luz) | na **bíblia**, que sobe de versão | o diretor sabe quais prompts usam aquele bloco e refaz só esses |
| Uma falha que se repete (o modelo insiste em X) | regra anti-IA nova na bíblia | todos os prompts seguintes já saem protegidos |

## Quem faz o quê na árvore

O diretor é o único que fala com você e o único que monta o prompt. Os departamentos não escrevem o prompt inteiro: cada um entrega o seu pedaço e diz o que pode dar errado na sua área.

```
                         ┌───────────────┐
            você ──────▶ │   DIRETOR     │ ──────▶ prompt + card / shotlist / bíblia
                         └───────┬───────┘
     ┌──────────┬──────────┬─────┴────┬──────────┬──────────┬──────────┬──────────┐
   story   performance   camera     light      sound      space     assets    realism
 (cortes)   (atuação)   (lente)    (luz)      (voz)    (quem onde) (referência)(anti-IA)
                                                                       │
                                                                     bible ── só no Modo D
```
