---
# Ensure that this title is the same as the one in `myst.yml`
title: Nucleus OnePot PURE
abstract: |
  This DevNote describes a detailed protocol for producing the protein component of Nucleus OnePot PURE. The protocol does not include tRNA or ribosome purification steps. Starting from a 500 mL OnePot culture, the protocol yields approximately 600 µL of PURE at a protein concentration of 15 mg/mL. Functional testing shows that protein expression with OnePot PURE reaches ~65% of the final yield achieved by the PURExpress system, with a maximum expression rate (Vmax) of ~45% relative to PURExpress.
---

# Preliminary Work

DNA sequences of the expression plasmids used for the preparation of OnePot PURE are maintained in the [nucleus-eng/DNA](https://github.com/nucleus-eng/DNA/tree/f7654f79d032efe157940e9ae388f5d405dcb29c/PURE/expression) registry (`PURE/expression/`) rather than attached here. *E. coli* BL21(DE3) was used as the expression strain for all 36 PURE proteins in the protocol.

## Starter Plate Preparation

Prepare a OnePot PURE starter plate containing each of the 36 strains, stored as 25% glycerol stocks at an OD₆₀₀ of 0.5. Each well of the starter glycerol stock plate should contain 40 µL of the corresponding strain at OD₆₀₀ = 0.5 and be stored at −80 °C.

:::{figure} ./figures/platemap.jpg
:label: fig:OnePotPURE-platemap
:width: 75%
Plate layout of 40 µL PCR plate aliquots for the Nucleus OnePot PURE protocol.
:::


## Buffer Preparation

The following stock buffers are required for preparing the working buffers used in PURE production. At this stage, the solutions are not pH-adjusted, as pH adjustment will be performed during preparation of the working buffers (see below).

### 1M HEPES (250 mL)

1. Dissolve 59.6 g HEPES (MW 238.3 g/mol) in 200 mL dH₂O.
2. Adjust to a final volume of 250 mL.
3. Sterilize by autoclaving or filter sterilization.
4. Store at 4 °C with the bottle wrapped in foil to protect from light. Avoid storing HEPES for longer than one week; prepare only the amount required for the intended number of preparations.

### 1M Magnesium Chloride (250mL)

1. Dissolve 23.8 g MgCl₂ (MW 95.21 g/mol) in 200 mL dH₂O.
2. Adjust to a final volume of 250 mL.
3. Sterilize by autoclaving or filter sterilization.
4. Store at 4 °C for up to 6 months.

### 2M Potassium Chloride (250 mL)

1. Dissolve 37.3 g KCl (MW 74.55 g/mol) in 200 mL dH₂O.
2. Adjust to a final volume of 250 mL.
3. Sterilize by autoclaving or filter sterilization.
4. Store at 4 °C for up to 6 months.

Following are the working buffers required for PURE protein production:

### Buffer A (1 L)

1. Add 53.5 g NH₄Cl to a 1 L Duran bottle and dissolve in 500 mL dH₂O.
2. Add 50 mL of 1 M HEPES.
3. Add 10 mL of 1 M MgCl₂.
4. Bring the volume up to 1 L with dH₂O.
5. Adjust pH to ~7.6 using KOH pellets.
6. Label the bottle “Add TCEP” as a reminder.
7. Filter sterilize.
8. Store at 4 °C, wrapped in foil to protect from light; suitable for multiple preparations.
9. For experiments, use Buffer A to prepare resuspension, equilibration, wash, and elution buffers as required. Add TCEP to each at a final concentration of 1 mM immediately before use.

### Buffer B (500 mL)

1. Add 17 g imidazole to a 500 mL Duran bottle and dissolve in 300 mL dH₂O.
2. Add 25 mL of 1 M HEPES.
3. Add 5 mL of 1 M MgCl₂.
4. Add 25 mL of 2 M KCl.
5. Bring the volume to 490 mL with dH₂O.
6. Adjust pH to ~7.6 using HCl.
7. Bring the final volume to 500 mL with dH₂O.
8. Label the bottle “Add TCEP” as a reminder.
9. Filter sterilize.
10. Store at 4 °C, wrapped in foil to protect from light; suitable for multiple preparations.
11. For experiments, use Buffer B to prepare wash and elution buffers as required. Add TCEP to each at a final concentration of 1 mM immediately before use.

### Buffer HT (2 L)

1. Use a sterile 2 L Duran bottle and sterile (filtered) HEPES, MgCl₂, KCl, and water to avoid the need for filter sterilization.
2. Add 100 mL of 1 M HEPES.
3. Add 20 mL of 1 M MgCl₂.
4. Add 100 mL of 2 M KCl.
5. Add 1780 mL sterile dH₂O.
6. Label the bottle “Add TCEP” as a reminder.
7. Store at 4 °C, wrapped in foil to protect from light; suitable for multiple preparations.
8. For experiments, aliquot the required volume into a sterile container and add TCEP to a final concentration of 1 mM immediately before use.

### Stock 60 (100 mL)

1. Add 5 mL of 1 M HEPES (filtered) to a sterile 100 mL Duran bottle.
2. Add 1 mL of 1 M MgCl₂ (filtered).
3. Add 5 mL of 2 M KCl (filtered).
4. Add 60 mL of 100% sterile glycerol.
5. Add 29 mL sterile dH₂O.
6. Label the bottle “Add TCEP” as a reminder.
7. Store at 4 °C, wrapped in foil to protect from light; suitable for multiple preparations.
8. Prepare Stock 30 using Stock 60 before adding any reducing agent to Stock 60.
9. For experiments, aliquot the required volume and add TCEP to a final concentration of 1 mM immediately before use.

### Stock 30 (50 mL)

1. Add 25 mL of filtered Buffer HT (without reducing agent) to a sterile 100 mL Duran bottle.
2. Add 25 mL of filtered Stock 60 (without reducing agent).
3. Label the bottle “Add TCEP” as a reminder.
4. Store at 4 °C, wrapped in foil to protect from light; suitable for multiple preparations.
5. For experiments, aliquot the required volume into a sterile container and add TCEP to a final concentration of 1 mM immediately before use.

---

# Protocol

A single OnePot PURE system preparation requires processing 500 mL of liquid culture. It is recommended to process two 500 mL cultures simultaneously to generate two independent PURE batches in a single run. These can be quantified separately and combined if their activity levels are comparable.

This protocol processes two 500 mL OnePot PURE cultures, yielding ~600 µL purified PURE proteins per batch. The final stock concentration is 15 mg/mL.


## Day 1: Starter Culture

1. Starter culture incubation needs to begin at 6 pm. As such begin subsequent steps at 5 pm to allow sufficient time to start incubation at 6pm. 
2. Thaw a PURE Starter Plate on ice. This starter plate contains each of the 36 strains frozen in 25% glycerol at OD 0.5.
3. Add 50 µL 1000X Kanamycin (50 mg/mL) to 50 mL of sterile LB in a sterile falcon tube.
4. Label 1.5 mL sterile tubes from 1 to 36 (except number 25) and add 1 mL of LB+KAN to each tube.
5. Add 10 µL of each of the 36 glycerol stocks (except number 25) to the corresponding labeled tubes and mix well by vortexing.
6. Add 300 µL of innoculated cuture from each tube into the corresponding well of a sterile 96 deep well plate. Seal the plate using a Breath-easy sealing membrane. 
7. Innoculate 3 mL of LB+KAN in 15 mL falcon tubes with 10 µL of number 25 glycerol stock for EF-Tu. Do this in duplicate.
8. Incubate deep well culture plate and 15 mL falcon tubes at 260 RPM 37°C for 16 hours.
9. Start incubation at 6pm. Check OD₆₀₀ at 10 am the next day (16 hours incubation).
10. Place 1.5 L of sterile LB in 37°C static incubator to prewarm overnight.

## Day 2: Main Growth

11. The next day, measure the OD₆₀₀ of the starter plate using a 96 well plate by adding 30 uL of each starter  to the bottom of each well and 270 µL of LB+KAN on top (10X dilution). Measure EF-Tu culture density at this time too. Expected OD₆₀₀ with 10X dilution is 0.2 - 0.3.
12. After 16 hours of incubation, all strains should be at OD 2-3. If a strain is growing very slowly, remove the starter volume from the 96-deep well plate and place it into a 2 mL sterile tube, and shake at 260 RPM 37°C independently until desired OD is reached. The remaining starters can be left in the deep well plate on the bench. If a starter has overgrown above OD₆₀₀, dilute the starters to OD₆₀₀ = 3 using LB+KAN in a sterile tube.
13. Once all starter strains have been equilibrated to OD₆₀₀ 2-3, proceed to main growth by adding 500 mL of prewarmed LB+KAN into a 2.5 L baffled flask (2X flasks).
14. Into a sterile 5 mL tube add 55 µL of each starter culture (excluding EF-Tu), and 1675 µL of EF-Tu starter culture. Mix well by vortexing and add entire content to 500 mL of LB+KAN in 2.5 L baffled flask. Repeat for the second culture flask.
15. Incubate the cultures at 37°C 260 RPM for 1.5 to 2 hours (until OD₆₀₀ reaches 0.2 - 0.3). Check OD after 1 hour as baffled flask may cause cells to grow faster.
16. Once OD₆₀₀ of 0.2- 0.3 is reached, innoculate each culture flask with 500 µL of 100 mM IPTG to achieve a final induction concentration of 0.1 mM IPTG.
17. Incubate cultures for a further 3 hours at 37°C 260 RPM.
18. During incubation periods of main growth, prepare protein purification buffers as described below and store at 4°C until use. Don't add TCEP at this point.

:::{table} Protein Purification Buffers
:label: protein-buffers
:align: center
:width: 75%

| Buffer Type | Buffer A (mL) | Buffer B (mL) | Total (mL) | 0.5 M TCEP (µL) |
| --- | --- | --- | --- | --- |
| Resuspension/Equilibration Buffer | 200 | 0 | 200 | 400 |
| Wash Buffer  | 99 | 1 | 100 | 200 |
| Elution Buffer | 2 | 18 | 20 | 40 |  
:::

19. 15 minutes before the end of the incubation, cool table top centrifuge to 4°C and prepare an ice bucket and cool centrifuge bottles.
20. At the end of the 3 hour incubation, place baffled flask into ice bucket and remove samples for OD₆₀₀ measurement. Final expected OD₆₀₀ is 2-3.
21. Fill each centrifuge bottle with 500 mL of culture from each flask and spin at 5000g, 4°C, 15 minutes and discard supernatant.
22. Add 20 mL of sterile LB into each bottle and resuspend the cell pellet thoroughly and move resuspension into labelled sterile 50 mL falcon tubes.
23. Centrifuge the Falcon tubes at 4°C, 2000g for 8 minutes, remove the supernatant by decanting.
24. Centrifuge Falcon tubes at 4°C, 2000g again for 2 minutes, remove residual supernatant by pipetting.
25. The pellets can be flash frozen in liquid nitrogen and stored at -80 °C for up to 3 days until protein purification.

## Day 3: Protein Purification

26. Thaw cell pellets on ice.
27. Add 2 mL of fresh cOmplete resin to chromotography column. Wash column with 30 mL dH20 twice to remove ethanol.
28. Add TCEP to Resuspension/Equilibration buffer to a final concentration of 1 mM (see {ref}`protein-buffers`).
29. Equilibrate column with 30 mL of Resuspension/Equilibration buffer+TCEP and close vavle on the column with 5 mL of buffer remaining in the column.
30. Add 7.5 mL of Buffer A+TCEP to each falcon tube containing cell pellet and resuspend thorougly and store on ice.
31. Lyse cells via sonication at 70% amplitude, 10s on 10s off with 2000 J of energy in a ice water bath. Use a clamp stand to hold the falcon tube in place such that the cell suspension is submerged in the ice water bath and place the probe deep enough into the solution without touching the tube. If a large amount of foam is generated, the energy transfer will be damped. In that case, let the foam settle, lower the probe deeper into the solution, and extend the sonication time. If sonication is successful, the solution will turn darker.
32. Aliquot the sonicated sample in 2 mL tubes (1 mL per tube) and spin at 15923g, 4°C, 20 minutes.
33. Collate all clarified pellet free supernatant into a fresh 50 mL falcon tube on ice.
34. Resuspend the resin in the remaining 5 mL of Resuspension/Equilibration buffer+TCEP within the column and collate buffer+resin into falcon tube containing supernatant. Seal the lid with parafilm and incubate in a rotisseriie shaker at 4°C for a minimum of 3 hours.
35. After incubation of sample with resin, briefly spin the falcon tubes in a table top centrifuge using pulse mode to collate the resin to the bottom of the tube.
36. Resuspend the sample with resin using a pipette and add the mixture back into the protein purification column.
37. Label three 15 mL falcon tubes as 'flow through', 'wash' and 'elution', respectively. Replicate as required for the number of purifications you are doing.
38. Add TCEP at a final concentration of 1 mM to wash and elution buffers (see {ref}`protein-buffers`) and store at 4°C until use.
39. Once the resin has settled into a bed at the bottom of the column, let the buffer run through and collect samples from the middle of the flow through into 15 mL falcon tube labelled 'flow through'.
40. Wash column with wash buffer+TCEP and collect flow through in 15 mL falcon tube labelled 'wash'.
41. Add 5 mL elution buffer+TCEP into the column and resuspend the resin a few times with pipette and incubate for 10 minutes before elution into tube labelled 'elution'. During this incubation, add 1 L of Buffer HT+TCEP into a 1L beaker and soak 2kDA dialysis cassette in buffer with magnetic stirir in cold room/fridge.
42. Store eluted protein on ice.
43. Remove dialysis cassette from beaker and add 5 mL of eluted protein into the dialysis casssette. Remove as much air as possible from cassette before putting the lid back on. Dialyse according to protocol stated below to remove imidazole. 5 mL of eluted protein is dialysed against 1L of buffer HT (without TCEP) for 12 hours/overnight at 4°C. In instances when elutions can be combined, 10 mL of elution can be dialysed against 2L of buffer HT.

## Day 4: Protein Concentration

44. After dialysis is complete, remove dialysed sample from cassette and add to a 3K MWCO Amicon Ultra 15 and top up volume with 10 mL of fresh buffer HT+TCEP.
45. Spin at 3220 g for 60 mins at 4°C. The sample volume will reduce down to 1.5 mL.
46. Remove sample from amicon tube and split into 2 mL sterile tubes in 500 µL aliquots. Spin to pellet any precipitated proteins at 14,000g for 10 minutes at 4°C.
47. Collate pellet free supernantant into a fresh 1.5 mL tube on ice.
48. Add equal volume of Stock-60+TCEP to collated sample. Proceed to determine protein concentration using bradford assay in triplicate with a calibration curve spanning 0 - 2 mg/mL.
49. Concentrate protein down using 0.5 mL 3K amicon columns and spin at 14862g for 15 minutes at 4°C until desired volume is reached to obtain a final concentration of 15 mg/mL. 
50. Spin to pellet any precipitated proteins at 14,000g for 10 minutes at 4°C.
51. Determine final protein concentration and dilute samples with Stock 30 as required to reach correct final concentration of 15 mg/mL.
52. Aliquot 50 µL into PCR tubes, snap freeze using liquid nitrogen, and store at -80°C. 

# Representative Results

The purified OnePot PURE proteins along with Nucleus tRNA, and Nucleus Ribosomes were used to setup PURE reactions expressing deGFP using a pOpen-deGFP template. Composition of 3.33X SMixΔCP, including all small molecules required for in vitro transcription and translation, except creatine phosphate, is given in {ref}`SMix` below. A few different reaction compositions were tested to optimize the final protein yield from PURE cell-free reaction, which are described in the subsection below. A 35 μL mastermix was prepared for each reaction, and 10 μL aliquots were dispensed in triplicate into a 384-well plate for fluorescence measurements.

:::{table} SMixΔCP composition
:label: SMix
:align: center
| **Component** | **Concentration in SMixΔCP (mM) [3.33X]** |
| --- | --- |
| HEPES-KOH (pH 7.6) | 166.67 |
| Potassium glutamate | 333.33 |
| Magnesium acetate | 26.64 |
| rATP | 6.67 |
| rGTP | 6.67 |
| rCTP | 3.33 |
| rUTP | 3.33 |
| Amino acids (each) | 1 |
| Creatine phosphate (CP) | 0 |
| Folinic acid | 0.067 |
| Spermidine | 6.67 |
| TCEP | 3.33 |
:::

## Magnesium acetate titration

To assess the performance of OnePot PURE across varying magnesium acetate concentrations and identify optimal conditions, we performed a titration over a range of 8–14 mM in 2 mM increments. SMixΔCP already provides 8 mM magnesium acetate in the final reaction, anything above that concentration was added exogenously in the final reaction to reach the desired concentration in the final reaction. The base reaction composition for this experiment is given in table below. 

:::{table} Reaction composition: Mg2+ optimization
:label: RC1
:align: center
| **Component** | **Stock Concentration** | **Final Concentration in Reaction** | 
| --- | --- | --- |
| OnePot Proteins | 15 mg/mL | 2.4 mg/mL
| SMixΔCP | 3.33X | 1X |
| Ribosomes | 10 $\mu$M | 1.8 $\mu$M |
| tRNA | 35 mg/mL | 3.5 mg/mL |
| pOpen-deGFP | 124 | 3 nM |
| Magnesium acetate | 50 mM | *varies* |
| RNAse Inhibitor, Murine | 40000 U/mL | 2000 U/mL |
| Creatine phosphate | 1000 mM | 30 mM |
| PEG 8000 | 40% | 0 |
:::

Magnesium acetate titration showed that 14 mM yielded the highest deGFP production; higher concentrations were not tested. The OnePot PURE reaction with 14 mM Mg²⁺ achieved approximately 40% of the protein yield observed in the PURExpress positive control. Note: Kinetics measurements were initiated 20–25 minutes after reaction setup, which explains the apparent expression observed at timepoint 00:00.

:::{figure} ./experiments/20260120-OnePot-Opt1/g.png
:label: fig:opt1
:width: 75%
Magnesium optimization in OnePot PURE: 14 mM provided highest deGFP yield among the tested concentrations, ~40% of the PURExpress positive control. 
:::

## Addition of PEG-8000 improves the protein yield

PEG-8000 is widely used as an additive in cell-free reactions to introduce molecular crowding and enhance protein expression yields. Here, we included 2% PEG in the final reaction alongside an optimized 14 mM magnesium acetate concentration to test its effect on improving OnePot PURE yields. In separate reactions, the impact of supplementing additional ribosomes (2.4 µM) or tRNAs (4.5 mg/mL) was also tested under the same optimized 14 mM Mg²⁺ condition, but without PEG.

:::::{tab-set}
::::{tab-item} Reaction composition
:sync: tab1-1
:::{table} Reaction composition
:label: RC2
:align: center
| **Component** | **Stock Concentration** | **Final Concentration in Reaction** | 
| --- | --- | --- |
| OnePot Proteins | 15 mg/mL | 2.4 mg/mL
| SMixΔCP | 3.33X | 1X |
| Ribosomes | 10 $\mu$M | *varies* |
| tRNA | 35 mg/mL | *varies* |
| pOpen-deGFP | 124 | 3 nM |
| Magnesium acetate | 200 mM | 14 mM |
| RNAse Inhibitor, Murine | 40000 U/mL | 2000 U/mL |
| Creatine phosphate | 1000 mM | 30 mM |
| PEG 8000 | 40% | *varies* |
:::
::::

::::{tab-item} Description of experimental parameters
:sync: tab1-1
:::{table} Description of experimental parameters
:label: table-exp-para-1
:align: center

| Condition | Description |
| --- | --- |
| 14 mM Mg + 2% PEG  | Reaction using 2% PEG, 14 mM Mg-acetate, 1.8 uM Ribosomes, and 3.5 mg/mL tRNA  added in the final reaction |
| 14 mM Mg with 2.4 uM Ribo | Reaction using 14 mM Mg-acetate, 2.4 uM Ribosomes, and 3.5 mg/mL tRNA  added in the final reaction |
| 14 mM Mg with 4.5 mg/mL tRNA  | Reaction using 14 mM Mg-acetate, 1.8 uM Ribosomes, and 4.5 mg/mL tRNA  added in the final reaction |
:::
::::
:::::

:::::{tab-set}
::::{tab-item} Reaction Kinetics
:sync: tab2-1
:::{figure} ./experiments/20260121-OnePot-Opt2/g.png
:label: fig:opt2
:width: 75%
The addition of 2% PEG to the final reaction resulted in an approximately 50% increase in protein yield; however, no significant change in yield was observed with the addition of extra ribosomes or tRNAs.
:::
::::

::::{tab-item} Reaction Summary
:sync: tab2-2
:::{figure} ./experiments/20260121-OnePot-Opt2/summary_plot.png
:label: fig:opt2_summary
:width: 75%
The addition of 2% PEG to the final reaction resulted in an approximately 50% increase in protein yield; however, no significant change in yield was observed with the addition of extra ribosomes or tRNAs.
:::
::::
:::::

The results showed an approximately 50% increase in protein yield with the addition of 2% PEG-8000 compared to reactions without PEG. In contrast, no significant changes in protein yield was observed with the addition of extra ribosomes or tRNAs. Overall, combining 2% PEG with a final Mg²⁺ concentration of 14 mM enabled the OnePot PURE to achieve about 60% of the yield obtained with the PURExpress positive control.

## Testing higher concentrations of Ribosomes and Creatine Phosphate

Next, we evaluated the effect of increasing creatine phosphate from 30 mM to 40 mM on protein yield and also tested a higher ribosome concentration than previously examined. In this experiment, ribosomes were used at 3.24 µM.

:::::{tab-set}
::::{tab-item} Reaction composition
:sync: tab3-1
:::{table} Reaction composition
:label: RC3
:align: center
| **Component** | **Stock Concentration** | **Final Concentration in Reaction** | 
| --- | --- | --- |
| OnePot Proteins | 15 mg/mL | 2.4 mg/mL
| SMixΔCP | 3.33X | 1X |
| Ribosomes | 18 $\mu$M | 3.24 $\mu$M |
| tRNA | 35 mg/mL | 3.5 mg/mL |
| pOpen-deGFP | 124 | 3 nM |
| Magnesium acetate | 200 mM | 14 mM |
| RNAse Inhibitor, Murine | 40000 U/mL | 2000 U/mL |
| Creatine phosphate | 1000 mM | *varies* |
| PEG 8000 | 40% | 2% |
:::
::::

::::{tab-item} Description of experimental parameters
:sync: tab3-1
:::{table} Description of experimental parameters
:label: table-exp-para-2
:align: center

| Condition | Description |
| --- | --- |
| 14 mM Mg + 3.24 uM Ribo  | Reaction using 2% PEG, 14 mM Mg-acetate, and 3.24 uM Ribosomes  added in the final reaction |
| 14 mM Mg + 3.24 uM Ribo + 40 mM CP | Reaction using 2% PEG, 14 mM Mg-acetate, 3.24 uM Ribosomes, and 40 mM Creatine phosphate  added in the final reaction |
:::
::::
:::::


:::{figure} ./experiments/20260123-OnePot-Opt4/g.png
:label: fig:opt4
:width: 75%
The addition of 40 mM creatine phosphate or 3.4 µM ribosomes resulted in only a slight improvement (~5%) in protein yield compared to previous experiments {ref}`fig:opt2_summary`.
:::

The results showed only a slight improvement in protein yield (~5%) compared to the highest yield obtained in the previous experiment when higher CP and ribosome concentrations were tested. In summary, combining 2% PEG with a final Mg²⁺ concentration of 14 mM and a final ribosome concentration of 3.24 µM enabled OnePot PURE to achieve approximately 65% of the yield of the PURExpress positive control, with a maximum expression rate (Vmax) of ~45%. 

# Bill of Materials

:::{table} Critical Materials
:label: materials
:align: center
| Product | Manufacturer |
| --- | --- |
| BL21(DE3) Competent Cells | NEB (C2527H) |
| [Nucleus PURE DNA constructs](https://github.com/nucleus-eng/DNA/tree/f7654f79d032efe157940e9ae388f5d405dcb29c/PURE/expression) | b.next |
| Creatine phosphate | Sigma-Aldrich (27920) |
| *E. coli* Ribosomes |	b.next |
| *E. coli* tRNAs |	b.next |
| Magnesium acetate | Sigma-Aldrich (M5661) |
| [pOpen-deGFP DNA template](https://github.com/nucleus-eng/DNA/blob/f7654f79d032efe157940e9ae388f5d405dcb29c/reporters/pOpen-deGFP.gbk) | b.next |
| RNAse Inhibitor, Murine | NEB (M0314S) |
| 96-well Polypropylene DeepWell Plates | Nunc (260251) |
| Amicon Ultra 0.5 mL - 3 KDa | Merck Millipore (UFC500324) |
| Amicon Ultra 15 mL - 3 KDa | Merck Millipore (UFC900324) |
| Amino acids | Biotech Rabbit (BR1401801) |
| Ammonium chloride | Sigma-Aldrich (09718-1KG) |
| Breathe-Easy sealing membrane | Sigma-Aldrich (Z380059-1PAK) |
| Econo-Pac Chromatography Columns | Bio-Rad Laboratories (7321010) |
| EDTA (Ethylenediaminetetraacetic acid) | Sigma-Aldrich (03609-250G) |
| Folinic acid | Sigma-Aldrich (PHR1541) |
| Glycerol | Sigma-Aldrich (G5516-1L) |
| HEPES | Sigma-Aldrich (H3375) |
| Imidazole | Sigma-Aldrich (I2399) |
| IPTG | Thermo Scientific (R0392) |
| Magnesium chloride | Sigma-Aldrich (M2670) |
| Potassium chloride | Sigma-Aldrich (P5405) |
| Potassium glutamate | Sigma-Aldrich (49601) |
| PURExpress Kit | NEB (E6800L) |
| Rapid-Flow Sterile Single Use Vacuum Filter Units | Thermo Scientific (596-3320) |
| SealPlate film | Excel Scientific (Z369659-100EA) |
| Spermidine | Sigma-Aldrich (S2626) |
| TCEP | Thermo Scientific (77720) |
| Potassium hydroxide | Sigma-Aldrich (P1767) |
:::

# Conclusion

We have presented a comprehensive protocol for preparing a OnePot PURE protein mixture using Nucleus PURE Plasmids and the BL21(DE3) expression strain. The resulting mixture achieves a protein yield of 65% relative to PURExpress, with a maximum expression rate (V~max~) of approximately 45% of that observed with PURExpress. While the system does not match the performance of PURExpress or the Nucleus Cytosol, it nonetheless offers a practical and accessible starting point for researchers seeking to prepare their own PURE proteins without the need to purify each component individually, a process that is otherwise both time-consuming and technically demanding.