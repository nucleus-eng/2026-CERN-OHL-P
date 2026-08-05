> **How to migrate a DevNote:** see [`MIGRATION-PLAYBOOK.md`](./MIGRATION-PLAYBOOK.md)
> for the end-to-end procedure (enumerate → recover from MECA → de-bloat →
> pin the CDK → execute → submit) and the catalogue of known snags.
>
> Note this table is **not** a complete work list — enumerate from the venue
> site instead. As of 2026-08-05 three published DevNotes were missing from it
> entirely; see the playbook's §1.

| Title | Author | Myst Key | Collection | Status |
|---|---|---|---|---|
| IV-HSL Emitter Cell | Yen-Yu Hsu | nucleus-devnote-core-02_emitter_cell | | staged — see Manual review checklist below (devnotes/02_emitter_cell) |
| MTHFS - an Unexpected Enzyme in PURE | Yemo Ku | nucleus-devnote-core-03_mthfs | Core | staged, notebook passes (fixed this session) — see Manual review checklist below (devnotes/03_mthfs) |
| PPK Module testing in PURE | Surendra Yadav | nucleus-devnote-core-04_ppk | Core | staged, notebooks pass (3 fixed this session) — see Manual review checklist below (devnotes/04_ppk) |
| Nucleus OnePot PURE workshop | OnePot Workshop | nucleus-devnote-core-09_pure-workshop | Workshops and Courses | staged, notebooks pass (1 fixed this session) — see Manual review checklist below (devnotes/05_pure_workshop) |
| Integrating PPK Module in PURE Cells | Yen-Yu Hsu | nucleus-devnote-core-08_ppk-module-in-pure-cell | Core | staged, notebook passes (fixed this session) — see Manual review checklist below (devnotes/08_ppk_cell) |
| Cx43 Cell: DNA Validation | Yen-Yu Hsu | nucleus-devnote-core-cx43_01 | Core | staged, notebooks pass — see Manual review checklist below (devnotes/09-cx43_cell) |
| First Nucleus Cytosol Testing | Surendra Yadav | nucleus-devnote-core-NucelusPURE_deGFP | Core | staged, notebooks pass — see Manual review checklist below (devnotes/10-nucleus_cytosol_v05) |
| Nucleus Base Cell Testing | Surendra Yadav | nucleus-devnote-core-Base_Cell | Core | staged — see Manual review checklist below (devnotes/11-Base_Cell) |
| ClpXP Control Module: Deployment in Nucleus Cytosol | Yen-Yu Hsu | 019f05c8-f7ea-74d8-ab37-a6e418627268 | Core | TODO |
| Characterizing the Limited Operational Lifetime of Cytosol Reactions | Surendra Yadav | 019ed70b-0af7-7dd0-aefe-688ebf933399 | Core | TODO |
| SecYEG-Based Membrane Translation Module in Synthetic Cells | Yen-Yu Hsu | 019e896a-6e0d-76d5-99ef-2df38c5ebd7f | Core | TODO |
| Using platemaps to analyze and share data | Jay Bhasin | 019d6e3a-c618-77bc-853c-fe4694511f53 | Core | TODO |
| Intro to Kinetics Analysis of Plate Reader Experiments | Sharon Newman | 019db3ce-4971-7fd6-83c0-c1a15e780bbe | Core | staged, notebook passes (recovered from MECA, CDK pin added — issue #17) — see Manual review checklist below (devnotes/2026-newman-kinetics-intro) |
| Nucleus OnePot PURE | Surendra Yadav | onepot-sy | Core | staged, notebooks pass (fixed this session), real submission on file — see Manual review checklist below (devnotes/onepot-sy) |
| ClpXP Control Module: Deployment in PURE Cells | Yen-Yu Hsu | nucleus-devnote-core-clpxp_module_cells-01 | Core | staged, notebooks pass (recovered from MECA, CDK pin added — issue #18) — see Manual review checklist below (devnotes/module-Clpxp-Cells) |
| ClpXP Control Module: Deployment in PURE | Yen-Yu Hsu | nucleus-devnote-core-clpxp_module_cytosol-01 | Core | staged, notebooks pass — see Manual review checklist below (devnotes/module-Clpxp-Cytosol) |
| DNA toolkit - The T7 promoter collection | Charlie Newell, Astrid Joergensen | nucleus-devnote-core-dna-toolkit-promoter | Core | staged, notebooks pass — see Manual review checklist below (devnotes/DNA-toolkit-T7-promoters) |
| Nucleus OnePot PURE Replication | Anton Molina, Anton Jackson-Smith | nucleus-devnote-core-07_bnext-onepot-pure-replication | Core | staged, notebook passes — see Manual review checklist below (devnotes/devnote-nucleus_onepot) |
| The Developer Cell Control Module: Protein Degradation by ClpXP | Yen-Yu Hsu | nucleus-devnote-core-06_clpxp_module_01 | Core | staged — see Manual review checklist below (devnotes/module-Clpxp) |
| Developer Cell: Project Introduction | Anton Jackson-Smith, Akshay Maheshwari | nucleus-devnote-core-05_devcell_01 | Core | staged — see Manual review checklist below (devnotes/devnote-developer_cell) |
| Liposome encapsulation: A tractable and reproducible approach | Chris Falcon, Katie Drew | 9e302e31-3dbb-494a-b8e3-5fc6d91ea941 | Workshops and Courses | TODO |
| Synthetic Cells Course Lab Manual: Cell-free Gene Expression and Liposome Encapsulation | Javin P Oza | 118a7ada-92d1-448f-adc2-f19c2da16b16 | Workshops and Courses | TODO |
| DevCells: Kickoff Workshop | DevCells Kickoff Workshop | b6272c31-dae6-4c60-bf48-a86466349d86 | Workshops and Courses | TODO |
| Tunable protein expression strength with toehold exchange riboregulators | Samuel Schaffter, Fernanda Piorino, Eugenia Romantseva | 7b6aaa00-7351-4a7e-ba45-ade3f7332335 | Community | TODO |
| DNA toolkit - The T7 terminator collection | Charlie Newell | cn-05272026-terminators | Community | TODO |
| Energy Metabolism Working Group at Build-a-Cell #15 | Energy Metabolism Working Group | bac-working-group | Community | staged, real submission on file, author missing email — see Manual review checklist below (devnotes/bac-working-group) |
| London Exchange Meeting: Liposome Protocol Survey | London Exchange Meeting Participants | 019dcea0-91e3-78da-be6d-6450c2ff8308 | Community | staged — see Manual review checklist below (devnotes/lipid-prep) |
| Cx43 Cell | Ahmed Z. Sihorwala | nucleus-devnote-core-01_contrib_cx43_cell | Community | staged — see Manual review checklist below (devnotes/cx43) |

## Remaining TODO rows (2) — likely require contacting original authors

**Update:** Anton's work on this branch (flat `devnotes/` restructure, commits `578ea19`..`8370dd9`) staged real, committed content for 7 of the previous 9 "genuinely missing" rows directly into `devnotes/` — not just found in a bulk download, but full devnote directories with `curvenote.yml`/`main.md`/notebooks matching the tracked Myst Key exactly. Verified by grep: no trace of the remaining 2 titles/authors anywhere in `devnotes/`, `devnotes-downloaded/`, or `sy-devnotes-download/`. Only two rows still need outreach to the original authors — "Liposome encapsulation: A tractable and reproducible approach" (Chris Falcon, Katie Drew) and "Synthetic Cells Course Lab Manual: Cell-free Gene Expression and Liposome Encapsulation" (Javin P Oza), both `Workshops and Courses` — see rows 23-24 in the table above for their Myst Keys.

Note: the two rows above (`onepot-sy`, `bac-working-group`) were previously "found (sy-devnotes-download/...), not staged"; both have since been staged into `devnotes/onepot-sy` and `devnotes/bac-working-group` (Step 1 of the migration plan), excluding `onepot-sy`'s `plasmids/PURE_plasmids.tar.gz` DNA archive, which is handled by a separate DNA-reconciliation workstream. Also new on this branch, outside the original tracker scope: `devnotes/fwm-aria-d2` (ARIA/IGOR optimization) and `devnotes/fwm-batch-bo` (Batch Bayesian Optimization) — new devnotes, not migrations of tracked TODO rows.

## Manual review checklist (all 21 devnotes currently in `devnotes/`)

**Status as of 2026-08-04: the first 19 devnotes submitted for real** (`curvenote submit` without `--draft`) — each row's URL below is the real, curator-visible submission build, ready for per-devnote curator review/approval. The **two rows added 2026-08-05** (`2026-newman-kinetics-intro`, `module-Clpxp-Cells`) are not submitted yet and still need a content review — see "Issues #17/#18" below.

Three review steps per devnote, each its own column: **notebooks run** (have the
notebooks actually been executed/re-executed and outputs checked), **content
reviewed** (has a human actually read `main.md` end to end — done for the
first 19, not yet for the 2 added on 2026-08-05), **submitted** (a REAL,
non-draft `curvenote submit` — an editor can't act on a draft, so a draft
build does not count as submitted here; the first
19 rows below are checked, see build URL column). URL is the real
submission's `https://scms.curvenote.com/build/...` build-report link.

Run `./manual-submit-all.sh` (repo root) to (re-)submit **drafts** for every
devnote in one pass and get fresh preview URLs; it discovers devnotes
dynamically rather than a fixed list, so it stays correct as devnotes are
added. That script is for review/preview only — it deliberately does not mark
anything as "submitted" here, since drafts aren't real submissions. Marking a
row ☑ under "submitted" requires an actual `curvenote submit` run without
`--draft`, which is a real, curator-visible action — do that deliberately per
devnote, not as a batch script.

| Devnote (dir) | Myst Key | Author(s) | Notebooks run | Content reviewed | Submitted (real) | Build URL |
|---|---|---|---|---|---|---|
| 02_emitter_cell | nucleus-devnote-core-02_emitter_cell | Yen-Yu Hsu | n/a (no toc notebooks; 1 orphaned main.ipynb, no environment.yml either) | ☑ | ☑ | https://scms.curvenote.com/build/019fcdbe-5745-7f49-a3f6-68ef77450817 |
| 03_mthfs | nucleus-devnote-core-03_mthfs | Yemo Ku | ☑ pass (1/1) | ☑ | ☑ | https://scms.curvenote.com/build/019fcdbd-7ece-7503-9897-c802441245ce |
| 04_ppk | nucleus-devnote-core-04_ppk | Surendra Yadav | ☑ pass (5/5) | ☑ | ☑ | https://scms.curvenote.com/build/019fcdbd-84b4-7d12-9a9a-d4a101f3ff0b |
| 05_pure_workshop | nucleus-devnote-core-09_pure-workshop | OnePot Workshop | ☑ pass (5/5) | ☑ | ☑ | https://scms.curvenote.com/build/019fcdbd-8559-7af4-b014-96363dd453b1 |
| 08_ppk_cell | nucleus-devnote-core-08_ppk-module-in-pure-cell | Yen-Yu Hsu | ☑ pass (1/1) | ☑ | ☑ | https://scms.curvenote.com/build/019fcdbd-9fa1-70f6-8b2e-435401361614 |
| 09-cx43_cell | nucleus-devnote-core-cx43_01 | Yen-Yu Hsu | ☑ pass (2/2) | ☑ | ☑ | https://scms.curvenote.com/build/019fcdbe-5ef0-7026-9610-99264e36e02a |
| 10-nucleus_cytosol_v05 | nucleus-devnote-core-NucelusPURE_deGFP | Surendra Yadav | ☑ pass (2/2) | ☑ | ☑ | https://scms.curvenote.com/build/019fcdbd-c96c-7e3b-815d-b4c130a2f023 |
| 11-Base_Cell | nucleus-devnote-core-Base_Cell | Surendra Yadav | n/a (no toc notebooks) | ☑ | ☑ | https://scms.curvenote.com/build/019fcdbd-8c20-7b08-bea8-967b2ea23099 |
| DNA-toolkit-T7-promoters | nucleus-devnote-core-dna-toolkit-promoter | Charlie Newell, Astrid Joergensen | ☑ pass (2/2) | ☑ | ☑ | https://scms.curvenote.com/build/019fcdbe-6e19-7f44-a94f-2b18457e0f19 |
| bac-working-group | bac-working-group | Energy Metabolism Working Group | n/a (no toc notebooks) | ☑ | ☑ | https://scms.curvenote.com/build/019fcdbd-d5e0-7602-bfb7-f1c75b3b30e1 |
| cx43 | nucleus-devnote-core-01_contrib_cx43_cell | Ahmed Z. Sihorwala | n/a (no toc notebooks) | ☑ | ☑ | https://scms.curvenote.com/build/019fcdbd-a991-7f87-9dce-bdd7f07c9395 |
| devnote-developer_cell | nucleus-devnote-core-05_devcell_01 | Anton Jackson-Smith, Akshay Maheshwari | n/a (no toc notebooks) | ☑ | ☑ | https://scms.curvenote.com/build/019fcdc0-dfe4-7002-828e-29b43c285245 |
| devnote-nucleus_onepot | nucleus-devnote-core-07_bnext-onepot-pure-replication | Anton Molina, Anton Jackson-Smith | ☑ pass (1/1) | ☑ | ☑ | https://scms.curvenote.com/build/019fcdbd-e4b6-7227-a6c7-c3ce474e1284 |
| fwm-aria-d2 | 019f6db2-e060-710d-8984-6bcd5747d775 | b.next, Find What Matters | n/a (no toc notebooks) | ☑ | ☑ | https://scms.curvenote.com/build/019fcdbe-363a-77c5-936a-17af2178ef46 |
| fwm-batch-bo | 019f9b60-cc79-7008-9c25-4a46b53b8604 | Joseph Lozier | n/a (no toc notebooks) | ☑ | ☑ | https://scms.curvenote.com/build/019fcdbe-1b37-7658-8b35-e8be01ca926f |
| lipid-prep | 019dcea0-91e3-78da-be6d-6450c2ff8308 | London Exchange Meeting Participants | n/a (no toc notebooks) | ☑ | ☑ | https://scms.curvenote.com/build/019fcdbd-7f13-7cc3-b358-c42e0c6c3bcd |
| module-Clpxp | nucleus-devnote-core-06_clpxp_module_01 | Yen-Yu Hsu | n/a (no toc notebooks) | ☑ | ☑ | https://scms.curvenote.com/build/019fcdc0-9407-7fae-986e-2fefa44eb448 |
| module-Clpxp-Cytosol | nucleus-devnote-core-clpxp_module_cytosol-01 | Yen-Yu Hsu | ☑ pass (6/6) | ☑ | ☑ | https://scms.curvenote.com/build/019fcdbd-8698-7638-9941-ae1285b2a831 |
| onepot-sy | onepot-sy | Surendra Yadav | ☑ pass (3/3) | ☑ | ☑ | https://scms.curvenote.com/build/019fcdbd-9f01-7488-839f-1c0979c0a693 |
| 2026-newman-kinetics-intro | 019db3ce-4971-7fd6-83c0-c1a15e780bbe | Sharon Newman | ☑ pass (1/1) | ☐ | ☐ (draft only) | https://scms.curvenote.com/build/019fd305-03a4-71fa-9e74-686b8f283f23 |
| module-Clpxp-Cells | nucleus-devnote-core-clpxp_module_cells-01 | Yen-Yu Hsu | ☑ pass (5/5, incl. 1 orphan) | ☐ | ☐ (draft only) | https://scms.curvenote.com/build/019fd304-b1cc-729d-8570-fd9b5c6b8cf4 |

**Note on `bac-working-group`/`onepot-sy`:** each previously had an *older* real, non-draft submission on file from early testing of whether the CLI path worked at all. Both have now been superseded by the real submission above (2026-08-04), which reflects this session's fixes.

**All 19 real submissions above came from `migrate/debug-and-review` (PR #13, superseding the stale PR #10, itself stacked on the fix-typst-seqviz-plugins/PR #9 commit, not yet merged)** — so every row reflects the notebook fixes from the 2026-08-03/04 sessions (`module-Clpxp`/`module-Clpxp-Cytosol`/`11-Base_Cell`/`10-nucleus_cytosol_v05` also still carry the earlier PR #9 fixes), not what's currently on `main`. `./manual-submit-all.sh` now supports both modes: `--draft` (default, or explicit) for review/preview, `--final` (or `MODE=final`) for a real, curator-visible submission — both run all devnotes concurrently (`xargs -P`, default 6, override with `CONCURRENCY=n`). Ran `CONCURRENCY=19 ./manual-submit-all.sh --final` on 2026-08-04 (all 19 launched at once); 17/19 succeeded on the first pass, 2 (`module-Clpxp`, `devnote-developer_cell`) hit a transient `api.curvenote.com` login timeout under load and were retried individually — all 19 are now submitted for real. Each devnote's submission is now awaiting individual curator review/approval.

### First full notebook-execution sweep (2026-08-01 session)

Ran every `toc`-listed notebook via `nbclient`, in a shared conda env (`environment.yml` is byte-identical across all 18 devnotes that have one — `02_emitter_cell` has none) with `nucleus-cdk==0.5.0rc2` installed (matches the pinned version in every notebook's install cell). "Notebooks run" above reflects this pass; devnotes with no notebooks in their `toc` are marked n/a (this doesn't mean they have zero risk — see the orphaned-notebook audit note below).

**Original sweep result: 19 pass / 9 fail across 28 notebooks** (every notebook listed in a `toc:` across all 19 devnotes; 6 devnotes have zero `toc`-listed notebooks, marked n/a above — that's a gap in coverage, not a pass). **Update: all 9 failures were debugged and fixed in a follow-up session — see "Notebook fixes" below. Current state: 28 pass / 0 fail.**

Of those 9, 3 turned out to be genuine upstream `nucleus-cdk` bugs (not fixable from the notebook side alone) and were filed against the real source repo, `bnext-bio/bnext`:

| Devnote | Notebook | Error | Issue |
|---|---|---|---|
| 03_mthfs | `20250220-analysis.ipynb` | `pr.plot_kinetics`: `ax.axvline` compares a `pandas.Timedelta` against a float axis limit | [bnext-bio/bnext#66](https://github.com/bnext-bio/bnext/issues/66) |
| 08_ppk_cell | `20250811-acjs-PPK.ipynb` | `pr.plot_steadystate`/`hue`/`col` regression: an earlier version merged the full platemap back in before plotting, a later commit removed that with no replacement | [bnext-bio/bnext#67](https://github.com/bnext-bio/bnext/issues/67) |
| 04_ppk | `20250613-PPK_Mg_Opt.ipynb` | `pr.plot_curves`: `data.READ_COLUMN_NAME` instead of `data[READ_COLUMN_NAME]` — already fixed on `bnext-bio/bnext`'s `main`, published `nucleus-cdk==0.5.0rc2` pip package is just stale | [bnext-bio/bnext#69](https://github.com/bnext-bio/bnext/issues/69) |

The other 6 failures were notebook-side bugs (typos, degenerate wells, stale variable references) — see "Notebook fixes" below for the full list and fixes.

### Notebook fixes (2026-08-03 session)

All 9 originally-failing notebooks were debugged live (in the `devnote-notebooks` conda env, actually re-executing each — not inferred from static reading) and fixed. Every fix is notebook-side only; nothing in `nucleus-cdk` was edited. Two genuine upstream `nucleus-cdk` bugs were found and could not be fixed from the notebook side at all — those cells were commented out with a note, and issues filed against the real source repo (`bnext-bio/bnext`, not `bnext-bio/nucleus`, which is a stale mirror — see memory `nucleus-cdk-source-repo`):

- **`onepot-sy` (3 notebooks):** `ctrl_name='10 uM HPTS'` didn't match any well in any of the 3 experiments' platemaps (boilerplate copied from a different devnote template) — no HPTS/fluorescein control was actually run. Fixed by skipping `normalize_data_to_controls` entirely and using raw data, per-notebook. (Worth noting: 2 of the 3 notebooks had previously "succeeded" by silently normalizing against a zero-row match, producing bogus data — not just the 1 that visibly crashed.)
- **`04_ppk/20250612-analysis.ipynb`:** well A23 (`CP + PolyP + 8 mM Mg`, replicate 3/3) fit to `k≈0` (degenerate), crashing the lag-time calculation. Fixed by excluding that one well (kept its 2 sibling replicates). Also had an independent `MergeError` (steady-state result no longer carries a `Well` column when merged the old way) — fixed by regrouping with `group_by=["Well","Read"]` and flattening columns before merge.
- **`04_ppk/20250611-analysis.ipynb`:** same `MergeError` pattern as above (no degenerate well in this dataset) — same fix.
- **`04_ppk/20250613-PPK_Mg_Opt.ipynb`:** real `nucleus-cdk` bug in `plot_curves` (a warning-message typo, `data.READ_COLUMN_NAME` instead of `data[READ_COLUMN_NAME]`), triggered because this dataset has 2 distinct `Read` gain settings and the call didn't split by `Read`. Fixed notebook-side by passing `col="Read"` explicitly (also the semantically correct plot). Already fixed on `bnext-bio/bnext`'s `main` branch — the published `nucleus-cdk==0.5.0rc2` pip package is just stale. Filed as [bnext-bio/bnext#69](https://github.com/bnext-bio/bnext/issues/69) for tracking/visibility on cutting a new release.
- **`05_pure_workshop/nucleus-pure-protein-debug.ipynb`:** same degenerate-well pattern as `04_ppk` (well D5, `OP -`, replicate 3/3) — excluded that well, plus excluded `Type=="Standard"` (a `plamGFP` calibration curve, not a live reaction — sigmoid kinetics isn't meaningful there and several of those wells were also degenerate). This notebook additionally had unrelated pre-existing bugs (an undefined-variable typo — `data_drop_ctrl` vs. the actual `data_drop_ctrl_0` — across 5 cells, and 2 names in a later cell, `data_list_concat`/`ordered_dict`, that were never defined anywhere) — all fixed.
- **`03_mthfs/20250220-analysis.ipynb`:** cell 8 computed kinetics on the filtered `data_drop` frame then discarded it; cell 9 recomputed on the raw, unfiltered `data` instead. Fixed to use `data_drop` consistently. Separately, `pr.plot_kinetics(data, kinetics)` also has an upstream bug (`ax.axvline` compares a `pandas.Timedelta` against a float axis limit) that no notebook-side argument combination avoids — commented out, filed as [bnext-bio/bnext#66](https://github.com/bnext-bio/bnext/issues/66).
- **`08_ppk_cell/20250811-acjs-PPK.ipynb`:** 11 cells called `pr.plot_steadystate(data, x=A, hue=B, ...)` with `B != A` — confirmed via git history to be a real upstream regression (an earlier `nucleus-cdk` version merged the full platemap back in before plotting, so `hue`/`col` could reference any column; a later commit commented that merge out with no replacement). No notebook-side fix exists; commented out all 11, filed as [bnext-bio/bnext#67](https://github.com/bnext-bio/bnext/issues/67). Separately, `pr.find_steady_state(data, group_by="Well")` passed a bare string where a list was expected (a real notebook-side typo) — fixed to `group_by=["Well"]`.

The draft/preview build URLs in the checklist table above have since been refreshed via `./manual-submit-all.sh` and reflect these fixes (see the note above the sweep table).

### Second debugging session (2026-08-04): stale outputs, seqviz, and per-devnote polish

This session started from a puzzling report: bugs already fixed and committed in the 2026-08-03 session (above) were still visibly showing up in fresh draft submissions. Root cause (commit `d3efa0e`): `curvenote submit` never re-executes a notebook — it only renders whatever cell outputs are already saved in the `.ipynb` file. The 2026-08-03 fix commit corrected the notebook *code*, but its own `git checkout -- devnotes/` cleanup step (used to discard the unrelated PNG diffs from a live debugging run) also discarded the newly-passing *execution outputs*, leaving the old pre-fix error tracebacks baked into the committed files. Fixed by re-executing all 28 `toc`-listed notebooks across every devnote and committing the refreshed outputs — confirmed via `git status` that all 28 files changed (i.e. every one had genuinely stale output, not just the one that was visibly reported).

Other fixes made in this session, each its own commit:
- **`onepot-sy/20260121-Analysis.ipynb` kernelspec** (`d3efa0e`): pointed at a never-registered custom kernel (`bnext-cdk`) unlike its sibling notebooks; switched to the standard `python3` kernel.
- **`manual-submit-all.sh` parallelized** (`d3efa0e`): now submits all devnotes concurrently via `xargs -P` (default 6, override with `CONCURRENCY=n`) instead of one at a time.
- **Stray per-devnote PDF exports** (`711d3ea`): `curvenote submit` drops an untracked PDF export into each devnote's own directory per its `curvenote.yml` `exports:` config (e.g. `bnext-ppk.pdf`, `devnote.pdf`). Deleted the accumulated ones; a permanent fix (disable the export, or have the script clean up after itself) is deferred — see memory `manual-submit-generates-stray-pdfs`.
- **`10-nucleus_cytosol_v05` seqviz plugin failure** (`871e92c`): the pOpen-deGFP plasmid-map tab showed "seqviz - Unknown Directive" / `ERR_MODULE_NOT_FOUND: seqparse`. This branch forked before PR #9 (`fix-typst-seqviz-plugins`)'s seqviz fix landed and was never rebased onto or merged with it. Cherry-picked that fix (`eb74b0d`): moves the plugin + its npm dependency into a shared `plugins/seqviz/` at the repo root with `node_modules` committed (CI never runs `npm install` for a devnote's own `package.json`), removes `11-Base_Cell`'s dead unused plugin declaration, and renames 6 space-containing figure labels in `module-Clpxp{,-Cytosol}` that broke the Typst compile step (Typst labels can't contain spaces), plus fixes one pre-existing case-mismatch dangling reference. Verified locally: plugin now loads, plasmid map renders.
- **`_build/` leaking untracked in `10-nucleus_cytosol_v05`** (`573e30d`): its devnote-local `.gitignore` was the only one of 19 missing the standard `_build/`/`.ipynb_checkpoints/`/`.DS_Store`/`node_modules/` entries (each devnote's `.gitignore` was carried over as-is from before the flat-restructure, from whatever template it started with — not corruption, just an inconsistent starting point). Brought it in line with its siblings and added a repo-wide `_build/` backstop rule.
- **`module-Clpxp`/`module-Clpxp-Cytosol` tab-set formatting** (`f16711e`, `08052bd`): wrapped DNA-Constructs/Purified-Proteins tables, the per-experiment protocol tables (Experiment 1–8 in `module-Clpxp`; 1–6 in `module-Clpxp-Cytosol`, converted from `{tip}` dropdown toggles), and three figure pairs in `module-Clpxp` (Figs 2/3, 4/5, 6/7) into MyST `tab-set`s. Structural only, no prose changed; also fixed a pre-existing bug where `module-Clpxp`'s "Experiment 4" heading was misplaced inside its table fence.
- **`onepot-sy` blank Figure 4 + embed conversion** (`d555f12`): `summary_plot.png` was silently blank. Root cause: `pr.plot_summary()` calls `plt.show()` internally, which closes the figure in Jupyter's inline backend — so the notebook's own subsequent `plt.savefig("summary_plot.png")` saved a brand-new *empty* figure (confirmed live: `plt.gcf()` had 0 axes at save time). Fixed by converting `main.md` to embed all four data-plot figures directly from their source notebook cells (`#fig:kinetics-opt1`, `#fig:kinetics-opt2`, `#fig:opt2_summary`, `#fig:kinetics-opt4`) instead of separately-saved PNGs — a pattern already established elsewhere in this repo (`03_mthfs`, `04_ppk`, etc.) that sidesteps this failure mode entirely. The plate-layout photo (`fig:OnePotPURE-platemap`) is a real static image, not notebook-derived, and stays as one. Deleted the now-orphaned `g.png`/`summary_plot.png`/`summary-normalized.png` files.

All of the above are on `migrate/debug-and-review`, not yet merged to `main`.

### Issues #17/#18: two unmigrated devnotes recovered from MECA (2026-08-05 session)

Anton filed two bugs against devnotes that were live but **not in this repo** —
both were still `TODO` rows in the table above, so nothing in `devnotes/` could
fix them:

- **[#17]** `Newman-20260421` — `experiments/kinetics-intro.ipynb` had **no
  install cell at all**, so Curvenote live compute raised
  `ModuleNotFoundError: No module named 'cdk'`.
- **[#18]** `bnext-devnotes-clpxp-pure-cells-01` — 4 notebooks on the unpinned
  `!pip install nucleus-cdk | tail -n2`.

**Source recovery.** Neither devnote exists in this repo,
`bnext-bio/nucleus-developer-notes`, or any other org repo. Both were recovered
from their Curvenote computational archives (MECA zips linked off the live
article pages). The Myst keys in those bundles match the tracker exactly, so
submitting from here updates the existing works rather than creating duplicates.

**Why the pin is `0.5.0rc2` and not `0.6.0rc2`.** Unpinned `pip install
nucleus-cdk` now resolves to **0.5.3**, not the rc these notebooks were written
against. And **0.6.x deleted `cdk/analysis/cytosol/platereader.py`** (moved to
`cdk/instruments/platereader/legacy/`), which every notebook in both devnotes
imports — so 0.6.x breaks them outright. Verified by test: `nucleus-cdk==0.5.0rc2`
installs clean on Python 3.14 (the live-compute Python) with all 14 deps, so the
`--no-deps` workaround used by `2026-garenne-pH-sensor` is **not** needed here —
that exists only because 0.6.x declares `pyarrow>=18,<19`, which has no cp314
wheels.

Every `toc` notebook in both devnotes now opens with:

```python
!pip install nucleus-cdk==0.5.0rc2 | tail -n2

# Surface a failed install here, rather than as a confusing ModuleNotFoundError
# in the import cell below.
import importlib.metadata as md
assert md.version("nucleus-cdk") == "0.5.0rc2", f"got {md.version('nucleus-cdk')}"
```

The assert is the pH-sensor devnote's pattern: `| tail -n2` hides a failed
install, so without it the real error surfaces later as a confusing
`ModuleNotFoundError`.

Other fixes needed to make the recovered bundles build:

- **Vendored CDK stripped** (`module-Clpxp-Cells`): the bundle shipped a whole
  `src/cdk/` copy, two 52 KB copies of `platereader.py`, and committed
  `__pycache__`. `20250930-analysis.ipynb` was importing the local copy
  (`import platereader as pr`) — repointed at the packaged
  `from cdk.analysis.cytosol import platereader as pr`, matching its siblings.
- **Typst compile failure** (`module-Clpxp-Cells`): `:name: fig:ClpX S`
  contained a space (Typst labels can't), and the one reference to it,
  `{ref}`fig:ClpX s``, also had the wrong case. Exactly the PR #9 bug class.
  Renamed to `fig:ClpX-S`; `devnote.pdf` now renders.
- **Dangling plasmid download** (`module-Clpxp-Cells`): `curvenote.yml`
  referenced `general/clpxp-module-plasmids-01.zip`; the real file is
  `general/Plasmids.zip`.
- **MECA-dropped assets**: neither bundle carried `banner*.webp` or `lorem.mjs`
  (both referenced in `curvenote.yml`) — restored from a sibling, where they are
  byte-identical across all devnotes. Newman's bundle also had `extends:
  base.yml` with no `base.yml` present (removed) and a stale `thebe: binder:`
  block pointing at the old repo (replaced with `jupyter: true`, matching the 15
  other devnotes that use live compute).
- **Newman thumbnail**: `assets/thumbnail.png` is *generated* by the notebook
  (`plt.savefig("../assets/thumbnail.png")`), and the missing `assets/` directory
  was making the notebook fail. Created the directory; verified the produced PNG
  is a real kinetic fit and not blank (the `plt.show()`-closes-the-figure trap
  that silently blanked `onepot-sy`'s Figure 4).
- **`20251211-analysis-cytation5.ipynb`** (orphan, not in `toc`): failed on
  `normalize_data_to_controls(ctrl_name='10 uM HPTS')` — the same
  copied-boilerplate bug as `onepot-sy`, where no HPTS control was ever run and
  `ctrl_name` matched zero wells. Its published sibling (Cytation 3) has no
  normalization step at all, so the call was commented out with a note.
- **Resource globs** trimmed in both `curvenote.yml`s to the directories that
  actually exist after staging (the `src/**/*` and `experimental/**/*` entries
  pointed at nothing).

**Notebook execution note.** All 6 notebooks were executed and their outputs
committed. Worth recording the near-miss: the first execution pass forced
`MPLBACKEND=Agg`, which made every notebook pass while saving **zero** figures —
`curvenote submit` renders saved outputs, so that would have published
figure-less devnotes. Caught by diffing PNG-output counts against the original
MECA bundles; re-run without `MPLBACKEND` (ipykernel's default
`matplotlib_inline` backend is what captures figures). Always compare figure
counts before and after a re-execution sweep.

**"Created a new work" on local draft submits — not a bug, and not specific to
these two devnotes.** Draft-submitting `module-Clpxp-Cells` from a personal
`curvenote token` reported `Created a new work` rather than
`Created a new work version`, which looked like it was making a duplicate.
Diagnosed by draft-submitting two devnotes already merged to `main`:
`module-Clpxp-Cytosol` (string key) and `lipid-prep` (UUID key) — **both also
report `Created a new work`**, so the key format is not the cause. The one
devnote that updated in place, `2026-newman-kinetics-intro`, is also the only
one of the three that appears in `curvenote submission list` for this account.

So work resolution is scoped to the submitting account: a local `curvenote
submit` under a personal token cannot see, and therefore cannot update, works
owned by someone else. The real publish path is CI — `submit.yml` runs on push
to `main` using the venue-level `secrets.CURVENOTE_TOKEN`, which is what
resolves these works correctly. Verify the correct key was matched by checking
`work.date_created` in `_build/logs/curvenote.submit.json`: an existing work
shows its original creation date, a duplicate shows today's.

Practical consequence: **use local drafts for build/QA only, and let the merge
to `main` do the real submission.** Drafts do not reach the editor panel and do
not create venue submissions (`curvenote submission list` shows no entry for
either draft above), so extra draft works are harmless.

**Known pre-existing issues, not fixed here** (both predate this work and are
visible on the live pages):

- `kinetics-intro.ipynb`'s own table-of-contents anchors (`#setup`,
  `#load-data`, `#plot-curves`, `#normalize`, `#kinetic-analysis`, `#summary`)
  do not resolve — the headings have no matching MyST targets. Left alone
  because fixing it means editing collaborator content beyond a URL.
- `main.md` in the Newman devnote links to
  `https://github.com/bnext-bio/bnext/tree/main/cdk/src/cdk/analysis/cytosol`,
  which 404s for `curvenote check` because `bnext-bio/bnext` is private.
- Three `module-Clpxp-Cells` figures are >3 MB PNGs, which makes the webp
  conversion slow at build time.

### `onepot-sy` original bug detail (for reference)

Confirmed real, reproducible bug, not an environment artifact — all 3 notebooks failed identically on:
```
data = pr.normalize_data_to_controls(data, ctrl_name='10 uM HPTS')
TypeError: Index(...) must be called with a collection of some kind, 'ctrl_ints' was passed
```
from `cdk.analysis.cytosol.platereader.normalize_data_to_controls`. Confirmed this isn't a pandas-version mismatch — `nucleus-cdk` declares `pandas>=2.2.3,<3.0.0` and the test env's `2.3.3` satisfies it. Isolated to `onepot-sy` — grepped every devnote and no other notebook calls this function.

**Orphaned-notebook audit** (on disk, not referenced by any `toc` — doesn't mean broken, but not part of what actually gets published, and some are clearly stale/junk):
- `src/20250220-analysis.ipynb` — a generic template-scaffold leftover, present unreferenced in `03_mthfs`, `04_ppk`, `05_pure_workshop`, `08_ppk_cell`, `10-nucleus_cytosol_v05`, `11-Base_Cell`, `module-Clpxp`, `module-Clpxp-Cytosol` (same stub pattern already found and removed from `fwm-aria-d2` in PR #9).
- `04_ppk`: `20250611-analysis-acjs-test.ipynb` (a "-test" variant alongside the real analysis notebook).
- `05_pure_workshop`: `20250516-labchip-analysis.ipynb`, `nucleus-pure-protein-debug-draft.ipynb`, `20250516-final-experiment.ipynb`.
- `08_ppk_cell`: 3 "Code (yh)" notebooks alongside the toc'd "Code (acjs)" one — looks like two authors' parallel analysis, only one wired into the published `toc`.
- `11-Base_Cell`: `experiments/20251119-nucleus-liposomes/Untitled.ipynb`.
- `devnote-nucleus_onepot`: 2 more debug notebooks alongside the one in `toc`.
- `fwm-batch-bo`, `lipid-prep`: each has one `experiments/experiment-01/20250220-analysis.ipynb` — likely the same unfilled scaffold stub as `fwm-aria-d2` had.

None of the above were deleted — flagging only, per the established rule against deleting notebooks without explicit confirmation.

**Known non-transient issue found during this pass:** `bac-working-group`'s only author, "Energy Metabolism Working Group," has no `email` field in `curvenote.yml` — `curvenote check` fails this specific rule every time (`No authors provided an email`). Not something to guess at; needs a real contact from whoever owns that devnote before "content reviewed" can be meaningfully checked off for it.

## Data-quality flags from `sy-devnotes-download/` audit

- **Duplicate/near-empty directories**: `trial/`, `pla1/`, `cytosol-lifetime/` are completely empty (no files, no `curvenote.yml`) despite matching names of real devnotes already accounted for elsewhere (`pla1` and `cytosol-lifetime` both appear — with actual content — in `devnotes-downloaded/`). `devnote-template/` is also near-empty after bloat removal — its lone surviving `main.md` is an unfinished draft stub of the MTHFS story (title matches `devnote-test/`'s real content, but body says "Abstract TODO" / "Caption TODO" placeholders), and it has no `curvenote.yml`. None of these four contribute real content.
- **Base_Cell data**: `sy-devnotes-download/Base_Cell/` shares its Myst Key with the already-staged `core/11-Base_Cell` and carries two large raw liposome-imaging CSVs (1.6G + 702M) under an experiment folder (`20251119-nucleus-liposomes`) not referenced in its own `curvenote.yml` toc. These files are individually far over GitHub's ~100MB hard per-file push limit — they cannot be committed as plain files; need Git LFS or external storage (S3) before they can go in this repo. See memory `github-file-size-limits.md`.
- **Myst Key collision cluster (4-way)**: `b6272c31-dae6-4c60-bf48-a86466349d86` is shared by the placeholder stub `devnotes-downloaded/devcells-chicago-node/devnote-template`, plus three real-content dirs in `sy-devnotes-download/` — `pHtdGFP and trigger ssDNA in Cytosol/`, `PPK Planning DevNote/`, and `kickoff/kickoff-experimental/` (the last is the real, finished "DevCells: Kickoff Workshop," superseding the placeholder). Each needs a distinct fresh key before migration.
- **Author mismatch**: `sy-devnotes-download/devnote-test/` contains the MTHFS story (matches already-staged `core/03_mthfs`, credited there to Yemo Ku) but lists its author as Surendra Yadav — unresolved discrepancy.
