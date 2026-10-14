#!/usr/bin/env python3
"""Gera o shotlist CINEORO do VT CODEMIG 60" (v2).

Uso: python3 build.py
Saídas: codemig-vt60-shotlist.html (página do artifact) e codemig-vt60-shotlist.md
"""
import html
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import assets as A  # noqa: E402
import generations as G  # noqa: E402
import templates as T  # noqa: E402

VERSION = "v2"

BLOCOS = {
    "ab": "Abertura", "rv": "Revezamento", "vr": "Virada",
    "mc": "Match cut", "cx": "Conexão", "fc": "Fechamento",
}


def gen(gid, prompt, acontece, dito, tempo, termina, direcao, shots_pt, task, attach, notes, alt=None):
    return dict(id=gid, prompt=prompt, acontece=acontece, dito=dito, tempo=tempo, termina=termina,
                direcao=direcao, shots_pt=shots_pt, task=task, attach=attach, notes=notes, alt=alt)


SCENES = [
    dict(id="T01", b="ab", t="Pico e descida até a sala", d=5.7,
         desc="De costas pro mar de morros, o jovem vira; corte seco pro close, ele fala e a câmera desce num movimento só, pela terra, minério e aço, até a sala de aula.",
         gens=[gen("T01-A", G.T01A,
                   "No alto do pico, o jovem de costas, de mochila, centralizado e de corpo inteiro num plano bem aberto, olhando os morros. Ele vira por completo até ficar de frente pra câmera, sorrindo, e segura o olhar.",
                   "nada.",
                   "de costas, olhando os morros — 2s · vira por completo — 2s · segura de frente — 2s = 6s",
                   "ele de frente, quadrado pra câmera, olhando a lente. O corte cai nesse olhar.",
                   "Plano aberto e simétrico, o único do filme: a figura inteira ao centro e os morros caindo dos dois lados, que no 21:9 ganham espaço. O giro é completo, para o T01-B começar de onde este termina (ele de frente, olhando a lente) e o corte pro close fazer sentido.",
                   ["Aberto, centralizado: de costas, vira por completo, segura de frente"],
                   "reference-to-video", ["@JOVEM (character sheet) — identidade"],
                   "o draft anterior saiu em médio sobre o ombro e terminou com ele meio virado. Confira três coisas: corpo inteiro no quadro, ele no centro, e o giro terminando de frente (ombros quadrados). Sem locação anexada: o pico sai só do texto."),
               gen("T01-B", G.T01B,
                   "Close do jovem, que fala e sorri. A câmera desce reto, nivelada, pelo corpo dele, entra no chão, atravessa terra, minério, as vigas de aço e o forro com o ventilador, e pousa no aluno sentado, com a professora em pé atrás à esquerda. Os dois falam.",
                   "JOVEM: \"Em Minas, terra não é só terra.\" / ALUNO: \"É futuro.\" / PROFESSORA: \"Minério não é só minério.\"",
                   "close, fala — 5s · desce pelo corpo — 2s · terra e minério — 2s · vigas, forro, ventilador — 2s · pousa no aluno — 2s · as duas falas e o olhar — 5s = 18s",
                   "aluno e professora segurando o seu olhar; corte seco.",
                   "Segue o seu bloqueio 3D (@Video1) como referência só de movimento: câmera nivelada que afunda, sem inclinar. As falas ficam nos trechos parados, nunca durante a descida. A tela preta saiu: a cadeia terra, minério, aço e escola agora é um movimento só.",
                   ["Close, fala, e descida contínua até a sala"],
                   "reference-to-video", ["@JOVEM (character sheet) — identidade", "@ALUNO (character sheet) — identidade", "@PROFESSORA (character sheet) — identidade", "@Video1 — bloqueio 3D, referência só de movimento (estendido para 18s)"],
                   "estenda o último frame do menino no bloqueio em ~3s (vídeo de 15s para 18s) para caber as duas falas. O bloqueio está em 16:9 e o filme é 21:9: se for fácil, reexporte em 21:9 (a descida vertical funciona igual, só ganha espaço dos lados); se não, o modelo extrapola as laterais. Se puder, exporte o bloqueio sem os textos (CHAO, TERRA, MINERIO…), porque letras em referência tendem a vazar para o vídeo. Risco nº 1: fala na boca errada; fallback de voz no ElevenLabs.")]),
    dict(id="T02", b="ab", t="Sala de aula", d=3.5,
         desc="Aluno e professora: as falas acontecem no final da geração T01-B.",
         gens=[], post="Sem geração própria: a chegada na sala e as falas do aluno e da professora fazem parte da geração T01-B, que segue o bloqueio 3D do pico até a sala."),
    dict(id="T04", b="rv", t="Eletroposto", d=2.8,
         desc="Plugue entrando no carro elétrico, a luz acendendo, o homem fala de lado e dá um tapinha no teto.",
         gens=[gen("T04", G.T04,
                   "Num estacionamento moderno com ipês floridos: detalhe do plugue entrando no carro elétrico, close da luz da porta acendendo, o homem fala de lado pra lente e dá um tapinha satisfeito no teto.",
                   "HOMEM: \"É a possibilidade de um mundo mais verde,\"",
                   "plugue — 3s · luz acende — 2s · fala — 5s · tapinha — 2s = 12s",
                   "ele saindo de quadro pela direita, câmera ainda andando.",
                   "P1 em todos os planos, inclusive nos closes: a câmera anda de lado da esquerda pra direita e nunca para. As subações em close cobrem a locução em off na montagem.",
                   ["Detalhe: plugue entrando no carro", "Close: luz acende, mão solta", "Médio-aberto: fala", "Close: tapinha no teto"],
                   "reference-to-video", ["@HOMEM_EV (character sheet) — identidade", "opcional: @CARRO_EV — objeto"],
                   "conferir se a câmera anda em todos os planos. A resistência do plugue é só para não parecer mágica; se entrar de primeira, tudo bem.")]),
    dict(id="T05", b="rv", t="Indústria", d=1.8,
         desc="Laminação moderna: placa incandescente nos rolos, a mão no joystick, o operário fala, a bobina pronta rola.",
         gens=[gen("T05", G.T05,
                   "Numa laminação moderna e automatizada: a placa de aço incandescente passa nos rolos, a mão do operário empurra o joystick, ele fala orgulhoso e a bobina pronta rola para o lugar.",
                   "OPERÁRIO: \"de uma indústria mais eficiente,\"",
                   "placa nos rolos — 3s · joystick — 2s · fala — 5s · bobina — 2s = 12s",
                   "a bobina rolando, câmera ainda andando.",
                   "Mesmo travelling lateral do revezamento em todos os planos. Fábrica limpa e automatizada, nada de chão de fábrica velho.",
                   ["Close: placa incandescente nos rolos", "Close: mão no joystick", "Médio-aberto: fala", "Close: bobina pronta rolando"],
                   "reference-to-video", ["@OPERARIO (character sheet) — identidade + EPI"],
                   "conferir EPI completo e sem logo, e telas do console sem texto legível.")]),
    dict(id="T06", b="rv", t="Laboratório", d=1.2,
         desc="Uma gota azul se mistura no vórtice do béquer, o rack entra no analisador, a pesquisadora fala e confere um frasco.",
         gens=[gen("T06", G.T06,
                   "Num laboratório farmacêutico moderno: detalhe do vórtice no béquer com uma gota azul se misturando, o rack de tubos entrando no analisador, a pesquisadora levanta os olhos e fala, depois confere um frasco contra a janela.",
                   "PESQUISADORA: \"de novas tecnologias,\"",
                   "vórtice — 3s · analisador — 2s · fala — 4s · frasco — 2s = 11s",
                   "ela conferindo o frasco, câmera ainda andando.",
                   "O close de algo sendo misturado que você pediu abre o take. É o trecho mais curto do filme no corte, então as subações seguram a locução.",
                   ["Detalhe: vórtice, gota azul se mistura", "Close: rack entra no analisador", "Médio-aberto: fala", "Close: frasco contra a janela"],
                   "reference-to-video", ["@PESQUISADORA (character sheet) — identidade + EPI"],
                   "se sair rótulo legível em frasco ou tela, regerar: texto não pode aparecer.")]),
    dict(id="T07", b="rv", t="Restaurante", d=1.8,
         desc="As mãos montam o prato, o prato chega à mesa, o dono fala cúmplice e a cliente aprova.",
         gens=[gen("T07", G.T07,
                   "Num restaurante saudável contemporâneo em BH: as mãos do dono finalizam o prato, o prato chega à mesa, ele vira pra lente com um sorriso cúmplice e fala, e a cliente aprova na primeira garfada.",
                   "DONO: \"de uma economia mais sustentável.\"",
                   "montando o prato — 3s · prato na mesa — 2s · fala — 5s · garfada — 2s = 12s",
                   "a cliente acenando que aprovou, câmera ainda andando.",
                   "Restaurante claro, madeira clara e plantas, cozinha aberta. Nada de toalha xadrez ou cara de interior antigo.",
                   ["Close: mãos montando o prato", "Close: prato na mesa, garfo", "Médio-aberto: fala", "Close: primeira garfada"],
                   "reference-to-video", ["@DONO (character sheet) — identidade"],
                   "conferir se a boca da cliente fica fechada e se ela não olha pra lente.")]),
    dict(id="T08", b="rv", t="Plantação", d=8.3,
         desc="A mão passa pelas plantas, abre uma vagem; a agricultora caminha e fala, sorrindo.",
         gens=[gen("T08", G.T08,
                   "Numa fazenda de soja moderna no Triângulo, com pivô central ao fundo: close da mão passando nas plantas, detalhe da vagem aberta, a agricultora caminha falando com a lente e termina num close sorrindo.",
                   "AGRICULTORA: \"Enquanto o mundo olha para o nióbio e as terras raras de Minas, Minas olha para o que há de mais raro na nossa terra:\"",
                   "mão nas plantas — 3s · vagem — 2s · caminha e fala — 10s · close sorrindo — 2s = 17s",
                   "close dela caminhando, olhando pra você; corte pra mina.",
                   "Ela não para mais de andar, porque no revezamento a câmera não fica parada. Fazenda moderna, sem chapéu de palha.",
                   ["Close: mão passando nas plantas", "Detalhe: abre uma vagem", "Médio-aberto: caminha e fala", "Close: rosto sorrindo"],
                   "reference-to-video", ["@AGRICULTORA (character sheet) — identidade"],
                   "fala longa: se o lipsync escorregar no fim, a montagem cobre o final com o close dela ou com a mão nas plantas.")]),
    dict(id="T09", b="vr", t="Mina de nióbio", d=4.8,
         desc="O minério gira na luva; o foco sai do minério e chega nele, que fala; no close, o olhar desce e sobe para a lente.",
         gens=[gen("T09", G.T09,
                   "Na beira de uma cava moderna em Araxá: detalhe do minério girando na luva; no médio-aberto o foco sai do minério e chega no funcionário, que fala; no close, o olhar desce para o minério e sobe para a lente.",
                   "FUNCIONÁRIO: \"a nossa gente. Afinal, o que cresce aqui também deve construir novos caminhos para quem nasce, vive e trabalha aqui.\"",
                   "minério na luva — 3s · rack e fala — 9s · close, olhar sobe — 3s = 15s",
                   "o olhar pousado na lente, sorrindo; match cut com o T10.",
                   "O rack de foco segue sendo o gesto da virada: onde se espera o minério, aparece a pessoa. O close final abre o match cut do olhar. A frase inteira está na fala, então o áudio de \"para quem nasce, vive e trabalha aqui\" vai para baixo do T10 ao T12.",
                   ["Detalhe: minério girando na luva", "Médio-aberto: rack para ele, fala", "Close (match): olhar sobe"],
                   "reference-to-video", ["@FUNCIONARIO (character sheet) — identidade + EPI"],
                   "validar o EPI com a SST da operadora antes do final (P11).")]),
    dict(id="T10", b="mc", t="Mãe e recém-nascido", d=1.2,
         desc="A mãe olha o bebê e levanta os olhos para você, no mesmo ponto da tela do funcionário.",
         gens=[gen("T10", G.T10,
                   "Num apartamento claro em BH, a mãe confere a respiração do recém-nascido e levanta os olhos para a lente, sorrindo; os olhos pousam onde pousaram os do funcionário.",
                   "nada na geração. Na montagem: V.O. do T09, \"para quem nasce,\"",
                   "olhos no bebê — 2s · olhar sobe — 1s · sorriso — 2s = 5s",
                   "segurando seu olhar; corte para o T11.",
                   "P2, o match cut pelo olhar: o mesmo close do T09 ao T12. Geração sem fala, para nenhuma boca formar palavras.",
                   ["Close (match): olhar sobe do bebê"],
                   "text-to-video", ["nenhuma referência (o modelo improvisa mãe e bebê)"],
                   "conferir a proporção do bebê (rosto parcialmente coberto) e se os olhos pousam no ponto marcado.")]),
    dict(id="T11", b="mc", t="Mineirão", d=0.8,
         desc="A torcedora segue a bola que sobe e os olhos dela chegam em você.",
         gens=[gen("T11", G.T11,
                   "No Mineirão reformado, a torcedora prende a respiração no lance; a bola sobe, os olhos dela sobem junto e pousam na lente, acesos.",
                   "nada na geração. Na montagem: V.O. do T09, \"vive,\"",
                   "olhos no lance — 2s · olhar sobe com a bola — 1s · segura — 2s = 5s",
                   "segurando seu olhar; corte para o T12.",
                   "O olhar tem motivo físico (a bola subindo). Estádio desfocado e figurino terracota, fora das cores de clube e do verde-amarelo.",
                   ["Close (match): olhar sobe com a bola"],
                   "text-to-video", ["nenhuma referência"],
                   "conferir a arquibancada desfocada: nada de camisa, bandeira ou cachecol de clube.")]),
    dict(id="T12", b="mc", t="Ônibus", d=6.6,
         desc="O estudante embarca; o olhar do motorista sobe para você e ele explica a rota com o ônibus andando.",
         gens=[gen("T12 + T13", G.T12,
                   "Num ônibus moderno de BH: a porta de vidro abre e o tênis do estudante entra; no close, o olhar do motorista acompanha o menino e sobe para a lente; com o ônibus andando, ele fala; fecha no estudante na janela, BH passando.",
                   "MOTORISTA: \"Se Minas tem o que o futuro procura, esse futuro também precisa chegar até os mineiros.\" (na montagem, a V.O. \"e trabalha aqui.\" do T09 cai no plano 1)",
                   "porta e tênis — 3s · olhar sobe — 3s · fala com o ônibus andando — 7s · estudante na janela — 3s = 16s",
                   "o estudante na janela; corte seco.",
                   "O olhar do motorista fecha o match cut e emenda a fala dele. O close final do estudante prepara o T14.",
                   ["Close: porta abre, tênis entra", "Close (match): olhar sobe", "Médio-aberto: ônibus andando, fala", "Close: estudante na janela"],
                   "reference-to-video", ["@MOTORISTA (character sheet) — identidade", "@ESTUDANTE (character sheet) — identidade"],
                   "risco: o estudante abrir a boca. O ônibus tem que estar andando quando o motorista fala.")]),
    dict(id="T14", b="cx", t="Trilhas de Futuro", d=3.8,
         desc="O estudante aperta o borne, a lâmpada acende, ele fala e comemora com a colega.",
         gens=[gen("T14", G.T14,
                   "Na oficina do curso técnico: detalhe do borne apertado, a lâmpada do painel acende, o estudante vira pra lente e fala orgulhoso, e bate um soquinho com a colega.",
                   "ESTUDANTE: \"É para isso que a Codemig existe… para fazer essa conexão acontecer.\"",
                   "borne — 3s · lâmpada acende — 2s · fala — 5s · soquinho — 2s = 12s",
                   "o soquinho na frente da lâmpada acesa; corte seco.",
                   "A ação dele é fazer uma conexão com as mãos antes de dizer \"conexão\". Mesmo figurino do ônibus.",
                   ["Detalhe: borne apertado", "Close: lâmpada acende", "Médio-aberto: fala", "Close: soquinho"],
                   "reference-to-video", ["@ESTUDANTE (character sheet) — identidade, mesmo figurino do T12"],
                   "conferir a pronúncia de \"Codemig\". Se sair errada, regerar antes de mexer na grafia.")]),
    dict(id="T15", b="cx", t="Hospital", d=6.8,
         desc="Oxímetro no dedo, gota no soro; a enfermeira cuida e fala; o paciente aperta a mão dela.",
         gens=[gen("T15", G.T15,
                   "Numa enfermaria moderna da rede pública: close do oxímetro no dedo, a gota caindo no soro, a enfermeira cuida do paciente enquanto fala e olha pra lente no fim, e ele aperta a mão dela.",
                   "ENFERMEIRA: \"Para fazer com que os recursos essenciais para a transição energética que o mundo precisa, também criem oportunidades para Minas.\"",
                   "oxímetro — 3s · soro — 2s · cuida e fala — 7s · aperto de mão — 2s = 14s",
                   "as mãos apertadas; corte seco.",
                   "Ela não para de cuidar para falar. As subações em close dão à montagem onde apoiar a fala longa em off, se precisar.",
                   ["Close: oxímetro no dedo", "Close: gota no soro", "Médio-aberto: cuida e fala", "Close: aperto de mão"],
                   "reference-to-video", ["@ENFERMEIRA (character sheet) — identidade"],
                   "fala longa: se o lipsync escorregar, use a fala em off sobre os closes.")]),
    dict(id="T16", b="fc", t="Close final", d=8.2,
         desc="O jovem do começo, num close bem fechado, fala as últimas frases sorrindo.",
         gens=[gen("T16", G.T16,
                   "No mesmo pico e na mesma luz do T01, o jovem em close bem fechado, na mão, fala direto com você, orgulhoso e sorrindo.",
                   "JOVEM: \"Para transformar a força que vem da nossa terra em mais desenvolvimento para a nossa terra. O minério é nosso. O futuro também.\"",
                   "olhar na lente — 1s · fala — 9s · sorriso — 2s = 12s",
                   "segurando seu olhar, sorrindo; corte para a assinatura.",
                   "Mantive o close bem fechado do pré-shotlist, agora na mão. É a exceção à regra da fala em plano mais aberto (P14).",
                   ["Close bem fechado: fala e sorriso"],
                   "reference-to-video", ["@JOVEM (character sheet) — identidade"],
                   "olhos e pele são o take inteiro. Conferir pupila viva e a cicatriz na sobrancelha.",
                   alt="Direção alternativa: um pull-back na mão, do close até o aberto, durante \"O futuro também.\", revelando o mar de morros.")]),
    dict(id="T17", b="fc", t="Assinatura", d=2.5,
         desc="Assinatura em pós (After Effects): Codemig. O futuro é mineiro. / Codemge. Abrindo caminhos para Minas crescer.",
         gens=[], post="Sem geração. Locução \"Codemig. O futuro é mineiro.\" gravada (locutor ou ElevenLabs); lettering e logos no After Effects."),
]

STYLE_INTENT = """STYLE INTENT — CODEMIG VT 60" (v2)
MEDIUM: live-action photoreal
REGISTER: warm, proud institutional film — direct address, happy people, a modern Brazil
CAMERA LANGUAGE: handheld in every shot of the film; sub-actions in close-ups and
          details, the line in the most open shot of the take, hard cuts between them;
          relay (P1) = the camera travels frame-left → frame-right in every shot
LIGHT LOGIC: one dominant motivated natural source per scene with real falloff, always
          on the frame-LEFT side of the faces (low late sun outside, window inside)
SOUND/MUSIC POLICY: NO music in generation (the score is added in post); location sound
COLOUR & TEXTURE: 35mm color negative (client style ref) — organic grain, warm halation,
          lifted blacks with a faint teal-green, vintage spherical glass, gentle vignette;
          colour comes from each location, never a grade on top
WORLD: modern Minas Gerais and Brazil — nothing rustic, rural-poor, old or colonial
MOTION: real-time 24 fps with natural motion blur
REALIST PRESET RULES SWITCHED OFF: "never look into the lens" (direct address);
          "no vignette" and "no teal" (client look); "grime / over-real wear" (modern
          world: material truth without decay); "locked composed frames" (handheld always)"""

DIRECTION = [
    ("Tom", "Feliz e orgulhoso. Cada personagem conta uma boa notícia sobre o estado a um amigo, que é a lente. As táticas de atuação são de mostrar, celebrar e convidar, e o NOT de todo prompt proíbe cara séria e discurso."),
    ("Falas", "Só o texto da fala, com o segundo em que entra. Nenhuma indicação de pausa ou entrega. O sotaque ficou num voice lock curto (R caipira ou R de BH, de P3) e o tom vem da atuação."),
    ("Gramática", "Câmera na mão o tempo todo. Subações antes e depois da fala em close ou detalhe, e a fala no plano mais aberto do take (médio-aberto, do joelho pra cima, com o lugar em volta), com corte seco entre eles. Exceções: o T01, com a fala no close como você pediu, e o T16, o close final."),
    ("Revezamento", "Em todos os planos, inclusive nos closes, a câmera anda de lado da esquerda pra direita e nunca para. Cada take tem 3 ou 4 subações para a montagem apoiar a locução em off."),
    ("Mundo", "Minas e Brasil modernos: arquitetura contemporânea, equipamento novo, espaços públicos bem cuidados e \"Brazilian\" espalhado pelos prompts. Nada rústico, pobre, velho ou colonial; isso está no template WORLD e na espinha do NEGATIVE."),
    ("Look", "O seu style ref de 35mm color negative, sem o parágrafo de cor e sem \"tactile surfaces\": a cor sai do ambiente de cada cena. A regra de luz é uma fonte natural dominante por cena, sempre do lado esquerdo do quadro."),
]

PEND = [
    ("P1", "Transição do revezamento (T04–T08)", "decidido",
     "Travelling lateral da esquerda pra direita em todos os planos, closes incluídos; a câmera nunca para. Corte seco entre subações e fala."),
    ("P2", "Match cut (T09–T12)", "decidido",
     "O levantar do olhar, no mesmo close na mão (olhos pousando no terço superior a ~45% da largura): funcionário, mãe, torcedora, motorista."),
    ("P3", "Sotaque", "decidido",
     "R caipira para interior, campo e mineração; R de BH para a cidade. Agora num voice lock curto, sem direção de entrega."),
    ("P4", "Falas finais do T16", "decidido", "Sem coro; o protagonista fala tudo."),
    ("P5", "Casting e representação", "proposta",
     "Proposta do diretor nos character sheets: pardos, pretos e brancos em proporção próxima à de Minas, sem amarrar ofício a cor. Validar antes de gerar os sheets."),
    ("P6", "Teto de 60 segundos", "decidido",
     "O corte segue estimado em ~60s. As gerações ficaram mais longas (11–17s) para caber as subações; a locução se ajusta em off na montagem."),
    ("P7", "Look (style ref)", "a testar",
     "FILM LOOK v2 a partir do seu ref. Antes de congelar, fazer draft do T01 (exterior com mergulho), do T05 (interior com travelling) e do T09 (virada com match)."),
    ("P9", "V.O. do T10 ao T12", "proposta",
     "O funcionário diz a frase inteira no T09; esse áudio vira a V.O. dos três takes seguintes, que são gerados sem fala."),
    ("P10", "T12 e T13 numa geração", "proposta", "Mesmo lugar e mesmas pessoas; o olhar do motorista emenda a fala."),
    ("P15", "Bloqueio 3D da descida (T01-B)", "confirmar",
     "O bloqueio vira referência só de movimento do T01-B. Pedido: estender o último frame do menino em ~3s (15s para 18s) para caberem as duas falas, e, se der, exportar sem os textos de marcação, que tendem a vazar para o vídeo. Os 5s iniciais para a fala do jovem estão bons."),
    ("P16", "Locações", "decidido",
     "Nenhuma plate será gerada por enquanto; todos os takes saem de text-to-video para o lugar. Os prompts de locação ficam de reserva."),
    ("P11", "EPI da mina e da siderurgia", "validar",
     "Os sheets trazem EPI padrão. Confirmar com a SST da operadora antes da geração final."),
    ("P13", "Formato", "decidido",
     "21:9 em todas as gerações (variável única no build). As character sheets ficam em 16:9, porque são referência de identidade. Nos closes o 21:9 deixa muito espaço dos lados; se algum close vier aberto demais, aperte o FOV (por exemplo 29° para 18°)."),
    ("P17", "Corte T01-A → T01-B", "decidido",
     "T01-A termina com ele totalmente de frente, ombros quadrados e olhando a lente; T01-B começa exatamente assim, em close. O corte cai no olhar, como um punch-in. A mesma luz (sol da esquerda) nos dois."),
    ("P14", "T16 em close", "confirmar",
     "Mantido o close bem fechado do pré-shotlist, exceção à regra da fala em plano mais aberto. Dá para abrir no fim com um pull-back (ver alternativa no take)."),
]

RISKS = [
    ("Muitos planos por geração", "3 a 4 cortes em 11–17s pedem timing preciso. Faça draft em 480p e confira se os cortes caem nos segundos certos antes do final."),
    ("Mergulho na terra (T01)", "o modelo pode cortar dentro do plano 2 ou não chegar ao preto. A montagem resolve o preto se preciso."),
    ("Mineirão (T11)", "nada de preto e branco, azul e branco, verde e branco ou verde-amarelo; a torcedora veste terracota."),
    ("Marcas reais", "carro, ônibus, mina, escola, programa e hospital saem sem marca e sem texto legível. Logos entram na pós."),
    ("Mineração (T09)", "EPI completo é trava crítica; falta validar com a SST (P11)."),
    ("Duas falas numa geração (T02)", "o prompt trava quem fala em qual segundo; fallback de voz no ElevenLabs."),
    ("Recém-nascido (T10)", "rosto do bebê parcialmente coberto e proporção travada."),
    ("Look com vinheta e franja cromática", "se aparecerem artefatos, tire a franja cromática do FILM LOOK primeiro, como manda o CINEORO."),
    ("Brasil genérico", "se algum lugar sair com cara de Europa ou EUA, reforce detalhes brasileiros na cena (ipês, rua, gente) antes de mexer no resto."),
]

# ------------------------------------------------------------------ parsing helpers
SHOT_RE = re.compile(r"^(SHOT|BEAT) (\d+) \((\d+)–(\d+)s\) — (.*)$", re.M)
LINE_RE = re.compile(r"^\[(\d+)–(\d+)s\] @(\w+)", re.M)
SIZE_RE = re.compile(r"\b(ECU|CU|MCU|MWS|MS|WS|EWS)\b")


def shots_of(g):
    found = SHOT_RE.findall(g["prompt"])
    if found and found[0][0] == "BEAT":
        a, b = int(found[0][2]), int(found[-1][3])
        sizes = SIZE_RE.findall(found[0][4])
        found = [("SHOT", "1", str(a), str(b), sizes[0] if sizes else "")]
    out = []
    for i, f in enumerate(found):
        size = SIZE_RE.search(f[4])
        out.append(dict(n=i + 1, a=int(f[2]), b=int(f[3]), size=size.group(1) if size else "—",
                        label=g["shots_pt"][i]))
    assert len(out) == len(g["shots_pt"]), (g["id"], len(out), len(g["shots_pt"]))
    return out


def speech_of(g):
    return [dict(a=int(a), b=int(b), who=w) for a, b, w in LINE_RE.findall(g["prompt"])]


def words(s):
    return len(s.split())


def build_data():
    scenes = []
    for s in SCENES:
        gens = []
        for g in s["gens"]:
            shots = shots_of(g)
            dur = shots[-1]["b"]
            gens.append(dict(
                id=g["id"], dur=dur, nshots=len(shots), shots=shots, speech=speech_of(g),
                acontece=g["acontece"], dito=g["dito"], tempo=g["tempo"], termina=g["termina"],
                direcao=g["direcao"], attach=g["attach"], notes=g["notes"], alt=g["alt"],
                task=g["task"], prompt=g["prompt"], words=words(g["prompt"]),
                card=G.card(g["task"], dur, g["attach"], g["notes"])))
        scenes.append(dict(id=s["id"], b=s["b"], bloco=BLOCOS[s["b"]], t=s["t"], d=s["d"],
                           desc=s["desc"], gens=gens, post=s.get("post")))
    templates = [
        ("CONTRACT (padrão)", "CONTRACT — Live-action photoreal film footage, " + T.ASPECT + ", [N] seconds total, [shots and cuts], [camera language], real-time motion, " + T.LANG + ". NO music, NO score. " + T.TEXT_POLICY + "."),
        ("FILM LOOK + flares", T.FILM_LOOK),
        ("LIGHT · exteriores", T.LIGHT_EXT),
        ("LIGHT · interiores (base)", T.light_int("[window]", "[practicals]", "[reach]")),
        ("CAMERA · na mão", T.handheld()),
        ("CAMERA · revezamento", T.REV_CAMERA),
        ("MATCH FRAME", T.MATCH_FRAME),
        ("Atuação compartilhada", T.SHARED_ACTING),
        ("VOICE LOCKS", "\n".join(T.voice_lock(k) for k in T.VOICE)),
        ("Política de música", T.MUSIC_POLICY),
        ("WORLD", T.WORLD),
        ("NEGATIVE · espinha", T.NEG_SPINE),
    ]
    return dict(
        version=VERSION, aspect=T.ASPECT, scenes=scenes, blocos=BLOCOS,
        direction=DIRECTION, style=STYLE_INTENT, templates=templates,
        chars=[dict(tag=c["tag"], papel=c["papel"], idade=c["idade"], r=c["r"], takes=c["takes"],
                    obs=c["obs"], prompt=c["prompt"]) for c in A.CHARS],
        face=A.FACE_ANCHOR_JOVEM, locs=A.LOCS, pend=PEND, risks=RISKS)


def build_md(data):
    out = [f"# CODEMIG · VT 60\" — Shotlist CINEORO {VERSION}", "",
           f"Seedance 2.5 via Higgsfield · {T.ASPECT} · ~60s no corte.", "", "## Direção", ""]
    out += [f"- **{k}:** {v}" for k, v in DIRECTION]
    out += ["", "```", STYLE_INTENT, "```", "", "## Takes", ""]
    for s in data["scenes"]:
        out += [f"### {s['id']} · {s['t']} ({s['bloco']}, ~{s['d']}s no corte)", "", s["desc"], ""]
        if s["post"]:
            out += [s["post"], ""]
        for g in s["gens"]:
            out += [f"#### Geração {g['id']} · {g['dur']}s · {g['nshots']} plano(s)", "",
                    f"- **O que acontece:** {g['acontece']}", f"- **O que é dito:** {g['dito']}",
                    f"- **Tempo:** {g['tempo']}", f"- **Como termina:** {g['termina']}",
                    f"- **Direção:** {g['direcao']}", "", "```", g["prompt"], "```", "", "```", g["card"], "```", ""]
            if g["alt"]:
                out += [g["alt"], ""]
    out += ["## Templates congelados", ""]
    for name, text in data["templates"]:
        out += [f"### {name}", "", "```", text, "```", ""]
    out += ["## Character sheets", "", "| Tag | Papel | Idade | R | Takes | Observações |", "| --- | --- | --- | --- | --- | --- |"]
    out += [f"| @{c['tag']} | {c['papel']} | {c['idade']} | {c['r']} | {c['takes']} | {c['obs'] or '—'} |" for c in data["chars"]]
    out.append("")
    for c in data["chars"]:
        out += [f"### @{c['tag']}", "", "```", c["prompt"], "```", ""]
    out += ["## Locações", ""]
    for l in data["locs"]:
        out += [f"### @{l['tag']} ({l['prio']}, {l['takes']})", "", l["why"], "", "```", l["prompt"], "```", ""]
    out += ["## Pendências", ""] + [f"- **{p[0]} · {p[1]}** ({p[2]}): {p[3]}" for p in PEND]
    out += ["", "## Riscos", ""] + [f"- **{r[0]}:** {r[1]}" for r in RISKS]
    return "\n".join(out) + "\n"


def build_html(data):
    payload = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    with open(os.path.join(HERE, "page.html"), encoding="utf-8") as f:
        page = f.read()
    return page.replace("/*__DATA__*/null", payload)


if __name__ == "__main__":
    data = build_data()
    with open(os.path.join(HERE, "codemig-vt60-shotlist.html"), "w", encoding="utf-8") as f:
        f.write(build_html(data))
    with open(os.path.join(HERE, "codemig-vt60-shotlist.md"), "w", encoding="utf-8") as f:
        f.write(build_md(data))
    for s in data["scenes"]:
        for g in s["gens"]:
            print(f"{g['id']:<12} {g['dur']:>3}s {g['nshots']} planos {g['words']:>5} palavras")
    print("corte:", round(sum(s['d'] for s in SCENES), 1), "s")
