---
title: "Membrane Translation Module Development"
abstract: |
  The Membrane Translation Module aims to enable functional membrane protein expression and integration in synthetic cells through the SecYEG translocon system. We developed DNA constructs encoding SecYEG and target membrane proteins, validated their expression in the PURExpress system, and demonstrated enhanced membrane localization and functionality in liposome-encapsulated reactions. This module will support active transporters, molecular sensors, and membrane-based communication in the Developer Cell platform.
---

# Overview

Current synthetic cell designs predominantly rely on simple channel pores for membrane regulation, as the expression and proper insertion of complex membrane proteins typically require chaperone support. Challenges such as improper folding and incorrect insertion orientation severely limit the functional use of membrane proteins in synthetic cell applications. The SecYEG translocon, the primary mechanism for membrane protein insertion in *E. coli* and other bacteria, has been demonstrated to enhance both insertion efficiency and functional activity of membrane proteins in PURE-based synthetic cells [[Sato *et al.* 2016](https://doi.org/10.1038/srep36466)].

The Membrane Translation Module integrates the SecYEG translocon into Developer synthetic cells to improve expression, insertion, orientation, and functionality of membrane proteins ({ref}`fig:membrane-overview`). By enabling the installation of active transporters in the cell membrane, this module will provide a foundation for substantially increased energy production and waste excretion, allowing synthetic cells to more closely mimic natural cell functions with broader applications.

:::{figure} ./general/ Schematic-SecYEG translocon.jpg
:label: fig:membrane-overview
:align: center
:width: 75%

Schematic representation of the SecYEG translocon facilitating membrane protein insertion in synthetic cells. SecYEG forms a sealed pore connecting the cytoplasm to the membrane, working with YidC to properly orient and insert membrane proteins during translation.
:::

## SecYEG Translocon System

SecYEG forms a sealed pore that connects the cell cytoplasm to the periplasm and lipid membrane, facilitating the translocation of membrane proteins. This process is guided by several mechanisms, including SecA, the signal recognition particle (SRP), and YidC. For this project, we focus on YidC as the primary co-factor responsible for membrane protein insertion. Building upon existing energy and control modules in the Developer Cell platform, integration of SecYEG will enable efficient membrane protein expression and translocation in synthetic cells.

# Objectives

This module aims to integrate the SecYEG translocon into PURE-based synthetic cells to enable functional membrane protein expression. The key objectives are:

- Design and validate DNA constructs encoding SecYEG components (SecY, SecE, SecG, YidC) and representative membrane protein targets
- Demonstrate that SecYEG enhances membrane localization of inner-membrane proteins in liposome-encapsulated PURE reactions
- Confirm specificity by showing no enhancement for outer-membrane or soluble protein controls
- Integrate the membrane translation module with PPK2-based energy regeneration to support sustained membrane protein synthesis

# DNA Design Strategy

The experimental approach requires DNA constructs encoding both the SecYEG translocon system and representative membrane proteins for validation. All constructs will be designed under T7 promoter control with optimized ribosome binding sites for PURE expression and appropriate fluorescent fusion tags for localization tracking.

**SecYEG System:** SecY, SecE, SecG (core translocon), purified SRP proteins (Ffh, FtsY and 4.5S RNA)

**Target Membrane Proteins:** Inner-membrane proteins (functional targets such as transporters or sensors), outer-membrane proteins (negative controls), and soluble proteins (additional negative controls)

Constructs will be validated by sequence verification, PURE expression testing, and functional assessment in liposome encapsulation assays.

# Materials
| **Product** | **Brand** | **Catalog No.** |
| --- | --- | --- | 
| PURExpress® In Vitro Protein Synthesis Kit | New England Biolabs | E6800L | 
| 16:0-18:1 PC (POPC) | Avanti Research | A80557C | 
| cholesterol (plant) | Avanti Research | A80100P |
| 18:0 Cyanine 5.5 PE | Avanti Research | A81346C |
| D-(+)-Glucose | Sigma Aldrich | 000455143 | 
| OptiPrep | Serumwerk | 1893 | 
| Mineral Oil | Thermo Scientific | 415080010 | 
| Purified Ffh | GenScript | Customized | 
| Purified FtsY | GenScript | Customized | 
| 4.5S RNA | Integrated DNA Technologies | Customized |

| **Construct** | **Function** | **Category** |
| --- | --- | --- |
| SecY | Core translocon channel subunit | SecYEG System |
| SecE | Core translocon subunit | SecYEG System |
| SecG | Core translocon subunit | SecYEG System |
| Ffh | Signal recognition particle protein | SRP System |
| FtsY | SRP receptor | SRP System |
| 4.5S RNA (ffs) | SRP RNA component | SRP System |
| EmrE | Multidrug transporter (inner membrane) | Target Protein |
| E14C | Loss-of-function mutant of EmrE | Target Protein (Control) |

## DNA Constructs

The following constructs are designed and sequencing validated. 
:::{table} DNA constructs for membrane translation module
:label: table-constructs
:align: center

| Construct | Length (bp) | Description |
| --- | --- | --- |
| pT7-SecY-deGFP | 2269 | linear DNA encoding SecY with GFP tag at C-terminus |
| pT7-SecE-deGFP | 1321 | linear DNA encoding SecE with GFP tag at C-terminus |
| pT7-SecG-deGFP | 1270 | linear DNA encoding SecG with GFP tag at C-terminus |
| pOpen-pT7-pSecYEG | 4190 | DNA plasmid encoding SecYEG with different synthetic ribosome-binding sites |
| pOpen-pT7-EmrE | 2422 | DNA plasmid encoding EmrE |
| pOpen-pT7-E14C | 2422 | DNA plasmid encoding E14C |
| pOpen-pT7-EmrE-deGFP | 3112 | DNA plasmid encoding EmrE with GFP tag at C-terminus |
| pOpen-pT7-E14C-deGFP | 3112 | DNA plasmid encoding E14C with GFP tag at C-terminus |

:::

DNA sequences of all the linear constructs and plasmids are attached to this DevNote and are available to download. Reference sequences for all genes are available from public databases (NCBI, UniProt, Shigen *E. coli* genome database). 


# Experimental Design


## Expression Testing in bulks

The first goal is to express SecYEG using the PURE system. To facilitate monitoring of protein expression levels, a GFP tag was genetically encoded at the C-terminus of SecY, SecE, and SecG, respectively. Linear DNA templates containing the pT7 promoter were constructed for expression in the PURE system. PURE reactions containing linear pT7-SecY-deGFP, pT7-SecE-deGFP, and pT7-SecG-deGFP were incubated at 37 °C for 6 hours, and GFP fluorescence signals were subsequently measured using a plate reader. The effects of liposome/ membranes addition on protein expression were also evaluated and compared. The table below summarizes the reaction compositions.

| Component | SecY | SecY+GUV | SecE | SecE+GUV | SecG | SecG+GUV |
| --- | --- | --- | --- | --- | --- | --- |
| NEB PURExpress Solution A | 4 | 4 | 4 | 4 | 4 | 4 |
| NEB PURExpress Solution B | 3 | 3 | 3 | 3 | 3 | 3 |
| RNase Inhibitor | 0.5 | 0.5 | 0.5 | 0.5 | 0.5 | 0.5 |
| pT7-SecY-deGFP (100 ng/ul) | 1 | 1 | 0 | 0 | 0 | 0 |
| pT7-SecE-deGFP (100 ng/ul) | 0 | 0 | 1 | 1 | 0 | 0 |
| pT7-SecG-deGFP (100 ng/ul) | 0 | 0 | 0 | 0 | 1 | 1 |
| GUV | 0 | 0.5 | 0 | 0.5 | 0 | 0.5 |
| Nucleus Free Water | 1.5 | 1 | 1.5 | 1 | 1.5 | 1 |
| Total volume (µL) | 10 | 10 | 10 | 10 | 10 | 10 |


## Expression Testing in cells

After confirming that SecYEG can be successfully expressed in the PURE system, we next investigated whether the synthesized proteins could localize to lipid membranes as expected for membrane proteins. Liposomes encapsulating NEB PURE reactions containing linear SecYEG DNA templates were incubated at 37 °C and monitored by fluorescence microscopy over a 6-hour period. Time-course imaging was performed to evaluate the localization and membrane association of the newly synthesized SecYEG proteins during expression. Below is the preparation of liposomes.

:::::{tab-set}

::::{tab-item} Inner Solution
:::{table}
:label: tbl-inners
| **Component** | **Liposomes (SecY)** | **Liposomes (SecE)** | **Liposomes (SecG)** |
| --- | --- | --- | --- |
| NEB PURExpress Solution A | 12 | 12 | 12 | 
| NEB PURExpress Solution B | 9 | 9 | 9 |
| RNase Inhibitor | 1.5 | 1.5 | 1.5 |
| pT7-SecY-deGFP (100 ng/ul) | 3 | 0 | 0 |
| pT7-SecE-deGFP (100 ng/ul) | 0 | 3 | 0 |
| pT7-SecG-deGFP (100 ng/ul) | 0 | 0 | 3 | 
| Optiprep | 1 | 1 | 1 | 
| Nucleus Free Water | 3.5 | 3.5 | 3.5 | 
| Total volume (µL) | 30 | 30 | 30 | 30 | 30 | 30 |
:::
::::

::::{tab-item} Membrane
:::{table}
:label: tbl-membrane
| **Lipid** | **Target Percentage %** | **Molecular Weight** | **Concentration(mg/mL)** | **Volume to Add (uL)** |
| --- | --- | --- | --- | --- |
| POPC | 70 | 760.076 | 25 | 162.17 |
| Cholesterol | 29.95 | 386.66 | 50 | 17.65 |
| 18:0 Cyanine 5.5 PE | 0.05 | 1301.72 | 1 | 5.21 |
:::
::::

::::{tab-item} Outer Solution
:::{table}
:label: tbl-outers
| **Component** | **Target Concentration(mM)** |
| --- | --- |
| Glucose | 870 | 

::::
:::::

**Preparation of the Lipid-Oil Mixture (5mg/mL):**

1. Add 1 mL mineral oil in the 2 mL small glass jar.
2. Add lipids shown in the {ref}`tbl-membrane` into the glass jar on top of the mineral oil.   
3. Vortex the lipid-oil mixture for 10 seconds.
4. Put the glass jar in the bead-loaded hot bath at 55 °C for 4 hours (keep the jar uncovered without lid).
5. Place the jar (with lid) containing lipid-in-oil solution at RT for 10 mins before using. 


**Formation of liposomes:**

1. Add 300 uL of outer solution in tube A.
2. Add 120 uL of the lipid-oil mixture on top of 20 uL of inner solution, and then do washboard for 50 times to form emulsion.
3. Add the milky solution (after washboarding) from the previous step on top of the the outer solution in tube A.
4. Centrifuge at RT for 10 mins at 9000 xg.
5. Remove the top residual oil until 100 uL of solution in the 1.5 mL Eppendorf tube.
6. Resuspend the pellet and collect liposomes.



## Membrane Localization Assay

The core validation will compare membrane protein localization in liposome-encapsulated PURE reactions with and without the SecYEG system. Target membrane proteins are expressed under two conditions:

- **PURE + SRP:** No SecYEG tranlocons present but only with signal recognition particle (SRP)
- **PURE + SRP + SecYEG:** SecYEG components co-expressed with target proteins

The small multidrug resistance (SMR) transporter EmrE from Escherichia coli and its loss-of-function mutant, E14C, were used as model membrane proteins in this study. Both proteins were fused to deGFP at their C-termini to facilitate visualization of membrane localization by fluorescence microscopy.

:::::{tab-set}

::::{tab-item} EmrE liposomes
**Preparation of the Inner solution:**
:::{table}
:label: tbl-local-EmrE
| **Component** | **Liposomes (-SecYEG)** | **Liposomes (+SecYEG)** |
| --- | --- | --- |
| NEB PURExpress Solution A | 12 | 12 |
| NEB PURExpress Solution B | 9 | 9 |
| RNase Inhibitor | 1.5 | 1.5 |
| pOpen-pT7-EmrE-deGFP (56.7 nM) | 1.5 | 1.5 |
| pOpen-pT7-pSecYEG (59 nM) | 0 | 1.5 |
| Ffh (10.24 uM) | 0.44 | 0.44 |
| FtsY (21.65 uM) | 1.04 | 1.04 |
| 4.5S RNA (67 uM) | 0.6 | 0.6 |
| Optiprep | 1 | 1 |
| Nucleus Free Water | 3.16 | 1.66 | 
| Total volume (µL) | 30 | 30 | 
:::
::::

::::{tab-item} E14C liposomes
**Preparation of the Inner solution:**
:::{table}
:label: tbl-local-E14C
| **Component** | **Liposomes (-SecYEG)** | **Liposomes (+SecYEG)** |
| --- | --- | --- |
| NEB PURExpress Solution A | 12 | 12 |
| NEB PURExpress Solution B | 9 | 9 |
| RNase Inhibitor | 1.5 | 1.5 |
| pOpen-pT7-E14C-deGFP (56.7 nM) | 1.5 | 1.5 |
| pOpen-pT7-pSecYEG (59 nM) | 0 | 1.5 |
| Ffh (10.24 uM) | 0.44 | 0.44 |
| FtsY (21.65 uM) | 1.04 | 1.04 |
| 4.5S RNA (67 uM) | 0.6 | 0.6 |
| Optiprep | 1 | 1 |
| Nucleus Free Water | 3.16 | 1.66 | 
| Total volume (µL) | 30 | 30 | 
:::
::::

**Preparation of the Lipid-Oil Mixture (5mg/mL):**
| **Lipid** | **Target Percentage %** | **Molecular Weight** | **Concentration(mg/mL)** | **Volume to Add (uL)** |
| --- | --- | --- | --- | --- |
| POPC | 70 | 760.076 | 25 | 162.17 |
| Cholesterol | 29.95 | 386.66 | 50 | 17.65 |
| 18:0 Cyanine 5.5 PE | 0.05 | 1366.32 | 1 | 5.21 |

**Preparation of the outer solution:**
| **Component** | **Target Concentration(mM)** |
| --- | --- |
| Glucose | 870 | 
:::::

**Formation of liposomes:**

1. Add 300 uL of outer solution in tube A.
2. Add 120 uL of the lipid-oil mixture on top of 20 uL of inner solution, and then do washboard for 50 times to form emulsion.
3. Add the milky solution (after washboarding) from the previous step on top of the the outer solution in tube A.
4. Centrifuge at RT for 10 mins at 9000 xg.
5. Remove the top residual oil until 100 uL of solution in the 1.5 mL Eppendorf tube.
6. Resuspend the pellet and collect liposomes.

## Substrate Transport Assay
Membrane localization of a protein does not necessarily indicate that the protein is functionally active. Therefore, we investigated whether incorporation of the Sec translocon affects the substrate transport activity of EmrE. Ethidium bromide (EtBr), a well-characterized substrate of EmrE, was employed as the fluorescent reporter. Since EtBr exhibits enhanced fluorescence upon binding to nucleic acids and the nucleic acids are confined within the liposome lumen, EtBr transport into the liposomes can be detected by an increase in internal fluorescence.

After cell-free expression of EmrE, EtBr was introduced into the outer solution to the final concentration to be 0.25 ug/ml, and fluorescence signals within liposomes were monitored by microscopy over time. The accumulation of EtBr inside the liposomes was then monitored by fluorescence microscopy. Functional EmrE is expected to facilitate EtBr accumulation inside the liposomes, resulting in elevated intraliposomal fluorescence. To assess whether any observed transport activity was specifically mediated by EmrE, the transport-deficient mutant E14C was analyzed under the same experimental conditions as a negative control.

:::::{tab-set}

::::{tab-item} EmrE liposomes
**Preparation of the Inner solution:**
:::{table}
:label: tbl-transport-EmrE
| **Component** | **EmrE Liposomes (+SecYEG)** | **EmrE Liposomes (-SecYEG)** | **Control Liposomes** |
| --- | --- | --- | --- |
| NEB PURExpress Solution A | 12 | 12 | 12 |
| NEB PURExpress Solution B | 9 | 9 | 9 |
| RNase Inhibitor | 1.5 | 1.5 | 1.5 |
| pOpen-pT7-EmrE-deGFP (56.7 nM) | 1.5 | 1.5 | 0 |
| pOpen-pT7-pSecYEG (59 nM) | 1.5 | 0 | 0 |
| Ffh (10.24 uM) | 0.44 | 0.44 | 0.44 |
| FtsY (21.65 uM) | 1.04 | 1.04 | 1.04 |
| 4.5S RNA (67 uM) | 0.6 | 0.6 | 0.6 |
| Optiprep | 1 | 1 | 1 |
| Nucleus Free Water | 1.42 | 2.92 | 4.42 |
| Total volume (µL) | 30 | 30 | 30 |
:::
::::

::::{tab-item} E14C liposomes
**Preparation of the Inner solution:**
:::{table}
:label: tbl-transport-E14C
| **Component** | **E14C Liposomes (+SecYEG)** | **E14C Liposomes (-SecYEG)** | **Control Liposomes** |
| --- | --- | --- | --- |
| NEB PURExpress Solution A | 12 | 12 | 12 |
| NEB PURExpress Solution B | 9 | 9 | 9 |
| RNase Inhibitor | 1.5 | 1.5 | 1.5 |
| pOpen-pT7-E14C-deGFP (56.7 nM) | 1.5 | 1.5 | 0 |
| pOpen-pT7-pSecYEG (59 nM) | 1.5 | 0 | 0 |
| Ffh (10.24 uM) | 0.44 | 0.44 | 0.44 |
| FtsY (21.65 uM) | 1.04 | 1.04 | 1.04 |
| 4.5S RNA (67 uM) | 0.6 | 0.6 | 0.6 |
| Optiprep | 1 | 1 | 1 |
| Nucleus Free Water | 1.42 | 2.92 | 4.42 |
| Total volume (µL) | 30 | 30 | 30 |
:::
::::

**Preparation of the Lipid-Oil Mixture (5mg/mL):**
| **Lipid** | **Target Percentage %** | **Molecular Weight** | **Concentration(mg/mL)** | **Volume to Add (uL)** |
| --- | --- | --- | --- | --- |
| POPC | 70 | 760.076 | 25 | 162.17 |
| Cholesterol | 29.95 | 386.66 | 50 | 17.65 |
| 18:0 Cyanine 5.5 PE | 0.05 | 1366.32 | 1 | 5.21 |

**Preparation of the outer solution:**
| **Component** | **Target Concentration(mM)** |
| --- | --- |
| Glucose | 870 | 
:::::

**Formation of liposomes:**

1. Add 300 uL of outer solution in tube A.
2. Add 120 uL of the lipid-oil mixture on top of 20 uL of inner solution, and then do washboard for 50 times to form emulsion.
3. Add the milky solution (after washboarding) from the previous step on top of the the outer solution in tube A.
4. Centrifuge at RT for 10 mins at 9000 xg.
5. Remove the top residual oil until 100 uL of solution in the 1.5 mL Eppendorf tube.
6. Resuspend the pellet and collect liposomes.

**Preparation of EtBr solution:**
| **Component** | **Stock Concentration(mM)** | **Volume to Add (uL)** |
| --- | --- | --- |
| Glucose | 870 | 99.5 |
| EtBr | 0.254 | 0.5 |

**Preparation of imaging:**
1. Liposomes are incubated at 37 °C for 3 hrs.
2. 20 uL of EtBr solution prepared above is added to the 384-well microscope plate.
3. 20 ul of the liposome solution is added on top of it.
4. Wait for 10 minutes for the liposomes to settle sown to the plate bottom before taking images.


# Observations and Experimental Results

## SecYEG Expression Testing
The first experiment focused on expression testing. Linear DNA templates encoding pT7-SecY-deGFP, pT7-SecE-deGFP, and pT7-SecG-deGFP were individually expressed using the NEB PURExpress system. Protein expression levels were evaluated by fluorescence measurements to quantify protein yield and monitor translation kinetics. The results demonstrated successful expression of all three SecYEG components in the PURE system, although the expression level of SecG-deGFP {ref}`fig:SecG-deGFP` was significantly higher than those of SecY-deGFP {ref}`fig:SecY-deGFP` and SecE-deGFP {ref}`fig:SecE-deGFP`.

To investigate whether the presence of a membrane environment could enhance protein expression, liposomes were added to the PURE reactions. These liposomes were prepared using 870 mM glucose as the outer solution and 870 mM glucose supplemented with 3.3% OptiPrep as the inner solution. These liposomes were prepared using 870 mM glucose as the outer solution and 870 mM glucose supplemented with 3.3% OptiPrep as the inner solution. However, the addition of liposomes did not result in a substantial increase in expression levels for any of the proteins. Only the SecG-deGFP reactions exhibited a slight increase in GFP fluorescence in the presence of liposomes, whereas little to no improvement was observed for SecY-deGFP or SecE-deGFP. These results suggest that the availability of membrane surfaces alone is insufficient to significantly enhance the expression of SecY and SecE under the current experimental conditions.


:::::{tab-set}

::::{tab-item} SecY-deGFP 
:sync: tab1-1
:::{figure} ./general/Platereader/SecY-deGFP.png
:label: fig:SecY-deGFP
GFP fluorescence signal in PURE reactions incubated at 37 °C for 6 hours. The reaction contains linear pT7-SecY-deGFP DNA.
Increasing green fluorescence was observed overtime. Addition of liposomes does not significantly affect the expression level.
:::
::::

::::{tab-item} SecE-deGFP
:sync: tab1-2
:::{figure} ./general/Platereader/SecE-deGFP.png
:label: fig:SecE-deGFP
GFP fluorescence signal in PURE reactions incubated at 37 °C for 6 hours. The reaction contains linear pT7-SecE-deGFP DNA.
Increasing green fluorescence was observed overtime. Addition of liposomes does not significantly affect the expression level.
:::
::::

::::{tab-item} SecG-deGFP
:sync: tab1-3
:::{figure} ./general/Platereader/SecG-deGFP.png
:label: fig:SecG-deGFP
GFP fluorescence signal in PURE reactions incubated at 37 °C for 6 hours. The reaction contains linear pT7-SecG-deGFP DNA.
Increasing green fluorescence was observed overtime. Addition of liposomes slightly increases the expression level.
:::
::::

:::::


The observed differences in expression levels are likely related to the structural complexity of the proteins. ({ref}`fig:Topology-of-SecYEG`). SecG is structurally simpler and contains only two transmembrane domains (TMDs), whereas SecY is a substantially larger and more complex membrane protein containing ten TMDs. SecE contains three TMDs along with a long amphipathic region that interacts closely with SecY [[Andreas K.J *et al.* 2004](https://doi.org/10.1016/j.bbamcr.2004.02.009)]. The lower expression levels of SecY-deGFP and SecE-deGFP compared to SecG-deGFP may therefore be attributed to their higher hydrophobicity and greater membrane topology complexity, which can hinder efficient translation, folding, and membrane insertion in the PURE system.

:::{figure} ./general/Schematic-Topology of SecYEG.jpg
:label: fig:Topology-of-SecYEG
:align: center
:width: 75%

:::


After confirming that SecYEG can be successfully expressed using the PURE system, we next examined whether the proteins could localize to lipid membranes as expected for membrane proteins. For SecY-deGFP–containing liposomes, GFP fluorescence was observed on the membranes of a subset of liposomes based on fluorescence microscopy images {ref}`fig:SecY-GUV`. However, the fraction of liposomes exhibiting clear fluorescent membrane rings was lower compared to SecE-deGFP {ref}`fig:SecE-GUV` and SecG-deGFP sample {ref}`fig:SecG-GUV`. Among all conditions, SecG-deGFP–containing liposomes showed the most intense membrane-associated green fluorescence. Overall, the percentage of liposomes displaying membrane-localized GFP followed the trend: SecG-deGFP > SecE-deGFP > SecY-deGFP. These results indicate that all three proteins (SecY, SecE, and SecG) are able to localize to liposome membranes under the current PURE-liposome system, while SecG exhibits more efficient membrane association compared to SecE and SecY. The successful membrane localization of SecY, SecE, and SecG individually indicates that the liposome membrane provides a suitable environment for the potential assembly of the SecYEG translocon.

:::::{tab-set}

::::{tab-item} SecY liposomes
:sync: tab2-1
:::{figure} ./general/Localization/SecY-deGFP.png
:label: fig:SecY-GUV
Microscopy fluorescent images of liposomes expressing SecY-deGFP after incubation at 37 °C for 6 hours. Some liposomes show green fluorescent rings, indicating membrane localization of SecY-deGFP. Left: Membranes (647 nm); Middle: GFP (488 nm); Right: Merge.
:::
::::

::::{tab-item} SecE liposomes
:sync: tab2-2
:::{figure} ./general/Localization/SecE-deGFP.png
:label: fig:SecE-GUV
Microscopy fluorescent images of liposomes expressing SecE-deGFP after incubation at 37 °C for 6 hours. Some liposomes show green fluorescent rings, indicating membrane localization of SecE-deGFP. Left: Membranes (647 nm); Middle: GFP (488 nm); Right: Merge.
:::
::::

::::{tab-item} SecG liposomes
:sync: tab2-3
:::{figure} ./general/Localization/SecG-deGFP.png
:label: fig:SecG-GUV
Microscopy fluorescent images of liposomes expressing SecG-deGFP after incubation at 37 °C for 6 hours. Most liposomes show strong green fluorescent rings, indicating membrane localization of SecG-deGFP. Left: Membranes (647 nm); Middle: GFP (488 nm); Right: Merge.
:::
::::

:::::

## Effect of SecYEG Incorporation on EmrE Membrane Localization

Fluorescence microscopy images revealed comparable numbers of liposomes exhibiting green fluorescent rings regardless of whether the pT7-pSecYEG plasmid and signal recognition particle (SRP) were included during protein expression. Furthermore, the average fluorescence intensity of the membrane-localized rings was similar between liposomes expressing EmrE-deGFP in the presence and absence of SecYEG and SRP ({ref}`fig:local-EmrE` and {ref}`fig:local-EmrE-Sec`). Quantitative image analysis further confirmed that neither the fraction of liposomes displaying membrane-localized fluorescence nor the average ring fluorescence intensity differed significantly between the two conditions (results not shown).

These results suggest that incorporation of SecYEG translocons does not substantially enhance the membrane integration of EmrE under the experimental conditions tested. Similar observations were obtained for the E14C mutant control, where no significant differences in membrane localization were detected between liposomes containing SecYEG and SRP and those lacking these components ({ref}`fig:local-E14C` and {ref}`fig:local-E14C-Sec`). Together, these findings indicate that SecYEG-mediated insertion does not measurably improve the membrane incorporation of either EmrE or the E14C mutant in this cell-free liposome system. 

::::::{tab-set}

:::::{tab-item} EmrE-containing liposomes
:sync: tab3-1
::::{grid} 1 1 1 1

:::{figure} ./general/Localization/EmrE.png
:label: fig:local-EmrE
:width: 100%
Time series of PURE cells containing EmrE without SecYEG and SRP system. Top: liposome membranes (647nm fluorescnece channel); Bottom: EmrE-deGFP (488nm fluorescence channel). 
:::

:::{figure} ./general/Localization/EmrE_SecYEG.png
:label: fig:local-EmrE-Sec
:width: 100%
Time series of PURE cells containing EmrE with SecYEG and SRP system. Top: liposome membranes (647nm fluorescnece channel); Bottom: EmrE-deGFP (488nm fluorescence channel). 
:::
Time series of PURE cells containing EmrE with (bottom) and without (top) Sec translocons.
::::
:::::

:::::{tab-item} E14C-containing liposomes
:sync: tab3-2
::::{grid} 1 1 1 1

:::{figure} ./general/Localization/E14C.png
:label: fig:local-E14C
:width: 100%
Time series of PURE cells containing E14C without SecYEG and SRP system. Top: liposome membranes (647nm fluorescnece channel); Bottom: EmrE-deGFP (488nm fluorescence channel). 
:::

:::{figure} ./general/Localization/E14C_SecYEG.png
:label: fig:local-E14C-Sec
:width: 100%
Time series of PURE cells containing E14C with SecYEG and SRP system. Top: liposome membranes (647nm fluorescnece channel); Bottom: EmrE-deGFP (488nm fluorescence channel). 
:::
Time series of PURE cells containing EmrE with (bottom) and without (top) Sec translocons.
::::
:::::
::::::



## Effect of SecYEG Translocons in EmrE-Mediated Substrate Transport

After confirming the successful expression and membrane localization of EmrE, its transport activity was evaluated using the EtBr uptake assay. Fluorescence microscopy showed that EmrE-containing liposomes accumulated EtBr much more rapidly than control liposomes lacking EmrE. In many cases, a substantial increase in intraliposomal fluorescence was observed within the first 10 minutes after EtBr addition, indicating that EmrE remained functionally active and facilitated EtBr transport into the liposome lumen. In contrast, control liposomes generally exhibited low fluorescence throughout the experiment, with only a slow increase in signal over time {ref}`fig:trans_EmrE-Control`. The weak fluorescence observed in some control liposomes is likely attributable to minor membrane leakage or passive EtBr permeation.

When comparing EmrE-expressing liposomes with and without the SecYEG/SRP system ({ref}`fig:trans_EmrE-Sec` and {ref}`fig:trans_EmrE`), liposomes containing SecYEG and SRP displayed faster fluorescence accumulation, particularly during the first 15 minutes following EtBr addition. Although both conditions eventually reached similar fluorescence plateaus after approximately 30 minutes, the accelerated uptake kinetics suggest that SecYEG and SRP increased the amount of functionally active EmrE incorporated into the membrane.


:::::{tab-set}

::::{tab-item} EmrE Liposomes (+SecYEG)
:sync: tab4-1
:::{figure} ./general/EtBr transporting/EmrE/EmrE_SecYEG.png
:label: fig:trans_EmrE-Sec
Time-series fluorescence microscopy of liposomes containing pT7-EmrE and pT7-pSecYEG DNAs together with purified SRP proteins, incubated at 37 °C. Intraliposomal EtBr fluorescence was monitored in the 561-nm channel (10 ms exposure, 40% laser intensity). Red fluorescence increased over time, indicating progressive accumulation of EtBr within the liposomes.
:::
::::

::::{tab-item} EmrE Liposomes 
:sync: tab4-2
:::{figure} ./general/EtBr transporting/EmrE/EmrE.png
:label: fig:trans_EmrE
Time-series fluorescence microscopy of liposomes containing pT7-EmrE DNA and purified SRP proteins, incubated at 37 °C. Intraliposomal EtBr fluorescence was monitored in the 561-nm channel (10 ms exposure, 40% laser intensity). Red fluorescence increased over time, indicating progressive accumulation of EtBr within the liposomes.
:::
::::

::::{tab-item} Control Liposomes 
:sync: tab4-3
:::{figure} ./general/EtBr transporting/EmrE/Control.png
:label: fig:trans_EmrE-Control
Time-series fluorescence microscopy images of liposomes containing only purified SRP proteins, incubated at 37 °C. Images were acquired in the 561 channel (10 ms exposure, 40% intensity) for EtBr intraliposome fluorescence. No significant increase in red fluorescence was observed in liposomes overtime.
:::
::::

:::::

To further validate this observation, the transport-deficient mutant E14C was analyzed under the same conditions. In contrast to wild-type EmrE, E14C liposomes exhibited minimal fluorescence increases and reached substantially lower final fluorescence intensities. In addition, there's nosignificant fluorescence difference between the E14C liposomes and the control liposomes. Together, these results indicate that SecYEG-mediated insertion enhances the transport activity of EmrE, despite having little effect on its overall membrane localization.

:::::{tab-set}

::::{tab-item} E14C Liposomes (+SecYEG)
:sync: tab5-1
:::{figure} ./general/EtBr transporting/E14C/E14C_SecYEG.png
:label: fig:trans_E14C-Sec
Time-series fluorescence microscopy of liposomes containing pT7-E14C and pT7-pSecYEG DNAs together with purified SRP proteins, incubated at 37 °C. Intraliposomal EtBr fluorescence was monitored in the 561-nm channel (10 ms exposure, 40% laser intensity). No significant increase in red fluorescence was observed in liposomes overtime.
:::
::::

::::{tab-item} E14C Liposomes 
:sync: tab5-2
:::{figure} ./general/EtBr transporting/E14C/E14C.png
:label: fig:trans_E14C
Time-series fluorescence microscopy of liposomes containing pT7-E14C DNA and purified SRP proteins, incubated at 37 °C. Intraliposomal EtBr fluorescence was monitored in the 561-nm channel (10 ms exposure, 40% laser intensity). No significant increase in red fluorescence was observed in liposomes overtime.
:::
::::

::::{tab-item} Control Liposomes 
:sync: tab5-3
:::{figure} ./general/EtBr transporting/E14C/Control.png
:label: fig:trans_E14C-Control
Time-series fluorescence microscopy images of liposomes containing only purified SRP proteins, incubated at 37 °C. Images were acquired in the 561 channel (10 ms exposure, 40% intensity) for EtBr intraliposome fluorescence. No significant increase in red fluorescence was observed in liposomes overtime.
:::
::::

:::::



# Future works
In this DevNote, we demonstrated the importance of SecYEG translocons in improving the activity of functional inner membrane proteins, using EmrE as our initial model system. While these results highlight the role of SecYEG in membrane protein biogenesis, SecYEG is also a central component of the bacterial protein secretion machinery.

As a next step, we will investigate whether PURE-expressed SecYEG can mediate the translocation of secretory proteins. Specifically, we will test the translocation of proOmpA, a well-established model substrate for Sec-dependent protein secretion. Successful translocation would provide strong evidence that our reconstituted SecYEG complexes are not only integrated into the membrane but are also functionally active. 

In parallel, we will continue to develop and evaluate additional assays to further verify the membrane integration, assembly, and functionality of SecYEG complexes in liposomes.


