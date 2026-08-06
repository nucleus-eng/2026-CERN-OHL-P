---
# Ensure that this title is the same as the one in `myst.yml`
title: "[Title]"
abstract:
 This project develops a tunable, pH-responsive liposome sensor that couples a pH-sensitive ssDNA/trigger ssDNA pair to a linear toehold switch, enabling protein expression only when environmental pH drops to ~6.5. By integrating DNA components, PURE cell-free expression, and POPC–cholesterol vesicles, the system seeks to achieve robust and detectable colorimetric output in both bulk and hydrogel-embedded formats despite the inherent pH limitations of cell-free reactions.
---

# Overview

This module builds a pH-responsive sensor where a slightly acidic pH induces cell-free protein production of colorimetric enzymes that induce a colorimetric response.
Numerous DevCell-based sensors have been developed, but not until recently pH-responsive sensor had not been developed. Acidic pH sensing is important with significant physiological relevance, as inflammatory tissue and cancer microenvironment exhibit slightly acidic tissue pH (~pH 6.4-6.8). 

The pH sensor design is based on previous work by [](https://doi.org/10.1101/2025.11.16.688650). The sensor, {ref}`fig-schematic`, consists of 3 components: 
1. pH-Responsive single-strand DNA (ssDNA)
2. Trigger ssDNA
3. Linear toehold switch construct

Toehold switch RNA prevents translation of colorimetric enzymes, catecholase or β-galactosidase, until trigger ssDNA binds to the toehold. Trigger ssDNA is bound to pH-responsive ssDNA until pH drops to pH 6.5. So, an acidic pH induces the expression of colorimetric enzymes, which leads to a colorimetric response in the presence of catechol or CPRG (chlorophenol red-β-D-galactopyranoside), substrates for catecholase or β-galactosidase, respectively.
We anticipate the detection pH 6.5 (+/- 0.1) within 1 hour with a colorimetric response visible by a smartphone camera.

This module will allow others to sense pH change for various applications, including environment detection and diagnotics. This module can also be coupled to deliver other protein products for either environmental remediation or drug delivery.


:::{figure} general/pH sensor schematic.png
:name: fig-schematic
:width: 75%

Schematic of DevCell pH sensor: from pH drop to colorimetric enzyme production to colorimetric response.
:::




# Components

:::::{tab-set}

::::{tab-item} Critical Materials
:::{table}
:name: components-cytosol

| Material | Brief description | Manufacturer | Item # | Notes | Link |
|----------|-------------------|--------------|--------|-------|------|
| T7-linear toehold-[LacZ/XylE]-T7term | A reporter enzyme under T7 promoter system. | N/A | N/A | N/A | N/A |
| Enzymatic reporter substrates (CPRG / Catechol) | Substrates that are processed by the reporter enzyme to generate a visible color change. | CPRG: Roche / Catechol: TCI America | CPRG: 10884308001 / Catechol: P031725G | Catechol is a phenolic compound. | N/A |
| POPC | Phospholipid for GUV production. | Avanti Polar Lipids | A80557C/0200/4C11M | N/A | https://www.avantiresearch.com/en-gb/products/product/850457-160-181-pc-popc |
| Cholesterol | Membrane components for GUV production. | Sigma-Aldrich | C3045-5G | N/A | https://www.sigmaaldrich.com/US/en/product/sigma/c3045 |
| Gramicidin A | Proton membrane channel for pH sensing | Sigma-Aldrich | 50845-5MG | Stock prepared in DMSO and stored at -80C | https://www.sigmaaldrich.com/US/en/product/sigma/50845 |
| Nucleus Cytosol | Cell-free expression system | b.next | N/A | N/A | N/A |

:::
::::

::::{tab-item} DNA
:::{table}
:name: components-dna

| Template | Expected Concentration Range | Sequence/status | Notes |
| :---- | :---- | :---- | :---- |
| *T7-toehold-LacZ-T7term* | 2 nM | *Designed*  | |
| *T7-toehold-XylE-T7term* | 2 nM | *Designed* |  |
| *trigger ssDNA* | 4.8 µM | Synthesized  |  |
| *pH responsive ssDNA* | 14.4 µM | Synthesized   |  |

:::
::::


::::{tab-item} Membrane
:::{table}
:name: components-membrane

| Lipid | Volume fraction | Notes |
| :---- | :---- | :---- |
| *POPC* | **89.9 %** | |
| *Cholesterol*  | **10 %** |  |
| *Rhod-PE* | **0.1%** |  |

:::
::::

::::{tab-item} Outer Solution
:::{table}
:name: components-outer

| Molecule | Expected Concentration Range | Membrane permeable? Which membrane? | Notes |
|----------|------------------------------|------------------------------------|-------|
| Feeding solution | Cytosol concentrations | Potentially | Used to prevent diffusion of small molecule components |

:::
::::

:::::



# Milestones

- **Milestone 1.** Demonstrate pH-responsive colorimetric response in bulk reaction.
    - **Risk.** Leaky expression of colorimetric enzyme. Titrating pH-responsive ssDNA and trigger ssDNA for a robust response to a narrower (less than 0.5 pH) pH range.
    - **Success Criteria:** Robust colorimetric response (quantified using metrics developed by other Chicago node colleagues).
- **Milestone 2.** Demonstrate sensor response when encapsulated in DevCells.
    - **Risk.** Limited colorimetric response. Optimize cell-free expression through varying DNA concentration. Ensure substrate diffuses through the membrane by tuning the membrane permeability.
    - **Success Criteria: Robust, repeatable, and visible colorimetric response.** 
- **Milestone 3.** Integrate DevCell sensors with photopatterned hydrogel.
    - **Risk.** Limited colorimetric response. DevCell concentration in the hydrogel will be maximized for more robust expression. Potentially including feeding solution outside to maximize cell-free expression.
    - **Success Criteria. Robust, repeatable, and visible colorimetric response.** 

## Immediate next step

Both linear toehold constructs will be purchased. Upon arrival, the toehold constructs with or without trigger strands will be tested in bulk with Nucleus cytosol. The output will be quantified with SDS-PAGE (via FluoroTect), Bradford assay, and by quantifying colorimetric response following completion of bulk expression.

# Useful references

- pH-responsive synthetic cells for controlled protein synthesis and release. [](https://doi.org/10.1101/2025.11.16.688650)
