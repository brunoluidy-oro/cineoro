# Prompts de assets (GPT): sheets de produto, uma visão por imagem

Gerado por `build.py` a partir de `assets_prompts.py`. Edite lá, não aqui.

Como usar: uma imagem por vez, formato horizontal; gere primeiro a visão 3/4 de cada objeto; depois de aprovada, anexe-a como referência nas outras visões e mantenha o MASTER igual.

## Bandeja real (Morango) (`@BANDEJA`)

**Anexar:** Anexe 200142_0.png (bandeja Morango) como referência exata. Para outro sabor, anexe 200140_0.png (Coco) ou 200141_0.png (Salada de Frutas) e troque a palavra do sabor no MASTER.

> Só há prompts das duas visões que a referência prova. Topo e lado não entram: a imagem não mostra o arranjo dos potes nem a altura, e o GPT inventaria essas geometrias. Elas dependem da foto real da bandeja.

### Visão: 3/4 herói

```
Create a product reference image, ONE single view only (no collage, no multiple panels, no insets, no turnaround), 16:9, one object, centred, on a neutral flat medium-grey seamless studio background.

VIEW: THREE-QUARTER HERO: seen from the front-left and slightly above, at the same angle as the attached reference, cleanly cut out on the grey background, no blue halo or edge fringe.

OBJECT: a six-pot yogurt multipack tray, 540 g net (6 x 90 g), strawberry flavour: six identical pale-pink opaque plastic pots joined into one connected block, wrapped in a single printed sleeve label whose upper edge is scalloped, following the rounded tops of the pots. SLEEVE (copy the attached reference exactly): leaf-green background with a soft darker-to-lighter gradient; a centred white shield-shaped badge with a green outline carrying the brand name 'Laticínios Porto Alegre' and a small golden bell under the name; below the badge the flavour word 'MORANGO' in bold white capitals; glossy strawberry photographs with water droplets on both sides (whole, halved, with green leaves); a stylised light-green countryside strip near the bottom with a tractor, cows, a tree and a motorbike rider; a barcode and 'Peso Líq. 540 g' at the lower left; a small square green stamp at the upper right; a small 'PUXE' tab at the upper left; all fine print rendered as unreadable micro-texture, never as new readable words.

IDENTITY LOCK: the object must be identical to the attached reference image in shape, proportions, colours and printed graphics. Do not redesign, simplify, add or remove anything, and do not change the number of pots.

Soft even studio lighting from the front-left, consistent, no harsh shadows, no coloured light, a faint soft contact shadow under the object. Tack-sharp focus over the whole object, deep depth of field. Photorealistic studio product photograph, NOT a render, NOT a cartoon.

NO collage, NO extra objects, NO hands, NO background environment, NO watermark, NO captions or labels outside the object. Clean reference image only.

--- NEGATIVE ---
different number of pots, altered or redrawn logo, new invented words, readable fake text, changed colours, blue halo or edge fringe, glossy CGI packshot look, harsh reflections, hands, extra objects, collage, watermark
```

### Visão: frente reta

```
Create a product reference image, ONE single view only (no collage, no multiple panels, no insets, no turnaround), 16:9, one object, centred, on a neutral flat medium-grey seamless studio background.

VIEW: FRONT, FLAT: the sleeve seen perfectly straight-on from the front, orthographic, no perspective, every printed graphic laid out exactly as on the reference.

OBJECT: a six-pot yogurt multipack tray, 540 g net (6 x 90 g), strawberry flavour: six identical pale-pink opaque plastic pots joined into one connected block, wrapped in a single printed sleeve label whose upper edge is scalloped, following the rounded tops of the pots. SLEEVE (copy the attached reference exactly): leaf-green background with a soft darker-to-lighter gradient; a centred white shield-shaped badge with a green outline carrying the brand name 'Laticínios Porto Alegre' and a small golden bell under the name; below the badge the flavour word 'MORANGO' in bold white capitals; glossy strawberry photographs with water droplets on both sides (whole, halved, with green leaves); a stylised light-green countryside strip near the bottom with a tractor, cows, a tree and a motorbike rider; a barcode and 'Peso Líq. 540 g' at the lower left; a small square green stamp at the upper right; a small 'PUXE' tab at the upper left; all fine print rendered as unreadable micro-texture, never as new readable words.

IDENTITY LOCK: the object must be identical to the attached reference image in shape, proportions, colours and printed graphics. Do not redesign, simplify, add or remove anything, and do not change the number of pots.

Soft even studio lighting from the front-left, consistent, no harsh shadows, no coloured light, a faint soft contact shadow under the object. Tack-sharp focus over the whole object, deep depth of field. Photorealistic studio product photograph, NOT a render, NOT a cartoon.

NO collage, NO extra objects, NO hands, NO background environment, NO watermark, NO captions or labels outside the object. Clean reference image only.

--- NEGATIVE ---
different number of pots, altered or redrawn logo, new invented words, readable fake text, changed colours, blue halo or edge fringe, glossy CGI packshot look, harsh reflections, hands, extra objects, collage, watermark
```

## Pote real (stand-in) (`@POTE`)

**Anexar:** Anexe 200142_0.png (bandeja Morango) e, depois de aprovada, a imagem 3/4 herói da bandeja gerada acima.

> Stand-in para o primeiro draft. A tampa e o ponto onde o pote solta da bandeja não aparecem em nenhuma referência, então a linha LID é suposição minha. Troque pela foto real do pote assim que ela chegar.

### Visão: fechado 3/4

```
Create a product reference image, ONE single view only (no collage, no multiple panels, no insets, no turnaround), 16:9, one object, centred, on a neutral flat medium-grey seamless studio background.

VIEW: CLOSED, THREE-QUARTER: seen from the front-left and slightly above, lid on and sealed, resting on the grey surface.

OBJECT: a single 90 g yogurt pot taken from the multipack: an opaque pale-pink plastic cup, slightly tapered with a rounded rim, its outer surface carrying the same leaf-green printed sleeve section as the attached tray reference (one 'MORANGO 90 g' line, strawberry photography and the white shield-shaped badge, cropped as it would be on one pot); [LID, ASSUMPTION, REPLACE WITH THE REAL LID: a flat pale foil-type lid sealed over the rim, with a small pull tab at one edge]; on one side of the cup a small stub where the thin plastic bridge to its neighbour snapped off.

IDENTITY LOCK: the object must be identical to the attached reference image in shape, proportions, colours and printed graphics. Do not redesign, simplify, add or remove anything, and do not change the pot's proportions.

Soft even studio lighting from the front-left, consistent, no harsh shadows, no coloured light, a faint soft contact shadow under the object. Tack-sharp focus over the whole object, deep depth of field. Photorealistic studio product photograph, NOT a render, NOT a cartoon.

NO collage, NO extra objects, NO hands, NO background environment, NO watermark, NO captions or labels outside the object. Clean reference image only.

--- NEGATIVE ---
different number of pots, altered or redrawn logo, new invented words, readable fake text, changed colours, blue halo or edge fringe, glossy CGI packshot look, harsh reflections, hands, extra objects, collage, watermark, more than one pot
```

### Visão: aberto

```
Create a product reference image, ONE single view only (no collage, no multiple panels, no insets, no turnaround), 16:9, one object, centred, on a neutral flat medium-grey seamless studio background.

VIEW: OPEN: the lid peeled off and lying beside the cup, tilted against it so its underside faces the camera with a thin glossy film of yogurt on it; the cup open showing smooth glossy pale-pink strawberry yogurt; seen from the front-left and slightly above.

OBJECT: a single 90 g yogurt pot taken from the multipack: an opaque pale-pink plastic cup, slightly tapered with a rounded rim, its outer surface carrying the same leaf-green printed sleeve section as the attached tray reference (one 'MORANGO 90 g' line, strawberry photography and the white shield-shaped badge, cropped as it would be on one pot); [LID, ASSUMPTION, REPLACE WITH THE REAL LID: a flat pale foil-type lid sealed over the rim, with a small pull tab at one edge]; on one side of the cup a small stub where the thin plastic bridge to its neighbour snapped off.

IDENTITY LOCK: the object must be identical to the attached reference image in shape, proportions, colours and printed graphics. Do not redesign, simplify, add or remove anything, and do not change the pot's proportions.

Soft even studio lighting from the front-left, consistent, no harsh shadows, no coloured light, a faint soft contact shadow under the object. Tack-sharp focus over the whole object, deep depth of field. Photorealistic studio product photograph, NOT a render, NOT a cartoon.

NO collage, NO extra objects, NO hands, NO background environment, NO watermark, NO captions or labels outside the object. Clean reference image only.

--- NEGATIVE ---
different number of pots, altered or redrawn logo, new invented words, readable fake text, changed colours, blue halo or edge fringe, glossy CGI packshot look, harsh reflections, hands, extra objects, collage, watermark, more than one pot
```

## Bandeja toon (fosca) (`@BANDEJA_TOON`)

**Anexar:** Anexe (1) 200142_0.png, só para estrutura e papéis de cor; (2) a model sheet da vaca fosca, só para o material.

> Sem texto, sem número, sem código de barras: o logo e as letras entram em pós. Gere a visão 3/4 primeiro; depois de aprovada, anexe-a nas outras e mantenha o MASTER igual.

### Visão: 3/4 herói

```
Create a product reference image, ONE single view only (no collage, no multiple panels, no insets, no turnaround), 16:9, one object, centred, on a neutral flat medium-grey seamless studio background.

VIEW: THREE-QUARTER HERO: seen from the front-left and slightly above, the whole tray in frame.

OBJECT: a six-pot yogurt multipack tray in the same matte designer-toy material language as the attached cow character (smooth matte soft-touch vinyl, rounded bevels on every edge, no gloss, no fur, no texture noise): six identical rounded pale-pink pots joined into one block with the same arrangement, proportions and scalloped sleeve outline as the attached tray reference, each pot closed with a thin matte cream lid; the sleeve is a matte leaf-green band with a white shield-shaped badge in the centre carrying only a simple golden bell icon (NO letters), large simplified strawberry shapes on both sides in flat matte red with tiny yellow seed dots and green leaves (no water droplets, no photography), and a lighter-green rolling-hills strip along the bottom with two tiny black-and-white cow silhouettes and a tiny red tractor; NO text, NO numerals, NO barcode, NO fine print.

IDENTITY LOCK: the object keeps the exact structure of the real product described above and in the attached tray reference (pot count, outline, colour roles), redrawn in the matte designer-toy material language of the attached cow character. Nothing is added: no text, no numerals, no extra graphics.

Soft even studio lighting from the front-left, consistent, no harsh shadows, no coloured light, a faint soft contact shadow under the object. Tack-sharp focus over the whole object, deep depth of field. Stylized 3D render, matte soft-touch designer-toy look, premium animated-film quality, soft global illumination, NOT a photograph, NOT glossy.

NO collage, NO extra objects, NO hands, NO background environment, NO watermark, NO captions or labels outside the object. Clean reference image only.

--- NEGATIVE ---
glossy candy shine, chrome, translucent jelly, fur or fuzz, ink outlines, flat 2D look, readable letters or numerals, barcode, fine print, photographic fruit, water droplets, hard shadows, extra pots, extra objects, hands, text overlays, watermark
```

### Visão: frente reta

```
Create a product reference image, ONE single view only (no collage, no multiple panels, no insets, no turnaround), 16:9, one object, centred, on a neutral flat medium-grey seamless studio background.

VIEW: FRONT, FLAT: the sleeve seen perfectly straight-on from the front, orthographic, no perspective.

OBJECT: a six-pot yogurt multipack tray in the same matte designer-toy material language as the attached cow character (smooth matte soft-touch vinyl, rounded bevels on every edge, no gloss, no fur, no texture noise): six identical rounded pale-pink pots joined into one block with the same arrangement, proportions and scalloped sleeve outline as the attached tray reference, each pot closed with a thin matte cream lid; the sleeve is a matte leaf-green band with a white shield-shaped badge in the centre carrying only a simple golden bell icon (NO letters), large simplified strawberry shapes on both sides in flat matte red with tiny yellow seed dots and green leaves (no water droplets, no photography), and a lighter-green rolling-hills strip along the bottom with two tiny black-and-white cow silhouettes and a tiny red tractor; NO text, NO numerals, NO barcode, NO fine print.

IDENTITY LOCK: the object keeps the exact structure of the real product described above and in the attached tray reference (pot count, outline, colour roles), redrawn in the matte designer-toy material language of the attached cow character. Nothing is added: no text, no numerals, no extra graphics.

Soft even studio lighting from the front-left, consistent, no harsh shadows, no coloured light, a faint soft contact shadow under the object. Tack-sharp focus over the whole object, deep depth of field. Stylized 3D render, matte soft-touch designer-toy look, premium animated-film quality, soft global illumination, NOT a photograph, NOT glossy.

NO collage, NO extra objects, NO hands, NO background environment, NO watermark, NO captions or labels outside the object. Clean reference image only.

--- NEGATIVE ---
glossy candy shine, chrome, translucent jelly, fur or fuzz, ink outlines, flat 2D look, readable letters or numerals, barcode, fine print, photographic fruit, water droplets, hard shadows, extra pots, extra objects, hands, text overlays, watermark
```

### Visão: topo

```
Create a product reference image, ONE single view only (no collage, no multiple panels, no insets, no turnaround), 16:9, one object, centred, on a neutral flat medium-grey seamless studio background.

VIEW: TOP-DOWN: seen from directly above, showing the six cream lids and the outline of the block.

OBJECT: a six-pot yogurt multipack tray in the same matte designer-toy material language as the attached cow character (smooth matte soft-touch vinyl, rounded bevels on every edge, no gloss, no fur, no texture noise): six identical rounded pale-pink pots joined into one block with the same arrangement, proportions and scalloped sleeve outline as the attached tray reference, each pot closed with a thin matte cream lid; the sleeve is a matte leaf-green band with a white shield-shaped badge in the centre carrying only a simple golden bell icon (NO letters), large simplified strawberry shapes on both sides in flat matte red with tiny yellow seed dots and green leaves (no water droplets, no photography), and a lighter-green rolling-hills strip along the bottom with two tiny black-and-white cow silhouettes and a tiny red tractor; NO text, NO numerals, NO barcode, NO fine print.

IDENTITY LOCK: the object keeps the exact structure of the real product described above and in the attached tray reference (pot count, outline, colour roles), redrawn in the matte designer-toy material language of the attached cow character. Nothing is added: no text, no numerals, no extra graphics.

Soft even studio lighting from the front-left, consistent, no harsh shadows, no coloured light, a faint soft contact shadow under the object. Tack-sharp focus over the whole object, deep depth of field. Stylized 3D render, matte soft-touch designer-toy look, premium animated-film quality, soft global illumination, NOT a photograph, NOT glossy.

NO collage, NO extra objects, NO hands, NO background environment, NO watermark, NO captions or labels outside the object. Clean reference image only.

--- NEGATIVE ---
glossy candy shine, chrome, translucent jelly, fur or fuzz, ink outlines, flat 2D look, readable letters or numerals, barcode, fine print, photographic fruit, water droplets, hard shadows, extra pots, extra objects, hands, text overlays, watermark
```

## Pote toon (fosco) (`@POTE_TOON`)

**Anexar:** Anexe a imagem 3/4 herói da bandeja toon aprovada e a model sheet da vaca fosca.

> A visão da tampa de frente serve ao Setor Tampinha e ao plano do prêmio: o centro fica liso de propósito, porque a mensagem é escrita em pós.

### Visão: fechado 3/4

```
Create a product reference image, ONE single view only (no collage, no multiple panels, no insets, no turnaround), 16:9, one object, centred, on a neutral flat medium-grey seamless studio background.

VIEW: CLOSED, THREE-QUARTER: seen from the front-left and slightly above, lid on, resting on the grey surface.

OBJECT: a single yogurt pot in the same matte designer-toy material language as the attached cow character (smooth matte soft-touch vinyl, rounded bevels, no gloss): a chubby pale-pink cup, slightly wider at the rim than at the base, with a thin leaf-green sleeve band carrying the white shield-shaped badge with only a simple golden bell icon (NO letters) and one simplified flat strawberry; a thin flat matte cream lid with a small round pull tab; the pot is friendly and rounded, matching the pots of the attached tray.

IDENTITY LOCK: the object keeps the exact structure of the real product described above and in the attached tray reference (pot count, outline, colour roles), redrawn in the matte designer-toy material language of the attached cow character. Nothing is added: no text, no numerals, no extra graphics.

Soft even studio lighting from the front-left, consistent, no harsh shadows, no coloured light, a faint soft contact shadow under the object. Tack-sharp focus over the whole object, deep depth of field. Stylized 3D render, matte soft-touch designer-toy look, premium animated-film quality, soft global illumination, NOT a photograph, NOT glossy.

NO collage, NO extra objects, NO hands, NO background environment, NO watermark, NO captions or labels outside the object. Clean reference image only.

--- NEGATIVE ---
glossy candy shine, chrome, translucent jelly, fur or fuzz, ink outlines, flat 2D look, readable letters or numerals, barcode, fine print, photographic fruit, water droplets, hard shadows, extra pots, extra objects, hands, text overlays, watermark, more than one pot
```

### Visão: aberto

```
Create a product reference image, ONE single view only (no collage, no multiple panels, no insets, no turnaround), 16:9, one object, centred, on a neutral flat medium-grey seamless studio background.

VIEW: OPEN: the lid lying beside the cup, tilted against it so its underside faces the camera, with a soft thin film of cream on it; the cup open showing smooth matte pale-pink yogurt; seen from the front-left and slightly above.

OBJECT: a single yogurt pot in the same matte designer-toy material language as the attached cow character (smooth matte soft-touch vinyl, rounded bevels, no gloss): a chubby pale-pink cup, slightly wider at the rim than at the base, with a thin leaf-green sleeve band carrying the white shield-shaped badge with only a simple golden bell icon (NO letters) and one simplified flat strawberry; a thin flat matte cream lid with a small round pull tab; the pot is friendly and rounded, matching the pots of the attached tray.

IDENTITY LOCK: the object keeps the exact structure of the real product described above and in the attached tray reference (pot count, outline, colour roles), redrawn in the matte designer-toy material language of the attached cow character. Nothing is added: no text, no numerals, no extra graphics.

Soft even studio lighting from the front-left, consistent, no harsh shadows, no coloured light, a faint soft contact shadow under the object. Tack-sharp focus over the whole object, deep depth of field. Stylized 3D render, matte soft-touch designer-toy look, premium animated-film quality, soft global illumination, NOT a photograph, NOT glossy.

NO collage, NO extra objects, NO hands, NO background environment, NO watermark, NO captions or labels outside the object. Clean reference image only.

--- NEGATIVE ---
glossy candy shine, chrome, translucent jelly, fur or fuzz, ink outlines, flat 2D look, readable letters or numerals, barcode, fine print, photographic fruit, water droplets, hard shadows, extra pots, extra objects, hands, text overlays, watermark, more than one pot
```

### Visão: tampa de frente

```
Create a product reference image, ONE single view only (no collage, no multiple panels, no insets, no turnaround), 16:9, one object, centred, on a neutral flat medium-grey seamless studio background.

VIEW: LID, FACE-ON: only the lid, seen perfectly straight-on from above, its underside facing the camera: a flat round matte cream disc with a thin raised rim and the small pull tab at the top edge; a thin ring of soft cream film along the rim only; the centre 60% of the disc is completely plain and smooth, with no marks, no drawing and no letters.

OBJECT: a single yogurt pot in the same matte designer-toy material language as the attached cow character (smooth matte soft-touch vinyl, rounded bevels, no gloss): a chubby pale-pink cup, slightly wider at the rim than at the base, with a thin leaf-green sleeve band carrying the white shield-shaped badge with only a simple golden bell icon (NO letters) and one simplified flat strawberry; a thin flat matte cream lid with a small round pull tab; the pot is friendly and rounded, matching the pots of the attached tray.

IDENTITY LOCK: the object keeps the exact structure of the real product described above and in the attached tray reference (pot count, outline, colour roles), redrawn in the matte designer-toy material language of the attached cow character. Nothing is added: no text, no numerals, no extra graphics.

Soft even studio lighting from the front-left, consistent, no harsh shadows, no coloured light, a faint soft contact shadow under the object. Tack-sharp focus over the whole object, deep depth of field. Stylized 3D render, matte soft-touch designer-toy look, premium animated-film quality, soft global illumination, NOT a photograph, NOT glossy.

NO collage, NO extra objects, NO hands, NO background environment, NO watermark, NO captions or labels outside the object. Clean reference image only.

--- NEGATIVE ---
glossy candy shine, chrome, translucent jelly, fur or fuzz, ink outlines, flat 2D look, readable letters or numerals, barcode, fine print, photographic fruit, water droplets, hard shadows, extra pots, extra objects, hands, text overlays, watermark, more than one pot
```
