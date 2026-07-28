---
title: DNA toolkit - Aptamer reporter constructs for simultaneous transcription and translation monitoring in PURE
abstract: |
    Resolving the temporal relationship between transcription and translation in PURE cell-free 
    systems requires reporters capable of simultaneously detecting both events with high precision. 
    As part of the ongoing development of the DNA toolkit for PURE-based systems, here we present 
    the third installment of the collection — a characterisation of aptamer-based transcription 
    reporters for simultaneous monitoring of transcription and translation in PURE. We evaluate 
    three aptamer/fluorescent protein reporter pairs — MangoIV/TO1-Biotin, Broccoli/DFHBI-1T, 
    and MangoIV/TO3-Biotin — each paired with a downstream fluorescent protein reporter, across 
    multiple construct designs incorporating the RiboJ insulator and two aptamer scaffold variants. 
    We find that the F30-2xBroccoli/DFHBI-1T system is the optimal transcription reporter, 
    combining high signal-to-background ratio with highly reproducible lag time measurements. 
    Using this system paired with mScarlet, we measure a translation initiation delay of 
    ~30-39 minutes across all constructs in the PURE system.
---

# Background

The PURE (Protein synthesis Using Recombinant Elements) cell-free system offers a powerful 
platform for synthetic biology, enabling the precise reconstitution of gene expression from 
purified components. A key advantage of PURE over cell lysate-based systems is its minimal 
and well-defined composition, which reduces non-specific background and allows for greater 
experimental control. However, this same compositional complexity presents a challenge for 
real-time monitoring of gene expression — specifically, the ability to simultaneously track 
both transcription and translation in a single reaction.

Building upon the release of the T7 promoter and terminator collections, we continue the 
development of a DNA toolkit designed specifically for PURE cell-free expression systems. 
By offering a well-characterised and standardised set of DNA parts and analytical methods, 
this resource aims to streamline the development of PURE-based technologies and empower the 
community to establish design considerations tailored specifically to the PURE environment. 
With the first two installments of the toolkit addressing transcriptional initiation and 
termination respectively, we now turn our attention to the real-time monitoring of gene 
expression — an analytical capability that is increasingly important as the complexity of 
PURE-based systems grows.

Fluorescent protein reporters are well-established tools for monitoring translation in 
cell-free systems, but they provide no direct readout of transcription. RNA aptamers that 
activate small molecule fluorophores upon binding offer a complementary approach, enabling 
real-time transcription monitoring without the need for additional enzymatic steps or 
labelling. By pairing an aptamer-based transcription reporter with a fluorescent protein 
translation reporter in a single construct, it is in principle possible to resolve the 
temporal delay between transcription and translation onset in a single plate reader 
experiment. **Such measurements have been demonstrated in cell lysate-based systems, however 
the performance of aptamer reporters in the more defined PURE environment has not been 
systematically evaluated.**

Several RNA aptamer systems have been developed for this purpose, including the Mango and 
Broccoli families. **MangoIV binds TO1-Biotin or TO3-Biotin dyes with high affinity and 
has been used as a real-time transcription reporter in cell-free systems.** **Broccoli binds 
DFHBI-1T and has similarly been applied in cell-free contexts as a transcription reporter.** 
**Both aptamer families have been shown to fold co-transcriptionally, enabling near real-time 
detection of mRNA production.** However, their performance specifically within the PURE 
system — and their suitability for precise kinetic measurements of transcription onset — has 
not been systematically evaluated. Here we present the first comparative characterisation of 
these aptamer systems in PURE, with a focus on their ability to accurately and reproducibly 
report transcription onset timing, and their utility as analytical tools within the broader 
DNA toolkit framework.

# Reporter constructs

To evaluate the performance of each reporter system, we designed a series of dual-reporter 
constructs in which an RNA aptamer sequence was placed upstream of a fluorescent protein 
coding sequence both under the control of a T7 promoter. In this architecture, the aptamer 
reports on transcription whilst the downstream fluorescent protein serves as 
a readout of translation. Three reporter pairs were evaluated:

- **MangoIV/TO1-Biotin + mScarlet**: MangoIV aptamer sequences paired with the TO1-Biotin 
  fluorophore as the transcription reporter, and mScarlet as the translation reporter.
- **Broccoli/DFHBI-1T + mScarlet**: Broccoli aptamer sequences paired with DFHBI-1T as 
  the transcription reporter, and mScarlet as the translation reporter.
- **MangoIV/TO3-Biotin + deGFP**: MangoIV aptamer sequences paired with TO3-Biotin as 
  the transcription reporter, and deGFP as the translation reporter.

For each reporter pair, two aptamer scaffold variants were tested. For the MangoIV system 
these were F30MangoIV, in which the aptamer is embedded within an F30 scaffold to stabilise 
its structure, and tMangoIV, a truncated variant with **higher dye-binding affinity**. For 
the Broccoli system these were F30-2xBroccoli, in which two Broccoli aptamer sequences are 
embedded within an F30 scaffold, and tdBroccoli, a tandem dimer variant with **enhanced 
fluorescence output**.

Each scaffold variant was additionally tested with and without the RiboJ ribozyme insulator 
sequence inserted between the aptamer and the fluorescent protein coding sequence. **RiboJ 
self-cleaves the mRNA to generate a defined 5' end upstream of the ribosome binding site, 
insulating translation efficiency from upstream sequence context effects.** Its inclusion 
here was intended to assess whether standardising the translational context affected either 
the aptamer signal or the measured transcription-translation delay. This gave a total of 
four constructs per reporter pair: non-RiboJ and RiboJ versions of each scaffold variant. 
All constructs were expressed from a T7 promoter and contained identical UTR1 ribosome 
binding site sequences upstream of the fluorescent protein to ensure comparable translation 
efficiency across constructs.

## Cloning strategy

Constructs were assembled using a two-component HiFi assembly strategy. The fluorescent 
protein backbones — pOpen-deGFP-His6C and pET21a-mScarlet — were linearised by PCR to 
generate UTR1-[FP]-pT7 linear templates, providing the entry vector for each reporter pair. 
The eight aptamer insert fragments — comprising F30MangoIV, tMangoIV, F30-2xBroccoli and 
tdBroccoli, each in RiboJ and non-RiboJ variants — were synthesised by Ansa Biotechnologies 
and linearised by PCR to generate pT7-[apt]-RiboJ-UTR1 and pT7-[apt]-UTR1 templates 
respectively. All insert fragments were <300 bp, enabling identical PCR conditions across 
all variants. Assembly was facilitated by shared pT7 and UTR1 homology regions between 
the aptamer inserts and the fluorescent protein backbones. Correct assembly was confirmed 
by Sanger sequencing prior to use in reporter assays.


# Reporter testing

## Experimental setup

All reporter constructs were evaluated in triplicate using 10 µL PURExpress reactions 
containing plasmid DNA at a concentration of **X ng/µL**. Fluorescent dyes were 
supplemented at the following concentrations: **TO1-Biotin at X µM, TO3-Biotin at X µM, 
and DFHBI-1T at X µM**. Reactions were run for **X hours** at 37°C with 5 minute kinetic 
intervals in a BioTek Cytation 5 spectrophotometer. Excitation and emission parameters 
were optimised for each reporter prior to the experiment. The following parameters were 
used:

- **TO1-Biotin**: Ex/Em **X nm / X nm**
- **TO3-Biotin**: Ex/Em **X nm / X nm**
- **DFHBI-1T (GFP-Gext)**: Ex/Em **X nm / X nm**
- **mScarlet**: Ex/Em **569 nm / 594 nm**
- **deGFP**: Ex/Em **485 nm / 528 nm**

## Background subtraction

Prior to analysis, background subtraction was applied to all datasets by subtracting the 
mean signal of the negative control wells at each timepoint from all wells. This removes 
non-specific fluorescence contributions from PURE reaction components and free dye. **The 
importance of this step was highlighted during initial analysis of the MangoIV/TO1-Biotin 
dataset, where a transient fluorescence spike was observed at t=0 across all wells 
including the negative control. This spike was found to be an intrinsic property of 
TO1-Biotin in the PURE reaction mixture, most likely arising from non-specific 
interactions between the free dye and PURE components before equilibration. Background 
subtraction effectively removed this artefact and, critically, transformed the F30MangoIV 
TO1-Biotin lag time CV% from ~51% to ~3%, demonstrating its importance for reliable 
kinetic analysis. For the Broccoli/DFHBI-1T dataset, background subtraction had a 
negligible effect on signal trends as expected, given the consistently low negative 
control signal for this dye.**

## Timecourse data

The full timecourse plots show the mean fluorescence across three replicate wells with 
shaded regions indicating 95% confidence interval for each construct, plotted separately 
for the aptamer and fluorescent protein reporters.

:::::{tab-set}

::::{tab-item} Broccoli/DFHBI-1T + mScarlet
:::{figure} ./experiments/20251027_Aptamer_test_Broccoli_mScarlet/figures/Broccoli_mScarlet_full_timecourse.png
:label: fig:broccoli_full_timecourse
:align: center
Full timecourse of DFHBI-1T (transcription) and mScarlet (translation) signals for all 
pT7-F30-2xBroccoli/tdBroccoli-{RiboJ}-UTR1-mScarlet constructs. Each trace represents 
the mean across three replicate wells with shaded regions indicating 95% confidence 
interval.
:::
::::

::::{tab-item} MangoIV/TO1-Biotin + mScarlet
:::{figure} ./experiments/20251030_Aptamer_test_Mango_mScarlet/figures/MangoIV_mScarlet_full_timecourse.png
:label: fig:mango_full_timecourse
:align: center
Full timecourse of TO1-Biotin (transcription) and mScarlet (translation) signals for all 
pT7-F30MangoIV/tMangoIV-{RiboJ}-UTR1-mScarlet constructs. Each trace represents the 
mean across three replicate wells with shaded regions indicating 95% confidence interval.
:::
::::

::::{tab-item} MangoIV/TO3-Biotin + deGFP
:::{figure} ./experiments/20251031_Aptamer_test_Mango_deGFP/figures/deGFP_full_timecourse.png
:label: fig:degfp_full_timecourse
:align: center
Full timecourse of TO3-Biotin (transcription) and deGFP (translation) signals for all 
pT7-F30MangoIV/tMangoIV-{RiboJ}-UTR1-deGFP constructs. Each trace represents the mean 
across three replicate wells with shaded regions indicating 95% confidence interval.
:::
::::

:::::

## First hour

To visualise the early onset of transcription and translation, we next examine the 
first hour of each reaction. Each trace represents the mean across three replicate 
wells with shaded regions indicating 95% confidence interval, split by aptamer variant 
to allow direct comparison of RiboJ and non-RiboJ constructs.

:::::{tab-set}

::::{tab-item} Broccoli/DFHBI-1T + mScarlet
:::{figure} ./experiments/20251027_Aptamer_test_Broccoli_mScarlet/figures/Broccoli_mScarlet_first_hour.png
:label: fig:broccoli_first_hour
:align: center
First hour of DFHBI-1T (transcription) and mScarlet (translation) signals for all 
pT7-F30-2xBroccoli/tdBroccoli-{RiboJ}-UTR1-mScarlet constructs following background 
subtraction.
:::

- It is clear that transcription begins earlier than translation for both Broccoli 
  variants.
- In both cases the RiboJ construct generates a weaker aptamer signal, however this 
  difference is less pronounced for the tdBroccoli variant.
- A clear lag phase is visible for both the aptamer and mScarlet reporters with high 
  signal-to-noise ratios.
::::

::::{tab-item} MangoIV/TO1-Biotin + mScarlet (pre background subtraction)
:::{figure} ./experiments/20251030_Aptamer_test_Mango_mScarlet/figures/MangoTO1_mScarlet_first_hour.png
:label: fig:mango_first_hour_raw
:align: center
First hour of TO1-Biotin (transcription) and mScarlet (translation) signals for all 
pT7-F30MangoIV/tMangoIV-{RiboJ}-UTR1-mScarlet constructs prior to background 
subtraction. A transient fluorescence spike is visible at t=0 in the TO1-Biotin signal 
across all constructs including the negative control, confirming this is a systematic 
dye artefact.
:::
::::

::::{tab-item} MangoIV/TO1-Biotin + mScarlet (background subtracted)
:::{figure} ./experiments/20251030_Aptamer_test_Mango_mScarlet/figures/MangoIV_mScarlet_first_hour.png
:label: fig:mango_first_hour_bgsub
:align: center
First hour of TO1-Biotin (transcription) and mScarlet (translation) signals for all 
pT7-F30MangoIV/tMangoIV-{RiboJ}-UTR1-mScarlet constructs following background 
subtraction. The initial TO1-Biotin spike is removed, revealing a cleaner signal 
baseline.
:::

- Background subtraction removes the initial TO1-Biotin spike with negligible impact 
  on the mScarlet signal.
- F30MangoIV constructs show a clear lag phase in both reporters following background 
  subtraction.
- tMangoIV constructs show no discernible lag phase in the TO1-Biotin signal, 
  suggesting near-instantaneous transcription onset.
::::

::::{tab-item} MangoIV/TO3-Biotin + deGFP (background subtracted)
:::{figure} ./experiments/20251031_Aptamer_test_Mango_deGFP/figures/20251031_TO3Biotin_deGFP-Background_sbtrkt_first_hour_plot.png
:label: fig:degfp_first_hour_bgsub
:align: center
First hour of TO3-Biotin (transcription) and deGFP (translation) signals for all 
pT7-F30MangoIV/tMangoIV-{RiboJ}-UTR1-deGFP constructs following background subtraction.
:::

- Despite background subtraction removing the initial TO3-Biotin spike, no clear lag 
  phase is visible in the TO3-Biotin signal across any construct.
- Replicate variability is high and the signal barely exceeds the noise floor, 
  indicating that TO3-Biotin is not a suitable transcription reporter in this system.
- The deGFP signal is clean and detectable, however without a reliable transcription 
  reporter this construct cannot be used to resolve transcription-translation delay.
- A notable observation is the substantially higher deGFP signal in the RiboJ variants 
  compared to the non-RiboJ variants, which warrants further investigation.
- This reporter pair was not pursued further.
::::

:::::

## Kinetic analysis

Sigmoid drift curves are fitted and visualised per construct using `pr.plot_kinetics`, 
grouped by name and read type. We visually confirm that the sigmoid model accurately 
describes the data before proceeding to quantitative extraction of lag times.

:::::{tab-set}

::::{tab-item} Broccoli/DFHBI-1T
:::{figure} ./experiments/20251027_Aptamer_test_Broccoli_mScarlet/figures/Broccoli_DFHBI-1T_kinetics.png
:label: fig:broccoli_dfhbi_kinetics
:align: center
Sigmoid drift fits to the DFHBI-1T transcription signal for all 
pT7-F30-2xBroccoli/tdBroccoli-{RiboJ}-UTR1-mScarlet constructs.
:::
::::

::::{tab-item} Broccoli/mScarlet
:::{figure} ./experiments/20251027_Aptamer_test_Broccoli_mScarlet/figures/Broccoli_mScarlet_kinetics.png
:label: fig:broccoli_mscarlet_kinetics
:align: center
Sigmoid drift fits to the mScarlet translation signal for all 
pT7-F30-2xBroccoli/tdBroccoli-{RiboJ}-UTR1-mScarlet constructs.
:::

- Sigmoidal curves are well fitted to all constructs for both reporters.
- All constructs have detectable lag times, clearly showing that transcription onset 
  precedes translation onset.
::::

::::{tab-item} MangoIV/TO1-Biotin
:::{figure} ./experiments/20251030_Aptamer_test_Mango_mScarlet/figures/MangoIV_TO1_kinetics.png
:label: fig:mango_to1_kinetics
:align: center
Sigmoid drift fits to the TO1-Biotin transcription signal for all 
pT7-F30MangoIV/tMangoIV-{RiboJ}-UTR1-mScarlet constructs following background 
subtraction.
:::
::::

::::{tab-item} MangoIV/mScarlet
:::{figure} ./experiments/20251030_Aptamer_test_Mango_mScarlet/figures/MangoIV_mScarlet_kinetics.png
:label: fig:mango_mscarlet_kinetics
:align: center
Sigmoid drift fits to the mScarlet translation signal for all 
pT7-F30MangoIV/tMangoIV-{RiboJ}-UTR1-mScarlet constructs.
:::

- Sigmoidal curves are well fitted to all constructs for both reporters.
- F30MangoIV constructs show lag times of ~23 min for TO1-Biotin, consistent with 
  the Broccoli transcription lag times.
- tMangoIV constructs show near-zero or negative lag times for TO1-Biotin, indicating 
  immediate transcription onset. The question of whether this reflects a genuine 
  biological difference or a fundamental property of the tMangoIV aptamer is discussed 
  further in the quantification metrics section.
::::

:::::

The Broccoli/DFHBI-1T and MangoIV/TO1-Biotin systems both successfully resolve 
transcription and translation onset after background subtraction. mScarlet lag times 
are consistent across both experiments (~47-54 min), confirming reliable and comparable 
translation detection regardless of aptamer system. Transcription lag times of ~22-23 
min are measured for F30MangoIV and ~16-23 min for Broccoli constructs, suggesting both 
systems detect transcription onset at similar times. tMangoIV constructs show 
near-instantaneous transcription onset (~0-2 min) indicating immediate transcription 
initiation, however this precludes calculation of a meaningful translation initiation 
delay. For constructs with a detectable transcription lag, the translation initiation 
delay is ~24-25 min for F30MangoIV and ~30-39 min for Broccoli, with F30-2xBroccoli-RiboJ 
showing a notably longer delay (~39 min) compared to all other constructs.

## Transcription/translation lag times and translation initiation delay

Lag times are extracted per replicate well individually and plotted side by side for 
the aptamer and fluorescent protein reporters per construct, with error bars representing 
standard deviation across three replicate wells. The translation initiation delay is 
calculated as the difference between the mScarlet lag time and the aptamer lag time 
for each construct.

:::::{tab-set}

::::{tab-item} Broccoli/DFHBI-1T + mScarlet — lag times
:::{figure} ./experiments/20251027_Aptamer_test_Broccoli_mScarlet/figures/Broccoli_mScarlet_Transcription_translation_lag_times.png
:label: fig:broccoli_lag_times
:align: center
Transcription (DFHBI-1T) and translation (mScarlet) lag times for all 
pT7-F30-2xBroccoli/tdBroccoli-{RiboJ}-UTR1-mScarlet constructs. Error bars represent 
standard deviation across three replicate wells.
:::

- Transcription (DFHBI-1T) lag times range from ~16-23 min across all constructs, 
  with F30-2xBroccoli-RiboJ showing the earliest onset.
- Translation (mScarlet) lag times are consistently ~50-54 min across all constructs.
- The gap between transcription and translation bars is visually clear and consistent, 
  demonstrating reliable resolution of the two events.
- Error bars are tight for all constructs except tdBroccoli which shows slightly more 
  variability.
::::

::::{tab-item} Broccoli/DFHBI-1T + mScarlet — translation initiation delay
:::{figure} ./experiments/20251027_Aptamer_test_Broccoli_mScarlet/figures/Broccoli_mScarlet_Translation_initiation_delay.png
:label: fig:broccoli_delay
:align: center
Translation initiation delay for all pT7-F30-2xBroccoli/tdBroccoli-{RiboJ}-UTR1-mScarlet 
constructs, calculated as the difference between the mScarlet and DFHBI-1T lag times. 
Error bars represent propagated standard deviation.
:::

- The delay between transcription and translation onset is ~30-39 min across all 
  constructs.
- F30-2xBroccoli-RiboJ shows a notably longer delay (~39 min) compared to the other 
  three constructs (~30 min).
- Three of four constructs show very consistent delays (~30 min) with tight error bars.
- The longer delay for F30-2xBroccoli-RiboJ may reflect altered translation initiation 
  kinetics due to the RiboJ insulator creating a different mRNA structural context.
::::

::::{tab-item} MangoIV/TO1-Biotin + mScarlet — lag times
:::{figure} ./experiments/20251030_Aptamer_test_Mango_mScarlet/figures/MangoIV_mScarlet_Transcription_translation_lag_times.png
:label: fig:mango_lag_times
:align: center
Transcription (TO1-Biotin) and translation (mScarlet) lag times for all 
pT7-F30MangoIV/tMangoIV-{RiboJ}-UTR1-mScarlet constructs following background 
subtraction. Error bars represent standard deviation across three replicate wells.
:::

- F30MangoIV constructs show consistent transcription (TO1-Biotin) lag times of ~23 
  min with tight error bars after background subtraction.
- tMangoIV-RiboJ shows no detectable transcription lag while tMangoIV shows a very 
  short lag (~2 min).
- Translation (mScarlet) lag times are consistent across all constructs at ~47-51 min, 
  comparable to the Broccoli mScarlet values.
::::

::::{tab-item} MangoIV/TO1-Biotin + mScarlet — translation initiation delay
:::{figure} ./experiments/20251030_Aptamer_test_Mango_mScarlet/figures/MangoIV_mScarlet_Translation_initiation_delay.png
:label: fig:mango_delay
:align: center
Translation initiation delay for all pT7-F30MangoIV/tMangoIV-{RiboJ}-UTR1-mScarlet 
constructs, calculated as the difference between the mScarlet and TO1-Biotin lag times. 
Error bars represent propagated standard deviation. Note that tMangoIV construct delays 
are not reported as true transcription-translation delays as the TO1-Biotin lag is 
effectively 0.
:::

- The delay between transcription and translation onset is ~24-25 min for F30MangoIV 
  constructs, with tight error bars indicating reliable measurements.
- tMangoIV constructs show artificially inflated delays (~48-51 min) since their 
  TO1-Biotin lag is effectively 0 and are therefore excluded from interpretation.
- The near-identical delays for F30MangoIV and F30MangoIV-RiboJ (~24-25 min) suggest 
  RiboJ has no significant effect on translation initiation timing for this aptamer 
  variant.
::::

:::::

# Quantification metrics

Moving on from the kinetic analysis, we now extract a set of quantitative metrics to 
assess the performance of each reporter combination. To accurately resolve transcription 
and translation, each reporter must reliably detect the onset of its respective event 
with a high signal to noise ratio. The key metrics are defined as follows:

- **SNR** (signal-to-noise ratio): the fitted steady-state signal divided by the noise 
  floor of the negative control after background subtraction. Higher values indicate a 
  cleaner signal above background noise.
- **R²**: goodness-of-fit of the sigmoid model to the timecourse data. Values close to 
  1.0 confirm the sigmoid accurately describes the kinetics and that lag time extraction 
  is reliable.
- **Lag mean**: the mean fitted lag time across replicate wells.
- **Lag std**: the standard deviation of lag times across replicate wells.
- **Lag CV%**: lag std / lag mean × 100. This is the key discriminator of reporter 
  quality — a low CV% indicates the timing measurement is both precise and reproducible 
  across replicates.
- **Signal stability**: ratio of end-of-experiment signal to peak signal. Values close 
  to 1.0 confirm the reporter signal is stable throughout the experiment duration.

These metrics are summarised in the tables below for each construct and reporter 
combination across both experiments.

:::::{tab-set}

::::{tab-item} Broccoli/DFHBI-1T + mScarlet

| Construct | Read | Lag detectable | SNR | R² | Lag mean (min) | Lag std (min) | Lag CV (%) | Signal stability |
|---|---|---|---|---|---|---|---|---|
| F30-2xBroccoli-RiboJ | DFHBI-1T | Yes | 1793.70 | 1.00 | 15.70 | 1.10 | 7.00 | 1.00 |
| F30-2xBroccoli-RiboJ | mScarlet | Yes | 207314.57 | 1.00 | 54.50 | 0.60 | 1.10 | 0.99 |
| F30-2xBroccoli | DFHBI-1T | Yes | 2008.57 | 0.99 | 22.90 | 0.20 | 0.90 | 0.93 |
| F30-2xBroccoli | mScarlet | Yes | 172219.34 | 1.00 | 53.90 | 1.10 | 2.00 | 0.98 |
| tdBroccoli-RiboJ | DFHBI-1T | Yes | 1561.18 | 0.99 | 23.40 | 2.30 | 9.80 | 0.88 |
| tdBroccoli-RiboJ | mScarlet | Yes | 203253.88 | 1.00 | 53.40 | 0.40 | 0.70 | 0.96 |
| tdBroccoli | DFHBI-1T | Yes | 1510.50 | 0.99 | 20.80 | 2.40 | 11.50 | 0.86 |
| tdBroccoli | mScarlet | Yes | 168963.24 | 1.00 | 50.50 | 0.60 | 1.20 | 0.98 |

All four constructs show excellent sigmoid fits (R² ≥ 0.99) with detectable lag phases 
for both reporters. DFHBI-1T SNR is consistently high (~1500-2000) and mScarlet SNR is 
very high (~170,000-210,000). F30-2xBroccoli has the lowest lag CV% (0.9%) making it 
the most precise transcription reporter, while tdBroccoli constructs show higher 
variability (9.8-11.5%). Whilst the lag CV% for the tdBroccoli constructs is higher than 
for F30-2xBroccoli, the absolute spread in lag times between replicates remains small 
(~2-3 min), and the translation initiation delays calculated from these constructs 
(~30 min) are consistent with those of F30-2xBroccoli (~30 min), suggesting the 
measurements remain biologically meaningful despite the elevated CV%. Signal stability 
is slightly reduced for tdBroccoli constructs (0.86-0.88) suggesting mild signal decay 
towards the end of the experiment.

To investigate the source of variability in the tdBroccoli constructs, we examine the 
per-well kinetic fits below. The overall spread of lag times is small, with the elevated 
CV% most likely driven by a single earlier measurement in well H for both constructs 
(18.0 min for tdBroccoli, 20.7 min for tdBroccoli-RiboJ).

:::{figure} ./experiments/20251027_Aptamer_test_Broccoli_mScarlet/figures/Broccoli_mScarlet_per_well_kinetics.png
:label: fig:broccoli_per_well_kinetics
:align: center
Per-well sigmoid fits to the DFHBI-1T transcription signal for tdBroccoli and 
tdBroccoli-RiboJ constructs. Individual well lag times are annotated on each plot.
:::
::::

::::{tab-item} MangoIV/TO1-Biotin + mScarlet

| Construct | Read | Lag detectable | SNR | R² | Lag mean (min) | Lag std (min) | Lag CV (%) | Signal stability |
|---|---|---|---|---|---|---|---|---|
| F30MangoIV-RiboJ | TO1-Biotin | Yes | 166.10 | 1.00 | 23.10 | 0.80 | 3.50 | 0.94 |
| F30MangoIV-RiboJ | mScarlet | Yes | 64876.97 | 1.00 | 47.40 | 0.50 | 1.10 | 1.02 |
| F30MangoIV | TO1-Biotin | Yes | 106.38 | 0.99 | 23.40 | 0.70 | 3.00 | 0.95 |
| F30MangoIV | mScarlet | Yes | 45477.55 | 1.00 | 48.40 | 0.60 | 1.20 | 0.98 |
| tMangoIV-RiboJ | TO1-Biotin | No† | 275.25 | 1.00 | 0.00 | 0.00 | N/A | 1.03 |
| tMangoIV-RiboJ | mScarlet | Yes | 41024.22 | 1.00 | 50.60 | 0.60 | 1.20 | 1.01 |
| tMangoIV | TO1-Biotin | Yes* | 287.69 | 0.99 | 2.00 | 0.60 | 30.00 | 0.98 |
| tMangoIV | mScarlet | Yes | 61681.59 | 1.00 | 49.70 | 1.00 | 2.00 | 0.97 |

*\* tMangoIV TO1-Biotin lag detectable at ~2 min after background subtraction but with 
high CV (30%) — interpret with caution. Note that the high CV% is likely inflated due 
to the very short lag time; the absolute lag std of 0.6 min is equivalent to that of 
the reliable F30MangoIV constructs.*

*† tMangoIV-RiboJ TO1-Biotin: no lag phase detectable. Construct label swap suspected 
— repeat experiment pending.*

F30MangoIV constructs perform well after background subtraction, with consistent lag 
times of ~23 min and low CV% (~3%) for both constructs. SNR for TO1-Biotin is lower 
than DFHBI-1T (~106-166 vs ~1500-2000) but sufficient for reliable lag time extraction. 
tMangoIV-RiboJ shows no detectable transcription lag and is excluded from timing 
analysis pending confirmation of a suspected label swap. tMangoIV shows a very short 
lag (~2 min) with high CV% (30%), indicating near-instantaneous transcription onset. 
Whilst this high CV% may suggest unreliable timing measurements, it is important to 
note that it is most likely inflated due to the very short lag time — the absolute lag 
std of 0.6 min is equivalent to that of the reliable F30MangoIV constructs. mScarlet 
performance is consistent across all MangoIV constructs (CV% 1.1-2.0%, R² 1.00) and 
comparable to the Broccoli experiment, confirming reliable translation detection 
independent of the aptamer system used.

The per-well kinetics of the tMangoIV TO1-Biotin signal are shown below. The absence 
of a defined lag time in the tMangoIV-RiboJ constructs is clearly visible, and whilst 
a positive lag time is present in the non-RiboJ variant, the very short duration makes 
confident interpretation challenging. In theory, if this data were reliable, tMangoIV 
could provide the most accurate measurement of transcription onset given its high 
sensitivity to mRNA presence. However, given the inconsistency with Broccoli 
measurements and the requirement for background subtraction to remove the initial 
TO1-Biotin peak, further evaluation is needed before tMangoIV can be recommended as 
a transcription reporter in PURE.

:::{figure} ./experiments/20251030_Aptamer_test_Mango_mScarlet/figures/MangoIV_mScarlet_per_well_kinetics.png
:label: fig:mango_per_well_kinetics
:align: center
Per-well sigmoid fits to the TO1-Biotin transcription signal for tMangoIV and 
tMangoIV-RiboJ constructs following background subtraction. Individual well lag times 
are annotated on each plot.
:::
::::

:::::

# Overall evaluation

Having assessed the performance of each reporter combination individually, we now bring 
together the key metrics across both experiments into a single summary figure. The figure 
comprises three panels: (i) SNR plotted against lag CV% for all transcription reporters, 
providing a direct visual comparison of signal quality and timing precision; (ii) lag CV% 
as a bar plot across all constructs, allowing direct comparison of reporter precision; 
and (iii) the translation initiation delay for all constructs with a detectable 
transcription lag, representing the key biological output of this analysis. Together 
these panels summarise the reporter evaluation and contextualise the biological findings 
within the constraints of each reporter system.

:::{figure} ./experiments/20260511_combined_analysis/figures/summary_figure.png
:label: fig:summary_figure
:align: center
Summary figure comparing transcription reporter quality across both aptamer systems and 
presenting the translation initiation delay. Panel (i) SNR vs lag CV% scatter for all 
transcription reporters. Panel (ii) lag CV% bar plot across all constructs grouped by 
reporter type. Panel (iii) translation initiation delay for all constructs with a 
detectable transcription lag, with MangoIV constructs shown as hatched bars and Broccoli 
constructs as solid bars.
:::

Both TO1-Biotin (MangoIV) and DFHBI-1T (Broccoli) transcription reporters achieve 
comparable lag CV% values for their F30 scaffold constructs (~3% and ~1% respectively), 
confirming that after background subtraction both systems are capable of reliably 
resolving transcription onset. F30-2xBroccoli remains the highest performing reporter 
overall, combining the lowest lag CV% with the highest SNR (~1500). The tdBroccoli 
constructs show higher lag CV% (9.8-11.5%) despite adequate SNR, however it is important 
to note that the absolute spread in lag times between replicates remains small (~2-3 min), 
and the translation initiation delays calculated from these constructs (~30 min) are 
consistent with those of F30-2xBroccoli (~30 min), suggesting the measurements remain 
biologically meaningful despite the elevated CV%. The MangoIV TO1-Biotin reporters have 
notably lower SNR (~100-170) compared to DFHBI-1T (~1500-2000), however this does not 
appear to compromise lag time precision for the F30 constructs.

For constructs with a reliable transcription lag, the translation initiation delay is 
~24-25 min for F30MangoIV constructs and ~30-39 min for Broccoli constructs. The 
consistently shorter delay measured by MangoIV (~24-25 min) compared to Broccoli 
(~30 min for most constructs) may reflect a detection lag inherent to the 
DFHBI-1T/Broccoli system, whereby the aptamer requires additional time to fold and 
accumulate sufficient fluorescent signal above the noise floor. F30-2xBroccoli-RiboJ 
is a notable outlier with a delay of ~39 min, which may reflect altered translation 
initiation kinetics due to RiboJ-mediated mRNA restructuring.

# Conclusions and future directions

We have presented the first comparative characterisation of RNA aptamer-based 
transcription reporters in the PURE cell-free system, evaluating the MangoIV/TO1-Biotin, 
Broccoli/DFHBI-1T, and MangoIV/TO3-Biotin systems across multiple construct designs. 
Of the three reporter pairs evaluated, MangoIV/TO3-Biotin was found to be unsuitable 
for use in PURE, with TO3-Biotin signal indistinguishable from background noise across 
all constructs. MangoIV/TO1-Biotin and Broccoli/DFHBI-1T both successfully resolved 
transcription and translation onset, however they differ in several key respects.

Broccoli/DFHBI-1T demonstrates superior signal quality, with DFHBI-1T SNR 
approximately 10-fold higher than TO1-Biotin (~1500-2000 vs ~100-170). Critically, 
DFHBI-1T does not exhibit the non-specific fluorescence spike observed for TO1-Biotin 
in PURE, making it more straightforward to use without the requirement for background 
subtraction. Of the Broccoli constructs evaluated, **F30-2xBroccoli/DFHBI-1T paired 
with mScarlet is recommended as the optimal reporter system** for simultaneous 
transcription and translation monitoring in PURE, combining the highest SNR with the 
lowest lag CV% (0.9%) across all constructs tested.

Using the F30-2xBroccoli/DFHBI-1T + mScarlet system, we measure a translation 
initiation delay of ~30-31 min in PURE. This value is consistent across three of the 
four Broccoli constructs, with F30-2xBroccoli-RiboJ showing a notably longer delay 
(~39 min) that may reflect altered translation initiation kinetics due to RiboJ-mediated 
mRNA restructuring. **This translation initiation delay is broadly consistent with 
previously reported values for cell-free expression systems**, though direct comparison 
is complicated by differences in fluorescent protein maturation times and system 
composition between studies.

MangoIV/TO1-Biotin represents an interesting alternative that warrants further 
investigation. After background subtraction, F30MangoIV TO1-Biotin achieves lag CV% 
values (~3%) comparable to those of F30-2xBroccoli, suggesting it is a viable 
transcription reporter when background subtraction is applied. The tMangoIV variant 
in particular raises an intriguing question — its near-instantaneous transcription onset 
(~0-2 min) may reflect a fundamentally higher sensitivity to mRNA presence, potentially 
providing a more accurate readout of true transcription onset than aptamers that require 
a longer accumulation time to generate detectable signal. However, given the requirement 
for background subtraction to remove the TO1-Biotin artefact, and the inconsistency 
between tMangoIV and Broccoli transcription lag times, further evaluation is required 
before tMangoIV can be recommended as a transcription reporter in PURE.

Several directions for future work are highlighted:

- **Confirmation of tMangoIV-RiboJ label swap** — a repeat experiment is pending to 
  confirm whether the tMangoIV and tMangoIV-RiboJ templates were swapped during 
  construct preparation. This is critical before any conclusions can be drawn about 
  the effect of RiboJ on tMangoIV performance.
- **Further evaluation of tMangoIV** — given the potential sensitivity advantage of 
  tMangoIV as a transcription reporter, a dedicated experiment using optimised TO1-Biotin 
  concentrations and reaction conditions would help clarify whether its near-instantaneous 
  signal onset reflects genuine transcription detection or a system artefact.
- **Decoupling aptamer detection lag from biological lag** — the difference in 
  translation initiation delay between MangoIV (~24-25 min) and Broccoli (~30 min) 
  constructs suggests that a portion of the measured delay may reflect aptamer folding 
  and dye-binding kinetics rather than true transcription-translation delay. Future 
  experiments using orthogonal approaches **such as RT-qPCR or single-molecule 
  fluorescence** could help decouple these contributions.
- **Application to DNA toolkit characterisation** — the F30-2xBroccoli/DFHBI-1T + 
  mScarlet system is now available as an analytical tool for the characterisation of 
  DNA parts in PURE. Future DevNotes will apply this system to characterise the 
  transcription and translation kinetics of promoter, terminator, and RBS variants 
  within the DNA toolkit collection.

