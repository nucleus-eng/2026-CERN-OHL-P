---
# Ensure that this title is the same as the one in `myst.yml`
title: "[Title]"
abstract: |
  This module is to ensure that we can properly encapsulate PURE system for protein production and to maintain membrane stability in hydrogel materials. Sensor and reporters used will be made and developed in Lucks and Tullman-Ercek labs and hydrogels in the Truby lab.
---

# Overview

In this module, I aim to make DeveloperCells (DevCells) that can both encapsulate and protect the PURE expression system while maintaining membrane stability after incorporation in materials. Here, a DevCell is defined as a giant unilamellar vesicle (GUV) that encapsulates the PURE expression system. Encapsulation of the PURE system is beneficial because DevCells protect the PURE components from external contaminants that could degrade them while maintaining crucial protein expression conditions. Additionally, we can define the membrane composition, and this user-defined, selectively permeable membrane enhances the modularity of the DevCell's cell-free capabilities. 

However, vesicles remain vulnerable, and many materials employ harsh chemistries that involve crosslinking via UV-induced free radical polymerization. Free radicals can oxidize lipids and create holes in the membrane, so we need to consider and test membrane compositions that remain robust after free radical polymerization. Once we find a composition to maintain membrane stability, we can implement the entire DevCecreate a hydrogel that is able to sense and respond to its environment. 

In {ref}`fig-schematic`, the key components are the sensors we are using, the composition of the membrane, and the composition of the matrix material and its crosslinking chemistry. The sensors we are using are the theophylline riboswitch and the anhydrotetracycline (aTc) sensor from the Lucks lab. The reporters are from the Tullman-Ercek lab, and they are the LacZ and catecholase enzyme reporters. The matrix material is composed of 4-arm PEG modified with a SH group for free radical photopolymerization. 

A metric to consider is the relevant concentrations of DNA and substrate we are using for the sensors, and how they will differ in a bulk vs. encapsulated reaction. Additionally, we should consider how it will again differ in a material and how concentrated the DevCells will need to be. 
      
This module will allow people to develop their own environmentally responsive materials and understand the parameters to consider when doing so. 

:::{figure} module pic.jpg
:name: fig-schematic
:width: 50%

Schematic showing the encapsulation of the Theophylline Riboswitch sensor and the Tetracycline sensor inside a membrane and then embedded inside a hydrogel.
:::




# Components

:::::{tab-set}

::::{tab-item} Cytosol
:::{table}
:name: components-cytosol

| Material | Brief description | Notes |
|----------|-------------------|-------|
| Nucleus cytosol | PURE prepared by b.next | N/A |
| Enzymatic reporter substrates (x-gal / Catechol) | Substrates that are processed by the reporter enzyme to generate a visible color change. | Catechol is a phenolic compound. |
| DNA | DNA necessary for protein expression | look at the next table tab to see what DNA structures |
| Sucrose | ~300mM | Used for density for phase transfer method |

:::
::::

::::{tab-item} DNA
:::{table}
:name: components-dna

| Template | Expected Concentration Range | Sequence/status | Notes |
| :---- | :---- | :---- | :---- |
| *pT7-TetO-XylE-T7term*| 1-10 nM | Waiting from Lucks/Tullman-Ercek |  |* | 1-10 nM | Waiting from Lucks/Tullman-Ercek |  
| *pT7-TetO-LacZ-T7term* | 1-10 nM | Waiting from Lucks/Tullman-Ercek |  
| *pT7-Theophylline-LacZ-T7term* | 1-10 nM | Waiting from Lucks/Tullman-Ercek  |  
| *pT7-TetO-GFP-T7term* | 2-4 nM | Waiting from Lucks/Tullman-Ercek  |  
| *pT7-Theophylline-GFP-T7term* | 1-10 nM | Waiting from Lucks/Tullman-Ercek  |  
:::
::::


::::{tab-item} Membrane
:::{table}
:name: components-membrane

| Lipid | Volume fraction | Notes |
| :---- | :---- | :---- |
| *POPC* | **33.3 %** |  |
| *Cholesterol*  | **66.6 %** |  |
| *Liss RhodPE* | **0.1%** |  |

:::
::::

::::{tab-item} Outer Solution
:::{table}
:name: components-outer

| Molecule | Expected Concentration Range | Membrane permeable? Which membrane? | Notes |
|----------|------------------------------|------------------------------------|-------|
| Glucose | ~300-1000 mM | Yes | Used for density for phase transfer method |
| Feeding solution | Cytosol concentrations | Maybe | Used to prevent diffusion of small molecule components |

:::
::::

:::::



# Milestones

- **Milestone 1.** Validate that PURE system is able to sense and respond to the analyte of interest while encapsulated in DevCell membrane.
    - **Risk.** It's usually a large risk that the analytes might not cross the membrane. However, we have mitigated this risk by choosing drugs that are able to permeate the membrane.
    - **Success Criteria: I will know I succeed when I am able to see the expression of my reporter protein when the substrate is present.**
- **Milestone 2.** Find DevCell membrane composition that remains robust and stable embedded in the material.
    - **Risk.** The biggest risk is that the vesicles lyse and release all their cargo from the free radical polymerization. The way we can mitigate this is by adding more cholesterol to the membrane to make it more robust, but also potentially vitamin E to combat the free radicals. 
    - **Success Criteria: I will know I succeed when I am able to see the expression of my reporter protein when the substrate is present, while the DevCell is embedded in the material matrix.** 
- **Milestone 3.** Validate that DevCell can sense and respond to the analyte of interest while embedded in the material.
    - **Risk.** The biggest risk is that the signal becomes undetectable through the material, or if the analyte cannot diffuse through the material. We can overcome this by increasing the analyte concentration or changing the crosslinking density of the material.
    - **Success Criteria: I will measure my success through observing a detectable signal from my DevCells through the material matrix.** 

## Immediate next step

The first experiment I will perform is to encapsulate the sensor system in PURE cytosol using the phase-transfer method. Then I will observe the expression of reporter proteins in the presence/absence of theophylline and tetracycline. From this, I will be able to determine if the analytes are able to pass through the membrane and if we can reach a detectable signal. 

# Useful references

- Robust and tunable performance of a cell-free biosensor encapsulated in lipid vesicles. [](https://doi.org/10.1126/sciadv.add6605)
