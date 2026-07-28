# DevNotes Downloaded — Catalog & Summary

This directory is a bulk download of DevNotes from the devnotes.nucleus.engineering server. It has been cleaned of build artifacts, VCS history, and other non-content bloat (`_build/`, `.git/`, `__pycache__/`, `.venv/`, `node_modules/`, `.ipynb_checkpoints/`, `.DS_Store`, duplicate archives) — what remains is genuine devnote content, roughly 360MB across 1,568 files.

**23 genuine devnotes** were found (identified by their `curvenote.yml` file), plus **2 orphaned/duplicate artifacts** nested inside `bnext/aria/aria-d1/`'s scratch subtree (see Notes below).

The Myst Key is the `project.id` field in each devnote's `curvenote.yml`.

## Catalog

| Title | Author | Myst Key | Team | Topic | Notes |
|---|---|---|---|---|---|
| AI-driven Cell-Free Energy Development and Optimization | Anton Jackson-Smith, Scott Riggs | `019db9cf-6b15-79fa-b71f-550cf37149fa` | bnext (ARIA/IGOR) | IGOR AI-scientist project charter: optimizing PPK + glycolysis energy modules in PURE | |
| IGOR PPK Optimization: Round 2 | Scott Riggs, "IGOR" | `591140bb-e66b-415b-ae5c-03302aa68bbe` | bnext (ARIA/IGOR) | LabCraft-assembled PURE yield loss due to path-dependent, non-equilibrium assembly kinetics | Exact duplicate nested inside `aria-d1/data/.../or-outputs/` |
| IGOR PPK Optimization: Round 1 | Scott Riggs, "IGOR" | `51030dec-7ab4-475a-8312-9c73c9d24301` | bnext (ARIA/IGOR) | Mg2+/ATP/GTP stoichiometry multivariate optimization of PURE yield | |
| Meta DevNote: a DevNote about creating DevNotes | Sam Cell | `019ce92a-50d4-7e63-b697-912113b450b0` | bnext (ARIA/IGOR) | Template/placeholder devnote | Boilerplate, not a real result |
| Dev Note - Bio - b.next V2 | "Zitadel Admin", IGOR | `02e60f09-8187-425c-b674-15f3cd639555` | bnext (ARIA/IGOR) | PolyP as Mg2+ chelator enabling PPK-based energy regen in PURE | Placeholder author fields unfilled |
| AI Scientist: Base Module Report | IGOR, Anton Jackson-Smith, Scott Riggs | `019dcbd4-f87a-7e0d-97d7-6e58ef3403df` | bnext (ARIA/IGOR) | Rollup report of IGOR's iterative PURE base-system optimization (D1 deliverable) | Largest devnote (334 files, 76M); contains the 2 nested duplicate artifacts |
| ClpXP Control Module: Deployment in PURE with Nucleus Cytosol | Yen-Yu Hsu | `019e896a-6e0d-76d5-99ef-2df38c5ebd7f` | bnext | ClpXP protease-based programmable degradation module in liposomes/synthetic cells | Myst Key collides with SecYEG-YH below |
| ClpXP Control Module: Deployment in Nucleus Cytosol | Yen-Yu Hsu | `019f05c8-f7ea-74d8-ab37-a6e418627268` | bnext | ClpXP-mediated ssrA-tag degradation reconstituted in Nucleus Cytosol | |
| Characterizing the Limited Operational Lifetime of Cytosol Reactions | Surendra Yadav | `019ed70b-0af7-7dd0-aefe-688ebf933399` | bnext | PURE/Cytosol reaction lifetime limited by multi-component metabolic drain, not thermal decay | |
| DNA toolkit - Aptamer reporter constructs (all) | Charlie Newell | `nucleus-devnote-core-devnotes-DNA_toolkit_aptamer_reporters` | bnext | Broccoli/Mango aptamer reporters for simultaneous transcription+translation kinetics in PURE | Myst Key collides with Broccoli-only variant below |
| DNA toolkit - Aptamer reporter constructs (Broccoli only) | Charlie Newell | `nucleus-devnote-core-devnotes-DNA_toolkit_aptamer_reporters` | bnext | Broccoli/DFHBI-1T + mScarlet dual reporter subset | Same Myst Key as sibling above — flag for dedup |
| DNA toolkit - The T7 terminator collection | Charlie Newell | `cn-05272026-terminators` | bnext | Characterizing T7 terminator library termination efficiency in PURE | |
| What Data | Jay Bhasin, Sharon Newman | `019d6e3a-c618-77bc-853c-fe4694511f53` | bnext (platform) | Intro/kickoff data-and-analysis platform note (platemaps/standards) | Myst Key collides with why-platemap below |
| Intro to Kinetics Analysis of Plate Reader Experiments | Sharon Newman | `019db3ce-4971-7fd6-83c0-c1a15e780bbe` | bnext (platform) | CDK logistic-with-drift model for time-series kinetics analysis | |
| Using platemaps to analyze and share data | Jay Bhasin | `019d6e3a-c618-77bc-853c-fe4694511f53` | bnext (platform) | Platemap format for joining experimental metadata to well-level measurement data | Same Myst Key as "What Data" above |
| What we talk about when we talk about data | Sam Cell | `sharon-why-standard` | bnext (platform) | Fluorescence standards (MESF/MEFL) for cross-lab comparability with GFP reporters | |
| SecYEG-Based Membrane Translation Module in Synthetic Cells | Yen-Yu Hsu | `019e896a-6e0d-76d5-99ef-2df38c5ebd7f` | bnext | SecYEG translocon reconstitution for membrane protein integration in liposomes | Myst Key collides with ClpXP-Cells-YH above |
| Membrane Translation Module Development Plan | Yen-Yu Hsu | `019c400f-9c04-7293-9a2e-613a75ad5d1d` | bnext | Dev plan (pre-registration) for SecYEG membrane module | Precursor to SecYEG-YH |
| Theophylline-LacZ sensor validation in Cytosol | Sam Cell | `b6272c31-dae6-4c60-bf48-a86466349d86` | devcells-chicago-node | Template/workshop devnote | Content incomplete (TODO placeholders) |
| Module Development Plan: DevCell-based pH sensor | Samuel J. Chen, Sung-Won Hwang (U. Michigan) | `sjcliulab` | devcells-chicago-node | pH-responsive DevCell sensor dev plan (colorimetric acidic-pH detection) | |
| Toehold switch-enabled translation regulation verified in Nucleus Cytosol | Chen, Hwang, Allen Liu (U. Michigan) | `sjcliulab02` | devcells-chicago-node | Preliminary toehold-switch/pHtdGFP validation test in Nucleus Cytosol | |
| PLA1 DevNote | Sung-Won Hwang | `019ed7c0-0591-70ce-bcf5-352d08e946f6` | devcells-chicago-node | Placeholder only — unstarted | |
| Theophylline-LacZ sensor validation in Nucleus Cytosol | Maram Naji (Northwestern) | `019d20e4-4787-7f35-9c77-f2f53f43d107` | devcells-chicago-node | Theophylline riboswitch → LacZ biosensor validated in Nucleus Cytosol | |
| TetO-Catecholase sensor validation in Nucleus Cytosol | Maram Naji (Northwestern) | `019db237-0d03-7ae1-8c40-e57e2ce1bea1` | devcells-chicago-node | aTc/TetR-controlled catecholase biosensor validated in Nucleus Cytosol | |
| CRNsemble | Arash Elahi (U. Tennessee, Knoxville) | `019deb45-d0ac-78f0-86dd-d7d351f201c2` | metapure | Title says CRNsemble but main.md content appears to be BCECF pH-sensor material | Content/title mismatch — flag for follow-up |
| BCECF pH Sensor | David Garenne (U. Minnesota) | `019d661b-b50a-7cbd-bac5-1359ad376c62` | metapure | BCECF ratiometric pH indicator adapted for continuous 24h kinetic pH tracking in myTXTL | |
| Tunable protein expression strength with toehold exchange riboregulators | Sam Schaffter (NIST) | `d26b0f43-315f-4706-ac4b-0adeeefd9057` | nucleus-eng-hub-access | Toehold-mediated strand exchange (TMSE) riboregulators tuning translation output | Abstract placeholder still unfilled |
| Meta DevNote: a DevNote about creating DevNotes | Sam Cell | `019e416c-f0b1-74a9-89ae-c8137ddabf55` | nucleus-eng-hub-access | Template/placeholder content despite "ufl-onepot" directory name | Template stub, not real UFL content |

## Notes / data-quality flags

1. **Nested duplicate/orphaned artifacts** — two extra `curvenote.yml` files live buried inside `bnext/aria/aria-d1/data/20260320-iteration-2/`:
   - `.../or/or-outputs/Optimize PURE System Yield via LabCraft - DevNote - 2026-04-22/` — exact duplicate of the top-level "IGOR PPK Optimization: Round 2" devnote (same Myst Key, same content).
   - `.../workspace/scr/old/PURE System Yield Optimization with Labcraft - DevNote - 2026-04-21/` (Myst Key `301bb456-4bbf-43c6-81b9-323985014d1a`) — an orphaned intermediate draft with no top-level counterpart, superseded by later rounds.
   
   Both are scratch artifacts from the automated IGOR research loop, harmless to leave in place inside the kept `aria-d1` tree.

2. **Myst Key collisions** (likely copy-paste-from-template without renaming the ID) — three pairs share an ID despite being distinct devnotes:
   - `ClpXP-Cells-YH` ↔ `SecYEG-YH`
   - `cytosol-data` ("What Data") ↔ `why-platemap` ("Using platemaps...")
   - DNA-toolkit aptamer reporters "all" ↔ "Broccoli only" variant

3. **Placeholder/unfinished devnotes** — several are template stubs rather than finished results: `aria-d1-results/test-devnote`, `devcells-chicago-node/devnote-template`, `Liu Lab-pH sensors/pla1`, `nucleus-eng-hub-access/.../ufl-onepot`, and `.../toehold-exchange` (abstract left as `[Abstract]`).

4. **Content/title mismatch** — `metapure/CRN-Ensemble/main.md` appears to contain leftover BCECF pH-sensor content rather than actual CRNsemble material; worth verifying with the author.

5. Largest devnote by far is `bnext/aria/aria-d1/` (334 files, 76MB) — the IGOR AI-scientist rollup report.

## Comparison against the migration TODO list

Cross-referencing this catalog against `devnote-migration-status.md` (the tracker for devnotes still marked TODO in the main repo migration): **7 of 20 outstanding TODOs are confirmed present** in this download (exact Myst Key match), **2 more are likely the same devnote** under a different/inconsistent Myst Key, and **11 are not present at all**.

### Confirmed present (exact Myst Key match)

| Title | Myst Key | Found at |
|---|---|---|
| ClpXP Control Module: Deployment in Nucleus Cytosol | `019f05c8-f7ea-74d8-ab37-a6e418627268` | `bnext/ClpXP-YH/` |
| Characterizing the Limited Operational Lifetime of Cytosol Reactions | `019ed70b-0af7-7dd0-aefe-688ebf933399` | `bnext/cytosol-lifetime/` |
| SecYEG-Based Membrane Translation Module in Synthetic Cells | `019e896a-6e0d-76d5-99ef-2df38c5ebd7f` | `bnext/SecYEG-YH/` |
| Using platemaps to analyze and share data | `019d6e3a-c618-77bc-853c-fe4694511f53` | `bnext/platform/devnotes/why-platemap/` |
| Intro to Kinetics Analysis of Plate Reader Experiments | `019db3ce-4971-7fd6-83c0-c1a15e780bbe` | `bnext/platform/devnotes/kinetics-intro/` |
| DevCells: Kickoff Workshop | `b6272c31-dae6-4c60-bf48-a86466349d86` | `devcells-chicago-node/devnote-template/` |
| DNA toolkit - The T7 terminator collection | `cn-05272026-terminators` | `bnext/DNA-toolkit-terminators/...` |

### Likely present, but Myst Key doesn't match

| TODO row | TODO's key | Downloaded match | Downloaded key | Why likely the same |
|---|---|---|---|---|
| Tunable protein expression strength with toehold exchange riboregulators | `7b6aaa00-7351-4a7e-ba45-ade3f7332335` | `nucleus-eng-hub-access/devnotes/toehold-exchange/` | `d26b0f43-315f-4706-ac4b-0adeeefd9057` | Identical title, same first author (Sam Schaffter) — different UUID entirely |
| ClpXP Control Module: Deployment in PURE Cells | `nucleus-devnote-core-clpxp_module_cells-01` | `bnext/ClpXP-Cells-YH/` ("...Deployment in PURE with Nucleus Cytosol") | `019e896a-6e0d-76d5-99ef-2df38c5ebd7f` | Near-identical title/topic, same author (Yen-Yu Hsu) — key convention mismatch |

### Not present in this download

6 of these are internal Core devnotes (bnext authors) simply not included in this export batch; the other 5 are external contributions (Workshops/Courses + Community) that likely live outside the bnext internal store this download was pulled from.

| Title | Author(s) | Myst Key | Collection | Likely reason missing |
|---|---|---|---|---|
| Nucleus OnePot PURE | Surendra Yadav | `onepot-sy` | Core | Internal bnext note, just not in this export batch |
| ClpXP Control Module: Deployment in PURE | Yen-Yu Hsu | `nucleus-devnote-core-clpxp_module_cytosol-01` | Core | Internal — possibly duplicate/alt-ID of the already-downloaded ClpXP-YH note |
| DNA toolkit - The T7 promoter collection | Charlie Newell, Astrid Joergensen | `nucleus-devnote-core-dna-toolkit-promoter` | Core | Internal bnext note, not in this export batch (sibling terminator/aptamer notes *were* included) |
| Nucleus OnePot PURE Replication | Anton Molina, Anton Jackson-Smith | `nucleus-devnote-core-07_bnext-onepot-pure-replication` | Core | Internal bnext note, not in this export batch |
| The Developer Cell Control Module: Protein Degradation by ClpXP | Yen-Yu Hsu | `nucleus-devnote-core-06_clpxp_module_01` | Core | Internal — another ClpXP variant not in this export batch |
| Developer Cell: Project Introduction | Anton Jackson-Smith, Akshay Maheshwari | `nucleus-devnote-core-05_devcell_01` | Core | Internal bnext note, not in this export batch |
| Liposome encapsulation: A tractable and reproducible approach | Chris Falcon, Katie Drew | `9e302e31-3dbb-494a-b8e3-5fc6d91ea941` | Workshops and Courses | External collaborators — likely lives outside the bnext internal store |
| Synthetic Cells Course Lab Manual: Cell-free Gene Expression and Liposome Encapsulation | Javin P Oza | `118a7ada-92d1-448f-adc2-f19c2da16b16` | Workshops and Courses | External course material, likely separate repo |
| Energy Metabolism Working Group at Build-a-Cell #15 | Energy Metabolism Working Group | `bac-working-group` | Community | External community/conference content |
| London Exchange Meeting: Liposome Protocol Survey | London Exchange Meeting Participants | `019dcea0-91e3-78da-be6d-6450c2ff8308` | Community | External community/event content |
| Cx43 Cell | Ahmed Z. Sihorwala | `nucleus-devnote-core-01_contrib_cx43_cell` | Community | External contributor, "contrib" naming suggests a separate submission path |
