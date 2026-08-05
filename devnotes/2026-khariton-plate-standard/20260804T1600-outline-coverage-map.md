# Outline Coverage Map — Platereader Fluorescein Standards DevNote

**Purpose:** map the GDoc outline onto notebook figures/tables/claims — what the outline
covers, and what points the notebooks made but the outline omits.

**Status:** revised 2026-08-04 after MK+JC review; superseded content removed, decisions
recorded in "Review outcomes" below.

## Sources

| Source | What it is |
|---|---|
| [GDoc outline](https://docs.google.com/document/d/1YeHG2oj1cGATSv0y6wwvwjQ64non8o1TuKJtkYuJVBc/edit) | `2026-khariton-plate-standards` — outline + a new (empty) Figures section |
| [Notion: Standards dev.](https://app.notion.com/p/374ae616eb51800689a6f779b22124e7) | Research notebook, 2026-05-12 → 2026-07-15. 113 figures, 22 tables |
| [Notion project page](https://app.notion.com/p/3b2ae616eb51801d82a6f49363ab9bda) | "Previous analyses" (primary figures) + review comments on this document |
| `glycine://bnext/platform/QC_standardization/fluorescein_standards_dev/Platereader_standards_devnotes_comp/` | `raw_data/` and `analysis/` |

> **On asset naming.** The `*_updated260630.html` combined analyses are primary but will
> be replaced by a refactor of the same code. Entries below key on **what the analysis
> shows**, not the filename — after the refactor, descriptions still apply; only filenames
> change.

### The primary combined analyses

| # | Analysis | Current file |
|---|---|---|
| A1 | Cy5 combined deep analysis | `cy5_reads_compare_updated260630.html` |
| A2 | Cy3 combined deep analysis | `cy3_reads_compare_updated260630.html` |
| A3 | Syn2 combined deep analysis | `syn2_reads_compare_updated260630.html` |
| A4 | All reads combined, chosen mono/filter/gain settings | `fluorescein_standards_updated260630.html` |
| A5 | All reads combined, every read | `all_reads_compare_updated260630.html` |
| A6 | Linear fits: concentration estimation over time vs. averaged | `20260609_conc-estimation_method-compare.html` |

### The cross-cutting summary assets (top of notebook, generated 2026-07-24)

| # | Asset | Shows |
|---|---|---|
| S1 | Master calibration overlay | Every instrument × date × optic on one curve; Poly2-origin, log R² ~0.99–1.00 |
| S2 | Slope stability / saturation | Slope per instrument-read across runs; Cy3 roll-off >2 µM |
| S3 | `summary_conditions.png` | Slope by fresh/frozen × neighboring/isolated, per instrument, pooled 6/9 + 6/18 |
| S4 | GFP recovery overlay | k-corrected GFP est. vs known, all instruments, with dose slope |
| S5 | Reduced-curve / filter-vs-mono error | % error per candidate curve × read optic — **the 4-point justification figure** |
| **T-A** | Reduced-curve linear error table | 8 rows: instrument × optic × curve → in-curve %err, below %err, >2 µM recovery |
| **T-B** | Poly2 vs linear error table | 12 rows: read × curve → Poly2 %err vs linear %err. **Most decisive table in the notebook** |

---

# Review outcomes (2026-08-04, MK + JC)

Decisions from the first version's review. Binding on the draft.

### Adopted into the outline

| Gap raised | Where it landed |
|---|---|
| Fresh vs. frozen ladders | §2.1.1 Protocol → Storage |
| No well-to-well crosstalk | §2.1.5 Protocol → Plating (neighbor/isolate), + "caveat: if your plate is different" |
| Signal decline over a long read | §2.1.2 Photobleaching, §2.3.1.1 Linear drift (end), §2.3.4.3 drift threshold |
| Held-out standard recovery | §2.3.4.4 Hold-out test |
| Detection floor | §3.2.2 Low end non-linear |
| QC as a use case for standards | §4.2 Quality Control using standards |
| k correction factor | §4.3 Discussion — **not** an SOP section (see below) |

Also added by MK/JC: §2.1.3 Sodium borate, §2.1.4 Temperature, §2.3.1.2 early-timepoint
effects ("cut out X first reads / how to tell which"), §3.2.1 Saturation, and a restructure
of §2.3.4 into an explicit **"Criteria / QC for using the SOP"** checklist.

### Declined, with reasoning

- **"Rename §2.3 Linear fitting → model choice / lead with Poly2."** Declined. JC: the point
  is "*kinda hit in the Caveats/Different Optics section (that is, 'confirm that your system
  is actually in linear range'). should come up in story approximately as: hey check your
  stuff and also here's the criteria to do so.*" SOP keeps linear as the recommended path;
  non-linearity becomes a **QC failure mode** to detect (§2.3.4.1 + §3.1), not a competing
  model. Deliberate: teach readers to check their instrument, not default to a quadratic.
- **"Add a §2.4 'converting to useful units' SOP section for k."** Declined. k moves to §4.3
  Discussion instead — "*K correction is a useful method to implement and you should know
  about it.*" Awareness, not procedure.

### Wording correction

- Write **the signal decays**, not **fluorescein decays**. JC: "*'decay' implies too much
  mechanism… because we don't know the underlying mechanism.*" Applied throughout this
  document; must hold in the draft too.

### Flagged for follow-up

- **Hold-out testing relates to bootstrapping and other empirical model-comparison methods**
  — JC flags this as a possible citation. Feeds the new **Stnd DN: Lit review** task.

---

# Part A — Outline coverage

Legend: ✅ strong · 🟡 partial · ❌ none

## 1. Motivation

| Outline node | Cov | Assets / evidence |
|---|---|---|
| 1.1 Context | 🟡 | No notebook assets. Upstream: grandparent project *Instrument consistency and calibration*, Lux 2023, Piorino 2026. Notebook's internal motive: "one flscn standard curve reproducible across runs, instruments, and labs, so PURE GFP output reads in real nM." |
| 1.2 Why standards? with/without | 🟡 | **S2** = "without" case: instrument slopes differ ~100× (Syn2 7–9, Cy3 43–46, Cy5 670–785 RFU/nM) yet each stable run-to-run — that fact *is* the argument. **S1** = "with" case. No purpose-built before/after figure. |
| 1.3 "Here, we…" | ✅ | Write from the Current-curve recommendation block + **T-B**. |
| 1.3.1 Narrative (?) | ✅ | Open framing choice; material ready — Part B §7. |
| 1.4 Why fluorescein | 🟡 | Chosen in the 5/12 dye screen vs GFP/HPTS — "flscn cleanest/most linear." Criteria: accessible, reliable, comparable. **5/12 screen produced no figures** — choice asserted, not shown. |
| 1.4.1 Ease of access, robustness | ✅ | 6/22 overnight ambient-light plate still gave a decent curve; frozen ladders within 1–10%; one 48 µM stock held across all dates, no drift. |
| 1.4.2 NIST-traceable | ✅ | Invitrogen F36915, nominal 50 µM/actual 48 µM (dilutions vs 48). Alt: Sigma NIST1932. Prose only. |

## 2. Recommended SOP

| Outline node | Cov | Assets / evidence |
|---|---|---|
| 2.1 Protocol | ✅ | F36915 48 µM stock; 100 mM sodium borate pH 9.5 (Thermo J63637-AK); 20 µL stock + 940 µL NaBor → 1 µM. Plate maps: 5/20, 6/1, 6/2, 6/9, 6/18. |
| 2.1.1 Storage (temp, etc) | ✅ | Frozen ~1–10% low overall (2–8% on 6/18), mostly Cy5/Syn2; Cy3 flat. Cy3 slopes: 29.299 fresh-isolated vs 27.966 frozen-isolated (−4.5%); Cy5: 762.526 vs 698.736 (−8.4%). Pre-made frozen ladders work. **S3**, `20260618_cmp_cond_slope_ratio.png`, T14/T16. |
| 2.1.2 Photobleaching | 🟡 | No controlled experiment. 5/12 took 4 repeat reads to gauge this (no figures). 6/1 accident (~2h RT under light) and 6/22 overnight plate: uncontrolled but informative. Per-run `_stability` figures show within-read decline. |
| 2.1.3 Sodium borate | 🟡 | Reagent/pH documented, but the Tris (5/12) → borate (5/20+) switch has **no side-by-side test** — "why borate" is unevidenced here. |
| 2.1.4 Temperature | ❌ | **Never characterized.** Notebook flags unchecked item "Temp relationship for fluorescein." No supporting data. |
| 2.1.5 Plating (neighbor/isolate) | ✅ | Cy3 fresh-isolated (29.299) vs fresh-neighboring (29.247): 0.2% apart — "skipping wells to isolate unnecessary." Same assets as 2.1.1. |
| 2.2 Set of standards: blank + 3 | ✅ | **T-A**, **T-B**, **S5**, plus per-run reduced-standard-set analyses on 6/11, 6/18, 7/15. |
| 2.2.1 Why not just 1 µM? | ✅ | 5/20 vs historical AR-1060 MFG QC overlay: real PURE samples **exceed** the 1 µM standard's RFU. PURE steady state ≥1 µM → top standard must be ≥2 µM. |
| 2.2.2 Why not more/fewer? | ✅ | **T-B**: 8pt→4pt costs nothing, and on Cy3 filter *improves* accuracy (17.8%→1.2%) by dropping the compressed 4 µM point. Fewer than 4 untested. |
| 2.2.3 Why 0.5 / 1 / 2 µM | ✅ | **T-A**: `0/500/1000/2000` beats `0/125/500/2000` on every read except Cy5's >2 µM metric. **T-B**: best design across all four reads = `0/500/1000/2000` + Poly2-origin. |
| — "idiot-proof & comprehensive" | ✅ | 2-fold spacing for easy dilution; 8pt = "dense enough for Poly2, few enough for an 8-channel pipette"; range covers PURE steady state. |
| 2.3 Linear fitting | ✅ | Framing settled: linear is the recommended path, non-linearity is a QC failure mode (Review outcomes). Evidence linear *works* where the instrument is linear: **T-B** Cy5 Gext linear ≈ Poly2 to one decimal; Syn2 G35 3.5–4.2%; Cy3 mono 1.9–3.3%. |
| 2.3.1 Over time vs. averaged | ✅ | **A6** is this analysis (also `20260601_cy3_fits_compavg.png`). Practice: fit each timepoint independently. |
| 2.3.1.1 Linear drift (end) | ✅ | Signal declines 10–15% over a 6h read (7/15, Syn2). Within-run: 6/2 Cy5 held-out 1 µM drops 925→871–878 nM, t=31→121 min. `20260715_mfg277_stability.png`, `20260611_mfg_stability.png`. |
| 2.3.1.2 Early-read effects / cut first X | 🟡 | Practice restricts fits to **t≥10 min**, but rationale/cutoff choice is unstated. Outline's "how to tell which" is a real open analysis question, not just writing. |
| 2.3.2 CDK / how get | ❌ | **No coverage.** Notebook never names the analysis code, library, or repo — must be written from the tooling side. |
| 2.3.3 Negative control / blanking | 🟡 | Practice clear: NaBorate blank-subtracted. Evidence for *why* thin. 7/15 had no negative control (PURE not background-subtracted) — judged negligible (t=0 ≈ a few RFU). |
| 2.3.4 Criteria / QC for using the SOP | 🟡 | Restructured at review into an explicit checklist. Material exists per item below, but **no checklist assembled yet** — highest-value writing task. |
| 2.3.4.1 Linearity + checks | 🟡 | Cy3 filter non-linearity every date; Poly2-origin remedy; 4PL/5PL tried & rejected (unstable low end, CV 22–77%); held-out analyses; row-H position QC. Needs assembly into a "checks to perform" list. |
| 2.3.4.2 Gain coverage | ✅ | 5/20 Syn2 gain series: G35 full range; G50/G65 saturate at 10 nM/100 nM. Cy5 Gext linear into the millions (4 µM≈2.6M RFU); Syn2 G35 4 µM≈31k RFU. |
| 2.3.4.3 Drift below threshold | 🟡 | Magnitude known (10–15%/6h). **No threshold defined** — needs a call on what's acceptable. |
| 2.3.4.4 Hold-out test | ✅ | `*_heldout.png` on 6/11, 6/18, 7/15; T10, T17. MFG 1 µM (AR-910): 106% recovery on 6/11 (Cy5), 85% on 7/15 (Syn2) — run/read-specific, not a bad stock. Citation request pending (bootstrapping). |

## 3. Caveats: comparing across plate readers

| Outline node | Cov | Assets / evidence |
|---|---|---|
| 3.1 Mono vs filter | ✅ | Best-evidenced section in the notebook. **T-B** same-instrument Cy3 mono vs filter: 8pt Poly2 0.3% vs 17.8%; linear 7.2% vs 117%. **T-A** >2 µM recovery: Cy3 filter 0.57–0.60 vs mono 0.94. 6/18 Cy3 GFP top point: linear recovers 2462/3571 nM (−31%), Poly2 3356 (−6%). Also carries the "confirm your system is in linear range" message (per review). |
| — "cube vs wheel" | ❌ | Unaddressed. Open question, or drop. |
| 3.2 Dynamic range | ✅ | **T-A** separates in-curve from below-curve error — below-curve worse for every configuration. |
| 3.2.1 Saturation | ✅ | 10 µM oversaturated, no value (6/1) — the one figure with real alt text. Cy3 filter saturates ~2 µM. |
| 3.2.2 Low end non-linear | ✅ | 6/2, same GFP dilutions: Syn2 read 0–3/25 timepoints above detection at 1:40k/1:400k vs Cy3's 25/25. GFP CV: 27–77% below ~1 nM estimated. T4 vs T5. |
| 3.3 Replicates vs number of points | 🟡 | Points side fully covered (**T-A**/**T-B**). Replicates side thinner: triplicate recommended per 6/11 data; row-H position effect is the real argument. **Replicate count was never controlled** — drifted 5→2→3→3→2 across runs. |

## 4. Discussion / Future work

| Outline node | Cov | Assets / evidence |
|---|---|---|
| 4.1 Other standards (e.g. microscopy) | ❌ | No notebook coverage. Related active effort: grandparent Obj 6 (deGFP protein standards) belongs here. |
| 4.2 QC using standards | ✅ | "Is my experiment informative? Is the instrument off today?" — held-out recovery, replicate/row agreement, drift, gain coverage all serve this. Precedent: MFG QC plates (6/2, 6/11, 7/15) already use the ladder this way in production. |
| 4.3 k correction (awareness) | ✅ | k_Syn2 = 1.942 (lin) / 1.922 (Poly2); k_Cy3 = 0.893 / 1.573; k_Cy5 = 2.103 / 2.114. GFP dose slope 1.05–1.14; corrected median recovery error 6–16%, consistently slightly under. **S4**, `20260618_cmp_k_by_instrument.png`, `20260618_cmp_gfp_corrected.png`, T12/T13/T15. |

## 5. Figures section (new, empty)

GDoc's new "Platereader Fluorescein Standards: Figures" section is empty. Candidate Figure 1
material and the strongest assets: Part B §7 and the summary-asset table above. Unblocked.

---

# Part B — Plot points still not in the outline

First version listed 14 orphaned plot points; review adopted 7 (Review outcomes). Remainder
below.

### 1. The absolute anchor of the ladder doesn't matter
6/18 ran two independent series — A from 4000 nM, B from 3200 nM — both land on one curve.
Reassuring for cross-lab use: labs need not hit identical concentrations.
Assets: `20260618_cmp_fluor_calib.png`, **S1**.

### 2. Instrument sensitivity spans ~100× yet each is internally stable
Cy3 ~43–46, Syn2 ~7–9, Cy5 ~670–785 RFU/nM; slopes hold between runs. Cy5 Gext 4 µM≈2.6M RFU
vs Syn2 G35 4 µM≈31k RFU. Cleanest one-sentence answer to "why standards at all" — would
strengthen §1.2 (currently only implicit). Asset: **S2**.

### 3. The reduced curve doesn't just cost nothing — sometimes it helps
Cy3 filter, Poly2: 8pt 17.8% error → 4pt `0/500/1000/2000` 1.2%, by dropping the compressed
4 µM point. Counterintuitive — state explicitly in §2.2.2, not just in a table.

### 4. Buffer and stock details that are easy to lose
Fluorescein ladder: 100 mM sodium borate pH 9.5. **GFP ladders: Tris pH 9** (different
buffer). Dilutions computed vs actual 48 µM, not nominal 50. One stock across every date —
lot isn't a confounder here. Partly in §2.1.3; the GFP-buffer difference and the
actual-vs-nominal detail have no home yet.

### 5. Position / pipetting error as a distinct error source
6/11 Cy5: row H reads 5–17% low vs rows J/L, worst mid-range (ratio 0.829 at 1000 nM). **Not**
on 7/15 (H within ~2% of J) — intermittent, likely pipetting. Only implicit under §2.1.5
Plating and §3.3; really the strongest argument for triplicate plus a replicate-agreement
check — belongs in §2.3.4 QC criteria.
Assets: `20260611_mfg_rowH_qc.png`, T11.

### 6. Open items the notebook flags
- **Temperature dependence never characterized** — now §2.1.4, no data
- Cy5 G70 collected, never analyzed
- 3-point curve (100 nM→>1 µM) considered, never tested
- "Do we care about <100 nM?"
- "How high — 2 vs 4 µM?" — needs historical b.next + collaborator data
- **"Handle the Cy3 Poly2 model robustly across labs?"** — deepest unresolved problem: an
  instrument-specific model undercuts the cross-lab comparability the project exists to
  deliver
- "Confidence gain from multiple gains + fewer samples?"

### 7. Narrative beats — the "lived experience" material
§1.3.1 `Narrative (?)` is still an open framing choice. Available beats:
- **Photobleaching accident (6/1):** a 30-min "come to temp" delay opened the instrument door
  instead of pre-warming — plate sat ~2h at RT under light before reading. "*I'm dumb… 2 hr
  delay at room temp (sad) and photobleaching (extra sad)*." Repeated 6/2.
- **10 µM didn't read** (6/1) — oversaturated, no value.
- **Overnight plate that worked anyway (6/22):** 6/18's Cy3 read crashed; plate sat out
  overnight in an open tray, RT, ambient light — rerun "looks surprisingly decent."
- **Ceiling discovery (5/20):** ladder overlaid on historical AR-1060 MFG QC data — real PURE
  samples exceeded the top standard. The moment the 1 µM ceiling broke.
- **Curve evolution #1→#5:** 1 nM–1 µM 10-fold → widened to 10 µM (saturated) → 2-fold 7 nM–4
  µM → 63 nM–4 µM + fresh/frozen → locked 8pt 0–4 µM. Ready-made Figure 1.
- **Cy5 cut short on 5/20** — another user needed the instrument.

---

# Part C — Open questions before drafting

Carried forward; none resolved at review.

1. **Poly2 + few points: the notebook contradicts itself.** 6/1 and 6/2: "the poly2 fit does
   not work well with fewer samples on the curve." The June summary then recommends a
   4-point curve, and **T-B** shows Poly2 at 0.1–6.1% error on exactly those curves. Reconcile
   before publishing either claim.

2. **Date inconsistency on MFG-262.** Summary timeline says 6/4; experiment section says
   6/11. Pick one.

3. **Replicate count was never a controlled variable.** "Triplicate" is recommended on the
   row-H incident, not an n-vs-error experiment. Soften the claim, or state the reasoning as
   "position artifacts happen, so n≥3 lets you detect them."

4. **The 5/12 dye screen has no figures** — the fluorescein-over-GFP-over-HPTS decision is
   asserted, not shown. Regenerate it if §1.4 must justify the choice.

5. **CDK / analysis code (§2.3.2) has zero source material.**

6. **Syn2 has no fresh/frozen conditions table** (Cy3 and Cy5 do) — can't assemble a clean
   3-instrument slope table from the notebook as-is.

7. **No temperature data at all** for §2.1.4 — either run it, or scope the section to "we
   haven't characterized this; here's what we'd expect."

8. **The t ≥ 10 min cutoff has no stated rationale**, and §2.3.1.2 now asks how a reader
   should choose it — likely needs new analysis, not just writing.

9. **No drift threshold defined** for §2.3.4.3 — what counts as too much?
