---
# Ensure that this title is the same as the one in `myst.yml`
title: IV-HSL emitter cell
abstract: |
  The Emitter Cell is a synthetic cell that produces and releases the signaling molecule IV-HSL to communicate with E. coli bacteria, serving as a foundation for creating Responder Cells that can detect molecular inputs and amplify signals in co-culture systems.
---

# Overview

The Emitter Cell produces and releases a chemical signal molecule into the environment. This capacity provides an example of enzymatic small-molecule production, molecule release as a reporter output,  inter-cell communication, and co-culture of synthetic cells with living bacteria. The Emitter Cell is largely based on a paper by Jefferson M Smith, Denis Hartmann, and Michael J. Booth: [Engineering cellular communication between light-activated synthetic cells and bacteria](https://doi.org/10.1038/s41589-023-01374-7).

In this first Emitter, the cell produces and releases N-isovaleryl-L-homoserine lactone (IV-HSL). IV-HSL is a branched acyl-homoserine lactone with several advantages for use in the Emitter Cell: it is able to cross the synthetic cell membrane; its uncommon branched-chain structure makes it orthogonal from many other HSLs [Lindemann, 2011](https://doi.org/10.1073/pnas.1114125108); and it is able to activate expression in signal receiver cells (in this case, E. coli) at very low (picomolar) concentrations [Lindemann, 2011](https://doi.org/10.1073/pnas.1114125108). The IV-HSL signal is received by a population of E. coli cells, which respond by producing a fluorescent output.

The [Detector Cells](https://docs.nucleus.engineering/docs/modules/detector-tetr-atc/spec/) and Emitter together form the basis for an upcoming Responder Cell; a synthetic cell which can detect a molecular input (such as aTc or IV-HSL itself), and produce a molecular output (IV-HSL) in response. Coupling Detector and Emitter modules will enable signal amplification, where a low amount of a molecule of interest can activate a large population of Responder cells and generate an output that is easy to detect. IV-HSL-detecting Responder Cells could also detect the production of IV-HSL from living cells, providing a means to report on their state in co-culture.

:::{figure} ./data/emitter-cell-schematic.png
:label: fig1-emitter-cell-schematic
:width: 75%
Schematic of IV-HSL emitter cell.
:::



# Design

The Emitter Cell implements the [IV-HSL Emitter Module](https://docs.nucleus.engineering/docs/modules/emitter-ivhsl/spec/) within a synthetic cell. The Emitter Module produces the BjaI enzyme under the control of a constitutive T7 promoter. BjaI produces IV-HSL from two substrate molecules, S-adenosylmethionine (SAM) and isovaleryl coenzyme A (IV-CoA). IV-HSL diffuses out of the cell, through the lipid bilayer.

:::{figure} ./data/emitter-module-schematic.png
:label: fig1-emitter-module-schematic
:width: 50%

Schematic of IV-HSL emitter module.
:::

# Usage

## Protocol

This protocol reconstitutes the BjaI/BjaR quorum sensing components from *Bradyrhizobium japonicum* to establish IV-HSL-producing synthetic cells (emitters) and IV-HSL-responsive *Escherichia coli* cells (receivers), implementing the IV-HSL Emitter Cell.

BjaI is expressed inside Emitter Cells containing PURExpress to produce the enzyme BjaI from the template `pT7-bjaI`. BjaI will catalyze a reaction between the membrane impermeable IV-CoA and SAM substrates to yield membrane *permeable* IV-HSL.

*E. coli* cells expressing BjaR act as receiver cells, providing an easy means to detect IV-HSL production. When BjaR binds IV-HSL, expression of a fluorescent reporter gene controlled by a BjaR-regulated promoter is triggered.

Successfully built IV-HSL Emitter Cells will release IV-HSL and induce GFP expression in XL10-Gold cell with increasing green fluorescence over time.

There are five key stages to making the IV-HSL Emitter Cell:

:::{table}
:label: tbl:protocol-stages
| Step | Process | Hands-on Time | Total Time | Notes |
| --- | --- | --- | --- | --- |
| 1 | [**Pre-culture BjaR receiver cells**](#step-1) | 30 mins | 3.5 hr |  |
| 2 | [**Prepare lipids-in-oil solution, outer solution, and substrate stock solutions**](#step-2) | 1 hr | 4 h | Buffers and lipids may be prepared in advance and used for experiments on subsequent days. |
| 3 | [**Assemble PURE reactions**](#step-3) | 30 mins | 30 mins |  |
| 4 | [**Encapsulate liposomes**](#step-4) | 30 mins | 30 mins |  |
| 5 | [**Measure and image**](#step-5) | 30 mins | 6–12 h | Total time depends on the exact experiment and incubation conditions. GFP expression should be seen over the first 6 hours at 37C. |
:::

(step-1)=
### Step 1: Pre-culture BjaR receiver cells

1. Prepare glycerol stock of BjaR receiver cells
   - Transform XL-10 Gold competent *E. coli* with `bjaR-GFP-native`:
     - Add 1–5 µl containing 1 pg–100 ng of plasmid DNA `bjaR-GFP-native` to 50 µl of XL10-Gold cell mixture. Carefully flick the tube 4–5 times to mix cells and DNA. **Do not vortex.**
     - Place the mixture on ice for 15 minutes. Do not mix.
     - Heat shock at exactly 42°C for 40 seconds. Do not mix.
     - Place on ice for 5 minutes. Do not mix.
     - Pipette 950 µl of room temperature SOC into the cell mixture.
     - Shake the cell mixture vigorously (250 rpm) at 37°C for 60 minutes.
     - Warm Ampicilin LB agarose plates at 37°C for 10 mins.
     - Mix the cells thoroughly by flicking the tube and inverting, then perform several 10-fold serial dilutions in LB.
     - Spread 50–100 µl of each dilution onto a Ampicilin agarose plate and incubate overnight for ~15 hrs at 37°C.
2. Prepare a streak plate from the glycerol stock ([reference](https://www.addgene.org/protocols/streak-plate/))
   - Streak a Ampicillin LB plate from the glycerol stock and incubate overnight at 37C.
3. Prepare M9 Media containing 1× M9 salts, 0.34 mg/ml−1 thiamine hydrochloride, 0.2% casamino acids, 2 mM MgSO4, 100 µM CaCl2 and 0.4% (wt/vol) glucose.
4. Pick a colony from the *E. coli* streak plate, and inoculate a 5 mL culture tube containing the M9 media with 100 ug/mL carbenicillin.
5. Incubate the cells at 37 °C, 225 rpm, for 3 h. *Prepare Emitter liposomes while the cells incubate.*
6. Dilute the culture media with the pre-warmed M9 media until OD600 = ~0.1.
7. Balance osmolarity of the culture media with PURE (inner solution in liposomes) by adding glucose to the M9 media:

:::{table}
:label: tbl:osmolarity-balance
|  | Volume to mix (uL) |
| --- | --- |
| **M9 media** | 1000 |
| **3M Glucose** | 293.81 |
:::

(step-2)=
### Step 2: Prepare lipids-in-oil solution, outer solution, and substrate stock solutions

**Prepare lipids-in-oil (mineral oil) solution**

1. Clean glass syringes.
   - Pour a small amount of 95% ethanol into a glass container (e.g. a 10 mL beaker).
   - Assemble the glass syringe and prime it by drawing ethanol into the glass syringe, then empty into a waste bottle.
2. Use glass syringes to add lipids, as shown in the table below, into the 10 ml glass vial containing 1 ml of mineral oil (final lipid concentration is 5 mg/ml).

:::{table}
:label: tbl:lipids-in-oil
| Lipids | Stock Concentration (mg/mL) | Volume to add (uL) | Target percentage |
| --- | --- | --- | --- |
| **Egg PC** | 25 | 160 | 66.68 |
| **Cholesterol** | 50 | 20 | 33.32 |
| **18:0 Liss Rhod PE** | 1 | 5 | 0.01 |
:::

3. Heat the lipids-in-oil mixture on a hotplate at 55 C for 3 hrs.
4. Vortex the lipids-in-oil mixture for 1 min.

- The lipids-in-oil mixture can be stored at 4 C for up to 3 days.

**Prepare outer solution**

Final concentration of sugar stock solution is 900 mM

:::{table}
:label: tbl:outer-solution
| Buffer | Volume to add (uL) |
| --- | --- |
| **3M Glucose Stock** | 700 |
| **H2O** | 300 |
:::

**Prepare substrate stock solutions**

:::{table}
:label: tbl:substrate-stocks
| Substrate | Concentration (uM) | MW (g/mol) | Weight (g) | Final Volume (mL) |
| --- | --- | --- | --- | --- |
| **SAM** | 5000 | 398.44 | 1.99 | 1 |
| **IV-CoA** | 5000 | 851.65 | 4.26 | 1 |
| **IV-HSL** | 10 | 183.21 | 1.83 | 1 |
:::

(step-3)=
### Step 3: Assemble PURE Reactions

**PURE reaction setup**

:::{table}
:label: tbl:pure-reaction-setup
|  | Sample | Negative control | Positive control |  |
| --- | --- | --- | --- | --- |
| **Component** | **Volume (uL)** | **Volume (uL)** | **Volume (uL)** | **Notes** |
| PURE Solution A | 12 | 12 | 0 | PURE energy solution: small molecules |
| PURE Solution B | 9 | 9 | 0 | PURE proteins and ribosomes |
| RNAse Inhibitor | 1.5 | 1.5 | 0 | Prevents RNAse activity |
| [EM01-pOpen-pT7-BjaI](https://github.com/nucleus-eng/DNA/blob/bf9cfc08f1e1443f8185da24cf78467c67911766/detectors/quorum-sensing/pOpen-pT7-bjaI.gb) (~200 ng/uL) | 1.5 | 0 | 0 | DNA encoding green fluorescent protein |
| SAM (5mM) | 1.8 | 1.8 | 0 | Substrate for IV-HSL production. |
| IV-CoA (5mM) | 0.48 | 0.48 | 0 | Substrate for IV-HSL production. |
| OptiPrep | 1.5 | 1.5 | 1.5 | Adds density for phase-transfer |
| IV-HSL (10 uM) | 0 | 0 | 0.3 | Commercial IV-HSL for positive control. |
| 3M Glucose | 0 | 0 | 8.46 |  |
| ddH2O | 2.22 | 3.72 | 19.74 |  |
| **Total** | 30 | 30 | 30 |  |
:::

1. Thaw reagents on ice and then keep on ice.
2. Prepare a PCR strip in a strip holder on ice for assembly of the three reactions (Sample, Negative, Positive).

(step-4)=
### Step 4: Encapsulate PURE reactions into Liposomes

*Some tips and tricks can be found in PURE Cell.*

1. Set up a microfuge tube rack, with three 1.5 mL microfuge tubes per liposome encapsulation:
   - Number the tubes per the number of reactions assembled in Step 3.
   - For each reaction, label the two tubes:
     - **I** — Oil emulsion
     - **O** — Outer solution
2. Add 30 ul of PURE reactions prepared in **Step 3** to tubes labelled **I**.
3. Add 180 uL of the lipids-in-oil mixture on top of the PURE reactions in tubes labelled **I** and pipette vigorously until the emulsion becomes cloudy.
4. Add 300 uL of outer solution to each of the tubes labelled **O**.
5. Add 210 uL of the milky solution carefully on top of the outer solution in the tubes labelled **O.**
6. Centrifuge at 9000 rpm at 4c for 10 mins.
7. Remove the top oil and resuspend the pellet in 100 ul of outer solution.
8. Collect the liposomes.

(step-5)=
### Step 5: Measure and Image Liposomes and Cells

**Imaging using confocal microscopy (Operetta CLS):**

While microscopy setups may vary, our performance data was collected using the following configuration.

1. Add BjaR receiver cells prepared in Step 1 into 384 Well Glass Bottom Microplates.
2. Add 10 uL of liposomes made in Step 3 on top of the receiver cells in 384 Well Glass Bottom Microplates.
3. Imaging conditions using Operetta:
   - Temperature: 37 C degree
   - Green fluorescence channel (200 us expsoure 95%) - excitation: 460-490 nm; emission: 500-550 nm.
   - Red fluorescence channel (50 us exposure 95%) - excitation: 530-560 nm; emission: 570-650 nm.
   - Brightfield (20 us 95%)
   - We capture a 6 h time lapse with 10 min intervals.
   - We also acquired z-stack images spanning from 0 µm to 80 µm of the focal plane.

**Measuring usinng plate reader (BioTek Cytation 5):**

1. Add BjaR receiver cells prepared in Step 1 into 96 Well Glass Bottom Microplates.
2. Add 10 uL of liposomes made in Step 3 on top of the receiver cells in 96 Well Glass Bottom Microplates.
3. Procedures:
   - Temperature: 37 C degree
   - Read the fluorescence intensity from the bottom
   - Excitation wavelength: 485 nm ; Emission wavelength: 528 nm
   - We capture a 6 h time lapse with 5 min intervals

### Background Protocols

- Prepare lipids for use in encapsulation: [Lipid Preparation](https://docs.nucleus.engineering/docs/processes/assemble-base-cell/main/#prepare-lipids-in-mineral-oil)
- Prepare inner and outer buffers: [PURE inner and outer solution](https://docs.nucleus.engineering/docs/processes/assemble-base-cell/main/#assemble-outer-solutions)

### Resources and References

- **Papers**
  - Smith, J. M., Hartmann, D. & Booth, M. J. Engineering cellular communication between light-activated synthetic cells and bacteria. *Nature Chemical Biology* **19,** 1138–1146 (2023). [https://www.nature.com/articles/s41589-023-01374-7](https://www.nature.com/articles/s41589-023-01374-7)

## Modules

[IV-HSL Emitter Module](https://docs.nucleus.engineering/docs/modules/emitter-ivhsl/spec/)

## DNA Components

:::{table}
:label: tbl:dna
| **Name** | **Length (bp)** | **Description** | **Link** |
| --- | --- | --- | --- |
| `pT7-bjaI` | 2752 | _upcoming_. Expresses the BjaI enzyme to produce IV-HSL. | [pOpen-pT7-bjaI.gb](https://github.com/nucleus-eng/DNA/blob/bf9cfc08f1e1443f8185da24cf78467c67911766/detectors/quorum-sensing/pOpen-pT7-bjaI.gb) |
| `bjaR-GFP-native` | 3877 | _upcoming_. E. coli native receiver module; responds to IV-HSL by producing GFP. | [pOpen-bjaR-GFP-native.gb](https://github.com/nucleus-eng/DNA/blob/bf9cfc08f1e1443f8185da24cf78467c67911766/detectors/quorum-sensing/pOpen-bjaR-GFP-native.gb) |
:::

## Key Materials

:::{table}
:label: tbl:materials
| **Name** | **Product** | **Manufacturer** | **Part #** | **Price** | **Link** |
| --- | --- | --- | --- | --- | --- |
| ***Buffers*** |  |  |  |  |  |
| **Glucose** | D-(+)-Glucose, 99% | Thermo Scientific | A16828-36 | $41.65 | [[link](https://www.thermofisher.com/order/catalog/product/A16828.36)] |
| **Sucrose** | Sucrose, bioultra, for molecular biology, ≥99.5% (HPLC) | Sigma-Aldrich | 84097-1KG | $170.00 | [[link](https://www.sigmaaldrich.com/US/en/product/sigma/84097)] |
| ***Lipids*** |  |  |  |  |  |
| **Egg PC** | 25mg/mL | Avanti Lipids | 840051C-200mg | $186 | [[link](https://www.avantiresearch.com/en-gb/products/product/840051-egg-pc)] |
| **Cholesterol** | Cholesterol (plant) | Avanti Research | A80100 | $261.00 | [[link](https://www.avantiresearch.com/en-gb/products/product/700100-cholesterol-plant)] |
| **Liss-Rhod-PE** | 18:0 Liss Rhod PE 1 mg/mL | Avanti Lipids | A81179 | $273.47 | [[link](https://www.avantiresearch.com/en-gb/products/product/810179-180-liss-rhod-pe)] |
| **Mineral Oil** | Mineral oil, mixed weight | Thermo Scientific | AC415080010 | $53.40 | [[link](https://www.thermofisher.com/order/catalog/product/AC415080010)] |
| **Glass Syringe 250 uL** | Hamilton glass syringe | Hamilton | 14-815-238 | $150.15 | [[link](https://www.fishersci.com/shop/products/800-microliter-syringes-rn-termination/14815238)] |
| ***PURE*** |  |  |  |  |  |
| **PURE** | PURExpress® _In Vitro_ Protein Synthesis Kit | NEB | E6800L | $2774.00 | [[link](https://www.neb.com/en-us/products/e6800-purexpress-invitro-protein-synthesis-kit)] |
| **RNase Inhibitor** | RNase Inhibitor, Murine | NEB | M0314S | $87.00 | [[link](https://www.neb.com/en-us/products/m0314-rnase-inhibitor-murine)] |
| **DNA** | `pT7-bjaI` | b. next |  |  | [[link](https://github.com/nucleus-eng/DNA/blob/bf9cfc08f1e1443f8185da24cf78467c67911766/detectors/quorum-sensing/pOpen-pT7-bjaI.gb)] |
|  | `bjaR-GFP-native` | b.next |  |  | [[link](https://github.com/nucleus-eng/DNA/blob/bf9cfc08f1e1443f8185da24cf78467c67911766/detectors/quorum-sensing/pOpen-bjaR-GFP-native.gb)] |
| **OptiPrep** | OptiPrep™ | STEMCELL Technologies | 07820 | $289.00 | [[link](https://www.stemcell.com/products/optipreptm.html)] |
| **SAM** | S-adenosylmethionine (SAM) | NEB | B9003S | $45 | [[link](https://www.neb.com/en-us/products/b9003-s-adenosylmethionine-sam?srsltid=AfmBOoqDUA87yhYE4UrHnh7q8qMgLw8BGgGfFflrpBxYBfuL5juVceYZ)] |
| **IV-CoA** | Isovaleryl coenzyme A lithium salt hydrate | Millipore Sigma | I9381-10MG | $348 | [[link](https://www.sigmaaldrich.com/US/en/product/sigma/i9381)] |
| **IV-HSL** | 3-Methyl-N-[(3S)-tetrahydro-2-oxo-3-furanyl]butanamide | LGC | TRC-M282980-50MG | $171 | [[link](https://www.lgcstandards.com/US/en/p/TRC-M282980)] |
| **DMSO** | Dimethyl sulfoxide | Thermo Scientific | 042780.M1 | $342 | [[link](https://www.thermofisher.com/order/catalog/product/042780.M1?SID=srch-srp-042780.M1)] |
| ***Cell culture*** |  |  |  |  |  |
| **XL10-Gold Cells** | XL10-Gold Ultracompetent Cells | Agilent | 200314 | $223 | [[link](https://www.agilent.com/en/product/mutagenesis-cloning/competent-cells-competent-cell-supplies/competent-cells-for-difficult-cloning/xl10-gold-ultracompetent-cells-233087)] |
| **M9 Media** | M9, Minimal Salts, 5X, powder, minimal microbial growth medium | Sigma-Aldrich | M6030-1KG | $260 | [[link](https://www.sigmaaldrich.com/US/en/product/sigma/m6030)] |
:::

# Performance Data

Emitter Cells were constructed following  and co-cultured with E. coli containing the `bjaR-GFP-native` IV-HSL receiver plasmid. We performed time-series confocal microscopy (Revvity Operetta CLS) over 8 hours, collecting red (Rhodamine-B) and green (GFP) fluorescence, and brightfield images at 40x magnification across multiple fields per well, such that the entirety of each well was imaged. Timepoints were approximately 15 minutes apart.

## The Emitter Cell causes E. coli to express GFP in response to IV-HSL.

:::{iframe} https://www.youtube.com/embed/ylHokZo5Qrg?si=rLfGsJ2vJJB9s-sI
:width: 100%

*Emitter Cell Timeseries.* *(Positive)* Liposomes contain PURE and 100 nM IV-HSL. *(Negative)* Liposomes contain PURE supplemented with SAM and IV-HSL, but no DNA encoding BjaI. *(Emitter)* Liposomes contain PURE expressing BjaI from `pT7-bjaI`. Exposures are matched between wells. Each field of view is 167 uM wide.
:::

:::{figure} ./data/emitter-cell-all.png
:label: fig-emitter-cell-endpoint-montage.png

:::

## Liposomes exclude E. coli cells from the plate coverslip

:::{figure} ./data/emitter-cell-endpoint-montage.png
:label: fig-emitter-cell-endpoint-montage

*Emitter Cell Endpoint Montage.* Single field of view of Emitter Cell in co-culture with E. coli receiver cells at t = 8 hours. *(green)* E. coli producing GFP in response to IV-HSL emitted by the emitter cells. *(red)* Emitter cells with rhodamine-labeled membrane producing IV-HSL. *(grey)* Brightfield image of liposomes and E. coli cells. *(rgb)* Merged image.
:::

:::{figure} ./data/emitter-cell-endpoint-zstack.mp4
:label: vid-emitter-cell-endpoint-zstack

*Emitter Cell Endpoint Z-Stack.* Z-stack, single field of view of the Emitter Cell after the final timeseries timepoint (>8h). Liposomes preferentially form a layer on the surface of the cover slip, occluding many of the _E. coli_ cells from the bottom layer imaged during the timeseries. More activated _E. coli_ cells become visible at longer focal distances (higher in the liquid column of the well).
:::

# Credits

- Jefferson Smith & Michael Booth (Oxford / UCL)
- b.next
