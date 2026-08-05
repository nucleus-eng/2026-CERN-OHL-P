---
abstract: |
  PURE systems exhibit limited operational lifetimes at 37 °C, but whether this stems from component instability or resource depletion remains unclear. We systematically deconvolved the Cytosol system and demonstrated that individual components remain fully active when thermally incubated in isolation. Instead, performance loss requires multi-component coexistence. Pre-incubating a small-molecule mix (SMix) with a protein mix (PMix) reduced translation yields, an effect severely exacerbated by ribosomes. These findings indicate that reaction lifetime is limited by an uncoupled, background metabolic drain rather than the intrinsic thermal decay of individual system resources.
---

# Overview

# Results

## Experiment 1: Evaluating the Thermal Stability of Cytosol Components

To investigate the mechanisms underlying the finite operational lifetime of Cytosol/PURE cell-free reactions, we performed a series of pre-incubation experiments. Standard Cytosol reactions were assembled and incubated at 37 °C for varying durations (0, 30, 60, 90, and 120 min) prior to the introduction of the DNA template. This approach allowed us to determine whether critical reaction components such as the PMix or SMix undergo intrinsic thermal degradation in the absence of active protein synthesis. We hypothesized that a time-dependent decrease in protein expression yield following pre-incubation would indicate that essential system components are thermally unstable at 37 °C. Conversely, sustained reaction performance across all pre-incubation windows would suggest that the typical decline in yield is driven by resource depletion during active translation rather than component instability.

:::{table} Composition of Reaction Mastermix
:label: reaction-composition1
:align: center
| Component | Input concentration | Unit | Final concentration | Unit | Volume for one reaction (µL) |
| --- | --- | --- | --- | --- | --- |
| SMix | 3.33 | × | 1 |	× |	10.51 |
| PMix | 15	| mg/mL | 1.80 | mg/mL| 4.2 |
| Ribosomes	| 10 | µM |	1.8 | µM | 6.3 |
| pOpen-deGFP DNA |	60	| nM | 3 |nM | 1.75 |
| tRNA | 35	| mg/ml | 3.5 | mg/ml |	3.5 |
| Water | | | | | 8.74 |				
| Total volume (µL) | | | | | 35 |

A 35 μL mastermix was prepared for each reaction **(without DNA)**, and incubated at 37 °C for varying durations. At the end of incubation, DNA template was added to each Mastermix and 10 μL aliquots were dispensed in triplicate into a 384-well plate for fluorescence measurements.
:::

:::{figure} ./experiments/20260506-Cytosol-Lifetime-Test/kinetics-normalized.png
:label: fig1
:width: 75%
Pre-incubation of the Cytosol reactions at 37 °C in the absence of the DNA template resulted in a time-dependent decrease in Cytosol performance.
:::

Our results revealed a clear, time-dependent decrease in Cytosol performance correlated with increasing pre-incubation time. This decline could abstractly be attributed to either the degradation of macromolecular protein components (e.g., PMix or ribosomes) or the degradation of low-molecular-weight species (e.g., SMix components or tRNAs). Previous literature indicates that PURE reactions can sustain protein synthesis for over 24 hours at 32 °C within dialysis cassettes where SMix is continuously replenished from an outer reservoir while the macromolecular translation machinery remains functional (https://pubs.acs.org/doi/10.1021/acssynbio.4c00618). Consequently, we initially suspected that SMix degradation was the primary driver of the observed decline. Additionally, futile cycles of tRNA aminoacylation during the 37 °C pre-incubation period could prematurely deplete the reaction's energy reserves (ATP/GTP).

## Experiment 2: Assessing the Impact of tRNA Aminoacylation on Energy Depletion

To test whether autonomous tRNA aminoacylation drives premature energy depletion, we omitted both the DNA template and tRNAs from the mixture during the initial 37 °C incubation period of 2 hours. These components were subsequently replenished immediately prior to initiating kinetic measurements.

:::{table} Composition of Reaction Mastermix
:label: reaction-composition2
:align: center
| Component | Input concentration | Unit | Final concentration | Unit | Volume for one reaction (µL) |
| --- | --- | --- | --- | --- | --- |
| SMix | 3.33 | × | 1 |	× |	10.51 |
| PMix | 15	| mg/mL | 1.80 | mg/mL| 4.2 |
| Ribosomes	| 10 | µM |	1.8 | µM | 6.3 |
| pOpen-deGFP DNA |	60	| nM | 3 |nM | 1.75 |
| tRNA | 35	| mg/ml | 3.5 | mg/ml |	3.5 |
| RNAse Inhibitor Murine | 40000 | U/ml | 2000 | U/ml |	1.75 |
| Water | | | | | 6.99 |				
| Total volume (µL) | | | | | 35 |

A 35 μL mastermix was prepared for each reaction **(without DNA and tRNA)**, and incubated at 37 °C for varying durations. At the end of incubation, DNA template and tRNA were added to each Mastermix and 10 μL aliquots were dispensed in triplicate into a 384-well plate for fluorescence measurements.
:::

:::{figure} ./experiments/20260521-Cytosol-Lifetime-Test-R2/kinetics-normalized.png
:label: fig2
:width: 75%
The omission of both tRNAs and the DNA template during pre-incubation failed to rescue reaction yields, thereby refuting the hypothesis that tRNA aminoacylation drives premature energy depletion.
:::

Interestingly, omitting tRNAs during the pre-incubation phase failed to rescue the reaction yield; a comparable decrease in Cytosol performance was still observed. This finding indicates that tRNA aminoacylation is not the primary driver of energy depletion during the pre-incubation window. Instead, the data suggested two alternative possibilities: either one or more isolated Cytosol components undergo independent thermal degradation during the 2-hour exposure to 37 °C, or an alternative, non-translational energy-consuming process occurs.


## Experiment 3: Deconvoluting the Thermal Stability of Isolated Components

To systematically identify which individual components might be susceptible to thermal inactivation, we incubated SMix, tRNAs, PMix, Ribosomes, DNA template, and RNAse Inhibitor Murine (RIM) separately at 37 °C for 2 hours before using them to assemble Cytosol reactions.

:::{table} Composition of Reaction Mastermix
:label: reaction-composition3
:align: center
| Component | Input concentration | Unit | Final concentration | Unit | Volume for one reaction (µL) |
| --- | --- | --- | --- | --- | --- |
| SMix | 3.33 | × | 1 |	× |	10.51 |
| PMix | 15	| mg/mL | 1.80 | mg/mL| 4.2 |
| Ribosomes	| 10 | µM |	1.8 | µM | 6.3 |
| pOpen-deGFP DNA |	60	| nM | 3 |nM | 1.75 |
| tRNA | 35	| mg/ml | 3.5 | mg/ml |	3.5 |
| RNAse Inhibitor Murine | 40000 | U/ml | 2000 | U/ml |	1.75 |
| Water | | | | | 6.99 |				
| Total volume (µL) | | | | | 35 |

A 35 μL mastermix was prepared for each reaction, and 10 μL aliquots were dispensed in triplicate into a 384-well plate for fluorescence measurements.
:::

:::{figure} ./experiments/20260603-Cytosol-Lifetime-Test3/kinetics-normalized.png
:label: fig3
:width: 75%
No reduction in expression was observed relative to the Cytosol Control reaction across any condition, except for the pre-incubated DNA sample. This decrease is likely driven by thermal degradation of the template via contaminating DNases. **Note:** As a result of transient plate reader malfunctions during the incubation period, only steady state yields were recorded.
:::

Surprisingly, none of the reactions assembled from individually pre-incubated components showed a significant reduction in reporter protein expression relative to the control, with the sole exception of the condition where the DNA template itself was incubated at 37 °C.

This presents an apparent paradox: while the combined reaction components (minus DNA/tRNA) exhibit a severe loss of yield after a 2-hour pre-incubation (Experiment 1 and Experiment 2), the components remain fully functional when incubated in isolation (Experiment 3). We can therefore conclude that the observed loss in performance is not caused by the intrinsic thermal degradation of isolated resources. Instead, the loss of activity requires the coexistence of multiple components, pointing toward a mechanism of resource depletion mediated by nonspecific or contaminating enzymatic activities present within the PMix or ribosome fractions.

## Experiment 4: Identifying the Component Combinations Driving Resource Depletion

To elucidate which specific combinations of components trigger this resource depletion, we pre-incubated various binary and ternary mixtures of Cytosol components at 37 °C for 2 hours prior to final reaction assembly.

:::{table} Composition of Reaction Mastermix
:label: reaction-composition3
:align: center
| Component | Input concentration | Unit | Final concentration | Unit | Volume for one reaction (µL) |
| --- | --- | --- | --- | --- | --- |
| SMix | 3.33 | × | 1 |	× |	10.51 |
| PMix | 15	| mg/mL | 1.80 | mg/mL| 4.2 |
| Ribosomes	| 10 | µM |	1.8 | µM | 6.3 |
| pOpen-deGFP DNA |	60	| nM | 3 |nM | 1.75 |
| tRNA | 35	| mg/ml | 3.5 | mg/ml |	3.5 |
| RNAse Inhibitor Murine | 40000 | U/ml | 2000 | U/ml |	1.75 |
| Water | | | | | 6.99 |				
| Total volume (µL) | | | | | 35 |

A 35 μL mastermix was prepared for each reaction, and 10 μL aliquots were dispensed in triplicate into a 384-well plate for fluorescence measurements.
:::

:::{figure} ./experiments/20260609-Cytosol-Lifetime-Testing4/kinetics-normalized.png
:label: fig4
:width: 75%
Pre-incubation of the binary SMix + PMix mixture reduced subsequent protein yields compared to the Cytosol control. Notably, the most pronounced reduction in yield occurred within the ternary SMix + PMix + Ribo sample.
:::

Pre-incubation of the SMix + PMix binary mixture resulted in a modest reduction in subsequent protein yield compared to the control. In contrast, the SMix + Ribo and PMix + Ribo binary mixtures exhibited no significant decrease in performance. Remarkably, the largest drop in yield was observed when the ternary mixture of SMix + PMix + Ribo was pre-incubated.

The synergistic negative effect seen in the SMix + PMix + Ribo condition, which far exceeds the minor decline observed in the SMix + PMix condition, suggests a complex multi-component interaction. Because SMix contains the primary energy buffers (ATP, GTP, and other substrates) and PMix contains essential translation factors (initiation, elongation, and release factors), we hypothesize that the translation factors within the PMix interact with the ribosomes to stimulate an uncoupled, high-rate GTP/ATP consumption cycle (such as continuous, futile ribosome-regeneration activity or ribosome-dependent GTPase activation). This background enzymatic activity rapidly depletes the energy substrates provided by the SMix, prematurely exhausting the system before the DNA template is introduced to initiate target protein synthesis.

# Discussion

To elucidate the mechanisms limiting the operational lifetime of Cytosol and PURE cell-free systems, we evaluated two conventional hypotheses:

- Translation-Coupled Resource Depletion: Posited that finite reaction lifetimes are driven by substrate exhaustion during active protein synthesis. This was refuted by Experiments 1 and 2, where pre-incubating the reaction mixtures at 37 °C without a DNA template or tRNAs still significantly reduced final protein yields.

- Intrinsic Component Instability: Posited that individual components undergo thermal degradation at physiological temperatures. This was falsified in Experiment 3, as all constituents (PMix, SMix, ribosomes, and tRNAs) remained robustly stable and fully functional when incubated individually for 2 hours prior to assembly.

**Coexistence-Mediated Metabolic Drain**

Deconvolution of component mixtures in Experiment 4 revealed that the performance decline is driven by a multi-component, coexistence-mediated process. Rather than individual molecular decay, the system undergoes a rapid, non-specific background metabolic drain. This uncoupled activity requires the simultaneous presence of SMix, PMix, and ribosomes, suggesting that background interactions prematurely exhaust vital ATP and GTP reserves.