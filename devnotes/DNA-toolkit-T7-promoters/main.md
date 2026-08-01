---
# Ensure that this title is the same as the one in `myst.yml`
title: DNA toolkit - The T7 promoter collection
abstract: |
   DNA is vital for testing and developing PURE cell-free expression systems, yet a dedicated DNA resource specific to PURE does not exist. To address this, we introduce the DNA toolkit - a well-characterised set of DNA parts designed and tested for PURE and available to the community. This will enable us to collectively build a DNA part library for engineering PURE systems while also defining key DNA design considerations for PURE. We begin by characterising the T7 promoter collection, a library of 9 promoters that express over a broad dynamic range and can be categorised into three functional expression levels. This characterisation, performed using three different reporter proteins (amajLime, deGFP, and plamGFP), also sheds light on important considerations for reporter choice in PURE quantification.
---

# Background
DNA is an important component of PURE cell-free expression systems providing the instructions to drive protein production. DNA is therefore paramount in both PURE development and testing, and its application in synthetic cell engineering. For example, the gold standard of PURE quantification is through fluorescent protein expression[{sup}`1`](https://doi.org/10.1021/acssynbio.4c00697), and synthetic cells more frequently encapsulate PURE to provide functionality[{sup}`2`](https://doi.org/10.1038/s41589-025-02002-2). However, there is not yet a DNA resource specific to PURE from which the community can draw. The DNA toolkit seeks to address this through providing a well-characterised set of DNA parts accessible to the community through the Nucleus Distribution. This aims to both simplify and standardize DNA construct design, benefitting PURE and synthetic cell development, and enabling the community to more efficiently establish DNA design considerations specifically for PURE. 

Here we present the T7 promoter collection as the first entry to the DNA toolkit. [Promoters](https://en.wikipedia.org/wiki/Promoter_(genetics)) are regulatory elements that control DNA transcription, the first operation of gene expression involving the decoding of DNA into RNA before its subsequent translation into protein. Tight regulation of transcription is desirable in PURE as it has a direct correlation to protein yield, and if referring to synthetic cells, the overall function to which that protein imparts on the cell. More importantly, without transcriptional control, we will be unable to orchestrate the expression of multiple proteins within PURE preventing us from reconstituting the complexity of living systems. 

Towards this goal, we have quantified the performance of nine different T7 promoter sequences in PURE using three distinct reporter proteins: amajLime, deGFP, and plamGFP. By utilising a selection of reporter proteins we were also able to gain insight into the considerations of reporter choice for PURE quantification. 

# The T7 Promoter Collection 

The T7 promoter collection ({ref}`table-promoter-params`) was originally curated by [Jackson-Smith](https://purl.stanford.edu/yt728jc2185) and was selected across two different libraries - the phage T7 phage genome engineered by Chan, Kosuri and Endy[{sup}`3`](https://doi.org/10.1038/msb4100025), and the T7 promoter variant library constructed and tested in vitro by Komura, et al [{sup}`4`](https://doi.org/10.1371/journal.pone.0196905). The collection was built to expand the PURE DNA toolbox allowing for greater control over the transcriptional machinery. Promoter sequences were chosen to span a broad dynamic range enabling the design of multi-gene DNA constructs with varied protein expression levels. This would advance PURE gene expression away from the co-expression of individual DNA molecules towards small genomes encoded on a single template. 
:::{table} T7 promoter sequences and their relative expression levels. Bases shown in bold represent mutations relative to the consensus T7 promoter sequence
:label: table-promoter-params
:align: center

| Promoter | Relative expression level| Sequence 5'-3' |No. of mutations| |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| T7-1 | <span style="color:Green">Low</span> | TAATA**TC**ACT**G**ACTA**A**AG**T** |5|
| T7-3 | <span style="color:Orange">Medium</span>| T**G**A**A**ACGACTCACT**T**TAGG |3| 
| T7-4 | <span style="color:Green">Low</span> | T**T**ATACG**TG**TC**C**CT**G**TAGG |5| 
| T7-5 | <span style="color:Orange">Medium</span> | **G**AATACG**C**CTCACT**T**TAGG |3| 
| T7-6 | <span style="color:Orange">Medium</span> | **C**AATACG**T**CTCACTATAG**C** |3| 
| T7-7 | <span style="color:Orange">Medium</span> | T**T**ATACGACTCA**G**TATAG**T** |3| 
| T7-8 | <span style="color:Red">High</span> | **CG**ATACGACTCACTATAGG |2| 
| T7-9 | <span style="color:Red">High</span> | **G**AATACGACTCACTATAGG |1| 
| T7-10 | <span style="color:Red">High</span> | TAATACGACTCACTA**A**AGG |1| 

:::

To enable quantification of the promoter collection, each promoter sequence was cloned upstream of a different fluorescent reporter. The expression of the fluorescent reporter could then be detected using a spectrophotometer. Promoters were cloned via PCR using universal primers which exploited the homologous 5'UTRs of the fluorescent reporters. After amplification, samples were column purified, DpnI digested to remove template plasmids, and then re-column purified to generate high quality templates for PURE.  

# Fluorescent Reporters

Fluorescent proteins have a unique set of properties that govern the way they interact with light. Their excitation and emission wavelengths determine their colour. The difference in these two values being known as the [Stokes shift](https://en.wikipedia.org/wiki/Stokes_shift); an important consideration for defining measurement parameters. Brightness is a value assigned to the product of the proteins' molar extinction coefficient and quantum yield. These values describe how strongly a protein is able to absorb photons, and the ratio to which photons are absorbed vs. emitted. Finally, maturation half-time reports on the time taken for a newly translated protein to be in an excitable state. By quantifying the promoter collection with three distinct proteins, we aimed to gain an insight into how these properties should inform reporter choice in PURE ({ref}`table-reporter-params`).

:::{table} The three reporters used in this study and their associated spectral and photophysical properties. Values acquired from FPbase. See links for details: [amajLime](https://www.fpbase.org/protein/amfp486/), [plamGFP](https://www.fpbase.org/protein/plamgfp/),   [deGFP](https://www.fpbase.org/protein/egfp/). 
:label: table-reporter-params
:align: center

| Property | amajLime| plamGFP| deGFP|  | |  | 
| --- | --- | --- | --- | --- | --- | --- |
|Color|Cyan|Green|Green|
| Peak excitation (nm) |458|502|488| 
| Peak emission (nm)|486 |514|512 | 
| Stokes shift (nm)|28|13|24| 
| Extinction coefficient (M{sup}`-1`cm{sup}`-1`) |40,000|98,600|55,900|
| Quantum yield|0.24|0.96|0.6| 
| Brightness | 9.6|94.7|33.5|
| Maturation half-time|12-48hrs [{sup}`8`](https://parts.igem.org/Part:BBa_K1033914)|???|7-8 mins| 

:::

The three proteins exhibit reasonable diversity in their origins and characteristics. amajLime and plamGFP are native fluorescent proteins derived from sea coral species, *Anemonia majano* and *Platygyra lamellina*, respectively. deGFP is an engineered variant of the *Aequorea victoria*-derived eGFP. It is important to note that all DNA sequences were codon optimised for PURE ribosomes to minimise any species-related translation bias.

Their features also vary. plamGFP is exceptionally bright, whereas amajLime has low brightness but is uniquely also a chromoprotein meaning it is visible in ambient light. deGFP has average brightness but its sequence was specifically optimised for PURE cell-free systems. It is a smaller, N- and C-terminally truncated protein expressed from an mRNA with minimal secondary structure leading to faster maturation and a higher expression efficiency. While maturation half-time data for plamGFP is unavailable, we expect it to be closer to that of amajLime than deGFP, given their shared native origin and lack of engineering.

# Promoter performance

The promoter collection was quantified in triplicate using 10 µL PURExpress reactions each containing DNA at a concentration of 5 ng/µL. A single experimentalist quantified the amajLime constructs (CN) whereas two experimentalists quantified the plamGFP/deGFP constructs (CN & AJ). The amajLime data was derived from a single endpoint measurement in comparison to timecourse measurements taken for plamGFP/deGFP. As such, the plamGFP/deGFP analysis is more thorough. Prior to quantification, excitation/emission parameters were optimised using our spectrophotometer for each reporter by performing a spectral scan on reactions that had gone to full completion. Once peak excitation emission values were identified, measurement bandwidths were adjusted to minimise noise generated from spectral overlaps. Experiments were run for ≥12 hours with 5 min kinetic intervals at 37 ˚C in a BioTek cytation 5 spectrophotometer. Ex/Em | bandwidth: *amajLime* 454nm/488nm | 20nm, *plamGFP/deGFP* 485nm/512nm | 17nm. 

:::::{tab-set}

::::{tab-item} deGFP
:::{figure} #deGFP-final-summary
:name: fig-summary-deGFP
:align: center
:width: 100%

Steadystate fluorescence values of deGFP expression under the control of the T7 promoter collection. All values were background subtracted prior to plotting. Reaction duration: 12 hrs.
:::
::::

::::{tab-item} plamGFP
:::{figure} #plamGFP-final-summary
:name: fig-summary-plamGFP
:align: center
:width: 100%

Steadystate fluorescence values of plamGFP expression under the control of the T7 promoter collection. All values were background subtracted prior to plotting. Reaction duration: 12 hrs.
:::
::::

::::{tab-item} amajLime
:::{figure} #amajLime-final-summary
:name: fig-summary-amajLime
:align: center
:width: 100%

Endpoint fluorescence values of amajLime expression under the control of the T7 promoter collection. All values were background subtracted prior to plotting. Reaction duration: 14 hrs.
:::
::::

:::::


The summary data informs us that the T7 promoter collection spans a ~1000-fold dynamic range of expression ({ref}`fig-summary-deGFP`). Promoters can be categorized into low, medium, and high expression level groups as denoted by the colored markers. These expression groups appear to directly correspond with the number of mutations present in the promoter sequences in comparison to the consensus sequence. Low expression promoters possess five mutations, medium promoters possess three mutations, and high promoters possess one or two mutations ({ref}`table-promoter-params`). With this in mind, it may be possible to define a fourth expression level group between medium and high expression level promoters to house T7-8. 

Whilst all reporters exhibit a similar dynamic range, deGFP appears to be the only reporter in which both of the low expression group promoters can be distinguished from the background signal. AmajLime and plamGFP have either T7-1 or both T7-1 and T7-4 within the background noise. This may be due to the difference in spectral properties of the proteins. In theory, plamGFP is reported to be the brightest of the three reporters and yet it is consistently detected at an order of magnitude lower than amajLime or deGFP. We assume that the smaller Stokes shift of plamGFP may play a role in this as it prevented us from measuring the reporter close to its optimum Ex/Em values. In fact, the optimum values were conveniently found to be very similar to deGFP at 485nm/512nm enabling us to measure the plamGFP and deGFP on the same plate. Moving the Ex/Em values closer to the optimum values of 502nm/514nm either resulted in a negligible increase, or a decrease in signal detection. The small Stokes shift of plamGFP may therefore prevent full exploitation of the reported brightness of the molecule. 

:::::{tab-set}

::::{tab-item} Low
:sync: tab4
:::{figure} #kinetics-low
:name: fig-curves-low
:align: center
:width: 100%

**Low expression promoters** - Each curve represents a single PURE replicate containing a promoter sequence controlling the expression of either plamGFP, or deGFP. The data from each row of figures was generated by either Astrid Joergensen (Top), or Charlie Newell (Bottom). 
:::
::::

::::{tab-item} Medium
:sync: tab5
:::{figure} #kinetics-medium
:name: fig-curves-medium
:align: center
:width: 100%

**Medium expression promoters** - Each curve represents a single PURE replicate containing a promoter sequence controlling the expression of either plamGFP, or deGFP. The data from each row of figures was generated by either Astrid Joergensen (Top), or Charlie Newell (Bottom). 
:::
::::

::::{tab-item} High
:sync: tab6
:::{figure} #kinetics-high
:name: fig-curves-High
:align: center
:width: 100%

**High expression promoters** - Each curve represents a single PURE replicate containing a promoter sequence controlling the expression of either plamGFP, or deGFP. The data from each row of figures was generated by either Astrid Joergensen (Top), or Charlie Newell (Bottom). 
:::
::::

:::::

Kinetic data from the plamGFP/deGFP constructs provides deeper insight into the expression characteristics of each promoter group. When observing the low expression group curves, the lack of clear distinction between the promoter signals and the negative noise in the plamGFP data again highlights its reduced sensitivity as a reporter ({ref}`fig-curves-low`). Despite this, the curves confirm the activity of T7-1 and T7-4 as functional promoters with T7-4 being the strongest. We can confirm the activity of both promoters due to the appearance of the latter phase of a sigmoidal curve in the deGFP samples. It is important to note here that signal detection began ~ 15mins after the reaction was placed at 37˚C which may explain the lack of the lag phase of the S-curve. 

The medium and high expression group curves continue to show the disparity in sensitivity between reporters by virtue of a ~10-fold difference in fluorescence signal. There is not a clear distinction in promoter activity in the medium expression group demonstrated by a significant overlap of standard deviation values between all samples for each reporter ({ref}`fig-curves-medium`). The middle expression group therefore represents a sub-collection of 4 promoters with similar expression levels. These sequences may be useful when engineering multi-gene constructs in which several proteins need to be expressed at similar abundances. Multiple promoters with minor sequence variations may limit the chance of homologous recombination that would otherwise occur when assembling multiple identical sequences. The curves of the high expression group highlight the relationship between amount of sequence mutations and promoter expression level ({ref}`fig-curves-high`). T7-8 is isolated and below T7-9 and T7-10 which are clustered together. 

# Conclusions and Future Directions

The T7 promoter collection consists of 9 promoters which span a ~1000-fold dynamic range of expression. Promoter sequences can be categorized into low, medium, and high expression level groups corresponding to their relative abundance of point mutations in comparison to the consensus T7 promoter sequence. It may be possible to exploit this relationship to design more T7 promoter sequences across all groups to increase the breadth of the collection. 

deGFP is a more optimal fluorescent protein for reporting on PURE performance than amajLime or plamGFP. The brightness of a fluorescent reporter should not be used a single characteristic to determine reporter choice for PURE. A holistic approach should be taken whereby all spectral and photophysical characteristics including Stokes shift and maturation half-time are considered. It is encouraged to always experimentally test a reporter protein prior to integrating it in a system for PURE quantification.

Whilst this has provided insight into the considerations for choosing a reporter protein for PURE, RNA aptamer reporters may be more accurate in quantifying promoter performance. Fluorescent RNA aptamers bind to small molecule dyes with high affinity causing them to fluoresce. This directly couples DNA transcription to the generation of a fluorescent signal removing the latency involved in protein translation and the subsequent maturation of the chromophore. Future work will aim to characterise the T7 promoter collection using aptamers providing insight into the best practices for PURE quantification. 



<!---DNA is an intrinsic component of PURE cell-free expression systems acting as the intructions to drive the primary goal of protein production. The ability to test and develop upon PURE, and to also apply it to synthetic cell applications, therefore heavily relies on the DNA that the system is provided with. For example, the current gold standard of PURE performance quantitifcation is through the expression of DNA encoding a fluorescent reporter protein [insert ref], and synthetic cell researchers are more frequently exploiting PURE systems to endow cells with useful functionality [insert refs]. However, there is not yet a DNA resource specific to PURE systems from which the community can draw from. The DNA toolkit seeks to address this through providing a well-characterised set of DNA parts accessible to the community through the nucleus distribution. This aims to both simplify and standardize DNA construct design, benefitting PURE and synthetic cell development, and enabling the community to more efficiently establish DNA design considerations specifically for PURE. 

Towards this, we have characterised nine different T7 promoter sequences in PURE. The collection originally curated by ACJS was selected across two different libraries - the phage T7 phage genome engineered by Chan, Kosuri and Endy¹, and the T7 promoter variant library constructed and tested in vitro by Komura², et al. The promoter sequences were chosen to exhibit a broad dynamic range enabling the design of DNA constructs with varied expression levels. To confirm their activity, we quantified the performance of each promoter using three different reporter proteins each with differing spectral properties: amajLime, deGFP, and plamGFP. Whilst enabling a comprehensive study of promoter performance, the difference in spectral properties revealed some important considerations on choosing an appropriate fluorescent reporter for PURE.

Their excitation and emission wavelengths determine their colour. The difference in these two values being known as as the Stokes shift; an important consideration for defining measurement parameters. Brightness is a value assigned to the product of the proteins' molar extinction coefficient and quantum yield. These values describe how strongly a protein is able to absorb photons, and the ratio to which photons are absorbed vs. emitted. Maturation half-time reports on the time taken for a newly translated protein to be in an excitable state

The three proteins exhibit reasonable diversity. amajLime and plamGFP are native fluorescent proteins derived from sea coral species, Anemonia majano and Platygyra lamellina, respectively. AmajLime has a modest brightness and is unique in that it is also a chromoprotein meaning it can be visualised in ambient light. plamGFP is an exceptionally bright protein. deGFP is an engineered variant of the Aequorea victoria-derived enhanced green fluorescent protein optimised for expression in cell-free systems. Specifically, deGFP DNA produces an mRNA with minimal secondary structures and an N- and C-terminal truncated protein which is smaller than eGFP and more efficiently expressed in PURE. To minimise any species related translation bias, all DNA sequences were codon optimised for the E.coli ribosomes used in PURE. Whilst there is no available data on the maturation half-time for plamGFP, we expect it to be closer to that of amajLime than of deGFP due to their species similarity and its absence of any engineering. 

To remove any codon-usage bias, all genes, apart from deGFP which is already optimised, were codon optimised to work in PURE. Unlike the wild-type amajLime and plamGFP, deGFP is unique in that it is an engineered variant of eGFP. Specifically, deGFP has N- and C-terminal truncations making it smaller than eGFP and more efficiently expressed in PURE. This gives rise to its fast maturation half-time. Whilst there is no available data for the specific maturation time of either plamGFP, or amajLime, we can be confident that they both mature at significantly slower rates than deGFP. For example, bacterial colony coloration has been reported to occur within 12-24 hours of expression of amajLime on several occasions. amajLime is also a very dim protein, espescially in comparison to the bright plamGFP, and slightly less bright deGFP. It will be interesting to see how the respective properties of each reporter differ in their ability to quantify the promoter collection.

## Excitation and emission spectra 

:::::::{tab-set}

:::::{tab-item} amajLime
:sync: tab1

:::{figure} ./experiments/251026-DNA-Toolkit-Promoter-Collection/04-Figures/00-Spectra/amajLime-spectra-Ex.png
:width: 65%
:align: center

amajLime excitation spectrum.
:::

:::{figure} ./experiments/251026-DNA-Toolkit-Promoter-Collection/04-Figures/00-Spectra/amajLime-spectra-Em.png
:width: 65%
:align: center

amajLime emission spectrum.
:::

:::::

:::::{tab-item} plamGFP
:sync: tab2

:::{figure} ./experiments/251026-DNA-Toolkit-Promoter-Collection/04-Figures/00-Spectra/plamGFP-spectra-Ex.png
:width: 65%
:align: center

plamGFP excitation spectrum.
:::

:::{figure} ./experiments/251026-DNA-Toolkit-Promoter-Collection/04-Figures/00-Spectra/plamGFP-spectra-Em.png
:width: 65%
:align: center

plamGFP emission spectrum.
:::

:::::

:::::{tab-item} deGFP
:sync: tab3

:::{figure} ./experiments/251026-DNA-Toolkit-Promoter-Collection/04-Figures/00-Spectra/deGFP-spectra-Ex.png
:width: 65%
:align: center

deGFP excitation spectrum.
:::

:::{figure} ./experiments/251026-DNA-Toolkit-Promoter-Collection/04-Figures/00-Spectra/deGFP-spectra-Em.png
:width: 65%
:align: center

deGFP emission spectrum.
:::

:::::

:::::::

::::::{figure} :label: fig-all-tabs
:align: center

Endpoint/steadystate fluorescent values of the three reporter proteins under the control of the T7 promoter collection.

:::::{tab-set}

::::{tab-item} amajLime
:sync: tab1
:::{figure} ./04-Figures/01-PURE_data/Summary_data_amajLime.png
:name: fig-summary-amajLime
:align: center
:width: 100%

Endpoint fluorescence values of AmajLime expression under the control of the T7 promoter collection. All values were background substracted prior to plotting. Reaction duration: 14 hrs.
:::

::::

::::{tab-item} plamGFP
:sync: tab2
:::{figure} ./04-Figures/01-PURE_data/Summary_data_plamGFP.png
:name: fig-summary-plamGFP
:align: center
:width: 100%

Steadystate fluorescence values of plamGFP expression under the control of the T7 promoter collection. All values were background substracted prior to plotting. Reaction duration: 12 hrs.
:::

::::

::::{tab-item} deGFP
:sync: tab3
:::{figure} ./04-Figures/01-PURE_data/Summary_data_deGFP.png
:name: fig-summary-deGFP
:align: center
:width: 100%

Steadystate fluorescence values of deGFP expression under the control of the T7 promoter collection. All values were background substracted prior to plotting. Reaction duration: 12 hrs.
:::

:::::
::::::
-->


