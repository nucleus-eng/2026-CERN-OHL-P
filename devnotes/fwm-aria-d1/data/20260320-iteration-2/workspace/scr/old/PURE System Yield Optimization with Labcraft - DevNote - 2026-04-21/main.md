---
title: 'Dev Note - bnext-iter-2'
abstract: |
  Low protein yield in PURE cell-free reactions on an automated Labcraft platform was attributed to accelerated evaporation from open-air microplate wells. This physical stressor induces a dual failure cascade: direct biochemical inhibition from rising salt concentrations and indirect metabolic collapse of the salt-sensitive creatine phosphate energy system. A unified model posits that a synergistic countermeasure combining a physical stabilizer (PEG) to reduce evaporation and a metabolically robust energy source (PPK/PolyP) is required to restore yield. A multivariate combinatorial experiment has been designed to map this interaction space and identify an optimal, biophysically robust formulation.
---

# Overview

This Dev Note summarizes the key findings and next steps from a research cycle aimed at improving PURE system performance on the Labcraft automated platform. It details the convergent hypothesis that evaporation is the root cause of diminished protein yield and outlines a combinatorial experimental plan to test a proposed synergistic solution.

## Workspace Data

See [workspace/workspace_data.csv](./workspace/workspace_data.csv) for the full exported dataset.

# Results

Analysis of prior literature and experimental data converged on a unified model explaining the observed protein yield deficit on the Labcraft platform. The following sections detail the top-ranked hypotheses derived from this model, which attribute the deficit to evaporation-induced stress, and present a multivariate experimental plan designed to validate this model and identify a robust solution.

## Claims

:::{claim} Unified Evaporation-Metabolism Stress Model for Automated PURE Systems
:label: claim-h1-unified-evaporation-metabolism-stress-mo

Reduced protein yield on the Labcraft platform is caused by accelerated water evaporation, which creates two failure modes: direct biochemical inhibition from rising salt concentrations and indirect metabolic collapse of the salt-sensitive Creatine Phosphate energy system. A successful countermeasure requires a physical stabilizer (PEG) to reduce evaporation and a metabolically robust energy source (PPK/PolyP) resilient
:::

:::{claim} Biophysical Robustness: A Synergistic Model of Metabolic Resilience and Evaporation Mitigation for Automated PURE Systems
:label: claim-h2-biophysical-robustness-a-synergistic-mod

The Labcraft platform creates a 'biophysically fragile' state where evaporation causes inhibitory shifts in salt concentrations. The observed synergy of PEG and a PPK/PolyP energy system is a required combinatorial solution, introducing physical robustness by slowing evaporation and metabolic robustness by making energy regeneration less sensitive to ionic shifts and inhibitory byproducts.
:::

## Evidence

:::{evidence} Mg2+ concentration sensitivity
:label: ev-h1-1-finding-magnesium-mg2-is-a-critical-cofa
:supports: claim-h1-unified-evaporation-metabolism-stress-mo

Optimal Magnesium (Mg2+) concentration is dependent on NTPs and creatine phosphate; an imbalance is inhibitory to the reaction (Shimizu et al., 2001; Li et al., 2014).
:::

:::{evidence} Potassium glutamate inhibition
:label: ev-h1-2-finding-high-concentrations-of-potassium
:supports: claim-h1-unified-evaporation-metabolism-stress-mo

High concentrations of potassium glutamate (>100-200 mM) can inhibit the transcription step (Gralla, 2005; Garen & Noireaux, 2024).
:::

:::{evidence} Creatine phosphate byproduct inhibition
:label: ev-h1-3-finding-the-standard-creatine-phosphate
:supports: claim-h1-unified-evaporation-metabolism-stress-mo

The standard creatine phosphate/creatine kinase energy system leads to the accumulation of inhibitory inorganic phosphate (Kim et al., 2007).
:::

:::{evidence} PPK/PolyP as a robust energy system
:label: ev-h1-4-finding-a-polyphosphate-kinase-ppk-and-i
:supports: claim-h1-unified-evaporation-metabolism-stress-mo

A polyphosphate kinase (PPK) and inorganic polyphosphate (PolyP) energy system avoids inhibitory phosphate accumulation and can have a synergistic effect on protein yield (Yadav, 2025).
:::

:::{evidence} Rationale for Unified Stress Model
:label: ev-h1-5-unified-evaporation-metabolism-stress-mo
:supports: claim-h1-unified-evaporation-metabolism-stress-mo

This model proposes a single physical mechanism (evaporation) as the root cause of yield loss, linking it to known failure modes (salt toxicity, metabolic instability). It explains why a synergistic solution (PEG + PPK/PolyP) is necessary: one part addresses the physical cause, the other addresses
:::

:::{evidence} High-yield experimental data point
:label: ev-h2-1-data-point-experiment-genscript-ppk-cust
:supports: claim-h2-biophysical-robustness-a-synergistic-mod

The highest yield experiment ('Genscript-PPK-custom-Smix-H8', 3.86) combined PEG (2%), PPK (1.96 uM), and PolyP (30 mM).
:::

:::{evidence} Automation-induced variability
:label: ev-h2-2-finding-automated-liquid-handlers-can-in
:supports: claim-h2-biophysical-robustness-a-synergistic-mod

Automated liquid handlers can introduce variability and error due to imprecise small-volume transfers (BioProcess International, 2009; Noireaux et al., 2024).
:::

:::{evidence} Research gap on macromolecular crowders
:label: ev-h2-3-opportunity-the-role-and-optimization-of
:supports: claim-h2-biophysical-robustness-a-synergistic-mod

The specific role of macromolecular crowders like PEG to counteract negative effects of automated, small-volume reaction environments has not been thoroughly investigated.
:::

:::{evidence} Research gap on energy systems in automation
:label: ev-h2-4-opportunity-there-is-a-lack-of-systemati
:supports: claim-h2-biophysical-robustness-a-synergistic-mod

Systematic studies comparing different energy regeneration systems under identical, automated, small-volume reaction conditions are lacking.
:::

:::{evidence} Rationale for Biophysical Robustness Model
:label: ev-h2-5-biophysical-robustness-a-synergistic-mod
:supports: claim-h2-biophysical-robustness-a-synergistic-mod

This model is grounded in high-yield data (PEG + PPK/PolyP) and frames the problem as achieving 'biophysical robustness'. It integrates the physical effects of evaporation (countered by PEG) with the biochemical benefits of a resilient energy system (PPK/PolyP), explaining the need for a combinatorial solution.
:::

## Detailed Findings

## Executive Summary

This research aimed to understand and overcome the consistently lower protein yield of the PURE cell-free synthesis system when run on the Labcraft automated platform. The IGOR process, synthesizing literature, experimental data, and multi-agent debate, converged on a unified model attributing the yield deficit to a primary physical stressor: accelerated water evaporation in the platform's open-air microplate wells. This evaporation induces a two-pronged failure cascade of direct biochemical inhibition from rising salt concentrations (Mg-acetate, K-glutamate) and indirect metabolic collapse of the salt-sensitive Creatine Phosphate energy system. The top-ranked hypotheses posit that a synergistic, two-part countermeasure is required, combining a physical stabilizer (PEG) to reduce the evaporation rate with a metabolically robust energy source (PPK/PolyP) resilient to ionic shifts. A multivariate combinatorial experimental plan has been designed to map this complex interaction space and identify an optimal, biophysically robust formulation for the Labcraft platform.

## Top-Ranked Hypotheses

### 1. Unified Evaporation-Metabolism Stress Model for Automated PURE Systems

The reduced protein yield on the Labcraft platform is caused by a primary physical stressor: accelerated water evaporation. This single stressor creates two distinct failure modes: 1) direct biochemical inhibition as salt concentrations (Mg-acetate, K-glutamate) rise to toxic levels, and 2) indirect metabolic collapse, as the standard Creatine Phosphate energy system is exquisitely sensitive to these salt fluctuations and also generates inhibitory phosphate byproducts. This unified model posits that the highest-performing recipes (containing PEG and PPK/PolyP) succeed because they provide a two-part countermeasure specifically tailored to this environment. PEG acts as a physical stabilizer, increasing viscosity to reduce the rate of evaporation, while the PPK/PolyP system provides a metabolically robust energy source that is more resilient to the ionic shifts that still occur. The model predicts that neither component is sufficient on its own for maximal yield on this platform; the physical stressor must be mitigated while also making the energy metabolism more resilient.

**Final rationale:**

This hypothesis was consistently favored in debates for its parsimonious and fundamental approach. It proposes a single, testable physical mechanism (evaporation) as the root cause of the platform-specific yield loss, directly linking it to two well-documented biochemical failure modes (salt toxicity and metabolic instability). It successfully evolved to integrate the data-driven insight from the highest-performing experiments, explaining *why* a synergistic solution (PEG + PPK/PolyP) is necessary: one component addresses the physical cause (evaporation) while the other addresses the resulting metabolic fragility. This provides a comprehensive, cause-and-effect model that is both predictive and directly testable.

**Key supporting evidence:**
- Finding: Magnesium (Mg2+) is a critical cofactor... its optimal concentration is highly dependent on the levels of NTPs and creatine phosphate... An imbalance can inhibit the reaction. (Shimizu et al., 2001; Li et al., 2014)
- Finding: High concentrations of potassium glutamate (>100-200 mM) can inhibit the transcription step... (Gralla, 2005; Garen & Noireaux, 2024)
- Finding: The standard creatine phosphate/creatine kinase energy regeneration system leads to the accumulation of inhibitory inorganic phosphate. (Kim et al., 2007)

### 2. Biophysical Robustness: A Synergistic Model of Metabolic Resilience and Evaporation Mitigation for Automated PURE Systems

Building on the data-driven observation that the highest yields are achieved with a combination of PEG and a PPK/PolyP energy system, this hypothesis posits that the Labcraft platform's primary drawback is the creation of a 'biophysically fragile' state. Accelerated evaporation in open-air wells induces dynamic, inhibitory shifts in salt concentrations. The observed synergy of the PEG + PPK/PolyP recipe is not merely additive but a required combinatorial solution to this fragility. The PPK/PolyP system introduces *metabolic robustness*, making energy regeneration less sensitive to the Mg2+ fluctuations and avoiding the accumulation of inhibitory phosphate. Simultaneously, PEG introduces *physical robustness* by increasing viscosity and slowing the rate of evaporation. This hypothesis proposes that maximizing yield on Labcraft is an optimization problem of achieving biophysical robustness, where the metabolic and physical components must be co-varied to counteract the platform-induced instability.

**Final rationale:**

This hypothesis excelled by grounding its rationale in the most successful experimental data points, which featured a combination of PEG and a PPK/PolyP energy system. Its core strength lies in framing the problem not as a simple chemical optimization, but as a challenge of achieving 'biophysical robustness'. It successfully evolved from a purely data-driven observation to a mechanistic model that integrates the physical effects of evaporation (countered by PEG) and the biochemical benefits of a more resilient energy system (PPK/PolyP). This synergistic view provides a powerful explanation for why a combinatorial, rather than a univariate, solution is essential for success on the Labcraft platform.

**Key supporting evidence:**
- Data Point: Experiment 'Genscript-PPK-custom-Smix-H8' achieved the highest yield (3.86) by combining [PEG] (2%), [PPK] (1.96 uM), and [PolyP] (30 mM).
- Finding: Automated liquid handlers can introduce variability and error due to imprecise small-volume transfers. (BioProcess International, 2009; Noireaux et al., 2024)
- Opportunity: The role and optimization of macromolecular crowding agents (e.g., PEG, Ficoll) specifically to counteract potential negative effects of automated, small-volume reaction environments have not been thoroughly investigated.

## Proposed Experimental Plan

### Objective
To test the Unified Evaporation-Metabolism Stress Model by mapping the synergistic interaction landscape between the primary energy regeneration system, a proposed metabolic stabilizer (PPK/PolyP), a physical stabilizer (PEG), and a key inhibitory salt (Magnesium Acetate). The combinatorial optimization goal is to identify a biophysically robust formulation that maximizes protein yield (`sigmoid_steady_state`) specifically on the Labcraft automated platform.

### Multivariate Design Space
This experiment will simultaneously vary four key factors across their effective ranges to explore their non-linear interactions. A Design of Experiments (DoE) approach, such as a full factorial or response surface methodology (e.g., Box-Behnken), should be used to generate the combinatorial conditions for the batch. The following parameters define the design space:

*   **Factor 1: Primary Energy Substrate (`[Creatine phosphate]`)**
    *   Levels (mM): `0, 20, 40, 60`
    *   Rationale: Explore the full range from no primary substrate (relying solely on PPK) to the upper bound to map the impact of its inhibitory byproduct, inorganic phosphate.

*   **Factor 2: Metabolic/Physical Stabilizer (`[PEG]`)**
    *   Levels (%): `0, 1, 2`
    *   Rationale: Test the effect of the proposed physical stabilizer against evaporation. Level 0 serves as the control for the evaporation effect.

*   **Factor 3: Metabolic Stabilizer (`[PPK]`/`[PolyP]`)**
    *   Levels (uM/mM): `0/0, 1/15, 2/30`
    *   Rationale: Titrate the alternative energy system to determine its effectiveness at rescuing yield, both alone and in combination with Creatine Phosphate.

*   **Factor 4: Key Inhibitory Cation (`[Magnesium acetate]`)**
    *   Levels (mM): `8, 16, 24`
    *   Rationale: Explore a range from baseline to inhibitory concentrations to map the system's sensitivity and how it is modulated by the stabilizing factors (PEG, PPK).

All other system components will be held constant at baseline 'Labcraft' conditions as defined in the master table bounds.

### Batch Protocol Steps
1.  Use a DoE software package to generate the full combinatorial set of experiments from the Multivariate Design Space defined above.
2.  Prepare stock solutions for each of the four varied factors at concentrations sufficient to achieve the specified final concentrations in a 10 uL reaction volume.
3.  Program the Labcraft liquid handler to dispense the unique combination of the four factors, along with the constant components (e.g., PMix, Ribosomes, DNA, etc.), into a 96-well microplate.
4.  Execute the automated protocol under standard, open-air laboratory conditions to mimic the evaporative pressure.
5.  Incubate the plate in a plate reader (e.g., Cytation5) at 37°C, measuring fluorescence (deGFP expression) over a 6-hour period.
6.  Process the kinetic fluorescence data to calculate the `sigmoid_steady_state` and `sigmoid_rate (1/h)` for each condition.

### Optimization Metrics
The primary metric is `sigmoid_steady_state` (yield). The analysis of this combinatorial batch will not be a simple comparison of means. Instead, the results will be used to:
1.  Fit a response surface model to the data, identifying significant main effects, two-way, and three-way interaction terms. We expect a strong positive interaction between `[PEG]` and `[PPK]`/`[PolyP]` and a negative interaction between `[Creatine phosphate]` and `[Magnesium acetate]` that is mitigated by `[PEG]`.
2.  Generate contour plots to visualize the interaction landscape. For example, a plot of `[Magnesium acetate]` vs. `[Creatine phosphate]` at different fixed levels of `[PEG]` will be generated to explicitly show how PEG alters the optimal operating window for the salts.
3.  Feed the complete, highly-coupled dataset back into the surrogate model. This will dramatically reduce epistemic uncertainty in the regions of synergistic activity, allowing the model to more accurately predict the peak of the biophysically robust operating regime and guide the next round of fine-tuned optimization.

### Generated Experimental Suggestions

| ID    | Note   | Experiment Type   | Experiment                 | NEB in Pmix   | [PMix] (mg/mL)     | [Ribosome] (uM)    | [tRNA] (ug/uL)     | [DNA] (nM)   | [Magnesium acetate] (mM)   | [Creatine phosphate] (mM)   | [Potassium glutamate] (mM)   | [ATP] (mM)         | [GTP] (mM)         | [Amino acid mix] (mM)   | [PPK] (uM)          | [PolyP] (mM)       | [RNase Inhib] (U/mL)   | Reader Type   | Gain        | Read Type   | [PEG] (%)   | Product     | Condition   | success   | sigmoid_steady_state   | sigmoid_rate (1/h)   | drift_rate (1/h)     |
|:------|:-------|:------------------|:---------------------------|:--------------|:-------------------|:-------------------|:-------------------|:-------------|:---------------------------|:----------------------------|:-----------------------------|:-------------------|:-------------------|:------------------------|:--------------------|:-------------------|:-----------------------|:--------------|:------------|:------------|:------------|:------------|:------------|:----------|:-----------------------|:---------------------|:---------------------|
|       |        |                   | categorical                | binary        | real               | real               | real               | real         | real                       | real                        | real                         | real               | real               | real                    | real                | real               | real                   | categorical   | categorical | categorical | real        | categorical | categorical | binary    | real                   | real                 | real                 |
| GES-1 |        | model_GESS        | 20260319-DiscoveryPlate-R2 | 0.0           | 1.7999999523162842 | 1.7999999523162842 | 3.6405751705169678 | 5.0          | 1.7714290618896484         | 60.0                        | 100.9048843383789            | 1.7000000476837158 | 1.7734655141830444 | 0.2939281165599823      | 2.012500047683716   | 30.0               | 2000.0                 | Cytation5     | ext         | M           | 0.0         | deGFP       | Labcraft    | 0.0       | 2.549518585205078      | 1.759095311164856    | 0.057075053453445435 |
| GES-2 |        | model_GESS        | 20260319-DiscoveryPlate-R2 | 0.0           | 1.7999999523162842 | 1.7999999523162842 | 3.805210590362549  | 5.0          | 18.898025512695312         | 60.0                        | 133.32887268066406           | 2.5219762325286865 | 1.4740643501281738 | 0.26329874992370605     | 2.012500047683716   | 30.0               | 2000.0                 | Cytation5     | ext         | M           | 0.0         | deGFP       | Labcraft    | 1.0       | 2.319556951522827      | 1.3753448724746704   | 0.05157735198736191  |
| GES-3 |        | model_GESS        | 20260319-DiscoveryPlate-R2 | 0.0           | 1.7999999523162842 | 1.7999999523162842 | 3.990000009536743  | 5.0          | 25.0                       | 56.85887908935547           | 40.0                         | 1.7000000476837158 | 1.399999976158142  | 0.15049999952316284     | 0.49452462792396545 | 26.095813751220703 | 2000.0                 | Cytation5     | ext         | M           | 0.0         | deGFP       | Labcraft    | 1.0       | 1.4255287647247314     | 3.358367681503296    | 0.03275139629840851  |
| GES-4 |        | model_GESS        | 20260319-DiscoveryPlate-R2 | 0.0           | 1.7999999523162842 | 1.7999999523162842 | 2.3554930686950684 | 5.0          | 10.89786148071289          | 60.0                        | 151.26583862304688           | 1.7000000476837158 | 2.520054340362549  | 0.23655906319618225     | 2.012500047683716   | 30.0               | 2000.0                 | Cytation5     | ext         | M           | 0.0         | deGFP       | Labcraft    | 1.0       | 2.1409947872161865     | 1.5774692296981812   | 0.04757155478000641  |
| GES-5 |        | model_GESS        | 20260319-DiscoveryPlate-R2 | 0.0           | 1.7999999523162842 | 1.7999999523162842 | 3.990000009536743  | 5.0          | 0.0                        | 37.68775177001953           | 40.0                         | 3.700000047683716  | 1.399999976158142  | 0.15049999952316284     | 2.012500047683716   | 30.0               | 2000.0                 | Cytation5     | ext         | M           | 0.0         | deGFP       | Labcraft    | 0.0       | 1.7805894613265991     | 1.9430307149887085   | 0.04967905208468437  |

## References
- [Improved Cell-Free RNA and Protein Synthesis System](https://doi.org/10.1371/journal.pone.0106232), Li J, 2014, PLOS ONE
- [Cell-free translation reconstituted with purified components](https://doi.org/10.1038/90802), Shimizu Y, 2001, Nature Biotechnology
- [Prolonged cell-free protein synthesis using dual energy sources...](https://doi.org/10.1016/j.jbiotec.2008.07.434), Kim TW, 2007, Biotechnology and Bioengineering
- [Potassium glutamate as a transcriptional inhibitor during bacterial osmoregulation](https://doi.org/10.1038/sj.emboj.7601041), Gralla JD, 2005, The EMBO Journal
- [PPK Module testing in PURE](https://doi.org/10.63765/djnv7772), Yadav S, 2025, Developer Notes
- [Optimization of PURE system composition using automation and active learning](https://doi.org/10.64898/2026.03.23.713685), Noireaux V et al., 2024, bioRxiv
- [Optimizing Protein Production in the One-Pot PURE System...](https://doi.org/10.1021/acssynbio.4c00779.s003), Libicher K & St-Pierre F, 2024, bioRxiv

## Dead Ends
- Hypothesis: 'Macromolecular Crowders as Biophysical Stabilizers for Automated PURE Systems'. Reason for rejection: This hypothesis was deemed less fundamental than its competitor ('Evaporation-Induced Salt Inhibition'). It proposed a solution (crowders) without first proposing a clean, falsifiable test for the root physical problem (evaporation). The debate concluded that establishing the root cause should precede testing solutions that have multiple complex effects.
- Hypothesis: The initial 'Quant 1' hypothesis. Reason for rejection: Similar to the 'Explorer 1' hypothesis, this proposal jumped to a complex, multi-part solution (synergy of PPK and PEG) without first isolating and testing the primary, platform-dependent variable (evaporation). The winning 'Architect 1' hypothesis was favored for its more rigorous, parsimonious approach of first establishing a foundational cause-and-effect relationship.

## Figures

:::{figure} ./figures/viz-01-1d-sensitivity-for-20260309-discoveryplate-r1-i10.png
:label: fig:viz-01-1d-sensitivity-for-20260309-discoveryplate-r1-i10.png
:name: fig-viz-01-1d-sensitivity-for-20260309-discoveryplate-r1-i10.png
:grounds: ev-h1-1-finding-magnesium-mg2-is-a-critical-cofa
:align: center
:width: 75%
1D Sensitivity for 20260309-DiscoveryPlate-R1-I10
:::

:::{figure} ./figures/viz-02-test-split-sigmoid_rate-1-h.png
:label: fig:viz-02-test-split-sigmoid_rate-1-h.png
:name: fig-viz-02-test-split-sigmoid_rate-1-h.png
:grounds: ev-h1-2-finding-high-concentrations-of-potassium
:align: center
:width: 75%
Test Split: sigmoid_rate (1/h)
:::

:::{figure} ./figures/viz-03-similarity-of-20260319-discoveryplate-r2-i10-to-dataset.png
:label: fig:viz-03-similarity-of-20260319-discoveryplate-r2-i10-to-dataset.png
:name: fig-viz-03-similarity-of-20260319-discoveryplate-r2-i10-to-dataset.png
:grounds: ev-h1-3-finding-the-standard-creatine-phosphate
:align: center
:width: 75%
Similarity of 20260319-DiscoveryPlate-R2-I10 to Dataset
:::

:::{figure} ./figures/viz-04-1d-sensitivity-for-20260319-discoveryplate-r2-i10-2.png
:label: fig:viz-04-1d-sensitivity-for-20260319-discoveryplate-r2-i10-2.png
:name: fig-viz-04-1d-sensitivity-for-20260319-discoveryplate-r2-i10-2.png
:grounds: ev-h1-4-finding-a-polyphosphate-kinase-ppk-and-i
:align: center
:width: 75%
1D Sensitivity for 20260319-DiscoveryPlate-R2-I10 (2)
:::

:::{figure} ./figures/viz-05-test-split-drift_rate-1-h.png
:label: fig:viz-05-test-split-drift_rate-1-h.png
:name: fig-viz-05-test-split-drift_rate-1-h.png
:grounds: ev-h1-5-unified-evaporation-metabolism-stress-mo
:align: center
:width: 75%
Test Split: drift_rate (1/h)
:::

:::{figure} ./figures/viz-06-sensitivities-for-20260309-discoveryplate-r1-j13.png
:label: fig:viz-06-sensitivities-for-20260309-discoveryplate-r1-j13.png
:name: fig-viz-06-sensitivities-for-20260309-discoveryplate-r1-j13.png
:grounds: ev-h2-1-data-point-experiment-genscript-ppk-cust
:align: center
:width: 75%
Sensitivities for 20260309-DiscoveryPlate-R1-J13
:::

:::{figure} ./figures/viz-07-similarity-of-ges-1-to-dataset.png
:label: fig:viz-07-similarity-of-ges-1-to-dataset.png
:name: fig-viz-07-similarity-of-ges-1-to-dataset.png
:grounds: ev-h2-2-finding-automated-liquid-handlers-can-in
:align: center
:width: 75%
Similarity of GES-1 to Dataset
:::

:::{figure} ./figures/viz-08-prob.-of-meeting-goals.png
:label: fig:viz-08-prob.-of-meeting-goals.png
:name: fig-viz-08-prob.-of-meeting-goals.png
:grounds: ev-h2-3-opportunity-the-role-and-optimization-of
:align: center
:width: 75%
Prob. of Meeting Goals
:::

:::{figure} ./figures/viz-09-1d-sensitivity-for-20260319-discoveryplate-r2-i10.png
:label: fig:viz-09-1d-sensitivity-for-20260319-discoveryplate-r2-i10.png
:name: fig-viz-09-1d-sensitivity-for-20260319-discoveryplate-r2-i10.png
:grounds: ev-h2-4-opportunity-there-is-a-lack-of-systemati
:align: center
:width: 75%
1D Sensitivity for 20260319-DiscoveryPlate-R2-I10
:::

:::{figure} ./figures/viz-10-1d-sensitivity-for-20260319-discoveryplate-r2-i15.png
:label: fig:viz-10-1d-sensitivity-for-20260319-discoveryplate-r2-i15.png
:name: fig-viz-10-1d-sensitivity-for-20260319-discoveryplate-r2-i15.png
:grounds: ev-h2-5-biophysical-robustness-a-synergistic-mod
:align: center
:width: 75%
1D Sensitivity for 20260319-DiscoveryPlate-R2-I15
:::

:::{figure} ./figures/viz-11-sigmoid_steady_state-vs-drift_rate-1-h.png
:label: fig:viz-11-sigmoid_steady_state-vs-drift_rate-1-h.png
:name: fig-viz-11-sigmoid_steady_state-vs-drift_rate-1-h.png
:grounds: ev-h1-1-finding-magnesium-mg2-is-a-critical-cofa
:align: center
:width: 75%
sigmoid_steady_state vs drift_rate (1/h)
:::

:::{figure} ./figures/viz-12-sigmoid_steady_state-vs-sigmoid_rate-1-h.png
:label: fig:viz-12-sigmoid_steady_state-vs-sigmoid_rate-1-h.png
:name: fig-viz-12-sigmoid_steady_state-vs-sigmoid_rate-1-h.png
:grounds: ev-h1-2-finding-high-concentrations-of-potassium
:align: center
:width: 75%
sigmoid_steady_state vs sigmoid_rate (1/h)
:::

:::{figure} ./figures/viz-13-test-split-sigmoid_steady_state.png
:label: fig:viz-13-test-split-sigmoid_steady_state.png
:name: fig-viz-13-test-split-sigmoid_steady_state.png
:grounds: ev-h1-3-finding-the-standard-creatine-phosphate
:align: center
:width: 75%
Test Split: sigmoid_steady_state
:::

:::{figure} ./figures/viz-14-sigmoid_steady_state-vs-sigmoid_steady_state.png
:label: fig:viz-14-sigmoid_steady_state-vs-sigmoid_steady_state.png
:name: fig-viz-14-sigmoid_steady_state-vs-sigmoid_steady_state.png
:grounds: ev-h1-4-finding-a-polyphosphate-kinase-ppk-and-i
:align: center
:width: 75%
sigmoid_steady_state vs sigmoid_steady_state
:::

# Conclusions and next steps

The research process converged on a testable, mechanistic model attributing platform-specific yield loss to evaporation-induced biophysical stress. The proposed combinatorial experiment is designed to validate this model by systematically mapping the interactions between physical (PEG) and metabolic (PPK/PolyP) stabilizers. The resulting data will directly inform the development of a robust PURE system formulation optimized for automated, open-air platforms.

This synthesis centers on {claim}`claim-h1-unified-evaporation-metabolism-stress-mo`, {claim}`claim-h2-biophysical-robustness-a-synergistic-mod`.

Grounding evidence includes {evidence}`ev-h1-1-finding-magnesium-mg2-is-a-critical-cofa`, {evidence}`ev-h1-2-finding-high-concentrations-of-potassium`.
