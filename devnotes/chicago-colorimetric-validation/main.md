---
# Ensure that this title is the same as the one in `myst.yml`
title: "Validation of colorimetric reporter sensors in Nucleus Cytosol"
abstract: | 
  This module covers the design and in vitro validation of the sensor and reporter combinations that are going to be used in the final Chicago node demonstration.
---

# Overview

This module is focused on completing the cytosol for the Chicago DevCells. It involves testing all possible combinations of the sensors and reporters we are considering using and identifying successful combinations for final integration. Successful combinations will be sensors that switch on with at least 2-fold signal improvement and do not have considerable leak.
This module will reveal potential complications from the theophylline riboswitch, which may cause leak depending on internal ribosome binding sites in the reporter of choice. It may also reveal complications in LaZ compatibility with PURE, as the large LacZ gene size will use up more resources than the GFP and aHL genes that have been demonstrated at b.next.


- **Describe how the Module works {ref}`fig-schematic`, its mechanism, and how the components relate to each other**
    - Sensor and reporter combination DNA constructs
    - Ligands of interest
    - Enzymatic reporters, produced through PURE
      
- With the introduction of the corresponding ligand, we're looking for at least 2-fold signal increase and max signal within two hours, which is in line with Lucks Lab's previous colorimetric sensors.

- We do not have a specific target for leak because this will depend on the visibility of the reporter in the cell and gel matrix. A level of leak that is visible in bulk may be invisible in the gel.

- This module will enable the other node members to successfully deploy the sensors in b.next cytosol for encapsulation. Since other node members have not used colorimetric reporters, this node will also explain how these reporters are characterized differently from fluorescent reporters, and how the longevity of the reporter differs.

:::{figure} modulefigure.png
:name: fig-schematic
:width: 50%

Multiple sensor and reporter combinations will be used to produce a unique colorimetric enzyme for each ligand :::

:::


# Components



:::::{tab-set}

::::{tab-item} Cytosol
:::{table}
:label: components-cytosol

| Material | Brief description | Notes |
|----------|-------------------|-------|
| Chlorophenol-red | Substrate converted by LacZ to produce a color change | N/A |
| Catechol | Substrate converted by XylE to produce a color change | Catechol is a phenolic compound. |
| TetR | Repressor protein for the tetracycline sensors. | Purified from MedChemExpress|
| b.next cytosol | PURE prepared by b.next | N/A |

:::
::::

::::{tab-item} DNA
:::{table}
:label: components-dna

| Template | Expected Concentration Range | Sequence/status | Notes |
| ---- | ---- | ---- | ---- |
| *pT7-TetO-XylE-T7term*| 1-10 nM | Awaiting from Twist |  |* | 1-10 nM | Awaiting from Twist  |  
| *pT7-TetO-LacZ-T7termm* | 1-10 nM | Awaiting from Twist |  
| *pT7-Theophylline-LacZ-T7term* | 1-10 nM | Awaiting from Twist  |  
| *pT7-TetO-GFP-T7term* | 2-4 nM | Synthesized and stocked  |  
| *pT7-Theophylline-GFP-T7term* | 1-10 nM | Awaiting from Twist  |  
:::
::::

:::::



# Milestones

- **Milestone 1.** Testing whether b.next PURE works in our lab environment with our constitutive GFP reporter.
    - **Risk.** The biggest risk is the reaction may not work, which may be due to mishandling during shipping from b.next.
    - **Success Criteria: We will compare our reaction kinetics to b.next and use a fluorescein standard to also confirm that we reach similar levels of protein production**
- **Milestone 2.** Assessing whether sensors switch on and off.
    - **Risk.** The biggest risk is the theophylline sensor functions independently of ligand, which can be mitigated by DNA design to ensure no internal ribosome binding sites in the reporters we are using.
    - **Success Criteria: We will look for at least 2-fold signal change within the first two hours of the reaction.** 


## Immediate next step

The first experiment will be to test constitutive GFP sensing in PURE, which is new to our lab, alongside testing each sensor construct at no ligand and high ligand concentrations to assess whether the sensors turn on and off. We expect PURE to work seamlessly in our lab given the simple setup and highly optimized composition by b.next, whereas the sensors may or may not work especially for theophylline which has not been demonstrated in our lab.  

# Useful references

- Mansy lab theophylline construct we will use for our sensor. [](https://doi.org/10.1038/ncomms5012)

