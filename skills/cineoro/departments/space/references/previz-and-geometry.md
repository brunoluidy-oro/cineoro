# Previz and geometry — solving the scene before generating it

The scene is solved before anything is generated. Text alone can't hold space; finished numbers can.

**Contents:** why previz · the Blender workflow · colour coding · solving crowds · blocking light ·
placing the camera · cutting the previz to time · from previz to GEOMETRY text · using previz renders
as references (and the grey-plastic risk) · no-3D fallback

---

## Why

By the second cut the characters have swapped sides and the background has moved. A previz gives
real sizes, distances and overlaps — exactly the parameters the engine gets wrong most often — and
turns them into plain numbers for the prompt.

## The Blender workflow

1. **Block with primitives.** A person is a cylinder, a sphere and two legs. Buildings are low boxes.
   A spear is a stick. No detail: the point is that sizes, distances and overlaps are real.
2. **Colour-code instead of naming.** The crowd stays neutral grey-brown; each character who matters
   gets one colour. From then on the scene is discussed by colour ("yellow steps out from the second
   row", "green with the spear, screen-right"). The crowd stays a mass, not a list of names.
3. **Solve the crowd physically.** How many figures, how far apart, who is in the front row, who
   occludes whom, where visibility falls off.
4. **Block the light at the same time.** One ambient (e.g. dark blue) and the real key source from its
   real direction. The previz shows how far the light reaches, whose faces it touches and whose it
   doesn't, where the shadows fall. The LIGHT block is then written from something already visible.
5. **Place the camera.** Height, distance, angle to the axis, movement — read the numbers off the
   scene.
6. **Cut the previz to time.** At 24 fps, in the film's aspect ratio, with real shot sizes (a wide of
   the crowd, a lateral move along the line, a push to a close-up). The output is a shot list with
   durations — how long each piece runs and what must be readable in it.

## From previz to the GEOMETRY block

Read off, per shot: each character's screen position (thirds), world position relative to the
landmark, body angle, distance between faces/bodies, prop positions relative to anatomy, camera
height, distance, angle off the axis, which side of the axis, what falls into darkness and at what
distance. Write them in metres and degrees.

## Using previz renders as references — the grey-plastic risk

- Production experience: feeding the grey layout render as an **image anchor** made the engine copy
  grey plastic. The grey render is a composition guide for the author and nothing else.
- Officially, Seedance 2.5 accepts **3D clay-model references for motion and lighting**. If you use a
  previz render or animation this way, scope it hard: "use Video N only for the movement, blocking and
  light direction; every visual quality — faces, materials, wardrobe, textures, colour — comes from
  the identity and location references; the shot is fully photoreal". Attach it after the photo
  references. Test once before relying on it.
- Safer default: keep the previz out of the generation; transfer it as numbers (GEOMETRY) and, if
  needed, as a staging map (see `staging-map.md`).

## No-3D fallback

Without Blender: sketch a top-down plan by hand to decide the numbers, then a front-view staging map
for the engine. Or block with a phone photo of stand-ins/toys at the right distances and read the
numbers off it.
