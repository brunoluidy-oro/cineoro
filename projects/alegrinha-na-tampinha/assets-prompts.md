# Prompts de assets (GPT): sheets de produto, uma visão por imagem

Gerado por `build.py` a partir de `assets_prompts.py`. Edite lá, não aqui.

Como usar: uma imagem por vez; anexe o que a nota pede; depois de aprovada, anexe a imagem nas visões seguintes.

## Pote real (stand-in) (`@POTE`)

**Anexar:** Anexe a bandeja Morango (a de 1920×1080). Na visão aberta, anexe também o pote fechado aprovado.

> A tampa não aparece em nenhuma imagem da bandeja, então o GPT vai inventá-la. Use como stand-in até chegar a foto do pote real, e confira se a tampa bate com a verdadeira.

### Visão: fechado

```
Using the attached tray as reference, create ONE single yogurt pot taken from it, with its lid closed. Same pale-pink cup, same green label with the white shield and gold bell, scaled to one pot. Three-quarter view, centered, plain medium-grey background, soft studio light. Photorealistic. One pot only: no tray, no hands, no new text.
```

### Visão: aberto

```
The same pot as the attached image, now with the lid peeled off and resting beside the cup, yogurt visible inside. Same view, background and light. Photorealistic.
```

## Bandeja toon (fosca) (`@BANDEJA_TOON`)

**Anexar:** Anexe a bandeja Morango e a model sheet da vaca fosca.

> Sem texto, sem número, sem código de barras: o logo e as letras entram em pós.

### Visão: 3/4

```
Redraw the attached tray as a 3D toy object in the same matte toy style as the attached cow: smooth matte vinyl, rounded edges, no gloss. Same shape and same six pots, same green label layout, but simplified: a white shield with a small gold bell, big flat strawberry shapes, no text, no numbers, no barcode. Three-quarter view, centered, plain medium-grey background, soft studio light.
```

## Pote toon (fosco) (`@POTE_TOON`)

**Anexar:** Anexe a bandeja toon aprovada e a model sheet da vaca fosca. Nas visões seguintes, anexe o pote fechado aprovado.

> A tampa de frente serve ao Setor Tampinha e à cena do prêmio: o centro fica liso de propósito, porque a mensagem é escrita em pós.

### Visão: fechado

```
ONE single yogurt pot taken from the attached toy tray, with its lid closed, in the same matte toy style as the attached cow: smooth matte vinyl, rounded edges, no gloss. Pale-pink cup, green label band with a white shield and a small gold bell, one flat strawberry, no text. Three-quarter view, centered, plain medium-grey background, soft studio light.
```

### Visão: aberto

```
The same pot as the attached image, lid open and resting beside the cup, soft cream yogurt inside. Same view, background and light.
```

### Visão: tampa de frente

```
Only the lid of the attached pot, seen straight from above, underside facing the camera: a flat round matte cream disc with a thin ring of cream along the rim and a small pull tab. The center of the disc is completely smooth and empty. Plain medium-grey background, soft studio light.
```
