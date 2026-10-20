# Infrared and Thermal Terminology

Updated: 20 October 2026.

## Physical Modality

The H30T payload uses an uncooled VOx microbolometer in the 8-14 micrometre
long-wave infrared (LWIR) band. The specific modality in UAV-TAlign-12K is
thermal infrared. The evaluated images are its grayscale and pseudocolor
renderings. Those display palettes do not define different spectral modalities.

Primary source: [DJI H30 Series specifications](https://enterprise.dji.com/zenmuse-h30-series/specs),
accessed 20 October 2026; cited as `dji_h30_specs` in both manuscripts.

## Manuscript Convention

- Keep `infrared-visible alignment` as the task name, including the title.
- Identify the captured data as RGB and thermal infrared in the abstract.
- Define the H30T LWIR band and the meaning of infrared images in Acquisition
  and Curation. Subsequent `infrared` and `RGB-infrared` references to this
  benchmark use that established meaning.
- Use `infrared-to-RGB` for transformation direction and `infrared rendering`
  for the grayscale/pseudocolor condition. Use `thermal` for physical sensing,
  the thermal camera, and the explicit term `thermal infrared`.
- Retain superscript T, explicitly defined as thermal infrared, in the method.
  Do not rename the image variables or alter any equation.
- Preserve published work titles, dataset/model names, bibliography keys,
  source filenames, `thermal/`, and `thermal_rendering`. These are fixed
  references and interfaces, not alternative claims about the spectrum.

The Chinese manuscript mirrors the same distinction, using the equivalent
full term at the physical definition and the shorter infrared term thereafter.

## Scope of This Pass

The check covers the main manuscript and its two appendices, Chinese mirror,
current figure labels/captions, Highlights, cover letter, and supplement
outline. Historical review notes, original student assets, archived results
and source metadata are preserved. No experiment or result was changed.
