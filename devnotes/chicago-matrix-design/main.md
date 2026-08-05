---
# Ensure that this title is the same as the one in `myst.yml`
title: "[Title]"
abstract: |
  This project evaluates conditions that support stable liposomes and effective cell-free protein synthesis within giant unilamellar vesicles (GUVs). GFP-expressing cell-free systems are encapsulated in GUVs of different lipid compositions to assess functional robustness, while microscopy and plate-based assays quantify vesicle stability and protein production within various matrix materials. Key parameters—including crosslinking density, external osmolarity, hydrogel weight percent, and nutrient supplementation—are systematically varied to identify conditions that maximize GFP yield and maintain artificial-cell sensor sensitivity within the matrix environment.
---

# Overview

This module is an experimental framework for integrating cell-free protein synthesis systems into liposome-based artificial cells embedded within hydrogel matrices. It addresses the challenge of maintaining both liposome stability and robust protein production when artificial cells are transferred from solution into structured material environments. By evaluating lipid composition, matrix compatibility, and environmental parameters that influence GFP expression and vesicle integrity, the module defines design rules for creating stable, functional artificial-cell sensors within engineered materials.

- **This module works by titrating hydrogel weight percent, crosslinker, and osmolarity {ref}`fig-schematic`, in order to stabilize liposomes and optimize protein production from encapsulated cell free**
    - Key components include the hydrogel, crosslinker, membrane lipids, cell free protein synthesis system, and a GFP plasmid.
    - The output of the system will be GFP fluorescence.
      
- Performance metrics:
    - Artificial cells should maintain stability and protein expression in a hydrogel environment for 24hrs as seen via confocal microscopy.
    - Artificial cells should express GFP at similar efficiency as bulk cell free expression of GFP. 
- This module will describe a matrix composition that will support cell free expression from liposomes containing cell free expression systems.

:::{figure} DiagramHydrogel.webp
:name: fig-schematic
:width: 50%

Diagram of a hydrogel containing liposomes. After incubation at 37C, GFP will be expressed in the liposomes.
:::




# Components

:::::{tab-set}

::::{tab-item} Cytosol
:::{table}
:name: components-cytosol

| Material | Brief description | Notes |
|----------|-------------------|-------|
| b.next Cytosol | PURE prepared by b.next | N/A |
| Sucrose | 300 mM-1M | Used for density |

:::
::::

::::{tab-item} DNA
:::{table}
:name: components-dna

| Template | Expected Concentration Range | Sequence/status | Notes |
| :---- | :---- | :---- | :---- |
| pT7-mEGPF-Flag | 10 ng/uL | *Synthesised and templates prepared* | A reporter under T7 promoter system with a flag-tag. |


:::
::::


::::{tab-item} Membrane
:::{table}
:name: components-membrane

| Lipid | Volume fraction | Notes |
| :---- | :---- | :---- |
| *POPC* | **29.95 %** | Or DOPC |
| *Cholesterol*  | **70 %** |  |
| *Liss RhodPE* | **0.05%** |  |

:::
::::

::::{tab-item} Outer Solution
:::{table}
:name: components-outer

| Molecule | Expected Concentration Range | Membrane permeable? Which membrane? | Notes |
|----------|------------------------------|------------------------------------|-------|
| Glucose | 300 mM-1M | Yes | Used for density |
| Feeding solution | Cytosol concentrations | Maybe | Used to prevent diffusion of small molecule components |

:::
::::

:::::


# Milestones

- **Milestone 1.** Final selection of matrix material and early proof of compatibility.
    - **Risk.** Incompatibility of crosslinking mechanism with liposome stability.
    - **Success Criteria:** Some Liposomes maintain integrity after crosslinking.
- **Milestone 2.** Adjustment of crosslinking density, osmolarity, and monomer wt% to stabilize large liposomes.
    - **Risk.** Greater than 50% of liposomes lyse following crosslinking.
    - **Success Criteria:** Greater than 50% of the liposomes are stable and produce GFP for at least 24 hours. 
- **Milestone 3.** Refinement of the external solution to support cell-free expression and increase protein yield.
    - **Risk.** Components from the external solution could attenuate cell-free expression.
    - **Success Criteria:** Passive diffusion of small molecules supports GFP expression on a similar scale to that seen in a bulk solution.

# Immediate next step

Selection of a hydrogel which is compatible with GUV stability and 3D printing.

# Useful references

- Robust and tunable performance of a cell-free biosensor encapsulated in lipid vesicles. [](https://www.science.org/doi/10.1126/sciadv.add6605)
- Generating dual structurally and functionally skin-mimicking hydrogels by crosslinking cell-membrane compartments. [](https://doi.org/10.1038/s41467-024-45006-7)
- Posing for a picture: vesicle immobilization in agarose gel. [](https://doi.org/10.1038/srep25254)

