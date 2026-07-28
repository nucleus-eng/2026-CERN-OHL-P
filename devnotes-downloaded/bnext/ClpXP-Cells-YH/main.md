---
title: "ClpXP Control Module: Deployment in Nucleus PURE Cells"
abstract: |
  We engineered a Cell Control Module that integrates the ATP-dependent ClpXP protease complex to enable programmable post-translational regulation in PURE-based systems. In the previous DevNote, we have reconstituted and characterized ClpXP-mediated degradation of ssrA-tagged target proteins using the the Nucleus PURE system. In this DevNote, we extend this work by implementing the same system in liposomes to demonstrate selective and energy-dependent degradation of target substrates in synthetic cells.
---

# Overview

The [Control Module](https://devnotes.nucleus.engineering/articles/clpxp-module-plan) of the [Developer Cell](https://devnotes.bnext.bio/articles/developer-cell-introduction) is dedicated to enabling precise, time-resolved control of protein expression within synthetic minimal systems, particularly those based on the PURE system. Please refer to [Control Module](https://devnotes.nucleus.engineering/articles/clpxp-module-plan) for Module overview and background information. 

:::{figure} ./general/control-module_cells.png
:name: fig:scheme
:align: center
:width: 65%
Illustration of the ClpXP protein degradation control module in the [Developer Cell](https://devnotes.nucleus.engineering/articles/developer-cell-introduction), with other modules grayed out.
:::

In the [previous DevNote](https://devnotes.nucleus.engineering/articles/bnext-devnotes-clpx-in-pure-01), we demonstrated the degradation of ssrA-tagged proteins by the ClpXP protease system in bulk reactions using the Nucleus cell-free expression system. In this DevNote, we expand the work to synthetic cells by encapsulating the control module with Nucleus PURE using different combinations of purified proteins and DNA constructs to verify target protein degradation in confined environments.



# Exprimental Design

The goal is to demonstrate degradation of the GFP-ssrA protein by the AAA+ ATPase ClpX and the tetradecameric peptidase ClpP in synthetic cells.  Because the reaction dynamics differ significantly between bulk and encapsulated environments, the concentrations of DNA templates and purified proteins must be fine-tuned separately for each context.


## DNA Constructs and Purified Proteins

All DNA constructs are designed to be used in PURE reactions for protein expressions:

| **DNA Constructs** | **Description** | 
| --- | --- |
| Linear pT7-ClpP | Express ClpP protein using linear DNA |

All purified proteins are ordered from GenScript:

| **Proteins** | **Description** |
| --- | --- |
| ClpX | Purified ClpX protein expressed using pET30a plasmid |
| deGFP-ssrA | Purified GFP protein wtih ssrA tag expressed using pET30a plasmid |


## Materials

| **Product** | **Brand** | **Catalog No.** |
| --- | --- | --- | 
| PURExpress® In Vitro Protein Synthesis Kit | New England Biolabs | E6800L | 
| RNase Inhinitor, Murine | New England Biolabs | M0314L |
| Nucleus Cytosol - SMix | B. NEXT | AR-1125 | 
| Nucleus Cytosol - PMix | B. NEXT | AR-1085 | 
| Nucleus Cytosol - Ribo | B. NEXT | AR-964 |
| Nucleus Cytosol - tRNA | B. NEXT | AR-1080 |

## Protocol
### Preparation of PURE bulk reactions:

::::{tip} Experiment 1 (No DNA)
:class: simple
:class: dropdown
:icon: false


:::{table}
:label: tbl-exp1
| **Component** | **Sample 1** | **Sample 2** | **Sample 3** | **Control** |
| --- | --- | --- | --- | --- |
| Purified deGFP-ssrA (41.2 uM)  | 0.5 | 0.5 | 0.5 | 0.5 |
| Purified ClpP (79.9 uM) | 0.5 | 0.5 | 0 | 0 |
| Purified ClpX (53.7 uM) | 0.5 | 0 | 0.5 | 0 |
| SMix | 3 | 3 | 3 | 3 |
| PMix | 1.2 | 1.2 | 1.2 | 1.2 |
| Ribo | 1.8 | 1.8 | 1.8 | 1.8 |
| tRNA | 1 | 1 | 1 | 1 |
| RNase Inhibitor | 0.5 | 0.5 | 0.5 | 0.5 |
| Nucleus Free Water | 1 | 1.5 | 1.5 | 2 |
| **Total** | **10** | **10** | **10** | **10** |
:::
::::

::::{tip} Experiment 2 (1 DNA: ClpP)
:class: simple
:class: dropdown
:icon: false

:::{table}
:label: tbl-exp2
| **Component** | **Sample 1** | **Sample 2** | **Sample 3** | **Control** |
| --- | --- | --- | --- | --- |
| Purified deGFP-ssrA (41.2 uM)  | 0.5 | 0.5 | 0.5 | 0.5 |
| pT7-ClpP (27.6 nM) | 0.5 | 1 | 1.5 | 0 |
| Purified ClpX (53.7 uM) | 0.5 | 0.5 | 0.5 | 0 |
| SMix | 3 | 3 | 3 | 3 |
| PMix | 1.2 | 1.2 | 1.2 | 1.2 |
| Ribo | 1.8 | 1.8 | 1.8 | 1.8 |
| tRNA | 1 | 1 | 1 | 1 |
| RNase Inhibitor | 0.5 | 0.5 | 0.5 | 0.5 |
| Nucleus Free Water | 1 | 0.5 | 0 | 2 |
| **Total** | **10** | **10** | **10** | **10** |
:::
::::

::::{tip} Experiment 3 (1 DNA: ClpX)
:class: simple
:class: dropdown
:icon: false

:::{table}
:label: tbl-exp3
| **Component** | **Sample 1** | **Sample 2** | **Sample 3** | **Control** |
| --- | --- | --- | --- | --- |
| Purified deGFP-ssrA (41.2 uM)  | 0.5 | 0.5 | 0.5 | 0.5 |
| Purified ClpP (79.9 nM) | 0.5 | 0.5 | 0.5 | 0 |
| pT7-ClpX (22.3 nM) | 0.5 | 1 | 1.5 | 0 |
| SMix | 3 | 3 | 3 | 3 |
| PMix | 1.2 | 1.2 | 1.2 | 1.2 |
| Ribo | 1.8 | 1.8 | 1.8 | 1.8 |
| tRNA | 1 | 1 | 1 | 1 |
| RNase Inhibitor | 0.5 | 0.5 | 0.5 | 0.5 |
| Nucleus Free Water | 1 | 0.5 | 0 | 2 |
| **Total** | **10** | **10** | **10** | **10** |
:::
::::

::::{tip} Experiment 4 (1 DNA: GFP-ssrA)
:class: simple
:class: dropdown
:icon: false

:::{table}
:label: tbl-exp4
| **Component** | **Sample 1** | **Sample 2** | **Sample 3** | **Control** |
| --- | --- | --- | --- | --- |
| pT7-deGFP-ssrA (27 nM)  | 0.5 | 1 | 1.5 | 0.5 |
| Purified ClpP (79.9 uM) | 0.5 | 0.5 | 0.5 | 0 |
| Purfied ClpX (53.7 uM) | 0.5 | 0.5 | 0.5 | 0 |
| SMix | 3 | 3 | 3 | 3 |
| PMix | 1.2 | 1.2 | 1.2 | 1.2 |
| Ribo | 1.8 | 1.8 | 1.8 | 1.8 |
| tRNA | 1 | 1 | 1 | 1 |
| RNase Inhibitor | 0.5 | 0.5 | 0.5 | 0.5 |
| Nucleus Free Water | 1 | 0.5 | 0 | 2 |
| **Total** | **10** | **10** | **10** | **10** |
:::
::::

::::{tip} Experiment 5 (2 DNA: ClpP and deGFP-ssrA)
:class: simple
:class: dropdown
:icon: false

:::{table}
:label: tbl-exp5
| **Component** | **Sample 1** | **Sample 2** | **Sample 3** |
| --- | --- | --- | --- |
| pT7-deGFP-ssrA (27 nM)  | 0.25 | 0.5 | 0.75 |
| pT7-ClpP (27.6 nM) | 0.25 | 0.5 | 0.75 |
| Purfied ClpX (53.7 nM) | 0.5 | 0.5 | 0.5 |
| SMix | 3 | 3 | 3 |
| PMix | 1.2 | 1.2 | 1.2 |
| Ribo | 1.8 | 1.8 | 1.8 |
| tRNA | 1 | 1 | 1 |
| RNase Inhibitor | 0.5 | 0.5 | 0.5 |
| Nucleus Free Water | 1.5 | 1 | 0.5 |
| **Total** | **10** | **10** | **10** | **10** |
:::
::::


::::{tip} Experiment 6 (2 DNA: ClpX and deGFP-ssrA)
:class: simple
:class: dropdown
:icon: false

:::{table}
:label: tbl-exp6
| **Component** | **Sample 1** | **Sample 2** | **Sample 3** |
| --- | --- | --- | --- |
| pT7-deGFP-ssrA (27 nM)  | 0.25 | 0.5 | 0.75 |
| Purified ClpP (79.9 uM) | 0.5 | 0.5 | 0.5 |
| pT7-ClpX (22.3 nM) | 0.25 | 0.5 | 0.75 |
| SMix | 3 | 3 | 3 |
| PMix | 1.2 | 1.2 | 1.2 |
| Ribo | 1.8 | 1.8 | 1.8 |
| tRNA | 1 | 1 | 1 |
| RNase Inhibitor | 0.5 | 0.5 | 0.5 |
| Nucleus Free Water | 1.5 | 1 | 0.5 |
| **Total** | **10** | **10** | **10** | **10** |
:::
::::

::::{tip} Experiment 7 (3 DNA)
:class: simple
:class: dropdown
:icon: false

:::{table}
:label: tbl-exp7
| **Component** | **Sample 1** | **Sample 2** | **Sample 3** |
| --- | --- | --- | --- |
| pT7-deGFP-ssrA (27 nM)  | 0.25 | 0.5 | 0.75 |
| pT7-ClpP (27.6 uM) | 0.25 | 0.25 | 0.25 |
| pT7-ClpX (22.3 nM) | 0.25 | 0.25 | 0.25 |
| SMix | 3 | 3 | 3 |
| PMix | 1.2 | 1.2 | 1.2 |
| Ribo | 1.8 | 1.8 | 1.8 |
| tRNA | 1 | 1 | 1 |
| RNase Inhibitor | 0.5 | 0.5 | 0.5 |
| Nucleus Free Water | 1.75 | 1.5 | 1.25 |
| **Total** | **10** | **10** | **10** | **10** |
:::
::::

***

### Preparation of liposomes:

# Observations and Experimental Results

:::::{tab-set}

::::{tab-item} Liposomes w/ ClpXP 
:sync: tab1-1
:::{figure} ./general/Cells/Microscopy/Sample.png
:label: fig:sample
Time-series fluorescence microscopy images of liposomes containing pT7-ClpP DNA with purified ClpX and purified GFP-ssrA, incubated at 37 °C. Images were acquired in the 488 channel (200 ms exposure, 40% intensity), with excitation at 460–490 nm and emission collected at 500–550 nm. Decreasing green fluorescence was observed in liposomes overtime.
:::
::::

::::{tab-item} Liposomes (w/o ClpXP)
:sync: tab1-2
:::{figure} ./general/Cells/Microscopy/Control.png
:label: fig:control
Time-series fluorescence microscopy images of control liposomes containing purified GFP-ssrA, incubated at 37 °C. Images were acquired in the 488 channel (200 ms exposure, 40% intensity), with excitation at 460–490 nm and emission collected at 500–550 nm.
:::
::::

:::::

In addition to encapsulated reactions, we performed bulk PURE reactions with identical components at the same concentrations. The overall trends in GFP fluorescence were similar to those observed in liposomes. However, protein degradation proceeded substantially faster in bulk reactions than in synthetic cells, highlighting the impact of confinement on reaction kinetics {ref}`fig:Cell-Platereader`

:::{figure} ./general/Cells/Platereader.png
:name: fig:Cells-Platereader
:align: center
:width: 90%

GFP fluorescence signal in bulk PURE reactions containing purified proteins and/or plasmid DNAs, incubated at 37 °C for 6 hours. Each DNA was present at a concentration of 3.5 ng/µL. Purified ClpX and deGFP-ssrA were included at final concentrations of 2.69 µM and 1.24 µM, respectively.
:::



# Conclusion and New Horizons

In [previous DevNotes](https://devnotes.nucleus.engineering/articles/bnext-devnotes-clpxp-pure-cells-01), we successfully demonstrated that the ClpXP-based control module functions effectively within the NEB PURE system in the confined environment of liposomes, establishing its robustness for protein degradation–based control in synthetic cells. Building on this foundation, the next step is to transition this system to synthetic cells encapsulating the Nucleus PURE system. This transition is important not only as a technical substitution, but also as an opportunity to directly compare how the two PURE systems perform under identical synthetic cell conditions. While we have already characterized and compared NEB PURE and Nucleus PURE in bulk reactions, their behavior in confined, cell-like environments remains unexplored and may reveal differences in expression efficiency, degradation dynamics, and system compatibility that are not apparent in bulk. Therefore, implementing the ClpXP control module in Nucleus PURE-based synthetic cells will enable a systematic, side-by-side evaluation of these two transcription–translation platforms in a more biologically relevant compartmentalized setting, helping to clarify their respective strengths and limitations for synthetic cell engineering.


