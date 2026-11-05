"""Prompts de imagem (GPT) para os assets de produto. Curtos, em linguagem corrida.

Cada objeto tem uma lista de (rótulo, prompt). Os potes saem em UM painel dividido 16:9: fechado à
esquerda, aberto com a tampa por perto à direita. Os prompts ficam em inglês; as notas, em português.
A bandeja real já existe (render 1920x1080 enviado), então não há prompt dela.

Fato do produto (explicado pelo diretor): o verde que cobre a bandeja é a TAMPA, uma película impressa
com aba "PUXE", sobre copos rosa ribados com borda branca. A tampa é quadrada de cantos arredondados.
"""

SPLIT = (
    "A 16:9 image split into two equal panels by a thin vertical line, same plain medium-grey background and "
    "soft studio light in both. LEFT: one single yogurt pot with its lid closed. RIGHT: the same pot opened, "
    "the lid resting against the cup beside it, {yogurt} inside. Three-quarter view from above in both."
)

OBJECTS = [
    {
        "id": "pote-real",
        "title": "Pote real (stand-in)",
        "kind": "real",
        "tag": "@POTE",
        "attach": "Anexe a bandeja Morango (a de 1920×1080).",
        "note": "Já gerado pelo diretor (Element prop_pote-morango-real). Fica aqui como registro. A tampa está descrita em palavras: película verde impressa, quadrada de cantos arredondados, com aba.",
        "prompts": [
            ("painel: fechado à esquerda, aberto à direita",
             SPLIT.format(yogurt="smooth pink yogurt visible")
             + " The cup is pink, rounded-square, with vertical ribs and a thin white rim. The lid is a flat rounded-square film printed in green, with a white shield logo with a small gold bell, the word MORANGO, a strawberry picture and a small pull tab at one corner. Use the attached tray for the exact colors and lid print. Photorealistic. One pot per panel: no tray, no hands, no other text."),
        ],
    },
    {
        "id": "bandeja-toon",
        "title": "Bandeja toon (fosca)",
        "kind": "toon",
        "tag": "@BANDEJA_TOON",
        "attach": "Anexe a bandeja Morango e a model sheet da vaca fosca.",
        "note": "Sem texto, sem número, sem código de barras: o logo e as letras entram em pós.",
        "prompts": [
            ("3/4",
             "Redraw the attached tray as a 3D toy object in the same matte style as the attached cow: smooth matte vinyl, rounded edges, no gloss. Same shape and same angle, six pink ribbed cups, each with its green lid, simplified: a white shield with a small gold bell, big flat strawberry shapes, no text, no numbers, no barcode. Plain medium-grey background, soft studio light."),
        ],
    },
    {
        "id": "pote-toon",
        "title": "Pote toon (fosco)",
        "kind": "toon",
        "tag": "@POTE_TOON",
        "attach": "Anexe a bandeja toon aprovada e a model sheet da vaca fosca. Para a tampa de frente, anexe o painel do pote aprovado.",
        "note": "A tampa de frente é opcional: serve ao Setor Tampinha e à cena do prêmio. O centro fica liso de propósito, porque a mensagem é escrita em pós.",
        "prompts": [
            ("painel: fechado à esquerda, aberto à direita",
             SPLIT.format(yogurt="soft pink yogurt")
             + " Make it a 3D toy object in the same matte style as the attached cow: smooth matte vinyl, rounded edges, no gloss. Pink ribbed cup with a thin white rim; the lid is a flat rounded-square green film with a white shield, a small gold bell, one flat strawberry and a small pull tab; no text."),
            ("tampa de frente (opcional)",
             "Only the lid of the attached toy pot, seen straight from above with its underside facing the camera: a flat rounded-square matte cream shape with a thin ring of pink yogurt along the edge and a small pull tab at one corner. The center is completely smooth and empty. Plain medium-grey background, soft studio light."),
        ],
    },
]
