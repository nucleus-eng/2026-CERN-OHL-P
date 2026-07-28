---
# Ensure that this title is the same as the one in `myst.yml`
title: Toehold switch-enabled translation regulation verified with Nucleus Cytosol
abstract: |
  These results are part of preliminary testing for the pH-responsive DevCell module conducted during the DevCell Kickoff workshop. Using Nucleus Cytosol, the toehold switch enabled translation regulation of pHtdGFP in the presence of trigger ssDNA.
---

# Introduction 
As part of the development for the pH-responsive DevCell module for the Chicago node, the Liu lab conducted a brief test to validate the toehold switch system in Nucleus Cytosol. The specific toehold switch used in this test is published in [](https://doi.org/10.1101/2025.11.16.688650), and is originally developed for PUREfrex2.0. This preliminary test was conducted at neutral pH, and pH-responsive protein expression was not tested. 

# Results
This preliminary test demonstrated that, using Nucleus Cytosol, the toehold-pHtdGFP linear DNA template was able to produce toehold pHtdGFP RNA and induce pHtdGFP expression gated by the presence of the trigger ssDNA. This preliminary test followed standard protocol for bulk reactions using Nucleus Cytosol (`pOpen-deGFP` plasmid concentration is 3 nM), and the toehold-pHtdGFP linear DNA template and trigger ssDNA concentrations are 2 nM and 4.8 nM, respectively, following those used in [](https://doi.org/10.1101/2025.11.16.688650). For each condition, three identical 10-μL reactions were incubated for 6 hours at 37 °C in a plate reader. The composition for each reaction is provided in {ref}`reaction-composition`.

:::{table} Experiment conditions
:name: reaction-description

| **Name** | **Description** |
| --- | --- |
| Cytosol Positive Control | Control Cytosol reaction expressing deGFP using `pOpen-deGFP` construct |
| toehold-pHtdGFP + trigger ssDNA | DNA template producing toehold-pHtdGFP RNA mixed with trigger ssDNA |
| toehold-pHtdGFP | DNA template producing toehold-pHtdGFP RNA without trigger ssDNA  |

:::

:::{table} Reaction composition
:label: reaction-composition
:align: center
| Component | Stock Concentration | Final concentration | Cytosol Positive Control [µL] | toehold-pHtdGFP + trigger ssDNA [µL] | toehold-pHtdGFP [µL] |
|---|---|---|---|---|---|
| SMix* | 3.33x | 1x | 10.5 | 10.5 | 10.5 |
| PMix | 15 mg/mL | 1.80 mg/mL | 4.2 | 4.2 | 4.2 |
| Ribosomes | 10 µM | 1.8 µM | 6.3 | 6.3 | 6.3 |
| tRNA | 35 mg/mL | 3.5 mg/mL | 3.5 | 3.5 | 3.5 |
| pOpen-deGFP DNA template | 124 nM | 3 nM | 0.85 | 0 | 0 |
| toehold-pHtdGFP DNA | 40 nM | 2 nM | 0 | 1.75 | 1.75 |
| trigger ssDNA | 100 nM | 4.8 nM | 0 | 1.68 | 0 |
| RNAse Inhibitor | 40000 U/mL | 2000 U/mL | 1.75 | 1.75 | 1.75 |
| Water |  |  | 7.9 | 5.32 | 7 |
| **Total mastermix volume [µL]** |  |  | **35** | **35** | **35** |
| **Reaction Volume × No. of replicates** |  |  | 10 µL × 3 | 10 µL × 3 | 10 µL × 3 |
:::
*SMix contains Mg-acetate and provides 8 mM final Mg-acetate concentration in the reaction.

:::::{tab-set}
::::{tab-item} Kinetics
:::{figure} ./experiments/20251212-Samuel-triggerDNA/kinetic.png
Kinetics of cell-free expression over time quantified via GFP fluorescence intensity.
:::
::::

::::{tab-item} Endpoint
:::{figure} ./experiments/20251212-Samuel-triggerDNA/endpoint.png
Endpoint GFP fluorescence intensity after a 6-hr incubation at 37 °C.
:::
::::
:::::

# Conclusion and Future Steps

This preliminary test shows that the toehold switch system is compatible with Nucleus Cytosol. Further testing of Nucleus Cytosol at acidic pH levels (~pH 6-6.5) would be needed to fully validate the compatibility of Nucleus Cytosol for the proposed pH-responsive DevCell module.
