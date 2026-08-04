#!/bin/bash
set -uo pipefail
# Deliberately not `set -e` - keep going after a failure so we get a
# full pass/fail summary across every devnote, not just the first one.

# Submits a DRAFT for every devnote currently in devnotes/ (any directory
# with a curvenote.yml), directly via the curvenote CLI - no git commits,
# no GitHub Actions. Matches Anton's documented manual-submit command
# (same venue/kind/collection as draft.yml/submit.yml), run from inside
# each devnote's own directory.
#
# Uses --draft on purpose - this is for review/QA (getting a build/preview
# link per devnote to manually check notebooks-ran/content/etc against),
# not for real curator-visible submissions. Use a separate, deliberate
# run without --draft when you actually want to submit for real.
#
# Requires `curvenote token set` already run in this shell/machine.
# Uses curvenote@latest explicitly - `submit` enforces a minimum CLI
# version (0.14.2+) that plain `npx curvenote` (which can resolve to an
# older cached/pinned version) doesn't always satisfy.
#
# Runs devnotes concurrently (default 6 at a time, override with
# CONCURRENCY=n) via xargs -P - each submission is an independent CLI
# invocation in its own directory, so there's no shared state to race on
# beyond npx's package cache, which is already warm after the first call.
#
# Run from anywhere inside a clone of nucleus-eng/2026-CERN-OHL-P.
# Written for bash 3.2 (macOS default) - no associative arrays.

REPO_ROOT="$(git rev-parse --show-toplevel)"
cd "$REPO_ROOT"

CONCURRENCY="${CONCURRENCY:-6}"

DEVNOTES=()
for path in devnotes/*/; do
  d="${path%/}"
  d="${d#devnotes/}"
  if [ -f "devnotes/$d/curvenote.yml" ]; then
    DEVNOTES+=("$d")
  fi
done

echo "Found ${#DEVNOTES[@]} devnotes: ${DEVNOTES[*]} (concurrency=$CONCURRENCY)"

RESULTS_DIR="$(mktemp -d "${TMPDIR:-/tmp}/curvenote-submit-XXXXXX")"
trap 'rm -rf "$RESULTS_DIR"' EXIT

submit_one() {
  d="$1"
  path="devnotes/$d"
  logfile="$path/_build/logs/curvenote.submit.json"
  outlog="$RESULTS_DIR/$d.log"
  rm -f "$logfile"
  (
    cd "$path"
    npx --yes curvenote@latest submit bnext-devnotes --kind devnote --collection developer-cells --draft -y
  ) >"$outlog" 2>&1
  rc=$?
  url=""
  if [ -f "$logfile" ]; then
    url=$(python3 -c "import json;print(json.load(open('$logfile')).get('buildUrl',''))" 2>/dev/null)
  fi
  status="OK"
  [ $rc -eq 0 ] || status="FAILED"
  printf '%s\t%s\t%s\n' "$d" "$status" "$url" >"$RESULTS_DIR/$d.result"
  echo
  echo "==================== $d: $status ===================="
  cat "$outlog"
}
export -f submit_one
export RESULTS_DIR

printf '%s\n' "${DEVNOTES[@]}" | xargs -P "$CONCURRENCY" -I{} bash -c 'submit_one "$@"' _ {}

echo
echo "==================== Summary ===================="
for d in "${DEVNOTES[@]}"; do
  if [ -f "$RESULTS_DIR/$d.result" ]; then
    IFS=$'\t' read -r name status url <"$RESULTS_DIR/$d.result"
    printf "%-30s %-8s %s\n" "$name" "$status" "$url"
  else
    printf "%-30s %-8s %s\n" "$d" "MISSING" ""
  fi
done
