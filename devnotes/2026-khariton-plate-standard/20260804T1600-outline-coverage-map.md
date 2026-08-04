# Outline Coverage Map — Platereader Fluorescein Standards DevNote

**Purpose:** map the GDoc outline onto the figures, tables, and claims that already exist in
the research notebooks, so we can see (a) what is already covered and by what, and (b) what
narrative points we made along the way but forgot to put in the outline.

**Status:** working document, 2026-08-04. Not committed.

## Sources

| Source | What it is |
|---|---|
| [GDoc outline](https://docs.google.com/document/d/1YeHG2oj1cGATSv0y6wwvwjQ64non8o1TuKJtkYuJVBc/edit) | `2026-khariton-plate-standards` — the outline being mapped |
| [Notion: Standards dev.](https://app.notion.com/p/374ae616eb51800689a6f779b22124e7) | Research notebook, 2026-05-12 → 2026-07-15. 113 figures, 22 tables |
| Notion project page, "Previous analyses" | 6 combined HTML analyses, updated 2026-06-30 — **primary figure source** |
| `smb://glycine.int.bnext.bio/bnext/platform/QC_standardization/fluorescein_standards_dev` | Raw data |

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

# Part A — Outline coverage

Legend: ✅ strong · 🟡 partial · ❌ none

## 1. Motivation

| Outline node | Cov | Assets / evidence |
|---|---|---|
| 1.1 Context | 🟡 | No notebook assets. Comes from upstream: grandparent project *Instrument consistency and calibration*, Lux 2023, Piorino 2026. Notebook supplies the b.next-internal motive: "one flscn standard curve reproducible across runs, instruments, and labs, so PURE GFP output reads in real nM." |
| 1.2 Why standards? with/without | 🟡 | **S2** carries the "without" case implicitly: instrument slopes differ ~100× (Syn2 7–9, Cy3 43–46, Cy5 670–785 RFU/nM) yet each is stable run-to-run. That single fact *is* the argument. **S1** is the "with" case. No purpose-built before/after figure exists. |
| 1.3 "Here, we…" | ✅ | Write from the Current-curve recommendation block + **T-B**. |
| 1.3.1 Narrative (?) | ✅ | The curve-evolution list (#1–#5 + 2 MFG QC deployments) is a ready-made Figure 1 timeline. See Part B §N. |
| 1.4 Why fluorescein | 🟡 | Notebook: chosen in the 5/12 dye screen vs GFP and HPTS — "flscn cleanest/most linear." Design criteria stated: accessible / reliable / comparable. **But the 5/12 screen produced no figures** — the comparison that justifies the choice is undocumented visually. |
| 1.4.1 Ease of access, robustness | ✅ | Robustness has real data: 6/22 overnight-ambient-light plate still gave a decent curve; frozen ladders within 1–10%; one 48 µM stock used across all dates without drift. |
| 1.4.2 NIST-traceable | ✅ | Invitrogen F36915, nominal 50 µM / actual 48 µM (dilutions prepared against 48). Alternative: Sigma NIST1932. Prose only, no figure needed. |

## 2. Recommended SOP

| Outline node | Cov | Assets / evidence |
|---|---|---|
| 2.1 Protocol | ✅ | Full reagent/volume detail in notebook: F36915 48 µM stock; 100 mM sodium borate pH 9.5 (Thermo J63637-AK); 20 µL stock + 940 µL NaBor → 1 µM; volume math. Plate maps exist for 5/20, 6/1, 6/2, 6/9, 6/18. |
| 2.2 Set of standards: blank + 3 | ✅ | **T-A**, **T-B**, **S5**, plus per-run reduced-standard-set analyses on 6/11, 6/18, 7/15. |
| 2.2.1 Why not just 1 µM? | ✅ | 5/20 vs historical AR-1060 MFG QC overlay: real PURE samples **exceed** the 1 µM standard's RFU. Also: PURE steady state ≥1 µM, so the top standard must be ≥2 µM. |
| 2.2.2 Why not more/fewer? | ✅ | **T-B** shows 8 pt → 4 pt costs nothing (and on Cy3 filter *improves* accuracy, 17.8% → 1.2%, by dropping the compressed 4 µM point). Fewer than 4 untested — the 3-pt curve is an open item. |
| 2.2.3 Why 0.5 / 1 / 2 µM | ✅ | **T-A**: `0/500/1000/2000` beats `0/125/500/2000` on every read except Cy5's >2 µM metric. **T-B**: best single design across all four reads is `0/500/1000/2000` + Poly2-origin (0.1–1.2% err; Cy5 6.1%). |
| — "idiot-proof & comprehensive" | ✅ | 2-fold spacing chosen for easy dilution; 8 pt chosen as "dense enough to fit Poly2, few enough wells for 8-channel pipette." Range chosen to fully encompass PURE steady state. |
| 2.3 Linear fitting | ⚠️ | Covered, but **the outline's framing is wrong** — see Part C §1. Linear is *not* sufficient on filter reads (117% error on Cy3 8-pt). |
| 2.3.1 Over time vs. averaged | ✅ | **A6** is exactly this analysis. Also `20260601_cy3_fits_compavg.png`. Notebook practice: independent fit at each timepoint, restricted to t ≥ 10 min. |
| 2.3.2 CDK / how get | ❌ | **No coverage anywhere.** The notebook never names the analysis code, library, or repo. Needs to be written from scratch / from the CDK side. |
| 2.3.3 Negative control / blanking | 🟡 | Practice is clear (NaBorate blank-subtracted). Evidence for *why* is thin. Relevant datapoint: 7/15 had no negative control, so PURE samples were not background-subtracted — judged negligible (t=0 ≈ a few RFU). |
| 2.3.4 What if standards aren't linear? | 🟡 | Rich material, no assembled checklist. Available: Cy3 filter non-linearity across every date; Poly2-origin as the remedy; 4PL/5PL tried and rejected; held-out/leave-one-out recovery analyses (6/11, 6/18, 7/15); row-H position QC. |
| 2.3.5 Gains: full range, no saturation | ✅ | 5/20 Syn2 gain series: G35 shows full range, G50/G65 saturate at 10 nM / 100 nM. Cy5 Gext linear into millions of RFU (4 µM ≈ 2.6 M); Syn2 G35 4 µM ≈ 31 k RFU. |

## 3. Caveats: comparing across plate readers

| Outline node | Cov | Assets / evidence |
|---|---|---|
| 3.1 Mono vs filter | ✅ | Strongest-evidenced section in the whole notebook. **T-B** same-instrument Cy3 mono vs filter: 8-pt Poly2 0.3% vs 17.8%; linear 7.2% vs 117%. **T-A**: >2 µM recovery — Cy3 filter 0.57–0.60 vs mono 0.94. 6/18 Cy3 GFP top point: linear recovers 2462 of 3571 nM (−31%), Poly2 3356 (−6%). |
| — "cube vs wheel" | ❌ | Not addressed anywhere. Open question, or drop it. |
| 3.2 Dynamic range; in vs out of linear fit | ✅ | **T-A** separates in-curve error from below-curve error — below-curve is worse for every configuration. Ceiling evidence: 10 µM oversaturated and returned no value (6/1, with an annotated figure). Floor evidence: GFP CV blows up 27–77% below ~1 nM estimated. |
| 3.3 Replicates vs number of points | 🟡 | Points side is fully covered (**T-A**/**T-B**). Replicates side is thinner: triplicate recommended "see 6/11 data", and the row-H position effect is the real argument. **No experiment varied replicate count as a controlled variable** — it drifted run to run (5 → 2 → 3 → 3 → 2). |

## 4. Discussion / Future work

| Outline node | Cov | Assets / evidence |
|---|---|---|
| 4.1 Other standards (e.g. microscopy) | ❌ | No notebook coverage. Adjacent: grandparent project Obj 6 (deGFP protein standards) is an active parallel effort and belongs in this section. |

**Headline:** coverage of the outline is high — but that is partly because the outline is
narrower than the work. The bigger finding is Part B.

---

# Part B — Plot points made in the notebooks that the outline misses

Ordered roughly by how much they'd cost the DevNote to omit.

### 1. The k correction factor — fluorescein-equivalent → GFP-equivalent
**Missing entirely from the outline.** This is arguably the payload of the whole project: the
standard curve is only useful if it converts to something meaningful.
- GFP estimated as fluorescein-equivalent nM × per-instrument/per-run factor **k**
- k_Syn2 = 1.942 (lin) / 1.922 (Poly2); k_Cy3 = 0.893 / 1.573; k_Cy5 = 2.103 / 2.114
- Cy3 is the outlier — its linear and Poly2 k values diverge nearly 2× — which is itself the
  filter-compression story told a second way
- GFP tracks the dilution series with dose slope 1.05–1.14; corrected median recovery error 6–16%
- Recovery is systematically slightly **under**, not over
- Assets: **S4**, `20260618_cmp_gfp_corrected.png`, `20260618_cmp_k_by_instrument.png`,
  `20260618_cmp_gfp_track.png`, `20260609_gfp_comp.png`, tables T12/T13/T15

### 2. Model choice is not "linear fitting"
The outline says "Linear fitting". The notebook's actual finding is that **linear is inadequate
on filter reads** and Poly2-through-origin (`RFU = a·c + b·c²`) is the general answer.
- Poly2 error 0.1–17.8% vs linear 1.9–117% across all reads and curves (**T-B**)
- 4PL and 5PL were tried and rejected — unstable at the low end (CV 22–77%), over-read at the top
- Non-obvious: **on Cy5 Gext, Poly2 buys literally nothing** — identical to linear to one decimal,
  because that read is genuinely linear. Good teaching moment: fit complexity should match the
  instrument, not be applied reflexively.

### 3. Fluorescein is not photostable over a long read
- Signal drops **10–15% over a 6 h read** (7/15, Syn2)
- Within-run drift visible on 6/2 Cy5: held-out 1 µM reads 925 → 871–878 nM across t = 31→121 min
- Directly relevant to the 6 h PURE SOP; nothing in the outline warns about it
- Assets: `20260715_mfg277_stability.png`, `20260611_mfg_stability.png`, per-run `_stability` figures

### 4. Fresh vs. frozen — pre-made ladders are fine
Operational recommendation with real shipping/kitting implications, absent from the outline.
- Frozen ~1–10% low overall (2–8% on 6/18), mostly Cy5/Syn2; Cy3 flat
- Cy3 slopes: fresh-isolated 29.299 vs frozen-isolated 27.966 (−4.5%)
- Cy5 slopes: fresh-isolated 762.526 vs frozen-isolated 698.736 (−8.4%)
- Assets: **S3**, `20260618_cmp_cond_slope_ratio.png`, tables T14/T16

### 5. No well-to-well crosstalk — don't waste wells isolating standards
- Cy3 fresh-isolated 29.299 vs fresh-neighboring 29.247 → 0.2% apart
- Conclusion: "skipping wells to isolate unnecessary"
- Same assets as §4

### 6. Plate position / pipetting error is a real error source
- 6/11 Cy5: row H read 5–17% low vs rows J/L, worst mid-range (ratio 0.829 at 1000 nM)
- Did **not** recur on 7/15 (H within ~2% of J) → intermittent, likely pipetting
- This is the strongest actual argument for triplicate + a replicate-agreement check
- Assets: `20260611_mfg_rowH_qc.png`, table T11

### 7. Held-out standard recovery as a QC method
- A standard deliberately left out of the fit, then recovered, is used as the accuracy check
- MFG 1 µM (AR-910): **106%** on 6/11 (Cy5) but **85%** on 7/15 (Syn2)
- Conclusion drawn: run/read-specific, **not** a bad stock
- This is a transferable QC technique the DevNote could recommend, and it is nowhere in the outline
- Assets: `*_heldout.png` on 6/11, 6/18, 7/15; tables T10, T17

### 8. Detection floor is instrument-specific
- 6/2, same GFP dilutions: Syn2 read 0–3 of 25 timepoints above detection at 1:40k/1:400k;
  Cy3 read 25/25 at every dilution
- The outline discusses samples *above* the linear range but never the floor
- Assets: tables T4 (Syn2) vs T5 (Cy3)

### 9. The absolute anchor of the ladder doesn't matter
- 6/18 ran two independent series — A from 4000 nM, B from 3200 nM — and both land on one curve
- Non-obvious and reassuring for cross-lab use: labs need not hit identical concentrations
- Assets: `20260618_cmp_fluor_calib.png`, **S1**

### 10. Instrument sensitivity spans ~100× yet each is internally stable
- Cy3 ~43–46, Syn2 ~7–9, Cy5 ~670–785 RFU/nM; slopes hold between runs
- Cy5 Gext 4 µM ≈ 2.6 M RFU vs Syn2 G35 4 µM ≈ 31 k RFU — three orders of magnitude
- This is the cleanest one-sentence answer to "why do we need standards at all"
- Asset: **S2**

### 11. The reduced curve doesn't just cost nothing — sometimes it helps
- Cy3 filter, Poly2: 8-pt 17.8% error → 4-pt `0/500/1000/2000` 1.2%
- Because dropping the compressed 4 µM point removes the worst-behaved data
- Counterintuitive; worth stating explicitly rather than burying in a table

### 12. Narrative beats — the "lived experience" material
The outline has a bare `Narrative (?)` placeholder. These are the actual story beats:
- **The photobleaching accident (6/1):** a 30-min "come to temp" delay opened the instrument door
  instead of pre-warming, leaving the plate ~2 h at RT under light before reading. Recorded in
  the notebook as "*I'm dumb… 2 hr delay at room temp (sad) and photobleaching (extra sad)*".
  Run repeated 6/2. Best available anecdote for why protocol details matter.
- **10 µM simply did not read** (6/1) — oversaturated, no value returned. The one figure in the
  notebook with real alt text calls this out.
- **The overnight plate that worked anyway (6/22):** Cy3's 6/18 read crashed; the plate sat out in
  an open tray at RT under ambient light overnight and the rerun "looks surprisingly decent."
  Robustness evidence *and* a good story.
- **The ceiling discovery (5/20):** overlaying the ladder on historical AR-1060 MFG QC data showed
  real PURE samples sitting above the top standard — the moment the 1 µM ceiling was disproved.
- **Curve evolution #1 → #5:** 1 nM–1 µM 10-fold → widened to 10 µM (saturated) → 2-fold 7 nM–4 µM
  → 63 nM–4 µM + fresh/frozen → locked 8-pt 0–4 µM. Ready-made Figure 1.
- **Cy5 cut short on 5/20** because another user needed the instrument.

### 13. Buffer and stock details that are easy to lose
- Diluent is 100 mM sodium borate pH 9.5 — the 5/12 screen used Tris and it was switched
- GFP ladders used Tris pH 9 (different buffer from the fluorescein ladder)
- Dilutions computed against **actual 48 µM**, not nominal 50 µM
- One stock used across every date → lot is not a confounder in this dataset

### 14. Open items the notebook flags and the outline should inherit
- **Temperature dependence of fluorescein was never characterized** (explicit unchecked box)
- Cy5 G70 collected but never analyzed
- Cy3 mono-vs-filter listed as an unfinished comparison (though data exists)
- 3-point curve (100 nM → >1 µM) contemplated, never tested
- "Do we care about <100 nM?" — unresolved
- "How high do we need to go, 2 vs 4 µM?" — wants historical b.next + collaborator data
- **"How to handle the Cy3 Poly2 model robustly across labs?"** — the deepest unresolved problem:
  an instrument-specific model undercuts the cross-lab comparability the project exists to deliver
- "What's the increase in confidence if we do multiple gains with decreased sampling?"

---

# Part C — Things to resolve before drafting

1. **The outline says "Linear fitting"; the data says Poly2-through-origin.** This isn't a wording
   tweak — §2.3 needs restructuring around model choice, with linear as the special case that
   works on genuinely-linear reads.

2. **Poly2 + few points: the notebook contradicts itself.** 6/1 and 6/2 state "the poly2 fit does
   not work well with fewer samples on the curve." The June summary then recommends a 4-point
   curve, and **T-B** shows Poly2 at 0.1–6.1% error on exactly those 4-point curves. Something
   changed between those analyses; needs reconciling before either claim is published.

3. **Date inconsistency on MFG-262.** The summary timeline says 6/4; the experiment section is
   dated 6/11. Pick one.

4. **Replicate count was never a controlled variable.** "Triplicate" is recommended, but the
   evidence is the row-H incident rather than an n-vs-error experiment. Either soften the claim
   or state the reasoning as "position artifacts happen, so n≥3 lets you detect them."

5. **The 5/12 dye screen has no figures** — the fluorescein-over-GFP-over-HPTS decision is
   asserted, not shown. If §1.4 is meant to justify the choice, we may need to regenerate it.

6. **CDK / analysis code (§2.3.2) has zero source material.** Must be written from the tooling
   side; nothing in the notebooks helps.

7. **Syn2 has no fresh/frozen conditions table** (Cy3 and Cy5 do), so a clean 3-instrument slope
   table can't be assembled from the notebook as-is.

---

# Part D — Suggested outline additions

Minimal edits that would close the Part B gaps:

- **§2.3 → rename** "Linear fitting" to "Fitting the curve", with sub-nodes: model choice
  (linear / Poly2-origin / why not 4PL-5PL), over-time vs averaged, t ≥ 10 min, blanking, CDK
- **§2.4 new — "Converting to useful units"**: fluorescein-equivalent nM, the k factor, GFP
  validation, what error to expect (6–16%)
- **§2.5 new — "Making and storing standards"**: fresh vs frozen, pre-made ladders, buffer,
  actual-vs-nominal stock concentration, plate layout (no isolation needed)
- **§3.4 new — "Standard stability during the read"**: 10–15% decay over 6 h, implications for
  long timecourses
- **§3.5 new — "QC your own curve"**: held-out standard recovery, replicate/row agreement,
  detection floor, what a bad curve looks like
- **§4 expand**: temperature dependence, 3-point curve, cross-lab model portability, deGFP
  protein standards (grandparent Obj 6), microscopy standards
