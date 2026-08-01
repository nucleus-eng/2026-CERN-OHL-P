---
abstract: |
 The Developer Cell Control Module integrates the ATP-dependent ClpXP protease complex to enable programmable post-translational regulation within PURE-based systems. In this DevNote, we reconstitute and evaluate ClpXP-mediated degradation of ssrA-tagged target proteins in bulk reactions. Using combinations of purified protein components and DNA templates supplemented with PURE, we demonstrate selective and energy-dependent degradation of target substrates.
---


# Overview

The [Control Module](https://devnotes.nucleus.engineering/articles/clpxp-module-plan) of the [Developer Cell](https://devnotes.bnext.bio/articles/developer-cell-introduction) is dedicated to enabling precise, time-resolved control of protein expression within synthetic minimal systems, particularly those based on the PURE system. Please refer to [Control Module](https://devnotes.nucleus.engineering/articles/clpxp-module-plan) for Module overview and background information. 

In this DevNote, we performed the degradation of the protein targeted with ssrA tag by ClpX and ClpP proteases in bulk reactions. We tested different combinations of purified proteins and DNA constructs with addition of PURE system to verify the target protein degradation. 

:::{figure} ./figures/clpXP.png
:name: fig:scheme
:align: center
:width: 65%

Cartoon of the general mechanism of protein degradation by ClpXP, ATP-dependent protease. Adapted from [R. Wedam, et al.](https://doi.org/10.3390/cancers15071936)
:::

# Exprimental Design

The goal is to demonstrate degradation of the GFP-ssrA protein by the AAA+ ATPase ClpX and the tetradecameric peptidase ClpP, as well as our ability to tune the extent of degradation. To achieve this, we show that GFP tagged with the ssrA sequence can be efficiently degraded either by purified ClpXP proteins or by ClpXP complexes expressed directly from DNA templates in the PURE system. We also examine the reverse configuration, in which GFP-ssrA is expressed using the PURE system and ClpXP is supplied in purified form, confirming that protein expression and degradation can be independently controlled. We further explore tuning by combining two DNA constructs in PURE reactions together with a purified protein component. The combinations of DNA templates and purified proteins used in each experiment or condition are listed below.

:::{table} This DevNote describes 8 bulk reaction experiments that test combinations of Control Module components. V = present in experiment; X = not present in experiment. 
| **Experiments** | **Purified ClpX** | **Purified ClpP** | **Purified GFP-ssrA** | **ClpP DNA** | **GFP-ssrA DNA** | **ClpX DNA** | **Sucrose/ Optiprep** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Experiment 1 | V | V | V | X | X | X | X |
| Experiment 2 | V | V | X | X | V | X | X |
| Experiment 3 | X | X | V | X | X | V | X |
| Experiment 4 | V | X | V | V | X | X | X |
| Experiment 5 | V | X | X | V | V | X | X |
| Experiment 6 | X | X | X | V | V | V | X |

:::

## DNA Constructs and Purified Proteins

All DNA constructs are designed to be used in PURE reactions for protein expressions:

| **DNA Constructs** | **Description** | 
| --- | --- |
| [pOpen-pT7-ClpP-CHis](https://github.com/nucleus-eng/DNA/blob/bf9cfc08f1e1443f8185da24cf78467c67911766/control/pOpen-ClpP-CHis.gb) | Express ClpP protein in the pOpen plasmid |
| [pOpen-pT7-ClpX-CHis](https://github.com/nucleus-eng/DNA/blob/bf9cfc08f1e1443f8185da24cf78467c67911766/control/pOpen-ClpX-CHis.gb) | Express ClpX protein in the pOpen plasmid |
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

## Reaction compositions

::::{tip} Experiment 1
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
| NEB PURExpress Solution A | 4 | 4 | 4 | 4 |
| NEB PURExpress Solution B | 3 | 3 | 3 | 3 |
| RNase Inhibitor | 0.5 | 0.5 | 0.5 | 0.5 |
| Nucleus Free Water | 1 | 1.5 | 1.5 | 2 |
| **Total** | **10** | **10** | **10** | **10** |
:::
::::

::::{tip} Experiment 2
:class: simple
:class: dropdown
:icon: false

:::{table}
:label: tbl-exp2
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
::::

::::{tip} Experiment 3
:class: simple
:class: dropdown
:icon: false

:::{table}
:label: tbl-exp3
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
::::

::::{tip} Experiment 4
:class: simple
:class: dropdown
:icon: false

:::{table}
:label: tbl-exp4
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
::::

::::{tip} Experiment 5
:class: simple
:class: dropdown
:icon: false

:::{table}
:label: tbl-exp5
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
::::


::::{tip} Experiment 6
:class: simple
:class: dropdown
:icon: false

:::{table}
:label: tbl-exp6
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
::::

***


# Observations and Experimental Results

The first experiment ({ref}`tbl-exp1`) involved mixing purified deGFP ssrA with purified ClpX and ClpP. We observed a clear decrease in GFP fluorescence over time, indicating that deGFP ssrA was efficiently degraded by the ClpXP protease. The degradation was rapid, with the GFP signal nearly disappearing within one and a half hours. In contrast, samples containing only purified ClpX or only purified ClpP did not show a significant decrease in fluorescence, confirming that degradation occurs only when both components of the ClpXP complex are present {ref}`fig:Protein`.

After establishing the functionality of the purified ClpXP degradation system, we next incorporated the PURE system. In this experiment ({ref}`tbl-exp2`), purified ClpP was replaced with pT7 ClpP DNA. Again, we observed a decrease in deGFP fluorescence over time, demonstrating that ClpP can be expressed in vitro by PURE and remains functional for deGFP degradation {ref}`fig:ClpP DNA`.

<!-- ./figures/ClpXP-protein.png -->
:::{figure} #20251120-kinetics
:label: fig:Protein
:align: center
:width: 65%

GFP fluorescence of samples containing purified proteins incubated at 37 °C for 4 hours. 
:::

<!-- ./figures/ClpP DNA with ClpX and GFP proteins.png -->
:::{figure} #20250919-kinetics  
:name: fig:ClpP DNA
:align: center
:width: 65%

GFP fluorescence signal in PURE reactions incubated at 37 °C for 6 hours. The reaction contains pT7-ClpP DNA, purified ClpX protein and purified deGFP-ssrA protein.
:::



Besides using ClpP DNA, we also tested ClpX DNA to express the ClpX protease using the PURE system ({ref}`tbl-exp3`). When the reaction was supplemented with purified ClpP protein and purified deGFP-ssrA substrate, we again observed the expected decrease in deGFP fluorescence over time. In contrast, the control reaction lacking ClpX DNA maintained constant fluorescence, aside from the small initial drop consistently seen in earlier experiments {ref}`fig:ClpX DNA`. 

<!-- ./figures/ClpX DNA with ClpP and GFP proteins.png -->
:::{figure} #20251205-kinetics
:label: fig:ClpX DNA
:align: center
:width: 70%

GFP fluorescence signal in PURE reactions incubated at 37 °C for 6 hours. The reaction contains pT7-ClpX DNA, purified ClpP protein and purified deGFP-ssrA protein.
:::


Next, instead of using ClpP DNA, we replaced purified deGFP-ssrA with pT7-deGFP DNA for PURE-based expression and degradation ({ref}`tbl-exp4`). By tuning the concentrations of purified ClpX and ClpP while keeping pT7-deGFP constant, we were able to control the GFP degradation kinetics. As expected, higher amounts of ClpXP resulted in faster decreases in GFP fluorescence. Interestingly, in a single PURE reaction, we could observe the fluorescence first rising (due to in vitro expression) and then declining (due to degradation) {ref}`fig:GFP DNA`. Notably, it's hard to see the GFP signal returning to its initial baseline in most of the reactions, suggesting that the system likely exhausted its available energy for continued protein degradation.

<!-- missing notebook -->
:::{figure} #20251021-kinetics
:name: fig:GFP DNA
:align: center
:width: 70%

GFP fluorescence signal produced using pT7-deGFP-ssrA DNA in PURE reactions incubated at 37 °C for 6 hours. Purified ClpX protein and purified ClpP protein are added to the reactions.
:::

Besides expressing a single protein from DNA in PURE, I also attempted to express two proteins simultaneously in one PURE reaction using two plasmids, pT7 ClpP and pT7 deGFP ssrA ({ref}`tbl-exp5`). Interestingly, we observed an oscillatory pattern in the GFP fluorescence over time. The fluorescence first increased strongly and then dropped quickly, which indicates rapid GFP degradation. After this initial decrease, the GFP signal increased again, although the second peak was lower than the first one, and it was then degraded again. Similar oscillations were observed even when we increased the total amount of DNA or tested different DNA concentrations in the PURE reactions {ref}`fig:Two DNA`.

<!-- ./figures/ClpXP-Two DNA.png -->
:::{figure} #20251016-kinetics 
:name: fig:Two DNA
:align: center
:width: 70%

GFP fluorescence signal produced using pT7-deGFP-ssrA DNA in PURE reactions incubated at 37 °C for 6 hours. ClpP is co-expressed in the same PURE reaction using pT7-ClpP DNA. Purified ClpX protein is added to the reactions.
:::

Finally, we examined the simultaneous expression of three proteins within a single PURE reaction using three plasmids: pT7-ClpX, pT7-ClpP, and pT7-deGFP-ssrA ({ref}`tbl-exp6`). By systematically tuning the concentrations of each DNA, we were able to modulate both the expression and degradation dynamics of deGFP-ssrA. As the ratio of ClpX and ClpP DNA relative to deGFP-ssrA DNA increased, the overall deGFP-ssrA fluorescence decreased and its degradation rate increased, consistent with enhanced proteolytic activity. Interestingly, after an initial phase of degradation, the deGFP signal exhibited a recovery (“bounce-back”) behavior. Both the rate and magnitude of this recovery were higher at lower ClpX/ClpP DNA concentrations, suggesting a shift toward deGFP-ssrA expression as protease levels became limiting. Despite these differences in dynamics, all PURE reactions eventually reached steady state. However, reactions with lower ClpXP-to-deGFP-ssrA ratios required a longer time to reach steady state compared with those containing higher ClpXP ratios {ref}`fig:Three DNA`.


<!-- ./figures/ClpXP-3DNA.png -->
:::{figure} #20251212-kinetics
:label: fig:Three DNA
:align: center
:width: 70%

GFP fluorescence signal produced using pT7-deGFP-ssrA DNA in PURE reactions incubated at 37 °C for 6 hours. ClpX and ClpP DNAs are co-expressed in the same PURE reaction.
:::



# Conclusion and New Horizons

These experiments demonstrate that the ClpXP based control module functions effectively with the PURE system in bulk reactions. We expected that introducing more independent DNA templates into a single PURE reaction will bring additional complexity. The next step is to test this module in liposomes. 
 
**Acknowledgments**

This work is supported by the Astera Institute and Sloan Foundation (Grant G-2024-22735).
