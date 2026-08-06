---
title: "Synthetic Cells Course Lab Manual: Cell-free Gene Expression and Liposome Encapsulation"
authors:
  - name: Javin P Oza
    corresponding: true
    email: joza@calpoly.edu
    orcid: 0000-0002-2902-6939
    affiliations:
      - name: California Polytechnic State University, San Luis Obispo, CA, USA
date: # REVIEW: not found in source
license: CC-BY-4.0
thumbnail: # REVIEW: rename figures/media/image5.png to descriptive name and set here
collections:
  - REVIEW: inferred — nucleus-contrib, devcells-node
---

<!-- REORDERED: moved from "NEB PURExpress Cell-Free Reaction > Background" and "Nucleus PURE Cell-Free Reaction > Background" to match style guide -->

:::{note}
This DevNote adapts existing Nucleus protocols for use in an undergraduate teaching course. The materials in this DevNote were used as course material in CHEM 471 at California Polytechnic State University (Cal Poly) to introduce students to synthetic cell engineering. [Learn more about the Cal Poly course.](https://www.sanluisobispo.com/news/health-and-medicine/article316414732.html)
:::

# Overview

A synthetic cell requires three core systems: a cytosol (the molecular
machinery for gene expression), an energy source (to power that
machinery), and a membrane (to define the cell boundary). You will build
cytosols using PURExpress — a reconstituted cell-free system composed of
purified components, then you will encapsulate these cytosols inside
lipid vesicles to create complete synthetic cells.

## The PURExpress System

[PURExpress](https://www.neb.com/en-us/products/e6800-purexpress-invitro-protein-synthesis-kit) (New England Biolabs) is a reconstituted cell-free
transcription-translation system. Unlike crude cell extract systems,
every component is purified and defined. The system is packaged into two
master solutions:

| Component | Contents & Function |
|-----------|---------------------|
| Solution A | Contains the small-molecule substrates and enzymes needed for transcription and translation: NTPs (ATP, GTP, CTP, UTP) for RNA synthesis; Amino acids for protein synthesis; T7 RNA polymerase for transcription; Translation factors (IF1, IF2, IF3, EF-Tu, EF-Ts, EF-G, RF1, RF2, RF3, RRF); Aminoacyl-tRNA synthetases (20 enzymes, one per amino acid); tRNAs; Energy regeneration system: creatine phosphate + creatine kinase (CP/CK); Salts, buffer, and cofactors (including Mg{sup}`2+`) |
| Solution B | Contains ribosomes — the molecular machines that translate mRNA into protein. HANDLE GENTLY. Never vortex Solution B. |

PURExpress is uniquely simple: you combine Solution A + Solution B +
your DNA template, and the system transcribes and translates your gene
of interest. All the complexity of 100+ purified components is pre-mixed
for you.

## The CP/CK Energy System

Protein synthesis consumes large amounts of ATP and GTP. Without energy
regeneration, nucleotide triphosphates are depleted within minutes. The
creatine phosphate/creatine kinase (CP/CK) system, built into standard
Solution A, regenerates ATP by transferring a phosphate from creatine
phosphate (CP) to ADP. This sustains protein production for 2--4 hours
before CP is depleted.

## Reporters

The DNA you will use is pOpen-deGFP, which expresses green fluorescent
protein (excitation 488 nm, emission 509 nm). By expressing fluorescent
proteins from the template DNA plasmid, you can monitor protein
synthesis in real time. As RNA is translated, fluorescence increases
proportionally. Fluorescent proteins 'mature' to form a chromophore
which provides a continuous, quantitative readout of translation
activity.

## The b.next Nucleus PURE System

[Nucleus Cytosol](https://docs.nucleus.engineering/docs/modules/base-cytosol/spec/) ([b.next](https://bnext.bio/)) is an open-source alternative to commercial PURE-based systems like NEB PURExpress. It's built on the same underlying PURE architecture, a fully reconstituted, defined transcription-translation system, but rather than being pre-packaged into two ready-to-use solutions, it's supplied as four separate, individually defined components:

| Component | Contents & Function |
|-----------|---------------------|
| PMix (Protein mix) | Contains the proteins needed for transcription and translation: T7 RNA polymerase for transcription; Translation factors (IF1, IF2, IF3, EF-Tu, EF-Ts, EF-G, RF1, RF2, RF3, RRF); Aminoacyl-tRNA synthetases (20 enzymes, one per amino acid); Methionyl-tRNA formyltransferase, Creatine kinase, adenylate kinase, nucleoside diphosphate kinase, inorganic pyrophosphatase for metabolism. |
| SMix (Small Molecule Mix) | NTPs (ATP, GTP, CTP, UTP) for RNA synthesis; 20 Amino acids for protein synthesis; Creatine phosphate, folinic acid cofactors; HEPES-KOH, potassium glutamate, magnesium acetate buffers; Spermidine, TCEP stabilizers. |
| tRNAs | Purified from E. coli strain A19 — attaches amino acids to a protein chain by reading mRNA code. |
| Ribosomes | Purified from E. coli strain A19 — ribosomes are the molecular machines that translate mRNA into protein. HANDLE GENTLY. Never vortex Ribosomes. |

Unlike PURExpress's "just add Solution A + Solution B + DNA" system, Nucleus Cytosol components' identities and concentrations are independently known, tunable, and — since it's open-source — inspectable and modifiable by the end user, rather than existing as a proprietary "black box" mixture.

---

# Cell-Free Protein Synthesis

<!-- REORDERED: moved from "NEB PURExpress Cell-Free Reaction" and "Nucleus PURE Cell-Free Reaction" protocol sections to match style guide -->

:::::{tab-set}

::::{tab-item} NEB PURExpress

**Materials:**

- PURExpress 6800L Kit (Solution A, Solution B)
- pOpen-dGFP: [DNA]= \_\_\_\_\_\_\_
- Murine RNase Inhibitor (40000 U/mL, 0.15 mL)
- Nuclease-free Water
- 2.5 μL micropipette
- 10 μL micropipette
- 20 μL micropipette
- 1.5 mL Microfuge Tube (6x)
- 384-well Black Bottom Plate\*

\*The 384-well plate will be shared among groups and kept on ice until students are ready to transfer their complete reactions.

**Safety:** Goggles and Nitrile Gloves should be worn while handling all reaction components. Dispose of tubes and micropipette tips in designated waste.

**Protocol: Adapted from the New England Biolabs® Protein Synthesis Reaction**

Assembling the Reaction:

- Thaw Solution A, Solution B, RNAse Inhibitor, and your plasmid on ice. Keep all empty reaction tubes (in tube rack, if available) on ice as well. Preparation on ice ensures that reagents remain stable, and protein expression does not begin during assembly.
- Flick to mix Solution A and B before using to resuspend any pellet that formed during storage. [Do not vortex Solution B]
- Label six PCR tubes on ice:
  a) "CP/CK-1", "CP/CK-2", and "CP/CK-3" (triplicate positive reactions)
  b) "--DNA-1", "--DNA-2" and "--DNA-3" (triplicate negative controls)
- Calculate the amount of DNA to add so that final [DNA] in solution is equal to 10 ng/µL using C{sub}`1`V{sub}`1`=C{sub}`2`V{sub}`2`.
- Assemble the following reactions in their respective microcentrifuge tubes, adding the reactants in the specified order.

**Technical Tips for success**

- Thoroughly pipette/flick mix all reagents before pipetting into your reaction tube.
- Ensure there are no bubbles in the micropipette tip before transferring a reagent to a reaction tube.
- When pipetting into your reaction tube, the micropipette tip should be touching the inside of the tube, and you should visualize the droplet leaving the micropipette.

DNA template used: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Stock Concentration: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

:::{table} NEB PURExpress Reaction Composition
| Component | +DNA PURExpress [µL] | --DNA Control [µL] |
|-----------|----------------------|--------------------|
| Solution A | 10.0 | 10.0 |
| Solution B | 7.5 | 7.5 |
| RNase Inhibitor (optional) | 1.25 | 1.25 |
| DNA template: \_\_\_\_\_ | TBD | — |
| Nuclease-free H{sub}`2`O | to 25 µL | 6.25 |
| Total Volume | 25 | 25 |
:::

- Close lids to all tubes and microfuge at 5 RPM for ~10s to collect all reagents at the bottom of the tube
- Your instructor will assign you which wells to pipette into. Record the grid letter(s) and number(s) to later identify your quantification.
- Pipette-mix each solution before transferring 8 μL of each into the 384-well plate. Set the micropipette to 8 μL and stop at the first stop when dispensing to prevent the introduction of bubbles into the sample. Pipette three wells for each reaction tube.
- After using each component, add a black dot to the tube lid with a lab marker. Each dot = one F/T cycle. If a tube has 5+ dots, notify the instructor.
- Return all components to −20°C (DNA, H{sub}`2`O, RNAse inhibitor) and -80°C (PURExpress Solution A and B) promptly.

Data Quantification: Real-time 4-hour fluorescence, incubated at 37 °C in the Synergy Plate reader, allowing the transcription and translation reactions to proceed within the tubes.

Clean Up: All used pipette tips and empty reaction tubes belong in the "used pipette tips" container on your lab bench. Ensure all reagents are on ice or stored properly before leaving your bench. Wash your hands thoroughly before leaving the lab.

::::

::::{tab-item} Nucleus PURE

**Materials:**

- pOpen-dGFP: [DNA]= \_\_\_\_\_\_\_
- Nuclease-free water
- SMix
- tRNA
- Pmix
- Ribosomes
- Murine RNase Inhibitor (40000 U/mL, 0.15 mL)
- 2.5 μL micropipette
- 10 μL micropipette
- 1.5 mL Microcentrifuge Tubes (6x)
- 384-well plate\*

\*The 384-well plate will be shared among groups and kept on ice until students are ready to transfer their complete reactions.

**Safety:** Goggles and Nitrile Gloves should be worn while handling all reaction components. Dispose of tubes and micropipette tips in designated waste.

**Protocol:**

Assembling the Reaction:

- Thaw all reagents on ice. Keep all empty reaction tubes (in tube rack, if using) on ice as well.
- Flick all tubes before using and keep all reagents on ice during your set up.
- Label six PCR tubes on ice:
  a) "CP/CK-1", "CP/CK-2", and "CP/CK-3" (triplicate positive reactions)
  b) "--DNA-1", "--DNA-2" and "--DNA-3" (triplicate negative controls)
- Calculate the amount of DNA to add so that final [DNA] in solution is equal to 6 ng/µL using C{sub}`1`V{sub}`1`=C{sub}`2`V{sub}`2`.
- Assemble the following reactions in their respective microcentrifuge tubes, adding the reactants in the order specified. Pipet mix each reactant before assembly.

**Technical Tips for success**

- Thoroughly pipette/flick mix all reagents before pipetting into your reaction tube.
- Ensure there are no bubbles in the micropipette tip before transferring a reagent to a reaction tube.
- When pipetting into your reaction tube, the micropipette tip should be touching the inside of the tube, and you should visualize the droplet leaving the micropipette.

DNA template used: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Stock Concentration: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

:::{table} Nucleus PURE Reaction Composition
| Component | Cytosol with CP/CK (µL) | Negative Control: Cytosol with CP/CK (No DNA) (µL) |
|-----------|-------------------------|------------------------------------------------------|
| SMix | 7.50 | 7.50 |
| tRNA | 2.50 | 2.50 |
| PMix | 3.00 | 3.00 |
| Ribosomes | 4.50 | 4.50 |
| RNAse Inhibitor | 1.25 | 1.25 |
| sfGFP: \_\_\_\_\_ | TBD | — |
| Water | To 25 µL | 6.25 |
| Total | 25 | 25 |
:::

- Close lids to all tubes and microfuge at 5 RPM for ~10s to collect all reagents at the bottom of the tube
- Your instructor will assign you which wells to pipette into. Record the grid letter(s) and number(s) to later identify your quantification.
- Pipette-mix each solution before transferring 8 μL of each into the 384-well plate. Set the micropipette to 8 μL and stop at the first stop when dispensing to prevent the introduction of bubbles into the sample. Pipette three wells for each reaction tube.
- After using each component, add a black dot to the tube lid with a lab marker. Each dot = one F/T cycle. If a tube has 5+ dots, notify the instructor.
- Return all components to −20°C (DNA, H{sub}`2`O, RNAse inhibitor) and -80°C (PURExpress Solution A and B) promptly.

Data Quantification: Real-time 4-hour fluorescence, incubated at 37 °C in the Synergy Plate reader, allowing the transcription and translation reactions to proceed within the tubes.

Clean Up: All used pipette tips and empty reaction tubes belong in the "used pipette tips" container on your lab bench. Ensure all reagents are on ice or stored properly before leaving your bench. Wash your hands thoroughly before leaving the lab.

::::

:::::

---

# Liposome Encapsulation

<!-- REORDERED: moved from "NEB PURExpress Encapsulation > Background" to match style guide -->

The objective of this lab is to successfully encapsulate PURExpress cell free protein synthesis system in liposomes and initiate a time trial to view the expression of deGFP inside a synthetic cell over a period of 4 hours.

Liposomes are spherical structures made from amphipathic lipids and are commonly used to model and encapsulate synthetic cells. The term "vesicle," derived from the Latin vesicula meaning "small bladder," refers to a compartment formed in vitro within an aqueous medium. Each vesicle consists of a small aqueous volume enclosed by one or a few thin membrane layers composed of amphiphilic molecules. These molecules contain both hydrophilic and hydrophobic regions and are bilayer-forming compounds such as phospholipids. They arrange themselves so that the hydrophilic heads face the surrounding aqueous environment, while the hydrophobic tails associate inward to form the interior of the bilayer. This arrangement creates a relatively permeable lipid bilayer that surrounds an aqueous core. Because liposomes form in aqueous solutions, they are able to encapsulate solutes present in the surrounding medium during their formation, making them highly useful tools for experimental investigation.

:::{figure} figures/media/image5.png
:label: fig-osmolarity
:width: 75%
An osmolarity/tonicity diagram showing three conditions side by side — cells in a hyperosmotic solution (0.2 M MgCl₂, 0.6 OsM) shrivel; isosmotic (0.5 M glucose, 0.5 OsM) normal; and a third condition (0.2 M MgCl₂ + 0.5 M glucose, 1.1 OsM) labeled "Hypoosmotic solution" where cells swell and burst.
:::

Although they mimic key features of living cells, liposome-based synthetic cells have much simpler membranes. In contrast to the fluid mosaic membrane of living cells, which contains a complex mixture of proteins, glycoproteins, glycolipids, cholesterol, and other components, liposomes typically include only a limited number of membrane proteins required to perform basic functions. This simplicity provides students and researchers with a more controlled and manageable environment for studying membrane dynamics and cellular processes and reactions. In typical laboratory preparations, the lipid solution used to form liposomes contains phospholipids, cholesterol, and a red dye attached to a modified phospholipid tail, which causes the membrane to appear red under a microscope.

:::{figure} figures/media/image6.png
:label: fig-emulsion-transfer
:width: 75%
Cartoon showing the emulsion transfer method workflow.
:::

An essential factor in successfully forming and maintaining liposomes is osmolarity, or the concentration of solutes inside and outside the synthetic cell. The balance of solute concentrations across the lipid bilayer directly influences water movement through osmosis. If the external solution is hypotonic (lower solute concentration than inside the liposome), water will move into the vesicle, causing it to swell and potentially burst. If the external solution is hypertonic (higher solute concentration than inside), water will move out, leading the vesicle to shrink or collapse. Therefore, carefully adjusting the osmolarity of the surrounding solution is critical in preventing membrane rupture and ensuring the stability and success of liposome-based synthetic cell experiments. The osmolarity of the inner solution (cytosol) should be about 100 units larger than the osmolarity of the outer solution, such that the cells will be slightly turgid from the influx of water, making them easier to visualize, but not turgid enough to cause the cells to burst ({ref}`fig-osmolarity`).

## What Is in the Mix?

The lipid-oil solution you will use to form liposomes contains three lipid components dissolved in mineral oil. Each plays a distinct role in forming the membrane that will compartmentalize your fluorescein.

:::{figure} figures/media/image7.png
:label: fig-popc
:width: 75%
[POPC](https://en.wikipedia.org/wiki/POPC) (1-palmitoyl-2-oleoyl-sn-glycero-3-phosphocholine)
:::

POPC (1-palmitoyl-2-oleoyl-sn-glycero-3-phosphocholine) ({ref}`fig-popc`) is a phospholipid and the primary structural lipid, comprising roughly 79 mol% of the mixture. POPC is a phosphatidylcholine, meaning it has a hydrophilic headgroup (a phosphate linked to a choline) and two hydrophobic fatty acid tails (one saturated 16-carbon chain and one unsaturated 18-carbon chain with a single cis double bond at position 9). This asymmetry in tail structure is important: the kinked oleoyl chain prevents tight packing, keeping the bilayer fluid at room temperature. POPC is one of the most abundant phospholipids in eukaryotic cell membranes, making it a biologically relevant choice for a model membrane. In your lipid mix, POPC does the heavy lifting of forming the bilayer itself.

:::{figure} figures/media/image8.png
:label: fig-cholesterol
:width: 75%
[Cholesterol](https://en.wikipedia.org/wiki/Cholesterol)
:::

Cholesterol ({ref}`fig-cholesterol`) makes up approximately 20 mol% of the mixture. In natural cell membranes, cholesterol inserts between phospholipid molecules, positioning its hydroxyl group near the phospholipid headgroup region and its rigid steroid ring system alongside the fatty acid tails. This has two major effects: it reduces membrane permeability to small water-soluble molecules by filling gaps between phospholipid tails, and it increases mechanical stability of the bilayer without making it rigid. Cholesterol also modifies the T{sub}`m` of the membrane, broadening the temperature range over which the membrane remains stable, giving you more experimental flexibility.

:::{figure} figures/media/image9.png
:label: fig-liss-rhod-pe
:width: 75%
[18:1 Liss Rhod PE](https://www.avantiresearch.com/en-gb/products/product/810150-181-liss-rhod-pe) (lissamine rhodamine B-labeled phosphatidylethanolamine)
:::

Liss-Rhod PE (lissamine rhodamine B-labeled phosphatidylethanolamine) ({ref}`fig-liss-rhod-pe`) is present at roughly 1 mol%. This is a phospholipid with a covalently attached rhodamine fluorophore on its headgroup. It incorporates directly into the bilayer and allows you to visualize the membrane under fluorescence microscopy (excitation ~638 nm on the Squid, appearing red/magenta). Because it is a true membrane component rather than a soluble dye, it marks the bilayer specifically. On the microscope, you will see the membrane as a bright ring surrounding each vesicle in the 638 nm channel. This lets you distinguish intact vesicles from debris, oil droplets, or aggregates, and it lets you confirm whether a green fluorescence signal (fluorescein, 488 nm channel) is actually inside a compartment or just free in solution. A vesicle visible at 638 nm but not at 488 nm tells you the membrane formed, but fluorescein was not trapped inside, either because the droplet was empty or because the contents leaked. Without the fluorescent lipid marker, you would have no way to find your vesicles or distinguish a membrane-bound compartment from a fluorescent smear.

Mineral oil is the solvent that carries these lipids. It is a mixture of long-chain alkanes and cycloalkanes that is immiscible with water. The oil serves as the continuous hydrophobic phase during vesicle formation.

## How the Mix Is Prepared (you don't need to do this)

The lipid-oil solution is prepared for you in advance but understanding how it is made will help you interpret your results.

The three lipid components arrive from the supplier (Avanti Polar Lipids) as stock solutions dissolved in chloroform, a common solvent for lipids because it is nonpolar enough to solubilize the fatty acid tails while being volatile enough to remove later. Preparation proceeds as follows:

1. Mineral oil (3--5 mL) is added to a clean glass vial.
2. Using a glass syringe, the lipid stocks in chloroform are drawn up and injected into the mineral oil at the correct molar ratio (79:20:1 POPC:cholesterol:Liss-Rhod PE).
3. The mixture is vortexed briefly (~10 seconds) in a fume hood.
4. The vial is covered with aluminum foil and placed in a 55°C dry bath for 4 hours.

The 4-hour incubation at 55°C drives off the chloroform, which is volatile (boiling point 61°C). What remains is a clear solution of lipids dispersed in mineral oil with no residual chloroform. Temperature control matters here. Below 50°C, chloroform evaporation is incomplete, and residual solvent can destabilize vesicles or be toxic to biological reactions in later experiments. Above 60°C, unsaturated lipids like POPC begin to oxidize, producing degradation products that compromise membrane integrity.

The result is a lipid-in-oil solution where lipid molecules are dispersed at the molecular level throughout the mineral oil phase. This is the starting material you receive for vesicle formation.

## How It Becomes a Liposome: The Emulsion Transfer Method

The emulsion transfer method (also called inverted emulsion) converts the lipid-oil solution into bilayer vesicles, encapsulating your fluorescein ({ref}`fig-emulsion-transfer`). The process builds the bilayer in two stages, depositing one lipid monolayer at a time.

Stage 1: Water-in-oil emulsion. You pipette 150 µL of the lipid-oil solution on top of your fluorescein/OptiPrep inner solution (~39 µL) in the E tube and emulsify by running the tube vigorously along the tube rack (40--50 passes). This shears the aqueous solution into tiny droplets suspended in the oil phase. At each oil-water interface, lipid molecules spontaneously orient with their hydrophilic headgroups facing the aqueous droplet and their hydrophobic tails extending into the oil. Each droplet is now coated with a single lipid monolayer. Your fluorescein is inside these droplets.

Stage 2: Monolayer-to-bilayer transfer. You layer this emulsion on top of the glucose outer solution (300 µL) in the T tube and centrifuge at 9,000 × g for 10 minutes. The aqueous droplets are denser than oil (the OptiPrep in your inner solution helps ensure this), so they sediment downward through the oil phase toward the aqueous outer solution. At the oil-water interface between the oil layer and the outer solution, a second population of lipid molecules has already assembled into a monolayer (headgroups facing the aqueous outer solution, tails facing the oil). As each droplet passes through this interface, it picks up this second monolayer. The droplet now has two monolayers oriented tail-to-tail: a lipid bilayer. The vesicle, now enclosed in a complete membrane, settles into the outer aqueous phase as a liposome.

The resulting vesicles are typically 1--50 µm in diameter, comparable in size to eukaryotic cells and large enough to image individually under a light microscope. Encapsulation efficiency is generally 5--20%, meaning most of your fluorescein volume remains in the emulsion or oil phase rather than inside vesicles.

## Why This Matters for Your Liposomes

The composition and preparation of the lipid-oil mix directly affect whether encapsulation succeeds. Several consequences are worth understanding as you work through the protocol:

Membrane composition controls permeability. Fluorescein is a small molecule (MW ~332 Da) that can slowly leak across lipid bilayers. The combination of POPC and cholesterol creates a bilayer that is fluid enough to form vesicles but tight enough to retain encapsulated fluorescein for the duration of your experiment. If cholesterol were omitted, you would see faster leakage and a weaker distinction between lumenal fluorescence and background.

Osmotic balance determines vesicle stability. This is the central variable in your experiment. You are testing three different glucose concentrations in the outer solution to find the osmolarity that produces the best liposomes. If the outer solution is slightly hypotonic relative to the inner solution (lower osmolarity by ~100--120 mOsm), vesicles remain gently inflated and round, which is ideal for imaging. If the osmolarities match exactly, vesicles may appear flaccid or irregularly shaped. If the outer solution is far too dilute, vesicles swell and burst. You will measure osmolarity with the vapor pressure osmometer before encapsulation, so you know the actual values you are working with, not just the nominal glucose concentrations.

OptiPrep provides the density gradient. The small amount of OptiPrep (iodixanol) mixed into your fluorescein inner solution increases its density above that of mineral oil. Without this density agent, the aqueous droplets would not sediment efficiently through the oil layer during centrifugation, and you would recover very few vesicles. OptiPrep is biologically inert and optically transparent, so it does not interfere with fluorescence imaging.

Residual chloroform or oxidized lipids compromise membranes. If the lipid-oil preparation were done at too low a temperature, trace chloroform in the oil phase would partition into the aqueous droplets during emulsification and could destabilize membranes or produce leaky vesicles. Similarly, oxidized POPC (from overheating during preparation) inserts into the bilayer and increases permeability unpredictably. This is why the lipid-oil solution is prepared carefully in advance for you.

The fluorescent lipid enables quality control. Liss-Rhod PE lets you assess encapsulation success in real time on the microscope. In the 638 nm channel, a bright, continuous ring indicates an intact bilayer membrane. Dim or patchy fluorescence suggests incomplete membrane formation. Green fluorescence (fluorescein, 488 nm channel) inside a red ring confirms successful encapsulation. A vesicle visible at 638 nm but not at 488 nm tells you the membrane formed, but fluorescein was not trapped inside, either because the droplet was empty or because the contents leaked. Without the fluorescent lipid marker, you would have no way to find your vesicles or distinguish a membrane-bound compartment from a fluorescent smear.

:::::{tab-set}

::::{tab-item} NEB PURExpress

**Materials (NEB PURExpress Encapsulation):**

- PURExpress 6800L Kit (Solution A, Solution B)
- pOpen-dGFP: [DNA]= \_\_\_\_\_\_\_
- Murine RNase Inhibitor (40000 U/mL, 0.15 mL)
- OptiPrep Density Gradient Medium
- Nuclease free water
- 2.5 μL micropipette
- 10 μL micropipette
- 20 μL micropipette
- 200 μL micropipette
- 1000 μL micropipette
- 1.5 mL Microcentrifuge Tubes (12x)
- Glucose solution (800mM and 900mM)
- Lipid-Oil Solution
- 384-Well clear-bottom plate\*

\*The 384-well plate will be shared among groups and kept on ice until students are ready to transfer their complete reactions.

**Safety:** Goggles and Nitrile Gloves should be worn while handling all reaction components. Dispose of tubes and micropipette tips in designated waste. Avoid looking into intense light sources when using microscopes.

**Protocol (NEB PURExpress Encapsulation):**

Assembling the reaction:

- Label 12 tubes, five of each of the following:
  - E — oil emulsion (E)
  - T — transfer (T)
  - L — liposomes (L)
- Calculate the amount of DNA to add so that final [DNA] in solution is equal to 10 ng/µL using C{sub}`1`V{sub}`1`=C{sub}`2`V{sub}`2`.
- Create PURExpress cytosol for encapsulation. Keep all reagents and reactions on ice throughout. Preparation on ice ensures that protein expression does not begin during assembly. Pipette the following reagents in the tube "E" in the order listed. Repeat for each "E" tube (3x).

DNA template used: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Stock Concentration: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

:::{table} NEB PURExpress Encapsulation Composition
| Component | Cytosol with CP/CK (µL) |
|-----------|-------------------------|
| Optiprep | 1.4 |
| Solution A | 16 |
| Solution B | 12 |
| RNAse Inhibitor | 2 |
| DNA: \_\_\_\_\_\_\_\_\_ | TBD |
| Nuclease-free H{sub}`2`O | To 40 µL |
| Total Volume | 40 |
:::

- Pipette mix each reaction, then centrifuge each reaction at 5000g [6685 RPM for tabletop centrifuges (r=10 cm)] for 30 seconds to spin down bubbles in the reaction.
- After using each component, add a black dot to the tube lid with a lab marker. Each dot = one F/T cycle. If a tube has 5+ dots, notify the instructor.
- Return all components to −20°C (DNA, H{sub}`2`O, RNAse inhibitor) and -80°C (PURExpress Solution A and B) promptly. Optiprep can stay at room temperature.

Check the osmolarity of each cytosol and your 900uM glucose outer solutions using a Vapor Pressure Osmometer before encapsulation:

- Press "open" on the osmometer and use tweezers to place a circular sample disc on the reading area.
- Pipette 10μL of the first cytosol condition (E1) onto the disc and press "close".
- Read and record the osmolarity.
- Repeat with each reaction (E2,E3) and the glucose outer solution.

E1 (mmol/kg): \_\_\_\_\_\_\_
E2 (mmol/kg): \_\_\_\_\_\_\_
E3 (mmol/kg): \_\_\_\_\_\_\_
Glucose solution (mmol/kg): \_\_\_\_\_\_\_

Encapsulate Cytosols into Liposomes:

- Set up a 1.5 mL tube rack on ice with two 1.5 mL microcentrifuge tubes (T and L) for each liposome encapsulation.
- Add 300 μL of the glucose outer solution to each of the tubes labelled T.
- Add 150 μL of the lipid-oil mixture on top of each cytosol reaction in tubes E.
- Emulsify the lipid-oil and cytosol mixture by running the tube along a row of empty slots on the 1.5 mL tube rack. Run it down 40--50 times until the solution forms a stable emulsion with a homogenous milky color.
- Important: While running the tubes on the tube rack, hold the cap firmly to prevent it from coming off during vigorous mixing.
- Slowly pipette the entire emulsion (from tube E) down the side of the corresponding T tube, so that the emulsion is layered on top of the glucose solution.
- Centrifuge all T tubes at 9000 g [8970 RPM for tabletop centrifuges (r=10 cm)] for 10 min at room temperature to pellet the liposomes.
- Extract the liposomes from each T tube:
  - Remove the oil layer and lipid debris from the top (supernatant) of each T tube by gently pipetting with a 1000 μL pipette set to 800 μL. Begin at the top of the mixture and aspirate from the solution surface as the liquid level descends in the tube. Dispose of supernatant in designated container or an empty microcentrifuge tube, which can then be disposed in designated waste.
  - Once the majority of supernatant is removed, extract liposomes by pipetting 50 μL of pellet and outer solution from tube T and transfer to the respective liposome tube L. Do not transfer the entire solution. It is important to avoid transferring the top of the solution which may contain a residual oil layer. Repeat for each T tube.
- Hold liposomes on ice until you are prepared to begin measurement.
- Pipette ~30μL of the liposomes in tube L into a well on a 384-well glass bottom plate. Set the micropipette to 32 μL and stop at the first stop when dispensing to prevent the introduction of bubbles into the sample.
- Wipe the bottom of the plate with a Kimwipe to rid the plate of any dust. Handle the plate by its sides with gloved hands to avoid dirtying the glass bottom. Place the plate in the microscope.

Data Quantification: Real-time 4-hour fluorescence (488nm and 638 nm), incubated at 37 °C. Time point micrographs taken every 10 minutes for 4 hours.

Clean Up: All used pipette tips and empty reaction tubes belong in the "used pipette tips" container on your lab bench. Ensure all reagents are on ice or stored properly before leaving your bench. Wash your hands thoroughly before leaving the lab.

::::

::::{tab-item} Nucleus PURE

**Materials:**

- pOpen-dGFP: [DNA]= \_\_\_\_\_\_\_
- Nuclease-free water
- SMix
- tRNA
- Pmix
- Ribosomes
- Murine RNase Inhibitor (40000 U/mL, 0.15 mL)
- OptiPrep Density Gradient Medium
- 2.5 μL micropipette
- 10 μL micropipette
- 20 μL micropipette
- 200 μL micropipette
- 1000 μL micropipette
- 1.5 mL Microcentrifuge Tubes (12x)
- Glucose solution (800mM and 900mM)
- Lipid-Oil Solution
- 384-Well clear-bottom plate\*

\*The 384-well plate will be shared among groups and kept on ice until students are ready to transfer their complete reactions. Notify your instructor when your solutions are complete.

**Safety:** Goggles and Nitrile Gloves should be worn while handling all reaction components. Dispose of tubes and micropipette tips in designated waste. Avoid looking into intense light sources when using microscopes.

**Protocol (Nucleus PURE Encapsulation):**

Assembling the reaction:

- Label 12 tubes, five of each of the following:
  - E — oil emulsion (E)
  - T — transfer (T)
  - L — liposomes (L)
- Calculate the amount of DNA to add so that final [DNA] in solution is equal to 6 ng/µL using C{sub}`1`V{sub}`1`=C{sub}`2`V{sub}`2`.
- Create PURExpress cytosol for encapsulation. Keep all reagents and reactions on ice throughout. Preparation on ice ensures that protein expression does not begin during assembly. Pipette the following reagents in the tube "E" in the order listed. Repeat for each "E" tube (3x).

DNA template used: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Stock Concentration: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

:::{table} Nucleus PURE Encapsulation Composition
| Component | Cytosol with CP/CK (µL) |
|-----------|-------------------------|
| SMix | 12 |
| tRNA | 4 |
| PMix | 4.8 |
| Ribosomes | 7.2 |
| RNAse Inhibitor | 2 |
| Optiprep | 1.33 |
| DNA: \_\_\_\_\_\_ | TBD |
| Nuclease-Free H{sub}`2`O | To 40 µL |
| Total Volume | 40 |
:::

- Pipette mix each reaction, then centrifuge each reaction at 5000g [6685 RPM for tabletop centrifuges (r=10 cm)] for 30 seconds to spin down bubbles in the reaction.
- After using each component, add a black dot to the tube lid with a lab marker. Each dot = one F/T cycle. If a tube has 5+ dots, notify the instructor.
- Return all components to −20°C (DNA, H{sub}`2`O, RNAse inhibitor) and -80°C (SMix, PMix, tRNA, Ribosomes) promptly. Optiprep can stay at room temperature.

Check the osmolarity of each cytosol and your 900uM glucose outer solutions using a Vapor Pressure Osmometer before encapsulation:

- Press "open" on the osmometer and use tweezers to place a circular sample disc on the reading area.
- Pipette 10μL of the first cytosol condition (E1) onto the disc and press "close".
- Read and record the osmolarity.
- Repeat with each reaction (E2,E3) and the glucose outer solution.

E1 (mmol/kg): \_\_\_\_\_\_\_
E2 (mmol/kg): \_\_\_\_\_\_\_
E3 (mmol/kg): \_\_\_\_\_\_\_
Glucose solution (mmol/kg): \_\_\_\_\_\_\_

Encapsulate Cytosols into Liposomes:

- Set up a 1.5 mL tube rack on ice with two 1.5 mL microcentrifuge tubes (T and L) for each liposome encapsulation.
- Add 300 μL of the glucose outer solution to each of the tubes labelled T.
- Add 150 μL of the lipid-oil mixture on top of each cytosol reaction in tubes E.
- Emulsify the lipid-oil and cytosol mixture by running the tube along a row of empty slots on the 1.5 mL tube rack. Run it down 40--50 times until the solution forms a stable emulsion with a homogenous milky color.
- Important: While running the tubes on the tube rack, hold the cap firmly to prevent it from coming off during vigorous mixing.
- Slowly pipette the entire emulsion (from tube E) down the side of the corresponding T tube, so that the emulsion is layered on top of the glucose solution.
- Centrifuge all T tubes at 9000 g [8970 RPM for tabletop centrifuges (r=10 cm)] for 10 min at room temperature to pellet the liposomes.
- Extract the liposomes from each T tube:
  - Remove the oil layer and lipid debris from the top (supernatant) of each T tube by gently pipetting with a 1000 μL pipette set to 800 μL. Begin at the top of the mixture and aspirate from the solution surface as the liquid level descends in the tube. Dispose of supernatant in designated container or an empty microcentrifuge tube, which can then be disposed in designated waste.
  - Once the majority of supernatant is removed, extract liposomes by pipetting 50 μL of pellet and outer solution from tube T and transfer to the respective liposome tube L. Do not transfer the entire solution. It is important to avoid transferring the top of the solution which may contain a residual oil layer. Repeat for each T tube.
- Hold liposomes on ice until you are prepared to begin measurement.
- Pipette ~30μL of the liposomes in tube L into a well on a 384-well glass bottom plate. Set the micropipette to 32 μL and stop at the first stop when dispensing to prevent the introduction of bubbles into the sample.
- Wipe the bottom of the plate with a Kimwipe to rid the plate of any dust. Handle the plate by its sides with gloved hands to avoid dirtying the glass bottom. Place the plate in the microscope.

Data Quantification: Real-time 4-hour fluorescence (488nm and 638 nm), incubated at 37 °C. Time point micrographs taken every 10 minutes for 4 hours.

Clean Up: All used pipette tips and empty reaction tubes belong in the "used pipette tips" container on your lab bench. Ensure all reagents are on ice or stored properly before leaving your bench. Wash your hands thoroughly before leaving the lab.

::::

:::::

# Resources

- NEB PURExpress In Vitro Protein Synthesis Kit (E6800): [neb.com/en-us/products/e6800-purexpress-invitro-protein-synthesis-kit](https://www.neb.com/en-us/products/e6800-purexpress-invitro-protein-synthesis-kit)
- Nucleus Documentation — Liposome Workshop: [docs.nucleus.engineering/guides/liposome-workshop/main](https://docs.nucleus.engineering/guides/liposome-workshop/main/)
- Nucleus Documentation — Assemble Base Cell: [docs.nucleus.engineering/docs/processes/assemble-base-cell/main](https://docs.nucleus.engineering/docs/processes/assemble-base-cell/main/)
- Nucleus Documentation — Base Cytosol Spec: [docs.nucleus.engineering/docs/modules/base-cytosol/spec](https://docs.nucleus.engineering/docs/modules/base-cytosol/spec/)
