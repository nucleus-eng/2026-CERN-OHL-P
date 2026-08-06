---
# Ensure that this title is the same as the one in `myst.yml`
title: "[Title]"
abstract: |
  We will be designing, manufacturing, and characterizing our biosensing material platforms that house DevCells. 
---

# Overview

Most extracellular matrix (ECM) materials are not suitable for traditional extrusion-based 3D printing because they require high viscosity and experience mechanical stresses that can damage fragile DevCells.
Photopatterning can be used for low-viscosity polymer and hydrogel-based ECMs laden with DevCells. 

As shown in {ref}`fig1`, the function of this module will be demonstrated by:

- Performing selective photopatterning of the hydrogel matrix and characterizing the resolution.

- Analyzing DevCell diffusion dynamics, quantifying the colourimetric response, and validating colour production by DevCells.

**Workflow**

A dual-wavelength  [DLP projector](https://www.ti.com/tool/DLPLCR4500EVM?keyMatch=dlp4500%20evm&tisearch=universal_search) will be used to project a custom-designed QR code to create a photoprogrammed PEGDA hydrogel. We can then integrate the photopatterned hydrogel with two colour-producing DevCell populations (Option 1) or the two salt-producing DevCell populations (Option 2), on an HPC gel, which shows a colorimetric response with the introduction of an analyte. Ideally, the colour response should stay ~24 hours, but the quantification of the same would be done.

:::{figure} ./picdevnote.jpg
:label: fig1
:width: 100%
Schematic workflow of the photopatterning technique. Option 1: DevCells release enzyme for colorimetric response, Option 2: DevCells release salts that change the colour of the HPC gel. 
:::



# Components



:::::{tab-set}


:::{table}
:name: components-cytosol

| Material | Brief description | Notes |
| :---- | :---- | :---- |
| DevCell components  | Salts, plasmids  | To be obtained from DTE, Lucks, and Kamat labs |
| PURE system | Cell-free expression system to be encapsulated | To be obtained from b.next |
| HPC gels  | Composite hydrogel matrix material | To be obtained from Chazot lab |
| DLP Projectors  | Integrate multiwavelength projectors into the systems already developed in the Truby lab | To be bought by the Truby Lab  |


:::





# Milestones

- **Milestone 1. Sensing**: Assess the survival, spatial distribution, and diffusion dynamics of DevCells within and on photopatterned hydrogels.
    - **Risk.** Vesicle Instability - How does free radical generation during polymerization affect encapsulated systems? This will be evaluated through confocal microscopy. Can the GUVs diffuse through the gel to reach the HPC gel and get a visual colorimetric response? Do a z-stack of the embedded GUVs in the hydrogel matrix to evaluate the thickness and to check if the GUVs have diffused.
    - **Success Criteria:** Visual colour readout.
- **Milestone 2. Patterned Colour Production**: Design and validate hydrogel-embedded QR code micro-patterns.
    - **Risk.** Diffusion of DevCell salt components within the hydrogel matrix, which could influence the resulting selective colourimetric response. I have been studying the resolution of photopatterning, which would be beneficial in quantifying the QR code readout.
    - **Success Criteria**: When combined with the HPC gelmatrix, we will see visually the colour change.
- **Milestone 3. Integration**: Demonstrate full system integration by confirming that DevCells embedded within these patterned hydrogels remain functional and produce quantifiable colour outputs.
  - **Risk.** DevCells tested in solution/model systems will fail to function in a hydrogel environment.
  - **Success Criteria**: Achieving reliable integration of all components in the SF lab environment. 
    

## Immediate next step

- Try just the encapsulated dye or encapsulated enzymes with dye to see if the signal in the photopatterned PEG hydrogel is interpretable.
- Try making GUVs made by using Nuclues' Cytosol and check the salt diffusion into the photopatterned hydrogels.
  

# Useful references

- PEG gels programmability described. [](https://doi.org/10.1016/j.eurpolymj.2015.11.002)
- Demonstration of Photopatterning [](https://doi.org/10.1002/adhm.201300054)


