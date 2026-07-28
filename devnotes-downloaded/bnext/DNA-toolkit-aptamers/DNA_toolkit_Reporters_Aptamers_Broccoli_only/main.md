---
title: DNA toolkit - Aptamer reporter systems for simultaneous transcription and translation monitoring in PURE
abstract: |
   The development of modular PURE-based systems depends on a well-characterised repertoire of genetic components. Building on our previous releases of the T7 promoter and terminator collections, here we address the simultaneous resolution of transcription and translation dynamics. We characterise the Broccoli/DFHBI-1T RNA aptamer system paired with mScarlet as a dual reporter for simultaneous transcription and translation monitoring in PURE. Four constructs were evaluated: F30-2xBroccoli and tdBroccoli, each in RiboJ and non-RiboJ backgrounds. Sigmoid-based kinetic analysis was used to extract transcription and translation lag times and assess reporter reproducibility across replicates. F30-2xBroccoli/DFHBI-1T paired with mScarlet was identified as the optimal reporter combination. Using this system we measure a translation initiation delay of approximately 30 minutes in the PURE cell-free environment.
---

# Background

Building upon the release of the T7 promoter and terminator collections, we continue the development of a DNA toolkit designed specifically for PURE cell-free expression systems. By offering a well-characterised and standardised set of DNA parts, this resource aims to streamline the development of PURE-based technologies and empower the community to establish design considerations tailored specifically to the PURE environment. With the first two installments of the toolkit addressing transcriptional initiation and termination respectively, we now turn our attention to the simultaneous resolution of transcription and translation dynamics.

RNA aptamers and fluorescent proteins provide a complementary approach to simultaneously assessing transcription and translation in cell-free systems, and this dual-reporter strategy has been demonstrated using a variety of aptamer constructs across different cell-free environments.[refs] Here we apply this strategy using Broccoli/DFHBI-1T paired with mScarlet in PURE, evaluating two aptamer variants, F30-2xBroccoli and tdBroccoli, each in RiboJ and non-RiboJ construct backgrounds. Kinetic analysis was performed using the Nucleus CDK to extract transcription and translation lag times across constructs and provide the community with reference measurements of the delay between transcription and translation initiation in PURE.
# Reporter constructs

To evaluate the performance of the Broccoli/DFHBI-1T reporter system, we designed a 
series of dual-reporter constructs in which a Broccoli aptamer sequence was placed 
upstream of an mScarlet coding sequence under the control of a T7 promoter. In this 
architecture, the aptamer reports on transcription in real time whilst mScarlet serves 
as a readout of translation.

Two aptamer scaffold variants were tested: F30-2xBroccoli, in which two Broccoli aptamer 
sequences are embedded within an F30 scaffold, and tdBroccoli, a tandem dimer variant 
with **enhanced fluorescence output**. Each scaffold variant was additionally tested with 
and without the RiboJ ribozyme insulator sequence inserted between the aptamer and the 
mScarlet coding sequence. **RiboJ self-cleaves the mRNA to generate a defined 5' end 
upstream of the ribosome binding site, insulating translation efficiency from upstream 
sequence context effects.** Its inclusion here was intended to assess whether standardising 
the translational context affected either the aptamer signal or the measured 
transcription-translation delay. This gave a total of four constructs: non-RiboJ and RiboJ 
versions of each scaffold variant. All constructs were expressed from a T7 promoter and 
contained identical UTR1 ribosome binding site sequences upstream of mScarlet to ensure 
comparable translation efficiency across constructs.

## Cloning strategy

Constructs were assembled using a two-component HiFi assembly strategy. The mScarlet 
backbone — pET21a-mScarlet — was linearised by PCR to generate a UTR1-mScarlet-pT7 
linear template, providing the entry vector. The four aptamer insert fragments — comprising 
F30-2xBroccoli and tdBroccoli, each in RiboJ and non-RiboJ variants — were synthesised 
by Ansa Biotechnologies and linearised by PCR to generate pT7-[apt]-RiboJ-UTR1 and 
pT7-[apt]-UTR1 templates respectively. All insert fragments were <300 bp, enabling 
identical PCR conditions across all variants. Assembly was facilitated by shared pT7 and 
UTR1 homology regions between the aptamer inserts and the mScarlet backbone. Correct 
assembly was confirmed by Sanger sequencing prior to use in reporter assays.

# Reporter testing

## Experimental setup

All reporter constructs were evaluated in triplicate using 10 µL PURExpress reactions 
containing linear DNA at a concentration of **X ng/µL**. DFHBI-1T was supplemented at 
a final concentration of **X µM**. Reactions were run for **X hours** at 37°C with 5 
minute kinetic intervals in a BioTek Cytation 5 spectrophotometer. Excitation and emission 
parameters were optimised for each reporter prior to the experiment. The following 
parameters were used:

- **DFHBI-1T (GFP-Gext)**: Ex/Em **X nm / X nm**
- **mScarlet**: Ex/Em **569 nm / 594 nm**

## Background subtraction

Prior to analysis, background subtraction was applied to the dataset by subtracting the 
mean signal of the negative control wells at each timepoint from all wells. This removes 
non-specific fluorescence contributions from PURE reaction components and free dye. For 
the Broccoli/DFHBI-1T system, background subtraction had a negligible effect on signal 
trends, consistent with DFHBI-1T being essentially non-fluorescent in its unbound state 
and the negative control signal remaining consistently low throughout the experiment.

## Timecourse data

The full timecourse plots show the mean fluorescence across three replicate wells with 
shaded regions indicating 95% confidence interval for each construct, plotted separately 
for the DFHBI-1T aptamer and mScarlet reporters.

:::{figure} ./experiments/20251027_Aptamer_test_Broccoli_mScarlet/figures/Broccoli_mScarlet_full_timecourse.png
:label: fig:broccoli_full_timecourse
:align: center
Full timecourse of DFHBI-1T (transcription) and mScarlet (translation) signals for all 
pT7-F30-2xBroccoli/tdBroccoli-{RiboJ}-UTR1-mScarlet constructs. Each trace represents 
the mean across three replicate wells with shaded regions indicating 95% confidence 
interval.
:::

## First hour

To visualise the early onset of transcription and translation, we next examine the first 
hour of each reaction. Each trace represents the mean across three replicate wells with 
shaded regions indicating 95% confidence interval, split by aptamer variant to allow 
direct comparison of RiboJ and non-RiboJ constructs.

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

## Kinetic analysis

Sigmoid drift curves are fitted and visualised per construct using `pr.plot_kinetics`, 
grouped by name and read type. We visually confirm that the sigmoid model accurately 
describes the data before proceeding to quantitative extraction of lag times.

:::::{tab-set}

::::{tab-item} DFHBI-1T — Transcription
:::{figure} ./experiments/20251027_Aptamer_test_Broccoli_mScarlet/figures/Broccoli_DFHBI-1T_kinetics.png
:label: fig:broccoli_dfhbi_kinetics
:align: center
Sigmoid drift fits to the DFHBI-1T transcription signal for all 
pT7-F30-2xBroccoli/tdBroccoli-{RiboJ}-UTR1-mScarlet constructs.
:::
::::

::::{tab-item} mScarlet — Translation
:::{figure} ./experiments/20251027_Aptamer_test_Broccoli_mScarlet/figures/Broccoli_mScarlet_kinetics.png
:label: fig:broccoli_mscarlet_kinetics
:align: center
Sigmoid drift fits to the mScarlet translation signal for all 
pT7-F30-2xBroccoli/tdBroccoli-{RiboJ}-UTR1-mScarlet constructs.
:::
::::

:::::

- Sigmoidal curves are well fitted to all constructs for both reporters.
- All constructs have detectable lag times, clearly showing that transcription onset 
  precedes translation onset.

## Transcription/translation lag times and translation initiation delay

Lag times are extracted per replicate well individually and plotted side by side for 
the DFHBI-1T and mScarlet reporters per construct, with error bars representing standard 
deviation across three replicate wells. The translation initiation delay is calculated 
as the difference between the mScarlet lag time and the DFHBI-1T lag time for each 
construct.

:::::{tab-set}

::::{tab-item} Transcription/translation lag times
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

::::{tab-item} Translation initiation delay
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

# Overall evaluation

Having assessed the performance of each reporter combination individually, we now bring 
together the key metrics into a single summary figure. The figure comprises three panels: 
(i) SNR plotted against lag CV% for all transcription reporters, providing a direct visual 
comparison of signal quality and timing precision; (ii) lag CV% as a bar plot across all 
constructs; and (iii) the translation initiation delay for each construct, representing 
the key biological output of this analysis.

:::{figure} ./experiments/20260511_combined_analysis/figures/Broccoli_mScarlet_summary_figure.png
:label: fig:summary_figure
:align: center
Summary figure. Panel (i) SNR vs lag CV% for all constructs. Panel (ii) lag CV% bar 
plot across all constructs. Panel (iii) translation initiation delay for all constructs.
:::

F30-2xBroccoli/DFHBI-1T paired with mScarlet is the highest performing reporter 
combination, achieving the lowest lag CV% (0.9%) and highest SNR (~2000) of all 
constructs tested. The tdBroccoli constructs show higher lag CV% (9.8-11.5%) but remain 
biologically meaningful, with translation initiation delays (~30 min) consistent with 
those of F30-2xBroccoli. For all constructs with a reliable transcription lag, the 
translation initiation delay is ~30-39 min, with F30-2xBroccoli-RiboJ showing a notably 
longer delay (~39 min) that may reflect altered translation initiation kinetics due to 
RiboJ-mediated mRNA restructuring.

# Conclusions and future directions

We have presented the first characterisation of the Broccoli/DFHBI-1T aptamer system as 
a transcription reporter in the PURE cell-free system, paired with mScarlet as a 
translation reporter for simultaneous monitoring of both events. All four constructs 
evaluated — F30-2xBroccoli, F30-2xBroccoli-RiboJ, tdBroccoli, and tdBroccoli-RiboJ — 
successfully resolved transcription and translation onset with high signal quality and 
reproducible lag time measurements.

**F30-2xBroccoli/DFHBI-1T paired with mScarlet is recommended as the optimal reporter 
system** for simultaneous transcription and translation monitoring in PURE, combining the 
highest SNR (~2000) with the lowest lag CV% (0.9%) of all constructs tested. Using this 
system, we measure a translation initiation delay of ~31 min in PURE, consistent across 
three of the four constructs evaluated. **This value is broadly consistent with previously 
reported translation initiation delays in cell-free expression systems**, though direct 
comparison is complicated by differences in fluorescent protein maturation times and 
system composition between studies.

F30-2xBroccoli-RiboJ shows a notably longer translation initiation delay (~39 min) 
compared to the other constructs, which may reflect altered translation initiation 
kinetics due to RiboJ-mediated mRNA restructuring. Whilst RiboJ is commonly used to 
insulate translation efficiency from upstream sequence context, these results suggest 
it may also influence the timing of translation initiation in PURE, which warrants 
further investigation.

Several directions for future work are highlighted:

- **Repeat MangoIV experiments with sequence-verified constructs** — sequencing of 
  the MangoIV constructs revealed unexpected construct identity issues, precluding 
  reliable interpretation of the MangoIV/TO1-Biotin data. Repeat experiments with 
  sequence-verified constructs are required before any conclusions can be drawn about 
  MangoIV performance in PURE.
- **Decoupling aptamer detection lag from biological lag** — a portion of the measured 
  translation initiation delay may reflect aptamer folding and dye-binding kinetics 
  rather than true transcription-translation delay. Future experiments using orthogonal 
  approaches **such as RT-qPCR or single-molecule fluorescence** could help decouple 
  these contributions.
- **RiboJ effect on translation timing** — the notably longer translation initiation 
  delay observed for F30-2xBroccoli-RiboJ warrants further investigation. A dedicated 
  experiment varying RiboJ position and sequence context could help clarify whether 
  this effect is specific to the Broccoli system or a more general property of RiboJ 
  in PURE.
- **Application to DNA toolkit characterisation** — the F30-2xBroccoli/DFHBI-1T + 
  mScarlet system is now available as an analytical tool for the characterisation of 
  DNA parts in PURE. Future DevNotes will apply this system to characterise the 
  transcription and translation kinetics of promoter, terminator, and RBS variants 
  within the DNA toolkit collection.