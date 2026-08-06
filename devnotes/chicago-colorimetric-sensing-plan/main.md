---
# Ensure that this title is the same as the one in `myst.yml`
title: "[Title]"
abstract: |
    This module enables colorimetric sensing utilizing salts to induce changes in the pitch of chiral nematic hydroxypropyl cellulose.
---

# Overview

While pigment production is often the primary mechanism for visual sensing applications in synthetic biology, this method has drawbacks in the scale of production needed, stability of the pigment, and potential leakage. As a possible alternative for pigment enabled sensing, this module, within the Chicago node, will investigate colorimetric sensing utilizing structurally colored hydroxypropyl cellulose (HPC). HPC is a biodegradable, bioderived and biocompatible material which allows a wide range of applications in medicine, food packaging and other toxin sensitive fields. 

- **{ref}`fig-schematic` shows an overview of the system while key components are listed below:**
    - Hydroxypropyl cellulose (main matrix material)
    - Glutaraldehyde (crosslinker)
    - Hydrochloric acid (catalyst)
    - Lithium chloride (blue-shifting salt)
    - Lithium iodide or other (red-shifting salt)

- **Required equiptment:**
    - Planetary mixer
    - Drying oven with humidity control
    - Reflection spectrometer capapble of conducting measurements with diffuse light

- **Anticipated performance metrics:**
    - We anticipate having the capability to detect 0.1M salt concentration differences

    - We anticipate reading of the gel to be possible 30 minutes after analyte exposure

- **Further applications/research:**
    - HPC is already touted as an ideal sensor material for biosensors and this system will be a demonstration of HPC not just as a potential sensor material but in a functioning sensor, enabling further development of it in biological applications.

:::{figure} general/HPC-drawing.png
:name: fig-schematic
:width: 50%

HPC Colorimetric Sensor Overview
:::

%myst md documentation for available commands


# Milestones

- **Milestone 1.** Verify diffusion of small unilamellar vesicles (SUVs) containing salt of interest into crosslinked HPC and quantify colorimetric response to vessicle rupture.
    - **Risk.** The biggest risk is that the concentrations of salt that vesicles are able to contain will not be able to produce an observable colorimetric change. Migitagion for this would include testing larger vesicles or higher concentrations of vesicles. 
    - **Success Criteria: How will you know if you succeed** Success will be measured by colorimetric readout and sensing a change with the addition of salt. 
- **Milestone 2.** Diffusion of salt after release within PEGDA hydrogels from DevCells. 
    - **Risk.** The biggest risk is that the DevCells cannot contain the necessary salt concentrations. A potential mitigation strategy for this would be to have one population of cells containing salts and another that produce a protein to rupture those cells utilizing cell free systems. 
    - **Success Criteria: How will you know if you succeed**  Sucess criteria is equivalent for both milestones. 

## Immediate next step

The immediate next step is to verify the acid we will be utilizing as a catalyst. This will involve a crosslinking study to determine how each sample survives in a solvated system and ensuring color visibility even within this solvated system. 

# Useful references

- Salt Addition Effects on Mesophase Structure and Optical Properties of Aqueous Hydroxypropyl Cellulose Solutions. [](https://doi.org/10.1295/polymj.34.149)
-  Visual Appearance of Chiral Nematic Cellulose-Based Photonic Films: Angular and Polarization Independent Color Response with a Twist. [](https://doi.org/10.1002/adma.201905151)
- Unraveling the Governing Mechanisms Behind the Chiral Nematic Self-Assembly of Cellulose-Based Polymers [](https://doi.org/10.1021/acs.chemmater.3c01904)

