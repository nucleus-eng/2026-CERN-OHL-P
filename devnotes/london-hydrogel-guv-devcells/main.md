---
# Ensure that this title is the same as the one in `myst.yml`
title: "Hydrogel-Embedded GUV Developer Cells"
abstract: |
  This module creates lipid-based GUV “developer cells” that can be hydrogel-embedded, and can stably encapsulate a cell-free expression system and produce functional proteins. It provides a foundational synthetic-cell chassis for building spatially organised signalling and functional modules.
---

# Overview

This module represents a developer-cell platform based on lipid-derived giant unilamellar vesicles (GUVs) designed to function as minimal, programmable synthetic cells. By encapsulating a cell-free expression system within these GUVs and embedding them in agarose or alginate hydrogels, the module establishes a robust chassis for spatially organised, transcription-translation–driven biological activity. The work enables controlled protein production—such as GFP—within immobilised synthetic cells, providing a stable and tuneable foundation for downstream signalling and communication modules.

This module addresses the core challenge of creating synthetic cells that are both functionally active and can be spatially constrained in 3D environments. Conventional GUVs can be fragile, difficult to stabilise, and challenging to integrate into tissue-like matrices. By developing reliable encapsulation methods, hydrogel-compatible membrane formulations, and demonstrably stable expression capabilities, this module solves a key bottleneck in building multicellular synthetic architectures.

- The module creates lipid-based GUV developer cells that encapsulate a cell-free TX–TL system and are immobilised within agarose or bioprinted hydrogels. Each GUV functions as a compartmentalised microreactor, taking DNA templates and TX–TL reagents as inputs and producing expressed proteins (e.g. GFP) as outputs, while the hydrogel provides mechanical stability and spatial organisation.

The module is expected to support stable vesicle encapsulation with low leakage, detectable protein expression within hours, and mm-scale spatial control of GUV placement in hydrogels.

What this module enables for others
It provides a reusable, plug-and-play synthetic-cell chassis that allows others to deploy programmable gene expression and spatially organised synthetic cells in 3D materials without developing GUV–hydrogel integration from scratch.

:::{figure} general/7eee0f6f-c61c-45a2-b08f-7b352b373331.png
:name: fig-schematic
:width: 50%

Lipid-based GUVs encapsulating TX–TL are embedded in hydrogels to form stable, spatially organised synthetic microreactors.
:::




# Components

:::

:::

:::::{tab-set}

::::{tab-item} Cytosol
:::{table}
:name: components-cytosol

| Material | Brief description | Notes |
|----------|-------------------|-------|
| TXTL cell-free expression mix | PURE or extract-based system for GFP expression inside GUVs. | Match osmolarity to outer solution. |
| GFP DNA template | Reporter construct for validating protein expression. | Plasmid or linear template possible. |
| Calcein | Fluorescent dye for encapsulation and leakage testing. | Avoid high concentrations (self-quenching). |
| Sucrose | Osmotic and density stabiliser for lumen. | Standard for GUV imaging. |

:::
::::

::::{tab-item} DNA
:::{table}
:name: components-dna

| Template | Expected Concentration Range | Sequence/status | Notes |
| :---- | :---- | :---- | :---- |
| *T7–GFP–T7term* | 5–10 nM | Ready | Benchmark TXTL reporter. |
| *Control no-GFP plasmid* | 5–10 nM | Ready | Negative control for fluorescence background. |

:::
::::

::::{tab-item} Membrane
:::{table}
:name: components-membrane

| Lipid | Volume fraction | Notes |
| :---- | :---- | :---- |
| *EggPC* | 50–100% | Primary GUV lipid; compatible with αHL. |
| *DOPC* | 0–50% | Tunes membrane fluidity. |
| *Cholesterol* | 0–30% | Provides rigidity and hydrogel stability. |
| *Liss Rhod PE* | 0.05–0.1% | Fluorescent membrane marker. |

:::
::::

::::{tab-item} Outer Solution
:::{table}
:name: components-outer

| Molecule | Expected Concentration Range | Membrane permeable? Which membrane? | Notes |
|----------|------------------------------|--------------------------------------|-------|
| Glucose | 200–500 mM | Yes | Density contrast with sucrose inside GUVs. |
| Agarose hydrogel | 0.5–1.5% | No | Immobilises GUVs for imaging. |
| Bioprinted hydrogel (bioink) | Variable | No | For 3D patterned embedding. |
| Osmotic buffer (matching TXTL) | Varies | Possible | Prevents vesicle swelling/shrinkage. |


:::
::::

:::::



# Milestones

-Milestone 1. Generate lipid-based GUVs and validate encapsulation and stability using calcein, followed by demonstration of TXTL-  driven GFP expression inside GUVs.
  -Risk. Osmolarity mismatches or low encapsulation efficiency may destabilise GUVs; this can be mitigated by carefully matching inner/outer osmolarity and optimising EPT or swelling conditions.
  -Success Criteria. Stable, intact GUVs with clear calcein encapsulation and measurable GFP fluorescence over time.

-Milestone 2. Embed calcein- and TXTL-loaded GUVs within agarose and bioprinted hydrogels and assess their spatial distribution and structural integrity.
  -Risk. Hydrogel gelation or bioprinting shear forces may disrupt or rupture GUVs; mitigation includes adjusting gelation temperatures, ink viscosity, and printing pressures.
  -Success Criteria. Evenly distributed, intact GUVs within hydrogels that retain encapsulated fluorescence and remain stable over defined time periods.

-Milestone 3. Optimise membrane composition (e.g., eggPC/DOPC mixtures) to enhance robustness and prepare the system for downstream modules such as αHL pore incorporation.
  -Risk. Certain lipid formulations may compromise GUV formation or compatibility with embedded environments; mitigation involves systematic variation and quantitative characterisation.
  -Success Criteria. Identification of membrane compositions that reliably form GUVs, maintain stability in hydrogels, and support future functionalisation steps. 

## Immediate next step

The first experiment will be to generate lipid-based GUVs and load them with calcein to confirm successful encapsulation and vesicle integrity. Will produce GUVs using either gentle swelling or EPT and image them by fluorescence microscopy to verify dye retention and membrane stability. This establishes the baseline formation method and quality control needed before introducing TXTL system and integration to hydrogels.

# Useful references

- Demonstrates how GUVs can be immobilised and stabilised within agarose gels, providing the foundational method used in this module. [](https://doi.org/10.1038/srep25254)
- Shows strategies for encapsulating and expressing genetic programs within synthetic cells, directly informing this module’s approach to TXTL-loaded GUVs. [](https://doi.org/10.1073/pnas.2404790121)


