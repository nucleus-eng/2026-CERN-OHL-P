---
# Ensure that this title is the same as the one in `myst.yml`
title: Energy Metabolism Working Group at Build-a-Cell
abstract: |
  The 15th Build-a-Cell Workshop was held at the University of Michigan, Ann Arbor, bringing together researchers to critically examine foundational challenges in synthetic cell development. The workshop facilitated the formation of several working groups, each addressing key aspects of synthetic cell design, ranging from computational modeling to intercellular communication systems. Among these, we led a working group dedicated to identifying and addressing critical limitations in energy regeneration and metabolism within synthetic cells (SynCells) and cell-free systems more broadly. This DevNote presents a summary of the major themes and insights that emerged from the working group discussions, and outlines a few strategies for improving energyy metabolism in SynCells. 
---

The working group aimed to address bottlenecks in current energy metabolism that limit the lifetime of cell-free and syncell systems. We discussed key potential bottlenecks in the current state of the system, highlighted below:

1. NTPs and amino acids (energy solution) were identified as the main limiting components in cell-free and syncell systems. PURE reactions have been shown to last multiple days when run in dialysis compartments with energy solution serving as the feeding solution to replenish substrates such as amino acids and NTPs ([Julia et al. 2025](https://pubs.acs.org/doi/10.1021/acssynbio.4c00618), [ Kazuta et al. 2014](https://doi.org/10.1016/j.jbiosc.2014.04.019)).
2. Thermally stable energy substrates to regenerate ATP for longer lifetimes is an important challenge. The current substrate (creatine phosphate) is not stable at room temperature and degrades within a few hours when incubated at 37°C.
3. Phosphate accumulation in the reaction caused by ATP hydrolysis from protein synthesis may chelate magnesium ions or cause a drop in pH. This inhibits the system through its own by-product as magnesium ions are critical cofactors for certain enzymes involved in the transcription and translation machinery. The current energy regeneration scheme using creatine phosphate and creatine kinase doesn't address this, as phosphate accumulates in the reaction at milli molar concentrations. New thermally stable substrates and metabolic pathways for energy regeneration should be chosen to overcome or avoid the phosphate accumulation problem.

**Application Outlook:** We want to make syncell and cell-free systems perform for multiple days. How we achieve this depends on the intended application. Do we want them to run slower and last for multiple days, or do we want them to maintain the same efficiency but for multiple days? The answer will determine our strategy, but it's better to have solutions for both types of applications.

**ATP Regeneration Strategies:** We explored two approaches for ATP regeneration. The first is a practical, near-term solution using metabolic pathways and thermally stable substrates to provide energy for protein synthesis. The second is more complex but may offer a more efficient long-term solution.
1. Short-term solutions; thermally stable substrate
   - 3-Phosphoglyceric acid (3-PGA): 3-PGA combined with lower glycolysis enzymes can power protein synthesis. This is a more suitable option because 3-PGA is much more stable at room temperature than creatine phosphate, remaining stable for over 24 hours. This stability can help achieve multi-day lifetimes, provided other components such as amino acids don't become limiting factors.
   - Glycolysis: Glycolysis is a strong alternative for powering syncells using stable and inexpensive substrates like glucose. However, the pathway is highly regulated and not energy efficient, it consumes ATP in its first half, creating a tug-of-war for ATP between glycolysis and protein synthesis ([Sato et al. 2024](https://pubs.acs.org/doi/10.1021/acssynbio.4c00209)). We need alternative pathways that bypass the energy-consuming, highly regulated first part of glycolysis. One approach is to use maltodextrin as a substrate instead of glucose, utilizing maltodextrin phosphorylase and phosphoglucomutase enzymes to bypass the first step and obtain glucose-6-phosphate directly.
2. Long-term solutions; light-powered energy production
   - Bacteriorhodopsin and ATP synthase: Powering synthetic cells through bacteriorhodopsin and ATP synthase in a vesicle has been demonstrated ([Berhanu et al. 2019](https://doi.org/10.1038/s41467-019-09147-4)). This method uses light as the sole energy source to create a proton motive force, which drives ATP synthase to produce ATP as protons flow out of the vesicle. It recycles phosphate and requires no chemical substrate. Though this is a preferable method to power syncells, the implementation is complex and would require significant optimization to work reliably over long periods.
   - Oxidative phosphorylation: Another method to power syncells is oxidative phosphorylation. This can be achieved by purifying mitochondria and adding them inside the syncell ([Li et al. 2022](https://doi.org/10.1002/adma.202204039)), or by reconstituting the electron transport chain and ATP synthase in a vesicle ([Biner et al.](https://doi.org/10.1021/acssynbio.0c00110)). However, both approaches are extremely challenging to implement. They require targeted, focused efforts from many researchers due to the complexity of working with multiple membrane proteins and optimizing the many parameters in such complex systems.

:::{figure} ./figures/fig1.png
:name: fig1
:align: center
:width: 50%

Schematics of the artificial photosynthetic cell encapsulating artificial organelle, which consists of bacteriorhodopsin (bR) and FoF1-ATP synthase (FoF1). Figure adapted from [Berhanu et al. 2019](https://doi.org/10.1038/s41467-019-09147-4).
:::

To better understand syncell and cell-free systems, we need to perform key measurements that can guide our approach:
1. ATP measurement: Luciferase for destructive measurement; Queen sensors and ATeam sensors (FRET-based sensors for ATP/ADP ratios)
2. Phosphate measurement assays to quantify inorganic phosphate accumulation over time in cell-free reactions
3. pH measurements over time to track changes in pH when cell-free systems are powered by different energy substrates and metabolic pathways.

---

**Participants:** Sung-Won Hwang (University of Michigan), Aisha Elsawah (Université Paris-Saclay, INRAE, Paris), Manuel Bibrowski (Imperial College London), Chengyen Lin (University of Michigan), Dale Landas (ERDC), Hyunjung Kim (ERDC), Javin Oza (Cal Poly SLO), Charles Rumberger (AFRL), and Surendra Yadav (b.next)
