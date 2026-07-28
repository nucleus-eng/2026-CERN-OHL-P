---
title: "ClpXP Control Module: Deployment in PURE with Nucleus Cytosol"
abstract: |
  We engineered a Cell Control Module that integrates the ATP-dependent ClpXP protease complex to enable programmable post-translational regulation in PURE-based systems. In the previous DevNote, we reconstituted and characterized ClpXP-mediated degradation of ssrA-tagged target proteins using the commercial NEB PURExpress system. In this DevNote, we extend this work by implementing the same module in Nucleus Cytosol, and demonstrate energy-dependent degradation of target substrates within the system.
---

# Overview

The [Control Module](https://devnotes.nucleus.engineering/articles/clpxp-module-plan) of the [Developer Cell](https://devnotes.bnext.bio/articles/developer-cell-introduction) is dedicated to enabling precise, time-resolved control of protein expression within synthetic minimal systems, particularly those based on the PURE system. Please refer to [Control Module](https://devnotes.nucleus.engineering/articles/clpxp-module-plan) for Module overview and background information. 

:::{figure} ./general/control-module.png
:name: fig:scheme
:align: center
:width: 65%
Illustration of the ClpXP protein degradation control module in the [Developer Cell](https://devnotes.nucleus.engineering/articles/developer-cell-introduction), with other modules grayed out.
:::

In the [previous DevNote](https://devnotes.nucleus.engineering/articles/bnext-devnotes-clpx-in-pure-01), we demonstrated the degradation of ssrA-tagged proteins by the ClpXP protease system in bulk reactions using the commercial NEB PURExpress system. In this DevNote, we replaced NEB PURE with Nucleus Cytosol and performed similar experiments using different combinations of purified proteins and DNA constructs to verify target protein degradation.

We also compared the performance of the two systems by evaluating protein expression levels, degradation efficiency, and degradation rates. These results help assess the capability of Nucleus Cytosol to support both protein synthesis and ClpXP-mediated protein degradation.



# Exprimental Design

The goal of this study is to demonstrate the degradation of GFP-ssrA by the AAA+ ATPase ClpX and the tetradecameric protease ClpP, as well as to evaluate tunable control over degradation levels.


## Bulk Reactions

We first tested whether purified GFP-ssrA can be efficiently degraded by purified ClpX and ClpP in the presence of Nucleus Cytosol, establishing baseline functionality of the control module in this environment. After confirming activity, we progressively replaced purified components with proteins expressed *in vitro* from linear DNA templates under a T7 promoter (pT7-GFP-ssrA, pT7-ClpX, and pT7-ClpP). We began by replacing one purified protein at a time, while keeping the others purified, and verified that the degradation system remained functional.

Next, we increased the number of components expressed in Nucleus Cytosol by replacing two of the three purified proteins, further testing whether the system could sustain functionality with limited energy resource and reduced reliance on purified proteins. Finally, we constructed a fully DNA-encoded system in which all three components (GFP-ssrA, ClpX, and ClpP) were co-expressed from linear DNA templates in Nucleus Cytosol, demonstrating the feasibility of a fully reconstituted Cytosol-expression-based control module.

In addition, we compared the performance of co-expression systems in commercial NEB PURExpress and Nucleus Cytosol by evaluating protein expression levels, degradation efficiency, and degradation rates.

The combinations of DNA templates and purified proteins used in each experiment or condition are listed below.

:::{table} This DevNote describes 5 bulk reaction experiments that test combinations of Control Module components. V = present in experiment; X = not present in experiment. 
| **Experiments** | **Purified ClpP** | **Purified ClpX** | **Purified GFP-ssrA** | **ClpP DNA** | **ClpX DNA** | **GFP-ssrA DNA** |
| --- | --- | --- | --- | --- | --- | --- |
| Experiment 1 (No DNA) | V | V | V | X | X | X |
| Experiment 2 (1 DNA) | X | V | V | V | X | X |
| Experiment 3 (1 DNA) | V | X | V | X | V | X |
| Experiment 4 (1 DNA) | V | V | X | X | X | V |
| Experiment 5 (2 DNA) | X | V | X | V | X | V |
| Experiment 6 (2 DNA) | V | X | X | X | V | V |
| Experiment 7 (3 DNA) | X | X | X | V | V | V |

:::


## DNA Constructs and Purified Proteins

All DNA constructs are designed to be used in PURE reactions for protein expression:

| **DNA Constructs** | **Description** | 
| --- | --- |
| Linear pT7-ClpX | Expresses ClpX protein using linear DNA |
| Linear pT7-ClpP | Expresses ClpP protein using linear DNA |
| Linear pT7-deGFP-ssrA | Expresses deGFP protein with ssrA tag using linear DNA |

All purified proteins were ordered from GenScript:

| **Proteins** | **Description** |
| --- | --- |
| ClpX | Purified ClpX protein expressed using pET30a plasmid |
| ClpP | Purified ClpP protein expressed using pET30a plasmid |
| deGFP-ssrA | Purified GFP protein wtih ssrA tag expressed using pET30a plasmid |


## Materials

| **Product** | **Brand** | **Catalog No.** |
| --- | --- | --- | 
| PURExpress® In Vitro Protein Synthesis Kit | New England Biolabs | E6800L | 
| RNase Inhinitor, Murine | New England Biolabs | M0314L |
| Nucleus Cytosol | b.next | N/A | 

***



# Observations and Experimental Results

## No DNA
The first experiment ({ref}`tbl-exp1`) involved mixing purified deGFP-ssrA with purified ClpX and ClpP in Nucleus cytosol reaction. We observed a clear decrease in GFP fluorescence over time, indicating efficient degradation of deGFP-ssrA by the ClpXP protease complex. The degradation was rapid, with the GFP signal nearly disappearing within one hour. As expected, the control samples containing either purified deGFP-ssrA alone or purified deGFP-ssrA with purified ClpP showed no significant decrease in fluorescence.

Interestingly, the control sample containing purified deGFP-ssrA and purified ClpX also exhibited a noticeable reduction in GFP fluorescence. This result was unexpected, as ClpX alone cannot degrade substrate proteins without the proteolytic activity of ClpP. One possible explanation is that the Nucleus cytosol contains residual endogenous ClpP that was not completely removed during the purification process. The presence of this residual ClpP could allow ClpX-mediated substrate recognition and unfolding to result in partial degradation, leading to the observed decrease in fluorescence. 

::::{tip} Reaction Compositions: Experiment 1 (No DNA)
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

:::{figure} ./general/Platereader/No DNA/No DNA.png
:name: fig:No DNA
:align: center
:width: 90%

GFP fluorescence signal of samples containing purified proteins in Nucleus Cytosol incubated at 37 °C for 6 hours. Data represent the mean of three replicate wells (n = 3), with shaded areas indicating SEM.
:::

## One DNA
After establishing the functionality of the purified ClpXP degradation system, we next incorporated Nucleus Cytosol-expressed proteins into the degradation module. We began by replacing one purified component with its corresponding DNA template. In the first experiment ({ref}`tbl-exp2`), purified ClpP was replaced with varying concentrations of pT7-ClpP DNA while purified deGFP-ssrA and ClpX were maintained in the reaction.

As shown in {ref}`fig:1 DNA-ClpP`, we again observed rapid decrease in deGFP fluorescence over time, demonstrating that ClpP can be efficiently expressed by Nucleus Cytosol and remains functional in supporting ClpXP-mediated degradation. Furthermore, the degradation rate of deGFP-ssrA increased with increasing concentrations of pT7-ClpP DNA, consistent with the expectation that higher ClpP expression levels would enhance proteolytic activity. Although this trend was evident, all tested conditions exhibited rapid degradation, with GFP fluorescence decreasing substantially within the first hour of the reaction.

::::{tip} Reaction Compositions Experiment 2 (1 DNA: ClpP)
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

:::{figure} ./general/Platereader/1DNA/1 DNA-ClpP.png
:name: fig:1 DNA-ClpP
:align: center
:width: 90%

GFP fluorescence signal in Nucleus Cytosol reactions incubated at 37 °C for 6 hours. The reaction contains pT7-ClpP DNA, purified ClpX protein and purified deGFP-ssrA protein. Data represent the mean of three replicate wells (n = 3), with shaded areas indicating SEM.
:::

Besides using ClpP DNA, we also tested ClpX DNA to express the ClpX protease in Nucleus Cytosol ({ref}`tbl-exp3`). When the reaction was supplemented with purified ClpP protein and purified deGFP-ssrA, we again observed the expected decrease in deGFP fluorescence over time. In contrast, the control reaction lacking ClpX DNA maintained constant fluorescence, aside from the minor initial drop consistently seen in earlier experiments {ref}`fig:1 DNA-ClpX`. 

::::{tip} Reaction Compositions: Experiment 3 (1 DNA: ClpX)
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

:::{figure} ./general/Platereader/1DNA/1 DNA-ClpX.png
:name: fig:1 DNA-ClpX
:align: center
:width: 90%

GFP fluorescence signal in Nucleus Cytosol reactions incubated at 37 °C for 6 hours. The reaction contains pT7-ClpX DNA, purified ClpP protein and purified deGFP-ssrA protein. Data represent the mean of three replicate wells (n = 3), with shaded areas indicating SEM.
:::

Next, we replaced purified deGFP-ssrA with pT7-deGFP-ssrA DNA to enable simultaneous protein expression and degradation ({ref}`tbl-exp4`). By varying the concentration of pT7-deGFP-ssrA DNA while keeping purified ClpX and ClpP constant, we observed an initial increase in GFP fluorescence due to *in vitro* protein expression, followed by a decrease as the newly synthesized GFP-ssrA was degraded by the ClpXP system {ref}`fig:deGFP-ssrA-2`.

Interestingly, after reaching a minimum, the GFP fluorescence gradually increased again under all tested conditions. This rebound suggests that GFP synthesis eventually outpaced GFP degradation, despite both processes competing for the same ATP and energy resources within the reaction. As expected, higher concentrations of pT7-deGFP-ssrA DNA resulted in higher minimum fluorescence levels, indicating that increased protein production partially offset ClpXP-mediated degradation.

A control reaction lacking ClpX and ClpP was also included for comparison. As expected, this control exhibited substantially higher GFP fluorescence, demonstrating that in the absence of the degradation machinery, the available energy resources were devoted entirely to GFP production rather than being shared between protein synthesis and proteolysis.

::::{tip} Reaction Compositions: Experiment 4 (1 DNA: GFP-ssrA)
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


:::::{tab-set}

::::{tab-item} deGFP-ssrA (w/ control) 
:sync: tab1-1
:::{figure} ./general/Platereader/1DNA/1 DNA-deGFP-ssrA-1.png
:label: fig:deGFP-ssrA-1
GFP expression using pT7-deGFP-ssrA DNA in Cytosol reactions incubated at 37 °C for 6 hours. Purified ClpX and ClpP proteins were added to the sample reactions. The control reaction (4.05 nM pT7-deGFP-ssrA only) doesn't contain purified proteins. Data represent the mean of three replicate wells (n = 3), with shaded areas indicating SEM.
:::
::::

::::{tab-item} deGFP-ssrA (w/o control)
:sync: tab1-2
:::{figure} ./general/Platereader/1DNA/1 DNA-deGFP-ssrA-2.png
:label: fig:deGFP-ssrA-2
GFP expression using pT7-deGFP-ssrA DNA in Cytosol reactions incubated at 37 °C for 6 hours. Purified ClpX and ClpP proteins were added to the reactions. Data represent the mean of three replicate wells (n = 3), with shaded areas indicating SEM.
:::
::::

:::::


## Two DNAs
To evaluate concurrent protein expression and degradation in the PURE system, we expanded the design to a dual-DNA configuration. Two setups were tested: (1) co-expression of pT7-deGFP-ssrA and pT7-ClpP with purified ClpX ({ref}`tbl-exp5`), and (2) co-expression of pT7-deGFP-ssrA and pT7-ClpX with purified ClpP ({ref}`tbl-exp6`).

In both cases, the GFP fluorescence exhibited a characteristic "rise-and-fall" profile. Following an initial increase due to deGFP-ssrA expression, the fluorescence rapidly declined as the ClpXP degradation machinery became active. The signal then reached a minimum and remained relatively stable, indicating that protein synthesis and degradation had approached a balance under the limited energy resources available in the cell-free system.

A notable difference between the two configurations was the peak fluorescence intensity. Reactions expressing ClpP {ref}`fig:2DNA-GFP_ClpP` reached substantially higher fluorescence levels than those expressing ClpX {ref}`fig:2DNA-GFP_ClpX`. This observation is likely due to the larger size and greater assembly requirements of ClpX, which place a higher burden on the transcription–translation machinery and compete more strongly with deGFP expression. In contrast, ClpP is smaller and easier to express, allowing greater accumulation of deGFP before degradation becomes dominant.

We also observed a slight fluorescence recovery after the minimum point in the ClpP-expression reactions {ref}`fig:2DNA-GFP_ClpP`, whereas this behavior was less pronounced in the ClpX-expression reactions {ref}`fig:2DNA-GFP_ClpX`. One possible explanation is that the presence of purified ClpX and residual endogenous ClpP in Nucleus Cytosol enables degradation to begin earlier and consume ATP more rapidly. Once the available energy becomes limiting, degradation slows while newly synthesized deGFP continues to mature into its fluorescent form, leading to the observed signal rebound.

::::{tip} Reaction Compositions: Experiment 5 (2 DNA: ClpP and deGFP-ssrA)
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

:::{figure} ./general/Platereader/2DNAs/2DNA-GFP_ClpP.png
:name: fig:2DNA-GFP_ClpP
:align: center
:width: 90%

GFP fluorescence signal in Cytosol reactions incubated at 37 °C for 6 hours. The reaction contains pT7-GFP-ssrA DNA, pT7-ClpX DNA, and purified ClpX protein. Data represent the mean of three replicate wells (n = 3), with shaded areas indicating SEM.
:::

::::{tip} Reaction Compositions: Experiment 6 (2 DNA: ClpX and deGFP-ssrA)
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
:::{figure} ./general/Platereader/2DNAs/2DNA-GFP_ClpX.png
:name: fig:2DNA-GFP_ClpX
:align: center
:width: 90%

GFP fluorescence signal in Cytosol reactions incubated at 37 °C for 6 hours. The reaction contains pT7-GFP-ssrA DNA, pT7-ClpX DNA, and purified ClpP protein. Data represent the mean of three replicate wells (n = 3), with shaded areas indicating SEM.
:::

Overall, these results demonstrate that the ClpXP degradation control module remains functional when key components are produced directly by Nucleus Cytosol from respective DNA templates. Both dual-DNA configurations successfully supported simultaneous protein expression and targeted degradation, confirming that the available transcriptional, translational, and energetic resources are sufficient to sustain the control module. The observed fluorescence dynamics further illustrate how the balance between protein synthesis, degradation, and energy consumption governs system behavior. 

## Three DNAs
Finally, we examined the simultaneous expression of three proteins within a single Cytosol reaction using three respective DNA constructs: pT7-ClpX, pT7-ClpP, and pT7-deGFP-ssrA ({ref}`tbl-exp7`). We progressively increased all the DNA concentrations and found that the fluorescence first increased strongly and then dropped quickly to a certain point, which indicates rapid GFP degradation, and then eventually reached steady state in all reactions. However, none of them can reach the initial fluorescence bottom line and final fluorescence levels are less than 50% of the peak fluorescence. As expected, the sample containing higher amount of DNA show higher fluorescence peak but lower GFP degradation percentages {ref}`fig:3DNA`. The results indicate alomst all of the energy is consumed in the first 1 hour and the total energy is not enough to degrade all GFP produced in Nucleus Cytosol. 

::::{tip} Reaction Compositions: Experiment 7 (3 DNA)
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

:::{figure} ./general/Platereader/3DNAs/3DNA.png
:name: fig:3DNA
:align: center
:width: 90%

GFP expression and degradation in Nucleus Cytosol reactions incubated at 37 °C for 6 hours. The reaction contains pT7-GFP-ssrA DNA, pT7-ClpX DNA, and pT7-ClpP DNA.
:::

Furthermore, we also repeated the exact same experiment but replacing Nucleus Cytosol with NEB PURExpress, for comparison. To compare the performance of the coupled synthesis–degradation circuit, we co-expressed pT7-deGFP-ssrA (0.68, 1.35, or 2.06 nM) with fixed amounts of pT7-ClpX and pT7-ClpP in Nucleus Cytosol {ref}`fig:3DNA` and NEB PURExpress {ref}`fig:3DNA-NEB`. Both systems showed the expected rise-and-fall fluorescence profile, with signals peaking within the first 45–60 minutes as GFP was produced and then degraded by ClpXP.

The main difference was expression capacity. Nucleus PURE reached much higher peak fluorescence (up to ~124,000 RFU) than NEB PURExpress (~65,000 RFU), indicating faster and stronger protein synthesis during the early phase of the reaction. The steeper initial rise in {ref}`fig:3DNA` suggests that deGFP accumulated more rapidly before the co-expressed ClpXP machinery became fully active.

The degradation phase, however, favored NEB PURExpress. In PURExpress reactions, fluorescence dropped to a low, nearly uniform baseline (~2,500–6,000 RFU), showing efficient and sustained degradation. In contrast, Nucleus Cytosol plateaued at much higher fluorescence levels (~23,000, 52,000, and 70,000 RFU, depending on reporter DNA concentration), indicating that degradation stopped before the accumulated deGFP was fully degraded.

:::{figure} ./general/Platereader/3DNAs/3DNA-NEB.png
:name: fig:3DNA-NEB
:align: center
:width: 90%

GFP expression and degradation in NEB PURExpress reactions incubated at 37 °C for 6 hours. The reaction contains pT7-GFP-ssrA DNA, pT7-ClpX DNA, and pT7-ClpP DNA. Data represent the mean of three replicate wells (n = 3), with shaded areas indicating SEM.
:::

Overall, these results show that Nucleus Cytosol provides substantially higher protein expression capacity, whereas NEB PURExpress supports more complete and sustained ClpXP-mediated degradation under the tested conditions. Importantly, both systems successfully supported the co-expression of deGFP-ssrA, ClpX, and ClpP from DNA templates, demonstrating that the ClpXP degradation control module can function perfectly in a multi-DNA setup.

# Future Works

In [previous DevNote](https://devnotes.nucleus.engineering/articles/bnext-devnotes-clpxp-pure-cells-01), we successfully demonstrated that the ClpXP-based control module functions effectively within the NEB PURExpress system in the confined environment of liposomes, establishing its robustness for protein degradation–based control in synthetic cells. Building on this foundation, the next step is to transition this module to synthetic cells encapsulating the Nucleus Cytosol system. This transition is important not only as a technical substitution, but also as an opportunity to directly compare how the two PURE systems perform under identical synthetic cell conditions. While we have already characterized and compared NEB PURExpress and Nucleus Cytosol in bulk reactions, their behavior in confined, cell-like environments remains unexplored and may reveal differences in expression efficiency, degradation dynamics, and system compatibility that are not apparent in bulk. Therefore, implementing the ClpXP control module in Nucleus Cytosol-based synthetic cells will enable a systematic, side-by-side evaluation of these two transcription–translation platforms in a more biologically relevant compartmentalized setting, helping to clarify their respective strengths and limitations for synthetic cell engineering.


