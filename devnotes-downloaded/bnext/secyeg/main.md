---
title: "Membrane Translation Module Development Plan"
abstract: |
  The Membrane Translation Module aims to enable functional membrane protein expression and integration in synthetic cells through the SecYEG translocon system. We will develop DNA constructs encoding SecYEG and target membrane proteins, validate their expression in the PURE system, and demonstrate enhanced membrane localization in liposome-encapsulated reactions. This module will support active transporters, molecular sensors, and membrane-based communication in the Developer Cell platform.
---

# Overview

Current synthetic cell designs predominantly rely on simple channel pores for membrane regulation, as the expression and proper insertion of complex membrane proteins typically require chaperone support. Challenges such as improper folding and incorrect insertion orientation severely limit the functional use of membrane proteins in synthetic cell applications. The SecYEG translocon, the primary mechanism for membrane protein insertion in *E. coli* and other bacteria, has been demonstrated to enhance both insertion efficiency and functional activity of membrane proteins in PURE-based synthetic cells [[Sato *et al.* 2016](https://doi.org/10.1038/srep36466)].

The Membrane Translation Module integrates the SecYEG translocon into Developer synthetic cells to improve expression, insertion, orientation, and functionality of membrane proteins ({ref}`fig:membrane-overview`). By enabling the installation of active transporters in the cell membrane, this module will provide a foundation for substantially increased energy production and waste excretion, allowing synthetic cells to more closely mimic natural cell functions with broader applications.

:::{figure} ./figures/membrane-schematic.png
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

**SecYEG System:** SecY, SecE, SecG (core translocon), YidC (insertase co-factor), and soluble protein controls

**Target Membrane Proteins:** Inner-membrane proteins (functional targets such as transporters or sensors), outer-membrane proteins (negative controls), and soluble proteins (additional negative controls)

Constructs will be validated by sequence verification, PURE expression testing, and functional assessment in liposome encapsulation assays.

## Planned Constructs

The following constructs will be designed and validated for this module. All sequences are from *E. coli* unless otherwise noted.

:::{table} Planned DNA constructs for membrane translation module
:label: table-constructs
:align: center

| Construct | Function | Length (bp) | Category |
| --- | --- | --- | --- |
| SecY | Core translocon channel subunit | 1317 | SecYEG System |
| SecE | Core translocon subunit | 336 | SecYEG System |
| SecG | Core translocon subunit | 336 | SecYEG System |
| YidC | Membrane protein insertase | 1719 | SecYEG System |
| Ffh | Signal recognition particle protein | 1377 | SRP System |
| FtsY | SRP receptor | 1824 | SRP System |
| 4.5S RNA (ffs) | SRP RNA component | 114 | SRP System |
| EmrE | Multidrug transporter (inner membrane) | 330 | Target Protein |
| EmrE E14C | EmrE variant for fluorescent labeling | 330 | Target Protein |
| MscS | Mechanosensitive channel (inner membrane) | 858 | Target Protein |
| MscL | Large mechanosensitive channel (inner membrane) | 411 | Target Protein |
| proOmpA | Outer membrane protein precursor | 1011 | Control Protein |
| SecA | ATPase motor protein | 2721 | Control Protein |

:::

Reference sequences for all constructs are available from public databases (NCBI, UniProt, Shigen *E. coli* genome database).

# Experimental Design

## Expression Testing

SecYEG components and target proteins will be expressed in Nucleus Cytosol (PURE system) at optimal magnesium acetate concentration (8 mM). Expression will be assessed by fluorescence measurement to quantify protein yield and translation kinetics.

## Membrane Localization Assays

The core validation will compare membrane protein localization in liposome-encapsulated PURE reactions with and without the SecYEG system. Target membrane proteins will be expressed under two conditions:

- **PURE only:** No SecYEG co-factors present
- **PURE + SecYEG:** SecYEG components co-expressed with target proteins

Membrane localization will be quantified by confocal microscopy measuring (1) fraction of liposomes showing membrane-localized fluorescence rings and (2) average membrane fluorescence intensity. Success criteria include statistically significant enhancement in either metric when SecYEG is present for inner-membrane proteins, but not for outer-membrane or soluble protein controls.

## Energy Module Integration

Following SecYEG validation, integration with the PPK2 energy regeneration module [[Wang *et al.* 2019](https://doi.org/10.1021/acssynbio.9b00456)] will be tested to enable sustained membrane protein expression. Performance will be compared across CP/CK energy module alone, PPK2 module alone, and combined CP/CK + PPK2 modules.

# Expected Outcomes and Next Steps

Based on published demonstrations of SecYEG function in cell-free systems [[Matsubayashi *et al.* 2014](https://doi.org/10.1002/anie.201403929)], we anticipate 2-5 fold enhancement in membrane localization metrics (fraction of liposomes with membrane signal or average membrane fluorescence intensity) when SecYEG is present, specifically for inner-membrane protein targets. Outer-membrane and soluble protein controls should show no enhancement, confirming SecYEG specificity. The module should be compatible with PPK2-based energy regeneration, enabling sustained membrane protein synthesis.

Future extensions include expanding the membrane protein library to metabolic transporters (lactate, acetate exporters), integrating membrane-based sensors and cell-cell communication systems, optimizing SecYEG stoichiometry for maximal insertion efficiency, and characterizing membrane protein orientation and topology. This module represents a critical capability for synthetic cells, enabling installation of active membrane components for enhanced metabolism, waste management, and environmental sensing.