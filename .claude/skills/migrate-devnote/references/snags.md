# Snag catalogue

Symptom → cause → fix. Most failures in this pipeline have been seen before.
Check here before diagnosing from scratch.

| Symptom | Cause | Fix |
|---|---|---|
| `ModuleNotFoundError: No module named 'cdk'` in live compute | no install cell, or the install failed silently | pinned install cell plus version assert — `prepare.md` §5 |
| Install cell fails on Python 3.14 | 0.6.x pulls `pyarrow`, which has no cp314 wheels | add `--no-deps`, or pin 0.5.0rc2 |
| `ImportError` on `cdk.analysis.cytosol` | pinned to 0.6.x, which moved the module | pin 0.5.0rc2 |
| Published DevNote still shows old errors after a fix | `submit` does not re-execute notebooks | re-run and commit outputs — `verify-submit.md` §6 |
| Notebooks pass but no figures render | `MPLBACKEND` forced to `Agg` | never set it; diff PNG counts |
| A figure renders blank | a CDK helper calls `plt.show()`, closing it before `savefig` | embed from the notebook cell instead |
| `devnote.pdf` export fails | space in a Typst label, or a wrong-case `{ref}` | rename the label, fix the reference — `verify-submit.md` §7 |
| File-not-found at build, path looks correct | `resources:` glob does not match | fix the glob, not the path — `prepare.md` §4 |
| Notebook crashes writing a file | a needed directory was pruned as "missing" | recreate it; check `savefig` targets |
| `Could not find static resource` in downloads | renamed or absent download target | point at the real filename |
| `No authors provided an email` | author has no `email` in `curvenote.yml` | needs a real contact — **do not invent one** |
| Submit reports "Created a new work" | work resolution is scoped to the submitting account | expected locally; let CI submit |
| 403 fetching an article page | no browser `User-Agent` | pass `-A "Mozilla/5.0"` |
| Enumeration finds too few DevNotes | not every collection page was fetched | fetch all of them; check counts sum |

## What to automate, and what not to

**Safe to automate:** enumeration, MECA download and unzip, de-bloat sweeps,
install-cell rewriting, notebook execution, output and figure-count
verification, `curvenote check`, draft submission, and gap reporting against the
tracker.

**Keep human:**

- **The licensing and curation decision.** Never automate it.
- Content review — a human reading `main.md` end to end.
- Deleting any notebook.
- Inventing missing author contact details.
- Any edit to collaborator prose.

A reasonable build order for issue #21 is one script per stage, with a
machine-readable report between stages. That makes a failure attributable, and
gives the curation gate a natural place to sit: after enumeration, before
recovery.

If a stage bounds its own coverage — a top-N cap, a sampling step, a skipped
retry — log what it dropped. Silent truncation reads as "covered everything"
when it did not. That is the same class of error that had the tracker reporting
26 published DevNotes when there were 49.
