---
abstract: |
 Originally introduced by Roger Tsien and co-workers in 1982 as the premier ratiometric indicator for intracellular pH, the small molecule BCECF has been successfully adapted here to monitor extracellular cell-free microenvironments. In this work, we utilize its ideal physiological $$(pK_{a})$$ (~7.0) to achieve continuous, 24-hour kinetic tracking of metabolic acidification within dynamic myTXTL reactions. By optimizing this continuous kinetic workflow, we bridge historical fluorophore chemistry with modern automation to offer a standardized, high-precision pH measurement platform for the cell-free community
---

# Overview


We use the small molecule sensor [BECECF](fig:bcecf)  to measure pH in the myTXTL cell-free transcription translation system. The ratiometric fluorescent probe BCECF is widely employed for monitoring internal pH due to its pKa of approximately 7.0, which ensures high sensitivity within the physiological range [](https://doi.org/10.1083/jcb.95.1.189). By determining the ratio of fluorescence emission at 535 nm from dual excitation at 490 nm and 440 nm,  the pH can be measured independently of the absolute fluorescence intensity.

:::{figure} bcecf.png
:label: fig:bcecf
:width: 50%

The pH-sensitive molecule 2’,7’-bis-(2-carboxyethyl)-5-(and-6)-carboxyfluorescein acetoxymethyl ester (BCECF).
:::

# Reagents

:::{table}
:label: tbl:reagents
| **Name** | **Product** | **Manufacturer** | **Storage Conditions** | **Link** |
| --- | --- | --- | --- | --- |
| BCECF | BCECF, AM (2',7'-Bis-(2-Carboxyethyl)-5-(and-6)-Carboxyfluorescein, Acetoxymethyl Ester) | ThermoFisher (B1150) | -5C to -30C | [link](https://www.thermofisher.com/order/catalog/product/B1150) |
| myTXTL | myTXTL Pro Cell-Free Expression Kit | Arbor Biosciences (540300) | -85C to -75C | [link](https://arborbiosci.com/mytxtl-ga-2023/) |
| plates | 96 well-plates flat V-bottom | NEST (701211) | RT | [link](https://www.nestscientificusa.com/96-well-cell-culture-plate-flat-v-bottom-non-treated-sterile-individually-wrapped-in-peelable-film-1-pk-100-cs.html) |
| plate Mats | 96 well-plates Cap Mats | Thermo Fisher (276000) | — | [link](https://www.thermofisher.com/order/catalog/product/276000) |
| pH test strips | — | Sigma (1095350001) | — | [link](https://www.sigmaaldrich.com/US/en/product/mm/109535) |
:::

# Protocol

## Reagent Preparation
- Stock Solution: Resuspend the BCECF powder in MilliQ water to a final concentration of 10 mM.
- Working Solution: Dilute the stock solution in MilliQ water to reach a 100 µM concentration.
- Storage: Store both solutions at 4°C, protected from light.

## Prepare Calibration curve
The Calibration curve is made by preparing solutions of TXTL at different pH (6,7,8,9) with 10 uM of BCECF
- Thaw one tube of myTXTL on ice.
- The pH of myTXTL is around pH 8. Adjust the pH with either KOH or acetic acid. Because the reaction volume is very low, pH strips are recommended to measure the pH of the myTXTL solution.
-  Add the 100 µM BCECF solution to reach a final concentration of 10 µM.
-  Add AC water to complete the volume to 100%
-  -> Plate Loading and Measurement

## Sample Preparation (myTXTL Mix)
- Thaw one tube of myTXTL on ice.
- Add the DNA template to reach a final concentration of 5 nM.
- Adjust the volume with MilliQ water to reach 90% of the target final volume. 
- Add the 100 µM BCECF solution to reach a final concentration of 10 µM (completing the remaining 10% of the volume).
- Mixing: Mix gently by pipetting up and down.
- Once the BCECF and myTXTL are mixed, incubate the solution at 4°C for 10 minutes before loading it onto the plate.
- Centrifugation: Briefly spin down the tube to collect the mixture and remove air bubbles.

- Recover 20 uL of the reaction mixture to manually measure the pH with indicator strips at key milestones, specifically at tt0, 4 hoursours, and overnight, to independently validate the kinetic curve.

## Plate Loading and Measurement
- Dispense 2 µL of the mixture per well into a 96-well plate.
- Place the plate into the Neo2 plate reader.
- Kinetics Settings: Run a 24-hour kinetic assay with measurements every 3 minutes at gain 40 ms, bottom read.
- Fluorescence Parameters: Perform ratiometric imaging using the following excitation/emission pairs:
    - 440 nm / 520 nm
    - 490 nm / 520 nm 

## Data Analysis
- Process the raw fluorescence data by calculating the ratio of the two signals
- Convert the ratio values into pH measurements using a pre-established calibration curve.

# Performance

The sensor is first [calibrated](fig:ph-callbriation). This calibration curve allows us to [measure](fig:ph-vs-time) the pH of the myTXTL system over time.

# Tips and Tricks

- Keep the BCECF solution at 4C and protected from the light when you use it.
- BCECF may precipitate during storage. Gently warm the tube between your hands to fully resuspend the solution before pipetting.
- After mixing, inspect the tube closely to ensure no precipitate remains. The solution should appear completely clear and slightly yellow.
- We tested multiple plate geometries, including round-bottom and flat-bottom designs. Only V-bottom plates provided successful, reliable results. Please take this into consideration when ordering your consumables
- Mix gently by pipetting to avoid the formation of air bubbles
- Ensure the plate is sealed tightly and correctly; evaporation can occur over long kinetic runs, which will skew the final results.
-  If signal issues arise, begin troubleshooting by verifying the BCECF concentration. Run a preliminary validation test using well-characterized, standard reference buffers across the target pH range.
-  Ensure the BCECF solutions are split into small aliquots prior to storage
-  If expressing a reporter protein, ensure its excitation and emission spectra do not overlap with BCECF; for example, mCherry is an ideal candidate.
-  Ensure that the BCECF at this specific working concentration is non-toxic and does not inhibit the overall yield of your cell-free expression (CFE) system.
-  Dispense the 2 µL droplets as close to the center of the well bottom as possible to ensure optimal optical alignment and reproducible fluorescence readings
-  Carefully inspect the wells after the overnight incubation to ensure no liquid evaporation has occurred, as volume loss will invalidate the results


# Expected behavior

- The final myTXTL-BCECF mixture must remain completely clear throughout the assay.
- The 100 µM BCECF working solution should exhibit a distinct yellow color.
- You should expect a strong, stable fluorescent signal with no significant background noise or unexpected fluctuations throughout the kinetic assay.
- The calculated pH values obtained with BCECF must closely coincide with independent measurements from pH indicator strips
- Technical replicates across the 96-well plate should exhibit minimal variance, yielding tightly overlapping kinetic traces with low standard deviations
- Due to the heavy buffering capacity of the myTXTL system, the resulting kinetic curve should remain relatively flat over time.
- An evaporation loss of up to 10% is expected; if the volume loss exceeds this threshold, exclude the affected well from your analysis.
:::{table}
:label: tbl:well-conditions

| Well | Description |
| --- | --- |
| C4 | ?? |
| C5 | ?? |
| D4 | ?? |
| D5 | ?? |
| E4 | ?? |
| E5 | ?? |

:::

:::::{tab-set}

::::{tab-item} Calibration
:::{figure} #ph-callibration
:label: fig:ph-callbriation


This is the callibration curve
:::

::::

::::{tab-item} Measurement
:::{figure} #pH-vs-time
:label: fig:ph-vs-time
:::
::::
:::::

