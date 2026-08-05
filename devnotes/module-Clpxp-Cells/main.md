---
abstract: |
 The Developer Cell Control Module integrates the ATP-dependent ClpXP protease complex to enable programmable post-translational regulation within PURE-based systems. In this DevNote, we reconstitute and evaluate ClpXP-mediated degradation of ssrA-tagged target proteins in both bulk reactions and liposome-encapsulated synthetic cells. Using combinations of purified protein components and DNA templates supplemented with PURE, we demonstrate selective and energy-dependent degradation of target substrates in synthetic cells. 
---


# Overview

The [Control Module](https://devnotes.nucleus.engineering/articles/clpxp-module-plan) of the [Developer Cell](https://devnotes.bnext.bio/articles/developer-cell-introduction) is dedicated to enabling precise, time-resolved control of protein expression within synthetic minimal systems, particularly those based on the PURE system. Please refer to [Control Module](https://devnotes.nucleus.engineering/articles/clpxp-module-plan) for Module overview and background information. 

In this DevNote, we performed the degradation of the protein targeted with ssrA tag by ClpX and ClpP proteases in both bulk reactions and encapsulated in liposomes. We tested different combinations of purified proteins and DNA constructs with addition of PURE system to verify the target protein degradation. 

:::{figure} ./general/control-module.png
:name: fig:scheme
:align: center
:width: 65%

Illustration of the ClpXP protein degradation control module in the [Developer Cell](https://devnotes.nucleus.engineering/articles/developer-cell-introduction), with other modules grayed out.
:::


# Exprimental Design

The goal is to demonstrate degradation of the GFP-ssrA protein by the AAA+ ATPase ClpX and the tetradecameric peptidase ClpP, as well as our ability to tune the extent of degradation. To achieve this, we show that GFP tagged with the ssrA sequence can be efficiently degraded either by purified ClpXP proteins or by ClpXP complexes expressed directly from DNA templates in the PURE system. We also examine the reverse configuration, in which GFP-ssrA is expressed using the PURE system and ClpXP is supplied in purified form, confirming that protein expression and degradation can be independently controlled. Importantly, all experiments are performed both in bulk reactions and in synthetic cells formed by liposome encapsulation. Because the reaction dynamics differ significantly between bulk and encapsulated environments, the concentrations of DNA templates and purified proteins must be fine-tuned separately for each context. We further explore tuning by combining two DNA constructs in PURE reactions together with a purified protein component. The combinations of DNA templates and purified proteins used in each experiment or condition are listed below.

### Bulk Reactions:


:::{table} This DevNote describes 3 bulk reaction experiments that test combinations of Control Module components. V = present in experiment; X = not present in experiment. 
| **Experiments** | **Purified ClpX** | **Purified ClpP** | **Purified GFP-ssrA** | **ClpP DNA** | **GFP-ssrA DNA** | **ClpX DNA** | **Sucrose** | **Optiprep** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Experiment 1 | V | V | X | X | V | X | X | V |
| Experiment 2 | V | V | X | X | V | X | V | X |
| Experiment 3 | X | X | V | X | X | V | V | V |

:::


### Liposomes:
:::{table} This DevNote describes 3 liposome samples that test combinations of Control Module components. V = present in experiment; X = not present in experiment. 

| **Samples** | **Purified ClpX** | **Purified GFP-ssrA** | **ClpX DNA** | **ClpP DNA** |
| --- | --- | --- | --- | --- |
| Liposomes (ClpXP - 2DNAs) | X | V | V | V |
| Liposomes (ClpXP - 1DNA) | V | V | X | V |
| Liposomes (ClpXP - Control) | X | V | X | X |
:::

## DNA Constructs and Purified Proteins

All DNA constructs are designed to be used in PURE reactions for protein expressions:

| **DNA Constructs** | **Description** | 
| --- | --- |
| pOpen-pT7-ClpP-CHis | Express ClpP protein in the pOpen plasmid |
| pOpen-pT7-deGFP-ssrA | Express GFP protein wtih ssrA tag in the pOpen plasmid |
| pOpen-pT7-ClpX-CHis | Express ClpX protein in the pOpen plasmid |
| Linear pT7-deGFP-ssrA | Express deGFP protein wtih ssrA tag using linear DNA |
| Linear pT7-deGFP |Express deGFP protein using linear DNA |

All purified proteins are ordered from GenScript:

| **Proteins** | **Description** |
| --- | --- |
| ClpX | Purified ClpX protein expressed using pET30a plasmid |
| ClpP | Purified ClpP protein expressed using pET30a plasmid |
| deGFP-ssRA | Purified GFP protein wtih ssrA tag expressed using pET30a plasmid |

## Materials

| **Product** | **Brand** | **Catalog No.** |
| --- | --- | --- | 
| PURExpress® In Vitro Protein Synthesis Kit | New England Biolabs | E6800L | 
| 16:0-18:1 PC (POPC) | Avanti Research | 850457C | 
| cholesterol (plant) | Avanti Research | 700100P |
| 18:1 Liss Rhod PE | Avanti Research | 810150C |
| D-(+)-Glucose | Sigma Aldrich | 000455143 | 
| Sucrose | Sigma Aldrich | 84097 | 
| OptiPrep | Serumwerk | 00124 | 
| Mineral Oil | Sigma Aldrich | M5904 | 


# Protocol

## Preparation of PURE bulk reactions:

::::{tip} Experiment 1
:class: simple
:class: dropdown
:icon: false

:::{table}
:label: tbl-exp1
| **Component** | **Sample 1** | **Sample 2** | **Sample 3** | **Control** |
| --- | --- | --- | --- | --- |
| Purified deGFP-ssrA (41.2 uM)  | 0.5 | 0.5 | 0.5 | 0.5 |
| pOpen-pT7-ClpP-cHis (100 nM) | 0.5 | 0.5 | 0.5 | 0 |
| Purified ClpX (53.7 uM) | 0.5 | 0.5 | 0.5 | 0 |
| NEB PURExpress Solution A | 4 | 4 | 4 | 4 |
| NEB PURExpress Solution B | 3 | 3 | 3 | 3 |
| RNase Inhibitor | 0.5 | 0.5 | 0.5 | 0.5 |
| Optiprep | 0 | 0.33 | 0.67 | 0 |
| Nucleus Free Water | 1 | 0.67 | 0.33 | 2 |
| **Total** | **10** | **10** | **10** | **10** |
:::
::::

::::{tip} Experiment 2
:class: simple
:class: dropdown
:icon: false

:::{table}
:label: tbl-exp2
| **Component** | **Sample 1** | **Sample 2** | **Sample 3** | **Sample 4** | **Control** |
| --- | --- | --- | --- | --- | --- |
| Purified deGFP-ssrA (41.2 uM)  | 0.1 | 0.1 | 0.1 | 0.1 | 0.1 |
| pOpen-pT7-ClpP-cHis (100 nM) | 0.5 | 0.5 | 0.5 | 0.5 | 0 |
| Purified ClpX (53.7 uM) | 0.2 | 0.2 | 0.2 | 0.2 | 0.2 |
| NEB PURExpress Solution A | 4 | 4 | 4 | 4 | 4 |
| NEB PURExpress Solution B | 3 | 3 | 3 | 3 | 3 |
| RNase Inhibitor | 0.5 | 0.5 | 0.5 | 0.5 | 0.5 |
| Sucrose (2M) | 0 | 0.5 | 1 | 1.5 | 0 |
| Nucleus Free Water | 1.7 | 1.2 | 0.7 | 0.2 | 2.2 |
| **Total** | **10** | **10** | **10** | **10** |
:::
::::


::::{tip} Experiment 3
:class: simple
:class: dropdown
:icon: false

:::{table}
:label: tbl-exp3
| **Component** | **Sample 1** | **Sample 2** | **Sample 3** | **Control** |
| --- | --- | --- | --- | --- | 
| Purified deGFP-ssrA (41.2 uM)  | 0.5 | 0.5 | 0.5 | 0.5 |
| Purified ClpP (79.9 uM) | 0.5 | 0.5 | 0.5 | 0.5 |
| pOpen-pT7-ClpX-cHis (86 nM) | 0.5 | 0.5 | 0.5 | 0 |
| NEB PURExpress Solution A | 4 | 4 | 4 | 4 |
| NEB PURExpress Solution B | 3 | 3 | 3 | 3 |
| RNase Inhibitor | 0.5 | 0.5 | 0.5 | 0.5 |
| Optiprep | 0 | 0 | 0.3 | 0 |
| Sucrose (2M) | 0 | 1 | 0 | 0 |
| Nucleus Free Water | 1 | 0 | 0.7 | 1.5 |
| **Total** | **10** | **10** | **10** | **10** |
:::
::::

***

## Preparation of liposomes:

:::::{tab-set}

::::{tab-item} Cytosols
:::{table}
:label: tbl-inners
| **Component** | **Liposomes (ClpXP - 2DNAs)** | **Liposomes (ClpXP - 1DNA)** | **Liposomes (Control)** |
| --- | --- | --- | --- |
| NEB PURExpress Solution A | 12 | 12 | 12 | 
| NEB PURExpress Solution B | 9 | 9 | 9 |
| RNase Inhibitor | 1.5 | 1.5 | 1.5 |
| Purified deGFP-ssrA (41.2 µM) | 0.3 | 0.3 | 0.3 |
| Purified ClpX (53.7 μM) | 0 | 0.6 | 0 |
| Linear pT7-ClpX (70 ng/ul) | 1.5 | 0 | 0 | 
| Linear pT7-ClpP (70 ng/ul) | 1.5 | 1.5 | 0 |
| Sucrose (2M) | 3 | 3 | 3 | 
| Nucleus Free Water | 1.2 | 2.2 | 4.2 | 
:::
::::

::::{tab-item} Membrane
:::{table}
:label: tbl-membrane
| **Lipid** | **Target Percentage %** | **Molecular Weight** | **Concentration(mg/mL)** | **Volume to Add (uL)** |
| --- | --- | --- | --- | --- |
| POPC | 70 | 760.076 | 25 | 162.17 |
| Cholesterol | 29.95 | 386.66 | 50 | 17.65 |
| Rhod PE | 0.05 | 1301.72 | 1 | 4.96 |
:::
::::

::::{tab-item} Outer Solutions
:::{table}
:label: tbl-outers
| **Samples** | **Component** | **Target Concentration(mM)** |
| --- | --- | --- |
| Liposomes (ClpXP - 2DNAs) | Glucose | 933 | 
| Liposomes (ClpXP - 1DNA) | Glucose | 960 |
| Liposomes (Control) | Glucose | 900 |

::::
:::::

**Preparation of the Lipid-Oil Mixture (5mg/mL):**

1. Add 1 mL mineral oil in the 2mL small glass jar
2. Add lipids shown in the {ref}`tbl-membrane` into the glass jar on top of the mineral oil.   
3. Vortex the lipid-oil mixture for 10 secs
4. Put the glass jar in the bead-loaded hot bath at ~55c for 4 hrs (keep the jar uncovered without lid)
5. Place the jar (with lid) containing lipid-in-oil solution at RT for 10 mins before using


**Formation of liposomes:**

1. Add 300 uL of outer solution in tube A.
2. Add 120 uL of the lipid-oil mixture on top of 20 uL of inner aqueous solution, and then do washboard for 50 times to form emulsion.
3. Add the milky solution (after washboarding) from the previous step on top of the the outer solution in tube A.
4. Centrifuge at RT for 10 mins at 9000 xg.
5. Remove the top residual oil until 100 uL of solution in the 1.5 mL Eppendorf tube.
6. Resuspend the pellet and collect liposomes.



# Observations and Experimental Results
## For Bulk Reactions:

Since our ultimate goal is to encapsulate the entire control module with PURE inside liposomes, which require either Optiprep or sucrose as density-gradient media, we tested bulk reactions supplemented with these additives ({ref}`tbl-exp1` and {ref}`tbl-exp2`). We found that increasing Optiprep concentrations noticeably slowed GFP degradation {ref}`fig:Optiprep`, whereas sucrose had minimal impact on the degradation rate {ref}`fig:Sucrose`. Accordingly, sucrose was selected for liposome preparation in all subsequent cell-encapsulation experiments.

<!-- #20250930-kinetics -->
:::{figure} #20250930-kinetics
:name: fig:Optiprep
:align: center
:width: 65%

GFP fluorescence signal in PURE reactions with addition of different amount of Optiprep incubated at 37 °C for 6 hours. The reaction contains pT7-ClpP DNA, purified ClpX protein and purified deGFP-ssrA protein.
:::

:::{figure} #20251008-kinetics
:name: fig:Sucrose
:align: center
:width: 70%

GFP fluorescence signal in PURE reactions with addition of different amount of sucrose incubated at 37 °C for 6 hours. The reaction contains pT7-ClpP DNA, purified ClpX protein and purified deGFP-ssrA protein.
:::

Next, we used ClpX DNA to express the ClpX protease alongside purified ClpP proteins and GFP-ssrA within the PURE system containing either Optiprep or sucrose {ref}`tbl-exp3` to examine the effects of these density-gradient additives on protein degradation. We found that the addition of either component slowed the degradation rate, with Optiprep having a stronger inhibitory effect than sucrose {ref}`fig:ClpX-S`. These results suggest that an even greater delay in GFP signal loss should be expected when the system is encapsulated within liposomes, where sucrose or OptiPrep is typically included. As a result, in subsequent liposome experiments, we elected to use sucrose as the density-gradient additive for liposome formation. 

:::{figure} #20251209-kinetics
:name: fig:ClpX-S
:align: center
:width: 75%

GFP fluorescence signal in PURE reactions with addition of Optiprep or sucrose incubated at 37 °C for 6 hours. The reaction contains pT7-ClpX DNA, purified ClpP protein and purified deGFP-ssrA protein.
:::

## For Liposome encapsulations:

Three liposome samples were prepared to demonstrate that the control module functions inside synthetic cells. All samples encapsulated purified deGFP-ssrA protein. The first liposome population additionally encapsulated two linear DNAs, pT7-ClpX and pT7-ClpP. The second population encapsulated pT7-ClpP DNA together with purified ClpX protein. The control liposomes contained no DNA. In all cases, the NEB PURE system was co-encapsulated along with the corresponding proteins and/or DNAs.

Fluorescence microscopy revealed that liposomes containing functional ClpXP, whether generated from co-encapsulated DNAs or from a combination of DNA and purified protein, exhibited a clear, macroscopic decrease in green fluorescence over the incubation period. Notably, liposomes containing both pT7-ClpX and pT7-ClpP DNA {ref}`fig:Cell-2DNA` displayed a slower rate of GFP fluorescence decrease compared with liposomes containing only pT7-ClpP DNA and purified ClpX protein {ref}`fig:Cell-1DNA`. This difference is consistent with increased competition for limited transcription–translation resources when multiple DNAs are present in a single PURE reaction. In contrast, control liposomes lacking ClpXP showed no substantial decrease in fluorescence; the slight signal reduction observed is most likely attributable to photobleaching {ref}`fig:Cell-Control`. A modest rise in green fluorescence was observed within the first ~20 minutes, likely reflecting the gradual sedimentation of liposomes to the bottom of the imaging well. 

:::::{tab-set}

::::{tab-item} Liposomes (ClpXP - 2 DNAs)
:sync: tab1-1
:::{figure} ./figures/Cell-2DNA.png
:label: fig:Cell-2DNA
Time-series fluorescence microscopy images of liposomes containing pT7-ClpX and pT7-ClpP DNA together with purified GFP-ssrA, incubated at 37 °C. Images were acquired in the 488 channel (200 ms exposure, 40% intensity), with excitation at 460–490 nm and emission collected at 500–550 nm. Decreasing green fluorescence was observed in liposomes overtime.
:::
::::

::::{tab-item} Liposomes (ClpXP - 1 DNA)
:sync: tab1-2
:::{figure} ./figures/Cell-1DNA.png
:label: fig:Cell-1DNA
Time-series fluorescence microscopy images of liposomes containing pT7-ClpP DNA with purified ClpX and purified GFP-ssrA, incubated at 37 °C. Images were acquired in the 488 channel (200 ms exposure, 40% intensity), with excitation at 460–490 nm and emission collected at 500–550 nm. Decreasing green fluorescence was observed in liposomes overtime.
:::
::::

::::{tab-item} Liposomes (Control - No DNA)
:sync: tab1-3
:::{figure} ./figures/Cell-Control.png
:label: fig:Cell-Control
Time-series fluorescence microscopy images of control liposomes containing purified GFP-ssrA, incubated at 37 °C. Images were acquired in the 488 channel (200 ms exposure, 40% intensity), with excitation at 460–490 nm and emission collected at 500–550 nm.
:::
::::

:::::

We further quantified liposome fluorescence by analyzing the GFP intensity distributions using histograms, which were consistent with the trends observed in fluorescence microscopy images. As expected, in liposomes containing ClpXP DNA and/or proteins, the majority of liposomes exhibited a progressive decrease in GFP intensity during incubation, whereas control liposomes lacking ClpXP maintained relatively stable fluorescence levels {ref}`fig:Data`. Notably, a small subpopulation of highly fluorescent liposomes persisted over time in all conditions, including both ClpXP-containing and control samples, showing no appreciable reduction in GFP signal. A potential reason is that these liposomes failed to encapsulate functional ClpXP components during formation, thereby preventing degradation of GFP–ssrA.

:::{figure} ./figures/Data.png
:name: fig:Data
:align: center
:width: 90%

Time-resolved histograms of mean GFP fluorescence intensity of individual liposomes during incubation. Top row: liposomes containing both ClpX and ClpP DNA (ClpXP–2DNAs); middle row: liposomes containing a single ClpXP DNA component (ClpXP–1DNA); bottom row: control liposomes lacking ClpXP. Histograms are shown at 0, 45, 90, 135, 180, and 225 min. In ClpXP-containing samples, the fluorescence distributions progressively shift toward lower intensities over time, consistent with GFP–ssrA degradation, whereas control liposomes maintain relatively stable intensity distributions. A persistent high-intensity subpopulation is observed across all conditions.
:::


In addition to encapsulated reactions, we performed bulk PURE reactions with identical components at the same concentrations. The overall trends in GFP fluorescence were similar to those observed in liposomes. However, protein degradation proceeded substantially faster in bulk reactions than in synthetic cells, highlighting the impact of confinement on reaction kinetics {ref}`fig:Cell-Bulk`.


<!-- ./figures/ClpXP-Cell-bulk.png -->
:::{figure} #20251211-kinetics
:name: fig:Cell-Bulk
:align: center
:width: 70%

GFP fluorescence signal in bulk PURE reactions containing purified proteins and/or plasmid DNAs, incubated at 37 °C for 6 hours. Each DNA was present at a concentration of 3.5 ng/µL. Purified ClpX and deGFP-ssrA were included at final concentrations of 2.69 µM and 1.24 µM, respectively.
:::

Together, these results demonstrate that the ClpXP protein degradation module remains active within synthetic cells and can function concurrently with protein expression driven by the PURE system.

# Conclusion and New Horizons

These experiments demonstrate that the ClpXP based control module functions effectively with the PURE system within the confined environment of liposomes. A natural next step is to explore how to tune the expression of multiple proteins inside liposomes, similar to what we have already achieved in bulk reactions where we observed interesting oscillations in GFP expression.

We expected that introducing more independent DNA templates into a single PURE reaction will bring additional complexity, especially within the restricted space of liposomes. In addition, our results show that protein degradation inside synthetic cells is limited and was much less efficient than in bulk. A likely explanation is energy shortage, since both protein synthesis by the PURE system and protein degradation by ClpXP require ATP.

Looking ahead, integrating the PPK-based energy regeneration module [Integrating PPK Module in PURE Cells](https://doi.org/10.63765/mwur3749) with the ClpXP control module may help address these energy limitations and support more robust regulation inside synthetic cells. This direction could enable the development of more advanced genetic and proteolytic circuits within minimal, cell-like environments.

 
**Acknowledgments**

This work is supported by the Astera Institute and Sloan Foundation (Grant G-2024-22735).
