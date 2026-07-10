# Prompt 1

```text
Create a dense, publication-quality computer-vision overview figure for a multimodal UAV image alignment paper. The figure must look like a real CVPR / ICCV / TPAMI style method figure, not a simple infographic. Use a white background, vector-paper style, thin linework, subtle shadows only where necessary, elegant academic typography, panel labels, inset callouts, grouped regions, local zoom boxes, and a compact legend. The visual complexity should be moderately high, with multiple hierarchical elements, but still clean and readable.

Use a multi-level composition, not a single left-to-right strip:
- top row: two smaller side-by-side panels (a) and (b)
- middle row: one dominant wide grouped panel (c)
- bottom row: two unequal panels, left larger than right, labeled (d) and (e)
Overall aspect ratio about 16:10.

Panel (a), top-left: “Real UAV RGB-Thermal Data”
Show exactly 4 paired RGB-thermal thumbnails arranged as a 2 by 2 mosaic. Each pair should use real-looking UAV viewpoints only: oblique aerial or elevated top-down, not car view, not street surveillance. Use only these scene types: farmland, substation / power lines, solar panels, industrial rooftop or road infrastructure. Two thermal thumbnails grayscale, two pseudocolor. Add very small corner condition tags on each pair such as day, night, low-light, wide, zoom, grayscale, pseudocolor. Keep tags tiny and elegant. Add one small inset magnifier box zooming into a local RGB-thermal structural region, such as wires, roof edges, field boundaries, or road markings.

Panel (b), top-right: “Broad Pairwise Homography Evidence”
Do not draw network internals. Instead, create a compact comparison-style abstract panel with 6 method tags arranged in two rows:
SIFT, AKAZE, LoFTR, RoMa, XoFTR, raw MINIMA.
Below the tags, show 3 tiny pair-level abstract match cards: paired image tokens, sparse or dense correspondence glyphs, and miniature homography tokens. Add a very small legend explaining green = usable homography, red = non-usable or rejected. Do not add numbers. This panel should visually suggest that many off-the-shelf baselines can produce pairwise homography evidence.

Panel (c), center full-width dominant panel: “UAV-TAlign Scene-Level Reliability Framework”
This must be the most visually sophisticated part of the figure, but still abstract, not full of fake qualitative outputs.
Divide panel (c) into 3 grouped subregions inside one large light-gray container:
c1 = candidate evidence organization
c2 = robust geometric aggregation
c3 = reliability-aware decision
Add tiny sublabels c1, c2, c3.

Subregion c1:
Show one long scene-level frame strip with 8 abstract RGB-thermal frame tokens. Over it, place a second layer of selection tokens showing staged candidate expansion: small subset, larger subset, full subset. Use curved braces or brackets to indicate progressive scheduling. Then show evenly distributed selections highlighted in green. Add one tiny dashed-note badge: “deterministic default”. Use no real images here.

Subregion c2:
Show accepted frame-level homography hypotheses as medium-size cards flowing into a consensus geometry space. Represent this as a compact manifold-like cluster or parameter-cloud diagram, with weighted hypothesis tokens converging toward a center. Add 1 or 2 red outlier hypothesis tokens drifting outward with dashed rejection arrows. Include one small inset box zooming into “quality weights”, represented by token size, border thickness, or confidence rings. Do not draw actual warped output images here.

Subregion c3:
Show a two-layer decision block. Upper layer: QA metric bank with exactly 6 chips arranged in a 2 by 3 grid:
edge, grad, accepted, stability, reject ratio, outliers.
Lower layer: split into two neighboring decision boxes:
“Canonical Gate”
“Reliability Score”
Canonical Gate must be drawn as a hard binary path with a green retained branch and a gray or muted red rejected branch.
Reliability Score must be drawn as a continuous ranking path with a tiny ranked-bar or ranked-curve abstraction.
Add a small centered separator label between them: “hard decision vs ranking”.

Panel (d), bottom-left: “Retained Scene Alignment Product”
Show exactly one real RGB frame with one subtle aligned thermal overlay. Add two tiny local zoom-in windows with thin connector lines, highlighting structural agreement, for example power lines, road edges, roof boundaries, or field contours. Keep the overlay realistic and understated. Add a small green badge: retained. Add one tiny gray caption tag only: “scene-level product”. No more text.

Panel (e), bottom-right: “Risk-Coverage Profile”
Show a compact scientific mini-plot, not decorative. Use one clean curve, one highlighted star operating point, one faint alternative ranking trajectory if needed, and tiny axis labels only: risk, coverage. Add a tiny note tag: “canonical point marked”. No numbers.

Add a minimal legend along one bottom corner:
blue = RGB
orange = thermal
green = accepted / retained
muted red = rejected / unstable
gray = neutral structure

Critical constraints:
- this must look like a real CV paper figure with layered composition and local callouts
- middle panel should use abstract geometry / hypothesis / metric design, not fake qualitative warping mosaics
- only input and final product panels should use real image thumbnails
- no giant drone illustrations
- no street driving scenes
- no pedestrians
- no segmentation masks, detection boxes, 3D maps, SLAM, or training loops
- no dark theme
- no oversimplified infographic appearance
```

# Prompt 2

```text
Create a detailed architecture figure for a scene-level multimodal image alignment method called “UAV-TAlign”. The figure must look like a real CV paper architecture diagram, not a simple blockchart. Use a white background, crisp vector style, grouped submodules, panel labels, inset zooms, multiple abstraction levels, compact legend, and hierarchical visual organization. Avoid a single straight left-to-right flow. Do not show real qualitative outputs inside the method core.

Use a 2-row architecture layout:
- Row 1: input and frame-level branch
- Row 2: scene-level branch and decision branch
Use vertical cross-links between rows. Overall aspect ratio about 16:10.

Row 1, left to right:
Module (a) “Scene Frame Pool”
Show 8 abstract paired frame tokens arranged in a long strip, with slight viewpoint variation encoded by tiny camera-angle icons. Use no real thumbnails.

Module (b) “Adaptive Candidate Scheduling”
Place above the frame strip a staged pyramid-like structure with three layers of candidate subsets, connected by narrow arrows down to the strip. The pyramid should visually imply progressive expansion from compact to broader evidence. Add small labels only: stage 1, stage 2, stage 3.

Module (c) “Even Representative Selection”
Show evenly distributed sampling markers over the frame strip. Use thin vertical connectors from chosen tokens to the next module. Add one tiny note: reproducible default.

Module (d) “Backbone-Agnostic Pairwise Matching + Geometry Gate”
This is a compound grouped box with two internal lanes:
upper lane = pairwise matching abstraction with image-pair icons and correspondence glyphs
lower lane = geometry screening with 5 metric chips: matches, inliers, ratio, reproj, coverage
At the output of this compound box, show 6 homography hypothesis cards, 4 green accepted and 2 muted red rejected.
Add a tiny corner tag only: backbone-agnostic.

Row 2:
Module (e), directly below matching: “Quality-Weighted Hypothesis Set”
Show accepted homography cards enlarged and encoded with unequal weights via border thickness, glow ring size, or token area. Use one small zoom-in inset to explicitly highlight the visual meaning of weights. No numbers.

Module (f), center and largest: “Robust Scene Consensus”
Represent this as a geometric hypothesis space. Show accepted weighted hypotheses projected into a compact cluster, with a median-like center, one consensus prototype card, and 1 or 2 outliers removed by dashed rejection arrows. Add a tiny local annotation only: robust aggregation. No real images. No large text.

Module (g), to the right of consensus: “QA Metric Bank”
Use a neat 2 by 3 matrix of metric capsules:
edge
grad
accepted
stability
reject ratio
outliers
Below the matrix, show a thin summary strip aggregating these cues.

Module (h), right side split vertically:
top = “Canonical Gate”
bottom = “Reliability Score”
Canonical Gate should visually look binary and threshold-like, using one green branch and one muted red branch.
Reliability Score should look continuous and ordering-like, for example a ranked ladder or tiny monotonic curve.
Add one small brace label between them: decision / ranking.

Module (i), far-right small output card:
“Retained Scene Transform”
Use exactly one small real RGB frame with subtle thermal overlay. This is the only real image-like output in the architecture core.

Additional CV-style structure:
- add panel labels a through i
- add one small legend box in a corner for accepted / rejected / weighted / consensus icons
- use 2 or 3 light-gray group boxes to separate frame-level operations, scene-level operations, and decision logic
- use thin connector lines with occasional orthogonal routing, not just straight arrows

Negative constraints:
- no oversimplified infographic look
- no giant horizontal pipeline
- no real images in the middle consensus or QA modules
- no fake feature maps resembling CNN activation art
- no training loops, losses, backpropagation
- no detection or segmentation outputs
- no extra sensors
```

# Prompt 3

```text
Create a sophisticated conceptual figure for a computer vision paper explaining why pairwise homography availability is not the same as retained scene-level alignment reliability. The style must match modern CV papers: white background, panel labels, local callouts, abstract geometry illustrations, compact legends, and carefully structured subpanels. Do not make it a simple three-box infographic.

Use a 4-panel composition arranged as:
top-left = (a)
top-right = (b)
bottom-left = (c)
bottom-right = (d)
Overall aspect ratio about 4:3.

Panel (a): “Abundant Pairwise Evidence”
Show 6 small real-looking RGB-thermal pair thumbnails from the same UAV scene family, arranged in a staggered 2 by 3 mosaic. At least 5 pairs should carry small green homography badges. Add one tiny inset magnifier highlighting a local structural region. This panel may use real images, but keep them small.

Panel (b): “Scene-Level Hypotheses Are Uneven”
Use abstract hypothesis cards only. Show a compact geometric arrangement where several hypotheses cluster and a few deviate. Add a tiny callout showing that some hypotheses have stronger support than others by using different border weights or confidence rings. No real images in this panel.

Panel (c): “Robust Consensus + QA”
Show a two-stage abstract process:
left half = weighted consensus cluster
right half = QA metric bank with edge, grad, stability, accepted, outliers
Connect them with a compact arrow. Add one tiny legend for accepted, unstable, and consensus center. No qualitative overlays.

Panel (d): “Retained Product vs Ranking”
Split this panel vertically into two mini-columns:
left mini-column = canonical retained result shown as one small RGB image with subtle thermal overlay and a green retained badge
right mini-column = ranking abstraction shown as a vertical ordered scene list or tiny curve
Place one small centered label between them:
hard decision != ranking
Keep it compact and paper-like.

Color rules:
- blue RGB
- orange thermal
- green accepted / retained
- muted red unstable / rejected
- gray neutral structure

Negative constraints:
- no simple storyboard
- no fake mid-pipeline qualitative outputs
- no benchmark tables
- no equations
- no city driving scenes
- no pedestrians
- no giant drones
- no glossy commercial rendering
```

# Prompt 4

```text
Create a benchmark protocol figure for a multimodal UAV image alignment benchmark called “UAV-TAlign-12K”. The figure must look like a real CV benchmark figure, with grouped tracks, panel labels, compact legends, subtle hierarchy, and a layout richer than a simple flowchart. Use a white background, precise vector-paper style, thin outlines, light-gray grouped regions, and moderate information density.

Use a 3-level composition:
Level 1 top band = benchmark anchor
Level 2 middle band = three protocol tracks
Level 3 bottom band = report artifacts
Overall aspect ratio about 16:9.

Top band:
Place two medium modules side by side:
(a) Official Manifest
(b) Scene Metadata
Official Manifest module contains only three tiny facts:
6037 valid pairs
15 scenes
fixed evaluation
Scene Metadata module contains four compact tag groups:
illumination
thermal rendering
view setting
scene family
Under each tag group, put tiny chips, not paragraph text.

Middle band:
Create three tall grouped protocol columns labeled (c), (d), (e):
(c) Track A Pairwise Evidence
(d) Track B Scene-Level Retention
(e) Track C Reliability-Coverage
These should be visually separated by whitespace and thin vertical group boundaries, not merely boxes in a row.

Inside Track A:
Use a compact internal vertical stack:
pair sampling
homography fitting
pair metrics
Add repeated pair icons in the background to indicate many independent evaluations.

Inside Track B:
Use a richer internal structure than Track A:
top = multi-frame scene token board
middle = aggregation node
bottom = QA gate node
end = retained scene token
Add one tiny side note only: hard decision.
All elements abstract, no real qualitative overlays.

Inside Track C:
Use a ranking column abstraction:
scene tokens sorted vertically
coverage sweep arrow
tiny operating-point curve
Add one tiny side note only: ranking only.

Between Track B and Track C place a floating neutral reminder badge:
canonical gate != ranking score

Bottom band:
Place 4 report artifact cards aligned under the relevant tracks:
pairwise benchmark table
scene-level main result
condition breakdown
risk-coverage figure
Use tiny artifact icons, not actual tables or plots with many labels.

Add a very small legend in one corner:
blue = RGB-related
orange = thermal-related
green = retained / accepted
gray = protocol structure

Negative constraints:
- no plain single-row left-to-right flowchart
- no network architecture internals
- no training loop
- no qualitative mid-pipeline image outputs
- no dense numeric table
- no dashboard aesthetic
- no dark theme
```

# Prompt 5

```text
Create a dataset characterization figure for a UAV RGB-thermal benchmark paper. The figure must look like a real CV dataset figure with a central data mosaic, supporting categorical structure, panel labels, local zooms, and controlled visual hierarchy. Use a white background, vector-paper style, thin outlines, elegant typography, light-gray support boxes, and compact legends. Avoid a simple infographic.

Use a radial-plus-grid composition:
center = real data mosaic
four surrounding condition panels = top, left, right, bottom
two small corner insets = zoom details
Overall aspect ratio about 4:3.

Center panel (a): “UAV-TAlign-12K”
Show 6 paired real RGB-thermal thumbnails arranged as a neat 3 by 2 grid. Use only realistic UAV scenes: farmland, road infrastructure, substation / power lines, solar panels, industrial rooftops, building blocks. Each pair must have RGB and thermal side by side. Keep thumbnails small but crisp.

Top panel (b): “Illumination”
Use three abstract condition chips with small icon cues:
day
night
low-light
No real images here.

Left panel (c): “Thermal Rendering”
Use two abstract palette cards:
grayscale
pseudocolor
No real thermal images here.

Right panel (d): “View Setting”
Use three abstract framing icons:
wide
zoom
standard

Bottom panel (e): “Scene Families”
Use 8 compact category chips laid out in two rows:
farmland
road
building
industrial
power infrastructure
solar panels
orchard
woodland

Add two tiny corner zoom-in insets connected to the center mosaic:
one zoom on structural lines or edges
one zoom on texture / thermal contrast
These insets should be small and refined, not dominant.

Add a tiny legend for RGB / thermal color coding.

Negative constraints:
- no pipeline layout
- no large tables
- no charts with many numbers
- no pedestrians, no cars, no street-view scenes
- no decorative drones
- no glossy poster feel
```

# Prompt 6

```text
Create a compact but sophisticated conceptual result figure distinguishing canonical retention from reliability ranking for a UAV RGB-thermal alignment paper. Make it look like a proper CV paper figure: white background, panel labels, miniature abstract tokens, one tiny plot, and careful separation of binary decision versus continuous ranking. Avoid a simple before-after infographic.

Use a split composition with three structured regions:
left large panel = canonical retained set
right upper panel = ranked scene list
right lower panel = risk-coverage plot
Overall aspect ratio about 4:3.

Left panel (a): “Canonical Retained Set”
Use an abstract 3 by 5 scene-card board representing 15 scenes. Exactly 9 cards green, 6 cards gray or muted red. Add one small gate icon above the board and a tiny note: hard retain / reject. No real thumbnails. No scene numbers. Use subtle heterogeneity in card patterns so the board feels like scene tokens, not plain rectangles.

Right upper panel (b): “Reliability Ranking”
Use the same 15 scene tokens reordered vertically from top to bottom. Apply a green-to-gray confidence gradient. Add one small side brace labeled ranking only. Make the visual clearly different from the board in panel (a).

Right lower panel (c): “Risk-Coverage”
Show one clean curve with a highlighted star marking the canonical operating point. Add one faint alternative ranked trajectory if helpful, but keep the plot minimal. Tiny axis labels only, no numbers.

Add one small neutral floating label between panels (a) and (b):
same scenes, different semantics

Negative constraints:
- no full benchmark table
- no oversized text
- no real image thumbnails
- no dark theme
- no glossy chart style
- no oversimplified infographic
```

