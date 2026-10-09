A bíblia está pronta. Montei no mesmo formato da do ANERNEQ: uma **skill de projeto** na pasta `project-sertao/`.

```
project-sertao/
├── SKILL.md                      ← a bíblia: templates fixos, @TAGs, elenco, vozes, regras anti-IA,
│                                   negativos, estrutura, declaração do diretor, produção
└── references/
    ├── script.md                 ← o filme quebrado em 23 gerações (G01–G23), com estado de entrada/saída e falas
    ├── asset-registry.md         ← registro @TAG completo + prompts de imagem para construir cada asset
    └── reference-prompts.md      ← dois prompts completos prontos (pouso noturno G08 e a virada G19)
```

Instale a pasta como skill. Depois disso, qualquer pedido de plano deste filme ("monta o G05", "faz a cena da cacimba") carrega a bíblia primeiro. Os blocos de luz, look, lente, mundo, vozes e negativos entram em todo prompt copiados letra por letra. É isso que segura o filme igual do primeiro ao último plano.

## O que ficou travado

O sol é o antagonista. A luz é dura e branca, o céu de seca não tem cor nem nuvem, e a paleta é osso, cinza e ocre. **A sombra da aba do chapéu esconde os olhos do pai** o filme todo. Só no último fim de tarde o sol baixo entra por baixo da aba e mostra a névoa nas pupilas: é a luz que o entrega. A cor quente aparece só no fogo, à noite, e o verde só uma vez, no juazeiro.

A câmera anda na altura do Zé e sempre do mesmo lado da trilha. Até a virada ela olha o pai montado de baixo para cima; depois, na altura dele.

A viagem anda sempre da esquerda para a direita do quadro, e **quem guia fica no lado direito**: o pai no dia 1, o filho a partir do dia 2, e no fim o filho puxando o pai pelo cabresto.

Não tem trilha sonora. **O chocalho da vaca-guia é a bússola**: o pai se guia por ele. O aboio é a única melodia e é uma voz: o do pai abre o filme, o do filho, falhando, fecha.

A cegueira nunca é "atuada". Damião nunca tateia. O olhar chega atrasado e pousa um palmo ao lado, a mão fecha no ar e acha no segundo toque, e ele põe a culpa no sol. A cabaça d'água aparece três vezes: na primeira o Zé não vê a mão errar, na segunda o pai recusa, na terceira o Zé vê. **Ninguém diz "cego".**

A lente é esférica 2.39, não anamórfica, porque com o sol perto do quadro a anamórfica puxa riscos de flare. O look é de 35mm colorido.

## O que eu decidi por você (mude o que quiser e a bíblia sobe de versão)

- **Título provisório: CABRESTO.** Nomes que inventei: o cavalo **Tição**, a vaca-guia **Estrela** (com o chocalho) e o **açude do Jatobá**, que é fictício. O sertão é uma composição do Cariri com o Sertão paraibano.
- **Idades:** Damião tem 66 e Zé tem 15. No elenco só entram os dois, o cavalo e as 6 cabeças. Não pus cachorro, jumento nem outras pessoas: quanto menos sujeito, menos cara de IA.
- **Estrutura:** 5 blocos em 23 gerações. São ~7:25 gerados mais ~35 s de título e créditos montados na edição, fechando 8:00.
- **Falas:** o argumento não trazia nenhuma, então propus 16 falas curtas em português do sertão da Paraíba ("Esse sol…", "Tô vendo.", "Bebe tu. Eu num tô com sede.", "Deixa que eu levo, pai. O caminho aqui é ruim."). Estão numa tabela na §6 da SKILL.md para você reescrever.
- **Final:** o filho já guiando o pai, a parede de terra do açude aparece no horizonte. — "Tem água, Zé?" — "Tem, pai." **Nunca mostramos a água.** A mentira que protege muda de boca: começa no "Tô vendo" do pai e termina no "Tem, pai" do filho.
- **Geração:** Higgsfield · `seedance_2_5` · 21:9 · draft 480p → final 1080p (2206×946) · áudio ligado · duração igual à soma da timeline.

**Uma nota de leitura, sem mexer na sua história:** catarata não avança em três dias. Na bíblia ela já está madura. O que a viagem tira do pai são as muletas: o caminho de casa decorado, a luz conhecida. É isso que "ir ficando cego" vira na tela.

## Assets que ainda faltam construir

1. **Rostos-base e looks:** DAMIAO com o estado da noite e o do dia 3 (poeira, lábios rachados e a névoa, feitos por máscara), ZE, e as mãos dos dois.
2. **Animais:** TICAO com sela e cabresto, e ESTRELA com o chocalho.
3. **Objetos sobre fundo neutro:** cabresto, chocalho, cabaça, binga, fumo, peixeira, vara.
4. **Placas de locação:** curral de madrugada, caatinga de dia e de tarde, rio seco, juazeiro, os dois pousos, lajedo e açude.
5. **Vozes:** saem do primeiro take aprovado de cada um (5–10 s limpos).

Os prompts de imagem para tudo isso estão em `asset-registry.md`.

## Próximo passo

Os templates estão na **v1, ainda sem teste**. Antes de produzir, gere em draft os três prompts de referência: G05 (dia), G08 (noite) e G19 (a virada). Gere também o G03, para ver se o aboio sai sem instrumento. Confira o look, a contagem de seis cabeças e se a névoa no olho fica sutil, nem branca. Aí ajustamos os templates uma vez, congelamos na v1.1 e não mexemos mais.

Um aviso: os prompts completos deste filme ficam entre ~2.700 e ~3.000 palavras. Isso é o teto do que já funcionou no Higgsfield. Se algum take ignorar instruções, a primeira coisa a fazer é encurtar o texto do plano, nunca os templates.
