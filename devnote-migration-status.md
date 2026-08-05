# DevNote migration status

This file tracks every DevNote: where it lives, whether it is published, and
what still needs to move.

To migrate a DevNote, use the `migrate-devnote` skill in
[`.claude/skills/migrate-devnote/`](./.claude/skills/migrate-devnote/). It gives
the full procedure and a catalogue of known snags. This file records **state**;
the skill records **method**.

## Summary as of 2026-08-05

| Count | Meaning |
|---|---|
| **49** | DevNotes published on the venue |
| **22** | DevNotes in this repo |
| **19** | in this repo **and** published |
| **3** | in this repo and submitted, but not yet published |
| **30** | published, but **not yet in this repo** — the remaining migration work |

Two corrections to earlier versions of this file, both found on 2026-08-05:

1. **This file used to be incomplete.** It listed 28 DevNotes. The venue
   publishes 49. The earlier count missed the `Node Chicago`, `Node London`,
   `AI Scientist` and `Workshops and Courses` collections entirely. Always
   enumerate from the venue, never from this file.
2. **"Needs author outreach" was wrong.** This file used to say two DevNotes
   probably needed us to contact their authors. Both are published, and both
   have a downloadable MECA archive. Recover them like anything else.

## Before you migrate anything

This repo is only for DevNotes released fully in the open, under CC-BY or a
CERN-OHL-P equivalent. **A human must decide whether a DevNote may be included.**
Never automate that decision. Many of the 30 remaining DevNotes come from
external contributors at the Chicago and London nodes, so this matters.

## How to regenerate this table

Do not edit the counts by hand. Fetch every collection page, then compare against
the repo. Match on the **Myst key**, never on the URL slug — the two often differ.

```bash
for c in index collections-core collections-contrib collections-ai-scientist \
         collections-workshops-and-courses collections-devcell-node-chicago \
         collections-devcell-node-london; do
  curl -s -A "Mozilla/5.0" "https://devnotes.nucleus.engineering/$c.json" -o "c-$c.json"
done
```

Then extract each article's `key`, `slug` and `title`, and compare with
`project.id` from every `devnotes/*/curvenote.yml`. Parse the YAML properly.
Several files carry other `id:` keys under `exports:` and `authors:` that a plain
grep matches first. The skill's `references/recover.md` has the full script.

## Every DevNote

A DevNote is **live** once the venue publishes it. A DevNote that is in the
repo but not yet live is waiting on a curator to approve its submission.
"Reviewed" means a human read `main.md` from start to end.

| Title | Author(s) | Collection | Myst key | Status |
|---|---|---|---|---|
| Characterizing the Limited Operational Lifetime of Cytosol Reactions | Surendra Yadav | Core | `019ed70b-0af7-7dd0-aefe-688ebf933399` | **Not in the repo yet.** Published, so recoverable from its MECA archive. |
| ClpXP Control Module: Deployment in Nucleus Cytosol | Yen-Yu Hsu | Core | `019f05c8-f7ea-74d8-ab37-a6e418627268` | **Not in the repo yet.** Published, so recoverable from its MECA archive. |
| ClpXP Control Module: Deployment in PURE | Yen-Yu Hsu | Core | `nucleus-devnote-core-clpxp_module_cytosol-01` | Live, from `module-Clpxp-Cytosol`. All 6 notebooks pass. Reviewed. [Build report](https://scms.curvenote.com/build/019fcdbd-8698-7638-9941-ae1285b2a831) |
| ClpXP Control Module: Deployment in PURE Cells | Yen-Yu Hsu | Core | `nucleus-devnote-core-clpxp_module_cells-01` | Live, from `module-Clpxp-Cells`. All 5 notebooks pass. **Still needs a content review.** [Build report](https://scms.curvenote.com/build/019fd304-b1cc-729d-8570-fd9b5c6b8cf4) |
| Cx43 Cell: DNA Validation | Yen-Yu Hsu | Core | `nucleus-devnote-core-cx43_01` | Live, from `09-cx43_cell`. Both notebooks pass. Reviewed. [Build report](https://scms.curvenote.com/build/019fcdbe-5ef0-7026-9610-99264e36e02a) |
| DNA toolkit - The T7 promoter collection | Charlie Newell, Astrid Joergensen | Core | `nucleus-devnote-core-dna-toolkit-promoter` | Live, from `DNA-toolkit-T7-promoters`. Both notebooks pass. Reviewed. [Build report](https://scms.curvenote.com/build/019fcdbe-6e19-7f44-a94f-2b18457e0f19) |
| Developer Cell: Project Introduction | Anton Jackson-Smith, Akshay Maheshwari | Core | `nucleus-devnote-core-05_devcell_01` | Live, from `devnote-developer_cell`. No notebooks to run. Reviewed. [Build report](https://scms.curvenote.com/build/019fcdc0-dfe4-7002-828e-29b43c285245) |
| Integrating PPK Module in PURE Cells | Yen-Yu Hsu | Core | `nucleus-devnote-core-08_ppk-module-in-pure-cell` | Live, from `08_ppk_cell`. Its notebook passes. Reviewed. [Build report](https://scms.curvenote.com/build/019fcdbd-9fa1-70f6-8b2e-435401361614) |
| Intro to Kinetics Analysis of Plate Reader Experiments | Sharon Newman | Core | `019db3ce-4971-7fd6-83c0-c1a15e780bbe` | Live, from `2026-newman-kinetics-intro`. Its notebook passes. **Still needs a content review.** [Build report](https://scms.curvenote.com/build/019fd305-03a4-71fa-9e74-686b8f283f23) |
| MTHFS - an Unexpected Enzyme in PURE | Yemo Ku | Core | `nucleus-devnote-core-03_mthfs` | Live, from `03_mthfs`. Its notebook passes. Reviewed. [Build report](https://scms.curvenote.com/build/019fcdbd-7ece-7503-9897-c802441245ce) |
| Nucleus Base Cell Testing | Surendra Yadav | Core | `nucleus-devnote-core-Base_Cell` | Live, from `11-Base_Cell`. No notebooks to run. Reviewed. [Build report](https://scms.curvenote.com/build/019fcdbd-8c20-7b08-bea8-967b2ea23099) |
| Nucleus OnePot PURE | Surendra Yadav | Core | `onepot-sy` | Live, from `onepot-sy`. All 3 notebooks pass. Reviewed. [Build report](https://scms.curvenote.com/build/019fcdbd-9f01-7488-839f-1c0979c0a693) |
| Nucleus OnePot PURE Replication | Anton Molina, Anton Jackson-Smith | Core | `nucleus-devnote-core-07_bnext-onepot-pure-replication` | Live, from `devnote-nucleus_onepot`. Its notebook passes. Reviewed. [Build report](https://scms.curvenote.com/build/019fcdbd-e4b6-7227-a6c7-c3ce474e1284) |
| PPK Module testing in PURE | Surendra Yadav | Core | `nucleus-devnote-core-04_ppk` | Live, from `04_ppk`. All 5 notebooks pass. Reviewed. [Build report](https://scms.curvenote.com/build/019fcdbd-84b4-7d12-9a9a-d4a101f3ff0b) |
| SecYEG-Based Membrane Translation Module in Synthetic Cells | Yen-Yu Hsu | Core | `019e896a-6e0d-76d5-99ef-2df38c5ebd7f` | **Not in the repo yet.** Published, so recoverable from its MECA archive. |
| The Developer Cell Control Module: Protein Degradation by ClpXP | Yen-Yu Hsu | Core | `nucleus-devnote-core-06_clpxp_module_01` | Live, from `module-Clpxp`. No notebooks to run. Reviewed. [Build report](https://scms.curvenote.com/build/019fcdc0-9407-7fae-986e-2fefa44eb448) |
| Using platemaps to analyze and share data | Jay Bhasin | Core | `019d6e3a-c618-77bc-853c-fe4694511f53` | **Not in the repo yet.** Published, so recoverable from its MECA archive. |
| BCECF pH Sensor | David Garenne | Community | `nucleus-devnote-core-2026-garenne-ph-sensor` | Live, from `2026-garenne-pH-sensor`. Its notebook passes. Reviewed. Submitted in PR #16. |
| DNA toolkit - The T7 terminator collection | Charlie Newell | Community | `cn-05272026-terminators` | **Not in the repo yet.** Published, so recoverable from its MECA archive. |
| Energy Metabolism Working Group at Build-a-Cell #15 | Energy Metabolism Working Group | Community | `bac-working-group` | Live, from `bac-working-group`. No notebooks to run. Reviewed. [Build report](https://scms.curvenote.com/build/019fcdbd-d5e0-7602-bfb7-f1c75b3b30e1) |
| London Exchange Meeting: Liposome Protocol Survey | London Exchange Meeting Participants | Community | `019dcea0-91e3-78da-be6d-6450c2ff8308` | Live, from `lipid-prep`. No notebooks to run. Reviewed. [Build report](https://scms.curvenote.com/build/019fcdbd-7f13-7cc3-b358-c42e0c6c3bcd) |
| Tunable protein expression strength with toehold exchange riboregulators | Samuel Schaffter, Fernanda Piorino, Eugenia Romantseva | Community | `7b6aaa00-7351-4a7e-ba45-ade3f7332335` | **Not in the repo yet.** Published, so recoverable from its MECA archive. |
| AI Scientist: Base Module Report | IGOR, b.next, FindWhatMatters | AI Scientist | `019dcbd4-f87a-7e0d-97d7-6e58ef3403df` | **Not in the repo yet.** Published, so recoverable from its MECA archive. |
| Batch Bayesian Optimization | Joseph Lozier | AI Scientist | `019f9b60-cc79-7008-9c25-4a46b53b8604` | Live, from `fwm-batch-bo`. No notebooks to run. Reviewed. [Build report](https://scms.curvenote.com/build/019fcdbe-1b37-7658-8b35-e8be01ca926f) |
| Defining AI Scientific Workflows: Using IGOR for Optimization of PURE | b.next, Find What Matters | AI Scientist | `019f6db2-e060-710d-8984-6bcd5747d775` | Live, from `fwm-aria-d2`. No notebooks to run. Reviewed. [Build report](https://scms.curvenote.com/build/019fcdbe-363a-77c5-936a-17af2178ef46) |
| IGOR PPK Optimization: Round 1 | Scott Riggs, IGOR | AI Scientist | `51030dec-7ab4-475a-8312-9c73c9d24301` | **Not in the repo yet.** Published, so recoverable from its MECA archive. |
| IGOR PPK Optimization: Round 2 | Scott Riggs, IGOR | AI Scientist | `591140bb-e66b-415b-ae5c-03302aa68bbe` | **Not in the repo yet.** Published, so recoverable from its MECA archive. |
| DevCells: Kickoff Workshop | DevCells Kickoff Workshop | Workshops and Courses | `b6272c31-dae6-4c60-bf48-a86466349d86` | **Not in the repo yet.** Published, so recoverable from its MECA archive. |
| Liposome encapsulation: A tractable and reproducible approach | Chris Falcon, Katie Drew | Workshops and Courses | `9e302e31-3dbb-494a-b8e3-5fc6d91ea941` | **Not in the repo yet.** Published, so recoverable from its MECA archive. |
| Nucleus OnePot PURE workshop | OnePot Workshop | Workshops and Courses | `nucleus-devnote-core-09_pure-workshop` | Live, from `05_pure_workshop`. All 5 notebooks pass. Reviewed. [Build report](https://scms.curvenote.com/build/019fcdbd-8559-7af4-b014-96363dd453b1) |
| Synthetic Cells Course Lab Manual: Cell-free Gene Expression and Liposome Encapsulation | Javin P Oza | Workshops and Courses | `118a7ada-92d1-448f-adc2-f19c2da16b16` | **Not in the repo yet.** Published, so recoverable from its MECA archive. |
| Biochromatic Materials | Maddie Briggs, Maram Naji, Mary Kelly, Matthew Lucia, Natalie Fisher, Ojaswita Pant, Samuel Chen, Allen Liu, Cecile Chazot, Danielle Tullman-Ercek, Julius Lucks, Neha Kamat, Ryan Truby | Node Chicago | `dd21c8ff-f44c-415c-83ee-8fc9ab9badc7` | **Not in the repo yet.** Published, so recoverable from its MECA archive. |
| Colorimetric Sensing Module Development Plan | Cécile A. C. Chazot, Natalie C. Fisher, Simona Fine | Node Chicago | `NCF-planningDevNote-01` | **Not in the repo yet.** Published, so recoverable from its MECA archive. |
| Double emulsion optimization: inner solution, lipid concentration, and composition | Mary Kelly | Node Chicago | `019d643c-63e8-74f3-a5f6-ae8d29175383` | **Not in the repo yet.** Published, so recoverable from its MECA archive. |
| Environmentally Responsive Materials via Integration of DevCells | Madison Briggs | Node Chicago | `mrb_kamatlab` | **Not in the repo yet.** Published, so recoverable from its MECA archive. |
| In Vitro Reporter Validation | Matthew Lucia | Node Chicago | `mjl-devnote-kickoff-workshop` | **Not in the repo yet.** Published, so recoverable from its MECA archive. |
| Matrix Design for Stable Liposomes and Efficient Cell-Free Protein Synthesis | Mary Kelly | Node Chicago | `PlanningDevNoteMaryKelly` | **Not in the repo yet.** Published, so recoverable from its MECA archive. |
| Module Development Plan: DevCell-based pH sensor | Samuel J. Chen, Sung-Won Hwang | Node Chicago | `sjcliulab` | **Not in the repo yet.** Published, so recoverable from its MECA archive. |
| Photopatterned Hydrogels with DevCells | Ojaswita Pant | Node Chicago | `ojaswitapant` | **Not in the repo yet.** Published, so recoverable from its MECA archive. |
| TetO-Catecholase sensor validation in Nucleus Cytosol | Maram Naji | Node Chicago | `019db237-0d03-7ae1-8c40-e57e2ce1bea1` | **Not in the repo yet.** Published, so recoverable from its MECA archive. |
| Theophylline-LacZ sensor validation in Nucleus Cytosol | Maram Naji | Node Chicago | `019d20e4-4787-7f35-9c77-f2f53f43d107` | **Not in the repo yet.** Published, so recoverable from its MECA archive. |
| Toehold switch-enabled translation regulation verified in Nucleus Cytosol | Samuel J. Chen, Sung-Won Hwang, Allen Liu | Node Chicago | `sjcliulab01` | **Not in the repo yet.** Published, so recoverable from its MECA archive. |
| Validation of colorimetric reporter sensors in Nucleus Cytosol | Maram Naji \| Lucks Lab | Node Chicago | `MN_LucksLab` | **Not in the repo yet.** Published, so recoverable from its MECA archive. |
| Bioprinting Synthetic Cells Within a Hydrogel Matrix | Niall McIntyre, Ravinash Krishna Kumar | Node London | `nm191611111` | **Not in the repo yet.** Published, so recoverable from its MECA archive. |
| Diffusion Kinetics | Jonah McDonald, James Hindley | Node London | `JMcDDiffusionKinetics-01` | **Not in the repo yet.** Published, so recoverable from its MECA archive. |
| Hydrogel-Embedded GUV Developer Cells | Ion Ioannou, Ignacio Gispert, James Hindley, Ocar Ces | Node London | `II9a7f1e82-58ea-42a8-896c-7312b3538ef6` | **Not in the repo yet.** Published, so recoverable from its MECA archive. |
| LacZ/XylE colour change module | Charlie Newell, Michael Booth | Node London | `CN_London_planning_DevNote` | **Not in the repo yet.** Published, so recoverable from its MECA archive. |
| Quorum Sensing Polymersome | Julia Purrinos De Oliveira, Claudia Contini | Node London | `62abfe00-110e-41e1-8121-4572a093eb17` | **Not in the repo yet.** Published, so recoverable from its MECA archive. |
| The colourimetric bacterial contamination sensing device. | Charlie Newell, Ion Ioannou, Jonah McDonald, Julia Purrinos De Oliveira, Manuel Bibrowski, Niall McIntyre, Ignascio Gispert, Claudia Contini, James Hindley, Michael Booth, Oscar Ces, Ravinash Krishna Kumar, Yuval Elani | Node London | `bd8b42b4-8a91-40c8-a636-3778d1c9a072` | **Not in the repo yet.** Published, so recoverable from its MECA archive. |
| IV-HSL Emitter Cell | — | — | `nucleus-devnote-core-02_emitter_cell` | In `02_emitter_cell`, waiting on the curator. No notebooks to run. Reviewed. [Build report](https://scms.curvenote.com/build/019fcdbe-5745-7f49-a3f6-68ef77450817) |
| First Nucleus Cytosol Testing | — | — | `nucleus-devnote-core-NucelusPURE_deGFP` | In `10-nucleus_cytosol_v05`, waiting on the curator. Both notebooks pass. Reviewed. [Build report](https://scms.curvenote.com/build/019fcdbd-c96c-7e3b-815d-b4c130a2f023) |
| Cx43 Cell | — | — | `nucleus-devnote-core-01_contrib_cx43_cell` | In `cx43`, waiting on the curator. No notebooks to run. Reviewed. [Build report](https://scms.curvenote.com/build/019fcdbd-a991-7f87-9dce-bdd7f07c9395) |

Two notes on the rows above:

- `bac-working-group` has an open problem. Its only author, "Energy Metabolism
  Working Group", has no `email` in `curvenote.yml`, so `curvenote check` fails
  every time. Do not guess an address. The DevNote's owner must supply one.
- `bac-working-group` and `onepot-sy` each had an older real submission from
  early testing of the CLI. The 2026-08-04 submission replaced both.

The first 19 submissions came from PR #13. On 2026-08-04 we ran
`CONCURRENCY=19 ./manual-submit-all.sh --final`. 17 of 19 succeeded on the first
pass. Two (`module-Clpxp`, `devnote-developer_cell`) hit a transient
`api.curvenote.com` login timeout under load, and we retried them one at a time.

Run `./manual-submit-all.sh` from the repo root to re-submit **drafts** for every
devnote and get fresh preview URLs. The script finds devnotes itself, so it stays
correct as devnotes are added. Use it for preview only. It does not mark anything
as submitted, because drafts are not submissions.

---

# Session history

What follows is the record of past migration sessions. Keep it. Most of the
snags below cost hours to diagnose, and several recurred.

## First notebook sweep (2026-08-01)

We ran every `toc`-listed notebook with `nbclient`, in one shared conda
environment with `nucleus-cdk==0.5.0rc2`. That version matches the pin in every
notebook's install cell. `environment.yml` is byte-identical across all 18
devnotes that have one; `02_emitter_cell` has none.

**Result: 19 pass, 9 fail, across 28 notebooks.** All 9 were later fixed. The
current state is 28 pass, 0 fail.

Six devnotes list no notebooks in their `toc`. They are marked "n/a" above. That
is a gap in coverage, not a pass.

Three of the 9 failures were real bugs in `nucleus-cdk`. We could not fix them
from the notebook. We filed them against the true source repo, `bnext-bio/bnext`
(`bnext-bio/nucleus` is a stale mirror):

| Devnote | Notebook | Error | Issue |
|---|---|---|---|
| 03_mthfs | `20250220-analysis.ipynb` | `pr.plot_kinetics`: `ax.axvline` compares a `pandas.Timedelta` against a float axis limit | [bnext#66](https://github.com/bnext-bio/bnext/issues/66) |
| 08_ppk_cell | `20250811-acjs-PPK.ipynb` | `pr.plot_steadystate` `hue`/`col` regression. An earlier version merged the full platemap in before plotting; a later commit removed that with no replacement | [bnext#67](https://github.com/bnext-bio/bnext/issues/67) |
| 04_ppk | `20250613-PPK_Mg_Opt.ipynb` | `pr.plot_curves`: `data.READ_COLUMN_NAME` instead of `data[READ_COLUMN_NAME]`. Already fixed on `bnext`'s `main`; the published 0.5.0rc2 package is stale | [bnext#69](https://github.com/bnext-bio/bnext/issues/69) |

## Notebook fixes (2026-08-03)

We debugged all 9 failing notebooks by re-executing them, not by reading them.
Every fix is notebook-side. We changed nothing in `nucleus-cdk`.

- **`onepot-sy`, 3 notebooks.** `ctrl_name='10 uM HPTS'` matched no well in any
  of the 3 platemaps. The line was boilerplate copied from another devnote, and
  no HPTS control was ever run. We skipped `normalize_data_to_controls` and used
  the raw data. Note that 2 of the 3 notebooks had previously "passed" by
  normalizing against a zero-row match, which produced meaningless data. Only 1
  crashed visibly.
- **`04_ppk/20250612-analysis.ipynb`.** Well A23 fit to `k≈0`, which crashed the
  lag-time calculation. We excluded that well and kept its 2 replicates. The
  notebook also raised a `MergeError`, because the steady-state result no longer
  carries a `Well` column. We regrouped with `group_by=["Well","Read"]` and
  flattened the columns before the merge.
- **`04_ppk/20250611-analysis.ipynb`.** The same `MergeError`, same fix. No
  degenerate well in this dataset.
- **`04_ppk/20250613-PPK_Mg_Opt.ipynb`.** A real `nucleus-cdk` bug in
  `plot_curves`. This dataset has 2 `Read` gain settings and the call did not
  split by `Read`. We passed `col="Read"`, which is also the correct plot.
- **`05_pure_workshop/nucleus-pure-protein-debug.ipynb`.** The same degenerate
  well pattern as `04_ppk` (well D5). We excluded that well, and also excluded
  `Type=="Standard"` — those are calibration wells, where sigmoid kinetics means
  nothing, and several were degenerate too. This notebook also had unrelated
  bugs: a misspelled variable (`data_drop_ctrl` for `data_drop_ctrl_0`) across 5
  cells, and 2 names in a later cell that were never defined anywhere.
- **`03_mthfs/20250220-analysis.ipynb`.** Cell 8 computed kinetics on the
  filtered `data_drop` frame, then threw it away. Cell 9 recomputed on the raw
  `data`. We made both use `data_drop`.
- **`08_ppk_cell/20250811-acjs-PPK.ipynb`.** 11 cells called `plot_steadystate`
  with `hue` set to a different column than `x`. Git history confirms an
  upstream regression. No notebook-side fix exists, so we commented out all 11.
  Separately, `find_steady_state(data, group_by="Well")` passed a string where a
  list was expected. Fixed to `group_by=["Well"]`.

## Stale outputs, seqviz and polish (2026-08-04)

This session began with a confusing report. Bugs fixed and committed the day
before still appeared in fresh draft submissions.

**Root cause: `curvenote submit` never re-executes a notebook.** It renders the
outputs already saved in the `.ipynb`. The 2026-08-03 commit fixed the notebook
*code*, but its own `git checkout -- devnotes/` cleanup also threw away the
newly-passing *outputs*. The old error tracebacks stayed baked into the files.

We re-executed all 28 notebooks and committed the refreshed outputs. `git status`
showed all 28 files changed, so every one held stale output — not just the one
that was reported.

Other fixes, each its own commit:

- **`onepot-sy/20260121-Analysis.ipynb` kernelspec** (`d3efa0e`). It pointed at
  `bnext-cdk`, a kernel that was never registered. Switched to `python3`.
- **`manual-submit-all.sh` made concurrent** (`d3efa0e`). Uses `xargs -P`,
  default 6, override with `CONCURRENCY=n`.
- **Stray PDF exports** (`711d3ea`). `curvenote submit` drops an untracked PDF
  into each devnote directory, per its `exports:` config. We deleted the
  accumulated ones. A permanent fix is deferred.
- **`10-nucleus_cytosol_v05` seqviz failure** (`871e92c`). The plasmid-map tab
  showed "seqviz - Unknown Directive". This branch forked before PR #9's fix and
  never picked it up. We cherry-picked it. The fix moves the plugin and its npm
  dependency to a shared `plugins/seqviz/` at the repo root, with `node_modules`
  committed, because CI never runs `npm install` for a devnote's own
  `package.json`.
- **`_build/` leaking** (`573e30d`). `10-nucleus_cytosol_v05` was the only one of
  19 whose `.gitignore` lacked the standard entries. Each devnote's `.gitignore`
  came from whatever template it started with, so they were never consistent. We
  matched it to its siblings and added a repo-wide `_build/` rule.
- **Tab-set formatting** (`f16711e`, `08052bd`). We wrapped the DNA and protein
  tables, the per-experiment protocol tables, and three figure pairs in
  `module-Clpxp` and `module-Clpxp-Cytosol` into MyST tab-sets. Structure only;
  no prose changed.
- **`onepot-sy` blank Figure 4** (`d555f12`). `summary_plot.png` was blank.
  `pr.plot_summary()` calls `plt.show()`, which closes the figure in the inline
  backend. The notebook's later `plt.savefig()` then wrote a new, empty figure.
  We converted `main.md` to embed all four plots directly from their notebook
  cells instead of from saved PNGs. That pattern is already used in `03_mthfs`
  and `04_ppk`, and it avoids this failure completely.

## Issues #17 and #18: two DevNotes recovered from MECA (2026-08-05)

Anton reported two bugs against DevNotes that were live but **not in this repo**.
Both were `TODO` rows here, so nothing in `devnotes/` could fix them.

- **#17**, `Newman-20260421`. `experiments/kinetics-intro.ipynb` had **no install
  cell at all**. Live compute raised `ModuleNotFoundError: No module named 'cdk'`.
- **#18**, `bnext-devnotes-clpxp-pure-cells-01`. Four notebooks used the unpinned
  `!pip install nucleus-cdk | tail -n2`.

**Source recovery.** Neither DevNote existed in this repo,
`bnext-bio/nucleus-developer-notes`, or any other org repo. We recovered both
from their Curvenote MECA archives, linked off the live article pages. This is
the method that PR #22 generalised into the `migrate-devnote` skill, and that issue #21 proposes
for the rest of the migration.

**Why the pin is `0.5.0rc2`, not `0.6.0rc2`.** Unpinned `pip install nucleus-cdk`
resolves to 0.5.3, not the release these notebooks were written against. And
0.6.x deleted `cdk/analysis/cytosol/platereader.py`; it moved to
`cdk/instruments/platereader/legacy/`. Every notebook in both DevNotes imports
the old path, so 0.6.x breaks them.

We tested the install: `nucleus-cdk==0.5.0rc2` installs cleanly on Python 3.14,
the live-compute version, with all 14 dependencies. So `--no-deps` is **not**
needed here. `2026-garenne-pH-sensor` needs it only because 0.6.x requires
`pyarrow>=18,<19`, and pyarrow ships no cp314 wheels.

Every `toc` notebook in both DevNotes now starts with:

```python
!pip install nucleus-cdk==0.5.0rc2 | tail -n2

# Surface a failed install here, rather than as a confusing ModuleNotFoundError
# in the import cell below.
import importlib.metadata as md
assert md.version("nucleus-cdk") == "0.5.0rc2", f"got {md.version('nucleus-cdk')}"
```

The assert comes from the pH-sensor DevNote. `| tail -n2` hides a failed install.
Without the assert, the real error appears much later as a confusing
`ModuleNotFoundError`.

Other fixes needed before the recovered bundles would build:

- **Vendored CDK removed** (`module-Clpxp-Cells`). The bundle carried a full
  `src/cdk/` copy, two 52 KB copies of `platereader.py`, and committed
  `__pycache__`. `20250930-analysis.ipynb` imported the local copy. We pointed it
  at the packaged CDK, matching its siblings.
- **Typst compile failure** (`module-Clpxp-Cells`). `:name: fig:ClpX S` contained
  a space, which Typst labels cannot. Its one reference, `{ref}` fig:ClpX s `,
  also had the wrong case. We renamed it to `fig:ClpX-S`. This is the same bug
  class PR #9 fixed six times.
- **Broken download link** (`module-Clpxp-Cells`). `curvenote.yml` pointed at
  `general/clpxp-module-plasmids-01.zip`. The real file is `general/Plasmids.zip`.
- **Assets that MECA drops.** Neither bundle carried `banner*.webp` or
  `lorem.mjs`, though `curvenote.yml` references both. We restored them from a
  sibling, where they are byte-identical. Newman's bundle also had
  `extends: base.yml` with no `base.yml`, and a stale `thebe: binder:` block
  pointing at the old repo. We removed the first and replaced the second with
  `jupyter: true`.
- **Newman's thumbnail.** `assets/thumbnail.png` is *generated* by the notebook.
  The `assets/` directory was missing, so the notebook crashed on `savefig`. We
  created the directory and kept the `thumbnail:` key. Deleting that key as a
  "dangling reference" was the original mistake: it would also have cost the
  DevNote its thumbnail. **A missing path may be one a notebook creates. Check
  the notebooks before pruning a file or the config that names it.**
- **`20251211-analysis-cytation5.ipynb`**, an orphan not in the `toc`. It failed
  on `normalize_data_to_controls(ctrl_name='10 uM HPTS')` — the same
  copied-boilerplate bug as `onepot-sy`. Its published sibling has no
  normalization step, so we commented the call out.
- **Resource globs** trimmed in both `curvenote.yml` files, down to the
  directories that exist after staging.

**A near-miss worth recording.** The first execution pass forced
`MPLBACKEND=Agg`. Every notebook passed while saving **zero** figures. Because
submit renders saved outputs, that would have published DevNotes with no figures.
We caught it by comparing PNG-output counts against the original MECA bundles,
then re-ran without `MPLBACKEND`. ipykernel's default `matplotlib_inline` backend
is what captures figures. **Always compare figure counts across a re-execution
sweep.**

**"Created a new work" from a local submit is expected.** Draft-submitting
`module-Clpxp-Cells` reported `Created a new work` instead of
`Created a new work version`, which looked like a duplicate. It is not specific
to that DevNote: `module-Clpxp-Cytosol` and `lipid-prep`, both already on `main`,
do the same. Work resolution is scoped to the submitting account, so a personal
token cannot update a work owned by someone else. The real publish path is CI on
push to `main`, which uses the venue token. To check which work a submit hit,
read `work.date_created` in `_build/logs/curvenote.submit.json`.

**Known problems we did not fix**, all pre-existing and visible on the live pages:

- `kinetics-intro.ipynb`'s own table-of-contents anchors do not resolve. The
  headings have no matching MyST targets. Fixing this means editing collaborator
  content beyond a URL, so we left it.
- Newman's `main.md` links to a path in `bnext-bio/bnext`, which 404s for
  `curvenote check` because that repo is private.
- Three `module-Clpxp-Cells` figures are over 3 MB, which slows the webp
  conversion at build time.

## Orphaned notebooks

These exist on disk but no `toc` references them. That does not make them broken.
It does mean they are not published, and some are clearly stale.

- `src/20250220-analysis.ipynb`, a template scaffold left over in `03_mthfs`,
  `04_ppk`, `05_pure_workshop`, `08_ppk_cell`, `10-nucleus_cytosol_v05`,
  `11-Base_Cell`, `module-Clpxp` and `module-Clpxp-Cytosol`.
- `04_ppk`: `20250611-analysis-acjs-test.ipynb`.
- `05_pure_workshop`: `20250516-labchip-analysis.ipynb`,
  `nucleus-pure-protein-debug-draft.ipynb`, `20250516-final-experiment.ipynb`.
- `08_ppk_cell`: 3 "Code (yh)" notebooks beside the "Code (acjs)" one in the
  `toc`. This looks like two authors working in parallel.
- `11-Base_Cell`: `experiments/20251119-nucleus-liposomes/Untitled.ipynb`.
- `devnote-nucleus_onepot`: 2 more debug notebooks beside the one in the `toc`.
- `fwm-batch-bo`, `lipid-prep`: one `20250220-analysis.ipynb` scaffold each.

None were deleted. **Do not delete a notebook without asking first.**

## Data-quality flags from the old bulk downloads

The `devnotes-downloaded/` and `sy-devnotes-download/` directories are gone, but
these findings still matter for future migrations.

- **`Base_Cell` raw data.** Two liposome-imaging CSVs, 1.6 GB and 702 MB, sit
  under an experiment folder no `toc` references. GitHub hard-blocks any file
  over 100 MB at push time, so these cannot be committed as plain files. They
  need Git LFS or external storage.
- **Myst key collisions.** The key `b6272c31-dae6-4c60-bf48-a86466349d86` was
  shared by four directories: a placeholder stub, plus three with real content.
  The finished "DevCells: Kickoff Workshop" is the real one. Each needs its own
  key before migration.
- **Author mismatch.** `devnote-test/` held the MTHFS content, which `03_mthfs`
  credits to Yemo Ku, but listed Surendra Yadav as its author. Unresolved.
