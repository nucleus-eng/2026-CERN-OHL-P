---
# Ensure that this title is the same as the one in `myst.yml`
title: "Developer Cell: Project Introduction"
abstract: |
  The goal of this project is to build a "Developer Cell" that enables development and deployment of interoperable synthetic cell modules at increasing scale. The baseline Developer Cell will include an ATP/GTP-recycling energy module for improved expression capacity, a protease control module for tunable gene expression and protein homeostasis, and a membrane translation module for inserting functional membrane proteins to support active transport and cell functions.
---
# Overview

Advancing synthetic cell science and engineering to incorporate all essential functions of life and beyond, with fully understood components and emergent functions, will require a shared cell platform capable of integrating increasingly sophisticated cell modules from many developers. We have thus far introduced PURE-based synthetic cells as a baseline option for shared engineering, and demonstrated implementation of detector, emitter, and responder modules. While the PURE system forms an excellent, defined base cytosol for implementing simple modules in synthetic cells, its capacity for supporting sophisticated behaviors is quite limited. Critically, the system can only express proteins for a few hours until it runs out of energy and accumulates toxic waste products, with no ability to tune protein production or maintain energy and waste balance.

Here, we propose overcoming these challenges and enabling the shared development of increasingly capable synthetic cells by building a baseline “Developer Cell” that extends [Nucleus PURE-based synthetic cells](https://nucleus.bnext.bio/container-protocols/hello-world-pure-liposomes) with integrated energy recycling, dynamic expression control, and membrane protein translation ({ref}`fig:DeveloperCell`). These additional functions have individually already been demonstrated by the community. We will implement them as Nucleus modules and integrate them for use in the Nucleus Distribution. We will optimize the Developer Cell to support additional modules and produce tools and workflows to enable and accelerate further module integration and development. 

:::{figure} ./figures/DeveloperCell.png
:label: fig:DeveloperCell
:width: 75%
The Developer Cell. We will build an integrated chassis for synthetic cell engineering that incorporates energy generation, protein control, and membrane protein translation, needed for large-scale integration.
:::

# Project

The Developer Cell will consist of three modules integrated with [Nucleus PURE](https://nucleus.bnext.bio/cytosol-documentation) and [Nucleus PURE-based synthetic cells](https://nucleus.bnext.bio/container-protocols/hello-world-pure-liposomes):

### Energy module
The PPK energy module will increase the metabolic efficiency of the base cytosol and cell, improving protein yield and kinetics and forming the basis for continuous energy maintenance. Increased energy and protein production is critical as more and more-complex cell systems are implemented within synthetic cells.

PURE uses GTP and ATP to power protein synthesis, with GTP fueling transcription initiation and translation elongation, and ATP facilitating recharging of tRNAs with amino acids by aminoacyl-tRNA synthetases. GTP and ATP are metabolized to GDP and AMP, respectively. PURE uses creatine kinase (CK), myosin kinase (MK), and nucleoside disphosphate kinase (NDK) to rephosphorylate GDP and AMP using energy from creatine phosphate, producing inorganic phosphate and diphosphate as byproducts; these phosphates are a key factor limiting the yield of PURE, accumulating and eventually poisoning the cytosol ([Jurado 2023](https://doi.org/10.1101/2023.08.14.553301)).
We will implement a bifunctional polyphosphate kinase (PPK) from C. hutchinsonii that regenerates ATP and GTP from diphosphate and inorganic phosphate respectively ([Wang 2019](10.1021/acssynbio.9b00456)). PPK has been shown to increase PURE protein yield by more than 20%, while increasing translation kinetics five-fold.

### Control module
The ClpXP control module enables temporal control of protein production and implementation of multigene modules with varying stoichiometry. PURE does not contain proteases—an advantage in some circumstances, but a limitation on the ability to control system dynamics. For example, once a sensor implemented in PURE is activated, it may never turn off because the output reporter protein is never degraded. As developers strive to implement more sophisticated modules, and cells of greater complexity, protein degradation is critical to enable cellular functions such as level matching, homeostasis, and time-ordered behavior such as cell cycle control ([McGinness 2006](10.1016/j.molcel.2006.04.027)).

We will implement the ClpXP protease to continuously degrade targeted proteins. ClpXP is an archetypal protease composed of two subunits: the ClpX ATPase and the ClpP peptidase ([Baker 2011](10.1016/j.bbamcr.2011.06.007)). Its function has been demonstrated within PURE ([Niederholtmeyer 2013](https://doi.org/10.1073/pnas.1311166110). ClpXP targets proteins labeled with a C-terminal ssrA tag, allowing its activity to be selectively targeted to desired proteins without indiscriminate degradation of the base cytosol machinery.

### Membrane translation module
The SecYEG membrane translation module allows for the expression and insertion of functional proteins on the synthetic cell membrane, enabling the implementation of active transporters to fuel metabolism and excrete waste, molecular sensors, and membrane-based cell-cell communication.

At present, most synthetic cell designs incorporate only simple channel pores for membrane control (e.g., alpha hemolysin), because translation and insertion of more complex membrane proteins requires ancillary proteins not present in PURE. The SecYEG translocon is the primary mechanism of membrane protein insertion in E. coli and other bacteria, and has been shown to increase both insertion rate and activity of membrane proteins in synthetic cells containing PURE ([Matsubayashi 2014](10.1007/s11084-014-9389-y), [Ohta 2016](10.1038/srep36466), [Schoenmakers 2024](10.1093/synbio/ysae007)). SecYEG forms a sealed pore connecting the cell cytoplasm to the periplasm and lipid membrane. Proteins are targeted for translocation by several mechanisms including SecA, the SRP, and YidC ([Oswald 2021](10.3389/fmolb.2021.664241)). We will target YidC as the targeting co-protein.

We will integrate SecYEG into Nucleus synthetic cells, enabling membrane protein expression. The ability to install active transporters in the cell membrane will enable a means to provide substantially more energy to synthetic cells and to excrete waste byproducts (such as phosphate by the E. coli phosphate homeostasis transporters PitA and PitB ([McCleary 2017](doi:10.5772/67283)). In microfluidic reactors, small molecule dialysis through an inorganic membrane has been shown to increase protein yield in PURE by 6-7 times, with expression lifetime increasing from 2 hours to over 30 hours ([Lavickova 2022](10.1021/acssynbio.2c00453), [Kazuta 2014](10.1016/j.jbiosc.2014.04.019)). Using membrane transporters, we expect that small molecule exchange will lead to similar yield improvements within synthetic cells.

 
:::{table} Integrated modules comprising the Developer Cell. 
:label: table-modules
:align: center
| **Module** | **Description** | **Components** |
| --- | --- | --- |
| **Energy:** Bifunctional polyphosphate kinase | Regenerates ATP from AMP | PPK |
| **Control:** targeted protein degradation | ClpXP protease selectively degrades labeled proteins. | ClpX <br>  ClpP |
| **Membrane translation:** SecYEG translocon | The Sec translocon transports membrane proteins and installs them in the membrane. | SecY <br> SecE <br> SecG <br> YidC <br> SRP <br> FtsY
 |
:::

Taken together, the energy, control and membrane translation modules will enable robust metabolism, tunable control, and the ability to express membrane proteins in the Developer Cell ({ref}`table-modules`). These integrated functions will provide support for more advanced synthetic cell functions: higher energy will enable expression of more and larger functional pathways; protein degradation will enable dynamic control of integrated modules; and translation of membrane proteins will open access to critical proteins for nutrient influx and waste efflux.  

# Timeline
We initiated this project in January 2025. We plan to complete development of the Developer Cell and associated tooling by June 2026, with the following expected module integration milestones:
1. Energy module - September 2025
2. Control module - December 2025
3. Membrane Translation module - June 2026

We will be sharing progress along the way.

**Acknowledgments**

This work is supported by the Astera Institute and Sloan Foundation (Grant G-2024-22735).