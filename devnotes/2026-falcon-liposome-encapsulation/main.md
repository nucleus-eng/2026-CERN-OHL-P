---
title: "Liposome encapsulation: A tractable and reproducible approach"
date: 2026-06-08
authors:
  - name: Chris Falcon
    affiliation: Department of Chemistry and Biochemistry, California Polytechnic State University, San Luis Obispo
    email: ccfalcon@calpoly.edu
  - name: Katie Drew
    affiliation: Department of Chemistry and Biochemistry, California Polytechnic State University, San Luis Obispo
    email: kdrew01@calpoly.edu
keywords:
  - liposome encapsulation
  - emulsion transfer
  - PURExpress
  - cell-free protein synthesis
  - synthetic cell
  - sfGFP
  - fluorescence microscopy
license: CC-BY-4.0
thumbnail: figures/fig1-timecourse.png
collections:
  - nucleus-contrib
id: 9e302e31-3dbb-494a-b8e3-5fc6d91ea941
---

# Overview

Liposome encapsulation is a useful method used within PURE systems to model the cellular environment of a biological cell.{sup}`1` This new synthetic cell allows researchers to understand how encapsulated biomolecules play within an artificial cellular environment. While this technique is useful, the standard methods used to encapsulate can be hard to reproduce and prove difficult to perform in inexperienced hands. We offer a very small but easily adaptable alteration to the industry standard encapsulation method that aims to address these limitations.

# Methods

## Reagents

<!-- vale nucleus.magnitude-unit-spacing = NO -->
:::{table} Reagents used in this experiment.
:label: tbl-reagents
:align: center
| Reagent | Product name | Manufacturer | Catalog no. | Price | Storage conditions | Link |
| --- | --- | --- | --- | --- | --- | --- |
| POPC | 16:0-18:1 PC 25 mg/mL | Avanti Lipids | 850457C (500 mg) | $435.00 | −20 °C | [Avanti Research](https://www.avantiresearch.com/en-gb/products/product/850457-160-181-pc-popc) |
| Liss-Rhod-PE | 16:0 Liss Rhod PE 1 mg/mL | Avanti Lipids | 810158C-1mg | $281.67 | −20 °C | [Avanti Research](https://www.avantiresearch.com/en-gb/products/product/810158-160-liss-rhod-pe) |
| Cholesterol | Cholesterol (D7) 1 EA | Avanti Lipids | A84100M | $193.72 | −20 °C | [Avanti Research](https://www.avantiresearch.com/en-gb/products/product/4100-cholesterol-d7) |
| Mineral oil | Mineral oil, mixed weight | Thermo Scientific | AC415080010 | $53.40 | RT | [Thermo Scientific](https://www.thermofisher.com/order/catalog/product/415080010) |
| Glucose | D-(+)-Glucose, 99% | Thermo Scientific | A16828-36 | $41.65 | Cool place (thanks thermo) | [Thermo Scientific](https://www.thermofisher.com/order/catalog/product/A16828.36) |
| PURExpress | PURExpress In Vitro Protein Synthesis Kit | NEB | E6800S | $295.00 | −80 °C | [NEB](https://www.neb.com/en-us/products/e6800-purexpress-invitro-protein-synthesis-kit) |
| RNase inhibitor | RNase Inhibitor, Murine | NEB | M0314S | $81.00 | −20 °C | [NEB](https://www.neb.com/en-us/products/m0314-rnase-inhibitor-murine) |
| OptiPrep | OptiPrep Density Gradient Medium | Sigma-Aldrich | D1556-250ML | $373.00 | 4 °C | [Sigma-Aldrich](https://www.sigmaaldrich.com/US/en/product/sigma/d1556) |
| DNA template | pJL1-sfGFP plasmid | — | — | — | −20 °C | — |
:::

<!-- vale nucleus.magnitude-unit-spacing = YES -->

:::{note}
pJL1-sfGFP is a self-prepared reagent. The sequence file (.gb or .dna) for this plasmid is not included in this submission — authors are encouraged to provide it alongside the DevNote for reproducibility.
:::

## Lipid-oil solution preparation

Prepare the lipid-oil mixture at least 4 h before encapsulation.

1. Add mineral oil (3 mL to 5 mL) to a clean glass vial.
2. Using a glass syringe, draw up the lipid stock and inject into the mineral oil at the correct molar ratio (70:29.95:0.05 POPC:cholesterol:Liss-Rhod-PE).
3. Vortex the mixture for 10 s in a fume hood.
4. Cover the vial with aluminum foil and place in a 55 °C dry bath for 4 h.

:::{table} Membrane lipid composition.
:label: tbl-membrane
:align: center
| Lipid | Target percentage (%) | Molecular weight | Concentration (mg/mL) | Volume to add (µL) |
| --- | --- | --- | --- | --- |
| POPC | 70 | 760.076 | 25 | 162.17 |
| Cholesterol | 29.95 | 386.66 | 50 | 17.65 |
| Liss-Rhod-PE | 0.05 | 1301.72 | 1 | 4.96 |
:::

## Outer solution

:::{table} Outer solution composition.
:label: tbl-outer
:align: center
| Component | Concentration |
| --- | --- |
| Glucose | 1320 mM |
:::

## PURE reaction setup

Label 16 tubes, one of each of the following:

a. E 1 - 4 oil emulsion
b. T 1- 4 transfer
c. L 1 - 4 liposomes

Pipette the reaction setup below into the first E tube:

150 µL reaction volume per DNA template

- 20 µL (2x 8 µL = 16 µL) will be used for quantifying protein synthesis in a plate reader
- 10 µL will be used for measuring osmolarity
- 30 µL will be used for encapsulation (per replicate)

:::{table} PURExpress mastermix composition (4-prep batch, 150 µL total).
:label: tbl-pure
:align: center
| Component | Volume for 4-prep mastermix (µL) |
| --- | --- |
| Nuclease-free H₂O | 15.1 |
| Solution A | 60 |
| Solution B | 45 |
| RNase inhibitor | 6.65 |
| pJL1-sfGFP plasmid DNA (µL)<br>Conc.: \_\_\_\_\_\_\_\_\_<br>[final conc.: 10 ng/µL] | 18.6 |
| OptiPrep | 4.65 |
| Total | 150 |
| Osmolarity | 1259 mOsm/kg |
:::

Pipette mix each reaction, then centrifuge the reaction at 5000 g (6685 rpm for tabletop centrifuges, r = 10 cm) for 10 s to 30 s to spin down bubbles in the reaction.<!-- REVIEW: highlighted in source -->

Check the osmolarity of your cytosol using a Vapor Pressure Osmometer before encapsulation.

- Pipette 10 µL of your cytosol onto the disc and press "close".
- Read and record the osmolarity.

Pipette mix the PURE solution before transferring 8 µL into two wells of a 384-well plate for kinetics quantification. Set the micropipette to 8 µL and stop at the first stop when dispensing to prevent the introduction of bubbles into the sample.

Aliquot 90 µL of the PURE mixture into the remaining 3 E tubes (30 µL per E tube)

## Encapsulation protocol

The modified and standard methods are identical except for the pipette size used to remove the oil supernatant in step 6a.

:::::{tab-set}

::::{tab-item} Modified method
:sync: method-modified

**Encapsulate PURExpress into Liposomes**

1. Add 300 µL of the glucose outer solution to each tube labeled T.
2. Add 150 µL of the lipid-oil mixture to the top of the PURE reaction in each E tube.
3. Emulsify the lipid-oil and PURE mixture by running the tube along a row of empty slots on a 1.5 mL tube rack. Run it down 40–50 times until the solution forms a stable emulsion with an even milky color.
   a. While running the tubes on the tube rack, hold the cap firmly to prevent it from coming off during vigorous mixing.
4. Slowly pipette the entire emulsion down the side of the corresponding T tube, so that the emulsion is layered on top of the glucose solution.
5. Centrifuge the T tube at 9000 g (8970 rpm for tabletop centrifuges, r = 10 cm) for 10 min at room temperature to pellet the liposomes.
   a. Arrange tubes so that hinge side is facing out taking note of where pellet will form (hinge side) after centrifugation
6. Extract the liposomes from the T tube:
   a. Remove the oil layer and lipid debris from the top (supernatant) of the T tube by gently pipetting with a **200 µL** pipette set to 100 µL. Begin at the top of the mixture and aspirate from the solution surface as the liquid level descends in the tube. Dispose of supernatant in designated container or an empty microcentrifuge tube, which can then be disposed in designated waste.
   b. Once the majority of supernatant is removed, extract liposomes by pipetting 50 µL of pellet and outer solution from tube T and transfer to the respective liposome tube L. Do not transfer the entire solution. It is important to avoid transferring the top of the solution which may contain a residual oil layer.
7. Resuspend pellet in tube L by pipetting up and down then keep tube on ice until ready for microscopy

::::

::::{tab-item} Standard method
:sync: method-standard

**Encapsulate PURExpress into Liposomes**

1. Add 300 µL of the glucose outer solution to each tube labeled T.
2. Add 150 µL of the lipid-oil mixture to the top of the PURE reaction in each E tube.
3. Emulsify the lipid-oil and PURE mixture by running the tube along a row of empty slots on a 1.5 mL tube rack. Run it down 40–50 times until the solution forms a stable emulsion with an even milky color.
   a. While running the tubes on the tube rack, hold the cap firmly to prevent it from coming off during vigorous mixing.
4. Slowly pipette the entire emulsion down the side of the corresponding T tube, so that the emulsion is layered on top of the glucose solution.
5. Centrifuge the T tube at 9000 g (8970 rpm for tabletop centrifuges, r = 10 cm) for 10 min at room temperature to pellet the liposomes.
   a. Arrange tubes so that hinge side is facing out taking note of where pellet will form (hinge side) after centrifugation
6. Extract the liposomes from the T tube:
   a. Remove the oil layer and lipid debris from the top (supernatant) of the T tube by gently pipetting with a **1000 µL** pipette set to 150 µL. Begin at the top of the mixture and aspirate from the solution surface as the liquid level descends in the tube. Dispose of supernatant in designated container or an empty microcentrifuge tube, which can then be disposed of in designated waste.
      a. Dislodge and resuspend the pellet by gently pipette mixing near the pellet. Pipet 50 µL of pellet and outer solution from tube T and transfer to the respective liposome tube L. Do not transfer the entire solution. It is important to avoid transferring the top of the solution which may contain a residual oil layer.
7. Keep tube on ice until ready for microscopy

::::

:::::

## Microscopy setup

1. Pipette ~30 µL of the liposomes from tube L into a well on a 384-well glass-bottom plate. Set the micropipette to 32 µL and stop at the first stop when dispensing to prevent the introduction of bubbles into the sample.
2. Wipe the bottom of the plate with a Kimwipe to rid the plate of any dust. Handle the plate by its sides with gloved hands to avoid dirtying the glass bottom.
3. Launch Squid software on the Cephla Microscope monitor.
4. Lower the objective on the focus knob to 0.
5. Add the plate with your sample to the viewing surface, ensuring that well A1 is in the correct spot (labeled "A1" on the microscope).
6. Click "Start Live" in the software.
7. Set live configuration to fluorescence 638 nm to visualize liposomes or 488 nm to visualize sfGFP.
8. Set exposure time to 50 ms to start. Adjust if needed (with instructor or TA guidance) to find best visualization settings.
9. Select the well you would like to view.
10. Slowly raise the stage with the focus knob. The microscope will likely focus on z ~3800.
11. Once you have focused on liposomes, go to the "laser AF" setting and press "Set Reference".
12. Under "Wellplate Multipoint" label your experiment ID with "initials.date.experiment#".
13. Select "laser AF", "fluorescence 488 nm", and "fluorescence 638 nm", then press snap image to view liposomes.

# Results

:::{figure} figures/fig1-timecourse.png
:label: fig-timecourse
:width: 90%
Time course of PURExpress encapsulation supplemented with sfGFP, measured at 488 nm and 638 nm on Cephla microscope for 240 min. The 4 wells represent modified method and standard method with replicates (MMR1–2 and SMR1–2 respectively).
:::

:::{figure} figures/fig2-mean-green.png
:label: fig-mean-green
:width: 90%
Mean green intensity of encapsulated PURE reaction over 4 hours. The left (green) bar represents fluorescence from the modified extraction method, and the right (red) bar represents fluorescence of the standard extraction method.
:::

:::::{tab-set}

::::{tab-item} Modified method fog plots
:sync: fogplot-modified

:::{figure} figures/fig3a-fogplot.png
:label: fig-fogplot-modified
:width: 90%
Fog plots of mean intensity per method over full-time course — modified method. Each individual dot represents an encapsulated PURE reaction and the intensity at which it is fluorescing.
:::

::::

::::{tab-item} Standard method fog plots
:sync: fogplot-standard

:::{figure} figures/fig3b-fogplot.png
:label: fig-fogplot-standard
:width: 90%
Fog plots of mean intensity per method over full-time course — standard method. Each individual dot represents an encapsulated PURE reaction and the intensity at which it is fluorescing.
:::

::::

:::::

:::{figure} figures/fig4-histogram.png
:label: fig-histogram
:width: 90%
Histogram representing the number of liposomes and their corresponding sizes. Left histogram: modified method; right histogram: standard method.
:::

:::{table} Measurement of mean green value
:label: tbl-results
:align: center
| Method | T = 0 h | T = 3 h | T = 5 h |
| --- | --- | --- | --- |
| Modified method replicate 1 | 24.7 | 17.3 | 16.8 |
| Modified method replicate 2 | 41.7 | 53.8 | 57.6 |
| Standard method replicate 1 | 27.2 | 32.5 | 35.4 |
| Standard method replicate 2 | 26.1 | 29.8 | 31.5 |

Samples were processed with ImageJ software. Each image was selected for highest density within well then taken at beginning middle and end of time course.
:::

Fluorescence kinetics were tracked over 4 h for both methods ({ref}`fig-timecourse`, {ref}`fig-mean-green`, {ref}`tbl-results`). Fog plots ({ref}`fig-fogplot-modified`, {ref}`fig-fogplot-standard`) show the distribution of per-liposome fluorescence intensity across replicates. Size distributions for both methods are shown in {ref}`fig-histogram`.

# Conclusions

Comparisons of modified and standard methods were performed using aliquots of same PURE reaction set up with two true replicates per method. {ref}`fig-timecourse`, {ref}`fig-mean-green`, and {ref}`tbl-results` show the density and intensity of the modified method to be greater than the standard method however reproducibility between replicates is lacking for the modified method. Both methods show similar trends of increasing intensity over time ({ref}`fig-fogplot-modified` and {ref}`fig-fogplot-standard`). However, the overall number of liposomes is seemingly much greater in the standard method ({ref}`fig-histogram`). Overall, the greater intensity of sfGFP fluorescence and liposome density seen in {ref}`fig-timecourse` points to the modified method being a suitable alternative to the standard method; however, issues stemming from reproducibility are still in question.

Due to time constraints preparation of the final tube (modified method replicate 1) had to be rushed within the lab. This caused a breaking of the lipid interface debris leading to a sizable transfer within the pipette tip and less pellet being taken along with it. The debris was removed from tube L before resuspension but unfortunately, as the results show, the replicate did not perform. In the future to showcase the ease and reproducibility of this modified approach it would be nice to have additional replicates and time dedicated solely for performing the experiment at hand.

# Resources

- CHEM 471 Engineering Synthetic Cells Laboratory Manual — Liposome Encapsulation. California Polytechnic State University, San Luis Obispo.
- [Hello World Liposomes bench protocol (v0.1.3)](https://docs.nucleus.engineering/guides/liposome-workshop/main/)
