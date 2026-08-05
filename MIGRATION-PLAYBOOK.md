# DevNote migration playbook

How to move a published DevNote into this repo, make it build, and get it
re-submitted — and the snags that have cost us the most time so far.

Written to support [#21](https://github.com/nucleus-eng/2026-CERN-OHL-P/issues/21)
(finish the migration programmatically). Every command here has been run against
the live site. Sources: PRs [#9](https://github.com/nucleus-eng/2026-CERN-OHL-P/pull/9),
[#13](https://github.com/nucleus-eng/2026-CERN-OHL-P/pull/13),
[#16](https://github.com/nucleus-eng/2026-CERN-OHL-P/pull/16),
[#20](https://github.com/nucleus-eng/2026-CERN-OHL-P/pull/20), and the session
notes in [`devnote-migration-status.md`](./devnote-migration-status.md).

> **Licensing gate — read first.** This repo is only for DevNotes released fully
> in the open (CC-BY or CERN-OHL-P equivalent). Deciding whether a DevNote *may*
> be included is a **human curation step**. Never automate it. Everything below
> assumes that decision is already made for the DevNote in hand.

---

## 0. The short version

```
enumerate → curate (human) → recover source → de-bloat → repair config
   → pin the CDK → execute notebooks → validate → draft → merge to main
```

Two rules that cause the most damage when broken:

1. **`curvenote submit` never re-executes a notebook.** It renders the outputs
   already saved in the `.ipynb`. Fixing code without re-running publishes the
   old, broken outputs.
2. **Do not edit collaborator prose.** In `main.md` and notebook *markdown*
   cells, the only permitted edit is a hyperlink's URL. Visible words stay
   byte-identical. Code cells and `curvenote.yml` are fair game. If prose is
   stale, say so in the PR instead of fixing it.

---

## 1. Enumerate what is published

The venue site serves machine-readable JSON. No scraping or login needed.

**Fetch every collection page.** Missing one silently hides whole groups of
DevNotes. An earlier draft of this playbook fetched three pages and reported 26
published; the real figure is 49. `index.json` alone is not enough either — it
lists only the most recent DevNotes.

```bash
# every article, with its work key, slug and title
for c in index collections-core collections-contrib collections-ai-scientist \
         collections-workshops-and-courses collections-devcell-node-chicago \
         collections-devcell-node-london; do
  curl -s -A "Mozilla/5.0" "https://devnotes.nucleus.engineering/$c.json" -o "c-$c.json"
done

python3 - <<'PY'
import json, glob
pub = {}
def walk(n):
    if isinstance(n, dict):
        if isinstance(n.get('key'), str) and 'slug' in n:
            pub[n['key']] = (n['slug'], n.get('title'))
        for v in n.values(): walk(v)
    elif isinstance(n, list):
        for v in n: walk(v)
for f in glob.glob('c-*.json'): walk(json.load(open(f)))
for k, (s, t) in sorted(pub.items(), key=lambda kv: kv[1][1] or ''):
    print(f"{str(t)[:54]:56} {s:36} {k}")
PY
```

`key` is the **work key** — the thing that must match `project.id` in the
DevNote's `curvenote.yml` for a submission to update the existing work instead
of creating a new one. `slug` is only the site URL, and the two often differ
(`bnext-devnotes-clpxp-pure-cells-01` is a slug; its key is
`nucleus-devnote-core-clpxp_module_cells-01`). **Match on key, never on slug.**

Diff that against what the repo already has, parsing the YAML properly rather
than grepping for `id:` — several `curvenote.yml` files have `id:` keys nested
under `exports:` and `authors:` that a naive regex picks up first:

```bash
python3 - <<'PY'
import glob, os, yaml
for y in sorted(glob.glob('devnotes/*/curvenote.yml')):
    pid = ((yaml.safe_load(open(y)) or {}).get('project') or {}).get('id')
    print(f"{pid or '*** NO project.id ***':52} {os.path.basename(os.path.dirname(y))}")
PY
```

As of 2026-08-05: **49 published, 22 in the repo, 30 published DevNotes not yet
migrated.** Most of the 30 sit in `Node Chicago` and `Node London`, which is
exactly why the licensing gate in §0 matters — much of it is external
contributor work.

Two lessons from getting this wrong. First, an incomplete fetch gives a
confidently wrong answer: three collection pages reported 26 published, and
nothing about the output looked suspicious. Fetch all of them, and sanity-check
that the per-collection counts add up to the total. Second, the tracker was
never a complete work list — it had 28 rows against 49 published DevNotes.
Enumerate from the site, then update
[`devnote-migration-status.md`](./devnote-migration-status.md) from that.

Also worth knowing: both rows the tracker used to mark as "likely require
contacting original authors" are published with downloadable archives. Recover
them the same way as anything else before chasing anyone by email.

---

## 2. Recover the source (MECA archive)

Every published article links a MECA computational archive containing the full
source bundle: `curvenote.yml`, `main.md`, `environment.yml`, all `toc`
notebooks, and the data files.

The download URL carries a content hash, so it cannot be guessed — read it off
the article page:

```bash
SLUG=Bhasin-20260421
curl -s -A "Mozilla/5.0" "https://devnotes.nucleus.engineering/articles/$SLUG" \
  | grep -oE 'https://pub\.curvenote\.com/[^"]+\.zip' | sort -u
```

A plain `curl` without a browser `User-Agent` gets a **403**. Some articles list
more than one zip (`curvenote_0`, `curvenote_1`); they have been identical
duplicates so far, but diff them rather than assuming.

Unzip and work from `bundle/`:

```bash
unzip -q archive.zip -d recovered && ls recovered/bundle
```

### What MECA drops

The archive is a *build product*, so it omits generated and repo-level files.
Expect to restore:

| Missing | Fix |
| --- | --- |
| `banner.webp` / `banner-2.webp` | copy from a sibling — byte-identical across all DevNotes |
| `lorem.mjs` | same |
| `LICENSE.md`, `README.md`, `.gitignore` | same |
| `base.yml` (if `extends: base.yml`) | delete the `extends:` line, inline anything it supplied |
| notebook-generated files (thumbnails, PNGs) | **do not delete the config that references them** — see §4 |

The archive reflects the last *submitted* build, which can lag the live page.
Before submitting, diff the recovered `main.md` against the live article and
confirm no later edit is being reverted. Normalize both sides first (lowercase,
strip punctuation and smart quotes) or MyST syntax like `{ref}` roles,
`:::{figure}` directives and LaTeX will produce a flood of false differences.

---

## 3. De-bloat

Bundles and bulk downloads carry the same junk every time. Survey before
deleting, and keep everything uncommitted until the trim is done so git history
stays clean.

```bash
du -h -d 1 . | sort -rh
find . -type d \( -name _build -o -name __pycache__ -o -name .ipynb_checkpoints \
  -o -name node_modules -o -name .venv -o -name .git \) -prune -exec du -sh {} \;
find . -type f \( -iname '*.tar' -o -iname '*.tar.gz' -o -iname '*.zip' \) -exec du -sh {} \;
```

Standard removals: `_build/`, `__pycache__/`, `.ipynb_checkpoints/`,
`node_modules/`, `.venv/`, per-DevNote `.git/` directories, and archives sitting
beside their own already-extracted contents.

**Vendored CDK copies.** Older DevNotes shipped a local `src/cdk/` tree and
`platereader.py` next to the notebooks, with cells doing `import platereader as
pr`. Delete the vendored copies and repoint the import at the packaged CDK
(§5). `module-Clpxp-Cells` had two 52 KB copies plus committed `.pyc` files.

**Verify before deleting.** Not every archive is a duplicate (`onepot-sy`'s
`plasmids/PURE_plasmids.tar.gz` was genuine content). Check with `tar -tzf`
first. Never delete a notebook without asking — flag orphans instead.

**Large files.** GitHub hard-blocks any file over 100 MB at push time. Check
sizes before staging; use Git LFS or external storage. `Base_Cell`'s liposome
imaging CSVs (1.6 G and 702 M) cannot be committed as plain blobs.

---

## 4. Repair `curvenote.yml`

**A missing path is not automatically a dead reference.** It may be a path a
notebook *creates* at runtime. Grep the notebooks before pruning either the file
or the config key naming it.

This cost us real time in #20: `thumbnail: "assets/thumbnail.png"` pointed at a
directory MECA had not shipped. Deleting the key as "dangling" broke the
notebook (`plt.savefig("../assets/thumbnail.png")` crashed on the missing
directory) *and* would have silently cost the DevNote its thumbnail. The fix was
`mkdir assets` and keep the key.

```bash
# every savefig target should write into a directory that exists
python3 - <<'PY'
import json, glob, os, re
for f in glob.glob('devnotes/*/**/*.ipynb', recursive=True):
    if '.ipynb_checkpoints' in f or '_build' in f: continue
    for c in json.load(open(f)).get('cells', []):
        if c.get('cell_type') != 'code': continue
        for m in re.finditer(r"savefig\(\s*[\"']([^\"']+)[\"']", "".join(c['source'])):
            p = m.group(1)
            d = os.path.normpath(os.path.join(os.path.dirname(f), os.path.dirname(p)))
            if os.path.dirname(p) and not os.path.isdir(d):
                print(f"{f} writes {p} -> missing {d}")
PY
```

**`resources:` globs.** Curvenote only uploads files matching a `resources:`
glob. A file-not-found at build time is usually a wrong glob, **not** a wrong
path in `main.md`. Check the globs before rewriting any content path — `03_mthfs`
lost a data file to `experimental/**/*` vs `experiments/**/*`. Also trim globs
pointing at directories that no longer exist after de-bloating.

**Downloads.** Confirm every `downloads:` entry resolves. `module-Clpxp-Cells`
referenced `general/clpxp-module-plasmids-01.zip`; the real file was
`general/Plasmids.zip`.

**Compute config.** Use `jupyter: true` (15 of the migrated DevNotes do). Some
recovered bundles carry a stale `thebe: binder:` block pointing at the old
`bnext-bio/nucleus-developer-notes` repo — replace it.

---

## 5. Pin the CDK

This is the single most common live-compute failure, and the subject of #17/#18.

Curvenote live compute runs **Python 3.14**. Every `toc` notebook needs a pinned
install cell as its first code cell:

```python
!pip install nucleus-cdk==0.5.0rc2 | tail -n2

# Surface a failed install here, rather than as a confusing ModuleNotFoundError
# in the import cell below.
import importlib.metadata as md
assert md.version("nucleus-cdk") == "0.5.0rc2", f"got {md.version('nucleus-cdk')}"
```

The assert matters because `| tail -n2` hides a failed install — without it the
real error surfaces much later as a baffling `ModuleNotFoundError`.

### Choosing the version

| Notebook imports | Pin | Notes |
| --- | --- | --- |
| `from cdk.analysis.cytosol import platereader as pr` | `0.5.0rc2` | the older API; what nearly every migrated DevNote uses |
| `from cdk.instruments.platereader import ...` | `0.6.0rc2` | the new API; needs `--no-deps` |

**0.6.x deleted `cdk/analysis/cytosol/platereader.py`** (it moved to
`cdk/instruments/platereader/legacy/`). Pinning an old-API notebook to 0.6.x
breaks it outright. Check the imports before choosing.

Unpinned `pip install nucleus-cdk` resolves to whatever is newest (**0.5.3** as
of 2026-08-05), which drifts on every read and may not match the API the
notebook was written against.

`--no-deps` is needed **only for 0.6.x**, which declares `pyarrow>=18,<19`;
pyarrow publishes no cp314 wheels, so a plain install fails on Python 3.14.
Verified: `0.5.0rc2` installs clean on 3.14 with all 14 dependencies, so do
**not** add `--no-deps` there — `environment.yml` does not list several of its
dependencies (scikit-learn, openpyxl, jinja2, ordered-set, jupyter-bokeh) and
skipping them breaks the import.

---

## 6. Execute the notebooks

Because submit renders saved outputs, **every notebook must be re-executed and
its outputs committed** after any code change.

```bash
python -m venv venv && ./venv/bin/pip install "nucleus-cdk==0.5.0rc2" nbclient ipykernel
```

**Never set `MPLBACKEND`.** ipykernel defaults to the `matplotlib_inline`
backend, and that backend is what captures figures as saved outputs. Forcing
`Agg` makes every notebook pass while saving **zero** figures — a green run that
publishes figure-less DevNotes. This nearly shipped in #20.

Always diff image-output counts against the pristine bundle afterwards:

```bash
python3 - <<'PY'
import json, sys
def pngs(f):
    nb = json.load(open(f))
    return sum(1 for c in nb['cells'] for o in c.get('outputs', [])
               if 'image/png' in (o.get('data') or {}))
for f in sys.argv[1:]: print(pngs(f), f)
PY
```

Also confirm no saved `output_type == "error"` remains, and spot-check that
generated PNGs are not blank. Several CDK plot helpers call `plt.show()`
internally, which closes the figure in the inline backend — a later
`plt.savefig()` then writes an *empty* image. That silently blanked
`onepot-sy`'s Figure 4. Where possible, embed figures directly from notebook
cells (`#fig:label`) rather than saving PNGs separately; that sidesteps the
failure mode entirely.

**Do not run `git checkout -- devnotes/` to clean up after a debugging run.**
That is exactly what discarded freshly-passing outputs in #13 and left stale
tracebacks baked into the committed files.

---

## 7. Validate

```bash
cd devnotes/<devnote>
npx --yes curvenote@latest check bnext-devnotes --kind devnote
```

**Typst labels cannot contain spaces.** A `:name:` or `:label:` with a space
fails the PDF export with `label <...> does not exist in the document`. Watch
for case mismatches between a label and its `{ref}` too — `fig:ClpX S` defined
against `{ref}`fig:ClpX s`` broke `module-Clpxp-Cells`, and #9 fixed six more of
these. Note `main.md` files mix `:name:` and `:label:`; grep for both.

```bash
grep -nE "^:(name|label):.*[A-Za-z0-9] +[A-Za-z0-9]" main.md   # labels with spaces
```

Known-benign messages: `Unhandled JATS conversion for node of "tabSet"` (any
DevNote using tab-sets), and `Image is too large ... to convert to webp`. When
unsure whether a message is pre-existing, run the same check against a DevNote
already merged to `main` and compare.

---

## 8. Submit

**Draft submits are cheap.** They do not reach the editor panel and do not
create venue submissions. Iterate on drafts freely.

```bash
cd devnotes/<devnote>
npx --yes curvenote@latest submit bnext-devnotes --kind devnote \
  --collection developer-cells --draft -y
```

**"Created a new work" from a local submit is expected, not a bug.** Work
resolution is scoped to the submitting account, so a personal token cannot see
or update a work owned by someone else. Confirmed by draft-submitting two
DevNotes already on `main` (`module-Clpxp-Cytosol`, `lipid-prep`) — both report
it. The key format is irrelevant.

To check which work a submit actually hit, read
`_build/logs/curvenote.submit.json`: an existing work shows its original
`work.date_created`, a duplicate shows today's date.

**The real publish path is CI.** `submit.yml` runs on push to `main` with the
venue-level `secrets.CURVENOTE_TOKEN`, which resolves works correctly.
`draft.yml` runs on PRs and posts preview links plus check results as a PR
comment — that comment is the best pre-merge signal. Use local drafts for
build/QA, and let the merge do the real submission.

Clean up afterwards: `curvenote submit` drops an untracked PDF export into each
DevNote directory per its `exports:` config. Remove them before committing.

---

## 9. Update the tracker

[`devnote-migration-status.md`](./devnote-migration-status.md) is the record.
Per DevNote: flip its status row, add a manual-review row (notebooks run /
content reviewed / submitted / build URL), and keep the counts in the section
headings honest.

"Content reviewed" means a human read `main.md` end to end. It cannot be
automated, and neither can the licensing gate in §0.

---

## 10. Snag catalogue

| Symptom | Cause | Fix |
| --- | --- | --- |
| `ModuleNotFoundError: No module named 'cdk'` in live compute | no install cell, or install silently failed | pinned install cell + version assert (§5) |
| Install cell fails on Python 3.14 | 0.6.x pulls `pyarrow`, no cp314 wheels | `--no-deps`, or pin 0.5.0rc2 |
| `ImportError` on `cdk.analysis.cytosol` | pinned to 0.6.x, which moved the module | pin 0.5.0rc2 |
| Published DevNote shows old errors after a fix | submit does not re-execute notebooks | re-run and commit outputs (§6) |
| Notebooks pass but no figures render | `MPLBACKEND` forced to `Agg` | never set it; diff PNG counts (§6) |
| Figure renders blank | CDK helper calls `plt.show()`, closing it before `savefig` | embed from the notebook cell instead |
| `devnote.pdf` export fails | space in a Typst label, or a wrong-case `{ref}` | rename the label, fix the reference (§7) |
| File-not-found at build, path looks correct | `resources:` glob does not match | fix the glob, not the path (§4) |
| Notebook crashes writing a file | a needed directory was pruned as "missing" | recreate it; check `savefig` targets (§4) |
| `Could not find static resource` in downloads | renamed or absent download target | point at the real filename (§4) |
| `No authors provided an email` | author has no `email` in `curvenote.yml` | needs a real contact — do not invent one |
| Submit creates a new work | account-scoped work resolution | expected locally; let CI submit (§8) |

---

## 11. What to automate, and what not to

Safe to automate: enumeration, MECA download and unzip, de-bloat sweeps,
install-cell rewriting, notebook execution, output/figure-count verification,
`curvenote check`, draft submission, and gap reporting against the tracker.

Keep human: **the licensing and curation decision (§0)**, content review,
deleting any notebook, inventing missing author contact details, and any edit to
collaborator prose.

A reasonable build order for #21 is one script per stage with a machine-readable
report between stages, so a failure is attributable and the curation gate has a
natural place to sit — after enumeration, before recovery.

The 30 outstanding migration targets are listed in
[`devnote-migration-status.md`](./devnote-migration-status.md). Re-run the
enumeration rather than trusting that count; it was current on 2026-08-05.
