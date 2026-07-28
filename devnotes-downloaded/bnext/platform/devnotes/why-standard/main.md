---
abstract: |
  Standards? They help compare data, which we really struggled with until we found the correct combination of fluorescein, careful pipetting, and wits.
---
<!-- Sensing and sense-ability 
Metaphor: how do we know we all have the same rulers?
-->

:::{topic} TL;DR
See our @recommendations for standards when using Cytosol with GFP as a reporter
:::

In the Nucleus Community, we're working on collaboratively solving hard problems at scale. Collaborators need to be able to compare experimental results with one another, to analyze data that's been collected across labs, and to make predictions that can be tested by others. Quantitatively, this means making measurements in comprehensible units. 

However, some measurements, like fluorescence, are made in arbitrary units that are instrument-specific. Additionally, ambient conditions can lead to fluorescence measurements of the same sample varying over time, even in the same instrument.

To make measurements from different instruments comparable, we will need to select standard units and a means of _calibrating_ each instrument—converting measurements from each instrument into standard units—that is robust to changing ambient conditions.


:::{seealso}
Make sure your data are correctly formatted for sharing. (link to platemap devnote)
:::

For fluorescence in particular, the issue is most salient when we are trying to use fluorescence as a proxy for concentration of a fluorophore reporter, like GFP. A straightforward approach to calibration is to measure the fluorescence of the reporter at a series of known concentrations—a standard curve—and fit a model. Then, when measuring fluorescence of a sample later on, you can invert the model to get an estimate of concentration. 

This approach does leave us some things to worry about. First, the accuracy of our model will depend on how well we can purify and quantify the reporter of interest. Next, our sample is usually a more complex system, like a PURE reaction that produces the reporter, with a different environment (i.e., pH) from the standards. So, the relationship between concentration and fluorescence for the samples will differ from the standard curve.

If there are changes in the instrument that cause the concentration-fluorescence relationship to change over time, then performing the calibration periodically will account for slow drift. But, if the measurement is highly sensitive between experiments, then we would need to plate some standard with every experiment. For a protein standard, this could be costly or difficult.

Another approach is to use a more accessible but different standard than the reporter of intrest, and measure concentration of the reporter in units of concentration of this standard. An ideal standard is something that is close to the reporter in measurement parameters, is stable over time, and is unlikely to be different across batches. 

For GFP, an easy-to-obtain small molecule standard with similar excitation and emission spectra is fluorescein. (Other similar standards have been proposed for other fluorescent color proteins.) Then, you just put fluorescein on every plate you run—it should account for changes in ambient conditions over time for the same plate reader, as we would expect these to affect both the samples and the fluorescein—and report sample fluorescence in units of fluorescein-equivalent concentration.[^mesf]

:::{hint} How to calculate fluorescein-equivalent concentration
:class: dropdown
:name: calculation
Here's a quick and dirty way:

**Calibration** (done periodically)
1. Measure the fluorescence of a fluorescein dilution series on your plate reader. 
2. For the usual gain settings on a plate reader, this will likely be a line.[^saturation] If so, fit a line. This is your standard curve.
3. Invert the standard curve.
   - For a line $F = mC + F_0$, where $F$ is raw fluorescence, $C$ is concentration, and $m$ and $F_0$ are the slope and bias parameters of the fit, the predicted concentration given fluorescence is $C = (F - F_0)/m$.
   - For a nonlinear curve, you can fit a different model; or make a finer dilution series and linearly interpolate between sample points. 

**Measurement**
1. Plate some replicates of fluorescein standard at a single known concentration with your experiment.
2. Invert the fluorescence of the fluorescein standards. Check that the predicted concentration is close to the actual. If not, check whether something went wrong with plating or aliquoting; you may have to recalibrate.
3. Put the fluorescence measurements of sample into the inverted standard curve to get estimates of concentration in fluorescein-equivalent units.
    - If you could fit the fluorescein dilution series with a line during calibration, and if $F_0$ is small enough to be neglible, then you can simply sample fluorescence by standard fluorescence to get concentration in units of the standard.

See @10.3389/fbioe.2023.1104445 for a more detailed model that provides uncertainty estimates.
:::

This still leaves the question of comparability between plate readers.[^igem-variance] Some difference is expected due to the different shapes of the emission spectra of fluorescein and GFP, which will lead to different interactions across plate reader lamp and optics types. 

We are in the process of thoroughly characterizing how well fluorescein can be used as a standard for GFP across our plate readers over time. While our preliminary results suggest there may be significant variability, it is still far less than the differences we see between the absolute levels of fluorescence between instruments. Therefore, for the time being we recommend reporting fluorescein-equivalent concentration, and stay tuned for further analysis and recommendations.

<!-- and between reaction volumes, maybe this is a later, deep dive devnote -->

:::{attention} Current recommendations
:name: recommendations
- Following the iGEM protocol [@10.17504/protocols.io.6zrhf56], we recommend including a few replicates of NIST-traceable sodium fluorescein on every plate you read fluorescence, and calculating fluorescein-equivalent concentration of all GFP samples.
- For Nucleus Cytosol and NEB PURExpress on our plate readers, we recommend 1 µM fluorescein.
- You can store aliquoted fluorescein in a –20 °C or –80 °C freezer.[^frozen] 
- Vortex thawed fluorescein aliquots for around 5 seconds before plating.[^not-vortexed]
- You may want to plot a fluorescein dilution curve to check whether your plate reader's gain and read height settings are appropriate.
:::

---



<!-- # What Standard
- It glows
- Fluorescein
- (d)eGFP

# How Standard
## How make
- Here is a recipe
- Here are tips to make it
- Here's what it looks like when you do

## How analyze
:::{tip}
Check out this example jupyter notebook!
:::

- Here is how you analyze data with standard
- Check out our CDK

# What's coming next for standard
- Perhaps there are more colors than just green
- Does it change over time?
- How stable are some standard curves?
- Would you like to help--reach out and send your standardized data. -->

# Further reading
- Standard curve in terms of fluorescent proteins directly: @10.1038/s41467-022-34232-6
- Normalization to another fluorophore (fluorescein or similar for other colors): @10.1371/journal.pone.0199432; @10.1093/synbio/ysac010; @10.1021/acssynbio.0c00296; @10.3389/fbioe.2023.1104445; @10.1021/acssynbio.5c00677; @10.17504/protocols.io.6zrhf56


[^mesf]: Also seen as MEFL [@10.1371/journal.pone.0199432; @10.17504/protocols.io.6zrhf56] or MESF [@10.1021/acssynbio.5c00677]
[^igem-variance]: The study by @10.1371/journal.pone.0199432 on data collected by 72 iGEM teams suggests a fairly large amount of variability between fluorescence measurements of GFP-producing _bacteria_ normalized to fluorescein and to OD.
[^frozen]: We are investigating if frozen aliquots degrade over time and how frequently they might need to be remade.
[^not-vortexed]: Our results suggest significant variability in fluorescence of fluorescein replicates when not vortexed.
[^saturation]: For one of our plate readers (a Cytation 3, only for the filter cube read) we noticed that fluorescence saturates as a function of concentration, which could be fit with a Michaelis-Menten-like curve.