---
title: Intro to Kinetics Analysis of Plate Reader Experiments
abstract: |

  Cell-free expression reactions are usually scored by a single endpoint fluorescence reading — simple to run, hard to interpret, and almost impossible to compare across labs. Watching the reaction unfold as a **timeseries** gives richer data, but that richness becomes useful once you can summarize a trace in a handful of interpretable numbers. This primer explains why we prefer timeseries measurements over endpoints, and shows how the Cell Development Kit (CDK) fits a logistic-with-drift model to plate-reader traces to extract steady-state yield, reaction rate, time-to-steady-state, and a drift correction. Along the way it flags the pitfalls that motivate the more careful treatment coming in Kinetics 102.
---

  Cell-free expression reactions are usually scored by a single endpoint fluorescence reading — simple to run, hard to interpret, and almost impossible to compare across labs. Watching the reaction unfold as a **timeseries** gives richer data, but that richness becomes useful once you can summarize a trace in a handful of interpretable numbers. This primer explains why we prefer timeseries measurements over endpoints, and shows how the Cell Development Kit (CDK) fits a logistic-with-drift model to plate-reader traces to extract steady-state yield, reaction rate, time-to-steady-state, and a drift correction. Along the way it flags the pitfalls that motivate the more careful treatment coming in Kinetics 102by measuring how much fluorescent protein it can make. Fluorescence is roughly proportional to reporter concentration, which makes steady-state fluorescence a simple and effective readout of total expression capacity.****different samples have the same endpoint fluorescence,th steady state twice as fast as the other? Endpoints can't tell you, and different labs makin different choices about incubation time produce results that look comparable but aren't.ostsamplesreading, which means observing the reaction as it runs is almost free. These **timeseries measurements** answer the questions endpoints can't, at the cost of a little more processing on the bac end. We think that trade is worth makand the rest of this DevNote is the case for hy
We've found that a quick way notice something is wrong with a reaction is to look at a fluorescence-versus-time plot. We've found some strange behaviors that would otherwise be hidden in a simple barplot of endpoints. For instance:

- Reactions that reach steady state and then **drift** slowly up or down: we suspect evaporation or incomplete sealing, but the cause matters less right now than the observation that ignoring drift can inflate or deflate apparent yield by tens of percent.
- Reactions that reach the **same steady state at different times**, which looks identical at endpoint but represents genuinely different underlying kinetics.
- **Biphasic traces** — an initial fast expression phase followed by a slower second one. This may reflect NTP depletion and re-phosphorylation, or some other resource-switching mechanism we don't yet fully understand. These are exactly the kind of observations that motivate mechanistic modeling, and they are completely invisible in an endpoint assay.

**Quantitative modeling needs the whole curve.** Those qualitative observations only become quantitative claims when you can fit them. As the Nucleus Community grows and more groups share cytosol data, information-dense timeseries will compound in value in a way that endpoints never will. You can always throw away the timepoints and recover an endpoint from a timeseries, but you can't go the other direction. We strongly encourage collecting timeseries now, even if you aren't ready to analyze them yet, so the data is there when the tools catch up.

-- JON WHAT DO YOU THINK OF THE ABOVE? I tried to clean it up but didnt want to delete since iM not sure if I like my version. aquick represent
A timeseries is a rich object: every trace is shaped by real reaction kinetics including transcription, translation initiation, fluorophore maturation, resource depletion, degradation — layered on top of instrument effects like evaporation and photobleaching. The goal of fitting is *not* to replace that richness with four numbers. The goal is to produce a compact, comparable summary of the curve that captures the features you want to reason about, while flagging the cases where a simple summary isn't enough and a richer model is warranted. It is also how we turn plate-reader output into units that travel: numbers you can put in a table, plot against a design variable, hand to a modeler, or publish in a DevNote alongside standards-normalized concentrations.
Wcytosol reactions are well approximated by a  sigmoid with a linear drift term. It approximates the following phases of cytosol reactions: 

1. **Lag.** Transcription, translation initiation; signal is flat or nearly so.
2. **Rise.** Protein accumulates approximately linearly; the slope near the inflection point is the phenomenological "Vmax" we report.
3. **Steady State.** Energy runs out, waste accumulates, the reporter plateaus. [JON PLEASE EDIT THIS]

A misbehaving trace adds a fourth phase:

4. **Drift.** Evaporation or lid condensation pulls signal up over time after the reaction has effectively finished. 

These four quantities are what the CDK currently aims to characterize, and the rest of this primer is about how it gets there and how to read the output.

## The model the CDK uses

We separate out the above phases by the "sigmoid drift" equation. Lauvel

where:
| Symbol | Name | What it tells you |
|---|---|---|
|$F_{ss}$ | asymptote | the fluorescence at steady state before drift |
| `k` | steepness | how fast the reaction crosses its midpoint |
| $\tau_{vel}$  | inflection time | when the reaction is at half-max |
| `d` | drift slope | rate of post-saturation drift (ideally ≈ 0) |
| $\tau_{drift}$| drift onset | time when drift starts contributing |


In addition to the above parameters, we also report three derived quantities: 

- **Vmax (phenomenological)** — the maximum slope of the sigmoid, which occurs at $\tau_{vel}$ and equals $A k / 4$. This is *not* the Michaelis–Menten $V_{\max}$; it is a single scalar summary of the steepest part of the accumulation curve. When comparing across conditions, prefer reporting `k` directly; report $Ak/4$ only when you need a slope-with-units for a downstream calculation.
- **Time-to-steady-state** — the time at which the sigmoid reaches a chosen fraction $\alpha$ of its asymptote (default $\alpha=0.95$), solved from the sigmoid as
  $$
  t_\alpha \;=\; t_0 + \frac{1}{k}\ln\!\left(\frac{\alpha}{1-\alpha}\right).
  $$
  Drift is intentionally excluded from this calculation — "when did the reaction finish" should not depend on how badly the plate was evaporating afterward.
- T-lag
  

or before drifthow fast the reaction crosses its midpoint\tauvel.)when drift starts contributing.teadystate| Parameter                 | Symbol         | Units            | Description                                                                                                                                                                                                                                                                      |
| ------------------------- | -------------- | ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Steady State Fluorescence | $F_{ss}$       | fluorescence units ($u$)              | How much total protein is expressed over the whole reaction? Fit explicitly in the model above.                                                                                                                                                                                  |
| Time to Steady State      | $\tau_{ss}$    | time (typically $h$)              | How long does it take for the reaction to reach steady state?                                                                                                                                                                                                                    |
| Lag Time                  | $\tau_{lag}$   | time (typically $min$)              | How long does it take for the reaction to start? This is roughly correlated with transcription lag time + translation lag time + maturation time of GFP. We calculate this as the x-intercept of the line tangent to the inflection point on the sigmoid |
| Maximum Velocity          | $V_{max}$      | fluorescence over time ($u \cdot h^{-1}$) | How fast is GFP getting produced at the fastest production rate in the reaction? This is the velocity of the reaction at $\tau_{max}$ and the slope of the line tangent to the inflection point and equals $F_{ss} * k / 4$^*                                 |
| Drift Rate                | $d$            | fluorescence over time ($u \cdot h^{-1}$) | If the reaction shows drift after steady state, how fast does it drift?                                                                                                                                                                                                          |
| Drift Onset Time          | $\tau_{drift}$ | time (typically $h$)              | If the reaction shows drift after steady state, when does it start to drift?                                                                                                                                                                                                     |

Notably, we have three derived quantities 
- insert box I sent you here? [Jon]
 in practice
This primer assumes you already have:

- a plate-reader export the CDK can ingest (BioTek, Cytation, or Envision; see [`cdk.instrument.platereader`](https://github.com/bnext-bio/bnext/tree/main/cdk/src/cdk/analysis/cytosol)),
- a platemap that labels each well with a condition (see the *Why you should use a platemap* DevNote),
- at least one fluorescent standard on the plate (see the *Why you should use standards* DevNote).

If any of those is missing, fix that first — fitting a curve to uncalibrated, unlabeled data just produces better-looking garbage. (JON: too hot of a take? haha pls feel free to remove)

- Look at this notebook
- Here are the plots you get

The minimum viable call is:

```python
from cdk.analysis.cytosol import platereader as pr

data = pr.load_platereader_data(
    path="20260416-my-experiment/",
    platemap="platemap.csv",
)

pr.plot_kinetics(data, fit_function_name="sigmoid_drift")
```

That produces, per condition group, (a) the overlaid raw traces with the fit, (b) a summary plot of `A`, `Vmax`, and `t_α`, and (c) a tidy DataFrame of fit parameters

**Default worth knowing.** The CDK currently defaults to fit_function_name="sigmoid_drift". If you truly dont want drift modeled, call "sigmoid"

# Common pitfalls

**Truncated saturation.** If the reaction hasn't actually plateaued by the last time-point, `A` is unconstrained and the optimizer will cheerfully return a garbage fit with small residuals. We are working on building checks for this.

**Reporting uncalibrated RFU.** `A` is in the reader's native fluorescence units until you normalize by a standard. For within-plate comparisons this is sub-par; for anything that leaves the plate, apply the standards pipeline first.

## When the sigmoid isn't enough

The sigmoid is a *phenomenological* fit: it is good at summarizing a well-behaved trace in four numbers, and bad at everything else. Specifically, it cannot represent:

- asymmetric rise/fall (use Gompertz or a generalized sigmoid),
- a biphasic reaction where a module kicks in mid-run (e.g., ClpXP-mediated degradation catching up to production),
- explicit resource-exhaustion dynamics that a mechanistic model could represent.



#Our next Kinetics DevNote will cover how to select among these fits, how to report **credible intervals** on `A`, `Vmax`, and `t_α` instead of point estimates. 
- Confidence intervals 


# Cytosol measurements: endpoints vs timeseries
We test our cytosol by measuring how much fluorescent protein it can make. Fluorescence is roughly proportional to reporter concentration, which makes steady-state fluorescence a simple and effective readout of total expression capacity.

The simple **endpoint measurement** is the easiest version of this assay. Just incubate your reactions until completion (at least 2 hrs) and measure the fluorescence. However, some complications make endpoint measurements hard to compare across labs, or even across your own experiments. Is 4 hrs enough? Does the fluorescence change after 16 hrs, or even more? If two different samples have the same endpoint fluorescence, did they behave identically, or did one reach steady state twice as fast as the other? Endpoints can't tell you, and different labs making different choices about incubation time produce results that look comparable but aren't.

Most plate readers can incubate samples while reading, which means observing the reaction as it runs is almost free. These **timeseries measurements** answer the questions endpoints can't, at the cost of a little more processing on the back end. We think that trade is worth making, and the rest of this DevNote is the case for why.

# Why timeseries?
We've found that a quick way notice something is wrong with a reaction is to look at a fluorescence-versus-time plot. We've found some strange behaviors that would otherwise be hidden in a simple barplot of endpoints. For instance:

- Reactions that reach steady state and then **drift** slowly up or down: we suspect evaporation or incomplete sealing, but the cause matters less right now than the observation that ignoring drift can inflate or deflate apparent yield by tens of percent.
- Reactions that reach the **same steady state at different times**, which looks identical at endpoint but represents genuinely different underlying kinetics.
- **Biphasic traces** — an initial fast expression phase followed by a slower second one. This may reflect NTP depletion and re-phosphorylation, or some other resource-switching mechanism we don't yet fully understand. These are exactly the kind of observations that motivate mechanistic modeling, and they are completely invisible in an endpoint assay.

**Quantitative modeling needs the whole curve.** Those qualitative observations only become quantitative claims when you can fit them. As the Nucleus Community grows and more groups share cytosol data, information-dense timeseries will compound in value in a way that endpoints never will. You can always throw away the timepoints and recover an endpoint from a timeseries, but you can't go the other direction. We strongly encourage collecting timeseries now, even if you aren't ready to analyze them yet, so the data is there when the tools catch up.

-- JON WHAT DO YOU THINK OF THE ABOVE? I tried to clean it up but didnt want to delete since iM not sure if I like my version. 
Why do we prefer timeseries over endpoints? 

First, we've found that a quick way to diagnose if our reactions are running correctly is visually inspecting fluorescence vs time graphs. We've found some strange behaviors that would otherwise be hidden in a simple barplot of endpoints. 

For instance, some reactions reach steady state then start to drift higher or lower slowly over time. We don't know why this happens -- e.g., perhaps if the well is not fully sealed, evaporation may affect readings? -- but not accounting for drift can artificially inflate or deflate estimates of total protein expression. We have also seen two reactions that reach the same steady state, at different times. 

(We've also seen more complex behavior that motivates new mechanistic models, like "biphasic" timeseries with an initial fast expression phase followed by a slow one. Are our reactions running out of NTPs and waiting for them to get re-phosphorylated?  -- Jon: we can omit this more advanced example, but it more strongly motivates modeling, I think)

These nuances would be missed in an endpoint measurement. 

Second, these qualitative observations can only be quantitatively modeled with timeseries data. As the Nucleus Community grows and we have more people sharing data and using that data to study how cytosol works, we believe that these more information-rich datasets will become increasingly valuable. Thus, we encourage everyone to take timeseries of their experiments now so that we can learn more from them in the future.


# How do we represent timeseries data?
A timeseries is a rich object: every trace is shaped by real reaction kinetics including transcription, translation initiation, fluorophore maturation, resource depletion, degradation — layered on top of instrument effects like evaporation and photobleaching. The goal of fitting is *not* to replace that richness with four numbers. The goal is to produce a compact, comparable summary of the curve that captures the features you want to reason about, while flagging the cases where a simple summary isn't enough and a richer model is warranted. It is also how we turn plate-reader output into units that travel: numbers you can put in a table, plot against a design variable, hand to a modeler, or publish in a DevNote alongside standards-normalized concentrations.

(ACJS: can you write a small blurb on the NIST workshop bit? I can't represent this myself - Based on NIST workshop and other conversations)
  
We find that much like bacterial growth curves, cytosol reactions are well approximated by a  sigmoid with a linear drift term. It approximates the following phases of cytosol reactions: 

1. **Lag.** Transcription, translation initiation; signal is flat or nearly so.
2. **Rise.** Protein accumulates approximately linearly; the slope near the inflection point is the phenomenological "Vmax" we report.
3. **Steady State.** Energy runs out, waste accumulates, the reporter plateaus. [JON PLEASE EDIT THIS]

A misbehaving trace adds a fourth phase:

4. **Drift.** Evaporation or lid condensation pulls signal up over time after the reaction has effectively finished. 

These four quantities are what the CDK currently aims to characterize, and the rest of this primer is about how it gets there and how to read the output.

## The model the CDK uses

We separate out the above phases by the "sigmoid drift" equation. Let $F(t)$ be the fluorescence of a reaction at time $t$:

$$
F(t) = F_{ss}\frac{1}{1 + e^{-k(t-\tau_{vel})}} + d(t- \tau_{drift}), 
$$

where:
| Symbol | Name | What it tells you |
|---|---|---|
|$F_{ss}$ | asymptote | the fluorescence at steady state before drift |
| `k` | steepness | how fast the reaction crosses its midpoint |
| $\tau_{vel}$  | inflection time | when the reaction is at half-max |
| `d` | drift slope | rate of post-saturation drift (ideally ≈ 0) |
| $\tau_{drift}$| drift onset | time when drift starts contributing |


In addition to the above parameters, we also report three derived quantities: 

- **$V_{max$ (phenomenological)** — the maximum slope of the sigmoid, which occurs at $\tau_{vel}$ and equals $A k / 4$. This is *not* the Michaelis–Menten $V_{\max}$; it is a single scalar summary of the steepest part of the accumulation curve. When comparing across conditions, prefer reporting `k` directly; report $Ak/4$ only when you need a slope-with-units for a downstream calculation.
- **Time-to-steady-state** — the time at which the sigmoid reaches a chosen fraction $\alpha$ of its asymptote (default $\alpha=0.95$), solved from the sigmoid as
  $$
  t_\alpha \;=\; t_0 + \frac{1}{k}\ln\!\left(\frac{\alpha}{1-\alpha}\right).
  $$
  Drift is intentionally excluded from this calculation — "when did the reaction finish" should not depend on how badly the plate was evaporating afterward.
- T-lag
  

$F_{ss}$ is the fluorescence at steady state before drift, $k$ is how fast the reaction crosses its midpoint, $\tau_{vel}$ is the inflection point of the reaction.), $d$ is the rate of drift and $\tau_{drift}$ is the time when drift starts contributing.

:::{figure} #fig:kinetics
:name: fig-kinetics
:align: center
:width: 50%

Example reactions (10 $\mu$L PURE in triplicate at typical composition) fit to a logistic curve with linear drift. Dots represent fluorescence at each timepoint (individual replicates in blue, mean of replicates in green). Diagnostic parameters time to steady state ($t_{steadystate}$), lag time ($t_{lag}$), and maximum velocity ($V_{max}$) are plotted as well. Vertical and horizontal dashed red lines represent time to steady state and steady state fluorescence ($F_{ss}$), respectively. Orange dashed line represents the tangent line at the inflection point. The slope of this line is $V_{max}$ and the x intercept of this line is $t_{lag}$. The fitted curve is plotted as a red dashed curve on top of data points. 
:::

Using this mathematical model, we can extract forms for the following useful parameters:


| Parameter                 | Symbol         | Units            | Description                                                                                                                                                                                                                                                                      |
| ------------------------- | -------------- | ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Steady State Fluorescence | $F_{ss}$       | fluorescence units ($u$)              | How much total protein is expressed over the whole reaction? Fit explicitly in the model above.                                                                                                                                                                                  |
| Time to Steady State      | $\tau_{ss}$    | time (typically $h$)              | How long does it take for the reaction to reach steady state?                                                                                                                                                                                                                    |
| Lag Time                  | $\tau_{lag}$   | time (typically $min$)              | How long does it take for the reaction to start? This is roughly correlated with transcription lag time + translation lag time + maturation time of GFP. We calculate this as the x-intercept of the line tangent to the inflection point on the sigmoid |
| Maximum Velocity          | $V_{max}$      | fluorescence over time ($u \cdot h^{-1}$) | How fast is GFP getting produced at the fastest production rate in the reaction? This is the velocity of the reaction at $\tau_{max}$ and the slope of the line tangent to the inflection point and equals $F_{ss} * k / 4$^*                                 |
| Drift Rate                | $d$            | fluorescence over time ($u \cdot h^{-1}$) | If the reaction shows drift after steady state, how fast does it drift?                                                                                                                                                                                                          |
| Drift Onset Time          | $\tau_{drift}$ | time (typically $h$)              | If the reaction shows drift after steady state, when does it start to drift?                                                                                                                                                                                                     |

Notably, we have three derived quantities 
- insert box I sent you here? [Jon]
  
# How do we fit kinetic parameters in practice?
We use the `cdk` to fit our curves and extract those parameters automatically. 
This primer assumes you already have:

- a plate-reader export the CDK can ingest (BioTek, Cytation, or Envision; see [`cdk.instrument.platereader`](https://github.com/bnext-bio/bnext/tree/main/cdk/src/cdk/analysis/cytosol)),
- a platemap that labels each well with a condition (see the *Why you should use a platemap* DevNote),
- at least one fluorescent standard on the plate (see the *Why you should use standards* DevNote).

If any of those is missing, fix that first — fitting a curve to uncalibrated, unlabeled data just produces better-looking garbage. (JON: too hot of a take? haha pls feel free to remove)

- Look at this notebook
- Here are the plots you get

The minimum viable call is:

```python
from cdk.analysis.cytosol import platereader as pr

data = pr.load_platereader_data(
    path="20260416-my-experiment/",
    platemap="platemap.csv",
)

pr.plot_kinetics(data, fit_function_name="sigmoid_drift")
```

That produces, per condition group, (a) the overlaid raw traces with the fit, (b) a summary plot of `A`, `Vmax`, and `t_α`, and (c) a tidy DataFrame of fit parameters

**Default worth knowing.** The CDK currently defaults to fit_function_name="sigmoid_drift". If you truly dont want drift modeled, call "sigmoid"


:::{tip}
Check out this example jupyter notebook!
:::

## Common pitfalls

**Truncated saturation.** If the reaction hasn't actually plateaued by the last time-point, `A` is unconstrained and the optimizer will cheerfully return a garbage fit with small residuals. We are working on building checks for this.

**Reporting uncalibrated RFU.** `A` is in the reader's native fluorescence units until you normalize by a standard. For within-plate comparisons this is sub-par; for anything that leaves the plate, apply the standards pipeline first.

## When the sigmoid isn't enough

The sigmoid is a *phenomenological* fit: it is good at summarizing a well-behaved trace in four numbers, and bad at everything else. Specifically, it cannot represent:

- asymmetric rise/fall (use Gompertz or a generalized sigmoid),
- a biphasic reaction where a module kicks in mid-run (e.g., ClpXP-mediated degradation catching up to production),
- explicit resource-exhaustion dynamics that a mechanistic model could represent.


# What's coming next for kinetic analysis?
Our next Kinetics DevNote will cover how to select among these fits, how to report **credible intervals** on `A`, `Vmax`, and `t_α` instead of point estimates. 
- RNA aptamers allow us to measure transcription rate directly. This allows us to directly observe the transcription/translation rate trade off.
- Mechanistic modeling.
- Confidence intervals 

# Other things to watch out for
- Fluorescence standards help you normalize your reactions for differences across platereaders and experimental conditions, check it out!
- Platemaps help standardize data representation, making it easy to compare data across experiments and teams.
- Here is a cool dataset that demonstrates all of these things put together..

  Cell-free expression reactions are usually scored by a single endpoint fluorescence reading — simple to run, hard to interpret, and almost impossible to compare across labs. Watching the reaction unfold as a **timeseries** gives richer data, but that richness becomes useful once you can summarize a trace in a handful of interpretable numbers. This primer explains why we prefer timeseries measurements over endpoints, and shows how the Cell Development Kit (CDK) fits a logistic-with-drift model to plate-reader traces to extract steady-state yield, reaction rate, time-to-steady-state, and a drift correction. Along the way it flags the pitfalls that motivate the more careful treatment coming in Kinetics 102by measuring how much fluorescent protein it can make. Fluorescence is roughly proportional to reporter concentration, which makes steady-state fluorescence a simple and effective readout of total expression capacity.****different samples have the same endpoint fluorescence,th steady state twice as fast as the other? Endpoints can't tell you, and different labs makin different choices about incubation time produce results that look comparable but aren't.ostsamplesreading, which means observing the reaction as it runs is almost free. These **timeseries measurements** answer the questions endpoints can't, at the cost of a little more processing on the bac end. We think that trade is worth makand the rest of this DevNote is the case for hy
We've found that a quick way notice something is wrong with a reaction is to look at a fluorescence-versus-time plot. We've found some strange behaviors that would otherwise be hidden in a simple barplot of endpoints. For instance:

- Reactions that reach steady state and then **drift** slowly up or down: we suspect evaporation or incomplete sealing, but the cause matters less right now than the observation that ignoring drift can inflate or deflate apparent yield by tens of percent.
- Reactions that reach the **same steady state at different times**, which looks identical at endpoint but represents genuinely different underlying kinetics.
- **Biphasic traces** — an initial fast expression phase followed by a slower second one. This may reflect NTP depletion and re-phosphorylation, or some other resource-switching mechanism we don't yet fully understand. These are exactly the kind of observations that motivate mechanistic modeling, and they are completely invisible in an endpoint assay.

**Quantitative modeling needs the whole curve.** Those qualitative observations only become quantitative claims when you can fit them. As the Nucleus Community grows and more groups share cytosol data, information-dense timeseries will compound in value in a way that endpoints never will. You can always throw away the timepoints and recover an endpoint from a timeseries, but you can't go the other direction. We strongly encourage collecting timeseries now, even if you aren't ready to analyze them yet, so the data is there when the tools catch up.

-- JON WHAT DO YOU THINK OF THE ABOVE? I tried to clean it up but didnt want to delete since iM not sure if I like my version. aquick represent
A timeseries is a rich object: every trace is shaped by real reaction kinetics including transcription, translation initiation, fluorophore maturation, resource depletion, degradation — layered on top of instrument effects like evaporation and photobleaching. The goal of fitting is *not* to replace that richness with four numbers. The goal is to produce a compact, comparable summary of the curve that captures the features you want to reason about, while flagging the cases where a simple summary isn't enough and a richer model is warranted. It is also how we turn plate-reader output into units that travel: numbers you can put in a table, plot against a design variable, hand to a modeler, or publish in a DevNote alongside standards-normalized concentrations.
Wcytosol reactions are well approximated by a  sigmoid with a linear drift term. It approximates the following phases of cytosol reactions: 

1. **Lag.** Transcription, translation initiation; signal is flat or nearly so.
2. **Rise.** Protein accumulates approximately linearly; the slope near the inflection point is the phenomenological "Vmax" we report.
3. **Steady State.** Energy runs out, waste accumulates, the reporter plateaus. [JON PLEASE EDIT THIS]

A misbehaving trace adds a fourth phase:

4. **Drift.** Evaporation or lid condensation pulls signal up over time after the reaction has effectively finished. 

These four quantities are what the CDK currently aims to characterize, and the rest of this primer is about how it gets there and how to read the output.

## The model the CDK uses

We separate out the above phases by the "sigmoid drift" equation. Lauvel

where:
| Symbol | Name | What it tells you |
|---|---|---|
|$F_{ss}$ | asymptote | the fluorescence at steady state before drift |
| `k` | steepness | how fast the reaction crosses its midpoint |
| $\tau_{vel}$  | inflection time | when the reaction is at half-max |
| `d` | drift slope | rate of post-saturation drift (ideally ≈ 0) |
| $\tau_{drift}$| drift onset | time when drift starts contributing |


In addition to the above parameters, we also report three derived quantities: 

- **Vmax (phenomenological)** — the maximum slope of the sigmoid, which occurs at $\tau_{vel}$ and equals $A k / 4$. This is *not* the Michaelis–Menten $V_{\max}$; it is a single scalar summary of the steepest part of the accumulation curve. When comparing across conditions, prefer reporting `k` directly; report $Ak/4$ only when you need a slope-with-units for a downstream calculation.
- **Time-to-steady-state** — the time at which the sigmoid reaches a chosen fraction $\alpha$ of its asymptote (default $\alpha=0.95$), solved from the sigmoid as
  $$
  t_\alpha \;=\; t_0 + \frac{1}{k}\ln\!\left(\frac{\alpha}{1-\alpha}\right).
  $$
  Drift is intentionally excluded from this calculation — "when did the reaction finish" should not depend on how badly the plate was evaporating afterward.
- T-lag
  

or before drifthow fast the reaction crosses its midpoint\tauvel.)when drift starts contributing.teadystate| Parameter                 | Symbol         | Units            | Description                                                                                                                                                                                                                                                                      |
| ------------------------- | -------------- | ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Steady State Fluorescence | $F_{ss}$       | fluorescence units ($u$)              | How much total protein is expressed over the whole reaction? Fit explicitly in the model above.                                                                                                                                                                                  |
| Time to Steady State      | $\tau_{ss}$    | time (typically $h$)              | How long does it take for the reaction to reach steady state?                                                                                                                                                                                                                    |
| Lag Time                  | $\tau_{lag}$   | time (typically $min$)              | How long does it take for the reaction to start? This is roughly correlated with transcription lag time + translation lag time + maturation time of GFP. We calculate this as the x-intercept of the line tangent to the inflection point on the sigmoid |
| Maximum Velocity          | $V_{max}$      | fluorescence over time ($u \cdot h^{-1}$) | How fast is GFP getting produced at the fastest production rate in the reaction? This is the velocity of the reaction at $\tau_{max}$ and the slope of the line tangent to the inflection point and equals $F_{ss} * k / 4$^*                                 |
| Drift Rate                | $d$            | fluorescence over time ($u \cdot h^{-1}$) | If the reaction shows drift after steady state, how fast does it drift?                                                                                                                                                                                                          |
| Drift Onset Time          | $\tau_{drift}$ | time (typically $h$)              | If the reaction shows drift after steady state, when does it start to drift?                                                                                                                                                                                                     |

Notably, we have three derived quantities 
- insert box I sent you here? [Jon]
 in practice
This primer assumes you already have:

- a plate-reader export the CDK can ingest (BioTek, Cytation, or Envision; see [`cdk.instrument.platereader`](https://github.com/bnext-bio/bnext/tree/main/cdk/src/cdk/analysis/cytosol)),
- a platemap that labels each well with a condition (see the *Why you should use a platemap* DevNote),
- at least one fluorescent standard on the plate (see the *Why you should use standards* DevNote).

If any of those is missing, fix that first — fitting a curve to uncalibrated, unlabeled data just produces better-looking garbage. (JON: too hot of a take? haha pls feel free to remove)

- Look at this notebook
- Here are the plots you get

The minimum viable call is:

```python
from cdk.analysis.cytosol import platereader as pr

data = pr.load_platereader_data(
    path="20260416-my-experiment/",
    platemap="platemap.csv",
)

pr.plot_kinetics(data, fit_function_name="sigmoid_drift")
```

That produces, per condition group, (a) the overlaid raw traces with the fit, (b) a summary plot of `A`, `Vmax`, and `t_α`, and (c) a tidy DataFrame of fit parameters

**Default worth knowing.** The CDK currently defaults to fit_function_name="sigmoid_drift". If you truly dont want drift modeled, call "sigmoid"

# Common pitfalls

**Truncated saturation.** If the reaction hasn't actually plateaued by the last time-point, `A` is unconstrained and the optimizer will cheerfully return a garbage fit with small residuals. We are working on building checks for this.

**Reporting uncalibrated RFU.** `A` is in the reader's native fluorescence units until you normalize by a standard. For within-plate comparisons this is sub-par; for anything that leaves the plate, apply the standards pipeline first.

## When the sigmoid isn't enough

The sigmoid is a *phenomenological* fit: it is good at summarizing a well-behaved trace in four numbers, and bad at everything else. Specifically, it cannot represent:

- asymmetric rise/fall (use Gompertz or a generalized sigmoid),
- a biphasic reaction where a module kicks in mid-run (e.g., ClpXP-mediated degradation catching up to production),
- explicit resource-exhaustion dynamics that a mechanistic model could represent.



#Our next Kinetics DevNote will cover how to select among these fits, how to report **credible intervals** on `A`, `Vmax`, and `t_α` instead of point estimates. 
- Confidence intervals 
- ---
title: Intro to Kinetics Analysis of Plate Reader Experiments
abstract: |
  We often test the function of cytosol by expressing a fluorescent protein off of a DNA template and measuring the resulting fluorescence. The simple "endpoint measurement" takes one reading at the end of the reaction, telling you the total amount of expression. However, a "timeseries measurement" can  tell you how fast your protein is made, giving you more rich information. Here, we explain why we at b.next model kinetics of cytosol timeseries and how you can too, using the `cdk`.

  Cell-free expression reactions are usually scored by a single endpoint fluorescence reading — simple to run, hard to interpret, and almost impossible to compare across labs. Watching the reaction unfold as a **timeseries** gives richer data, but that richness becomes useful once you can summarize a trace in a handful of interpretable numbers. This primer explains why we prefer timeseries measurements over endpoints, and shows how the Cell Development Kit (CDK) fits a logistic-with-drift model to plate-reader traces to extract steady-state yield, reaction rate, time-to-steady-state, and a drift correction. Along the way it flags the pitfalls that motivate the more careful treatment coming in Kinetics 102.
---

# Cytosol measurements: endpoints vs timeseries
We test our cytosol by measuring how much fluorescent protein it can make. Fluorescence is roughly proportional to reporter concentration, which makes steady-state fluorescence a simple and effective readout of total expression capacity.

The simple **endpoint measurement** is the easiest version of this assay. Just incubate your reactions until completion (at least 2 hrs) and measure the fluorescence. However, some complications make endpoint measurements hard to compare across labs, or even across your own experiments. Is 4 hrs enough? Does the fluorescence change after 16 hrs, or even more? If two different samples have the same endpoint fluorescence, did they behave identically, or did one reach steady state twice as fast as the other? Endpoints can't tell you, and different labs making different choices about incubation time produce results that look comparable but aren't.

Most plate readers can incubate samples while reading, which means observing the reaction as it runs is almost free. These **timeseries measurements** answer the questions endpoints can't, at the cost of a little more processing on the back end. We think that trade is worth making, and the rest of this DevNote is the case for why.

# Why timeseries?
We've found that a quick way notice something is wrong with a reaction is to look at a fluorescence-versus-time plot. We've found some strange behaviors that would otherwise be hidden in a simple barplot of endpoints. For instance:

- Reactions that reach steady state and then **drift** slowly up or down: we suspect evaporation or incomplete sealing, but the cause matters less right now than the observation that ignoring drift can inflate or deflate apparent yield by tens of percent.
- Reactions that reach the **same steady state at different times**, which looks identical at endpoint but represents genuinely different underlying kinetics.
- **Biphasic traces** — an initial fast expression phase followed by a slower second one. This may reflect NTP depletion and re-phosphorylation, or some other resource-switching mechanism we don't yet fully understand. These are exactly the kind of observations that motivate mechanistic modeling, and they are completely invisible in an endpoint assay.

**Quantitative modeling needs the whole curve.** Those qualitative observations only become quantitative claims when you can fit them. As the Nucleus Community grows and more groups share cytosol data, information-dense timeseries will compound in value in a way that endpoints never will. You can always throw away the timepoints and recover an endpoint from a timeseries, but you can't go the other direction. We strongly encourage collecting timeseries now, even if you aren't ready to analyze them yet, so the data is there when the tools catch up.

-- JON WHAT DO YOU THINK OF THE ABOVE? I tried to clean it up but didnt want to delete since iM not sure if I like my version. 
Why do we prefer timeseries over endpoints? 

First, we've found that a quick way to diagnose if our reactions are running correctly is visually inspecting fluorescence vs time graphs. We've found some strange behaviors that would otherwise be hidden in a simple barplot of endpoints. 

For instance, some reactions reach steady state then start to drift higher or lower slowly over time. We don't know why this happens -- e.g., perhaps if the well is not fully sealed, evaporation may affect readings? -- but not accounting for drift can artificially inflate or deflate estimates of total protein expression. We have also seen two reactions that reach the same steady state, at different times. 

(We've also seen more complex behavior that motivates new mechanistic models, like "biphasic" timeseries with an initial fast expression phase followed by a slow one. Are our reactions running out of NTPs and waiting for them to get re-phosphorylated?  -- Jon: we can omit this more advanced example, but it more strongly motivates modeling, I think)

These nuances would be missed in an endpoint measurement. 

Second, these qualitative observations can only be quantitatively modeled with timeseries data. As the Nucleus Community grows and we have more people sharing data and using that data to study how cytosol works, we believe that these more information-rich datasets will become increasingly valuable. Thus, we encourage everyone to take timeseries of their experiments now so that we can learn more from them in the future.


# How do we represent timeseries data?
A timeseries is a rich object: every trace is shaped by real reaction kinetics including transcription, translation initiation, fluorophore maturation, resource depletion, degradation — layered on top of instrument effects like evaporation and photobleaching. The goal of fitting is *not* to replace that richness with four numbers. The goal is to produce a compact, comparable summary of the curve that captures the features you want to reason about, while flagging the cases where a simple summary isn't enough and a richer model is warranted. It is also how we turn plate-reader output into units that travel: numbers you can put in a table, plot against a design variable, hand to a modeler, or publish in a DevNote alongside standards-normalized concentrations.

(ACJS: can you write a small blurb on the NIST workshop bit? I can't represent this myself - Based on NIST workshop and other conversations)
  
We find that much like bacterial growth curves, cytosol reactions are well approximated by a  sigmoid with a linear drift term. It approximates the following phases of cytosol reactions: 

1. **Lag.** Transcription, translation initiation; signal is flat or nearly so.
2. **Rise.** Protein accumulates approximately linearly; the slope near the inflection point is the phenomenological "Vmax" we report.
3. **Steady State.** Energy runs out, waste accumulates, the reporter plateaus. [JON PLEASE EDIT THIS]

A misbehaving trace adds a fourth phase:

4. **Drift.** Evaporation or lid condensation pulls signal up over time after the reaction has effectively finished. 

These four quantities are what the CDK currently aims to characterize, and the rest of this primer is about how it gets there and how to read the output.

## The model the CDK uses

We separate out the above phases by the "sigmoid drift" equation. Let $F(t)$ be the fluorescence of a reaction at time $t$:

$$
F(t) = F_{ss}\frac{1}{1 + e^{-k(t-\tau_{vel})}} + d(t- \tau_{drift}), 
$$

where:
| Symbol | Name | What it tells you |
|---|---|---|
|$F_{ss}$ | asymptote | the fluorescence at steady state before drift |
| `k` | steepness | how fast the reaction crosses its midpoint |
| $\tau_{vel}$  | inflection time | when the reaction is at half-max |
| `d` | drift slope | rate of post-saturation drift (ideally ≈ 0) |
| $\tau_{drift}$| drift onset | time when drift starts contributing |


In addition to the above parameters, we also report three derived quantities: 

- **Vmax (phenomenological)** — the maximum slope of the sigmoid, which occurs at $\tau_{vel}$ and equals $A k / 4$. This is *not* the Michaelis–Menten $V_{\max}$; it is a single scalar summary of the steepest part of the accumulation curve. When comparing across conditions, prefer reporting `k` directly; report $Ak/4$ only when you need a slope-with-units for a downstream calculation.
- **Time-to-steady-state** — the time at which the sigmoid reaches a chosen fraction $\alpha$ of its asymptote (default $\alpha=0.95$), solved from the sigmoid as
  $$
  t_\alpha \;=\; t_0 + \frac{1}{k}\ln\!\left(\frac{\alpha}{1-\alpha}\right).
  $$
  Drift is intentionally excluded from this calculation — "when did the reaction finish" should not depend on how badly the plate was evaporating afterward.
- T-lag
  

$F_{ss}$ is the fluorescence at steady state before drift, $k$ is how fast the reaction crosses its midpoint, $\tau_{vel}$ is the inflection point of the reaction.), $d$ is the rate of drift and $\tau_{drift}$ is the time when drift starts contributing.

:::{figure} #fig:kinetics
:name: fig-kinetics
:align: center
:width: 50%

Example reactions (10 $\mu$L PURE in triplicate at typical composition) fit to a logistic curve with linear drift. Dots represent fluorescence at each timepoint (individual replicates in blue, mean of replicates in green). Diagnostic parameters time to steady state ($t_{steadystate}$), lag time ($t_{lag}$), and maximum velocity ($V_{max}$) are plotted as well. Vertical and horizontal dashed red lines represent time to steady state and steady state fluorescence ($F_{ss}$), respectively. Orange dashed line represents the tangent line at the inflection point. The slope of this line is $V_{max}$ and the x intercept of this line is $t_{lag}$. The fitted curve is plotted as a red dashed curve on top of data points. 
:::

Using this mathematical model, we can extract forms for the following useful parameters:


| Parameter                 | Symbol         | Units            | Description                                                                                                                                                                                                                                                                      |
| ------------------------- | -------------- | ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Steady State Fluorescence | $F_{ss}$       | fluorescence units ($u$)              | How much total protein is expressed over the whole reaction? Fit explicitly in the model above.                                                                                                                                                                                  |
| Time to Steady State      | $\tau_{ss}$    | time (typically $h$)              | How long does it take for the reaction to reach steady state?                                                                                                                                                                                                                    |
| Lag Time                  | $\tau_{lag}$   | time (typically $min$)              | How long does it take for the reaction to start? This is roughly correlated with transcription lag time + translation lag time + maturation time of GFP. We calculate this as the x-intercept of the line tangent to the inflection point on the sigmoid |
| Maximum Velocity          | $V_{max}$      | fluorescence over time ($u \cdot h^{-1}$) | How fast is GFP getting produced at the fastest production rate in the reaction? This is the velocity of the reaction at $\tau_{max}$ and the slope of the line tangent to the inflection point and equals $F_{ss} * k / 4$^*                                 |
| Drift Rate                | $d$            | fluorescence over time ($u \cdot h^{-1}$) | If the reaction shows drift after steady state, how fast does it drift?                                                                                                                                                                                                          |
| Drift Onset Time          | $\tau_{drift}$ | time (typically $h$)              | If the reaction shows drift after steady state, when does it start to drift?                                                                                                                                                                                                     |

Notably, we have three derived quantities 
- insert box I sent you here? [Jon]
  
# How do we fit kinetic parameters in practice?
We use the `cdk` to fit our curves and extract those parameters automatically. 
This primer assumes you already have:

- a plate-reader export the CDK can ingest (BioTek, Cytation, or Envision; see [`cdk.instrument.platereader`](https://github.com/bnext-bio/bnext/tree/main/cdk/src/cdk/analysis/cytosol)),
- a platemap that labels each well with a condition (see the *Why you should use a platemap* DevNote),
- at least one fluorescent standard on the plate (see the *Why you should use standards* DevNote).

If any of those is missing, fix that first — fitting a curve to uncalibrated, unlabeled data just produces better-looking garbage. (JON: too hot of a take? haha pls feel free to remove)

- Look at this notebook
- Here are the plots you get

The minimum viable call is:

```python
from cdk.analysis.cytosol import platereader as pr

data = pr.load_platereader_data(
    path="20260416-my-experiment/",
    platemap="platemap.csv",
)

pr.plot_kinetics(data, fit_function_name="sigmoid_drift")
```

That produces, per condition group, (a) the overlaid raw traces with the fit, (b) a summary plot of `A`, `Vmax`, and `t_α`, and (c) a tidy DataFrame of fit parameters

**Default worth knowing.** The CDK currently defaults to fit_function_name="sigmoid_drift". If you truly dont want drift modeled, call "sigmoid"


:::{tip}
Check out this example jupyter notebook!
:::

## Common pitfalls

**Truncated saturation.** If the reaction hasn't actually plateaued by the last time-point, `A` is unconstrained and the optimizer will cheerfully return a garbage fit with small residuals. We are working on building checks for this.

**Reporting uncalibrated RFU.** `A` is in the reader's native fluorescence units until you normalize by a standard. For within-plate comparisons this is sub-par; for anything that leaves the plate, apply the standards pipeline first.

## When the sigmoid isn't enough

The sigmoid is a *phenomenological* fit: it is good at summarizing a well-behaved trace in four numbers, and bad at everything else. Specifically, it cannot represent:

- asymmetric rise/fall (use Gompertz or a generalized sigmoid),
- a biphasic reaction where a module kicks in mid-run (e.g., ClpXP-mediated degradation catching up to production),
- explicit resource-exhaustion dynamics that a mechanistic model could represent.



# What's coming next for kinetic analysis?
Our next Kinetics DevNote will cover how to select among these fits, how to report **credible intervals** on `A`, `Vmax`, and `t_α` instead of point estimates. 
- RNA aptamers allow us to measure transcription rate directly. This allows us to directly observe the transcription/translation rate trade off.
- Mechanistic modeling.
- Confidence intervals 

# Other things to watch out for
- Fluorescence standards help you normalize your reactions for differences across platereaders and experimental conditions, check it out!
- Platemaps help standardize data representation, making it easy to compare data across experiments and teams.
- Here is a cool dataset that demonstrates all of these things put together..

  Cell-free expression reactions are usually scored by a single endpoint fluorescence reading — simple to run, hard to interpret, and almost impossible to compare across labs. Watching the reaction unfold as a **timeseries** gives richer data, but that richness becomes useful once you can summarize a trace in a handful of interpretable numbers. This primer explains why we prefer timeseries measurements over endpoints, and shows how the Cell Development Kit (CDK) fits a logistic-with-drift model to plate-reader traces to extract steady-state yield, reaction rate, time-to-steady-state, and a drift correction. Along the way it flags the pitfalls that motivate the more careful treatment coming in Kinetics 102by measuring how much fluorescent protein it can make. Fluorescence is roughly proportional to reporter concentration, which makes steady-state fluorescence a simple and effective readout of total expression capacity.****different samples have the same endpoint fluorescence,th steady state twice as fast as the other? Endpoints can't tell you, and different labs makin different choices about incubation time produce results that look comparable but aren't.ostsamplesreading, which means observing the reaction as it runs is almost free. These **timeseries measurements** answer the questions endpoints can't, at the cost of a little more processing on the bac end. We think that trade is worth makand the rest of this DevNote is the case for hy
We've found that a quick way notice something is wrong with a reaction is to look at a fluorescence-versus-time plot. We've found some strange behaviors that would otherwise be hidden in a simple barplot of endpoints. For instance:

- Reactions that reach steady state and then **drift** slowly up or down: we suspect evaporation or incomplete sealing, but the cause matters less right now than the observation that ignoring drift can inflate or deflate apparent yield by tens of percent.
- Reactions that reach the **same steady state at different times**, which looks identical at endpoint but represents genuinely different underlying kinetics.
- **Biphasic traces** — an initial fast expression phase followed by a slower second one. This may reflect NTP depletion and re-phosphorylation, or some other resource-switching mechanism we don't yet fully understand. These are exactly the kind of observations that motivate mechanistic modeling, and they are completely invisible in an endpoint assay.

**Quantitative modeling needs the whole curve.** Those qualitative observations only become quantitative claims when you can fit them. As the Nucleus Community grows and more groups share cytosol data, information-dense timeseries will compound in value in a way that endpoints never will. You can always throw away the timepoints and recover an endpoint from a timeseries, but you can't go the other direction. We strongly encourage collecting timeseries now, even if you aren't ready to analyze them yet, so the data is there when the tools catch up.

-- JON WHAT DO YOU THINK OF THE ABOVE? I tried to clean it up but didnt want to delete since iM not sure if I like my version. aquick represent
A timeseries is a rich object: every trace is shaped by real reaction kinetics including transcription, translation initiation, fluorophore maturation, resource depletion, degradation — layered on top of instrument effects like evaporation and photobleaching. The goal of fitting is *not* to replace that richness with four numbers. The goal is to produce a compact, comparable summary of the curve that captures the features you want to reason about, while flagging the cases where a simple summary isn't enough and a richer model is warranted. It is also how we turn plate-reader output into units that travel: numbers you can put in a table, plot against a design variable, hand to a modeler, or publish in a DevNote alongside standards-normalized concentrations.
Wcytosol reactions are well approximated by a  sigmoid with a linear drift term. It approximates the following phases of cytosol reactions: 

1. **Lag.** Transcription, translation initiation; signal is flat or nearly so.
2. **Rise.** Protein accumulates approximately linearly; the slope near the inflection point is the phenomenological "Vmax" we report.
3. **Steady State.** Energy runs out, waste accumulates, the reporter plateaus. [JON PLEASE EDIT THIS]

A misbehaving trace adds a fourth phase:

4. **Drift.** Evaporation or lid condensation pulls signal up over time after the reaction has effectively finished. 

These four quantities are what the CDK currently aims to characterize, and the rest of this primer is about how it gets there and how to read the output.

## The model the CDK uses

We separate out the above phases by the "sigmoid drift" equation. Lauvel

where:
| Symbol | Name | What it tells you |
|---|---|---|
|$F_{ss}$ | asymptote | the fluorescence at steady state before drift |
| `k` | steepness | how fast the reaction crosses its midpoint |
| $\tau_{vel}$  | inflection time | when the reaction is at half-max |
| `d` | drift slope | rate of post-saturation drift (ideally ≈ 0) |
| $\tau_{drift}$| drift onset | time when drift starts contributing |


In addition to the above parameters, we also report three derived quantities: 

- **Vmax (phenomenological)** — the maximum slope of the sigmoid, which occurs at $\tau_{vel}$ and equals $A k / 4$. This is *not* the Michaelis–Menten $V_{\max}$; it is a single scalar summary of the steepest part of the accumulation curve. When comparing across conditions, prefer reporting `k` directly; report $Ak/4$ only when you need a slope-with-units for a downstream calculation.
- **Time-to-steady-state** — the time at which the sigmoid reaches a chosen fraction $\alpha$ of its asymptote (default $\alpha=0.95$), solved from the sigmoid as
  $$
  t_\alpha \;=\; t_0 + \frac{1}{k}\ln\!\left(\frac{\alpha}{1-\alpha}\right).
  $$
  Drift is intentionally excluded from this calculation — "when did the reaction finish" should not depend on how badly the plate was evaporating afterward.
- T-lag
  

or before drifthow fast the reaction crosses its midpoint\tauvel.)when drift starts contributing.teadystate| Parameter                 | Symbol         | Units            | Description                                                                                                                                                                                                                                                                      |
| ------------------------- | -------------- | ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Steady State Fluorescence | $F_{ss}$       | fluorescence units ($u$)              | How much total protein is expressed over the whole reaction? Fit explicitly in the model above.                                                                                                                                                                                  |
| Time to Steady State      | $\tau_{ss}$    | time (typically $h$)              | How long does it take for the reaction to reach steady state?                                                                                                                                                                                                                    |
| Lag Time                  | $\tau_{lag}$   | time (typically $min$)              | How long does it take for the reaction to start? This is roughly correlated with transcription lag time + translation lag time + maturation time of GFP. We calculate this as the x-intercept of the line tangent to the inflection point on the sigmoid |
| Maximum Velocity          | $V_{max}$      | fluorescence over time ($u \cdot h^{-1}$) | How fast is GFP getting produced at the fastest production rate in the reaction? This is the velocity of the reaction at $\tau_{max}$ and the slope of the line tangent to the inflection point and equals $F_{ss} * k / 4$^*                                 |
| Drift Rate                | $d$            | fluorescence over time ($u \cdot h^{-1}$) | If the reaction shows drift after steady state, how fast does it drift?                                                                                                                                                                                                          |
| Drift Onset Time          | $\tau_{drift}$ | time (typically $h$)              | If the reaction shows drift after steady state, when does it start to drift?                                                                                                                                                                                                     |

Notably, we have three derived quantities 
- insert box I sent you here? [Jon]
 in practice
This primer assumes you already have:

- a plate-reader export the CDK can ingest (BioTek, Cytation, or Envision; see [`cdk.instrument.platereader`](https://github.com/bnext-bio/bnext/tree/main/cdk/src/cdk/analysis/cytosol)),
- a platemap that labels each well with a condition (see the *Why you should use a platemap* DevNote),
- at least one fluorescent standard on the plate (see the *Why you should use standards* DevNote).

If any of those is missing, fix that first — fitting a curve to uncalibrated, unlabeled data just produces better-looking garbage. (JON: too hot of a take? haha pls feel free to remove)

- Look at this notebook
- Here are the plots you get

The minimum viable call is:

```python
from cdk.analysis.cytosol import platereader as pr

data = pr.load_platereader_data(
    path="20260416-my-experiment/",
    platemap="platemap.csv",
)

pr.plot_kinetics(data, fit_function_name="sigmoid_drift")
```

That produces, per condition group, (a) the overlaid raw traces with the fit, (b) a summary plot of `A`, `Vmax`, and `t_α`, and (c) a tidy DataFrame of fit parameters

**Default worth knowing.** The CDK currently defaults to fit_function_name="sigmoid_drift". If you truly dont want drift modeled, call "sigmoid"

# Common pitfalls

**Truncated saturation.** If the reaction hasn't actually plateaued by the last time-point, `A` is unconstrained and the optimizer will cheerfully return a garbage fit with small residuals. We are working on building checks for this.

**Reporting uncalibrated RFU.** `A` is in the reader's native fluorescence units until you normalize by a standard. For within-plate comparisons this is sub-par; for anything that leaves the plate, apply the standards pipeline first.

## When the sigmoid isn't enough

The sigmoid is a *phenomenological* fit: it is good at summarizing a well-behaved trace in four numbers, and bad at everything else. Specifically, it cannot represent:

- asymmetric rise/fall (use Gompertz or a generalized sigmoid),
- a biphasic reaction where a module kicks in mid-run (e.g., ClpXP-mediated degradation catching up to production),
- explicit resource-exhaustion dynamics that a mechanistic model could represent.



#Our next Kinetics DevNote will cover how to select among these fits, how to report **credible intervals** on `A`, `Vmax`, and `t_α` instead of point estimates. 
- Confidence intervals 
- ---
title: Intro to Kinetics Analysis of Plate Reader Experiments
abstract: |
  We often test the function of cytosol by expressing a fluorescent protein off of a DNA template and measuring the resulting fluorescence. The simple "endpoint measurement" takes one reading at the end of the reaction, telling you the total amount of expression. However, a "timeseries measurement" can  tell you how fast your protein is made, giving you more rich information. Here, we explain, why and how, we at b.next model kinetics of cytosol timeseries and how you can too, using the `cdk`.

  Cell-free expression reactions are usually scored by a single endpoint fluorescence reading — simple to run, hard to interpret, and almost impossible to compare across labs. Watching the reaction unfold as a **timeseries** gives richer data, but that richness becomes useful once you can summarize a trace in a handful of interpretable numbers. This primer explains why we prefer timeseries measurements over endpoints, and shows how the Cell Development Kit (CDK) fits a logistic-with-drift model to plate-reader traces to extract steady-state yield, reaction rate, time-to-steady-state, and a drift correction. Along the way it flags the pitfalls that motivate the more careful treatment coming in Kinetics 102.[JON -not a fan of this version I wrote, but leaving here for your assesment]
--- 

# Cytosol measurements: endpoints vs timeseries
We test our cytosol by measuring how much fluorescent protein it can make. Fluorescence is roughly proportional to reporter concentration, which makes steady-state fluorescence a simple and effective readout of total expression capacity.

The simple **endpoint measurement** is the easiest version of this assay. Just incubate your reactions until completion (at least 2 hrs) and measure the fluorescence. However, some complications make endpoint measurements hard to compare across labs, or even across your own experiments. Is 4 hrs enough? Does the fluorescence change after 16 hrs, or even more? If two different samples have the same endpoint fluorescence, did they behave identically, or did one reach steady state twice as fast as the other? Endpoints can't tell you, and different labs making different choices about incubation time produce results that look comparable but aren't.

Most plate readers can incubate samples while reading, which means observing the reaction as it runs is almost free. These **timeseries measurements** answer the questions endpoints can't, at the cost of a little more processing on the back end. We think that trade is worth making, and the rest of this DevNote is the case for why.

# Why timeseries?
We've found that a quick way notice something is wrong with a reaction is to look at a fluorescence-versus-time plot. We've found some strange behaviors that would otherwise be hidden in a simple barplot of endpoints. For instance:

- Reactions that reach steady state and then **drift** slowly up or down: we suspect evaporation or incomplete sealing, but the cause matters less right now than the observation that ignoring drift can inflate or deflate apparent yield by tens of percent.
- Reactions that reach the **same steady state at different times**, which looks identical at endpoint but represents genuinely different underlying kinetics.
- **Biphasic traces** — an initial fast expression phase followed by a slower second one. This may reflect NTP depletion and re-phosphorylation, or some other resource-switching mechanism we don't yet fully understand. These are exactly the kind of observations that motivate mechanistic modeling, and they are completely invisible in an endpoint assay.

**Quantitative modeling needs the whole curve.** Those qualitative observations only become quantitative claims when you can fit them. As the Nucleus Community grows and more groups share cytosol data, information-dense timeseries will compound in value in a way that endpoints never will. You can always throw away the timepoints and recover an endpoint from a timeseries, but you can't go the other direction. We strongly encourage collecting timeseries now, even if you aren't ready to analyze them yet, so the data is there when the tools catch up.

-- JON WHAT DO YOU THINK OF THE ABOVE? I tried to clean it up but didnt want to delete since iM not sure if I like my version. 
Why do we prefer timeseries over endpoints? 

First, we've found that a quick way to diagnose if our reactions are running correctly is visually inspecting fluorescence vs time graphs. We've found some strange behaviors that would otherwise be hidden in a simple barplot of endpoints. 

For instance, some reactions reach steady state then start to drift higher or lower slowly over time. We don't know why this happens -- e.g., perhaps if the well is not fully sealed, evaporation may affect readings? -- but not accounting for drift can artificially inflate or deflate estimates of total protein expression. We have also seen two reactions that reach the same steady state, at different times. 

(We've also seen more complex behavior that motivates new mechanistic models, like "biphasic" timeseries with an initial fast expression phase followed by a slow one. Are our reactions running out of NTPs and waiting for them to get re-phosphorylated?  -- Jon: we can omit this more advanced example, but it more strongly motivates modeling, I think)

These nuances would be missed in an endpoint measurement. 

Second, these qualitative observations can only be quantitatively modeled with timeseries data. As the Nucleus Community grows and we have more people sharing data and using that data to study how cytosol works, we believe that these more information-rich datasets will become increasingly valuable. Thus, we encourage everyone to take timeseries of their experiments now so that we can learn more from them in the future.


# How do we represent timeseries data?
A timeseries is a rich object: every trace is shaped by real reaction kinetics including transcription, translation initiation, fluorophore maturation, resource depletion, degradation — layered on top of instrument effects like evaporation and photobleaching. The goal of fitting is *not* to replace that richness with four numbers. The goal is to produce a compact, comparable summary of the curve that captures the features you want to reason about, while flagging the cases where a simple summary isn't enough and a richer model is warranted. It is also how we turn plate-reader output into units that travel: numbers you can put in a table, plot against a design variable, hand to a modeler, or publish in a DevNote alongside standards-normalized concentrations.

(ACJS: can you write a small blurb on the NIST workshop bit? I can't represent this myself - Based on NIST workshop and other conversations)
  
We find that much like bacterial growth curves, cytosol reactions are well approximated by a  sigmoid with a linear drift term. It approximates the following phases of cytosol reactions: 

1. **Lag.** Transcription, translation initiation; signal is flat or nearly so.
2. **Rise.** Protein accumulates approximately linearly; the slope near the inflection point is the phenomenological "Vmax" we report.
3. **Steady State.** Energy runs out, waste accumulates, the reporter plateaus. [JON PLEASE EDIT THIS]

A misbehaving trace adds a fourth phase:

4. **Drift.** Evaporation or lid condensation pulls signal up over time after the reaction has effectively finished. 

These four quantities are what the CDK currently aims to characterize, and the rest of this primer is about how it gets there and how to read the output.

## The model the CDK uses

We separate out the above phases by the "sigmoid drift" equation. Let $F(t)$ be the fluorescence of a reaction at time $t$:

$$
F(t) = F_{ss}\frac{1}{1 + e^{-k(t-\tau_{vel})}} + d(t- \tau_{drift}), 
$$

where:
| Symbol | Name | What it tells you |
|---|---|---|
|$F_{ss}$ | asymptote | the fluorescence at steady state before drift |
| `k` | steepness | how fast the reaction crosses its midpoint |
| $\tau_{vel}$  | inflection time | when the reaction is at half-max |
| `d` | drift slope | rate of post-saturation drift (ideally ≈ 0) |
| $\tau_{drift}$| drift onset | time when drift starts contributing |


In addition to the above parameters, we also report three derived quantities: 

- **Vmax (phenomenological)** — the maximum slope of the sigmoid, which occurs at $\tau_{vel}$ and equals $A k / 4$. This is *not* the Michaelis–Menten $V_{\max}$; it is a single scalar summary of the steepest part of the accumulation curve. When comparing across conditions, prefer reporting `k` directly; report $Ak/4$ only when you need a slope-with-units for a downstream calculation.
- **Time-to-steady-state** — the time at which the sigmoid reaches a chosen fraction $\alpha$ of its asymptote (default $\alpha=0.95$), solved from the sigmoid as
  $$
  t_\alpha \;=\; t_0 + \frac{1}{k}\ln\!\left(\frac{\alpha}{1-\alpha}\right).
  $$
  Drift is intentionally excluded from this calculation — "when did the reaction finish" should not depend on how badly the plate was evaporating afterward.
- T-lag
  

$F_{ss}$ is the fluorescence at steady state before drift, $k$ is how fast the reaction crosses its midpoint, $\tau_{vel}$ is the inflection point of the reaction.), $d$ is the rate of drift and $\tau_{drift}$ is the time when drift starts contributing.

:::{figure} #fig:kinetics
:name: fig-kinetics
:align: center
:width: 50%

Example reactions (10 $\mu$L PURE in triplicate at typical composition) fit to a logistic curve with linear drift. Dots represent fluorescence at each timepoint (individual replicates in blue, mean of replicates in green). Diagnostic parameters time to steady state ($t_{steadystate}$), lag time ($t_{lag}$), and maximum velocity ($V_{max}$) are plotted as well. Vertical and horizontal dashed red lines represent time to steady state and steady state fluorescence ($F_{ss}$), respectively. Orange dashed line represents the tangent line at the inflection point. The slope of this line is $V_{max}$ and the x intercept of this line is $t_{lag}$. The fitted curve is plotted as a red dashed curve on top of data points. 
:::

Using this mathematical model, we can extract forms for the following useful parameters:


| Parameter                 | Symbol         | Units            | Description                                                                                                                                                                                                                                                                      |
| ------------------------- | -------------- | ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Steady State Fluorescence | $F_{ss}$       | fluorescence units ($u$)              | How much total protein is expressed over the whole reaction? Fit explicitly in the model above.                                                                                                                                                                                  |
| Time to Steady State      | $\tau_{ss}$    | time (typically $h$)              | How long does it take for the reaction to reach steady state?                                                                                                                                                                                                                    |
| Lag Time                  | $\tau_{lag}$   | time (typically $min$)              | How long does it take for the reaction to start? This is roughly correlated with transcription lag time + translation lag time + maturation time of GFP. We calculate this as the x-intercept of the line tangent to the inflection point on the sigmoid |
| Maximum Velocity          | $V_{max}$      | fluorescence over time ($u \cdot h^{-1}$) | How fast is GFP getting produced at the fastest production rate in the reaction? This is the velocity of the reaction at $\tau_{max}$ and the slope of the line tangent to the inflection point and equals $F_{ss} * k / 4$^*                                 |
| Drift Rate                | $d$            | fluorescence over time ($u \cdot h^{-1}$) | If the reaction shows drift after steady state, how fast does it drift?                                                                                                                                                                                                          |
| Drift Onset Time          | $\tau_{drift}$ | time (typically $h$)              | If the reaction shows drift after steady state, when does it start to drift?                                                                                                                                                                                                     |

Notably, we have three derived quantities 
- insert box I sent you here? [Jon]
  
# How do we fit kinetic parameters in practice?
We use the `cdk` to fit our curves and extract those parameters automatically. 
This primer assumes you already have:

- a plate-reader export the CDK can ingest (BioTek, Cytation, or Envision; see [`cdk.instrument.platereader`](https://github.com/bnext-bio/bnext/tree/main/cdk/src/cdk/analysis/cytosol)),
- a platemap that labels each well with a condition (see the *Why you should use a platemap* DevNote),
- at least one fluorescent standard on the plate (see the *Why you should use standards* DevNote).

If any of those is missing, fix that first — fitting a curve to uncalibrated, unlabeled data just produces better-looking garbage. (JON: too hot of a take? haha pls feel free to remove)

- Look at this notebook
- Here are the plots you get

The minimum viable call is:

```python
from cdk.analysis.cytosol import platereader as pr

data = pr.load_platereader_data(
    path="20260416-my-experiment/",
    platemap="platemap.csv",
)

pr.plot_kinetics(data, fit_function_name="sigmoid_drift")
```

That produces, per condition group, (a) the overlaid raw traces with the fit, (b) a summary plot of `A`, `Vmax`, and `t_α`, and (c) a tidy DataFrame of fit parameters

**Default worth knowing.** The CDK currently defaults to fit_function_name="sigmoid_drift". If you truly dont want drift modeled, call "sigmoid"


:::{tip}
Check out this example jupyter notebook!
:::

## Common pitfalls

**Truncated saturation.** If the reaction hasn't actually plateaued by the last time-point, `A` is unconstrained and the optimizer will cheerfully return a garbage fit with small residuals. We are working on building checks for this.

**Reporting uncalibrated RFU.** `A` is in the reader's native fluorescence units until you normalize by a standard. For within-plate comparisons this is sub-par; for anything that leaves the plate, apply the standards pipeline first.

## When the sigmoid isn't enough

The sigmoid is a *phenomenological* fit: it is good at summarizing a well-behaved trace in four numbers, and bad at everything else. Specifically, it cannot represent:

- asymmetric rise/fall (use Gompertz or a generalized sigmoid),
- a biphasic reaction where a module kicks in mid-run (e.g., ClpXP-mediated degradation catching up to production),
- explicit resource-exhaustion dynamics that a mechanistic model could represent.



# What's coming next for kinetic analysis?
Our next Kinetics DevNote will cover how to select among these fits, how to report **credible intervals** on `A`, `Vmax`, and `t_α` instead of point estimates. 
- RNA aptamers allow us to measure transcription rate directly. This allows us to directly observe the transcription/translation rate trade off.
- Mechanistic modeling.
- Confidence intervals 

# Other things to watch out for
- Fluorescence standards help you normalize your reactions for differences across platereaders and experimental conditions, check it out!
- Platemaps help standardize data representation, making it easy to compare data across experiments and teams.
- Here is a cool dataset that demonstrates all of these things put together.