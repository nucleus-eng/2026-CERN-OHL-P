---
# Ensure that this title is the same as the one in `myst.yml`
title: "Control Module - Degradation of targeted proteins by ClpXP protease "
abstract: |
  Precise and time-resolved regulation of protein levels is essential for constructing synthetic minimal cells that can display dynamic and reversible behaviors. However, the PURE system, although it provides a defined and protease-free environment with high transcription and translation fidelity, does not contain endogenous pathways for controlled protein degradation. This limitation restricts the development of circuits that require signal reset, feedback, or temporal coordination. To address this gap, the Developer Cell Control Module integrates the ATP-dependent ClpXP protease complex to enable programmable post-translational regulation within PURE-based systems. In this DevNote, we reconstitute and evaluate ClpXP-mediated degradation of ssrA-tagged target proteins in both bulk reactions and liposome-encapsulated synthetic cells. Using combinations of purified protein components and DNA templates supplemented with PURE, we demonstrate selective and energy-dependent degradation of target substrates. These results establish an effective strategy for controlling protein lifetimes in minimal synthetic environments and lay the groundwork for engineering synthetic cells with more sophisticated, dynamic, and tunable functional behaviors.
---


# Overview

The Control Module of the [Developer Cell](https://devnotes.bnext.bio/articles/developer-cell-introduction) is dedicated to enabling precise, time-resolved control of protein expression within synthetic minimal systems, particularly those based on the PURE system. The PURE system offers a defined, protease-free biochemical environment that allows high-fidelity transcription and translation without the background interference found in crude cell lysates. While this protease-free context is beneficial for maximizing protein yield and reducing unwanted degradation, it introduces a critical limitation: the lack of mechanisms for post-translational regulation, particularly controlled protein degradation.

This limitation becomes increasingly significant as synthetic cell engineering moves toward more dynamic and autonomous behaviors. Without an active degradation pathway, any protein expressed in response to a stimulus such as a sensor activation remains indefinitely active, even after the stimulus is removed. This impedes the design of synthetic circuits requiring time-dependent or reversible responses, including feedback regulation, homeostasis, noise filtering, signal reset, and periodic behaviors akin to cell cycle progression.

To overcome this challenge, the Control Module aims to incorporate a programmable degradation pathway using the ClpXP protease system, allowing researchers to actively manage protein lifetimes in the synthetic environment. By integrating ClpXP into the PURE system, we introduce the capacity for selective, energy-dependent degradation of target proteins, enabling dynamic control over circuit behavior and opening the door to more sophisticated synthetic cellular functionalities.

In this DevNote, we performed the degradation of the protein targeted with ssrA tag by ClpX and ClpP proteases in both bulk reactions and encapsulated in liposomes. We tested different combinations of purified proteins and DNA constructs with addition of PURE system to verify the target protein degradation. 

:::{figure} ./figures/clpXP.png
:name: fig:scheme
:align: center
:width: 65%

Cartoon of the general mechanism of protein degradation by ClpXP, ATP-dependent protease. Adapted from [R. Wedam et al., Targeting Mitochondria with ClpP Agonists as a Novel Therapeutic Opportunity in Breast Cancer. Cancers. 15 (2023)](https://doi.org/10.3390/cancers15071936)
:::

# Background

ClpXP is a highly conserved, ATP-dependent proteolytic complex that plays a central role in protein quality control and regulatory degradation in prokaryotic cells. It is composed of two main components: the ClpX ATPase, which recognizes and unfolds substrate proteins, and the ClpP peptidase, which degrades the unfolded polypeptides into short peptides. This two-part system is capable of tightly regulated and substrate-specific degradation, a feature that is critical for synthetic systems requiring fine-tuned control over protein turnover.

In the context of the PURE system, ClpXP has been functionally reconstituted and shown to maintain activity when supplied with appropriate ATP levels. Importantly, ClpXP exhibits high specificity by recognizing substrate proteins that carry a C-terminal ssrA degradation tag, allowing researchers to selectively mark proteins for degradation while leaving other components of the system untouched. This specificity ensures that only user-defined targets are removed from the system, avoiding unwanted disruption of essential cellular processes encoded within the synthetic cytosol.

Furthermore, ClpXP's reliance on ATP hydrolysis couples its activity to the metabolic state of the system. This makes it an ideal candidate for integration with the energy module of the synthetic cell platform, ensuring coordinated control over both protein synthesis and degradation. Together, these features make ClpXP a powerful tool for implementing regulated, dynamic behavior in synthetic systems, bringing us closer to building minimal cells with lifelike properties such as adaptability, robustness, and controlled developmental trajectories.

# Exprimental Design

The goal is to demonstrate degradation of the GFP-ssrA protein by the AAA+ ATPase ClpX and the tetradecameric peptidase ClpP, as well as our ability to tune the extent of degradation. To achieve this, we show that GFP tagged with the ssrA sequence can be efficiently degraded either by purified ClpXP proteins or by ClpXP complexes expressed directly from DNA templates in the PURE system. We also examine the reverse configuration, in which GFP-ssrA is expressed using the PURE system and ClpXP is supplied in purified form, confirming that protein expression and degradation can be independently controlled. Importantly, all experiments are performed both in bulk reactions and in synthetic cells formed by liposome encapsulation. Because the reaction dynamics differ significantly between bulk and encapsulated environments, the concentrations of DNA templates and purified proteins must be fine-tuned separately for each context. We further explore tuning by combining two DNA constructs in PURE reactions together with a purified protein component. The combinations of DNA templates and purified proteins used in each experiment or condition are listed below.

### Bulk Reactions:


:::{table} This DevNote describes 8 bulk reaction experiments that test combinations of Control Module components. V = present in experiment; X = not present in experiment. 
| **Experiments** | **Purified ClpX** | **Purified ClpP** | **Purified GFP-ssrA** | **ClpP DNA** | **GFP-ssrA DNA** | **ClpX DNA** | **Sucrose/ Optiprep** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Experiment 1 | V | V | V | X | X | X | X |
| Experiment 2 | V | V | X | X | V | X | X |
| Experiment 3 | V | V | X | X | V | X | V |
| Experiment 4 | X | X | V | X | X | V | X |
| Experiment 5 | X | X | V | X | X | V | V |
| Experiment 6 | V | X | V | V | X | X | X |
| Experiment 7 | V | X | X | V | V | X | X |
| Experiment 8 | X | X | X | V | V | V | X |

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
| [pOpen-pT7-ClpP-CHis](https://github.com/nucleus-eng/DNA/blob/bf9cfc08f1e1443f8185da24cf78467c67911766/control/pOpen-ClpP-CHis.gb) | Express ClpP protein in the pOpen plasmid |
| [pOpen-pT7-deGFP-ssrA](https://github.com/nucleus-eng/DNA/blob/bf9cfc08f1e1443f8185da24cf78467c67911766/control/pOpen-deGFP-ssrA.gb) | Express GFP protein wtih ssrA tag in the pOpen plasmid |
| Linear pT7-deGFP-ssrA | Express deGFP protein wtih ssrA tag using linear DNA |
| Linear pT7-deGFP |Express deGFP protein using linear DNA |

All purified proteins are ordered from GenScript:

| **Proteins** | **Description** |
| --- | --- |
| [ClpX](https://github.com/nucleus-eng/DNA/blob/bf9cfc08f1e1443f8185da24cf78467c67911766/control/protein-purification/pET28a-ClpX-CHis.gb) | Purified ClpX protein expressed using pET28a plasmid |
| [ClpP](https://github.com/nucleus-eng/DNA/blob/bf9cfc08f1e1443f8185da24cf78467c67911766/control/protein-purification/pET28a-ClpP-CHis.gb) | Purified ClpP protein expressed using pET28a plasmid |
| [deGFP-ssRA](https://github.com/nucleus-eng/DNA/blob/bf9cfc08f1e1443f8185da24cf78467c67911766/control/protein-purification/pET28a-deGFP-CHis-ssrA.gb) | Purified GFP protein wtih ssrA tag expressed using pET28a plasmid |



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

### Experiment 1:

:::{table}
| **Component** | **Sample 1** | **Sample 2** | **Sample 3** | **Control** |
| --- | --- | --- | --- | --- |
| Purified deGFP-ssrA (41.2 uM)  | 0.5 | 0.5 | 0.5 | 0.5 |
| Purified ClpP (79.9 uM) | 0.5 | 0.5 | 0 | 0 |
| Purified ClpX (53.7 uM) | 0.5 | 0 | 0.5 | 0 |
| NEB PURExpress Solution A | 4 | 4 | 4 | 4 |
| NEB PURExpress Solution B | 3 | 3 | 3 | 3 |
| RNase Inhibitor | 0.5 | 0.5 | 0.5 | 0.5 |
| Nucleus Free Water | 1 | 1.5 | 1.5 | 2 |
| **Total** | **10** | **10** | **10** | **10** |
:::

### Experiment 2:

:::{table}
| **Component** | **Sample 1** | **Sample 2** | **Sample 3** | **Control** |
| --- | --- | --- | --- | --- |
| Purified deGFP-ssrA (41.2 uM)  | 0.5 | 0.5 | 0.5 | 0.5 |
| pOpen-pT7-ClpP-cHis (40 nM) | 0.5 | 1 | 1.5 | 0 |
| Purified ClpX (53.7 uM) | 0.2 | 0.2 | 0.2 | 0 |
| NEB PURExpress Solution A | 4 | 4 | 4 | 4 |
| NEB PURExpress Solution B | 3 | 3 | 3 | 3 |
| RNase Inhibitor | 0.5 | 0.5 | 0.5 | 0.5 |
| Nucleus Free Water | 1.3 | 0.8 | 0.3 | 2 |
| **Total** | **10** | **10** | **10** | **10** |

:::

### Experiment 3-1:

:::{table}
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

### Experiment 3-2:

:::{table}
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

:::{table}
### Experiment 4:
| **Component** | **Sample** | **Control** |
| --- | --- | --- | 
| Purified deGFP-ssrA (41.2 uM)  | 0.5 | 0.5 |
| Purified ClpP (79.9 uM) | 0.5 | 0.5 |
| pOpen-pT7-ClpX-cHis (86 nM) | 0.5 | 0 |
| NEB PURExpress Solution A | 4 | 4 |
| NEB PURExpress Solution B | 3 | 3 |
| RNase Inhibitor | 0.5 | 0.5 |
| Nucleus Free Water | 1 | 1.5 |
| **Total** | **10** | **10** |
:::

### Experiment 5:
:::{table}
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

### Experiment 6:
:::{table}
| **Component** | **Sample 1** | **Sample 2** | **Sample 3** | **Control** |
| --- | --- | --- | --- | --- | 
| pOpen-pT7-deGFP ssrA (63.5 ng/ul)  | 0.5 | 0.5 | 0.5 | 0.5 |
| Purified ClpP | 0.5 (20 uM) | 0.5 (40 uM) | 0.5 (80 uM) | 0.5 |
| Purified ClpX | 0.5 (14.4 uM) | 0.5 (26.9 uM) | 0.5 (53.7 uM) | 0 |
| NEB PURExpress Solution A | 4 | 4 | 4 | 4 |
| NEB PURExpress Solution B | 3 | 3 | 3 | 3 |
| RNase Inhibitor | 0.5 | 0.5 | 0.5 | 0.5 |
| Nucleus Free Water | 1.2 | 1.2 | 1.2 | 2 |
| **Total** | **10** | **10** | **10** | **10** |
:::

### Experiment 7:
:::{table}
| **Component** | **Sample 1** | **Sample 2** | **Sample 3** | **Control** |
| --- | --- | --- | --- | --- | 
| pT7-deGFP ssrA (63.5 ng/ul)  | 0.4 | 0.4 | 0.4 | 0.4 |
| pT7-ClpP (47.9 ng/ul) | 0.6 | 0.8 | 1 | 0 |
| Purified ClpX (53.7 uM)| 0.4 | 0.4 | 0.4 | 0 |
| NEB PURExpress Solution A | 4 | 4 | 4 | 4 |
| NEB PURExpress Solution B | 3 | 3 | 3 | 3 |
| RNase Inhibitor | 0.5 | 0.5 | 0.5 | 0.5 |
| Nucleus Free Water | 1.1 | 0.9 | 0.7 | 2.1 |
| **Total** | **10** | **10** | **10** | **10** |
:::


### Experiment 8:

:::{table}
| **Component** | **Sample 1** | **Sample 2** | **Sample 3** | **Sample 4** |
| --- | --- | --- | --- | --- | 
| pT7-deGFP ssrA (63.5 ng/ul)  | 0.5 | 0.5 | 0.5 | 0.5 |
| pT7-ClpP (17.5 ng/ul) | 0.4 | 0.4 | 0.6 | 0.8 |
| pT7-ClpX (17.5 ng/ul)| 0.4 | 0.4 | 0.6 | 0.8 |
| NEB PURExpress Solution A | 4 | 4 | 4 | 4 |
| NEB PURExpress Solution B | 3 | 3 | 3 | 3 |
| RNase Inhibitor | 0.5 | 0.5 | 0.5 | 0.5 |
| Nucleus Free Water | 1.6 | 1.2 | 0.8 | 0.4 |
| **Total** | **10** | **10** | **10** | **10** |
:::


## Preparation of liposomes:

### Preparation of the Lipid-Oil Mixture (5mg/mL):
1. Add 1 mL mineral oil in the 2mL small glass jar
2. Add lipids shown in the following table into the glass jar on top of the mineral oil.

:::{table}
| **Lipid** | **Target Percentage %** | **Molecular Weight** | **Concentration(mg/mL)** | **Volume to Add (uL)** |
| --- | --- | --- | --- | --- |
| POPC | 70 | 760.076 | 25 | 162.17 |
| Cholesterol | 29.95 | 386.66 | 50 | 17.65 |
| Rhod PE | 0.05 | 1301.72 | 1 | 4.96 |
:::
   
4. Vortex the lipid-oil mixture for 10 secs
5. Put the glass jar in the bead-loaded hot bath at ~55c for 4 hrs (keep the jar uncovered without lid)
6. Place the jar (with lid) containing lipid-in-oil solution at RT for 10 mins before using


### Preparation of the Outer Solution (1 mL):
| **Samples** | **Component** | **Target Concentration(mM)** |
| --- | --- | --- |
| Liposomes (ClpXP - 2DNAs) | Glucose | 933 | 
| Liposomes (ClpXP - 1DNA) | Glucose | 960 |
| Liposomes (Control) | Glucose | 900 |


### Preparation of the Inner Solution:

#### Experiment:
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


### Formation of liposomes:

1. Add 300 uL of outer solution in tube A.
2. Add 120 uL of the lipid-oil mixture on top of 20 uL of inner aqueous solution, and then do washboard for 50 times to form emulsion.
3. Add the milky solution (after washboarding) from the previous step on top of the the outer solution in tube A.
4. Centrifuge at RT for 10 mins at 9000 xg.
5. Remove the top residual oil until 100 uL of solution in the 1.5 mL Eppendorf tube.
6. Resuspend the pellet and collect liposomes.



# Observations and Experimental Results
## For Bulk Reactions:
The first experiment (Experiment 1) involved mixing purified deGFP ssrA with purified ClpX and ClpP. We observed a clear decrease in GFP fluorescence over time, indicating that deGFP ssrA was efficiently degraded by the ClpXP protease. The degradation was rapid, with the GFP signal nearly disappearing within one and a half hours. In contrast, samples containing only purified ClpX or only purified ClpP did not show a significant decrease in fluorescence, confirming that degradation occurs only when both components of the ClpXP complex are present {ref}`fig:Protein`.

After establishing the functionality of the purified ClpXP degradation system, we next incorporated the PURE system. In this experiment (Experiment 2), purified ClpP was replaced with pT7 ClpP DNA. Again, we observed a decrease in deGFP fluorescence over time, demonstrating that ClpP can be expressed in vitro by PURE and remains functional for deGFP degradation {ref}`fig:ClpP DNA`.

:::{figure} ./figures/ClpXP-protein.png
:name: fig:Protein
:align: center
:width: 65%

GFP fluorescence of samples containing purified proteins incubated at 37 °C for 4 hours. 
:::

:::{figure} ./figures/ClpP DNA with ClpX and GFP proteins.png
:name: fig:ClpP DNA
:align: center
:width: 65%

GFP fluorescence signal in PURE reactions incubated at 37 °C for 6 hours. The reaction contains pT7-ClpP DNA, purified ClpX protein and purified deGFP-ssrA protein.
:::

Because our ultimate goal is to encapsulate the entire control module with PURE inside liposomes, which require either Optiprep or sucrose as density-gradient media, we also tested bulk reactions supplemented with these additives (Experiment 3). We found that increasing Optiprep concentrations noticeably slowed GFP degradation {ref}`fig:Optiprep`, whereas sucrose had minimal impact on the degradation rate {ref}`fig:Sucrose`. Accordingly, sucrose was selected for liposome preparation in all subsequent cell-encapsulation experiments.

:::{figure} ./figures/ClpXP-optiprep.png
:name: fig:Optiprep
:align: center
:width: 65%

GFP fluorescence signal in PURE reactions with addition of different amount of Optiprep incubated at 37 °C for 6 hours. The reaction contains pT7-ClpP DNA, purified ClpX protein and purified deGFP-ssrA protein.
:::

:::{figure} ./figures/ClpXP-sucrose.png
:name: fig:Sucrose
:align: center
:width: 70%

GFP fluorescence signal in PURE reactions with addition of different amount of sucrose incubated at 37 °C for 6 hours. The reaction contains pT7-ClpP DNA, purified ClpX protein and purified deGFP-ssrA protein.
:::

Besides using ClpP DNA, we also tested ClpX DNA to express the ClpX protease using the PURE system (Experiment 4). When the reaction was supplemented with purified ClpP protein and purified deGFP-ssrA substrate, we again observed the expected decrease in deGFP fluorescence over time. In contrast, the control reaction lacking ClpX DNA maintained constant fluorescence, aside from the small initial drop consistently seen in earlier experiments {ref}`fig:ClpX DNA`. We also examined the effects of OptiPrep and sucrose on protein degradation (Experiment 5) and found that the addition of either component slowed the degradation rate, with Optiprep having a stronger inhibitory effect {ref}`fig:ClpX s`. These results suggest that an even greater delay in GFP signal loss should be expected when the system is encapsulated within liposomes, where sucrose or OptiPrep is typically included. 

:::{figure} ./figures/ClpX DNA with ClpP and GFP proteins.png
:name: fig:ClpX DNA
:align: center
:width: 70%

GFP fluorescence signal in PURE reactions incubated at 37 °C for 6 hours. The reaction contains pT7-ClpX DNA, purified ClpP protein and purified deGFP-ssrA protein.
:::

:::{figure} ./figures/ClpX-Sucrose-Optiprep.png
:name: fig:ClpX S
:align: center
:width: 75%

GFP fluorescence signal in PURE reactions with addition of Optiprep or sucrose incubated at 37 °C for 6 hours. The reaction contains pT7-ClpX DNA, purified ClpP protein and purified deGFP-ssrA protein.
:::


Next, instead of using ClpP DNA, we replaced purified deGFP-ssrA with pT7-deGFP DNA for PURE-based expression and degradation (Experiment 6). By tuning the concentrations of purified ClpX and ClpP while keeping pT7-deGFP constant, we were able to control the GFP degradation kinetics. As expected, higher amounts of ClpXP resulted in faster decreases in GFP fluorescence. Interestingly, in a single PURE reaction, we could observe the fluorescence first rising (due to in vitro expression) and then declining (due to degradation) {ref}`fig:GFP DNA`. Notably, it's hard to see the GFP signal returning to its initial baseline in most of the reactions, suggesting that the system likely exhausted its available energy for continued protein degradation.

:::{figure} ./figures/ClpXP-GFP DNA.png
:name: fig:GFP DNA
:align: center
:width: 70%

GFP fluorescence signal produced using pT7-deGFP-ssrA DNA in PURE reactions incubated at 37 °C for 6 hours. Purified ClpX protein and purified ClpP protein are added to the reactions.
:::

Besides expressing a single protein from DNA in PURE, I also attempted to express two proteins simultaneously in one PURE reaction using two plasmids, pT7 ClpP and pT7 deGFP ssrA (Experiment 7). Interestingly, we observed an oscillatory pattern in the GFP fluorescence over time. The fluorescence first increased strongly and then dropped quickly, which indicates rapid GFP degradation. After this initial decrease, the GFP signal increased again, although the second peak was lower than the first one, and it was then degraded again. Similar oscillations were observed even when we increased the total amount of DNA or tested different DNA concentrations in the PURE reactions {ref}`fig:Two DNA`.

:::{figure} ./figures/ClpXP-Two DNA.png
:name: fig:Two DNA
:align: center
:width: 70%

GFP fluorescence signal produced using pT7-deGFP-ssrA DNA in PURE reactions incubated at 37 °C for 6 hours. ClpP is co-expressed in the same PURE reaction using pT7-ClpP DNA. Purified ClpX protein is added to the reactions.
:::

Finally, we examined the simultaneous expression of three proteins within a single PURE reaction using three plasmids: pT7-ClpX, pT7-ClpP, and pT7-deGFP-ssrA (Experiment 8). By systematically tuning the concentrations of each DNA, we were able to modulate both the expression and degradation dynamics of deGFP-ssrA. As the ratio of ClpX and ClpP DNA relative to deGFP-ssrA DNA increased, the overall deGFP-ssrA fluorescence decreased and its degradation rate increased, consistent with enhanced proteolytic activity. Interestingly, after an initial phase of degradation, the deGFP signal exhibited a recovery (“bounce-back”) behavior. Both the rate and magnitude of this recovery were higher at lower ClpX/ClpP DNA concentrations, suggesting a shift toward deGFP-ssrA expression as protease levels became limiting. Despite these differences in dynamics, all PURE reactions eventually reached steady state. However, reactions with lower ClpXP-to-deGFP-ssrA ratios required a longer time to reach steady state compared with those containing higher ClpXP ratios {ref}`fig:Three DNA`.

:::{figure} ./figures/ClpXP-3DNA.png
:name: fig:Three DNA
:align: center
:width: 70%

GFP fluorescence signal produced using pT7-deGFP-ssrA DNA in PURE reactions incubated at 37 °C for 6 hours. ClpX and ClpP DNAs are co-expressed in the same PURE reaction.
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

:::{figure} ./figures/ClpXP-Cell-bulk.png
:name: fig:Cell-Bulk
:align: center
:width: 70%

GFP fluorescence signal in bulk PURE reactions containing purified proteins and/or plasmid DNAs, incubated at 37 °C for 6 hours. Each DNA was present at a concentration of 3.5 ng/µL. Purified ClpX and deGFP-ssrA were included at final concentrations of 2.69 µM and 1.24 µM, respectively.
:::

Together, these results demonstrate that the ClpXP protein degradation module remains active within synthetic cells and can function concurrently with protein expression driven by the PURE system.





# Conclusion and New Horizons

These experiments demonstrate that the ClpXP based control module functions effectively with the PURE system in both bulk reactions and within the confined environment of liposomes. So far, our liposome experiments have focused on expressing a single protein from one DNA template. A natural next step is to explore how to tune the expression of multiple proteins inside liposomes, similar to what we have already achieved in bulk reactions where we observed interesting oscillations in GFP expression.

We expected that introducing two or more independent DNA templates into a single PURE reaction will bring additional complexity, especially within the restricted space of liposomes. In addition, our results show that protein degradation inside synthetic cells is limited and much less efficient than in bulk. A likely explanation is energy shortage, since both protein synthesis by the PURE system and protein degradation by ClpXP require ATP.

Looking ahead, integrating our PPK based energy regeneration module [Integrating PPK Module in PURE Cells](https://doi.org/10.63765/mwur3749) with the ClpXP control module may help address these energy limitations and support more robust regulation inside synthetic cells. This direction could enable the development of more advanced genetic and proteolytic circuits within minimal, cell-like environments.

 
**Acknowledgments**

This work is supported by the Astera Institute and Sloan Foundation (Grant G-2024-22735).
