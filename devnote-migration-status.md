# DevNote migration status

This file tracks every DevNote: where it lives, whether it is published, and
what still needs to move.

To migrate a DevNote, start at [`MIGRATION-PLAYBOOK.md`](./MIGRATION-PLAYBOOK.md).
It links to the full procedure and a catalogue of known snags, which live in the
`migrate-devnote` skill. This file records **state**; the playbook records
**method**.

## Summary as of 2026-08-05

| Count | Meaning |
|---|---|
| **49** | DevNotes published on the venue |
| **51** | DevNotes in this repo |
| **48** | in this repo **and** published |
| **3** | in this repo and submitted, but not yet published |
| **1** | published, but **not yet in this repo** |
| **0** | of that 1, cleared for this repo — **the migration is complete** |

Two corrections to earlier versions of this file, both found on 2026-08-05:

1. **This file used to be incomplete.** It listed 28 DevNotes. The venue
   publishes 49. The earlier count missed the `Node Chicago`, `Node London`,
   `AI Scientist` and `Workshops and Courses` collections entirely. Always
   enumerate from the venue, never from this file.
2. **"Needs author outreach" was wrong.** This file used to say two DevNotes
   probably needed us to contact their authors. Both are published, both have
   a downloadable MECA archive, and on 2026-08-05 both were recovered from it
   with no author contact at all — see `2026-falcon-liposome-encapsulation`
   and `2026-oza-synthetic-cells-lab-manual`.

## Before you migrate anything

This repo is only for DevNotes released fully in the open, under CC-BY or a
CERN-OHL-P equivalent. **A human must decide whether a DevNote may be included.**
Never automate that decision. Many of the remaining DevNotes come from
external contributors at the Chicago and London nodes, so this matters.

### Curation decisions of 2026-08-05

Jon Calles reviewed the 30 DevNotes then outstanding and cleared all of them
except one:

- **"Tunable protein expression strength with toehold exchange riboregulators"**
  (Samuel Schaffter, Fernanda Piorino, Eugenia Romantseva, key
  `7b6aaa00-7351-4a7e-ba45-ade3f7332335`) — **not licensed for this repo. Do not
  migrate it.**
- Charlie Newell's RNA aptamers DevNote is also not licensed for this repo. It
  is not published on the venue, so it never enters the work list. Nothing to
  skip, but do not add it by hand either.

Every other outstanding DevNote has a compatible licence.

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

**Match `devnotes/*/curvenote.yml` exactly — one level deep.** A looser pattern
such as `git ls-files '*curvenote.yml'` returns 53, not 51: `fwm-aria-d1` ships
two more inside its `data/` tree, from sub-DevNotes IGOR generated during the
run. They are data, not DevNotes in this repo, and counting them overstates the
total by two.

## Every DevNote

A DevNote is **live** once the venue publishes it. A DevNote that is in the
repo but not yet live is waiting on a curator to approve its submission.
"Reviewed" means a human read `main.md` from start to end.

| Title | Author(s) | Collection | Myst key | Status |
|---|---|---|---|---|
| Characterizing the Limited Operational Lifetime of Cytosol Reactions | Surendra Yadav | Core | `019ed70b-0af7-7dd0-aefe-688ebf933399` | Submitted from `2026-yadav-cytosol-lifetime`, recovered from MECA. `curvenote check` passes, 6/6 frontmatter, PDF builds. No `toc` notebooks. **Still needs a content review.** [Build report](https://scms.curvenote.com/build/019fd4e3-d4b1-7374-8348-1817e823f704) |
| ClpXP Control Module: Deployment in Nucleus Cytosol | Yen-Yu Hsu | Core | `019f05c8-f7ea-74d8-ab37-a6e418627268` | Submitted from `2026-hsu-clpxp-cytosol`, recovered from MECA. `curvenote check` passes, 6/6 frontmatter, PDF builds. No `toc` notebooks. **Still needs a content review.** [Build report](https://scms.curvenote.com/build/019fd4e3-c412-7d96-9010-55907d500a37) |
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
| SecYEG-Based Membrane Translation Module in Synthetic Cells | Yen-Yu Hsu | Core | `019e896a-6e0d-76d5-99ef-2df38c5ebd7f` | Submitted from `2026-hsu-secyeg`, recovered from MECA. `curvenote check` passes, 7/7 frontmatter. No `toc` notebooks. **No PDF export** — see the note below. **Still needs a content review.** [Build report](https://scms.curvenote.com/build/019fd4e3-b7a9-7459-b265-d513e13d6a46) |
| The Developer Cell Control Module: Protein Degradation by ClpXP | Yen-Yu Hsu | Core | `nucleus-devnote-core-06_clpxp_module_01` | Live, from `module-Clpxp`. No notebooks to run. Reviewed. [Build report](https://scms.curvenote.com/build/019fcdc0-9407-7fae-986e-2fefa44eb448) |
| Using platemaps to analyze and share data | Jay Bhasin | Core | `019d6e3a-c618-77bc-853c-fe4694511f53` | Submitted from `2026-bhasin-platemaps`, recovered from MECA. Its notebook passes, pinned to `nucleus-cdk==0.5.0rc2`. `curvenote check` passes, PDF builds. **Still needs a content review.** [Build report](https://scms.curvenote.com/build/019fd4e3-a72d-7b40-99b4-9962d40f67e6) |
| BCECF pH Sensor | David Garenne | Community | `nucleus-devnote-core-2026-garenne-ph-sensor` | Live, from `2026-garenne-pH-sensor`. Its notebook passes. Reviewed. Submitted in PR #16. |
| DNA toolkit - The T7 terminator collection | Charlie Newell | Community | `cn-05272026-terminators` | In `DNA-toolkit-T7-terminators`, recovered from MECA. Its notebook passes, pinned to `nucleus-cdk==0.5.0rc2`. `curvenote check` passes, 8/8 frontmatter, 3/3 content, PDF builds. **Still needs a content review.** |
| Energy Metabolism Working Group at Build-a-Cell #15 | Energy Metabolism Working Group | Community | `bac-working-group` | Live, from `bac-working-group`. No notebooks to run. Reviewed. [Build report](https://scms.curvenote.com/build/019fcdbd-d5e0-7602-bfb7-f1c75b3b30e1) |
| London Exchange Meeting: Liposome Protocol Survey | London Exchange Meeting Participants | Community | `019dcea0-91e3-78da-be6d-6450c2ff8308` | Live, from `lipid-prep`. No notebooks to run. Reviewed. [Build report](https://scms.curvenote.com/build/019fcdbd-7f13-7cc3-b358-c42e0c6c3bcd) |
| Tunable protein expression strength with toehold exchange riboregulators | Samuel Schaffter, Fernanda Piorino, Eugenia Romantseva | Community | `7b6aaa00-7351-4a7e-ba45-ade3f7332335` | **Not in the repo yet.** Published, so recoverable from its MECA archive. |
| AI Scientist: Base Module Report | IGOR, b.next, FindWhatMatters | AI Scientist | `019dcbd4-f87a-7e0d-97d7-6e58ef3403df` | In `fwm-aria-d1`, recovered from MECA, **minus 31 unreferenced PDFs** — see the note below. `curvenote check` passes, 10/10 content, PDF builds. Its notebook only displays an image, so nothing to pin. **Still needs a content review.** |
| Batch Bayesian Optimization | Joseph Lozier | AI Scientist | `019f9b60-cc79-7008-9c25-4a46b53b8604` | Live, from `fwm-batch-bo`. No notebooks to run. Reviewed. [Build report](https://scms.curvenote.com/build/019fcdbe-1b37-7658-8b35-e8be01ca926f) |
| Defining AI Scientific Workflows: Using IGOR for Optimization of PURE | b.next, Find What Matters | AI Scientist | `019f6db2-e060-710d-8984-6bcd5747d775` | Live, from `fwm-aria-d2`. No notebooks to run. Reviewed. [Build report](https://scms.curvenote.com/build/019fcdbe-363a-77c5-936a-17af2178ef46) |
| IGOR PPK Optimization: Round 1 | Scott Riggs, IGOR | AI Scientist | `51030dec-7ab4-475a-8312-9c73c9d24301` | In `fwm-igor-ppk-r1`. **No MECA archive** — rebuilt from the venue's published assets. `curvenote check` passes, PDF builds. Two broken `{include}`s and two unknown roles carried over from the live article; see the note below. **Still needs a content review.** |
| IGOR PPK Optimization: Round 2 | Scott Riggs, IGOR | AI Scientist | `591140bb-e66b-415b-ae5c-03302aa68bbe` | In `fwm-igor-ppk-r2`. **No MECA archive** — rebuilt from the venue's published assets. `curvenote check` passes, PDF builds. Same broken `{include}`s and roles, plus one broken data link; see the note below. **Still needs a content review.** |
| DevCells: Kickoff Workshop | DevCells Kickoff Workshop | Workshops and Courses | `b6272c31-dae6-4c60-bf48-a86466349d86` | In `devcells-kickoff-workshop`, recovered from MECA. Both notebooks pass, pinned to `nucleus-cdk==0.5.0rc2`. `curvenote check` passes. **No PDF export** — see the note below. **Still needs a content review.** |
| Liposome encapsulation: A tractable and reproducible approach | Chris Falcon, Katie Drew | Workshops and Courses | `9e302e31-3dbb-494a-b8e3-5fc6d91ea941` | In `2026-falcon-liposome-encapsulation`, recovered from MECA. `curvenote check` passes, 13/15 frontmatter, PDF builds. No notebooks. **Still needs a content review.** |
| Nucleus OnePot PURE workshop | OnePot Workshop | Workshops and Courses | `nucleus-devnote-core-09_pure-workshop` | Live, from `05_pure_workshop`. All 5 notebooks pass. Reviewed. [Build report](https://scms.curvenote.com/build/019fcdbd-8559-7af4-b014-96363dd453b1) |
| Synthetic Cells Course Lab Manual: Cell-free Gene Expression and Liposome Encapsulation | Javin P Oza | Workshops and Courses | `118a7ada-92d1-448f-adc2-f19c2da16b16` | In `2026-oza-synthetic-cells-lab-manual`, recovered from MECA. `curvenote check` passes, 10/10 frontmatter, PDF builds. No notebooks. Its `date:` was a placeholder — see the note below. **Still needs a content review.** |
| Biochromatic Materials | Maddie Briggs, Maram Naji, Mary Kelly, Matthew Lucia, Natalie Fisher, Ojaswita Pant, Samuel Chen, Allen Liu, Cecile Chazot, Danielle Tullman-Ercek, Julius Lucks, Neha Kamat, Ryan Truby | Node Chicago | `dd21c8ff-f44c-415c-83ee-8fc9ab9badc7` | In `chicago-biochromatic-materials`, recovered from MECA, minus the MTHFS template scaffolding. `curvenote check` passes, PDF builds. No `toc` notebooks. **Still needs a content review.** |
| Colorimetric Sensing Module Development Plan | Cécile A. C. Chazot, Natalie C. Fisher, Simona Fine | Node Chicago | `NCF-planningDevNote-01` | In `chicago-colorimetric-sensing-plan`, recovered from MECA, minus the MTHFS template scaffolding. `curvenote check` passes, PDF builds. No `toc` notebooks. **Still needs a content review.** |
| Double emulsion optimization: inner solution, lipid concentration, and composition | Mary Kelly | Node Chicago | `019d643c-63e8-74f3-a5f6-ae8d29175383` | In `chicago-double-emulsion`, recovered from MECA, minus the MTHFS template scaffolding. `curvenote check` passes, PDF builds. Fixed a duplicate figure label. **Its corresponding email is a placeholder** — see the note below. **Still needs a content review.** |
| Environmentally Responsive Materials via Integration of DevCells | Madison Briggs | Node Chicago | `mrb_kamatlab` | In `chicago-env-responsive-materials`, recovered from MECA, minus the MTHFS template scaffolding. PDF builds, but `curvenote check` **exits 1: no author email** — see the note below. **Still needs a content review.** |
| In Vitro Reporter Validation | Matthew Lucia | Node Chicago | `mjl-devnote-kickoff-workshop` | In `chicago-invitro-reporter`, recovered from MECA, minus the MTHFS template scaffolding. `curvenote check` passes, PDF builds. No `toc` notebooks. **Still needs a content review.** |
| Matrix Design for Stable Liposomes and Efficient Cell-Free Protein Synthesis | Mary Kelly | Node Chicago | `PlanningDevNoteMaryKelly` | In `chicago-matrix-design`, recovered from MECA, minus the MTHFS template scaffolding. PDF builds, but `curvenote check` **exits 1: no author email** — see the note below. **Still needs a content review.** |
| Module Development Plan: DevCell-based pH sensor | Samuel J. Chen, Sung-Won Hwang | Node Chicago | `sjcliulab` | In `chicago-ph-sensor-plan`, recovered from MECA, minus the MTHFS template scaffolding. `curvenote check` passes, PDF builds. No `toc` notebooks. **Still needs a content review.** |
| Photopatterned Hydrogels with DevCells | Ojaswita Pant | Node Chicago | `ojaswitapant` | In `chicago-photopatterned-hydrogels`, recovered from MECA, minus the MTHFS template scaffolding. `curvenote check` passes, PDF builds. No `toc` notebooks. **Still needs a content review.** |
| TetO-Catecholase sensor validation in Nucleus Cytosol | Maram Naji | Node Chicago | `019db237-0d03-7ae1-8c40-e57e2ce1bea1` | In `chicago-teto-catecholase`, recovered from MECA, minus the MTHFS template scaffolding. `curvenote check` passes, PDF builds. No `toc` notebooks. **Still needs a content review.** |
| Theophylline-LacZ sensor validation in Nucleus Cytosol | Maram Naji | Node Chicago | `019d20e4-4787-7f35-9c77-f2f53f43d107` | In `chicago-theophylline-lacz`, recovered from MECA, minus the MTHFS template scaffolding. `curvenote check` passes, PDF builds. No `toc` notebooks. **Still needs a content review.** |
| Toehold switch-enabled translation regulation verified in Nucleus Cytosol | Samuel J. Chen, Sung-Won Hwang, Allen Liu | Node Chicago | `sjcliulab01` | In `chicago-toehold-switch`, recovered from MECA, minus the MTHFS template scaffolding. `curvenote check` passes, PDF builds. No `toc` notebooks. **Still needs a content review.** |
| Validation of colorimetric reporter sensors in Nucleus Cytosol | Maram Naji \| Lucks Lab | Node Chicago | `MN_LucksLab` | In `chicago-colorimetric-validation`, recovered from MECA, minus the MTHFS template scaffolding. `curvenote check` passes, PDF builds. No `toc` notebooks. **Still needs a content review.** |
| Bioprinting Synthetic Cells Within a Hydrogel Matrix | Niall McIntyre, Ravinash Krishna Kumar | Node London | `nm191611111` | In `london-bioprinting-hydrogel`, recovered from MECA, minus the MTHFS template scaffolding. `curvenote check` passes, PDF builds. Its `BioPrinting.png` was recovered from the venue — see the note below. **Still needs a content review.** |
| Diffusion Kinetics | Jonah McDonald, James Hindley | Node London | `JMcDDiffusionKinetics-01` | In `london-diffusion-kinetics`, recovered from MECA, minus the MTHFS template scaffolding. `curvenote check` passes, PDF builds. No `toc` notebooks. **Still needs a content review.** |
| Hydrogel-Embedded GUV Developer Cells | Ion Ioannou, Ignacio Gispert, James Hindley, Ocar Ces | Node London | `II9a7f1e82-58ea-42a8-896c-7312b3538ef6` | In `london-hydrogel-guv-devcells`, recovered from MECA, minus the MTHFS template scaffolding. `curvenote check` passes, PDF builds. No `toc` notebooks. **Still needs a content review.** |
| LacZ/XylE colour change module | Charlie Newell, Michael Booth | Node London | `CN_London_planning_DevNote` | In `london-lacz-xyle-module`, recovered from MECA, minus the MTHFS template scaffolding. `curvenote check` passes 11/11 frontmatter, PDF builds. Renamed one label containing spaces. **Still needs a content review.** |
| Quorum Sensing Polymersome | Julia Purrinos De Oliveira, Claudia Contini | Node London | `62abfe00-110e-41e1-8121-4572a093eb17` | In `london-quorum-sensing-polymersome`, recovered from MECA, minus the MTHFS template scaffolding. `curvenote check` passes 10/10 frontmatter, PDF builds. Renamed one label containing spaces; its `AHL.jpg` thumbnail was recovered from the venue. **Still needs a content review.** |
| The colourimetric bacterial contamination sensing device. | Charlie Newell, Ion Ioannou, Jonah McDonald, Julia Purrinos De Oliveira, Manuel Bibrowski, Niall McIntyre, Ignascio Gispert, Claudia Contini, James Hindley, Michael Booth, Oscar Ces, Ravinash Krishna Kumar, Yuval Elani | Node London | `bd8b42b4-8a91-40c8-a636-3778d1c9a072` | In `london-colourimetric-device`, recovered from MECA, minus the MTHFS template scaffolding. `curvenote check` passes, PDF builds. No `toc` notebooks. **Still needs a content review.** |
| IV-HSL Emitter Cell | — | — | `nucleus-devnote-core-02_emitter_cell` | In `02_emitter_cell`, waiting on the curator. No notebooks to run. Reviewed. [Build report](https://scms.curvenote.com/build/019fcdbe-5745-7f49-a3f6-68ef77450817) |
| First Nucleus Cytosol Testing | — | — | `nucleus-devnote-core-NucelusPURE_deGFP` | In `10-nucleus_cytosol_v05`, waiting on the curator. Both notebooks pass. Reviewed. [Build report](https://scms.curvenote.com/build/019fcdbd-c96c-7e3b-815d-b4c130a2f023) |
| Cx43 Cell | — | — | `nucleus-devnote-core-01_contrib_cx43_cell` | In `cx43`, waiting on the curator. No notebooks to run. Reviewed. [Build report](https://scms.curvenote.com/build/019fcdbd-a991-7f87-9dce-bdd7f07c9395) |

Notes on the rows above:

- **`2026-hsu-secyeg` publishes without a PDF.** It lays its figures out with
  `{grid}` inside `{tab-set}` (`main.md` lines 421 and 440). Typst has no
  conversion for a `grid` node, so it drops the node **and the four figures
  inside it**. The `{ref}` calls to those figures then fail with `label
  <fig:local-emre> does not exist in the document`, and the PDF never builds.
  Deleting the two `{grid}` wrappers would probably fix it — a one-column grid
  renders much like stacked figures — but that changes the author's layout, so
  the typst export and the "Download Article PDF" entry are left out instead.
  The published version has no PDF either, so nothing is lost. Reinstate both
  if Yen-Yu Hsu agrees to the change, or if Typst gains `grid` support.
- **Three JATS conversion messages are author-content limits, not config bugs.**
  `2026-bhasin-platemaps` builds a `{table}` whose body is an `{include}` of
  `assets/simple-platemap.txt`, so that table is empty in JATS and in the PDF;
  it also uses `{aside}`. `2026-hsu-clpxp-cytosol` uses a thematic break outside
  a table cell. All three still pass `curvenote check`. Leave them to their
  authors.
- **`2026-yadav-cytosol-lifetime` keeps four notebooks that never render.** Its
  `toc` is `main.md` alone, and `main.md` embeds pre-generated PNGs as static
  figures. The four `analysis.ipynb` files ship as resources. That is the
  author's design, so they were not added to the `toc` and not re-executed.
- **Its `experiments/Test1.tar.gz` and `Test4.tar.gz` are not redundant.** They
  look like duplicates of the extracted experiment directories, and `Test2` and
  `Test3` are. But `Test1` holds a `summary.png` that exists nowhere else, and
  both hold a different `analysis.ipynb` from the one on disk. They were kept.
  Verify before deleting an archive.
- **`DNA-toolkit-T7-terminators` carries an orphan notebook.** Its
  `src/20250220-analysis.ipynb` is a 24-cell notebook titled "20250220
  analysis" — MTHFS scaffolding, copied in with the vendored `src/cdk/` tree.
  It is in no `toc` and nothing references it. The vendored CDK and its `.pyc`
  files were deleted; the notebook was kept, because deleting a notebook is
  not an automated decision. Charlie Newell should confirm it can go.
- **`fwm-aria-d1` ships without 31 PDFs that its archive contained.** Its
  `data/**/*` glob pulled in 31 PDF files, 29.6 MB of the bundle's 72 MB, 15
  unique after duplicates. Among them: four third-party journal papers
  (Shimizu 2001 in *Nature Biotechnology*, Li 2014 in *PLoS ONE*, Lavickova
  2019 in *ACS Synthetic Biology*, and a "PURE overview"), plus "20250630
  FWMai_bnext Meeting Notes", which appeared three times. None of the 31 was
  referenced by any `main.md`, notebook or config. Jon Calles decided on
  2026-08-05 to drop all of them, rather than redistribute paywalled papers
  and internal notes from a fully-open repo. Verified inert: the DevNote
  builds identically without them — same 10/10 content, same 2.9 MB PDF — and
  the tree is 43 MB instead of 72 MB. **This is the licensing gate applied per
  file, not per DevNote. Run the same check on every bundle.**
- **A second call on `fwm-aria-d1`, still open.** The same sweep found **31
  Office documents** — `.docx` drafts, `.pptx` decks, curation notes, and
  files like "Prompt to not do OFAT.docx". All 31 are unreferenced too. They
  were **kept**, on the grounds that the PDFs were third-party copyrighted
  work while these are b.next's and Find What Matters' own writing, published
  by their own authors through the venue's archive. That is a judgement about
  disclosure, not copyright, so it is reversible and cheap:

  ```bash
  find devnotes/fwm-aria-d1 -type f \( -iname '*.doc*' -o -iname '*.ppt*' \) -delete
  ```

  Confirm with Anton Jackson-Smith and Scott Riggs before this reaches `main`,
  because merging is what publishes it.
- **Node London shipped the same MTHFS scaffolding, and it was removed too.**
  All six carried the byte-identical `experiments/experiment-01/` and
  `general/schematic-FA_metabolism.png`. Same template, same decision.
- **Two Node London files were recovered from the venue, not the archive.**
  `london-bioprinting-hydrogel`'s `main.md` embeds `/BioPrinting.png` from the
  project root, which no `resources:` glob matched, so MECA never shipped it —
  the article would have built with a missing figure. `london-quorum-sensing-
  polymersome`'s `AHL.jpg` thumbnail was missing the same way. Both are
  published as assets and were downloaded. **When a recovered figure is
  missing, check the article page before dropping the reference.**
- **Two more labels with spaces, both renamed.**
  `london-lacz-xyle-module` used `:name: Colour change module schematic` and
  `london-quorum-sensing-polymersome` used `:label: fig:Module Diagram`.
  Neither was referenced, and both would have failed the PDF export.
- **Every Node Chicago DevNote shipped MTHFS's example data.** Eleven of the
  twelve carried an identical `experiments/experiment-01/` — the
  `20250220-analysis.ipynb` scaffold notebook, MTHFS plate data, MTHFS
  figures, and `MTHFS-labnotebook.pdf` — plus
  `general/schematic-FA_metabolism.png`. It comes from the DevNote template,
  is in no `toc`, is referenced by no `main.md`, and duplicates content the
  repo already holds as `03_mthfs`. Jon Calles approved deleting it on
  2026-08-05. That took the batch from about 65 MB to 11 MB. Each author's own
  files were kept, including data and sequences they never cited. The same
  scaffold explains two earlier puzzles: the orphan notebook in
  `DNA-toolkit-T7-terminators`, and `2026-hsu-clpxp-cytosol`'s thumbnail
  pointing at `general/schematic-FA_metabolism.png`.
- **Three Node Chicago DevNotes have a contact problem. Do not guess.**
  `chicago-env-responsive-materials` (Madison Briggs) and
  `chicago-matrix-design` (Mary Kelly) declare no author email, so
  `curvenote check` exits 1 — the same blocker `bac-working-group` has had all
  along. Worse, `chicago-double-emulsion` publishes
  **`mary.kelly@example.com`**, a placeholder that is live on the venue right
  now; it passes the check precisely because an address exists, and
  correspondence would go nowhere. Addresses for both people appear in
  `chicago-biochromatic-materials`, the 13-author node DevNote they co-wrote:
  `mbriggs@u.northwestern.edu` and `marykelly2026@u.northwestern.edu`. Those
  look authoritative, but a contact detail is the authors' to confirm, so
  nothing was changed. Confirm with Madison Briggs and Mary Kelly, then set
  all three.
- **`chicago-invitro-reporter` lost a dangling thumbnail.** It pointed at
  `general/exa.png`, which is in neither the archive nor the venue's published
  assets, and no notebook generates it. The key was dropped; its banner is
  unaffected.
- **`chicago-double-emulsion` had two figures sharing one label.** Its
  `GUV-diameter.jpg` figure was labelled `GUV-count`, the same as the figure
  above it. Nothing referenced either, so the second was renamed to
  `GUV-diameter`.
- **`devcells-kickoff-workshop` publishes without a PDF, for the same reason
  as `2026-hsu-secyeg`.** Its `main.md` wraps the "Kinetic Fits" tab-set in
  `:::{admonition}` with a custom title (line 218). The bnext Typst template
  reports "Unknown admonition kind", drops the block, and the two figure
  labels inside go with it, so `{ref}`Group1-kineticfit`` and
  `Group2-kineticfit` dangle and the export fails. Deleting the admonition
  wrapper and keeping the bare tab-set would fix it — the other five tab-sets
  in the file are unwrapped — but that removes the collapsible "Kinetic Fits"
  heading the authors chose. Setting `:class: dropdown` instead of
  `simple, dropdown` was tried and does not help; the template rejects the
  custom title itself.
- **Two real fixes in `devcells-kickoff-workshop`, both kept.** Its figure
  `:label: participants` collided with the automatic label of the
  `# Participants` heading, which Typst reports as "label occurs multiple
  times"; the figure is now `participants-photo`, with its one `{ref}`
  updated. And `analysis-G1.ipynb` saved its summary figure as
  `kinetics-summary-1.png` while `main.md` referenced
  `kinetics-summary-group1.png` — a typo, since its sibling `analysis-G2.ipynb`
  writes the `-group2` form. The notebook now regenerates the file `main.md`
  actually uses.
- **`2026-oza-synthetic-cells-lab-manual` had a placeholder for a date.** Its
  `curvenote.yml` carried the literal string
  `REVIEW: not found in source — confirm with course organizers` in `date:`.
  The venue publishes the article with `2026-07-20`, so that is what the
  recovered file now uses. Worth confirming with Javin P Oza. Its `main.md`
  frontmatter also declares affiliations whose `id` and `name` are not
  strings, which `curvenote check` reports; that is author content, left alone.
- **The two IGOR rounds have no MECA archive.** Their article pages offer none.
  They were rebuilt from the venue's published assets instead: `config.json`
  supplies the frontmatter and work key, and `main.md` supplies the original
  relative paths, because the site truncates every asset's stem to 20
  characters and appends a content hash. The method is in the skill's
  `references/recover.md` §3. Expect more of these — check for an archive
  first, and fall back to this.
- **Both IGOR rounds ship two broken `{include}`s and two unknown roles.**
  `main.md` does `{include} discourse.md` and `{include} ges.md`, and uses
  `{claim}` and `{evidence}` roles. None of those files, and no plugin
  defining those roles, was ever published — the live articles render the
  literal text `discourse.md`. This is not migration damage; it is the
  published state. **Find What Matters needs to supply the two files and the
  discourse-graph plugin.** `fwm-igor-ppk-r2` additionally links
  `./workspace/workspace_data.csv`, which was never published either.
- **Round 2's includes were deliberately left broken.** Jon Calles decided on
  2026-08-05 to migrate both rounds exactly as published, and to ask Find What
  Matters for the missing files rather than reconstruct them. The evidence
  behind the option not taken is kept below, in case that changes.
- **A likely fix for Round 2's includes, if it is ever wanted.**
  `fwm-aria-d1` contains `orchestrated-research/iter2/`, whose `main.md` is
  byte-identical to `fwm-igor-ppk-r2`'s except for the title and an added
  "generated by an AI Scientist" notice, and whose 11 figures are all
  byte-identical. Its `discourse.md` and `ges.md` are therefore very probably
  the missing files. They were **not** copied across, because that would add
  content to a published article. Approve it and it is a two-file copy.
  **Do not do the same for Round 1**: `iter1` is a different report, with a
  different abstract and a completely different set of five figures.
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
