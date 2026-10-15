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
    dict(id="T01", b="ab", t="Abertura: pico, descida e sala (T01 a T03)", d=12.0,
         desc="Plano aberto do jovem virando; corte pro close com a fala; a câmera desce logo depois que ele termina (aos 3s), atravessa terra, minério e aço e pousa na sala, onde o aluno responde e a professora corrige.",
         gens=[gen("T01-A", G.T01A,
                   "No alto do pico, o jovem de costas, de mochila, centralizado e de corpo inteiro num plano bem aberto, olhando os morros. Ele dá uma volta rápida, de uns 1s, até ficar de frente pra câmera, sorrindo, e segura o olhar.",
                   "nada.",
                   "de costas, olhando os morros — 2s · volta rápida, 1s — 1s · segura de frente — 2s = 5s",
                   "ele de frente, quadrado pra câmera, olhando a lente. O corte cai nesse olhar.",
                   "Plano bem aberto e simétrico, o único do filme: câmera baixa, a uns 60 cm do chão, mostrando a rocha em primeiro plano, a figura pequena e inteira ao centro e os morros caindo dos dois lados. O giro é rápido (~1s) e completo, para o T01-B começar de onde este termina (ele de frente, olhando a lente).",
                   ["Bem aberto, câmera baixa, centralizado: de costas, volta rápida, segura de frente"],
                   "reference-to-video", ["@JOVEM (character sheet) — identidade"],
                   "confira quatro coisas: câmera baixa com o chão aparecendo, plano bem aberto, ele no centro com o corpo inteiro, e o giro terminando de frente (ombros quadrados). Sem locação anexada. Na montagem entra só um trecho curto (~3s) deste plano."),
               gen("T01-B · 9s", G.T01B_SHORT,
                   "Close do jovem, que fala por cima do vento. Logo depois que ele termina (a fala acaba em ~2s e ele segura o sorriso até os 3s), a câmera desce reta e nivelada, num speed ramp: pelo corpo, terra, minério, vigas, ventilador ligado, e pousa no aluno. O aluno responde; a professora entra abaixada pela direita e fala com ele, corrigindo; ele olha pra ela, concorda e sorri.",
                   "JOVEM: \"Em Minas, terra não é só terra.\" / ALUNO: \"É futuro.\" / PROFESSORA: \"E minério não é só minério, viu?\"",
                   "close: fala em ~2s e sorriso até os 3s — 3s · descida com speed ramp — 2s · \"É futuro.\" e a professora entra — 1s · \"E minério não é só minério, viu?\" com uma olhadinha pra câmera, e ele concorda e sorri — 3s = 9s",
                   "o aluno olhando pra professora, concordando com um sorriso.",
                   "Versão escolhida por você, a de 9s, por causa do speed ramp. É o seu bloqueio de 8s, com a fala do jovem fechando em 3s. A descida leva 2s, com o speed ramp dentro deles, e o pouso cai na entrada do aluno. É a que cabe no teto de 60s. Mudanças desta rodada: (a) as raízes eram grandes e pareciam lava, então agora são raiz simples de grama: finas, claras, pequenas e quietas, num solo marrom comum, sem brilho e sem laranja ou vermelho (o \"solo vermelho\" saiu do prompt, porque junto com raiz escura dava cara de lava); o prompt ainda manda ignorar os gravetos marrons do seu guia, que representam raízes, e o NEGATIVE proíbe raiz grande, grossa ou brilhante e brilho de lava; (b) a camada de terra virou só um lampejo, e a pedra em camadas e o veio largo de minério de ferro, com brilho metálico, são o corpo da descida. (c) ritmo: a fala do jovem (10 sílabas) agora tem janela de 2s (0–2s), num fluxo só e sem pausa depois de \"Em Minas,\"; ele segura o sorriso até os 3s do guia e a câmera desce a partir daí; a janela da professora fica em 3s porque a sua gravação tem 2,4s. Para ajudar, no bloqueio 3D você pode tirar os gravetos e encolher a faixa de terra. Rodada anterior: (1) a voz da professora vem da sua gravação (@Audio1, ElevenLabs \"Scheila · Serious and Direct\", 2,4s), em que uma professora diz \"E minério não é só minério, viu?\", a mesma fala que ela diz no filme: o prompt manda copiar só o timbre, o sotaque e o jeito de professora, e o VOICE LOCK dela aponta pra essa gravação; (2) a fala dela agora é a frase inteira, \"E minério não é só minério, viu?\", com 7 palavras, e a janela é de 3s (6–9s), porque a gravação tem 2,4s; o aceno e o sorriso do aluno acontecem quando ela termina, ainda dentro dos 9s; (3) a professora olha pro aluno e dá UMA olhadinha rápida pra câmera no meio da fala; (4) a sala ficou menos sóbria: atrás do aluno, na parede de fundo, um armário de madeira clara, uma estante de livros coloridos e fileiras de desenhos de criança (sol, árvore, casa, foguete, sem texto); (5) os colegas estão felizes: sorrindo, relaxados, de olho brilhando, um cutucando o outro, alguns rindo sem som. Entendi \"T01-B e T01-C\" como as duas versões do T01-B (9s e 18s): as mudanças valem para as duas.",
                   ["Uma geração só: close e fala, descida com speed ramp, sala"],
                   "reference-to-video", ["@JOVEM (character sheet) — identidade", "@PICO_FRAME (último frame do T01-A, ele de frente) — só lugar, luz e roupa; nunca como primeiro frame nem enquadramento", "@ALUNO (character sheet) — identidade", "@PROFESSORA (character sheet) — identidade", "@Audio1 — sua gravação do ElevenLabs (Scheila, Serious and Direct): só a voz da professora", "@Video1 — blocking-9s-sem-texto.mp4 (9s, sem texto, feito do seu blocking-2-9s: close 3s, descida 2s, sala 4s), referência só de movimento. Plano B: o blocking-8s.mp4, que tem texto na tela (estenda o último frame em ~0,4s)"],
                   "confira: a fala dele acaba em ~2s, sem pausa depois de \"Em Minas,\", e a descida começa aos 3s; a terra passa num lampejo, com raiz fininha de grama e sem brilho de lava, e a pedra e o minério dominam; o ventilador gira; a professora entra pela direita, abaixada, e fala PARA o aluno com uma olhadinha pra câmera, na voz da sua gravação; armário, estante e desenhos atrás do aluno; colegas felizes; sem lousa atrás do aluno; sem efeitos sonoros (se vier whoosh ou rumble, peça edição de áudio: remover todos os efeitos, manter vento e falas). Se usar o blocking-8s.mp4 em vez do guia sem texto, estenda o último frame em ~0,4s. Não anexe o guia de 19s nesta versão: os tempos dele (close 5s, descida 7s, sala 7s) não batem com a linha do tempo de 9s (3s, 2s, 4s). A cadeia terra, minério, aço passa em cerca de 1,5s: se não ler, use a versão de 18s."),
               gen("T01-B · 18s", G.T01B_LONG,
                   "Close do jovem, que fala por cima do vento. Logo depois que ele termina (a fala acaba em ~2s e ele segura o sorriso até os 3s), a câmera desce reta e nivelada, no ritmo do bloqueio: pelo corpo, terra, minério, vigas, ventilador ligado, e pousa no aluno. O aluno responde; a professora entra abaixada pela direita e fala com ele, corrigindo; ele olha pra ela, concorda e sorri.",
                   "JOVEM: \"Em Minas, terra não é só terra.\" / ALUNO: \"É futuro.\" / PROFESSORA: \"E minério não é só minério, viu?\"",
                   "close: fala em ~2s e sorriso até os 3s — 3s · desce pelo corpo — 2s · terra e minério — 3s · vigas, forro e ventilador — 2s · pouso — 2s · \"É futuro.\" e a professora entra — 1s · fala dela com uma olhadinha pra câmera — 3s · ele concorda e sorri — 2s = 18s",
                   "o aluno olhando pra professora, concordando com um sorriso.",
                   "Versão longa, mantida. Segue o bloqueio de 19s, com a fala do jovem fechando em 3s (no bloqueio o close tem 5s). A cadeia terra, minério, aço e escola fica legível. Mesmas mudanças da versão de 9s (raiz simples de grama, terra em lampejo, pedra e minério em destaque): voz e jeito de professora pela sua gravação (@Audio1), fala dela com a frase inteira \"E minério não é só minério, viu?\" e janela de 3s (13–16s), uma olhadinha dela pra câmera, sala com armário, estante e desenhos atrás do aluno, colegas felizes.",
                   ["Uma geração só: close e fala, descida no ritmo do bloqueio, sala"],
                   "reference-to-video", ["@JOVEM (character sheet) — identidade", "@PICO_FRAME (último frame do T01-A, ele de frente) — só lugar, luz e roupa; nunca como primeiro frame nem enquadramento", "@ALUNO (character sheet) — identidade", "@PROFESSORA (character sheet) — identidade", "@Audio1 — sua gravação do ElevenLabs (Scheila, Serious and Direct): só a voz da professora", "@Video1 — blocking-2-9s.mp4 (19s, sem texto), referência só de movimento (corte ~2s do close inicial e estenda o último frame em ~1s: fica 18s)"],
                   "mesmos pontos de conferência da versão de 9s. No bloqueio de 19s, o close dura 5s e a fala do jovem agora fecha em 3s: corte 2s do começo e estenda o final em 1s. Se couber no filme, esta versão rende mais no filme; no teto de 60s ela estoura cerca de 9s.")]),
    dict(id="T04", b="rv", t="Eletroposto", d=2.8,
         desc="Plugue entrando no carro elétrico, a luz acendendo, o homem fala de lado e dá um tapinha no teto.",
         gens=[gen("T04", G.T04,
                   "Num estacionamento moderno com ipês floridos: detalhe do plugue entrando no carro elétrico, close da luz da porta acendendo, o homem fala de lado pra lente e dá um tapinha satisfeito no teto.",
                   "HOMEM: \"É a possibilidade de um mundo mais verde,\"",
                   "plugue — 3s · luz acende — 2s · fala — 3s · tapinha — 2s = 10s",
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
                   "placa nos rolos — 3s · joystick — 2s · fala — 2s · bobina — 2s = 9s",
                   "a bobina rolando, câmera ainda andando.",
                   "Mesmo travelling lateral do revezamento em todos os planos. Fábrica limpa e automatizada, nada de chão de fábrica velho.",
                   ["Close: placa incandescente nos rolos", "Close: mão no joystick", "Médio-aberto: fala", "Close: bobina pronta rolando"],
                   "reference-to-video", ["@OPERARIO (character sheet) — identidade + EPI"],
                   "conferir EPI completo e sem logo, e telas do console sem texto legível.")]),
    dict(id="T07", b="rv", t="Restaurante", d=1.8,
         desc="Visão estritamente zenital (90°, de cima pra baixo), câmera parada, de um prato de salada no balcão de inox recebendo azeite de ervas verde-escuro; corte para o dono já olhando pra câmera, com a cozinha industrial de inox atrás, jogando o pano no ombro enquanto fala.",
         gens=[gen("T07", G.T07,
                   "Na cozinha industrial de um restaurante saudável em BH, tudo de inox: visão estritamente zenital (90°, reta de cima), câmera parada, do prato de salada sobre o balcão de inox (campainha, utensílios de chef e comandas de papel ao lado) sendo finalizado com um fio de azeite de ervas verde-escuro, saindo de uma bisnaga. Corte: o dono, que já olha pra câmera no primeiro frame, com a cozinha de inox e os cozinheiros trabalhando ao fundo, fala e joga um pano no ombro.",
                   "DONO: \"de uma economia mais sustentável.\"",
                   "zenital 90° parado: azeite sobre o prato — 3s · dono olhando pra câmera, fala e joga o pano — 3s · segura o sorriso — 1s = 7s",
                   "ele sorrindo pra lente, a cozinha trabalhando atrás; corte seco.",
                   "Dois planos, como você pediu. O primeiro agora é uma vista zenital absoluta — lente apontada reto pra baixo, 90° do balcão, prato como círculo perfeito, sem horizonte, parede ou borda do balcão, e o prompt proíbe vista de lado ou em ângulo. Fica parado (só uma respiração leve de câmera na mão, sem andar); o segundo plano anda de lado. A cozinha virou industrial: inox por todo lado (bancadas, fogão sob coifa, prateleiras, recipientes plásticos), dólmãs brancos, sem madeira, plantas nem luz de pendente. Ele já começa olhando pra lente, sem virar. A cliente saiu. A fala ganhou 1s (agora 3s, no ritmo tranquilo) porque ele estava atropelando a frase; o take passou de 6s para 7s. O pano cai no ombro durante a frase.",
                   ["Zenital: azeite de ervas sobre o prato de salada", "Médio-aberto: cozinha ao fundo, pano no ombro, fala"],
                   "reference-to-video", ["@DONO (character sheet) — identidade"],
                   "confira: plano 1 exatamente reto de cima (prato circular perfeito, sem horizonte nem parede) e sem andar, balcão de inox com campainha, utensílios e comandas, azeite verde-escuro saindo de uma bisnaga; plano 2 com ele olhando pra lente desde o primeiro frame e cozinha industrial de inox com cozinheiros ao fundo (sem logos, nada de salão chique); o pano pousa no ombro durante a fala. Se quiser a câmera 100% travada no plano 1, me diga: deixei uma respiração mínima para não ficar congelado.")]),
    dict(id="T08", b="rv", t="Mina de nióbio", d=8.3,
         desc="Detalhe da luva deslizando na parede de minério; depois o funcionário anda pra frente num patamar da cava, com a câmera num arco leve em volta dele, e abre a frase: o que o mundo olha e o que Minas olha, em aberto.",
         gens=[gen("T08", G.T08,
                   "Na beira de uma cava moderna em Araxá, no fim de tarde: close da luva deslizando pela parede de minério pálido, soltando poeira; corte, e o funcionário anda pra frente num patamar largo da cava, falando com a lente e sorrindo, enquanto a câmera anda de lado e recua, fazendo um arco leve em volta dele; a frase termina em aberto e ele segue andando e sorrindo.",
                   "FUNCIONÁRIO: \"Enquanto o mundo olha para o nióbio e as terras raras de Minas, Minas olha para o que há de mais raro na nossa terra:\" (a frase fica em aberto; quem a fecha é a agricultora, no T09-A, com \"a nossa gente.\")",
                   "luva na parede de minério — 2s · anda de frente e fala — 7s · segue andando e sorrindo — 2s = 11s",
                   "ele ainda andando pra frente, sorrindo, com a frase em aberto; corte para a plantação (T09-A).",
                   "Inversão pedida: a frase longa que era da agricultora agora é do funcionário, e o take segue a estrutura que você aprovou para ela: um detalhe curto (agora a luva na parede de minério, no lugar da mão nas plantas) e um plano médio-aberto dele andando pra frente, só com os olhos na lente, com a câmera andando de lado e recuando em arco leve (~20° de cada lado), tipo orbit. Luz de fim de tarde, sol à esquerda, como nos takes anteriores da mina (a manhã clara fica na plantação). A frase termina em aberto (os dois-pontos): tom de expectativa e sorriso, não de conclusão, porque quem fecha é a agricultora. A pronúncia de \"nióbio\" veio junto: no prompt está \"nióbiu\" (como se fala), com guia nee-OH-byoo, B bem marcado, nunca \"niório\", na fala, na trava e no NEGATIVE. Assumi fala em cena, com lipsync, e não V.O. A janela é de 7s para as 41 sílabas (uns 6 por segundo), mais 2s de sorriso no fim; a geração é de 11s. A cena da pedra na frente do rosto saiu: a revelação agora é da agricultora (T09-A).",
                   ["Detalhe: luva deslizando na parede de minério", "Médio-aberto: ele anda pra frente e fala, câmera em arco leve"],
                   "reference-to-video", ["@FUNCIONARIO (character sheet) — identidade + EPI"],
                   "confira: ele anda pra frente o tempo todo, sem virar a cabeça de lado (só os olhos vão à lente); a câmera anda de lado, esquerda→direita, e recua, num arco leve em volta dele, sem parar nem passar pro lado ou pras costas; a fala corre sem pausa e termina em aberto, com expectativa; \"nióbio\" dito nee-OH-byoo (não \"niório\"); EPI completo e sem logo; luz de fim de tarde, sol à esquerda; olhos legíveis atrás dos óculos. Validar o EPI com a SST da operadora antes do final (P11). Fala longa (41 sílabas em 7s): se o lipsync escorregar no fim, a montagem cobre o final com o close da luva na parede.")]),
    dict(id="T09", b="vr", t="Plantação: a virada", d=10.0,
         desc="A: a agricultora segura uma planta de soja na frente do rosto, desfocado atrás; abaixa a planta, revela o rosto já sorrindo e diz \"a nossa gente.\". B: plano baixíssimo dela de costas, falando enquanto anda até o trator, contra o sol da manhã e com flare; corte para o rosto em médio close, que fala com um dolly-out lento.",
         gens=[gen("T09-A · revelação", G.T09,
                   "Numa fazenda de soja moderna no Triângulo, de manhã clara: uma planta de soja nítida, na mão da agricultora, cobre quase todo o rosto dela, que mal aparece desfocado atrás; ela abaixa a planta, revelando o rosto já sorrindo, e já diz só \"a nossa gente.\", sorrindo, e segura o olhar.",
                   "AGRICULTORA: \"a nossa gente.\" (fecha a frase do funcionário no T08: \"…na nossa terra:\" → \"a nossa gente.\")",
                   "planta na frente do rosto — 1s · abaixa a planta, revela o rosto sorrindo e fala — 2s · segura o sorriso — 2s = 5s",
                   "o olhar pousado na lente, sorrindo; corte seco para o plano baixo da plantação (T09-B).",
                   "A cena da pedra saiu: a revelação agora é dela, e o objeto virou o que cresce ali, uma planta de soja inteira (caule com folhas e vagens, as raízes fora do quadro). O gesto que você aprovou continua o mesmo: a planta nítida na frente, o rosto desfocado atrás, mal aparecendo; ela abaixa a planta, o rosto aparece já sorrindo, o foco chega nos olhos e a fala começa junto com o gesto, sem pausa. Faz sentido com o resto: a frase do funcionário termina em \"…na nossa terra:\", a planta (o que cresce aqui) enche o quadro e, ao abaixar, quem aparece é a pessoa, \"a nossa gente.\", e o plano seguinte abre com \"Afinal, o que cresce aqui:\". O rosto fica escondido só 1s (eram 3s com o nióbio), para a resposta não demorar depois dos dois-pontos; na montagem dá para alongar. Direção da fala: conclusiva, orgulhosa e sem seriedade, como a última palavra de uma frase maior. Luz: manhã clara, sol à esquerda, a mesma da plantação inteira. Os olhos precisam ficar legíveis sob a aba do chapéu.",
                   ["Close (revelação): planta na frente do rosto; ela abaixa e diz \"a nossa gente.\""],
                   "reference-to-video", ["@AGRICULTORA (character sheet) — identidade"],
                   "confira: o rosto quase não aparece no primeiro segundo e já está sorrindo quando aparece (sem pausa antes da fala); a planta é uma planta de soja de verdade (folhas e vagens, não um buquê), sai por baixo do quadro e não cruza o rosto; ela diz só \"a nossa gente.\"; os olhos pousam no terço superior (~45% da largura) e aparecem sob a aba do chapéu; sem luvas; luz de manhã, sem cara de entardecer.",
                   alt="Direção alternativa, se a planta virar buquê ou atrapalhar: sem objeto, ela abre as folhas da soja com a mão, revelando o rosto sorrindo, e diz a fala junto. Me peça que eu troco."),
              gen("T09-B · plantação", G.T09B,
                   "Numa fazenda de soja moderna, de manhã clara: plano aberto rente ao chão, com a agricultora pequena, de costas, andando pela linha da soja até um trator de porte médio ao longe e dizendo a primeira parte da frase, com o sol da manhã atrás do trator e um flare suave. Corte: médio close do rosto dela, no centro e reto pra lente, na frente do mesmo trator, com a luz do T09-A; ela já está de frente no corte e fala sorrindo, num fluxo só, com uma pequena pausa depois de \"nasce,\" e de \"vive,\", enquanto a câmera recua devagar (dolly-out, sem zoom) e o quadro vai abrindo.",
                   "AGRICULTORA, plano 1 (de costas): \"Afinal, o que cresce aqui:\" / plano 2: \"também deve construir novos caminhos para quem nasce, [pausa] vive [pausa] e trabalha aqui.\" Mesma voz e mesma entrega do \"a nossa gente.\", sem V.O.",
                   "de costas, fala e anda — 3s (fala em 0–2s) · rosto centralizado, fala corrida com duas pausas curtas e dolly-out — 5s · segura o sorriso — 2s = 10s",
                   "ela sorrindo pra lente, rosto no centro; corte para o match do T10.",
                   "É o antigo plano da cava, agora na plantação e com a agricultora, que diz \"Afinal, o que cresce aqui:\" e o resto da frase, como você corrigiu. Plano 1: lente quase no chão entre duas linhas de soja, ela pequena e de costas (chapéu, trança, camisa) andando até um trator de porte médio, uns 3 m, branco-sujo e cinza com uma faixa laranja e sem logo, bem longe, com o sol atrás do trator e UM flare. O contraluz é de manhã (sol a ~35°, alto no quadro), porque você não quis cara de entardecer na plantação; se preferir o sol baixo de fim de tarde, me diga. Plano 2: médio close centralizado com dolly-out lento, sem zoom, na mesma luz do T09-A (sol da manhã à esquerda, sem flare). O corte para a mãe cai em \"vive\" e o áudio dela segue por cima dos match cuts. Ritmo: a janela do plano 2 é de 5s (25 sílabas, uns 6 por segundo, mais as duas pausas curtas que você pediu, fora do texto entre aspas, num bloco PACING), e ela já está de frente no corte, sem pausa antes da primeira palavra; o sorriso final tem 2s, para uma fala que escorregue não ser cortada; a geração segue em 10s. Para o diálogo longo da plantação, a divisão em vários takes é a mesma que a da cava: a revelação (T09-A), o plano baixo (plano 1) e o médio close (plano 2), cada um com um pedaço da frase.",
                   ["Wide baixíssimo: ela de costas, falando e andando até o trator (contraluz, flare)", "Médio close (match): rosto centralizado, fala, dolly-out"],
                   "reference-to-video", ["@AGRICULTORA (character sheet) — identidade"],
                   "confira: plano 1 com a lente quase no chão, ela de costas e pequena, o trator bem longe e de porte médio, um flare só, e a voz dela dizendo \"Afinal, o que cresce aqui:\"; plano 2 com o rosto no centro, já de frente e falando no corte, a câmera recuando de verdade (sem zoom), as duas pausas curtas depois de \"nasce,\" e \"vive,\" e nenhuma outra, olhos legíveis sob a aba do chapéu, e a mesma luz do T09-A (manhã, sol à esquerda), sem flare; mesma voz e entrega nas duas falas. Se a câmera ficar parada ou der zoom, reforce \"the camera moves back, no zoom\".")]),
    dict(id="T10", b="mc", t="Mãe e recém-nascido", d=3.0,
         desc="Médio close da mãe com o bebê no colo, olhando pra câmera e sorrindo, com dolly-out lento.",
         gens=[gen("T10", G.T10,
                   "Num apartamento claro em BH, a mãe, com o recém-nascido no colo, olha pra lente e sorri, enquanto a câmera recua devagar (dolly-out) e o quadro vai abrindo.",
                   "nada na geração. Na montagem: o áudio da agricultora segue por cima.",
                   "olha pra lente, sorrindo, com o bebê no colo, dolly-out — 4s",
                   "segurando seu olhar, sorrindo; corte para o T11.",
                   "Simplificado como você pediu: enquadramento simples com dolly-out, ela olha pra câmera sorrindo com o bebê no colo. Sem o olhar pro bebê e de volta. Agora com character sheet (@MAE). Geração de 4s (mínimo do modelo); na montagem entram ~3s. Sem fala.",
                   ["Médio close (match): ela sorri pra lente com o bebê no colo, dolly-out"],
                   "reference-to-video", ["@MAE (character sheet) — identidade"],
                   "conferir a proporção do bebê (rosto parcialmente coberto), o rosto dela no centro o tempo todo e a câmera recuando sem zoom.")]),
    dict(id="T11", b="mc", t="Estádio", d=3.0,
         desc="Médio close da torcedora sentada numa arquibancada cheia, animada e empolgada com o jogo, olhando um pouco na direção da câmera, com dolly-out lento.",
         gens=[gen("T11", G.T11,
                   "Numa arquibancada de estádio, a torcedora, cercada de torcedores, acompanha o jogo empolgada, com os olhos brilhando na partida, um pouco ao lado da lente, enquanto a câmera recua devagar (dolly-out) e a torcida vai aparecendo em volta dela.",
                   "nada na geração. Na montagem: o áudio da agricultora segue por cima.",
                   "animada com o jogo, olhando um pouco ao lado da lente, dolly-out — 4s",
                   "ainda animada, de olho no jogo; corte para o T12.",
                   "Refeito: sem nenhuma menção ao Mineirão nem à estrutura do estádio. O prompt só diz que ela está sentada na arquibancada de um estádio com vários torcedores em volta. A atuação saiu do blasé sem exagero: ela está empolgada, com os olhos brilhando, uma respiração animada e um sorriso que vem e vai e vai abrindo conforme a jogada cresce (sem gritar, sem reações exageradas e sem formar palavras). Os olhos ficam ao lado da lente, nunca nela. Cabelo slicked back e camisa de futebol genérica terracota com gola creme. Atenção: a camisa do sheet saiu com um escudo azul e amarelo no peito. O prompt manda ignorar o emblema, mas o mais seguro é gerar o sheet de novo ou apagar o escudo antes de anexar. Geração de 4s; na montagem entram ~3s.",
                   ["Médio close (match): animada com o jogo, olhos ao lado da lente, dolly-out"],
                   "reference-to-video", ["@TORCEDORA (character sheet) — identidade"],
                   "conferir: ela animada e natural, nem blasé nem exagerada; peito da camisa liso (sem escudo, patrocínio, número ou texto); olhos ao lado da lente (não nela); torcedores ao redor de roupa comum, sem camisa, bandeira ou cachecol de clube.")]),
    dict(id="T12", b="mc", t="Ônibus", d=5.6,
         desc="O motorista, em médio close com dolly-out, sorri pra você; corte para o outro ângulo, e ele entrega a fala com o ônibus parado.",
         gens=[gen("T12", G.T12,
                   "Num ônibus urbano brasileiro de BH parado no ponto (corrimãos amarelos, bancos azuis estampados, piso de borracha cinza): médio close do motorista, no centro e reto pra lente, com dolly-out lento e um sorriso; corte seco para o outro ângulo, plano médio da cintura pra cima, e ele fala olhando pra lente.",
                   "MOTORISTA: \"Se Minas tem o que o futuro procura, esse futuro também precisa chegar até os mineiros.\"",
                   "médio close, dolly-out, sorri — 3s · outro ângulo, fala corrida com o ônibus parado — 5s · segura o sorriso — 2s = 10s",
                   "ele sorrindo; corte seco.",
                   "Do jeito que você descreveu: depois do dolly-out do match, ele não abre a porta e o estudante não existe mais neste take; o corte vai direto para o outro ângulo (o antigo plano 3, do primeiro banco, atrás e à direita dele) e ele entrega a fala. O ônibus está parado nos dois planos: nada passa pelas janelas, sem desfoque de movimento, porta de vidro fechada, e o prompt proíbe estudante, passageiro embarcando e ônibus em movimento. A geração caiu de 14s para 10s, e o T13 deixou de existir. Ritmo (esta rodada), com os enquadramentos iguais: medi o áudio do seu vídeo (só a energia do som; eu não consigo ouvir as palavras). No plano 2 a fala começou 1,1s depois do corte, teve uma pausa de 0,8s no meio e três curtas de ~0,2s, e terminou 1,5s depois do fim da janela de 6s. Nos trechos com voz, se ele disse a frase inteira (31 sílabas), o ritmo já é de uns 6 sílabas por segundo: o problema são o começo atrasado e as pausas, não a velocidade. Mudei quatro coisas: (1) a janela caiu de 6s para 5s (3–8s); (2) ele já está virado pra lente no corte e a primeira palavra sai em até 1/3 de segundo; (3) entrou um bloco PACING: um fluxo só, só respiro entre as frases, sem pausa; (4) segurar o sorriso passou a 2s (8–10s), para uma fala que ainda escorregue não ser cortada. A geração segue em 10s. Referências: @MOTORISTA, interior e cabine (duas fotos suas, só o lugar).",
                   ["Médio close (match): motorista sorri, dolly-out", "Médio: outro ângulo, ônibus parado, fala"],
                   "reference-to-video", ["@MOTORISTA (character sheet) — identidade", "@ONIBUS_INT (sua foto do interior do ônibus) — só o lugar; ignorar pessoas, textos, adesivos, luz e grade de cor", "@ONIBUS_CAB (sua foto da cabine, sem o motorista e sem textos) — só o lugar; apagar antes a estrela no volante"],
                   "conferir: ônibus parado (nada deslizando pelas janelas), porta fechada, sem estudante; interior com corrimãos amarelos e bancos azuis (nada de cromado nem tudo cinza), sem texto legível; plano 1 com o rosto no centro e a câmera recuando sem zoom; no plano 2 ele já está virado pra lente no corte e fala logo, num fluxo só, sem pausa de meio segundo no meio da frase.")]),
    dict(id="T14", b="cx", t="Trilhas de Futuro", d=3.8,
         desc="Um take só em plano médio: o estudante, sozinho em primeiro plano, já virado pra câmera, com o tablet na mão e o robozinho amador acenando atrás; fala a frase numa oficina clara, com os outros alunos ao fundo em seus próprios projetos.",
         gens=[gen("T14", G.T14,
                   "Na oficina de robótica do curso técnico, plano médio da cintura pra cima e sem cortes: o estudante, sozinho em primeiro plano e já virado pra lente, com o tablet baixo na mão (a tela nunca aparece) e o robozinho amador, sem pilhas, acenando em silêncio atrás do ombro dele, fala orgulhoso; os outros alunos ficam bem ao fundo, cada um no seu projeto; a sala é clara, com luz natural e luz do teto acesa.",
                   "ESTUDANTE: \"É para isso que a Codemig existe… para fazer essa conexão acontecer.\" (no prompt a palavra está escrita \"Cô-dê-mí-gui\", com guia de pronúncia)",
                   "fala — 5s · segura o sorriso — 1s = 6s",
                   "ele sorrindo pra lente, o robô ainda acenando; fim seco.",
                   "Ajustes desta rodada: (a) a sala estava escura: a luz agora é de sala clara, com luz natural da esquerda e as luminárias do teto acesas como enchimento uniforme (5600 K), sem cantos escuros e com a sala de fundo só meio ponto abaixo do primeiro plano; no NEGATIVE entrou sala escura, sombria ou turva. Entendi \"tem luz natural mas tem luz artificial também\" como as duas luzes devendo existir e deixar a sala clara, sem uma brigar com a outra; se você queria só luz natural, é só dizer. (b) saiu o soquinho (agora é um take só de 6s: 5s de fala e 1s segurando o sorriso), saiu a colega ao lado dele (ele está sozinho em primeiro plano; os outros alunos ficam bem ao fundo, cada um num projeto diferente, sem olhar pra câmera nem pro robô) e saiu a bateria do robô (e o NEGATIVE proíbe pilhas e bateria). (c) a pronúncia: ele disse \"Có\", com o ó aberto. O guia agora diz que a primeira sílaba tem o ô fechado e arredondado, como o \"o\" de \"bolo\" e \"avô\", nunca o ó aberto de \"avó\" ou \"pó\", e o NEGATIVE proíbe \"Có-dê-mí-gui\"; continua sem R no nome. Já são três tentativas com a palavra: se errar de novo, recomendo gravar só ela no ElevenLabs e trocar no áudio.",
                   ["Médio: sozinho, já virado pra lente, tablet na mão, robô amador acenando, fala"],
                   "reference-to-video", ["@ESTUDANTE (character sheet) — identidade e figurino do sheet"],
                   "conferir: \"Cô\" com ô fechado (não \"Có\"), sem R; sala clara, sem cantos escuros; ele sozinho em primeiro plano, os outros ao fundo em projetos diferentes; robô pequeno, amador, sem pilhas, acenando o tempo todo e mudo; nenhuma tela de tablet; estantes e caixas sóbrias, nada com cara de brinquedo.")]),
    dict(id="T15", b="cx", t="Hospital", d=6.8,
         desc="Um take só, em plano médio: a cena já começa com a enfermeira andando e falando no corredor de um hospital moderno e bem iluminado; ela pega o prontuário na parede em movimento e, no meio do take, faz uma curva de 90 graus com a câmera, sem parar de falar.",
         gens=[gen("T15", G.T15,
                   "Num corredor de hospital moderno, claro e bem iluminado por luz artificial, em plano médio e sem cortes: a enfermeira já está andando e falando no primeiro frame, tira o prontuário do suporte da parede sem parar, e no meio do take o corredor faz uma curva de 90 graus: a câmera, recuando à frente dela, vira a esquina e ela vira junto, sem quebrar o passo nem a fala.",
                   "ENFERMEIRA: \"Para fazer com que os recursos essenciais para a transição energética que o mundo precisa, também criem oportunidades para Minas.\" (a frase inteira, num fluxo só, ritmo ligeiro, do primeiro frame até ~7s)",
                   "já andando e falando, pega o prontuário — 3s · curva de 90 graus — 3s · corredor novo, termina a frase — 2s = 8s",
                   "ela andando, com um olhar caloroso pra você; fim seco no meio do passo.",
                   "Ajustado: (1) a cena já começa com ela no corredor, andando e falando, sem sair de quarto e sem porta; o prontuário sai do suporte da parede em movimento, nos primeiros 3s; (2) a curva agora é uma curva MESMO, de 90 graus, no meio do take (3–6s): o corredor vira para a esquerda, a câmera, ainda recuando à frente dela, faz a esquina e ela vira junto, as paredes passando e o corredor novo se abrindo atrás dela, tudo sem corte e sem quebrar a fala. Resto igual: plano médio (40°) o tempo todo, câmera sempre acompanhando, frase de 20 palavras em ~7s num ritmo ligeiro, luz artificial e corredor moderno. A curva de 90° é a parte mais arriscada: se o modelo perder a geometria, regerar antes de simplificar.",
                   ["Médio: já andando e falando, pega o prontuário, dobra a esquina de 90° e termina a frase"],
                   "reference-to-video", ["@ENFERMEIRA (character sheet) — identidade"],
                   "conferir: ela já em movimento e falando no primeiro frame; o prontuário pego sem parar; uma esquina de verdade (90°), não uma curva suave, com a câmera acompanhando sem corte; fala contínua e ligeira; corredor claro e moderno (nada velho, escuro ou verde), sem o interior de quarto e sem ninguém doente.")]),
    dict(id="T16", b="fc", t="Close final", d=3.5,
         desc="O jovem do começo, num close bem fechado, diz a última frase: \"O minério é nosso, o futuro também.\" Duas versões para você testar: v1 como estava e v2 com a atuação reforçada e a abertura guiada pelo seu mapa de profundidade.",
         gens=[gen("T16 · v1 (como estava)", G.T16_V1,
                   "No mesmo pico e na mesma luz do T01, o jovem em close bem fechado, na mão, fala direto com você, orgulhoso e sorrindo.",
                   "JOVEM: \"O minério é nosso, o futuro também.\"",
                   "olhar na lente — 1s · fala — 2s · sorriso — 2s = 5s",
                   "segurando seu olhar, sorrindo; corte para a assinatura.",
                   "Versão como estava antes da rodada de atuação, guardada para você comparar: close bem fechado (CU 18°, a 1,3 m, da sobrancelha ao queixo, um pouco à esquerda do centro), sem keyframe e com a atuação resumida (motivo, tática, olhos e um detalhe involuntário). É o close bem fechado do pré-shotlist, exceção à regra da fala em plano mais aberto (P14). Correção desta rodada: eu tinha entendido o contrário. A fala que fica é só \"O minério é nosso, o futuro também.\" (13 sílabas) e a frase \"Para transformar a força que vem da nossa terra em mais desenvolvimento para a nossa terra.\" saiu. Pela regra de ~6 sílabas por segundo, a fala tem 2s (1–3s) e o take caiu para 5s: abertura 1s, fala 2s, sorriso 2s.",
                   ["Close bem fechado: fala e sorriso"],
                   "reference-to-video", ["@JOVEM (character sheet) — identidade"],
                   "olhos e pele são o take inteiro. Conferir pupila viva e a pinta no rosto.",
                   alt="Direção alternativa: um pull-back na mão, do close até o aberto, durante \"o futuro também.\", revelando o mar de morros."),
               gen("T16 · v2 (atuação reforçada + mapa de profundidade)", G.T16,
                   "No mesmo pico e na mesma luz do T01, o jovem em close fechado, na mão, abre no enquadramento do seu mapa de profundidade (cabeça no centro, topo dos cachos perto da borda de cima, gola e alças da mochila embaixo), com sorriso de boca fechada e olhos na lente, e diz direto pra você, caloroso e orgulhoso, a última frase, até um sorriso aberto no fim.",
                   "JOVEM: \"O minério é nosso, o futuro também.\"",
                   "olhar na lente, sorriso de boca fechada — 1s · a fala, num fluxo só — 2s · segura o sorriso — 2s = 5s",
                   "segurando seu olhar, sorrindo; corte para a assinatura.",
                   "Correção desta rodada: eu tinha entendido o contrário. A fala que fica é só \"O minério é nosso, o futuro também.\" (13 sílabas), com a vírgula do seu texto, e a primeira frase (\"Para transformar a força que vem da nossa terra em mais desenvolvimento para a nossa terra.\") saiu. Pela regra de ~6 sílabas por segundo, a fala tem 2s (1–3s), num fluxo só, com só um respiro na vírgula, e o take é de 5s: abertura de 1s, fala de 2s e 2s segurando o sorriso (a sobra cobre uma fala que escorregue). A atuação foi reescrita para a frase curta: \"O minério é nosso,\" firme e rápido, com o queixo subindo e um aceno pequeno em \"nosso\"; depois \"o futuro também.\" como convite, com as sobrancelhas subindo, os olhos brilhando, o sorriso abrindo por completo e um leve inclinar pra lente, pedindo o seu sim; tudo acontece ENQUANTO ele fala. Se sair atropelado, volto a janela para 3s (take de 6s). A v1 ficou como estava, só com a frase certa. Mapa de profundidade (rodada anterior): a imagem colorida do rosto saiu e entrou o seu mapa de profundidade (@DEPTH_T16, branco = perto, escuro = longe). Ele fixa só o enquadramento de abertura: cabeça no centro, topo dos cachos perto da borda de cima, as duas orelhas e o pescoço, gola e alças da mochila na borda de baixo, morros em camadas ao fundo. Rosto, pele, cor e luz vêm do @JOVEM e do texto, então o mapa não carrega a textura mole do keyframe. O prompt proíbe quadro cinza, cara de mapa de profundidade, rosto liso ou vazio e silhueta branca. Três cuidados: (1) o seu mapa tem 16:9 (1672×941) e a geração é 21:9; se puder, gere o mapa em 21:9 a partir da mesma imagem, senão o modelo pode esticar ou cortar o enquadramento, e eu não sei como o Seedance trata essa diferença; (2) a documentação que eu tenho cita apenas modelos 3D de argila como referência de movimento e luz, nada sobre mapa de profundidade, então é teste: se vier cinza, com rosto vazio ou com o enquadramento errado, volte ao v1 ou me peça a versão com o keyframe (está no histórico do projeto); (3) sem a imagem colorida, a cor, a luz e o fundo vêm só do texto; se a abertura destoar do T01-A, o plano B é anexar o @PICO_FRAME só como lugar, luz e roupa, com o risco de ele trazer o rosto mole de volta",
                   ["Close fechado: abre no enquadramento do mapa, fala e sorri"],
                   "reference-to-video", ["@JOVEM (character sheet) — identidade", "@DEPTH_T16 (seu height map) — só a geometria da abertura: enquadramento, distâncias e camadas; nunca a cor, o visual cinza nem o rosto vazio"],
                   "olhos e pele são o take inteiro. Conferir: abertura no enquadramento do mapa e em cores; rosto com detalhe, não liso nem vazio; pupila viva, olhar viajando entre os seus olhos; a pinta no rosto dele; nada de tom de slogan, de lágrima nem de piscadela.",
                   alt="Direção alternativa: um pull-back na mão, do close até o aberto, durante \"o futuro também.\", revelando o mar de morros.")]),
    dict(id="T17", b="fc", t="Assinatura", d=2.5,
         desc="Assinatura em pós (After Effects): Codemig. O futuro é mineiro. / Codemge. Abrindo caminhos para Minas crescer.",
         gens=[], post="Sem geração. Locução \"Codemig. O futuro é mineiro.\" gravada (locutor ou ElevenLabs); lettering e logos no After Effects."),
]

STYLE_INTENT = """STYLE INTENT — CODEMIG VT 60" (v2)
MEDIUM: live-action photoreal
REGISTER: warm, proud institutional film — direct address, happy people, a modern Brazil
CAMERA LANGUAGE: handheld in every shot of the film; sub-actions in close-ups and
          details, the line in the most open shot of the take, hard cuts between them;
          relay (P1) = the camera travels frame-left → frame-right in every shot;
          match series (P2) = medium close-up, face centred, slow dolly-out (~3s)
LIGHT LOGIC: one dominant motivated natural source per scene with real falloff, always
          on the frame-LEFT side of the faces (low late sun outside, window inside);
          exceptions by request: the plantation (T09) is bright morning, T09-B shot 1 backlit with one flare
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
    ("Falas", "Só o texto da fala, com a janela de ~6 sílabas por segundo (cerca de 3 palavras por segundo) e um bloco PACING pedindo um fluxo só: respiro entre as frases, sem pausa. Pausas só onde você pediu (T09-B). A fala começa junto com o plano em que ele fala e o corte seguinte vem logo depois. O sotaque ficou num voice lock curto (R caipira ou R de BH, de P3) e o tom vem da atuação."),
    ("Gramática", "Câmera na mão o tempo todo. Subações antes e depois da fala em close ou detalhe, e a fala no plano mais aberto do take (médio-aberto, do joelho pra cima, com o lugar em volta), com corte seco entre eles. Exceções: o T01, com a fala no close como você pediu, e o T16, o close final."),
    ("Revezamento", "T04, T05, T07 e T08 (a mina): em todos os planos, inclusive nos closes, a câmera anda de lado da esquerda pra direita e nunca para. Cada take tem 3 ou 4 subações para a montagem apoiar a locução em off."),
    ("Virada", "Ordem no corte: T08 (mina: o funcionário abre a frase) → T09-A (plantação: a agricultora responde \"a nossa gente.\" e revela o rosto) → T09-B (ela no campo: \"Afinal, o que cresce aqui:\" e o match com dolly-out) → match cuts T10 a T12. A mina e a plantação não se intercalam."),
    ("Mundo", "Minas e Brasil modernos: arquitetura contemporânea, equipamento novo, espaços públicos bem cuidados e \"Brazilian\" espalhado pelos prompts. Nada rústico, pobre, velho ou colonial; isso está no template WORLD e na espinha do NEGATIVE."),
    ("Look", "O seu style ref de 35mm color negative, sem o parágrafo de cor e sem \"tactile surfaces\": a cor sai do ambiente de cada cena. A regra de luz é uma fonte natural dominante por cena, sempre do lado esquerdo do quadro."),
]

PEND = [
    ("P1", "Transição do revezamento (T04, T05, T07, T08)", "decidido",
     "Travelling lateral da esquerda pra direita em todos os planos, closes incluídos; a câmera nunca para. Corte seco entre subações e fala. Exceção pedida: T07 plano 1 (zenital, câmera parada). No T08 (mina) ele anda pra frente e o travelling lateral continua, com a câmera recuando no passo dele: vira um arco leve, tipo orbit."),
    ("P2", "Match cut (T09-B a T12)", "decidido",
     "Médio close centralizado, reto pra câmera, mesma distância, com dolly-out lento (~3s) em todos: agricultora (T09-B), mãe, torcedora e motorista, que abre o T12. É só a câmera recuando, sem movimento de lente: o quadro abre aos poucos de médio close para médio. O \"olhar que sobe\" do pedido anterior saiu."),
    ("P3", "Sotaque", "decidido",
     "R caipira para interior, campo e mineração; R de BH para a cidade. Agora num voice lock curto, sem direção de entrega."),
    ("P4", "Falas finais do T16", "decidido", "Sem coro; o protagonista fala tudo."),
    ("P5", "Casting e representação", "proposta",
     "Proposta do diretor nos character sheets: pardos, pretos e brancos em proporção próxima à de Minas, sem amarrar ofício a cor. Validar antes de gerar os sheets."),
    ("P6", "Teto de 60 segundos", "a decidir",
     "Com a abertura de 12s (T01-A curto + T01-B de 9s) e o bloco T09-B a T12 (plantação com fala, match cuts de ~3s cada), o corte estimado fica em ~65s; com o T01-B de 18s, ~74s (a abertura de 12s, o T06 já excluído, a fala curta do T16 e as falas mais corridas entram na conta). O pré-shotlist previa ~9s para a abertura inteira. O revezamento tem takes mais longos que o necessário, de propósito, para cobrir a locução em off: o enxugamento fica para a montagem, mas o teto de 60s precisa de uma decisão sua (onde cortar)."),
    ("P7", "Look (style ref)", "a testar",
     "FILM LOOK v2 a partir do seu ref. Antes de congelar, fazer draft do T01 (exterior com mergulho), do T05 (interior com travelling) e do T09 (virada com match)."),
    ("P9", "Falas da virada (T08 e T09)", "decidido",
     "Inversão: a mina vem antes da plantação, e os dois blocos não se intercalam. Ordem no corte: T08 (mina) → T09 (plantação) → T10 a T12. T08 (o funcionário, em cena, sem V.O.): \"Enquanto o mundo olha para o nióbio e as terras raras de Minas, Minas olha para o que há de mais raro na nossa terra:\", em aberto. T09-A (a agricultora): \"a nossa gente.\", na revelação. T09-B: plano 1 (de costas) \"Afinal, o que cresce aqui:\" e plano 2 \"também deve construir novos caminhos para quem nasce, [pausa] vive [pausa] e trabalha aqui.\", com as duas pausas pedidas (no prompt vão num bloco PACING, fora das aspas). Mesma voz e mesma entrega dela nas três falas, sem V.O. no ElevenLabs nesse trecho. O corte para a mãe cai em \"vive\" e o áudio dela segue por cima dos match cuts."),
    ("P10", "T12 só com o motorista", "decidido", "O T12 virou dois planos, só o motorista (match com dolly-out + fala em outro ângulo), com o ônibus parado, sem porta, sem estudante e sem T13."),
    ("P15", "Bloqueios 3D (T01-B)", "confirmar",
     "Os bloqueios entram como referência só de movimento. T01-B de 9s: use o blocking-9s-sem-texto.mp4 (9s, feito do seu blocking-2-9s: close 3s, descida acelerada 2s, sala 4s); plano B, o blocking-8s.mp4, que tem texto na tela (estenda o último frame em ~0,4s). T01-B de 18s: o blocking-2-9s.mp4 (19s, sem texto), cortando ~2s do close inicial e estendendo o último frame em ~1s. Não use o guia de 19s na versão de 9s: os tempos não batem. Se der, exportar em 21:9."),
    ("P16", "Locações", "decidido",
     "Nenhuma plate será gerada por enquanto; todos os takes saem de text-to-video para o lugar. Os prompts de locação ficam de reserva."),
    ("P18", "Tempo por fala (regra de ~6 sílabas por segundo)", "decidido",
     "Medi o áudio do T12 (só a energia do som, não as palavras): a fala começou 1,1s depois do corte, teve pausas de 0,8s e de ~0,2s e terminou 1,5s depois do fim da janela; se ele disse a frase inteira (31 sílabas), o ritmo nos trechos com voz já era de uns 6 por segundo. O problema são o começo atrasado e as pausas, não a velocidade. Regra nova: janela = sílabas ÷ 6, arredondada ao segundo mais próximo (mínimo de 1s, e 2s para falas de punchline de 3 palavras); a primeira palavra sai junto com o plano em que ele fala; todo take falado ganhou o bloco PACING (um fluxo só, só respiro entre as frases); e o sorriso final ganhou 1–2s de sobra, para uma fala que escorregue não ser cortada. Janelas que mudaram: T12 6s→5s, T09-B (plano 2) 6s→5s, T01-B (jovem) 3s→2s, T16 8s→2s (a fala agora é só \"O minério é nosso, o futuro também.\"). Exceções: o T07 fica com 3s (você pediu +1s porque ele atropelava), o T01-B (professora) com 3s (a sua gravação tem 2,4s), o T15 já era corrido (7s para 46 sílabas) e o T14 já tinha 5s para 27."),
    ("P19", "Sem efeitos sonoros no T01-B", "decidido",
     "Só vento forte sob a fala do jovem (que fala alto por cima dele), que some quando a câmera afunda. Da sala em diante, só o som natural: o ventilador ligado e um murmúrio leve dos alunos. Nada de whoosh, rumble ou chiado na descida."),
    ("P20", "Os 5s antes dos match cuts", "decidido",
     "Resolvidos pelo T09-B (a direção é sua; agora na plantação): plano 1, wide baixíssimo dela de costas andando até o trator, contra o sol da manhã e com flare, falando \"Afinal, o que cresce aqui:\"; plano 2, médio close dela com a fala e o dolly-out."),
    ("P21", "Sheets da mãe, da torcedora e do funcionário", "ok, com um alerta",
     "@MAE e @TORCEDORA gerados; o @FUNCIONARIO foi atualizado sem os protetores auriculares (descritor e prompt do sheet ajustados). Alerta: a camisa da torcedora saiu com um escudo azul e amarelo no peito. O prompt do T11 manda ignorar o emblema, mas o ideal é gerar o sheet de novo (o prompt agora pede o peito liso) ou apagar o escudo da imagem antes de anexar. Também saiu com jeans marrom-escuro, não índigo; o descritor segue o sheet."),
    ("P22", "Exceções de look no T09-B", "decidido",
     "Só o plano 1 (ela de costas) é diferente: contraluz, com o sol da manhã (~35°, alto no quadro) atrás do trator, e UM flare. O plano 2 usa a mesma luz do T09-A (sol da manhã à esquerda), sem flare. O resto do filme segue sem flares e com o sol à esquerda."),
    ("P23", "Ônibus do T12 (cara brasileira)", "decidido",
     "O interior estava com cara de ônibus gringo (alças de aço, bancos cinza). Agora segue as suas fotos: corrimãos amarelos, bancos azuis estampados, piso de borracha cinza. Duas referências só de lugar, sem pessoas: @ONIBUS_INT (a foto do interior) e @ONIBUS_CAB (a foto da cabine, já sem o motorista e sem textos). Antes de anexar a cabine, apague a estrela da marca no centro do volante. Ordem de upload: motorista, interior, cabine. O ônibus fica parado e o estudante não aparece mais no T12. O sheet do @MOTORISTA foi atualizado por você (uniforme sem escrita) e o descritor segue o sheet."),
    ("P24", "Voz da professora (T01-B)", "decidido",
     "A sua gravação do ElevenLabs (\"Scheila · Serious and Direct\", 2,4s) diz \"E minério não é só minério, viu?\" e foi feita para dar o tom de professora. Entra como @Audio1 só como referência de voz e de jeito de falar (timbre, sotaque, tom de professora), e a fala dela no filme é exatamente essa frase, inteira: \"E minério não é só minério, viu?\". A janela da fala é de 3s (6–9s no de 9s; 13–16s no de 18s), porque são 7 palavras e a gravação tem 2,4s. Ordem de upload: jovem, pico, aluno, professora, áudio e bloqueio."),
    ("P25", "T16 em duas versões", "testar",
     "v1 como estava (CU 18°, atuação resumida, sem imagem de apoio) e v2 com a atuação reforçada e a abertura guiada pelo seu mapa de profundidade (@DEPTH_T16, CU 31°). O keyframe colorido foi testado por você e perdeu qualidade, então saiu da v2. Gere as duas e fique com a melhor; a que não for usada pode sair. O mapa deve ter a proporção da geração (21:9)"),
    ("P26", "Exclusões", "decidido",
     "T06 (laboratório) saiu: some o card, o prompt e o sheet da @PESQUISADORA; o revezamento fica T04, T05, T07 e T08, e a frase corre \"…um mundo mais verde, de uma indústria mais eficiente, de uma economia mais sustentável.\" No T16 saiu \"Para transformar a força que vem da nossa terra em mais desenvolvimento para a nossa terra.\" (eu tinha entendido o contrário): a fala é só \"O minério é nosso, o futuro também.\", em 2s, e o take tem 5s."),
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
    ("Estádio (T11)", "nada de preto e branco, azul e branco, verde e branco ou verde-amarelo; a torcedora veste uma camisa de futebol genérica terracota com gola creme, sem escudo, patrocínio, número ou texto, e a torcida não veste camisa de clube."),
    ("Marcas reais", "carro, ônibus, mina, escola, programa e hospital saem sem marca e sem texto legível. Logos entram na pós."),
    ("Mineração (T08)", "EPI completo é trava crítica; falta validar com a SST (P11)."),
    ("Revelação da planta (T09-A)", "o modelo pode deixar a planta na frente do rosto, atravessá-la pelo rosto, virar a planta em buquê ou começar o sorriso depois do reveal. Se acontecer, reforce \"lowers the plant straight down\"; plano B: sem objeto, ela abre as folhas da soja com a mão (me peça)."),
    ("Pronúncia de nióbio (T08)", "a agricultora dizia \"niório\"; a palavra agora está na fala do funcionário, escrita \"nióbiu\" no prompt, com guia nee-OH-byoo. Se errar de novo, grave só \"nióbio\" no ElevenLabs e troque no áudio."),
    ("Dolly-out (match)", "o modelo pode deixar a câmera parada ou dar um zoom em vez de recuar. No draft, confira se a câmera recua de verdade (o rosto encolhe aos poucos e o fundo abre); reforce \"the camera moves back, no zoom\" se precisar."),
    ("Flare do T09-B", "um só, no plano 1 (sol da manhã atrás do trator). Se aparecer flare no plano 2, ou bolhas de bokeh, regenerar; o plano 2 tem que repetir a luz do T09-A."),
    ("Escudo na camisa da torcedora", "o sheet da @TORCEDORA veio com um escudo azul e amarelo no peito, que lembra seleção ou clube. Gere o sheet de novo com o peito liso ou apague o escudo; no T11 confira que o peito sai liso."),
    ("Pronúncia de Codemig (T14)", "o modelo leu \"Codemigri\" e depois \"Có-dê-mí-gui\" (ó aberto). O prompt pede o ô fechado, como em \"bolo\" e \"avô\", sem R. Se errar de novo, grave só essa palavra no ElevenLabs e troque no áudio."),
    ("Tela do tablet (T14)", "o modelo tende a mostrar a tela ou um brilho dela. O prompt mostra o tablet quase de perfil e proíbe qualquer interface; se aparecer, regerar com o tablet ainda mais de lado."),
    ("Corredor do T15", "se o hospital sair velho, escuro ou verde, reforce a luz de LED neutro-quente e as paredes claras com madeira; a esquina de 90° é o ponto frágil: se a câmera cortar, perder a ela ou a curva sair mole, regerar reforçando \"a true 90-degree corner\"; se a fala vier lenta, reforce \"brisk, no drawn-out words\"."),
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
        ("LIGHT · exterior de dia (plantação, T09)", T.LIGHT_EXT_DAY),
        ("LIGHT · contraluz de manhã (T09-B, só o plano 1)", T.LIGHT_DAY_BACK),
        ("FILM LOOK com um flare (T09-B, plano 1)", T.FILM_LOOK_FLARE),
        ("LIGHT · interiores (base)", T.light_int("[window]", "[practicals]", "[reach]")),
        ("CAMERA · na mão", T.handheld()),
        ("CAMERA · revezamento", T.REV_CAMERA),
        ("MATCH FRAME (série T09-B a T12)", T.MATCH_FRAME),
        ("CAMERA · dolly-out", T.dolly_out(3)),
        ("Quadro do T09-A (revelação)", T.REVEAL_FRAME),
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
