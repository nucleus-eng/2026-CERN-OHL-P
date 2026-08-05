---
# Ensure that this title is the same as the one in `myst.yml`
title: "Bioprinting Synthetic Cells Within a Hydrogel Matrix"
abstract: | 
    This module focuses on using commercial bioprinters to incorporate synthetic cells and bacteria within an agarose hydrogel. Bioprinting will enable precise spatial patterning of giant unilamellar vesicles (GUVs) and bacteria within the matrix. The GUVs will encapsulate nucleus cytosol and a DNA template encoding *pT7-GFP-T7term*, whereas *E. coli* are tagged with red fluorescent protein (RFP), allowing both to be visualised with fluorescence microscopy. Bioprinting should also facilitate scaling of the material after incorporation of the other modules.
---

# Overview

Bioprinting enables precise spatial patterning of cells within hydrogels. This allows synthetic cells and bacteria to be patterned within the same material, which may be required for the wider biosensing applications of the project. The work will initially focus on using commercial bioprinters to print ultra-low gelling temperature agarose with defined thickness in custom well plates. Next, GUVs incorporating nucelus cytosol and a DNA template encoding *pT7-GFP-T7term* will be encapsulated within the hydrogel and protein expression visualised using fluorescence microscopy. Similarly, *E. coli* expressing RFP will be printed within the hydrogel and visualised using fluorescence microscopy. Finally, the synthetic cells and bacteria will be spatially patterned throughout the same hydrogel material, by firstly forming droplet interface bilayers (DIBs) between the different populations to enable segregation, prior to gelling the material (See Ref 1 + 2). The project will evolve in complexity in collaboration with the team to produce a colourimetric material that can sense and respond in the presence of bacteria. 

:::{figure} /BioPrinting.png
:label: fig:FA_metabolism
:width: 75%
Schematic of the project. Bioprinting should enable controlled spatial patterning of organelles within the hydrogel. 
:::

# Components

:::::{tab-set}

::::{tab-item} Membrane
:::{table}
:name: components-membrane

| Lipid | Volume fraction | Notes |
| :---- | :---- | :---- |
| *POPC* | **70 %** | Purchased from Avanti Polar Lipids |
| *Cholesterol*  | **29.95 %** |Purchased from Sigma Aldrich|
| *Liss RhodPE* | **0.05%** |Purchased from Avanti Polar Lipids|

:::
::::
::::{tab-item} Hydrogel
:::{table}
:name: components-Hydrogel

| Material | Brief description | Notes |
|----------|-------------------|-------|
| 1.5% w/v ultra-low gelling temperature agarose | Hydrogel which gels at room temperature| Purchased from Sigma Aldrich |
:::
::::


::::{tab-item} DNA
:::{table}
:name: components-dna

| Template | Expected Concentration Range | Notes ||
| :---- | :---- | :---- | :---- |
| *pT7-GFP-T7term* | 10 ng / µL | Manuel has stock in Yuval's lab |  |

:::
::::





# Milestones

- **Milestone 1.** Printing of agarose hydrogel with defined thickness using a commercial bioprinter/liquid handler.
    - **Risk:** Material is too viscous for controlled printing.
    - **Success criteria:** Printing material at varied thicknesses in custom well plates.
- **Milestone 2.** Embedding of GUVs encapsulating a fluorescent dye within the hydrogel matrix. Fluorescence microscopy will be used to visualise incorporation.
    - **Risk:** Minimal risk; this has previously been conducted in the literature (see Ref 3).
    - **Success criteria:** Imaging of GUVs within the hydrogel.
- **Milestone 3.** Embedding of *E. coli* expressing RFP within the hydrogel. Fluorescence microscopy will be used to visualise incorporation.
    - **Risk:** Minimal risk; this has previously been conducted in the literature (see Ref 1).
    - **Success criteria:** Imaging of fluorescent bacteria.

- **Milestone 4.** Segregated printing of GUVs and bacteria within the same hydrogel. This will first require the formation of DIBs to enable separation before the droplets gel.
    - **Risk:** May encounter compatibility issues with bioprinting directly into the lipid-in-oil solution.
    - **Success criteria:**  Variation in fluorescent readout across the material, depending on whether GUV or bacterial population.
      
- **Milestone 5.** Incorporating other modules developed by collaborators to produce a material with visible colour change in the presence of bacteria.
    - **Risk:** Difficulties in incorporating the different modules and scaling to be visible without a microscope.
    - **Success criteria:** Visual readout in the material by the naked eye.

# Immediate next step

- Initial experiments will focus on printing ultra-low gelling temperature agarose hydrogel with defined thickness in custom well plates. Different commercial bioprinters/liquid handling robots will be trialled.
- Working alongside Julia Purrinos (Contini lab) and Ion Ioannou (Ces lab), GUVs and polymersomes encapsulating a fluorescent dye will be embedded within the hydrogel matrix and visualised using microscopy to confirm incorporation.
- Alongside Charlie Newell (Booth lab), the thickness of hydrogel required for visual readout of the biosensor will be quantified. Dyes will be encapsulated within GUVs and printed in hydrogels to determine the minimum viable thickness of material for successful readout.

# Useful references
- Bioprinting different bacteria species within the same hydrogel. [](https://doi.org/10.1038/s41467-021-20996-w)
- Bioprinting synthetic cells and communication with bacteria.  [](https://doi.org/10.1002/adma.202412292)
- Embedding GUVs into agarose hydrogels. []( https://doi.org/10.1038/s41589-023-01374-7)

