#!/usr/bin/env python3
"""Gera o shotlist CINEORO do VT CODEMIG 60" em HTML e Markdown.

Uso: python3 build.py   (gera codemig-vt60-shotlist.html e .md nesta pasta)
"""
import html
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import assets as A  # noqa: E402
import generations as G  # noqa: E402
import templates as T  # noqa: E402

BLOCOS = {
    "ab": ("Abertura", "--b1"), "rv": ("Revezamento", "--b2"), "vr": ("Virada", "--b3"),
    "mc": ("Match cut", "--b4"), "cx": ("Conexão", "--b5"), "fc": ("Fechamento", "--b6"),
}


def hdr(acontece, dito, tempo, termina, direcao):
    return (f"O QUE ACONTECE: {acontece}\nO QUE É DITO: {dito}\nTEMPO: {tempo}\n"
            f"COMO TERMINA: {termina}\nDIREÇÃO: {direcao}")


SCENES = [
    dict(id="T01", b="ab", t="Pico da montanha", d=4.7,
         desc="O jovem, de costas pro mar de morros, vira e diz a primeira frase do filme.",
         gens=[dict(id="T01", label="8s · 1 take · 16:9", prompt=G.T01,
                    header=hdr("No alto de um pico, o jovem olha o mar de morros de costas pra câmera; vira e fala com quem assiste, enquanto a câmera chega nele num único travelling.",
                               "JOVEM: \"Em Minas, terra não é só terra.\"",
                               "olha o horizonte, câmera avançando — 3s · vira — 1s · fala — 3s · segura o olhar — 1s = 8s",
                               "corte seco com ele sustentando seu olhar, boca fechada.",
                               "abertura composta (registro autoral): um travelling único e lento leva do plano aberto ao médio, para a terra ser o assunto antes do rosto e o lipsync ter leitura. A luz baixa da esquerda volta idêntica no T16."),
                    card=G.card("reference-to-video", 8,
                                ["@JOVEM (character sheet) — identidade", "@PICO (plate) — mundo"],
                                "draft primeiro: conferir se o primeiro frame já tem ele no terço esquerdo e se o dolly não vira drone. No corte entra só o trecho de 1,5s antes da virada até o fim da fala (~4,7s)."),
                    alt="ALTERNATIVE DIRECTION: o EWS original — câmera parada a ~40 m, ele minúsculo na pedra, a fala com lipsync quase ilegível. Mais escala e mais terra, menos rosto.")]),
    dict(id="T02", b="ab", t="A terra vira escola (transição + T03)", d=4.5,
         desc="A câmera afunda na terra, passa pelo minério e pelo aço do teto e pousa na sala de aula.",
         gens=[dict(id="T02-B1", label="5s · 1 take · 16:9", prompt=G.T02B1,
                    header=hdr("A câmera desce dos pés do jovem e mergulha na terra: raízes, solo, rocha, até um veio escuro de minério de ferro encher o quadro.",
                               "nada.",
                               "botas na terra vermelha — 1s · entra no chão — 1s · camadas passando, acelerando — 2s · minério enche o quadro — 1s = 5s",
                               "quadro tomado de minério escuro, a câmera ainda descendo. É ali que fica o corte escondido para o B2.",
                               "câmera impossível, mas com corpo de câmera real (descendo um talude de escavação), para não virar corte geológico em CGI. A luz do dia morre com a profundidade, sem lanterna inventada."),
                    card=G.card("reference-to-video", 5,
                                ["@JOVEM — só as botas (objeto)", "@PICO (plate) — chão do pico no primeiro segundo"],
                                "se as botas não baterem com o T01 aprovado, use um frame do T01 (pés) como keyframe do beat 1. O corte escondido entra no último frame escuro de minério."),
                    alt=None),
               dict(id="T02-B2 + T03", label="12s · 1 take · 16:9", prompt=G.T02B2,
                    header=hdr("Do escuro do minério surgem vigas de aço; a câmera passa entre elas, atravessa o forro e desce na sala de aula até pousar no aluno, que responde. A professora entra ao lado e arremata.",
                               "ALUNO: \"É futuro.\" / PROFESSORA: \"Minério não é só minério.\"",
                               "minério vira aço — 2s · entre as vigas e pelo forro — 2s · desce e pousa no aluno — 2s · \"É futuro.\" — 1s · ela entra — 1s · \"Minério não é só minério.\" — 2s · os dois seguram — 2s = 12s",
                               "os dois sustentam o olhar; corte seco.",
                               "a câmera viaja rápido na terra e no aço e fica parada assim que pousa. Toda fala acontece em 1x, depois do pouso, o que resolve o risco do speed ramp. Ele ocupa a esquerda sentado, ela a direita em pé, e o prompt trava quem fala quando."),
                    card=G.card("reference-to-video", 12,
                                ["@ALUNO (character sheet) — identidade", "@PROFESSORA (character sheet) — identidade", "opcional: @SALA_ESTADUAL — mundo (se a sala sair genérica)"],
                                "o risco nº 1 é a fala ir para a boca errada. No draft, confira só isso. Fallback: ElevenLabs só na voz da professora. O speed ramp, se ainda quiser, vai na pós e só no trecho de 0 a 6s."),
                    alt=None),
               dict(id="T02-B3 (alternativa)", label="17s · 1 take · 16:9", prompt=G.T02B3,
                    header=hdr("Versão inteiriça: das botas no pico, terra adentro, minério, aço, forro, sala, aluno e professora, tudo numa geração.",
                               "ALUNO: \"É futuro.\" / PROFESSORA: \"Minério não é só minério.\"",
                               "botas — 1s · terra — 3s · minério e aço — 2s · forro — 2s · pouso — 2s · \"É futuro.\" — 1s · ela entra — 1s · fala dela — 3s · seguram — 2s = 17s",
                               "os dois sustentam o olhar; corte seco.",
                               "mesma lógica do B1 + B2, sem corte escondido. É mais orgânico, mas um erro em qualquer trecho obriga a refazer tudo."),
                    card=G.card("reference-to-video", 17,
                                ["@JOVEM — só as botas (objeto)", "@ALUNO (character sheet) — identidade", "@PROFESSORA (character sheet) — identidade"],
                                "só vale gerar depois que B1 e B2 estiverem aprovados como plano B. É mais caro de acertar."),
                    alt="ALTERNATIVE DIRECTION: o T02-A original — drone FPV saindo do ombro do jovem, descendo a encosta, cruzando morros e telhados e entrando pela janela da escola. Conta a mesma cadeia pela superfície em vez de por dentro da terra.")]),
    dict(id="T04", b="rv", t="Estacionamento com eletroposto", d=2.8,
         desc="Homem encaixa o plugue no carro elétrico e fala de lado para a câmera, que passa da esquerda pra direita.",
         gens=[dict(id="T04", label="6s · 1 take · 16:9", prompt=G.T04,
                    header=hdr("Num estacionamento aberto, o homem encaixa o plugue no carro elétrico (a trava só fecha na segunda empurrada) e fala de lado para a lente, enquanto a câmera passa.",
                               "HOMEM: \"É a possibilidade de um mundo mais verde,\"",
                               "encaixa o plugue — 2s · fala de lado — 3s · volta ao cabo — 1s = 6s",
                               "a câmera ainda andando; o corte cai na vírgula, na montagem.",
                               "P1: travelling lateral constante, esquerda → direita, na mesma velocidade em todo o revezamento. A direção de tela é o que costura os cinco takes."),
                    card=G.card("reference-to-video", 6,
                                ["@HOMEM_EV (character sheet) — identidade", "opcional: @CARRO_EV — objeto"],
                                "conferir no draft se a câmera não para nem empurra. O corte entra na vírgula; a sobra antes e depois é a alça de montagem."),
                    alt=None)]),
    dict(id="T05", b="rv", t="Indústria", d=1.8,
         desc="Operário na metalúrgica olha a linha de bobinas, fala por cima do barulho e volta à linha.",
         gens=[dict(id="T05", label="6s · 1 take · 16:9", prompt=G.T05,
                    header=hdr("No chão de uma usina siderúrgica, o operário acompanha uma bobina de aço passando nos roletes, faz um sinal com a mão, fala para a lente e volta os olhos para a linha.",
                               "OPERÁRIO: \"de uma indústria mais eficiente,\"",
                               "olha a linha, sinal com a mão — 2s · fala — 2s · volta à linha, confere você — 2s = 6s",
                               "a câmera ainda andando; corte na vírgula.",
                               "mesmo travelling lateral do revezamento. O olhar vai da máquina pra você, para a fala apontar o que funciona sem ele precisar apontar."),
                    card=G.card("reference-to-video", 6,
                                ["@OPERARIO (character sheet) — identidade + EPI"],
                                "conferir EPI completo e sem logo, e se os olhos estão vivos atrás dos óculos."),
                    alt=None)]),
    dict(id="T06", b="rv", t="Laboratório", d=1.2,
         desc="Pesquisadora tira os olhos da pipeta só pelo tempo da frase.",
         gens=[dict(id="T06", label="5s · 1 take · 16:9", prompt=G.T06,
                    header=hdr("Num laboratório de medicamentos, a pesquisadora pipeta amostras, levanta os olhos para a lente só pelo tempo da frase e volta ao trabalho.",
                               "PESQUISADORA: \"de novas tecnologias,\"",
                               "pipetando — 2s · olha e fala — 2s · troca a ponteira — 1s = 5s",
                               "a câmera ainda andando; corte na vírgula.",
                               "é o take mais curto do filme, então a tática é emprestar dois segundos do experimento e devolver."),
                    card=G.card("reference-to-video", 5,
                                ["@PESQUISADORA (character sheet) — identidade + EPI"],
                                "no corte ficam ~1,2s. Se o draft sair com rótulos legíveis nos frascos, refaça: texto não pode aparecer."),
                    alt=None)]),
    dict(id="T07", b="rv", t="Restaurante", d=1.8,
         desc="Dono serve o prato, espera a reação da cliente e te inclui com um olhar cúmplice.",
         gens=[dict(id="T07", label="6s · 1 take · 16:9", prompt=G.T07,
                    header=hdr("No restaurante de comida saudável, o dono põe o prato diante de uma cliente antiga, espera a primeira olhada dela e então vira o olhar para a lente, cúmplice.",
                               "DONO: \"de uma economia mais sustentável.\"",
                               "serve — 2s · espera a reação dela — 1s · fala para a lente — 2s · volta a ela — 1s = 6s",
                               "a câmera ainda andando; corte no ponto final.",
                               "resolve o que estava em aberto: o olhar sai da cliente no segundo 3, depois que ela olha o prato. A cliente fica de costas, em primeiro plano suave, para não disputar a fala."),
                    card=G.card("reference-to-video", 6,
                                ["@DONO (character sheet) — identidade"],
                                "conferir se a boca da cliente fica fechada e se ela não olha pra lente."),
                    alt=None)]),
    dict(id="T08", b="rv", t="Plantação", d=8.3,
         desc="Agricultora caminha pela soja falando com você; em \"mais raro\" ela para, e a câmera para junto.",
         gens=[dict(id="T08", label="11s · 1 take · 16:9", prompt=G.T08,
                    header=hdr("A agricultora caminha pela lavoura de soja, da esquerda pra direita, mão nas plantas, falando com a lente. Em \"mais raro\" ela para de avaliar as plantas e procura seus olhos, e a câmera para junto.",
                               "AGRICULTORA: \"Enquanto o mundo olha para o nióbio e as terras raras de Minas,\" / \"Minas olha para o que há de mais raro na nossa terra:\"",
                               "caminha — 1s · 1ª frase andando — 4s · confere uma vagem — 1s · 2ª frase começa — 2s · para em \"mais raro\" e termina — 2s · segura — 1s = 11s",
                               "parada, segurando seu olhar; corte para a mina.",
                               "o travelling lateral do revezamento termina aqui. Quando ela para, a câmera para, e a quietude já prepara a virada."),
                    card=G.card("reference-to-video", 11,
                                ["@AGRICULTORA (character sheet) — identidade"],
                                "a aba do chapéu precisa deixar os olhos à vista. Conferir se a parada cai em \"mais raro\"."),
                    alt=None)]),
    dict(id="T09", b="vr", t="Mina de nióbio", d=4.8,
         desc="Onde se espera o minério, aparece a pessoa: o foco sai do minério e vai para ele.",
         gens=[dict(id="T09", label="14s · 1 take · 16:9", prompt=G.T09,
                    header=hdr("Na beira da cava da mina, o quadro abre no minério nítido; o foco passa para o funcionário, que já te olhava. Ele fala, baixa os olhos para o minério e os levanta para você em \"novos caminhos\", terminando a frase inteira.",
                               "FUNCIONÁRIO: \"a nossa gente.\" / \"Afinal, o que cresce aqui também deve construir novos caminhos para quem nasce, vive e trabalha aqui.\"",
                               "minério nítido — 1s · rack para ele — 1s · \"a nossa gente.\" — 2s · olhar desce ao minério — 1s · 2ª frase, olhar sobe em \"novos caminhos\" — 4s · termina a frase — 3s · segura — 2s = 14s",
                               "segurando seu olhar; na montagem o corte cai em \"para quem nasce\" e entra o T10.",
                               "virada composta: quadro travado e um único gesto de câmera, o rack de foco do minério para o homem. Ele diz a frase inteira on camera; esse áudio vira a V.O. do T10 ao T12, com a mesma voz sem esforço. O levantar do olhar dele abre a série do match cut."),
                    card=G.card("reference-to-video", 14,
                                ["@FUNCIONARIO (character sheet) — identidade + EPI", "@MINA (plate) — mundo"],
                                "o áudio de 9 a 12s (\"para quem nasce, vive e trabalha aqui.\") vai para baixo do T10–T12 na montagem. Validar EPI com a SST da operadora antes do final. A pausa depois de \"a nossa gente.\" pode ser apertada na montagem."),
                    alt="ALTERNATIVE DIRECTION: em vez do rack, um plano geral da cava com ele pequeno na borda e um corte seco para o MCU na fala. É mais didático, perde o gesto de \"onde se espera o minério, aparece a pessoa\".")]),
    dict(id="T10", b="mc", t="Mãe com recém-nascido", d=1.2,
         desc="A mãe olha o bebê e levanta os olhos para você, no mesmo ponto da tela do funcionário.",
         gens=[dict(id="T10", label="5s · 1 take · 16:9 · sem fala", prompt=G.T10,
                    header=hdr("A mãe confere a respiração do recém-nascido no colo e levanta os olhos para a lente; os olhos pousam no mesmo ponto da tela onde pousaram os do funcionário.",
                               "nada na geração. Na montagem entra a V.O. do T09: \"para quem nasce,\"",
                               "olhos no bebê — 2s · olhos sobem para a lente — 1s · segura — 2s = 5s",
                               "segurando seu olhar; corte para o T11.",
                               "P2, o match cut pelo levantar do olhar: mesmo quadro (MCU 29°, câmera travada, olhos a 45% da largura no terço superior) do T09 ao T12. Geração muda, para nenhuma boca formar palavras."),
                    card=G.card("text-to-video", 5,
                                ["nenhuma referência (o modelo improvisa mãe e bebê)"],
                                "conferir a proporção do bebê (rosto parcialmente coberto) e se os olhos pousam no ponto marcado. Usar o frame final aprovado do T09 como guia de enquadramento na montagem."),
                    alt=None)]),
    dict(id="T11", b="mc", t="Arquibancada do Mineirão", d=0.8,
         desc="A torcedora segue a bola que sobe e os olhos dela chegam em você.",
         gens=[dict(id="T11", label="5s · 1 take · 16:9 · sem fala", prompt=G.T11,
                    header=hdr("Na arquibancada, a torcedora segura a respiração no lance; a bola sobe, o queixo e os olhos dela sobem junto e pousam na lente.",
                               "nada na geração. Na montagem: V.O. do T09, \"vive,\"",
                               "olhos no lance — 2s · olhos sobem com a bola até a lente — 1s · segura com o estádio crescendo — 2s = 5s",
                               "segurando seu olhar; corte para o T12.",
                               "o levantar do olhar tem motivo físico aqui (a bola subindo). O estádio fica desfocado, então não precisa de plate. Figurino terracota, fora das cores dos clubes e do verde-amarelo."),
                    card=G.card("text-to-video", 5,
                                ["nenhuma referência"],
                                "conferir se nenhuma camisa, bandeira ou cachecol na arquibancada desfocada lembra Atlético, Cruzeiro ou América."),
                    alt=None)]),
    dict(id="T12", b="mc", t="Ônibus: embarque + motorista fala (T12 + T13)", d=6.6,
         desc="O estudante embarca; o motorista o acompanha com os olhos, levanta o olhar para você e explica a rota.",
         gens=[dict(id="T12 + T13", label="15s · 2 planos · 16:9", prompt=G.T12,
                    header=hdr("A porta abre, o estudante sobe e acena, e o motorista responde com a cabeça. Corte: no painel, os olhos do motorista acompanham o menino, sobem para a lente (fechando o match cut), o ônibus sai e ele explica a rota.",
                               "MOTORISTA: \"Se Minas tem o que o futuro procura, esse futuro também precisa chegar até os mineiros.\" (na montagem, a V.O. \"e trabalha aqui.\" do T09 cai no plano 1)",
                               "embarque — 4s · olhos seguem o menino — 1s · olhos sobem para a lente — 1s · ônibus sai — 1s · fala — 5s · estrada e você — 3s = 15s",
                               "dirigindo, olhos voltando à estrada; corte seco.",
                               "duas gerações viraram uma: mesmo lugar, mesmas duas pessoas. O levantar do olhar do motorista é o último elo do match cut e já vira a fala dele, sem emenda."),
                    card=G.card("reference-to-video", 15,
                                ["@MOTORISTA (character sheet) — identidade", "@ESTUDANTE (character sheet) — identidade", "@ONIBUS_INT (plate) — mundo"],
                                "risco: o estudante abrir a boca no embarque. Conferir no draft. O ônibus tem que estar andando quando ele fala."),
                    alt=None)]),
    dict(id="T14", b="cx", t="Sala do Trilhas de Futuro", d=3.8,
         desc="O mesmo estudante do ônibus termina uma ligação elétrica e diz a frase da marca.",
         gens=[dict(id="T14", label="7s · 1 take · 16:9", prompt=G.T14,
                    header=hdr("Na oficina do curso técnico, o estudante aperta o último borne de um painel elétrico, testa o fio e vira para a lente.",
                               "ESTUDANTE: \"É para isso que a Codemig existe… para fazer essa conexão acontecer.\"",
                               "aperta o borne e testa — 2s · vira e fala — 4s · segura — 1s = 7s",
                               "segurando seu olhar; corte seco.",
                               "a ação dele é literalmente fazer uma conexão com as próprias mãos, antes de dizer \"conexão\". \"Codemig\" vai escrito como palavra única, para o modelo não soletrar."),
                    card=G.card("reference-to-video", 7,
                                ["@ESTUDANTE (character sheet) — identidade, mesmo figurino do T12"],
                                "conferir a pronúncia de \"Codemig\" (co-de-MIG). Se sair errado, regerar com outra descrição de entrega antes de mexer na grafia."),
                    alt=None)]),
    dict(id="T15", b="cx", t="Hospital", d=6.8,
         desc="Enfermeira mede a pressão do paciente enquanto fala; só no fim te dá os olhos.",
         gens=[dict(id="T15", label="11s · 1 take · 16:9", prompt=G.T15,
                    header=hdr("Na enfermaria, a enfermeira fecha o manguito no braço do paciente, bombeia e fala enquanto trabalha; solta a válvula e olha para a lente só na última parte da frase.",
                               "ENFERMEIRA: \"Para fazer com que os recursos essenciais para a transição energética que o mundo precisa, também criem oportunidades para Minas.\"",
                               "manguito — 2s · bombeia falando, olhos no paciente — 5s · solta a válvula, olhos na lente — 2s · volta ao paciente — 2s = 11s",
                               "lendo o ponteiro e acenando para o paciente; corte seco.",
                               "a fala longa fica on camera, mas com os olhos no paciente na maior parte (perfil de trabalho, menos risco de lipsync), e só o fim vai para a lente. Ela não para de cuidar."),
                    card=G.card("reference-to-video", 11,
                                ["@ENFERMEIRA (character sheet) — identidade"],
                                "fala longa: se o lipsync escorregar no fim, a saída é a proposta antiga, com o começo da frase em V.O. sobre as mãos e só \"também criem oportunidades para Minas\" on camera."),
                    alt="ALTERNATIVE DIRECTION: a proposta em aberto do pré-shotlist, com a primeira metade da frase em V.O. sobre as mãos no manguito e o corte para o rosto só em \"também criem oportunidades para Minas\". Mais seguro pro lipsync, menos presença dela.")]),
    dict(id="T16", b="fc", t="Montanha: close final", d=8.2,
         desc="O jovem do começo, num close muito fechado, reivindica e convida.",
         gens=[dict(id="T16", label="12s · 1 take · 16:9", prompt=G.T16,
                    header=hdr("No mesmo pico e na mesma hora, o jovem em close bem fechado fala direto com você: a primeira frase firme, depois \"O minério é nosso\" como reivindicação e \"O futuro também\" como convite.",
                               "JOVEM: \"Para transformar a força que vem da nossa terra em mais desenvolvimento para a nossa terra.\" / \"O minério é nosso. O futuro também.\"",
                               "respira — 1s · 1ª frase — 5s · respira — 1s · \"O minério é nosso.\" — 1s · \"O futuro também.\" — 2s · segura — 2s = 12s",
                               "segurando seu olhar; corte para a assinatura.",
                               "fechamento composto: quadro travado a 18°, pele em detalhe (face anchor extra), mesma luz do T01. O travelling da abertura chega nele e aqui ele já está perto."),
                    card=G.card("reference-to-video", 12,
                                ["@JOVEM (character sheet + face anchor de pele) — identidade", "@PICO (plate) — fundo"],
                                "olhos e pele são o take inteiro. Conferir pupila viva e cicatriz na sobrancelha."),
                    alt="ALTERNATIVE DIRECTION: um pull-back lento do close até o plano aberto durante \"O futuro também.\", revelando o mar de morros. Rima invertida com o travelling do T01.")]),
    dict(id="T17", b="fc", t="Assinatura", d=2.5,
         desc="Assinatura final em pós (AE): Codemig. O futuro é mineiro. / Codemge. Abrindo caminhos para Minas crescer.",
         gens=[], post="Sem geração. Locução \"Codemig. O futuro é mineiro.\" gravada (locutor ou ElevenLabs), lettering e logos no After Effects. O pot-pourri saiu por decisão da direção."),
]

STYLE_INTENT = """STYLE INTENT — CODEMIG VT 60"
MEDIUM: live-action photoreal
REGISTER: hybrid — observed-realist in the relay and connection blocks (T04–T08, T14–T15);
          authored-composed at the hinges (T01, T02/T03, T09, T10–T12 match series, T16)
CAMERA LANGUAGE: observed = a breathing handheld operator; relay (P1) = handheld crab-walk
          frame-left → frame-right at one constant pace, cut on the comma; hinges = one deliberate
          move per take (dolly, impossible descent, focus rack) or a locked frame
LIGHT LOGIC: natural motivated; one state-wide rule — the key is always on the frame-LEFT side of
          every face (late-afternoon low sun outside, window daylight inside)
SOUND/MUSIC POLICY: NO music in generation (the score is added in post); location sound only
COLOUR & TEXTURE: muted and true; the red-ochre of Minas earth as the constant; mid-key; very fine
          grain; spherical, round bokeh; no flares
MOTION: real-time; only the T02 descent travels fast, speech always at 1x
REALIST PRESET RULES SWITCHED OFF: "never look into the lens" (direct address is the film's form —
          the viewer is the scene partner); "no score" applies to generation only; "observed
          handheld everywhere" (hinges are composed); "hard end mid-action" (pieces end on a held
          look, the edit's handle)"""

PEND = [
    ("P1", "Linguagem de transição do revezamento (T04–T08)", "decidido",
     "Travelling lateral constante, câmera na mão andando de lado da esquerda para a direita na mesma velocidade, com o corte seco na vírgula de cada frase. Fica diferente do match cut e para junto com a agricultora no T08, preparando a virada."),
    ("P2", "Elemento do match cut (T09–T12)", "decidido",
     "O levantar do olhar. Mesmo quadro em todos (MCU 29°, tripé, olhos pousando no terço superior a ~45% da largura): o funcionário levanta do minério, a mãe do bebê, a torcedora segue a bola, o motorista acompanha o menino. O olhar do motorista vira a fala dele (T13)."),
    ("P3", "Qual \"R\" mineiro em cada personagem", "decidido",
     "R caipira (retroflexo leve) para interior, campo e mineração; R de BH (aspirado, quase h) para a cidade. Agora está escrito no VOICE LOCK de cada personagem, colado literalmente em todo prompt. Se exagerar e virar caricatura, corrigir com ElevenLabs."),
    ("P4", "Falas finais do T16", "decidido", "Sem coro. O protagonista fala as duas frases."),
    ("P5", "Casting e representação", "proposta",
     "Sotaque e fisionomia seguem a mesma divisão. Proposta do diretor para as character sheets: pardos, pretos e brancos distribuídos em proporção próxima à de Minas, sem amarrar ofício a cor. Pesquisadora preta, operário preto, dono do restaurante branco, agricultora parda etc. Validar antes de gerar os sheets."),
    ("P6", "Timing: teto de 60 segundos", "decidido",
     "O corte continua estimado em ~60s (barra acima). Cada geração tem alça de ação antes e depois da fala, e toda a alça é ação escrita, sem tempo morto. Gerações curtas (T04–T07, T10, T11) têm de 5 a 6s, porque o mínimo do Seedance é 4s."),
    ("P7", "Style ref", "a testar",
     "Substituída pelo FILM LOOK v1 (template congelado). Antes de congelar a v1.1, fazer draft de três tipos de cena: T01 (exterior autoral), T05 (interior observado com travelling) e T09 (virada travada com rack)."),
    ("P8", "Especificidade das locações", "decidido",
     "Soja, siderurgia, laboratório de medicamentos e restaurante de comida saudável, como contexto de cena."),
    ("P9", "V.O. do T10 ao T12", "proposta",
     "O funcionário diz a frase inteira on camera no T09 (\"…para quem nasce, vive e trabalha aqui.\"), e esse áudio vira a V.O. dos três takes seguintes. A voz fica idêntica sem depender de voice lock, e T10/T11 saem como gerações mudas, sem risco de boca errada."),
    ("P10", "T12 + T13 numa geração só", "proposta",
     "Mesmo lugar, mesmas duas pessoas, e o levantar do olhar do motorista emenda a fala. Duas gerações viram uma de 15s com um corte."),
    ("P11", "EPI da mina e da siderurgia", "validar",
     "Os sheets trazem um EPI padrão (capacete com jugular, óculos, colete refletivo, luvas, protetor auricular, bota). Confirmar com a SST da operadora o que é obrigatório naquela cava antes da geração final."),
    ("P12", "Takes de preenchimento", "próxima etapa",
     "T04.1, T04.2 etc. entram depois dos drafts dos principais, usando o prompt mínimo do CINEORO com os mesmos templates."),
]

RISKS = [
    ("Mineirão (T11)", "preto e branco, azul e verde remetem a Atlético, Cruzeiro e América, e o verde-amarelo tem carga política. A torcedora veste terracota, e o WORLD e o NEGATIVE do take proíbem camisas, bandeiras e cachecóis. Conferir a arquibancada desfocada também."),
    ("Marcas reais", "Trilhas de Futuro, a operadora da mina, a escola, o ônibus, o carro e o eletroposto saem sem marca e sem texto legível (template WORLD em todo prompt). Logos entram na pós."),
    ("Mineração (T09)", "é o take que a comissão vai olhar com mais atenção. O EPI completo é uma das cinco travas críticas e se repete em quatro lugares do prompt, mas ainda falta validar com a SST (P11)."),
    ("Duas falas numa geração (T02-B2/B3)", "o prompt trava quem fala em qual segundo e ninguém fala enquanto a câmera viaja. O ElevenLabs fica de fallback de voz."),
    ("Recém-nascido (T10)", "plano curto, rosto do bebê parcialmente coberto pela manta e pela mão, proporção travada no WHO IS WHO e no NEGATIVE."),
    ("Speed ramp (T02)", "resolvido na direção: toda fala acontece depois do pouso, em 1x. Se ainda quiser rampa, faça na pós e só de 0 a 6s."),
    ("Olhar para a lente", "o filme inteiro fala com quem assiste, e olhar fixo na lente é onde o olho de vidro mais aparece. Todo ACTING dá tarefa aos olhos (conferir os seus dois olhos) e traz a camada de olhos vivos."),
    ("Pronúncia de \"Codemig\" (T14)", "escrito como palavra única. Se o modelo soletrar ou trocar a tônica, regerar com outra descrição de entrega antes de mexer na grafia."),
]


# ------------------------------------------------------------------ render helpers
def esc(s):
    return html.escape(s, quote=True)


def words(s):
    return len(s.split())


def gen_html(g):
    alt = f'<div class="alt">{esc(g["alt"])}</div>' if g.get("alt") else ""
    return f"""<div class="gen">
  <div class="gen-label"><span>Geração {esc(g['id'])} · {esc(g['label'])}</span>
    <span><button class="copy-btn" data-target="pre.prompt">Copiar prompt</button>
    <button class="copy-btn" data-target="pre.card">Copiar card</button></span></div>
  <div class="header-lines">{esc(g['header'])}</div>
  <details><summary>Prompt CINEORO · {words(g['prompt'])} palavras</summary><pre class="prompt">{esc(g['prompt'])}</pre></details>
  <pre class="card">{esc(g['card'])}</pre>
  {alt}
</div>"""


def scene_html(s):
    bname = BLOCOS[s["b"]][0]
    gens = "".join(gen_html(g) for g in s["gens"])
    if s.get("post"):
        gens = f'<div class="post">{esc(s["post"])}</div>'
    return f"""<article class="scene" id="{s['id']}">
  <div class="scene-header">
    <input type="checkbox" data-scene="{s['id']}" aria-label="{s['id']} aprovado">
    <div class="scene-num">{s['id']}</div>
    <div class="scene-desc"><b>{esc(s['t'])}</b> <span class="blk">{bname} · ~{s['d']}s no corte</span><br>{esc(s['desc'])}</div>
  </div>
  {gens}
</article>"""


def tpl_block(title, text, note=""):
    n = f'<p class="muted">{esc(note)}</p>' if note else ""
    return f"""<div class="gen tpl"><div class="gen-label"><span>{esc(title)}</span>
<span><button class="copy-btn" data-target="pre.prompt">Copiar</button></span></div>{n}
<details><summary>Ver texto</summary><pre class="prompt">{esc(text)}</pre></details></div>"""


def build_html():
    total_cut = sum(s["d"] for s in SCENES)
    n_gens = sum(len(s["gens"]) for s in SCENES)
    timeline = [{"id": s["id"], "t": s["t"], "d": s["d"], "c": BLOCOS[s["b"]][1], "b": s["b"]} for s in SCENES]
    legend = "".join(f'<span><i style="background:var({c})"></i>{n}</span>' for n, c in BLOCOS.values())
    scenes = "".join(scene_html(s) for s in SCENES)

    voices = "\n\n".join(T.voice_lock(k) for k in T.VOICE)
    templates = "".join([
        tpl_block("CONTRACT (padrão)", "CONTRACT — Live-action photoreal film footage, 16:9, [N] seconds total, [takes], [camera language of this take], real-time motion, " + T.LANG + ". NO music, NO score. " + T.TEXT_POLICY + "."),
        tpl_block("FILM LOOK + NO LENS FLARES", T.FILM_LOOK),
        tpl_block("LIGHT · exteriores", T.LIGHT_EXT),
        tpl_block("LIGHT · interiores (base)", T.light_int("[window]", "[practicals]", "[reach]"), "As linhas fixas são literais; só fonte, práticos e alcance mudam por cena."),
        tpl_block("CAMERA · revezamento (P1)", T.rev_camera("[distance]", "[size]")),
        tpl_block("MATCH FRAME (P2)", T.MATCH_FRAME),
        tpl_block("VOICE LOCKS · 12 personagens", voices),
        tpl_block("SOUND · política de música", T.MUSIC_POLICY),
        tpl_block("WORLD", T.WORLD),
        tpl_block("NEGATIVE · espinha", T.NEG_SPINE),
    ])

    char_rows = "".join(
        f'<tr><td><input type="checkbox" data-k="codemig-char-{c["tag"]}" aria-label="{c["tag"]} pronto"></td>'
        f'<td><code>@{c["tag"]}</code></td><td>{esc(c["papel"])}</td><td>{esc(c["idade"])}</td>'
        f'<td>{esc(c["r"])}</td><td>{esc(c["takes"])}</td><td class="muted">{esc(c["obs"] or "—")}</td></tr>'
        for c in A.CHARS)
    char_prompts = "".join(tpl_block(f"@{c['tag']} · character sheet", c["prompt"]) for c in A.CHARS)
    char_prompts += tpl_block("@JOVEM · face anchor de pele (T16)", A.FACE_ANCHOR_JOVEM)
    loc_rows = "".join(
        f'<tr><td><input type="checkbox" data-k="codemig-loc-{l["tag"]}" aria-label="{l["tag"]} pronto"></td>'
        f'<td><code>@{l["tag"]}</code></td><td>{esc(l["prio"])}</td><td>{esc(l["takes"])}</td>'
        f'<td class="muted">{esc(l["why"])}</td></tr>' for l in A.LOCS)
    loc_prompts = "".join(tpl_block(f"@{l['tag']} · plate", l["prompt"]) for l in A.LOCS)
    pend = "".join(
        f'<li><div class="pid">{p[0]}</div><div class="pb"><h3>{esc(p[1])}<span class="st {"ok" if p[2] == "decidido" else ""}">{esc(p[2])}</span></h3><p>{esc(p[3])}</p></div></li>'
        for p in PEND)
    risks = "".join(f"<li><b>{esc(r[0])}:</b> {esc(r[1])}</li>" for r in RISKS)

    return PAGE.format(
        total=round(total_cut), n_gens=n_gens, n_chars=len(A.CHARS), legend=legend,
        timeline=json.dumps(timeline, ensure_ascii=False), scenes=scenes,
        style=esc(STYLE_INTENT), templates=templates, char_rows=char_rows, char_prompts=char_prompts,
        loc_rows=loc_rows, loc_prompts=loc_prompts, pend=pend, risks=risks)


PAGE = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>CODEMIG VT Shotlist</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,300..800&display=swap" rel="stylesheet">
<style>
:root{{
  --bg:#EDEFEE; --panel:#FFFFFF; --panel2:#F5F6F5; --line:#D3D8D6;
  --ink:#1D2225; --dim:#5E676C; --ore:#9A3F24; --steel:#4E5D68; --field:#4F6B3A; --warn:#8A5A00;
  --b1:#9A3F24; --b2:#B8834A; --b3:#1D2225; --b4:#4E5D68; --b5:#4F6B3A; --b6:#7A6F9B;
  --code:#F2F3F2;
}}
@media (prefers-color-scheme: dark){{
  :root:not([data-theme="light"]){{
    --bg:#15191B; --panel:#1D2326; --panel2:#232A2E; --line:#333C41;
    --ink:#E4E7E5; --dim:#98A2A6; --ore:#D0714C; --steel:#8FA3B1; --field:#8CB070; --warn:#E0B24F;
    --b1:#D0714C; --b2:#D6A86E; --b3:#E4E7E5; --b4:#8FA3B1; --b5:#8CB070; --b6:#A99BD6; --code:#181D20;
  }}
}}
:root[data-theme="dark"]{{
  --bg:#15191B; --panel:#1D2326; --panel2:#232A2E; --line:#333C41;
  --ink:#E4E7E5; --dim:#98A2A6; --ore:#D0714C; --steel:#8FA3B1; --field:#8CB070; --warn:#E0B24F;
  --b1:#D0714C; --b2:#D6A86E; --b3:#E4E7E5; --b4:#8FA3B1; --b5:#8CB070; --b6:#A99BD6; --code:#181D20;
}}
*,*::before,*::after{{box-sizing:border-box}}
body{{margin:0;background:var(--bg);color:var(--ink);font-family:"Archivo",system-ui,-apple-system,"Segoe UI",sans-serif;line-height:1.5;font-size:15px}}
.wrap{{max-width:1080px;margin:0 auto;padding:40px 16px 96px}}
header h1{{font-size:clamp(34px,6vw,58px);line-height:1;margin:0;font-weight:800;font-variation-settings:"wdth" 70;letter-spacing:-.01em}}
header p{{margin:10px 0 0;color:var(--dim);max-width:72ch}}
.facts{{display:flex;flex-wrap:wrap;gap:8px 28px;margin:22px 0 0;padding:0;list-style:none;color:var(--dim);font-size:14px}}
.facts b{{color:var(--ink);font-weight:700}}
.tl{{margin:34px 0 8px}}
.tl-bar{{position:relative;display:flex;height:64px;border-radius:4px;background:var(--panel2);border:1px solid var(--line)}}
.tl-seg{{position:relative;border-right:1px solid var(--bg);display:flex;align-items:flex-end;justify-content:center;padding-bottom:6px;font-weight:700;font-size:11px;font-variation-settings:"wdth" 62;color:#fff;min-width:0;text-decoration:none}}
.tl-seg:hover,.tl-seg:focus-visible{{filter:brightness(1.15);outline:none}}
.tl-seg span{{overflow:hidden;white-space:nowrap}}
.tl-60{{position:absolute;top:-10px;bottom:-22px;border-left:2px dashed var(--ink)}}
.tl-60 small{{position:absolute;bottom:0;right:6px;white-space:nowrap;font-size:12px;font-weight:700}}
.tl-legend{{display:flex;flex-wrap:wrap;gap:6px 18px;margin-top:30px;font-size:13px;color:var(--dim)}}
.tl-legend i{{display:inline-block;width:10px;height:10px;border-radius:2px;margin-right:6px;vertical-align:-1px}}
.tl-note,.muted{{font-size:13px;color:var(--dim)}}
h2{{font-size:30px;font-weight:800;font-variation-settings:"wdth" 75;margin:64px 0 6px}}
.lede{{color:var(--dim);margin:0 0 22px;max-width:78ch}}
.shared{{background:var(--panel);border:1px solid var(--line);border-left:4px solid var(--ore);padding:16px 20px;margin-bottom:22px;border-radius:4px}}
.shared h3{{margin:0 0 6px;font-size:15px}}
.shared p{{margin:4px 0;max-width:80ch}}
.howto{{background:var(--panel2);border:1px solid var(--line);border-radius:4px;padding:12px 16px;font-size:13px;color:var(--dim);margin-bottom:18px}}
.scene{{background:var(--panel);border:1px solid var(--line);border-radius:6px;padding:18px 20px;margin-bottom:14px;scroll-margin-top:16px}}
.scene.done{{opacity:.55}}
.scene-header{{display:flex;align-items:flex-start;gap:12px}}
.scene-header input{{width:20px;height:20px;margin-top:4px;accent-color:var(--field);flex-shrink:0}}
.scene-num{{font-size:30px;line-height:1;font-weight:800;font-variation-settings:"wdth" 62;color:var(--ore);min-width:58px}}
.scene-desc{{flex:1;min-width:0}}
.scene-desc b{{font-size:18px}}
.blk{{font-size:12px;color:var(--dim);margin-left:6px}}
.gen{{background:var(--panel2);border:1px solid var(--line);border-radius:4px;margin-top:12px;overflow:hidden}}
.gen-label{{display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:8px;padding:8px 14px;border-bottom:1px solid var(--line);font-size:12px;color:var(--dim);font-weight:700;letter-spacing:.03em;text-transform:uppercase}}
.copy-btn{{background:transparent;color:var(--ore);border:1px solid var(--line);border-radius:3px;padding:4px 10px;font-size:11px;cursor:pointer;font-family:inherit;font-weight:700;text-transform:uppercase;letter-spacing:.04em}}
.copy-btn:hover{{border-color:var(--ore)}}
.copy-btn.copied{{color:var(--field);border-color:var(--field)}}
.header-lines{{padding:10px 14px;font-size:13.5px;white-space:pre-wrap;border-bottom:1px solid var(--line)}}
details summary{{cursor:pointer;padding:9px 14px;font-size:13px;font-weight:700;color:var(--steel)}}
pre{{margin:0;padding:14px 16px;font-family:ui-monospace,"SF Mono",Menlo,Consolas,monospace;font-size:12.5px;white-space:pre-wrap;word-break:break-word;background:var(--code)}}
pre.card{{color:var(--dim);border-top:1px solid var(--line)}}
.alt{{padding:10px 14px;border-top:1px solid var(--line);font-size:13px;color:var(--steel)}}
.post{{margin-top:12px;padding:12px 14px;border:1px dashed var(--line);border-radius:4px;color:var(--dim);font-size:14px}}
.tpl .muted{{margin:8px 14px 0}}
.tw{{overflow-x:auto;border:1px solid var(--line);border-radius:4px;background:var(--panel);margin-bottom:14px}}
table{{border-collapse:collapse;width:100%;min-width:760px;font-size:14px}}
th,td{{text-align:left;padding:10px 12px;border-bottom:1px solid var(--line);vertical-align:top}}
th{{font-size:13px;color:var(--dim);font-weight:700;background:var(--panel2)}}
tr:last-child td{{border-bottom:0}}
td code{{font-family:inherit;font-weight:700;font-variation-settings:"wdth" 75;font-size:15px;white-space:nowrap}}
td input{{accent-color:var(--field);width:16px;height:16px}}
.pend{{list-style:none;padding:0;margin:0}}
.pend li{{display:grid;grid-template-columns:56px 1fr;background:var(--panel);border:1px solid var(--line);border-radius:4px;margin-bottom:10px}}
.pend .pid{{font-weight:800;font-size:22px;font-variation-settings:"wdth" 62;padding:14px 0 0 14px;color:var(--ore)}}
.pend .pb{{padding:12px 18px 14px 4px}}
.pend h3{{margin:0;font-size:16px}}
.pend p{{margin:4px 0;font-size:14px;max-width:80ch}}
.st{{display:inline-block;font-size:12px;font-weight:700;margin-left:8px;color:var(--warn)}}
.st.ok{{color:var(--field)}}
.risks{{margin:0;padding-left:20px}}
.risks li{{margin:6px 0;max-width:80ch}}
footer{{margin-top:56px;color:var(--dim);font-size:13px}}
@media (max-width:720px){{
  .scene-header{{flex-wrap:wrap}}
  .scene-num{{font-size:24px;min-width:0}}
  .tl-seg span{{display:none}}
}}
</style>
</head>
<body>
<div class="wrap">
<header>
  <h1>CODEMIG · VT 60"</h1>
  <p>Shotlist CINEORO do filme institucional: os takes principais com o prompt completo de cada geração, a direção travada, os templates congelados (v1, a testar), os character sheets e as pendências. Gerado a partir do pré-shotlist v3.</p>
  <ul class="facts">
    <li><b>16:9</b></li>
    <li><b>Seedance 2.5</b> via Higgsfield</li>
    <li><b>~{total}s</b> estimados no corte</li>
    <li><b>{n_gens}</b> gerações (1 alternativa)</li>
    <li><b>{n_chars}</b> character sheets</li>
  </ul>
</header>

<section class="tl" aria-label="Linha do tempo estimada do corte">
  <div class="tl-bar" id="tl"></div>
  <div class="tl-legend">{legend}</div>
  <p class="tl-note">Duração no corte, a cerca de 3 palavras por segundo, como no pré-shotlist. Cada geração é mais longa que o trecho usado, porque leva alça de ação antes e depois da fala. Clique num trecho para ir ao take.</p>
</section>

<h2>Direção</h2>
<p class="lede">O STYLE INTENT trava o filme antes de qualquer departamento. Cada prompt é escrito dentro dele, e nada nos NEGATIVE contradiz o que ele pede.</p>
<div class="shared">
  <h3>A tese em forma</h3>
  <p><b>Observado onde é vida, autoral onde o filme vira.</b> O revezamento e a conexão são gente trabalhando, filmada por um operador que respira. A abertura, a mina, o match cut e o close final são quadros desenhados com um único gesto de câmera, para o espectador sentir a virada antes de entendê-la.</p>
  <p><b>Uma luz para o estado inteiro:</b> a luz principal vem sempre do lado esquerdo do quadro, com sol baixo de fim de tarde nos exteriores e janela nos interiores. São doze lugares diferentes com a mesma direção de luz.</p>
  <p><b>A terra como constante:</b> o vermelho-ocre do solo e do minério aparece como matéria em quase todo quadro, na terra, no minério, na ferrugem, na camisa do jovem e na roupa da torcedora.</p>
  <p><b>Direção de atuação compartilhada:</b> contar a um conterrâneo, de igual pra igual, uma coisa de que se tem orgulho. A lente é esse conterrâneo. O obstáculo comum é virar discurso. Cada personagem tem motivo e tática próprios, e o trabalho acontece nos olhos.</p>
</div>
<details class="gen tpl"><summary>STYLE INTENT (bloco interno do diretor)</summary><pre>{style}</pre></details>

<h2>Takes</h2>
<p class="lede">A nomenclatura do pré-shotlist foi mantida: o take é a unidade de montagem e a geração é o que vai pro Seedance. T12 e T13 viraram uma geração só. As gerações dos takes de preenchimento (T04.1, T04.2…) entram na próxima etapa.</p>
<div class="howto">Marque o take quando todas as gerações dele estiverem aprovadas (fica salvo neste navegador). O botão copia o prompt inteiro, em inglês, com as falas em português. O card diz a duração e quais referências subir, em que ordem. Faça draft em 480p, confira o que a nota pede e finalize o mesmo draft em 1080p.</div>
{scenes}

<h2>Templates congelados v1</h2>
<p class="lede">Estes blocos são colados literalmente em todos os prompts. Mudou um, muda em todos (rode o build). Eles congelam como v1.1 depois dos drafts de teste (P7).</p>
{templates}

<h2>Character sheets</h2>
<p class="lede">Template padrão do CINEORO: close à esquerda, corpo inteiro de frente e de costas, fundo cinza liso. No Higgsfield, salve cada Element com o nome exato da tag, sem o @. O casting étnico é proposta do diretor (P5).</p>
<div class="tw"><table>
<thead><tr><th>Pronto</th><th>Tag</th><th>Papel</th><th>Idade</th><th>R</th><th>Takes</th><th>Observações</th></tr></thead>
<tbody>{char_rows}</tbody></table></div>
{char_prompts}

<h2>Locações e props</h2>
<p class="lede">Só o que precisa de asset. Mãe, bebê, torcedora, cliente, paciente e figurantes o modelo improvisa a partir do texto. O Mineirão saiu da lista porque no T11 o estádio fica desfocado.</p>
<div class="tw"><table>
<thead><tr><th>Pronto</th><th>Tag</th><th>Prioridade</th><th>Takes</th><th>Por quê</th></tr></thead>
<tbody>{loc_rows}</tbody></table></div>
{loc_prompts}

<h2>Etapas a discutir</h2>
<ul class="pend">{pend}</ul>

<h2>Riscos sinalizados</h2>
<ul class="risks">{risks}</ul>

<footer>Shotlist CINEORO v1 · CODEMIG VT 60". Gerado por build.py a partir de templates.py, generations.py e assets.py. Os checkboxes ficam salvos neste navegador.</footer>
</div>
<script>
const TL = {timeline};
const store = {{
  get(k){{ try {{ return localStorage.getItem(k); }} catch(e){{ return null; }} }},
  set(k,v){{ try {{ localStorage.setItem(k,v); }} catch(e){{}} }}
}};
const total = TL.reduce((s,t) => s + t.d, 0);
const tl = document.getElementById("tl");
TL.forEach(t => {{
  const a = document.createElement("a");
  a.className = "tl-seg"; a.href = "#" + t.id;
  a.style.flex = t.d + " 1 0"; a.style.background = "var(" + t.c + ")";
  if (t.b === "vr") a.style.color = "var(--bg)";
  a.title = t.id + " · " + t.t + " · ~" + t.d + "s";
  a.innerHTML = "<span>" + t.id + "</span>";
  tl.appendChild(a);
}});
const m = document.createElement("div");
m.className = "tl-60"; m.style.left = Math.min(60 / total * 100, 100) + "%";
m.innerHTML = "<small>60s</small>";
tl.appendChild(m);
document.querySelectorAll(".scene input[data-scene]").forEach(cb => {{
  const key = "codemig-take-" + cb.dataset.scene;
  if (store.get(key) === "1") {{ cb.checked = true; cb.closest(".scene").classList.add("done"); }}
  cb.addEventListener("change", () => {{
    store.set(key, cb.checked ? "1" : "0");
    cb.closest(".scene").classList.toggle("done", cb.checked);
  }});
}});
document.querySelectorAll("[data-k]").forEach(cb => {{
  if (store.get(cb.dataset.k) === "1") cb.checked = true;
  cb.addEventListener("change", () => store.set(cb.dataset.k, cb.checked ? "1" : "0"));
}});
document.querySelectorAll(".copy-btn").forEach(btn => {{
  btn.addEventListener("click", () => {{
    const target = btn.closest(".gen").querySelector(btn.dataset.target);
    const done = () => {{
      btn.classList.add("copied"); const t = btn.textContent; btn.textContent = "Copiado";
      setTimeout(() => {{ btn.classList.remove("copied"); btn.textContent = t; }}, 1500);
    }};
    try {{ navigator.clipboard.writeText(target.textContent).then(done); }} catch (e) {{}}
  }});
}});
</script>
</body>
</html>
"""


def build_md():
    out = ["# CODEMIG · VT 60\" — Shotlist CINEORO v1", "",
           "Seedance 2.5 via Higgsfield · 16:9 · ~60s no corte. Prompts em inglês com as falas em português; header, card e notas em português.", "",
           "## Direção (STYLE INTENT)", "", "```", STYLE_INTENT, "```", "", "## Takes", ""]
    for s in SCENES:
        out += [f"### {s['id']} · {s['t']} ({BLOCOS[s['b']][0]}, ~{s['d']}s no corte)", "", s["desc"], ""]
        if s.get("post"):
            out += [s["post"], ""]
        for g in s["gens"]:
            out += [f"#### Geração {g['id']} · {g['label']}", "", "```", g["header"], "```", "",
                    "```", g["prompt"], "```", "", "```", g["card"], "```", ""]
            if g.get("alt"):
                out += [g["alt"], ""]
    out += ["## Templates congelados v1", "", "```", T.FILM_LOOK, "", T.LIGHT_EXT, "", T.MATCH_FRAME, "",
            T.rev_camera("[distance]", "[size]"), "", T.WORLD, "", "NEGATIVE spine: " + T.NEG_SPINE, "```", "",
            "### Voice locks", "", "```", "\n\n".join(T.voice_lock(k) for k in T.VOICE), "```", "",
            "## Character sheets", "", "| Tag | Papel | Idade | R | Takes | Observações |", "| --- | --- | --- | --- | --- | --- |"]
    out += [f"| @{c['tag']} | {c['papel']} | {c['idade']} | {c['r']} | {c['takes']} | {c['obs'] or '—'} |" for c in A.CHARS]
    out.append("")
    for c in A.CHARS:
        out += [f"### @{c['tag']}", "", "```", c["prompt"], "```", ""]
    out += ["### @JOVEM · face anchor de pele (T16)", "", "```", A.FACE_ANCHOR_JOVEM, "```", "",
            "## Locações e props", "", "| Tag | Prioridade | Takes | Por quê |", "| --- | --- | --- | --- |"]
    out += [f"| @{l['tag']} | {l['prio']} | {l['takes']} | {l['why']} |" for l in A.LOCS]
    out.append("")
    for l in A.LOCS:
        out += [f"### @{l['tag']}", "", "```", l["prompt"], "```", ""]
    out += ["## Etapas a discutir", ""]
    out += [f"- **{p[0]} · {p[1]}** ({p[2]}): {p[3]}" for p in PEND]
    out += ["", "## Riscos sinalizados", ""]
    out += [f"- **{r[0]}:** {r[1]}" for r in RISKS]
    return "\n".join(out) + "\n"


if __name__ == "__main__":
    with open(os.path.join(HERE, "codemig-vt60-shotlist.html"), "w", encoding="utf-8") as f:
        f.write(build_html())
    with open(os.path.join(HERE, "codemig-vt60-shotlist.md"), "w", encoding="utf-8") as f:
        f.write(build_md())
    for s in SCENES:
        for g in s["gens"]:
            print(f"{g['id']:<22} {words(g['prompt']):>5} palavras")
    print("total no corte:", round(sum(s['d'] for s in SCENES), 1), "s")
