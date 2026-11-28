---
name: at-blender-head
description: Use when making a realistic human head in Blender, by sculpting one from a sphere or by building a likeness from photos (KeenTools FaceBuilder). Also use when a head sculpt looks off (wrong proportions, an egg-shaped skull, lumpy or dotted surfaces, ears or a neck that don't sit right) or a photo-built head won't fit its images.
version: 1.0.0
author: Team
status: published
---

# Realistic Heads in Blender

Two routes. **Sculpt** when you're inventing a character or practising form.
**FaceBuilder** when the head must look like a real person in photos. A
FaceBuilder head can then be refined in Sculpt Mode.

Sources: a CG Boost sculpting walkthrough (BPAvvF8py1M, educator, sells
courses) and the official KeenTools FaceBuilder tutorial (tETtRwCnLyg, the
vendor demoing its own paid add-on).

## The one principle

**Big shapes first, at low resolution. Correct early.** Every fix is cheap
while the mesh is coarse and expensive once detail is on it. Don't raise the
resolution or add detail until the silhouette and proportions match the
reference from the front, side and 3/4 views.

## Route 1: Sculpt from a UV sphere

### Setup
- Delete the default objects, add a UV Sphere, and switch to the
  **Sculpting** workspace.
- Turn on **X symmetry** (the butterfly icon, top right).
- **Reference is mandatory**, because nobody sculpts well from memory. Pin
  images over Blender with PureRef. Collect front, side, 3/4, a skull, a
  planar (simplified planes) head, scans, and an écorché for muscles.
- Set the viewport lens to about **95 mm** (N panel > View > Focal Length).
  The default perspective distorts proportions and won't line up with
  photos.
- Tablet: let pen pressure control **strength only**, not radius.

### Stages

| # | Stage | Resolution | Main brushes | Done when |
|---|---|---|---|---|
| 1 | Block | Raw sphere | Grab, Mask + Move | Upside-down egg from the front; chin and back of skull from the side; rough neck |
| 2 | Landmarks | Voxel 0.05 | Crease (low pinch), Grab | Jaw, eye sockets, brow, nose, mouth, cheekbones and ear sketched in |
| 3 | Structure | Voxel 0.05 | Grab, Crease | Skull silhouette matches a skull reference; nose set deep; nasolabial area separated |
| 4 | Forms | Voxel ~0.0085 | Clay Strips, Crease, Flatten, Scrape | Eyelids, nose, lips, mouth corners and masseter have volume |
| 5 | Proportion pass | 0.0085 | Mask + Move/Scale/Rotate | Ears, nose, mouth and jaw are in the right places |
| 6 | Ears | 0.0085 | Clay Strips, Crease, Flatten | Helix, antihelix (the Y/S ridge), lobe and a back "tube" blend into the head |
| 7 | Neck | 0.0085 | Crease, Clay Strips, Grab | Neck upright; Adam's apple, sternocleidomastoid, clavicle and trapezius placed |
| 8 | Character | 0.0085 | Grab | Front/side tweaks set the personality (wider neck and masseter read as strong) |

Remesh: press **R**, set the voxel size, then **Ctrl+R**. Smooth after each
remesh (hold **Shift**).

### Techniques
- **Move a feature without breaking it:** mask it (**M**), soften the mask,
  invert with **Ctrl+I**, then use the Move, Scale or Rotate tool. **Alt+M**
  clears the mask. To scale around the feature, use Sculpt > Set Pivot >
  **Unmasked**.
- **Eyes:** size and place them with the masking method above *before*
  adding eyeball spheres. An eyeball added early anchors you to the wrong
  eye. Lids wrap an imagined sphere; use Grab with a smoother falloff.
- **Polish:** use Flatten with **Normal Radius 1**. It averages the surface
  normal, removes noise and blends shapes together. Use Scrape for harsh
  edges.
- **Sharp creases:** set Crease falloff to Sharper. Hold **Ctrl** to invert
  any brush (push becomes pull).
- **Flow:** Clay Strips along the muscle grain leaves streaks that show the
  muscle's direction. Shape it with Grab, then Flatten and Smooth, then bring
  key creases back with Crease.
- **Blend, then redefine:** smoothing ears or muscles together and creasing
  them back gives better flow than sculpting each part separately.
- **Fat hides muscle.** Hint at most muscles; don't define every one.

### Proportion checks
- Profile: the face is slightly triangular, and the mouth sits back from the
  nose and chin. A mouth set too far forward is the most common error.
- The mouth corners line up roughly below the eyes.
- The top of the ear lines up roughly with the eyes; the bottom is near the
  nose base (standard anatomy, not in the video). Ears tilt back slightly
  and sit well behind the jaw.
- The forehead curves gradually into the side and back of the skull, with no
  hard corner. The top and back of the head follow the skull, not the egg.
- The neck rises roughly vertically; it shouldn't make the head jut forward.
  Its front base sits where the clavicles are.
- Zoom out often to fight tunnel vision. Take features from references
  rather than copying one face.

### Fixes

| Symptom | Fix |
|---|---|
| Dotted, beaded strokes | Stroke Spacing ~5%, turn off Adjust Strength for Spacing, lower the strength |
| Smoothing wipes out form | Lower the Smooth brush strength |
| Head still reads as an egg | Grab the silhouette against skull and planar references from each view |
| Clay Strips artifacts in tight areas | Switch to Crease, then Flatten |
| Features in the wrong place late in the sculpt | Mask + Move (above); don't re-sculpt them |
| Perspective makes it look off | 95 mm lens, and line up the view with the reference |

## Route 2: FaceBuilder (likeness from photos)

Paid KeenTools add-on with a 15-day trial.

1. **Install:** Edit > Preferences > Add-ons > Install the KeenTools ZIP (on
   a Mac it's inside the DMG). Enable it, accept the licence, then click
   **Install Online** for the core library.
2. In the N panel, open FaceBuilder > **Create new head** > **Add images**.
3. **Photos:** front, both 3/4 views, both profiles, both half-backs, low
   and high angles, and the back (needed for back-of-head texture). One
   photo works, but the result is much less accurate. With only a few
   photos, fit the views you have and tell the user the likeness will be
   weaker. Ask for profiles and 3/4 views before anything else.
4. **Round 1 (rough):** align views in the order front → 3/4 → sides → rest.
   Click **Auto Align** on each, then press **Tab** to toggle the mesh and
   check the fit. Keep only pins you're sure of (eyes, ears, nose wings,
   mouth corners). Fewer pins is better here. For views that won't
   auto-align (backs), turn the mesh with the 45° buttons. Your first three
   pins set its orientation and the fourth starts morphing it.
5. **Round 2 (fit):** start from a 3/4 view; it carries the most 3D
   information. Refine eyes, nose, chin, cheekbones, lips, forehead and neck
   in every view. A pin in one view moves the mesh in all of them.
   Complicated faces need a third pass on small curves and bumps.
6. **Model tab:** hide parts you don't want, such as the neck base under a
   T-shirt. For a non-neutral photo (smile, open mouth, closed eyes), turn
   on **Allow facial expressions** in the Views tab so those regions flex without
   distorting the head. Apply a view's expression to the model if needed.
7. **Texture tab:** **Create texture**. The gear icon sets the source views
   and resolution.

- Pins: left-click the mesh to add one, right-click to delete one. Undo is
  safe, so delete pins freely.
- **Long blue dotted residuals** show tension. They're normal far from the
  default head, but they can also mean two pins are pulling against each
  other: remove one.
- Several faces in one image: click Auto Align and pick the target face.
- If the mesh is hard to see over the photo, change its colour or opacity in
  the Appearance tab.

## Not covered here

Retopology, UVs, polycount budgets and export for games or animation. Neither
source video covers them, so say so instead of improvising.

## Driving Blender from Python or an MCP

```python
import bpy
obj = bpy.context.active_object
obj.data.use_mirror_x = True                 # X symmetry
obj.data.remesh_voxel_size = 0.05            # then 0.0085 for detail
bpy.ops.object.voxel_remesh()
bpy.context.space_data.lens = 95             # viewport focal length (in a 3D View context)
```

Brush strokes can't be scripted well. Script the setup, remesh and camera,
and leave the sculpting itself to the user.
