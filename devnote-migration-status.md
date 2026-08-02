| Title | Author | Myst Key | Collection | Status |
|---|---|---|---|---|
| IV-HSL Emitter Cell | Yen-Yu Hsu | nucleus-devnote-core-02_emitter_cell | | staged, untested |
| MTHFS - an Unexpected Enzyme in PURE | Yemo Ku | nucleus-devnote-core-03_mthfs | Core | staged, untested |
| PPK Module testing in PURE | Surendra Yadav | nucleus-devnote-core-04_ppk | Core | staged, untested |
| Nucleus OnePot PURE workshop | OnePot Workshop | nucleus-devnote-core-09_pure-workshop | Workshops and Courses | staged, untested |
| Integrating PPK Module in PURE Cells | Yen-Yu Hsu | nucleus-devnote-core-08_ppk-module-in-pure-cell | Core | staged, untested |
| Cx43 Cell: DNA Validation | Yen-Yu Hsu | nucleus-devnote-core-cx43_01 | Core | staged, untested |
| First Nucleus Cytosol Testing | Surendra Yadav | nucleus-devnote-core-NucelusPURE_deGFP | Core | staged, untested |
| Nucleus Base Cell Testing | Surendra Yadav | nucleus-devnote-core-Base_Cell | Core | staged, untested |
| ClpXP Control Module: Deployment in Nucleus Cytosol | Yen-Yu Hsu | 019f05c8-f7ea-74d8-ab37-a6e418627268 | Core | TODO |
| Characterizing the Limited Operational Lifetime of Cytosol Reactions | Surendra Yadav | 019ed70b-0af7-7dd0-aefe-688ebf933399 | Core | TODO |
| SecYEG-Based Membrane Translation Module in Synthetic Cells | Yen-Yu Hsu | 019e896a-6e0d-76d5-99ef-2df38c5ebd7f | Core | TODO |
| Using platemaps to analyze and share data | Jay Bhasin | 019d6e3a-c618-77bc-853c-fe4694511f53 | Core | TODO |
| Intro to Kinetics Analysis of Plate Reader Experiments | Sharon Newman | 019db3ce-4971-7fd6-83c0-c1a15e780bbe | Core | TODO |
| Nucleus OnePot PURE | Surendra Yadav | onepot-sy | Core | staged, untested (devnotes/onepot-sy) |
| ClpXP Control Module: Deployment in PURE Cells | Yen-Yu Hsu | nucleus-devnote-core-clpxp_module_cells-01 | Core | TODO |
| ClpXP Control Module: Deployment in PURE | Yen-Yu Hsu | nucleus-devnote-core-clpxp_module_cytosol-01 | Core | staged, untested (devnotes/module-Clpxp-Cytosol) |
| DNA toolkit - The T7 promoter collection | Charlie Newell, Astrid Joergensen | nucleus-devnote-core-dna-toolkit-promoter | Core | staged, untested (devnotes/DNA-toolkit-T7-promoters) |
| Nucleus OnePot PURE Replication | Anton Molina, Anton Jackson-Smith | nucleus-devnote-core-07_bnext-onepot-pure-replication | Core | staged, untested (devnotes/devnote-nucleus_onepot) |
| The Developer Cell Control Module: Protein Degradation by ClpXP | Yen-Yu Hsu | nucleus-devnote-core-06_clpxp_module_01 | Core | staged, untested (devnotes/module-Clpxp) |
| Developer Cell: Project Introduction | Anton Jackson-Smith, Akshay Maheshwari | nucleus-devnote-core-05_devcell_01 | Core | staged, untested (devnotes/devnote-developer_cell) |
| Liposome encapsulation: A tractable and reproducible approach | Chris Falcon, Katie Drew | 9e302e31-3dbb-494a-b8e3-5fc6d91ea941 | Workshops and Courses | TODO |
| Synthetic Cells Course Lab Manual: Cell-free Gene Expression and Liposome Encapsulation | Javin P Oza | 118a7ada-92d1-448f-adc2-f19c2da16b16 | Workshops and Courses | TODO |
| DevCells: Kickoff Workshop | DevCells Kickoff Workshop | b6272c31-dae6-4c60-bf48-a86466349d86 | Workshops and Courses | TODO |
| Tunable protein expression strength with toehold exchange riboregulators | Samuel Schaffter, Fernanda Piorino, Eugenia Romantseva | 7b6aaa00-7351-4a7e-ba45-ade3f7332335 | Community | TODO |
| DNA toolkit - The T7 terminator collection | Charlie Newell | cn-05272026-terminators | Community | TODO |
| Energy Metabolism Working Group at Build-a-Cell #15 | Energy Metabolism Working Group | bac-working-group | Community | staged, untested (devnotes/bac-working-group) |
| London Exchange Meeting: Liposome Protocol Survey | London Exchange Meeting Participants | 019dcea0-91e3-78da-be6d-6450c2ff8308 | Community | staged, untested (devnotes/lipid-prep) |
| Cx43 Cell | Ahmed Z. Sihorwala | nucleus-devnote-core-01_contrib_cx43_cell | Community | staged, untested (devnotes/cx43) |

## Remaining TODO rows (2) — likely require contacting original authors

**Update:** Anton's work on this branch (flat `devnotes/` restructure, commits `578ea19`..`8370dd9`) staged real, committed content for 7 of the previous 9 "genuinely missing" rows directly into `devnotes/` — not just found in a bulk download, but full devnote directories with `curvenote.yml`/`main.md`/notebooks matching the tracked Myst Key exactly. Verified by grep: no trace of the remaining 2 titles/authors anywhere in `devnotes/`, `devnotes-downloaded/`, or `sy-devnotes-download/`. Only these 2 rows still need outreach to the original authors:

| Title | Author(s) | Myst Key | Collection |
|---|---|---|---|
| Liposome encapsulation: A tractable and reproducible approach | Chris Falcon, Katie Drew | `9e302e31-3dbb-494a-b8e3-5fc6d91ea941` | Workshops and Courses |
| Synthetic Cells Course Lab Manual: Cell-free Gene Expression and Liposome Encapsulation | Javin P Oza | `118a7ada-92d1-448f-adc2-f19c2da16b16` | Workshops and Courses |

Note: the two rows above (`onepot-sy`, `bac-working-group`) were previously "found (sy-devnotes-download/...), not staged"; both have since been staged into `devnotes/onepot-sy` and `devnotes/bac-working-group` (Step 1 of the migration plan), excluding `onepot-sy`'s `plasmids/PURE_plasmids.tar.gz` DNA archive, which is handled by a separate DNA-reconciliation workstream. Also new on this branch, outside the original tracker scope: `devnotes/fwm-aria-d2` (ARIA/IGOR optimization) and `devnotes/fwm-batch-bo` (Batch Bayesian Optimization) — new devnotes, not migrations of tracked TODO rows.

## Manual review checklist (all 19 devnotes currently in `devnotes/`)

Three review steps per devnote, each its own column: **notebooks run** (have the
notebooks actually been executed/re-executed and outputs checked), **content
reviewed** (has a human actually read `main.md` end to end), **submitted** (a
REAL, non-draft `curvenote submit` — an editor can't act on a draft, so a
draft build does not count as submitted here). Draft URL is the most recent
`https://scms.curvenote.com/build/...` link — draft or real — open it to see
the live preview; it does not by itself mean "submitted."

Run `./manual-submit-all.sh` (repo root) to (re-)submit **drafts** for every
devnote in one pass and get fresh preview URLs; it discovers devnotes
dynamically rather than a fixed list, so it stays correct as devnotes are
added. That script is for review/preview only — it deliberately does not mark
anything as "submitted" here, since drafts aren't real submissions. Marking a
row ☑ under "submitted" requires an actual `curvenote submit` run without
`--draft`, which is a real, curator-visible action — do that deliberately per
devnote, not as a batch script.

| Devnote (dir) | Myst Key | Author(s) | Notebooks run | Content reviewed | Submitted (real) | Draft/preview URL |
|---|---|---|---|---|---|---|
| 02_emitter_cell | nucleus-devnote-core-02_emitter_cell | Yen-Yu Hsu | ☐ | ☐ | ☐ | |
| 03_mthfs | nucleus-devnote-core-03_mthfs | Yemo Ku | ☐ | ☐ | ☐ | |
| 04_ppk | nucleus-devnote-core-04_ppk | Surendra Yadav | ☐ | ☐ | ☐ | |
| 05_pure_workshop | nucleus-devnote-core-09_pure-workshop | OnePot Workshop | ☐ | ☐ | ☐ | |
| 08_ppk_cell | nucleus-devnote-core-08_ppk-module-in-pure-cell | Yen-Yu Hsu | ☐ | ☐ | ☐ | |
| 09-cx43_cell | nucleus-devnote-core-cx43_01 | Yen-Yu Hsu | ☐ | ☐ | ☐ | https://scms.curvenote.com/build/019fc02a-19bf-784b-af8f-93f08fa3edc7 (draft) |
| 10-nucleus_cytosol_v05 | nucleus-devnote-core-NucelusPURE_deGFP | Surendra Yadav | ☐ | ☐ | ☐ | https://scms.curvenote.com/build/019fc02c-3e48-7812-8082-1f6b362b9632 (draft) |
| 11-Base_Cell | nucleus-devnote-core-Base_Cell | Surendra Yadav | ☐ | ☐ | ☐ | https://scms.curvenote.com/build/019fc02b-f140-7434-945e-365ae2323b0b (draft) |
| DNA-toolkit-T7-promoters | nucleus-devnote-core-dna-toolkit-promoter | Charlie Newell, Astrid Joergensen | ☐ | ☐ | ☐ | |
| bac-working-group | bac-working-group | Energy Metabolism Working Group | ☐ | ☐ | ☑ | https://scms.curvenote.com/build/019fc034-3f41-7bc8-b207-3cd4979b1aea (real submission) |
| cx43 | nucleus-devnote-core-01_contrib_cx43_cell | Ahmed Z. Sihorwala | ☐ | ☐ | ☐ | |
| devnote-developer_cell | nucleus-devnote-core-05_devcell_01 | Anton Jackson-Smith, Akshay Maheshwari | ☐ | ☐ | ☐ | |
| devnote-nucleus_onepot | nucleus-devnote-core-07_bnext-onepot-pure-replication | Anton Molina, Anton Jackson-Smith | ☐ | ☐ | ☐ | https://scms.curvenote.com/build/019fc029-64f5-73ce-b2f5-0a8ab298fc78 (draft) |
| fwm-aria-d2 | 019f6db2-e060-710d-8984-6bcd5747d775 | b.next, Find What Matters | ☐ | ☐ | ☐ | https://scms.curvenote.com/build/019fc029-bd16-7c3d-8825-90835da5c5b9 (draft) |
| fwm-batch-bo | 019f9b60-cc79-7008-9c25-4a46b53b8604 | Joseph Lozier | ☐ | ☐ | ☐ | |
| lipid-prep | 019dcea0-91e3-78da-be6d-6450c2ff8308 | London Exchange Meeting Participants | ☐ | ☐ | ☐ | |
| module-Clpxp | nucleus-devnote-core-06_clpxp_module_01 | Yen-Yu Hsu | ☐ | ☐ | ☐ | https://scms.curvenote.com/build/019fc02e-f178-7ad8-af75-1575d8adb1fd (draft) |
| module-Clpxp-Cytosol | nucleus-devnote-core-clpxp_module_cytosol-01 | Yen-Yu Hsu | ☐ | ☐ | ☐ | https://scms.curvenote.com/build/019fc02b-a5b5-7f3c-8f26-dccb332a376c (draft) |
| onepot-sy | onepot-sy | Surendra Yadav | ☐ | ☐ | ☑ | https://scms.curvenote.com/build/019fc034-5ab6-7f11-948f-9e5c6e096f02 (real submission) |

**Note on `bac-working-group`/`onepot-sy`:** these are the only two rows with a real, non-draft submission on file — made while testing whether the CLI path worked at all, not a mistake to undo. Every other row's URL (where present) is a draft/preview build only and does NOT count as submitted.

**Note on `module-Clpxp`/`module-Clpxp-Cytosol`/`11-Base_Cell`/`10-nucleus_cytosol_v05`:** these draft URLs were built from the `fix-typst-seqviz-plugins` branch (PR #9, not yet merged), which fixes real typst-compile and seqviz bugs in these four — the draft link reflects the fixed version, not what's currently on `main`.

**Known non-transient issue found during this pass:** `bac-working-group`'s only author, "Energy Metabolism Working Group," has no `email` field in `curvenote.yml` — `curvenote check` fails this specific rule every time (`No authors provided an email`). Not something to guess at; needs a real contact from whoever owns that devnote before "content reviewed" can be meaningfully checked off for it.

## Data-quality flags from `sy-devnotes-download/` audit

- **Duplicate/near-empty directories**: `trial/`, `pla1/`, `cytosol-lifetime/` are completely empty (no files, no `curvenote.yml`) despite matching names of real devnotes already accounted for elsewhere (`pla1` and `cytosol-lifetime` both appear — with actual content — in `devnotes-downloaded/`). `devnote-template/` is also near-empty after bloat removal — its lone surviving `main.md` is an unfinished draft stub of the MTHFS story (title matches `devnote-test/`'s real content, but body says "Abstract TODO" / "Caption TODO" placeholders), and it has no `curvenote.yml`. None of these four contribute real content.
- **Base_Cell data**: `sy-devnotes-download/Base_Cell/` shares its Myst Key with the already-staged `core/11-Base_Cell` and carries two large raw liposome-imaging CSVs (1.6G + 702M) under an experiment folder (`20251119-nucleus-liposomes`) not referenced in its own `curvenote.yml` toc. These files are individually far over GitHub's ~100MB hard per-file push limit — they cannot be committed as plain files; need Git LFS or external storage (S3) before they can go in this repo. See memory `github-file-size-limits.md`.
- **Myst Key collision cluster (4-way)**: `b6272c31-dae6-4c60-bf48-a86466349d86` is shared by the placeholder stub `devnotes-downloaded/devcells-chicago-node/devnote-template`, plus three real-content dirs in `sy-devnotes-download/` — `pHtdGFP and trigger ssDNA in Cytosol/`, `PPK Planning DevNote/`, and `kickoff/kickoff-experimental/` (the last is the real, finished "DevCells: Kickoff Workshop," superseding the placeholder). Each needs a distinct fresh key before migration.
- **Author mismatch**: `sy-devnotes-download/devnote-test/` contains the MTHFS story (matches already-staged `core/03_mthfs`, credited there to Yemo Ku) but lists its author as Surendra Yadav — unresolved discrepancy.
