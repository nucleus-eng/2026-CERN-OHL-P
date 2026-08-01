---
# Ensure that this title is the same as the one in `myst.yml`
title: An Unexpected Enzyme in PURE Why Folinic Acid Needs Extra Help
abstract: |
  The Connexin 43 Cell is a synthetic cell system that expresses and functionally integrates the mammalian channel protein connexin 43 (Cx43) into artificial cell membranes. This system encapsulates plasmid DNA encoding Cx43-GFP fusion protein along with the PURE cell-free expression system within lipid vesicles. Upon expression, Cx43 spontaneously inserts into the vesicle membrane and self-associates to form hexameric nanopores called connexons. The functionality of connexon formation can be demonstrated through controlled release of an encapsulated fluorescent dye. The ability of connexons to form gap junctions between neighboring cells could enable the development of tissues composed Cx43-derived cells.
---

# Overview

The Connexin 43 Cell expresses the mammalian channel protein, connexin 43 (Cx43). Cx43 is a four-pass transmembrane protein that self-associates to form hexameric nanopores called Cx43 connexons ({ref}`fig:connexin-scheme`). Members of the connexin family of proteins are designated with the abbreviation Cx followed by their predicted molecular mass in kilodaltons [Totland *et al.*, 2023](https://doi.org/10.1016/j.bbadis.2023.166812); hence Cx43 has a molecular weight of 43 kDa. These nanopores act as conduits that facilitate exchange of different molecules across the Cell’s membrane. Under certain conditions, connexons may form gap junctions between neighboring cells, enabling selective material exchange between neighbors through the junction. The Connexin 43 Cell is largely based on a paper by Ahmed Z. Sihorwala, Jeanne C. Stachowiak, and Brian Belardi: [Light-activated assembly of connexons in synthetic cells](https://pubs.acs.org/doi/abs/10.1021/jacs.2c12491).

More specifically, the Connexin 43 Cell encapsulates a plasmid DNA encoding for Cx43-GFP (green fluorescent protein) along with the PURE cell-free expression system. Following PURE expression, Cx43 is able to spontaneously insert into the Cell membrane, and subsequently form connexons. Successful integration of connexons in the Cell membrane leads to release of fluorescent small molecules, thus connecting the Cell lumen to its external environment.

:::{figure} ./figures/connexin-scheme.png
:label: fig:connexin-scheme
:width: 50%

Depiction of connexin and its relationship to a connexon: (*left*)Connexins are tetra-membrane-spanning proteins whose N- and C-termini are located in
the cytoplasm; (*right*) six connexins oligomerize to form a connexon. Figure by [Totland *et al.*](https://doi.org/10.1016/j.bbadis.2023.166812) used under [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/) / cropped from original.
:::

# Design

The Connexin 43 Cell expresses Cx43-GFP under the control of a T7 promoter. Cx43 expression leads to the formation of membrane nanopores, called connexons. These connexons enable release of a fluorescent small molecule, Alexa Fluor 647, from the Cell to its external environment.

# Dependencies

**Modules**

- This component does not function as a stand alone component in PURE, it requires the membrane environment

**DNA components**

- `pT7-Cx43-eGFP` - express Cx43 eGFP fusion protein in the pRSET plasmid

**Key Materials**

| **Name** | **Product** | **Manufacturer** | **Part #** | **Price** | **Link** |
| --- | --- | --- | --- | --- | --- |
| Alexa Fluor 647 | Alex Fluor 647 NHS Ester | Thermo Scientific | A20006 | $429.00 | [[link](https://www.thermofisher.com/order/catalog/product/A20006)] |
| Atto 390 | DOPE-Atto390 | ATTO TEC | AD 390-161 | $445.00 | [[link](https://www.atto-tec.com/DOPE.html)] |

# Protocol

**Create Lipid-Oil Mixture (500uL):**

- Add 400 uL Silicone Oil (SO) and 70 uL Mineral Oil (MO) to large glass vial, vortex to mix.
- Add 0.2 mg POPC and 0.286 ug Atto390-DOPE to small glass vial. Evaporate with nitrogen to create lipid film. Use glass syringes to handle lipids, which are aliquoted in chloroform. These need to be handled and rinsed carefully. Lipids are stored in the -80 fridge.
- Resuspend lipid film in 30 uL decane, vortex
- Add 30uL of lipid-decane solution to SO / MO mixture, vortex
- In an Eppendorf tube, add 90 uL of HEPES buffered saline (5mM HEPES, 30mM NaCl) to the bottom. Gently add 20 uL of lipid-oil solution over the aqueous solution and let the interface stabilize for 30 min.

**Inner aqueous solution:**

- On ice, prepare PURExpress reaction:

| **Component** | **Volume [uL]** |
| --- | --- |
| NEB PURExpress Solution A | 5 |
| NEB PURExpress Solution B | 3.75 |
| Cx43-GFP in pRSET Plasmid (total amount 70 ng) | 0.25 |
| Opti-PREP (for final dilution = 10% OptiPREP) | 1.25 |
| Alexa Fluor 647 (start with 100uM AF647) | 1.25 |
| “Top it off with” 25mM HEPES; 150mM NaCl | 1.25 |
| **Total** | **12.75** |

- The total volume is 12.5 uL, but only 5 uL is needed for encapsulation.

**Create Emulsion:**

- In a large glass vial, mix 80 uL of lipid-oil mixture with 5 uL inner aqueous solution. Vortex to emulsify.

**Create Vesicle:**

- Gently add the emulsion to the Eppendorf tube.
- Centrifuge at 2400xg for 10 min at 4C.
- Puncture side of tube near the bottom using 26G needle and eject vesicle solution into fresh tube. Ejected solution contains vesicles.
- Incubate the vesicles at 37C for 2 hours. Cover the vesicles with foil.

# Performance assays

**Insertion assay.** Observe liposomes under microscope. Ref paper uses 60x confocal and obtained time series by taking different preps at 10, 30, 60, 120, and 180 min; alternatively can use a single sample with on-stage incubation. Note: expression plateaued at 60 min. 

**Leakage assay.** Observe liposomes under microscope. Ref paper uses 60x confocal and obtained time series by taking different preps at 10, 30, 60, 120, and 180 min; alternatively can use a single sample with on-stage incubation. Report percentage of vesicles with dye leakage. Expect 20% leakage in Negative Control and 60% leakage in Sample. Most leakage occurred within 30 minutes. Can also quantify leakage by measuring supernatant of pelleted vesicles, a 2-fold difference was observed. 

Note: that leakage can be inhibited by presence of 2 mM Ca++ in outer solution.

# Performance data

performance data is available in the original [publication](https://pubs.acs.org/doi/abs/10.1021/jacs.2c12491).

# Credits

- Brian Belardi (UT Austin)
- Jeanne C. Stachowiak (UT Austin)

