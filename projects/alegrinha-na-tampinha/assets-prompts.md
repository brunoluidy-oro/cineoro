# Prompts de assets (GPT): pote real e objetos toon

Gerado por `build.py` a partir de `assets_prompts.py`. Edite lá, não aqui.

Como usar: uma imagem por vez; anexe o que a nota pede; depois de aprovada, anexe a imagem aprovada nas seguintes.

## Pote real (stand-in) (`@POTE`)

**Anexar:** Anexe a bandeja Morango (a de 1920×1080).

> A tampa está descrita em palavras, a partir do que você explicou: película verde impressa, quadrada de cantos arredondados, com aba. Se o recorte ou a aba reais forem diferentes, ajuste só a frase da tampa.

### Visão: painel: fechado à esquerda, aberto à direita

```
A 16:9 image split into two equal panels by a thin vertical line, same plain medium-grey background and soft studio light in both. LEFT: one single yogurt pot with its lid closed. RIGHT: the same pot opened, the lid resting against the cup beside it, smooth pink yogurt visible inside. Three-quarter view from above in both. The cup is pink, rounded-square, with vertical ribs and a thin white rim. The lid is a flat rounded-square film printed in green, with a white shield logo with a small gold bell, the word MORANGO, a strawberry picture and a small pull tab at one corner. Use the attached tray for the exact colors and lid print. Photorealistic. One pot per panel: no tray, no hands, no other text.
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
