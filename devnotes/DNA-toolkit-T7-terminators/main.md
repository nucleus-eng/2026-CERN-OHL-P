---
# Ensure that this title is the same as the one in `myst.yml`
title: DNA toolkit - The T7 terminator collection
abstract: | 
    The development of modular PURE-based systems depends on a well-characterized repertoire of genetic components. Building on our previous release of the T7 promoter collection, here we address the subsequent process of transcriptional termination. We present the first characterization of an established library of T7 terminator sequences specifically within the PURE cell-free environment. Using a dual-reporter DNA construct, we quantified termination efficiencies and observed several distinct trends. Most notably, the PURE system appears to exhibit a higher relative propensity for transcriptional termination than has been reported for *E. coli* or IVT systems. Furthermore, the relative efficiency rankings of several sequences appear to shift between these biological contexts, suggesting that the PURE system may present a distinct transcriptional termination landscape worthy of further investigation. Regarding the DNA toolkit, we highlight the collection's potential for both the transcriptional isolation of multi-gene constructs, and the stoichiometric control of polycistronic operons. This characterization provides an initial foundation for a standardized terminator collection, offering additional "knobs" to tune protein production and potentially aiding the design of increasingly complex systems within the PURE environment.
---

# Background

Building upon the release of the T7 promoter collection, we continue the development of a DNA toolkit designed specifically for PURE cell-free expression systems. By offering a well-characterized and standardized set of DNA parts, this resource aims to streamline the development of PURE-based technologies and empower the community to establish DNA design considerations tailored specifically to the PURE environment.
Following our initial work on transcriptional initiation, we now focus on the subsequent process of termination. The native bacteriophage T7 [terminator](https://en.wikipedia.org/wiki/Terminator_(genetics)) is a DNA sequence that transcribes into an RNA stem-loop followed by a poly(U) tract to arrest T7 polymerase and halt gene transcription. In practice, researchers commonly rely on this single canonical sequence, which provides a termination efficiency of only ~60% in vivo and offers little scope for exploiting termination as a design variable. To address this, scientists previously engineered a collection of T7 terminators with varied efficiencies, including variants stronger than the native sequence, as well as weaker variants that expand the range of available termination strengths ([](https://doi.org/10.1093/g3journal/jkac070)).

Predictable termination is a critical requirement for sophisticated genetic design. In complex PURE systems and synthetic cell designs involving multi-gene constructs, robust termination allows genetic modules to operate independently through transcriptional isolation, preventing the production of oversized non-functional transcripts and ensuring finite system resources are not exhausted on unintended read-through products. Beyond simply improving on the native sequence, the range of efficiencies offered by this collection could also provide an additional design capability: weaker terminators could enable controlled read-through for stoichiometric control, allowing researchers to tune the relative abundance of different proteins within a single [polycistronic](https://en.wikipedia.org/wiki/Polycistronic_mRNA) operon. However, while these terminators were characterized in E. coli and simple in vitro transcription (IVT) systems, their performance has not been assessed within the specific context of the PURE system.

Towards this goal, we conducted the first characterization of this set of previously engineered T7 terminator sequences in PURE using a dual-reporter DNA construct. We highlight the differences and similarities in termination efficiency compared to the values previously reported, showcase their utility as a functional panel of terminators for use in the PURE system, and offer directions for further understanding transcriptional termination in PURE.

# The T7 terminator collection 

{ref}`table-t7-terminator-sequences` details the T7 terminator collection developed by  [Calvopina-Chavez et al., 2022](https://doi.org/10.1093/g3journal/jkac070). Terminators are distinguished by their structural properties: class I terminators are defined by the formation of stable RNA hairpins, while class II variants remain unstructured. The collection includes members from both categories, featuring the native T7 terminator sequence (T7nat), a structureless T7pause sequence, and 11 hybrid variants. 

:::{table} T7 terminator collection names, descriptions, and DNA sequences. This table was adapted from [Calvopina-Chavez et al., 2022](https://doi.org/10.1093/g3journal/jkac070). a, underlined text indicates sequences that form a secondary stem loop structure. b, lower case text indicates UUCG loop structures or TATCTGTT single- or double-pause sites.
:label: table-t7-terminator-sequences
:align: center

| Name    | Description                                 | DNA sequence<sup>a,b</sup>                                                      |
|---------|-----------------------------------------|---------------------------------------------------------------------------------|
| T7nat   | Wild-type sequence                      | {u}`AACCCCTTGGGGCCT`CTAAAC{u}`GGGTCTTGAGGGGTTT`TTTTT                                      |
| T7mod   | Stronger stem, shorter loop             | {u}`AACCCTGCGAGGCCTC`ttcg{u}`GAGGTCTCGCAGGGTT`TTTTTT                                      |
| T7pause | Dual pause sites, no hairpin            | CtatctgttatctgttCT                                                                        |
| T7hyb1  | T7mod with single pause                 | {u}`AAACAGATAGGCCCTC`ttcg{u}`GAGGGCCtatctgttT`TTTTTTT                                     |
| T7hyb2  | Short variant of T7hyb1                 | {u}`AACAGATAGGCCTC`ttcg{u}`GAGGCCtatctgtt`TTTTTTT                                         |
| T7hyb3  | T7hyb2, higher GC%                      | {u}`AACAGATAGGCCGC`ttcg{u}`GCGGCCtatctgtt`TTTTTT                                          |
| T7hyb4  | T7hyb3 altered GC sequence              | {u}`AACAGATAGCCGCG`ttcg{u}`CGCGGCtatctgtt`TTTTTT                                          |
| T7hyb5  | Short variant of T7hyb3                 | {u}`AGATAGGCCGC`ttcg{u}`GCGGCCtatctgt`tTTTTTT                                             |
| T7hyb6  | Dual-pause hairpin                      | {u}`AGATAACAGATAC`ttcg{u}`Gtatctgttatctgt`tTTTTTT                                         |
| T7hyb7  | T7hyb6, pause sites scrambled—variant 1 | {u}`AAGATAAGCAATC`ttcg{u}`GATTGCTTATCTT`GTTTTTTTT                                         |
| T7hyb8  | T7hyb6, pause sites scrambled—variant 2 | {u}`TAAAGAATAAACC`ttcg{u}`GGTTTATTCTTTA`GTTTTTTTT                                         |
| T7hyb9  | Fusion: T7hyb4-T7hyb6                   | {u}`AACAGATAGCCGCG`ttcg{u}`CGCGGCtatctgtt`TTTTTT{u}`CAGATAACAGATAC`ttcg{u}`Gtatctgttatct`gttTTTTTT |
| T7hyb10 | Fusion: T7hyb6-T7hyb4                   | {u}`AGATAACAGATAC`ttcg{u}`Gtatctgttatct`gttTTTTTTc{u}`AACAGATAGCCGCG`ttcg{u}`CGCGGCtatctgtt`TTTTTT |
:::

T7nat served as the architectural reference for the library, beginning with T7mod, which features a strengthened stem and a compact UUCG-hairpin loop inspired by [Mairhofer et al. (2015)](https://doi.org/10.1021/sb5000115). Building upon these designs, the hybrid variants were engineered to combine both class I and class II elements, integrating stable hairpins with structureless pause sites. This design strategy was intended to test whether such combinations could enhance termination efficiency while maintaining a compact genetic footprint.

The sequences were originally characterized using a bicistronic reporter construct under the control of a T7 promoter. In this architecture, the terminator was flanked by two fluorescent proteins; the relative fluorescence of these reporters provided a quantitative readout of transcriptional read-through and, consequently, termination efficiency. Previous studies evaluated the collection in both *E. coli* and simplified IVT systems as termination efficiencies have been shown to diverge significantly between biological contexts ([Du et al., 2009](https://doi.org/10.1002/bit.22491)). Due to this, our objective was to characterize their performance specifically within the PURE system.

# The dual-reporter construct

Following the design principles of the original study, we developed a dual-reporter DNA construct ({ref}`fig:pOpen-plamGFP-T7hyb10-mScarlet`) to quantify the termination efficiency of each variant in the collection. In this architecture, the inserted terminator is flanked by green ([plamGFP](https://www.fpbase.org/protein/plamgfp/)) and red ([mScarlet](https://www.fpbase.org/protein/mscarlet/)) fluorescent proteins; the relative fluorescence of these two reporters serves as a direct readout of termination efficiency. The assembly followed a two-stage cloning strategy which is outlined below. For more in-depth documentation, please refer to the research notebook attached to this DevNote.

::::{figure}
:label: fig:pOpen-plamGFP-T7hyb10-mScarlet
:::{seqviz} DNA/pOpen-plamGFP-T7hyb10-mScarlet.gbk
:height: 500px
:viewer: both
:name: pOpen-plamGFP-T7hyb10-mScarlet
:::
An example plasmid map of the dual-reporter construct containing the T7hyb10 variant. Note that the 5' untranslated regions of both reporter genes are identical to ensure that the native expression efficiency of both genes were as similar as possible.
::::

**Stage 1:** HiFi Assembly – We first generated a bicistronic entry vector, pOpen-plamGFP-ccdB-mScarlet. This involved linearizing the open-source pOpen-ccdB backbone and inserting plamGFP upstream and mScarlet downstream. The ccdB gene was reinserted between the reporters to serve as a marker for counter-selection in the subsequent step. pOpen was specifically chosen to enable dissemination of the construct through the Nucleus Distribution.

**Stage 2:** Golden Gate Assembly – We then utilized BsmBI restriction sites to replace the ccdB cassette with each T7 terminator variant. The resulting plasmid therefore enabled the measurement of termination efficiency based on the relative fluorescent signals of the two adjacent reporters. 

It is important to note that a construct entirely lacking a central terminator was not synthesized. Consequently, the T7pause variant was utilized as the negative control for termination throughout this work. While this does not provide an exact no-terminator baseline, previous studies reported that the T7pause sequence exhibits no termination in vivo and negligible termination in IVT systems ([Calvopina-Chavez et al., 2022](https://doi.org/10.1093/g3journal/jkac070)). We therefore deemed it a sufficient control for the initial characterization of the collection in the PURE system.

# Characterizing the T7 terminator collection in PURE

## Experiment setup

The terminator collection was quantified in triplicate using 10 µL PURExpress reactions each containing DNA at a concentration of 5 ng/µL ({ref}`reaction-setup`). Prior to quantification, excitation/emission parameters were optimized using our spectrophotometer for each reporter by performing a spectral scan on reactions that had gone to full completion. Once peak excitation emission values were identified, measurement bandwidths were adjusted to minimize noise generated from spectral overlaps. Experiments were run for 12 hours with 5 min kinetic intervals at 37 ˚C in a BioTek cytation 5 spectrophotometer. Ex/Em plamGFP 485nm/528nm | mScarlet 569nm/594nm. 

:::{table} Reaction setup
:label: reaction-setup
:align: center

| Component | Starting Concentration | Final Concentration | + DNA (μL) | - DNA (μL) |
|---|---|---|---|---|
| PURExpress - Solution A | 2.5x | 1X | 14.00 | 14.00 |
| PURExpress - Solution B | 3.3x | 1x | 10.51 | 10.51 |
| Murine RNAse inhibitor | 40 U / μL | 1 U / μL | 0.88 | 0.88 |
| DNA Template | 40 ng / μL | 5 ng / μL | 4.38 | — |
| Nuclease-Free Water | — | — | 5.24 | 9.62 |
| **Total** | | | **35** | **35** |
:::

## Timecourse data 

{ref}`fig:timecourse-representative-subset` presents the timecourse plate reader data for a representative subset of the T7 terminator collection. These time-course profiles are presented here primarily to exemplify the raw data distribution and to allow for a direct visualization of the kinetic trends across a representative subset of the library. The subset transitions from the native bacteriophage sequence (T7nat) to increasingly complex engineered hybrids. T7hyb1 leverages a strengthened stem-loop (T7mod) integrated with an internal pause site, while T7hyb6 features a stem-loop coupled with dual overlapping pause sites. To isolate the specific impact of these pause sites on termination efficiency, T7hyb8 serves as a control variant utilizing scrambled pause sequences, and the subset is completed by T7hyb10, which incorporates tandem double stem-loop structures to achieve maximal transcriptional arrest.

:::{figure} #fig:kinetics
:name: fig:timecourse-representative-subset
:align: center
:width: 100%
Timecourse data of plamGFP and mScarlet signals for a representative subset of the T7 terminator variants: T7pause, T7nat, T7hyb1, T7hyb6, T7hyb8, and T7hyb10. The shaded region within each plot represents the standard deviation in signal across three repeats.
:::

Since plamGFP is positioned at the 5' end and mScarlet at the 3' end of the bicistronic construct, weaker terminators are expected to yield higher mScarlet signals due to increased transcriptional read-through. This trend is clearly visible in the data, particularly with the T7pause variant, which exhibits the weakest GFP signal and a robust mScarlet signal, validating its role as a low-efficiency control. Note, however, that despite being a stronger terminator than T7pause, T7hyb8 actually produces a greater mScarlet signal. We therefore have to look at the ratio of GFP/mScarlet signal to determine the true termination efficiencies of each variant. A possible reason for this inflated mScarlet signal may be due to varying amounts of DNA concentrations being present in the final reactions despite efforts to ensure that they were normalized. 

## Termination efficiencies  

The termination efficiency of each variant was determined using the plamGFP and mScarlet fluorescence values at the 12-hour endpoint of each reaction. Following background subtraction against a negative control, the fluorescence ratio of GFP to mScarlet was then calculated. As the T7pause variant served as the baseline control, these ratios were normalized to the mean T7pause ratio. Termination efficiency was then derived as a percentage using the expression (1−(1/Normalized Ratio))×100 before plotting ({ref}`fig:efficiency`). This methodology therefore quantified termination efficiency by measuring the reduction in transcriptional readthrough relative to the T7pause control. 

:::::{tab-set}

::::{tab-item} Termination efficiency plot
:::{figure} #fig:termination_efficiency
:label: fig:efficiency
:align: center
Termination efficiencies of the T7 terminator collection normalized to T7pause.
:::
::::

::::{tab-item} Termination efficiency comparison
:::{table} A comparison of termination efficiencies across different biological contexts: PURE, E.coli, and an IVT system. The efficiency values for *E.coli* and IVT were derived from the original paper ([Calvopina-Chavez et al., 2022](https://doi.org/10.1093/g3journal/jkac070)). The T7pause value in PURE is emboldened to signify that this was used to normalize the PURE termination efficiencies.
:name: table-T7_terminator_efficiencies
:align: center
| Terminator | Efficiency in PURE (%) | Efficiency in *E.coli* (%) | Efficiency in IVT (%) |
|------------|--------------------------|------------------------|-------------------------|
| T7pause    | **-0**                   | ~0                     | 4                       |
| T7nat      | 91                       | 62                     | 5                       |
| T7mod      | 93                       | 78                     | 11                      |
| T7hyb1     | 95                       | 91                     | 41                      |
| T7hyb2     | 93                       | 90                     | —                       |
| T7hyb3     | 92                       | 89                     | —                       |
| T7hyb4     | 92                       | 89                     | —                       |
| T7hyb5     | 86                       | 83                     | —                       |
| T7hyb6     | 94                       | 91                     | 62                      |
| T7hyb7     | 70                       | 12                     | —                       |
| T7hyb8     | 63                       | 46                     | —                       |
| T7hyb9     | 98                       | 69                     | —                       |
| T7hyb10    | 97                       | 98                     | 91                      |
::::

:::::

By comparing our results with previously reported data, we found that the T7 terminator collection demonstrates higher absolute termination efficiencies across all variants in the PURE system ({ref}`table-T7_terminator_efficiencies`). This is most notable in the T7nat sequence, which yielded an efficiency of 91% in PURE, compared to the 62% reported in *E. coli* and only 5% in simplified IVT systems. While the relative performance ranking remained consistent for T7nat, T7mod, and T7hyb1–6 across all biological contexts, the T7hyb7–10 variants presented notable exceptions. Although T7hyb7 and T7hyb8 exhibited the lowest efficiencies in the collection as expected, they reached 70% and 63% in the PURE environment—a substantial increase and rank reversal over the 12% and 46% reported in *E. coli*. Similarly, T7hyb9 marginally exceeded the performance of T7hyb10 in PURE, whereas in *E. coli*, T7hyb9 showed a significantly weaker termination efficiency of 69% relative to the 98% achieved by T7hyb10.

# Conclusions and future directions

By comparing the termination efficiencies of the T7 terminator collection in PURE to previously reported measurements in *E. coli* and IVT systems, we observed that PURE exhibits an inherently higher propensity for transcriptional termination. Notably, the relative performance ranking of several variants underwent a rank reversal in PURE compared to data generated in *E. coli*. Collectively, these findings suggest that the PURE system presents a distinct transcriptional landscape warranting further investigation.

One potentially important implication of this increased termination propensity is that the T7pause variant may exert a non-negligible impact on transcription, potentially limiting its suitability as a baseline control. To address this, future follow-up experiments should include a dedicated no-terminator control to establish an absolute baseline for read-through and more accurately quantify the specific effects of the pausing sequences.

Beyond the comparative analysis, this collection provides a versatile toolbox for genetic design within the PURE system. With the exception of T7hyb7 and T7hyb8, these sequences represent a functional panel for the transcriptional isolation of genes. Utilizing these diverse sequences in multi-gene constructs should allow for robust genetic insulation while mitigating the risk of homologous recombination that often occurs when repeating identical native sequences.

Conversely, T7hyb7 and T7hyb8 serve as valuable tools for stoichiometric control in polycistronic operons. Future efforts should focus on further modifying these variants to generate a library with a broader dynamic range. This could facilitate the development of large polycistronic operons in PURE systems.







