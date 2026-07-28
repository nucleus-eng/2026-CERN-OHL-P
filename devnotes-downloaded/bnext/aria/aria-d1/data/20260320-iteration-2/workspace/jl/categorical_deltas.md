 For upcoming experiments, several choices of method, parameter or equipment were enforced at suggestion-generation time to advance process development. Each choice led to a decrease in mean predicted fluorescence compared to the same (re)prediction for the choice made for the most-fluorescent experiment in the existing dataset. Switching from NEB solution B and introducing RNAase inhibitor each had only a marginal effect, however. Optimization of the remaining parameters was able to compensate for most of the loss due to elimination of PEG, but not elsewhere.

| feature name(s)	| setpoint(s) of previous best | new forced setpoint(s)	| mean fluorescence change due to category switch | mean fluorescence change due to optimization |
| --- | --- | --- | --- | --- |
| PMix is NEB Sol B | True | False | -0.08 | 0.02 |
| [PEG] (%) | 2 | 0 | -0.41 | 0.35 |
| [RNase Inhib] (U/mL) | 0 | 2000 | -0.04 | 0.02 |
| Reader Type, Gain, Read Type | Synergy 2, 35, F | Cytation5, ext, M | -0.52 | 0.07 |
| Product | plamGFP | deGFP | -0.33 | 0.04 |
| Experiment | Genscript-PPK-custom-Smix | 20260319-DiscoveryPlate-R2 | -0.38 | 0.04 |
| Condition | R&D | Labcraft | -0.57 | -0.02 |

Table explanation: Nine essentially categorical features had pre-specified values; Reader Type, \[Reader\] Gain and Read Type were combined giving the seven rows in the table. Experimental suggestions were generated at all 128 combinations of previous and new setpoints, with the remaining, continuous setpoints allowed to float within the range of existing experimental data points. Of all the paths from the all-previous to the all-new corner that change only one category at a time, the one with the least total variance of the sigmoid_steady_state prediction was selected in an attempt to stay within the best-predicted region. Along this path, the mean predictions for sigmoid_steady_state were calculated as the setpoints were changed one by one, alternating with re-optimization at the new points. The differences are reported in the table. Note the *decrease* in optimizing after the last, Labcraft step: by this point the prediction was so far from the fluorescence goal of 3 that the optimizer began trading off mean prediction for variance as it determined it needed to explore more aggressively.