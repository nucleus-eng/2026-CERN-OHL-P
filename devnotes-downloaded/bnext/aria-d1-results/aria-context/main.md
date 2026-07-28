---
abstract: |
  We will deploy the IGOR (Iterative Guide and Orchestrated Research) AI scientist to develop and optimize two metabolic energy modules and integrate them into the PURE cell-free system: PPK, a single-enzyme kinase; and glycolysis, a 10-enzyme pathway as-yet unimplemented in PURE. Success will increase the productivity of the PURE system, create new tools and avenues for energy system research, and enable development of more sophisticated cell-free and synthetic cell applications in line with ARIA’s Bioenergetic Engineering and Manufacturing Abundance opportunity spaces. Moreover, success will demonstrate IGOR’s capability to rapidly and effectively develop, optimize, and integrate synthetic biological systems in complex high-dimensional experimental landscapes, opening powerful opportunities for AI scientists to accelerate development in bioenergy and elsewhere. 
---

# Background


IGOR is a multi-agent AI scientist integrated with an empirically-grounded Bayesian engine to thwart hallucination and drive effective science. The Bayesian engine comprises a neural network ensemble trained on empirical data combined with an acquisition-function-based Bayesian optimization routine to efficiently optimize the underlying experimental process in light of research goals [](https://findwhatmatters.ai/ai-process-assay-optimization.pdf). The AI scientist [](https://doi.org/10.48550/arXiv.2502.18864), through the Bayesian engine, is anchored to ground-truth through its training data and a suite ofmodeling inductive biases that are consistent with characteristics of scientific data.



:::{figure} general/overview.png
:label: scheme

Workflow and platform. (top) IGOR is a closed loop AI scientist framework that autonomously generates hypotheses, DOEs, data interpretation, and publications, in tandem with the b.next experimental, open data, and publication platform. (left) IGOR is composed of scientific LLM agents, grounded by an empirical Bayesian engine.(center) AI-published open data, findings, and concrete biotechnology open new frontiers of science and engineering. (right) Project timeline.

:::




# Research Challenge

Our AI scientist will identify and publish two optimized energy modules—PPK (Base) and Glycolysis (Extension)—as a specification of the optimal identities and concentrations for the module components and the 108 underlying PURE components, as well as mechanistic interpretation, supporting data, and scientific context. PPK complements native PURE creatine–phosphate metabolism by using polyphosphate as a substrate to phosphorylate AMP, ADP, and GDP [](https://doi.org/10.1021/acssynbio.9b00456). 

Our preliminary results show that PPK increases PURE protein yield by 97%, but that optimization within PURE across the total design space of 110 system components should further increase productivity.16 Glycolysis—a 10-enzyme pathway which produces ATP from glucose—has not been implemented in PURE, would open up implementation of and integration with further metabolic pathways (such as the citric acid cycle), and may require up to 17 supplementary enzymes to achieve metabolic balance [](https://doi.org/10.1038/ncomms15526). Here, IGOR will iterate within a design space of at least 129 components (enzymes and intermediates) against a mechanistically complex and as-yet unexplored challenge. 

Success will require IGOR to draw novel insight from existing literature and the data it collects during the Base challenge and then to efficiently and effectively explore and optimize the integrated system. IGOR’s ability to integrate ground-truth data, literature, and its own insight to explore combinatorially large design spaces make it well-matched for this task. 



# Workflow 

IGOR will perform hypothesis generation, design of experiments, interpretation, and publication using three key agents.

:::{card}
:header: **Key agents**
:footer: *An additional orchestrator agent can call any other agent during any part of the workflow to refine output.* 

**Generation:** uses contextual information (e.g., data, powerpoints, papers, figures) in tandem with the Bayesian engine to generate candidate hypotheses.

**Reflection:** evaluates, compares, evolves, and ranks the generated hypotheses.

**Meta-analysis:** synthesizes emergent insights using all available context.

:::



IGOR integrates results, designs new experiments to achieve its objective (in this case, increased protein yield), and simultaneously interprets the results in context to write and publish Developer Notes ([](#scheme)). Experimental design, assembly, analysis, and publication will be performed autonomously, while human scientists will support experimental operations (supervising instruments, preparing reagents, etc.) and oversee experimental progress and safety. Domain experts will supervise IGOR’s experimental output to provide a point of comparison and guide adjustments to the project design and objective as necessary (while explicitly avoiding the design of specific experiments). 
