# Enumerate and recover

## 1. Enumerate what is published

The venue site serves machine-readable JSON. No scraping or login needed.

**Fetch every collection page.** Missing one silently hides whole groups of
DevNotes. An earlier attempt fetched three pages and reported 26 published; the
real figure is 49. `index.json` alone is not enough either — it lists only the
most recent DevNotes.

```bash
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

`key` is the **work key**. It must match `project.id` in the DevNote's
`curvenote.yml`, or a submission creates a new work instead of updating the
existing one. `slug` is only the site URL, and the two often differ:
`bnext-devnotes-clpxp-pure-cells-01` is a slug; its key is
`nucleus-devnote-core-clpxp_module_cells-01`. **Match on key, never on slug.**

Diff that against the repo. Parse the YAML properly — several `curvenote.yml`
files have `id:` keys nested under `exports:` and `authors:` that a plain grep
matches first:

```bash
python3 - <<'PY'
import glob, os, yaml
for y in sorted(glob.glob('devnotes/*/curvenote.yml')):
    pid = ((yaml.safe_load(open(y)) or {}).get('project') or {}).get('id')
    print(f"{pid or '*** NO project.id ***':52} {os.path.basename(os.path.dirname(y))}")
PY
```

Sanity-check that the per-collection counts add up to the total. An incomplete
fetch gives a confidently wrong answer, and nothing about the output looks
suspicious.

Write the result into `devnote-migration-status.md`. Never treat that file as
the work list — it has been out of date before.

## 2. Recover the source (MECA archive)

Every published article links a MECA computational archive with the full source
bundle: `curvenote.yml`, `main.md`, `environment.yml`, all `toc` notebooks, and
the data files.

The download URL carries a content hash, so it cannot be guessed. Read it off
the article page:

```bash
SLUG=Bhasin-20260421
curl -s -A "Mozilla/5.0" "https://devnotes.nucleus.engineering/articles/$SLUG" \
  | grep -oE 'https://pub\.curvenote\.com/[^"]+\.zip' | sort -u
```

A plain `curl` without a browser `User-Agent` gets a **403**. Some articles list
more than one zip (`curvenote_0`, `curvenote_1`). They have been identical
duplicates so far, but diff them rather than assuming.

Unzip and work from `bundle/`:

```bash
unzip -q archive.zip -d recovered && ls recovered/bundle
```

### What MECA drops

The archive is a *build product*, so it omits generated and repo-level files.
Expect to restore:

| Missing | Fix |
|---|---|
| `banner.webp` / `banner-2.webp` | copy from a sibling — byte-identical across all DevNotes |
| `lorem.mjs` | same |
| `LICENSE.md`, `README.md`, `.gitignore` | same |
| `base.yml` (if `extends: base.yml`) | delete the `extends:` line, inline anything it supplied |
| notebook-generated files (thumbnails, PNGs) | **do not delete the config that references them** — see `prepare.md` |

### Check for drift

The archive reflects the last *submitted* build, which can lag the live page.
Before submitting, diff the recovered `main.md` against the live article so you
do not silently revert a later edit.

Normalize both sides first — lowercase, strip punctuation and smart quotes — or
MyST syntax like `{ref}` roles, `:::{figure}` directives and LaTeX produces a
flood of false differences.
