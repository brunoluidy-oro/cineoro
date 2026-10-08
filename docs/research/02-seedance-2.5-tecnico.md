# Seedance 2.5 — brief técnico (pesquisa em 2026-10-08)

Relatório produzido por um agente de pesquisa a partir da documentação oficial da BytePlus (atualizada em 2026-09-28), do catálogo de API do Higgsfield, dos schemas da fal.ai e do Replicate e de imprensa e guias de praticantes.
**Marcação:** CONFIRMED = fonte oficial ou várias fontes independentes · REPORTED = fonte única ou secundária · UNVERIFIED = sem fonte adequada. As siglas remetem à lista de fontes no fim.

## Correções-chave a suposições comuns

1. **O 2.5 vai até 1080p** (4K existe só no 2.0).
2. **Não há campo de prompt negativo** em nenhuma plataforma; exclusões vão no texto.
3. **O 2.5 não tem parâmetro de multi-shot.** `multi_shots`, `multi_shot_mode`, `multi_prompt` e `speedramp` do Higgsfield pertencem ao Cinema Studio e ao Kling.
4. **Timestamps funcionam no 2.5** (no 2.0 só "Shot N").
5. **A sintaxe de referência a uploads varia por plataforma.**

## 1. Lançamento

- ByteDance; "Dreamina Seedance 2.5", ID `dreamina-seedance-2-5-260628` — CONFIRMED (BP-2.5).
- Prévia em 2026-06-23 (FORCE) — REPORTED. Lançamento na China em 2026-07-31 (Jimeng, Doubao) — CONFIRMED. Higgsfield: post de 2026-08-06, changelog de 2026-08-07 — CONFIRMED.
- Novidades vs 2.0 — CONFIRMED (BP-2.5, BP-2.5-PG):
  - duração máxima de 15 → 30 s;
  - imagens de referência de 9 → 30; vídeos e áudios de 3 → 10 cada; duração total de áudio/vídeo de 15 → 30 s; máximo de 50 referências;
  - referência só de áudio passa a ser permitida;
  - aspecto e duração travam automaticamente no input em edição, extensão e first-frame;
  - saída em `mov`;
  - 11 idiomas;
  - modo draft;
  - 1080p em HEVC 10-bit;
  - **timestamps respeitados**;
  - **imagens multi-view de personagem aceitas**.
- A própria ByteDance diz que não é um salto do tamanho do 2.0 e que 2.5 e 2.0 têm "preferências estéticas significativamente diferentes" — CONFIRMED.

## 2. Limites de geração

- **Duração:** `[4, 30]` s inteiros ou `-1` (o modelo escolhe). Higgsfield: 4–30 s — CONFIRMED.
- **Resolução:** 480p e 720p (8-bit), 1080p (10-bit H.265); padrão 720p; sem 4K no 2.5 — CONFIRMED. O "native 4K" da landing do Higgsfield contradiz a doc oficial e a própria API (marketing ou upscale).
- **Aspectos:** `21:9, 16:9, 4:3, 1:1, 3:4, 9:16, adaptive`; 21:9 em 1080p = 2206×946 — CONFIRMED. First-frame, first/last-frame, edit e extend exigem `adaptive`.
- **FPS:** 24 — CONFIRMED.
- **Tamanho do prompt:** recomendação oficial de "no more than 500 Chinese characters or 1,000 English words" — CONFIRMED. Não há limite rígido documentado na BytePlus; o limite do Higgsfield é UNVERIFIED. *(Observado no ANERNEQ: prompts de até ~19 mil caracteres, ~3 mil palavras, funcionaram no Higgsfield.)*
- **Áudio** sai mono — CONFIRMED (BP-API).
- **Rostos reais:** a BytePlus 2.5 não aceita upload direto de referência com rosto humano real; os caminhos são outputs de modelo confiáveis, personagens pré-definidos ou assets autorizados — CONFIRMED. No Higgsfield: UNVERIFIED.

## 3. Referências multimodais

- **Limites** — CONFIRMED:
  - imagens: 1–30, até 30 MB cada, 300–6000 px, proporção 0,4–2,5;
  - vídeos: até 10, 2–30 s cada, total ≤30 s, ≤200 MB;
  - áudios: até 10 (wav/mp3), 2–30 s cada, total ≤30 s, ≤15 MB;
  - corpo da requisição ≤64 MB.
- **Papéis:** `first_frame`, `last_frame`, `reference_image`, `reference_video`, `reference_audio` — CONFIRMED.
- **O que uma referência pode controlar** (tabela oficial) — CONFIRMED:
  - identidade e/ou voz do sujeito;
  - movimento (ação, expressão, câmera, efeitos);
  - **movimento e luz a partir de modelo 3D "clay" (sem textura)**;
  - estilo;
  - áudio (música, diálogo, timbre);
  - storyboard multi-painel (≤15 painéis, traço);
  - **keyframes seguidos estritamente**, abrindo o prompt com "Use Images X to X in order as keyframes.";
  - first/last frame.
- **Contagens recomendadas:** 1–8 sujeitos por imagem (9–12 é menos estável); 1–5 sujeitos por áudio/vídeo, com clipes de 5–10 s — CONFIRMED.
- **Sintaxe por plataforma:**
  - BytePlus: `@Image 1`, `@Video 1`, `@Audio 1`, numerados pela ordem de upload, com variações toleradas — CONFIRMED. Recomendação: descrever cada mapeamento no texto e subir as referências na ordem em que os sujeitos aparecem.
  - fal: `@Image1`. Replicate: `[Image1]`. Higgsfield (blog): "the woman in @Image 1" — REPORTED.
  - *Observado no ANERNEQ:* o Higgsfield salva menções como `<<<uuid-do-element>>>` e `<<<image_1>>>`.
- **Na edição/extensão:** escreva "Video 1", não "reference Video 1" — CONFIRMED para o 2.0.

## 4. Áudio nativo

- Com `generate_audio` (padrão), gera voz, efeitos e música, com fala sincronizada — CONFIRMED.
- **Vários falantes:** suportado, com mapeamento do tipo "Images 1-2 are Character 1 and correspond to Audio 1" — CONFIRMED.
- **Idiomas (2.5):** chinês, inglês, espanhol, indonésio, malaio, tailandês, árabe, **português**, vietnamita, japonês e coreano — CONFIRMED.
- **Voz por áudio:** a referência carrega "music, dialogue, voice, tone, or timbre"; ajuda descrever a voz junto, como "the low, thick, warm… voice of @Audio 1" — CONFIRMED.
- **Notação oficial:** música em `()`, SFX em `<>`, diálogo em `{}`, legendas em `【】`; nomear o idioma antes da fala; "Character's line (emotion): content". A referência de API sugere aspas duplas. As duas formas são oficiais.
- **Padrão quando não especificado:** tende a diálogo em mandarim e música de sonoridade chinesa; nomeie idioma e sotaque — REPORTED.

## 5. Multi-shot

- **Cortes dentro de uma geração, por texto: sim** — CONFIRMED. Use timestamps ou "Shot N", por exemplo `Shot 1 | 0-2s` ou "[Shot list] (9 shots, approximately 30 seconds)".
- **Regras de timestamp:**
  - unidades de 1 s, sem lacunas entre faixas;
  - conteúdo demais numa faixa gera "excessive cuts or omit parts of the plot";
  - não use timestamps para ações de alta frequência — CONFIRMED.
- **Transições:** dê o momento e o método — CONFIRMED.
- **Sem parâmetro dedicado** no 2.5 em nenhuma plataforma — CONFIRMED.

## 6. Negativos

- Não há campo separado — CONFIRMED.
- Guia oficial: "Use positive descriptions whenever possible. Negative constraints are supported for subtitles and audio control." — CONFIRMED.
- O FAQ oficial, porém, usa negativos em outros casos: "normal human eyes; no glowing eyes" como "highest-priority negative constraint", "Do not generate duplicate versions of a character or a twin effect" e uma seção `[Strictly exclude]` — CONFIRMED.

## 7. Guia oficial de prompt

- **Fórmula do 2.5:** sujeito + ação/evento + cena e ambiente + estilo visual + movimento de câmera/cortes + som — CONFIRMED.
- **Ordem recomendada:** mapeamento dos assets → resumo de uma frase → timeline/Shot N → notas do que permanece constante — CONFIRMED.
- **Vocabulário de câmera:**
  - planos: extreme wide/wide/medium/medium close-up/close-up;
  - movimentos: push in/pull out/pan/track/follow/orbit/dive/pull back/tilt up/handheld shake;
  - ângulos: low angle/overhead/first-person;
  - técnicas: one-shot, dolly zoom, FPV, bullet time, speed ramp;
  - para termos de nicho, use "[termo + explicação descritiva]" — CONFIRMED.
- **Atuação:**
  - 2.0: partes do corpo com amplitude, velocidade e força; emoção pelo detalhe físico;
  - 2.5: ações gerais e expressões descritivas, sem expressões idiomáticas — CONFIRMED.
- **Skill oficial de otimização de prompt** `sd25-pe` — CONFIRMED:
  - instalação: `npx --yes skills@latest add "https://arkdocs-en.tos-ap-southeast-1.volces.com/skills/" --skill sd25-pe --yes`
  - uso: `/sd25-pe`
- **Prática no Higgsfield:** seções rotuladas, "one visual rule at the top, one sound rule at the bottom", fala no formato `At 5.4s she says, soft and unsteady: "…"` — REPORTED.

## 8. Edição, extensão, continuação

- `omni_reference_task_type`: `auto | reference | edit | extend`; um prompt incoerente com o tipo gera erro — CONFIRMED.
- **Edição parcial por timestamp** ("from 4-6 seconds in Video 1… leave the rest unchanged"); exige ratio `adaptive` e duração `-1`; input de 4–30 s — CONFIRMED.
- **Extensão** de 4–30 s, repetível; **transição** que gera o trecho entre dois vídeos; `return_last_frame` para encadear clipes — CONFIRMED.
- **Higgsfield:** `mode` = `t2v | omni_reference | video_edit | video_extension`; `extension_mode` = `backward/forward` — CONFIRMED.

## 9. Falhas e correções

- **Legendas aparecendo:**
  - não repita palavras da fala nem anexe tom a palavras isoladas;
  - use "Character's line (emotion): content";
  - use vídeos de referência sem legenda — CONFIRMED.
- **Música apesar de "no BGM":** liste os sinônimos (music, BGM, score, instrumental, melody, synth, ambient pad) e repita a restrição no início e no fim — CONFIRMED.
- **"Glowing eyes":**
  - vêm de linguagem emocional forte; corrija com palavras neutras e "normal human eyes; no glowing eyes" — CONFIRMED;
  - "glassy/dead eyes" como problema documentado: UNVERIFIED (documentado por praticantes e no ANERNEQ).
- **Deriva de identidade:** headshot separado, assets importantes primeiro, nome amarrado à imagem a cada menção — CONFIRMED.
- **Clones e gêmeos:**
  - mais de 4 pessoas referenciadas fica instável;
  - amarre cada personagem a uma imagem e adicione uma restrição global de "no duplicates";
  - use fotos de uma pessoa só e divida elencos grandes em imagens de grupo de no máximo 4 — CONFIRMED.
- **Esquerda/direita trocando entre cortes:** UNVERIFIED como problema documentado. A técnica oficial é declarar o blocking ("A is on the left…"). Hedra relata que uma imagem de referência venceu o texto "NEVER cross"; nesse caso, conserte a imagem — REPORTED.
- **Outros problemas e correções** — CONFIRMED:
  - texto na tela com erro: soletre ou mande o texto como imagem;
  - texturas de "impressão digital": reduza as referências à resolução de saída;
  - áudio borbulhando: remova palavras de água e eco;
  - tarefas complexas: separe em uma passada de referência e outra de edição.
- **Relatos de praticantes** — REPORTED:
  - lip-sync atrasando no fim de falas longas: falas curtas, MCU, falante nomeado;
  - pronúncia inglesa irregular: grafia fonética e nada de fala nos últimos segundos;
  - o 2.5 pede direção mais explícita que o 2.0.

## 10. Draft, bitrate, genre, Cinema Studio

- **Draft:** `draft=true` gera prévia em 480p; finalizar com `draft_task.id` renderiza **1080p** sem reenviar prompt nem assets (dá erro mesmo com valores iguais); o id vale 7 dias — CONFIRMED. Higgsfield tem `draft` e `draft_job_id` — CONFIRMED.
- **`bitrate_mode`** (`standard | high`) no Higgsfield: "High gives higher video quality at the same credit cost" — CONFIRMED.
- **`genre`:** não é parâmetro do `seedance_2_5` no Higgsfield (só do 2.0) — CONFIRMED.
- **Cinema Studio 4.0** (Higgsfield):
  - parâmetros de era, câmera, lente, abertura, ritmo, gênero, rig de luz e paleta; mesmos parâmetros de modo, duração e resolução do `seedance_2_5` — CONFIRMED;
  - que roda sobre o 2.5: UNVERIFIED (inferência).
- O `seedance_2_5` no Higgsfield não tem `seed` — CONFIRMED.

## Fontes

- BP-2.5: https://docs.byteplus.com/en/docs/modelark/seedance-2-5
- BP-2.5-PG: https://docs.byteplus.com/en/docs/modelark/seedance-2-5-prompt-guide
- BP-2.0: https://docs.byteplus.com/en/docs/modelark/seedance-2-0
- BP-2.0-PG: https://docs.byteplus.com/en/docs/modelark/seedance-2-0-prompt-guide
- BP-API: https://docs.byteplus.com/en/docs/modelark/create-video-generation-task-api
- Seed 2.5: https://seed.bytedance.com/en/seedance2_5
- Seed 2.0 paper: https://seed.bytedance.com/en/public_papers/seedance-2-0-advancing-video-generation-for-world-complexity
- IT之家: https://www.ithome.com/0/984/104.htm
- TechNode: https://technode.com/2026/07/31/bytedance-launches-seedance-2-5-video-generation-model/
- AIbase: https://news.aibase.com/zh/news/29094
- Higgsfield changelog: https://higgsfield.ai/changelog
- Higgsfield blog (lançamento): https://higgsfield.ai/blog/seedance-2-5-on-higgsfield-2026
- Higgsfield prompting guide: https://higgsfield.ai/blog/seedance-2-5-prompting-guide
- Higgsfield página: https://higgsfield.ai/seedance-2.5
- fal: https://fal.ai/models/bytedance/seedance-2.5/reference-to-video/api · https://fal.ai/learn/tools/seedance-2-5-workflows
- Replicate: https://replicate.com/bytedance/seedance-2.5/api
- Comfy Router: https://docs.comfy.org/development/comfy-router/models/byteplus/dreamina-seedance-2-5-260628/code.md
- APIYI: https://docs.apiyi.com/en/live/2026-08/seedance-2-5-launch
- AI Video Sensei: https://aivideosensei.com/guides/seedance-2-5-higgsfield-settings
- Hedra: https://www.hedra.com/blog/directing-seedance-2-5-with-beats
- Leadde: https://leadde.ai/blog/seedance-2-5-reddit-review
- seedance.tv: https://www.seedance.tv/blog/seedance-2-5-lip-sync-issues
