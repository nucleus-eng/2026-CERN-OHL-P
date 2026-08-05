---
title: BCECF pH Sensor
abstract: |
  Originally introduced by Roger Tsien and co-workers in 1982 as the premier ratiometric indicator for intracellular pH, the small molecule BCECF has been successfully adapted here to monitor extracellular cell-free microenvironments. In this work, we utilize its ideal physiological $pK_a$ (~7.0) to achieve continuous, 24-hour kinetic tracking of metabolic acidification within dynamic myTXTL reactions. By optimizing this continuous kinetic workflow, we bridge historical fluorophore chemistry with modern automation to offer a standardized, high-precision pH measurement platform for the cell-free community.
---

<!--
TODO: Author's TODO, carried over from the source Google Doc (comment thread, Jon Calles → Daniel, 2026-07-22/27). Kept here verbatim as an open checklist for the author before this draft is publish-ready. Delete this block once resolved.

Daniel, please address the following items - Jon
- [ ] Respond to comments
- [ ] Fill out "Prepare Calibration Curve"
  - [ ] Description of method
  - [ ] Point out / upload supplementary files: raw data, plate map, analysis code
      NOTE: raw data, platemaps, and the ph_calibration.py/.ipynb analysis code
      have been copied into experiments/ms-ph_sensor/ as part of this ingest.
      One raw instrument export (2026_3_10 BCECF pH measurement Calibration.xlsx)
      could not be retrieved byte-for-byte during ingest; its computed
      ratio/pH values are preserved in
      experiments/ms-ph_sensor/2026_3_10-bcecf-calibration-results.csv.
      Re-fetch the original .xlsx from Drive if the raw instrument file itself
      is needed.

Open reviewer comments not yet addressed in the source (from Jonathan Calles
and Anton Molina, thread status OPEN as of 2026-07-27 unless noted):
- "this needs a longer explanation. 'Ratiometric' analysis is the core of
  this method, so explaining how it works is one of the key goals of this
  DevNote. Would benefit from one additional sentence in the Overview
  section." — see TODO flag in Overview below.
- "gain (typically) doesn't have units (milliseconds is incorrect) /
  typo: should be unitless" — see TODO flag in Plate Loading and
  Measurement below.
- "Ultrapure water? is brand name important here, or is any 18.2 MOhm water
  sufficient?" (reply: "resistivity is spec; brand name optional") — see
  TODO flag in Reagent Preparation below.
- "convention is to use degree sign, with space separating number and unit,
  e.g., 'store at 4 °C' ... NOTE: this comment applies manywheres, but only
  given here. apply fix throughout" (Anton: "We can run through our linter.
  Would be good to get that set up on the DevNotes repo") — applies
  throughout this draft; run `vale` per the style guide before publishing.
- "This section would benefit from a reaction assembly table. See example:
  Nucleus/Base Cell/Composition/Cytosol,
  https://docs.nucleus.engineering/docs/modules/base-cell/spec/" — see
  TODO flag in Sample Preparation below.
- "We have used tables like this to provide descriptions of figures. See
  example: https://devnotes.nucleus.engineering/articles/ppk-module-test"
  (Anton, re: the well-conditions table) — see TODO flag in Expected
  behavior below.
- "Fold this section together with # Expected Behavior (as it stands, this
  stub section isn't doing anything)" / "move below # Expected Behavior" —
  Jon's comments reference a stub section not present in the current
  document text pulled for this ingest; could not be located to action.
  Confirm with Jon which section this refers to.
-->

# Overview

We use the small molecule sensor BCECF ({ref}`fig:bcecf`) to measure pH in the myTXTL cell-free transcription-translation system. The ratiometric fluorescent probe BCECF is widely employed for monitoring internal pH due to its pKa of approximately 7.0, which ensures high sensitivity within the physiological range. By determining the ratio of fluorescence emission at 535 nm from dual excitation at 490 nm and 440 nm, the pH can be measured independently of the absolute fluorescence intensity.

<!-- TODO: the following two paragraphs both explain the same 490/440 ratiometric principle and appear to be a partially-merged draft revision (the source Google Doc contains both an unreferenced version and a referenced version back-to-back). Confirm with the author whether the first paragraph above should be removed once the citations below are retained, per Jon's open comment: "this needs a longer explanation. 'Ratiometric' analysis is the core of this method, so explaining how it works is one of the key goals of this DevNote. Would benefit from one additional sentence in the Overview section." -->

The ratiometric fluorescent probe BCECF is widely employed for monitoring internal pH due to its pKa of approximately 7.0, which ensures high sensitivity within the physiological range [[1](https://ionbiosciences.com/store/bcecf-am/), [2](https://pdfs.semanticscholar.org/abeb/116438515e303e6126b8726094ab38de2be6.pdf), [3](https://pubs.acs.org/doi/10.1021/jp0615712)].

Specifically, this ratiometric assay exploits the pH-dependent spectral shifts of the BCECF molecule. Excitation at 490 nm targets the base form of the dye, displaying a high fluorescence intensity that increases as pH rises. Conversely, excitation at 440 nm corresponds to the isosbestic point, where the fluorescence intensity remains unaffected by hydrogen ion concentration. By calculating the ratio of emission intensities (I₄₉₀/I₄₄₀), we obtain a normalized value that is directly proportional to the pH of the system. This ratio is then converted into absolute pH values using an *in situ* calibration curve, typically established via a nigericin-based potassium buffer system or standard pH-titrated cell-free matrices.

:::{figure} figures/bcecf.png
:label: fig:bcecf
:width: 50%
The pH-sensitive molecule 2',7'-bis-(2-carboxyethyl)-5-(and-6)-carboxyfluorescein acetoxymethyl ester (BCECF).
:::

# Reagents

:::{table}
:label: tbl:reagents
| Name | Product | Manufacturer | Storage Conditions | Link |
| --- | --- | --- | --- | --- |
| BCECF | BCECF, AM (2',7'-Bis-(2-Carboxyethyl)-5-(and-6)-Carboxyfluorescein, Acetoxymethyl Ester) | ThermoFisher (B1150) | -5C to -30C | [link](https://www.thermofisher.com/order/catalog/product/B1150) |
| myTXTL | myTXTL Pro Cell-Free Expression Kit | Arbor Biosciences (540300) | -85C to -75C | [link](https://arborbiosci.com/mytxtl-ga-2023/) |
| plates | 96 well-plates flat V-bottom | NEST (701211) | RT | [link](https://www.nestscientificusa.com/96-well-cell-culture-plate-flat-v-bottom-non-treated-sterile-individually-wrapped-in-peelable-film-1-pk-100-cs.html) |
| plate Mats | 96 well-plates Cap Mats | Thermo Fisher (276000) | — | [link](https://www.thermofisher.com/order/catalog/product/276000) |
| pH test strips | — | Sigma (1095350001) | — | [link](https://www.sigmaaldrich.com/US/en/product/mm/109535) |
:::

<!-- TODO: an open (unresolved) comment on the myTXTL storage condition proposes "store at -80 °C" in place of "-85C to -75C" — the source document overlays both the original range and a suggested edit without resolving which is correct. Confirm with the author before publishing, and apply the project's degree-sign convention (`°C` with a leading space) throughout this table. -->

# Protocol

## Reagent Preparation

- Stock Solution: Resuspend the BCECF powder in MilliQ water to a final concentration of 10 mM.
- Working Solution: Dilute the stock solution in MilliQ water to reach a 100 µM concentration.
- Storage: Store both solutions at 4°C, protected from light.

<!-- TODO: open comment — "Ultrapure water? is brand name important here, or is any 18.2 MOhm water sufficient?" (reply: "resistivity is spec; brand name optional"). Confirm whether "MilliQ water" should be replaced with a resistivity spec (18.2 MΩ·cm ultrapure water) throughout. -->

## Prepare Calibration curve

<!-- TODO: open comment (Jon Calles) — "This section is missing content. Can you describe how you prepared your pH calibration curve (stepwise bullets). can you also point out which supplementary files are associated with the calibration curve? (raw data, plate map, analysis code)". The bullets below are the author's in-progress response to this comment; the thread remains open as of the source document's last edit. Supplementary files for this section — 2026_3_10-bcecf-calibration-platemap.csv, 2026_3_10-bcecf-calibration-results.csv, ph_calibration.py, ph_calibration.ipynb — are in experiments/ms-ph_sensor/. -->

- The Calibration curve is made by preparing solutions of myTXTL at different pH (6, 7, 8, 9) with 10 µM of BCECF.
- Thaw one tube of myTXTL on ice.
- The pH of myTXTL is around pH 8. Adjust the pH with either KOH or acetic acid. Because the reaction volume is very low, pH strips are recommended to measure the pH of the myTXTL solution.
- Add the 100 µM BCECF solution to reach a final concentration of 10 µM.
- Add 18.2 MΩ water to complete the volume to 100%.
- Proceed to Plate Loading and Measurement.

TODO: "Is this done in aqueous?" — open question left by the author in the source document; unresolved.

## Sample Preparation (myTXTL Mix)

- Thaw one tube of myTXTL on ice.
- Add the DNA template to reach a final concentration of 5 nM.
- Adjust the volume with MilliQ water to reach 90% of the target final volume.
- Add the 100 µM BCECF solution to reach a final concentration of 10 µM (completing the remaining 10% of the volume).
- Mixing: Mix gently by pipetting up and down.
- Once the BCECF and myTXTL are mixed, incubate the solution at 4°C for 10 minutes before loading it onto the plate.
- Centrifugation: Briefly spin down the tube to collect the mixture and remove air bubbles.
- Recover 20 µL of the reaction mixture to manually measure the pH with indicator strips at key milestones, specifically at t0, 4 hours, and overnight, to independently validate the kinetic curve.

<!-- TODO: open comment — "This section would benefit from a reaction assembly table. See this example: Nucleus/Base Cell/Composition/Cytosol, https://docs.nucleus.engineering/docs/modules/base-cell/spec/". A Nucleus six-column composition table (Component | Input concentration | Unit | Final concentration | Unit | Volume) has not been authored here — the concentrations above are stated in prose only, and building the table is left to the author per their own open TODO. -->

## Plate Loading and Measurement

- Dispense 2 µL of the mixture per well into a 96-well plate.
- Place the plate into the Neo2 plate reader.
- Kinetics Settings: Run a 24-hour kinetic assay with measurements every 3 minutes at gain 40, bottom read.
- Fluorescence Parameters: Perform ratiometric imaging using the following excitation/emission pairs:
  - 440 nm / 520 nm
  - 490 nm / 520 nm
- Perform the ratiometric analysis as described below:
  - **Dual excitation:** Excite the sample sequentially at 490 nm (pH-sensitive) and 440 nm (pH-insensitive isosbestic point).
  - **Single emission:** Measure the fluorescence emission intensity at 535 nm for both excitation wavelengths.
  - **Ratio calculation:** Divide the emission intensity at 490 nm by the emission intensity at 440 nm.
  - **Calibration:** Convert the resulting ratio to absolute pH values using a standard calibration curve obtained with pH-calibrated myTXTL reactions.

<!-- TODO: open comment — "gain (typically) doesn't have units (milliseconds is incorrect) / typo: should be unitless". The source stated "gain 40 ms"; rendered here as unitless "gain 40" per that comment, but this has not been confirmed by the author — verify against the instrument protocol before publishing. -->

## Data Analysis

- Process the raw fluorescence data by calculating the ratio of the two signals.
- Convert the ratio values into pH measurements using a pre-established calibration curve.

# Results

The sensor is first calibrated ({ref}`fig:ph-calibration`). This calibration curve allows us to measure the pH of the myTXTL system over time ({ref}`fig:ph-vs-time`).

:::::{tab-set}
::::{tab-item} Calibration
:::{figure} #ph-callibration
:label: fig:ph-calibration
*In situ* pH calibration curve for BCECF in the myTXTL cell-free system. The fluorescence emission ratio (I₄₉₀/I₄₄₀) at 535 nm is plotted as a function of pH across a standard range (e.g., pH 6.0 to 8.0). Standard calibration samples were prepared by buffering the myTXTL cell-free system to known pH values. Data points represent the mean ± standard deviation (SD) of triplicate measurements. The solid line represents a mathematical fit used to convert experimental fluorescence ratios into absolute pH values.
:::
::::
::::{tab-item} Measurement
:::{figure} #pH-vs-time
:label: fig:ph-vs-time
TODO: no caption in source — this figure should show pH vs. time (the kinetic pH trace, converted from the fluorescence ratio via the calibration above) for the myTXTL/BCECF reactions; confirm caption with the author before publishing.
:::
::::
:::::

<!--
TODO: both figure directives above reference notebook-glue output (`#ph-callibration` — matches the notebook's misspelled `#| label: ph-callibration` in cell 9 verbatim, do not "fix" the spelling here without also renaming the notebook cell tag — and `#pH-vs-time`, matching cell 15's `#| label: pH-vs-time`) rather than a static image path. Once the analysis in experiments/ms-ph_sensor/ph_calibration.ipynb is finalized, consider either renaming the notebook's glue label to fix the typo (updating both sides together) or replacing these with static PNG file references (pattern 1) per the style guide.

TODO: computed calibration ratio-vs-pH values (pH 6.0–8.5, two replicates) are available in experiments/ms-ph_sensor/2026_3_10-bcecf-calibration-results.csv and correspond to the "Calibration" figure above.
-->

TODO: Conclusions section not present in source — add before publishing. A DevNote of this kind is expected to close with 2–4 sentences stating what was shown, its significance, and next steps (e.g., whether the calibration is validated for the kinetic myTXTL measurements above).

TODO: Specification section not present in source — add before publishing. Per the style guide, this should distill the key protocol parameters (BCECF/myTXTL concentrations, plate type, kinetics settings, excitation/emission pairs) a reader would need to reproduce the measurement.

# Tips and Tricks

- Keep the BCECF solution at 4°C and protected from the light when you use it.
- BCECF may precipitate during storage. Gently warm the tube between your hands to fully resuspend the solution before pipetting.
- After mixing, inspect the tube closely to ensure no precipitate remains. The solution should appear completely clear and slightly yellow.
- We tested multiple plate geometries, including round-bottom and flat-bottom designs. Only V-bottom plates provided successful, reliable results. Please take this into consideration when ordering your consumables.
- Mix gently by pipetting to avoid the formation of air bubbles.
- Ensure the plate is sealed tightly and correctly; evaporation can occur over long kinetic runs, which will skew the final results.
- If signal issues arise, begin troubleshooting by verifying the BCECF concentration. Run a preliminary validation test using well-characterized, standard reference buffers across the target pH range.
- Ensure the BCECF solutions are split into small aliquots prior to storage.
- If expressing a reporter protein, ensure its excitation and emission spectra do not overlap with BCECF; for example, mCherry is an ideal candidate.
- Ensure that the BCECF at this specific working concentration is non-toxic and does not inhibit the overall yield of your cell-free expression (CFE) system.
- Dispense the 2 µL droplets as close to the center of the well bottom as possible to ensure optimal optical alignment and reproducible fluorescence readings.
- Carefully inspect the wells after the overnight incubation to ensure no liquid evaporation has occurred, as volume loss will invalidate the results.

# Expected behavior

- The final myTXTL-BCECF mixture must remain completely clear throughout the assay.
- The 100 µM BCECF working solution should exhibit a distinct yellow color.
- You should expect a strong, stable fluorescent signal with no significant background noise or unexpected fluctuations throughout the kinetic assay.
- The calculated pH values obtained with BCECF must closely coincide with independent measurements from pH indicator strips.
- Technical replicates across the 96-well plate should exhibit minimal variance, yielding tightly overlapping kinetic traces with low standard deviations.
- Due to the heavy buffering capacity of the myTXTL system, the resulting kinetic curve should remain relatively flat over time.
- An evaporation loss of up to 10% is expected; if the volume loss exceeds this threshold, exclude the affected well from your analysis.

:::{table} Description of experimental wells
:label: tbl:well-conditions
| Well | Description |
| --- | --- |
| C4 | TODO: not filled in by author |
| C5 | TODO: not filled in by author |
| D4 | TODO: not filled in by author |
| D5 | TODO: not filled in by author |
| E4 | TODO: not filled in by author |
| E5 | TODO: not filled in by author |
:::

<!-- TODO: table cells above were "??" placeholders in the source, unfilled by the author. Anton Molina's open comment suggests this Nucleus format for describing figures/wells: https://devnotes.nucleus.engineering/articles/ppk-module-test — confirm the well descriptions with the author before publishing. -->
