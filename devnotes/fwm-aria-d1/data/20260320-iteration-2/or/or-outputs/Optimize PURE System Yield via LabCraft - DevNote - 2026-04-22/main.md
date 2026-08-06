---
title: 'Dev Note - bnext-iter-2'
abstract: |
  We investigate the reduced protein yield in PURE systems assembled by an automated, component-wise liquid handler. Our analysis suggests this is not a failure of final component stoichiometry, but a process-induced limitation rooted in non-equilibrium dynamics. We hypothesize that sequential component addition creates transient concentration spikes, leading to the formation of kinetically-trapped, non-productive states like inorganic precipitates or protein aggregates. A multivariate experiment is designed to test this 'path-dependent yield limitation' by systematically varying both component concentrations and their order of addition to identify an optimized assembly pathway.
---

# Overview

Automated cell-free protein synthesis platforms like LabCraft promise high-throughput experimentation, but can suffer from performance deficits compared to manual, pre-mixed preparations. This work addresses a persistent reduction in protein yield observed in LabCraft-assembled PURE systems. Through a process of structured debate and hypothesis generation, we moved beyond simple stoichiometric optimization to focus on the assembly process itself. The central hypothesis posits that the sequence of component addition creates path-dependent kinetic traps that limit yield. This note details this hypothesis and presents a multivariate experimental plan to map the interplay between assembly order and key component concentrations, aiming to discover a high-yield protocol.

## Workspace Data

See [workspace/workspace_data.csv](./workspace/workspace_data.csv) for the full exported dataset.

# Results

The investigation converged upon two highly-ranked hypotheses that describe how the automated assembly process itself can limit reaction yield. The core idea is that transient, localized concentrations during sequential mixing create distinct, non-productive states. Below, we outline these hypotheses and the experimental plan designed to distinguish between their proposed failure modes and identify an optimal assembly pathway.

## Claims

:::{claim} Path-Dependent Formation of Distinct Kinetically-Trapped States in Automated Assembly
:label: claim-h1-path-dependent-formation-of-distinct-kin

Reduced yield in LabCraft-assembled PURE systems is caused by the path-dependent formation of distinct, kinetically-trapped, non-productive states. Transient concentration spikes during sequential addition determine the type of trap formed: high local magnesium and energy components favor inorganic precipitates, while high local salts or proteins favor aggregation. Final yield is thus a function of the dominant
:::

:::{claim} Assembly Order Dictates the Dominant Kinetic Trap and Yield Ceiling in LabCraft PURE Systems
:label: claim-h2-assembly-order-dictates-the-dominant-kin

The specific order of component addition in LabCraft PURE systems determines the dominant, yield-limiting kinetic trap. Adding concentrated magnesium last to an energy-rich solution will favor inorganic precipitation. Conversely, adding the concentrated energy mix last to a magnesium-buffered solution will mitigate precipitation but may favor protein aggregation. Assembly order is therefore a direct, controllable variable
:::

## Evidence

:::{evidence} Support from Hypothesis Debate: General Framework
:label: ev-h1-1-rationale-from-debate-explorer-1-vs.-arc
:supports: claim-h1-path-dependent-formation-of-distinct-kin

The 'Explorer 1' hypothesis was favored in debate for providing a general framework of path-dependent, kinetically-trapped states that could encompass multiple, distinct failure modes.
:::

:::{evidence} Support from Hypothesis Debate: Testable Mechanism
:label: ev-h1-2-rationale-from-debate-architect-1-vs.-qu
:supports: claim-h1-path-dependent-formation-of-distinct-kin

The 'Architect 1' hypothesis was praised for proposing a specific, testable mechanism (inorganic precipitation) that directly addressed the performance difference between automated and manual assembly.
:::

:::{evidence} Literature Support: Assembly Method Matters
:label: ev-h1-3-finding-the-method-of-pure-system-assemb
:supports: claim-h1-path-dependent-formation-of-distinct-kin

Different PURE system assembly methods (e.g., from individual components versus pre-mixed solutions) can result in different performance, requiring method-specific optimization (Bernard-Lapeyre et al., 2026).
:::

:::{evidence} Rationale for Hypothesis Evolution
:label: ev-h1-4-path-dependent-formation-of-distinct-kin
:supports: claim-h1-path-dependent-formation-of-distinct-kin

This hypothesis integrates the general 'kinetically-trapped states' framework with the specific mechanism of 'inorganic precipitation', making the abstract concept more testable by proposing concrete, distinguishable failure modes (precipitation vs. aggregation).
:::

:::{evidence} Incorporation of a More General Framework
:label: ev-h2-1-rationale-from-debate-explorer-1-vs.-arc
:supports: claim-h2-assembly-order-dictates-the-dominant-kin

This hypothesis incorporates the winning debate concept of 'kinetically-trapped, non-productive complexes' to provide a more powerful explanatory model.
:::

:::{evidence} Research Opportunity: Characterizing Automated Assembly
:label: ev-h2-2-opportunity-the-specific-mechanistic-rea
:supports: claim-h2-assembly-order-dictates-the-dominant-kin

The specific mechanistic reasons for reduced yield in PURE systems assembled by component-wise automated methods are not yet fully characterized, representing a key knowledge gap.
:::

:::{evidence} Analogical Support from Chemical Synthesis
:label: ev-h2-3-analogical-support-from-chemistry-where
:supports: claim-h2-assembly-order-dictates-the-dominant-kin

In chemical synthesis, the order of reagent addition is often critical for controlling reaction pathways and preventing the formation of unwanted precipitates.
:::

:::{evidence} Rationale for Hypothesis Evolution
:label: ev-h2-4-assembly-order-dictates-the-dominant-kin
:supports: claim-h2-assembly-order-dictates-the-dominant-kin

This hypothesis evolves prior ideas by proposing a specific, actionable solution rooted in non-equilibrium dynamics: controlling the order of addition. It makes the abstract concept of 'path dependency' directly testable and prescriptive for improving the LabCraft process.
:::

## Detailed Findings

## Executive Summary

This research aimed to understand and overcome the reduced protein yield (`sigmoid_steady_state`) observed in PURE systems assembled via the automated, component-wise LabCraft machine. Through a literature review and a debate-driven hypothesis generation process, the core problem was identified not as a simple issue of final component concentrations, but as a process-induced limitation. The IGOR process converged on the concept of 'path-dependent yield limitation,' where the sequential addition of components creates transient localized concentration spikes, leading to kinetically-trapped, non-productive states (e.g., inorganic precipitates or protein aggregates). The top-ranked hypotheses propose that the specific order of addition of critical components, such as magnesium and the energy regeneration mix, dictates which of these failure modes dominates, thereby setting a ceiling on the final yield. A multivariate experimental plan has been designed to test this by systematically varying both component concentrations and their order of addition, aiming to map this complex interaction and identify an optimized assembly pathway for the LabCraft system.

## Top-Ranked Hypotheses

### 1. Path-Dependent Formation of Distinct Kinetically-Trapped States in Automated Assembly

The reduced yield in PURE systems assembled by LabCraft is caused by path-dependent formation of kinetically-trapped, non-productive complexes, a phenomenon that manifests in distinct, experimentally distinguishable forms. Building on the general framework of path-dependency, we propose that the specific class of trap formed is determined by which components experience transient concentration spikes during sequential addition. Specifically, localized spikes of Magnesium and energy components (e.g., Creatine Phosphate, ATP) will favor the formation of inorganic precipitates (e.g., magnesium pyrophosphate), while localized spikes in salts (e.g., Potassium Glutamate) or proteins will favor protein/ribosome aggregation. The final yield is therefore a function of not only the final concentrations but the dominant kinetic trap established by the assembly pathway, providing a more comprehensive model that unifies previous, more specific hypotheses.

**Final rationale:**

This hypothesis was evolved by combining the winning general framework of 'Explorer 1' (path-dependent, kinetically-trapped states) with the specific, testable mechanism from 'Architect 1' (inorganic precipitation). The debate revealed that 'Explorer 1' was powerful but abstract. This evolution addresses that by proposing multiple, concrete, and distinguishable failure modes (inorganic precipitation vs. protein aggregation) under the same general umbrella. It makes the abstract concept more testable and provides a richer, more nuanced model that has greater explanatory power than either predecessor alone.

**Key supporting evidence:**
- Rationale from debate (Explorer 1 vs. Architect 1): 'Explorer 1' was praised for its general framework that could encompass multiple failure modes.
- Rationale from debate (Architect 1 vs. Quant 1): 'Architect 1' was praised for its specific, testable mechanism directly addressing the automated vs. manual assembly problem.
- Finding: The method of PURE system assembly, whether from individual components (as with LabCraft) or from pre-mixed solutions, can lead to different performance outcomes, necessitating method-specific optimization. (Bernard-Lapeyre et al., 2026)

### 2. Assembly Order Dictates the Dominant Kinetic Trap and Yield Ceiling in LabCraft PURE Systems

The reduced yield in LabCraft-assembled PURE systems is determined by the specific order in which critical components are added, which in turn selects for a dominant, yield-limiting kinetic trap. We hypothesize that the sequence of adding Magnesium Acetate relative to the primary energy source (Creatine Phosphate and ATP/GTP) dictates the failure mode. Specifically, (1) adding concentrated Magnesium to a solution already containing the energy mix will favor inorganic magnesium pyrophosphate precipitation. Conversely, (2) adding the concentrated energy mix to a solution where Magnesium is already present and buffered by other components will mitigate precipitation but may instead favor protein/ribosome aggregation due to localized ionic strength changes. This 'assembly order' hypothesis proposes a direct, controllable experimental variable that determines which non-productive, kinetically-trapped state is formed, thereby setting a path-dependent ceiling on the final protein yield.

**Final rationale:**

This hypothesis evolves 'Architect 1' by incorporating the more powerful 'kinetically-trapped state' framework from the tournament winner, 'Explorer 1', thus addressing its main criticism of being too narrow. It introduces a significant element of novelty by moving beyond just identifying a problem (precipitation) to proposing a specific, actionable solution rooted in non-equilibrium dynamics: controlling the *order of addition*. This makes the hypothesis not only explanatory but also directly prescriptive for improving the LabCraft process, a key research goal. It elegantly links the abstract concept of 'path dependency' to a simple, testable experimental variable.

**Key supporting evidence:**
- Rationale from debate (Explorer 1 vs. Architect 1): The winning hypothesis proposed a more general framework of 'kinetically-trapped, non-productive complexes' which is now incorporated.
- Opportunity: The specific mechanistic reasons for reduced yield in PURE systems assembled via automated, component-wise methods (like LabCraft) compared to manual, pre-mixed methods are not fully characterized.
- Analogical support from chemistry where the order of reagent addition is critical in preventing precipitation and controlling reaction pathways.

## Proposed Experimental Plan

### Objective
To test the hypothesis that the assembly pathway dictates the formation of distinct, yield-limiting kinetic traps in the LabCraft PURE system. The goal is to identify an assembly order and concentration profile for Magnesium Acetate and Creatine Phosphate that maximizes the final protein yield (`sigmoid_steady_state`) by avoiding these non-productive states.

### Multivariate Design Space
This experiment abandons a one-factor-at-a-time approach and instead uses a multivariate combinatorial design. We will simultaneously vary a categorical variable (Assembly Order) and two continuous variables (component concentrations).

1.  **Categorical Variable: Assembly Order**
    *   **`Order_A (Precipitation-Prone)`**: LabCraft protocol will be programmed to first dispense a master mix of all components *except* Magnesium Acetate. Then, the full volume of concentrated Magnesium Acetate will be added last. This sequence is hypothesized to create transient, localized Mg²⁺ spikes that favor inorganic precipitation.
    *   **`Order_B (Aggregation-Prone)`**: LabCraft protocol will be programmed to first dispense a master mix of all components *except* the energy sources (Creatine Phosphate, ATP, GTP). Then, a concentrated mix of these energy components will be added last. This sequence is hypothesized to mitigate inorganic precipitation but may promote protein/ribosome aggregation due to localized ionic strength changes.

2.  **Continuous Variables: Concentration Matrix**
    *   For *each* of the Assembly Orders defined above, a combinatorial matrix of concentrations will be explored.
    *   **`[Magnesium acetate] (mM)`**: 5 levels, e.g., `{5, 10, 15, 20, 25}` mM.
    *   **`[Creatine phosphate] (mM)`**: 5 levels, e.g., `{20, 30, 40, 50, 60}` mM.

This design creates a batch of `2 (Orders) x 5 (Mg levels) x 5 (CP levels) = 50` unique experimental conditions, plus controls and replicates. This batch structure will efficiently map the complex interaction landscape between assembly path and component concentrations, directly addressing the epistemic uncertainty around the LabCraft performance gap.

### Batch Protocol Steps
1.  Prepare concentrated stock solutions for all PURE system components.
2.  Program the LabCraft liquid handler with two distinct, multi-step protocols corresponding to `Order_A` and `Order_B`.
3.  For `Order_A`, the program will:
    a. Create an intermediate master mix (IMM-A) of all components (including Creatine Phosphate, ATP, GTP) except Magnesium Acetate.
    b. Dispense the required volumes of IMM-A for each well.
    c. Dispense the specified volume of Magnesium Acetate stock solution into each well to achieve the target concentration from the design matrix.
4.  For `Order_B`, the program will:
    a. Create an intermediate master mix (IMM-B) of all components (including Magnesium Acetate) except the energy sources (CP, ATP, GTP).
    b. Dispense the required volumes of IMM-B for each well.
    c. Dispense the specified volume of a concentrated energy mix into each well to achieve the target concentrations.
5.  Add the DNA template for deGFP expression to all wells.
6.  Seal the plate and immediately begin measurements in the plate reader at 37°C.

### Optimization Metrics
1.  **Primary Metric (`sigmoid_steady_state`)**: Final fluorescence endpoint will be used to quantify total protein yield. The results will generate two distinct yield landscapes (one for each Assembly Order) as a function of Mg²⁺ and CP concentrations. This directly evaluates the highly coupled interaction between assembly path and stoichiometry.
2.  **Secondary Metric (`sigmoid_rate (1/h)`)**: The maximum rate of fluorescence increase will be calculated to determine if the assembly path affects the kinetics of protein synthesis, not just the final yield.
3.  **Qualitative Metric (Initial Turbidity)**: An initial absorbance reading (e.g., at 600nm) or light scattering measurement will be taken at time zero for all wells. This serves as a direct, physical probe for the formation of precipitates or aggregates hypothesized to be the 'kinetic traps'. A correlation between high initial turbidity and low final yield would provide strong support for the hypothesis.

**Feedback Loop to Surrogate Model**: The results of this batch experiment—specifically, the `sigmoid_steady_state` values for each of the 50+ conditions—will be fed back into the surrogate model. The `assembly_order` will be encoded as a new categorical feature. The model will then be retrained to learn not only the impact of Mg²⁺ and CP concentrations but also the critical influence of the assembly pathway. This will enable the model to actively optimize the assembly protocol itself, guiding future suggestions toward compositions and assembly sequences that are predicted to avoid kinetic traps and maximize yield, thereby driving the optimization process toward the stated goals.

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
- [Optimization of PURE system composition using automation and active learning](https://doi.org/10.64898/2026.03.23.713685), Bernard-Lapeyre et al., 2026, bioRxiv
- [Improved Cell-Free RNA and Protein Synthesis System](https://doi.org/10.1371/journal.pone.0106232), Li et al., 2014, PLoS ONE
- [Dissecting limiting factors of the Protein synthesis Using Recombinant Elements (PURE) system](https://doi.org/10.1080/21690731.2017.1327006), Li et al., 2017, Translation
- [Cell-free translation reconstituted with purified components](https://doi.org/10.1038/90802), Shimizu et al., 2001, Nature Biotechnology
- [A Simple](https://doi.org/10.1007/bf02701951), Robust, and Low-Cost Method To Produce the PURE Cell-Free System, Lavickova and Maerkl, 2019, ACS Synthetic Biology

## Dead Ends
- Bimodal Synergy of Magnesium and Creatine Phosphate Drives Protein Yield (ID: Quant 1): This hypothesis was rejected because it focused on rationalizing an existing data pattern rather than providing a novel, mechanistic explanation for the core research problem—the performance deficit of the automated LabCraft assembly process. The winning hypotheses were deemed more impactful as they addressed the *process-induced* limitations, which was central to the research goal.

## Figures

:::{figure} ./figures/viz-01-1d-sensitivity-for-20260309-discoveryplate-r1-i10.png
:label: fig:viz-01-1d-sensitivity-for-20260309-discoveryplate-r1-i10.png
:name: fig-viz-01-1d-sensitivity-for-20260309-discoveryplate-r1-i10.png
:grounds: ev-h1-1-rationale-from-debate-explorer-1-vs.-arc
:align: center
:width: 75%
1D Sensitivity for 20260309-DiscoveryPlate-R1-I10
:::

:::{figure} ./figures/viz-02-test-split-sigmoid_rate-1-h.png
:label: fig:viz-02-test-split-sigmoid_rate-1-h.png
:name: fig-viz-02-test-split-sigmoid_rate-1-h.png
:grounds: ev-h1-2-rationale-from-debate-architect-1-vs.-qu
:align: center
:width: 75%
Test Split: sigmoid_rate (1/h)
:::

:::{figure} ./figures/viz-03-similarity-of-20260319-discoveryplate-r2-i10-to-dataset.png
:label: fig:viz-03-similarity-of-20260319-discoveryplate-r2-i10-to-dataset.png
:name: fig-viz-03-similarity-of-20260319-discoveryplate-r2-i10-to-dataset.png
:grounds: ev-h1-3-finding-the-method-of-pure-system-assemb
:align: center
:width: 75%
Similarity of 20260319-DiscoveryPlate-R2-I10 to Dataset
:::

:::{figure} ./figures/viz-04-1d-sensitivity-for-20260319-discoveryplate-r2-i10-2.png
:label: fig:viz-04-1d-sensitivity-for-20260319-discoveryplate-r2-i10-2.png
:name: fig-viz-04-1d-sensitivity-for-20260319-discoveryplate-r2-i10-2.png
:grounds: ev-h1-4-path-dependent-formation-of-distinct-kin
:align: center
:width: 75%
1D Sensitivity for 20260319-DiscoveryPlate-R2-I10 (2)
:::

:::{figure} ./figures/viz-05-test-split-drift_rate-1-h.png
:label: fig:viz-05-test-split-drift_rate-1-h.png
:name: fig-viz-05-test-split-drift_rate-1-h.png
:grounds: ev-h2-1-rationale-from-debate-explorer-1-vs.-arc
:align: center
:width: 75%
Test Split: drift_rate (1/h)
:::

:::{figure} ./figures/viz-06-sensitivities-for-20260309-discoveryplate-r1-j13.png
:label: fig:viz-06-sensitivities-for-20260309-discoveryplate-r1-j13.png
:name: fig-viz-06-sensitivities-for-20260309-discoveryplate-r1-j13.png
:grounds: ev-h2-2-opportunity-the-specific-mechanistic-rea
:align: center
:width: 75%
Sensitivities for 20260309-DiscoveryPlate-R1-J13
:::

:::{figure} ./figures/viz-07-similarity-of-ges-1-to-dataset.png
:label: fig:viz-07-similarity-of-ges-1-to-dataset.png
:name: fig-viz-07-similarity-of-ges-1-to-dataset.png
:grounds: ev-h2-3-analogical-support-from-chemistry-where
:align: center
:width: 75%
Similarity of GES-1 to Dataset
:::

:::{figure} ./figures/viz-08-prob.-of-meeting-goals.png
:label: fig:viz-08-prob.-of-meeting-goals.png
:name: fig-viz-08-prob.-of-meeting-goals.png
:grounds: ev-h2-4-assembly-order-dictates-the-dominant-kin
:align: center
:width: 75%
Prob. of Meeting Goals
:::

:::{figure} ./figures/viz-09-1d-sensitivity-for-20260319-discoveryplate-r2-i10.png
:label: fig:viz-09-1d-sensitivity-for-20260319-discoveryplate-r2-i10.png
:name: fig-viz-09-1d-sensitivity-for-20260319-discoveryplate-r2-i10.png
:grounds: ev-h1-1-rationale-from-debate-explorer-1-vs.-arc
:align: center
:width: 75%
1D Sensitivity for 20260319-DiscoveryPlate-R2-I10
:::

:::{figure} ./figures/viz-10-1d-sensitivity-for-20260319-discoveryplate-r2-i15.png
:label: fig:viz-10-1d-sensitivity-for-20260319-discoveryplate-r2-i15.png
:name: fig-viz-10-1d-sensitivity-for-20260319-discoveryplate-r2-i15.png
:grounds: ev-h1-2-rationale-from-debate-architect-1-vs.-qu
:align: center
:width: 75%
1D Sensitivity for 20260319-DiscoveryPlate-R2-I15
:::

:::{figure} ./figures/viz-11-sigmoid_steady_state-vs-drift_rate-1-h.png
:label: fig:viz-11-sigmoid_steady_state-vs-drift_rate-1-h.png
:name: fig-viz-11-sigmoid_steady_state-vs-drift_rate-1-h.png
:grounds: ev-h2-4-assembly-order-dictates-the-dominant-kin
:align: center
:width: 75%
sigmoid_steady_state vs drift_rate (1/h)
:::

:::{figure} ./figures/viz-12-sigmoid_steady_state-vs-sigmoid_rate-1-h.png
:label: fig:viz-12-sigmoid_steady_state-vs-sigmoid_rate-1-h.png
:name: fig-viz-12-sigmoid_steady_state-vs-sigmoid_rate-1-h.png
:grounds: ev-h2-4-assembly-order-dictates-the-dominant-kin
:align: center
:width: 75%
sigmoid_steady_state vs sigmoid_rate (1/h)
:::

:::{figure} ./figures/viz-13-test-split-sigmoid_steady_state.png
:label: fig:viz-13-test-split-sigmoid_steady_state.png
:name: fig-viz-13-test-split-sigmoid_steady_state.png
:grounds: ev-h2-4-assembly-order-dictates-the-dominant-kin
:align: center
:width: 75%
Test Split: sigmoid_steady_state
:::

:::{figure} ./figures/viz-14-sigmoid_steady_state-vs-sigmoid_steady_state.png
:label: fig:viz-14-sigmoid_steady_state-vs-sigmoid_steady_state.png
:name: fig-viz-14-sigmoid_steady_state-vs-sigmoid_steady_state.png
:grounds: ev-h2-4-assembly-order-dictates-the-dominant-kin
:align: center
:width: 75%
sigmoid_steady_state vs sigmoid_steady_state
:::

# Conclusions and next steps

This research has successfully reframed the problem of reduced yield in automated PURE system assembly from a static optimization problem to one of non-equilibrium, process-dependent dynamics. The leading hypotheses concerning path-dependent formation of kinetic traps are both mechanistic and testable. The proposed multivariate experiment is designed to efficiently map the effects of assembly order and concentration, providing a clear path toward not only validating the core hypothesis but also discovering a robust, high-yield protocol for the LabCraft platform. The results will be used to retrain our surrogate model, incorporating assembly sequence as a key variable for future optimization campaigns.

This synthesis centers on {claim}`claim-h1-path-dependent-formation-of-distinct-kin`, {claim}`claim-h2-assembly-order-dictates-the-dominant-kin`.

Grounding evidence includes {evidence}`ev-h1-1-rationale-from-debate-explorer-1-vs.-arc`, {evidence}`ev-h1-2-rationale-from-debate-architect-1-vs.-qu`.
