# Outline Coverage Map — Platereader Fluorescein Standards DevNote

**Purpose:** map the GDoc outline onto the figures, tables, and claims that already exist in
the research notebooks, so we can see (a) what is already covered and by what, and (b) what
narrative points we made along the way but forgot to put in the outline.

**Status:** revised 2026-08-04 after MK + JC review. Superseded content removed; review
decisions recorded in "Review outcomes" below.

## Sources

| Source | What it is |
|---|---|
| [GDoc outline](https://docs.google.com/document/d/1YeHG2oj1cGATSv0y6wwvwjQ64non8o1TuKJtkYuJVBc/edit) | `2026-khariton-plate-standards` — outline + a new (empty) Figures section |
| [Notion: Standards dev.](https://app.notion.com/p/374ae616eb51800689a6f779b22124e7) | Research notebook, 2026-05-12 → 2026-07-15. 113 figures, 22 tables |
| [Notion project page](https://app.notion.com/p/3b2ae616eb51801d82a6f49363ab9bda) | "Previous analyses" (primary figures) + review comments on this document |
| `glycine://bnext/platform/QC_standardization/fluorescein_standards_dev/Platereader_standards_devnotes_comp/` | `raw_data/` and `analysis/` |

> **On asset naming.** The combined `*_updated260630.html` analyses are primary, but will be
> superseded by refactored versions of the same analysis code. So everything below is keyed to
> **what the analysis shows**, with the current filename only as a pointer. When the refactor
> lands, the descriptions should still resolve; only the filenames change.

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

Decisions made on the first version of this document. These are binding on the draft.

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

Also added by MK/JC beyond what this document raised: §2.1.3 Sodium borate, §2.1.4 Temperature,
§2.3.1.2 early-timepoint effects ("cut out X first reads / how to tell which"), §3.2.1 Saturation,
and a restructure of §2.3.4 into an explicit **"Criteria / QC for using the SOP"** checklist.

### Declined, with reasoning

- **"Rename §2.3 Linear fitting → model choice / lead with Poly2."** Declined. JC: the point is
  "*kinda hit in the Caveats/Different Optics section (i.e., 'confirm that your system is actually
  in linear range'). should come up in story approximately as: hey check your stuff and also here's
  the criteria to do so.*" So the SOP keeps linear as the recommended path, and non-linearity is
  handled as a **QC failure mode** the reader is taught to detect (§2.3.4.1 + §3.1) rather than as
  a competing model recommendation. This is a deliberate narrative choice: the DevNote teaches
  readers to check their instrument, not to fit a quadratic by default.
- **"Add a §2.4 'converting to useful units' SOP section for k."** Declined. k moved to §4.3
  Discussion instead — "*K correction is a useful method to implement and you should know about
  it.*" Scoped as awareness, not procedure.

### Wording correction

- Do not write that **fluorescein decays**. Write that the **signal decays**. JC: "*'decay'
  implies too much mechanism… because we don't know the underlying mechanism.*" Applied
  throughout this document; must hold in the draft too.

### Flagged for follow-up

- **Hold-out testing is related to bootstrapping and other empirical model-comparison methods** —
  JC flags this may be worth a citation. Feeds the new **Stnd DN: Lit review** task.

---

# Part A — Outline coverage

Legend: ✅ strong · 🟡 partial · ❌ none

## 1. Motivation

| Outline node | Cov | Assets / evidence |
|---|---|---|
| 1.1 Context | 🟡 | No notebook assets. From upstream: grandparent project *Instrument consistency and calibration*, Lux 2023, Piorino 2026. Notebook supplies the internal motive: "one flscn standard curve reproducible across runs, instruments, and labs, so PURE GFP output reads in real nM." |
| 1.2 Why standards? with/without | 🟡 | **S2** carries the "without" case: instrument slopes differ ~100× (Syn2 7–9, Cy3 43–46, Cy5 670–785 RFU/nM) yet each is stable run-to-run. That single fact *is* the argument. **S1** is the "with" case. No purpose-built before/after figure exists. |
| 1.3 "Here, we…" | ✅ | Write from the Current-curve recommendation block + **T-B**. |
| 1.3.1 Narrative (?) | ✅ | Still an open framing choice, but the material is ready — see Part B §7. |
| 1.4 Why fluorescein | 🟡 | Chosen in the 5/12 dye screen vs GFP and HPTS — "flscn cleanest/most linear." Design criteria: accessible / reliable / comparable. **The 5/12 screen produced no figures**, so the choice is asserted, not shown. |
| 1.4.1 Ease of access, robustness | ✅ | 6/22 overnight ambient-light plate still gave a decent curve; frozen ladders within 1–10%; one 48 µM stock across all dates without drift. |
| 1.4.2 NIST-traceable | ✅ | Invitrogen F36915, nominal 50 µM / actual 48 µM (dilutions prepared against 48). Alternative: Sigma NIST1932. Prose only. |

## 2. Recommended SOP

| Outline node | Cov | Assets / evidence |
|---|---|---|
| 2.1 Protocol | ✅ | F36915 48 µM stock; 100 mM sodium borate pH 9.5 (Thermo J63637-AK); 20 µL stock + 940 µL NaBor → 1 µM. Plate maps for 5/20, 6/1, 6/2, 6/9, 6/18. |
| 2.1.1 Storage (temp, etc) | ✅ | Frozen ~1–10% low overall (2–8% on 6/18), mostly Cy5/Syn2; Cy3 flat. Cy3 slopes fresh-isolated 29.299 vs frozen-isolated 27.966 (−4.5%); Cy5 762.526 vs 698.736 (−8.4%). Conclusion: pre-made frozen ladders are fine. **S3**, `20260618_cmp_cond_slope_ratio.png`, T14/T16. |
| 2.1.2 Photobleaching | 🟡 | No controlled photobleaching experiment. Available: 5/12 design took 4 repeat reads specifically to gauge it (but produced no figures); the 6/1 accident (~2 h at RT under light) and the 6/22 overnight plate are both uncontrolled but informative; per-run `_stability` figures show within-read decline. |
| 2.1.3 Sodium borate | 🟡 | Reagent and pH documented. But the switch from Tris (5/12) to borate (5/20 onward) has **no documented side-by-side** — the "why borate" claim is currently unevidenced in this dataset. |
| 2.1.4 Temperature | ❌ | **Explicitly never characterized.** The notebook carries an unchecked item "Temp relationship for fluorescein". This outline node has no supporting data at all. |
| 2.1.5 Plating (neighbor/isolate) | ✅ | Cy3 fresh-isolated 29.299 vs fresh-neighboring 29.247 → 0.2% apart. Conclusion: "skipping wells to isolate unnecessary." Same assets as 2.1.1. |
| 2.2 Set of standards: blank + 3 | ✅ | **T-A**, **T-B**, **S5**, plus per-run reduced-standard-set analyses on 6/11, 6/18, 7/15. |
| 2.2.1 Why not just 1 µM? | ✅ | 5/20 vs historical AR-1060 MFG QC overlay: real PURE samples **exceed** the 1 µM standard's RFU. PURE steady state ≥1 µM → top standard must be ≥2 µM. |
| 2.2.2 Why not more/fewer? | ✅ | **T-B**: 8 pt → 4 pt costs nothing, and on Cy3 filter *improves* accuracy (17.8% → 1.2%) by dropping the compressed 4 µM point. Fewer than 4 untested. |
| 2.2.3 Why 0.5 / 1 / 2 µM | ✅ | **T-A**: `0/500/1000/2000` beats `0/125/500/2000` on every read except Cy5's >2 µM metric. **T-B**: best design across all four reads is `0/500/1000/2000` + Poly2-origin. |
| — "idiot-proof & comprehensive" | ✅ | 2-fold spacing for easy dilution; 8 pt = "dense enough to fit Poly2, few enough wells for 8-channel pipette"; range encompasses PURE steady state. |
| 2.3 Linear fitting | ✅ | Framing settled at review: linear is the recommended path, non-linearity is a QC failure mode (see Review outcomes). Evidence that linear *works* where the instrument is linear: **T-B** Cy5 Gext linear ≡ Poly2 to one decimal; Syn2 G35 3.5–4.2%; Cy3 mono 1.9–3.3%. |
| 2.3.1 Over time vs. averaged | ✅ | **A6** is exactly this analysis. Also `20260601_cy3_fits_compavg.png`. Practice: independent fit at each timepoint. |
| 2.3.1.1 Linear drift (end) | ✅ | Signal declines 10–15% over a 6 h read (7/15, Syn2). Within-run: 6/2 Cy5 held-out 1 µM reads 925 → 871–878 nM across t = 31→121 min. `20260715_mfg277_stability.png`, `20260611_mfg_stability.png`. |
| 2.3.1.2 Early-read effects / cut first X | 🟡 | The practice exists — fits are restricted to **t ≥ 10 min** — but the notebook never states the rationale or how the cutoff was chosen. The outline now asks "how to tell which", which is a genuine open analysis question, not just a writing task. |
| 2.3.2 CDK / how get | ❌ | **Still no coverage.** The notebook never names the analysis code, library, or repo. Must be written from the tooling side. |
| 2.3.3 Negative control / blanking | 🟡 | Practice clear (NaBorate blank-subtracted). Evidence for *why* is thin. Datapoint: 7/15 had no negative control, so PURE samples were not background-subtracted — judged negligible (t=0 ≈ a few RFU). |
| 2.3.4 Criteria / QC for using the SOP | 🟡 | Restructured at review into an explicit checklist. Material exists for each item below but **no assembled checklist yet** — this is now the highest-value writing task. |
| 2.3.4.1 Linearity + checks | 🟡 | Cy3 filter non-linearity across every date; Poly2-origin as remedy; 4PL/5PL tried and rejected (unstable low end, CV 22–77%); held-out analyses; row-H position QC. Needs assembling into "checks to perform". |
| 2.3.4.2 Gain coverage | ✅ | 5/20 Syn2 gain series: G35 full range, G50/G65 saturate at 10 nM / 100 nM. Cy5 Gext linear into millions (4 µM ≈ 2.6 M RFU); Syn2 G35 4 µM ≈ 31 k RFU. |
| 2.3.4.3 Drift below threshold | 🟡 | Magnitudes known (10–15% / 6 h). **No threshold defined** — needs a call on what's acceptable. |
| 2.3.4.4 Hold-out test | ✅ | `*_heldout.png` on 6/11, 6/18, 7/15; T10, T17. MFG 1 µM (AR-910) recovers 106% on 6/11 (Cy5) but 85% on 7/15 (Syn2) → run/read-specific, not a bad stock. Cite request pending (bootstrapping). |

## 3. Caveats: comparing across plate readers

| Outline node | Cov | Assets / evidence |
|---|---|---|
| 3.1 Mono vs filter | ✅ | Best-evidenced section in the notebook. **T-B** same-instrument Cy3 mono vs filter: 8-pt Poly2 0.3% vs 17.8%; linear 7.2% vs 117%. **T-A** >2 µM recovery: Cy3 filter 0.57–0.60 vs mono 0.94. 6/18 Cy3 GFP top point: linear recovers 2462 of 3571 nM (−31%), Poly2 3356 (−6%). Per review, this section also carries the "confirm your system is in linear range" message. |
| — "cube vs wheel" | ❌ | Still not addressed anywhere. Open question, or drop it. |
| 3.2 Dynamic range | ✅ | **T-A** separates in-curve from below-curve error — below-curve is worse for every configuration. |
| 3.2.1 Saturation | ✅ | 10 µM oversaturated and returned no value (6/1) — the one notebook figure with real alt text calls this out. Cy3 filter saturates ~2 µM. |
| 3.2.2 Low end non-linear | ✅ | 6/2, same GFP dilutions: Syn2 read 0–3 of 25 timepoints above detection at 1:40k/1:400k while Cy3 read 25/25. GFP CV blows up 27–77% below ~1 nM estimated. T4 vs T5. |
| 3.3 Replicates vs number of points | 🟡 | Points side fully covered (**T-A**/**T-B**). Replicates side thinner: triplicate recommended "see 6/11 data", and the row-H position effect is the real argument. **Replicate count was never a controlled variable** — it drifted run to run (5 → 2 → 3 → 3 → 2). |

## 4. Discussion / Future work

| Outline node | Cov | Assets / evidence |
|---|---|---|
| 4.1 Other standards (e.g. microscopy) | ❌ | No notebook coverage. Adjacent: grandparent Obj 6 (deGFP protein standards) is an active parallel effort and belongs here. |
| 4.2 QC using standards | ✅ | "Is my experiment informative? Is the instrument off today?" — held-out recovery, replicate/row agreement, drift, gain coverage all serve this. Real precedent: the MFG QC plates on 6/2, 6/11, 7/15 already use the ladder this way in production. |
| 4.3 k correction (awareness) | ✅ | k_Syn2 = 1.942 (lin) / 1.922 (Poly2); k_Cy3 = 0.893 / 1.573; k_Cy5 = 2.103 / 2.114. GFP dose slope 1.05–1.14; corrected median recovery error 6–16%, systematically slightly under. **S4**, `20260618_cmp_k_by_instrument.png`, `20260618_cmp_gfp_corrected.png`, T12/T13/T15. |

## 5. Figures section (new, empty)

The GDoc now carries a second section, "Platereader Fluorescein Standards: Figures", with no
entries. Candidate Figure 1 material and the strongest assets are listed in Part B §7 and in the
summary-asset table above. Populating this is unblocked.

---

# Part B — Plot points still not in the outline

The first version of this document listed 14 orphaned plot points. Seven were adopted into the
outline at review (see Review outcomes). These are what remain.

### 1. The absolute anchor of the ladder doesn't matter
6/18 ran two independent series — A from 4000 nM, B from 3200 nM — and both land on one curve.
Non-obvious and reassuring for cross-lab use: labs need not hit identical concentrations.
Assets: `20260618_cmp_fluor_calib.png`, **S1**.

### 2. Instrument sensitivity spans ~100× yet each is internally stable
Cy3 ~43–46, Syn2 ~7–9, Cy5 ~670–785 RFU/nM; slopes hold between runs. Cy5 Gext 4 µM ≈ 2.6 M RFU
vs Syn2 G35 4 µM ≈ 31 k RFU. This is the cleanest one-sentence answer to "why standards at all",
and would strengthen §1.2 where coverage is currently only implicit. Asset: **S2**.

### 3. The reduced curve doesn't just cost nothing — sometimes it helps
Cy3 filter, Poly2: 8-pt 17.8% error → 4-pt `0/500/1000/2000` 1.2%, because dropping the compressed
4 µM point removes the worst-behaved data. Counterintuitive; worth stating explicitly in §2.2.2
rather than leaving it inside a table.

### 4. Buffer and stock details that are easy to lose
Fluorescein ladder in 100 mM sodium borate pH 9.5; **GFP ladders in Tris pH 9** (different buffer).
Dilutions computed against actual 48 µM, not nominal 50 µM. One stock across every date, so lot is
not a confounder in this dataset. Partially lands in §2.1.3, but the GFP-buffer difference and the
actual-vs-nominal detail have no home yet.

### 5. Position / pipetting error as a distinct error source
6/11 Cy5: row H read 5–17% low vs rows J/L, worst mid-range (ratio 0.829 at 1000 nM). Did **not**
recur on 7/15 (H within ~2% of J) → intermittent, likely pipetting. Currently only implicit under
§2.1.5 Plating and §3.3; it is really the strongest argument for triplicate plus a
replicate-agreement check, and belongs in §2.3.4 QC criteria.
Assets: `20260611_mfg_rowH_qc.png`, T11.

### 6. Open items the notebook flags
- **Temperature dependence never characterized** — now an outline node (§2.1.4) with no data
- Cy5 G70 collected but never analyzed
- 3-point curve (100 nM → >1 µM) contemplated, never tested
- "Do we care about <100 nM?"
- "How high do we need to go, 2 vs 4 µM?" — wants historical b.next + collaborator data
- **"How to handle the Cy3 Poly2 model robustly across labs?"** — deepest unresolved problem: an
  instrument-specific model undercuts the cross-lab comparability the project exists to deliver
- "What's the increase in confidence if we do multiple gains with decreased sampling?"

### 7. Narrative beats — the "lived experience" material
§1.3.1 `Narrative (?)` is still an open framing choice. The available beats:
- **The photobleaching accident (6/1):** a 30-min "come to temp" delay opened the instrument door
  instead of pre-warming, leaving the plate ~2 h at RT under light before reading. Recorded as
  "*I'm dumb… 2 hr delay at room temp (sad) and photobleaching (extra sad)*". Repeated 6/2.
- **10 µM simply did not read** (6/1) — oversaturated, no value returned.
- **The overnight plate that worked anyway (6/22):** Cy3's 6/18 read crashed; the plate sat out in
  an open tray at RT under ambient light overnight and the rerun "looks surprisingly decent."
- **The ceiling discovery (5/20):** overlaying the ladder on historical AR-1060 MFG QC data showed
  real PURE samples above the top standard — the moment the 1 µM ceiling was disproved.
- **Curve evolution #1 → #5:** 1 nM–1 µM 10-fold → widened to 10 µM (saturated) → 2-fold 7 nM–4 µM
  → 63 nM–4 µM + fresh/frozen → locked 8-pt 0–4 µM. Ready-made Figure 1.
- **Cy5 cut short on 5/20** because another user needed the instrument.

---

# Part C — Open questions before drafting

Carried forward; none of these were resolved at review.

1. **Poly2 + few points: the notebook contradicts itself.** 6/1 and 6/2 state "the poly2 fit does
   not work well with fewer samples on the curve." The June summary then recommends a 4-point
   curve, and **T-B** shows Poly2 at 0.1–6.1% error on exactly those 4-point curves. Something
   changed between those analyses; needs reconciling before either claim is published.

2. **Date inconsistency on MFG-262.** The summary timeline says 6/4; the experiment section is
   dated 6/11. Pick one.

3. **Replicate count was never a controlled variable.** "Triplicate" is recommended, but the
   evidence is the row-H incident rather than an n-vs-error experiment. Either soften the claim or
   state the reasoning as "position artifacts happen, so n≥3 lets you detect them."

4. **The 5/12 dye screen has no figures** — the fluorescein-over-GFP-over-HPTS decision is
   asserted, not shown. If §1.4 is meant to justify the choice, we may need to regenerate it.

5. **CDK / analysis code (§2.3.2) has zero source material.**

6. **Syn2 has no fresh/frozen conditions table** (Cy3 and Cy5 do), so a clean 3-instrument slope
   table can't be assembled from the notebook as-is.

7. **No temperature data at all** for the new §2.1.4 node — either run it, or scope the section to
   "we haven't characterized this; here's what we'd expect."

8. **The t ≥ 10 min cutoff has no stated rationale**, and §2.3.1.2 now asks how a reader should
   choose it for themselves. Likely needs new analysis, not just writing.

9. **No drift threshold defined** for §2.3.4.3 — what counts as too much?
