---
abstract: |
   We validated that a biosensor for theophylline switches on with the addition of 1.5 mM theophylline in Nucleus Cytosol, resulting in a faster conversion of CPRG from a yellow to red product through the production of LacZ from the biosensor.
---

# Overview

The translational theophylline riboswitch controls expression of the downstream expression platform in response to theophylline, a xanthine derivative. This sensor uses a synthetic theophylline riboswitch designed by [Lynch and Gallivan](https://doi.org/10.1093/nar/gkn924) and has since been demonstrated in several encapsulated systems.

In this work, the theophylline riboswitch has been encoded upstream of a LacZ reporter. The resulting biosensor is then added to a Nucleus Cytosol reaction supplemented with chlorophenol red-β-D-galactopyranoside (CPRG), which is converted from yellow into a red product by LacZ.

# Results

Comparing the absorbance at 570 nm over time demonstrates that the sensor is able to convert CPRG from yellow to red faster in the presence of 1.5 mM theophylline in standard Nucleus Cytosol conditions with 5 nM of sensor DNA. For each condition, a 10 µl reaction was assembled with 0.6 mg/ml CPRG and incubated at 37 °C in a platereader. 

:::{table} Experiment conditions
:name: reactions

| Condition | Description |
| --- | --- |
| - theophylline  | Control sensor reaction without theophylline |
| + 1.5 mM theophylline  | Sensor reaction with 1.5 mM theophylline |

:::



:::{table} Reaction composition
:label: reaction-composition
:align: center

| Component | Stock Concentration | Final concentration | - theophylline [µL] | + 1.5 mM theophylline [µL] |
|---|---|---|---|---|
| SMix | 3.33x | 1x | 3 | 3 | 
| PMix | 15 mg/mL | 1.80 mg/mL | 1.2 | 1.2 | 
| Ribosomes | 10 µM | 1.8 µM | 1.8 | 1.8 | 
| tRNA | 35 mg/mL | 3.5 mg/mL | 1 | 1 | 
| pT7-theophylline-LacZ (pMN066) DNA template | 49.55 nM | 5 nM | 1 | 1 | 
| CPRG | 10 mg/mL | 0.6 mg/mL | 0.6 | 0.6 |
| Theophylline | 10 mM | 1.5 mM | 0.95 | 0.95 | 
| RNAse Inhibitor | 40000 U/mL | 2000 U/mL | 0.5 | 0.5 | 
| Water |  |  | 0.54 | 0 | 

:::

:::{figure} ./experiments/pT7_theo_lacZ.png
:label: fig:theo_lacZ
:width: 75%
Kinetics for colorimetric conversion of CPRG into a red product.
:::


# Conclusion and Future Steps

This preliminary test shows that the theophylline riboswitch with a LacZ reporter is compatible with Nucleus Cytosol. Encapsulation of the sensor will inform whether the DNA template concentration should be modified to improve extent of conversion or increase the time to leak in the - theophylline condition.

# Bill of Materials

## Critical Materials

| Reagent | Product Name | Manufacturer | Part # | Price | Storage Conditions | Link |
|---|---|---|---|---|---|---|
| Cytosol | Nucleus Cytosol | b.next | N/A | N/A | -80C | N/A |
| CPRG | Chlorophenol red-β-D-galactopyranoside| Roche | 10884308001 | $160 | -20C in water at 10 mg/ml | https://www.sigmaaldrich.com/US/en/product/roche/10884308001 |
| Theophylline | Theophylline, ≥99% (HPLC), powder| Sigma-Aldrich | T1633 | $34.6 | Prepared fresh at 10 mM in water | https://www.sigmaaldrich.com/US/en/product/sigma/t1633?srsltid=AfmBOooXyXrNfmCDlKEsxtiHbE7P5z-FzHCoJ2cL0aF2H_XgVCikS_0B |