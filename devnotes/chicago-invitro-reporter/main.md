---
# Ensure that this title is the same as the one in `myst.yml`
title: "[Title]"
abstract: |
  The deployment of developer cells necessitates reporters that can produce robust and interpretable signals. Toward this goal, I plan to develop a methodology to test and assess the functionality of genetically encoded reporter proteins for use in the nucleus cytosol module.
---

# Overview

We have identified two potential types of genetically-encodable signals for integration. The first are protein-based outputs, where each increase in signal corresponds to a discrete amount of protein produced. These are signals like fluorescent proteins or membrane pores, where changes in sample fluorescence or cytosolic composition are tied directly to the concentration/number of proteins. The other are enzymatically driven outputs, where the amount of protein drives the kinetics or rate of change in the system. This module seeks to develop robust and interpretable signals that can be generated in the nucleus cytosol and can be ported into sensing modules.

For proper deployment, the signal must be interpretable through the hydrogel matrix at accessible concentrations of protein in the cytosol. We are investigating the β-galactosidase (LacZ) and a catechol-2,3 dioxygenase (C23DO) due to their previous implementations in a cell-free context. We will use GFP as a standard benchmark and a way to easily show protein production in bulk reactions and encapsulated in artificial cells. We hope that this information will provide useful benchmarks for those considering the integration of colorimetric readouts from artificial cells encapsulated in hydrogel matrices.

:::{figure} general/Module_1.png
:name: Module_1_schematic
:width: 75%

Plate reader assay for purchased or cell-free synthesized protein readouts.
:::




# Components

:::::{tab-set}

::::{tab-item} Cytosol
:::{table}
:name: components-cytosol

| Material | Brief description | Notes |
|----------|-------------------|-------|
| pT7-[LacZ/XylE]-T7term | A β-galactosidase enzyme under the T7 promoter system. | N/A |
| pT7-[C23DO]-T7term | A Catechol-2,3 dioxygenase enzyme under the T7 promoter system. | N/A |
| pT7-[GFP]-T7term | A green fluorescent protein under the T7 promoter system. | N/A |
| Enzymatic reporter substrates (CPRG / Catechol) | Substrates that are processed by the reporter enzyme to generate a visible color change. | Catechol is a phenolic compound. |
| b.next cytosol | PURE prepared by b.next | N/A |

:::
::::

::::{tab-item} DNA
:::{table}
:name: components-dna

| Template | Expected Concentration Range | Sequence/status | Notes |
| :---- | :---- | :---- | :---- |
| *pT7-LacZ-T7term* | 0.01-10 nM | Design incoming | DNA concentration dependent on enzyme kinetics |
| *pT7-C23DO-T7term* | 0.01-10 nM | Design incoming  | DNA concentration dependent on enzyme kinetics |
| *pT7-sfGFP-T7term* | 7.5 nM | Midi-prepped | DNA concentration based on historic concentration |

:::
::::


::::{tab-item} Membrane
:::{table}
:name: components-membrane

| Lipid | Volume fraction | Notes |
| :---- | :---- | :---- |
| *POPC* | **66.6 %** | Order POPC |
| *Cholesterol*  | **33.3 %** |  |
| *Liss RhodPE* | **0.1 %** |  |

:::
::::

::::{tab-item} Outer Solution
:::{table}
:name: components-outer

| Molecule | Expected Concentration Range | Membrane permeable? Which membrane? | Notes |
|----------|------------------------------|------------------------------------|-------|
| Glucose | 1.14 M | Yes | Used for density and osmolarity balance |
| Feeding solution | Cytosol concentrations | Maybe | Used to prevent concentration gradients across membranes |

:::
::::

:::::



# Milestones

- **Milestone 1.** Implement LacZ and C23DO plate reader assays in bulk cell-free reactions. Benchmark against purified enzymes or spent reactions.
    - **Risk.** LacZ is present in small amounts in the B.Next Cytosol which converts the substrate to a colored dye. LacZ may also be difficult to express in the Nucleus cytosol.
    - **Success Criteria: Interpretable signal is present after 30 minutes. There is a difference between no reporter DNA and reporter DNA conditions.**
- **Milestone 2.** Test how encapsulation in GUVs affects the kinetics of enzymatic turnover.
    - **Risk.** Small molecule dyes are not membrane-permeable. We can get around this by encapsulating the small-molecule dyes with the enzymes.
    - **Success Criteria: Demonstration of enzymatic reporters encapsulated in a liposome with differences between no reporter DNA and reporter DNA conditions.** 
- **Milestone 3.** Send liposomes expressing LacZ and C23DO to the hydrogel team for embedding in a hydrogel.
    - **Risk.** We can send encapsulated spent reactions or encapsulate the colored molecules to send to the hydrogel team.
    - **Success Criteria: Color change is interpretable through the hydrogel matrix. There is a difference between no reporter DNA and reporter DNA conditions.** 

## Immediate next step

I will order the LacZ construct and try to run an enzymatic assay with CPRG and X-Gal with and without the LacZ construct to ensure minimal basal turnover of either substrate.

# Useful references

- Use of the C23DO enzyme downstream of a fluoride riboswitch for a colorimetric readout. [](https://www.science.org/doi/10.1126/sciadv.add6605)
- LacZ colorimetric readout using PURE cell-free protein synthesis. [](https://pubs.acs.org/doi/10.1021/acssynbio.1c00360)
- aHL synthesized using a cell-free system as a way to secrete small molecules from vesicles. [](https://pubs.acs.org/doi/abs/10.1021/acssynbio.8b00435)

