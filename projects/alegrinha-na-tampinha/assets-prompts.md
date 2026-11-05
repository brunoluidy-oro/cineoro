# Prompts de assets (GPT): pote real e objetos toon

Gerado por `build.py` a partir de `assets_prompts.py`. Edite lá, não aqui.

Como usar: uma imagem por vez; anexe o que a nota pede; depois de aprovada, anexe a imagem aprovada nas seguintes.

## Pote real (stand-in) (`@POTE`)

**Anexar:** Anexe a bandeja Morango (a de 1920×1080).

> Já gerado pelo diretor (Element prop_pote-morango-real). Fica aqui como registro. A tampa está descrita em palavras: película verde impressa, quadrada de cantos arredondados, com aba.

### Visão: painel: fechado à esquerda, aberto à direita

```
A 16:9 image split into two equal panels by a thin vertical line, same plain medium-grey background and soft studio light in both. LEFT: one single yogurt pot with its lid closed. RIGHT: the same pot opened, the lid resting against the cup beside it, smooth pink yogurt visible inside. Three-quarter view from above in both. The cup is pink, rounded-square, with vertical ribs and a thin white rim. The lid is a flat rounded-square film printed in green, with a white shield logo with a small gold bell, the word MORANGO, a strawberry picture and a small pull tab at one corner. Use the attached tray for the exact colors and lid print. Photorealistic. One pot per panel: no tray, no hands, no other text.
```

## Alegrinha: 4 looks e expressões (`@ALEGRINHA_LOOKS`)

**Anexar:** Anexe a model sheet da vaca fosca.

> Um painel com os 4 looks vale como uma referência só no vídeo (mais estável do que quatro referências separadas). O painel de expressões inclui a boca vermelha, que no chaveiro é um pedacinho da boca dela.

### Visão: 4 looks lado a lado

```
Using the attached cow as reference, show the same cow four times side by side in one 16:9 image, full body, front view, same scale, same matte vinyl style, plain medium-grey background, soft studio light. Four work outfits, left to right: 1) a white hairnet with the horns poking through, white rubber boots, a pale-green apron; 2) a white lab coat with a blank ID badge, white rubber boots; 3) big over-ear headphones; 4) a cream painter's smock with a small beret between the horns. Keep her exact face, ears, bell and colors. Happy, relaxed smile in all four.
```

### Visão: expressões felizes

```
Using the attached cow as reference, a 16:9 image split into four equal panels, close-up of her head and shoulders in each, same matte vinyl style, plain medium-grey background, soft studio light. Always happy, never sad or angry: 1) calm smile; 2) big open smile showing her red mouth; 3) happy eyes closed with pleasure; 4) focused and content, working. Same face, ears and colors in every panel.
```

## Bandeja toon (fosca) (`@BANDEJA_TOON`)

**Anexar:** Anexe a bandeja Morango e a model sheet da vaca fosca.

> Sem texto, sem número, sem código de barras: o logo e as letras entram em pós.

### Visão: 3/4

```
Redraw the attached tray as a 3D toy object in the same matte style as the attached cow: smooth matte vinyl, rounded edges, no gloss. Same shape and same angle, six pink ribbed cups, each with its green lid, simplified: a white shield with a small gold bell, big flat strawberry shapes, no text, no numbers, no barcode. Plain medium-grey background, soft studio light.
```

## Pote toon (fosco) (`@POTE_TOON`)

**Anexar:** Anexe a bandeja toon aprovada e a model sheet da vaca fosca. Para a tampa de frente, anexe o painel do pote aprovado.

> A tampa de frente é opcional: serve ao Setor Tampinha e à cena do prêmio. O centro fica liso de propósito, porque a mensagem é escrita em pós.

### Visão: painel: fechado à esquerda, aberto à direita

```
A 16:9 image split into two equal panels by a thin vertical line, same plain medium-grey background and soft studio light in both. LEFT: one single yogurt pot with its lid closed. RIGHT: the same pot opened, the lid resting against the cup beside it, soft pink yogurt inside. Three-quarter view from above in both. Make it a 3D toy object in the same matte style as the attached cow: smooth matte vinyl, rounded edges, no gloss. Pink ribbed cup with a thin white rim; the lid is a flat rounded-square green film with a white shield, a small gold bell, one flat strawberry and a small pull tab; no text.
```

### Visão: tampa de frente (opcional)

```
Only the lid of the attached toy pot, seen straight from above with its underside facing the camera: a flat rounded-square matte cream shape with a thin ring of pink yogurt along the edge and a small pull tab at one corner. The center is completely smooth and empty. Plain medium-grey background, soft studio light.
```
