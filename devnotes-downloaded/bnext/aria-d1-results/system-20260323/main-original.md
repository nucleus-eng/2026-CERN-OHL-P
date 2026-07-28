---
title: 'Dev Note - bnext-round-1'
abstract: |
  To maximize protein yield and synthesis rate in the PURE system, this work employed a multivariate optimization strategy for key components including ATP, GTP, and tRNA. Analysis concluded that optimal performance is not governed by a single factor, but rather a co-dependent relationship between physicochemical viability and kinetic efficiency. The top-ranked hypothesis posits that performance is dictated by the interplay between 'free Mg2+' concentration, a function of nucleotide levels, and the stoichiometric ratio of ATP to GTP. This unified model provides a framework for navigating the complex parameter space to identify novel, high-performance operational regimes.
---

# Overview

This work details the systematic investigation into optimizing the PURE (Protein synthesis Using Recombinant Elements) cell-free system. By integrating new experimental parameters with existing data, a multivariate analysis was conducted to move beyond simple one-factor-at-a-time optimizations. The process culminated in a unified hypothesis that reconciles the system's physicochemical constraints with its kinetic bottlenecks, proposing a co-dependent optimization strategy for achieving maximal protein synthesis.

## Workspace Data

See [workspace/workspace_data.csv](./workspace/workspace_data.csv) for the full exported dataset.

# Results

The investigation converged on a primary hypothesis that integrates two critical aspects of PURE system function: physicochemical stability and kinetic throughput. This model, termed 'Unified Physicochemical and Kinetic Control,' proposes that peak performance is achieved by co-optimizing the availability of free magnesium ions with the stoichiometric ratio of the primary energy sources, ATP and GTP. The following sections detail the leading hypotheses and the experimental plan designed to validate this unified model.

## Claims

:::{claim} Unified Physicochemical and Kinetic Control: Co-optimization of Free Mg2+ Availability and Energy Stoichiometry
:label: claim-h1-unified-physicochemical-and-kinetic-cont

Maximal system performance is achieved by co-optimizing two interdependent layers: first, establishing a physicochemically viable operational space by managing 'free Mg2+' concentration (a function of total NTPs), and second, maximizing kinetic efficiency within that space by tuning the stoichiometric ATP:GTP ratio.
:::

:::{claim} Substrate-Demand Driven Energetic Tuning
:label: claim-h2-substrate-demand-driven-energetic-tuning

The optimal ATP:GTP ratio is not fixed but is dynamically determined by the 'demand' from other substrates. As concentrations of tRNA and amino acids increase, the optimal ratio shifts toward being more ATP-rich to prevent the tRNA charging pathway from becoming a bottleneck.
:::

## Evidence

:::{evidence} Prerequisite of 'Free Mg2+' Availability
:label: ev-h1-1-architect-1-rationale-won-debates-by-add
:supports: claim-h1-unified-physicochemical-and-kinetic-cont

The availability of 'free Mg2+', as a function of total NTP concentration, is a foundational and non-negotiable prerequisite for system viability.
:::

:::{evidence} Kinetic Importance of ATP:GTP Ratio
:label: ev-h1-2-explorer-1-rationale-praised-for-its-nov
:supports: claim-h1-unified-physicochemical-and-kinetic-cont

The stoichiometric ratio of ATP to GTP is a key multivariate parameter for optimizing the kinetic efficiency of the translation machinery.
:::

:::{evidence} Coupling of Mg2+ and Nucleotides (Li et al., 2014)
:label: ev-h1-3-li-et-al.-2014-finding-that-mg2-sensitiv
:supports: claim-h1-unified-physicochemical-and-kinetic-cont

Literature evidence shows that the sensitivity of the PURE system to Mg2+ concentration is strongly coupled to the concentrations of ATP and GTP.
:::

:::{evidence} Energy Depletion as a Limiting Factor (Shimizu et al., 2001)
:label: ev-h1-4-shimizu-et-al.-2001-finding-that-energy
:supports: claim-h1-unified-physicochemical-and-kinetic-cont

Prior research identifies the depletion of the energy sources (ATP/GTP) as a primary cause for the cessation of protein synthesis reactions.
:::

:::{evidence} Rationale for Unified Hypothesis
:label: ev-h1-5-unified-physicochemical-and-kinetic-cont
:supports: claim-h1-unified-physicochemical-and-kinetic-cont

The unified model is superior because it combines physicochemical prerequisites with kinetic tuning, moving beyond merely preventing system failure to actively maximizing throughput.
:::

:::{evidence} ATP:GTP Ratio and Substrate Availability
:label: ev-h2-1-explorer-1-rationale-praised-for-its-nov
:supports: claim-h2-substrate-demand-driven-energetic-tuning

The ATP:GTP ratio is a novel kinetic argument that is coupled to the availability of other key substrates in the system.
:::

:::{evidence} Constraint of Physicochemical Viability
:label: ev-h2-2-architect-1-critique-of-explorer-1-highl
:supports: claim-h2-substrate-demand-driven-energetic-tuning

Any kinetic optimization strategy, such as tuning the ATP:GTP ratio, can only be effective within a system that is fundamentally viable from a physicochemical standpoint.
:::

:::{evidence} System Sensitivity to Component Balance (Li et al., 2014)
:label: ev-h2-3-li-et-al.-2014-showed-that-yield-improve
:supports: claim-h2-substrate-demand-driven-energetic-tuning

Yield can be improved by adjusting translation factors and tRNA, implying the system is sensitive to the balance of all components, not just the primary energy source.
:::

:::{evidence} Rationale for Demand-Driven Hypothesis
:label: ev-h2-4-substrate-demand-driven-energetic-tuning
:supports: claim-h2-substrate-demand-driven-energetic-tuning

This hypothesis refines kinetic arguments by directly linking the optimal ATP:GTP ratio to substrate demand (tRNA, amino acids) while operating within established physicochemical constraints.
:::

## Detailed Findings

## Executive Summary

The research aimed to maximize the protein expression yield and synthesis rate of the PURE (Protein synthesis Using Recombinant Elements) system. The IGOR process employed a multivariate combinatorial optimization strategy, integrating new features ([ATP], [GTP], [Amino acid mix], [tRNA]) with existing experimental data. The investigation concluded that optimal PURE system performance is not governed by a single factor but by a complex, co-dependent relationship between physicochemical viability and kinetic efficiency. The top-ranked hypothesis, 'Unified Physicochemical and Kinetic Control,' posits that system performance is dictated by the interplay between the concentration of 'free Mg2+'—a function of total nucleotide levels—and the stoichiometric ratio of ATP to GTP. This unified model provides a robust framework for navigating the high-dimensional parameter space to discover a new, high-performance operational regime, moving beyond simple one-factor-at-a-time optimizations.

## Top-Ranked Hypotheses

### 1. Unified Physicochemical and Kinetic Control: Co-optimization of Free Mg2+ Availability and Energy Stoichiometry

This hypothesis integrates the foundational physicochemical constraints of the PURE system with its kinetic bottlenecks. It posits that maximal system performance (rate and yield) is not found by optimizing single factors, but by co-optimizing two interdependent layers. The first layer is **physicochemical viability**, governed by the concentration of 'free Mg2+', which is non-linearly dependent on the total concentration of chelating nucleotides (ATP and GTP). This defines the boundaries of a viable operational space, addressing the failures observed at high total [Mg2+] and [NTP]. The second layer is **kinetic efficiency**, which is optimized *within* that viable space by tuning the stoichiometric ratio of ATP to GTP. This 'energetic resonance' balances the ATP-dependent tRNA charging machinery with the GTP-dependent ribosomal translocation machinery. Therefore, peak performance lies in a multi-dimensional sweet spot where sufficient free Mg2+ ensures fundamental component function, while the ATP:GTP ratio is optimally matched to prevent kinetic bottlenecks in the translation cycle. **Testable Question:** Can we achieve a >5x improvement in PURE performance by mapping the interaction surface between total nucleotide concentration (Total NTPs from 2-8 mM), the ATP:GTP ratio (from 1:2 to 2:1), and total [Mg2+] (from 6-18 mM)? This multivariate approach aims to identify a globally optimal regime that surpasses performance achievable by optimizing any single variable alone.

**Final rationale:**

This hypothesis evolves the top-ranked 'Architect 1' by directly incorporating the key strengths of its main competitor, 'Explorer 1'. The debate revealed that while 'Architect 1' correctly identified the fundamental importance of the 'free Mg2+'-NTP relationship, 'Explorer 1' introduced a novel and valuable kinetic argument around the ATP:GTP ratio. This combined hypothesis is superior because it creates a unified model where physicochemical viability is a prerequisite for, and is modulated by, kinetic efficiency. It moves beyond simply preventing system failure (the core of 'Architect 1') to actively tuning for maximal throughput within the viable operational space, thus presenting a more comprehensive and powerful optimization strategy.

**Key supporting evidence:**
- Architect 1 Rationale: Won debates by addressing the foundational, non-negotiable prerequisite of 'free Mg2+' availability as a function of total NTP concentration.
- Explorer 1 Rationale: Praised for its novel, multivariate kinetic argument focusing on the stoichiometric ratio of ATP to GTP as a key optimization parameter.
- Li et al., 2014: Finding that Mg2+ sensitivity is strongly coupled to ATP/GTP concentrations.

### 2. Substrate-Demand Driven Energetic Tuning

This hypothesis refines the concept of 'energetic resonance' by proposing that the optimal stoichiometric ratio of ATP to GTP is not a fixed constant, but is dynamically determined by the demand from other key substrates. The PURE system's two main energy sinks—ATP for tRNA aminoacylation and GTP for ribosomal translocation—are coupled. The efficiency of the overall system depends on balancing the flux through these two pathways. This hypothesis posits that the 'demand' on the ATP-dependent charging pathway is a direct function of the total concentration of available tRNA and amino acids. Therefore, as tRNA and amino acid concentrations increase, the optimal ATP:GTP ratio required to maximize kinetic rate will shift towards being ATP-rich to prevent the charging machinery from becoming a bottleneck. This entire kinetic optimization is, however, constrained within a viable physicochemical window where total [NTP] and [Mg2+] levels do not lead to component precipitation or ribosomal stalling. **Testable Question:** While holding the total [NTP + Mg2+] concentrations within a known viable range, does systematically varying the concentration of the tRNA and amino acid pools (e.g., low vs. high levels) cause a predictable and significant shift in the optimal ATP:GTP ratio required to maximize the protein synthesis rate (sigmoid_rate)?

**Final rationale:**

This hypothesis evolves 'Explorer 1' by addressing the primary critique from its debate against 'Architect 1'—that its kinetic arguments must operate within a fundamentally viable system. It explicitly incorporates the physicochemical constraints (the 'viable window') as a boundary condition. Its primary evolution is to make the 'energetic resonance' concept more concrete and testable by directly linking the optimal ATP:GTP ratio to the 'demand' created by other substrates (tRNA and Amino Acids), a variable that was mentioned but not central to the original hypothesis. This provides a more nuanced, multi-layered interaction model that is mechanistically specific and highly ambitious.

**Key supporting evidence:**
- Explorer 1 Rationale: Praised for its novel kinetic argument about the ATP:GTP ratio and its coupling to substrate availability.
- Architect 1 Critique of Explorer 1: Highlighted that kinetic optimization can only occur within a system that is fundamentally viable from a physicochemical standpoint.
- Li et al., 2014: Showed that yield improvements are possible through adjustment of translation factors and tRNA, implying that the system is sensitive to the balance of all components, not just energy.

## Proposed Experimental Plan

### Objective
To experimentally validate the 'Unified Physicochemical and Kinetic Control' hypothesis by systematically mapping the three-dimensional interaction surface of total nucleotide concentration, ATP:GTP ratio, and Magnesium concentration to identify a globally optimal condition for both PURE system protein synthesis rate and final yield.

### Variables & Controls
| Variable Type | Parameter | Levels/Range | Notes |
| :--- | :--- | :--- | :--- |
| **Independent** | Total Nucleotide Conc. ([ATP] + [GTP]) | 2 mM, 5 mM, 8 mM | Spans a range from standard to high energy. |
| **Independent** | ATP:GTP Molar Ratio | 1:2, 1:1, 2:1 | Tests GTP-rich, equimolar, and ATP-rich conditions. |
| **Independent** | [Magnesium acetate] (mM) | 6 mM, 12 mM, 18 mM | Explores the viable range identified in prior experiments. |
| **Dependent** | Final Protein Yield (ng/μL) | Continuous | Measured as `sigmoid_steady_state`. |
| **Dependent** | Synthesis Rate (1/h) | Continuous | Measured as `sigmoid_rate`. |
| **Control** | [DNA], [PMix], [Ribosome], [K-glutamate] | Constant | Held at values from a high-performing baseline experiment. |
| **Control** | [Amino acid mix], [tRNA] | Constant | Held at the mean of their specified bounds (0.35 mM and 3.125 ug/uL, respectively). |

### Protocol Steps
1.  **Design Experiment**: Create a full factorial (3x3x3 = 27 conditions) experimental design based on the independent variables. Include triplicate reactions for each condition and baseline controls.
2.  **Prepare Stocks**: Prepare concentrated stocks of ATP, GTP, and Magnesium Acetate. Prepare a master mix containing all other constant PURE system components (Protein Mix, Ribosomes, DNA, salts, buffers, Amino Acids, tRNA).
3.  **Assemble Reactions**: In a 384-well plate, dispense the master mix into each well. Then, using a liquid handler, add varying volumes of the ATP, GTP, and Magnesium Acetate stocks according to the experimental design. Add nuclease-free water to bring all reactions to a constant final volume.
4.  **Incubate & Measure**: Place the plate in a plate reader pre-heated to 37°C. Monitor GFP fluorescence (Excitation: 488 nm, Emission: 507 nm) every 5 minutes for at least 5 hours.
5.  **Analyze Data**: Process the time-course fluorescence data for each well. Fit a sigmoid function to each curve to extract the key metrics.

### Key Metrics
*   **`sigmoid_steady_state (ng/uL)`**: The upper plateau of the fitted sigmoid curve, converted to concentration using a standard curve. This quantifies the final protein yield.
*   **`sigmoid_rate (1/h)`**: The maximum slope of the fitted sigmoid curve. This quantifies the peak rate of protein synthesis.
*   **Response Surface Plots**: Generate 3D surface plots visualizing yield and rate as a function of the three independent variables. These plots will be used to identify the coordinates of the optimal performance region and confirm the hypothesized co-dependence.

### Generated Experimental Suggestions

| ID     | Note   |   [DNA] (nM) |   [PEG4K 40%] (%) |   [RNAse Inhib] (U/mL) |   [PMix] (mg/mL) |   [Ribosome] (uM) |   Rxn Volume (uL) |   [Magnesium acetate] (mM) |   [Creatine phosphate] (mM) |   [Potassium glutamate] (mM) |   [PPK] (uM) |   [PolyP] (mM) |        IsNEB |   HasMgAR953 |   sigmoid_steady_state (ng/uL) |   sigmoid_rate (1/h) |   sigmoid_time_offset (h) |   success |   isplamGFP |
|:-------|:-------|-------------:|------------------:|-----------------------:|-----------------:|------------------:|------------------:|---------------------------:|----------------------------:|-----------------------------:|-------------:|---------------:|-------------:|-------------:|-------------------------------:|---------------------:|--------------------------:|----------:|------------:|
| GES-1  |        |      3.96852 |       0           |                   2000 |          1.80479 |           1.79883 |                10 |                    7.56226 |                21.8087      |                      98.408  | -9.09624e-09 |    1.12283e-07 |  0           |  0           |                        73.3044 |              4.12786 |                  0.859325 |  1        | 0           |
| GES-2  |        |     17.1366  |       1.90914e-08 |                   2000 |          1.8551  |           4.44817 |                10 |                    1       |               100           |                      40      | -9.09624e-09 |    1.12283e-07 | -2.16801e-08 | -4.72021e-09 |                        74.1715 |              3.54919 |                  1.20757  |  0.999996 | 2.56833e-08 |
| GES-3  |        |      6.37947 |       1.90914e-08 |                   2000 |          1.71443 |           1.92424 |                10 |                    6.66519 |                44.69        |                      76.9154 | -9.09624e-09 |    1.12283e-07 | -2.16801e-08 | -4.72021e-09 |                        61.6767 |              3.46023 |                  1.11766  |  0.974694 | 2.56833e-08 |
| GES-4  |        |     19.6292  |       1.90914e-08 |                   2000 |          1.58247 |           1.73705 |                10 |                    7.68833 |                98.2803      |                      41.5292 | -9.09624e-09 |    1.12283e-07 | -2.16801e-08 | -4.72021e-09 |                        50.5099 |              2.01897 |                  1.73891  |  0.826795 | 2.56833e-08 |
| GES-5  |        |     10.4771  |       1.90914e-08 |                   2000 |          1.93061 |           1.41632 |                10 |                    1       |                43.8393      |                      40      | -9.09624e-09 |    1.12283e-07 | -2.16801e-08 | -4.72021e-09 |                        60.4489 |              3.07589 |                  1.43345  |  0.994473 | 2.56833e-08 |
| GES-6  |        |      3.45744 |       1.90914e-08 |                   2000 |          1.81158 |           1.79063 |                10 |                    8.41242 |                13.3839      |                     102.706  | -9.09624e-09 |    1.12283e-07 | -2.16801e-08 | -4.72021e-09 |                        70.8083 |              4.22316 |                  0.825993 |  0.998416 | 2.56833e-08 |
| GES-7  |        |     11.536   |       1.90914e-08 |                   2000 |          1.992   |           4.5     |                10 |                   24.3033  |               100           |                      86.1676 | -9.09624e-09 |    1.12283e-07 | -2.16801e-08 | -4.72021e-09 |                        60.9121 |              4.68735 |                  0.563818 |  1        | 2.56833e-08 |
| GES-8  |        |     12.9324  |       1.90914e-08 |                   2000 |          1.97001 |           1.46725 |                10 |                    6.50792 |               100           |                      56.0007 | -9.09624e-09 |    1.12283e-07 | -2.16801e-08 | -4.72021e-09 |                        52.1188 |              3.25111 |                  1.32842  |  0.950477 | 2.56833e-08 |
| GES-9  |        |      4.96434 |       1.90914e-08 |                   2000 |          1.89322 |           1.88378 |                10 |                    6.37434 |                 7.91221     |                      95.836  | -9.09624e-09 |    1.12283e-07 | -2.16801e-08 | -4.72021e-09 |                        61.1843 |              4.11276 |                  0.945928 |  0.998715 | 2.56833e-08 |
| GES-10 |        |      4.933   |       1.90914e-08 |                   2000 |          1.81559 |           1.62621 |                10 |                   14.7795  |                52.8506      |                      99.8438 | -9.09624e-09 |    1.12283e-07 | -2.16801e-08 | -4.72021e-09 |                        51.9602 |              3.67524 |                  1.00333  |  0.983543 | 2.56833e-08 |
| GES-11 |        |      3.7449  |       1.90914e-08 |                   2000 |          1.80468 |           1.78473 |                10 |                    7.65395 |                21.523       |                      97.4844 | -9.09624e-09 |    1.12283e-07 | -2.16801e-08 | -4.72021e-09 |                        73.4009 |              4.13637 |                  0.852575 |  0.997327 | 2.56833e-08 |
| GES-12 |        |     20       |       1.90914e-08 |                   2000 |          1.98137 |           4.5     |                10 |                   25       |               100           |                      97.731  | -9.09624e-09 |    1.12283e-07 | -2.16801e-08 | -4.72021e-09 |                        61.6897 |              4.44225 |                  0.721471 |  0.999999 | 2.56833e-08 |
| GES-13 |        |     18.9571  |       1.90914e-08 |                   2000 |          2.07287 |           1.23295 |                10 |                   21.7164  |               100           |                      43.1032 | -9.09624e-09 |    1.12283e-07 | -2.16801e-08 | -4.72021e-09 |                        48.7029 |              3.12072 |                  1.30945  |  0.998181 | 2.56833e-08 |
| GES-14 |        |      4.67828 |       1.90914e-08 |                   2000 |          1.67647 |           1       |                10 |                   25       |                91.7408      |                     178.92   | -9.09624e-09 |    1.12283e-07 | -2.16801e-08 | -4.72021e-09 |                        29.4359 |              2.74643 |                  1.23961  |  0.984947 | 2.56833e-08 |
| GES-15 |        |      2.71684 |       1.90914e-08 |                   2000 |          1.88289 |           2.04919 |                10 |                   21.5156  |                 9.42588e-07 |                     179.524  | -9.09624e-09 |    1.12283e-07 | -2.16801e-08 | -4.72021e-09 |                        38.6099 |              3.36649 |                  1.04477  |  0.999017 | 2.56833e-08 |
| GES-16 |        |      3.71039 |       1.90914e-08 |                   2000 |          1.80885 |           1.79858 |                10 |                    7.89535 |                19.5206      |                      99.8639 | -9.09624e-09 |    1.12283e-07 | -2.16801e-08 | -4.72021e-09 |                        72.9683 |              4.16228 |                  0.846566 |  0.997599 | 2.56833e-08 |
| GES-17 |        |      4.58845 |       1.90914e-08 |                   2000 |          1.86446 |           1.87882 |                10 |                    7.67922 |                32.871       |                     113.131  | -9.09624e-09 |    1.12283e-07 | -2.16801e-08 | -4.72021e-09 |                        64.8248 |              3.97151 |                  0.932145 |  0.987549 | 2.56833e-08 |
| GES-18 |        |      8.01366 |       1.90914e-08 |                   2000 |          1.79379 |           2.04681 |                10 |                    4.33641 |                23.6723      |                      82.6587 | -9.09624e-09 |    1.12283e-07 | -2.16801e-08 | -4.72021e-09 |                        62.6171 |              3.59443 |                  1.13557  |  0.993209 | 2.56833e-08 |
| GES-19 |        |      7.1188  |       1.90914e-08 |                   2000 |          2.05198 |           4.43758 |                10 |                   22.2534  |               100           |                      67.8727 | -9.09624e-09 |    1.12283e-07 | -2.16801e-08 | -4.72021e-09 |                        60.1108 |              4.6406  |                  0.588453 |  1        | 2.56833e-08 |
| GES-20 |        |     16.9449  |       1.90914e-08 |                   2000 |          2.2096  |           1.53481 |                10 |                   23.1447  |               100           |                      77.9894 | -9.09624e-09 |    1.12283e-07 | -2.16801e-08 | -4.72021e-09 |                        45.5461 |              3.19317 |                  1.31506  |  0.997649 | 2.56833e-08 |
| GES-21 |        |      7.92875 |       1.90914e-08 |                   2000 |          1.74789 |           1.19469 |                10 |                   24.7713  |                99.8407      |                      40      | -9.09624e-09 |    1.12283e-07 | -2.16801e-08 | -4.72021e-09 |                        41.8877 |              3.22017 |                  1.05322  |  0.999135 | 2.56833e-08 |
| GES-22 |        |      5.42271 |       1.90914e-08 |                   2000 |          1.83144 |           1.95473 |                10 |                    6.80422 |                 9.42588e-07 |                     124.834  | -9.09624e-09 |    1.12283e-07 | -2.16801e-08 | -4.72021e-09 |                        54.8418 |              4.12369 |                  0.884734 |  0.997893 | 2.56833e-08 |
| GES-23 |        |      2.35317 |       1.90914e-08 |                   2000 |          1.79821 |           2.04176 |                10 |                    1.93909 |                41.7229      |                      78.161  | -9.09624e-09 |    1.12283e-07 | -2.16801e-08 | -4.72021e-09 |                        64.8984 |              3.40732 |                  1.13085  |  0.992876 | 2.56833e-08 |
| GES-24 |        |      5.23939 |       1.90914e-08 |                   2000 |          1.74375 |           1.84736 |                10 |                    2.36373 |                 3.23654     |                      75.4841 | -9.09624e-09 |    1.12283e-07 | -2.16801e-08 | -4.72021e-09 |                        62.6115 |              3.6328  |                  1.04744  |  0.999241 | 2.56833e-08 |
| GES-25 |        |      2.30832 |       1.90914e-08 |                   2000 |          1.87809 |           1.45236 |                10 |                    4.34829 |                 0.635882    |                     111.897  | -9.09624e-09 |    1.12283e-07 | -2.16801e-08 | -4.72021e-09 |                        55.2478 |              3.98456 |                  0.876047 |  0.999604 | 2.56833e-08 |
| GES-26 |        |      3.71039 |       1.90914e-08 |                   2000 |          1.80885 |           1.79858 |                10 |                    7.89535 |                19.5206      |                      99.8639 | -9.09624e-09 |    1.12283e-07 | -2.16801e-08 | -4.72021e-09 |                        72.9683 |              4.16228 |                  0.846566 |  0.997599 | 2.56833e-08 |
| GES-27 |        |     19.3237  |       1.90914e-08 |                   2000 |          1.56518 |           4.5     |                10 |                    9.87089 |               100           |                      40      | -9.09624e-09 |    1.12283e-07 | -2.16801e-08 | -4.72021e-09 |                        66.6929 |              3.58189 |                  1.0675   |  0.999997 | 2.56833e-08 |
| GES-28 |        |      1.11845 |       1.90914e-08 |                   2000 |          1.77163 |           1.02189 |                10 |                    6.25564 |                30.1212      |                      65.8751 | -9.09624e-09 |    1.12283e-07 | -2.16801e-08 | -4.72021e-09 |                        55.3324 |              3.31869 |                  1.05007  |  0.999171 | 2.56833e-08 |
| GES-29 |        |     20       |       1.90914e-08 |                   2000 |          1.94539 |           3.67581 |                10 |                    3.66636 |                 9.42588e-07 |                      56.2631 | -9.09624e-09 |    1.12283e-07 | -2.16801e-08 | -4.72021e-09 |                        38.9664 |              3.66155 |                  1.25984  |  0.999987 | 2.56833e-08 |
| GES-30 |        |      3.11468 |       1.90914e-08 |                   2000 |          1.34894 |           1       |                10 |                   21.048   |                33.9038      |                      97.339  | -9.09624e-09 |    1.12283e-07 | -2.16801e-08 | -4.72021e-09 |                        24.9474 |              2.54753 |                  1.25979  |  0.997603 | 2.56833e-08 |
| GES-31 |        |      8.17706 |       1.90914e-08 |                   2000 |          1.79434 |           1.99872 |                10 |                    4.64946 |                30.9079      |                      40      | -9.09624e-09 |    1.12283e-07 | -2.16801e-08 | -4.72021e-09 |                        61.9011 |              3.42507 |                  1.20034  |  0.997244 | 2.56833e-08 |
| GES-32 |        |      3.18267 |       1.90914e-08 |                   2000 |          1.83168 |           1       |                10 |                    9.12956 |                 9.42588e-07 |                     159.235  | -9.09624e-09 |    1.12283e-07 | -2.16801e-08 | -4.72021e-09 |                        40.4724 |              3.61029 |                  0.948781 |  0.999112 | 2.56833e-08 |
| GES-33 |        |      5.04296 |       1.90914e-08 |                   2000 |          1.84944 |           1.96363 |                10 |                   11.7487  |                 4.0859      |                     112.192  | -9.09624e-09 |    1.12283e-07 | -2.16801e-08 | -4.72021e-09 |                        57.8273 |              4.0943  |                  0.935844 |  0.998088 | 2.56833e-08 |
| GES-34 |        |      4.54755 |       1.90914e-08 |                   2000 |          1.75537 |           1.85316 |                10 |                    7.52347 |                 9.42588e-07 |                     108.515  | -9.09624e-09 |    1.12283e-07 | -2.16801e-08 | -4.72021e-09 |                        61.1284 |              4.14551 |                  0.845176 |  0.998686 | 2.56833e-08 |
| GES-35 |        |      1       |       1.90914e-08 |                   2000 |          2.11848 |           4.5     |                10 |                   11.8858  |               100           |                      40      | -9.09624e-09 |    1.12283e-07 | -2.16801e-08 | -4.72021e-09 |                        62.6727 |              4.25288 |                  0.779052 |  1        | 2.56833e-08 |

## References
- [Cell-free translation reconstituted with purified components](https://doi.org/10.1038/90802), Shimizu Y, 2001, Nature Biotechnology
- [Improved Cell-Free RNA and Protein Synthesis System](https://doi.org/10.1371/journal.pone.0106232), Li J, 2014, PLoS ONE
- [A Simple](https://doi.org/10.1007/bf02701951), Robust, and Low-Cost Method To Produce the PURE Cell-Free System, Lavickova B, 2019, ACS Synthetic Biology

## Dead Ends
- **Hypothesis 'Magnesium-ATP/GTP Interaction Governs PURE System Yield'**: This hypothesis was consistently rejected in debates. Its core rationale was deemed too remedial and narrow, focusing only on preventing a specific failure mode (precipitation at high Mg2+ levels) rather than exploring the broader, multi-dimensional landscape to discover new high-performance regimes. It was judged to be less ambitious and less aligned with the multivariate optimization goal compared to hypotheses that proposed more comprehensive kinetic and physicochemical models.

## Figures

:::{figure} ./figures/viz-01-test-split-sigmoid_rate-1-h.png
:label: fig:viz-01-test-split-sigmoid_rate-1-h.png
:name: fig-viz-01-test-split-sigmoid_rate-1-h.png
:grounds: ev-h1-1-architect-1-rationale-won-debates-by-add
:align: center
:width: 75%
Parity plot showing the predictive performance of the model for protein synthesis rate (sigmoid_rate) on a held-out test dataset. The clustering of points along the diagonal indicates the model's ability to generalize to unseen experimental conditions.
:::

:::{figure} ./figures/viz-02-test-split-sigmoid_steady_state-ng-ul.png
:label: fig:viz-02-test-split-sigmoid_steady_state-ng-ul.png
:name: fig-viz-02-test-split-sigmoid_steady_state-ng-ul.png
:grounds: ev-h1-2-explorer-1-rationale-praised-for-its-nov
:align: center
:width: 75%
Parity plot showing the predictive performance of the model for final protein yield (sigmoid_steady_state) on a held-out test dataset. The correlation between predicted and actual values demonstrates the model's effectiveness in capturing the factors that determine total yield.
:::

:::{figure} ./figures/viz-03-sigmoid_rate-1-h-vs-sigmoid_steady_state-ng-ul.png
:label: fig:viz-03-sigmoid_rate-1-h-vs-sigmoid_steady_state-ng-ul.png
:name: fig-viz-03-sigmoid_rate-1-h-vs-sigmoid_steady_state-ng-ul.png
:grounds: ev-h1-3-li-et-al.-2014-finding-that-mg2-sensitiv
:align: center
:width: 75%
Scatter plot of protein synthesis rate versus final protein yield. This visualization explores the relationship between the two primary optimization targets, indicating whether conditions that improve rate also tend to improve final yield.
:::

# Conclusions and next steps

The analysis revealed that maximizing PURE system performance requires a shift from optimizing individual components to co-optimizing interdependent factors. The top-ranked 'Unified Physicochemical and Kinetic Control' hypothesis provides a robust model where fundamental physicochemical viability, governed by free Mg2+, sets the stage for achieving maximum kinetic efficiency through the precise tuning of the ATP:GTP ratio. The proposed full-factorial experiment is designed to map this multi-dimensional interaction surface, validating the hypothesis and systematically identifying a globally optimal regime for protein synthesis that would be undiscoverable through traditional, linear optimization methods.

This synthesis centers on {claim}`claim-h1-unified-physicochemical-and-kinetic-cont`, {claim}`claim-h2-substrate-demand-driven-energetic-tuning`.

Grounding evidence includes {evidence}`ev-h1-1-architect-1-rationale-won-debates-by-add`, {evidence}`ev-h1-2-explorer-1-rationale-praised-for-its-nov`.
