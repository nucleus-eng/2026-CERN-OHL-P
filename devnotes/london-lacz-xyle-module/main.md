---
# Ensure that this title is the same as the one in `myst.yml`
title: "LacZ/XylE colour change module "
abstract: |
  This module aims to develop LacZ and XylE as reporter enzymes to produce a colorimetric output within hydrogel-embedded GUVs in response to the detection of bacteria. 
---

# Overview

Fundamental to the London node project is the production of a detectable colorimetric output which serves as a signal for the presence of bacteria within the hydrogel device. To generate the output we will use well-characterised reporter enzymes, such as LacZ and XylE. These enzymes can process commercially available substrates into products with different light absorption characteristics, resulting in a colour change. XylE catalyses the oxidation of colourless catechol into a yellow semi-aldehyde. LacZ instead operates by hydrolysing a beta-glycosidic bond of several available galactosides. We will mainly focus on the chlorophenol red galactopyranoside (CPRG) that is converted from a yellow to a dark magenta pigment. 

The LacZ/XylE reporter enzymes will be encoded on linear DNA templates. Two different templates will be tested, T7pro-reporter-T7term, and T7pro-UTR1-G10_leader_peptide-reporter-T7term. The latter sequence incorporates G10 leader transcriptional and translational enhancer sequences to increase expression. The performance of each construct to produce a colorimetric output will be compared. Kinetic absorption measurements of Nucleus cytosol reactions, supplemented with DNA and an appropriate substrate, will be performed to measure the production of colourful pigment over time. Absorbance values will be correlated with the visual observation of pigment so we can accurately quantify the amount of pigment required to generate a detectable output. After performing reactions in bulk cytosol, the system will be transferred to GUVs to determine whether visible colour can be detected in a liposome. The module will then be handed over to be incorporated with the sensor, chassis, and hydrogel modules. 

In the future, this module can be applied to any biological device requiring a colorimetric signal output: from the detection of living entities, to analytes in aqueous samples. Other reporter enzymes can be added/substituted into the system to provide different readouts. Logic could be integrated within the system to increase the complexity of detection. 



:::{figure} ./general/Figures/Color_change_module_schematic.png
:name: fig:colour-change-module-schematic
:width: 100%

The colour change module consisting of DNA encoding a reporter enzyme (LacZ) along with an appropriate substrate is encapsulated in GUVs containing nucleus cytosol. LacZ converts the substrate into a colourful product. The GUV-encapsulated module will be integrated with a quorum sensing system before being embedded in a hydrogel to detect the presence of bacteria. 
:::




# Components

:::::{tab-set}

::::{tab-item} Cytosol
:::{table}
:name: components-cytosol

| Material | Brief description |
|----------|-------------------|
| Enzymatic reporter substrates (CPRG / catechol) | Substrates that are processed by the reporter enzyme to generate a visible colour change. |
| Nucleus cytosol | PURE prepared by b.next |

:::
::::

::::{tab-item} DNA
:::{table}
:name: components-dna

| Template | Expected Concentration Range | Sequence/status | Notes |
| :---- | :---- | :---- | :---- |
| *pT7-LacZ/XylE-T7term* | 2-4 nM | *LacZ synthesised and templates prepared. XylE to be designed.* |Low expression
| *pT7-UTR1-G10_leader_peptide-LacZ/XylE-T7term* | 2-4 nM | *LacZ synthesised and templates prepared. XylE to be designed.* |High expression

::::


::::{tab-item} Membrane
:::{table}
:name: components-membrane

| Lipid composition | Volume fraction | Notes |
| :--------- | :------- | :------- |
| POPC / Cholesterol / Liss RhodPE | 70% / 29.95% / 0.05%| Different quantities of cholesterol will be tested to assess GUV stability, and pigment leakage. Fluorescent Lipophilic dyes such as, DiD, will also be tested for membrane observation. In this case, Liss RhodPE will be replaced with POPC. 

:::
::::

::::{tab-item} Outer Solution
:::{table}
:name: components-outer

| Molecule | Expected Concentration Range | Membrane permeable?| Notes |
|----------|------------------------------|------------------------------------|-------|
| Glucose | 300 mM-1M | No | Used for density |

:::
::::

:::::



# Milestones

- **Milestone 1:** To confirm colourful pigment production in bulk Nucleus cytosol. Identify an optimal reporter/substrate pair.
    - **Risk:** LacZ contamination in Nucleus cytosol.
    - **Success Criteria:** Observe visible pigment production in bulk Nucleus cytosol reactions when provided with reporter DNA.
- **Milestone 2:** Chart absorbance kinetics of pigment production in Nucleus cytosol. Correlate an absorbance value with the visible observation of pigment.
    - **Risk:** Inaccurate kinetic data due to detection limit of platereader. Reducing concentration of substrate may result in values that are not applicable to the overall system.
    - **Success Criteria:** Acquire kinetic curves of colourful pigment production. Determine absorbance values for CPRG/catechol products at which they are visible to the naked eye. 
- **Milestone 3:** Encapsulate reporter system in GUVs.
    - **Risk:** Substrate/products interfere with vesicle generation. Encapsulation efficiency and yield of GUVs prevent visible observation of pigment.
    - **Success Criteria:** Synthesis of GUVs encapsulating entire reporter module. Stability of vesicles monitored through microscopy. Pigment generation observed by the naked-eye and quantified by a spectrophotometer.
- **Milestone 4.** Integrate Quorum sensing module.
    - **Risk:** The leak of the quorum sensing module may prevent a tight-off state producing false positive results.
    - **Success Criteria:** Colourful pigment is only generated in the presence of AHl. Characterised through spectroscopy and microscopy, and by the visible eye. 

## Immediate next step

Test LacZ contamination in Nucleus cytosol by supplementing the reaction with CPRG in the absence of DNA encoding LacZ. Acquire absorbance kinetics of colourful pigment generation in Nucleus cytosol. Correlate absorbance values of catechol and CPRG product with visible observation of pigment. Encapsulate module in GUVs and assess vesicle stability and pigment production. Once completed, the module will be handed off to Manuel Bibrowski for the integration of the quorum sensing module. Quorum sensing integration will be followed by hydrogel embedding which be taken care off by Niall Mcintyre. Once we have prepared an initial demonstration, I will collobarate further with Manuel and Niall to introduce further complexity in the system. We will consider orthogonal quorum sensing systems to activate the production of both LacZ and XylE. If possible, we will optimise the spatial patterning of GUV printing to ensure the clear detection of two signals. 

# Useful references

- Reporter enzymes characterised in PURE. [](https://doi/10.1021/acssynbio.1c00360)
- Characterisation of LacZ/GusA/XylE in lysate-based systems. [](https://doi.org/10.1039/D0RA05293K)
- XylE reporter demonstration in OnePot PURE. [iGEM EPFL 2019](https://2019.igem.org/Team:EPFL/Results)




