---
# Ensure that this title is the same as the one in `myst.yml`
title: "GUV Immobilisation"
abstract: |
  This process describes the use of DSPE-Biotin in the GUV membrane to cause immobilisation on a neutravidin-coated plate, for the purposes of microscopy. 3%-by-mass appears to be the lower limit for total (or near-total) immobilisation, whilst lower percentages allow for some movement, or the movement of smaller GUVs. Whereas non-immobilised GUVs migrate from frame or leave the visualised plane when additional substrate is added to a well, this process facilitates single-cell resolution of synthetic cells across long protocols or across the addition of other outer solution components for real-time analysis.
---

# Overview

Over the course of a synthetic cell experiment,  GUVs tend to migrate out of frame, resulting in an "after" image containing different GUVs than a "before" image. This can limit the observation of a visual process occurring, such as a colour change. Additionally, an experiment may require the addition of some substrate to a GUV population whilst it is on the microscope to observe a change - for example, if studying permeation of a substrate or an enzymatic reaction on the membrane. For such protocols, the ability to study the same GUV over the course of an experiment offers a broader scope for data collection. Indeed, if the 

The investigations described here will inform design choices within the rest of the London Node, particularly reporter molecule choice and membrane composition. The relevant small molecules to be investigated will be a range of colourimetric substrates that can be released into a broader hydrogel (CPRG, catechol etc.), and the quorum-sensing molecule acyl homoserine lactone (AHL). The idea is to verify that AHL will diffuse into a GUV at a sufficient rate to cause a timely colour change, and that any enclosed substrate does not leak out of the GUV before the colour change is triggered. Following this, the inclusion of a pore-forming protein will allow for distribution of a coloured dye throughout a hydrogel if this is required to produce more distinct colour change.


- **The experimental setup:**
    - GUVs containing 1% biotin will be immobilised on neutravidin-coated wells. These GUVs will encapsulate either enzyme or substrate, the counterpart of which will be added to the outer solution before confocal microscopy for single-cell resolution of colour change over time.
    - These data can then be plotted and analysed using the Nucleus CDK to compare kinetics of membrane permeability to these small molecules, leading to different permeability rates in cm•s {sup}`-1`. Ideally these will be as low as possible for passive permeation of substrates through the membrane. If the "out" rate is too high, membrane composition and substrate molecule can be altered.
    - This same setup will also be used to assess the permeation with added purified (and in time, expressed in Nucleus cytosol) pore forming proteins such as alpha hemolysin to release substrate into the wider hydrogel, if colour change in GUVs alone does not produce a distinct enough colour change.

- This Module will provide useful fundamental characteristics, or indeed to anyone interested in releasing/retaining small molecules from/in GUVs. This will be fundamental in all applications of DevCells in which they communicate with eachother or interface with life.

:::{figure} general/modulefigure.jpg
:name: fig-schematic
:width: 50%

A graphical summary of the two internal conditions of the GUVs and their expected diffusion kinetics.
:::




# Components



:::::{tab-set}


::::{tab-item} DNA
:::{table}
:name: components-dna

| Template | Expected Concentration Range | Sequence/status | Notes |
| :---- | :---- | :---- | :---- |
| N/A | N/A | N/A | |

:::
::::


::::{tab-item} Membrane
:::{table}
:name: components-membrane

| Lipid | Volume fraction | Notes |
| :---- | :---- | :---- |
| *POPC* | **as required** |  |
| *Cholesterol*  | **as required** |  |
| *DSPE-PEG(2000)-Biotin* | **3% by mass** |  |

:::
::::

::::{tab-item} Outer Solution
:::{table}
:name: components-outer

| Molecule | Expected Concentration Range | Membrane permeable? Which membrane? | Notes |
|----------|------------------------------|------------------------------------|-------|
| Glucose | As required | No |  |

:::
::::

:::::



# Milestones

- **Milestone 1.** Successful experimental setup
    - **Risk.** GUVs are not sufficiently immobilised or are too closely packed to be individually examined. Mitigation by dilution or inclusion of more/less biotin-PC.
    - **Success Criteria: How will you know if you succeed** GUVs can be easily individually tracked.
- **Milestone 2.** Successful diffusion screening of substrates. 
    - **Risk.** Lack of T=0 data points. May need a more advanced setup to mitigate. Under development.
    - **Success Criteria: How will you know if you succeed** Rates calculated in cm•s {sup}`-1`.
- **Milestone 3.** Cell-free production of pore-forming proteins and addition to permeation experiments.
    - **Risk.** Pore formation causes egress of substrate too quickly for rate to be calculated.
    - **Success Criteria: How will you know if you succeed** Rates calculated in cm•s {sup}`-1`.


## Immediate next step

First thing to be done is piloting the biotin-GUV immobilisation on the neutravidin slides and assessing to how much immobilisation this actually leads, whether biotin-lipid proportion needs to be changed, whether GUVs are too densely arrayed.

# Useful references

- Shetty, S. et al. (2021) ‘Directed Signaling Cascades in Monodisperse Artificial Eukaryotic Cells’. [](10.1021/acsnano.1c04219)
- Chalmeau, J. et al. (2011) ‘Α-hemolysin pore formation into a supported phospholipid bilayer using cell-free expression’. [](10.1016/j.bbamem.2010.07.027. )

