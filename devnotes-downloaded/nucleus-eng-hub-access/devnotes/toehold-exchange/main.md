---
abstract: |
  [Abstract].
---

# Overview

Toehold exchange (THE) riboregulators are a class of RNA molecules that us toehold-mediated strand exchange (TMSE -- Ref 1) to regulate protein translation ([](https://doi.org/10.1101/2025.09.25.678518), [](https://doi.org/10.1101/2025.09.24.678369)). In TMSE reactions an input RNA strand binds to an RNA duplex (gate) via a short toehold domain and, through sequence complementarity, initiates a process of branch migration that ultimately
can displace an output RNA strand from the double stranded gate duplex. In the case of a THE riboregulator, the release of the output RNA esults in exposure of a ribosome binding sequence (*rbs*) that connects RNA strand exchange to protein expression. THE riboregulators are a subset of a broader class of circuits, termed ctRSD circuits ([](10.1126/sciadv.abl4354), [](https://doi.org/10.1021/acssynbio.3c00079), [](https://doi.org/10.1021/acs.nanolett.0c03629)), that use self-cleaving ribozymes to cotranscriptionally produce the double-strand RNA gates needed for TMSE reactions. ctRSD circuits can be programmed to execute logic, signal amplification, and signaling cascades.

The mechanism of TMSE offers many design parameters for precisely tuning
the strength of protein expression. In {ref}`fig1` we emphasize methods
that rely on design changes to the short input RNA rather than changes
to the gate that contains the long protein coding sequence. In addition
to transcriptional control of expression strength by changing DNA
template concentrations ({ref}`fig1`, left), protein expression strength
can be controlled at the translational level by varying the length of an
unstructured domain at the 5' end of the input strand (*d* domain). This
unstructured domain serves as a standby site for the ribosome to bind to
facilitate translation initiation after strand exchange ([](https://doi.org/10.1021/acs.nanolett.0c03629)), with
increasing lengths increasing translation strength ({ref}`fig1`, right).
Lengths beyond 20 bases are not predicted to provide additional benefit
([](https://doi.org/10.1021/acs.nanolett.0c03629)). Because the toehold exchange mechanism is reversible (Ref 1),
protein expression can also be controlled by modulating the strength of
the forward or reverse strand exchange reactions. Increasing the degree
of complementarity between the input toehold of the input and gate (*s'*
domain) increases the rate of production of gate in the ON state.
Conversely, increasing the degree of complementarity between the output
toehold of the gate and input (*e* domain) decreases the rate of
production of gate in the ON state. Both mechanisms thus tune protein
expression strength at the post-transcriptional level ({ref}`fig1`,
middle).

Together these results illustrate three distinct mechanisms for tuning
protein expression with THE riboregulators:

1.  Modulating the concentration of reactants (transcriptional control)

2.  Modulating the rate and extent of reaction to produce products (post-transcriptional control)

3.  Modulating the translation rate of the products (translational control)

Here we present the sequences and protocols for translational control experiments.

:::{figure} ./general/image1-1.png
:label: fig1

Kinetic data of THE riboregulator operation in PURExpress
with plasmid DNA templates. The yellow highlighted domains on the input
RNA specify domains that can be modified to control protein expression
strength. The *Rz* domain on the gate indicates the self-cleaving
ribozyme necessary to cotranscriptionally produce the double strand RNA
duplex needed for TMSE. For transcriptional control results INPUT and
GATE template concentrations are listed in the plot. In the remain
results both templates were at 5 nmol/L. Legends indicate the length (in
bases) of *s'*, *e*, or *d* domains on the input RNA. Other than the
translational control results, the *d* domain was 20 bases. Data from
[](https://doi.org/10.1101/2025.09.25.678518). See Supplementary Section 1 in [](https://doi.org/10.1101/2025.09.25.678518) for a detailed description
of component and domain nomenclature.
:::

# Design

For a detailed description of THE riboregulator design see Supplementary
Section 2 of [](https://doi.org/10.1101/2025.09.24.678369). Supplementary Section S2 of [](https://www.science.org/doi/full/10.1126/sciadv.abl4354) describes the
design choices for the broader class of ctRSD gates.

Below we summarize a few design considerations of particular note:

1.  THE riboregulators are currently designed with an 18-base linker
    sequence (*n* domain) upstream of the protein coding sequence (CDS)
    that adds 6 amino acids N terminus of the protein.

2.  There is a start codon at beginning of the *n* linker domain for
    translation initiation; the start codon in native protein sequence
    is changed to a leucine codon (TTA) to minimize the chance for
    spurious initiation from gates in the OFF state.

3.  Not all design trends in PURE produce the same results in cells or
    in cell lysate, notably the post-transcriptional control mechanisms
    (see [](https://doi.org/10.1101/2025.09.25.678518) and [](https://doi.org/10.1101/2025.09.24.678369)).

To design alternative sequences see resources below for software to create.

## Key Materials

:::{table} Non-nucleis acid materials. *Most 384-well plates should work but check the minimum volume recommended by the manufacture and scale the reactions up accordingly if the minimum volume is > X µL. 
:label: tbl:materials
:align: center

| **Name** | **Product** | **Manufacturer** | **Part #** | **Price** | **Link** | **Storage** |
| --- | --- | --- | --- | --- | --- | --- |
| PURExpress | NEB PURExpress in vitro protein synthesis kit | New England Biolabs | E6800S | $307.00 | [link](https://www.neb.com/en-us/products/protein-expression/cell-free-protein-expression/purexpress) | -80°C |
| HBC620 Pepper dye | HBC620 | MedChemExpress | HY-133520 | | [link](https://www.medchemexpress.com/HBC620.html) | |
| DMSO | DMSO | | | | [link]() | |
| 5x txn buffer | T7 RNA polymerase | ThermoFisher Scientific | EP0111 | $109.00 | [link](https://www.thermofisher.com/order/catalog/product/EP0111) | -20°C |
| 384-well plates | Microplate, 384 well, PS, F-bottom | Greiner Bio-one | 784101 | $408.20 | [link](https://shop.gbo.com/en/usa/products/bioscience/microplates/384-well-microplates/384-well-small-volume-hibase-microplates/784101.html) | Room temp |
| Nuclease free water | Nuclease free water (not DEPC treated) | ThermoFisher Scientific | AM9939 | $162.00 | [link](https://www.thermofisher.com/order/catalog/product/AM9939) | Room temp |
| 200 µL PCR tubes | TempAssure PCR Flex-Free 8-Tube Strips, Attached Individual Optical Caps | USA Scientific | 1402-4700 | $96.75 | [link](https://www.usascientific.com/flex-free-pcr-8-strip-attached-clear-flat-caps/p/PCR-Tu-Flex-Att-Optic) | Room temp |
| 2x PCR Master Mix | Phusion Flash High-Fidelity PCR Master Mix | ThermoFisher Scientific | F548S | $110.65 | [link](https://www.thermofisher.com/order/catalog/product/F548S) | -20°C |
| PureLink cleanup kit | PureLink PCR Purification Kit | ThermoFisher Scientific | K310001 | $148.00 | [link](https://www.thermofisher.com/order/catalog/product/K310001) | Room temp |

:::

## DNA Components

:::::{tab-set}

::::{tab-item} Primers and Molecular Beacons
:::{table} Nucleic acid primers and molecular beacon oligonucleotides, typically ordered from Integrated DNA Technologies (IDT). Base modifications follow IDT's nomenclature. An 'm' preceding a base indicates a 2'-O-methyl modification. The quencher modified strand of the reporter should be ordered with HPLC purification. All other strands can be ordered with standard desalting.
:label: tbl:sequences
:align: center

| **Name** | **Sequence** | **Purpose** |
| --- | --- | --- |
| T7fwd | TTCTAATACGACTCACTATAGGGAG | fwd primer for T7 promoter |
| T7rev | CAAAAAACCCCTCAAGACCCGTTTAG | rev primer for T7t terminator |
| Thyb10rev | AAAAAAAAACAGATAGCCGCGCGAAC | rev primer for Thyb10 terminator |
| R{x2}-F-2omR | /5HEX/mCmUmAmCmAmUmCmAmCmAmUmAmCmUmA | 2omRNA-based fluorophore strand of molecular beacon, can be used with any quencher strand below |
| R{rbs2}-Q-2omR | mAmGmGmAmGmGmUmAmGmUmAmUmGmUmGmAmUmGmUmAmG/3IAbRQSp/ | 2omRNA-based quencher strand of molecular beacon with rbs toehold |
| MB rbs trigger 2omR | mCmUmAmCmAmUmCmAmCmAmUmAmCmUmAmCmCmUmCmCmU | 2omRNA-based trigger strand for spiking molecular beacon signal, rbs toehold |

:::
::::

::::{tab-item} ctRSD Inputs
:::{table} DNA templates for ctRSD inputs. These sequences can be ordered as linear gene fragments, typically eBlocks or gBlocks from IDT. Full sequences are for eBlock orders (>300 bases). Underlined portions of the sequences represent the transcription unit (promoter to terminator) for ordering as a gBlock (>125 bases).
:label: tbl:dna-templates
:align: center

| **Translation strength** | **Short name** | **Full name** | **Sequence** |
| --- | --- | --- | --- |
| Expression: Min (OFF) | Io | Io | gaagtctaacgctgctctgggctaactgtcCATTACTCGCATCCATTCTCAGGCTGTCTC<br>GTCTCGTCTC<u>TTC**TAATACGACTCACTATA**GGGAGATTCGTCTCCCAATCAATAACA</u><br><u>CACATA*ataatcAGATAACAGATACttcgGtatctgttatctgttTTTTTTcAACAGATAG</u><br><u>CCGCGttcgCGCGGCtatctgttTTTTTTt*</u>agctgtcaccggatgtgctttccggtctg<br>atgagtccgtgaggacgaaacagcctcCCAGGATACATAGATTACCACAACTCCGAGCCCT<br>TCCACC |
| Expression: Max | IN_1 | I{u1d} [], [d₂₀ Thyb10] | gaagtctaacgctgctctgggctaactgtcCATTACTCGCATCCATTCTCAGGCTGTCTC<br>GTCTCGTCTC<u>TTC**TAATACGACTCACTATA**GGGAGATTCGTCTCCCAAATACTTAAT</u><br><u>ACAAAATAATCACTTCACAACATCA*ataatcAGATAACAGATACttcgGtatctgttatct</u><br><u>gttTTTTTTcAACAGATAGCCGCGttcgCGCGGCtatctgttTTTTTT*t</u>agctgtcaccg<br>gatgtgctttccggtctgatgagtccgtgaggacgaaacagcctcCCAGGATACATAGATTA<br>CCACAACTCCGAGCCCTTCCACC |
| Expression: Low | IN_2 | I{u1} [], [Thyb10] | gaagtctaacgctgctctgggctaactgtcCATTACTCGCATCCATTCTCAGGCTGTCTC<br>GTCTCGTCTC<u>TTC**TAATACGACTCACTATA**GGGAGATTCGTCTCCCATCACTTCACA</u><br><u>ACATCA*ataatcAGATAACAGATACttcgGtatctgttatctgttTTTTTTcAACAGATAGC</u><br><u>CGCGttcgCGCGGCtatctgttTTTTTUt*</u>agctgtcaccggatgtgctttccggtctga<br>tgagtccgtgaggacgaaacagcctcCCAGGATACATAGATTACCACAACTCCGAGCCCTTC<br>CACC |
| Expression: Medium | IN_3 | I{u1d} [], [d₅ Thyb10] | gaagtctaacgctgctctgggctaactgtcCATTACTCGCATCCATTCTCAGGCTGTCTC<br>GTCTCGTCTC<u>TTC**TAATACGACTCACTATA**GGGAGATTCGTCTCCCAATAATCACTT</u><br><u>CACAACATCA*ataatcAGATAACAGATACttcgGtatctgttatctgttTTTTTTcAACAGA</u><br><u>TAGCCGCGttcgCGCGGCtatctgttTTTTTUt*</u>agctgtcaccggatgtgctttccggtctg<br>atgagtccgtgaggacgaaacagcctcCCAGGATACATAGATTACCACAACTCCGAGCCCTT<br>CCACC |
| Expression: High | IN_4 | I{u1d} [], [d₁₀ Thyb10] | gaagtctaacgctgctctgggctaactgtcCATTACTCGCATCCATTCTCAGGCTGTCTC<br>GTCTCGTCTC<u>TTC**TAATACGACTCACTATA**GGGAGATTCGTCTCCCAACAAAATAATC</u><br><u>ACTTCACAACATCA*ataatcAGATAACAGATACttcgGtatctgttatctgttTTTTTTcAA</u><br><u>CAGATAGCCGCGttcgCGCGGCtatctgttTTTTTUt*</u>agctgtcaccggatgtgctttccgg<br>tctgatgagtccgtgaggacgaaacagcctcCCAGGATACATAGATTACCACAACTCCGAGC<br>CCTTCCACC |

:::
::::

::::{tab-item} Full THE TX unit
:::{table} DNA templates for full THE riboregulator transcription (TX) unit. **Bold** sequences indicate promoters. Underlined sequences indicate complementary regions for overlap PCR. *Italic* sequences indicate terminators.
:label: tbl:dna-tx-unit
:align: center

| **Full TX unit** | **Short name** | **Full name** | **Sequence** |
| --- | --- | --- | --- |
| | G_1 | G{u1,rbs2} [s₄u], [], [R3 sCFP3A tDF30PPr T7t] | <u>TTC**TAATACGACTCACTATA**GGGAGATTCGTCTCCCACTACATCCACA</u><br><u>TACTACCTCCTTTACTTCACATTCGGGTCGGCATGGCATGTGCACCTCCTCGCGGTCCGA</u><br><u>CCTGGGCTACTTCGGTAGGCTAAGGCACAGTATGATGTTGTGAAGTGAAGGAGGATATAA</u><br><u>ATGAAACAGAACAAAGAACAG</u><br>TTAGTCAGTAAAGGTGAAGAATTATTTACCGGTGTTGTACCGATATTAGTCGAACTGGACG<br>GTGACGTAAACGGACATAAGTTCTCTGTAAGTGGAGAAGGTGAAGGGGATGCCACCTACGG<br>GAAATTGACGCTGAAATTTATTTGCACGACAGGGAAACTGCCAGTCCCCTGGCCTACTCTG<br>GTAACCACACTTACGTGGGGGGTTCAGTGCTTTGCACGCTATCCCGACCATATGAAGCAGC<br>ACGATTTTTTCAAATCTGCGATGCCGGAGGGCTATGTGCAAGAACGGACCATTTTCTTTAA<br>GGACGATGGTAACTATAAAACTCGCGCCGAAGTTAAATTTGAAGGTGACACTTTGGTCAAC<br>CGTATAGAACTGAAGGGGATAGATTTTAAGGAAGATGGTAATATCCTTGGTCACAAGTTGG<br>AATACAACTACATCAGCGATAATGTATACATCACAGCCGACAAGCAAAAAAACGGTATCAAA<br>GCAAACTTCAAAATACGTCACAACATCGAGGACGGTGGAGTCCAGCTGGCCGACCACTACC<br>AGCAGAACACCCCAATAGGCGACGGACCTGTTCTTCTGCCAGACAACCACTACCTTTCGAC<br>TCAATCAAAGCTTTCAAAGGATCCTAACGAGAAACGGGATCATATGGTGTTGCTTGAGTTC<br>GTTACGGCAGCTGGTATAACCTTGGGGATGGACGAACTTTACAAATAATAAAAAGCCCGGAT<br>AGCTCAGTCGGTAGAGCAGCGGCCGGTTGCCATGTGTATGTGGGCCAATCGTGGCGTGTCG<br>GCCTGCTTCGGCAGGCACTGGCGCCGCCCACATACTCTGATGATCCCCAATCGTAGCGTGTC<br>GGGGTGCGCTTGCACCCACTGGCGCTGGGATCATTCATGGCAACGGCCGCGGGTCCAGGGT<br>TCAAGTCCCTGTTCGGGCGCCA<br>*ataatcAGATAACAGATACttcgGtatctgttatctgttTTTTTTcAACAGATAGCCGCGttcgCGCGGCtatctgttTTTTTTt* |
| | G_1 | G{u1,rbs2} [s₄u], [], [R3 sfGFP tDF30PPr T7t] | <u>TTC**TAATACGACTCACTATA**GGGAGATTCGTCTCCCACTACATCCACA</u><br><u>TACTACCTCCTTTACTTCACATTCGGGTCGGCATGGCATGTGCACCTCCTCGCGGTCCGA</u><br><u>CCTGGGCTACTTCGGTAGGCTAAGGCACAGTATGATGTTGTGAAGTGAAGGAGGATATAA</u><br><u>ATGAAACAGAACAAAGAACAG</u><br>ATGAGCAAAGGTGAAGAACTGTTTACCGGCGTTGTGCCGATTCTGGTGGAACTGGATGGCG<br>ATGTGAACGGTCACAAATTCAGCGTGCGTGGTGAAGGTGAAGGCGATGCCACGATTGGCAA<br>ACTGACGCTGAAATTTATCTGCACCACCGGCAAACTGCCGGTGCCGTGGCCGACGCTGGTG<br>ACCACCCTGACCTATGGCGTTCAGTGTTTTAGTCGCTATCCGGATCACATGAAACGTCACG<br>ATTTCTTTAAATCTGCAATGCCGGAAGGCTATGTGCAGGAACGTACGATTAGCTTTAAAGAT<br>GATGGCAAATATAAAACGCGCGCCGTTGTGAAATTTGAAGGCGATACCCTGGTGAACCGCA<br>TTGAACTGAAAGGCACGGATTTTAAAGAAGATGGCAATATCCTGGGCCATAAACTGGAATAC<br>AACTTTAATAGCCATAATGTTTATATTACGGCGGATAAACAGAAAAATGGCATCAAAGCGAA<br>TTTTACCGTTCGCCATAACGTTGAAGATGGCAGTGTGCAGCTGGCAGATCATTATCAGCAGA<br>ATACCCCGATTGGTGATGGTCCGGTGCTGCTGCCGGATAATCATTATCTGAGCACGCAGACC<br>GTTCTGTCTAAAGATCCGAACGAAAAAGGCACGCGGGACCACATGGTTCTGCACGAATATGT<br>GAATGCGGCAGGTATTACGTGGAGCCATCCGCAGTTCGAAAAATAATATGCCCGGATAGCTC<br>AGTCGGTAGAGCAGCGGCCGGTTGCCATGTGTATGTGGGCCAATCGTGGCGTGTCGGCCTG<br>CTTCGGCAGGCACTGGCGCCGCCCACATACTCTGATGATCCCCAATCGTAGCGTGTCGGGGT<br>GCGCTTGCACCCACTGGCGCTGGGATCATTCATGGCAACGGCCGCGGGTCCAGGGTTCAAGT<br>CCCTGTTCGGGCGCCA<br>*ctagcataaccccttggggcctctaaacgggtcttgaggggttttttg* |

:::
::::

::::{tab-item} Overlap PCR
:::{table} DNA templates for assembling THE riboregulators with overlap PCR. **Bold** sequences indicate promoters. Underlined sequences indicate complementary regions for overlap PCR. *Italic* sequences indicate terminators.
:label: tbl:dna-assembly
:align: center

| **Component** | **Short name** | **Full name** | **Sequence** |
| --- | --- | --- | --- |
| 5' UTR | G_1 | G{u1,rbs2} [s₄u], [], [R3] | ataggagccgcgaagtctaacgctgctctgggctaactgtccgcatctagacttaactga<br>gatattaccatagatgactagccattcctctagatactacgactagcatacTTC**TAATACG<br>ACTCACTATA**GGGAGATTCGTCTCCCACTACATCCACATACTACCTCCTTTACTTCACATT<br>CGGGTCGGCATGGCATGTGCACCTCCTCGCGGTCCGACCTGGGCTACTTCGGTAGGCTAAGGC<br>ACAGTATGATGTTGTGAAGTGAAGGAGG<u>ATATAAATGAAACAGAACAAAGAACAG</u> |
| sCFP3A-PPr CDS | sCFP3A | sCFP3A tDF30PPr | <u>ATATAAATGAAACAGAACAAAGAACAG</u>TTAGTCAGTAAAGGTGAAGAATTATTTACCG<br>GTGTTGTACCGATATTAGTCGAACTGGACGGTGACGTAAACGGACATAAGTTCTCTGTAAGTG<br>GAGAAGGTGAAGGGGATGCCACCTACGGGAAATTGACGCTGAAATTTATTTGCACGACAGGGA<br>AACTGCCAGTCCCCTGGCCTACTCTGGTAACCACACTTACGTGGGGGGTTCAGTGCTTTGCACG<br>CTATCCCGACCATATGAAGCAGCACGATTTTTTCAAATCTGCGATGCCGGAGGGCTATGTGCA<br>AGAACGGACCATTTTCTTTAAGGACGATGGTAACTATAAAACTCGCGCCGAAGTTAAATTTGAA<br>GGTGACACTTTGGTCAACCGTATAGAACTGAAGGGGATAGATTTTAAGGAAGATGGTAATATCC<br>TTGGTCACAAGTTGGAATACAACTACATCAGCGATAATGTATACATCACAGCCGACAAGCAAAA<br>AAACGGTATCAAAGCAAACTTCAAAATACGTCACAACATCGAGGACGGTGGAGTCCAGCTGGCC<br>GACCACTACCAGCAGAACACCCCAATAGGCGACGGACCTGTTCTTCTGCCAGACAACCACTACC<br>TTTCGACTCAATCAAAGCTTTCAAAGGATCCTAACGAGAAACGGGATCATATGGTGTTGCTTGA<br>GTTCGTTACGGCAGCTGGTATAACCTTGGGGATGGACGAACTTTACAAATAATAAAAAGCCCGGA<br>TAGCTCAGTCGGTAGAGCAGCGGCCGGTTGCCATGTGTATGTGGGCCAATCGTGGCGTGTCGGC<br>CTGCTTCGGCAGGCACTGGCGCCGCCCACATACTCTGATGATCCCCAATCGTAGCGTGTCGGGGT<br>GCGCTTGCACCCACTGGCGCTGGGATCATTCATGGCAACGGCCGCGGGTCCAGGGTTCAAGTCCC<br>TGTTCGGGCGCCA*ataatcAGATAACAGATACttcgGtatctgttatctgttTTTTTTcAACAG<br>ATAGCCGCGttcgCGCGGCtatctgttTTTTTTt* |
| sfGFP-PPr CDS | sfGFP | sfGFP tDF30PPr | <u>ATATAAATGAAACAGAACAAAGAACAG</u>ATGAGCAAAGGTGAAGAACTGTTTACCGGCGTT<br>GTGCCGATTCTGGTGGAACTGGATGGCGATGTGAACGGTCACAAATTCAGCGTGCGTGGTGAAG<br>GTGAAGGCGATGCCACGATTGGCAAACTGACGCTGAAATTTATCTGCACCACCGGCAAACTGCCG<br>GTGCCGTGGCCGACGCTGGTGACCACCCTGACCTATGGCGTTCAGTGTTTTAGTCGCTATCCGGA<br>TCACATGAAACGTCACGATTTCTTTAAATCTGCAATGCCGGAAGGCTATGTGCAGGAACGTACGA<br>TTAGCTTTAAAGATGATGGCAAATATAAAACGCGCGCCGTTGTGAAATTTGAAGGCGATACCCTG<br>GTGAACCGCATTGAACTGAAAGGCACGGATTTTAAAGAAGATGGCAATATCCTGGGCCATAAACTG<br>GAATACAACTTTAATAGCCATAATGTTTATATTACGGCGGATAAACAGAAAAATGGCATCAAAGCG<br>AATTTTACCGTTCGCCATAACGTTGAAGATGGCAGTGTGCAGCTGGCAGATCATTATCAGCAGAAT<br>ACCCCGATTGGTGATGGTCCGGTGCTGCTGCCGGATAATCATTATCTGAGCACGCAGACCGTTCTG<br>TCTAAAGATCCGAACGAAAAAGGCACGCGGGACCACATGGTTCTGCACGAATATGTGAATGCGGCA<br>GGTATTACGTGGAGCCATCCGCAGTTCGAAAAATAATATGCCCGGATAGCTCAGTCGGTAGAGCAGC<br>GGCCGGTTGCCATGTGTATGTGGGCCAATCGTGGCGTGTCGGCCTGCTTCGGCAGGCACTGGCGCCG<br>CCCACATACTCTGATGATCCCCAATCGTAGCGTGTCGGGGTGCGCTTGCACCCACTGGCGCTGGGAT<br>CATTCATGGCAACGGCCGCGGGTCCAGGGTTCAAGTCCCTGTTCGGGCGCCA*ctagcatacccctt<br>GGGGCCTCTAAACGGGTCTTGAGGGGTTTTTTG* |

:::
::::

:::::

# Protocol

**Preparation of HBC620 Pepper dye stock solution**

*The HBC620 dye is not necessary to assess THE riboregulator
performance, but it does provide a measurement of transcription rate in
an experiment. It should only be included if the RNA component you are
testing encodes for the Pepper RNA aptamer, otherwise no signal will be
produced.*

1.  Centrifuge the tube containing lyophilized HBC620 dye to ensure all
    the dye is at the bottom of the tube.

2.  In a chemical fume hood, prepare a 10 mM stock solution by adding
    100 % DMSO to the HBC620 dye tube (273.6 µL DMSO per 1 mg of HBC620
    dye).

3.  Vortex thoroughly until dye is dissolved.

4.  Wrap tube in aluminum foil to prevent photobleaching.

5.  Store at -20°C when not in use.

**Preparation of the molecular beacon (optional)**

*The molecular beacon is not strictly necessary to assess THE
riboregulator performance, but it does provide a complementary
measurement to fluorescent protein expression for strand exchange and
can provide mechanistic insight. It is useful to include in experiments
in which translation is absent or inhibited, such as experiments in PURE
lacking ribosomes or elongation factors, as this enables measurement of
strand exchange without fluorescent protein production.*

1.  Centrifuge tubes containing lyophilized DNA to ensure all the DNA is
    at the bottom of the tube.

2.  Using nuclease free water, resuspend lyophilized DNA to 100 µM
    concentration (10 µL of water per 1 nmol of DNA).

3.  Vortex thoroughly until DNA is dissolved.

4.  In a 200 µL PCR tube, prepare 20 µM molecular beacon solution for
    thermal annealing ({ref}`tbl:molecular-beacon`).

5.  In a thermocycler, run the following thermal annealing protocol ({ref}`tbl:thermal-annealing`).

6.  Store annealed molecular beacon at -20°C when not in use.

:::::{tab-set}

::::{tab-item} Molecular Beacon Solution
:::{table} Molecular beacon solution.
:label: tbl:molecular-beacon
:align: center

| **Component** | **Volume** |
| --- | --- |
| Nuclease free water | 40 µL |
| 5x txn buffer | 20 µL |
| 100 µM R{x2}-F-2omR | 20 µL |
| 100 µM R{rbs2}-Q-2omR | 20 µL |

:::
::::

::::{tab-item}
:::{table} Molecular beacon thermal annealing protocol.
:label: tbl:thermal-annealing
:align: center

| **Step** | **Temperature** | **Time** | **Iterations** |
| --- | --- | --- | --- |
| Initial denaturation | 90°C | 5 min | 1 |
| 90°C to 80°C ramp | -1°C/min | 1 min | 9 |
| 80°C to 70°C ramp | -1°C/min | 1 min | 9 |
| 70°C to 60°C ramp | -1°C/min | 1 min | 9 |
| 60°C to 50°C ramp | -1°C/min | 1 min | 9 |
| 50°C to 40°C ramp | -1°C/min | 1 min | 9 |
| 40°C to 30°C ramp | -1°C/min | 1 min | 9 |
| 30°C to 20°C ramp | -1°C/min | 1 min | 9 |
| Hold | 4°C | Hold | 1 |

:::
::::

:::::

**Preparation of linear DNA templates**

*Linear PCR product templates are recommended as they are simpler to
work with and less prone to variability from prep to prep compared to
plasmid extractions. We also find that linear PCR product templates
produce higher fluorescent signals in PURE than plasmid templates.*

*Gene fragments containing full transcription units (spanning a promoter
sequence to terminator sequence) can be ordered (Tables 3 and 4) and PCR
amplified as shown in {ref}`tbl:pcr-solution-full` and {ref}`tbl:pcr-solution-overlap`. Alternatively, for THE riboregulator
gates, a single gene fragment spanning the N-terminal linker sequence to
the terminator sequence of the gate can be ordered and the 5' UTR and
promoter of the gate can be ordered separately and appended with overlap
PCR (Table 5). This reduces cost and increases flexibility as multiple
short 5' UTR sequences can be ordered and appended to the single protein
coding sequence. {ref}`tbl:pcr-thermal-cycling` shows how to set up the overlap extension PCR.*

1.  Prepare DNA templates:

    a.  If ordering DNA as gBlock gene fragments, resuspend DNA to 10
        ng/µL in nuclease free water.

    b.  If ordering DNA as eBlock gene fragments, the DNA will come at
        10 ng/µL in IDTE buffer and can be used directly.

2.  Prepare DNA primers:

    a.  Centrifuge tubes containing lyophilized DNA to ensure all the
        DNA is at the bottom of the tube.

    b.  Using nuclease free water, resuspend lyophilized DNA to 100 µM
        concentration (10 µL of water per 1 nmol of DNA).

    c.  Vortex thoroughly until DNA is dissolved.

3.  In a 200 µL PCR tube prepare PCR solution ({ref}`tbl:pcr-solution-full` and {ref}`tbl:pcr-solution-overlap`).

4.  In a thermocycler, run the following protocol ({ref}`tbl:pcr-thermal-cycling`). The same protocol can be used for single template PCR or overlap extension PCR.

5.  

6.  Purify the PCR products from the reactions with the PureLink PCR
    cleanup kit.

    a.  Add 300 µL of B2 buffer to PureLink column.

    b.  Add all 75 µL of PCR reaction the PureLink column and pipette
        mix with B2 buffer \~10 times.

    c.  Centrifuge PureLink column at 13000 rpm for 1 min, discard flow
        through

    d.  For overlap PCR products, a 300 µL wash with B3 buffer is
        recommended to remove short secondary products. DO NOT DO THIS
        FOR SHORT TEMPLATES THAT ENCODE INPUT RNAS or a lot of DNA will
        be lost.

        Add 300 µL of B3 buffer and repeat step c.

    e.  Add 650 µL Wash buffer to PureLink column and repeat step c.

    f.  Repeat step c. one more time to remove any residual Wash buffer

    g.  Add 35 µL of PureLink Elution buffer and let the column sit at
        room temperature for \~2 min.

    h.  Move PureLink column to a fresh collection tube and centrifuge
        at 13000 rpm for 1 min.

    i.  Save collection tube with eluted DNA.

7.  Measure the concentration of the purified PCR product using A260
    absorbance measurements (Nanodrop) or fluorogenic measurements
    (Qubit).

    a.  For PCR products we find these two measurements are fairly
        similar. Qubit measurements were used in our published work.

8.  Purified PCR products can be stored at -20°C when not in use.

:::::{tab-set}

::::{tab-item} PCR Solution
:::{table} PCR solution for DNA templates that contain full transcription units (promoter to terminator). See sequences in Table 3 and Table 4.
:label: tbl:pcr-solution-full
:align: center

| **Component** | **Volume** |
| --- | --- |
| Nuclease free water | 36.6 µL |
| 2x PCR master mix | 37.5 µL |
| 100 µM T7fwd primer | 0.375 µL |
| 100 µM Thyb10rev primer | 0.375 µL |
| 10 ng/µL DNA template | 0.15 µL |

:::
::::

::::{tab-item} PCR Solution Overlap
:::{table} PCR solution for overlap PCR to produce THE riboregulators by appending 5' UTR sequence to downstream protein coding sequence. See sequences in Table 5.
:label: tbl:pcr-solution-overlap
:align: center

| **Component** | **Volume** |
| --- | --- |
| Nuclease free water | 36.6 µL |
| 2x PCR master mix | 37.5 µL |
| 100 µM T7fwd primer | 0.375 µL |
| 100 µM Thyb10rev primer | 0.375 µL |
| 10 ng/µL 5' UTR template | 0.15 µL |
| 10 ng/µL CDS template | 0.45 µL |

:::
::::

::::{tab-item} PCR Protocol
:::{table} PCR thermal cycling protocol.
:label: tbl:pcr-thermal-cycling
:align: center

| **Step** | **Temperature** | **Time** | **Iterations** |
| --- | --- | --- | --- |
| Initial denaturation | 98°C | 5 min | 1 |
| Denaturation | 98°C | 30 s | 30 |
| Annealing | 60°C | 30 s | 30 |
| Extension | 72°C | 30 s | 30 |
| Final extension | 72°C | 3 min | 1 |
| Hold | 4°C | Hold | 1 |

:::
::::

:::::

**Preparation of plasmid templates**

Methods for plasmid extraction can be found in Ref 1. Additional details
on best practices for DNA plasmid preparation for cell-free expression
systems can be found in Ref 8.

To obtain similar results to linear templates with plasmid templates, we
have identified three crucial points:

1.  After plasmid extraction from cells a secondary PCR clean up should
    be performed on the plasmids (we use the PureLink kit specified in
    materials)

2.  We found high copy number plasmids produced results most comparable
    to linear templates. Low copy number plasmids (\~10 copies) deviated
    from linear template results even when using nominally the same
    concentrations.

3.  For plasmids Qubit concentration measurements are necessary to get
    close correlation to linear template results. Nanodrop measurements
    indicate much higher plasmid concentrations than Qubit measurements;
    this difference is not as great for linear templates.

**Kinetic plate reader experiments**

...Description...Keep constant total template concentrations across
samples you want to compare

1.  Remove PURExpress solution A and solution B from -80 ^o^C and thaw
    on ice.

2.  Thaw DNA templates (purified PCR products), annealed molecular
    beacon, and HBC620 stock solution at room temperature.

3. 

# Performance Data

:::{figure} ./general/image2.png
Kinetic results of a THE riboregulator cotranscribed with
input RNAs possessing *d* domains of increasing length. The fluorogenic
Pepper aptamer provides a measure of initial transcription rate of the
gate, the molecular beacon provides a measure of output RNA release, and
CFP provides a measure of translation rate from the gate in the ON
state.
:::

What's next...

<!-- **Papers**

1.  **DNA toehold-mediated strand exchange reactions:** \[Link: \]

2.  **THE riboregulators in cell-free expression systems:** \[Link:
    <https://www.biorxiv.org/content/10.1101/2025.09.25.678518v2.full>
    \]

3.  **THE riboregulators in bacteria:** \[Link:
    <https://www.biorxiv.org/content/10.1101/2025.09.24.678369v1.full>
    \]

4.  **Original description of ctRSD circuits:** \[Link:
    <https://www.science.org/doi/full/10.1126/sciadv.abl4354> \]

5.  **The ctRSD toolkit:** \[Link:
    <https://pubs.acs.org/doi/abs/10.1021/acssynbio.3c00079> \]

6.  **An alternative design for producing dsRNA gates:** \[Link:
    <https://pubs.acs.org/doi/abs/10.1021/acs.nanolett.0c03629> \]

7.  **Ribosome standby site and translation strength:** \[Link:
    <https://academic.oup.com/nar/article/42/4/2646/2435298> \]

8.  **Best practices for plasmid template extraction:** \[Link:
    <https://academic.oup.com/synbio/article/7/1/ysac015/6664141> \] -->



