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
         desc="Plano aberto do jovem virando; corte pro close com a fala; a câmera desce no instante em que ele termina, atravessa terra, minério e aço e pousa na sala, onde o aluno responde e a professora corrige.",
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
                   "Close do jovem, que fala por cima do vento. No instante em que ele termina, a câmera desce reta e nivelada, num speed ramp: pelo corpo, terra, minério, vigas, ventilador ligado, e pousa no aluno. O aluno responde; a professora entra abaixada pela direita e fala com ele, corrigindo; ele olha pra ela, concorda e sorri.",
                   "JOVEM: \"Em Minas, terra não é só terra.\" / ALUNO: \"É futuro.\" / PROFESSORA: \"Minério não é só minério.\"",
                   "close e fala — 3s · descida com speed ramp — 2s · \"É futuro.\" e a professora entra — 1s · \"Minério não é só minério.\" — 2s · ele concorda e sorri — 1s = 9s",
                   "o aluno olhando pra professora, concordando com um sorriso.",
                   "Versão recomendada. É o seu bloqueio de 8s, com a fala do jovem fechando em 3s e as duas falas coladas uma na outra, sem espaço morto. A descida leva 2s, com o speed ramp dentro deles, e o pouso cai na entrada do aluno. É a que cabe no teto de 60s.",
                   ["Uma geração só: close e fala, descida com speed ramp, sala"],
                   "reference-to-video", ["@JOVEM (character sheet) — identidade", "@PICO_FRAME (último frame do T01-A, ele de frente) — só lugar, luz e roupa; nunca como primeiro frame nem enquadramento", "@ALUNO (character sheet) — identidade", "@PROFESSORA (character sheet) — identidade", "@Video1 — blocking-8s.mp4, referência só de movimento (estenda o último frame em ~0,4s para fechar 9s)"],
                   "confira: a descida começa assim que ele termina; o ventilador gira; a professora entra pela direita, abaixada, e fala PARA o aluno; sem lousa atrás do aluno; sem efeitos sonoros (se vier whoosh ou rumble, peça edição de áudio: remover todos os efeitos, manter vento e falas). Estenda o último frame do bloqueio em ~0,4s. A cadeia terra, minério, aço passa em cerca de 1,5s: se não ler, use a versão de 18s."),
               gen("T01-B · 18s", G.T01B_LONG,
                   "Close do jovem, que fala por cima do vento. No instante em que ele termina, a câmera desce reta e nivelada, no ritmo do bloqueio: pelo corpo, terra, minério, vigas, ventilador ligado, e pousa no aluno. O aluno responde; a professora entra abaixada pela direita e fala com ele, corrigindo; ele olha pra ela, concorda e sorri.",
                   "JOVEM: \"Em Minas, terra não é só terra.\" / ALUNO: \"É futuro.\" / PROFESSORA: \"Minério não é só minério.\"",
                   "close e fala — 3s · desce pelo corpo — 2s · terra e minério — 3s · vigas, forro e ventilador — 2s · pouso — 2s · \"É futuro.\" e a professora entra — 1s · fala dela — 2s · ele concorda e sorri — 3s = 18s",
                   "o aluno olhando pra professora, concordando com um sorriso.",
                   "Versão longa, mantida. Segue o bloqueio de 19s, com a fala do jovem fechando em 3s (no bloqueio o close tem 5s) e as falas dos dois sem espaço. A cadeia terra, minério, aço e escola fica legível.",
                   ["Uma geração só: close e fala, descida no ritmo do bloqueio, sala"],
                   "reference-to-video", ["@JOVEM (character sheet) — identidade", "@PICO_FRAME (último frame do T01-A, ele de frente) — só lugar, luz e roupa; nunca como primeiro frame nem enquadramento", "@ALUNO (character sheet) — identidade", "@PROFESSORA (character sheet) — identidade", "@Video1 — blocking-19-s.mp4, referência só de movimento (corte ~2s do close inicial e estenda o último frame em ~1s: fica 18s)"],
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
    dict(id="T06", b="rv", t="Laboratório", d=1.2,
         desc="Uma gota azul se mistura no vórtice do béquer, o rack entra no analisador, a pesquisadora fala e confere um frasco.",
         gens=[gen("T06", G.T06,
                   "Num laboratório farmacêutico moderno: detalhe do vórtice no béquer com uma gota azul se misturando, o rack de tubos entrando no analisador, a pesquisadora levanta os olhos e fala, depois confere um frasco contra a janela.",
                   "PESQUISADORA: \"de novas tecnologias,\"",
                   "vórtice — 3s · analisador — 2s · fala — 2s · frasco — 2s = 9s",
                   "ela conferindo o frasco, câmera ainda andando.",
                   "O close de algo sendo misturado que você pediu abre o take. É o trecho mais curto do filme no corte, então as subações seguram a locução.",
                   ["Detalhe: vórtice, gota azul se mistura", "Close: rack entra no analisador", "Médio-aberto: fala", "Close: frasco contra a janela"],
                   "reference-to-video", ["@PESQUISADORA (character sheet) — identidade + EPI"],
                   "se sair rótulo legível em frasco ou tela, regerar: texto não pode aparecer.")]),
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
    dict(id="T08", b="rv", t="Plantação", d=8.3,
         desc="A mão passa pelas plantas; a agricultora anda pra frente numa manhã clara e fala olhando pra lente, com a câmera fazendo um arco leve em volta dela.",
         gens=[gen("T08", G.T08,
                   "Numa fazenda de soja moderna no Triângulo, de manhã clara, com pivô central ao fundo: close da mão passando nas plantas e, em seguida, a agricultora anda pra frente falando com a lente e sorrindo, até o fim da frase, enquanto a câmera anda de lado e recua, fazendo um arco leve em volta dela.",
                   "AGRICULTORA: \"Enquanto o mundo olha para o nióbio e as terras raras de Minas, Minas olha para o que há de mais raro na nossa terra:\"",
                   "mão nas plantas — 2s · anda de frente e fala — 7s · segue sorrindo — 1s = 10s",
                   "ela ainda andando pra frente, olhando pra você; corte pra mina.",
                   "Pronúncia: ela dizia \"niório\" (e o 11s não resolveu: o problema é a palavra, não o tempo). No prompt a palavra está escrita \"nióbiu\" (como se fala), com guia de pronúncia (nee-OH-byoo, B bem marcado, nunca \"niório\") na fala, na trava e no NEGATIVE. Se ainda errar, plano B: a V.O. do ElevenLabs cobre \"Enquanto o mundo olha para o nióbio e as terras raras de Minas,\" sobre o close da mão (esticado para ~4s) e ela fala em cena só \"Minas olha para o que há de mais raro na nossa terra:\" (também resolve a frase longa). Refeito a seu pedido. Luz: manhã clara, sol alto à esquerda (~50°), céu azul com algumas nuvens, sem cara de entardecer (variante LIGHT_EXT_DAY nos templates). Movimento: ela anda pra frente pela linha da soja, com cabeça e corpo na direção da caminhada, e só os olhos encontram a lente. O travelling lateral do revezamento volta: a câmera anda de lado, da esquerda pra direita, e recua no passo dela, então faz um arco leve em volta dela (cerca de 25° de cada lado da linha da caminhada), como um orbit curto. Nunca para, nunca vai pro lado ou pras costas dela. A fala continua ocupando 7s.",
                   ["Close: mão passando nas plantas", "Médio-aberto: ela anda pra frente e fala, câmera em arco leve"],
                   "reference-to-video", ["@AGRICULTORA (character sheet) — identidade"],
                   "confira: ela anda pra frente o tempo todo, sem virar a cabeça de lado (só os olhos vão à lente); a câmera anda de lado, esquerda→direita, e recua, num arco leve em volta dela, sem parar nem passar pro lado ou pras costas; luz de manhã clara, sem sol baixo/alaranjado nem sombra comprida; olhos legíveis sob a aba do chapéu. Fala longa (22 palavras em 7s): se o lipsync escorregar no fim, a montagem cobre o final com o close da mão nas plantas; se errar a frase, abrir 1s na janela (como no T07).")]),
    dict(id="T09", b="vr", t="Mina de nióbio", d=10.5,
         desc="A: o funcionário segura o nióbio na frente do rosto, desfocado atrás; tira o nióbio e diz \"a nossa gente.\". B: plano baixíssimo dele de costas, falando enquanto anda até a máquina, contra o sol e com flare; corte para o rosto em médio close, que fala com um dolly-out lento.",
         gens=[gen("T09-A · nióbio", G.T09,
                   "Na beira de uma cava moderna em Araxá: um pedaço de nióbio prateado, na luva, cobre quase todo o rosto do funcionário, que mal aparece desfocado atrás; ele abaixa o nióbio, revelando o rosto já sorrindo, e já diz só \"a nossa gente.\", sorrindo, e segura o olhar.",
                   "FUNCIONÁRIO: \"a nossa gente.\" (fecha a frase da agricultora no T08; o resto, \"Afinal, o que cresce aqui também deve construir novos caminhos para quem nasce, vive e trabalha aqui.\", é V.O. gravada no ElevenLabs e entra na montagem)",
                   "nióbio na frente do rosto — 3s · abaixa o nióbio, revela o rosto já sorrindo e já fala — 2s · segura o sorriso — 1s = 6s",
                   "o olhar pousado na lente, sorrindo; corte seco para o plano baixo da cava (T09-B).",
                   "Um plano só, no close do match. O gesto da virada continua sendo o foco: o nióbio nítido na frente, o rosto quase escondido, e quando o nióbio sai por baixo o rosto aparece já sorrindo, o foco chega nos olhos e a fala começa junto com o gesto, sem pausa. A fala fecha a frase do T08 (\"...nossa terra:\" → \"a nossa gente.\"), com direção conclusiva, orgulhosa e sem seriedade. O nióbio agora é prateado e facetado, como na sua foto de referência (antes eu tinha escrito marrom-escuro). Não anexei a foto: ela traria o rosto daquele homem e a marca d'água; o prompt descreve o enquadramento e o metal.",
                   ["Close (match): nióbio na frente do rosto; ele tira e diz \"a nossa gente.\""],
                   "reference-to-video", ["@FUNCIONARIO (character sheet) — identidade + EPI"],
                   "confira: o rosto quase não aparece até 3s e já está sorrindo quando aparece (sem pausa antes da fala); o nióbio é prata facetado (não lingote liso nem espelho), sai por baixo do quadro e não cruza o rosto; ele diz só \"a nossa gente.\"; os olhos pousam no terço superior (~45% da largura); luvas limpas. Validar o EPI com a SST da operadora antes do final (P11)."),
              gen("T09-B · cava", G.T09B,
                   "No fundo de uma cava moderna em Araxá: plano aberto rente ao chão, com o funcionário pequeno, de costas, andando até uma escavadeira de porte médio ao longe e dizendo a primeira parte da frase, com o sol baixo atrás da máquina e um flare suave. Corte: médio close do rosto dele, no centro e reto pra lente, na frente da mesma máquina, com a luz do T09-A; ele fala sorrindo, com uma pequena pausa depois de \"nasce,\" e de \"vive,\", enquanto a câmera recua devagar (dolly-out, sem zoom) e o quadro vai abrindo.",
                   "FUNCIONÁRIO, plano 1 (de costas): \"Afinal, o que cresce aqui:\" / plano 2: \"também deve construir novos caminhos para quem nasce, [pausa] vive [pausa] e trabalha aqui.\" Mesma voz e mesma entrega do \"a nossa gente.\", sem V.O.",
                   "de costas, fala e anda — 3s (fala em 0–2s) · rosto centralizado, fala com duas pausas e dolly-out — 6s · segura o sorriso — 1s = 10s",
                   "ele sorrindo pra lente, rosto no centro; corte para o match do T10.",
                   "Corrigido: o movimento é só a câmera recuando (dolly-out), sem zoom, então o rosto encolhe aos poucos e o quadro abre de médio close para médio. As duas falas são dele, com a mesma voz e entrega do \"a nossa gente.\" (sem V.O. no ElevenLabs): a primeira, \"Afinal, o que cresce aqui:\", sai enquanto ele anda de costas no plano baixo (a boca não aparece). Luz: só o plano 1 (ele de costas) é em contraluz, com um flare; o plano 2 usa a mesma luz do T09-A (sol baixo à esquerda). O corte para a mãe cai em \"vive\". Ajustes desta rodada: a máquina ficou menor (entendi \"empilhadeira\" como a máquina do fundo; no prompt segue sendo uma escavadeira, de porte médio, uns 3,5 m) e a fala ganhou as duas pausas que você pediu, fora do texto entre aspas (um bloco PACING), para o modelo não ler \"pausa\" em voz alta. Mantive o \"também deve construir\" no começo. A geração passou de 9s para 10s para caber as pausas.",
                   ["Wide baixíssimo: ele de costas, falando e andando até a máquina (contraluz, flare)", "Médio close (match): rosto centralizado, fala, dolly-out"],
                   "reference-to-video", ["@FUNCIONARIO (character sheet) — identidade + EPI"],
                   "confira: plano 1 com a lente quase no chão, ele de costas e pequeno, a máquina bem longe, um flare só, e a voz dele dizendo \"Afinal, o que cresce aqui:\"; plano 2 com o rosto no centro, a câmera recuando de verdade (sem zoom), as duas pausas depois de \"nasce,\" e \"vive,\" e a mesma luz do T09-A (sol baixo à esquerda), sem flare; mesma voz e entrega nas duas falas; EPI completo. Se a câmera ficar parada ou der zoom, reforce \"the camera moves back, no zoom\".")]),
    dict(id="T10", b="mc", t="Mãe e recém-nascido", d=3.0,
         desc="Médio close da mãe com o bebê no colo, olhando pra câmera e sorrindo, com dolly-out lento.",
         gens=[gen("T10", G.T10,
                   "Num apartamento claro em BH, a mãe, com o recém-nascido no colo, olha pra lente e sorri, enquanto a câmera recua devagar (dolly-out) e o quadro vai abrindo.",
                   "nada na geração. Na montagem: o áudio do funcionário segue por cima.",
                   "olha pra lente, sorrindo, com o bebê no colo, dolly-out — 4s",
                   "segurando seu olhar, sorrindo; corte para o T11.",
                   "Simplificado como você pediu: enquadramento simples com dolly-out, ela olha pra câmera sorrindo com o bebê no colo. Sem o olhar pro bebê e de volta. Agora com character sheet (@MAE). Geração de 4s (mínimo do modelo); na montagem entram ~3s. Sem fala.",
                   ["Médio close (match): ela sorri pra lente com o bebê no colo, dolly-out"],
                   "reference-to-video", ["@MAE (character sheet) — identidade"],
                   "conferir a proporção do bebê (rosto parcialmente coberto), o rosto dela no centro o tempo todo e a câmera recuando sem zoom.")]),
    dict(id="T11", b="mc", t="Mineirão", d=3.0,
         desc="Médio close da torcedora no Mineirão, bem atenta ao jogo, olhando um pouco na direção da câmera, com dolly-out lento.",
         gens=[gen("T11", G.T11,
                   "No Mineirão reformado, a torcedora acompanha o jogo bem atenta, com os olhos na partida, um pouco ao lado da lente, enquanto a câmera recua devagar (dolly-out) e o estádio vai aparecendo atrás.",
                   "nada na geração. Na montagem: o áudio do funcionário segue por cima.",
                   "atenta ao jogo, olhando um pouco ao lado da lente, dolly-out — 4s",
                   "ainda atenta ao jogo; corte para o T12.",
                   "Simplificado: enquadramento simples com dolly-out; ela presta atenção no jogo olhando um pouco na direção da câmera (os olhos ficam ao lado da lente, nunca nela). Cabelo slicked back e camisa de futebol genérica terracota com gola creme. Atenção: a camisa do sheet saiu com um escudo azul e amarelo no peito. O prompt do T11 manda ignorar o emblema, mas o mais seguro é gerar o sheet de novo ou apagar o escudo da imagem antes de anexar. Geração de 4s; na montagem entram ~3s.",
                   ["Médio close (match): atenta ao jogo, olhos ao lado da lente, dolly-out"],
                   "reference-to-video", ["@TORCEDORA (character sheet) — identidade"],
                   "conferir: peito da camisa liso (sem escudo, patrocínio, número ou texto), olhos ao lado da lente (não nela) e a arquibancada desfocada (nada de camisa, bandeira ou cachecol de clube).")]),
    dict(id="T12", b="mc", t="Ônibus", d=6.6,
         desc="O motorista, em médio close com dolly-out, sorri pra você e olha pra baixo pra abrir a porta; o estudante embarca e o motorista explica a rota com o ônibus andando.",
         gens=[gen("T12 + T13", G.T12,
                   "Num ônibus moderno de BH: médio close do motorista, no centro e reto pra lente, com dolly-out lento; ele sorri e, aos 2s, olha pra baixo e abre a porta de vidro; corte para o tênis do estudante entrando; com o ônibus andando, o motorista fala; fecha no estudante na janela, BH passando.",
                   "MOTORISTA: \"Se Minas tem o que o futuro procura, esse futuro também precisa chegar até os mineiros.\" (na montagem, a V.O. \"e trabalha aqui.\" cai no plano 1)",
                   "motorista em médio close, olha pra baixo e abre a porta — 3s · porta e tênis — 3s · fala com o ônibus andando — 5s · estudante na janela — 3s = 14s",
                   "o estudante na janela; corte seco.",
                   "O primeiro plano agora é o match do motorista: médio close centralizado, mesmo dolly-out de ~3s dos outros rostos; nesses 3s ele olha pra baixo e abre a porta. O resto segue (porta e tênis, fala com o ônibus andando, estudante na janela), só que o tênis agora vem depois de a porta abrir. O close final do estudante prepara o T14.",
                   ["Médio close (match): motorista, dolly-out, olha pra baixo e abre a porta", "Close: porta abre, tênis entra", "Médio-aberto: ônibus andando, fala", "Close: estudante na janela"],
                   "reference-to-video", ["@MOTORISTA (character sheet) — identidade", "@ESTUDANTE (character sheet) — identidade"],
                   "risco: o estudante abrir a boca. O ônibus tem que estar andando quando o motorista fala; no plano 1 o rosto do motorista fica no centro e a câmera recua sem zoom.")]),
    dict(id="T14", b="cx", t="Trilhas de Futuro", d=3.8,
         desc="O estudante aperta o borne, a lâmpada acende, ele fala e comemora com a colega.",
         gens=[gen("T14", G.T14,
                   "Na oficina do curso técnico: detalhe do borne apertado, a lâmpada do painel acende, o estudante vira pra lente e fala orgulhoso, e bate um soquinho com a colega.",
                   "ESTUDANTE: \"É para isso que a Codemig existe… para fazer essa conexão acontecer.\"",
                   "borne — 3s · lâmpada acende — 2s · fala — 4s · soquinho — 2s = 11s",
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
                   "olhar na lente — 1s · fala — 8s · sorriso — 2s = 11s",
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
          relay (P1) = the camera travels frame-left → frame-right in every shot;
          match series (P2) = medium close-up, face centred, slow dolly-out (~3s)
LIGHT LOGIC: one dominant motivated natural source per scene with real falloff, always
          on the frame-LEFT side of the faces (low late sun outside, window inside);
          exceptions by request: T08 bright morning, T09-B shot 1 backlight with one flare
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
    ("Falas", "Só o texto da fala, com a janela do tamanho da frase e o corte logo depois. Nenhuma indicação de pausa ou entrega. O sotaque ficou num voice lock curto (R caipira ou R de BH, de P3) e o tom vem da atuação."),
    ("Gramática", "Câmera na mão o tempo todo. Subações antes e depois da fala em close ou detalhe, e a fala no plano mais aberto do take (médio-aberto, do joelho pra cima, com o lugar em volta), com corte seco entre eles. Exceções: o T01, com a fala no close como você pediu, e o T16, o close final."),
    ("Revezamento", "Em todos os planos, inclusive nos closes, a câmera anda de lado da esquerda pra direita e nunca para (no T08 a agricultora anda pra frente e o travelling lateral vira um arco leve em volta dela, tipo orbit). Cada take tem 3 ou 4 subações para a montagem apoiar a locução em off."),
    ("Mundo", "Minas e Brasil modernos: arquitetura contemporânea, equipamento novo, espaços públicos bem cuidados e \"Brazilian\" espalhado pelos prompts. Nada rústico, pobre, velho ou colonial; isso está no template WORLD e na espinha do NEGATIVE."),
    ("Look", "O seu style ref de 35mm color negative, sem o parágrafo de cor e sem \"tactile surfaces\": a cor sai do ambiente de cada cena. A regra de luz é uma fonte natural dominante por cena, sempre do lado esquerdo do quadro."),
]

PEND = [
    ("P1", "Transição do revezamento (T04–T08)", "decidido",
     "Travelling lateral da esquerda pra direita em todos os planos, closes incluídos; a câmera nunca para. Corte seco entre subações e fala. Exceção pedida: T07 plano 1 (zenital, câmera parada). No T08 ela anda pra frente e o travelling lateral continua, com a câmera recuando no passo dela: vira um arco leve, tipo orbit."),
    ("P2", "Match cut (T09-B a T12)", "decidido",
     "Médio close centralizado, reto pra câmera, mesma distância, com dolly-out lento (~3s) em todos: funcionário (T09-B), mãe, torcedora e motorista, que abre o T12. É só a câmera recuando, sem movimento de lente: o quadro abre aos poucos de médio close para médio. O \"olhar que sobe\" do pedido anterior saiu."),
    ("P3", "Sotaque", "decidido",
     "R caipira para interior, campo e mineração; R de BH para a cidade. Agora num voice lock curto, sem direção de entrega."),
    ("P4", "Falas finais do T16", "decidido", "Sem coro; o protagonista fala tudo."),
    ("P5", "Casting e representação", "proposta",
     "Proposta do diretor nos character sheets: pardos, pretos e brancos em proporção próxima à de Minas, sem amarrar ofício a cor. Validar antes de gerar os sheets."),
    ("P6", "Teto de 60 segundos", "a decidir",
     "Com a abertura de 12s (T01-A curto + T01-B de 9s) e o novo bloco T09-B a T12 (cava com fala, match cuts de ~3s cada), o corte estimado fica em ~72s; com o T01-B de 18s, ~81s. O pré-shotlist previa ~9s para a abertura inteira. O revezamento tem takes mais longos que o necessário, de propósito, para cobrir a locução em off: o enxugamento fica para a montagem, mas o teto de 60s precisa de uma decisão sua (onde cortar)."),
    ("P7", "Look (style ref)", "a testar",
     "FILM LOOK v2 a partir do seu ref. Antes de congelar, fazer draft do T01 (exterior com mergulho), do T05 (interior com travelling) e do T09 (virada com match)."),
    ("P9", "Falas do T09-B (sem V.O.)", "decidido",
     "T09-A: ele diz \"a nossa gente.\". T09-B plano 1: ele diz \"Afinal, o que cresce aqui:\" de costas, andando; plano 2: \"também deve construir novos caminhos para quem nasce, [pausa] vive [pausa] e trabalha aqui.\" em cena, com as duas pausas pedidas (no prompt vão num bloco PACING, fora das aspas). Mesma voz e mesma entrega nas três falas, sem V.O. no ElevenLabs nesse trecho. O corte para a mãe cai em \"vive\" e o áudio dele segue por cima dos match cuts."),
    ("P10", "T12 e T13 numa geração", "proposta", "Mesmo lugar e mesmas pessoas; o olhar do motorista emenda a fala."),
    ("P15", "Bloqueios 3D (T01-B)", "confirmar",
     "Os dois bloqueios entram como referência só de movimento. Ajustes pedidos: no de 8,6s, estender o último frame em ~0,4s (fica 9s); no de 19s, cortar ~2s do close inicial e estender o último frame em ~1s (fica 18s). Se der, exportar sem os textos de marcação e em 21:9."),
    ("P16", "Locações", "decidido",
     "Nenhuma plate será gerada por enquanto; todos os takes saem de text-to-video para o lugar. Os prompts de locação ficam de reserva."),
    ("P18", "Falas apertadas em todos os takes", "decidido",
     "A janela de cada fala tem o tamanho da frase (cerca de 3 palavras por segundo) e começa junto com o plano em que ele fala; o corte seguinte vem logo depois. O T15 ganhou tempo (a frase longa estava apertada, 5s para 23 palavras); os outros encolheram 1 a 3s."),
    ("P19", "Sem efeitos sonoros no T01-B", "decidido",
     "Só vento forte sob a fala do jovem (que fala alto por cima dele), que some quando a câmera afunda. Da sala em diante, só o som natural: o ventilador ligado e um murmúrio leve dos alunos. Nada de whoosh, rumble ou chiado na descida."),
    ("P20", "Os 5s antes dos match cuts", "decidido",
     "Resolvidos pelo T09-B (a direção é sua): plano 1, wide baixíssimo dele de costas andando até a máquina, contra o sol e com flare, falando \"Afinal, o que cresce aqui:\"; plano 2, médio close dele com a fala e o dolly-out."),
    ("P21", "Sheets da mãe, da torcedora e do funcionário", "ok, com um alerta",
     "@MAE e @TORCEDORA gerados; o @FUNCIONARIO foi atualizado sem os protetores auriculares (descritor e prompt do sheet ajustados). Alerta: a camisa da torcedora saiu com um escudo azul e amarelo no peito. O prompt do T11 manda ignorar o emblema, mas o ideal é gerar o sheet de novo (o prompt agora pede o peito liso) ou apagar o escudo da imagem antes de anexar. Também saiu com jeans marrom-escuro, não índigo; o descritor segue o sheet."),
    ("P22", "Exceções de look no T09-B", "decidido",
     "Só o plano 1 (ele de costas) é diferente: contraluz, com o sol baixo atrás da máquina, e UM flare. O plano 2 usa a mesma luz do T09-A (sol baixo à esquerda), sem flare. O resto do filme segue sem flares e com o sol à esquerda."),
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
    ("Mineirão (T11)", "nada de preto e branco, azul e branco, verde e branco ou verde-amarelo; a torcedora veste uma camisa de futebol genérica terracota com gola creme, sem escudo, patrocínio, número ou texto, e a torcida não veste camisa de clube."),
    ("Marcas reais", "carro, ônibus, mina, escola, programa e hospital saem sem marca e sem texto legível. Logos entram na pós."),
    ("Mineração (T09)", "EPI completo é trava crítica; falta validar com a SST (P11)."),
    ("Dolly-out (match)", "o modelo pode deixar a câmera parada ou dar um zoom em vez de recuar. No draft, confira se a câmera recua de verdade (o rosto encolhe aos poucos e o fundo abre); reforce \"the camera moves back, no zoom\" se precisar."),
    ("Flare do T09-B", "um só, no plano 1. Se aparecer flare no plano 2, ou bolhas de bokeh, regenerar; o plano 2 tem que repetir a luz do T09-A."),
    ("Escudo na camisa da torcedora", "o sheet da @TORCEDORA veio com um escudo azul e amarelo no peito, que lembra seleção ou clube. Gere o sheet de novo com o peito liso ou apague o escudo; no T11 confira que o peito sai liso."),
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
        ("LIGHT · exterior de dia (T08)", T.LIGHT_EXT_DAY),
        ("LIGHT · contraluz (T09-B, só o plano 1)", T.LIGHT_EXT_BACK),
        ("FILM LOOK com um flare (T09-B, plano 1)", T.FILM_LOOK_FLARE),
        ("LIGHT · interiores (base)", T.light_int("[window]", "[practicals]", "[reach]")),
        ("CAMERA · na mão", T.handheld()),
        ("CAMERA · revezamento", T.REV_CAMERA),
        ("MATCH FRAME (série T09-B a T12)", T.MATCH_FRAME),
        ("CAMERA · dolly-out", T.dolly_out(3)),
        ("Quadro do T09-A (nióbio)", T.NIOBIUM_FRAME),
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
